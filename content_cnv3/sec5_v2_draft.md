## 5.2 Tokenized-to-Policy Transformation (Policy Internalization)

Policy Internalization 把 Tokenized agent experience 内化为 Policy 参数，使序贯决策能力固化在权重中。按 policy update 消费的经验信号形态，本节分为 Imitation-based、Environment-Reward-based 与 Preference-based 三类。本节与 §7 的边界由信号 provenance 决定：信号来自环境可验证结果或 rule-based verifier 时属本节；信号来自参数化 evaluator 时，转化先经 P4 再经 P6，归 §7；参数化 evaluator 仅用于数据筛选、其分数不进 loss 时，工作仍归本节。

### 5.2.1 Imitation-based Policy Internalization

Imitation-based internalization 把高质量 agent trajectories 作为监督示范，通过 behavior cloning 写入 Policy 参数。环境反馈不进入优化目标，只承担数据筛选。按示范来源分 self-generated experience 与 teacher demonstrations 两类——二者在能力上限上有本质区别：前者受限于 agent 当前的探索能力，后者受限于 teacher 的覆盖范围。

**Learning from self-generated experience.** 核心挑战是筛选——agent 产生的大多是失败轨迹，只有少数可被模仿。[Pat24] 在 WebArena 中以 environment error 与 self-critique 筛选自生成轨迹中 plausible 的动作做 SFT，失败经验仅用于告知"哪些不该学"。NNetNav [Mur24b] 通过无监督探索采集网页交互，再用 hindsight instruction relabeling 把交互改写成 demonstrations 后做 SFT，ORM 仅用于轨迹过滤——属 P6 边界。AppVLM [Pap25b] 与 [Guo25d] 进一步让 agent 在线交互、持续将新成功轨迹加入训练集——RL 在其中扮演 data discovery 而非 optimization 角色，最终 policy update 仍是 success-only 数据上的最大似然。

**Learning from teacher demonstrations.** 核心挑战是获取与覆盖——高质量示范昂贵，且 teacher 的成功路径未必覆盖 agent 会犯的所有错误。[Pan24] 在 SWE-Gym 中以 unit test 判定 patch trajectory 成败，做 rejection-sampling fine-tuning。AgentTuning [Zen23d] 把多环境 GPT-4 生成的 thought-action trajectories 与通用 instruction 数据混合训练，展示 agent 行为协议可与通用 instruction-following 联合学习。Explorer [Pah25] 通过 GPT-4o 多 agent pipeline 合成 multimodal web trajectories，经 Task Verifier 过滤后对学生模型做 SFT。Go-Browse [Gan25b] 与 AndroidGen [Lai25d] 引入参数化 evaluator 辅助筛选——前者用 VLM-as-a-judge 判定轨迹成败，后者用 StepCritic 把 teacher 长轨迹切成成功子段——但 evaluator 分数均不进 policy loss，属 P6 边界。

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
