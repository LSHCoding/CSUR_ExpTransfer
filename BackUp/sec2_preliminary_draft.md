# §2 Preliminary: Taxonomy and Framework

---

在正式进入经验转化路径的分析之前，本节对三个基础概念给出形式化定义并固定全文符号：（1）智能体（Agent）——经验的生产者；（2）智能体经验（Agent Experience）——经验的语义结构及其在模型架构中的存在形式；（3）经验转化（Experience Transformation）——经验在不同载体之间的迁移过程。这三个定义为后续所有章节提供统一的概念语汇与判定标准。

---

## §2.1 智能体的定义

本文将智能体（Agent）定义为在任务上下文中执行序贯决策（sequential decision-making）的系统。这一定义有意从宽，涵盖单一 LLM agent、多 agent 系统、工具增强 agent、具身 agent 等变体，其共同本质是在每一步决策中面临"给定当前已知信息，选择下一步动作"的问题。

智能体的基本运作机制是 **experience loop**。在每一决策步 $t$，智能体感知当前上下文 $c_t$，产生动作 $a_t$，环境返回客观后果 $o_t$，并可选择地接收评价信号 $f_t$。这一循环是经验的生产机制——每一轮 $(c_t, a_t, o_t, f_t)$ 构成一条原子经验记录，多条记录按时序组织为轨迹（trajectory）$\tau = (e_1, e_2, \dots, e_T)$，其中 $e_t = (c_t, a_t, o_t, f_t)$。

本文关注的智能体具备一个关键性质：**异构动作空间**（heterogeneous action space）。智能体的动作 $a_t$ 可以同时涵盖自然语言推理链（CoT）、代码生成、工具调用（API / 函数调用）、规划分解（子目标展开）、环境操控（GUI 点击、具身 motor command）、多智能体通信等不同形态。这一性质将本文讨论的智能体与仅执行单步分类或标准序列生成的系统区分开来，是 Scope 纳入标准的构成要件。

Environment 的界定同样从宽。本文中 environment 不限于物理世界或模拟器，它可以是推理验证器（如 Lean、定理证明的 type checker）、工具执行沙箱（代码解释器、命令行环境）、多 agent 通信网络、或人类反馈通道。只要一个外部系统能够接收 $a_t$ 并返回与任务目标相关的 $o_t$，它就在本文框架下充当 environment。这一多层次 environment 概念使得框架能覆盖从纯推理 agent 到具身 agent 的完整谱系，而不必为不同环境类型单独建立定义体系。

---

## §2.2 智能体经验

### §2.2.1 经验的最小语义单元

一条原子经验定义为一个模态无关的四元组：

$$e = (c, a, o, f)$$

各元素的含义、必需性与多模态示例如表 1 所示。

| 元素 | 符号 | 必需性 | 含义 | 多模态示例 |
|:---|:---|:---|:---|:---|
| Context | $c$ | 必需 | Agent 决策前可获得的信息 | 文本指令、GUI 截图、摄像头图像、音频 |
| Action | $a$ | 必需 | Agent 当前步骤的输出 | CoT 推理链、工具调用、屏幕坐标点击、motor command |
| Observation | $o$ | 可选 | 环境返回的客观后果 | 执行报错信息、渲染后网页截图、传感器读数 |
| Feedback | $f$ | 可选 | 对 $(c,a,o)$ 或 $(c,a)$ 的评价信号 | Scalar reward、Textual critique、Visual diff |

$c$ 和 $a$ 为必需元素——只要智能体执行了一次决策，就必然存在决策上下文和决策输出。$o$ 和 $f$ 为可选元素：部分场景中智能体不接收环境的显式 observation（如纯推理链生成任务仅依赖模型内部验证），部分场景中没有显式 feedback（如零样本任务执行仅依赖最终结果判定）。

**轨迹（Trajectory）。** 一次完整的任务执行产生按时序排列的经验序列，记为 $\tau = (e_1, e_2, \dots, e_T)$，其中 $T$ 为轨迹长度。$\tau$ 是后续经验转化操作的基本输入单位——无论是将轨迹抽象为文本反思、压缩为隐空间表示、还是固化为参数更新，均以一条或多条 $\tau$ 为源端。

**模态无关性。** 四元组 $e = (c, a, o, f)$ 对模态不做预设。同一形式化框架可描述文本推理轨迹（$c$ 和 $a$ 均为自然语言）、GUI 操作轨迹（$c$ 含截图、$a$ 含点击坐标）、具身交互轨迹（$c$ 含多传感器数据、$a$ 含 joint angles）等异质经验。模态差异在本文框架中以属性标签而非独立类别出现，不影响经验的结构定义。

---

### §2.2.2 经验载体

经验载体（Experience Carrier）描述经验在模型架构中的存在形式。同一条经验 $e$ 可以寄存于不同载体——例如一段任务轨迹既可以以文本形式存储在 context 中，也可以压缩为 KV cache 的隐状态表示，还可以通过训练固化在模型权重中。不同载体在可解释性、推理开销、可编辑性等维度上呈现截然不同的 trade-off 画像，载体的选择直接决定了经验复用的方式与效率。

本文依据经验在模型架构中的**存在层次**对载体进行分类。这一维度直接映射到 Agent 系统关心的核心 trade-off：存在层次越深（从显式 token 到隐式权重），interpretability 与 editability 递减，inference efficiency 递增；存储位置从外部存储 / context window 迁移至 GPU memory，最终落入 model checkpoint。按此轴，经验载体分为三个顶层类别：**Tokenized、Latent 与 Parametric**。

---

**Tokenized Carriers（Token 化载体）。** 以离散 token 序列形式显式存在于模型前向传播输入端的经验载体。涵盖 text tokens、code tokens、visual patch tokens、action tokens、serialized structural tokens（如序列化的 graph / workflow / JSON schema）等，不限于自然语言文本。Tokenized 载体占用 context window，推理时需经完整的前向编码处理；其中自然语言与代码通常可直接读写编辑，而 patch / action / 结构化序列则未必具有人类可读性。

Tokenized 载体按形式化程度进一步分为两个子类：

- **Narrative Tokenized（叙事型，记作 $\mathcal{C}^T_N$）**：以自然语言或感知顺序组织的弱形式化载体，通过语言理解或多模态理解实现复用。典型形式包括 raw trajectories、reflections、summaries、rules、insights、hints、skill descriptions，以及 screenshot / video sequences、audio traces、interleaved visual-textual interaction logs 等多模态形态。

- **Schematic Tokenized（图式型，记作 $\mathcal{C}^T_S$）**：以语法结构或拓扑结构组织的强形式化载体，通过 parsing、execution 或 graph traversal 实现复用。典型形式包括 code libraries、workflows、SOPs、API specifications、composite actions（程序化），以及 knowledge graphs、sentence graphs、decision trees、execution graphs（图结构）。

Narrative 与 Schematic 的划分依据是形式化程度而非模态——两者均可承载任意模态的经验。

---

**Latent Carriers（隐空间载体，记作 $\mathcal{C}^L$）。** 以连续向量或 hidden state 形式存在、直接参与模型 attention 或 hidden-state 计算的中间表示。Latent 载体不等同于离散 token（不占用显式 context 位置），也不固化在模型权重中（不改变模型参数），是介于两者之间的桥梁层。省去前置的 token 编码开销，但对人类不可直接阅读。涵盖 KV cache、activation memory、prefix cache、learnable soft prompts、continuous memory tokens、trained memory composers 等形式。

---

**Parametric Carriers（参数化载体，记作 $\mathcal{C}^P$）。** 经验固化在神经网络权重分布中，完全隐式。推理时不占用 context window，直接通过前向传播输出；修改需重新训练，可编辑性最低。Parametric 载体按功能角色进一步分为两个子类：

- **Policy Parameters（策略参数，记作 $\mathcal{C}^P_\pi$）**：生成动作 $a$ 的 actor 权重。涵盖 LLM agent 权重、VLA（Vision-Language-Action）权重、GUI agent 权重、LoRA adapters 等。

- **Evaluator Parameters（评估器参数，记作 $\mathcal{C}^P_\phi$）**：评估 $(c,a,o,f)$ 的判断器权重。涵盖 reward models、process reward models (PRM)、verifiers、critics、VLM judges 等。

Policy 与 Evaluator 的划分与转化路径的组织直接相关：Evaluator 既可作为转化的终端产物（Tokenized → Evaluator），也可作为产生新转化的中间状态（Evaluator → Policy via RLHF / DPO）。

---

**三类载体的连续谱。** Tokenized、Latent、Parametric 并非三个孤立类别，而是沿存在层次构成的连续谱：

> **Tokenized → Latent → Parametric**
>
> 沿此方向：interpretability ↓，inference efficiency ↑，editability ↓
>
> 存储位置：外部存储 / context window → GPU memory → model checkpoint

在这一谱系中，Latent 占据独特的位置：它兼具 Tokenized 的"未固化"特性（不修改模型权重，可随 session 丢弃）和 Parametric 的"连续表示"特性（以向量形式参与计算），是两类载体之间进行渐进式转化的天然中介。

---

**形式化符号。** 记 $\mathcal{C}$ 为全体经验载体的集合。$\mathcal{C}^T$、$\mathcal{C}^L$、$\mathcal{C}^P$ 分别表示 Tokenized、Latent、Parametric 载体子集，满足 $\mathcal{C} = \mathcal{C}^T \cup \mathcal{C}^L \cup \mathcal{C}^P$ 且两两不交。Tokenized 子集进一步划分为 $\mathcal{C}^T = \mathcal{C}^T_N \cup \mathcal{C}^T_S$；Parametric 子集进一步划分为 $\mathcal{C}^P = \mathcal{C}^P_\pi \cup \mathcal{C}^P_\phi$。Latent 载体不做正式子类划分。

---

**边界说明。** 原始交互轨迹（raw trajectories）本身属于 Narrative Tokenized 载体的一个特例——它是零度抽象（未经任何提炼）的 Narrative 载体，而非独立于载体体系之外的原始材料。Transformation 通常以 raw 为起点，目标是提升抽象程度（Narrative raw → Narrative refined）、改变形式化程度（Narrative → Schematic）、或改变存在层次（Tokenized → Latent / Parametric）。将 raw 纳入 Tokenized 类别内部而非置于其外，保证了载体体系的封闭性——经验的任何存在形式都落在三类载体之一当中。

---

## §2.3 经验转化的定义

经验转化（Experience Transformation）指经验在不同载体之间的迁移过程。一个映射

$$\mathcal{T}: \mathcal{C}_{\text{src}} \rightarrow \mathcal{C}_{\text{tgt}}$$

构成经验转化，当且仅当同时满足以下两个条件：

**条件 1 — 经验锚定（Experience Grounding）。** 源端内容可追溯至一条或多条经验记录 $e = (c, a, o, f)$，或明确由 $e$ 派生。此条件排除以非经验数据（如静态预训练语料、人工编写的通用规则）为起点的操作——源端必须包含智能体在具体决策上下文中的交互证据。

**条件 2 — 经验承载（Experience Embodiment）。** 目标载体编码了源经验的语义内容，而非仅发生形式上的格式转换。此条件要求转化过程保留了源经验中与任务决策相关的信息——一条轨迹被压缩为 KV cache 后，cache 中确实蕴含了该轨迹的决策模式；轨迹被用于训练 reward model 后，模型权重确实捕捉了轨迹中的偏好信号。

两个条件共同划定了本文的讨论边界：条件 1 确保讨论的是"从经验出发"的转化，条件 2 确保讨论的是"到经验载体"的转化。源载体与目标载体可以属于同一顶层类别（如 Narrative Tokenized → Schematic Tokenized），也可以跨越类别边界（如 Tokenized → Latent、Tokenized → Parametric、Parametric → Tokenized、Parametric → Parametric）。转化的具体路径及其机制分析构成后续 §3–§7 的内容主体。
