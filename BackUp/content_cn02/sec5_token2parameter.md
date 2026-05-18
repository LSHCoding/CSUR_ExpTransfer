

## Tokenized-to-Evaluator Experience Transformation

Tokenized-to-Evaluator Experience Transformation 将 tokenized agent experience 内化为参数化评估器。tokenized experience 包括 agent trajectory、reasoning trace、tool-use log、action history、preference pair、execution outcome、failure annotation、diagnostic feedback 等。通过训练，这些离散经验中的评价语义被写入 evaluator 参数，形成可复用的评估能力。训练后的 evaluator 表现为 outcome reward model、process reward model、verifier、critic、judge、value model、failure detector 或 diagnostic feedback model。

这类方法与 prompted LLM-as-a-judge 有本质区别。Prompted judge 仅在推理时通过 prompt 激发现有模型的评估能力，而 P4 要求 evaluator 的参数发生训练更新——评价能力被经验数据显式内化进模型参数。

本文按训练后 evaluator 向 agent 提供的监督信息形式组织方法。Outcome-supervised evaluator internalization 学习完整输出或完整轨迹上的全局评估信号；Process-supervised evaluator internalization 学习中间推理步骤、动作前缀或局部决策上的过程性评估信号；Outcome-supervised evaluator internalization 和 Process-supervised evaluator internalization 得到 Evaluator，其输出主要是 scalar 或 scalarizable reward，Diagnostic-feedback evaluator internalization 超越 scalar 或 scalarizable reward，内化 critique、error diagnosis、rationale 或 repair suggestion 等更丰富的语义反馈；Evolution-based evaluator internalization 描述 evaluator 随 agent 经验分布变化而持续更新的动态扩展，构成单步 evaluator construction 与 composite self-improving agent pipeline 之间的边界区域。

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

新增：
- I-FailSense: Towards General Robotic Failure Detection with Vision-Language Models
- Generative Verifiers: Reward Modeling as Next-Token Prediction
- Self-Generated Critiques Boost Reward Modeling for Language Models
- Enhancing Robotic Manipulation with AI Feedback from Multimodal Large Language Models

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

新增：
- SAFE: Multitask Failure Detection for Vision-Language-Action Models
- Towards Policy-Compliant Agents: Learning Efficient Guardrails For Policy Violation Detection


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
- AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation  
- Self-Refining Vision Language Model for Robotic Failure Detection and Reasoning  
- OS-Oracle: A Comprehensive Framework for Cross-Platform GUI Critic Models  
- Look Before You Leap: A GUI-Critic-R1 Model for Pre-Operative Error Diagnosis in GUI Automation  
- WebArbiter: A Principle-Guided Reasoning Process Reward Model for Web Agents  
- Web-Shepherd: Advancing PRMs for Reinforcing Web Agents  
- SOLE-R1: Video-Language Reasoning as the Sole Reward for On-Robot Reinforcement Learning  
- Hybrid Reward Normalization for Process-supervised Non-verifiable Agentic Tasks  
- No More Stale Feedback: Co-Evolving Critics for Open-World Agent Learning  
- Don’t Act Blindly: Robust GUI Automation via Action-Effect Verification and Self-Correction  
- AgentV-RL: Scaling Reward Modeling with Agentic Verifier  
- Teaching Language Models to Critique via Reinforcement Learning  
- DeepCritic: Deliberate Critique with Large Language Models  
- Enhancing LLM Reasoning via Critique Models with Test-Time and Training-Time Supervision  
- StepWiser: Stepwise Generative Judges for Wiser Reasoning  
- RL4F: Generating Natural Language Feedback with Reinforcement Learning for Repairing Model Outputs 


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
- AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials
- NNetNav: Unsupervised Learning of Browser Agents Through Environment Interaction in the Wild
- Training Software Engineering Agents and Verifiers with SWE-Gym

```
Imitation-based Policy Internalization 关注的是如何通过 imitation-style 的监督目标，将 tokenized agent experience 转化为 policy parameters，而非通过显式 reward optimization 来更新策略。[Pat24, Lai25d, Pap25b, Pah25, Gan25b, Hu25i, Zen23d, Xu24, Mur24b, Pan24] 这一路径的关键不只是收集 trajectories，而是将原始交互轨迹转化为足够可靠的监督信号，使其能够支持参数更新。总体而言，这类方法通常遵循相似的经验转化流程：agent 先在环境中产生 reasoning-action trajectories、tool-use traces、GUI operation sequences、web interaction histories 或 code-editing episodes；随后，系统利用任务结果、verifier judgment、self-critique、subgoal decomposition 或 hindsight relabeling 等机制，对这些轨迹进行筛选、重构、重标注或结构化处理；最后，将处理后的序列作为 supervised demonstrations，用于 SFT、behavior cloning 或 rejection-sampled fine-tuning，从而将相应的决策模式吸收到 policy weights 中。从 experience transformation 的角度看，这一类方法中的环境反馈主要承担 data construction 与 quality control 的作用，而不是像 RL 中那样直接作为 reward signal 进入 policy-gradient 式的 credit assignment。

进一步看，这一子类的差异主要体现在 trajectory 如何被转化为 imitation target。部分工作主要依赖 success filtering，将完成任务的 trajectories 直接转化为可模仿的监督样本：例如，[Pat24] 通过 environment error 与 self-critique 过滤 self-generated web trajectories，再进行 supervised self-improvement；[Pap25b] 在 AndroidWorld 中保留成功 rollout，并继续以 SFT loss 而非 policy gradient 进行迭代更新；[Pan24] 则利用 unit-test outcome 从 software engineering trajectories 中筛选成功样本，并通过 rejection-sampling fine-tuning 完成 policy update。另一部分工作则更强调在参数更新之前，对 trajectory 本身进行重构或增强，以提高 imitation signal 的质量与覆盖范围： [Lai25d] 利用 StepCritic 将 Android trajectories 分解为 subgoals，并结合 trajectory augmentation 扩展高质量示范；[Hu25i] 将 reflection、branching 与 rollback 中隐含的推理过程重构为显式 Chain-of-Thought，使 reasoning 与 action 能够被联合模仿；[Mur24b] 通过 hindsight relabeling 将 exploratory browser interaction 转化为 instruction-conditioned demonstrations；[Xu24] 则将 web tutorials 转写为可执行的 procedural guidance，并通过 guided replay 合成 demonstrations。还有一些工作更突出强 agent 或大规模 exploration pipeline 在 imitation data construction 中的作用： [Pah25] 与 [Gan25b] 都先通过结构化网页探索生成并验证 success trajectories，再将这些轨迹蒸馏为学生模型的监督数据；[Zen23d] 则将多个环境中的 GPT-4 agent trajectories 统一为 thought-action supervision，用于 generalized agent tuning。总体而言，这一子类共享的核心机制是：先将 tokenized trajectory 加工为“可模仿的行为模板”，再通过监督式参数更新将外显经验压缩为可复用的内隐 policy competence。[Pat24, Lai25d, Pap25b, Pah25, Gan25b, Hu25i, Zen23d, Xu24, Mur24b, Pan24]
```

### Reward-based Policy Internalization

Reward-based Policy Internalization 指 agent 通过与环境交互产生 trajectories，利用非参数化、可验证的反馈信号直接优化 policy。典型反馈包括任务成功率、unit test 结果、代码执行反馈、SQL execution correctness、ground-truth answer match、工具调用结果、GUI 任务完成状态、机器人操作成功与否等。

与 Imitation-based 方法相比，Reward-based 方法不再只学习”成功轨迹中做了什么”，而是进一步学习”哪些行为在环境中真正有效”。这使其能利用 agent experience loop 的完整结构：context 和 action 构成 agent 的决策过程，observation 和 feedback 为 policy update 提供外部依据。在软件工程、数据库查询、工具调用、web navigation、GUI automation 与 embodied control 等任务中，环境往往能提供相对明确的成功或失败信号，因此 reward-based internalization 是 P5 中最直接、最典型的一类方法。

这类方法通常采用 PPO、GRPO、REINFORCE、RLVR 或其 agent-specific variants。LLM-based agents 的动作空间往往不是传统 RL 中的固定离散动作或连续控制量，而是自然语言 reasoning、tool call、代码片段、GUI 坐标、API 调用、search query、inter-agent message 等异构动作，因此 reward-based 方法通常需要对传统 RL 算法进行适配，以处理长上下文、多轮交互、结构化动作与复杂环境反馈。

Reward-based internalization 的主要优势在于能力上限较高。policy 可以通过试错发现超出示范数据的新策略，有潜力突破 imitation learning 的数据覆盖限制。对于具有可验证目标的任务，reward signal 还可帮助模型避免单纯模仿中的伪相关或错误示范，更直接地优化任务成功率。

但这类方法面临若干关键挑战：许多 agent 任务的 reward 极其稀疏，系统往往只有最终成功或失败信号，缺少中间步骤监督；长程任务中 credit assignment 十分困难，最终 reward 很难准确归因到具体 turn、step 或 token；online rollout 成本较高，尤其在 GUI、robotics、web browsing 与 software engineering 等环境中，执行一次完整 trajectory 需要真实环境交互、代码构建、页面加载或仿真运行；即便 reward 来自可验证环境，仍可能存在 reward hacking 或 proxy exploitation——agent 学到利用评测漏洞而非真正解决任务。

Reward-based Policy Internalization 内部形成了若干重要技术方向：outcome-level reward optimization，直接基于最终任务成败更新 policy；turn-level 或 step-level credit assignment，将最终反馈分配到中间动作以缓解稀疏奖励问题；entropy- 或 uncertainty-shaped optimization，通过不确定性、信息增益或熵调节探索行为，避免 policy 过早收敛或陷入无效探索；replay- 或 off-policy-enhanced optimization，复用历史经验、成功 transitions 或 semi-online trajectories 以提升样本效率；domain-specific reward design，针对 SQL、SWE、GUI、tool-use 或 VLA 任务设计更细粒度、更可靠的可验证反馈。

本文归入该类的判定标准：核心训练信号来自非参数化环境反馈、执行反馈、规则化 verifier 或 ground truth，且该反馈直接参与 policy optimization。若 reward 或 preference 主要来自 trained reward model、process reward model、fine-tuned judge、prompted LLM-as-judge 或 VLM-based evaluator，则不属于纯 P5，而应视为 evaluator-mediated policy optimization 或 P6 相关方法。

论文：
- Grounding Large Language Models in Interactive Environments with Online Reinforcement Learning [Car23]
- Large Language Models as Generalizable Policies for Embodied Tasks [Szo23]
- ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL [Zho24f]
- WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning [Wei25]
- Training Long-Context, Multi-Turn Software Engineering Agents with Reinforcement Learning [Gol25]
- GUI-R1: A Generalist R1-Style Vision-Language Action Model For GUI Agents [Luo25b]
- Improving Vision-Language-Action Model with Online Reinforcement Learning [Guo25d]
- AgentCPM-GUI: Building Mobile-Use Agents with Reinforcement Fine-Tuning [Zha25an]
- SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning [Li25aa]
- Fine-Tuning Large Vision-Language Models as Decision-Making Agents via Reinforcement Learning [Zha24s]
- AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning [Xi25c]
- Agentic Reinforced Policy Optimization [Don25d]
- AgentRL: Scaling Agentic Reinforcement Learning with a Multi-Turn, Multi-Task Framework [Zha25ag]
- Information Gain-based Policy Optimization: A Simple and Effective Approach for Multi-Turn LLM Agents [Wan25y]
- UI-S1: Advancing GUI Automation via Semi-online Reinforcement Learning [Lu25j]
- EPO: Entropy-regularized Policy Optimization for LLM Agents Reinforcement Learning [Xu25k]
- SQL-Trail: Multi-Turn Reinforcement Learning with Interleaved Feedback for Text-to-SQL [Hua26d]
- LongNav-R1: Horizon-Adaptive Multi-Turn RL for Long-Horizon VLA Navigation [Hu26e]
- Agentic Entropy-Balanced Policy Optimization [Don25c]
- Harnessing Uncertainty: Entropy-Modulated Policy Gradients for Long-Horizon LLM Agents [Wan25ad]
- ARPO: End-to-End Policy Optimization for GUI Agents with Experience Replay [Lu25f]
- Group-in-Group Policy Optimization for LLM Agent Training [Fen25c]
- ToolRL: Reward is All Tool Learning Needs [Qia25b]
- Generalization in Online Reinforcement Learning for Mobile Agents [Gu26b]
- Reinforcement Learning for Long-Horizon Interactive LLM Agents [Che25af]
- Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs [Li25ae]
- Q-SFT: Q-Learning for Language Models via Supervised Fine-Tuning [Hon24]
- SQL-ASTRA: Alleviating Sparse Feedback in Agentic SQL via Column-Set Matching and Trajectory Aggregation [Li26r]
- RLVMR: Reinforcement Learning with Verifiable Meta-Reasoning Rewards for Robust Long-Horizon Agents [Zha25ao]
- Succeed or Learn Slowly: Sample Efficient Off-Policy Reinforcement Learning for Mobile App Control [Pap25c]

```
## Reward-based Policy Internalization

Reward-based Policy Internalization 指 agent 在与环境交互过程中产生 tokenized experience，并利用环境返回的非参数化、可验证反馈直接优化 policy parameters，使离散经验最终以内化的行为能力而非外部 artifacts 的形式保存在模型中。与 imitation-based internalization 主要回答“成功轨迹是什么样”不同，这一路径更直接回答“哪些行为在环境中真正有效”，因此其核心监督不来自示范本身，而来自任务执行后的外部结果，如 task completion、unit test 结果、SQL execution correctness、tool invocation correctness、GUI 操作完成状态或 embodied success [Car23, Wei25, Gol25, Hua26d]。从 experience transformation 的角度看，该类方法的本质是把 context–action–observation–feedback 回路中的反馈部分转写为 policy update，使过去交互中的 trial-and-error 不再需要被显式重放，而是被压缩为 actor 对未来相似情境的参数化反应能力。

这一方向的早期工作首先证明了 foundation model 可以直接作为交互式 policy，并通过环境奖励被“ground”到真实决策问题上。GLAM 将 FLAN-T5 放入 BabyAI-Text 等交互环境中，通过 PPO 利用任务成功奖励对语言模型做 online grounding，使其从文本观测中学会生成环境可执行动作 [Car23]。LLaRP 则将冻结的 LLaMA 与视觉编码器连接为 embodied policy，并以 success、subgoal completion 和 invalid action penalty 等环境反馈进行 DD-PPO 训练，说明 language model 也可以直接吸收具身任务中的长程交互经验 [Szo23]。这些工作确立了 Reward-based Policy Internalization 的基本前提，即只要 agent 的动作可以在环境中执行，且环境能够返回客观可验证的结果，tokenized trajectory 就可以不经外部 memory，而被直接转化为 policy weights。

在此基础上，第一类核心方法是 outcome-grounded policy optimization，即直接以 trajectory-level 的最终成败作为 policy internalization 的主监督。这类方法通常不试图先学习一个 evaluator，再由 evaluator 间接指导 actor，而是直接将环境结果映射为可优化目标。WebAgent-R1 将网页交互建模为端到端 multi-turn RL 问题，使用 M-GRPO 对同一任务并行采样多条 browser trajectories，并通过 URL match、string match 与 Playwright-based verification 产生结果奖励 [Wei25]。Training Long-Context, Multi-Turn Software Engineering Agents with Reinforcement Learning 面向长上下文 Software Engineering agent，先用能通过测试的轨迹做 Rejection Fine-Tuning 热启动，再利用 DAPO 在真实代码环境中继续优化；在这一过程中，奖励直接来自 unit test pass or fail 与 trajectory length penalty，因此模型学到的是哪些多轮编辑与调试行为真正能在执行环境中生成可用 patch [Gol25]。类似地，Reinforcement Learning for Long-Horizon Interactive LLM Agents 在 AppWorld 中以任务结束时 unit tests 的通过比例作为奖励，利用 leave-one-out PPO 训练能完成长程 API 调用和状态操作的 interactive agents [Che25af]。在这些工作中，reward 的角色不是辅助筛选轨迹，而是直接定义 policy 应该吸收什么经验，因此它们构成了 Reward-based Policy Internalization 最纯粹的形式。

然而，agent 场景中的一个核心困难在于，最终反馈通常极为稀疏，而真正需要学习的决策往往跨越多个 turn、多个 tool call 或多个 environment transition。因此，第二类关键工作转向 credit-aware reward redistribution，即在不改变外部 feedback 本质的前提下，把稀疏 trajectory reward 重新组织为更适合长程 agent 学习的局部训练信号。ArCHer 是这一方向的代表，它将 multi-turn language agent 的学习拆成高层 utterance-level critic 与低层 token-level policy，使环境回报先被整合为回合级价值，再传递给 token 生成层 [Zho24f]。Turn-PPO 进一步指出，对 agent 来说真正的决策单元通常是一整轮 response，而不是单个 token，因此将 multi-turn interaction 显式建模为 turn-level MDP，并在 turn 粒度上用 critic 做 GAE，可使环境反馈更准确地对齐到回合级 reasoning 或 tool-use 决策 [Li25ae]。GiGPO 则利用 anchor state grouping 比较不同 rollout 在相同中间状态下采取的不同动作，同时构造 episode-level 与 step-level relative advantage，在无需额外 critic 的前提下提高奖励分配的局部精度 [Fen25c]。Information Gain-based Policy Optimization 代表了另一种思路：它不直接学习 value decomposition，而是用每一轮交互前后正确答案 log-prob 的增量定义 Information Gain reward，将 observation 的真实信息贡献转化为 turn-level intrinsic signal [Wan25y]。在 SQL 场景中，SQL-ASTRA 通过 step-level Column-Set Matching Reward 从中间执行结果中提取局部结构正确性，再用 trajectory aggregation 将这些局部改进汇聚为更稳定的轨迹级训练信号 [Li26r]。这类方法的共同点在于，它们关注的不是“是否有 reward”，而是“如何把最终可验证反馈转译成与 agent 决策结构相匹配的 update unit”。

第三类工作进一步表明，仅有 reward redistribution 仍然不足，因为长程 agent 很容易在训练早期过快坍缩到低探索策略。因此，一批方法开始显式把 exploration 和 uncertainty 纳入 Reward-based Policy Internalization 的核心机制。Agentic Reinforced Policy Optimization 在 multi-turn tool-use 过程中引入 entropy-based adaptive rollout，在高不确定性步骤触发局部分支采样，再通过 advantage attribution estimation 区分共享前缀与分支后动作的贡献，使 correctness、format 与 multi-tool collaboration 等规则奖励能够更细粒度地塑造 policy [Don25d]。EPO 则在 PPO 或 GRPO 外层加入 trajectory-level entropy regularization 与 entropy smoothing，专门缓解 sparse-reward multi-turn RL 中的 exploration-exploitation cascade failure，使模型在长轨迹优化过程中避免过早丢失探索能力 [Xu25k]。在 embodied navigation 中，LongNav-R1 用 geodesic distance 改善与 SPL 构造环境奖励，并通过 horizon-adaptive kernel baseline 处理不同阶段的 advantage estimation，使 long-horizon navigation 中的探索、逼近和终局完成能够获得更合适的训练信号 [Hu26e]。SimpleVLA-RL 也体现了类似趋势：它通过高温采样、dynamic sampling 与 critic-free GRPO，提高 VLA 在 binary outcome reward 下发现新策略的能力 [Li25aa]。这一类工作说明，在 Reward-based Policy Internalization 中，探索并不是 reward 之外的附属问题，而是决定经验能否真正沉淀为 policy capability 的核心环节。

第四类工作则把关注点放在 experience reuse and efficiency enhancement 上。由于 GUI、software、web 和 embodied environment 的 rollout 成本很高，许多方法开始研究如何提高每一条 tokenized interaction trajectory 向 policy 的转化效率。ARPO 在 GUI 环境中维护成功 trajectory replay buffer，当当前采样组全部失败时从历史缓冲区注入正样本，以避免 group-based RL 因全零奖励而失去有效梯度 [Lu25f]。Reinforcement Learning for Long-Horizon Interactive LLM Agents 通过多 rollout 的 leave-one-out baseline 允许对同一批 collected trajectories 做多轮更新，在无需额外 critic 的前提下提高高成本环境中的训练效率 [Che25af]。AgentGym-RL 则从训练组织方式入手，提出 ScalingInter-RL，通过先短后长的 horizon curriculum 让 agent 先掌握基础交互，再逐步吸收更长程的决策经验，从而显著改善从零开始训练 multi-turn agents 的稳定性 [Xi25c]。在 VLA 设置下，Improving Vision-Language-Action Model with Online Reinforcement Learning 采用 RL 与 supervised learning 交替的两阶段框架：先在 RL 阶段利用 binary success reward 发现成功轨迹，再将这些轨迹回流到 supervised stage 做 LoRA 微调，以缓解大模型直接在线 RL 时的不稳定性 [Guo25d]。从 transformation 角度看，这类方法解决的是“经验如何高效地被吸收”，而不是“经验是否可吸收”。

值得注意的是，尽管这类方法并不适合按领域划分，但不同交互环境中的 reward design 确实越来越结构化。Text-to-SQL 是一个典型例子。SQL-Trail 将 agent 放入 reason–execute–observe 循环，不仅利用 final execution correctness，还引入 syntax validity、schema grounding 与 turn-budget shaping，使 policy 学会在多轮数据库交互中逐步修正错误 SQL，而不是仅优化最终答案是否正确 [Hua26d]。ToolRL 也并非只依赖任务是否完成，而是将奖励分解为 format correctness 以及 tool name、parameter name、parameter content 的层级匹配分数，使模型能从工具调用过程中的结构化约束直接学习动作语义 [Qia25b]。因此，domain-specific reward design 更适合作为 Reward-based Policy Internalization 的横向趋势来理解：随着 agent 环境变得更复杂，真正高价值的 reward 不再只是一个终局 success flag，而是环境中那些可程序验证的中间结构被逐步挖掘出来，并重写为 policy optimization 的组成部分。

总体来看，Reward-based Policy Internalization 的主线不是“用 RL 训练更强的 agent”这么简单，而是如何把可验证环境反馈系统地转译为可被 actor 吸收的参数更新信号。其方法演化大致经历了三个层层推进的过程：首先证明 foundation model 可以直接作为交互式 policy，并从环境成功信号中学习 [Car23, Szo23]；随后转向多轮 agent setting，重点解决 sparse reward 下的 credit assignment 与 exploration collapse [Zho24f, Li25ae, Fen25c, Wan25y, Don25d, Xu25k]；进一步又在高成本交互环境中发展出 replay、curriculum 和 staged optimization 等经验复用机制，以提高 tokenized trajectories 向 policy weights 的转化效率 [Lu25f, Che25af, Xi25c, Guo25d]。在这一意义上，Reward-based Policy Internalization 代表的是一条从“交互经验的可验证结果”直接通向“参数化决策能力”的 transformation pathway：经验并不以可读 artifacts 的形式留下，而是以更低推理成本、更弱显式可追踪性但更强执行即时性的方式沉淀到 actor 内部。
```

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
- Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards
- Advancing Tool-Augmented Large Language Models: Integrating Insights from Errors in Inference Trees
- Solving the Granularity Mismatch: Hierarchical Preference Learning for Long-Horizon LLM Agents
- WEPO: Web Element Preference Optimization for LLM-based Web Navigation

```

Preference-based Policy Internalization 的核心，是从 agent interaction experience 中构造 preferred 与 dispreferred trajectory 或 action pair，并通过 DPO 及其变体将这种相对偏好直接内化到 policy weights，而非显式设计逐步 reward 或仅保留成功示范。[Shi24c] 将这一思路系统扩展到 multi-turn language agent 场景，使偏好优化能够作用于完整交互轨迹；[Son24] 则进一步强调失败经验的价值，通过将探索得到的失败轨迹与成功示范配对，使策略同时学习成功行为与应避免的错误路径。

这一路径也常见于可验证环境中的 agent post-training，即先由执行结果诱导出相对偏好，再进行 policy internalization。[Da25] 依据 unit test 的 pass fail 结果构造软件工程轨迹的 preference pairs，并结合 guidance 缓解稀疏反馈下的探索困难；[Che24k] 则从 tool-use inference tree 中提取成功步骤与失败分支形成 step-level preference，从而将搜索过程中暴露的错误工具调用与无效推理转化为负监督。

近期工作进一步开始优化偏好信号的粒度设计。[Gao25c] 指出长程任务中仅做 trajectory-level comparison 往往过粗，因此联合 trajectory-level、group-level 与 step-level preference 进行分层优化；[Liu25z] 则将偏好学习收缩到 web element selection 层面，通过对目标元素与干扰元素的对比训练提升 web navigation 中的局部动作判别能力。整体来看，这类方法的共同特点是将原本容易被丢弃的失败、冗余与局部误操作保留下来，并重写为可直接驱动 policy update 的 comparative supervision。
```

| 标题 | 关键思想与方法 ｜ 粒度 ｜ 产物 ｜ 领域 ｜ 备注 ｜
| --- | --- | --- | --- | --- | --- |

开始做这批 paper 的全文判定了。先把项目里已有 PDF 的论文逐篇读起来，同时把缺全文的条目标出来，后面你补传后我可以无缝续上。
| 标题 | 关键思想与方法 ｜ 粒度 ｜ 产物 ｜ 领域 ｜ 备注 ｜
| --- | --- | --- | --- | --- | --- |
| S2J: Bridging the Gap Between Solving and Judging Ability in Generative Reward Models | 该文把 mixed judging experience 内化进 generative reward model，训练样本来自 Math-DPO-10K、WebInstruct-verified 与 HelpSteer3，包含候选答案、模型自解过程与最终偏好判定。训练核心是 S2J 的 RLVR 配方，用 DAPO 或 GRPO 一类 RL 优化把 solving correctness 与 judging correctness 组成联合回报，同时更新 judge 本身参数，而非只靠 prompt 激发已有能力。训练后 Evaluator 学到的是对完整候选回答或比较对象进行自解再裁决的能力，既能判断最终 verdict 是否正确，也能在 subjective preference 任务上给出偏好结论。其推理产物是显式生成的 judging rationale 加最终 verdict token，下游既可把 verdict 当 reward signal 用于 post-training，也可把整段评判过程当作可读 judge output 用于自动评测。 | outcome | non-scalar | general | 训练回报是 outcome-level。虽然最后 verdict 可塌缩为标量，但模型有意对外暴露完整 judging rationale，因此更接近 non-scalar。 |
| J4R: Learning to Judge with Equivalent Initial State Group Relative Policy Optimization | 该文用 ReClor 与 MATH 上的 pairwise judged responses 训练 judge，经验数据是不同 LLM 生成的完整候选解答对，并进一步构造顺序互换等 equivalent initial state 子组来增强位置鲁棒性。训练方法是 EIS-GRPO，用 rule-based correctness 与格式奖励对整次 judging rollout 施加 RL 信号，直接更新 judge 参数。训练后模型学到的是对完整 reasoning answers 做稳健 pairwise judgment 的能力，尤其减少位置偏置与表面格式对判定的干扰。推理时它会先生成 critique 式 rationale，再输出类似 A>B 的最终判断标签，下游用作 reasoning evaluator 或自动 judge。 | outcome | non-scalar | reasoning math | 奖励挂在最终 judgment 是否正确上，属于 outcome。虽然最终有离散标签，但有意输出 critique 文本，因此记为 non-scalar。 |
| RL-VLM-F: Reinforcement Learning from Vision Language Foundation Model Feedback | 该文把机器人交互中采样到的图像状态对转成 preference data，经验来源是 agent 在控制与 manipulation 环境中收集的 observation buffer，再由 GPT-4V 或 Gemini 先做 analysis 再给 pairwise label。训练用 Bradley-Terry 式 preference learning 与 binary cross-entropy 学一个参数化 reward model，把 VLM 的离散偏好监督内化为连续奖励函数。训练后 Evaluator 学到的是给单帧或短段视觉状态相对任务目标打分的能力，本质上判断哪个状态更接近成功。其推理产物只有 scalar reward score，下游直接作为 SAC 等 RL 算法的奖励信号。 | process | scalar | embodied robotics | 监督落在状态或短段比较上，更像局部 progress supervision，而非整条 episode verdict。 |
| Video-Language Critic: Transferable Reward Functions for Language-Conditioned Robotics | 该文把机器人执行视频与语言指令配对为训练经验，正样本来自成功 demonstration，负样本来自 random action failures，并在时间维度上使用成功视频内部的前后帧次序。训练方法是对比式 symmetric cross-entropy 加 sequential ranking objective，一方面学 video-language alignment，另一方面强制成功轨迹中后期片段分数高于前期片段。训练后 Evaluator 学到的是对视频前缀相对指令完成度打连续分的能力，可作为 transferable reward function。其推理产物是每个时间步的 scalar similarity 或 reward score，下游既可用于 SAC 式 RL，也可用于 trajectory ranking 与 planning。 | outcome+process | scalar | embodied robotics | 对比目标是整段视频与指令匹配，属 outcome。顺序排序目标又给局部时间位置施加 progress 约束，故记为 outcome+process。 |
| Large Reward Models: Generalizable Online Robot Reward Generation with Vision-Language Models | 该文把多来源机器人与人类交互视频转成 reward supervision，经验数据来自 OXE、HOI4D、EgoDex、LIBERO、RoboCasa 等 24 个来源的视频轨迹，并自动抽取关键帧形成 progress 与 completion 样本。训练时对同一 Qwen3-VL backbone 结合 LoRA、SFT 与 DPO，分别学习 contrastive reward、absolute progress reward 与 completion reward，把时序经验内化进统一 LRM。训练后 Evaluator 学到的是既能判断任务是否完成，也能估计当前进展快慢与相对优劣的评估能力。推理时模型会生成 reasoning-first 的分析文本并给出离散或连续 reward label，下游主要解析成数值奖励供 PPO 在线机器人学习与 trajectory filtering 使用。 | outcome+process | scalar+non-scalar | embodied robotics | completion 头是 outcome，progress 与 contrastive reward 是 process。文本分析是显式输出，但实际下游主要消费数值 reward。 |
| RoboReward: General-Purpose Vision-Language Reward Models for Robotics | 该文把 OXE demonstration 与 RoboArena 中带人类核验进度分的 success 或 failure rollouts 汇成经验数据，并通过 counterfactual relabeling 与 temporal clipping 构造 1 到 5 级 episode rubric。训练方法是对 Qwen3-VL 的 fusion 与 LLM 层做 supervised fine-tuning，以 MAE 回归离散 episodic reward。训练后 Evaluator 学到的是对完整机器人 rollout 给出整体完成质量评分的能力，而不是解释具体哪一步出错。其推理产物是 1 到 5 的离散 reward score，下游直接作为 DSRL 等真实机器人 RL 的外部奖励。 | outcome | scalar | embodied robotics | 论文明确聚焦 episodic rewards，即使分数名为 progress，也仍挂在整段 episode 上。 |
| Generative Reward Models | 该文把 UltraFeedback 与 UltraInteract 中的 preference pairs、reasoning traces 与自生成 rationales 作为经验数据，探索把 reward modeling 改写成 next-token generation。训练方法包括直接 SFT 的 GenRM、带推理链的 CoT-GenRM，以及用 STaR 自举 rationales 的 SFT 与 DPO 变体，把偏好经验内化进 judge 权重。训练后 Evaluator 学到的是对完整候选回答给出偏好 verdict，并在部分变体中显式生成判决理由的能力。其产物在直接 GenRM 里可只是 verdict token 概率，在 CoT 变体里则是 rationale 加 verdict，下游用于 RLHF 中的 reward scoring、re-ranking 与 alignment。 | outcome | scalar+non-scalar | general | 论文同时包含仅输出 verdict 的 direct GenRM 与显式输出 rationale 的 CoT-GenRM，故记为 scalar+non-scalar。 |
| VLP: Vision-Language Preference Learning for Embodied Manipulation | 该文从 Meta-World 轨迹构造 MTVLP 数据，经验数据是 expert、medium、random 三类 manipulation 视频段与 GPT-4V 生成的多样语言指令。训练时不用人工偏好，而用 Intra-Task、Inter-Language、Inter-Video 三类隐式 preference 规则构建比较标签，再用总 cross-entropy 目标学习跨模态 preference model。训练后 Evaluator 学到的是判断某段操作视频在给定语言目标下是否更优的能力，本质是 trajectory segment 级 preference scorer。其推理产物是单个 scalar preference score，下游作为 offline RL 的 reward annotator，支持 P-IQL、IPL、CPL 等策略学习。 | outcome | scalar | embodied robotics | 标签挂在整段 trajectory segment 上，而非某个单步 action。 |
| LIV: Language-Image Representations and Rewards for Robotic Control | 该文把 egocentric human video 与文本描述，以及少量机器人域内数据，作为经验来源来训练 language-image value representation。训练方法结合 VIP 风格的时序 value pretraining 与 CLIP 风格 InfoNCE，对初始帧、中间帧、目标帧之间的相对位置施加学习信号，使表征编码任务进展。训练后 Evaluator 学到的是给当前图像与语言目标之间估计距离或价值的能力，可在无动作标注时形成 dense reward。其推理产物是 scalar similarity 或 value score，下游直接用于 planning、reward specification 与 imitation learning。 | process | scalar | embodied robotics | 虽然目标来自终态图像或文本，但监督分配到子轨迹时序位置，属于 process-oriented progress signal。 |
| Vision-Language Models as Success Detectors | 该文把 household、robot manipulation 与 Ego4D 视频中的行为轨迹切成 clips，并用人工标注每个 clip 是否已经达到任务成功，从而形成 SuccessVQA 经验数据。训练方法是把 success detection 改写成 visual question answering，对 Flamingo 的视觉相关层做 supervised finetuning。训练后 Evaluator 学到的是对给定视频片段和任务描述回答 yes 或 no 的成功检测能力。其推理产物是二值文本标签 yes 或 no，下游既可用于 policy evaluation，也可用于 reward-filtered behavior cloning。 | outcome | scalar | embodied robotics | 虽然样本是 clip 而非整条长轨迹，但标签仍挂在该片段整体是否成功上，而非单步局部行为。 |
| WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning | 该文的经验数据来自 WebArena-Lite 上 12200 条 web rollout 以及后续在线课程学习中新生成的 trajectory buffer，包含状态、动作、HTML 观测与环境成败。它同时训练两个评估器模块，一是用终局 success 或 failure 信号监督的 Outcome-supervised Reward Model，二是用 rollout return 与 GAE 更新的 value network critic。训练方法因此结合二值 outcome fine-tuning、critic cross-entropy 或 value 学习、KL-constrained policy update 与 curriculum RL。训练后 Evaluator 学到的是既能对完整 web trajectory 判定成败，也能对中间状态提供价值估计；推理产物主要是 YES 或 NO 型成功判断和 scalar value，下游分别用于无脚本环境中的 reward 替代与策略优化。 | outcome+process | scalar | web | 论文同时训练 outcome ORM 与 process-like critic，故记为 outcome+process。 |
| Video-Based Reward Modeling for Computer-Use Agents | 该文构建 ExeVR-53k，把 human demos、human-rated agent trajectories 与 rule-evaluated rollouts 汇成 video-task-reward triplets，并通过 adversarial instruction translation 合成困难负样本。训练方法是在 Qwen3-VL 上做 reward modeling fine-tuning，同时引入时空 token pruning 以处理长视频，并联合学习 holistic success judgment 与 first-failure attribution。训练后 Evaluator 学到的是对完整 computer-use 执行视频判断任务是否完成，并定位首个失误时间段的能力。其推理产物包含 success 或 failure 判断与时间区间式 attribution，下游用于替代手写脚本评价器，并支持 agent debugging 与 targeted data collection。 | outcome+process | scalar+non-scalar | GUI 与 computer-use | 主任务是 video-level success judgment，但同时训练 first-failure localization。时间区间是结构化非标量产物。 |
| I-FailSense: Towards General Robotic Failure Detection with Vision-Language Models | 该文把 CALVIN、AHA、DROID 等机器人数据中的视觉轨迹与语言目标转成 success 或 failure 样本，正例来自 expert demonstrations，负例主要通过目标错配构造。训练分两阶段进行，先对 VLM 做 LoRA 式 SFT，再训练附着在中间层上的 FailSense blocks，用 cross-entropy 与 BCE 学 failure detector。训练后 Evaluator 学到的是对整条机器人执行轨迹做成功或失败判别的能力，强调跨任务与跨失误类型泛化。其推理产物是 success 或 failure 的二值标签或概率，下游用于触发 recovery、reward shaping 或 subtask verification。 | outcome | scalar | embodied robotics |  |
| Generative Verifiers: Reward Modeling as Next-Token Prediction | 该文把 algorithmic reasoning 与 GSM8K 等任务中的问题、候选解答与正确性标签转成 verifier 训练经验，并为 CoT 版本额外合成 verification rationale。训练方法是把 reward modeling 改成 next-token prediction，用 SFT 学 Yes 或 No verdict，另有 unified loss 联合 solution generation 与 verification。训练后 Evaluator 学到的是对完整候选解答进行 correctness verification 的能力，既可直接输出 verdict token，也可在 CoT 版本中先给验证推理再给 verdict。其推理产物在 direct GenRM 中是可转成分数的 Yes token probability，在 GenRM-CoT 中是 rationale 加 verdict，下游用于 Best-of-N re-ranking 与 weighted self-consistency。 | outcome | scalar+non-scalar | reasoning math | direct verifier 与 CoT verifier 同时存在，故记为 scalar+non-scalar。 |
| Self-Generated Critiques Boost Reward Modeling for Language Models | 该文把 public preference corpora 与 synthetic math 或 safety preference data 结合起来，并让模型自生成 critique 作为 latent rationale，形成 prompt、chosen、rejected、critique 四元经验。训练方法是 Critic-RM 的联合目标，同时优化 critique generation loss 与 Bradley-Terry 风格 preference modeling loss，把自生成批注和偏好判断一起内化进 reward model。训练后 Evaluator 学到的是对完整回答给出连续 reward，同时生成解释性 critique 的能力。其推理产物既包括自然语言 critique，也包括连续标量分数，下游既可直接用于 RLHF 奖励，也可把 critique 用于纠错与 reasoning rectification。 | outcome | scalar+non-scalar | general |  |
| Enhancing Robotic Manipulation with AI Feedback from Multimodal Large Language Models | 该文从 Meta-World 收集不同训练阶段策略生成的 manipulation 视频轨迹，并用环境全信息脚本自动生成 pairwise analysis 与 preference result，把这些离散经验用来训练 CriticGPT。训练方法先对 LLaVA-1.5 做 LoRA fine-tuning 学习视觉比较与文字分析，再把 CriticGPT 产生的偏好反馈蒸馏成单独的 reward model 供 RL 使用。训练后核心 Evaluator 学到的是比较两条完整操作轨迹优劣并指出差异原因的能力。其推理产物是 analysis 文本加最终 preference judgment，下游一方面直接作为 AI feedback，另一方面被用来训练 dense scalar reward model 驱动 DrQ-v2。 | outcome | non-scalar | embodied robotics | 论文同时训练了下游 scalar reward model，但直接被经验更新以产生评判内容的核心 evaluator 是 CriticGPT。 |
| Let’s Verify Step by Step | 该文以 PRM800K 为核心经验源，样本来自 GPT-4 生成的数学解题过程，再由人工对每一步标注 positive、negative、neutral。训练方法是把每一步后的标签 token 作为监督目标，对 GPT-4 系模型做 process reward model fine-tuning，而不是只训练最终 outcome RM。训练后 Evaluator 学到的是对单个 reasoning step 输出正确性概率的能力，并能把整条解答按步评分。其推理产物是每步 scalar correctness probability，下游通过逐步分数乘积或聚合做 best-of-N 选择与过程监督。 | process | scalar | reasoning math |  |
| Improve Mathematical Reasoning in Language Models by Automated Process Supervision | 该文把 MATH 上大量模型 rollout 通过 OmegaPRM 变成自动 process labels，经验数据是问题、部分解答前缀与由 MCTS 加 binary search 定位得到的步骤正确性分数。训练方法比较 soft label pointwise、hard label pointwise 与 pairwise Bradley-Terry 三类目标，核心思想是用 rollout success ratio 自动估计每一步的价值。训练后 Evaluator 学到的是对单个 reasoning step 给出 scalar correctness 或 continuation success score 的能力。其推理产物是 step-level score，下游用于 PRM-weighted majority voting 与 self-consistency re-ranking。 | process | scalar | reasoning math |  |
| Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning | 该文把 prover policy 生成的 seed traces 与从各前缀展开的 Monte Carlo rollouts 作为经验，自动估计每个前缀的 future success probability 与 advantage。训练方法是把这些连续优势值离散成 buckets，训练 Process Advantage Verifier 以 cross-entropy 预测 step-level progress，而不是只判定最终答案对错。训练后 Evaluator 学到的是对每一步输出 promise 与 progress 信号的能力，本质上估计当前步骤给后续成功带来的边际提升。其推理产物是 scalar advantage 或 effective reward，下游既用于 beam search 和 reranking，也用于在线 RL 的 dense reward。 | process | scalar | reasoning math |  |
| Process Reward Model with Q-Value Rankings | 该文使用 Math-Shepherd 风格 reasoning trajectories 作为经验，并通过多次 completion 采样与 first-error 规则自动给每一步构造 Q-value 排名标签。训练方法不是普通 BCE，而是带 margin 的 comparative Q-value ranking loss，显式要求正确前缀的成功概率高于错误前缀。训练后 Evaluator 学到的是对单个 step 预测 future success probability 的能力，从而在错误刚出现处急剧降分。其推理产物是每步 scalar Q-value，下游用于 best-of-n trajectory selection 与 PRM-guided beam search。 | process | scalar | reasoning math |  |
| Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision | 该文把 PRM800K 人工标注轨迹与 RLHFlow Mistral 轨迹合并为经验，再用 DeepSeek-R1-Distill-Qwen-32B 给错误步骤补充 math error 与 consistency error 两层标签。训练方法是 hierarchical supervision，通过两阶段 token prediction 先预测错误类型，再预测最终 correctness reward，而不是只学单一正负标签。训练后 Evaluator 学到的是区分不同错误来源并输出更稳健 step reward 的能力。其推理产物包含离散 error-type 标签与最终 correctness score，下游主要消费 correctness 概率做 reward-guided search。 | process | scalar | reasoning math | 模型会输出结构化错误标签，但不生成自然语言解释，且下游主要使用数值 reward，因此记为 scalar。 |
| Better Process Supervision with Bi-directional Rewarding Signals | 该文从 MetaMath 采样大规模 reasoning trajectories，经验中既包含由 teacher 或自动方法标注的 step correctness，也包含用 MC 或 outcome estimation 得到的前向 value labels。训练方法是 BiRM 的联合 MSE 目标，把 backward-looking process reward 与 forward-looking value model 一起学习。训练后 Evaluator 学到的是既看当前步骤是否合理，也估计该前缀未来成功率的双向评估能力。其推理产物是组合后的 scalar score，下游用于 best-of-N、beam search、A star 与 MCTS 等推理搜索。 | process | scalar | reasoning math |  |
| AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress | 该文把 agent 在 web 等多步环境中的自采样 trajectories 作为经验，样本包含状态、动作、观察与最终 sparse success signal。训练方法用 TD 与 GAE 自动构造 step-wise Q 值和 advantage 伪标签，再用联合 MSE 同时学习 promise 与 progress 两个头。训练后 Evaluator 学到的是评估某一步动作长期成功潜力与局部推进程度的能力，而不只是终局成败。其推理产物是每步 scalar value，下游用于 Best-of-N、beam search 与 PPO 中的 dense reward。 | process | scalar | web |  |
| ProgRM: Build Better GUI Agents with Progress Rewards | 该文把 GUI agent 在 WikiHow 等环境中的 10438 条 trajectories 转成经验，并通过 LCS 匹配 recipe 的自标注算法找出 key steps，再为每一步分配归一化 progress label。训练方法是对 Progress Reward Model 做 BCE 训练，使其预测当前动作执行后在任务 recipe 中的进展位置。训练后 Evaluator 学到的是对 GUI 执行过程中的每一步给出 progress estimate 的能力。其推理产物是 0 到 1 的 scalar progress value，下游通过 progress gain 形式为 REINFORCE++ 提供 dense reward。 | process | scalar | GUI |  |
| Building Autonomous GUI Navigation via Agentic-Q Estimation and Step-Wise Policy Optimization | 该文把 GUI 环境中自生成的 state、thought、action、return 序列作为经验，并把每个中间步骤与其从终局 reward 反传得到的 return 对齐。训练方法是用 BCE 训练 Agentic-Q 预测 step-wise success probability，再在此基础上用 SWPO 配合 GRPO、RLOO 或 REINFORCE++ 做策略优化。训练后 Evaluator 学到的是对给定状态与候选动作估计任务完成概率的能力，本质是 step-level Q estimator。其推理产物是每步 scalar value，下游既用于动作过滤，也作为 dense reward 驱动 GUI policy learning。 | process | scalar | GUI | 监督虽然源自终局 success 或 failure，但被广播到每个步骤并显式训练 step-wise Q，因此归 process。 |
| GUI-Shepherd: Reliable Process Reward and Verification for Long-Sequence GUI Tasks | 该文把 AndroidWorld 在线 rollout 与 AndroidControl 离线状态汇成 52k GUI 交互经验，并由人工给每步动作打正负标签，再用 GPT-4o 生成解释性 rationale。训练方法是对 UI-TARS-1.5-7B 做 SFT，让模型学会 step-level verification；同时论文还研究 CoT verifier 变体，把推理与判定一并学进参数。训练后 Evaluator 学到的是对单步 GUI action 判对错并在部分设置下解释原因的能力。其推理产物既可以是 positive 或 negative 的 logit 或 label，也可以是 rationale 加最终判定，下游既能做 RL reward provider，也能做 inference-time verifier。 | process | scalar+non-scalar | GUI | 论文同时报告纯分数型 PRM 与带解释 verifier 变体，故记为 scalar+non-scalar。 |
| Advancing Mobile GUI Agents: A Verifier-Driven Approach to Practical Deployment | 该文把 Android 任务中的细粒度 step trajectories 与 self-correcting pairs 作为经验，初期由人工标注正确动作，后续轮次再用 verifier 预标并由人工校正。训练方法是 Pairwise Process Preference，也就是在每一步让正动作分数高于负动作，并用 Q-LoRA 微调 backbone 与评分头。训练后 Evaluator 学到的是对候选 GUI actions 做 step-level preference scoring 的能力，可在多个候选动作中选出最可能正确者。其推理产物是单个 scalar estimated score，下游直接用于 action extractor 之后的候选重排与执行选择。 | process | scalar | GUI |  |
| IntentScore: Intent-Conditioned Action Evaluation for Computer-Use Agents | 该文使用 AgentNet 的 398K 跨系统 GUI steps 作为经验，输入包含 screenshot、任务指令、动作历史、可执行代码以及 planning intent 文本。训练方法分为 contrastive alignment 与 margin ranking 两部分，让 state embedding 与正确 action embedding 更接近，同时把 intent 作为条件信息融入 action encoder。训练后 Evaluator 学到的是结合当前界面状态与候选动作意图来评估单步动作好坏的能力。其推理产物是 scalar reward score 或相似度分数，下游用于对生成器采样出的多个候选动作做 reranking。 | process | scalar | GUI 与 computer-use | intent 是输入条件，不是输出产物，因此不记为 non-scalar。 |
| GAIA: A Data Flywheel System for Training GUI Test-Time Scaling Critic Models | 该文把真实 GUI agents 在 AndroidControl 与 GUI-Odyssey 上的 step-level 操作记录转成 critic 训练经验，样本包含截图、指令、历史与候选动作，并通过对齐 ground truth 标出 correct 或 wrong。训练方法是先做 SFT 学 step-level binary critic，再用 flywheel 迭代让第一轮 critic 挖掘更难样本训练第二轮 critic。训练后 Evaluator 学到的是对单步 GUI action 做快速正确性判断的能力，而不依赖长篇推理。其推理产物是 correct 或 wrong 标签及其概率分数，下游通过 Best-of-N test-time scaling 过滤候选动作。 | process | scalar | GUI 与 computer-use | 论文强调 intuitive binary critic，概率由分类 token 读出，仍属 scalar。 |
| SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents | 该文从 SWE-Bench 真实 issue 与 mini-SWE-Agent 生成的代码修复 trajectories 中收集经验，记录 reasoning、tool use、文件编辑、测试结果等中间动作。训练方法用启发式给中间 actions 赋即时奖励，再折扣累积成 step-wise target，并以 qLoRA 加 MSE 训练 PRM。训练后 Evaluator 学到的是对代码 agent 每个候选 action 估计未来修复价值的能力。其推理产物是单步 scalar reward score，下游用于 reward-guided inference，在每步候选动作中选最高分继续执行。 | process | scalar | code |  |
| SAFE: Multitask Failure Detection for Vision-Language-Action Models | 该文把 simulated 与 real-world VLA rollouts 作为经验，输入含轨迹观测与策略内部 latent embedding，监督只需要整条轨迹是否失败这一粗粒度标签。训练方法分别用 MLP 的 L1 目标或 LSTM 的 BCE 目标，把 trajectory-level success 或 failure 内化为 failure score predictor。训练后 Evaluator 学到的是在执行过程中持续输出失败风险的能力，虽训练标签粗但推理时可逐时刻监测。其推理产物是每个时间步的 scalar failure likelihood，下游用 conformal threshold 触发 abort、backtrack 或 human intervention。 | outcome | scalar | embodied robotics | 训练标签只有 trajectory-level success 或 failure，因此按监督粒度记为 outcome。 |
| Towards Policy-Compliant Agents: Learning Efficient Guardrails For Policy Violation Detection | 该文基于 WebArena 上的 agent trajectories 构建 POLICYGUARDBENCH，经验数据是带 domain metadata 的完整操作序列与不同长度前缀，再由人工制定规范后用 gpt-oss-120B 批量标注 violation 或 no_violation。训练方法是对 Qwen3-4B-Instruct 做 full-parameter SFT，把 policy violation detection 训练成严格格式的二分类指令跟随任务。训练后 Evaluator 学到的是对完整轨迹或早期前缀判断是否已经违反政策的能力。其推理产物是 violation 或 no_violation 标签，下游作为轻量 guardrail 在 agent 运行中或运行后进行拦截与审查。 | outcome+process | scalar | web | 论文同时训练完整轨迹判定与 prefix early detection，故记为 outcome+process。 |
| AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation | 该文通过 FailGen 从 RLBench 成功 demonstration 程序化生成大量失败子任务，经验数据是相邻关键帧构成的 subtask 片段、二值成功条件与失败原因文本。训练方法是按照 LLaVA 指令微调范式做 autoregressive next-token 训练，让模型同时学 yes 或 no 判断与失败解释。训练后 Evaluator 学到的是对中间 manipulation subtask 判定是否成功并指出失败模式的能力。其推理产物是 yes 或 no 标签加自由文本 failure rationale，下游可用于 Eureka 奖励改写、TAMP 规划修正与 zero-shot subtask verification。 | process | non-scalar | embodied robotics | 虽然每次判定针对一个小 subtask 的结果，但它嵌在长程操作过程中，因而更适合记为 process。 |
| Self-Refining Vision Language Model for Robotic Failure Detection and Reasoning | 该文使用大规模 sparse 二值 failure labels 与较小规模 dense reasoning annotations 训练机器人失败检测器，并在 online refinement 阶段继续吸收模型自身 rollout 形成的新经验。训练方法分为 warm-up、expert-conditioned SFT 与在线 refinement，联合优化 BCE 的 detection head 和 next-token reasoning decoder。训练后 Evaluator 学到的是对整段机器人视频进行失败检测并给出文字化原因分析的能力，还能通过多轮自精炼提升置信度。其推理产物同时包含 binary failure label 与自然语言 rationale，下游可用于人工接管、reward shaping 与 corrective planning。 | outcome | scalar+non-scalar | embodied robotics | 判定目标是任务级 failure 或 success，但模型通过多轮 refinement 生成解释。 |
| OS-Oracle: A Comprehensive Framework for Cross-Platform GUI Critic Models | 该文把七个开源 GUI trajectory 数据集整合成 31 万 step-level 样本，正例是专家动作，负例由规则模拟四类常见错误动作合成。训练方法先做 SFT 学 reason 加 judgment，再用 CP-GRPO 以 accuracy、format 与 reasoning-consistency 奖励继续强化 critic。训练后 Evaluator 学到的是对单步 GUI action 做跨平台正确性验证并解释错误类型的能力。其推理产物是自然语言 rationale 与 Yes 或 No judgment，下游既可在执行前过滤错误动作，也可作为离线数据质量筛选器。 | process | non-scalar | GUI 与 computer-use |  |
| Look Before You Leap: A GUI-Critic-R1 Model for Pre-Operative Error Diagnosis in GUI Automation | 该文从公开 GUI 数据集提取正确操作作正例，并从开源 MLLM agents 采样错误操作作负例，再用 GPT-4o 做数据过滤，形成面向单步诊断的 critic 训练经验。训练方法先做 RFT cold-start，再用 Suggestion-aware GRPO 强化 correctness、reasoning 与 suggestion 质量。训练后 Evaluator 学到的是在动作执行前判断该步是否正确、指出可能原因并给出修正建议的能力。其推理产物包含 thinking 文本、0 到 1 correctness score 与 corrective suggestion，下游把这些反馈回送给 agent 做 action refinement。 | process | scalar+non-scalar | GUI |  |
| WebArbiter: A Principle-Guided Reasoning Process Reward Model for Web Agents | 该文使用 WEBPRM COLLECTION 中约 3 万个 step-level preference pair 作为经验，样本包含 instruction、observation、候选 action 及其 teacher rationale。训练分两阶段进行，先用 o3 生成的教师推理做 reasoning distillation，再用 GRPO 让最终 verdict 与 ground-truth correctness 对齐。训练后 Evaluator 学到的是对 web agent 单步候选动作归纳判断原则并据此做 preference judgment 的能力。其推理产物是显式 principle induction、structured justification 与最终 preference verdict，下游通过 knockout tournament 等机制在多个候选动作中选优。 | process | non-scalar | web |  |
| Web-Shepherd: Advancing PRMs for Reinforcing Web Agents | 该文构建 WEBPRM COLLECTION，经验数据来自 human expert trajectories、拒绝动作、checklists 以及 GPT-4o 生成的 checklist-level judgments 与 feedback。训练方法是在 MLLM 上做 next-token prediction，使模型给定 instruction、checklist 与 state-action pair 时生成反馈文本和 checklist judgment，并可再通过 verbalizer 转成 reward。训练后 Evaluator 学到的是按子目标分解 web 任务并对单步动作给出完成度判断与反馈的能力。其推理产物包括自然语言 feedback、各 checklist item 的 Yes 或 No 或 In Progress 判断，以及由 token probability 映射得到的 scalar reward，下游用于 reward-guided search、step-wise refinement 与 RL。 | process | scalar+non-scalar | web |  |
| SOLE-R1: Video-Language Reasoning as the Sole Reward for On-Robot Reinforcement Learning | 该文把真实与模拟机器人视频转为 120 万条 spatiotemporal CoT traces，经验数据通过几何距离、时间反转与偏离注入自动得到每时刻 progress supervision。训练方法先做 SFT 学结构化 reasoning 加 progress value，再用 RLVR 与 GRPO 继续优化进度判断精度。训练后 Evaluator 学到的是对机器人执行视频逐时刻解释当前状态并预测相对任务进展的能力。其推理产物是 think 区中的时空分析文本与 answer 区中的整数 progress score，下游把解析出的分数作为 on-robot RL 的唯一 dense reward，也可用来语义化 steering 预训练策略。 | process | scalar+non-scalar | embodied robotics | 文本 reasoning 是显式输出，但实际控制环主要消费其中的数值 progress。 |
| Hybrid Reward Normalization for Process-supervised Non-verifiable Agentic Tasks | 该文从真实多轮 search 型 agentic task 中采样约 2000 条轨迹，经验数据包含每轮 reasoning trace 与 search action，再由 GPT-4o 与 Qwen3-235B-A22B 按 correctness、relevance、consistency 等原则给 step-wise 分数。训练方法是对 PPRM 做 SFT，学习生成分析文本与标准化分数，并在策略优化时把 process reward 与 outcome reward 通过 ReNorm 混合。训练后 Evaluator 学到的是对不可验证 agentic 中间步骤做原则化评估并定量打分的能力。其推理产物是 Analysis 文本加结构化 final score，下游作为 PPO 中的 dense process reward 使用。 | process | scalar+non-scalar | general agentic | RL 中最终 reward 会把 outcome 信息广播到各步，但 evaluator 本身训练监督仍是 step-wise principle scores。 |
| No More Stale Feedback: Co-Evolving Critics for Open-World Agent Learning | 该文从 WebShop、ALFWorld、SciWorld 与 DeepSearch 的在线 rollouts 中构造经验，每个样本含初始轨迹、基线分数、多个 diagnostic critiques 与基于 critique 修正后的 refined trajectory。训练方法是 ECHO 的 dual-track GRPO，用 refined score 相对 baseline 的提升作为 critic 的 gain shaping 奖励，和 policy 一起协同进化。训练后 Evaluator 学到的是对完整 agent trajectory 生成高层诊断反馈并指出改进方向的能力。其推理产物是自然语言 diagnostic feedback，下游直接作为 conditional refinement 的指导信号，驱动 actor 生成更高回报的新轨迹。 | outcome | non-scalar | general agentic | critique 内容面向过程缺陷，但 critic 训练奖励来自整条 refined trajectory 的最终性能提升，因此按 outcome 记。 |
| Don’t Act Blindly: Robust GUI Automation via Action-Effect Verification and Self-Correction | 该文把 AndroidControl-High 中的成功轨迹和合成的 failure recovery 轨迹一起作为经验，其中负例通过制造 action 后界面无变化的假历史来教模型识别 false success。训练分两阶段进行，先做 robust SFT，再用 Verification-Action-Effect GRPO，以 action quality、effect honesty 与 verification accuracy 组成复合奖励。训练后 Evaluator 学到的是在每一步检查上一步动作是否真正产生预期效果，并在失败时给出诊断与修正线索的能力。其推理产物是带 Verify、Diagnose、Recall 标签的 reasoning 文本和 SUCCESS 或 NO_CHANGE verdict，下游据此触发 self-correction 与 recovery。 | process | non-scalar | GUI | 监督作用在每个 action-effect transition 上，尽管判的是上一步结果，仍属于 process-level verification。 |
| AgentV-RL: Scaling Reward Modeling with Agentic Verifier | 该文把 Polaris、DeepScaleR-40K、AReaL-boba-106k 等数据中的多轮 tool-augmented verification trajectories 作为经验，样本含 thoughts、Python actions、tool observations 与最终真假标签。训练方法先做 rejection fine-tuning 学高质量 verifier 轨迹，再用 GRPO 以最终 verdict 是否与 ground truth 一致作为 RL 奖励。训练后 Evaluator 学到的是对完整候选解答展开多轮工具验证并给出真假结论的能力。其推理产物是多轮 reasoning、可能的代码执行轨迹与最终 True 或 False verdict，下游既可做 Best-of-N verifier scoring，也可作为 critique model 指导 sequential refinement。 | outcome | non-scalar | reasoning | 训练奖励是整次 verification trajectory 的最终 verdict 正确性。论文也会用 True token logit 做排序，但模型对外产物仍是生成式验证过程。 |
| Teaching Language Models to Critique via Reinforcement Learning | 该文在 TACO 等代码任务上把问题、候选程序、模型生成 critique 与修复后程序表现组成经验，奖励由 sandbox 执行后的隐藏单测通过情况给出。训练方法先用 execution-guided synthetic critiques 做 SFT，再用 GRPO 直接优化 critique 使其更能帮助 generator 产出通过测试的新代码。训练后 Evaluator 学到的是对完整代码解答给出 structured critique、改进建议与 correctness judgment 的能力。其推理产物是分析文本、行动性建议与 Correct 或 Incorrect 标签，下游用于多轮 code refinement，也可作为 pairwise judge 使用。 | outcome | non-scalar | code | 虽然 critique 会谈及局部错误，但真正训练信号只看修复后最终代码是否通过测试。 |
| DeepCritic: Deliberate Critique with Large Language Models | 该文把 PRM800K 人工标签与 NuminaMath-CoT 自动标注样本转成 deliberate critique 训练经验，关键步骤是用 Monte Carlo 估计每一步后的成功率并定位 first error。训练分为 critique teaching 的 SFT 与 critique incentivization 的 GRPO 两阶段，让模型学会长程、多视角的 step-wise critique。训练后 Evaluator 学到的是对数学解题过程中每一步进行深度审查、标出首个错误并解释原因的能力。其推理产物是长文本 deliberate rationale、每步正负 judgment 与 first-error index，下游用于 majority voting verifier 与 critique-based refinement。 | process | non-scalar | reasoning math |  |
| Enhancing LLM Reasoning via Critique Models with Test-Time and Training-Time Supervision | 该文构建 MathCritique-76k，经验数据来自 GSM8K 与 MATH 上受控生成的 flawed reasoning paths，再由 GPT-4o 为首个错误步骤生成 critique，并通过 soft filtering 保留能真正帮助修正的样本。训练方法是对 critique model 做标准 SFT，使其输入问题与解答后输出 step-level labels 加 constructive feedback。训练后 Evaluator 学到的是识别首个出错步骤并生成可用于修正的批评信息的能力。其推理产物是 Correct 或 Wrong 风格的步骤判定与自然语言解释，下游既可在 test-time 做 conditional refinement，也可在 training-time 过滤和改写 actor 探索数据。 | process | non-scalar | reasoning math |  |
| StepWiser: Stepwise Generative Judges for Wiser Reasoning | 该文把 NuminaMath-CoT 中的中间 reasoning chunks 与从这些前缀展开的 Monte Carlo rollouts 作为经验，依据前后 Q-value 或 effective reward 的变化自动标出每个 chunk 是 positive 还是 negative。训练方法不是普通分类，而是用 GRPO 直接强化 judge 生成正确 stepwise verdict 与解释，使其学习 meta-reasoning。训练后 Evaluator 学到的是对单个 reasoning chunk 判断它是否提升后续成功率的能力。其推理产物是显式 rationale 加 boxed 的 Positive 或 Negative verdict，下游用于 chunk-reset 搜索与高质量训练数据筛选。 | process | non-scalar | reasoning math | verdict 本身可离散化，但论文有意保留 stepwise generative rationale，因此记为 non-scalar。 |
| RL4F: Generating Natural Language Feedback with Reinforcement Learning for Repairing Model Outputs | 该文在 summarization、action planning 与 alphabetization 任务上把输入、初始输出、真值、critic 生成的反馈以及修复后输出改进量组成经验，reward 取决于 refined output 相对 ground truth 的最终任务指标。训练方法先做 warm-start SFT，再用 PPO 直接优化 critique generator，使生成的自然语言反馈更能帮助固定 task model 修正答案。训练后 Evaluator 学到的是对完整模型输出生成可操作自然语言反馈的能力，而不是输出单一数值分。其推理产物是 critique 文本，下游把它作为 prompt 反馈给黑盒 task model 进行输出修复。 | outcome | non-scalar | general | 奖励只在终局 refined output 上计算，属于 outcome。 |