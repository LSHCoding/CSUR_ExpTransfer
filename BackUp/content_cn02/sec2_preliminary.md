# §2 预备知识（Preliminaries）

在正式进入对 *agent experience transformation* 的讨论之前，本节对三个基础概念给出形式化定义：智能体、智能体的经验以及智能体经验的转化。

## §2.1 Agent


本文将智能体（Agent）定义为在环境中根据任务上下文执行序贯决策（sequential decision-making）的系统。在每一决策步 $t$，智能体感知当前上下文 $c_t$，产生动作 $a_t$，环境可选地返回客观后果 $o_t$，并可选地接收评价信号 $f_t$。

智能体的动作 $a_t$ 可以同时涵盖自然语言推理链、代码生成、工具调用、环境操控等不同形态。

Agent 在执行任务时遵循如下循环：

$$
c_t \xrightarrow{\pi} a_t \xrightarrow{\mathcal{E}} (o_t) \xrightarrow{} (f_t) \xrightarrow{} c_{t+1}.
$$

其中 $\pi$ 表示 agent 的策略（policy），$\mathcal{E}$ 表示环境，$(\cdot)$ 表示可选项。

这一循环是经验的生产机制——每一轮 $(c_t, a_t, o_t, f_t)$ 构成一条原子经验记录，将在 §2.2.1 形式化。

---

## §2.2 Agent Experience

### §2.2.1 Minimum Semantic Unit

智能体经验的最小语义记录定义为模态无关的四元组：

$$e = (c, a, o, f),$$

$c$ 和 $a$ 为必需元素，$o$ 和 $f$ 为可选元素。

**轨迹（Trajectory）。** 一次完整的任务执行产生按时序排列的经验序列，记为 $\tau = (e_1, e_2, \dots, e_T)$，其中 $T$ 为轨迹长度。多条轨迹的集合记为 $\mathcal{D} = \{\tau^{(i)}\}_{i=1}^N$。


### §2.2.2 Experience Carriers

最小语义单元 $e$ 描述的是经验的语义层——它说明"发生了什么"。经验载体（Experience Carrier）描述经验在模型架构中的存在形式，可按显式程度分为：**Tokenized、Latent 与 Parametric**。

**Tokenized Carriers（Token 化载体，记作 $\mathcal{C}^T$）。** 以离散 token 序列形式显式存在于模型前向传播输入端的经验载体。涵盖 text tokens、visual patch tokens、action tokens、serialized structural tokens（如序列化的 graph / workflow）等，不限于自然语言文本。Tokenized 载体按形式化程度进一步分为两个子类：
- **Narrative Tokenized（叙事型，记作 $\mathcal{C}^T_N$）**：以自然语言或感知顺序组织的弱形式化载体，通过语言理解或多模态理解实现复用。典型形式包括 raw trajectories、reflections、summaries、screenshots 等。

- **Schematic Tokenized（图式型，记作 $\mathcal{C}^T_S$）**：以语法结构或拓扑结构组织的强形式化载体，通过 parsing、execution 或 graph traversal 实现复用。典型形式包括 workflows、SOPs、knowledge graphs 等。

原始交互轨迹（raw trajectories）本身属于 Narrative Tokenized 载体的一个特例——它是零度抽象（未经任何提炼）的 Narrative 载体，而非独立于载体体系之外的原始材料。Transformation 通常以 raw 为起点。

**Latent Carriers（隐空间载体，记作 $\mathcal{C}^L$）。** 以连续向量或 hidden state 形式存在、直接参与模型 attention 或 hidden-state 计算的中间表示。Latent 载体不等同于离散 token（不以离散 token 形式占用 context 窗口），也不固化在模型权重中（不改变模型参数），是介于两者之间的桥梁层。典型形式包括 KV cache、prefix cache、learnable soft prompts、continuous memory tokens 等。

**Parametric Carriers（参数化载体，记作 $\mathcal{C}^P$）。** 经验固化在神经网络权重分布中，完全隐式。Parametric 载体按功能角色进一步分为两个子类：

- **Policy Parameters（策略参数，记作 $\mathcal{C}^P_\pi$）**：生成动作 $a$ 的 actor 权重。
- **Evaluator Parameters（评估器参数，记作 $\mathcal{C}^P_\phi$）**：评估 $(c,a,o,f)$ 的判断器权重。




## §2.3 Experience Transformation

经验转化（Experience Transformation）指经验在不同载体之间的迁移过程。一个映射

$$\mathcal{T}: \mathcal{C}_{\text{src}} \rightarrow \mathcal{C}_{\text{tgt}}$$

构成经验转化，当且仅当同时满足以下两个条件，其中 $\mathcal{C}_{\text{src}}, \mathcal{C}_{\text{tgt}} \in \{\mathcal{C}^T_N,\, \mathcal{C}^T_S,\, \mathcal{C}^L,\, \mathcal{C}^P_\pi,\, \mathcal{C}^P_\phi\}$：

**条件 1 — 经验锚定（Experience Grounding）。** 源端内容可追溯至一条或多条经验记录 $e = (c, a, o, f)$。
**条件 2 — 经验承载（Experience Embodiment）。** 目标载体编码了源经验的语义内容，而非仅发生形式上的格式转换。