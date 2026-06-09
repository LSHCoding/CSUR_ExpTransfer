# §8 Cross-Pathway Synthesis：完整分析框架

本文档是 §8 的设计蓝图。§8 的标题是 "Cross-Pathway Synthesis"，核心任务是 **synthesis 而非 comparison**——不是把差异列出来，而是找到产生差异的深层原则，使框架不仅能描述已有的 7 条路径和 5 类载体，还能推理任何尚未被发明的转化形式。

---

## 0. §8 的定位与三节逻辑关系

### 0.1 与 §2-§7 的分工

| Section | 分析对象 | 颗粒度 | 核心问题 |
|---------|---------|--------|----------|
| §2 | Carrier 定义 | Carrier-level | 经验以什么形式存在？ |
| §3–§6 | 7 条单路径文献综述 | Method-level | 社区做了什么、怎么做？ |
| §7 | 复合路径解剖 | Pipeline-level | 多路径如何衔接？ |
| **§8** | **跨路径合成** | **Pathway-level + Carrier-level** | **不同路径和载体之间如何选择？为什么？** |
| §9 | 开放问题 | — | 什么我们还不会？ |

§8 从 §3–§7 的 method-level 细节中抽身，站到 pathway-level 做结构性对比。它不引入新文献，而是用已有的文献证据来建立和验证分析框架。

### 0.2 §8 内部三节的逻辑关系

§8 的逻辑结构不是并列的三块，而是一个**两输入一输出的推理链**：

```
§8.1  Pathway Trade-off        §8.2  Carrier Utilization
  (生产代价画像)                  (消费代价画像)
       ↓                              ↓
       └──────────┬───────────────────┘
                  ↓
       §8.3  Utilization-Driven Pathway Selection
              (给定约束 → 选择路径/载体组合)
```

- §8.1 分析**生产侧**：从 trajectory 到目标 carrier，转化过程本身的代价与信息动态。
- §8.2 分析**消费侧**：每个 carrier 在推理时如何被使用，成本结构、控制自由度如何。
- §8.3 做**交叉匹配**：给定任务约束，结合生产画像和消费画像，推导载体与路径选择。

§8.3 不生产新数据。它的全部工作是把 §8.1 和 §8.2 的数据放在任务约束的透镜下交叉。如果 §8.3 开始引入新概念或新维度，说明 §8.1 或 §8.2 有遗漏，应该补回去。

---

## 1. 三条生成性原则（§8 开篇概念龙骨）

这是 §8 最重要的合成性产出。三条原则不是 carrier 属性的复读——它们是 **carrier 属性之所以如此的深层原因**。§8.1、§8.2、§8.3 的每一个分析都应在自己领域内展示这些原则如何体现。

### 原则一：存在层次原则（The Existence-Level Principle）

> Carrier 在 Tokenized → Latent → Parametric 谱系上的位置，同时决定了它的消费接口、每用成本、控制自由度与可追溯性。这些维度不是独立变化的——它们被存在层次**单调地锁定**。

推导：

- **Tokenized** 载体以离散符号存在于模型外部。→ 消费接口必然是 context injection。→ 每用成本包含检索延迟 + context processing。→ 但离散符号可被独立寻址、读写。→ 控制自由度高、可追溯性高。
- **Parametric** 载体以连续权重存在于模型内部。→ 消费接口必然是 forward pass computation。→ 每用成本为零边际（权重恒在，前向传播自动激活）。→ 但权重不可被独立寻址。→ 控制自由度近乎零、可追溯性近乎零。
- **Latent** 载体位于两者之间。→ 消费接口是 forward pass (attention integration)。→ 每用成本低但不是零。→ 连续向量不可直接阅读，但可被选择性加载（选择哪个 bank / 哪些 KV）。→ 控制自由度与可追溯性居中。

**分析后果**：沿 Tokenized → Latent → Parametric 谱系，没有任何 carrier 可以同时拥有"零边际推理成本"和"高可解释性"。这不是工程瓶颈——是存在层次的结构约束。任何声称"既快又透明"的方案必然在 carrier 分类上有模糊之处。

**对 §8 各节的影响**：
- §8.1：转化路径的跨层与否（跨存在层次 vs. 同层内）比目标 carrier 选择更根本地决定了生产成本。
- §8.2：消费画像表里的五个 column 不是五个独立变量，而是沿存在层次单调变化的关联变量。
- §8.3：利用驱动的选择在根子上是**存在层次的选择**——先决定经验应该放在谱系的哪个位置，再在位置内选具体 carrier 子类。

### 原则二：形式化原则（The Formalization Principle）

> 在 Tokenized 层内，Narrative → Schematic 的形式化程度差异决定了经验是**被理解消费**还是**被机制性消费**，进而决定了产物的可验证性模式。

推导：

- **Narrative** 通过 language / multimodal understanding 消费。→ 验证靠"读"（人类或强 LLM 判断语义正确性）。→ 可验证性高但主观——两个审阅者可能对同一 reflection 的质量判断不同。
- **Schematic** 通过 parsing / execution / traversal 消费。→ 验证靠"跑"（execution test 给出客观通过/失败信号）。→ 可验证性也高但是客观——通过就是通过，失败就是失败。

**关键洞察**：Narrative 验证和 Schematic 验证覆盖**不同类别的错误**：
- Narrative 验证覆盖"说的对不对"（语义正确性）——可能漏掉"说得好但做不到"的经验。
- Schematic 验证覆盖"跑不跑得通"（形式正确性 + 环境一致性）——可能漏掉"跑得通但方向错"的经验。

两者都是"高可验证性"，但不是同一种可验证性。这意味着 Tokenized 层内的子类选择不能仅靠"可验证性"的 yes/no，还需要区分"你需要验证什么类型的正确性"。

**分析后果**：
- §8.1：P1 和 P2 虽然都是 Tokenized → Tokenized，但 Output Verifiability 的类别不同，不是程度差异。
- §8.2：Narrative 和 Schematic 虽然共享 context injection 的消费接口，但消费过程中经验是否经过 execution 这一步导致了完全不同的错误暴露模式。
- §8.3：安全性约束需要进一步区分——execution safety（不能做错事 → 偏向 Schematic 的客观测试）vs. semantic safety（不能理解错 → 偏向 Narrative 的人类可审查）。

### 原则三：功能角色原则（The Functional-Role Principle）

> 在 Parametric 层内，Policy → Evaluator 的功能角色差异决定了载体在 pathway 图中的**拓扑位置**——Policy 是枢纽节点（可以进任何下游 pathway），Evaluator 是终端节点（只能进 P6）。

推导：

- **Policy** 产生 action。→ action 产生新的 trajectory（通过环境交互或 rollout）。→ trajectory 可以进 P1/P2/P4/P5/P7。→ Policy 通过 P7（外化）重新进入整个 pathway 图。
- **Evaluator** 产生评估信号（标量分数 / critique / preference）。→ 评估信号只能用于 scoring / ranking / reward。→ 如果不与 Policy 结合（P6），评估信号无处可去。→ Evaluator 是 pathway 图的汇节点。

**图论刻画**：在 7 条路径构成的有向图中：
- Tokenized 载体（Narrative / Schematic）是**源节点**——大量路径以它们为起点。
- Latent 载体是**中间节点**——有入边（P3）但出边目前文献中极少（latent → tokenized 的显式解码不是主流转化路径）。
- Policy 是**强连通分量成员**——可以通过 P7（外化）出、通过 P5（内化）回，形成闭环。
- Evaluator 是**汇节点**——只有入边 P4，只有出边 P6（通向 Policy）。

**分析后果**：
- §8.1：Composability 维度的差异不是经验性的而是结构性的——Evaluator "不可组合"不是因为社区没探索，而是因为评估信号的语义决定了它只有一个消费方（Policy）。
- §8.3：选择 Evaluator 作为目标载体意味着**接受终端化**——你不再能以这个 Evaluator 为起点继续转化（除了进 P6）。这限制了经验管理系统的未来灵活性。
- §7：复合路径之所以主要围绕 Policy 构建（Evaluator–Policy Co-Evolution、Refinement-Mediated Policy Internalization、Generative Experience Curation 三类中两类以 Policy 为枢纽），是因为 Policy 在图中的 hub 位置，不是研究偏好的偶然结果。

---

## 2. §8.1 Pathway Trade-off Comparison：生产侧分析框架

### 2.1 分析对象

一条 pathway $\mathcal{T}: \mathcal{C}_{\text{src}} \rightarrow \mathcal{C}_{\text{tgt}}$ 是一个转化操作——把源载体中的经验重新表示为目标载体。Pathway 比较的对象是**转化操作本身的结构特性**，而非目标载体的静态属性。

"Policy 可解释性低"是 Policy carrier 的属性，不是 Policy Internalization pathway 的专属特征——Evaluator Internalization 也产出低可解释性的 Parametric 载体。把 carrier 属性当 pathway 属性来比，等于把 §2.3 复读一遍。Pathway 独有的东西是转化过程的代价、信息损失、可验证性、增量能力。

### 2.2 分析维度

七个维度，按转化操作的三个截面组织。

#### 截面 A：输入侧——"喂什么进去"

**A1. Source Carrier（源载体类型）**
- 直接来自 pathway 定义。7 条路径源端分属 Tokenized (P1–P5) 和 Parametric (P6–P7)。
- 列此维度的目的不是"比较"（它是恒定的），而是为表建立行身份。

**A2. Data Prerequisite（数据前提）**
- **Volume**：需要多少源经验？单条 trajectory 够（reflection），还是需要跨轨迹归纳（multi-trajectory induction），还是需要大规模 batch（SFT/RL）？
- **Quality signal**：源经验带什么监督标签？无监督（只需 trajectory 本身）/ 弱监督（success/failure signal）/ 过程监督（step-level annotation）/ 偏好监督（pairwise preference）/ 强监督（human label）。
- **Source diversity**：只能用 self-generated trajectory，还是可以用 human demo / teacher model？

**A3. Input Robustness（输入鲁棒性）**
- 转化操作对噪声输入有多敏感？失败轨迹、含噪声的动作序列、不完整的 observation——这些还能用吗，还是会导致转化失败或产物质量骤降？

#### 截面 B：转化过程——"转化本身怎么发生、代价多大"

**B1. Transformation Semantics（转化语义）**

转化操作对经验做了什么性质的重新表示？七条路径的转化语义：

| 路径 | 转化语义 |
|------|----------|
| P1 Narrative Abstraction | **语义抽象**：从具体轨迹提炼规则/反思/insight，保留语义内容，提升抽象层级 |
| P2 Schematic Formalization | **结构形式化**：从自然语言轨迹抽取可执行/可遍历的结构，注入形式约束 |
| P3 Latent-Space Transformation | **连续压缩**：离散 token → 连续向量，保留计算状态，丢弃符号可读性 |
| P4 Evaluator Internalization | **评估能力内化**：交互经验 → 判断函数，学会"评价"而非"执行" |
| P5 Policy Internalization | **决策能力内化**：交互经验 → 生成函数，学会"执行"而非"评价" |
| P6 Evaluator-Driven Optimization | **偏好迁移**：评估能力 → 决策偏好，Evaluator 的判断转化为 Policy 的生成倾向 |
| P7 Parametric Externalization | **知识外化**：隐式权重 → 显式 token，不可读的能力重新变成可读的数据 |

**B2. Production Mechanism（生产机制）**

转化靠什么计算来执行？
- **LLM inference (prompting)**：P1、P2 主流——模型读 trajectory，输出 artifact。不需训练，每次转化付 inference cost。
- **Gradient-based training**：P3 (Prompt/Module-based)、P4、P5、P6——需要 GPU 训练。
- **Gradient-free optimization**：P3 (Cache-based) 直接存 KV；部分 P2 (parsing + template filling)——不需反向传播。
- **Execution + verification loop**：P2 (Programmatic Skill)——生成代码 → 执行 → 验证 → 入库。转化过程包含环境反馈闭环。

分析价值：决定需要什么基础设施。只需 API key vs. 需要 GPU 集群 vs. 需要执行环境。

**B3. Production Cost（生产成本）**

三个子维度：
- **Computational cost**：数量级差异。LLM inference 单次秒级 + 亚美元；SFT 一批若干 GPU-hour；RLHF/DPO 完整 pipeline 几十到几百 GPU-hour。
- **Human cost**：需要人类参与吗？P4 (RM training) 需 human preference label；P1/P2 可全自动。这是 continuum，不是 binary。
- **Cost amortization**：成本是一次性的还是每次新增经验都要重新支付？连接 B5 Incrementality。

**B4. Information Dynamics（信息动态）**

这是 §8.1 最核心的分析维度——carrier analysis (§2.3, §8.2) 完全覆盖不到。转化操作同时做三件事：

**(a) Information Preservation（信息保留）**

源经验中的什么语义内容在转化后仍可获取？
- P1：核心洞察与模式被保留，具体步骤和时序细节被抽象掉。
- P2：过程结构被保留，自然语言中的隐含假设和上下文 nuance 可能丢失。
- P3：模型的内部计算状态被保留（token 无法还原的 hidden representation），但符号内容不可直接读取。
- P5：决策模式被保留在权重中，单条经验的贡献不可区分。
- P6：评估偏好被保留，但评估器的原始校准信息在训练中丢失。
- P7：权重中的"能力"通过采样的方式部分恢复为 token，但采样有偏且不完整。

**(b) Information Loss（信息损失）**

关键区分 lossy-by-design vs. lossy-by-limitation：
- **Lossy-by-design**：P1/P2 的损失——抽象必然丢弃细节，形式化必然丢弃自然语言的 nuance。这是设计的意图，不是缺陷。
- **Lossy-by-limitation**：P5 的损失——SFT 欠拟合、RL reward hacking、分布漂移。损失的可能包含信号，不是单纯去噪。

**(c) Information Gain（信息增益）**

转化是否产生了源经验中不存在的新信息？
- P1：跨轨迹归纳可能产生单条轨迹中不存在的综合 insight。
- P2：形式结构（如 workflow DAG 中的依赖边）可能在原始 log 中只是隐式存在，formalism 是外显化。
- P3：连续表示可能捕获离散 token 未显式编码的统计规律。
- P6：Evaluator 信号可能引导 Policy 发现单靠 trajectory 无法学到的行为模式。
- P7：外化过程依赖采样，可能产生源权重中并不存在的 hallucination——增益也可以是负的。

**(d) Traceability（可追溯性）**

转化产物的元素能追溯到源经验的哪个部分？
- P1：高——reflection 引用的失败模式可对应到具体 trajectory 步骤。
- P2：中——workflow 步骤可大致对应但经过泛化。
- P3：低——连续向量无法逐元素解释。
- P4/P5：极低——权重更新是 batch 梯度累积的结果，不可追溯单条经验。
- P6：极低——Evaluator 信号的来源已在 P4 阶段丢失。
- P7：中——生成的 trajectory 是新的，不可追溯权重的具体成分，但至少是 tokenized 的可读形式。

**B5. Incrementality（增量性）**

新经验持续到来时，转化操作能否增量执行？
- **Incremental**：P1 (Static store)——新 trajectory → 新 reflection 写入，不影响已有条目。
- **Incremental with side effects**：P1 (Dynamic store)——新条目可能触发旧条目的 merge/prune，增量但有级联。
- **Batch reprocess**：P3 (Prompt/Module-based)、P5 (SFT)——增加新数据需重新训练，可热启动。
- **Online/iterative**：P5 (RL)、P6——在线更新，但分布漂移使旧经验的效果衰减。
- **Full retrain**：P4 (RM training with human labels)——新增人类标注通常需重新训练以保持校准。

**B6. Output Verifiability（产物可验证性）**

转化完成后，能否独立验证产物是否正确？注意这不是载体可解释性，而是"这次转化操作是否成功"的可独立判定性。

- **Direct inspection**：P1 的 reflection 可直接阅读判断——人类或强 LLM 都可做。但判断是主观的。
- **Execution test**：P2 的 code skill 可以跑——通过/失败是客观信号。但测试覆盖度有限。
- **Behavioral test**：P5 的策略只能通过 rollout 间接判断——新策略比旧策略好吗？好多少？不确定。
- **No direct verification**：P4 Evaluator 的质量只能通过它在 P6 中的下游效用间接评估；P3 Latent 只能通过 ablation 间接判断。
- **Circular verification risk**：P6 用 Evaluator 训练 Policy，再用 Policy 的行为评估 Evaluator——存在循环验证风险。

这一列直接连接 verifiability → correctability → maintainability 的结构规律：如果转化产物不可验证，就不可纠正，进而不可维护。

#### 截面 C：输出侧——"产出的东西能接着干什么"

**C1. Composability（可组合性）**

本 pathway 的产物能否直接作为另一个 pathway 的输入？分析价值在于揭示 pathway 图的拓扑结构。

基于功能角色原则：
- **P1 (Narrative)** → 可进 P2, P3, P4, P5。是 pathway 图的最多出边节点。
- **P2 (Schematic)** → 可进 P5（skill as action space）。不太直接进 P3/P4。
- **P3 (Latent)** → 文献中极少作为新 pathway 源端。实际上是一个弱终端。
- **P4 (Evaluator)** → 唯一出边 P6。是 pathway 图的汇节点。
- **P5 (Policy)** → 可进 P7。也可经 rollout 进 P1/P2/P4。是强连通分量成员。
- **P6 (Evaluator-Driven Optimization)** → 产出 Policy，同 P5 的 Composability。
- **P7 (Parametric Externalization)** → 可进 P1, P2, P4, P5。**是 pathway 图的闭环节点**——Policy → P7 → Tokenized → P5 → Policy 构成自生成环。

### 2.3 呈现结构

#### 分组逻辑

按转化语义的"跨度"将 7 条路径分为三组，每组内部有共享的 trade-off 模式：

**Group 1: Same-Level Refinement（P1, P2）**
- 共同特征：源和目标都在 Tokenized 层内。转化靠 LLM inference。保持可读性。可增量。
- 对比焦点：P1 做语义抽象（损失细节但保留语义灵活性），P2 做结构形式化（注入结构但牺牲自然语言 nuance）。两者的 Output Verifiability 都是"高"但不同质——P1 靠阅读验证（主观），P2 靠执行测试（客观）。形式化原则的直接体现。

**Group 2: Cross-Level Internalization（P3, P4, P5）**
- 共同特征：从 Tokenized 跨到 Latent/Parametric。转化靠训练。可解释性断崖式下降。增量性受限。
- 对比焦点：存在层次原则的直接体现——P3 压缩程度最轻（保留计算状态但只在 attention 层面），P4 专化评估能力但终端化（功能角色原则），P5 直接改变决策但不可追溯。三者代表了 Tokenized → 连续谱的三个不同目标点。

**Group 3: Parametric-to-X（P6, P7）**
- 共同特征：以 Parametric 为源端。都是"用已有的隐式经验做第二件事"。
- 对比焦点：P6 是"从评估到生成"的参数间迁移（Evaluator → Policy，进权重），P7 是"从权重到 token"的外化（Policy → Tokenized，出权重）。方向相反。Composability 角色互补——P6 是 Evaluator 的唯一出路，P7 是 Policy 回路的关键边。

#### 总表

三组 prose 分析之后，附一张精简总表。行 = 7 条路径，列 = 跨组差异最显著的维度：

| Pathway | Transformation Semantics | Production Mechanism | Info Loss | Traceability | Incrementality | Output Verifiability | Composability |
|---------|-------------------------|---------------------|------------|-------------|----------------|---------------------|---------------|
| P1 Narrative Abstraction | | | | | | | |
| P2 Schematic Formalization | | | | | | | |
| P3 Latent-Space | | | | | | | |
| P4 Evaluator Internalization | | | | | | | |
| P5 Policy Internalization | | | | | | | |
| P6 Evaluator-Driven Opt. | | | | | | | |
| P7 Parametric Externalization | | | | | | | |

表追求的不是穷尽（B1-B6 的 6 个过程维度全部入表太密），而是**最 discriminate 跨组差异的维度**。Information Dynamics 中最关键的 Info Loss 和 Traceability，加上 Production Mechanism、Incrementality、Output Verifiability、Composability。表格用简化的符号 + 关键词填，详细分析在 prose 中完成。

---

## 3. §8.2 Carrier Utilization Analysis：消费侧分析框架

### 3.1 分析对象

每种 carrier 在推理时如何被消费。载体结构属性决定了消费接口，消费接口决定了成本结构与控制自由度。§8.2 不讨论生产（那是 §8.1），只讨论"经验已经以这种载体存在了，用的时候要付什么代价，能调什么"。

### 3.2 分析维度

从 agent 决策规则 $a_t \sim \pi_\theta(\cdot \mid c_t)$ 出发。经验要影响决策，必须通过两个入口之一——$c_t$（外部、显式）或 $\theta$（内部、隐式）。载体在架构中的存在形式决定了它走哪个入口。五个维度对所有 5 类载体都有意义（无 N/A 列）。

**D1. Consumption Interface（消费接口）**

经验从架构的哪个位置进入决策循环？这是结构性约束，不是设计选择。

| 消费接口 | 进入点 | 对应载体 |
|----------|--------|----------|
| Context Injection | 写入 $c_t$，经前向传播影响 $a_t$ | Narrative、非可执行的 Schematic |
| External Execution | 在模型外执行，结果写入 $c_t$ 或直接产动作 | 可执行的 Schematic |
| Forward-Pass (Attention) | 连续向量参与 attention / hidden-state 计算 | Latent |
| Forward-Pass (Weights) | 固化在权重中，前向传播自动激活 | Policy |
| Signal Provision | 提供评估信号，用于 scoring / ranking / selection | Evaluator |

五种接口是穷尽的——决策规则只有 $c_t$ 和 $\theta$ 两个入口，经验要么走外部、要么走内部、要么走评估回路（信号不进 $c_t$ 也不进 $\theta$，作用在决策后的 selection/ranking 上）。

"选载体"同时锁定了"怎么用"——这是存在层次原则在消费侧的体现。

**D2. Activation Selectivity（激活选择性）**

能否在推理时有选择地激活特定经验？
- **Per-item**：可精确选择单条经验。Narrative：retrieve specific memory by similarity/key。
- **Per-skill / Per-node**：按功能单元选择。Schematic：invoke specific skill / traverse specific node。
- **Per-bank / Per-session**：按粗粒度块选择。Latent：load specific latent bank / session KV。
- **Indivisible / Always-on**：不可分割，始终激活。Policy：所有经验融合在权重中，无选择性。
- **Per-evaluator**：选择用哪个评估器，但评估器内部不可分割。Evaluator。

存在层次原则决定了选择性：从 Tokenized 到 Parametric，选择性单调递减。

**D3. Cost Structure（成本结构）**

**(a) Fixed Cost（固定成本）**：使经验可用的一次性投入。
- Narrative：存储 + 索引构建。
- Schematic：curation + testing（程序化 skill 需执行验证）。
- Latent (session-scoped)：零（无需训练，直接存 KV）。
- Latent (trained)：训练（soft prompt / memory module 训练）。
- Policy：fine-tuning / RL training。
- Evaluator：training（需标注或 success/failure signal）。

**(b) Per-Use Cost（单次使用成本）**：每次复用经验支付的代价。
- Narrative：context tokens + retrieval latency。每次复用都付。
- Schematic (executable)：execution compute + 可能的 API 调用延迟。
- Schematic (non-executable)：context tokens（同 Narrative）。
- Latent：attention integration（与 forward pass 融合，增额很小）。
- Policy：零边际（权重恒在，前向传播自动激活）。
- Evaluator：额外 forward pass（用于打分/评判）。

**(c) Where Work Happens**：计算发生在哪里？
- GPU context processing（Narrative、部分 Schematic）。
- External executor / API（可执行 Schematic）。
- GPU attention computation（Latent，融合在前向传播中）。
- GPU weights computation（Policy，融合在前向传播中）。
- GPU forward pass（Evaluator，独立的前向传播）。

**D4. Control Freedom（控制自由度）**

在推理时，系统设计者可以在不重新生产 carrier 的前提下调节什么？这是存在层次原则的直接体现——存在层次越高（越外部），控制自由度越大；存在层次越低（越内部），控制自由度越小。

- **Narrative**：High。检索策略（similarity / keyword / hybrid）、top-k、排序、截断、prompt 模板、注入位置——几乎每个环节都可调。
- **Schematic**：Medium-High。选哪个 skill（selection strategy）、invoke 时机、执行后结果如何整合进 context。Skill 内部不可调（code 是固定的）。
- **Latent**：Low-Medium。检索机制（相似度阈值、top-k）、融合权重（gate / residual weight）。Latent 内容不可调（向量是固定的）。
- **Policy**：Near-zero。权重一旦训练完，推理时无法选择"用哪部分经验、不用哪部分"。唯一的控制是 system prompt / few-shot example（但那走的是 Narrative carrier，不是 Policy）。
- **Evaluator**：Low。选哪个 evaluator（如果有多个）、何时调用（每步 / 最终 / 仅在低置信度时）。Evaluator 内部的判断标准不可调。

**D5. Maintenance Mechanism（维护机制）**

新经验持续到来时，载体如何演化？点到机制类型即可，深入分析归到 verifiability → correctability → maintainability 结构规律。

- **Narrative** (Static store)：Append-only。新条目写入，旧的不变。需人工清理过时条目。
- **Narrative** (Dynamic store)：Append/Edit/Delete + Merge/Prune。条目可被改写、合并且淘汰。
- **Schematic**：Version/Replace。新版本经过 test 后替换旧版本。支持 rollback。
- **Latent** (session-scoped)：Auto-expire。旧 session 自然失效，不需显式维护。
- **Latent** (trained)：Retrain。需用新数据重新训练或 fine-tune。
- **Policy**：Fine-tune / Retrain。无法逐条修正——任何修改都需要重新训练。
- **Evaluator**：Replace evaluator / Retrain。替换整个评估器或重新训练。

### 3.3 呈现结构

#### §8.2.1 Carrier × Utilization Table

行 = 5 类载体（Narrative / Schematic / Latent / Policy / Evaluator），列 = 5 个消费维度。

Policy 和 Evaluator 必须分两行——它们的消费接口、选择性、控制自由度完全不同，合一行就抹掉了 §6.1 里 Evaluator 作为 signal source 的枢纽地位。

表用简化符号 + 关键词填。与 §2.3 Carrier 属性表的区别：§2.3 表是"这个载体是什么"（存在形式、子类），§8.2 表是"用这个载体要付什么代价、能调什么"（消费接口、成本、控制）。角度不同，不重复。

#### §8.2.2 从维度到原则

表后的 prose 不做逐 carrier 枚举（表已经做了）。而是展示五个列的读数不是五个独立事实——它们是存在层次原则、形式化原则、功能角色原则在消费侧的体现。沿 Tokenized → Parametric：消费接口从外部注入变为内部计算，每用成本从按次支付变为零边际，控制自由度从高变为近乎零。这使 §8.2 从"一张有用的表"升级为"原则的消费侧实例化"。

#### §8.2.3 Multi-Carrier Synergy（多载体协同）

多载体协同不是单个 carrier 的属性，不入表，在 prose 中独立讨论。
- 典型协同模式：Narrative + Policy（可解释 + 高效）、Evaluator + Policy（评估 + 执行）、Latent + Narrative（快速上下文 + 可读备份）。
- §2.4 命名的"多载体协同"在此兑现——不写成 per-carrier 列，而是 cross-carrier 关系。
- 与 §8.3 的三种组合模式（并行互补 / 分层分级 / 时序分阶段）呼应但不重复——§8.2.3 停留在"carrier 间如何配合"的机制描述，§8.3 进一步到"在什么约束下应该选哪种组合模式"。

---

## 4. §8.3 Utilization-Driven Pathway Selection：选择侧分析框架

### 4.1 设计原则

§8.3 不生产新数据。它的全部工作是把 §8.1（生产画像）和 §8.2（消费画像）的数据放在任务约束的透镜下交叉，产出选择逻辑。

不要做决策树。不要列"每个场景的推荐路径"清单。框架的作用是揭示分析的维度与张力，不是给读者自动化的选择算法。承认竞争约束无解的情况是分析产出而非分析缺陷。

### 4.2 Phase 1: Constraint Elicitation（约束引出）

任务场景对 agent 系统施加的约束，按来源分为四个不可互相归约的类别：

**Class 1: Inference Resource Constraints（推理时资源约束）**
来自部署环境，不来自任务语义。

| 子维度 | 含义 |
|--------|------|
| Latency budget | 单步决策允许的最大延迟。实时对话 vs. 离线批处理，差三个数量级。 |
| Context budget | 上下文窗口的可用空间。长程任务 vs. 短问答，可用 context 量悬殊。 |
| Compute budget | 每步可用的 GPU/CPU。手机端 vs. 云端。 |
| Per-call cost ceiling | 每次推理允许的最大金钱成本。百万级 API 调用 vs. 单次研究实验。 |

**Class 2: Experience Scale Constraints（经验规模约束）**
来自经验的积累速度和总量。

| 子维度 | 含义 |
|--------|------|
| Stock | 已有多少历史经验？ |
| Velocity | 新经验以多快速度到达？ |
| Diversity | 经验跨多少任务/领域？ |
| Retention horizon | 经验需要保留多久？ |

**Class 3: Quality & Governance Constraints（质量与治理约束）**
来自组织/监管/安全需求，不来自技术限制。

| 子维度 | 含义 |
|--------|------|
| Interpretability | 人类是否需要审查经验的使用过程？ |
| Correctability | 错误经验需要多快能被修正？ |
| Safety criticality | 错误决策的后果是否不可逆？ |
| Audit trail | 是否需要事后追溯决策依据？ |

**Class 4: Environment Dynamics Constraints（环境动态约束）**
来自外部世界的变化速度。

| 子维度 | 含义 |
|--------|------|
| Task distribution drift | 任务本身是否随时间变化？ |
| Interface stability | 工具/API 是否稳定？ |
| Experience staleness rate | 旧经验多快失效？ |

### 4.3 Phase 2: Hard Constraint Pruning（硬约束剪枝）

#### 原理

某些约束是 hard constraint——不满足就直接排除载体，不与其他约束"加权平均"。典型来源：
- Safety criticality = extreme → Policy 和 Latent 直接出局。
- Interpretability = mandatory → Policy 和 Latent 直接出局。
- Latency budget < 50ms（硬实时）→ Narrative 和 Schematic-execution 直接出局。

硬约束的作用是**缩小搜索空间**——先排除，再在幸存者中优化。

#### 存在层次原则的直接应用

Phase 2 本质上是在 Tokenized → Latent → Parametric 谱系上画不可逾越的线。例如，"强制可解释"这条硬约束意味着经验必须留在 Tokenized 层——任何跨层转化（P3/P4/P5）都不允许。这不是在选 carrier，而是在选存在层次。

### 4.4 Phase 3: Multi-Constraint Resolution（多约束解析）

#### 4.4.1 约束压力映射

每个约束维度对每类载体施加方向性压力（toward / neutral / against）。这是 §8.3 的数据核心。

| 约束维度 | Narrative | Schematic | Latent | Policy | Evaluator |
|----------|-----------|-----------|--------|--------|-----------|
| Low Latency | against (retrieval + context overhead) | against (execution latency or context) | toward (attention integration, fused in forward pass) | **strong toward** (zero marginal) | weak against (extra forward pass) |
| Large Experience Volume | against (retrieval degrades, context limit) | weak toward (per-skill selection, no shared context budget) | neutral-weak-against (memory capacity) | **strong toward** (O(1) inference, training cost amortized) | toward (O(1) inference, training cost amortized) |
| High Interpretability | **strong toward** (human-readable, inspectable) | toward (structure inspectable, needs technical skill) | against (opaque vectors) | **strong against** (opaque weights) | weak against (output visible, but reasoning opaque) |
| Fast Correctability | **strong toward** (per-item edit/delete) | toward (per-skill versioning, needs retest) | against (retrain whole bank) | **strong against** (retrain only, catastrophic forgetting risk) | **strong against** (retrain only) |
| High Environment Volatility | toward (fast append, auto-prune in dynamic stores) | against (interface-dependent, skill breaks on API change) | weak toward (session-scoped auto-expires) / against (trained needs retrain) | **strong against** (retrain cost, stale during training) | **strong against** (retrain cost) |
| Extreme Safety Criticality | **strong toward** (pre-use reading gate) | **strong toward** (pre-use testing gate) | against (no pre-use verification) | **strong against** (no pre-use verification) | weak toward (calibration check possible, not exhaustive) |

此表反映的是存在层次原则——pressure direction 沿 Tokenized → Parametric 单调变化。

#### 4.4.2 联盟约束（Aligned Constraints）

多个约束指向同一方向时，形成联盟，推荐信号增强。联盟不是简单的"同方向相加"——意味着即使某个约束在未来放松，推荐依然稳健。

示例：
- 高延迟敏感 + 大经验体量 + 低可解释需求 → 三重 toward Policy。即使体量后来变小了，Policy 依然不差。
- 强可解释 + 快速可修正 + 高环境变动 → 三重 toward Narrative。即使环境后来稳定了，Narrative 依然可用。

联盟约束的分析价值：识别 **overdetermined 推荐**——这些推荐的稳健性最高，是最安全的工程选择。

#### 4.4.3 竞争约束（Competing Constraints）→ 不可化约张力

当两个强约束指向相反方向时，单一载体无法同时满足。这是框架最有分析增量的部分。

**不可化约张力对**：

| 张力对 | 冲突本质 | 为什么不可化约 |
|--------|---------|---------------|
| 低延迟 × 强可解释 | Policy 快但不透明，Narrative 透明但慢 | 存在层次原则的推论——没有载体同时占据谱系两端。结构性约束，不是工程瓶颈。 |
| 大体量 × 强可解释 | Policy 可 scale (O(1)) 但不可读，Narrative 可读但检索在大体量下退化 | 检索精度随体量衰减是信息论约束，context budget 是硬件约束。无法通过增加检索预算彻底解决。 |
| 高环境变动 × 低延迟 | Narrative 适应快（即时写入）但每次付 token 延迟，Policy 推理快但更新慢（需 retrain） | 环境变动要求频繁更新（turn to Narrative），低延迟要求零边际成本（turn to Policy）。矛盾。 |
| 快速可修正 × 大体量 | Narrative 可逐条修正但不 scale（百万条经验逐条修正人力不可承受），Policy 可 scale 但修正需 retrain（太慢） | 可修正性在微观（per-item）和宏观（per-retrain）两个时间尺度上不兼容。 |

这些张力不是框架的失败——它们是框架最重要的产出。它们解释了：
- 为什么 §7 的 composite pipelines 存在（它们正是设计来部分缓解这些张力的）。
- 为什么没有普适最优载体（张力是结构性的，不是暂时的工程困难）。
- §9 的 open problems 该写什么（如何动态调节载体组合以响应张力变化）。

### 4.5 Phase 4: Carrier Composition（载体组合逻辑）

竞争约束的存在使载体组合不是可选项而是必须项。三种组合模式：

**模式 A：并行互补（Parallel Complement）**

两个载体同时服务于同一决策，各自覆盖对方无法满足的约束。
- 典型实例：**Narrative + Policy**。Policy 承担实时决策（满足低延迟），Narrative 承担 audit trail（满足可解释）。Policy 出错时，Narrative 中的反思提供纠错依据。
- 文献对应：§7.2 Refinement-Mediated Policy Internalization——先用 Narrative 准备高质量监督，再转入 Policy 获得推理效率。
- 脆弱点：两套系统维护成本叠加。Narrative 与 Policy 中的经验可能不一致（Policy 更新后 Narrative 中的旧反思可能指向已修正的行为）。

**模式 B：分层分级（Tiered Routing）**

按决策的重要性或难度分流到不同载体。
- 典型实例：**Policy (routine) + Evaluator (gate) + Narrative (exception)**。Policy 处理常规决策，Evaluator 检测异常/低置信度，触发 Narrative-based 人工或 LLM 复核。
- 文献对应：PRM/verifier 作为 safety gate 的模式散布在 §5.1 和 §6.1 中。
- 脆弱点：Evaluator 的判断本身可能出错。gate 的 false negative 导致本该复核的决策被 Policy 直接执行。

**模式 C：时序分阶段（Temporal Staging）**

经验在时间维度上经历载体迁移：先以低成本载体快速可用，再逐步结晶为高效率载体。
- 典型实例：**Narrative (recent) → Policy (stable)**。新经验先写成 reflection 立即可用（低生产延迟），积累到一定量后经 P5 固化进 Policy（降低消费成本），旧 reflection 可选保留为 audit trail 或淘汰。
- 文献对应：§7.3 Generative Experience Curation 的经验构造与筛选，以及自生成闭环。
- 脆弱点：切换时机（什么时候从 Narrative 迁到 Policy）涉及 optimization——过早迁移 Policy 质量不足，过晚迁移累积了不必要的消费成本。

三种模式不是互斥的——一个完整的 agent 系统可以同时使用三种模式。

### 4.6 Phase 5: Production Path Selection（生产路径选择）

载体组合确定后，对每个目标载体，匹配可用的生产 pathway。这里接入 §8.1 的数据。

**Pathway-Carrier 耦合表**（放在 §8.1 结尾或 §8.2 开头，作为 Phase 5 的数据基础）：

| 目标 Carrier | 可用 Pathway | Production Mechanism | Production Cost | Incrementality | 备注 |
|-------------|-------------|---------------------|-----------------|----------------|------|
| Narrative | P1 (Narrative Abstraction) | LLM inference | Low: API call per abstraction | Incremental (append new entries) | 唯一主流路径。成本低，可增量，产物可读验证。 |
| Narrative | P7 (Parametric Externalization) | Sampling from trained policy | High: requires prior trained policy | Batch (policy retrain → re-sample) | 从权重外化经验。代价比 P1 高一个数量级。用途不是常规经验生产，而是审计/调试。 |
| Schematic | P2 (Schematic Formalization) | LLM inference + execution verification | Medium: API call + execution test loop | Incremental (append new skills) | 唯一路径。执行验证增加了生产成本但提供了 P1 没有的客观可验证性。 |
| Latent (session) | P3 (Cache-Based) | Forward pass + KV store | Very Low: no training | Per-session (auto-expire) | 无训练成本但仅 session-scoped。不是长期经验的载体。 |
| Latent (cross-session) | P3 (Prompt/Module-Based) | Gradient-based training | Medium-High | Batch reprocess | 需要训练。跨 session 可复用。 |
| Policy | P5 (Policy Internalization, SFT/RL) | Gradient-based training | High | Batch reprocess | 直接内化 trajectory。需要大规模高质量数据。 |
| Policy | P6 (Evaluator-Driven Optimization) | Gradient-based training (RL/DPO) | Very High (P4 + P6 叠加) | Online/iterative | 需要先有 Evaluator（叠加 P4 的成本）。可学到 trajectory-only 无法提供的细粒度偏好。 |
| Evaluator | P4 (Evaluator Internalization) | Gradient-based training | High (needs labels or clear success signal) | Batch reprocess or full retrain | 唯一路径。需要标注数据或明确的 success/failure signal。 |

**关键发现：Policy 是唯一有两条差异化生产路径的 carrier。** P5（从 trajectory 直接训练）和 P6（从 Evaluator 信号训练）的代价画像完全不同。Phase 5 不只是 feasibility check——当目标载体是 Policy 时，需要在 P5 和 P6 之间做生产路径选择：
- P5 适合：有大规模高质量 trajectory，不需要细粒度偏好信号。
- P6 适合：有已训练好的 Evaluator，需要比 trajectory-level success/failure 更细的决策引导。
- P5 + P6 组合：先用 P5 获得 baseline Policy，再用 P6 做偏好对齐——这是 RLHF 的经典两阶段，对应 §7.1 Evaluator–Policy Co-Evolution。

### 4.7 §8.3.4 Temporal Evolution（时序演化）

这是对"当前框架缺少时间维度"的补全。经验管理是持续进行的，optimal carrier configuration 是时间的函数。

#### 4.7.1 约束的时序导数

| 约束 | 随时间的变化方向 | 对 carrier 选择的压力变化 |
|------|-----------------|------------------------|
| Experience Volume | **单调递增**（经验只增不减） | 压力从 Narrative toward Policy |
| Experience Diversity | **通常递增**（agent 被用到更多任务） | 增加 Policy 的泛化优势，增加 Narrative 的检索难度 |
| Task Distribution | **可能漂移**（域变化） | Pressure toward adaptable carriers (Narrative) |
| Environment Interface | **离散变化**（API 更新、工具升级） | 每次变化对 Schematic 造成冲击 |
| Training Cost | **单调递减**（硬件进步、算法改进） | Policy/Latent/Evaluator 的固定成本随时间降低 |
| Latency Requirement | **大致恒定**（物理极限 + 用户期望） | 不随时间变化的硬锚点 |

#### 4.7.2 迁移触发条件

最关键的一条迁移路径：**Narrative → Policy**。触发条件：
1. 经验体量超过检索精度阈值（top-k 检索中相关条目占比持续下降）。
2. 经验分布趋于稳定（新增经验不再显著改变经验的内容分布）。
3. 训练成本可被 Policy 的消费侧节省摊销（系统预期寿命足够长）。

其他迁移路径（Narrative → Latent, Narrative → Schematic 等）遵循类似的触发逻辑。

#### 4.7.3 迁移代价

迁移不是免费的——一次 P5 的固定训练成本需要在 Policy 消费侧的节省中被收回。如果过早迁移（经验量不足、分布未稳定），policy 质量低，需要回退或重新训练。迁移决策本质上是 irreversible investment under uncertainty——这是 §9 的 open problem 素材（"什么时候应该把经验固化进权重？"缺乏理论指导）。

### 4.8 §8.3.5 Mismatch Analysis（失配分析）

框架应该能够预测：如果选错了载体，会发生什么，有哪些症状，哪些是可恢复的，哪些是不可逆的。

| 失配类型 | 症状 | 可恢复性 | 恢复路径 |
|----------|------|----------|----------|
| 可解释需求 × Policy | 无法审计决策、错误归因失败、修正单个错误引发灾难性遗忘 | **低**（权重中的经验不可单独提取） | P7 外化 → 审查 → 筛选 → 重新 P5。代价极高。本质上是不可逆的——外化重建的不是原来的经验。 |
| 低延迟需求 × Narrative | 检索延迟叠加、context prefill 超时、端到端延迟超标 | **高** | 渐进迁移：先精简 store（去冗）→ 如仍超标，做 P5 迁移至 Policy。 |
| 大体量 × Narrative | 检索精度下降、检索延迟上升、context 塞不下全部相关经验、幻觉引用（LLM 引用不存在的"记忆"） | **中** | 做 P1 Dynamic（merge/prune 去冗）→ 如仍超标，做 P5 迁移。迁移需重新训练，有过渡期。 |
| 高环境变动 × Policy | 策略过时、在新工具/API 上行为退化、无法快速适应 | **低** | 需重新训练 Policy，训练期间系统持续退化。短期缓解：临时注入 Narrative（规则/反思）覆盖过时行为，但增加延迟。 |
| 高环境变动 × Schematic | Skill 因 API 变更而不可执行、execution 报错率上升 | **中** | 重新生成 + 测试受影响的 skill。局部修正（受影响 skill 数量有限）。比 Policy 的全局重训练便宜。 |
| 安全关键 × Latent | 无法验证 latent 中的经验质量、latent 注入后产生不可预测的行为变化 | **低** | Latent 无法审计。只能放弃当前 latent bank，重建为 Tokenized 形式（Narrative 或 Schematic）以确保可验证性。 |
| 大体量 × Evaluator | Evaluator 校准随经验分布漂移而退化（训练时的经验分布与当前分布不一致） | **中** | 重新校准或重新训练 Evaluator。需新的标注数据。 |

失配分析不是给读者一个"不要犯错"的清单。它的分析功能是：
- **验证框架**：预测的症状与文献中观察到的 failure mode 一致 → 框架有解释力。
- **连接 §9**：每种"低可恢复性"失配都是一个 open problem——"如何在需要 X 的场景中安全地使用 Y 载体？"

---

## 5. §8 完整结构

```
§8 Cross-Pathway Synthesis

  开篇（~1 page）：三条生成性原则
  - 存在层次原则（Existence-Level Principle）
  - 形式化原则（Formalization Principle）
  - 功能角色原则（Functional-Role Principle）
  - 说明三条原则如何贯穿 §8.1–§8.3，使分析从"比较差异"升级为"推导差异"
  ↓

§8.1 Pathway Trade-off Comparison (~5–8 pages)
  开篇：明确 pathway 比较的颗粒度——不是 method-level（§3–§6），不是 carrier-level（§2），是 pathway-level（转化操作的结构特性）
  
  §8.1.1 Same-Level Refinement（P1, P2）
    - P1 Narrative Abstraction 的转化画像
    - P2 Schematic Formalization 的转化画像
    - 对比焦点：语义抽象 vs. 结构形式化；验证的主观 vs. 客观；形式化原则的体现
  §8.1.2 Cross-Level Internalization（P3, P4, P5）
    - P3 Latent-Space Transformation 的转化画像
    - P4 Evaluator Internalization 的转化画像
    - P5 Policy Internalization 的转化画像
    - 对比焦点：存在层次原则的体现——压缩程度与信息损失的 trade-off；功能角色原则的体现——P4 的终端化
  §8.1.3 Parametric-to-X（P6, P7）
    - P6 Evaluator-Driven Optimization 的转化画像
    - P7 Parametric Externalization 的转化画像
    - 对比焦点：方向相反（进 vs. 出权重）；Composability 角色的互补
  §8.1.4 Production Pathway Summary
    - 精简总表（7 paths × 关键维度）
    - Pathway-Carrier 耦合表（5 carriers × 可用 pathway + 代价差异）
  ↓

§8.2 Carrier Utilization Analysis (~4–6 pages)
  开篇：从 §8.1 的生产侧转到消费侧。用决策规则 $a_t \sim \pi_\theta(\cdot \mid c_t)$ 说明消费接口的分类基础。
  
  §8.2.1 Carrier × Utilization Table
    - 5 carriers × 5 消费维度
    - Policy 与 Evaluator 分两行
  §8.2.2 From Dimensions to Principles
    - 展示五个列的读数如何从三条生成性原则（尤其是存在层次原则）中推出
  §8.2.3 Multi-Carrier Synergy
    - 协同模式（并行互补 / 分层分流 / 时序接力）
    - 与 §2.4 "多载体协同"的回连
  ↓

§8.3 Utilization-Driven Pathway Selection (~6–8 pages)
  开篇：§8.3 不引入新数据，它用 §8.1 和 §8.2 的数据做交叉匹配。选择逻辑分五阶段。
  
  §8.3.1 Constraint Dimensions & Carrier Pressure
    - 四类约束 → 载体压力总表
    - 标注哪些约束是 hard（可成为 dictator）
  §8.3.2 Constraint Interaction: Aligned, Dictator, and Competing
    - 联盟约束 → overdetermined 推荐
    - 独裁约束 → hard pruning
    - 竞争约束 → 不可化约张力对 → 为什么 composite 存在
  §8.3.3 Carrier Composition Patterns
    - 并行互补 / 分层分级 / 时序分阶段
    - 每种模式的适用条件、文献对应、脆弱点
  §8.3.4 Temporal Evolution: Constraint Drift and Carrier Migration
    - 约束的时序导数
    - 迁移触发条件（重点是 Narrative → Policy）
    - 迁移代价与时机问题 → 连接 §9
  §8.3.5 Mismatch Analysis: Symptoms, Recoverability, and Recovery Paths
    - 失配类型 → 症状 → 可恢复性 → 恢复路径
    - 框架自我验证 → 连接 §9
```

---

## 6. 写作纪律

1. **每段都在"比"或"推"，不在"列"。** §8 不是 §3–§7 的 mini-summary。如果某段开头是"P1 包括 Reflexion、ExpeL、AutoGuide 等工作"——删掉重写。正确开头是"P1 与 P5 的生产成本差异跨越三个数量级——LLM inference 按 API call 计费，SFT 按 GPU-hour 计费——这意味着……"

2. **三条原则反复出现但不反复定义。** 开篇定义一次，后续 §8.1–§8.3 中只用一句话回指（"这是存在层次原则在消费侧的体现"），不再展开推导。原则是龙骨，不是反复敲的钉子。

3. **表与 prose 的分工。** 表给结构（一目了然的对比坐标），prose 给推理（为什么是这个值、这个值意味着什么）。Prose 不应复述表的内容——prose 应该做表做不到的事。

4. **用 §3–§7 的文献做 evidence，不做 enumeration。** 提到具体工作只在两种情况下：(a) 作为某个结构性特征的典型实例（一个工作代表一类现象），(b) 作为反常案例（偏离框架预测的工作，需要解释）。

5. **保持从属于 transformation 主轴。** Introduction 明确把本文和 memory survey 划开。§8 的 utilization 分析要停在"机制类型 + 成本结构 + 控制度"的抽象层，不滑入 retrieval 算法细节。

6. **敢于说"目前没有好的方案"。** 不可化约张力、失配分析中的"低可恢复性"——这些是分析产出，不是分析缺陷。明确标注哪些是框架能解决的（通过载体组合缓解张力），哪些是框架只能诊断但不能解决的（→ §9）。

---

## 附录：关键术语对照

| 中文 | English |
|------|---------|
| 存在层次原则 | Existence-Level Principle |
| 形式化原则 | Formalization Principle |
| 功能角色原则 | Functional-Role Principle |
| 消费接口 | Consumption Interface |
| 激活选择性 | Activation Selectivity |
| 成本结构 | Cost Structure |
| 控制自由度 | Control Freedom |
| 维护机制 | Maintenance Mechanism |
| 转化语义 | Transformation Semantics |
| 信息动态 | Information Dynamics |
| 可追溯性 | Traceability |
| 增量性 | Incrementality |
| 产物可验证性 | Output Verifiability |
| 可组合性 | Composability |
| 数据前提 | Data Prerequisite |
| 输入鲁棒性 | Input Robustness |
| 生产机制 | Production Mechanism |
| 生产成本 | Production Cost |
| 硬约束剪枝 | Hard Constraint Pruning |
| 联盟约束 | Aligned Constraints |
| 竞争约束 | Competing Constraints |
| 不可化约张力 | Irreducible Tension |
| 并行互补 | Parallel Complement |
| 分层分级 | Tiered Routing |
| 时序分阶段 | Temporal Staging |
| 失配分析 | Mismatch Analysis |
| 时序演化 | Temporal Evolution |
| 载体迁移 | Carrier Migration |
