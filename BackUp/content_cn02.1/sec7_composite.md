## Composite Experience Transformation Pipelines

除了前文讨论的单步 experience transformation pathways 之外，LLM-based agent 文献中还存在一类更复杂的方法：它们并不只把经验从一种载体转化为另一种载体，而是将多个 transformation steps 组织成一个链式或闭环式 pipeline。本文将这类方法称为 Composite Experience Transformation Pipelines。其核心特征是，经验在 N-Tok、S-Tok、V-Par 与 \(\pi\)-Par 等多个载体之间连续流动，并且相邻转化步骤之间的衔接机制本身构成方法的主要贡献。

Composite pipeline 的判定关键不是“方法是否包含多个操作步骤”，而是这些步骤之间是否存在实质性的 integration mechanism。例如，一篇论文可能先生成 agent trajectories，再用这些 trajectories 训练 policy；如果中间只是常规数据收集与常规 fine-tuning，则更适合归入单步 N-Tok / S-Tok \(\rightarrow\) \(\pi\)-Par internalization。相反，如果论文的核心贡献在于如何筛选、修复、校准、重标、评估或闭环调度这些中间经验，使其能够被下游 policy 或 evaluator 有效消费，则应归入 Composite。

因此，Composite 方法的分析重点不只是源载体和目标载体，而是经验在不同载体之间流动时如何被重新解释。原始 agent trajectory 中可能同时包含成功策略、失败动作、局部正确步骤、环境反馈、错误恢复过程和噪声行为。Composite pipeline 试图通过多阶段转化，把这些混杂的经验信号组织成更可靠的训练、评估或改进机制。与单 pathway 相比，这类方法通常具有更强的经验利用能力，但也更容易受到衔接误差、错误反馈累积、分布漂移和闭环坍缩的影响。

本文将 Composite Experience Transformation Pipelines 进一步划分为三类：Evaluator–Policy Co-Evolution、Refinement-Mediated Policy Internalization，以及 Other Composite Experience Pipelines。前两类对应当前文献中机制相对清晰、复用频率较高的复合模式；第三类则收纳那些同样满足 Composite 条件，但不以 evaluator–policy 共同演化或 refined experience internalization 为核心的异质复合路径。

### Evaluator–Policy Co-Evolution

Evaluator–Policy Co-Evolution 指的是 evaluator parameter 与 policy parameter 在同一个 agent learning loop 中围绕 agent experience 进行相互校准、相互净化和共同演化的方法。这类方法并不强调一个严格的线性顺序，例如“先训练 evaluator，再训练 policy”。更准确地说，它们关注的是 V-Par 与 \(\pi\)-Par 之间的耦合关系：policy 产生新的行为分布和交互经验，evaluator 根据这些经验更新或校准自身的评价能力；随后 evaluator 又通过 reward、critique、preference、verification 或 process feedback 反过来筛选、纠正或推动 policy 更新。

这类方法的抽象结构可以表示为 \(\pi\)-Par \(\leftrightarrow\) V-Par。展开来看，policy 在环境中 rollout 或执行任务，产生 N-Tok / S-Tok 形式的 trajectories、reasoning traces、tool-use logs、GUI actions、robot execution records、step-level labels 或 failure cases；这些经验被用于训练、更新或校准 evaluator，使其形成 reward model、critic、verifier、judge、process reward model 或 diagnostic feedback model。与此同时，evaluator 生成的评价信号又会被用于 policy improvement，例如 guiding exploration、constructing preference pairs、selecting trajectories、providing language critiques、shaping rewards 或 supporting reinforcement learning。

这一类方法与单步 N-Tok / S-Tok \(\rightarrow\) V-Par 不同。单步 evaluator internalization 的目标是把 tokenized experience 写入 evaluator 参数中，使其获得可复用的评估能力；而 Evaluator–Policy Co-Evolution 的重点在于 evaluator 不是最终产物，而是 policy improvement loop 中的动态参与者。同样，它也不同于单步 V-Par \(\rightarrow\) \(\pi\)-Par preference alignment，因为这里的 evaluator 往往不是固定的外部 reward model，而是会随着 policy 行为分布的变化不断调整。换言之，评价能力和决策能力并不是两个独立模块，而是在同一个经验闭环中共同演化。

这类方法的基本思想是，agent 的持续学习不仅需要更强的 policy，也需要与当前 policy 行为分布相匹配的 evaluator。在 open-world agent、GUI agent、web agent 或 embodied agent 中，policy 的行为会随着训练不断变化，旧 evaluator 很容易变得 stale：它可能无法识别新型失败模式，也可能对新策略产生错误评价。如果仍然用静态 evaluator 监督不断变化的 policy，policy 可能会过拟合 evaluator 的偏差，甚至通过 reward hacking 获得高分但不真正提升任务能力。因此，许多方法将 evaluator 与 policy 放入共同更新框架中，使 evaluator 能够从 policy 的新行为、新错误和新边界样例中继续学习，而 policy 也能从更新后的 evaluator 中获得更贴近当前问题分布的反馈。

Evaluator–Policy Co-Evolution 的 integration mechanism 通常包括 alternating update、feedback reflux、hard negative mining、critic refresh、dual-track optimization、reward-model relabeling、process-level critique generation、policy-conditioned evaluator training 或 evaluator-guided trajectory selection。这些机制的共同目标是防止 evaluator 与 policy 脱节。一方面，policy 需要通过 evaluator 获得比稀疏环境反馈更密集、更细粒度的学习信号；另一方面，evaluator 也需要通过 policy 产生的新经验来扩大自身覆盖范围，减少 stale feedback 和 distribution mismatch。

这类方法的主要优势在于能够将“评估经验”和“决策经验”结合起来。agent trajectory 不仅可以告诉 policy 什么动作可能成功，也可以训练 evaluator 判断什么行为是合理的、什么过程是错误的、什么中间状态代表进展。由此，系统可以把离散的历史反馈抽象为更泛化的评估能力，再利用这种评估能力持续改进 policy。对于环境反馈稀疏、人工标注昂贵或过程质量难以直接度量的任务，这种 evaluator–policy coupling 尤其有价值。

然而，这类方法也引入了较高的闭环风险。如果 evaluator 的训练数据主要来自当前 policy，它可能继承 policy 的探索盲区和行为偏差；如果 policy 过度依赖 evaluator，则可能学会利用 evaluator 的漏洞，而不是真正提升任务表现。更复杂的情况下，evaluator 和 policy 可能形成共适应偏差：evaluator 奖励 policy 已经偏好的行为，policy 又产生更多类似行为强化 evaluator 的偏见。因而，分析这类方法时需要重点关注其是否包含外部验证、hard negatives、out-of-distribution behavior、evaluator refresh、human/environment grounding 或 anti-collapse 机制。

论文：
- UI-Genie: A Self-Improving Approach for Iteratively Boosting MLLM-based Mobile GUI Agents
- MagicGUI-RMS: A Multi-Agent Reward Model System for Self-Evolving GUI Agents via Automated Feedback Reflux
- No More Stale Feedback: Co-Evolving Critics for Open-World Agent Learning
- RLAnything: Forge Environment, Policy, and Reward Model in Completely Dynamic RL System
- RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning
- VARP: Reinforcement Learning from Vision-Language Model Feedback with Agent Regularized Preferences
- EVPO: Explained Variance Policy Optimization for Adaptive Critic Utilization in LLM Post-Training
- Co-Evolution of Policy and Internal Reward for Language Agents

```
可以直接写成下面这种更接近 CSUR 正文风格的小段落：

## Evaluator–Policy Co-Evolution

在 Composite Experience Transformation Pipelines 中，Evaluator–Policy Co-Evolution 的核心不在于“先有 evaluator 再训练 policy”的线性顺序，而在于 evaluator parameter 与 policy parameter 围绕同一批交互经验形成持续闭环：policy 在环境中产生新的行为分布、失败模式与边界样例，evaluator 由此获得更新；更新后的 evaluator 又以 reward、critique、verification 或 step-level preference 的形式反过来塑造后续 policy learning。现有文献中，最强匹配的实例主要出现在 GUI 与 open-world agent 场景。UI-Genie [Xia25e] 将 GUI agent 与 reward model 放入多轮 self-improving loop 中：agent 的探索轨迹一方面被 reward-guided search 用于筛选高价值行为，另一方面失败轨迹又经 continuation rollout 自动转化为新的 step-level supervision 来刷新 reward model，从而形成 evaluator 与 policy 的双向迭代。MagicGUI-RMS [Li26n] 则进一步将这种闭环做成分层评估体系，通过 DS-RM 与 GP-RM 的协作及 feedback reflux 机制，把 agent 执行中的高质量纠偏动作回流为 policy supervision，同时把评估分歧样本回流为 evaluator 的再训练数据，实现策略与评估器的同步净化。与之相近，ECHO [Li26l] 将 critic staleness 明确视为核心问题，采用由初始轨迹、语言诊断与条件修正组成的 synchronized update loop，使 critic 始终跟随当前 policy 的失败模式演化，并借助 saturation-aware gain shaping 保持对高分段细粒度改进的敏感性。RLAnything [Wan26u] 也体现了明显的 evaluator–policy 耦合：reward model 由 evolving policy 的轨迹持续更新，而其 step-wise feedback 又与 outcome signal 一起反向驱动 policy 优化；不过该方法同时显式引入 environment adaptation，因此更准确地说，它代表了 evaluator–policy co-evolution 向“policy–reward–environment”三元闭环的进一步扩展。

相比之下，另一些论文更适合作为该子类的边界实例，而非其最典型代表。RL Tango [Zha25y] 在 reasoning setting 中交替训练 generator 与 verifier，使 verifier 随 generator 的推理轨迹分布共同更新，并以 process-level feedback 反向塑造 generator；其机制上符合 evaluator–policy co-evolution，但场景更偏 reasoning agent 而非外部交互 agent。VARP [Sin25b] 在 embodied RL 中通过 agent-regularized preferences 让 reward learning 显式依赖当前 policy rollout，从而缓解奖励模型与行为分布脱节的问题，也体现了 reward 与 policy 的协同更新，但其任务背景仍更接近 preference-based robotics RL。EVPO [Pan26] 进一步展示了另一种较弱耦合形式：critic 虽随 policy 持续训练，但论文关注的重点是依据 explained variance 自适应控制 critic 在不同阶段的可用性，因此更像是 critic utilization 与 policy optimization 的动态协调，而非典型的 critic refresh loop。最后，Co-Evolution of Policy and Internal Reward for Language Agents [Wan26aj] 将 evaluator 内生化为 policy 自身生成的 self-guidance，并把该信号同时用于 inference-time steering 与 training-time internal reward，形成“更强 policy 产生更好 guidance，更好 guidance 再改进 policy”的自洽闭环；这一方向说明，Evaluator–Policy Co-Evolution 不一定总以独立外部 evaluator 的形式出现，也可以以内生化的 internal reward 机制存在。
```


### Refinement-Mediated Policy Internalization

Refinement-Mediated Policy Internalization 指的是将原始 agent experience 先转化为更可学习的 refined artifact，再将其内化进 policy parameter 的复合路径。这类方法的典型结构是 N-Tok \(\rightarrow\) N-Tok / S-Tok \(\rightarrow\) \(\pi\)-Par。源经验通常是 agent 在交互过程中产生的 raw trajectory、failure episode、reasoning trace、tool-use log、GUI interaction trace、web navigation history、robot execution record、dialogue history 或 environment feedback。这些原始经验首先被表示为 N-Tok，因为它们通常以自然语言、多模态序列或弱形式化轨迹的方式记录 agent 在特定上下文下如何观察、推理、行动并接收反馈。

这类方法的核心不是直接把 raw trajectory 训练进 policy，而是先对原始经验进行反思、修复、校准、净化、压缩或形式化，使其变成更适合 policy learning 的中间 artifact。转化后的 artifact 可以仍然是 N-Tok，例如 reflection、failure explanation、lesson、correction suggestion、repaired trajectory、natural-language skill、process feedback 或 distilled experience note；也可以是 S-Tok，例如 program of thought、workflow、step-level action schema、structured plan、trajectory tree、state transition graph 或 executable procedure。无论目标是 N-Tok 还是 S-Tok，关键在于 refinement step 是 policy internalization 的中介，而不是一个独立的 memory-writing 或 summarization step。

这类方法与单步 N-Tok \(\rightarrow\) N-Tok 转化不同。单步 narrative refinement 通常将 reflection、summary、lesson 或 memory 作为 inference-time context 使用，后续 agent 通过 retrieval 或 prompt injection 复用这些经验。而在 Refinement-Mediated Policy Internalization 中，refined artifact 会进一步进入训练过程，被用于 supervised fine-tuning、preference optimization、reinforcement learning、distillation 或 process supervision。因此，refinement 的目标不是仅仅让经验更容易被读懂，而是让经验更适合被写入 \(\pi\)-Par。

这类方法也不同于直接的 N-Tok / S-Tok \(\rightarrow\) \(\pi\)-Par internalization。直接训练 raw trajectories 往往假设轨迹本身就是可靠监督信号，但 agent experience 通常是混杂的：失败轨迹中可能包含正确的前缀和局部有效动作；成功轨迹中也可能包含冗余动作、偶然成功或不可迁移的 shortcut。如果直接模仿整条轨迹，policy 可能把错误动作、无效恢复或偶然因素一并内化。Refinement-Mediated Policy Internalization 的核心假设是，经验在写入参数之前需要被重新解释：哪些步骤真正导致成功，哪些步骤是失败根源，哪些经验具有跨任务迁移价值，哪些轨迹片段应被删除、修复或重标。

因此，这类方法的 integration mechanism 通常包括 failure reflection、first-error localization、hindsight rewriting、trajectory repair、step-level process refinement、calibration、self-purification、skill extraction、program induction、positive amplification 或 causal correction。它们试图把 noisy、局部、冗长、失败混杂的原始 experience 转化为更短、更明确、更具因果指向的 training signal。例如，一条失败轨迹可以被重写为“错误定位 + 修正动作 + 新轨迹”；一组成功轨迹可以被压缩为 reusable skill；一个多步 GUI trace 可以被转化为 step-level correction；一个 embodied trajectory 可以被转化为 program-like thought structure。随后，policy 通过训练内化这些 refined artifacts，从而获得比直接模仿 raw traces 更稳定的行为改进。

这类方法的基本思想是，agent 的历史经验并不天然等价于可学习监督。经验要进入 policy 参数，必须先经过某种形式的“经验加工”。这种加工可以保留原始经验中的有效决策模式，去除或弱化噪声行为，并显式暴露失败原因、修复策略或可迁移 skill。对于长程、多步、稀疏反馈任务，这一点尤其重要，因为最终 reward 往往不足以解释中间步骤的贡献，而 refinement 可以提供更细粒度的过程信号。

Refinement-Mediated Policy Internalization 的优势在于能够更充分地利用失败经验和过程经验。传统 imitation learning 更依赖成功 demonstrations，而这类方法可以从失败轨迹中提取错误模式、反事实修正和改进行为，使 failure 不再只是被丢弃的负样本，而成为 policy improvement 的来源。它也有助于缓解长轨迹训练中的 credit assignment 问题，因为 reflection、repair 或 calibration 可以把最终结果回溯到关键步骤。

但这类方法的局限同样明显。首先，refinement 本身可能出错。如果模型错误定位失败原因，或将偶然因素解释为通用规律，那么 refined artifact 会成为有害训练信号。其次，refinement 过程可能过度依赖强 teacher model、人工规则或任务特定 verifier，使方法的泛化性受到限制。再次，如果 refined artifacts 过于抽象，policy 可能难以将其映射回具体动作；如果过于具体，则可能失去跨任务迁移能力。因此，在分析这类方法时，应重点关注作者是否比较了 raw experience training 与 refined experience training，是否验证 refinement step 的必要性，以及 refinement 后的经验是否真正提升了 policy 的泛化能力而非只提升训练集拟合。

论文：
- Internalizing Agency from Reflective Experience [Ge26]
- Watch Every Step! LLM Agent Learning via Iterative Step-level Process Refinement [Xio24]
- Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training [Yua25c]
- Skill-SD: Skill-Conditioned Self-Distillation for Multi-turn LLM Agents [Wan26al]
- Online Experiential Learning for Language Models [Ye26f]
- STeCa: Step-level Trajectory Calibration for LLM Agent Learning [Wan25x]
- GUI-Reflection: Empowering Multimodal GUI Models with Self-Reflection Behavior [Wu25b]
- ReAct Meets ActRe: When Language Agents Enjoy Training Data Autonomy [Yan24m]
- CLEANER: Self-Purified Trajectories Boost Agentic Reinforcement Learning [Xu26j]
- AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling [Din26]
- Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents [Son24]
- Memento No More: Coaching AI Agents to Master Multiple Tasks via Hints Internalization [Ala25]
- UI-Genie: A Self-Improving Approach for Iteratively Boosting MLLM-based Mobile GUI Agents [Xia25e]
- OpenWebVoyager: Building Multimodal Web Agents via Iterative Real-World Exploration, Feedback and Optimization [He24e]
- Policy Improvement using Language Feedback Models [Zho24e]
- RetroAgent: From Solving to Evolving via Retrospective Dual Intrinsic Feedback [Zha26]
- VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought [Sar24b]

```
## Refinement-Mediated Policy Internalization

在 Refinement-Mediated Policy Internalization 这一类方法中，核心问题并不是如何直接把 raw trajectory 写入 policy，而是如何先将原始交互经验加工为更稳定、更具因果指向性、也更适于学习的中间监督，再完成参数内化。现有代表性工作大体沿着三条机制展开：一类强调对失败经验的反思、修复与重写；一类强调对长轨迹中局部步骤质量的辨析、校准与过程监督；还有一类强调将经验进一步抽象为 skill、hint 或 transferable knowledge，再通过蒸馏或监督训练写回 policy 参数。

第一类工作以失败经验的再解释为核心，将原本不可直接学习的失败轨迹转化为可训练的纠错监督。[Ge26] 将失败 rollout 提炼为 rollback target 与 reflective summary，再据此生成修正分支，并通过 counterfactual distillation 使模型在不显式依赖反思文本的条件下复现这些修正决策，从而把外显的 reflective agency 内化为参数能力。[Yua25c] 则从 good 与 bad trajectories 中构造带有 reflection signal 的 revision trajectory，使模型学习在识别到首个关键错误后尽早切换到修正路径，而不是仅在任务失败后被动补救。[Wan25x] 进一步把这种修复粒度细化到步骤层面，通过定位第一个偏离 expert path 的动作，生成包含 reflective thought 与 corrected action 的 calibrated trajectory，再据此训练 policy。[Xu26j] 关注工具调用与代码执行中的噪声污染问题，利用 similarity-aware rollback 将含错误上下文的轨迹纯化为 self-purified trajectories，避免模型把无效恢复过程一并内化。[Din26] 则从另一方向利用失败经验：它并不修复原轨迹，而是根据失败轨迹实际达成的 outcome 逆向生成 hindsight goal，把失败运行重写为新的成功 demonstration，再将这些 relabeled samples 用于 SFT 或 DPO。

第二类工作更关注如何把长程交互中的局部优劣结构转化为可学习的过程监督。[Xio24] 利用 Monte Carlo rollout 将稀疏的 outcome reward 下放到具体步骤，构造 step-level contrastive pairs 与 trajectory-level preference pairs，并通过 step-DPO、outcome-DPO 与 SFT 的联合优化，把过程层面的 refined signal 写入 policy。[Son24] 也并不直接在 exploration rollout 上训练，而是将失败轨迹与成功轨迹组织为 preference pairs，再通过 DPO 让模型学习“成功优于失败”的结构化偏好。[Yan24m] 的关键贡献在于用 ActRe 为探索得到的动作序列反向补写 posterior reasoning，将原本缺乏解释的 action traces 重构为可训练的 ReAct-style trajectories，再通过 contrastive self-training 实现经验内化。[Wu25b] 面向 GUI agent，系统性地通过离线伪造错误与在线挖掘失败轨迹构造 reflection thought、rollback 与 correction 数据，使模型学习的不是单纯成功示范，而是更具恢复性和自检性的 refined interaction traces。

第三类工作则将经验进一步压缩为更抽象、可迁移的中间知识形式，再通过蒸馏或监督目标将其写回参数。[Wan26al] 先把多轮 agent trajectories 总结为结构化 natural-language skills，包括 success analysis、mistake analysis 与 golden workflow，再把这些 skills 仅作为训练期 teacher 的特权信息，通过 self-distillation 将其吸收到 student policy 中。[Ye26f] 将在线交互轨迹递增式提炼为 experiential knowledge，并通过 on-policy context distillation 将“带知识的 teacher”压缩为“无知识的 student”，明确体现出“先抽取经验，再参数固化”的两阶段逻辑。[Ala25] 则以 corrective hints 为中介：reviewer 先从轨迹中识别错误模式并生成针对性提示，teacher 在 hints 引导下产生更优行为分布，student 再通过 context distillation 学会在不显式接收 hints 的情况下复现这些行为，从而完成从外部 coaching 到参数内化的转换。

相比之下，一些边界性工作虽然同样包含“经验加工后再优化 policy”的复合链条，但 refinement 的中介性或 internalization 的纯度相对较弱。[Xia25e] 与 [He24e] 更接近“验证、过滤与重标后再训练”的数据 flywheel；[Zho24e] 则更适合视为 evaluator-mediated filtering 与 policy learning 的交界情形；[Zha26] 和 [Sar24b] 也都涉及显著的 composite transformation，但前者同时混合了 intrinsic reward shaping，后者则保留了较强的 memory-writing 与 inference-time reuse 色彩。因此，若以 Refinement-Mediated Policy Internalization 为主线，正文应以 [Ge26, Yua25c, Wan25x, Xu26j, Din26, Xio24, Son24, Yan24m, Wu25b, Wan26al, Ye26f, Ala25] 为核心展开，而将其余工作作为边界补充更为稳妥。
```

### Other Composite Experience Pipelines

第三类方法是 Other Composite Experience Pipelines。它收纳那些确实满足 Composite 条件，但不以 evaluator–policy co-evolution 或 refinement-mediated policy internalization 为核心的复合路径。这一类并不是一个单一机制完全统一的类别，而是一个保守的剩余类：其中的论文都包含多阶段 experience transformation，并且中间的 generation、filtering、verification、simulation、search、selection、relabeling 或 scheduling 机制是方法贡献的重要组成部分；但这些机制不一定表现为 V-Par 与 \(\pi\)-Par 的共同演化，也不一定表现为 raw experience 到 refined artifact 再到 policy 的内化过程。

这类方法中最常见的结构是 \(\pi\)-Par \(\rightarrow\) N-Tok / S-Tok \(\rightarrow\) \(\pi\)-Par。policy、teacher model、simulator-like model 或 world model 首先外化出 trajectories、demonstrations、interaction traces、synthetic tasks、search paths、GUI action sequences、robot rollouts 或 structured training examples；随后，这些 tokenized experience 被筛选、验证、选择、重标或组织成训练数据；最后，它们被用于改进 policy parameter。与 Refinement-Mediated Policy Internalization 不同，这里的中间步骤不一定是 reflection、repair、skill extraction 或 narrative/schematic refinement，而可能更侧重于 experience generation、coverage expansion、automatic verification、search-based exploration 或 simulator-based synthesis。

例如，某些方法让当前 policy 在环境中 self-rollout，随后通过 success signal、environment feedback、step-level filter、VLM judge 或 rule-based verifier 筛选高质量 trajectories，再将其用于 policy training。这类 pipeline 的核心问题是：policy 生成的经验哪些值得回灌训练，哪些应被丢弃或降权。另一些方法使用 teacher model、LLM simulator、world model 或 domain simulator 生成 synthetic experience，再通过环境执行、模拟验证或 consistency check 过滤这些经验，然后训练目标 policy。还有一些方法通过 search、MCTS、trajectory tree、branching exploration 或 multi-sample selection 构造更丰富的 experience space，再将搜索得到的高质量 trajectories、preference pairs 或 structured paths 蒸馏进 policy。

这类方法与单步 \(\pi\)-Par \(\rightarrow\) N-Tok / S-Tok externalization 的区别在于，生成 tokenized experience 不是最终目标。外化出的 trajectories、tasks 或 demonstrations 必须进一步被消费，用于训练、优化或改进 policy。它们也不同于普通 N-Tok / S-Tok \(\rightarrow\) \(\pi\)-Par training，因为训练数据不是静态给定的，而是在 pipeline 中通过 policy rollout、teacher synthesis、simulation、search 或 exploration 动态产生，并通过特定 integration mechanism 变成可训练经验。因此，这类方法的贡献通常不在某一次单独的生成或训练，而在于“如何产生足够可靠、足够多样、足够贴近目标分布的 experience，并将其转化为有效 policy update”。

Other Composite Experience Pipelines 的共同思想是，agent experience 的规模、覆盖率和质量可以通过主动生成与选择机制得到扩展。相比只依赖人工 demonstrations 或固定离线数据，这类方法能够利用 agent 自身、teacher model 或 simulator 持续产生新的经验，从而形成数据飞轮。对于 web、GUI、robotics 和 embodied control 等需要大量交互数据的任务，这种机制尤其重要，因为真实标注成本高，而环境或模拟器反馈又可以提供部分自动验证信号。

这类方法的优势在于可扩展性和工程灵活性。它们可以通过 self-rollout 扩大经验池，通过 simulator 降低真实交互成本，通过 search 发现高质量轨迹，通过 filtering 控制训练噪声，通过 teacher generation 提供跨任务 demonstrations。它们也能与其他 pathway 组合，例如生成的 trajectories 可以进一步进入 evaluator training，或者经过 refinement 后再进入 policy internalization。因此，第三类在机制上更异质，但反映了 Composite pipeline 的一个重要趋势：经验不只是被动记录，而是可以被主动生成、选择和重用。

然而，正因为这一类方法较为异质，它也更容易出现归类风险。首先，如果一篇论文只是使用 off-the-shelf teacher model 生成数据，再用常规 SFT 训练 policy，而没有提出关键的筛选、验证、搜索或闭环机制，那么它不应被归入 Composite。其次，如果中间机制只是工程流水线的一部分，而非论文主要实证 claim 所依赖的对象，也应更谨慎地归入单 pathway。再次，self-generated 或 simulator-generated experience 可能存在分布偏差、覆盖不足和错误累积问题。policy 当前不会探索的行为很难被生成；simulator 的错误可能被下游 policy 内化；teacher model 的偏差也可能通过 synthetic data 传递给 student policy。因此，这类方法通常需要依赖 diversity control、environment verification、step-level filtering、hard negative construction、human correction、search-based exploration 或 external validation 来保证经验质量。

因此，Other Composite Experience Pipelines 在本文中作为一个剩余但必要的类别存在。它提醒我们，并非所有 Composite 方法都能被整齐地归入 evaluator–policy co-evolution 或 refinement-mediated internalization。有些工作的核心贡献在于如何生成经验，有些在于如何验证经验，有些在于如何通过 search 或 simulation 扩展经验空间。尽管这些方法之间机制差异较大，它们共同体现了 Composite transformation 的基本特征：经验在多个载体和处理步骤之间流动，中间衔接机制决定了经验能否真正成为可复用、可训练、可泛化的 agent improvement signal。

论文：
- OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis
- OpenWebVoyager: Building Multimodal Web Agents via Iterative Real-World Exploration, Feedback and Optimization
- AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials
- Bootstrapping Language-Guided Navigation Learning with Self-Refining Data Flywheel
- MCTS-EP: Empowering Embodied Planning with Online Preference Optimization
- Self-Improving Vision-Language-Action Models with Data Generation via Residual RL
- Scalable Data Synthesis for Computer Use Agents with Step-Level Filtering
- Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents
- AutoSurfer -- Teaching Web Agents through Comprehensive Surfing, Learning, and Modeling
- WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning
- Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents
- DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning
- BLAZER: Bootstrapping LLM-based Manipulation Agents with Zero-Shot Data Generation

```
### Other Composite Experience Pipelines

与 evaluator–policy co-evolution 或 reflection-mediated internalization 不同，这一类方法的核心并不在于学习一个不断共演化的 evaluator，也不主要依赖对原始经验的反思式修复；它们更典型的做法是，先主动生成、扩展或重组 experience space，再通过 verification、filtering、search 或 replay 等中间机制，将这些原始交互经验转化为可被 policy 消费的训练信号。换言之，这类工作真正的方法贡献，往往不在于“又收集了一批轨迹”，而在于如何把本来噪声较大、覆盖不均或任务形式不稳定的 agent experience，组织成质量更高、分布更合适、监督形式更明确的 policy improvement signal。

一条最清晰的子脉络，是由 exploration 或 task synthesis 驱动的数据构造链。OS-Genesis [Sun24b] 代表性地将 GUI exploration 置于 task construction 之前：方法先在环境中进行 interaction-driven traversal，收集 action-centered traces，再反向合成 high-level tasks，并借助 trajectory reward model 对生成出的完整轨迹做分级采样，从而把“先探索、后命题、再训练”的链式衔接本身变成方法核心。类似地，AgentTrek [Xu24] 并不把 web tutorial 直接视作训练语料，而是先将其转写为结构化 task specification，再在真实环境中执行 guided replay 生成 multimodal trajectories，并经由 VLM evaluator 验证 instruction adherence 与 goal completion，最终得到可用于 agent training 的高质量轨迹数据。AutoSurfer [Fai26] 则进一步强调 website coverage 的系统化构造：它先以 breadth-first 方式探索网站，基于探索路径合成 grounded tasks，再利用同一批 exploration trajectories 作为 hints 引导 trajectory refinement，最后转成 SFT 数据训练 web agent。相比之下，OpenWebVoyager [He24e] 更接近在线闭环自举：模型先通过 imitation learning 获得初始 web policy，再在真实网页中持续 self-exploration，并由外部 judge 对 rollout 结果进行 trajectory-level rejection sampling，只把 judged-good trajectories 回灌到后续训练；这里的关键已不是普通 online collection，而是 exploration、judging 与 selective optimization 组成的闭环经验转化机制。

另一条重要脉络，是 synthetic or self-generated experience 经由验证与筛选后再进入 policy internalization。Bootstrapping Language-Guided Navigation Learning with Self-Refining Data Flywheel [Wan24ad] 构造了一个 generator–navigator self-refining flywheel：instruction generator 从无标注轨迹生成指令，navigator 再依据执行一致性指标筛选高保真样本，这些样本反过来提升 generator，并继续产生更好的 navigator training data；经验在 generator 与 navigator 之间不是单向流动，而是在 fidelity-based filtering 的作用下反复被重整。BLAZER [Das25] 则体现了 simulator-backed generate-verify-train 的典型范式：强 LLM 在 simulator 中零样本生成 manipulation demonstrations，环境执行负责验证成功与否，只有 automatically verified demonstrations 被保留下来用于微调较小的 manipulation agent。Scalable Data Synthesis for Computer Use Agents with Step-Level Filtering [He25g] 更进一步把“成功轨迹”本身重新问题化：该文指出即便整体成功的 CUA trajectories 也包含大量局部错误或次优动作，因此方法对每一步执行 step-level grading，只让高质量 steps 贡献监督损失，同时保留错误步骤作为上下文，从而把 noisy rollout 重新编译为 graded supervision。与此相近，PLD [Xia25h] 先训练 residual actor 去 probe base VLA 的 failure regions，再通过 hybrid rollout 收集既贴近 base-policy deployment distribution、又包含 recovery behavior 的成功轨迹，最后将这些经分布校准的数据蒸馏回 generalist VLA；其关键正在于 probe、curate、distill 三阶段对经验分布的主动塑形，而非单纯的 residual RL 或后续 SFT。

第三类强匹配工作则更强调 search 或 contrastive restructuring 对经验的再组织。MCTS-EP [Xu25q] 使用 MCTS 在 embodied environment 中扩展 trajectory space，不仅提取成功路径，还在分支节点上根据搜索得到的 long-horizon value 构造 preference pairs，并分别用于 SFT 与 DPO 更新 policy；在这里，search 不只是求解器，而是将原始交互经验重组为 success trajectories 与 structured preferences 两种训练载体的关键中介。Trial and Error [Son24] 同样不是直接对探索轨迹做 RL，而是让 agent 主动探索并显式收集 failure trajectories，再把 failure–success pairs 转换为 DPO 所需的 contrastive training data，以较低方差的 preference optimization 取代直接在线优化。Agent Q [Put24] 则把这一思路推进到更结构化的形态：方法通过 MCTS 生成搜索树和多分支轨迹，并结合 critic ranking 与 outcome reward 形成 node-level preference signal，再将这些 search-derived preferences 编译成 DPO 训练数据；其复合性恰恰体现为 search experience 从“探索过程”进一步转化为“可监督 artifact”。

在更偏 RL 的系统中，也可以看到相似但相对边界化的 composite 倾向。WebRL [Qi24] 通过 failure-driven curriculum generation、task filtering、ORM-based trajectory judging 与 replay selection，把 self-evolving task construction 与 off-policy RL 串成一条数据管线；DigiRL [Bai24] 则在真实 device environment 中结合 VLM-based AutoEval、instruction-level curriculum selection 与 step-level filtering，再以 advantage-weighted regression 更新 policy。这些工作与前述代表性方法共享“先生成或收集经验，再经中间机制重构监督，再做 policy update”的总体框架，但其叙述重心更偏向 RL training system，因此在本小节中更适合作为补充性例子，而非最核心的原型。

总体看，Other Composite Experience Pipelines 的共同趋势在于：经验不再被视为可直接回放的原始轨迹，而被当作需要经过二次组织、验证和编译的中间材料。无论是由 exploration 派生 task，再派生 trajectory [Sun24b, Xu24, Fai26]，还是由 simulator、自生成 rollout 或 failure probing 派生经过筛选的 training data [Wan24ad, Das25, He25g, Xia25h]，抑或是由 search tree 和 failure branch 派生 preference-style supervision [Xu25q, Son24, Put24]，真正决定方法效果的，都是这些中间 transformation steps 如何把原始 agent experience 变成更可靠、更高价值、也更可被 policy 内化的学习信号。

```

## Summary

总体而言，Composite Experience Transformation Pipelines 将 agent experience 的复用从单一载体转化扩展为跨载体、跨模块、跨阶段的链式或闭环过程。Evaluator–Policy Co-Evolution 关注 V-Par 与 \(\pi\)-Par 如何在同一学习闭环中相互校准和共同演化；Refinement-Mediated Policy Internalization 关注 raw N-Tok experience 如何先被反思、修复、校准、净化或形式化，再被写入 \(\pi\)-Par；Other Composite Experience Pipelines 则收纳那些以 experience generation、filtering、verification、simulation、search 或 selection 为核心的异质复合路径。

这三类方法共同表明，LLM-based agent 的经验复用问题不只是“经验存储在哪里”，也不只是“经验最终是否训练进模型”，而是经验在不同载体之间转化时如何保持有效性、可验证性和可迁移性。Composite 方法的潜在收益在于，它们能够更充分地利用失败经验、过程反馈、synthetic experience、search results 和 evaluator signals；但其风险也更高，因为每一个中间步骤都可能引入新的噪声、偏差或错误归因。因此，在评价 Composite pipeline 时，应重点考察其 integration mechanism 是否必要、是否经过消融验证、是否能防止错误经验累积，以及是否真正提升了 agent 在新任务和新环境中的泛化能力。