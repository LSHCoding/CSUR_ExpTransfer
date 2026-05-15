

## Tokenized-to-Evaluator Experience Transformation

Tokenized-to-Evaluator Experience Transformation 将 tokenized agent experience 内化为参数化评估器。tokenized experience 包括 agent trajectory、reasoning trace、tool-use log、action history、preference pair、execution outcome、failure annotation、diagnostic feedback 等。通过训练，这些离散经验中的评价语义被写入 evaluator 参数，形成可复用的评估能力。训练后的 evaluator 表现为 outcome reward model、process reward model、verifier、critic、judge、value model、failure detector 或 diagnostic feedback model。

这类方法与 prompted LLM-as-a-judge 有本质区别。Prompted judge 仅在推理时通过 prompt 激发现有模型的评估能力，而 P4 要求 evaluator 的参数发生训练更新——评价能力被经验数据显式内化进模型参数。

本文按训练后 evaluator 向 agent 提供的监督信息形式组织方法。Outcome-supervised evaluator internalization 学习完整输出或完整轨迹上的全局评估信号；Process-supervised evaluator internalization 学习中间推理步骤、动作前缀或局部决策上的过程性评估信号；Diagnostic-feedback evaluator internalization 超越 scalar 或 scalarizable reward，内化 critique、error diagnosis、rationale 或 repair suggestion 等更丰富的语义反馈；Evolution-based evaluator internalization 描述 evaluator 随 agent 经验分布变化而持续更新的动态扩展，构成单步 evaluator construction 与 composite self-improving agent pipeline 之间的边界区域。

### Outcome-supervised Evaluator Internalization

Outcome-supervised evaluator internalization 训练 evaluator 对完整输出、完整轨迹或完整 episode 给出全局判断。监督信号被分配在 outcome level：任务是否完成、最终答案是否正确、两个完整 response 哪一个更好，或一条完整 trajectory 在某个 reward 或 quality criterion 下是否更优。训练后的 evaluator 将一个完整候选行为映射为 global scalar 或 scalarizable signal——reward score、success probability、correctness probability、pass/fail label、ranking score 或 pairwise preference。

这类方法最接近传统 reward modeling，主要优势是 outcome-level label 通常比 dense process label 更容易获得。对于具有明确最终答案、显式成功标准或 human / AI preference comparison 的任务，outcome supervision 可直接对齐最终任务目标。这类 evaluator 常被用于 best-of-\(N\) selection、trajectory reranking、rejection sampling，或作为 reinforcement learning 中的 reward model。当中间步骤难以标注或最终结果是最可靠的监督信号时，outcome-supervised evaluator 尤其有吸引力。

主要局限是 credit assignment 较弱。一条失败轨迹可能包含许多有价值的中间决策，一条成功轨迹也可能包含偶然有效但并不稳健的推理或动作。将整条轨迹压缩为单一标签，容易掩盖哪些动作应该被强化、哪些应该被修正。在 web navigation、GUI automation、software engineering 和 embodied manipulation 等 long-horizon agent setting 中，这一问题更加突出——早期错误可能在很多步骤之后才显现。outcome-supervised evaluator 更适合作为粗粒度过滤器、终局 reward provider 或候选轨迹选择器；当任务需要细粒度过程指导时，它往往不充分。

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
- Vision-Language Models as Success Detectors
- WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning
- Video-Based Reward Modeling for Computer-Use Agents

```
## Outcome-supervised Evaluator Internalization

Outcome-supervised evaluator internalization 的共同特征是：训练信号被放在完整输出、完整轨迹或完整 episode 的结果层面，而不是显式标注中间步骤。被内化的经验可以是 response pair preference、trajectory-level success or failure、rollout video 的完成度，或环境返回的最终成败信号；训练后的 evaluator 则将这些离散 outcome semantics 压缩为可复用的全局评估能力，用于 response selection、trajectory reranking、reward provision 或 online RL 中的终局监督 [Mah24b, Sun25l, Xu25i, Qi24]。这一谱系的核心优势在于标签相对容易获得，且能直接对齐最终任务目标；但其局限同样明确，即 evaluator 往往只能判断“整体是否更好”，却难以解释究竟是哪一步导致了成功或失败。

一类工作首先出现在对完整回答进行全局比较的 generative judge 与 reward model 中。Generative Reward Models 将 reward modeling 重写为 next-token generation，让 evaluator 对完整 response pair 直接生成 preference verdict，并进一步通过 CoT 自举把能够导向正确 verdict 的 reasoning pattern 内化为参数 [Mah24b]。S2J 则进一步指出 generative reward model 存在 solving ability 与 judging ability 的落差，因此要求 evaluator 在判断前先自行求解，再用 solving reward 与 judging reward 的联合 RL 目标更新参数，把“会解题”与“会判优劣”这两种 outcome-level 语义同时写入 judge 权重 [Sun25l]。J4R 沿着同一路径训练 pairwise judge，但强调 response order 等等价初始状态上的一致性，通过 EIS-GRPO 用最终 judgment correctness 驱动 RL，使 evaluator 学到更稳定、更少位置偏差的全局比较能力 [Xu25i]。这组方法的共同点是：它们都将 tokenized preference data 直接压缩为对完整候选输出进行 ranking 的参数化 evaluator，而不依赖逐步过程监督。

另一类工作把 outcome supervision 建立在 agent 与环境交互后的整条轨迹或最终状态上，尤其集中于 web、computer-use 与一般数字代理场景。WebRL 在整体自进化 RL 框架中训练了 outcome-supervised reward model，使 evaluator 根据用户指令、历史动作与最终网页状态判断整条 web trajectory 是否完成任务，从而把环境返回的终局成败信号内化为 online RL 可用的粗粒度 reward provider [Qi24]。在 computer-use 场景中，Video-Based Reward Modeling for Computer-Use Agents 进一步去除了对 agent 内部 reasoning 和 action log 的依赖，直接训练 Execution Video Reward Model 仅根据 user instruction 与 execution video sequence 判断完整 trajectory 的 success or failure，并将 execution outcome 中的全局完成语义写入多模态 evaluator [Son26d]。与这一路径相近，Vision-Language Models as Success Detectors 将 success detection 表述为 SuccessVQA，通过微调 Flamingo 让 evaluator 对图像或短视频片段加任务描述输出 yes or no，从而以内化的方式学习 episode-level success semantics，而不是局部动作质量 [Du23]。这类方法表明，在具有明确终局判据的 interactive environment 中，outcome-supervised evaluator 往往首先扮演 coarse filter、terminal verifier 或 sparse reward model 的角色。

第三类工作主要出现在 embodied manipulation 与 robot control 中，其共同策略是把整段视频、整条 rollout 或 trajectory pair 的全局优劣关系转化为 vision-language evaluator。RL-VLM-F 并不直接把 prompt-only VLM 作为 reward 使用，而是先让 foundation model 对 observation image pair 产生偏好标签，再训练参数化 reward model 来吸收这些 pairwise visual preferences，使离散反馈转化为可复用的环境内奖励 [Wan24l]。VLP 则学习 trajectory-wise vision-language preference model，通过 ITP、ILP 与 IVP 三类 language-conditioned trajectory preference，把 expert、medium 与 random rollouts 的全局排序关系内化为 evaluator [Liu25w]。更进一步地，Video-Language Critic 从 video-caption 对齐与成功轨迹的时间排序中学习一个对 partial video history 和 language instruction 输出标量分数的 critic；虽然它利用了隐式时序结构，但 supervision 仍主要来自 trajectory-level outcome 与成功序关系，而非人工过程标签 [Ala24]。LIV 代表了更弱标签但仍属结果导向的一端：它从 action-free video 与 language annotation 中联合学习 language-image representation 与 reward-like value function，把 toward-goal trajectory 的时序结构和最终 outcome 对齐信号压缩进统一表示空间 [Ma23d]。最近的 RoboReward 与 Large Reward Models 则进一步扩大了 evaluator 的数据与任务覆盖范围：前者通过 counterfactual relabeling 和 negative clipping，把原本以成功 rollout 为主的数据自动扩展为带 1 到 5 progress score 的 episodic reward dataset，进而训练通用 vision-language reward model [Lee26b]；后者则利用大规模无标签视频中的时间单调性，学习 temporal contrastive reward、absolute progress reward 与 task completion reward，把 rollout 中隐含的完成度语义写入通用 VLM reward generator [Wu26e]。整体上，这些 embodied 工作说明 outcome supervision 虽然较粗，但当最终状态、视频完成度或 trajectory-level preference 本身足够可靠时，仍然可以支撑出泛化性很强的 evaluator family。

```


### Process-supervised Evaluator Internalization

Process-supervised evaluator internalization 训练 evaluator 对中间推理步骤、动作前缀或单个 agent decision 提供局部监督。与 outcome-supervised evaluator 不同，这类方法不是在完整 trajectory 上分配整体得分，而是在 step、state、prefix、tool call、code edit、GUI action 或 web-navigation decision 等局部位置学习评价信号。训练后的 evaluator 表现为 process reward model、step-level verifier、progress model、action-value model、Q-value ranker 或 advantage-style critic。

这类方法的核心动机是：agent 失败通常不是最后一步的突然事件，而是一系列局部错误的累积。多步推理中，一个无效的中间推断可能使最终答案失效，即使最后一步看起来合理；web 或 GUI agent 中，点击错误元素、发出错误 search query、忽略用户约束，都可能使后续轨迹偏离目标；code agent 中，早期错误 edit 可能直到测试失败才暴露，且难以回溯原因。Process-supervised evaluator 试图解决 credit assignment 问题：它不仅判断最终 outcome 是否成功，还判断每个中间决策是否正确、是否有希望、是否推动任务进展。

过程监督信号可通过多种方式获得。一些方法依赖 human step annotation，人工标注每个 reasoning step 的正确性或有用性；另一些通过 rollout、Monte Carlo completion、temporal-difference estimate、execution result 或 alternative prefix comparison 自动推导 process label。对于 agentic tasks，过程监督也可来自 state change、task progress、test execution 或 action-level preference。尽管标签来源不同，共同的输出形式通常是 local scalar 或 scalarizable signal：step correctness、process reward、progress score、promise score、Q-value、advantage estimate 或 step-level preference。

相比 outcome-supervised evaluator，process-supervised evaluator 提供更密集、更可操作的反馈，尤其适用于 test-time search、tree expansion、trajectory pruning、step reranking 以及需要 dense reward 的 reinforcement learning。但 process supervision 也带来新困难：step-level label 获取成本更高，自动构造的 process label 往往存在噪声，且局部正确并不必然意味着全局成功——一个步骤可能局部合理但策略上无用，也可能暂时看起来不优但对后续任务完成是必要的。这类方法的关键问题是如何定义既具有局部信息量、又与最终任务成功保持一致的 process signal。

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


- Let’s Verify Step by Step
- Improve Mathematical Reasoning in Language Models by Automated Process Supervision
- Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning
- Process Reward Model with Q-Value Rankings
- Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision
- Better Process Supervision with Bi-directional Rewarding Signals
- AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress
- ProgRM: Build Better GUI Agents with Progress Rewards
- Building Autonomous GUI Navigation via Agentic-Q Estimation and Step-Wise Policy Optimization
- GUI-Shepherd: Reliable Process Reward and Verification for Long-Sequence GUI Tasks
- Advancing Mobile GUI Agents: A Verifier-Driven Approach to Practical Deployment
- IntentScore: Intent-Conditioned Action Evaluation for Computer-Use Agents
- GAIA: A Data Flywheel System for Training GUI Test-Time Scaling Critic Models
- SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents

```
## Process-supervised evaluator internalization

Process-supervised evaluator internalization 的核心，不在于 evaluator 被实现成何种架构，而在于它是否把离散经验中的局部评价语义写入参数，使模型能够对中间步骤、动作前缀或单步决策输出可标量化的过程信号。与只在完整轨迹末端判断成败的 outcome evaluator 不同，这一路线试图把 credit assignment 前移到推理或交互过程内部：一个步骤是否正确、一个前缀是否仍有希望、一个动作是否真正推动任务进展，都被转化为 evaluator 可学习的局部监督目标。[Lig23] 最早系统地确立了这一范式，用人工 step annotation 训练 PRM 对每个 reasoning step 给出 positive、negative、neutral 判断，证明过程监督比只看最终答案更能支持 test-time reranking。随后，一系列工作开始围绕“如何自动构造局部标签”展开扩展：OmegaPRM [Luo24] 通过 rollout 与 binary search 自动定位 first error，并把前缀的可完成性转成 soft process label；Rewarding Progress [Set24] 则进一步指出，局部监督不应只刻画 step correctness，还应刻画一步对未来成功概率的实际增益，因此把目标改写为 step-level advantage。沿着这条思路，PQM [Li24m] 将 PRM 的训练目标从独立分类改为 Q-value ranking，强调正确推理应随着过程推进而逐步抬高状态价值，而错误步骤应触发显著价值断裂；PathFinder-PRM [Pal25] 和 BiRM [Che25s] 则分别把 process supervision 推向更细的误差结构与更强的前瞻建模，前者先区分 math error 与 consistency error 再汇总为最终 reward judgment，后者联合学习 reward 与 value 两个头，使 evaluator 同时编码“当前这一步是否好”与“当前前缀未来是否还有希望”。

这类 reasoning PRM 的重要性，不仅在于它们改进了数学推理搜索，更在于它们为 agentic setting 提供了一套可迁移的 supervision 设计语言：局部信号可以是 correctness，也可以是 progress、promise、advantage 或 Q-value，而标签既可来自人工逐步标注，也可由 Monte Carlo completion、temporal-difference estimate、prefix comparison 或 outcome back-propagation 自动导出。[Xi25b] 明确把这一思想推广到多步 agent 决策，提出 AgentPRM，用 Promise 和 Progress 分别建模 action-value 与 advantage，并通过 TD 与 GAE 从 rollout 中自动估计 step-wise pseudo-label，使 evaluator 能够服务于 beam search、Best-of-N 和 PPO。类似地，ProgRM [Zha25z] 不再直接判断动作对错，而是学习每一步对 GUI 任务完成度的 progress value，并通过 LCS-based self-annotation 从成功轨迹中自动抽取关键步骤与相对进度；Building Autonomous GUI Navigation via Agentic-Q Estimation and Step-Wise Policy Optimization [Wan26s] 则采用更直接的 value 建模，把最终成功信号向前传播到 state-thought-action 三元组，训练 step-wise 的 success-probability evaluator，再把它作为代理 reward 用于 step-wise policy optimization。相比 reasoning 场景中较纯粹的“解题步骤正确性”，这些 agentic 方法更强调局部决策对长期任务完成的贡献，因此 process signal 的语义也从 correctness 进一步转向 progress 与 future utility。

当过程监督进入真实的交互环境后，研究重点开始从“是否需要 step label”转向“如何从环境行为中稳定提炼出高密度局部信号”。在 GUI 与 computer-use 场景中，GUI-Shepherd [Che25h] 训练 step-level binary PRM，对 state-action 对直接预测 positive 或 negative judgment，并把该 evaluator 同时用于 candidate action reranking 与在线 RL 的 dense reward；Advancing Mobile GUI Agents via a verifier-driven approach [Dai25] 进一步采用 pairwise process preference 训练 generative verifier，让模型在每一步把正确动作与若干错误动作拉开分数差距。IntentScore [Che26s] 则走向轻量化设计：它不依赖大型生成式 judge，而是训练 intent-conditioned action evaluator，对 state-action-intent 三元组输出 per-step correctness score，从而以极低延迟完成 test-time reranking。GAIA [Wan26p] 把这条线推进到 data flywheel 范式，通过真实 GUI agent 的错误分布不断扩充训练集，持续训练 step-level binary critic，使 evaluator 学到的不是静态 benchmark 上的“理想错误”，而是 agent 在真实 rollout 中最常犯的局部失误。

同样的过程监督思想也延伸到了更专门的 agent 域。SWE-Shepherd [Dih26] 面向 code agent，把读文件、编辑、执行测试等中间动作转化为 heuristic progress reward，并据此训练 PRM 预测局部动作价值，从而支持 reward-guided search。整体来看，这一分支的演进路径相当清晰：早期工作先在 reasoning 中证明 step-level evaluator 的必要性 [Lig23, Luo24]，随后把局部监督从 correctness 扩展为 advantage、Q-value 与 hierarchical reward semantics [Set24, Li24m, Pal25, Che25s]，再在 GUI、computer-use 与 code agent 中把这些抽象过程信号落地为与环境状态变化、任务推进和动作后果直接对齐的 evaluator [Che25h, Dai25, Xi25b, Zha25z, Che26s, Wan26p, Wan26s, Dih26]。因此，这类方法的共同贡献并不是简单地“把轨迹拿来训练 reward model”，而是把原本只在完整 experience 中隐含存在的局部决策质量，重写为可复用、可搜索、可强化学习利用的过程性 evaluator。
```

### Diagnostic-feedback Evaluator Internalization

Diagnostic-feedback evaluator internalization 训练 evaluator 产生更丰富的语义反馈，而不仅是 scalar 或 scalarizable score。目标输出包括 natural-language critique、error diagnosis、failure explanation、verification rationale、risk analysis、policy-violation explanation 或 repair suggestion。这类 evaluator 不仅判断 agent 行为是好是坏，还解释为什么有问题以及应该如何修正。

这类方法体现了 evaluator 从 scoring function 向 feedback generator 的转变。在复杂 agent setting 中，单纯的 reward score 往往不足以支持有效自我修正：一个分数可以告诉 agent 某个动作不好，却未必指出违反了什么约束、基于了什么错误假设、忽略了哪些观察，或应该考虑什么替代动作。Diagnostic-feedback evaluator 通过内化更具解释性和行动指导性的反馈，弥补 scalar reward 的信息不足。

例如，reasoning task 中，critique model 可指出推理步骤为何无效；code task 中，feedback model 可说明错误修改导致了什么问题；robotic manipulation 中，failure detector 可基于视觉观察解释操作失败的原因；GUI 或 web automation 中，critic 可指出当前动作与用户意图、屏幕状态或任务约束的不一致；安全敏感场景中，risk evaluator 可在执行前解释某个动作为什么违反 policy 或存在风险。

Diagnostic-feedback evaluator 的输出通常是文本，输入可以是文本、视觉、多模态或 embodied trajectory。主要优势是信息量高、可解释性强，适合 reflection、debugging、repair、human oversight 和 constraint-aware decision making，也可以与 scalar reward 结合使用。

但评估 diagnostic feedback 的质量比 scalar label 更难。一个 critique 可能语言合理却在事实层面错误、不完整，或未抓住真正的失败原因。这类方法通常需要额外机制控制反馈质量：execution checking、human validation、self-consistency filtering，或利用下游 repair performance 作为间接训练信号。

并非所有 failure detector 或 risk classifier 都应归入此类。若模型只输出 \(0/1\) failure probability 或 scalar risk score，它更接近 outcome-supervised 或 process-supervised evaluator。仅当论文的核心贡献强调 failure reason、diagnosis、critique、rationale 或 correction guidance 时，才适合归入 Diagnostic-feedback Evaluator Internalization。

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



## Tokenized-to-Policy Experience Transformation

Tokenized-to-Policy Experience Transformation 将离散化的 agent experience 转化为 policy / actor parameters。源经验表现为自然语言轨迹、工具调用记录、代码编辑历史、GUI 操作序列、web browsing traces、reasoning chains、环境执行反馈等 tokenized artifacts；目标是将这些经验内化到模型参数中，使模型在后续任务中不必显式检索、拼接或重放原始经验，也能表现出更强的序贯决策能力。

从经验转化角度看，这一路径的核心不是简单地”训练一个更强的模型”，而是回答：agent 在交互过程中形成的离散经验，如何被组织为训练信号并改变 policy 的参数化决策能力？与 Narrative-to-Narrative 或 Narrative-to-Schematic transformation 不同，P5 的目标载体不再是可读的文本、规则、程序或工作流，而是模型内部的 policy weights。这一路径在可解释性、可编辑性与推理效率之间呈现明显权衡：经验一旦内化进参数，后续调用成本低，不受上下文窗口限制，但经验的显式可追踪性与局部可修改性会下降。

本文将 P5 进一步划分为四类：Imitation-based Policy Internalization、Reward-based Policy Internalization、Preference-based Policy Internalization 与 Evolution-based Policy Internalization，分别对应四种经验内化逻辑：模仿高质量轨迹、利用可验证奖励、构造轨迹偏好，以及通过闭环机制持续生成并内化新经验。


### Imitation-based Policy Internalization

Imitation-based Policy Internalization 将高质量 agent trajectories 直接作为监督示范，通过 behavior cloning、supervised fine-tuning 或 rejection-sampled fine-tuning 等方式训练 policy。基本假设是：若一组轨迹已体现有效的任务解决行为，模型可以通过模仿其中的动作选择、推理模式、工具调用习惯或 GUI 操作序列，将相应经验内化进参数。

在这类方法中，环境反馈或任务结果通常不直接作为优化目标，而是用于筛选、清洗、重构或标注训练轨迹。系统可从多条候选 trajectories 中保留成功完成任务的轨迹，也可根据执行结果过滤无效工具调用、错误 GUI 操作或失败代码修改——feedback 主要扮演 data selection 或 data construction 的角色。

从经验转化角度看，Imitation-based 方法将 agent experience 视为可模仿的行为模板。轨迹中的 action sequence、reasoning trace、tool-use pattern、workflow structure 或 interface operation 被作为”应该学习的行为样例”。训练后，模型不再需要在 prompt 中看到这些示范，就可在类似上下文中复现相应行为模式。这种方法尤其适合 agent 的 cold-start training，能快速教会模型任务格式、动作空间、输出协议和基本交互流程。

经验来源包括人工示范、teacher model 生成轨迹、自动探索得到的成功轨迹，以及由搜索、回滚、反思或重构机制生成的 reasoning traces。对 web agent、GUI agent、tool-use agent 和 code agent 等任务，Imitation-based internalization 往往是构建可用 policy 的第一步：模型先通过模仿高质量轨迹获得基本能力，再通过 reward-based 或 preference-based 方法提升性能。

能力上限通常受示范轨迹质量与覆盖范围限制。若训练数据只包含有限场景下的成功路径，模型可能学到表层格式或局部启发式，难以主动探索新策略。rejection-sampled fine-tuning 虽能提升样本质量，但可能丢弃失败轨迹中具有局部价值的经验。在长程、开放或高不确定性的 agent 任务中，单纯依赖 imitation 往往不足以支撑持续能力增长。

本文归入该类的判定标准：核心 policy update 主要依赖 SFT / behavior cloning / imitation objective；环境反馈主要用于筛选或构造训练样本，而非直接进入 policy-gradient 或 reward optimization 目标。

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

Reward-based Policy Internalization 指 agent 通过与环境交互产生 trajectories，利用非参数化、可验证的反馈信号直接优化 policy。典型反馈包括任务成功率、unit test 结果、代码执行反馈、SQL execution correctness、ground-truth answer match、工具调用结果、GUI 任务完成状态、机器人操作成功与否等。

与 Imitation-based 方法相比，Reward-based 方法不再只学习”成功轨迹中做了什么”，而是进一步学习”哪些行为在环境中真正有效”。这使其能利用 agent experience loop 的完整结构：context 和 action 构成 agent 的决策过程，observation 和 feedback 为 policy update 提供外部依据。在软件工程、数据库查询、工具调用、web navigation、GUI automation 与 embodied control 等任务中，环境往往能提供相对明确的成功或失败信号，因此 reward-based internalization 是 P5 中最直接、最典型的一类方法。

这类方法通常采用 PPO、GRPO、REINFORCE、RLVR 或其 agent-specific variants。LLM-based agents 的动作空间往往不是传统 RL 中的固定离散动作或连续控制量，而是自然语言 reasoning、tool call、代码片段、GUI 坐标、API 调用、search query、inter-agent message 等异构动作，因此 reward-based 方法通常需要对传统 RL 算法进行适配，以处理长上下文、多轮交互、结构化动作与复杂环境反馈。

Reward-based internalization 的主要优势在于能力上限较高。policy 可以通过试错发现超出示范数据的新策略，有潜力突破 imitation learning 的数据覆盖限制。对于具有可验证目标的任务，reward signal 还可帮助模型避免单纯模仿中的伪相关或错误示范，更直接地优化任务成功率。

但这类方法面临若干关键挑战：许多 agent 任务的 reward 极其稀疏，系统往往只有最终成功或失败信号，缺少中间步骤监督；长程任务中 credit assignment 十分困难，最终 reward 很难准确归因到具体 turn、step 或 token；online rollout 成本较高，尤其在 GUI、robotics、web browsing 与 software engineering 等环境中，执行一次完整 trajectory 需要真实环境交互、代码构建、页面加载或仿真运行；即便 reward 来自可验证环境，仍可能存在 reward hacking 或 proxy exploitation——agent 学到利用评测漏洞而非真正解决任务。

Reward-based Policy Internalization 内部形成了若干重要技术方向：outcome-level reward optimization，直接基于最终任务成败更新 policy；turn-level 或 step-level credit assignment，将最终反馈分配到中间动作以缓解稀疏奖励问题；entropy- 或 uncertainty-shaped optimization，通过不确定性、信息增益或熵调节探索行为，避免 policy 过早收敛或陷入无效探索；replay- 或 off-policy-enhanced optimization，复用历史经验、成功 transitions 或 semi-online trajectories 以提升样本效率；domain-specific reward design，针对 SQL、SWE、GUI、tool-use 或 VLA 任务设计更细粒度、更可靠的可验证反馈。

本文归入该类的判定标准：核心训练信号来自非参数化环境反馈、执行反馈、规则化 verifier 或 ground truth，且该反馈直接参与 policy optimization。若 reward 或 preference 主要来自 trained reward model、process reward model、fine-tuned judge、prompted LLM-as-judge 或 VLM-based evaluator，则不属于纯 P5，而应视为 evaluator-mediated policy optimization 或 P6 相关方法。

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

Preference-based Policy Internalization 从 agent experience 中构造轨迹间的相对偏好关系，通过 DPO、DMPO、IPO、KTO、ORPO 或其他 trajectory-pair optimization 方法更新 policy。相对更优的轨迹可来自成功任务、通过验证的执行结果、人工标注、修正后的轨迹或更高效的操作路径；相对较差的轨迹可来自失败尝试、错误工具调用、无效搜索、错误 GUI 点击或未通过测试的代码修改。

这类方法的基本动机是：在许多 agent 场景中，精确设计每一步 reward 很困难，但比较两条轨迹哪一条更好却相对容易。web navigation 中，一条轨迹成功找到目标信息，另一条陷入无关页面；GUI automation 中，一条轨迹到达目标界面，另一条点击了错误控件；tool-use 中，一条轨迹调用了正确工具得到有效结果，另一条产生了 hallucinated tool call；software engineering 中，一条轨迹通过测试，另一条引入了新错误。这些比较均可形成 preference signal。

从经验转化角度看，Preference-based 方法能显式利用失败经验。Imitation-based 方法通常只保留成功轨迹，Reward-based 方法需要将失败轨迹转化为数值 reward 或 advantage。Preference-based 方法提供了另一种选择：失败轨迹作为 negative sample 与成功轨迹、修正轨迹或更高效轨迹配对，帮助 policy 学习哪些行为应该避免。

Preference-based internalization 适合四类场景：任务反馈天然表现为 success / failure 对比而非连续数值 reward；存在大量失败或低质量 trajectories，直接丢弃浪费经验；可通过 verifier、execution result、unit test、task completion 或人工标注自动构造 preferred / dispreferred pairs；agent 的错误模式具有结构性——错误工具调用、无效搜索、错误 GUI 点击、冗余步骤或不 grounded 的推理。通过偏好优化，模型不仅学习成功行为，也学习避免失败行为。

与 Reward-based 方法相比，Preference-based 方法具有更稳定的 supervised-style 训练形式，不需直接估计高方差 policy gradient，也不要求精确设计 step-level reward。与 Imitation-based 方法相比，它能利用负样本和轨迹间对比，更适合处理失败经验、修正经验和探索经验。

但这类方法也有自身限制。preference pairs 的构造质量直接影响训练效果——若 preferred / dispreferred 的判定过于粗糙，模型可能学到表层差异而非真正的策略改进。trajectory-level preference 仍可能缺乏细粒度 credit assignment：模型知道哪条轨迹更好，却未必知道哪些步骤真正导致了差异。若偏好标签来自 LLM-as-judge 或 trained reward model，监督信号已经过参数化 evaluator，发生了 Evaluator-to-Policy transformation，不能再视为纯粹 P5。

本文归入该类的判定标准：核心 policy update objective 是 preference optimization 或 trajectory-pair optimization；偏好标签主要来自非参数化信号——执行成功、任务完成、测试通过、人工 per-trajectory 标注或规则化比较——而非参数化 evaluator。

论文：
- Direct Multi-Turn Preference Optimization for Language Agents
- Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents
- UI-Voyager: A Self-Evolving GUI Agent Learning via Failed Experience


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
