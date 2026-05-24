[Title]: WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: Raw web interaction trajectories (online rollouts from current policy)
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 用于训练 open LLM 成为 proficient web agent，在 WebArena-Lite 上评估
- [Method]: ⟨hybrid⟩
- [Mechanism]: hybrid 由 ⟨LLM-extract⟩ + ⟨RL: PPO⟩（或类似 online RL）+ SFT（ORM 训练）组成。核心为 Policy → Narrative → Policy 自生成闭环（§8.1）：Stage 1 (P7)：当前 policy 在 web 环境中在线 rollout，产生成功与失败 trajectory；Stage 2 (P1)：从失败尝试中通过 LLM 提取生成新任务（self-evolving curriculum），同时训练 outcome-supervised reward model (ORM) 作为 Evaluator（P4：Narrative → Evaluator）；Stage 3 (P5 + P6)：agent 在新旧任务上继续 rollout，由 ORM 提供稠密奖励信号，通过 adaptive RL 更新 policy 权重。论文贡献点在闭环衔接机制：用失败轨迹生成课程任务以解决训练任务稀缺、用 ORM 缓解稀疏反馈、用 adaptive RL 策略应对在线学习的 policy distribution drift。

[Title]: WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Raw web interaction trajectories（异步生成的 online rollout）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 Qwen-2.5-3B / Llama-3.1-8B 成为 web agent，在 WebArena-Lite 评估
- [Method]: ⟨RL: GRPO⟩（binary reward guided online RL）
- [Mechanism]: Agent 在 web 环境中在线交互、异步生成多样化 trajectory，仅以二值任务成功信号为奖励，通过端到端多轮 RL 将 raw trajectory 经验内化为 policy 权重。论文核心贡献在 RL 算法层面（多轮 GRPO 适配 web agent），探索了不同 RL 初始化策略（Zero 无热身 vs CoT 行为克隆热身）。{self} 标签已捕获"数据由当前 policy 自生成"的事实，但论文贡献不在闭环衔接机制而在 RL 训练框架本身。

[Title]: SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from Experience
- [Pathway]: Policy → Narrative → Policy (§8.1), multi-target (§8.8)
- [Source Experience]: Raw GUI interaction trajectories（agent 在陌生软件上的探索轨迹）
- [Target Experience]: Updated policy weights (π-Par) + World State Model (V-Par) + Curriculum Generator
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 训练 CUA 自主掌握陌生软件；specialist-to-generalist 策略整合多个 specialist agent 的经验洞察
- [Method]: ⟨hybrid⟩
- [Mechanism]: hybrid 由 ⟨LLM-extract⟩ + ⟨RL: GRPO⟩ + SFT（adversarial imitation）组成。核心为 Policy → Narrative → Policy 自演化闭环（§8.1），含多目标分支（§8.8）：Stage 1 (P7)：当前 CUA policy 在陌生软件上自主探索，产生成功与失败 trajectory；Stage 2a (P4)：World State Model（V-Par）从 step-wise trajectory 中训练，用于评估每步质量——此为 Narrative → Evaluator 分支；Stage 2b：Curriculum Generator 从 exploration 经验中自动生成由简到繁的任务——此为 Narrative → Narrative (P1)；Stage 3 (P5)：对失败动作做 adversarial imitation（SFT 形式的负样本学习），对成功轨迹做 GRPO——此为 Narrative → Policy。最后 specialist-to-generalist 整合阶段将多个 specialist 在各自软件上的经验洞察（Narrative）汇聚训练 stronger generalist CUA。

[Title]: ARPO: End-to-End Policy Optimization for GUI Agents with Experience Replay
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: GUI interaction trajectories（从环境交互中收集的成功经验存入 replay buffer）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 训练 vision-language GUI agent 在 OSWorld 上执行复杂长时程计算机任务
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 在 GRPO 基础上引入 experience replay buffer，将成功 trajectory 跨训练迭代复用，缓解 GUI 场景下稀疏奖励、延迟反馈和高 rollout 成本问题。同时提出 task selection strategy 基于 baseline agent 表现过滤任务，使 agent 聚焦于 informative interactions。本质上是对 GRPO 的数据效率改进：将 agent 自身交互产生的 raw trajectory（Narrative）通过 GRPO + replay 内化为 policy 权重（π-Par）。replay buffer 复用的是成功经验的数据复用策略而非闭环衔接机制的核心创新。

[Title]: ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Raw multi-turn interaction trajectories（utterance 级别的决策序列）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 LLM agent 在 goal-directed multi-turn 决策任务中表现更好
- [Method]: ⟨hybrid⟩
- [Mechanism]: hybrid 由 hierarchical RL（high-level off-policy value-based RL + low-level on-policy RL）组成，但不涉及 Carrier 层面的多步转化。本质是对 P5 路径中 RL 算法的层次化改造：high-level critic 跨 utterance 聚合长期回报，low-level actor 在每个 utterance 内做 token-level 策略优化。源端 raw trajectory 来自 agent 与环境的 online 交互，目标端为更新后的 policy 权重。层次化结构解决多轮场景下的 credit assignment 和长时程奖励延迟问题，是 RL 算法架构创新而非经验转化路径创新。

[Title]: RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: Raw multi-turn interaction trajectories（agent 在线 rollout）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练和评估 LLM agent 在四个 stylized environments 上的表现
- [Method]: ⟨RL: PPO⟩（StarPO / StarPO-S）
- [Mechanism]: 提出 StarPO (State-Thinking-Actions-Reward Policy Optimization) 轨迹级 agent RL 框架，核心研究自演化（self-evolution）过程中的现象与问题。闭环为 Policy → Narrative → Policy（§8.1）：Stage 1 (P7)：当前 policy 在线 rollout 产生 trajectory；Stage 2 (P5)：trajectory 通过 StarPO 回灌训练 policy。论文贡献点恰在闭环衔接机制的分析与稳定化——发现 Echo Trap 现象（reward variance cliffs + gradient spikes），提出 StarPO-S 稳定变体（trajectory filtering + critic incorporation + gradient stabilization）；同时分析 rollout shaping（初始状态多样性、交互粒度、采样频率）对训练效果的影响；指出缺少 fine-grained reasoning-aware reward 时 agent reasoning 难以通过多轮 RL 涌现。

[Title]: Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: Raw web interaction trajectories（MCTS-guided exploration 产生的成功与失败轨迹）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 LLM agent 在 WebShop 和真实预订场景中执行复杂多步推理任务
- [Method]: ⟨hybrid⟩
- [Mechanism]: hybrid 由 ⟨MCTS⟩ + ⟨LLM-extract⟩（self-critique）+ ⟨RL: DPO⟩ 组成。Policy → Narrative → Policy 闭环（§8.1）：Stage 1 (P7)：当前 policy 在 guided MCTS 搜索下与 web 环境交互，生成多样化 exploration trajectory（成功+失败）；Stage 2a (P1)：self-critique mechanism（LLM-extract）对 trajectory 进行反思精炼——Narrative → refined Narrative；Stage 2b (P5)：使用 off-policy DPO 在 contrastive trajectory pairs 上迭代微调 policy。闭环衔接创新点：MCTS 提供 guided exploration 提升 trajectory 质量与多样性；self-critique 提供中间反思信号；off-policy DPO 使 agent 同时从成功和失败轨迹中学习，缓解 compounding errors。

[Title]: DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Raw device-control interaction trajectories（AitW 数据集静态人类示范 + online 自主收集轨迹）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {human}, {self}
- [Utilization]: 训练 VLM 成为 in-the-wild Android device control agent
- [Method]: ⟨RL: PPO⟩（advantage-weighted RL with automatic curriculum）
- [Mechanism]: 两阶段训练：(1) offline RL 在静态人类示范数据（AitW）上初始化 model——此为 {human} Narrative → Policy (P5)；(2) offline-to-online RL 在 parallelizable Android learning environment 中通过 VLM-based evaluator 提供稠密奖励信号继续训练——此为 {self} Narrative → Policy (P5)。核心创新在 RL 算法层面：advantage estimator 增强以考虑环境随机性，automatic curriculum 最大化学习信号。两阶段都是 Narrative → Policy 单步转化，离线到在线的过渡是训练策略而非经验形式的二次转化。

[Title]: Grounding Large Language Models in Interactive Environments with Online Reinforcement Learning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Raw text-based interaction trajectories（agent 在交互式文本环境中探索）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 用于解决 spatial 和 navigation 任务，研究 functional grounding
- [Method]: ⟨RL: PPO⟩（online RL）
- [Mechanism]: 以 LLM (FLAN-T5) 作为 policy 网络，在交互式文本环境中在线 RL 逐步更新参数，使 LLM 的抽象世界知识与具体环境对齐（functional grounding）。源端为 agent 自主交互产生的 task-solving trajectory（Narrative），通过 online RL 的奖励信号（任务完成与否）内化为 policy 权重。本质是 P5 的标准 online RL 应用，创新点在"用 LLM 作为 RL policy 网络"以实现 functional grounding 这一概念验证。

[Title]: Reinforcement Learning for Long-Horizon Interactive LLM Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Raw API-call-based interaction trajectories（在 AppWorld 中 multi-domain, multi-app 交互）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 32B agent 在 AppWorld 环境中直接通过 API 调用完成长时程任务
- [Method]: ⟨RL: PPO⟩（LOOP: 无 value network 的 PPO 变体）
- [Mechanism]: 将 LLM agent 在 stateful digital environment 中的训练形式化为 POMDP，推导出 LOOP——data- and memory-efficient PPO 变体，仅维护一份 LLM 副本、不用 value network。源端为 agent 在 AppWorld 中的 API 调用 trajectory，通过 trajectory-level 奖励信号（任务成功）内化为 policy 权重。核心创新在 RL 算法工程层面（内存效率、实现简洁性），是 P5 路径下对 PPO 算法的 agent-specific 适配。

[Title]: Direct Multi-Turn Preference Optimization for Language Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Multi-turn preference trajectory pairs（preferred vs. dis-preferred trajectories）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: 不清楚（abstract 未明示 trajectory pairs 来源）
- [Utilization]: 使 LLM 适应多轮 agent 任务
- [Method]: ⟨RL: DPO⟩（DMPO loss）
- [Mechanism]: 将 DPO 推广至多轮 agent 场景，通过用 state-action occupancy measure 约束替代 policy constraint、并在 Bradley-Terry 模型中引入长度归一化，推导出 DMPO loss 以解决 partition function 在多轮设定下无法消去的问题。转化本身仍是 preference trajectory → policy weights 的 P5 单步，核心创新在损失函数的理论推导，为 DPO 从单轮静态任务扩展到多轮序贯决策提供数学基础。

[Title]: Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: Raw exploration trajectories（包含大量失败轨迹）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 open LLM agent 在三个复杂任务上持续改进
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: ETO 的迭代优化框架本质是 Policy → Narrative → Policy 闭环（§8.1）：Stage 1 (P7)：当前 policy 在环境中探索交互、收集失败与成功轨迹（exploration phase）；Stage 2 (P5)：将成功与失败轨迹构成 contrastive trajectory pairs（此为数据组织步骤，不构成独立的 P1 精炼——轨迹内容本身未经 reflection/改写），用 DPO 在 preference pairs 上更新 policy（training phase）。此循环迭代进行（"iterative cycle of exploration and training"）。闭环衔接创新点在于：让 agent 从 exploration failures 而非仅从 expert trajectories 中学习，通过 DPO 的对比学习机制将失败经验转化为策略改进信号。

[Title]: Group-in-Group Policy Optimization for LLM Agent Training
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Raw multi-turn agent-environment interaction trajectories（完整 episode）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 LLM agent 在 ALFWorld, WebShop 和 search-augmented QA 等 benchmark 上执行任务
- [Method]: ⟨RL: GRPO⟩（GiGPO 变体）
- [Mechanism]: 对 GRPO 的细粒度 credit assignment 改进：episode-level 基于完整 trajectory group 计算 macro relative advantage，step-level 通过 anchor state grouping mechanism（跨 trajectory 识别重复环境状态、将同状态下动作分组）计算 micro relative advantage。双层结构保留 GRPO 的 critic-free、低内存、稳定收敛优点，同时解决多轮场景下稀疏/延迟奖励导致的 credit assignment 困难。本质是 Narrative → Policy (P5) 路径下对 RL 算法的 advantage estimation 机制创新。

[Title]: OpenWebVoyager: Building Multimodal Web Agents via Iterative Real-World Exploration, Feedback and Optimization
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: Real-world web exploration trajectories（多模态感知的网页交互轨迹）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {self}
- [Utilization]: 训练 multimodal web agent 在真实网页环境中自主改进
- [Method]: ⟨hybrid⟩
- [Mechanism]: hybrid 由 SFT（imitation learning 初始化）+ ⟨LLM-extract⟩（feedback collection）+ SFT/RL（policy improvement）组成。exploration-feedback-optimization 循环即 Policy → Narrative → Policy 闭环（§8.1）：Stage 0 (P5)：imitation learning 训练 base model 获得基本 web 能力；Stage 1 (P7)：agent 在真实开放网页上探索、收集 trajectory 反馈；Stage 2 (P1)：另一 general-purpose model 判断 trajectory 质量、筛选 well-performing trajectories 作为正样本；Stage 3 (P5)：在高质量 trajectory 上进一步优化 policy。循环可多轮迭代。闭环创新点：真实环境（非合成）+ 多模态感知 + 无 ground-truth reward 下的模型评判驱动的自我改进。

[Title]: AutoWebGLM: A Large Language Model-based Web Navigating Agent
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Web browsing trajectories（hybrid human-AI 构建 + bootstrap RL/ rejection sampling 自生成）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}, {teacher}, {self}
- [Utilization]: 训练 ChatGLM3-6B 成为 automated web navigation agent
- [Method]: ⟨hybrid⟩
- [Mechanism]: hybrid 由 SFT（curriculum training）+ ⟨RL: PPO⟩（reinforcement learning）+ ⟨LLM-extract⟩（rejection sampling）组成。主要贡献在整体系统工程而非闭环机制：(1) HTML simplification algorithm 将复杂网页压缩为关键信息表示；(2) hybrid human-AI 方法构建 web browsing data 做 curriculum SFT——此为 {human}+{teacher} Narrative → Policy (P5)；(3) RL + rejection sampling 做 bootstrap 进一步自我提升——此为 {self} Narrative → Policy (P5)。RL 和 rejection sampling 阶段的自生成数据用于策略提升，但论文贡献重点是完整 agent 系统的构建（HTML 简化 + 数据构建 + 训练 pipeline）而非自生成闭环本身。


[Title]: Large Language Models Can Self-Improve At Web Agent Tasks
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: Synthetic web interaction trajectories（模型自身生成的数据）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 LLM agent 在 WebArena 上执行 long-horizon web navigation 任务
- [Method]: ⟨SFT⟩
- [Mechanism]: 论文核心贡献恰是研究 self-improvement 闭环本身（§8.1）：Stage 1 (P7)：当前 LLM policy 在 WebArena 中自主执行任务，生成 synthetic trajectory 数据（三种不同数据混合策略）；Stage 2 (P5)：用自生成数据 fine-tune 同一模型，将交互经验内化为 policy 权重。论文探索了 self-improvement 的限度、不同合成数据混合策略的效果差异，并贡献了超越简单 benchmark score 的细粒度评估指标（robustness, capabilities, trajectory quality）。闭环机制的核心问题是"什么样的自生成数据能有效驱动 self-improvement"。

[Title]: WebDancer: Towards Autonomous Information Seeking Agency
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Web browsing trajectories（browsing data construction + trajectory sampling 阶段构建）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: 不清楚（abstract 未明示 browsing data 来源是 human / teacher / self）
- [Utilization]: 训练 WebDancer agent 在 GAIA 和 WebWalkerQA 上执行信息检索任务
- [Method]: ⟨SFT⟩, ⟨RL: PPO⟩（或类似 online RL）
- [Mechanism]: 四阶段训练范式：(1) browsing data construction — 构建网页浏览数据；(2) trajectory sampling — 采样交互轨迹；(3) SFT cold start — 将 trajectory 经验通过监督微调内化为 policy 权重（Narrative → Policy, P5）；(4) RL enhancement — 通过 RL 进一步优化 policy（同 P5 路径，以 RL 替代 SFT）。两个训练阶段都是 Narrative → Policy 单步转化，以 SFT+RL 串行组合实现 cold start + generalization 增强。论文贡献在 data-centric 的训练流程设计，而非经验形式的二次转化。

[Title]: STeCa: Step-level Trajectory Calibration for LLM Agent Learning
- [Pathway]: Narrative → Narrative → Policy (§8.3)
- [Source Experience]: Raw exploration trajectories（含 suboptimal actions 的原始交互轨迹）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 通过 calibrated trajectories 做 reinforced training，提升 agent 在 long-horizon 任务上的鲁棒性
- [Method]: ⟨hybrid⟩
- [Mechanism]: hybrid 由 ⟨LLM-extract⟩（reflection-driven calibration）+ RL/SFT（reinforced training）组成。两阶段转化（§8.3）：Stage 1 (P1)：通过 step-level reward comparison 在 exploration 中识别 suboptimal actions，利用 LLM-driven reflection 自动构建 calibrated trajectories——将含错误步骤的 raw trajectory 精炼为修正后的高质量 trajectory（Narrative → refined Narrative）；Stage 2 (P5)：将 calibrated + successful trajectories 合并用于 reinforced training，将精炼后的经验内化为 policy 权重（refined Narrative → Policy）。论文核心贡献在 Stage 1 的 timely calibration 机制：在 long-horizon 任务中，子最优动作逐步累积导致偏离正确轨迹，STeCa 通过 step-level 校准及时纠正偏差。

[Title]: Advancing Tool-Augmented Large Language Models: Integrating Insights from Errors in Inference Trees
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Tree-like expert trajectories from DFSDT search（包含成功路径与失败路径）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}（DFSDT 搜索机制生成 expert trajectories）
- [Utilization]: 训练 LLM 在 16000+ 真实 API 上做多步工具使用推理
- [Method]: ⟨SFT⟩, ⟨RL: DPO⟩
- [Mechanism]: 两阶段训练：(1) SFT 在成功 tool-usage expert trajectories 上微调 LLM 获得基础工具使用能力（Narrative → Policy, P5）；(2) 从 DFSDT inference trees 中提取此前被忽略的失败探索路径，构建 step-wise preference data（成功 vs 失败 trajectory pairs），用 DPO 更新 policy（同 P5，以 preference learning 替代 SFT）。论文贡献在数据利用层面——将 DFSDT 搜索树中的失败分支转化为偏好学习信号，扩展模型学习空间。两阶段均为 Narrative → Policy 单步转化，数据来自搜索机制（{teacher}）而非 agent 自身 rollout。

[Title]: Solving the Granularity Mismatch: Hierarchical Preference Learning for Long-Horizon LLM Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Expert trajectories（被分解为 semantically coherent action groups）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: 不清楚（abstract 未明示 expert trajectories 来源）
- [Utilization]: 训练 LLM agent 在三个 agent benchmark 上执行复杂长时程任务
- [Method]: ⟨RL: DPO⟩（HPL: trajectory-level + step-level + group-level DPO）
- [Mechanism]: 将 expert trajectories 分解为语义连贯的 action groups，在 trajectory-level、group-level、step-level 三个粒度上构建 preference pairs，并通过 dual-layer curriculum（group length 复杂度 + reward gap 难度）从简到繁组织训练。本质是 P5 路径下对 DPO 的多粒度扩展：解决 trajectory-level DPO 信号过粗、step-level DPO 信号过短视的 granularity mismatch 问题。核心创新在 preference signal 的多粒度组织与课程调度，不涉及经验形式的跨载体转化。

[Title]: SPA-RL: Reinforcing LLM Agents via Stepwise Progress Attribution
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Raw multi-step interaction trajectories（含最终任务完成信号）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 LLM agent 在 WebShop, ALFWorld, VirtualHome 上执行 goal-oriented 多步任务
- [Method]: ⟨RL: PPO⟩（SPA-enhanced）
- [Mechanism]: 训练 progress estimator 将 trajectory 的最终完成信号分解为 stepwise progress contribution，为 RL 训练的每步提供细粒度中间奖励。本质是 P5 路径下对 RL reward signal 的 credit assignment 改进：最终任务奖励 → stepwise progress 奖励 → policy 更新。核心创新在 reward redistribution（奖励信号的 step 级分解），不涉及经验形式的跨载体转化。训练 progress estimator 本身是独立的回归任务，不构成 Evaluator (V-Par) 训练意义上的 P4。

[Title]: ToolRL: Reward is All Tool Learning Needs
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Tool-use interaction trajectories（多工具调用序列）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 LLM 在多种工具使用 benchmark 上提升工具选择和调用能力
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 对工具使用场景下的 reward design 做全面研究，系统探索 reward 类型、尺度、粒度和时序动态，提出 principled reward design 后用 GRPO 将 tool-use trajectory 经验内化为 policy 权重。本质是 P5 路径下对 reward 工程的系统性分析：raw trajectory → reward signal（经过精心设计的多维度奖励）→ GRPO → policy。论文贡献在 reward design space 而非经验转化路径。

[Title]: Natural Language Actor-Critic: Scalable Off-Policy Learning in Language Space
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Raw interaction trajectories（reasoning, web browsing, tool-use with dialogue）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 LLM agent 在 reasoning, web browsing, tool-use with dialogue 等任务上执行
- [Method]: ⟨RL: PPO⟩（actor-critic variant with NL critic）
- [Mechanism]: 用 generative LLM critic（产生自然语言反馈而非标量值）替代传统 scalar critic，为 policy 提供更丰富、更具可操作性的训练信号。NL critic 的反馈本质上是 trajectory → natural language feedback（Narrative → Narrative, P1），但该 feedback 作为中间产物直接用于 policy 训练的监督信号（Narrative → Policy, P5），而非作为独立经验产物被存储复用。整体转化仍为 P5：raw trajectory → NL critic 分析 → policy 更新。相对于传统 scalar reward，NL feedback 提供"为什么某动作不佳"的解释，在 open-ended action space 中减少了随机探索的依赖。

[Title]: AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Multi-turn interactive decision-making trajectories（跨多种真实环境）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 LLM agent 在 27 个多样化任务上匹配或超越商业模型
- [Method]: ⟨RL: PPO⟩（ScalingInter-RL）
- [Mechanism]: ScalingInter-RL 通过控制交互轮数实现 exploration-exploitation balance：早期限制交互次数强调 exploitation，后期逐步扩大 horizon 鼓励 exploration 和多样化策略。本质是 P5 路径下对 RL 训练过程中数据收集策略的改进：当前 policy → 交互收集 trajectory（Narrative）→ RL 更新 policy（π-Par）。核心创新在 exploration-exploitation 的阶段调度策略，解决长时程下 policy collapse 问题。

[Title]: Q-SFT: Q-Learning for Language Models via Supervised Fine-Tuning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Static offline interaction datasets（对话、机器人操作、导航等）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt] / [embodied]（含视觉机器人操作）
- [Target Modality]: [txt] / [embodied]
- [Experience Source]: 不清楚（offline datasets，来源取决于具体数据集）
- [Utilization]: 训练 LLM 和 VLM 在多轮对话、机器人操作和导航任务上执行
- [Method]: ⟨SFT⟩（Q-learning as modified SFT）
- [Mechanism]: 将 Q-learning 重新表述为 modified SFT 问题——token 概率直接映射为 Q-values，使训练目标从 pretraining 的 likelihood maximization 平滑过渡到 finetuning 的 near-optimal Q-function learning。本质是 P5 路径下的算法创新：offline trajectory data → Q-SFT objective → policy weights。核心创新在将 value-based RL 的形式转化为与 SFT 兼容的目标函数，无需重新初始化权重或添加新 head，使 offline RL 可规模化应用于 LLM/VLM。

[Title]: Soft Policy Optimization: Online Off-Policy RL for Sequence Models
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Arbitrary online and offline trajectories（来自训练早期、历史 runs、人类专家、其他 policy 或不同解码策略）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {human}, {teacher}
- [Utilization]: 在 code contests 上训练 sequence model policy
- [Method]: ⟨RL: PPO⟩（SPO: Soft RL alternative）
- [Mechanism]: SPO 替代 PPO 实现 online off-policy RL：可学习任意来源（online/offline、当前/历史、自身/他人）的 trajectory，不需要单独 value model。本质是 P5 路径下对 RL 算法的数据效率改进：多源 trajectory → Soft RL objective → policy weights。核心创新在让 RL 不再受 on-policy 限制，从而能利用更丰富多样的 trajectory 数据。

[Title]: Offline RL by Reward-Weighted Fine-Tuning for Conversation Optimization
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Pre-collected conversation trajectories with rewards（短时程问答策略数据）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: 不清楚（pre-collected dataset，来源未明示）
- [Utilization]: 学习 short-horizon question-answering policies（reason about potential answers or ask clarifying questions）
- [Method]: ⟨SFT⟩（reward-weighted fine-tuning）
- [Mechanism]: 将 offline RL 转化为 reward-weighted fine-tuning——按 trajectory reward 加权做 SFT，用与标准 SFT 相似的技术直接优化奖励。本质是 P5 路径下的算法简化：pre-collected trajectory + reward → reward-weighted SFT → policy。核心创新在将 offline RL 简化为 reward-weighted SFT，消除 DPO 等方法中的额外超参数。

[Title]: TGPO: Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Web interaction trajectories（tree-structured trajectory representation merging semantically identical states）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: 不清楚（abstract 未明示 trajectory 来源）
- [Utilization]: 训练 web agent 在 Online-Mind2Web 和 C-WebShop 上执行网页交互任务
- [Method]: ⟨RL: DPO⟩（offline preference optimization with PRM-guided rewards）
- [Mechanism]: 构建 tree-structured trajectory representation 合并跨 trajectory 的语义相同状态以消除标签冲突；Process Reward Model (PRM) 通过 subgoal progress、redundancy detection、action verification 自动生成细粒度奖励（PRM 是规则驱动或轻量训练的奖励生成组件，不构成独立训练的 V-Par）；dynamic weighting mechanism 优先高影响力决策点。本质是 P5 路径下对 preference optimization 的数据表示与奖励信号改进：raw trajectory → tree-structured representation + PRM rewards → DPO → policy。

[Title]: UI-TARS-2 Technical Report: Advancing GUI Agent with Multi-Turn Reinforcement Learning
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: GUI interaction trajectories（data flywheel 自生成 + multi-turn RL 收集）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 训练 native GUI-centered agent model 在 GUI benchmarks、游戏环境和长时程信息检索任务上执行
- [Method]: ⟨hybrid⟩
- [Mechanism]: hybrid 由 SFT（data flywheel 监督训练）+ ⟨RL: PPO⟩（multi-turn RL）组成。核心闭环为 Policy → Narrative → Policy（§8.1）：data flywheel 机制中，当前 policy 生成 GUI 交互数据 → 数据回灌训练更强 policy → 更强 policy 生成更高质量数据，形成自我强化的数据飞轮。同时 stabilized multi-turn RL framework 直接在线训练 policy。论文贡献在闭环的工程实现（数据飞轮 + 稳定多轮 RL + 混合 GUI 环境 + 统一沙盒平台），确保大规模 agent RL 训练的稳定性和效率。

[Title]: ComputerRL: Scaling End-to-End Online Reinforcement Learning for Computer Use Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Desktop interaction trajectories（API + GUI 统一范式中收集）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 训练 open models (GLM-4-9B) 成为 desktop automation agent，在 OSWorld 上评估
- [Method]: ⟨hybrid⟩（RL + SFT 交替的 Entropulse）
- [Mechanism]: Entropulse 训练策略交替执行 RL 和 SFT，缓解 extended RL training 中的 entropy collapse。分布式 RL 基础设施编排数千并行虚拟桌面环境加速 online RL。本质是 P5 路径下的大规模工程实现：online interaction trajectory → RL → policy（交替 SFT 做稳定性正则化）。核心创新在训练基础设施（分布式虚拟桌面）+ 训练稳定性策略（Entropulse），是 P5 在 computer use 领域的 scaling 实践。

[Title]: Mobile-Agent-v3 / GUI-Owl: Fundamental Agents for GUI Automation
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: GUI interaction trajectories（Self-Evolving GUI Trajectory Production 框架自生成）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 训练 GUI-Owl foundational GUI agent model 在 10 个跨桌面和移动端的 GUI benchmark 上执行
- [Method]: ⟨hybrid⟩
- [Mechanism]: hybrid 由 ⟨LLM-extract⟩（automated query generation + correctness validation）+ ⟨RL: GRPO⟩（TRPO: Trajectory-aware Relative Policy Optimization）组成。核心为 Policy → Narrative → Policy 自改进闭环（§8.1）：Stage 1 (P7)：当前 GUI-Owl policy 在云虚拟环境（Android/Ubuntu/macOS/Windows）中执行任务；Stage 2 (P1)：通过 automated query generation 和 correctness validation 对 trajectory 进行迭代精炼——失败的交互被修正为高质量数据（Narrative → refined Narrative）；Stage 3 (P5)：精炼后的 trajectory 通过 Scalable Environment RL（TRPO + fully asynchronous training）内化为 policy 权重。闭环由 Self-Evolving GUI Trajectory Production 框架驱动，实现数据飞轮效应。

[Title]: EvoCUA: Evolving Computer Use Agents via Learning from Scalable Synthetic Experience
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: Synthetic computer-use interaction trajectories（verifiable synthesis engine 生成 + 大规模 sandbox rollout）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 训练 native CUA model 在 OSWorld 上执行计算机操作任务
- [Method]: ⟨hybrid⟩
- [Mechanism]: hybrid 由 SFT（policy optimization）+ ⟨LLM-extract⟩（error analysis + self-correction）组成。核心为 Policy → Narrative → Policy 自持续演化闭环（§8.1）：Stage 1 (P7)：verifiable synthesis engine 自动生成多样化任务及可执行验证器，tens of thousands of asynchronous sandbox rollouts 产生大规模 trajectory 经验；Stage 2 (P1)：iterative evolving learning strategy 识别 capability boundaries——通过 error analysis 和 self-correction 将失败 trajectory 转化为 rich supervision（Narrative → refined Narrative），同时 reinforcement of successful routines 保留成功经验；Stage 3 (P5)：精炼后的经验通过 policy optimization 内化为 π-Par。闭环衔接创新点：能力边界驱动的动态更新策略——不是对所有数据等权重训练，而是识别哪些能力已掌握（保持）、哪些需要修正（转化失败为监督信号）。

[Title]: Agentic Reinforced Policy Optimization (ARPO)
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Multi-turn tool-use interaction trajectories（含工具调用前后的 entropy 变化）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 LLM agent 在计算推理、知识推理和深度搜索等 13 个 benchmark 上执行多轮工具使用
- [Method]: ⟨RL: GRPO⟩（ARPO: entropy-based adaptive rollout + advantage attribution）
- [Mechanism]: ARPO 的核心观察是 LLM 在调用外部工具后 token entropy 显著升高（高度不确定行为）。由此提出：(1) entropy-based adaptive rollout mechanism 在工具调用后的高不确定性步骤动态平衡全局 trajectory 采样与 step-level 采样，促进 exploration；(2) advantage attribution estimation 使 LLM 在 stepwise tool-use 交互中内化 advantage 差异。本质是 P5 路径下对 GRPO 在 agentic 场景的适配改进：raw trajectory → entropy-guided exploration + advantage attribution → GRPO → policy。核心创新在利用 entropy 信号指导 exploration-exploitation 平衡。

[Title]: BEPA: From Off-Policy to On-Policy — Enhancing GUI Agents via Bi-level Expert-to-Policy Assimilation
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Static expert trajectories + self-rolled reachable trajectories under base policy
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {human}（expert trajectories）, {self}（self-rolled trajectories）
- [Utilization]: 训练 end-to-end screenshot-to-action GUI policy 在 OSWorld-Verified 上执行
- [Method]: ⟨RL: PPO⟩（RLVR with bi-level assimilation）
- [Mechanism]: 两层次将静态 expert trajectory 转化为 policy-aligned 训练信号：(LEVEL-1) 在 base policy 下 self-roll 生成 reachable trajectories，使 expert traces 与当前 policy 的能力分布对齐；(LEVEL-2) 构建 per-task 动态更新缓存用于 RLVR。核心问题是解决 off-policy expert trajectories 与 on-policy RL 之间的 structural mismatch 和 distribution shift。本质是 P5 路径下对 expert data 在 online RL 中的利用效率改进：expert + self-rolled trajectory → bi-level alignment → RLVR → policy。

[Title]: GUI-R1: A Generalist R1-Style Vision-Language Action Model For GUI Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Curated high-quality GUI interaction data across multiple platforms（Windows, Linux, MacOS, Android, Web）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: 不清楚（curated data，abstract 未明示来源）
- [Utilization]: 训练 LVLM 成为跨平台 GUI agent，在 8 个 benchmark 上评估
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 借鉴 DeepSeek-R1 的 Reinforcement Fine-Tuning 范式，通过 unified action space rule modeling 将 GUI 操作统一为规则化动作空间，仅用 0.02% 的数据量（3K vs 13M）通过 GRPO 策略优化实现跨平台 GUI 能力。本质是 P5 路径下 R1-style RL 在 GUI 领域的迁移：少量高质量 GUI trajectory → unified action space modeling → GRPO → policy。核心创新在 unified action space rule modeling 使 RL 信号在极少量数据下高效传播。

[Title]: Training Long-Context, Multi-Turn Software Engineering Agents with Reinforcement Learning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: SWE interaction trajectories（execution feedback + iterative improvement）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 Qwen2.5-72B-Instruct 在 SWE-bench Verified 上执行软件工程任务
- [Method]: ⟨hybrid⟩
- [Mechanism]: 两阶段训练：(1) Rejection Fine-Tuning (RFT) 利用 execution feedback 训练 policy 遵循指令和格式——trajectory 执行成功则保留、失败则丢弃（Narrative → Policy, P5）；(2) DAPO (Dynamic Asynchronous Policy Optimization) synchronous RL pipeline 进行迭代改进——agent 与环境交互产生 trajectory，基于执行结果 reward 更新 policy（同 P5）。两阶段串行组合，核心创新在多轮 SWE 场景下 RL 的成功应用（此前 RL 多限于单轮数学/代码），以及 RFT → DAPO 的 pipeline 设计。

[Title]: MobileGUI-RL: Advancing Mobile GUI Agent through Reinforcement Learning in Online Environment
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Online mobile GUI interaction trajectories（self-exploration + filtering 生成的 curriculum tasks）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 训练 vision-based GUI agent 在三个 online mobile-agent benchmark 上执行任务
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 两个关键组件：(1) self-exploration and filtering 合成可学习任务的 curriculum——agent 自主探索生成任务并过滤（Narrative 数据准备）；(2) 将 GRPO 适配到 GUI 导航——trajectory-aware advantages + composite rewards（任务成功 + 执行效率）。本质是 P5 路径下从 offline 到 online 的转变：online interaction trajectory → trajectory-aware GRPO → policy。相对于 offline pre-collected trajectory 训练，online RL 缓解了对特定 UI 模板的 overfitting。

[Title]: Generalization in Online Reinforcement Learning for Mobile Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Online mobile GUI interaction trajectories（AndroidWorld-Generalization benchmark）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 训练 7B VLM agent 在 Android 设备上执行 GUI 自动化任务，研究 zero-shot generalization
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 将问题形式化为 Contextual MDP，用 GRPO + scalable rollout collection system（容器化基础设施 + 异步执行）训练 VLM agent。核心贡献不在转化机制而在 generalization 的实证研究：RL 训练的 agent 在 unseen instances 上提升 26.1%，但在 unseen templates (15.7%) 和 unseen apps (8.3%) 上增益有限。本质是 P5 的 standard online RL 应用，研究重点是泛化能力边界而非转化路径。

[Title]: AgentRL: Scaling Agentic Reinforcement Learning with a Multi-Turn, Multi-Task Framework
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Multi-turn, multi-task agent interaction trajectories（跨 5 个 agentic tasks）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 open LLM agent 在 5 个多样化 agentic tasks 上显著超越 GPT-5, Claude-Sonnet-4, DeepSeek-R1
- [Method]: ⟨RL: PPO⟩（cross-policy sampling + task advantage normalization）
- [Mechanism]: 基础设施层面：fully-asynchronous generation-training pipeline + unified function-call API + containerized environments。算法层面：cross-policy sampling 在 multi-turn 设定中鼓励模型 exploration（用不同 policy 版本或策略收集数据），task advantage normalization 稳定多任务训练。本质是 P5 的大规模工程实现：multi-turn online trajectory → cross-policy exploration → advantage-normalized RL → policy。核心创新在 scaling 基础设施和 multi-task 稳定性。

[Title]: Fine-tuning with RAG for Improving LLM Learning of New Skills
- [Pathway]: Narrative → Narrative → Policy (§8.3)
- [Source Experience]: Agent failure trajectories → extracted compact hints → improved teacher trajectories（三步级联精炼）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}（agent 失败轨迹）, {teacher}（RAG-augmented teacher 生成 improved trajectories）
- [Utilization]: 训练 student agent 在 ALFWorld 和 WebShop 上执行交互任务，消除运行时 RAG 依赖
- [Method]: ⟨SFT⟩
- [Mechanism]: 三步级联精炼（§8.3）：Stage 1 (P1)：从 agent 失败中提取 compact, reusable hints——将含噪声的失败 trajectory 精炼为紧凑的可复用提示（Narrative → refined Narrative）；Stage 2 (P1)：用 hints 通过 one-shot retrieval at episode start 生成 improved teacher trajectories——将 hints 展开为完整的高质量轨迹（Narrative → further refined Narrative）；Stage 3 (P5)：在 hint strings removed 的条件下训练 student model，迫使 student internalize hints 中的知识而非 memorizing 提示字符串。两级 P1 精炼（failure → hints → improved trajectories）是论文核心贡献——中间 representations 逐步提升经验质量，最终通过 SFT 内化为 policy。创新在于将 RAG 的推理时检索收益通过多级蒸馏内化为模型能力。

[Title]: Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards
- [Pathway]: Policy → Narrative → Narrative → Policy (§8.1 + §8.3)
- [Source Experience]: Raw SWE agent attempt trajectories（初次尝试）+ guidance-augmented trajectories（引导后重试）
- [Target Experience]: Updated policy weights (π-Par) + Reward Model (V-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 Qwen-2.5-72B-Instruct 在 SWE-Bench Verified 上执行软件工程任务
- [Method]: ⟨hybrid⟩
- [Mechanism]: hybrid 由 ⟨LLM-extract⟩（agent guidance generation）+ ⟨RL: PPO⟩（RLVR）+ SFT（reward model training）组成。复合转化含两个子路径：主线 Policy → Narrative → Narrative → Policy（§8.1 + §8.3）：Stage 1 (P7)：agent 初次尝试解决 SWE 任务，产生 initial trajectory；Stage 2 (P1)：agent guidance 机制利用 diverse informational cues（high-level strategic plans + dynamic error feedback + environmental interaction cues）将 initial trajectory 精炼为 guided trajectory——Narrative → refined Narrative；Stage 3 (P5)：agent 在 guidance 下重新尝试，产生 guided trajectory 后通过 RLVR 基于 unit test 验证的 reward 更新 policy。旁支 (P4)：guidance-augmented RLVR data 额外用于训练 test-time reward model（Narrative → Evaluator），进一步将 pass@1 从 22.4% 提升至 27.8%。闭环衔接创新：借鉴人类教学法的 agent guidance——在稀疏奖励的复杂 agentic 环境中，主动引导 agent 走向成功轨迹。

[Title]: SCoRe: From Correction to Mastery — Reinforced Distillation of Large Language Model Agents
- [Pathway]: Narrative → Narrative → Policy (§8.3)
- [Source Experience]: Student-generated trajectories（含错误的原始探索轨迹）
- [Target Experience]: Updated student policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}（student 生成）, {teacher}（teacher 纠错）
- [Utilization]: 训练 7B student agent 匹配 72B teacher 的 agentic performance
- [Method]: ⟨hybrid⟩
- [Mechanism]: hybrid 由 ⟨LLM-extract⟩（teacher correction）+ SFT + RL 组成。student-centered 框架（§8.3）：Stage 1 (P7/P1)：student 生成 training trajectory → teacher 仅纠正 earliest error（而非完整 trajectory），生成与 student 能力匹配的 corrected trajectory（Narrative → refined Narrative）；Stage 2 (P5)：student 在 corrected trajectory 上 SFT；Stage 3 (P5)：short-horizon RL 从 verified prefix（错误发生前的正确前缀）开始，target reward 在该步赋予，鼓励超越模仿的自主问题解决。核心创新：teacher 仅在最早错误处纠正（而非提供完整示范），使训练数据精准匹配 student 能力边界，同时 RL 阶段鼓励超越 teacher 的自主探索。

[Title]: Structured Agent Distillation for Large Language Model
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Teacher agent ReAct-style trajectories（含 REASON 和 ACT 段）
- [Target Experience]: Updated student policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: 压缩 large LLM agent 为 smaller student model，在 ALFWorld, HotPotQA-ReAct, WebShop 上部署
- [Method]: ⟨SFT⟩（segment-specific distillation loss）
- [Mechanism]: 将 teacher trajectory 分割为 {[REASON]} 和 {[ACT]} span，对每段施加 segment-specific loss 使 student 在 reasoning fidelity 和 action consistency 两个维度上分别对齐 teacher。本质是 P5 路径下对蒸馏目标的细粒度结构化改进：teacher trajectory → span-level alignment → SFT → student policy。核心创新在 trajectory 的分段结构感知监督（而非 token-level distillation）。

[Title]: Sub-goal Distillation: A Method to Improve Small Language Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: LLM-annotated oracle paths（含 sub-goal 序列标注）
- [Target Experience]: Updated small LM policy weights (π-Par) 分为 planning module 和 execution module
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}（LLM 标注 oracle path with sub-goals）
- [Utilization]: 训练 770M small LM agent 在 ScienceWorld 上执行长时程交互任务
- [Method]: ⟨SFT⟩
- [Mechanism]: 层次化 agent 架构（planning module + execution module）：(1) LLM teacher 标注 oracle path 的 sub-goal 序列——将完整任务路径分解为子目标链（Narrative → Schematic-like sub-goal structure）；(2) planning module 通过 Knowledge Distillation 从 LLM 学习生成 sub-goals；(3) execution module 学习用 elementary actions 完成 sub-goals。两个 module 均通过 SFT 从 LLM 标注数据中学习。本质是 P5 路径下的层次化蒸馏：LLM 标注的 sub-goal path → SFT → planning module + execution module weights。推理时无需 LLM 实时访问。

[Title]: DynaWeb: Model-Based Reinforcement Learning of Web Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Real expert web trajectories + dreamed rollout trajectories（web world model 生成的合成轨迹）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}（expert trajectories）, {teacher}（world model 生成 dreamed rollouts）
- [Utilization]: 训练 web agent policy 在 WebArena 和 WebVoyager 上执行网页导航任务
- [Method]: ⟨RL: PPO⟩（MBRL with interleaved real + dreamed rollouts）
- [Mechanism]: 训练 web world model 预测给定 agent action 后的网页表示，agent policy 在此合成 web 环境中"做梦"（dreaming）——生成大量 rollout action trajectory 进行高效 online RL。Real expert trajectories 随机交织于 on-policy dreamed rollouts 中以提升稳定性和样本效率。本质是 P5 路径下对训练环境的改进：dreamed + real trajectory → RL → policy。World model 是环境模拟器（非经验载体），用于解决 live internet 交互的低效、高成本和风险问题。核心创新在 MBRL 范式在 web agent 训练中的应用。

[Title]: Agentic Reinforcement Learning for Real-World Code Repair
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: GPT-4.1 teacher trajectories（SFT 阶段）+ agent online interaction trajectories（RL 阶段）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}（SFT 阶段）, {self}（RL 阶段）
- [Utilization]: 训练 Qwen3-32B 在 ~1K real-world GitHub issues 上执行代码修复
- [Method]: ⟨SFT⟩, ⟨RL: PPO⟩
- [Mechanism]: 两阶段训练：(1) SFT 在 GPT-4.1 teacher trajectory 上将 Qwen3-32B 蒸馏至与 teacher 性能持平（56x 更小模型）——{teacher} Narrative → Policy (P5)；(2) 在 simplified pipeline 中施加 RL 做进一步 online 优化——{self} Narrative → Policy (P5)。核心发现：train-test environment matching 至关重要（SFT 和 RL 模型均无法跨环境泛化），"thinking mode"未带来增益。贡献在真实仓库代码修复的 RL 训练工程。

[Title]: SoLS: Succeed or Learn Slowly — Sample Efficient Off-Policy RL for Mobile App Control
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Mobile app control interaction trajectories（online off-policy 收集）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 训练 foundation model 在 AndroidWorld 上执行 UI 导航
- [Method]: ⟨RL: PPO⟩（SoLS: off-policy actor-critic variant）
- [Mechanism]: SoLS 基于一个关键洞察：高回报正样本的更新不需要 policy regularization，而负样本（反映 undesirable behavior）的更新可能损害模型性能。由此设计 modified off-policy actor-critic：正样本直接 policy update，负样本施加 conservative regularised update。STR (Successful Transition Replay) 增强机制优先从成功交互中学习。本质是 P5 路径下对 off-policy RL 更新规则的改进：online trajectory → positive/negative decomposition → asymmetric update → policy。

[Title]: IGPO: Information Gain-based Policy Optimization for Multi-Turn LLM Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Multi-turn search-based tool-use trajectories（含最终答案正确性信号）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 LLM agent 在 multi-turn 搜索和工具使用任务上执行
- [Method]: ⟨RL: GRPO⟩（IGPO: information gain intrinsic rewards）
- [Mechanism]: 将每个交互轮次建模为 incremental information acquisition process，定义 turn-level reward 为 policy 对正确答案概率的 marginal increase——直接从模型自身 belief updates 中推导 intrinsic reward，无需外部 reward model 或 Monte Carlo estimation。Intrinsic turn-level rewards 与 outcome-level supervision 结合形成稠密奖励轨迹。本质是 P5 路径下对 sparse reward 问题的解决方案：raw trajectory → belief-update-based intrinsic reward → dense RL → policy。核心创新在以 information gain 作为内在奖励信号。

[Title]: Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Credit Assignment
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Multi-turn tool-use interaction trajectories（MDP 建模的多步决策序列）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 LLM agent 在 multi-turn reasoning 和 search-based tool-use 任务上执行，达到 100% tool execution 成功率
- [Method]: ⟨RL: GRPO⟩（turn-level advantage estimation enhanced）
- [Mechanism]: 提出细粒度 turn-level advantage estimation 策略替代 trajectory-level bandit 设定，使 credit assignment 精确到每个决策步。该策略可融入各种 RL 算法（如 GRPO）。本质是 P5 路径下对 RL 中 advantage estimation 的粒度改进：multi-turn trajectory → turn-level credit assignment → GRPO → policy。核心创新在将 MDP 框架引入 LLM agent RL，使每步决策获得独立信用分配。

[Title]: A³T: ReAct Meets ActRe — When Language Agents Enjoy Training Data Autonomy
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: ReAct-style agent trajectories（自主合成 + ActRe 标注 + contrastive self-training 累积）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}（ReAct policy 自主执行）, {teacher}（ActRe prompting agent 提供 posterior reasoning）
- [Utilization]: 训练 Mistral-7B agent 在 AlfWorld（1-shot 96%, 4-round 100%）和 WebShop（接近人类专家）上执行
- [Method]: ⟨hybrid⟩
- [Mechanism]: hybrid 由 ⟨LLM-extract⟩（ActRe posterior reasoning）+ ⟨RL: PPO⟩（policy gradient with binarized rewards）组成。核心为 Policy → Narrative → Policy 自改进闭环（§8.1）：Stage 1 (P7)：当前 ReAct-style policy 在任务上执行、收集失败 trajectory；Stage 2 (P1)：ActRe prompting agent（独立于被训练 policy 的 teacher 组件）对外部随机采样的 action 生成 posterior reasoning（"解释为什么这个 action 合理"），将 posterior reasoning prepend 到 sampled action 前合成新 trajectory——实现 Autonomous Annotation of Agent Trajectories；Stage 3 (P5)：从合成 trajectory 中筛选成功者，与失败 trajectory 构成 contrastive pairs，通过 policy gradient with binarized rewards 做 contrastive self-training。闭环可多轮迭代（4 rounds），trajectory 持续累积。闭环衔接创新：ActRe 的 posterior reasoning 机制使 agent 无需人工标注即可自主合成高质量 training trajectory。

[Title]: Tree-GRPO: Tree Search for LLM Agent Reinforcement Learning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Tree-structured multi-turn interaction trajectories（tree search 采样产生）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 LLM agent 在 11 个数据集和 3 类 QA 任务上执行
- [Method]: ⟨hybrid⟩
- [Mechanism]: hybrid 由 ⟨MCTS⟩（tree search sampling）+ ⟨RL: GRPO⟩（Tree-GRPO）组成。Tree search 通过共享 common prefix 在固定 token/tool call 预算内增加 rollout 数量。Tree-structured trajectory 天然允许仅用 outcome reward 构建 step-wise process supervision signal。Tree-GRPO 在 intra-tree 和 inter-tree 两个层次估计 grouped relative advantage（理论证明 intra-tree GRPO 等价于 step-level DPO）。本质是 P5 路径下对 exploration 采样策略的改进：tree search → structured trajectory → intra/inter-tree advantage → GRPO → policy。

[Title]: Policy Improvement using Language Feedback Models
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Visual trajectories verbalized to language descriptions（经 LFM 筛选的高质量轨迹）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {teacher}（LLM 提供 feedback 训练 LFM）
- [Utilization]: 通过 imitation learning 训练 instruction-following agent 在 Touchdown, ScienceWorld, ALFWorld 上执行
- [Method]: ⟨SFT⟩（imitation learning on LFM-selected behavior）
- [Mechanism]: Language Feedback Model (LFM) 从 LLM 对 visual trajectory（verbalized to language）的反馈中训练，学会识别 desirable behavior（有助于完成指令的动作）。LFM 作为数据过滤器筛选高质量 trajectory，agent 通过 imitation learning 在筛选后的 trajectory 上训练。本质是 P5 路径下对训练数据质量的改进：raw trajectory → LLM feedback → LFM training（训练一个行为评估器）→ LFM-filtered trajectory → imitation learning → policy。LFM 提供 human-interpretable feedback 且可泛化到 unseen environments。

[Title]: EPO: Hierarchical LLM Agents with Environment Preference Optimization
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Multimodal environment interaction trajectories（ALFRED 环境中含 subgoal 分解）
- [Target Experience]: Updated policy weights (π-Par) for subgoal predictor + low-level action generator
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {self}
- [Utilization]: 训练层次化 agent 在 ALFRED 上执行 long-horizon 具身决策任务（public leaderboard 第一）
- [Method]: ⟨RL: DPO⟩（EPO: environment preference optimization）
- [Mechanism]: 层次化框架将复杂任务分解为 subgoal prediction（高层 LLM）和 low-level action generation（低层 LLM）。EPO 从 environment feedback 中自动生成 preference signals（无需人工标注），用 preference optimization 训练 agent。本质是 P5 路径下 preference learning 在具身环境中的适配：environment interaction → automatic preference signal extraction → DPO → hierarchical policy weights。核心创新在利用 environment 自身反馈自动构建偏好信号，消除对人工标注的依赖。

[Title]: iRe-VLA: Improving Vision-Language-Action Model with Online Reinforcement Learning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Simulated and real-world robot manipulation trajectories（online RL 收集）
- [Target Experience]: Updated VLA policy weights (π-Par)
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 在仿真 benchmark 和真实机器人操作中提升 VLA model 表现
- [Method]: ⟨hybrid⟩（RL + SFT 迭代）
- [Mechanism]: iRe-VLA 在 RL 和 Supervised Learning 之间迭代交替——RL 阶段利用 exploration 发现新策略，SFT 阶段在 RL 收集的数据上稳定训练，避免直接 online RL 对 large VLA model 造成的训练不稳定和计算负担。本质是 P5 路径下的训练策略创新：online interaction trajectory → RL exploration → SFT stabilization → policy。核心创新在 RL 与 SFT 交替迭代的框架设计，解决 VLA model 上 online RL 的稳定性与计算可行性问题。

[Title]: EVOLVE-VLA: Test-Time Training from Environment Feedback for VLA Models
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Environment interaction trajectories at test time（deployment 时实时收集）
- [Target Experience]: Adapted VLA policy weights at test time (π-Par)
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 在部署时持续适应环境，支持 long-horizon tasks, 1-shot learning, cross-task generalization
- [Method]: ⟨hybrid⟩（RL test-time training with learned progress estimator）
- [Mechanism]: 关键挑战是 test time 无 oracle reward signal。解决方案：(1) 训练 learned progress estimator 提供稠密反馈——替代不可得的 oracle reward（但 progress estimator 本身需要训练，属独立模型组件）；(2) accumulative progress estimation mechanism 平滑 noisy point-wise estimates；(3) progressive horizon extension strategy 逐步扩展 horizon 实现渐进策略演化。本质是 P5 路径在 test-time 的特化应用：test-time interaction trajectory → progress-estimator rewards → RL → adapted policy。核心创新在 test-time training 范式：将 RL 从训练阶段移至部署阶段，实现持续自适应。

[Title]: AgentCPM-GUI: Building Mobile-Use Agents with Reinforcement Fine-Tuning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: High-quality Chinese + English GUI trajectories（grounding-aware pre-training + SFT 阶段）+ online RL trajectories
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {human}（SFT trajectories）, {self}（RL 阶段）
- [Utilization]: 训练 8B GUI agent 在中英文移动端 GUI benchmark 上执行（CAGUI 等）
- [Method]: ⟨SFT⟩, ⟨RL: GRPO⟩
- [Mechanism]: 三阶段训练 pipeline：(1) grounding-aware pre-training 增强视觉感知；(2) SFT 在高质量中英文 trajectory 上模仿人类操作；(3) Reinforcement Fine-Tuning with GRPO 提升推理能力。同时引入 compact action space 降低输出长度支持移动端低延迟执行。本质是 P5 的标准训练范式在中文移动 GUI 领域的应用：SFT + RL 串行将 trajectory 经验内化为 policy 权重。

[Title]: ZeroGUI: Automating Online GUI Learning at Zero Human Cost
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Online GUI interaction trajectories（VLM 自动生成任务 + VLM 自动估计奖励）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 训练 UI-TARS 和 Aguvis GUI agent 在 OSWorld 和 AndroidLab 上显著提升
- [Method]: ⟨RL: PPO⟩（two-stage online RL）
- [Mechanism]: 三个组件实现零人工成本的 online GUI agent 训练：(1) VLM-based automatic task generation 从当前环境状态生成多样化训练目标；(2) VLM-based automatic reward estimation 无需手工评估函数判断任务成功；(3) two-stage online RL 持续与环境交互学习。注意此处的 task generation 和 reward estimation 均由 VLM（teacher）完成，而非 agent 自身 policy。本质是 P5 路径下训练过程全自动化：VLM 生成 task + reward → agent online interaction → RL → policy。核心创新在消除 GUI agent RL 训练中的人工标注依赖。

[Title]: UI-Voyager: A Self-Evolving GUI Agent Learning via Failed Experience
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: Mobile GUI interaction trajectories（failed + successful）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 训练 4B mobile GUI agent 在 AndroidWorld 上达到 81.0% Pass@1（超越人类水平）
- [Method]: ⟨hybrid⟩
- [Mechanism]: hybrid 由 ⟨LLM-extract⟩（RFT filtering）+ ⟨RL: DPO⟩（GRSD self-distillation）组成。两阶段自演化闭环（§8.1）：Stage 1 — Rejection Fine-Tuning (RFT, P7 + P5)：agent 自主交互产生 trajectory，成功者保留、失败者丢弃，实现 data 和 model 在完全自主闭环中的 co-evolution（Policy → Narrative → Policy）；Stage 2 — Group Relative Self-Distillation (GRSD, P7 + P1 + P5)：在 group rollout 中识别 critical fork points（成功与失败轨迹的分叉点），从成功 trajectory 构建 dense step-level supervision 以纠正失败 trajectory 中的错误步骤——此为 Narrative → refined Narrative (P1)，精炼后的 trajectory 再用于 policy 更新 (P5)。核心创新在 GRSD 的 self-distillation 机制：无需外部 teacher，agent 自身的成功经验为失败经验提供 step-level 纠正信号。

[Title]: OpenMobile: Building Open Mobile Agents with Task and Trajectory Synthesis
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Synthesized mobile task instructions + agent trajectories（policy-switching strategy 生成）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}（task synthesis pipeline）, {self} + {teacher}（policy-switching rollout）
- [Utilization]: 训练 Qwen2.5-VL / Qwen3-VL 成为 open mobile agent，在 AndroidWorld 上达到 51.7%/64.7%
- [Method]: ⟨SFT⟩
- [Mechanism]: 两个关键组件生成训练数据：(1) scalable task synthesis pipeline 从 exploration 构建 global environment memory，基于此生成多样化、grounded 的任务指令；(2) policy-switching strategy 在 learner 和 expert model 间交替 rollout，捕获标准 imitation learning 中缺失的 error-recovery 数据。合成数据通过 SFT 训练 agent。本质是 P5 路径下的数据合成方法：synthetic task + trajectory → SFT → policy。核心贡献在开放数据合成 pipeline 而非模型训练方法。

[Title]: AndroidGen: Building an Android Language Agent under Data Scarcity
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Android interaction trajectories（AndroidGen 框架收集）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: 不清楚（abstract 未明示 trajectory 来源是 agent 自身生成还是人类标注）
- [Utilization]: 训练 open-source LLM 成为 Android mobile agent 在 AndroidWorld, AitW 上执行
- [Method]: ⟨SFT⟩
- [Mechanism]: AndroidGen 框架在数据稀缺条件下增强 LLM-based agent 能力：通过框架收集给定人类任务的 trajectories，用这些 trajectories 训练 open-source LLM 成为 mobile agent。本质是 P5 的标准数据收集+训练流程，核心贡献在数据稀缺场景下的 trajectory 收集框架设计。

[Title]: AppVLM: A Lightweight Vision Language Model for Online App Control
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: App control trajectories（AndroidControl dataset offline + AndroidWorld online 收集）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {human}（AndroidControl dataset）, {self}（AndroidWorld online collection）
- [Utilization]: 训练 lightweight VLM 成为手机 app agent，在 AndroidControl 和 AndroidWorld 上执行
- [Method]: ⟨SFT⟩
- [Mechanism]: 两阶段 SFT 训练：(1) 在 AndroidControl dataset 上 offline fine-tune 获得基础 app 控制能力；(2) 从 AndroidWorld 环境在线收集交互数据做 further training 精炼 policy。本质是 P5 的最简形式——两阶段 SFT 将 trajectory 经验内化为 policy 权重。核心贡献在 lightweight 架构设计（比 GPT-4o 快 10 倍且匹配其成功率）。

[Title]: Step-GUI Technical Report
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: Model-generated GUI trajectories（self-evolving training pipeline 产生）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 训练 Step-GUI 模型家族（4B/8B）在 AndroidWorld, OSWorld, ScreenShot-Pro 上执行
- [Method]: ⟨hybrid⟩
- [Mechanism]: hybrid 由 ⟨LLM-extract⟩（Calibrated Step Reward System）+ SFT/RL（policy training）组成。Self-evolving training pipeline (§8.1)：Stage 1 (P7)：当前 Step-GUI policy 生成 GUI interaction trajectory；Stage 2 (P1)：Calibrated Step Reward System 通过 trajectory-level calibration 将 model-generated trajectory 转化为可靠训练信号（>90% annotation accuracy, 10-100x 更低成本）——Narrative → refined Narrative with calibrated rewards；Stage 3 (P5)：精炼后的 signal 用于 policy training 更新 π-Par。闭环可持续迭代。此外还贡献了 GUI-MCP（Model Context Protocol for GUI automation）和 AndroidDaily benchmark。

[Title]: GUI-GENESIS: Automated Synthesis of Efficient Environments with Verifiable Rewards for GUI Agent Post-Training
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: GUI interaction trajectories（在自动合成的 lightweight web environments 中收集）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 训练 GUI agent 在 held-out real-world tasks 上执行，超越 real-world RL baselines 3.27%
- [Method]: ⟨RL: PPO⟩（RL with code-native verifiable rewards）
- [Mechanism]: GUI-GENESIS 的核心贡献在环境端而非经验转化端：用 multimodal code models 将真实应用重建为 lightweight web environments，配备 code-native executable assertions 提供确定性奖励信号（消除 visual estimation noise）。Agent 在这些合成环境中通过 RL 训练：interaction trajectory → verifiable reward → RL → policy (P5)。环境延迟降低 10x、每 epoch 成本降低 $28,000+。发现 models 能合成自己尚未解决的环境——暗示 self-improving agents 的可能路径。

[Title]: Grounding Multimodal LLMs to Embodied Agents that Ask for Help with Reinforcement Learning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Embodied interaction trajectories（Ask-to-Act task 中的多模态交互序列，含 clarification questions）
- [Target Experience]: Updated VLA policy weights (π-Par)
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 训练 MLLM 成为能主动询问澄清问题的 household robot VLA policy
- [Method]: ⟨RL: PPO⟩（online RL with LLM-generated rewards）
- [Mechanism]: 在 Ask-to-Act 任务中，agent 需在 partial observability 下策略性地提出最少但最相关的澄清问题。通过 online RL with LLM-generated rewards 训练 MLLM——LLM 自动生成 reward 替代人工标注和手工 reward 工程。本质是 P5 在 embodied agent 领域首次成功应用 online RL with LLM rewards：embodied interaction trajectory → LLM-generated reward → RL → VLA policy。核心创新在将"asking for help"作为可学习的策略行为。

[Title]: UI-S1: Advancing GUI Automation via Semi-online Reinforcement Learning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Offline GUI trajectories（pre-collected）+ rollout 过程中恢复的 divergence
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {human}（offline expert trajectories）, {self}（rollout 产生的输出）
- [Utilization]: 训练 7B GUI agent 在 AndroidWorld, AITW 等 4 个动态 benchmark 上达到 SOTA
- [Method]: ⟨RL: PPO⟩（Semi-online RL with Patch Module + discounted future returns）
- [Mechanism]: Semi-online RL 在 offline trajectory 上模拟 online RL 效果：(1) Patch Module 在 rollout 过程中自适应恢复 rollout 与 expert trajectory 间的 divergence；(2) discounted future returns 引入长期训练信号，加权 step-level 和 episode-level advantages。本质是 P5 路径下训练范式的创新：在 offline trajectory 上通过 Patch Module 实现 online-like RL，融合 offline 的数据效率和 online 的多步推理能力。

[Title]: π*0.6: a VLA That Learns From Experience
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Heterogeneous robot interaction data（demonstrations + on-policy collection + expert teleoperated interventions）
- [Target Experience]: Updated VLA policy weights (π-Par)
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {human}（demonstrations + teleoperated interventions）, {self}（on-policy collection）
- [Utilization]: 训练 VLA 执行折叠衣物、组装盒子、制作浓缩咖啡等真实家庭任务
- [Method]: ⟨hybrid⟩（offline RL pretraining + online RL with advantage conditioning）
- [Mechanism]: RECAP (RL with Experience and Corrections via Advantage-conditioned Policies) 方法：(1) offline RL pre-training 在 heterogeneous data 上训练 generalist VLA (π*0.6)；(2) advantage-conditioned policies 将 heterogeneous data（demonstrations, on-policy, expert teleoperated interventions during autonomous execution）统一纳入 self-improvement process；(3) on-robot data collection 实现 downstream task specialization。本质是 P5 的 multi-source RL 实现：heterogeneous trajectory → advantage conditioning → RL → specialized VLA policy。

[Title]: VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable RL
- [Pathway]: Narrative → Evaluator → Policy (§8.2)
- [Source Experience]: Robotic manipulation trajectories（multi-modal multi-turn conversation 形式）
- [Target Experience]: Updated VLA policy weights (π-Par) + Process Reward Model (V-Par)
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 训练 OpenVLA-7B 在 LIBERO 40 个 challenging 任务上超越最强 finetuned baseline 4.5%
- [Method]: ⟨hybrid⟩
- [Mechanism]: hybrid 由 SFT（PRM training）+ ⟨RL: PPO⟩（RL with PRM rewards）组成。两阶段复合转化 (§8.2)：Stage 1 (P4)：fine-tune pretrained VLM 作为 robotic Process Reward Model (PRM)，在自动提取的 task segments 上以 pseudo reward labels 训练——trajectory segments → PRM (V-Par)；Stage 2 (P5 + P6)：PRM 提供 dense process rewards，结合 final outcome signal，通过 critic-free policy gradient 更新 VLA policy。工程贡献包括 curriculum selection strategy, GPU-balanced vectorized environments, batch decoding, critic warmup。发现 test-time optimization 的 scaling law 早期迹象（"inference scaling laws in robotics"）。

[Title]: Agent-World: Scaling Real-World Environment Synthesis for Evolving General Agent Intelligence
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: Multi-environment tool-use interaction trajectories（thousands of real-world environment themes）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 Agent-World-8B/14B 在 23 个 agent benchmarks 上超越 strong proprietary models
- [Method]: ⟨hybrid⟩
- [Mechanism]: hybrid 由 ⟨LLM-extract⟩（environment-task discovery）+ RL（multi-environment RL）组成。Self-evolving training arena (§8.1)：Stage 1 (P7)：Agentic Environment-Task Discovery 从数千真实世界 themes 中自主探索和合成 verifiable tasks with controllable difficulty——environment 维度上的自生成；Stage 2 (P7)：Continuous Self-Evolving Agent Training 中的 agent 在合成环境中 rollout 产生 trajectory；Stage 3 (P1/P5)：dynamic task synthesis 自动识别 capability gaps 并生成针对性任务，agent 通过 multi-environment RL 更新 policy。闭环特色在于 agent policies 与 environments 的 co-evolution——环境随 agent 能力增长而动态调整难度。

[Title]: BPO: Beyond Policy Optimization — A Data Curation Flywheel for Sparse-Reward Long-Horizon Planning
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: Agentic planning trajectories（bootstrapping + extrapolation + refinement 三阶段产生）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 reasoning model 在 ALFWorld, ScienceWorld, WebShop 上执行 long-horizon, sparse-reward 规划
- [Method]: ⟨hybrid⟩
- [Mechanism]: hybrid 由 ⟨LLM-extract⟩（planning quaternions with long-short CoT fusion）+ SFT + RL（reward-gated rejection sampling）组成。Self-improving data flywheel (§8.1) 三阶段：Stage 1 Bootstrapping (P7 → P5)：agent 用 planning quaternions + long-short CoT fusion 高效推理并 rollout，产生 trajectory → policy 初始训练；Stage 2 Extrapolation (P7 → P5)：通过 complexity-stratified curriculum learning 将 policy 推到 OOD tasks，产生更多样化的 trajectory → 继续训练；Stage 3 Refinement (P7 → P1 → P5)：reward-gated rejection sampling 筛选高质量经验，agent iteratively refines itself——仅在被选中的经验上学习。闭环创新点在 data curation 而非 policy optimization：通过 reward-gated 筛选机制确保数据飞轮的每一轮只注入高质量经验。

[Title]: SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Robotic manipulation trajectories（VLA-specific trajectory sampling + exploration-enhancing strategies）
- [Target Experience]: Updated VLA policy weights (π-Par)
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 训练 OpenVLA-OFT 在 LIBERO 和 RoboTwin 上达到 SOTA，真实任务中超越 SFT
- [Method]: ⟨RL: PPO⟩（SimpleVLA-RL framework）
- [Mechanism]: 基于 veRL 构建 VLA-specific RL 框架：VLA-specific trajectory sampling, scalable parallelization, multi-environment rendering, optimized loss computation, exploration-enhancing strategies。本质是 P5 在 VLA 领域的工程化实现。发现 "pushcut" 现象——RL 训练中 policy 发现 training process 中未曾出现的新 pattern。核心贡献在 RL 基础设施的 VLA 适配和 scaling。

[Title]: EPO: Entropy-regularized Policy Optimization for LLM Agents RL
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Multi-turn interaction trajectories（30+ turns per episode, sparse reward）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 LLM agent 在 ScienceWorld (+152%) 和 ALFWorld (+19.8%) 上执行
- [Method]: ⟨RL: PPO⟩（EPO: entropy-regularized variant）
- [Mechanism]: 识别多轮稀疏奖励设定中特有的 "exploration-exploitation cascade failure"：早期 policy premature convergence（稀疏反馈导致 agent 过早锁定 flawed low-entropy strategy）→ 后期 policy collapse（传统 entropy regularization 反而促进 chaotic exploration）。EPO 通过三个协同机制打破此失败循环：(1) multi-turn 设定中采用 entropy regularization 增强 exploration；(2) entropy smoothing regularizer 将 policy entropy 约束在历史均值范围内防突变；(3) adaptive phase-based weighting 跨训练阶段平衡 exploration/exploitation。理论证明 EPO 保证单调递减的 entropy variance。本质是 P5 路径下对 RL entropy 控制的重新设计。

[Title]: RLVMR: Reinforcement Learning with Verifiable Meta-Reasoning Rewards for Robust Long-Horizon Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Long-horizon interaction trajectories with explicit cognitive tags（planning, exploration, reflection）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 7B agent 在 ALFWorld 最难的 unseen task split 上达到 83.6% 成功率
- [Method]: ⟨RL: PPO⟩（critic-free policy gradient with meta-reasoning rewards）
- [Mechanism]: 关键洞察：仅优化最终任务成功的 RL 会强化 flawed/inefficient reasoning paths（inefficient exploration 问题）。RLVMR 让 agent 显式标注认知步骤（planning, exploration, reflection），对有助于有效问题解决的行动提供 programmatic rule-based process rewards。Process-centric rewards 与 final outcome signal 结合。本质是 P5 路径下 reward shaping 的 meta-cognitive 扩展：trajectory with cognitive tags → process reward + outcome reward → RL → policy。效果体现在 reasoning quality 提升（redundant actions 显著减少，error recovery 增强）。

[Title]: Tool-R1: Sample-Efficient Reinforcement Learning for Agentic Tool Use
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Tool-use interaction trajectories（generating executable Python code, 含代码执行结果）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 LLM 在 GAIA benchmark 上执行通用、组合式、多步工具使用
- [Method]: ⟨RL: GRPO⟩（outcome-based reward: LLM answer judgment + code execution success）
- [Mechanism]: Tool-R1 让 LLM 生成 executable Python code 完成工具使用，支持用户自定义工具和标准库、跨步变量共享构建 coherent workflows。Outcome-based reward 结合 LLM-based answer judgment 和 code execution success。为提升训练效率，dynamic sample queue 缓存和复用高质量 trajectory 降低在线采样开销。本质是 P5 在工具使用场景的应用：tool-use trajectory → outcome reward → GRPO → policy。核心创新在工具使用的代码化表征和动态样本队列的效率优化。

[Title]: EvolveSearch: An Iterative Self-Evolving Search Agent
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: Web search trajectories（agent 自主产生 + SFT/RL 迭代增强）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 web search agent 在 7 个 MHQA benchmarks 上持续提升，最终平均超越 SOTA 4.7%
- [Method]: ⟨hybrid⟩
- [Mechanism]: hybrid 由 SFT + RL 交替迭代组成。Iterative self-evolution framework (§8.1)：(1) 初始 policy 在 open web search 中产生 trajectory；(2) SFT 在成功的 self-generated trajectory 上训练 policy (P7 → P5)；(3) RL 进一步优化 policy (P5)；(4) 更新后的 policy 产生更高质量的 trajectory——回到步骤 (2)，形成迭代闭环。完全无需 external human-annotated reasoning data。闭环创新点：SFT 和 RL 的交替迭代结合——SFT 提供稳定初始化防止 RL 过早收敛（open-search domain 中数据利用效率低的问题），RL 提供 exploration-driven improvement。

[Title]: WebEvolver: Enhancing Web Agent Self-Improvement with Coevolving World Model
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: Web interaction trajectories（agent 自主采样 + World Model 生成的 self-instructed training data）
- [Target Experience]: Updated agent policy weights (π-Par) + Updated World Model weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 web agent 在 Mind2Web-Live, WebVoyager, GAIA-web 上持续自我改进
- [Method]: ⟨hybrid⟩
- [Mechanism]: hybrid 由 SFT（agent + World Model training）+ ⟨LLM-extract⟩（self-instructed data generation）组成。核心创新在引入 co-evolving World Model LLM 解决 self-improvement 的 stagnation 问题 (§8.1)：Stage 1 (P7)：agent policy 在 web 环境中 rollout 产生 trajectory；Stage 2：World Model 从 trajectory 中学习预测 next observation given current observation + action——此为环境建模而非经验转化，但 World Model 本身也被持续训练更新；Stage 3a (P7)：World Model 作为 virtual web server 生成 self-instructed training data，供 agent policy 持续精炼 (P5)；Stage 3b：World Model 作为 inference 时的 imagination engine，通过 look-ahead simulation 指导 action selection。两个 LLM (agent + world model) co-evolve 形成相互促进的闭环，无需从更强 closed-source model 蒸馏。

[Title]: OpenClaw-RL: Train Any Agent Simply by Talking
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Live agent interaction next-state signals（user reply, tool output, terminal/GUI state change）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [cross-modal]（conversations, terminal, GUI, SWE, tool-call traces 等多种交互模态）
- [Target Modality]: [cross-modal]
- [Experience Source]: {self}
- [Utilization]: 训练 personal agents（从用户使用中持续改进）和 general agents（跨 terminal/GUI/SWE/tool-call 设置）
- [Method]: ⟨hybrid⟩
- [Mechanism]: hybrid 由 ⟨LLM-extract⟩（PRM judge + Hindsight-Guided OPD）+ ⟨RL: PPO⟩（online policy update）组成。核心观察：每次 agent 交互产生的 next-state signal 包含两类信息——(1) evaluative signals 通过 PRM judge 提取为 scalar reward；(2) directive signals 通过 Hindsight-Guided On-Policy Distillation (OPD) 从 next state 提取 textual hints、构建 enhanced teacher context、提供 token-level directional advantage supervision（比 scalar reward 更丰富）。异步架构使 model serving、PRM judging 和 policy training 同时进行。本质是 P5 下将 next-state signal 作为通用在线学习源：interaction next-state → PRM reward + OPD directive signal → online RL → policy。

[Title]: What Can RL Bring to VLA Generalization? An Empirical Study
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Embodied interaction trajectories（comprehensive benchmark 中收集）
- [Target Experience]: Updated VLA policy weights (π-Par)
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 评估 RL fine-tuned VLA 在 visual, semantic, execution 维度的泛化能力
- [Method]: ⟨RL: PPO⟩（与 DPO, GRPO 对比）
- [Mechanism]: 系统性实证研究——对比 RL (PPO/DPO/GRPO) 与 SFT 对 VLA 泛化的影响。发现 PPO 在 semantic understanding 和 execution robustness 上显著超越 SFT，而 visual robustness 持平；PPO 对 VLA 比 LLM-derived methods (DPO/GRPO) 更有效。论文贡献在 empirical understanding 而非新转化机制。本质是 P5 路径下不同 RL 算法的效果对比研究。

[Title]: VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning with Verified Rewards in World Simulators
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Simulated rollout trajectories（data-driven world model 作为可控模拟器产生）
- [Target Experience]: Updated VLA policy weights (π-Par)
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}（policy rollout in simulator）
- [Utilization]: 训练 VLA model 在 perturbed conditions 下维持稳定任务执行
- [Method]: ⟨RL: PPO⟩（RFT with world-model-based rewards）
- [Mechanism]: 从真实交互数据训练 data-driven world model 作为可控模拟器——预测给定 action 后的未来视觉观察。Policy 在模拟器中 rollout，dense trajectory-level rewards 从 goal-achieving references 中导出。<400 fine-tuning steps 即可超越 SFT baseline。本质是 P5 在 model-based RL 范式下的实现：world model → simulated rollout trajectory → dense reward → RL → VLA policy。核心创新在 world-model-based RFT 作为实用后训练范式。

[Title]: Explorer: Scaling Exploration-driven Web Trajectory Synthesis for Multimodal Web Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Synthesized multimodal web trajectories（94K+ successful trajectories, 49K URLs, 720K screenshots）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {teacher}（web exploration + refinement 合成）
- [Utilization]: 训练 Explorer multimodal web agent 在 Mind2Web-Live, Multimodal-Mind2Web, MiniWob++ 上执行
- [Method]: ⟨SFT⟩
- [Mechanism]: 通过 extensive web exploration and refinement 合成大规模多样化 web trajectory 数据集（平均 28 cents/successful trajectory）。用此数据集 SFT 训练 multimodal web agent。本质是 P5 的数据 scaling 贡献：大规模合成 trajectory → SFT → policy。论文核心在数据合成 recipe 而非转化机制。

[Title]: TGRPO: Fine-tuning VLA Model via Trajectory-wise Group Relative Policy Optimization
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Robot manipulation trajectories（online RL 收集）
- [Target Experience]: Updated VLA policy weights (π-Par)
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 训练 VLA model 在 LIBERO 四类任务上达到 80.7% 平均成功率
- [Method]: ⟨RL: GRPO⟩（TGRPO: trajectory-wise group relative optimization）
- [Mechanism]: 两个关键设计：(1) LLM 生成的 task analysis 自动构建 dense reward function，提供细粒度反馈加速收敛和改善 credit assignment；(2) group-based strategy 并行采样和归一化多条 trajectory，通过相对比较降低方差。整合 trajectory-level 和 step-level advantage estimation 同时捕获全局和局部优化信号（无需 value network）。本质是 P5 路径下 GRPO 在 VLA 场景的适配：task analysis → dense reward → group-based GRPO → VLA policy。

[Title]: SQL-Trail: Multi-Turn Reinforcement Learning with Interleaved Feedback for Text-to-SQL
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Multi-turn database interaction trajectories（含 execution feedback）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 7B/14B model 在 BIRD-SQL 等 benchmark 上超越 larger proprietary systems 平均 5%
- [Method]: ⟨RL: PPO⟩（adaptive turn-budget + composite reward panel）
- [Mechanism]: 将 Text-to-SQL 从 single-pass 范式转变为 multi-turn RL agent 范式：agent 与数据库环境交互，利用 execution feedback 迭代精炼 SQL 预测。两个核心设计：(1) adaptive turn-budget allocation 根据问题难度缩放交互深度；(2) composite reward panel 同时激励 SQL 正确性和高效探索。数据效率比 single-pass RL SOTA 高 18x。本质是 P5 在 Text-to-SQL 领域的 multi-turn RL 实现。

[Title]: The Generalization Gap in Offline Reinforcement Learning
- [Pathway]: Narrative → Policy (P5)（研究多种 offline learning 算法）
- [Source Experience]: Pre-collected trajectories from Procgen and WebShop（varying sizes and skill-levels）
- [Target Experience]: Policy weights（via online RL, offline RL, sequence modeling, or BC）
- [Source Modality]: [txt] / [vis+txt]
- [Target Modality]: [txt] / [vis+txt]
- [Experience Source]: {human}（pre-collected datasets）
- [Utilization]: 评估各算法在 train 和 test 环境上的泛化能力
- [Method]: ⟨hybrid⟩（比较 online RL, offline RL, sequence modeling, BC）
- [Mechanism]: 实证研究论文——提出首个 offline learning 泛化评估 benchmark，比较 online RL, offline RL, sequence modeling, BC 在新环境上的泛化能力。核心发现：(1) offline learning 算法在新环境上弱于 online learning；(2) BC 在 multi-environment data 上表现强劲；(3) 数据多样性比数据规模对泛化更重要。论文本身不提出新转化机制，而是对现有 P5 路径下各种算法的泛化能力做系统比较。

[Title]: PAE: Proposer-Agent-Evaluator — Autonomous Skill Discovery For Foundation Model Internet Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Web navigation trajectories（agent 自主尝试 task proposer 生成的任务）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {self}
- [Utilization]: 训练 web navigation agent 在 WebVoyager 和 WebArena 上达到 SOTA
- [Method]: ⟨RL: PPO⟩（reward from VLM-based success evaluator）
- [Mechanism]: 三个角色协同：(1) context-aware task proposer 利用环境上下文（user demos 或 website name）自主提出任务——消除对 human-annotated instructions 的依赖；(2) agent policy 在真实环境中尝试任务并产生 trajectory；(3) VLM-based success evaluator 自动评估 trajectory 成功与否作为 RL reward。本质是 P5 的全自动化训练流程：auto-proposed task → agent interaction trajectory → VLM evaluator reward → RL → policy。任务提议和评估由 VLM (teacher) 完成，agent 自身 policy 负责交互和 RL 学习。

[Title]: LongNav-R1: Horizon-Adaptive Multi-Turn RL for Long-Horizon VLA Navigation
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Navigation interaction trajectories（multi-turn conversation between VLA policy and embodied environment）
- [Target Experience]: Updated VLA policy weights (π-Par)
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 训练 Qwen3-VL-2B 在 object navigation 上从 64.3% 提升到 73.0%（仅 4000 rollout trajectories）
- [Method]: ⟨RL: PPO⟩（Horizon-Adaptive Policy Optimization）
- [Mechanism]: 将导航重新形式化为 VLA policy 与 embodied environment 之间的 continuous multi-turn conversation。Horizon-Adaptive Policy Optimization 在 advantage estimation 中显式考虑不同 horizon 长度，实现 extended sequences 上精确的 temporal credit assignment。本质是 P5 在 long-horizon navigation 的 multi-turn RL 实现。核心创新在 horizon-adaptive advantage estimation 解决不同长度轨迹的 credit assignment 偏差。

[Title]: OS-Copilot: Towards Generalist Computer Agents with Self-Improvement
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: OS-level interaction trajectories（web, code terminals, files, multimedia, third-party apps）
- [Target Experience]: Updated policy weights (π-Par) + accumulated skills (Narrative)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 训练 FRIDAY agent 在 GAIA 上超越先前方法 35%，在 Excel 和 PowerPoint 上自我改进
- [Method]: ⟨hybrid⟩（SFT + RL 或其他自我改进机制，abstract 未详述具体算法）
- [Mechanism]: FRIDAY 作为 self-improving embodied agent，在 OS 层面跨 web, code terminals, files, multimedia, third-party apps 交互。Self-improvement 体现在：从先前任务中积累技能（accumulated skills from previous tasks），在未见应用上展现强泛化。Abstract 未详细描述训练机制，但"self-improving"的核心是交互经验 → 技能积累 (Narrative) → 策略提升 (Policy)。本质是 P5 在 OS-scale generalist agent 的应用，技能积累机制构成从经验到能力的桥梁。

[Title]: Go-Browse: Training Web Agents with Structured Exploration
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Web exploration trajectories（graph search 结构化探索收集）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}（graph search exploration 生成）
- [Utilization]: 训练 7B model 在 WebArena 上达到 21.7% 成功率（超越 GPT-4o mini 2.4%）
- [Method]: ⟨SFT⟩
- [Mechanism]: 将数据收集形式化为 graph search——在 web 环境中结构化探索，跨 exploration episodes 复用信息，自动收集 10K successful task-solving trajectories + 40K interaction steps。用此数据集 SFT 训练 web agent。本质是 P5 的数据收集方法创新：graph-structured exploration → diverse trajectory data → SFT → policy。

[Title]: RandomWorld: Procedural Environment Generation for Tool-Use Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Synthetic tool-use trajectories（RandomWorld pipeline 程序化生成）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}（procedural generation 合成）
- [Utilization]: 训练 tool-use agent 在 NESTFUL 等 benchmark 上达到新 SOTA
- [Method]: ⟨SFT⟩, ⟨RL: PPO⟩
- [Mechanism]: RandomWorld pipeline 程序化生成 interactive tools 和 compositional tool-use data。SFT 和 RL 在合成数据上训练模型，下游性能随 RandomWorld 数据量 scaling。本质是 P5 的数据合成贡献：procedurally generated tool-use data → SFT + RL → policy。核心创新在交互式、组合式的合成工具使用数据生成 pipeline。

[Title]: AEPO: Agentic Entropy-Balanced Policy Optimization
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Multi-turn web agent tool-use trajectories（rollout 阶段在线收集）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 Qwen3-14B 在 GAIA (47.6%), Humanity's Last Exam (11.2%), WebWalker (43.0%) 上执行
- [Method]: ⟨RL: GRPO⟩（AEPO: entropy-balanced variant）
- [Mechanism]: 识别主流 agentic RL 算法中 excessive reliance on entropy signals 导致的 training collapse。两个核心组件：(1) dynamic entropy-balanced rollout mechanism——通过 entropy pre-monitoring 自适应分配全局和分支采样预算，对连续高熵工具调用步施加 branch penalty 防止 over-branching；(2) Entropy-Balanced Policy Optimization——在高熵 clipping term 中插入 stop-gradient 保留并正确重缩放梯度，entropy-aware advantage estimation 优先学习高不确定性 token。本质是 P5 路径下 entropy 管理的系统性改进。

[Title]: PORTool: Importance-Aware Policy Optimization with Rewarded Tree for Multi-Tool-Integrated Reasoning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Multi-tool-integrated reasoning trajectories（rewarded rollout tree 中的分支轨迹）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 tool-use agent 在 multi-tool-integrated reasoning 任务上提升 final-answer accuracy 并减少 tool-call steps
- [Method]: ⟨hybrid⟩
- [Mechanism]: hybrid 由 ⟨MCTS⟩（rewarded rollout tree）+ ⟨RL: GRPO⟩（importance-aware policy optimization）组成。Rewarded rollout tree 中 trajectory 共享 prefix 后分支，使同一下文中不同 tool-use 决策可直接比较。每步 importance 由 correctness-dominant signal（该步的后代能否最终产生正确答案）+ auxiliary term（tool calls 是否满足格式约束并执行成功）估计。策略更新同时受 branching decision 的局部比较和 trajectory 全局质量指导。本质是 P5 路径下 tree search 与 importance-aware credit assignment 的结合。

[Title]: SWE-ZERO to SWE-HERO: Execution-free to Execution-based Fine-tuning for Software Engineering Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Distilled trajectories from Qwen3-Coder-480B（300K SWE-ZERO + 13K SWE-HERO）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}（distilled from Qwen3-Coder-480B）
- [Utilization]: 训练 Qwen2.5-Coder 系列模型在 SWE-bench Verified 上达到 62.2%（32B），zero-shot 迁移至多语言 44.1%
- [Method]: ⟨SFT⟩（two-stage evolutionary refinement）
- [Mechanism]: 两阶段 SFT 蒸馏：(1) SWE-ZERO——大规模 execution-free trajectory 掌握代码语义和仓库级推理；(2) SWE-HERO——targeted execution-backed refinement 将语义直觉转化为严格工程工作流。本质是 P5 的蒸馏实现：teacher (Qwen3-Coder-480B) trajectory → two-stage SFT → student policy。核心创新在 evolutionary refinement strategy——从 execution-free 到 execution-backed 的渐进式蒸馏。

[Title]: MagicGUI: A Foundational Mobile GUI Agent with Scalable Data Pipeline and Reinforcement Fine-tuning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Large-scale GUI-centric multimodal data（open-source repositories + automated crawling + targeted manual annotation 聚合）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {human}（manual annotation）, {teacher}（automated crawling/synthesis）
- [Utilization]: 训练 MagicGUI foundational mobile GUI agent 在 Magic-RICH 和十几个公开 benchmark 上执行
- [Method]: ⟨SFT⟩（large-scale continue pre-training）, ⟨RL: GRPO⟩（reinforcement fine-tuning with spatially enhanced composite reward + dual filtering）
- [Mechanism]: 两阶段训练：(1) scalable GUI Data Pipeline 聚合最大最多样的 GUI-centric multimodal data（7.8M samples），做 large-scale continue pre-training 增强感知和 grounding；(2) Reinforcement Fine-tuning 采用 spatially enhanced composite reward 和 dual filtering strategy 做 policy 优化。本质是 P5 的标准大规模训练范式在 mobile GUI 领域的 comprehensive 实现。

[Title]: ADMIRE: Adaptive Milestone Reward for GUI Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Mobile GUI interaction trajectories（含成功与失败探索）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 训练 Mobile GUI Agent 在 AndroidWorld 上提升 10%+ 绝对成功率
- [Method]: ⟨RL: PPO⟩（ADMIRE: milestone-anchored reward）
- [Mechanism]: ADMIRE 解决 reward fidelity 与 density 的 trade-off：outcome reward 保真度高但稀疏，process reward 稠密但易偏差和 reward hacking。核心机制：(1) 从成功探索中动态蒸馏 milestones，将 trajectory 锚定到 milestones 构建可验证的自适应奖励系统；(2) asymmetric credit assignment strategy——对成功 trajectory 去噪（denoise），对失败 trajectory 架桥（scaffold，用最近 milestone 提供部分信用）。本质是 P5 路径下 reward shaping 的创新：successful trajectory → milestone extraction → adaptive dense reward → RL → policy。方法跨 RL 算法和环境（web navigation, embodied tasks）泛化。

[Title]: TT-VLA: On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Test-time environment interaction trajectories（部署时实时收集的 step-by-step task-progress signals）
- [Target Experience]: Adapted VLA policy weights at test time (π-Par)
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 在推理时实时适应 dynamic, previously unseen scenarios
- [Method]: ⟨RL: PPO⟩（test-time RL with dense progress-based rewards）
- [Mechanism]: TT-VLA 在推理时（而非训练时）进行 policy adaptation：利用 step-by-step task-progress signals 构造 dense reward mechanism，在保留 SFT/RL-trained priors 的同时在线精炼 action policy。本质是 P5 的 test-time 应用变体——将 RL 从训练阶段移到推理阶段，使 agent 在部署中持续适应。与 EVOLVE-VLA（Paper 55）同属 test-time training 范式。

[Title]: AWPO: Enhancing Tool-Use of LLMs through Explicit Integration of Reasoning Rewards
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Tool-use interaction trajectories（含 CoT reasoning quality 信号）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 4B model 在多轮工具使用中超越 Grok-4 16.0%
- [Method]: ⟨RL: PPO⟩（AWPO: advantage-weighted with reasoning rewards）
- [Mechanism]: AWPO 将 reasoning rewards（基于 CoT 质量的奖励）显式集成到 advantage estimation 中：(1) variance-aware gating 基于 group-relative statistics 自适应调节 reasoning signals 的 advantage 贡献；(2) difficulty-aware weighting 按任务难度加权；(3) tailored clipping mechanism 稳定优化。本质是 P5 路径下对 reward composition 的 principled 方法：trajectory → outcome reward + reasoning reward → advantage-weighted policy optimization → policy。

[Title]: SWE-Dev: Building Software Engineering Agents with Training and Inference Scaling
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Agent trajectories（synthesized test cases + scaled-up SWE trajectories）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}（trajectory synthesis pipeline 生成）
- [Utilization]: 训练 SWE-Dev 7B/32B 在 SWE-bench-Verified 上达到 23.4%/36.6%（open-source SOTA）
- [Method]: ⟨SFT⟩
- [Mechanism]: 两个关键 pipeline：(1) robust test case synthesis 用于 patch evaluation；(2) scaled-up agent trajectory 构建训练数据。用合成数据 SFT 训练 SWE agent。本质是 P5 的数据+训练 pipeline 贡献：synthetic test cases + scaled trajectories → SFT → SWE policy。

[Title]: Android Coach: Improve Online Agentic Training Efficiency with Single State Multiple Actions
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Online Android interaction trajectories（Single State Multiple Actions 范式收集）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 训练 Android agent 在 AndroidLab 和 AndroidWorld 上执行（1.4x 训练效率提升）
- [Method]: ⟨hybrid⟩（critic learning + process reward model + group-wise advantage estimator）
- [Mechanism]: 关键洞察：现有 Single State Single Action 范式在每个 costly emulator state 上仅做一次 one-to-one state-action 更新，效率极低。Android Coach 转变为 Single State Multiple Actions：学习 critic 估计 action values，使单个 online state 上可采样和利用多个 action（无额外 emulator 开销）。Critic 由 process reward model 增强，group-wise advantage estimator 基于平均 critic 输出。本质是 P5 路径下 sample efficiency 的改进：online state → critic-estimated multi-action → group-wise advantage → RL → policy。

[Title]: WebCoT: Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback
- [Pathway]: Narrative → Narrative → Policy (§8.3)
- [Source Experience]: Raw web agent trajectories（含隐式推理过程）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}（reasoning algorithm reconstruction 生成 CoT-augmented trajectory）
- [Utilization]: 训练 web agent 在 WebVoyager, Mind2web-live, SimpleQA 上显著提升
- [Method]: ⟨SFT⟩
- [Mechanism]: 识别 web agent 必需的三种关键推理技能（reflection&lookahead, branching, rollback），将 agent inference-time reasoning algorithms 重构为 explicit CoT rationales 以生成 exemplify 这些能力的 trajectory data。两阶段转化 (§8.3)：Stage 1 (P1)：raw trajectory → CoT-reconstructed trajectory（将隐式推理过程显式化为逐步推理文本，Narrative → refined Narrative）；Stage 2 (P5)：distilling salient reasoning patterns into backbone LLM via SFT。核心创新在 reasoning skill 的显式化重构和蒸馏。

[Title]: VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Real-world robot rollout data + world-model-generated synthetic rollout data
- [Target Experience]: Updated VLA policy weights (π-Par) + Improved World Model weights
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}（real-world rollouts）, {teacher}（world model synthetic rollouts）
- [Utilization]: 在真实机器人上提升 SOTA VLA model 的多任务表现（39.2% 绝对成功率提升）
- [Method]: ⟨hybrid⟩（iterative improvement: real data → world model → synthetic data → VLA policy）
- [Mechanism]: 迭代协同改进算法：(1) 真实 robot rollout 数据用于改进 world model (action-conditioned video generation model) 的物理保真度——解决 demonstration dataset 缺乏 failure cases 和物理细节的问题；(2) 改进后的 world model 生成 supplemental synthetic rollout data；(3) synthetic data 用于提升 VLA policy。本质是 P5 路径下 data augmentation 的迭代范式：real rollout → world model improvement → synthetic rollout → RL/SFT → VLA policy。两个模型交替改进形成协同循环。

[Title]: LLaRP: Large Language Models as Generalizable Policies for Embodied Tasks
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Embodied interaction trajectories（Language Rearrangement benchmark, 150K training tasks）
- [Target Experience]: Adapted policy（pre-trained frozen LLM + 可能的 adapter 权重，abstract 未明确说明参数更新方式）
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 训练 LLM 作为 embodied policy 在 1,000 unseen tasks 上达到 42% 成功率（1.7x baseline）
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 将 pre-trained frozen LLM 适配为 embodied visual task 的 policy——输入 text instructions + visual egocentric observations，直接输出 environment actions。仅通过 RL 和环境交互学习"看"和"做"。本质是 P5 的早期探索性工作（2023），展示 LLM 通过 RL 可成为 generalizable embodied policy，对复杂 task paraphrasing 鲁棒且可泛化到需要 novel optimal behavior 的新任务。

[Title]: JOSH: Sparse Rewards Can Self-Train Dialogue Agents
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: Tool-calling dialogue trajectories（simulation environment 中的 self-generated outputs）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 LLM agent 在 ToolWOZ 和其他 benchmark 上提升 tool-based interactions
- [Method]: ⟨RL: PPO⟩（JOSH: self-alignment algorithm）
- [Mechanism]: JOSH 是一种无需 external human feedback 的 self-improvement paradigm (§8.1)：Stage 1 (P7)：LLM agent 在 sparse reward simulation environment (ToolWOZ) 中自主交互、产生多种行为输出；Stage 2 (P1/P5)：Juxtaposed Outcomes for Simulation Harvesting——将同一 context 下的不同行为结果并置对比，从 sparse reward 中提取 ideal behaviors，用 agent 自身输出训练自身（self-alignment）。关键洞察：即使只有 sparse reward，通过并置对比不同 simulation outcomes 仍可提取有效训练信号。完全消除对人类反馈的依赖。

[Title]: MATPO: Multi-Agent Tool-Integrated Policy Optimization
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Multi-agent tool-integrated planning trajectories（planner + worker rollout）
- [Target Experience]: Updated policy weights (π-Par)（单一 LLM instance 内 role-specific prompts 训练）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练单一 LLM 在 GAIA-text, WebWalkerQA, FRAMES 上超越 single-agent baseline 平均 18.38%
- [Method]: ⟨RL: PPO⟩（MATPO: principled credit assignment across planner and worker rollouts）
- [Mechanism]: 在单一 LLM instance 内通过 role-specific prompts 训练 planner 和 worker 两种角色（无需部署多个 LLM）：planner 负责高层规划，worker 负责工具调用执行。Principled credit assignment mechanism 跨 planner 和 worker rollout 分配信用。本质是 P5 路径下 multi-agent RL 在单模型内的实现：multi-role trajectory → role-specific credit assignment → RL → unified policy。

[Title]: SSR: Toward Training Superintelligent Software Agents through Self-Play SWE-RL
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: Self-play software engineering trajectories（agent 自主注入和修复 bug 的交互序列）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 SWE agent 在 SWE-bench Verified 和 SWE-Bench Pro 上自我改进（+10.4 和 +7.8 points）
- [Method]: ⟨RL: PPO⟩（self-play RL）
- [Mechanism]: Self-play SWE-RL 闭环 (§8.1)：(1) agent 在真实 codebase 中自主注入 bug（由 test patch 而非自然语言 issue 形式化指定）；(2) agent 尝试修复自己注入的 bug；(3) 修复结果（test pass/fail）作为 RL reward 更新 policy；(4) 更新后的 agent 注入更复杂的 bug → 修复 → 训练，复杂度递增。仅需 sandboxed repositories with source code and installed dependencies，无需 human-labeled issues 或 tests。关键创新：完全 self-play 范式——agent 既是 bug 的创造者也是修复者，自主从真实 codebase 中积累学习经验。

[Title]: SQL-ASTRA: Alleviating Sparse Feedback in Agentic SQL via Column-Set Matching and Trajectory Aggregation
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Multi-turn Text-to-SQL interaction trajectories（含中间查询执行结果）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 Text-to-SQL agent 在 BIRD 和 Spider 2.0 上超越 SOTA
- [Method]: ⟨RL: GRPO⟩（two-tiered reward: ATR + CSMR）
- [Mechanism]: 双层奖励机制：(1) Aggregated Trajectory Reward (ATR)——使用 asymmetric transition matrix 聚合 process-oriented scores，Lyapunov stability theory 证明其作为 energy dissipation operator 保证 cycle-free policy 和 monotonic convergence；(2) Column-Set Matching Reward (CSMR)——每轮执行查询将 binary (0/1) feedback 转化为基于 partial correctness 的 dense [0, 1] signals。本质是 P5 路径下 credit assignment 和 reward densification 的理论化改进。

[Title]: Fine-Tuning Large Vision-Language Models as Decision-Making Agents via Reinforcement Learning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Multi-step goal-directed interaction trajectories（VLM 生成 CoT reasoning → executable action → environment feedback）
- [Target Experience]: Updated VLM policy weights (π-Par)
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {self}
- [Utilization]: 训练 7B VLM agent 在多种决策任务上超越 GPT4-V 和 Gemini
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 框架：(1) task description 提示 VLM 生成 CoT reasoning；(2) open-ended text output 解析为 executable action 与环境交互获得 goal-directed task reward；(3) task reward 用于 RL 微调整个 VLM。发现 CoT reasoning 是性能提升的关键组件（移除后性能显著下降）。本质是 P5 在 VLM agent 领域的早期（2024）系统探索：VLM CoT trajectory → executable action → environment reward → RL → VLM policy。

[Title]: MTSQL-R1: Towards Long-Horizon Multi-Turn Text-to-SQL via Agentic Training
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Multi-turn conversational SQL interaction trajectories（propose → execute → verify → refine cycle）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 agent 在 COSQL 和 SPARC 上做 multi-turn Text-to-SQL
- [Method]: ⟨RL: PPO⟩（agentic training in MDP framework）
- [Mechanism]: 将 multi-turn Text-to-SQL 形式化为 MDP：agent 与 (i) database 交互获取 execution feedback，(ii) persistent dialogue memory 交互做 coherence verification。Iterative propose → execute → verify → refine cycle 直到所有检查通过。本质是 P5 在 conversational semantic parsing 的 multi-turn RL 实现：interaction trajectory → execution + coherence reward → RL → policy。核心创新在 environment-driven verification 和 memory-guided refinement 的闭环设计。

[Title]: AgentTuning: Enabling Generalized Agent Abilities for LLMs
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: High-quality interaction trajectories（AgentInstruct dataset: 6 agent tasks 的多样化交互轨迹）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}（AgentInstruct 从 GPT-4 等 teacher model 生成）
- [Utilization]: 训练 Llama 2 系列 (7B/13B/70B) 在 unseen agent tasks 上达到 GPT-3.5-turbo 水平
- [Method]: ⟨SFT⟩（hybrid instruction-tuning: AgentInstruct + general domain instructions）
- [Mechanism]: 构建 AgentInstruct（轻量级指令微调数据集，含 6 类 agent tasks 的高质量交互轨迹），采用 hybrid instruction-tuning strategy（AgentInstruct + 通用开源指令）训练 LLM，在不损害通用能力的前提下增强 agent 能力。本质是 P5 的最简形式——通用 agent 能力 SFT。早期工作（2023），核心贡献在数据集构建和 hybrid tuning 策略。

[Title]: DistRL: An Asynchronous Distributed Reinforcement Learning Framework for On-Device Control Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Online mobile device control interaction trajectories（decentralized data acquisition 收集）
- [Target Experience]: Updated MLLM policy weights (π-Par)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 训练 on-device control agent 在 Android tasks 上提升 20% 相对成功率
- [Method]: ⟨RL: PPO⟩（DistRL: centralized training + decentralized data acquisition）
- [Mechanism]: 采用 centralized training and decentralized data acquisition 架构提升 online RL fine-tuning 效率——3x 训练效率提升，2.4x 数据收集加速。Tailor-made RL algorithm 平衡 exploration 与 prioritized data utilization。本质是 P5 路径下的分布式系统工程实现，核心贡献在异步分布式 RL 基础设施。

[Title]: SPA: Internalizing World Models via Self-Play Finetuning for Agentic RL
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Self-play interaction trajectories（用于学习 internal world model + RL 训练）
- [Target Experience]: Updated policy weights (π-Par) with internalized world model
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 LLM agent 在 Sokoban (+34.2%), FrozenLake (+48.8%), Sudoku 上执行
- [Method]: ⟨hybrid⟩
- [Mechanism]: 关键假设：equipping LLM agents with internal world model 可更好地将推理与环境动态对齐。SPA 两阶段：(1) Self-Play SFT——agent 通过与环境交互学习 world model（分解为 state representation + transition modeling），此为将环境动态 internalize 为模型内部表示（Narrative → internal world representation → Policy, P5）；(2) 在 RL policy optimization 前用 world model 模拟 future states。核心创新在 self-play SFT 冷启动阶段，使 agent 在 RL 前获得环境的内部心智模型。

[Title]: CM2: Reinforcement Learning with Checklist Rewards for Multi-Turn Agentic Tool Use
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Multi-turn tool-use interaction trajectories（LLM-simulated tool environment 中生成）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}（RL rollouts in simulated environment）
- [Utilization]: 训练 8B model 在 tau-Bench (+8), BFCL-V4 (+10), ToolSandbox (+12) 上提升
- [Method]: ⟨RL: PPO⟩（checklist reward based RL）
- [Mechanism]: CM2 用 checklist rewards 替代 verifiable outcome rewards：(1) 将每轮 expected behavior 分解为细粒度二值标准（explicit evidence grounding + structured metadata）；(2) 采用 sparse reward assignment but dense evaluation criteria 策略平衡稳定性与信息量；(3) 在 scalable LLM-simulated tool environment 中训练避免真实工具环境的高昂工程成本。本质是 P5 路径下 reward 设计的创新：open-ended judging → classification-style checklist criteria → RL → policy。

[Title]: SWE-Playground: Training Versatile Coding Agents in Synthetic Environments
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Synthetically generated coding trajectories（SWE-Playground pipeline 从零生成 projects + tasks）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}（synthetic generation by strong LMs and agents）
- [Utilization]: 训练 versatile coding agents 在三个 distinct benchmarks 上执行多样化的编码任务
- [Method]: ⟨SFT⟩
- [Mechanism]: SWE-Playground pipeline 从零合成 projects 和 tasks（不依赖 GitHub repositories），支持更广泛的编码任务类型（reproducing issues by generating unit tests, implementing libraries from scratch 等）。产生的 trajectory 含 dense training signal，用更少的 trajectory 达到 comparable performance。本质是 P5 的数据合成贡献：synthetic environment → diverse coding trajectory → SFT → policy。

[Title]: SAND: Boosting LLM Agents with Self-Taught Action Deliberation
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: Action deliberation trajectories（agent 自身 base model 生成的 step-wise deliberation thoughts）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 LLM agent 在两个交互式 agent tasks 上平均提升 20%
- [Method]: ⟨hybrid⟩
- [Mechanism]: hybrid 由 ⟨LLM-extract⟩（self-consistency action sampling + execution-guided action critique）+ SFT 组成。Self-taught 闭环 (§8.1)：Stage 1 (P7)：用 base model 的 self-consistency action sampling 生成候选动作，execution-guided action critique 评估每步动作质量，合成 step-wise action deliberation thoughts——Narrative → refined Narrative with deliberation (P1)；Stage 2 (P5)：deliberation trajectories 用于 finetune LLM agent 自身（iterative manner）。核心创新：让 agent 在行动前显式 deliberation over candidate actions，避免 over-commit 到看似合理但次优的动作。

[Title]: COVERT: Controllable and Verifiable Tool-Use Data Synthesis for Agentic RL
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Synthesized tool-use trajectories（self-evolving synthesis with multi-level validation + oracle-preserving augmentations）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}（synthesis pipeline 生成）
- [Utilization]: 训练 Qwen2.5-Instruct-14B 在 BFCL v3 (56.5→59.9) 和 ACEBench (53.0→59.3) 上提升
- [Method]: ⟨RL: PPO⟩（RL with auto-computed reference-matching rewards）
- [Mechanism]: 两阶段合成 pipeline：(1) self-evolving synthesis with multi-level validation 生成可靠基础 tool-use trajectory；(2) oracle-preserving augmentations 系统性地增加环境复杂度（distractor tools, indirect/ambiguous queries, noisy tool outputs）但严格保留 oracle tool calls 和 final answers。设计使 automatic reward computation 通过 reference matching（标准情况）或 judge-assisted verification（特殊行为如 error detection）实现。本质是 P5 路径下合成训练环境与自动奖励的设计方法。

[Title]: CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Constraint-guided synthesized tool-use trajectories（12K high-quality trajectories）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}（constraint-guided synthesis 生成）
- [Utilization]: 训练 CoVe-4B 在 tau²-bench 上达到 43.0% (Airline) / 59.4% (Retail)，与 17x 更大模型竞争
- [Method]: ⟨SFT⟩, ⟨RL: PPO⟩
- [Mechanism]: 定义 explicit task constraints 发挥双重作用：(1) 引导 complex trajectory 的生成；(2) 作为 deterministic verifier 评估 trajectory 质量。这使高质量 SFT 训练数据构建和 RL 精确奖励信号推导成为可能。本质是 P5 路径下数据合成与验证的统一框架：constraint definition → guided trajectory synthesis + deterministic verification → SFT + RL → policy。

[Title]: VEM: Environment-Free Exploration for Training GUI Agent with Value Environment Model
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Offline GUI interaction data（用于预训练 VEM）+ online policy exploration（VEM-guided）
- [Target Experience]: Updated VLM policy weights (π-Par)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {human}（offline data 预训练 VEM）, {self}（VEM-guided policy exploration）
- [Utilization]: 训练 GUI agent 在 Android-in-the-Wild benchmarks 上达到 SOTA
- [Method]: ⟨hybrid⟩（VEM pretraining + VEM-guided RL）
- [Mechanism]: VEM (Value Environment Model) 从 offline data 预训练，直接预测 state-action values（distilling human-like priors about GUI interaction outcomes），无需 next-state prediction 或 environment feedback。两阶段：(1) 预训练 VEM 估计长期动作效用——此为 offline data → value estimator 的训练（类似 P4 但 VEM 是 value estimator 而非传统 RM/PRM）；(2) frozen VEM signals 引导 policy exploration 实现 layout-agnostic GUI automation。本质是 P5 的 environment-free RL 实现：offline data → VEM value estimation → guided policy exploration → policy。

[Title]: Environment Tuning: Don't Just Fine-tune the Agent, Tune the Environment
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Environment interaction trajectories（仅 400 problem instances from BFCL，无 expert trajectories）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 agent 在 BFCL benchmark 上实现 competitive in-distribution + superior OOD generalization
- [Method]: ⟨RL: PPO⟩（Environment Tuning: structured curriculum + corrective environment augmentation + progress rewards）
- [Mechanism]: Environment Tuning 使 agent 直接从 problem instances 学习（无需 pre-collected expert trajectories）：(1) structured curriculum 组织学习进程；(2) actionable environment augmentation 提供纠正性反馈；(3) fine-grained progress rewards 确保稳定高效探索。核心范式转变：从 SFT on static trajectories 到 dynamic environment-based exploration。本质是 P5 路径下的训练范式创新——通过环境端增强解决 SFT overfitting 和 RL cold-start 问题。

[Title]: Agent models: Internalizing Chain-of-Action Generation into Reasoning models
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Chain-of-Action (CoA) trajectories（含 step-level action triggering + trajectory-level CoA optimization）
- [Target Experience]: Updated policy weights (π-Par) with internalized CoA generation
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 agent model 在 open-domain QA tasks 上超越 ReAct-based workflows
- [Method]: ⟨SFT⟩, ⟨RL: PPO⟩
- [Mechanism]: AutoCoA 框架使 reasoning model 内部化 CoA 生成能力（无需外部 prompt 管理工具交互）：(1) step-level action triggering 自主决定何时及如何使用工具；(2) trajectory-level CoA optimization；(3) internal world model 降低真实环境交互成本。本质是 P5 在 agent 模型能力内部化中的应用——将工具使用的工作流从外部 prompt 工程移入模型参数。

[Title]: ToolOmni: Enabling Open-World Tool Use via Agentic Learning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Multi-turn tool-use interaction trajectories（cold-start SFT dataset + online RL rollouts）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}（cold-start dataset）, {self}（online RL）
- [Utilization]: 训练 LLM 在 open-world 场景中进行工具检索和执行（+10.8% end-to-end success rate）
- [Method]: ⟨SFT⟩, ⟨RL: GRPO⟩（Decoupled Multi-Objective GRPO）
- [Mechanism]: 两阶段：(1) cold-start multi-turn interaction dataset 通过 SFT 注入基础 agentic capabilities；(2) Decoupled Multi-Objective GRPO 在在线环境中同时优化工具检索精度和执行效能。本质是 P5 在 open-world tool use 的应用——SFT + multi-objective GRPO 串行组合。

[Title]: SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Long-horizon interaction trajectories（WebShop, ALFWorld, AppWorld）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 作为 plug-and-play 模块增强现有 group-based RL 算法
- [Method]: ⟨RL: GRPO⟩（SALT-enhanced）
- [Mechanism]: 关键洞察：group-based RL (如 GRPO) 中 uniform reward/penalty per trajectory 导致 beneficial actions 和 detrimental actions 在多步交互中纠缠。SALT 从同一 prompt 的多条 trajectory 构建 graph，量化每步质量并分配 finer-grained advantage——完全从 outcome reward 推导，无需额外 rollout 修改或 critic model。本质是 P5 路径下 credit assignment 的轻量级改进：trajectory graph → step quality quantification → fine-grained advantage → GRPO → policy。

[Title]: EMPG: Entropy-Modulated Policy Gradients for Long-Horizon LLM Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Long-horizon interaction trajectories（WebShop, ALFWorld, Deep Search）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 agent 在三个 challenging agent tasks 上显著提升
- [Method]: ⟨RL: PPO⟩（EMPG: entropy-modulated variant）
- [Mechanism]: 发现 LLM 学习动态中的根本问题：policy gradient magnitude 与 entropy 固有耦合——confident correct actions 更新幅度过小（低效），uncertain actions 更新幅度过大（不稳定）。EMPG 基于 step-wise uncertainty 和 final task outcome 重新校准学习信号：放大 confident correct actions 的更新、惩罚 confident errors、衰减 uncertain steps 的更新。Future clarity bonus term 鼓励 agent 寻找更可预测的解决路径。本质是 P5 路径下对 policy gradient 信号质量的改进。

[Title]: ToolCAD: Exploring Tool-Using LLMs in Text-to-CAD Generation with RL
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: CAD modeling interaction trajectories（interactive CAD modeling gym 中 rollout）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {human}（hybrid feedback and human supervision）
- [Utilization]: 训练 LLM agent 进行 text-to-CAD generation
- [Method]: ⟨RL: PPO⟩（online curriculum RL with hybrid feedback）
- [Mechanism]: 首次将 tool-using LLM 应用于 CAD 领域：interactive CAD modeling gym 中 rollout reasoning + tool-augmented interaction trajectory，通过 end-to-end post-training strategy（含 online curriculum RL）使 LLM 生成 refined CAD Modeling Chain of Thought (CAD-CoT) 并进化为熟练的 CAD tool-using agent。本质是 P5 在 CAD 新领域的应用。

[Title]: Understanding the performance gap between online and offline alignment algorithms
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Preference data（prompt + response pairs with human preferences）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: 研究 online vs offline alignment 算法的根本差异，指导 alignment 方法选择
- [Method]: ⟨RL: PPO⟩（online）, ⟨RL: DPO⟩（offline）— 对比研究
- [Mechanism]: 实证研究论文——系统比较 online (on-policy RL) 和 offline (DPO 等) alignment 算法的性能差距。核心发现：(1) online 方法在 generation quality 上显著优于 offline 方法，offline 方法在 pairwise classification 上更强——揭示了 discriminative 和 generative 能力的独特交互；(2) offline data coverage 和 data quality 本身不能充分解释性能差异；(3) 性能差距在 contrastive 和 non-contrastive loss functions 中均持续存在，且不能通过简单扩展 policy network 解决。虽非 agent-specific 研究，但其发现对理解 P5 路径中 online vs offline RL 的选择有直接启示。

[Title]: TSR: Trajectory-Search Rollouts for Multi-Turn RL of LLM Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Multi-turn interaction trajectories（tree-style search 生成的高质量 rollout）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 agent 在 Sokoban, FrozenLake, WebShop 上提升最高 15%（PPO/GRPO 均可搭配）
- [Method]: ⟨hybrid⟩
- [Mechanism]: hybrid 由 ⟨MCTS⟩（lightweight tree-style search: best-of-N, beam, shallow lookahead）+ ⟨RL: PPO⟩ 或 ⟨RL: GRPO⟩ 组成。TSR 将 test-time scaling 思想重新用于训练时 rollout 生成——在每个 turn 用 task-specific feedback 选择高评分动作构建高质量 trajectory。核心创新在将 search 从 inference time 移到 training rollout stage：tree search → high-quality trajectory → standard RL objective → policy。Optimizer-agnostic（可搭配 PPO/GRPO），与 rejection-sampling 方法互补。

[Title]: Instructing LLMs to Negotiate using Reinforcement Learning with Verifiable Rewards
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Bilateral price negotiation trajectories（buyer agent vs regulated LLM seller 的多轮博弈）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 30B buyer agent 在不完全信息博弈中超越 10x 更大的 frontier models，泛化到未见过的更强对手
- [Method]: ⟨RL: PPO⟩（RLVR: reward grounded in economic surplus + budget constraint adherence）
- [Mechanism]: 将谈判训练 formalize 为 RLVR 问题：reward 直接锚定在经济剩余最大化和预算约束严格遵守上，而非人类偏好标注。训练过程揭示四阶段策略演化（naive bargaining → aggressive starting prices → deadlock → sophisticated persuasive skills）。本质是 P5 在策略博弈领域的应用：negotiation interaction trajectory → verifiable economic reward → RL → policy。核心发现在 emergent strategic behavior 的 phase transition。

[Title]: Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Multi-turn interaction trajectories（WebShop, Sokoban）
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练 LLM agent 在 WebShop 和 Sokoban 上执行 multi-turn 任务
- [Method]: ⟨RL: PPO⟩（turn-PPO: turn-level MDP variant）
- [Mechanism]: 发现 GRPO 在 multi-turn 任务中存在局限，PPO 更鲁棒。Turn-PPO 在 turn-level MDP 形式化上操作（而非 token-level MDP），使 advantage estimation 与 agent 的实际决策边界对齐。本质是 P5 路径下对 MDP 粒度的重新定义：multi-turn trajectory → turn-level MDP → PPO → policy。核心创新在将 RL 的决策单元从 token 提升到 turn。

[Title]: DRO: Offline Regularised Reinforcement Learning for Large Language Models Alignment
- [Pathway]: Out of Scope
- [Mechanism]: 论文研究的是通用 LLM alignment（从单轮 prompt-response-feedback 三元组学习偏好），而非 LLM-based agent 的决策任务。经验形式为 single-trajectory human feedback（thumbs-up/down），Action 空间为单轮文本生成（同质动作空间，非异构 agent 动作空间）。属于 §3.2 排除标准：无 LLM-based system 的异构动作空间。

[Title]: ILQL: Offline RL for Natural Language Generation with Implicit Language Q Learning
- [Pathway]: Out of Scope
- [Mechanism]: 论文提出的 ILQL 是面向通用自然语言生成的 offline RL 方法，应用场景为 end-to-end dialogue 和 toxic comment labeling。Dialogue 应用虽涉及多轮交互，但动作空间为同质的文本生成（无工具调用、环境控制等异构动作）。Toxic comment labeling 为单步分类任务。属于 §3.2 排除标准：非异构动作空间，非 LLM-based agent 序贯决策。

[Title]: LaMo: Unleashing the Power of Pre-trained Language Models for Offline Reinforcement Learning
- [Pathway]: Out of Scope
- [Mechanism]: LaMo 使用 Decision Transformer 架构和预训练 LM 解决传统 RL 任务（motion control），属于用 LM 架构作为传统 RL 的 policy backbone，而非 LLM-based agent 在异构动作空间中的序贯决策。动作空间为传统 RL 的连续/离散控制动作，无 LLM agent 特有的推理轨迹、工具调用、规划分解等异构动作。属于 §3.2 排除标准：非 LLM-based agent system（尽管使用了 LM 架构）。

[Title]: A-LoL: Advantage-based Offline Reinforcement Learning for Language Models
- [Pathway]: Out of Scope
- [Mechanism]: A-LoL 针对通用 LM alignment（RLHF benchmark: Helpful and Harmless Assistant）和语言生成任务，将整个 LM output sequence 视为 "single action"。该设定下动作空间为单轮文本生成（同质），不涉及 LLM-based agent 的多步异构决策（工具调用、环境交互、规划分解等）。属于 §3.2 排除标准：非异构动作空间。

[Title]: Language Models are Few-Shot Butlers
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Expert demonstrations（ALFWorld 环境中的任务完成轨迹）+ agent 自身交互
- [Target Experience]: Updated policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}（expert demonstrations）, {self}（RL 交互阶段）
- [Utilization]: 训练 LM agent 在 ALFWorld 中仅用 1.2% expert demonstrations + RL 达到 51% 绝对成功率提升
- [Method]: ⟨SFT⟩, ⟨RL: PPO⟩
- [Mechanism]: 两阶段过程：(1) few-shot SFT 在极少 expert demonstrations (1.2%) 上微调 LM 获得基础能力；(2) RL 通过环境交互进一步改进。本质是 P5 的早期（2021）高效范式：少量 demonstration → SFT → agent 在线交互 → RL → policy。核心贡献在证明极少量 demonstration + RL 即可达到强性能。

[Title]: Learning to Navigate Wikipedia by Taking Random Walks
- [Pathway]: Out of Scope
- [Mechanism]: 任务为 Wikipedia 链接导航——动作空间仅包含"选择下一个超链接"这一种动作类型（同质动作空间），系统通过学习随机游走轨迹的 behavioral cloning 训练 link selection policy。不存在 LLM agent 特有的异构动作空间（推理、工具调用、规划分解等）。属于 §3.2 排除标准：非异构动作空间。

[Title]: WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Human demonstrations（1,600+ crowd-sourced） + agent online interaction trajectories
- [Target Experience]: Policy weights（via RL, imitation learning, or pre-trained models）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}（demonstrations）, {self}（RL 交互）
- [Utilization]: 训练和评估多种 agent（RL, imitation learning, pre-trained models）在 WebShop 上执行
- [Method]: ⟨SFT⟩（imitation learning）, ⟨RL: PPO⟩
- [Mechanism]: WebShop 是 foundational benchmark 论文——构建 1.18M 真实商品的模拟电商环境，收集 1,600+ 人类示范。训练 agent 通过 RL 和 imitation learning 将 interaction trajectory 经验转化为 policy（P5）。最佳模型 29% 成功率（超越 rule-based 9.6%，低于人类专家 59%）。发现 agents trained on WebShop 在 amazon.com 和 ebay.com 上展现 non-trivial sim-to-real transfer。核心贡献在环境与 benchmark 构建而非转化机制。


## New Tags Introduced

- ⟨RL: DAPO⟩ —— Dynamic Asynchronous Policy Optimization，DAPO 论文提出的 RL 算法，首次出现：「Training Long-Context, Multi-Turn Software Engineering Agents with Reinforcement Learning」
- ⟨RL: ReST⟩ —— Reinforced Self-Training，已在 Notions.md 预定义但此批次标注中首次实际使用，出现在 self-improvement 相关论文中

## Annotation Failures

（无 —— 所有 131 篇论文均成功完成标注或判定为 Out of Scope）

## Parser Errors

（无 —— parse_papers.py 成功解析全部 131 篇论文，errors 列表为空）

## Out of Scope Summary

- 「DRO: Offline Regularised RL for LLMs Alignment」(#125) —— 通用 LLM alignment，单轮文本生成，非异构动作空间
- 「ILQL: Offline RL for NLG」(#126) —— 通用 NLG offline RL，dialogue/classification 任务，非异构动作空间
- 「LaMo: Unleashing PLMs for Offline RL」(#127) —— Decision Transformer 用于传统 motion control RL，非 LLM-based agent
- 「A-LoL: Advantage-based Offline RL for LMs」(#128) —— 通用 LM alignment，单轮文本生成，非异构动作空间
- 「Learning to Navigate Wikipedia by Taking Random Walks」(#130) —— 同质动作空间（仅 link selection），非 LLM agent 异构动作
