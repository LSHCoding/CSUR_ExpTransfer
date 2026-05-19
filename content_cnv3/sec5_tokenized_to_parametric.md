# 5. Tokenized-to-Parametric Transformations

本章讨论经验从 Tokenized 载体向 Parametric 载体转化的两条路径：P4（Tokenized → Evaluator，经验固化为评估能力）与 P5（Tokenized → Policy，经验固化为决策能力）。两条路径共享同一源端类型——Agent trajectory、reasoning trace、tool-use log、action history、execution outcome 等离散经验记录——区别在于目标载体的功能角色。Evaluator 参数回答"如何判断行为质量"，Policy 参数回答"如何生成行为"。

## 5.1 Tokenized-to-Evaluator Transformation (P4)

P4 将 Tokenized Agent Experience 内化为参数化 Evaluator。通过训练，离散经验中的评价语义被写入 Evaluator 参数，形成可复用的评估能力。训练后的 Evaluator 表现为 outcome reward model、process reward model、verifier、critic、judge、value model、failure detector 或 diagnostic feedback model。

判定一项工作属于 P4 的硬标准是 **Evaluator 参数是否被经验数据实质性更新**。只在推理时通过 prompt 激发已有模型评估能力、参数不发生更新的 prompted LLM-as-a-judge 不在此列。判定只看参数是否被更新，不限训练手段——SFT、RL、self-training、对比学习均可作为内化方式。

<!-- P4 的分类沿两条正交轴展开。主轴是监督粒度（supervision granularity），区分训练时监督信号被分配到的层次：Outcome-supervised 把信号分配在完整输出、完整轨迹或完整 episode 上；Process-supervised 把信号分配在中间步骤、动作前缀或单个 decision 上。次轴是产物形态，区分训练后 Evaluator 推理时输出什么：判别式（discriminative）评估器产物只有标量或可读为标量的信号；生成式（generative）评估器产物包含自然语言或结构化生成内容（critique、error diagnosis、verification rationale、repair suggestion）。一项工作只要其方法贡献包含生成式产物，就按其更富的成分归入生成式子类。少数 Evaluator 同时携带 outcome 与 process 两种监督，按其主导监督信号归入对应子节。 -->

### 5.1.1 Outcome-supervised Evaluator Internalization

Outcome-supervised evaluator internalization 训练 Evaluator 对完整候选行为给出全局判断，把一个完整 response、trajectory 或 episode 映射为 outcome-level 的评价。其吸引力在于 outcome-level label 通常比 dense process label 更易获得，且对具有明确最终答案或显式成功标准的任务可直接对齐最终目标。结构性局限是 credit assignment 弱：一条失败轨迹可能含有许多有价值的中间决策，一条成功轨迹也可能含有偶然有效但并不稳健的推理，把整条轨迹压成单一标签会掩盖哪些动作应被强化、哪些应被修正。

#### Discriminative Outcome Evaluators

判别式 outcome 评估器的产物是一个针对完整候选的标量分或离散标签，下游消费路径最短。

具身领域的 episode-level success/failure detector 构成最集中的一簇。Vision-Language Models as Success Detectors [Du23] 把 success detection 重写为 visual question answering，用人工标注的 clip-level 成功标签对 Flamingo 做 SFT，学习对"视频片段 + 任务描述"回答 yes/no 的能力。I-FailSense [Fen25b] 面向跨任务 failure detection，分两阶段训练——先对 VLM 做 LoRA SFT，再训练附着在中间层的 FailSense blocks，用 cross-entropy 与 BCE 把 expert demonstration 与目标错配负例的 success/failure 信号内化为 detector。SAFE [Wan25v] 把输入从纯观测扩展到 VLA policy 的内部 latent embedding，用 MLP 或 LSTM 学习 trajectory-level 失败预测，推理时逐时刻输出 failure likelihood 并配合 conformal threshold 触发 abort 或 human intervention。

RoboReward [Lee26b] 把 OXE demonstration 与带人工核验进度分的 RoboArena rollouts 汇成经验，经 counterfactual relabeling 与 temporal clipping 构造 1–5 级 episode rubric，对 Qwen3-VL 做 SFT 以 MAE 回归离散 episodic reward。VLP [Liu25w] 从 Meta-World 的 expert/medium/random 三类操作视频段出发，用 Intra-Task、Inter-Language、Inter-Video 三类隐式 preference 规则构造比较标签，以 cross-entropy 学习 trajectory-segment 级 cross-modal preference model。WebRL [Qi24] 在自进化在线课程 RL 框架中训练 outcome-supervised reward model，依据用户指令、历史动作与最终网页状态判定整条 web trajectory 是否完成任务。

#### Generative Outcome Evaluators

生成式 outcome 评估器对完整候选生成 verdict 之外的语义内容——judging rationale、failure reasoning、repair suggestion——产物信息密度更高，推理与输出开销也更大。

在 reasoning 与 general 域，Generative Reward Models [Mah24b] 把 reward modeling 改写为 next-token generation，用 SFT 与 STaR 自举 rationale 训练带推理链的 CoT-GenRM。S2J [Sun25l] 指出 generative reward model 存在 solving 与 judging 能力的落差，要求 Evaluator 判断前先自行求解，用 solving reward 与 judging reward 的联合 RL 目标更新参数。J4R [Xu25i] 用 EIS-GRPO 训练 pairwise judge，通过 response order swap 等等价初始状态上的 judgment correctness 驱动 RL，压低位置偏置与表面格式干扰。Critic-RM [Wan25s] 让模型自生成 critique 作为 latent rationale，以联合目标同时优化 critique generation loss 与 Bradley-Terry preference loss。

面向"让反馈帮助下游修复"的目标，CTRL [Xie25c] 面向 code，以 sandbox 隐藏单测的通过情况为奖励，先用 execution-guided synthetic critique 做 SFT，再用 GRPO 直接优化 critique 使其更能帮助 generator 产出通过测试的代码。RL4F [Aky23] 训练 critique generator，以 refined output 相对 ground truth 的任务指标为 PPO 奖励。AgentV-RL [Wan25aq] 把 verifier 做成多轮 tool-augmented 验证 agent，先做 rejection fine-tuning 学高质量 verifier 轨迹，再用 GRPO 以最终 verdict 与 ground truth 的一致性为奖励。

在具身与 computer-use 域，CriticGPT for Robotic Manipulation [Zho25m] 从 Meta-World 不同训练阶段策略的操作视频出发，用环境全信息脚本自动生成 pairwise analysis 与 preference，对 VLM 做 LoRA 微调学习视觉比较与文字分析。ARMOR [Qi26] 以大规模 sparse failure label 与较小规模 dense reasoning annotation 训练机器人失败检测器，联合优化 BCE detection head 与 next-token reasoning decoder，在 online refinement 阶段吸收自身 rollout。Video-Based Reward Modeling for Computer-Use Agents [Son26d] 构建 video-level success judgment 与 first-failure attribution 联合目标，对 VLM 做 reward modeling 微调。

<!-- 判别式与生成式 outcome 评估器呈现不同的 utilization 画像。判别式的下游消费路径最短、延迟最低，适合 reward-filtered behavior cloning、offline RL annotation 与运行时 guardrail。生成式以更高的推理与输出开销换取可解释性与可修正性：其 verdict 可塌缩为标量进入 P6，而 rationale/critique 支持 critique-driven refinement 这类用法。 -->

### 5.1.2 Process-supervised Evaluator Internalization

Process-supervised evaluator internalization 训练 Evaluator 对中间推理步骤、动作前缀或单个 decision 提供局部监督。核心动机是 agent 失败通常不是最后一步的突然事件，而是一系列局部错误的累积；process 评估器试图解决 outcome 监督抹平的 credit assignment 问题——不仅判断最终 outcome，还判断每个中间决策是否正确、是否有希望、是否推动任务进展。

#### Discriminative Process Evaluators

判别式 process 评估器对每个 step、prefix 或 state-action 对输出标量分，是这一支中规模最大的一簇。

reasoning PRM 谱系奠定了局部监督的基本范式。Let's Verify Step by Step [Lig23] 用 PRM800K 的人工 step 标注训练 PRM，对每一步给 positive/negative/neutral 判断。OmegaPRM [Luo24] 用 MCTS 加 binary search 自动定位 first error，把前缀的可完成性转成 soft process label 替代人工标注。Rewarding Progress [Set24] 把监督目标从 step correctness 改写为 step-level advantage——从各前缀展开 Monte Carlo rollout 估计 future success probability，评估该步是否真正提高未来成功概率。PQM [Li24m] 把 PRM 训练从独立分类改为带 margin 的 comparative Q-value ranking——正确前缀的成功概率高于错误前缀，错误处价值出现显著断裂。PathFinder-PRM [Pal25] 引入 hierarchical supervision，先预测 math error 与 consistency error 两层错误类型、再预测最终 correctness reward。BiRM [Che25s] 联合学习 backward-looking process reward 与 forward-looking value 两个头，同时编码"当前步是否合理"与"该前缀未来是否还有希望"。

agentic、GUI 与 web 域把这些抽象过程信号落地为与环境状态变化直接对齐的 step-level 评估。AgentPRM [Xi25b] 把 reasoning PRM 推广到多步 agent 决策，用 TD 与 GAE 从 rollout 自动构造 step-wise Q 值与 advantage 伪标签。ProgRM [Zha25z] 通过 LCS 匹配的自标注算法在 GUI 轨迹中定位 key step 并分配归一化 progress label。Building Autonomous GUI Navigation via Agentic-Q Estimation [Wan26s] 把终局 success 信号反传到 state-thought-action 三元组，训练 step-wise success probability estimator。Advancing Mobile GUI Agents [Dai25] 采用 Pairwise Process Preference——每一步让正确动作分数高于若干错误动作——以 Q-LoRA 微调 backbone 与评分头。IntentScore [Che26s] 把 planning intent 作为条件信息融入 action encoder，用 contrastive alignment 与 margin ranking 学习单步评估，以极低延迟服务 test-time reranking。GAIA [Wan26p] 用 data flywheel 迭代训练 step-level binary critic，先 SFT 学第一轮 critic，再让其挖掘更难样本训练第二轮，持续纳入真实 GUI agent 的错误分布。

code 域的 SWE-Shepherd [Dih26] 把读文件、编辑、跑测试等中间动作用启发式赋即时奖励，用折扣累积形成 step-wise target 并以 qLoRA 加 MSE 训练 PRM。具身领域，RL-VLM-F [Wan24l] 让 GPT-4V/Gemini 对 observation image pair 先做 analysis 再给 pairwise label，用 Bradley-Terry 式 preference learning 学习连续 reward function。Video-Language Critic [Ala24] 以对比式 symmetric cross-entropy 加 sequential ranking objective 学习，强制成功视频中后期片段分数高于前期。Large Reward Models [Wu26e] 对同一 VLM backbone 用 LoRA、SFT、DPO 分别学习 contrastive reward、absolute progress reward 与 completion reward，把大规模视频的时序经验内化进统一 LRM。

#### Generative Process Evaluators

生成式 process 评估器对每个中间步骤生成 critique、错误诊断或修正建议，不止判断某步好坏，还解释违反了什么约束、错误属于何种类型、应朝什么方向修正。

reasoning 域，DeepCritic [Yan25u] 用 Monte Carlo 估计每步后的成功率并定位 first error，分 critique teaching SFT 与 critique incentivization GRPO 两阶段，产物是长文本 deliberate rationale 与每步正负 judgment。Enhancing LLM Reasoning via Critique Models [Wan25ae] 构建 MathCritique-76k，对 flawed reasoning path 加 GPT-4o 对首个错误步骤的 critique，经 soft filtering 保留真正有助修正的样本做 SFT。

GUI 与 web 域是生成式 process 评估器最密集的领域。GUI-Shepherd [Che25h] 把 AndroidWorld 在线 rollout 与 AndroidControl 离线状态汇成交互经验，人工给每步动作打正负标签、GPT-4o 补解释性 rationale，对 UI-TARS 做 SFT 学 step-level verification。GUI-Critic-R1 [Wan25q] 是 pre-operative critic——在动作执行前生成 observation analysis、possible result、critique、correctness score 与 corrective suggestion——先做 RFT cold-start，再用 Suggestion-aware GRPO 强化。OS-Oracle [Wu25m] 整合七个开源 GUI trajectory 数据集，规则模拟四类常见错误动作作负例，先 SFT 学 reason 加 judgment、再用 CP-GRPO 训练跨平台 critic。WebArbiter [Zha26ab] 是 principle-guided generative PRM——先用 o3 教师推理做 reasoning distillation、再用 GRPO 对齐最终 verdict 与 ground-truth correctness，产物含 principle induction、structured justification 与 preference verdict。Web-Shepherd [Cha25b] 把 web process evaluation 做成 checklist-grounded generative judging，生成每个 checklist item 的 Yes/No/In-Progress 判断。

具身领域，AHA [Dua24] 通过 FailGen 从成功 demonstration 程序化生成失败子任务，按 VLM 指令微调范式做 autoregressive next-token 训练，对长程操作中的中间 subtask 输出 yes/no 判断与自由文本 failure rationale。SOLE-R1 [Sch26] 把真实与模拟机器人视频转为 spatiotemporal CoT trace，用几何距离、时间反转与偏离注入自动得到逐时刻 progress 监督，先 SFT 学结构化 reasoning 加 progress value、再用 RLVR 与 GRPO 优化。general agentic 场景下，PPRM [Xu25h] 面向不可验证的多轮 search 型任务，按 correctness、relevance、consistency 等原则给 step-wise 分数，通过 ReNorm 将 process reward 与 outcome reward 统一校准。

<!-- process 子类的演进脉络清晰：早期工作先在 reasoning 中确立 step-level evaluator 的必要性，随后把局部监督从 correctness 扩展为 advantage、Q-value、progress 与双向 reward 语义，再在 GUI、computer-use、code 与 embodied 中落地。判别式与生成式之间，生成式信息密度最高，适合错误类型复杂、任务空间开放的场景，也有助于跨任务迁移——"未验证工具返回结果""忽略用户约束"等诊断可能在不同任务中重复出现。其代价是可靠性：自然语言 critique 可能听起来合理却与环境真实反馈不一致。产物形态与下游 utilization 自由度之间存在单调关系——生成式产物信息含量最高，下游可塌缩成标量进入 P6 的 RL、可取 binary 做 Best-of-N 筛选、也可保留全文驱动 step-wise refinement；判别式产物则下游选择最受限。 -->

### 5.1.3 Discussion

P4 两条轴构成四个交叉格，呈现不均匀分布。outcome 判别式工作最密集、工程最成熟，直接继承经典 reward modeling 的优化接口。process 判别式围绕 credit assignment 快速扩张，代价是 step-level label 的获取成本与噪声。生成式两支信息密度较高，但 critique 的正确性缺乏自动验证手段，是 P4 留给后续工作的开放性难题。

<!-- Evaluator 产物形态与下游 utilization 自由度之间存在单调关系：生成式产物信息含量最高，下游可塌缩为标量进入 P6 的 RL、可取 binary 做 Best-of-N 筛选、也可保留全文驱动 step-wise refinement；判别式产物下游选择最受限，只能作为数值信号被消费。这一关系在 §8 与 P6 的对接中进一步展开。 -->

## 5.2 Tokenized-to-Policy Transformation (P5)

P5 将离散化的 Agent Experience 内化为 Policy/Actor 参数。源经验是各类 Tokenized artifacts——自然语言轨迹、工具调用记录、代码编辑历史、GUI 操作序列、reasoning chains；转化目标是让这些经验进入 Policy weights，使模型在后续任务中无需显式检索、拼接或重放原始经验即可完成序贯决策。

P5 要回答的不是如何训练一个更强的模型，而是 Agent 在交互中形成的离散经验如何被组织成训练信号并改写 Policy 的参数化决策能力。与 P1/P2 不同，P5 的目标载体是不可读、不可局部寻址的权重；经验内化后调用成本低、不受 context window 限制，代价是显式可追踪性与局部可修改性下降。

本文按 policy update 消费了轨迹经验的哪个侧面将 P5 分为三类：Imitation-based Policy Internalization 消费成功轨迹的动作序列本身；Environment-Reward-based Policy Internalization 消费每条轨迹的客观结果，用可验证的环境反馈优化；Preference-based Policy Internalization 消费轨迹之间的相对序，构造偏好并优化。

P5 与 P6 的边界由 reward 或 preference 信号的来源决定：信号是非参数化的——环境可验证结果、unit test、ground-truth match、rule-based verifier——经验直接走 Tokenized → Policy，属 P5；信号来自参数化 evaluator（trained RM、PRM、LLM-as-a-judge）时，转化先经 P4 再经 P6，是复合路径，不在本节。参数化 evaluator 若仅用于筛选或重构训练数据、其分数不进入 policy update 的 loss，经验仍是直接内化，工作仍归 P5。

### 5.2.1 Imitation-based Policy Internalization

Imitation-based Policy Internalization 把高质量 Agent trajectories 当作监督示范，通过 behavior cloning、SFT 或 rejection-sampled fine-tuning 训练 Policy。它消费的是成功轨迹的动作序列本身：若一组轨迹已体现有效的任务解决行为，模型经模仿其动作选择、推理模式、工具调用习惯或 GUI 操作序列即可把相应经验内化进参数。环境反馈在这里不进入优化目标，只承担 data selection 与 data construction——筛掉失败 rollout、过滤无效工具调用、保留通过测试的代码修改。

主线机制是 success-filtered behavior cloning，环境信号决定哪些数据进训练集，loss 始终是成功数据上的最大似然。在 web agent 域，<!-- TODO: 补充方法名缩写 --> [Pat24] 以 environment error 与 self-critique 过滤 WebArena 中的自生成轨迹，在 QLoRA 下做 autoregressive SFT。SWE-Gym [Pan24] 用可执行 unit test 判定 patch trajectory 成败，以 rejection-sampling fine-tuning 完成 policy update，同文另训的 verifier 只做 reranking、不改变 agent 归类。Go-Browse [Gan25b] 通过 structured exploration 采集 web trajectories，仅对成功轨做 SFT，成功标签由 VLM-as-a-judge 给出但仅用于筛选。

<!-- 一类工作在 imitation 前对轨迹做轻量加工，以提升示范信号的质量与覆盖。NNetNav [Mur24b] 对开放网页中的无监督探索轨迹做 hindsight instruction relabeling，把无目的交互改写成 instruction-following demonstrations 后 SFT。AndroidGen [Lai25d] 用 StepCritic 把长 Android 轨迹切成成功子段并做 augmentation，在筛后轨迹上做 LoRA-SFT。这类加工只重排或重标注轨迹内容、不改变其载体层次，仍是 P5 内部的预处理。若加工把经验跨载体重构，则构成与 P1 或 P2 的链式复合，归 §7 处理：WebCoT [Hu25i] 把 reflection、branching、rollback 痕迹 verbalize 成显式 CoT 再内化，AgentTrek [Xu24] 把 web tutorial 编译成 Goal-Observation-Reasoning-Action schema 再 SFT。 -->

AgentTuning [Zen23d] 将多个环境中的 GPT-4 agent trajectories 统一为 thought-action supervision 用于 generalized agent tuning。Explorer [Pah25] 与 InSTA [Tra25] 通过 exploration-driven 流水线让强模型在真实网页中生成并验证 success trajectories，再蒸馏给学生模型。AgentTrek [Xu24] 把 web tutorials 转写为可执行的 procedural guidance，通过 guided replay 合成 demonstrations。

Imitation-based 方法特别适合 Agent 的 cold-start training，能快速教会模型动作空间、输出协议与基本交互流程。能力上限受示范轨迹质量与覆盖范围限制——若训练数据只含有限场景下的成功路径，模型易学到表层格式或局部启发式，难以主动探索新策略。经验写进权重后即不可局部寻址，新增或修正一类行为需重新 fine-tune。

<!-- 数篇工作冠以 RFT、ReST 或 RL 之名，最终的 policy update 仍是 success-filtered 数据上的最大似然。判定 P5 子类依据的是 policy weight 被改写时所用的 objective，而非论文的方法命名。 -->

### 5.2.2 Environment-Reward-based Policy Internalization

Environment-Reward-based Policy Internalization 让 Agent 与环境交互产生 trajectories，用非参数化、可验证的反馈信号直接优化 Policy。它消费的是每条轨迹的客观结果：任务成败、unit test pass/fail、代码执行反馈、SQL execution correctness、ground-truth answer match、GUI 任务完成状态、机器人操作成败——这些均由环境本身可程序判定。命名中的 Environment-Reward 划界：reward 来自 trained RM 或 LLM-as-a-judge 的工作归 P6。与 Imitation 只学成功轨迹做了什么不同，这里失败轨迹经 reward 转成负信号，同样进入优化。

基本前提由早期工作确立。GLAM [Car23] 把 FLAN-T5 放入 BabyAI-Text，以任务成功 sparse reward 经 PPO 做 online grounding。LLaRP [Szo23] 连接冻结的 LLaMA 与视觉编码器为 embodied policy，以 success、subgoal completion、invalid-action penalty 组成的环境 reward 经 DD-PPO 训练 adapter 与 heads。只要 Agent 动作可在环境中执行、环境能返回客观可验证的结果，Tokenized trajectory 即可直接转化为 Policy weights。

当设定推进到长程、多轮的真实环境，核心困难暴露出来：一条几十步的轨迹只在终局拿到一个稀疏的可验证 reward，信号难以被有效利用。让一个稀疏而可验证的 reward 在长程多轮下变得可用，是此后工作的主线问题，沿三层推进。

**让信号不消失。** 长程 Agent 在训练早期极易坍缩到低探索策略，一旦坍缩便不再产生成功轨迹。EPO [Xu25k] 在 PPO/GRPO 外层加 trajectory-level entropy regularization 与 entropy smoothing，缓解 sparse-reward multi-turn RL 的 exploration-exploitation cascade failure。Agentic Reinforced Policy Optimization [Don25d] 在 multi-turn tool-use 中用 entropy-based adaptive rollout，在高不确定性步骤触发局部分支采样。ARPO [Lu25f] 在 GUI 环境中维护成功 trajectory replay buffer，当采样组全失败、无梯度时从历史缓冲注回正样本。AgentGym-RL [Xi25c] 提出 ScalingInter-RL，以先短后长的 horizon curriculum 让 Agent 先在可完成的短程任务上拿到信号、再逐步延长。

**让信号可归因。** 多轮轨迹里 reward 常只在终局给出，而决定成败的可能是中间某一步。演化线是归因粒度的持续下沉：从整轨，到 turn-level，到 step-level。WebAgent-R1 [Wei25] 以 M-GRPO 并行采样 browser trajectories，reward 由 URL match 与 Playwright verification 给出。<!-- TODO: 补充方法名缩写 --> [Gol25] 先用通过测试的轨迹做 RFT 热启动，再用 DAPO 在真实代码环境中优化，奖励来自 unit test pass/fail 与 trajectory length penalty。ArCHer [Zho24f] 用环境 reward 先训 utterance-level Q critic，再把 multi-turn advantage 传给 token actor。Turn-PPO [Li25ae] 把多轮交互建模为 turn-level MDP，在 turn 粒度上用 critic 做 GAE。GiGPO [Fen25c] 用 anchor-state grouping 比较不同 rollout 在相同中间状态下的动作，同时构造 episode-level 与 step-level relative advantage。Information Gain-based Policy Optimization [Wan25y] 用每轮交互前后 ground-truth answer log-prob 的增量定义 information-gain intrinsic reward，把 observation 的真实信息贡献转成 turn-level 信号。

<!-- actor-critic 中的 critic 由环境 reward 在 RL 算法内部 bootstrap 而来，是估计 expected return 的内部辅助件，并非独立训练的外部 reward 来源。reward 的 provenance 仍是环境，因此这些方法仍属 P5，与 P6 中 evaluator 充当 reward 来源有本质区别。 -->

**让信号在源头变密。** 与其在一个固定的稀疏 reward 上更努力地探索或归因，不如让 reward 信号本身在源头变密。做法是从环境里挖掘可程序验证的中间结构，把单一终局 flag 重写成 composite reward。ToolRL [Qia25b] 把 reward 拆成 format correctness 与 tool name、arg name、arg value 的三层匹配。SQL-Trail [Hua26d] 在 reason-execute-observe 循环里用 execution、turn-budget、schema grounding、syntax、format 等六项组成 composite reward。SQL-ASTRA [Li26r] 的 Column-Set Matching Reward 从结果表列值集合的比较中给出 dense partial-credit。在 GUI 与 VLA 域，rule-based verifiable reward 被直接用作 GRPO 的输入，format 合法性叠加 action-type、click-point、text-match 等可判定项 [Luo25b, Zha25an]。

Environment-Reward-based 的能力上限高于 Imitation——Policy 能通过试错发现超出示范数据的新策略——代价是 reward 稀疏、credit assignment 困难、online rollout 昂贵以及 reward hacking。它与 Imitation 共享经验写进权重后不可局部寻址的性质，并多一层不可逆：RL 更新由高方差梯度驱动，一次坍缩或 reward hacking 造成的能力损伤难以像编辑一条文本规则那样回退。实践中 imitation 与 reward 常是同一 pipeline 的两个阶段——cold-start 用 imitation 立起格式，能力突破交给 reward optimization。

### 5.2.3 Preference-based Policy Internalization

Preference-based Policy Internalization 从 Agent experience 中构造轨迹间的相对偏好，通过 DPO、DMPO 或其他 trajectory-pair optimization 更新 Policy。它消费的是轨迹之间的相对序：相对更优的轨迹来自成功任务、通过验证的执行、修正后的轨迹或更高效的操作路径，相对较差的来自失败尝试、错误工具调用、未通过测试的代码修改。

这一方法的基本动机在于：许多 Agent 场景中精确设计每步 reward 很难，但判断两条轨迹孰优孰劣相对容易。Web navigation 中一条轨迹成功找到目标信息另一条陷入无关页面，GUI automation 中一条轨迹到达目标界面另一条点击了错误控件——这些比较均可形成 preference signal。

相对另两类，Preference-based 显式消费失败经验：Imitation 丢弃失败轨，Environment-Reward 把失败轨压成一个负 scalar，Preference 则把失败轨作为 negative 与成功或修正轨配对。DMPO [Shi24c] 把 DPO 从单轮 response preference 扩到 multi-turn trajectory preference，引入 state-action occupancy measure 与 length normalization 解决长轨迹下的 preference objective。ETO [Son24] 先用 expert trajectory 做 behavior cloning，再让 Policy 主动探索，把成功示范与探索中的失败轨组成 preference pairs 用 DPO 持续更新。在 SWE agent 域，<!-- TODO: 补充方法名缩写 --> [Da25] 用 guidance 帮助模型探索更可能成功的修复轨迹，再依 unit test pass/fail 构造 preference pairs 并通过 DPO 完成更新。

偏好粒度同样在下沉，与 §5.2.2 中 credit assignment 的演化平行。HPL [Gao25c] 指出长程任务只做 trajectory-level comparison 过粗，联合 trajectory、group、step 三层偏好做分层优化。WEPO [Liu25z] 把偏好收缩到 web element 层面，用目标元素对干扰元素的对比训练提升局部动作判别。Environment-Reward 与 Preference 两条路线各自独立地走向更细的归因或对比粒度。

与 Environment-Reward 相比，Preference-based 是 supervised-style 训练，不需要直接估计高方差 policy gradient，训练更稳。与 Imitation 相比，它能用负样本与轨迹对比，更适合处理失败、修正与探索经验。局限在于 preference pair 的构造质量直接决定效果，trajectory-level preference 仍可能缺乏细粒度 credit assignment。

<!-- 三类的判定标准对应划分轴：核心 objective 是 SFT/behavior cloning/imitation，environment feedback 仅用于筛选或构造样本，归 Imitation-based；核心训练信号是非参数化环境反馈/执行反馈/规则化 verifier/ground truth，且直接进入 policy optimization，归 Environment-Reward-based；核心 objective 是 preference 或 trajectory-pair optimization，且偏好标签来自非参数化信号，归 Preference-based。reward 或 preference 若主要来自参数化 evaluator，则属 P6。 -->
