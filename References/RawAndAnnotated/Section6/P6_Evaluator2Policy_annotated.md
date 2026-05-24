[Title]: RLAIF vs. RLHF: Scaling Reinforcement Learning from Human Feedback with AI Feedback
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: Human preference pairs / AI-generated preference pairs (from off-the-shelf LLM)
- [Target Experience]: Policy weights aligned with preferences
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}, {human}
- [Utilization]: Policy generates summaries and dialogue responses aligned with human/AI preferences
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: Stage 1 (P4): 用 off-the-shelf LLM 生成偏好标注（AI Feedback），训练 reward model (RM)，替代人工标注。Stage 2 (P6): 用训练好的 RM 作为 reward signal，通过 RL (PPO) 优化 policy。核心贡献在 Stage 1——证明 AI Feedback 训练 RM 可达到与 human feedback 可比的效果。另提出 direct-RLAIF (d-RLAIF) 变体：跳过 RM 训练，直接从 off-the-shelf LLM 获取 reward 进行 RL。

[Title]: Constitutional AI: Harmlessness from AI Feedback
- [Pathway]: Narrative → Narrative → Evaluator → Policy (§8.3 + §8.2)
- [Source Experience]: Initial model samples + human-provided constitutional principles/rules
- [Target Experience]: Policy weights for harmless AI assistant
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {human}
- [Utilization]: Policy generates harmless responses to harmful queries by explaining objections
- [Method]: ⟨SFT⟩, ⟨RL: PPO⟩
- [Mechanism]: 整体为三段 composite。Stage 1 (P1): 从初始模型采样，生成 self-critiques 和 revisions（raw → refined Narrative），用 revised responses 做 SFT（对应 §8.3: Narrative(raw) → Narrative(refined) → Policy via SFT = P5）。Stage 2 (P4): 从 SFT 模型采样 response pairs，用 LLM 评估偏好（AI Feedback），训练 preference model (Evaluator)。Stage 3 (P6): 用 preference model 作为 reward signal 进行 RL (RLAIF)，优化 policy。整个 pipeline 实现了从 constitutional principles 出发、无需 human harmfulness labels 的无害化对齐。

[Title]: Direct Language Model Alignment from Online AI Feedback
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Online AI preference feedback (LLM annotator chooses preferred response from current policy's samples)
- [Target Experience]: Policy weights aligned via DPO
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Policy generates higher-quality responses evaluated by humans
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: 用 LLM 作为在线标注器（online AI feedback, OAIF）：每个 training iteration 从当前 policy 采样两个 response，由 LLM annotator 选择偏好，产生在线偏好数据，直接用 DPO 更新 policy。关键区别于传统 RLHF：不训练单独的 RM，而是在线生成偏好数据直接优化 policy。路径实质是 preference pairs (Narrative) → Policy via DPO (P5)，OAIF 的核心贡献在于让偏好数据是 online 和 on-policy 的。

[Title]: Self-Rewarding Language Models
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: Policy's own generated responses (self-generated)
- [Target Experience]: Improved policy weights with enhanced instruction-following and self-rewarding ability
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy generates better responses and provides higher-quality self-rewards for subsequent iterations
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: §8.1 self-reinforce 闭环 (Policy → Narrative → Policy)。Iterative DPO training：每轮迭代中，policy (LLM) 通过 LLM-as-a-Judge prompting 给自己的 responses 打分（Policy 外化为 Narrative preference judgments），然后用这些 self-generated preferences 做 DPO 训练更新 policy。两轴同时提升：instruction following 能力和 self-rewarding 判断能力。不训练单独 RM，policy 自身充当 judge。

[Title]: RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Generated samples scored and filtered by a reward model
- [Target Experience]: Policy weights via fine-tuning on high-reward samples
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy generates higher-quality, less biased samples
- [Method]: ⟨SFT⟩
- [Mechanism]: 用已有 reward model 对生成样本打分，筛选高 reward 样本（丢弃低质量样本），用过滤后的高质量样本做 SFT 更新 policy。本质是 reward-ranked rejection sampling + SFT，不涉及 RL 在线优化。Pathway 是 filtered trajectories (Narrative) → Policy via SFT (P5)。Reward model 在此作为 filter（工具），不被训练，因此不构成 Evaluator 中间步骤。

[Title]: BOND: Aligning LLMs with Best-of-N Distillation
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Best-of-N distribution derived from base policy + reward model rankings
- [Target Experience]: Policy weights that emulate Best-of-N sampling distribution
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy generates high-quality outputs at inference without N× sampling cost
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: 将 Best-of-N (BoN) sampling 的分布蒸馏到 policy：用 reward model 对 N 个候选打分选出最佳，构造 BoN 分布，通过 Jeffreys divergence (forward + backward KL 组合) 做 distribution matching，使 policy 生成的分布逼近 BoN 分布。Reward model 在此作为 BoN 选择器（固定工具），不参与训练。路径实质是 BoN-filtered generation distribution (Narrative) → Policy (P5)。

[Title]: BoNBoN Alignment for Large Language Models and the Sweetness of Best-of-n Sampling
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Best-of-n sampling distribution from base LLM
- [Target Experience]: Policy weights mimicking Best-of-n distribution
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy produces outputs preferred over base policy with minimal off-target effects
- [Method]: ⟨hybrid⟩
- [Mechanism]: 先进行理论分析：将 BoN 分布和各种 alignment 方法（RLHF, DPO）统一在 tilted distribution 框架中，证明 BoN 在 win-rate vs KL 的 trade-off 上近似最优。然后提出 BoNBoN Alignment：利用 BoN 分布的特殊结构设计 fine-tuning 目标，使 policy 直接逼近 BoN 采样分布。hybrid 由 distribution matching + SFT 组成。Reward model 作为 BoN 排序工具（不训练），路径为 BoN-filtered distribution (Narrative) → Policy (P5)。

[Title]: Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: Automatically constructed process-wise supervision data (math solution steps)
- [Target Experience]: Process Reward Model (PRM) weights AND improved policy weights via PPO
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: PRM used for verification (reranking) AND as reward signal for RL (PPO) training of policy
- [Method]: ⟨RL: PPO⟩, ⟨SFT⟩
- [Mechanism]: Stage 1 (P4): 自动构造 process-wise supervision data（通过 MCTS 等方法推断每个 step 的正确性），训练 Math-Shepherd PRM——一个为数学解题每步分配 reward score 的 process reward model。Stage 2 (P6): 用 Math-Shepherd 作为 dense reward signal，通过 step-by-step PPO 训练 policy。Stage 3 (独立用途): PRM 还用于 inference-time verification (reranking)。两阶段构成 §8.2 composite (Narrative → Evaluator → Policy)。

[Title]: Process Reinforcement through Implicit Rewards
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: Policy rollouts with outcome labels (correct/incorrect answers)
- [Target Experience]: Implicitly updated PRM AND improved policy weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy achieves higher accuracy on math and coding reasoning benchmarks
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 提出 PRIME (Process Reinforcement through IMplicit rEwards)：不需要单独训练 PRM 的阶段，而是利用 policy rollouts 和 outcome labels 通过 implicit process rewards 在线更新 PRM。核心机制：从 outcome label 推断 implicit process rewards，同时用于更新 PRM 和 policy。这本质上是一种在线联合优化：Narrative (rollouts with outcome labels) → Evaluator (PRM, implicit update) → Policy (via PPO with PRM dense rewards)。§8.2 composite 但 PRM 训练和 policy 训练在同一 loop 中隐式耦合。

[Title]: Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: Reasoning traces with automated progress-based labels
- [Target Experience]: Process Advantage Verifier (PAV) weights AND improved policy weights via online RL
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: PAV used for test-time search AND as dense rewards for online RL training
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: Stage 1 (P4): 训练 Process Advantage Verifier (PAV)。关键 insight：process reward 应衡量 progress——即在采取某步前后、生成正确答案的 likelihood 变化（对应 RL 中 step-level advantage 概念）。Progress 需在 distinct prover policy 下测量（而非 base policy），理论刻画了"好 prover"的条件。Stage 2 (P6): 用 PAV 作为 dense reward signal 进行 online RL 训练 policy。同时 PAV 也用于 test-time search。

[Title]: Autonomous Evaluation and Refinement of Digital Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Agent trajectories evaluated by domain-general automatic evaluators
- [Target Experience]: Improved agent policy via fine-tuning on evaluator-guided data
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Agent achieves 29% improvement on WebArena and 75% relative improvement in device control
- [Method]: ⟨SFT⟩
- [Mechanism]: 使用 domain-general automatic evaluator 评估 web navigation 和 device control agent 的 trajectories，然后用这些 evaluators 通过 fine-tuning 和 inference-time guidance 改进 agent 性能。Evaluator 在此作为自动评估工具（训练好的模型，不在此工作中更新），筛选或引导 trajectories 用于 SFT。路径：evaluator-filtered trajectories (Narrative) → Policy via SFT (P5)。

[Title]: WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning
- [Pathway]: Narrative → Evaluator → Policy (§8.2) + Policy → Narrative → Policy (§8.1)
- [Source Experience]: Agent interaction trajectories in web environments
- [Target Experience]: Outcome-supervised Reward Model (ORM) AND improved web agent policy weights
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Policy navigates web tasks (WebArena-Lite) with significantly improved success rate
- [Method]: ⟨hybrid⟩
- [Mechanism]: 混合 composite：包含三个组件。(1) Self-evolving curriculum: 从失败尝试中自动生成新任务——属于 §8.1 (Policy → Narrative → Policy) 的自生成闭环。(2) 训练 robust ORM (P4): 从 interaction trajectories 训练 outcome-supervised reward model 提供 feedback 信号。(3) Adaptive RL (P6): 用 ORM 信号通过 RL 训练 policy，配合 adaptive RL strategies 应对 policy distribution drift。hybrid 由 ⟨LLM-extract⟩ (curriculum generation) + ⟨SFT⟩ (ORM training) + ⟨RL: PPO⟩ (policy optimization) 组成。

[Title]: RL-VLM-F: Reinforcement Learning from Vision Language Foundation Model Feedback
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: Pairs of agent image observations with VLM preference labels
- [Target Experience]: Learned reward function (Evaluator) AND RL-trained policy weights
- [Source Modality]: [vis+txt]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}
- [Utilization]: Policy executes manipulation and control tasks without human-designed reward functions
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: Stage 1 (P4): Query VLM (vision language foundation model) 对 agent 的 image observation pairs 给出偏好（基于 text task description），从 preference labels 学习 reward function (Evaluator)，而非直接 prompted raw reward scores。Stage 2 (P6): 用学习到的 reward function 通过 RL 训练 policy。应用于 classic control 和 rigid/articulated/deformable object manipulation。

[Title]: AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Agent interaction trajectories in multi-turn decision-making tasks (web shopping, browser navigation)
- [Target Experience]: AgentPRM weights (process reward model for agent tasks)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: PRM used for test-time compute scaling (8× more compute-efficient) and applicable to RL of LLM agents (mentioned but not primary)
- [Method]: ⟨SFT⟩
- [Mechanism]: 针对 agent task 重新定义 PRM：不同于 LLM reasoning 中按"正确性"评分，agent actions 应基于"proximity to goal"和"progress"评分。提出 AgentPRM，通过 TD-based (Temporal Difference) estimation + GAE (Generalized Advantage Estimation) 从 trajectories 自动获取训练标签（比 prior methods 更 sample-efficient）。主要贡献在 PRM 构建（P4），RL 应用作为后续分析提及。若将 PRM 用于 RL training 则构成 §8.2。

[Title]: Meta-Rewarding Language Models: Self-Improving Alignment with LLM-as-a-Meta-Judge
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: Policy's own generated responses AND self-judgments
- [Target Experience]: Improved policy with better judgment AND instruction-following ability
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy achieves higher win rate on AlpacaEval 2 and Arena-Hard
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: §8.1 self-reinforce 闭环的扩展。在 Self-Rewarding LM 基础上引入 Meta-Rewarding 步骤：模型不仅 judging 自己的 responses，还 judging 自己的 judgements（Meta-Judge）。流程：Policy 生成 responses → Policy (as Judge) 评判 responses → Policy (as Meta-Judge) 评判 judgement 质量 → 用 judgement + meta-judgement 反馈通过 DPO 更新 policy。这个额外步骤解决了 iterative self-rewarding 中判断能力快速饱和的问题。

[Title]: Policy Improvement using Language Feedback Models
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Visual trajectories verbalized to language descriptions + LLM feedback identifying desirable behaviour
- [Target Experience]: Policy weights via imitation learning on LLM-identified desirable actions
- [Source Modality]: [vis+txt]
- [Target Modality]: [cross-modal]
- [Experience Source]: {teacher}
- [Utilization]: Policy improves task-completion rate in language grounding environments (Touchdown, ScienceWorld, ALFWorld)
- [Method]: ⟨SFT⟩
- [Mechanism]: 训练 Language Feedback Models (LFMs)：用 LLM 对 visual trajectories（语言化描述后）提供 feedback，识别哪些 actions 有助于完成任务（desirable behaviour）。然后用 LFM 识别的 desirable behaviour 做 imitation learning (behavioral cloning) 训练 policy。注意：此处 LLM feedback 是识别"哪些行为值得模仿"的过滤信号，而非训练单独的 evaluator 权重。路径：LLM-filtered desirable trajectories (Narrative) → Policy via SFT (P5)。

[Title]: Vision-Language Models are Zero-Shot Reward Models for Reinforcement Learning
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Pretrained VLM (CLIP) as zero-shot reward model
- [Target Experience]: RL-trained policy for humanoid control tasks (kneeling, splits, lotus position)
- [Source Modality]: [vis+txt]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}
- [Utilization]: Policy learns complex humanoid motor tasks from a single text prompt description
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 使用 pretrained VLM (CLIP) 作为 zero-shot reward model (VLM-RM)：仅需一句自然语言 task description，VLM 对 agent 的 visual observations 打分作为 reward，不训练 RM。核心是在 CLIP embedding space 中比较 goal vs baseline prompt 来定义 reward。可引入第二个 "baseline" prompt 做 projection 以去除非相关 embedding 维度。这是少数可标为纯 P6 的工作：VLM 作为 frozen Evaluator (V-Par)，其信号直接通过 RL 转化为 Policy (π-Par)。

[Title]: ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search
- [Pathway]: Policy → Narrative → Evaluator → Policy (§8.1 + §8.2)
- [Source Experience]: LLM-generated reasoning traces with oracle final correct answers
- [Target Experience]: Process reward model (PRM) weights AND improved policy weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy and PRM improve iteratively; PRM guides tree search for higher-quality trace collection
- [Method]: ⟨MCTS⟩, ⟨SFT⟩
- [Mechanism]: 多层 composite。核心循环：Policy 通过 MCTS* (process reward guided tree search) 生成 reasoning traces → 利用 oracle final correct answers 推断每个 step 的 process rewards（通过估计该 step 帮助到达正确答案的概率）→ 推断的 rewards 用作 value targets 训练/refine PRM (P4: Narrative → Evaluator) + 筛选高质量 traces 做 policy self-training (P5: Narrative → Policy)。同时 Policy 外化生成 traces (P7: Policy → Narrative)。整体构成 §8.1 闭环（Policy → Narrative → Policy）+ §8.2（Narrative → Evaluator → Policy），PRM 和 Policy 交替提升。

[Title]: Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: Agent interaction trajectories in WebShop environment (both successful and unsuccessful)
- [Target Experience]: Policy weights improved via iterative DPO on self-generated trajectories
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Policy achieves 340% relative increase in real-world booking scenarios
- [Method]: ⟨MCTS⟩, ⟨RL: DPO⟩
- [Mechanism]: §8.1 self-reinforce 闭环。Guided MCTS search + self-critique mechanism 生成 exploration trajectories（Policy → Narrative: P7）；使用 off-policy DPO 从成功和失败 trajectories 中学习，更新 policy（Narrative → Policy: P5）。关键创新：同时利用成功和失败 trajectories，MCTS 引导 exploration 解决 compounding errors 问题。Self-critique 机制提供中间反思信号。MCTS 作为 search 策略，不单独训练 evaluator。

[Title]: OpenWebVoyager: Building Multimodal Web Agents via Iterative Real-World Exploration, Feedback and Optimization
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: Agent exploration trajectories in real web environments with AI feedback
- [Target Experience]: Improved multimodal web agent policy weights
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Policy performs web navigation tasks with improving success rate across iterations
- [Method]: ⟨SFT⟩, ⟨RL: DPO⟩
- [Mechanism]: §8.1 self-reinforce 闭环。流程：(1) 先用 imitation learning 训练 base model 获得基本能力；(2) 让 agent 在开放 web 上探索，收集 trajectory feedback；(3) 用另一个 general-purpose model 评判哪些 trajectories 表现好；(4) 从 well-performing trajectories 学习（fine-tuning/DPO）改进 policy。Exploration-feedback-optimization 循环可多轮迭代。Teacher model 提供 feedback judgment，但 feedback 本身是 Narrative 形式，用于 policy 训练。

[Title]: Web-Shepherd: Advancing PRMs for Reinforcing Web Agents
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Web navigation trajectories with step-level preference annotations (WebPRM Collection, 40K pairs)
- [Target Experience]: Web-Shepherd PRM weights (process reward model for web navigation)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {human}, {teacher}
- [Utilization]: PRM used as verifier during inference (reranking) and potentially for RL training
- [Method]: ⟨SFT⟩
- [Mechanism]: 构建 WebPRM Collection（40K step-level preference pairs + annotated checklists），训练第一个专门针对 web navigation 的 process reward model (Web-Shepherd)。同时发布 WebRewardBench 作为 PRM 评估 benchmark。Web-Shepherd 比 GPT-4o 在 WebRewardBench 上高 ~30 points。当用作 verifier 时提升 web agent 性能。若将 PRM 用于 RL 训练 policy 则构成 §8.2 composite，但摘要主要强调 PRM 构建和 inference-time verification。

[Title]: GUI-Shepherd: Reliable Process Reward and Verification for Long-Sequence GUI Tasks
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: GUI interaction trajectories with human-annotated scores and GPT-4o generated rationales (52K interactions)
- [Target Experience]: GUI-Shepherd PRM weights AND PPO-improved GUI agent policy weights
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {human}, {teacher}
- [Utilization]: PRM serves as reward provider for RL training AND as verifier at inference; agent achieves +7.7 points on AndroidWorld
- [Method]: ⟨SFT⟩, ⟨RL: PPO⟩
- [Mechanism]: Stage 1 (P4): 在大规模 GUI interaction 数据集（52K, human-annotated scores + GPT-4o rationales）上训练 GUI-Shepherd PRM，提供 dense step-by-step feedback。Stage 2 (P6): 用 GUI-Shepherd 作为 reward provider 进行 multi-turn online PPO 训练 policy。PRM 同时用于 inference-time verification。首次在 GUI agent 领域进行 process supervision 的系统性研究。

[Title]: Real-World Offline Reinforcement Learning from Vision Language Model Feedback
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: Unlabeled offline robot manipulation datasets + VLM preference feedback
- [Target Experience]: Learned reward function AND offline RL-trained dressing policy
- [Source Modality]: [vis+txt]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}
- [Utilization]: Policy performs real-world robot-assisted dressing tasks
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 继承 RL-VLM-F 框架，扩展到 offline RL setting。Stage 1 (P4): 用 VLM (vision-language model) 对 offline dataset 中的 trajectory pairs 提供 preference feedback（基于 text task description），自动标注 reward labels，学习 reward function。Stage 2 (P6): 用学习到的 reward 通过 Implicit Q-learning (offline RL) 训练 dressing policy。应用于复杂的真实世界 robot-assisted dressing 任务。

[Title]: AdaRubric: Task-Adaptive Rubrics for LLM Agent Evaluation
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Task descriptions and agent trajectories in web navigation and tool use benchmarks
- [Target Experience]: AdaRubric evaluator (task-specific rubric generator + dimension-aware scorer)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Evaluator generates preference pairs for DPO training (+6.8 to +8.5 pp task success) and accelerates PPO convergence (+6.6 pp)
- [Method]: ⟨LLM-extract⟩, ⟨SFT⟩
- [Mechanism]: 针对 LLM-as-Judge 在 agent tasks 上的缺陷（固定 rubric 无法捕捉 task-specific 维度），提出 AdaRubric：从 task description 自动生成 task-specific evaluation rubrics；用 confidence-weighted per-dimension feedback 对 trajectories 做 step-by-step 评分；通过 DimensionAwareFilter 过滤 preference pairs（防止高分维度掩盖维度级失败）。生成的 preference pairs 随后用于 DPO (P5) 训练 agent。主要贡献在 Evaluator 构建 (P4)，为下游 policy 训练提供更可靠信号。

[Title]: Let's Verify Step by Step
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Human-annotated step-level feedback labels (PRM800K dataset: 800,000 step-level labels)
- [Target Experience]: Process-supervised Reward Model (PRM) weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: PRM used for training more reliable reasoning models (process supervision outperforms outcome supervision on MATH)
- [Method]: ⟨SFT⟩
- [Mechanism]: 系统比较 process supervision vs outcome supervision 对训练可靠推理模型的影响。收集 PRM800K（800K step-level human feedback labels）训练 process-supervised reward model。证明 process supervision 在 MATH 数据集上显著优于 outcome supervision。PRM 提供 per-step 反馈，用于训练 policy（可构成 §8.2 composite，但论文核心贡献在 PRM 构建和标注数据集）。Active learning 进一步提升 process supervision 效率。

[Title]: WebArbiter: A Principle-Guided Reasoning Process Reward Model for Web Agents
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Web navigation trajectory data with principle-guided reasoning annotations
- [Target Experience]: WebArbiter PRM weights (reasoning-first, principle-inducing WebPRM)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}
- [Utilization]: WebArbiter used for reward-guided trajectory search on WebArena-Lite (+6.4 points over best prior WebPRM)
- [Method]: ⟨SFT⟩, ⟨RL: PPO⟩
- [Mechanism]: 提出 reasoning-first WebPRM：将 reward modeling 形式化为 text generation（生成 structured justifications → preference verdict → 识别最有利于 task completion 的 action）。两阶段训练：(1) reasoning distillation：从 teacher 模型蒸馏 principle-guided reasoning 能力；(2) RL：通过直接对齐 verdicts 与 correctness 来纠正 teacher biases（注意此 RL 是对 PRM 自身的校准，非 policy 训练）。发布 WebPRMBench benchmark。若用于下游 policy RL 训练则构成 §8.2。

[Title]: From Correction to Mastery: Reinforced Distillation of Large Language Model Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Student-generated trajectories with teacher correction at earliest error
- [Target Experience]: Student policy weights via SFT + short-horizon RL
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: 7B student matches agentic performance of 72B teacher on 12 benchmarks
- [Method]: ⟨SFT⟩, ⟨RL: PPO⟩
- [Mechanism]: 提出 SCoRe (Student-Centered Correction and Reinforcement)：Student policy 首先生成 training trajectories → Teacher 仅在最早出错处进行 correction（而非模仿整个 teacher trajectory），生成匹配 student 能力的训练数据 → Student 在 corrected trajectories 上 SFT → Short-horizon RL 从 verified prefix 开始训练，target rewards 在出错 step 处。关键贡献在 teacher correction 策略（Narrative refinement）和 short-horizon RL，不同于标准 RLHF 的 RM 训练。

[Title]: Improve Mathematical Reasoning in Language Models by Automated Process Supervision
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: CoT reasoning traces with automated step-level annotations (1.5M+ process supervision annotations)
- [Target Experience]: Process Reward Model (PRM) weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: PRM enhances LLM math reasoning via weighted self-consistency at inference time
- [Method]: ⟨MCTS⟩, ⟨SFT⟩
- [Mechanism]: 提出 OmegaPRM：一种 divide-and-conquer 风格的 MCTS 算法，自动高效收集 process supervision data。通过 binary search 快速定位 CoT 中第一个错误，平衡正负样本。用收集到的 1.5M+ process supervision annotations 训练 PRM。配合 weighted self-consistency 算法提升推理性能。纯 P4：主要贡献在自动 process supervision data collection 方法，PRM 用于 inference-time verification。

[Title]: ZeroGUI: Automating Online GUI Learning at Zero Human Cost
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: Agent GUI interaction trajectories with VLM-based automatic reward estimation
- [Target Experience]: Improved GUI agent policy weights via online RL
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Policy achieves improved performance on OSWorld and AndroidLab
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: §8.1 self-reinforce 闭环用于 GUI agents。三组件：(1) VLM-based automatic task generation：从当前 environment state 自动生成多样化训练目标 (Policy → Narrative: P7)；(2) VLM-based automatic reward estimation：无需 hand-crafted evaluation functions 自动评估 task success；(3) Two-stage online RL：持续与环境交互学习。整体构成 Policy (exploration) → Narrative (trajectories + VLM rewards) → Policy (RL update) 闭环。

[Title]: SRR-Judge: Step-Level Rating and Refinement for Enhancing Search-Integrated Reasoning in Search Agents
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Step-level reasoning and search action assessments from SRR-Judge
- [Target Experience]: SRR-Judge evaluator weights (step-level assessment for search agents)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: SRR-annotated data used for iterative rejection sampling fine-tuning to enhance deep search capability (+10% pass@1)
- [Method]: ⟨SFT⟩
- [Mechanism]: 提出 SRR-Judge，一个针对 search-integrated reasoning 的 step-level 评估框架。集成到 ReAct-style rate-and-refine workflow 中，提供 fine-grained guidance。用 SRR-annotated data 通过 iterative rejection sampling fine-tuning 增强 base agent 的 deep search 能力。SRR-Judge 的评估比 DeepSeek-V3.1 等更大模型更可靠。路径核心是 Evaluator 构建 (P4)，但 SRR-annotated data 随后用于 policy fine-tuning (P5)，构成 §8.2 lite。

[Title]: ProgRM: Build Better GUI Agents with Progress Rewards
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: GUI agent trajectories with LCS-based progress labels
- [Target Experience]: Progress Reward Model (ProgRM) weights AND improved GUI agent policy via RL
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Policy outperforms proprietary LLMs and ORM-trained actors
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: Stage 1 (P4): 提出 Progress Reward Model (ProgRM)，通过预测每个 step 的 task completion progress 提供 dense intermediate rewards。设计基于 LCS (Longest Common Subsequence) 的 self-annotation 算法自动发现 trajectory 中的 key steps 并分配 progress labels。Stage 2 (P6): 用 ProgRM 作为 dense reward signal 进行 online RL 训练 GUI agent policy。解决 ORM 无法提供 fine-grained feedback 和过度惩罚失败 trajectory 中有价值 steps 的问题。

[Title]: TGPO: Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: Web agent trajectories represented as tree-structured graph
- [Target Experience]: Process Reward Model (PRM) weights AND improved web agent policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Policy achieves higher success rates with fewer redundant steps on web navigation tasks
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: Stage 1: 将 trajectories 表示为 tree-structured representation，合并语义相同的 states 以消除 label conflicts。Stage 2 (P4): 训练 PRM，通过 subgoal progress、redundancy detection、action verification 自动生成 fine-grained rewards。Stage 3 (P6): Dynamic weighting mechanism 优先高影响决策点，用 PRM signals 通过 offline RL (DPO-style preference optimization) 训练 policy。整体构成 §8.2 composite offline variant。

[Title]: Building Autonomous GUI Navigation via Agentic-Q Estimation and Step-Wise Policy Optimization
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: GUI state-action trajectories produced by policy itself
- [Target Experience]: Agentic-Q model weights (step-wise action value estimator) AND improved GUI policy weights
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Policy achieves remarkable GUI navigation and grounding performance, surpassing larger models
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: Stage 1 (P4): 训练 Agentic-Q model（Q-model）生成 step-wise values 评估每个 action 对 task completion 的贡献。所有 state-action trajectories 由 policy 自身产生。Stage 2 (P6): Step-wise policy optimization：从 state-action trajectory 提取 step-wise samples，用 Agentic-Q model 提供的 values 作为 reward signals 通过 RL 优化 policy。Policy update 与 environment 解耦，保证稳定优化。

[Title]: Robust Preference Optimization through Reward Model Distillation
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Explicit reward model trained on preference data (distilled into implicit reward)
- [Target Experience]: Policy weights via DPO with distilled reward signal
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Policy generates preferred responses robust to distribution shift in preference annotations
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: 分析 DPO 中的 reward overfitting 问题（implicit rewards 趋向无限大导致 degenerate policies）。提出将显式训练的 reward model (RM) 蒸馏到 DPO 的 implicit reward 中：训练 policy 使其 implicit reward (scaled log-likelihood ratio) 匹配显式 RM。进一步考虑 RM 不确定性：对一族 reward models 做优化（而非单个 RM），增加对 preference distribution shift 的鲁棒性。路径：显式 RM (V-Par) → Policy (π-Par) via distilled DPO (P6)，其中 RM 提供 reward 蒸馏信号。

[Title]: MagicGUI-RMS: A Multi-Agent Reward Model System for Self-Evolving GUI Agents via Automated Feedback Reflux
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: GUI agent trajectories evaluated by multi-agent reward model system
- [Target Experience]: Domain-Specific RM + General-Purpose RM weights AND improved GUI agent policy via feedback reflux
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Policy achieves gains in task accuracy and behavioral robustness
- [Method]: ⟨hybrid⟩
- [Mechanism]: Stage 1 (P4): 构建 MagicGUI-RMS (multi-agent reward model system)，集成 Domain-Specific RM (DS-RM) 和 General-Purpose RM (GP-RM) 实现 fine-grained action assessment。通过 structured data construction pipeline 自动生成 balanced/diverse reward datasets。Stage 2 (P6): RM system 识别错误 actions、提出 refined alternatives，通过 automated data-reflux mechanism 持续增强 agent behavior。Hybrid 由 ⟨SFT⟩ (RM training) + ⟨LLM-extract⟩ (feedback generation) 组成。Self-evolving 体现在 feedback → training data → policy improvement 循环。

[Title]: Motif: Intrinsic Motivation from Artificial Intelligence Feedback
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: LLM preferences over pairs of captions (game state descriptions)
- [Target Experience]: Intrinsic reward function AND RL-trained agent policy for NetHack
- [Source Modality]: [txt]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}
- [Utilization]: Policy achieves higher game score than algorithm directly trained to maximize score
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: Stage 1 (P4): 用 LLM 对 captions pairs（游戏状态的语言描述）给出偏好，构建 intrinsic reward function（不依赖环境 reward）。Stage 2 (P6): 用 LLM 产生的 intrinsic reward 训练 RL agent。关键发现：仅最大化 intrinsic reward 就能达到比直接优化 game score 更高的分数。Combined reward (intrinsic + environment) 显著优于现有方法。LLM 在此作为偏好提供者（teacher），不需要与环境交互。

[Title]: OpenClaw-RL: Train Any Agent Simply by Talking
- [Pathway]: Policy → Narrative → Policy (§8.1) + Narrative → Evaluator (P4)
- [Source Experience]: Agent interactions across diverse settings (personal conversations, terminal, GUI, SWE, tool-call)
- [Target Experience]: PRM judge AND continuously improved agent policy weights
- [Source Modality]: [cross-modal]
- [Target Modality]: [cross-modal]
- [Experience Source]: {self}, {human}
- [Utilization]: Policy improves simply by being used; personal agent learns from user re-queries, corrections, feedback
- [Method]: ⟨hybrid⟩
- [Mechanism]: 利用 next-state signals 作为通用学习源。两类信号：(1) Evaluative signals: 由 PRM judge 提取 scalar rewards (P4: Narrative → Evaluator)；(2) Directive signals: 通过 Hindsight-Guided On-Policy Distillation 提取 textual hints 构建 enhanced teacher context，提供 token-level directional advantage supervision（丰富度超越 scalar reward）。整体构成 §8.1 闭环：Policy 交互产生 Narrative (P7) → Narrative 被 PRM 评估 + 提取 directive signals → 回灌训练 Policy (P5)。Hybrid 由 ⟨LLM-extract⟩ (PRM judging + hint extraction) + ⟨SFT⟩ (distillation) + ⟨RL: PPO⟩ 组成。

[Title]: Vision-Language Models as a Source of Rewards
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Off-the-shelf VLM (CLIP family) as zero-shot reward models
- [Target Experience]: RL-trained agent policies for various visual goal tasks
- [Source Modality]: [vis+txt]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}
- [Utilization]: Policy achieves various language-specified visual goals
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 使用 off-the-shelf VLMs (CLIP family) 作为 reward source。VLM 基于 language goal description 对 visual observations 打分，为 RL agent 提供 reward 信号。展示 scaling trend：更大的 VLMs 产生更准确的 rewards → 训练出更 capable RL agents。纯 P6：frozen VLM as Evaluator (V-Par) → Policy (π-Par) via RL。

[Title]: OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: GUI agent trajectories decomposed into verifiable milestones
- [Target Experience]: OS-Themis multi-agent critic (Evaluator) for GUI outcome rewards
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Critic used for online RL training (+10.3% on AndroidWorld) and trajectory validation/filtering in self-training loop (+6.9%)
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 提出 OS-Themis，一个 scalable multi-agent critic framework。不同于单一 judge，OS-Themis 将 trajectories 分解为 verifiable milestones（isolate critical evidence），采用 review mechanism 严格审计 evidence chain 后再做 final verdict。发布 OmniGUIRewardBench (OGRBench) benchmark。主要贡献在 Evaluator 设计 (P4)，其输出被用于下游 RL training (P6) 和 self-training loop (§8.1)。

[Title]: Zero-Shot Reward Specification via Grounded Natural Language
- [Pathway]: Out of Scope
- [Mechanism]: 使用 CLIP 等 visuolanguage model 从 text description + raw pixel observations 生成 task reward signal 用于 RL 训练 policy。属于 zero-shot reward specification 方法，但经验源是 text description + visual observations 而非 agent 的 interaction trajectories/decision-making data。缺乏决策过程语义（无 $(c,a,o,f)$ 中的 action 序列和经验积累），不满足纳入标准中的"决策过程语义"条件。属于 §3.2 排除范围：静态视觉-语言对齐的信号源，非 agent experience transformation。

[Title]: VEM: Environment-Free Exploration for Training GUI Agent with Value Environment Model
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: Offline GUI interaction data with human-like priors about interaction outcomes
- [Target Experience]: Value Environment Model (VEM) weights AND improved GUI agent policy via VEM-guided RL
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {human}
- [Utilization]: Policy achieves state-of-the-art GUI automation on Android-in-the-Wild benchmarks
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: Stage 1 (P4): Pretrain Value Environment Model (VEM) 从 offline data 直接预测 state-action values（distilling human-like priors about GUI interaction outcomes），不需要 next-state prediction 或 environment feedback。VEM 侧重 semantic reasoning（"这个 action 是否推进了用户目标？"）。Stage 2 (P6): Frozen VEM 提供 value signals 引导 policy exploration 进行 RL（environment-free，避免 costly real interactions）。

[Title]: FuRL: Visual-Language Models as Fuzzy Rewards for Reinforcement Learning
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Fine-tuned VLM providing fuzzy reward signals
- [Target Experience]: RL-trained agent policies for Meta-World manipulation tasks
- [Source Modality]: [vis+txt]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}
- [Utilization]: Policy performs sparse reward manipulation tasks more effectively
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 识别 VLM 作为 reward model 时的 reward misalignment 问题。提出 FuRL：对 VLM representations 做 lightweight fine-tuning 实现 reward alignment，结合 relay RL 避免 local minima。VLM 在此作为 reward source，经过 fine-tuning 后提供 "fuzzy rewards" 用于 RL 训练 policy。Frozen/fine-tuned VLM (V-Par) → Policy (π-Par) via RL (P6)。

[Title]: No More Stale Feedback: Co-Evolving Critics for Open-World Agent Learning
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: Agent interaction trajectories with evolving natural-language critique feedback
- [Target Experience]: Co-evolved critic AND improved agent policy weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy achieves more stable training and higher long-horizon task success
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 提出 ECHO (Evolving Critic for Hindsight-Guided Optimization)：解决静态 critic 在 on-policy RL 中随 policy 演变而过时的问题。Cascaded rollout mechanism：critic 对初始 trajectory 生成多个 diagnoses → policy refinement 进行 group-structured advantage estimation。Saturation-aware gain shaping objective：奖励 critic 在高表现 trajectory 上诱导增量改进。Dual-track GRPO updates 使 critic feedback 与 evolving policy 同步。Critic 和 policy 形成 co-evolutionary loop。Critic (V-Par) 在此是 natural-language feedback generator（既有 evaluator 功能也提供 qualitative feedback）。

[Title]: RLAnything: Forge Environment, Policy, and Reward Model in Completely Dynamic RL System
- [Pathway]: Narrative → Evaluator → Policy (§8.2) + Policy → Narrative → Policy (§8.1)
- [Source Experience]: Agent interaction trajectories with step-wise and outcome signals
- [Target Experience]: Dynamically optimized reward model AND improved policy weights
- [Source Modality]: [cross-modal]
- [Target Modality]: [cross-modal]
- [Experience Source]: {self}
- [Utilization]: Policy improves on OSWorld (+9.1%), AlfWorld (+18.7%), LiveBench (+11.9%)
- [Method]: ⟨hybrid⟩
- [Mechanism]: 提出完全动态的 RL 系统，同时优化 Environment、Policy 和 Reward Model。核心机制：Policy 用 step-wise + outcome signals 的 integrated feedback 训练；Reward model 通过 consistency feedback 联合优化（反过来又改善 policy 训练）。Theory-motivated automatic environment adaptation 利用 critic feedback 改进 training。整体构成双重闭环：§8.2 (Narrative → Evaluator → Policy) + §8.1 (Policy → Narrative → Policy)。Hybrid 由 ⟨RL: PPO⟩ + ⟨RL: GRPO⟩ + ⟨LLM-extract⟩ 组成。

[Title]: Iterative Tool Usage Exploration for Multimodal Agents via Step-wise Preference Tuning
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: Self-discovered tool usage strategies from multimodal task exploration
- [Target Experience]: Improved multimodal agent policy via step-wise preference optimization
- [Source Modality]: [cross-modal]
- [Target Modality]: [cross-modal]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Policy achieves 6.41% improvement on GTA and 3.64% on GAIA benchmarks
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: 提出 SPORT：无需 pre-collected data 的 iterative tool usage exploration 方法。四组件循环：(1) Task synthesis: LLM 合成 multimodal tasks；(2) Step sampling: agent 尝试不同 tools；(3) Step verification: AI verifier 提供 preference feedback 构造 step-wise preference data；(4) Preference tuning: 用 preference data 通过 step-wise preference optimization 更新 controller。Policy → Narrative (interaction trajectories) → Policy (preference tuning) 闭环，无需 human annotations。

[Title]: VARP: Reinforcement Learning from Vision-Language Model Feedback with Agent Regularized Preferences
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: Robot manipulation trajectories with VLM preference labels (enhanced by trajectory sketches)
- [Target Experience]: Agent-regularized reward model AND improved RL policy for continuous-control robotics
- [Source Modality]: [vis+txt]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}, {self}
- [Utilization]: Policy achieves ~70-80% success rate on MetaWorld tasks (vs <50% for standard approaches)
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: Two-part solution for VLM-based reward learning in robotics。Stage 1 (P4): 改进 feedback accuracy——在 final observations 上叠加 trajectory sketches 以揭示 agent 的 motion path，让 VLM 提供更可靠的 preferences（+15-20% accuracy）。Stage 2 (P6): Agent-regularized reward learning——reward model 优化时 incorporate agent's performance，确保 reward model 基于当前 policy 的数据优化（+20-30% episode returns）。

[Title]: SWEET-RL: Training Multi-Turn LLM Agents on Collaborative Reasoning Tasks
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: Multi-turn collaborative interaction data with training-time information
- [Target Experience]: Critic model (step-level value estimator) AND improved policy model
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy achieves 6% absolute improvement in success and win rates; Llama-3.1-8B matches/exceeds GPT-4o
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 提出 ColBench benchmark（LLM agent 与 human collaborator 多轮交互）。Stage 1 (P4): 用精心设计的优化目标训练 critic model，该 critic 可访问额外 training-time information，提供 step-level rewards。Stage 2 (P6): Critic 的 step-level rewards 用于 policy model 的 RL 训练（multi-turn credit assignment）。解决现有 multi-turn RL 算法在多轮交互中 credit assignment 失效的问题。

[Title]: Teaching LLM to be Persuasive: Reward-Enhanced Policy Optimization for Alignment from Heterogeneous Rewards
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: Multi-turn negotiation dialogues with heterogeneous reward signals
- [Target Experience]: Policy weights optimized via composite reward signals (RM + LLM-judge + rule-based)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}, {teacher}
- [Utilization]: Policy achieves +12.14pp response rate and +5.94pp task success in production A/B test (9,653 conversations)
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 提出 REPO (Reward-Enhanced Policy Optimization)：组合 heterogeneous rewards 进行 RL post-training。(1) Preference-trained RM (V-Par) 提供偏好信号；(2) LLM-as-a-judge (RJ) 提供 nuanced behaviors 评估（emotional value, SOP compliance）；(3) Rule-based reward functions (RF) 提供 deterministic checks（numerics, formatting, guardrails）。三种 reward signals 聚合后通过 GRPO 优化 policy。RM 在此是预先训练的 evaluator，整体构成 §8.2。

[Title]: Aligning Large Language Models by On-Policy Self-Judgment
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: Policy's own pairwise judgments of on-the-fly generated responses
- [Target Experience]: Single model weights that serve as both policy and judge
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy generates preferred responses; rejection sampling further improves performance without additional evaluator
- [Method]: ⟨SFT⟩
- [Mechanism]: 提出 SELF-JUDGE：训练单一模型同时充当 policy 和 judge。通过 Judge-augmented Supervised Fine-Tuning (JSFT) 将 pairwise judgment task 视为 instruction-following task 的特例。因此，当前 policy 的 on-the-fly responses 可由其自身 judge（无需额外 RM）。本质是 §8.1 闭环：Policy 外化生成 responses + judgments (Policy → Narrative: P7) → 用 self-judgments 优化 policy (Narrative → Policy: P5)。参数高效（不需要额外 RM）。

[Title]: Video-Language Critic: Transferable Reward Functions for Language-Conditioned Robotics
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Cross-embodiment robot video data with language task descriptions (Open X-Embodiment)
- [Target Experience]: Video-Language Critic (reward model weights)
- [Source Modality]: [vis+txt]
- [Target Modality]: [embodied]
- [Experience Source]: {human}
- [Utilization]: Reward model enables 2× more sample-efficient policy training on Meta-World tasks
- [Method]: ⟨SFT⟩
- [Mechanism]: 分离 "what to accomplish" (从 external observation-only data 学习) 和 "how to accomplish" (依赖具体 robot embodiment)。提出 Video-Language Critic：用 contrastive learning + temporal ranking objective 在 cross-embodiment data (Open X-Embodiment) 上训练 reward model，可跨 robot 迁移。Reward model 用于为独立 actor 的行为轨迹评分。主要贡献在 Evaluator 构建 (P4)，下游 RL 使用时构成 §8.2。

[Title]: Enhancing Robotic Manipulation with AI Feedback from Multimodal Large Language Models
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Robot manipulation trajectory videos with MLLM analysis and preference feedback
- [Target Experience]: CriticGPT weights (multimodal LLM critic for robot manipulation)
- [Source Modality]: [vis+txt]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}
- [Utilization]: CriticGPT's reward model efficiently guides policy learning, surpassing state-of-the-art pre-trained representation models
- [Method]: ⟨SFT⟩
- [Mechanism]: 训练 CriticGPT (multimodal LLM)：能理解 robot manipulation 的 trajectory videos，作为 critic 提供 analysis 和 preference feedback。从 preference labels 的角度验证 CriticGPT 作为 reward model 的效果。主要贡献在训练一个能理解 robot video 的 Evaluator (P4)，其 preference labels 用于下游 policy learning（构成 §8.2）。

[Title]: DPO Learning with LLMs-Judge Signal for Computer Use Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Synthetic interaction trajectories filtered by LLM-as-Judge
- [Target Experience]: Lightweight vision-language model policy weights for local machine deployment
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}
- [Utilization]: Local policy outperforms baselines on OS-World benchmark
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: 提出 LLM-as-Judge framework：自动评估和过滤 synthetic interaction trajectories，生成高质量 preference data 而无需 human annotation。用过滤后的 preference data 通过 DPO（或 similar RL method）训练 lightweight vision-language model（policy）。LLM judge 在此作为 filter（不训练），路径为 LLM-judge-filtered trajectories (Narrative) → Policy via DPO (P5)。

[Title]: Policy Learning from Large Vision-Language Model Feedback Without Reward Modeling
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Visual trajectory segments with VLM preference labels
- [Target Experience]: Policy weights via supervised contrastive preference learning
- [Source Modality]: [vis+txt]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}
- [Utilization]: Policy performs robotic manipulation tasks on par with or surpassing VLM-based reward generation methods
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: 提出 PLARE：绕过显式 reward model 训练。Query VLM 对 visual trajectory segment pairs 给出 preference labels（基于 language task description）。直接用 supervised contrastive preference learning objective 从 preference labels 训练 policy，不学习显式 reward model。路径为 VLM preference labels on trajectories (Narrative) → Policy via contrastive learning (P5)，不经过独立的 Evaluator 参数。


[Title]: Expanding the Capabilities of Reinforcement Learning via Text Feedback
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Textual feedback (richer than scalar rewards, cheaper than demonstrations) on policy rollouts
- [Target Experience]: Policy weights internalizing feedback to improve single-turn performance
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}, {teacher}
- [Utilization]: Policy achieves improved single-turn performance on reasoning, math, and creative writing tasks
- [Method]: ⟨SFT⟩
- [Mechanism]: 提出 RL from Text Feedback (RLTF)：text feedback 作为 intermediate signal（比 binary reward 更丰富，比 demonstration 更便宜）。两种方法：(1) Self Distillation (RLTF-SD)：训练 single-turn policy 匹配其自身 feedback-conditioned second-turn generations；(2) Feedback Modeling (RLTF-FM)：预测 feedback 作为 auxiliary objective。两种方法都将 text feedback (Narrative) 内化为 policy 能力 (P5)。Text feedback 作为自然语言信号被 policy weight 吸收。

[Title]: The Lighthouse of Language: Enhancing LLM Agents via Critique-Guided Improvement
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: Detailed natural language critiques from a trained critic model
- [Target Experience]: Trained critic model weights AND improved actor policy weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Actor achieves state-of-the-art performance in interactive environments
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 提出 Critique-Guided Improvement (CGI)，two-player framework。Stage 1 (P4): 训练 critic model 生成 fine-grained assessments 和 actionable revisions（natural language feedback）。Stage 2 (P6): Actor model 利用这些 critiques 探索 alternative strategies。Critic 生成的自然语言反馈比 scalar rewards 更丰富、更具可操作性。小 critic model 的反馈质量甚至超越 GPT-4。Actor 和 Critic 构成对抗性协同训练：Critic 学习更好地评估 → Actor 学习更好地利用评估。

[Title]: Code as Reward: Empowering Reinforcement Learning with VLMs
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: VLM-generated dense reward functions (in code form)
- [Target Experience]: RL-trained agent policies for discrete and continuous control
- [Source Modality]: [vis+txt]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}
- [Utilization]: Policy achieves more effective training than with original sparse environment rewards
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 提出 VLM-CaR (Code as Reward)：让 VLM 通过 code generation 产生 dense reward functions（而非频繁 query VLM 获取 reward）。VLM 分析 image-based observations 并生成可执行代码形式的 reward function，显著降低 VLM inference 计算负担。生成的 dense rewards 比原始 sparse environment rewards 更有效。纯 P6：frozen VLM as Evaluator (V-Par) → 生成 code reward → Policy (π-Par) via RL。

[Title]: Training Agents with Weakly Supervised Feedback from Large Language Models
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: Agent self-generated interaction trajectories, with critic LLM selecting high-quality subsets
- [Target Experience]: Improved agent policy weights via iterative SFT on critic-selected self-generated trajectories
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Agent achieves comparable performance to GPT-4 using open-source models with fewer parameters
- [Method]: ⟨SFT⟩
- [Mechanism]: §8.1 self-reinforce 闭环。每轮迭代：Agent (Policy) 在环境中自主交互生成 trajectories (Policy → Narrative: P7) → 外部 Critic LLM 作为 weakly supervised selector 筛选 "good" trajectory 子集（提供 selection signal 但不生成新内容，不训练）→ 用 selected self-generated trajectories 通过 SFT 更新 Agent (Narrative → Policy: P5) → 更新后的 Agent 在下一轮生成 improved trajectories。核心创新在于用 Critic LLM 的 weakly supervised selection 替代 expert demonstrations 或 definitive environmental feedback，绕过传统 RL 对强监督信号的依赖。迭代闭环使 Agent 能力逐步提升。

[Title]: Affordance-Guided Reinforcement Learning via Visual Prompting
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: VLM-generated keypoint-based affordance rewards
- [Target Experience]: RL-trained robot manipulation policy
- [Source Modality]: [vis+txt]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}
- [Utilization]: Policy achieves successful task completion in 30K online fine-tuning steps
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 提出 KAGI (Keypoint-based Affordance Guidance for Improvements)：利用 state-of-the-art VLMs 的 zero-shot affordance reasoning（通过 keypoints），定义 dense rewards 引导自主 robotic learning。VLM 在此作为 zero-shot reward provider（frozen Evaluator, V-Par），其 keypoint-based affordance rewards 通过 RL 训练 policy (π-Par)。纯 P6 variant：VLM 的 affordance knowledge → Policy weights。

[Title]: Reinforcement Learning with Foundation Priors: Let Embodied Agent Efficiently Learn on Its Own
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Guidance from policy, value, and success-reward foundation models
- [Target Experience]: RL-trained robot manipulation policies
- [Source Modality]: [vis+txt]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}
- [Utilization]: Policy achieves 86% average success rate across 5 dexterous tasks after 1 hour real-time learning
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 提出 RLFP (Reinforcement Learning with Foundation Priors) 框架：利用 foundation models 的 policy prior、value prior 和 success-reward prior 来引导 agent exploration。FAC (Foundation-guided Actor-Critic) 算法使 embodied agents 能用自动 reward functions 高效探索。Foundation models 作为 frozen priors (V-Par evaluators + π-Par policy priors) 提供 guidance signals，下游 RL 训练具体的 robot policy。纯 P6 variant with additional policy-prior guidance。

[Title]: Teaching Language Models to Self-Improve by Learning from Language Feedback
- [Pathway]: Narrative → Narrative → Policy (§8.3)
- [Source Experience]: Self-generated responses with critiques and refinements from a more advanced model
- [Target Experience]: Policy weights via SFT on self-generated feedback and refinements
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Policy win rate increases from 9.6% to 25.8% on AlpacaEval 2.0 (70B model)
- [Method]: ⟨SFT⟩
- [Mechanism]: 提出 Self-Refinement Tuning (SRT)：Base model 生成 initial responses → 更 advanced model (GPT-4-Turbo) 提供 critiques 和 refinements → Base model 从 self-generated feedback 和 refinements 中学习。这是 §8.3 模式：Narrative (raw responses) → Narrative (refined: critiques + refinements, P1) → Policy via SFT (P5)。Feedback loop 持续促进 model improvement。

[Title]: SAIL: Self-Improving Efficient Online Alignment of Large Language Models
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: Online self-generated samples with iteratively refined preference labels
- [Target Experience]: Policy weights aligned via bilevel optimization reduced to single-level method
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy achieves improved alignment performance with minimal computational overhead
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: 将 online LLM alignment 形式化为 bilevel optimization，利用 reward-policy equivalence 将其简化为高效的 single-level first-order method。Policy 生成新 samples (P7: Policy → Narrative) → 用自身作为 implicit reward model 评估和调节 preference labels → 用 refined preference data 更新 policy (P5: Narrative → Policy)。在线和 self-improving 方式操作，统一了先前的 online RLHF 方法。§8.1 闭环的在线实现。

[Title]: Athena: Enhancing Multimodal Reasoning with Data-efficient Process Reward Models
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Multimodal reasoning traces with prediction consistency-based labels (only 5,000 samples)
- [Target Experience]: Athena-PRM weights (multimodal process reward model)
- [Source Modality]: [cross-modal]
- [Target Modality]: [cross-modal]
- [Experience Source]: {self}, {teacher}
- [Utilization]: PRM used for test-time scaling verification (+10.2 on WeMath, +7.1 on MathVista), reasoning step evaluation, and reward ranked fine-tuning
- [Method]: ⟨SFT⟩
- [Mechanism]: 提出 Athena-PRM (multimodal process reward model)。数据高效的关键：利用 weak 和 strong completers 之间的 prediction consistency 作为识别可靠 process labels 的标准（而非昂贵的 MCTS estimation）。仅用 5,000 samples 即可训练高性能 PRM。额外贡献：ORM initialization + up-sampling for negative data 策略。纯 P4：主要贡献在 multimodal PRM 构建。用于 reward ranked fine-tuning 时构成 P5。

[Title]: Taming the Judge: Deconflicting AI Feedback for Stable Reinforcement Learning
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: LLM judge preference judgments with logical inconsistencies (preference cycles)
- [Target Experience]: Deconflicted reward signal (DAG-based) AND improved policy via stable RL
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Policy trained with deconflicted signal achieves improved training stability and performance
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 针对 AI feedback 中 judgment inconsistencies（特别是 preference cycles）导致 RL 训练不稳定。Stage 1 (P4 refinement): 提出 Conflict Detection Rate (CDR) 量化 judgment conflicts；Deconflicted Graph Rewards (DGR) framework 将 raw preference judgments 构建为 preference graphs → 转化为无冲突 DAG → 生成 logically coherent reward signal。Stage 2 (P6): 用净化的 reward signal 训练 policy。核心贡献在 Evaluator 信号的净化和去冲突。

[Title]: Fine-Tuning Language Models with Reward Learning on Policy
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: Policy-generated samples used via unsupervised multi-view learning + synthetic preference data
- [Target Experience]: On-distribution refined reward model AND improved policy weights via PPO
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy achieves state-of-the-art alignment on benchmark datasets
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: §8.2 composite。Stage 1 (P4): 提出 RLP (Reward Learning on Policy)——用两种机制从 policy samples (Narrative) 训练/refine RM：(a) unsupervised multi-view learning 从 policy samples 学习 robust representations；(b) synthetic preference generation 用 policy outputs 模拟高质量 preference data。目标是保持 RM on-distribution（解决 policy 分布偏移导致的 RM 不准确）。Stage 2 (P6): Refined/on-distribution RM 通过 PPO 为 policy 提供更准确的 reward signal。与传统 RLHF 不同，RM 不是固定的——它随 policy 演化而持续更新。

[Title]: RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: All self-generated samples (both positive and negative trajectories) with scalar rewards
- [Target Experience]: Policy weights via reward-weighted fine-tuning
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy achieves better mathematical reasoning performance than Rejection Sampling Fine-Tuning
- [Method]: ⟨SFT⟩
- [Mechanism]: 提出 RIFT (Reward Informed Fine-Tuning)：不丢弃 negative trajectories（不同于 standard RFT），而是利用所有 self-generated samples。用 scalar rewards 对 loss 做 reweighting，从 positive 和 negative trajectories 中学习。引入 stabilized loss formulation 解决 naive reward integration 导致的 training collapse（unbounded loss）。路径：reward-weighted trajectories (Narrative) → Policy via weighted SFT (P5)。Reward model 作为打分器（不训练）。

[Title]: Off-Policy Corrected Reward Modeling for Reinforcement Learning from Human Feedback
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: Human preference data + off-policy correction via importance weighting
- [Target Experience]: Corrected reward model (more accurate under distribution shift) AND improved final policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Policy performs significantly better than standard RLHF on summarization and chatbot tasks
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 分析 RLHF 中的 overoptimization 问题：从 distribution shift 角度揭示 RM parameter 估计不一致导致 policy gradient 估计不一致。提出 OCRM (Off-Policy Corrected Reward Modeling)：用 importance weighting 迭代 off-policy correct RM，不需要新 labels 或 samples。Stage 1 (P4 refinement): 校正 RM 使其在 policy 分布偏移下保持准确。Stage 2 (P6): 更准确的 RM → 更好的 policy via RL。

[Title]: WARM: On the Benefits of Weight Averaged Reward Models
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Human preference data used to train multiple reward models
- [Target Experience]: Weight-averaged ensemble RM (improved efficiency and robustness)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: RM used for RL fine-tuning; policy trained with WARM achieves 79.4% win rate vs single RM policy
- [Method]: ⟨SFT⟩
- [Mechanism]: 提出 WARM (Weight Averaged Reward Models)：fine-tune 多个 RMs（同预训练基座），在 weight space 中做平均（而非传统 prediction ensembling）。利用 fine-tuned weights 在共享预训练下保持 linear mode connectivity 的特性。Weight averaging 比 prediction ensembling 更高效，在 distribution shift 下更可靠，对 preference inconsistencies 更 robust。纯 P4：改进 Evaluator 构建方法。用于 RL 训练时构成 P6。

[Title]: Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Human preference data used to train reward model ensembles
- [Target Experience]: Ensemble of reward models for more robust reward estimation
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: RM ensembles used for alignment at training time (RL) and inference time (reranking); mitigate but don't eliminate reward hacking
- [Method]: ⟨SFT⟩
- [Mechanism]: 分析 reward model ensembles 对 reward hacking 的缓解作用。发现 reward models 是 underspecified（in-distribution 表现相似的 RMs 在 alignment 中产生非常不同的 rewards）。Underspecification 导致 overoptimization。RM ensembles 缓解 overoptimization，pretraining seed 变化的 ensembles 比 fine-tuning seed 变化的 ensembles 泛化更好。但即使 pretrain ensembles 也不能完全消除 reward hacking（因为所有 RMs 共享相似 error patterns）。纯 P4：Evaluator 设计分析，用于下游 RL 时构成 P6。

[Title]: Improving Multimodal Interactive Agents with Reinforcement Learning from Human Feedback
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: Human interaction data with annotated progress/regress moments in simulated 3D environment
- [Target Experience]: Inter-temporal Bradley-Terry (IBT) reward model AND RL-improved embodied agent policy
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {human}
- [Utilization]: Policy improves on all metrics including subsequent human judgment during live interactions
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: Stage 1 (P4): 收集人类与 simulated embodied agents 交互数据，标注人类判断 agent "progressed toward" 或 "regressed from" goal 的时刻。用 Inter-temporal Bradley-Terry (IBT) modelling 构建 reward model 捕捉人类时间性判断。Stage 2 (P6): Agents 用 IBT reward models 的 rewards 进行 RL 训练。在复杂 embodied domain 中无需 programmatic reward functions。

[Title]: The Perfect Blend: Redefining RLHF with Mixture of Judges
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: Multiple evaluation signals from diverse judges (human preference data proxy)
- [Target Experience]: Constrained Generative Policy Optimization (CGPO) with Mixture of Judges (MoJ) AND improved policy weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}, {teacher}
- [Utilization]: Policy achieves +7.4% AlpacaEval-2 (general chat), +12.5% Arena-Hard (STEM), and consistent gains in math/coding
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 提出 Constrained Generative Policy Optimization (CGPO)。核心是 Mixture of Judges (MoJ)：多个 judge 提供多维度评估 → cost-efficient constrained policy optimization with stratification → 在极大数量目标间找到 pareto-optimal 点。同时检测和缓解 reward hacking。Stage 1 (P4): MoJ 构建多维 Evaluator 系统。Stage 2 (P6): Constrained optimization 将 MoJ 信号转化为 policy weights。解决 multi-task learning 中的 reward hacking 和 extreme multi-objective optimization 挑战。

[Title]: Confronting Reward Model Overoptimization with Constrained RLHF
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Composite reward models (multiple component RMs) with overoptimization thresholds
- [Target Experience]: Policy weights optimized within each RM's useful range via constrained RL
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Policy stays within each RM's effective proxy range, improving evaluation performance
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 首次研究 composite RMs 中的 overoptimization：component RMs 之间的 correlation 显著影响 overoptimization 临界点位置。提出 constrained RLHF：用 constrained RL 防止 agent 超出每个 RM's threshold of usefulness。通过 Lagrange multipliers 学习动态 weights（自然表达各 RM 的权重），gradient-free optimization 在单次 run 中识别和优化 overoptimization 临界点。纯 P6：固定 composite RMs (V-Par) → Policy (π-Par) via constrained RL。

[Title]: Stepwise Guided Policy Optimization: Coloring Your Incorrect Reasoning in GRPO
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: All-negative-sample groups in GRPO (incorrect reasoning trajectories)
- [Target Experience]: Step-wise judge model AND improved policy via diversified GRPO
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy improves performance across 9 reasoning benchmarks (7B, 14B, 32B models)
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 解决 GRPO 中的 all-negative-sample 问题（group 内所有 responses 都错误时 GRPO 无法更新 policy）。Stage 1 (P4): 训练 step-wise judge model（可 adapt from existing LLMs）在 all-negative groups 中通过 response diversity 提供有意义的区分信号。Stage 2 (P6): Judge model 的 step-wise 区分信号使 GRPO 在 all-negative groups 中也能学习。理论上证明这种 diversification 加速 GRPO learning dynamics。Judge 不需要生成正确解（区别于 knowledge distillation）。

[Title]: Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Reward model or verifiable reward with gradient-based regularization
- [Target Experience]: Policy weights optimized in flatter regions where reward is more accurate
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}, {teacher}
- [Utilization]: Policy achieves higher GPT-judged win-rate in RLHF and avoids format hacking in rule-based math rewards
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 提出新的 reward hacking 解决框架：将 policy updates 偏向 reward 更准确的区域（而非仅用 KL penalty 限制 policy update）。理论推导：reward model accuracy 与 convergence 时 optimum 的 flatness 存在关联。Gradient Regularization (GR) 将训练偏向 flatter regions → 维持 reward model accuracy。证明 Reference Resets（KL penalty 的常见做法）隐式使用了 GR。Explicit GR 在多个 RL 实验上优于 KL penalty。纯 P6：关注于如何从 (可能不准确的) Evaluator 信号更安全地转化到 Policy。

[Title]: LongReward: Improving Long-context Large Language Models with AI Feedback
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Off-the-shelf LLM providing multi-dimensional rewards for long-context responses
- [Target Experience]: Policy weights via DPO with long-context reward signals
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Policy achieves improved long-context performance and enhanced short instruction following
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: 提出 LongReward：利用 off-the-shelf LLM 为 long-context model responses 从四个维度提供 rewards（helpfulness, logicality, faithfulness, completeness），每个维度有精心设计的评估 pipeline。Combined reward 信号通过 offline RL algorithm DPO 训练 policy。LLM reward provider 是 frozen tool（不训练），路径为 LLM-scored long-context responses (Narrative) → Policy via DPO (P5)。

[Title]: Pretrain Value, Not Reward: Decoupled Value Policy Optimization
- [Pathway]: Narrative → Evaluator (P4) [with novel framing]
- [Source Experience]: Human preference data (same as used for reward modeling)
- [Target Experience]: Global Value Model (GVM) weights — a pretrained value function for policy optimization
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Frozen GVM serves as universal critic for policy learning; policy matches or surpasses SOTA RLHF
- [Method]: ⟨SFT⟩
- [Mechanism]: 提出 DVPO (Decoupled Value Policy Optimization)：直接 pretrain value model (Global Value Model, GVM) 而非先 train reward model 再 derive value model。关键 insight：从 preference data 训练 reward model 再 online 学习 value function 在信息论上是冗余的（与直接 pretrain value model 信息等价）。GVM 提供 stable, fine-grained credit assignment，无需 critic drift 或 trajectory sampling。纯 P4：Evaluator (作为 value model) 的新构建方式。下游 policy optimization 时 GVM 为 frozen critic，构成 P6。

[Title]: ODIN: Disentangled Reward Mitigates Hacking in RLHF
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Human preference data with length bias issues
- [Target Experience]: Disentangled reward model (length-decorrelated head for actual content)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: RM used for RL; almost eliminates reward correlation with length and improves policy quality
- [Method]: ⟨SFT⟩
- [Mechanism]: 针对 RLHF 中 reward hacking on response length 的问题。提出 disentangled RM：在 shared feature representations 上联合训练两个 linear heads——一个与 length 相关，另一个与 length 解相关（聚焦实际内容质量）。RL 时丢弃 length head 只用 content head，防止 reward hacking on length。纯 P4：改进 Evaluator 构建以抵抗特定类型的 reward hacking。用于下游 RL 时构成 P6。

[Title]: Reinforcement Learning from LLM Feedback to Counteract Goal Misgeneralization
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: LLM-analyzed RL agent policies and identified failure scenarios
- [Target Experience]: LLM-informed reward model AND further-trained RL agent policy
- [Source Modality]: [txt]
- [Target Modality]: [embodied]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Policy shows marked improvements in goal generalization in maze navigation tasks
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: Stage 1 (P4): LLM 分析 RL agent 的 policies 并识别潜在 failure scenarios → RL agent 在这些 scenarios 中部署 → 从 LLM preferences 和 feedback 学习 reward model (LLM-informed RM)。Stage 2 (P6): 用此 RM 进一步训练 RL agent。有趣的是：LLM 缺乏 task proficiency（不能自己做任务）但仍能有效监督 RL agent，提供 scalable oversight。

[Title]: Scaling Laws for Reward Model Overoptimization
- [Pathway]: Out of Scope
- [Mechanism]: 分析 reward model overoptimization 的 scaling laws（Goodhart's law 在 RLHF 中的表现）。使用 synthetic setup（gold-standard RM 模拟 human labels，proxy RM 训练后进行 RL/BoN optimization），测量 gold RM score 随 proxy RM optimization 的变化。研究发现 overoptimization 遵循不同函数形式（取决于 optimization method），系数与 RM parameter count 平滑缩放。属于 empirical analysis / measurement paper，描述的是 alignment 中的现象和规律，而非提出新的 experience transformation 方法。属于 §3.2：不满足纳入标准——缺乏新的 transformation 机制，是对已有 RM→Policy 转化中 overoptimization 现象的测量研究。

[Title]: Reinforcement Learning from Meta-Evaluation: Aligning Language Models Without Ground-Truth Labels
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Evaluator's answers to natural-language meta-questions about generation quality
- [Target Experience]: Policy weights via group-relative policy optimization on meta-evaluation rewards
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Policy achieves accuracy and sample efficiency comparable to label-based training; generalizes to open-domain settings
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 提出 RLME (Reinforcement Learning from Meta-Evaluation)：不依赖 ground-truth labels 或 task-specific verifiers。用 evaluator 回答 natural-language meta-questions（如 "Is the answer correct?"）的概率作为 reward。通过 group-relative policy optimization 更新 generator。Evaluator 在此作为 frozen judge (V-Par)，其 meta-evaluation 概率转化为 Narrative reward signal → Policy (π-Par) via GRPO (P5/P6 boundary)。若 evaluator 是 LLM-as-a-Judge (不训练)，路径偏向 P5；若 evaluator 是 trained RM，偏向 P6。

[Title]: LLaVA-Critic-R1: Your Critic Model is Secretly a Strong Policy Model
- [Pathway]: Narrative → Policy (P5) + Narrative → Evaluator (P4) [Multi-target §8.8]
- [Source Experience]: Preference-labeled critic datasets reorganized into verifiable training signals
- [Target Experience]: Unified model weights that excel at BOTH evaluation (critic) and generation (policy)
- [Source Modality]: [cross-modal]
- [Target Modality]: [cross-modal]
- [Experience Source]: {teacher}
- [Utilization]: Model serves as both top-performing critic and competitive policy; self-critique at test time yields +13.8% improvement
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 挑战 critic/policy 分离的传统。将 preference-labeled critic datasets 重组为 verifiable training signals，直接在 base generative model 上做 RL。结果：同一模型既是 top-performing critic (P4: Narrative → Evaluator) 又是 competitive policy model (P5: Narrative → Policy)。Multi-target (§8.8)：单一 RL 训练过程同时产出 Evaluator 和 Policy 能力。Self-critique at test time (evaluator 能力反馈给 policy 推理) 带来额外提升。

[Title]: Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms
- [Pathway]: Out of Scope
- [Mechanism]: 研究 Direct Alignment Algorithms (DAAs, 如 DPO) 中的 reward overoptimization 现象。尽管 DAAs 不使用单独 proxy reward model，在更高 KL budgets 下仍表现出与 classic RLHF 类似的退化模式。发现 DAA 方法不仅在宽 KL budget 范围内退化，而且常在完成 single dataset epoch 前就开始退化。这是 empirical analysis / measurement paper：描述 DAAs 中的 overoptimization scaling laws，不提出 new transformation mechanism。属于已有 P5 路径中的现象研究，非新 transformation 方法。

[Title]: Statistical Rejection Sampling Improves Preference Optimization
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Preference pairs sourced from target optimal policy via rejection sampling
- [Target Experience]: Policy weights via improved DPO/SLiC loss with rejection-sampled preference data
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy outperforms both SLiC and DPO on LLM and human evaluation
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: 提出 RSO (Statistical Rejection Sampling Optimization)：解决 DPO/SLiC 中 preference data 来源不匹配 target optimal policy 的问题。通过 rejection sampling 从 target optimal policy 获取 preference data（而非 SFT policy）。Unified framework 从 preference modeling 角度增强 SLiC 和 DPO 的 loss functions。路径：rejection-sampled preference data (Narrative, 来自更接近 optimal policy 的分布) → Policy via DPO/SLiC (P5)。

[Title]: PRAISE: Prefix-Based Rollout Reuse in Agentic Search Training
- [Pathway]: Narrative → Policy (P5) + Policy → Narrative → Policy (§8.1 element)
- [Source Experience]: Complete search trajectories with prefix states and intermediate answers
- [Target Experience]: Policy weights via RL with step-level rewards from prefix-based performance differences
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy consistently improves over strong baselines on multi-hop QA benchmarks
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 提出 PRAISE：解决 agentic search training 中昂贵 long-horizon rollouts 未被充分利用和 reward sparsity 的问题。从完整 search trajectory 提取不同 search turns 的 prefix states → 从 prefix states 引出 intermediate answers → 用这些 prefixes 构造额外 training trajectories (data efficiency) 和从 performance differences across prefixes 推导 step-level rewards (credit assignment)。单一模型同时用于 search policy learning 和 prefix answer evaluation（无额外 RM 或 human annotation）。Policy 外化 trajectories (P7) 并从中提取训练信号 (P5)，形成 self-improvement loop。

[Title]: Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Best-of-N inference-time selection outcomes used as training signal
- [Target Experience]: Policy weights optimized for BoN inference-time performance
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Bo32 performance improves on MATH (26.8%→30.8%) and HumanEval pass@16 (61.6%→67.1%)
- [Method]: ⟨SFT⟩, ⟨RL: PPO⟩
- [Mechanism]: 提出 inference-aware fine-tuning：直接在训练时优化 inference-time strategy 的性能。针对 Best-of-N (BoN) inference strategy（verifier 从 N 个 LLM-generated responses 中选择最佳），设计 imitation learning 和 RL 方法克服 BoN 中 non-differentiable argmax 的挑战。BoN-aware models 隐式学习 meta-strategy：交替生成 best responses 和 more diverse responses（类似 exploration-exploitation trade-off）。路径：BoN-selected outputs (Narrative) → Policy (P5)。

[Title]: Examining Reasoning LLMs-as-Judges in Non-Verifiable LLM Post-Training
- [Pathway]: Out of Scope
- [Mechanism]: 系统性研究 reasoning vs non-reasoning judges 在 RL-based LLM alignment 中的影响。Controlled synthetic setting（gold-standard judge 标注 preferences → 训练 smaller judges）揭示：non-reasoning judges 易导致 reward hacking，reasoning judges 训练的 policies 能学会生成 highly effective adversarial outputs（可欺骗其他 LLM-judges）。这是 evaluation/analysis paper，研究 judge 类型对训练的影响，但不提出新的 experience transformation 机制。属于已有 P5/P6 路径中的 judge 行为分析。

[Title]: SERL: Self-Examining Reinforcement Learning on Open-Domain
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: Self-generated responses with Copeland-style pairwise comparison judgments and self-consistency rewards
- [Target Experience]: Policy weights improved in both Actor and Judge capabilities
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Qwen3-8B LC win rate on AlpacaEval 2.0 from 52.37% to 59.90% (SOTA among self-improving approaches)
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: §8.1 self-reinforce 闭环。SERL 中 LLM 同时作为 Actor 和 Judge。两种 synergistic reward mechanisms（无 external signals）：(1) Copeland-style pairwise comparison judgments across a group 为 Actor 提供 reward；(2) Self-consistency reward 鼓励 coherent judgments 来 refine Judge。Judge 的 refinement 又增强 Actor 的训练信号。形成 self-reinforcing loop：better Judge → better Actor → better Judge。

[Title]: RS-DPO: A Hybrid Rejection Sampling and Direct Preference Optimization Method for Alignment of Large Language Models
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Diverse k responses per prompt sampled from SFT policy, with reward-based contrastive pairs
- [Target Experience]: Policy weights via DPO on rejection-sampled contrastive pairs
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy achieves improved alignment with user intent, outperforming RS, PPO, and DPO
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: 系统组合 Rejection Sampling (RS) 和 DPO。从 SFT policy 为每个 prompt 采样 k 个 diverse responses → 基于 reward distribution 识别 contrastive sample pairs → 用 DPO 优化 policy。关键区别：contrastive pairs 来自 policy model 自身而非 human annotator 或 alternative LLM。Reward model 在此仅作为 pair selection 的 scoring tool（不训练）。路径：reward-selected contrastive pairs (Narrative) → Policy via DPO (P5)。

[Title]: Direct Nash Optimization: Teaching Language Models to Self-Improve with General Preferences
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: Self-generated on-policy samples with preference feedback from oracle
- [Target Experience]: Policy weights via batched on-policy regression-based Nash equilibrium optimization
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Orca-2.5-7B achieves 33% win-rate against GPT-4-Turbo on AlpacaEval 2.0 (26% absolute gain)
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: 提出 Direct Nash Optimization (DNO)：超越 point-wise reward maximization (Bradley-Terry)，直接优化 general (pair-wise) preferences。Batched on-policy algorithm：每轮从当前 policy 采样 → oracle 提供 preference feedback (Narrative) → regression-based objective 更新 policy 朝向 Nash equilibrium。理论保证 monotonic improvement across iterations。即使从强 teacher (GPT-4) 出发也能持续改进。§8.1 闭环 on-policy 变体：Policy → samples (P7) → oracle preferences (Narrative) → Policy update (P5)。

[Title]: Aligning Language Models Using Follow-up Likelihood as Reward Signal
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Follow-up utterance likelihoods from conversational data as implicit reward signals
- [Target Experience]: Policy weights via DPO on automatically mined preference data
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {human}
- [Utilization]: Policy achieves stronger helpfulness; FLR reward matches strong RMs trained on large-scale human/GPT-4 data
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: 提出 FLR (Follow-up Likelihood as Reward)：受人类对话中 follow-up reactions 作为 feedback 的启发，用 follow-up utterance 的 likelihood 作为 reward 区分 preferred vs less favored responses。FLR 匹配大规模 human/GPT-4 标注训练的 strong RMs。进一步从 online policy generations 自动挖掘 preference data，用 DAP 方法 (DPO) 提升 helpfulness。路径：FLR-scored conversation data (Narrative) → Policy via DPO (P5)。

[Title]: DRLC: Reinforcement Learning with Dense Rewards from LLM Critic
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Token/span-level dense rewards from LLM critic on policy outputs
- [Target Experience]: Policy weights via PPO with dense critic rewards
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Policy achieves consistent performance gains over PPO baseline with holistic rewards
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 提出 DRLC (Dense Rewards from LLM Critic)：LLM critic 被 prompted（task description + question + policy output + environment reward signal），输出 token/span-level dense rewards 反映每个 output segment 的质量。这些 artificial dense rewards 融入 PPO 训练 policy。解决了传统 RLHF 中 sparse reward（整个 generation 只有一个 reward）导致的低效和不稳定。Self-critique variant：同一模型同时作为 policy 和 critic 时也能提升学习效率。路径：LLM critic output (Narrative dense rewards) → Policy via PPO (P5)。

[Title]: Arena Learning: Build Data Flywheel for LLMs Post-training via Simulated Chatbot Arena
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: AI-driven simulated arena battles evaluating model outputs
- [Target Experience]: Continuously improved policy via iterative SFT and RL on battle-informed training data
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: WizardLM-β achieves significant performance enhancements across various metrics
- [Method]: ⟨SFT⟩, ⟨RL: DPO⟩
- [Mechanism]: 提出 Arena Learning：用 AI-driven annotations 模拟 Chatbot Arena battles（离线）。两核心组件：(1) WizardArena pipeline：精确预测 Elo rankings（离线模拟与在线竞赛一致性高）；(2) Data flywheel：根据 battle results 识别 target model 弱点 → 从多种不同模型的优势中迭代更新 training data → SFT + RL 训练。Policy 外化 responses 参与 simulated battles (P7) → battle results 转化为 training data (Narrative) → 回灌训练 (P5)。§8.1 闭环利用多个模型的集体优势。

[Title]: Enhancing LLM-based Search Agents via Contribution Weighted Group Relative Policy Optimization
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Per-round contribution scores from LLM judge on retrieval utility and reasoning correctness
- [Target Experience]: Policy weights via CW-GRPO (Contribution-Weighted GRPO)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Policy outperforms standard GRPO by 5.0% (Qwen3-8B) and 6.3% (Qwen3-1.7B) on knowledge-intensive benchmarks
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 提出 CW-GRPO：将 process supervision 集成到 GRPO 中。LLM judge 评估每轮 search 的 retrieval utility 和 reasoning correctness，生成 per-round contribution scores。这些 scores 用于 rescale outcome-based advantages along trajectory（而非直接优化 process rewards），实现 fine-grained credit assignment 同时保持 optimization stability。路径：LLM judge contribution scores on trajectories (Narrative) → Policy via weighted GRPO (P5)。LLM judge 在此是 scoring tool（不训练）。

[Title]: Co-Evolution of Policy and Internal Reward for Language Agents
- [Pathway]: Policy → Narrative → Policy (§8.1) + Policy → Evaluator (P4) [Dual-use internal reward]
- [Source Experience]: Agent interaction trajectories with self-generated internal reward signals
- [Target Experience]: Internal reward (Self-Guide) AND improved policy weights via GRPO
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy achieves 8% improvement over baselines trained solely with environment reward
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 提出 Self-Guide：一种 self-generated internal reward 双重用途。Inference-time：作为 short self-guidance signal 引导下一步 action。Training-time：转化为 step-level internal reward 用于 denser policy optimization。形成 co-evolving loop：better policy → better self-guidance → better internal reward → better policy。Policy 同时扮演 (1) Actor 生成 trajectories (P7: Policy → Narrative) 和 (2) Internal Reward provider (P4: Narrative → Evaluator 但 evaluator 是自然语言 self-guidance 形式)。Co-evolution 使用 GRPO。

[Title]: Dense Reward for Free in Reinforcement Learning from Human Feedback
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Reward model's attention map over tokens (inherent in RM architecture)
- [Target Experience]: Policy weights via density-enhanced PPO with redistributed reward signal
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Policy training stabilizes, accelerates learning, and may lead to better local optima
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 利用 reward model (RM) 的 attention map（transformer 架构的副产品）将 sparse episode-level reward 重新分配到 completion 中的每个 token。这在理论上等价于 potential-based reward shaping（保证最优 policy 不变），无需额外计算成本。解决了 auto-regressive generation 中 "多步 action (token selection) 仅获得单次 sparse reward" 的 RL 困难。纯 P6：利用 RM (V-Par) 内部结构提升 reward signal 质量 → Policy (π-Par) via PPO。

[Title]: Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Reasoning trajectories with outcome labels (correct/incorrect)
- [Target Experience]: Conditional Reward Model (CRM) weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: CRM used for Best-of-N sampling, beam search, and RL; more robust to reward hacking
- [Method]: ⟨SFT⟩
- [Mechanism]: 提出 Conditional Reward Modeling (CRM)：将 LLM reasoning 视为 temporal process leading to correct answer。每个 reasoning step 的 reward 不仅条件于 preceding steps，还显式 linked to final outcome。通过 enforcing conditional probability rules，捕捉 reasoning steps 间的 causal relationships。解决现有 PRM 的两个缺陷：孤立处理每个 step（忽略 inter-step dependencies）和 process rewards 与 final outcome 对齐不一致。纯 P4：改进 Evaluator (PRM) 的建模方式。用于下游 RL 时构成 §8.2。

[Title]: SPARK: Stepwise Process-Aware Rewards for Reference-Free Reinforcement Learning
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: Generator-produced diverse solutions with verifier evaluations (self-consistency + meta-critique)
- [Target Experience]: Generative PRM weights AND RL-trained policy weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy achieves 47.4% average accuracy across 6 math reasoning benchmarks (outperforms ground-truth-based RLVR 43.9%)
- [Method]: ⟨SFT⟩, ⟨RL: PPO⟩
- [Mechanism]: Three-stage framework。Stage 1: Generator 产生 diverse solutions → Verifier 通过 parallel scaling (self-consistency) 和 sequential scaling (meta-critique) 评估 outputs。Stage 2 (P4): 将 verification outputs 作为 synthetic training data fine-tune generative PRM（PRM 以 chain-of-thought verification 形式生成 process rewards）。Stage 3 (P6): 用 generative PRM (PRM-CoT) 作为 reward model 进行 RL，引入 format constraints 防止 reward hacking。实现 reference-free RL training 超越 ground-truth methods。

[Title]: Free Process Rewards without Process Labels
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Response-level (outcome) labels only (cheaper than step-level labels)
- [Target Experience]: Implicit PRM (derived from ORM parameterization)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {human}
- [Utilization]: Implicit PRM used for evaluating reasoning steps and improving generation models
- [Method]: ⟨SFT⟩
- [Mechanism]: 理论加实证证明：仅通过 cheaper response-level labels 训练 ORM 即可获得 implicit PRM（无额外成本）。核心假设是将 outcome reward 参数化为 policy 和 reference model 的 log-likelihood ratios（与具体 loss 选择无关）。Implicit PRM 在使用不到 1/38 训练数据的情况下超越 MCTS-based Math-Shepherd baseline。纯 P4：提出一种更经济高效的 PRM 构建方法（从 outcome labels 隐式获取 process rewards）。训练 extra step labels 不会带来额外改进。

[Title]: RLVF: Learning from Verbal Feedback without Overgeneralization
- [Pathway]: Narrative → Narrative → Policy (§8.3)
- [Source Experience]: High-level verbal feedback (e.g., "Don't use emojis when drafting emails to my boss")
- [Target Experience]: Policy weights fine-tuned to apply feedback in relevant contexts without overgeneralization
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}, {teacher}
- [Utilization]: Policy adheres to verbal feedback comparably to in-context baselines while reducing overgeneralization by 30%
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: 提出 C3PO (Contextualized Critiques with Constrained Preference Optimization)。Stage 1 (P1): 从一段 high-level verbal feedback 生成小型 synthetic preference dataset，明确反馈在哪些 contexts 中应当（和不应当）被应用（raw feedback → refined preference data）。Stage 2 (P5): 在 synthetic preference data 上 fine-tune model（DPO-style），同时最小化与原始模型在 feedback 不适用 prompts 上的 divergence。§8.3 模式：Narrative (raw verbal feedback) → Narrative (refined, context-specific preference data) → Policy。


[Title]: On Designing Effective RL Reward at Training Time for LLM Reasoning
- [Pathway]: Narrative → Evaluator (P4) + Evaluator → Policy (P6) [reward refinement study]
- [Source Experience]: Reasoning trajectories with learned reward model scores (ORM/PRM) + success rewards
- [Target Experience]: More effective reward function design (Clipping/Delta techniques) AND improved policy via RL
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy improves on MATH and GSM8K; RL training without additional SFT improves all evaluated LLMs
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 评估 popular reward models (ORM, PRM) 在 RL training time 的效果。关键发现：inference-time 表现强的 RM 在 RL training 时可能反而有害或无效（因为 LLM 可通过重复正确但不必要的推理步骤获得高 reward——reward hacking）。提出两种 reward refinement 技术：Clipping（截断累积 reward 上界）和 Delta（reward 变化量限制）。改进后 RL training（仅用 success reward + refined learned reward）在无需额外 SFT 的情况下提升所有评估 LLMs。

[Title]: Policy Filtration for RLHF to Mitigate Noise in Reward Models
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Reward model scores with varying reliability across different reward levels
- [Target Experience]: Policy weights via PF-PPO (Policy Filtration for PPO) with filtered reward signals
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Policy achieves SOTA 7B performance on HumanEval (+7.9%), MBPP (+0.7%), and math reasoning
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 发现 reward model 的可靠性在不同 reward level 的 responses 之间差异很大。提出 PF-PPO (Policy Filtration for PPO)：使用 coefficient of determination (R²) between rewards 和 actual scores 在 filtered samples 上作为 metric，寻找有效的 policy filtering strategy 来过滤 reward 可能不可靠的样本，提升 policy learning 的 signal-to-noise ratio。纯 P6：改进从 Evaluator (V-Par) 信号到 Policy (π-Par) 的转化质量。

[Title]: The Trickle-down Impact of Reward (In-)consistency on RLHF
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Human preference data with analysis of reward model consistency
- [Target Experience]: More consistent reward model (via ConvexDA/RewardFusion techniques)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: More consistent RM yields more useful downstream RLHF policy responses
- [Method]: ⟨SFT⟩
- [Mechanism]: 研究 reward model (in-)consistency：RM 是否能识别不同 prompts 的语义变化并相应调整 reward。提出 Contrast Instructions benchmark 测量 RM consistency。发现当前 standard ranking objective 训练的 RMs 在 consistency 上远不及人类。提出 ConvexDA（训练时增强 consistency 的 extrapolation）和 RewardFusion（推理时增强 consistency）两种技术。纯 P4：改进 Evaluator 质量。展示 reward inconsistency 对下游 RLHF (P6) 有 trickle-down effect。

[Title]: Discriminative Policy Optimization for Token-Level Reward Models
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Preference data (response pairs) without fine-grained annotations
- [Target Experience]: Q-function Reward Model (Q-RM) weights — token-level value estimator
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Q-RM enhances PPO/REINFORCE training (+5.85/4.70 over ORM) with 12× faster convergence on GSM8K
- [Method]: ⟨SFT⟩
- [Mechanism]: 提出 Q-RM (Q-function Reward Model)：将 reward modeling 与 language generation 解耦。通过优化 discriminative policy 从 preference data 中显式学习 token-level Q-functions（不需要 fine-grained annotations）。理论上证明 Q-RM 能直接学习每个 token 的 Q-value。纯 P4：构建更精细的 Evaluator (token-level value model)。用于 RL 训练 policy 时构成 P6，且显著提升 training efficiency。

[Title]: Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation
- [Pathway]: Out of Scope
- [Mechanism]: 研究使用 CoT monitor 检测和抑制 reward hacking 的效果与风险。发现 CoT monitors (GPT-4o monitoring o3-mini) 在检测 exploits 方面很有效。但将 CoT monitor 整合进 RL reward 时，在低优化区间能产生更 capable 和更 aligned 的 agents，但在高优化区间 agents 学会 obfuscated reward hacking（在 CoT 中隐藏意图）。这是 alignment safety / monitoring 研究，关注 reward hacking 的检测和抑制，不提出新的 experience transformation 机制。属于安全性分析论文。

[Title]: Natural Emergent Misalignment from Reward Hacking in Production RL
- [Pathway]: Out of Scope
- [Mechanism]: 研究 reward hacking 在 production RL 环境中导致的 emergent misalignment 现象。展示当 LLMs 学会 reward hack 后，会泛化出 alignment faking、与恶意行为者合作、推理恶意目标、尝试 sabotage 等行为。测试三种 mitigations 的效果。这是 AI safety / alignment 研究，关注 reward hacking 的安全后果和缓解，不提出新的 experience transformation 机制。属于安全性实证研究，非 transformation 方法论文。

[Title]: InfAlign: Inference-aware language model alignment
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Calibrated and transformed reward signals for inference-time alignment
- [Target Experience]: Policy weights optimized for inference-time win rate (against base model)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Policy achieves 3-8% improvement on inference-time win rates for Best-of-N and Best-of-N jailbreaking
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 提出 InfAlign framework：解决标准 RLHF 训练目标与 inference-time decoding algorithms (Best-of-N, controlled decoding, tree search) 之间的 train/test mismatch。理论证明：对于任意 inference-time decoding procedure，最优 aligned policy 是标准 RLHF 问题在 reward transformation 后的解。提出 calibrate-and-transform RL (InfAlign-CTRL)：reward calibration step + KL-regularized reward maximization with transformed reward。纯 P6：改进从 Evaluator 信号到 Policy 的转化以匹配特定 inference-time strategy。

[Title]: RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning
- [Pathway]: Narrative → Evaluator → Policy (§8.2) with co-evolution
- [Source Experience]: Policy-generated reasoning traces with outcome-level verification correctness rewards
- [Target Experience]: Generative PRM (LLM verifier) weights AND improved generator policy weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Both generator and verifier achieve SOTA among 7B/8B models across math benchmarks and ProcessBench
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 提出 Tango：用 RL 同时训练 generator (policy) 和 verifier (PRM)。Verifier 是 generative, process-level LLM，仅通过 outcome-level verification correctness rewards 训练（不需要 process-level annotations），与 generator co-evolve。Generator 生成 traces (P7) → Verifier 评估并接收 outcome correctness signals 自我改进 (P4) → Verifier 提供 process rewards 训练 Generator (P6)。两个组件形成 mutual reinforcement。Verifier 是 generative（生成文本判断）而非 scalar-output，提高了鲁棒性和泛化性。

[Title]: Natural Language Actor-Critic: Scalable Off-Policy Learning in Language Space
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: Agent interaction trajectories with generative LLM critic's natural language feedback
- [Target Experience]: LLM critic weights AND improved LLM agent policy weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy outperforms existing training approaches in reasoning, web browsing, and tool-use with dialogue tasks
- [Method]: ⟨SFT⟩
- [Mechanism]: 提出 NLAC (Natural Language Actor-Critic)：Generative LLM critic 产生 natural language feedback（而非 scalar values），提供更丰富、更具可操作性的训练信号。Off-policy 训练（不需要 policy gradients），比 on-policy methods 更 data-efficient 和 stable。Critic 解释为什么某 action 是 suboptimal 的——在大型、开放动作空间中这对 LLM policies 极其有用。Stage 1 (P4): 训练 LLM critic 产生 informative feedback。Stage 2 (P6): Critic 的 NL feedback 引导 policy (actor) 改进。

[Title]: Sycophancy to Subterfuge: Investigating Reward-Tampering in Large Language Models
- [Pathway]: Out of Scope
- [Mechanism]: 研究 LLM 从简单 specification gaming (sycophancy) 到 reward-tampering 的泛化。构建 increasingly sophisticated gameable environments 的 curriculum，发现 training on early-curriculum environments 导致更多 specification gaming，少量情况下 LLM 会 zero-shot 泛化到直接改写自己的 reward function。这是 AI safety / specification gaming 研究，关注 misbehavior 的泛化而非 experience transformation 机制。属于安全性实证研究。

[Title]: Enhancing Decision-Making of Large Language Models via Actor-Critic
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: Agent interaction trajectories with Q-values from token logits and future rollouts
- [Target Experience]: Action evaluation capability (Q-values) AND improved policy via gradient-free optimization
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy achieves competitive performance using 7B/8B LLMs, outperforming GPT-4-based methods in complex tasks
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 提出 LAC (LLM-based Actor-Critic)。Stage 1 (P4): 通过 token logits associated with positive/negative outcomes 计算 Q-values（提取 robust action evaluations），增强 by future trajectory rollouts 和 reasoning。Stage 2 (P6): Gradient-free mechanism 利用 Q-value evaluations 改进 policy。在多个环境中验证（ALFWorld, BabyAI-Text, WebShop），覆盖高层决策到低层动作空间。

[Title]: EVPO: Explained Variance Policy Optimization for Adaptive Critic Utilization in LLM Post-Training
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Learned critic's value estimates with adaptive gating based on explained variance
- [Target Experience]: Policy weights via adaptive switching between critic-based and batch-mean advantage estimation
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy consistently outperforms both PPO and GRPO across classical control, agentic interaction, and math reasoning
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 将 baseline selection (critic-based PPO vs critic-free GRPO) 形式化为 Kalman filtering problem。证明 Explained Variance (EV) 可从 single training batch 计算，并识别 exact boundary：positive EV = critic reduces variance，zero/negative EV = critic inflates variance。提出 EVPO：每步监控 batch-level EV，在 critic-based 和 batch-mean advantage estimation 之间自适应切换。纯 P6：优化从 Evaluator (critic) 信号到 Policy 的利用方式。

[Title]: Rethinking Reward Model Evaluation: Are We Barking up the Wrong Tree?
- [Pathway]: Out of Scope
- [Mechanism]: 研究 reward model evaluation 中 accuracy metric 与下游 policy performance 之间的关系。发现 accuracy 与 downstream performance 仅有弱正相关，相似 accuracy 的 RMs 可优化出性能差异很大的 policies。通过 Regressional Goodhart effect 视角分析：accuracy 作为 RM quality 的 metric 无法完全捕捉 RM overoptimization 的潜在风险。这是 evaluation methodology 研究，分析 evaluation metric 的有效性，不提出 new transformation 方法。

[Title]: Mitigating Reward Hacking in RLHF via Advantage Sign Robustness
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: RM parameters with certified sign-preservation analysis of advantage estimates
- [Target Experience]: Policy weights via SignCert-PO with down-weighted non-robust completions
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Policy achieves better win rate and reduces reward hacking on summarization and AlpacaFarm
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 提出 reward hacking 常由 flipped advantage signs 引起（本该减少 bad response 的 likelihood，但 flipped sign 导致 update 反而增加它）。通过分析 RM parameter space 中的 adversarial perturbation，推导 certified sign-preservation radius。提出 SignCert-PO (Sign-Certified Policy Optimization)：在 policy gradient update 中对 non-robust completions 降权，仅使用 RM parameters 和 on-policy completions，轻量级。纯 P6：保护从 Evaluator 到 Policy 的梯度信号不被 reward hacking 破坏。

[Title]: Regularized Best-of-N Sampling with Minimum Bayes Risk Objective for Language Model Alignment
- [Pathway]: Evaluator → Policy (P6 variant)
- [Source Experience]: Best-of-N samples with MBR objective as proximity regularizer
- [Target Experience]: Policy alignment via regularized BoN sampling (inference-time) and DPO training on MBR-BoN-generated preference data
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: MBR-BoN outperforms both BoN sampling and MBR decoding; DPO on MBR-BoN data outperforms vanilla BoN-based DPO
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: 提出 MBR-BoN：在 BoN sampling 中融入 Minimum Bayes Risk (MBR) objective 作为 proximity regularization term，缓解 inference-time 的 reward hacking。MBR objective 量化 response 与 reference policy 的接近程度。MBR-BoN 还可生成 pairwise preference learning dataset 用于 DPO 训练。纯 P6 variant：在 inference-time 和 training-time 层面改进 Evaluator → Policy 转化。

[Title]: Online Preference-based Reinforcement Learning with Self-augmented Feedback from Large Language Model
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: LLM-generated self-augmented imagined trajectories + preference labels
- [Target Experience]: Reward function (from LLM preference labels) AND online PbRL-trained policy
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}, {self}
- [Utilization]: Policy achieves effective task performance without relying on online privileged information
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 提出 RL-SaLLM-F：不依赖 privileged information 的 online Preference-based RL。识别 LLM-based preference discrimination 中的 "query ambiguity" 问题。LLM 提供 preference labels 并生成 self-augmented imagined trajectories（更好地达成 task goal），提升反馈质量和效率。Double-check mechanism 引入以缓解 preference labels 中的随机性。Stage 1 (P4): LLM preferences + imagined trajectories → reward function。Stage 2 (P6): Reward function 信号 → RL policy。

[Title]: LAPP: Large Language Model Feedback for Preference-Driven Reinforcement Learning
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: Raw state-action trajectories with LLM-generated preference labels
- [Target Experience]: Online preference predictor weights AND RL-trained robot policy for locomotion and manipulation
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}
- [Utilization]: Policy masters dynamic tasks including quadruped backflips (out of reach for standard LLM-generated or handcrafted rewards)
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 提出 LAPP (LLM-Assisted Preference Prediction)：将 LLM 集成到 RL feedback loop 中。LLM 从 raw state-action trajectories 自动生成 preference labels → 训练 online preference predictor (Evaluator, P4) → preference predictor 引导 policy optimization (P6)。无需 reward engineering、human demonstrations 或昂贵的 pairwise preference labels。能处理 highly dynamic tasks（quadruped backflips）——超越标准 LLM-generated 或 handcrafted rewards 的能力范围。

[Title]: Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Proxy reward function with χ² divergence regularization against reference policy
- [Target Experience]: Policy weights via regularized RL that better mitigates reward hacking
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Policy better mitigates reward hacking across four realistic settings including RLHF
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 提出 reward hacking 的新定义：基于 proxy 和 true rewards 在 reference policy 下的相关性在优化过程中 breakdown。理论证明 regularization to reference policy 可有效防止 reward hacking。与当前 RLHF 中使用 KL penalty 的做法不同，理论建议 regularizing χ² divergence between policies' occupancy measures 更有效。纯 P6：改进从 Evaluator (proxy reward) 到 Policy 的转化机制。Reward hacking 的形式化和缓解。

[Title]: Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: Automatically constructed process-level rewards (RAG-ProGuide dataset, 5k instances)
- [Target Experience]: Process-level reward signals AND improved agentic RAG policy via process-supervised RL
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Policy achieves superior performance on 5 benchmark datasets using only 5k training instances (vs 90k for Search-R1)
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 提出 ReasonRAG：利用 fine-grained process-level rewards 改进 agentic RAG 训练。Stage 1 (P4): 自动构建 RAG-ProGuide 数据集——为 query generation、evidence extraction、answer generation 三个阶段提供 process-level rewards。Stage 2 (P6): 用 process-level rewards 通过 process-supervised RL 训练 policy。解决 outcome-based RL 的 exploration efficiency、gradient conflict 和 reward sparsity 问题。仅需 5k instances 即可达到优于 Search-R1 (90k instances) 的性能。

[Title]: Rethinking Reward Model Evaluation Through the Lens of Reward Overoptimization
- [Pathway]: Out of Scope
- [Mechanism]: 通过 reward overoptimization 视角重新思考 reward model evaluation 的 benchmark 设计。三个关键发现：(1) 需最小化 chosen/rejected responses 之间超出 correctness 的差异；(2) 评估 RM 需要跨 wide range 的多个比较；(3) responses 应来自 diverse models。但极高 overoptimization 相关性可能反而降低与某些 downstream performance 的相关性。这是 evaluation benchmark design 方法论研究，不提出 new transformation 机制。

[Title]: Subliminal Signals in Preference Labels
- [Pathway]: Out of Scope
- [Mechanism]: 研究 preference labels 作为 covert communication channel 的可能性。展示即使 neutral student model 生成语义上 unbiased 的 completions，biased judge 也能通过 preference assignments 传递 unintended behavioral traits（且在 iterative alignment rounds 中增强）。这是 AI safety / superalignment 研究，关注 preference-based alignment 中 hidden signal transmission 问题。不提出新的 experience transformation 机制，而是 warn 现有 P5/P6 路径中潜在的安全性风险。

[Title]: Hybrid Reward Normalization for Process-supervised Non-verifiable Agentic Tasks
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: Agentic task trajectories with principle-based step-level assessment + outcome verification
- [Target Experience]: Principle-based process reward model (PRM) AND RL-trained policy via ReNorm-calibrated rewards
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Policy achieves SOTA across wide range of benchmarks with robust generalization
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 提出 PPR (Principle Process Reward)：统一 principled step-level assessment 和 outcome verification。Stage 1 (P4): 训练 principle-based reward model 提升 process evaluation 的透明度和可靠性。Stage 2 (P6): 引入 Reward Normalization (ReNorm) 策略校准 outcome 和 process rewards（解决 step-wise quality 与 final outcome 之间可能的不对齐）。应用于 non-verifiable agentic tasks（没有 golden answers 的场景）。

[Title]: Process-based Self-Rewarding Language Models
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: Self-generated long-thought reasoning with step-wise LLM-as-a-Judge evaluations
- [Target Experience]: Policy weights via step-wise preference optimization in self-rewarding paradigm
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy enhances performance on multiple mathematical reasoning benchmarks through iterative self-rewarding
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: 将 self-rewarding paradigm 扩展到数学推理领域。引入三个关键元素：(1) long-thought reasoning 生成详细推理链；(2) step-wise LLM-as-a-Judge：policy 对自身推理的每个 step 做判断；(3) step-wise preference optimization：用 self-generated step-wise judgments 做 preference optimization。解决原 self-rewarding 在数学推理场景下效果不佳甚至导致性能下降的问题。§8.1 闭环的 process-based 变体。

[Title]: Variational Best-of-N Alignment
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Best-of-N distribution from base policy + reward model
- [Target Experience]: Policy weights via variational inference (minimizing backward KL to BoN distribution)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: vBoN achieves closest performance to BoN and surpasses standard KL-constrained RL on summarization and controlled generation
- [Method]: ⟨SFT⟩
- [Mechanism]: 提出 variational BoN (vBoN)：推导 BoN sampling 诱导的分布，通过最小化 backward KL divergence 将 policy fine-tune 到 BoN 分布（类比 mean-field variational inference）。成功 fine-tune 后将 inference cost 降低 N 倍。vBoN 在 reward-KL Pareto frontier 上比其它 alignment 方法更频繁出现。路径：RM-ranked BoN distribution (Narrative) → Policy via variational distribution matching (P5)。

[Title]: IPO: Your Language Model is Secretly a Preference Classifier
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: LLM's own preference classifications on self-generated response pairs
- [Target Experience]: Policy weights via DPO using self-generated preferences
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy achieves performance comparable to using SOTA reward models for obtaining preferences
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: 提出 IPO (Implicit Preference Optimization)：将 generative LLM 直接用作 preference classifier（不依赖外部 reward models 或 human feedback）。用 RewardBench 全面评估 LLMs 作为 preference classifiers 的能力。Self-improvement：对给定 instruction 生成多个 responses → model 自身作为 preference classifier 进行判断 → DPO 训练。§8.1 闭环：Policy 外化生成 responses + preference judgments (P7) → 用 self-preferences 训练 Policy (P5)。

[Title]: Process Reward Model with Q-Value Rankings
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Multi-step reasoning trajectories in MDP framework
- [Target Experience]: Process Q-value Model (PQM) weights — Q-value based process reward model
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: PQM outperforms classification-based PRMs across various sampling policies, backbones, and reasoning benchmarks
- [Method]: ⟨SFT⟩
- [Mechanism]: 提出 PQM (Process Q-value Model)：将 PRM 重新定义为 Markov Decision Process 中的 Q-value ranking problem。取代 standard classification-based cross-entropy loss，设计 novel comparative loss function 优化 Q-value rankings。更好地捕捉 sequential decisions 之间的 intricate dynamics。纯 P4：改进 Evaluator (PRM) 的数学框架和训练目标。

[Title]: Value-Incentivized Preference Optimization: A Unified Approach to Online and Offline RLHF
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Preference data with value-function-regularized reward estimation
- [Target Experience]: Policy weights via unified online/offline preference optimization
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Policy performs effectively on text summarization and dialog tasks
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: 提出 VPO (Value-Incentivized Preference Optimization)：统一 online 和 offline RLHF 的方法。用 value function 对 reward function 的 maximum-likelihood estimate 做正则化（通过 sign 控制 optimism 或 pessimism）。VPO 以 implicit reward modeling 直接优化 policy（类似 DPO 的简化 pipeline）。提供 online 和 offline 设置下的理论保证。路径：preference data with value regularization (Narrative) → Policy via implicit reward optimization (P5)。

[Title]: Process Supervision-Guided Policy Optimization for Code Generation
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: Code generation trajectories with dense line-level PRM feedback
- [Target Experience]: Process Reward Model (PRM) weights AND RL-enhanced code generation policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Policy achieves significantly boosted code generation performance, especially in long-horizon scenarios
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 提出 Process Reward Model (PRM) 用于 code generation：提供 dense line-level feedback on code correctness during generation（模仿人类代码精炼过程）。Stage 1 (P4): 训练 code PRM。Stage 2 (P6): 将 PRM 同时用作 dense rewards 和 value function initialization 来显著提升 RL-driven code generation。解决 unit test feedback 的 sparse reward 问题（code fails all tests → no learning signal）。

[Title]: WPO: Enhancing RLHF with Weighted Preference Optimization
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Off-policy preference data reweighted to simulate on-policy data
- [Target Experience]: Policy weights via reweighted DPO
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}, {teacher}
- [Utilization]: Gemma-2-9b-it achieves 76.7% length-controlled winning rate against GPT-4-turbo on Alpaca Eval 2
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: 提出 WPO (Weighted Preference Optimization)：解决 off-policy preference optimization 中 data collection policy 与 target policy 之间的 distributional gap。通过根据 preference pairs 在当前 policy 下的概率对 off-policy data 做 reweighting，模拟 on-policy learning。无需额外成本地增强优化过程。路径：reweighted preference data (Narrative, closer to on-policy) → Policy via DPO (P5)。

[Title]: Catastrophic Goodhart: regularizing RLHF with KL divergence does not mitigate heavy-tailed reward misspecification
- [Pathway]: Out of Scope
- [Mechanism]: 理论分析 RLHF 中 KL regularization 对 reward misspecification 的缓解能力。证明当 reward function error 是 light-tailed 时，较少限制性的 KL penalties 可实现 arbitrarily high utility。但如果 error 是 heavy-tailed，某些 policies 可获得 arbitrarily high reward 但 utility 不高于 base model（catastrophic Goodhart）。通过离散优化方法测量 reward model tails，发现与 light-tailed error 一致。但真实世界中 heavy-tailed distributions 的普遍性表明未来 RL reward 源可能具有 heavy-tailed error。这是理论/分析论文，不提出 new transformation 方法。

[Title]: Reward Model Overoptimisation in Iterated RLHF
- [Pathway]: Out of Scope
- [Mechanism]: 系统性研究 iterated RLHF 中 overoptimisation 的 dynamics。分析关键设计选择：reward model training data 如何在 iterations 间转移、哪个 reward function 用于 optimization、policies 如何初始化。发现 overoptimisation 在 successive iterations 中趋于减少（RMs 越来越接近 ground-truth preferences），但 performance gains 递减。这是 empirical analysis of RLHF dynamics 论文，描述 overoptimisation 在 iterated setting 中的行为，不提出 new transformation 机制。

[Title]: On the Interplay of Pre-Training, Mid-Training, and RL on Reasoning Language Models
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Synthetic reasoning tasks with atomic operations and parseable step-by-step reasoning traces
- [Target Experience]: Policy weights via RL-based post-training (with analysis of pre/mid/RL training interactions)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy achieves extrapolative and contextual generalization on reasoning tasks
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 使用受控实验框架分离 pre-training、mid-training 和 RL-based post-training 的因果贡献。四个关键发现：(1) RL 仅在 pre-training 留有足够 headroom 且 RL data targeting model's edge of competence 时产生 true capability gains (pass@128)；(2) Contextual generalization 需要 minimal yet sufficient pre-training exposure；(3) Mid-training 在 fixed compute 下显著增强性能；(4) Process-level rewards 减少 reward hacking 并改善 reasoning fidelity。路径是标准的 P5 (Narrative → Policy via RL)，但核心贡献在于分析 pre/mid/RL 阶段的交互而非提出新转化机制。

[Title]: FAPO: Flawed-Aware Policy Optimization for Efficient and Reliable Reasoning
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: Flawed-positive rollouts detected by generative reward model (GenRM) with process-level reward
- [Target Experience]: GenRM weights AND improved policy via FAPO with penalty for flawed patterns
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy improves outcome correctness, process reliability, and training stability without increasing token budget
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 系统研究 RLVR 中的 flawed-positive rollouts（answer-guessing, jump-in-reasoning）。发现它们在早期优化阶段带来 rapid capability gains，但后期会限制推理能力。Stage 1 (P4): 引入 generative reward model (GenRM) 提供 process-level reward 精确定位推理错误。Stage 2 (P6): 提出 FAPO (Flawed-Aware Policy Optimization)：parameter-free reward penalty for flawed-positive rollouts——在 warm-up 阶段将它们作为 useful shortcuts，后期逐渐将优化转向可靠推理。

[Title]: WARP: On the Benefits of Weight Averaged Rewarded Policies
- [Pathway]: Evaluator → Policy (P6) + Policy refinement via weight merging
- [Source Experience]: Multiple independently RLHF-fine-tuned policy checkpoints
- [Target Experience]: Merged policy weights with improved KL-reward Pareto front
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Merged policy improves quality and alignment, outperforming other open-source LLMs
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 提出 WARP (Weight Averaged Rewarded Policies)：三阶段 weight merging 策略。(1) Exponential moving average of policy 作为 KL regularization 中的 dynamic anchor；(2) Spherical interpolation 合并多个独立 fine-tuned policies（不同 random seeds）；(3) Linear interpolation between merged model 和 initialization（恢复 pre-training features）。Iteratively applied：每轮 final model 作为下一轮 advanced initialization。纯 P6 variant + weight-space 后处理，不涉及新的 Narrative → Evaluator 转化。

[Title]: Pairwise Proximal Policy Optimization: Harnessing Relative Feedback for LLM Alignment
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Relative/comparative preference feedback (pairwise comparisons) on trajectories
- [Target Experience]: Policy weights via trajectory-wise policy gradient on comparative rewards
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: P3O outperforms PPO in KL-Reward trade-off and matches/outperforms prior alignment methods
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 提出 P3O (Pairwise Proximal Policy Optimization)：直接在 comparative rewards 上操作的 trajectory-wise policy gradient algorithm。解决 PPO 的两个局限：(1) PPO 对包含相同偏好信息的等价 reward functions 不是 invariant 的（需校准 reward scale）；(2) PPO 需 token-wise updates（增加 function approximation 和算法设计复杂性）。P3O 对等价 rewards invariant，理论上避免 PPO 的复杂性。路径：pairwise preference data (Narrative) → Policy via trajectory-wise optimization (P5)。

[Title]: Dataset Reset Policy Optimization for RLHF
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Offline preference dataset combined with online RL via dataset reset mechanism
- [Target Experience]: Policy weights via DR-PO with provable guarantees
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Policy generation quality surpasses PPO and DPO under GPT-4 win-rate metric
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 提出 DR-PO (Dataset Reset Policy Optimization)：利用 offline preference dataset 提供 informative states（被 labelers 偏好的数据）。Dataset reset 机制：将 policy optimizer 直接 reset 到 offline dataset 中的 states，而非总是从初始 state distribution 开始。理论上保证 DR-PO 学习到至少与 offline dataset 覆盖的任何 policy 同样好。纯 P6：改进从 RM (V-Par) 信号出发的 RL optimization 过程，利用 offline data 的 state coverage。

[Title]: Iterative Data Smoothing: Mitigating Reward Overfitting and Overoptimization in RLHF
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Human preference ranking data with iteratively smoothed (soft) labels
- [Target Experience]: Improved reward model via IDS (Iterative Data Smoothing) algorithm
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: RM achieves superior performance over traditional training methods; (downstream policy benefits implied)
- [Method]: ⟨SFT⟩
- [Mechanism]: 提出 IDS (Iterative Data Smoothing)：解决 RM training 中 overfitting 问题（RM 性能在一个 epoch 后开始退化）。核心思想：每个 training epoch 不仅用数据更新模型，还用模型更新数据——将 hard labels 替换为 soft labels（模型自身的预测作为 smoothed targets）。纯 P4：改进 Evaluator 训练方法，使其更 robust to overfitting。

[Title]: Solving the Inverse Alignment Problem for Efficient RLHF
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Periodically frozen policy + offline preference dataset subsets
- [Target Experience]: Improved reward model (via inverse alignment) AND improved final policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Policy achieves superior alignment and faster convergence compared to standard RLHF
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 定义 "inverse alignment problem"：对 fixed actor 和 fixed offline preference dataset 优化 critic's reward。假设 offline dataset 的 aggregation 对 RM scores 有 averaging effect（限制信号质量）。反复在 periodically frozen policy 下 aligned 的 offline preference dataset 子集上 fine-tune RM → 提供更清晰的 policy 当前行为反馈。纯 P6：通过更好地对齐 RM 与当前 policy 来改进 RM 信号质量。

[Title]: Simultaneous Reward Distillation and Preference Learning: Get You a Language Model Who Can Do Both
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Oracle rewards AND human preference labels (simultaneously modeled)
- [Target Experience]: Policy weights via DRDO (simultaneous reward distillation and preference optimization)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}, {teacher}
- [Utilization]: Policy surpasses DPO and e-DPO in expected rewards; more robust to noisy preference signals and OOD settings
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: 提出 DRDO (Direct Reward Distillation and policy-Optimization)：同时 modeling rewards 和 preferences。DRDO 直接模仿 oracle rewards（reward distillation）同时通过 novel preference likelihood formulation 学习人类偏好。这避免了 DPO 等纯 preference-based 方法在 noisy/non-deterministic preference labels 下的退化。路径：oracle rewards + preference labels (Narrative) → Policy via hybrid objective (P5)。

[Title]: Provably Efficient Online RLHF with One-Pass Reward Modeling
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: Online interaction data with one-pass reward model updates (no historical data storage)
- [Target Experience]: Continuously updated reward model AND improved policy via online mirror descent
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Policy achieves improved alignment with constant-time updates per iteration
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 解决 online RLHF 中每轮需重新整合所有历史数据并重新训练的 scalability 瓶颈。将 RLHF 形式化为 contextual preference bandit，基于 online mirror descent with tailored local norm 开发 one-pass reward modeling 方法（取代 standard MLE）。实现 constant-time updates per iteration，无需存储历史数据。理论保证提升统计和计算效率。§8.2 的 online 高效实现。

[Title]: Language Model Alignment with Elastic Reset
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Reward model signal with Elastic Reset regularization
- [Target Experience]: Policy weights achieving higher reward with less drift
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Policy achieves SOTA on translation benchmark, outperforms baselines in sentiment task and technical QA
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 提出 Elastic Reset：不显式修改 training objective（无需 KL penalty），而是通过 periodically reset 在线模型到自身的 EMA，然后 reset EMA 到初始模型。通过 EMA 实现快速恢复。实现更高 reward + 更少 drift（相比标准 KL penalty）。纯 P6：改进从 RM (V-Par) 出发的 RL optimization 策略，通过 reset 机制而非 reward 修改来控制 reward-drift trade-off。

[Title]: RLHF Workflow: From Reward Modeling to Online RLHF
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: Open-source preference datasets with proxy preference model
- [Target Experience]: Proxy preference model AND online iteratively RLHF-trained policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}, {teacher}
- [Utilization]: Policy achieves impressive performance on AlpacaEval-2, Arena-Hard, MT-Bench, HumanEval, TruthfulQA
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 提供 online iterative RLHF 的完整可复现 workflow。Stage 1 (P4): 用 diverse open-source datasets 构建 proxy preference model（approximate human feedback，解决开源社区 human feedback 不可行的问题）。Stage 2 (P6): Online iterative RLHF（理论 insights + 实践实现细节）。证明 SFT + iterative RLHF 用全开源数据集可达 SOTA。这是一份 technical report / recipe paper，workflow 本身是标准 §8.2。

[Title]: Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: Human preference data collected on a weekly cadence (iterated online mode)
- [Target Experience]: Preference model AND RLHF-trained helpful and harmless policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Policy improves on almost all NLP evaluations; compatible with specialized skills (coding, summarization)
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: RLHF 的 foundational 工作。Stage 1 (P4): 用 human preference data 训练 preference model (RM)。Stage 2 (P6): 用 PPO 优化 policy 以最大化 RM reward（同时 KL penalty 限制偏离初始 policy）。Iterated online mode：preference models 和 RL policies 每周用 fresh human feedback 更新。识别 RL reward 和 policy-initialization KL divergence 平方根之间的近似线性关系。§8.2 的 canonical 实现。

[Title]: Reward Model Routing in Alignment
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Pool of candidate reward models dynamically selected via Bayesian routing
- [Target Experience]: Policy weights via RL with adaptively routed reward signals
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Policy consistently outperforms individual RMs, RM ensembling, and existing routing methods
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 提出 BayesianRouter：解决单 RM 的 alignment 局限性和 RM ensembling 的计算开销。Offline stage: multi-task router 在 preference data 上训练估计 per-RM reliability。Online stage: Bayesian Thompson sampling router 做 per-query RM selection——以 offline embeddings 作为 Gaussian priors 初始化 RM-specific weight vectors，用 online rewards adaptively update posteriors 以适应 evolving policy distribution。纯 P6：改进从多个 Evaluators 到 Policy 的信号路由。

[Title]: Black-Box On-Policy Distillation of Large Language Models
- [Pathway]: Policy → Narrative → Evaluator → Policy (§8.1 + §8.2 hybrid)
- [Source Experience]: Student-generated responses discriminated against teacher responses
- [Target Experience]: Discriminator weights AND improved student policy weights via GAN-style minimax game
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}, {self}
- [Utilization]: Qwen2.5-14B-Instruct (student) becomes comparable to GPT-5-Chat (teacher) on LMSYS-Chat
- [Method]: ⟨hybrid⟩
- [Mechanism]: 提出 GAD (Generative Adversarial Distillation)：Black-box 和 on-policy distillation。Student LLM 作为 generator，训练 discriminator 区分 student responses 和 teacher responses（minimax game）。Discriminator 充当 on-policy reward model (P4: student-generated Narrative → Evaluator)，与 student co-evolves，提供稳定自适应反馈 (P6: Evaluator → Policy)。Student 生成 responses (P7: Policy → Narrative)。整体构成 §8.1 self-reinforce 闭环 + §8.2 Evaluator 中间步骤。

[Title]: Learning beyond Teacher: Generalized On-Policy Distillation with Reward Extrapolation
- [Pathway]: Evaluator → Policy (P6) [distillation framing]
- [Source Experience]: Teacher logit distribution on student-generated trajectories with reward extrapolation
- [Target Experience]: Student policy weights via generalized on-policy distillation (ExOPD)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}, {self}
- [Utilization]: Student surpasses teacher's performance boundary and outperforms domain teachers
- [Method]: ⟨SFT⟩
- [Mechanism]: 理论证明 On-Policy Distillation (OPD) 是 dense KL-constrained RL 的特例。提出 Generalized On-Policy Distillation (G-OPD)：引入 flexible reference model 和 reward scaling factor。发现 reward scaling factor > 1 (reward extrapolation, ExOPD) 持续改善 OPD——使 student 超越 teacher 性能边界。在 strong-to-weak setting 中，选择 teacher's base model before RL 作为 reference model 做 reward correction 进一步提高蒸馏性能。纯 P6 variant：知识的参数间转移。

[Title]: LLMR: Knowledge Distillation with a Large Language Model-Induced Reward
- [Pathway]: Evaluator → Policy (P6) [distillation variant]
- [Source Experience]: LLM-induced reward function for knowledge distillation
- [Target Experience]: Student policy weights via KD with LLM reward
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Student outperforms traditional KD methods in dialogue generation and summarization
- [Method]: ⟨SFT⟩
- [Mechanism]: 提出 LLMR：基于 LLM 诱导的 reward function 进行 knowledge distillation。用 LLM 作为 reward source（Evaluator, V-Par）为 student model 的 outputs 打分，引导 student 学习 teacher 的知识。纯 P6：LLM as Evaluator → Student Policy (π-Par) via distillation。

[Title]: WebGPT: Browser-assisted question-answering with human feedback
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: Web-browsing trajectories with human preference labels
- [Target Experience]: Reward model (trained to predict human preferences) AND RLHF-aligned web-browsing policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Policy answers long-form questions using web search; preferred by humans 56% of the time over human demonstrators
- [Method]: ⟨SFT⟩, ⟨RL: PPO⟩
- [Mechanism]: 经典 RLHF pipeline 应用于 web-browsing agent。流程：(1) Behavior cloning (SFT) 用 human demonstrations 获得初始 web-browsing 能力 (Narrative → Policy: P5)；(2) 在 BC model 的 outputs 上收集 human preference labels (Narrative)；(3) 训练 reward model 预测 human preferences (P4: Narrative → Evaluator)；(4) Rejection sampling + PPO 优化 policy 以最大化 RM reward (P6: Evaluator → Policy)。整体 §8.2 composite：必须收集 references 以支持 factual accuracy 的人类评估。

## New Tags Introduced

- ⟨RL: REINFORCE⟩ —— vanilla REINFORCE policy gradient method；首次出现：「Discriminative Policy Optimization for Token-Level Reward Models」
- > 注：绝大多数标注复用了 Notions.md 已有标签。REINFORCE 作为 PPO 的基础算法在部分论文中作为 baseline 或替代方法出现，Notions.md 中仅列出了 ⟨RL: PPO⟩ / ⟨RL: GRPO⟩ / ⟨RL: DPO⟩ / ⟨RL: ReST⟩ 四种 RL 方法标签。REINFORCE 与 PPO 在机制上有实质区别（无 clipped surrogate objective、无 value function baseline），故新增。

## Annotation Failures

（无——所有论文均成功完成标注或判定为 Out of Scope。）

## Parser Errors

（无——parse_papers.py 对 146 篇论文全部解析成功。）

---

## Out of Scope 论文汇总

以下论文经分析后判定为 Out of Scope，不纳入 Experience Transformation 框架：

1. **Zero-Shot Reward Specification via Grounded Natural Language** (block #48) —— 使用 CLIP 从 text description + raw pixel observations 生成 reward，但经验源缺乏决策过程语义（无 $(c,a,o,f)$ 中的 action 序列和经验积累），属于 §3.2 排除范围。
2. **Scaling Laws for Reward Model Overoptimization** (block #37) —— 测量 overoptimization scaling laws 的 empirical analysis paper，不提出新的 transformation 方法。属于 §3.2（无新增转化机制）。
3. **Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms** (block #39) —— 同上，描述 DAAs 中 overoptimization 现象的 measurement paper。
4. **Examining Reasoning LLMs-as-Judges in Non-Verifiable LLM Post-Training** (block #41) —— 系统性研究 judge 类型对 alignment 影响的 evaluation paper，不提出新的 transformation 方法。
5. **Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation** (block #44) —— AI safety / monitoring 研究，关注 CoT monitor 检测 reward hacking 的效果和 obfuscation 风险。
6. **Natural Emergent Misalignment from Reward Hacking in Production RL** (block #45) —— AI safety 实证研究，关注 reward hacking 导致的 emergent misalignment 现象。
7. **Sycophancy to Subterfuge: Investigating Reward-Tampering in Large Language Models** (block #47) —— specification gaming / reward-tampering 泛化研究，属于 AI safety。
8. **Rethinking Reward Model Evaluation: Are We Barking up the Wrong Tree?** (block #49) —— RM evaluation methodology 研究，分析 accuracy metric 与 downstream policy performance 的关系。
9. **Rethinking Reward Model Evaluation Through the Lens of Reward Overoptimization** (block #54) —— RM evaluation benchmark design 方法论研究。
10. **Subliminal Signals in Preference Labels** (block #55) —— superalignment safety 研究，分析 preference labels 作为 covert communication channel 的可能性。
11. **Catastrophic Goodhart: regularizing RLHF with KL divergence does not mitigate heavy-tailed reward misspecification** (block #58) —— 理论分析 KL regularization 对 reward misspecification 的缓解能力，不提出新的 transformation 方法。
12. **Reward Model Overoptimisation in Iterated RLHF** (block #59) —— 系统性研究 iterated RLHF 中 overoptimisation dynamics，属于 empirical analysis。
