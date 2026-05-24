# 5. Tokenized-to-Parametric Transformations

经验从 Tokenized 载体到 Parametric 载体的转化包含两条 pathway：Evaluator Internalization（§5.1）把交互经验固化为评估能力，Policy Internalization（§5.2）把交互经验固化为决策能力。两条 pathway 共享同一类源端——agent trajectory、reasoning trace、tool-use log、action history、execution outcome 等离散经验记录，差别在目标载体的功能角色：Evaluator 参数回答"如何判断行为质量"，Policy 参数回答"如何生成行为"。

## 5.1 Tokenized-to-Evaluator Transformation (Evaluator Internalization)

Evaluator Internalization 把 Tokenized agent experience 内化为 Evaluator 参数，使评估能力固化在权重中而非每次推理通过 prompt 临时激发。产物形态包括 outcome reward model、process reward model、verifier、critic、judge、value model、failure detector 与 diagnostic feedback model，是 §7 中复合 pipeline 的核心中间件。判定属于这条 pathway 的硬条件是 Evaluator 参数被经验数据实质更新；纯 prompt 触发评估行为、参数不变的 LLM-as-a-judge 不在此列。

### 5.1.1 Outcome-supervised Evaluator Internalization

Outcome-supervised internalization 把监督信号绑定到完整候选——一条 response、整段轨迹或整个 episode 被映射为单一评价标签。outcome label 易于从环境信号、执行结果或人工裁判得到，对具有明确成功标准的任务可直接对齐最终目标。

#### Discriminative Outcome Evaluators

判别式 outcome 评估器把完整候选映射为一个标量或离散类别，下游消费路径最短。

机器人 episode-level success / failure detector 构成最集中的一簇。Vision-Language Models as Success Detectors [Du23]（边界，多数样本是 success detection 视角而非显式 agent decision trajectory）把 success detection 写成 visual question answering，用 clip-level 成功标签对 Flamingo 做 SFT。I-FailSense [Gri25] 把这条思路扩展到跨任务 failure detection，先对 PaliGemma2 做 LoRA SFT，再在多层 hidden states 上训练 FailSense 分类块，正例来自原指令、负例来自与轨迹语义不匹配的指令。SAFE [Gu25b] 把输入换成 VLA policy 的内部 latent embedding，以 MLP 或 LSTM 在 rollout prefix 上学习随时间变化的 failure probability，配合 conformal threshold 触发 abort。

围绕 episode-level scalar reward 自身的细化沿两个方向展开。RoboReward [Lee26b] 在 OXE 与 RoboArena 的真实 rollout 上做 counterfactual relabeling 与 negative clipping，构造 1–5 级 episode rubric，用 SFT 让 Qwen3-VL 回归离散 progress。VLP [Liu25w] 不学绝对分而学相对偏好，从 Meta-World 的 expert / medium / random 三档轨迹中以 Intra-Task、Inter-Language、Inter-Video 三类规则构造比较标签，按 Bradley-Terry 学习 cross-modal preference。

环境外的 episode-level signal 在 web 域以两种形态出现。WebRL [Qi24] 在自演化在线课程 RL 中训练 outcome reward model，依据用户指令、历史动作与最终页面状态判定整条 web trajectory 是否完成任务。POLICYGUARDBENCH [Wen25b] 把判定目标从 task success 移到 policy violation——在 WebArena trajectories 上用 LLM 标注 obligation、prohibition、ordering、conditional 四类规则违反，用 SFT 训练一个既能消费完整轨迹也能消费 prefix 的 guardrail evaluator。

#### Generative Outcome Evaluators

生成式 outcome 评估器除 verdict 外还产出 judging rationale、failure reasoning 或 repair suggestion，信息密度更高，下游可塌缩为标量也可保留全文驱动 refinement。

reasoning 域的基本范式由 Generative Verifiers [Zha24o] 确立——把 reward modeling 写成 next-token prediction，既有直出 Yes / No 的 GenRM-Direct，也有先生成 CoT rationale 再给 verdict 的 GenRM-CoT，并探索 generation 与 verification 的联合训练。沿此范式，S2J [Sun25l]（边界，监督锚定 pairwise preference 而非典型 agent trajectory）让 judge 在判断前先自行解题，把 solving reward 与 judging reward 联合送入 DAPO；J4R [Xu25i]（边界，对象是 reasoning answer pair）用 EIS-GRPO 让 judge 在 response order swap 等等价初始状态上保持一致的 judgment correctness，压低位置偏置与表面格式干扰。

面向"让 critique 帮助下游修复"的目标，CTRL [Xie25c] 以单测通过为奖励，先用 execution-guided synthetic critique 做 SFT，再用 GRPO 直接优化 critique 让 generator 更可能产出通过测试的代码。AgentV-RL [Zha26ac]（边界，验证轨迹偏向 candidate solution 而非外部 agent 交互）把 verifier 做成多轮 tool-augmented agent，先做 rejection fine-tuning 学高质量 verifier 轨迹，再用 GRPO 以 verdict 与 ground truth 的一致性为奖励。Co-Evolving Critics [Li26l] 把 critic 与 actor 嵌入 dual-track GRPO：critic 给出 diagnosis 文本，actor 据此重写轨迹，critic 的奖励由 outcome model 与 saturation-aware gain 共同计算，避免 critic 随 policy 进化而失效；尽管训练采用 co-evolution，critic 仍是可独立调用的 standalone evaluator。RL4F [Aky23]（precursor，训练对象是通用 NLP 输出修复而非 agent 交互经验）以 refined output 相对 ground truth 的任务指标作为 PPO 奖励训练 critique generator，是这条 critique-driven repair 思路的早期形态。

具身与 computer-use 域里，CriticGPT for Robotic Manipulation [Liu24g] 从 Meta-World 不同阶段的操作视频出发，用环境全信息脚本自动生成 pairwise analysis 与 preference，对 LLaVA 做 LoRA 微调；下游再用 CriticGPT 的 preference 经 Bradley-Terry 训练独立 reward model 接入 DrQ-v2。AHA [Dua24] 通过 FailGen 在成功 demonstration 上注入七类失败模式，按 visual instruction tuning 让 LLaVA 同时输出 yes / no 与自由文本 failure rationale。ARMOR [Qi26] 在 Qwen2.5-VL 上联合训练 BCE detection head 与 next-token reasoning decoder，先离线 imitation 预热再做在线 self-refinement，使模型在多轮生成 detection 与 reasoning 时按自信度选择结果。Video-Based Reward Modeling for Computer-Use Agents [Son26d] 以 AgentNet、ScaleCUA、OSWorld 的执行视频与 instruction-translated hard negatives 训练 ExeVRM，配合 spatial 与 temporal token pruning 处理长视频，输出 video-level success judgment 与失败定位。

### 5.1.2 Process-supervised Evaluator Internalization

Process-supervised internalization 把监督信号分配到中间步骤、动作前缀或单步 decision，把"该步是否正确、是否有希望、是否推进任务"这类局部判断写进 Evaluator 参数。动因来自一项经验观察：长程 agent 的失败通常不是终局的突然事件，而是若干局部错误的累积，单一 outcome label 无法把这些局部错误从一条整体失败的轨迹中分离出来。

#### Discriminative Process Evaluators

判别式 process 评估器对每个 step、prefix 或 state-action 对输出标量分，是这一支文献最密集的一簇。

reasoning PRM 谱系奠定了基本范式。Let's Verify Step by Step [Lig23] 在 PRM800K 的 75K 数学解答上用人工 step-level 标签训练 PRM，对每一步给 positive / negative / neutral judgment。OmegaPRM [Luo24] 用 MCTS 加 binary search 自动定位 first error，把人工标注替换成 soft process label。Rewarding Progress [Set24] 把监督目标从 step correctness 改为 step advantage——从每个 prefix 展开 Monte Carlo rollout 估计未来成功概率，让 Evaluator 直接回答"这一步是否真把未来成功率推高"。PQM [Li24m] 把 PRM 改写成带 margin 的 Q-value ranking 问题，用 Plackett-Luce 损失替代独立 BCE，强制正确前缀的成功概率高于错误前缀。PathFinder-PRM [Pal25] 引入 hierarchical supervision，先预测 math error 与 consistency error 两层错误类型，再预测最终 correctness reward。BiRM [Che25s] 在同一 backbone 上联合训练 reward head 与 value head——前者评估已走过步骤的局部正确性，后者估计 partial trajectory 仍然通向正确答案的概率，相当于把 backward-looking 与 forward-looking 两类语义同时写入 Evaluator。

agentic、GUI 与 web 域把这些抽象 process signal 落到与环境状态变化对齐的 step-level 评估。AgentPRM [Xi25b] 把 reasoning PRM 推广到多步 agent 决策，用 TD 与 GAE 从 rollout 自动构造 state-action 上的 Q-value 与 advantage 伪标签。ProgRM [Zha25z] 在 GUI 轨迹中用 LCS recipe matching 自动定位 key step 并分配归一化 progress label。Agentic-Q [Wan26s] 让终局 success 反传到 state-thought-action 三元组，训 step-wise success probability estimator。Advancing Mobile GUI Agents [Dai25] 用 Pairwise Process Preference——同一步内正确动作分数高于若干错误动作——以 Q-LoRA 微调 backbone 与评分头。IntentScore [Che26s] 把 planning intent 作为条件信息融入 action encoder，用 InfoNCE 与 margin ranking 学习单步 state-action-intent 相容性，以极低延迟服务 test-time reranking。GAIA [Wan26p] 把训练做成 data flywheel：先以正确 / 错误 action 与 ground truth 比对训练第一轮 ICM，再用 critic 难例回流训练第二轮 ICM-r2，持续吸收真实 GUI agent 的错误分布。

code 域的 SWE-Shepherd [Dih26] 把读文件、编辑、跑测试等中间动作用启发式赋即时 progress 奖励（相关文件访问、目标文件修改、测试结果变化），折扣累积形成 step-wise target，用 qLoRA 加 MSE 训练 repo-level PRM。具身领域的三项工作走略偏离主轴的边界路径：RL-VLM-F [Wan24l]（边界，输入为 observation pair 而非显式 state-action token）用 prompted VLM 给 observation image pair 两阶段分析后产生 ternary preference，按 Bradley-Terry 训练独立 RM 接入 SAC；Video-Language Critic [Ala24]（边界，缺少显式 agent action token）以 contrastive cross-entropy 与 sequential ranking loss 训练 CLIP 初始化的图文-时间编码器，强制成功视频中后期片段分数高于前期；Large Reward Models [Wu26e]（边界，监督来自大规模视频与自动时序标签）在同一 VLM backbone 上分别用 LoRA、SFT、DPO 学习 contrastive、absolute progress 与 completion 三类 reward head，把 24 个来源的视频时序经验内化进统一 LRM。

#### Generative Process Evaluators

生成式 process 评估器在每个中间步骤生成 critique、错误诊断或修正建议——不止判定该步好坏，还解释违反了什么约束、错误属于何种类型、应朝什么方向修正。

reasoning 域的三项工作强调 deliberate critique。DeepCritic [Yan25u] 先用 Qwen2.5-72B 生成 4.5K 条 deliberate critique 做 critique teaching SFT，再用 PRM800K 与 MC 自动标注的 step correctness 数据做 critique incentivization GRPO，产物是长文本 rationale 加 step-level 正负判断。AutoMathCritique [Xi24] 走相近路径：在 GSM8K、MATH 上让 actor 生成 flawed reasoning paths，GPT-4o 标注首个错误步骤，再用 Monte Carlo soft filtering 留下真正有助修正的 MathCritique-76k 做 SFT。StepWiser [Xio25c] 先训 chunk segmentation 模块把 reasoning chain 自分块，再用 MC continuation 估计每个 chunk 前后的 Q-value 变化构造 Abs-Q、Rel-Effective、Rel-Ratio 三类标签，用 GRPO 训练在给出 Positive / Negative verdict 前先写出 meta-reasoning 的 generative judge。

GUI 与 web 域是生成式 process 评估器最密集的领域。GUI-Shepherd [Che25h] 把 AndroidWorld 在线 rollout 与 AndroidControl 单步状态汇成约 52K 样本，人类提供二值 step correctness、GPT-4o 补 CoT rationale，对 UI-TARS 做 SFT。GUI-Critic-R1 [Wan25q] 是 pre-operative critic——动作执行前依次生成 observation analysis、possible result、critique、correctness score 与 corrective suggestion——先做 RFT cold-start，再用 Suggestion-aware GRPO 强化。OS-Oracle [Wu25m] 通过 operation failure、error recovery、mistimed termination、element localization 四类错误注入合成负例，先 SFT 学 reason 与 judgment，再用 CP-GRPO 训跨平台 critic。WebArbiter [Zha26ab] 是 principle-guided generative PRM——先蒸馏 o3 教师的 principle-induced reasoning，再用 verifiable correctness reward 做 GRPO 对齐，产物含 principle、structured justification 与 preference verdict。Web-Shepherd [Cha25b] 把 web process evaluation 做成 checklist-grounded generative judging，对每个 checklist item 生成 Yes / No / In-Progress 判断，并用 verbalizer 读出标量 reward。

具身领域，SOLE-R1 [Sch26] 把真实与模拟机器人视频扩展为 1.2M 条 spatiotemporal CoT 与 progress trace——几何距离、时间反转与偏离注入自动得到逐时刻 progress label——先 SFT 学结构化 reasoning 加 progress value，再用 RLVR 加 GRPO 优化。在不可验证的多轮 search 任务上，PPRM [Xu25h] 按 correctness、relevance、consistency 等原则给 step score，再通过 ReNorm 把 process reward 与 outcome reward 校准到同一尺度送入 PPO。一项边界工作 Don't Act Blindly [Zha26z]（边界，verification 内嵌进 policy 而不产出可独立分离的 standalone evaluator）让 GUI agent 在每步生成 Think、Verification、Action、Expected Effect 四段，用 Verification-Action-Effect GRPO 训练，推理时读取 SUCCESS / NO_CHANGE 判定触发自纠；其参数化结果不能像 standalone PRM 那样被独立复用。

### 5.1.3 Discussion

两条监督粒度与两种产物形态构成四个交叉格，文献分布显著不均。outcome 判别式由经典 reward modeling 接口直接继承，工程最成熟、文献最厚——在具身的 episode-level success detection 上几乎是默认选择，下游消费直接落在 scalar reward。process 判别式围绕 credit assignment 快速扩张，演化轴是从 correctness 到 advantage、progress、Q-value、bidirectional reward 的语义细分，再向 GUI、computer-use、code、embodied 等带显式中间状态的领域落地；代价是 step-level label 的获取成本（要么人工标注，要么 MC 自动估计）与噪声。生成式两支让 Evaluator 输出可读 critique 或 diagnosis，下游可塌缩为标量进入 Evaluator-Driven Optimization 的 RL、可取 binary 做 Best-of-N 筛选、也可保留全文驱动 step-wise refinement——产物形态与下游 utilization 自由度间存在单调关系，生成式自由度最大。代价是 critique 的正确性缺乏自动验证——一条听起来合理的 critique 可能与环境真实反馈不一致——这是 Evaluator Internalization 留给后续工作的开放性难题，仅靠本节文献本身无法收敛。

跨监督粒度看，process 监督换更细的 credit assignment，付出标注成本与噪声；跨产物形态看，生成式以更高推理成本换更丰富的下游 utilization。两条轴上的选择由下游任务的 verifiability 与监督预算共同决定，不存在普适最优。

## 5.2 Tokenized-to-Policy Transformation (Policy Internalization)

Policy Internalization 把离散化的 agent experience 内化为 Policy 参数，使序贯决策能力固化在权重中。源端是各类 Tokenized artifacts——自然语言轨迹、工具调用记录、代码编辑历史、GUI 操作序列、reasoning chains；转化后，模型在后续任务中无需显式检索、拼接或重放原始经验即可完成决策。本节与 §7 中 Evaluator-Driven Optimization 的边界由 reward 或 preference 信号的 provenance 决定：信号是非参数化的——环境可验证结果、unit test、ground-truth match、rule-based verifier——经验直接 Tokenized → Policy，属本节；信号来自参数化 evaluator（trained RM、PRM、LLM-as-a-judge）时，转化先经 P4 再经 P6，是复合 pipeline，归 §7。参数化 evaluator 仅用于筛选或重构训练数据、其分数不进 policy update 的 loss 时，经验仍属直接内化，工作仍归本节。

### 5.2.1 Imitation-based Policy Internalization

Imitation-based internalization 把高质量 agent trajectories 当作监督示范，通过 behavior cloning、SFT 或 rejection-sampled fine-tuning 把示范动作序列写入 Policy 参数。环境反馈不进入优化目标，只承担 data selection 与 data construction——筛掉失败 rollout、过滤无效工具调用、保留通过测试的代码修改。子类归属看 policy weight 被改写时所用的 objective，与方法是否冠以 RFT、ReST 或 RL 之名无关。

主线机制是 success-filtered behavior cloning，loss 始终是成功数据上的最大似然。在 web agent 域，[Pat24] 以 environment error 与 self-critique 过滤 WebArena 中自生成的轨迹，在 QLoRA 下做 autoregressive SFT。SWE-Gym [Pan24] 用可执行 unit test 判定 patch trajectory 成败，以 rejection-sampling fine-tuning 完成 policy update；同文另训的 verifier 只做 reranking，不进 agent 自身的 loss，不改变归类。Go-Browse [Gan25b] 通过 structured exploration 采集 web trajectories 后仅对成功轨做 SFT，成功标签由 VLM-as-a-judge 给出但仅用于筛选——属 P6 边界（参数化 evaluator 介入但不进 loss）。NNetNav [Mur24b] 在开放网页中做无监督探索，再用 hindsight instruction relabeling 把交互改写成 instruction-following demos 做 SFT，ORM 同样只做轨迹过滤。AndroidGen [Lai25d] 用 StepCritic 把长 Android 轨迹切成成功子段并 augmentation，最终更新仍是 LoRA-SFT，critic 分数不进 loss。

多 teacher 蒸馏与跨任务 instruction tuning 沿同一机制扩展。AgentTuning [Zen23d] 把多环境中 GPT-4 生成的 thought-action trajectories 与 ShareGPT 通用数据混合做 NLL SFT，让模型同时获得 agent 行为协议与通用 instruction-following。Explorer [Pah25] 让 GPT-4o 多 agent pipeline 合成 multimodal web trajectories，由 Task Verifier 过滤后对学生模型做 next-action SFT。AppVLM [Pap25b] 名义上做 ReST / RFT，最终 policy 更新仍是 success-only 数据上的 MLE-SFT——失败轨 return = 0 且不进训练集，按 objective 判定属本子类。具身 VLA 的 [Guo25d] 名义为 online RL，Stage 1 只在 action head 上用 binary reward 做探索、Stage 2 才对 expert 与新发现成功轨的并集做全模型 MSE supervised learning，按最终全模型更新机制归本子类。

部分工作在 imitation 前对轨迹做轻量加工以提升示范信号的质量与覆盖——AndroidGen 的 StepCritic 切段、NNetNav 的 hindsight relabeling 均属此类，加工只重排或重标注轨迹内容、不改变载体层次，仍是 Imitation 内部的预处理。若加工把经验跨载体重构——WebCoT [Hu25i] 把 reflection、branching、rollback 痕迹 verbalize 成显式 CoT 再 SFT、AgentTrek [Xu24] 把 web tutorial 编译成 Goal-Observation-Reasoning-Action schema 再 SFT——则前置步骤本身是 Narrative → Narrative 或 Narrative → Schematic 的 Transformation，与 Imitation 构成 P1 → P5 或 P2 → P5 的链式复合，按 §7 处理。

### 5.2.2 Environment-Reward-based Policy Internalization

Environment-Reward-based internalization 让 agent 与环境交互产生 trajectories，用非参数化、可验证的反馈信号直接进入 policy optimization 的 objective。可验证信号涵盖任务成败、unit test pass / fail、execution output、SQL execution correctness、ground-truth answer match、GUI 任务完成状态、机器人操作成败等环境本身可程序判定的结果。失败轨迹经 reward 转成负信号后同样进入优化，这点与 Imitation 只消费成功轨迹动作不同。

基本前提由两项早期工作确立。GLAM [Car23] 把 FLAN-T5 放入 BabyAI-Text，以任务成功 sparse reward 经 PPO 做 online grounding。LLaRP [Szo23] 连接冻结的 LLaMA 与视觉编码器为 embodied policy，以 success、subgoal completion、invalid-action penalty 组成的环境 reward 经 DD-PPO 训练 adapter 与 heads。这两项展示：只要动作可在环境中执行、环境能返回可验证结果，Tokenized trajectory 即可直接转化为 Policy weights。

设定推进到长程多轮的真实环境后，一个核心困难暴露：一条几十步的轨迹只在终局拿到一个稀疏的可验证 reward，信号难以被有效利用。此后工作沿三层推进。

**让稀疏信号不消失。** 长程 agent 在训练早期极易坍缩到低探索策略，一旦坍缩便不再产生成功轨迹。EPO [Xu25k] 在 PPO 或 GRPO 外层加 trajectory-level entropy regularization 与 entropy smoothing，缓解 sparse-reward multi-turn RL 的 exploration-exploitation cascade failure。Agentic Reinforced Policy Optimization [Don25d] 在多轮 tool-use 中用 entropy-based adaptive rollout，在高不确定性步骤触发局部 branching。AEPO [Don25c] 把 entropy 同时纳入 advantage 与 clipping，并动态分配 global 与 branch rollout budget。EMPG [Wan25ad] 用当前 entropy 缩放每步 advantage 并加上鼓励进入更低熵后继状态的 future-clarity bonus。ARPO [Lu25f] 在 GUI 环境中维护成功 trajectory replay buffer，当采样组全失败、无梯度时从历史缓冲注回正样本。AgentGym-RL [Xi25c] 提出 ScalingInter-RL，以先短后长的 horizon curriculum 让 agent 先在可完成的短程任务上拿到信号。SoLS [Pap25c] 在 mobile app control 中用非对称 actor update——正优势样本强更新、负优势样本做 PPO-like 保守正则——并配合成功转移回放 STR。

**让信号可归因到具体决策。** 归因粒度从整轨持续下沉到 turn、step、token。WebAgent-R1 [Wei25] 以 M-GRPO 并行采样 browser trajectories，reward 由 URL match 与 Playwright verification 给出。[Gol25] 在 SWE 环境中以 unit test pass / fail 加 trajectory length penalty 做 token-level DAPO。ArCHer [Zho24f] 先用环境 reward 训练 utterance-level Q critic，再把 multi-turn advantage 传给 token actor。Turn-PPO [Li25ae] 把多轮交互建模为 turn-level MDP，在 turn 粒度上用 critic 做 GAE。GiGPO [Fen25c] 用 anchor-state grouping 比较不同 rollout 在相同中间状态下的动作，同时构造 episode-level 与 step-level relative advantage。LOOP [Che25af] 在 AppWorld API 环境用 leave-one-out PPO 做 critic-free token-level 更新。Information Gain-based Policy Optimization [Wan25y] 用每轮交互前后 ground-truth answer log-prob 的增量定义 information-gain intrinsic reward，把 observation 的真实信息贡献转成 turn-level dense 信号。RLVMR [Zha25ao] 给轨迹挂 `<planning>`、`<explore>`、`<reflection>`、`<monitor>` 标签，用 rule-verifiable process reward 加 outcome reward 让 meta-reasoning 行为可被显式监督。actor-critic 类方法中的 critic 是由环境 reward 在 RL 算法内部 bootstrap 而来的 expected-return estimator，不是独立训练的外部 reward 源——reward provenance 仍是环境，故归本节，与 §7 中 evaluator 作为 reward source 的情形有本质区别。

**让信号在源头变密。** 与其在固定的稀疏 reward 上更努力探索或归因，不如从环境本身挖掘可程序验证的中间结构，把单一终局 flag 改写为 dense composite reward。ToolRL [Qia25b] 把 tool-use reward 拆成 format correctness 与 tool name、arg name、arg value 的三层匹配。SQL-Trail [Hua26d] 在 reason-execute-observe 循环里用 execution、turn-budget、schema grounding、bigram overlap、syntax、format 六项组成 composite reward。SQL-ASTRA [Li26r] 的 Column-Set Matching Reward 从结果表列值集合比较给 dense partial-credit，再用 Asymmetric Trajectory Reward 聚合整轨。LongNav-R1 [Hu26e] 在长程 navigation 中用 geodesic progress shaped reward 加 terminal SPL，以 critic-free time-aware baseline 做 REINFORCE++ 风格更新。GUI 与 VLA 域把 rule-based verifiable reward 直接送入 GRPO：GUI-R1 [Luo25b]、AgentCPM-GUI [Zha25an]、SimpleVLA-RL [Li25aa] 在 format 合法性之上叠加 action-type、click-point、text-match、bbox 命中等可判定项；UI-S1 [Lu25j] 在 semi-online RL 中用模型自生成历史并由 patch module 续接，reward 由 offline ground-truth matching 提供。VLM as Decision-Making Agents [Zha24s] 把 CoT 加 action 当作端到端 text rollout，在用 λ 重加权 reasoning token 的 log-prob 贡献后用环境 reward 做 PPO。AgentRL [Zha25ag] 把这些范式扩展为多任务 framework，以 deterministic verifiable rewards 加 task advantage normalization 稳住多任务 RL；Generalization in Mobile Agents [Gu26b] 在异步 emulator 上验证 instance、template、app 三层泛化。Q-SFT [Hon24] 处于本子类的形式边界——形式像 SFT，但 sample weight 由 Bellman target 或 Q-value 给出，机制更接近 offline value-based RL；reward provenance 仍是环境信号，归本节。

### 5.2.3 Preference-based Policy Internalization

Preference-based internalization 从 agent experience 中构造轨迹间或步骤间的相对偏好，用 DPO 或其他 trajectory-pair optimization 直接更新 Policy。源信号是相对序：优势轨来自成功任务、通过验证的执行、修正后的轨迹或更高效操作路径，劣势轨来自失败尝试、错误工具调用、未通过测试的代码修改。这条 pathway 显式消费失败经验——Imitation 丢弃失败轨，Environment-Reward 把失败轨压成一个负 scalar，Preference 则把失败轨作为 negative 与成功或修正轨配对。

trajectory-level preference 是这条路径的入口。DMPO [Shi24c] 把 DPO 从单轮 response preference 扩到 multi-turn trajectory preference，引入 state-action occupancy measure 与 length normalization 处理长轨迹下的 preference objective。ETO [Son24] 先用 expert trajectory 做 behavior cloning，再让 policy 主动探索，把成功示范与探索中的失败轨配成 failure-success pair 用 DPO 持续更新。Agent-RLVR [Da25] 在 SWE 环境里用 guidance 帮助模型探索更可能成功的修复轨迹，再依 unit test pass / fail 构造 preference pairs 做 DPO；guidance 在此扮演数据生成器，不进 reward。

偏好粒度沿与 §5.2.2 平行的轴线下沉。Step-wise DPO for Tool Use [Che24k] 在 tool-use inference tree 中把"同一父节点下成功 step 优于错误分支 step"作为 step-level preference pair，在 SFT 后接续 DPO 优化。HPL [Gao25c] 同时引入 trajectory、step、action group 三层偏好，group 由 fixed、entropy 或 semantic segmentation 划出，最终目标是 BC 与三层 DPO 的复合，其中 group-DPO 是主要增益来源。WEPO [Liu25z] 把偏好收缩到 web element 层面，用目标元素对 DOM 距离近的干扰元素做对比训练 element selection policy，标签来自 benchmark GT 与 DOM 结构，不依赖 learned judge。

### 5.2.4 Discussion

三类的核心差异在 policy update 消费了轨迹经验的哪个侧面，由此衍生出不同的信号承载力、训练稳定性与能力上限画像。Imitation-based 直接消费成功动作序列，cold-start 阶段能快速教会模型动作空间、输出协议与基本交互流程；能力上限受示范覆盖限制——只含有限场景的成功路径会让模型学到表层格式或局部启发式，难以主动探索新策略；失败经验被完全丢弃。Environment-Reward-based 能通过试错发现超出示范的新策略，能力上限最高；代价是 reward 稀疏、credit assignment 困难、online rollout 昂贵、reward hacking 风险，且 RL 更新由高方差梯度驱动，一次坍缩或 hacking 造成的能力损伤不像编辑文本规则那样可回退。Preference-based 介于两者之间——supervised-style 训练不需直接估计高方差 policy gradient，训练比 RL 稳；显式消费失败轨而不像 Imitation 那样浪费失败经验；局限是 preference pair 的构造质量直接决定效果，trajectory-level preference 仍可能缺乏细粒度归因。

三类在实践中常组合为同一 pipeline 的不同阶段：cold-start 用 imitation 立起格式与协议，能力突破交给 reward optimization 或 preference learning。Environment-Reward 与 Preference 都沿 credit assignment 的演化轴下沉——前者向 turn / step / token，后者向 step / element / group——本质区别在监督形式：一个是绝对的 verifiable reward 进 RL objective，一个是相对的 pair 进 supervised loss。三类还共享一个 Parametric 载体特有的属性：经验写进权重后不可局部寻址，新增或修正一类行为需要重新训练。这一属性是 Parametric 相对 Tokenized 的根本性 trade-off，须把全章文献的相似行为汇总后才能浮现，§8 中将与其他 pathway 一并对比。