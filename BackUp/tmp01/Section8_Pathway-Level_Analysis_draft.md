# 8 Pathway-Level Analysis

§3–§7 归纳了七条转化路径,每条在生产代价、利用代价与可修订性上呈现不同画像。这些画像是否可归约为一个共同的结构性决定量,以及该决定量对约束下的载体选择意味着什么,是 §8 所要解决的问题。

该变异归约为单一变量:载体在 localist–distributed 谱上的位置——表征学习中可分离符号单元与共享参数的区分,亦即 retrieval-augmented generation 中 non-parametric 与 parametric 知识的区分 [CITE]。§2.2 的 Tokenized → Latent → Parametric 层次即此谱:Tokenized 经验以离散单元存于模型外部(可分离端),Parametric 经验融入权重(融合端),Latent 居中。

> **The separability–amortization trade-off.** 载体在 separable↔fused 谱上的位置联合决定其利用代价、访问粒度与可修订性;三者沿谱同向变动,因其同为一个性质的不同侧面——经验以相互独立的单元保存,抑或融入相互交融的参数。

可分离表示将经验保存为相互独立的单元(reflection、skill、被索引的 trajectory),支持逐单元的定位、编辑与按需取用,但每次复用须将单元重新载入 context 或重新执行,推理开销随取用量增长。融合表示经梯度将经验均摊入权重的联合分布,单次前向传播即全部就位,边际开销趋零,但单元性被抹除,无法定位、审查或修正单条经验。二者互斥:可分离要求单元隔离,可摊销要求单元交融。访问粒度、利用代价与可修订性因此被同一存储选择一并锁定。

两个 subclass 分叉正交于该谱。Formalization(Narrative/Schematic)决定验证模式:Narrative 经语义理解消费,正确性由人工或模型判读;Schematic 经 parsing/execution 消费,正确性由执行结果客观判定;二者同处可分离端,验证质地不同而位置相同。Role(Policy/Evaluator)决定经验进入决策的通道:Policy 权重生成动作,Evaluator 权重产出信号以调制候选选择。

Role 分叉构成该谱单调性的唯一例外。Policy 与 Evaluator 同处融合端,而 Evaluator 保留访问粒度——可选用评估器、信号注入点与评分粒度(outcome/step)。该粒度源于通道而非存储:评估信号后置作用于输出分布,为可拆卸的调制步骤,与融合存储解耦。命题的单调性因此限定于经 input 与 parameter 通道的载体,selection 通道为结构性例外;其可推广性与该耦合的约束性质见 §9。

§8.1–§8.3 沿三侧展开:§8.1 以 pathway 为索引刻画生产代价与信息转换,§8.2 以 carrier 为索引刻画利用代价与粒度,§8.3 将任务约束映为前两者的对偶以界定可行解。

## 8.1 Pathway Production Trade-offs

Pathway 是将源经验重新表示为目标载体的转化算子,其生产画像刻画 §2 的载体静态属性不覆盖的三方面:转化的执行代价、转化对源经验信息的处理、面对新经验的增量能力。五个维度为 mechanism、construction cost、information transformation(preservation/loss/introduction)、incrementality、output verifiability,其中 information transformation 描述转化对信息的保留、损失与注入,为相对 §2 的主要增量。按转化在 separable↔fused 谱上跨越的距离,七条路径分三组。

**G1 同层精炼(P1, P2).** 源与目标同处 Tokenized 端,转化经 LLM inference,产物可读且可增量。二者分野在 information transformation:P1(Narrative Abstraction)做语义抽象,保留模式与洞察、损失步骤与时序,属 lossy-by-design;P2(Schematic Formalization)做结构形式化,注入显式过程约束(依赖、类型),损失自然语言的隐含假设。两者注入的内容源于执行转化的模型先验而非源经验,抽象不增加 Shannon 信息。

**G2 跨层内化(P3, P4, P5).** 自 Tokenized 跨至 Latent/Parametric,除 P3 的 cache 子类外均经训练,可读性骤降,增量受限,沿压缩程度与不可追溯性同步加深排列。P3(Latent-Space Transformation)最轻,保留计算状态、损失符号可读性,内部分 cache-based(gradient-free, session-scoped)与 trained(gradient, 跨 session);P4(Evaluator Internalization)将经验固化为判断函数,产物专化且在 pathway 图中终端化(§8.3);P5(Policy Internalization)改写决策能力,单条经验贡献不可区分。P5 的损失分两类:抽象式 lossy-by-design,与欠拟合或 reward hacking 导致的 lossy-by-limitation,后者为工程风险而非设计意图。

**G3 以 Parametric 为源(P6, P7).** P6(Evaluator-Driven Optimization)将已内化的评估能力转为 policy 更新的监督,成本叠加于 P4,换取 trajectory-only 无法提供的细粒度偏好;P7(Parametric Externalization)将权重中的隐式能力采样为显式 token,为 pathway 图中唯一的出权重操作。二者方向相反而可组合性互补:P6 终端化,P7 令经验重入 pathway 图的循环。

| Pathway | Mechanism | Construction cost | Information transformation(保留 / 损失 / 注入) | Incrementality | Output verifiability |
|---|---|---|---|---|---|
| P1 Narrative Abstraction | LLM inference | 低·可全自动 | 模式与洞察 / 步骤与时序(by-design) / 跨轨迹综合(源自模型先验) | 增量(dynamic store 的 merge/prune 有级联) | 直接阅读判断(主观) |
| P2 Schematic Formalization | LLM inference + 可选 execution 验证 | 中·需可执行环境 | 过程结构 / NL 隐含假设 / 显式依赖结构 | 增量(新 artifact 入库) | execution test(客观) |
| P3 Latent-Space Transformation | cache(gradient-free) / trained(gradient) | cache 低且仅 session;trained 中 | 计算状态 / 符号可读性 / token 未显式编码的统计规律 | cache 即时重建;trained 需 batch 重训 | 无直接验证·仅 ablation 间接 |
| P4 Evaluator Internalization | gradient training | 高·需标注或明确成败信号 | 评估偏好 / 校准来源与单条贡献 / — | 新标注通常需重训以保校准 | 无直接验证·hold-out 上 calibration check |
| P5 Policy Internalization | gradient training(SFT/RL) | 高·需大规模高质量 trajectory | 决策模式 / 单条贡献(by-limitation 风险) / — | batch 重训(可热启动);RL 可在线但漂移衰减旧经验 | 仅 behavioral(rollout 间接) |
| P6 Evaluator-Driven Optimization | gradient training(RLHF/DPO) | 高·叠加 P4 | 偏好迁移入 policy / — / trajectory-only 学不到的偏好 | online/iterative·漂移敏感 | behavioral·循环验证风险 |
| P7 Parametric Externalization | 从 policy 采样生成 | 中·依赖采样质量·须先有 trained policy | 经采样恢复的能力 / 采样未覆盖部分 / hallucination | 可增量生成新样本 | 产物作为新 Tokenized 可验·但不可追溯权重成分 |

Table 8.1 给出四个独属生产层面的结论。(i) mechanism 将七条路径二分为 inference-based 与 training-based,边界落于 G1 与 G2∪G3 之间,对应仅需 API 访问与需训练基础设施之分。(ii) traceability 与 verifiability 沿 explicit→implicit 单调下降:越趋融合端,产物越缺乏可独立检视的单元,转化越难验证。(iii) Policy 是唯一具两条生产路径的载体(P5 直训 trajectory、P6 经 evaluator 信号),代价画像不同,使 §8.3 的可行性检验成为路径选择而非二元判断。(iv) 循环验证(P6)与 hallucination(P7)是仅现于过程层的风险,载体静态分类无从识别。

## 8.2 Carrier Utilization Profiles

利用画像刻画载体造出后如何进入决策:经由哪个接口、能否精确取用单条经验、每次使用付多少、新经验到来时如何演化。四个维度为 access interface、access granularity、utilization cost(含计算发生位置)、revisability;§2.4 deferred 的 utilization 关切在此按载体兑现。

访问接口由存在形态决定。由 §8 开篇的决策式 $a_t \sim \mathrm{Select}(\pi_\theta(\cdot\mid c_t),\, v_\phi)$,经验影响 $a_t$ 仅三个位置:进入 $c_t$、进入 $\theta$、进入 $v_\phi$。Tokenized 与 Latent 走上下文通道(前者作为离散 token,后者作为连续状态注入 attention),Policy 走参数通道,Evaluator 走选择通道。可执行 Schematic 不构成第四通道:其仍走上下文通道,中间隔一道外部执行,进 $c_t$ 的是执行产物而非技能本身。分析的最小单元因此为 7 个(存在层次 × subclass 形态):Schematic 横跨两接口,Latent 分 session-scoped 与 trained 两形态,二者区分对 §8.3 至关重要。

| Carrier(subclass) | Access interface | Access granularity | Utilization cost(计算位置) | Revisability |
|---|---|---|---|---|
| Narrative | context injection | per-item | retrieval latency + context tokens·每次付(GPU prefill + 外部检索) | append/edit/delete·逐条互不影响 |
| Schematic — executable | external execution(产物入 context) | per-skill | execution compute·卸至外部 executor·通常同步阻塞 | version/replace·需重测 |
| Schematic — non-executable | context injection | per-item / per-node | context tokens(GPU prefill) | version/replace |
| Latent — session-scoped | forward-pass attention | per-session | 无独立检索/编码·融入 forward pass(GPU) | session 结束即自动失效 |
| Latent — trained | forward-pass attention | per-bank | 占虚拟 token 位的 attention/KV·与长度成正比·非零(GPU) | 改训练数据·重训整个 bank |
| Policy | forward-pass weights | indivisible / always-on | 零边际(每单位经验)·仍付完整 forward pass(GPU) | retrain·可能 catastrophic forgetting |
| Evaluator | selection(signal:score/rank/reward) | per-evaluator(选哪个 + 信号注入点 + outcome/step)·内部不可分 | 额外 forward pass·offline 可摊销 / realtime gate 纯增量 | retrain·可能破坏校准 |

访问粒度沿 explicit→implicit 单调退化(per-item → per-skill/node → per-session/bank → indivisible),与 separable↔fused 谱一致;Evaluator 为唯一例外,其细粒度源于 selection 通道(§8 开篇)。利用代价须区分两处常见误述:Policy 的零边际仅对每单位经验成立,单次前向传播的完整开销不变;trained-Latent 的 per-use 成本亦非零,soft prompt 占用虚拟 token 位,开销随长度线性增长——zero marginal 与 zero cost 不可混用。interpretability 与 control freedom 不列为独立维度:二者是访问粒度与存在层次位置的下游读数,单列将与访问粒度重复,其分析位置在 §8.3 作为约束的对偶。

## 8.3 Constraint-Driven Pathway Selection

§8.1 与 §8.2 给出供给侧两份画像。§8.3 做反向映射:将任务约束读为这两份画像的对偶,界定可行的载体与路径,不引入新维度;映射中若缺数据,补回 §8.1 或 §8.2。

### 8.3.1 约束作为供给属性的对偶

任务约束是供给侧各 facet 的镜像(Table 8.3)。经验体量与到达速度不直接施压,为调节量,放大某项约束的压力强度。

| 任务约束 | 对偶的供给 facet | 来源 |
|---|---|---|
| 延迟 / context / compute / 单次成本上限 | utilization cost | §8.2 |
| 可解释 / 审计 / 数据合规(如 PII 不入权重) | access granularity + 存在层次位置 | §8.2 |
| 可修正速度 / 环境变动 | revisability + incrementality | §8.2 + §8.1 |
| 训练资源 / 标注可得性 | construction cost | §8.1 |
| 经验体量 / 到达速度(modulator) | — | — |

### 8.3.2 约束到载体的方向性压力

将每个约束沿其对偶 facet 推至 7 个载体单元,得方向性压力表(Table 8.4)。↑↑ 强 toward,↑ toward,○ 中性,↓ against,↓↓ 强 against;每格为结构推断,正文须锚至 §3–§7 中表现该压力的系统。

| 约束 | Narrative | Schematic(exec) | Latent(sess) | Latent(trained) | Policy | Evaluator |
|---|---|---|---|---|---|---|
| 低延迟 | ↓↓ | ↓ | ↑ | ○ | ↑↑ | ↓ realtime / ○ offline |
| context 紧 | ↓↓ | ○ | ↑ | ↑ | ↑↑ | ○ |
| 大体量 | ↓ | ↑ | ↓ | ↓ | ↑↑(推理 O(1)) | ↑ |
| 强可解释 | ↑↑ | ↑ | ↓ | ↓ | ↓↓ | ↓ |
| 快可修正 | ↑↑ | ↑ | ↓ | ↓ | ↓↓ | ↓↓ |
| 高环境变动 | ↑ | ↓ | ↑ | ↓ | ↓↓ | ↓↓ |
| 安全关键(事前可验) | ↑↑ | ↑↑ | ↓ | ↓ | ↓↓ | ↑ |

选择逻辑含五阶段:Phase 1–3 基于该表,Phase 4(载体组合)见 §8.3.3,Phase 5(可行性)见 §8.3.4。**Phase 1 约束抽取**:从任务场景读出各约束强度,而非先验假定。**Phase 2 硬约束剪枝**:hard constraint 不满足即排除载体——安全关键至错误不可逆则 Policy 与 Latent 出局(产物无法事前验证),监管强制可解释同理,硬实时则 Narrative 与 Schematic-execution 出局;剪枝等价于在(存在层次 × subclass)平面切除不可行区。**Phase 3 多约束解析**:多约束同向时形成联盟,推荐 overdetermined,稳健性最高。

### 8.3.3 不可化约的张力

两个强约束的对偶各拉向 separable↔fused 谱两端时,无单一载体同时满足;此为中心命题的直接推论,谱上不存在同处两端之点(Table 8.5)。

| 张力对 | 冲突 | 结构性无解之由 |
|---|---|---|
| 低延迟 × 强可解释 | Policy 快但不透明,Narrative 透明但慢 | 透明需可分离单元(每次重读),零延迟需融合(不可读) |
| 大体量 × 强可解释 | Policy 可 scale 不可读,Narrative 可读不可 scale | 大体量下检索精度下降 + context 不足,加检索预算无法补救 |
| 高环境变动 × 低延迟 | 频繁更新偏 Narrative,零边际偏 Policy | 频繁更新需可分离单元,零边际需融合 |
| 快可修正 × 大体量 | 逐条修正不 scale,retrain 太慢 | 大体量下人力逐条修正不可承受,重训周期过长 |

这些张力是 §8 的核心产出,解释三项事实:§7 的 composite pipelines 为部分缓解张力而存在;不存在普适最优载体,因张力为结构性;§9 的 open problem 在于如何动态调节载体组合以响应张力的时变。分工上 §8.3 仅回答张力为何迫使组合,组合的具体形态交还 §7;若正文保留并行互补、分层分级、时序分阶段三种形态,须逐一映回 §7 已立的 composition pattern。

### 8.3.4 可行性检验与时序演化

载体组合确定后,对每个目标载体回到 §8.1 检验生产路径的可负担性:目标 Narrative → P1,低成本可增量;目标 Policy → P5 或 P6(§8.1(iii)),需检验训练资源与环境稳定性;目标 Schematic → P2,需 interface 稳定。若目标载体在利用侧匹配约束、但唯一生产路径在生产侧不可承受,该困境如实记录并指向 §9。

约束随时间变化:经验体量增长,任务分布漂移,工具 API 变动,故最优载体配置为时间的函数。约束的时间导数各异——体量与 staleness 收紧,训练资源放松,延迟上限不变——可行域随之移动。系统初期经验少,Narrative 检索精度高、context 开销小,P1 充分;经验积累后检索质量下降、context 紧张,需迁移至 Policy。迁移本身为一条具完整生产画像的 pathway(即 P5),其一次性训练成本须由 Policy 利用侧的节省收回;迁移过早则训出的 Policy 不足、切换后退化,故迁移时机为收益–成本判断。目前无系统能自动完成该判断与切换,此为 §9 的直接 open problem。在此视角下 §7 的复合路径获得时序读法:Refinement-Mediated Policy Internalization(§7.2)先令经验停留于 Narrative 形态(可读、可修、即时可用),积累至量且质量达标后固化进 Policy,所编排者为经验在各载体间的停留时间。

### 8.3.5 失配症状

约束可能被误判或在部署后变化。Table 8.6 列出框架预测的失配症状;其作为框架支持的效力取决于这些症状是否与文献中独立报告的 failure mode 吻合,故每行须对照 §3–§7 的实证判定为支持或反例。

| 失配类型 | 预测症状 | 可恢复性 | 恢复路径 |
|---|---|---|---|
| 强可解释 × Policy | 无法审计决策、错误定位困难、修正引发灾难性遗忘 | 低 | P7 外化 → 审查 → 筛选后重训 P5,代价极高 |
| 低延迟 × Narrative | 检索延迟叠加、context 过长致 prefill 超时 | 高 | 渐进迁移至 Latent 或 Policy |
| 大体量 × Narrative | 检索精度下降、超出 context budget、幻觉式引用 | 中 | 做 P5 迁移,需重训 |
| 高环境变动 × Policy | 策略过时、无法快速适应新工具 | 低 | 重训,训练期间系统持续退化 |
| 安全关键 × Latent | 无法事前验证 latent 中经验质量 | 低 | latent 不可审计,只能放弃重建 |

可恢复的失配对应一条有代价但可执行的迁移路径;不可恢复的失配——经验已融入权重、无法单独提取者——每条对应一个 §9 问题:如何在需要某约束的场景中安全使用融合端载体。

## 8.4 The Structural Origin of Carrier Diversity

§8.1–§8.3 表明,载体的生产代价、利用画像与约束压力分布共同取决于其在 separable↔fused 谱上的位置,叠加两个 subclass 分叉的正交修正(formalization 定验证模式,role 定通道与 pathway 拓扑)。该归约赋予框架生成性:任一新转化技术可先在 §2.2 的层次结构中定位,据以推断其三侧画像,并检验其是否突破主耦合,使分析涵盖尚未出现的形式而不止于已有的七路径五载体。

该结构提出三个待解问题,构成 §9 的核心:separability–amortization 耦合属信息论约束抑或当前架构的工程约束;selection 通道的解耦能否推广至生成端,得到融合存储下仍可选择性调取、可局部修正的载体;以及最优配置随约束时变时,何种机制可在线判定迁移时机并重排经验在各载体间的分布。
