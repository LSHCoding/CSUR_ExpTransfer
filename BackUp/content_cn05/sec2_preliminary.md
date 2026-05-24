# §2 预备知识（Preliminaries）

在进入对 Agent Experience Transformation 的讨论之前，本节对三个基础概念给出形式化定义：Agent、Agent Experience 以及 Experience Transformation。

## §2.1 Agent

本文将 Agent 定义为在环境中根据任务上下文执行序贯决策（sequential decision-making）的系统。在每一决策步 \(t\)，Agent 感知当前上下文 \(c_t\)，产生动作 \(a_t\)，环境可选地返回客观后果 \(o_t\)，并可选地接收评价信号 \(f_t\)。

Agent 的动作 \(a_t\) 涵盖自然语言推理链、代码生成、工具调用、环境操控等异构形态，不限于单一动作空间。

Agent 在执行任务时遵循如下循环：

$$
c_t \xrightarrow{\pi} a_t \xrightarrow{\mathcal{E}} (o_t) \xrightarrow{} (f_t) \xrightarrow{} c_{t+1},
$$

其中 \(\pi\) 为 Agent 的策略（policy），\(\mathcal{E}\) 为环境，\((\cdot)\) 表示可选项。这一循环是经验的生产机制——每一轮 \((c_t, a_t, o_t, f_t)\) 构成一条原子经验记录。

Environment 在此定义下可以是 reasoning verification、tool execution、physical world 等不同层次——关键特征是 Agent 在其中进行序贯决策，而非环境的物理属性。

## §2.2 Agent Experience

### §2.2.1 最小语义单元

Agent 经验的最小语义记录定义为模态无关的四元组：

$$e = (c, a, o, f),$$

其中 \(c\) 和 \(a\) 为必需元素，\(o\) 和 \(f\) 为可选元素。该定义同时承载决策过程语义与异构动作空间两个条件。

**轨迹（Trajectory）。** 一次完整的任务执行产生按时序排列的经验序列，记为 \(\tau = (e_1, e_2, \dots, e_T)\)，\(T\) 为轨迹长度。多条轨迹的集合记为 \(\mathcal{D} = \{\tau^{(i)}\}_{i=1}^N\)。

### §2.2.2 Experience Carriers

最小语义单元 \(e\) 描述经验的语义内容——它说明"发生了什么"。Experience Carrier（经验载体）描述经验在模型架构中的存在形式，是分析经验转化路径的基础坐标。

Carrier 分类沿"经验在模型架构中的存在层次"切分，而非按传统维度（modality、technique、component）组织。这一选择基于三点考虑：存在层次直接映射到 Agent 系统关心的核心 trade-off——interpretability、inference cost、editability，使分类本身携带分析维度；存在层次与 modality 正交，多模态工作自然融入框架而不必开辟特殊通道；存在层次直接对应载体形式的根本差异，最大化 pathway 分类的判别力。

Carrier 分为三个顶层类别：

**Tokenized Carriers（\(\mathcal{C}^T\)，Token 化载体）。** 以离散 token 序列形式显式存在于模型前向传播输入端的经验载体。涵盖 text tokens、visual patch tokens、action tokens、serialized structural tokens 等，不限于自然语言文本。占用 context window，推理时需完整处理。按形式化程度进一步分为两个子类：

- **Narrative Tokenized（\(\mathcal{C}^T_N\)）**：以自然语言或感知顺序组织的弱形式化载体，通过语言理解或多模态理解复用。典型形式：raw trajectories、reflections、summaries、screenshots、video sequences。
- **Schematic Tokenized（\(\mathcal{C}^T_S\)）**：以语法结构或拓扑结构组织的强形式化载体，通过 parsing、execution 或 graph traversal 复用。典型形式：code libraries、workflows、knowledge graphs、decision trees。

原始交互轨迹（raw trajectories）是 Narrative Tokenized 的零度抽象特例——未经任何提炼的 Narrative 载体，而非独立于载体体系之外的原始材料。Transformation 通常以 raw 为起点。

**Latent Carriers（\(\mathcal{C}^L\)，隐空间载体）。** 以连续向量或 hidden state 形式存在，直接参与模型 attention 或 hidden-state 计算的中间表示。不等同于离散 token（不占用 context window），也不固化在权重中（不改变模型参数），是介于 Tokenized 与 Parametric 之间的桥梁层。典型形式：KV cache、prefix cache、learnable soft prompts、continuous memory tokens。

Latent 载体可按实现形态区分 session-scoped（无需训练，如 KV cache）与 cross-session reusable（需训练，如 soft prompts）两种，但不作为正式分类子类。

**Parametric Carriers（\(\mathcal{C}^P\)，参数化载体）。** 经验固化在神经网络权重分布中，完全隐式。推理时不占用 context，直接前向传播输出；修改需再训练，可编辑性最低。按功能角色进一步分为两个子类：

- **Policy Parameters（\(\mathcal{C}^P_\pi\)，策略参数）**：生成动作 \(a\) 的 actor 权重，涵盖 LLM agent、VLA、GUI agent 权重及 LoRA adapters。
- **Evaluator Parameters（\(\mathcal{C}^P_\phi\)，评估器参数）**：评估 \((c,a,o,f)\) 的判断器权重，涵盖 reward models、PRM、verifiers、critics、VLM judges。

此划分与 Transformation 路径组织直接相关——Evaluator 参数既可作为 Transformation 的产物（Tokenized → Evaluator），也可作为产生新 Transformation 的中间状态（Evaluator → Policy via RLHF）。

三类载体构成连续谱：

> **Tokenized → Latent → Parametric**
>
> 沿此方向：interpretability ↓，inference efficiency ↑，editability ↓；存储位置从外部数据库/prompt → GPU memory → model checkpoint。

### §2.2.3 正交属性

以下三个维度作为每个 carrier 实例的属性标签而非分类维度，在 pathway 分析中作为编织维度使用：

| 属性 | 取值 | 使用场景 |
|---|---|---|
| **Modality** | textual / visual / auditory / GUI / embodied-sensor / cross-modal | 讨论各 pathway 在不同模态下的实现差异 |
| **Abstraction level** | raw / refined | 区分原始轨迹与其精炼衍生物，主要在 Tokenized 层内体现 |
| **Experience Source** | {self} / {human} / {teacher} | 讨论经验来源对 pathway 选择的影响 |

### §2.2.4 边界澄清

**Embedding 的分层归属。** 按用途区分：Embedding 作为外部 memory 的检索索引（retrieve 后再进入 context）时，归入所索引 Tokenized 内容的附加机制，不归入 Latent；Embedding 作为可学习的 memory 表示（不解码回 token，直接参与模型 attention）时，归入 Latent。

## §2.3 Experience Transformation

经验转化（Experience Transformation）指经验在不同载体之间的迁移过程。一个映射

$$\mathcal{T}: \mathcal{C}_{\text{src}} \rightarrow \mathcal{C}_{\text{tgt}}$$

构成经验转化，当且仅当同时满足以下两个条件，其中 \(\mathcal{C}_{\text{src}}, \mathcal{C}_{\text{tgt}} \in \{\mathcal{C}^T_N, \mathcal{C}^T_S, \mathcal{C}^L, \mathcal{C}^P_\pi, \mathcal{C}^P_\phi\}\)：

**条件 1 — 经验语义锚定（Experience Grounding）。** 源端内容可追溯至一条或多条经验记录 \(e = (c, a, o, f)\) 或由其派生。

**条件 2 — 经验内容承载（Experience Embodiment）。** 目标载体编码了源经验的语义内容，而非仅发生无关语义的格式转换。

条件 1 排除了那些虽操作同类型数据但不追溯至具体 agent 决策过程的通用处理（如通用语料上的预训练）；条件 2 排除了纯格式转写（如把 JSON trajectory 转为 markdown），以及不承载经验语义的存储或传输操作。两个条件共同保证本文的分析对象聚焦于经验的实质性转化，而非数据流水线中的任意步骤。

## §2.4 七条基础转化路径

在上述定义框架下，本文识别出 7 条基础转化路径，按源载体类型组织为后续四个 Section：

| 路径 | 定义 | Section |
|---|---|---|
| P1: \(\mathcal{C}^T_N \rightarrow \mathcal{C}^T_N\) | Narrative → Narrative：同层语义抽象（raw → reflections / rules / insights） | §3 |
| P2: \(\mathcal{C}^T_N \rightarrow \mathcal{C}^T_S\) | Narrative → Schematic：同层形式化（logs → code / workflows / graphs） | §3 |
| P3: \(\mathcal{C}^T \rightarrow \mathcal{C}^L\) | Tokenized → Latent：跨层压缩（trajectories → KV cache / soft prompts / memory tokens） | §4 |
| P4: \(\mathcal{C}^T \rightarrow \mathcal{C}^P_\phi\) | Tokenized → Evaluator：评估器内化（trajectories → RM / PRM / verifier） | §5 |
| P5: \(\mathcal{C}^T \rightarrow \mathcal{C}^P_\pi\) | Tokenized → Policy：策略内化（trajectories → policy weights via SFT / RL） | §5 |
| P6: \(\mathcal{C}^P_\phi \rightarrow \mathcal{C}^P_\pi\) | Evaluator → Policy：偏好对齐（RM 信号 → policy weights via RLHF / DPO） | §6 |
| P7: \(\mathcal{C}^P \rightarrow \mathcal{C}^T\) | Parametric → Tokenized：知识外化（weights → synthetic trajectories / demonstrations） | §6 |

**复合路径的处理。** 当单篇论文将多路径链式组合作为整体方法时（如 \(\mathcal{C}^T_N \rightarrow \mathcal{C}^T_S \rightarrow \mathcal{C}^P_\pi\) 或 \(\mathcal{C}^T \rightarrow \mathcal{C}^L \rightarrow \mathcal{C}^P_\pi\)），其贡献点在于路径间的衔接机制（integration mechanism），而非任一单路径本身，此类工作在独立的 §7 Composite Pipelines 中作为 first-class 对象讨论。单篇论文中偶现的两条独立转化则分别在对应单路径 Section 中引用。
