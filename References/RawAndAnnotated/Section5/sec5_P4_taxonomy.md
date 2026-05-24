
# Judge

- S2J: Bridging the Gap Between Solving and Judging Ability in Generative Reward Models
- 首次识别 solve-to-judge gap（GRM 能 solve 某 query 但无法正确 judge 它，14%-37% queries 存在此现象）。S2J 同时 leverage solving 和 judging capabilities on single GRM's output for supervision，在 model optimization 中显式连接 problem-solving 和 evaluation abilities。

- J4R: Learning to Judge with Equivalent Initial State Group Relative Policy Optimization
- 提出 EIS-GRPO (Equivalent Initial State GRPO) 算法训练 judge model，使其对 positional biases 鲁棒（evaluation 中 candidate order 的影响）

- I-FailSense: Towards General Robotic Failure Detection with Vision-Language Models
- 构建 Semantic Misalignment Failures 检测数据集（从现有 language-conditioned manipulation datasets）。Post-train base VLM，在其不同 internal layers 上训练轻量 FS blocks (classification heads)，通过 ensembling mechanism 聚合预测。

- Self-Refining Vision Language Model for Robotic Failure Detection and Reasoning
- 将 failure detection 和 reasoning 作为 multi-task self-refinement process：模型迭代预测 detection outcomes 和 natural language reasoning conditioned on past outputs。训练结合 offline 和 online imitation learning 处理 heterogeneous supervision。

- Towards Policy-Compliant Agents: Learning Efficient Guardrails For Policy Violation Detection
- 从 diverse agent runs 生成 broad set of policies 并标注 violation labels，构建 PolicyGuardBench。训练轻量 PolicyGuard-4B guardrail model 检测 agent trajectories 是否违反 policies。

- StepWiser: Stepwise Generative Judges for Wiser Reasoning
- 将 stepwise reward modeling 从 classification 重构为 reasoning task；StepWiser 在给出 verdict 前先产生 thinking tokens（meta-reasoning about the policy model's reasoning）。训练使用 rollout 的 relative outcomes 作为 RL reward signal，无需 step-level human annotations。

- AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation
- 我们引入AHA，一个开源VLM，旨在用自然语言检测和推理机器人操作中的失败。通过将失败检测构建为自由形式推理任务，AHA识别失败并跨不同机器人、任务和环境提供详细、可适应的解释。

- SAFE: Multitask Failure Detection for Vision-Language-Action Models
- 利用 VLA internal features（发现 VLA 对 task success/failure 已有 sufficient high-level knowledge）训练轻量 failure detector。SAFE 从 VLA 内部特征学习预测 single scalar indicating likelihood of task failure，无需额外环境交互。训练数据来自 VLA 的成功和失败 rollouts。


# World model

- Is Your LLM Secretly a World Model of the Internet? Model-Based Planning for Web Agents
- WebDreamer 训练 specialized LLM 作为 world model：在采取 action 前模拟和 deliberating 每个 candidate action 的 outcome。World model 同时充当 value function 评估 states。

- SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from Experience
- 多目标论文（同时产出 V-Par World State Model + π-Par agent policy + curriculum/task N-Tok）。Policy 在 novel software 中自主探索（P7 外化 trajectory）；World State Model 对 trajectory 做 step-wise assessment（P4）；policy 通过 adversarial imitation of failure actions + GRPO on successful ones 更新（P5）；Curriculum Generator 从简单到复杂生成新任务（Narrative→Narrative，P1）。specialist-to-generalist training 将多个 specialist agent 的经验整合为 generalist。多目标并列（§8.8），主轴按核心贡献标注为 P4（World State Model）+ P5（policy via GRPO）+ P7（trajectory generation）的复合。 


# ORM

- WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning
- 三组件协同：(1) self-evolving curriculum 从失败尝试生成新任务（P7 外化）；(2) 训练 ORM 提供 robust outcome-supervised reward（P4）；(3) adaptive RL strategies 用 ORM 信号训练 policy（P6）

- RL-VLM-F: Reinforcement Learning from Vision Language Foundation Model Feedback
- 查询 VLM 对 agent image observation pairs 给出 preferences（基于 task goal 的 text description），从 preference labels 学习 reward function（而非直接 prompt VLM 输出 raw reward score，避免噪声和不一致）。Learned reward function 然后用于 RL policy training。

# PRM

- Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision
- 我们引入PathFinder-PRM，一种新颖的分层、错误感知判别式PRM，首先在每个步骤分类数学错误和一致性错误，然后结合这些细粒度信号估计步骤正确性。



- SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents
-  从 SWE-Bench trajectories 构建 action-level reward dataset，训练 lightweight PRM 估计每个 intermediate action 的 usefulness。

- Process Reward Model with Q-Value Rankings
- 将 PRM 重构为 Markov Decision Process 框架下的 Q-value ranking 问题；PQM 使用 novel comparative loss function 优化 Q-value rankings，捕捉 sequential decisions 之间的 intricate dynamics。相比 classification-based PRM（cross-entropy loss 独立评估每步），PQM 更好地建模步骤间依赖关系。

- MagicGUI-RMS: A Multi-Agent Reward Model System for Self-Evolving GUI Agents via Automated Feedback Reflux
- 构建 structured data construction pipeline 自动生成 balanced and diverse reward datasets；训练 DS-RM（Domain-Specific RM）做 fine-grained action assessment + GP-RM（General-Purpose RM）做跨任务泛化。部署时 reward model system 识别错误 action 并提议修正，修正后的 trajectory 通过 data-reflux mechanism 回流至训练集，实现 self-evolving。整体形成 Policy → Narrative → Evaluator → Narrative(refined) → Policy 闭环，但主轴为 Evaluator 训练。

- Let's Verify Step by Step
- 收集 800K step-level human feedback labels（PRM800K），训练 PRM 对每个 intermediate reasoning step 给出 correctness score；通过 active learning 提升 process supervision 的数据效率。PRM 在 Best-of-N 等 test-time search 策略中为每一步提供细粒度评分。

- GUI-Shepherd: Reliable Process Reward and Verification for Long-Sequence GUI Tasks
- 在 52k GUI 交互轨迹上，利用 human-annotated scores 和 GPT-4o 生成的 rationale 作为监督信号，训练一个 Process Reward Model，使其能为 GUI agent 的每一步 action 提供 dense step-level feedback；Dataset:AndroidWorld

- Web-Shepherd: Advancing PRMs for Reinforcing Web Agents
- 构建 WebPRM Collection（40K step-level preference pairs + annotated checklists），以此为监督信号训练 Web-Shepherd PRM，使其能评估 web navigation 每一步的正确性与进展；训练好的 PRM 在推理时作为 verifier 对候选 trajectory 进行 step-level 评分与筛选。


- AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress
- web shopping and browser navigation
- 使用 Temporal Difference (TD) + Generalized Advantage Estimation (GAE) 自动标注 step-level labels，捕捉 sequential decisions 之间的 interdependence 和对 final goal 的 contribution；训练 PRM 同时建模每一步的 promise（离目标多远）和 progress（已取得多少进展），从而实现更好的 exploration-exploitation balance。


- WebArbiter: A Principle-Guided Reasoning Process Reward Model for Web Agents
- 两阶段训练：(1) reasoning distillation 阶段用 teacher model 的 principle-guided reasoning 做 SFT，使 PRM 具备结构化 justification 能力；(2) RL 阶段直接 align verdicts with correctness，纠正 teacher biases。PRM 以 text generation 形式输出 structured justification + preference verdict，比 scalar PRM 更具可解释性。

- Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning
- 核心 insight 是 process reward 应衡量 progress（step 前后产生正确 response 的 likelihood 变化），对应 RL 中 step-level advantage 概念。PAV 在 prover policy（与 base policy 不同）下预测 progress，训练数据通过自动标注生成。PAV 提供 dense reward 用于 online RL（5-6x sample efficiency gain）和 test-time search（>8% accuracy gain）。
- Process Advantage Verifier (PAV)


- Improve Mathematical Reasoning in Language Models by Automated Process Supervision
- OmegaPRM（divide-and-conquer MCTS 算法）通过 binary search 自动识别 CoT 中的第一个错误步骤，高效收集 1.5M process supervision annotations；用此自动标注数据训练 PRM，无需 human intervention。PRM 在推理时配合 weighted self-consistency 做 solution selection。


- IntentScore: Intent-Conditioned Action Evaluation for Computer-Use Agents
- 训练时使用两个互补目标：(1) contrastive alignment for state-action relevance；(2) margin ranking for action correctness。架构上将 candidate 的 planning intent 嵌入 action encoder，使模型能区分相似 action 但不同 rationale 的候选。

- ProgRM: Build Better GUI Agents with Progress Rewards
- 设计 LCS-based (Longest Common Subsequence) self-annotation algorithm 自动发现 trajectory 中的 key steps 并分配 progress labels；ProgRM 训练为预测每步的 task completion progress，避免 ORM 的稀疏反馈和 over-penalize 问题。

- Scaling Autonomous Agents via Automatic Reward Modeling And Planning
- 三步：(1) LLM agent 随机 navigate 环境生成 diverse action trajectories；(2) 另一个 LLM 为每条 trajectory 分配 task intent 并合成 negative response 与 correct response；(3) 用 (task intent, positive response, negative response) triplets 训练 reward model。无需 human annotations。

- SPARK: Stepwise Process-Aware Rewards for Reference-Free Reinforcement Learning
- 我们提出SPARK：一个三阶段框架，第一阶段生成器模型产生多样化解，验证器模型使用并行扩展（自一致性）和序贯扩展（元批判）评估它们。第二阶段我们使用这些验证输出作为合成训练数据微调生成式过程奖励模型，其随后在训练中充当奖励信号。


# Critic Model
assess each action before execution

- RLAC: Reinforcement Learning with Adversarial Critic for Free-Form Generation Tasks
- RLAC 中 critic (LLM) 动态识别最可能的 failure modes，external validator 验证这些 modes。Generator 和 critic 通过 adversarial game 联合优化：critic 学习检测更多 errors，generator 学习产生更少 errors。Dynamic critics 比 fixed critics 更有效。

- LLaVA-Critic-R1: Your Critic Model is Secretly a Strong Policy Model
- 将 preference-labeled critic datasets 重组为 verifiable training signals，直接在 base generative model 上做 RL training。结果涌现出双向能力：LLaVA-Critic-R1 既是 top-performing critic 又是 competitive policy model。

- DeepCritic: Deliberate Critique with Large Language Models
- 两阶段：(1) Qwen2.5-72B 生成 4.5K deliberate step-wise critiques（含 multi-perspective verifications + in-depth critiques of initial critiques）做 SFT；(2) 在 PRM800K human-labeled data 或 auto-annotated data（Monte Carlo sampling-based correctness estimation）上做 RL 进一步增强 critique ability。

- SPC: Evolving Self-Play Critic via Adversarial Games for LLM Reasoning
- 两个 model copy 进行 adversarial self-play：sneaky generator 故意生成难以检测的错误步骤；critic 分析 reasoning steps 的正确性。Game outcome（critic 是否识别出错误）作为 RL reward 驱动双方迭代进化。

- No More Stale Feedback: Co-Evolving Critics for Open-World Agent Learning
- ECHO 框架同时优化 policy 和 critic 通过 synchronized co-evolutionary loop：(1) cascaded rollout mechanism: critic 生成多个 diagnoses for initial trajectory；(2) policy refinement 通过 group-structured advantage estimation；(3) saturation-aware gain shaping 奖励 critic 在 high-performing trajectories 上的 incremental improvements。

- Teaching Language Models to Critique via Reinforcement Learning
- CTRL 框架训练 critic model 生成 feedback，目标最大化 fixed generator model 的 correction performance，无需 human supervision。Critic 的 reward 来自其 feedback 帮助 generator 修复代码的实际效果。CTRL-trained critic 同时充当 accurate generative reward model，支持 iterative critique-revision（test-time scaling，relative improvement up to 106.1%）。


- Enhancing LLM Reasoning via Critique Models with Test-Time and Training-Time Supervision
- AutoMathCritique 自动生成 step-level critique data。Critique model 在 test-time 为 actor 提供逐步反馈（尤其在 scaling inference-time compute 时有效）；在 training-time，critique-based supervision 被引入 actor 的 self-training process，改善 exploration efficiency 和 solution diversity。


- Enhancing Robotic Manipulation with AI Feedback from Multimodal Large Language Models
- 训练 multimodal LLM (CriticGPT) 理解 robot manipulation trajectory videos，输出 analysis 和 preference feedback。CriticGPT 生成的 preference labels 从 reward modeling perspective 验证有效性。

- OS-Oracle: A Comprehensive Framework for Cross-Platform GUI Critic Models
- Step level Critic Model
- 两阶段训练：(1) SFT 阶段在 310k critic samples 上训练基础 critic 能力；(2) CP-GRPO (consistency-preserving GRPO) 阶段通过 group relative policy optimization 增强 critic 的评估一致性与准确性。Critic 在推理时作为 pre-execution filter 对每个 candidate action 评分。

- Look Before You Leap: A GUI-Critic-R1 Model for Pre-Operative Error Diagnosis in GUI Automation
- mobile and web domains
- 通过 reasoning-bootstrapping data collection pipeline 构建 GUI-Critic-Train 数据集；使用 S-GRPO (Suggestion-aware GRPO) 训练 critic model，引入 suggestion reward 增强反馈可靠性。Critic 在 action 执行前进行 pre-operative error diagnosis，预测 action 潜在结果并给出 corrective feedback。

- GAIA: A Data Flywheel System for Training GUI Test-Time Scaling Critic Models
- 先用 base agent 的 positive/negative action examples 训练第一轮 ICM；ICM 随后 guide agent actions 收集 refined samples，启动 self-improving cycle（data flywheel）；augmented data 再训练第二轮 critic。这是 critic 的 iterative self-improvement 通过数据飞轮实现，critic 本身通过 SFT 训练

- Video-Language Critic: Transferable Reward Functions for Language-Conditioned Robotics
- 在 Open X-Embodiment data 上使用 contrastive learning + temporal ranking objective 训练 Video-Language Critic。Critic 将 language-conditioned task 与 robot behavior video 进行匹配评分。关键设计是分离 what to accomplish（可从 external observation-only data 学习）和 how to accomplish it（robot-specific），使 reward model 跨 embodiment 迁移。


- CORA: Conformal Risk-Controlled Agents for Safeguarded Mobile GUI Automation
- 训练 Guardian model 估计每个 action 的 action-conditional risk；使用 Conformal Risk Control 校准 execute/abstain boundary（满足 user-specified risk budget）。Diagnostician model 对 rejected actions 做 multimodal reasoning 推荐 interventions (confirm/reflect/abort)。Goal-Lock mechanism 将评估锚定在 clarified user intent 上防止 visual injection attacks。核心为 safety-focused evaluator 架构。

# Verifier

- Generative Verifiers: Reward Modeling as Next-Token Prediction
-  将 verifier 训练为 next-token prediction 任务（而非 discriminative classification），jointly 训练 verification 和 solution generation；GenRM 可利用 CoT reasoning、majority voting 等 LLM 原生能力。用 synthetic verification rationales 作为训练数据，使 GenRM 能检测 subtle errors。
-  

- RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning
- Verifier 和 Generator 通过 RL 交替训练（interleaved co-evolution）。Verifier 是 generative process-level LLM verifier，仅靠 outcome-level verification correctness rewards 训练，无需 process-level annotations。Generator 用 verifier 的 process-level feedback 做 RL training。两者形成 mutual reinforcement 循环（Evaluator → Policy 对应 P6，Policy → Narrative 提供新的 training data for Evaluator 对应 P7+P4）。整体为 co-evolution 的双向互训，主轴向按 Verifier 与 Generator 并重的贡献标注为 P4+P6 composite + P7 外化反馈环。


# 混合的

## PRM + ORM

- UI-Genie: A Self-Improving Approach for Iteratively Boosting MLLM-based Mobile GUI Agents
- 多目标论文（同时产出 V-Par RM + π-Par agent）。RM 训练：通过 rule-based verification + controlled trajectory corruption + hard negative mining 生成 UI-Genie-RM-517k，训练 image-text interleaved RM 同时提供 action-level 和 task-level rewards。Agent 训练：self-improvement pipeline 通过 reward-guided exploration + outcome verification 生成 UI-Genie-Agent-16k 做 SFT。整体构成 Policy → Narrative（agent rollout）→ Evaluator（RM scoring）→ Policy（RM-guided SFT/RL）的自生成闭环（§8.1 信号）。主轴标注为 P4，但 Mechanism 中包含 P7 + P4 + P5/P6 的复合链路。

- Large Reward Models: Generalizable Online Robot Reward Generation with Vision-Language Models
- 在 large-scale multi-source dataset 上训练 VLM-based reward model，使其能基于当前 visual observations 生成 process reward、completion reward 和 temporal contrastive reward。

- Better Process Supervision with Bi-directional Rewarding Signals
- 受 A* 算法启发，BiRM 同时建模两个方向：评估已执行步骤的正确性（incurred cost）+ 预测未来成功的概率（estimated cost to target）。这使 BiRM 比单向 PRM（仅看过去步骤）提供更全面的 guidance。



## Critic + Reward

- Self-Generated Critiques Boost Reward Modeling for Language Models
- 两阶段：(1) 生成并过滤高质量 self-generated critiques（Narrative → Narrative, P1: raw output → filtered critiques）；(2) joint fine-tuning on reward prediction + critique generation（Narrative → Evaluator, P4）

# 不清不楚

- SOLE-R1: Video-Language Reasoning as the Sole Reward for On-Robot Reinforcement Learning
- 两阶段：(1) 通过 large-scale video trajectory and reasoning synthesis pipeline 生成 temporally grounded CoT traces + continuous progress supervision，用 hybrid SFT + RL from verifiable rewards 训练 SOLE-R1 作为 video-language reward model；(2) policy 在 zero-shot online RL 中用 SOLE-R1 的 per-timestep progress estimates 作为唯一 reward signal（Evaluator → Policy，P6）。整体为 P4+P6 composite（§8.2），且 SOLE-R1 作为 sole reward 的特殊性在于完全替代 ground-truth reward。

-  RoboReward: General-Purpose Vision-Language Reward Models for Robotics
-  通过 counterfactual relabeling of successful episodes + temporal clipping 从成功 trajectory 生成 calibrated negative and near-miss examples，解决 OXE 缺乏 failure examples 的问题。在构建的 RoboReward dataset 上训练 VLM-based reward model。


- Generative Reward Models
- GenRM 迭代训练 LLM 在 self-generated reasoning traces 上，产生与 human preference judgments 一致的 synthetic preference labels。

- Hybrid Reward Normalization for Process-supervised Non-verifiable Agentic Tasks
- PPR (Principle Process Reward) 训练 principle-based reward model 改善 process evaluation 的 transparency 和 reliability（P4）。Reward Normalization (ReNorm) 策略校准 outcome 和 process rewards 的平衡，解决 process reward 优化可能与 final outcome 不一致的问题。用 calibrated reward 做 RL training（P6）。

- VLP: Vision-Language Preference Learning for Embodied Manipulation
- 定义三种 language-conditioned preferences，构建 vision-language preference dataset（含 versatile implicit preference orders，无 human annotations）。Preference model 学习提取 language-related features 并作为 preference annotator 服务 downstream RL tasks（通过 reward learning 或 direct policy optimization）。

- RL4F: Generating Natural Language Feedback with Reinforcement Learning for Repairing Model Outputs
- Multi-agent collaborative framework：critique generator 通过 RL 训练，目标最大化 fixed GPT-3 的 end-task performance（critique 帮助 GPT-3 revise outputs 后的实际改善程度作为 reward）。Critique generator 是 GPT-3 大小的 1/200+，无需 fine-tune target model。

- LIV: Language-Image Representations and Rewards for Robotic Control
- LIV objective 基于 dual RL 和 mutual information contrastive learning 的统一，训练 multi-modal representation 隐式编码 universal value function（对 language/image goals）。从 large human video datasets (EpicKitchen) 预训练，可在 unseen environments 中为每帧分配 dense rewards。


- Constitutional AI: Harmlessness from AI Feedback
- 两阶段：(1) SL phase: initial model 采样 → self-critique and revise → fine-tune on revised responses（Narrative → Narrative, P1）；(2) RL phase: fine-tuned model 采样 → AI model 评估偏好 → 训练 preference model（Narrative → Evaluator, P4）→ 用 preference model 作为 reward signal 做 RL training（Evaluator → Policy, P6）。整体为 P1 + P4 + P6 的 composite pipeline。