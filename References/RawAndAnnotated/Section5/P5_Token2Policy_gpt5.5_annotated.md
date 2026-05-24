[Title]: WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning
- [Pathway]: Policy → Narrative → Policy
- [Source Experience]: current open-model web-agent policy rollouts, unsuccessful attempts, generated curriculum tasks, and outcome feedback
- [Target Experience]: ORM-guided open Llama-3.1 / GLM-4 web-agent policy weights
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: ORM supplies robust outcome supervision and adaptive RL updates internalize web task experience into open-model web agents.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段 1 对应 P7/P1：当前网页智能体策略产生在线交互轨迹，并把失败尝试转化为新的课程任务。阶段 2 对应 P5：自适应 RL 利用任务结果和 ORM 信号更新开源模型策略；摘要明确提到的 ORM 构建属于次要的叙事载体→评估器分支。

[Title]: WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: asynchronously generated web-environment interaction trajectories with binary task-success rewards
- [Target Experience]: Qwen-2.5-3B and Llama-3.1-8B web-agent policy weights
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Online multi-turn trajectories are used as RL feedback to improve web navigation and decision making.
- [Method]: ⟨RL: unspecified⟩
- [Mechanism]: 智能体直接与网页环境进行多轮交互，采样多样化轨迹，依据二元成功奖励端到端更新 LLM 策略；行为克隆只作为预热或初始化变体出现。
> New tag: ⟨RL: unspecified⟩ — 用于 abstract 只说明 RL / online RL / RLVR / policy optimization，但未给出可归入 PPO、GRPO、DPO、ReST 的具体算法时的泛化方法标签。

[Title]: SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from Experience
- [Pathway]: Policy → Narrative → Policy
- [Source Experience]: CUA policy exploration rollouts, trial-and-error software trajectories, failure actions, successful rollouts, and specialist-agent experiential insights
- [Target Experience]: stronger generalist computer-use agent policy weights
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Step-wise assessment and curriculum-generated tasks supply training feedback; failure actions and successful trajectories are internalized through imitation and GRPO.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段 1 对应 P7/P1：CUA 自主探索陌生软件，产生试错轨迹，并把任务组织为由易到难的课程；世界状态模型与课程生成器是次要的评估/课程分支。阶段 2 对应 P5：失败动作支持对抗模仿，成功轨迹支持 GRPO，专家洞察被内化为通用 CUA 策略。

[Title]: ARPO:End-to-End Policy Optimization for GUI Agents with Experience Replay
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: successful GUI-agent interaction trajectories retained in a replay buffer
- [Target Experience]: vision-language GUI-agent policy weights
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Successful experiences are replayed across training iterations and paired with task selection to stabilize GUI RL.
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: ARPO 在 GRPO 中加入成功多轮 GUI 轨迹的经验回放；任务过滤选择信息量更高的交互，轨迹奖励随后更新长程计算机任务策略。

[Title]: ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL
- [Pathway]: Narrative → Evaluator → Policy
- [Source Experience]: multi-turn agent utterance/action trajectories with delayed rewards
- [Target Experience]: fine-tuned LLM agent token policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: High-level value estimates aggregate multi-turn rewards and guide token-level policy training.
- [Method]: ⟨RL: PPO⟩, ⟨hybrid⟩
- [Mechanism]: 阶段 1 对应 P4：轨迹奖励被压缩为高层离策略价值函数。阶段 2 对应 P6：该价值信号训练每个话语/回合内的低层词元策略，把单轮 RL 扩展到智能体任务。

[Title]: RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning
- [Pathway]: Policy → Narrative → Policy
- [Source Experience]: current LLM-agent policy rollouts, trajectory filters, critic signals, and environment feedback
- [Target Experience]: StarPO / StarPO-S trained LLM agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Trajectory filtering, critic incorporation, and stabilized gradient updates improve multi-turn agent self-evolution.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段 1 对应 P7：当前 LLM 智能体策略生成多轮轨迹。阶段 2 对应 P5：StarPO/StarPO-S 将这些轨迹反馈给策略优化，并通过轨迹过滤、价值评估器引入和梯度稳定化缓解 Echo Trap。

[Title]: Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents
- [Pathway]: Policy → Narrative → Policy
- [Source Experience]: successful and unsuccessful MCTS-guided web-agent trajectories with self-critique
- [Target Experience]: iteratively fine-tuned autonomous web-agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Collected trajectories are converted into preference-style training data for off-policy DPO.
- [Method]: ⟨MCTS⟩, ⟨RL: DPO⟩
- [Mechanism]: 阶段 1 对应 P7：当前 LLM 策略在 MCTS 与自我批评引导下产生交互轨迹。阶段 2 对应 P5：成功与失败轨迹为迭代式离策略 DPO 更新提供偏好证据。

[Title]: DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Android device-control trajectories, static human demonstrations, online interactions, and evaluator feedback
- [Target Experience]: RL-fine-tuned VLM device-control policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {human}
- [Utilization]: Offline RL initializes the model, then offline-to-online RL uses evaluator-backed interaction feedback to adapt the policy to real GUI stochasticity.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 静态示范和在线 Android 交互由基于 VLM 的评估器打分；摘要没有说明该评估器由轨迹训练得到，因此主转化是轨迹/反馈经验通过离线到在线 RL 内化为 VLM 策略。

[Title]: Grounding Large Language Models in Interactive Environments with Online Reinforcement Learning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: interactive textual-environment trajectories and online rewards
- [Target Experience]: functionally grounded FLAN-T5 policy variants
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Online RL updates the LLM policy so its decisions align with environment dynamics.
- [Method]: ⟨RL: unspecified⟩
- [Mechanism]: GLAM 将 LLM 视为策略，让它与文本空间/导航环境交互，并用在线奖励反馈逐步更新模型参数。

[Title]: Reinforcement Learning for Long-Horizon Interactive LLM Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: AppWorld API-call trajectories with stateful environment observations and rewards
- [Target Experience]: LOOP-trained interactive digital agent policy weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Environment rewards from direct API interactions train IDAs to consult documentation, recover from errors, and reduce confabulation.
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: LOOP 将有状态的多应用交互形式化为 POMDP，并用节省显存的 PPO 变体把 API 调用轨迹和延迟奖励转化为策略更新。

[Title]: Direct Multi-Turn Preference Optimization for Language Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: preferred and dispreferred multi-turn agent trajectories
- [Target Experience]: LLM agent policy optimized with DMPO loss
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: 不清楚
- [Utilization]: Preference trajectories are used to directly optimize multi-turn agent policies while accounting for occupancy and length.
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: DMPO 将 DPO 改造到多轮任务上，用状态-动作占用度量约束替代原策略约束，并加入长度归一化来建模偏好。

[Title]: Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents
- [Pathway]: Policy → Narrative → Policy
- [Source Experience]: exploration failure trajectories and contrastive trajectory preference pairs
- [Target Experience]: DPO-updated open LLM agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Failure-derived contrastive pairs guide iterative policy updates.
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: 阶段 1 对应 P7：智能体探索任务并产生失败轨迹。阶段 2 对应 P5：失败轨迹与更优轨迹被配对为偏好样本，并通过对比式/DPO 风格优化更新策略。

[Title]: Group-in-Group Policy Optimization for LLM Agent Training
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: complete multi-turn trajectories and repeated-state action groups
- [Target Experience]: GiGPO-trained LLM agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Episode-level and step-level relative advantages supply fine-grained RL feedback.
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: GiGPO 同时按完整轨迹构造宏观优势、按重复状态构造微观优势，并用这些信号在不增加辅助模型或额外轨迹的情况下更新策略。

[Title]: OpenWebVoyager: Building Multimodal Web Agents via Iterative Real-World Exploration, Feedback and Optimization
- [Pathway]: Policy → Narrative → Policy
- [Source Experience]: current multimodal web-agent exploration trajectories, imitation trajectories, and model-judged feedback
- [Target Experience]: iteratively optimized multimodal web-agent policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {human}, {teacher}
- [Utilization]: Well-performing trajectories judged by another model are reused for iterative policy improvement.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段 1 对应 P7：经过模仿学习后，当前多模态网页智能体探索开放网页并产生轨迹。阶段 2 对应 P5：另一个模型判断轨迹质量，被筛选出的高表现轨迹用于策略优化，并反复执行探索-反馈-优化循环。

[Title]: AutoWebGLM: A Large Language Model-based Web Navigating Agent
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: hybrid human-AI web browsing data and self-bootstrapped navigation trajectories
- [Target Experience]: AutoWebGLM web-navigation policy weights
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {human}, {teacher}, {self}
- [Utilization]: Curriculum training, rejection sampling, and RL internalize webpage comprehension, browser operation, and task decomposition skills.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 人机网页浏览轨迹用于课程训练；随后 RL 与拒绝采样继续把额外成功行为自举到模型策略中。

[Title]: Large Language Models Can Self-Improve At Web Agent Tasks
- [Pathway]: Policy → Narrative → Policy
- [Source Experience]: synthetic web-agent training data generated by the model itself
- [Target Experience]: fine-tuned WebArena agent model
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Self-generated data mixtures are used for fine-tuning to improve long-horizon web task completion.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P7：基础 LLM 智能体生成合成网页交互轨迹。阶段 2 对应 P5：这些轨迹被用于微调同类智能体模型，从而实现自我改进。

[Title]: WebDancer: Towards Autonomous Information Seeking Agency
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: browsing data, sampled information-seeking trajectories, and RL feedback
- [Target Experience]: ReAct-style WebDancer information-seeking agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Trajectories support SFT cold start and RL generalization for multi-step research tasks.
- [Method]: ⟨SFT⟩, ⟨RL: unspecified⟩
- [Mechanism]: 该流程构造浏览数据、采样轨迹、进行冷启动微调，再通过 RL 让策略内化自主信息检索行为。

[Title]: STeCa: Step-level Trajectory Calibration for LLM Agent Learning
- [Pathway]: Narrative → Narrative → Policy
- [Source Experience]: exploratory trajectories with suboptimal actions, step-level reward comparisons, and successful trajectories
- [Target Experience]: policy trained on calibrated and successful trajectories
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Calibrated trajectories are reused as training data for reinforced agent learning.
- [Method]: ⟨LLM-extract⟩, ⟨hybrid⟩
- [Mechanism]: 阶段 1 对应 P1：逐步奖励比较定位次优动作，并由 LLM 反思构造改进后的校准轨迹。阶段 2 对应 P5：校准轨迹和成功轨迹共同训练智能体策略。

[Title]: Advancing Tool-Augmented Large Language Models: Integrating Insights from Errors in Inference Trees
- [Pathway]: Schematic → Policy (P5)
- [Source Experience]: tree-like expert trajectories containing successful paths and failed explorations
- [Target Experience]: TP-LLaMA tool-use policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Successful paths provide SFT data; failed branches provide step-wise preference data for DPO.
- [Method]: ⟨SFT⟩, ⟨RL: DPO⟩
- [Mechanism]: 决策树轨迹被切分为成功专家路径和失败分支；SFT 模仿成功工具使用轨迹，DPO 则内化由失败探索得到的偏好。

[Title]: Solving the Granularity Mismatch: Hierarchical Preference Learning for Long-Horizon LLM Agents
- [Pathway]: Narrative → Schematic → Policy
- [Source Experience]: expert trajectories, semantically coherent action groups, and contrasting suboptimal groups
- [Target Experience]: HPL-optimized LLM agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Multi-granularity preference signals train the agent from trajectory-, group-, and step-level evidence.
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: 阶段 1 对应 P2：专家轨迹被分解为结构化动作组，并在课程设置下与对照动作组配对。阶段 2 对应 P5：层次化 DPO 损失把这些偏好内化到策略中。

[Title]: SPA-RL: Reinforcing LLM Agents via Stepwise Progress Attribution
- [Pathway]: Narrative → Evaluator → Policy
- [Source Experience]: multi-step task trajectories with final task-completion rewards and grounded action signals
- [Target Experience]: RL-trained LLM agent policy with intermediate reward guidance
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: A progress estimator redistributes final rewards into per-step contributions for policy optimization.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段 1 对应 P4：训练进展估计器，使逐步贡献能够累积到最终结果。阶段 2 对应 P6：估计出的逐步进展和动作落地信号作为密集奖励训练策略。

[Title]: ToolRL: Reward is All Tool Learning Needs
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: tool selection/application trajectories with reward strategies of varying granularity and dynamics
- [Target Experience]: GRPO-trained tool-use LLM policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: 不清楚
- [Utilization]: Reward design supplies RL feedback for tool-use capability and generalization.
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 该工作研究工具选择和工具应用中的奖励信号，并用原则化奖励设计配合 GRPO 更新面向多样工具使用基准的 LLM 策略。

[Title]: Natural Language Actor-Critic: Scalable Off-Policy Learning in Language Space
- [Pathway]: Narrative → Narrative → Policy
- [Source Experience]: long-horizon LLM-agent trajectories, sparse rewards, and natural-language critic feedback
- [Target Experience]: off-policy trained LLM agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Natural-language critiques serve as actionable training signals for policy improvement.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段 1 对应 P1：生成式 LLM 评论器将轨迹缺陷转化为自然语言解释。阶段 2 对应 P5：这些批评反馈在不依赖随机探索的情况下引导离策略策略改进。

[Title]: AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: multi-turn online interaction trajectories across diverse realistic environments
- [Target Experience]: AgentGym-RL trained generalist LLM agent policies
- [Source Modality]: [cross-modal]
- [Target Modality]: [cross-modal]
- [Experience Source]: {self}
- [Utilization]: Interactive rollouts provide RL feedback for training agents from scratch across tasks.
- [Method]: ⟨RL: unspecified⟩
- [Mechanism]: 该框架从模块化环境收集多轮轨迹，并使用 ScalingInter-RL，通过改变交互时长来平衡利用与探索，同时更新策略。

[Title]: Q-SFT: Q-Learning for Language Models via Supervised Fine-Tuning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: offline multi-turn datasets for dialogue, robotic manipulation, and navigation
- [Target Experience]: language-model policy whose token probabilities encode Q-values
- [Source Modality]: [cross-modal]
- [Target Modality]: [cross-modal]
- [Experience Source]: 不清楚
- [Utilization]: Offline trajectories are used to learn a near-optimal Q-function within the language model policy.
- [Method]: ⟨SFT⟩
- [Mechanism]: Q-learning 被重写为一种修改后的 SFT 目标，因此预收集的轨迹词元和回报可以在不新增价值头的情况下更新策略权重。

[Title]: Soft Policy Optimization: Online Off-Policy RL for Sequence Models
- [Pathway]: Out of Scope
- [Mechanism]: 摘要聚焦序列模型后训练和代码竞赛生成，没有清晰的 LLM 智能体交互或异质动作空间；因此按 Project_Infos.md §3.2 的单步/非智能体边界排除。

[Title]: Offline RL by Reward-Weighted Fine-Tuning for Conversation Optimization
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: pre-collected question-answering trajectories with rewards
- [Target Experience]: reward-weighted fine-tuned conversational policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: 不清楚
- [Utilization]: Offline trajectory rewards weight SFT-style updates for question answering and clarification behavior.
- [Method]: ⟨SFT⟩
- [Mechanism]: 该方法把离线 RL 重写为按奖励加权的微调：奖励更高的回答/澄清问题轨迹对 LLM 策略施加更强监督。

[Title]: TGPO: Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning
- [Pathway]: Schematic → Policy (P5)
- [Source Experience]: web-agent trajectories merged into tree-structured states with subgoal progress, redundancy, and action-verification signals
- [Target Experience]: preference-optimized web-agent policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: PRM-generated fine-grained rewards and dynamic weights guide offline RL.
- [Method]: ⟨hybrid⟩
- [Mechanism]: TGPO 先把网页智能体轨迹组织成树结构表示，合并语义相同的状态；随后 PRM 产生细粒度奖励和动态权重，最终由离线偏好优化把这些结构化轨迹证据内化到策略中。

[Title]: UI-TARS-2 Technical Report: Advancing GUI Agent with Multi-Turn Reinforcement Learning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: GUI data flywheel outputs and large-scale sandbox rollout trajectories
- [Target Experience]: UI-TARS-2 native GUI-centered agent policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Multi-turn RL rollouts and scalable data generation improve GUI, game, information-seeking, and SWE agent behavior.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 数据飞轮和沙盒平台生成交互轨迹；稳定化的多轮 RL 将由 GUI 决策经验形成的轨迹内化进模型。

[Title]: ComputerRL: Scaling End-to-End Online Reinforcement Learning for Computer Use Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: desktop automation rollouts involving API calls and GUI actions
- [Target Experience]: AutoGLM-OS computer-use policy weights
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Distributed online RL and alternating SFT/RL updates train agents for complex desktop tasks.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 数千个并行虚拟桌面产生在线轨迹；Entropulse 在 RL 与监督更新之间交替，避免熵塌缩，同时内化 API-GUI 交互经验。

[Title]: Mobile-Agent-v3: Fundamental Agents for GUI Automation
- [Pathway]: Policy → Narrative → Policy
- [Source Experience]: self-evolving GUI trajectories from automated query generation, correctness validation, and iterative refinement
- [Target Experience]: GUI-Owl / Mobile-Agent-v3 GUI agent policies
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Self-produced interaction data and asynchronous RL are used to train a foundational GUI agent.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段 1 对应 P7：GUI-Owl 在虚拟环境中生成并修正 GUI 轨迹。阶段 2 对应 P5：这些轨迹和 TRPO 风格的在线 RL 更新端到端 GUI 策略权重。

[Title]: EvoCUA: Evolving Computer Use Agents via Learning from Scalable Synthetic Experience
- [Pathway]: Policy → Narrative → Policy
- [Source Experience]: synthetic tasks, executable validators, asynchronous sandbox rollouts, and failure trajectories with self-correction
- [Target Experience]: EvoCUA native computer-use agent policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Massive trajectories and corrected failures are internalized through iterative evolving learning.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 系统合成可验证任务，执行大规模轨迹采样，强化成功例程，并通过错误分析和自我修正把失败轨迹转成监督信号后再更新策略。

[Title]: Agentic Reinforced Policy Optimization
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: multi-turn tool-use interaction trajectories with entropy patterns and advantage estimates
- [Target Experience]: ARPO-trained LLM-based tool-use agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Advantage attribution and entropy-adaptive sampling guide policy updates for tool interaction.
- [Method]: ⟨RL: unspecified⟩
- [Mechanism]: 该方法围绕高不确定性的工具交互采样轨迹级和步骤级轨迹，估计逐步决策优势，并更新策略以内化工具使用能力。

[Title]: From Off-Policy to On-Policy: Enhancing GUI Agents via Bi-level Expert-to-Policy Assimilation
- [Pathway]: Narrative → Narrative → Policy
- [Source Experience]: static expert GUI trajectories, self-rolled reachable trajectories, and per-task RLVR cache
- [Target Experience]: BEPA-trained end-to-end GUI policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {human}, {self}
- [Utilization]: Expert traces are converted into policy-aligned guidance and cached for RLVR training.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段 1 对应 P1：离策略专家轨迹被转化为学习者可到达且对齐的轨迹和动态任务指导。阶段 2 对应 P5：缓存中的指导在可验证奖励 RL 更新期间被策略使用。

[Title]: GUI-R1 : A Generalist R1-Style Vision-Language Action Model For GUI Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: curated cross-platform GUI interaction data and GRPO rewards
- [Target Experience]: R1-style LVLM GUI agent policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {human}
- [Utilization]: Curated GUI trajectories and GRPO internalize unified action-space rule modeling into the LVLM.
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 小规模高质量 GUI 数据先对策略进行界面落地，随后 GRPO 在统一 GUI 动作空间下更新模型权重，以处理高层真实任务。

[Title]: Training Long-Context, Multi-Turn Software Engineering Agents with Reinforcement Learning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: SWE execution-feedback trajectories, rejection fine-tuning samples, and RL rollouts
- [Target Experience]: Qwen2.5-72B-Instruct software-engineering agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: RFT improves formatting / instruction following; synchronous RL uses stateful SWE environment feedback for iterative improvement.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 执行反馈先过滤轨迹用于拒绝式微调，随后在有状态 SWE 环境中进行 DAPO 风格 RL 轨迹，进一步更新多轮仓库任务的策略权重。

[Title]: MobileGUI-RL: Advancing Mobile GUI Agent through Reinforcement Learning in Online Environment
- [Pathway]: Policy → Narrative → Policy
- [Source Experience]: self-explored mobile GUI tasks, filtered curriculum items, and online GUI trajectories
- [Target Experience]: GRPO-trained mobile GUI agent policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Self-exploration supplies curriculum tasks and trajectory-aware rewards for online RL.
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 智能体通过探索和过滤合成可学习任务，随后使用带轨迹感知优势和组合奖励的 GRPO 更新 GUI 策略。

[Title]: Generalization in Online Reinforcement Learning for Mobile Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Android GUI rollout trajectories from a scalable asynchronous training system
- [Target Experience]: 7B VLM mobile-agent policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: GRPO rollouts improve zero-shot generalization across AndroidWorld task regimes.
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 系统将移动 GUI 控制形式化为 CMDP，收集异步轨迹，并用 GRPO 将交互经验内化进 VLM 策略。

[Title]: AgentRL: Scaling Agentic Reinforcement Learning with a Multi-Turn, Multi-Task Framework
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: multi-turn trajectories from heterogeneous function-call environments across five agentic tasks
- [Target Experience]: multi-task open LLM agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Cross-policy sampling and task-normalized rewards train a generalist multi-task agent.
- [Method]: ⟨RL: unspecified⟩
- [Mechanism]: AgentRL 通过统一函数调用 API 收集异步多任务轨迹，再用跨策略采样和任务优势归一化稳定策略更新。

[Title]: Fine-tuning with RAG for Improving LLM Learning of New Skills
- [Pathway]: Narrative → Narrative → Policy
- [Source Experience]: agent failures, compact reusable hints, and improved teacher trajectories
- [Target Experience]: student agent policy weights with retrieval benefits internalized
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Hint-augmented teacher trajectories are distilled into students with hint strings removed, eliminating runtime RAG dependence.
- [Method]: ⟨LLM-extract⟩, ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P1：失败被总结为紧凑提示，并通过一次性检索生成改进轨迹。阶段 2 对应 P5：学生模型在无提示的轨迹上微调，迫使经验参数化内化。

[Title]: Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards
- [Pathway]: Policy → Narrative → Policy
- [Source Experience]: initial SWE agent attempts, unit-test validation rewards, guidance cues, and guided reattempt trajectories
- [Target Experience]: RLVR-trained software-engineering agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Guided trajectories and verifiable environment rewards update the agent policy; the data can also train a test-time reward model.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段 1 对应 P7/P1：当前智能体先尝试 SWE 任务，产生由单元测试验证的失败/部分解轨迹，并补充指导。阶段 2 对应 P5：带指导的重试轨迹和环境奖励驱动 RLVR 策略更新。

[Title]: From Correction to Mastery: Reinforced Distillation of Large Language Model Agents
- [Pathway]: Policy → Narrative → Policy
- [Source Experience]: student-generated trajectories and teacher corrections at the earliest error
- [Target Experience]: smaller student agent policy matching a larger teacher
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Corrected trajectories support SFT, and short-horizon RL from verified prefixes improves beyond imitation.
- [Method]: ⟨SFT⟩, ⟨RL: unspecified⟩
- [Mechanism]: 学生模型先暴露自身薄弱轨迹；教师修改最早错误以形成能力匹配的监督，随后 RL 从验证过的前缀开始并分配局部目标奖励。

[Title]: Structured Agent Distillation for Large Language Model
- [Pathway]: Policy → Narrative → Policy
- [Source Experience]: teacher ReAct-style trajectories segmented into reasoning and action spans
- [Target Experience]: compact student LLM agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Segment-specific losses preserve teacher reasoning fidelity and action consistency in smaller models.
- [Method]: ⟨SFT⟩
- [Mechanism]: 教师行为被外化为轨迹；方法把轨迹切分为 [REASON] 与 [ACT] 片段，并对学生策略施加片段特定的蒸馏损失。

[Title]: Sub-goal Distillation: A Method to Improve Small Language Agents
- [Pathway]: Narrative → Schematic → Policy
- [Source Experience]: oracle paths annotated by an LLM into sub-goal sequences
- [Target Experience]: smaller planning and execution module policies
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Sub-goal annotations and elementary actions fine-tune the planner and executor without runtime LLM access.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P2：LLM 将标准路径转换为结构化子目标分解。阶段 2 对应 P5：规划模块和执行模块分别在子目标与动作上微调。

[Title]: DynaWeb: Model-Based Reinforcement Learning of Web Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: real expert web trajectories, world-model-generated synthetic web rollouts, and on-policy rollouts
- [Target Experience]: RL-trained open-source web-agent policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {human}, {self}
- [Utilization]: Synthetic and expert trajectories are interleaved during RL for stable, sample-efficient web-agent training.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 真实交互数据训练一个位于当前策略/评估器载体划分之外的辅助世界模型；该模型生成轨迹轨迹，再与专家和同策略轨迹混合以更新智能体策略。

[Title]: Agentic Reinforcement Learning for Real-World Code Repair
- [Pathway]: Policy → Narrative → Policy
- [Source Experience]: GPT-4.1 code-repair trajectories, build-validation outcomes, and simplified-environment RL rollouts
- [Target Experience]: Qwen3-32B code-fixing agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}, {self}
- [Utilization]: Teacher trajectories provide SFT initialization; RL in a simplified environment adds pass-rate gains under matched train-test conditions.
- [Method]: ⟨SFT⟩, ⟨RL: unspecified⟩
- [Mechanism]: 教师生成的代码修复情节先被蒸馏进智能体，随后大规模 RL 轨迹的可验证构建结果进一步更新策略。

[Title]: Succeed or Learn Slowly: Sample Efficient Off-Policy Reinforcement Learning for Mobile App Control
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: mobile app control transitions, successful interactions, and negative samples
- [Target Experience]: SoLS-trained foundation-model GUI navigation policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Positive samples receive direct policy updates, while negative samples are regularized to avoid degrading the model.
- [Method]: ⟨hybrid⟩
- [Mechanism]: SoLS 使用离策略演员-评论家更新，优先回放成功转移样本，并把移动 GUI 交互结果转化为非对称策略更新规则。

[Title]: Information Gain-based Policy Optimization: A Simple and Effective Approach for Multi-Turn LLM Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: multi-turn search/tool-use interaction trajectories and model belief updates
- [Target Experience]: IGPO-trained multi-turn LLM agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Intrinsic turn-level rewards plus outcome supervision create dense reward trajectories for RL.
- [Method]: ⟨RL: unspecified⟩
- [Mechanism]: 每一轮都被视为信息获取；正确答案概率的边际提升作为内在奖励，并与最终结果监督结合用于策略优化。

[Title]: Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Credit Assignment
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: multi-turn tool-use trajectories with turn-level credit assignment signals
- [Target Experience]: GRPO-trained LLM agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Fine-grained turn-level advantages improve multi-turn reasoning and tool execution.
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 该方法把工具使用建模为 MDP，按回合估计优势，并将该信号整合进 GRPO，以跨多个决策步骤更新 LLM 策略。

[Title]: ReAct Meets ActRe: When Language Agents Enjoy Training Data Autonomy
- [Pathway]: Policy → Narrative → Policy
- [Source Experience]: sampled external actions, ActRe-generated rationales, successful synthesized ReAct-style trajectories, and failed-task trajectories
- [Target Experience]: QLoRA-fine-tuned ReAct-style language agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Synthesized trajectories and binarized rewards support contrastive self-training over multiple rounds.
- [Method]: ⟨hybrid⟩
- [Mechanism]: ActRe 为采样动作生成解释以合成后验推理，选择成功轨迹进行对比式自训练，并用带二值奖励的策略梯度更新智能体循环。

[Title]: Tree Search for LLM Agent Reinforcement Learning
- [Pathway]: Schematic → Policy (P5)
- [Source Experience]: tree-structured agent interaction steps with shared prefixes and outcome rewards
- [Target Experience]: Tree-GRPO-trained LLM agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Tree structure creates step-wise process supervision and grouped relative advantages.
- [Method]: ⟨tree-search⟩, ⟨RL: GRPO⟩
- [Mechanism]: 树搜索把轨迹组织为共享前缀树；结果奖励被传播为树内和树间相对优势，再用于更新策略。
> New tag: ⟨tree-search⟩ — 通过 tree / beam / best-of-N / lookahead 等显式搜索组织或筛选多步 rollout；既有 ⟨MCTS⟩ 过窄，无法覆盖非 Monte Carlo 的树式搜索。

[Title]: Policy Improvement using Language Feedback Models
- [Pathway]: Narrative → Evaluator → Policy
- [Source Experience]: visual trajectories verbalized into language descriptions and LLM feedback on desirable behavior
- [Target Experience]: imitation-learned instruction-following policy
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {teacher}
- [Utilization]: LFMs identify actions to imitate and provide human-interpretable feedback for adaptation.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P4：LLM 对语言化轨迹的反馈训练 LFM，使其能够判断期望行为。阶段 2 对应 P6：由 LFM 选择的行为转化为模仿监督，用于策略改进。

[Title]: EPO: Hierarchical LLM Agents with Environment Preference Optimization
- [Pathway]: Narrative → Evaluator → Policy
- [Source Experience]: multimodal environment feedback, automatically generated preference signals, and hierarchical subgoal/action trajectories
- [Target Experience]: hierarchical LLM agent policy for ALFRED
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: Environment-derived preference signals train subgoal prediction and low-level action generation.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 奖励模型把多模态环境反馈转化为偏好信号；EPO 再用这些偏好训练面向长程具身任务的层次化 LLM 策略。

[Title]: Improving Vision-Language-Action Model with Online Reinforcement Learning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: VLA environment-interaction trajectories from simulated and real-world manipulation tasks
- [Target Experience]: improved VLA policy weights
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}, {human}
- [Utilization]: RL exploration is alternated with supervised learning to improve VLA behavior while maintaining stability.
- [Method]: ⟨hybrid⟩
- [Mechanism]: iRe-VLA 在在线 RL 和监督学习之间迭代，用具身交互反馈更新 VLA 权重，使其超越初始专家数据 SFT 行为。

[Title]: EVOLVE-VLA: Test-Time Training from Environment Feedback for Vision-Language-Action Models
- [Pathway]: Narrative → Evaluator → Policy
- [Source Experience]: test-time environment interactions, progress-estimator feedback, and sparse task demonstrations
- [Target Experience]: continuously adapted VLA policy at test time
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: Dense autonomous feedback updates the VLA during deployment.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 学习得到的进展估计器替代标准奖励；平滑后的进展估计和渐进式时域长度扩展产生训练信号，使 VLA 策略通过测试时更新演化。

[Title]: AgentCPM-GUI: Building Mobile-Use Agents with Reinforcement Fine-Tuning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: high-quality Chinese and English GUI trajectories plus reinforcement fine-tuning rewards
- [Target Experience]: AgentCPM-GUI mobile-use policy weights
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {human}
- [Utilization]: Trajectories teach grounding and planning; GRPO improves reasoning capability for mobile GUI execution.
- [Method]: ⟨SFT⟩, ⟨RL: GRPO⟩
- [Mechanism]: 该流程先预训练感知能力，再在双语 GUI 轨迹上微调，最后在紧凑动作空间下用 GRPO 内化移动交互技能。

[Title]: ZeroGUI: Automating Online GUI Learning at Zero Human Cost
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: automatically generated GUI tasks, GUI rollouts, and VLM-based reward estimates
- [Target Experience]: online-trained GUI agent policies
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Automatic task generation and reward estimation replace manual annotations for online RL.
- [Method]: ⟨hybrid⟩
- [Mechanism]: VLM 从环境状态生成任务并估计任务成功；由于摘要描述的是奖励估计而非由轨迹学习可复用评估器，核心转化是 GUI 任务/轨迹经验通过两阶段在线 RL 进入策略参数。

[Title]: UI-Voyager: A Self-Evolving GUI Agent Learning via Failed Experience
- [Pathway]: Policy → Narrative → Policy
- [Source Experience]: failed mobile GUI trajectories, group rollouts, successful trajectories, and critical fork points
- [Target Experience]: self-evolved mobile GUI agent policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Failed and successful trajectories produce dense step-level supervision for self-distillation.
- [Method]: ⟨hybrid⟩
- [Mechanism]: RFT 支持自演化的数据/模型循环，GRSD 随后在组轨迹中识别分叉点，并用成功轨迹修正失败轨迹后更新策略。

[Title]: OpenMobile: Building Open Mobile Agents with Task and Trajectory Synthesis
- [Pathway]: Narrative → Narrative → Policy
- [Source Experience]: exploration-derived global environment memory, synthesized task instructions, and learner/expert rollout trajectories
- [Target Experience]: fine-tuned Qwen2.5-VL / Qwen3-VL mobile-agent policies
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Synthetic task instructions and error-recovery trajectories become open training data for mobile agents.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P1：环境探索被总结为全局记忆，并用于生成具环境依据的指令。阶段 2 对应 P5：策略切换式轨迹提供轨迹以微调 VLM 智能体。

[Title]: AndroidGen: Building an Android Language Agent under Data Scarcity
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: trajectories collected by AndroidGen for human-specified mobile tasks
- [Target Experience]: open-source Android language-agent policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {human}, {teacher}
- [Utilization]: Filtered trajectories train open-source LLMs for mobile-device control without manually labeled trajectories.
- [Method]: ⟨SFT⟩
- [Mechanism]: AndroidGen 从现有 LLM 智能体收集并过滤移动任务轨迹，再用这些轨迹微调开源移动智能体策略。

[Title]: AppVLM: A Lightweight Vision Language Model for Online App Control
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: AndroidControl offline trajectories and AndroidWorld online collected data
- [Target Experience]: lightweight VLM app-control policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {human}, {self}
- [Utilization]: Offline fine-tuning and later online training iterations refine the policy for smartphone control.
- [Method]: ⟨SFT⟩
- [Mechanism]: AppVLM 先通过离线微调内化 AndroidControl 轨迹，再收集 AndroidWorld 交互数据进一步细化策略。

[Title]: Step-GUI Technical Report
- [Pathway]: Policy → Narrative → Policy
- [Source Experience]: model-generated GUI trajectories calibrated by a step reward system
- [Target Experience]: Step-GUI 4B/8B agent policy family
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Calibrated training signals build GUI-agent models and support privacy-preserving GUI automation deployment.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段 1 对应 P7：当前或中间 GUI 智能体模型生成轨迹。阶段 2 对应 P5：校准式步骤奖励系统通过轨迹级校准把这些轨迹转化为可靠训练信号，自演化流程据此更新 GUI 策略权重。

[Title]: GUI-GENESIS: Automated Synthesis of Efficient Environments with Verifiable Rewards for GUI Agent Post-Training
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: synthetic GUI-environment rollouts with code-native executable rewards
- [Target Experience]: post-trained GUI agent policies
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}, {self}
- [Utilization]: Lightweight synthesized environments provide scalable reward-checkable rollouts for GUI post-training.
- [Method]: ⟨RL: unspecified⟩
- [Mechanism]: 真实应用被重构为带可执行断言的合成网页环境；智能体与这些环境交互，并通过 RL 内化可验证经验。

[Title]: Grounding Multimodal LLMs to Embodied Agents that Ask for Help with Reinforcement Learning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Ask-to-Act embodied interaction trajectories, clarification questions, navigation actions, and LLM-generated rewards
- [Target Experience]: RL-fine-tuned MLLM VLA policy
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}, {teacher}
- [Utilization]: LLM-generated rewards train agents to ask relevant questions and execute household rearrangement tasks.
- [Method]: ⟨RL: unspecified⟩
- [Mechanism]: 该方法通过奖励被试回答帮助请求、惩罚过度提问来训练具身智能体，使其在不确定时学会主动求助。

[Title]: UI-S1: Advancing GUI Automation via Semi-online Reinforcement Learning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: offline expert GUI trajectories, preserved rollout dialogues, patch-module recoveries, and future-return signals
- [Target Experience]: semi-online RL trained 7B GUI agent policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {human}, {self}
- [Utilization]: Offline trajectories simulate online RL and supply weighted step/episode advantages.
- [Method]: ⟨hybrid⟩
- [Mechanism]: DAG 形式的工作流追踪与专家路径的偏差，计算折扣未来回报，并用步骤级和情节级优势优化策略。

[Title]: π*0.6: a VLA That Learns From Experience
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: demonstrations, on-policy robot data, and expert teleoperated interventions during autonomous execution
- [Target Experience]: RECAP-trained generalist and specialized VLA policies
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {human}, {self}
- [Utilization]: Heterogeneous deployment data trains a generalist VLA and supports downstream task specialization.
- [Method]: ⟨hybrid⟩
- [Mechanism]: RECAP 根据示范、同策略采集和遥操作修正中的优势来条件化策略学习，把真实部署经验转化为 VLA 策略更新。

[Title]: VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning
- [Pathway]: Narrative → Evaluator → Policy
- [Source Experience]: robotic manipulation trajectories, extracted task segments, pseudo reward labels, and online collected data
- [Target Experience]: OpenVLA-7B policy improved by scalable RL
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: A robotic PRM supplies dense feedback for online VLA RL.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段 1 对应 P4：从轨迹中抽取任务片段，并用伪标签训练机器人过程奖励模型。阶段 2 对应 P6：PRM 以及课程/价值评估器预热信号共同引导在线 VLA 策略优化。

[Title]: Agent-World: Scaling Real-World Environment Synthesis for Evolving General Agent Intelligence
- [Pathway]: Schematic → Narrative → Policy
- [Source Experience]: executable tool ecosystems, synthesized verifiable tasks, capability-gap diagnoses, and multi-environment rollouts
- [Target Experience]: Agent-World general agent policies
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Dynamic task synthesis targets capability gaps and drives continuous multi-environment RL.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段 1 对应 P2/P7 类数据生成：工具生态被转化为可验证任务和交互场域。阶段 2 对应 P5：多环境 RL 将所得轨迹内化为智能体策略。

[Title]: Beyond Policy Optimization: A Data Curation Flywheel for Sparse-Reward Long-Horizon Planning
- [Pathway]: Narrative → Schematic → Policy
- [Source Experience]: planning trajectories, planning quaternions, curriculum-stratified tasks, and reward-gated experiences
- [Target Experience]: robust reasoning model for long-horizon sparse-reward environments
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Curated experiences are used for bootstrapping, extrapolation, and refinement of long-horizon planning policies.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 原始推理历史被压缩为结构化规划四元组，经课程学习扩展，并由奖励门控拒绝采样过滤后供策略学习。

[Title]: SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: VLA trajectory samples from parallel simulated and real-world manipulation environments
- [Target Experience]: RL-trained OpenVLA-OFT policy
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: VLA-specific rollout sampling and exploration strategies improve long-horizon robotic planning.
- [Method]: ⟨RL: unspecified⟩
- [Mechanism]: SimpleVLA-RL 将可扩展 RL 基础设施适配到 VLA 轨迹上，利用并行轨迹和优化后的损失在 SFT 行为之外继续更新策略。

[Title]: EPO: Entropy-regularized Policy Optimization for LLM Agents Reinforcement Learning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: sparse-reward multi-turn interaction trajectories with entropy statistics
- [Target Experience]: entropy-regularized LLM agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Entropy regularization stabilizes exploration and exploitation during sparse-reward RL.
- [Method]: ⟨RL: unspecified⟩
- [Mechanism]: EPO 观察到多轮轨迹中的熵塌缩和不稳定性，并把熵平滑与阶段化加权纳入策略优化。

[Title]: RLVMR: Reinforcement Learning with Verifiable Meta-Reasoning Rewards for Robust Long-Horizon Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: long-horizon agent trajectories with tagged planning, exploration, reflection, and outcome rewards
- [Target Experience]: critic-free policy-gradient trained long-horizon agent
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Programmatic meta-reasoning rewards densify the training signal for coherent agent reasoning.
- [Method]: ⟨RL: unspecified⟩
- [Mechanism]: 智能体标注认知步骤，针对有用的元推理行为获得规则奖励，并结合最终结果奖励，用无价值评估器的策略梯度更新策略。

[Title]: Tool-R1: Sample-Efficient Reinforcement Learning for Agentic Tool Use
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: executable Python tool-use trajectories, code execution success, and LLM answer-judgment rewards
- [Target Experience]: Tool-R1 tool-augmented reasoning policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Cached high-quality trajectories and outcome rewards train robust multi-step tool use.
- [Method]: ⟨RL: unspecified⟩
- [Mechanism]: 智能体生成含工具调用的可执行 Python 代码，接收执行/答案组合奖励，通过动态样本队列复用高质量轨迹，并更新策略。

[Title]: EvolveSearch: An Iterative Self-Evolving Search Agent
- [Pathway]: Policy → Narrative → Policy
- [Source Experience]: self-evolved web-search reasoning trajectories without human annotation
- [Target Experience]: improved agentic web-search policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Iterative SFT and RL reuse self-generated search data to improve multi-hop question answering.
- [Method]: ⟨SFT⟩, ⟨RL: unspecified⟩
- [Mechanism]: 当前搜索智能体生成训练轨迹，SFT 与 RL 消耗这些轨迹，循环重复以把网页搜索策略内化到模型中。

[Title]: WebEvolver: Enhancing Web Agent Self-Improvement with Coevolving World Model
- [Pathway]: Policy → Narrative → Policy
- [Source Experience]: self-sampled web-agent trajectories, world-model-generated training data, and look-ahead simulated observations
- [Target Experience]: self-improved web-agent policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: A coevolving world model generates synthetic data and supports look-ahead action selection.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 策略采样网页轨迹；辅助世界模型 LLM 预测观察并生成自指令式训练数据；这些显式轨迹既细化策略，也引导推理时搜索。

[Title]: OpenClaw-RL: Train Any Agent Simply by Talking
- [Pathway]: Narrative → Narrative → Policy
- [Source Experience]: next-state signals from user replies, tool outputs, terminal / GUI states, SWE traces, and tool-call traces
- [Target Experience]: asynchronously updated general agent policy
- [Source Modality]: [cross-modal]
- [Target Modality]: [cross-modal]
- [Experience Source]: {self}, {human}
- [Utilization]: PRM rewards and hindsight textual hints provide live online supervision for policy updates.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段 1 对应 P1：下一状态信号经后见引导式 OPD 转化为文本提示，同时 PRM 判断提供标量评估信号。阶段 2 对应 P5：提示、方向性优势和奖励由异步训练器消费并更新策略。

[Title]: What Can RL Bring to VLA Generalization? An Empirical Study
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: VLA trial-and-error trajectories and PPO rewards across visual, semantic, and execution generalization settings
- [Target Experience]: PPO-fine-tuned VLA policy
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: RL fine-tuning improves semantic understanding and execution robustness over SFT baselines.
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 具身试错经验通过 PPO 优化，学习到的策略再与 SFT 和其它 RL 算法比较其泛化能力。

[Title]: VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning with Verified Rewards in World Simulators
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: real interaction data, world-simulator rollouts, and dense trajectory-level rewards from goal-achieving references
- [Target Experience]: reinforcement-fine-tuned VLA policy
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: Simulator-generated action-aligned rollouts lower sample requirements for policy post-training.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 真实交互数据训练可控模拟器；策略在该模拟器内采样轨迹并接收密集可验证奖励，这些奖励用于更新 VLA 权重。

[Title]: Explorer: Scaling Exploration-driven Web Trajectory Synthesis for Multimodal Web Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: 94K successful multimodal web trajectories with screenshots and web elements
- [Target Experience]: Explorer multimodal web-agent policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Large-scale synthesized web trajectories are used as training data for multimodal web agents.
- [Method]: ⟨SFT⟩
- [Mechanism]: 网页探索和细化生成多样任务意图与成功轨迹；所得数据集用于微调多模态网页智能体，并带来数据规模增益。

[Title]: TGRPO :Fine-tuning Vision-Language-Action Model via Trajectory-wise Group Relative Policy Optimization
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: parallel VLA trajectories, LLM-generated task analysis, and dense rewards
- [Target Experience]: TGRPO-trained VLA policy
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Dense task-analysis rewards and group-relative advantages update robotic VLA policies.
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: LLM 生成任务分析以构造密集奖励；多个轨迹按组采样和归一化，产生轨迹级与步骤级优势用于策略优化。

[Title]: SQL-Trail: Multi-Turn Reinforcement Learning with Interleaved Feedback for Text-to-SQL
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: database interaction trajectories, execution feedback, SQL correctness rewards, and exploration-efficiency rewards
- [Target Experience]: SQL-Trail multi-turn Text-to-SQL agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Interleaved database feedback trains iterative schema exploration and SQL refinement behavior.
- [Method]: ⟨RL: unspecified⟩
- [Mechanism]: 智能体反复查询数据库，接收执行反馈，并由组合奖励面板优化，该奖励同时平衡 SQL 正确性和高效探索。

[Title]: The Generalization Gap in Offline Reinforcement Learning
- [Pathway]: Out of Scope
- [Mechanism]: 摘要研究通用在线/离线 RL 以及包含 Procgen/WebShop 的基准，但没有清晰地把策略表述为 LLM 智能体；因此按 Project_Infos.md §3.2 的非 LLM/传统 RL 边界排除。

[Title]: Proposer-Agent-Evaluator(PAE): Autonomous Skill Discovery For Foundation Model Internet Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: proposed web tasks, real-world grounded operation trajectories, and VLM-based success evaluations
- [Target Experience]: RL-refined foundation-model internet-agent policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {human}
- [Utilization]: Autonomous task proposal and success evaluation provide reward signals for skill discovery and policy refinement.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 任务提出器根据环境上下文生成任务，智能体执行任务，VLM 评估器评分成功与否，RL 使用这些提议任务轨迹和成功奖励更新策略；摘要没有说明评估器被训练。

[Title]: LongNav-R1: Horizon-Adaptive Multi-Turn RL for Long-Horizon VLA Navigation
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: long-horizon embodied navigation rollouts with varying horizon lengths
- [Target Experience]: horizon-adaptive RL-trained VLA navigation policy
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: Online interactions and horizon-adaptive advantages improve long-horizon navigation behavior.
- [Method]: ⟨RL: unspecified⟩
- [Mechanism]: 导航被重写为与具身环境的多轮对话；轨迹轨迹通过考虑时域长度长度的优势估计来更新 VLA 策略。

[Title]: OS-Copilot: Towards Generalist Computer Agents with Self-Improvement
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: previous OS task interactions and accumulated task-solving experience
- [Target Experience]: accumulated skills for general computer task automation
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Skills from prior tasks are reused to generalize to unseen applications such as Excel and PowerPoint.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 摘要强调通过累积技能实现自我改进，而非模型权重训练；先前计算机交互经验被组织为可复用技能，因此更适合标为叙事载体 → 图式载体而不是 P5。

[Title]: Go-Browse: Training Web Agents with Structured Exploration
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: graph-search-collected successful web task trajectories and interaction steps
- [Target Experience]: fine-tuned 7B web-agent policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Collected successful task-solving trajectories fine-tune a web navigation model.
- [Method]: ⟨SFT⟩
- [Mechanism]: 结构化探索把数据收集表述为图搜索，以收集可复用的成功轨迹；这些轨迹随后用于微调策略。

[Title]: Procedural Environment Generation for Tool-Use Agents
- [Pathway]: Schematic → Narrative → Policy
- [Source Experience]: procedurally generated interactive tools, compositional tasks, and synthetic tool-use trajectories
- [Target Experience]: tool-use agent policy tuned by SFT and RL
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Synthetic RandomWorld data supports SFT and online RL training for tool-use benchmarks.
- [Method]: ⟨SFT⟩, ⟨RL: unspecified⟩
- [Mechanism]: 阶段 1 对应 P2/P7 类合成：程序化工具环境生成组合式交互数据。阶段 2 对应 P5：在合成轨迹上调优的模型改进工具使用策略。

[Title]: Agentic Entropy-Balanced Policy Optimization
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: web-agent tool-call rollouts, entropy pre-monitoring signals, and token-level advantages
- [Target Experience]: AEPO-trained web-agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Entropy-balanced rollout and update rules stabilize scalable web-agent RL.
- [Method]: ⟨RL: unspecified⟩
- [Mechanism]: AEPO 用熵分配全局和分支采样预算，惩罚过度分支的工具步骤，重标定高熵词元的梯度，并用熵感知优势更新策略。

[Title]: PORTool: Importance-Aware Policy Optimization with Rewarded Tree for Multi-Tool-Integrated Reasoning
- [Pathway]: Schematic → Policy (P5)
- [Source Experience]: rewarded rollout trees with branching tool-use decisions, correctness-dominant importance scores, and execution-format signals
- [Target Experience]: efficient multi-tool reasoning policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Step-wise importance estimates guide policy updates toward efficient tool calls.
- [Method]: ⟨RL: unspecified⟩
- [Mechanism]: 轨迹树在同一上下文中比较替代工具决策；后继正确性和工具执行约束用于估计步骤重要性，并据此更新策略。

[Title]: From SWE-ZERO to SWE-HERO: Execution-free to Execution-based Fine-tuning for Software Engineering Agents
- [Pathway]: Policy → Narrative → Policy
- [Source Experience]: 300K execution-free and 13K execution-backed SWE trajectories distilled from Qwen3-Coder-480B
- [Target Experience]: Qwen2.5-Coder SWE agent policies
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Distilled trajectories are used in a two-stage SFT recipe for open-source SWE agents.
- [Method]: ⟨SFT⟩
- [Mechanism]: 前沿教师把仓库推理和执行支持的工作流外化为轨迹；SWE-ZERO 与 SWE-HERO 再在这些轨迹上微调较小的 SWE 智能体。

[Title]: MagicGUI: A Foundational Mobile GUI Agent with Scalable Data Pipeline and Reinforcement Fine-tuning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: GUI-centric multimodal data from repositories, automated crawling, manual annotation, and RL reward-filtered interactions
- [Target Experience]: MagicGUI foundational mobile GUI policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {human}, {teacher}, {self}
- [Utilization]: Data pipeline outputs and reinforcement fine-tuning improve perception, grounding, planning, and action execution.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 大规模多模态 GUI 数据支持继续预训练；带空间组合奖励和双重过滤的两阶段训练过程把 GUI 交互行为内化进策略。

[Title]: Adaptive Milestone Reward for GUI Agents
- [Pathway]: Narrative → Evaluator → Policy
- [Source Experience]: successful explorations, failed trajectories, and dynamically distilled milestones
- [Target Experience]: GUI agent policies trained with ADMIRE rewards
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Adaptive milestone rewards densify credit assignment across RL algorithms and environments.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段 1 对应 P4：成功探索被蒸馏为里程碑，形成可验证奖励系统。阶段 2 对应 P6：非对称信用分配在策略更新中为成功去噪、为失败搭建脚手架。

[Title]: On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: test-time step-by-step task-progress signals from dynamic simulated and physical deployments
- [Target Experience]: on-the-fly adapted VLA policy
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: Dense progress rewards refine the action policy during inference while preserving pretrained priors.
- [Method]: ⟨RL: unspecified⟩
- [Mechanism]: TT-VLA 在部署时使用任务进展信号作为密集奖励，并通过测试时 RL 更新把 VLA 策略适配到未见条件。

[Title]: AWPO: Enhancing Tool-Use of Large Language Models through Explicit Integration of Reasoning Rewards
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: tool-use trajectories with outcome rewards and chain-of-thought quality rewards
- [Target Experience]: AWPO-trained tool-use LLM policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Reasoning rewards are integrated into advantage estimates to improve multi-turn tool utilization.
- [Method]: ⟨RL: unspecified⟩
- [Mechanism]: AWPO 用方差和难度统计对推理奖励优势进行门控和加权，再与结果奖励结合，执行稳定的策略优化。

[Title]: SWE-Dev: Building Software Engineering Agents with Training and Inference Scaling
- [Pathway]: Schematic → Narrative → Policy
- [Source Experience]: synthesized test cases, scaled SWE agent trajectories, and patch-evaluation evidence
- [Target Experience]: SWE-Dev 7B / 32B software-engineering agent policies
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}, {self}
- [Utilization]: Test cases evaluate patches, while large-scale trajectories train open SWE agents.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P2：测试用例合成用于判断补丁行为的结构化评估器。阶段 2 对应 P5：扩展后的轨迹成为 SWE-Dev 策略权重的训练数据。

[Title]: Android Coach: Improve Online Agentic Training Efficiency with Single State Multiple Actions
- [Pathway]: Narrative → Evaluator → Policy
- [Source Experience]: Android online states, multiple sampled actions, process reward signals, and critic value estimates
- [Target Experience]: Android agent policy improved by coached RL
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Critic and PRM signals allow multiple actions per expensive emulator state to train the policy efficiently.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 价值评估器在同一状态下估计多个动作的价值，并由过程奖励模型辅助；平均价值评估器输出得到的组优势用于指导策略更新。

[Title]: WebCoT: Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback
- [Pathway]: Narrative → Narrative → Policy
- [Source Experience]: web-agent trajectories exhibiting reflection, lookahead, branching, and rollback
- [Target Experience]: fine-tuned web-agent backbone LLM with distilled CoT reasoning patterns
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Reconstructed CoT rationales are distilled into the backbone LLM to improve web-agent reasoning.
- [Method]: ⟨LLM-extract⟩, ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P1：推理时的反思、分支和回滚算法被重构为轨迹上的 CoT 推理依据。阶段 2 对应 P5：微调把这些推理模式内化为策略权重。

[Title]: VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model
- [Pathway]: Policy → Narrative → Policy
- [Source Experience]: real-world VLA rollouts and synthetic rollouts generated by an improved action-conditioned video world model
- [Target Experience]: improved VLA policy for real-robot tasks
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: Real rollouts improve the world model, and synthetic rollouts from that model improve the VLA policy.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 策略收集真实轨迹；辅助世界模型由这些轨迹改进，随后生成补充合成轨迹，这些显式训练经验继续用于 VLA 策略。

[Title]: Large Language Models as Generalizable Policies for Embodied Tasks
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: embodied visual environment interactions, text instructions, observations, and task rewards
- [Target Experience]: LLaRP embodied LLM policy
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: Environmental interactions train the LLM to map observations and instructions directly to actions.
- [Method]: ⟨RL: unspecified⟩
- [Mechanism]: 冻结的预训练 LLM 被改造成策略，并通过具身任务交互上的 RL 训练，使其能直接向环境输出动作。

[Title]: Sparse Rewards Can Self-Train Dialogue Agents
- [Pathway]: Policy → Narrative → Policy
- [Source Experience]: model-generated tool-calling dialogue outputs in a sparse-reward simulation environment
- [Target Experience]: JOSH-trained dialogue / tool-calling agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Sparse simulation rewards identify ideal behaviors from the model's own outputs for further training.
- [Method]: ⟨hybrid⟩
- [Mechanism]: JOSH 从稀疏奖励的工具调用模拟器中收集成败对照结果，并在 LLM 自己筛选出的输出上训练，以改进多轮工具交互。

[Title]: Multi-Agent Tool-Integrated Policy Optimization
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: planner and worker rollouts in multi-agent tool-integrated tasks
- [Target Experience]: single-LLM policy with role-specific planner / worker behavior
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Role-specific credit assignment trains multi-agent tool use within one LLM instance.
- [Method]: ⟨RL: unspecified⟩
- [Mechanism]: MATPO 对规划器和执行器的轨迹做信用分配，然后更新一个由角色提示条件化的共享权重策略，使其在分工中专门化。

[Title]: Toward Training Superintelligent Software Agents through Self-Play SWE-RL
- [Pathway]: Policy → Narrative → Policy
- [Source Experience]: self-play bug injection and repair trajectories in sandboxed repositories with test-patch specifications
- [Target Experience]: self-improved SWE-RL software-agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Self-play trajectories replace human-labeled issues and tests as RL experience for SWE agents.
- [Method]: ⟨RL: unspecified⟩
- [Mechanism]: 同一个智能体在仓库中制造缺陷并修复缺陷，接收形式化测试/补丁反馈，并用产生的自博弈情节改进策略。

[Title]: SQL-ASTRA: Alleviating Sparse Feedback in Agentic SQL via Column-Set Matching and Trajectory Aggregation
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: multi-turn SQL trajectories, final feedback, executed-query intermediate signals, ATR scores, and CSMR partial-correctness rewards
- [Target Experience]: Agentic SQL policy trained with dense reward signals
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Dense trajectory-level and step-level rewards reduce sparse-feedback ambiguity during RL.
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: ATR 聚合多轮过程分数，CSMR 把执行查询反馈转化为部分正确性奖励，这些密集信号共同训练 Text-to-SQL 智能体策略。

[Title]: Fine-Tuning Large Vision-Language Models as Decision-Making Agents via Reinforcement Learning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: CoT reasoning outputs, parsed executable actions, environment observations, and task rewards
- [Target Experience]: RL-fine-tuned VLM decision-making agent policy
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {self}
- [Utilization]: Task rewards from environment interaction fine-tune VLM agents for multi-step goal-directed decisions.
- [Method]: ⟨RL: unspecified⟩
- [Mechanism]: VLM 生成 CoT 和文本动作，动作被解析并在环境中执行，观察到的奖励再通过 RL 更新完整 VLM 策略。

[Title]: MTSQL-R1: Towards Long-Horizon Multi-Turn Text-to-SQL via Agentic Training
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: propose-execute-verify-refine SQL trajectories, database execution feedback, and persistent dialogue-memory verification
- [Target Experience]: MTSQL-R1 long-horizon Text-to-SQL agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Execution and memory feedback train coherent multi-turn SQL refinement behavior.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 任务被建模为 MDP，智能体与数据库和对话记忆交互；日志和验证反馈成为训练策略的轨迹。

[Title]: AgentTuning: Enabling Generalized Agent Abilities for LLMs
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: AgentInstruct high-quality interaction trajectories for planning, memorization, and tool use
- [Target Experience]: AgentLM policy weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: 不清楚
- [Utilization]: Agent trajectories are combined with general instructions to tune Llama 2 without degrading general abilities.
- [Method]: ⟨SFT⟩
- [Mechanism]: AgentInstruct 交互轨迹提供监督式决策过程数据；混合指令微调将智能体能力内化到 LLM 参数中。

[Title]: DistRL: An Asynchronous Distributed Reinforcement Learning Framework for On-Device Control Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: decentralized mobile-device control trajectories from dynamic online interactions
- [Target Experience]: RL-fine-tuned MLLM on-device control policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Asynchronous online rollouts support efficient fine-tuning of mobile control agents.
- [Method]: ⟨RL: unspecified⟩
- [Mechanism]: DistRL 将去中心化数据获取与中心化训练分离，平衡探索和优先级采集数据，并更新移动设备控制策略。

[Title]: Internalizing World Models via Self-Play Finetuning for Agentic RL
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: self-play environment interactions, state representations, transition-modeling traces, and simulated future states
- [Target Experience]: LLM agent policy with internalized world-model behavior
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Self-play SFT cold-starts an internal world model that supports later RL policy optimization.
- [Method]: ⟨SFT⟩, ⟨RL: unspecified⟩
- [Mechanism]: 交互轨迹通过自博弈 SFT 教会状态表示和转移建模；初始化后的策略在 RL 更新前先模拟未来状态，再改进决策。

[Title]: CM2: Reinforcement Learning with Checklist Rewards for Multi-Turn and Multi-Step Agentic Tool Use
- [Pathway]: Schematic → Policy (P5)
- [Source Experience]: checklist criteria, evidence-grounded metadata, LLM-simulated tool-environment trajectories, and sparse reward assignments
- [Target Experience]: CM2-trained multi-turn tool-use agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Checklist rewards replace verifiable outcome rewards for scalable tool-agent RL.
- [Method]: ⟨RL: unspecified⟩
- [Mechanism]: 预期行为被拆解成带显式证据的细粒度二元标准；这些结构化标准评判模拟工具轨迹，并为策略更新提供奖励。

[Title]: Training Versatile Coding Agents in Synthetic Environments
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: synthetically generated coding environments, tasks, trajectories, unit-test reproduction traces, and library-implementation traces
- [Target Experience]: versatile coding-agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Synthetic trajectories with dense training signal train coding agents with fewer episodes.
- [Method]: ⟨SFT⟩
- [Mechanism]: 强语言模型和智能体从零合成项目、任务和轨迹；这些显式编码智能体轨迹被用来训练策略权重。

[Title]: SAND: Boosting LLM Agents with Self-Taught Action Deliberation
- [Pathway]: Policy → Narrative → Policy
- [Source Experience]: base LLM-agent policy samples, candidate actions, execution-guided critiques, and step-wise deliberation thoughts
- [Target Experience]: fine-tuned LLM agent policy with action deliberation
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Deliberation trajectories fine-tune the agent to compare actions before committing.
- [Method]: ⟨LLM-extract⟩, ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P7/P1：基础 LLM 智能体采样候选动作，并用执行引导的批评反馈合成自教式慎思轨迹。阶段 2 对应 P5：迭代微调把这些轨迹内化到同一智能体策略中。

[Title]: Controllable and Verifiable Tool-Use Data Synthesis for Agentic Reinforcement Learning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: self-evolved tool-use trajectories, validated oracle calls, augmented noisy tool environments, and reward-checkable rollouts
- [Target Experience]: COVERT-RL tool-calling policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}, {self}
- [Utilization]: Oracle-preserving synthetic environments provide reference-matched rewards for RL refinement.
- [Method]: ⟨SFT⟩, ⟨RL: unspecified⟩
- [Mechanism]: COVERT 先合成并验证基础轨迹，再在保持标准行为的前提下扩增环境；SFT/RL 使用所得轨迹和自动奖励更新策略。

[Title]: CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification
- [Pathway]: Schematic → Narrative → Policy
- [Source Experience]: explicit task constraints, generated complex trajectories, deterministic verifier outputs, and reward signals
- [Target Experience]: CoVe interactive tool-use agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Constraints generate SFT trajectories and derive RL reward signals.
- [Method]: ⟨SFT⟩, ⟨RL: unspecified⟩
- [Mechanism]: 阶段 1 对应 P2/P4：约束引导轨迹生成并验证质量。阶段 2 对应 P5：验证后的轨迹和奖励用于 SFT 与 RL 后训练。

[Title]: VEM: Environment-Free Exploration for Training GUI Agent with Value Environment Model
- [Pathway]: Narrative → Evaluator → Policy
- [Source Experience]: offline GUI state-action data and long-term action utility labels / estimates
- [Target Experience]: GUI policy guided by a frozen Value Environment Model
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {human}
- [Utilization]: VEM value estimates guide policy exploration without costly environment interaction.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段 1 对应 P4：离线数据训练 VEM 来估计状态-动作价值。阶段 2 对应 P6：冻结的 VEM 信号引导面向布局无关 GUI 自动化的策略优化。

[Title]: Don't Just Fine-tune the Agent, Tune the Environment
- [Pathway]: Schematic → Narrative → Policy
- [Source Experience]: BFCL problem instances, structured curriculum, environment augmentation, corrective feedback, and progress rewards
- [Target Experience]: robust tool-use LLM agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Environment tuning turns problem instances into dynamic exploration experience for RL.
- [Method]: ⟨RL: unspecified⟩
- [Mechanism]: 结构化课程和环境增强提供纠错反馈与细粒度进展奖励，使智能体能够直接从问题实例中学习工具使用行为。

[Title]: Agent models: Internalizing Chain-of-Action Generation into Reasoning models
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Chain-of-Action trajectories, step-level action triggers, and trajectory-level optimization feedback
- [Target Experience]: Large Agent Model policy that autonomously switches between reasoning and external actions
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: 不清楚
- [Utilization]: SFT and RL internalize formerly prompt-managed tool/environment interaction workflows into model weights.
- [Method]: ⟨SFT⟩, ⟨RL: unspecified⟩
- [Mechanism]: AutoCoA 在动作链行为上训练模型，优化动作触发和轨迹结果，并用内部世界模型降低真实环境交互成本。

[Title]: ToolOmni: Enabling Open-World Tool Use via Agentic learning with Proactive Retrieval and Grounded Execution
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: cold-start multi-turn interaction dataset and online open-world tool retrieval / execution trajectories
- [Target Experience]: ToolOmni open-world tool-use policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: 不清楚
- [Utilization]: SFT instills base agentic behavior; GRPO jointly optimizes retrieval accuracy and execution efficacy.
- [Method]: ⟨SFT⟩, ⟨RL: GRPO⟩
- [Mechanism]: 系统先在多轮交互上微调，再在在线工具环境中应用解耦多目标 GRPO，以内化检索和执行经验。

[Title]: SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph
- [Pathway]: Narrative → Schematic → Policy
- [Source Experience]: same-prompt trajectories, outcome rewards, and trajectory graphs of shared steps
- [Target Experience]: group-based RL policy with finer-grained advantages
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Trajectory graphs assign step-level advantages and plug into existing group-based RL algorithms.
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 阶段 1 对应 P2：轨迹被组织成图，用最终结果奖励估计每一步质量。阶段 2 对应 P5：导出的优势指导策略更新。

[Title]: Harnessing Uncertainty: Entropy-Modulated Policy Gradients for Long-Horizon LLM Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: long-horizon agent trajectories, final task outcomes, and step-wise uncertainty estimates
- [Target Experience]: EMPG-trained LLM agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Uncertainty-modulated gradients stabilize exploration and reward assignment.
- [Method]: ⟨RL: unspecified⟩
- [Mechanism]: EMPG 用逐步熵和最终结果重标定策略梯度，放大自信且正确的动作，惩罚自信错误，并鼓励可预测的解题路径。

[Title]: TOOLCAD: Exploring Tool-Using Large Language Models in Text-to-CAD Generation with Reinforcement Learning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: CAD reasoning and tool-augmented interaction trajectories with hybrid feedback and human supervision
- [Target Experience]: CAD tool-using LLM agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {human}
- [Utilization]: Online curriculum RL trains refined CAD-CoT and CAD tool-use behavior.
- [Method]: ⟨hybrid⟩
- [Mechanism]: CAD 训练环境生成推理和与 CAD 引擎的工具交互；混合反馈和人类监督成为在线课程 RL 的训练信号。

[Title]: Understanding the performance gap between online and offline alignment algorithms
- [Pathway]: Out of Scope
- [Mechanism]: 摘要研究基于提示-回答偏好数据的一般 RLHF/离线对齐，没有清晰的多步 LLM 智能体环境或异质动作空间；因此按 Project_Infos.md §3.2 的单步对齐边界排除。

[Title]: TSR: Trajectory-Search Rollouts for Multi-Turn RL of LLM Agents
- [Pathway]: Schematic → Policy (P5)
- [Source Experience]: tree-style rollout trajectories selected by best-of-N, beam, or shallow lookahead search with task feedback
- [Target Experience]: PPO / GRPO-trained multi-turn LLM agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Training-time search improves rollout quality and stabilizes multi-turn RL.
- [Method]: ⟨tree-search⟩, ⟨RL: PPO⟩, ⟨RL: GRPO⟩
- [Mechanism]: 轻量树搜索在轨迹采样时构造更高质量轨迹；这些轨迹直接输入未改动的 PPO/GRPO 目标以更新策略。

[Title]: Instructing LLMs to Negotiate using Reinforcement Learning with Verifiable Rewards
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: buyer-seller negotiation dialogues with verifiable economic-surplus and budget-adherence rewards
- [Target Experience]: 30B buyer-agent negotiation policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Verifiable rewards train strategic negotiation behavior and generalization to unseen counterparties.
- [Method]: ⟨RL: unspecified⟩
- [Mechanism]: 买方智能体与受规则约束的 LLM 卖方谈判；盈余和预算约束提供奖励信号，推动策略在多个战略阶段中更新。

[Title]: Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: multi-turn WebShop / Sokoban trajectories with turn-level MDP advantages
- [Target Experience]: turn-PPO trained agentic LLM policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Turn-level advantage estimates stabilize PPO for long-horizon agent tasks.
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 该方法把多轮交互重写到回合级而非词元级，计算回合级优势，并用 PPO 更新策略。

[Title]: Offline Regularised Reinforcement Learning for Large Language Models Alignment
- [Pathway]: Out of Scope
- [Mechanism]: 摘要关注由提示-回答-反馈三元组/偏好数据进行的 LLM 对齐，而不是带异质动作的 LLM 智能体轨迹；因此按 Project_Infos.md §3.2 的单步对齐边界排除。

[Title]: Offline RL for Natural Language Generation with Implicit Language Q Learning
- [Pathway]: Out of Scope
- [Mechanism]: 摘要聚焦自然语言生成和主观效用优化，没有清楚建立 LLM 智能体与异质动作环境交互的设定，因此落在 Project_Infos.md §3.2 边界之外。

[Title]: Unleashing the Power of Pre-trained Language Models for Offline Reinforcement Learning
- [Pathway]: Out of Scope
- [Mechanism]: 摘要讨论使用预训练语言模型进行离线 RL/决策 Transformer 运动控制训练，但没有清楚表述具备异质推理、工具或环境控制动作空间的 LLM 智能体；因此按 Project_Infos.md §3.2 的非 LLM/传统离线 RL 边界排除。

[Title]: Leftover Lunch: Advantage-based Offline Reinforcement Learning for Language Models
- [Pathway]: Out of Scope
- [Mechanism]: 摘要把整个 LM 输出序列视为 RLHF 风格语言生成任务中的单个动作，没有显现多步 LLM 智能体环境或异质动作空间；因此按 Project_Infos.md §3.2 排除。

[Title]: Language Models are Few-Shot Butlers
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: small expert demonstrations and ALFWorld environment-interaction trajectories
- [Target Experience]: fine-tuned / RL-improved autoregressive language-agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}, {self}
- [Utilization]: Demonstrations initialize the agent, then interaction experience further improves ALFWorld task success.
- [Method]: ⟨SFT⟩, ⟨RL: unspecified⟩
- [Mechanism]: 两阶段过程先在少量专家示范上微调，再利用来自环境交互的简单 RL 更新语言模型策略。

[Title]: Learning to Navigate Wikipedia by Taking Random Walks
- [Pathway]: Out of Scope
- [Mechanism]: 摘要呈现 Wikipedia 图上的超链接导航行为克隆，但没有清楚把策略表述为 LLM 智能体；因此按 Project_Infos.md §3.2 的非 LLM 系统边界排除。

[Title]: WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: crowd-sourced product-search instructions, human demonstrations, agent / human trajectories, and RL / imitation feedback
- [Target Experience]: grounded web-shopping agent policies
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}, {self}
- [Utilization]: Demonstrations and web-environment rewards train and evaluate language agents for e-commerce navigation.
- [Method]: ⟨SFT⟩, ⟨RL: unspecified⟩
- [Mechanism]: WebShop 提供模拟网页环境和人类示范；智能体通过模仿学习与 RL 学习商品搜索、查询改写和购买动作。

## New Tags Introduced
- ⟨RL: unspecified⟩ —— Abstract 只说明 RL / online RL / RLVR / policy optimization，但未给出可归入 PPO、GRPO、DPO、ReST 的具体算法；首次出现：「WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning」
- ⟨tree-search⟩ —— 通过 tree / beam / best-of-N / lookahead 等显式搜索组织或筛选多步 rollout；首次出现：「Tree Search for LLM Agent Reinforcement Learning」
