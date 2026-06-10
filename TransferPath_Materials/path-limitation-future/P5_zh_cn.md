# Experience transformation gaps for CSUR

# 面向 CSUR 的经验转化缺口

##### [**Undermind**](https://undermind.ai)

##### [**Undermind**](https://undermind.ai) 资料源

---


## Table of Contents

- [Challenges](#challenges)
  - [Warm start dependence and the sparse success threshold](#warm-start-dependence-and-the-sparse-success-threshold)
  - [Credit assignment remains unresolved across levels of granularity](#credit-assignment-remains-unresolved-across-levels-of-granularity)
  - [Exploration and optimization stability are still in tension](#exploration-and-optimization-stability-are-still-in-tension)
  - [Generalization gains are real but still mostly local](#generalization-gains-are-real-but-still-mostly-local)
  - [Reward design and evaluation still flatter current methods](#reward-design-and-evaluation-still-flatter-current-methods)
  - [Synthetic experience scales, but quality control remains the real bottleneck](#synthetic-experience-scales-but-quality-control-remains-the-real-bottleneck)
  - [Grounding and representation losses still block robust reuse](#grounding-and-representation-losses-still-block-robust-reuse)
  - [The systems burden now shapes the science](#the-systems-burden-now-shapes-the-science)
- [Future directions](#future-directions)
  - [Failure-native pipelines should become the default](#failure-native-pipelines-should-become-the-default)
  - [Multi-scale credit assignment should replace single-granularity objectives](#multi-scale-credit-assignment-should-replace-single-granularity-objectives)
  - [Horizon-adaptive exploration control is likely more important than stronger generic entropy bonuses](#horizon-adaptive-exploration-control-is-likely-more-important-than-stronger-generic-entropy-bonuses)
  - [Offline and off-policy experience should be used more deliberately, not just as a fallback](#offline-and-off-policy-experience-should-be-used-more-deliberately-not-just-as-a-fallback)
  - [Reward models and evaluators need to become more grounded without giving up verifiability](#reward-models-and-evaluators-need-to-become-more-grounded-without-giving-up-verifiability)
  - [Experience representations should preserve more of the original environment signal](#experience-representations-should-preserve-more-of-the-original-environment-signal)
  - [Transfer-oriented training and evaluation should become the default standard](#transfer-oriented-training-and-evaluation-should-become-the-default-standard)
  - [Real-world online learning systems deserve to be treated as core methodology](#real-world-online-learning-systems-deserve-to-be-treated-as-core-methodology)
- [References](#references)

## Challenges

## 挑战

| Challenge | What the papers collectively show | Representative support |
|:---|:---|:---|
| Learning still depends on a warm start | Most methods need competent demonstrations, strong teachers, or at least some successful rollouts before experience can be turned into useful supervision | \[Pat24\], \[Son24\], \[Da25\], \[Wei25\], \[Li25aa\], \[Pap25c\] |
| Credit assignment is still the central technical bottleneck | Outcome rewards are too sparse, step rewards are noisy, and token-level optimization often mismatches turn-level decision structure | \[Shi24c\], \[Gao25c\], \[Zho24f\], \[Fen25c\], \[Li25ae\], \[Li26r\] |
| Exploration and stability pull against each other | Methods that push exploration often trigger entropy drift, loops, or collapse, while methods that stabilize training can prematurely narrow behavior | \[Xu25k\], \[Don25d\], \[Don25c\], \[Wan25ad\], \[Xi25c\], \[Che25af\] |
| Generalization remains shallow | Gains are often strong on seen tasks or nearby templates but weaken on unseen sites, unseen apps, new interfaces, and truly novel skill combinations | \[Pap25b\], \[Gan25b\], \[Gu26b\], \[Lu25f\], \[Zha25an\], \[Wei25\] |
| Reward design and evaluation still hide the real difficulty | Binary success signals, proxy judges, and curated subsets often make progress look cleaner than it is | \[Pah25\], \[Liu25z\], \[Wan25y\], \[Hua26d\], \[Gu26b\], \[Pan24\] |
| Synthetic and self-generated experience is abundant but noisy | Many pipelines discard most collected experience, and even accepted trajectories often contain hidden errors, teacher bias, or narrow task coverage | \[Zen23d\], \[Xu24\], \[Mur24b\], \[Pah25\], \[Lai25d\], \[Pan24\] |
| Grounding and representation remain weak | Agents still lose crucial state when text compresses GUI, web, or embodied environments, and many failures are perceptual or interface specific rather than purely strategic | \[Pap25b\], \[Xu24\], \[Zha24s\], \[Szo23\], \[Hu26e\], \[Pap25c\] |
| The systems burden is now part of the research problem | Rollouts are slow, environments are brittle, and scalable online learning increasingly depends on engineering choices rather than just better objectives | \[Pan24\], \[Gol25\], \[Zha25ag\], \[Gu26b\], \[Lu25f\], \[Pap25c\] |

| 挑战 | 这些论文共同显示的现象 | 代表性依据 |
|:---|:---|:---|
| 学习仍依赖暖启动 | 多数方法需要有能力的示范、强教师，或至少若干成功采样轨迹，经验才能转化为有用监督 | \[Pat24\], \[Son24\], \[Da25\], \[Wei25\], \[Li25aa\], \[Pap25c\] |
| 信用分配仍是中心技术瓶颈 | 结果奖励过于稀疏，步骤奖励带噪，token 级优化常与轮次级决策结构错配 | \[Shi24c\], \[Gao25c\], \[Zho24f\], \[Fen25c\], \[Li25ae\], \[Li26r\] |
| 探索与稳定性相互拉扯 | 推动探索的方法常触发熵漂移、循环或崩塌，稳定训练的方法又可能过早收窄行为 | \[Xu25k\], \[Don25d\], \[Don25c\], \[Wan25ad\], \[Xi25c\], \[Che25af\] |
| 泛化仍然浅 | 增益常在已见任务或邻近模板上很强，但在未见站点、未见应用、新界面和真正新颖技能组合上减弱 | \[Pap25b\], \[Gan25b\], \[Gu26b\], \[Lu25f\], \[Zha25an\], \[Wei25\] |
| 奖励设计和评估仍隐藏真实难度 | 二元成功信号、代理裁判器和策划子集常让进展看起来比实际更干净 | \[Pah25\], \[Liu25z\], \[Wan25y\], \[Hua26d\], \[Gu26b\], \[Pan24\] |
| 合成与自生成经验充足但有噪 | 许多流水线丢弃大多数已收集经验，即便被接收的轨迹也常包含隐藏错误、教师偏差或狭窄任务覆盖 | \[Zen23d\], \[Xu24\], \[Mur24b\], \[Pah25\], \[Lai25d\], \[Pan24\] |
| Grounding 和表示仍然薄弱 | 当文本压缩图形界面、网页或具身环境时，智能体仍会丢失关键状态，许多失败是感知或界面特定的，而非纯策略性的 | \[Pap25b\], \[Xu24\], \[Zha24s\], \[Szo23\], \[Hu26e\], \[Pap25c\] |
| 系统负担如今是研究问题的一部分 | 采样轨迹很慢，环境很脆弱，可扩展在线学习越来越依赖工程选择，而不只是更好的目标 | \[Pan24\], \[Gol25\], \[Zha25ag\], \[Gu26b\], \[Lu25f\], \[Pap25c\] |

### Warm start dependence and the sparse success threshold

### 暖启动依赖与稀疏成功阈值

A recurring pattern across imitation, preference, and reward based papers is that learning from experience rarely starts from raw interaction. It starts from a preconditioned agent that already knows enough to produce at least some useful trajectories. \[Pat24\] improves web agents by filtering self-generated data, but Table 1 shows how low the raw success rate is before filtering, and Appendix E shows that later self-improvement rounds degrade once the collected pool becomes lower quality. \[Son24\] is even more direct: ETO needs successful trajectories to form contrastive pairs, and Table 5 shows that without a behavioral cloning warm start, the method does not improve. \[Wei25\] reports the same structure in web RL, where the zero warm-up variant deteriorates rather than learns. \[Li25aa\] shows the hard version of this failure in embodied control: when the base model has zero initial success, RL produces zero improvement and stays at zero across tasks in Table 7. \[Pap25c\] reaches a similar conclusion in mobile control, arguing that SoLS can only learn patterns that the initial SFT and exploration distribution already exposes.

在模仿、偏好和基于奖励的论文中，一个反复模式是：从经验中学习很少从原始交互开始。它从一个已有先验条件的智能体开始，这个智能体已经知道足够多，能至少产生一些有用轨迹。\[Pat24\] 通过过滤自生成数据改进网页智能体，但表 1 显示过滤前原始成功率有多低，附录 E 显示，一旦收集池质量下降，后续自我改进轮次就会退化。\[Son24\] 更直接：ETO 需要成功轨迹来形成对比对，表 5 显示，若没有行为克隆暖启动，该方法不会改进。\[Wei25\] 在网页强化学习中报告了相同结构，其中零暖启动变体不是学习，而是退化。\[Li25aa\] 在具身控制中显示了这一失败的硬版本：当基础模型初始成功为零时，强化学习带来零改进，并在表 7 的各任务上保持为零。\[Pap25c\] 在移动控制中得到类似结论，认为 SoLS 只能学习初始监督微调和探索分布已经暴露出来的模式。

What makes this more than a cold-start cliché is that the threshold is not just about getting any reward at all. It is about getting the right kind of diversity above that threshold. \[Da25\] shows that guidance helps agentic RL primarily by making successful trajectories common enough to optimize against. \[Pan24\] finds that self-improvement on a model’s own successful trajectories can still reduce performance if the source policy is too weak or too narrow. \[Guo25d\] in VLA training and \[Pap25b\] in app control both rely on selecting successful or near successful trajectories for later policy updates, which means the pipeline inherits the blind spots of the early policy. **Inference.** The field still lacks a method that can reliably bootstrap from mostly failing interaction data without either a strong teacher, heavy shaping, or manually engineered curriculum \[Pat24, Son24, Wei25, Li25aa, Pap25c\].

使这一点超出冷启动套话的是，阈值不只是关于获得任何奖励，而是关于在阈值以上获得合适类型的多样性。\[Da25\] 显示，引导帮助智能体式强化学习，主要是因为它让成功轨迹足够常见，可供优化。\[Pan24\] 发现，如果源策略太弱或太窄，在模型自身成功轨迹上做自我改进仍可能降低性能。\[Guo25d\] 在 VLA 训练中、\[Pap25b\] 在应用控制中，都依赖选择成功或接近成功的轨迹用于后续策略更新，这意味着流水线会继承早期策略的盲点。**推断。** 该领域仍缺少一种方法，能在没有强教师、重度塑形或手工课程的情况下，从大多失败的交互数据中可靠引导启动 \[Pat24, Son24, Wei25, Li25aa, Pap25c\]。

### Credit assignment remains unresolved across levels of granularity

### 信用分配在不同粒度层级上仍未解决

Long horizon agent learning still does not know what the right supervision unit is. \[Shi24c\] shows why single-turn DPO breaks in multi-turn settings: the partition function no longer cancels, trajectory length disparity introduces bias, and noisy lose trajectories poison preference learning. \[Gao25c\] frames this as a granularity mismatch. Trajectory-level supervision is stable but blurry, while step-level supervision is precise but statistically noisy. Their ablations show that the group-level signal does most of the work, yet the full method still needs trajectory and step level terms to perform best. \[Fen25c\] reaches a parallel result from the RL side: removing either episode-relative or step-relative advantages causes major drops, especially on harder ALFWorld tasks. \[Li25ae\] argues that even token-level PPO is a poor fit for multi-turn agents because environment transitions happen between turns, not smoothly between tokens, so turn-level advantage estimation is more stable. \[Li26r\] shows the same issue in SQL agents, where pure final-turn reward throws away partially correct intermediate work.

长时域智能体学习仍不知道合适的监督单元是什么。\[Shi24c\] 显示了为何单轮 DPO 会在多轮设置中失效：配分函数不再抵消，轨迹长度差异引入偏差，带噪失败轨迹污染偏好学习。\[Gao25c\] 将其表述为粒度错配。轨迹级监督稳定但模糊，步骤级监督精确但统计上有噪。其消融显示，组级信号完成了大部分工作，但完整方法仍需要轨迹级和步骤级项才能表现最好。\[Fen25c\] 从强化学习侧得到平行结果：移除 episode 相对优势或步骤相对优势都会造成大幅下降，尤其是在更难的 ALFWorld 任务上。\[Li25ae\] 认为，即便 token 级 PPO 也不适合多轮智能体，因为环境转移发生在轮次之间，而不是平滑发生在 token 之间，因此轮次级优势估计更稳定。\[Li26r\] 在 SQL 智能体中显示了同一问题，纯最终轮奖励会丢弃部分正确的中间工作。

The hidden disagreement is important. Some papers argue for denser process level signals. Others show that naive dense signals are unstable or misleading. \[Son24\] tried step-wise contrastive modeling and found it less stable because final rewards are too weak a proxy for local action quality. \[Wan25y\] proposes information gain because final outcome rewards collapse too often, yet Table 3 shows that information gain alone is not enough and must be anchored by outcome rewards. \[Hua26d\] adds interleaved SQL feedback and shaped rewards, but its ablations show substantial redundancy among some reward components once the main scaffolds are in place. **Inference.** The field has moved past the question of whether agents need denser feedback. The open question is which intermediate signals are causally aligned with later success and which only create the appearance of fine-grained supervision \[Shi24c, Son24, Gao25c, Wan25y, Li25ae, Li26r\].

隐含分歧很重要。一些论文主张更稠密的过程级信号。另一些论文显示，朴素稠密信号不稳定或具有误导性。\[Son24\] 尝试逐步对比建模，发现它更不稳定，因为最终奖励是局部动作质量的弱代理。\[Wan25y\] 提出信息增益，因为最终结果奖励太常崩塌，但表 3 显示，单独信息增益不够，必须由结果奖励锚定。\[Hua26d\] 加入交错 SQL 反馈和塑形奖励，但其消融显示，一旦主要脚手架到位，一些奖励组件之间存在大量冗余。**推断。** 该领域已经越过“智能体是否需要更稠密反馈”的问题。开放问题是哪些中间信号与后续成功因果对齐，哪些只是制造细粒度监督的表象 \[Shi24c, Son24, Gao25c, Wan25y, Li25ae, Li26r\]。

### Exploration and optimization stability are still in tension

### 探索与优化稳定性仍然存在张力

A second deep fault line is that better exploration often destabilizes training, while stronger stabilization often suppresses exactly the behavior that long horizon agents need. \[Xu25k\] formalizes this as shared-parameter entropy coupling. Because the same policy parameters govern early and late turns, entropy control at one point spills into the rest of the trajectory, creating cascade failure. Their EPO-Decay ablation is especially revealing because the intuitive fix of stronger early exploration and later exploitation fails precisely due to that coupling. \[Don25d\] and \[Don25c\] surface the same issue empirically in tool-using agents. Both papers show entropy spikes after tool feedback, branch concentration on a few trajectories, and failure of clipping based baselines to preserve useful high-uncertainty behavior. \[Wan25ad\] then shows a related instability in long horizon RL, where confident correct actions can receive weak updates while uncertain actions dominate gradients and trigger policy collapse.

第二条深层断裂线是，更好的探索常会扰乱训练，而更强的稳定化又常会压制长时域智能体正需要的行为。\[Xu25k\] 将其形式化为共享参数熵耦合。由于同一组策略参数控制早期和后期轮次，某一点的熵控制会溢出到轨迹其他部分，造成级联失败。其 EPO-Decay 消融尤其有启发性，因为“早期更强探索、后期利用”这一直觉修复方案恰因该耦合而失败。\[Don25d\] 与 \[Don25c\] 在工具使用智能体中经验性地呈现相同问题。两篇论文都显示，工具反馈后会出现熵尖峰，分支集中到少数轨迹上，基于裁剪的基线无法保留有用的高不确定性行为。\[Wan25ad\] 随后显示长时域强化学习中的相关不稳定性：有把握的正确动作可能得到弱更新，而不确定动作主导梯度并触发策略崩塌。

Several papers also show that classic RL fixes do not transfer cleanly. \[Li25ae\] reports abrupt GRPO crashes in WebShop and Sokoban, and standard tweaks like removing KL or changing reward normalization do not reliably solve it. \[Che25af\] finds that using a learned value function with ordinary GAE settings can diverge in long horizon agent training. \[Xi25c\] shows that simply starting with long interaction horizons causes reward collapse, while progressive horizon scaling is much more stable. \[Gol25\] exposes a quieter version of the same problem in software engineering, where decoding choices such as top k and min p during training can create distribution mismatch severe enough to collapse DAPO. **Inference.** Exploration for agents is no longer just a search problem. It is a distribution-control problem in which context growth, tool feedback, entropy dynamics, and rollout policy all interact in ways that single-turn RL theory only weakly captures \[Xu25k, Don25d, Don25c, Wan25ad, Li25ae, Gol25\].

多篇论文还显示，经典强化学习修复方案无法干净迁移。\[Li25ae\] 报告 WebShop 和 Sokoban 中出现突然的 GRPO 崩溃，移除 KL 或改变奖励归一化等标准调整不能可靠解决。\[Che25af\] 发现，在长时域智能体训练中，用普通 GAE 设置学习价值函数可能发散。\[Xi25c\] 显示，直接从长交互时域开始会造成奖励崩塌，而渐进式时域扩展稳定得多。\[Gol25\] 在软件工程中暴露了同一问题的更安静版本：训练期间 top k 和 min p 等解码选择会制造严重到使 DAPO 崩塌的分布错配。**推断。** 智能体探索已不只是搜索问题，而是分布控制问题，其中上下文增长、工具反馈、熵动态和采样轨迹策略以单轮强化学习理论难以充分捕捉的方式相互作用 \[Xu25k, Don25d, Don25c, Wan25ad, Li25ae, Gol25\]。

### Generalization gains are real but still mostly local

### 泛化增益是真实的，但仍主要是局部的

Many papers report large average gains, but the strongest gains often stay close to the training distribution. \[Pap25b\] is unusually clear about the mismatch: offline action accuracy and online task success diverge sharply, and the final online-refined model loses offline accuracy while gaining control competence. \[Gan25b\] improves web agents through structured exploration, yet performance on Online-Mind2Web remains very low, which exposes how far synthetic data on a few benchmark domains still is from open web generalization. \[Gu26b\] provides the cleanest decomposition in mobile RL. Success gains are large for unseen instances, smaller for unseen templates, and much smaller for unseen apps. That pattern suggests current policies learn interaction habits and local skill fragments more readily than abstract task structure.

许多论文报告了很大的平均增益，但最强增益常停留在训练分布附近。\[Pap25b\] 对这种错配异常清楚：离线动作准确率和在线任务成功率急剧分离，最终在线精炼模型在获得控制能力的同时损失离线准确率。\[Gan25b\] 通过结构化探索改进网页智能体，但在 Online-Mind2Web 上性能仍很低，这暴露出少数基准领域上的合成数据距离开放网页泛化仍有多远。\[Gu26b\] 在移动端强化学习中提供了最清晰分解。未见实例上的成功增益很大，未见模板上较小，未见应用上小得多。这个模式提示，当前策略更容易学习交互习惯和局部技能片段，而不是抽象任务结构。

Even papers designed for broad coverage show silent scope narrowing. \[Xu24\] scales tutorial-based synthesis across eleven categories, but also acknowledges tutorial expiration and dynamic website changes as persistent failure sources. \[Wei25\] beats strong baselines on LiveWebBench, yet the method still depends on fixed action sets, binary outcome rewards, and text-only HTML observations. \[Lu25f\] nearly doubles in-domain success on OSWorld Hard but improves out-of-domain performance only marginally. \[Zha25an\] reports that reinforcement fine-tuning helps on some GUI benchmarks and gives limited or even slightly negative returns on others once the SFT base is already strong. **Inference.** Current experience transformation methods mostly learn how to do more reliably what the training ecology already exposes. They are much weaker at extracting interface invariant procedural knowledge that transfers across websites, apps, and task families \[Pap25b, Gan25b, Gu26b, Lu25f, Zha25an\].

即便为广覆盖设计的论文也显示出隐性范围收窄。\[Xu24\] 将基于教程的合成扩展到十一个类别，但也承认教程过期和动态网站变化是持续失败来源。\[Wei25\] 在 LiveWebBench 上击败强基线，但该方法仍依赖固定动作集合、二元结果奖励和纯文本 HTML 观察。\[Lu25f\] 几乎将 OSWorld Hard 上的领域内成功率翻倍，但领域外性能只略有提升。\[Zha25an\] 报告称，强化微调在一些图形界面基准上有帮助，但当监督微调基础已经很强时，在其他基准上收益有限，甚至略为负。**推断。** 当前经验转化方法大多学习如何更可靠地完成训练生态已经暴露的事情。它们在抽取跨网站、应用和任务族迁移的界面不变程序性知识方面弱得多 \[Pap25b, Gan25b, Gu26b, Lu25f, Zha25an\]。

### Reward design and evaluation still flatter current methods

### 奖励设计和评估仍会美化现有方法

A large share of the literature depends on reward and evaluation choices that are reasonable but convenience-driven. \[Pah25\] uses an LLM verifier with 81 percent agreement with human judgments, which is useful but not strong enough to treat the accepted trajectories as clean labels. \[Liu25z\] shows that web element preference optimization can work well once the correct candidate survives pruning, but the teacher-forcing row in Table 2 reveals that retrieval coverage, not preference learning itself, is often the real bottleneck. \[Gu26b\] is blunt about the danger of LLM-as-judge rewards in mobile RL: Appendix G shows false positives that push the policy in a misleading direction. \[Hua26d\] depends on a white-box interactive SQL environment and shaped auxiliary rewards, which is powerful for research but harder to carry into production settings.

大量文献依赖合理但由便利性驱动的奖励和评估选择。\[Pah25\] 使用与人类判断一致率为 81% 的大型语言模型验证器，这很有用，但还不足以把被接收轨迹视为干净标签。\[Liu25z\] 显示，一旦正确候选在剪枝后保留下来，网页元素偏好优化可以很好工作，但表 2 中的教师强制行揭示，真正瓶颈常是检索覆盖，而不是偏好学习本身。\[Gu26b\] 直白指出移动端强化学习中“以大型语言模型作裁判”的危险：附录 G 显示假阳性会把策略推向误导方向。\[Hua26d\] 依赖白盒交互式 SQL 环境和塑形辅助奖励，这对研究很有力，但更难带入生产设置。

The same issue appears as benchmark curation. \[Pan24\] required large manual effort to create reproducible software environments and filtered down to validated instances from only eleven repositories. \[Lu25f\] trains on a hand-picked valuable subset of OSWorld tasks where a baseline can already succeed at least once. \[Pap25b\] removes unsupported AndroidWorld task types. \[Pah25\] drops inaccessible websites from live evaluation. None of these choices is unreasonable, but together they show that many gains are conditional on pre-cleaned slices of the problem. **Inference.** The field still measures whether a method can exploit a tractable evaluation scaffold more often than it measures whether the transformed experience is robust under interface drift, ambiguous goals, or incomplete observability \[Pah25, Pan24, Lu25f, Gu26b, Hua26d\].

同一问题也表现为基准策展。\[Pan24\] 需要大量人工工作来创建可复现软件环境，并从仅十一个仓库中过滤出已验证实例。\[Lu25f\] 在手工挑选的 OSWorld 任务有价值子集上训练，其中基线至少已经成功过一次。\[Pap25b\] 移除不受支持的 AndroidWorld 任务类型。\[Pah25\] 从实时评估中剔除无法访问的网站。这些选择都并非不合理，但合在一起显示，许多增益以预清洗的问题切片为条件。**推断。** 该领域仍更常测量一种方法能否利用可处理的评估脚手架，而不是测量转化经验在界面漂移、含混目标或不完整可观察性下是否鲁棒 \[Pah25, Pan24, Lu25f, Gu26b, Hua26d\]。

### Synthetic experience scales, but quality control remains the real bottleneck

### 合成经验可扩展，但质量控制仍是真正瓶颈

One of the clearest cross-paper findings is that the raw volume of synthetic or self-generated experience is no longer the main barrier. The barrier is extracting a high-quality subset without discarding the very diversity that makes experience useful. \[Zen23d\] reports that some tasks contribute usable trajectories at rates below one percent after filtering. \[Mur24b\] shows that unguided web exploration creates many easy and medium demonstrations but relatively few truly hard workflows. \[Xu24\] turns tutorials into interactive trajectories at scale, but the replay phase is expensive and failures arise from outdated or non-replayable instructions. \[Pah25\] surfaces grounding errors, summarization hallucinations, and website unresponsiveness as the main synthesis bottlenecks. \[Lai25d\] extracts successful sub-trajectories from partially successful Android episodes, which is clever precisely because full trajectories are too noisy to use as-is.

最清晰的跨论文发现之一是，合成或自生成经验的原始数量已不再是主要障碍。障碍在于抽取高质量子集，同时不丢弃使经验有用的多样性。\[Zen23d\] 报告称，一些任务经过过滤后贡献可用轨迹的比例低于 1%。\[Mur24b\] 显示，无引导网页探索会创造许多简单和中等示范，但真正困难的工作流相对较少。\[Xu24\] 大规模地把教程转化为交互轨迹，但回放阶段昂贵，失败来自过时或不可回放的指令。\[Pah25\] 揭示 grounding 错误、摘要幻觉和网站无响应是主要合成瓶颈。\[Lai25d\] 从部分成功的 Android 回合中抽取成功子轨迹，这很巧妙，原因正是完整轨迹噪声太大，不能原样使用。

What is striking is how often the accepted data still contains hidden defects. \[Pat24\] fine-tunes on plausible trajectories that are successful much more often than random rollouts, but many of those plausible traces are still failures. \[Pap25b\] finds that technically successful RL trajectories can include wrong actions that need extra filtering before reuse. \[Pan24\] shows that the source of verifier training data matters strongly, with mixed on-policy and off-policy data beating either alone. \[Che24k\] demonstrates that failed inference tree branches contain real signal, but also that scaling preference data too far can hurt generalization. **Inference.** Experience generation has become a weak supervision problem. The key missing ingredient is not more trajectories, but stronger methods for preserving informative mistakes while excluding misleading success-like artifacts \[Zen23d, Pat24, Pap25b, Pan24, Che24k\].

值得关注的是，被接收数据仍常含有隐藏缺陷。\[Pat24\] 在看似合理的轨迹上微调，这些轨迹成功率远高于随机采样轨迹，但其中许多看似合理的轨迹仍是失败。\[Pap25b\] 发现，技术上成功的强化学习轨迹可能包含错误动作，复用前需要额外过滤。\[Pan24\] 显示，验证器训练数据来源很重要，混合在策略和离策略数据优于任一单独来源。\[Che24k\] 证明，失败推理树分支包含真实信号，但也显示将偏好数据扩展过远会伤害泛化。**推断。** 经验生成已经变成弱监督问题。关键缺失成分不是更多轨迹，而是更强的方法，用来保留有信息量的错误，同时排除误导性的成功样产物 \[Zen23d, Pat24, Pap25b, Pan24, Che24k\]。

### Grounding and representation losses still block robust reuse

### Grounding 与表示损失仍阻碍鲁棒复用

Many agent failures are not primarily about high-level planning. They are about losing the right state when experience is represented in a convenient but lossy form. \[Pap25b\] shows that small but critical GUI actions such as clearing a text field can be absent from human data and therefore invisible to the learned policy. \[Xu24\] reports a large remaining gap between text grounding and icon or widget grounding, and tutorial replay can fail when websites change in ways that invalidate previously grounded instructions. \[Zha24s\] gives a clean embodied version of the same issue: RL can improve decision making, but perception failures still dominate on tasks like card reasoning, where the chain of thought is logically fine once the visual input is misread. \[Szo23\] similarly shows that embodied agents often succeed without truly checking conditional state, so apparent reasoning competence can ride on accidental environmental regularities.

许多智能体失败主要不是高层规划问题，而是当经验以便利但有损形式表示时丢失了正确状态。\[Pap25b\] 显示，清空文本字段等小但关键的图形界面动作可能不存在于人类数据中，因此对学习策略不可见。\[Xu24\] 报告文本 grounding 与图标或控件 grounding 之间仍有很大差距，当网站变化使先前已 grounding 的指令失效时，教程回放会失败。\[Zha24s\] 给出了同一问题的清晰具身版本：强化学习可以改善决策，但在卡片推理等任务中，感知失败仍占主导，一旦视觉输入被误读，思维链在逻辑上再好也无济于事。\[Szo23\] 同样显示，具身智能体常常在没有真正检查条件状态的情况下成功，因此表面推理能力可能依赖偶然环境规律。

The problem gets worse in long horizon embodied and GUI settings. \[Hu26e\] shows that long navigation training quickly runs into memory and KV cache limits because the full visual history is too large to keep cheaply. \[Pap25c\] and \[Lai25d\] both document tasks that fail because agents cannot remember earlier observations or because the text-only UI view omits crucial spatial or visual cues. \[Luo25b\] finds that image resolution materially changes RL outcomes, which means perception quality is not just an upstream module issue. It changes the shape of the learning signal itself. **Inference.** Much current experience transformation is still performed after the environment has already been compressed into partial text views. That makes some downstream failures irrecoverable because the missing signal was never represented in the stored experience to begin with \[Pap25b, Xu24, Zha24s, Pap25c, Hu26e, Luo25b\].

这个问题在长时域具身和图形界面设置中更严重。\[Hu26e\] 显示，长导航训练很快遇到记忆和 KV cache 限制，因为完整视觉历史太大，无法廉价保留。\[Pap25c\] 与 \[Lai25d\] 都记录了因智能体无法记住早先观察，或因纯文本 UI 视图遗漏关键空间或视觉线索而失败的任务。\[Luo25b\] 发现，图像分辨率会实质改变强化学习结果，这意味着感知质量不只是上游模块问题。它会改变学习信号本身的形状。**推断。** 许多当前经验转化仍发生在环境已经被压缩成部分文本视图之后。这使一些下游失败不可恢复，因为缺失信号一开始就没有被表示在存储经验中 \[Pap25b, Xu24, Zha24s, Pap25c, Hu26e, Luo25b\]。

### The systems burden now shapes the science

### 系统负担如今塑造研究本身

A final cross-cutting challenge is that online learning quality is now heavily constrained by infrastructure. \[Pan24\] quantifies the cost of making software tasks executable, with hundreds of human hours and large CPU budgets just to build a trainable benchmark. \[Gol25\] filters more than half of the candidate software tasks to ensure stable training and deterministic tests. \[Zha25ag\] frames multi-turn multi-task RL as a systems problem of asynchronous generation and training because synchronous pipelines waste large amounts of compute on idle waiting. \[Gu26b\] shows that rollout collection takes over 95 percent of runtime in mobile RL and that a single environment crash can poison a whole training batch. \[Pap25c\] reports four to five second environment steps in AndroidWorld, which radically changes what kinds of RL algorithms are practical.

最后一个横向挑战是，在线学习质量如今受到基础设施的强约束。\[Pan24\] 量化了使软件任务可执行的成本，仅构建可训练基准就需要数百个人工小时和大量 CPU 预算。\[Gol25\] 过滤超过一半候选软件任务，以确保稳定训练和确定性测试。\[Zha25ag\] 将多轮多任务强化学习表述为异步生成与训练的系统问题，因为同步流水线会在空闲等待上浪费大量计算。\[Gu26b\] 显示，在移动端强化学习中，采样轨迹收集占运行时间 95% 以上，单个环境崩溃会污染整个训练批次。\[Pap25c\] 报告 AndroidWorld 中环境步长为 4 到 5 秒，这会彻底改变哪些强化学习算法具有实践可行性。

These constraints quietly shape method design. \[Lu25f\] uses experience replay because successful GUI trajectories are too expensive to waste. \[Hua26d\] and \[Li26r\] both limit horizon and rely on interactive but controlled SQL environments so that training remains tractable. \[Don25d\] and \[Don25c\] explicitly optimize tool-call budgets because unrestricted branching would be financially prohibitive. **Inference.** In this area, the engineering substrate is no longer a neutral implementation detail. It actively determines what counts as feasible experience, which reward signals can be computed, how much exploration is tolerated, and even which research questions get asked \[Pan24, Gol25, Zha25ag, Gu26b, Pap25c, Don25d\].

这些约束隐性塑造方法设计。\[Lu25f\] 使用经验回放，因为成功图形界面轨迹太昂贵，不能浪费。\[Hua26d\] 与 \[Li26r\] 都限制时域，并依赖交互式但受控的 SQL 环境，使训练保持可处理。\[Don25d\] 与 \[Don25c\] 明确优化工具调用预算，因为无限制分支在经济上不可承受。**推断。** 在这一领域，工程基底已不再是中性实现细节。它主动决定什么算可行经验、哪些奖励信号可被计算、多少探索可被容忍，甚至哪些研究问题会被提出 \[Pan24, Gol25, Zha25ag, Gu26b, Pap25c, Don25d\]。

## Future directions

## 未来方向

| Direction | What concrete progress would look like | Core support |
|:---|:---|:---|
| Failure-native learning pipelines | Agents should learn from partial success, repaired traces, and structured failure diagnoses rather than only from filtered successes | \[Lai25d\], \[Son24\], \[Li26r\], \[Che24k\], \[Zha25ao\] |
| Multi-scale credit assignment | Future methods should combine trajectory, turn, and step signals with explicit tests of which level adds unique value | \[Gao25c\], \[Fen25c\], \[Li25ae\], \[Wan25y\], \[Hua26d\] |
| Horizon-adaptive exploration control | Exploration budgets should vary by turn, uncertainty, and task phase rather than being fixed for whole trajectories | \[Xu25k\], \[Hu26e\], \[Xi25c\], \[Don25d\], \[Don25c\] |
| Better use of offline and off-policy experience | Replay, aggregation, and successful transition reuse should become first-class training objects rather than side modules | \[Lu25f\], \[Pap25c\], \[Li26r\], \[Gol25\], \[Pan24\] |
| Environment-grounded reward models and evaluators | Binary success should give way to denser but still verifiable feedback tied to state changes, action effects, and partial progress | \[Wei25\], \[Hua26d\], \[Li26r\], \[Gu26b\], \[Pah25\] |
| Representation-rich experience stores | Policies should learn from observations that preserve visual, spatial, and temporal detail instead of only compressed text snapshots | \[Pap25b\], \[Xu24\], \[Zha24s\], \[Hu26e\], \[Pap25c\] |
| Transfer-oriented benchmarks and training | Progress should be measured on unseen apps, unseen sites, and novel task recompositions, not just nearby held-out instances | \[Gan25b\], \[Gu26b\], \[Lu25f\], \[Pap25b\], \[Zha25an\] |
| Scalable real-world training systems | Asynchronous rollouts, crash-tolerant execution, and cheaper policy updates should be treated as core research contributions | \[Zha25ag\], \[Gu26b\], \[Gol25\], \[Pan24\], \[Pap25c\] |

| 方向 | 具体进展形态 | 核心依据 |
|:---|:---|:---|
| 失败原生学习流水线 | 智能体应从部分成功、修复轨迹和结构化失败诊断中学习，而不只从过滤后的成功中学习 | \[Lai25d\], \[Son24\], \[Li26r\], \[Che24k\], \[Zha25ao\] |
| 多尺度信用分配 | 未来方法应结合轨迹、轮次和步骤信号，并显式测试哪个层级增加了独特价值 | \[Gao25c\], \[Fen25c\], \[Li25ae\], \[Wan25y\], \[Hua26d\] |
| 时域自适应探索控制 | 探索预算应随轮次、不确定性和任务阶段变化，而非固定于整条轨迹 | \[Xu25k\], \[Hu26e\], \[Xi25c\], \[Don25d\], \[Don25c\] |
| 更有意识地使用离线与离策略经验 | 回放、聚合和成功转移复用应成为一等训练对象，而非侧模块 | \[Lu25f\], \[Pap25c\], \[Li26r\], \[Gol25\], \[Pan24\] |
| 有环境根基的奖励模型与评估器 | 二元成功应让位于更稠密但仍可验证的反馈，并与状态变化、动作效果和部分进展绑定 | \[Wei25\], \[Hua26d\], \[Li26r\], \[Gu26b\], \[Pah25\] |
| 表示丰富的经验存储 | 策略应从保留视觉、空间和时间细节的观察中学习，而不只是从压缩文本快照中学习 | \[Pap25b\], \[Xu24\], \[Zha24s\], \[Hu26e\], \[Pap25c\] |
| 面向迁移的基准与训练 | 进展应在未见应用、未见站点和新任务重组上测量，而不只是邻近留出实例 | \[Gan25b\], \[Gu26b\], \[Lu25f\], \[Pap25b\], \[Zha25an\] |
| 可扩展真实世界训练系统 | 异步采样轨迹、容错执行和更廉价的策略更新应被视为核心研究贡献 | \[Zha25ag\], \[Gu26b\], \[Gol25\], \[Pan24\], \[Pap25c\] |

### Failure-native pipelines should become the default

### 失败原生流水线应成为默认选择

The literature repeatedly shows that discarding failed interaction is wasteful, but it also shows that naïvely keeping failure is toxic. That points toward a more structured future pipeline rather than a simple keep or discard choice. \[Lai25d\] already moves in this direction by extracting successful sub-trajectories from partially failed Android episodes. \[Son24\] shows that preference learning benefits from exploration failures, but also that step-wise use of failure is unstable when the local quality estimate is weak. \[Che24k\] goes further by mining failed inference tree branches, showing that failure-to-failure distinctions can carry signal that expert-only cloning misses. \[Li26r\] turns final SQL failure cases into partial micro-rewards by column-set matching and uses stagnation-sensitive aggregation to escape loops. \[Zha25ao\] makes meta-reasoning itself verifiable, rewarding agents for discovering new states and reducing repetitive action patterns rather than only for final success.

文献反复显示，丢弃失败交互是浪费，但也显示朴素保留失败是有毒的。这指向更结构化的未来流水线，而不是简单保留或丢弃。\[Lai25d\] 已通过从部分失败的 Android 回合中抽取成功子轨迹朝这个方向推进。\[Son24\] 显示，偏好学习受益于探索失败，但也显示，当局部质量估计较弱时，逐步使用失败是不稳定的。\[Che24k\] 进一步挖掘失败推理树分支，显示失败与失败之间的差异可以携带专家克隆遗漏的信号。\[Li26r\] 通过列集合匹配将最终 SQL 失败案例转化为部分微奖励，并使用停滞敏感聚合逃离循环。\[Zha25ao\] 使元推理本身可验证，奖励智能体发现新状态并减少重复动作模式，而不是只奖励最终成功。

Concrete progress here would mean representing failure as an object with internal structure: what went wrong, at what turn, under what observed state, and whether a later repair succeeded. A strong next paper would compare at least four variants on the same tasks: success-only training, raw failure inclusion, structured failure extraction, and counterfactual repair. It should measure not only end-task success but also loop rate, recovery success, and whether failure-aware training improves performance on unseen tasks rather than only seen ones. That would directly test whether failure is becoming reusable knowledge or merely a noisy contrast set.

这里的具体进展意味着把失败表示为具有内部结构的对象：哪里出错、在哪一轮、处于什么观察状态，以及后续修复是否成功。下一篇强论文应在相同任务上至少比较四个变体：仅成功训练、纳入原始失败、结构化失败抽取和反事实修复。它不应只测量最终任务成功，也应测量循环率、恢复成功率，以及失败感知训练是否改善未见任务而不只是已见任务上的表现。这将直接测试失败是在变成可复用知识，还是只是带噪对比集。

### Multi-scale credit assignment should replace single-granularity objectives

### 多尺度信用分配应替代单粒度目标

Several papers already point toward the same conclusion from different angles. \[Gao25c\] shows that trajectory, group, and step-level preference signals each solve a different weakness of the others. \[Fen25c\] finds a similar complementarity in RL with episode-relative and state-anchored step-relative advantages. \[Li25ae\] argues that turn-level MDPs are a better fit for agentic interaction than token MDPs, especially when environment feedback arrives in blocks between responses. \[Wan25y\] derives intermediate rewards from belief change rather than hand-coded step labels. \[Hua26d\] uses interleaved SQL feedback to transform a single-pass generation problem into a short interactive control loop.

多篇论文已经从不同角度指向同一结论。\[Gao25c\] 显示，轨迹级、组级和步骤级偏好信号分别解决其他信号的不同弱点。\[Fen25c\] 在强化学习中发现类似互补性，使用 episode 相对优势和状态锚定的步骤相对优势。\[Li25ae\] 认为，轮次级马尔可夫决策过程比 token 级马尔可夫决策过程更适合智能体交互，尤其是当环境反馈以块状形式在回复之间到来时。\[Wan25y\] 从信念变化而不是手工步骤标签中导出中间奖励。\[Hua26d\] 使用交错 SQL 反馈，将单遍生成问题转化为短交互控制循环。

The promising direction is not to choose one granularity once and for all. It is to learn which granularity is reliable for which regime. Early exploration may benefit from coarse group level credit. Late execution may need step or turn-specific shaping. A useful benchmark for this direction would report what each supervision level contributes after controlling for the others. It should also include failure cases where denser supervision hurts, because several current papers already imply that naive process rewards can be anti-causal or redundant. Progress would look like agents whose learning signals become finer only when the state and task support that precision.

有前景的方向不是一次性选择某一种粒度，而是学习哪种粒度在哪种机制下可靠。早期探索可能受益于粗组级信用。后期执行可能需要步骤或轮次特定塑形。这个方向的有用基准应报告在控制其他层级后，每个监督层级贡献了什么。它还应包含更稠密监督造成损害的失败案例，因为已有多篇论文暗示，朴素过程奖励可能是反因果的或冗余的。进展可以表现为：智能体的学习信号只在状态和任务支持这种精度时才变得更细。

### Horizon-adaptive exploration control is likely more important than stronger generic entropy bonuses

### 时域自适应探索控制可能比更强通用熵奖励更重要

The recent entropy papers suggest that long horizon agents need exploration policies that are phase-aware rather than uniformly noisy. \[Xu25k\] shows that independent per-turn weighting does not work once the same parameters govern the whole dialogue, but its entropy corridor idea still points toward constrained exploration instead of fixed regularization. \[Hu26e\] shows that advantage estimation should respect where in the trajectory the agent is, because early navigation and late goal acquisition have different variance structures. \[Xi25c\] demonstrates that gradually increasing interaction rounds is far more stable than training with long horizons from the start. \[Don25d\] and \[Don25c\] both show that branching should focus on the few turns where uncertainty spikes after tool feedback, not be spent evenly across the whole tree.

近期熵相关论文提示，长时域智能体需要阶段感知探索策略，而不是均匀加噪。\[Xu25k\] 显示，一旦相同参数控制整个对话，独立的逐轮加权就不起作用，但其熵走廊想法仍指向受约束探索，而非固定正则化。\[Hu26e\] 显示，优势估计应尊重智能体处在轨迹中的位置，因为早期导航和后期目标获取具有不同方差结构。\[Xi25c\] 证明，逐步增加交互轮数远比一开始就用长时域训练稳定。\[Don25d\] 与 \[Don25c\] 都显示，分支应聚焦在工具反馈后不确定性激增的少数轮次，而不是均匀花在整棵树上。

Concrete progress would look like adaptive exploration schedules keyed to observed uncertainty, trajectory depth, and branch utility. Verification should measure more than final success. It should report path diversity, repeated action rate, tool-call efficiency, and how often exploration discovers qualitatively new strategies rather than merely more samples of the same one. A particularly strong contribution would show that the same adaptive rule helps in at least two domains such as web navigation and software engineering, where the visible action spaces differ but the uncertainty dynamics share the same long-horizon structure.

具体进展可以表现为根据观察到的不确定性、轨迹深度和分支效用设定的自适应探索日程。验证不应只测量最终成功。它应报告路径多样性、重复动作率、工具调用效率，以及探索发现质性新策略的频率，而不只是同一策略的更多样本。特别强的贡献会显示，同一自适应规则至少在网页导航和软件工程等两个领域有帮助；这些领域的可见动作空间不同，但不确定性动态共享相同长时域结构。

### Offline and off-policy experience should be used more deliberately, not just as a fallback

### 离线与离策略经验应被更有意识地使用，而不只是作为回退

The most practical papers increasingly win by reusing old experience better. \[Lu25f\] injects successful trajectories from a replay buffer whenever sparse reward groups would otherwise produce no learning signal. \[Pap25c\] shows that successful transition replay is central to sample-efficient off-policy RL on slow mobile environments. \[Li26r\] aggregates trajectories across SQL rollouts to combat limit cycles and preserve partial progress. \[Gol25\] highlights how filtering long trajectories can accidentally remove the very negative evidence needed to learn how to break loops. \[Pan24\] shows that verifier performance improves most when on-policy and off-policy experiences are mixed rather than treated as separate sources.

最实用的论文越来越多地通过更好复用旧经验取胜。\[Lu25f\] 在稀疏奖励组本来不会产生学习信号时，从回放缓冲区注入成功轨迹。\[Pap25c\] 显示，在缓慢移动端环境中，成功转移回放是样本高效离策略强化学习的核心。\[Li26r\] 跨 SQL 采样轨迹聚合轨迹，以对抗极限循环并保留部分进展。\[Gol25\] 强调，过滤长轨迹可能意外移除学习如何打破循环所需的负面证据。\[Pan24\] 显示，当在策略与离策略经验混合，而不是把二者当作分离来源时，验证器表现提升最大。

A promising direction is to treat the replay buffer as a structured memory of learning opportunities rather than a bag of transitions. Buffer entries could be tagged by failure family, novelty, uncertainty, or evidence of recovery. That would make it possible to ask which historical experiences are worth replaying for which current policy weaknesses. Progress here would be verified by sample efficiency under fixed rollout budgets and by robustness when rollout generation is deliberately throttled. This matters because in many real agents the cost bottleneck is not optimization but experience collection.

一个有前景的方向是把回放缓冲区视为学习机会的结构化记忆，而不是转移袋。缓冲区条目可以按失败族、新颖性、不确定性或恢复证据标注。这样就能询问哪些历史经验值得为当前策略弱点回放。这里的进展可通过固定采样轨迹预算下的样本效率，以及有意限制采样轨迹生成时的鲁棒性来验证。这很重要，因为在许多真实智能体中，成本瓶颈不是优化，而是经验收集。

### Reward models and evaluators need to become more grounded without giving up verifiability

### 奖励模型和评估器需要更有根基，同时不放弃可验证性

Most current work still sits between two imperfect poles: cheap binary rewards that are too sparse and richer evaluators that are expensive or unreliable. \[Wei25\] shows that binary rule-based rewards are robust but too coarse for nuanced web learning. \[Hua26d\] and \[Li26r\] show that interleaved and partial rewards can help materially in SQL agents. \[Gu26b\] warns that LLM-as-judge signals can be over-optimistic enough to misdirect optimization. \[Pah25\] documents only moderate agreement between automated trajectory verification and human judgment. Taken together, these papers suggest that the next step is not simply richer rewards. It is richer rewards whose grounding is still externally checkable.

多数当前工作仍处在两个不完美端点之间：廉价但过稀疏的二元奖励，以及更丰富但昂贵或不可靠的评估器。\[Wei25\] 显示，基于规则的二元奖励很鲁棒，但对细微网页学习来说太粗。\[Hua26d\] 与 \[Li26r\] 显示，交错奖励和部分奖励可以实质帮助 SQL 智能体。\[Gu26b\] 警告称，以大型语言模型为裁判的信号可能过度乐观，足以误导优化。\[Pah25\] 记录了自动轨迹验证与人类判断之间只有中等一致性。合在一起，这些论文提示，下一步并非简单增加奖励丰富度，而是让更丰富奖励的 grounding 仍可由外部检查。

Concrete progress would look like action-effect or state-change rewards that can be verified by the environment without requiring full task success. In web and GUI settings, this might mean rewarding confirmed element state changes, validated navigation progress, or successful recovery after a wrong click. In software and SQL tasks, it might mean partial execution consistency, patch validity, or schema-correct intermediate plans. The right evaluation would compare reward informativeness against judge reliability and compute cost. A method that improves learning but only by introducing an opaque or expensive evaluator would not yet solve the broader field problem.

具体进展可以表现为动作效果或状态变化奖励，它们能由环境验证，而不要求完整任务成功。在网页和图形界面设置中，这可能意味着奖励已确认的元素状态变化、已验证的导航进展，或错误点击后的成功恢复。在软件和 SQL 任务中，这可能意味着部分执行一致性、补丁有效性或模式正确的中间计划。合适评估应比较奖励信息量、裁判器可靠性和计算成本。若一种方法只能通过引入不透明或昂贵评估器来改善学习，它仍未解决更宽的领域问题。

### Experience representations should preserve more of the original environment signal

### 经验表示应保留更多原始环境信号

Several failures in this literature are traceable to what got thrown away before learning even began. \[Pap25b\] and \[Pap25c\] show that text-only views of mobile interfaces miss critical visual and stateful cues. \[Xu24\] highlights the remaining weakness in icon and widget grounding even after large-scale trajectory synthesis. \[Zha24s\] shows that reasoning improvements cannot compensate for perception failures when visual state is misread. \[Hu26e\] makes the long-horizon version explicit: preserving full visual history is too expensive, but compressing it too aggressively loses exactly the signal needed for navigation. These papers motivate a shift from text-first experience transformation toward representation-rich trajectories that preserve temporal and spatial structure longer.

这类文献中的若干失败可追溯到学习开始前就被丢弃的内容。\[Pap25b\] 与 \[Pap25c\] 显示，移动界面的纯文本视图会漏掉关键视觉和状态线索。\[Xu24\] 强调，即便经过大规模轨迹合成，图标和控件 grounding 仍是弱点。\[Zha24s\] 显示，当视觉状态被误读时，推理改进无法弥补感知失败。\[Hu26e\] 明确给出长时域版本：保留完整视觉历史太昂贵，但过度压缩又会丢失导航所需信号。这些论文推动一种转变：从文本优先的经验转化，转向能更久保留时间和空间结构的表示丰富轨迹。

Concrete progress would mean comparing the same training objective under multiple observation carriers, such as UI tree only, screenshot only, fused screenshot and tree, and compact state summaries learned from those sources. Verification should ask not only which representation gives higher average success, but which one remains robust under interface perturbations, small targets, or tasks requiring memory of earlier visual details. A strong result here would matter beyond one benchmark because representation loss is a shared bottleneck across web, mobile, GUI, and embodied agents.

具体进展意味着在多种观察载体下比较同一训练目标，例如仅 UI 树、仅截图、融合截图和树，以及从这些来源学习得到的紧凑状态摘要。验证不应只问哪种表示带来更高平均成功率，还应问哪种表示在界面扰动、小目标或需要记住早期视觉细节的任务下保持鲁棒。这里的强结果会超越单个基准，因为表示损失是网页、移动端、图形界面和具身智能体的共同瓶颈。

### Transfer-oriented training and evaluation should become the default standard

### 面向迁移的训练与评估应成为默认标准

The field now has enough evidence that held-out instances are too weak a test. \[Gan25b\] shows that synthetic web trajectories collected from a few domains do not carry far into truly live tasks. \[Gu26b\] gives a concrete benchmark hierarchy from unseen instance to unseen app and shows sharply decaying gains. \[Lu25f\] finds strong in-domain improvements with almost no out-of-domain movement. \[Pap25b\] and \[Zha25an\] both show that better online control does not imply broad transfer once app distributions shift. The literature therefore already contains the ingredients for a stronger benchmark agenda.

该领域现在已有足够证据表明，留出实例是过弱测试。\[Gan25b\] 显示，从少数领域收集的合成网页轨迹无法很好迁移到真正实时任务。\[Gu26b\] 给出了从未见实例到未见应用的具体基准层级，并显示增益急剧衰减。\[Lu25f\] 发现强领域内改进几乎没有带来领域外变化。\[Pap25b\] 与 \[Zha25an\] 都显示，一旦应用分布变化，更好的在线控制并不意味着广泛迁移。因此，文献已经包含构建更强基准议程的材料。

Progress would look like routine reporting across multiple transfer regimes: unseen instances, unseen templates, unseen applications or sites, and new compositions of known subskills. Training methods should also report where their data came from in that transfer hierarchy. A method trained on near-neighbor templates should not be described as solving open-world transfer. More ambitiously, future work could test whether one domain’s learned primitive such as search, file selection, or form filling transfers as a reusable skill into another domain. That would move the discussion from benchmark adaptation toward genuine experience reuse.

进展会表现为在多个迁移机制上常规报告：未见实例、未见模板、未见应用或站点，以及已知子技能的新组合。训练方法还应报告其数据在该迁移层级中的来源。基于近邻模板训练的方法不应被描述为解决开放世界迁移。更有雄心的未来工作可以测试，一个领域学到的搜索、文件选择或填表等基元是否能作为可复用技能迁移到另一领域。这会把讨论从基准适配推进到真正的经验复用。

### Real-world online learning systems deserve to be treated as core methodology

### 真实世界在线学习系统应被视为核心方法学

Finally, the systems layer needs to be elevated from appendix material to first-class research contribution. \[Zha25ag\] shows that asynchronous multi-task RL changes what scales at all. \[Gu26b\] shows that containerization and crash isolation are essential for mobile training. \[Gol25\] and \[Pan24\] demonstrate that environment curation, determinism filtering, and reproducible execution are preconditions for meaningful software agent learning. \[Pap25c\] makes clear that rollout latency alone can force a turn toward off-policy methods. These are not peripheral implementation details. They decide which experience transformation schemes are even testable.

最后，系统层需要从附录材料提升为一等研究贡献。\[Zha25ag\] 显示，异步多任务强化学习会改变什么东西能够扩展。\[Gu26b\] 显示，容器化和崩溃隔离对移动端训练是必要的。\[Gol25\] 与 \[Pan24\] 证明，环境策展、确定性过滤和可复现执行是有意义的软件智能体学习的前提。\[Pap25c\] 明确表明，仅采样轨迹延迟就能迫使方法转向离策略。这些不是边缘实现细节。它们决定哪些经验转化方案甚至可被测试。

Concrete progress would look like papers that report full training economics: rollout throughput, crash rate, synchronization waste, tool-call cost, and how these interact with learning curves. A particularly valuable direction would be systems that support continual policy improvement under real-world constraints such as asynchronous environments, stale states, and intermittent evaluator availability. The field will likely make larger practical gains from better execution substrates and replay-aware training loops than from another isolated RL loss if those substrates dramatically increase the amount of trustworthy interactive experience that can be collected per dollar and per hour.

具体进展可以表现为论文报告完整训练经济学：采样轨迹吞吐量、崩溃率、同步浪费、工具调用成本，以及这些因素如何与学习曲线相互作用。一个特别有价值的方向是，系统在异步环境、陈旧状态和评估器间歇可用等真实世界约束下支持持续策略改进。如果更好的执行基底和回放感知训练循环能大幅增加每美元、每小时可收集的可信交互经验量，那么该领域可能从中获得比另一个孤立强化学习损失更大的实践收益。

---

## References

\[Pat24\] A. Patel, M. Hofmarcher, C. Leoveanu-Condrei, M.-C. Dinu, C. Callison-Burch, and S. Hochreiter, “Large Language Models Can Self-Improve At Web Agent Tasks,” *ArXiv*, vol. abs/2405.20309, May 2024, doi: [10.48550/arXiv.2405.20309](https://doi.org/10.48550/arXiv.2405.20309).

\[Son24\] Y. Song, D. Yin, X. Yue, J. Huang, S. Li, and B. Y. Lin, “Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents,” *Annual Meeting of the Association for Computational Linguistics*, pp. 7584–7600, Mar. 2024, doi: [10.48550/arXiv.2403.02502](https://doi.org/10.48550/arXiv.2403.02502).

\[Da25\] J. Da, C. J. Wang, X. Deng, Y. Ma, N. Barhate, and S. M. Hendryx, “Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards,” *ArXiv*, vol. abs/2506.11425, Jun. 2025, doi: [10.48550/arXiv.2506.11425](https://doi.org/10.48550/arXiv.2506.11425).

\[Wei25\] Z. Wei *et al.*, “WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning,” *Conference on Empirical Methods in Natural Language Processing*, pp. 7909–7928, May 2025, doi: [10.48550/arXiv.2505.16421](https://doi.org/10.48550/arXiv.2505.16421).

\[Li25aa\] H. Li *et al.*, “SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning,” *ArXiv*, vol. abs/2509.09674, Sep. 2025, doi: [10.48550/arXiv.2509.09674](https://doi.org/10.48550/arXiv.2509.09674).

\[Pap25c\] G. Papoudakis, T. Coste, J. Hao, J. Wang, and K. Shao, “Succeed or Learn Slowly: Sample Efficient Off-Policy Reinforcement Learning for Mobile App Control,” *ArXiv*, vol. abs/2509.01720, Sep. 2025, doi: [10.48550/arXiv.2509.01720](https://doi.org/10.48550/arXiv.2509.01720).

\[Shi24c\] W. Shi, M. Yuan, J. Wu, Q. Wang, and F. Feng, “Direct Multi-Turn Preference Optimization for Language Agents,” *ArXiv*, vol. abs/2406.14868, Jun. 2024, doi: [10.48550/arXiv.2406.14868](https://doi.org/10.48550/arXiv.2406.14868).

\[Gao25c\] H. Gao *et al.*, “Solving the Granularity Mismatch: Hierarchical Preference Learning for Long-Horizon LLM Agents,” *ArXiv*, vol. abs/2510.03253, Sep. 2025, doi: [10.48550/arXiv.2510.03253](https://doi.org/10.48550/arXiv.2510.03253).

\[Zho24f\] Y. Zhou, A. Zanette, J. Pan, S. Levine, and A. Kumar, “ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL,” *International Conference on Machine Learning*, pp. 62178–62209, Feb. 2024, doi: [10.48550/arXiv.2402.19446](https://doi.org/10.48550/arXiv.2402.19446).

\[Fen25c\] L. Feng, Z. Xue, T. Liu, and B. An, “Group-in-Group Policy Optimization for LLM Agent Training,” *ArXiv*, vol. abs/2505.10978, May 2025, doi: [10.48550/arXiv.2505.10978](https://doi.org/10.48550/arXiv.2505.10978).

\[Li25ae\] J. Li, P. Zhou, R. Meng, M. P. Vadera, L. Li, and Y. Li, “Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs,” *ArXiv*, vol. abs/2512.17008, Dec. 2025, doi: [10.48550/arXiv.2512.17008](https://doi.org/10.48550/arXiv.2512.17008).

\[Li26r\] L. Li *et al.*, “SQL-ASTRA: Alleviating Sparse Feedback in Agentic SQL via Column-Set Matching and Trajectory Aggregation,” Mar. 17, 2026.

\[Xu25k\] W. Xu *et al.*, “EPO: Entropy-regularized Policy Optimization for LLM Agents Reinforcement Learning,” *ArXiv*, vol. abs/2509.22576, Sep. 2025, doi: [10.48550/arXiv.2509.22576](https://doi.org/10.48550/arXiv.2509.22576).

\[Don25d\] G. Dong *et al.*, “Agentic Reinforced Policy Optimization,” *ArXiv*, vol. abs/2507.19849, Jul. 2025, doi: [10.48550/arXiv.2507.19849](https://doi.org/10.48550/arXiv.2507.19849).

\[Don25c\] G. Dong *et al.*, “Agentic Entropy-Balanced Policy Optimization,” *ArXiv*, vol. abs/2510.14545, Oct. 2025, doi: [10.48550/arXiv.2510.14545](https://doi.org/10.48550/arXiv.2510.14545).

\[Wan25ad\] J. Wang *et al.*, “Harnessing Uncertainty: Entropy-Modulated Policy Gradients for Long-Horizon LLM Agents,” *ArXiv*, vol. abs/2509.09265, Sep. 2025, doi: [10.48550/arXiv.2509.09265](https://doi.org/10.48550/arXiv.2509.09265).

\[Xi25c\] Z. Xi *et al.*, “AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning,” *ArXiv*, vol. abs/2509.08755, Sep. 2025, doi: [10.48550/arXiv.2509.08755](https://doi.org/10.48550/arXiv.2509.08755).

\[Che25af\] K. Chen *et al.*, “Reinforcement Learning for Long-Horizon Interactive LLM Agents,” *ArXiv*, vol. abs/2502.01600, Feb. 2025, doi: [10.48550/arXiv.2502.01600](https://doi.org/10.48550/arXiv.2502.01600).

\[Pap25b\] G. Papoudakis, T. Coste, Z. Wu, J. Hao, J. Wang, and K. Shao, “AppVLM: A Lightweight Vision Language Model for Online App Control,” *ArXiv*, vol. abs/2502.06395, Feb. 2025, doi: [10.48550/arXiv.2502.06395](https://doi.org/10.48550/arXiv.2502.06395).

\[Gan25b\] A. Gandhi and G. Neubig, “Go-Browse: Training Web Agents with Structured Exploration,” *ArXiv*, vol. abs/2506.03533, Jun. 2025, doi: [10.48550/arXiv.2506.03533](https://doi.org/10.48550/arXiv.2506.03533).

\[Gu26b\] L. Gu *et al.*, “Generalization in Online Reinforcement Learning for Mobile Agents,” Mar. 08, 2026.

\[Lu25f\] F. Lu, Z. Zhong, S. Liu, C.-W. Fu, and J. Jia, “ARPO:End-to-End Policy Optimization for GUI Agents with Experience Replay,” *ArXiv*, vol. abs/2505.16282, May 2025, doi: [10.48550/arXiv.2505.16282](https://doi.org/10.48550/arXiv.2505.16282).

\[Zha25an\] Z. Zhang *et al.*, “AgentCPM-GUI: Building Mobile-Use Agents with Reinforcement Fine-Tuning,” *ArXiv*, vol. abs/2506.01391, Jun. 2025, doi: [10.48550/arXiv.2506.01391](https://doi.org/10.48550/arXiv.2506.01391).

\[Pah25\] V. Pahuja *et al.*, “Explorer: Scaling Exploration-driven Web Trajectory Synthesis for Multimodal Web Agents,” *Annual Meeting of the Association for Computational Linguistics*, pp. 6300–6323, Feb. 2025, doi: [10.48550/arXiv.2502.11357](https://doi.org/10.48550/arXiv.2502.11357).

\[Liu25z\] J. Liu, J. Hao, C. Zhang, and Z. Hu, “WEPO: Web Element Preference Optimization for LLM-based Web Navigation,” *AAAI Conference on Artificial Intelligence*, pp. 26614–26622, Apr. 2025, doi: [10.1609/aaai.v39i25.34863](https://doi.org/10.1609/aaai.v39i25.34863).

\[Wan25y\] G. Wang *et al.*, “Information Gain-based Policy Optimization: A Simple and Effective Approach for Multi-Turn LLM Agents,” *ArXiv*, vol. abs/2510.14967, 2025, doi: [10.48550/arXiv.2510.14967](https://doi.org/10.48550/arXiv.2510.14967).

\[Hua26d\] H. Hua *et al.*, “SQL-Trail: Multi-Turn Reinforcement Learning with Interleaved Feedback for Text-to-SQL,” *ArXiv*, vol. abs/2601.17699, Jan. 2026, doi: [10.48550/arXiv.2601.17699](https://doi.org/10.48550/arXiv.2601.17699).

\[Pan24\] J. Pan *et al.*, “Training Software Engineering Agents and Verifiers with SWE-Gym,” *ArXiv*, vol. abs/2412.21139, Dec. 2024, doi: [10.48550/arXiv.2412.21139](https://doi.org/10.48550/arXiv.2412.21139).

\[Zen23d\] A. Zeng *et al.*, “AgentTuning: Enabling Generalized Agent Abilities for LLMs,” *ArXiv*, vol. abs/2310.12823, Oct. 2023, doi: [10.48550/arXiv.2310.12823](https://doi.org/10.48550/arXiv.2310.12823).

\[Xu24\] Y. Xu *et al.*, “AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials,” *ArXiv*, vol. abs/2412.09605, Dec. 2024, doi: [10.48550/arXiv.2412.09605](https://doi.org/10.48550/arXiv.2412.09605).

\[Mur24b\] S. Murty, D. Bahdanau, and C. D. Manning, “NNetNav: Unsupervised Learning of Browser Agents Through Environment Interaction in the Wild,” Oct. 03, 2024.

\[Lai25d\] H. Lai *et al.*, “AndroidGen: Building an Android Language Agent under Data Scarcity,” *ArXiv*, vol. abs/2504.19298, Apr. 2025, doi: [10.48550/arXiv.2504.19298](https://doi.org/10.48550/arXiv.2504.19298).

\[Zha24s\] Y. Zhai *et al.*, “Fine-Tuning Large Vision-Language Models as Decision-Making Agents via Reinforcement Learning,” *ArXiv*, vol. abs/2405.10292, May 2024, doi: [10.48550/arXiv.2405.10292](https://doi.org/10.48550/arXiv.2405.10292).

\[Szo23\] A. Szot *et al.*, “Large Language Models as Generalizable Policies for Embodied Tasks,” *ArXiv*, vol. abs/2310.17722, Oct. 2023, doi: [10.48550/arXiv.2310.17722](https://doi.org/10.48550/arXiv.2310.17722).

\[Hu26e\] Y. Hu *et al.*, “LongNav-R1: Horizon-Adaptive Multi-Turn RL for Long-Horizon VLA Navigation,” *ArXiv*, vol. abs/2602.12351, Feb. 2026, doi: [10.48550/arXiv.2602.12351](https://doi.org/10.48550/arXiv.2602.12351).

\[Gol25\] A. Golubev *et al.*, “Training Long-Context, Multi-Turn Software Engineering Agents with Reinforcement Learning,” *ArXiv*, vol. abs/2508.03501, Aug. 2025, doi: [10.48550/arXiv.2508.03501](https://doi.org/10.48550/arXiv.2508.03501).

\[Zha25ag\] H. Zhang *et al.*, “AgentRL: Scaling Agentic Reinforcement Learning with a Multi-Turn, Multi-Task Framework,” *ArXiv*, vol. abs/2510.04206, Oct. 2025, doi: [10.48550/arXiv.2510.04206](https://doi.org/10.48550/arXiv.2510.04206).

\[Guo25d\] Y. Guo *et al.*, “Improving Vision-Language-Action Model with Online Reinforcement Learning,” *2025 IEEE International Conference on Robotics and Automation (ICRA)*, pp. 15665–15672, Jan. 2025, doi: [10.1109/ICRA55743.2025.11127299](https://doi.org/10.1109/ICRA55743.2025.11127299).

\[Che24k\] S. Chen *et al.*, “Advancing Tool-Augmented Large Language Models: Integrating Insights from Errors in Inference Trees,” *ArXiv*, vol. abs/2406.07115, Jun. 2024, doi: [10.48550/arXiv.2406.07115](https://doi.org/10.48550/arXiv.2406.07115).

\[Luo25b\] R. Luo, L. Wang, W. He, and X. Xia, “GUI-R1 : A Generalist R1-Style Vision-Language Action Model For GUI Agents,” *ArXiv*, vol. abs/2504.10458, Apr. 2025, doi: [10.48550/arXiv.2504.10458](https://doi.org/10.48550/arXiv.2504.10458).

\[Zha25ao\] Z. Zhang, Z. Chen, M. Li, Z. Tu, and X. Li, “RLVMR: Reinforcement Learning with Verifiable Meta-Reasoning Rewards for Robust Long-Horizon Agents,” *ArXiv*, vol. abs/2507.22844, Jul. 2025, doi: [10.48550/arXiv.2507.22844](https://doi.org/10.48550/arXiv.2507.22844).
