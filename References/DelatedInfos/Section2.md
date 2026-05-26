# 2. Preliminaries: Experience, Carriers, and Transformations

本节对三个基础概念给出形式化定义，构成全文的分析框架。

## 2.1 Agent

本文对 Agent 采用广义定义：其核心特征是在环境中依据任务上下文执行序贯决策（sequential decision-making）。在每一决策步 $t$，Agent 感知当前上下文 $c_t$，产生动作 $a_t$，环境可选地返回客观后果 $o_t$，并可选地接收评价信号 $f_t$。

Agent 的动作 $a_t$ 涵盖自然语言推理链、代码生成、工具调用、环境操控、多智能体通信等异构形态，不限于单一动作空间。Environment 可以是 reasoning verification、tool execution、physical world 等不同层次——关键特征是 Agent 在其中进行序贯决策。

Agent 在执行任务时遵循如下循环：

$$
c_t \xrightarrow{\pi} a_t \xrightarrow{\mathcal{E}} o_t \dashrightarrow f_t \dashrightarrow c_{t+1}
$$

其中 $\pi$ 为 Agent 的策略（policy），$\mathcal{E}$ 为环境。这一循环是经验的生产机制——每一轮 $(c_t, a_t, o_t, f_t)$ 构成一条原子经验记录。

## 2.2 Agent Experience

### 2.2.1 最小语义单元

Agent 经验的最小语义记录定义为模态无关的四元组：

$$e = (c, a, o, f)$$

其中 $c$（Context）和 $a$（Action）为必需元素，$o$（Observation）和 $f$（Feedback）为可选元素。该定义同时承载决策过程语义与异构动作空间两个纳入条件。

**轨迹（Trajectory）。** 一次完整的任务执行产生按时序排列的经验序列，记为 $\tau = (e_1, e_2, \dots, e_T)$，$T$ 为轨迹长度。多条轨迹的集合记为 $\mathcal{D} = \{\tau^{(i)}\}_{i=1}^N$。

### 2.2.2 Experience Carriers

最小语义单元 $e$ 描述经验的语义内容——"发生了什么"。Experience Carrier（经验载体）描述经验在模型架构中的存在形式，是分析经验转化路径的基础坐标。

<!-- Carrier 分类的设计考量：沿"经验在模型架构中的存在层次"切分，而非按传统维度（modality、technique、component）组织。存在层次直接映射到 Agent 系统关心的核心 trade-off（interpretability、inference cost、editability），与 modality 正交使多模态工作自然融入框架，且直接对应载体形式的根本差异，最大化 pathway 分类的判别力。 -->

Carrier 分为三个顶层类别，构成 Tokenized → Latent → Parametric 连续谱。沿此方向：可解释性与可编辑性递减，推理效率递增；存储位置从外部数据库/prompt → GPU memory → model checkpoint。

**Tokenized Carriers（Token 化载体，$\mathcal{C}^T$）。** 以离散 token 序列形式显式存在于模型前向传播输入端的经验载体。涵盖 text tokens、visual patch tokens、action tokens、serialized structural tokens 等，不限于自然语言文本。占用 context window，推理时需完整处理。按形式化程度分为两个子类：

- **Narrative Tokenized（叙事型，$\mathcal{C}^T_N$）**：以自然语言或感知顺序组织的弱形式化载体，通过 language / multimodal understanding 复用。典型形式：raw trajectories、reflections、summaries、screenshots、video sequences、natural-language rules 与 skill descriptions。
- **Schematic Tokenized（图式型，$\mathcal{C}^T_S$）**：以语法结构或拓扑结构组织的强形式化载体，通过 parsing、execution 或 graph traversal 复用。典型形式：executable code skills、workflows、DAGs、knowledge graphs、decision trees、structured memory graphs。

原始交互轨迹（raw trajectories）是 Narrative Tokenized 的零度抽象特例——未经提炼的 Narrative 载体，而非独立于载体体系之外的原始材料。

**Latent Carriers（隐空间载体，$\mathcal{C}^L$）。** 以连续向量或 hidden state 形式存在，直接参与模型 attention 或 hidden-state 计算的中间表示。不等同于离散 token（不占用 context window），也不固化在权重中（不改变模型参数），是介于 Tokenized 与 Parametric 之间的桥梁层。典型形式：KV cache、prefix cache、learnable soft prompts、continuous memory tokens、latent memory bank。可按实现形态区分 session-scoped（无需训练，如 KV cache）与 cross-session reusable（需训练，如 soft prompts），不作为正式分类子类。

**Parametric Carriers（参数化载体，$\mathcal{C}^P$）。** 经验固化在神经网络权重分布中，完全隐式。推理时不占用 context，直接前向传播输出；修改需再训练，可编辑性最低。按功能角色分为两个子类：

- **Policy Parameters（策略参数，$\mathcal{C}^P_\pi$，π-Par）**：生成动作 $a$ 的 actor 权重，涵盖 LLM agent、VLA、GUI agent 权重及 LoRA adapters。
- **Evaluator Parameters（评估器参数，$\mathcal{C}^P_\phi$，V-Par）**：评估 $(c,a,o,f)$ 的判断器权重，涵盖 reward models、PRM、verifiers、critics、VLM judges。

Evaluator 参数的划分与 Transformation 路径组织直接相关——它既可作为 Evaluator Internalization 的产物（Tokenized → Evaluator），也可作为 Evaluator-Driven Optimization 的起点（Evaluator → Policy via RLHF）。

### 2.2.3 正交属性

以下三个维度作为每个 carrier 实例的属性标签而非分类维度：

| 属性 | 取值 | 用途 |
|---|---|---|
| **Modality** | textual / visual / GUI / embodied / cross-modal | 在每条 pathway 中讨论不同模态下的实现差异 |
| **Abstraction level** | raw / refined | 区分原始终轨迹与精炼衍生物，主要在 Tokenized 层内体现 |
| **Experience Source** | {self} / {human} / {teacher} | 讨论经验来源对 pathway 选择的影响 |

### 2.2.4 边界澄清

**Embedding 的分层归属。** 按用途区分：Embedding 作为外部 memory 的检索索引（retrieve 后再进入 context）时，归入所索引 Tokenized 内容的附加机制；Embedding 作为可学习的 memory 表示（不解码回 token，直接参与模型 attention）时，归入 Latent。

**Raw experience 的定位。** Raw trajectories 是最低抽象程度的 Narrative Tokenized 载体，非独立于 carrier 体系之外。Transformation 通常以 raw 为起点，目标是提升抽象程度、改变形式化程度或改变存在层次。

## 2.3 Experience Transformation

经验转化（Experience Transformation）指经验在不同载体之间的迁移过程。一个映射

$$
\mathcal{T}: \mathcal{C}_{\text{src}} \rightarrow \mathcal{C}_{\text{tgt}}
$$

构成经验转化，当且仅当同时满足两个条件：

**条件 1——经验语义锚定（Experience Grounding）。** 源端内容可追溯至一条或多条经验记录 $e = (c, a, o, f)$ 或由其派生。

**条件 2——经验内容承载（Experience Embodiment）。** 目标载体编码了源经验的语义内容，而非仅发生无关语义的格式转换。

条件 1 排除那些虽操作同类型数据但不追溯至具体 agent 决策过程的通用处理（如通用语料预训练）；条件 2 排除纯格式转写（如把 JSON trajectory 转为 markdown）。两个条件共同保证分析对象聚焦于经验的实质性转化。

## 2.4 Seven Transformation Pathways

在上述定义框架下，本文识别出 7 条基础转化路径，沿载体源端聚合为 §3–§6 四个 Section：

| 路径 | 源载体 → 目标载体 | 定义 | Section |
|---|---|---|---|
| Narrative Abstraction | $\mathcal{C}^T_N \rightarrow \mathcal{C}^T_N$ | Narrative → Narrative：同层语义抽象（raw → reflections/rules/insights） | §3 |
| Schematic Formalization | $\mathcal{C}^T_N \rightarrow \mathcal{C}^T_S$ | Narrative → Schematic：同层形式化（logs → code/workflows/graphs） | §3 |
| Latent-Space Transformation | $\mathcal{C}^T \rightarrow \mathcal{C}^L$ | Tokenized → Latent：跨层压缩（trajectories → KV cache/soft prompts/memory tokens） | §4 |
| Evaluator Internalization | $\mathcal{C}^T \rightarrow \mathcal{C}^P_\phi$ | Tokenized → Evaluator：评估器内化（trajectories → RM/PRM/verifier） | §5 |
| Policy Internalization | $\mathcal{C}^T \rightarrow \mathcal{C}^P_\pi$ | Tokenized → Policy：策略内化（trajectories → policy weights via SFT/RL） | §5 |
| Evaluator-Driven Optimization | $\mathcal{C}^P_\phi \rightarrow \mathcal{C}^P_\pi$ | Evaluator → Policy：偏好对齐（RM 信号 → policy weights via RLHF/DPO） | §6 |
| Parametric Externalization | $\mathcal{C}^P \rightarrow \mathcal{C}^T$ | Parametric → Tokenized：知识外化（weights → synthetic trajectories/demonstrations） | §6 |

<!-- Latent-Space Transformation 的源端记为 $\mathcal{C}^T$ 而非 $\mathcal{C}^T_N$ 或 $\mathcal{C}^T_S$，因为 Cache-Based 方法的输入是任何 token 化经验经前向传播产生的 KV cache，理论来源不限于 Narrative——但现有文献主要操作于 Narrative Tokenized 输入，实际形成的是 Narrative-based Latent-Space Transformation。 -->

**复合路径的处理。** 当单篇论文将多路径链式或闭环式组合作为整体方法时（如 Narrative → Schematic → Policy，或 Policy → Tokenized → Policy 的自生成环路），其贡献点在于路径间的衔接机制（integration mechanism），而非任一单路径本身。此类工作在独立的 §7 Composite Pipelines 中作为 first-class 对象讨论。单篇论文中偶现的两条独立转化则分别在对应单路径 Section 中引用相关片段。
