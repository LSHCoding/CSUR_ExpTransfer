# §1 Introduction

从静态大语言模型（LLM、VLM 等）到自主 Agent 的转变，不仅意味着模型能力的增强，更带来了一个根本性的变化：Agent 在持续的 *experience loop* 中运作——它在具体决策上下文下尝试任务、产生异构动作（推理轨迹、工具调用、环境控制等）、观察环境返回的客观后果，并可选择接收评价反馈。这些累积的决策证据构成了 *agent experience*，最初以原始日志形式存在。

直接保留原始日志并通过检索复用（如 RAG）虽然直观，但在长程 Agent、test-time search、过程级监督等近期趋势的推动下，规模上迅速变得昂贵且脆弱：上下文窗口受限阻碍长期保留，检索延迟拖慢决策，单条 episode 的噪声妨碍跨任务泛化。社区由此发展出多种存储与复用经验的机制——不同机制对应不同载体形式，各自呈现不同的可复用性（reusability）、可验证性（verifiability）、推理成本（inference cost）与鲁棒性（robustness）权衡画像。不存在普适最优载体，最优选择依赖下游任务约束。

本文的核心立意是：不按传统的"组件"（Memory / Planning / Tool Use）或"技术"（SFT / RAG / RLHF）维度分类，而是以 **Experience 的 Transformation 与 Utilization** 为主线，将 memory、evaluator、training 视为同一语义记录在不同载体间的 representation-to-representation pathway，在统一框架下比较其 trade-off，并分析 LLM-based Agent 如何将交互经验转化为不同形式的载体，在不同决策场景中复用。

具体而言，本文将经验的最小语义单元定义为模态无关的四元组 \(e = (c, a, o, f)\)，分别对应上下文（Context）、动作（Action）、观察（Observation）与反馈（Feedback）。经验载体按存在层次分为三大类：**Tokenized**（离散 token 序列，占用 context window）、**Latent**（连续向量或 hidden state，参与 attention 计算）和 **Parametric**（固化于网络权重，完全隐式）。Tokenized 内部按形式化程度进一步区分 Narrative 与 Schematic；Parametric 内部按功能角色区分 Policy 与 Evaluator。

经验转化（Experience Transformation）定义为经验在不同载体之间的迁移过程 \(\mathcal{T}: \mathcal{C}_{\text{src}} \rightarrow \mathcal{C}_{\text{tgt}}\)，需同时满足两个条件：源端内容可追溯至 agent 经验记录（经验语义锚定），目标载体编码了源经验的语义内容（经验内容承载）。

在此框架下，本文识别出 7 条基础转化路径，按载体源端聚合为 4 组：

- **Tokenized 内部转化**（§3）：Narrative → Narrative（P1，同层语义抽象），Narrative → Schematic（P2，同层形式化）；
- **Tokenized → Latent**（§4）：P3，将离散经验压缩为连续计算状态；
- **Tokenized → Parametric**（§5）：Tokenized → Evaluator（P4，经验固化为评估能力），Tokenized → Policy（P5，经验固化为决策能力）；
- **Parametric 源端转化**（§6）：Evaluator → Policy（P6，偏好对齐），Parametric → Tokenized（P7，隐式经验外化）。

除单路径外，本文还将复合路径（Composite Pipelines，§7）作为独立章节，分析将多路径链式组合作为整体方法的工作，识别 composition pattern 并分析 integration mechanism。最后，通过跨路径综合（Cross-Pathway Synthesis，§8）对比各路径的 trade-off、分析 utilization 驱动力并给出场景化推荐，再以开放问题与未来方向（§9）收束全文。

在方法论上，本文的纳入标准要求数据同时具备决策过程语义（可映射为 \(e = (c, a, o, f)\) 结构）和异构动作空间（Action 属于 LLM-based system 的 heterogeneous action space）。排除范围包括：静态语料预训练、单步分类 SFT、纯模型蒸馏（Parametric → Parametric，经验语义链断裂）、纯视觉基础模型训练，以及非 LLM-based 系统。经验来源不限（Agent 自身轨迹 / 人类专家示范 / Teacher model 合成），判定依据底层机制而非论文自我定位。

本文的主要贡献包括：（1）提出以经验转化为轴心的统一框架，为 LLM-based Agent 的经验复用提供跨子领域的共同分析语言；（2）系统梳理 7 条转化路径及相关文献，揭示各路径的机制特征、trade-off 与演化趋势；（3）识别并解剖复合路径的 composition pattern，填补单路径分析无法覆盖的空白；（4）提供跨路径对比与场景化推荐，为后续研究的方法选型提供参考。
