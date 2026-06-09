# 4. Latent-Space Transformation：Tokenized-to-Latent Transformations

Latent-Space Transformation 把 Tokenized Agent Experience 转化为连续表示，使其直接进入 attention 或 hidden-state computation。使用 latent 而非 token 的核心原因在于：模型处理一段 Tokenized experience 时会形成离散 token 无法完整复原的内部状态——逐层上下文表示、注意力对历史的组织、对经验消化后的理解；把经验解码回 token 再读入会丢弃这部分理解。Latent-Space Transformation 复用的正是这些内部表示状态。它由此处在 Tokenized 与 Parametric 之间：经验不再是模型之外的可读符号，也尚未固化进权重。

KV cache eviction 等推理优化方法虽操作 KV / hidden states，但不承载长程经验复用语义。本文只纳入 latent 表示明确承担经验存储与复用功能的方法。按获取 latent 表示所需的机制，分为三类：**Cache-Based** 不训练，直接复用历史 forward pass 产生的真实 KV / hidden states；**Prompt-Based** 通过训练把经验压缩为静态连续提示，底座冻结；**Module-Based** 通过训练构建带写入、读取、融合的动态 latent memory 系统。

## 4.1 Cache-Based Latent Transformation

Cache-Based Latent Transformation 不训练，直接保存并复用模型历史交互中产生的 KV cache 或隐藏状态。Memorizing Transformers [Wu22] 确立了机制基础：把先前 token 在中间层的 key-value 对写入外部 memory，后续时间步通过 kNN 检索接入 attention。LAG [Che25b] 将其用于推理 agent 的自生成经验：对历史推理日志做完整前向传播，只为选中的少量 token 持久化 KV，推理时检索相关日志并将其 KV 注入当前推理。TempoFit [Sun26] 推进到具身场景：在 VLA 上把早先时间步的 layer-wise KV 存入 memory，检索后注入当前 attention，支撑 long-horizon episode 内的历史继承。

## 4.2 Prompt-Based Latent Transformation

Prompt-Based Latent Transformation 通过训练把经验转化为一组连续向量，底座模型冻结。MAP-VLA [Li25g] 把 expert demonstrations 按任务阶段切分，为每阶段训练一组 soft prompt，推理时按轨迹相似度检索并与 base prompt embedding 相加。ReasonCACHE [Gup26] 把大规模 reasoning demonstrations 编码为各层可训练的 prefix K/V，与当前 token KV 拼成扩展后的 attention 字典。TokMem [Wu25c] 把一个过程性流程编码为单个 memory token embedding，该 token 兼作可路由的离散索引与连续控制向量，由路由器按 query 选取。

## 4.3 Module-Based Latent Transformation

Module-Based Latent Transformation 构建能动态写入、读取、融合的 latent memory 系统：Agent 交互过程中的历史观察与动作被编码为 latent entries 进入 memory，推理时按当前状态检索相关条目，被读取的 latent 经 cross-attention 或 gating 融入后续 generation 或 action 输出。

单通道方法维护一路 latent。LatentMem [Fu26] 的 latent 在 query 时才生成：它检索多智能体历史轨迹，由 role-aware composer 即时压成定长 latent matrix 拼入 hidden states，同一段经验能按不同 agent role 重新表征；HAMLET [Koo25] 用可学习的 moment tokens 每步提取 latent summary，经浅层 Transformer 聚合为 history-aware state；GMP [Gao26] 由二值 memory gate 决定缓存的 latent history 是否经 cross-attention 进入 policy；Chameleon [Guo26] 用 selective state-space dynamics 把多视角视觉与 proprioceptive history 压成 episodic latent state 注入 policy 各层。

多通道方法把经验拆为承担不同语义角色的多路 latent，分别维护、分别读取。MemoryVLA [Shi25] 分存视觉 perceptual latent 与语言 cognitive latent，经 cross-attention 与 gated residual 融入 action prediction；EchoVLA [Lin25d] 维护持久 scene memory（voxelized 3D feature volume）与 FIFO episodic memory，对应空间级与时序近程两种维度；L²-VMAS [Yu26d] 把多智能体协作经验拆为 perception 与 thinking 两路 latent，在高熵解码时注入 hidden states。

## 4.4 Discussion

三类方法的差异可沿 Cache-Based → Prompt-Based → Module-Based 系统展开。从前往后，实现复杂度与训练投入递增，能容纳的历史经验长度和动态适应性也递增；反方向，经验的可读性与可追溯性递减——Cache-Based 的 KV 直接来自真实前向传播，能对应到具体历史片段；Prompt-Based 的静态向量难以再对应到单条经验；Module-Based 的动态 memory 不断改写，出处最难追到。Prompt-Based 在更宽视角下也居于无训练的 in-context prompting 与全量 fine-tuning 之间，这一中间位置与其在本章三类中的中段位置一致。

Module-Based 还有几个特有问题：memory 会过时、容量饱和后旧条目被覆盖、latent 表示随训练漂移、错误经验进入后难以发现。这些条目不像 Tokenized 载体那样可以直接读和改写，错误一旦写入很难单独清理。实现复杂度越高、表达能力越强，可检视性与可控性越低。

三类方法目前都集中在 embodied / VLA 场景，纯文本 reasoning agent 中的应用明显更少。原因在于经验的可 tokenize 程度：视觉、空间、proprioceptive 等经验难以无损写成离散 token，latent 化收益最大；文本推理经验本可直接以可读形式保存，latent 化的动力相应较弱。


**Table 4.1.** Overview of Latent-Space Transformation methods.

<!-- 列定义：**Acquisition Mechanism** 记录获取 latent 表示所需的机制（是否训练、训练何物）；**Latent Encoding** 记录连续表示的具体形态；**Memory Structure** 记录维护的 latent 通道数；**Retrieval** 记录推理时如何选中相关 latent；**Fusion** 记录被选中的 latent 以何种方式进入前向计算；**Modality** 记录经验的模态；**Source**（可选）记录经验来源。各列取值集合：Acquisition Mechanism ∈ {`Cache-based`, `Prompt-based`, `Module-based`}；Latent Encoding ∈ {`KV/hidden states`, `soft prompt`, `prefix K/V`, `memory token`, `composed latent`, `feature volume`, `SSM latent`}；Memory Structure ∈ {`single-stream`, `multi-stream`}；Retrieval ∈ {`always-injected`, `kNN`, `similarity`, `role-aware`, `query-routed`, `gated-admit`}；Fusion ∈ {`attention-injection`, `additive`, `concatenation`, `cross-attention`, `gated-residual`, `SSM-injection`}；Modality ∈ {`text`, `visual`, `GUI`, `embodied`, `cross-modal`}；Source* ∈ {`self`, `human`, `teacher`}。 -->

| Work | Acquisition Mechanism | Latent Encoding | Memory Structure | Retrieval | Fusion | Modality |
|------|------------------------|-----------------|------------------|-----------|--------|----------|
| [Wu22]† | Cache-based | KV/hidden states | single-stream | kNN | attention-injection | text |
| [Che25b] | Cache-based | KV/hidden states | single-stream | similarity | attention-injection | text |
| [Sun26] | Cache-based | KV/hidden states | single-stream | similarity | additive | embodied |
| [Li25g] | Prompt-based | soft prompt | single-stream | similarity | additive | embodied |
| [Gup26] | Prompt-based | prefix K/V | single-stream | always-injected | attention-injection | text |
| [Wu25c] | Prompt-based | memory token | single-stream | query-routed | concatenation | text |
| [Fu26] | Module-based | composed latent | single-stream | similarity | concatenation | text |
| [Koo25] | Module-based | composed latent | single-stream | always-injected | concatenation | embodied |
| [Gao26] | Module-based | composed latent | single-stream | gated-admit | gated-residual | embodied |
| [Guo26] | Module-based | SSM latent | single-stream | query-routed | SSM-injection | embodied |
| [Shi25] | Module-based | memory token | multi-stream | similarity | gated-residual | embodied |
| [Lin25d] | Module-based | feature volume | multi-stream | similarity | cross-attention | embodied |
| [Yu26d] | Module-based | KV/hidden states | multi-stream | similarity | attention-injection | cross-modal |
