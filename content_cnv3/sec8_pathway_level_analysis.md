# 8. Pathway-Level Analysis

§3–§7 按转化路径逐一梳理了社区将 agent experience 从一种载体重新表示为另一种载体的机制。每条路径在生产代价、利用代价与可修订性上呈现不同画像。本章要回答的是：这些画像能否归约为一个共同的结构性决定量，以及在任务约束下该决定量如何左右载体与路径的选择。

§2.1 将 agent 决策写为 $a_t \sim \pi_\theta(\cdot \mid c_t)$，决策依据分置于两处：流经 $c_t$ 的外部信息，与固化在 $\theta$ 中的内部能力。当考虑作用在 $\pi_\theta$ 候选输出上的 selection 算子时，经验影响 $a_t$ 的位置穷举为三处：$c_t$（输入通道）、$\theta$（参数通道）、以及评估信号 $v_\phi$ 对候选分布的后置调制（选择通道）。§2.3 将经验载体沿 Tokenized → Latent → Parametric 连续谱分类。**载体在谱上的位置锁定了它通过哪个通道进入决策循环**——Tokenized 走输入通道（离散 token 注入 context），Latent 走输入通道（连续向量注入 attention，不占 token 位），Policy 走参数通道（权重恒在，前向传播自动激活），Evaluator 走选择通道（对候选输出施加 score/rank/reward 信号）。通道决定利用代价、访问粒度与可修订性。

三者的统一根源是 **separability–amortization trade-off**。Tokenized 载体在模型外部以离散 token 序列存在（§2.3.2），每条 reflection、每条 rule 是独立寻址的单元，可逐条编辑，但每次复用都须重新载入 context。Parametric 载体在模型内部以连续权重存在，复用时无须额外载入，每单位经验的边际利用成本趋零，却无法在推理时单独取用某一条。两者互斥的根源是同一选择：单元可分离要求经验以相互独立的符号结构存储，摊销要求经验以相互交融的数值分布存储。不存在同处两端的载体。

<!-- 移除：原 §8 引入段第 4 段（subclass 分叉预览）。
内容已在下游展开：§8.1（验证模式，G1 段 + 表 8.1）、§8.2（Evaluator 访问粒度例外与信号注入点，表 8.2 结论）、§8.4（thesis 综合 + §9 open problem，§8.4 开篇与第二个 open problem）。
因与下游重复而从引入段移除，原文存档如下：

两个 subclass 分叉不沿谱移动载体位置，但在各自层内产生关键分化。Tokenized 层内的 formalization 分叉（Narrative / Schematic）改变验证模式：Narrative 靠语言理解消费，验证是主观的"读"——覆盖"说得对不对"，盲区是"说得好但做不到"；Schematic 靠 parsing/execution 消费，验证是客观的"跑"——覆盖"跑不跑得通"，盲区是"跑得通但方向错"。两者同为高可验证性，但是类别差异而非程度差异。Parametric 层内的 functional-role 分叉（Policy / Evaluator）改变经验进入决策的通道与载体在 pathway 图中的拓扑位置：Policy 走参数通道，产生动作，动作产生新 trajectory 可被任何以 Tokenized 为源的路径消费——它是 pathway 图的枢纽节点，通过 P7 外化与 P5 内化形成闭环；Evaluator 走选择通道，产生评估信号，评估信号的语义是"对行为的判断"，唯一有意义的消费方是行为生产者 Policy——它是 pathway 图的汇节点，只有出边 P6。Evaluator 同时构成 separability–amortization 单调性的结构性例外：Policy 与 Evaluator 同处融合端（存储上不可分），但 Evaluator 保留了 Policy 不具备的访问粒度——可选择用哪个评估器、信号从 decode 引导/rerank/best-of-N/RL reward 哪个点进入、outcome 级还是 step 级评分。该粒度不来自存储形式（存储仍是 fused），而来自选择通道的后置调制特性——评估信号独立于参数通道，是可拆卸的调制步骤。核心命题的单调性因此限定于输入通道与参数通道；选择通道的部分解耦能否推广至生成端，是 §9 的核心 open problem。
-->

§8.1–§8.3 沿三侧展开：§8.1 以 pathway 为索引刻画生产代价与信息转换，§8.2 以 carrier 为索引刻画利用代价与粒度，§8.3 将任务约束读为前两者的对偶以界定可行解。§8.4 讨论该归约的结构起源与生成性。

## 8.1 Pathway Production Profiles

Pathway comparison 的分析对象是转化操作本身的结构特性，而非 §2.3 刻画的载体静态属性。本节以五个维度刻画每条 pathway 的生产画像。Production Mechanism（D1）：转化靠什么计算机制执行，如 LLM inference、gradient-based training、gradient-free persistence、execution + verification loop。Construction Cost（D2）：转化消耗多少计算与人力。Information Transformation（D3）：经验信息在转化中被保留、损失、注入了什么，以及能否被追溯（traceability）；其中 loss 区分 lossy-by-design（抽象/压缩必然丢弃细节，损失类别可控）与 lossy-by-limitation（欠拟合、reward hacking、采样偏差，损失类别不可控，属工程风险而非设计意图）。Incrementality（D4）：新经验持续到来时，转化能否增量执行。Output Verifiability（D5）：转化产物能否在不依赖下游任务表现的情况下被独立验证。

**G1 同层精炼（P1, P2）。** 源与目标同处 Tokenized 端，转化靠 LLM inference，产物保持可读性，可增量。P1（Narrative Abstraction）执行语义抽象：Reflexion [Shi23b] 在每次 trial 结束后依据失败轨迹与环境反馈生成简短 reflection，将错误归因写入下一轮 prompt；ExpeL [Zha23c] 从成功轨迹池与失败-成功对中抽取可迁移 insight，对已有条目执行 add、edit、upvote、downvote；AutoGuide [Fu24] 从同一任务的优劣轨迹对中定位首次决策分叉点，抽出 when-context then-action 形式的 guideline。P1 保留的是源 trajectory 中跨任务可迁移的模式与因果关联，损失的是具体步骤与时序细节——这是 lossy-by-design，损失类别可控，抽象程度由 prompt 设计与归纳策略调节。P2（Schematic Formalization）执行结构形式化：Voyager [Wan23c] 通过 iterative prompting 反复生成、执行、修正 action program，只有经环境反馈与 self-verification 验证通过的程序才以 JavaScript program 形式写入 skill library；AWM [Wan24] 从 web agent 经验中抽取 recurring sub-routine，产物是含环境描述、推理与动作程序的 workflow trajectory；AriGraph [Ano24] 把每步交互转为 semantic triplet 并在新旧单元间建立关系，构建可遍历的 episodic-semantic 双图。P2 保留的是过程结构与动作序列，损失的是自然语言中的隐含假设与情境 nuance——同样属 lossy-by-design，但注入的显式依赖结构（类型约束、控制流、节点关系）使产物可通过 parser 或 executor 机制性消费，而非依赖语言理解的语义推断。

P1 与 P2 的对比焦点在 information transformation 的性质差异。两者注入的新信息均来自执行转化模型的先验而非源经验本身——抽象不增加 Shannon 信息量。但两者损失的类别不同：P1 损失时序信息（一条 reflection "在执行 A 之前必须先检查 B"省略了发现这一规则的具体失败过程），P2 损失软信息（workflow 中 "navigate to login page" 不编码 login page 在不同网站上的视觉差异）。损失的对称后果是验证模式的根本分化：P1 靠"读"——生成的 reflection 可被人类或强 LLM 直接阅读判断语义正确性，验证是主观的，两个审阅者可能判断不同；P2 靠"跑"——生成的 code skill 可在环境中执行，通过/失败是客观的二值信号（Voyager 的 execution verification gate），但测试完备性无法保证——一个通过所有现有测试的 skill 可能在未覆盖的 corner case 中失败。

**G2 跨层内化（P3, P4, P5）。** 自 Tokenized 跨至 Latent/Parametric，除 P3 的 cache 子类外均经 gradient-based training，可读性骤降，增量性受限。三者沿压缩程度与不可追溯性递增排列。

P3（Latent-Space Transformation）保留的是模型处理经验时的内部计算状态，是 G2 中最轻量的转化。Cache-based 子类不需要训练：Memorizing Transformers [Wu22] 将先前 token 在中间层的 key-value 对写入外部 memory，后续时间步通过 kNN 检索接入 attention；LAG [Che25b] 对历史推理日志做完整前向传播，只为选中的少量 token 持久化 KV，推理时检索相关日志并将其 KV 注入当前推理；TempoFit [Sun26] 在 VLA 上将早先时间步的 layer-wise KV 注入当前 attention，支撑 long-horizon episode 内的历史继承。Cache-based 方法成本极低——本质是存储成本加一次前向传播——但产物仅 session 内有效，不跨 session 泛化。Trained 子类需训练但跨 session 可复用：MAP-VLA [Li25g] 把 expert demonstrations 按任务阶段切分，为每阶段训练一组 soft prompt；ReasonCACHE [Gup26] 把大规模 reasoning demonstrations 编码为各层可训练的 prefix K/V。P3 的损失是符号可读性的丧失——连续向量无法逐元素对应回源 token——这是 lossy-by-design，压缩必然牺牲可读性。注入的是 token 未显式编码的统计规律：模型在处理某段 trajectory 时某个 attention head 持续关注某个 token 位置，这种模式不来自 trajectory 的显式内容。

P4（Evaluator Internalization）将交互经验固化为判断函数。监督粒度分 outcome 与 process 两支。Outcome 支将完整 trajectory 映射为评价标签：WebRL [Qi24] 训练 outcome reward model 依据指令、历史动作与页面状态判定 web trajectory 是否完成任务；GenRM [Zha24o] 把 reward modeling 写成 next-token prediction，有直出 Yes/No 的变体与先生成 CoT rationale 再判的变体。Process 支将监督信号分配到中间步骤：Let's Verify Step by Step [Lig23] 在 PRM800K 上用人工 step-level 标签训练 PRM，对每一步预测 positive/negative/neutral；OmegaPRM [Luo24] 用 MCTS 与 binary search 自动定位 first error，以 Monte Carlo 估计替代人工标注。P4 的损失含两类：by-design（评估偏好被压缩进权重，校准来源与单条贡献不可追溯）与 by-limitation（标注噪声、标注者不一致直接进入 Evaluator 权重，难以事后检测）。P4 的产物专化且终端化——Evaluator 在 pathway 图中只有出边 P6，一旦经验到达 Evaluator，它唯一的下游消费方式是进入 Policy（见 §8.3.4）。

P5（Policy Internalization）将交互经验固化为决策能力。SFT 变体以成功 trajectory 为监督做 behavior cloning：[Pat24] 让 web agent 在 WebArena 中自生成 action-observation trajectories，以环境报错与 self-critique 滤出可信动作做 autoregressive SFT；SWE-Gym [Pan24] 以可执行 unit test 判定 patch trajectory 成败后做 rejection-sampling fine-tuning。RL 变体以环境可验证信号为 reward 直接优化 policy：DigiRL [Bai24] 在真实移动端用 Gemini 做二值评估，以任务级 curriculum 与步级 doubly-robust 筛选选出最值得学的任务与动作。P5 的损失分两类：by-design——单条经验对权重的贡献被 batch 梯度累积淹没，不可区分解构；by-limitation——SFT 欠拟合可能导致某些行为模式完全未被学习，RL reward hacking 可能导致 policy 学会最大化 reward signal 的捷径而非真正提升任务性能。后者是工程风险而非设计意图，但后果同样严重——policy 在训练分布外可能系统性失效。

G2 内部的关键梯度是 traceability 沿 P3 → P4 → P5 单调下跌。P3 cache-based 的 KV 直接来自真实前向传播，能对应到具体历史片段；P3 trained 的 soft prompt 已无法对应回单条经验；P4 和 P5 更甚——权重更新是 batch 梯度累积的结果，无法追问"这个决策用了训练集中的哪条轨迹"。这不是工程精度的限制，是 batch training 的结构性限制。

**G3 以 Parametric 为源（P6, P7）。** 两者的共性是"用已有隐式经验做第二件事"，方向相反，在 pathway 图中的 composability 角色互补。

P6（Evaluator-Driven Optimization）将已内化的评估能力转为 Policy 更新的监督，方向是进一步深入融合端。按评估器信号进入 policy 的方式分三支。Reward Maximization 将标量分数当 reward 做 RL 最大化：Constitutional AI [Bai22b] 的 RL-CAI 阶段由 AI judge 对完整回答给偏好，训练出 preference model 后经 RLAIF 让 policy 最大化其分数；OAIF [Guo24] 让在线 LLM annotator 对当前 policy 采样出的回答对给偏好，直接进 DPO/IPO/SLiC，使监督分布始终跟随 policy。Preference Contrast 让评估器的 chosen/rejected 偏好直接驱动对比式优化：Self-Rewarding Language Models [Yua24] 让同一模型既作 generator 又作 judge，自评分构造 chosen/rejected 对后以 iterative DPO 回灌。Reward-Ranked Selection 只将评估器分数用于筛选样本，再以 SFT 写入 policy：RAFT [Don23] 用 RM 对同一 prompt 的多条回答打分，保留 best-of-K 做 SFT；BOND [Ses24] 将整个 best-of-N 分布蒸馏进单次采样 policy。P6 的信息损失是双重重压缩——第一重是 P4 阶段从 trajectory 到 Evaluator 的压缩，第二重是 P6 阶段从 Evaluator 信号到 Policy 权重的压缩。双重重压缩后，原始 trajectory 中的经验语义已不可辨识。P6 面临循环验证风险：用 Evaluator 评分来训练 Policy，再用 Policy 的表现来验证 Evaluator 的质量——两个评估互相参照，没有独立的外部 ground truth。ECHO [Li26l] 的 critic 与 actor 同步更新是试图缓解这一依赖的实例，但无法消除。

P7（Parametric Externalization）将权重中的隐式能力经采样恢复为显式 token，方向是退出融合端。Demonstration Externalization 外化 Policy 的决策行为：Explorer [Pah25] 用 GPT-4o 在真实网页中自主发现任务、执行多步交互，经多阶段 refine 与 verifier 产出带页面状态与动作序列的 multimodal trajectory；OS-Genesis [Sun24b] 让 agent 在 GUI 环境中做交互式遍历，从观察到的功能反向合成高层任务并执行得到完整轨迹，由 trajectory reward model 按完成度与连贯性打分后按分采样进训练集；AgentTrek [Xu24] 把网页教程标准化为结构化任务规格后驱动 agent 在真实页面复现，再由 VLM 校验指令遵循与目标完成。Evaluative Supervision Externalization 外化 Evaluator 的判断能力：[He25g] 先用强 computer-use agent 产出 noisy trajectory，再由 o4-mini 对每步做 correctness 与 optimality grading，产物被物化为 WebSTAR（训练 student agent）与 WebSCORE（蒸馏轻量 StepRM）两套独立数据。P7 的根本局限在于采样——能从权重中提取的只是权重所编码知识的一个样本，不是知识的全部。不同的采样策略（温度、prompt、任务分布）产生不同的外化结果，不存在"完备外化"。P7 引入 hallucination 风险：Policy 权重的采样噪声可能被当作知识外化，产生源权重中并不构成"知识"但外化后表现得像是经验的 trajectory——这是仅现于过程层的风险，§2 的载体静态分类无法识别。

表 8.1 汇总了七条路径在五个维度上的对比。表中单元格填写的是 structural constraint，不是 literature count。以 P1 的 Incrementality 为例，"增量（append）"对应 Static Store 类方法（如 Reflexion），"增量含 merge/prune 级联"对应 Dynamic Store 类方法（如 ExpeL）——读者若需了解具体方法归属，回查 §3.1。

| Pathway | Mechanism | Construction Cost | Information Transformation | Incrementality | Output Verifiability |
|---|---|---|---|---|---|
| P1 Narrative Abstraction | LLM inference | 低·可全自动 | **保留**: 模式与洞察 / **损失**: 步骤与时序(by-design) / **注入**: 跨轨迹综合 insight(源自模型先验) | 增量(append); dynamic store 有 merge/prune 级联 | 直接阅读判断(主观) |
| P2 Schematic Formalization | LLM inference + 可选 execution 验证 | 中·需可执行环境 | **保留**: 过程结构 / **损失**: NL nuance/隐含假设(by-design) / **注入**: 显式依赖结构 | 增量(新 artifact 入库) | execution test(客观, coverage-limited) |
| P3 Latent-Space Transformation | cache: gradient-free / trained: gradient | cache 低·仅 session; trained 中 | **保留**: 计算状态 / **损失**: 符号可读性(by-design) / **注入**: token 未显式编码的统计规律 | cache 即时重建; trained 需 batch 重训 | 无直接验证·仅 ablation 间接 |
| P4 Evaluator Internalization | gradient training | 高·需标注或明确成败信号 | **保留**: 评估偏好 / **损失**: 校准来源与单条贡献(mix: by-design + by-limitation) | batch 重训; 新标注需重训以保校准 | 无直接验证·hold-out calibration check |
| P5 Policy Internalization | gradient training (SFT/RL) | 高·需大规模高质量 trajectory | **保留**: 决策模式 / **损失**: 单条贡献不可区分(by-design) + 欠拟合/reward hacking 风险(by-limitation) | batch 重训(可热启动); RL 可在线但漂移衰减旧经验 | 仅 behavioral (rollout 间接比较) |
| P6 Evaluator-Driven Optimization | gradient training (RLHF/DPO) | 高·叠加 P4 成本 | **保留**: 偏好迁移入 policy / **注入**: trajectory-only 学不到的细粒度偏好 / **损失**: 经 P4+P6 双重压缩 | online/iterative·漂移敏感 | behavioral·循环验证风险 (Evaluator ⇄ Policy) |
| P7 Parametric Externalization | 从 policy 采样生成 | 中·依赖采样质量·须先有 trained policy | **保留**: 权重中的能力经采样部分恢复为 token / **损失**: 采样未覆盖部分 / **注入**: hallucination 风险 | 可增量生成新样本·跟随源模型更新 | 产物可读但不可追溯权重成分·完备性不可验证 |

**Table 8.1.** Pathway production profiles across five dimensions.

表 8.1 给出四条跨路径的结构性结论。第一，mechanism 将七条路径二分为 inference-based（P1, P2）与 training-based（P3-P6），P7 居中（依赖采样而非训练，但须先有 trained policy）。这一边界对应基础设施需求的质变——仅需 API 访问 vs. 需 GPU 训练集群——是 pathway 选择的第一道硬过滤。第二，traceability 与 verifiability 沿 explicit → implicit 单调下跌，是 separability–amortization 在生产侧的投影。P1 的产物可直接阅读判断，P5 的产物只能通过 rollout 间接比较——两者之间横着一条"可用直接证据验证"与"只能靠间接行为推断"的分界线。第三，Policy 是唯一有两条生产路径的载体：P5 从 trajectory 直训（需大规模高质量数据），P6 经 Evaluator 信号训练（需先有 Evaluator，但可学到 trajectory-only 无法提供的细粒度偏好）。两者的代价画像不同，使 §8.3 的可行性步骤成为路径选择（P5 还是 P6）而非二元判断。第四，循环验证（P6）与 hallucination（P7）是仅现于过程层的风险——循环验证来自 Evaluator 与 Policy 在训练中互为参照而缺乏独立外部锚点，hallucination 来自采样的随机性——§2 的载体静态分类无法识别这两种风险。

## 8.2 Carrier Utilization Profiles

利用画像刻画载体生产完成后如何进入决策循环：经哪个通道、能否精确取用单条经验、每次使用付多少代价、经验有误时如何修正。§2.4 将 utilization 关切（检索策略、上下文编排、运行时维护、多载体协同）defer 到 §8——本节按载体兑现这一承诺。

分析的最小单元不是五个顶层 carrier 类别，而是七个（存在层次 × subclass 形态）单元。Schematic 分 executable 与 non-executable：Voyager [Wan23c] 的 code skill 走 external execution（产物经 executor 运行后结果入 context），AriGraph [Ano24] 的 semantic triplet 走 context injection（结构化文本直接注入 context）——两者在利用代价和延迟敏感性上截然不同。Latent 分 session-scoped 与 trained：LAG [Che25b] 的 KV cache 无训练成本但仅 session 内有效、session 结束自动失效，MAP-VLA [Li25g] 的 soft prompt 跨 session 可复用但需训练、且占虚拟 token 位。这些区分在 §8.3 的约束压力表中吃重。

四个分析维度。Access Interface（D1）：经验从架构的哪个通道进入决策循环——这是 §2.1 决策规则与 §2.3 存在层次分类的结构推论，不是设计选择。Access Granularity（D2）：能否在推理时有选择地激活特定经验，还是整个载体始终全开。Utilization Cost（D3）：使用经验需要支付什么资源，计算发生在哪里（GPU prefill / external executor / forward pass / extra forward pass）。Revisability（D4）：发现经验有误时如何修正，修正是否影响其他经验。

Interpretability 与 control freedom 不列为独立维度。前者是 access granularity 与存在层次位置的下游读数：Tokenized 可读是因为 per-item 粒度加离散符号，Parametric 不可读是因为 indivisible 加连续权重。后者同样是 granularity 的函数：per-item 粒度允许在检索、编排、注入各环节调节（Narrative 可调检索策略、top-k、排序、截断、prompt 格式），indivisible 则不允许。将二者单列将与 access granularity 重复。它们的分析位置在 §8.3，作为约束的对偶出现。

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

表 8.2 给出四条跨载体的结构性结论。第一，访问接口由存在层次锁死。Tokenized 必须走 context injection，Policy 必须走 forward-pass weights，Evaluator 必须走 selection signal。不存在"选载体但不选接口"的自由度——选载体同时锁定了怎么用。这是 utilization-driven selection 的硬约束层。第二，访问粒度沿 explicit → implicit 单调退化：per-item（Narrative, Schematic non-exec）→ per-skill（Schematic exec）→ per-session/bank（Latent）→ indivisible（Policy）。Evaluator 为例外——其 per-evaluator 粒度来自选择通道的后置调制特性，与存储融合解耦。第三，"零边际"仅对 Policy 的每单位经验成立，且仍付完整 forward pass。trained-Latent 的 per-use 成本亦非零——soft prompt 占用虚拟 token 位，开销随 bank 长度线性增长。zero marginal 与 zero cost 不可混用。第四，Evaluator 的信号注入点是利用侧独特的自由度：信号可从 decode 引导、rerank、best-of-N、RL reward、数据筛选等不同位置进入，粒度可从 outcome 级到 step 级。以 PRM [Lig23] 为例，其 step-level correctness score 可作为 PPO 的 dense reward（每步都收到信号）、Best-of-N 的 step-level filter（筛掉低分步）、或 tree search 的 pruning criterion（低分分支停止扩展）。这一自由度不来自存储（存储仍是 fused），而来自选择通道的可拆卸性——与 Policy 的 indivisible/always-on 形成载体层最尖锐的利用不对称性。

## 8.3 Constraint-Driven Pathway Selection

§8.1 与 §8.2 给出了供给侧两份画像。§8.3 做反向映射：将任务约束读为这两份画像的对偶，界定可行的载体与路径组合。§8.3 不引入新维度——若匹配中缺数据，补回 §8.1 或 §8.2。

### 8.3.1 约束作为供给 facet 的对偶

任务约束不是外生的四类分类——每个约束维度是供给侧特定 facet 的镜像。经验体量与到达速度不直接施压，而是放大下述某项约束的压力强度。

| 任务约束 | 对偶的供给/利用 facet | 数据来源 |
|---|---|---|
| 延迟上限 / context 容量 / compute budget / 单次成本上限 | Utilization Cost | §8.2 |
| 可解释性 / 审计要求 / 数据合规（如 PII 不入权重） | Access Granularity + 存在层次位置 | §8.2 |
| 可修正速度 / 环境变动频率 | Revisability + Incrementality | §8.2 + §8.1 |
| 训练资源可得性 / 标注可得性 | Construction Cost | §8.1 |
| 经验体量 / 到达速度 | （调节量——放大上述某项约束的压力强度） | — |

**Table 8.3.** Task constraints as duals of supply-side facets.

### 8.3.2 约束到载体的方向性压力

将每个约束沿其对偶 facet 推至七个载体单元，得方向性压力表（Table 8.4）。↑↑ 强 toward，↑ toward，○ 中性，↓ against，↓↓ 强 against。每格为结构性推断，以下逐格锚至文献。

| 约束 | Narrative | Schematic (exec) | Schematic (non-exec) | Latent (session) | Latent (trained) | Policy | Evaluator |
|---|---|---|---|---|---|---|---|
| 低延迟 | ↓↓ | ↓ | ↓ | ↑ | ○ | ↑↑ | ↓(realtime) / ○(offline) |
| context 紧 | ↓↓ | ○ | ↓ | ↑ | ↑ | ↑↑ | ○ |
| 大体量经验 | ↓ | ↑ | ↓ | ↓ | ↓ | ↑↑ | ↑ |
| 强可解释 | ↑↑ | ↑ | ↑↑ | ↓ | ↓ | ↓↓ | ↓ |
| 快可修正 | ↑↑ | ↑ | ↑ | ↓ | ↓ | ↓↓ | ↓↓ |
| 高环境变动 | ↑ | ↓ | ↑ | ↑ | ↓ | ↓↓ | ↓↓ |
| 安全关键(事前可验) | ↑↑ | ↑↑ | ↑↑ | ↓ | ↓ | ↓↓ | ↑ |

**Table 8.4.** Directional pressure from task constraints to carrier units.

**低延迟。** Narrative 的 retrieval latency + context prefill 直接叠加在决策延迟上。Reflexion [Shi23b] 的 always-on prepend 模式——每次推理都将 reflection 拼入 prompt——随 reflection 数量增长，prefill 时间线性增加。Schematic exec 的外部执行（Voyager [Wan23c] 的 Mineflayer program 在环境中运行）通常是同步阻塞的——agent 需要执行结果才能继续决策。Policy 的零边际推理成本直接支持低延迟：权重恒在，前向传播自动激活，无额外检索或执行步骤。Latent(session) 不增加独立检索步骤，attention integration 与 forward pass 融合，因此标 ↑。Latent(trained) 标 ○：ReasonCACHE [Gup26] 的 prefix K/V 需拼入 attention 字典，额外的 K/V 长度增加 attention 计算量，是否压过 token 检索+编码取决于 bank 长度——正文假设 bank 长度控制在 10-100 虚拟 token 量级时开销可忽略，超出此范围则降为 ↓。Evaluator 的额外 forward pass 增加延迟：作为 realtime gate（每步评估并决定是否 abort）是纯增量延迟，标 ↓；仅用于 offline best-of-N selection（如 BOND [Ses24] 的离线 best-of-N 蒸馏），延迟可摊销，标 ○。

**context 紧。** Narrative 直接竞争 context window——每条 reflection 消耗 token 预算，体量大时 top-k 检索被迫在覆盖率和精度之间取舍。ExpeL [Zha23c] 的 insight store 随使用增长，context 占用持续上升。Schematic exec 的产物不占 context（code skill 在外部 executor 运行，只有执行结果进 context），标 ○。Latent 不占 token 位，标 ↑。Policy 完全不占 context——经验在权重中——标 ↑↑。

**大体量经验。** Policy 的推理成本与训练数据体量解耦（O(1)）。SWE-Gym [Pan24] 的 rejection-sampling fine-tuning 需大规模 trajectory 做训练，但训后推理成本恒定。Narrative 的检索质量随 store 增大下降：AutoGuide [Fu24] 的 keyed lookup 依赖 context 匹配精度，store 增大后相似度阈值难以全局最优。Schematic exec 标 ↑：每个 skill 独立执行、不争 context，但 skill library 增大后 skill selection 变难——Voyager 的 skill library 随探索扩张，选择合适 skill 的 embedding similarity 召回精度随 library 增大下降。该标注带 †：若 skill selection 退化程度抵消独立执行优势，则降为 ○。

**强可解释。** Narrative 的可读性使每条 reflection、rule、guideline 都可被人类直接审查。ExpeL [Zha23c] 的 upvote/downvote 机制依赖经验的可读性——人类或 LLM 必须能阅读 insight 内容才能判断其质量。Schematic non-exec（如 AriGraph [Ano24] 的 semantic triplet）可读性高，标 ↑↑；Schematic exec（如 Voyager 的 JavaScript program）需技术能力阅读，标 ↑。Policy 完全不可解释——无法追问"这个决策用了训练集中的哪条轨迹"——标 ↓↓。

**快可修正。** Narrative 的逐条独立性使修正一条 reflection 不影响其他条目。ExpeL [Zha23c] 的 edit 操作可单独修改一条 insight，不触发全局重写。Schematic exec 的 skill 独立版本控制——修正一个 skill 重新测试后替换——但需重测，修正成本高于 Narrative。Policy 修正需 retrain，且可能 catastrophic forgetting。Evaluator 与 Policy 同处融合端，修正侧的融合存储约束未被选择通道绕过——标 ↓↓。

**高环境变动。** Narrative 可快速追加新经验：ExpeL [Zha23c] 的 add 操作即时生效，新经验立即可被检索。Schematic exec 对环境 interface 稳定性敏感——Voyager 的 Mineflayer program 依赖 Minecraft API，API 变动导致已有 skill 直接不可用。Latent(session)（如 LAG [Che25b] 的 KV cache）天然无 staleness——每次 session 重新产生，旧 session 自动失效。Policy 需重新训练以适应新分布：DigiRL [Bai24] 的 online RL 虽可持续更新，但旧经验的效用随分布漂移衰减——这不是真正适应，是遗忘旧经验、仅依赖近端经验。

**安全关键。** Narrative 使用前可阅读验证，Schematic 使用前可测试验证——两者均支持事前 gate。Voyager [Wan23c] 的 execution verification 恰是在 skill 入库前执行客观测试，不合格者不入库——这是安全关键场景的标准实践。Evaluator 标 ↑（弱于 Narrative 和 Schematic）：可做 calibration check（在已知 ground truth 的 hold-out set 上评估），但无法穷尽验证所有输入。Policy 和 Latent 标 ↓↓：无法事前验证——只能看 rollout 结果或 ablation 间接推断。

选择逻辑分五阶段。Phase 1（约束抽取）：从任务场景读出各约束维度的强度，而非先验假定。Phase 2（硬约束剪枝）：hard constraint 不满足直接排除载体——安全关键至错误不可逆则 Policy 与 Latent 出局（产物无法事前验证），监管强制可解释同理，硬实时（延迟 < 50ms）则 Narrative 与 Schematic-execution 出局。剪枝等价于在（存在层次 × subclass）平面上切除不可行区。Phase 3（多约束解析）：多约束同向时形成联盟，推荐 overdetermined——低延迟 + 大体量 + 低可解释需求 → 三重 toward Policy，即使某一约束后来放松，推荐依然稳健。多约束反向时形成张力（§8.3.3），单载体无解，需组合（§8.3.4）。

### 8.3.3 不可化约的张力

两个强约束的对偶各拉向 separable↔fused 谱两端时，无单一载体同时满足。这是核心命题的直接推论——谱上不存在同处两端的点。

| 张力对 | 冲突 | 结构性无解之由 |
|---|---|---|
| 低延迟 × 强可解释 | Policy 快但不透明，Narrative 透明但慢 | 透明需可分离单元（每次重读），零延迟需融合（不可读） |
| 大体量 × 强可解释 | Policy 可 scale 不可读，Narrative 可读不可 scale | 大体量下检索精度下降 + context 不足，问题不在检索质量，在 context window 的物理上限 |
| 高环境变动 × 低延迟 | 频繁更新偏 Narrative（可逐条修正），零边际偏 Policy（推理 O(1)） | 频繁更新需可分离单元，零边际需融合 |
| 快可修正 × 大体量 | 逐条修正不 scale（人力不可承受），retrain 太慢（周期过长） | 大体量下人力逐条修正不可承受，重训周期又过长——两头堵 |

**Table 8.5.** Irreducible tension pairs and their structural origin.

这些张力是 §8.3 的核心分析产出。它们解释了三项事实。第一，§7 的 composite pipelines 为部分缓解张力而存在——Refinement-Mediated Policy Internalization（§7.2）通过先让经验停留于 Narrative（可读、可修、即时可用）、积累至量且质量达标后固化进 Policy，缓解了"快可修正 × 大体量"的张力：修正发生在 Narrative 阶段（逐条可修），推理效率来自 Policy 阶段（零边际）。Generative Experience Curation（§7.3）的自生成环（Policy → Tokenized → Policy）则缓解了"高环境变动 × 低延迟"：Policy 提供低延迟推理，Tokenized 中转允许经验在重新内化前被验证、筛选、修正。第二，不存在普适最优载体——四种张力覆盖了实际部署中最常见的约束冲突，每种冲突都使单载体方案不可行。第三，§9 的 open problem 是如何动态调节载体组合以响应张力的时变——当前无系统能自动完成这一判断与切换。

### 8.3.4 载体组合模式

竞争约束使载体组合不是可选项而是必需项。§8.3 只回答"张力为何迫使组合"，组合的具体机制细节留在 §7。以下三种组合模式各自对应 §7 已建立的 composition pattern。

**并行互补。** 两个载体同时服务于同一决策，各自覆盖对方无法满足的约束。Evaluator–Policy Co-Evolution（§7.1）是典型实例：Policy 承担实时决策（满足低延迟），Evaluator 在 Policy 的候选输出上施加 selection 信号（满足质量控制）。UI-Genie [Xia25e] 的 reward model 与 policy 交替更新——policy 产生动作，reward model 打分筛选，高分行为回流为 policy 监督——正是这一模式的完整实现。Self-Guide [Wan26aj] 将其推到共享参数的极限：同一 agent 每步生成的 verbal self-guidance 既是推理时的 selection 信号、又是训练时的内部奖励，并行互补退化为单一模型内的双通道。

**时序分阶段。** 经验在时间维度上经历载体迁移：先以低成本载体快速可用，再逐步结晶为高效率载体。Refinement-Mediated Policy Internalization（§7.2）是这一模式的直接对应：Agent-R [Yua25c] 先让 actor 在 MCTS 搜索树中定位失败轨迹的首个错误步并插入修正信号（Narrative 阶段，可读可修），再以 SFT 将修正后的 trajectory 内化进参数（Policy 阶段，零边际推理）。Skill-SD [Wan26al] 进一步蒸馏：teacher 在 skill 引导下产生更优行为，student 在不接收 skill 的条件下通过 reverse-KL 学会复现——经验在 Narrative 阶段被抽象为 skill，再在 Policy 阶段被蒸馏为不依赖 skill 的权重。这一模式的前提是经验质量在 Narrative 阶段已被充分验证和修正，否则固化进权重的可能是被误判的伪规则。

**分层分流。** 按决策的重要性或难度将请求分流到不同载体。Evaluator 作为 safety gate 的模式散布在 §5.1 和 §6.1 中：PRM [Lig23] 对中间步骤输出 correctness score，低分步可触发人工复核或更保守的策略；WebRL [Qi24] 的 outcome reward model 对 trajectory 做终局判定，失败 trajectory 被回收到 Generative Experience Curation（§7.3）的筛选管线而非直接丢弃。这一模式的核心是 Evaluator 作为 router——不是替代 Policy 做决策，而是判定 Policy 的决策何时需要升级处理。

### 8.3.5 生产路径可行性

载体组合确定后，对每个目标载体回查 §8.1 检验生产路径的可负担性。目标 Narrative → P1（LLM inference，低成本、可增量），可行。目标 Schematic → P2（需 LLM inference + execution verification，如 Voyager [Wan23c] 的环境执行闭环），需 interface 相对稳定。目标 Latent(session) → P3 cache-based（无训练成本，但不跨 session）；目标 Latent(trained) → P3 trained（需训练）。目标 Policy → 路径选择：P5 从 trajectory 直训（如 SWE-Gym [Pan24] 的 rejection-sampling fine-tuning，需大规模高质量数据），还是 P6 经 Evaluator 信号训练（如 Constitutional AI [Bai22b] 的 RL-CAI，需先有 Evaluator，但可学到 trajectory-only 无法提供的细粒度偏好）？两者的代价画像已在 §8.1 中给出——这是 §8.1 读数 (iii) 的直接应用。目标 Evaluator → P4（如 PRM [Lig23] 需 step-level 标签，OmegaPRM [Luo24] 以 MC 自动标注降低成本但引入噪声）。

若目标载体在消费侧完美匹配约束、但唯一生产路径在生产侧代价不可承受——如实记录此困境，指向 §9。

### 8.3.6 时序演化

约束有时间导数。经验体量单调增长——系统初期经验少，Narrative store 检索精度高、context 开销小（Reflexion [Shi23b] 的 always-on prepend 在经验少时完全可行），P1 充分。经验积累至百万条后，检索质量下降、context 紧张（ExpeL [Zha23c] 的 insight store 随使用增长面临检索退化），需向 Policy 迁移（P5 或 P6）。任务分布漂移——GUI agent 的目标网站改版、工具 API 废弃——使已有 Schematic artifact（Voyager 的 code skill）和训练好的 Policy 同时面临 staleness。安全要求可能升级——从无监管到强制可审计——使 Policy 从可行变为不可行。

最优载体配置因此是时间的函数。迁移本身是一条有完整生产画像的 pathway——其一次性训练成本须由 Policy 利用侧的节省收回。迁移过早则训出的 Policy 不足、切换后退化；迁移过晚则持续的检索退化已造成累积效率损失。迁移时机是收益–成本优化问题。在此视角下，§7 的复合路径获得时序读法：Refinement-Mediated Policy Internalization（§7.2）编排的是经验在不同载体间的停留时间——先在 Narrative 中积累到量且质量达标，再固化进 Policy。目前无系统能自动完成该判断与切换——此为 §9 的直接 open problem。

### 8.3.7 失配分析

约束可能被误判或在部署后变化。表 8.6 列出框架预测的失配症状。这些症状不构成框架的自我验证——每条须拿 §3–§7 中独立报告的 failure mode 对照，吻合处算证据，不吻合处转 open question。

| 失配类型 | 预测症状 | 可恢复性 | 恢复路径 |
|---|---|---|---|
| 强可解释 × Policy | 无法审计决策、错误定位困难、修正引发 catastrophic forgetting | 低 | P7 外化 → 审查 → 筛选后重训 P5 |
| 低延迟 × Narrative | 检索延迟叠加、context 过长致 prefill 超时 | 高 | 渐进迁移至 Latent 或 Policy |
| 大体量 × Narrative | 检索精度下降、超出 context budget、幻觉式引用 | 中 | 做 P5 迁移，需重训 |
| 高环境变动 × Policy | 策略过时、无法快速适应新工具/新 API | 低 | 重训，训练期间系统持续退化 |
| 安全关键 × Latent | 无法事前验证 latent 中经验质量 | 低 | latent 不可审计，只能放弃重建 |

**Table 8.6.** Predicted mismatch symptoms, recoverability, and recovery paths.

"大体量 × Narrative"的症状已在文献中独立报告：ExpeL [Zha23c] 的 insight store 随规模增长面临检索精度与 context 占用的双重压力，Darwinian Memory [Mi26b] 引入 survival-based pruning 正是对 memory bloat 的直接回应。"高环境变动 × Policy"的症状体现在工具调用域：Voyager [Wan23c] 的 code skill 在 Minecraft 版本更新后需重新生成和验证——skill library 的 staleness 是环境变动的直接后果。"安全关键 × Latent"的不可恢复性解释了为什么 Latent 几乎不进入 §7 composite 的中间环节——§7.4 已指出，Latent"缺少让外部模块插入评估或修复的接口，一旦写错便难在闭环里被发现"。可恢复的失配对应一条有代价但可执行的迁移路径；不可恢复的失配——经验已融入权重或连续向量、无法单独提取者——每条对应一个 §9 问题。

## 8.4 The Structural Origin and Generative Power

§8.1–§8.3 的分析共同指向一个结论：载体的生产代价、利用画像与约束压力分布，共同取决于其在 separable↔fused 谱上的位置，叠加两个 subclass 分叉的修正——formalization 定验证模式，functional role 定通道与 pathway 拓扑位。这不是五类载体的经验归纳，而是从 §2 的存在层次分类和决策规则出发的结构推论。

该归约赋予框架生成性。任一新转化技术可先在 §2 的层次结构中定位源端与目标端——这一定位即足以推断其生产机制的大致类型（inference-based 还是 training-based）、信息损失的性质（by-design 还是 by-limitation 主导）、利用侧的代价结构与访问粒度区间。分析涵盖尚未出现的形式，而不止于已有的七条路径与五个载体类别。

框架同时生成否定性预测。声称"既快又透明"的单载体方案等价于声称存在同处 separable 与 fused 两端的载体，与核心命题矛盾。若此类系统在实践中被报告，它要么实际上维护了 Tokenized 副本供审计（那是两套载体，不是一套），要么"透明"指某种近似解释（probing、attribution）而非真正的逐单元可读。这一否定性预测使框架可证伪——发现一个真正在融合存储下同时具备 per-item 可读性与零边际推理成本的载体，即构成对核心命题的反驳。

三个结构性待解问题构成 §9 的核心。第一，separability–amortization 耦合是信息论硬约束还是当前架构的软约束？Sparse feature、可编辑 parametric memory、adapter、retrieval-over-activations 等方向都在试探这一边界——它们不同程度地在融合存储中引入可选择性，但尚未在任何工作中实现 Policy 的逐单元可读与可修正。第二，Evaluator 通过选择通道实现的部分解耦能否推广至生成端？当前 Evaluator 的粒度来自后置于输出分布的调制——生成端不存在对等的后置机制。若能在 Policy 的前向传播中引入类似的"可拆卸调制步骤"——如可控的 activation gating 或 token-level routing——则可能在融合存储下实现选择性调取。第三，最优配置随时间变化时，何种机制可在线判定迁移时机并自动重排经验在各载体间的分布？§8.3.6 已将迁移形式化为收益–成本问题，但社区尚无系统能自动执行这一判断——它需要同时监控检索退化速率、训练成本估算与任务分布 drift 检测，是一个跨越经验管理全链路的元控制问题。