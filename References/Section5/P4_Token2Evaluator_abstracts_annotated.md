****[Title]: GUI-Shepherd: Reliable Process Reward and Verification for Long-Sequence GUI Tasks
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: GUI interaction trajectories with human-annotated scores and GPT-4o generated rationales
- [Target Experience]: Process Reward Model (GUI-Shepherd PRM) weights
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {human}
- [Utilization]: 作为 RL training 的 reward provider（multi-turn online PPO）和 inference-time verifier
- [Method]: ⟨SFT⟩
- [Mechanism]: 在 52k GUI 交互轨迹上，利用 human-annotated scores 和 GPT-4o 生成的 rationale 作为监督信号，训练一个 Process Reward Model，使其能为 GUI agent 的每一步 action 提供 dense step-level feedback；PRM 随后在 online PPO 中作为 reward provider 提供逐步奖励信号，或在推理时作为 verifier 筛选 action。

[Title]: Web-Shepherd: Advancing PRMs for Reinforcing Web Agents
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Web navigation trajectories with step-level preference pairs and annotated checklists
- [Target Experience]: Process Reward Model (Web-Shepherd PRM) weights
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {self}, {human}
- [Utilization]: 作为 verifier 在 inference-time 评估 web navigation trajectories；可配合 policy model (GPT-4o-mini) 做 test-time verification
- [Method]: ⟨SFT⟩
- [Mechanism]: 构建 WebPRM Collection（40K step-level preference pairs + annotated checklists），以此为监督信号训练 Web-Shepherd PRM，使其能评估 web navigation 每一步的正确性与进展；训练好的 PRM 在推理时作为 verifier 对候选 trajectory 进行 step-level 评分与筛选。

[Title]: OS-Oracle: A Comprehensive Framework for Cross-Platform GUI Critic Models
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Cross-platform GUI interaction data (310k critic samples from Mobile/Web/Desktop)
- [Target Experience]: Critic Model (OS-Oracle-7B) weights
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {teacher}
- [Utilization]: 作为 pre-critic 在 action 执行前评估其正确性，提升 native GUI agents 在 OSWorld/AndroidWorld 的表现
- [Method]: ⟨SFT⟩, ⟨RL: GRPO⟩
- [Mechanism]: 两阶段训练：(1) SFT 阶段在 310k critic samples 上训练基础 critic 能力；(2) CP-GRPO (consistency-preserving GRPO) 阶段通过 group relative policy optimization 增强 critic 的评估一致性与准确性。Critic 在推理时作为 pre-execution filter 对每个 candidate action 评分。

[Title]: The Art of Building Verifiers for Computer Use Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: CUA trajectories with process and outcome human labels
- [Target Experience]: Structured evaluation rubrics + verifier design principles（自然语言评估准则）
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: 评估 CUA trajectory 是否成功完成用户指令（evaluation + training signal）
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 基于 human-labeled CUA trajectories 提炼四项 verifier 设计原则和结构化 rubric：rubric-based evaluation、process/outcome reward 分离、controllable vs uncontrollable failure 区分、divide-and-conquer context management。本质是将 trajectory evaluation 经验抽象为评估准则（Narrative → Narrative，P1），不涉及 V-Par 权重训练。Universal Verifier 是 prompt/rubric-based 系统而非 trained parametric evaluator。

[Title]: Autonomous Evaluation and Refinement of Digital Agents
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Agent trajectories from web navigation and device control benchmarks
- [Target Experience]: Automatic evaluator models (multiple variants trading off cost/modularity/accuracy)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 评估 agent trajectories 的正确性 (74.4-92.9% agreement with oracle)；同时用于 fine-tuning 和 inference-time guidance 提升 agent 表现
- [Method]: ⟨SFT⟩
- [Mechanism]: 训练 domain-general automatic evaluators 来判断 agent trajectory 是否成功；训练数据来自 agent 在 benchmark 中的 rollout 与 oracle evaluation metrics 的对照。Evaluator 随后既用于 evaluation，也作为 reward signal 对 agent 做 fine-tuning 和 inference-time guidance。
- 注：本文 evaluator 的训练为 P4；用 evaluator 信号 fine-tune agent 的部分构成 P4+P6 composite，但 Abstract 对该 composite 的描述较简略，主贡献在 evaluator 构建。

[Title]: OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: GUI agent trajectories
- [Target Experience]: Multi-agent critic evaluation protocol（milestone-based decomposition + review chain 评估准则）
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 支持 online RL training（作为 reward provider）+ trajectory validation and filtering（self-training loop 中）
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 将 trajectory 分解为 verifiable milestones，通过多 agent 协作（decomposition + review mechanism）对每个 milestone 的证据链做严格审计后给出最终 verdict。本质是将 trajectory evaluation 经验抽象为结构化的多 agent 审查协议（Narrative → Narrative，P1），不涉及 V-Par 权重训练。OS-Themis 输出为基于审查协议的评估结论，而非可独立部署的 parametric evaluator。

[Title]: Scaling Agents for Computer Use
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Multiple rollout agent executions (raw behavior trajectories)
- [Target Experience]: Behavior narratives（结构化行为描述）
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 用于在多个 rollout 之间比较和选择最优 candidate behavior
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Behavior Judge (BJudge) 将 agent 的多次 rollout execution 表示为 behavior narratives，在此抽象层次上比较 candidate behaviors，从而选出最优执行路径。本质上是 raw trajectories → structured behavior descriptions 的 Narrative→Narrative 抽象转化（P1），而非训练 Evaluator 参数。目标载体是 Narrative（behavior descriptions），不是 V-Par。

[Title]: Look Before You Leap: A GUI-Critic-R1 Model for Pre-Operative Error Diagnosis in GUI Automation
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: GUI automation trajectories with action-outcome pairs
- [Target Experience]: Pre-operative critic model (GUI-Critic-R1) weights
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 在 action 实际执行前提供 pre-operative feedback，评估 action 的潜在结果和正确性
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 通过 reasoning-bootstrapping data collection pipeline 构建 GUI-Critic-Train 数据集；使用 S-GRPO (Suggestion-aware GRPO) 训练 critic model，引入 suggestion reward 增强反馈可靠性。Critic 在 action 执行前进行 pre-operative error diagnosis，预测 action 潜在结果并给出 corrective feedback。

[Title]: Let's Verify Step by Step
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Mathematical reasoning trajectories with step-level human feedback labels (PRM800K)
- [Target Experience]: Process-supervised Reward Model (PRM) weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: 作为 process reward model 在推理时对 reasoning steps 评分；也可用于 RL training 提供 dense reward
- [Method]: ⟨SFT⟩
- [Mechanism]: 收集 800K step-level human feedback labels（PRM800K），训练 PRM 对每个 intermediate reasoning step 给出 correctness score；通过 active learning 提升 process supervision 的数据效率。PRM 在 Best-of-N 等 test-time search 策略中为每一步提供细粒度评分。

[Title]: AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Multi-turn agent interaction trajectories (web shopping, browser navigation)
- [Target Experience]: AgentPRM（re-defined PRM for agent tasks）weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 评估每个 decision 的 promise 和 progress，guide agent 的 decision-making process；也可 apply to RL of LLM agents
- [Method]: ⟨RL: GRPO⟩, ⟨hybrid⟩
- [Mechanism]: 使用 Temporal Difference (TD) + Generalized Advantage Estimation (GAE) 自动标注 step-level labels，捕捉 sequential decisions 之间的 interdependence 和对 final goal 的 contribution；训练 PRM 同时建模每一步的 promise（离目标多远）和 progress（已取得多少进展），从而实现更好的 exploration-exploitation balance。

[Title]: GAIA: A Data Flywheel System for Training GUI Test-Time Scaling Critic Models
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: GUI agent action examples (positive/negative from base agent rollouts)
- [Target Experience]: Intuitive Critic Model (ICM) weights
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 在 test-time 评估 agent 每个 intended action 的 immediate correctness，选择高成功概率的 action
- [Method]: ⟨SFT⟩
- [Mechanism]: 先用 base agent 的 positive/negative action examples 训练第一轮 ICM；ICM 随后 guide agent actions 收集 refined samples，启动 self-improving cycle（data flywheel）；augmented data 再训练第二轮 critic。这是 critic 的 iterative self-improvement 通过数据飞轮实现，critic 本身通过 SFT 训练，不从 π-Par 外化数据。

[Title]: Advancing Mobile GUI Agents: A Verifier-Driven Approach to Practical Deployment
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Mobile GUI task trajectories with human-agent joint annotations
- [Target Experience]: Verifier model (V-Droid verifier) weights
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {human}
- [Utilization]: 在每步决策前评估 candidate actions，选择最优 action 执行
- [Method]: ⟨SFT⟩
- [Mechanism]: 通过 pair-wise progress preference training 训练 verifier 在 discretized action space 中比较 candidate actions；使用 human-agent joint annotation scheme 收集训练数据。Verifier 在推理时对候选 action 评分并选择最优，配合 prefilling-only workflow 加速验证（4.3s/step）。

[Title]: WebArbiter: A Principle-Guided Reasoning Process Reward Model for Web Agents
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Web navigation trajectories with preference annotations
- [Target Experience]: WebArbiter-7B (reasoning-first WebPRM) weights
- [Source Modality]: [vis+txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: 在 reward-guided trajectory search 中为每个 candidate action 提供 principle-guided reasoning 和 preference verdict
- [Method]: ⟨SFT⟩, ⟨RL: DPO⟩
- [Mechanism]: 两阶段训练：(1) reasoning distillation 阶段用 teacher model 的 principle-guided reasoning 做 SFT，使 PRM 具备结构化 justification 能力；(2) RL 阶段直接 align verdicts with correctness，纠正 teacher biases。PRM 以 text generation 形式输出 structured justification + preference verdict，比 scalar PRM 更具可解释性。

[Title]: Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Multi-step reasoning traces with automatically labeled progress signals
- [Target Experience]: Process Advantage Verifier (PAV) weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: test-time search（Best-of-N against PAV）+ online RL with dense rewards from PAV
- [Method]: ⟨SFT⟩
- [Mechanism]: 核心 insight 是 process reward 应衡量 progress（step 前后产生正确 response 的 likelihood 变化），对应 RL 中 step-level advantage 概念。PAV 在 prover policy（与 base policy 不同）下预测 progress，训练数据通过自动标注生成。PAV 提供 dense reward 用于 online RL（5-6x sample efficiency gain）和 test-time search（>8% accuracy gain）。

[Title]: Video-Based Reward Modeling for Computer-Use Agents
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Execution video keyframes from CUA trajectories (ExeVR-53k dataset)
- [Target Experience]: Execution Video Reward Model (ExeVRM 8B) weights
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: 仅凭 user instruction 和 video-execution sequence 预测 task success
- [Method]: ⟨SFT⟩
- [Mechanism]: 构建 ExeVR-53k（53k video-task-reward triplets），通过 adversarial instruction translation 合成带 step-level annotations 的负样本；设计 spatiotemporal token pruning 处理长视频冗余。在此数据上 fine-tune VLM 得到 ExeVRM，直接从 execution video keyframes 预测 task success，不依赖 agent 内部 reasoning 或 actions。

[Title]: Improve Mathematical Reasoning in Language Models by Automated Process Supervision
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Mathematical reasoning CoT traces with automatically collected process supervision annotations (1.5M)
- [Target Experience]: Process Reward Model (PRM) weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 与 weighted self-consistency 算法结合，在推理时增强 LLM math reasoning
- [Method]: ⟨MCTS⟩, ⟨SFT⟩
- [Mechanism]: OmegaPRM（divide-and-conquer MCTS 算法）通过 binary search 自动识别 CoT 中的第一个错误步骤，高效收集 1.5M process supervision annotations；用此自动标注数据训练 PRM，无需 human intervention。PRM 在推理时配合 weighted self-consistency 做 solution selection。

[Title]: UI-Genie: A Self-Improving Approach for Iteratively Boosting MLLM-based Mobile GUI Agents
- [Pathway]: Narrative → Evaluator (P4) / 整体框架含 Policy → Narrative → Policy 闭环
- [Source Experience]: GUI agent trajectories with rule-based verification, controlled corruption, and hard negative mining
- [Target Experience]: UI-Genie-RM (reward model) weights + UI-Genie-Agent (policy) weights
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: RM 提供 action-level + task-level rewards；self-improvement pipeline 通过 reward-guided exploration 扩展 solvable tasks
- [Method]: ⟨hybrid⟩
- [Mechanism]: 多目标论文（同时产出 V-Par RM + π-Par agent）。RM 训练：通过 rule-based verification + controlled trajectory corruption + hard negative mining 生成 UI-Genie-RM-517k，训练 image-text interleaved RM 同时提供 action-level 和 task-level rewards。Agent 训练：self-improvement pipeline 通过 reward-guided exploration + outcome verification 生成 UI-Genie-Agent-16k 做 SFT。整体构成 Policy → Narrative（agent rollout）→ Evaluator（RM scoring）→ Policy（RM-guided SFT/RL）的自生成闭环（§8.1 信号）。主轴标注为 P4，但 Mechanism 中包含 P7 + P4 + P5/P6 的复合链路。

[Title]: IntentScore: Intent-Conditioned Action Evaluation for Computer-Use Agents
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: 398K offline GUI interaction steps spanning 3 operating systems
- [Target Experience]: IntentScore (plan-aware reward model) weights
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 作为 re-ranker 对 candidate actions 评分，选出最优 action；部署于 Agent S3 上提升 OSWorld 表现
- [Method]: ⟨SFT⟩
- [Mechanism]: 训练时使用两个互补目标：(1) contrastive alignment for state-action relevance；(2) margin ranking for action correctness。架构上将 candidate 的 planning intent 嵌入 action encoder，使模型能区分相似 action 但不同 rationale 的候选。97.5% pairwise discrimination accuracy。

[Title]: ProgRM: Build Better GUI Agents with Progress Rewards
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: GUI agent online training trajectories with LCS-based auto-annotated progress labels
- [Target Experience]: Progress Reward Model (ProgRM) weights
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 在 online RL training 中提供 dense informative intermediate rewards（预测 task completion progress）
- [Method]: ⟨SFT⟩
- [Mechanism]: 设计 LCS-based (Longest Common Subsequence) self-annotation algorithm 自动发现 trajectory 中的 key steps 并分配 progress labels；ProgRM 训练为预测每步的 task completion progress，避免 ORM 的稀疏反馈和 over-penalize 问题。Actors 用 ProgRM 的 dense progress rewards 做 online RL training。

[Title]: Generative Verifiers: Reward Modeling as Next-Token Prediction
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: LLM-generated solutions with synthetic verification rationales
- [Target Experience]: Generative Verifier (GenRM) weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Best-of-N ranking：对 N 个 candidate solutions 评分选出最优
- [Method]: ⟨SFT⟩
- [Mechanism]: 将 verifier 训练为 next-token prediction 任务（而非 discriminative classification），jointly 训练 verification 和 solution generation；GenRM 可利用 CoT reasoning、majority voting 等 LLM 原生能力。用 synthetic verification rationales 作为训练数据，使 GenRM 能检测 subtle errors。

[Title]: MagicGUI-RMS: A Multi-Agent Reward Model System for Self-Evolving GUI Agents via Automated Feedback Reflux
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: GUI agent trajectories with automatically constructed balanced reward datasets
- [Target Experience]: Multi-agent reward model system (DS-RM + GP-RM)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 识别 erroneous actions、提出 refined alternatives、通过 automated data-reflux 持续增强 agent behavior
- [Method]: ⟨hybrid⟩
- [Mechanism]: 构建 structured data construction pipeline 自动生成 balanced and diverse reward datasets；训练 DS-RM（Domain-Specific RM）做 fine-grained action assessment + GP-RM（General-Purpose RM）做跨任务泛化。部署时 reward model system 识别错误 action 并提议修正，修正后的 trajectory 通过 data-reflux mechanism 回流至训练集，实现 self-evolving。整体形成 Policy → Narrative → Evaluator → Narrative(refined) → Policy 闭环，但主轴为 Evaluator 训练（P4）。

[Title]: WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning
- [Pathway]: Narrative → Evaluator → Policy (P4 + P6, §8.2)
- [Source Experience]: Web agent interaction trajectories from online curriculum
- [Target Experience]: Outcome-supervised Reward Model (ORM) weights + Web agent policy weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: ORM 提供 robust outcome-supervised reward signal；policy 通过 adaptive RL strategies 持续改进
- [Method]: ⟨SFT⟩, ⟨RL: PPO⟩
- [Mechanism]: 三组件协同：(1) self-evolving curriculum 从失败尝试生成新任务（P7 外化）；(2) 训练 ORM 提供 robust outcome-supervised reward（P4）；(3) adaptive RL strategies 用 ORM 信号训练 policy（P6）。整体为 Policy → Narrative（rollout）→ Evaluator（ORM）→ Policy（RL）的自生成闭环（§8.1 + §8.2 重叠）。主轴按训练流程标注为 P4+P6 composite。

[Title]: Solving math word problems with process- and outcome-based feedback
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Mathematical reasoning trajectories (GSM8K) with process-based and outcome-based feedback
- [Target Experience]: Learned reward models that emulate process-based feedback
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 提供 process-based feedback 用于监督 reasoning steps 的正确性
- [Method]: ⟨SFT⟩
- [Mechanism]: 系统比较 outcome-based vs process-based supervision 在数学推理任务上的效果；训练 learned reward models 来 emulating process-based feedback，为每个 reasoning step 提供监督信号。发现 pure outcome-based supervision 在 final-answer error 上效果相当，但正确 reasoning steps 需要 process-based supervision。

[Title]: SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from Experience
- [Pathway]: Narrative → Evaluator (P4) / 整体框架含 Policy → Narrative → Evaluator → Policy 闭环
- [Source Experience]: Agent interaction trajectories from autonomous exploration of novel software
- [Target Experience]: World State Model (evaluator) weights + Agent policy weights (via GRPO + adversarial imitation)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: World State Model 做 step-wise trajectory assessment；Curriculum Generator 生成递增难度任务；policy 通过 experiential learning 更新
- [Method]: ⟨hybrid⟩
- [Mechanism]: 多目标论文（同时产出 V-Par World State Model + π-Par agent policy + curriculum/task N-Tok）。Policy 在 novel software 中自主探索（P7 外化 trajectory）；World State Model 对 trajectory 做 step-wise assessment（P4）；policy 通过 adversarial imitation of failure actions + GRPO on successful ones 更新（P5）；Curriculum Generator 从简单到复杂生成新任务（Narrative→Narrative，P1）。specialist-to-generalist training 将多个 specialist agent 的经验整合为 generalist。多目标并列（§8.8），主轴按核心贡献标注为 P4（World State Model）+ P5（policy via GRPO）+ P7（trajectory generation）的复合。 
> New tag: ⟨RL: adversarial imitation⟩ —— 对失败 action 做 adversarial imitation learning，作为 GRPO 的补充训练策略，既有 ⟨SFT⟩ 的模仿属性又有 ⟨RL⟩ 的对抗属性，现有标签不足以精确刻画。

[Title]: Vision-Language Models as Success Detectors
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Visual trajectories from simulated household agents, real-world robot manipulation, and human egocentric videos
- [Target Experience]: Success detection model (Flamingo-based VLM) weights
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {human}
- [Utilization]: 检测 agent behavior 是否成功；作为 generalizable reward model 用于训练 agents
- [Method]: ⟨SFT⟩
- [Mechanism]: 将 success detection 形式化为 Visual Question Answering (SuccessVQA)；在 Flamingo VLM 上使用 human reward annotations fine-tune success detector。该 success detector 可跨 domain（simulated household / real robot / egocentric video）泛化，作为 reward model 评估 behavior 是否成功。

[Title]: StepWiser: Stepwise Generative Judges for Wiser Reasoning
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: LLM reasoning rollouts with relative outcome comparisons
- [Target Experience]: StepWiser (generative judge with meta-reasoning) weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 评估 policy model 每个 reasoning step 的正确性；用于 training-time policy improvement 和 inference-time search
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 将 stepwise reward modeling 从 classification 重构为 reasoning task；StepWiser 在给出 verdict 前先产生 thinking tokens（meta-reasoning about the policy model's reasoning）。训练使用 rollout 的 relative outcomes 作为 RL reward signal，无需 step-level human annotations。输出为 generative judgment，比 classifier-based PRM 更具可解释性。

[Title]: GroundedPRM: Tree-Guided and Fidelity-Aware Process Reward Modeling for Step-Level Reasoning
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: MCTS-constructed structured reasoning paths with tool-verified step-level labels
- [Target Experience]: GroundedPRM (generative, rationale-enhanced PRM) weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在 reward-guided greedy search 中为 reasoning steps 评分并选择最优路径
- [Method]: ⟨MCTS⟩, ⟨SFT⟩
- [Mechanism]: (1) MCTS 构建 structured reasoning paths 实现 fine-grained credit assignment，减少 reward noise；(2) 使用 external tool（如代码执行器）验证每个 intermediate step，消除 hallucinated supervision；(3) hybrid reward aggregation 融合 tool-based verification 与 MCTS-derived feedback；(4) 将 reward signal 格式化为 rationale-enhanced generative structure 增强可解释性。仅用 40K auto-labeled samples 训练，达到甚至超越 human-labeled PRM 的性能。

[Title]: OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis
- [Pathway]: Policy → Narrative (P7)
- [Source Experience]: Agent policy weights (GUI VLM agent) 在环境中自主探索
- [Target Experience]: High-quality GUI interaction trajectories (synthetic trajectory data)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 合成 trajectory 数据用于训练 GUI agents，提升其在 online benchmarks 上的表现
- [Method]: ⟨SFT⟩
- [Mechanism]: 逆转传统 trajectory collection 流程（P7 外化）：agent 先 perceive environment 并进行 step-wise interactions，再 retrospectively derive high-quality tasks 形成 trajectory-level exploration data。Trajectory reward model 在 pipeline 中起 quality filter 作用（辅助 P4），但主贡献是将 agent policy 的交互能力外化为可复用的 trajectory 数据集。属于 Parametric → Tokenized 的 P7 外化路径。

[Title]: RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning
- [Pathway]: Narrative → Evaluator (P4) / 整体含 Evaluator → Policy 的互训
- [Source Experience]: LLM reasoning rollouts with outcome-level verification correctness rewards
- [Target Experience]: Generative process-level LLM verifier weights + LLM generator (policy) weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Verifier 提供 process-level feedback 用于 guide generator 的 RL training；Generator 产生的新 rollouts 又用于训练 verifier
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: Verifier 和 Generator 通过 RL 交替训练（interleaved co-evolution）。Verifier 是 generative process-level LLM verifier，仅靠 outcome-level verification correctness rewards 训练，无需 process-level annotations。Generator 用 verifier 的 process-level feedback 做 RL training。两者形成 mutual reinforcement 循环（Evaluator → Policy 对应 P6，Policy → Narrative 提供新的 training data for Evaluator 对应 P7+P4）。整体为 co-evolution 的双向互训，主轴向按 Verifier 与 Generator 并重的贡献标注为 P4+P6 composite + P7 外化反馈环。

[Title]: SOLE-R1: Video-Language Reasoning as the Sole Reward for On-Robot Reinforcement Learning
- [Pathway]: Narrative → Evaluator (P4) / 整体含 Evaluator → Policy 的 RL 训练
- [Source Experience]: Robot video trajectories with temporally grounded CoT traces and continuous progress supervision
- [Target Experience]: SOLE-R1 (video-language reasoning model) weights as reward model + robot policy weights (via online RL)
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: SOLE-R1 提供 per-timestep dense task progress estimates 作为 RL reward signal; policy 通过 zero-shot online RL 从 random initialization 学习
- [Method]: ⟨hybrid⟩
- [Mechanism]: 两阶段：(1) 通过 large-scale video trajectory and reasoning synthesis pipeline 生成 temporally grounded CoT traces + continuous progress supervision，用 hybrid SFT + RL from verifiable rewards 训练 SOLE-R1 作为 video-language reward model（P4）；(2) policy 在 zero-shot online RL 中用 SOLE-R1 的 per-timestep progress estimates 作为唯一 reward signal（Evaluator → Policy，P6）。整体为 P4+P6 composite（§8.2），且 SOLE-R1 作为 sole reward 的特殊性在于完全替代 ground-truth reward。

[Title]: BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: GUI agent action trajectories with outcome page observations
- [Target Experience]: Verifier + Judger + Reflector components (evaluator modules)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 检测错误、判断是否需要 backtrack、reflect 产生修正策略
- [Method]: ⟨SFT⟩
- [Mechanism]: BacktrackAgent 包含三个 evaluator 组件：verifier 验证 action 执行结果、judger 判断是否需 backtrack、reflector 分析失败原因并生成修正策略。通过专门设计的 training dataset（考虑 action 执行后的 outcome pages）训练这些组件。Judgment rewards 进一步增强 agent 表现。核心贡献在通过多组件 evaluator 实现 error detection + recovery。

[Title]: Multi-step Problem Solving Through a Verifier: An Empirical Analysis on Model-induced Process Supervision
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Reasoning model's own completions used for automatic step annotation (MiPS)
- [Target Experience]: Verifier (PRM) weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 对 intermediate steps 评分，在推理时做 verification-guided selection
- [Method]: ⟨SFT⟩
- [Mechanism]: MiPS (Model-induced Process Supervision) 自动生成 verifier 训练数据：对每个 intermediate step，通过 reasoning model 采样多个 completions，计算正确 completion 的比例作为该 step 的 accuracy annotation。发现 verification focusing on high predicted scores 优于 low predicted scores（与 human curated data 上的观察相反）。Verifier 展现跨 reasoning model 的强泛化能力。

[Title]: RL-VLM-F: Reinforcement Learning from Vision Language Foundation Model Feedback
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Pairs of agent image observations with VLM preference labels
- [Target Experience]: Learned reward function (from preference labels)
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}
- [Utilization]: 作为 reward function 为 RL agent 提供训练信号
- [Method]: ⟨SFT⟩
- [Mechanism]: 查询 VLM 对 agent image observation pairs 给出 preferences（基于 task goal 的 text description），从 preference labels 学习 reward function（而非直接 prompt VLM 输出 raw reward score，避免噪声和不一致）。Learned reward function 然后用于 RL policy training。核心转化是 VLM 的 preference judgments → learned reward model 参数。

[Title]: A Rubric-Supervised Critic from Sparse Real-World Outcomes
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Human-agent interaction traces with 24 behavioral features (Critic Rubrics) + sparse human feedback
- [Target Experience]: Critic model weights (used for RL training or inference-time scaling)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}, {self}
- [Utilization]: best-of-N reranking on SWE-bench、early stopping、training-time data curation via critic-selected trajectories
- [Method]: ⟨SFT⟩
- [Mechanism]: 从 human-agent interaction traces 提取 24 behavioral features（Critic Rubrics）；使用 semi-supervised objective 同时预测 rubrics 和 sparse human feedback。Critic 尽管主要从 trace-observable rubrics 和 sparse real-world outcome proxies 训练，仍显著改善 Best@8 reranking (+15.9)、early stopping (+17.7, 83% fewer attempts) 和 training data curation。

[Title]: RoboReward: General-Purpose Vision-Language Reward Models for Robotics
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Real-robot trajectories from OXE and RoboArena + augmented negative/near-miss examples
- [Target Experience]: RoboReward 4B/8B (vision-language reward models) weights
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 为 robot RL 提供 reward signal；部署在 real-robot RL 中改善 policy learning
- [Method]: ⟨SFT⟩
- [Mechanism]: 通过 counterfactual relabeling of successful episodes + temporal clipping 从成功 trajectory 生成 calibrated negative and near-miss examples，解决 OXE 缺乏 failure examples 的问题。在构建的 RoboReward dataset 上训练 VLM-based reward model。8B 模型在 real-robot RL 中 outperforms Gemini Robotics-ER 1.5 并在缩小与 human-provided rewards 的差距。

[Title]: CUARewardBench: A Benchmark for Evaluating Reward Models on Computer-using Agent
- [Pathway]: Not a transformation paper — benchmark/evaluation resource
- [Source Experience]: N/A（benchmark paper，不提出新的 transformation 方法）
- [Target Experience]: N/A
- [Source Modality]: N/A
- [Target Modality]: N/A
- [Experience Source]: N/A
- [Utilization]: N/A
- [Method]: N/A
- [Mechanism]: 本文为 benchmark paper，引入 CUARewardBench 用于评估 CUA reward models (ORM/PRM)。主要贡献为 benchmark dataset、comprehensive analysis of current RM limitations、和 Unanimous Prompt Ensemble (UPE) 方法。UPE 是一种 prompt ensemble 策略而非 transformation 机制，不涉及经验载体转化。归入 benchmark/resource 类，不属于 transformation 论文。

[Title]: GUIDE: Interpretable GUI Agent Evaluation via Hierarchical Diagnosis
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Full GUI agent trajectories (action-observation sequences)
- [Target Experience]: Structured diagnostic reports (subtask-level verdicts + error analysis + corrective recommendations)
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 提供 interpretable diagnostic reports 直接 inform agent improvement
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 三层级联评估：Trajectory Segmentation 将 full trace 划分为 semantic subtask units → Subtask Diagnosis 对每个 unit 做 completion verdict + structured error analysis with corrective recommendations → Overall Summary 聚合为 task-level judgment。本质上是 raw GUI trajectories → structured diagnostic reports 的抽象转化（Narrative → Narrative，P1），不训练 Evaluator 参数，而是通过分解策略提升评估质量。

[Title]: Let's reward step by step: Step-Level reward model as the Navigators for Reasoning
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Multi-step reasoning trajectories (math + code) with automatically generated step-level reward dataset
- [Target Experience]: Process-Supervised Reward Model (PRM) weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在 inference phase 通过 heuristic greedy search 利用 step-level feedback 优化 reasoning pathways
- [Method]: ⟨SFT⟩
- [Mechanism]: 训练 PRM 为 multi-step reasoning 每个 step 提供 feedback（similar to PPO 或 reject sampling 中的 reward signal）。提出自动生成 code 任务 step-level reward dataset 的方法。在推理时，PRM 通过 heuristic greedy search 为 LLM 探索的 reasoning paths 提供 step-level 导航。

[Title]: Process Reward Model with Q-Value Rankings
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Multi-step reasoning trajectories with step-level correctness labels
- [Target Experience]: Process Q-value Model (PQM) weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在推理时对 multi-step reasoning 的每一步提供 granular process rewards
- [Method]: ⟨SFT⟩
- [Mechanism]: 将 PRM 重构为 Markov Decision Process 框架下的 Q-value ranking 问题；PQM 使用 novel comparative loss function 优化 Q-value rankings，捕捉 sequential decisions 之间的 intricate dynamics。相比 classification-based PRM（cross-entropy loss 独立评估每步），PQM 更好地建模步骤间依赖关系。

[Title]: Large Reward Models: Generalizable Online Robot Reward Generation with Vision-Language Models
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Large-scale multi-source dataset (real-world robot trajectories, human-object interactions, simulated environments)
- [Target Experience]: VLM-based online reward generator weights
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}, {human}
- [Utilization]: 在 closed-loop online policy refinement 中提供 multifaceted reward signal (process + completion + temporal contrastive rewards)
- [Method]: ⟨SFT⟩
- [Mechanism]: 在 large-scale multi-source dataset 上训练 VLM-based reward model，使其能基于当前 visual observations 生成 process reward、completion reward 和 temporal contrastive reward。Reward model 在 test environments 中以 zero-shot 方式运行，guided base policy（IL 初始化）在 30 RL iterations 内显著改善 success rate。

[Title]: AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Robotic failure trajectories generated by FailGen (procedural perturbation of successful demonstrations)
- [Target Experience]: AHA (failure detection and reasoning VLM) weights
- [Source Modality]: [embodied]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 提供 failure feedback 用于 refine dense reward functions、optimize task planning、improve sub-task verification
- [Method]: ⟨SFT⟩
- [Mechanism]: FailGen 通过 procedurally perturbing successful demonstrations 生成大规模 robotic failure trajectories（AHA dataset）。AHA 在此数据上 fine-tune，将 failure detection 作为 free-form reasoning task，输出 detailed natural language explanations。AHA 的 failure feedback 随后被集成到三个 manipulation frameworks 中（RL、task and motion planning、zero-shot trajectory generation），提升 policy performance。注意：AHA 的 failure feedback 属于 Narrative 输出（natural language reasoning），但模型本身是 V-Par evaluator，所以主轴是 P4。

[Title]: "Are We Done Yet?": A Vision-Based Judge for Autonomous Task Completion of Computer Use Agents
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Screenshots and task descriptions from 42 macOS applications (1,260 human-labeled tasks)
- [Target Experience]: Vision-based task completion judge weights
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {human}
- [Utilization]: 判断 task 是否完成；evaluator feedback 用于改善 agent 的 reliability 和 self-correction
- [Method]: ⟨SFT⟩
- [Mechanism]: 在 1,260 human-labeled tasks 的 screenshots + task descriptions 上训练 vision-language model 作为 task completion judge。Judge 直接从 screenshots 和 task descriptions 判断任务是否完成（73% accuracy）。Judge feedback 带来 27% average relative improvement in task success。

[Title]: Critique-out-Loud Reward Models
- [Pathway]: Out of Scope
- [Mechanism]: 排除理由：源经验为通用 RLHF 偏好数据（人类对 LLM 单轮响应的 preference judgments），非 Agent 在异构动作空间中的序贯决策经验。该 RM 训练属于通用 LLM alignment 基础设施，不满足 §3.1 纳入标准——源数据缺乏异构动作空间中的决策过程语义。

[Title]: SAFE: Multitask Failure Detection for Vision-Language-Action Models
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: VLA rollout trajectories (successful + failed) with internal VLA features
- [Target Experience]: SAFE failure detector (classification model) weights
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 在 robot 执行过程中提供 timely failure alert，使 robot 能 stop/backtrack/ask for help
- [Method]: ⟨SFT⟩
- [Mechanism]: 利用 VLA internal features（发现 VLA 对 task success/failure 已有 sufficient high-level knowledge）训练轻量 failure detector。SAFE 从 VLA 内部特征学习预测 single scalar indicating likelihood of task failure，无需额外环境交互。训练数据来自 VLA 的成功和失败 rollouts。

[Title]: OS-Sentinel: Towards Safety-Enhanced Mobile GUI Agents via Hybrid Validation in Realistic Workflows
- [Pathway]: Narrative → Evaluator (P4) / 含 Narrative → Schematic 的 Formal Verifier 分支
- [Source Experience]: Mobile GUI agent trajectories with fine-grained safety annotations (MobileRisk-Live)
- [Target Experience]: Hybrid safety detection framework (Formal Verifier + VLM-based Contextual Judge)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {human}
- [Utilization]: 在 agent 操作前检测 safety violations（system compromise, privacy leakage），阻止不安全操作
- [Method]: ⟨hybrid⟩
- [Mechanism]: 双组件：(1) Formal Verifier 检测 explicit system-level violations——将 trajectory 中的操作与安全规则做形式化匹配（Narrative → Schematic，P2）；(2) VLM-based Contextual Judge 评估 contextual risks 和 agent actions 的语义安全性（Narrative → Evaluator，P4）。两者协同形成 hybrid safety guard。整体可视为 safety-focused 的 evaluator 系统。

[Title]: Entropy-Regularized Process Reward Model
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Multi-step reasoning trajectories (MATH, GSM8K) with process supervision labels
- [Target Experience]: Entropy-Regularized PRM (ER-PRM) weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Best-of-N evaluation + RLHF（作为 reward model 引导 policy optimization）
- [Method]: ⟨SFT⟩
- [Mechanism]: 将 KL-regularized MDP 集成到 PRM 训练中，推导 novel reward construction method：optimal reward model 可从 initial policy sampling 推导。Entropy regularization 平衡 policy optimization 与防止 policy 偏离 initial distribution 过远。在 Best-of-N 和 RLHF 设置下均取得 consistent improvement。

[Title]: Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning
- [Pathway]: Narrative → Evaluator (P4) / 整体含 Evaluator → Policy 的 RL training
- [Source Experience]: Agentic RAG trajectories with process-level rewards (RAG-ProGuide dataset)
- [Target Experience]: Process-supervised reward model + reason-augmented policy weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 提供 process-level rewards 用于 (i) query generation, (ii) evidence extraction, (iii) answer generation 的 policy optimization
- [Method]: ⟨SFT⟩, ⟨RL: GRPO⟩
- [Mechanism]: ReasonRAG 自动构建 RAG-ProGuide 数据集（5K instances with process-level rewards for query generation + evidence extraction + answer generation），在此数据上训练 process-supervised reward model（P4）。然后用 process-level policy optimization 训练 LLM agent（P5/P6）。比较 process-supervised vs outcome-supervised RL 在 agentic RAG 上的效果，发现 process-supervised 在 sample efficiency 和 stability 上显著优于 outcome-supervised。

[Title]: Video-Language Critic: Transferable Reward Functions for Language-Conditioned Robotics
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Cross-embodiment robot behavior traces with temporal video data
- [Target Experience]: Video-Language Critic (reward model) weights
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 作为 reward model 为 separate actor 的 behavior traces 评分，实现 2x more sample-efficient policy training
- [Method]: ⟨SFT⟩
- [Mechanism]: 在 Open X-Embodiment data 上使用 contrastive learning + temporal ranking objective 训练 Video-Language Critic。Critic 将 language-conditioned task 与 robot behavior video 进行匹配评分。关键设计是分离 what to accomplish（可从 external observation-only data 学习）和 how to accomplish it（robot-specific），使 reward model 跨 embodiment 迁移。

[Title]: SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Repository-level code agent trajectories from SWE-Bench with action-level reward labels
- [Target Experience]: SWE-Shepherd PRM weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在 inference 时评估 candidate actions 并 guide agent 向 higher-reward decisions
- [Method]: ⟨SFT⟩
- [Mechanism]: 从 SWE-Bench trajectories 构建 action-level reward dataset，训练 lightweight PRM 估计每个 intermediate action 的 usefulness。在推理时 PRM 评估 candidate actions（code editing, file navigation, test execution 等）并导向高奖励决策，无需 full RL training。

[Title]: Adapt2Reward: Adapting Video-Language Models to Generalizable Robotic Rewards via Failure Prompts
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Robot video data from minimal tasks in a singular environment + human video-language datasets
- [Target Experience]: Language-conditioned reward function (VLM-based) weights
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}, {human}
- [Utilization]: 为 robot planning 和 RL 提供 generalizable language-conditioned reward
- [Method]: ⟨SFT⟩
- [Mechanism]: 将 video-language models 迁移为 language-conditioned reward function：利用 human video-language datasets（缺乏 failure videos），通过 clustering failure video features 识别 failure patterns，为每个 cluster 训练专门的 failure prompt 增强模型区分成功/失败的能力。Reward function 泛化到新环境和指令。

[Title]: Accurate Failure Prediction in Agents Does Not Imply Effective Failure Prevention
- [Pathway]: Not a transformation paper — empirical analysis of critic deployment
- [Source Experience]: N/A
- [Target Experience]: N/A
- [Source Modality]: N/A
- [Target Modality]: N/A
- [Experience Source]: N/A
- [Utilization]: N/A
- [Method]: N/A
- [Mechanism]: 本文为 empirical analysis paper，发现高准确率的 binary LLM critic (AUROC 0.94) 在部署时仍可能造成 severe performance degradation（disruption-recovery tradeoff）。提出 pre-deployment test 来估计 intervention 是否有效。核心贡献在 critic deployment safety 分析，不涉及 experience transformation 机制。

[Title]: Self-Generated Critiques Boost Reward Modeling for Language Models
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: LLM-generated critiques (self-generated) + human preference pairs
- [Target Experience]: Critic-RM (critique-augmented reward model) weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {human}
- [Utilization]: 作为 reward model 在 RLHF 中提供 scalar reward + critiques
- [Method]: ⟨SFT⟩
- [Mechanism]: 两阶段：(1) 生成并过滤高质量 self-generated critiques（Narrative → Narrative, P1: raw output → filtered critiques）；(2) joint fine-tuning on reward prediction + critique generation（Narrative → Evaluator, P4）。Critiques 提供额外监督信号，改善 reward modeling accuracy（+3.7%-7.3%）和 reasoning error rectification（+2.5%-3.2%）。

[Title]: CORA: Conformal Risk-Controlled Agents for Safeguarded Mobile GUI Automation
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: GUI action trajectories with step-level harm labels (Phone-Harm benchmark)
- [Target Experience]: Guardian model (risk estimation) + Diagnostician model (intervention recommendation) weights
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {human}
- [Utilization]: 在 action 执行前评估 risk，decide execute/abstain；对 rejected actions 推荐 interventions
- [Method]: ⟨SFT⟩
- [Mechanism]: 训练 Guardian model 估计每个 action 的 action-conditional risk；使用 Conformal Risk Control 校准 execute/abstain boundary（满足 user-specified risk budget）。Diagnostician model 对 rejected actions 做 multimodal reasoning 推荐 interventions (confirm/reflect/abort)。Goal-Lock mechanism 将评估锚定在 clarified user intent 上防止 visual injection attacks。核心为 safety-focused evaluator 架构。

[Title]: Better Process Supervision with Bi-directional Rewarding Signals
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Multi-step reasoning trajectories with step-level correctness labels
- [Target Experience]: BiRM (bidirectional process supervision model) weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在 Best-of-N sampling 和 search-based strategies 中提供更精确的 step-level 评估
- [Method]: ⟨SFT⟩
- [Mechanism]: 受 A* 算法启发，BiRM 同时建模两个方向：评估已执行步骤的正确性（incurred cost）+ 预测未来成功的概率（estimated cost to target）。这使 BiRM 比单向 PRM（仅看过去步骤）提供更全面的 guidance。在 Best-of-N（+3.1% on Gaokao2023）和 search-based strategies（+5.0% over ORM, +3.8% over PRM）上均取得改善。

[Title]: Don't Act Blindly: Robust GUI Automation via Action-Effect Verification and Self-Correction
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: GUI interaction trajectories with synthetic failure trajectories (Robustness Benchmark)
- [Target Experience]: VeriGUI verifier/critic weights + robust policy weights
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 在每步 action 后验证 action effect，检测 failure 并触发 self-correction
- [Method]: ⟨SFT⟩, ⟨RL: GRPO⟩
- [Mechanism]: 两阶段：(1) Robust SFT 在 synthetic failure trajectories 上训练 agent 识别和恢复失败；(2) GRPO with asymmetric verification rewards 增强 agent 的 verification 和 recovery 能力。TVAE 框架（Thinking-Verification-Action-Expectation）使 agent 在每步 action 后验证效果、检测失败并修正。核心为 verification-guided robust policy training。

[Title]: MotIF: Motion Instruction Fine-Tuning
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Robot demonstration videos with motion descriptions (MotIF-1K dataset: 653 human + 369 robot demos)
- [Target Experience]: VLM success detector (motion-aware) weights
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {human}, {self}
- [Utilization]: 评估 robot motion 是否成功 given task and motion instructions；ranking trajectories on alignment with task/motion descriptions
- [Method]: ⟨SFT⟩
- [Mechanism]: 使用 abstract representations（将 keypoint trajectories overlay 到 final image）捕捉 trajectory-level motion 信息，fine-tune VLM 使其能 semantically ground robot behavior。MotIF 解决 VLMs 难以从 full trajectory video 判断 success 的问题，通过 motion instruction fine-tuning 使 VLM 成为 trajectory-aware success detector。

[Title]: Enhancing Robotic Manipulation with AI Feedback from Multimodal Large Language Models
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Robot manipulation trajectory videos with CriticGPT-generated preference labels
- [Target Experience]: CriticGPT (MLLM-based critic) weights as reward model
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}
- [Utilization]: 提供 automated preference feedback 从 image inputs 引导 policy learning
- [Method]: ⟨SFT⟩
- [Mechanism]: 训练 multimodal LLM (CriticGPT) 理解 robot manipulation trajectory videos，输出 analysis 和 preference feedback。CriticGPT 生成的 preference labels 从 reward modeling perspective 验证有效性。CriticGPT's reward model 在 Meta-World 任务上有效引导 policy learning，超越基于 pretrained representation models 的 rewards。

[Title]: Towards Policy-Compliant Agents: Learning Efficient Guardrails For Policy Violation Detection
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Web agent trajectories with policy violation labels (PolicyGuardBench, ~60K examples)
- [Target Experience]: PolicyGuard-4B (guardrail model) weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在 agent trajectory 执行中/后检测 policy violations；支持 full-trajectory 和 prefix-based 两种检测
- [Method]: ⟨SFT⟩
- [Mechanism]: 从 diverse agent runs 生成 broad set of policies 并标注 violation labels，构建 PolicyGuardBench。训练轻量 PolicyGuard-4B guardrail model 检测 agent trajectories 是否违反 policies。模型能跨 domain 泛化，支持 prefix-based 检测（从 truncated trajectory 预测 violation）。

[Title]: AgentV-RL: Scaling Reward Modeling with Agentic Verifier
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: LLM reasoning solutions with tool-augmented multi-turn verification traces
- [Target Experience]: Agentic Verifier (multi-turn, tool-augmented verifier) weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在 test-time scaling（parallel and sequential）中提供 comprehensive and interpretable assessment of solutions
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 将 reward modeling 重构为 multi-turn, tool-augmented deliberative process。双向 agent 设计：forward agent traces solutions from premises to conclusions，backward agent re-checks conclusions against premises。通过 proactive exploration + RL (AgentV-RL) 训练 verifier 自主 interleave tool-use 与 internal reasoning。4B variant surpasses SOTA ORMs by 25.2%。

[Title]: Improving Reward Models with Synthetic Critiques
- [Pathway]: Out of Scope
- [Mechanism]: 排除理由：源经验为通用人类偏好数据（human preference scores on general LLM responses），synthetic critiques 作为辅助信号改善 RM 的 instruction following / correctness / style 评估。该 RM 面向通用 LLM 输出对齐，源数据非 Agent 序贯决策经验，不满足 §3.1 纳入标准。

[Title]: FuRL: Visual-Language Models as Fuzzy Rewards for Reinforcement Learning
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Sparse reward task rollouts with VLM-based reward signals
- [Target Experience]: Fine-tuned VLM reward model weights (through lightweight fine-tuning)
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}
- [Utilization]: 作为 fuzzy reward signal 为 online RL (SAC/DrQ) 提供训练奖励
- [Method]: ⟨SFT⟩
- [Mechanism]: 识别 VLM 直接用作 reward 时的 reward misalignment 问题。FuRL 通过 lightweight fine-tuning of VLM representations + relay RL 解决此问题：(1) fine-tune VLM 使其 reward signal 更准确对齐 task success；(2) relay RL 避免 local minima。在 Meta-world 稀疏奖励任务上验证。

[Title]: Scaling Agentic Verifier for Competitive Coding
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Code execution traces and program behaviors from competitive programming solutions
- [Target Experience]: Agentic Verifier (execution-based agent) weights for code verification
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在 test-time 通过 execution-based re-ranking 选出正确 solution
- [Method]: ⟨SFT⟩, ⟨RL: GRPO⟩
- [Mechanism]: Agentic Verifier 能在 code execution environment 中 multi-turn 交互，主动搜索 discriminative test inputs 来 expose behavioral discrepancies among candidate solutions。训练 pipeline：large-scale data synthesis → rejection fine-tuning → agentic RL。Verifier 学习生成 targeted counterexamples（而非 blind sampling），在 Best@K accuracy 上实现 +10-15% absolute gains。

[Title]: Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Math reasoning trajectories with 3D step-level labels (math errors, consistency errors, step correctness)
- [Target Experience]: PathFinder-PRM (hierarchical, error-aware discriminative PRM) weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}, {self}
- [Utilization]: 在 reward guided greedy search 中为每个 step 评分
- [Method]: ⟨SFT⟩
- [Mechanism]: 丰富 PRM800K + RLHFlow Mistral traces 为三维 step-level labels（math error type + consistency error type + step correctness）。PathFinder-PRM 先对每步做 error classification（math/consistency errors），再融合 fine-grained error signals 估计 step correctness。Decoupled error detection + reward estimation 提升 fine-grained error detection 和 end-to-end reasoning（PRMScore 67.7 on PRMBench，仅用 1/3 数据超越 prior best）。

[Title]: Enhancing LLM Reasoning via Critique Models with Test-Time and Training-Time Supervision
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: AutoMathCritique dataset (76,321 responses with step-level feedback)
- [Target Experience]: Critique model (providing natural language step-level feedback) weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: test-time: 提供 step-level feedback 改善 actor 在 difficult queries 上的表现；training-time: critique-in-the-loop self-improvement
- [Method]: ⟨SFT⟩
- [Mechanism]: AutoMathCritique 自动生成 step-level critique data。Critique model 在 test-time 为 actor 提供逐步反馈（尤其在 scaling inference-time compute 时有效）；在 training-time，critique-based supervision 被引入 actor 的 self-training process，改善 exploration efficiency 和 solution diversity。探索 critique supervision 训练 self-talk reasoning models。

[Title]: EVOLVE-VLA: Test-Time Training from Environment Feedback for Vision-Language-Action Models
- [Pathway]: Narrative → Evaluator (P4) / 整体含 Evaluator → Policy 的 Test-Time Training
- [Source Experience]: Robot interaction video + environment feedback (learned progress estimator)
- [Target Experience]: Learned progress estimator weights + continuously adapted VLA policy weights
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 提供 dense progress feedback 替代 oracle reward signals，在 test-time 持续 adapt VLA policy
- [Method]: ⟨SFT⟩
- [Mechanism]: 两个关键组件：(1) learned progress estimator 从 environment interaction 中提供 dense feedback（P4: 训练 evaluator from interaction data）；(2) accumulative progress estimation smoothing + progressive horizon extension "驯服" noisy signal。Policy 在 test-time 通过此 feedback 持续 adapt（Evaluator → Policy，P6）。整体为 P4+P6 composite，且核心创新在 test-time adaptation 闭环。

[Title]: Scaling Autonomous Agents via Automatic Reward Modeling And Planning
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Random agent navigation trajectories with task intent annotations + positive/negative responses
- [Target Experience]: Automatically learned reward model weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: 评估 action trajectories；为 task planning 提供 heuristics
- [Method]: ⟨SFT⟩
- [Mechanism]: 三步：(1) LLM agent 随机 navigate 环境生成 diverse action trajectories；(2) 另一个 LLM 为每条 trajectory 分配 task intent 并合成 negative response 与 correct response；(3) 用 (task intent, positive response, negative response) triplets 训练 reward model。无需 human annotations。

[Title]: Efficient PRM Training Data Synthesis via Formal Verification
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Formal reasoning trajectories with step-level error labels annotated by Z3/Isabelle
- [Target Experience]: PRM weights (fine-tuned on FoVer-generated data)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在推理时对 informal reasoning tasks 提供 process supervision
- [Method]: ⟨SFT⟩
- [Mechanism]: FoVer (Formal Verification) 利用 Z3、Isabelle 等形式验证工具自动标注 formal reasoning tasks 的 step-level error labels。在 FoVer 生成的 PRM training data 上 fine-tune 的 PRM 不仅在 math/logic 任务上提升，还泛化到 NLI 和 BBH 等 informal reasoning tasks。

[Title]: Teaching Language Models to Critique via Reinforcement Learning
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Code generation outputs with correction performance as reward signal
- [Target Experience]: CTRL critic model weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 提供 feedback 使 generator model 修正 code errors；作为 generative reward model 支持 test-time iterative critique-revision
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: CTRL 框架训练 critic model 生成 feedback，目标最大化 fixed generator model 的 correction performance，无需 human supervision。Critic 的 reward 来自其 feedback 帮助 generator 修复代码的实际效果。CTRL-trained critic 同时充当 accurate generative reward model，支持 iterative critique-revision（test-time scaling，relative improvement up to 106.1%）。

[Title]: Self-Refining Vision Language Model for Robotic Failure Detection and Reasoning
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Robotic failure/success trajectories with heterogeneous supervision (large-scale sparse binary labels + small-scale rich reasoning annotations)
- [Target Experience]: ARMOR (multi-task VLM for failure detection + reasoning) weights
- [Source Modality]: [embodied]
- [Target Modality]: [txt]
- [Experience Source]: {human}, {self}
- [Utilization]: 检测 robot 是否失败 + 输出 failure reasoning（natural language explanations）
- [Method]: ⟨hybrid⟩
- [Mechanism]: 将 failure detection 和 reasoning 作为 multi-task self-refinement process：模型迭代预测 detection outcomes 和 natural language reasoning conditioned on past outputs。训练结合 offline 和 online imitation learning 处理 heterogeneous supervision。推理时生成多个 refinement trajectories，通过 self-certainty metric 选择最 confident prediction。

[Title]: No More Stale Feedback: Co-Evolving Critics for Open-World Agent Learning
- [Pathway]: Narrative → Evaluator → Policy (P4 + P6, §8.2) / 含双向 co-evolution
- [Source Experience]: Agent rollout trajectories in open-world environments
- [Target Experience]: ECHO critic weights + agent policy weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Critic 提供 natural-language feedback 为 policy 做 RL training
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: ECHO 框架同时优化 policy 和 critic 通过 synchronized co-evolutionary loop：(1) cascaded rollout mechanism: critic 生成多个 diagnoses for initial trajectory；(2) policy refinement 通过 group-structured advantage estimation；(3) saturation-aware gain shaping 奖励 critic 在 high-performing trajectories 上的 incremental improvements。Dual-track GRPO updates 确保 critic feedback 与 evolving policy 同步。整体为 P4+P6 composite + co-evolution 同步机制。

[Title]: SPC: Evolving Self-Play Critic via Adversarial Games for LLM Reasoning
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Adversarially generated reasoning steps (from sneaky generator) with game outcome rewards
- [Target Experience]: SPC critic model weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在 test-time search 中评估 LLM reasoning steps 的正确性；guide diverse LLMs 改善 math reasoning
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 两个 model copy 进行 adversarial self-play：sneaky generator 故意生成难以检测的错误步骤；critic 分析 reasoning steps 的正确性。Game outcome（critic 是否识别出错误）作为 RL reward 驱动双方迭代进化。无需 manual step-level annotations。Critic accuracy 从 70.8% 提升到 77.7% on ProcessBench。

[Title]: Code as Reward: Empowering Reinforcement Learning with VLMs
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: VLM image-based observations with task descriptions
- [Target Experience]: VLM-generated dense reward functions (as executable code)
- [Source Modality]: [vis+txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: 作为 dense reward function 为 RL agent 提供训练信号
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: VLM-CaR 通过 code generation 从 VLM 产生 dense reward functions：VLM 分析 image-based observations 和 task descriptions，生成可执行的 reward code，而非频繁 query VLM（计算昂贵）。生成的 dense rewards 比原始 sparse environment rewards 更有效。核心转化是 VLM 的 visual understanding → executable reward code（属于 Narrative → Schematic 的 P2，但 reward code 本身是 evaluator 的替代物，作为规则化评估器）。

[Title]: SCRIBE: Structured Mid-Level Supervision for Tool-Using Language Models
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Tool-use agent trajectories with skill prototype library (structured rubrics)
- [Target Experience]: Skill-conditioned reward model weights (equipped with precise structured rubrics)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {human}
- [Utilization]: 为 RL training 提供 mid-level reward signal（在 high-level planning 和 low-level execution 之间）
- [Method]: ⟨SFT⟩, ⟨RL: GRPO⟩
- [Mechanism]: SCRIBE 将 reward modeling 锚定在 curated skill prototypes library 上，将 open-ended LLM evaluation 转化为 constrained verification problem。每个 subgoal 被路由到对应 prototype，使 reward model 配备 precise structured rubrics，大幅降低 reward variance。在 tool-use 和 reasoning benchmarks 上达到 SOTA。观察 co-evolution：mid-level skill mastery 先于 high-level planning emergence。

[Title]: Uncertainty-Aware Step-wise Verification with Generative Reward Models
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Multi-step reasoning solutions with step-wise verification labels
- [Target Experience]: Uncertainty-aware generative PRM weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在推理时提供 step-wise verification with uncertainty estimates
- [Method]: ⟨SFT⟩
- [Mechanism]: 提出 CoT Entropy（novel uncertainty quantification method）量化 generative reward model 在 step-wise verification 中的 uncertainty。将 uncertainty estimates 整合进 PRM 的 verification process，提升 judge-LM PRM 的 reliability 和对 reward hacking 的鲁棒性。

[Title]: Natural Language Actor-Critic: Scalable Off-Policy Learning in Language Space
- [Pathway]: Narrative → Evaluator (P4) / 整体含 Evaluator → Policy (P6)
- [Source Experience]: Agent interaction trajectories (reasoning, web browsing, tool-use with dialogue)
- [Target Experience]: Generative LLM critic weights + LLM policy weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Critic 提供 natural language feedback 指导 policy 改进 actions
- [Method]: ⟨SFT⟩
- [Mechanism]: NLAC 提出 generative LLM critic 输出 natural language explanations（而非 scalar values）作为 training signal。Critic 解释 action 为何 suboptimal，使 policy 能 reason about how to improve。Off-policy training 无需 policy gradients，比 on-policy 方法更 data-efficient 和 stable。整体为 Evaluator → Policy（P6），critic 通过 SFT 从 trajectory data 训练（P4）。

[Title]: DeepCritic: Deliberate Critique with Large Language Models
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: 4.5K long-form critiques (seed data from Qwen2.5-72B) + PRM800K / auto-annotated data
- [Target Experience]: DeepCritic (deliberate step-wise critique model) weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}, {human}
- [Utilization]: 帮助 LLM generator 通过 detailed feedback 修正错误 reasoning steps
- [Method]: ⟨SFT⟩, ⟨RL: GRPO⟩
- [Mechanism]: 两阶段：(1) Qwen2.5-72B 生成 4.5K deliberate step-wise critiques（含 multi-perspective verifications + in-depth critiques of initial critiques）做 SFT；(2) 在 PRM800K human-labeled data 或 auto-annotated data（Monte Carlo sampling-based correctness estimation）上做 RL 进一步增强 critique ability。DeepCritic 在 error identification benchmarks 上显著超越 DeepSeek-R1-distill 和 GPT-4o。

[Title]: Policy Improvement using Language Feedback Models
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Visual trajectories verbalized to language descriptions + LLM feedback
- [Target Experience]: Language Feedback Model (LFM) weights
- [Source Modality]: [vis+txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: 识别 desirable behaviour 用于 imitation learning
- [Method]: ⟨SFT⟩
- [Mechanism]: 将 visual trajectories 转化为 language descriptions，query LLM 获取 feedback on behaviour desirability。LFM 从 LLM feedback 学习识别哪些行为是 desirable，用作 imitation learning 中的 behaviour selection signal。LFM 泛化到 unseen environments (+3.5-12.0%)，并支持 human-interpretable feedback。

[Title]: AURORA: Automated Training Framework of Universal Process Reward Models via Ensemble Prompting and Reverse Verification
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Diverse LLM reasoning processes with ensemble prompting annotations + reverse verification signals
- [Target Experience]: Universal PRM weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: 在推理时对 reasoning processes 做 step-level evaluation
- [Method]: ⟨SFT⟩
- [Mechanism]: 两阶段：(1) 使用 diverse prompting strategies 和 ensemble methods 做 automated annotation and evaluation of reasoning processes，确保 robust assessments；(2) 利用 practical reference answers 做 reverse verification，增强模型验证输出和 training accuracy。提出 UniversalBench 评估 PRM 在 diverse policy distributions 和 long-CoT 下的表现。

[Title]: Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training
- [Pathway]: Narrative → Narrative (P1) / 整体含 Policy → Narrative → Policy 的自生成闭环
- [Source Experience]: Agent interaction trajectories in interactive environments
- [Target Experience]: Error correction / reflection capability (refined narratives) in policy weights via self-training
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在 rollout 过程中及时识别和修正错误 actions
- [Method]: ⟨MCTS⟩, ⟨SFT⟩
- [Mechanism]: Agent-R 通过 MCTS 构建训练数据，从错误 trajectories 恢复正确路径。Model-guided critique construction：actor model 识别 failed trajectory 中第一个错误步骤，splice with adjacent correct path（共享 same parent node in tree），生成 reflection training data。Iterative self-training 持续改善 error correction 和 dataset construction。本质是将 raw failed trajectories → correct recovery trajectories 的 P1 转化，再通过 SFT 内化为 policy 能力（P5）。整体构成 §8.1 闭环。

[Title]: SPARK: Stepwise Process-Aware Rewards for Reference-Free Reinforcement Learning
- [Pathway]: Narrative → Evaluator → Policy (P4 + P6, §8.2)
- [Source Experience]: Generator-produced diverse solutions with verifier evaluations (self-consistency + meta-critique)
- [Target Experience]: Generative PRM weights (stage 2) + Policy weights (stage 3)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: PRM-CoT 作为 reward model 在 RL 训练中提供 step-level rewards；final policy 在 math reasoning benchmarks 上取得 47.4% average accuracy
- [Method]: ⟨LLM-extract⟩, ⟨SFT⟩, ⟨RL: GRPO⟩
- [Mechanism]: 三阶段：(1) Generator 生成 diverse solutions，verifier 通过 parallel scaling (self-consistency) + sequential scaling (meta-critique) 评估；(2) 用 verification outputs 作为 synthetic training data fine-tune generative PRM（P4: Narrative → Evaluator）；(3) 用 PRM-CoT 作为 reward model 做 RL training of policy（P6: Evaluator → Policy），引入 format constraints 防 reward hacking。不依赖 ground truth references，aggregated verifications 超越 ground-truth outcome supervision 质量。

[Title]: VerIF: Verification Engineering for Reinforcement Learning in Instruction Following
- [Pathway]: Out of Scope
- [Mechanism]: 排除理由：本文在通用 instruction-following 任务上探索 RLVR 的 verification engineering（rule-based code verification + LLM-based verification），VerInstruct 数据集包含 ~22K 通用指令实例。源任务为 instruction following（通用 LLM 输出对齐），非 Agent 在异构动作空间中的序贯决策经验，不满足 §3.1 纳入标准。

[Title]: Self-Taught Evaluators
- [Pathway]: Out of Scope
- [Mechanism]: 排除理由：源经验为 unlabeled instructions（通用自然语言指令），通过 self-generated contrasting outputs 训练 LLM-as-a-Judge。该 Evaluator 面向通用 LLM 输出质量评估（RewardBench），指令本身不携带 Agent 决策过程语义，source 非 Agent 序贯决策经验。尽管训练过程涉及 iterative self-improvement，但转化的内容不是 agent experience，不满足 §3.1 纳入标准。

[Title]: Training Language Models to Critique With Multi-agent Feedback
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Multi-agent aggregated critiques (MultiCritiqueDataset) + multi-agent feedback on critique quality
- [Target Experience]: Critique-augmented LLM (7B) weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: 作为 critic model 评估和 critique 其他 model outputs
- [Method]: ⟨SFT⟩, ⟨RL: DPO⟩
- [Mechanism]: (1) MultiCritique SFT 阶段：从多个 agent 聚合高质量 critiques（而非 single model），以 crucial information 作为输入简化 critique 任务；(2) RL 阶段：通过 multi-agent feedback 提升 critique quality 的 preference accuracy，用 DPO 优化。7B model 显著超越其他 7B-13B open-source models，接近 70B 和 GPT-4 水平。

[Title]: VARP: Reinforcement Learning from Vision-Language Model Feedback with Agent Regularized Preferences
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Robot trajectory sketches overlaid on final observations + VLM preference labels
- [Target Experience]: Agent-regularized reward model weights
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}
- [Utilization]: 作为 reward model 为 continuous-control robotics RL 提供 preference-based rewards
- [Method]: ⟨SFT⟩
- [Mechanism]: 两部分贡献：(1) 通过 overlay trajectory sketches on final observations 展示 robot motion path，使 VLM 能提供更准确的 preferences（+15-20% accuracy）；(2) agent-regularized reward learning：在 reward model 优化中 incorporate agent's performance data，确保 reward model 基于 current policy 生成的数据优化。在 MetaWorld 任务上达到 70-80% success rate。

[Title]: Generative Reward Models
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: LLM-generated outputs with self-generated reasoning traces and synthetic preference labels
- [Target Experience]: GenRM (generative reward model) weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 作为 reward model 在 RLHF/RLAIF 流程中提供 synthetic preference labels
- [Method]: ⟨SFT⟩
- [Mechanism]: GenRM 迭代训练 LLM 在 self-generated reasoning traces 上，产生与 human preference judgments 一致的 synthetic preference labels。GenRM 在 in-distribution 上达到 Bradley-Terry RM 精度，在 out-of-distribution 上显著超越（10-45%）。Unify RLHF 和 RLAIF 的优势：利用 RLAIF 的 scalability + RLHF 的 alignment quality。

[Title]: LLM Critics Help Catch LLM Bugs
- [Pathway]: Out of Scope
- [Mechanism]: 排除理由：训练 LLM critics 检测 model-written code 中的 bugs，源经验为通用代码质量评估数据（ChatGPT training data 中的代码）。该 critic 面向代码 review 场景，code generation/evaluation 为单步任务，非 Agent 在异构动作空间中的序贯决策经验，不满足 §3.1 纳入标准。

[Title]: Recursive Introspection: Teaching Language Model Agents How to Self-Improve
- [Pathway]: Annotation Failed
- [Mechanism]: Abstract 为空，无法识别源经验形式、转化机制和目标载体。仅从标题推断涉及 self-improvement 和 introspection，但缺乏具体内容无法标注。

[Title]: Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision
- [Pathway]: Narrative → Schematic → Evaluator → Policy (P2 + P4 + P5/P6)
- [Source Experience]: Symbolic reasoning trajectories with pseudo-labels via MC estimation
- [Target Experience]: PRM weights + improved policy weights (via DPO + SFT on selected trajectories)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: PRM 用于选择高质量 symbolic trajectories；selected trajectories 再通过 DPO/SFT 训练 policy
- [Method]: ⟨MCTS⟩, ⟨SFT⟩, ⟨RL: DPO⟩
- [Mechanism]: (1) MC estimation 合成带 stepwise pseudo-labels 的 symbolic reasoning trajectories（Narrative → Schematic: 将自然语言推理形式化为 symbolic representation，P2）；(2) 在 synthesized data 上训练 PRM（Narrative → Evaluator, P4）；(3) PRM 筛选高质量 symbolic trajectories，用 selected trajectories 做 DPO + SFT 训练（Evaluator → Policy, P6 + Narrative → Policy, P5）。整体为 P2+P4+P6 复合链路。

[Title]: RM-RF: Reward Model for Run-Free Unit Test Evaluation
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Source code + test code with execution-derived labels (compile/run success, coverage, mutation kill rate)
- [Target Experience]: RM-RF (lightweight reward model) weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 预测 generated unit tests 的 execution-derived signals，无需实际编译执行
- [Method]: ⟨SFT⟩
- [Mechanism]: 从 multilingual dataset (Java, Python, Go) 中提取 source code + test code pairs，用 execution-based pipeline 标注三个 execution-derived signals。训练 RM-RF 从 source + test code 直接预测这三项指标，替代 compile-and-run 的 latency 和 infrastructure cost。Average F1 of 0.69 across three targets。注意：本文涉及的是 code/test evaluation 而非 agent trajectory evaluation，但单元测试的验证属于工具性评估，action 为 test generation，可视为 agentic。

[Title]: I-FailSense: Towards General Robotic Failure Detection with Vision-Language Models
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Robotic manipulation trajectories with semantic misalignment failure annotations
- [Target Experience]: I-FailSense (post-trained VLM + FS blocks) failure detector weights
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 检测 robot 执行中的 semantic misalignment errors（robot 执行了语义合理但与指令不一致的任务）
- [Method]: ⟨SFT⟩
- [Mechanism]: 构建 Semantic Misalignment Failures 检测数据集（从现有 language-conditioned manipulation datasets）。Post-train base VLM，在其不同 internal layers 上训练轻量 FS blocks (classification heads)，通过 ensembling mechanism 聚合预测。尽管仅训练在 semantic misalignment detection 上，泛化到 broader robotic failure categories。

[Title]: Training Turn-by-Turn Verifiers for Dialogue Tutoring Agents: The Curious Case of LLMs as Your Coding Tutors
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Coding tutoring dialogue trajectories with student knowledge tracing and turn-by-turn verification
- [Target Experience]: Turn-by-turn verifier (within TRAVER workflow) weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: 在每个 tutoring turn 验证 guidance 有效性，确保 student 向 task completion 前进
- [Method]: ⟨SFT⟩
- [Mechanism]: TRAVER 工作流包含 knowledge tracing（估计 student knowledge state）+ turn-by-turn verification（确保每步 guidance 有效）。Verifier 评估 tutor agent 的每步 guidance 是否有效引导 student 完成 coding task。DICT 评估协议使用 controlled student simulation 和 code generation tests 自动评估。

[Title]: Joint Verification and Refinement of Language Models for Safety-Constrained Planning
- [Pathway]: Narrative → Schematic → Policy (P2 + P5)
- [Source Experience]: Generated robot programs (Python) with automaton-based verification results
- [Target Experience]: Verified-safe policy weights (fine-tuned to generate specification-compliant sub-components)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 验证生成的 robot programs 是否符合 safety specifications；verification outcomes 作为 fine-tuning supervision
- [Method]: ⟨SFT⟩
- [Mechanism]: 将生成的 robot programs 转化为 automaton-based representation，验证是否符合 safety specifications。定理证明：任意 verified sub-components 的组合仍满足 safety。利用 verification outcomes 作为 supervision fine-tune model 生成 safe sub-components（而非 full programs），提升训练效率（+30% specification-compliant，训练时间减半）。

[Title]: Tool Verification for Test-Time Reinforcement Learning
- [Pathway]: Evaluator → Policy (P6 variant: tool-verified reward → policy via test-time RL)
- [Source Experience]: Unlabeled test inputs with tool-verified pseudo-labels (code execution results)
- [Target Experience]: Improved policy weights via test-time RL (T^3RL)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在 test-time 通过 verified pseudo-labels 做 RL self-evolution
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: T^3RL 在 TTRL 基础上引入 test-time tool verification：verifier 使用 external tool evidence (e.g., code execution) 在 verification-aware voting 中 upweight verified rollouts，产生更可靠的 pseudo-labels。本质上是用 tool-based evaluator（规则化，非 V-Par 权重）提供 verified reward signal 做 policy RL。属于 P6 变体（Evaluator 为规则/tool-based 而非参数化 V-Par）。

[Title]: P-Check: Advancing Personalized Reward Model via Learning to Generate Dynamic Checklist
- [Pathway]: Out of Scope
- [Mechanism]: 排除理由：源经验为 user interaction history 用于个性化偏好建模，训练 checklist generator 辅助 reward prediction。核心贡献在个性化 reward modeling 的用户偏好适配，源数据为通用用户交互历史而非 Agent 在异构动作空间中的序贯决策经验，不满足 §3.1 纳入标准。

[Title]: JudgeLRM: Large Reasoning Models as a Judge
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Evaluation task data with judge-wise outcome-driven rewards
- [Target Experience]: JudgeLRM (judgment-oriented LLM) weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {human}
- [Utilization]: 作为 LLM judge 替代 human annotation，在复杂推理任务上做 evaluation
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 用 judge-wise outcome-driven rewards 做 RL training 激活 LLM 的 reasoning capabilities for judgment。JudgeLRM 超越 SFT-tuned baselines 和 state-of-the-art reasoning models（JudgeLRM-7B/8B outperforms DeepSeek-R1 by >2% F1）。观察到 SFT performance gains 与 reasoning-demanding sample proportion 负相关，说明 RL 在 reasoning-intensive judgment 上不可替代。

[Title]: Asymmetric Actor-Critic for Multi-turn LLM Agents
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Multi-turn agent interaction trajectories with automatically generated supervision signals
- [Target Experience]: Lightweight open-source critic weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: 在 runtime 监督 actor (proprietary LLM) 的 actions，在同一 interaction trajectory 内 intervene
- [Method]: ⟨SFT⟩
- [Mechanism]: 利用 generation-verification asymmetry（高质量生成需大模型，有效监督可用小模型）：powerful proprietary LLM 作为 actor，smaller open-source critic 提供 runtime supervision。Data generation pipeline 在不修改 actor 的情况下产生 supervision signals 用于 critic fine-tuning。Lightweight critics rival or surpass larger proprietary models in critic role。

[Title]: Hybrid Reward Normalization for Process-supervised Non-verifiable Agentic Tasks
- [Pathway]: Narrative → Evaluator → Policy (P4 + P6, §8.2)
- [Source Experience]: Agentic task trajectories with principle-based step-level assessments + outcome verification
- [Target Experience]: Principle Process Reward model weights + RL-trained policy weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 为 non-verifiable agentic tasks（无 golden answers）提供 process reward + outcome reward
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: PPR (Principle Process Reward) 训练 principle-based reward model 改善 process evaluation 的 transparency 和 reliability（P4）。Reward Normalization (ReNorm) 策略校准 outcome 和 process rewards 的平衡，解决 process reward 优化可能与 final outcome 不一致的问题。用 calibrated reward 做 RL training（P6）。

[Title]: Self-critiquing models for assisting human evaluators
- [Pathway]: Out of Scope
- [Mechanism]: 排除理由：源经验为 topic-based summarization 任务的 summaries + human flaw annotations。Summarization 为单步文本生成任务，非 Agent 在异构动作空间中的序贯决策过程。尽管 self-critique + refine 构成 sequential self-improvement，但底层任务缺乏异构动作空间（action 仅为 generate summary），不满足 §3.1 纳入标准。

[Title]: VLP: Vision-Language Preference Learning for Embodied Manipulation
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Embodied manipulation trajectories with language-conditioned preferences (3 types, no human annotations)
- [Target Experience]: Vision-Language Preference model weights
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 作为 preference annotator 为 downstream tasks 提供 preference feedback（用于 reward learning 或 direct policy optimization）
- [Method]: ⟨SFT⟩
- [Mechanism]: 定义三种 language-conditioned preferences，构建 vision-language preference dataset（含 versatile implicit preference orders，无 human annotations）。Preference model 学习提取 language-related features 并作为 preference annotator 服务 downstream RL tasks（通过 reward learning 或 direct policy optimization）。

[Title]: Real-Time Verification of Embodied Reasoning for Generative Skill Acquisition
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Embodied skill learning trajectories with automatically synthesized dense reward signals
- [Target Experience]: VERGSA verification model weights
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 在 generative skill acquisition 过程中提供 real-time verification 和 dense reward signals
- [Method]: ⟨SFT⟩
- [Mechanism]: 将 mathematical reasoning verification 的理念扩展到 embodied learning：(1) 动态将 contextually relevant tasks 纳入 prompts 并定义 subtask 和 overall task 的 success metrics；(2) automated scalable reward labeling scheme 迭代确定 scene configuration 和 subtask learning 对整体 skill acquisition 的 contribution。构建首个 verification-driven generative skill acquisition training dataset。

[Title]: RL4F: Generating Natural Language Feedback with Reinforcement Learning for Repairing Model Outputs
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Model outputs (action planning, summarization, alphabetization) with end-task performance as reward
- [Target Experience]: RL4F critique generator weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 为 black-box/fixed model (GPT-3) 提供 natural language feedback 帮助其 repair outputs
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: Multi-agent collaborative framework：critique generator 通过 RL 训练，目标最大化 fixed GPT-3 的 end-task performance（critique 帮助 GPT-3 revise outputs 后的实际改善程度作为 reward）。Critique generator 是 GPT-3 大小的 1/200+，无需 fine-tune target model。

[Title]: Learning LLM-as-a-Judge for Preference Alignment
- [Pathway]: Annotation Failed
- [Mechanism]: Abstract 为空，无法从论文摘要识别源经验形式、转化机制和目标载体。标题涉及 LLM-as-a-Judge 和 Preference Alignment，暗示可能涉及 Evaluator 训练（P4）或 Evaluator→Policy alignment（P6），但缺乏具体内容无法确认。

[Title]: LLaVA-Critic-R1: Your Critic Model is Secretly a Strong Policy Model
- [Pathway]: Narrative → Evaluator (P4) / 且 critic 同时具备 Policy → Narrative (P7) 的 self-critique 能力
- [Source Experience]: Preference-labeled critic datasets (reorganized into verifiable training signals)
- [Target Experience]: LLaVA-Critic-R1 (unified multimodal critic + policy model) weights
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {self}, {human}
- [Utilization]: 作为 critic 评估 multimodal outputs；作为 policy model 直接生成 responses；test-time self-critique 提升 reasoning performance (+13.8%)
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 将 preference-labeled critic datasets 重组为 verifiable training signals，直接在 base generative model 上做 RL training。结果涌现出双向能力：LLaVA-Critic-R1 既是 top-performing critic 又是 competitive policy model。Test-time self-critique（policy 评估自己的输出并修正）进一步提升 reasoning，对应 Policy → Narrative (critique) → Policy (refined) 的闭环。

[Title]: HyperClick: Advancing Reliable GUI Grounding via Uncertainty Calibration
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: GUI grounding predictions with correctness labels and confidence calibration data
- [Target Experience]: GUI grounding model with calibrated confidence (introspective self-criticism) weights
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 在 GUI automation 中提供 well-calibrated confidence estimates，减少 overconfidence 导致的错误
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: HyperClick 引入 dual reward mechanism：binary reward for correct actions + truncated Gaussian-based spatial confidence modeling (calibrated by Brier score)。Jointly optimizes grounding accuracy 和 confidence reliability，培养 introspective self-criticism。核心是将 confidence calibration 作为 evaluator 能力融入 grounding model。

[Title]: Tapered Off-Policy REINFORCE: Stable and efficient reinforcement learning for LLMs
- [Pathway]: Narrative → Evaluator (P4) / Narrative → Policy (P5)
- [Source Experience]: LLM reasoning solutions (GSM8K, MATH) with positive and negative examples
- [Target Experience]: Improved policy weights (solution generation) + generative verifier weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 同时训练 solution generator 和 generative verifier
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: TOPR (Tapered Off-Policy REINFORCE) 使用 asymmetric tapered importance sampling 在 off-policy regime 中统一处理 positive 和 negative examples。同时应用于训练 solution generation model（P5）和 generative verifier（P4）。发现 REINFORCE baseline parameter 在 defining dataset composition 中起关键作用。

[Title]: SafePred: A Predictive Guardrail for Computer-Using Agents via World Models
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: CUA interaction trajectories with safety policies and world model predictions
- [Target Experience]: World model + safety guardrail (SafePred) weights
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {human}
- [Utilization]: 预测 short-term 和 long-term risks，在 action 执行前 prune 高风险 actions
- [Method]: ⟨SFT⟩
- [Mechanism]: SafePred 建立 risk-to-decision loop：(1) world model 基于 safety policies 预测 short- 和 long-term risks，生成 semantic risk representations，识别 leading to high-risk states 的 actions；(2) decision optimization 通过 step-level interventions 和 task-level re-planning 将 predicted risks 转化为 actionable safe decision guidances。超过 97.6% safety performance。

[Title]: Evaluating Judges as Evaluators: The JETTS Benchmark of LLM-as-Judges as Test-Time Scaling Evaluators
- [Pathway]: Not a transformation paper — benchmark/evaluation resource
- [Mechanism]: JETTS 是 benchmark paper，评估 judge models 在 test-time scaling 设置下（response reranking, step-level beam search, critique-based response refinement）的表现。覆盖 math reasoning, code generation, instruction following 三个 domain。发现 judges 在 reranking 上 competitive with ORMs，但在 beam search 上 consistently worse than PRMs；natural language critiques currently ineffective for guiding generators。不涉及 experience transformation 机制。

[Title]: J4R: Learning to Judge with Equivalent Initial State Group Relative Policy Optimization
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Reasoning task evaluation data (ReasoningJudgeBench)
- [Target Experience]: J4R (7B judge trained with EIS-GRPO) weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {human}
- [Utilization]: 作为 LLM judge 在 reasoning-intensive domains 评估 model outputs
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 提出 EIS-GRPO (Equivalent Initial State GRPO) 算法训练 judge model，使其对 positional biases 鲁棒（evaluation 中 candidate order 的影响）。J4R-7B 超越 GPT-4o 和 larger GRPO-trained judges on JudgeBench 和 ReasoningJudgeBench。核心贡献在 judge 训练的 RL 算法改进。

[Title]: Reward Modeling from Natural Language Human Feedback
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: LLM-generated critiques + human natural language critiques (with similarity as reward)
- [Target Experience]: GRM (Generative Reward Model) weights + MetaRM weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}, {self}
- [Utilization]: 提供 process reward signals 替代 outcome-only binary supervision
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: RM-NLHF 利用 natural language human feedback 产生 process reward signals：计算 GRM-generated critiques 与 human critiques 的 similarity 作为训练 reward（比 binary outcome-only supervision 更准确）。MetaRM 从有 human critiques 的数据学习预测 process reward，再泛化到无 human critiques 的数据，解决 human critiques 不可规模化的问题。

[Title]: Agent-RewardBench: Towards a Unified Benchmark for Reward Modeling across Perception, Planning, and Safety in Real-World Multimodal Agents
- [Pathway]: Annotation Failed
- [Mechanism]: Abstract 为空，无法识别具体方法、转化机制和载体。标题表明是 reward modeling benchmark paper（覆盖 perception, planning, safety），但缺乏 Abstract 内容无法标注。

[Title]: Scaling Reward Modeling without Human Supervision
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Document prefixes and suffixes from large-scale web corpora (11M tokens math-focused web data)
- [Target Experience]: Unsupervised reward model weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: best-of-N selection 和 policy optimization（改善 downstream math performance）
- [Method]: ⟨SFT⟩
- [Mechanism]: Reward-based scaling (RBS)：从 web corpora 的 document prefixes 和 suffixes 进行 preference learning，完全无 human annotations。11M tokens 的 math-focused web data 训练即可在 RewardBench v1/v2 上 steady gains（+7.7 points average on v2, +16.1 on in-domain math）。RM 应用于 best-of-N selection 和 policy optimization，match or exceed supervised RM baselines。

[Title]: Evaluating Robustness of Reward Models for Mathematical Reasoning
- [Pathway]: Not a transformation paper — evaluation benchmark
- [Mechanism]: 本文为 reward model evaluation benchmark paper。发现 RewardBench 的 math subset 在 chosen/rejected completions 之间存在 representation difference 且依赖单一比较，导致 unreliable results。提出 RewardMATH benchmark 更可靠地评估 reward model robustness，发现 RewardMATH scores 与 optimized policy results 强相关（RewardBench 则几乎无相关性）。不涉及 experience transformation 机制。

[Title]: LIV: Language-Image Representations and Rewards for Robotic Control
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Action-free human videos with text annotations (EpicKitchen) + robot videos
- [Target Experience]: LIV model (vision-language representation + universal value function) weights
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {human}
- [Utilization]: 为 unseen robots/humans 的每一帧分配 dense rewards（给定 language or image goal）；作为 representation 用于 imitation learning 和 reward specification
- [Method]: ⟨SFT⟩
- [Mechanism]: LIV objective 基于 dual RL 和 mutual information contrastive learning 的统一，训练 multi-modal representation 隐式编码 universal value function（对 language/image goals）。从 large human video datasets (EpicKitchen) 预训练，可在 unseen environments 中为每帧分配 dense rewards。

[Title]: Real-World Offline Reinforcement Learning from Vision Language Model Feedback
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Offline robot datasets (sub-optimal, unlabeled) with VLM preference feedback
- [Target Experience]: Learned reward function weights + offline RL-trained dressing policy weights
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}
- [Utilization]: 为 offline RL 提供自动生成的 reward labels；训练 robot-assisted dressing policy
- [Method]: ⟨SFT⟩
- [Mechanism]: 基于 RL-VLM-F，使用 VLM 对 sub-optimal offline dataset 生成 preference feedback，学习 reward function。随后用 learned reward 做 Implicit Q-learning (offline RL) 训练 dressing policy。在 simulation 和 real-world robot-assisted dressing 任务上验证。

[Title]: Learning and Leveraging Verifiers to Improve Planning Capabilities of Pre-trained Language Models
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Planning action sequences (Blocksworld) with validity labels (valid/invalid in state)
- [Target Experience]: Verifier weights (classifying action validity in a given state)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在推理时 prune invalid trajectories（由 generator 随机采样产生）
- [Method]: ⟨SFT⟩
- [Mechanism]: 从 planning dataset 随机采样 actions 生成 invalid action examples，训练 verifier 分类 action 在特定 state 中是否 valid。部署时 generator 随机采样 diverse actions，verifier prune invalid trajectories，显著提升 Blocksworld 成功率。发现 fine-tuning GPT-2 generator 自身作为 verifier 比 fine-tuning base GPT-2 泛化更好。

[Title]: Interpretable Preferences via Multi-Objective Reward Modeling and Mixture-of-Experts
- [Pathway]: Out of Scope
- [Mechanism]: 排除理由：源经验为 multi-dimensional absolute-rating data（honesty, verbosity, safety 等通用对齐维度的人类评分），训练多目标 RM 用于通用 LLM alignment。评分数据来自静态人类判断，非 Agent 在异构动作空间中的序贯决策经验，不满足 §3.1 纳入标准。

[Title]: Generative Judge for Evaluating Alignment
- [Pathway]: Out of Scope
- [Mechanism]: 排除理由：Auto-J 在通用 user queries + LLM-generated responses 上训练，作为通用 generative evaluator 评估 LLM 输出对齐质量。源数据为静态用户查询-模型响应对，非 Agent 在异构动作空间中的序贯决策经验，不满足 §3.1 纳入标准。

[Title]: Improve LLM-as-a-Judge Ability as a General Ability
- [Pathway]: Out of Scope
- [Mechanism]: 排除理由：将 judge ability 作为 LLM 通用能力训练（SFT warm-up + DPO enhancement），合成 judgmental content 用于通用 judge 模型训练。源数据非 Agent 序贯决策经验，属于通用 LLM evaluation 基础设施，不满足 §3.1 纳入标准。

[Title]: S2J: Bridging the Gap Between Solving and Judging Ability in Generative Reward Models
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: GRM outputs with both solving and judging supervision on the same queries
- [Target Experience]: S2J-enhanced GRM weights (narrowed solve-to-judge gap)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 作为 generative reward model 同时具备 strong solving 和 judging capabilities
- [Method]: ⟨SFT⟩
- [Mechanism]: 首次识别 solve-to-judge gap（GRM 能 solve 某 query 但无法正确 judge 它，14%-37% queries 存在此现象）。S2J 同时 leverage solving 和 judging capabilities on single GRM's output for supervision，在 model optimization 中显式连接 problem-solving 和 evaluation abilities。Reduce gap by 16.2%，judgment performance +5.8%，self-evolution 无需更强 external models。

[Title]: Bringing Value Models Back: Generative Critics for Value Modeling in LLM Reinforcement Learning
- [Pathway]: Narrative → Evaluator (P4) / 整体含 Evaluator → Policy (P6)
- [Source Experience]: LLM interaction rollouts with trajectory-level returns
- [Target Experience]: GenAC (Generative Actor-Critic) critic weights + policy weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Critic 提供 fine-grained advantage estimation 改善 policy RL training 中的 credit assignment
- [Method]: ⟨SFT⟩, ⟨RL: GRPO⟩
- [Mechanism]: GenAC 将 one-shot scalar value prediction 替换为 generative critic（CoT reasoning → value estimate），提升 value function 的 expressiveness。In-Context Conditioning 使 critic 在整个 training 中保持 calibrated to current actor。GenAC 在 value approximation, ranking reliability, OOD generalization 上均超越 value-based 和 value-free baselines，转化为更强的 downstream RL performance。

[Title]: Multimodal Reinforcement Learning with Agentic Verifier for AI Agents
- [Pathway]: Narrative → Evaluator (P4) / 整体含 Evaluator → Policy
- [Source Experience]: Multimodal agent interaction trajectories (spatial reasoning, visual hallucination, robotics)
- [Target Experience]: Argos agentic verifier weights + multimodal reasoning policy weights
- [Source Modality]: [cross-modal]
- [Target Modality]: [cross-modal]
- [Experience Source]: {self}
- [Utilization]: 为 SFT data curation 和 RL training 提供 multi-objective reward（response accuracy + spatiotemporal localization + reasoning quality）
- [Method]: ⟨SFT⟩, ⟨RL: GRPO⟩
- [Mechanism]: Argos 为每个 sample 从 pools of teacher-model derived + rule-based scoring functions 中选择合适的评估函数，同时评估三个维度。Agentic verifier 跨 SFT data curation 和 RL training 两阶段使用。Pareto-optimality 理论上 justification。发现仅靠 SFT on curated reasoning data 不足，无 online verification 时 agents collapse to ungrounded solutions。核心为 P4+P6 composite + multi-objective evaluation。

[Title]: AutoGLM: Autonomous Foundation Agents for GUIs
- [Pathway]: Narrative → Policy (P5) / 整体含 Policy → Narrative → Policy 自生成闭环
- [Source Experience]: GUI interaction trajectories from online curriculum RL
- [Target Experience]: AutoGLM policy weights
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 直接执行 GUI 操作（web browsing + Android device control）
- [Method]: ⟨SFT⟩, ⟨RL: GRPO⟩
- [Mechanism]: AutoGLM 核心贡献在：(1) "intermediate interface" 设计分离 planning 和 grounding behaviors；(2) progressive training framework 实现 self-evolving online curriculum RL。Self-evolving 涉及 policy rollout → 数据收集 → RL training 的循环（Policy → Narrative → Policy，§8.1 闭环）。虽然论文涉及 RM 在 RL 中的使用，但 Abstract 未详细描述 RM 训练机制，主贡献在 policy training pipeline。标注为 P5 主线，含 §8.1 闭环。

[Title]: Is Your LLM Secretly a World Model of the Internet? Model-Based Planning for Web Agents
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Web interaction trajectories with scalable data synthesis pipeline
- [Target Experience]: Dreamer-7B (specialized world model + value function) weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 作为 world model 模拟每个 candidate action 的 outcome；作为 value function 评估 states
- [Method]: ⟨SFT⟩
- [Mechanism]: WebDreamer 训练 specialized LLM 作为 world model：在采取 action 前模拟和 deliberating 每个 candidate action 的 outcome。World model 同时充当 value function 评估 states。通过 scalable data synthesis pipeline 训练 Dreamer-7B，性能与 GPT-4o 相当。本质将 LLM 训练为 evaluator（预测 action outcome + state value），属于 P4。区别于 typical PRM 的是其 world model framing。

[Title]: Constitutional AI: Harmlessness from AI Feedback
- [Pathway]: Narrative → Evaluator → Policy (P4 + P6, §8.2)
- [Source Experience]: Self-generated critiques and revisions (SL phase) + AI preference dataset (RL phase)
- [Target Experience]: Preference model (RM) weights + harmless policy weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Preference model 作为 reward signal 在 RLAIF 中训练 harmless policy
- [Method]: ⟨SFT⟩, ⟨RL: PPO⟩
- [Mechanism]: 两阶段：(1) SL phase: initial model 采样 → self-critique and revise → fine-tune on revised responses（Narrative → Narrative, P1）；(2) RL phase: fine-tuned model 采样 → AI model 评估偏好 → 训练 preference model（Narrative → Evaluator, P4）→ 用 preference model 作为 reward signal 做 RL training（Evaluator → Policy, P6）。整体为 P1 + P4 + P6 的 composite pipeline。Constitution/rules 仅作为人类监督的替代形式（a list of principles），不参与 transformation 核心机制。

[Title]: RewardBench: Evaluating Reward Models for Language Modeling
- [Pathway]: Not a transformation paper — benchmark resource
- [Mechanism]: 本文为 reward model evaluation benchmark paper。提出 RewardBench dataset（prompt-chosen-rejected trios spanning chat, reasoning, safety）用于评估 reward models 的性能。对多种 RM training methods（direct MLE, DPO implicit RM）做系统评估。不涉及 experience transformation 机制。

[Title]: RLAC: Reinforcement Learning with Adversarial Critic for Free-Form Generation Tasks
- [Pathway]: Narrative → Evaluator → Policy (P4 + P6, §8.2) / 含 adversarial co-evolution
- [Source Experience]: Free-form generation outputs with dynamically identified failure modes + external validator results
- [Target Experience]: Adversarial critic weights + generator policy weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Critic 动态识别最可能的 failure modes；generator 优化后减少 errors；external validator 提供 verification
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: RLAC 中 critic (LLM) 动态识别最可能的 failure modes，external validator 验证这些 modes。Generator 和 critic 通过 adversarial game 联合优化：critic 学习检测更多 errors，generator 学习产生更少 errors。Dynamic critics 比 fixed critics 更有效。整体为 P4（critic 训练）+ P6（critic-guided generator training）的 adversarial co-evolution。

[Title]: RLHF Workflow: From Reward Modeling to Online RLHF
- [Pathway]: Out of Scope
- [Mechanism]: 排除理由：本文为 online iterative RLHF 的技术报告/recipe，使用 open-source preference datasets 构建 proxy preference model 并做 online RLHF。源数据为通用 LLM 偏好数据（AlpacaEval-2、Arena-Hard、MT-Bench 等 chatbot benchmarks），非 Agent 在异构动作空间中的序贯决策经验。尽管 RLHF workflow 的 pipeline 结构与 P4+P6 同构，但转化对象不是 agent experience，不满足 §3.1 纳入标准。

[Title]: Zero-Shot Reward Specification via Grounded Natural Language
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Goal text descriptions + raw pixel observations with CLIP-based reward signals
- [Target Experience]: Learned task policy weights (via CLIP-generated rewards) + distilled goal-conditioned policy
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}
- [Utilization]: CLIP 生成 task reward signal 用于学习 policy；distilled policy 在 zero-shot 下泛化到新任务
- [Method]: ⟨SFT⟩
- [Mechanism]: 使用 CLIP (visuolanguage model) 从 goal text description 和 raw pixel observations 生成 task reward signal（无需 true state 或 expert demonstrations）。Reward signal 用于 policy learning。最后将 individual task policies 蒸馏为 single goal-conditioned policy 实现 zero-shot generalization。核心转化是 VLM 的 visual-language alignment → reward signal（用于 policy training）。

## New Tags Introduced
- ⟨RL: adversarial imitation⟩ —— 对失败 action 做 adversarial imitation learning，作为 GRPO 的补充训练策略，既有 ⟨SFT⟩ 的模仿属性又有 ⟨RL⟩ 的对抗属性，现有标签不足以精确刻画；首次出现：「SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from Experience」

## Out of Scope Papers
以下论文经复核后判定不满足 §3.1 纳入标准，已标为 `[Pathway]: Out of Scope`（排除理由在各篇 [Mechanism] 中详述）：

- 「Critique-out-Loud Reward Models」—— 通用 RLHF RM，源数据为静态人类偏好对
- 「Improving Reward Models with Synthetic Critiques」—— 通用 RM 训练，源为人类偏好评分
- 「Self-Taught Evaluators」—— 通用 unlabeled instructions 训练 LLM-as-a-Judge
- 「Interpretable Preferences via Multi-Objective Reward Modeling (ArmoRM)」—— 通用多目标 RM
- 「Generative Judge for Evaluating Alignment (Auto-J)」—— 通用 LLM 输出评估器
- 「Improve LLM-as-a-Judge Ability as a General Ability」—— 通用 judge 训练
- 「P-Check: Advancing Personalized Reward Model」—— 个性化 RM，用户偏好数据
- 「Self-critiquing models for assisting human evaluators」—— summarization 任务，单步生成
- 「LLM Critics Help Catch LLM Bugs」—— 通用代码 review critic
- 「RLHF Workflow: From Reward Modeling to Online RLHF」—— 通用 RLHF recipe
- 「VerIF: Verification Engineering for RL in Instruction Following」—— 通用 instruction following
- 「CUARewardBench」—— benchmark 资源（非 transformation）
- 「Accurate Failure Prediction in Agents」—— empirical analysis（非 transformation）
- 「Evaluating Judges as Evaluators (JETTS)」—— benchmark 资源（非 transformation）
- 「Evaluating Robustness of Reward Models for Mathematical Reasoning」—— benchmark 资源（非 transformation）
- 「RewardBench: Evaluating Reward Models for Language Modeling」—— benchmark 资源（非 transformation）

## Annotation Failures
- 「Recursive Introspection: Teaching Language Model Agents How to Self-Improve」（block #87）—— Abstract 为空，无法识别源经验形式、转化机制和目标载体
- 「Learning LLM-as-a-Judge for Preference Alignment」（block #102）—— Abstract 为空，无法识别具体方法、转化机制和载体
- 「Agent-RewardBench: Towards a Unified Benchmark for Reward Modeling across Perception, Planning, and Safety in Real-World Multimodal Agents」（block #110）—— Abstract 为空，无法识别具体方法、转化机制和载体

## Parser Errors
（无）
