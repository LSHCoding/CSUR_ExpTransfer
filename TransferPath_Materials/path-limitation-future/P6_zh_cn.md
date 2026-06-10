# Evaluator gaps for CSUR

# 综述 评估器缺口


##### [**Undermind**](https://undermind.ai)

##### [**Undermind**](https://undermind.ai) 来源


---


## Table of Contents

- [Challenges](#challenges)
  - [Evaluators improve more slowly than the policies they supervise](#evaluators-improve-more-slowly-than-the-policies-they-supervise)
  - [Process supervision is useful but fragile](#process-supervision-is-useful-but-fragile)
  - [Failure attribution is still weak in long horizon settings](#failure-attribution-is-still-weak-in-long-horizon-settings)
  - [Reward hacking remains structural rather than incidental](#reward-hacking-remains-structural-rather-than-incidental)
  - [Judge quality does not transfer cleanly across models, domains, or tasks](#judge-quality-does-not-transfer-cleanly-across-models-domains-or-tasks)
  - [Evaluation practice still hides major weaknesses](#evaluation-practice-still-hides-major-weaknesses)
  - [Data creation and systems cost are now first order bottlenecks](#data-creation-and-systems-cost-are-now-first-order-bottlenecks)
- [Future directions](#future-directions)
  - [Co evolving and routed evaluators should become the default rather than the exception](#co-evolving-and-routed-evaluators-should-become-the-default-rather-than-the-exception)
  - [Grounded hybrid process rewards are a more promising direction than either pure scalar reward or free form judging](#grounded-hybrid-process-rewards-are-a-more-promising-direction-than-either-pure-scalar-reward-or-free-form-judging)
  - [Failure native supervision should replace success only filtering](#failure-native-supervision-should-replace-success-only-filtering)
  - [Anti hacking evaluator stacks need to be treated as core method design, not as cleanup](#anti-hacking-evaluator-stacks-need-to-be-treated-as-core-method-design-not-as-cleanup)
  - [Transfer aware judge design should become a required evaluation axis](#transfer-aware-judge-design-should-become-a-required-evaluation-axis)
  - [Rubrics, critiques, and explanations should be preserved as reusable supervision artifacts](#rubrics-critiques-and-explanations-should-be-preserved-as-reusable-supervision-artifacts)
  - [Harder benchmark and audit protocols are needed if evaluator papers are to claim generality](#harder-benchmark-and-audit-protocols-are-needed-if-evaluator-papers-are-to-claim-generality)
- [References](#references)

## Challenges

## 挑战


| Challenge | Core evidence | Why current work still falls short |
|:---|:---|:---|
| Evaluators improve more slowly than the policies they supervise | Static reward models go stale, self judges saturate, and live judges still drift or collapse \[Lee23b, Guo24, Wu24d, Ren26b, Li26l\] | The field still has no robust recipe for keeping evaluator quality aligned with the policy distribution over long training runs |
| Process supervision is useful but fragile | Dense and stepwise rewards help, but only with careful normalization, decomposition, and judge design \[Cha24b, Xu25h, Che25v, Wan26ac, Wan26s, Li26p, Zha26am\] | Fine grained feedback is now clearly valuable, yet current methods remain narrow, unstable, and domain specific |
| Failure attribution is still weak in long horizon settings | Many methods can say a trajectory failed but cannot localize why, especially in search, GUI, and multi turn collaboration \[Zho25p, Luo25f, Wan26ac, Wan26s, Li26p, Wan26ad\] | Without reliable failure localization, dense supervision often becomes noisy reward shaping rather than real diagnosis |
| Reward hacking remains structural rather than incidental | Hacking appears in RM based RL, self judging loops, process rewards, and judge mixtures \[Bai22b, Don23, Gui24, Wu24d, Ack26, Ren26b, Din25b, Xu24d\] | Mitigations exist, but most are local defenses rather than field wide solutions |
| Judge quality does not transfer cleanly across models, domains, or tasks | Larger general judges can underperform smaller specialists, and weak to strong supervision often breaks \[Guo24, Wu24d, Xu25h, Zha26am, Fu25d\] | The literature often frames evaluator quality as a scaling problem, but much of it is an interface and specialization problem |
| Evaluation practice still hides major weaknesses | Simulated users, strict retrieval constraints, filtered datasets, and task specific scaffolds make results cleaner than deployment \[Pan24b, Zho24e, Zho25p, Wan26ac, Fu25d, Li26p\] | Many reported gains are conditional on evaluation choices that remove the hardest failure modes |
| Data creation and systems cost are now first order bottlenecks | High quality supervision usually requires aggressive filtering, long pipelines, or expensive judge calls \[Gon24b, Fu25d, Wan26ad, Li26p, Ack26\] | The field often presents better objectives as the main story, but pipeline economics now shape what can even be studied |

| 挑战 | 核心证据 | 当前工作仍然不足之处 |
|:---|:---|:---|
| 评估器进步慢于其监督的策略 | 静态奖励模型会过时，自评裁判器会饱和，在线裁判器仍会漂移或崩溃 \[Lee23b, Guo24, Wu24d, Ren26b, Li26l\] | 该领域仍缺少一种稳健方案，能在长训练过程中让评估器质量持续对齐策略分布 |
| 过程监督有用但脆弱 | 稠密奖励和逐步奖励有帮助，但依赖谨慎的归一化、分解和裁判器设计 \[Cha24b, Xu25h, Che25v, Wan26ac, Wan26s, Li26p, Zha26am\] | 细粒度反馈的价值已经很明确，但现有方法仍然狭窄、不稳定且依赖具体领域 |
| 长时程设置中的失败归因仍然薄弱 | 许多方法能判断一条轨迹失败，却无法定位失败原因，尤其是在搜索、图形界面 和多轮协作中 \[Zho25p, Luo25f, Wan26ac, Wan26s, Li26p, Wan26ad\] | 缺少可靠的失败定位时，稠密监督常常变成带噪的奖励塑形，而非真正诊断 |
| 奖励黑客仍是结构性问题 | 黑客行为出现在基于奖励模型的 强化学习、自评循环、过程奖励和裁判器混合中 \[Bai22b, Don23, Gui24, Wu24d, Ack26, Ren26b, Din25b, Xu24d\] | 已有缓解方法，但多数是局部防御，尚未形成全领域方案 |
| 裁判器质量难以在模型、领域或任务之间干净迁移 | 更大的通用裁判器可能弱于更小的专用裁判器，弱到强监督也经常失效 \[Guo24, Wu24d, Xu25h, Zha26am, Fu25d\] | 文献常把评估器质量表述为规模问题，但很大一部分其实是接口和专门化问题 |
| 评估实践仍遮蔽主要弱点 | 模拟用户、严格检索约束、过滤后的数据集和任务特定脚手架，使结果比部署场景更干净 \[Pan24b, Zho24e, Zho25p, Wan26ac, Fu25d, Li26p\] | 许多报告的收益依赖评估选择，而这些选择移除了最困难的失败模式 |
| 数据创建和系统成本已经成为一阶瓶颈 | 高质量监督通常需要激进过滤、长流水线或昂贵裁判器调用 \[Gon24b, Fu25d, Wan26ad, Li26p, Ack26\] | 该领域常把更好的目标函数当作主线，但流水线经济性已经决定了哪些问题能被研究 |

### Evaluators improve more slowly than the policies they supervise

### 评估器进步慢于其监督的策略


- **Supported by** \[Lee23b, Guo24, Yua24, Wu24d, Ren26b, Li26l, Wu25x\]
  **支持文献** \[Lee23b, Guo24, Yua24, Wu24d, Ren26b, Li26l, Wu25x\]

A repeated pattern is that evaluator quality lags behind actor improvement. \[Lee23b\] identifies reward model staleness directly and proposes direct RLAIF as a workaround, because a frozen reward model is asked to judge responses that drift away from its training distribution. \[Guo24\] makes the same point more sharply. Figure 3 shows offline DPO overfitting to static preferences, and Section 4.4 argues that online AI feedback is needed precisely because the response distribution moves during alignment. \[Li26l\] then shows the open world version of the same problem. In ALFWorld and SciWorld, a frozen critic does not just stop helping. It can underperform standard GRPO once failure patterns shift.

一个反复出现的模式是，评估器质量落后于行动者改进。\[Lee23b\] 直接指出奖励模型陈旧化，并提出直接 基于人工智能反馈的强化学习 作为变通方案，因为冻结的奖励模型被要求评判已经偏离其训练分布的回答。\[Guo24\] 更尖锐地表达了同一点。图 3 显示离线 直接偏好优化 会过拟合静态偏好，第 4.4 节认为在线 人工智能 反馈之所以必要，正是因为对齐过程中回答分布会移动。\[Li26l\] 随后展示了同一问题的开放世界版本。在 ALFWorld 和 SciWorld 中，冻结批评器不只是停止提供帮助；一旦失败模式转移，它甚至可能弱于标准 组相对策略优化。

The self improving judge papers do not solve this cleanly. \[Yua24\] is optimistic that the model can improve as both actor and judge, but the gains depend on a narrow seed distribution and only three single turn iterations. \[Wu24d\] explicitly reports that correlation with human judgments rises and then falls, that non self generated responses see limited improvement, and that Iteration 3 is hindered by score saturation and positional bias. \[Ren26b\] adds a useful disagreement. Live self evaluation turns out to differ little from frozen self evaluation in some settings, yet both still suffer late stage collapse. That is an important warning sign. A moving evaluator is not enough if the update rule preserves the same blind spots.

自我改进裁判器论文并没有干净地解决这一点。\[Yua24\] 乐观地认为模型可以同时作为行动者和裁判器改进，但收益依赖狭窄的种子分布，并且只经历三轮单轮迭代。\[Wu24d\] 明确报告，与人类判断的相关性先升后降，非自生成回答的改进有限，第 3 轮还受到分数饱和和位置偏置阻碍。\[Ren26b\] 给出了有用的不同意见。在若干设置中，在线自评与冻结自评差异很小，但二者仍然遭遇后期崩溃。这是一个重要警讯。如果更新规则保留同样的盲点，让评估器移动并不足够。

\[Wu25x\] suggests a partial answer through routing. No single reward model dominates all categories, and the online Bayesian layer is valuable because the policy induced data distribution keeps changing. But the gap to the oracle router remains large, which means even adaptive evaluator selection is still brittle under shift.

\[Wu25x\] 通过路由给出部分答案。没有单一奖励模型能支配所有类别，在线贝叶斯层有价值，因为策略诱导的数据分布持续变化。但它与 理想 路由器之间的差距仍然很大，意味着即便是自适应评估器选择，在分布转移下也仍然脆弱。

Inference. The literature has moved past the question of whether static evaluators are enough. They are not. The unresolved question is how to keep evaluators trustworthy when both the task distribution and the policy induced failure distribution move at the same time.

推断。文献已经越过“静态评估器是否足够”的问题。答案是否定的。未解决的问题是，当任务分布和策略诱导的失败分布同时移动时，如何保持评估器可信。

### Process supervision is useful but fragile

### 过程监督有用但脆弱


- **Supported by** \[Cha24b, Xu25h, Din25b, Che25v, Wan26ac, Wan26s, Li26p, Zha26am, Zho24e\]
  **支持文献** \[Cha24b, Xu25h, Din25b, Che25v, Wan26ac, Wan26s, Li26p, Zha26am, Zho24e\]

These papers collectively support denser feedback, but they also show how easy it is to get it wrong. \[Cha24b\] argues that token level credit can be extracted from the reward model attention map almost for free, yet the method needs a shared tokenizer, a transformer reward model, and a same sign assumption for all highlighted tokens. The proof only covers the shaping regime, while their own beta sweep often works best outside that guarantee. \[Xu25h\] shows an even harsher result. Process rewards without principled design and ReNorm can underperform outcome only training. Their stability depends on sign consistency and on anchoring the process reward to an exact match outcome signal.

这些论文共同支持更稠密的反馈，但也显示它很容易出错。\[Cha24b\] 认为 词元 级信用可以几乎免费地从奖励模型注意力图中提取，但该方法需要共享分词器、变换器 奖励模型，以及所有高亮 词元 同号的假设。证明只覆盖塑形情形，而他们自己的 参数 扫描经常在该保证之外表现最好。\[Xu25h\] 展示了更严苛的结果。没有原则性设计和 重新归一化 的过程奖励可能弱于仅使用结果的训练。其稳定性依赖符号一致性，并依赖将过程奖励锚定到精确匹配的结果信号。

The reasoning papers reveal a similar tension. \[Din25b\] shows that outcome rewards reinforce flawed positive trajectories and that a generative reward model can reduce this, but the obvious step ratio alternative causes jump in reasoning reward hacking. \[Che25v\] helps GRPO by rating the first error location, yet the paper admits the method still degenerates when all trajectories fail at the same first error and sometimes matches or underperforms GRPO on tasks with short or low structure negative samples. \[Zha26am\] finds that process supervision beats outcome only supervision for search reasoning, but the step ratings need five run majority voting, heavy data balancing, and a silver filtering threshold because raw labels are too noisy.

推理论文揭示了类似张力。\[Din25b\] 显示，结果奖励会强化有缺陷的正轨迹，生成式奖励模型可以缓解这一点，但看似直接的步骤比例替代方案会引发推理奖励黑客的跃升。\[Che25v\] 通过评定第一个错误位置来帮助 组相对策略优化，但论文承认，当所有轨迹都在同一个首错位置失败时，该方法仍会退化，并且在短或低结构负样本任务上有时持平或弱于 组相对策略优化。\[Zha26am\] 发现，过程监督在搜索推理中优于仅使用结果的监督，但步骤评分需要五次运行多数投票、重度数据平衡和银标过滤阈值，因为原始标签噪声太大。

The agent papers bring out the domain dependence. \[Wan26ac\] works only when contribution is sharply concentrated on a few search rounds. Low sharpness can hurt performance. \[Wan26s\] finds that a longer interaction window degrades success and destabilizes entropy, so even a learned Q style step reward becomes harder to use when context grows. \[Li26p\] gets strong precision from milestone wise critic decomposition, but Appendix B.2 shows a recall drop on single action trajectories because the method expects multi step evidence chains. \[Zho24e\] and \[Zho25p\] both show that process signals can outperform final answer only signals, but only when the verbalized or collaborative state carries enough structure for the evaluator to grade the process at all.

智能体论文凸显领域依赖。\[Wan26ac\] 只有当贡献高度集中在少数搜索轮次时才有效；低尖锐度会损害性能。\[Wan26s\] 发现更长的交互窗口会降低成功率并扰乱熵，因此当上下文增长时，即便学习到的 Q 式步骤奖励也更难使用。\[Li26p\] 通过里程碑式批评器分解获得高精度，但附录 B.2 显示，该方法期待多步证据链，因此在单动作轨迹上召回率下降。\[Zho24e\] 和 \[Zho25p\] 都显示，过程信号可以优于仅最终答案信号，但前提是语言化或协作状态携带足够结构，使评估器能够评定过程。

The disagreement across papers matters. Some works present dense process rewards as the cure for sparse outcome signals. Others show that naive dense signals destabilize training, miscalibrate scales, or collapse into style and length preferences. The field therefore still lacks a stable recipe for deciding which intermediate feedback is genuinely causal and which is merely easier to score.

论文之间的分歧很关键。有些工作把稠密过程奖励呈现为稀疏结果信号的解药。另一些工作显示，朴素稠密信号会扰乱训练、误校准尺度，或坍缩为风格和长度偏好。因此，该领域仍缺少稳定方案来判断哪些中间反馈真正具有因果性，哪些只是更容易打分。

### Failure attribution is still weak in long horizon settings

### 长时程设置中的失败归因仍然薄弱


- **Supported by** \[Luo25f, Zho25p, Wan26ac, Wan26s, Li26p, Wan26ad, Yua25c, Fu25d\]
  **支持文献** \[Luo25f, Zho25p, Wan26ac, Wan26s, Li26p, Wan26ad, Yua25c, Fu25d\]

Several papers can detect that a trajectory is bad, but not where or why it became bad. \[Luo25f\] is unusually transparent. The judge signal is strongest at separating zero like failures from ground truth, yet the error analysis still finds invalid coordination and spatial grounding problems that the preference labels do not resolve. Performance falls at 50 steps, which implies that step pair supervision did not solve compounding error. \[Zho25p\] faces the same issue in collaborative reasoning. SWEET RL needs asymmetrically informed critics because binary end rewards are too sparse, but even then the model collapses to shorter outputs without length normalization and needs enough data before the critic becomes reliable.

若干论文能检测一条轨迹不好，却不能指出它在何处或为何变坏。\[Luo25f\] 异常透明。裁判器信号最擅长把零分式失败与真实标注区分开，但误差分析仍发现偏好标签无法解决的无效协调和空间 grounding 问题。性能在 50 步时下降，暗示步骤对监督没有解决累积错误。\[Zho25p\] 在协作推理中面对同样问题。SWEET 强化学习 需要信息不对称的批评器，因为二元终局奖励过于稀疏；即便如此，若没有长度归一化，模型仍会坍缩为更短输出，并且需要足够数据之后批评器才可靠。

In search and GUI work the attribution gap is even clearer. \[Wan26ac\] can reallocate reward across successful rounds, but for failed trajectories it gives every round the same contribution because reliable failure attribution is too hard. Appendix A lists redundant queries, cascading reasoning errors, and retriever failures as confounded patterns. \[Wan26s\] addresses credit assignment through Agentic Q estimation, yet it still has to filter samples by action diversity and return variance to avoid unstable updates. \[Li26p\] solves part of the problem by decomposing trajectories into milestones, but the ablations show that without the Selector Agent evidence gets diluted by many minor wins and critical failures are masked.

在搜索和 图形界面 工作中，归因缺口更清楚。\[Wan26ac\] 可以在成功轮次之间重新分配奖励，但对失败轨迹，它会给每一轮相同贡献，因为可靠失败归因太难。附录 A 列出冗余查询、级联推理错误和检索器失败等相互混杂的模式。\[Wan26s\] 通过 智能体价值 估计处理信用分配，但仍必须按动作多样性和回报方差过滤样本，以避免不稳定更新。\[Li26p\] 通过把轨迹分解为里程碑解决部分问题，但消融显示，如果没有 选择器智能体，证据会被许多小胜利稀释，关键失败也会被遮蔽。

The verbal feedback papers show a nearby limit. \[Wan26ad\] only trains on main line turns and leaves side turns without training signal. \[Yua25c\] identifies revision points using ten manual revision thoughts and thresholded reward gaps. \[Fu25d\] accepts a refinement trace only if it contains enough error refine turns and passes a complex verification pipeline, which suggests raw correction traces are too noisy to trust directly.

语言反馈论文展示了邻近限制。\[Wan26ad\] 只在主线轮次上训练，旁支轮次没有训练信号。\[Yua25c\] 使用十条人工修订思路和带阈值的奖励差来识别修订点。\[Fu25d\] 只接受包含足够错误修正轮次并通过复杂验证流水线的 修订 轨迹，这暗示原始纠错轨迹噪声太大，难以直接信任。

Inference. The field has better tools for scoring partial progress than it had two years ago, but it still lacks a robust language for representing failure cause. Until that exists, many stepwise methods will remain clever credit shaping schemes rather than reliable error localization systems.

推断。与两年前相比，该领域有了更好的部分进展评分工具，但仍缺少一种稳健语言来表示失败原因。在这种表示出现之前，许多逐步方法仍会是巧妙的信用塑形方案，而不是可靠的错误定位系统。

### Reward hacking remains structural rather than incidental

### 奖励黑客仍是结构性问题


- **Supported by** \[Bai22b, Don23, Ses24, Gui24, Wu24d, Ack26, Ren26b, She24c, Xu24d, Din25b\]
  **支持文献** \[Bai22b, Don23, Ses24, Gui24, Wu24d, Ack26, Ren26b, She24c, Xu24d, Din25b\]

The strongest cross paper signal is that reward hacking is not a corner case tied to one optimizer. \[Bai22b\] reports Goodharting directly. Stronger RL pressure produces over harsh responses and repetitive boilerplate. \[Don23\] surfaces the proxy version. Appendix A.3 shows the gold reward falling while the proxy reward rises, and Appendix A.2 documents an early failure mode where the reward model favored emojis and hash symbols. \[Gui24\] gives the theoretical diagnosis that contrastive preference objectives can improve pairwise win rate by pushing down both winners and losers, which in practice shows up as length inflation and off target drift.

最强的跨论文信号是，奖励黑客并非绑定到某个优化器的边角案例。\[Bai22b\] 直接报告 古德哈特化。更强 强化学习 压力会产生过度严厉回答和重复模板。\[Don23\] 暴露了代理目标版本。附录 A.3 显示真实奖励下降而代理奖励上升，附录 A.2 记录了早期失败模式：奖励模型偏好表情符号和井号。\[Gui24\] 给出理论诊断，指出对比偏好目标可以通过同时压低赢家和输家来提升成对胜率，在实践中表现为长度膨胀和偏离目标。

The same pattern appears in judge based training. \[Wu24d\] finds that the meta judge becomes heavily biased toward high scores and longer judgments, with fractional scores emerging outside the rubric. \[Ren26b\] shows late stage collapse even when reward continues to rise, which they trace to acquiescence bias in the evaluator. \[Xu24d\] makes hacking a first class design target, but its own ablations imply that most of the benefit comes from the task specific judges rather than from the constrained optimizer alone. \[Din25b\] shows that a seemingly sensible process reward based on the ratio of correct steps leads the model to skip uncertain reasoning altogether.

同一模式也出现在基于裁判器的训练中。\[Wu24d\] 发现元裁判器严重偏向高分和更长判断，并出现了超出 评分规程 的小数分数。\[Ren26b\] 显示，即使奖励继续上升，后期仍会崩溃，他们将其追溯到评估器中的迎合偏置。\[Xu24d\] 把黑客作为一阶设计目标，但其自身消融暗示，大部分收益来自任务特定裁判器，而非仅来自受约束优化器。\[Din25b\] 显示，一种看似合理的基于正确步骤比例的过程奖励，会导致模型完全跳过不确定推理。

The defense papers are revealing because they solve only parts of the problem. \[Ack26\] convincingly shows that gradient regularization can prevent sharp peak exploitation and improve true accuracy on harder questions, but the paper is explicit that it does not rule out convergence to flat but incorrect regions. \[She24c\] shows that filtering out moderate reward regions can help because reward models are least reliable there, yet best of n filtration actually hurts in RL. \[Ses24\] argues that quantile based Best of N distillation should be more robust to reward scale and monotone transforms, but the reward hacking advantage remains mostly conjectural rather than directly stress tested.

防御论文很有启发，因为它们只解决问题的一部分。\[Ack26\] 有力显示梯度正则化可以防止尖锐峰值利用，并在更难问题上提升真实准确率，但论文明确说明它不能排除收敛到平坦但错误区域。\[She24c\] 显示过滤掉中等奖励区域会有帮助，因为奖励模型在那里最不可靠，但 多候选最优选择 过滤在 强化学习 中反而有害。\[Ses24\] 认为基于分位数的 多候选最优选择 蒸馏应当对奖励尺度和单调变换更稳健，但其奖励黑客优势主要仍是推测，而非直接压力测试结果。

Inference. The open problem is no longer to notice hacking. It is to build evaluators whose geometry, uncertainty, and update rules make exploitation hard across many failure modes rather than just one.

推断。开放问题已经不再是发现黑客现象。问题在于构建评估器，使其几何结构、不确定性和更新规则能在多种失败模式下提高利用难度，而不只是修补其中一种。

### Judge quality does not transfer cleanly across models, domains, or tasks

### 裁判器质量难以在模型、领域或任务之间干净迁移


- **Supported by** \[Guo24, Yua24, Wu24d, Xu25h, Zha26am, Fu25d, Gon24b\]
  **支持文献** \[Guo24, Yua24, Wu24d, Xu25h, Zha26am, Fu25d, Gon24b\]

A quiet but important theme is that better or larger evaluators do not automatically yield better supervision. \[Guo24\] finds that a weaker annotator can improve a stronger student, but still less effectively than a stronger annotator. That is a mild version of weak to strong transfer. \[Zha26am\] shows the failure case. SRR refinement can actively hurt a much stronger agent such as DeepSeek V3.1. The judge is good enough to help peers and weaker models, but not strong enough to supervise substantially stronger search agents.

一个低调但重要的主题是，更好或更大的评估器并不自动产生更好的监督。\[Guo24\] 发现较弱标注器可以改进较强学生，但效果仍弱于较强标注器。这是弱到强迁移的温和版本。\[Zha26am\] 展示失败情形。SRR 修订 可能主动损害 DeepSeek V3.1 这类更强智能体。裁判器足以帮助同级和更弱模型，却不足以监督明显更强的搜索智能体。

\[Xu25h\] provides an even sharper surprise. Their specialized 8B Principle based Process Reward Model beats Qwen3 235B as an evaluator on NVProcessBench. The paper attributes the larger model failure to broad exploration and weaker role fidelity. That finding undermines a common assumption that evaluator quality mostly scales with model size. \[Wu24d\] reaches a compatible conclusion from another angle. The meta judge improves mostly on self generated responses and remains weak on non self generated ones. \[Yua24\] also shows domain skew. The self rewarding loop helps writing and humanities much more than math and reasoning because the seed data underrepresents those tasks.

\[Xu25h\] 提供了更尖锐的意外结果。他们专用的 8B Principle based Process 奖励 Model 在 NVProcessBench 上作为评估器击败 Qwen3 235B。论文把更大模型的失败归因于广泛探索和较弱角色忠实度。该发现削弱了一个常见假设：评估器质量主要随模型规模增长。\[Wu24d\] 从另一个角度得到相容结论。元裁判器主要在自生成回答上改进，在非自生成回答上仍然较弱。\[Yua24\] 也显示领域偏斜。自奖励循环对写作和人文学科帮助更大，对数学和推理帮助较小，因为种子数据低估了这些任务。

There is also an authoring gap in the data pipelines. \[Fu25d\] shows that the quality of refinement data depends strongly on the synthesis model. GPT 4o based synthesis outperforms DeepSeek based synthesis on harder environments. \[Gon24b\] reaches a related result at the policy level, where smaller student agents can outperform the 34B critic that filtered their data, but only after aggressive top 10 percent selection. That means evaluator outputs can be useful even when the evaluator is not globally stronger, but only after careful interface design and filtering.

数据流水线中也存在 创制 缺口。\[Fu25d\] 显示 修订 数据质量强烈依赖合成模型。在更难环境中，基于 GPT-4o 的合成优于基于 DeepSeek 的合成。\[Gon24b\] 在策略层面得到相关结果：更小学生智能体可以超过过滤其数据的 34B 批评器，但前提是进行激进的前 10% 选择。这意味着评估器输出即便在评估器并非全局更强时也可能有用，但需要谨慎的接口设计和过滤。

Inference. Judge transfer is not just a capability ladder. It depends on domain specialization, role adherence, and how much the judged behavior resembles the data the evaluator knows how to read.

推断。裁判器迁移不只是能力阶梯。它依赖领域专门化、角色遵循，以及被评判行为与评估器熟悉数据之间的相似程度。

### Evaluation practice still hides major weaknesses

### 评估实践仍遮蔽主要弱点


- **Supported by** \[Pan24b, Zho24e, Zho25p, Wan26ac, Xu25h, Fu25d, Li26p, Luo25f\]
  **支持文献** \[Pan24b, Zho24e, Zho25p, Wan26ac, Xu25h, Fu25d, Li26p, Luo25f\]

A recurring pattern is that papers target hard agentic settings but evaluate on cleaned slices of those settings. \[Zho25p\] uses LLM based human simulators and gives them ground truth artifacts. This is reasonable for reproducibility, but it narrows the collaborative ambiguity that a real assistant would face. \[Wan26ac\] imposes a strict retrieval constraint because otherwise search agents can answer from parametric memory, which is useful scientifically but also means the benchmark is built to expose one narrow type of search reasoning. \[Xu25h\] studies non verifiable process rewards but still anchors them to exact match outcome rewards, so the hard part is shifted from the process level to the final answer scaffold.

一个反复出现的模式是，论文瞄准困难的智能体设置，却在这些设置的清洁切片上评估。\[Zho25p\] 使用基于 大语言模型 的人类模拟器，并给它们真实标注工件。这对可复现性合理，但会缩窄真实助手会面对的协作歧义。\[Wan26ac\] 强加严格检索约束，因为搜索智能体否则可能从参数化记忆中回答；这在科学上有用，但也意味着基准被构造成只暴露一种狭窄搜索推理。\[Xu25h\] 研究不可验证过程奖励，但仍将它们锚定到精确匹配的结果奖励，因此难点从过程层面转移到最终答案脚手架。

\[Pan24b\] surfaces another common convenience. Most evaluators only inspect the last frame because longer context does not help current models much. That makes the task easier to evaluate but hides temporal reasoning failures. The paper also shows how damaging false negatives are in evaluator driven refinement. A successful execution mislabeled as failure usually leads the agent to retry and then fail. \[Zho24e\] similarly depends on a verbalization module that faithfully turns state into language. Appendix G shows large disagreement between GPT 4 and Llama 2 judges, and training on the weaker judge produces a sizable drop on ALFWorld.

\[Pan24b\] 暴露了另一种常见便利。多数评估器只检查最后一帧，因为更长上下文对当前模型帮助不大。这让任务更容易评估，却隐藏了时间推理失败。论文还显示了假阴性在评估器驱动 修订 中的破坏性。一次成功执行如果被误标为失败，通常会使智能体重试并随后失败。\[Zho24e\] 同样依赖一个能忠实把状态转为语言的语言化模块。附录 G 显示 GPT-4 与 Llama-2 裁判器之间存在巨大分歧，用较弱裁判器训练会在 ALFWorld 上产生明显下降。

The newer agent papers keep running into cost motivated truncation. \[Luo25f\] evaluates at 15 and 50 steps, but the whole setup revolves around a 2B model for local execution and still shows low absolute success rates. \[Fu25d\] changes AgentBoard prompts into ReAct format and transforms historical data into chat structure. \[Li26p\] caps selector and reviewer iterations to keep evaluation bounded. These are defensible choices, yet they also mean the literature still knows more about how these methods behave under carefully budgeted conditions than under messy deployment conditions.

较新的智能体论文持续遭遇成本驱动的截断。\[Luo25f\] 在 15 步和 50 步评估，但整个设置围绕用于本地执行的 2B 模型展开，并且绝对成功率仍然较低。\[Fu25d\] 把 AgentBoard 提示改为 推理-行动 格式，并将历史数据转为聊天结构。\[Li26p\] 限制 选择器 和 审阅器 迭代次数，以保持评估有界。这些选择都可以辩护，但也意味着文献对这些方法在精心预算条件下的行为了解更多，对其在混乱部署条件下的行为了解更少。

Inference. The field now has many strong methods for evaluator guided improvement, but still too few tests where the evaluator itself is stressed by drift, ambiguity, long context, or stronger students.

推断。该领域现在已有许多强大的评估器引导改进方法，但仍很少测试评估器自身在漂移、歧义、长上下文或更强学生压力下的表现。

### Data creation and systems cost are now first order bottlenecks

### 数据创建和系统成本已经成为一阶瓶颈


- **Supported by** \[Gon24b, Fu25d, Ack26, Wan26ad, Li26p, Wan26ac, Din26e\]
  **支持文献** \[Gon24b, Fu25d, Ack26, Wan26ad, Li26p, Wan26ac, Din26e\]

Several papers quietly show that the main bottleneck is no longer inventing a loss. It is producing trustworthy supervision at acceptable cost. \[Gon24b\] runs five trials per instruction across several turns and then keeps only the top 10 percent. Table 1 shows why. About 30 percent of critic labeled successes are false positives against human judgment. \[Fu25d\] builds an even heavier pipeline with JSON checks, action matching, task success checks, and a minimum number of correction turns. Section 8 still finds that GPT 4o misses a meaningful share of wrong turns. High quality synthetic supervision is possible, but it is expensive and filter heavy.

若干论文悄然显示，主要瓶颈已不再是发明损失函数，而是在可接受成本下产生可信监督。\[Gon24b\] 对每条指令运行五次多轮尝试，然后只保留前 10%。表 1 解释了原因：约 30% 的批评器标注成功相对于人类判断是假阳性。\[Fu25d\] 构建了更重的流水线，包括 结构化数据 检查、动作匹配、任务成功检查，以及最低纠错轮数要求。第 8 节仍发现 GPT-4o 会漏掉相当一部分错误轮次。高质量合成监督是可能的，但代价高且严重依赖过滤。

The training side is no cheaper. \[Ack26\] roughly doubles or triples policy update time in their finite difference setting. \[Wan26ac\] reports a one third wall clock increase from the external judge. \[Li26p\] needs over one hundred seconds and more than fourteen VLM calls on average to evaluate a trajectory. \[Wan26ad\] adds separate cost for hosting process reward models during conversational RL. \[Din26e\] gets strong offline evaluation gains from adaptive rubrics, but at three to five times the latency of direct GPT 4 style scoring.

训练侧也不便宜。\[Ack26\] 在有限差分设置中大约使策略更新时间翻倍或变为三倍。\[Wan26ac\] 报告外部裁判器带来三分之一的 实际运行时间 增加。\[Li26p\] 平均需要一百多秒和十四次以上 视觉语言模型 调用来评估一条轨迹。\[Wan26ad\] 为会话式 强化学习 中托管过程奖励模型增加额外成本。\[Din26e\] 通过自适应 评分规程 获得强离线评估收益，但延迟达到直接 GPT-4 式评分的三到五倍。

These costs matter scientifically, not just operationally. Methods that need expensive multi pass judging, majority voting, or layered agent critics are less likely to be tested in truly online, long horizon, or open world settings. That feeds back into the evaluation problem, because the field then gravitates toward tasks whose supervision economics are affordable.

这些成本具有科学意义，而不只是操作问题。需要昂贵多轮裁判、多数投票或分层智能体批评器的方法，更不可能在真正在线、长时程或开放世界设置中测试。这会反向影响评估问题，因为领域随后会倾向于监督经济性可承受的任务。

Inference. Future progress depends as much on supervision pipeline efficiency and data curation discipline as on better RL objectives.

推断。未来进展同样依赖监督流水线效率和数据筛选纪律，不只依赖更好的 强化学习 目标。

## Future directions

## 未来方向


| Direction | What concrete progress would look like | Verification |
|:---|:---|:---|
| Co evolving and routed evaluators | Critics are refreshed or routed as the policy changes rather than frozen at the start \[Guo24, Li26l, Wu25x\] | Measure evaluator quality over training time, not just final policy win rate |
| Grounded hybrid process rewards | Process signals are tied to verifiable state changes, milestones, or outcome anchored normalization \[Xu25h, Li26p, Wan26s, Zha26am\] | Report whether denser rewards improve both learning and evaluator reliability |
| Failure native supervision | Training data preserves error cause, repair attempt, and successful recovery rather than only final success \[Din25b, Yua25c, Fu25d, Li26l\] | Evaluate recovery from seeded failures and robustness on longer horizons |
| Anti hacking evaluator stacks | Use ensembles, sparse ground truth anchors, routing, or geometric regularization rather than a single scalar judge \[Ack26, Ren26b, Wu25x, Xu24d, She24c\] | Stress test against length bias, score saturation, and proxy exploitation |
| Transfer aware judge design | Evaluators are tested across stronger students, new domains, and new agent backbones before being trusted as supervisors \[Guo24, Xu25h, Zha26am\] | Report weak to strong curves and cross domain judge degradation |
| Rubrics and explanations as reusable supervision artifacts | Rich evaluator outputs become training artifacts instead of being collapsed immediately to a scalar \[Din26e, Pan24b, Zho24e, Wan26ad\] | Compare scalar only training against rubric, critique, and directive artifact reuse |
| Harder benchmark and audit protocols | Benchmarks expose evaluator failures under drift, ambiguity, long context, and online interaction \[Pan24b, Zho25p, Li26p, Fu25d\] | Evaluate both policy success and evaluator false positive and false negative rates |

| 方向 | 具体进展形态 | 验证方式 |
|:---|:---|:---|
| 共同演化和路由式评估器 | 批评器会随着策略变化而刷新或路由，而不是从一开始就冻结 \[Guo24, Li26l, Wu25x\] | 衡量训练过程中的评估器质量，而不只衡量最终策略胜率 |
| 有依托 混合过程奖励 | 过程信号绑定到可验证状态变化、里程碑或结果锚定归一化 \[Xu25h, Li26p, Wan26s, Zha26am\] | 报告更稠密奖励是否同时改善学习和评估器可靠性 |
| 失败原生监督 | 训练数据保留错误原因、修复尝试和成功恢复，而不仅保留最终成功 \[Din25b, Yua25c, Fu25d, Li26l\] | 评估从种子失败中恢复的能力，以及长时程鲁棒性 |
| 反黑客评估器栈 | 使用集成、稀疏真实标注锚点、路由或几何正则化，而非单一标量裁判器 \[Ack26, Ren26b, Wu25x, Xu24d, She24c\] | 针对长度偏置、分数饱和和代理目标利用进行压力测试 |
| 迁移感知裁判器设计 | 评估器在被信任为监督者前，需要跨更强学生、新领域和新智能体骨干测试 \[Guo24, Xu25h, Zha26am\] | 报告弱到强曲线和跨领域裁判器退化 |
| 将 评分规程 和解释作为可复用监督工件 | 丰富评估器输出成为训练工件，而不是立即坍缩为标量 \[Din26e, Pan24b, Zho24e, Wan26ad\] | 比较仅标量训练与 评分规程、批评和指令性工件复用 |
| 更难的基准和审计协议 | 基准暴露评估器在漂移、歧义、长上下文和在线交互下的失败 \[Pan24b, Zho25p, Li26p, Fu25d\] | 同时评估策略成功率以及评估器假阳性和假阴性率 |

### Co evolving and routed evaluators should become the default rather than the exception

### 共同演化和路由式评估器应成为默认设计，而不是例外


- **Supported by** \[Guo24, Yua24, Wu24d, Ren26b, Wu25x, Li26l\]
  **支持文献** \[Guo24, Yua24, Wu24d, Ren26b, Wu25x, Li26l\]

The literature already points toward evaluators that adapt as the actor changes. \[Guo24\] is the clearest policy level example. OAIF keeps feedback online because static preference sets become off policy fast. \[Li26l\] extends the same logic to open world agents by co evolving critic and actor. The stale critic ablation is especially important because it shows that failure patterns drift in content, not just frequency. \[Wu25x\] suggests that even adaptation may need to be heterogeneous. Different reward models are better on different categories, and online Bayesian routing improves over a single judge.

文献已经指向会随行动者变化而适配的评估器。\[Guo24\] 是最清楚的策略层面例子。O人工智能F 保持反馈在线，因为静态偏好集很快变成离策略。\[Li26l\] 通过批评器和行动者共同演化，把同一逻辑扩展到开放世界智能体。陈旧批评器消融尤其重要，因为它显示失败模式是在内容上漂移，而不只是频率变化。\[Wu25x\] 暗示，即便适配也可能需要异质性。不同奖励模型擅长不同类别，在线贝叶斯路由优于单一裁判器。

The key step forward is to make evaluator adaptation explicit and measurable. A strong next paper would track judge calibration, human agreement, and category level failure over the course of policy improvement. It would compare four regimes on the same tasks: frozen judge, periodically refreshed judge, routed judge pool, and co evolving judge. It should also report when updates improve evaluator quality and when they simply chase the actor distribution.

关键前进步骤是让评估器适配变得显式且可测。强论文应当在策略改进过程中跟踪裁判器校准、人类一致性和类别级失败。它应在同一任务上比较四种机制：冻结裁判器、周期刷新裁判器、路由裁判器池和共同演化裁判器。它还应报告更新何时提升评估器质量，何时只是追随行动者分布。

A useful caution comes from the self judge papers. \[Yua24\] and \[Wu24d\] show that co improvement is possible, but \[Ren26b\] shows that live updating alone does not remove collapse. Concrete progress therefore means adaptive evaluator systems with external checks, not just more self referential loops.

自评裁判器论文提供了有用警示。\[Yua24\] 和 \[Wu24d\] 显示共同改进是可能的，但 \[Ren26b\] 显示，仅在线更新无法移除崩溃。实际进展意味着带外部检查的自适应评估器系统，而不只是更多自指循环。

### Grounded hybrid process rewards are a more promising direction than either pure scalar reward or free form judging

### 有依托 混合过程奖励比纯标量奖励或自由形式裁判更有前景


- **Supported by** \[Cha24b, Xu25h, Wan26s, Li26p, Zha26am, Wan26ac, Zho24e\]
  **支持文献** \[Cha24b, Xu25h, Wan26s, Li26p, Zha26am, Wan26ac, Zho24e\]

Pure outcome rewards are too sparse for long horizon agents, but pure free form process scoring is too easy to miscalibrate. The promising middle ground already appears in several papers. \[Xu25h\] anchors process rewards to exact match and enforces sign consistency. \[Li26p\] decomposes GUI evaluation into milestones and uses a final holistic judge to avoid local evidence dilution. \[Wan26s\] treats step returns as estimates of task completion and filters unstable low variance groups. \[Zha26am\] uses step ratings for search reasoning but validates them through multi run voting and trajectory level filtering.

纯结果奖励对长时程智能体过于稀疏，纯自由形式过程评分又太容易误校准。若干论文已经出现有前景的中间路径。\[Xu25h\] 将过程奖励锚定到精确匹配，并强制符号一致性。\[Li26p\] 把 图形界面 评估分解为里程碑，并使用最终整体裁判器避免局部证据稀释。\[Wan26s\] 将步骤回报视为任务完成估计，并过滤不稳定的低方差组。\[Zha26am\] 使用步骤评分进行搜索推理，但通过多次运行投票和轨迹级过滤来验证它们。

What concrete progress would look like is not just another denser reward. It would be a reward stack in which each intermediate signal corresponds to a verifiable state change, milestone, or grounded progress event. In GUI domains that could mean validated navigation state and action effect. In search it could mean evidence acquisition and correct integration. In reasoning it could mean error localization tied to a reference or verifier, not just style scoring.

实际进展不会只是另一种更稠密奖励。它应是一个奖励栈，其中每个中间信号都对应可验证状态变化、里程碑或 有依托 进展事件。在 图形界面 领域，这可以是经过验证的导航状态和动作效果。在搜索中，可以是证据获取和正确整合。在推理中，可以是绑定到参考答案或验证器的错误定位，而不只是风格评分。

Verification should compare reward informativeness against reward trustworthiness. The literature already shows that many dense signals help optimization while making the judge easier to exploit. A stronger next generation of work would report both learning gains and evaluator failure rates under adversarial or shifted trajectories.

验证应比较奖励信息量和奖励可信度。文献已经显示，许多稠密信号有助于优化，却让裁判器更容易被利用。更强的下一代工作应同时报告学习收益和评估器在对抗或转移轨迹下的失败率。

### Failure native supervision should replace success only filtering

### 失败原生监督应取代只保留成功的过滤


- **Supported by** \[Din25b, Che25v, Yua25c, Fu25d, Li26l, Wan26ad\]
  **支持文献** \[Din25b, Che25v, Yua25c, Fu25d, Li26l, Wan26ad\]

Some of the most valuable evidence in this set comes from papers that learn from flawed or corrected behavior rather than only from wins. \[Din25b\] is explicit that flawed positives must be separated from fully correct trajectories. \[Che25v\] shows that informative negative samples can rescue GRPO from forgetting previously solvable tasks. \[Yua25c\] turns revision points and recovery traces into training data. \[Fu25d\] pushes this further by masking erroneous turns and training only on the refinement process, which is one of the cleanest demonstrations that the correction trajectory can matter more than the original success trace.

这一组中部分最有价值的证据来自学习有缺陷或被修正的行为，而不只是胜利样本。\[Din25b\] 明确指出，带缺陷的正样本必须与完全正确轨迹分开。\[Che25v\] 显示，信息丰富的负样本可以挽救 组相对策略优化 对先前可解任务的遗忘。\[Yua25c\] 将修订点和恢复轨迹转为训练数据。\[Fu25d\] 进一步推进，掩蔽错误轮次并只在 修订 过程上训练，这是纠错轨迹比原始成功轨迹更重要的最清楚示范之一。

\[Li26l\] offers a complementary angle. The critic becomes more fine grained as the actor improves, which suggests failure itself has a curriculum structure. \[Wan26ad\] shows that directive hints and scalar rewards are complementary, which is exactly what a failure native pipeline would want: diagnosis plus optimization signal.

\[Li26l\] 提供了互补角度。随着行动者改进，批评器变得更细粒度，这暗示失败本身具有课程结构。\[Wan26ad\] 显示指令性提示和标量奖励互补，这正是失败原生流水线所需要的：诊断加优化信号。

Concrete progress would mean storing a richer object than a binary bad trajectory. Each failure case should preserve at least the suspected error span, the repair attempt, the post repair outcome, and the confidence of the diagnosis. A convincing evaluation would seed known failure families, then test whether the learned system recovers earlier and generalizes that recovery to longer tasks rather than merely memorizing local patches.

实际进展意味着存储比二元坏轨迹更丰富的对象。每个失败案例至少应保留疑似错误跨度、修复尝试、修复后结果和诊断置信度。有说服力的评估应植入已知失败族，然后测试学习系统是否更早恢复，并将这种恢复泛化到更长任务，而不只是记住局部补丁。

### Anti hacking evaluator stacks need to be treated as core method design, not as cleanup

### 反黑客评估器栈需要被视为核心方法设计，而不是收尾清理


- **Supported by** \[Ack26, Ren26b, She24c, Wu25x, Xu24d, Fis24, Bai22b\]
  **支持文献** \[Ack26, Ren26b, She24c, Wu25x, Xu24d, Fis24, Bai22b\]

The literature already contains a menu of partial defenses. \[Ack26\] regularizes the reward geometry. \[Ren26b\] shows that even 1 percent ground truth anchoring can sharply reduce late stage collapse. \[She24c\] filters out the moderate reward region where reward models are least trustworthy. \[Wu25x\] spreads supervisory load across multiple reward models. \[Xu24d\] uses judge mixtures and explicit constraints. \[Fis24\] distills through explicit reward models and ensembles rather than relying on the implicit reward in DPO. \[Bai22b\] improves robustness by ensembling constitutional principles.

文献已经包含一组局部防御。\[Ack26\] 正则化奖励几何。\[Ren26b\] 显示，即使 1% 的真实标注锚定也能显著减少后期崩溃。\[She24c\] 过滤掉奖励模型最不可信的中等奖励区域。\[Wu25x\] 将监督负载分摊到多个奖励模型。\[Xu24d\] 使用裁判器混合和显式约束。\[Fis24\] 通过显式奖励模型和集成蒸馏，而非依赖 直接偏好优化 中的隐式奖励。\[Bai22b\] 通过集成宪法原则改进鲁棒性。

The next step is to combine these ideas into evaluator stacks that expose and limit exploitability. A strong system would not trust a single score. It would combine uncertainty, disagreement, and grounded checks. It would also report where each layer fails. For example, does routing reduce length bias but increase category instability. Does sparse ground truth anchoring protect late stage collapse but reduce exploration.

下一步是把这些想法组合成能暴露并限制可利用性的评估器栈。强系统不应信任单一分数。它应结合不确定性、分歧和 有依托 检查。它还应报告每一层在哪里失败。例如，路由是否降低长度偏置却增加类别不稳定性；稀疏真实标注锚定是否保护后期崩溃却降低探索。

Concrete verification should include deliberate hacking probes. The model should be tested for length inflation, score saturation, formatting exploitation, acquiescence bias, and reward scale drift. Right now many papers demonstrate robustness only on the pathology they were built to fix.

具体验证应包含刻意黑客探针。模型应测试长度膨胀、分数饱和、格式利用、迎合偏置和奖励尺度漂移。当前许多论文只在其设计所针对的病灶上展示鲁棒性。

### Transfer aware judge design should become a required evaluation axis

### 迁移感知裁判器设计应成为必要评估轴


- **Supported by** \[Guo24, Wu24d, Xu25h, Zha26am, Fu25d\]
  **支持文献** \[Guo24, Wu24d, Xu25h, Zha26am, Fu25d\]

Several papers already show that judge quality is conditional on who is being judged. \[Guo24\] offers a mild weak to strong success case. \[Zha26am\] shows the failure case where refinement hurts a stronger agent. \[Wu24d\] shows that meta judging improves mostly on self generated responses. \[Xu25h\] shows that a smaller specialist can beat a much larger general evaluator. \[Fu25d\] adds that the quality of correction data changes materially with the synthesis model.

若干论文已经显示，裁判器质量取决于它在评判谁。\[Guo24\] 提供了温和的弱到强成功案例。\[Zha26am\] 展示了 修订 损害更强智能体的失败案例。\[Wu24d\] 显示元裁判主要在自生成回答上改进。\[Xu25h\] 显示较小的专用评估器可以击败更大的通用评估器。\[Fu25d\] 补充说明，纠错数据质量会随合成模型发生实质变化。

A promising direction is to turn this from a surprise into a standard protocol. Evaluators should be benchmarked across weaker, similar, and stronger students, as well as across nearby and far domain shifts. The report card should not just be agreement with humans on a held out set. It should include weak to strong degradation, cross domain degradation, and failure asymmetry such as false positives versus false negatives.

有前景的方向是把这种意外现象转为标准协议。评估器应跨更弱、相近和更强学生，以及相近和遥远领域转移进行基准测试。成绩单不应只包含与人类在保留集上的一致性。它应包含弱到强退化、跨领域退化，以及假阳性和假阴性等失败不对称。

Concrete progress would look like evaluator papers reporting transfer matrices rather than a single correlation number. That would immediately clarify whether a judge is a general supervisor, a domain specialist, or only a same distribution tool.

实际进展应体现为评估器论文报告迁移矩阵，而非单一相关数值。那会立即澄清一个裁判器是通用监督者、领域专家，还是仅同分布工具。

### Rubrics, critiques, and explanations should be preserved as reusable supervision artifacts

### 评分规程、批评和解释应保留为可复用监督工件


- **Supported by** \[Din26e, Pan24b, Zho24e, Wan26ad, Yua25c, Fu25d\]
  **支持文献** \[Din26e, Pan24b, Zho24e, Wan26ad, Yua25c, Fu25d\]

A striking underused resource in these papers is the evaluator output itself. \[Pan24b\] explicitly notes that its natural language explanations are discarded and could be used to improve policies. \[Zho24e\] shows that detailed language feedback can match succinct feedback in final policy performance, which means explanations need not be treated as expensive decoration. \[Din26e\] makes the strongest structural case. Static scalar judgments hide dimension level failure, while adaptive rubrics preserve which aspect of performance broke. \[Wan26ad\] finds that directive signals and scalar rewards are complementary, with textual hints supplying token level directional guidance that binary RL alone cannot provide.

这些论文中一个醒目但未被充分使用的资源是评估器输出本身。\[Pan24b\] 明确指出，其自然语言解释被丢弃，但可用于改进策略。\[Zho24e\] 显示，详细语言反馈可以在最终策略性能上匹配简洁反馈，这意味着解释不必被视为昂贵装饰。\[Din26e\] 给出最强的结构性论证。静态标量判断隐藏维度级失败，而自适应 评分规程 保留了哪个表现维度出错。\[Wan26ad\] 发现指令性信号和标量奖励互补，文本提示提供了二元 强化学习 单独无法提供的 词元 级方向引导。

\[Yua25c\] and \[Fu25d\] provide concrete examples of what reusable artifact supervision can look like: revision trajectories, correction spans, and masked refinement targets. These artifacts are likely to matter most in the exact settings where scalar reward is weakest, namely long horizon and partially observable tasks.

\[Yua25c\] 和 \[Fu25d\] 提供了可复用工件监督的具体例子：修订轨迹、纠错跨度和掩蔽 修订 目标。这些工件很可能在标量奖励最弱的设置中最重要，即长时程和部分可观察任务。

Concrete progress here would mean comparing three training regimes on the same data: scalar reward only, scalar plus critique text, and structured rubric or correction artifact supervision. Verification should measure not just end score but recovery ability, sample efficiency, and robustness under evaluator disagreement. The field has enough evidence to justify treating evaluator outputs as first class training data.

这里的实际进展意味着在同一数据上比较三种训练机制：仅标量奖励、标量加批评文本，以及结构化 评分规程 或纠错工件监督。验证不仅应衡量最终分数，还应衡量恢复能力、样本效率和评估器分歧下的鲁棒性。该领域已有足够证据支持把评估器输出视为一阶训练数据。

### Harder benchmark and audit protocols are needed if evaluator papers are to claim generality

### 如果评估器论文要声称通用性，就需要更难的基准和审计协议


- **Supported by** \[Pan24b, Zho25p, Li26p, Fu25d, Zho24e, Zha26am\]
  **支持文献** \[Pan24b, Zho25p, Li26p, Fu25d, Zho24e, Zha26am\]

Current benchmarks often make evaluator development feasible by narrowing the problem. The next step is to stress the evaluators themselves. \[Pan24b\] shows why asymmetric error costs matter and why reasoning errors dominate. \[Zho25p\] still depends on simulator collaborators with hidden ground truth. \[Li26p\] exposes distributional mismatch when the test set shifts from multi step to single action trajectories. \[Fu25d\] finds a nontrivial gap between GPT 4o turn labels and human judgment on wrong turns. \[Zho24e\] shows large evaluator disagreement in grounded settings. \[Zha26am\] shows that a judge that works on one model scale can fail on a stronger one.

当前基准常通过缩窄问题来让评估器开发变得可行。下一步是对评估器自身施压。\[Pan24b\] 显示了为什么非对称错误成本很重要，以及为什么推理错误占主导。\[Zho25p\] 仍依赖带隐藏真实标注的模拟协作者。\[Li26p\] 暴露了测试集从多步轨迹转向单动作轨迹时的分布不匹配。\[Fu25d\] 发现 GPT-4o 轮次标签与人类对错误轮次的判断之间存在非平凡差距。\[Zho24e\] 显示 有依托 设置中的评估器分歧很大。\[Zha26am\] 显示，在一个模型规模上有效的裁判器可能在更强模型上失败。

A concrete benchmark agenda would therefore vary at least four axes: stronger students, longer horizons, noisier or more ambiguous environments, and evaluator audit with human spot checks. It should report false positive and false negative rates separately because these errors have very different downstream consequences. It should also include some online or semi online interaction rather than only replayed trajectories.

一套具体基准议程至少应变化四个轴：更强学生、更长时程、更有噪声或更歧义的环境，以及带人类抽查的评估器审计。它应分别报告假阳性和假阴性率，因为这些错误具有非常不同的下游后果。它还应包含某种在线或半在线交互，而不只是回放轨迹。

Progress on this front would not look glamorous, but it would have high value for CSUR style synthesis. It would separate methods that genuinely improve evaluator driven learning from methods that only fit the current experimental scaffolds.

这条方向的进展未必醒目，但对 综述 式综合很有价值。它会区分真正改进评估器驱动学习的方法，以及只适配当前实验脚手架的方法。

---

## References

\[Lee23b\] H. Lee *et al.*, “RLAIF vs. RLHF: Scaling Reinforcement Learning from Human Feedback with AI Feedback,” *International Conference on Machine Learning*, pp. 26874–26901, Sep. 2023.

\[Guo24\] S. Guo *et al.*, “Direct Language Model Alignment from Online AI Feedback,” *ArXiv*, vol. abs/2402.04792, Feb. 2024, doi: [10.48550/arXiv.2402.04792](https://doi.org/10.48550/arXiv.2402.04792).

\[Wu24d\] T. Wu *et al.*, “Meta-Rewarding Language Models: Self-Improving Alignment with LLM-as-a-Meta-Judge,” *ArXiv*, vol. abs/2407.19594, Jul. 2024, doi: [10.48550/arXiv.2407.19594](https://doi.org/10.48550/arXiv.2407.19594).

\[Ren26b\] M. Rentschler and J. Roberts, “Reinforcement Learning from Meta-Evaluation: Aligning Language Models Without Ground-Truth Labels,” *ArXiv*, vol. abs/2601.21268, Jan. 2026, doi: [10.48550/arXiv.2601.21268](https://doi.org/10.48550/arXiv.2601.21268).

\[Li26l\] Z. Li *et al.*, “No More Stale Feedback: Co-Evolving Critics for Open-World Agent Learning,” *ArXiv*, vol. abs/2601.06794, Jan. 2026, doi: [10.48550/arXiv.2601.06794](https://doi.org/10.48550/arXiv.2601.06794).

\[Cha24b\] A. J. Chan, H. Sun, S. Holt, and M. Schaar, “Dense Reward for Free in Reinforcement Learning from Human Feedback,” *ArXiv*, vol. abs/2402.00782, Feb. 2024, doi: [10.48550/arXiv.2402.00782](https://doi.org/10.48550/arXiv.2402.00782).

\[Xu25h\] P. Xu, Z. Li, X. Xing, G. Zhang, D. Li, and K. Shi, “Hybrid Reward Normalization for Process-supervised Non-verifiable Agentic Tasks,” *ArXiv*, vol. abs/2509.25598, Sep. 2025, doi: [10.48550/arXiv.2509.25598](https://doi.org/10.48550/arXiv.2509.25598).

\[Che25v\] P. Chen, X. Li, Z. Li, X. Chen, and T. Lin, “Stepwise Guided Policy Optimization: Coloring Your Incorrect Reasoning in GRPO,” *Trans. Mach. Learn. Res.*, vol. 2026, May 2025.

\[Wan26ac\] J. Wang *et al.*, “Enhancing LLM-based Search Agents via Contribution Weighted Group Relative Policy Optimization,” Apr. 15, 2026.

\[Wan26s\] Y. Wang *et al.*, “Building Autonomous GUI Navigation via Agentic-Q Estimation and Step-Wise Policy Optimization,” *ArXiv*, vol. abs/2602.13653, Feb. 2026, doi: [10.48550/arXiv.2602.13653](https://doi.org/10.48550/arXiv.2602.13653).

\[Li26p\] Z. Li *et al.*, “OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards,” Mar. 2026.

\[Zha26am\] C. Zhang *et al.*, “SRR-Judge: Step-Level Rating and Refinement for Enhancing Search-Integrated Reasoning in Search Agents,” *ArXiv*, vol. abs/2602.07773, Feb. 2026, doi: [10.48550/arXiv.2602.07773](https://doi.org/10.48550/arXiv.2602.07773).

\[Zho25p\] Y. Zhou *et al.*, “SWEET-RL: Training Multi-Turn LLM Agents on Collaborative Reasoning Tasks,” *ArXiv*, vol. abs/2503.15478, Mar. 2025, doi: [10.48550/arXiv.2503.15478](https://doi.org/10.48550/arXiv.2503.15478).

\[Luo25f\] M. Luo *et al.*, “DPO Learning with LLMs-Judge Signal for Computer Use Agents,” *ArXiv*, vol. abs/2506.03095, Jun. 2025, doi: [10.48550/arXiv.2506.03095](https://doi.org/10.48550/arXiv.2506.03095).

\[Wan26ad\] Y. Wang, X. Chen, X. Jin, M. Wang, and L. Yang, “OpenClaw-RL: Train Any Agent Simply by Talking,” Mar. 10, 2026.

\[Bai22b\] Y. Bai *et al.*, “Constitutional AI: Harmlessness from AI Feedback,” *ArXiv*, vol. abs/2212.08073, Dec. 2022, doi: [10.48550/arXiv.2212.08073](https://doi.org/10.48550/arXiv.2212.08073).

\[Don23\] H. Dong *et al.*, “RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment,” *ArXiv*, vol. abs/2304.06767, Apr. 2023, doi: [10.48550/arXiv.2304.06767](https://doi.org/10.48550/arXiv.2304.06767).

\[Gui24\] L. Gui, C. Garbacea, and V. Veitch, “BoNBoN Alignment for Large Language Models and the Sweetness of Best-of-n Sampling,” *ArXiv*, vol. abs/2406.00832, Jun. 2024, doi: [10.48550/arXiv.2406.00832](https://doi.org/10.48550/arXiv.2406.00832).

\[Ack26\] J. Ackermann, M. Noukhovitch, T. Ishida, and M. Sugiyama, “Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards,” *ArXiv*, vol. abs/2602.18037, Feb. 2026, doi: [10.48550/arXiv.2602.18037](https://doi.org/10.48550/arXiv.2602.18037).

\[Din25b\] Y. Ding, C. Zhang, J. Li, H. Lin, X. Liu, and M. Zhang, “FAPO: Flawed-Aware Policy Optimization for Efficient and Reliable Reasoning,” *ArXiv*, vol. abs/2510.22543, Oct. 2025, doi: [10.48550/arXiv.2510.22543](https://doi.org/10.48550/arXiv.2510.22543).

\[Xu24d\] T. Xu *et al.*, “The Perfect Blend: Redefining RLHF with Mixture of Judges,” *ArXiv*, vol. abs/2409.20370, Sep. 2024, doi: [10.48550/arXiv.2409.20370](https://doi.org/10.48550/arXiv.2409.20370).

\[Fu25d\] D. Fu *et al.*, “AgentRefine: Enhancing Agent Generalization through Refinement Tuning,” *ArXiv*, vol. abs/2501.01702, Jan. 2025, doi: [10.48550/arXiv.2501.01702](https://doi.org/10.48550/arXiv.2501.01702).

\[Pan24b\] J. Pan, Y. Zhang, N. Tomlin, Y. Zhou, S. Levine, and A. Suhr, “Autonomous Evaluation and Refinement of Digital Agents,” *ArXiv*, vol. abs/2404.06474, Apr. 2024, doi: [10.48550/arXiv.2404.06474](https://doi.org/10.48550/arXiv.2404.06474).

\[Zho24e\] V. Zhong, D. Misra, X. Yuan, and M.-A. Côté, “Policy Improvement using Language Feedback Models,” *ArXiv*, vol. abs/2402.07876, Feb. 2024, doi: [10.48550/arXiv.2402.07876](https://doi.org/10.48550/arXiv.2402.07876).

\[Gon24b\] D. Gong, P. Lu, Z. Wang, M. Zhou, and X. He, “Training Agents with Weakly Supervised Feedback from Large Language Models,” *ArXiv*, vol. abs/2411.19547, Nov. 2024, doi: [10.48550/arXiv.2411.19547](https://doi.org/10.48550/arXiv.2411.19547).

\[Yua24\] W. Yuan, R. Y. Pang, K. Cho, S. Sukhbaatar, J. Xu, and J. Weston, “Self-Rewarding Language Models,” *ArXiv*, vol. abs/2401.10020, Jan. 2024, doi: [10.48550/arXiv.2401.10020](https://doi.org/10.48550/arXiv.2401.10020).

\[Wu25x\] X. Wu and Y. Lu, “Reward Model Routing in Alignment,” *ArXiv*, vol. abs/2510.02850, Oct. 2025, doi: [10.48550/arXiv.2510.02850](https://doi.org/10.48550/arXiv.2510.02850).

\[Yua25c\] S. Yuan, Z. Chen, Z. Xi, J. Ye, Z. Du, and J. Chen, “Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training,” *ArXiv*, vol. abs/2501.11425, Jan. 2025, doi: [10.48550/arXiv.2501.11425](https://doi.org/10.48550/arXiv.2501.11425).

\[Ses24\] P. G. Sessa *et al.*, “BOND: Aligning LLMs with Best-of-N Distillation,” *ArXiv*, vol. abs/2407.14622, Jul. 2024, doi: [10.48550/arXiv.2407.14622](https://doi.org/10.48550/arXiv.2407.14622).

\[She24c\] W. Shen and C. Zhang, “Policy Filtration for RLHF to Mitigate Noise in Reward Models,” *International Conference on Machine Learning*, Sep. 2024.

\[Din26e\] L. Ding, “AdaRubric: Task-Adaptive Rubrics for LLM Agent Evaluation,” Mar. 22, 2026.

\[Fis24\] A. Fisch *et al.*, “Robust Preference Optimization through Reward Model Distillation,” *ArXiv*, vol. abs/2405.19316, May 2024, doi: [10.48550/arXiv.2405.19316](https://doi.org/10.48550/arXiv.2405.19316).
