# 6. Parametric-Source Transformations

本章讨论以 Parametric 载体为源端的两条转化路径：P6（Evaluator → Policy，将已内化的评估经验转移到 Policy 参数中）与 P7（Parametric → Tokenized，将参数化经验外化为可被其他系统消费的 Token-level artifacts）。

## 6.1 Evaluator-to-Policy Transformation (P6)

P6 描述的转化是：固化在参数化评估器中的评价经验被迁移进 Policy 参数。源载体是 Evaluator parameter——trained reward model、process reward model、parametric verifier、critic、judge 或 value model 的权重；目标载体是 Policy parameter。与 P5（Tokenized → Policy）的区别在于监督所经的中介：P5 的监督是原始轨迹、人类示范或环境成功信号的直接写入，P6 的监督必经一个参数化评估器的已习得评价能力折射后才进入 Policy。

严格地说，被评价的 $(c,a,o)$ 才是经验的最初来源，Evaluator 只把这段经验的一个侧面（"什么样的输出更好"）压缩进了自己的权重。P6 与 P5 的分界落在"监督经过的中介"上，而非"经验从哪来"。本 Survey 在 P6 中以 Evaluator parameter 为源载体——它既是 P4（Tokenized → Evaluator）的产物，又是 P6 的起点。

P6 的判定特征是：评估器不只是被 Agent 在推理时调用，而是通过训练信号持久地改变 Policy 参数。若评估器仅在 decoding、reranking、best-of-N selection、tree search 或 MCTS 中作为推理时控制器使用，Policy 权重未被该信号更新，则属 evaluator utilization 而非 P6。只要评估器输出被转化为 reward、preference pair、advantage、penalty、filtered trajectory 或 refinement target 并用于更新 Policy 参数，即构成 P6。

**边界处理。** 规则型 verifier（单元测试、数学答案精确匹配、编译器返回码）是零参数函数，其信号是 environment-grounded outcome，归 P5 而非 P6；只有参数化 verifier（训练得到的 correctness 判别模型）才是 P6 的合法源载体。Off-the-shelf LLM-as-a-judge 的评价能力主要来自预训练，难以回溯到某段具体的 agent experience，对 §2.3 的经验语义锚定条件构成挑战，本文将其作为 P6 的边界案例处理而非排除——当 judge 被约束在特定 constitution、rubric 或 meta-question 之下时，被评价的 $(c,a)$ 与约束共同提供经验锚定。涉及 off-the-shelf judge 的工作在正文中显式标注其边界属性。

<!-- 评估器筛选/修正数据的 P5/P6 判据：若评估器的判断是数据得以改善的 load-bearing 因素（去掉评估器，这些轨迹既不会被构造也不会被选中），且方法核心贡献在于"如何用评估器筛选或修正经验"，则归 P6；若评估器只是边角环节、核心是轨迹本身的来源或形式，则归 P5。 -->

本节沿两条正交轴组织 P6 方法。第一条是**反馈粒度**：Outcome（评估完整输出/完整 trajectory/完整 episode）与 Process（评估中间步骤、局部动作、reasoning prefix 或 state-action pair）。第二条是**反馈形态**：Discriminative（评估器产出 scalar reward、score、pairwise preference 等可比较的数值或序关系信号）与 Generative（评估器产出 natural-language critique、failure explanation、refined step 或 revised trajectory 等解释性/修正性内容）。两轴交叉得到四类，对应 §6.1.1–§6.1.4。分配工作时以真正驱动 policy update 的主要 feedback artifact 为准，而非评估器内部最丰富的能力或训练算法的名称。

### 6.1.1 Discriminative Outcome Evaluator-to-Policy Transfer

判别式 outcome 评估器对完整输出或完整 trajectory 给出 scalar reward、trajectory-level score、pairwise preference 或 chosen/rejected label，这些信号通过 RLHF/RLAIF、preference optimization 或 filtered distillation 进入 Policy。这是 P6 四格中文献最密集、工程最成熟的一格，直接继承经典 RLHF 流水线。

**经典 RLHF 与 AI feedback 替代 human feedback。** Constitutional AI [Bai22b] 的 RL-CAI 阶段由 constitution-guided AI judge 对完整回答给偏好，训练出 preference model 后经 RLAIF 把 harmlessness 判断写入 policy。<!-- TODO: 补充方法名缩写 --> [Lee23b] 系统比较 RLHF 与 RLAIF，指出 off-the-shelf LLM 既可先提供偏好数据训练 RM，也可在 d-RLAIF 中直接对完整输出打 outcome-level 分数驱动 RL，其 judge 为通用 LLM，属边界案例。

**在线化与自反式评估。** OAIF [Guo24] 让在线 LLM annotator 对当前 policy 采样出的完整回答对给偏好，偏好不再蒸馏成独立 RM 而是直接进入 DPO/IPO/SLiC，保证监督分布始终 on-policy。自反式 P6 的特殊形态是源评估器与目标 policy 共享同一组参数：Self-Rewarding Language Models [Yua24] 让同一模型既当 generator 又当 judge，自评分构造 winner-loser pairs 后以 iterative DPO 回灌。Meta-Rewarding Language Models [Wu24d] 进一步加入 meta-judge 改进 judge 自身评分质量，形成 actor/judge/meta-judge 共演化。

**Best-of-N distillation 与 filtered SFT。** 这组工作不走 on-policy RL，而是用评估器筛出高分样本后做监督式写入。RAFT [Don23] 用 RM 对同 prompt 的多条回答打分、保留 best-of-K 做 SFT。BOND [Ses24] 把推理时的 Best-of-N selection 蒸馏为单次采样 policy，用 forward/backward KL 逼近 RM 定义的 BoN 分布。BoNBoN [Gui24] 离线刻画 best-of-n 分布，用 SFT-BoN 与 IPO-BoN 把最优、最差样本同时纳入。在 agent 域，<!-- TODO: 补充方法名缩写 --> [Gon24b] 的 critic LLM 对整条 trajectory 评分，top p% 高分轨迹作为伪示范配合通用数据做迭代 SFT。

**稳定性、去偏与多评估器。** 当 policy 持续针对一个 imperfect 评估器优化时，reward hacking、length bias、judge bias 会被放大。<!-- TODO: 补充方法名缩写 --> [Ack26] 把 reward hacking 解释为 policy 利用 proxy reward 的尖锐高点，加入 gradient regularization/reference reset 稳定 outcome-level RL。[She24c] 的 policy filtration 只让 RM 最可靠的高低分样本进入 PPO buffer。[Wu25x] 用 Bayesian router 在多个 trained RM 间按 query 动态选路，将 routed preference pairs 用于 online DPO。[Xu24d] 的 Mixture of Judges 把 calibrated RM、LLM judges 与 rule-based constraint judges 的判断注入 CRPG/CODPO/CRRAFT。<!-- TODO: 补充方法名缩写 --> [Fis24] 把 RM 的 reward difference 蒸馏进 policy 的 implicit reward。[Ren26b] 让 LLM judge 通过 meta-question 的 YES 概率合成 scalar reward，经 GRPO/CISPO 更新 policy。

<!-- 评估器具 process 能力、但 artifact 落在 outcome 的边界情形：[Din25b] 的 FAPO 用 generative RM 定位 first invalid step，该诊断被压缩成对整条 rollout 的 penalty 后才进入 GRPO。[Che25v] 的 step-wise judge 对推理链做 first-error identification，转成 trajectory 的 partial-correctness 标量，使 all-negative groups 也能产生梯度。[Li26p] 内部有 milestone verifier 与 trajectory judge，但在线 RL 主信号是 trajectory-level reward。评估器的诊断粒度与 policy 实际消费的 artifact 粒度可以解耦。 -->

判别式 outcome 的优势是形式简单、与现有 RLHF/DPO/rejection sampling 框架适配性强、scalar 信号易规模化。代价集中在两点：评估器只评完整结果，长程任务下 credit assignment 粗糙；当 policy 持续针对固定且 imperfect 的评估器优化时，reward hacking、length bias 与 judge bias amplification 会显现，且随 policy 漂移、离线训练的 RM 会逐渐 off-distribution 而失真。

### 6.1.2 Generative Outcome Evaluator-to-Policy Transfer

生成式 outcome 评估器对完整输出或完整 trajectory 产出解释性、批评性或修正性的自然语言内容——critique、failure explanation、revised response——并把这些内容（而非 scalar）作为 policy 的主要监督。

这一格的早期实例是 Constitutional AI [Bai22b] 的 SL-CAI 阶段：反馈模型按 constitution 对完整回答生成 critique 与 revision，policy 直接对 revision 做 SFT。进入训练的是一条被修正过的完整回答，粒度是 outcome、形态是生成式。ECHO [Li26l] 是更晚近的完整实例：与 actor 同步更新的 linguistic critic 对完整 rollout 生成 score-aware critique，actor 据此产出 refined rollout，policy 用 GRPO 在 critique 条件下优化这些 refined trajectories，critic 在同批数据上共演化。

这一格在四格中文献最稀疏。原因带结构性：生成式反馈的价值在于指出"哪里错、为何错、如何改"，这种定位能力天然倾向落到步级而非整条轨迹——一旦评估器愿意生成细粒度解释，把它用在 process 粒度比用在 outcome 粒度信息利用率更高。生成式评估器多向 §6.1.4 聚集，纯粹停留在 outcome 粒度的生成式工作相对少见。

生成式 outcome 的优势是单条信号信息量远高于 scalar，能为 policy 提供"为什么"的监督，且与 co-evolution 结合可缓解评估器陈旧。代价是 critique 与 revision 的质量受评估器自身能力上限制约，评估器幻觉出的错误诊断会被 policy 当作正确监督吸收，而 critique 正确性本身难以验证。

### 6.1.3 Discriminative Process Evaluator-to-Policy Transfer

判别式 process 评估器对轨迹中的中间步骤、局部动作、reasoning prefix 或 state-action pair 给出数值或序关系信号——step score、turn-level advantage、token-level dense reward、step-wise preference——并把这些步级判别信号转进 policy。核心动机是长程 agent 学习的 credit assignment：仅靠末端 reward，policy 难以知道该强化或避免哪些局部行为。

**Turn/step-wise value 与 critic。** SWEET-RL [Zho25p] 在 multi-turn 协作推理中训练 turn-level critic，利用 training-time privileged information 直接学每轮 action 的 advantage，经 DPO 把 turn-wise credit assignment 蒸馏进 actor。[Wan26s] 在 GUI 场景训练 Agentic-Q model 对 state-action pair 估计 future return，把 step-wise value 接入 SWPO 式更新。PPRM [Xu25h] 面向 non-verifiable 的 multi-turn search，用 principle-based PRM 对每个 turn 的 correctness/relevance/coherence 评分，经 ReNorm 与末端 ORM 校准后送入 PPO + GAE。

**Dense reward 从评估器内部解包。** <!-- TODO: 补充方法名缩写 --> [Cha24b] 不额外构造 process label，而是把标准 RM 最后层 attention 的 token 归因取出，将终局 scalar reward 重分配为 token-level dense reward 送入 PPO——评估器不变，改变的是 reward 从评估器投影到 policy 的粒度。CW-GRPO [Wan26ac] 用 rubric-based LLM judge 对每轮 search 给 retrieval utility 与 reasoning correctness 两个 binary 信号，合成 round-level contribution weight 把 trajectory-level advantage 按轮重分配。

**Step-level filtering 与多维 rubric。** Language Feedback Model [Zho24e] 对每个动作判断是否 productive，policy 通过 behavior cloning 吸收被标为 desirable 的 state-action pairs。AdaRubric [Din26e] 先为任务生成 rubric，再对每个 step、每个维度输出 1–5 分，聚合后既做 trajectory-level DPO 也做 step-level PPO，rationale 主要用于解释而非训练主载体。[Luo25f] 用 GPT-4o judge 对 computer-use 场景的单步 GUI action 候选打 0–100 分，由高低分构造 step-level preferred/rejected pairs 训练 UI-TARS-2B。

判别式 process 的优势是直接缓解 credit assignment，梯度更密、长程与多轮任务下样本效率更高。代价是可靠的 PRM 训练成本高，过程标签噪声大且"什么是一个好步骤"本身难以界定。PRM 自身同样可被 hack，policy 可能学会生成局部高分但全局错误的步骤。step reward 与 outcome reward 的尺度校准困难。[Xu25h] 的 ReNorm 与 [Wan26ac] 的归一化都是对此的应对。

### 6.1.4 Generative Process Evaluator-to-Policy Transfer

生成式 process 评估器对中间步骤产出解释性、诊断性或修正性内容——step-level critique、first-error 定位加 refined step、revision trajectory、directive hint——并把这些内容转进 policy。与判别式 process 回答"这一步好不好"不同，生成式 process 回答"这一步为什么不好、应如何改"。这一格是 P6 与 P5/P7 边界最模糊处：进入 policy 的常是 refined trajectory 这一 tokenized 载体，且修正动作往往由某个强 policy 生成。按判据，只要评估器的诊断是修正得以发生的 load-bearing 因素、且方法核心是用评估器定位并修正经验，即归 P6。

**Step-wise 诊断与 refinement。** SRR-Judge [Zha26am] 对 search agent 每个 thought-action step 同时输出 explanation、1–5 rating 与 refined thought/refined action，rating 负责筛选、refined step 作为生成式对齐目标，经 iterative RFT 写入 policy。Natural Language Actor-Critic [Hon25c] 用 generative language critic 为每个 state-action 产出 future trajectory 走向与优劣理由的自然语言 critique，actor 在 critique 条件下生成 refined action 再反向蒸馏回基础 policy。

**Failure-driven reflection 与修正内化。** Agent-R [Yua25c] 让 actor 自身充当 verifier，在搜索树分叉中定位坏轨迹的 transition point，在错误前缀与正确后续之间插入 revision signal，把"反思加修正"实例做迭代 SFT。Agent-R 进入 policy 的是 revision trajectory 的文本 token，与 P5 相邻；归 P6 的依据是其自评判断是修正数据得以构造的 load-bearing 环节。OpenClaw-RL [Wan26ad] 从用户话语或环境信号中抽取 directive textual hints，用 On-Policy Distillation 把 hint-enhanced teacher 与 student 的 log-prob gap 转成 token-level directional update。

<!-- AgentRefine [Fu25d] 构造 multi-turn error-refine trajectories，由强模型针对 parameter error、logical error 和 location error 给出诊断性反馈并展示 refined action。训练时仅对修正步骤计算损失——其 evaluator agent 的诊断是 refined data 得以构造的 load-bearing 因素。 -->

生成式 process 的信息密度与可解释性在四格中最高，最适配错误类型复杂、任务空间开放的 agent 场景，也是当前最活跃的前沿。代价同样最重：critique 与 refined step 的质量受评估器能力上限封顶，"谁来评估评估器"在生成式形态下尤其突出——一个错误的 critique 比一个错误的 scalar 更具误导性，且其正确性难以自动验证。refined trajectory 相对当前 policy 是 off-policy 的，蒸馏存在分布失配。评估器与 teacher policy 的角色在 refined-action 这一支高度重叠，使 P6 与 P7 难以干净切分。

### 6.1.5 Discussion

**四格分布的不均衡。** 判别式 outcome 直接继承经典 RLHF，工程接口稳定、工作最多。判别式 process 围绕 credit assignment 快速扩张。生成式 process 是最活跃的前沿但与 P5/P7 纠缠最深。生成式 outcome 最稀疏——生成式反馈的定位价值会把评估器推向步级粒度。两轴并非对称：粒度轴回答"评估落在多大的单位上"，形态轴回答"评估以什么形式表达"，后者同时决定信息密度与可验证性之间的 trade-off。

**评估器被利用是跨四格的共同失效模式。** 无论评估器输出 scalar 还是 critique、落在 outcome 还是 step，只要 policy 持续针对一个固定且 imperfect 的评估器优化，就会逼近评估器的偏差而非真实目标。文献中的三类应对各有侧重：co-evolution 让评估器随 policy 更新 [Yua24, Wu24d, Li26l]；ensembling/routing 用多评估器分散单点偏差 [Wu25x, Xu24d]；regularization 与 filtration 约束优化过程 [Ack26, She24c]。生成式形态下这一问题更隐蔽——错误 critique 的误导性强于错误 scalar，而 critique 的正确性缺乏自动验证手段。

<!-- 自反式 P6 是一个反复出现的结构：评估器与 policy 共享参数 [Yua24, Wu24d, Yua25c]。此时 source 与 target 载体重合，P6 与 P7 在同一组权重内闭环。这类工作的可持续性取决于评估能力能否与生成能力同步提升。 -->

**趋势。** 跨四格的趋势是评估器从判别走向生成、从 outcome 走向 process——从回答"好不好"转向回答"为什么不好、应如何改"。这条趋势提升了监督的信息密度，也把"评估器自身的可靠性如何保证"推到前台。判别式信号至少可以用 held-out 偏好一致性等方式间接核验，生成式步级 critique 的正确性核验目前仍缺乏成熟手段。

## 6.2 Parametric-to-Tokenized Transformation (P7)

P7 把已内化在参数化模型权重中的经验外化为可被其他系统消费的 Token-level artifacts。源端是 Policy 或 Evaluator 参数（承载这些参数的模型可由任意 modality 实现，LLM、VLM、VLA 均可），目标端是 agent trajectories、tool-use demonstrations、GUI action traces、step-level labels、critiques、preference annotations 等 Tokenized 载体。P7 与 P5 方向相反：P5 把离散经验写入参数，P7 从参数中读出可复用的经验表达。

P7 仍是一条 representation-to-representation pathway。外化出的 trajectory 并非凭空产生，它重新编码了曾经经由 P4/P5 写入参数的经验语义，满足经验语义锚定与经验内容承载两个条件。与 P1–P6 不同的是 source 端的形态：P3 的 source 是一条确定的 trajectory，转化算子是确定性的 re-encoding；P7 的 source 是参数这种聚合态表示，贡献它的多条原始 trajectory 已在权重分布中彼此叠加、无法再被个别定位，转化算子相应地包含一次采样——$\mathcal{T}$ 从 $p(e \mid \text{prompt}, \text{env})$ 中抽取样本，而非对某个给定的 $e$ 做重编码。

这一 source 性质决定了 P7 的两个组织性事实。采样有方差，低质量样本必须由 verifier/filter 在事后剔除，这解释了为何 P7 方法几乎无一例外地挂载验证环节。采样可重复进行并保留最优样本，这带来 best-of-N 效应：在筛选后的 teacher 数据上训练的 student，其可靠性可以高于 teacher 单次采样的平均水平。

P7 需与三类相邻过程区分。普通 inference 中模型生成的 CoT 或答案只服务于当前 query，没有独立归档与复用意图，不构成 P7。Self-training/iterative bootstrapping 中模型生成的 rollouts 被同一训练循环的后继版本直接消费，更接近 composite pipeline（§7）。与 P1/P2 的区分可归结为一条可操作判据：追溯转化的输入端——若输入是一条已存在的 trajectory、转化是对这条 trajectory 的重表述，归 P1/P2；若输入只是 prompt 或 task specification、被外化的内容来自模型已内化的能力，归 P7。

按外化经验在下游系统中的消费角色，P7 分为两类：**Demonstration Externalization** 外化"如何行动"的经验，来自 Policy 参数；**Evaluative Supervision Externalization** 外化"如何评价"的经验，来自 Evaluator 参数。两类的分界线在于 Evaluator 判断的去向——判断被物化为独立、可复用的监督数据则归入后者，判断只作为内部过滤开关则仍是前者内部的质量控制机制。

### 6.2.1 Demonstration Externalization

Demonstration Externalization 指参数化 Policy 或 teacher agent 将其隐式决策能力外化为可供 student 模仿学习的行为示范。目标 artifact 通常是 agent trajectories、tool-use dialogues、web/GUI/mobile interaction traces 或 reasoning-action paths，下游 consumer 通过 SFT、behavioral cloning 或 imitation-style training 吸收这些示范。消费方式是 SFT 还是 RL 不改变 artifact 的载体属性，归类依据是被外化 artifact 的形态而非它如何被消费。

Demonstration Externalization 的根本定性约束是能力天花板：student 在任务能力维度上继承的是 teacher 的上界。P7 用 teacher 的一次性推理成本换取 student 的低推理成本、可规模化与领域专用化，而非超出 teacher 的能力。best-of-N 效应能把 student 的可靠性抬高到 teacher 平均水平之上，但抬高的是同一能力前沿内的稳定性，而非能力前沿本身。

本节以环境合成度为组织轴。它锚定在四元组的 observation $o$ 上：$o$ 越是来自真实环境的客观返回，外化轨迹的 grounding 越强；$o$ 越是由模型自身生成，轨迹越接近一次纯参数读出。沿这条轴，pseudo-success 与 hallucinated observation 的风险递增，verifier 的必要性也相应递增。

**真实环境锚定。** Teacher 在真实网站、真实 MCP server 或真实操作系统上交互，$o$ 是环境返回的客观后果。Explorer [Pah25] 让 GPT-4o 在真实网页中以 exploration-driven 方式自主发现任务、执行多步交互，经 proposer/refiner/summarizer/verifier 流水线产出带页面状态、动作序列与任务总结的 multimodal trajectories。InSTA [Tra25] 将这一思路推至 internet scale，使强模型在大规模真实网站上自动提出任务、执行操作并生成 reasoning traces。AutoSurfer [Fai26] 先系统性 surf 真实网站、识别功能空间，再整理为含页面状态、动作历史与推理的 task tuples。SynthAgent [Wan25ar] 在目标网站上先做 element-level exploration 与任务合成，再于收集后全局 refine。Structured Distillation of Web Agent Capabilities [Lu26] 以 Agent-as-Annotators 框架让 Gemini teacher 生成带结构化 reasoning block 的成功轨迹。

计算机与移动端，Fara-7B [Awa25] 经 FaraGen 产出 screenshot-thought-action trajectories 并由三重 verifier 筛选。OpenMobile [Che26d] 以 expert 接管修正 learner 偏差，把 corrected trajectories 与 step-level CoT 一并保留。TOUCAN [Xu25o] 在真实 MCP environments 中让多个强模型合成任务并执行完整 tool-use rollouts，经 task-level 与 trajectory-level 双重过滤形成大规模 tool-agentic corpus。

**模拟环境合成。** 环境本身由模型扮演，$o$ 不再是真实返回而是 simulator 的生成结果。ToolAlpaca [Tan23] 用 ChatGPT 分别扮演 user、assistant 与 tool executor，通过多智能体 simulation 生成工具使用轨迹。ToolMind [Yan25ab] 以 user/assistant/tool 三类 agent 的模拟生成带 reasoning 的多轮交互轨迹，并在 trajectory-level 与 turn-level 做细粒度过滤。ToolACE [Liu24o] 先自动扩充 API pool，再以 self-guided dialogue 合成多种复杂度的工具调用对话。APIGen-MT [Pra25b] 先生成 task blueprint 与 ground-truth action sequence，再经 simulated agent-human interplay 合成多轮 function-calling dialogues。Learning with Challenges [Kan26b] 先评估 student 能力边界，再用多智能体生成器合成难度自适应的 mobile GUI demonstrations。

**构造式合成（弱交互）。** 此端几乎没有交互环境，trajectory 围绕预先给定的 answer、evidence 或问题结构反向构造，最接近纯参数读出。EviPath [Li25at] 从 gold evidence 反推 abductive reasoning path，再由强模型生成含 planning、sub-question decomposition 与 evidence-grounded answering 的 RAG trajectories。RAGShaper [Tao26] 构造带 distractor 的信息树与多跳问题，在受控检索环境中诱导强 teacher 产出 agentic RAG trajectories。APIGen [Liu24n] 让强模型基于真实可执行 API 生成自然语言 query 与结构化 function-calling answers，经 format/execution/semantic 三层检查筛选——保留了基于真实 API 的 execution check，但交互深度浅，整体偏生成而非交互。

以上方法的目标载体都是 Narrative trajectory，但 Demonstration Externalization 的目标不限于 Narrative。FABRIC [Ver25b] 通过 LLM-only pipeline 生成 task description、tool definition、policy pseudocode、dialogue 与 execution trace，其中 policy pseudocode 与 task/tool schema 属于 Schematic Tokenized，构成 P7 → Schematic 子格。

Demonstration Externalization 的风险沿环境合成度轴分布。teacher 生成的轨迹可能包含 hallucinated actions、不可执行步骤或伪成功轨迹，这一风险在模拟环境与构造式合成两端显著放大。单一 teacher 还会导致 distribution narrowing，使 student 过度拟合 teacher 的表达风格与决策偏好，multi-teacher mixing 是常见缓解手段。

### 6.2.2 Evaluative Supervision Externalization

Evaluative Supervision Externalization 指参数化 Evaluator——judge、verifier、critic、reward model——将其隐式评估能力外化为 Token-level supervision，供 student model、agent system、data filtering pipeline 或 reward-model training 消费。与 Demonstration Externalization 外化"如何行动"不同，这类方法外化的是"如何判断行动质量"。

目标 artifact 包括 critiques、step-level labels、action correctness annotations、progress labels、preference pairs、verification traces、failure diagnoses 等。

**步骤级正确性标注。** Scalable Data Synthesis with Step-Level Filtering [He25g] 先用强 computer-use agent 生成 noisy trajectories，再由 o4-mini 对每一步做 correctness 与 optimality grading，附 screenshot analysis、action review、alternative analysis 等 reasoning-rich annotations。评估结果被物化为 WebSTAR 与 WebSCORE 两套数据资源，前者训练 student computer-use agent，后者蒸馏出轻量 StepRM。STEVE [Lu25e] 以 GPT-4o 作为 step verifier，比对动作执行前后的界面状态，为每一步生成 binary correctness label 与 verification reasoning，据此构建 step-verified trajectory data 并经 KTO 训练开源 student agent。

**长程进展与过程结构。** Constraint-guided Web Task Evaluation [Log26b] 用 judge 从 web task 抽取显式 constraints，在轨迹每一步评估 constraint satisfaction state，形成细粒度 CSR progress signal，并据此执行 prefix extraction 与 hindsight relabeling，使部分成功轨迹也能转化为可训练样本。Step-GUI [Yan25x] 先以轨迹级 verifier 建立质量锚点，再由强多模态 thinking model 把验证结果转写为 progress tracking、state summary、effect prediction、self-reflection 等七类结构化 step-level supervision。

Evaluative Supervision Externalization 与 P6 的区分：P6 的核心是 Evaluator 的 reward/preference/critique 直接参与 Policy 优化、使 Policy 参数更新；P7 强调 Evaluator 的输出被显式物化为 Tokenized artifact，且可脱离原 Evaluator 被其他系统复用。许多 Demonstration Externalization 方法用 judge 删除低质量轨迹，但若 judge 的输出只作为内部过滤开关，它就只是质量控制机制；只有当 Evaluator 的判断本身成为独立、可复用的 artifact，才归入 Evaluative Supervision Externalization。

### 6.2.3 Discussion

Demonstration Externalization 与 Evaluative Supervision Externalization 分别外化 Policy 的决策能力与 Evaluator 的评估能力，对应"应该如何行动"与"如何判断行动质量"两条主线。一篇论文可能涉及多条转化路径，placement 取决于其主要被下游消费的 artifact 类型。

P7 在 Experience Source 属性上占据一个特殊位置：{teacher}-sourced experience 几乎全部经由 P7 进入语料，P7 正是制造 {teacher} 这一经验来源的工艺过程。这也使 P7 区别于其余六条路径——P1–P6 处理的是已经存在的经验，P7 在生产新的经验载体。

P7 的核心 trade-off 由几个相互咬合的因素决定：能力天花板限定了 P7 不扩展 teacher 的能力前沿，它兑换的是成本、推理效率与领域专用化；相对人工标注，P7 以 teacher 的一次性推理成本换取近乎任意规模的监督数据，代价是数据质量受 teacher 能力与采样方差双重限制。verifier 在这条 trade-off 中既吸收采样方差，又通过 best-of-N 效应把 filtered student 的可靠性抬到 teacher 平均水平之上。环境合成度决定 $o$ 的 grounding 强度与 verifier 的负担轻重。environment-mediated synthesis、multi-teacher mixing、curriculum 与 difficulty-aware sampling、execution-based verification 等横向设计维度，作用对象都是外化 artifact 的质量、规模、多样性与可验证性。
