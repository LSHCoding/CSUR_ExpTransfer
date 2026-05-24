# Evaluator research gaps and directions

# 评估器研究缺口与方向

##### [**Undermind**](https://undermind.ai)

##### [**Undermind**](https://undermind.ai) 资料源

---


## Table of Contents

- [Challenges](#challenges)
  - [Judging lags solving and acting](#judging-lags-solving-and-acting)
  - [Process targets are still under-specified](#process-targets-are-still-under-specified)
  - [Label acquisition is a bottleneck and a source of bias](#label-acquisition-is-a-bottleneck-and-a-source-of-bias)
  - [Evaluators generalize much worse than their framing suggests](#evaluators-generalize-much-worse-than-their-framing-suggests)
  - [Temporal and state grounding remain weak](#temporal-and-state-grounding-remain-weak)
  - [More evaluator compute can hurt, not help](#more-evaluator-compute-can-hurt-not-help)
  - [Critic and policy coadaptation is unstable](#critic-and-policy-coadaptation-is-unstable)
  - [Failure supervision is still narrow and template-bound](#failure-supervision-is-still-narrow-and-template-bound)
  - [Deployment costs remain high](#deployment-costs-remain-high)
  - [Evaluation still flatters current methods](#evaluation-still-flatters-current-methods)
- [Future directions](#future-directions)
  - [Judge-specific training objectives](#judge-specific-training-objectives)
  - [Richer process supervision](#richer-process-supervision)
  - [Environment-grounded validation and attribution](#environment-grounded-validation-and-attribution)
  - [Continually updated critics](#continually-updated-critics)
  - [Better failure-native datasets](#better-failure-native-datasets)
  - [Stronger temporal and multimodal state models](#stronger-temporal-and-multimodal-state-models)
  - [Efficient critic distillation](#efficient-critic-distillation)
  - [Harder and more honest benchmarks](#harder-and-more-honest-benchmarks)
  - [Cross-platform and cross-embodiment transfer studies](#cross-platform-and-cross-embodiment-transfer-studies)
- [References](#references)

## Challenges

## 挑战

| Challenge | What the literature actually shows | Core support |
|:---|:---|:---|
| Judging lags solving and acting | Models that can solve, act, or critique often still fail at evaluation itself | \[Sun25l\], \[Xu25i\], \[Che25h\], \[Xie25c\], \[Yan25u\] |
| Process targets are still under-specified | Binary correctness is too weak, but progress, promise, value, and critique signals each miss part of the problem | \[Set24\], \[Li24m\], \[Che25s\], \[Xi25b\], \[Xu25h\] |
| Label acquisition is a bottleneck and a source of bias | Human labels do not scale, while synthetic labels inherit teacher bias, shortcut noise, and data composition artifacts | \[Lig23\], \[Luo24\], \[Pal25\], \[Cha25b\], \[Lee26b\] |
| Evaluators generalize much worse than their framing suggests | Cross-domain, cross-platform, cross-embodiment, and sim-to-real transfer all show large drops | \[Ala24\], \[Du23\], \[Gri25\], \[Wu25m\], \[Che26s\] |
| Temporal and state grounding remain weak | Evaluators still miss subtle action effects, short-lived events, and long-horizon dependencies | \[Son26d\], \[Lee26b\], \[Sch26\], \[Zha26z\], \[Dua24\] |
| More evaluator compute can hurt, not help | Larger sample budgets, longer histories, or more reasoning can amplify verifier failures and false positives | \[Lig23\], \[Set24\], \[Xi25b\], \[Wan26s\], \[Wan26p\] |
| Critic and policy coadaptation is unstable | Frozen critics go stale, naive reward mixing collapses, and optimization often learns evaluator artifacts | \[Li26l\], \[Xu25h\], \[Wan26s\], \[Qi24\], \[Zha26ac\] |
| Failure supervision is still narrow and template-bound | Many systems detect only coarse failure types, or only those seen in synthetic taxonomies | \[Dua24\], \[Qi26\], \[Gri25\], \[Gu25b\], \[Zha26z\] |
| Deployment costs remain high | Real-time use is constrained by latency, token cost, tool calls, and annotation infrastructure | \[Wan24l\], \[Wu26e\], \[Sch26\], \[Dai25\], \[Zha26ac\] |
| Evaluation still flatters current methods | Pairwise accuracy, final success, and static offline tests hide the hardest failure modes | \[Zha26ab\], \[Che26s\], \[Wen25b\], \[Son26d\], \[Du23\] |

| 挑战 | 文献实际显示的现象 | 核心依据 |
|:---|:---|:---|
| 判断能力落后于求解和行动能力 | 能求解、行动或批评的模型，往往仍会在评估本身上失败 | \[Sun25l\], \[Xu25i\], \[Che25h\], \[Xie25c\], \[Yan25u\] |
| 过程目标仍未充分界定 | 二元正确性太弱，但进展、前景、价值和批评信号又各自遗漏问题的一部分 | \[Set24\], \[Li24m\], \[Che25s\], \[Xi25b\], \[Xu25h\] |
| 标签获取既是瓶颈，也是偏差来源 | 人类标签难以扩展，合成标签又继承教师偏差、捷径噪声和数据组成伪影 | \[Lig23\], \[Luo24\], \[Pal25\], \[Cha25b\], \[Lee26b\] |
| 评估器泛化远弱于其表述暗示 | 跨领域、跨平台、跨具身形态以及仿真到真实迁移都出现大幅下降 | \[Ala24\], \[Du23\], \[Gri25\], \[Wu25m\], \[Che26s\] |
| 时间和状态 grounding 仍然薄弱 | 评估器仍会漏掉细微动作效果、短暂事件和长时域依赖 | \[Son26d\], \[Lee26b\], \[Sch26\], \[Zha26z\], \[Dua24\] |
| 更多评估器计算可能有害，而非有益 | 更大的样本预算、更长历史或更多推理可能放大验证器失败和假阳性 | \[Lig23\], \[Set24\], \[Xi25b\], \[Wan26s\], \[Wan26p\] |
| 批评器与策略的共同适配不稳定 | 冻结批评器会过时，朴素奖励混合会崩塌，优化常学到评估器伪影 | \[Li26l\], \[Xu25h\], \[Wan26s\], \[Qi24\], \[Zha26ac\] |
| 失败监督仍狭窄且受模板绑定 | 许多系统只能检测粗粒度失败类型，或只能检测合成分类体系中出现过的类型 | \[Dua24\], \[Qi26\], \[Gri25\], \[Gu25b\], \[Zha26z\] |
| 部署成本仍然很高 | 实时使用受延迟、token 成本、工具调用和标注基础设施约束 | \[Wan24l\], \[Wu26e\], \[Sch26\], \[Dai25\], \[Zha26ac\] |
| 评估仍会美化现有方法 | 成对准确率、最终成功率和静态离线测试会隐藏最困难的失败模式 | \[Zha26ab\], \[Che26s\], \[Wen25b\], \[Son26d\], \[Du23\] |

### Judging lags solving and acting

### 判断能力落后于求解和行动能力

A recurring hidden result is that evaluation is not a free byproduct of general capability. \[Sun25l\] makes this explicit. Section 2.3 and Figure 1 show a large solve-to-judge gap, with models failing to correctly judge 14.9 to 35.2 percent of the problems they can themselves solve. Even when ground truth answers are given, judging accuracy plateaus near 95 percent rather than saturating, which means some error remains in the comparison process itself rather than in factual knowledge. Table 3 sharpens the point: optimizing only the solving reward degrades judge performance, so better solving does not mechanically turn into better judging. \[Xu25i\] reaches a similar conclusion from another angle. Section 5.2 and Table 2 show that standard SFT or DPO on teacher judgments can actually reduce judge quality, and Figure 3 shows that positional inconsistency rises sharply on harder reasoning tasks.

一个反复出现的隐性结果是，评估并不是通用能力的免费副产物。\[Sun25l\] 明确呈现了这一点。第 2.3 节和图 1 显示，求解到判断之间存在巨大差距：模型对自身能够求解的问题，有 14.9% 到 35.2% 不能正确判断。即便给出真实答案，判断准确率也停在约 95% 附近而非饱和，这意味着部分错误留在比较过程本身，而不是事实知识中。表 3 进一步强化这一点：只优化求解奖励会降低裁判器表现，因此更好的求解不会机械地转化为更好的判断。\[Xu25i\] 从另一角度得到类似结论。第 5.2 节和表 2 显示，在教师判断上做标准监督微调或直接偏好优化，实际上可能降低裁判器质量；图 3 显示，在更难推理任务上，位置不一致性会急剧上升。

Agent papers expose the same split between doing and judging. \[Che25h\] shows in Table 3 that a GPT-4o based labeler still lags human annotation enough to lower downstream agent performance. \[Xie25c\] finds that self-critique SFT raises regression risk, with Table 1 showing more cases where a correct program is turned into an incorrect one. \[Yan25u\] reports that weaker verifiers can be actively harmful, with Figure 4 showing that using a weak model as its own verifier often hurts rather than helps. The broader claim that evaluator ability is a distinct competence is an inference, but it is strongly supported by repeated mismatches between solving, acting, and judging across \[Sun25l\], \[Xu25i\], \[Che25h\], \[Xie25c\], and \[Yan25u\].

智能体论文暴露出行动与判断之间的相同分裂。\[Che25h\] 在表 3 中显示，基于 GPT-4o 的标注器仍落后于人类标注，差距足以降低下游智能体性能。\[Xie25c\] 发现自我批评监督微调会提高回归风险，表 1 显示更多正确程序被转成错误程序的案例。\[Yan25u\] 报告称，较弱验证器可能主动有害，图 4 显示使用弱模型作为自身验证器常常弊大于利。评估器能力是一种独立能力，这一较宽主张是一种推断，但 \[Sun25l\]、\[Xu25i\]、\[Che25h\]、\[Xie25c\] 和 \[Yan25u\] 中求解、行动与判断之间反复出现的错配为它提供了强支撑。

What matters for the field is that many current pipelines still treat evaluation as a thin wrapper on top of generation. The evidence says otherwise. Judge models need their own training signals, calibration procedures, and failure analysis. A paper that reports only actor gains without separately testing judge consistency, order sensitivity, regression rate, and self contradiction is likely hiding the core difficulty rather than resolving it.

对该领域而言，关键是许多当前流水线仍把评估当作生成之上的薄包装。证据并不支持这种看法。裁判器模型需要自己的训练信号、校准过程和失败分析。若一篇论文只报告行动器增益，却不单独测试裁判器一致性、顺序敏感性、回归率和自我矛盾，那么它很可能是在隐藏核心困难，而非解决核心困难。

### Process targets are still under-specified

### 过程目标仍未充分界定

The literature agrees that outcome supervision is too sparse, but it does not yet agree on what should replace it. \[Set24\] argues that absolute value targets create exploitable shortcuts. Appendix G shows a model learning to begin every solution by rephrasing the problem because this yields spurious reward. The same paper therefore shifts toward process advantage rather than raw value. \[Li24m\] argues that ordinary binary cross-entropy is structurally wrong for PRMs because it treats states independently and allows Q-values to decrease along correct trajectories. Table 3 and Section 4.3 show that even theoretically motivated ranking losses can fail once noisy negatives are introduced. \[Che25s\] then argues that backward correctness alone is incomplete and adds forward-looking value signals, because PRMs are strong late in a trajectory while value models are stronger early. Figure 1 is the clearest summary of that complementarity.

文献同意结果监督过于稀疏，但尚未就替代对象达成一致。\[Set24\] 认为绝对价值目标会制造可利用捷径。附录 G 显示，模型学会在每个解答开头重述问题，因为这会带来虚假奖励。因此，同一论文转向过程优势，而不是原始价值。\[Li24m\] 认为普通二元交叉熵对过程奖励模型在结构上是错误的，因为它独立处理状态，并允许 Q 值沿正确轨迹下降。表 3 和第 4.3 节显示，即使有理论动机的排序损失，在引入带噪负样本后也可能失败。\[Che25s\] 随后认为，仅有后向正确性是不完整的，并加入前向价值信号，因为过程奖励模型在轨迹后段更强，而价值模型在前段更强。图 1 最清楚地概括了这种互补性。

Agent papers make the target design problem sharper. \[Xi25b\] shows that promise without progress is not enough. Section 5.1 and Figure 4 show clear drops when the progress term is removed, even though promise looks like the natural target for a sparse-return task. \[Xu25h\] reaches a different but related conclusion in non-verifiable search tasks. Section 3.2 and Table 3 show that naively summing dense process rewards into sparse outcome rewards destabilizes training, while principled normalization is required to keep local fidelity from overriding end-task success. \[Zha25z\] adds a GUI-specific twist: the reward must separate key steps from hollow steps, yet Table 4 shows that making progress depend on longer windows hurts rather than helps. This is a strong sign that the right temporal abstraction depends on the action domain.

智能体论文使目标设计问题更尖锐。\[Xi25b\] 显示，只有前景而没有进展是不够的。第 5.1 节和图 4 显示，移除进展项会造成明显下降，尽管前景看起来像稀疏回报任务的自然目标。\[Xu25h\] 在不可验证搜索任务中得到不同但相关的结论。第 3.2 节和表 3 显示，朴素地把稠密过程奖励加到稀疏结果奖励中会使训练不稳定，而原则化归一化是必要的，用来防止局部保真度压过最终任务成功。\[Zha25z\] 加入了图形界面特定的变化：奖励必须区分关键步骤和空洞步骤，但表 4 显示，让进展依赖更长窗口反而有害。这是一个强信号：合适的时间抽象依赖动作领域。

There is real disagreement here. \[Set24\] and \[Che25s\] push toward richer forward-looking signals. \[Li24m\] insists on ranking structure. \[Xi25b\] argues for promise plus progress. \[Xu25h\] shows that even well-motivated dense signals can destabilize RL when the task is non-verifiable. The field therefore does not yet have a settled object of supervision. This survey section should treat that as a live research gap, not as a solved design choice.

这里存在真实分歧。\[Set24\] 和 \[Che25s\] 推向更丰富的前向信号。\[Li24m\] 坚持排序结构。\[Xi25b\] 主张前景加进展。\[Xu25h\] 显示，当任务不可验证时，即便动机良好的稠密信号也可能使强化学习不稳定。因此，该领域尚未拥有稳定的监督对象。综述这一节应把它视为仍在发生的研究缺口，而不是已解决的设计选择。

### Label acquisition is a bottleneck and a source of bias

### 标签获取既是瓶颈，也是偏差来源

The most important innovation surface in this area is often not model architecture but how labels are obtained. \[Lig23\] shows both the power and fragility of human process labels. Their PRM800K dataset is strong enough to beat outcome supervision, but Section 4.2 reports instability when retraining the active selector, and Appendix F notes sensitivity to optimization hyperparameters because the training setup is far from ordinary language modeling. \[Luo24\] replaces human labels with automated Monte Carlo estimates, but Section 5 and Appendix A make clear that this introduces both false negatives and false positives. Their solution is to filter out questions that are too easy or too hard, which is a scope retreat rather than a universal answer. \[Pal25\] shows that richer label taxonomies help, but Appendix B also shows negative scaling: more weakly generated data can make the model worse.

这一领域最重要的创新界面常常不是模型架构，而是标签如何获得。\[Lig23\] 同时显示了人类过程标签的力量与脆弱性。其 PRM800K 数据集足够强，能超过结果监督，但第 4.2 节报告，重训主动选择器时会出现不稳定，附录 F 指出，由于训练设置远离普通语言建模，它对优化超参数敏感。\[Luo24\] 用自动蒙特卡洛估计替代人类标签，但第 5 节和附录 A 明确显示，这会同时引入假阴性和假阳性。他们的解法是过滤掉太容易或太难的问题，这是范围收缩，而不是通用答案。\[Pal25\] 显示，更丰富的标签分类有帮助，但附录 B 也显示负向扩展：更多弱生成数据可能使模型变差。

Web and GUI work reveals the same tradeoff between scale and label quality. \[Cha25b\] builds a large checklist-based PRM dataset, yet Section 7.5 documents hallucinated checklists and Section B.4 says 15 percent of human annotations had to be discarded. \[Che25h\] still needs human labels for core correctness even after adding VLM assistance. \[Wu25m\] is especially revealing here. Table 3 shows that GPT-annotated negatives actually hurt training compared with the base model, which means natural-looking synthetic negatives are often not the same thing as useful supervision. In robotics, \[Lee26b\] shows that organic failures are not enough and that synthetic counterfactual augmentation is what really broadens generalization. That is one of the strongest recent arguments that failure data must be designed, not merely harvested.

网页与图形界面工作揭示了规模和标签质量之间的相同权衡。\[Cha25b\] 构建了一个大型清单式过程奖励模型数据集，但第 7.5 节记录了幻觉清单，第 B.4 节表示 15% 的人工标注必须被丢弃。\[Che25h\] 即便加入视觉语言模型辅助，核心正确性仍需要人工标签。\[Wu25m\] 在这里尤其有启发性。表 3 显示，相比基础模型，GPT 标注的负例实际上会伤害训练，这意味着看起来自然的合成负例常常并不等于有用监督。在机器人领域，\[Lee26b\] 显示自然产生的失败还不够，真正扩展泛化的是合成反事实增强。这是近期最有力的论据之一：失败数据必须被设计，而不能只是被采集。

This matters because many papers present synthetic labeling as a pure scalability win. The evidence is less comfortable. Label pipelines quietly encode strong assumptions about error taxonomy, teacher style, data balance, and what counts as progress. An inference supported across \[Lig23\], \[Luo24\], \[Pal25\], \[Cha25b\], \[Wu25m\], and \[Lee26b\] is that evaluator training is now data-engineering limited at least as much as it is model-limited.

这一点重要，因为许多论文把合成标注呈现为纯粹的扩展性收益。证据并不那么舒适。标签流水线隐性编码了关于错误分类、教师风格、数据平衡和何为进展的强假设。由 \[Lig23\]、\[Luo24\]、\[Pal25\]、\[Cha25b\]、\[Wu25m\] 和 \[Lee26b\] 共同支持的一个推断是：评估器训练如今至少同样受限于数据工程，而不只是受限于模型。

### Evaluators generalize much worse than their framing suggests

### 评估器泛化远弱于其表述暗示

Many papers use language like general purpose, transferable, or cross-platform, but the actual results are much narrower. \[Ala24\] shows genuine transfer, yet Table 1 still drops from 91 percent on in-domain hard tasks to 73 percent when training on out-of-domain data. \[Du23\] is harsher. Section 6 reports a 99 percent training balanced accuracy but only 62 percent on Ego4D test data, and Section 4.2 says zero-shot success detection in IA Playroom is near random. \[Gri25\] shows an even sharper sim-to-real break: Table II reports recall collapsing from about 0.94 in simulation to about 0.32 when a sim-trained detector is tested on real data.

许多论文使用“通用”“可迁移”或“跨平台”等表述，但实际结果窄得多。\[Ala24\] 显示了真实迁移，但表 1 仍显示，从领域内困难任务上的 91% 下降到使用领域外数据训练时的 73%。\[Du23\] 更严苛。第 6 节报告训练平衡准确率为 99%，但在 Ego4D 测试数据上只有 62%；第 4.2 节表示，IA Playroom 中的零样本成功检测接近随机。\[Gri25\] 显示了更尖锐的仿真到真实断裂：表 II 报告，当用仿真训练的检测器测试真实数据时，召回率从仿真中的约 0.94 崩到约 0.32。

Cross-platform GUI critics show the same pattern in a different modality. \[Wu25m\] is strong on mobile, but Table 1 shows a large remaining gap to proprietary systems on desktop. \[Wan25q\] likewise performs well on mobile GUI-I while trailing GPT-4o on GUI-W web critic accuracy in Table 1. \[Che26s\] reports 97.5 percent pairwise accuracy offline, yet only a modest 6.9 point online gain, and Section 4.3 attributes the difference to distribution shift from human training data to live agent outputs. In robotics, \[Lee26b\] shows strong average performance but large subset-level swings, and Section 5.1 makes clear that a single reward model is not uniformly best across embodiments.

跨平台图形界面批评器在另一模态中显示相同模式。\[Wu25m\] 在移动端很强，但表 1 显示它在桌面端与专有系统之间仍有很大差距。\[Wan25q\] 同样在移动端 GUI-I 上表现良好，但表 1 中的 GUI-W 网页批评准确率仍落后于 GPT-4o。\[Che26s\] 报告离线成对准确率为 97.5%，但在线增益只有温和的 6.9 个点，第 4.3 节将差异归因于从人类训练数据到实时智能体输出的分布偏移。在机器人领域，\[Lee26b\] 显示平均表现很强，但子集层面波动很大，第 5.1 节清楚表明，单一奖励模型并非在所有具身形态上都一致最优。

The broad implication is that evaluator portability remains more rhetorical than demonstrated. This is an inference, but it follows from repeated gaps between in-distribution offline metrics and out-of-distribution online use in \[Ala24\], \[Du23\], \[Gri25\], \[Wu25m\], \[Wan25q\], \[Che26s\], and \[Lee26b\]. Transfer needs to be measured across task families, embodiments, user interfaces, and agent action formats, not just across held-out prompts from the same dataset.

较宽的含义是，评估器可移植性仍更多停留在表述层面，而不是被充分证明。这是一个推断，但它来自 \[Ala24\]、\[Du23\]、\[Gri25\]、\[Wu25m\]、\[Wan25q\]、\[Che26s\] 和 \[Lee26b\] 中反复出现的领域内离线指标与领域外在线使用之间的差距。迁移需要跨任务族、具身形态、用户界面和智能体动作格式测量，而不能只跨同一数据集的留出提示测量。

### Temporal and state grounding remain weak

### 时间和状态 grounding 仍然薄弱

A large share of recent work is really about a grounding problem disguised as reward modeling. \[Son26d\] shows that full video context matters because sparse observations miss decisive temporal windows, yet even their best model reaches only 0.3332 temporal IoU in Figure 3. Appendix A adds that long Ubuntu trajectories with trial-and-error behavior are particularly hard because the evaluator confuses exploration with failure. \[Lee26b\] reports that reward models often interpolate a plausible manipulation narrative rather than tracking exact physical state, especially for fine-grained spatial distinctions. \[Sch26\] quantifies this from on-robot RL: Appendix C attributes 34 percent of SOLE-R1 failures to temporal under-detection of brief events such as clicks and latch releases.

近期工作中很大一部分其实是披着奖励建模外衣的 grounding 问题。\[Son26d\] 显示完整视频上下文很重要，因为稀疏观察会漏掉决定性时间窗口，但即便其最佳模型在图 3 中也只有 0.3332 的时间交并比。附录 A 补充说，带有试错行为的长 Ubuntu 轨迹尤其困难，因为评估器会把探索混同为失败。\[Lee26b\] 报告称，奖励模型常常插值出一个看似合理的操控叙事，而不是跟踪精确物理状态，尤其是在细粒度空间区分上。\[Sch26\] 从机上强化学习量化了这一点：附录 C 将 34% 的 SOLE-R1 失败归因于对点击、锁扣释放等短暂事件的时间欠检测。

GUI work surfaces the same issue in a different form. \[Zha26z\] relies on action-effect verification, but Section 6 admits the core assumption is failure idempotency, meaning failed actions usually leave the screen unchanged. That is useful, but it excludes many non-idempotent failures. \[Dua24\] shows why richer failure reasoning is attractive, yet Section 6 admits AHA remains closely aligned to the specific failure scenarios seen during fine-tuning. \[Gu25b\] shows that even strong latent failure detectors lose their clean failure zones in real-world settings, where Appendix C.1 says failed and successful rollouts are not easily separable.

图形界面工作以另一种形式呈现了同一问题。\[Zha26z\] 依赖动作效果验证，但第 6 节承认核心假设是失败幂等性，也就是失败动作通常会让屏幕保持不变。这很有用，但排除了许多非幂等失败。\[Dua24\] 显示了为何更丰富的失败推理有吸引力，但第 6 节承认 AHA 仍与微调时见过的特定失败场景密切对齐。\[Gu25b\] 显示，即便强隐空间失败检测器在真实世界设置中也会失去干净的失败区域，附录 C.1 表示失败与成功采样轨迹并不容易分离。

This matters because evaluator errors in these domains are not random. They are concentrated where action effects are small, delayed, partially occluded, or semantically subtle. Progress reward models, failure detectors, and video judges all become unreliable in the same places. That convergence across \[Son26d\], \[Lee26b\], \[Sch26\], \[Zha26z\], \[Dua24\], and \[Gu25b\] suggests that better temporal state abstractions may matter more than yet another scoring head.

这一点重要，因为这些领域中的评估器错误并非随机。它们集中在动作效果微小、延迟、部分遮挡或语义细微的位置。进展奖励模型、失败检测器和视频裁判器都会在相同位置变得不可靠。\[Son26d\]、\[Lee26b\]、\[Sch26\]、\[Zha26z\]、\[Dua24\] 和 \[Gu25b\] 的这种收敛提示，更好的时间状态抽象可能比再添加一个打分头更重要。

### More evaluator compute can hurt, not help

### 更多评估器计算可能有害，而非有益

A buried pattern across the literature is that more search, more context, or more reasoning often exposes evaluator weakness rather than compensating for it. \[Lig23\] already showed this in an early form: Appendix G reports that ORM performance can decrease on easier problems as sample count increases because search finds adversarial examples that fool the verifier. \[Set24\] finds a related failure at the policy level. Section 5 reports that ORM reranking can fall below the SFT policy at large sample counts because the verifier collapses candidate diversity. \[Xi25b\] reproduces the same effect in agentic settings, with Table 1 showing ORM performance in WebShop dropping from 19.5 to 8.0 as beam search scales from small to large.

文献中有一个被埋住的模式：更多搜索、更多上下文或更多推理常常暴露评估器弱点，而不是弥补它。\[Lig23\] 早已以早期形式显示这一点：附录 G 报告，随着样本数增加，结果奖励模型在较容易问题上的表现会下降，因为搜索会找到欺骗验证器的对抗样例。\[Set24\] 在策略层面发现相关失败。第 5 节报告，在大样本数下，结果奖励模型重排序会低于监督微调策略，因为验证器会压垮候选多样性。\[Xi25b\] 在智能体设置中复现了相同效应，表 1 显示，随着束搜索从小规模扩展到大规模，WebShop 中的结果奖励模型表现从 19.5 降到 8.0。

Longer context can be just as harmful. \[Wan26s\] shows that as reward model context grows, the agentic-Q model becomes unstable, and Figure 4 finds that window size 1 is best while larger windows sharply reduce entropy and performance. \[Wan26p\] adds an uncomfortable twist: reasoning-heavy critics are not automatically better. Table 5 shows the reasoning critic model underperforming the intuitive critic, and Table 1 shows even the intuitive critic degrading grounding on GUI-Odyssey. \[Yan25u\] and \[Xio25c\] suggest that extra critique or majority voting can help, but both also show ceilings and diminishing returns once the underlying judgment task becomes binary or answer leakage appears.

更长上下文同样可能有害。\[Wan26s\] 显示，随着奖励模型上下文增长，agentic-Q 模型会变得不稳定，图 4 发现窗口大小 1 最好，而更大窗口会显著降低熵和性能。\[Wan26p\] 加入了一个不舒服的转折：推理密集批评器并不自动更好。表 5 显示，推理批评模型弱于直觉批评器，表 1 显示，即便直觉批评器也会降低 GUI-Odyssey 上的 grounding。\[Yan25u\] 和 \[Xio25c\] 提示额外批评或多数投票可能有帮助，但二者也显示，一旦底层判断任务变成二元，或出现答案泄漏，就会出现上限和收益递减。

The field often treats evaluator quality as monotone in inference-time compute. The evidence does not support that. Better compute helps only if the judge remains calibrated under broader search and longer histories. Otherwise, extra compute just gives the system more chances to select false positives. That is a central challenge for any survey of evaluator-guided test-time scaling.

该领域常把评估器质量视为随推理时计算单调增加。证据并不支持这种看法。只有当裁判器在更宽搜索和更长历史下仍保持校准时，更多计算才有帮助。否则，额外计算只是给系统更多机会去选择假阳性。这是任何关于评估器引导测试时扩展综述的核心挑战。

### Critic and policy coadaptation is unstable

### 批评器与策略的共同适配不稳定

Once evaluators are put inside learning loops, a second class of problems appears. \[Li26l\] is the clearest statement of critic staleness. Section 5.2.2 and Table 2 show that freezing the critic can underperform even standard GRPO, because feedback that was useful early becomes noisy once the policy’s failure pattern changes. \[Qi24\] shows the same general issue in web RL. Appendix C finds that including failed trajectories slows and destabilizes learning, and Figure 12 shows domain-specific regressions even as average performance rises. \[Wan26s\] adds that standard GRPO style normalization interacts badly with continuous agentic-Q rewards, producing unstable advantages unless extra filtering is added.

一旦评估器被放入学习循环，第二类问题就会出现。\[Li26l\] 最清楚地表述了批评器过时问题。第 5.2.2 节和表 2 显示，冻结批评器甚至可能弱于标准 GRPO，因为早期有用的反馈会在策略失败模式变化后变得有噪。\[Qi24\] 在网页强化学习中显示了相同的一般问题。附录 C 发现，纳入失败轨迹会减慢并扰乱学习，图 12 显示，即使平均性能上升，也会出现领域特定退化。\[Wan26s\] 补充说，标准 GRPO 式归一化与连续 agentic-Q 奖励之间相互作用很差，若不加入额外过滤，会产生不稳定优势。

Reward composition is another instability source. \[Xu25h\] shows that raw or reduced reward mixtures collapse on non-verifiable agentic tasks, while hybrid normalization is required to keep process and outcome signals aligned. \[Zha26ac\] reveals a different risk: as verifiers become agentic and tool-using, they inherit tool failures, quota limits, and additional error channels. Table 8 reports nontrivial Python error and quota-exceeded rates even when the final verdict is correct. \[Xie25c\] shows that PPO value networks for critique quality are unstable enough to be abandoned in favor of GRPO, and their Section D explains why holistic critique quality resists clean credit assignment.

奖励组合是另一种不稳定来源。\[Xu25h\] 显示，原始或简化的奖励混合在不可验证智能体任务上会崩塌，而混合归一化是保持过程信号与结果信号对齐所必需的。\[Zha26ac\] 揭示了另一种风险：当验证器变得智能体化并使用工具时，它们会继承工具失败、配额限制和额外错误通道。表 8 报告，即便最终裁决正确，也存在不可忽略的 Python 错误和配额超限率。\[Xie25c\] 显示，用于批评质量的 PPO 价值网络不稳定到被放弃，改用 GRPO，其附录 D 解释了为何整体批评质量难以进行干净信用分配。

The broader inference is that evaluator training and policy training cannot be cleanly separated. Policies change the distribution of mistakes. Critics trained on older failures go stale. More elaborate verifiers create more moving parts. This is not just an engineering nuisance. It means the field still lacks a stable theory of how evaluators should evolve alongside the agents they supervise.

更宽的推断是，评估器训练和策略训练无法干净分离。策略会改变错误分布。基于旧失败训练的批评器会过时。更复杂的验证器会制造更多活动部件。这不只是工程麻烦。它意味着该领域仍缺少稳定理论，用来说明评估器应如何与其监督的智能体共同演化。

### Failure supervision is still narrow and template-bound

### 失败监督仍狭窄且受模板绑定

Many recent systems claim to reason about failures, but the failure object itself is often narrowly defined. \[Dua24\] builds a useful seven-way failure taxonomy and shows strong downstream gains, yet Section 6 states that AHA’s reasoning remains closely aligned to its fine-tuning failure scenarios. \[Qi26\] moves beyond single-pass failure detection, but Table 1 shows severe collapse for naive multitask SFT under distribution shift, and Appendix C.2 documents refinement drift where the model converges on plausible but wrong explanations. \[Gri25\] broadens failure detection to semantic misalignment and control errors, though Section VI-B notes that their zero-shot transfer is still dominated by control-heavy AHA style failures.

许多近期系统声称能对失败进行推理，但失败对象本身常被窄化定义。\[Dua24\] 构建了有用的七类失败分类体系，并显示强下游增益，但第 6 节表示，AHA 的推理仍与其微调失败场景密切对齐。\[Qi26\] 超越了单遍失败检测，但表 1 显示，朴素多任务监督微调在分布偏移下严重崩塌，附录 C.2 记录了精炼漂移：模型会收敛到看似合理但错误的解释。\[Gri25\] 将失败检测扩展到语义错配和控制错误，不过第 VI-B 节指出，其零样本迁移仍由控制密集的 AHA 式失败主导。

Other papers show that failure categories are still too coarse for what agents need. \[Gu25b\] discovers meaningful latent failure zones in simulation, but Appendix C.1 shows these zones blur in real-world robotics where failures lack a unified semantic meaning. \[Zha26z\] makes a productive simplifying assumption by focusing on unchanged screens after bad actions, but Section 6 acknowledges that richer failure taxonomies are needed for non-idempotent errors. \[Dih26\] is perhaps the most sobering case. Their code-agent PRM assigns dense intermediate rewards, yet Table 2 shows almost no separation between resolved and unresolved tasks, implying that the current failure and progress signals are not semantically tied enough to repository-level success.

其他论文显示，对智能体需求而言，失败类别仍过于粗糙。\[Gu25b\] 在仿真中发现有意义的隐空间失败区域，但附录 C.1 显示，在失败缺少统一语义含义的真实世界机器人场景中，这些区域会变得模糊。\[Zha26z\] 通过聚焦坏动作后不变的屏幕，作出了有生产力的简化假设，但第 6 节承认，非幂等错误需要更丰富的失败分类体系。\[Dih26\] 也许是最令人警醒的案例。其代码智能体过程奖励模型分配稠密中间奖励，但表 2 显示，已解决任务与未解决任务之间几乎没有分离，暗示当前失败和进展信号与仓库级成功之间的语义绑定不够。

This matters because first-generation failure supervision mostly answers whether something went wrong, not what kind of reusable lesson the failure contains. A mature evaluator should distinguish wrong intent, wrong action, wrong grounding, wrong recovery, and wrong verification. Most current systems still collapse several of these into one label or one free-form explanation.

这一点重要，因为第一代失败监督主要回答是否出了错，而不是失败包含何种可复用经验。成熟评估器应区分错误意图、错误动作、错误 grounding、错误恢复和错误验证。多数当前系统仍将其中若干项压缩成一个标签或一段自由形式解释。

### Deployment costs remain high

### 部署成本仍然很高

Even when evaluator ideas work, using them in realistic loops is expensive. \[Wan24l\] had to query proprietary VLMs under tight budgets, and Appendix B.3 shows that Fold Cloth used drastically fewer queries due to GPT-4V quota limits. \[Wu26e\] narrows online reward generation to an interval-hold strategy because per-step large reward model inference is too slow for control. \[Sch26\] makes the same compromise in real robot RL, using interpolation between reward queries because even a one second per frame reward model is too slow for true dense evaluation. \[Zha26ac\] quantifies the cost of agentic verification directly, with Table 5 showing roughly triple the token and time cost relative to a base verifier.

即便评估器想法有效，在现实循环中使用它们也很昂贵。\[Wan24l\] 必须在紧张预算下查询专有视觉语言模型，附录 B.3 显示，由于 GPT-4V 配额限制，Fold Cloth 使用的查询数大幅减少。\[Wu26e\] 将在线奖励生成收窄为区间保持策略，因为逐步大型奖励模型推理对控制来说太慢。\[Sch26\] 在真实机器人强化学习中作出相同折中，使用奖励查询之间的插值，因为即便每帧一秒的奖励模型也太慢，无法做真正稠密评估。\[Zha26ac\] 直接量化智能体式验证成本，表 5 显示，相比基础验证器，其 token 和时间成本约为三倍。

GUI systems hit a different infrastructure wall. \[Dai25\] had to redesign the interaction setup to make verifier-driven training feasible in containerized environments, and Table 4 shows that better memory construction greatly improves performance but adds a step-time bottleneck of its own. \[Che25h\] reports the hidden cost of human annotation, while \[Cha25b\] shows that using GPT-4o style evaluators inside tree search is economically unrealistic at scale. The conclusion is not just that evaluation is expensive. It is that many current papers succeed only after substantial engineering simplifications, such as lower query frequency, smaller action spaces, static offline data, or narrower domains.

图形界面系统遇到另一种基础设施墙。\[Dai25\] 必须重新设计交互设置，才能让验证器驱动训练在容器化环境中可行；表 4 显示，更好的记忆构建大幅提升性能，但也带来自己的单步时间瓶颈。\[Che25h\] 报告了人工标注的隐藏成本，\[Cha25b\] 则显示，在树搜索中使用 GPT-4o 式评估器，在规模上不具备经济现实性。结论不只是评估昂贵，而是许多当前论文只有在做出大量工程简化后才成功，例如降低查询频率、缩小动作空间、使用静态离线数据或收窄领域。

For a CSUR discussion, this is important because the practical bottleneck is no longer merely whether an evaluator can be trained. It is whether it can run often enough, cheaply enough, and robustly enough to matter in online agent learning.

对 CSUR 讨论而言，这一点重要，因为实践瓶颈已不只是评估器能否被训练出来。关键还在于它能否以足够高的频率、足够低的成本和足够强的鲁棒性运行，使其在在线智能体学习中真正产生作用。

### Evaluation still flatters current methods

### 评估仍会美化现有方法

A final cross-cutting gap is that many metrics make evaluator progress look cleaner than it is. \[Zha26ab\] shows that pairwise accuracy compresses model differences and hides failure on hard distractor sets, while BoN accuracy reveals much larger gaps. \[Che26s\] similarly reports very high offline pairwise accuracy but only modest online gains, making the offline metric an incomplete proxy for action selection value. \[Wen25b\] introduces EA-F1 because raw detection performance ignores the latency constraint that matters in deployment. \[Son26d\] adds temporal IoU precisely because outcome accuracy alone does not reveal whether a video reward model can localize failure. \[Zha26z\] introduces loop rate and recovery success rate because task success alone misses robustness to repeated local failure.

最后一个横向缺口是，许多指标会让评估器进展看起来比实际更干净。\[Zha26ab\] 显示，成对准确率会压缩模型差异，并隐藏在困难干扰集上的失败，而最佳样本准确率揭示出大得多的差距。\[Che26s\] 同样报告很高的离线成对准确率，但在线增益仅为温和水平，使离线指标成为动作选择价值的不完整代理。\[Wen25b\] 引入 EA-F1，因为原始检测性能忽略了部署中重要的延迟约束。\[Son26d\] 加入时间交并比，正是因为单靠结果准确率无法揭示视频奖励模型能否定位失败。\[Zha26z\] 引入循环率和恢复成功率，因为任务成功率本身会漏掉对重复局部失败的鲁棒性。

Older work already hinted at the same problem. \[Du23\] notes that human agreement itself caps success detector accuracy in some settings, which means standard classification metrics partly measure label ambiguity rather than objective task truth. \[Lig23\] shows that reward model evaluation without policy optimization can understate later reward hacking risk. \[Wan26p\] uses Pass at N to expose a large gap between the existence of a correct candidate and the critic’s ability to pick it.

较早工作已经暗示了同一问题。\[Du23\] 指出，在某些设置中，人类一致性本身会限制成功检测器准确率，这意味着标准分类指标部分测量的是标签含混性，而非客观任务真值。\[Lig23\] 显示，不结合策略优化的奖励模型评估会低估后续奖励黑客风险。\[Wan26p\] 使用 Pass at N 暴露出正确候选存在与批评器选出它之间的巨大差距。

The field therefore needs evaluator-specific benchmarks, not just better agent benchmarks. This is an inference, but it is hard to avoid after reading \[Zha26ab\], \[Che26s\], \[Wen25b\], \[Son26d\], \[Zha26z\], \[Du23\], and \[Wan26p\]. The key open problem is not only to build better evaluators, but to measure what better really means.

因此，该领域需要评估器特定基准，而不只是更好的智能体基准。这是一个推断，但在阅读 \[Zha26ab\]、\[Che26s\]、\[Wen25b\]、\[Son26d\]、\[Zha26z\]、\[Du23\] 和 \[Wan26p\] 后很难回避。关键开放问题不只是构建更好的评估器，还要测量“更好”究竟意味着什么。

## Future directions

## 未来方向

| Direction | What concrete progress would look like | Core support |
|:---|:---|:---|
| Judge-specific training objectives | Training recipes that explicitly target consistency, regression avoidance, and comparison fidelity rather than hoping these emerge from solving | \[Sun25l\], \[Xu25i\], \[Xie25c\], \[Yan25u\] |
| Richer process supervision | Signals that combine correctness, progress, promise, intent, and action effects in a calibrated way | \[Che25s\], \[Xi25b\], \[Che26s\], \[Zha26z\], \[Set24\] |
| Environment-grounded validation and attribution | Evaluators that justify scores with verifiable state changes and can localize which feedback item changed behavior | \[Zha26z\], \[Son26d\], \[Li26l\], \[Dih26\], \[Zha26ac\] |
| Continually updated critics | Critics that evolve with the policy and adapt to changing failure distributions | \[Li26l\], \[Wan26p\], \[Qi26\], \[Qi24\] |
| Better failure-native datasets | Counterfactual, hard-negative, and recovery-labeled data rather than success-heavy corpora | \[Lee26b\], \[Dua24\], \[Gri25\], \[Gu25b\], \[Pal25\] |
| Stronger temporal and multimodal state models | Video, action-effect, and multi-sensor evaluators that preserve subtle changes rather than flattening them away | \[Son26d\], \[Sch26\], \[Qi26\], \[Ma23d\], \[Lee26b\] |
| Efficient critic distillation | Turning costly judges into lightweight deployable critics without losing grounding and calibration | \[Wu26e\], \[Sch26\], \[Dai25\], \[Wan26p\], \[Zha26ac\] |
| Harder and more honest benchmarks | Metrics that expose selection failure, stale feedback, recovery, timing, and transfer under shift | \[Zha26ab\], \[Wen25b\], \[Zha26z\], \[Son26d\], \[Che26s\] |
| Cross-platform and cross-embodiment transfer studies | Evaluators tested on genuinely different interfaces, action spaces, and embodiments rather than nearby splits | \[Wu25m\], \[Che26s\], \[Lee26b\], \[Gri25\], \[Ala24\] |

| 方向 | 具体进展形态 | 核心依据 |
|:---|:---|:---|
| 面向裁判器的训练目标 | 显式针对一致性、避免回归和比较保真度的训练方案，而不是期待它们从求解中自然涌现 | \[Sun25l\], \[Xu25i\], \[Xie25c\], \[Yan25u\] |
| 更丰富的过程监督 | 以校准方式结合正确性、进展、前景、意图和动作效果的信号 | \[Che25s\], \[Xi25b\], \[Che26s\], \[Zha26z\], \[Set24\] |
| 有环境根基的验证与归因 | 评估器用可验证状态变化支撑分数，并能定位哪个反馈项改变了行为 | \[Zha26z\], \[Son26d\], \[Li26l\], \[Dih26\], \[Zha26ac\] |
| 持续更新的批评器 | 批评器随策略演化，并适应变化中的失败分布 | \[Li26l\], \[Wan26p\], \[Qi26\], \[Qi24\] |
| 更好的失败原生数据集 | 反事实、困难负例和带恢复标签的数据，而不是偏向成功样本的语料 | \[Lee26b\], \[Dua24\], \[Gri25\], \[Gu25b\], \[Pal25\] |
| 更强的时间与多模态状态模型 | 保留细微变化的视频、动作效果和多传感器评估器，而不是把它们压平 | \[Son26d\], \[Sch26\], \[Qi26\], \[Ma23d\], \[Lee26b\] |
| 高效批评器蒸馏 | 在不丢失 grounding 与校准的情况下，把昂贵裁判器转化为轻量可部署批评器 | \[Wu26e\], \[Sch26\], \[Dai25\], \[Wan26p\], \[Zha26ac\] |
| 更难且更诚实的基准 | 暴露选择失败、陈旧反馈、恢复、时序和分布偏移下迁移的指标 | \[Zha26ab\], \[Wen25b\], \[Zha26z\], \[Son26d\], \[Che26s\] |
| 跨平台与跨具身形态迁移研究 | 在真正不同的界面、动作空间和具身形态上测试评估器，而非只在邻近划分上测试 | \[Wu25m\], \[Che26s\], \[Lee26b\], \[Gri25\], \[Ala24\] |

### Judge-specific training objectives

### 面向裁判器的训练目标

One clear direction is to stop treating evaluation as a side effect of reasoning or instruction following. \[Sun25l\] shows that solving-aware objectives help only when explicitly tied to judgment rewards, and Table 3 shows solving-only supervision is counterproductive. \[Xu25i\] goes further by designing equivalent-initial-state GRPO specifically for judge consistency, because plain RL, SFT, and DPO do not remove positional bias. \[Xie25c\] shows that critique training must explicitly penalize regression, not just reward actionability, and \[Yan25u\] shows that deliberate multi-stage critique generation improves evaluation more than direct one-pass verification.

一个清晰方向是停止把评估当作推理或指令遵循的副作用。\[Sun25l\] 显示，求解感知目标只有在明确绑定到判断奖励时才有帮助，表 3 显示仅求解监督会适得其反。\[Xu25i\] 更进一步，专门为裁判器一致性设计等价初始状态的 GRPO，因为普通强化学习、监督微调和直接偏好优化不能消除位置偏差。\[Xie25c\] 显示，批评训练必须显式惩罚回归，而不只是奖励可操作性；\[Yan25u\] 显示，刻意的多阶段批评生成比直接单遍验证更能改善评估。

Concrete progress would look like judge training regimes that report, and directly optimize for, four things at once:

具体进展可以表现为裁判器训练机制同时报告并直接优化四件事：

- Verdict accuracy
  裁决准确率
- Consistency under order and format changes
  顺序和格式变化下的一致性
- Low regression on already correct solutions
  对已有正确解的低回归率
- Calibration under increased test-time search
  测试时搜索增加下的校准性

A strong paper in this direction would treat evaluator training as its own optimization problem rather than as a byproduct of actor tuning. It should also compare specialized judge objectives against generic reasoning fine-tuning on the same backbone.

这个方向上的强论文会把评估器训练视为自身的优化问题，而不是行动器调参的副产物。它还应在同一主干上比较专门裁判器目标与通用推理微调。

### Richer process supervision

### 更丰富的过程监督

The field is moving away from single scalar correctness toward richer process signals, but the pieces remain disconnected. \[Che25s\] shows why bidirectional signals help. \[Xi25b\] shows that promise plus progress is stronger than either alone in agentic settings. \[Che26s\] adds intent conditioning because action correctness is often ambiguous without a local plan. \[Zha26z\] adds predicted action effects because post-action verification is too late in irreversible interfaces. \[Set24\] suggests that advantage-style targets are often better than raw values when the goal is to encourage useful next actions rather than states that merely look promising.

该领域正在从单一标量正确性转向更丰富的过程信号，但各个部件仍未连接。\[Che25s\] 显示双向信号为何有帮助。\[Xi25b\] 显示，在智能体设置中，前景加进展强于任一单独信号。\[Che26s\] 加入意图条件化，因为缺少局部计划时，动作正确性常常含混。\[Zha26z\] 加入预测动作效果，因为在不可逆界面中，动作后验证太晚。\[Set24\] 提示，当目标是鼓励有用下一步动作，而不是鼓励看似有前景的状态时，优势式目标常优于原始价值。

Concrete progress would mean evaluators whose outputs have structure rather than one number. A useful agent-side evaluator might jointly predict:

具体进展意味着评估器输出具有结构，而不是只有一个数字。一个有用的智能体侧评估器可以联合预测：

- Whether the last step was valid
  上一步是否有效
- Whether the state improved toward the task
  状态是否朝任务方向改善
- Whether the current branch remains promising
  当前分支是否仍有前景
- What action effect should be visible next
  接下来应可见的动作效果是什么
- What intent or subgoal the action is serving
  该动作服务于什么意图或子目标

The key verification test would be whether each component adds unique downstream value. Ablations should not stop at final success rate. They should test selection quality, recovery after local errors, false positive rate under search, and robustness when multiple valid action sequences exist.

关键验证测试应检查每个组件是否增加独特下游价值。消融不应停在最终成功率，而应测试选择质量、局部错误后的恢复、搜索下假阳性率，以及存在多条有效动作序列时的鲁棒性。

### Environment-grounded validation and attribution

### 有环境根基的验证与归因

A large gap in current work is that evaluators often say something useful-looking without proving that the score corresponds to the environment. \[Zha26z\] points toward a better pattern by tying evaluation to observable action effects. \[Son26d\] shows that temporal attribution is valuable in its own right because it reveals where a trajectory began to fail. \[Li26l\] argues that critic feedback must remain actionable as policy failures evolve. \[Dih26\] shows how weak intermediate rewards can be when they are only loosely connected to final success. \[Zha26ac\] adds that tool-augmented verification introduces its own hidden failure modes, so external grounding needs to be measured, not assumed.

当前工作的一个大缺口是，评估器常说出看似有用的话，却没有证明分数与环境对应。\[Zha26z\] 通过把评估绑定到可观察动作效果，指向更好的模式。\[Son26d\] 显示，时间归因本身有价值，因为它揭示轨迹从哪里开始失败。\[Li26l\] 认为，随着策略失败演化，批评器反馈必须保持可操作。\[Dih26\] 显示，当中间奖励只与最终成功松散连接时，它们会有多弱。\[Zha26ac\] 补充说，工具增强验证会引入自己的隐藏失败模式，因此外部 grounding 需要被测量，而不是被假定。

Concrete progress would look like evaluators that return both a verdict and a grounded evidence trail. Depending on the domain, that might be:

具体进展可以表现为评估器同时返回裁决和有根基的证据轨迹。根据领域不同，这可能是：

- The frame interval where the task diverged
  任务发生偏离的帧区间
- The missing state transition after an action
  动作之后缺失的状态转移
- The tool check that failed
  失败的工具检查
- The exact intermediate step whose reward contribution later predicted success
  其奖励贡献后来预测成功的精确中间步骤

This direction matters not just for interpretability but for lifecycle management. Without attribution, stale or harmful evaluator behavior is hard to diagnose, prune, or retrain.

这个方向不仅关系到可解释性，也关系到生命周期管理。没有归因，陈旧或有害的评估器行为很难被诊断、剪枝或重训。

### Continually updated critics

### 持续更新的批评器

Static critics are poorly matched to non-stationary agent learning. \[Li26l\] provides the clearest evidence that co-evolution matters, with frozen critics becoming worse than no critic at all. \[Wan26p\] shows a similar flywheel idea in GUI critics, where one round of training still leaves systematic blind spots and another round improves coverage. \[Qi26\] suggests refinement-aware training is necessary if a critic is expected to improve its own reasoning at inference time. \[Qi24\] shows that online web agents shift domain difficulty over time, which is exactly the setting in which frozen evaluators will go stale.

静态批评器与非平稳智能体学习并不匹配。\[Li26l\] 提供了共同演化重要性的最清晰证据，其中冻结批评器变得比完全没有批评器更差。\[Wan26p\] 在图形界面批评器中显示了类似飞轮想法：一轮训练仍留下系统性盲点，而另一轮训练改善覆盖。\[Qi26\] 提示，如果期待批评器在推理时改善自身推理，则需要精炼感知训练。\[Qi24\] 显示，在线网页智能体会随时间改变领域难度，而这正是冻结评估器会过时的设置。

Concrete progress would mean treating critic refresh as part of the method rather than as an occasional retraining event. A robust pipeline would specify:

具体进展意味着把批评器刷新视为方法的一部分，而不是偶发重训事件。鲁棒流水线应说明：

- How new failure modes are detected
  如何检测新失败模式
- How critic data is refreshed without self-confirming bias
  如何在没有自我确认偏差的情况下刷新批评器数据
- How evaluator drift is measured
  如何测量评估器漂移
- When a policy update should trigger a critic update
  何时策略更新应触发批评器更新

A strong evaluation here would use time-indexed metrics. Instead of one aggregate score, it would show whether critic usefulness decays, stabilizes, or improves as the policy distribution changes.

这里的强评估应使用时间索引指标。它不会只给出一个聚合分数，而会显示随着策略分布变化，批评器效用是衰减、稳定还是改善。

### Better failure-native datasets

### 更好的失败原生数据集

Current datasets are still too success-heavy or too template-bound to support robust evaluators. \[Lee26b\] shows that synthetic counterfactual augmentation is more valuable than relying on organic failures. \[Dua24\] shows the usefulness of explicit failure taxonomies, but also why narrow taxonomies are only a start. \[Gri25\] and \[Gu25b\] reveal that failure representations learned in controlled settings do not naturally carry into real-world clutter and task diversity. \[Pal25\] shows that richer error typing materially improves PRM performance, which is a sign that label semantics matter.

当前数据集仍过于偏向成功样本，或过于受模板绑定，难以支持鲁棒评估器。\[Lee26b\] 显示，合成反事实增强比依赖自然失败更有价值。\[Dua24\] 显示了显式失败分类体系的用处，也显示狭窄分类体系只是起点。\[Gri25\] 和 \[Gu25b\] 揭示，在受控设置中学到的失败表示不会自然迁移到真实世界杂乱环境和任务多样性中。\[Pal25\] 显示，更丰富的错误类型会实质改善过程奖励模型表现，这说明标签语义很重要。

Concrete progress would look like datasets that preserve failure structure rather than only binary outcomes. High-value annotations would include:

具体进展可以表现为数据集保留失败结构，而不只是二元结果。高价值标注会包括：

- Failure cause
  失败原因
- Earliest divergence point
  最早偏离点
- Whether recovery remained possible
  是否仍可恢复
- Whether the failure was semantic, perceptual, motor, or planning related
  失败是语义、感知、运动还是规划相关
- Counterfactual near-miss variants
  反事实近失误变体

This direction is especially important because evaluator weaknesses concentrate on hard negatives and near-success failures. A benchmark built mostly from obvious failures will not stress the systems that now dominate leaderboards.

这个方向尤其重要，因为评估器弱点集中在困难负例和接近成功的失败上。主要由明显失败构成的基准无法对当前占据排行榜前列的系统形成压力。

### Stronger temporal and multimodal state models

### 更强的时间与多模态状态模型

Several papers imply that reward modeling quality is now limited by state representation rather than by ranking loss. \[Son26d\] shows that dense video context and temporal pruning are both necessary because important cues are localized in time and space. \[Sch26\] shows that even strong reward models miss brief contact events or occluded state changes. \[Qi26\] argues that vision-only failure reasoning misses some important failure modes and points toward force and proprioception as future inputs. \[Ma23d\] exposes the language grounding gap in robot reward models, and \[Lee26b\] shows that coarse progress labels still do not guarantee fine-grained spatial tracking.

多篇论文暗示，奖励建模质量如今受限于状态表示，而不是排序损失。\[Son26d\] 显示，稠密视频上下文和时间剪枝都是必要的，因为重要线索局限在时间和空间中。\[Sch26\] 显示，即便强奖励模型也会漏掉短暂接触事件或被遮挡的状态变化。\[Qi26\] 认为，仅视觉的失败推理会遗漏一些重要失败模式，并指向力和本体感知作为未来输入。\[Ma23d\] 暴露出机器人奖励模型中的语言 grounding 缺口，\[Lee26b\] 显示，粗粒度进展标签仍不能保证细粒度空间跟踪。

Concrete progress would look like evaluators that preserve action-critical state rather than compressing it too early into generic language or a single scalar. In practice that means more models that work over:

具体进展可以表现为评估器保留动作关键状态，而不是过早把它压缩成通用语言或单个标量。实践中，这意味着更多模型工作在：

- Short video clips rather than start and end frames only
  短视频片段，而不只是起始帧和结束帧
- Predicted action effects tied to future observations
  与未来观察绑定的预测动作效果
- Multi-view or multi-sensor traces when vision alone is ambiguous
  当单靠视觉存在歧义时，使用多视角或多传感器轨迹
- Long-horizon state summaries that retain causal transitions rather than only task semantics
  保留因果转移的长时域状态摘要，而不只是任务语义

The right verification would be whether these richer states improve not only accuracy, but also temporal localization, recovery quality, and resistance to reward hacking.

合适验证应检查这些更丰富状态是否不仅提高准确率，也提高时间定位、恢复质量和抗奖励黑客能力。

### Efficient critic distillation

### 高效批评器蒸馏

Many of the strongest evaluators are too expensive for direct deployment. \[Wu26e\] reduces online robotic reward costs with interval-hold querying, but that is still a workaround for inference latency. \[Sch26\] relies on interpolation between expensive reward calls. \[Dai25\] shows that practical deployment lives or dies on engineering details such as memory construction cost. \[Wan26p\] argues that intuitive critics can outperform more expensive reasoning-heavy ones in some GUI settings. \[Zha26ac\] makes the token and time overhead of agentic verification impossible to ignore.

许多最强评估器过于昂贵，无法直接部署。\[Wu26e\] 通过区间保持查询降低在线机器人奖励成本，但这仍只是推理延迟的变通方案。\[Sch26\] 依赖昂贵奖励调用之间的插值。\[Dai25\] 显示，实践部署成败取决于记忆构建成本等工程细节。\[Wan26p\] 认为，在某些图形界面设置中，直觉批评器可以超过更昂贵的推理密集批评器。\[Zha26ac\] 使智能体式验证的 token 和时间开销变得无法忽视。

Concrete progress would mean a two-stage evaluator pipeline that separates teacher quality from student efficiency. A costly teacher could use tools, long reasoning, or multi-view context offline. A distilled student could then provide fast online judgments. The right benchmarks would report not only accuracy, but also:

具体进展意味着两阶段评估器流水线，将教师质量与学生效率分离。昂贵教师可以离线使用工具、长推理或多视角上下文。蒸馏学生随后提供快速在线判断。合适基准不只报告准确率，也报告：

- Wall-clock latency
  墙钟延迟
- Token cost per step
  每步 token 成本
- How much of the teacher’s ranking quality survives distillation
  教师排序质量有多少在蒸馏后保留下来
- Whether the student preserves calibration under search and domain shift
  学生是否在搜索和领域偏移下保持校准

This would turn efficiency from an afterthought into a first-class evaluation target.

这会把效率从事后考虑变成一等评估目标。

### Harder and more honest benchmarks

### 更难且更诚实的基准

The literature is beginning to invent the right metrics, but they are still fragmented. \[Zha26ab\] shows that BoN accuracy is often more revealing than pairwise accuracy. \[Wen25b\] argues that evaluator quality should be adjusted for runtime cost. \[Zha26z\] adds loop rate and recovery success rate to expose robustness. \[Son26d\] uses temporal IoU to test failure localization. \[Che26s\] shows that offline pairwise accuracy can badly overstate online value.

文献正在开始发明合适指标，但这些指标仍然碎片化。\[Zha26ab\] 显示，最佳样本准确率常比成对准确率更有揭示力。\[Wen25b\] 认为，评估器质量应按运行时成本调整。\[Zha26z\] 加入循环率和恢复成功率来暴露鲁棒性。\[Son26d\] 使用时间交并比测试失败定位。\[Che26s\] 显示，离线成对准确率可能严重高估在线价值。

Concrete progress would be benchmark suites that combine these ideas. A serious evaluator benchmark should test:

具体进展将是结合这些想法的基准套件。严肃的评估器基准应测试：

- Candidate ranking under many hard negatives
  多个困难负例下的候选排序
- Transfer to live agents rather than only offline replay
  迁移到实时智能体，而不只是离线回放
- Recovery after local failure
  局部失败后的恢复
- Stability under increased search budget
  搜索预算增加下的稳定性
- Performance under stale feedback and policy drift
  陈旧反馈和策略漂移下的性能
- Runtime and memory cost
  运行时和记忆成本

This direction is less glamorous than new model design, but it is essential. Without it, the field will keep mistaking cleaner offline metrics for genuinely better evaluators.

这个方向不如新模型设计醒目，但它是必要的。没有它，该领域会持续把更干净的离线指标误认为真正更好的评估器。

### Cross-platform and cross-embodiment transfer studies

### 跨平台与跨具身形态迁移研究

The promise of evaluator portability remains only partly tested. \[Wu25m\] is one of the few papers to study mobile, web, and desktop together, and its results show that parity across them is still far away. \[Che26s\] exposes a large offline to online gap when the acting agent’s output format changes. \[Lee26b\] shows that even strong general-purpose reward models have embodiment-specific blind spots. \[Gri25\] reveals how fast simulated failure cues collapse in the real world. \[Ala24\] shows transfer is possible, but only with a clear performance penalty.

评估器可移植性的承诺仍只被部分测试。\[Wu25m\] 是少数同时研究移动端、网页和桌面端的论文之一，其结果显示三者之间距离持平仍很远。\[Che26s\] 暴露出当行动智能体输出格式变化时，离线到在线之间存在巨大缺口。\[Lee26b\] 显示，即便强通用奖励模型也有具身形态特定盲点。\[Gri25\] 揭示仿真失败线索在真实世界中崩塌得多快。\[Ala24\] 显示迁移是可能的，但会带来明确性能代价。

Concrete progress would mean experiments where the same evaluator is moved across genuinely different consumers and environments. For example:

具体进展意味着实验将同一评估器迁移到真正不同的消费者和环境中。例如：

- Mobile critic to desktop critic
  从移动端批评器到桌面端批评器
- Sim-trained robot failure detector to real robot deployment
  从仿真训练的机器人失败检测器到真实机器人部署
- Human-trajectory evaluator to agent-generated trajectory evaluator
  从人类轨迹评估器到智能体生成轨迹评估器
- Web reward model across consumer websites and enterprise workflows
  跨消费者网站和企业工作流的网页奖励模型

The point is not to show zero loss. It is to measure what aspects of evaluator behavior remain stable, what breaks, and what adaptation layers are needed. That would turn portability from an aspiration into a measurable property.

重点不是展示零损失，而是测量评估器行为的哪些方面保持稳定、哪些方面会破裂，以及需要哪些适配层。这样会把可移植性从愿景转化为可测属性。

---

## References

\[Sun25l\] S. Sun, J. Yu, Z. Wang, X. Yang, T. Gu, and Y. Yang, “S2J: Bridging the Gap Between Solving and Judging Ability in Generative Reward Models,” *ArXiv*, vol. abs/2509.22099, Sep. 2025, doi: [10.48550/arXiv.2509.22099](https://doi.org/10.48550/arXiv.2509.22099).

\[Xu25i\] A. Xu, Y. Zhou, X.-P. Nguyen, C. Xiong, and S. Joty, “J4R: Learning to Judge with Equivalent Initial State Group Relative Policy Optimization,” *ArXiv*, vol. abs/2505.13346, May 2025, doi: [10.48550/arXiv.2505.13346](https://doi.org/10.48550/arXiv.2505.13346).

\[Che25h\] C. Chen *et al.*, “GUI-Shepherd: Reliable Process Reward and Verification for Long-Sequence GUI Tasks,” *ArXiv*, vol. abs/2509.23738, Sep. 2025, doi: [10.48550/arXiv.2509.23738](https://doi.org/10.48550/arXiv.2509.23738).

\[Xie25c\] Z. Xie, J. Chen, L. Chen, W. Mao, J. Xu, and L. Kong, “Teaching Language Models to Critique via Reinforcement Learning,” *ArXiv*, vol. abs/2502.03492, Feb. 2025, doi: [10.48550/arXiv.2502.03492](https://doi.org/10.48550/arXiv.2502.03492).

\[Yan25u\] W. Yang, J. Chen, Y. Lin, and J. Wen, “DeepCritic: Deliberate Critique with Large Language Models,” *ArXiv*, vol. abs/2505.00662, May 2025, doi: [10.48550/arXiv.2505.00662](https://doi.org/10.48550/arXiv.2505.00662).

\[Set24\] A. R. Setlur *et al.*, “Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning,” *ArXiv*, vol. abs/2410.08146, Oct. 2024, doi: [10.48550/arXiv.2410.08146](https://doi.org/10.48550/arXiv.2410.08146).

\[Li24m\] W. Li and Y. Li, “Process Reward Model with Q-Value Rankings,” *ArXiv*, vol. abs/2410.11287, Oct. 2024, doi: [10.48550/arXiv.2410.11287](https://doi.org/10.48550/arXiv.2410.11287).

\[Che25s\] W. Chen *et al.*, “Better Process Supervision with Bi-directional Rewarding Signals,” *ArXiv*, vol. abs/2503.04618, Mar. 2025, doi: [10.48550/arXiv.2503.04618](https://doi.org/10.48550/arXiv.2503.04618).

\[Xi25b\] Z. Xi *et al.*, *AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress*. 2025. doi: [10.1145/3774904.3792551](https://doi.org/10.1145/3774904.3792551).

\[Xu25h\] P. Xu, Z. Li, X. Xing, G. Zhang, D. Li, and K. Shi, “Hybrid Reward Normalization for Process-supervised Non-verifiable Agentic Tasks,” *ArXiv*, vol. abs/2509.25598, Sep. 2025, doi: [10.48550/arXiv.2509.25598](https://doi.org/10.48550/arXiv.2509.25598).

\[Lig23\] H. Lightman *et al.*, “Let’s Verify Step by Step,” *ArXiv*, vol. abs/2305.20050, May 2023, doi: [10.48550/arXiv.2305.20050](https://doi.org/10.48550/arXiv.2305.20050).

\[Luo24\] L. Luo *et al.*, “Improve Mathematical Reasoning in Language Models by Automated Process Supervision,” *ArXiv*, vol. abs/2406.06592, Jun. 2024.

\[Pal25\] T. D. Pala, P. Sharma, A. Zadeh, C. Li, and S. Poria, “Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision,” *ArXiv*, vol. abs/2505.19706, May 2025, doi: [10.48550/arXiv.2505.19706](https://doi.org/10.48550/arXiv.2505.19706).

\[Cha25b\] H. Chae *et al.*, “Web-Shepherd: Advancing PRMs for Reinforcing Web Agents,” *ArXiv*, vol. abs/2505.15277, May 2025, doi: [10.48550/arXiv.2505.15277](https://doi.org/10.48550/arXiv.2505.15277).

\[Lee26b\] T. Lee, A. Wagenmaker, K. Pertsch, P. Liang, S. Levine, and C. Finn, “RoboReward: General-Purpose Vision-Language Reward Models for Robotics,” *ArXiv*, vol. abs/2601.00675, Jan. 2026, doi: [10.48550/arXiv.2601.00675](https://doi.org/10.48550/arXiv.2601.00675).

\[Ala24\] M. Alakuijala *et al.*, “Video-Language Critic: Transferable Reward Functions for Language-Conditioned Robotics,” *ArXiv*, vol. abs/2405.19988, May 2024, doi: [10.48550/arXiv.2405.19988](https://doi.org/10.48550/arXiv.2405.19988).

\[Du23\] Y. Du *et al.*, “Vision-Language Models as Success Detectors,” *ArXiv*, vol. abs/2303.07280, Mar. 2023, doi: [10.48550/arXiv.2303.07280](https://doi.org/10.48550/arXiv.2303.07280).

\[Gri25\] C. Grislain, H. Rahimi, O. Sigaud, and M. Chetouani, “I-FailSense: Towards General Robotic Failure Detection with Vision-Language Models,” *ArXiv*, vol. abs/2509.16072, Sep. 2025, doi: [10.48550/arXiv.2509.16072](https://doi.org/10.48550/arXiv.2509.16072).

\[Wu25m\] Z. Wu *et al.*, “OS-Oracle: A Comprehensive Framework for Cross-Platform GUI Critic Models,” *ArXiv*, vol. abs/2512.16295, Dec. 2025, doi: [10.48550/arXiv.2512.16295](https://doi.org/10.48550/arXiv.2512.16295).

\[Che26s\] R. Chen, Y. Li, Z. Fang, S. Tang, W. Cao, and T. Lan, “IntentScore: Intent-Conditioned Action Evaluation for Computer-Use Agents,” Apr. 06, 2026.

\[Son26d\] L. Song *et al.*, “Video-Based Reward Modeling for Computer-Use Agents,” Mar. 10, 2026.

\[Sch26\] P. Schroeder, T. Weng, K. Schmeckpeper, E. Rosen, S. Hart, and O. Biza, “SOLE-R1: Video-Language Reasoning as the Sole Reward for On-Robot Reinforcement Learning,” Mar. 30, 2026.

\[Zha26z\] Y. Zhang *et al.*, “Don’t Act Blindly: Robust GUI Automation via Action-Effect Verification and Self-Correction,” Apr. 07, 2026.

\[Dua24\] J. Duan *et al.*, “AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation,” *ArXiv*, vol. abs/2410.00371, Oct. 2024, doi: [10.48550/arXiv.2410.00371](https://doi.org/10.48550/arXiv.2410.00371).

\[Wan26s\] Y. Wang *et al.*, “Building Autonomous GUI Navigation via Agentic-Q Estimation and Step-Wise Policy Optimization,” *ArXiv*, vol. abs/2602.13653, Feb. 2026, doi: [10.48550/arXiv.2602.13653](https://doi.org/10.48550/arXiv.2602.13653).

\[Wan26p\] S. Wang *et al.*, “GAIA: A Data Flywheel System for Training GUI Test-Time Scaling Critic Models,” *ArXiv*, vol. abs/2601.18197, Jan. 2026, doi: [10.48550/arXiv.2601.18197](https://doi.org/10.48550/arXiv.2601.18197).

\[Li26l\] Z. Li *et al.*, “No More Stale Feedback: Co-Evolving Critics for Open-World Agent Learning,” *ArXiv*, vol. abs/2601.06794, Jan. 2026, doi: [10.48550/arXiv.2601.06794](https://doi.org/10.48550/arXiv.2601.06794).

\[Qi24\] Z. Qi *et al.*, “WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning,” *ArXiv*, vol. abs/2411.02337, Nov. 2024, doi: [10.48550/arXiv.2411.02337](https://doi.org/10.48550/arXiv.2411.02337).

\[Zha26ac\] J. Zhang *et al.*, “AgentV-RL: Scaling Reward Modeling with Agentic Verifier,” Apr. 17, 2026.

\[Qi26\] C. Qi *et al.*, “Self-Refining Vision Language Model for Robotic Failure Detection and Reasoning,” *ArXiv*, vol. abs/2602.12405, Feb. 2026, doi: [10.48550/arXiv.2602.12405](https://doi.org/10.48550/arXiv.2602.12405).

\[Gu25b\] Q. Gu *et al.*, “SAFE: Multitask Failure Detection for Vision-Language-Action Models,” *ArXiv*, vol. abs/2506.09937, Jun. 2025, doi: [10.48550/arXiv.2506.09937](https://doi.org/10.48550/arXiv.2506.09937).

\[Wan24l\] Y. Wang *et al.*, “RL-VLM-F: Reinforcement Learning from Vision Language Foundation Model Feedback,” *International Conference on Machine Learning*, pp. 51484–51501, Feb. 2024, doi: [10.48550/arXiv.2402.03681](https://doi.org/10.48550/arXiv.2402.03681).

\[Wu26e\] Y. Wu, W. Yuan, A. Qi, V. Guizilini, J. Mao, and Y. Wang, “Large Reward Models: Generalizable Online Robot Reward Generation with Vision-Language Models,” Mar. 17, 2026.

\[Dai25\] G. Dai *et al.*, “Advancing Mobile GUI Agents: A Verifier-Driven Approach to Practical Deployment,” *ArXiv*, vol. abs/2503.15937, Mar. 2025, doi: [10.48550/arXiv.2503.15937](https://doi.org/10.48550/arXiv.2503.15937).

\[Zha26ab\] Y. Zhang, S. Tang, Z. Li, Z. Han, and V. Tresp, “WebArbiter: A Principle-Guided Reasoning Process Reward Model for Web Agents,” *ArXiv*, vol. abs/2601.21872, Jan. 2026, doi: [10.48550/arXiv.2601.21872](https://doi.org/10.48550/arXiv.2601.21872).

\[Wen25b\] X. Wen, W. Mo, Y. Xie, P. Qi, and M. Chen, “Towards Policy-Compliant Agents: Learning Efficient Guardrails For Policy Violation Detection,” *ArXiv*, vol. abs/2510.03485, Oct. 2025, doi: [10.48550/arXiv.2510.03485](https://doi.org/10.48550/arXiv.2510.03485).

\[Zha25z\] D. Zhang *et al.*, “ProgRM: Build Better GUI Agents with Progress Rewards,” *ArXiv*, vol. abs/2505.18121, May 2025, doi: [10.48550/arXiv.2505.18121](https://doi.org/10.48550/arXiv.2505.18121).

\[Wan25q\] Y. Wanyan *et al.*, “Look Before You Leap: A GUI-Critic-R1 Model for Pre-Operative Error Diagnosis in GUI Automation,” *ArXiv*, vol. abs/2506.04614, Jun. 2025, doi: [10.48550/arXiv.2506.04614](https://doi.org/10.48550/arXiv.2506.04614).

\[Xio25c\] W. Xiong *et al.*, “StepWiser: Stepwise Generative Judges for Wiser Reasoning,” *ArXiv*, vol. abs/2508.19229, Aug. 2025, doi: [10.48550/arXiv.2508.19229](https://doi.org/10.48550/arXiv.2508.19229).

\[Dih26\] M. L. Dihan and Md. A. R. Khan, “SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents,” Apr. 12, 2026.

\[Ma23d\] Y. Ma *et al.*, “LIV: Language-Image Representations and Rewards for Robotic Control,” *International Conference on Machine Learning*, pp. 23301–23320, Jun. 2023, doi: [10.48550/arXiv.2306.00958](https://doi.org/10.48550/arXiv.2306.00958).
