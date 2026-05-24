# Composite.md — Experience-Transformation Annotations

[Title]: BAGEL: Bootstrapping Agents by Guiding Exploration with Language
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: 随机探索轨迹或合成指令的种子集（seed set of randomly explored trajectories or synthetic instructions）
- [Target Experience]: 经迭代往返优化后的自然语言可描述的高质量 demonstrations
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 优化后的 demonstrations 通过检索式 ICL 在 test time 适配 zero-shot LM agent
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 两个带噪 LM 组件之间的迭代往返（round-trip）：LM labeler 将轨迹转化为合成指令，zero-shot LM agent 将合成指令映射回精炼轨迹。多轮迭代使轨迹分布逐步收敛到"能被自然语言良好描述"的区域。最终产物是 refined demonstrations，通过 ICL 检索注入 agent 上下文窗口以改进决策。全程无参数更新——ICL 属于上下文窗口级行为改变，不构成 P5。归入 P1 纯 Narrative → Narrative 抽象。
> Note: 此前误标为 P1+P5 composite。ICL-based policy adaptation 不满足 P5 的 Parametric 更新条件，已修正为纯 P1。

[Title]: OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis
- [Pathway]: Narrative → Narrative → Policy (P1 + P5)
- [Source Experience]: Agent 在 GUI 环境中主动感知并执行逐步交互所产生的原始轨迹（raw trajectories）
- [Target Experience]: 通过逆向任务推导生成的高质量 task-trajectory pairs → 经 SFT 训练的 GUI agent policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 经验证的高质量轨迹用作 SFT 训练数据训练 GUI agent 模型权重
- [Method]: ⟨LLM-extract⟩, ⟨SFT⟩
- [Mechanism]: 阶段一（P1）：与常规"先定义任务再收集轨迹"不同，OS-Genesis 逆转该流程——Agent 先感知环境、执行逐步交互（step-wise interactions），再从交互中逆向推导（retrospectively derive）高质量任务描述。一个 trajectory reward model（V-Par，作为质量过滤器使用）筛选优质轨迹。阶段二（P5）：经验证的 trajectory-task pairs 作为 SFT 训练数据，将交互经验固化到 GUI agent 的权重中。V-Par 在此是辅助性过滤组件，非主要转化目标。复合模式 §8.3 Refine-then-Internalize。

[Title]: AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling
- [Pathway]: Narrative → Narrative → Policy (P1 + P5)
- [Source Experience]: 被丢弃的失败轨迹（failed trajectories，来自 WebArena/ToolBench）
- [Target Experience]: 经 hindsight relabeling 的高质量 SFT/DPO/ShareGPT 训练数据 → 微调后的 agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Relabeled 数据用于 SFT 和 DPO 训练 LLM agent；迭代部署下增益叠加
- [Method]: ⟨LLM-extract⟩, ⟨SFT⟩, ⟨RL: DPO⟩
- [Mechanism]: 阶段一（P1）：四阶段 pipeline——失败分类（failure classification）→ 结果提取（outcome extraction）→ LLM 引导的 prompt relabeling（带置信度门控 confidence gating）→ 数据打包。核心洞察来自 Hindsight Experience Replay 在自然语言 agent 轨迹上的适配：一条未能完成目标 A 的轨迹，往往是某个可达成替代目标 B 的正确示范。阶段二（P5）：Relabeled 数据用于 SFT 和 DPO 训练 agent policy 权重。支持迭代部署（iterative redeployment），每轮增益叠加。复合模式 §8.3。

[Title]: ECHO: Sample-Efficient Online Learning in LM Agents via Hindsight Trajectory Rewriting
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: 失败交互轨迹 / 不成功的尝试（failed interaction trajectories）
- [Target Experience]: 为替代可达成目标优化的反事实轨迹（optimized counterfactual trajectories for alternative achievable goals）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 压缩轨迹表征存入记忆，用于在后续新环境中指导决策
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Hindsight rule 利用 LM 自身从失败轨迹中识别相关子目标（relevant subgoals），生成针对"本可达成"的替代目标的反事实优化轨迹。Update rule 维护记忆中的压缩轨迹表征。本质是纯 P1：将失败轨迹通过 hindsight rewriting 转化为合成正例轨迹（synthetic positive examples），无参数更新。与 AgentHER 的区别在于 ECHO 不包含后续的 policy 训练步骤。

[Title]: Autonomous Evaluation and Refinement of Digital Agents
- [Pathway]: Narrative → Evaluator → Policy (P4 + P6)
- [Source Experience]: Agent 在 web navigation 和 device control 中的交互轨迹
- [Target Experience]: 训练得到的 domain-general 自动评估器 → 经 fine-tuning 改进的 agent policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 评估器既用于 fine-tuning 提供训练信号，也用于 inference-time guidance
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段一（P4）：多个评估模型在 agent 轨迹上训练为自动评估器，达到与 oracle 指标 74.4-92.9% 的一致率。这些评估器能判断轨迹质量。阶段二（P6）：评估器的判断信号用于 fine-tuning 改进 agent policy（以 evaluator 输出作为奖励/监督）。此外评估器还用于 inference-time guidance。复合模式 §8.2 Evaluate-then-Optimize。

[Title]: UI-Genie: A Self-Improving Approach for Iteratively Boosting MLLM-based Mobile GUI Agents
- [Pathway]: Narrative → Evaluator → Policy (P4 + P6)
- [Source Experience]: GUI agent 在动态移动环境中的交互轨迹（rollouts）
- [Target Experience]: UI-Genie-RM（image-text interleaved 奖励模型）→ 经三代 self-improvement 迭代提升的 GUI agent policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: RM 用于 reward-guided exploration 和 outcome verification；policy 通过 self-improvement pipeline 逐步扩展可解的复杂 GUI 任务范围
- [Method]: ⟨SFT⟩, ⟨RL: GRPO⟩
- [Mechanism]: 阶段一（P4）：UI-Genie-RM 采用 image-text interleaved 架构，通过精心设计的数据生成策略（rule-based verification、controlled trajectory corruption、hard negative mining）统一 action-level 和 task-level 奖励。训练数据 UI-Genie-RM-517k 为首个 GUI agent 专用 RM 数据集。阶段二（P6）：Self-improvement pipeline 通过 reward-guided exploration 和 outcome verification 交替提升 agent 和 RM——agent 的改进产生更好的轨迹数据，RM 的改进提供更准确的奖励信号。三代数据-模型自我提升循环。复合模式 §8.2 + self-reinforce loop。

[Title]: GAIA: A Data Flywheel System for Training GUI Test-Time Scaling Critic Models
- [Pathway]: Narrative → Evaluator (P4) [含 self-reinforce 飞轮]
- [Source Experience]: Base GUI agent 产生的正负动作示例
- [Target Experience]: 经多轮飞轮迭代的 Intuitive Critic Model（ICM），判别能力逐轮增强
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Critic 在 test time 评估 agent 每个待执行动作的即时正确性（immediate correctness），筛选高成功概率的操作
- [Method]: ⟨SFT⟩
- [Mechanism]: 飞轮机制：Base agent 生成正负动作示例 → 训练初始 ICM（P4：轨迹 → critic 权重）。该 critic 随后指导 agent 动作选择以收集更精炼的正负样本 → 训练第二轮判别能力更强的 critic → 循环往复。飞轮的核心转化是 P4（每次迭代将 agent 轨迹固化为更强的 critic），critic 本身不直接训练 policy（该论文未涉及 policy 更新步骤）。critic 仅用于 test-time action selection。与 §8.2 的区别在于缺少 Evaluator → Policy 的 P6 步骤——GAIA 训练的是 critic 而非用 critic 训 policy。

[Title]: MagicGUI-RMS: A Multi-Agent Reward Model System for Self-Evolving GUI Agents via Automated Feedback Reflux
- [Pathway]: Narrative → Evaluator → Policy (P4 + P6)
- [Source Experience]: 跨异构 GUI 任务的 agent 交互轨迹
- [Target Experience]: Domain-Specific RM（DS-RM）+ General-Purpose RM（GP-RM）→ 通过自动反馈回流持续增强的 agent 行为
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: RM 系统在执行中识别错误动作、提出修正替代方案；automated data-reflux mechanism 将评估信号反馈至 agent 训练
- [Method]: ⟨SFT⟩, ⟨RL: GRPO⟩
- [Mechanism]: 阶段一（P4）：结构化数据构建 pipeline 自动生成均衡且多样化的 RM 训练数据。DS-RM 处理细粒度动作评估，GP-RM 确保跨任务泛化。阶段二（P6）：执行中 RM 系统提供纠错反馈（corrective feedback）；automated data-reflux mechanism 将评估信号持续回流到 agent 训练中。自进化闭环：更强的 agent 产生更高质量轨迹 → 更好的 RM 训练数据 → 更强的 RM → 更精准的 agent 训练信号。复合模式 §8.2。

[Title]: Watch Every Step! LLM Agent Learning via Iterative Step-level Process Refinement (IPR)
- [Pathway]: Narrative → Policy (P5) [含迭代精炼]
- [Source Experience]: 专家轨迹 + agent 探索轨迹，使用 Monte Carlo 方法估计 step-level rewards
- [Target Experience]: 通过对比动作对（contrastive action pairs）训练得到的 agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: 对比动作对用作 SFT 训练数据更新 policy 权重
- [Method]: ⟨SFT⟩, ⟨MCTS⟩
- [Mechanism]: Monte Carlo 方法沿专家轨迹估计逐步奖励（step-level rewards）。Agent 在每个步骤探索并生成新动作，与专家轨迹对应步骤通过 step-level rewards 比对以识别偏差，形成对比动作对（contrastive action pairs）。这些对比动作对用作 SFT 训练数据更新 policy。迭代精炼：每轮迭代产生更好的步骤级监督信号，逐步提升训练数据质量。核心为 P5（轨迹 → policy via SFT）。MC 步骤级奖励估计是诊断工具（diagnostic tool），并非单独训练的 V-Par，因此不归入 §8.2。

[Title]: Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training
- [Pathway]: Policy → Narrative → Policy (§8.1 Self-Reinforce，兼有 §8.3 重叠)
- [Source Experience]: Policy 自身的 rollout 轨迹（成功和错误轨迹）
- [Target Experience]: 具备反思与纠错能力的 policy（模型学会在推理时识别错误并及时修正）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: MCTS 构建的修复轨迹用作 SFT 训练数据更新 policy
- [Method]: ⟨MCTS⟩, ⟨SFT⟩
- [Mechanism]: 阶段一（P7→P1）：当前 policy 生成 rollout 轨迹（含成功和失败）。MCTS 从错误轨迹中构建能恢复正确路径的训练数据——model-guided critique construction 定位轨迹中首个错误步骤，将其拼接到 MCTS 树中共享同一父节点的相邻正确路径上，从而生成"从错误中恢复"的完整正确轨迹。阶段二（P5）：修复后的正确轨迹作为 SFT 数据更新 policy。闭环：更新后的 policy → 更高质量的 rollout → 更精准的错误定位与修复 → 更强的 policy。属于 §8.1 Self-Reinforce 闭环；中间 MCTS 构建修复轨迹的步骤涉及 Narrative refinement，因此兼有 §8.3（Refine-then-Internalize）特征。

[Title]: Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents (ETO)
- [Pathway]: Policy → Narrative → Policy (§8.1 Self-Reinforce)
- [Source Experience]: Agent 自身的探索轨迹（含失败轨迹）
- [Target Experience]: 通过 DPO 对比学习更新的 agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 对比轨迹对（失败 vs. 成功）用于 DPO 更新 policy 权重
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: 探索阶段：agent 与环境交互，收集失败轨迹并构建对比轨迹对（contrastive trajectory pairs）。训练阶段：轨迹偏好对通过 DPO 更新 policy 权重。探索与训练迭代交替，推动持续改进。纯 §8.1 Self-Reinforce：policy rollout → 轨迹数据 → policy 更新 via preference learning。与 Agent-R 的区别在于 ETO 没有中间的 Narrative refinement 步骤（无 MCTS 修复、无 reflection 中间层），失败轨迹直接作为负样本与成功轨迹配对使用。

[Title]: OpenWebVoyager: Building Multimodal Web Agents via Iterative Real-World Exploration, Feedback and Optimization
- [Pathway]: Policy → Narrative → Policy (§8.1 Self-Reinforce)
- [Source Experience]: Agent 自身在开放网络中的多模态探索轨迹 + 通用 judging model 的反馈
- [Target Experience]: 通过迭代模仿学习逐步改进的多模态 web agent policy
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {self}
- [Utilization]: 被通用 judging model 判定为高质量的执行轨迹用于进一步模仿学习训练 policy
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段一：使用模仿学习训练 base model 获得基础能力。阶段二：agent 在开放网络中自主探索，收集轨迹并由一个通用 judging model（frozen，未训练）评估质量。阶段三（P5）：高质量轨迹用于通过模仿学习更新 policy。探索-反馈-优化循环迭代多轮。属于 §8.1 Self-Reinforce。judge model 在此是冻结的过滤器（frozen filter），未经历训练，因此区别于 §8.2（后者要求 Evaluator 本身也被训练）。

[Title]: OS-Copilot: Towards Generalist Computer Agents with Self-Improvement
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: 跨 OS 元素的交互轨迹（web、code terminals、files、multimedia、第三方应用）
- [Target Experience]: 可复用的累积技能库（accumulated reusable skills，以可执行程序化知识形式存在）
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 累积的技能以 ICL 方式注入 agent，使其泛化到 unseen applications
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Agent 跨 OS 多元素交互，从历次任务中累积可复用技能。这些技能以可执行的程序化知识形式存在（属于 Schematic：具有执行语义的过程性模板），而非纯自然语言提示。技能库随交互扩展使 agent 能泛化到未见应用。Abstract 未提及 SFT 或 RL 参数更新——FRIDAY 通过累积技能的 ICL 注入实现 self-improvement，而非权重更新。因此归入纯 P2（Narrative → Schematic），不包含 P5。
> Note: 此前误标为 P2 + P5 composite。Abstract 未描述参数更新，self-improvement 通过可复用技能库的 ICL 注入实现，修正为纯 P2。

[Title]: STeCa: Step-level Trajectory Calibration for LLM Agent Learning
- [Pathway]: Narrative → Narrative → Policy (P1 + P5)
- [Source Experience]: Agent 探索轨迹中通过 step-level reward 比对识别出的含次优动作的轨迹
- [Target Experience]: LLM 驱动的校准轨迹（calibrated trajectories）+ 成功轨迹 → 经强化训练更新的 policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 校准轨迹与成功轨迹合并用于 reinforced training 更新 agent policy
- [Method]: ⟨LLM-extract⟩, ⟨SFT⟩
- [Mechanism]: 阶段一（P1）：探索中通过 step-level reward 比对识别次优动作（suboptimal actions）。LLM 驱动的 reflection 在次优步骤处改进决策，构建校准轨迹（calibrated trajectories）——本质是对原始轨迹的步骤级语义修正。阶段二（P5）：校准轨迹与成功轨迹合并，作为强化训练数据更新 agent policy 权重。核心贡献在于"及时校准"（timely calibration）而非仅依赖终局奖励。复合模式 §8.3 Refine-then-Internalize。

[Title]: UI-Evol: Automatic Knowledge Evolving for Computer Use Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Agent 与环境实际交互产生的客观动作序列（action sequences from actual agent-environment interactions）
- [Target Experience]: 经 Retrace + Critique 两阶段精炼的外部知识（refined external knowledge）
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 精炼后的知识以 plug-and-play 模块形式注入 agent，提升 OSWorld 任务执行表现与行为稳定性
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 两阶段知识进化：Retrace Stage 从实际 agent-环境交互中提取忠实客观的动作序列；Critique Stage 将这些序列与外部参考知识对比，精炼现有知识。产出是 refined knowledge（Narrative），以 plug-and-play 模块形式注入 agent 执行流程。全程无参数更新——知识注入属于上下文窗口级行为改变。归入纯 P1（raw interaction traces → refined knowledge）。
> Note: 此前误标为 P1+P5。P5 需参数更新，此处仅通过知识注入实现 ICL 级行为改变，修正为纯 P1。

[Title]: GUI-Reflection: Empowering Multimodal GUI Models with Self-Reflection Behavior
- [Pathway]: Narrative → Narrative → Policy (P1 + P5)
- [Source Experience]: 离线成功 GUI 轨迹 + 在线交互 rollout
- [Target Experience]: 自动构建的 reflection 和 error correction 数据 → 具备 self-reflection 行为能力的 GUI model
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 自动生成的 reflection 数据用于三阶段训练（GUI-specific pre-training → offline SFT → online reflection tuning）
- [Method]: ⟨LLM-extract⟩, ⟨SFT⟩
- [Mechanism]: 阶段一（P1）：可扩展数据管线从已有成功轨迹中自动构建 reflection 和 error correction 数据——通过引入合成错误并生成对应的修正理由（correction rationales），无需人工标注。阶段二（P5）：三阶段训练将 reflection 能力固化到模型权重中——GUI-specific pre-training（基础能力）→ offline SFT with reflection data（学会反思）→ iterative online reflection tuning（在线环境中持续增强反思与纠错）。复合模式 §8.3，带 iterative online loop。

[Title]: Scalable Data Synthesis for Computer Use Agents with Step-Level Filtering
- [Pathway]: Narrative → Narrative → Policy + Narrative → Evaluator (multi-target, §8.8)
- [Source Experience]: 强 teacher model（OpenAI computer-use-preview）的带噪 CUA rollouts
- [Target Experience]: WebSTAR 数据集（13.3K 过滤轨迹）→ 经 SFT 训练的 CUA policy + StepRM（7B 多模态 PRM）
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}
- [Utilization]: WebSTAR 用于 SFT 训练 CUA policy；WebSCORE 用于训练 StepRM process reward model
- [Method]: ⟨LLM-extract⟩, ⟨SFT⟩
- [Mechanism]: 核心机制是步骤级过滤（step-level filtering）：独立评估每个动作，仅保留正确步骤，辅以推理增强（reasoning augmentation）。同一数据合成管线产生两类目标载体：(1) P5——WebSTAR（13.3K 轨迹，267K 分级推理增强步骤）用于 SFT 训练 CUA policy 权重；(2) P4——WebSCORE（步骤级评分数据集）用于训练 StepRM，一个从 o4-mini 蒸馏得到的 7B 多模态 process reward model。Multi-target §8.8 模式：单一数据合成管线同时产出 Policy（via SFT）和 Evaluator（PRM）两类 Carrier 目标。

[Title]: Self-Improving Vision-Language-Action Models with Data Generation via Residual RL (PLD)
- [Pathway]: Policy → Narrative → Policy (§8.1 Self-Reinforce)
- [Source Experience]: VLA generalist 自身的 rollout 轨迹 + residual actor 在失败区域探索产生的恢复轨迹
- [Target Experience]: 经 curated recovery trajectories SFT 蒸馏后的增强版 generalist VLA
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 经筛选的恢复轨迹通过标准 SFT 蒸馏回 generalist VLA
- [Method]: ⟨RL: PPO⟩, ⟨SFT⟩
- [Mechanism]: 三阶段框架（Probe, Learn, Distill）：阶段一（P7）：训练轻量 residual actors 通过 RL 探测 VLA generalist 的失败区域，产生恢复行为轨迹。采用 hybrid rollout scheme 使收集的轨迹与 generalist 的部署分布对齐。阶段二（P5）：将 curated trajectories 通过标准 SFT 蒸馏回 generalist 权重。residual actor 仅为探测工具，而非最终 policy 目标——主转化路径为 generalist policy → rollouts → 增强的 generalist policy。§8.1 Self-Reinforce 带 residual RL 探索组件的变体。

[Title]: Mobile-Agent-v3 / GUI-Owl: Fundamental Agents for GUI Automation
- [Pathway]: Policy → Narrative → Policy (§8.1 Self-Reinforce)
- [Source Experience]: Self-Evolving GUI Trajectory Production 框架自动生成并验证的交互轨迹数据
- [Target Experience]: GUI-Owl 基础 GUI agent 模型 + Mobile-Agent-v3 框架
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 自动生成的交互数据用于 SFT 训练 GUI-Owl；TRPO 用于 online RL alignment
- [Method]: ⟨SFT⟩, ⟨RL: GRPO⟩
- [Mechanism]: 核心贡献是 Self-Evolving GUI Trajectory Production：自动查询生成 → 正确性验证 → 利用 GUI-Owl 自身迭代精炼轨迹，形成自改进闭环。阶段一（P7）：GUI-Owl 生成轨迹数据。阶段二（P5）：生成的数据用于 SFT 训练 GUI-Owl 权重。此外提出 TRPO（Trajectory-aware Relative Policy Optimization）进行 online RL 对齐。主路径为 §8.1 Self-Reinforce：policy rollouts → 过滤/验证后的轨迹 → policy SFT。云基础设施（跨 Android、Ubuntu、macOS、Windows）使规模化 self-evolving 成为可能。

[Title]: ANCHOR: Branch-Point Data Generation for GUI Agents
- [Pathway]: Narrative → Narrative → Policy (P1 + P5)
- [Source Experience]: 少量经验证的种子示范轨迹（verified seed demonstrations）
- [Target Experience]: 经分支点扩展（branch-point augmented）的大规模轨迹语料 → 经 SFT 训练的 GUI agent 模型
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {human}
- [Utilization]: 扩展轨迹语料用于 SFT 训练 GUI agent 模型，跨应用和操作系统泛化
- [Method]: ⟨LLM-extract⟩, ⟨SFT⟩
- [Mechanism]: 阶段一（P1）：从每条种子示范中识别分支点（branch points，对应有意义的状态变化），基于当前 GUI 上下文提出 state-grounded 新任务变体。执行 agent 按提议指令生成新轨迹，verifier 通过状态感知检查（state-aware checks）和轨迹级一致性（trajectory-level consistency）确保任务完成。Task-conditioned step-level filtering 移除未落地动作（ungrounded actions）并对分支后片段去噪。阶段二（P5）：扩展语料用于 SFT 训练 GUI agent 模型。复合模式 §8.3：种子示范 → 分支扩展/精炼轨迹 → policy 权重。

[Title]: LLMs as Scalable, General-Purpose Simulators For Evolving Digital Agent Training (UI-Simulator)
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: 数字世界模拟器生成的带结构 UI 状态和转换（structured UI states and transitions）
- [Target Experience]: 合成训练轨迹 → 经 SFT 训练的数字 agent policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}
- [Utilization]: 合成轨迹用作 SFT 训练数据训练数字 agent；UI-Simulator-Grow 通过优先高影响力任务实现更高效扩展
- [Method]: ⟨SFT⟩
- [Mechanism]: 数字世界模拟器生成结构化的 UI 状态和转换，guided rollout 过程确保连贯探索，trajectory wrapper 产出高质量多样化轨迹。这些合成轨迹作为 SFT 数据训练数字 agent。UI-Simulator-Grow 进一步通过优先高影响力任务和合成信息量更大的轨迹变体实现 targeted scaling。纯 P5（合成轨迹 → policy via SFT）。模拟器是环境生成器而非训练的 parametric 组件，不构成 co-evolving world model 模式（§8.9）。

[Title]: AutoTraj: Guided by Trajectories — Repairing and Rewarding Tool-Use Trajectories
- [Pathway]: Narrative → Narrative → Policy + Narrative → Evaluator (multi-target, §8.8)
- [Source Experience]: LLM 为每个查询生成的多条候选工具使用轨迹
- [Target Experience]: 修复后的高质量轨迹 → SFT 数据集 + trajectory-level reward model + RL 训练后的 policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: SFT 数据集用于初始 policy 训练；trajectory-level RM 在 RL 阶段结合 outcome 和 format rewards 引导 PPO 优化
- [Method]: ⟨LLM-extract⟩, ⟨SFT⟩, ⟨RL: PPO⟩
- [Mechanism]: 阶段一（P1）：对每个查询生成多条候选工具使用轨迹，沿多个维度评估。高质量轨迹直接保留；低质量轨迹通过 LLM-as-Repairer 修复。修复后的高质量轨迹构成 SFT 数据集（用于 P5）；每条修复轨迹与其原始低质量版本配对构成偏好数据集。阶段二（P4）：在偏好数据集上训练 trajectory-level reward model。阶段三（P6）：RL 阶段中，trajectory-level RM 与 outcome rewards 和 format rewards 结合，通过 PPO 引导 policy 优化。Multi-target §8.8——单一管线同时产出 Policy（via SFT + RL）和 Evaluator（trajectory-level RM）两类目标。同时符合 §8.2 Evaluate-then-Optimize（P4+P6 段）。

[Title]: Step-GUI Technical Report
- [Pathway]: Policy → Narrative → Policy (§8.1 Self-Reinforce)
- [Source Experience]: 模型自身生成的 GUI 交互轨迹
- [Target Experience]: 经 Calibrated Step Reward System 校准的训练信号 → Step-GUI 系列模型（4B/8B）
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 校准后的训练信号用于训练 Step-GUI 模型达到 SOTA GUI 性能（80.2% AndroidWorld, 48.5% OSWorld）
- [Method]: ⟨SFT⟩
- [Mechanism]: Self-evolving training pipeline：Calibrated Step Reward System 将模型自身生成的轨迹通过轨迹级校准转化为可靠训练信号，达到 >90% 标注准确率，成本降低 10-100x。校准后的数据训练 Step-GUI 模型权重（P5）。核心转化路径为 policy rollouts → calibrated training signals → policy SFT，属于 §8.1 Self-Reinforce 模式。论文还包含 GUI-MCP（Model Context Protocol，基础设施贡献）和 AndroidDaily benchmark（评估贡献），非转化机制组成部分。

[Title]: LEAFE: Internalizing Agency from Reflective Experience
- [Pathway]: Policy → Narrative → Policy (§8.1 Self-Reinforce，兼 §8.3 重叠)
- [Source Experience]: Agent 自身探索轨迹 + 丰富的环境反馈（rich environment feedback）
- [Target Experience]: 经验引导的修正轨迹（experience-guided corrections）→ 经 SFT 训练具备增强恢复能力（recovery agency）的 policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 修正轨迹通过 SFT 提升 policy 的 Pass@1 和 Pass@k
- [Method]: ⟨LLM-extract⟩, ⟨SFT⟩
- [Mechanism]: 阶段一（P7 + P1）：探索中 agent 将环境反馈总结为可操作经验（actionable experience），回溯到更早决策点（backtracks to earlier decision points），以修正后的动作探索替代分支。这一过程产出经验引导的修正轨迹——既是从 policy 外化的 Narrative（P7），也是经反思精炼的 Narrative（P1）。阶段二（P5）：这些修正通过 SFT 蒸馏到模型权重中，使 policy 在未来交互中更有效地恢复。闭环：更强的 policy → 更丰富的探索 → 更高质量的反思经验 → 更强的 policy。属于 §8.1 Self-Reinforce；显式的 backtracking + reflection 中间步骤使兼有 §8.3 特征。与 GRPO 等 outcome-driven 方法的关键区别：LEAFE 利用丰富的环境反馈而非仅最终成功信号，从而避免 distribution sharpening。

[Title]: RetroAgent: From Solving to Evolving via Retrospective Dual Intrinsic Feedback
- [Pathway]: Policy → Narrative → Policy (§8.1 Self-Reinforce)
- [Source Experience]: Agent 在线交互轨迹 + 外部任务奖励（extrinsic task rewards）
- [Target Experience]: 双重 intrinsic feedback（数值 + 语言）→ 经 online RL 更新的 policy + 文本记忆库中的可复用经验
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Intrinsic numerical feedback 用于 reward shaping；intrinsic language feedback 存入记忆缓冲区，通过 SimUtil-UCB 检索为后续决策提供上下文指导
- [Method]: ⟨RL: GRPO⟩, ⟨LLM-extract⟩
- [Mechanism]: 阶段一（P7 + P1）：Hindsight self-reflection 从 policy rollout 中生成两种互补信号——(1) intrinsic numerical feedback：通过追踪相对于先前尝试的实时增量子任务进展来奖励有前景的探索（P7：policy 行为 → 数值奖励信号）；(2) intrinsic language feedback：将可复用经验教训蒸馏到文本记忆缓冲区（P1：原始轨迹 → 精炼文本经验）。阶段二（P5）：外部任务奖励与双重 intrinsic feedback 共同引导 online RL（GRPO-based）更新 policy 权重。SimUtil-UCB 检索策略在相关性、历史效用和探索三者间取得平衡。核心复合模式为 §8.1 Self-Reinforce，创新点在于双重 intrinsic feedback 机制的设计。

[Title]: TRACE: Capability-Targeted Agentic Training
- [Pathway]: Narrative → Schematic → Policy (P2 + P5)
- [Source Experience]: 目标环境中 agent 的成功与失败轨迹
- [Target Experience]: 针对能力缺陷自动合成的训练环境规范（Schematic）+ 经 RL 训练的 LoRA adapters（Policy）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练后的 LoRA adapters 在推理时根据任务需求路由选择
- [Method]: ⟨LLM-extract⟩, ⟨RL: GRPO⟩
- [Mechanism]: 阶段一（P2）：TRACE 对比成功与失败轨迹，自动识别 agent 在目标环境中缺乏的能力（lacking capabilities），然后为每种能力缺陷合成一个针对性的训练环境——环境规范本身是带结构的人工产物（Schematic：包含奖励函数定义、任务分布约束等）。阶段二（P5）：在每个合成环境上通过 RL 训练 LoRA adapter，推理时按任务路由到相应 adapter。复合模式 §8.5 Formalize-then-Optimize：轨迹 → 结构化能力针对性训练环境 → LoRA 权重。TRACE 对比 GRPO 和 GEPA 具有更高的 rollout 效率。

[Title]: R3L: Reflect-then-Retry Reinforcement Learning with Language-Guided Exploration
- [Pathway]: Policy → Narrative → Policy (§8.1 Self-Reinforce)
- [Source Experience]: Policy 自身的 rollout 轨迹（含失败尝试）
- [Target Experience]: 通过 reflect-then-retry 合成的成功轨迹 → 经 pivotal credit assignment 和 positive amplification 优化的 policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 合成的高质量轨迹用于 RL 训练；Pivotal Credit Assignment 仅更新分叉后缀的梯度，Positive Amplification 提升成功轨迹权重
- [Method]: ⟨LLM-extract⟩, ⟨RL: GRPO⟩
- [Mechanism]: 阶段一（P7 + P1）：R3L 不从零随机采样，而是通过语言反馈（language feedback）诊断错误，利用 reflect-then-retry 将失败尝试转化为成功轨迹，且从识别到的失败点重启（降低 rollout 成本）。阶段二（P5）：Pivotal Credit Assignment 仅更新存在对比信号的分叉后缀（diverging suffix），排除共享前缀的梯度更新——解决轨迹级奖励对有效前缀的误惩罚。Positive Amplification 提升成功轨迹的优化权重，确保正向信号在失败占多数的困难任务中不被淹没。§8.1 模式，创新点在于信用分配（credit assignment）的精细化。

[Title]: Hi-WM: Human-in-the-World-Model for Scalable Robot Post-Training
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Policy 在 learned world model 内部的闭环 rollout + 人类在失败状态下的纠正动作
- [Target Experience]: 纠正轨迹 → post-trained robot policy
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}, {human}
- [Utilization]: 纠正轨迹加入训练集用于 policy post-training
- [Method]: ⟨SFT⟩
- [Mechanism]: Policy 在 learned world model 中闭环执行。当 rollout 出现错误或失败倾向时，人类直接在 world model 中干预提供短纠正动作。World model 缓存中间状态并支持回滚和分支（rollback and branching），使单一失败状态可生成多条纠正延续路径（dense supervision around poorly handled behaviors）。纠正轨迹加入训练集进行 post-training（P5：纠正轨迹 → policy via SFT）。World model 在此充当可复用的纠正基底（corrective substrate），而非训练中的 Evaluator——人类提供纠正信号，world model 提供安全的"试错空间"。不构成 co-evolving world model 模式（world model 预训练且不参与 co-evolution）。

[Title]: ReAct Meets ActRe: When Language Agents Enjoy Training Data Autonomy (A3T)
- [Pathway]: Policy → Narrative → Policy (§8.1 Self-Reinforce)
- [Source Experience]: Agent 自身轨迹（含失败任务）+ 通过 ActRe prompting 随机采样的外部动作
- [Target Experience]: 合成成功轨迹 → 通过 policy gradient with binarized rewards 更新的 policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Contrastive self-training：合成成功轨迹补充失败轨迹用于 policy gradient 更新
- [Method]: ⟨LLM-extract⟩, ⟨RL: PPO⟩
- [Mechanism]: 阶段一（P7）：ActRe prompting agent 为任意动作解释其理由。ReAct-style agent 随机采样外部动作后查询 ActRe 获取文本理由（textual rationales），将事后推理（posterior reasoning）前置到采样动作之前，合成新轨迹。Agent 为失败任务执行多条轨迹，筛选成功者。阶段二（P5）：累积轨迹进行 contrastive self-training，使用 policy gradient 方法配合二值奖励（binarized rewards）。多轮闭环迭代。§8.1 Self-Reinforce 的独特变体——创新在于 ActRe 的动作-理由合成机制，使 agent 能"理解"原本不理解的外部动作。

[Title]: VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model
- [Pathway]: Policy → Narrative → Evaluator + Evaluator → Policy (candidate new pattern §8.9, world model co-evolution)
- [Source Experience]: 真实世界 VLA policy rollout（含失败案例，特别是接触密集型操作）
- [Target Experience]: 经真实数据增强的 world model（动作条件视频生成模型）+ 经合成数据增强的 VLA policy
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 改进的 world model 生成补充合成 rollout 数据用于训练 VLA policy
- [Method]: ⟨SFT⟩
- [Mechanism]: 迭代协同改进循环：(1) 真实世界 VLA rollout → 提升 world model（动作条件视频生成模型）的物理保真度（P4：轨迹 → 学习型模拟器权重）。VLAW 发现现有 world model 因主要训练在示范数据上而缺乏失败案例的覆盖，无法准确建模接触密集型操作的关键物理细节。(2) 改进的 world model → 生成补充合成数据 → SFT 训练 VLA policy（P6/P5）。协同进化闭环：更强的 policy → 更丰富的真实 rollout（含边缘失败案例）→ 更好的 world model → 更高质量的合成数据 → 更强的 policy。归入 candidate pattern §8.9 Co-Evolving World Model——world model 是独立训练的 parametric 组件且与 policy 协同进化。

[Title]: SPORT: Iterative Trajectory Exploration for Multimodal Agents
- [Pathway]: Policy → Narrative → Policy (§8.1 Self-Reinforce)
- [Source Experience]: Agent 自身任务求解轨迹 + verifier 提供的步骤级 AI feedback
- [Target Experience]: 经步骤级偏好优化（step-wise preference optimization）更新的 controller policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 步骤级偏好数据通过 DPO 更新 controller policy 权重
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: 四个迭代组件：(1) task synthesis——自动生成多模态任务；(2) step sampling——agent 在真实环境中执行步骤；(3) step verification——verifier 提供 AI feedback 构建步骤级偏好数据；(4) preference tuning——DPO 更新 controller policy 权重。Verifier 是冻结的 AI feedback 提供者（未经训练），因此归入 §8.1 而非 §8.2。自强化闭环：policy 生成轨迹 → verifier 评判 → 偏好数据 → policy 更新 → 更好的轨迹。无需任何专家标注。

[Title]: Reflection-Based Task Adaptation for Self-Improving VLA
- [Pathway]: Narrative → Evaluator → Policy + Narrative → Narrative → Policy (dual-pathway, §8.2 + §8.3)
- [Source Experience]: Agent 自身操作任务经验（失败与成功）
- [Target Experience]: VLM 合成的 dense reward function（Evaluator）+ 质量筛选后的成功轨迹（refined Narrative）→ 经 RL + SFT 双路径训练的 VLA policy
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: Dense reward function 加速 RL 策略探索；高质量成功轨迹通过 SFT 保持 task alignment 防止 reward hacking
- [Method]: ⟨LLM-extract⟩, ⟨RL: PPO⟩, ⟨SFT⟩
- [Mechanism]: 双路径架构：(1) Failure-Driven Reflective RL 路径（§8.2）：VLM 的因果推理从失败分析中自动合成针对性的 dense reward function（P4），该聚焦奖励信号通过 RL 加速 policy 探索（P6）。(2) Success-Driven Quality-Guided SFT 路径（§8.3）：识别并选择性模仿高质量成功轨迹（P1），通过条件课程机制辅助初始探索，SFT 使 policy 扎根于整体任务成功（P5）。双路径互补——RL via proxy reward 提升探索效率但有 reward hacking 风险，SFT via quality-filtered success 保持任务对齐。两条路径共享同一源经验但在不同阶段介入。

[Title]: No More Stale Feedback: Co-Evolving Critics for Open-World Agent Learning (ECHO)
- [Pathway]: Evaluator → Policy + Policy → Narrative → Evaluator (§8.2 + critic-policy 同步协同进化)
- [Source Experience]: Agent 在策略（on-policy）rollout 轨迹 + 随时间变化的错误模式
- [Target Experience]: 同步协同进化的 critic + 改进的 policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Critic 为每条轨迹生成多条诊断意见；dual-track GRPO 同时更新 policy 和 critic
- [Method]: ⟨LLM-extract⟩, ⟨RL: GRPO⟩
- [Mechanism]: 级联 rollout 机制（cascaded rollout）：(1) Critic 为初始轨迹生成多条诊断意见。(2) Policy 精炼使 group-structured advantage estimation 成为可能（Evaluator → Policy, P6）。(3) Saturation-aware gain shaping objective 奖励 critic 在高性能轨迹中诱导增量改进——解决学习平台（learning plateaus）问题。(4) Dual-track GRPO 同时更新 critic 和 policy，确保 critic 反馈随 policy 进化保持同步。核心创新：critic 非静态/离线——它与 policy 在同步协同进化循环中持续更新，解决"stale feedback"问题。复合模式 §8.2 Evaluate-then-Optimize 的动态协同进化版本。

[Title]: Self-Improving LLM Agents at Test-Time (TT-SI / TT-D)
- [Pathway]: Narrative → Policy (P5) [test-time 变体]
- [Source Experience]: Agent 在 test time 识别出的自身不确定/失败案例
- [Target Experience]: 自增广训练样本 → test-time fine-tuned policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self} (TT-SI); {teacher} (TT-D)
- [Utilization]: 自生成样本在 test time 用于轻量 fine-tuning
- [Method]: ⟨SFT⟩
- [Mechanism]: 三步 test-time 算法：(i) Self-awareness——识别模型难以处理的样本；(ii) Self-data augmentation——从检测到的不确定样本生成相似示例；(iii) Self-improvement——使用新生成样本进行 test-time fine-tuning。TT-SI 使用同一模型进行生成和学习；TT-D 使用更强模型生成示例（蒸馏变体）。核心路径为 P5（生成示例 → policy via SFT），全部在 test time 完成，训练样本量减少 68x。非传统 composite pipeline——转化本身是单步 P5，贡献在于 self-awareness + augmentation 机制使 test-time 场景下的 P5 成为可能。

[Title]: The Lighthouse of Language: Enhancing LLM Agents via Critique-Guided Improvement (CGI)
- [Pathway]: Narrative → Evaluator → Policy (P4 + P6)
- [Source Experience]: Actor agent 在交互环境中的探索轨迹
- [Target Experience]: 经训练的 critic model（生成细粒度 NL 评估和可操作修正建议）+ 经训练的 actor policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Critic 的自然语言反馈用于指导 actor 的探索和决策，避免局部最优
- [Method]: ⟨SFT⟩
- [Mechanism]: 双玩家框架（two-player framework）：(1) P4：Critic 训练为从 actor 探索轨迹中生成细粒度评估（fine-grained assessments）和可操作修正建议（actionable revisions）。即使小型 critic 也能超越 GPT-4 的反馈质量。(2) P6：Actor 训练为利用这些 critiques 进行更稳健的探索，躲避局部最优。Critic 提供比数值奖励信号更丰富、更具操作性的自然语言反馈。复合模式 §8.2 Evaluate-then-Optimize。

[Title]: VLM Agents Generate Their Own Memories (ICAL)
- [Pathway]: Narrative → Narrative → Policy (P1 + P5)
- [Source Experience]: 次优/带噪任务示范轨迹（suboptimal trajectories）
- [Target Experience]: 泛化策略与动作标注（认知抽象：因果关系、物体状态变化、时序子目标、任务相关视觉元素）→ 经 SFT/RAG 增强的 agent policy
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {self}, {human}
- [Utilization]: 精炼示例既可用于 RAG（检索增强生成）也可用于 fine-tuning 更新 policy 权重
- [Method]: ⟨LLM-extract⟩, ⟨SFT⟩
- [Mechanism]: 阶段一（P1）：VLM 将次优轨迹抽象为泛化策略和动作标注，通过修正低效操作并标注认知抽象（因果关系、物体状态变化、时序子目标、任务相关视觉元素）实现。在相似环境中的执行过程中通过人类反馈迭代精炼。阶段二（P5）：精炼示例既可用于 RAG（ICL 级别）也可用于 fine-tuning 更新模型权重。随着示例库增长，agent 抽象新示例的效率提升（需要更少的人类反馈和环境交互）。复合模式 §8.3 Refine-then-Internalize，兼具 ICL 和 SFT 两种利用模式。

[Title]: OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: 被分解为可验证里程碑（verifiable milestones）的 GUI agent 轨迹
- [Target Experience]: 多 agent critic（OS-Themis），具备证据链审计能力的评估器
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Critic 用于 online RL training (+10.3%) 和 trajectory validation/filtering (+6.9%)
- [Method]: ⟨SFT⟩
- [Mechanism]: 多 agent critic 框架：将轨迹分解为可验证里程碑（verifiable milestones）以隔离决策关键证据，采用审查机制（review mechanism）在做出最终裁决前严格审计证据链。OS-Themis 本身是训练的 Evaluator（P4：轨迹 → critic 权重）。论文同时展示了下游应用（online RL training、trajectory filtering），这些属于 Evaluator 的 utilization 而非转化本身。若考虑完整 pipeline（P4 + 下游 P6），则属 §8.2。论文核心贡献在 critic 架构而非完整的 evaluate-then-optimize 链条。

[Title]: Policy Improvement using Language Feedback Models (LFMs)
- [Pathway]: Narrative → Evaluator → Policy (P4 + P6)
- [Source Experience]: 视觉轨迹经语言化描述 + LLM 反馈标识的理想行为
- [Target Experience]: Language Feedback Model（LFM）→ 经模仿学习改进的 policy
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {teacher}
- [Utilization]: LFM 标识理想行为（desirable behavior）用于模仿学习
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段一（P4）：LLM 对语言化描述的视觉轨迹提供反馈，标识哪些行为是"理想行为"（desirable behaviour）——这些反馈用于训练 LFM。阶段二（P6）：LFM 对理想行为的识别用于模仿学习，改进 policy 的任务完成率。LFM 可修改为提供人类可解释的反馈而不损失性能。复合模式 §8.2。注意 Experience Source 为 {teacher}，因为 feedback 信号来自外部 LLM。

[Title]: RLAnything: Forge Environment, Policy, and Reward Model in Completely Dynamic RL System
- [Pathway]: Narrative → Evaluator → Policy (§8.2 + co-evolution loop)
- [Source Experience]: Agent 交互轨迹 + 步骤级和结局级信号（step-wise and outcome signals）
- [Target Experience]: 联合优化的 RM + policy + 自动适配的环境
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: RM 提供整合反馈（步骤级 + 结局级）训练 policy；consistency feedback 反向优化 RM；环境自动适配同时改进 RM 和 policy 训练
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 完全动态闭环系统：(1) Policy 使用步骤级和结局级融合反馈训练。(2) RM 通过 consistency feedback 联合优化——RM 的改进反过来提升 policy 训练质量。(3) 理论驱动的自动环境适配（automatic environment adaptation）利用来自 RM 和 policy 的 critic feedback 改进环境配置，增强两者的训练效果。三组件（环境、policy、RM）协同进化。核心复合为 §8.2（Narrative → Evaluator → Policy），但环境适配机制使协同进化比标准 §8.2 更深一层——RM 和 policy 在动态适应的环境中共同进化。

[Title]: Pre-Trained Language Models for Interactive Decision-Making
- [Pathway]: Narrative → Policy (P5) [含 hindsight relabeling]
- [Source Experience]: 专家示范 + 经 hindsight relabeling 的"失败"经验（以新目标重新标注）
- [Target Experience]: 经 behavior cloning + self-supervised loop 训练的 LM-based policy network
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}, {self}
- [Utilization]: Behavior cloning from expert demos + self-supervised policy update from relabeled experiences
- [Method]: ⟨SFT⟩
- [Mechanism]: 目标和观测编码为序列嵌入；以预训练 LM 初始化的 policy network 预测下一步动作。阶段一：在专家示范上 behavior cloning 微调。阶段二：Active data gathering——agent 迭代与环境交互，将过去"失败"的经验以新目标重新标注（hindsight relabeling：失败轨迹对目标 A 而言是失败，但对替代目标 B 可能是成功），在自监督循环中更新 policy。Hindsight relabeling 本质上是一次 P1（失败轨迹 → 重标注为成功轨迹），随后 P5（重标注数据 → policy SFT）。关键发现：LM 权重初始化和序列化输入表征对泛化至关重要，而输入编码格式（自然语言 vs. 任意序列编码）影响甚微。

[Title]: OS-Oracle: A Comprehensive Framework for Cross-Platform GUI Critic Models
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: 通过可扩展数据管线合成的跨平台 GUI 交互数据（310k critic samples）
- [Target Experience]: OS-Oracle-7B critic model（经 SFT + CP-GRPO 两阶段训练）
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}
- [Utilization]: Pre-critic 在执行前评估每个动作；提升原生 GUI agent 在 OSWorld 和 AndroidWorld 的性能
- [Method]: ⟨SFT⟩, ⟨RL: GRPO⟩
- [Mechanism]: 可扩展数据管线合成跨平台 GUI critic 数据。两阶段训练：SFT + Consistency-Preserving GRPO（CP-GRPO）——GRPO 的变体，用于训练 critic 本身而非 policy。主转化为 P4（GUI 轨迹 → critic 权重）。当作为 pre-critic 服务下游 agent 时 pipeline 变为 §8.2（Evaluator → Policy），但论文核心贡献在 critic 训练方法论和 OS-Critic Bench 基准。CP-GRPO 中 consistency-preserving 机制确保 critic 在不同平台间保持评判一致性。

[Title]: ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Agent 自我判断的成功和失败交互经验
- [Target Experience]: 可泛化的推理策略（generalizable reasoning strategies）存入 ReasoningBank 记忆库
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 检索到的相关记忆指导 agent 交互；新学到的经验整合回记忆库；MaTTS 通过分配更多 compute 扩展交互经验以合成更高质量记忆
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: ReasoningBank 从 agent 自我判断的成功和失败经验中蒸馏可泛化的推理策略（P1：原始经验 → 精炼推理策略）。MaTTS（memory-aware test-time scaling）通过扩展推理时的交互计算量，生成丰富多样经验，为合成更高质量记忆提供对比信号——更好的记忆反过来指导更有效的 scaling，形成协同效应（synergy）。全程无参数更新——记忆通过检索注入上下文窗口引导决策。归入纯 P1。
> Note: 此前误标为 P1+P5 light。记忆引导仅通过检索 ICL 实现，不涉及权重更新，修正为纯 P1。

[Title]: AutoRefine: From Trajectories to Reusable Expertise for Continual LLM Agent Refinement
- [Pathway]: Narrative → Schematic + Narrative (multi-target, §8.8)
- [Source Experience]: Agent 执行历史（execution histories / trajectories）
- [Target Experience]: 双形态 Experience Patterns：专用子 agent（Schematic，具备独立推理和记忆）+ 技能模式（Narrative，guidelines / code snippets）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Experience Patterns 检索并应用于新任务；持续维护机制评分、剪枝和合并模式以防止知识库退化
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 从执行历史中提取两类并行经验形态：(1) P2：程序化子任务提取为专用子 agent，具备独立推理和记忆——属于 Schematic 实体（可执行的子 agent 规范）；(2) P1：静态知识提取为技能模式，以 guidelines 或 code snippets 形式存在——属于 Narrative 实体。持续维护机制（评分、剪枝、合并）防止知识库随经验累积而退化。Multi-target §8.8：同一提取框架同时产出 Schematic（子 agent）和 Narrative（技能模式）两类载体。自动提取超越人工设计系统（TravelPlanner 27.1% vs. 12.1%）。

[Title]: Improving Vision-Language-Action Model with Online Reinforcement Learning (iRe-VLA)
- [Pathway]: Policy → Narrative → Policy (§8.1 Self-Reinforce)
- [Source Experience]: VLA 模型自身的在线交互轨迹
- [Target Experience]: RL 探索产生的轨迹 → 经 SFT 稳定化训练的 VLA policy
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: RL 探索的轨迹通过 SFT 回蒸馏到 VLA policy；迭代交替 RL 和 SL
- [Method]: ⟨RL: PPO⟩, ⟨SFT⟩
- [Mechanism]: 直接在大 VLA 模型上应用 online RL 面临训练不稳定和计算负担两大挑战。iRe-VLA 在 RL 和 SL 之间迭代交替：阶段一（P7）：通过 RL 探索产生轨迹（利用 RL 的探索优势）。阶段二（P5）：探索轨迹通过 SFT 蒸馏回 policy（利用 SL 的稳定性）。§8.1 模式，iRe（iterative RL-SL）作为集成机制解决大规模 VLA 的 RL 训练稳定性问题。

[Title]: Memento No More: Coaching AI Agents to Master Multiple Tasks via Hints Internalization
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Agent 收集的新经验 + 人类纠正性提示（corrective hints）
- [Target Experience]: 通过 context distillation 将提示内化到权重中的 agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {human}
- [Utilization]: 内化的知识替代不断扩展的 prompts，实现 multi-task mastery
- [Method]: ⟨SFT⟩
- [Mechanism]: 迭代过程：agent 收集新经验 → 接收人类以提示（hints）形式的纠正反馈 → 通过 context distillation 训练过程将反馈整合到模型权重中。核心机制是 context distillation：将 hints 增强后的上下文转化为权重更新，使 agent 内化知识而非依赖不断膨胀的 prompts。P5：人类 hints + agent 经验 → policy 权重 via SFT。灵感来自 anterograde amnesia（顺行性遗忘症）的比喻——不依赖外部"笔记系统"。

[Title]: XSkill: Continual Learning from Experience and Skills in Multimodal Agents
- [Pathway]: Narrative → Narrative + Schematic (multi-target, §8.8)
- [Source Experience]: Agent 的过往多路径 rollout 轨迹
- [Target Experience]: Experiences（动作级指导：工具选择与决策）+ Skills（任务级指导：规划与工具使用）
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {self}
- [Utilization]: 检索并适配到当前视觉上下文用于推理；使用历史反馈到累积过程形成持续学习闭环
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 双流框架从多路径 rollout 中并行提取：(1) P1：Experiences 蒸馏为简洁的动作级指导（action-level guidance），用于工具选择和决策——Narrative；(2) P2：Skills 蒸馏为结构化的任务级指导（task-level guidance），用于规划与工具编排——这些技能具有较强的 Schematic 特征（程序性/结构化）。两者均基于视觉观察进行 grounding。跨 rollout critique 提升提取质量。持续学习闭环：推理时检索适配 → 使用历史反馈到累积 → 改进的累积提升后续提取。Multi-target §8.8。

[Title]: Memp: Exploring Agent Procedural Memory
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: 过往 agent 交互轨迹
- [Target Experience]: 细粒度逐步指令 + 高层脚本式抽象（双形态程序化记忆）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 程序化记忆被检索并部署用于类似任务；动态更新机制持续更新、修正和废弃过时内容
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 将过往轨迹蒸馏为双形态程序化记忆：(1) 细粒度、逐步指令（fine-grained, step-by-step instructions），(2) 高层、脚本式抽象（higher-level, script-like abstractions）。两者均属于 Schematic——是具备执行语义的过程性模板/脚本，而非纯自然语言提示。动态管理机制（更新、修正、废弃）确保记忆随新经验演进。P2：原始轨迹 → 结构化程序化记忆。关键发现：从更强模型构建的程序化记忆迁移到较弱模型仍能带来显著增益——Schematic 载体是 model-agnostic 的。

[Title]: Voyager: An Open-Ended Embodied Agent with Large Language Models
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Agent 在 Minecraft 中的交互经验（环境反馈、执行错误、自我验证）
- [Target Experience]: 不断增长的可执行代码技能库（temporally extended, interpretable, compositional skills）
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 技能库存取和检索复杂行为；技能快速组合（compositional）缓解灾难性遗忘
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 迭代 prompting 机制整合环境反馈、执行错误和自我验证以持续改进程序。技能以可执行代码（executable code）形式存储于技能库中——属于 Schematic 载体。自动课程（automatic curriculum）最大化探索。P2：原始交互经验 → 可执行代码技能库。注意：此处的 skills 是 executable code（Schematic），而非自然语言技能描述（若为 NL 描述则归 Narrative）。奠基性工作——首次在 embodied 场景中大规模验证 Narrative → Schematic 转化。GPT-4 黑盒查询，无参数更新。

[Title]: Skill Set Optimization (SSO)
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Agent 与环境交互的轨迹 + 环境奖励信号
- [Target Experience]: 可迁移技能集（common subtrajectories + subgoals + instructions，经 pruning 优化）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 技能以 ICL 方式提供给 LLM actor 强化高奖励行为；技能集经 pruning 持续优化
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 通过提取高奖励的公共子轨迹（common subtrajectories with high rewards）并生成子目标和指令来构建技能。技能经 pruning 持续优化——移除不再产生高奖励的技能。这些技能是结构化的过程性单元（Schematic：具备定义明确的子目标的可执行子轨迹），而非纯 NL hints。P2：原始轨迹 → 结构化技能集。ICL-based policy improvement 通过技能注入实现。与 Voyager 的区别：SSO 的技能是子轨迹 + 指令的混合体（介于 Narrative 和 Schematic 之间，但因具有可执行的子轨迹结构归入 Schematic）。

[Title]: WebXSkill: Skill Learning for Autonomous Web Agents
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: 合成 web agent 轨迹
- [Target Experience]: 可执行技能（参数化动作程序 parameterized action programs + 步骤级 NL 指导）
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}
- [Utilization]: 两种部署模式：grounded mode（全自动多步执行）和 guided mode（agent 以技能为逐步指令进行原生规划）
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 三阶段：(1) 技能提取——从合成轨迹中挖掘可复用的动作子序列，抽象为参数化技能（parameterized skills）。每个技能将参数化动作程序（可执行）与步骤级自然语言指导（可解释）配对。(2) 技能组织——将技能索引到基于 URL 的图中，实现上下文感知检索。(3) 技能部署——暴露 grounded 和 guided 两种互补模式。P2：原始轨迹 → 可执行参数化动作程序（Schematic）。核心创新：弥合"文本技能不可执行、代码技能不透明"的 grounding gap——每个技能兼具执行力和可解释性。

[Title]: Failure Makes the Agent Stronger: Enhancing Accuracy through Structured Reflection
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: 包含结构化反思（错误诊断 + 修正后的可执行跟进调用）的工具使用轨迹
- [Target Experience]: 经 DAPO + GSPO 训练的策略，学会按 Reflect → Call → Final 步骤执行
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 结构化反思数据用于训练 agent 的错误诊断和修复能力
- [Method]: ⟨RL: DPO⟩, ⟨RL: GRPO⟩
- [Mechanism]: 结构化反思（structured reflection）将"错误到修复"的路径转化为显式、可控、可训练的动作：agent 基于前一步证据诊断失败原因，然后提出正确的可执行跟进调用。训练结合 DAPO（Direct Alignment Policy Optimization）和 GSPO（Group Sampling Policy Optimization）目标，配合针对工具使用的奖励方案，优化"Reflect → Call → Final"的步骤策略。P5：包含结构化反思的轨迹 → policy via RL。结构化反思在此是动作空间的一种格式（action format），而非独立的载体——它是被训练进 policy 的行为模式。创新点在于使反思从启发式 prompt 变为可优化的动作。
> New tag: ⟨RL: DAPO⟩ — Direct Alignment Policy Optimization，针对工具使用场景的 RL 优化目标，优化 stepwise strategy（Reflect → Call → Final）。
> New tag: ⟨RL: GSPO⟩ — Group Sampling Policy Optimization，用于多轮工具交互中优化步骤级策略的 RL 目标。

[Title]: LaViT: Aligning Latent Visual Thoughts for Multi-modal Reasoning
- [Pathway]: Out of Scope
- [Mechanism]: 该工作聚焦多模态 latent reasoning 中的 knowledge distillation——学生模型自回归重建教师模型的 visual semantics 和 attention trajectories 以弥合 Perception Gap（学生模仿教师文本输出时实际关注不同的视觉区域）。核心是跨模型 latent alignment（teacher → student latent space），源端的 visual attention trajectories 来自教师推理过程，但目标端是学生模型的 latent representation 对齐。属于模型蒸馏（Parametric → Latent），不满足本 Survey 的经验转化判定标准——缺乏 Agent 决策过程语义（无 e=(c,a,o,f) 映射）与异构动作空间。归入 §3.2 排除：纯模型蒸馏，经验语义链断裂。

[Title]: Contextual Experience Replay (CER)
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Agent 过往交互经验（环境动态 + 常见决策模式）
- [Target Experience]: 动态记忆缓冲区（积累并合成的过往经验）
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {self}
- [Utilization]: 检索到的相关知识注入 agent 上下文窗口用于新任务
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Training-free 框架：积累和合成过往经验到动态记忆缓冲区。经验涵盖环境动态（environment dynamics）和常见决策模式（common decision-making patterns）。测试时检索相关知识并注入 agent 上下文窗口。P1：原始轨迹 → 合成压缩经验（记忆缓冲区）。无参数更新——纯 Narrative → Narrative 抽象用于 ICL 复用。相对 GPT-4o baseline 提升 51.0%。

[Title]: TAME: A Trustworthy Test-Time Evolution of Agent Memory
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Agent 任务执行轨迹（executor memory）+ 历史安全/效用反馈（evaluator memory）
- [Target Experience]: 可泛化方法论（executor memory）+ 精炼的安全/效用评估（evaluator memory）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 双记忆闭环：记忆过滤 → 草稿生成 → 可信精炼 → 执行 → 双轨记忆更新
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 双记忆进化框架应对 Agent Memory Misevolution（良性任务进化中安全对齐退化）：(1) Executor memory 从任务轨迹中蒸馏可泛化方法论以提升任务表现（P1）。(2) Evaluator memory 基于历史反馈精炼安全与效用的评估（P1）。闭环确保可信度与任务表现联合提升。两个转化均为 P1（原始经验 → 精炼文本记忆）。注意 Evaluator memory 在此是 Narrative 构造（文本形式的安全/效用评估），非参数化 V-Par——这是关键区分。

[Title]: Investigate-Consolidate-Exploit (ICE)
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Agent 跨任务的规划与执行轨迹
- [Target Experience]: 简化的 workflows 和 pipelines（从轨迹中整合提取）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 整合的 workflows 用于改进任务执行；API 调用减少高达 80%
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 跨任务自进化策略：动态调查（investigate）规划与执行轨迹 → 整合为简化的 workflows 和 pipelines（consolidate）→ 用于改进任务执行（exploit）。P2：原始轨迹 → 结构化 workflows/pipelines（Schematic——具备执行语义的过程性模板）。跨任务迁移使 ICE 区别于仅做 intra-task learning 的方法。当与 GPT-3.5 结合时性能匹敌裸 GPT-4——Schematic 载体的效率增益。注意：workflow/pipeline 按 §2.2.3 规则无论以何种形式存在均属 Schematic。

[Title]: TGPO: Tree-Guided Preference Optimization for Robust Web Agent RL
- [Pathway]: Narrative → Evaluator → Policy (P4 + P6)
- [Source Experience]: 合并到树结构中的 web agent 轨迹（消除标签冲突）
- [Target Experience]: Process Reward Model（通过子目标进展、冗余检测、动作验证自动生成细粒度奖励）→ 经 offline RL 训练的 policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: PRM 提供细粒度奖励；动态加权机制优先训练高影响力决策点
- [Method]: ⟨RL: DPO⟩, ⟨SFT⟩
- [Mechanism]: 阶段一（P4）：树结构轨迹表征合并跨轨迹的语义相同状态以消除标签冲突。Process Reward Model 训练为通过子目标进展（subgoal progress）、冗余检测（redundancy detection）和动作验证（action verification）自动生成细粒度奖励。阶段二（P6）：Offline RL 配合动态加权机制（dynamic weighting），利用 PRM 信号优先训练高影响力决策点（high-impact decision points）。复合模式 §8.2。

[Title]: Agent Workflow Memory (AWM)
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Agent 交互轨迹（来自训练示例或测试查询）
- [Target Experience]: 归纳的通用可复用例程（workflows）
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Workflows 被选择性地提供给 agent 以指导后续生成；同时适用于离线和在线场景
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 从过往轨迹中归纳常用可复用例程（commonly reused routines / workflows）。同时支持离线（从训练示例预先归纳）和在线（从测试查询即时归纳）场景。P2：原始轨迹 → 可复用 workflows（Schematic：结构化过程性例程）。跨任务、网站和领域泛化验证。相对成功率在 Mind2Web 和 WebArena 上分别提升 24.6% 和 51.1%。

[Title]: AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials
- [Pathway]: Narrative → Narrative → Policy (P1 + P5)
- [Source Experience]: 从互联网公开获取的 web tutorials（文本教程）
- [Target Experience]: 多模态 GUI 轨迹（text-based HTML + vision-based screenshot with pixel-level actions）→ 经 SFT 训练的 GUI agent policy
- [Source Modality]: [txt]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}
- [Utilization]: 合成多模态轨迹用于训练 GUI agent（WebArena, ScreenSpot Web, Multimodal Mind2Web）
- [Method]: ⟨LLM-extract⟩, ⟨SFT⟩
- [Mechanism]: 阶段一（P1）：三阶段管线——(1) 使用专用分类模型自动从互联网抓取并过滤 tutorial-like texts；(2) 将文本转化为带逐步指令的结构化任务规范；(3) VLM agent 在真实环境中执行指令，VLM-based evaluator 验证轨迹正确性。每条约 $0.55 成本，无需人类标注。阶段二（P5）：合成多模态轨迹（含 CoT 推理增强）用于 SFT 训练 GUI agent。复合模式 §8.3：web tutorials（外部 Narrative 源）→ 结构化任务规范 + 验证轨迹 → policy 权重。跨模态转化（源端纯文本教程 → 目标端视觉 GUI 操作轨迹）。

[Title]: CLEANER: Self-Purified Trajectories Boost Agentic Reinforcement Learning
- [Pathway]: Narrative → Narrative → Policy (P1 + P5)
- [Source Experience]: 带噪声的 agent 探索轨迹（含频繁执行失败）
- [Target Experience]: 自我纯化的干净轨迹（失败被成功自我修正替换）→ 经 RL 更新的 policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 干净轨迹用于 RL 训练，policy 内化正确推理模式而非 error-recovery loops
- [Method]: ⟨LLM-extract⟩, ⟨RL: GRPO⟩
- [Mechanism]: 阶段一（P1）：Similarity-Aware Adaptive Rollback（SAAR）自主构建纯化轨迹——通过回顾式替换失败为成功的自我修正。基于语义相似度，SAAR 自适应调节替换粒度：从浅层执行修复到深层推理替换。阶段二（P5）：Policy 在自我纯化路径上通过 RL 训练，内化正确推理模式（而非错误恢复循环）。复合模式 §8.3：原始噪声轨迹 → 自我纯化轨迹（refined Narrative）→ policy via RL。与外部过滤方法的区别：CLEANER 利用模型内在的自我修正能力，无需外部 verifier。

[Title]: MCTS-EP: Empowering Embodied Planning with Online Preference Optimization
- [Pathway]: Narrative → Policy (P5) [MCTS-guided exploration]
- [Source Experience]: MCTS 引导的探索轨迹 + 偏好数据
- [Target Experience]: 经迭代偏好优化训练的 embodied agent policy
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 偏好数据通过 iterative training pipeline 更新 policy
- [Method]: ⟨MCTS⟩, ⟨RL: DPO⟩
- [Mechanism]: MCTS 引导探索收集偏好数据；高效多模态推理机制处理轨迹；迭代训练管线通过偏好优化（DPO）更新 policy。理论证明 MCTS-EP 在强凸损失函数下达到比传统 on-policy 算法更好的性能界，可形式化为 search-enhanced GAIL 变体。P5：MCTS 探索轨迹 → policy via DPO。MCTS 在此是搜索/规划方法，用于结构化探索并生成偏好数据——它本身不是载体转化，而是为 P5 提供更高质量训练数据的方式。

[Title]: Environment Maps: Structured Environmental Representations for Long-Horizon Agents
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: 异质证据（屏幕录制 screen recordings + 执行轨迹 execution traces）
- [Target Experience]: 结构化图（四个组件：Contexts 抽象位置、Actions 参数化功能、Workflows 观测轨迹、Tacit Knowledge 领域定义和可复用过程）
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 持久化、agent-agnostic 表征用于长程规划；人类可解释、可编辑、可增量精炼
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 将异质证据（屏幕录制、执行轨迹）整合为结构化图表征。四核心组件：Contexts（抽象位置）、Actions（参数化 affordances）、Workflows（观测轨迹）、Tacit Knowledge（领域定义与可复用过程）。P2：原始多模态交互日志 → 结构化环境图（Schematic）。几乎使 baseline 成功率翻倍（14.2%→28.2%），超越直接使用原始轨迹数据的 agent（23.3%）。关键属性：跨会话持久化、agent-agnostic——环境图独立于任意特定 agent 实例。

[Title]: WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: 跨会话的原始 web 导航日志（raw navigation logs）
- [Target Experience]: 压缩的 episodic 摘要 + 任务特定建议（task-specific advice）
- [Source Modality]: [vis+txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 检索到的相关经验通过 runtime hooks 注入为任务特定建议；跨会话记忆使 agent 无需重训练即可持续改进
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 三组件：(1) WebCondenser 将原始导航日志标准化为简洁摘要（P1：原始轨迹 → 压缩摘要）；(2) External Memory Store 以 episodic 形式组织完整轨迹；(3) Coach 基于相似度和新近度检索相关经验，决定是否通过 runtime hooks 注入任务特定建议。自进化通过持续从新导航轨迹中策划 episodic memory 实现。P1：原始导航日志 → 压缩摘要 + 建议。无参数更新——model-agnostic，training-free。38B 模型从 47% 提升至 61%（WebVoyager）。

[Title]: Scaling Autonomous Agents via Automatic Reward Modeling And Planning
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: LLM-based agent 随机导航环境产生的多样化动作轨迹
- [Target Experience]: 从轨迹三元组（任务意图、正响应、负响应）自动学习的奖励模型
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: RM 用于评估动作轨迹和为任务规划提供启发式信号
- [Method]: ⟨LLM-extract⟩, ⟨SFT⟩
- [Mechanism]: 一个 LLM agent 随机导航环境产生多样化动作轨迹。另一个 LLM 为每条轨迹分配任务意图（task intent），并合成正负响应配对。这些三元组（任务意图、正响应、负响应）通过 SFT 训练 RM。P4：轨迹 → RM 权重。RM 的下游应用（评估轨迹、提供规划启发式）属于 utilization 而非转化本身。核心贡献在于无需人类标注自动学习 RM，克服数据稀缺和 API 限制。

[Title]: ExpeL: LLM Agents Are Experiential Learners
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Agent 在一组训练任务中的自身执行经验
- [Target Experience]: 提取的自然语言洞察（insights）和过往经验
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 提取的洞察和过往经验在推理时被召回用于做出明智决策
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 自主从训练任务集合中收集经验并提取自然语言知识。推理时 agent 召回提取的洞察和过往经验以指导决策。P1：原始任务轨迹 → 提取的 NL insights。无参数更新——专为只能通过 API 访问的专有模型设计。随经验积累持续增强性能，支持迁移学习。奠基性 P1 工作。

[Title]: SCOPE: Prompt Evolution for Enhancing Agent Effectiveness
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Agent 执行轨迹（纠正失败和增强失败案例）
- [Target Experience]: 进化的 prompt（合成的 guidelines：战术特异性 + 战略通用性）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 进化后的 prompt 替代静态 prompt；Dual-Stream 机制平衡战术和战略指导
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 将上下文管理框架化为在线优化问题：从执行轨迹中合成 guidelines，自动进化 agent 的 prompt。Dual-Stream 机制平衡战术特异性（解决即时错误）和战略通用性（进化长期原则）。Perspective-Driven Exploration 最大化策略覆盖。P1：原始执行轨迹 → 进化的 prompt guidelines。HLE 任务成功率从 14.23% 提升至 38.64%，无人工干预。

[Title]: AutoPlay: Scaling Synthetic Task Generation for Agents via Exploration
- [Pathway]: Narrative → Narrative → Policy (P1 + P5)
- [Source Experience]: MLLM explorer agent 系统性发现环境状态和功能的探索轨迹
- [Target Experience]: 环境扎根的多样化任务 → 用于训练 MLLM-based UI agent 的大规模示范数据
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 生成的任务使能大规模任务示范合成；MLLM verifier-based rewards 使能 RL 训练的扩展
- [Method]: ⟨LLM-extract⟩, ⟨SFT⟩, ⟨RL: GRPO⟩
- [Mechanism]: 阶段一（P1）：探索阶段——MLLM explorer 系统性揭示新环境状态和功能。任务生成阶段——task generator 利用探索轨迹和任务 guideline prompts 合成多样化、可执行、可验证的任务。阶段二（P5）：生成的任务用于 SFT 训练 MLLM-based UI agent（移动端 +20.0%，桌面端 +10.9%）。此外 MLLM verifier-based rewards 使能 RL 训练扩展（额外 +5.7%）。复合模式 §8.3：探索轨迹 → 合成任务 → policy 权重。

[Title]: Experience-Evolving Multi-Turn Tool-Use Agent with Hybrid Episodic-Procedural Memory (H-EPM)
- [Pathway]: Narrative → Schematic + Narrative (multi-target, §8.8)
- [Source Experience]: 累积的多轮工具使用轨迹
- [Target Experience]: 工具图（tool graph，边含 episodic 摘要）——Schematic 结构 + Narrative 标注
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Memory-guided RL 将探索偏向历史上成功的工具转换；推理时动态平衡 episodic recall 和 procedural execution
- [Method]: ⟨LLM-extract⟩, ⟨RL: GRPO⟩
- [Mechanism]: 从累积轨迹构建工具图：循环性工具到工具依赖关系捕获程序化例程（Schematic：图结构），每条边附加紧凑的 episodic 上下文摘要（Narrative）。推理时动态平衡 episodic recall（Narrative：上下文推理）和 procedural execution（Schematic：例行步骤）。Memory-guided RL 将探索偏向历史上成功的工具转换。Multi-target：P2（轨迹 → 工具图结构）+ P1（轨迹 → episodic 摘要）。RL 部分添加 P5（记忆偏置轨迹 → policy）。

[Title]: Enhancing Web Agents with a Hierarchical Memory Tree (HMT)
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Web 交互的原始 agent 轨迹
- [Target Experience]: 三级层次化记忆：Intent level（标准化任务目标）、Stage level（可复用语义子目标，含前置/后置条件）、Action level（动作模式配可迁移语义元素描述）
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Stage-aware inference：Planner 验证前置条件并将当前状态与正确逻辑子目标对齐；Actor 通过匹配存储的语义描述到目标页面来落地动作
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 自动抽象管线从原始轨迹构建三级层次化记忆，显式解耦逻辑规划（Intent/Stage）与动作执行（Action level），解决扁平记忆结构的 workflow mismatch 问题。P2：原始轨迹 → 结构化层次化记忆（Schematic：树结构，含形式化的前置/后置条件和语义元素描述）。跨网站和跨领域泛化显著优于扁平记忆方法。

[Title]: Bootstrapping Language-Guided Navigation Learning with Self-Refining Data Flywheel (SRDF)
- [Pathway]: Policy → Narrative → Policy (§8.1 Self-Reinforce, cross-model)
- [Source Experience]: 指令生成器和导航器模型生成的 instruction-trajectory pairs
- [Target Experience]: 逐步提升质量的数据 → 改进的导航器 policy + 改进的指令生成器
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 更高保真度数据训练更好的生成器 → 更好的生成器产出更高质量数据 → 更好的导航器
- [Method]: ⟨SFT⟩
- [Mechanism]: 跨模型飞轮（cross-model flywheel）：(1) 基础生成器创建初始数据池 → 训练基础导航器。(2) 训练后的导航器过滤数据池 → 更高保真度数据 → 训练更好的生成器。(3) 更好的生成器产出更高质量数据 → 训练下一轮导航器。两个模型之间的迭代自精炼过程。导航器超越人类表现（76%→78% SPL）。§8.1 模式扩展到跨模型：导航器 policy 产生过滤判断 → 精炼数据 → 改进的导航器和生成器。生成器的改进是次要目标。

[Title]: ProRe: A Proactive Reward System for GUI Agents via Reasoner-Actor Collaboration
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: GUI agent 轨迹 + evaluator agents 主动探测环境产生的额外观察
- [Target Experience]: 主动式奖励系统（通用推理器 + 领域特定 evaluator agents，产出可验证奖励）
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 更准确可验证的奖励分配给 GUI agent；与 policy agent 集成提升成功率最高 22.4%
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 主动式奖励范式（proactive reward paradigm）：通用推理器调度针对性的状态探测任务，evaluator agents 通过主动与环境交互执行探测以收集额外观察。这使推理器能分配更准确可验证的奖励——克服被动观察型 LLM-as-a-Judge 的局限性。P4：GUI 轨迹 + 主动探测证据 → 奖励判断。注意此处的奖励系统是 agentic 的（主动探测环境），而非训练的参数化模型——以 agentic evaluator 形式实现 P4。利用"GUI 任务易验证难求解"的洞察。

[Title]: Agentic Reward Modeling: Verifying GUI Agent via Online Proactive Interaction (VAGEN)
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: 具有部分状态可观测性的 GUI agent 轨迹
- [Target Experience]: 能自主规划验证策略并主动探测环境的 verifier agent
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Verifier agent 为 RLVR 提供准确评估；test-time scaling strategies 进一步增强性能
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 范式转换——从被动评估到 Agentic Interactive Verification（主动交互式验证）。VAGEN 部署一个配备交互工具的 verifier agent，自主规划验证策略并主动探测环境收集任务完成证据。P4：GUI 轨迹 + 交互式探测 → 验证评估。Verifier 是 agentic 系统而非训练的参数化模型。核心洞察：GUI 任务"easy to verify but hard to solve"，因此 agentic verifier 比 passive judge 更有效。

[Title]: Agent KB: Leveraging Cross-Domain Experience for Agentic Problem Solving
- [Pathway]: Narrative → Narrative + Schematic (multi-target, §8.8)
- [Source Experience]: 从异质 agent 框架（smolagents, OpenHands, OWL）聚合的轨迹
- [Target Experience]: 含跨领域 workflows 的结构化知识库（Schematic）+ 诊断性修复（Narrative）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 混合检索：planning 以跨领域 workflows 播种 agent；feedback 应用针对性诊断修复；disagreement gate 防止知识干扰
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 将多个 agent 框架的轨迹聚合到通用记忆基础设施中。两阶段检索：(1) planning 以跨领域 workflows 播种 agent（Schematic：过程性模板）；(2) feedback 应用针对性诊断修复（Narrative：错误特定指导）。Disagreement gate 确保检索知识增强而非扰乱推理。Multi-target §8.8：P1（轨迹 → 诊断修复）+ P2（轨迹 → 跨领域 workflows）。跨框架迁移无需重训练——奠定 collective agent intelligence 基础。

[Title]: Self-Supervised Bootstrapping of Action-Predictive Embodied Reasoning (R&B-EnCoRe)
- [Pathway]: Narrative → Narrative → Policy (P1 + P5)
- [Source Experience]: 互联网规模知识 + VLA 模型的 embodied 交互轨迹
- [Target Experience]: 精炼的 embodiment-specific 推理策略数据集 → 蒸馏到 VLA policy 权重
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 精炼推理数据集用于训练 VLA 模型，蒸馏出能预测成功控制的推理模式
- [Method]: ⟨LLM-extract⟩, ⟨SFT⟩
- [Mechanism]: 将推理视为重要性加权变分推断（importance-weighted variational inference）中的潜变量。模型生成并蒸馏一个精炼的 embodiment-specific 策略推理训练数据集——无需外部奖励、验证器或人类标注。阶段一（P1）：互联网规模知识 → 通过自监督精炼生成 embodiment-specific 推理策略。阶段二（P5）：精炼推理数据集蒸馏到 VLA policy。操作成功率 +28%，导航分数 +101%。绕过手动标注工程，将互联网知识扎根于物理执行。

[Title]: AutoSurfer — Teaching Web Agents through Comprehensive Surfing, Learning, and Modeling
- [Pathway]: Narrative → Narrative → Policy (P1 + P5)
- [Source Experience]: 系统性广度优先探索轨迹（覆盖网站完整动作空间）
- [Target Experience]: 探索扎根的任务规范 + 精炼轨迹 → 经 SFT 训练的 web agent
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 探索轨迹既用作任务合成的 grounding context，也用作 hints 指导 web agent 进行更准确的轨迹精炼
- [Method]: ⟨LLM-extract⟩, ⟨SFT⟩
- [Mechanism]: 阶段一（P1）：系统性广度优先探索——维护发现页面和动作轨迹的队列，跨页面传播知识以避免冗余探索，递归展开多级 GUI 元素。探索轨迹用于扎根任务合成（减少幻觉），并作为 hints 引导 web agent 进行更准确的轨迹精炼。阶段二（P5）：生成的数据用于 SFT 训练 web agent。复合模式 §8.3。总体任务完成准确率 24.23%，超越此前最佳方法 Explorer/OS-Genesis/SynthAgent 的 19.59%。

[Title]: Bifrost: Steering Strategic Trajectories to Bridge Contextual Gaps
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: 先前已解决的任务轨迹（成功 rollout）
- [Target Experience]: 通过表征层引导适配目标上下文的改编轨迹（context-adapted trajectories）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 改编轨迹用作 ICL examples 辅助后续推理
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 揭示 context-trajectory correlation：上下文的变化与轨迹的变化高度并行。Training-free 方法——利用上下文差异在表征层（agent hidden states）精确引导先前成功轨迹向目标任务适配，在共享空间中实现轨迹转化与目标上下文的准确对齐。P1 的新颖变体：转化通过 representation-level steering 而非 LLM extraction 实现——在隐空间中对轨迹表征进行操纵以弥合上下文差异。区别于传统的 LLM-extract 式 P1。

[Title]: ACON: Optimizing Context Compression for Long-horizon LLM Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: 长程 agent 轨迹（环境观察 + 交互历史）
- [Target Experience]: 简洁而有信息量的压缩上下文（condensed context）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 压缩上下文替代完整上下文；蒸馏后的小型 compressor 降低开销；增强小型 LM 作为长程 agent 的性能
- [Method]: ⟨LLM-extract⟩, ⟨SFT⟩
- [Mechanism]: 在自然语言空间中进行压缩 guideline 优化：给定完整上下文成功但压缩上下文失败的成对轨迹，强 LLM 分析失败原因并更新压缩 guideline。优化后的 LLM compressor 随后蒸馏到更小模型（SFT，属于模型压缩而非经验转化）。P1：长轨迹上下文 → 压缩精炼。核心 P1 机制是迭代 guideline-based 压缩优化——压缩 guideline 本身是 Narrative 产物。峰值 token 减少 26-54%，蒸馏后保持 >95% 准确率。

[Title]: WebCoT: Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Web agent 轨迹数据 + 重构的 CoT 推理（reflection & lookahead, branching, rollback）
- [Target Experience]: 经 SFT 训练的 backbone LLM，具备增强的 web 推理能力
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 将显著的推理模式蒸馏到 backbone LLM 权重中
- [Method]: ⟨SFT⟩
- [Mechanism]: 识别 web agent 的关键推理技能（reflection & lookahead, branching, rollback），将 agent 在推理时的推理算法重构为 CoT rationales。这些 CoT 增强轨迹用于 SFT 训练 backbone LLM。P5：推理增强轨迹 → policy via SFT。CoT 重构是数据预处理/标注步骤，而非独立的载体转化——本质是将推理时行为模式显式化为训练数据中的 CoT，然后通过 SFT 内化。

[Title]: Weak-to-Strong Generalization with Failure Trajectories: A Tree-based Approach
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: 弱模型生成的动作轨迹（成功和失败均用），组织为轨迹树
- [Target Experience]: 经 MCTS 优化轨迹树训练的强模型 policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: 轨迹树 + MCTS 用于激发强模型的最优策略
- [Method]: ⟨MCTS⟩, ⟨SFT⟩
- [Mechanism]: 将 Weak-to-Strong Generalization 范式扩展到交互式决策环境。弱模型生成动作轨迹；成功和失败轨迹均被组织为层次化"轨迹树"（trajectory trees）。MCTS 利用这些树结构轨迹优化强模型。P5：弱模型轨迹（经 MCTS 组织为树结构）→ 强模型 policy via 微调。轨迹树是 P5 输入数据的组织结构，不是独立的载体转化。理论分析提供方法有效性的形式化保证。

[Title]: Guiding VLM Agents with Process Rewards at Inference Time for GUI Navigation
- [Pathway]: Evaluator → Policy (P6) [test-time only]
- [Source Experience]: 基于 GUI 导航轨迹训练的过程奖励模型（process reward model）
- [Target Experience]: 在每个推理步骤受 process reward 引导的 VLM agent
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}
- [Utilization]: Process supervision 在推理时（test time）优化每步动作选择；结合轨迹反思和重试机制进一步增益
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 过程奖励模型在推理时为 VLM agent 提供步骤级监督，指导每步动作优化。这是 P6（Evaluator → Policy）在推理时执行而非通过权重更新的形式——RM 的信号塑造动作选择但不更新 policy 权重。属于轻量级 P6（test-time guidance variant）。配合轨迹反思和重试机制进一步提升任务成功率（静态环境 +3.4% 单步准确率，动态环境 +33% 任务成功率）。

[Title]: VerificAgent: Domain-Specific Memory Verification for Scalable Oversight
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Agent 交互轨迹中累积的未审核记忆（unvetted memories，可能编码不适当或不安全的启发式）
- [Target Experience]: 专家策划 + 人类事实核查后的验证记忆（frozen safety contract）
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {human}
- [Utilization]: 验证后的记忆充当冻结的安全契约，未来 agent 动作必须满足其约束；限制无声的策略漂移（silent policy drift）
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 三阶段验证：(1) 专家策划的领域知识种子；(2) 训练中迭代式基于轨迹的记忆增长；(3) 部署前的人类事后事实核查（post-hoc human fact-checking）以净化累积记忆。P1：来自轨迹的原始记忆 → 验证后可审计的指导。验证过程将潜在不安全的启发式转化为可靠、可解释的记忆。无需模型微调——记忆本身是对齐表面（alignment surface）。人类纠正一次高影响力错误后，验证记忆充当冻结安全契约。

[Title]: Reflexion: language agents with verbal reinforcement learning
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: 任务反馈信号（标量值或自由形式语言，外部或内部模拟）
- [Target Experience]: 维护在 episodic memory buffer 中的反思文本
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Episodic memory buffer 中的反思文本在后续试验中诱导更好的决策
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Agent 对任务反馈信号进行口头反思（verbally reflect），将反思文本维护在 episodic memory buffer 中。无权重更新——通过语言反馈而非参数更新来强化 agent。P1：原始任务反馈 + 轨迹 → 反思文本。奠基性 P1 工作，开创 verbal RL 范式。Reflexion 的"反思"载体是纯 Narrative。HumanEval pass@1 达 91%，超越 GPT-4 的 80%。

[Title]: BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: GUI agent 轨迹 + verifier/judger/reflector 组件产生的错误检测和恢复数据
- [Target Experience]: 具备回溯能力（backtracking capability）的 GUI agent，judgment rewards 增强性能
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 专为回溯机制设计的训练数据集用于训练 GUI agent 的错误恢复能力
- [Method]: ⟨SFT⟩
- [Mechanism]: Verifier、judger 和 reflector 组件检测错误并恢复；judgment rewards 施加于 agent 以增强性能。专为回溯机制设计的训练数据集考虑动作执行后的结果页面（outcome pages）。P5：含错误检测/恢复标注的轨迹 → policy via SFT。回溯机制本身是被训练进 policy 的行为能力（behavioral capability），而非独立载体。在 Mobile3M 和 Auto-UI 上均有提升。

[Title]: LAGEA: Language Guided Embodied Agents for Robotic Manipulation
- [Pathway]: Narrative → Narrative → Policy (P1 + P5)
- [Source Experience]: VLM 对机器人操作尝试的情节性、模式约束反思（episodic, schema-constrained reflections）
- [Target Experience]: 时间扎根的语言反馈 → 有界逐步塑形奖励 → RL 训练的 policy
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 语言反馈转化为有界逐步塑形奖励用于 RL；adaptive failure-aware coefficient 调节影响强度
- [Method]: ⟨LLM-extract⟩, ⟨RL: PPO⟩
- [Mechanism]: 阶段一（P1）：VLM 用简洁语言总结每次尝试，定位轨迹中的决定性时刻（decisive moments），在共享表征中对齐反馈与视觉状态。将目标进展和反馈一致性转化为有界逐步塑形奖励（bounded, step-wise shaping rewards）。Adaptive failure-aware coefficient 在探索需要方向时提供密集信号，在能力增长后优雅退场。阶段二（P5）：塑形奖励用于 RL 训练 policy。复合模式 §8.3：原始机器人轨迹 → 语言反馈 → 塑形奖励 → policy via RL。核心假设：语言，当被结构化并扎根于时间时，是教机器人从错误中反思的有效机制。

[Title]: A Self-Evolving Framework for Efficient Terminal Agents (TACO)
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Terminal agent 交互轨迹（含噪声终端观测）
- [Target Experience]: 结构化压缩规则（工作流自适应过滤模式）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 压缩规则应用于过滤低价值终端输出同时保留任务相关观测；提升 token 效率和任务表现
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Training-free、自进化压缩：从交互轨迹中自动发现、精炼和复用结构化压缩规则。工作流自适应过滤（workflow-adaptive filtering）去除低价值终端输出，同时保留任务关键观测。P1：原始终端观测序列 → 结构化压缩规则。自进化：新轨迹持续精炼压缩规则。跨 agent scaffold 和 backbone model 一致提升。

[Title]: REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: 多传感器机器人观测的分层摘要（multisensory observations → hierarchical summary）
- [Target Experience]: 失败解释（LLM 生成的失败推理）→ 基于语言的规划器修正
- [Source Modality]: [embodied]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 失败解释指导基于语言的规划器纠正失败并完成任务
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 基于多传感器观测生成的分层摘要查询 LLM 进行失败推理。失败解释随后指导基于语言的规划器纠正失败。P1：多传感器轨迹摘要 → 失败解释。解释到修正的步骤是规划修正（属 Narrative → Narrative 范畴），非独立载体转化。RoboFail 数据集系统评估该框架。

[Title]: CLIN: A Continually Learning Language Agent
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Agent 在 ScienceWorld 中的试错经验（多变环境和任务）
- [Target Experience]: 以因果抽象（causal abstractions）为中心的持久、动态文本记忆
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 记忆在每次试验后定期更新，agent 逐渐学习对新试验有用的知识，可迁移到新环境/任务
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 使用以因果抽象（causal abstractions）而非通用的"有用提示"为中心的持久动态文本记忆。每次试验后记忆定期更新，agent 逐渐积累有用知识。P1：原始试错经验 → 因果抽象文本记忆。持续改进无需参数更新。因果抽象焦点使 CLIN 区别于 Reflexion 等通用反思方法——知识以"因果机制"而非"启发式提示"形式组织。同一任务持续改进 +23pp，跨任务迁移 +4-13pp。

[Title]: LLM-Driven Self-Refinement for Embodied Drone Task Planning (SRDrone)
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: 无人机任务执行轨迹 + 连续状态评估
- [Target Experience]: 层次化行为树（Behavior Tree）修改（多级 BT 计划分析 + 约束策略空间）
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 经迭代自精炼优化的经验库；BT 计划修改使能结构化反思学习
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 连续状态评估方法论（continuous state evaluation）鲁棒准确地判定任务结果并提供解释性反馈。层次化 BT 修改模型将多级 BT 计划分析与约束策略空间结合，实现结构化反思学习。P2：原始无人机执行轨迹 → 结构化行为树修改（Schematic：形式化计划表征）。真实世界部署使用经迭代自精炼优化的经验库达到 96.25% SR。将 LLM 的通用推理智能与 embodied drone 的严格物理执行约束整合。

[Title]: Accurate Failure Prediction in Agents Does Not Imply Effective Failure Prevention
- [Pathway]: Out of Scope
- [Mechanism]: 该工作是对 LLM critic 干预效果的实证分析研究——发现 binary LLM critic 的高离线准确率（AUROC 0.94）不保证部署时有效干预，揭示 disruption-recovery tradeoff（干预可能恢复失败轨迹但也破坏本会成功的轨迹）。论文贡献在于提出 pre-deployment test（50 任务试点预估干预安全性），不涉及经验转化机制——没有从源端经验到目标端载体的转化过程。属于 agent evaluation/monitoring 方法论。归入 §3.2：该工作属于 critic intervention 的评估与安全部署研究，不构成 experience transformation。

[Title]: WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning
- [Pathway]: Annotation Failed
- [Mechanism]: Abstract 为空，无法识别源端/目标端经验形式及转化机制。论文标题暗示 self-evolving online curriculum RL 用于训练 web agents，可能涉及 Policy → Narrative → Policy (§8.1) 闭环，但缺乏 abstract 信息无法确认。

[Title]: APEX-EM: Non-Parametric Online Learning for Autonomous Agents via Structured Procedural-Episodic Experience Replay
- [Pathway]: Narrative → Schematic + Narrative (multi-target, §8.8)
- [Source Experience]: Agent 完整执行轨迹（程序化-情节化追踪：规划步骤、artifacts、迭代历史含错误分析、质量评分）
- [Target Experience]: 结构化经验表征（Schematic：plan DAG with structural signatures）+ 情节化摘要（Narrative：带标注的紧凑执行追踪）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 成功经验作为正例 ICL examples；失败经验作为带结构化错误标注的负例；混合检索结合语义搜索、结构签名匹配和 plan DAG traversal
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: PRGII 工作流（Plan-Retrieve-Generate-Iterate-Ingest）：编码完整程序化-情节化追踪——规划步骤、artifacts、迭代历史含错误分析、质量评分。双结果经验记忆（Dual-outcome Experience Memory）：P2（轨迹 → plan DAG with structural signatures，用于程序化检索）+ P1（轨迹 → 情节化摘要含错误标注）。混合检索结合语义搜索、结构签名匹配和 DAG traversal——使能在词法无重叠但操作结构类似的任务间进行跨领域迁移。消融实验揭示组件价值依赖任务类型：rich judge feedback 对代码生成可忽略，对结构化查询至关重要（+10.3pp）。超越 oracle-retrieval upper bound（89.6% vs. 84.9%）。

[Title]: Beyond Human Preferences: Exploring RL Trajectory Evaluation and Improvement through LLMs (LLM4PG)
- [Pathway]: Narrative → Evaluator → Policy (P4 + P6)
- [Source Experience]: 复杂游戏任务中带语言约束的 RL policy 轨迹
- [Target Experience]: LLM 驱动的自动偏好生成 → 重构的奖励函数 → 优化的条件策略
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: LLM 生成的奖励函数替代人类偏好标注，加速 RL 收敛
- [Method]: ⟨LLM-extract⟩, ⟨RL: PPO⟩
- [Mechanism]: 阶段一（P4）：LLM 抽象轨迹、排序偏好、重构奖励函数——替代 PbRL 中昂贵的人类偏好标注。阶段二（P6）：重构的奖励函数通过 RL 优化条件策略。复合模式 §8.2：轨迹 → LLM 重构的 RM → policy via RL。核心贡献：利用 LLM 自动化偏好生成，克服 PbRL 中人类偏好数据的瓶颈。在有复杂语言约束的任务上验证有效性。

[Title]: Closed-Loop Verbal Reinforcement Learning for Task-Level Robotic Planning
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: VLM critic 观测的机器人执行轨迹 + 物理机器人交互结果
- [Target Experience]: 结构化自然语言反馈 → 经迭代精炼的行为树（Behavior Trees）
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: VLM critic 反馈用于 LLM actor 迭代改进 BT；闭环适应执行失败
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 闭环 VRL：可执行行为树由 LLM actor 反复精炼，使用 VLM critic 观察物理机器人和执行轨迹后生成的结构化自然语言反馈。策略更新发生在符号规划层（symbolic planning level），无需基于梯度的优化。P2：原始执行观测 → 结构化 NL 反馈 → 精炼的行为树（Schematic：形式化计划表征）。BT 是形式化计划结构，归入 Schematic 而非 Narrative。闭环逻辑与 §8.1 Self-Reinforce 类似但完全在 Tokenized 层操作，无参数更新。

[Title]: ReUseIt: Synthesizing Reusable AI Agent Workflows for Web Automation
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Agent 在 web 任务中的成功和失败尝试
- [Target Experience]: 可复用 workflows，含执行守卫（execution guards：错误检测与修复能力）
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Workflows 使 agent 在最小用户干预下完成重复性任务；execution guards 帮助检测和修复错误
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 从 agent 的成功和失败尝试中自动合成可复用 workflows。Workflows 嵌入执行守卫（execution guards）——帮助 agent 检测和修复错误，同时向用户报告进展和问题。P2：原始 web 交互尝试 → 可复用 workflows with guards（Schematic：带嵌入式错误处理逻辑的过程性模板）。成功率从 24.2% 提升至 70.1%。用户研究验证易监控性和可理解性。

[Title]: ReGAL: Refactoring Programs to Discover Generalizable Abstractions
- [Pathway]: Schematic → Schematic (intra-Schematic refinement)
- [Source Experience]: 少量现有程序（code）
- [Target Experience]: 可复用函数库（通过代码重构发现的共享函数抽象）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 共享函数库使程序在多个领域更易预测；封装高频子程序和领域动态
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 无梯度方法：通过代码重构（code refactorization——重构代码而不改变执行输出）学习可复用函数库。迭代验证并通过执行精炼抽象。源端和目标端均为代码（Schematic），但转化提升了抽象层级和可复用性——属于 intra-Schematic 精炼。执行结果是 grounding 信号。这是一个边界案例：源和目标都是 Schematic Tokenized，不属于现有 7 条 Pathway 中的任何一条（P1 专指 Narrative → Narrative，此处的源和目标均为程序化/结构化代码）。可视为 P2 的逆过程或 P1 的 Schematic 类比。
> Note: 该论文是边界案例——源和目标均属 Schematic Tokenized（code → reusable function library）。不严格匹配任何已知 P 编号。最接近 P1 的"同层抽象"逻辑但载体类型不同。建议在 Survey 中作为 intra-Schematic abstraction 的特殊案例讨论。

[Title]: WorkflowGen: An Adaptive Workflow Generation Mechanism Driven by Trajectory Experience
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: 完整 agent 执行轨迹（错误指纹、最优工具映射、参数模式、执行路径、异常避免策略）
- [Target Experience]: 自适应 workflow 模板 + 三级路由（直接复用、重写式生成、全初始化）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 三级自适应路由根据与历史查询的语义相似度动态选择 workflow 复用策略；token 消耗减少 40%+
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 捕获完整轨迹并在节点和 workflow 两层提取可复用知识：错误指纹（error fingerprints）、最优工具映射、参数模式（parameter schemas）、执行路径、异常避免策略。闭环机制通过轨迹重写、经验更新和模板归纳仅在可变节点上执行轻量生成。P2：原始轨迹 → 结构化 workflow 模板（含参数模式和错误指纹，Schematic）。三级路由：直接复用、基于重写的生成、全初始化——根据语义相似度动态选择。

[Title]: Co-Evolving Agents: Learning from Failures as Hard Negatives
- [Pathway]: Policy → Narrative → Policy (§8.1 Self-Reinforce, dual-agent co-evolution)
- [Source Experience]: Target agent 自身轨迹 + failure agent 的轨迹（两者均为成功和失败）
- [Target Experience]: Failure agent 生成的 hard negative 失败轨迹 → 经偏好优化的 target agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Hard negatives（接近成功但仍失败的轨迹）锐化 target agent 偏好优化中的决策边界
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: 协同进化框架：target agent 与辅助 failure agent 共同改进。Failure agent 通过偏好优化从 target 和自身两者的失败轨迹中学习，生成 hard negatives——这些轨迹接近成功但仍失败，蕴含丰富的对比信号。阶段一（P7）：两个 agent 均生成轨迹。阶段二（P5）：轨迹（特别是来自 failure agent 的 hard negatives）通过 DPO 用于更新两个 policy。§8.1 模式扩展到双 agent 协同进化：失败被系统性地转化为结构化的有价学习信号，而非被简单丢弃。核心洞察：直接用原始失败不如将其转化为 hard negatives 有效。

[Title]: View-oriented Conversation Compiler for Agent Trace Analysis (VCC)
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: 原始 agent JSONL 日志（深度结构化：嵌套工具调用、CoT 推理块、子 agent 调用、上下文窗口压缩边界、harness 注入指令）
- [Target Experience]: 结构化视图族：full view（无损转录）、UI view（用户感知的交互重建）、adaptive view（结构保持投影）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: VCC 编译视图替代原始 JSONL 作为 reflector 输入格式；更高通过率，token 消耗减半到三分之二，更简洁的学习记忆
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 编译器（lex, parse, IR, lower, emit）将原始 agent JSONL 日志转化为结构化视图族。P1：原始 agent 日志 → 结构化、面向视图的表征。转化是格式层的（JSONL → 结构化视图），但保留语义完整性。核心洞察：消息格式是上下文工程的基础设施（infrastructure），而非偶发的实现选择——格式转化本身能显著提升下游分析质量。与典型 P1 的语义抽象不同，此处的"精炼"主要是表征格式的结构化重组。

[Title]: Evolvable Embodied Agent for Robotic Manipulation via Long Short-Term Reflection (EEAgent)
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: 机器人操作任务经验（成功与失败）
- [Target Experience]: 长短时反思 prompt（基于过往经验和新学教训动态精炼）
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 精炼的 prompts 用于 VLM-based 环境解释和策略规划
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: LSTRO（Long Short-Term Reflective Optimization）基于过往经验和新学教训动态精炼 prompts，促进持续自进化。P1：原始操作经验 → 精炼 prompts。"长短期"区分指积累反思的时间粒度——长期经验总结与近期教训融合。无权重更新——纯 Narrative → Narrative via prompt refinement。

[Title]: Self-Corrected Multimodal Large Language Model for End-to-End Robot Manipulation
- [Pathway]: Annotation Failed
- [Mechanism]: Abstract 为空，无法识别源端/目标端经验形式及转化机制。论文标题暗示 self-correction mechanism for end-to-end robot manipulation，可能涉及 P1（Narrative → Narrative via self-correction feedback loop）或 P5（corrected trajectories → policy via SFT），但缺乏 abstract 信息无法确认。

[Title]: Self-driven Grounding (SDG): LLM Agents with Automatical Language-aligned Skill Learning
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: LLM 提出并通过环境交互验证的子目标假设
- [Target Experience]: 泛化技能（language-aligned, executable skill library，扎根于环境）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 学习到的技能用于完成更复杂任务；技能从成功扎根的子目标中泛化而来
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: LLM 提出子目标假设以完成任务 → 通过环境交互验证假设可行性 → 成功验证的子目标指导提取泛化技能。这些技能可用于完成之前验证失败的更复杂任务。P2：环境交互验证的子目标 → 泛化的、语言对齐的可执行技能（Schematic）。性能与需要数百万示范的模仿学习方法相当。自动且渐进地将 LLM 扎根到环境中，无需为每个任务定制预定义行为 API。

[Title]: WorldGUI: An Interactive Benchmark for Desktop GUI Automation from Any Starting Point
- [Pathway]: Out of Scope
- [Mechanism]: 该工作贡献在于 benchmark 构建（WorldGUI benchmark，系统性构造非默认初始状态的 GUI 任务）和 agent framework 提议（WorldGUI-Agent with three critique stages）。核心是评估方法论和 agent 架构设计，不涉及经验转化机制——三个 critique stages 是推理时规划策略，不产生持久化的经验载体。没有从源端经验到目标端载体的转化过程。归入 §3.2：属于 benchmark + agent architecture，不构成 experience transformation。

[Title]: BLAZER: Bootstrapping LLM-based Manipulation Agents with Zero-Shot Data Generation
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: LLM planner 零样本生成的多样化操作任务示范（模拟器中验证为成功的示例）
- [Target Experience]: 经 SFT 微调的 LLM 规划策略（改进的规划能力）
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}
- [Utilization]: 成功示范用于 SFT 微调 LLM planner；技能从模拟直接迁移到基于传感器的操作
- [Method]: ⟨SFT⟩
- [Mechanism]: 利用 LLM planner 的零样本能力自动生成多样化操作任务示范。成功示例（通过模拟器状态访问验证）用于 SFT 微调 LLM 规划能力。P5：零样本生成示范 → policy via SFT。与 §8.1 自强化闭环的区别：BLAZER 是一次性数据生成 + SFT，无迭代反馈循环。直接 sim-to-real 迁移，无需真实世界数据收集。

[Title]: A Real-to-Sim-to-Real Approach to Robotic Manipulation with VLM-Generated Iterative Keypoint Rewards (IKER)
- [Pathway]: Narrative → Evaluator → Policy (P4 + P6)
- [Source Experience]: RGB-D 观测 + 自由形式语言指令
- [Target Experience]: VLM 生成的、基于关键点的 Python 奖励函数（IKER）→ 经 RL 训练的操作策略
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}
- [Utilization]: IKER 奖励函数在仿真中训练 RL 策略，部署到真实世界（real-to-sim-to-real loop）
- [Method]: ⟨LLM-extract⟩, ⟨RL: PPO⟩
- [Mechanism]: 阶段一（P4）：VLM 从 RGB-D 观测和自由形式语言指令生成视觉扎根的 Python 奖励函数（IKER）。在场景中采样关键点，奖励函数基于关键点之间的空间关系进行条件化，利用常识先验实现精确 SE(3) 控制。阶段二（P6）：IKER 奖励函数用于在仿真中训练 RL 策略（real-to-sim-to-real）。核心创新：IKER 是动态可迭代精炼的任务规范（dynamic task specification），而非静态奖励函数——支持多步任务执行、自发错误恢复和即时策略调整。

[Title]: PAACE: A Plan-Aware Automated Agent Context Engineering Framework
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: 多步 agent 工作流（规划、工具使用、反思、与外部知识系统交互）
- [Target Experience]: 计划感知的压缩上下文（通过 next-k-task relevance modeling、plan-structure analysis、instruction co-refinement、function-preserving compression）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: 压缩上下文替代膨胀的原始上下文；PAACE-FT 蒸馏压缩器保持 97% teacher 性能，推理成本降低超一个数量级
- [Method]: ⟨LLM-extract⟩, ⟨SFT⟩
- [Mechanism]: PAACE-Syn 大规模生成合成 agent 工作流，标注步骤级压缩监督信号（来自成功 teacher demonstration）。PAACE-FT 训练蒸馏后的计划感知压缩器。P1：agent 工作流上下文 → 计划感知压缩上下文。计划感知使压缩区别于通用摘要——压缩尊重多步计划结构而不破坏任务逻辑。蒸馏到 PAACE-FT 属于模型压缩技术，非经验转化。AppWorld 上准确性超越所有 baseline 同时降低峰值上下文和累积依赖。

[Title]: Self-Improving Loops for Visual Robotic Planning (SILVR)
- [Pathway]: Policy → Narrative → Policy (§8.1 Self-Reinforce)
- [Source Experience]: In-domain 视频模型自产出的视频轨迹（作为视觉规划器）
- [Target Experience]: 迭代更新的视频模型（改进的视觉规划性能）
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 自产出轨迹用于迭代更新视频模型；多轮迭代后性能持续提升
- [Method]: ⟨SFT⟩
- [Mechanism]: In-domain 视频模型在自产出轨迹上迭代更新自身，稳步提升指定任务的规划性能。阶段一（P7）：视频模型生成视觉规划轨迹。阶段二（P5）：自产出轨迹通过 SFT 更新视频模型权重。无需人类提供的 ground-truth 奖励函数或专家级示范即可稳健运行。§8.1 Self-Reinforce 应用于视觉规划领域：视频模型同时充当 planner（生成轨迹）和训练数据生成器。与 VLAW 类似但在视觉规划领域，且无分离的 world model 组件——视频模型本身就是 planner。

## New Tags Introduced
- ⟨RL: DAPO⟩ — Direct Alignment Policy Optimization，针对工具使用场景的 RL 优化目标，优化 stepwise strategy（Reflect → Call → Final）；首次出现：「Failure Makes the Agent Stronger」
- ⟨RL: GSPO⟩ — Group Sampling Policy Optimization，用于多轮工具交互中优化步骤级策略的 RL 目标；首次出现：「Failure Makes the Agent Stronger」
- ⟨RL: TRPO⟩ — Trajectory-aware Relative Policy Optimization，一种针对 GUI agent online RL 的变体（非传统 Trust Region Policy Optimization）；首次出现：「Mobile-Agent-v3 / GUI-Owl」

## Annotation Failures
- 「WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning」（block #89）—— Abstract 为空，无法识别源端/目标端经验形式及转化机制。标题暗示可能涉及 Policy → Narrative → Policy (§8.1) 闭环。
- 「Self-Corrected Multimodal Large Language Model for End-to-End Robot Manipulation」（block #99）—— Abstract 为空，无法识别源端/目标端经验形式及转化机制。标题暗示 self-correction mechanism，具体路径无法确认。

## Parser Errors
（无——parse_papers.py 成功解析全部 105 篇，errors 列表为空。）
