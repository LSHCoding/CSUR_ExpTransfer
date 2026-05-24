# 4. Latent-Space Transformation：Tokenized-to-Latent Transformations

Latent-Space Transformation 把 Tokenized Agent Experience 转化为连续表示，使其直接进入 attention 或 hidden-state computation，复用时不再解码回离散 token。使用 latent 而非 token 的核心原因在于：模型处理一段 Tokenized experience 时会形成离散 token 无法完整复原的内部状态——逐层上下文表示、注意力对历史的组织、对经验消化后的理解；把经验解码回文本再读入会丢弃这部分理解，并迫使模型重新处理同一段经验。Latent-Space Transformation 复用的正是这些内部表示状态。它由此处在 Tokenized 的 externalized reuse 与 Parametric 的 fully parametric reuse 之间：经验不再是模型之外的可读符号，也尚未固化进权重。

KV cache eviction 等推理优化方法虽操作 KV / hidden states，但不承载长程经验复用语义。本文只纳入 latent 表示明确承担经验存储与复用功能的方法。按 latent 表示的来源——即获取它所需的专用机制——分为三类：**Cache-Based** 不训练，直接复用历史 forward pass 产生的真实 KV / hidden states；**Prompt-Based** 通过训练把经验压缩为静态连续提示，底座冻结；**Module-Based** 通过训练构建带写入、读取、融合的动态 latent memory 系统。

<!-- 三类专用机制投入与表达能力递增，训练与工程成本同向上升。 -->

## 4.1 Cache-Based Latent Transformation

Cache-Based Latent Transformation 直接保存并复用模型历史交互中已产生的 KV cache 或 hidden states，不引入新训练目标，复用的是真实 forward pass 的原始产物。Memorizing Transformers [Wu22] 确立了机制基础：把先前 token 在中间层的 key-value 对写入外部 memory，后续时间步通过 kNN 检索接入 attention。Log-Augmented Generation [Che25b] 将其用于 reasoning agent 的自生成经验：对历史 reasoning logs 做完整 forward pass，只为选中的少量 token 持久化真实 KV，推理时检索相关 log、对历史 KV 做位置重映射后作为 `past_key_values` 注入，复用其 attention-level computation。TempoFit [Sun26] 推进到 embodied setting：在冻结 VLA 上维护 layer-wise temporal KV memory，把早先时间步的 prefix K/V 存入分层 FIFO，经 key-to-key 相似度加 temporal bias 检索后以 pre-attention residual 写回，支撑同一 long-horizon episode 内的历史状态继承。

## 4.2 Prompt-Based Latent Transformation

Prompt-Based Latent Transformation 通过训练把 demonstrations、reasoning traces、procedures 等经验压缩为 soft prompt、prefix vectors 或 memory token embeddings，连续表示由训练目标压缩得到，底座模型冻结。MAP-VLA [Li25g] 把 expert demonstrations 按任务阶段切分，为每阶段训练一组 soft prompt，推理时按轨迹相似度检索并与 base prompt embedding 相加。ReasonCACHE [Gup26] 把大规模 reasoning demonstrations 压缩成各层可训练的 prefix K/V，与当前 token KV 拼成扩展后的 attention 字典。TokMem [Wu25c] 把一个 procedure 压成单个 memory token embedding，该 token 兼作可路由的离散索引与连续控制向量，由路由器按 query 选取。这类方法介于 textual prompting 与 full fine-tuning 之间，比文本 prompt 紧凑、比微调模块化，适合边界清晰、重复性强的经验模式。

## 4.3 Module-Based Latent Transformation

Module-Based Latent Transformation 构建能动态写入、读取、融合的 latent memory 系统：历史轨迹、多轮交互、视觉观察被编码为 latent entries 存入 memory bank，当前 query、task state 或 visual observation 作为信号检索相关经验，被读取的 memory 经 cross-attention、gating 或 residual connection 影响后续 generation 或 action prediction。

<!-- 训练范围比 §4.2 更宽——多数训练新增的 memory 模块，部分工作（如 MemoryVLA）连同 backbone 端到端训练。 -->

单通道方法维护单一 latent memory。LatentMem [Fu26] 的 latent 在 query 时才生成：它检索多智能体历史轨迹，由 role-aware composer 即时压成定长 latent matrix 拼入 hidden states，同一段经验能按不同 agent role 重新表征；HAMLET [Koo25] 用可学习的 moment tokens 每步提取 latent summary，经浅层 Transformer 聚合为 history-aware state；Gated Memory Policy [Gao26] 由二值 memory gate 决定缓存的 latent history 是否经 cross-attention 进入 policy；Chameleon [Guo26] 用 selective state-space dynamics 把多视角视觉与 proprioceptive history 压成 episodic latent state 注入 policy 各层。

双通道方法把经验拆为"感知"与"认知 / 时序"两路分别维护、分别读取。MemoryVLA [Shi25] 分存视觉 perceptual latent 与语言 cognitive latent，经 cross-attention 与 gated residual 融入 action prediction；EchoVLA [Lin25d] 维护持久 scene memory（voxelized 3D feature volume）与 FIFO episodic memory，对应环境级与近程两种时间尺度；Dual Latent Memory [Yu26d] 把多智能体协作经验拆为 perception 与 thinking 两路 latent，在高熵解码时注入 hidden states。

<!-- （Hybrid Self-evolving Structured Memory for GUI Agents [Zhu26] 并行维护 Schematic Tokenized 与 latent 两类 memory，二者无耦合的 integration mechanism，不作 Composite Pipeline 处理，仅为 latent 与 Tokenized 并存的边界示例。） -->

## 4.4 Discussion

三类方法构成连续谱。沿 Cache-Based → Prompt-Based → Module-Based，专用机制投入、表达能力与动态适应性递增，训练与工程成本同向上升；信息保真度则相反——Cache-Based 复用真实 forward pass 的原始产物，保真度最高，Prompt-Based 与 Module-Based 经训练压缩有损。verifiability 沿同一方向递减：Cache-Based 的 KV 尚可追溯到具体历史片段，Prompt-Based 的静态向量已无法对应单条经验，Module-Based 的动态 memory 持续更新最难审计，并独有 staleness、capacity saturation、latent drift 与错误经验累积等失效模式——错误经验进入 latent memory 后既难发现，也无法像 text rule 那样被直接删改。专用机制投入越高、表达能力越强，可检视性与可控性越低，这是 Latent-Space Transformation 内部的核心 trade-off。

Latent-Space Transformation 相对集中在 embodied / VLA 场景，纯文本 reasoning agent 中的应用明显更少。原因在于经验的可 tokenize 程度：视觉、空间等经验难以无损写成离散文本，latent 化收益最大；文本推理经验本可直接以可读形式保存，latent 化的动力相应较弱。