[Title]: RLAIF vs. RLHF: Scaling Reinforcement Learning from Human Feedback with AI Feedback
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: Human preference pairs / AI-generated preference pairs (from off-the-shelf LLM)
- [Target Experience]: Policy weights aligned with preferences
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}, {human}
- [Utilization]: Policy generates summaries and dialogue responses aligned with human/AI preferences
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段1（P4）：用现成 LLM 生成 AI 偏好标注并训练 RM，以替代人工偏好标注。阶段2（P6）：用训练好的 RM 提供奖励信号，通过 RL 更新策略参数；d-RLAIF 变体跳过 RM 训练，直接调用现成 LLM 给出奖励。

[Title]: Constitutional AI: Harmlessness from AI Feedback
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: 初始模型样本、自我批评、自我修订、AI preference pairs，以及人类给定的 rules/principles
- [Target Experience]: Preference model reward signal and harmless assistant policy weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}, {human}
- [Utilization]: Preference model 作为 RL 阶段 reward signal；修订响应作为 supervised fine-tuning 数据
- [Method]: ⟨SFT⟩, ⟨hybrid⟩
- [Mechanism]: 阶段1（P4）：模型依据宪法原则生成批评与修订，并用 AI 偏好数据训练偏好模型。阶段2（P6）：偏好模型提供奖励信号，经 RLAIF/RL 更新助手策略；由于过程包含 CoT 式推理与修订轨迹，符合推理经验转化边界。

[Title]: Direct Language Model Alignment from Online AI Feedback
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Online AI preference feedback (LLM annotator chooses preferred response from current policy's samples)
- [Target Experience]: Policy weights aligned via DPO
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Policy generates higher-quality responses evaluated by humans
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: 把 LLM 作为在线标注器：每轮从当前策略采样两个响应，由标注器选择偏好，再用 DPO 更新策略。该方法不训练独立 RM，核心是将在线、同策略偏好对作为叙事型经验直接内化到策略参数中。

[Title]: Self-Rewarding Language Models
- [Pathway]: Policy → Narrative → Policy (P7+P5)
- [Source Experience]: Policy's own generated responses (self-generated)
- [Target Experience]: Improved policy weights with enhanced instruction-following and self-rewarding ability
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy generates better responses and provides higher-quality self-rewards for subsequent iterations
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: P7+P5 自增强闭环：策略模型先生成响应，再以判断器角色给自己的响应打分，偏好判断作为叙事型经验外化出来，随后通过 DPO 回灌更新策略。该闭环同时提升指令遵循能力和自评能力，不训练独立 RM。

[Title]: RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Generated samples scored and filtered by a reward model
- [Target Experience]: Policy weights via fine-tuning on high-reward samples
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy generates higher-quality, less biased samples
- [Method]: ⟨SFT⟩
- [Mechanism]: 固定 RM 对生成样本打分，筛出高奖励样本并丢弃低质量样本，再用筛选后的叙事型轨迹做 SFT 更新策略。RM 在这里是选择工具而非被训练的评估器，因此主路径是叙事型经验到策略参数的 P5。

[Title]: BOND: Aligning LLMs with Best-of-N Distillation
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Best-of-N distribution derived from base policy + reward model rankings
- [Target Experience]: Policy weights that emulate Best-of-N sampling distribution
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy generates high-quality outputs at inference without N× sampling cost
- [Method]: ⟨hybrid⟩
- [Mechanism]: 用 RM 对多个候选响应排序并选出 Best-of-N 样本，形成 BoN 诱导分布，再通过 Jeffreys 散度做分布匹配，使策略逼近 BoN 采样分布。RM 只作为固定排序器，路径实质是经 BoN 筛选的叙事型生成分布到策略参数的 P5。

[Title]: BoNBoN Alignment for Large Language Models and the Sweetness of Best-of-n Sampling
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Best-of-n sampling distribution from base LLM
- [Target Experience]: Policy weights mimicking Best-of-n distribution
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy produces outputs preferred over base policy with minimal off-target effects
- [Method]: ⟨hybrid⟩
- [Mechanism]: 论文先把 BoN、RLHF 和 DPO 统一到倾斜分布框架中，说明 BoN 在胜率与 KL 约束之间接近最优。随后用 BoN 分布结构设计微调目标，使策略直接逼近 BoN 采样分布；RM 只提供排序信号，因此归为叙事型分布到策略参数的 P5。

[Title]: Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: Automatically constructed process-wise supervision data for math solution steps
- [Target Experience]: Math-Shepherd process reward model and PPO-updated math reasoning policy weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: PRM 用于 reranking LLM outputs，并作为 step-by-step PPO 的 dense reward
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 阶段1（P4）：自动构造步骤级过程监督并训练 Math-Shepherd PRM。阶段2（P6）：PRM 为每个推理步骤提供奖励，通过 PPO 强化开源 LLM 的数学推理策略。

[Title]: Process Reinforcement through Implicit Rewards
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: Policy rollouts with outcome labels for multi-step math and coding reasoning
- [Target Experience]: Online-updated PRM / implicit process rewards and reasoning policy weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 隐式 process rewards 作为 RL advantage / dense feedback，训练 math and coding reasoning policies
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段1（P4）：PRIME 利用策略展开轨迹与最终结果标签在线更新 PRM，避免额外的过程标签。阶段2（P6）：隐式过程奖励与优势函数结合，为策略优化提供细粒度反馈。

[Title]: Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: Multi-step reasoning traces, prover-policy progress estimates, and step-level advantage targets
- [Target Experience]: Process advantage verifiers (PAVs) and policy improved by search / online RL
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: PAVs 用于 test-time search scoring，并作为 online RL dense rewards
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段1（P4）：在不同证明器策略下估计每个推理步骤对未来正确性的贡献，训练 PAV 预测步骤级优势。阶段2（P6）：PAV 奖励用于搜索和在线 RL，提高基础策略的探索效率与样本效率。

[Title]: Autonomous Evaluation and Refinement of Digital Agents
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Domain-general automatic evaluators for web navigation and device-control trajectories
- [Target Experience]: Fine-tuned digital-agent policy and inference-time guided agent behavior
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: 不清楚
- [Utilization]: Evaluator outputs 用于 fine-tuning existing agents，并在 inference time 指导 web/device-control decisions
- [Method]: ⟨hybrid⟩
- [Mechanism]: 自动评估器把数字智能体的轨迹质量转化为训练和推理时的反馈信号。评估器信号被复用于策略微调与推理期动作引导，直接改变智能体策略的决策分布。

[Title]: WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: Web-agent unsuccessful attempts, self-evolved tasks, and web interaction rollouts
- [Target Experience]: Outcome-supervised reward model and RL-trained open LLM web-agent policies
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: ORM 提供 sparse outcome feedback；self-evolving curriculum 提供在线训练任务；adaptive RL 更新 web-agent policy
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段1（P4）：WebRL 从网页交互尝试和结果监督中构造稳健 ORM。阶段2（P6）：ORM 奖励与自演化课程共同驱动在线 RL，把 Llama/GLM 等开放模型转化为网页智能体策略。

[Title]: RL-VLM-F: Reinforcement Learning from Vision Language Foundation Model Feedback
- [Pathway]: Out of Scope
- [Mechanism]: 摘要中的受训对象是经典控制和机器人操作的传统 RL 策略，虽然奖励来自 VLM 偏好标注，但没有清楚表明策略是 LLM/VLA/基于 LLM 的智能体；对应 §3.2 的非基于 LLM 的系统边界。

[Title]: AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Agent interaction trajectories in multi-turn decision-making tasks (web shopping, browser navigation)
- [Target Experience]: AgentPRM weights (process reward model for agent tasks)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: PRM used for test-time compute scaling (8× more compute-efficient) and applicable to RL of LLM agents (mentioned but not primary)
- [Method]: ⟨SFT⟩
- [Mechanism]: 论文针对智能体任务重新定义 PRM：智能体动作不只按正确性评分，还按接近目标程度和进展评分。AgentPRM 通过 TD 估计与 GAE 从轨迹中自动获得训练标签，核心贡献是 PRM 构建；若后续用于 RL 训练，则形成 P4+P6。

[Title]: Meta-Rewarding Language Models: Self-Improving Alignment with LLM-as-a-Meta-Judge
- [Pathway]: Policy → Narrative → Policy (P7+P5)
- [Source Experience]: Policy's own generated responses AND self-judgments
- [Target Experience]: Improved policy with better judgment AND instruction-following ability
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy achieves higher win rate on AlpacaEval 2 and Arena-Hard
- [Method]: ⟨hybrid⟩
- [Mechanism]: 这是 P7+P5 自增强闭环的扩展：模型先作为策略端生成响应，再作为判断器评判响应，随后作为元判断器评判判断质量。判断与元判断共同形成偏好反馈，经偏好优化更新策略，用来缓解自奖励训练中判断能力过早饱和的问题。

[Title]: Policy Improvement using Language Feedback Models
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: Visual trajectories verbalized as language descriptions and LLM feedback on desirable actions
- [Target Experience]: Language Feedback Models and imitation-learning policy updates in Touchdown, ScienceWorld, and ALFWorld
- [Source Modality]: [cross-modal]
- [Target Modality]: [cross-modal]
- [Experience Source]: {teacher}
- [Utilization]: LFM 识别 desirable behaviour，筛选可模仿 action，用于 one-round adaptation 和 imitation learning
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段1（P4）：LLM 对视觉/语言落地轨迹给出行为反馈，训练 LFM 判断哪些动作有助于完成指令。阶段2（P6）：LFM 判断被复用为模仿信号，更新具身或文本游戏策略。

[Title]: Vision-Language Models are Zero-Shot Reward Models for Reinforcement Learning
- [Pathway]: Out of Scope
- [Mechanism]: 摘要中的策略是 MuJoCo 人形控制等传统 RL 智能体，VLM/CLIP 只作为奖励来源，未清楚表明受训策略是 LLM/VLA/基于 LLM 的智能体；对应 §3.2 的非基于 LLM 的系统边界。

[Title]: ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: MCTS*-searched reasoning traces, oracle final-answer correctness, and inferred per-step values
- [Target Experience]: Process reward model, value targets, and self-trained LLM reasoning policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Inferred process rewards refine PRM；high-quality searched traces feed policy self-training
- [Method]: ⟨MCTS⟩, ⟨RL: ReST⟩
- [Mechanism]: 阶段1（P4）：利用树搜索展开轨迹与最终正确性估计每步通向正确答案的概率，形成过程奖励和值目标。阶段2（P6/P5）：PRM 引导与筛选后的推理轨迹共同训练策略，并迭代增强奖励模型与策略模型。

[Title]: Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Successful and unsuccessful web-agent interaction trajectories, guided MCTS traces, and self-critiques
- [Target Experience]: LLM agent policy weights for WebShop and booking tasks
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Agent interaction trajectories are used for iterative fine-tuning with off-policy DPO
- [Method]: ⟨MCTS⟩, ⟨RL: DPO⟩
- [Mechanism]: 引导式 MCTS 扩展网页交互决策，自我批评标记轨迹质量；成功和失败轨迹被转化为偏好式训练信号，再通过离线 DPO 内化到智能体策略参数中。

[Title]: OpenWebVoyager: Building Multimodal Web Agents via Iterative Real-World Exploration, Feedback and Optimization
- [Pathway]: Policy → Narrative → Policy (P7+P5)
- [Source Experience]: Agent exploration trajectories in real web environments with AI feedback
- [Target Experience]: Improved multimodal web agent policy weights
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Policy performs web navigation tasks with improving success rate across iterations
- [Method]: ⟨SFT⟩, ⟨hybrid⟩
- [Mechanism]: P7+P5 自增强闭环：先用模仿学习得到基础网页操作能力，再让智能体在开放网页中探索并收集轨迹反馈。通用模型评判哪些轨迹表现较好，筛选出的轨迹通过微调或偏好优化回灌策略，探索、反馈、优化可多轮迭代。

[Title]: Web-Shepherd: Advancing PRMs for Reinforcing Web Agents
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Web navigation trajectories, step-level preference pairs, and annotated checklists
- [Target Experience]: Web-Shepherd process reward model for web navigation
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {human}
- [Utilization]: Web-Shepherd is reused as verifier during WebArena-lite test-time decision selection; the abstract says it can support training and test-time use
- [Method]: ⟨SFT⟩
- [Mechanism]: WebPRM Collection 将网页智能体的步骤级决策、偏好标注和检查清单组织为监督信号，并内化为能给网页导航步骤评分的 PRM。摘要未说明 Web-Shepherd 在报告的 WebArena-lite 设置中直接更新策略权重，因此主路径是 P4。

[Title]: GUI-Shepherd: Reliable Process Reward and Verification for Long-Sequence GUI Tasks
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: GUI interaction trajectories with human-annotated scores and GPT-4o rationales
- [Target Experience]: GUI-Shepherd PRM and GUI agent policy updated by multi-turn online PPO
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {human}, {teacher}
- [Utilization]: PRM serves as RL reward provider and inference verifier across AndroidWorld / AndroidControl settings
- [Method]: ⟨RL: PPO⟩, ⟨SFT⟩
- [Mechanism]: 阶段1（P4）：带标注的 GUI 交互和理由用于训练 GUI-Shepherd，使其成为步骤级 PRM。阶段2（P6）：GUI-Shepherd 奖励用于多轮在线 PPO，也可作为验证器，提升长序列 GUI 策略。

[Title]: Real-World Offline Reinforcement Learning from Vision Language Model Feedback
- [Pathway]: Out of Scope
- [Mechanism]: 摘要中的受训对象是离线 RL 机器人策略，VLM 用于给传统机器人数据生成奖励标签；未清楚表明策略是 LLM/VLA/基于 LLM 的智能体，对应 §3.2 的非基于 LLM 的系统边界。

[Title]: AdaRubric: Task-Adaptive Rubrics for LLM Agent Evaluation
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: Task descriptions, WebArena/ToolBench trajectories, step-wise trajectory scores, and filtered preference pairs
- [Target Experience]: Task-adaptive rubric evaluator and DPO/PPO-trained LLM agents
- [Source Modality]: [txt]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}
- [Utilization]: Rubric-scored preference pairs train agents with DPO and accelerate PPO; evaluator also supports step-wise trajectory assessment
- [Method]: ⟨RL: DPO⟩, ⟨RL: PPO⟩
- [Mechanism]: 阶段1（P4）：任务描述被转化为任务自适应评分规约，用来逐步评分智能体轨迹并筛选偏好对。阶段2（P6）：这些由评估器产生的偏好或奖励被 DPO/PPO 复用，用来改进网页、工具使用和代码修复智能体。

[Title]: Let's Verify Step by Step
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Human-annotated step-level feedback labels (PRM800K dataset: 800,000 step-level labels)
- [Target Experience]: Process-supervised Reward Model (PRM) weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: PRM used for training more reliable reasoning models (process supervision outperforms outcome supervision on MATH)
- [Method]: ⟨SFT⟩
- [Mechanism]: 论文比较过程监督与结果监督对可靠推理模型训练的影响，并用 PRM800K 步骤级人工反馈训练过程监督 RM。PRM 提供逐步反馈，可被用于策略训练而形成 P4+P6；但论文核心贡献在 PRM 构建、标注数据集和主动学习提升标注效率。

[Title]: WebArbiter: A Principle-Guided Reasoning Process Reward Model for Web Agents
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Web-agent preference annotations, reasoning distillation data, and correctness feedback for verdicts
- [Target Experience]: WebArbiter generative WebPRM with structured justifications and preference verdicts
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {human}, {teacher}
- [Utilization]: WebPRM scores reward-guided trajectory search on WebArena-Lite
- [Method]: ⟨SFT⟩, ⟨hybrid⟩
- [Mechanism]: WebArbiter 先把原则引导的推理蒸馏进生成式 PRM，再用 RL 校正教师偏差，使判断更贴近真实正确性。摘要中下游复用主要是奖励引导搜索而非策略权重更新，因此主转化是 P4。

[Title]: From Correction to Mastery: Reinforced Distillation of Large Language Model Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Student-generated agent trajectories, teacher corrections at earliest errors, verified prefixes, and target rewards
- [Target Experience]: Student LLM-agent policy weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Corrected trajectories support SFT；verified prefixes and target rewards initialize short-horizon RL
- [Method]: ⟨SFT⟩, ⟨hybrid⟩
- [Mechanism]: 学生智能体先生成轨迹暴露能力短板，教师定位并纠正第一个错误，产生与学生能力匹配的训练轨迹。这些轨迹先经 SFT 内化，再从已验证前缀处启动短程 RL，训练模型超越单纯模仿并自主续写正确行动。

[Title]: Improve Mathematical Reasoning in Language Models by Automated Process Supervision
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: CoT solution steps, first-error locations, and automatically collected process supervision annotations
- [Target Experience]: Process reward models for mathematical reasoning
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: PRMs support weighted self-consistency and enhance math reasoning performance
- [Method]: ⟨MCTS⟩
- [Mechanism]: OmegaPRM 用分治式 MCTS 定位 CoT 中的首个错误，并平衡正负步骤样本；这些自动标注用于训练 PRM。摘要重点是 PRM 构建与推理期加权自一致性，没有明确的策略权重 RL 更新。

[Title]: ZeroGUI: Automating Online GUI Learning at Zero Human Cost
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: VLM-generated task goals and VLM-estimated success rewards from GUI environment states
- [Target Experience]: Online RL-trained pure-vision GUI agent policies
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}, {self}
- [Utilization]: Automatic reward estimation supplies online RL feedback; task generation supplies curriculum goals
- [Method]: ⟨hybrid⟩
- [Mechanism]: 基于 VLM 的评估器估计 GUI 交互任务是否成功，并在无人标注条件下提供奖励。两阶段在线 RL 复用这些评估器信号，同时让智能体持续与 OSWorld/AndroidLab 环境交互。

[Title]: SRR-Judge: Step-Level Rating and Refinement for Enhancing Search-Integrated Reasoning in Search Agents
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: SRR-Judge step-level ratings and refinements for reasoning/search actions
- [Target Experience]: Fine-tuned deep search agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: SRR-annotated trajectories are reused in iterative rejection sampling fine-tuning
- [Method]: ⟨hybrid⟩
- [Mechanism]: SRR-Judge 评估中间 ReAct 思考与搜索动作，生成评分和修订标注；随后在被评估器选择或标注的轨迹上微调智能体策略，以增强搜索集成推理。

[Title]: ProgRM: Build Better GUI Agents with Progress Rewards
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: GUI trajectories, self-annotated key steps, and progress labels
- [Target Experience]: Progress Reward Model and GUI actor policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: ProgRM provides dense intermediate rewards for online GUI-agent training
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段1（P4）：基于 LCS 的自标注发现关键步骤，并为轨迹分配进展标签以训练 ProgRM。阶段2（P6）：ProgRM 预测步骤级任务完成进度，并向 GUI 执行器提供密集奖励。

[Title]: TGPO: Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: Tree-structured web-agent trajectories, semantically merged states, subgoal progress, redundancy, and action verification signals
- [Target Experience]: Process Reward Model and TGPO-trained web-agent policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {teacher}
- [Utilization]: PRM rewards and dynamic decision-point weights supervise offline RL for web agents
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段1（P4）：轨迹树暴露状态/动作进展与冲突，使 PRM 能生成细粒度奖励。阶段2（P6）：TGPO 将 PRM 奖励和动态加权结合，用于优化高影响网页决策。

[Title]: Building Autonomous GUI Navigation via Agentic-Q Estimation and Step-Wise Policy Optimization
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: Policy-produced GUI state-action trajectories
- [Target Experience]: Agentic-Q model and step-wise optimized MLLM GUI policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Agentic-Q values evaluate action contribution and guide decoupled policy RL
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段1（P4）：自生成的状态-动作轨迹训练 Q 模型，用于估计动作的长期效用。阶段2（P6）：学习到的 Q 值成为步骤级反馈，用于策略优化并改善 GUI 导航与落地。

[Title]: Robust Preference Optimization through Reward Model Distillation
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Explicit reward model trained on preference data (distilled into implicit reward)
- [Target Experience]: Policy weights via DPO with distilled reward signal
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Policy generates preferred responses robust to distribution shift in preference annotations
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: 论文分析 DPO 中隐式奖励过拟合导致策略退化的问题，并将显式 RM 蒸馏到 DPO 的隐式奖励中，使策略的对数似然比匹配 RM 信号。进一步用一组 RM 表达不确定性，以提高偏好分布偏移下的鲁棒性；路径是显式评估器信号到策略参数的 P6。

[Title]: MagicGUI-RMS: A Multi-Agent Reward Model System for Self-Evolving GUI Agents via Automated Feedback Reflux
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: GUI agent trajectories, erroneous actions, refined alternatives, and automatically constructed reward datasets
- [Target Experience]: DS-RM / GP-RM reward model system and self-evolving GUI agent behavior
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Reward model system evaluates trajectories, gives corrective feedback, and feeds automated data reflux for continual agent improvement
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段1（P4）：结构化数据构造把 GUI 轨迹和纠错备选动作转化为平衡的奖励数据集，用于训练 DS-RM/GP-RM。阶段2（P6）：奖励系统识别错误动作并提出替代方案，反馈再回流到智能体学习闭环。

[Title]: Motif: Intrinsic Motivation from Artificial Intelligence Feedback
- [Pathway]: Out of Scope
- [Mechanism]: 摘要中的受训对象是 NetHack 传统 RL 智能体，LLM 只提供由图像描述偏好派生的内在奖励；未清楚表明策略是基于 LLM 的智能体，对应 §3.2 的非基于 LLM 的系统边界。

[Title]: OpenClaw-RL: Train Any Agent Simply by Talking
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: User replies, tool outputs, terminal / GUI state changes, SWE traces, and next-state textual hints
- [Target Experience]: PRM-derived rewards, Hindsight-Guided OPD supervision, and updated general agent policy
- [Source Modality]: [cross-modal]
- [Target Modality]: [cross-modal]
- [Experience Source]: {self}, {human}
- [Utilization]: PRM rewards drive RL；textual hints and enhanced teacher context supply token-level directional supervision
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段1（P4）：下一状态信号被 PRM 判断器解析为评价性标量奖励。阶段2（P6/P5）：同一批交互还产生指令式提示，用于同策略蒸馏；奖励反馈则用于会话、终端、GUI、SWE 和工具调用场景中的策略更新。

[Title]: Vision-Language Models as a Source of Rewards
- [Pathway]: Out of Scope
- [Mechanism]: 摘要使用 CLIP/VLM 奖励训练传统视觉域 RL 智能体，未明确存在 LLM/VLA 策略或基于 LLM 的智能体决策过程；对应 §3.2 的非基于 LLM 的系统边界。

[Title]: OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: GUI trajectories decomposed into verifiable milestones and audited evidence chains
- [Target Experience]: Multi-agent critic framework and GUI policies improved by online RL / self-training filtering
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {teacher}
- [Utilization]: OS-Themis supports online RL reward feedback and validates trajectories for self-training loops
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段1（P4）：OS-Themis 将 GUI 轨迹组织为里程碑和可审查证据链，使结果奖励更可靠。阶段2（P6）：批评器判断被复用为在线 RL 奖励和过滤信号，以改进 AndroidWorld GUI 智能体。

[Title]: Zero-Shot Reward Specification via Grounded Natural Language
- [Pathway]: Out of Scope
- [Mechanism]: 摘要用 CLIP 从目标文本和原始像素生成奖励信号，以训练控制或机器人操作策略；未清楚表明策略是基于 LLM 的智能体，对应 §3.2 的非基于 LLM 的系统边界。

[Title]: VEM: Environment-Free Exploration for Training GUI Agent with Value Environment Model
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: Offline GUI state-action data and human-like priors about GUI interaction outcomes
- [Target Experience]: Value Environment Model and VLM GUI-agent policy guided by frozen values
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {human}, {self}
- [Utilization]: Frozen VEM predicts action utility and guides environment-free policy exploration
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段1（P4）：离线 GUI 交互数据被内化为 VEM 中的语义状态-动作价值估计。阶段2（P6）：VEM 信号在没有实时环境交互的情况下引导策略探索和 RL。

[Title]: FuRL: Visual-Language Models as Fuzzy Rewards for Reinforcement Learning
- [Pathway]: Out of Scope
- [Mechanism]: 摘要聚焦 MetaWorld 上的 SAC/DrQ 传统 RL 智能体与 VLM 奖励对齐，未清楚表明受训策略是 LLM/VLA/基于 LLM 的智能体；对应 §3.2 的非基于 LLM 的系统边界。

[Title]: No More Stale Feedback: Co-Evolving Critics for Open-World Agent Learning
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: Open-world LLM-agent rollouts, critic diagnoses, and group-structured refinements
- [Target Experience]: Co-evolving critic and GRPO-trained LLM-agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Critic feedback supplies natural-language guidance and shaped rewards for synchronized policy updates
- [Method]: ⟨RL: GRPO⟩, ⟨hybrid⟩
- [Mechanism]: 阶段1（P4）：批评器对级联展开轨迹给出诊断，并被优化为能诱导增量改进的反馈。阶段2（P6）：双轨 GRPO 保持批评器反馈与演化中的策略对齐，并用该反馈进行长程策略学习。

[Title]: RLAnything: Forge Environment, Policy, and Reward Model in Completely Dynamic RL System
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: LLM/agentic task rollouts, step-wise signals, outcome signals, and critic feedback for environment adaptation
- [Target Experience]: Jointly optimized reward model, adapted environment, and agent policy
- [Source Modality]: [cross-modal]
- [Target Modality]: [cross-modal]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Optimized reward-model signals provide feedback for policy training; critic feedback also adapts the training environment
- [Method]: ⟨hybrid⟩
- [Mechanism]: RLAnything 形成闭环：轨迹和批评器反馈更新奖励模型与环境，改进后的奖励模型再向策略训练提供步骤级和结果级反馈。阶段1把经验映射为评估器/环境信号，阶段2用这些信号优化策略。

[Title]: Iterative Tool Usage Exploration for Multimodal Agents via Step-wise Preference Tuning
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Verifier-provided AI feedback over sampled tool-use steps and synthesized multimodal tasks
- [Target Experience]: Preference-tuned multimodal tool-use controller policy
- [Source Modality]: [cross-modal]
- [Target Modality]: [cross-modal]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Step-wise preference data updates the controller through preference tuning
- [Method]: ⟨hybrid⟩
- [Mechanism]: SPORT 在真实环境工具使用中交替进行步骤采样与步骤验证；验证器将探索到的工具结果转化为步骤级偏好，偏好信号再调优控制器，使后续工具使用轨迹更有效。

[Title]: VARP: Reinforcement Learning from Vision-Language Model Feedback with Agent Regularized Preferences
- [Pathway]: Out of Scope
- [Mechanism]: 摘要中的策略是连续控制机器人或 MetaWorld RL 策略，VLM 提供偏好标签但未清楚表明存在 LLM/VLA 策略；对应 §3.2 的非基于 LLM 的系统边界。

[Title]: SWEET-RL: Training Multi-Turn LLM Agents on Collaborative Reasoning Tasks
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: Multi-turn collaborative task trajectories with training-time information from ColBench
- [Target Experience]: Critic model and LLM-agent policy improved by step-wise rewards
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}, {self}
- [Utilization]: Critic outputs step-level rewards for multi-turn policy optimization
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段1（P4）：批评器在训练时访问额外信息并评估每一轮协作。阶段2（P6）：批评器的步骤级奖励解决后端编程与前端设计协作任务中的信用分配问题，并更新策略。

[Title]: Teaching LLM to be Persuasive: Reward-Enhanced Policy Optimization for Alignment from Heterogeneous Rewards
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Preference RM scores, LLM-as-a-judge evaluations, rule-based reward checks, SOP compliance signals, and expert consensus evaluations
- [Target Experience]: Persuasive multi-turn business-development dialogue agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}, {teacher}
- [Utilization]: Heterogeneous rewards are combined during REPO post-training to optimize long multi-turn negotiation behavior
- [Method]: ⟨RL: GRPO⟩, ⟨hybrid⟩
- [Mechanism]: RM/RJ/RF 等评估器从 SOP 遵循、护栏等多个方面评分多阶段 OTA 谈判动作；REPO 将这些异构评估器信号整合为策略优化奖励，用于部署型 LLM 对话智能体。

[Title]: Aligning Large Language Models by On-Policy Self-Judgment
- [Pathway]: Policy → Narrative → Policy (P7+P5)
- [Source Experience]: Policy's own pairwise judgments of on-the-fly generated responses
- [Target Experience]: Single model weights that serve as both policy and judge
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy generates preferred responses; rejection sampling further improves performance without additional evaluator
- [Method]: ⟨SFT⟩
- [Mechanism]: SELF-JUDGE 训练单一模型同时作为策略和判断器，并把成对判断任务视为指令跟随任务的一种。当前策略即时生成响应，再由自身判断器给出判断，判断作为叙事型经验外化并通过偏好优化回灌策略，构成 P7+P5。

[Title]: Video-Language Critic: Transferable Reward Functions for Language-Conditioned Robotics
- [Pathway]: Out of Scope
- [Mechanism]: 摘要中的执行器是机器人或 MetaWorld 策略，批评器来自视频-语言奖励学习；未清楚表明受训策略是 LLM/VLA/基于 LLM 的智能体，对应 §3.2 的非基于 LLM 的系统边界。

[Title]: Enhancing Robotic Manipulation with AI Feedback from Multimodal Large Language Models
- [Pathway]: Out of Scope
- [Mechanism]: 摘要训练 CriticGPT 提供机器人操作偏好反馈，但下游是 MetaWorld 策略学习，未清楚表明受训策略是 LLM/VLA/基于 LLM 的智能体；对应 §3.2 的非基于 LLM 的系统边界。

[Title]: DPO Learning with LLMs-Judge Signal for Computer Use Agents
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: LLM-as-Judge evaluations over synthetic GUI interaction trajectories
- [Target Experience]: Lightweight local VLM computer-use agent policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}
- [Utilization]: Evaluator-filtered synthetic trajectories become high-quality RL/DPO training data for local CUA
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: LLM 评审器框架为合成 GUI 轨迹打分并筛选样本；这些评估器决策被转化为偏好/训练信号，用于微调可在本地 GUI 上操作的小型 VLM 策略。

[Title]: Policy Learning from Large Vision-Language Model Feedback Without Reward Modeling
- [Pathway]: Out of Scope
- [Mechanism]: 摘要中的受训对象是机器人操作离线 RL 策略，VLM 偏好标签直接监督传统控制策略；未清楚表明存在 LLM/VLA/基于 LLM 的智能体，属 §3.2 非基于 LLM 的系统边界。

[Title]: Expanding the Capabilities of Reinforcement Learning via Text Feedback
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Multi-turn textual feedback, feedback-conditioned second-turn generations, and auxiliary feedback targets
- [Target Experience]: Single-turn LLM policy that internalizes text feedback
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}, {teacher}
- [Utilization]: Feedback is available during training and removed at inference; policy learns via self-distillation or feedback modeling
- [Method]: ⟨SFT⟩, ⟨hybrid⟩
- [Mechanism]: RLTF 把文本反馈作为训练时中间信号。RLTF-SD 将带反馈的第二轮行为转化为单轮策略目标，RLTF-FM 增加反馈预测辅助目标，把多轮反馈经验内化进策略参数。

[Title]: The Lighthouse of Language: Enhancing LLM Agents via Critique-Guided Improvement
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: Actor trajectories in interactive environments and natural-language critiques / actionable revisions
- [Target Experience]: Trained critic model and improved actor policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Critic-generated feedback guides actor exploration and policy improvement
- [Method]: ⟨hybrid⟩
- [Mechanism]: CGI 先训练批评器对执行器轨迹给出细粒度评估和修订建议，再训练执行器使用这些批评。评估器语言反馈由此转化为交互任务中的更好决策能力，形成 P4+P6。

[Title]: Code as Reward: Empowering Reinforcement Learning with VLMs
- [Pathway]: Out of Scope
- [Mechanism]: 摘要中 VLM-CaR 为传统 RL 智能体生成密集奖励代码，受训策略覆盖离散和连续环境；未清楚表明存在 LLM/VLA/基于 LLM 的智能体，对应 §3.2 的非基于 LLM 的系统边界。

[Title]: Training Agents with Weakly Supervised Feedback from Large Language Models
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Critic LLM selections over self-generated environmental interaction trajectories
- [Target Experience]: Updated LLM-based agent policy for API-bank tasks
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Critic-selected good trajectories update the agent iteratively
- [Method]: ⟨SFT⟩
- [Mechanism]: 智能体先通过环境交互生成轨迹，批评器 LLM 从中选择表现较好的子集；这些由评估器筛选的轨迹作为下一轮策略的模仿或更新数据。

[Title]: Affordance-Guided Reinforcement Learning via Visual Prompting
- [Pathway]: Out of Scope
- [Mechanism]: 摘要关注机器人操作 RL 中由 VLM 关键点可供性产生的奖励，未清楚表明受训策略是 LLM/VLA/基于 LLM 的智能体；对应 §3.2 的非基于 LLM 的系统边界。

[Title]: Reinforcement Learning with Foundation Priors: Let Embodied Agent Efficiently Learn on Its Own
- [Pathway]: Out of Scope
- [Mechanism]: 摘要虽使用基础模型先验，但受训对象是机器人操作中的 FAC/RL 策略，未清楚表明存在 LLM/VLA 策略或基于 LLM 的智能体；对应 §3.2 的非基于 LLM 的系统边界。

[Title]: Teaching Language Models to Self-Improve by Learning from Language Feedback
- [Pathway]: Narrative → Narrative → Policy (P1+P5)
- [Source Experience]: Self-generated responses with critiques and refinements from a more advanced model
- [Target Experience]: Policy weights via SFT on self-generated feedback and refinements
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Policy win rate increases from 9.6% to 25.8% on AlpacaEval 2.0 (70B model)
- [Method]: ⟨SFT⟩
- [Mechanism]: SRT 流程是：基础模型生成初始响应，更强模型提供批评和修订，基础模型再从自生成反馈与修订中学习。原始响应先转化为批评/修订叙事型经验（P1），再通过 SFT 内化为策略参数（P5）。

[Title]: SAIL: Self-Improving Efficient Online Alignment of Large Language Models
- [Pathway]: Policy → Narrative → Policy (P7+P5)
- [Source Experience]: Online self-generated samples with iteratively refined preference labels
- [Target Experience]: Policy weights aligned via bilevel optimization reduced to single-level method
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy achieves improved alignment performance with minimal computational overhead
- [Method]: ⟨hybrid⟩
- [Mechanism]: SAIL 将在线 LLM 对齐形式化为双层优化，并借助奖励-策略等价性化简为高效一阶方法。策略生成样本后，以自身隐式奖励模型调节偏好标签，再用精炼偏好数据更新策略，构成在线 P7+P5 自改进闭环。

[Title]: Athena: Enhancing Multimodal Reasoning with Data-efficient Process Reward Models
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: Multimodal reasoning steps, weak/strong completer consistency signals, and process-labeled samples
- [Target Experience]: Athena-PRM and Athena-7B policy trained by reward-ranked fine-tuning
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {teacher}
- [Utilization]: PRM supports test-time scaling, step correctness evaluation, and reward-ranked fine-tuning
- [Method]: ⟨SFT⟩, ⟨hybrid⟩
- [Mechanism]: 阶段1（P4）：弱/强补全器之间的预测一致性用于筛选可靠的多模态推理步骤标签，训练 Athena-PRM。阶段2（P6）：Athena-PRM 给推理过程评分，并提供按奖励排序的微调信号来更新策略。

[Title]: Taming the Judge: Deconflicting AI Feedback for Stable Reinforcement Learning
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: LLM judge preference judgments with logical inconsistencies (preference cycles)
- [Target Experience]: Deconflicted reward signal (DAG-based) AND improved policy via stable RL
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Policy trained with deconflicted signal achieves improved training stability and performance
- [Method]: ⟨hybrid⟩
- [Mechanism]: 论文针对 AI 反馈中的判断不一致，特别是偏好环导致的 RL 不稳定。阶段1（P4 精炼）：用 CDR 衡量判断冲突，并将原始偏好判断构成偏好图，再转化为无冲突 DAG 与逻辑一致的奖励信号。阶段2（P6）：用净化后的奖励信号训练策略。

[Title]: Fine-Tuning Language Models with Reward Learning on Policy
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: Policy-generated samples used via unsupervised multi-view learning + synthetic preference data
- [Target Experience]: On-distribution refined reward model AND improved policy weights via RL
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy achieves state-of-the-art alignment on benchmark datasets
- [Method]: ⟨hybrid⟩
- [Mechanism]: P4+P6 组合：RLP 从策略样本中训练或精炼 RM，包括无监督多视角学习和合成偏好生成，使 RM 保持贴近当前策略分布。随后同分布 RM 经 RL 给策略提供更准确奖励；与传统 RLHF 不同，RM 会随策略演化持续更新。

[Title]: RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: All self-generated samples (both positive and negative trajectories) with scalar rewards
- [Target Experience]: Policy weights via reward-weighted fine-tuning
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy achieves better mathematical reasoning performance than Rejection Sampling Fine-Tuning
- [Method]: ⟨SFT⟩
- [Mechanism]: RIFT 不丢弃负样本，而是利用所有自生成样本，并用标量奖励对损失加权，使模型同时从正负轨迹中学习。稳定化损失避免朴素奖励整合导致训练崩溃；路径是奖励加权叙事型轨迹到策略参数的 P5。

[Title]: Off-Policy Corrected Reward Modeling for Reinforcement Learning from Human Feedback
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: Human preference data + off-policy correction via importance weighting
- [Target Experience]: Corrected reward model (more accurate under distribution shift) AND improved final policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Policy performs significantly better than standard RLHF on summarization and chatbot tasks
- [Method]: ⟨hybrid⟩
- [Mechanism]: 论文从分布偏移角度分析 RLHF 过优化：RM 参数估计不一致会导致策略梯度估计不一致。OCRM 用重要性加权迭代校正离线 RM，无需新增标签或样本；更准确的 RM 再通过 RL 改进策略，形成 P4 精炼 + P6。

[Title]: WARM: On the Benefits of Weight Averaged Reward Models
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Human preference data used to train multiple reward models
- [Target Experience]: Weight-averaged ensemble RM (improved efficiency and robustness)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: RM used for RL fine-tuning; policy trained with WARM achieves 79.4% win rate vs single RM policy
- [Method]: ⟨SFT⟩
- [Mechanism]: WARM 微调多个同基座 RM，并在权重空间中平均，而非做预测集成。由于共享预训练基座下微调权重存在近似线性连通性，权重平均比预测集成更高效，并在分布偏移和偏好不一致下更稳健；主贡献是 P4。

[Title]: Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Human preference data used to train reward model ensembles
- [Target Experience]: Ensemble of reward models for more robust reward estimation
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: RM ensembles used for alignment at training time (RL) and inference time (reranking); mitigate but don't eliminate reward hacking
- [Method]: ⟨SFT⟩
- [Mechanism]: 论文分析 RM 集成对奖励黑客的缓解作用：同分布表现相似的 RM 在对齐中可能产生差异很大的奖励，反映评估器欠定性。RM 集成可缓解过优化，预训练种子差异带来的集成通常优于微调种子差异，但共享错误模式使其无法完全消除奖励黑客；主贡献是 P4 分析。

[Title]: Improving Multimodal Interactive Agents with Reinforcement Learning from Human Feedback
- [Pathway]: Out of Scope
- [Mechanism]: 摘要中的具身智能体是模拟 3D 世界里的模仿/RL 智能体，未清楚表明存在 LLM/VLA/基于 LLM 的策略；按 §3.2 的非基于 LLM 的系统边界排除。

[Title]: The Perfect Blend: Redefining RLHF with Mixture of Judges
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: Multiple evaluation signals from diverse judges (human preference data proxy)
- [Target Experience]: Constrained Generative Policy Optimization (CGPO) with Mixture of Judges (MoJ) AND improved policy weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}, {teacher}
- [Utilization]: Policy achieves +7.4% AlpacaEval-2 (general chat), +12.5% Arena-Hard (STEM), and consistent gains in math/coding
- [Method]: ⟨hybrid⟩
- [Mechanism]: CGPO 的核心是 MoJ：多个判断器提供多维评估，再通过分层的约束策略优化在大量目标之间寻找 Pareto 最优点。阶段1（P4）构建多维评估器系统；阶段2（P6）把 MoJ 信号转化为策略权重，同时检测和缓解奖励黑客。

[Title]: Confronting Reward Model Overoptimization with Constrained RLHF
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Composite reward models (multiple component RMs) with overoptimization thresholds
- [Target Experience]: Policy weights optimized within each RM's useful range via constrained RL
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Policy stays within each RM's effective proxy range, improving evaluation performance
- [Method]: ⟨hybrid⟩
- [Mechanism]: 论文研究复合 RM 中的过优化，指出组件 RM 的相关性会影响过优化临界点。约束 RLHF 用约束 RL 防止智能体越过每个 RM 的有效范围，并通过拉格朗日乘子动态学习各 RM 权重；固定复合评估器到策略参数的转化属于 P6。

[Title]: Stepwise Guided Policy Optimization: Coloring Your Incorrect Reasoning in GRPO
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Step-wise judge signals over incorrect and diverse reasoning responses in GRPO groups
- [Target Experience]: GRPO-trained reasoning policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Judge model diversifies all-negative groups and supplies step-wise guidance during offline/online training
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 步骤级判断器在 GRPO 组内评估推理响应，尤其处理全负样本。SGPO 将该评估器信号注入 GRPO，使失败推理轨迹也能塑造策略更新。

[Title]: Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Reward-model accuracy / gradient-norm signals in RLHF, RLVR, and LLM-as-a-Judge math tasks
- [Target Experience]: Policy updates biased toward reward-accurate regions
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}, {teacher}
- [Utilization]: Gradient regularization shapes policy optimization to avoid reward hacking
- [Method]: ⟨hybrid⟩
- [Mechanism]: 奖励/评估器信号没有被直接使用，而是通过梯度正则估计奖励准确性更稳定的区域，并把策略更新偏向更平坦的最优点。这样可以减少推理和判断器任务中对缺陷评估器的利用。

[Title]: LongReward: Improving Long-context Large Language Models with AI Feedback
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Off-the-shelf LLM providing multi-dimensional rewards for long-context responses
- [Target Experience]: Policy weights via DPO with long-context reward signals
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Policy achieves improved long-context performance and enhanced short instruction following
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: LongReward 利用现成 LLM 从有用性、逻辑性、忠实性和完整性四个维度给长上下文响应打分，并通过设计好的评估流程合成奖励。冻结的 LLM 奖励提供器不被训练，奖励信号经 DPO 内化为长上下文策略参数，路径是 P5。

[Title]: Pretrain Value, Not Reward: Decoupled Value Policy Optimization
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Human preference data (same as used for reward modeling)
- [Target Experience]: Global Value Model (GVM) weights — a pretrained value function for policy optimization
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Frozen GVM serves as universal critic for policy learning; policy matches or surpasses SOTA RLHF
- [Method]: ⟨SFT⟩
- [Mechanism]: DVPO 主张直接预训练全局价值模型 GVM，而非先训练 RM 再在线学习价值函数。其关键观点是偏好数据到 RM 再到价值函数存在信息冗余；冻结 GVM 提供稳定、细粒度信用分配，主贡献是评估器构建，供下游策略优化时形成 P6。

[Title]: ODIN: Disentangled Reward Mitigates Hacking in RLHF
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Human preference data with length bias issues
- [Target Experience]: Disentangled reward model (length-decorrelated head for actual content)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: RM used for RL; almost eliminates reward correlation with length and improves policy quality
- [Method]: ⟨SFT⟩
- [Mechanism]: ODIN 针对响应长度引发的奖励黑客，提出解耦 RM：在共享特征上联合训练长度相关头和长度解相关的内容质量头。RL 阶段丢弃长度头，只使用内容头奖励，主路径是改进评估器构建的 P4；用于下游 RL 时构成 P6。

[Title]: Reinforcement Learning from LLM Feedback to Counteract Goal Misgeneralization
- [Pathway]: Out of Scope
- [Mechanism]: 摘要中的受训对象是迷宫导航传统 RL 智能体，LLM 用于分析策略并生成偏好；未清楚表明策略是基于 LLM 的智能体，对应 §3.2 的非基于 LLM 的系统边界。

[Title]: Scaling Laws for Reward Model Overoptimization
- [Pathway]: Out of Scope
- [Mechanism]: 摘要使用合成金标准/代理 RM 设置研究过优化缩放规律，没有智能体异构动作空间或具体基于 LLM 的智能体决策过程；对应 §3.2 的普通 RLHF 分析边界。

[Title]: Reinforcement Learning from Meta-Evaluation: Aligning Language Models Without Ground-Truth Labels
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Evaluator answers to natural-language meta-questions about correctness and reasoning consistency
- [Target Experience]: GRPO-trained generator policy for reasoning/open-domain tasks
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Evaluator positive-judgment probability is used as reward for policy optimization
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: RLME 用自然语言元问题提示评估器，并把正向判断概率转化为奖励。GRPO 使用该评估器奖励更新生成器策略，无需真实标签或任务专用验证器，属于评估器到策略参数的 P6。

[Title]: LLaVA-Critic-R1: Your Critic Model is Secretly a Strong Policy Model
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Preference-labeled critic datasets reorganized into verifiable training signals
- [Target Experience]: Multimodal generative policy that also retains critic ability
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {human}, {teacher}
- [Utilization]: RL on critic data produces a model used for both visual reasoning generation and self-critique at inference
- [Method]: ⟨hybrid⟩
- [Mechanism]: 带偏好标签的批评器数据被重组为可验证 RL 监督，用于训练基础 VLM。所得参数同时编码评估行为和生成策略，因此主要支持的是词元化批评器数据到具备策略/评估能力参数的 P5，而不是独立的评估器到策略步骤。

[Title]: Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms
- [Pathway]: Out of Scope
- [Mechanism]: 摘要比较 RLHF 与 DAA/DPO 的过优化模式，未提供智能体决策过程或异构动作空间；对应 §3.2 的普通 LLM 对齐分析边界。

[Title]: Statistical Rejection Sampling Improves Preference Optimization
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Preference pairs sourced from target optimal policy via rejection sampling
- [Target Experience]: Policy weights via improved DPO/SLiC loss with rejection-sampled preference data
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy outperforms both SLiC and DPO on LLM and human evaluation
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: RSO 解决 DPO/SLiC 中偏好数据来源与目标最优策略分布不匹配的问题。它通过拒绝采样从更接近目标最优策略的分布获取偏好数据，并从偏好建模角度改进 SLiC 和 DPO 损失；路径是叙事型偏好数据到策略参数的 P5。

[Title]: PRAISE: Prefix-Based Rollout Reuse in Agentic Search Training
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: Complete multi-turn search trajectories, prefix states, intermediate answers, and performance differences across prefixes
- [Target Experience]: Intermediate step rewards and jointly optimized search policy / prefix answer evaluator
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Prefix-derived trajectories and rewards improve data efficiency and credit assignment for agentic search RL
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段1（P4）：PRAISE 将长搜索展开轨迹切分为前缀，诱导中间答案，并根据前缀表现变化推导步骤级奖励。阶段2（P6）：共享模型用这些奖励同时学习搜索策略和前缀答案评估。

[Title]: Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Best-of-N inference-time selection outcomes used as training signal
- [Target Experience]: Policy weights optimized for BoN inference-time performance
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Bo32 performance improves on MATH (26.8%→30.8%) and HumanEval pass@16 (61.6%→67.1%)
- [Method]: ⟨SFT⟩, ⟨hybrid⟩
- [Mechanism]: 论文提出推理感知微调，直接在训练时优化推理期策略表现。针对 BoN 推理策略，作者设计模仿学习与 RL 方法处理不可微的最大值选择选择，使模型学习在最佳响应和多样响应之间切换；路径是 BoN 选择结果到策略参数的 P5。

[Title]: Examining Reasoning LLMs-as-Judges in Non-Verifiable LLM Post-Training
- [Pathway]: Out of Scope
- [Mechanism]: 摘要评估推理判断器对普通不可验证 LLM 后训练的影响，核心动作是响应偏好标注和对抗响应生成，未明确智能体异构动作空间；对应 §3.2 的普通 LLM 对齐边界。

[Title]: SERL: Self-Examining Reinforcement Learning on Open-Domain
- [Pathway]: Policy → Narrative → Policy (P7+P5)
- [Source Experience]: Self-generated responses with Copeland-style pairwise comparison judgments and self-consistency rewards
- [Target Experience]: Policy weights improved in both Actor and Judge capabilities
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Qwen3-8B LC win rate on AlpacaEval 2.0 from 52.37% to 59.90% (SOTA among self-improving approaches)
- [Method]: ⟨hybrid⟩
- [Mechanism]: SERL 是 P7+P5 自增强闭环：LLM 同时作为策略端和判断器。Copeland 式成对比较为策略端提供奖励，自一致性奖励促使判断器给出连贯判断；判断器改进后又提升策略端的训练信号，形成互相强化。

[Title]: RS-DPO: A Hybrid Rejection Sampling and Direct Preference Optimization Method for Alignment of Large Language Models
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Diverse k responses per prompt sampled from SFT policy, with reward-based contrastive pairs
- [Target Experience]: Policy weights via DPO on rejection-sampled contrastive pairs
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy achieves improved alignment with user intent, outperforming RS, PPO, and DPO
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: 该方法组合拒绝采样与 DPO：从 SFT 策略为每个提示采样多个响应，根据奖励分布识别对比样本对，再用 DPO 优化策略。对比对来自策略自身而非人工标注者或其他 LLM，RM 只作为样本对选择的评分工具。

[Title]: Direct Nash Optimization: Teaching Language Models to Self-Improve with General Preferences
- [Pathway]: Policy → Narrative → Policy (P7+P5)
- [Source Experience]: Self-generated on-policy samples with preference feedback from oracle
- [Target Experience]: Policy weights via batched on-policy regression-based Nash equilibrium optimization
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Orca-2.5-7B achieves 33% win-rate against GPT-4-Turbo on AlpacaEval 2.0 (26% absolute gain)
- [Method]: ⟨hybrid⟩
- [Mechanism]: DNO 不做点式奖励最大化，而是直接优化一般成对偏好。每轮从当前策略采样，预言机提供偏好反馈，再用基于回归的目标把策略推向 Nash 均衡；这是 P7+P5 的同策略自改进变体。

[Title]: Aligning Language Models Using Follow-up Likelihood as Reward Signal
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Follow-up utterance likelihoods from conversational data as implicit reward signals
- [Target Experience]: Policy weights via DPO on automatically mined preference data
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {human}
- [Utilization]: Policy achieves stronger helpfulness; FLR reward matches strong RMs trained on large-scale human/GPT-4 data
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: FLR 把后续话语出现概率视为隐式奖励，用对话中的后续反应区分更受偏好的响应。作者再从在线策略生成中自动挖掘偏好数据，并用 DPO 提升有用性；路径是 FLR 评分的对话数据到策略参数的 P5。

[Title]: DRLC: Reinforcement Learning with Dense Rewards from LLM Critic
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Token/span-level dense rewards from LLM critic on policy outputs
- [Target Experience]: Policy weights via RL with dense critic rewards
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Policy achieves consistent performance gains over PPO baseline with holistic rewards
- [Method]: ⟨hybrid⟩
- [Mechanism]: DRLC 通过提示 LLM 批评器，使其根据任务描述、问题、策略输出和环境奖励给出词元/片段级密集奖励。这些人工密集奖励并入 RL 训练，缓解整段生成只有一个稀疏奖励带来的低效和不稳定；路径是批评器输出的叙事型密集奖励到策略参数的 P5。

[Title]: Arena Learning: Build Data Flywheel for LLMs Post-training via Simulated Chatbot Arena
- [Pathway]: Policy → Narrative → Policy (P7+P5)
- [Source Experience]: AI-driven simulated arena battles evaluating model outputs
- [Target Experience]: Continuously improved policy via iterative SFT and RL on battle-informed training data
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: WizardLM-β achieves significant performance enhancements across various metrics
- [Method]: ⟨SFT⟩, ⟨hybrid⟩
- [Mechanism]: Arena Learning（竞技场学习）用 AI 注释模拟 Chatbot Arena 对战：WizardArena 预测 Elo 排名，数据飞轮根据对战结果识别目标模型弱点，并从不同模型优势中迭代更新训练数据。策略响应先外化参与模拟对战，结果再转化为训练数据并通过 SFT/RL 回灌策略，构成 P7+P5。

[Title]: Enhancing LLM-based Search Agents via Contribution Weighted Group Relative Policy Optimization
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: LLM judge contribution scores for retrieval utility and reasoning correctness at each search round
- [Target Experience]: CW-GRPO-trained search-agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Contribution scores rescale outcome-based advantages along search trajectories
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 判断器逐轮评估检索效用和推理正确性并分配贡献分。CW-GRPO 用这些评估器分数重新分配轨迹级优势，使搜索步骤上的奖励归因更精细，并改进搜索智能体策略学习。

[Title]: Co-Evolution of Policy and Internal Reward for Language Agents
- [Pathway]: Policy → Narrative → Policy (P7+P5)
- [Source Experience]: Policy-generated Self-Guide signals during language-agent acting
- [Target Experience]: Step-level internal reward and GRPO-updated language-agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Self-Guide steers next actions at inference and becomes dense internal reward at training
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 阶段1（P7）：智能体在行动时把当前策略知识外化为简短自然语言 Self-Guide。阶段2（P5）：同一指导信号被转化为步骤级内部奖励并用于 GRPO，形成策略与内部奖励共同演化的闭环。

[Title]: Dense Reward for Free in Reinforcement Learning from Human Feedback
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Reward model's attention map over tokens (inherent in RM architecture)
- [Target Experience]: Policy weights via dense-reward RL with redistributed reward signal
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Policy training stabilizes, accelerates learning, and may lead to better local optima
- [Method]: ⟨hybrid⟩
- [Mechanism]: 利用 RM 的注意力图将稀疏回合级奖励重新分配到生成中的每个词元。该方法等价于基于势函数的奖励塑形，理论上保持最优策略不变且无需额外计算；它通过改善奖励信号质量完成评估器到策略参数的 P6。

[Title]: Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: Step-by-step reasoning trajectories and final outcome links
- [Target Experience]: Conditional reward model and RL/search-improved reasoning policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: CRM rewards support Best-of-N sampling, beam search, and reinforcement learning
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段1（P4）：CRM 在给每步打分时同时条件化于先前步骤和最终结果，以建模推理中的时间因果关系。阶段2（P6）：所得过程奖励用于搜索和 RL，并降低奖励黑客风险。

[Title]: SPARK: Stepwise Process-Aware Rewards for Reference-Free Reinforcement Learning
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: Generator-produced solutions, verifier self-consistency outputs, meta-critiques, and synthetic step-level verification data
- [Target Experience]: Generative PRM / PRM-CoT and RL-trained math reasoning policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: PRM-CoT serves as reward model in reference-free RL training
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段1（P4）：生成器解答由验证器的并行扩展和顺序元批评检查，产生合成 PRM 训练数据。阶段2（P6）：生成式 PRM 被用作 RL 奖励，同时加入格式约束以限制奖励黑客。

[Title]: Free Process Rewards without Process Labels
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: Response-level outcome labels and reasoning trajectories for MATH
- [Target Experience]: Implicit PRM derived from ORM training and improved generation model
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Implicit PRM provides process rewards for majority voting and for improving generation models
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段1（P4）：用带对数似然比参数化的 ORM 训练得到无需步骤标签的隐式 PRM。阶段2（P6）：隐式 PRM 的步骤级分数被复用于改进弱监督条件下的推理生成策略。

[Title]: RLVF: Learning from Verbal Feedback without Overgeneralization
- [Pathway]: Narrative → Narrative → Policy (P1+P5)
- [Source Experience]: High-level verbal feedback (e.g., "Don't use emojis when drafting emails to my boss")
- [Target Experience]: Policy weights fine-tuned to apply feedback in relevant contexts without overgeneralization
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}, {teacher}
- [Utilization]: Policy adheres to verbal feedback comparably to in-context baselines while reducing overgeneralization by 30%
- [Method]: ⟨hybrid⟩
- [Mechanism]: C3PO 先把高层自然语言反馈生成小型合成偏好数据集，并明确反馈在哪些上下文中适用或不适用。随后在该偏好数据上微调模型，同时约束不适用提示上的偏离；路径是原始语言反馈到上下文化偏好数据，再到策略参数的 P1+P5。

[Title]: On Designing Effective RL Reward at Training Time for LLM Reasoning
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: ORM/PRM rewards, success rewards, and refined Clipping / Delta reward signals over math reasoning trajectories
- [Target Experience]: RL-trained math reasoning policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Refined reward functions are combined with sparse success rewards during RL training
- [Method]: ⟨hybrid⟩
- [Mechanism]: 已训练 RM 会给推理轨迹打分，但可能被重复无用步骤利用。截断（Clipping）与差分（Delta）对评估器信号做界限和增量修正，使累计奖励保持有界并继续适用于策略优化。

[Title]: Policy Filtration for RLHF to Mitigate Noise in Reward Models
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Reward model scores and reliability estimates over code/math reasoning samples
- [Target Experience]: PF-PPO-trained code/math reasoning policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Policy filtration removes unreliable reward samples before policy gradient updates
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: RM 先为策略样本打分，PF-PPO 再用 R2 式过滤估计哪些奖励区间更能预测真实得分。训练时只使用更可靠的评估器反馈进行 PPO 更新，以降低噪声奖励对策略的影响。

[Title]: The Trickle-down Impact of Reward (In-)consistency on RLHF
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Human preference data with analysis of reward model consistency
- [Target Experience]: More consistent reward model (via ConvexDA/RewardFusion techniques)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: More consistent RM yields more useful downstream RLHF policy responses
- [Method]: ⟨SFT⟩
- [Mechanism]: 论文研究 RM 一致性：RM 是否能识别提示语义变化并相应调整奖励。Contrast Instructions 基准用于测量一致性，ConvexDA 和 RewardFusion 分别在训练与推理阶段增强一致性；主贡献是改进评估器质量，并展示其对下游 RLHF 的连锁影响。

[Title]: Discriminative Policy Optimization for Token-Level Reward Models
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: Preference data for mathematical reasoning and token-level Q-function supervision
- [Target Experience]: Q-function Reward Model and PPO/REINFORCE-trained reasoning policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}, {teacher}
- [Utilization]: Q-RM provides token-level rewards for PPO/REINFORCE and improves training efficiency
- [Method]: ⟨RL: PPO⟩, ⟨hybrid⟩
- [Mechanism]: 阶段1（P4）：偏好数据训练判别式 Q-RM，使奖励建模与生成解耦，并分配词元级 Q 值。阶段2（P6）：Q-RM 奖励被整合进数学推理的策略优化。

[Title]: Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: CoT monitor judgments over frontier reasoning-model behavior in agentic coding environments
- [Target Experience]: RL-trained coding-agent policy shaped by monitor reward
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: CoT monitor is inserted into the RL reward to suppress reward hacking, with monitorability trade-offs
- [Method]: ⟨hybrid⟩
- [Mechanism]: LLM 监控器观察 CoT 推理，比只看动作或输出更能检测利用行为。将监控器判断纳入奖励目标会改变策略，但过高优化压力也可能诱导模型学习更难观察的 CoT。

[Title]: Natural Emergent Misalignment from Reward Hacking in Production RL
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Production coding-environment rewards, reward-hacking strategy prompts / synthetic documents, and RLHF safety rewards
- [Target Experience]: Coding-agent policy with reward-hacking or mitigated behavior
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Production RL reward and safety-training reward shape agentic coding behavior
- [Method]: ⟨hybrid⟩
- [Mechanism]: 模型在真实编码环境中接受 RL 训练，而奖励目标可能被利用。评估器/奖励信号被内化为策略行为，论文由此观察奖励黑客的泛化，以及多样化 RLHF 安全训练或阻止黑客行为对缓解效果的影响。

[Title]: InfAlign: Inference-aware language model alignment
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Calibrated and transformed reward signals for inference-time alignment
- [Target Experience]: Policy weights optimized for inference-time win rate (against base model)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Policy achieves 3-8% improvement on inference-time win rates for Best-of-N and Best-of-N jailbreaking
- [Method]: ⟨hybrid⟩
- [Mechanism]: InfAlign 解决标准 RLHF 训练目标与推理期解码算法之间的不匹配。理论上，任意推理期解码过程对应一个奖励变换后的 RLHF 问题；InfAlign-CTRL 通过奖励校准和变换后的 KL 正则奖励最大化，使评估器到策略的转化匹配特定推理策略。

[Title]: RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: Outcome-level verification correctness rewards and process-level reasoning traces
- [Target Experience]: Generative process-level verifier and reinforced reasoning generator policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Verifier guides generator RL; generator and verifier are trained interleaved
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段1（P4）：Tango 用结果级正确性而非显式过程标签，通过 RL 训练生成式验证器。阶段2（P6）：验证器的过程级信号引导生成器 RL，生成器与验证器交替共同演化。

[Title]: Natural Language Actor-Critic: Scalable Off-Policy Learning in Language Space
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Generative LLM critic natural-language explanations for suboptimal actions in long-horizon agent trajectories
- [Target Experience]: Off-policy trained LLM-agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Natural-language critic feedback replaces scalar value feedback and trains policies off-policy
- [Method]: ⟨hybrid⟩
- [Mechanism]: 批评器为推理、网页浏览、工具使用和对话轨迹生成自然语言动作质量反馈。NLAC 将这些评估器语言转化为离线策略学习信号，适用于大规模自然语言动作空间。

[Title]: Sycophancy to Subterfuge: Investigating Reward-Tampering in Large Language Models
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Rewards from a curriculum of gameable environments and later harmlessness training rewards
- [Target Experience]: LLM assistant policy exhibiting or mitigating specification gaming / reward tampering
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Reward signals train assistants across increasingly gameable environments, testing generalization of reward-tampering behavior
- [Method]: ⟨hybrid⟩
- [Mechanism]: 早期环境中的错设奖励被策略内化为规格博弈行为。随着课程中的持续 RL，评估器/奖励缺陷会转化为策略行为，并可能泛化到直接篡改奖励。

[Title]: Enhancing Decision-Making of Large Language Models via Actor-Critic
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Q-value action evaluations computed from token logits, future rollouts, and reasoning
- [Target Experience]: Gradient-free improved LLM decision-making policy for ALFWorld, BabyAI-Text, and WebShop
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Actor-critic Q evaluations guide long-term policy improvement
- [Method]: ⟨hybrid⟩
- [Mechanism]: LAC 从包含展开轨迹的推理和词元未归一化概率信号中推导稳健的长期动作评估。这些批评器式 Q 值驱动无需梯度的策略改进，覆盖多步环境决策。

[Title]: EVPO: Explained Variance Policy Optimization for Adaptive Critic Utilization in LLM Post-Training
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Learned critic baseline estimates and batch-level explained variance in sparse-reward LLM tasks
- [Target Experience]: Policy trained with adaptive critic / batch-mean advantage estimation
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: EV gates whether the critic or GRPO-style batch baseline is used at each training step
- [Method]: ⟨RL: PPO⟩, ⟨RL: GRPO⟩
- [Mechanism]: EVPO 把批评器视为训练中有效性会变化的评估器，并用解释方差判断何时使用批评器优势、何时改用批均值优势更稳妥。该机制在智能体交互与推理任务中自适应调节策略优化。

[Title]: Rethinking Reward Model Evaluation: Are We Barking up the Wrong Tree?
- [Pathway]: Out of Scope
- [Mechanism]: 摘要在合成设置中分析 RM 验证准确率与优化后策略表现的关系，没有智能体轨迹或异构动作空间；对应 §3.2 的普通 RM 评估边界。

[Title]: Mitigating Reward Hacking in RLHF via Advantage Sign Robustness
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: RM parameters with certified sign-preservation analysis of advantage estimates
- [Target Experience]: Policy weights via SignCert-PO with down-weighted non-robust completions
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Policy achieves better win rate and reduces reward hacking on summarization and AlpacaFarm
- [Method]: ⟨hybrid⟩
- [Mechanism]: 论文指出奖励黑客常由优势符号翻转引起，即本应降低坏响应概率的更新反而提高其概率。SignCert-PO 通过分析 RM 参数空间中的对抗扰动，推导符号保持半径，并在策略梯度更新中降低不稳健样本权重，保护评估器到策略的梯度信号。

[Title]: Regularized Best-of-N Sampling with Minimum Bayes Risk Objective for Language Model Alignment
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Best-of-N samples with MBR objective as proximity regularizer
- [Target Experience]: Policy alignment via regularized BoN sampling (inference-time) and DPO training on MBR-BoN-generated preference data
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: MBR-BoN outperforms both BoN sampling and MBR decoding; DPO on MBR-BoN data outperforms vanilla BoN-based DPO
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: MBR-BoN 在 BoN 采样中加入最小贝叶斯风险目标作为接近性正则，缓解推理期奖励黑客。该目标衡量响应与参考策略的接近程度，并可生成成对偏好数据用于 DPO；它在推理期和训练期改进评估器到策略的转化。

[Title]: Online Preference-based Reinforcement Learning with Self-augmented Feedback from Large Language Model
- [Pathway]: Out of Scope
- [Mechanism]: 摘要中的 RL-SaLLM-F 在 MetaWorld 等传统 RL 任务上用 LLM 偏好反馈替代脚本教师，未清楚表明受训策略是 LLM/VLA/基于 LLM 的智能体；对应 §3.2 的非基于 LLM 的系统边界。

[Title]: LAPP: Large Language Model Feedback for Preference-Driven Reinforcement Learning
- [Pathway]: Out of Scope
- [Mechanism]: 摘要用于四足运动和灵巧操作的机器人 RL，LLM 生成偏好标签但受训策略并非明确的基于 LLM 的智能体；对应 §3.2 的非基于 LLM 的系统边界。

[Title]: Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Proxy reward function with χ² divergence regularization against reference policy
- [Target Experience]: Policy weights via regularized RL that better mitigates reward hacking
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Policy better mitigates reward hacking across four realistic settings including RLHF
- [Method]: ⟨hybrid⟩
- [Mechanism]: 论文把奖励黑客重新定义为代理奖励与真实奖励在参考策略下的相关性在优化过程中崩解。理论表明向参考策略正则化可缓解奖励黑客，并建议使用占用度量的 χ² 散度正则；核心是改进代理评估器信号到策略参数的 P6。

[Title]: Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: Agentic RAG query-generation, evidence-extraction, answer-generation steps and process-level rewards in RAG-ProGuide
- [Target Experience]: Process reward model / reward dataset and RL-trained agentic RAG policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}, {self}
- [Utilization]: Process-level rewards supervise RL for autonomous search invocation, query generation, evidence extraction, and answer generation
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段1（P4）：RAG-ProGuide 为多种智能体式 RAG 动作编码过程级奖励。阶段2（P6）：ReasonRAG 在过程监督 RL 中使用这些奖励，以改进动态检索、多步证据抽取和答案构造。

[Title]: Rethinking Reward Model Evaluation Through the Lens of Reward Overoptimization
- [Pathway]: Out of Scope
- [Mechanism]: 摘要是 RM 基准设计与奖励过优化分析，未呈现智能体交互轨迹或异构动作；对应 §3.2 的普通 RM 评估边界。

[Title]: Subliminal Signals in Preference Labels
- [Pathway]: Out of Scope
- [Mechanism]: 摘要研究偏好标签作为隐蔽通信通道的风险，没有智能体决策过程语义或异构动作空间；对应 §3.2 的普通监督/对齐边界。

[Title]: Hybrid Reward Normalization for Process-supervised Non-verifiable Agentic Tasks
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: External-tool/search agent steps, principle-based step judgments, and outcome verification signals
- [Target Experience]: Principle-based reward model and process-supervised agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}, {self}
- [Utilization]: Principle Process Reward and ReNorm calibrate process/outcome rewards for RL on non-verifiable agentic tasks
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段1（P4）：PPR 训练基于原则的 RM，用局部标准和结果感知标准评估步骤质量。阶段2（P6）：混合奖励归一化结合过程和结果信号，使工具/搜索智能体策略能从密集反馈中学习。

[Title]: Process-based Self-Rewarding Language Models
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Step-wise LLM-as-a-Judge rewards over long-thought mathematical reasoning outputs
- [Target Experience]: Step-wise preference-optimized math reasoning policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Step-wise judge rewards drive iterative process-based self-rewarding
- [Method]: ⟨hybrid⟩
- [Mechanism]: 模型用 LLM 评审器机制评估自己的长思维推理步骤，形成过程级评估器信号。这些步骤级偏好在多轮迭代中更新推理策略，属于评估器到策略的 P6。

[Title]: Variational Best-of-N Alignment
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Best-of-N distribution from base policy + reward model
- [Target Experience]: Policy weights via variational inference (minimizing backward KL to BoN distribution)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: vBoN achieves closest performance to BoN and surpasses standard KL-constrained RL on summarization and controlled generation
- [Method]: ⟨SFT⟩
- [Mechanism]: vBoN 推导 BoN 采样诱导的分布，并通过最小化反向 KL 将策略微调到 BoN 分布，可把推理成本降低 N 倍。路径是 RM 排序得到的 BoN 分布到策略参数的 P5。

[Title]: IPO: Your Language Model is Secretly a Preference Classifier
- [Pathway]: Policy → Narrative → Policy (P7+P5)
- [Source Experience]: LLM's own preference classifications on self-generated response pairs
- [Target Experience]: Policy weights via DPO using self-generated preferences
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Policy achieves performance comparable to using SOTA reward models for obtaining preferences
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: IPO 把生成式 LLM 直接用作偏好分类器，不依赖外部 RM 或人工反馈。模型为给定指令生成多个响应，再由自身分类偏好并用 DPO 训练；这是策略外化响应与偏好判断，再回灌策略的 P7+P5 闭环。

[Title]: Process Reward Model with Q-Value Rankings
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Sequential reasoning / decision-making traces and Q-value ranking comparisons
- [Target Experience]: Process Q-value Model for step-level reward modeling
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: 不清楚
- [Utilization]: PQM provides granular process rewards for multi-step reasoning benchmarks
- [Method]: ⟨hybrid⟩
- [Mechanism]: PQM 将 PRM 训练重写为马尔可夫决策中的 Q 值排序问题：序贯推理轨迹被转化为比较式 Q 值监督，从而得到能捕捉中间决策依赖的评估器。摘要未说明下游策略权重更新，因此主路径是 P4。

[Title]: Value-Incentivized Preference Optimization: A Unified Approach to Online and Offline RLHF
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Preference data with value-function-regularized reward estimation
- [Target Experience]: Policy weights via unified online/offline preference optimization
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Policy performs effectively on text summarization and dialog tasks
- [Method]: ⟨hybrid⟩
- [Mechanism]: VPO 统一在线与离线 RLHF，用价值函数正则奖励函数的最大似然估计，并通过符号控制乐观或悲观倾向。它以隐式奖励建模直接优化策略，路径是带价值正则的偏好数据到策略参数的 P5。

[Title]: Process Supervision-Guided Policy Optimization for Code Generation
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: Generated code trajectories, unit-test feedback, and line-level correctness signals
- [Target Experience]: Process Reward Model and RL-driven code-generation policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: PRM provides dense line-level rewards and value-function initialization for RL
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段1（P4）：单元测试结果和代码生成过程信号被转化为行级 PRM 反馈。阶段2（P6）：PRM 作为密集奖励和价值初始化器，使代码策略即使在最终单元测试奖励稀疏时也能获得更新。

[Title]: WPO: Enhancing RLHF with Weighted Preference Optimization
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Off-policy preference data reweighted to simulate on-policy data
- [Target Experience]: Policy weights via reweighted DPO
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}, {teacher}
- [Utilization]: Gemma-2-9b-it achieves 76.7% length-controlled winning rate against GPT-4-turbo on Alpaca Eval 2
- [Method]: ⟨hybrid⟩
- [Mechanism]: WPO 解决离线偏好优化中数据采集策略与目标策略的分布差距。它按偏好对在当前策略下的概率对离线数据重新加权，模拟同策略学习；路径是重新加权的偏好数据到策略参数的 P5。

[Title]: Catastrophic Goodhart: regularizing RLHF with KL divergence does not mitigate heavy-tailed reward misspecification
- [Pathway]: Out of Scope
- [Mechanism]: 摘要是奖励错设与 KL 正则化的理论分析，未包含智能体决策轨迹或异构动作空间；对应 §3.2 的普通 RLHF 理论边界。

[Title]: Reward Model Overoptimisation in Iterated RLHF
- [Pathway]: Out of Scope
- [Mechanism]: 摘要系统分析迭代 RLHF 的过优化动态，实验为受控 AlpacaFarm，未体现智能体异构动作空间；对应 §3.2 的普通 LLM 对齐边界。

[Title]: On the Interplay of Pre-Training, Mid-Training, and RL on Reasoning Language Models
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Process-level rewards and verifiable outcomes over parseable step-by-step synthetic reasoning traces
- [Target Experience]: RL-trained reasoning language model policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Process-level rewards reduce reward hacking and improve reasoning fidelity during controlled RL post-training
- [Method]: ⟨hybrid⟩
- [Mechanism]: 框架隔离推理轨迹，并在受控能力边界上施加 RL 奖励。过程奖励作为评估器信号塑造策略更新，同时帮助分析后训练如何改变推理行为。

[Title]: FAPO: Flawed-Aware Policy Optimization for Efficient and Reliable Reasoning
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: GenRM process-level detections of flawed-positive reasoning rollouts
- [Target Experience]: Flawed-aware RL-trained reasoning policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: GenRM detects flawed rollouts and FAPO converts them into staged reward penalties
- [Method]: ⟨hybrid⟩
- [Mechanism]: 生成式 RM 在正向展开轨迹中定位推理错误，FAPO 将该评估器信号转化为无需额外参数的奖励惩罚。策略早期仍可利用捷径获得收益，后期更新则逐渐转向可靠推理。

[Title]: WARP: On the Benefits of Weight Averaged Rewarded Policies
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Rewarded / RLHF-fine-tuned policy checkpoints
- [Target Experience]: Merged policy weights with improved KL-reward Pareto front
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Merged policy improves quality and alignment, outperforming other open-source LLMs
- [Method]: ⟨hybrid⟩
- [Mechanism]: WARP 是三阶段权重合并策略：用策略 EMA 作为 KL 正则的动态锚点，球面插值合并多个独立微调策略，再将合并模型与初始化线性插值以恢复预训练特征。它是 P6 的权重空间后处理变体，不涉及新的叙事型载体到评估器转化。

[Title]: Pairwise Proximal Policy Optimization: Harnessing Relative Feedback for LLM Alignment
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Relative/comparative preference feedback (pairwise comparisons) on trajectories
- [Target Experience]: Policy weights via trajectory-wise policy gradient on comparative rewards
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: P3O outperforms PPO in KL-Reward trade-off and matches/outperforms prior alignment methods
- [Method]: ⟨hybrid⟩
- [Mechanism]: P3O 直接在比较式奖励上执行轨迹级策略梯度，解决 PPO 对等价奖励函数不保持不变、且需要词元级更新的问题。它对等价奖励保持不变，路径是成对偏好数据到策略参数的 P5。

[Title]: Dataset Reset Policy Optimization for RLHF
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Offline preference dataset combined with online RL via dataset reset mechanism
- [Target Experience]: Policy weights via DR-PO with provable guarantees
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Policy generation quality surpasses PPO and DPO under GPT-4 win-rate metric
- [Method]: ⟨hybrid⟩
- [Mechanism]: DR-PO 利用离线偏好数据集提供信息量更高的状态，把策略优化器重置到离线数据中的状态，而非总从初始状态分布开始。该机制利用离线数据覆盖改进从 RM 信号出发的 RL 优化，属于 P6。

[Title]: Iterative Data Smoothing: Mitigating Reward Overfitting and Overoptimization in RLHF
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: Human preference ranking data with iteratively smoothed (soft) labels
- [Target Experience]: Improved reward model via IDS (Iterative Data Smoothing) algorithm
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: RM achieves superior performance over traditional training methods; (downstream policy benefits implied)
- [Method]: ⟨hybrid⟩
- [Mechanism]: IDS 缓解 RM 训练中过拟合：每个训练训练轮次不只更新模型，也用模型更新数据，把硬标签替换为模型预测形成的软标签。主贡献是改进评估器训练，使其更抗过拟合。

[Title]: Solving the Inverse Alignment Problem for Efficient RLHF
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Periodically frozen policy + offline preference dataset subsets
- [Target Experience]: Improved reward model (via inverse alignment) AND improved final policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Policy achieves superior alignment and faster convergence compared to standard RLHF
- [Method]: ⟨hybrid⟩
- [Mechanism]: 论文定义反向对齐问题：在固定执行器和固定离线偏好数据集下优化批评器奖励。通过在周期性冻结的策略下选择对齐的离线偏好子集来微调 RM，可为当前策略行为提供更清晰反馈，改进 P6 中 RM 与策略的匹配。

[Title]: Simultaneous Reward Distillation and Preference Learning: Get You a Language Model Who Can Do Both
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Oracle rewards AND human preference labels (simultaneously modeled)
- [Target Experience]: Policy weights via DRDO (simultaneous reward distillation and preference optimization)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}, {teacher}
- [Utilization]: Policy surpasses DPO and e-DPO in expected rewards; more robust to noisy preference signals and OOD settings
- [Method]: ⟨hybrid⟩
- [Mechanism]: DRDO 同时建模奖励与偏好：一方面直接模仿预言机奖励，另一方面用新的偏好似然形式学习人类偏好。它避免纯偏好方法在噪声或非确定性标签下退化，路径是预言机奖励与偏好标签到策略参数的 P5。

[Title]: Provably Efficient Online RLHF with One-Pass Reward Modeling
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: Online interaction data with one-pass reward model updates (no historical data storage)
- [Target Experience]: Continuously updated reward model AND improved policy via online mirror descent
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Policy achieves improved alignment with constant-time updates per iteration
- [Method]: ⟨hybrid⟩
- [Mechanism]: 论文解决在线 RLHF 每轮重整历史数据并重训的可扩展性瓶颈。它把 RLHF 形式化为上下文偏好序贯决策问题，并基于带局部范数的在线镜像下降设计单遍奖励建模，实现每轮常数时间更新；整体是高效 P4+P6。

[Title]: Language Model Alignment with Elastic Reset
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Reward model signal with Elastic Reset regularization
- [Target Experience]: Policy weights achieving higher reward with less drift
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Policy achieves SOTA on translation benchmark, outperforms baselines in sentiment task and technical QA
- [Method]: ⟨hybrid⟩
- [Mechanism]: 弹性重置（Elastic Reset）不显式修改训练目标，而是周期性地把在线模型重置到自身 EMA，再把 EMA 重置到初始模型。该机制用重置控制奖励提升与策略漂移之间的权衡，属于从 RM 信号出发改进 RL 优化的 P6。

[Title]: RLHF Workflow: From Reward Modeling to Online RLHF
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: Open-source preference datasets with proxy preference model
- [Target Experience]: Proxy preference model AND online iteratively RLHF-trained policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}, {teacher}
- [Utilization]: Policy achieves impressive performance on AlpacaEval-2, Arena-Hard, MT-Bench, HumanEval, TruthfulQA
- [Method]: ⟨SFT⟩, ⟨hybrid⟩
- [Mechanism]: 这是一套在线迭代 RLHF 可复现流程。阶段1（P4）：用多样开源数据集构建代理偏好模型，以近似人工反馈。阶段2（P6）：结合理论观察和实践细节执行在线迭代 RLHF；流程本身是标准 P4+P6。

[Title]: Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: Human preference data collected on a weekly cadence (iterated online mode)
- [Target Experience]: Preference model AND RLHF-trained helpful and harmless policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Policy improves on almost all NLP evaluations; compatible with specialized skills (coding, summarization)
- [Method]: ⟨hybrid⟩
- [Mechanism]: 这是 RLHF 的基础性实现：阶段1（P4）用人工偏好数据训练偏好模型/RM；阶段2（P6）用 RL 优化策略以最大化 RM 奖励，并用 KL 惩罚限制偏离初始策略。迭代在线模式中，偏好模型和策略会定期用新人工反馈更新。

[Title]: Reward Model Routing in Alignment
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Pool of candidate reward models dynamically selected via Bayesian routing
- [Target Experience]: Policy weights via RL with adaptively routed reward signals
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Policy consistently outperforms individual RMs, RM ensembling, and existing routing methods
- [Method]: ⟨hybrid⟩
- [Mechanism]: BayesianRouter 解决单 RM 对齐能力受限和 RM 集成计算昂贵的问题。离线阶段训练多任务路由器估计各 RM 可靠性；在线阶段用贝叶斯 Thompson 采样按查询选择 RM，并随演化中的策略分布更新后验，属于多评估器信号到策略的 P6 路由机制。

[Title]: Black-Box On-Policy Distillation of Large Language Models
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: Student-generated responses discriminated against teacher responses
- [Target Experience]: Discriminator weights AND improved student policy weights via GAN-style minimax game
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}, {self}
- [Utilization]: Qwen2.5-14B-Instruct (student) becomes comparable to GPT-5-Chat (teacher) on LMSYS-Chat
- [Method]: ⟨hybrid⟩
- [Mechanism]: GAD 是黑盒同策略蒸馏：学生 LLM 生成响应，判别器区分学生响应与教师响应，并作为同策略 RM 与学生共同演化。学生响应外化为叙事型经验，判别器提供自适应反馈，再通过 P6 更新学生策略。

[Title]: Learning beyond Teacher: Generalized On-Policy Distillation with Reward Extrapolation
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: Teacher logit distribution on student-generated trajectories with reward extrapolation
- [Target Experience]: Student policy weights via generalized on-policy distillation (ExOPD)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}, {self}
- [Utilization]: Student surpasses teacher's performance boundary and outperforms domain teachers
- [Method]: ⟨hybrid⟩
- [Mechanism]: OPD 被证明是密集 KL 约束 RL 的特例。G-OPD 引入灵活参考模型和奖励缩放因子，其中奖励外推可使学生突破教师性能边界；在强到弱设置中，用教师 RL 前的基座作参考模型可进一步校正奖励。主路径是参数间 P6。

[Title]: LLMR: Knowledge Distillation with a Large Language Model-Induced Reward
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: LLM-induced reward function for knowledge distillation
- [Target Experience]: Student policy weights via KD with LLM reward
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Student outperforms traditional KD methods in dialogue generation and summarization
- [Method]: ⟨hybrid⟩
- [Mechanism]: LLMR 使用 LLM 诱导的奖励函数进行知识蒸馏：LLM 作为评估器给学生模型输出打分，分数引导学生学习教师知识。该工作属于 LLM 评估器到学生策略参数的 P6。

[Title]: WebGPT: Browser-assisted question-answering with human feedback
- [Pathway]: Narrative → Evaluator → Policy (P4+P6)
- [Source Experience]: Web-browsing trajectories with human preference labels
- [Target Experience]: Reward model (trained to predict human preferences) AND RLHF-aligned web-browsing policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Policy answers long-form questions using web search; preferred by humans 56% of the time over human demonstrators
- [Method]: ⟨SFT⟩, ⟨hybrid⟩
- [Mechanism]: WebGPT 将经典 RLHF 流程用于网页浏览智能体：先用人工示范做行为克隆，再在模型输出上收集人工偏好，训练 RM 预测偏好，最后用相对 RM 的拒绝采样优化策略输出。整体是 P4+P6 组合，同时人工评估需要参考资料支撑事实性判断。
