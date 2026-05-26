# 6. Parametric-Source Transformations

以 Parametric 载体为源端的转化共两条:Evaluator-to-Policy(§6.1)把固化在评估器参数中的判断能力转入 Policy 参数,Parametric-to-Tokenized(§6.2)把权重中已内化的决策或评估能力外化为可被其他系统消费的 Token-level artifacts。两条 pathway 的共同特征是 source 已处于参数态——它是其他 pathway 的产物,而非来自原始交互日志的直接监督。

## 6.1 Evaluator-to-Policy Transformation (Evaluator-Driven Optimization)

Evaluator-Driven Optimization 通过训练信号把参数化评估器的已习得评价能力持久地写入 Policy 参数。监督经由一个参数化中介这一点是它与 Policy Internalization 的分界——后者的监督是原始轨迹、人类示范或环境成功信号的直接写入,前者经评估器的判断折射后才进入 Policy;判定特征是 Policy 权重确实因评估器信号而更新,仅在 decoding、reranking、best-of-N selection、tree search 或 MCTS 中受评估器调控而不更新权重的工作不属此路径。

源载体取 Evaluator parameter,而非真正被评价的 $(c,a,o)$。被评价的轨迹是更早的经验,已经在 Evaluator Internalization 阶段被压缩进权重;Evaluator parameter 既是该路径的产物,也是 Evaluator-Driven Optimization 的起点。

### 6.1.1 Discriminative Outcome Evaluator-to-Policy Transfer

判别式 outcome 评估器对完整输出或完整 trajectory 给出 scalar reward、trajectory-level score、pairwise preference 或 chosen/rejected label,policy 经 RLHF/RLAIF、preference optimization 或 filtered SFT 把这些可比较信号写入参数。这一格直接继承经典 RLHF 流水线,与现成的对齐工具链接口稳定。

**经典 RLHF 与 AI feedback 替代人类反馈。** Constitutional AI [Bai22b] 的 RL-CAI 阶段是这一格的母本:constitution-guided AI judge 对完整回答给偏好,训练出 preference model 后经 RLAIF 把 harmlessness 判断写入 policy。RLAIF [Lee23b] 沿同一思路系统比较了 off-the-shelf LLM 充当偏好标注与直接给分两种用法——canonical RLAIF 仍先训 RM,d-RLAIF 则把 judge score 当在线 reward;judge 为通用 LLM、不针对具体 agent experience 训练,对经验语义锚定较弱,在归属上属边界。

**在线化与自反式评估。** 把偏好标注从离线移到在线可避免 RM 随 policy 漂移而 off-distribution。OAIF [Guo24] 让在线 LLM annotator 对当前 policy 采样出的完整回答对给偏好,偏好不再蒸馏成独立 RM 而是直接进入 DPO/IPO/SLiC,保证监督分布始终 on-policy。自反式 Evaluator-Driven Optimization 进一步让源评估器与目标 policy 共享同一组参数:Self-Rewarding Language Models [Yua24] 让同一模型既作 generator 又作 judge,自评分构造 winner-loser pairs 后以 iterative DPO 回灌;Meta-Rewarding Language Models [Wu24d] 在此之上加入 meta-judge 改进 judge 自身评分质量,形成 actor/judge/meta-judge 共演化。

**Best-of-N distillation 与 filtered SFT。** 这组工作不走 on-policy RL,而是用评估器筛出高分样本后做监督式写入,以更低算力逼近 RL 的对齐效果。RAFT [Don23] 用 RM 对同 prompt 多条回答打分、保留 best-of-K 做 SFT。BOND [Ses24] 把推理时的 Best-of-N selection 蒸馏为单次采样 policy,以 forward/backward KL 逼近 RM 定义的 BoN 分布。BoNBoN [Gui24] 离线刻画 best-of-n 分布,通过 SFT-BoN 与 IPO-BoN 把最优与最差样本同时纳入。在 agent 域,[Gon24b] 的 critic LLM 对整条 trajectory 评分,top p% 高分轨迹作为伪示范配合通用数据做迭代 SFT。

**稳定性、去偏与多评估器。** policy 持续针对一个 imperfect 评估器优化会放大 reward hacking、length bias 与 judge bias,这组工作针对这一点设计 regularization 与 ensembling 机制。[Ack26] 把 reward hacking 解释为 policy 利用 proxy reward 的尖锐高点,在 Dr.GRPO 风格的 RL 目标上加入 gradient regularization 与 reference reset。Policy Filtration [She24c] 只让 RM 最可靠的高低分样本进入 PPO buffer。[Wu25x] 用 Bayesian router 在多个 trained RM 间按 query 动态选路,将 routed preference pairs 用于 online DPO。Mixture of Judges [Xu24d] 把 calibrated RM、LLM judges 与 rule-based constraint judges 的判断注入 CRPG/CODPO/CRRAFT,以多评估器结构抑制单点偏置——其中规则约束部分严格而言不属 Evaluator-Driven Optimization,但参数化评估器仍是核心信号源。[Fis24] 把 RM 的 reward difference 蒸馏进 policy 的 implicit reward,用 L2 distillation loss 加 forward KL 正则做离线更新。[Ren26b] 让 LLM judge 通过 meta-question 的 YES 概率合成 scalar reward,经 GRPO/CISPO 更新 policy;其 judge 可 frozen、self-eval 或 ensemble,与 [Lee23b] 同属 off-the-shelf judge 边界。

**步级诊断压缩为轨迹标量。** 评估器内部具备步级诊断能力,但落到 policy 上的 artifact 仍是轨迹级标量,粒度归属以后者为准。FAPO [Din25b] 的 generative RM 定位 first invalid step,该诊断被压缩成对整条 rollout 的 penalty 后才进入 GRPO。[Che25v] 的 step-wise judge 对推理链做 first-error identification,转成 trajectory 的 partial-correctness 标量,使 all-negative groups 也能产生梯度。OS-Themis [Li26p] 内部含 milestone verifier 与 trajectory judge,但在线 RL 主信号是 trajectory-level reward。

### 6.1.2 Generative Outcome Evaluator-to-Policy Transfer

生成式 outcome 评估器对完整输出或完整 trajectory 产出解释性、批评性或修正性的自然语言内容——critique、failure explanation 或 revised response——并把这些内容(而非 scalar)作为 policy 的主要监督。

这一格的早期实例是 Constitutional AI [Bai22b] 的 SL-CAI 阶段:反馈模型按 constitution 对完整回答生成 critique 与 revision,policy 直接对 revision 做 SFT;进入训练的是一条被修正过的完整回答,粒度是 outcome、形态是生成式。ECHO [Li26l] 是更近期的完整实例:与 actor 同步更新的 linguistic critic 对完整 rollout 生成 score-aware critique,actor 据此产出 refined rollout,policy 以 GRPO 在 critique 条件下优化这些 refined trajectories,critic 在同批数据上经双轨 GRPO 共演化。生成式反馈的定位价值天然倾向落到步级——一旦评估器愿意生成细粒度解释,把它用在 process 粒度比用在 outcome 粒度信息利用率更高,因此 outcome 形态的生成式评估器多向 §6.1.4 迁移。

### 6.1.3 Discriminative Process Evaluator-to-Policy Transfer

判别式 process 评估器对中间步骤、局部动作、reasoning prefix 或 state-action pair 给出 step score、turn-level advantage、token-level dense reward 或 step-wise preference,policy 经这些步级判别信号更新参数。核心动机是长程 agent 学习的 credit assignment:仅靠末端 reward,policy 难以辨别该强化或避免哪些局部行为。

**Turn/step-wise value 与 critic。** 评估器以单独模型形态承担步级价值估计。SWEET-RL [Zho25p] 在 multi-turn 协作推理中训练 turn-level critic,利用 training-time privileged information 直接学每轮 action 的 advantage,经 DPO 把 turn-wise credit assignment 蒸馏进 actor。[Wan26s] 在 GUI 场景训练 Agentic-Q model 对 state-action pair 估计 future return,把 step-wise value 接入 SWPO 式更新。PPRM [Xu25h] 面向 non-verifiable 的 multi-turn search,用 principle-based PRM 对每个 turn 的 correctness/relevance/coherence 评分,经 ReNorm 与末端 ORM 校准后送入 PPO + GAE。

**Dense reward 从评估器内部解包。** 评估器形态不变,改变的是把已有 outcome reward 投影到 token 或 round 上。[Cha24b] 不额外构造 process label,而是把标准 RM 最后层 attention 的 token 归因取出,将终局 scalar reward 重分配为 token-level dense reward 送入 PPO。CW-GRPO [Wan26ac] 用 rubric-based LLM judge 对每轮 search 给 retrieval utility 与 reasoning correctness 两个 binary 信号,合成 round-level contribution weight 把 trajectory-level advantage 按轮重分配。

**Step-level filtering 与多维 rubric。** 评估器为每个步骤或维度直接产出可比较分数,policy 通过筛选或对比写入。Language Feedback Model [Zho24e] 对每个动作判断是否 productive,policy 通过 behavior cloning 吸收被标为 desirable 的 state-action pairs。同类思路下,[Pan24b] 的 autonomous evaluator 既可端到端由 GPT-4V 实现也可由 captioner+reasoner 模块化构成,device-control 分支用其 per-step progress filtering 结果做 Filtered BC——只有此分支属 Evaluator-Driven Optimization,inference-time Reflexion 分支不更新权重不在路径内。AdaRubric [Din26e] 先为任务生成 rubric,再对每个 step、每个维度输出 1–5 分,聚合后既做 trajectory-level DPO 也做 step-level PPO,rationale 仅用于解释而非训练主载体。[Luo25f] 用 GPT-4o judge 对 computer-use 场景的单步 GUI action 候选打 0–100 分,由高低分构造 step-level preferred/rejected pairs 训练 UI-TARS-2B。

### 6.1.4 Generative Process Evaluator-to-Policy Transfer

生成式 process 评估器对中间步骤产出解释性、诊断性或修正性内容——step-level critique、first-error 定位加 refined step、revision trajectory、directive hint——并把这些内容转进 policy。与判别式 process 回答"这一步好不好"不同,生成式 process 回答"这一步为什么不好、应如何改"。

这一格的归属判定较微妙——进入 policy 的常是 refined trajectory 这一 tokenized 载体,且修正动作往往由某个强 policy 生成,使其与 Policy Internalization 和 Parametric Externalization 边界接壤;只要评估器的诊断是修正得以发生的 load-bearing 因素、且方法核心是用评估器定位并修正经验,即归 Evaluator-Driven Optimization。

**Step-wise 诊断与 refinement。** SRR-Judge [Zha26am] 对 search agent 每个 thought-action step 同时输出 explanation、1–5 rating 与 refined thought/refined action,rating 负责筛选、refined step 作为生成式对齐目标,经 iterative RFT 写入 policy;此处 rating 与 refined step 同时入训,在四格归属上以生成式为主。Natural Language Actor-Critic [Hon25c] 用 generative language critic 为每个 state-action 产出未来走向与优劣理由的自然语言 critique,actor 在 critique 条件下生成 refined action 再反向蒸馏回基础 policy。

**Failure-driven reflection 与修正内化。** Agent-R [Yua25c] 让 actor 自身充当 verifier,在搜索树分叉中定位坏轨迹的 transition point,在错误前缀与正确后续之间插入 revision signal,把"反思加修正"实例做迭代 SFT;进入 policy 的是 revision trajectory 的文本 token,与 Policy Internalization 相邻,归此格的依据是其自评判断是修正数据得以构造的 load-bearing 环节。OpenClaw-RL [Wan26ad] 从用户话语或环境信号中抽取 directive textual hints,用 On-Policy Distillation 把 hint-enhanced teacher 与 student 的 log-prob gap 转成 token-level directional update;该方法同时辅以 sequence-level binary RL on scalar reward,此处仅讨论其 generative process 一侧。

### 6.1.5 Discussion

Evaluator-Driven Optimization 整体带来三种有别于直接监督的好处。第一,评估器把"什么样的输出更好"的判断离线压缩进权重,可以脱离原始轨迹被反复调用——采样、过滤、对比的边际成本都低,这是 RLHF 工具链能横向扩展的根本前提。第二,在 non-verifiable 任务上——开放对话、长程 search、多维 agentic 行为——环境本身无法给出 clean reward,评估器是把"难以量化的偏好"转成可优化训练信号的唯一手段;rule-based verifier 只在数学、code、game 等任务上成立,P6 覆盖了 verifier 失效的广阔区域。第三,评估器作为质量门可以吸收原始轨迹的噪声,policy 拟合的是经评估器筛选或排序后的较清洁子集,而非带噪示范本身。

代价集中在评估器与目标之间的失配。当 policy 持续针对一个固定且 imperfect 的评估器优化,它会逼近评估器的偏差而非真实目标,这是 reward hacking 的统一根源,在 scalar 与 critique、outcome 与 step 各种形式下都会出现。文献中三类应对各占其位——co-evolution 让评估器随 policy 更新 [Yua24, Wu24d, Li26l]、ensembling 与 routing 用多评估器分散单点偏差 [Wu25x, Xu24d]、regularization 与 filtration 约束优化过程 [Ack26, She24c];三者都只能缓解,不能从原理上消除。评估器质量直接构成 policy 能力的上界:错误的 critique 比错误的 scalar 更具误导性,判别式信号至少可以用 held-out 偏好一致性间接核验,生成式步级 critique 的正确性目前仍依赖人工或更强模型校验。

与 Policy Internalization 相比,Evaluator-Driven Optimization 的特征是监督经过一层有损中介。Policy Internalization 把原始轨迹、示范或环境成功信号直接写入 policy,信号是 grounded 的,但噪声直接传递;Evaluator-Driven Optimization 在轨迹与 policy 之间插入一个参数化评估器,信号经折射后更稳定、更具可比较性,代价是 grounding 被抹除一层——policy 学到的是"评估器认为什么是好",而非"环境认为什么是好"。两条路径的适用面互补:在环境信号可靠且充足时 Policy Internalization 更直接,在环境信号稀疏、嘈杂或难以量化时 Evaluator-Driven Optimization 通过评估器把零散信号聚合为可训练监督。两者也常被串接成 P4 → P6 形式——Evaluator Internalization 产生评估器,Evaluator-Driven Optimization 用评估器训练 policy——构成完整的 evaluator-based pipeline,具体复合形态由 §7 讨论。

路径内部的两条划分轴反映两种独立的张力。粒度轴(outcome vs process)关乎"评估落在多大的单位上",决定 credit assignment 的精度——outcome 粒度信号简单但 long-horizon credit 粗糙,process 粒度提供 dense supervision 但 step-label 的可靠性与一致性更难保证。形态轴(discriminative vs generative)关乎"评估以什么形式表达",决定信息密度与可验证性的折中——判别式信号密度低但可比较、易于过滤与排序;生成式信号密度高但难以核验,且与 refined trajectory 等 tokenized 载体的边界模糊,常使方法在归属上接近 Policy Internalization 或 Parametric Externalization。两轴的演化方向是评估器从判别走向生成、从 outcome 走向 process——从回答"好不好"转向回答"为什么不好、应如何改",这一转向提升监督的信息密度,代价是把"评估器自身的可靠性如何保证"推到前台。

## 6.2 Parametric-to-Tokenized Transformation (Parametric Externalization)

Parametric Externalization 把已内化在参数化模型权重中的经验外化为可被其他系统消费的 Token-level artifacts。源端是 Policy 或 Evaluator 参数(承载这些参数的模型可由任意 modality 实现,LLM、VLM、VLA 均可),目标端是 agent trajectories、tool-use demonstrations、GUI action traces、step-level labels、critiques、preference annotations 等 Tokenized 载体。Parametric Externalization 与 Policy Internalization 方向相反——Policy Internalization 把离散经验写入参数,Parametric Externalization 从参数中读出可复用的经验表达。

Parametric Externalization 仍是 representation-to-representation pathway:外化出的 trajectory 并非凭空产生,它重新编码了曾经经由 Evaluator Internalization 或 Policy Internalization 写入参数的经验语义,满足经验语义锚定与经验内容承载两个条件。与其余六条转化路径不同的是 source 端的形态——Latent-Space Transformation 的 source 是一条确定 trajectory,转化算子是确定性的 re-encoding;Parametric Externalization 的 source 是参数这种聚合态表示,贡献它的多条原始 trajectory 已在权重分布中彼此叠加、无法再被个别定位,转化算子相应地包含一次采样:$\mathcal{T}$ 从 $p(e \mid \text{prompt}, \text{env})$ 中抽取样本,而非对某个给定的 $e$ 做重编码。

source 的聚合-采样性质决定 Parametric Externalization 的两个组织性事实。采样有方差,低质量样本必须由 verifier 或 filter 在事后剔除,因此 Parametric Externalization 方法几乎无一例外地挂载验证环节;采样可重复进行并保留最优样本,这带来 best-of-N 效应——在筛选后的 teacher 数据上训练的 student,其可靠性可以高于 teacher 单次采样的平均水平。

按外化经验在下游系统中的消费角色,Parametric Externalization 分为两类:Demonstration Externalization(§6.2.1)外化"如何行动",来自 Policy 参数;Evaluative Supervision Externalization(§6.2.2)外化"如何评价",来自 Evaluator 参数。两类的分界线在于 Evaluator 判断的去向——判断被物化为独立、可复用的监督数据则归后者,判断仅作为内部过滤开关则仍是前者内部的质量控制机制。

### 6.2.1 Demonstration Externalization

Demonstration Externalization 把参数化 Policy 或 teacher agent 的隐式决策能力外化为可供 student 模仿学习的行为示范——agent trajectories、tool-use dialogues、web/GUI/mobile interaction traces、reasoning-action paths。下游 consumer 通过 SFT、behavioral cloning 或 imitation-style training 吸收这些示范;消费方式是 SFT 还是 RL 不改变 artifact 的载体属性,归类依据是外化 artifact 本身的形态。

下文以**环境合成度**为组织轴。它锚定在四元组的 observation $o$ 上:$o$ 越是来自真实环境的客观返回,外化轨迹的 grounding 越强;$o$ 越是由模型自身生成,轨迹越接近一次纯参数读出。沿这条轴,pseudo-success 与 hallucinated observation 的风险递增,verifier 的必要性也相应递增。

**真实环境锚定。** Teacher 在真实网站、真实 MCP server 或真实操作系统上交互,$o$ 是环境返回的客观后果。在 web 域,Explorer [Pah25] 让 GPT-4o 在真实网页中以 exploration-driven 方式自主发现任务、执行多步交互,经 proposer/refiner/summarizer/verifier 流水线产出带页面状态、动作序列与任务总结的 multimodal trajectories;InSTA [Tra25] 将这一思路推至 internet scale,使强模型在大规模真实网站上自动提任务、执行操作并生成 reasoning traces;AutoSurfer [Fai26] 先系统性 surf 真实网站、识别功能空间,再整理为含页面状态、动作历史与推理的 task tuples;SynthAgent [Wan25ar] 在目标网站上做 element-level exploration 与任务合成、再于收集后全局 refine;A3-SYNTH [Lu26] 以 Agent-as-Annotators 框架让 Gemini teacher 生成带结构化 reasoning block 的成功轨迹;[Log26b] 用 Llama 系列 teacher 在真实网页执行后,由 judge 抽取显式 constraints、按 constraint satisfaction rate 做 prefix extraction 与 hindsight relabeling,使部分成功轨迹也能转化为可训练样本——judge 在此主要承担质量控制,主产物仍是 trajectory prefix dataset。在计算机与移动端,Fara-7B [Awa25] 经 FaraGen 产出 screenshot-thought-action trajectories 并由三重 verifier 筛选;OpenMobile [Che26d] 以 expert 接管修正 learner 偏差、把 corrected trajectories 与 step-level CoT 一并保留,因任务合成依赖前期 exploration trajectory 建立的环境记忆,与 §3 的同层转化接壤;AgentSynth [Xie25e] 在 OSWorld 等环境中先生成可验证的简单 subtasks 并执行验证,再总结为更长程的复合任务,保留完整 action trajectory、reasoning trace 与视觉证据。在工具与 MCP 域,TOUCAN [Xu25o] 在近 500 个真实 MCP environments 中让多个强模型合成任务并执行完整 tool-use rollouts,经 task-level 与 trajectory-level 双重过滤形成 1.5M 规模 tool-agentic corpus。一类与 seed demonstration 显式耦合的方法处于边缘:ANCHOR [Wei26b] 沿少量 high-quality seed trajectory 找到 branch point,在这些状态上让模型提出新任务并继续执行,形成共享前缀、后段分叉的树状 GUI 数据——后缀由模型新生成因此仍属 Parametric Externalization,但共享前缀来自既有 demonstration,与 §3 的 Narrative-to-Narrative 接壤。

**模拟环境合成。** 环境本身由模型扮演,observation $o$ 由 simulator 生成,失去了真实环境返回的客观性。这组工作在工具调用域最集中:ToolAlpaca [Tan23] 用 ChatGPT 分别扮演 user、assistant 与 tool executor,通过多智能体 simulation 生成工具使用轨迹;ToolMind [Yan25ab] 以 user/assistant/tool 三类 agent 的模拟产出带 reasoning 的多轮交互轨迹,并在 trajectory-level 与 turn-level 做细粒度过滤;ToolACE [Liu24o] 先做 Tool Self-Evolution Synthesis 扩充 API pool,再以 Self-Guided Dialogue Generation 合成多种复杂度的工具调用对话;APIGen-MT [Pra25b] 先生成 task blueprint 与 ground-truth action sequence,再经 simulated agent-human interplay 合成多轮 function-calling dialogues。在 mobile GUI 域,Learning with Challenges [Kan26b] 先对 student 做能力 profiling,再用 explorer、supervisor 与 synthesizer 等 VLM 角色在 emulator 中生成难度自适应的 goal-conditioned trajectory,通过 inverse synthesis 重建 thought 与 instruction。一组工作把"环境本体"作为主产物而非附属物:[Wan25as] 把 GPT-4o-mini 同时用作 world simulator 与 teacher agent,既产出 trajectory 又产出可扩展的 UI state-transition simulator;Mock Worlds [Lu26j] 用 teacher 从 persona 出发合成 workflow、虚拟 tool ecosystem 与 task rubric,核心消费方式是闭环 RL;ASTRA [Tia26] 从 tool document 与知识源出发,一条线产出 SFT trajectory、另一条线把 QA 对与工具实现编译成 sandbox-verifiable Python RL arena;[Xu26e] 在少量 seed trajectory 之上做 self-evolving generation 形成 base instance,再扰动 user query、tool set 与 tool output 构造 RL-ready mock 环境,其主产物是带 oracle 与 verifier metadata 的增强环境。后四者的 trajectory 产物均合法,但当 environment 与 rubric 同时构成论文的实质贡献时,这条路径与 §7 的复合 pipeline 接壤。

**构造式合成。** 此端几乎没有交互环境,trajectory 围绕预先给定的 answer、evidence 或问题结构反向构造,最接近一次纯参数读出。EviPath [Li25at] 从 gold evidence 反推 abductive reasoning path,再由强模型生成含 planning、sub-question decomposition 与 evidence-grounded answering 的 RAG trajectories;RAGShaper [Tao26] 构造带 distractor 的信息树与多跳问题,在受控检索环境中诱导强 teacher 产出 agentic RAG trajectories;APIGen [Liu24n] 让强模型基于真实可执行 API 生成自然语言 query 与结构化 function-calling answers,经 format、execution 与 semantic 三层检查筛选——保留了基于真实 API 的 execution check,但交互深度浅,整体偏生成而非交互。

以上方法的目标载体多为 Narrative trajectory,Demonstration Externalization 同样支持 Schematic 形态:FABRIC [Ver25b] 通过 LLM-only pipeline 生成 task description、tool definition、policy pseudocode、dialogue 与 execution trace,其中 policy pseudocode 与 task/tool schema 属于 Schematic Tokenized,构成 Parametric Externalization → Schematic 子格;TOUCAN 与 ToolACE 的 tool-call 部分同样含明显 Schematic 成分。

### 6.2.2 Evaluative Supervision Externalization

Evaluative Supervision Externalization 把参数化 Evaluator——judge、verifier、critic、reward model——的隐式评估能力外化为 Token-level supervision,供 student model、agent system、data filtering pipeline 或 reward-model training 消费。与 Demonstration Externalization 外化"如何行动"不同,这类方法外化的是"如何判断行动质量",目标 artifact 包括 critiques、step-level labels、action correctness annotations、progress labels、preference pairs、verification traces 与 failure diagnoses。

**步骤级正确性标注。** [He25g] 先用强 computer-use agent 生成 noisy trajectories,再由 o4-mini 对每一步做 correctness 与 optimality grading,附 screenshot analysis、action review 与 alternative analysis 等 reasoning-rich annotations;评估结果被物化为 WebSTAR 与 WebSCORE 两套独立数据资源,前者训练 student computer-use agent,后者蒸馏出轻量 StepRM。它同时外化 Policy 与 Evaluator 两端,evaluator 的判断被独立物化为 WebSCORE 与 StepRM 的内容主体,超出了通常的过滤开关角色。

**长程进展与过程结构。** Step-GUI [Yan25x] 先以轨迹级 verifier 建立质量锚点,再由强多模态 thinking model 把验证结果转写为 progress tracking、state summary、effect prediction、self-reflection、state verification、intent execution 与 action prediction 等七类结构化 step-level supervision,与原轨迹一道用于下一轮 cold-start fine-tuning 与 RLVR;产物主要回流到同一家族后继模型,self-training 耦合较强,与 §7 的复合 pipeline 接壤。

### 6.2.3 Discussion

Parametric Externalization 的核心优点是规模与可控性的双重突破。它用 teacher 的一次性推理成本换取近乎任意规模的监督数据,既绕开人工标注的吞吐瓶颈,又支持沿 curriculum、difficulty、domain coverage、failure pattern 等维度定向合成;verifier 在其中既吸收采样方差又通过 best-of-N 效应把 filtered student 的可靠性抬至 teacher 平均水平之上,这意味着 student 可以在稳定性维度超越 teacher 的"单次"输出,即使二者能力上界相同。能力专用化与推理成本压缩是另一类直接收益——昂贵的大 teacher 的能力可以蒸馏到一组轻量、领域专用的 student,代价是一次性合成成本而非持续的推理成本。

共同的根本约束是能力天花板:student 在任务能力维度上继承的是 teacher 的上界,Parametric Externalization 兑换的是成本、推理效率与领域专用化,而非能力前沿本身。其余代价大都从这一约束派生。teacher hallucination、伪成功轨迹与不可执行步骤会被 student 当作正确监督吸收,这一风险沿环境合成度轴递增——真实环境一端 verifier 校验任务成功即可,模拟与构造一端还需校验 observation 自身的可信度。distribution narrowing 是另一种衰减,单一 teacher 的表达风格与决策偏好会被放大,multi-teacher mixing 是常见缓解手段但不能根本消除。verifier 既是这条路径的支柱也是其最薄弱处——筛选信号本身可能不可靠,verifier 的 false positive 让伪成功漏入 student,false negative 让高质量样本被错杀;evaluation-grade verifier 与生成同等规模的 teacher 数据并行扩展,是这条路径目前的开放工程问题。

与其余六条路径相比,Parametric Externalization 在 source 形态上独一份。其余路径处理的是已经存在的经验——一条具体的 trajectory、一组确定的判断、一段写入参数的能力,转化是对已有经验的重表述、压缩或转化;Parametric Externalization 的 source 是参数这种聚合态表示,转化算子包含一次采样而非对已有 $e$ 的重编码。这一形态使它在 experience source 属性上承担一个独有角色——{teacher}-sourced experience 几乎全部经由这条路径进入语料,Parametric Externalization 正是制造 {teacher} 这一经验来源的工艺过程。

与 Policy Internalization 构成方向相反的对偶。Policy Internalization 把离散经验写入参数,Parametric Externalization 从参数中读出可复用的离散经验,两者常以 P7 → P5 形式串接:teacher 外化产生 student 训练数据,student 再做 internalization。与 Narrative Abstraction 和 Schematic Formalization 的区别同样落在 source 形态上——后两者输入是已存在的 trajectory、转化是对其重表述,产物受限于源 trajectory 的覆盖度;Parametric Externalization 输入仅为 prompt 或 task specification,产物的覆盖度由 teacher 能力与 prompt 设计决定,可任意扩展,代价是放弃原始 trajectory 自带的 environmental grounding。在 utilization 维度,Parametric Externalization 的产物几乎只服务一个目的——给 student 做 SFT 或 imitation learning;这与 Latent Compression 的产物(继续在同一 agent 内部消费)和 Evaluator Internalization 的产物(被 Evaluator-Driven Optimization 调用更新 policy)形成功能上的分工。

Demonstration Externalization 与 Evaluative Supervision Externalization 在 agent 系统中的功能分工对应 Policy 与 Evaluator 的角色分工。两者在下游训练管线中的位置互不替代:外化"如何行动"的产物用于训练 student policy,外化"如何判断"的产物用于训练 verifier、PRM 或 step-level critic;He25g 与 Step-GUI 这类同时外化两端的工作出现在两类下游管线交汇之处,它们的存在说明同一组 teacher 推理可以同时为两条管线供数据,但需要分别为 policy 与 evaluator 设计独立的 quality control。