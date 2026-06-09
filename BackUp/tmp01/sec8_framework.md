# §8 Pathway-Level Analysis — 完整分析框架

## 〇、地基：从 §2 已立的概念出发

§8 不引入任何 §2 未定义的新轴系。框架的全部推导起点只有两个 §2 已建立的事实。

**事实 1（§2.1）**：Agent 决策规则

$$a_t \sim \pi_\theta(\cdot \mid c_t)$$

经验要影响 $a_t$，只能通过两个入口——进入 $c_t$（外部、显式），或进入 $\theta$（内部、隐式）。当考虑作用在 $\pi_\theta$ 候选输出上的 selection 算子时，存在第三个位置：$\mathrm{Select}\big(\pi_\theta(\cdot\mid c_t),\, v_\phi\big)$——该算子不改变 $c_t$ 或 $\theta$，而是对输出分布做后置调制。经验影响决策的位置穷举为三处：$c_t$（输入通道）、$\theta$（参数通道）、$v_\phi$（选择通道）。

**事实 2（§2.3）**：Carrier 沿 Tokenized → Latent → Parametric 连续谱分类。沿此方向，可解释性与可编辑性递减，推理效率递增，存储位置从外部数据库/prompt 移至 GPU memory 再到 model checkpoint。

§8 的核心工作是将这两个事实之间的因果关系显式化：**事实 2 中的谱位置锁定了事实 1 中的进入通道，进而锁定了利用代价、访问粒度与可修订性。三者不是独立可调的维度——它们同出一源。**

---

## 一、概念架构：一棵树，不是网格

### 1.1 根轴 = 存在层次谱

Carrier 的存在形式决定它通过哪个通道进入决策循环。这不是设计选择，是结构约束：

| 存在层次 | 进入决策的通道（由存在形式决定） |
|---|---|
| Tokenized | 输入通道（$c_t$）：离散 token 经检索后注入 context，参与前向传播 |
| Latent | 输入通道（$c_t$）：连续向量注入 attention/hidden-state，不占 token 位 |
| Parametric (Policy) | 参数通道（$\theta$）：权重恒在，前向传播自动激活 |
| Parametric (Evaluator) | 选择通道（$v_\phi$）：对 $\pi_\theta$ 候选输出施加 score/rank/reward 信号 |

可执行 Schematic 不构成独立通道：经验经外部 executor 执行后，产物仍注入 $c_t$，走的是输入通道的变体。Latent 与 Tokenized 共享输入通道，区别在于注入形式（连续 vs. 离散），不需要额外解码步骤。

通道一旦定，利用代价的结构（每次复用付什么、付在哪里）随之定。这是 utilization-driven selection 的硬约束层。

### 1.2 核心命题：separability–amortization trade-off

> 经验在 Tokenized → Latent → Parametric 谱上的位置决定其以**可分离单元**保存还是**融入共享参数**。可分离保存允许逐单元访问（细粒度、可编辑、可追溯），代价是每次复用需重读或重执行（per-use 成本）；融入参数将利用摊销到近零边际，代价是丧失逐单元访问。访问粒度、利用代价与可修订性三者沿谱同向变动，因其同为存储形式选择的不同侧面。

推导直接来自 §2 的内部概念：

- §2.3.1 已指出 Tokenized → Parametric 方向上可解释性↓、推理效率↑、可编辑性↓。这三者的共变不是经验巧合——Tokenized 载体以离散 token 序列存在于模型外部（§2.3.2），每个 reflection、每条 rule 是独立寻址的单元，可被单独定位、阅读、编辑或删除；但每次复用必须将该单元重新载入 context，支付检索延迟与 prefill 开销。Parametric 载体以连续权重存在于模型内部（§2.3.2），前向传播自动激活，每单位经验的边际利用成本趋零；但单条经验的贡献被 batch 梯度累积淹没，无法在推理时选择性激活"这一条而非那一条"。
- 两者互斥的根源是同一选择：单元隔离要求经验以相互独立的符号结构存储，摊销要求经验以相互交融的数值分布存储。没有载体能同时满足两者。

该命题的解释范围：7 条路径的生产代价差异（§8.1）与 7 个载体单元的消费特性差异（§8.2）均是该命题在各自侧面的投影。它对 Policy（参数通道）严格成立；Evaluator 通过选择通道部分解耦了存储融合与访问粒度，构成命题单调性的结构性例外（见 §1.3.2 与 §8.3 待定项）。

### 1.3 两个 subclass 分叉

Subclass 分叉不沿根轴移动载体位置——它们在同一存在层次内部做区分，不影响载体在 separable↔fused 谱上的坐标。但它们的分析后果在 §8.1–§8.3 中吃重，必须在开篇显式建立。

#### 1.3.1 Formalization 分叉（Tokenized 层内）：Narrative / Schematic

分叉依据是 §2.3.2 已定义的形式化程度。此分叉不改变载体的谱位置（两者同处可分离端），但改变**产物的验证模式**：

- Narrative 通过 language/multimodal understanding 消费，验证靠"读"——人类或强 LLM 判断语义正确性。覆盖"说得对不对"，盲区是"说得好但做不到"。验证是主观的。
- Schematic 通过 parsing/execution/graph traversal 消费，验证靠"跑"——execution test 给出客观通过/失败信号。覆盖"跑不跑得通"，盲区是"跑得通但方向错"。验证是客观的。

两者同为"高可验证性"，但不是同一种可验证性——是类别的差异，而非程度的差异。这一区分对 §8.3 的安全约束分析有直接后果：execution safety 偏向 Schematic（可执行测试 gate），semantic safety 偏向 Narrative（人类可事前审查内容）。

#### 1.3.2 Functional-Role 分叉（Parametric 层内）：Policy / Evaluator

分叉依据是 §2.3.2 已定义的功能角色。此分叉不改变载体的存储形式（两者同处融合端），但改变**经验进入决策的通道**和**载体在 pathway 图中的拓扑位置**：

- Policy 走参数通道（$\theta$），产生动作。动作产生新 trajectory（Tokenized），可被任何以 Tokenized 为源的 pathway 消费——Policy 通过 P7 外化或 rollout 隐式外化，重新进入 pathway 图。它是强连通分量成员（可通过 P7 → P5 闭环）。
- Evaluator 走选择通道（$v_\phi$），产生评估信号（score/rank/reward）。评估信号的语义是"对行为的判断"，唯一有意义的消费方是行为生产者 Policy——Evaluator 只有出边 P6。它是 pathway 图的汇节点。

**Evaluator 是核心命题单调性的结构性例外。** Policy 与 Evaluator 同处融合端（存储上不可分），但 Evaluator 保留了 Policy 不具备的访问粒度：可选择用哪个评估器、信号从 decode 引导/rerank/best-of-N/RL reward 哪个点进入、outcome 级还是 step 级评分。该粒度不来自存储形式（存储仍是 fused），而来自选择通道——评估信号后置于 $\pi_\theta$ 输出分布，是独立于参数通道的可拆卸调制步骤。因此核心命题的单调性限定于输入通道（$c_t$）和参数通道（$\theta$）上的载体；选择通道（$v_\phi$）因其后置调制特性而部分解耦了存储融合与访问粒度。该解耦的可推广性——能否在生成端实现融合存储下仍可选择性调取、可局部修正——是 §9 的核心 open problem。

### 1.4 树的全貌

```
根轴: 存在层次谱 (≡ separable ↔ fused)
  │
  ├── Tokenized (可分离端)
  │     ├── Narrative ── 验证: "读" (语义, 主观)
  │     └── Schematic ── 验证: "跑" (形式, 客观)
  │
  ├── Latent (中间)
  │     (session-scoped / trained 两种实现形态, 不作为正式子类)
  │
  └── Parametric (融合端)
        ├── Policy ── 通道: θ (生成) ── 拓扑: 枢纽
        └── Evaluator ── 通道: v_φ (选择) ── 拓扑: 汇节点
                                 ── 例外: 粒度与存储部分解耦
```

§8 全程只用这棵树。§8.1 的生产画像、§8.2 的利用画像、§8.3 的约束选择，全部作为树的可推导后果展开。

---

## 二、§8.1 Pathway Production Profiles（生产视角）

### 2.1 分析对象与边界

分析对象是**转化操作本身的结构特性**，而非目标载体的静态属性。例："Policy 可解释性低"是 Policy carrier 的属性（§2.3 已覆盖），不是 P5 的专属特征——P4 的产物也是 Parametric，同样不可解释。真正属于 P5 的 trade-off 是：它需要大规模 trajectory 作为输入，通过 gradient-based training 执行转化，单条经验贡献不可区分，新增经验需重新训练。这些不是 Policy carrier 的属性，而是"从 trajectory 到 policy weights"这条转化路径的属性。

此边界若失守，§8.1 将沦为 §2.3 的复读。

### 2.2 五个分析维度

| # | 维度 | 核心问题 |
|---|---|---|
| D1 | Production Mechanism | 转化靠什么计算机制执行？ |
| D2 | Construction Cost | 消耗多少计算/人力/时间？ |
| D3 | Information Transformation | 经验信息在转化中被保留、损失、注入了什么？ |
| D4 | Incrementality | 新经验持续到来时，能否增量执行？ |
| D5 | Output Verifiability | 转化产物能否在不依赖下游任务表现的情况下被独立验证？ |

D3（Information Transformation）是相对于 §2 载体静态属性的主要分析增量——它刻画转化过程对经验信息做什么，是 §2 的载体分类完全覆盖不到的。D3 内部含四个子维度：

- **Information Preservation**：源经验中的什么语义内容在转化后仍可获取？
- **Information Loss**：转化丢弃了什么？关键区分——lossy-by-design（抽象/压缩必然丢弃细节，损失类别可控）vs. lossy-by-limitation（欠拟合/reward hacking/采样偏差导致的损失，损失类别不可控，是工程风险而非设计意图）。
- **Information Gain**：转化是否产生了源经验中不显式存在的新信息？（跨轨迹归纳产生的统计性知识、形式结构注入的显式依赖、连续表示捕获的隐式统计规律等。）
- **Traceability**：转化产物的哪些元素能对应回源经验的哪些片段？此维度决定经验被审计或纠错时，问题是出在源经验上还是出在转化操作上。

### 2.3 分组逻辑

7 条路径按转化在 separable↔fused 谱上的跨度分三组。组内共享 trade-off 模式，组间有结构性差异。

**G1 同层精炼（P1, P2）**：源与目标同处 Tokenized 端。转化靠 LLM inference，产物保持可读性，可增量。对比焦点在 information transformation 的性质差异——P1 做语义抽象（保留模式与洞察，损失步骤与时序，属 lossy-by-design），P2 做结构形式化（保留过程结构，损失 NL 隐含假设，注入显式依赖结构）。两者的信息注入均来自执行转化模型的先验，而非源经验本身——抽象不增加 Shannon 信息量。

**G2 跨层内化（P3, P4, P5）**：自 Tokenized 跨至 Latent/Parametric。除 P3 cache 子类外均经 gradient-based training，可读性骤降，增量性受限。三者沿压缩程度与不可追溯性递增排列——P3 保留计算状态但最轻量（cache 子类连训练都不需要），P4 专化评估能力但产物在 pathway 图中终端化（§1.3.2），P5 改写决策能力但单条贡献不可区分。P5 的损失含 lossy-by-design（压缩）和 lossy-by-limitation（欠拟合/reward hacking）两类，后者为工程风险而非设计意图。

**G3 以 Parametric 为源（P6, P7）**：两者的共性是"用已有隐式经验做第二件事"。P6 将已内化的评估能力转为 Policy 更新的监督，成本叠加于 P4，换取 trajectory-only 无法提供的细粒度偏好，方向是进一步深入融合端。P7 将权重中的隐式能力经采样恢复为显式 token，方向是退出融合端——两条路径方向相反，在 pathway 图中的 composability 角色互补：P6 终端化（产物 Policy 虽可继续参与 pathway 图，但 P6 这一步本身止于 Policy），P7 是闭环节点（使经验重入 pathway 图的循环，是 §7.3 自生成环的结构基础）。

### 2.4 总表

| Pathway | Mechanism | Construction Cost | Information Transformation | Incrementality | Output Verifiability |
|---|---|---|---|---|---|
| P1 Narrative Abstraction | LLM inference | 低·可全自动 | **保留**: 模式与洞察 / **损失**: 步骤与时序(by-design) / **注入**: 跨轨迹综合 insight(源自模型先验) | 增量(append); dynamic store 有 merge/prune 级联 | 直接阅读判断(主观) |
| P2 Schematic Formalization | LLM inference + 可选 execution 验证 | 中·需可执行环境 | **保留**: 过程结构 / **损失**: NL nuance/隐含假设(by-design) / **注入**: 显式依赖结构 | 增量(新 artifact 入库) | execution test(客观, coverage-limited) |
| P3 Latent-Space Transformation | cache: gradient-free / trained: gradient | cache 低·仅 session; trained 中 | **保留**: 计算状态 / **损失**: 符号可读性(by-design) / **注入**: token 未显式编码的统计规律 | cache 即时重建; trained 需 batch 重训 | 无直接验证·仅 ablation 间接 |
| P4 Evaluator Internalization | gradient training | 高·需标注或明确成败信号 | **保留**: 评估偏好 / **损失**: 校准来源与单条贡献(mix: by-design + by-limitation) | batch 重训; 新标注需重训以保校准 | 无直接验证·hold-out calibration check |
| P5 Policy Internalization | gradient training (SFT/RL) | 高·需大规模高质量 trajectory | **保留**: 决策模式 / **损失**: 单条贡献不可区分(by-design) + 欠拟合/reward hacking 风险(by-limitation) | batch 重训(可热启动); RL 可在线但漂移衰减旧经验 | 仅 behavioral (rollout 间接比较) |
| P6 Evaluator-Driven Optimization | gradient training (RLHF/DPO) | 高·叠加 P4 成本 | **保留**: 偏好迁移入 policy / **注入**: trajectory-only 学不到的细粒度偏好 / **损失**: 经 P4+P6 双重压缩 | online/iterative·漂移敏感 | behavioral·**循环验证风险** (Evaluator ⇄ Policy) |
| P7 Parametric Externalization | 从 policy 采样生成 | 中·依赖采样质量·须先有 trained policy | **保留**: 权重中的能力经采样部分恢复为 token / **损失**: 采样未覆盖部分 / **注入**: hallucination 风险 | 可增量生成新样本·跟随源模型更新 | 产物可读但不可追溯权重成分·完备性不可验证 |

### 2.5 立论用的非平凡读数

以下四条是 prose 展开的核心论点，不是对表格的逐行复述：

1. **Mechanism 将 7 条路径二分为 inference-based 与 training-based**，边界落于 G1 与 G2∪G3 之间。这对应基础设施需求的质变——仅需 API 访问 vs. 需 GPU 训练集群。它是 pathway 选择的第一道硬过滤：没有训练基础设施的 practitioner 被限制在 G1。

2. **Traceability 与 verifiability 沿 explicit → implicit 单调下跌**，是 separability–amortization 在生产侧的投影。越趋融合端，产物越缺乏可独立检视的单元，转化质量越难独立判定。P1 的产物可直接阅读判断，P5 的产物只能通过 rollout 间接比较——这不是连续的"程度"差异，是质变：P1 和 P5 之间横着一条"可用直接证据验证"与"只能靠间接行为推断"的分界线。

3. **Policy 是唯一有两条生产路径的载体**（P5 从 trajectory 直训 / P6 经 Evaluator 信号），两者代价画像不同——P5 需大规模高质量 trajectory，P6 需先有 Evaluator（叠加 P4 成本）但可学到 trajectory-only 无法提供的细粒度偏好。这使 §8.3 的可行性步骤成为**路径选择**（P5 还是 P6），而非二元判断。

4. **循环验证（P6）与 hallucination（P7）是仅现于过程层的风险**，§2 的载体静态属性无法识别——循环验证来自 Evaluator 与 Policy 的互为参照（两者在训练中互相提供 ground truth，缺乏独立外部锚点），hallucination 来自采样的随机性（Policy 权重的采样噪声被当作知识外化）。这是 §8.1 相对 §2 的真增量。

---

## 三、§8.2 Carrier Utilization Profiles（利用视角）

### 3.1 分析对象与边界

利用画像刻画载体生产完成后如何进入决策循环：经哪个通道、能否精确取用单条经验、每次使用付多少代价、经验有误时如何修正。§2.4 末尾 deferred 的 utilization 关切（"检索策略、上下文编排、运行时维护、多载体协同"）在此按载体兑现。

分析的最小单元不是 5 个 carrier 顶层类别，而是 **7 个（存在层次 × subclass 形态）单元**。Schematic 分 executable 与 non-executable——前者走 external execution（产物入 context），后者走 context injection（artifact 直接入 context），在利用代价和延迟敏感性上截然不同。Latent 分 session-scoped 与 trained——前者无训练成本但仅 session 内有效、session 结束自动失效，后者跨 session 可复用但需训练、且占虚拟 token 位。这些区分在 §8.3 的约束压力表中吃重。

### 3.2 四个分析维度

| # | 维度 | 核心问题 |
|---|---|---|
| D1 | Access Interface | 经验从架构的哪个通道进入决策循环？ |
| D2 | Access Granularity | 能否在推理时有选择地激活特定经验，还是整个载体始终全开？ |
| D3 | Utilization Cost | 使用经验需要支付什么资源？计算发生在哪里（GPU prefill / external executor / forward pass / extra forward pass）？ |
| D4 | Revisability | 发现经验有误时，如何修正？修正是否影响其他经验？ |

**维度取舍说明。** Interpretability 与 control freedom 不列为独立维度。前者是 access granularity 与存在层次位置的下游读数——Tokenized 可读是因为 per-item 粒度 + 离散符号，Parametric 不可读是因为 indivisible + 连续权重。后者同样是 granularity 的函数——per-item 粒度允许在检索/编排/注入各环节调节，indivisible 则不允许。将二者单列将与 access granularity 重复。它们的分析位置在 §8.3，作为约束的对偶出现。

### 3.3 利用画像表

| Carrier (subclass) | Access Interface | Access Granularity | Utilization Cost (计算位置) | Revisability |
|---|---|---|---|---|
| Narrative | context injection（$c_t$） | per-item（精确取单条 reflection/rule） | retrieval latency + context tokens·每次复用均付（GPU prefill + 外部检索） | append/edit/delete·逐条互不影响 |
| Schematic — executable | external execution → 产物入 $c_t$ | per-skill | execution compute·卸至外部 executor·通常同步阻塞 | version/replace·需重测 |
| Schematic — non-executable | context injection（$c_t$） | per-item / per-node | context tokens（GPU prefill） | version/replace |
| Latent — session-scoped | forward-pass attention（$c_t$） | per-session（整段·粗） | 无独立检索/编码开销·融入 forward pass（GPU） | session 结束自动失效 |
| Latent — trained | forward-pass attention（$c_t$） | per-bank | 占虚拟 token 位的 attention/KV·与 bank 长度成正比·非零（GPU） | 改训练数据·重训整个 bank |
| Policy | forward-pass weights（$\theta$） | indivisible / always-on（全局生效，不可取单条） | 零边际（每单位经验）·仍付完整 forward pass（GPU） | retrain·可能 catastrophic forgetting |
| Evaluator | selection signal: score/rank/reward（$v_\phi$） | per-evaluator（选哪个 + 信号注入点 + outcome/step 粒度）·内部不可分 | 额外 forward pass·offline 可摊销 / realtime gate 纯增量 | retrain·可能破坏校准 |

### 3.4 立论用的非平凡读数

1. **访问接口由存在层次锁死。** Tokenized 必须走 context injection，Policy 必须走 forward-pass weights，Evaluator 必须走 selection signal。不存在"选载体但不选接口"的自由度——选载体同时锁定了怎么用。这是 utilization-driven selection 的硬约束层。

2. **访问粒度沿 explicit → implicit 单调退化**（per-item → per-skill/node → per-session/bank → indivisible），与 separable↔fused 谱一致。Evaluator 为例外——其粒度来自选择通道的后置调制特性，与存储融合解耦（见 §1.3.2）。

3. **"零边际"仅对 Policy 的每单位经验成立，且仍付完整 forward pass。** trained-Latent 的 per-use 成本亦非零——soft prompt 占用虚拟 token 位，开销随 bank 长度线性增长。zero marginal 与 zero cost 不可混用。

4. **Evaluator 的信号注入点是利用侧的自由度。** 信号可从 decode 引导、rerank、best-of-N、RL reward、数据筛选等不同位置进入，粒度可从 outcome 级到 step 级。这一自由度不来自存储（存储仍是 fused），而来自选择通道的可拆卸性——与 Policy 的"indivisible / always-on"形成载体层最尖锐的利用不对称性。

---

## 四、§8.3 Constraint-Driven Pathway Selection（选择视角）

### 4.1 基本原则

§8.3 不引入新维度。它把任务约束读为 §8.1 与 §8.2 中各供给 facet 的对偶，界定可行载体与路径。若匹配中缺数据，补回 §8.1 或 §8.2，不在 §8.3 临时造。

选择逻辑的推理方向是：**先定目标载体（消费侧约束 → 载体），再定生产路径（生产侧约束 → pathway），再检验可行性。** 不是扁平的"约束 → 路径"直接映射。

### 4.2 约束作为供给 facet 的对偶

| 任务约束 | 对偶的供给/利用 facet | 数据来源 |
|---|---|---|
| 延迟上限 / context 容量 / compute budget / 单次成本上限 | Utilization Cost | §8.2 |
| 可解释性 / 审计要求 / 数据合规（如 PII 不入权重） | Access Granularity + 存在层次位置 | §8.2 |
| 可修正速度 / 环境变动频率 | Revisability + Incrementality | §8.2 + §8.1 |
| 训练资源可得性 / 标注可得性 | Construction Cost | §8.1 |
| 经验体量 / 到达速度 | （调节量——放大上述某项约束的压力强度，不直接施压） | — |

各约束的具体子维度（延迟分 hard-real-time / interactive / offline，context 分 severely-constrained / moderate / abundant，可解释分 mandatory / preferred / not-required 等）在 prose 中展开，作为"如何从任务场景读出约束强度"的操作指南，不单独成表。

### 4.3 约束 → 载体压力表

行 = 7 个约束维度，列 = 7 个载体单元。↑↑ 强 toward，↑ toward，○ 中性，↓ against，↓↓ 强 against。每格为结构性推断，正文须锚至 §3–§7 中表现该压力的具体系统。

| 约束 | Narrative | Schematic (exec) | Schematic (non-exec) | Latent (session) | Latent (trained) | Policy | Evaluator |
|---|---|---|---|---|---|---|---|
| 低延迟 | ↓↓ | ↓ | ↓ | ↑ | ○ † | ↑↑ | ↓(realtime) / ○(offline) |
| context 紧 | ↓↓ | ○ | ↓ | ↑ | ↑ | ↑↑ | ○ |
| 大体量经验 | ↓ | ↑ † | ↓ | ↓ | ↓ | ↑↑(推理 O(1)) | ↑ |
| 强可解释 | ↑↑ | ↑ | ↑↑ | ↓ | ↓ | ↓↓ | ↓ |
| 快可修正 | ↑↑ | ↑ | ↑ | ↓ | ↓ | ↓↓ | ↓↓ |
| 高环境变动 | ↑ | ↓ | ↑ | ↑ | ↓ | ↓↓ | ↓↓ |
| 安全关键(事前可验) | ↑↑ | ↑↑ | ↑↑ | ↓ | ↓ | ↓↓ | ↑ |

**三处待定标注（†）——正文写作前需确定：**

1. **Schematic(exec) 在"大体量"标 ↑ †**：体量大时 skill library 增大，skill selection 变难——是否抵消"每个 skill 独立执行、不争 context"的好处？若抵消则降为 ○。
2. **Latent(trained) 在"低延迟"标 ○ †**：soft prompt/memory bank 占虚拟 token 位的 attention 开销，能否压过 token 检索 + 编码？取决于 bank 长度假设。正文须把假设写明。
3. **Evaluator 在"快可修正"标 ↓↓**（与 Policy 同级）：Evaluator 虽在访问粒度上部分解耦（§1.3.2），但修正仍需 retrain、可能破坏校准——修正侧的融合存储约束未被选择通道绕过。

### 4.4 选择流程

**Phase 1 — 约束抽取。** 从任务场景读出各约束维度的强度，而非先验假定。Prose 中给出每个约束维度的操作化问题（如"单步决策允许的最大延迟是多少？""经验总量预计以什么速度增长？""是否有监管要求必须能审计决策依据？"）。

**Phase 2 — 硬约束剪枝。** 某些约束是 hard constraint——不满足直接排除载体，不与其他约束加权。典型 dictator：
- 安全关键至错误不可逆 → Policy 与 Latent 出局（产物无法事前验证）
- 监管强制可解释 → Policy 与 Latent 出局
- 硬实时（延迟 < 50ms）→ Narrative 与 Schematic-execution 出局

剪枝等价于在（存在层次 × subclass）平面上切除不可行区。此步骤缩小搜索空间。

**Phase 3 — 多约束解析。** 在幸存载体中做多约束交叉：
- **联盟（aligned constraints）**：多约束指向同一方向 → 推荐 overdetermined，稳健性最高。例：低延迟 + 大体量 + 低可解释需求 → 三重 toward Policy。
- **张力（competing constraints）**：两约束的对偶各拉向 separable↔fused 谱两端 → 单载体无解，需组合。详见 §4.5。

### 4.5 不可化约张力对

张力是 §8.3 的核心分析产出——不是分析缺陷，是 separability–amortization 的直接推论。谱上不存在同处两端的点。

| 张力对 | 冲突 | 结构性无解之由 |
|---|---|---|
| 低延迟 × 强可解释 | Policy 快但不透明，Narrative 透明但慢 | 透明需可分离单元（每次重读），零延迟需融合（不可读） |
| 大体量 × 强可解释 | Policy 可 scale 不可读，Narrative 可读不可 scale | 大体量下检索精度下降 + context 不足，加检索预算无法补救——问题不在检索质量，在 context window 的物理上限 |
| 高环境变动 × 低延迟 | 频繁更新偏 Narrative（可逐条修正），零边际偏 Policy（推理 O(1)） | 频繁更新需可分离单元，零边际需融合——二者互斥 |
| 快可修正 × 大体量 | 逐条修正不 scale（人力不可承受），retrain 太慢（周期过长） | 大体量下人力逐条修正不可承受，重训周期又过长——两头堵 |

这些张力解释了三项事实：(i) §7 的 composite pipelines 为部分缓解张力而存在；(ii) 不存在普适最优载体——张力是结构性的，不是暂时的工程困难；(iii) §9 的 open problem 是如何动态调节载体组合以响应张力的时变。

**与 §7 的分工：** §8.3 只回答"张力为何迫使组合"，组合的具体形态交还 §7。若正文保留并行互补、分层分级、时序分阶段三种组合模式，须逐一显式映回 §7 已立的 composition pattern（Evaluator–Policy Co-Evolution 对应并行互补与分层分级中的 Evaluator gate 模式，Refinement-Mediated Policy Internalization 对应时序分阶段中的 Narrative → Policy 迁移，Generative Experience Curation 对应 Policy → Tokenized → Policy 闭环），杜绝与 §7 重复。

### 4.6 载体组合 → 生产路径可行性

载体组合确定后，对每个目标载体回查 §8.1 检验生产路径的可负担性：

- 目标 Narrative → P1（低成本、可增量），可行
- 目标 Schematic → P2（需 LLM inference + execution verification，需 interface 相对稳定）
- 目标 Latent(session) → P3 cache-based（无训练成本，但不跨 session）
- 目标 Latent(trained) → P3 trained（需训练）
- 目标 Policy → **路径选择**：P5（从 trajectory 直训，需大规模高质量数据）还是 P6（从 Evaluator 信号训练，需先有 Evaluator，但可学到 trajectory-only 无法提供的偏好）？两者的代价画像不同——这是 §8.1 读数 (iii) 的直接应用
- 目标 Evaluator → P4（需标注或明确成败信号）

若目标载体在消费侧完美匹配约束、但唯一可行的生产路径在生产侧代价不可承受 → 这是真实困境，如实记录，指向 §9（需更低成本的 Policy Internalization 方法、更高效的 Latent 训练等）。

### 4.7 时序演化：约束漂移与载体迁移

约束有时间导数——经验体量单调增长，任务分布漂移，工具 API 变化，安全要求可能升级——可行域随之移动。最优载体配置是时间的函数。

系统初期经验少，Narrative store 检索精度高、context 开销小，P1 充分。经验积累至百万条后，检索质量下降、context 紧张，需向 Policy 迁移（P5 或 P6）。迁移本身是一条有完整生产画像的 pathway——其一次性训练成本须由 Policy 利用侧的节省收回。迁移过早则训出的 Policy 不足、切换后退化；迁移过晚则持续的检索退化已造成累积效率损失。迁移时机是收益–成本优化问题。

在此视角下 §7 的复合路径获得时序读法：Refinement-Mediated Policy Internalization（§7.2）本质是先让经验停留于 Narrative 形态（可读、可修、即时可用），积累至量且质量达标后固化进 Policy。复合路径不只是在空间上组合多条边，而是在时间上编排经验在不同载体间的停留。

目前无系统能自动完成该判断与切换——此为 §9 的直接 open problem。

### 4.8 失配分析

约束可能被误判或在部署后变化。失配分析不冠以"validation"——它是框架的**预测**，每条须拿文献核（§3–§7 中独立报告的 failure mode），吻合处算证据，不吻合处转 open question。自产自证不算数。

| 失配类型 | 预测症状 | 可恢复性 | 恢复路径 |
|---|---|---|---|
| 强可解释 × Policy | 无法审计决策、错误定位困难、修正引发 catastrophic forgetting | 低 | P7 外化 → 审查 → 筛选后重训 P5，代价极高 |
| 低延迟 × Narrative | 检索延迟叠加、context 过长致 prefill 超时 | 高 | 渐进迁移至 Latent 或 Policy |
| 大体量 × Narrative | 检索精度下降、超出 context budget、幻觉式引用 | 中 | 做 P5 迁移，需重训 |
| 高环境变动 × Policy | 策略过时、无法快速适应新工具/新 API | 低 | 重训，训练期间系统持续退化 |
| 安全关键 × Latent | 无法事前验证 latent 中经验质量 | 低 | latent 不可审计，只能放弃并重建 |

可恢复的失配对应一条有代价但可执行的迁移路径；不可恢复的失配——经验已融入权重、无法单独提取者——每条对应一个 §9 问题。

---

## 五、§8.4 The Structural Origin and Generative Power

§8.1–§8.3 的分析共同指向一个结论：载体的生产代价、利用画像与约束压力分布，共同取决于其在 separable↔fused 谱上的位置，叠加两个 subclass 分叉的修正（formalization 定验证模式，functional role 定通道与 pathway 拓扑位）。这不是五类载体的经验归纳，而是从 §2 的存在层次分类和决策规则出发的结构推论。

该归约赋予框架生成性。任一新转化技术可先在 §2 的层次结构中定位源端与目标端——这一定位即足以推断其生产机制的大致类型（inference-based 还是 training-based）、信息损失的性质（by-design 还是 by-limitation 主导）、利用侧的代价结构与访问粒度区间。分析涵盖尚未出现的形式，而不止于已有的 7 路径 5 载体。

框架同时生成否定性预测——解释为什么某些组合在结构上不可行。声称"既快又透明"的单载体方案，等价于声称存在同处 separable 与 fused 两端的载体，与核心命题矛盾。若此类系统在实践中被报告，它要么实际上维护了 Tokenized 副本供审计（那是两套载体，不是一套），要么"透明"指某种近似解释（probing、attribution）而非真正的逐单元可读。

三个结构性待解问题构成 §9 的核心：
1. separability–amortization 耦合是信息论硬约束还是当前架构的软约束？（sparse feature、可编辑 parametric memory、adapter、retrieval-over-activations 都在攻它。）
2. Evaluator 通过选择通道实现的部分解耦能否推广至生成端——是否存在融合存储下仍可选择性调取、可局部修正的 Policy 载体？
3. 最优配置随时间变化时，何种机制可在线判定迁移时机并自动重排经验在各载体间的分布？

---

## 六、写作原则

1. **准确、简洁、直接、专业。** 不使用比喻、口语化表述、华丽修辞。概念架构中的"一棵树"是内部代号，正文中用"存在层次为主轴、subclass 为分叉的层级结构"表述。
2. **每一段都在"比"或"推"，不在"列"。** §8 不逐篇复述文献——文献从 §3–§7 来，§8 只引用它们的结构性含义。表格给出对比，prose 给出对比的逻辑和推论。
3. **表格不重复 prose，prose 不重复表格。** 表是压缩的结构数据，prose 是非凡读数和论证——前者是"what"，后者是"why"和"so what"。
4. **与 §2 咬合。** §8 的每个概念都可以追溯到 §2 的术语和分类。不在 §8 中重新定义已在 §2 定义过的东西，但可以在第一次使用时以"§2.3 已定义..."的方式唤起。
5. **与 §7 咬合但不重复。** §8.3 的载体组合模式须显式映回 §7 的 composition pattern，但组合的机制细节留在 §7。
6. **待定标注（†）保留到正文写作时确定。** 三处标注在填 prose 时需给出明确判断和假设，判断须有文献依据或明确的假设边界声明。

---

## 七、§8 整体结构

```
§8 Pathway-Level Analysis

  开篇（不编号）
    - 从 §2 的决策规则和载体分类出发
    - 建立存在层次谱 ↔ 进入通道的映射
    - 陈述核心命题：separability–amortization trade-off
    - 两个 subclass 分叉及其分析后果
    - §8.1–§8.3 的预览

  §8.1 Pathway Production Profiles
    - 分析对象与边界
    - G1/G2/G3 分组 + 五个维度 prose 对比
    - 总表 (Table 8.1)
    - 四条非平凡读数

  §8.2 Carrier Utilization Profiles
    - 分析对象与边界（7 个载体单元）
    - 四个维度 + 利用画像表 (Table 8.2)
    - 四条非平凡读数

  §8.3 Constraint-Driven Pathway Selection
    - §8.3.1 约束作为供给 facet 的对偶 (Table 8.3)
    - §8.3.2 约束 → 载体压力表 (Table 8.4) + 三阶段选择流程
    - §8.3.3 不可化约张力对 (Table 8.5)
    - §8.3.4 载体组合模式（显式映回 §7 composition patterns）
    - §8.3.5 生产路径可行性检验
    - §8.3.6 时序演化：约束漂移与载体迁移
    - §8.3.7 失配分析 (Table 8.6)

  §8.4 The Structural Origin and Generative Power
    - 核心命题作为统一归约
    - 框架的生成性与否定性预测
    - 三个结构性待解问题 → §9
```
