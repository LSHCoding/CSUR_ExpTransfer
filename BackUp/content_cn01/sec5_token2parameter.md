

## Tokenized-to-Evaluator Experience Transformation

第四类转化路径是 Tokenized-to-Evaluator Experience Transformation，即将 tokenized agent experience 内化为参数化评估器。这里的 tokenized experience 可以包括 agent trajectory、reasoning trace、tool-use log、action history、preference pair、execution outcome、failure annotation、diagnostic feedback 等。通过训练，这些离散经验中的评价语义被写入 evaluator 参数中，形成可复用的评估能力。训练后的 evaluator 可以表现为 outcome reward model、process reward model、verifier、critic、judge、value model、failure detector 或 diagnostic feedback model。

这一类方法与 prompted LLM-as-a-judge 有本质区别。Prompted judge 只是在推理时通过 prompt 激发现有模型的评估能力，而 P4 路径要求 evaluator 的参数发生训练更新。也就是说，评价能力不是仅被调用出来，而是被经验数据显式内化进模型参数。

我们按照训练后 evaluator 向 agent 提供的监督信息形式来组织这一类方法。Outcome-supervised evaluator internalization 学习完整输出或完整轨迹上的全局评估信号；Process-supervised evaluator internalization 学习中间推理步骤、动作前缀或局部决策上的过程性评估信号；Diagnostic-feedback evaluator internalization 进一步超越 scalar 或 scalarizable reward，内化 critique、error diagnosis、rationale 或 repair suggestion 等更丰富的语义反馈；Evolution-based evaluator internalization 则描述 evaluator 随 agent 经验分布变化而持续更新的动态扩展，因此构成单步 evaluator construction 与 composite self-improving agent pipeline 之间的边界区域。

### Outcome-supervised Evaluator Internalization

Outcome-supervised evaluator internalization 指的是训练 evaluator 对完整输出、完整轨迹或完整 episode 给出全局判断。这类方法的监督信号被分配在 outcome level，例如任务是否完成、最终答案是否正确、两个完整 response 哪一个更好，或者一条完整 trajectory 在某个 reward 或 quality criterion 下是否更优。训练后的 evaluator 通常将一个完整候选行为映射为 global scalar 或 scalarizable signal，例如 reward score、success probability、correctness probability、pass/fail label、ranking score 或 pairwise preference。

这一类方法最接近传统意义上的 reward modeling。它的主要优势是 outcome-level label 通常比 dense process label 更容易获得。对于具有明确最终答案、显式成功标准或 human / AI preference comparison 的任务，outcome supervision 可以直接对齐最终任务目标。因此，这类 evaluator 常被用于 best-of-\(N\) selection、trajectory reranking、rejection sampling，或者作为 reinforcement learning 中的 reward model。当中间步骤难以标注，或者最终结果是最可靠的监督信号时，outcome-supervised evaluator 尤其有吸引力。

不过，outcome-supervised evaluator 的主要局限是 credit assignment 较弱。一条失败轨迹中可能包含许多有价值的中间决策，而一条成功轨迹中也可能包含偶然有效但并不稳健的推理或动作。将整条轨迹压缩为一个整体标签，容易掩盖到底哪些动作应该被强化、哪些动作应该被修正。在 web navigation、GUI automation、software engineering 和 embodied manipulation 等 long-horizon agent setting 中，这一问题会更加明显，因为早期错误可能在很多步骤之后才显现出来。因此，outcome-supervised evaluator 更适合作为粗粒度过滤器、终局 reward provider 或候选轨迹选择器；当任务需要细粒度过程指导时，它往往是不充分的。

论文：
- S2J: Bridging the Gap Between Solving and Judging Ability in Generative Reward Models
- J4R: Learning to Judge with Equivalent Initial State Group Relative Policy Optimization
- RL-VLM-F: Reinforcement Learning from Vision Language Foundation Model Feedback
- Video-Language Critic: Transferable Reward Functions for Language-Conditioned Robotics
- Large Reward Models: Generalizable Online Robot Reward Generation with Vision-Language Models
- RoboReward: General-Purpose Vision-Language Reward Models for Robotics
- Generative Reward Models
- VLP: Vision-Language Preference Learning for Embodied Manipulation
- LIV: Language-Image Representations and Rewards for Robotic Control

### 4.2 Process-supervised Evaluator Internalization

Process-supervised evaluator internalization 指的是训练 evaluator 对中间推理步骤、动作前缀或单个 agent decision 提供局部监督。与 outcome-supervised evaluator 不同，这类方法不是给完整 trajectory 分配一个整体得分，而是在 step、state、prefix、tool call、code edit、GUI action 或 web-navigation decision 等局部位置上学习评价信号。训练后的 evaluator 可以表现为 process reward model、step-level verifier、progress model、action-value model、Q-value ranker 或 advantage-style critic。

这类方法的核心动机是：agent 的失败通常不是在最后一步突然发生，而是在一系列局部错误中逐渐累积。在多步推理中，一个无效的中间推断可能会使最终答案失效，即使最后一步看起来是合理的。在 web 或 GUI agent 中，点击错误元素、发出错误 search query、忽略用户约束，都可能使后续轨迹偏离目标。在 code agent 中，一个早期错误 edit 可能直到测试失败时才暴露出来，并且很难回溯原因。Process-supervised evaluator 试图解决这种 credit assignment 问题：它不仅判断最终 outcome 是否成功，还判断每一个中间决策是否正确、是否有希望、是否推动了任务进展。

这类方法的过程监督信号可以通过多种方式获得。一些方法依赖 human step annotation，由人工标注每个 reasoning step 的正确性或有用性。另一些方法通过 rollout、Monte Carlo completion、temporal-difference estimate、execution result 或 alternative prefix comparison 自动推导 process label。对于 agentic tasks，过程监督也可以来自 state change、task progress、test execution 或 action-level preference。尽管标签来源不同，这类 evaluator 的共同输出形式通常是 local scalar 或 scalarizable signal，例如 step correctness、process reward、progress score、promise score、Q-value、advantage estimate 或 step-level preference。

相比 outcome-supervised evaluator，process-supervised evaluator 能提供更密集、更可操作的反馈。它们尤其适用于 test-time search、tree expansion、trajectory pruning、step reranking，以及需要 dense reward 的 reinforcement learning。然而，process supervision 也带来新的困难。首先，step-level label 的获取成本更高；其次，自动构造的 process label 往往存在噪声；再次，局部正确并不必然意味着全局成功。一个步骤可能局部合理但策略上无用，也可能暂时看起来不优但对后续任务完成是必要的。因此，这一类方法的关键问题是：如何定义既具有局部信息量、又与最终任务成功保持一致的 process signal。

论文：
- StepWiser: Stepwise Generative Judges for Wiser Reasoning
- Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision
- SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents
- Process Reward Model with Q-Value Rankings
- Let's Verify Step by Step
- GUI-Shepherd: Reliable Process Reward and Verification for Long-Sequence GUI Tasks
- Web-Shepherd: Advancing PRMs for Reinforcing Web Agents
- AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress
- WebArbiter: A Principle-Guided Reasoning Process Reward Model for Web Agents
- Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning
- Improve Mathematical Reasoning in Language Models by Automated Process Supervision
- IntentScore: Intent-Conditioned Action Evaluation for Computer-Use Agents
- ProgRM: Build Better GUI Agents with Progress Rewards
- Generative Verifiers: Reward Modeling as Next-Token Prediction
- Better Process Supervision with Bi-directional Rewarding Signals


### 4.3 Diagnostic-feedback Evaluator Internalization

Diagnostic-feedback evaluator internalization 指的是训练 evaluator 产生更丰富的语义反馈，而不仅仅是 scalar 或 scalarizable score。这类 evaluator 的目标输出可以包括 natural-language critique、error diagnosis、failure explanation、verification rationale、risk analysis、policy-violation explanation 或 repair suggestion。它们不仅判断 agent 行为是好是坏，还进一步解释为什么有问题，以及应该如何修正。

这一类方法体现了 evaluator 从 scoring function 向 feedback generator 的转变。在复杂 agent setting 中，单纯的 reward score 往往不足以支持有效的自我修正。一个分数可以告诉 agent 某个动作不好，却未必能指出违反了什么约束、基于了什么错误假设、忽略了哪些观察，或者应该考虑什么替代动作。Diagnostic-feedback evaluator 通过内化更具解释性和行动指导性的反馈，弥补了 scalar reward 的信息不足。

例如，在 reasoning task 中，critique model 可以指出某个推理步骤为何无效；在 code task 中，feedback model 可以说明错误修改导致了什么问题；在 robotic manipulation 中，failure detector 可以基于视觉观察解释操作失败的原因；在 GUI 或 web automation 中，critic 可以指出当前动作与用户意图、屏幕状态或任务约束之间的不一致；在安全敏感场景中，risk evaluator 可以在执行前解释某个动作为什么违反 policy 或存在风险。

Diagnostic-feedback evaluator 的输出通常是文本形式，但其输入可以是文本、视觉、多模态或 embodied trajectory。它的主要优势是信息量高、可解释性强，适合用于 reflection、debugging、repair、human oversight 和 constraint-aware decision making。它也可以与 scalar reward 结合，例如同时输出 verdict 和 rationale，或者同时给出 score 和 explanation。

但这一类方法也面临更复杂的评估问题。与 scalar label 相比，diagnostic feedback 的质量更难度量。一个 critique 可能语言上很合理，却在事实层面错误、不完整，或者没有抓住真正的失败原因。因此，这类方法通常需要额外机制来控制反馈质量，例如 execution checking、human validation、self-consistency filtering，或者利用下游 repair performance 作为间接训练信号。

需要注意的是，并不是所有 failure detector 或 risk classifier 都应归入这一类。如果某个模型只输出 \(0/1\) failure probability 或 scalar risk score，它更接近 outcome-supervised 或 process-supervised evaluator。只有当论文的核心贡献强调 failure reason、diagnosis、critique、rationale 或 correction guidance 时，才更适合归入 Diagnostic-feedback Evaluator Internalization。

论文：
- I-FailSense: Towards General Robotic Failure Detection with Vision-Language Models
- Self-Refining Vision Language Model for Robotic Failure Detection and Reasoning
- Towards Policy-Compliant Agents: Learning Efficient Guardrails For Policy Violation Detection
- AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation
- SAFE: Multitask Failure Detection for Vision-Language-Action Models
- DeepCritic: Deliberate Critique with Large Language Models
- Teaching Language Models to Critique via Reinforcement Learning
- Enhancing LLM Reasoning via Critique Models with Test-Time and Training-Time Supervision
- Enhancing Robotic Manipulation with AI Feedback from Multimodal Large Language Models
- OS-Oracle: A Comprehensive Framework for Cross-Platform GUI Critic Models
- Look Before You Leap: A GUI-Critic-R1 Model for Pre-Operative Error Diagnosis in GUI Automation
- CORA: Conformal Risk-Controlled Agents for Safeguarded Mobile GUI Automation
- Self-Generated Critiques Boost Reward Modeling for Language Models
- SOLE-R1: Video-Language Reasoning as the Sole Reward for On-Robot Reinforcement Learning
- RL4F: Generating Natural Language Feedback with Reinforcement Learning for Repairing Model Outputs


### 4.4 Evolution-based Evaluator Internalization

Evolution-based evaluator internalization 将 evaluator construction 从一次性训练扩展为随 agent 经验分布变化而持续更新的动态过程。在静态 evaluator training 中，reward model、verifier 或 critic 通常在固定数据集上训练一次，然后被用于下游决策。然而，当 agent policy 持续改进、探索新状态，或者开始利用旧 reward signal 的漏洞时，原有 evaluator 可能会变得 stale。它的训练分布不再匹配当前 policy 的行为分布，反馈也无法覆盖新出现的错误模式。

这一类方法关注的核心问题是 evaluator staleness。随着 agent 经验流不断增长，evaluator 需要根据新轨迹、新错误类型、新 policy 行为、hard negative examples、self-play interactions、online curriculum、human / AI feedback 或 execution outcomes 进行刷新。Evaluator 可以与 policy 共同演化，也可以在 generator-verifier loop 中交替更新，还可以在发现新的 failure mode 后通过 data flywheel 进行增量训练。在这种设置下，evaluator 不再是一个被动的静态模块，而成为 self-improving agent system 的组成部分。

Evolution-based internalization 可以产生 outcome-level、process-level 或 diagnostic-feedback evaluator。因此，它并不是与前三类完全同构的“输出形式”类别，而是描述一种动态训练机制。我们仍然将其作为独立家族，是因为这类方法的核心贡献在于 evaluator 的生命周期：如何刷新 evaluator，如何选择新的经验数据，如何控制 evaluator-policy drift，以及如何避免 feedback loop 不断强化自身错误。

这一类方法自然构成 P4 与 Composite pathway 的边界。当论文的主要贡献是 evaluator 本身的构建、刷新或自适应机制时，可以在 P4 中讨论；当 evaluator training、policy optimization、data generation 和 planning 被紧密耦合为一个闭环自进化系统时，则更适合归入 Composite。事实上，许多近期 agent-learning system 都处于这一边界区域，这说明 evaluator internalization 正在从静态 reward modeling 走向 adaptive critic construction。

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

这四类方法的主要区别在于训练后 evaluator 向 agent 提供的监督信息形式及其生命周期。Outcome-supervised evaluator 提供完整行为上的全局判断；Process-supervised evaluator 提供中间步骤或局部动作上的过程判断；Diagnostic-feedback evaluator 提供更丰富的语义解释、诊断或修正建议；Evolution-based evaluator 则随着 agent 经验分布变化而持续更新。它们共同展示了 tokenized agent experience 如何被转化为参数化评估能力，并进一步支持 search、verification、reinforcement learning、self-correction 和 safe execution。



## Tokenized-to-Policy Experience Transformation

Tokenized-to-Policy Experience Transformation 指将离散化的 agent experience 转化为 policy / actor parameters 的一类方法。其源经验通常表现为自然语言轨迹、工具调用记录、代码编辑历史、GUI 操作序列、web browsing traces、reasoning chains、环境执行反馈等 tokenized artifacts；其目标则是将这些经验内化到模型参数中，使模型在后续任务中不必显式检索、拼接或重放原始经验，也能够表现出更强的序贯决策能力。

从经验转化的角度看，这一路径的核心不是简单地“训练一个更强的模型”，而是回答如下问题：agent 在交互过程中形成的离散经验，如何被组织为训练信号，并进一步改变 policy 的参数化决策能力？ 与 Narrative-to-Narrative 或 Narrative-to-Schematic transformation 不同，P5 的目标载体不再是可读的文本、规则、程序或工作流，而是模型内部的 policy weights。因此，这一路径在可解释性、可编辑性与推理效率之间呈现出明显权衡：经验一旦被内化进参数，后续调用成本较低，且不受上下文窗口限制；但同时，经验的显式可追踪性与局部可修改性也会下降。

本文将 P5 进一步划分为四类：Imitation-based Policy Internalization、Reward-based Policy Internalization、Preference-based Policy Internalization 与 Evolution-based Policy Internalization。这四类方法分别对应四种不同的经验内化逻辑：模仿高质量轨迹、利用可验证奖励、构造轨迹偏好，以及通过闭环机制持续生成并内化新经验。


### Imitation-based Policy Internalization

Imitation-based Policy Internalization 指将高质量 agent trajectories 直接作为监督示范，通过 behavior cloning、supervised fine-tuning 或 rejection-sampled fine-tuning 等方式训练 policy。其基本假设是：如果一组轨迹已经体现了有效的任务解决行为，那么模型可以通过模仿这些轨迹中的动作选择、推理模式、工具调用习惯或 GUI 操作序列，将相应经验内化进参数。

在这类方法中，环境反馈或任务结果通常不直接作为优化目标，而是用于筛选、清洗、重构或标注训练轨迹。例如，系统可以从多条候选 trajectories 中保留成功完成任务的轨迹，也可以根据执行结果过滤无效工具调用、错误 GUI 操作或失败代码修改。换言之，feedback 在此类方法中主要扮演 data selection 或 data construction 的角色，而不是直接参与 policy optimization。

从经验转化的角度看，Imitation-based 方法将 agent experience 视为一种可模仿的行为模板。轨迹中的 action sequence、reasoning trace、tool-use pattern、workflow structure 或 interface operation 被作为“应该学习的行为样例”。经过训练后，模型不再需要在 prompt 中看到这些示范，就能够在类似上下文中复现相应的行为模式。这种方法尤其适合 agent 的 cold-start training，因为它能够快速教会模型任务格式、动作空间、输出协议和基本交互流程。

该类方法的经验来源可以包括人工示范、teacher model 生成轨迹、自动探索得到的成功轨迹，以及由搜索、回滚、反思或重构机制生成的 reasoning traces。对于 web agent、GUI agent、tool-use agent 和 code agent 等任务，Imitation-based internalization 往往是构建可用 policy 的第一步：模型先通过模仿高质量轨迹获得基本能力，再进一步通过 reward-based 或 preference-based 方法提升性能。

然而，这类方法的能力上限通常受示范轨迹质量与覆盖范围限制。如果训练数据只包含有限场景下的成功路径，模型可能学到表层格式或局部启发式，而难以主动探索新的任务解决策略。此外，rejection-sampled fine-tuning 虽然能够提升样本质量，但也可能丢弃失败轨迹中具有局部价值的经验。因此，在长程、开放或高不确定性的 agent 任务中，单纯依赖 imitation 往往不足以支撑持续能力增长。

本文将一篇工作归入该类的判定标准是：其核心 policy update 主要依赖 SFT / behavior cloning / imitation objective；环境反馈主要用于筛选或构造训练样本，而不是直接进入 policy-gradient 或 reward optimization 目标。

论文：
- Large Language Models Can Self-Improve At Web Agent Tasks
- AndroidGen: Building an Android Language Agent under Data Scarcity
- AppVLM: A Lightweight Vision Language Model for Online App Control
- Explorer: Scaling Exploration-driven Web Trajectory Synthesis for Multimodal Web Agents
- Go-Browse: Training Web Agents with Structured Exploration
- WebCoT: Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback
- AgentTuning: Enabling Generalized Agent Abilities for LLMs
- MagicGUI: A Foundational Mobile GUI Agent with Scalable Data Pipeline and Reinforcement Fine-tuning
- AutoWebGLM: A Large Language Model-based Web Navigating Agent

### Reward-based Policy Internalization

Reward-based Policy Internalization 指 agent 通过与环境交互产生 trajectories，并利用非参数化、可验证的反馈信号直接优化 policy。典型反馈包括任务成功率、unit test 结果、代码执行反馈、SQL execution correctness、ground-truth answer match、工具调用结果、GUI 任务完成状态、机器人操作成功与否等。

与 Imitation-based 方法相比，Reward-based 方法不再只是学习“成功轨迹中做了什么”，而是进一步学习“哪些行为在环境中真正有效”。这使其能够利用 agent experience loop 的完整结构：context 和 action 构成 agent 的决策过程，observation 和 feedback 则为 policy update 提供外部依据。特别是在软件工程、数据库查询、工具调用、web navigation、GUI automation 与 embodied control 等任务中，环境往往能够提供相对明确的成功或失败信号，因此 reward-based internalization 成为 P5 中最直接、也最典型的一类方法。

这类方法通常采用 PPO、GRPO、REINFORCE、RLVR 或其 agent-specific variants。对于 LLM-based agents 而言，动作空间往往并非传统强化学习中的固定离散动作或连续控制量，而是包括自然语言 reasoning、tool call、代码片段、GUI 坐标、API 调用、search query、inter-agent message 等异构动作。因此，reward-based 方法通常需要对传统 RL 算法进行适配，使其能够处理长上下文、多轮交互、结构化动作与复杂环境反馈。

Reward-based internalization 的主要优势在于能力上限较高。由于 policy 可以通过试错发现超出示范数据的新策略，这类方法有潜力突破 imitation learning 的数据覆盖限制。对于具有可验证目标的任务，reward signal 还可以帮助模型避免单纯模仿中存在的伪相关或错误示范，从而更直接地优化任务成功率。

但该类方法也面临若干关键挑战。首先，许多 agent 任务的 reward 极其稀疏，系统往往只有最终成功或失败信号，而缺少中间步骤监督。其次，长程任务中的 credit assignment 十分困难，最终 reward 很难准确归因到具体 turn、step 或 token。再次，online rollout 成本较高，尤其是在 GUI、robotics、web browsing 与 software engineering 等环境中，执行一次完整 trajectory 可能需要真实环境交互、代码构建、页面加载或仿真运行。最后，即便 reward 来自可验证环境，仍可能存在 reward hacking 或 proxy exploitation 的风险，即 agent 学到利用评测漏洞而非真正解决任务。

因此，Reward-based Policy Internalization 内部形成了若干重要技术方向。第一类是 outcome-level reward optimization，即直接基于最终任务成败更新 policy。第二类是 turn-level 或 step-level credit assignment，即将最终反馈分配到中间动作，以缓解长程任务中的稀疏奖励问题。第三类是 entropy- 或 uncertainty-shaped optimization，即通过不确定性、信息增益或熵调节探索行为，避免 policy 过早收敛或陷入无效探索。第四类是 replay- 或 off-policy-enhanced optimization，即复用历史经验、成功 transitions 或 semi-online trajectories，以提升样本效率。第五类是 domain-specific reward design，例如针对 SQL、SWE、GUI、tool-use 或 VLA 任务设计更细粒度、更可靠的可验证反馈。

本文将一篇工作归入该类的判定标准是：其核心训练信号来自非参数化环境反馈、执行反馈、规则化 verifier 或 ground truth，并且该反馈直接参与 policy optimization。若 reward 或 preference 主要来自 trained reward model、process reward model、fine-tuned judge、prompted LLM-as-judge 或 VLM-based evaluator，则不属于纯 P5，而应视为 evaluator-mediated policy optimization 或 P6 相关方法。

论文：
- Training Long-Context, Multi-Turn Software Engineering Agents with Reinforcement Learning
- GUI-R1: A Generalist R1-Style Vision-Language Action Model For GUI Agents
- Improving Vision-Language-Action Model with Online Reinforcement Learning
- AgentCPM-GUI: Building Mobile-Use Agents with Reinforcement Fine-Tuning
- SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning
- Language Models are Few-Shot Butlers
- Fine-Tuning Large Vision-Language Models as Decision-Making Agents via Reinforcement Learning
- WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning
- AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning
- Agentic Reinforced Policy Optimization
- AgentRL: Scaling Agentic Reinforcement Learning with a Multi-Turn, Multi-Task Framework
- Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards
- Information Gain-based Policy Optimization: A Simple and Effective Approach for Multi-Turn LLM Agents
- UI-S1: Advancing GUI Automation via Semi-online Reinforcement Learning
- EPO: Entropy-regularized Policy Optimization for LLM Agents Reinforcement Learning
- SQL-Trail: Multi-Turn Reinforcement Learning with Interleaved Feedback for Text-to-SQL
- LongNav-R1: Horizon-Adaptive Multi-Turn RL for Long-Horizon VLA Navigation
- Agentic Entropy-Balanced Policy Optimization
- On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning
- Large Language Models as Generalizable Policies for Embodied Tasks
- Multi-Agent Tool-Integrated Policy Optimization
- Harnessing Uncertainty: Entropy-Modulated Policy Gradients for Long-Horizon LLM Agents
- ARPO: End-to-End Policy Optimization for GUI Agents with Experience Replay
- Group-in-Group Policy Optimization for LLM Agent Training
- ToolRL: Reward is All Tool Learning Needs
- MobileGUI-RL: Advancing Mobile GUI Agent through Reinforcement Learning in Online Environment
- Generalization in Online Reinforcement Learning for Mobile Agents
- Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Credit Assignment
- TGRPO: Fine-tuning Vision-Language-Action Model via Trajectory-wise Group Relative Policy Optimization
- SQL-ASTRA: Alleviating Sparse Feedback in Agentic SQL via Column-Set Matching and Trajectory Aggregation
- ToolOmni: Enabling Open-World Tool Use via Agentic learning with Proactive Retrieval and Grounded Execution
- Reinforcement Learning for Long-Horizon Interactive LLM Agents
- Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs
- Grounding Large Language Models in Interactive Environments with Online Reinforcement Learning
- Q-SFT: Q-Learning for Language Models via Supervised Fine-Tuning
- Succeed or Learn Slowly: Sample Efficient Off-Policy Reinforcement Learning for Mobile App Control
- RLVMR: Reinforcement Learning with Verifiable Meta-Reasoning Rewards for Robust Long-Horizon Agents


### Preference-based Policy Internalization

Preference-based Policy Internalization 指从 agent experience 中构造轨迹间的相对偏好关系，并通过 DPO、DMPO、IPO、KTO、ORPO 或其他 trajectory-pair optimization 方法更新 policy。其中，相对更优的轨迹可以来自成功任务、通过验证的执行结果、人工标注、修正后的轨迹或更高效的操作路径；相对较差的轨迹则可以来自失败尝试、错误工具调用、无效搜索、错误 GUI 点击或未通过测试的代码修改。

这一类方法的基本动机是：在许多 agent 场景中，精确设计每一步 reward 很困难，但比较两条轨迹哪一条更好却相对容易。例如，在 web navigation 中，一条轨迹成功找到目标信息，另一条轨迹陷入无关页面；在 GUI automation 中，一条轨迹到达目标界面，另一条轨迹点击了错误控件；在 tool-use 中，一条轨迹调用了正确工具并得到有效结果，另一条轨迹产生了 hallucinated tool call；在 software engineering 中，一条轨迹通过了测试，另一条轨迹引入了新的错误。这些相对比较都可以形成 preference signal。

从经验转化角度看，Preference-based 方法的重要特点是能够显式利用失败经验。Imitation-based 方法通常只保留成功轨迹，而将失败轨迹过滤掉；Reward-based 方法则需要将失败轨迹转化为数值 reward 或 advantage。Preference-based 方法提供了另一种选择：失败轨迹可以作为 negative sample，与成功轨迹、修正轨迹或更高效轨迹配对，从而帮助 policy 学习哪些行为应该避免。

Preference-based internalization 通常适合以下几类场景。第一，任务反馈天然表现为 success / failure 对比，而非连续数值 reward。第二，存在大量失败或低质量 trajectories，直接丢弃会浪费经验。第三，可以通过 verifier、execution result、unit test、task completion 或人工标注自动构造 preferred / dispreferred pairs。第四，agent 的错误模式具有结构性，例如错误工具调用、无效搜索、错误 GUI 点击、冗余步骤或不 grounded 的推理。通过偏好优化，模型不仅学习成功行为，也学习避免失败行为。

与 Reward-based 方法相比，Preference-based 方法通常具有更稳定的 supervised-style 训练形式，不需要直接估计高方差 policy gradient，也不要求精确设计 step-level reward。与 Imitation-based 方法相比，它能够利用负样本和轨迹间对比，因此更适合处理失败经验、修正经验和探索经验。

不过，该类方法也有自身限制。首先，preference pairs 的构造质量直接影响训练效果。如果 preferred / dispreferred 的判定过于粗糙，模型可能学到表层差异而非真正的策略改进。其次，trajectory-level preference 仍然可能缺乏细粒度 credit assignment，模型知道哪条轨迹更好，却未必知道其中哪些步骤真正导致了差异。再次，如果偏好标签来自 LLM-as-judge 或 trained reward model，则该方法的监督信号已经经过参数化 evaluator，中间发生了 Evaluator-to-Policy transformation，不能再被视为纯粹的 P5。

本文将一篇工作归入该类的判定标准是：其核心 policy update objective 是 preference optimization 或 trajectory-pair optimization；偏好标签主要来自非参数化信号，例如执行成功、任务完成、测试通过、人工 per-trajectory 标注或规则化比较，而不是参数化 evaluator。

论文：
- Direct Multi-Turn Preference Optimization for Language Agents
- Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents
- UI-Voyager: A Self-Evolving GUI Agent Learning via Failed Experience


### Evolution-based Policy Internalization

Evolution-based Policy Internalization 指通过持续的经验生成、筛选、验证、重标注、训练与再生成构成闭环，使 policy 不断利用自身或环境产生的新经验进行更新。与前三类方法相比，该类方法的核心不在于单一训练目标，而在于组织一个 self-improving experience pipeline。

典型闭环可以表现为：当前 policy 先与环境交互产生新 trajectories；系统随后基于环境反馈、执行结果或规则 verifier 对这些轨迹进行筛选、修正、重标注或重组；处理后的经验再被用于下一轮 policy training；更新后的 policy 又继续生成新的经验。对于某些方法，闭环中还会引入 self-play、world model、synthetic environment 或自动 curriculum，使 agent 能够持续接触更复杂或更具挑战性的任务。

这类方法的基本思想是：agent 不只是被动消费已有经验，而是主动参与新经验的生成，并通过反复内化这些经验形成能力增长的 data flywheel。在传统 imitation 或 reward optimization 中，经验通常来自固定数据集、人工示范或一次性 rollout；而在 Evolution-based 方法中，policy 的当前版本会影响下一轮经验的分布，经验筛选和再训练又会进一步改变 policy，从而形成动态闭环。

从 transformation pathway 的角度看，这类方法通常已经超出单步 P5，而更接近 Composite pathway。原因在于，其内部往往包含多个连续的经验转化步骤。例如，原始 rollout 可能先被过滤为高质量训练集，再用于 SFT；失败轨迹可能先被分析和修正，再构造成 preference pairs；world model 可能先从真实轨迹中学习环境动态，再生成 imagined trajectories 用于 policy training；synthetic environment 可能先被自动生成并验证，再为 agent 提供新的交互经验。尽管如此，由于这些闭环系统的最终目标通常仍然是将 tokenized experience 内化进 policy weights，因此它们可以作为 P5 的高级扩展进行讨论。

Evolution-based 方法的常见机制包括以下几类。第一，rollout-filter-train loop，即当前 policy 生成 trajectories，系统通过环境反馈、规则 verifier 或任务成功率筛选高质量经验，再将其用于下一轮训练。第二，failure-driven self-improvement，即失败轨迹不被简单丢弃，而是被诊断、修正、重标注或转化为偏好对。第三，self-play experience generation，即 agent 或其副本生成越来越难的任务、bug、goal 或 environment challenge，从而推动 policy 学习更复杂策略。第四，synthetic environment generation，即系统自动构建可验证环境，以扩大 agent 可交互、可训练的经验空间。第五，world-model co-evolution，即 world model 从真实交互中学习环境反馈，并生成 imagined rollouts；policy 利用这些模拟经验训练后，又产生新的轨迹改进 world model。第六，large-scale data flywheel，即数据生成、执行验证、训练更新和再生成被系统化整合为持续循环。

该类方法的优势是扩展潜力强。对于 web search、computer use、GUI automation、software engineering 和 embodied tasks 等开放或长程任务，静态训练数据往往难以覆盖真实任务分布。Evolution-based 方法通过持续生成和内化新经验，有可能突破固定数据集限制，并支持 agent 能力的逐轮增长。

但这类方法也最容易产生系统性风险。首先，自生成数据可能导致 distribution drift，使 policy 越来越适应自身生成的经验，而偏离真实任务分布。其次，错误经验可能在闭环中被反复放大，形成 self-training error accumulation。第三，world model 或 synthetic environment 可能引入 hallucinated dynamics，导致 policy 学到不可迁移的策略。第四，reward loophole 或 evaluation contamination 可能在多轮自改进中被放大。第五，这类系统通常需要大量 rollout、环境实例、验证器和训练资源，因此计算与工程成本显著高于单步 SFT 或 RL。

本文将一篇工作归入该类的判定标准是：其核心贡献是 self-improvement loop、data flywheel、self-play、world-model co-evolution、synthetic environment generation 或其他持续经验生成与内化机制；如果论文只是常规的“先 SFT 再 RL”，但没有将闭环经验演化作为核心贡献，则不应归入该类，而应根据其主要训练目标归入 Imitation-based 或 Reward-based 方法。

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

P5 与其他 transformation pathways 存在若干容易混淆的边界。为了保持 taxonomy 的一致性，有必要单独讨论这些边界案例。

首先，P5 与 P6 的核心区别在于监督信号是否经过参数化 evaluator。若 policy 的更新信号直接来自环境、执行器、unit tests、规则函数、ground-truth match 或人工 per-trajectory 标注，则该方法可以视为 Tokenized-to-Policy internalization。相反，若 reward、preference 或 reasoning feedback 主要由 trained reward model、process reward model、fine-tuned judge、prompted LLM-as-judge 或 VLM-based evaluator 产生，则监督信号已经被参数化评估器中介。这类方法更接近 Evaluator-to-Policy transformation，或者至少应被视为 P5/P6 mixed pipeline，而不应纳入纯 P5 主类。

其次，P5 与 Composite pathway 的区别在于论文的核心贡献是否是多步 transformation chain。许多 Evolution-based 方法虽然最终包含 policy training，但其主要贡献可能是 world model construction、synthetic environment generation、experience relabeling、data flywheel 或 self-play curriculum。如果这些衔接机制本身构成论文的 headline contribution，则更适合在 Composite pathway 中主讲，在 P5 中仅作为相关子步骤引用。

最后，P5 还需要与普通 instruction tuning、chat preference alignment 或单轮 conversation optimization 区分开来。P5 要求方法处在 LLM-based agent setting 中，即模型需要进行序贯决策，并产生异构动作，例如工具调用、代码执行、GUI 操作、web navigation、search action、embodied control 或多轮环境交互。如果一篇工作只是普通单轮问答、chat-style preference alignment 或缺少环境交互的对话优化，即使它也更新了 policy weights，也不应被视为 P5。

综上，P5 关注的是 agent experience 如何从显式 tokenized trajectories 转化为参数化决策能力。Imitation-based 方法通过模仿成功经验完成内化；Reward-based 方法通过可验证环境反馈优化 policy；Preference-based 方法通过轨迹间相对优劣关系学习行为偏好；Evolution-based 方法则通过持续经验生成与再训练形成自改进闭环。四类方法共同构成了当前 LLM-based agents 中 Tokenized-to-Policy Experience Transformation 的主要技术图景。
