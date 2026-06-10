# 8. Pathway-Level Analysis

§3–§7 按转化路径逐一梳理了社区将 agent experience 从一种载体重新表示为另一种载体的机制。本章横向比较这些路径与它们产出的载体：每条 pathway 在生产侧付出什么，每类 carrier 在利用侧表现如何，任务约束如何在二者之间做出选择。

§2.1 将 agent 决策写为 $a_t \sim \pi_\theta(\cdot \mid c_t)$，经验影响决策只有两条途径——流经 $c_t$ 的外部信息，或固化在 $\theta$ 的内部能力。§2.3 据此将载体沿 $c_t \to \theta$ 的存在形态切分为 Tokenized → Latent → Parametric 连续谱：输入侧的离散 token、输入侧的连续向量、权重内的隐式表示。本章的分析站在这一前提上展开，不再重述其推导。

§8.1 以五个维度刻画每条 pathway 的生产画像，§8.2 以四个维度刻画每类 carrier 的利用画像，§8.3 将任务约束读为这两组维度的对偶——分析约束如何剪除不可行载体、约束冲突时如何迫使载体组合、约束随部署漂移时最优配置如何随之改变。

## 8.1 Pathway Production Profiles

本节以五个维度刻画每条 pathway 的生产画像。Production Mechanism（D1）：转化靠什么计算机制执行，如 LLM inference、gradient-based training、gradient-free persistence、execution + verification loop。Construction Cost（D2）：转化消耗多少计算与人力。Information Transformation（D3）：经验信息在转化中被保留、损失、注入了什么，以及能否被追溯（traceability）；其中 loss 区分 lossy-by-design（抽象/压缩必然丢弃细节，损失类别可控）与 lossy-by-limitation（欠拟合、reward hacking、采样偏差，损失类别不可控，属工程风险而非设计意图）。Incrementality（D4）：新经验持续到来时，转化能否增量执行。Output Verifiability（D5）：转化产物能否在不依赖下游任务表现的情况下被独立验证。


| Pathway                          | Mechanism                                | Construction Cost            | Information Transformation                                                        | Incrementality                             | Output Verifiability                   | 代表工作 / 详节                                            |
| -------------------------------- | ---------------------------------------- | ---------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------ | -------------------------------------- | ---------------------------------------------------- |
| P1 Narrative Abstraction         | LLM inference                            | 低·可全自动                       | **保留**: 模式与洞察 / **损失**: 步骤与时序(by-design) / **注入**: 跨轨迹综合 insight(源自模型先验)          | 增量(append); dynamic store 有 merge/prune 级联 | 直接阅读判断(主观)                             | Reflexion [Shi23b]；§3.1                              |
| P2 Schematic Formalization       | LLM inference + 可选 execution 验证          | 中·需可执行环境                     | **保留**: 过程结构 / **损失**: NL nuance/隐含假设(by-design) / **注入**: 显式依赖结构                 | 增量(新 artifact 入库)                          | execution test(客观, coverage-limited)   | Voyager [Wan23c]；§3.2                                |
| P3 Latent-Space Transformation   | cache: gradient-free / trained: gradient | cache 低·仅 session; trained 中 | **保留**: 计算状态 / **损失**: 符号可读性(by-design) / **注入**: token 未显式编码的统计规律                | cache 即时重建; trained 需 batch 重训             | 无直接验证·仅 ablation 间接                    | LAG [Che25b]（cache）/ ReasonCACHE [Gup26]（trained）；§4 |
| P4 Evaluator Internalization     | gradient training                        | 高·需标注或明确成败信号                 | **保留**: 评估偏好 / **损失**: 校准来源与单条贡献(mix: by-design + by-limitation)                  | batch 重训; 新标注需重训以保校准                       | 无直接验证·hold-out calibration check       | Let's Verify Step by Step [Lig23]；§5.1               |
| P5 Policy Internalization        | gradient training (SFT/RL)               | 高·需大规模高质量 trajectory         | **保留**: 决策模式 / **损失**: 单条贡献不可区分(by-design) + 欠拟合/reward hacking 风险(by-limitation) | batch 重训(可热启动); RL 可在线但漂移衰减旧经验             | 仅 behavioral (rollout 间接比较)            | SWE-Gym [Pan24]；§5.2                                 |
| P6 Evaluator-Driven Optimization | gradient training (RLHF/DPO)             | 高·叠加 P4 成本                   | **保留**: 偏好迁移入 policy / **注入**: trajectory-only 学不到的细粒度偏好 / **损失**: 经 P4+P6 双重压缩   | online/iterative·漂移敏感                      | behavioral·循环验证风险 (Evaluator ⇄ Policy) | Constitutional AI [Bai22b]；§6.1                      |
| P7 Parametric Externalization    | 从 policy 采样生成                            | 中·依赖采样质量·须先有 trained policy  | **保留**: 权重中的能力经采样部分恢复为 token / **损失**: 采样未覆盖部分 / **注入**: hallucination 风险         | 可增量生成新样本·跟随源模型更新                           | 产物可读但不可追溯权重成分·完备性不可验证                  | Explorer [Pah25]；§6.2                                |


**Table 8.1.** Pathway production profiles across five dimensions.

**Production Mechanism** 把七条路径沿是否更新权重切成两组。P1、P2、P3 的 cache 子类与 P7 不更新权重——P1、P2 靠 LLM inference，P3-cache 靠 gradient-free 的前向状态留存，P7 靠从已训练模型采样；P3 的 trained 子类与 P4、P5、P6 经 gradient training，需数据筹备与优化的整套机制，单步资源消耗高于一次 inference。P2 在 inference 之外可叠加 execution + verification loop，是不更新权重一侧唯一带客观产出闸门的机制。

**Construction Cost** 在 gradient 一类整体高、inference 一类整体低。P4 卡在标注或明确成败信号的获取，P5 卡在大规模高质量 trajectory，P6 在 P4 的 Evaluator 训练之上再叠一层、成本累加。P1 可全自动、近零成本，P3-cache 极低但仅 session 内有效，P2 中等、需可执行环境；P7 受制于采样质量，且须先有 trained policy——它的低成本只就外化这一步而言，不含上游训练。

**Information Transformation** 的关键分野在 loss 的两种性质。七条路径注入的新信息都来自转化模型的先验、而非源经验——抽象不增加 Shannon 信息量。P1（丢步骤与时序）、P2（丢 NL nuance 与隐含假设）、P3（丢符号可读性）的损失均为 lossy-by-design，损失类别可控、由抽象策略调节；P4、P5 在 by-design 之外混入 lossy-by-limitation——P4 的标注噪声与标注者不一致直接进权重，P5 的 SFT 欠拟合与 RL reward hacking 不可控，属工程风险而非设计意图；P6 的损失是 P4 阶段与 P6 阶段的双重压缩，原始经验语义到达后已不可辨识；P7 的损失来自采样未覆盖的部分，并注入 hallucination 风险。traceability 沿 P3 → P4 → P5(→ P6) 单调下跌：P3-cache 的 KV 直接来自真实前向传播、能对应具体历史片段，P3-trained 的 soft prompt 已无法对应回单条经验，P4/P5/P6 把单条贡献经 batch 梯度平均进权重、无法追问某个决策用了训练集中哪条轨迹；P7 从另一侧失效——产物虽是 Tokenized 端的离散 token，却采样自 Parametric 权重、追不到源知识。这道下跌是 batch 梯度平均的结构性后果，与工程精度无关。

**Incrementality** 在 inference 一类天然增量——P1 append、P2 新 artifact 入库、P3-cache 即时重建、P7 随源模型更新持续生成新样本；gradient 一类须 batch 重训，P3-trained 改训练数据即重训整个 bank、P4 的新标注需重训以保校准。P5 可热启动、RL 还能在线更新，但旧经验的效用随分布漂移衰减，在线性以遗忘旧经验为代价；P6 的 online/iterative 更新同样对漂移敏感。P1 一侧的 dynamic store 在 append 之外带 merge/prune 级联，单条写入可能触发已有条目的连带改写。

**Output Verifiability** 不沿 Tokenized → Latent → Parametric 谱递减，取决于产物容许哪种独立检验。P2 的 code skill 由环境 execution 给出客观二值信号（如 Voyager 的 verification gate，通过/失败可判定，但测试完备性无法保证、未覆盖的 corner case 仍可能失败），P1 的 reflection 只能靠人或强 LLM 主观阅读、两审阅者可能给出不同结论——同处 Tokenized 端却分居客观与主观，决定 verifiability 的是检验类型而非载体位置。向 Parametric 端，P4 的 Evaluator 尚可用 hold-out calibration 间接核验，P3、P5、P6 退到只能借 rollout 或 ablation 推断，P7 又从另一侧受限：产物虽可读，却追不到采样自哪部分权重、完备性不可验证。

几个结构事实不落在任何单一维度上。P6 与 P7 都以已固化的 Parametric 经验为源、做第二步加工，方向相反、在 pathway 图中互补：P6 把 Evaluator 的判断进一步写入 Policy 权重、深入 Parametric 端，P7 把 Policy 或 Evaluator 的能力采样回 Tokenized、退出 Parametric 端，使权重中的隐式经验重新成为可供其他路径使用的显式载体。Policy 由 P5、P6 两条路径产生，二者代价画像不同，使 §8.3 对 Policy 目标的可行性判断成为 P5 还是 P6 的选择、而非二元判断；多生产路径并非 Policy 独有——Narrative 既可由 P1 同层精炼、也可由 P7 从权重外化。循环验证与 hallucination 是仅现于转化过程的两类风险：前者来自 P6 中 Evaluator 与 Policy 互为参照、缺独立外部 ground truth（ECHO [Li26l] 的同步更新可缓解、不能消除），后者来自 P7 从权重采样、缺环境 grounding 时产出似真而无据的 trajectory。

## 8.2 Carrier Utilization Profiles

利用画像刻画载体生产完成后如何进入决策循环，落在 §2.3 的五类载体上。载体的进入方式由其存在形态决定，与生产它的路径无关：Latent 向量无论来自 cache 留存还是训练所得模块，都作为连续向量参与 forward pass；Schematic artifact 无论是 code、workflow 还是 graph，都是 $c_t$ 中的强形式化离散 token、靠结构被操作（parse、execution 或 traversal），其中 code-skill 形态把执行卸至外部 executor。这些层内差异改变具体单元格的取值（利用代价、修正方式），但不改变载体的可寻址性与访问粒度，记为单元格内限定，不另立载体。

沿四个维度展开。Access Interface（D1）：经验从 $c_t$ 还是 $\theta$ 进入决策循环。Access Granularity（D2）：能否在推理时有选择地激活特定经验，还是整个载体始终全开。Utilization Cost（D3）：使用经验需支付什么资源、计算发生在何处。Revisability（D4）：经验有误时如何修正，修正是否波及其他经验。

可解释性与控制自由度都是访问粒度的下游读数。可读性随粒度与层次走——Tokenized 因逐条可寻址加离散符号而可读，Parametric 因不可寻址加连续权重而不可读；控制自由度同样系于粒度——逐条可寻址允许在检索、编排、注入各环节调节，不可寻址则不允许。二者作为任务约束的对偶留待 §8.3。


| Carrier   | Access Interface                                                      | Access Granularity                  | Utilization Cost（计算位置）                                                             | Revisability                                  |
| --------- | --------------------------------------------------------------------- | ----------------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------- |
| Narrative | context injection（$c_t$）                                              | per-item（精确取单条 reflection/rule）     | retrieval latency + context tokens·每次复用均付（GPU prefill + 外部检索）                      | append/edit/delete·逐条互不影响                     |
| Schematic | context injection（$c_t$）；executable 形态经 external execution 后结果回 $c_t$ | per-item / per-node                 | context tokens（GPU prefill）；executable 形态叠加 execution compute·卸至外部 executor·通常同步阻塞 | version/replace（executable 需重测）               |
| Latent    | forward-pass attention（输入侧·连续向量·不占 token 位）                           | per-block（整段·粗）                     | 无独立检索/编码开销·融入 forward pass（GPU）；trained 形态占虚拟 token 位·与 bank 长度成正比·非零              | 不可逐条（session-scoped 自动失效 / trained 重训整个 bank） |
| Policy    | forward-pass weights（$\theta$）→ $a_t$                                 | indivisible / always-on（全局生效·不可取单条） | 零边际（每单位经验）·仍付完整 forward pass（GPU）                                                  | retrain·可能 catastrophic forgetting            |
| Evaluator | forward-pass weights（$\theta$）→ 候选信号                                  | indivisible / always-on             | 零边际（每单位经验）·额外 forward pass·offline 可摊销 / realtime gate 纯增量                         | retrain·可能破坏校准                                |


**Table 8.2.** Carrier utilization profiles across four dimensions.

访问接口由存在形态锁定：Tokenized 走 context injection（$c_t$），Latent 走 forward-pass attention（仍在输入侧，但以连续向量参与、不占 token 位、不进权重），Parametric 走 forward-pass weights（$\theta$）——选定载体即锁定接口。访问粒度沿 Tokenized → Latent → Parametric 单调变粗：Tokenized 逐条可寻址（per-item，取单条 reflection、node 或 skill），Latent 只能整块取用（per-block），Parametric 不可寻址、全局生效，无例外。

层内的两个分叉不改变这条单调性，各自只动一两个维度。Tokenized 内，Narrative 与 Schematic 同处 per-item、同样可读，差别仅在复用机制——Narrative 靠 language understanding 阅读，Schematic 靠 parse、execution 或 graph traversal 按结构操作；这一差别落在 Output Verifiability（§8.1）与利用延迟（executable Schematic 的执行同步阻塞），不动可寻址性。Parametric 内，Policy 与 Evaluator 共享同一份存储画像——都不可寻址、都 retrain 才能改、复用都零边际——差别纯在功能角色：Policy 的 forward pass 直接产 $a_t$，Evaluator 的产一个关于候选的信号，可被训练消费（→ Evaluator-Driven Optimization）或推理消费（对 $\pi_\theta$ 候选 rerank、Best-of-N 筛选、tree search 剪枝）。以 PRM [Lig23] 为例，同一套 step-level score 既能作 RL 的 dense reward，又能作 Best-of-N 的 step 级筛选或 tree search 的剪枝准则——这种下游灵活是"评估型输出可被多处取用"的性质，选哪个 evaluator、信号注入到哪个环节、取 outcome 还是 step 粒度，是把功能模块接入决策环的编排（属 §7），不是 Evaluator 的存储比 Policy 更可寻址。

复用代价这一维上，Tokenized 与 Parametric 两端的取值互斥、无法兼得：逐条可寻址要求经验以相互独立的符号存储，每次复用重新载入 context；零边际要求经验存进权重，复用不重载却无法单取一条。Latent 居中——不占 token 位省去重载，却也整块取用、无法逐条取出。"零边际"只对 Policy/Evaluator 的每单位经验成立、且仍付一次完整 forward pass，与 trained-Latent 占虚拟 token 位、随 bank 长度线性增长的非零 per-use 成本不可混。

## 8.3 Constraint-Driven Pathway Selection

载体的可行性由部署约束界定。延迟预算、可解释要求、修正频率、训练资源可得性各为一类载体划出可行边界；这些约束都是 §8.1 生产维度或 §8.2 利用维度的对偶——约束为对应维度设定阈值，载体能否进入决策循环，取决于其取值是否满足。约束相容时逐一剪枝即可定位可行载体；约束冲突时单载体无解，迫使载体在时间或空间上组合。约束还会被误判、随部署漂移，使最优配置成为时间的函数。

### 8.3.1 约束到载体的方向性压力

任务约束沿四个轴展开，§8.1、§8.2 的维度各有归属。多数是维度的对偶——任务为该维度设阈值，载体取值是否过阈决定可行：Serving Cost 对偶 Utilization Cost，Maintainability 对偶 Revisability 与 Incrementality，Build Cost 对偶 Construction Cost。Inspectability 一轴含两个性质不同的子约束：readability 要求逐条可读，对偶 Access Granularity 与 traceability，随载体在谱上的位置走；verifiability 要求使用前可客观验证，对偶 Output Verifiability，由载体的复用机制设定（Schematic 经 execution、Evaluator 经 calibration），与谱上位置无关。两个子约束在 Schematic 与 Evaluator 上反向，须分列。Scale 不单占独立一轴：其 volume 与 arrival rate 只放大其余各轴的压力，arrival rate 的对偶与 non-stationarity 同落 Incrementality。

另两个维度与相邻代价并列，但由载体选择锁死、非任务所能设定：Access Interface 决定 Utilization Cost 表现为何种开销（context token、零边际、额外 forward pass），Mechanism（转化是否更新权重）决定 Construction Cost 的量级（gradient 训练贵、inference 廉）。Information Transformation 进入对偶的只有 traceability；其保真度一支——by-design 损失随存在层次，by-limitation 的 reward hacking、欠拟合与 hallucination——是转化过程的工程结果，任务不对其设阈，不构成载体选择的约束，归 §8.1。


| 约束轴            | 子约束                                 | 利用侧维度（§8.2）                       | 生产侧维度（§8.1）                              |
| -------------- | ----------------------------------- | --------------------------------- | ---------------------------------------- |
| Serving Cost   | latency / context budget            | Utilization Cost、Access Interface | —                                        |
| Inspectability | readability                         | Access Granularity                | Information Transformation（traceability） |
| Inspectability | verifiability                       | —                                 | Output Verifiability                     |
| Inspectability | error correction / non-stationarity | Revisability                      | Incrementality                           |
| Build Cost     | training resources                  | —                                 | Construction Cost、Mechanism              |
| Scale（放大轴）     | volume / arrival rate               | 放大各轴                              | 放大各轴                                     |


**Table 8.3.** Constraint axes, their sub-constraints, and the §8.1/§8.2 dimensions each engages.

将每个子约束沿其对偶维度推至五类载体，得方向性压力表（Table 8.4）。`++` 强烈偏向，`+` 偏向，`○` 中性，`−` 不利，`−−` 强烈不利，指载体在该约束下的适配度。各子约束取该量处于约束状态的场景——latency、context budget、training resources 指该资源紧张，余项指其需求为高；Schematic 双值为 executable / non-executable 形态，Latent 双值为 session-scoped / trained 形态，单值表两形态一致，Evaluator 的 realtime / offline 另注。每格为结构性推断。


| 约束轴             | 子约束                | Narrative | Schematic | Latent | Policy | Evaluator              |
| --------------- | ------------------ | --------- | --------- | ------ | ------ | ---------------------- |
| Serving Cost    | latency            | −−        | −         | +/○    | ++     | −(realtime)/○(offline) |
| Serving Cost    | context budget     | −−        | ○/−       | +      | ++     | ○                      |
| Inspectability  | readability        | ++        | +/++      | −      | −−     | −                      |
| Inspectability  | verifiability      | ++        | ++        | −      | −−     | +                      |
| Maintainability | error correction   | ++        | +         | −      | −−     | −−                     |
| Maintainability | non-stationarity   | +         | −/+       | +/−    | −−     | −−                     |
| Build Cost      | training resources | ++        | +         | ++/−   | −−     | −−                     |


**Table 8.4.** Directional pressure from constraint sub-dimensions to carrier classes.

**Serving Cost。** 分时间与空间两面，区别在该代价随每次复用重新产生、还是一次性摊销。Narrative 两面均付、且每次复用重付：条目须检索并 prefill 进 context，prefill 时间随条目数线性增长 [Shi23b, Zha23c]。Schematic 分形态——executable 将计算卸至外部 executor、不占 context，但执行同步阻塞决策；non-executable 仍注入 context。Latent 不占 token 位、无独立检索步骤，其中 trained 形态将 prefix K/V 拼入 attention，开销随 bank 长度增加，bank 较短可忽略、较长显著 [Gup26]。Policy 边际复用成本为零，权重常驻。Evaluator 的额外 forward pass 不占 context，作实时 gate 时为纯增量延迟、仅作离线筛选时可摊销 [Ses24]。

**Inspectability。** readability 与 verifiability 在 Schematic 与 Evaluator 上分岔：前者要逐条可读，后者要使用前可验证。Narrative 逐条可读、可主观核验，两者俱强 [Zha23c]。Schematic 分形态：non-executable 的图结构可读性最高 [Ano24]；executable 的程序需技术能力方能阅读、可读性较低，但其执行可在落库前客观测试 [Wan23c]——这是可验证性的来源，与可读性反向。Latent 与 Policy 既不可读也无法事前验证，Policy 的不可寻址更彻底。Evaluator 作为 Parametric 权重不可逐条阅读，却能在已知 ground truth 的 hold-out 上做 calibration check，是唯一支持事前验证的 Parametric 载体，而 hold-out 无法穷尽输入空间——可验证而不可读，恰是两个子约束在它身上反向的实证。

**Maintainability。** error correction 是修正已知错误的速度，non-stationarity 是跟随漂移的能力。Narrative 逐条独立，单条修正不触发全局重写，新增条目即时可检索 [Zha23c]。Schematic 在跟随面分形态：executable 可独立版本控制但需重测，且对环境 interface 敏感、接口变动使既有 skill 失效 [Wan23c]，non-executable 的图结构可局部更新。Latent 两面俱弱于 Tokenized——均不可逐条修正，session-scoped 因每会话重建而无 staleness [Che25b]、trained 须重训整个 bank。Policy 的修正需 retrain 并可能引发 catastrophic forgetting，其在线更新以近端经验覆盖旧经验、旧经验效用随之衰减 [Bai24]。Evaluator 与 Policy 同处 Parametric 端，修正侧的约束一致。

**Build Cost。** 由转化是否更新权重决定，资源含算力与标注两类。gradient-free 的转化——P1、P2 与 P3 的 cache 子类——预算受限时仍可执行，不付训练成本；gradient-based 的转化——P3 的 trained 子类与 P4、P5、P6——需完整训练循环，预算不足时不可行，Latent 在此沿 cache 与 trained 分化最明显。算力与标注可分别稀缺：纯环境可验证信号（unit test、ground-truth match）驱动的 Policy RL 不需人工标注，而依赖人类示范或偏好标签的 SFT 与 reward modeling 在标注稀缺时受限更重。

**Scale。** 经验体量放大其余各轴的压力，本身不构成独立轴，故不单列压力行。放大集中在谱的两端：Narrative 的检索质量随经验库增大而下降 [Fu24]、Latent 整块取用使体量增大后更难定位所需片段，Tokenized 端本就要逐次重载的利用成本被进一步抬高；Policy 推理成本与训练数据体量解耦、训练完成后保持恒定 [Pan24]，Evaluator 的离线评分可随体量摊销，Parametric 端的零边际优势随体量放大。Schematic 居中分形态：executable 各自独立执行、执行成本不随体量变化，但库增大后 skill selection 的召回精度下降，与 non-executable 的图检索 noise 同源——执行可扩、选择不可扩。

各约束的强度须从任务场景读出，而非先验假定。硬约束直接排除不满足的载体——错误不可逆的安全关键场景排除 Policy 与 Latent（产物无法事前验证），监管强制可解释同理，硬实时要求排除 Narrative 与 executable Schematic；剪枝在载体空间上切除不可行区。余下载体由多约束的合力定位：同向约束叠加为 overdetermined 的稳健推荐——低延迟、大体量与低可解释需求三重指向 Policy，单一约束放松仍不改结论；反向约束形成张力、单载体无解、迫使组合（§8.3.2），约束随部署漂移则使配置随时间变化（§8.3.3）。

### 8.3.2 约束张力与载体组合

两个强约束各把载体推向存在形态谱的相反两端时，单载体无解——谱上没有同处两端的点（§8.2）。推向 Parametric 端（零边际、与体量解耦）的是 Serving Cost 与 Scale，推向 Tokenized 端（逐条可读、逐条可改）的是 readability 与 Maintainability，两两交叉即 Table 8.5 的四对；Inspectability 只取 readability 入对——其另一半 verifiability 不沿谱排布、由复用机制设定（§8.3.1）。


| 张力对                            | 冲突                                                                      | 结构性无解之由                                        |
| ------------------------------ | ----------------------------------------------------------------------- | ---------------------------------------------- |
| Serving Cost × readability     | latency 偏 Policy（快但不可读），readability 偏 Narrative（可读但慢）                   | 逐条可读须在 Tokenized 端、每次重载，零边际须在 Parametric 端、不可读 |
| Scale × readability            | volume 偏 Policy（可 scale 不可读），readability 偏 Narrative（可读但受 context 上限制约） | volume 增大受 context window 物理上限制约，与逐条可读不可兼得     |
| Serving Cost × Maintainability | latency 偏 Policy（O(1) 推理），non-stationarity 偏 Narrative（可逐条增改）           | 逐条可改须在 Tokenized 端，零边际须在 Parametric 端          |
| Scale × Maintainability        | volume 偏 Policy（训后恒定），error correction 偏 Narrative（逐条独立修正）              | volume 大时逐条修正人力不可承受，重训周期又过长                    |


**Table 8.5.** Irreducible tension pairs and their structural origin.

四对张力覆盖部署中最常见的约束冲突，每对都使单载体方案不可行。把拉向两端的约束分配给不同载体、再让它们协同，是唯一出路；分配可在时间或空间上进行——时序迁移对应 §7.2、§7.3，空间并置对应 §7.1，衔接机制的细节属 §7。

**时序分阶段。** 经验沿时间迁移载体——早期停留于 Tokenized 端、晚期结晶到 Parametric 端，Table 8.5 的四对张力由此化解：修正与逐条审查发生在 Tokenized 阶段，摊销与可扩展性来自 Parametric 阶段。前提是两端的需求可在时间上分离、而非须同时满足。Refinement-Mediated Policy Internalization（§7.2）直接对应——经验先以 Narrative 形态积累、逐条可读可修，质量达标后内化进 Policy 获零边际推理（Agent-R [Yua25c] 定位失败轨迹的错误步、修正后以 SFT 内化；Skill-SD [Wan26al] 把 Narrative 阶段抽象的 skill 蒸馏进不依赖 skill 的权重）。Generative Experience Curation（§7.3）的自生成环 Policy → Tokenized → Policy 把这一结构闭合：经验在重新内化前经 Tokenized 中转被验证、筛选、修正，使 Parametric 端的 Policy 也能跟随环境更新。两个 pattern 都落在时序分阶段；若 Tokenized 阶段校验不足，固化进权重的可能是误判的伪规则。

**并行互补。** 两个载体同时参与同一决策、各守一侧，处理无法在时间上分离的冲突。典型是同时要求快速决策与质量把关：Policy 以零边际承担实时决策、满足 Serving Cost，另一载体在其候选输出上施加质量控制。Evaluator–Policy Co-Evolution（§7.1）是此类（UI-Genie [Xia25e] 让 reward model 与 policy 交替更新、高分行为回流为监督；Self-Guide [Wan26aj] 把二者压进同一组参数，verbal self-guidance 既导引推理又充当训练奖励）。Evaluator 补足的是 verifiability 而非 readability——它本身也是 Parametric 权重、不可逐条阅读，故 §7.1 化解的是 Serving Cost 与 verifiability 的冲突，不是 Table 8.5 的 readability 张力；readability 张力若须同时满足，只能并行维护一份可读的 Tokenized 副本供审计，那是两套载体并置，单载体仍无法两端兼得。

载体组合确定后，对每个目标载体回查 §8.1 检验生产路径的可负担性：Narrative 经 P1（低成本、可增量），Schematic 经 P2（需 inference 加 execution verification、要求 interface 相对稳定），Latent 经 P3（cache-based 无训练成本但不跨 session、trained 需训练），Evaluator 经 P4。目标为 Policy 时存在 P5 与 P6 之分——P5 从 trajectory 直训（如 SWE-Gym [Pan24]），P6 经 Evaluator 信号训练（如 Constitutional AI [Bai22b] 的 RL-CAI），后者需先有 Evaluator、却能学到 trajectory-only 无法提供的细粒度偏好，二者代价画像见 §8.1。若目标载体在利用侧完美匹配约束、唯一生产路径却在生产侧代价不可承受，此困境指向 §9。

### 8.3.3 约束的时变与失配

在固定时点上，约束界定可行载体（§8.3.1、§8.3.2）；约束本身则随部署漂移，使一个一度可行的配置滑出可行域，经退化的检索、失效的 skill 或过时的权重传导为更差的 $a_t$。

约束随时间变化有三个常见来源。经验体量单调增长：系统初期经验少，Narrative store 检索精度高、context 开销小（Reflexion [Shi23b] 的 always-on prepend 在经验少时完全可行），P1 充分；积累至百万条后检索质量下降、context 占用升高（ExpeL [Zha23c] 的 insight store 随使用增长面临检索精度与 context 占用的双重压力），需向 Policy 迁移（P5 或 P6）。任务分布漂移——GUI agent 的目标网站改版、工具 API 废弃——使已有 Schematic artifact 与训练好的 Policy 同时 stale（Voyager [Wan23c] 的 code skill 在 Minecraft 版本更新后须重新生成、验证）。安全要求升级——从无监管到强制可审计——使 Policy 从可行变为不可行。

最优载体配置因此是时间的函数。迁移本身是一条有完整生产画像的 pathway，以一次性训练成本换取迁移后更低的稳态利用成本。迁移过早，源载体尚未积累足够且经校验的经验，训出的 Policy 欠拟合、切换后 $a_t$ 质量不升反降；迁移过晚，漂移中的载体持续抬高利用成本、并经退化的检索拖低 $a_t$。迁移时机因此是决策质量与成本的联合优化。在此视角下，§7 的复合路径获得时序读法——Refinement-Mediated Policy Internalization（§7.2）编排的正是经验在不同载体间的停留时间：先在 Narrative 中积累到量且质量达标，再固化进 Policy。

约束漂移留下的失配在文献中已有独立印证。经验体量增长引发的 Narrative 检索退化即 memory bloat，Darwinian Memory [Mi26b] 以 survival-based pruning 直接回应。安全要求升级使 Latent 失效尤其难补救：§7.4 已指出 Latent“缺少让外部模块插入评估或修复的接口，一旦写错便难在闭环里被发现”，这也解释了 Latent 为何几乎不进入 §7 composite 的中间环节。可经迁移修复的失配对应一条有代价但可执行的路径；经验一旦融入权重或连续向量、无法单独提取，则修复无路，每条这样的不可逆失配对应一个 §9 问题。