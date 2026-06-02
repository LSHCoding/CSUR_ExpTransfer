# 5. Tokenized-to-Parametric Transformations

经验从 Tokenized 载体到 Parametric 载体的转化包含两条路径：Evaluator Internalization（§5.1）把交互经验固化为评估能力，Policy Internalization（§5.2）把交互经验固化为决策能力。两条路径共享同一类源端——Agent 序贯决策产生的交互轨迹。

## 5.1 Tokenized-to-Evaluator Transformation (Evaluator Internalization)

Evaluator Internalization 把 Tokenized agent experience 内化为 Evaluator 参数，使评估能力固化在权重中。产物涵盖 reward model（outcome / process）、verifier、critic 与 failure detector 等形态。纳入前提是 Evaluator 参数被经验数据实质更新；纯 prompt 触发、参数不变的 LLM-as-a-judge 不在此列。

<!-- 待定：是否需要在 introduction 段落也提经验来源约束——纳入前提除"Evaluator 参数被经验数据实质更新"外，还应加"监督信号锚定 agent 交互轨迹而非通用 preference data"？当前 P4.describe.md 中大量案例标"边界"或"不属于 P4"的争议点正出在 experience grounding 条件上（如 Mah24b、Yu24 标不属于 P4，Sun25l、Xu25i 标边界）。若不在此写清，读者可能在后续子节遇到这些判定时感到困惑。 -->

### 5.1.1 Outcome-supervised Evaluator Internalization

Outcome-supervised internalization 把监督信号绑定到一条完整 response、整段轨迹或整个 episode，将其映射为单一评价标签。按输出形态，本节分为判别式与生成式 outcome 评估器两支。

#### Discriminative Outcome Evaluators

判别式 outcome 评估器输出标量判定，按信号类型分 binary outcome judgment 与 graded outcome scoring 两类。

Binary outcome judgment 将完整 episode 映射为成功/失败或违规/合规等二值判定。Du et al. [Du23] 把 success detection 写成 visual question answering，用 clip-level 成功标签训练 Flamingo 做二值判定。<!-- 边界：多数样本是 success detection 视角而非显式 agent decision trajectory -->I-FailSense [Gri25] 扩展到跨任务 failure detection，正例来自原指令、负例来自语义不匹配指令。WebRL [Qi24] 在自演化课程 RL 中训练 outcome reward model，依据指令、历史动作与页面状态判定 web trajectory 是否完成任务。Wen et al. [Wen25b] 把判定目标从 task success 移到 policy violation，对四类规则逐条判违规。

Graded outcome scoring 在二值之外给出更细的信号——分级分值、连续概率或相对偏好。RoboReward [Lee26b] 在真实 rollout 上做 counterfactual relabeling 与 negative clipping，构造 1–5 级 rubric 回归离散 progress。SAFE [Gu25b] 以 VLA policy 的内部 latent 为输入，在 rollout prefix 上学习随时间变化的 failure probability，由 conformal threshold 触发 abort。VLP [Liu25w] 改学相对偏好，从 expert / medium / random 三档轨迹构造比较标签，按 Bradley-Terry 学习 cross-modal preference。

#### Generative Outcome Evaluators

生成式 outcome 评估器除 verdict 外还产出自然语言文本，按文本承担的角色分 verdict justification、failure diagnosis 与 corrective critique 三类。

Verdict justification 在判定之外生成支撑该判定的推理。GenRM [Zha24o] 把 reward modeling 写成 next-token prediction，有直出 Yes / No 的 GenRM-Direct 与先生成 CoT rationale 再判的 GenRM-CoT。<!-- S2J 边界：监督锚定 pairwise preference 而非典型 agent trajectory -->S2J [Sun25l] 让 judge 判断前先自行解题，把 solving 与 judging reward 联合优化。<!-- J4R 边界：对象是 reasoning answer pair -->J4R [Xu25i] 让 judge 在 response order swap 等等价输入上保持一致判断，压低位置偏置。<!-- AgentV-RL 边界：验证轨迹偏向 candidate solution 而非外部 agent 交互 -->AgentV-RL [Zha26ac] 把 verifier 做成多轮 tool-augmented agent，以 verdict 与 ground truth 的一致性为奖励。CriticGPT-RM [Liu24g] 从不同阶段操作视频自动生成 pairwise analysis 与 preference，下游经 Bradley-Terry 训练独立 reward model。

Failure diagnosis 在判定之外生成对失败的解释或定位。AHA [Dua24] 通过 FailGen 在成功 demonstration 上注入多类失败模式，训练模型同时输出 yes / no 与自由文本 failure rationale。ARMOR [Qi26] 联合训练 detection head 与 reasoning decoder，多轮生成 detection 与 reasoning 后按自信度选取结果。ExeVRM [Son26d] 以执行视频训练，输出 video-level success judgment 与失败定位。

Corrective critique 生成被下游 generator 或 actor 消费的修正性意见。CTRL [Xie25c] 以单测通过为奖励用 GRPO 优化 critique，使 generator 更可能产出通过测试的代码。Co-Evolving Critics [Li26l] 让 critic 给出 diagnosis、actor 据此重写轨迹，critic 奖励含 saturation-aware gain 以防随 policy 进化而失效。<!-- RL4F precursor：训练对象是通用 NLP 输出修复而非 agent 交互经验 -->RL4F [Aky23] 以 refined output 相对 ground truth 的任务指标为奖励训练 critique generator，是 critique-driven repair 的早期形态。

### 5.1.2 Process-supervised Evaluator Internalization

Process-supervised internalization 把监督信号分配到中间步骤或动作前缀，将局部决策质量写进 Evaluator 参数。按输出形态，本节分为判别式与生成式 process 评估器两支。动因来自一项经验观察：长程 agent 的失败通常是若干局部错误的累积，单一 outcome label 无法把这些错误从一条整体失败的轨迹中分离出来。

#### Discriminative Process Evaluators

判别式 process 评估器对每个中间步骤或动作前缀输出标量分。按信号语义分 step correctness scoring、step advantage and progress estimation 与 step-action compatibility 三类。

**Step correctness scoring** 把每步映射为正确/错误或更细的错误类型标签。Let's Verify Step by Step [Lig23] 在 PRM800K 上用人工 step-level 标签训练 PRM，对每一步预测 positive/negative/neutral。OmegaPRM [Luo24] 用 MCTS 与 binary search 自动定位 first error，以 Monte Carlo 估计替代人工标注，产出 soft process label。PathFinder-PRM [Pal25] 的核心主张是 reward 估计应以错误类型为条件——模型先显式判定该步犯了 math error 还是 consistency error，再基于错误类型预测 step reward，而非从步骤文本直接跳到分数。GUI-Shepherd [Che25h] 把 step correctness 标签落到 GUI 域，人工标注 state-action 对是否正确、GPT-4o 补充 CoT rationale 作为训练增强，推理时输出标量正确性分数。GAIA [Wan26p] 把训练组织为 data flywheel——首轮以正确/错误 action 与 ground truth 比对训练 critic，次轮把 critic 难例回流训练第二轮，持续吸收真实 GUI agent 的错误分布。

**Step advantage and progress estimation** 在二值之外给出更细的信号：估计一步对未来成功概率的边际贡献或任务进度的连续值。Rewarding Progress [Set24] 从每个 prefix 展开 Monte Carlo rollout 估计未来成功概率的变化量，让 Evaluator 直接学习 step advantage 而非 step correctness。PQM [Li24m] 把问题形式化为 Q-value ranking——用 Plackett-Luce 排序损失替代独立 BCE，强制正确前缀的估计成功概率高于错误前缀。BiRM [Che25s] 在同一 backbone 上联合训练 backward-looking reward head 与 forward-looking value head，同时输出步骤局部正确性与 partial trajectory 仍通向正确答案的概率。AgentPRM [Xi25b] 将这一思路从 reasoning 扩展到多步 agent 决策——用 TD 与 GAE 从 rollout 自动估计 state-action 对上的 Q-value 与 advantage，使 agent trajectory 的中间步骤也能获得 process reward。ProgRM [Zha25z] 在 GUI 轨迹中用 LCS recipe matching 自动定位 key step 并分配归一化 progress label，基于动作历史与当前观测预测任务进度。Agentic-Q [Wan26s] 让终局 success 信号沿 trajectory 反传，训练 step-wise success probability estimator。SWE-Shepherd [Dih26] 在 code 域面临一个特殊困难——代码修改轨迹缺少自然的过程监督信号——于是用相关文件访问、目标文件修改、测试结果变化等启发式指标构造弱 process reward，折扣累积为 step-wise target 训练 repo-level PRM。

**Step-action compatibility** 在二值正确性之外引入另一种信号：比较同一决策点多个候选动作的相对优劣。V-Droid [Dai25] 的核心机制是 Pairwise Process Preference——不孤立地给单个动作打分，而是强制同一步内正确动作的分数高于若干错误动作，从相对序而非绝对值中学习。IntentScore [Che26s] 把 compatibility 的条件从 state 扩展到 planning intent——action encoder 显式接收 planning intent 作为输入，学习 state-action-intent 三元组的相容性分数，使评估器能区分"动作本身正确"与"动作在当前意图下正确"。

<!-- 具身领域三项工作位于 process supervision 的边界：监督信号带有步骤或进展语义，但对 agent 决策轨迹的锚定较弱。RL-VLM-F [Wan24l] 用 prompted VLM 对 observation image pair 做两阶段分析产生 ternary preference，按 Bradley-Terry 训练独立 RM 接入 SAC，但输入为 observation pair 而非显式 state-action token。Video-Language Critic [Ala24] 以 contrastive cross-entropy 与 sequential ranking loss 训练 CLIP 初始化的图文-时间编码器，强制成功视频中后期片段分数高于前期，但缺少显式 agent action token。Large Reward Models [Wu26e] 在统一 VLM backbone 上以 LoRA、SFT、DPO 分别学习 contrastive、absolute progress 与 completion 三类 reward head，从 24 个来源的视频时序经验训练通用 LRM，但监督主要来自大规模视频与自动时序标签。 -->

#### Generative Process Evaluators

生成式 process 评估器在标量判定之外产出自然语言文本——critique、错误诊断或修正建议。按文本在下游的功能分 step-level critique、verdict with structured reasoning 与 pre-operative corrective feedback 三类。

**Step-level critique** 对中间步骤生成针对性诊断，指出错误位置、类型与原因，不强制附带数值评分。DeepCritic [Yan25u] 先用 teacher model 生成的 deliberate critique 做 critique teaching SFT，再用 PRM800K 与 MC 自动标注的 step correctness 数据做 critique incentivization GRPO，使模型学会多视角、可纠错的长文本步骤批注。AutoMathCritique [Xi24] 让 actor 在 GSM8K 与 MATH 上生成 flawed reasoning paths，由 GPT-4o 标注首个错误步骤，经 Monte Carlo soft filtering 保留真正有助修正的 critique 做 SFT，产物是可直接驱动 actor refinement 的 step-level 反馈。

**Verdict with structured reasoning** 在给出判定（正确/错误、有希望/无希望）的同时生成支撑推理，使判定可审计、可质疑。与纯 critique 不同，这类评估器需同时产出 verdict 与 reasoning，且两者之间存在逻辑约束——reasoning 必须支撑 verdict。StepWiser [Xio25c] 让模型在对 reasoning chunk 给出 Positive/Negative verdict 前先写出 meta-reasoning，用 MC continuation 估计的 chunk 前后 Q-value 变化作为监督。OS-Oracle [Wu25m] 通过四类错误注入合成负例，用 CP-GRPO 强化 verdict 与 rationale 之间的一致性。WebArbiter [Zha26ab] 在 reasoning 结构上引入一个关键变化：模型在比较候选动作前必须先归纳适用于当前任务与页面的原则，再从原则推导 preference verdict，而非直接从状态跳到判断。Web-Shepherd [Cha25b] 引入另一种结构——checklist-grounded evaluation——按预定义 checklist 逐项生成 Yes/No/In-Progress 判断，使评估过程被分解为可逐项核验的子问题。SOLE-R1 [Sch26] 把 structured reasoning 扩展到具身时序域，从机器人视频中学习生成 per-timestep progress 分数及解释其判断的 spatiotemporal CoT。PPRM [Xu25h] 在不可验证的多轮 search 任务上按 correctness、relevance、consistency 等原则生成 step score，再通过 ReNorm 与 outcome reward 校准。

**Pre-operative corrective feedback** 在动作执行前生成诊断与修正建议，使错误在发生前被拦截。GUI-Critic-R1 [Wan25q] 在候选动作执行前依次生成 observation analysis、possible result、critique、correctness score 与 corrective suggestion，用 Suggestion-aware GRPO 强化，使 critic 的建议能实际降低后续执行失败率。

<!-- 一项边界工作 Don't Act Blindly [Zha26z] 让 GUI agent 在每步生成 Think、Verification、Action、Expected Effect 四段，用 Verification-Action-Effect GRPO 训练，推理时读取 SUCCESS/NO_CHANGE 判定触发自纠。其 verification 能力内嵌在 policy 中，不产出可独立分离、复用的 standalone evaluator，处于 P4 与 P5 的边界。 -->

### 5.1.3 Discussion

两条监督粒度与两种产物形态构成四个交叉格，文献分布显著不均。outcome label 易于从环境信号、执行结果或人工裁判得到，对具有明确成功标准的任务可直接对齐最终目标，因此 outcome 判别式由经典 reward modeling 接口直接继承，工程最成熟、文献最厚——在具身的 episode-level success detection 上几乎是默认选择，下游消费直接落在 scalar reward。process 判别式围绕 credit assignment 快速扩张，演化轴是从 correctness 到 advantage、progress、Q-value、bidirectional reward 的语义细分，再向 GUI、computer-use、code、embodied 等带显式中间状态的领域落地；代价是 step-level label 的获取成本（要么人工标注，要么 MC 自动估计）与噪声。生成式两支让 Evaluator 输出可读 critique 或 diagnosis，下游可塌缩为标量进入 Evaluator-Driven Optimization 的 RL、可取 binary 做 Best-of-N 筛选、也可保留全文驱动 step-wise refinement——产物形态与下游 utilization 自由度间存在单调关系，生成式自由度最大。代价是 critique 的正确性缺乏自动验证——一条听起来合理的 critique 可能与环境真实反馈不一致——这是 Evaluator Internalization 留给后续工作的开放性难题，仅靠本节文献本身无法收敛。

跨监督粒度看，process 监督换更细的 credit assignment，付出标注成本与噪声；跨产物形态看，生成式以更高推理成本换更丰富的下游 utilization。两条轴上的选择由下游任务的 verifiability 与监督预算共同决定，不存在普适最优。

## 5.2 Policy Internalization: Tokenized-to-Policy Transformation


Policy Internalization 把 Tokenized agent experience 内化为 Policy 参数，使序贯决策能力固化在权重中。按 policy update 消费的经验信号形态，本节分为 Imitation-based、Environment-Reward-based 与 Preference-based 三类。本节与 §7 的边界由信号 provenance 决定：信号来自环境可验证结果或 rule-based verifier 时属本节；信号来自参数化 evaluator 时，转化先经 P4 再经 P6，归 §7。

### 5.2.1 Imitation-based Policy Internalization

Imitation-based internalization 把高质量 agent trajectories 作为监督示范，通过 behavior cloning 写入 Policy 参数。环境反馈不进入优化目标，只承担数据筛选。按示范来源分 self-generated experience 与 teacher demonstrations 两类——二者在能力上限上有本质区别：前者受限于 agent 当前的探索能力，后者受限于 teacher 的覆盖范围。

**Learning from self-generated experience.** 核心挑战是筛选——agent 产生的大多是失败轨迹，只有少数可被模仿。[Pat24] 在 WebArena 中以 environment error 与 self-critique 筛选自生成轨迹中 plausible 的动作做 SFT，失败经验仅用于告知"哪些不该学"。NNetNav [Mur24b] 通过无监督探索采集网页交互，再用 hindsight instruction relabeling 把交互改写成 demonstrations 后做 SFT，ORM 仅用于轨迹过滤。AppVLM [Pap25b] 与 [Guo25d] 进一步让 agent 在线交互、持续将新成功轨迹加入训练集——RL 在其中扮演 data discovery 而非 optimization 角色，最终 policy update 仍是 success-only 数据上的最大似然。

**Learning from teacher demonstrations.** 核心挑战是获取与覆盖——高质量示范昂贵，且 teacher 的成功路径未必覆盖 agent 会犯的所有错误。[Pan24] 在 SWE-Gym 中以 unit test 判定 patch trajectory 成败，做 rejection-sampling fine-tuning。AgentTuning [Zen23d] 把多环境 GPT-4 生成的 thought-action trajectories 与通用 instruction 数据混合训练，展示 agent 行为协议可与通用 instruction-following 联合学习。Explorer [Pah25] 通过 GPT-4o 多 agent pipeline 合成 multimodal web trajectories，经 Task Verifier 过滤后对学生模型做 SFT。Go-Browse [Gan25b] 与 AndroidGen [Lai25d] 引入参数化 evaluator 辅助筛选——前者用 VLM-as-a-judge 判定轨迹成败，后者用 StepCritic 把 teacher 长轨迹切成成功子段——但 evaluator 分数均不进 policy loss。

部分工作在 imitation 前对轨迹做轻量加工以提升示范信号质量——AndroidGen 的 StepCritic 切段、NNetNav 的 hindsight relabeling 均属此类，加工未改变载体层次。若加工本身构成独立的 Transformation——WebCoT [Hu25i] 把 reflection、branching、rollback 痕迹 verbalize 成显式 CoT 再 SFT、AgentTrek [Xu24] 把 web tutorial 编译成 Goal-Observation-Reasoning-Action schema 再 SFT——则前置步骤是 P1 或 P2，与 Imitation 构成链式复合，归 §7。

### 5.2.2 Environment-Reward-based Policy Internalization

Environment-Reward-based internalization 用非参数化、可验证的环境反馈直接进入 policy optimization objective。与 Imitation 的关键区别是失败轨迹同样进入优化——经 reward 转成负信号后参与 policy update。基本前提由 GLAM [Car23] 与 LLaRP [Szo23] 确立：前者展示 LLM 可通过 PPO 从环境 sparse reward 中学习文本动作空间的 online grounding，后者展示冻结 LLM 加 trainable adapter 可通过 DD-PPO 从 embodied reward 中学习序贯决策。

推进到长程多轮的真实环境后，一个困难暴露：一条几十步的轨迹只在终局拿到一个稀疏的可验证 reward，信号难以支撑有效学习。此后工作沿三个方向推进——维持信号的持续存在、提高信号的归因精度、从源头加密信号本身。

**Exploration stabilization.** 长程 agent 在训练早期极易坍缩到低探索策略——一旦坍缩便不再产生成功轨迹，稀疏 reward 彻底消失。一类工作从 entropy 入手维持探索：EPO [Xu25k] 在 policy gradient 外层加 trajectory-level entropy regularization；ARPO [Don25d] 在高不确定性步骤触发局部 branching；AEPO [Don25c] 与 EMPG [Wan25ad] 分别从 advantage 构造与 bonus 设计两个角度将 entropy 纳入优化——前者把 entropy 写入 advantage 与 clipping，后者用 entropy 缩放 advantage 并加 future-clarity bonus。另一类工作从数据入手防止梯度消失：ARPO with Replay [Lu25f] 在 GUI 环境中维护成功 trajectory replay buffer，当采样组全失败时从历史缓冲注回正样本；SoLS [Pap25c] 在 mobile app control 中用非对称 actor update——正优势样本强更新、负优势样本保守正则——并配合成功转移回放。AgentGym-RL [Xi25c] 从课程设计入手，以先短后长的 horizon curriculum 让 agent 先在可完成的任务上拿到信号。

**Credit assignment refinement.** 归因粒度从整轨持续下沉到 turn、step、token。WebAgent-R1 [Wei25] 并行采样多条 browser trajectory，以 group-relative advantage 替代绝对 reward。[Gol25] 在 SWE 环境中将 trajectory-level unit test 结果分配到每个 action token。ArCHer [Zho24f] 与 Turn-PPO [Li25ae] 在 turn 粒度上做 credit assignment——前者先训练 utterance-level Q critic 再传到 token actor，后者将多轮交互建模为 turn-level MDP。GiGPO [Fen25c] 的 anchor-state grouping 比较不同 rollout 在相同中间状态下的动作质量，同时构造 episode-level 与 step-level relative advantage。LOOP [Che25af] 与 IGPO [Wan25y] 代表两种不依赖 critic 的归因方式：前者用 leave-one-out baseline 做 token-level 更新，后者用每轮交互前后模型对 ground-truth answer log-prob 的增量定义 information-gain intrinsic reward。RLVMR [Zha25ao] 在归因对象上引入一个变化——不只归因到动作，还归因到 planning、explore、reflection、monitor 等 meta-reasoning 行为，用 rule-verifiable process reward 让这些行为可被显式监督。上述方法中出现的 critic（如 ArCHer 的 Q critic、Turn-PPO 的 value head）是由环境 reward 在 RL 算法内部 bootstrap 而来的 expected-return estimator，不是独立训练的外部 reward 源——reward provenance 仍是环境，与 §7 中 evaluator 作为 reward source 的情形有本质区别。

**Reward densification.** 与其在固定稀疏 reward 上更努力探索或归因，不如从环境本身挖掘可程序验证的中间结构，把单一终局 flag 改写为 dense composite reward。在 tool-use 与代码域，ToolRL [Qia25b] 把单次 tool call 的 reward 拆为 format correctness 与 tool name、arg name、arg value 三层匹配；SQL-Trail [Hua26d] 在 reason-execute-observe 循环里用 execution、turn-budget、schema grounding 等六项组成 composite reward；SQL-ASTRA [Li26r] 从结果表列值集合比较给出 dense partial-credit。在导航与具身域，LongNav-R1 [Hu26e] 用 geodesic progress shaped reward 加 terminal SPL 替换纯 sparse success。GUI 与 VLA 域广泛采用 rule-based verifiable reward——GUI-R1 [Luo25b]、AgentCPM-GUI [Zha25an]、SimpleVLA-RL [Li25aa] 在 format 合法性上叠加 action-type、click-point、text-match、bbox 命中等可判定项；UI-S1 [Lu25j] 在 semi-online 设定下由 offline ground-truth matching 提供 reward。VLM as Decision-Making Agents [Zha24s] 把 CoT 加 action 当作端到端 text rollout，用 λ 重加权 reasoning token 的 log-prob 贡献后以环境 reward 做 PPO。AgentRL [Zha25ag] 将这些范式扩展为多任务 framework，以 task advantage normalization 稳住多任务 RL；Generalization in Mobile Agents [Gu26b] 在异步 emulator 上验证大规模 RL 训练的泛化行为。Q-SFT [Hon24] 处于形式边界——训练形式像 SFT，但 sample weight 由 Bellman target 给出，机制更接近 offline value-based RL；reward provenance 仍是环境信号，归本节。

### 5.2.3 Preference-based Policy Internalization

Preference-based internalization 从 agent experience 中构造轨迹间或步骤间的相对偏好，用 DPO 或其他 pairwise optimization 直接更新 Policy。源信号是相对序——优势轨来自成功任务或修正后的轨迹，劣势轨来自失败尝试。与 Imitation 丢弃失败轨、Environment-Reward 把失败轨压成负 scalar 不同，Preference 显式消费失败轨作为 negative 与成功轨配对，以 supervised-style loss 替代高方差 policy gradient。按偏好构造的粒度分 trajectory-level 与 step-level 两类。

**Trajectory-level preference.** DMPO [Shi24c] 把 DPO 从单轮 response preference 扩到 multi-turn trajectory preference，核心问题是长轨迹下 token 数量不对称导致偏好目标偏差——解决方式是引入 state-action occupancy measure 与 length normalization。ETO [Son24] 先用 expert trajectory 做 behavior cloning，再让 policy 主动探索，把成功示范与探索中的失败轨配成 failure-success pair 用 DPO 持续更新。Agent-RLVR [Da25] 在 SWE 环境里用 guidance 帮助模型探索更可能成功的修复轨迹，再依 unit test pass/fail 构造 preference pairs 做 DPO。

**Step-level and element-level preference.** Trajectory-level preference 面临与 sparse environment reward 相同的 credit assignment 困难——只知道整条轨迹更好，不知道哪一步关键。Step-wise DPO for Tool Use [Che24k] 在 tool-use inference tree 中把同一父节点下成功 step 优于错误分支 step 作为 step-level preference pair。HPL [Gao25c] 同时引入 trajectory、step、action group 三层偏好，其中 group-DPO 用 MC rollout 估计 action group 的 return，填补了 trajectory 太粗、step 太细之间的粒度空缺。WEPO [Liu25z] 把偏好进一步收缩到 web element 层面，用目标元素对 DOM 距离近的干扰元素做对比训练，标签来自 benchmark GT 与 DOM 结构而非 learned judge。

### 5.2.4 Discussion

三类的核心差异在 policy update 消费了轨迹经验的哪个侧面，由此衍生出不同的信号承载力、训练稳定性与能力上限画像。Imitation-based 直接消费成功动作序列，cold-start 阶段能快速教会模型动作空间、输出协议与基本交互流程；能力上限受示范覆盖限制——只含有限场景的成功路径会让模型学到表层启发式而非深层策略；失败经验被完全丢弃。Environment-Reward-based 能通过试错发现超出示范的新策略，能力上限最高；代价是 reward 稀疏、credit assignment 困难、online rollout 昂贵、reward hacking 风险，且 RL 更新由高方差梯度驱动，一次坍缩或 hacking 造成的损伤不像编辑 Tokenized 载体那样可局部回退。Preference-based 介于两者之间——supervised-style 训练不需直接估计高方差 policy gradient，比 RL 稳；显式消费失败轨而不像 Imitation 浪费失败经验；局限是 preference pair 的构造质量直接决定效果，trajectory-level preference 的 credit assignment 困难与 sparse reward 同源。

三类在实践中常组合为同一 pipeline 的不同阶段：cold-start 用 imitation 立起格式与协议，能力突破交给 reward optimization 或 preference learning。Environment-Reward 与 Preference 都沿 credit assignment 的演化轴下沉——前者向 turn/step/token，后者向 step/group/element——本质区别在监督形式：一个是绝对的可验证 reward 进 RL objective，一个是相对 pair 进 supervised loss。三类还共享一个 Parametric 载体特有的属性：经验写进权重后不可局部寻址，新增或修正一类行为需要重新训练，不像 Tokenized 载体可以逐条编辑。这一属性是 Parametric 相对 Tokenized 的根本性 trade-off，§8 中将与其他 pathway 一并对比。
