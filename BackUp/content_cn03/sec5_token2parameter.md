# §5 Tokenized 到 Parametric 转化（Tokenized-to-Parametric Transformations, P4 + P5）

本章讨论经验从 Tokenized 载体向 Parametric 载体转化的两条路径：P4（Tokenized → Evaluator，经验固化为评估能力）与 P5（Tokenized → Policy，经验固化为决策能力）。两条路径共享同一源端类型，区别在于目标载体的功能角色——Evaluator 参数回答"如何判断行为质量"，Policy 参数回答"如何生成行为"。

## §5.1 Tokenized-to-Evaluator Transformation（P4）

P4 将 Tokenized Agent Experience 内化为参数化评估器。Tokenized experience 包括 agent trajectory、reasoning trace、tool-use log、action history、preference pair、execution outcome、failure annotation 等。通过训练，这些离散经验中的评价语义被写入 Evaluator 参数，形成可复用的评估能力。训练后的 Evaluator 表现为 outcome reward model、process reward model、verifier、critic、judge、value model、failure detector 或 diagnostic feedback model。

P4 与 prompted LLM-as-a-judge 有本质区别：prompted judge 仅在推理时通过 prompt 激发现有模型的评估能力，参数不发生训练更新；P4 要求 Evaluator 的参数发生实质性变化——评价能力被经验数据显式内化进模型参数。

本文按训练后 Evaluator 向 Agent 提供的监督信息形式组织方法：**Outcome-supervised Evaluator Internalization**（学习完整轨迹上的全局评估信号）、**Process-supervised Evaluator Internalization**（学习中间步骤上的过程性评估信号）和 **Diagnostic-feedback Evaluator Internalization**（内化 critique、error diagnosis、rationale 等更丰富的语义反馈）。

### §5.1.1 Outcome-supervised Evaluator Internalization

Outcome-supervised evaluator internalization 训练 Evaluator 对完整输出、完整轨迹或完整 episode 给出全局判断。监督信号被分配在 outcome level：任务是否完成、最终答案是否正确、两个完整 response 哪一个更好，或一条完整 trajectory 在某个 reward 或 quality criterion 下是否更优。训练后的 Evaluator 将一个完整候选行为映射为 global scalar 或 scalarizable signal。

主要优势是 outcome-level label 通常比 dense process label 更容易获得。对于具有明确最终答案、显式成功标准或 human/AI preference comparison 的任务，outcome supervision 可直接对齐最终任务目标。主要局限是 credit assignment 较弱——一条失败轨迹可能包含许多有价值的中间决策，一条成功轨迹也可能包含偶然有效但并不稳健的推理或动作，将整条轨迹压缩为单一标签容易掩盖哪些动作应该被强化、哪些应该被修正。

**Generative Judge 与 Reward Model 方向。** Generative Reward Models [Mah24b] 将 reward modeling 重写为 next-token generation，让 Evaluator 对完整 response pair 直接生成 preference verdict，并通过 CoT 自举把能导向正确 verdict 的 reasoning pattern 内化为参数。S2J [Sun25l] 进一步指出 generative reward model 存在 solving ability 与 judging ability 的落差，要求 Evaluator 在判断前先自行求解，再用 solving reward 与 judging reward 的联合 RL 目标更新参数。J4R [Xu25i] 用 EIS-GRPO 训练 pairwise judge，通过 response order swap 等等价初始状态上的 judgment correctness 驱动 RL，学到更稳定、更少位置偏差的全局比较能力。

**Web 与 Computer-Use 方向。** WebRL [Qi24] 在自进化 RL 框架中训练 outcome-supervised reward model，使 Evaluator 根据用户指令、历史动作与最终网页状态判断整条 web trajectory 是否完成任务。Video-Based Reward Modeling for Computer-Use Agents [Son26d] 训练 Execution Video Reward Model，仅基于 user instruction 和 execution video sequence 判断完整 trajectory 的 success or failure。Vision-Language Models as Success Detectors [Du23] 通过 SuccessVQA 微调 Flamingo 学习 episode-level success semantics。

**Embodied 方向。** RL-VLM-F [Wan24l] 先让 foundation model 对 observation image pair 产生偏好标签，再训练参数化 reward model 吸收这些 pairwise visual preferences。VLP [Liu25w] 学习 trajectory-wise vision-language preference model，通过 ITP、ILP 与 IVP 三类 language-conditioned trajectory preference 把不同质量轨迹的全局排序关系内化为 Evaluator。Video-Language Critic [Ala24] 从 video-caption 对齐与成功轨迹的时间排序中学习对 partial video history 输出标量分数的 critic。LIV [Ma23d] 从 action-free video 与 language annotation 中联合学习 language-image representation 与 reward-like value function。RoboReward [Lee26b] 与 Large Reward Models [Wu26e] 进一步扩大数据与任务覆盖：前者通过 counterfactual relabeling 和 negative clipping 自动扩展 episodic reward dataset；后者利用大规模无标签视频的时间单调性，学习 temporal contrastive reward 与 task completion reward。

### §5.1.2 Process-supervised Evaluator Internalization

Process-supervised evaluator internalization 训练 Evaluator 对中间推理步骤、动作前缀或单个 Agent decision 提供局部监督。与 outcome-supervised evaluator 不同，这类方法不是在完整 trajectory 上分配整体得分，而是在 step、state、prefix、tool call、code edit、GUI action 或 web-navigation decision 等局部位置学习评价信号。

核心动机是：Agent 失败通常不是最后一步的突然事件，而是一系列局部错误的累积。Process-supervised evaluator 试图解决 credit assignment 问题——不仅判断最终 outcome 是否成功，还判断每个中间决策是否正确、是否有希望、是否推动任务进展。

**Reasoning PRM 谱系。** Let's Verify Step by Step [Lig23] 最早系统确立了这一范式，用人工 step annotation 训练 PRM 对每个 reasoning step 给出 positive、negative、neutral 判断。OmegaPRM [Luo24] 通过 rollout 与 binary search 自动定位 first error，把前缀的可完成性转成 soft process label。Rewarding Progress [Set24] 将目标从 step correctness 改写为 step-level advantage，评估该步骤是否真正提高未来成功概率。PQM [Li24m] 将 PRM 训练目标从独立分类改为 Q-value ranking，要求正确推理步骤随过程推进呈现更高价值而错误步骤导致显著价值断裂。PathFinder-PRM [Pal25] 先区分 math error 与 consistency error 再汇总为最终 reward judgment。BiRM [Che25s] 联合学习 reward 与 value 两个头，使 Evaluator 同时编码"当前步骤是否好"与"当前前缀未来是否还有希望"。

**Agentic PRM 扩展。** AgentPRM [Xi25b] 将 reasoning PRM 推广到多步 Agent 决策，用 Promise 和 Progress 分别建模 action-value 与 advantage，通过 TD 与 GAE 从 rollout 自动估计 step-wise pseudo-label。ProgRM [Zha25z] 学习每一步对 GUI 任务完成度的 progress value，通过 LCS-based self-annotation 从成功轨迹中自动抽取关键步骤与相对进度。Building Autonomous GUI Navigation via Agentic-Q Estimation [Wan26s] 训练 step-wise 的 Agentic-Q evaluator，把最终成功信号向前传播到 state-thought-action 三元组。GUI-Shepherd [Che25h] 训练 step-level binary PRM，对 state-action 对直接输出 positive 或 negative judgment，同时服务于 candidate action reranking 与在线 RL 的 dense reward。Advancing Mobile GUI Agents [Dai25] 采用 pairwise process preference 训练 generative verifier，在每一步把正确动作与若干错误动作拉开分数差距。

**Computer-Use、Code 与其他领域。** IntentScore [Che26s] 训练 intent-conditioned action evaluator，对 state-action-intent 三元组输出 per-step correctness score，以极低延迟完成 test-time reranking。GAIA [Wan26p] 通过 data flywheel 持续纳入真实 GUI agent 的错误分布，训练 step-level binary critic。SWE-Shepherd [Dih26] 面向 code agent，把读文件、编辑、执行测试等中间动作转化为 heuristic progress reward 并据此训练 PRM。

这一分支的演进路径相当清晰：早期工作先在 reasoning 中证明 step-level evaluator 的必要性 [Lig23, Luo24]，随后把局部监督从 correctness 扩展为 advantage、Q-value 与 hierarchical reward semantics [Set24, Li24m, Pal25, Che25s]，再在 GUI、computer-use 与 code agent 中把这些抽象过程信号落地为与环境状态变化、任务推进和动作后果直接对齐的 Evaluator [Che25h, Dai25, Xi25b, Zha25z, Che26s, Wan26p, Wan26s, Dih26]。

### §5.1.3 Diagnostic-feedback Evaluator Internalization

Diagnostic-feedback evaluator internalization 训练 Evaluator 产生更丰富的语义反馈，而不仅是 scalar 或 scalarizable score。目标输出包括 natural-language critique、error diagnosis、failure explanation、verification rationale、risk analysis 或 repair suggestion。这类 Evaluator 不仅判断 Agent 行为是好是坏，还解释为什么有问题以及应该如何修正。

在复杂 Agent setting 中，单纯的 reward score 往往不足以支持有效自我修正：一个分数可以告诉 Agent 某个动作不好，却未必指出违反了什么约束、基于了什么错误假设，或应该考虑什么替代动作。Diagnostic-feedback evaluator 通过内化更具解释性和行动指导性的反馈，弥补 scalar reward 的信息不足。

**Robotic Failure Detection 与 GUI Critic。** AHA [Dua24] 将 robotic failure evaluation 从单纯的 success/failure classification 改写为 free-form failure reasoning task，训练 VLM 为 replanning 和 reward refinement 提供可解释的诊断反馈。Self-Refining VLM for Robotic Failure Detection [Qi26] 训练 ARMOR 同时输出 binary failure detection 和 open-ended failure reasoning，通过 iterative self-refinement 提升 failure explanation 质量。OS-Oracle [Wu25m] 将 GUI critic 建模为"rationale generation + yes/no judgment"的统一任务，通过跨平台正负样本合成与 CP-GRPO 训练 critic。GUI-Critic-R1 [Wan25q] 是一个 pre-operative critic，在动作执行前生成 observation analysis、possible result、critique、correctness score 和 corrective suggestion，直接承担 pre-action diagnosis 和 repair guidance。

**Web、Code 与 General Reasoning。** WebArbiter [Zha26ab] 将 web-agent evaluator 设计为 principle-guided generative PRM，先诱导与当前网页任务相关的 principles，再生成 structured justification 和最终 verdict。Web-Shepherd [Cha25b] 将 web-agent process evaluation 扩展为 checklist-grounded generative judging。SOLE-R1 [Sch26] 训练 video-language reward model 同时输出自然语言 reasoning 与 dense progress estimate，显式说明当前状态是前进、停滞还是倒退以及尚缺失的子目标。Teaching Language Models to Critique via Reinforcement Learning [Xie25c] 训练 code critique model 输出 analysis、actionable improvement suggestions 和 final judgment，以"下游修复后代码是否通过 tests"作为 RL 信号。DeepCritic [Yan25u] 对 reasoning trajectory 的每一步生成长文本 critique 与 first-error localization。RL4F [Aky23] 训练 critique generator 输出自然语言反馈，用"反馈是否帮助固定模型修复输出"作为 PPO 奖励。

Diagnostic-feedback evaluator 的主要优势是信息密度高、可解释性强，适合错误类型复杂、任务空间开放的 Agent 场景，也有助于跨任务迁移——"未验证工具返回结果""忽略用户约束""过早停止搜索"等诊断可能在不同任务中重复出现。但可靠性问题也更突出：自然语言 critique 可能听起来合理但实际错误，refinement suggestion 可能与环境真实反馈不一致。在高风险任务中，diagnostic feedback 通常需要与环境验证、程序执行或 human audit 结合使用。

## §5.2 Tokenized-to-Policy Transformation（P5）

P5 将离散化的 Agent Experience 转化为 Policy/Actor 参数。源经验表现为自然语言轨迹、工具调用记录、代码编辑历史、GUI 操作序列、web browsing traces、reasoning chains 等 Tokenized artifacts；目标是将这些经验内化到模型参数中，使模型在后续任务中不必显式检索、拼接或重放原始经验，也能表现出更强的序贯决策能力。

从经验转化角度看，P5 的核心不是简单地"训练一个更强的模型"，而是回答：Agent 在交互过程中形成的离散经验，如何被组织为训练信号并改变 Policy 的参数化决策能力？与 P1 或 P2 不同，P5 的目标载体不再是可读的文本、规则、程序或工作流，而是模型内部的 Policy weights。经验一旦内化进参数，后续调用成本低，不受上下文窗口限制，但经验的显式可追踪性与局部可修改性会下降。

本文将 P5 按经验内化逻辑划分为三类：**Imitation-based Policy Internalization**（模仿高质量轨迹）、**Reward-based Policy Internalization**（利用可验证奖励优化）和 **Preference-based Policy Internalization**（构造轨迹偏好并优化）。三类方法在经验来源、监督信号形态和能力边界上各有差异。

### §5.2.1 Imitation-based Policy Internalization

Imitation-based Policy Internalization 将高质量 Agent trajectories 直接作为监督示范，通过 behavior cloning、SFT 或 rejection-sampled fine-tuning 训练 Policy。基本假设是：若一组轨迹已体现有效的任务解决行为，模型可以通过模仿其中的动作选择、推理模式、工具调用习惯或 GUI 操作序列，将相应经验内化进参数。

在这类方法中，环境反馈或任务结果通常不直接作为优化目标，而是用于筛选、清洗、重构或标注训练轨迹。系统可从多条候选 trajectories 中保留成功完成任务的轨迹，也可根据执行结果过滤无效工具调用或失败代码修改——feedback 主要扮演 data selection 或 data construction 的角色。

**基于 success filtering 的直接模仿。** 一部分工作主要依赖 success filtering，将完成任务的 trajectories 直接转化为可模仿的监督样本。Large Language Models Can Self-Improve At Web Agent Tasks [Pat24] 通过 environment error 与 self-critique 过滤 self-generated web trajectories，再进行 supervised self-improvement。AppVLM [Pap25b] 在 AndroidWorld 中保留成功 rollout，继续以 SFT loss 进行迭代更新。Training Software Engineering Agents and Verifiers with SWE-Gym [Pan24] 利用 unit-test outcome 从 software engineering trajectories 中筛选成功样本，通过 rejection-sampling fine-tuning 完成 policy update。

**基于轨迹重构与增强的模仿。** 另一部分工作更强调在参数更新之前对 trajectory 本身进行重构或增强，以提高 imitation signal 的质量与覆盖范围。AndroidGen [Lai25d] 利用 StepCritic 将 Android trajectories 分解为 subgoals，结合 trajectory augmentation 扩展高质量示范。WebCoT [Hu25i] 将 reflection、branching 与 rollback 中隐含的推理过程重构为显式 Chain-of-Thought，使 reasoning 与 action 能被联合模仿。NNetNav [Mur24b] 通过 hindsight relabeling 将 exploratory browser interaction 转化为 instruction-conditioned demonstrations。AgentTrek [Xu24] 将 web tutorials 转写为可执行的 procedural guidance，通过 guided replay 合成 demonstrations。Explorer [Pah25] 与 Go-Browse [Gan25b] 先通过结构化网页探索生成并验证 success trajectories，再将其蒸馏为学生模型的监督数据。AgentTuning [Zen23d] 将多个环境中的 GPT-4 agent trajectories 统一为 thought-action supervision 用于 generalized agent tuning。

Imitation-based 方法特别适合 Agent 的 cold-start training，能快速教会模型任务格式、动作空间、输出协议和基本交互流程。能力上限通常受示范轨迹质量与覆盖范围限制：若训练数据只包含有限场景下的成功路径，模型可能学到表层格式或局部启发式，难以主动探索新策略。

### §5.2.2 Reward-based Policy Internalization

Reward-based Policy Internalization 指 Agent 通过与环境交互产生 trajectories，利用非参数化、可验证的反馈信号直接优化 Policy。典型反馈包括任务成功率、unit test 结果、代码执行反馈、SQL execution correctness、ground-truth answer match、工具调用结果、GUI 任务完成状态、机器人操作成功与否等。

与 Imitation-based 方法相比，Reward-based 方法不再只学习"成功轨迹中做了什么"，而是进一步学习"哪些行为在环境中真正有效"。这使其能利用 Agent experience loop 的完整结构：context 和 action 构成 Agent 的决策过程，observation 和 feedback 为 policy update 提供外部依据。

这类方法的演进大致经历了三个阶段：

**第一阶段：Foundation Model 作为交互式 Policy。** GLAM [Car23] 将 FLAN-T5 放入 BabyAI-Text 等交互环境，通过 PPO 利用任务成功奖励做 online grounding。LLaRP [Szo23] 将冻结的 LLaMA 与视觉编码器连接为 embodied policy，以 success、subgoal completion 和 invalid action penalty 等环境反馈进行 DD-PPO 训练。这些工作确立了 Reward-based Policy Internalization 的基本前提：只要 Agent 的动作可以在环境中执行且环境能返回客观可验证的结果，Tokenized trajectory 就可以被直接转化为 Policy weights。

**第二阶段：Multi-Turn RL 与 Credit Assignment。** WebAgent-R1 [Wei25] 将网页交互建模为端到端 multi-turn RL，使用 M-GRPO 并行采样多条 browser trajectories，奖励由 URL match、string match 与 Playwright-based verification 给出。Training Long-Context, Multi-Turn Software Engineering Agents [Gol25] 先用通过测试的成功轨迹做 RFT 热启动，再用 DAPO 在真实代码环境中继续优化，奖励直接来自 unit test pass/fail 与 trajectory length penalty。ArCHer [Zho24f] 将 multi-turn language agent 训练拆成高层 utterance-level critic 与低层 token-level policy，使环境回报先被整合为回合级价值再传递给 token 生成层。

在 credit assignment 方面，Turn-PPO [Li25ae] 将 multi-turn interaction 建模为 turn-level MDP，在 turn 粒度上用 critic 做 GAE，使环境反馈更准确地对齐到回合级决策。GiGPO [Fen25c] 利用 anchor state grouping 比较不同 rollout 在相同中间状态下的动作差异，同时构造 episode-level 与 step-level relative advantage。Information Gain-based Policy Optimization [Wan25y] 用每一轮交互前后正确答案 log-prob 的增量定义 Information Gain reward，将 observation 的真实信息贡献转化为 turn-level intrinsic signal。SQL-ASTRA [Li26r] 通过 step-level Column-Set Matching Reward 从中间执行结果中提取局部结构正确性，再用 trajectory aggregation 汇聚为稳定的轨迹级训练信号。

**第三阶段：Exploration 与 Experience Reuse。** 长程 Agent 很容易在训练早期过快坍缩到低探索策略。Agentic Reinforced Policy Optimization [Don25d] 在 multi-turn tool-use 中引入 entropy-based adaptive rollout，在高不确定性步骤触发局部分支采样，通过 advantage attribution estimation 区分共享前缀与分支后动作的贡献。EPO [Xu25k] 在 PPO 或 GRPO 外层加入 trajectory-level entropy regularization 与 entropy smoothing，缓解 sparse-reward multi-turn RL 中的 exploration-exploitation cascade failure。LongNav-R1 [Hu26e] 用 geodesic distance 改善与 SPL 构造环境奖励，通过 horizon-adaptive kernel baseline 处理不同阶段的 advantage estimation。

在经验复用与效率提升方面，ARPO [Lu25f] 在 GUI 环境中维护成功 trajectory replay buffer，当当前采样组全部失败时从历史缓冲区注入正样本。AgentGym-RL [Xi25c] 提出 ScalingInter-RL，通过先短后长的 horizon curriculum 让 Agent 先掌握基础交互再逐步吸收更长程的决策经验。Improving VLA with Online RL [Guo25d] 采用 RL 与 supervised learning 交替的两阶段框架：先在 RL 阶段利用 binary success reward 发现成功轨迹，再将这些轨迹回流到 supervised stage 做 LoRA 微调。

**Domain-Specific Reward Design。** SQL-Trail [Hua26d] 将 Agent 放入 reason-execute-observe 循环，不仅利用 final execution correctness，还引入 syntax validity、schema grounding 与 turn-budget shaping。ToolRL [Qia25b] 将奖励分解为 format correctness 以及 tool name、parameter name、parameter content 的层级匹配分数。这些结构化 reward 设计表明：随着 Agent 环境变得更复杂，真正高价值的 reward 不再只是一个终局 success flag，而是环境中那些可程序验证的中间结构被逐步挖掘出来并重写为 policy optimization 的组成部分。

Reward-based Internalization 的主线是如何把可验证环境反馈系统地转译为可被 Actor 吸收的参数更新信号。其能力上限较高——Policy 可以通过试错发现超出示范数据的新策略——但面临 reward 稀疏、credit assignment 困难、online rollout 成本高以及 reward hacking 等挑战。

### §5.2.3 Preference-based Policy Internalization

Preference-based Policy Internalization 从 Agent experience 中构造轨迹间的相对偏好关系，通过 DPO、DMPO 或其他 trajectory-pair optimization 方法更新 Policy。相对更优的轨迹可来自成功任务、通过验证的执行结果、人工标注、修正后的轨迹或更高效的操作路径；相对较差的轨迹可来自失败尝试、错误工具调用或未通过测试的代码修改。

这类方法的基本动机是：在许多 Agent 场景中，精确设计每一步 reward 很困难，但比较两条轨迹哪一条更好却相对容易。Web navigation 中一条轨迹成功找到目标信息另一条陷入无关页面；GUI automation 中一条轨迹到达目标界面另一条点击了错误控件——这些比较均可形成 preference signal。

从经验转化角度看，Preference-based 方法能显式利用失败经验。Imitation-based 方法通常只保留成功轨迹，Reward-based 方法需要将失败轨迹转化为数值 reward。Preference-based 方法提供了另一种选择：失败轨迹作为 negative sample 与成功轨迹或修正轨迹配对，帮助 Policy 学习哪些行为应该避免。

**代表性工作。** [Shi24c] 将 DPO 从单轮 response preference 扩展到 multi-turn trajectory preference，通过引入 state-action occupancy measure 与 length normalization 解决长轨迹下的 preference objective 问题。[Son24] 先用 expert trajectory 做 behavior cloning，再让当前 Policy 在环境中主动探索，把成功示范与探索过程中产生的失败 trajectory 组成 preference pairs，用 DPO 持续更新 Policy。[Da25] 针对 software engineering agent 中奖励稀疏的问题，引入 guidance 机制帮助模型探索更可能成功的代码修复轨迹，再依据 unit tests 的 pass/fail 结果构造 preference pairs 并通过 DPO 完成 Policy update。[Che24k] 从 tool-use agent 的 inference tree 中系统挖掘失败分支，将成功路径上的关键步骤与同层失败兄弟节点配对，构造 step-level preference data。

在粒度优化方面，[Gao25c] 指出长程任务中仅做 trajectory-level comparison 过粗，联合 trajectory-level、group-level 与 step-level preference 进行分层优化。[Liu25z] 将偏好学习收缩到 web element selection 层面，通过对目标元素与干扰元素的对比训练提升 web navigation 中的局部动作判别能力。

与 Reward-based 方法相比，Preference-based 方法具有更稳定的 supervised-style 训练形式，不需直接估计高方差 policy gradient。与 Imitation-based 方法相比，它能利用负样本和轨迹间对比，更适合处理失败经验、修正经验和探索经验。局限在于 preference pairs 的构造质量直接影响训练效果，trajectory-level preference 仍可能缺乏细粒度 credit assignment。

**三类方法的判定标准。** P5 内部的分类依据是 policy update 所依赖的核心监督信号类型：若主要依赖 SFT/behavior cloning/imitation objective，environment feedback 仅用于筛选或构造训练样本，归入 Imitation-based；若核心训练信号来自非参数化环境反馈、执行反馈、规则化 verifier 或 ground truth，且该反馈直接参与 policy optimization，归入 Reward-based；若核心 policy update objective 是 preference optimization/trajectory-pair optimization，偏好标签主要来自非参数化信号（执行成功、任务完成、测试通过等），归入 Preference-based。若 reward 或 preference 主要来自 trained reward model、LLM-as-a-judge 等参数化 evaluator，则属于 Evaluator-mediated Policy Optimization（偏向 P6）。
