
## Parametric Evaluator-to-Policy Transformation

Parametric Evaluator-to-Policy Transformation 指的是将已经内化在参数化评估器中的评价经验转移到 policy 参数中的一类经验转化路径。这里的源载体是 evaluator parameter，例如 reward model、process reward model、verifier、critic、judge、value model、failure detector 或 multimodal evaluator；目标载体是 policy parameter，即 agent 在后续推理时用于生成动作的 actor / policy 权重。与 Tokenized-to-Policy Transformation 不同，P6 的监督源不是原始轨迹、人类示范、环境成功信号或规则化 verifier，而是某个参数化模型已经学习或具备的评价能力。换言之，P6 关注的是 evaluator 中的 preference、correctness criterion、quality judgment、risk assessment 或 process-level credit assignment 如何通过训练过程被 policy 吸收。

这一转化路径的关键特征是，评估器不只是被 agent 在推理时调用，而是通过训练信号持久性地影响 policy 参数。若一个 reward model、LLM-as-a-judge、VLM judge、critic 或 verifier 只在 decoding、reranking、tree search、best-of-N selection 或 MCTS 中作为推理时控制器使用，而 policy 权重没有被该信号更新，则它属于 evaluator utilization，而不是 P6。相反，只要 evaluator 的输出被转化为 reward、preference pair、advantage、penalty、filtered trajectory、critique target 或 distillation data，并进一步用于更新 policy 参数，就构成 evaluator-to-policy transformation。

本文不按照 PPO、GRPO、DPO、SFT、RFT 或 actor-critic 等训练算法来组织 P6 方法，因为同一种 evaluator feedback 可以被不同训练接口消费，而同一种训练算法也可能接收不同形态的 evaluator signal。相反，本文按照 evaluator 产出的主要反馈形态来划分 P6 方法：Outcome Feedback-to-Policy Transfer 关注完整输出或完整轨迹的总体评价如何进入 policy；Process Feedback-to-Policy Transfer 关注中间步骤、动作、prefix 或 token 的局部评价如何进入 policy；Diagnostic Feedback-to-Policy Transfer 关注解释、批评、修正建议和失败诊断如何被 policy 吸收；Evaluator–Policy Co-Evolution 则关注 evaluator 本身随 agent 新经验持续刷新、重训或共同演化的复合流程。

这种划分的核心依据不是 evaluator 的表面名称，而是它在训练管线中产生并传递给 policy 的主要经验产物。例如，LLM-as-a-judge 既可以给完整 response 打分，也可以评价中间步骤，还可以生成自然语言 critique；reward model 既可以输出 trajectory-level reward，也可以被改造成 token-level dense reward；critic 既可以输出 scalar value，也可以生成 natural-language future summary。因此，同一个 evaluator 类型可能出现在不同方法类中。本文将一篇方法归入哪一类，取决于真正驱动 policy improvement 的主要 feedback artifact，而不是 evaluator backbone 或训练算法的名称。


### Outcome Feedback-to-Policy Transfer

Outcome Feedback-to-Policy Transfer 指的是 evaluator 主要对完整输出、完整 response、完整 trajectory 或完整 episode 进行评价，并将这种 outcome-level feedback 转移到 policy 参数中的方法。这里的 evaluator 可以是 trained reward model、holistic reward model、LLM-as-a-judge、VLM judge、generative reward model、preference model 或 mixture of judges。它们的共同点在于，评估对象主要是一次完整行为的最终质量，而不是具体某一步动作或某个中间 reasoning prefix。

这类 evaluator 的输出可以表现为 scalar reward、trajectory-level score、response-level quality rating、pairwise preference、chosen / rejected label、success likelihood 或 holistic critique score。随后，这些 outcome-level signals 可以通过多种训练接口进入 policy：在 RLHF 或 RLAIF 风格方法中，它们通常作为 PPO、GRPO、REINFORCE、SAC 或其他 policy-gradient objective 的 reward；在 preference optimization 方法中，它们可以被转化为 DPO、IPO、KTO、ORPO、SimPO 或 online DPO 所需的 preference pairs；在 filtered distillation 方法中，它们也可以用于筛选高分轨迹，再通过 SFT 或 rejection fine-tuning 更新 policy。

这类方法的基本思想是，参数化评估器已经从人类偏好、AI feedback、历史成功样本、教师模型输出或大规模预训练中获得了对“什么是好输出”的判断能力。通过让 policy 在训练过程中最大化、模仿或偏向 evaluator 所偏好的完整行为，policy 可以在无需推理时调用 evaluator 的情况下内化这些评价标准。例如，在通用 RLHF 中，reward model 对完整 response 进行评分，policy 通过强化学习逐渐生成更符合 reward model 偏好的输出；在 LLM-as-a-judge 设定中，强模型对候选 trajectory 或 GUI action 进行比较，较弱 agent 再通过 DPO 或 RL 将这些判断转化为自身行为能力。

Outcome Feedback-to-Policy Transfer 的优势是形式简单、适配性强，并且容易与现有 RLHF、RLAIF、DPO 和 rejection sampling 框架结合。对于任务目标可以通过最终结果判断的场景，例如开放式回答质量、工具调用成功率、GUI 任务完成度、search agent 最终答案质量或 embodied trajectory 成功程度，outcome feedback 往往提供了足够直接的优化信号。相比人工逐步标注，trajectory-level 或 response-level evaluator 也更容易规模化。

然而，这类方法的局限也很明显。由于 evaluator 只评价完整结果，它往往无法告诉 policy 中间哪一步导致了成功或失败，因而在长轨迹、强交互、多工具调用或多轮 reasoning 任务中容易面临 credit assignment 问题。一个完整 trajectory 的低分可能由错误的搜索查询、无效的工具调用、遗漏的约束检查或最后一步 reasoning mistake 导致，但 outcome-level feedback 本身并不区分这些原因。此外，当 policy 反复优化同一个 imperfect evaluator 时，还可能出现 reward hacking、Goodhart over-optimization、length bias exploitation、judge bias amplification 或 reward model distribution shift。因而，Outcome Feedback-to-Policy Transfer 通常需要 KL regularization、reward filtering、judge deconflicting、reward model routing、ensemble evaluator 或 evaluator refresh 等机制来提升稳定性。

这一路径与 Process Feedback-to-Policy Transfer 的区别在于，前者的主要监督对象是完整行为结果，而后者的主要监督对象是中间过程。即使最终训练算法同样是 PPO、GRPO 或 DPO，只要 evaluator 的核心反馈产物是 response-level score 或 trajectory-level preference，就应归入 Outcome Feedback-to-Policy Transfer。相反，如果 evaluator 明确对 step、turn、prefix、token、state-action pair 或 search round 给出局部评价，则应归入 Process Feedback-to-Policy Transfer。

论文：
- Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards
- Reinforcement Learning from Meta-Evaluation: Aligning Language Models Without Ground-Truth Labels
- Policy Filtration for RLHF to Mitigate Noise in Reward Models
- Reward Model Routing in Alignment
- The Perfect Blend: Redefining RLHF with Mixture of Judges
- Robust Preference Optimization through Reward Model Distillation
- DPO Learning with LLMs-Judge Signal for Computer Use Agents

### Process Feedback-to-Policy Transfer

Process Feedback-to-Policy Transfer 指的是 evaluator 主要评价 agent 轨迹中的中间步骤、局部动作、reasoning prefix、tool-use step、search round、dialogue turn、token 或 state-action pair，并将这种 process-level feedback 转移到 policy 参数中的方法。这里的 evaluator 可以表现为 process reward model、step-level judge、verifier、turn-wise critic、value model、prefix scorer、action evaluator、token-level reward allocator 或 contribution estimator。与 outcome-level evaluator 不同，它们试图回答的不是“整个输出是否好”，而是“哪一步是好的、哪一步是错的、哪一段中间行为对最终成功有贡献”。

这类方法的核心动机是解决长程 agent 学习中的 credit assignment 问题。在复杂 agent 任务中，最终成功或失败往往由多个中间决策共同决定。对于 search agent，关键可能在于某一轮检索是否提供了有用证据；对于 GUI agent，关键可能在于某一次点击是否推进了任务状态；对于 reasoning agent，关键可能在于某个推理 prefix 是否首次偏离正确路径；对于 multi-agent collaboration，关键可能在于某一轮交互是否提供了有效协作信息。仅依赖最终 reward 会使 policy 很难知道应该强化或避免哪些局部行为，而 process-level evaluator 可以提供更细粒度的训练信号。

Process Feedback-to-Policy Transfer 的 feedback artifact 可以有多种形式。最直接的是 step-level score 或 process reward，即 evaluator 对每个 reasoning step、tool call 或 action 给出局部质量判断。另一类是 first-error localization，即 evaluator 找出推理链或行动序列中最早出错的位置，并据此惩罚后续错误 prefix 或奖励更长的正确 prefix。还有一类是 contribution weight，即 evaluator 不直接决定 reward，而是估计每个中间步骤对最终 outcome reward 的贡献，再将最终 advantage 重新分配到各个步骤。此外，trained critic 或 value model 可以为中间状态估计 future return，从而提供 turn-level advantage 或 state-level value target；某些方法还会将 trajectory-level reward 通过 attention、saliency 或 value decomposition 转化为 token-level dense reward。

这类方法可以通过不同训练接口更新 policy。如果 evaluator 输出 dense process reward，它可以直接进入 PPO、GRPO、REINFORCE 或 actor-critic objective；如果 evaluator 输出 step-level preference，它可以进入 step-DPO、stepwise SimPO 或其他 preference optimization objective；如果 evaluator 输出局部错误诊断，它也可以被转化为 penalty、mask、weight 或 filtered training target。无论具体算法如何，关键在于 evaluator 的主要作用是把原本稀疏的 outcome feedback 分解为过程级监督，使 policy 能够学习到局部决策与长期结果之间的关系。

Process Feedback-to-Policy Transfer 的主要优势在于，它更适合长轨迹、强交互和多阶段任务。对于 reasoning、search、web navigation、GUI automation、tool-use、multi-turn collaboration 和 embodied control 等任务，中间行为的质量往往比最终结果更能揭示 agent 的能力结构。过程反馈不仅可以提高样本效率，还可以降低“答案正确但过程错误”或“最终失败但局部策略有效”所造成的错误监督。尤其在 all-negative group 或 sparse reward setting 中，process-level evaluator 可以为仍未成功的 trajectories 提供 partial credit，从而避免 policy 完全无法学习。

但这一类方法也带来新的风险。首先，process-level feedback 的质量高度依赖 evaluator 是否真的理解任务过程。如果 evaluator 对中间步骤的判断不可靠，错误的 dense reward 可能比稀疏 reward 更有害。其次，过程监督容易诱发 process reward hacking：policy 可能学会生成看似合理、能骗过 step judge 的中间过程，而不真正提升任务成功率。再次，step-level annotation 或 PRM training 的成本通常高于 outcome-level scoring，尤其在 GUI、web、robotics 和 multi-agent 场景中，中间状态本身可能具有多模态、部分可观测和强上下文依赖的特点。因此，许多方法并不直接最大化 process reward，而是将它作为 advantage redistribution、flawed trajectory penalty、partial-progress signal 或 auxiliary constraint 使用。

这一路径与 Outcome Feedback-to-Policy Transfer 的区别在于反馈粒度。只要 evaluator 的核心贡献是定位、评价或加权中间步骤，即使最终仍然使用 outcome reward、GRPO 或 DPO 进行训练，也应归入 Process Feedback-to-Policy Transfer。相反，如果 step-level 信息只是为了汇总出一个最终 trajectory score，而 policy 实际只接收完整轨迹偏好，则更适合归入 Outcome Feedback-to-Policy Transfer。

论文：
- FAPO: Flawed-Aware Policy Optimization for Efficient and Reliable Reasoning
- SWEET-RL: Training Multi-Turn LLM Agents on Collaborative Reasoning Tasks
- Stepwise Guided Policy Optimization: Coloring Your Incorrect Reasoning in GRPO
- Dense Reward for Free in Reinforcement Learning from Human Feedback
- Enhancing LLM-based Search Agents via Contribution Weighted Group Relative Policy Optimization
- TGPO: Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning


### Diagnostic Feedback-to-Policy Transfer

Diagnostic Feedback-to-Policy Transfer 指的是 evaluator 主要输出解释性、诊断性、批评性、修正性或风险说明形式的反馈，并将这些 diagnostic feedback 转移到 policy 参数中的方法。与 Outcome Feedback 和 Process Feedback 主要提供“好不好”或“哪一步好不好”的评价不同，Diagnostic Feedback 更关注“为什么不好”“哪里出了问题”“应该如何修改”“当前策略存在什么风险”以及“后续应该采用什么替代行为”。

这类 evaluator 的输出通常不是简单 scalar reward 或 pairwise label，而是 natural-language critique、failure explanation、error analysis、refinement suggestion、risk rationale、rubric-based comments、hindsight feedback、corrected step、revised trajectory、action directive 或 future summary。它们可能由 prompted LLM-as-a-critic、fine-tuned generative judge、natural-language critic、rubric evaluator、self-refinement model、failure diagnosis model 或 multimodal critique model 生成。与前两类相比，Diagnostic Feedback-to-Policy Transfer 更强调 evaluator 将其评估能力外显为可读、可解释、可修正的 tokenized artifact，然后 policy 再通过训练吸收这些诊断性经验。

这类方法的基本思想是，单纯的 reward 或 preference 有时不足以表达复杂 agent 任务中的失败原因。对于 web agent，失败可能来自网页状态理解错误、工具选择错误、检索证据不足或目标约束遗漏；对于 code agent，失败可能来自接口误用、测试覆盖不足或隐含依赖错误；对于 embodied agent，失败可能来自视觉 grounding、动作时序或物理约束误判。若 evaluator 能够生成“错误原因”和“修正方向”，policy 就不只是学习偏好排序，而是获得了更具结构的信息。这些诊断性反馈可以作为 SFT target、revision target、critique-conditioned training data、preference construction basis 或 reward shaping source，最终被写入 policy 参数。

Diagnostic Feedback-to-Policy Transfer 的训练接口可以有多种形式。一种常见方式是 evaluator 先对失败轨迹生成 critique 或 refinement，再将修正后的 trajectory 作为 supervised target 训练 policy。另一种方式是将 diagnostic feedback 与原始 trajectory 拼接，训练 policy 在类似状态下生成更合适的 action 或 reasoning step。还有一些方法会让 evaluator 生成 rubric-based explanation 或 failure labels，然后将这些诊断信息转化为 preference pairs、filtered datasets 或 auxiliary loss。对于 natural-language actor-critic 类方法，critic 甚至可以用自然语言描述未来风险、状态价值或改进行动，使 policy 学习到比 scalar value 更丰富的经验表示。

这类方法的优势是信息密度高、可解释性强，并且更适合错误类型复杂、任务空间开放的 agent 场景。相比只告诉 policy 某条轨迹分数低，diagnostic feedback 可以指出失败原因，从而减少错误归因。它也有助于跨任务迁移：某些失败诊断，如“未验证工具返回结果”“忽略用户约束”“过早停止搜索”“没有检查执行结果”，可能在不同任务中重复出现，因而比单个 trajectory reward 更具有抽象复用价值。

但是，Diagnostic Feedback-to-Policy Transfer 也面临更强的可靠性问题。自然语言 critique 可能听起来合理但实际上错误，refinement suggestion 可能与环境真实反馈不一致，risk rationale 也可能反映 evaluator 的偏见而非任务事实。如果 policy 直接模仿错误诊断，可能会把 evaluator 的幻觉或偏见内化进自身行为。此外，diagnostic feedback 的表达通常较长，训练成本高，并且需要额外机制判断哪些 critique 真正有用。因此，在高风险任务中，diagnostic feedback 往往需要与环境验证、程序执行、human audit、self-consistency 或 evaluator ensemble 结合使用。

Diagnostic Feedback-to-Policy Transfer 与 Process Feedback-to-Policy Transfer 容易重叠，因为许多诊断本身是针对中间步骤产生的。本文的判定原则是：如果 evaluator 的核心产物是局部 score、step reward、first-error index 或 contribution weight，则归入 Process Feedback；如果 evaluator 的核心产物是自然语言解释、批评、修正建议、失败原因或风险理由，并且这些文本性诊断被训练管线直接消费，则归入 Diagnostic Feedback。换言之，Process Feedback 强调“局部评价”，Diagnostic Feedback 强调“解释与修正”。

论文：
- AdaRubric: Task-Adaptive Rubrics for LLM Agent Evaluation
- SRR-Judge: Step-Level Rating and Refinement for Enhancing Search-Integrated Reasoning in Search Agents
- Training Agents with Weakly Supervised Feedback from Large Language Models
- Natural Language Actor-Critic: Scalable Off-Policy Learning in Language Space
- OpenClaw-RL: Train Any Agent Simply by Talking

### Evaluator–Policy Co-Evolution

Evaluator–Policy Co-Evolution 指的是 evaluator 与 policy 在同一学习闭环中随 agent 新经验持续更新、刷新、重训或共同演化的一类复合方法。前三类方法通常默认 evaluator 在 policy update 期间相对固定，或者至少 evaluator 的构建不是主要贡献；而在这一类方法中，evaluator 本身的动态变化就是方法核心。它不再只是一个静态监督源，而是随着 policy 产生的新 trajectories、失败模式、分布漂移和环境反馈不断调整自身评价能力。

这类方法通常包含一个循环结构：当前 policy 与环境交互产生新的 trajectories；evaluator 对这些 trajectories 进行评分、比较、诊断或筛选；policy 根据 evaluator feedback 更新；更新后的 policy 产生新的经验分布；evaluator 又基于这些新经验被刷新、重训、校准或扩展。根据具体设计，evaluator 可以是 reward model、critic、judge、PRM、discriminator、self-rewarding model 或 mixture of evaluators。其更新方式也可能不同：有的方法在 on-policy samples 上重新训练 reward model，有的方法交替训练 discriminator 与 generator，有的方法让 critic 随 agent 新失败模式持续进化，还有的方法让同一个模型同时扮演 policy 和 evaluator，形成 self-rewarding loop。

Evaluator–Policy Co-Evolution 的核心动机是缓解 static evaluator 在长期 policy improvement 中的失效问题。当 policy 被反复优化时，它会逐渐偏离 reward model 或 judge 最初见过的数据分布。此时，固定 evaluator 可能出现 reward overestimation、blind spot、stale feedback 或被 policy exploited 的漏洞。通过让 evaluator 随 policy-generated experience 更新，系统可以在一定程度上保持 feedback 与当前 policy distribution 的匹配，使 evaluator 能继续识别新的错误模式、新的 reward hacking 策略或新的任务能力边界。

这类方法可以表现为多种具体模式。第一种是 reward model refresh，即在 policy 新生成的数据上持续校准或更新 RM，以减少 distribution shift。第二种是 critic-policy co-evolution，即 critic 随 actor 变化不断学习新的 value、advantage 或 failure patterns，并继续指导 actor。第三种是 self-rewarding loop，即模型自身生成候选答案、评价候选答案、构造偏好数据，并用这些偏好继续更新自身。第四种是 search-evaluate-distill pipeline，即 evaluator 先指导搜索或筛选高质量 trajectories，再将这些经验蒸馏回 policy；若搜索、评价和训练反复迭代，也属于 co-evolutionary pipeline。第五种是 environment–policy–reward joint optimization，即环境生成、任务分布、reward model 和 policy 都在同一系统中动态变化。

Evaluator–Policy Co-Evolution 的优势是适合开放世界、长周期和持续学习场景。在这些场景中，agent 的能力、任务分布和失败模式都会随训练发生变化，静态 evaluator 很难长期保持有效。共同演化机制可以让 evaluator 不断吸收新的 agent experience，并把更新后的评价标准再次传回 policy，从而形成更强的经验循环。这一点对于 web agent、GUI agent、tool-use agent、self-improving agent、open-world embodied agent 和 multi-agent 系统尤其重要，因为这些任务中的环境状态、工具组合和错误模式往往高度动态。

然而，这类方法也带来更复杂的稳定性风险。由于 evaluator 和 policy 同时变化，系统可能出现 feedback drift、self-confirmation bias、reward model collapse、critic overfitting 或 evaluator-policy collusion。特别是在 self-rewarding setting 中，模型可能逐渐强化自身偏见，而不是接近真实任务目标。如果 evaluator 的更新缺乏外部锚点，如 human preference、environment verification、held-out benchmark、rule-based constraint 或 independent judge，co-evolution 可能放大错误评价。因此，这类方法通常需要额外的稳定化机制，例如 frozen reference evaluator、periodic human audit、ensemble judges、conservative update、KL constraint、external validation set 或 uncertainty-aware reward modeling。

严格来说，Evaluator–Policy Co-Evolution 并不是与前三类完全同维度的单步 P6 方法，而是 P6 的复合扩展。前三类描述的是 evaluator feedback 以何种产物形态进入 policy；本类描述的是 evaluator 本身是否在经验循环中持续变化。因此，当一篇论文只是使用固定 PRM 或 LLM judge 给 policy 提供过程反馈时，应归入 Process Feedback-to-Policy Transfer；当它的核心贡献是 PRM、judge 或 critic 会随 policy 新经验不断刷新时，则应归入 Evaluator–Policy Co-Evolution。对于同时包含 evaluator construction、feedback generation、policy update 和 evaluator refresh 的方法，本文将其视为 composite pipeline，并在 P6 章节中作为 evaluator-to-policy transfer 的动态扩展进行讨论。

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

## Parametric-to-Tokenized Experience Transformation

第七类转化路径是 Parametric-to-Tokenized Experience Transformation，即将已经内化在参数化模型权重中的经验外化为可被其他系统消费的 token-level artifacts。这里的参数化源可以是 policy model、teacher foundation model、LLM / VLM / MLLM / VLA agent，也可以是 reward model、verifier、critic、judge 等 evaluator model。与 Tokenized-to-Parametric 路径相反，P7 的方向不是把离散经验写入模型参数，而是从模型参数中“读出”可复用的经验表达。

在 LLM-based agent 场景中，P7 的目标通常不是生成一次性回答，而是生成可以被另一个 student model、retrieval store、agent system、verifier 或下游训练管线继续消费的 tokenized artifacts。这些 artifacts 可以表现为 agent trajectories、tool-use demonstrations、GUI action traces、RAG reasoning paths、function-calling dialogues、step-level labels、critiques、verification traces 或 preference annotations 等。换言之，P7 将模型权重中隐式保存的任务执行能力或评估能力外化为可存储、可筛选、可训练、可检索或可组合的数据资源。

这一类转化路径需要与普通 inference、self-training loop 以及 P1/P2 路径区分开来。普通 inference 中，模型生成的 CoT 或答案仅服务于当前 query，缺乏独立归档和复用意图，因此不构成 P7。Self-training 或 iterative bootstrapping 中，模型自身生成的 rollouts 被同一训练循环中的后继版本直接消费，这更接近 composite pipeline，而非独立的 Parametric-to-Tokenized pathway。P1/P2 则以已有 logs、trajectories 或 demonstrations 为主要输入，由模型对具体轨迹进行摘要、反思、重写或形式化；P7 的关键在于源经验主要来自参数化模型已经内化的能力，而不是来自某条已存在的 agent trajectory。

我们按照外化 artifact 在下游系统中的主要消费角色，将 P7 方法划分为两类：Demonstration Externalization 和 Evaluative Supervision Externalization。前者外化的是“如何行动”的经验，即 policy 或 teacher model 的决策能力；后者外化的是“如何评价”的经验，即 evaluator 或 judge model 的评估能力。二者分别对应 agent experience 中 action-oriented knowledge 与 evaluation-oriented knowledge 的 token-level externalization。

---

### Demonstration Externalization

Demonstration Externalization 指的是参数化 policy、teacher foundation model 或 teacher agent 将其隐式决策能力外化为可供 student agent 模仿学习的行为示范。这类方法的目标 artifact 通常是 agent trajectories、task demonstrations、tool-use dialogues、web / GUI / mobile interaction traces、function-calling records、RAG reasoning-action paths 或 code / tool execution traces。下游 consumer 通常通过 SFT、behavioral cloning、distillation 或 imitation-style training 学习这些示范数据，从而获得相应的 agentic behavior。

这一类方法的基本思想是：强模型或 teacher agent 已经在参数中内化了一定的任务执行能力，但这些能力如果只停留在模型权重中，就难以被小模型、专用 agent 或独立系统直接复用。因此，Demonstration Externalization 通过任务提示、环境交互、tool schema、GUI state、retrieval context 或 seed instruction 诱导 teacher model 产生完整的行为过程，将“模型会做什么”转化为“学生可以学习的数据”。在这个意义上，示范轨迹是 policy knowledge 的 tokenized read-out。

典型流程可以概括为：首先由模型或系统生成任务、目标或环境初始状态；随后由 teacher policy 在环境中执行多步推理和动作，形成包含 observation、thought、action、tool call、GUI operation、retrieval step 或 final response 的轨迹；最后通过 execution checking、LLM-as-a-judge、rule-based validation、trajectory filtering、step-level filtering 或 human screening 等机制筛除低质量数据。经过筛选后的轨迹被物化为训练语料，用于训练 student agent 或增强下游 agent 的任务执行能力。

这一类方法覆盖了多种 agent 设定。在 web agent 和 computer-use agent 中，外化 artifact 通常是浏览器或 GUI 环境中的多步操作轨迹，例如点击、输入、滚动、导航和读取结果。在 tool-use 或 function-calling agent 中，示范数据表现为多轮用户请求、assistant reasoning、API selection、function arguments、tool responses 和 final answer。在 RAG agent 中，外化 artifact 则包括问题分解、检索动作、证据选择、中间推理和最终回答。虽然这些任务领域不同，但它们共享同一个转化逻辑：将 teacher model 的隐式行动能力外化为 action-bearing trajectories。

Demonstration Externalization 的优势在于可扩展性和低人工成本。相比人工标注多步 agent trajectories，强模型可以在大量环境、任务和工具集合上自动生成示范，从而缓解 agent training data 的稀缺问题。特别是在 web navigation、GUI automation、tool use 和 mobile control 等场景中，人工收集高质量轨迹成本很高，而 teacher-generated demonstrations 可以快速扩大训练覆盖面。此外，模型生成的数据可以通过 task diversity control、multi-teacher mixing、curriculum sampling、difficulty-aware generation 或 environment-mediated synthesis 扩展到更多任务分布。

不过，这一类方法也面临明显风险。首先，teacher-generated trajectories 可能包含 hallucinated actions、不可执行步骤、错误 tool arguments 或伪成功轨迹。如果缺乏可靠验证，student 会继承 teacher 的错误行为。其次，单一 teacher 或单一 prompt 生成的数据可能导致 distribution narrowing，使 student 过度拟合 teacher 的表达风格和决策偏好。第三，对于 long-horizon agent tasks，完整轨迹的成功与否并不能直接说明每个中间动作的质量，错误可能在后续步骤中才暴露。因此，Demonstration Externalization 通常需要与 execution-based verification、fine-grained filtering、diversity-promoting generation 和 curriculum design 结合使用。

在分类上，RAGShaper、EviPath 等 evidence-grounded 方法仍可归入 Demonstration Externalization。虽然它们的生成过程受到 evidence、retrieval context、information tree 或 sub-question dependency 的约束，但下游消费的主要 artifact 仍然是可训练的 reasoning-action trajectory。同样，UI simulator、mock world 或 executable environment 在某些方法中也可能参与数据生成，但如果最终被 student 直接消费的是 trajectories、dialogues 或 demonstrations，则这些环境构造更适合作为示范轨迹外化的生成机制，而不是单独的一级方法家族。

因此，Demonstration Externalization 可以被概括为：从 policy 或 teacher model 的参数化决策能力中外化可模仿的行为经验。它回答的问题是：模型已经会做某类任务，如何把这种能力转化为其他 agent 可以学习的示范数据？

论文：
- Explorer: Scaling Exploration-driven Web Trajectory Synthesis for Multimodal Web Agents
- Towards Internet-Scale Training For Agents
- RAGShaper: Eliciting Sophisticated Agentic RAG Skills via Automated Data Synthesis
- Structured Distillation of Web Agent Capabilities Enables Generalization
- TOUCAN: Synthesizing 1.5M Tool-Agentic Data from Real-World MCP Environments
- From Evidence to Trajectory: Abductive Reasoning Path Synthesis for Training Retrieval-Augmented Generation Agents
- LLMs as Scalable, General-Purpose Simulators For Evolving Digital Agent Training
- FABRIC: Framework for Agent-Based Realistic Intelligence Creation
- Mock Worlds, Real Skills: Building Small Agentic Language Models with Synthetic Tasks, Simulated Environments, and Rubric-Based Rewards
- SynthAgent: Adapting Web Agents with Synthetic Supervision
- AgentSynth: Scalable Task Generation for Generalist Computer-Use Agents
- Fara-7B: An Efficient Agentic Model for Computer Use
- ToolMind Technical Report: A Large-Scale, Reasoning-Enhanced Tool-Use Dataset
- ASTRA: Automated Synthesis of agentic Trajectories and Reinforcement Arenas
- OpenMobile: Building Open Mobile Agents with Task and Trajectory Synthesis
- Learning with Challenges: Adaptive Difficulty-Aware Data Generation for Mobile GUI Agent Training
- APIGen-MT: Agentic Pipeline for Multi-Turn Data Generation via Simulated Agent-Human Interplay
- ToolAlpaca: Generalized Tool Learning for Language Models with 3000 Simulated Cases
- APIGen: Automated Pipeline for Generating Verifiable and Diverse Function-Calling Datasets
- ToolACE: Winning the Points of LLM Function Calling

---

### Evaluative Supervision Externalization

Evaluative Supervision Externalization 指的是参数化 evaluator、judge、verifier、critic 或 reward model 将其隐式评估能力外化为 token-level supervision，并将这些监督信号提供给其他 student model、agent system、data filtering pipeline 或 reward-model training process 使用。不同于 Demonstration Externalization 主要外化“如何行动”的行为知识，这类方法外化的是“如何判断行动质量”的评价知识。

这类方法的目标 artifact 可以包括 critiques、step-level labels、action correctness annotations、progress labels、preference pairs、verification traces、failure diagnoses、repair suggestions、trajectory refinement comments 或 reward-model training data。它们可以是自然语言形式的 critique，也可以是结构化标签、局部动作评分、步骤级 pass/fail 判断、候选轨迹排序，或者带有理由说明的 preference annotation。只要 evaluator 的输出被物化为可复用 token-level artifact，并被另一个系统消费，就属于这一类。

这一类方法的基本思想是：许多强模型不仅能够执行任务，也能够判断一个 agent 的行为是否合理、某一步动作是否有效、某条轨迹是否完成目标、某个 tool call 是否参数正确，或者某个中间推理是否偏离证据。Evaluative Supervision Externalization 将这种评估能力从模型权重中外化出来，形成比 scalar reward 更丰富的监督数据。下游系统可以用这些数据过滤 demonstrations、训练 verifier、构造 reward model、指导 student agent 学习，或者为失败轨迹提供可修正的诊断信息。

这一类方法需要与 P6 区分开来。P6 的核心是 Parametric Evaluator-to-Policy alignment，即 evaluator 的 reward、preference 或 critique 直接参与 policy 的优化，使 policy 参数发生更新。Evaluative Supervision Externalization 则强调 evaluator 的输出被显式物化为 tokenized artifacts，并且这些 artifacts 可以脱离原 evaluator 被其他系统复用。例如，一个 judge 对每个 GUI action 生成 step-level correctness label，并将这些 labels 组成独立训练集，用于训练 student agent 或 step reward model，这属于 P7；如果 judge 只在同一个 RL loop 中给当前 policy 一个 scalar reward，则更接近 P6，而不是 P7。

这一类方法也需要与普通数据过滤区分开来。许多 Demonstration Externalization 方法都会使用 judge 或 verifier 删除低质量轨迹，但如果 judge 的输出只作为内部过滤开关，并没有作为独立监督数据被保存或消费，那么它只是质量控制机制，而不是 Evaluative Supervision Externalization。只有当 evaluator 的判断本身成为可复用 artifact，例如 graded steps、progress annotations、verification traces、critiques 或 preference rationales，才应将其作为这一类方法的核心。

Evaluative Supervision Externalization 的优势在于能够缓解长程 agent 任务中的 credit assignment 问题。对于 web navigation、GUI automation、tool use、software engineering 和 embodied control 等任务，完整 trajectory 的成功或失败往往不足以说明每一步动作的局部价值。步骤级 labels、action-level critiques 或 progress annotations 可以提供更细粒度的学习信号，使 student 不只是模仿整条轨迹，而是知道哪些中间动作是正确的、哪些动作导致偏离目标、哪些失败轨迹仍然包含可利用的局部步骤。因此，这类方法特别适合与 noisy teacher rollouts、partially successful trajectories 和 large-scale synthetic demonstrations 结合。

此外，Evaluative Supervision Externalization 可以提高 synthetic data pipeline 的数据利用率。传统 trajectory-level filtering 往往将整条失败轨迹直接丢弃，即使其中包含大量正确中间步骤。通过 step-level evaluation，方法可以从失败轨迹中保留局部正确动作，或者为错误步骤生成诊断和修正建议。这使得 evaluator 不只是数据筛选器，而成为新的经验外化源：它把自身对行为质量的判断转化为可训练的评价经验。

不过，这一类方法也存在局限。首先，evaluator 本身可能存在系统性偏差，错误的 step labels 或 critique 会误导 student。其次，LLM-as-a-judge 在复杂环境中的判断并不总是可靠，尤其是当任务成功条件依赖隐式状态、外部工具结果或视觉细节时。第三，细粒度标注虽然提供更强监督，但会显著增加计算成本和 pipeline 复杂度。因此，实际系统通常需要结合 execution-based checking、rule-based validation、multi-judge agreement、calibration、human audit 或 consistency verification 来控制 evaluator-generated supervision 的质量。

总体而言，Evaluative Supervision Externalization 可以被概括为：从 evaluator model 的参数化评估能力中外化可复用的评价经验。它回答的问题是：模型已经能够判断任务执行质量，如何把这种判断能力转化为其他 agent 可以学习、过滤或验证的监督数据？

论文：
- Scalable Data Synthesis for Computer Use Agents with Step-Level Filtering
- Scaling Web Agent Training through Automatic Data Generation and Fine-grained Evaluation
- ToolMind Technical Report: A Large-Scale, Reasoning-Enhanced Tool-Use Dataset（secondary；若其 turn-level filtering / validation labels 被作为监督信号保留）
- Structured Distillation of Web Agent Capabilities Enables Generalization（secondary；其 judge / evaluation hints 可作为评估监督外化的辅助例子）
- TOUCAN: Synthesizing 1.5M Tool-Agentic Data from Real-World MCP Environments（secondary；其 model-based validation 更主要是质量控制机制）
- 
---

### 小结：行动经验与评价经验的外化

上述两类方法共同构成 P7 路径中的核心组织方式。Demonstration Externalization 将 policy 或 teacher model 的决策能力外化为 trajectories 和 demonstrations，强调“应该如何行动”；Evaluative Supervision Externalization 将 evaluator 或 judge model 的评估能力外化为 labels、critiques 和 verification traces，强调“如何判断行动质量”。前者主要服务于 student agent 的行为模仿与能力蒸馏，后者主要服务于数据筛选、细粒度监督、verifier 训练和 agent 行为改进。

这两类方法并非在实际系统中完全孤立。许多 agent data synthesis pipeline 会同时包含 teacher rollout 和 evaluator filtering：teacher model 先生成候选 trajectories，judge model 再对这些 trajectories 进行验证、打分或步骤级标注。在这种情况下，主分类应取决于论文的核心贡献和最终被下游消费的主要 artifact。如果主要贡献是生成可模仿的 trajectories，则归入 Demonstration Externalization；如果主要贡献是将 evaluator 的判断外化为可复用监督，则归入 Evaluative Supervision Externalization。

除了这两个主类之外，P7 方法还存在若干横向设计维度，例如 environment-mediated synthesis、multi-teacher mixing、curriculum control、difficulty-aware sampling、execution-based verification、step-level filtering、human-in-the-loop screening 和 multimodal grounding。这些机制通常不构成独立的外化目标，而是影响外化 artifact 的质量、规模、多样性和可验证性。因此，在综述组织上，它们更适合作为跨方法家族的设计轴进行讨论，而不是作为一级分类。
