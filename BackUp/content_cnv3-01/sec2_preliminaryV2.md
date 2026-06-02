# 2. Preliminaries: Experience, Carriers, and Transformations

本节建立全文的概念体系。§2.1 从 Russell & Norvig 的 rational agent 定义出发，锚定 agent 的工作定义并引出决策依据的二分结构。§2.2 定义经验的最小语义单元，并论证为何经验——而非 trajectory、memory 或 feedback——是组织本领域的正确抽象。§2.3 定义经验载体的三层分类体系。§2.4 给出经验转化的判定标准。§2.5 列出七条基础转化路径。§2.6 在所有概念就位后，给出选择"载体间转化"作为组织轴的完整论证。

## 2.1 Agent

*Artificial Intelligence: A Modern Approach*（Russell & Norvig, 4th ed.）将 agent 定义为"任何能够通过传感器感知环境、并通过执行器对环境施加作用的实体"。rational agent 的定义则更进一步：对于每一种可能的感知序列（percept sequence），理性 agent 应选择一个在该感知序列所提供的证据、**以及 agent 所具有的任何内置知识（built-in knowledge）**之下，期望最大化其性能度量的动作。

这个定义中有一个对本综述至关重要的结构：**决策依据被明确分置于两处**——一处是外部流动的感知序列，另一处是内部积累的内置知识。LLM-based agent 完整落在这个二分上：它在每一步的决策既依赖上下文窗口中显式可见的交互记录（感知序列侧——对话历史、检索文档、工具输出），也依赖已固化在权重中的能力（内置知识侧——世界知识、推理模式、通过训练获得的任务技能）。

本文由此给出 agent 的工作定义：**在任务上下文中执行序贯决策、且决策依据可以同时分布于外部上下文与内部参数的系统。** 这个定义是广义的——环境可以是推理验证器（reasoning verifier）、工具执行器（tool executor）、物理世界（physical world）或另一个 agent——关键特征不是环境的性质，而是决策循环的结构以及决策依据的分布性。这个定义同时划出了全文的纳入边界：系统须具备可映射为经验循环（见 §2.2）的序贯决策语义。静态语料预训练、单步分类/标注 SFT、传统 RL agent 等不在本框架的讨论范围内。

## 2.2 Agent Experience

### 2.2.1 最小语义单元

Agent 与环境的每一次交互产生一个决策事件。每个事件可被记录为一个最小语义单元——模态无关的四元组：

$$e = (c, a, o, f)$$

其中 $c$（Context）为 agent 决策前可获得的信息，$a$（Action）为 agent 当前步骤的输出，$o$（Observation）为环境返回的客观后果，$f$（Feedback）为对 $(c,a,o)$ 或 $(c,a)$ 的可选评价信号。$c$ 和 $a$ 为必需元素，$o$ 和 $f$ 为可选元素——一步动作可能没有可观测的环境后果，也可能没有收到的评价反馈，但这些缺失不影响经验记录的完整性。

一次完整的任务执行产生按时序排列的经验序列，记为轨迹 $\tau = (e_1, e_2, \dots, e_T)$，多条轨迹的集合记为 $\mathcal{D} = \{\tau^{(i)}\}_{i=1}^N$。

### 2.2.2 为什么是"经验"——与三个竞争概念的比较

以"经验"为组织单元的选择并非不证自明。在文献中，trajectory、memory 和 feedback 是三个更为成熟的替代概念，且各自都有以此为轴心的综述或研究传统。本节论证为什么这些概念——尽管在各自语境中有效——无法胜任一个以"跨形式重新表示"为中心论点的综述的组织单元。§2.1 中 R&N 的二分结构恰好为这一比较提供了统一的判据。

**Experience vs. Trajectory（轨迹）。** Trajectory 是 agent 感知序列和动作序列的时序记录——它是经验在 Narrative Tokenized 载体中的一种存在形式。但 R&N 的定义明确指出，agent 的决策依据还包括 built-in knowledge。一个经过 RLHF 训练的策略权重承载了 agent 的决策经验——它影响每一步的动作选择——但它不是任何意义上的 trajectory。以 trajectory 为组织单元，框架就将**结构性无法纳入**整个 Parametric 分支——恰恰是本综述试图与 Tokenized 侧建立关联的那一半。

**Experience vs. Memory（记忆）。** Memory 是一个关于存储位置的概念——它回答"经验放在哪里"，而非"经验是什么"。没有人会将固化在权重中的能力称为 memory，也不会将在 GPU memory 中缓存的 KV cache 称为 memory 系统的一部分——但它们都承载经验。Memory 这个词跨不过 token↔权重这条边界；以它为组织单元，分析会自然局限在 Tokenized 载体及其检索机制中——而这正是本综述试图超越的单组件视角。

**Experience vs. Feedback（反馈）。** Feedback 是经验四元组中的一个元素——$f$ 字段。以部分指代整体会在分类上造成混淆：大量转化路径（Narrative Abstraction、Schematic Formalization、通过 SFT 的 Policy Internalization）操作的是 $(c,a,o)$ 三元组，并不依赖显式 feedback。以 feedback 为组织单元，这些路径的归属就会产生歧义。

上述比较指向同一个结论。本综述的中心论点是：**同一份决策证据在不同形式之间被反复重新表示。** 一个以"重新表示"为论点的综述，其组织单元必须定义在跨形式不变的语义层级上——否则"转化"这一动作连一个稳定的主语都没有。Trajectory 是经验的一种形式，memory 是经验的一个存放位置，feedback 是经验的一个元素。只有 $e = (c, a, o, f)$ 定义在"决策证据是什么"这个层级，不预设它以何种形式存在、存放在何处——它正是 §2.1 R&N 二分中那个横跨感知序列与内置知识两侧、并在两侧之间迁移时保持不变的语义内容。

## 2.3 Experience Carriers

### 2.3.1 分类轴

最小语义单元 $e$ 描述经验的语义内容。Experience Carrier 描述经验在模型架构中的**存在形式**，是分析转化路径的源端与目标端的基础坐标。

Carrier 分类沿"经验在模型架构中的存在层次"这条主轴切分。这个选择的考量是：存在层次直接映射到 agent 系统关心的核心 trade-off——可解释性（人类能否直接阅读经验内容）、推理效率（复用经验是否需要重新支付前向传播成本）、可编辑性（能否在不重新训练的情况下修改经验）——使分类本身携带分析维度；存在层次与模态正交，任意模态的经验都可存在于任一存在层次，多模态工作由此自然融入框架；存在层次直接对应载体形式的根本差异，最大化 pathway 分类的判别力。

### 2.3.2 三顶层类别与连续谱

Carrier 分为三个顶层类别，构成 Tokenized → Latent → Parametric 连续谱。沿此方向：可解释性与可编辑性递减，推理效率递增；存储位置从外部数据库/prompt → GPU memory → model checkpoint。

**Tokenized Carriers（Token 化载体，$\mathcal{C}^T$）。** 以离散 token 序列形式显式存在于模型前向传播的输入端。涵盖 text tokens、visual patch tokens、action tokens、serialized structural tokens（如序列化的 graph/code/workflow token）等，不限于自然语言文本。占用 context window，推理时需完整处理。按形式化程度分为两个子类：

- **Narrative Tokenized（叙事型，$\mathcal{C}^T_N$）**：以自然语言或感知顺序组织的弱形式化载体，通过 language/multimodal understanding 复用。典型形式：raw trajectories、reflections、summaries、natural-language rules、skill descriptions、screenshots、video sequences。
- **Schematic Tokenized（图式型，$\mathcal{C}^T_S$）**：以语法结构或拓扑结构组织的强形式化载体，通过 parsing、execution 或 graph traversal 复用。典型形式：executable code skills、workflows、DAGs、knowledge graphs、decision trees、structured memory graphs。

Raw trajectories 是 Narrative Tokenized 的零度抽象特例——未经提炼的 Narrative 载体，而非独立于载体体系之外的原材料。

**Latent Carriers（隐空间载体，$\mathcal{C}^L$）。** 以连续向量或 hidden state 形式存在，直接参与模型 attention 或 hidden-state 计算。不等同于离散 token（不占用 context window），也不固化在权重中（不改变模型参数），是介于 Tokenized 与 Parametric 之间的桥梁层。典型形式：KV cache、prefix cache、learnable soft prompts、continuous memory tokens、latent memory bank。可按实现形态区分 session-scoped（无需训练，如 KV cache）与 cross-session reusable（需训练，如 soft prompts），不作为正式分类子类。

**Parametric Carriers（参数化载体，$\mathcal{C}^P$）。** 经验固化在神经网络权重分布中，完全隐式。推理时不占用 context，直接前向传播输出；修改需再训练，可编辑性最低。按功能角色分为两个子类：

- **Policy Parameters（策略参数，$\mathcal{C}^P_\pi$，π-Par）**：生成动作 $a$ 的 actor 权重，涵盖 LLM agent、VLA、GUI agent 权重及 LoRA adapters。
- **Evaluator Parameters（评估器参数，$\mathcal{C}^P_\phi$，V-Par）**：评估 $(c,a,o,f)$ 的判断器权重，涵盖 reward models、PRM、verifiers、critics、VLM judges。

Evaluator 参数的位置在转化路径组织中具有特殊意义：它既可作为 Tokenized → Evaluator（Evaluator Internalization）的终点，也可作为 Evaluator → Policy（Evaluator-Driven Optimization）的起点，形成跨路径的衔接枢纽。

### 2.3.3 正交属性

以下三个维度作为每个 carrier 实例的属性标签，不构成独立分类维度：

| 属性 | 取值 | 用途 |
|---|---|---|
| **Modality** | textual / visual / GUI / embodied / cross-modal | 在每条 pathway 中讨论不同模态下的实现差异 |
| **Abstraction Level** | raw / refined | 区分原始轨迹与精炼衍生物，主要在 Tokenized 层内体现 |
| **Experience Source** | {self} / {human} / {teacher} | 讨论经验来源对 pathway 选择的影响 |

### 2.3.4 边界澄清

**Embedding 的分层归属。** 按用途区分：Embedding 作为外部 memory 的检索索引（retrieve 后再进入 context），归入所索引 Tokenized 内容的附加机制；Embedding 作为可学习的 memory 表示（不解码回 token，直接参与模型 attention），归入 Latent。

**Raw experience 的定位。** Raw trajectories 是 Narrative Tokenized 的最低抽象程度特例。Transformation 通常以 raw 为起点，目标是提升抽象程度、改变形式化程度或改变存在层次。

## 2.4 Experience Transformation

经验转化（Experience Transformation）指经验在不同载体之间的迁移过程。一个映射

$$\mathcal{T}: \mathcal{C}_{\text{src}} \rightarrow \mathcal{C}_{\text{tgt}}$$

构成经验转化，当且仅当同时满足两个条件：

**条件 1——经验语义锚定（Experience Grounding）。** 源端内容可追溯至一条或多条经验记录 $e = (c, a, o, f)$ 或由其派生。此条件排除虽操作同类型数据但不追溯至具体 agent 决策过程的通用处理（如通用语料预训练）。

**条件 2——经验内容承载（Experience Embodiment）。** 目标载体编码了源经验的语义内容。此条件排除纯格式转写（如 JSON trajectory → Markdown）——载体可能改变，但若语义内容未在目标端被实质性编码，则不构成经验转化。

两个条件共同保证分析对象聚焦于经验的**实质性转化**，而非数据格式的机械变换。

## 2.5 Seven Transformation Pathways

在上述定义框架下，本文识别出 7 条基础转化路径，沿源载体类型聚合为 §3–§6 四个 Section：

| 路径 | 源载体 → 目标载体 | 定义 | Section |
|---|---|---|---|
| Narrative Abstraction | $\mathcal{C}^T_N \rightarrow \mathcal{C}^T_N$ | Narrative → Narrative：同层语义抽象（raw → reflections/rules/insights） | §3 |
| Schematic Formalization | $\mathcal{C}^T_N \rightarrow \mathcal{C}^T_S$ | Narrative → Schematic：同层形式化（logs → code/workflows/graphs） | §3 |
| Latent-Space Transformation | $\mathcal{C}^T \rightarrow \mathcal{C}^L$ | Tokenized → Latent：跨层压缩（trajectories → KV cache/soft prompts/memory tokens） | §4 |
| Evaluator Internalization | $\mathcal{C}^T \rightarrow \mathcal{C}^P_\phi$ | Tokenized → Evaluator：评估器内化（trajectories → RM/PRM/verifier） | §5 |
| Policy Internalization | $\mathcal{C}^T \rightarrow \mathcal{C}^P_\pi$ | Tokenized → Policy：策略内化（trajectories → policy weights via SFT/RL） | §5 |
| Evaluator-Driven Optimization | $\mathcal{C}^P_\phi \rightarrow \mathcal{C}^P_\pi$ | Evaluator → Policy：偏好对齐（RM 信号 → policy weights via RLHF/DPO） | §6 |
| Parametric Externalization | $\mathcal{C}^P \rightarrow \mathcal{C}^T$ | Parametric → Tokenized：知识外化（weights → synthetic trajectories/demonstrations） | §6 |

**复合路径的处理。** 当单篇论文将多路径链式或闭环式组合作为整体方法时（如 Narrative → Schematic → Parametric 的技能内化流水线，或 Policy → Tokenized → Policy 的自生成环路），其贡献点在于路径间的衔接机制（integration mechanism），而非任一单路径本身。此类工作在独立的 §7 Composite Pipelines 中作为 first-class 对象讨论。单篇论文中偶现的两条独立转化则分别在对应单路径 Section 中引用相关片段。

## 2.6 Why Transformation as the Organizing Axis

§2.2 论证了"经验"是正确的组织单元——它是跨 carrier 不变的语义内容。本节论证"载体间转化"是正确的组织轴——它捕捉了该领域在 2023–2026 年间最根本的演变逻辑。

### 2.6.1 两个层级的问题

理解本综述的组织轴选择，需要先区分两个不同层级的问题。

**载体内优化（Intra-Carrier Optimization）。** 更好的检索、更好的 prompt 设计、更好的模型架构——这三者的共同特征是它们都在**一个固定载体的内部**做优化。检索改善的是"在 Tokenized 载体内更快找到对的那条经验记录"；prompt 设计改善的是"在 Tokenized 载体内更有效地排布多条经验"；架构改进（如更高效的 attention、更大的 context window）改善的是"某一种载体被模型处理的效率"。这些改进都是真实且有效的，但它们提升的是经验在**某一种**表示下的利用效率。

**载体间转化（Inter-Carrier Transformation）。** 载体间转化处理的，是载体内优化在定义上够不到的问题：**载体本身的 trade-off 天花板**。一个以 Tokenized Narrative 形式存在的经验记忆，无论检索器做得多精确，都仍然占用上下文窗口、且每次复用都要重新支付完整的推理成本——这不是检索质量的缺陷，而是 Tokenized 载体的固有属性。同样地，一个以 Parametric 形式固化在权重中的能力，无论训练得多好，都无法在单条经验粒度上被检查或编辑——这不是训练技术的缺陷，而是 Parametric 载体的固有属性。要突破这类天花板，唯一的途径是更换载体：将经验从 Tokenized 内化进 Parametric（获得无需检索、推理成本可摊销的快速决策），从 Tokenized 压缩进 Latent（省去前置编码开销），或从 Parametric 外化回 Tokenized（重获可检查性和可编辑性）。

两者的关系不是竞争性的——载体内优化和载体间转化解决的是不同粒度的问题——而是互补的：载体内优化决定了经验在当前载体中的利用效率，载体间转化决定了经验能否抵达更适合当前任务约束的载体。

### 2.6.2 历史叙事作为证据

当以载体迁移为透镜回看 2023–2026 年的 agent 研究史，一条连贯的演变主线浮现出来。

Agent 产生的经验最初以 raw trajectory 的形式存在——最自然、最完整的记录方式，对应 Narrative Tokenized 载体。社区很快发现，直接以 raw + RAG 的方式复用经验，会依次撞上三堵墙：上下文窗口限制使长程经验无法完整注入；检索延迟使每一步决策都需要额外的检索耗时；单条 episode 的噪声使跨任务泛化困难。这三堵墙不是检索质量或 prompt 设计的问题——它们是 Tokenized Narrative 载体固有的天花板。

社区的反应构成了一连串的载体迁移。一部分工作将冗长的 raw log 抽象为精炼的 reflection、summary 或 rule（Narrative → Narrative 抽象），本质是在同一载体内压缩语义密度、降低上下文消耗。另一部分工作将叙事性的经验转化为可执行 code、workflow 或 graph（Narrative → Schematic 形式化），本质是改变载体的形式化程度，使经验从"需要被理解"变成"可以直接被执行或遍历"。还有一部分工作将筛选后的高质量轨迹直接内化进模型权重（Tokenized → Policy 内化），本质是放弃 Tokenized 载体的可检查性，换取 Parametric 载体的推理效率和泛化能力。同时，社区发现并非所有经验都需要内化为生成能力——有时只需要内化为判断能力，遂有奖励建模和 PRM（Tokenized → Evaluator 内化），再由评估器信号驱动策略更新（Evaluator → Policy）。此外，连续记忆表示（Tokenized → Latent）和知识外化（Parametric → Tokenized）分别从压缩效率和数据生成的角度填补了载体迁移图景的剩余边。

**记忆摘要、技能归纳、奖励建模、RLHF、KV cache 训练、知识蒸馏——这些在传统分类下分属不同子领域的工作，在转化视角下显露为同一种适应性反应**：当经验在当前载体中触及该载体固有的 trade-off 天花板时，更换载体以重新表示经验。它们不是六个独立的话题，而是同一种基本操作的六条变体。

### 2.6.3 转化视角的独特回报

一个分类框架的价值不在于它是否正确——所有足够宽泛的分类都可以声称自己是正确的——而在于它是否让原本需要逐篇论文事后提取的结构性属性变成了由分类轴本身直接给出的属性。

组件视角（Memory / Planning / Tools）和技术视角（RAG / SFT / RLHF）都是合理的分类，但它们有一个共同的局限：**可解释性、推理成本、可编辑性这三个 agent 系统最关心的维度，在这些分类轴上是杂乱的**。同一个"Memory"标签下，raw trajectory 和 knowledge graph 在可编辑性上差了不止一个数量级；同一个"RLHF"标签下，reward model 训练和 policy optimization 在推理成本上完全不同。要从这些分类中得出 trade-off 判断，读者必须逐篇论文深入细节。

而在转化视角下，这三个 trade-off 是**沿分类轴单调变化**的。Tokenized → Latent → Parametric 方向，可解释性和可编辑性严格递减，推理效率严格递增。这一单调性不是来自对论文的归纳——它来自载体存在层次的物理约束：token 序列天然可读、天然占用上下文；隐向量天然不可直接阅读但计算高效；权重天然完全隐式但前向传播最快。转化视角将 trade-off 从需要逐篇提取的后验属性，变成了由载体分类轴直接给出的结构属性。

这不是给既有分组换标签。这是把分析维度从分类的外部移到了分类的内部。

### 2.6.4 转化与利用的互补

最后需要明确本框架的边界。转化刻画的是经验如何被**生产**为各种载体——这是生产侧的问题。它必须与经验如何被**消费**的利用侧（检索策略、上下文编排、运行时维护、多载体协同调度）配对，完整的 agent 经验管理图景才闭合。本综述以转化为主轴，但不把利用排除在讨论之外——Section 8（Cross-Pathway Synthesis）专门分析利用需求（任务对延迟、可解释性、跨任务泛化的约束）如何反过来驱动转化路径的选择，以及不同载体在实际部署中如何协同工作。转化本身不是完整故事；转化 + 利用才是。
