# 8. Pathway-Level Analysis

§3–§7 按转化路径逐一梳理了社区将 agent experience 从一种载体重新表示为另一种载体的机制。每条路径在生产代价、利用代价与可修订性上呈现不同画像。本章要回答的是：这些画像能否归约为一个共同的结构性决定量，以及在任务约束下该决定量如何左右载体与路径的选择。

§2.1 将 agent 决策写为 $a_t \sim \pi_\theta(\cdot \mid c_t)$，决策依据分置于两处：流经 $c_t$ 的外部信息，与固化在 $\theta$ 中的内部能力。当考虑作用在 $\pi_\theta$ 候选输出上的 selection 算子时，经验影响 $a_t$ 的位置穷举为三处：$c_t$（输入通道）、$\theta$（参数通道）、以及评估信号 $v_\phi$ 对候选分布的后置调制（选择通道）。§2.3 将经验载体沿 Tokenized → Latent → Parametric 连续谱分类。**载体在谱上的位置锁定了它通过哪个通道进入决策循环**——Tokenized 走输入通道（离散 token 注入 context），Latent 走输入通道（连续向量注入 attention，不占 token 位），Policy 走参数通道（权重恒在，前向传播自动激活），Evaluator 走选择通道（对候选输出施加 score/rank/reward 信号）。通道决定利用代价、访问粒度与可修订性。

三者的统一根源是 **separability–amortization trade-off**。Tokenized 载体在模型外部以离散 token 序列存在（§2.3.2），每条 reflection、每条 rule 是独立寻址的单元，可逐条编辑，但每次复用都须重新载入 context。Parametric 载体在模型内部以连续权重存在，复用时无须额外载入，每单位经验的边际利用成本趋零，却无法在推理时单独取用某一条。两者互斥的根源是同一选择：单元可分离要求经验以相互独立的符号结构存储，摊销要求经验以相互交融的数值分布存储。不存在同处两端的载体。

§8.1–§8.3 沿三侧展开：§8.1 刻画每条 pathway 的生产代价与信息转换，§8.2 刻画每类 carrier 的利用代价与粒度，§8.3 将任务约束读为前两者的对偶以界定可行解。§8.4 讨论该归约的结构起源与生成性。

## 8.1 Pathway Production Profiles

本节以五个维度刻画每条 pathway 的生产画像。Production Mechanism（D1）：转化靠什么计算机制执行，如 LLM inference、gradient-based training、gradient-free persistence、execution + verification loop。Construction Cost（D2）：转化消耗多少计算与人力。Information Transformation（D3）：经验信息在转化中被保留、损失、注入了什么，以及能否被追溯（traceability）；其中 loss 区分 lossy-by-design（抽象/压缩必然丢弃细节，损失类别可控）与 lossy-by-limitation（欠拟合、reward hacking、采样偏差，损失类别不可控，属工程风险而非设计意图）。Incrementality（D4）：新经验持续到来时，转化能否增量执行。Output Verifiability（D5）：转化产物能否在不依赖下游任务表现的情况下被独立验证。

| Pathway | Mechanism | Construction Cost | Information Transformation | Incrementality | Output Verifiability | 代表工作 / 详节 |
|---|---|---|---|---|---|---|
| P1 Narrative Abstraction | LLM inference | 低·可全自动 | **保留**: 模式与洞察 / **损失**: 步骤与时序(by-design) / **注入**: 跨轨迹综合 insight(源自模型先验) | 增量(append); dynamic store 有 merge/prune 级联 | 直接阅读判断(主观) | Reflexion [Shi23b]；§3.1 |
| P2 Schematic Formalization | LLM inference + 可选 execution 验证 | 中·需可执行环境 | **保留**: 过程结构 / **损失**: NL nuance/隐含假设(by-design) / **注入**: 显式依赖结构 | 增量(新 artifact 入库) | execution test(客观, coverage-limited) | Voyager [Wan23c]；§3.2 |
| P3 Latent-Space Transformation | cache: gradient-free / trained: gradient | cache 低·仅 session; trained 中 | **保留**: 计算状态 / **损失**: 符号可读性(by-design) / **注入**: token 未显式编码的统计规律 | cache 即时重建; trained 需 batch 重训 | 无直接验证·仅 ablation 间接 | LAG [Che25b]（cache）/ ReasonCACHE [Gup26]（trained）；§4 |
| P4 Evaluator Internalization | gradient training | 高·需标注或明确成败信号 | **保留**: 评估偏好 / **损失**: 校准来源与单条贡献(mix: by-design + by-limitation) | batch 重训; 新标注需重训以保校准 | 无直接验证·hold-out calibration check | Let's Verify Step by Step [Lig23]；§5.1 |
| P5 Policy Internalization | gradient training (SFT/RL) | 高·需大规模高质量 trajectory | **保留**: 决策模式 / **损失**: 单条贡献不可区分(by-design) + 欠拟合/reward hacking 风险(by-limitation) | batch 重训(可热启动); RL 可在线但漂移衰减旧经验 | 仅 behavioral (rollout 间接比较) | SWE-Gym [Pan24]；§5.2 |
| P6 Evaluator-Driven Optimization | gradient training (RLHF/DPO) | 高·叠加 P4 成本 | **保留**: 偏好迁移入 policy / **注入**: trajectory-only 学不到的细粒度偏好 / **损失**: 经 P4+P6 双重压缩 | online/iterative·漂移敏感 | behavioral·循环验证风险 (Evaluator ⇄ Policy) | Constitutional AI [Bai22b]；§6.1 |
| P7 Parametric Externalization | 从 policy 采样生成 | 中·依赖采样质量·须先有 trained policy | **保留**: 权重中的能力经采样部分恢复为 token / **损失**: 采样未覆盖部分 / **注入**: hallucination 风险 | 可增量生成新样本·跟随源模型更新 | 产物可读但不可追溯权重成分·完备性不可验证 | Explorer [Pah25]；§6.2 |

**Table 8.1.** Pathway production profiles across five dimensions.

**Production Mechanism** 把七条路径沿是否更新权重切成两组。P1、P2、P3 的 cache 子类与 P7 不更新权重——P1、P2 靠 LLM inference，P3-cache 靠 gradient-free 的前向状态留存，P7 靠从已训练模型采样；P3 的 trained 子类与 P4、P5、P6 经 gradient training，需数据筹备与优化的整套机制，单步资源消耗高于一次 inference。P2 在 inference 之外可叠加 execution + verification loop，是不更新权重一侧唯一带客观产出闸门的机制。

**Construction Cost** 在 gradient 一类整体高、inference 一类整体低。P4 卡在标注或明确成败信号的获取，P5 卡在大规模高质量 trajectory，P6 在 P4 的 Evaluator 训练之上再叠一层、成本累加。P1 可全自动、近零成本，P3-cache 极低但仅 session 内有效，P2 中等、需可执行环境；P7 受制于采样质量，且须先有 trained policy——它的低成本只就外化这一步而言，不含上游训练。

**Information Transformation** 的关键分野在 loss 的两种性质。七条路径注入的新信息都来自转化模型的先验、而非源经验——抽象不增加 Shannon 信息量。P1（丢步骤与时序）、P2（丢 NL nuance 与隐含假设）、P3（丢符号可读性）的损失均为 lossy-by-design，损失类别可控、由抽象策略调节；P4、P5 在 by-design 之外混入 lossy-by-limitation——P4 的标注噪声与标注者不一致直接进权重，P5 的 SFT 欠拟合与 RL reward hacking 不可控，属工程风险而非设计意图；P6 的损失是 P4 阶段与 P6 阶段的双重压缩，原始经验语义到达后已不可辨识；P7 的损失来自采样未覆盖的部分，并注入 hallucination 风险。traceability 沿 P3 → P4 → P5(→ P6) 单调下跌：P3-cache 的 KV 直接来自真实前向传播、能对应具体历史片段，P3-trained 的 soft prompt 已无法对应回单条经验，P4/P5/P6 把单条贡献经 batch 梯度平均进权重、无法追问某个决策用了训练集中哪条轨迹；P7 从另一侧失效——产物虽是可分离 token，却采样自融合权重、追不到源知识。这道下跌是 batch 梯度平均的结构性后果，与工程精度无关。

**Incrementality** 在 inference 一类天然增量——P1 append、P2 新 artifact 入库、P3-cache 即时重建、P7 随源模型更新持续生成新样本；gradient 一类须 batch 重训，P3-trained 改训练数据即重训整个 bank、P4 的新标注需重训以保校准。P5 可热启动、RL 还能在线更新，但旧经验的效用随分布漂移衰减，在线性以遗忘旧经验为代价；P6 的 online/iterative 更新同样对漂移敏感。P1 一侧的 dynamic store 在 append 之外带 merge/prune 级联，单条写入可能触发已有条目的连带改写。

**Output Verifiability** 不沿 Tokenized → Latent → Parametric 谱递减，取决于产物容许哪种独立检验。P2 的 code skill 由环境 execution 给出客观二值信号（如 Voyager 的 verification gate，通过/失败可判定，但测试完备性无法保证、未覆盖的 corner case 仍可能失败），P1 的 reflection 只能靠人或强 LLM 主观阅读、两审阅者可能给出不同结论——同处 Tokenized 端却分居客观与主观，决定 verifiability 的是检验类型而非载体位置。向融合端，P4 的 Evaluator 尚可用 hold-out calibration 间接核验，P3、P5、P6 退到只能借 rollout 或 ablation 推断，P7 又从另一侧受限：产物虽可读，却追不到采样自哪部分权重、完备性不可验证。

几个结构事实不落在任何单一维度上。P6 与 P7 都以已固化的 Parametric 经验为源、做第二步加工，方向相反、在 pathway 图中互补：P6 把 Evaluator 的判断进一步写入 Policy 权重、深入融合端，P7 把 Policy 或 Evaluator 的能力采样回 Tokenized、退出融合端，使权重中的隐式经验重新成为可供其他路径使用的显式载体。Policy 由 P5、P6 两条路径产生，二者代价画像不同，使 §8.3 对 Policy 目标的可行性判断成为 P5 还是 P6 的选择、而非二元判断；多生产路径并非 Policy 独有——Narrative 既可由 P1 同层精炼、也可由 P7 从权重外化。循环验证与 hallucination 是仅现于转化过程的两类风险：前者来自 P6 中 Evaluator 与 Policy 互为参照、缺独立外部 ground truth（ECHO [Li26l] 的同步更新可缓解、不能消除），后者来自 P7 从权重采样、缺环境 grounding 时产出似真而无据的 trajectory。


## 8.2 Carrier Utilization Profiles

利用画像刻画载体生产完成后如何进入决策循环。Schematic 与 Latent 在层内各有分化，且分化直接改变利用方式：Schematic 的 executable 形态经 executor 运行、结果再入 context（如 Voyager [Wan23c] 的 code skill），non-executable 形态直接注入 context（如 AriGraph [Ano24] 的 semantic triplet），两者在利用代价与延迟敏感性上截然不同；Latent 的 session-scoped 形态无训练成本、仅 session 内有效（如 LAG [Che25b] 的 KV cache），trained 形态跨 session 可复用但需训练、占虚拟 token 位（如 MAP-VLA [Li25g] 的 soft prompt）。利用分析因此落在 Narrative、Schematic（exec / non-exec）、Latent（session / trained）、Policy、Evaluator 七个单元上，这些区分在 §8.3 的约束压力表中吃重。

沿四个维度展开。Access Interface（D1）：经验从哪个通道进入决策循环。Access Granularity（D2）：能否在推理时有选择地激活特定经验，还是整个载体始终全开。Utilization Cost（D3）：使用经验需支付什么资源、计算发生在何处。Revisability（D4）：经验有误时如何修正，修正是否波及其他经验。

可解释性与控制自由度都是访问粒度的下游读数。可读性随粒度与层次走——Tokenized 因逐条可寻址加离散符号而可读，Parametric 因不可寻址加连续权重而不可读；控制自由度同样系于粒度——逐条可寻址允许在检索、编排、注入各环节调节，不可寻址则不允许。二者作为任务约束的对偶留待 §8.3。

| Carrier (subclass) | Access Interface | Access Granularity | Utilization Cost (计算位置) | Revisability |
|---|---|---|---|---|
| Narrative | context injection（$c_t$） | per-item（精确取单条 reflection/rule） | retrieval latency + context tokens·每次复用均付（GPU prefill + 外部检索） | append/edit/delete·逐条互不影响 |
| Schematic — executable | external execution → 产物入 $c_t$ | per-skill | execution compute·卸至外部 executor·通常同步阻塞 | version/replace·需重测 |
| Schematic — non-executable | context injection（$c_t$） | per-item / per-node | context tokens（GPU prefill） | version/replace |
| Latent — session-scoped | forward-pass attention（$c_t$） | per-session（整段·粗） | 无独立检索/编码开销·融入 forward pass（GPU） | session 结束自动失效 |
| Latent — trained | forward-pass attention（$c_t$） | per-bank | 占虚拟 token 位的 attention/KV·与 bank 长度成正比·非零（GPU） | 改训练数据·重训整个 bank |
| Policy | forward-pass weights（$\theta$） | indivisible / always-on（全局生效，不可取单条） | 零边际（每单位经验）·仍付完整 forward pass（GPU） | retrain·可能 catastrophic forgetting |
| Evaluator | selection signal: score/rank/reward（$v_\phi$） | per-evaluator（选哪个 + 信号注入点 + outcome/step 粒度）·内部不可分 | 额外 forward pass·offline 可摊销 / realtime gate 纯增量 | retrain·可能破坏校准 |

**Table 8.2.** Carrier utilization profiles across four dimensions.

访问接口由存在层次锁死：Tokenized 走 context injection，Policy 走 forward-pass weights，Evaluator 走 selection signal——选定载体即锁定接口，没有"选载体而不选接口"的余地。访问粒度随经验融合而变粗：Tokenized 的产物逐条可寻址——取单条 reflection、node 或单个 skill；Latent 只能整块取用，per-session 或 per-bank；Policy 不可寻址、全局生效。可寻址到何种单元由访问机制决定，而非仅由载体层次。Evaluator 是这条趋势的例外——存储同样融合，却经选择通道保留 per-evaluator 的可选择性，这源于选择通道的可拆卸调制：信号可从 decode 引导、rerank、best-of-N、RL reward、数据筛选等位置进入，粒度从 outcome 级到 step 级。以 PRM [Lig23] 为例，同一套 step-level score 既能作 PPO 的 dense reward，又能作 Best-of-N 的 step 级筛选或 tree search 的剪枝准则——与 Policy 的不可寻址、全局生效形成载体层最尖锐的利用不对称。代价一侧，"零边际"只对 Policy 的每单位经验成立、且仍付完整 forward pass；trained-Latent 的 per-use 成本非零——soft prompt 占虚拟 token 位、开销随 bank 长度线性增长——零边际与零成本不可混。

## 8.3 Constraint-Driven Pathway Selection

载体的可行性由部署约束界定。延迟预算、可解释要求、修正频率、训练资源可得性各为一类载体划出可行边界；这些约束都是 §8.1 生产 facet 或 §8.2 利用 facet 的对偶——约束为对应 facet 设定阈值，载体能否进入决策循环，取决于其取值是否满足。约束相容时逐一剪枝即可定位可行载体；约束冲突时单载体无解，迫使载体在时间或空间上组合。约束还会被误判、随部署漂移，使最优配置成为时间的函数。

### 8.3.1 约束到载体的方向性压力

任务约束沿四个轴展开，§8.1、§8.2 的九个 facet 在 Table 8.3 中各有归属。多数是轴的对偶——任务为该 facet 设阈值，载体取值是否过阈决定可行：复用代价对偶 Utilization Cost，可检视性对偶 Access Granularity、Output Verifiability 与 Information Transformation 的 traceability 分量，可变更性对偶 Revisability 与 Incrementality，构建代价对偶 Construction Cost。轴内子约束彼此独立、却可共享或多重映射同侧 facet——可检视性下的强可解释与安全关键同属一轴，前者落 Access Granularity 与 traceability、后者落 Output Verifiability；可变更性下的快可修正与高环境变动同涉 Revisability，后者另涉 Incrementality。经验体量与到达速度不单占一轴，只放大其余各轴的压力。

另两个 facet 与相邻代价并列，但由载体选择锁死、非任务所能设定：Access Interface 决定 Utilization Cost 表现为何种开销（context token、零边际、额外 forward pass），Mechanism（转化是否更新权重）决定 Construction Cost 的量级（gradient 训练贵、inference 廉）。Information Transformation 进入对偶的只有 traceability；其保真度一支——by-design 损失随 separability，by-limitation 的 reward hacking、欠拟合与 injection 的 hallucination——是转化过程而非载体的属性，归 §8.1，不左右载体选择。

| 约束轴 | 子约束 | 利用侧 facet（§8.2） | 生产侧 facet（§8.1） |
|---|---|---|---|
| 复用代价 | 低延迟 / context 紧 | Utilization Cost、Access Interface | — |
| 可检视性 | 强可解释 / 安全关键 | Access Granularity | Output Verifiability、Information Transformation |
| 可变更性 | 快可修正 / 高环境变动 | Revisability | Incrementality |
| 构建代价 | 训练资源紧 | — | Construction Cost、Mechanism |
| 规模 | 大体量 / 到达速度（调节量） | 放大各轴 | 放大各轴 |

**Table 8.3.** Four constraint axes, their sub-dimensions, and the §8.1/§8.2 facets each engages.

将每个子约束沿其对偶 facet 推至五类载体，得方向性压力表（Table 8.4）。↑↑ 强 toward，↑ toward，○ 中性，↓ against，↓↓ 强 against；Schematic 双值为 executable / non-executable，Latent 双值为 session-scoped / trained，单值表两形态一致，Evaluator 的 realtime / offline 另注。每格为结构性推断。

| 约束轴 | 子约束 | Narrative | Schematic | Latent | Policy | Evaluator |
|---|---|---|---|---|---|---|
| 复用代价 | 低延迟 | ↓↓ | ↓ | ↑/○ | ↑↑ | ↓(realtime)/○(offline) |
| 复用代价 | context 紧 | ↓↓ | ○/↓ | ↑ | ↑↑ | ○ |
| 可检视性 | 强可解释 | ↑↑ | ↑/↑↑ | ↓ | ↓↓ | ↓ |
| 可检视性 | 安全关键 | ↑↑ | ↑↑ | ↓ | ↓↓ | ↑ |
| 可变更性 | 快可修正 | ↑↑ | ↑ | ↓ | ↓↓ | ↓↓ |
| 可变更性 | 高环境变动 | ↑ | ↓/↑ | ↑/↓ | ↓↓ | ↓↓ |
| 构建代价 | 训练资源紧 | ↑↑ | ↑ | ↑↑/↓ | ↓↓ | ↓↓ |
| 规模 | 大体量 | ↓ | ↑/↓ | ↓ | ↑↑ | ↑ |

**Table 8.4.** Directional pressure from constraint sub-dimensions to carrier classes.

**复用代价。** 复用代价分时间与空间两面，区别在该代价随每次复用重新产生、还是一次性摊销。Narrative 在两面均产生代价、且随每次复用重新产生：条目须检索并 prefill 进 context，prefill 时间随条目数线性增长，context 占用随经验库累积而上升 [Shi23b, Zha23c]。Schematic 在两面分裂——executable 将计算卸至外部 executor、不占 context，但执行同步阻塞决策；non-executable 仍注入 context。Latent 不占 token 位、融入 forward pass 而无独立检索步骤；其中 trained 形态将 prefix K/V 拼入 attention，开销随 bank 长度增加，bank 较短时可忽略、较长时显著 [Gup26]。Policy 的边际复用成本为零，权重常驻、无额外检索或执行。Evaluator 的额外 forward pass 不占 context，作实时 gate 时为纯增量延迟、仅作离线筛选时可摊销 [Ses24]。

**可检视性。** 两类约束分别要求能否逐条阅读、能否在使用前客观验证，二者在 Schematic 与 Evaluator 上分岔。Narrative 逐条可读，两类俱强 [Zha23c]。Schematic 分形态：non-executable 的图结构可读性最高 [Ano24]，executable 的程序需技术能力方能阅读，但其执行可在落库前客观测试 [Wan23c]——可读性较低而可验证性较强。Latent 与 Policy 既不可读也无法事前验证，区别在于 Policy 的不可寻址更彻底。Evaluator 在两类间分野：作为融合权重内部不可拆分、难以逐条阅读，却能在已知 ground truth 的 hold-out 上做 calibration check，是唯一支持事前验证的融合载体，而 hold-out 无法穷尽输入空间。

**可变更性。** 两类约束分别要求修正已知错误的速度、跟随环境漂移的能力。Narrative 逐条独立，单条修正不触发全局重写，新增条目即时可被检索 [Zha23c]。Schematic 在跟随面分形态：executable 可独立版本控制但需重测，且对环境 interface 敏感，接口变动使既有 skill 失效 [Wan23c]，non-executable 的图结构可局部更新。Latent 两面俱弱于 Tokenized——均不可逐条修正，跟随面则 session-scoped 因每会话重建而无 staleness [Che25b]、trained 须重训整个 bank。Policy 的修正需 retrain 并可能引发 catastrophic forgetting；其在线更新以近端经验覆盖旧经验、旧经验效用随之衰减 [Bai24]。Evaluator 与 Policy 同处融合端，修正侧的融合约束未被选择通道绕过。

**构建代价。** 构建代价由转化是否更新权重决定，其资源含算力与标注两类。gradient-free 的转化——P1、P2 与 P3 的 cache 子类——在预算受限时仍可执行，不付训练成本；gradient-based 的转化——P3 的 trained 子类与 P4、P5、P6——需完整训练循环，预算不足时不可行，Latent 在此沿 cache 与 trained 分化最明显。算力与标注可分别稀缺：纯环境可验证信号（unit test、ground-truth match）驱动的 Policy RL 不需人工标注，而依赖人类示范或偏好标签的 SFT 与 reward modeling 在标注稀缺时受限更重。

**规模。** 经验体量是放大其余各轴的调节量，本身不构成独立轴。其最直接的对偶是 Policy 推理成本与训练数据体量解耦、训练完成后保持恒定 [Pan24]。Narrative 的检索质量随经验库增大而下降 [Fu24]。Schematic 分形态：executable 各自独立执行、不随体量变化，但库增大后 skill selection 的召回精度下降、独立执行的优势可能被抵消 [Wan23c]，non-executable 的图检索同样引入 noise。Latent 整块取用，体量增大后难以定位所需片段。Evaluator 的离线评分可随体量摊销。

各约束的强度须从任务场景读出，而非先验假定。硬约束直接排除不满足的载体——错误不可逆的安全关键场景排除 Policy 与 Latent（产物无法事前验证），监管强制可解释同理，硬实时要求排除 Narrative 与 executable Schematic；剪枝等价于在存在层次 × subclass 平面上切除不可行区。余下载体由多约束的合力定位：同向约束叠加为 overdetermined 的稳健推荐——低延迟、大体量与低可解释需求三重指向 Policy，单一约束放松仍不改结论；反向约束形成张力（§8.3.2），单载体无解、迫使组合（§8.3.3）。


### 8.3.2 约束张力与载体组合

两个强约束的对偶各拉向 separable↔fused 谱两端时，无单一载体同时满足——这是核心命题的直接推论，谱上不存在同处两端的点。Table 8.5 的四对张力是两个 amortization-pulling 轴（复用代价、规模，偏 fused）与两个 separability-pulling 轴（可检视性、可变更性，偏 separable）的两两组合，穷尽二者交叉。构建代价虽也限制可达载体——预算紧时只能用 gradient-free 的 Tokenized 端——但其约束是经济性的：预算充足即可构建 Policy、张力随之消失，这与 separable↔fused 上无论多少资源都无解的结构性对立不同，故不计入此处的张力。

| 张力对（轴级） | 冲突 | 结构性无解之由 |
|---|---|---|
| 复用代价 × 可检视性 | 低延迟偏 Policy（快但不透明），强可解释偏 Narrative（透明但慢） | 透明需可分离单元（每次重读），零边际需融合（不可读） |
| 规模 × 可检视性 | 大体量偏 Policy（可 scale 不可读），强可解释偏 Narrative（可读但受 context 上限制约） | 大体量受 context window 物理上限限制，与逐条可读不可兼得 |
| 复用代价 × 可变更性 | 低延迟偏 Policy（O(1) 推理），高环境变动偏 Narrative（可逐条增改） | 频繁更新需可分离单元，零边际需融合 |
| 规模 × 可变更性 | 大体量偏 Policy（训后恒定），快可修正偏 Narrative（逐条独立修正） | 大体量下逐条修正人力不可承受，重训周期又过长 |

**Table 8.5.** Irreducible tension pairs (axis-level) and their structural origin.

四对张力覆盖部署中最常见的约束冲突，每对都使单载体方案不可行，普适最优载体因此不存在。竞争约束使载体组合从可选项变为必需项——把拉向两端的约束分配给不同载体、再让它们协同。组合在结构上有三种方式，各自对应 §7 已建立的一个 composition pattern，衔接机制的细节属 §7。

**并行互补。** 两个载体同时参与同一决策，各守一侧约束。Evaluator–Policy Co-Evolution（§7.1）是典型：Policy 以零边际承担实时决策、满足复用代价，Evaluator 在其候选输出上施加 selection 信号、补足 Policy 无法自查的质量控制。UI-Genie [Xia25e] 让 reward model 与 policy 交替更新，高分行为回流为监督；Self-Guide [Wan26aj] 把二者压进同一组参数，每步的 verbal self-guidance 既导引推理又充当训练奖励。这一模式让两端载体并置、各守一侧，绕开单载体两端不可兼得的限制。

**时序分阶段。** 经验在时间维度上迁移载体——早期停留于 separable 端、晚期结晶到 fused 端，两端优势在不同阶段分别取得，由此缓解可变更性与复用代价、规模之间的张力：修正发生在 separable 阶段，摊销来自 fused 阶段。Refinement-Mediated Policy Internalization（§7.2）是直接对应：经验先以 Narrative 形态积累、逐条可读可修，质量达标后内化进 Policy 获零边际推理。Agent-R [Yua25c] 定位失败轨迹的错误步、修正后以 SFT 内化，Skill-SD [Wan26al] 把 Narrative 阶段抽象的 skill 蒸馏进不依赖 skill 的权重。Generative Experience Curation（§7.3）的自生成环 Policy → Tokenized → Policy 把这一结构闭合，经验在重新内化前经 Tokenized 中转被验证、筛选、修正，使 fused 端的 Policy 也能跟随环境更新。前提是经验在 separable 阶段已被充分校验，否则固化进权重的可能是误判的伪规则。

**分层分流。** 按决策的难度或重要性把请求分流到不同载体：高频常规请求由快载体处理，疑难或高风险者升级到可检视、可验证的载体。Evaluator 在此充当 router，判定 Policy 的决策何时需要升级，自身不直接出决策。PRM [Lig23] 对中间步骤打分、低分触发复核或更保守的策略，WebRL [Qi24] 的 outcome reward model 判定失败 trajectory、将其回收再利用而非直接丢弃。

载体组合确定后，对每个目标载体回查 §8.1 检验生产路径的可负担性：Narrative 经 P1（低成本、可增量），Schematic 经 P2（需 inference 加 execution verification、要求 interface 相对稳定），Latent 经 P3（cache-based 无训练成本但不跨 session、trained 需训练），Evaluator 经 P4。目标为 Policy 时存在 P5 与 P6 之分——P5 从 trajectory 直训（如 SWE-Gym [Pan24]），P6 经 Evaluator 信号训练（如 Constitutional AI [Bai22b] 的 RL-CAI），后者需先有 Evaluator、却能学到 trajectory-only 无法提供的细粒度偏好，二者代价画像见 §8.1。若目标载体在利用侧完美匹配约束、唯一生产路径却在生产侧代价不可承受，此困境指向 §9。


### 8.3.3 约束的时变与失配

在固定时点上，约束界定可行载体（§8.3.1、§8.3.2）；约束本身则随部署漂移，使一个一度可行的配置滑出可行域，经退化的检索、失效的 skill 或过时的权重传导为更差的 $a_t$。

约束的时间导数有三个常见来源。经验体量单调增长：系统初期经验少，Narrative store 检索精度高、context 开销小（Reflexion [Shi23b] 的 always-on prepend 在经验少时完全可行），P1 充分；积累至百万条后检索质量下降、context 紧张（ExpeL [Zha23c] 的 insight store 随使用增长面临检索精度与 context 占用的双重压力），需向 Policy 迁移（P5 或 P6）。任务分布漂移——GUI agent 的目标网站改版、工具 API 废弃——使已有 Schematic artifact 与训练好的 Policy 同时 stale（Voyager [Wan23c] 的 code skill 在 Minecraft 版本更新后须重新生成、验证）。安全要求升级——从无监管到强制可审计——使 Policy 从可行变为不可行。

最优载体配置因此是时间的函数。迁移本身是一条有完整生产画像的 pathway，以一次性训练成本换取迁移后更低的稳态利用成本。迁移过早，源载体尚未积累足够且经校验的经验，训出的 Policy 欠拟合、切换后 $a_t$ 质量不升反降；迁移过晚，漂移中的载体持续抬高利用成本、并经退化的检索拖低 $a_t$。迁移时机因此是决策质量与成本的联合优化。在此视角下，§7 的复合路径获得时序读法——Refinement-Mediated Policy Internalization（§7.2）编排的正是经验在不同载体间的停留时间：先在 Narrative 中积累到量且质量达标，再固化进 Policy。

约束漂移留下的失配在文献中已有独立印证。经验体量增长引发的 Narrative 检索退化即 memory bloat，Darwinian Memory [Mi26b] 以 survival-based pruning 直接回应。安全要求升级使 Latent 失效尤其难补救：§7.4 已指出 Latent"缺少让外部模块插入评估或修复的接口，一旦写错便难在闭环里被发现"，这也解释了 Latent 为何几乎不进入 §7 composite 的中间环节。可经迁移修复的失配对应一条有代价但可执行的路径；经验一旦融入权重或连续向量、无法单独提取，则修复无路，每条这样的不可逆失配对应一个 §9 问题。


## 8.4 The Structural Origin and Generative Power

§8.1–§8.3 的分析共同指向一个结论：载体的生产代价、利用画像与约束压力分布，共同取决于其在 separable↔fused 谱上的位置，叠加两个 subclass 分叉的修正——formalization 定验证模式，functional role 定通道与 pathway 拓扑位。这不是五类载体的经验归纳，而是从 §2 的存在层次分类和决策规则出发的结构推论。

该归约赋予框架生成性。任一新转化技术可先在 §2 的层次结构中定位源端与目标端——这一定位即足以推断其生产机制的大致类型（inference-based 还是 training-based）、信息损失的性质（by-design 还是 by-limitation 主导）、利用侧的代价结构与访问粒度区间。分析涵盖尚未出现的形式，而不止于已有的七条路径与五个载体类别。

框架同时生成否定性预测。声称"既快又透明"的单载体方案等价于声称存在同处 separable 与 fused 两端的载体，与核心命题矛盾。若此类系统在实践中被报告，它要么实际上维护了 Tokenized 副本供审计（那是两套载体，不是一套），要么"透明"指某种近似解释（probing、attribution）而非真正的逐单元可读。这一否定性预测使框架可证伪——发现一个真正在融合存储下同时具备 per-item 可读性与零边际推理成本的载体，即构成对核心命题的反驳。

<!--
§8.4↔§9 前向引用去重（待 §9 成稿后定夺）：以下"三个结构性待解问题"原在 §8.4 收尾完整展开，与 §9（Open Problems and Future Directions）存在跨章重复风险，暂注释，使 §8.4 收束于 falsifiability 论断。§9 成稿后二选一：(a) §9 完整展开、§8.4 仅留一句 crisp 指引收尾；(b) §8.4 展开、§9 回指。
注意：上一轮已将"在线迁移时机无自动系统"这一 open problem 从 §8.3.3 结尾移入此处第三问，故该问题目前仅存于本注释，§9 须接手，否则全文将缺失这一 open problem。
原文备查：
三个结构性待解问题构成 §9 的核心。第一，separability–amortization 耦合是信息论硬约束还是当前架构的软约束？Sparse feature、可编辑 parametric memory、adapter、retrieval-over-activations 等方向都在试探这一边界——它们不同程度地在融合存储中引入可选择性，但尚未在任何工作中实现 Policy 的逐单元可读与可修正。第二，Evaluator 通过选择通道实现的部分解耦能否推广至生成端？当前 Evaluator 的粒度来自后置于输出分布的调制——生成端不存在对等的后置机制。若能在 Policy 的前向传播中引入类似的"可拆卸调制步骤"——如可控的 activation gating 或 token-level routing——则可能在融合存储下实现选择性调取。第三，最优配置随时间变化时，何种机制可在线判定迁移时机并自动重排经验在各载体间的分布？§8.3.3 已将迁移形式化为收益–成本问题，但社区尚无系统能自动执行这一判断——它需要同时监控检索退化速率、训练成本估算与任务分布 drift 检测，是一个跨越经验管理全链路的元控制问题。
-->