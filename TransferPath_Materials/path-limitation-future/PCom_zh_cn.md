# Experience transformation gaps from paper set

# 论文集中的经验转化缺口


##### [**Undermind**](https://undermind.ai)

##### [**Undermind**](https://undermind.ai) 来源


---


## Table of Contents

- [Challenges](#challenges)
  - [Warm-start dependence remains structural](#warm-start-dependence-remains-structural)
  - [Verification remains the decisive weak link](#verification-remains-the-decisive-weak-link)
  - [Credit assignment remains unresolved across levels of granularity](#credit-assignment-remains-unresolved-across-levels-of-granularity)
  - [Failure reuse is promising, but still fragile](#failure-reuse-is-promising-but-still-fragile)
  - [Self-improvement loops still go stale or self-confirm](#self-improvement-loops-still-go-stale-or-self-confirm)
  - [Experience carriers still lose crucial state](#experience-carriers-still-lose-crucial-state)
  - [Evaluation still hides the hardest parts of the problem](#evaluation-still-hides-the-hardest-parts-of-the-problem)
- [Future directions](#future-directions)
  - [Failure-native pipelines are the clearest underdeveloped direction](#failure-native-pipelines-are-the-clearest-underdeveloped-direction)
  - [Evaluators need to co-evolve and become more grounded](#evaluators-need-to-co-evolve-and-become-more-grounded)
  - [Credit assignment should become adaptive rather than doctrinal](#credit-assignment-should-become-adaptive-rather-than-doctrinal)
  - [Internalization methods need to avoid both prompt crutches and over-cleaning](#internalization-methods-need-to-avoid-both-prompt-crutches-and-over-cleaning)
  - [Richer multimodal carriers need direct comparison, not isolated proposals](#richer-multimodal-carriers-need-direct-comparison-not-isolated-proposals)
  - [Transfer-first evaluation should replace near-distribution reporting](#transfer-first-evaluation-should-replace-near-distribution-reporting)
- [References](#references)

## Challenges

## 挑战


| Challenge | Why it is still undercovered | Representative support |
|:---|:---|:---|
| Bootstrapping still depends on strong seeds, strong teachers, or both | Most pipelines need a competent base policy, successful traces, or a stronger evaluator before self-improvement becomes productive | \[Son24\], \[Xia25h\], \[He25g\], \[Li26n\], \[Yua25c\], \[Bai24\] |
| Verification is still the main bottleneck in turning experience into supervision | LLM judges, reward models, and replay verifiers remain noisy enough that transformed data cannot be treated as clean ground truth | \[Xia25e\], \[Sun24b\], \[Xu24\], \[He24e\], \[Din26\], \[Das25\], \[Zho24e\] |
| Credit assignment is unresolved across trajectory, turn, and step scales | Dense signals help, but naive step signals are unstable, while coarse signals miss the real point of failure | \[Son24\], \[Xio24\], \[Wan25x\], \[Wan26aj\], \[Pan26\], \[Wan26u\], \[Xu26j\] |
| Failure is useful, but current reuse schemes are still brittle and narrow | The best recent methods salvage only certain failure types and often need heavy filtering, relabeling, or purification to avoid poisoning learning | \[Din26\], \[Yua25c\], \[Xu26j\], \[He25g\], \[Son24\], \[Ge26\] |
| Self-improvement loops still drift, stale, or overfit to their own transformed experience | Policy, critic, and skill distributions move during training, and many loops become unstable or locally self-confirming | \[Li26l\], \[Li26n\], \[Wan26aj\], \[Wan26al\], \[Ye26f\], \[Qi24\], \[Bai24\] |
| Carrier and representation choices still erase crucial state | Many methods compress experience into text, hints, skills, or purified traces that lose visual, temporal, or causal detail needed later | \[Sin25b\], \[Xu25q\], \[Sar24b\], \[Wu25b\], \[Zho24e\], \[Das25\] |
| Evaluation still flatters progress by simplifying the hard parts | Many papers narrow websites, tasks, action spaces, or reward definitions in ways that make transformed experience look cleaner than it is | \[He24e\], \[Xu24\], \[Fai26\], \[Qi24\], \[Bai24\], \[Sar24b\], \[Das25\] |

| 挑战 | 仍未充分覆盖的原因 | 代表性支持文献 |
|:---|:---|:---|
| 引导启动仍依赖强种子、强教师或二者兼有 | 多数流水线需要有能力的基础策略、成功轨迹或更强评估器，自我改进才会有产出 | \[Son24\], \[Xia25h\], \[He25g\], \[Li26n\], \[Yua25c\], \[Bai24\] |
| 验证仍是把经验转为监督的主要瓶颈 | 大语言模型 裁判器、奖励模型和回放验证器仍然噪声较大，使被转化数据不能被视为干净真实标注 | \[Xia25e\], \[Sun24b\], \[Xu24\], \[He24e\], \[Din26\], \[Das25\], \[Zho24e\] |
| 信用分配在轨迹、轮次和步骤尺度上仍未解决 | 稠密信号有帮助，但朴素步骤信号不稳定，粗粒度信号又错过真正失败点 | \[Son24\], \[Xio24\], \[Wan25x\], \[Wan26aj\], \[Pan26\], \[Wan26u\], \[Xu26j\] |
| 失败有用，但当前复用方案仍脆弱且狭窄 | 最近最好的方法只挽救某些失败类型，并常需要重度过滤、重新标注或净化来避免污染学习 | \[Din26\], \[Yua25c\], \[Xu26j\], \[He25g\], \[Son24\], \[Ge26\] |
| 自我改进循环仍会漂移、陈旧或自我确认 | 策略、批评器和技能分布在训练中移动，许多循环会变得不稳定或局部自我确认 | \[Li26l\], \[Li26n\], \[Wan26aj\], \[Wan26al\], \[Ye26f\], \[Qi24\], \[Bai24\] |
| 载体和表示选择仍会擦除关键状态 | 许多方法把经验压缩为文本、提示、技能或净化轨迹，丢失之后需要的视觉、时间或因果细节 | \[Sin25b\], \[Xu25q\], \[Sar24b\], \[Wu25b\], \[Zho24e\], \[Das25\] |
| 评估仍通过简化难点来美化进展 | 许多论文缩窄网站、任务、动作空间或奖励定义，让被转化经验看起来比实际更干净 | \[He24e\], \[Xu24\], \[Fai26\], \[Qi24\], \[Bai24\], \[Sar24b\], \[Das25\] |

### Warm-start dependence remains structural

### 暖启动依赖仍是结构性的


The literature still does not show a reliable way to start from mostly bad interaction data and climb upward without a strong seed. \[Son24\] is unusually direct: Table 5 shows that ETO without behavioral cloning drops to 12.5 average reward, below the untuned base model at 17.9, so failure-based contrastive learning does not bootstrap itself. \[Xia25h\] states in Section 5.2 that PLD assumes a non-zero base success rate for warm-start exploration. \[He25g\] makes the same dependency operational. Section 10 notes that if the teacher does not produce successful computer-use trajectories, the synthesis pipeline has nothing usable to distill. \[Yua25c\] identifies the same problem in reflective self-training. Section 3.2 says the early model discovers only a limited number of optimal trajectories, so the whole revision loop is bottlenecked by cold-start scarcity. \[Bai24\] also begins from AutoUI-Base checkpoints rather than raw exploration.

文献仍未展示一种可靠方式，能从主要是坏交互数据出发，在没有强种子的情况下向上爬升。\[Son24\] 异常直接：表 5 显示，没有行为克隆的 ETO 平均奖励降到 12.5，低于未调优基础模型的 17.9，因此基于失败的对比学习无法自我引导启动。\[Xia25h\] 在第 5.2 节指出，PLD 假设基础策略存在非零成功率以进行暖启动探索。\[He25g\] 将同一依赖操作化。第 10 节指出，如果教师无法生成成功的计算机使用轨迹，合成流水线就没有可蒸馏的可用内容。\[Yua25c\] 在反思式自训练中识别出同样问题。第 3.2 节说，早期模型只能发现有限数量的最优轨迹，因此整个修订循环受冷启动稀缺制约。\[Bai24\] 也从 AutoUI-Base checkpoint 开始，而非从原始探索开始。

The stronger claim is that even papers marketed as self-evolving remain teacher bootstrapped. \[Li26n\] uses GPT-4o as the general-purpose reward model during the “early stages” in Section 4.1. \[Sun24b\] relies on GPT-4o both for reverse task synthesis and for the trajectory reward model in Section 4.1. \[Xu24\] filters tutorials with GPT-4o-mini and then validates replay with a VLM evaluator whose accuracy is only 84 percent in Appendix D. **Inference.** The field has many flywheels, but very few genuine ignition mechanisms. Most current systems begin after competence already exists, either in the policy, the teacher, or the verifier \[Son24, Xia25h, He25g, Li26n, Yua25c\].

更强的主张是，即便以自演化为宣传点的论文也仍由教师引导启动。\[Li26n\] 在第 4.1 节的“early stages”中使用 GPT-4o 作为通用奖励模型。\[Sun24b\] 在第 4.1 节同时依赖 GPT-4o 进行反向任务合成和轨迹奖励建模。\[Xu24\] 用 GPT-4o-mini 过滤教程，再用 视觉语言模型 评估器验证回放，而附录 D 中该评估器准确率只有 84%。**推断。** 该领域有许多飞轮，但很少有真正的点火机制。多数当前系统是在能力已经存在之后才开始，无论这种能力位于策略、教师还是验证器 \[Son24, Xia25h, He25g, Li26n, Yua25c\]。

### Verification remains the decisive weak link

### 验证仍是决定性薄弱环节


Across this paper set, experience is rarely reused directly. It is filtered, relabeled, judged, or purified first, and that verification layer is still noisy. \[Xia25e\] builds a custom benchmark because no standard GUI reward benchmark exists, then shows in Table 7 that unified history-aware reward modeling helps. Yet Section 5 still admits that the reward model may produce suboptimal signals and cannot guarantee fully correct expanded trajectories. \[Sun24b\] uses a GPT-4o-based trajectory reward model to filter synthesized trajectories, but Section 5.3 shows performance saturating around 1,500 trajectories, which suggests that more generated data does not solve judgment noise by itself. \[Xu24\] reports only 84 percent agreement for its evaluator in Appendix D, while Appendix H shows failures caused by tutorial expiration and website change. \[He24e\] leans on GPT-4o as both auto-evaluator and improvement signal, and Section 4.3 admits cross-website gains are unstable.

在这一论文集中，经验很少被直接复用。它会先被过滤、重新标注、裁判或净化，而这个验证层仍有噪声。\[Xia25e\] 构建自定义基准，因为不存在标准 图形界面 奖励基准，随后在表 7 中显示统一的历史感知奖励建模有帮助。但第 5 节仍承认，奖励模型可能产生次优信号，无法保证扩展轨迹完全正确。\[Sun24b\] 使用基于 GPT-4o 的轨迹奖励模型过滤合成轨迹，但第 5.3 节显示性能在约 1,500 条轨迹处饱和，这暗示更多生成数据本身无法解决判断噪声。\[Xu24\] 在附录 D 中报告其评估器只有 84% 一致性，而附录 H 显示教程过期和网站变化会造成失败。\[He24e\] 依赖 GPT-4o 同时作为自动评估器和改进信号，第 4.3 节承认跨网站收益不稳定。

The same bottleneck appears in hindsight and robotics settings. \[Din26\] adds a multi-stage validation loop because naive relabeling is harmful. Table 2 shows that removing the confidence filter increases noise from 2.3 percent to 14.8 percent, and random relabeling loses 6.0 points versus full AgentHER. \[Das25\] can only transform manipulation experience because the simulator provides an automatic verification operator in Section III-B. When that strong verifier disappears, the method’s premise weakens sharply. \[Zho24e\] reaches a related conclusion from language feedback: Appendix G shows weaker judges identify spurious actions as productive, and Table 3 shows that direct action imitation can underperform simple behavioral cloning. **Inference.** The field’s real limiting reagent is not raw experience volume. It is verifier reliability at the level where the transformation happens \[Xia25e, Xu24, Din26, Das25, Zho24e\].

同一瓶颈也出现在 hindsight 和机器人设置中。\[Din26\] 增加多阶段验证循环，因为朴素重新标注有害。表 2 显示，移除置信过滤会使噪声从 2.3% 增至 14.8%，随机重新标注比完整 AgentHER 低 6.0 点。\[Das25\] 能够转化操控经验，是因为模拟器在第 III-B 节提供了自动验证算子。当这种强验证器消失时，方法前提会明显变弱。\[Zho24e\] 从语言反馈得到相关结论：附录 G 显示较弱裁判器会把虚假动作识别为有用，表 3 显示直接动作模仿可能弱于简单行为克隆。**推断。** 该领域真正的限制性试剂不是原始经验体量，而是转化发生层面的验证器可靠性 \[Xia25e, Xu24, Din26, Das25, Zho24e\]。

### Credit assignment remains unresolved across levels of granularity

### 信用分配在不同粒度层面仍未解决


Several papers show that outcome-only supervision is too coarse, but they disagree on what finer signal should replace it. \[Son24\] finds in Table 4 that step-level contrastive data is dramatically worse than trajectory-level data, with average reward dropping from 67.4 to 8.3. \[Xio24\] moves in the opposite direction and argues that iterative step-level refinement is helpful, but Table 4 also shows performance peaking at iteration 4 and then dropping at iteration 5, while Section 5.3 admits Monte Carlo step scoring is noisy. \[Wan25x\] identifies deviations with Monte Carlo step rewards, yet Section 7 lists the heavy cost of reward construction and the inability to handle multiple deviated actions as core limitations. \[Xu26j\] shows why crude token or trajectory credit is problematic: Section 3 argues that GRPO reinforces erroneous reasoning inside successful solutions, while Appendix B reports that using erroneous tool calls as negative DPO pairs can trigger late-stage collapse.

若干论文显示仅结果监督过于粗糙，但它们不同意应由哪种更细信号替代。\[Son24\] 在表 4 中发现，步骤级对比数据明显弱于轨迹级数据，平均奖励从 67.4 降到 8.3。\[Xio24\] 走向相反方向，认为迭代式步骤级 修订 有帮助，但表 4 也显示性能在第 4 轮达到峰值并在第 5 轮下降，第 5.3 节还承认 Monte Carlo 步骤评分有噪声。\[Wan25x\] 用 Monte Carlo 步骤奖励识别偏差，但第 7 节把奖励构建成本高和无法处理多个偏差动作列为核心限制。\[Xu26j\] 显示了为什么粗糙 词元 或轨迹信用有问题：第 3 节认为 组相对策略优化 会强化成功解中的错误推理，而附录 B 报告，将错误工具调用作为负 直接偏好优化 对会触发后期崩溃。

The deeper problem is that different papers need different supervision units. \[Wan26aj\] maps verbal self-guidance into small scalar rewards at each step, but Figure 5 shows that full-strength internal reward too early harms performance, and Appendix B reports query looping in WebShop rising from 17.5 percent to 67.8 percent. \[Pan26\] argues that whether a critic helps depends on explained variance, not on a fixed PPO versus GRPO commitment. Figure 5 shows critic usefulness can even regress mid-training in FrozenLake. \[Wan26u\] mixes outcome and process signals, but Table 2 reveals a trade-off between optimizing the policy and optimizing the reward model’s own process accuracy. **Inference.** The open question is no longer whether denser feedback helps. It is when a denser signal is causally aligned with eventual success and when it is only a more convenient proxy \[Son24, Xio24, Wan25x, Pan26, Wan26aj, Wan26u, Xu26j\].

更深层问题是，不同论文需要不同监督单元。\[Wan26aj\] 把语言化自我指导映射成每步小标量奖励，但图 5 显示，过早使用全强度内部奖励会损害性能，附录 B 报告 WebShop 中查询循环从 17.5% 上升到 67.8%。\[Pan26\] 认为批评器是否有帮助取决于解释方差，而非固定选择 PPO 或 组相对策略优化。图 5 显示，批评器有用性甚至会在 FrozenLake 训练中期退化。\[Wan26u\] 混合结果和过程信号，但表 2 揭示了优化策略与优化奖励模型自身过程准确率之间的权衡。**推断。** 开放问题已不再是稠密反馈是否有帮助，而是稠密信号何时与最终成功存在因果对齐，何时只是更方便的代理 \[Son24, Xio24, Wan25x, Pan26, Wan26aj, Wan26u, Xu26j\]。

### Failure reuse is promising, but still fragile

### 失败复用有前景，但仍然脆弱


Some of the most interesting progress in this set comes from learning from failure rather than discarding it, but the gains are narrow and highly mediated. \[Din26\] shows that hindsight relabeling works best for incomplete trajectories and yields much smaller gains for tool errors, only 2.1 points in Figure 5 because crashes leave little salvageable signal. \[Yua25c\] finds that self-corrected trajectories can outperform GPT-4o “optimal” trajectories for training the base agent, but the whole loop depends on the model already being able to identify the first error in Section 3.1. \[Xu26j\] goes further by purifying failed trajectories with SAAR, yet Section 4.3 says 30 percent raw trajectories must be kept for the 7B model to preserve robustness. Full purification makes the learner brittle. \[He25g\] also shows that even successful trajectories contain many wrong steps. Table 2 finds that fewer than half the steps in successful traces are correct, so success labels cannot be reused naively.

这一组中部分最有意思的进展来自从失败中学习，而非丢弃失败，但收益狭窄且高度依赖中介机制。\[Din26\] 显示 事后重新标注 最适合不完整轨迹，对工具错误收益小得多，图 5 中只有 2.1 点，因为崩溃留下的可挽救信号很少。\[Yua25c\] 发现，自我修正轨迹在训练基础智能体时可以优于 GPT-4o “最优”轨迹，但整个循环依赖模型在第 3.1 节中已经能够识别第一个错误。\[Xu26j\] 进一步通过 SAAR 净化失败轨迹，但第 4.3 节说 7B 模型必须保留 30% 原始轨迹才能保持鲁棒性。完全净化会让学习器变脆。\[He25g\] 也显示，即便成功轨迹也包含许多错误步骤。表 2 发现，成功轨迹中少于一半步骤正确，因此不能朴素复用成功标签。

The hidden difficulty is that each paper salvages a different slice of failure. \[Ge26\] argues in Table 4 that rehearsal on successful rollouts is not enough and that counterfactual correction is what lifts Pass@128. \[Son24\] uses failure as trajectory-level negative evidence but cannot localize the bad action without destabilizing training. \[Wan25x\] calibrates at the first deviation only, then lists multi-deviation calibration as future work in Section 7. **Inference.** The field still lacks a general representation of failure that preserves at least four things together: where the trajectory went wrong, why it went wrong, what repair was attempted, and whether the repair generalized beyond that episode \[Din26, Yua25c, Xu26j, He25g, Ge26, Wan25x\].

隐藏困难在于，每篇论文都只挽救失败的不同切片。\[Ge26\] 在表 4 中认为，仅在成功采样轨迹上排练不足够，真正提高 128 次通过率 的是反事实纠正。\[Son24\] 把失败作为轨迹级负证据，但无法在不扰乱训练的情况下定位坏动作。\[Wan25x\] 只在第一次偏差处校准，随后在第 7 节把多偏差校准列为未来工作。**推断。** 该领域仍缺少一种通用失败表示，能同时保留至少四件事：轨迹哪里出错、为什么出错、尝试了什么修复，以及修复是否泛化到该 片段 之外 \[Din26, Yua25c, Xu26j, He25g, Ge26, Wan25x\]。

### Self-improvement loops still go stale or self-confirm

### 自我改进循环仍会陈旧或自我确认


The newest papers increasingly agree that transformed experience becomes stale as soon as the policy changes. \[Li26l\] is the clearest statement of the problem. Figure 3 shows fail-pattern drift over training, and Table 2 shows that removing critic evolution hurts much more than removing saturation-aware shaping. \[Li26n\] also presents a closed-loop reward reflux system, but Table 5 shows that combining domain-specific and general-purpose reward models actually hurts moderate-difficulty tasks relative to the domain-specific model alone. \[Wan26al\] finds that letting the teacher own rollout generation causes catastrophic off-policy collapse, and Table 2 shows frozen teachers plateau far below evolving ones. \[Ye26f\] reaches a parallel result from another angle: Figure 6 shows off-policy context distillation causes catastrophic forgetting of general capabilities, while on-policy consolidation avoids that failure.

最新论文越来越同意，被转化经验会在策略变化后立即陈旧。\[Li26l\] 对这个问题表述最清楚。图 3 显示训练中失败模式漂移，表 2 显示移除批评器演化的伤害远大于移除饱和感知塑形。\[Li26n\] 也提出闭环奖励 reflux 系统，但表 5 显示，组合领域特定和通用奖励模型实际上会损害中等难度任务，相对于只用领域特定模型更差。\[Wan26al\] 发现，让教师掌握采样轨迹生成会造成灾难性离策略崩溃，表 2 显示冻结教师的平台期远低于演化教师。\[Ye26f\] 从另一个角度得到并行结果：图 6 显示离策略上下文蒸馏会造成一般能力灾难性遗忘，而在线策略整合可避免该失败。

The same pattern appears in environment-facing agents. \[Qi24\] uses replay buffers, KL control, and confidence filtering because the policy otherwise drifts toward recent tasks and forgets older behavior. Appendix C shows a real cross-site trade-off, with Map performance declining while other sites improve. \[Bai24\] demonstrates policy staleness directly in Figure 4, where frozen device-control policies degrade over days as the environment changes. \[He24e\] shows a subtler version of the same issue: Section 4.4 says iterative optimization makes trajectories shorter, but this also increases hallucinated early stopping. **Inference.** Current loops are better described as moving-target supervision systems than as simple self-improvement pipelines. They still need principled mechanisms for evaluator refresh, replay selection, and anti-collapse control \[Li26l, Li26n, Wan26al, Ye26f, Qi24, Bai24, He24e\].

同一模式也出现在面向环境的智能体中。\[Qi24\] 使用回放缓冲区、KL 控制和置信过滤，因为策略否则会漂向近期任务并遗忘旧行为。附录 C 显示真实跨站点权衡：Map 性能下降，而其他站点改进。\[Bai24\] 在图 4 中直接展示策略陈旧性：冻结设备控制策略会随着环境变化在数天内退化。\[He24e\] 展示了同一问题的更细微版本：第 4.4 节说迭代优化使轨迹变短，但这也增加了幻觉式提前停止。**推断。** 当前循环更适合被描述为移动目标监督系统，而非简单自我改进流水线。它们仍需要有原则的评估器刷新、回放选择和反崩溃控制机制 \[Li26l, Li26n, Wan26al, Ye26f, Qi24, Bai24, He24e\]。

### Experience carriers still lose crucial state

### 经验载体仍会丢失关键状态


A recurring limitation is that transformed experience often becomes easier to train on by becoming less faithful to the original interaction. \[Sin25b\] improves VLM feedback by adding trajectory sketches, but Section VI still says the method is bounded by the underlying VLM and would likely need intermediate views or subgoal annotations for long-horizon tasks. \[Xu25q\] uses selective state representation, keeping only the current image and converting history into text in Section 3.3, which is an implicit compression gamble in visually grounded planning. \[Sar24b\] reports a strong embodied abstraction story, but Table 1 shows success dropping from 35.1 percent with ground-truth perception to 10.5 percent with estimated perception, so the distilled program of thought cannot repair missing perception. Table S1 also shows that full text trajectory memory can beat the more visibly multimodal variant on VisualWebArena. \[Wu25b\] narrows reflection data mostly to visual and action-grounded errors and says in Appendix B that deeper planning failures are not yet covered.

一个反复出现的限制是，被转化经验常通过降低对原始交互的忠实度来变得更易训练。\[Sin25b\] 通过加入轨迹草图来改进 视觉语言模型 反馈，但第 VI 节仍说该方法受限于底层 视觉语言模型，并且长时程任务很可能需要中间视图或子目标标注。\[Xu25q\] 使用选择性状态表示，在第 3.3 节只保留当前图像，并把历史转成文本，这是视觉 有依托 规划中的隐式压缩赌注。\[Sar24b\] 报告了强具身抽象叙事，但表 1 显示，使用真实感知时成功率为 35.1%，使用估计感知时降到 10.5%，因此蒸馏出的思维程序无法修复缺失感知。表 S1 还显示，完整文本轨迹记忆可以在 VisualWebArena 上超过更明显的多模态变体。\[Wu25b\] 将反思数据主要缩窄到视觉和动作 有依托 错误，并在附录 B 中说更深层规划失败尚未覆盖。

Other papers expose the same problem from different carriers. \[Zho24e\] names the verbalization module as a core limitation, because the whole feedback loop depends on turning environmental state into faithful text. \[Das25\] trains manipulation policies from privileged simulator state, then shows in Figure 4 that success drops sharply when deployment uses visual observations instead of ground-truth state. **Inference.** Much of the current literature transforms experience by stripping away exactly the spatial, perceptual, and temporal detail that later failures depend on. This is efficient for training, but it constrains how much of the original experience can actually be reused \[Sin25b, Xu25q, Sar24b, Wu25b, Zho24e, Das25\].

其他论文从不同载体暴露出同一问题。\[Zho24e\] 把语言化模块称为核心限制，因为整个反馈循环依赖把环境状态忠实转成文本。\[Das25\] 从特权模拟器状态训练操控策略，随后在图 4 中显示，当部署使用视觉观察而非真实状态时，成功率显著下降。**推断。** 当前许多文献通过剥离空间、感知和时间细节来转化经验，而这些细节恰恰是后续失败所依赖的部分。这对训练高效，但限制了原始经验实际能被复用的程度 \[Sin25b, Xu25q, Sar24b, Wu25b, Zho24e, Das25\]。

### Evaluation still hides the hardest parts of the problem

### 评估仍遮蔽问题中最难的部分


Many gains in this set depend on evaluation choices that make the transformation problem cleaner than real deployment. \[He24e\] excludes richer interaction types such as drag and hover and still relies heavily on accessibility trees, despite presenting a multimodal web agent. \[Xu24\] narrows ScreenSpot evaluation to web-only cases aligned with its dataset and reports a replay success rate of only 39.9 percent in Appendix C, which means most harvested tutorials never become usable trajectories. \[Fai26\] caps exploration at 1,000 synthesized tasks per website and excludes Wikipedia and Maps from WebArena evaluation. \[Qi24\] evaluates on WebArena-Lite for cost reasons and uses manually reviewed GPT-4o filtered tasks. \[Bai24\] excludes portions of Android-in-the-Wild for security and account reasons despite the “in-the-wild” framing. \[Sar24b\] omits the verification stage entirely on Ego4D because the task is passive, so the full loop is not tested there. \[Das25\] depends on simulator-side ground truth and structured manipulation tasks.

这一组中的许多收益依赖评估选择，这些选择让转化问题比真实部署更干净。\[He24e\] 排除拖拽和悬停等更丰富交互类型，并且虽然呈现为多模态网页智能体，仍重度依赖 无障碍树。\[Xu24\] 将 ScreenSpot 评估缩窄到与其数据集对齐的 仅网页 案例，并在附录 C 中报告回放成功率只有 39.9%，意味着多数采集教程从未成为可用轨迹。\[Fai26\] 将探索限制为每个网站 1,000 个合成任务，并在 WebArena 评估中排除 Wikipedia 和 Maps。\[Qi24\] 出于成本原因在 WebArena-Lite 上评估，并使用人工审查的 GPT-4o 过滤任务。\[Bai24\] 尽管采用“真实环境”表述，仍因安全和账号原因排除 Android-in-the-Wild 的部分内容。\[Sar24b\] 在 Ego4D 上完全省略验证阶段，因为任务是被动的，所以完整循环没有在那里测试。\[Das25\] 依赖模拟器侧真实标注和结构化操控任务。

These are not minor implementation details. They shape what kinds of transformed experience appear to work. Binary final rewards, filtered task pools, fixed APIs, and privileged state all make experience reuse look more reliable than it is under interface drift or ambiguous partial progress. **Inference.** The literature still has stronger evidence for whether a method can exploit a curated scaffold than for whether it can robustly transform messy open-world experience into reusable knowledge \[He24e, Xu24, Fai26, Qi24, Bai24, Sar24b, Das25\].

这些不是次要实现细节。它们塑造哪些被转化经验看起来有效。二元最终奖励、过滤任务池、固定 API 和特权状态都会让经验复用看起来比接口漂移或歧义性部分进展下更可靠。**推断。** 文献对方法能否利用筛选过的脚手架已有较强证据，但对方法能否把混乱开放世界经验稳健转化为可复用知识，证据仍弱得多 \[He24e, Xu24, Fai26, Qi24, Bai24, Sar24b, Das25\]。

## Future directions

## 未来方向


| Direction | What concrete progress would look like | Core support |
|:---|:---|:---|
| Failure-native transformation pipelines | Store partial progress, failure type, repair attempt, and verified recovery rather than success-only traces | \[Din26\], \[Yua25c\], \[Xu26j\], \[Ge26\], \[Wan25x\] |
| Co-evolving and grounded evaluators | Refresh judges and reward models online while tying more of their signals to environment-checkable changes | \[Li26l\], \[Li26n\], \[Xia25e\], \[Wan26u\], \[Zho24e\] |
| Adaptive multi-scale credit assignment | Learn when to use trajectory, turn, step, or token supervision instead of fixing one granularity for all tasks | \[Pan26\], \[Wan26aj\], \[Son24\], \[Xio24\], \[Wan25x\], \[Xu26j\] |
| Internalization without prompt overfitting or purification collapse | Distill hints, skills, and reflection into policy weights while preserving robustness and exploration diversity | \[Ala25\], \[Wan26al\], \[Ye26f\], \[Ge26\], \[Wu25b\] |
| Richer multimodal carriers and cross-carrier comparisons | Compare the same underlying experience after conversion into different representations and test which details survive | \[Sin25b\], \[Sar24b\], \[Xu25q\], \[Wu25b\], \[Das25\] |
| Transfer-first evaluation and online systems reporting | Measure gains on unseen sites, changed interfaces, stale tasks, and changing environments, with full rollout economics | \[He24e\], \[Xu24\], \[Qi24\], \[Bai24\], \[Fai26\], \[Xia25h\] |

| 方向 | 具体进展形态 | 核心支持文献 |
|:---|:---|:---|
| 失败原生转化流水线 | 存储部分进展、失败类型、修复尝试和已验证恢复，而不是只保留成功轨迹 | \[Din26\], \[Yua25c\], \[Xu26j\], \[Ge26\], \[Wan25x\] |
| 共同演化且 有依托 的评估器 | 在线刷新裁判器和奖励模型，同时把更多信号绑定到环境可检查变化 | \[Li26l\], \[Li26n\], \[Xia25e\], \[Wan26u\], \[Zho24e\] |
| 自适应多尺度信用分配 | 学习何时使用轨迹、轮次、步骤或 词元 监督，而不是为所有任务固定一种粒度 | \[Pan26\], \[Wan26aj\], \[Son24\], \[Xio24\], \[Wan25x\], \[Xu26j\] |
| 避免提示依赖和过度清洗崩溃的内化 | 将提示、技能和反思蒸馏进策略权重，同时保留鲁棒性和探索多样性 | \[Ala25\], \[Wan26al\], \[Ye26f\], \[Ge26\], \[Wu25b\] |
| 更丰富多模态载体与跨载体比较 | 将同一底层经验转成不同表示后直接比较，并测试哪些细节能存活 | \[Sin25b\], \[Sar24b\], \[Xu25q\], \[Wu25b\], \[Das25\] |
| 以迁移为优先的评估和在线系统报告 | 在未见站点、变化界面、陈旧任务和变化环境上衡量收益，并完整报告采样经济性 | \[He24e\], \[Xu24\], \[Qi24\], \[Bai24\], \[Fai26\], \[Xia25h\] |

### Failure-native pipelines are the clearest underdeveloped direction

### 失败原生流水线是最清楚的未充分发展方向


This paper set already shows that partial failures can be more valuable than filtered success, but only when they are transformed with structure. \[Din26\] demonstrates the core idea with hindsight relabeling, but Figure 5 also shows the transformability of failures is highly uneven across failure types. \[Yua25c\] shows that revision trajectories derived from the model’s own errors can beat expert trajectories for training, which means repair traces are not just auxiliary metadata. They can be better supervision than pristine demonstrations. \[Xu26j\] adds a second lesson: cleaned trajectories cannot fully replace raw ones, because some noise must stay in the curriculum to preserve self-repair ability. \[Ge26\] then shows that counterfactual correction, not rehearsal alone, is what changes the capability ceiling. \[Wan25x\] suggests that the timing of correction matters too, but currently corrects only at the first deviation.

这一论文集已经显示，部分失败可以比过滤后的成功更有价值，但前提是以结构化方式转化它们。\[Din26\] 通过 事后重新标注 展示核心想法，但图 5 也显示，失败的可转化性在不同失败类型间高度不均。\[Yua25c\] 显示，由模型自身错误产生的修订轨迹可以优于专家轨迹用于训练，这意味着修复轨迹不只是辅助元数据。它们可以是比完美示范更好的监督。\[Xu26j\] 补充第二点：清洗轨迹不能完全替代原始轨迹，因为课程中必须保留一些噪声以维持自我修复能力。\[Ge26\] 随后显示，改变能力上限的是反事实纠正，而非仅仅排练。\[Wan25x\] 暗示纠正时机也重要，但目前只在第一次偏差处纠正。

Concrete progress would look like a single training object that preserves four linked fields for each imperfect episode: the best verified prefix, the diagnosed failure span, the repair attempt, and the post-repair outcome. A convincing paper would compare success-only replay, hindsight relabeling, repair-annotated replay, and mixed raw-plus-purified replay under the same rollout budget. It should measure recovery from seeded failure families, not only end-task success. That would test whether the agent is learning reusable repair skills rather than merely benefiting from cleaner labels.

实际进展应是一种单一训练对象，为每个不完美 片段 保留四个相互链接字段：最佳已验证前缀、诊断出的失败跨度、修复尝试和修复后结果。有说服力的论文应在同一采样预算下比较只含成功的回放、事后重新标注、带修复标注的回放，以及原始加净化混合回放。它应衡量从种子失败族中恢复的能力，而不只是终局任务成功率。这会测试智能体是在学习可复用修复技能，还是只受益于更干净标签。

### Evaluators need to co-evolve and become more grounded

### 评估器需要共同演化并变得更 有依托


The strongest recent papers already point toward moving judges and reward models online. \[Li26l\] shows directly that stale critics underperform as failure patterns drift. \[Li26n\] uses disagreement between domain-specific and general-purpose reward models as a reflux signal, but Table 5 also shows that more judge diversity is not automatically better. \[Xia25e\] collapses step and outcome reward into one unified reward model, which is useful, yet Section 5 still warns that reward noise can corrupt trajectory expansion. \[Wan26u\] treats environment, reward model, and policy as jointly evolving objects, and its main contribution is precisely that the reward model should not remain fixed while the task pool changes. \[Zho24e\] offers a complementary lesson from older language-feedback work: feedback is most useful when it is informative and cheap, but it is brittle when verbalization and judge quality drift.

最强近期论文已经指向在线移动裁判器和奖励模型。\[Li26l\] 直接显示，随着失败模式漂移，陈旧批评器表现较差。\[Li26n\] 使用领域特定和通用奖励模型之间的分歧作为 reflux 信号，但表 5 也显示，更多裁判器多样性并不自动更好。\[Xia25e\] 把步骤奖励和结果奖励合并到一个统一奖励模型中，这有用，但第 5 节仍警告奖励噪声可能污染轨迹扩展。\[Wan26u\] 把环境、奖励模型和策略视为共同演化对象，其主要贡献正是奖励模型不应在任务池变化时保持固定。\[Zho24e\] 从较早的语言反馈工作提供互补教训：反馈在信息量大且便宜时最有用，但当语言化和裁判器质量漂移时会很脆弱。

Concrete progress would mean evaluator systems that are both adaptive and auditable. The most promising path is not unrestricted LLM judgment. It is hybrid feedback in which some signals are tied to verifiable state changes, action effects, or partial completion, while other signals remain textual and diagnostic. Verification should report judge false positives and false negatives over training time, not only final policy wins. Right now the field has many better judges, but too little evidence about whether those judges stay calibrated after the policy moves.

实际进展意味着评估器系统既自适应又可审计。最有前景的路径不是不受限制的 大语言模型 判断，而是混合反馈：一部分信号绑定到可验证状态变化、动作效果或部分完成，另一部分信号保持文本性和诊断性。验证应报告训练过程中裁判器假阳性和假阴性，而不只报告最终策略胜利。当前领域有许多更好的裁判器，但关于这些裁判器在策略移动后是否保持校准，证据太少。

### Credit assignment should become adaptive rather than doctrinal

### 信用分配应变得自适应，而非教条化


Different papers in this set each discover that one supervision granularity is not enough. \[Pan26\] formalizes the critic question as a dynamic gating problem rather than a static algorithm choice. \[Wan26aj\] shows that step-level self-guidance is useful only under a trust schedule, because the same internal reward can help later and harm earlier. \[Son24\] shows that naive step-level contrastive supervision can be much worse than trajectory-level learning. \[Xio24\] and \[Wan25x\] show that finer-grained process signals help only when their construction is sufficiently reliable. \[Xu26j\] demonstrates that token- and action-level punishment can create reasoning-action misalignment if the correction target is too local.

这一组中不同论文都发现，单一监督粒度不足。\[Pan26\] 将批评器问题形式化为动态门控问题，而非静态算法选择。\[Wan26aj\] 显示步骤级自我指导只有在信任调度下才有用，因为同一内部奖励后期有益、早期有害。\[Son24\] 显示朴素步骤级对比监督可能远弱于轨迹级学习。\[Xio24\] 和 \[Wan25x\] 显示，更细粒度过程信号只有在其构造足够可靠时才有帮助。\[Xu26j\] 证明，如果纠正目标太局部，词元 和动作级惩罚可能制造推理-动作错配。

The undercovered direction is a learner that decides when the supervision unit should be the whole rollout, a segment, a single step, or a token block. Verification for such a system should include counterexamples where denser signals hurt. A method would be much more convincing if it could explain why it used trajectory-level supervision on one failure class and step-level repair on another. That would move the field beyond the current pattern of proposing one favored granularity per paper.

未充分覆盖的方向是让学习器决定监督单元何时应是整个采样轨迹、一个片段、单个步骤或一个 词元 块。此类系统的验证应包含稠密信号有害的反例。如果一个方法能解释为什么它在某类失败上使用轨迹级监督、在另一类失败上使用步骤级修复，它会更有说服力。这会让领域越过当前每篇论文只提出一种偏好粒度的模式。

### Internalization methods need to avoid both prompt crutches and over-cleaning

### 内化方法需要同时避免提示依赖和过度清洗


A second frontier is how to turn externalized experience into policy weights without simply teaching the model to depend on added context or overly sanitized traces. \[Ala25\] shows that hint internalization can beat ever-growing prompts, but its appendix also reveals human-written hints and balancing choices still matter, and some ablations show trade-offs across tasks rather than uniform gains. \[Wan26al\] makes the prompt-overfitting problem especially clear: skill-augmented GRPO reaches high training accuracy but collapses badly on validation, while using skills to guide the teacher rather than the student generalizes much better. \[Ye26f\] shows that raw trajectories are worse than extracted knowledge for consolidation and that off-policy context distillation causes catastrophic forgetting. \[Ge26\] shows that internalizing reflective experience can expand the capability ceiling, but Table 6 also shows auxiliary RL or early-experience targets can shrink Pass@128 while improving Pass@1. \[Wu25b\] adds a cautionary signal from GUI reflection, where regular GUI pretraining erodes reflection-related abilities before reflection tuning restores them.

第二个前沿是如何把外化经验转为策略权重，同时不只是教模型依赖新增上下文或过度净化轨迹。\[Ala25\] 显示提示内化可以击败不断增长的提示，但其附录也揭示人工提示和数据平衡选择仍重要，且某些消融显示跨任务权衡，而非均匀收益。\[Wan26al\] 尤其清楚地呈现了提示过拟合问题：技能增强 组相对策略优化 在训练准确率上很高，但验证上严重崩溃，而用技能指导教师而非学生泛化更好。\[Ye26f\] 显示，原始轨迹弱于提取知识用于整合，且离策略上下文蒸馏会导致灾难性遗忘。\[Ge26\] 显示，内化反思经验可以扩展能力上限，但表 6 也显示，辅助 强化学习 或早期经验目标会在提升 1 次通过率 的同时降低 128 次通过率。\[Wu25b\] 从 图形界面 反思提供警示信号：常规 图形界面 预训练会侵蚀反思相关能力，随后需要反思调优来恢复。

Concrete progress would mean internalization systems that report two things at once: whether the model can act without the external artifact at inference, and whether it retains robustness when new errors appear. A strong benchmark would test the same learner with hints, skills, rubrics, or reflections available only during training, then remove them at test time and measure both greedy performance and recovery from unfamiliar errors.

实际进展意味着内化系统同时报告两件事：模型在推理时没有外部工件是否还能行动，以及当新错误出现时是否保持鲁棒性。强基准应测试同一学习器在训练时可获得提示、技能、评分规程 或反思，随后在测试时移除它们，并同时衡量贪心性能和从陌生错误中恢复的能力。

### Richer multimodal carriers need direct comparison, not isolated proposals

### 更丰富多模态载体需要直接比较，而非孤立提案


Several papers suggest that the choice of carrier may matter more than the amount of experience. \[Sin25b\] shows that adding trajectory sketches resolves a real blind spot in final-state VLM judging. \[Sar24b\] shows that distilled programs of thought can beat raw noisy demonstrations, but also that text trajectory memory can outperform some multimodal variants and that estimated perception remains a hard ceiling. \[Xu25q\] quietly exposes the same issue when it compresses history into text while keeping only the current frame. \[Wu25b\] confines reflection mostly to local grounding errors, which suggests the current carrier does not yet encode higher-level planning failures well. \[Das25\] shows how a policy trained on state-rich simulator experience weakens sharply when that carrier changes to noisy visual observations.

若干论文暗示，载体选择可能比经验数量更重要。\[Sin25b\] 显示，加入轨迹草图能解决最终状态 视觉语言模型 裁判中的真实盲点。\[Sar24b\] 显示，蒸馏出的思维程序可以击败原始带噪示范，但也显示文本轨迹记忆可以超过某些多模态变体，且估计感知仍是硬上限。\[Xu25q\] 在把历史压缩为文本、同时只保留当前帧时，悄然暴露同一问题。\[Wu25b\] 把反思主要限制在局部 grounding 错误上，暗示当前载体尚未很好编码更高层规划失败。\[Das25\] 显示，在状态丰富模拟器经验上训练的策略，当载体切换为带噪视觉观察后会明显变弱。

A high-value next paper would take one fixed interaction corpus and convert it into at least three carriers such as full multimodal trace, summarized textual lesson, and structured repair artifact. The same base policy should then be trained under matched budgets. That experiment would answer a question the current literature mostly leaves implicit: which information survives conversion, and which apparent gains are really just carrier-model compatibility effects.

高价值的下一篇论文应取一个固定交互语料，并将其转为至少三种载体，例如完整多模态轨迹、摘要文本经验和结构化修复工件。随后应在匹配预算下训练同一基础策略。该实验会回答当前文献大多隐含处理的问题：哪些信息能在转换中存活，哪些表面收益其实只是载体-模型兼容性效应。

### Transfer-first evaluation should replace near-distribution reporting

### 以迁移为优先的评估应取代近分布报告


This paper set repeatedly shows that transformed experience often works best near its source distribution. \[He24e\] reports unstable cross-website improvement. \[Xu24\] is vulnerable to tutorial expiration and changing websites. \[Qi24\] improves average performance while losing ground on some sites. \[Bai24\] demonstrates that frozen policies decay as device environments change over time. \[Fai26\] improves within website families but still evaluates in a budgeted, bounded synthesis regime. \[Xia25h\] shows real generalization gains in cluttered unseen settings, yet Section 6 still calls for work on continual on-robot learning and safer exploration.

这一论文集反复显示，被转化经验通常在靠近其源分布时效果最好。\[He24e\] 报告跨网站改进不稳定。\[Xu24\] 容易受教程过期和网站变化影响。\[Qi24\] 提升平均性能的同时，在某些站点上退步。\[Bai24\] 显示冻结策略会随着设备环境随时间变化而衰减。\[Fai26\] 在网站族内部改进，但仍在有预算、有边界的合成机制中评估。\[Xia25h\] 显示在杂乱未见设置中有真实泛化收益，但第 6 节仍呼吁继续研究机器人上的持续在线学习和更安全探索。

Concrete progress would look like routine reporting across at least four axes: unseen instances, changed interfaces over time, unseen sites or apps, and shifts in observation carrier. Papers should also report the economics of those gains: rollout time, judge cost, success-to-usable-data ratio, and crash or invalid-action rates. The systems burden is part of the research problem in this area, not an appendix detail. A method that improves success only on a filtered benchmark slice but requires extremely expensive verification may still be less important than a slightly weaker method that scales to broader, noisier experience collection.

实际进展应体现为至少跨四个轴的常规报告：未见实例、随时间变化的界面、未见站点或应用，以及观察载体转移。论文还应报告这些收益的经济性：采样时间、裁判器成本、成功到可用数据比例，以及崩溃或无效动作率。系统负担是该领域研究问题的一部分，不是附录细节。一个方法如果只在过滤后的基准切片上提升成功率，却需要极其昂贵的验证，可能不如一个稍弱但能扩展到更广、更有噪声经验收集的方法重要。

---

## References

\[Son24\] Y. Song, D. Yin, X. Yue, J. Huang, S. Li, and B. Y. Lin, “Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents,” *Annual Meeting of the Association for Computational Linguistics*, pp. 7584–7600, Mar. 2024, doi: [10.48550/arXiv.2403.02502](https://doi.org/10.48550/arXiv.2403.02502).

\[Xia25h\] W. Xiao *et al.*, “Self-Improving Vision-Language-Action Models with Data Generation via Residual RL,” *ArXiv*, vol. abs/2511.00091, Oct. 2025, doi: [10.48550/arXiv.2511.00091](https://doi.org/10.48550/arXiv.2511.00091).

\[He25g\] Y. He, P. Chawla, Y. Souri, S. Som, and X. Song, “Scalable Data Synthesis for Computer Use Agents with Step-Level Filtering,” *ArXiv*, vol. abs/2512.10962, Nov. 2025, doi: [10.48550/arXiv.2512.10962](https://doi.org/10.48550/arXiv.2512.10962).

\[Li26n\] Z. Li *et al.*, “MagicGUI-RMS: A Multi-Agent Reward Model System for Self-Evolving GUI Agents via Automated Feedback Reflux,” *ArXiv*, vol. abs/2601.13060, Jan. 2026, doi: [10.48550/arXiv.2601.13060](https://doi.org/10.48550/arXiv.2601.13060).

\[Yua25c\] S. Yuan, Z. Chen, Z. Xi, J. Ye, Z. Du, and J. Chen, “Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training,” *ArXiv*, vol. abs/2501.11425, Jan. 2025, doi: [10.48550/arXiv.2501.11425](https://doi.org/10.48550/arXiv.2501.11425).

\[Bai24\] H. Bai *et al.*, “DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning,” *ArXiv*, vol. abs/2406.11896, Jun. 2024, doi: [10.48550/arXiv.2406.11896](https://doi.org/10.48550/arXiv.2406.11896).

\[Xia25e\] H. Xiao *et al.*, “UI-Genie: A Self-Improving Approach for Iteratively Boosting MLLM-based Mobile GUI Agents,” *ArXiv*, vol. abs/2505.21496, May 2025, doi: [10.48550/arXiv.2505.21496](https://doi.org/10.48550/arXiv.2505.21496).

\[Sun24b\] Q. Sun *et al.*, “OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis,” *ArXiv*, vol. abs/2412.19723, Dec. 2024, doi: [10.48550/arXiv.2412.19723](https://doi.org/10.48550/arXiv.2412.19723).

\[Xu24\] Y. Xu *et al.*, “AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials,” *ArXiv*, vol. abs/2412.09605, Dec. 2024, doi: [10.48550/arXiv.2412.09605](https://doi.org/10.48550/arXiv.2412.09605).

\[He24e\] H. He *et al.*, “OpenWebVoyager: Building Multimodal Web Agents via Iterative Real-World Exploration, Feedback and Optimization,” *Annual Meeting of the Association for Computational Linguistics*, pp. 27545–27564, Oct. 2024, doi: [10.48550/arXiv.2410.19609](https://doi.org/10.48550/arXiv.2410.19609).

\[Din26\] L. Ding, “AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling,” Mar. 22, 2026.

\[Das25\] R. J. Das *et al.*, “BLAZER: Bootstrapping LLM-based Manipulation Agents with Zero-Shot Data Generation,” *ArXiv*, vol. abs/2510.08572, Oct. 2025, doi: [10.48550/arXiv.2510.08572](https://doi.org/10.48550/arXiv.2510.08572).

\[Zho24e\] V. Zhong, D. Misra, X. Yuan, and M.-A. Côté, “Policy Improvement using Language Feedback Models,” *ArXiv*, vol. abs/2402.07876, Feb. 2024, doi: [10.48550/arXiv.2402.07876](https://doi.org/10.48550/arXiv.2402.07876).

\[Xio24\] W. Xiong *et al.*, “Watch Every Step! LLM Agent Learning via Iterative Step-level Process Refinement,” *ArXiv*, vol. abs/2406.11176, Jun. 2024, doi: [10.48550/arXiv.2406.11176](https://doi.org/10.48550/arXiv.2406.11176).

\[Wan25x\] H. Wang, J. Wang, C. T. Leong, and W. Li, “STeCa: Step-level Trajectory Calibration for LLM Agent Learning,” *Annual Meeting of the Association for Computational Linguistics*, pp. 11597–11614, Feb. 2025, doi: [10.48550/arXiv.2502.14276](https://doi.org/10.48550/arXiv.2502.14276).

\[Wan26aj\] X. Wang *et al.*, “Co-Evolution of Policy and Internal Reward for Language Agents,” Apr. 03, 2026.

\[Pan26\] C. Pan *et al.*, “EVPO: Explained Variance Policy Optimization for Adaptive Critic Utilization in LLM Post-Training,” Apr. 21, 2026.

\[Wan26u\] Y. Wang, T. Xie, K. Shen, M. Wang, and L. Yang, “RLAnything: Forge Environment, Policy, and Reward Model in Completely Dynamic RL System,” *ArXiv*, vol. abs/2602.02488, Feb. 2026, doi: [10.48550/arXiv.2602.02488](https://doi.org/10.48550/arXiv.2602.02488).

\[Xu26j\] T. Xu, Y.-T. Chen, and M. Li, “CLEANER: Self-Purified Trajectories Boost Agentic Reinforcement Learning,” *ArXiv*, vol. abs/2601.15141, Jan. 2026, doi: [10.48550/arXiv.2601.15141](https://doi.org/10.48550/arXiv.2601.15141).

\[Ge26\] R. Ge *et al.*, “Internalizing Agency from Reflective Experience,” Mar. 17, 2026.

\[Li26l\] Z. Li *et al.*, “No More Stale Feedback: Co-Evolving Critics for Open-World Agent Learning,” *ArXiv*, vol. abs/2601.06794, Jan. 2026, doi: [10.48550/arXiv.2601.06794](https://doi.org/10.48550/arXiv.2601.06794).

\[Wan26al\] H. Wang *et al.*, “Skill-SD: Skill-Conditioned Self-Distillation for Multi-turn LLM Agents,” Apr. 12, 2026.

\[Ye26f\] T. Ye, L. Dong, Q. Dong, X. Wu, S. Huang, and F. Wei, “Online Experiential Learning for Language Models,” Mar. 17, 2026.

\[Qi24\] Z. Qi *et al.*, “WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning,” *ArXiv*, vol. abs/2411.02337, Nov. 2024, doi: [10.48550/arXiv.2411.02337](https://doi.org/10.48550/arXiv.2411.02337).

\[Sin25b\] A. Singh *et al.*, “VARP: Reinforcement Learning from Vision-Language Model Feedback with Agent Regularized Preferences,” *ArXiv*, vol. abs/2503.13817, Mar. 2025, doi: [10.48550/arXiv.2503.13817](https://doi.org/10.48550/arXiv.2503.13817).

\[Xu25q\] H. Xu, Z. Yu, Y. Tang, P. Hu, Y. Tang, and H. Dong, “MCTS-EP: Empowering Embodied Planning with Online Preference Optimization,” *ArXiv*, vol. abs/2509.17116, Sep. 2025, doi: [10.48550/arXiv.2509.17116](https://doi.org/10.48550/arXiv.2509.17116).

\[Sar24b\] G. Sarch, L. Jang, M. J. Tarr, W. W. Cohen, K. Marino, and K. Fragkiadaki, “VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought,” *Advances in Neural Information Processing Systems 37*, Jun. 2024, doi: [10.52202/079017-2418](https://doi.org/10.52202/079017-2418).

\[Wu25b\] P. Wu, S. Ma, B. Wang, J. Yu, L. Lu, and Z. Liu, “GUI-Reflection: Empowering Multimodal GUI Models with Self-Reflection Behavior,” *ArXiv*, vol. abs/2506.08012, Jun. 2025, doi: [10.48550/arXiv.2506.08012](https://doi.org/10.48550/arXiv.2506.08012).

\[Fai26\] F. Faisal, Q. Wu, B. Peng, and J. Gao, “AutoSurfer -- Teaching Web Agents through Comprehensive Surfing, Learning, and Modeling,” Apr. 29, 2026.

\[Ala25\] M. Alakuijala *et al.*, “Memento No More: Coaching AI Agents to Master Multiple Tasks via Hints Internalization,” *ArXiv*, vol. abs/2502.01562, Feb. 2025, doi: [10.48550/arXiv.2502.01562](https://doi.org/10.48550/arXiv.2502.01562).
