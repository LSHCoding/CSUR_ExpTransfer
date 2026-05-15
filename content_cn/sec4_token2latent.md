## Tokenized-to-Latent Experience Transformation

**Tokenized-to-Latent Experience Transformation** 将 tokenized agent experience 转化为可被模型直接消费的连续表示：KV cache、hidden states、soft prompt、prefix vectors、memory token embeddings、latent memory bank、recurrent memory state 或 cross-attention memory output。源经验来自 agent 序贯决策中产生的 reasoning trace、tool-use history、multi-turn interaction、robot execution trajectory、GUI operation record、visual observation history、demonstration 或 task procedure。这些经验原本可被表示为 narrative 或 schematic tokenized artifact，但在 P3 中，它们进一步被编码、蒸馏或组织为 latent carrier，在后续推理中直接参与 attention、hidden-state computation 或 action prediction。

P3 的核心不是一般意义上的”上下文压缩”，而是经验载体层级的变化。源经验处于 tokenized 层，具有较强的可读性、可编辑性和可检索性；目标经验处于 latent 层，推理效率更高、模型内部耦合性更强，但可解释性和可编辑性相对更弱。P3 关注的是 agent 如何把过去交互中形成的经验语义从离散 token artifact 转化为连续计算状态，使未来决策不再通过阅读文本经验来复用过去，而是直接在模型内部状态空间中消费这些经验。

P3 与标准 RAG-style memory 有明确区别。RAG-style memory 中，历史经验被 embedding model 编码为向量用于相似度检索，但最终被模型消费的通常是 retrieved text——文本片段被重新 tokenized 后作为 prompt 的一部分进入模型，embedding 只是索引机制，而非最终被复用的经验载体。P3 要求转化后的经验以 continuous representation 的形式直接进入 attention 或 hidden-state computation，不被解码回自然语言或其他离散 token 后再输入模型。

P3 也不同于单纯的 inference efficiency optimization。许多 KV cache eviction、attention sparsification、cache quantization、prompt caching 或 serving-level cache reuse 方法同样操作 KV cache 或 hidden states，但其目标主要是降低单次请求的显存占用、延迟或吞吐成本，并不一定具有跨 turn、跨 session、跨 task、跨 skill 或长程 episode 的经验复用语义。本文只将那些明确把历史交互、任务示范、轨迹或环境反馈转化为可复用 latent artifact 的方法纳入 P3——latent representation 必须承担经验存储与复用功能，而非仅是推理系统中的临时加速结构。

不同论文以 cache、soft prompt、memory token、latent memory、episodic memory、scene memory 等术语指代不同机制，本文不按表面名称组织，而是按 tokenized experience 转化为 latent experience 的机制将 P3 方法划分为三类：**Cache-Based Latent Transformation** 直接复用历史 forward pass 产生的内部计算；**Prompt-Based Latent Transformation** 将经验蒸馏为可训练的连续提示表示；**Module-Based Latent Transformation** 通过显式 memory module、memory bank、compressor、reader 或循环状态动态组织和维护 latent memory。

### Cache-Based Latent Transformation

**Cache-Based Latent Transformation** 将历史交互过程中产生的 KV cache、hidden states 或其他 attention-level computation 保存下来，在后续任务或后续时间步中直接复用。其核心思想是：agent 的历史经验不仅存在于可读的 trajectory log 或 reasoning trace 中，也已被模型在处理这些 tokenized experience 时编码进内部连续状态。系统可以直接复用过去 forward pass 中形成的 latent computation，把历史计算状态本身转化为经验载体，而非在未来任务中重新读取文本日志并再次计算。

这类方法以 raw trajectory、reasoning log、multi-turn context 或 visual-action history 为输入。模型处理这些输入时，在每层 attention 中产生对应的 key-value states 或 hidden representations。系统将与经验复用相关的部分保存为 latent memory，在后续遇到相关任务、相似 query 或相邻时间步时，将这些 cached states 检索出来，经过位置校正、拼接、重排或选择性注入后，与当前输入一起参与 attention computation。代表性方法包括将 reasoning logs 转化为 reusable KV computation 的 Log-Augmented Generation，以及在 long-horizon VLA manipulation 中维护 layer-wise temporal KV memory 的 TempoFit。

这一路径的关键在于，经验既不被重新训练成新的参数，也不被总结成新的文本 artifact，而是以历史计算缓存的形式保留。对于长推理链、复杂工具调用轨迹或多步视觉-动作交互，历史 forward computation 中可能已包含大量关于上下文约束、动作选择、子任务进展和环境反馈的隐式编码。Cache-Based Latent Transformation 直接复用这些计算结果，使 agent 在未来决策中继承过去的计算过程。

这类方法的优势是训练成本低、信息保真度高，能充分利用模型已完成的计算。相比 narrative reflection 或 textual summary，KV cache 保留更细粒度的 token-level 或 layer-level 信息；相比 soft prompt 或 memory module，它通常不需额外训练，更容易作为 plug-and-play mechanism 接入已有模型。对过去推理过程较长、重复计算成本较高、且历史任务与当前任务存在明显关联的场景，cache-based transformation 提供了一种高效的 latent experience reuse 方式。

限制也同样存在。KV cache 与具体模型结构、layer layout、position encoding 和 attention implementation 强耦合，跨模型迁移能力较弱。历史 KV states 的容量开销较大，需要配套设计选择、检索、压缩、淘汰和位置对齐机制。cached latent states 的语义可解释性较低，用户难以像编辑文本记忆那样直接修正错误经验。此外，这类方法与普通 KV-cache efficiency 方法存在边界风险：只有当缓存被明确用于跨次或长程经验复用时，才属于 P3；若仅为减少单次请求的计算成本，则不应归入 Tokenized-to-Latent Experience Transformation。

论文：
- Log-Augmented Generation: Scaling Test-Time Reasoning with Reusable Computation
- TempoFit: Plug-and-Play Layer-Wise Temporal KV Memory for Long-Horizon Vision-Language-Action Manipulation
- Memorizing Transformers

### Prompt-Based Latent Transformation

**Prompt-Based Latent Transformation** 通过训练将 demonstrations、reasoning traces、task procedures、stage-level skills 或其他 tokenized experience 转化为 soft prompt、prefix vectors、prefix KV 或 memory token embeddings 等连续提示表示。推理时，这些 latent prompts 被插入模型的 embedding space、prefix attention states 或特殊 memory token 位置，直接影响模型的 generation、reasoning 或 action prediction，而非作为自然语言 prompt 被读取。

许多经验的复用不必保留完整历史轨迹。对于稳定的 reasoning pattern、tool-use procedure、robotic manipulation stage 或 task-specific skill，经验的核心作用是改变模型在某类上下文中的行为倾向。Prompt-Based Latent Transformation 通过优化少量外部连续向量，将这些经验语义压缩为可加载、可复用的 latent prompt，使模型在不显著更新底座权重的情况下获得 task-specific 或 skill-specific adaptation。

在具体机制上，这类方法以 demonstrations、procedure-response pairs、reasoning examples 或 stage-level trajectories 为训练数据，冻结或基本冻结底座模型，仅训练 soft prompt、prefix KV 或 memory token embeddings。训练目标可以是让模型在 latent prompt 条件下复现正确的 reasoning process、输出期望答案、调用合适工具，或产生正确的机器人动作。代表性方法包括将 manipulation demonstrations 蒸馏为 memory prompts 的 MAP-VLA，将 reasoning demonstrations 压缩为 learned prefix KV 的 ReasonCACHE，以及将 reusable procedure 编码进 one-token memory embedding 的 TokMem。

Prompt-Based Latent Transformation 与 P5 中的 policy parameter internalization 有重要区别。P5 将经验写入模型的 policy parameters，使底座模型本身发生能力内化；而 Prompt-Based Latent Transformation 中，经验主要存在于外部 soft prompt、prefix 或 memory token 中，底座模型通常保持冻结。这类方法可看作介于 textual prompting 与 full fine-tuning 之间的轻量经验转化方式：比文本 prompt 更紧凑，不受自然语言上下文长度的直接限制；同时又比参数微调更模块化，便于按任务、技能或场景加载不同的 latent prompts。

这类方法的优势在于压缩率高、部署灵活，适合承载边界相对清晰、重复性较强的经验——某类数学推理模式、固定工具调用流程、机器人操作阶段或程序性任务规则，都可被训练成相对稳定的 latent prompt。由于这些 latent artifacts 通常与主模型参数分离，它们有可能形成可检索、可组合或可路由的经验单元，支持多技能或多任务场景下的经验复用。

局限也不容忽视。soft prompt 或 memory token 的可解释性较弱，用户难以直接观察其内部存储了哪些经验语义。泛化能力高度依赖训练数据覆盖范围：若 demonstrations 过窄，latent prompt 可能只捕捉局部模式。这类 latent prompts 与特定模型的 embedding space 和 attention mechanism 强耦合，跨模型复用并不直接。极端压缩虽高效，但可能带来容量不足、语义混叠和错误经验难以定位的问题。这类方法更适合承载稳定、可重复、粒度相对明确的经验，不宜作为开放式长期记忆的唯一机制。

论文：
- MAP-VLA: Memory-Augmented Prompting for Vision-Language-Action Model in Robotic Manipulation
- ReasonCACHE: Teaching LLMs To Reason Without Weight Updates
- TokMem: One-Token Procedural Memory for Large Language Models

### Module-Based Latent Transformation

**Module-Based Latent Transformation** 通过显式 memory module、memory bank、compressor、composer、cross-attention reader、recurrent state、scene memory 或 structured memory graph，将历史经验动态转化、组织、读取和更新为 latent memory。与 Cache-Based Latent Transformation 不同，这类方法不只是保存历史 forward pass 中产生的原始 KV states；与 Prompt-Based Latent Transformation 不同，其经验表示也不是一组相对固定的 soft prompts。这类方法构建的是一个更完整的 latent memory system，使 agent 能根据当前 context、历史轨迹、视觉状态、agent role 或任务进程动态访问和整合经验。

复杂 agent 任务中的经验往往是长程的、多模态的、动态变化的，且具有内部结构。单纯复用历史 KV cache 难以控制容量和更新；固定 soft prompt 也难以表达不断变化的 scene state、episodic history、multi-agent context 或 GUI interaction progress。Module-Based Latent Transformation 引入专门的记忆结构，将历史 observation、action、reasoning trace、visual perception、robot state 或 interaction outcome 编码为可被查询、融合和更新的 latent memory entries。

经验复用通常包含显式的写入、读取和融合过程。写入阶段，系统将历史轨迹、多轮交互、视觉观察、动作反馈或 agent-specific context 编码为 latent entries，存入 memory bank、episodic buffer、scene memory 或 structured memory graph。读取阶段，当前 query、task state、visual observation、agent role representation 或 policy hidden state 作为查询信号，从 memory 中选择相关经验。融合阶段，被读取的 latent memory 通过 cross-attention、gating、residual connection、state update、decision-state readout 或 action-conditioning mechanism 影响后续 generation 或 action prediction。

代表性方法包括 LatentMem、Dual Latent Memory for Visual Multi-agent System、MemoryVLA、Gated Memory Policy、HAMLET、Chameleon、EchoVLA 和 Hybrid Self-evolving Structured Memory for GUI Agents。这些方法的具体结构各异：有些侧重于 composer 或 compressor，根据检索到的历史经验和 agent context 生成 compact latent memory；有些构建 perceptual-cognitive memory bank 或 dual latent memory，保存视觉感知、推理过程或多智能体通信信息；有些维护 recurrent memory state、episodic state 或 scene memory，使 agent 在 long-horizon interaction 中持续更新历史状态；还有一些将 latent memory 与 GUI graph、task structure 或 textual guidance 结合，形成 hybrid memory system。

尽管内部设计多样，这些方法的共同点是经验复用依赖显式的 latent memory architecture，而非单纯的文本检索、固定 latent prompt 或原始 KV cache 复用。Module-Based Latent Transformation 不仅关注如何把 tokenized experience 编码为 latent vectors，还关注这些 latent vectors 如何被存储、索引、组合、更新、遗忘和注入决策过程——它更接近系统级 memory mechanism，而非单一的压缩操作。

这类方法特别适合 long-horizon、multi-modal、embodied、GUI 和 multi-agent 场景。在机器人操控、移动操作、视觉多智能体系统和 GUI 自动化中，经验通常包含大量难以完全语言化的视觉细节、空间关系、动作后果、环境状态和时间依赖。若只将这些经验总结成文本，可能丢失关键的 perceptual grounding；若只使用短期上下文，agent 难以在长程任务中维持一致的目标和状态。Module-Based Latent Transformation 通过持续维护和动态访问 latent memory，使 agent 能够将过去的观察、动作和反馈整合进当前决策。

这类方法的优势是表达能力强、动态适应性好，能将 memory access 与当前决策紧密耦合。相比 fixed latent prompt，它可根据当前任务状态选择不同历史经验；相比 raw KV reuse，它可引入更明确的写入、读取、压缩、门控、更新和遗忘机制；相比 textual memory，它能够保留更多视觉、空间和动作层面的细节。它是 P3 中最适合复杂长程 agent 的方法形态。

系统复杂度也最高。它往往需要额外的 memory module、cross-attention layer、compressor、gating mechanism、scene encoder 或 action-conditioning architecture，训练和部署成本较高。memory representation 与环境、感知编码器、任务分布和 policy architecture 深度耦合，跨任务和跨模型迁移仍具挑战。持续更新 latent memory 会带来 staleness、capacity saturation、latent drift、错误经验累积和 memory interference 等问题。若缺乏有效的 selection、consolidation、aging、verification 或 reset 机制，历史经验不仅不能帮助当前决策，反而成为干扰源。在 P3 路径中，Module-Based Latent Transformation 是表达能力最强、但稳定性与工程复杂度挑战也最高的一类方法。

论文：
- LatentMem: Customizing Latent Memory for Multi-Agent Systems
- Dual Latent Memory for Visual Multi-agent System
- MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation
- Gated Memory Policy
- HAMLET: Switch your Vision-Language-Action Model into a History-Aware Policy
- Chameleon: Episodic Memory for Long-Horizon Robotic Manipulation
- EchoVLA: Synergistic Declarative Memory for VLA-Driven Mobile Manipulation
- Hybrid Self-evolving Structured Memory for GUI Agents


```
## Tokenized-to-Latent Experience Transformation

Tokenized-to-Latent Experience Transformation 关注的是一种更深层的经验复用方式：agent 不再主要通过重新阅读 textual memory、trajectory log 或 demonstration artifact 来调用过去经验，而是将这些原本存在于 tokenized carrier 中的经验语义进一步转化为可被模型直接消费的 continuous representation。这里的目标载体可以是 KV cache、hidden states、soft prompt、prefix KV、memory token embedding、latent memory bank、recurrent memory state 或 cross-attention memory output；共同点在于，经验在复用时不再回到自然语言或其他离散 token 形式，而是直接进入 attention、hidden-state update 或 action prediction 的内部计算。

这一 transformation pathway 与常见的 RAG-style memory 有本质区别。后者虽然也常用 embedding 做索引，但最终被模型消费的通常仍是 retrieved text；embedding 只是检索机制，而不是经验真正被复用的载体。P3 关心的则是 tokenized experience 如何被编码、蒸馏或组织为 latent carrier，并在后续决策中以 model-native state 的形式被再次调用。它也不同于单纯的 inference efficiency optimization：只有当 KV states、hidden states 或其他 latent structure 被明确用于跨 step、跨 turn、跨 episode 或跨 task 的经验存储与继承时，这类方法才属于 Tokenized-to-Latent transformation，而非普通的 caching 或 serving trick。

从机制上看，这一路径大致可以分为三类。第一类方法直接复用历史交互已经产生的内部计算，将过去 forward pass 的结果保留下来，形成 cache-based latent experience。第二类方法将 demonstrations、reasoning traces 或 procedures 压缩为可训练的连续提示，使经验以 soft prompt、prefix 或 memory token 的形式被重复加载。第三类方法则构建更完整的 latent memory architecture，通过显式 memory module、memory bank 或 recurrent state 对历史经验进行持续写入、读取、更新与融合。三类方法在表达能力、训练成本、部署灵活性与可解释性上各有取舍，也共同勾勒出 tokenized experience 向 latent carrier 迁移的连续谱。

### Cache-Based Latent Transformation

Cache-Based Latent Transformation 的核心思想，是将历史经验视为已经完成过的内部计算，并直接复用这些计算产生的 latent states，而不是把经验重新组织成文本后再送入模型。其经验来源通常仍是 reasoning log、multi-turn interaction、visual-action history 或其他 tokenized trajectory，但方法真正保存和继承的是这些轨迹在模型前向传播中形成的 KV states 或 hidden representations。

这一方向的机制前驱可以追溯到 Memorizing Transformers [Wu22]。该方法将长序列中先前 token 在中间层形成的 key value 对写入外部 memory，并在后续时间步通过 kNN 检索重新接入 attention，说明 tokenized context 可以被转化为可直接参与后续 hidden-state computation 的 latent memory。虽然该工作并非 agent-centric memory 设计，但它清楚展示了“离散序列先编码为 latent state，再在未来计算中直接复用”的基本机制。

沿着这一思路，Log-Augmented Generation [Che25b] 将历史 reasoning logs 保存为可复用的 KV cache。推理时，系统先按语义检索相关 log，再对其中的 KV states 做位置对齐，并将其注入当前 `past_key_values`，从而让模型继承过去推理链对应的内部计算，而不是重新阅读日志文本并再执行一遍同样的前向传播。这里被复用的不再是 reasoning trace 的可读表面形式，而是其在 transformer 内部已经形成的 attention-level computation。

TempoFit [Sun26] 则将这一思路推进到 embodied setting。在 long-horizon VLA manipulation 中，该方法持续维护 layer-wise temporal KV memory，将过去视觉观察与语言条件对应的 prefix KV states 保存在 temporal cache 中，并通过 key matching 与 temporal bias 检索相关历史状态，再以 pre-attention residual 的方式写回冻结的 VLA。与一般 serving-oriented KV reuse 不同，这里的 cache 不只是为了减少单次推理成本，而是承担了跨时间状态继承与经验延续的功能，因此属于更典型的 latent experience reuse。

总体来看，cache-based 方法的优势在于训练成本低、信息保真度高，能够直接继承模型已经完成的细粒度内部计算；但其局限也很明显，即与特定 backbone、position encoding 和 attention implementation 强耦合，且 latent state 的可解释性和可编辑性较弱。它更适合那些历史计算本身就高度有价值、且未来任务与过去上下文存在明显连续性的场景。

### Prompt-Based Latent Transformation

如果说 cache-based 方法保留的是过去已经发生的内部计算，那么 Prompt-Based Latent Transformation 更强调对经验进行压缩与固化：agent 不必复用完整轨迹，也不必更新底座权重，而是将 demonstrations、reasoning traces 或 task procedures 提炼为可反复加载的连续提示，使经验以 soft prompt、prefix KV 或 memory token embedding 的形式直接调节后续生成。

MAP-VLA [Li25g] 是这一思路在 robotic manipulation 中的代表。该方法将 manipulation demonstrations 按阶段切分，并为每个 stage 学习一组 memory prompts；推理时，系统根据当前执行窗口匹配最相关的历史阶段，再把对应 soft prompt 加入当前 prompt embedding，使 demonstration experience 以连续提示而不是文本示例的形式参与 action generation。这里经验并未写入 policy weights，而是停留在外部、可加载的 latent prompt 中。

ReasonCACHE [Gup26] 则将类似思想用于 reasoning demonstrations。该方法把大规模推理示例压缩为各层可训练的 prefix KV pairs，在冻结 backbone 的前提下将 reasoning experience 固化为固定长度的 latent reasoning prior。测试时，模型无需再读入长篇 exemplars，而是直接在 attention 前缀中调用这部分经验。与 few-shot prompting 相比，经验复用不再依赖长文本上下文；与 fine-tuning 相比，经验也未被完全吸收到主模型参数中，而是保留为相对独立的 continuous prefix。

TokMem [Wu25c] 进一步将 procedural knowledge 压缩到单个 memory token embedding 中。该方法基于 procedure-response pairs 训练专门的 memory tokens，使每个 token 同时充当可路由的离散索引与连续控制向量；推理时，模型先根据 query 选择最相关的 memory token，再借助该 token 激活相应 procedure。这样，procedure 不再以自然语言规则或文本 SOP 的形式被读取，而是以 embedding-level control unit 的形式参与生成。

Prompt-based 方法的共同特点，是在 textual prompting 与 parameter update 之间提供了一种更轻量的中间层。它们通常具有较高压缩率和较强部署灵活性，适合承载边界清晰、重复性强的经验模式，如特定 reasoning style、固定 procedure 或分阶段操作技能。但其局限同样明显：latent prompt 的内部语义较难解释，泛化能力依赖训练数据覆盖，而与特定模型 embedding space 的强耦合也使跨模型迁移并不直接。

### Module-Based Latent Transformation

相比前两类方法，Module-Based Latent Transformation 代表了 P3 中最完整的 latent memory form。这里的重点不再只是“保存过去计算”或“压缩为小型 prompt”，而是显式构建一个可写入、可读取、可更新、可遗忘的 memory system，使 tokenized experience 能在长期、多模态、动态变化的 agent loop 中被持续组织和调用。换言之，这类方法不仅完成了 tokenized-to-latent 的表示转化，也进一步关心 latent experience 的存储结构、访问方式与生命周期管理。

一条重要路线，是从原始离散轨迹中检索历史经验，再将其重新编码为与当前 agent 状态耦合的 latent memory。LatentMem [Fu26] 先从 experience bank 检索历史多智能体轨迹，再用 role-aware memory composer 将这些 tokenized trajectories 压缩为 agent-specific latent memory matrix，并直接拼接到当前 agent hidden states 中参与推理，使同一段历史经验能够按不同 agent role 被重新表征和注入。Dual Latent Memory for Visual Multi-agent System [Yu26d] 则进一步将多智能体经验拆分为 latent perception memory 与 latent thinking memory 两个通道，分别保存视觉观察与推理轨迹的语义 chunk，并在当前 agent 解码不确定时把相关 latent units 注入 hidden states，从而将过去 agent 的 observation 与 thinking 以 latent communication 的方式传递给后续 agent。

另一条路线主要出现在 embodied 和 VLA 场景中，即把视觉、动作和任务进展共同编码进持续维护的 memory bank 或 recurrent state。MemoryVLA [Shi25] 构建了双通道的 Perceptual-Cognitive Memory Bank，通过 cross-attention 与 gating 将历史 perceptual 与 cognitive latents 融合进当前 action prediction，使过去观察与高层认知状态能够共同影响后续 manipulation。HAMLET [Koo25] 使用 moment tokens 提取各时间步的紧凑 latent summary，再通过轻量 Transformer 聚合历史 token cache，从而为原本更偏 memoryless 的 VLA 提供显式的 history-aware state。Gated Memory Policy [Gao26] 则强调按需调用：它将历史图像与动作轨迹编码为缓存状态，并通过显式 memory gate 决定何时让这些 latent history tokens 通过 cross-attention 进入 policy，因此过去经验是否参与当前控制成为一个受学习机制调节的过程。

当任务进一步扩展到更长时程和更强空间依赖时，latent memory system 往往呈现出更复杂的结构化形态。Chameleon [Guo26] 将多视角视觉与 proprioceptive history 写入分层 spatiotemporal slot memory，并通过 state-space dynamics 从 latent episodic bank 中读出 decision state，再由下游 rectified-flow policy 直接消费。EchoVLA [Lin25d] 则维护 scene memory 与 episodic memory 的双层 declarative memory，通过 coarse-to-fine cross-attention 将空间结构与时间经验融合为 diffusion policy 的条件。与 textual memory 相比，这类方法能够保留更多视觉、空间与动作层面的细粒度信息，因此尤其适合 long-horizon robotic manipulation 和 mobile manipulation 等高度非 Markovian 的任务。

需要指出的是，并非所有相关工作都落在纯粹的 latent pathway 上。Hybrid Self-evolving Structured Memory for GUI Agents [Zhu26] 是一个典型的 hybrid boundary case：该方法同时维护 high-level strategy 与 attribute tags 这类结构化离散 memory，以及 low-level trajectory embeddings 这类 continuous memory。其意义不在于提供一个“纯 P3”实例，而在于表明在 GUI agents 中，经验复用可以同时沿 symbolic pathway 与 latent pathway 并行展开，其中离散部分提供可解释的检索和更新结构，而连续部分保存难以文本化的视觉与操作细节。

## Discussion

总体来看，Tokenized-to-Latent Experience Transformation 标志着 agent memory 从“把过去写下来再读回来”转向“把过去编码进可直接参与计算的内部状态”。在这一过程中，经验的可读性、可编辑性与可解释性逐步下降，而推理效率、模型内耦合性与细粒度信息保留能力则相应上升。Cache-based 方法最接近对原始内部计算的直接复用，训练成本最低，但也最依赖具体 backbone；prompt-based 方法提供了较轻量、模块化的 latent adaptation 形式，适合压缩稳定的 skill 或 reasoning prior；module-based 方法则最接近系统级 latent memory mechanism，能够支持长期、多模态、动态更新的经验组织，但同时也面临更高的建模与工程复杂度。

因此，P3 的关键并不在于某种特定的 memory 名称，而在于经验是否真正完成了载体层级的迁移：历史交互中形成的 tokenized artifact，不再通过再次 tokenization 被读取，而是被转化为 continuous representation，并直接进入模型未来决策的 attention、hidden-state computation 或 action prediction。正是在这一意义上，P3 构成了从 externalized experience reuse 走向 model-native experience reuse 的关键中间层。

```