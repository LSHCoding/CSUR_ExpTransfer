# 1. Introduction

从静态大语言模型（LLM、VLM 等）到自主 Agent 的转变，不仅意味着模型能力的扩展，更带来一个根本性变化：Agent 在持续的 experience loop 中运作——在具体决策上下文下尝试任务、产生异构动作（推理轨迹、工具调用、环境控制等）、观察环境返回的客观后果，并可选地接收评价反馈。这些累积的决策证据构成 agent experience，最初以原始日志（raw trajectory）形式存在。

直接保留原始日志并通过检索复用（如 RAG）虽然直观，但在长程 Agent、test-time search 和过程级监督等近期趋势的推动下，于规模上迅速变得昂贵且脆弱。上下文窗口受限阻碍长期保留，检索延迟拖慢决策，单条 episode 的噪声妨碍跨任务泛化。社区由此发展出多种存储与复用经验的机制，对应不同的载体形式——自然语言总结、可执行代码技能、continuous memory tokens、reward model 权重、policy 参数等——各自呈现不同的可复用性、可验证性、推理成本与鲁棒性权衡画像。不存在普适最优载体，最优选择依赖下游任务约束。

本文的核心立意是不按传统的"组件"（Memory / Planning / Tool Use）或"技术"（SFT / RAG / RLHF）维度分类，而是以 Experience 的 Transformation 与 Utilization 为主线，将 memory、evaluator、training 视为同一语义记录在不同载体间的 representation-to-representation pathway，在统一框架下比较其 trade-off，并分析 LLM-based Agent 如何将交互经验转化为不同形式的载体、在不同决策场景中复用。

本文将经验的最小语义单元定义为模态无关的四元组 $e = (c, a, o, f)$，分别对应 Context（决策上下文）、Action（异质动作）、Observation（环境客观后果）与 Feedback（评价信号）。经验载体（Experience Carrier）按存在层次分为三个顶层类别：Tokenized——以离散 token 序列形式显式存在于模型输入端，占用 context window，内部按形式化程度进一步区分为 Narrative（弱形式化，依赖语言/多模态理解复用）与 Schematic（强形式化，依赖 parsing/execution/graph traversal 复用）；Latent——以连续向量或 hidden state 形式存在，直接参与 attention 或 hidden-state 计算，是人类不可直接阅读的中间表示层；Parametric——固化在神经网络权重分布中，完全隐式，推理时不占用 context，内部按功能角色区分为 Policy（actor 权重）与 Evaluator（RM/PRM/verifier 等判断器权重）。Modality（文本/视觉/GUI/具身）、Abstraction level（raw/refined）与 Experience Source（{self}/{human}/{teacher}）作为正交属性标签贯穿所有载体，不构成独立分类维度。

经验转化（Experience Transformation）定义为经验在不同载体之间的迁移过程 $\mathcal{T}: \mathcal{C}_{\text{src}} \rightarrow \mathcal{C}_{\text{tgt}}$，需同时满足两个条件：源端内容可追溯至 agent 经验记录（经验语义锚定），目标载体编码了源经验的语义内容（经验内容承载）。

在此框架下，本文识别出 7 条基础转化路径，按源载体类型聚合为 4 组：

- **Tokenized 内部转化**（§3）：Narrative Abstraction 将原始叙事经验提炼为更高层的自然语言洞察、规则或反思（载体转化 Narrative → Narrative），Schematic Formalization 将叙事经验转化为可解析、可执行或可遍历的结构化 artifact（载体转化 Narrative → Schematic）；
- **Tokenized → Latent**（§4）：Latent-Space Transformation 将离散 tokenized 经验转化为可直接参与 attention 计算的连续表示（载体转化 Tokenized → Latent）；
- **Tokenized → Parametric**（§5）：Evaluator Internalization 将交互经验固化为参数化评估器的判断能力（载体转化 Tokenized → Evaluator），Policy Internalization 将交互经验固化为参数化策略的决策能力（载体转化 Tokenized → Policy）；
- **Parametric 源端转化**（§6）：Evaluator-Driven Optimization 将已内化的评估器能力转化为驱动策略更新的监督信号（载体转化 Evaluator → Policy），Parametric Externalization 将参数化模型中已内化的经验外化为可被其他系统消费的 tokenized artifact（载体转化 Parametric → Tokenized）。

除单路径外，本文还将复合路径（Composite Pipelines，§7）作为独立章节，识别那些将多路径链式或闭环式组合作为整体方法的工作，按衔接机制（integration mechanism）划分为 Evaluator–Policy Co-Evolution、Refinement-Mediated Policy Internalization 与 Generative Experience Curation 三类 pattern，并分析各自的 composition topology 与失效模式。跨路径综合（Cross-Pathway Synthesis，§8）对比各路径的 trade-off 画像、分析 utilization 驱动力并给出场景化推荐，开放问题与未来方向（§9）收束全文。

在方法论上，本文的纳入标准要求数据同时具备决策过程语义（可映射为 $e = (c, a, o, f)$ 结构）和异构动作空间（Action 属于 LLM-based system 的 heterogeneous action space）。排除范围包括：静态语料预训练（无决策过程语义）、单步分类/标注任务的 SFT（非异构动作空间）、纯模型蒸馏 Parametric → Parametric（经验语义链断裂）、纯视觉基础模型训练（无序贯决策语义），以及非 LLM-based 系统。经验来源不限（Agent 自身轨迹、人类专家示范、Teacher model 合成），判定依据底层机制而非论文自我定位。

本文的主要贡献包括：（1）提出以经验转化为轴心的统一框架，为 LLM-based Agent 的经验复用提供跨子领域的共同分析语言；（2）系统梳理 7 条转化路径及相关文献，揭示各路径的机制特征、trade-off 与演化趋势；（3）识别并解剖复合路径的 composition pattern，填补单路径分析无法覆盖的衔接机制空白；（4）提供跨路径对比与场景化推荐，为后续研究的方法选型提供参考。
