# 2. Preliminaries: Experience, Carriers, and Transformations

本节建立全文的概念体系。§2.1 给出 agent 的工作定义与决策规则;§2.2 定义经验的最小语义单元;§2.3 给出经验载体的三层分类;§2.4 给出经验转化的判定标准、基础路径,以及转化在整体经验管理图景中的位置。

## 2.1 Agent

本文关注的 agent 是在任务上下文中执行序贯决策的系统:每一步依据当前可获得的信息选择一个动作,环境据此更新,新的信息进入下一步。沿用序贯决策 agent 的标准刻画 [Russell and Norvig 2021],将第 $t$ 步的决策写为

$$a_t \sim \pi_\theta(\cdot \mid c_t),$$

其中 $c_t$ 是该步外部可见的上下文(指令、历史交互、检索内容、环境观测),$\theta$ 是 agent 的内部参数,$\pi_\theta$ 为由参数决定的策略。

这条决策规则把决策依据分置于两处:流经 $c_t$ 的外部信息,与固化在 $\theta$ 中的内部能力。LLM-based agent 同时使用两者——上下文窗口中显式可见的交互记录(对话历史、检索文档、工具输出),以及训练所得的权重(世界知识、推理模式、任务技能)。同一份经验既可存在于 $c_t$ 一侧(外部、显式),也可存在于 $\theta$ 一侧(内部、隐式),这一分布性是 §2.3 区分载体的出发点。

环境的性质不进入这个定义——它可以是 reasoning verifier、tool executor、physical world 或另一个 agent。纳入本框架的判据是决策循环的结构:系统须具备可映射为经验循环(§2.2)的序贯决策语义。静态语料预训练、单步分类/标注 SFT、传统 RL agent 因不满足这一结构,不在讨论范围内。

## 2.2 Agent Experience

Agent 与环境的每一次交互产生一个决策事件,记录为一个模态无关的四元组:

$$e = (c, a, o, f),$$

其中 $c$(Context)为决策前可获得的信息,$a$(Action)为该步输出的动作,$o$(Observation)为环境返回的客观后果,$f$(Feedback)为对 $(c,a,o)$ 或 $(c,a)$ 的评价信号。$c$ 与 $a$ 必需,$o$ 与 $f$ 可选——一步动作未必产生可观测后果,也未必收到评价反馈,缺失不影响记录的完整性。$c$、$a$ 即 §2.1 决策规则中的上下文与动作,$o$、$f$ 记录环境在动作之后的返回。

一次完整任务执行产生按时序排列的经验序列,记为轨迹 $\tau = (e_1, \dots, e_T)$;多条轨迹的集合记为 $\mathcal{D} = \{\tau^{(i)}\}_{i=1}^N$。

经验是本文组织全文的基本单元。它定义在"决策证据是什么"这一层级,不预设证据以何种形式存在、存放于何处,横跨 §2.1 的外部/内部两侧。

## 2.3 Experience Carriers

最小语义单元 $e$ 描述经验的语义内容;experience carrier 描述经验在模型架构中的**存在形式**,是刻画转化路径源端与目标端的基础坐标。

### 2.3.1 分类轴

Carrier 沿"经验在模型架构中的存在层次"切分。这条轴直接映射到 agent 系统关心的三个 trade-off——可解释性(人类能否直接阅读经验内容)、推理效率(复用经验是否需重新支付前向传播成本)、可编辑性(能否不经再训练修改经验)。它与模态正交:任意模态的经验都可存在于任一存在层次。它捕捉载体形式的根本差异,为转化路径的分类提供判别基础。

### 2.3.2 三个顶层类别

Carrier 分为三类,构成 Tokenized → Latent → Parametric 连续谱。沿此方向,可解释性与可编辑性递减,推理效率递增,存储位置由外部数据库/prompt 移至 GPU memory 再到 model checkpoint。

**Tokenized Carriers（$\mathcal{C}^T$）** 以离散 token 序列显式存在于前向传播的输入端,涵盖 text tokens、visual patch tokens、action tokens、序列化的 graph/code/workflow token 等,不限于自然语言。占用 context window,推理时需完整处理。按形式化程度分两子类:

- **Narrative Tokenized（$\mathcal{C}^T_N$）**:以自然语言或感知顺序组织的弱形式化载体,通过 language/multimodal understanding 复用。典型形式:trajectories、reflections、summaries、natural-language rules、skill descriptions、screenshots、video sequences。
- **Schematic Tokenized（$\mathcal{C}^T_S$）**:以语法或拓扑结构组织的强形式化载体,通过 parsing、execution 或 graph traversal 复用。典型形式:executable code skills、workflows、DAGs、knowledge graphs、decision trees、structured memory graphs。

Trajectories 是抽象层级最低的 Narrative Tokenized 载体,转化通常以它为起点。

**Latent Carriers（$\mathcal{C}^L$）** 以连续向量或 hidden state 存在,直接参与 attention 或 hidden-state 计算;不占用 context window,也不改变模型权重,位于 Tokenized 与 Parametric 之间。典型形式:KV cache、prefix cache、learnable soft prompts、continuous memory tokens、latent memory bank。可按是否需训练区分 session-scoped(如 KV cache)与 cross-session reusable(如 soft prompts),不作为正式子类。检索式 RAG 中用于索引的 embedding 在 retrieve 后仍解码回 token 进入 context,归入所索引 Tokenized 内容的检索机制;只有不解码回 token、直接参与 attention 的可学习表示才属 Latent。

**Parametric Carriers（$\mathcal{C}^P$）** 经验固化在网络权重中,完全隐式;推理时不占用 context,直接前向输出,修改需再训练。按功能角色分两子类:

- **Policy Parameters（$\mathcal{C}^P_\pi$）**:生成动作 $a$ 的 actor 权重,即 §2.1 决策规则中的 $\theta$,涵盖 LLM agent、VLA、GUI agent 权重及 LoRA adapters。
- **Evaluator Parameters（$\mathcal{C}^P_\phi$）**:评估 $(c,a,o,f)$ 的判断器权重,涵盖 reward models、PRM、verifiers、critics、VLM judges。

Evaluator 参数在路径组织中是衔接枢纽:既是 Evaluator Internalization 的终点,又是 Evaluator-Driven Optimization 的起点。

## 2.4 Experience Transformation

经验转化指经验 $e=(c,a,o,f)$ 或其派生物被**重新表示**为另一载体的过程,记为 $\mathcal{T}: \mathcal{C}_{\text{src}} \rightarrow \mathcal{C}_{\text{tgt}}$。重新表示要求目标载体是从源经验重新推导或编码而来的新形式:抽象层级的提升(trajectories → reflections)、形式化程度的改变(trajectories → code)、存在层次的迁移(tokenized → parametric)。源端与目标端是否同属一个顶层类别不影响判定——Narrative → Narrative 的语义抽象同样产生新形式。

只搬运而不重新表示原始记录的操作不在此列:重新序列化(同一 trajectory 的 JSON ↔ Markdown)改写的是语法,子集筛选与轨迹截断保留的是原始记录的一部分或一个前缀,留存内容仍以原形式存在,未被编码成新载体。

在此判定下,本文识别 7 条基础转化路径,按源载体类型聚合为 §3–§6:

| 路径 | 源载体 → 目标载体 | 定义 | Section |
|---|---|---|---|
| Narrative Abstraction | $\mathcal{C}^T_N \rightarrow \mathcal{C}^T_N$ | Narrative → Narrative:同层语义抽象（trajectories → reflections / rules / insights） | §3 |
| Schematic Formalization | $\mathcal{C}^T_N \rightarrow \mathcal{C}^T_S$ | Narrative → Schematic:同层形式化（logs → code / workflows / graphs） | §3 |
| Latent-Space Transformation | $\mathcal{C}^T \rightarrow \mathcal{C}^L$ | Tokenized → Latent:跨层压缩（trajectories → KV cache / soft prompts / memory tokens） | §4 |
| Evaluator Internalization | $\mathcal{C}^T \rightarrow \mathcal{C}^P_\phi$ | Tokenized → Evaluator:评估器内化（trajectories → RM / PRM / verifier） | §5 |
| Policy Internalization | $\mathcal{C}^T \rightarrow \mathcal{C}^P_\pi$ | Tokenized → Policy:策略内化（trajectories → policy weights via SFT / RL） | §5 |
| Evaluator-Driven Optimization | $\mathcal{C}^P_\phi \rightarrow \mathcal{C}^P_\pi$ | Evaluator → Policy:偏好对齐（RM 信号 → policy weights via RLHF / DPO） | §6 |
| Parametric Externalization | $\mathcal{C}^P \rightarrow \mathcal{C}^T$ | Parametric → Tokenized:知识外化（weights → synthetic trajectories / demonstrations） | §6 |

**复合路径。** 当单篇论文将多条路径链式或闭环组合作为整体方法时(如 Narrative → Schematic → Parametric 的技能内化流水线,或 Policy → Tokenized → Policy 的自生成环路),其贡献在路径间的衔接机制,而非任一单路径。此类工作在 §7 Composite Pipelines 作为 first-class 对象讨论;单篇论文中偶现的两条独立转化,则分别在对应单路径 Section 引用。

**转化与利用的分工。** 转化刻画经验如何被生产为各种载体,是生产侧的问题;它与经验如何被消费的利用侧(检索策略、上下文编排、运行时维护、多载体协同)配对,才构成完整的经验管理图景。本文以转化为主轴,§8 专门分析利用需求(任务对延迟、可解释性、跨任务泛化的约束)如何反向驱动路径选择。