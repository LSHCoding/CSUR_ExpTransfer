## Parametric Evaluator-to-Policy Transformation

Parametric Evaluator-to-Policy Transformation 将已内化在参数化评估器中的评价经验转移到 policy 参数中。源载体是 evaluator parameter：reward model、process reward model、verifier、critic、judge、value model、failure detector 或 multimodal evaluator；目标载体是 policy parameter，即 agent 在后续推理时用于生成动作的 actor / policy 权重。与 Tokenized-to-Policy Transformation 不同，P6 的监督源不是原始轨迹、人类示范、环境成功信号或规则化 verifier，而是某个参数化模型已学习或具备的评价能力。P6 关注的是 evaluator 中的 preference、correctness criterion、quality judgment、risk assessment 或 process-level credit assignment 如何通过训练被 policy 吸收。

这一转化路径的关键特征是，评估器不只是被 agent 在推理时调用，而是通过训练信号持久性地影响 policy 参数。若一个 reward model、LLM-as-a-judge、VLM judge、critic 或 verifier 只在 decoding、reranking、tree search、best-of-N selection 或 MCTS 中作为推理时控制器使用，而 policy 权重未被该信号更新，则它属于 evaluator utilization，而非 P6。只要 evaluator 的输出被转化为 reward、preference pair、advantage、penalty、filtered trajectory、critique target 或 distillation data 并用于更新 policy 参数，就构成 evaluator-to-policy transformation。

本文按 evaluator 产出的主要反馈形态来划分 P6 方法：Outcome Feedback-to-Policy Transfer 关注完整输出或完整轨迹的总体评价如何进入 policy；Process Feedback-to-Policy Transfer 关注中间步骤、动作、prefix 或 token 的局部评价如何进入 policy；Diagnostic Feedback-to-Policy Transfer 关注解释、批评、修正建议和失败诊断如何被 policy 吸收；Evaluator–Policy Co-Evolution 关注 evaluator 本身随 agent 新经验持续刷新、重训或共同演化的复合流程。

这一划分的核心依据不是 evaluator 的表面名称，而是它在训练管线中产生并传递给 policy 的主要经验产物。LLM-as-a-judge 既可为完整 response 打分，也可评价中间步骤，还可生成自然语言 critique；reward model 既可输出 trajectory-level reward，也可被改造成 token-level dense reward；critic 既可输出 scalar value，也可生成 natural-language future summary。同一 evaluator 类型可能出现在不同方法类中。本文将一篇方法归入哪一类，取决于真正驱动 policy improvement 的主要 feedback artifact，而非 evaluator backbone 或训练算法的名称。


### Outcome Feedback-to-Policy Transfer

Outcome Feedback-to-Policy Transfer 指 evaluator 主要对完整输出、完整 response、完整 trajectory 或完整 episode 进行评价，并将 outcome-level feedback 转移到 policy 参数中。evaluator 可以是 trained reward model、holistic reward model、LLM-as-a-judge、VLM judge、generative reward model、preference model 或 mixture of judges。共同点是评估对象为一次完整行为的最终质量，而非具体某一步动作或某个中间 reasoning prefix。

这类 evaluator 的输出表现为 scalar reward、trajectory-level score、response-level quality rating、pairwise preference、chosen / rejected label、success likelihood 或 holistic critique score。这些 outcome-level signals 可通过多种训练接口进入 policy：在 RLHF 或 RLAIF 风格方法中作为 PPO、GRPO、REINFORCE、SAC 或其他 policy-gradient objective 的 reward；在 preference optimization 方法中转化为 DPO、IPO、KTO、ORPO、SimPO 或 online DPO 所需的 preference pairs；在 filtered distillation 方法中用于筛选高分轨迹，再通过 SFT 或 rejection fine-tuning 更新 policy。

参数化评估器已从人类偏好、AI feedback、历史成功样本、教师模型输出或大规模预训练中获得对”什么是好输出”的判断能力。让 policy 在训练中最大化、模仿或偏向 evaluator 所偏好的完整行为，policy 便可在无需推理时调用 evaluator 的情况下内化这些评价标准。通用 RLHF 中，reward model 对完整 response 评分，policy 通过强化学习逐渐生成更符合 reward model 偏好的输出；LLM-as-a-judge 设定中，强模型对候选 trajectory 或 GUI action 进行比较，较弱 agent 再通过 DPO 或 RL 将这些判断转化为自身行为能力。

Outcome Feedback-to-Policy Transfer 的优势是形式简单、适配性强，易与现有 RLHF、RLAIF、DPO 和 rejection sampling 框架结合。对于可通过最终结果判断的任务目标——开放式回答质量、工具调用成功率、GUI 任务完成度、search agent 最终答案质量或 embodied trajectory 成功程度——outcome feedback 提供了足够直接的优化信号。相比人工逐步标注，trajectory-level 或 response-level evaluator 也更容易规模化。

局限同样明显。evaluator 只评价完整结果，往往无法告诉 policy 中间哪一步导致了成功或失败，在长轨迹、强交互、多工具调用或多轮 reasoning 任务中面临 credit assignment 问题。完整 trajectory 的低分可能来自错误搜索查询、无效工具调用、遗漏的约束检查或最后一步 reasoning mistake，但 outcome-level feedback 本身不区分这些原因。当 policy 反复优化同一个 imperfect evaluator 时，还可能出现 reward hacking、Goodhart over-optimization、length bias exploitation、judge bias amplification 或 reward model distribution shift。Outcome Feedback-to-Policy Transfer 通常需要 KL regularization、reward filtering、judge deconflicting、reward model routing、ensemble evaluator 或 evaluator refresh 等机制提升稳定性。

这一路径与 Process Feedback-to-Policy Transfer 的区别在于：前者主要监督完整行为结果，后者主要监督中间过程。即使训练算法同为 PPO、GRPO 或 DPO，只要 evaluator 的核心反馈产物是 response-level score 或 trajectory-level preference，就归入 Outcome Feedback-to-Policy Transfer；若 evaluator 明确对 step、turn、prefix、token、state-action pair 或 search round 给出局部评价，则归入 Process Feedback-to-Policy Transfer。

论文：
- Constitutional AI: Harmlessness from AI Feedback [Bai22b]
- RLAIF vs. RLHF: Scaling Reinforcement Learning from Human Feedback with AI Feedback [Lee23b]
- Direct Language Model Alignment from Online AI Feedback [Guo24]
- Self-Rewarding Language Models [Yua24]
- RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment [Don23]
- BOND: Aligning LLMs with Best-of-N Distillation [Ses24]
- BoNBoN Alignment for Large Language Models and the Sweetness of Best-of-n Sampling [Gui24]
- Meta-Rewarding Language Models: Self-Improving Alignment with LLM-as-a-Meta-Judge [Wu24d]
- Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards [Ack26]
- Reinforcement Learning from Meta-Evaluation: Aligning Language Models Without Ground-Truth Labels [Ren26b]
- Policy Filtration for RLHF to Mitigate Noise in Reward Models [She24c]
- Reward Model Routing in Alignment [Wu25x]
- The Perfect Blend: Redefining RLHF with Mixture of Judges [Xu24d]
- Robust Preference Optimization through Reward Model Distillation [Fis24]
- DPO Learning with LLMs-Judge Signal for Computer Use Agents [Luo25f]

```
### Outcome Feedback-to-Policy Transfer

Outcome Feedback-to-Policy Transfer 的核心脉络，是将 parametric evaluator 对完整 response 或完整 trajectory 的总体判断，转化为可持续更新 policy 权重的训练信号。在这一方向上，研究并非简单沿着 reward model、judge 或 DPO 等表面术语展开，而是逐步回答三个更本质的问题：谁来替代人类给出 outcome-level judgment，这种 judgment 如何从推理时控制转化为训练时监督，以及当 policy 持续优化 evaluator 信号时如何抑制噪声、偏置与过优化。

这一范式首先由 AI feedback 替代 human feedback 的工作确立。[Bai22b] 用 constitution-guided AI feedback 对完整 responses 做偏好判断，并进一步训练 preference model，再通过 RLAIF 将 harmlessness judgment 吸收到 policy 中；[Lee23b] 则系统比较 RLHF 与 RLAIF，说明 off-the-shelf LLM 既可先提供偏好数据来训练 reward model，也可在 d-RLAIF 中直接对完整输出打 outcome-level 分数并驱动 RL 更新。沿着这一路线，outcome evaluator 不再只是对生成结果做离线打分，而成为 policy post-training 中可替代人类监督的参数化经验来源。

在此基础上，一部分工作把 evaluator-to-policy transfer 推向更强的在线化与自举化。[Guo24] 让 LLM annotator 在线比较当前 policy 生成的完整 responses，并在 on-policy 分布上直接构造 chosen-rejected pairs 供 DPO、IPO 或 SLiC 更新 policy；[Yua24] 更进一步让同一模型同时充当 generator 与 judge，对多个完整候选答案自评分后再以 iterative DPO 回灌到自身 policy 中；[Wu24d] 在此之上加入 meta-judge，使 judge 的评分质量本身也能被迭代改进，从而形成 actor、judge、meta-judge 共同演化的 outcome feedback loop；[Luo25f] 则把这一机制具体落到 computer-use 场景中，用 GPT-4o 对完整候选操作结果打分，再将所得 preference pairs 用于训练 UI-TARS-2B，体现了 outcome-level judge signal 向具身 agent policy 的直接迁移。

另一条重要路线并不强调在线 RL，而是把 evaluator 对完整结果的偏好直接编译为可蒸馏的训练目标。[Don23] 的 RAFT 用 reward model 对多个完整候选输出做 outcome ranking，仅保留高分样本进行 SFT，从而以 filtered distillation 的方式写入 policy；[Ses24] 的 BOND 试图把推理时的 Best-of-N selection distill 为单次采样 policy，通过分布匹配让模型吸收 reward model 所支持的 outcome-level selection behavior；[Gui24] 的 BoNBoN 则进一步从理论上刻画 Best-of-n 分布，并结合 SFT-BoN 与 IPO-BoN 将最好样本和最差样本共同纳入训练；[Fis24] 则显式训练 reward model，并将其 reward difference 直接蒸馏到 policy 的隐式 reward 结构中，说明 evaluator-to-policy transfer 并不必然依赖经典 RL，而也可以通过 reward-surface distillation 来完成。

随着这一路线成熟，研究重点开始从“如何拿到 evaluator”转向“如何避免 policy 过度利用 evaluator”。[Ack26] 将 reward hacking 解释为 policy 对 proxy reward 尖锐高点的利用，并通过 gradient regularization 稳定 outcome-level RL 更新；[She24c] 观察到 reward model 在中等分数区域往往更不可靠，因此提出 policy filtration，只让最可信的高分或低分样本进入训练；[Wu25x] 不再假设单一 evaluator 足够稳健，而是用 Bayesian router 在多个 trained reward models 间按 query 动态选路，再将 routed preference pairs 用于 online DPO；[Xu24d] 则以 Mixture of Judges 的形式，把多个 judges 对完整生成结果的约束判断注入不同 policy optimization 接口，使 policy 学到的是多源 evaluator 共同裁决后的 outcome preference；[Ren26b] 更进一步表明，即使没有 ground-truth labels，也可以通过 meta-questions 让 LLM evaluator 对完整 responses 的目标答案概率形成 scalar reward，并经由 CISPO 一类 GRPO 变体转化为 policy update。由此，Outcome Feedback-to-Policy Transfer 已从早期的单一路径 reward maximization，发展为一个包含 AI feedback、在线偏好构造、Best-of-N distillation，以及 evaluator routing 与 stabilization 的完整方法谱系。
```

### Process Feedback-to-Policy Transfer

Process Feedback-to-Policy Transfer 指 evaluator 主要评价 agent 轨迹中的中间步骤、局部动作、reasoning prefix、tool-use step、search round、dialogue turn、token 或 state-action pair，并将 process-level feedback 转移到 policy 参数中。evaluator 可表现为 process reward model、step-level judge、verifier、turn-wise critic、value model、prefix scorer、action evaluator、token-level reward allocator 或 contribution estimator。与 outcome-level evaluator 不同，它们回答的不是”整个输出是否好”，而是”哪一步好、哪一步错、哪一段中间行为对最终成功有贡献”。

核心动机是解决长程 agent 学习中的 credit assignment 问题。复杂 agent 任务中，最终成败往往由多个中间决策共同决定。search agent 的关键可能在某一轮检索是否提供了有用证据；GUI agent 的关键可能在某一次点击是否推进了任务状态；reasoning agent 的关键可能在某个推理 prefix 是否首次偏离正确路径；multi-agent collaboration 的关键可能在某一轮交互是否提供了有效协作信息。仅依赖最终 reward 使 policy 很难知道应强化或避免哪些局部行为，process-level evaluator 则提供更细粒度的训练信号。

feedback artifact 有多种形式。最直接的是 step-level score 或 process reward，evaluator 对每个 reasoning step、tool call 或 action 给出局部质量判断。另一类是 first-error localization，evaluator 找出推理链或行动序列中最早出错的位置，据此惩罚后续错误 prefix 或奖励更长的正确 prefix。还有 contribution weight，evaluator 估计每个中间步骤对最终 outcome reward 的贡献，将最终 advantage 重新分配到各步骤。此外，trained critic 或 value model 可为中间状态估计 future return，提供 turn-level advantage 或 state-level value target；某些方法还会将 trajectory-level reward 通过 attention、saliency 或 value decomposition 转化为 token-level dense reward。

这类方法可通过不同训练接口更新 policy。若 evaluator 输出 dense process reward，可直接进入 PPO、GRPO、REINFORCE 或 actor-critic objective；若输出 step-level preference，可进入 step-DPO、stepwise SimPO 或其他 preference optimization objective；若输出局部错误诊断，可转化为 penalty、mask、weight 或 filtered training target。关键在于 evaluator 的主要作用是把原本稀疏的 outcome feedback 分解为过程级监督，使 policy 学习局部决策与长期结果之间的关系。

Process Feedback-to-Policy Transfer 更适合长轨迹、强交互和多阶段任务。reasoning、search、web navigation、GUI automation、tool-use、multi-turn collaboration 和 embodied control 等任务中，中间行为质量往往比最终结果更能揭示 agent 的能力结构。过程反馈不仅提高样本效率，还可降低”答案正确但过程错误”或”最终失败但局部策略有效”所造成的错误监督。在 all-negative group 或 sparse reward setting 中，process-level evaluator 可为仍未成功的 trajectories 提供 partial credit，避免 policy 完全无法学习。

但这类方法也带来新风险。process-level feedback 的质量高度依赖 evaluator 是否真正理解任务过程——若对中间步骤的判断不可靠，错误的 dense reward 可能比稀疏 reward 更有害。过程监督容易诱发 process reward hacking：policy 可能学会生成看似合理、能骗过 step judge 的中间过程，而不真正提升任务成功率。step-level annotation 或 PRM training 的成本通常高于 outcome-level scoring，在 GUI、web、robotics 和 multi-agent 场景中，中间状态本身可能具有多模态、部分可观测和强上下文依赖的特点。许多方法并不直接最大化 process reward，而是将其作为 advantage redistribution、flawed trajectory penalty、partial-progress signal 或 auxiliary constraint 使用。

这一路径与 Outcome Feedback-to-Policy Transfer 的区别在于反馈粒度。只要 evaluator 的核心贡献是定位、评价或加权中间步骤，即使最终使用 outcome reward、GRPO 或 DPO 训练，也归入 Process Feedback-to-Policy Transfer。若 step-level 信息只为汇总出一个最终 trajectory score，而 policy 实际只接收完整轨迹偏好，则归入 Outcome Feedback-to-Policy Transfer。

论文：
- FAPO: Flawed-Aware Policy Optimization for Efficient and Reliable Reasoning
- SWEET-RL: Training Multi-Turn LLM Agents on Collaborative Reasoning Tasks
- Stepwise Guided Policy Optimization: Coloring Your Incorrect Reasoning in GRPO
- Dense Reward for Free in Reinforcement Learning from Human Feedback
- Enhancing LLM-based Search Agents via Contribution Weighted Group Relative Policy Optimization
- Hybrid Reward Normalization for Process-supervised Non-verifiable Agentic Tasks
- Building Autonomous GUI Navigation via Agentic-Q Estimation and Step-Wise Policy Optimization
- OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards

```

Process Feedback-to-Policy Transfer 的共同目标，是把 evaluator 对中间决策质量的判断转化为可持久吸收到 policy 参数中的训练信号，从而缓解长轨迹 agent learning 中最核心的 credit assignment 难题。这一路径并不依赖单一的 evaluator 形态，而是沿着几条相对稳定的方法脉络展开：一类方法首先显式识别推理过程中的局部错误，再把这种错误定位能力写入 policy update；另一类方法直接学习 step-wise 或 turn-wise 的价值判断，使 policy 在交互过程中获得局部行为与最终成败之间的更细粒度映射；还有一类方法并不单独训练新的 process supervisor，而是从既有 reward model 或 critic framework 中提取隐含的局部评价结构，再将其重写为 dense training signal。

第一类方法主要出现在 reasoning policy optimization 中，核心是让 evaluator 不只判断“答对没有”，而是判断“从哪里开始错了”。[Din25b] 训练一个 generative reward model 来识别 answer-correct but process-flawed 的轨迹，并定位 first incorrect step，再将这种 flawed-positive diagnosis 写入 GRPO 的 penalty 设计，使 policy 在维持 outcome correctness 的同时压制不可靠的中间推理模式。[Che25v] 则用 step-wise judge 顺序检查 reasoning trajectory，将正确前缀长度转化为 Reasoning Trajectory Score，并用它替代 GRPO 对错误样本统一置零的粗粒度处理；这样即使在 all-negative groups 中，policy 也能从“哪条错误轨迹更接近正确路径”这一过程差异中获得有效更新信号。

第二类方法更直接地把 evaluator 学成局部价值函数，并将其作为 policy improvement 的核心接口。[Zho25p] 在 multi-turn collaborative reasoning agent 中训练一个 turn-level critic，并利用 training-time privileged information 直接学习每轮 action 的 advantage；随后该 critic 被用来对候选动作排序、构造 chosen and rejected pairs，再通过 DPO 将这种 turn-wise credit assignment 蒸馏进 policy。[Xu25h] 面向 non-verifiable 的 multi-turn search setting，引入 principle-based process reward model，对每个 turn 的 correctness、relevance 与 coherence 进行评分，并通过 ReNorm 将 process reward 与 sparse outcome reward 统一校准后送入 GAE 和 PPO。[Wan26s] 则在 GUI agent 中训练 Agentic-Q evaluator，对 state-action pair 估计 future return，再把这种 step-wise value feedback 接入 Step-Wise Policy Optimization，使 policy 学到哪些局部 GUI 操作真正推动了后续任务完成。[Wan26ac] 处于这一脉络的边界位置：它不训练独立的 critic，而是用 LLM judge 从 retrieval utility 与 reasoning correctness 两个维度估计各搜索轮次的 contribution，并据此重分配 trajectory-level GRPO advantage；尽管 evaluator 更接近 frozen judge，但其方法实质上同样是在把 round-level process judgment 内化为 policy improvement 的局部更新信号。

第三类方法展示了 process feedback 不一定要来自显式的 step supervisor，也可以从已有 evaluator 的内部结构或更复杂的 critic system 中被“解包”出来。[Cha24b] 并不额外构造 process labels，而是直接利用 Transformer reward model 在最终打分时的 attention-based credit attribution，将 sequence-level scalar reward 分解为 token-level dense rewards，并把这些局部评价信号送入 PPO 式 RLHF，从而把 reward model 中隐含的 fine-grained judgment 吸收到 policy 权重中。[Li26p] 则把长程 GUI trajectory 分解为一系列 milestones，并通过 selector, verifier, reviewer 和 judge 组成的 critic framework 对中间进展进行逐步验证与校准，再将这些 milestone-level judgments 汇总为 online RL 的 reward signal；相较于前述方法，它更像 system-level critic，但仍然体现了同一核心机制，即 policy 的改进不再仅由最终成败驱动，而是由 evaluator 对中间过程结构的判断持续塑形。

```

### Diagnostic Feedback-to-Policy Transfer

Diagnostic Feedback-to-Policy Transfer 指 evaluator 主要输出解释性、诊断性、批评性、修正性或风险说明形式的反馈，并将这些 diagnostic feedback 转移到 policy 参数中。与 Outcome Feedback 和 Process Feedback 主要提供”好不好”或”哪一步好不好”的评价不同，Diagnostic Feedback 更关注”为什么不好””哪里出了问题””应该如何修改””当前策略存在什么风险”以及”后续应采用什么替代行为”。

这类 evaluator 的输出通常不是简单 scalar reward 或 pairwise label，而是 natural-language critique、failure explanation、error analysis、refinement suggestion、risk rationale、rubric-based comments、hindsight feedback、corrected step、revised trajectory、action directive 或 future summary。它们可由 prompted LLM-as-a-critic、fine-tuned generative judge、natural-language critic、rubric evaluator、self-refinement model、failure diagnosis model 或 multimodal critique model 生成。与前两类相比，Diagnostic Feedback-to-Policy Transfer 更强调 evaluator 将其评估能力外显为可读、可解释、可修正的 tokenized artifact，然后 policy 再通过训练吸收这些诊断性经验。

单纯的 reward 或 preference 有时不足以表达复杂 agent 任务中的失败原因。web agent 的失败可能来自网页状态理解错误、工具选择错误、检索证据不足或目标约束遗漏；code agent 的失败可能来自接口误用、测试覆盖不足或隐含依赖错误；embodied agent 的失败可能来自视觉 grounding、动作时序或物理约束误判。若 evaluator 能生成”错误原因”和”修正方向”，policy 获得的就不只是偏好排序，而是更具结构的信息。这些诊断性反馈可作为 SFT target、revision target、critique-conditioned training data、preference construction basis 或 reward shaping source，最终写入 policy 参数。

训练接口有多种形式：evaluator 先对失败轨迹生成 critique 或 refinement，再将修正后的 trajectory 作为 supervised target 训练 policy；将 diagnostic feedback 与原始 trajectory 拼接，训练 policy 在类似状态下生成更合适的 action 或 reasoning step；让 evaluator 生成 rubric-based explanation 或 failure labels，然后将诊断信息转化为 preference pairs、filtered datasets 或 auxiliary loss。natural-language actor-critic 类方法中，critic 可用自然语言描述未来风险、状态价值或改进行动，使 policy 学习到比 scalar value 更丰富的经验表示。

这类方法的优势是信息密度高、可解释性强，更适合错误类型复杂、任务空间开放的 agent 场景。相比只告诉 policy 某条轨迹分数低，diagnostic feedback 可指出失败原因以减少错误归因，也有助于跨任务迁移——“未验证工具返回结果””忽略用户约束””过早停止搜索””没有检查执行结果”等诊断可能在不同任务中重复出现，比单个 trajectory reward 更具抽象复用价值。

但可靠性问题也更突出。自然语言 critique 可能听起来合理但实际错误，refinement suggestion 可能与环境真实反馈不一致，risk rationale 可能反映 evaluator 的偏见而非任务事实。若 policy 直接模仿错误诊断，可能将 evaluator 的幻觉或偏见内化进自身行为。diagnostic feedback 表达通常较长，训练成本高，需要额外机制判断哪些 critique 真正有用。在高风险任务中，diagnostic feedback 往往需要与环境验证、程序执行、human audit、self-consistency 或 evaluator ensemble 结合使用。

Diagnostic Feedback-to-Policy Transfer 与 Process Feedback-to-Policy Transfer 容易重叠——许多诊断本身针对中间步骤产生。本文的判定原则是：若 evaluator 的核心产物是局部 score、step reward、first-error index 或 contribution weight，归入 Process Feedback；若核心产物是自然语言解释、批评、修正建议、失败原因或风险理由，且这些文本性诊断被训练管线直接消费，归入 Diagnostic Feedback。Process Feedback 强调”局部评价”，Diagnostic Feedback 强调”解释与修正”。

论文：
- AdaRubric: Task-Adaptive Rubrics for LLM Agent Evaluation
- SRR-Judge: Step-Level Rating and Refinement for Enhancing Search-Integrated Reasoning in Search Agents
- Training Agents with Weakly Supervised Feedback from Large Language Models
- Natural Language Actor-Critic: Scalable Off-Policy Learning in Language Space
- OpenClaw-RL: Train Any Agent Simply by Talking
- Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training
- AgentRefine: Enhancing Agent Generalization through Refinement Tuning
- No More Stale Feedback: Co-Evolving Critics for Open-World Agent Learning
- Autonomous Evaluation and Refinement of Digital Agents
- Policy Improvement using Language Feedback Models

```
在 Diagnostic Feedback-to-Policy Transfer 中，评估器的核心作用不再只是输出 outcome-level reward 或 step-level score，而是将失败原因、修正方向与行为建议外显为可读的诊断性反馈，再通过 refinement tuning、distillation 或 critic-guided policy optimization 将这些信息持久写入 policy 参数。与仅在 decoding、reranking 或 tree search 阶段提供控制信号的 evaluator utilization 不同，这一路径要求 evaluator 产生的 critique、revision 或 hindsight guidance 被训练管线直接消费，并最终转化为 actor 的参数化能力。[Zha26am, Hon25c, Wan26ad, Yua25c, Fu25d, Li26l]

一类代表性方法直接围绕局部决策诊断与在线修正展开。[Zha26am] 面向 search agent 的每个 thought-action step 同时生成评分、错误解释以及 refined thought 和 refined action，并将这些修正后的高质量轨迹用于多轮 rejection-sampling fine-tuning。其关键不在于 judge 参与推理时打分，而在于 step-wise 的诊断与修正被重写为可训练轨迹，从而使 policy 内化“哪里错了以及应如何改”的搜索行为。[Hon25c] 则以 natural-language critic 取代传统 scalar critic，先预测某个动作可能导向的未来 rollout，再生成带理由的 textual critique 和 optimality judgment，并据此产生 refined action 蒸馏回基础 policy。这里 critic 提供的不是抽象 value，而是关于失败机理与改进行动的语言化解释，因此策略改进体现为诊断信息向 policy 权重的直接迁移。[Wan26ad] 进一步将这一思路扩展到真实交互环境：该方法从 next-state signal 中抽取 hindsight hints，把环境回应中的纠错信息转化为 concise action directives，再通过 Hindsight-Guided On-Policy Distillation 将“带 hint 的 teacher 分布”压入原始 policy，使 conversational correction 成为 token-level directional update，而非一次性的外部提示。

另一类工作将失败轨迹系统地改写为带反思或修正信号的训练样本，再以监督学习将这些诊断性经验写入策略。[Yua25c] 通过搜索树中的分叉结构定位 failed trajectory 的 first error step，并在错误前缀与正确后续之间插入 revision signal，构造显式的 reflection-plus-revision training instances。模型随后经由迭代 SFT 学会在多轮交互中主动识别错误并切换到修正后的行动路径，因此 evaluator 所提供的并非简单偏好排序，而是具有时序定位能力的失败诊断与恢复信号。[Fu25d] 采用相近但更偏环境化的设计：它构造 multi-turn error-refine trajectories，由强模型扮演的 Dungeon Master 针对 parameter error、logical error 与 location error 给出诊断性反馈，并展示后续 refined action。训练时错误步骤被保留在上下文中但不参与监督，只有修正步骤参与参数更新，因此 policy 学到的是“在收到诊断后如何纠正”，而不是仅仅模仿成功轨迹。

更进一步，[Li26l] 展示了 diagnostic transfer 与 evaluator–policy co-evolution 的结合形态。该方法训练一个与 actor 同步演化的 linguistic critic，为开放世界 agent 的失败轨迹生成简短但高信息量的 natural-language critiques，并据此诱导 refined trajectories。由于 critic 与 actor 在同一学习循环中共同更新，diagnostic feedback 不再来自静态 evaluator，而是随 agent 能力提升持续刷新，从而缓解了 critic staleness 导致的反馈失真问题；就本综述的划分而言，这类方法既是 Diagnostic Feedback-to-Policy Transfer 的强实例，也可视为 evaluator–policy co-evolution 的前沿形态。[Li26l]

相较之下，一些边界案例虽包含诊断性 evaluator，但其训练接口并未完整保留 critique 本身。[Pan24b] 使用 multimodal evaluator 对数字 agent 的轨迹或单步行为给出 success、failure、progress 判断，并常伴随自然语言 reasoning；然而在参数更新阶段，方法主要利用 evaluator 过滤出的高质量 state-action pairs 进行 behavior cloning，诊断文本更多用于 test-time reflection，因此更适合作为边界案例。[Zho24e] 先让强 LLM 生成 productive step 判断、原因解释与 strategy advice，再将其蒸馏为较小的 Language Feedback Model，以识别 desirable actions 并支持离线 imitation learning；这里 policy 主要吸收的是经 evaluator 过滤后的行为数据，而不是 critique 文本本身。[Din26e] 也体现出类似特征：虽然其 task-adaptive rubrics 为 agent 轨迹提供了多维诊断结构，并通过 DimensionAwareFilter 构造更可靠的 preference pairs，但真正进入 DPO 或 PPO 的主要仍是结构化 score 与 filtering outcome，因此更接近 diagnostic-structured supervision，而非典型的 critique-to-policy transfer。[Pan24b, Zho24e, Din26e]

总体来看，这一方向的关键趋势是：评估器不再只回答“好不好”，而是 increasingly 以自然语言或修正轨迹的形式回答“为什么不好”以及“应如何改”。一旦这些诊断性产物被直接纳入训练目标，policy 所吸收的就不只是偏好强弱或局部价值，而是可迁移的 failure abstraction 与 correction pattern；这也是 Diagnostic Feedback-to-Policy Transfer 区别于 Outcome Feedback 和 Process Feedback 的根本所在。[Zha26am, Hon25c, Wan26ad, Yua25c, Fu25d, Li26l]
```

## Parametric-to-Tokenized Experience Transformation

Parametric-to-Tokenized Experience Transformation 将已内化在参数化模型权重中的经验外化为可被其他系统消费的 token-level artifacts。参数化源可以是 policy model、teacher foundation model、LLM / VLM / MLLM / VLA agent，也可以是 reward model、verifier、critic、judge 等 evaluator model。与 Tokenized-to-Parametric 路径相反，P7 的方向不是把离散经验写入模型参数，而是从模型参数中”读出”可复用的经验表达。

在 LLM-based agent 场景中，P7 的目标不是生成一次性回答，而是生成可被另一个 student model、retrieval store、agent system、verifier 或下游训练管线继续消费的 tokenized artifacts——agent trajectories、tool-use demonstrations、GUI action traces、RAG reasoning paths、function-calling dialogues、step-level labels、critiques、verification traces 或 preference annotations。P7 将模型权重中隐式保存的任务执行能力或评估能力外化为可存储、可筛选、可训练、可检索或可组合的数据资源。

P7 需与普通 inference、self-training loop 及 P1/P2 路径区分。普通 inference 中，模型生成的 CoT 或答案仅服务于当前 query，缺乏独立归档和复用意图，不构成 P7。Self-training 或 iterative bootstrapping 中，模型自身生成的 rollouts 被同一训练循环的后继版本直接消费，更接近 composite pipeline。P1/P2 以已有 logs、trajectories 或 demonstrations 为主要输入，由模型对具体轨迹进行摘要、反思、重写或形式化；P7 的关键在于源经验主要来自参数化模型已内化的能力，而非某条已存在的 agent trajectory。

本文按外化 artifact 在下游系统中的主要消费角色，将 P7 方法划分为两类：Demonstration Externalization 外化”如何行动”的经验，即 policy 或 teacher model 的决策能力；Evaluative Supervision Externalization 外化”如何评价”的经验，即 evaluator 或 judge model 的评估能力。二者分别对应 agent experience 中 action-oriented knowledge 与 evaluation-oriented knowledge 的 token-level externalization。

---

### Demonstration Externalization

Demonstration Externalization 指参数化 policy、teacher foundation model 或 teacher agent 将其隐式决策能力外化为可供 student agent 模仿学习的行为示范。目标 artifact 通常是 agent trajectories、task demonstrations、tool-use dialogues、web / GUI / mobile interaction traces、function-calling records、RAG reasoning-action paths 或 code / tool execution traces。下游 consumer 通过 SFT、behavioral cloning、distillation 或 imitation-style training 学习这些示范数据，获得相应的 agentic behavior。

强模型或 teacher agent 已在参数中内化了一定的任务执行能力，但这些能力若只停留在模型权重中，便难以被小模型、专用 agent 或独立系统直接复用。Demonstration Externalization 通过任务提示、环境交互、tool schema、GUI state、retrieval context 或 seed instruction 诱导 teacher model 产生完整的行为过程，将”模型会做什么”转化为”学生可以学习的数据”——示范轨迹是 policy knowledge 的 tokenized read-out。

典型流程可概括为：由模型或系统生成任务、目标或环境初始状态；teacher policy 在环境中执行多步推理和动作，形成包含 observation、thought、action、tool call、GUI operation、retrieval step 或 final response 的轨迹；通过 execution checking、LLM-as-a-judge、rule-based validation、trajectory filtering、step-level filtering 或 human screening 筛除低质量数据。筛选后的轨迹被物化为训练语料，用于训练 student agent 或增强下游 agent 的任务执行能力。

这类方法覆盖多种 agent 设定。web agent 和 computer-use agent 中，外化 artifact 是浏览器或 GUI 环境中的多步操作轨迹——点击、输入、滚动、导航和读取结果。tool-use 或 function-calling agent 中，示范数据表现为多轮用户请求、assistant reasoning、API selection、function arguments、tool responses 和 final answer。RAG agent 中，外化 artifact 包括问题分解、检索动作、证据选择、中间推理和最终回答。任务领域不同，但共享同一转化逻辑：将 teacher model 的隐式行动能力外化为 action-bearing trajectories。

Demonstration Externalization 的优势在于可扩展性和低人工成本。相比人工标注多步 agent trajectories，强模型可在大量环境、任务和工具集合上自动生成示范，缓解 agent training data 的稀缺问题。web navigation、GUI automation、tool use 和 mobile control 等场景中，人工收集高质量轨迹成本很高，teacher-generated demonstrations 可快速扩大训练覆盖面。模型生成的数据可通过 task diversity control、multi-teacher mixing、curriculum sampling、difficulty-aware generation 或 environment-mediated synthesis 扩展到更多任务分布。

风险也同样存在。teacher-generated trajectories 可能包含 hallucinated actions、不可执行步骤、错误 tool arguments 或伪成功轨迹，缺乏可靠验证时 student 会继承 teacher 的错误行为。单一 teacher 或单一 prompt 生成的数据可能导致 distribution narrowing，使 student 过度拟合 teacher 的表达风格和决策偏好。long-horizon agent tasks 中，完整轨迹的成功不能直接说明每个中间动作的质量——错误可能在后续步骤中才暴露。Demonstration Externalization 通常需要与 execution-based verification、fine-grained filtering、diversity-promoting generation 和 curriculum design 结合。

RAGShaper、EviPath 等 evidence-grounded 方法仍可归入 Demonstration Externalization。虽然生成过程受 evidence、retrieval context、information tree 或 sub-question dependency 约束，下游消费的主要 artifact 仍是可训练的 reasoning-action trajectory。UI simulator、mock world 或 executable environment 在某些方法中可能参与数据生成，但若最终被 student 直接消费的是 trajectories、dialogues 或 demonstrations，则这些环境构造更适合作为示范轨迹外化的生成机制，而非单独的方法家族。

Demonstration Externalization 可概括为：从 policy 或 teacher model 的参数化决策能力中外化可模仿的行为经验。它回答的问题是——模型已会做某类任务，如何把这种能力转化为其他 agent 可以学习的示范数据？

论文：
- Explorer: Scaling Exploration-driven Web Trajectory Synthesis for Multimodal Web Agents
- Towards Internet-Scale Training For Agents
- RAGShaper: Eliciting Sophisticated Agentic RAG Skills via Automated Data Synthesis
- Structured Distillation of Web Agent Capabilities Enables Generalization
- TOUCAN: Synthesizing 1.5M Tool-Agentic Data from Real-World MCP Environments
- From Evidence to Trajectory: Abductive Reasoning Path Synthesis for Training Retrieval-Augmented Generation Agents
- LLMs as Scalable, General-Purpose Simulators For Evolving Digital Agent Training
- SynthAgent: Adapting Web Agents with Synthetic Supervision
- Fara-7B: An Efficient Agentic Model for Computer Use
- ToolMind Technical Report: A Large-Scale, Reasoning-Enhanced Tool-Use Dataset
- OpenMobile: Building Open Mobile Agents with Task and Trajectory Synthesis
- Learning with Challenges: Adaptive Difficulty-Aware Data Generation for Mobile GUI Agent Training
- APIGen-MT: Agentic Pipeline for Multi-Turn Data Generation via Simulated Agent-Human Interplay
- ToolAlpaca: Generalized Tool Learning for Language Models with 3000 Simulated Cases
- APIGen: Automated Pipeline for Generating Verifiable and Diverse Function-Calling Datasets
- ToolACE: Winning the Points of LLM Function Calling
- AutoSurfer -- Teaching Web Agents through Comprehensive Surfing, Learning, and Modeling
- Scalable Data Synthesis for Computer Use Agents with Step-Level Filtering
- ANCHOR: Branch-Point Data Generation for GUI Agents
- FABRIC: Framework for Agent-Based Realistic Intelligence Creation
- AgentSynth: Scalable Task Generation for Generalist Computer-Use Agents
- ASTRA: Automated Synthesis of agentic Trajectories and Reinforcement Arenas
- Mock Worlds, Real Skills: Building Small Agentic Language Models with Synthetic Tasks, Simulated Environments, and Rubric-Based Rewards
- Controllable and Verifiable Tool-Use Data Synthesis for Agentic Reinforcement Learning
- Step-GUI Technical Report

```
在 Demonstration Externalization 路径中，参数化经验的外化对象不再是抽象规则或结构化 workflow，而是可被 student 直接模仿学习的行为示范。其基本做法是，由强 policy model、teacher foundation model 或 teacher agent 在真实环境或高保真模拟环境中执行多步任务，将已内化的决策能力读出为 tokenized trajectories、tool-use dialogues、GUI action traces 或 reasoning-action paths，并经过执行验证、judge 过滤或步骤级筛选后，转化为可供 SFT 或 behavioral cloning 消费的训练语料。因而，这类方法的关键不在于“模型生成了答案”，而在于“模型生成了可复用的示范数据”，将 teacher 的隐式 agentic competence 物化为 student 可学习的外部经验资源。

在 web 与 computer-use 场景中，这一路径通常体现为对多步交互轨迹的自动合成与过滤。Explorer 通过 exploration-driven 流水线让 GPT-4o 在真实网页中自主发现任务并执行交互，再由 proposer、refiner、summarizer 与 verifier 生成带页面状态、动作序列与任务总结的 multimodal trajectories，是较早较完整的 teacher-to-student web demonstration synthesis 代表 [Pah25]。InSTA 则将这一思路扩展到 internet scale，使强模型在大规模真实网站上自动提出任务、执行网页操作并生成 reasoning traces，再借助 judge filtering 保留高质量成功轨迹，从而把网页代理能力外化为大规模训练数据 [Tra25]。在此基础上，Structured Distillation of Web Agent Capabilities Enables Generalization 进一步强调示范形式的结构化约束，通过 Agent-as-Annotators 框架生成带结构化 reasoning blocks 的成功轨迹，以提升 student 对长程网页行为模式的学习效率 [Lu26]。SynthAgent 与 AutoSurfer 则更突出“先探索环境，再外化数据”的逻辑：前者在目标网站上进行 element-level exploration、任务合成与轨迹重写，生成更贴合特定站点分布的 synthetic supervision [Wan25ar]；后者先系统性 surf 网站、识别功能空间，再整理为包含页面状态、动作历史、下一步动作与推理的 task tuples，以降低脱离真实网页结构的数据幻觉 [Fai26]。在 GUI 与 computer-use 设定中，Fara-7B 利用强模型驱动的 FaraGen 生成大规模 screenshot-thought-action trajectories，并通过多重 verifier 筛选高质量 demonstrations [Awa25]；WebSTAR 则进一步引入 post-hoc thought augmentation 与 step-level filtering，说明 demonstration externalization 不仅可以外化整条轨迹，也可以对轨迹内部步骤进行再评分与重写，以提高监督信号密度 [He25g]。类似地，OpenMobile 通过 expert 接管修正 learner 偏差，保留 corrected trajectories 与 step-level CoT 作为训练数据 [Che26d]；Learning with Challenges 则显式根据 student 的能力边界生成难度自适应的 mobile GUI demonstrations，使外化数据始终处于“可学但有挑战”的区间 [Kan26b]。

在 tool-use 与 function-calling 场景中，外化 artifact 的主要形式转向多轮工具交互对话与函数调用记录。TOUCAN 在真实 MCP environments 中让多个强模型合成任务并执行完整的 tool-use rollouts，记录 planning、tool call、tool response 与 final answer，再通过 task-level 与 trajectory-level 双重过滤形成大规模 tool-agentic corpus，是 tool-use demonstration externalization 的代表性工作 [Xu25o]。ToolMind 通过 user agent、assistant agent 与 tool agent 的多智能体模拟生成带 `<think>`、`<tool_call>` 与 `<tool_response>` 的多轮交互轨迹，并在 trajectory-level 与 turn-level 做细粒度过滤，突出展示了 reasoning-enhanced tool-use dialogue 作为行为示范的形式 [Yan25ab]。APIGen-MT 先生成 task blueprint 与 ground-truth action sequence，再通过 simulated agent-human interplay 合成多轮 function-calling dialogues，并以 rejection sampling 保证最终轨迹与预期目标一致，从而将 teacher 关于多轮 API 协作和用户澄清流程的隐式能力外化为可验证 demonstrations [Pra25b]。更早的 ToolAlpaca 已经清楚展示了这一范式，即通过多智能体 simulation 生成 `{Instruction, Actions, Response}` 型工具使用轨迹，并据此微调 student 模型 [Tan23]；随后，APIGen 与 ToolACE 分别从可验证函数调用样本生成与复杂 API orchestration 对话合成两个方向推进了这一谱系 [Liu24n, Liu24o]。

在 retrieval-augmented agent 场景中，Demonstration Externalization 的重点转向 evidence-grounded reasoning-action path 的生成。RAGShaper 通过构造带 distractor 的信息树与多跳问题，诱导强 teacher 在受控检索环境中生成包含 thought、retrieval action、observation 与 final answer 的 agentic RAG trajectories，从而将复杂检索、抗干扰与证据整合能力外化为可直接监督 student 的 reasoning-action data [Tao26]。From Evidence to Trajectory 则进一步采用从 gold evidence 反推 abductive reasoning path 的方式，再由强模型生成包含规划、子问题分解与 evidence-grounded answering 的 RAG trajectories [Li25at]。这类方法的重要意义在于，它们并非仅对已有日志做事后压缩，而是直接从 teacher 已内化的推理能力中读出可训练的行为路径，因此仍然属于参数化能力向 tokenized demonstrations 的外化。

总体来看，这一类工作虽然覆盖 web、GUI、tool use 与 RAG 等不同任务形态，但共享同一经验转化逻辑：先由强模型在环境中显式演示“如何行动”，再通过验证、过滤与重写将这些演示物化为 student 可消费的训练数据。相较之下，一些同时构造任务、环境或奖励的系统更接近 composite pipeline，可作为邻近工作补充讨论，但不宜作为这一子类的主干代表。对 Demonstration Externalization 而言，最关键的共性仍是：外化的最终产物是 trajectories、dialogues 或 reasoning-action demonstrations，本质上回答的是“模型已经会做某类任务，如何把这种能力转化为其他 agent 可以学习的数据”。
```

### Evaluative Supervision Externalization

Evaluative Supervision Externalization 指参数化 evaluator、judge、verifier、critic 或 reward model 将其隐式评估能力外化为 token-level supervision，并将这些监督信号提供给其他 student model、agent system、data filtering pipeline 或 reward-model training process 使用。不同于 Demonstration Externalization 外化”如何行动”的行为知识，这类方法外化的是”如何判断行动质量”的评价知识。

目标 artifact 包括 critiques、step-level labels、action correctness annotations、progress labels、preference pairs、verification traces、failure diagnoses、repair suggestions、trajectory refinement comments 或 reward-model training data。形式可以是自然语言 critique、结构化标签、局部动作评分、步骤级 pass/fail 判断、候选轨迹排序，或带有理由说明的 preference annotation。只要 evaluator 的输出被物化为可复用 token-level artifact 并被另一系统消费，就属于此类。

许多强模型不仅能执行任务，也能判断 agent 行为是否合理、某一步动作是否有效、某条轨迹是否完成目标、某个 tool call 参数是否正确，或某个中间推理是否偏离证据。Evaluative Supervision Externalization 将这种评估能力从模型权重中外化，形成比 scalar reward 更丰富的监督数据。下游系统可用这些数据过滤 demonstrations、训练 verifier、构造 reward model、指导 student agent 学习，或为失败轨迹提供可修正的诊断信息。

此类方法需与 P6 区分。P6 的核心是 Parametric Evaluator-to-Policy alignment，evaluator 的 reward、preference 或 critique 直接参与 policy 优化，使 policy 参数发生更新。Evaluative Supervision Externalization 强调 evaluator 的输出被显式物化为 tokenized artifacts，且可脱离原 evaluator 被其他系统复用。一个 judge 对每个 GUI action 生成 step-level correctness label 并组成独立训练集用于训练 student agent 或 step reward model，这属于 P7；若 judge 只在同一 RL loop 中给当前 policy 一个 scalar reward，则更接近 P6。

此类方法也需与普通数据过滤区分。许多 Demonstration Externalization 方法用 judge 或 verifier 删除低质量轨迹，但若 judge 的输出只作为内部过滤开关而非独立监督数据被保存或消费，则只是质量控制机制。只有当 evaluator 的判断本身成为可复用 artifact——graded steps、progress annotations、verification traces、critiques 或 preference rationales——才应作为此类方法的核心。

Evaluative Supervision Externalization 的优势在于缓解长程 agent 任务中的 credit assignment 问题。web navigation、GUI automation、tool use、software engineering 和 embodied control 等任务中，完整 trajectory 的成功或失败往往不足以说明每一步动作的局部价值。步骤级 labels、action-level critiques 或 progress annotations 提供更细粒度的学习信号，使 student 不只是模仿整条轨迹，而是知道哪些中间动作正确、哪些动作导致偏离目标、哪些失败轨迹仍包含可利用的局部步骤。这类方法特别适合与 noisy teacher rollouts、partially successful trajectories 和 large-scale synthetic demonstrations 结合。

此外，这类方法可提高 synthetic data pipeline 的数据利用率。传统 trajectory-level filtering 往往将整条失败轨迹直接丢弃，即使其中包含大量正确中间步骤。通过 step-level evaluation，可从失败轨迹中保留局部正确动作，或为错误步骤生成诊断和修正建议——evaluator 不只是数据筛选器，而成为新的经验外化源，将自身对行为质量的判断转化为可训练的评价经验。

局限同样存在。evaluator 本身可能有系统性偏差，错误的 step labels 或 critique 会误导 student。LLM-as-a-judge 在复杂环境中的判断并不总是可靠，尤其当任务成功条件依赖隐式状态、外部工具结果或视觉细节时。细粒度标注虽提供更强监督，但显著增加计算成本和 pipeline 复杂度。实际系统通常需要结合 execution-based checking、rule-based validation、multi-judge agreement、calibration、human audit 或 consistency verification 控制 evaluator-generated supervision 的质量。

Evaluative Supervision Externalization 可概括为：从 evaluator model 的参数化评估能力中外化可复用的评价经验。它回答的问题是——模型已能判断任务执行质量，如何把这种判断能力转化为其他 agent 可以学习、过滤或验证的监督数据？

论文：
- Scalable Data Synthesis for Computer Use Agents with Step-Level Filtering
- Scaling Web Agent Training through Automatic Data Generation and Fine-grained Evaluation
- ToolMind Technical Report: A Large-Scale, Reasoning-Enhanced Tool-Use Dataset（secondary；若其 turn-level filtering / validation labels 被作为监督信号保留）
- Structured Distillation of Web Agent Capabilities Enables Generalization（secondary；其 judge / evaluation hints 可作为评估监督外化的辅助例子）
- TOUCAN: Synthesizing 1.5M Tool-Agentic Data from Real-World MCP Environments（secondary；其 model-based validation 更主要是质量控制机制）
- 

```

在 Evaluative Supervision Externalization 路径中，一类较为清晰的方法不是直接用 evaluator 的标量 reward 优化 policy，而是将其隐含的评估能力外化为可保存、可复用的 token-level supervision artifacts，再由 student agent 或后续训练管线消费。这类工作在 web、GUI 与 computer-use agent 中尤为突出：强 judge 或 verifier 不再只是充当一次性的质量门控器，而是把对步骤正确性、局部进展和失败原因的判断转化为 graded steps、verification labels、progress annotations 或结构化反思信号，从而把“如何判断行为质量”的经验沉淀为独立的数据资源。

其中，若从步骤级评估信号的显式外化来看，[He25g] 是代表性例子。该工作先用强 computer-use agent 生成 noisy trajectories，再由 o4-mini 对每一步进行 correctness 与 optimality grading，并附带 screenshot analysis、action review 和 alternative analysis 等 reasoning-rich annotations；这些评估结果被物化为 WebSTAR 与 WebSCORE 等数据资源，前者用于训练 student computer-use agent，后者进一步蒸馏出轻量 StepRM，因此完整体现了从参数化评估能力到 tokenized evaluative supervision 的外化链条。[Lu25e] 则以 GPT-4o 作为 step verifier，比对动作前后界面状态，为每一步生成 binary correctness label 与 verification reasoning，并据此构建 step-verified trajectory data，再通过 KTO 训练开源 student agent；这里 verifier 的输出本身已成为可独立消费的训练监督，而不只是内部过滤信号。

另一类强匹配工作强调对长程任务进展的细粒度判定。[Log26b] 从 web task 中抽取显式 constraints，并在轨迹每一步评估 constraint satisfaction state，形成细粒度的 CSR progress signal，随后据此执行 prefix extraction 与 hindsight relabeling，使部分成功轨迹也能转化为可训练样本。其关键贡献在于，judge 的评估不只决定样本去留，而是进一步塑造了最终保存下来的 progress annotations 与 relabeled artifacts。[Yan25x] 也体现出相近思路：其 Calibrated Step Reward System 先以轨迹级 verifier 建立质量锚点，再由强多模态模型将这些验证结果转写为 progress tracking、state summary、effect prediction、self-reflection、state verification、intent execution 和 action prediction 等七类结构化 step-level supervision，从而把稀疏的轨迹级成败判断转化为密集的过程监督数据。

相比之下，一些边界案例虽然也包含 evaluative artifact 的外化，但其核心机制与 trajectory repair、process refinement 或 critique-guided improvement 更紧密耦合，因而更适合作为补充而非主例。[Wan25x] 将 step-level deviation detection 转化为 reflective thoughts 与 calibrated actions，把失败步骤改写为带反思和修正信息的 calibrated trajectory；[Xio24] 则主要通过 Monte Carlo rollout 将 outcome reward 细化为 step-level preference data，再用于 Step-DPO 式优化。类似地，[Yan25s] 和 [Li26l] 都展示了 critic 生成自然语言 critique 或 diagnosis 并被 actor 继续消费的机制，但其 token artifacts 主要服务于同一改进闭环，而非以独立、可迁移的数据资产形态存在。因此，从“参数化 evaluator 的判断被显式物化并供后续系统复用”的纯粹程度看，[He25g]、[Lu25e]、[Log26b] 与 [Yan25x] 更适合作为本小节的核心文献，而其余工作可用于补充说明该路径与 calibration、refinement 及 critic-guided improvement 之间的连续边界。
```

### 小结：行动经验与评价经验的外化

上述两类方法构成 P7 路径的核心组织方式。Demonstration Externalization 将 policy 或 teacher model 的决策能力外化为 trajectories 和 demonstrations，强调”应该如何行动”；Evaluative Supervision Externalization 将 evaluator 或 judge model 的评估能力外化为 labels、critiques 和 verification traces，强调”如何判断行动质量”。前者主要服务于 student agent 的行为模仿与能力蒸馏，后者主要服务于数据筛选、细粒度监督、verifier 训练和 agent 行为改进。

两类方法在实际系统中并非完全孤立。许多 agent data synthesis pipeline 同时包含 teacher rollout 和 evaluator filtering：teacher model 生成候选 trajectories，judge model 进行验证、打分或步骤级标注。主分类取决于论文的核心贡献和最终被下游消费的主要 artifact——若主要贡献是生成可模仿的 trajectories，归入 Demonstration Externalization；若主要贡献是将 evaluator 的判断外化为可复用监督，归入 Evaluative Supervision Externalization。

除两个主类外，P7 方法还存在若干横向设计维度：environment-mediated synthesis、multi-teacher mixing、curriculum control、difficulty-aware sampling、execution-based verification、step-level filtering、human-in-the-loop screening 和 multimodal grounding。这些机制不构成独立的外化目标，而是影响外化 artifact 的质量、规模、多样性和可验证性。在综述组织上，它们更适合作为跨方法家族的设计轴讨论，而非一级分类。
