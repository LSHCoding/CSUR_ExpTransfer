## Tokenized-to-Latent Experience Transformation

第三类转化路径是 **Tokenized-to-Latent Experience Transformation**，即将 tokenized agent experience 转化为可被模型直接消费的连续表示，例如 KV cache、hidden states、soft prompt、prefix vectors、memory token embeddings、latent memory bank、recurrent memory state 或 cross-attention memory output。这里的源经验通常来自 agent 在序贯决策过程中产生的 reasoning trace、tool-use history、multi-turn interaction、robot execution trajectory、GUI operation record、visual observation history、demonstration 或 task procedure。这些经验原本可以被表示为 narrative tokenized artifact 或 schematic tokenized artifact，但在 P3 中，它们进一步被编码、蒸馏或组织为 latent carrier，并在后续推理中直接参与 attention、hidden-state computation 或 action prediction。

P3 的核心不是一般意义上的“上下文压缩”，而是**经验载体层级的变化**。源经验处于 tokenized 层，具有较强的可读性、可编辑性和可检索性；目标经验则处于 latent 层，具有更高的推理效率和更强的模型内部耦合性，但可解释性和可编辑性相对更弱。换言之，P3 关注的是 agent 如何把过去交互中形成的经验语义，从离散 token artifact 转化为连续计算状态，使未来决策不再通过阅读文本经验来复用过去，而是直接在模型内部状态空间中消费这些经验。

因此，P3 与标准 RAG-style memory 有明确区别。在 RAG-style memory 中，历史经验可以被 embedding model 编码为向量并用于相似度检索，但最终被模型消费的通常仍是 retrieved text。检索出的文本片段会被重新 tokenized，并作为 prompt 的一部分进入模型。此时，embedding 只是索引机制，而不是最终被复用的经验载体。相反，P3 要求转化后的经验以 continuous representation 的形式直接进入 attention 或 hidden-state computation，而不是被解码回自然语言或其他离散 token 后再输入模型。

P3 也不同于单纯的 inference efficiency optimization。许多 KV cache eviction、attention sparsification、cache quantization、prompt caching 或 serving-level cache reuse 方法同样操作 KV cache 或 hidden states，但其目标主要是降低单次请求的显存占用、延迟或吞吐成本，并不一定具有跨 turn、跨 session、跨 task、跨 skill 或长程 episode 的经验复用语义。本文只将那些明确把历史交互、任务示范、轨迹或环境反馈转化为可复用 latent artifact 的方法纳入 P3。换言之，P3 中的 latent representation 必须承担经验存储与复用功能，而不能只是推理系统中的临时加速结构。

由于不同论文使用 cache、soft prompt、memory token、latent memory、episodic memory、scene memory 等术语时侧重点不同，本文不按照表面名称组织 P3 方法。相反，我们按照 tokenized experience 被转化为 latent experience 的机制，将 P3 方法划分为三类：**Cache-Based Latent Transformation** 直接复用历史 forward pass 所产生的内部计算；**Prompt-Based Latent Transformation** 将经验蒸馏为可训练的连续提示表示；**Module-Based Latent Transformation** 则通过显式记忆模块、记忆库、压缩器、读取器或循环状态来动态组织和维护 latent memory。

### Cache-Based Latent Transformation

**Cache-Based Latent Transformation** 指的是将历史交互过程中产生的 KV cache、hidden states 或其他 attention-level computation 保存下来，并在后续任务或后续时间步中直接复用。这里的核心思想是，agent 的历史经验不仅存在于可读的 trajectory log 或 reasoning trace 中，也已经被模型在处理这些 tokenized experience 时编码进内部连续状态。与其在未来任务中重新读取文本日志并再次计算，系统可以直接复用过去 forward pass 中形成的 latent computation，从而把历史计算状态本身转化为经验载体。

这类方法通常以 raw trajectory、reasoning log、multi-turn context 或 visual-action history 为输入。当模型处理这些输入时，会在每一层 attention 中产生对应的 key-value states 或 hidden representations。系统将其中与经验复用相关的部分保存为 latent memory，并在后续遇到相关任务、相似 query 或相邻时间步时，将这些 cached states 检索出来，经过位置校正、拼接、重排或选择性注入后，与当前输入一起参与 attention computation。代表性方法包括将 reasoning logs 转化为 reusable KV computation 的 Log-Augmented Generation，以及在 long-horizon VLA manipulation 中维护 layer-wise temporal KV memory 的 TempoFit。

这一路径的关键在于，经验不是被重新训练成新的参数，也不是被总结成新的文本 artifact，而是以历史计算缓存的形式被保留下来。对于长推理链、复杂工具调用轨迹或多步视觉-动作交互而言，历史 forward computation 中可能已经包含了大量关于上下文约束、动作选择、子任务进展和环境反馈的隐式编码。Cache-Based Latent Transformation 试图直接复用这些计算结果，使 agent 能够在未来决策中继承过去的计算过程，而不是从头重建经验语义。

这类方法的优势是训练成本低、信息保真度高，并且能够充分利用模型已经完成的计算。相比 narrative reflection 或 textual summary，KV cache 能够保留更细粒度的 token-level 或 layer-level 信息；相比 soft prompt 或 memory module，它通常不需要额外训练，因而更容易作为 plug-and-play mechanism 接入已有模型。对于那些过去推理过程较长、重复计算成本较高、且历史任务与当前任务存在明显关联的场景，cache-based transformation 可以提供一种高效的 latent experience reuse 方式。

然而，这类方法也存在明显限制。首先，KV cache 与具体模型结构、layer layout、position encoding 和 attention implementation 强耦合，跨模型迁移能力较弱。其次，历史 KV states 的容量开销通常较大，需要配套设计选择、检索、压缩、淘汰和位置对齐机制。再次，cached latent states 的语义可解释性较低，用户难以像编辑文本记忆那样直接修正其中的错误经验。最后，这类方法与普通 KV-cache efficiency 方法之间存在边界风险。只有当缓存被明确用于跨次或长程经验复用时，它才属于 P3；如果缓存只是为了减少单次请求的计算成本，则不应归入 Tokenized-to-Latent Experience Transformation。

论文：
- Log-Augmented Generation: Scaling Test-Time Reasoning with Reusable Computation
- TempoFit: Plug-and-Play Layer-Wise Temporal KV Memory for Long-Horizon Vision-Language-Action Manipulation
- Memorizing Transformers

### Prompt-Based Latent Transformation

**Prompt-Based Latent Transformation** 指的是通过训练将 demonstrations、reasoning traces、task procedures、stage-level skills 或其他 tokenized experience 转化为 soft prompt、prefix vectors、prefix KV 或 memory token embeddings 等连续提示表示。推理时，这些 latent prompts 被插入模型的 embedding space、prefix attention states 或特殊 memory token 位置中，直接影响模型的 generation、reasoning 或 action prediction，而不是作为自然语言 prompt 被读取。

这类方法的基本思想是，许多经验的复用不一定需要保留完整历史轨迹。对于稳定的 reasoning pattern、tool-use procedure、robotic manipulation stage 或 task-specific skill，经验的核心作用是改变模型在某类上下文中的行为倾向。Prompt-Based Latent Transformation 通过优化少量外部连续向量，将这些经验语义压缩为可加载、可复用的 latent prompt，使模型在不显著更新底座权重的情况下获得某种 task-specific 或 skill-specific adaptation。

在具体机制上，这类方法通常以 demonstrations、procedure-response pairs、reasoning examples 或 stage-level trajectories 为训练数据，冻结或基本冻结底座模型，仅训练 soft prompt、prefix KV 或 memory token embeddings。训练目标可以是让模型在 latent prompt 条件下复现正确的 reasoning process、输出期望答案、调用合适工具，或产生正确的机器人动作。代表性方法包括将 manipulation demonstrations 蒸馏为 memory prompts 的 MAP-VLA，将 reasoning demonstrations 压缩为 learned prefix KV 的 ReasonCACHE，以及将 reusable procedure 编码进 one-token memory embedding 的 TokMem。

Prompt-Based Latent Transformation 与 P5 中的 policy parameter internalization 有重要区别。P5 是将经验写入模型的 policy parameters，使底座模型本身发生能力内化；而在 Prompt-Based Latent Transformation 中，经验主要存在于外部 soft prompt、prefix 或 memory token 中，底座模型通常保持冻结。因而，这类方法可以被看作介于 textual prompting 与 full fine-tuning 之间的轻量经验转化方式。它比文本 prompt 更紧凑，也不受自然语言上下文长度的直接限制；同时又比参数微调更模块化，便于按任务、技能或场景加载不同的 latent prompts。

这类方法的优势在于压缩率高、部署灵活，并且适合承载边界相对清晰、重复性较强的经验。例如，某类数学推理模式、固定工具调用流程、机器人操作阶段或程序性任务规则，都可以被训练成相对稳定的 latent prompt。由于这些 latent artifacts 通常与主模型参数分离，它们也有可能形成可检索、可组合或可路由的经验单元，从而支持多技能或多任务场景下的经验复用。

但 Prompt-Based Latent Transformation 也有局限。首先，soft prompt 或 memory token 的可解释性较弱，用户难以直接观察其内部存储了哪些经验语义。其次，其泛化能力高度依赖训练数据覆盖范围；如果 demonstrations 过窄，latent prompt 可能只捕捉局部模式，而难以迁移到显著不同的任务。再次，这类 latent prompts 与特定模型的 embedding space 和 attention mechanism 强耦合，跨模型复用并不直接。最后，极端压缩形式虽然高效，但也可能带来容量不足、语义混叠和错误经验难以定位的问题。因此，这类方法更适合承载稳定、可重复、粒度相对明确的经验，而不适合作为开放式长期记忆的唯一机制。

论文：
- MAP-VLA: Memory-Augmented Prompting for Vision-Language-Action Model in Robotic Manipulation
- ReasonCACHE: Teaching LLMs To Reason Without Weight Updates
- TokMem: One-Token Procedural Memory for Large Language Models

### Module-Based Latent Transformation

**Module-Based Latent Transformation** 指的是通过显式 memory module、memory bank、compressor、composer、cross-attention reader、recurrent state、scene memory 或 structured memory graph，将历史经验动态转化、组织、读取和更新为 latent memory。与 Cache-Based Latent Transformation 不同，这类方法并不只是保存历史 forward pass 中产生的原始 KV states；与 Prompt-Based Latent Transformation 不同，它们的经验表示也不是一组相对固定的 soft prompts。相反，这类方法通常构建一个更完整的 latent memory system，使 agent 能够根据当前 context、历史轨迹、视觉状态、agent role 或任务进程动态访问和整合经验。

这类方法的基本思想是，复杂 agent 任务中的经验往往是长程的、多模态的、动态变化的，并且具有内部结构。单纯复用历史 KV cache 可能难以控制容量和更新；固定 soft prompt 也难以表达不断变化的 scene state、episodic history、multi-agent context 或 GUI interaction progress。因此，Module-Based Latent Transformation 引入专门的记忆结构，将历史 observation、action、reasoning trace、visual perception、robot state 或 interaction outcome 编码为可被查询、融合和更新的 latent memory entries。

在这类方法中，经验复用通常包含显式的写入、读取和融合过程。写入阶段，系统将历史轨迹、多轮交互、视觉观察、动作反馈或 agent-specific context 编码为 latent entries，并存入 memory bank、episodic buffer、scene memory 或 structured memory graph。读取阶段，当前 query、task state、visual observation、agent role representation 或 policy hidden state 会作为查询信号，从 memory 中选择相关经验。融合阶段，被读取的 latent memory 通过 cross-attention、gating、residual connection、state update、decision-state readout 或 action-conditioning mechanism 影响后续 generation 或 action prediction。

代表性方法包括 LatentMem、Dual Latent Memory for Visual Multi-agent System、MemoryVLA、Gated Memory Policy、HAMLET、Chameleon、EchoVLA 和 Hybrid Self-evolving Structured Memory for GUI Agents。这些方法的具体结构并不完全相同：有些侧重于 composer 或 compressor，根据检索到的历史经验和 agent context 生成 compact latent memory；有些构建 perceptual-cognitive memory bank 或 dual latent memory，以保存视觉感知、推理过程或多智能体通信信息；有些维护 recurrent memory state、episodic state 或 scene memory，使 agent 在 long-horizon interaction 中持续更新历史状态；还有一些将 latent memory 与 GUI graph、task structure 或 textual guidance 结合，形成 hybrid memory system。

尽管内部设计多样，这些方法的共同点是：经验复用依赖显式的 latent memory architecture，而不是单纯的文本检索、固定 latent prompt 或原始 KV cache 复用。换言之，Module-Based Latent Transformation 不仅关注如何把 tokenized experience 编码为 latent vectors，还关注这些 latent vectors 如何被存储、索引、组合、更新、遗忘和注入决策过程。它更接近一种系统级 memory mechanism，而不是单一的压缩操作。

这类方法特别适合 long-horizon、multi-modal、embodied、GUI 和 multi-agent 场景。在机器人操控、移动操作、视觉多智能体系统和 GUI 自动化中，经验通常包含大量难以完全语言化的视觉细节、空间关系、动作后果、环境状态和时间依赖。如果只将这些经验总结成文本，可能会丢失关键的 perceptual grounding；如果只使用短期上下文，agent 又难以在长程任务中维持一致的目标和状态。Module-Based Latent Transformation 通过持续维护和动态访问 latent memory，使 agent 能够将过去的观察、动作和反馈整合进当前决策。

这类方法的优势是表达能力强、动态适应性好，并且能够将 memory access 与当前决策紧密耦合。相比 fixed latent prompt，它可以根据当前任务状态选择不同历史经验；相比 raw KV reuse，它可以引入更明确的写入、读取、压缩、门控、更新和遗忘机制；相比 textual memory，它能够保留更多视觉、空间和动作层面的细节。因此，它通常是 P3 中最适合复杂长程 agent 的方法形态。

然而，Module-Based Latent Transformation 的系统复杂度也最高。它往往需要额外的 memory module、cross-attention layer、compressor、gating mechanism、scene encoder 或 action-conditioning architecture，训练和部署成本较高。由于 memory representation 与环境、感知编码器、任务分布和 policy architecture 深度耦合，跨任务和跨模型迁移仍然具有挑战。此外，持续更新 latent memory 会带来 staleness、capacity saturation、latent drift、错误经验累积和 memory interference 等问题。如果缺乏有效的 selection、consolidation、aging、verification 或 reset 机制，历史经验可能不仅不能帮助当前决策，反而会成为干扰源。因此，在 P3 路径中，Module-Based Latent Transformation 可以被视为表达能力最强、但稳定性与工程复杂度挑战也最高的一类方法。

论文：
- LatentMem: Customizing Latent Memory for Multi-Agent Systems
- Dual Latent Memory for Visual Multi-agent System
- MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation
- Gated Memory Policy
- HAMLET: Switch your Vision-Language-Action Model into a History-Aware Policy
- Chameleon: Episodic Memory for Long-Horizon Robotic Manipulation
- EchoVLA: Synergistic Declarative Memory for VLA-Driven Mobile Manipulation
- Hybrid Self-evolving Structured Memory for GUI Agents