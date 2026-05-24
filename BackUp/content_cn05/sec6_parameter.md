# §6 Parametric 源端转化（Parametric-Source Transformations, P6 + P7）

本章讨论以 Parametric 载体为源端的两条转化路径：P6（Evaluator → Policy，将已内化的评估经验转移到 Policy 参数中）与 P7（Parametric → Tokenized，将参数化经验外化为可被其他系统消费的 Token-level artifacts）。

## §6.1 Parametric Evaluator-to-Policy Transformation（P6）

P6 将已内化在参数化评估器中的评价经验转移到 Policy 参数中。源载体是 Evaluator parameter（reward model、PRM、verifier、critic、judge、value model 或 multimodal evaluator）；目标载体是 Policy parameter。与 P5（Tokenized → Policy）不同，P6 的监督源不是原始轨迹、人类示范或环境成功信号，而是某个参数化模型已学习或具备的评价能力。

P6 的关键特征是：评估器不只是被 Agent 在推理时调用，而是通过训练信号持久性地影响 Policy 参数。若一个 Evaluator 只在 decoding、reranking、tree search、best-of-N selection 或 MCTS 中作为推理时控制器使用，而 Policy 权重未被该信号更新，则它属于 evaluator utilization 而非 P6。只要 Evaluator 的输出被转化为 reward、preference pair、advantage、penalty、filtered trajectory 或 critique target 并用于更新 Policy 参数，就构成 Evaluator-to-Policy transformation。

本文按 Evaluator 产出的主要反馈形态划分 P6 方法：**Outcome Feedback-to-Policy Transfer**（完整输出的总体评价进入 Policy）、**Process Feedback-to-Policy Transfer**（中间步骤的局部评价进入 Policy）和 **Diagnostic Feedback-to-Policy Transfer**（解释性、修正性反馈被 Policy 吸收）。划分依据是真正驱动 policy improvement 的主要 feedback artifact，而非 Evaluator backbone 或训练算法的名称。

### §6.1.1 Outcome Feedback-to-Policy Transfer

Outcome Feedback-to-Policy Transfer 指 Evaluator 主要对完整输出、完整 trajectory 或完整 episode 进行评价，并将 outcome-level feedback 转移到 Policy 参数中。Evaluator 可以是 trained reward model、LLM-as-a-judge、VLM judge、generative reward model、preference model 或 mixture of judges。

这类 Evaluator 的输出表现为 scalar reward、trajectory-level score、pairwise preference、chosen/rejected label 或 success likelihood。这些 outcome-level signals 可通过 RLHF/RLAIF（PPO、GRPO、REINFORCE）、preference optimization（DPO、IPO、KTO）或 filtered distillation（RAFT、BOND、BoNBoN）等训练接口进入 Policy。

**AI Feedback 替代 Human Feedback。** Constitutional AI [Bai22b] 用 constitution-guided AI feedback 对完整 responses 做偏好判断，训练 preference model 再通过 RLAIF 将 harmlessness judgment 吸收到 policy 中。[Lee23b] 系统比较 RLHF 与 RLAIF，说明 off-the-shelf LLM 既可先提供偏好数据来训练 reward model，也可在 d-RLAIF 中直接对完整输出打 outcome-level 分数并驱动 RL 更新。

**在线化与自举化。** OAIF [Guo24] 让 LLM annotator 在线比较当前 policy 生成的完整 responses，在 on-policy 分布上直接构造 chosen-rejected pairs 供 DPO、IPO 或 SLiC 更新 policy。Self-Rewarding Language Models [Yua24] 让同一模型同时充当 generator 与 judge，对多个完整候选答案自评分后再以 iterative DPO 回灌到自身 policy。Meta-Rewarding Language Models [Wu24d] 加入 meta-judge，使 judge 的评分质量本身也能被迭代改进，形成 actor、judge、meta-judge 共同演化的 outcome feedback loop。[Luo25f] 把这一机制落到 computer-use 场景，用 GPT-4o 对完整候选操作结果打分，将所得 preference pairs 用于训练 UI-TARS-2B。

**Best-of-N Distillation 与 Filtered SFT。** RAFT [Don23] 用 reward model 对多个完整候选输出做 outcome ranking，仅保留高分样本进行 SFT，以 filtered distillation 的方式写入 policy。BOND [Ses24] 试图把推理时的 Best-of-N selection distill 为单次采样 policy，通过分布匹配让模型吸收 reward model 所支持的 outcome-level selection behavior。BoNBoN [Gui24] 从理论上刻画 Best-of-n 分布，结合 SFT-BoN 与 IPO-BoN 将最好样本和最差样本共同纳入训练。[Fis24] 显式训练 reward model，将其 reward difference 直接蒸馏到 policy 的隐式 reward 结构中。

**稳定性与去偏。** [Ack26] 将 reward hacking 解释为 policy 对 proxy reward 尖锐高点的利用，通过 gradient regularization 稳定 outcome-level RL 更新。[She24c] 提出 policy filtration，只让 reward model 最可靠的高分或低分样本进入训练。[Wu25x] 用 Bayesian router 在多个 trained reward models 间按 query 动态选路，将 routed preference pairs 用于 online DPO。[Xu24d] 以 Mixture of Judges 把多个 judges 对完整生成结果的约束判断注入不同 policy optimization 接口。[Ren26b] 用 meta-questions 让 LLM evaluator 对完整 responses 的目标答案概率形成 scalar reward，通过 CISPO 一类 GRPO 变体转化为 policy update。

Outcome Feedback-to-Policy Transfer 的优势是形式简单、适配性强，易与现有 RLHF、DPO 和 rejection sampling 框架结合。局限在于 evaluator 只评价完整结果，无法告诉 policy 中间哪一步导致了成功或失败；当 policy 反复优化同一个 imperfect evaluator 时可能出现 reward hacking、length bias 或 judge bias amplification。

### §6.1.2 Process Feedback-to-Policy Transfer

Process Feedback-to-Policy Transfer 指 Evaluator 主要评价 Agent 轨迹中的中间步骤、局部动作、reasoning prefix、tool-use step 或 state-action pair，并将 process-level feedback 转移到 Policy 参数中。核心动机是解决长程 Agent 学习中的 credit assignment 问题：仅依赖最终 reward 使 policy 很难知道应强化或避免哪些局部行为，process-level evaluator 则提供更细粒度的训练信号。

**错误定位驱动 Policy Update。** FAPO [Din25b] 训练 generative reward model 识别 answer-correct but process-flawed 的轨迹并定位 first incorrect step，将 flawed-positive diagnosis 写入 GRPO 的 penalty 设计。Stepwise Guided Policy Optimization [Che25v] 用 step-wise judge 顺序检查 reasoning trajectory，将正确前缀长度转化为 Reasoning Trajectory Score，替代 GRPO 对错误样本统一置零的粗粒度处理——即使在 all-negative groups 中，policy 也能从"哪条错误轨迹更接近正确路径"这一过程差异中获得有效更新信号。

**Turn-wise / Step-wise Value Learning。** SWEET-RL [Zho25p] 在 multi-turn collaborative reasoning agent 中训练 turn-level critic，利用 training-time privileged information 直接学习每轮 action 的 advantage，通过 DPO 将 turn-wise credit assignment 蒸馏进 policy。[Xu25h] 面向 non-verifiable 的 multi-turn search setting，引入 principle-based process reward model 对每个 turn 的 correctness、relevance 与 coherence 评分，通过 ReNorm 将 process reward 与 sparse outcome reward 统一校准后送入 GAE 和 PPO。[Wan26s] 在 GUI agent 中训练 Agentic-Q evaluator，对 state-action pair 估计 future return，把 step-wise value feedback 接入 SWPO 式更新。

**Dense Reward 从 Evaluator 内部解包。** [Cha24b] 不额外构造 process labels，而是直接利用 Transformer reward model 的 attention-based credit attribution，将 sequence-level scalar reward 分解为 token-level dense rewards，并送入 PPO 式 RLHF 更新。[Wan26ac] 用 LLM judge 按 retrieval utility 与 reasoning correctness 对各搜索轮次评分，将结果归一化为 round-level contribution weights 用于重分配 trajectory-level GRPO advantage。[Li26p] 将长程 GUI trajectory 分解为 milestones，通过 selector、verifier、reviewer 与 judge 组成的 critic framework 对中间进展逐步验证与校准，汇总为 online RL 的 reward signal。

这一路径与 Outcome Feedback-to-Policy Transfer 的区别在于反馈粒度：只要 Evaluator 的核心贡献是定位、评价或加权中间步骤，即使最终使用 GRPO 或 DPO 训练，也归入 Process Feedback-to-Policy Transfer。若 step-level 信息只为汇总出一个最终 trajectory score，而 policy 实际只接收完整轨迹偏好，则归入 Outcome Feedback-to-Policy Transfer。

### §6.1.3 Diagnostic Feedback-to-Policy Transfer

Diagnostic Feedback-to-Policy Transfer 指 Evaluator 主要输出解释性、诊断性、批评性或修正性反馈，并将这些 diagnostic feedback 转移到 Policy 参数中。与 Outcome Feedback 和 Process Feedback 主要提供"好不好"或"哪一步好不好"的评价不同，Diagnostic Feedback 更关注"为什么不好""哪里出了问题""应该如何修改"。

这类 Evaluator 的输出通常不是 scalar reward 或 pairwise label，而是 natural-language critique、failure explanation、error analysis、refinement suggestion、risk rationale、corrected step、revised trajectory 或 action directive。训练接口有多种形式：evaluator 先对失败轨迹生成 critique 或 refinement，再将修正后的 trajectory 作为 supervised target 训练 policy；将 diagnostic feedback 与原始 trajectory 拼接，训练 policy 在类似状态下生成更合适的 action；或让 evaluator 生成 rubric-based explanation，将诊断信息转化为 preference pairs 或 auxiliary loss。

**Step-wise Diagnosis 与 Refinement Tuning。** SRR-Judge [Zha26am] 面向 search agent 的每个 thought-action step 同时生成评分、错误解释以及 refined thought 和 refined action，将修正后的高质量轨迹用于多轮 rejection-sampling fine-tuning。Natural Language Actor-Critic [Hon25c] 用 language successor model 预测未来 rollout 摘要，再由 language evaluator 生成带理由的 textual critique 和 optimality judgment，据此产生 refined action 蒸馏回基础 policy。OpenClaw-RL [Wan26ad] 从 next-state signal 中抽取 hindsight hints，将环境回应中的纠错信息转化为 concise action directives，通过 Hindsight-Guided On-Policy Distillation 将 conversational correction 转化为 token-level directional update。

**Failure-Driven Reflection 与修正内化。** Agent-R [Yua25c] 通过搜索树中的分叉结构定位 failed trajectory 的 first error step，在错误前缀与正确后续之间插入 revision signal，构造 reflection-plus-revision training instances。模型随后以迭代 SFT 的方式学会在多轮交互中主动识别错误并切换到修正后的行动路径。AgentRefine [Fu25d] 构造 multi-turn error-refine trajectories，由强模型针对 parameter error、logical error 和 location error 给出诊断性反馈并展示 refined action，训练时仅对修正步骤计算损失。

**Critic Co-Evolution 与边界案例。** [Li26l] 训练与 actor 同步演化的 linguistic critic，为开放世界 Agent 的失败轨迹生成 natural-language critiques 并诱导 refined trajectories，既是 Diagnostic Feedback-to-Policy Transfer 的强实例，也体现了 evaluator–policy co-evolution 的前沿形态。[Pan24b] 使用 multimodal evaluator 给出 success/failure/progress 判断，但参数更新阶段主要利用 evaluator 过滤出的高质量 state-action pairs 进行 behavior cloning，诊断文本更多用于 test-time reflection，适合作为边界案例。[Zho24e] 先让强 LLM 生成 language feedback 再蒸馏为 Language Feedback Model，policy 主要吸收经 evaluator 过滤后的行为数据而非 critique 文本本身。[Din26e] 的 task-adaptive rubrics 虽为 trajectory 提供多维诊断结构，真正进入 DPO 或 PPO 的主要仍是结构化 score 与 filtering outcome。

Diagnostic Feedback-to-Policy Transfer 的优势是信息密度高、可解释性强，更适合错误类型复杂、任务空间开放的 Agent 场景。核心趋势是：评估器不再只回答"好不好"，而是 increasingly 以自然语言或修正轨迹的形式回答"为什么不好"以及"应如何改"。

## §6.2 Parametric-to-Tokenized Transformation（P7）

P7 将已内化在参数化模型权重中的经验外化为可被其他系统消费的 Token-level artifacts。参数化源可以是 Policy model、teacher foundation model、LLM/VLM/VLA agent，也可以是 Evaluator model（reward model、verifier、critic、judge）。与 P5（Tokenized → Policy）方向相反，P7 的方向不是把离散经验写入模型参数，而是从模型参数中"读出"可复用的经验表达。

在 LLM-based Agent 场景中，P7 的目标不是生成一次性回答，而是生成可被另一个 student model、retrieval store、agent system 或下游训练管线继续消费的 Tokenized artifacts——agent trajectories、tool-use demonstrations、GUI action traces、step-level labels、critiques 或 preference annotations。P7 将模型权重中隐式保存的任务执行能力或评估能力外化为可存储、可筛选、可训练、可检索或可组合的数据资源。

P7 需与普通 inference、self-training loop 及 P1/P2 路径区分。普通 inference 中模型生成的 CoT 或答案仅服务于当前 query，缺乏独立归档和复用意图，不构成 P7。Self-training 或 iterative bootstrapping 中模型自身生成的 rollouts 被同一训练循环的后继版本直接消费，更接近 composite pipeline。P1/P2 以已有 logs、trajectories 或 demonstrations 为主要输入；P7 的关键在于源经验主要来自参数化模型已内化的能力，而非某条已存在的 Agent trajectory。

本文按外化 artifact 在下游系统中的主要消费角色将 P7 方法划分为两类：**Demonstration Externalization**（外化"如何行动"的经验）和 **Evaluative Supervision Externalization**（外化"如何评价"的经验）。

### §6.2.1 Demonstration Externalization

Demonstration Externalization 指参数化 Policy、teacher foundation model 或 teacher agent 将其隐式决策能力外化为可供 student agent 模仿学习的行为示范。目标 artifact 通常是 agent trajectories、task demonstrations、tool-use dialogues、web/GUI/mobile interaction traces 或 reasoning-action paths。下游 consumer 通过 SFT、behavioral cloning 或 imitation-style training 学习这些示范数据。

强模型或 teacher agent 已在参数中内化了一定的任务执行能力，但这些能力若只停留在模型权重中便难以被小模型、专用 agent 或独立系统直接复用。Demonstration Externalization 通过任务提示、环境交互、tool schema、GUI state 或 retrieval context 诱导 teacher model 产生完整的行为过程，将"模型会做什么"转化为"学生可以学习的数据"。

**Web 与 Computer-Use 场景。** Explorer [Pah25] 通过 exploration-driven 流水线让 GPT-4o 在真实网页中自主发现任务并执行交互，再由 proposer、refiner、summarizer 与 verifier 生成带页面状态、动作序列与任务总结的 multimodal trajectories。InSTA [Tra25] 将这一思路扩展到 internet scale，使强模型在大规模真实网站上自动提出任务、执行网页操作并生成 reasoning traces。Structured Distillation of Web Agent Capabilities [Lu26] 通过 Agent-as-Annotators 框架生成带结构化 reasoning blocks 的成功轨迹。SynthAgent [Wan25ar] 在目标网站上先做 element-level exploration、任务合成与轨迹重写，生成更贴合特定站点分布的 synthetic supervision。AutoSurfer [Fai26] 先系统性 surf 网站、识别功能空间，再整理为包含页面状态、动作历史与推理的 task tuples。Fara-7B [Awa25] 利用 FaraGen 生成大规模 screenshot-thought-action trajectories，通过多重 verifier 筛选高质量 demonstrations。OpenMobile [Che26d] 通过 expert 接管修正 learner 偏差，保留 corrected trajectories 与 step-level CoT 作为训练数据。Learning with Challenges [Kan26b] 根据 student 的能力边界生成难度自适应的 mobile GUI demonstrations。

**Tool-Use 与 Function-Calling 场景。** TOUCAN [Xu25o] 在真实 MCP environments 中让多个强模型合成任务并执行完整的 tool-use rollouts，通过 task-level 与 trajectory-level 双重过滤形成大规模 tool-agentic corpus。ToolMind [Yan25ab] 通过 user agent、assistant agent 与 tool agent 的多智能体模拟生成带 reasoning 的多轮交互轨迹。APIGen-MT [Pra25b] 先生成 task blueprint 与 ground-truth action sequence，再通过 simulated agent-human interplay 合成多轮 function-calling dialogues。更早的 ToolAlpaca [Tan23] 已展示通过多智能体 simulation 生成工具使用轨迹并据此微调 student 模型的基本范式；APIGen [Liu24n] 与 ToolACE [Liu24o] 分别从可验证函数调用样本生成与复杂 API orchestration 对话合成两个方向推进了这一谱系。

**RAG Agent 场景。** RAGShaper [Tao26] 通过构造带 distractor 的信息树与多跳问题，诱导强 teacher 在受控检索环境中生成包含 thought、retrieval action、observation 与 final answer 的 agentic RAG trajectories。From Evidence to Trajectory [Li25at] 从 gold evidence 反推 abductive reasoning path，再由强模型生成包含规划、子问题分解与 evidence-grounded answering 的 RAG trajectories。

Demonstration Externalization 的优势在于可扩展性和低人工成本，能缓解 agent training data 的稀缺问题。风险在于 teacher-generated trajectories 可能包含 hallucinated actions、不可执行步骤或伪成功轨迹；单一 teacher 可能导致 distribution narrowing，使 student 过度拟合 teacher 的表达风格和决策偏好。

### §6.2.2 Evaluative Supervision Externalization

Evaluative Supervision Externalization 指参数化 Evaluator、judge、verifier、critic 或 reward model 将其隐式评估能力外化为 Token-level supervision，供其他 student model、agent system、data filtering pipeline 或 reward-model training process 使用。不同于 Demonstration Externalization 外化"如何行动"的行为知识，这类方法外化的是"如何判断行动质量"的评价知识。

目标 artifact 包括 critiques、step-level labels、action correctness annotations、progress labels、preference pairs、verification traces、failure diagnoses 或 trajectory refinement comments。只要 Evaluator 的输出被物化为可复用 Token-level artifact 并被另一系统消费，就属于此类。

**步骤级评估信号的显式外化。** [He25g] 先用强 computer-use agent 生成 noisy trajectories，再由 o4-mini 对每一步进行 correctness 与 optimality grading，附带 screenshot analysis、action review 和 alternative analysis 等 reasoning-rich annotations。评估结果被物化为 WebSTAR 与 WebSCORE 等数据资源，前者用于训练 student computer-use agent，后者进一步蒸馏出轻量 StepRM。[Lu25e] 以 GPT-4o 作为 step verifier，比对动作前后界面状态，为每一步生成 binary correctness label 与 verification reasoning，据此构建 step-verified trajectory data 并通过 KTO 训练开源 student agent。

**长程任务进展判定。** [Log26b] 从 web task 中抽取显式 constraints，在轨迹每一步评估 constraint satisfaction state，形成细粒度的 CSR progress signal，据此执行 prefix extraction 与 hindsight relabeling，使部分成功轨迹也能转化为可训练样本。[Yan25x] 先以轨迹级 verifier 建立质量锚点，再由强多模态模型将验证结果转写为 progress tracking、state summary、effect prediction、self-reflection 等七类结构化 step-level supervision。

Evaluative Supervision Externalization 需与 P6 区分：P6 的核心是 Evaluator 的 reward、preference 或 critique 直接参与 Policy 优化，使 Policy 参数发生更新；P7 强调 Evaluator 的输出被显式物化为 Tokenized artifacts，且可脱离原 Evaluator 被其他系统复用。此外，许多 Demonstration Externalization 方法用 judge 或 verifier 删除低质量轨迹，但若 judge 的输出只作为内部过滤开关而非独立监督数据被保存，则只是质量控制机制——只有当 Evaluator 的判断本身成为可复用 artifact，才应归入此类。

### §6.2.3 小结

Demonstration Externalization 与 Evaluative Supervision Externalization 构成 P7 的两条主线：前者将 Policy 或 teacher model 的决策能力外化为 trajectories 和 demonstrations，强调"应该如何行动"；后者将 Evaluator 或 judge model 的评估能力外化为 labels、critiques 和 verification traces，强调"如何判断行动质量"。前者主要服务于 student agent 的行为模仿与能力蒸馏，后者主要服务于数据筛选、细粒度监督和 verifier 训练。

两类方法在实际系统中并非完全孤立——许多 agent data synthesis pipeline 同时包含 teacher rollout 和 evaluator filtering。主分类取决于论文的核心贡献和最终被下游消费的主要 artifact。此外，P7 方法还存在若干横向设计维度：environment-mediated synthesis、multi-teacher mixing、curriculum control、difficulty-aware sampling、execution-based verification、step-level filtering 和 human-in-the-loop screening，这些机制不构成独立的外化目标，而是影响外化 artifact 的质量、规模、多样性和可验证性。








