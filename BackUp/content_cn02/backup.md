### 4.4 Evolution-based Evaluator Internalization

Evolution-based evaluator internalization 将 evaluator construction 从一次性训练扩展为随 agent 经验分布变化而持续更新的动态过程。在静态 evaluator training 中，reward model、verifier 或 critic 在固定数据集上训练一次后用于下游决策。但当 agent policy 持续改进、探索新状态或开始利用旧 reward signal 的漏洞时，原有 evaluator 可能变得 stale——训练分布不再匹配当前 policy 的行为分布，反馈也无法覆盖新出现的错误模式。

这类方法关注的核心问题是 evaluator staleness。随着 agent 经验流不断增长，evaluator 需要根据新轨迹、新错误类型、新 policy 行为、hard negative examples、self-play interactions、online curriculum、human / AI feedback 或 execution outcomes 进行刷新。Evaluator 可与 policy 共同演化，也可在 generator-verifier loop 中交替更新，还可在发现新 failure mode 后通过 data flywheel 进行增量训练。在这种设置下，evaluator 不再是被动的静态模块，而成为 self-improving agent system 的组成部分。

Evolution-based internalization 可以产生 outcome-level、process-level 或 diagnostic-feedback evaluator，因此它不是与前三类完全同构的”输出形式”类别，而是描述一种动态训练机制。之所以将其作为独立家族，是因为核心贡献在于 evaluator 的生命周期：如何刷新 evaluator，如何选择新经验数据，如何控制 evaluator-policy drift，以及如何避免 feedback loop 不断强化自身错误。

这类方法自然构成 P4 与 Composite pathway 的边界。当论文的主要贡献是 evaluator 本身的构建、刷新或自适应机制时，可在 P4 中讨论；当 evaluator training、policy optimization、data generation 和 planning 被紧密耦合为闭环自进化系统时，更适合归入 Composite。许多近期 agent-learning system 都处于这一边界区域，说明 evaluator internalization 正在从静态 reward modeling 走向 adaptive critic construction。

论文：
- SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from Experience
- WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning
- MagicGUI-RMS: A Multi-Agent Reward Model System for Self-Evolving GUI Agents via Automated Feedback Reflux
- Scaling Autonomous Agents via Automatic Reward Modeling And Planning
- SPARK: Stepwise Process-Aware Rewards for Reference-Free Reinforcement Learning
- RLAC: Reinforcement Learning with Adversarial Critic for Free-Form Generation Tasks
- LLaVA-Critic-R1: Your Critic Model is Secretly a Strong Policy Model
- SPC: Evolving Self-Play Critic via Adversarial Games for LLM Reasoning
- No More Stale Feedback: Co-Evolving Critics for Open-World Agent Learning
- RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning
- UI-Genie: A Self-Improving Approach for Iteratively Boosting MLLM-based Mobile GUI Agents
- GAIA: A Data Flywheel System for Training GUI Test-Time Scaling Critic Models
- Hybrid Reward Normalization for Process-supervised Non-verifiable Agentic Tasks

### 小结

四类方法的主要区别在于训练后 evaluator 向 agent 提供的监督信息形式及其生命周期。Outcome-supervised evaluator 提供完整行为的全局判断；Process-supervised evaluator 提供中间步骤或局部动作的过程判断；Diagnostic-feedback evaluator 提供更丰富的语义解释、诊断或修正建议；Evolution-based evaluator 随 agent 经验分布变化而持续更新。它们共同展示了 tokenized agent experience 如何被转化为参数化评估能力，支撑 search、verification、reinforcement learning、self-correction 和 safe execution。


### Evolution-based Policy Internalization

Evolution-based Policy Internalization 通过持续的经验生成、筛选、验证、重标注、训练与再生成构成闭环，使 policy 不断利用自身或环境产生的新经验进行更新。与前三类相比，核心不在于单一训练目标，而在于组织一个 self-improving experience pipeline。

典型闭环表现为：当前 policy 与环境交互产生新 trajectories；系统基于环境反馈、执行结果或规则 verifier 对这些轨迹进行筛选、修正、重标注或重组；处理后的经验用于下一轮 policy training；更新后的 policy 继续生成新经验。某些方法还会引入 self-play、world model、synthetic environment 或自动 curriculum，使 agent 持续接触更复杂或更具挑战性的任务。

基本思想是：agent 不只是被动消费已有经验，而是主动参与新经验的生成，通过反复内化形成能力增长的 data flywheel。在传统 imitation 或 reward optimization 中，经验通常来自固定数据集、人工示范或一次性 rollout；Evolution-based 方法中，policy 的当前版本影响下一轮经验分布，经验筛选和再训练又进一步改变 policy，形成动态闭环。

从 transformation pathway 角度看，这类方法通常已超出单步 P5，更接近 Composite pathway，其内部往往包含多个连续的经验转化步骤：原始 rollout 先被过滤为高质量训练集再用于 SFT；失败轨迹先被分析和修正再构造成 preference pairs；world model 先从真实轨迹中学习环境动态再生成 imagined trajectories 用于 policy training；synthetic environment 先被自动生成并验证再为 agent 提供新的交互经验。尽管如此，这些闭环系统的最终目标通常仍是将 tokenized experience 内化进 policy weights，因此可作为 P5 的高级扩展讨论。

Evolution-based 方法的常见机制包括：rollout-filter-train loop，当前 policy 生成 trajectories，系统通过环境反馈、规则 verifier 或任务成功率筛选高质量经验用于下一轮训练；failure-driven self-improvement，失败轨迹不被简单丢弃而是被诊断、修正、重标注或转化为偏好对；self-play experience generation，agent 或其副本生成越来越难的任务、bug、goal 或 environment challenge 以推动 policy 学习更复杂策略；synthetic environment generation，系统自动构建可验证环境以扩大可交互、可训练的经验空间；world-model co-evolution，world model 从真实交互中学习环境反馈并生成 imagined rollouts，policy 利用模拟经验训练后又产生新轨迹改进 world model；large-scale data flywheel，数据生成、执行验证、训练更新和再生成被系统化整合为持续循环。

该类方法的优势是扩展潜力强。对于 web search、computer use、GUI automation、software engineering 和 embodied tasks 等开放或长程任务，静态训练数据往往难以覆盖真实任务分布。Evolution-based 方法通过持续生成和内化新经验，有可能突破固定数据集限制，支持 agent 能力的逐轮增长。

但这类方法也最容易产生系统性风险。自生成数据可能导致 distribution drift，使 policy 越来越适应自身生成的经验而偏离真实任务分布；错误经验可能在闭环中被反复放大，形成 self-training error accumulation；world model 或 synthetic environment 可能引入 hallucinated dynamics，导致 policy 学到不可迁移的策略；reward loophole 或 evaluation contamination 可能在多轮自改进中被放大；这类系统通常需要大量 rollout、环境实例、验证器和训练资源，计算与工程成本显著高于单步 SFT 或 RL。

本文归入该类的判定标准：核心贡献是 self-improvement loop、data flywheel、self-play、world-model co-evolution、synthetic environment generation 或其他持续经验生成与内化机制；若论文只是常规的”先 SFT 再 RL”而未将闭环经验演化作为核心贡献，则应根据主要训练目标归入 Imitation-based 或 Reward-based 方法。

论文：
- EvoCUA: Evolving Computer Use Agents via Learning from Scalable Synthetic Experience
- WebDancer: Towards Autonomous Information Seeking Agency
- EvolveSearch: An Iterative Self-Evolving Search Agent
- UI-TARS-2 Technical Report: Advancing GUI Agent with Multi-Turn Reinforcement Learning
- GUI-GENESIS: Automated Synthesis of Efficient Environments with Verifiable Rewards for GUI Agent Post-Training
- Toward Training Superintelligent Software Agents through Self-Play SWE-RL
- ComputerRL: Scaling End-to-End Online Reinforcement Learning for Computer Use Agents
- DynaWeb: Model-Based Reinforcement Learning of Web Agents
- WebEvolver: Enhancing Web Agent Self-Improvement with Coevolving World Model

### Boundary Cases and Pathway Distinctions

P5 与其他 transformation pathways 存在若干易混淆的边界，需要单独澄清。

P5 与 P6 的核心区别在于监督信号是否经过参数化 evaluator。若 policy 更新信号直接来自环境、执行器、unit tests、规则函数、ground-truth match 或人工 per-trajectory 标注，则属于 Tokenized-to-Policy internalization。若 reward、preference 或 reasoning feedback 主要由 trained reward model、process reward model、fine-tuned judge、prompted LLM-as-judge 或 VLM-based evaluator 产生，则监督信号已被参数化评估器中介，更接近 Evaluator-to-Policy transformation，或至少应为 P5/P6 mixed pipeline，不应纳入纯 P5 主类。

P5 与 Composite pathway 的区别在于论文的核心贡献是否是多步 transformation chain。许多 Evolution-based 方法最终包含 policy training，但主要贡献可能是 world model construction、synthetic environment generation、experience relabeling、data flywheel 或 self-play curriculum。若这些衔接机制本身构成 headline contribution，则更适合在 Composite pathway 中主讲，在 P5 中仅作为相关子步骤引用。

P5 还需与普通 instruction tuning、chat preference alignment 或单轮 conversation optimization 区分。P5 要求方法处于 LLM-based agent setting 中，即模型需要进行序贯决策并产生异构动作——工具调用、代码执行、GUI 操作、web navigation、search action、embodied control 或多轮环境交互。若一篇工作只是普通单轮问答、chat-style preference alignment 或缺少环境交互的对话优化，即使更新了 policy weights，也不应被视为 P5。

P5 关注的是 agent experience 如何从显式 tokenized trajectories 转化为参数化决策能力。Imitation-based 方法通过模仿成功经验完成内化；Reward-based 方法通过可验证环境反馈优化 policy；Preference-based 方法通过轨迹间相对优劣关系学习行为偏好；Evolution-based 方法通过持续经验生成与再训练形成自改进闭环。四类方法共同构成了当前 LLM-based agents 中 Tokenized-to-Policy Experience Transformation 的主要技术图景。

### Evaluator–Policy Co-Evolution

Evaluator–Policy Co-Evolution 指 evaluator 与 policy 在同一学习闭环中随 agent 新经验持续更新、刷新、重训或共同演化的复合方法。前三类方法通常默认 evaluator 在 policy update 期间相对固定，或至少 evaluator 的构建不是主要贡献；而在这一类中，evaluator 本身的动态变化就是方法核心——它随 policy 产生的新 trajectories、失败模式、分布漂移和环境反馈不断调整自身评价能力。

这类方法包含一个循环结构：当前 policy 与环境交互产生新 trajectories；evaluator 对这些 trajectories 进行评分、比较、诊断或筛选；policy 根据 evaluator feedback 更新；更新后的 policy 产生新经验分布；evaluator 又基于新经验被刷新、重训、校准或扩展。evaluator 可以是 reward model、critic、judge、PRM、discriminator、self-rewarding model 或 mixture of evaluators。更新方式多样：有的在 on-policy samples 上重新训练 reward model，有的交替训练 discriminator 与 generator，有的让 critic 随 agent 新失败模式持续进化，还有的让同一模型同时扮演 policy 和 evaluator 形成 self-rewarding loop。

核心动机是缓解 static evaluator 在长期 policy improvement 中的失效。当 policy 被反复优化时，它会逐渐偏离 reward model 或 judge 最初见过的数据分布，固定 evaluator 可能出现 reward overestimation、blind spot、stale feedback 或被 policy exploited 的漏洞。让 evaluator 随 policy-generated experience 更新，系统可在一定程度上保持 feedback 与当前 policy distribution 的匹配，使 evaluator 能继续识别新的错误模式、reward hacking 策略或任务能力边界。

具体模式包括：reward model refresh，在 policy 新生成的数据上持续校准或更新 RM 以减少 distribution shift；critic-policy co-evolution，critic 随 actor 变化不断学习新的 value、advantage 或 failure patterns 并继续指导 actor；self-rewarding loop，模型自身生成候选答案、评价候选答案、构造偏好数据并用这些偏好继续更新自身；search-evaluate-distill pipeline，evaluator 先指导搜索或筛选高质量 trajectories，再将经验蒸馏回 policy——若搜索、评价和训练反复迭代，也属于 co-evolutionary pipeline；environment–policy–reward joint optimization，环境生成、任务分布、reward model 和 policy 都在同一系统中动态变化。

Evaluator–Policy Co-Evolution 适合开放世界、长周期和持续学习场景。在这些场景中，agent 的能力、任务分布和失败模式都会随训练变化，静态 evaluator 很难长期保持有效。共同演化让 evaluator 不断吸收新的 agent experience，并把更新后的评价标准再次传回 policy，形成更强的经验循环。这对 web agent、GUI agent、tool-use agent、self-improving agent、open-world embodied agent 和 multi-agent 系统尤其重要，因为这些任务中的环境状态、工具组合和错误模式高度动态。

但稳定性风险也更复杂。evaluator 和 policy 同时变化，系统可能出现 feedback drift、self-confirmation bias、reward model collapse、critic overfitting 或 evaluator-policy collusion。在 self-rewarding setting 中，模型可能逐渐强化自身偏见而非接近真实任务目标。若 evaluator 的更新缺乏外部锚点——human preference、environment verification、held-out benchmark、rule-based constraint 或 independent judge——co-evolution 可能放大错误评价。这类方法通常需要额外的稳定化机制：frozen reference evaluator、periodic human audit、ensemble judges、conservative update、KL constraint、external validation set 或 uncertainty-aware reward modeling。

严格来说，Evaluator–Policy Co-Evolution 并非与前三类完全同维度的单步 P6 方法，而是 P6 的复合扩展。前三类描述 evaluator feedback 以何种产物形态进入 policy；本类描述 evaluator 本身是否在经验循环中持续变化。当论文仅使用固定 PRM 或 LLM judge 给 policy 提供过程反馈时，归入 Process Feedback-to-Policy Transfer；当核心贡献是 PRM、judge 或 critic 随 policy 新经验不断刷新时，归入 Evaluator–Policy Co-Evolution。同时包含 evaluator construction、feedback generation、policy update 和 evaluator refresh 的方法，视为 composite pipeline，在 P6 章节中作为 evaluator-to-policy transfer 的动态扩展讨论。

论文：
- No More Stale Feedback: Co-Evolving Critics for Open-World Agent Learning
- RLAnything: Forge Environment, Policy, and Reward Model in Completely Dynamic RL System
- Fine-Tuning Language Models with Reward Learning on Policy
- Black-Box On-Policy Distillation of Large Language Models
- Process-based Self-Rewarding Language Models
- SRR-Judge: Step-Level Rating and Refinement for Enhancing Search-Integrated Reasoning in Search Agents
- VARP: Reinforcement Learning from Vision-Language Model Feedback with Agent Regularized Preferences
- Iterative Tool Usage Exploration for Multimodal Agents via Step-wise Preference Tuning
- OpenClaw-RL: Train Any Agent Simply by Talking
- EVPO: Explained Variance Policy Optimization for Adaptive Critic Utilization in LLM Post-Training（边界论文；若强调 critic 随 policy training 的 adaptive utilization）

