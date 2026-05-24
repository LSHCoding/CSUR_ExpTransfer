# 4. Latent-Space Transformation：Tokenized-to-Latent Transformations

Latent-Space Transformation 将 Tokenized Agent Experience 转化为可被模型直接消费的连续表示——KV cache、hidden states、soft prompt、prefix vectors、memory token embeddings、latent memory bank 或 cross-attention memory output。这里的目标载体不再是离散 token，而是可直接参与 attention、hidden-state computation 或 action prediction 的内部计算状态。经验在复用时不再回到自然语言或其他离散 token 形式，而是以 model-native state 的形式被再次调用。Latent-Space Transformation 与常见 RAG-style memory 有本质区别：后者虽然也用 embedding 做索引，但最终被模型消费的通常是 retrieved text——embedding 只是检索机制，经验真正被复用的载体仍是 Tokenized 文本。Latent-Space Transformation 要求转化后的经验以 continuous representation 的形式直接进入 attention 或 hidden-state computation，不被解码回自然语言或其他离散 token 后再输入模型。

Latent-Space Transformation 也不同于单纯的 inference efficiency optimization。许多 KV cache eviction、attention sparsification、cache quantization 或 serving-level cache reuse 方法同样操作 KV cache 或 hidden states，但其目标主要是降低显存占用、延迟或吞吐成本，并不一定具有跨 session、跨 task 或长程 episode 的经验复用语义。本文只将那些明确把历史交互转化为可复用 Latent artifact 的方法纳入 Latent-Space Transformation——Latent representation 必须承担经验存储与复用功能，而非仅是推理系统中的临时加速结构。

Latent-Space Transformation 方法的差异集中在一点：可复用的 Latent 表示从何而来。沿"获得该表示所需投入的专用机制"这条轴划分为三类。Cache-Based Latent Transformation 不额外训练，直接复用历史 forward pass 产生的真实 KV/hidden states。Prompt-Based Latent Transformation 通过训练把经验压缩为静态的连续提示表示（soft prompt、prefix vectors、memory token embeddings），底座模型保持冻结。Module-Based Latent Transformation 通过训练构建带显式写入、读取、融合的动态 Latent memory 系统。三类沿"复用现成计算 → 训练静态 latent → 训练动态 latent 系统"递进，专用机制与表达能力递增，训练与工程成本同向上升。

## 4.1 Cache-Based Latent Transformation

Cache-Based Latent Transformation 将历史交互过程中产生的 KV cache、hidden states 或其他 attention-level computation 保存下来，在后续任务或时间步中直接复用。其核心思想是：Agent 的历史经验不仅存在于可读的 trajectory log 中，也已被模型在处理这些 Tokenized experience 时编码进内部连续状态。系统可以直接复用过去 forward pass 中形成的 Latent computation，而非在未来任务中重新读取文本日志并再次计算。

Memorizing Transformers [Wu22] 是这一方向的机制前驱：它将长序列中先前 token 在中间层形成的 key-value 对写入外部 memory，并在后续时间步通过 kNN 检索重新接入 attention，确立了"离散序列先编码为 latent state，再在未来计算中直接复用"的基本机制。该工作并非 agent-centric memory 设计，但确立了 cache-based latent reuse 的技术基础。

Log-Augmented Generation [Che25b] 将历史 reasoning logs 保存为可复用的 KV cache。推理时系统先按语义检索相关 log，再对其中的 KV states 做位置对齐，并将其注入当前 past_key_values，从而让模型继承过去推理链对应的内部计算，而不是重新阅读日志文本并再执行一遍同样的前向传播。被复用的不再是 reasoning trace 的可读表面形式，而是其在 Transformer 内部已经形成的 attention-level computation。

TempoFit [Sun26] 将这一思路推进到 embodied setting。在 long-horizon VLA manipulation 中，该方法持续维护 layer-wise temporal KV memory，将过去视觉观察与语言条件对应的 prefix KV states 保存在 temporal cache 中，并通过 key matching 与 temporal bias 检索相关历史状态，再以 pre-attention residual 的方式写回冻结的 VLA。与一般 serving-oriented KV reuse 不同，这里的 cache 承担了跨时间状态继承与经验延续的功能。

Cache-Based 方法的优势在于训练成本低、信息保真度高，能直接继承模型已完成的细粒度内部计算。局限在于与特定 backbone、position encoding 和 attention implementation 强耦合，latent state 的可解释性和可编辑性较弱，容量开销较大，需要配套设计选择、检索、压缩、淘汰和位置对齐机制。

## 4.2 Prompt-Based Latent Transformation

Prompt-Based Latent Transformation 通过训练将 demonstrations、reasoning traces、task procedures 或其他 Tokenized experience 转化为 soft prompt、prefix vectors 或 memory token embeddings 等连续提示表示。底座模型通常保持冻结，仅训练这些外部连续向量。与 §4.1 直接复用真实 forward pass 产生的 KV 不同，这里的连续表示由训练目标压缩得到——即便其形态同样表现为 layer-wise KV（如 ReasonCACHE），来源也是优化过程而非某次具体推理。这类方法可看作介于 textual prompting 与 full fine-tuning 之间的轻量经验转化方式：比文本 prompt 更紧凑，不受自然语言上下文长度的直接限制；比参数微调更模块化，便于按任务、技能或场景加载不同的 Latent prompts。

MAP-VLA [Li25g] 在 robotic manipulation 中将 demonstrations 按阶段切分，为每个 stage 学习一组 memory prompts。底座 VLA 保持冻结，推理时系统根据当前执行片段匹配最相近的历史阶段，把对应 soft prompt 加到 base prompt embedding 上，使 demonstration experience 以连续提示而非文本示例的形式参与 action generation。经验并未写入 policy weights，而停留在外部、可加载的 Latent prompt 中。

ReasonCACHE [Gup26] 将大规模 reasoning demonstrations 压缩为各层可训练的 prefix KV pairs。测试时，模型无需再读入长篇 exemplars，而是直接在 attention 前缀中调用这部分经验。与 few-shot prompting 相比，经验复用不再依赖长文本上下文；与 fine-tuning 相比，经验未被完全吸收到主模型参数中，保留为相对独立的 continuous prefix。

TokMem [Wu25c] 将 procedural knowledge 压缩到单个 memory token embedding 中。每个 token 同时充当可路由的离散索引与连续控制向量：推理时模型先根据 query 选择最相关的 memory token，再借助该 token 激活相应 procedure。Procedure 不再以自然语言规则或文本 SOP 的形式被读取，而是以 embedding-level control unit 的形式参与生成。

Prompt-Based 方法的共同优势是压缩率高、部署灵活，适合承载边界清晰、重复性强的经验模式。局限在于 latent prompt 的内部语义较难解释，泛化能力依赖训练数据覆盖，与特定模型 embedding space 的强耦合使跨模型迁移并不直接。

## 4.3 Module-Based Latent Transformation

Module-Based Latent Transformation 通过显式 memory module、memory bank、compressor、composer、cross-attention reader 或 structured memory graph，将历史经验动态转化、组织、读取和更新为 Latent memory。与前两类方法不同，这类方法构建的是一个更完整的 Latent memory system，使 Agent 能根据当前 context、历史轨迹、视觉状态或任务进程动态访问和整合经验。

经验复用通常包含显式的写入、读取和融合过程。写入阶段，系统将历史轨迹、多轮交互、视觉观察或动作反馈编码为 latent entries，存入 memory bank 或 episodic buffer。读取阶段，当前 query、task state 或 visual observation 作为查询信号，从 memory 中选择相关经验。融合阶段，被读取的 Latent memory 通过 cross-attention、gating、residual connection 或 action-conditioning mechanism 影响后续 generation 或 action prediction。

在这一共同骨架下，Module-Based 方法可沿两个维度进一步区分。其一是 Latent memory 的产生时机：一类在离线阶段就将经验持久化为 latent entries，读取时直接取用（如 MemoryVLA、Chameleon 的 latent episodic bank）；另一类在外部仍以 Tokenized 形式保存历史，inference 时检索后再即时压缩为 latent，转化发生在查询时而非写入时（如 LatentMem 先检索历史轨迹、再经 composer 压缩）。其二是 memory 的通道结构：部分工作维护单一 latent memory，另一部分把经验显式拆为"感知性"与"认知/时序性"双通道分别维护与读取。

LatentMem [Fu26] 先从 experience bank 检索历史多智能体轨迹，再用 role-aware memory composer 将这些 Tokenized trajectories 压缩为 agent-specific latent memory matrix，直接拼接到当前 Agent hidden states 中参与推理。同一段历史经验能够按不同 agent role 被重新表征和注入。Dual Latent Memory for Visual Multi-agent System [Yu26d] 将多智能体经验拆分为 latent perception memory 与 latent thinking memory 两个通道，分别在当前 Agent 解码不确定时注入 hidden states，将过去 Agent 的 observation 与 thinking 以 latent communication 的方式传递。

在 embodied 和 VLA 场景中，MemoryVLA [Shi25] 构建双通道 Perceptual-Cognitive Memory Bank，通过 cross-attention 与 gating 将历史 perceptual 与 cognitive latents 融合进当前 action prediction。HAMLET [Koo25] 使用 moment tokens 提取各时间步的紧凑 latent summary，再通过轻量 Transformer 聚合历史 token cache，为原本 memoryless 的 VLA 提供显式的 history-aware state。Gated Memory Policy [Gao26] 将历史图像与动作轨迹编码为缓存状态，并通过显式 memory gate 决定何时让这些 latent history tokens 通过 cross-attention 进入 policy，使过去经验是否参与当前控制成为一个受学习机制调节的过程。

当任务进一步扩展到更长时程和更强空间依赖时，Chameleon [Guo26] 将多视角视觉与 proprioceptive history 写入分层 spatiotemporal slot memory，并通过 state-space dynamics 从 latent episodic bank 中读出 decision state。EchoVLA [Lin25d] 维护 scene memory 与 episodic memory 的双层 declarative memory，通过 coarse-to-fine cross-attention 将空间结构与时间经验融合为 diffusion policy 的条件。与 textual memory 相比，这类方法能够保留更多视觉、空间与动作层面的细粒度信息，尤其适合 long-horizon robotic manipulation 和 mobile manipulation 等高度非 Markovian 任务。

<!-- Hybrid Self-evolving Structured Memory for GUI Agents [Zhu26] 同时维护 Schematic Tokenized memory（high-level strategy/attribute tags）与 Latent memory（low-level trajectory embeddings），两类 memory 各自独立维护，其间不存在耦合二者的 integration mechanism，不作为 Composite Pipeline 处理，仅在此作为 Latent 与 Tokenized 并存的边界示意。 -->

Module-Based 方法是 Latent-Space Transformation 中表达能力最强的方法形态，特别适合 long-horizon、multi-modal、embodied、GUI 和 multi-agent 场景。优势在于表达能力强、动态适应性好，能将 memory access 与当前决策紧密耦合。局限在于系统复杂度最高——需要额外的 memory module、cross-attention layer、compressor 或 gating mechanism，训练和部署成本较高；持续更新 Latent memory 会带来 staleness、capacity saturation、latent drift 和错误经验累积等问题。

## 4.4 Discussion

Latent-Space Transformation 标志着 Agent memory 从"把过去写下来再读回来"转向"把过去编码进可直接参与计算的内部状态"。在这一过程中，经验的可读性、可编辑性与可解释性逐步下降，而推理效率、模型内耦合性与细粒度信息保留能力则相应上升。三类方法构成一个连续谱：Cache-Based 方法最接近对原始内部计算的直接复用，训练成本最低，但也最依赖具体 backbone；Prompt-Based 方法提供了较轻量、模块化的 Latent adaptation 形式，适合压缩稳定的 skill 或 reasoning prior；Module-Based 方法最接近系统级 Latent memory mechanism，能够支持长期、多模态、动态更新的经验组织，但同时也面临更高的建模与工程复杂度。

三类方法在 verifiability 与 robustness 上也呈现明显梯度。Latent memory 一旦写入便难以被人直接检视或定点修正，经验是否正确、是否过时通常只能从下游行为间接推断。这种不可检视性在三类中程度递增：Cache-Based 复用单次推理的真实 KV，内容尚可追溯到具体历史片段；Prompt-Based 的静态向量经训练压缩后已无法对应单条经验；Module-Based 的动态 memory 持续写入更新，最难审计，并独有 staleness、capacity saturation、latent drift 与错误经验累积等失效模式——错误经验进入 latent memory 后既不易被发现，也无法像 text rule 那样被直接删改。

<!-- Latent-Space Transformation 在整体框架中的位置：它处在 externalized reuse（通过 Tokenized carrier）与 fully parametric reuse（通过 Parametric carrier）之间。关键转变在于经验被复用时的形式，而非其存储位置——Cache-Based 的外部 KV memory 与 Module-Based 的 latent memory bank 在存储—检索结构上仍与 RAG 同构，经验依然存放在模型本体之外；区别在于检索出的经验以 continuous representation 直接进入 attention 或 hidden-state computation，不再经 tokenization 解码回离散 token。正是这种 attention-consumable 的消费形式，使 Latent-Space Transformation 成为通往 Parametric carrier 的过渡形态，也解释了为何它在具身、GUI 和多智能体等高度依赖 perceptual grounding 与动态经验整合的场景中日益重要。 -->
