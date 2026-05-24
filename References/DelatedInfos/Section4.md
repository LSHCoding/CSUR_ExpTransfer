
# 4. Latent-Space Transformation：Tokenized-to-Latent Transformations

## 4.1 Cache-Based Latent Transformation

## 4.2 Prompt-Based Latent Transformation

——即便其形态同样表现为 layer-wise KV（如 ReasonCACHE），来源也是优化过程而非某次具体推理


MAP-VLA [Li25g]：经验并未写入 policy weights，而停留在外部、可加载的 Latent prompt 中。

ReasonCACHE [Gup26]：与 few-shot prompting 相比，经验复用不再依赖长文本上下文；与 fine-tuning 相比，经验未被完全吸收到主模型参数中，保留为相对独立的 continuous prefix。

TokMem [Wu25c]：Procedure 不再以自然语言规则或文本 SOP 的形式被读取，而是以 embedding-level control unit 的形式参与生成。

## 4.3 Module-Based Latent Transformation

---

# 4. Latent-Space Transformation：Tokenized-to-Latent Transformations

Latent-Space Transformation 把 Tokenized Agent Experience 转化为连续表示，使其能直接进入 attention 或 hidden-state computation，而不必先解码回自然语言或其他离散 token。判定这一类转化只需一条标准：经验在复用时以 continuous representation 的形式被模型消费，没有重新经过 tokenization。

经验为何值得以这种形式保存，而非始终维持可读 token？离散 token 只记录经验的表面形式。模型在处理一段 Tokenized experience 时，会在内部形成一组连续状态——逐层的上下文表示、注意力对历史片段的组织方式、对该段经验消化之后的理解——这些状态无法由 token 表面形式完整复原。把经验解码回文本、在未来任务中重新读入，意味着丢弃这部分内部理解，并让模型对同一段经验再理解一遍。Latent-Space Transformation 复用的正是模型已经形成的内部表示状态，保留了离散 token 承载不了的细粒度信息；推理开销下降只是附带结果。在本 Survey 的载体框架中，Latent 由此处在 Tokenized carrier 的 externalized reuse 与 Parametric carrier 的 fully parametric reuse 之间：经验以连续表示存在，已不是模型之外的可读符号，也尚未固化进权重。这一中间位置（§4.4 展开）是它在具身、GUI、多智能体等场景中日益重要的原因。

两类表面相似的机制需要与 Latent-Space Transformation 划清。RAG-style memory 同样使用 embedding，但 embedding 只作检索索引，被模型消费的仍是 retrieved text，经验复用的载体依旧是 Tokenized。KV cache eviction、attention sparsification、serving-level cache reuse 等推理优化方法同样操作 KV cache 或 hidden states，但目标是压低显存、延迟与吞吐，并不承载长程经验复用的语义。本文只纳入明确把历史交互转成可复用 latent 表示的方法——该表示要承担经验存储与复用功能，而不只是推理系统里的临时加速结构。

Latent-Space Transformation 方法的根本差异在于：可复用的 latent 表示从何而来，以及为获得它需要投入多少专用机制。沿这条轴可分为三类。**Cache-Based Latent Transformation** 不额外训练，直接复用历史 forward pass 已经产生的真实 KV / hidden states。**Prompt-Based Latent Transformation** 通过训练把经验压缩为静态的连续提示表示，底座模型保持冻结。**Module-Based Latent Transformation** 通过训练构建带显式写入、读取、融合的动态 latent memory 系统。三类沿"复用现成计算 → 训练静态 latent → 训练动态 latent 系统"递进，专用机制投入与表达能力依次增强，训练与工程成本同向上升。

## 4.1 Cache-Based Latent Transformation

Cache-Based Latent Transformation 专用机制投入最低：它不训练任何新目标，直接保存并复用模型在历史交互中已经产生的 KV cache 或 hidden states。Agent 的历史经验不止存在于可读的 trajectory log 里——模型处理这些 Tokenized experience 时，经验已被编码进 attention 层的连续状态。这部分状态既然算过一次，就可以持久化下来、在未来直接复用，省去重新读入文本日志、重新形成同一份内部表示的过程。它复用的是真实 forward pass 的原始产物，区别于后两类经训练目标压缩或重构得到的表示。

Memorizing Transformers [Wu22] 确立了这一机制的技术基础：它把长序列中先前 token 在中间层形成的 key-value 对写入外部 memory，后续时间步通过 kNN 检索重新接入 attention。该工作本身并不是 agent experience 的复用实例——memory 服务于单一 document 内的长上下文建模，文档切换即清空，经验来源也是静态语料。但它把"离散序列先编码为 latent state、再在未来计算中直接复用"这一范式确立了下来，后续 agent-centric 方法在此之上展开。

Log-Augmented Generation [Che25b] 把 cache-based 复用用到 reasoning 场景下 agent 自生成的经验。它将过往求解过程中的 reasoning logs 经一次完整 forward pass 编码，只为选中的少量 token 持久化真实 KV；推理时按语义相似度检索相关 log，对取回的历史 KV 做位置重映射后作为 `past_key_values` 注入当前生成。模型继承的是 reasoning trace 在 Transformer 内部已经形成的 attention-level computation，可读文本本身不再被读取。TempoFit [Sun26] 把同样的思路推进到 embodied setting。在 long-horizon VLA manipulation 中，它在冻结 backbone 上维护 layer-wise temporal KV memory，把早先时间步的 prefix K/V 存进分层 FIFO buffer，用 key-to-key 相似度加 temporal bias 检索，再以 pre-attention residual 写回当前层。这里的 cache 承担同一 long-horizon episode 内的历史状态继承，让原本受 non-Markov 性困扰的决策能用上早先经验。

Cache-Based 方法的优劣需相对后两类来界定。它复用真实 forward pass 的原始产物，信息保真度最高，没有 Prompt-Based 与 Module-Based 那种由训练目标引入的压缩损失；同时无需训练，专用机制投入也最低。代价是：latent state 与特定 backbone、position encoding、attention implementation 强耦合，跨模型迁移困难；真实 KV 的容量开销大于压缩后的 latent；且要配套选择、检索、压缩、淘汰与位置对齐机制。保存下来的是连续状态而非可读符号，可解释性与可编辑性都弱。

## 4.2 Prompt-Based Latent Transformation

Prompt-Based Latent Transformation 通过训练把 demonstrations、reasoning traces、task procedures 等 Tokenized experience 压缩为 soft prompt、prefix vectors 或 memory token embeddings 等静态连续表示。与 §4.1 直接复用真实 KV 不同，这里的连续表示由专门的训练目标压缩得到，并非 forward pass 的原始产物。底座模型通常冻结，训练与复用的只有这些外部连续向量。专用机制投入因此高于 Cache-Based——多一个离线训练阶段，但仍不触及底座权重。

MAP-VLA [Li25g] 在 robotic manipulation 中把 expert demonstrations 按任务阶段切分，为每个阶段训练一组 soft prompt 向量。底座 VLA 冻结，推理时按当前轨迹与演示轨迹的相似度在局部阶段范围内检索 prompt，与 base prompt embedding 逐元素相加后参与 action generation——demonstration 经验以连续提示而非文本示例的形式进入模型。ReasonCACHE [Gup26] 把大规模 reasoning demonstrations 压缩成各层可训练的 prefix K/V；测试时模型不再读入长篇 exemplars，各层 prefix KV 与当前 token KV 直接拼成扩展后的 attention 字典，attention 输出显式混合历史经验与当前输入。TokMem [Wu25c] 把压缩粒度推到极致：一个 procedure 压成单个 memory token embedding，该 token 兼作可路由的离散索引与连续控制向量，推理时路由器按 query 选出最相关的 memory token 并激活对应 procedure。TokMem 的经验来源偏向整理或合成的 procedure 与 tool-use 数据，agent 自生成属性较弱，处在本 Survey 的纳入边界。

Prompt-Based 方法介于 textual prompting 与 full fine-tuning 之间。相对文本 prompt，它更紧凑，且不受自然语言上下文长度的直接限制；相对参数微调，它更模块化，可按任务、技能、场景分别加载不同的 latent prompt，而不改动底座权重。它适合边界清晰、重复性强、相对稳定的经验模式。局限同样来自"静态压缩"这一特征：latent prompt 内部语义难以解释，泛化能力受训练数据覆盖约束，与特定模型 embedding space 的强耦合也使跨模型迁移并不直接。相比 §4.1，它以一定的信息保真度损失换取更高的紧凑性与模块化。

## 4.3 Module-Based Latent Transformation

Module-Based Latent Transformation 专用机制投入最高。它构建一个能动态写入、读取、更新的 latent memory 系统——由显式的 memory module、memory bank、compressor、composer 或 cross-attention reader 构成——让 Agent 按当前 context、历史轨迹、视觉状态或任务进程动态访问与整合经验，而不停留在静态 latent 表示。

这类方法通常包含写入、读取、融合三个环节。写入阶段，系统把历史轨迹、多轮交互、视觉观察或动作反馈编码为 latent entries，存入 memory bank 或 episodic buffer。读取阶段，当前 query、task state 或 visual observation 作为查询信号，从 memory 中选出相关经验。融合阶段，被读取的 latent memory 通过 cross-attention、gating、residual connection 或 action-conditioning 机制影响后续 generation 或 action prediction。§4.2 中底座模型多保持冻结，Module-Based 方法的训练范围则更宽：多数只训练新增的 memory 模块，部分工作（如下文 MemoryVLA）连同 backbone 一并端到端训练。

在这一共同骨架下，Module-Based 方法可沿两个维度进一步区分。第一个维度是 latent memory 的产生时机：一类方法在 episode 进行中增量维护 latent memory，每步观测即时编码写入，memory 被读取前已是 latent 形态；另一类在外部仍以 Tokenized 形式保存历史，只在 query 到来时检索、再即时压缩成 latent。产生时机是一条横切维度，并不与三类划分平行——三类划分依据的是专用机制投入，query-time 压缩的方法（如下文 LatentMem）因为训练了专门的压缩模块，仍明确归 Module-Based，产生时机只是它的属性。第二个维度是 memory 的通道结构：一部分工作维护单一 latent memory，另一部分把经验显式拆成两条通道——典型是"感知性"与"认知 / 时序性"——分别维护、分别读取，各自保留 observation 与 thinking / temporal 两类信息。

单通道方法中，LatentMem [Fu26] 是 query-time 压缩的代表：它先用外部 embedding 检索多智能体系统过往的 raw interaction trajectories，再由一个 role-aware memory composer 把这些 tokenized trajectories 连同 agent role profile 压缩为固定长度的 latent memory matrix，直接拼接到当前 Agent hidden states，同一段历史经验能按不同 agent role 被重新表征。HAMLET [Koo25] 属于增量维护：它引入可学习的 moment tokens，在每个时间步从 VLM 提取紧凑的 latent summary，再由一个浅层 Transformer memory module 对窗口内历史做聚合，为原本 memoryless 的 VLA 提供 history-aware state。Gated Memory Policy [Gao26] 在增量维护之上引入选择性：它把历史图像与动作轨迹编码为缓存 token，由一个二值 memory gate 决定这些 latent history 是否经 cross-attention 进入 policy，经验是否参与当前控制本身成为受学习机制调节的环节。Chameleon [Guo26] 面向更长时程与更强空间依赖：它通过 spatiotemporal anchoring 与 selective state-space dynamics 把多视角视觉与 proprioceptive history 连续压缩为 episodic latent state，再投影成 conditioning token 注入 policy 各层。

双通道方法把经验按性质拆流维护。embodied 场景中，MemoryVLA [Shi25] 构建 Perceptual-Cognitive Memory Bank，分别保存视觉 token 压缩得到的 perceptual latent 与语言模型 hidden state 给出的 cognitive latent，通过 cross-attention 与 gated residual fusion 融入 action prediction。EchoVLA [Lin25d] 在 mobile manipulation 中维护 scene memory 与 episodic memory 双层 declarative memory：前者把 3D 特征聚合为持续积累的 voxelized feature volume，后者按 FIFO 保留时间索引的近程历史，经 coarse-to-fine cross-attention 融合为 diffusion policy 的条件，两条通道对应环境级持久表征与近程经历两种时间尺度。multi-agent 场景中，Dual Latent Memory for Visual Multi-agent System [Yu26d] 把协作经验拆为 latent perception memory 与 latent thinking memory，在当前 Agent 解码不确定（高熵）时分别注入 hidden states，使前序 Agent 的 observation 与 thinking 以 latent communication 的形式传递。

作为边界示意，Hybrid Self-evolving Structured Memory for GUI Agents [Zhu26] 同时维护 Schematic Tokenized memory（图结构的 trajectory node 与结构边）与 latent memory（Q-Former 风格 encoder 压缩出的 continuous embeddings）。两类 memory 各自独立维护，其间没有耦合二者的 integration mechanism，因此不作为 Composite Pipeline 处理（§7）；此处只用以说明 latent 与 Tokenized 载体可在同一系统内并行存在。

Module-Based 是 Latent-Space Transformation 中表达能力最强的形态，适合 long-horizon、multi-modal、embodied、GUI 与 multi-agent 场景。相对 Cache-Based 与 Prompt-Based 的静态复用，它能把 memory access 与当前决策动态耦合并支持持续更新，也由此保留更多视觉、空间与动作层面的细粒度信息，契合高度非 Markovian 的 robotic manipulation 与 mobile manipulation。代价是三类中最高的系统复杂度——额外的 memory module、cross-attention、compressor 或 gating 机制带来更重的训练与部署成本；持续更新的 latent memory 还引入前两类没有的失效模式（§4.4 详述）。

## 4.4 Discussion

三类 Latent-Space Transformation 方法构成一个连续谱。沿 Cache-Based → Prompt-Based → Module-Based 的方向，专用机制投入递增：从复用现成计算，到训练静态 latent，再到训练动态 latent 系统；表达能力与动态适应性随之上升，训练与工程成本同向上升。信息保真度呈相反梯度：Cache-Based 复用真实 forward pass 的原始产物，保真度最高；Prompt-Based 与 Module-Based 经训练目标压缩，以一定的信息损失换取紧凑性与可组织性。

三类方法在 verifiability 与 robustness 上呈现同样清晰的梯度。latent memory 一旦写入便难以被人直接检视或定点修正，经验是否正确、是否过时通常只能从下游行为间接推断。这种不可检视性在三类中递增：Cache-Based 复用单次推理的真实 KV，内容尚可追溯到具体历史片段；Prompt-Based 的静态向量经训练压缩后已无法对应单条经验；Module-Based 的动态 memory 持续写入更新，最难审计，并独有 staleness、capacity saturation、latent drift 与错误经验累积等失效模式——错误经验进入 latent memory 后既不易被发现，也无法像 text rule 那样被直接删改。这一梯度与 §4.1–§4.3 的表达能力梯度方向相反，构成 Latent-Space Transformation 内部最核心的 trade-off：专用机制投入越高、表达能力越强，可检视性与可控性越低。

回到整体载体框架，Latent 的过渡位置由经验被复用时的形式决定，与存储位置无关。Cache-Based 的外部 KV memory 和 Module-Based 的 latent memory bank 在"存储—检索"结构上仍与 RAG 同构，经验照样存放在模型本体之外；区别在于检索出的经验以 continuous representation 直接进入 attention 或 hidden-state computation，不再经 tokenization 解码回离散 token。这种 attention-consumable 的消费形式让经验离开"模型之外的可读符号"形态，向"模型可直接计算的内部状态"靠近一步，但还没固化进权重。具身、GUI、多智能体等场景的经验本就难以无损地写成离散文本，这解释了 Latent-Space Transformation 在这些场景中的重要性；同样的位置也让它成为通往 Parametric carrier（§5、§6）的过渡形态。