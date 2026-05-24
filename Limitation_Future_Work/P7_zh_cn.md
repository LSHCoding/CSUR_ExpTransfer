# Carrier transformation gaps for CSUR

# 综述 载体转化缺口


##### [**Undermind**](https://undermind.ai)

##### [**Undermind**](https://undermind.ai) 来源


---


## Table of Contents

- [Challenges](#challenges)
  - [Converting raw interaction into reusable carriers is still lossy](#converting-raw-interaction-into-reusable-carriers-is-still-lossy)
  - [Verification remains the main weak link](#verification-remains-the-main-weak-link)
  - [The field still does not know how to reuse failure without poisoning the carrier](#the-field-still-does-not-know-how-to-reuse-failure-without-poisoning-the-carrier)
  - [Carrier design is a granularity problem, not just a data volume problem](#carrier-design-is-a-granularity-problem-not-just-a-data-volume-problem)
  - [Simulated carriers still flatten real state and long-horizon dependence](#simulated-carriers-still-flatten-real-state-and-long-horizon-dependence)
  - [Generalization claims are still narrower than the carrier rhetoric suggests](#generalization-claims-are-still-narrower-than-the-carrier-rhetoric-suggests)
  - [Cost and infrastructure are shaping which carriers get studied](#cost-and-infrastructure-are-shaping-which-carriers-get-studied)
- [Future directions](#future-directions)
  - [Failure-native carrier pipelines](#failure-native-carrier-pipelines)
  - [Grounded verification that is aware of carrier type](#grounded-verification-that-is-aware-of-carrier-type)
  - [Adaptive carrier granularity](#adaptive-carrier-granularity)
  - [More stateful and cross-system synthetic environments](#more-stateful-and-cross-system-synthetic-environments)
  - [Cross-carrier transfer studies](#cross-carrier-transfer-studies)
  - [Cost-aware carrier design](#cost-aware-carrier-design)
- [References](#references)

## Challenges

## 挑战


| Challenge | What the listed papers show | Hidden signals that matter for a CSUR discussion | Representative support |
|:---|:---|:---|:---|
| Converting raw interaction into reusable carriers is still lossy | Exploration traces usually need summarization, pruning, hindsight relabeling, or post hoc rewriting before they become trainable artifacts | The loss is not cosmetic. It changes task semantics, drops recovery behavior, and can remove the very steps that made the original interaction succeed | \[Pah25\], \[Tra25\], \[Wan25as\], \[Xie25e\], \[Log26b\], \[Pra25b\] |
| Verification remains the main weak link | Most pipelines depend on LLM judges, semantic checkers, or mock evaluators to decide whether a carrier is valid | Judge agreement is good enough to scale, but rarely good enough to treat accepted carriers as clean ground truth | \[Pah25\], \[Tra25\], \[Liu24n\], \[Awa25\], \[Wei26b\], \[Xu26e\], \[Xie25e\] |
| The field still does not know how to reuse failure without poisoning the carrier | Many systems either discard failed trajectories or convert them only through strong filtering | Partial success often helps more than success-only training, but naive failure inclusion is usually harmful | \[Log26b\], \[He25g\], \[Pra25b\], \[Liu24n\], \[Che26d\], \[Tao26\], \[Yan25x\] |
| Carrier design is a granularity problem, not just a data volume problem | Reasoning traces, fuzzy tasks, rubrics, step labels, and personas all help in some settings and hurt in others | Partial structure can be worse than no structure, and richer carriers can create new mismatch between teacher, verifier, and student | \[Lu26\], \[Lu26j\], \[Yan25ab\], \[Xu25o\], \[Liu24o\], \[Wei26b\] |
| Simulated carriers still flatten real state and long-horizon dependence | Mock tools, dense information trees, local mappings, and synthetic arenas help scale but simplify the hardest forms of agency | Long-horizon, stateful, cross-system behavior remains the place where synthetic carriers lose realism fastest | \[Wan25as\], \[Li25at\], \[Tao26\], \[Tia26\], \[Lu26j\], \[Xu26e\], \[Ver25b\] |
| Generalization claims are still narrower than the carrier rhetoric suggests | Many papers show strong gains on the target format or benchmark but weaker transfer across sites, apps, prompt protocols, or reasoning regimes | The same transformed experience often does not survive format shift, prompt shift, or evaluation shift cleanly | \[Lu26\], \[Tra25\], \[Awa25\], \[Che26d\], \[Wei26b\], \[Liu24o\], \[Xu26e\] |
| Cost and infrastructure are shaping which carriers get studied | Real execution, step filtering, expert monitors, and executable environment synthesis are all expensive | The literature often treats these costs as engineering details, but they already determine what forms of experience can be preserved at all | \[Pah25\], \[Xu25o\], \[Awa25\], \[Che26d\], \[Tia26\], \[He25g\] |

| 挑战 | 所列论文显示的内容 | 对 综述 讨论重要的隐藏信号 | 代表性支持文献 |
|:---|:---|:---|:---|
| 将原始交互转为可复用载体仍然有损 | 探索轨迹通常需要摘要、剪枝、 事后重新标注 或事后重写，才能成为可训练工件 | 这种损失不是表面问题。它会改变任务语义、丢失恢复行为，并可能移除原始交互成功所依赖的步骤 | \[Pah25\], \[Tra25\], \[Wan25as\], \[Xie25e\], \[Log26b\], \[Pra25b\] |
| 验证仍是主要薄弱环节 | 多数流水线依赖 大语言模型 裁判器、语义检查器或模拟评估器来判断载体是否有效 | 裁判器一致性足以支撑规模化，但很少足以把被接受载体当作干净真实标注 | \[Pah25\], \[Tra25\], \[Liu24n\], \[Awa25\], \[Wei26b\], \[Xu26e\], \[Xie25e\] |
| 领域仍不知道如何在不污染载体的情况下复用失败 | 许多系统要么丢弃失败轨迹，要么只通过强过滤转化它们 | 部分成功常比只用成功训练更有帮助，但朴素纳入失败通常有害 | \[Log26b\], \[He25g\], \[Pra25b\], \[Liu24n\], \[Che26d\], \[Tao26\], \[Yan25x\] |
| 载体设计是粒度问题，不只是数据量问题 | 推理轨迹、模糊任务、评分规程、步骤标签和 persona 在某些设置中有帮助，在另一些设置中有害 | 部分结构可能比没有结构更差，更丰富的载体会在教师、验证器和学生之间制造新错配 | \[Lu26\], \[Lu26j\], \[Yan25ab\], \[Xu25o\], \[Liu24o\], \[Wei26b\] |
| 模拟载体仍会压平真实状态和长时程依赖 | 模拟工具、稠密信息树、局部映射和合成场域有助于规模化，但简化了最困难的能动性形式 | 长时程、有状态、跨系统行为仍是合成载体最快失真的地方 | \[Wan25as\], \[Li25at\], \[Tao26\], \[Tia26\], \[Lu26j\], \[Xu26e\], \[Ver25b\] |
| 泛化声明仍比载体叙事暗示的范围更窄 | 许多论文在目标格式或基准上有强收益，但跨站点、应用、提示协议或推理机制迁移较弱 | 同一被转化经验常常无法干净承受格式转移、提示转移或评估转移 | \[Lu26\], \[Tra25\], \[Awa25\], \[Che26d\], \[Wei26b\], \[Liu24o\], \[Xu26e\] |
| 成本和基础设施正在塑造哪些载体会被研究 | 真实执行、步骤过滤、专家监控器和可执行环境合成都很昂贵 | 文献常把这些成本当作工程细节，但它们已经决定哪些经验形式能被保留下来 | \[Pah25\], \[Xu25o\], \[Awa25\], \[Che26d\], \[Tia26\], \[He25g\] |

### Converting raw interaction into reusable carriers is still lossy

### 将原始交互转为可复用载体仍然有损


A recurring pattern across web, tool, and GUI papers is that raw interaction almost never becomes the final training artifact directly. It is first cleaned, rewritten, summarized, or partially relabeled. Explorer turns web exploration into task proposals, iterative refinements, trajectory summaries, and then a verifier-approved final task, but Section 6 shows that the largest failure modes are precisely inside that conversion stack: grounding errors account for 30 percent of failures and summarization hallucinations for 29 percent, with the summary sometimes adding goals that were never achieved in the underlying trajectory \[Pah25\]. InSTA uses exploratory trajectories to generate harder grounded tasks through the loop formalized in Equation 4, yet Section 6.2 then discards the reasoning trace when converting those data to static benchmark formats \[Tra25\]. AgentSynth makes the asymmetry even starker: the whole method works by first solving many easy subtasks and then using a task summarizer to compress them into a single hard instruction, but the final summary explicitly abstracts away step-level details that were necessary during generation, and success rates fall steeply from easier to harder summary levels in Table 5 \[Xie25e\].

在网页、工具和 图形界面 论文中，一个反复出现的模式是，原始交互几乎从不直接成为最终训练工件。它会先被清洗、重写、摘要或部分重新标注。探索系统 将网页探索转为任务提案、迭代 修订、轨迹摘要，再转为验证器批准的最终任务，但第 6 节显示，最大的失败模式恰好位于这个转化栈内部：grounding 错误占失败的 30%，摘要幻觉占 29%，摘要有时还会加入底层轨迹从未达成的目标 \[Pah25\]。互联网规模训练方法 使用探索轨迹，通过公式 4 形式化的循环生成更难的 有依托 任务，但第 6.2 节随后在把这些数据转为静态基准格式时丢弃推理轨迹 \[Tra25\]。任务合成方法 让这种不对称更明显：整个方法先解决许多简单子任务，再用任务摘要器把它们压缩成一条困难指令，但最终摘要显式抽象掉生成过程中必要的步骤级细节，且表 5 中成功率从较易摘要层级到较难摘要层级急剧下降 \[Xie25e\]。

Several papers go further and rescue useful data only by changing the task after the fact. Logeswaran et al. extract the prefix at the point of maximum constraint satisfaction and then perform hindsight relabeling so that a partially completed task becomes a valid new task for training \[Log26b\]. SynthAgent reports a similar tension in web supervision: task refinement improves feasibility, but also injects noise that trajectory refinement must later remove, and Table 10 shows that on Shopping the version without either refinement stage can match or slightly beat the full pipeline \[Wan25ar\]. APIGen-MT reveals the same issue in conversational tool use from another angle. Figure 4 shows a drop from blueprint success to simulated interaction success, meaning some information is lost while moving from a verified structural plan to a multi-turn dialogue trace \[Pra25b\].

若干论文更进一步，只有通过事后改变任务才能挽救有用数据。相关工作 在约束满足最大点提取前缀，然后进行 事后重新标注，使部分完成任务变成可用于训练的有效新任务 \[Log26b\]。网页合成方法 报告了网页监督中的类似张力：任务 修订 提升可行性，但也注入噪声，随后必须由轨迹 修订 移除；表 10 显示，在 Shopping 上，没有任一 修订 阶段的版本可以匹配或略微超过完整流水线 \[Wan25ar\]。多轮接口生成方法 从会话式工具使用的另一个角度揭示同一问题。图 4 显示从 blueprint 成功到模拟交互成功存在下降，意味着从已验证结构计划移动到多轮对话轨迹时会损失部分信息 \[Pra25b\]。

Inference. The field has not yet found a carrier that preserves both procedural fidelity and training usability. Current systems succeed by compressing or rewriting interaction until it fits a clean training interface. That makes transformed experience useful, but it also means the transformed carrier is often a curated interpretation of experience rather than the experience itself \[Pah25, Tra25, Xie25e, Log26b, Pra25b\].

推断。该领域尚未找到一种同时保留过程忠实度和训练可用性的载体。当前系统通过压缩或重写交互，直到它适配干净训练接口而成功。这让被转化经验变得有用，但也意味着被转化载体常常是对经验的筛选式解释，而非经验本身 \[Pah25, Tra25, Xie25e, Log26b, Pra25b\]。

### Verification remains the main weak link

### 验证仍是主要薄弱环节


Most of these papers are best read as verification papers disguised as data papers. APIGen is explicit that raw synthetic function-calling data is too noisy to trust, so it introduces format, execution, and semantic checkers. Even then, Table 1 shows that weaker generators fail verification at very high rates, and Appendix B.2 admits that stronger credibility might require multiple LLM checkers rather than one \[Liu24n\]. Explorer reports only 81 percent agreement between its automated verifier and human judgment in Table 10 \[Pah25\]. InSTA’s judge reaches roughly 78 to 82.6 percent accuracy for trajectory success depending on setting, which is strong enough to curate at scale but weak enough that accepted demonstrations still contain meaningful label noise \[Tra25\]. Fara-7B similarly needs three different verifiers and still reaches only 83.3 percent agreement with humans \[Awa25\]. ANCHOR reports 87 percent verifier accuracy with a wide confidence interval in a targeted human audit, again good enough for pipeline control but not clean enough to treat verification as solved \[Wei26b\]. AgentSynth’s verifier has 88 percent agreement with humans, yet Table 2 shows that it still falsely accepts 12 percent of near-miss cases, precisely the kind of subtle failure that matters for long-horizon desktop tasks \[Xie25e\].

这些论文最好被理解为伪装成数据论文的验证论文。接口生成方法 明确指出，原始合成函数调用数据噪声太大，不能信任，因此引入格式、执行和语义检查器。即便如此，表 1 显示较弱生成器的验证失败率很高，附录 B.2 承认，更强可信度可能需要多个 大语言模型 检查器，而非一个 \[Liu24n\]。探索系统 在表 10 中报告其自动验证器与人类判断只有 81% 一致 \[Pah25\]。互联网规模训练方法 的裁判器在不同设置下对轨迹成功的准确率约为 78% 到 82.6%，足以规模化筛选，但仍会让被接受示范包含有意义的标签噪声 \[Tra25\]。七十亿参数模型 同样需要三种不同验证器，仍只达到与人类 83.3% 的一致性 \[Awa25\]。分支生成方法 在定向人工审计中报告 87% 的验证器准确率，置信区间较宽，同样足以控制流水线，但不足以把验证视为已解决 \[Wei26b\]。任务合成方法 的验证器与人类有 88% 一致性，但表 2 显示它仍错误接受 12% 的近似失败案例，而这正是长时程桌面任务中关键的细微失败 \[Xie25e\]。

This matters because verification is not just the last stage. It shapes the carrier itself. In Structured Distillation, evaluation hints are valuable because the judge cannot reliably infer success from the trajectory alone. Appendix C.5 reports that hints help the judge catch 144 additional false positives, and removing hints drops student performance by 2.4 points \[Lu26\]. In COVERT, some target behaviors can only be scored through judge-assisted augmentations, and Section 4 openly notes that these judge decisions are non-deterministic and have not yet been validated against humans \[Xu26e\]. ToolMind highlights a subtler failure mode: trajectory-level filtering cannot isolate turn-level errors, so apparently valid multi-turn traces may still contain wrong intermediate assumptions or role drift \[Yan25ab\].

这一点很重要，因为验证不只是最后阶段。它会塑造载体本身。在 结构化蒸馏 中，评估提示之所以有价值，是因为裁判器无法仅从轨迹可靠推断成功。附录 C.5 报告，提示帮助裁判器额外捕捉 144 个假阳性，移除提示会使学生性能下降 2.4 点 \[Lu26\]。在 可控工具合成方法 中，一些目标行为只能通过裁判器辅助增强来评分，第 4 节公开说明这些裁判器决策是非确定性的，且尚未与人类验证 \[Xu26e\]。工具数据集方法 强调了一个更细微的失败模式：轨迹级过滤不能隔离轮次级错误，因此表面有效的多轮轨迹仍可能包含错误中间假设或角色漂移 \[Yan25ab\]。

There is little real disagreement across the papers about whether judges are needed. The disagreement is about how much trust they deserve. The more careful papers treat the judge as a noisy bottleneck rather than an oracle \[Lu26, Xu26e, Xie25e\]. The less careful framing appears when accepted data are described as high quality without a serious estimate of residual error. For a survey discussion, that residual error is not a footnote. It is one of the main reasons current carrier transformations are still brittle.

论文之间对是否需要裁判器几乎没有真实分歧。分歧在于它们应获得多少信任。更谨慎的论文把裁判器视为带噪瓶颈，而非 理想 \[Lu26, Xu26e, Xie25e\]。较不谨慎的表述出现在被接受数据被称为高质量、却缺少严肃残余错误估计的地方。对 survey 讨论而言，残余错误不是脚注。它是当前载体转化仍然脆弱的主要原因之一。

### The field still does not know how to reuse failure without poisoning the carrier

### 领域仍不知道如何在不污染载体的情况下复用失败


The listed papers repeatedly show that failure is informative, but they also show that failure is hard to package. RAGShaper keeps only teacher trajectories whose answers score above 0.9 F1, which means failed reasoning paths are not transformed into negative supervision at all \[Tao26\]. APIGen-MT explicitly discards failed trajectories from its second phase and names contrastive use of those failures as future work \[Pra25b\]. APIGen has to synthesize negative relevance cases manually by discarding tools or parameters, which is revealing because the main pipeline does not naturally generate enough useful failure examples on its own \[Liu24n\].

所列论文反复显示失败有信息量，但也显示失败很难被包装。检索增强塑形方法 只保留答案 F1 高于 0.9 的教师轨迹，这意味着失败推理路径完全没有被转化为负监督 \[Tao26\]。多轮接口生成方法 明确从第二阶段丢弃失败轨迹，并把这些失败的对比式使用列为未来工作 \[Pra25b\]。接口生成方法 必须通过丢弃工具或参数来人工合成负相关案例，这很有启发，因为主流水线本身无法自然生成足够有用的失败样本 \[Liu24n\]。

At the same time, several papers show that filtering everything down to perfect success is also too blunt. WebSTAR reports that fewer than half of the steps in successful teacher trajectories are actually correct or optimal, so trajectory-level success is a bad proxy for step-level supervision quality \[He25g\]. Logeswaran et al. show that training on transformed partial successes beats training only on complete successes, and Table 2 shows that partial-success data plus LoRA gives the best CSR score \[Log26b\]. OpenMobile argues that expert trajectory distillation misses error recovery, which is why it introduces policy switching and an error-intervention monitor to generate correction trajectories rather than ideal rollouts alone \[Che26d\]. Step-GUI makes the failure split explicit. Its calibrated step reward system allows failed trajectories to contribute knowledge repair items but prevents them from contributing direct action prediction, precisely to avoid propagating wrong behavior \[Yan25x\].

与此同时，若干论文显示把一切过滤成完美成功也太粗糙。步骤过滤方法 报告，成功教师轨迹中少于一半步骤实际上正确或最优，因此轨迹级成功并不是步骤级监督质量的好代理 \[He25g\]。相关工作 显示，用被转化的部分成功训练优于只用完整成功训练，表 2 显示部分成功数据加 低秩适配 得到最佳 约束满足率 分数 \[Log26b\]。开放移动智能体方法 认为专家轨迹蒸馏错过错误恢复，因此引入策略切换和错误干预监控器来生成纠错轨迹，而非只生成理想采样轨迹 \[Che26d\]。Step-图形界面 明确区分失败。其校准步骤奖励系统允许失败轨迹贡献知识修复项，但阻止它们贡献直接动作预测，以避免传播错误行为 \[Yan25x\]。

The tension is not between success and failure as simple opposites. It is between different kinds of failure transformation. Prefix extraction \[Log26b\], step-level filtering \[He25g\], error-intervention recovery \[Che26d\], and knowledge-only reuse from failed rollouts \[Yan25x\] each preserve different parts of a failed episode. No paper here shows a generally reliable way to preserve failure cause, attempted repair, and downstream correction in one stable carrier. Inference. That missing representation is one of the clearest research gaps in this subliterature \[Log26b, He25g, Che26d, Pra25b, Yan25x\].

张力不在于把成功和失败当作简单对立面。它存在于不同失败转化方式之间。前缀提取 \[Log26b\]、步骤级过滤 \[He25g\]、错误干预恢复 \[Che26d\] 和从失败采样轨迹中仅复用知识 \[Yan25x\]，各自保留失败 片段 的不同部分。这里没有论文展示一种普遍可靠方式，能在一个稳定载体中同时保留失败原因、尝试过的修复和下游纠正。推断。缺失的这种表示是该子文献中最清楚的研究缺口之一 \[Log26b, He25g, Che26d, Pra25b, Yan25x\]。

### Carrier design is a granularity problem, not just a data volume problem

### 载体设计是粒度问题，不只是数据量问题


The strongest hidden result in this set is that carrier choice is often more important than raw sample count. Structured Distillation provides the clearest example. Full reasoning traces help, but Appendix C.3 shows that truncating them is worse than removing them entirely. The issue is not simply having more rationale tokens. It is whether the trace remains coherent enough to be a usable carrier \[Lu26\]. The same paper also finds that a reduced-thinking teacher produces better distillation data than a higher-budget teacher, apparently because the more powerful teacher compresses too much of its reasoning internally and externalizes a less learnable trace \[Lu26\]. That is an unusually direct warning that better reasoning does not automatically mean better transferable reasoning carriers.

这一组中最强的隐藏结果是，载体选择常比原始样本数更重要。结构化蒸馏 提供了最清楚例子。完整推理轨迹有帮助，但附录 C.3 显示，截断它们比完全移除它们更差。问题不只是拥有更多 rationale 词元，而是轨迹是否保持足够连贯，能成为可用载体 \[Lu26\]。同一论文还发现，低思考预算教师产生的蒸馏数据优于更高预算教师，表面原因是更强教师把太多推理压缩到内部，外化出的轨迹反而更难学习 \[Lu26\]。这是一个异常直接的警告：更好的推理并不自动意味着更好的可迁移推理载体。

Other papers reach the same conclusion from different carrier forms. SYNTHAGENT introduces an information gap by rewriting detailed workflows as underspecified instructions with hidden context. Table 4 shows that removing this gap causes a sharp drop in performance, because the policy becomes too deterministic and RL gradients weaken \[Lu26j\]. Here, less explicit information creates a better learning carrier. ToolMind shows the opposite problem at a different granularity: trajectory-level filtering misses erroneous turns, so macro-level quality control is not enough when the true supervision signal lives at the turn level \[Yan25ab\]. TOUCAN finds that adding persona-based diversification produces a slight overall decline in Table 6 after irrelevance handling has already been added, suggesting that one more layer of carrier richness can turn into linguistic noise rather than capability gain \[Xu25o\]. ToolACE shows that removing multi-type data causes irrelevance detection to collapse, but also reports a tradeoff where specialization for function calling leaves general reasoning lagging behind frontier general models \[Liu24o\].

其他论文从不同载体形式得到同样结论。合成智能体方法 通过把详细工作流重写为带隐藏上下文的欠指定指令来引入信息缺口。表 4 显示，移除这个缺口会显著降低性能，因为策略变得过于确定，强化学习 梯度变弱 \[Lu26j\]。在这里，信息不那么显式反而创造了更好的学习载体。工具数据集方法 在另一种粒度上展示相反问题：轨迹级过滤会漏掉错误轮次，因此当真实监督信号位于轮次级时，宏观质量控制不足够 \[Yan25ab\]。工具数据合成方法 发现，在已经加入无关性处理后，再加入基于 persona 的多样化会在表 6 中带来轻微整体下降，暗示再多一层载体丰富性可能转为语言噪声，而非能力收益 \[Xu25o\]。函数调用方法 显示，移除多类型数据会使无关性检测坍缩，但也报告了一个权衡：对函数调用的专门化会让一般推理落后于前沿通用模型 \[Liu24o\]。

These results do not form a clean consensus around one best carrier. They point to a design space with real incompatibilities. Richer carriers can preserve more task structure, but can also overload students or misalign teacher and consumer interfaces. Simpler carriers can stabilize optimization, but can also erase the reasoning or recovery structure the field claims to care about. Inference. The open problem is not how to scale one carrier format. It is how to choose, adapt, and sometimes switch carrier granularity so that each transformation preserves the part of experience needed for the next learning stage \[Lu26, Lu26j, Yan25ab, Xu25o, Liu24o\].

这些结果并不围绕某个最佳载体形成干净共识。它们指向一个存在真实不兼容性的设计空间。更丰富载体可以保留更多任务结构，但也可能让学生过载，或错配教师与消费者接口。更简单载体可以稳定优化，但也可能擦除领域声称关心的推理或恢复结构。推断。开放问题不在于如何扩展单一载体格式，而在于如何选择、适配，并在必要时切换载体粒度，使每次转化都保留下一学习阶段所需的经验部分 \[Lu26, Lu26j, Yan25ab, Xu25o, Liu24o\]。

### Simulated carriers still flatten real state and long-horizon dependence

### 模拟载体仍会压平真实状态和长时程依赖


Many papers solve the scale problem by replacing live environments with mock worlds, simulated tool feedback, or prestructured information graphs. That move is productive, but it also exposes a major gap. EviPath avoids real-time retrieval by constructing a simulated local environment from supporting facts, and Figure 4 shows a large gap between distractor settings with gold evidence and open-domain settings with noisy retrieval \[Li25at\]. RAGShaper builds dense information trees and forces constrained navigation through distractors, which is effective for eliciting sophisticated RAG behavior, but also narrows the target to factoid-style multi-hop paths and leaves more open-ended retrieval skills largely untouched \[Tao26\]. ASTRA translates tool-use problems into executable arenas, yet Section 2.1.2 explicitly restricts composition to tools within the same MCP server, and Section 4.2 shows that reward design becomes unstable when precision and recall are not balanced carefully \[Tia26\]. COVERT reports limited gains on long-horizon categories and no real improvement on BFCL Multi-Turn or ACEBench Agent, then explains that its current mock environments do not model tightly coupled stateful dependencies across many turns \[Xu26e\].

许多论文通过用模拟世界、模拟工具反馈或预结构化信息图替代实时环境来解决规模问题。这一步有生产力，但也暴露出主要缺口。证据路径方法 通过从支持事实构建模拟局部环境来避免实时检索，图 4 显示带 黄金证据 的干扰设置与带噪检索的开放域设置之间存在很大差距 \[Li25at\]。检索增强塑形方法 构建稠密信息树，并强制通过干扰项进行受限导航，这对引出复杂 RAG 行为有效，但也把目标缩窄到 factoid 式多跳路径，基本未触及更开放的检索技能 \[Tao26\]。场域合成方法 将工具使用问题转译为可执行场域，但第 2.1.2 节明确把组合限制在同一个 模型上下文协议服务器 内的工具，第 4.2 节显示，当 precision 和 recall 没有仔细平衡时，奖励设计会变得不稳定 \[Tia26\]。可控工具合成方法 报告在长时程类别上收益有限，在 BFCL Multi-Turn 或 ACEBench Agent 上没有真正改进，随后解释其当前模拟环境没有建模多轮之间紧密耦合的有状态依赖 \[Xu26e\]。

The same flattening appears in digital-world simulation. Wang et al. show that retrieval-free simulation underperforms retrieval-augmented simulation on AndroidWorld, and Appendix F documents context fusion failures where the simulator carries over irrelevant page state or over-relies on retrieved reference states \[Wan25as\]. SYNTHAGENT’s lightweight finite mapping is intentionally task-local and works because many tool simulations reduce to formatted question answering, but that is also a scope limit acknowledged in the paper \[Lu26j\]. FABRIC makes the carrier hierarchy more explicit: records become dialogues become atomic tool calls, but Section 5 warns that this decomposition risks loss of grounding generality and amplification of synthetic signal biases \[Ver25b\].

同样的压平也出现在数字世界模拟中。相关工作 显示，在 AndroidWorld 上，无检索模拟弱于检索增强模拟，附录 F 记录了上下文融合失败：模拟器会携带无关页面状态，或过度依赖检索到的参考状态 \[Wan25as\]。合成智能体方法 的轻量有限映射有意保持任务局部性，并且之所以有效，是因为许多工具模拟可简化为格式化问答，但这也是论文承认的范围限制 \[Lu26j\]。智能体数据生成框架 更显式地呈现载体层级：记录变成对话，对话变成原子工具调用，但第 5 节警告，这种分解有丢失 grounding 泛化性和放大合成信号偏差的风险 \[Ver25b\]。

The important point is not simply that simulators are imperfect. It is that their imperfections are structurally aligned with the hardest forms of agency: statefulness, cross-tool dependency, hidden context, and long-horizon repair. Those are exactly the parts of interaction experience that current carrier transformations are most likely to flatten away.

关键点不只是模拟器不完美。它们的不完美在结构上对齐于最困难的能动性形式：有状态性、跨工具依赖、隐藏上下文和长时程修复。这些正是当前载体转化最可能压平掉的交互经验部分。

### Generalization claims are still narrower than the carrier rhetoric suggests

### 泛化声明仍比载体叙事暗示的范围更窄


Several papers claim that transformed experience supports broader capability transfer, but their own ablations show that transfer often depends on staying close to the source format. In Structured Distillation, gains are real and impressive, but Figure 9a shows diminishing returns within the same six sites, and Section 5.1 notes a clear residual gap on WorkArena++ L2, where longer compositional tasks still favor larger models \[Lu26\]. InSTA can pretrain agents on a huge live-web dataset, yet when its data are adapted to static benchmarks the reasoning trace is discarded to match older formats, which is itself evidence of incomplete carrier compatibility \[Tra25\]. COVERT goes out of its way to evaluate under a minimal prompt and shows that SFT baselines can suffer unexpectedly large regressions from prompt-format sensitivity alone \[Xu26e\]. Fara-7B trains a native pixel agent on traces generated with accessibility-tree and Set-of-Marks scaffolding, creating a producer-consumer mismatch in which the teacher’s carrier contains structural information the student never sees at inference time \[Awa25\].

若干论文声称被转化经验支持更广能力迁移，但它们自己的消融显示，迁移常依赖保持接近源格式。在 结构化蒸馏 中，收益真实且令人印象深刻，但图 9a 显示在同六个站点内收益递减，第 5.1 节指出 WorkArena++ L2 上仍存在明显残余差距，较长组合任务仍偏向更大模型 \[Lu26\]。互联网规模训练方法 可以在巨量 实时网页 数据上预训练智能体，但当其数据被适配到静态基准时，推理轨迹被丢弃以匹配旧格式，这本身就是载体兼容性不完整的证据 \[Tra25\]。可控工具合成方法 特意在极简提示下评估，并显示 监督微调 基线仅因提示格式敏感性就会遭遇意外的大幅退化 \[Xu26e\]。七十亿参数模型 用 无障碍树 和 标记集合 脚手架生成的轨迹训练原生像素智能体，制造了生产者-消费者错配：教师载体包含学生推理时看不到的结构信息 \[Awa25\]。

There are also domain-specific limits. OpenMobile finds that RL variants do not consistently beat the SFT baseline, attributing this partly to limited environment diversity and to the mismatch between step-level optimization and long-horizon execution \[Che26d\]. ANCHOR shows that cross-domain augmentation helps only after enough data accumulate, and can lag Ubuntu-only training at smaller scales \[Wei26b\]. ToolACE improves function calling while still lagging much stronger models on broad reasoning benchmarks such as MMLU and GSM8K \[Liu24o\]. These are not side notes. They show that transformed experience can overfit to the interface between its source carrier and its consumer.

也存在领域特定限制。开放移动智能体方法 发现 强化学习 变体并不稳定超过 监督微调 基线，并将部分原因归于有限环境多样性，以及步骤级优化与长时程执行之间的错配 \[Che26d\]。分支生成方法 显示，跨领域增强只有在积累足够数据后才有帮助，并且在较小规模上可能落后于仅 Ubuntu 训练 \[Wei26b\]。函数调用方法 改进了函数调用，但在 MMLU 和 GSM8K 等广泛推理基准上仍落后于强得多的模型 \[Liu24o\]。这些不是旁注。它们显示，被转化经验可能过拟合其源载体与消费者之间的接口。

Inference. Much of the literature still demonstrates transfer within a carrier family more than transfer across carrier changes. The harder question for this survey topic is whether a skill learned as a summarized task, reasoning trace, rubric, or synthetic reward remains useful after the representation changes. The current evidence says only partially.

推断。许多文献展示的是载体家族内部迁移，而非跨载体变化的迁移。对本 survey 主题来说，更难的问题是，以摘要任务、推理轨迹、评分规程 或合成奖励学到的技能，在表示改变后是否仍有用。当前证据只给出部分肯定。

### Cost and infrastructure are shaping which carriers get studied

### 成本和基础设施正在塑造哪些载体会被研究


The listed papers make it clear that carrier design is already constrained by economics. TOUCAN starts from 2,851 crawled MCP servers and ends with 495 high-quality servers after credential and stability filtering, then identifies slow and costly real tool execution as a reason to consider expert simulators in future work \[Xu25o\]. Explorer reports an average cost per successful trajectory of 0.28 dollars and still filters out inaccessible sites, scrolling-heavy traces, and safety-sensitive states such as logins and payments \[Pah25\]. Fara-7B quantifies the funnel even more starkly: on complex task families only a tiny fraction of solved trajectories survive verification as successful training examples, while the bulk of cost is spent in the reasoning agents rather than the final student \[Awa25\]. OpenMobile depends on a high-capability monitor to inject corrective trajectories \[Che26d\]. WebSTAR shows that stricter quality thresholds make data much more expensive because many more rollouts are required to hit a fixed step budget \[He25g\]. ASTRA notes that executable environment synthesis itself is expensive enough that future work should reject low-confidence topologies before code generation \[Tia26\].

所列论文清楚显示，载体设计已经受到经济性约束。工具数据合成方法 从 2,851 个爬取的 模型上下文协议服务器 出发，在凭证和稳定性过滤后只保留 495 个高质量 服务器，随后把缓慢且昂贵的真实工具执行列为未来考虑专家模拟器的理由 \[Xu25o\]。探索系统 报告每条成功轨迹平均成本为 0.28 美元，并且仍过滤掉不可访问站点、滚动过多的轨迹，以及登录和支付等安全敏感状态 \[Pah25\]。七十亿参数模型 更鲜明地量化漏斗：在复杂任务族上，只有极小比例的已解决轨迹通过验证成为成功训练样本，而大部分成本花在推理智能体上，而非最终学生 \[Awa25\]。开放移动智能体方法 依赖高能力监控器注入纠正轨迹 \[Che26d\]。步骤过滤方法 显示，更严格质量阈值会显著增加成本，因为需要更多采样轨迹才能达到固定步骤预算 \[He25g\]。场域合成方法 指出，可执行环境合成本身已足够昂贵，因此未来工作应在代码生成前拒绝低置信拓扑 \[Tia26\]。

This systems burden matters scientifically because it biases the field toward carriers that are cheap to validate, compress, and replay. That bias favors short or medium-horizon tasks, deterministic interfaces, local state mappings, and cheap binary judgments. It disfavors exactly the experiences that are hardest to transform and probably most valuable for robust agents.

这种系统负担具有科学意义，因为它会让领域偏向那些便宜验证、压缩和回放的载体。该偏向有利于短或中等时程任务、确定性接口、局部状态映射和廉价二元判断。它不利于最难转化、也可能对鲁棒智能体最有价值的经验。

## Future directions

## 未来方向


| Direction | What concrete progress would look like | Core support |
|:---|:---|:---|
| Failure-native carrier pipelines | Carriers preserve partial progress, failure cause, repair attempt, and verified recovery instead of keeping only clean success traces | \[Log26b\], \[He25g\], \[Che26d\], \[Pra25b\], \[Yan25x\] |
| Grounded verification that is aware of carrier type | Different carriers receive different validation regimes rather than passing all artifacts through one generic LLM judge | \[Pah25\], \[Tra25\], \[Lu26\], \[Xie25e\], \[Xu26e\], \[Yan25ab\] |
| Adaptive carrier granularity | Systems choose when experience should stay as a trace, become a summarized task, become a rubric, or become a reward signal | \[Lu26\], \[Lu26j\], \[Xie25e\], \[Yan25ab\], \[Xu25o\], \[Liu24o\] |
| More stateful and cross-system synthetic environments | Synthetic carriers should model long-range dependencies, cross-tool composition, and non-random failure patterns | \[Wan25as\], \[Li25at\], \[Tao26\], \[Tia26\], \[Xu26e\], \[Ver25b\] |
| Cross-carrier transfer studies | The same underlying experience should be evaluated after conversion into multiple carrier forms, not only in the original representation | \[Tra25\], \[Awa25\], \[Lu26\], \[Liu24o\], \[Xu26e\] |
| Cost-aware carrier design | Papers should report which carrier transformations produce the most validated utility per unit of rollout, judge, or simulator cost | \[Pah25\], \[Xu25o\], \[Awa25\], \[Che26d\], \[He25g\], \[Tia26\] |

| 方向 | 具体进展形态 | 核心支持文献 |
|:---|:---|:---|
| 失败原生载体流水线 | 载体保留部分进展、失败原因、修复尝试和已验证恢复，而不是只保留干净成功轨迹 | \[Log26b\], \[He25g\], \[Che26d\], \[Pra25b\], \[Yan25x\] |
| 感知载体类型的 有依托 验证 | 不同载体使用不同验证机制，而不是让所有工件通过一个通用 大语言模型 裁判器 | \[Pah25\], \[Tra25\], \[Lu26\], \[Xie25e\], \[Xu26e\], \[Yan25ab\] |
| 自适应载体粒度 | 系统选择经验何时应保留为轨迹、变成摘要任务、变成 评分规程 或变成奖励信号 | \[Lu26\], \[Lu26j\], \[Xie25e\], \[Yan25ab\], \[Xu25o\], \[Liu24o\] |
| 更有状态、跨系统的合成环境 | 合成载体应建模长程依赖、跨工具组合和非随机失败模式 | \[Wan25as\], \[Li25at\], \[Tao26\], \[Tia26\], \[Xu26e\], \[Ver25b\] |
| 跨载体迁移研究 | 同一底层经验应在转为多种载体形式后评估，而不只在原始表示中评估 | \[Tra25\], \[Awa25\], \[Lu26\], \[Liu24o\], \[Xu26e\] |
| 成本感知载体设计 | 论文应报告哪些载体转化在单位采样、裁判器或模拟器成本下产生最高验证效用 | \[Pah25\], \[Xu25o\], \[Awa25\], \[Che26d\], \[He25g\], \[Tia26\] |

### Failure-native carrier pipelines

### 失败原生载体流水线


The clearest near-term direction is to stop treating failure as either raw poison or discarded waste. Current papers already contain pieces of a better design. Logeswaran et al. show that prefix extraction and hindsight relabeling can recover useful learning signal from partial success \[Log26b\]. WebSTAR shows why this matters at finer granularity: even successful trajectories contain many weak steps, so the right unit of salvage is often below the full trajectory \[He25g\]. OpenMobile demonstrates that error-recovery traces created through monitor-triggered intervention capture skills that pure expert distillation misses \[Che26d\]. Step-GUI separates failed rollouts into knowledge repair rather than direct behavior cloning, which is a principled way to let failure teach without copying wrong actions \[Yan25x\]. APIGen-MT explicitly names contrastive use of failed conversations as missing future work \[Pra25b\].

最清楚的近期方向是停止把失败视为原始毒素或被丢弃废料。当前论文已经包含更好设计的若干组件。相关工作 显示，前缀提取和 事后重新标注 可以从部分成功中恢复有用学习信号 \[Log26b\]。步骤过滤方法 显示了为什么这在更细粒度上重要：即便成功轨迹也包含许多薄弱步骤，因此可挽救的正确单元常低于完整轨迹 \[He25g\]。开放移动智能体方法 证明，通过监控器触发干预生成的错误恢复轨迹捕捉到纯专家蒸馏错过的技能 \[Che26d\]。Step-图形界面 将失败采样轨迹分离为知识修复而非直接行为克隆，这是一种有原则的方式，让失败能教学而不复制错误动作 \[Yan25x\]。多轮接口生成方法 明确把失败会话的对比使用称作缺失的未来工作 \[Pra25b\]。

Concrete progress here would look like a carrier that stores four linked objects for each non-perfect episode: the best verified prefix, the failure type, the repair attempt, and the later evidence that the repair worked or failed. That design would let a survey claim something stronger than “partial success helps.” It would allow direct tests of whether transformed failure teaches recovery, avoidance, or both. A strong paper should compare success-only carriers, prefix-only carriers, repair-annotated carriers, and failure-aware reward carriers on the same environment set. If only the last variant improves recovery on unseen tasks, then the field would finally have evidence that it is learning from failure rather than merely filtering around it.

这里的实际进展应是一个载体，为每个非完美 片段 存储四个相互链接的对象：最佳已验证前缀、失败类型、修复尝试，以及随后证明修复成功或失败的证据。该设计会让 survey 能提出比“部分成功有帮助”更强的主张。它允许直接测试被转化失败是在教授恢复、规避，还是二者兼有。强论文应在同一环境集合上比较只含成功的载体、只含前缀的载体、带修复标注的载体和失败感知奖励载体。如果只有最后一种变体提升未见任务上的恢复能力，那么领域才终于有证据表明它是在从失败中学习，而不只是绕着失败过滤。

### Grounded verification that is aware of carrier type

### 感知载体类型的 有依托 验证


The current literature uses one broad idea too uniformly: ask an LLM judge whether the transformed artifact looks right. The next step is not simply better judges. It is verification that matches the carrier being validated. Step-level traces, summarized tasks, rubrics, and simulated environments each fail in different ways. Explorer and AgentSynth both show that near-correct or hallucinated summaries can pass a judge too easily \[Pah25, Xie25e\]. Structured Distillation shows that the judge often needs privileged evaluation hints because the raw trajectory is too ambiguous \[Lu26\]. ToolMind shows that a trajectory that is acceptable globally may still contain bad turns \[Yan25ab\]. COVERT makes the boundary explicit by separating exact-verifiable from judge-assisted augmentations and admitting that the latter remain under-validated against humans \[Xu26e\].

当前文献过于统一地使用一个宽泛想法：询问 大语言模型 裁判器被转化工件看起来是否正确。下一步不只是更好的裁判器，而是与被验证载体匹配的验证。步骤级轨迹、摘要任务、评分规程 和模拟环境各自以不同方式失败。探索系统 和 任务合成方法 都显示，近似正确或带幻觉的摘要很容易通过裁判器 \[Pah25, Xie25e\]。结构化蒸馏 显示，裁判器常需要特权评估提示，因为原始轨迹太歧义 \[Lu26\]。工具数据集方法 显示，全局可接受的轨迹仍可能包含坏轮次 \[Yan25ab\]。可控工具合成方法 通过区分精确可验证增强和裁判器辅助增强来明确边界，并承认后者仍缺少人类验证 \[Xu26e\]。

A better research program would validate each carrier at the level where its errors live. Summarized tasks should be checked against omitted and added constraints. Step-level traces should be checked for local causal correctness, not just final success. Rubrics should be tested by counterfactual execution of subgoal and forbidden-behavior rules. Mock environments should be audited for state consistency across repeated calls, not just for answer plausibility. Progress would be visible when papers report not one judge accuracy number but a carrier-specific validation profile. That would also make cross-paper comparisons much cleaner for a survey discussion.

更好的研究计划应在每种载体错误发生的层面验证它。摘要任务应检查遗漏和新增约束。步骤级轨迹应检查局部因果正确性，而不只是最终成功。评分规程 应通过反事实执行子目标和禁忌行为规则来测试。模拟环境应审计重复调用中的状态一致性，而不只是答案看起来是否合理。进展会体现为论文报告载体特定验证画像，而非单一裁判器准确率。那也会让 survey 中的跨论文比较更清晰。

### Adaptive carrier granularity

### 自适应载体粒度


The literature already suggests that no single carrier granularity is best. Structured Distillation shows that reasoning traces help only when they remain coherent \[Lu26\]. SYNTHAGENT shows that underspecified tasks can be better learning carriers than fully explicit workflows because they preserve a useful information gap \[Lu26j\]. AgentSynth demonstrates the power of summarizing many easy subtasks into one hard task, but also exposes how much control is lost when this summary gets too far from the underlying procedure \[Xie25e\]. ToolMind indicates that trajectory-level filtering misses turn-level errors \[Yan25ab\]. TOUCAN and ToolACE both show that adding new carrier dimensions such as personas or multi-type data can help some competencies and hurt others \[Xu25o, Liu24o\].

文献已经暗示没有单一载体粒度总是最好。结构化蒸馏 显示，推理轨迹只有在保持连贯时才有帮助 \[Lu26\]。合成智能体方法 显示，欠指定任务可以比完全显式工作流更适合作为学习载体，因为它们保留了有用信息缺口 \[Lu26j\]。任务合成方法 展示了把许多简单子任务摘要成一个困难任务的威力，但也暴露出当摘要离底层过程太远时会失去多少控制 \[Xie25e\]。工具数据集方法 表明轨迹级过滤会漏掉轮次级错误 \[Yan25ab\]。工具数据合成方法 和 函数调用方法 都显示，添加 persona 或多类型数据等新载体维度可以帮助某些能力，同时损害另一些能力 \[Xu25o, Liu24o\]。

Inference. The natural next step is a system that does not commit to one carrier too early. It should decide whether a given episode is best preserved as a raw trace, a constraint-satisfying prefix, a summarized instruction, a rubric, or a reward model target. Verification should then test not only whether the downstream agent improves, but whether the chosen carrier was more sample-efficient and more robust than the alternatives for that class of interaction. That would move the field from ad hoc carrier design toward carrier selection as a learned or at least benchmarked decision.

推断。自然的下一步是构建不太早承诺单一载体的系统。它应决定一个给定 片段 最适合被保存为原始轨迹、满足约束的前缀、摘要指令、评分规程，还是奖励模型目标。验证随后不仅应测试下游智能体是否改进，还应测试所选载体在该类交互上是否比替代方案更具样本效率和鲁棒性。这会把领域从临时载体设计推进到把载体选择作为可学习、至少可基准化的决策。

### More stateful and cross-system synthetic environments

### 更有状态、跨系统的合成环境


Synthetic environments have already moved the field forward, but they now need to grow along the axes they currently simplify away. EviPath and RAGShaper both show the value of structured retrieval worlds, yet both rely on heavily controlled evidence spaces \[Li25at, Tao26\]. ASTRA creates executable arenas but still restricts composition to tools within a single MCP server and approximates failure by injecting it at a fixed rate \[Tia26\]. COVERT explicitly attributes its long-horizon plateau to the lack of tightly coupled stateful dependencies \[Xu26e\]. Wang et al. document context-fusion failures in UI simulation, showing that even when the simulator has the right local pieces, it can carry forward the wrong global state \[Wan25as\]. FABRIC notes that conditional branching and long-term memory traces remain future work rather than present capability \[Ver25b\].

合成环境已经推动了领域前进，但它们现在需要沿着当前被简化掉的轴增长。证据路径方法 和 检索增强塑形方法 都显示了结构化检索世界的价值，但二者都依赖高度受控的证据空间 \[Li25at, Tao26\]。场域合成方法 创建可执行场域，但仍把组合限制在单个 模型上下文协议服务器 内的工具，并通过固定速率注入来近似失败 \[Tia26\]。可控工具合成方法 明确把其长时程平台期归因于缺少紧密耦合的有状态依赖 \[Xu26e\]。相关工作 记录了 UI 模拟中的上下文融合失败，显示即便模拟器拥有正确局部组件，也可能携带错误全局状态 \[Wan25as\]。智能体数据生成框架 指出，条件分支和长期记忆轨迹仍是未来工作，而非当前能力 \[Ver25b\]。

Concrete progress would look like synthetic carriers that preserve mutable state over many turns, allow cross-server or cross-tool composition, and model failures that are conditional rather than random. A useful benchmark would vary only the statefulness of the environment while keeping the high-level task family fixed. If a carrier design improves short-turn robustness but still collapses when earlier tool outputs constrain later legal actions, then the field would have a cleaner diagnosis than today’s broad “long horizon remains hard.”

实际进展应体现为合成载体能在多轮中保留可变状态、允许跨 服务器 或跨工具组合，并建模条件性而非随机性失败。有用基准可以在保持高层任务族固定的同时，只变化环境有状态性。如果一种载体设计改进了短轮次鲁棒性，却在早期工具输出约束后续合法动作时仍然崩溃，那么领域会获得比今天笼统“长时程仍困难”更清楚的诊断。

### Cross-carrier transfer studies

### 跨载体迁移研究


For a survey on experience transformation itself, a major missing line of work is direct comparison across carrier conversions. InSTA already contains a natural experiment when its live-web data are converted to static benchmark format and reasoning traces are dropped \[Tra25\]. Fara-7B contains another when DOM-grounded synthetic supervision is consumed by a pixel-only student \[Awa25\]. Structured Distillation raises the same question in a more favorable setting by showing that some traces transfer well, but only when they preserve coherence \[Lu26\]. ToolACE reveals a broader tradeoff in which function-calling specialization can coincide with weaker general reasoning \[Liu24o\]. COVERT adds prompt-format sensitivity, showing that a capability learned in one prompt-carrier interface may appear to disappear in another \[Xu26e\].

对经验转化 survey 而言，一条主要缺失工作线是对不同载体转换进行直接比较。互联网规模训练方法 在其 实时网页 数据被转为静态基准格式且推理轨迹被丢弃时，已经包含一个自然实验 \[Tra25\]。七十亿参数模型 在 DOM-有依托 合成监督被像素学生消费时包含另一个自然实验 \[Awa25\]。结构化蒸馏 在更有利设置中提出同一问题，显示某些轨迹可以很好迁移，但前提是保持连贯 \[Lu26\]。函数调用方法 揭示了更广泛权衡：函数调用专门化可能伴随较弱一般推理 \[Liu24o\]。可控工具合成方法 补充了提示格式敏感性，显示在一种提示-载体接口中学到的能力，可能在另一种接口中似乎消失 \[Xu26e\]。

A strong future paper would take a fixed set of underlying interactions and convert them into at least three carrier forms such as full traces, summarized tasks, and rubric-based rewards. It would then train or evaluate the same base agent under matched budgets. That design would let the field ask questions it currently mostly avoids. Which parts of experience survive conversion best. Which carrier is most robust to prompt changes. Which carrier helps a weaker student versus a stronger one. Right now these comparisons are usually implicit across different papers. They need to become explicit within the same experiment.

强未来论文应取一组固定底层交互，并将它们转为至少三种载体形式，例如完整轨迹、摘要任务和基于 评分规程 的奖励。随后在匹配预算下训练或评估同一基础智能体。该设计会让领域提出目前大多回避的问题：经验的哪些部分最能承受转换；哪种载体对提示变化最鲁棒；哪种载体帮助较弱学生或较强学生。当前这些比较通常隐含地分散在不同论文之间。它们需要进入同一实验。

### Cost-aware carrier design

### 成本感知载体设计


The last direction is methodological rather than purely algorithmic, but it is overdue. Many of the most consequential carrier decisions in this set are already cost decisions. Explorer filters trajectories with too many scrolls partly because long interaction is expensive and noisy \[Pah25\]. TOUCAN rejects large fractions of real-world tools because credentialing and stable execution are too costly \[Xu25o\]. Fara-7B shows that verified successful trajectories are expensive because most attempts fail long before they become reusable data \[Awa25\]. OpenMobile’s error-recovery traces depend on a powerful monitor \[Che26d\]. WebSTAR shows that stricter thresholds increase cost sharply \[He25g\]. ASTRA highlights executable arena synthesis as a computational bottleneck \[Tia26\].

最后一个方向偏方法学，但已经迟到。这一组中许多最重要载体决策本来就是成本决策。探索系统 过滤滚动过多的轨迹，部分原因是长交互昂贵且有噪声 \[Pah25\]。工具数据合成方法 拒绝大量真实世界工具，因为凭证和稳定执行成本太高 \[Xu25o\]。七十亿参数模型 显示已验证成功轨迹昂贵，因为多数尝试在成为可复用数据前很早就失败 \[Awa25\]。开放移动智能体方法 的错误恢复轨迹依赖强大监控器 \[Che26d\]。步骤过滤方法 显示，更严格阈值会显著提高成本 \[He25g\]。场域合成方法 强调可执行场域合成是计算瓶颈 \[Tia26\]。

Concrete progress would look like reporting carrier utility per unit cost. That means not just task success, but validated success gained per rollout dollar, judge call, simulator token, or human audit hour. It also means comparing carriers under equal budget, not only equal sample count. A carrier that is slightly weaker but ten times cheaper to validate may be the better research direction if it enables much broader environment coverage. Today that tradeoff is usually buried in appendices. It should become first-class evidence.

实际进展应体现为报告单位成本下的载体效用。这不仅意味着任务成功，还包括每单位采样美元、裁判器调用、模拟器 词元 或人类审计小时获得的已验证成功增益。它也意味着在相同预算下比较载体，而不只在相同样本数下比较。一个稍弱但验证成本低十倍的载体，如果能覆盖更广泛环境，可能是更好的研究方向。今天，这种权衡通常埋在附录中。它应成为一阶证据。

---

## References

\[Pah25\] V. Pahuja *et al.*, “Explorer: Scaling Exploration-driven Web Trajectory Synthesis for Multimodal Web Agents,” *Annual Meeting of the Association for Computational Linguistics*, pp. 6300–6323, Feb. 2025, doi: [10.48550/arXiv.2502.11357](https://doi.org/10.48550/arXiv.2502.11357).

\[Tra25\] B. Trabucco, G. Sigurdsson, R. Piramuthu, and R. Salakhutdinov, “Towards Internet-Scale Training For Agents,” *ArXiv*, vol. abs/2502.06776, Feb. 2025, doi: [10.48550/arXiv.2502.06776](https://doi.org/10.48550/arXiv.2502.06776).

\[Wan25as\] Y. Wang *et al.*, “LLMs as Scalable, General-Purpose Simulators For Evolving Digital Agent Training,” *ArXiv*, vol. abs/2510.14969, Oct. 2025, doi: [10.48550/arXiv.2510.14969](https://doi.org/10.48550/arXiv.2510.14969).

\[Xie25e\] J. Xie, D. Xu, X. Zhao, and D. Song, “AgentSynth: Scalable Task Generation for Generalist Computer-Use Agents,” *ArXiv*, vol. abs/2506.14205, Jun. 2025, doi: [10.48550/arXiv.2506.14205](https://doi.org/10.48550/arXiv.2506.14205).

\[Log26b\] L. Logeswaran, J. Kim, S. Sohn, C. Glasscock, and H. Lee, “Scaling Web Agent Training through Automatic Data Generation and Fine-grained Evaluation,” *ArXiv*, vol. abs/2602.12544, Feb. 2026, doi: [10.48550/arXiv.2602.12544](https://doi.org/10.48550/arXiv.2602.12544).

\[Pra25b\] A. Prabhakar *et al.*, “APIGen-MT: Agentic Pipeline for Multi-Turn Data Generation via Simulated Agent-Human Interplay,” *ArXiv*, vol. abs/2504.03601, Apr. 2025, doi: [10.48550/arXiv.2504.03601](https://doi.org/10.48550/arXiv.2504.03601).

\[Liu24n\] Z. Liu *et al.*, “APIGen: Automated Pipeline for Generating Verifiable and Diverse Function-Calling Datasets,” *ArXiv*, vol. abs/2406.18518, Jun. 2024, doi: [10.48550/arXiv.2406.18518](https://doi.org/10.48550/arXiv.2406.18518).

\[Awa25\] A. Awadallah *et al.*, “Fara-7B: An Efficient Agentic Model for Computer Use,” *ArXiv*, vol. abs/2511.19663, Nov. 2025, doi: [10.48550/arXiv.2511.19663](https://doi.org/10.48550/arXiv.2511.19663).

\[Wei26b\] J. Wei, Y. Zhao, K. Ni, and A. Cohan, “ANCHOR: Branch-Point Data Generation for GUI Agents,” *ArXiv*, vol. abs/2602.07153, Feb. 2026, doi: [10.48550/arXiv.2602.07153](https://doi.org/10.48550/arXiv.2602.07153).

\[Xu26e\] S. Xu *et al.*, “Controllable and Verifiable Tool-Use Data Synthesis for Agentic Reinforcement Learning,” Apr. 10, 2026.

\[He25g\] Y. He, P. Chawla, Y. Souri, S. Som, and X. Song, “Scalable Data Synthesis for Computer Use Agents with Step-Level Filtering,” *ArXiv*, vol. abs/2512.10962, Nov. 2025, doi: [10.48550/arXiv.2512.10962](https://doi.org/10.48550/arXiv.2512.10962).

\[Che26d\] K. Cheng *et al.*, “OpenMobile: Building Open Mobile Agents with Task and Trajectory Synthesis,” Apr. 16, 2026.

\[Tao26\] Z. Tao *et al.*, “RAGShaper: Eliciting Sophisticated Agentic RAG Skills via Automated Data Synthesis,” *ArXiv*, vol. abs/2601.08699, Jan. 2026, doi: [10.48550/arXiv.2601.08699](https://doi.org/10.48550/arXiv.2601.08699).

\[Yan25x\] H. Yan *et al.*, “Step-GUI Technical Report,” *ArXiv*, vol. abs/2512.15431, Dec. 2025, doi: [10.48550/arXiv.2512.15431](https://doi.org/10.48550/arXiv.2512.15431).

\[Lu26\] X. H. Lù and S. Reddy, “Structured Distillation of Web Agent Capabilities Enables Generalization,” Apr. 09, 2026.

\[Lu26j\] Y.-J. Lü, C. Wang, L. Shen, J. Huang, and T. Xu, “Mock Worlds, Real Skills: Building Small Agentic Language Models with Synthetic Tasks, Simulated Environments, and Rubric-Based Rewards,” *ArXiv*, vol. abs/2601.22511, Jan. 2026, doi: [10.48550/arXiv.2601.22511](https://doi.org/10.48550/arXiv.2601.22511).

\[Yan25ab\] C. Yang *et al.*, “ToolMind Technical Report: A Large-Scale, Reasoning-Enhanced Tool-Use Dataset,” *ArXiv*, vol. abs/2511.15718, Nov. 2025, doi: [10.48550/arXiv.2511.15718](https://doi.org/10.48550/arXiv.2511.15718).

\[Xu25o\] Z. Xu *et al.*, “TOUCAN: Synthesizing 1.5M Tool-Agentic Data from Real-World MCP Environments,” *ArXiv*, vol. abs/2510.01179, Oct. 2025, doi: [10.48550/arXiv.2510.01179](https://doi.org/10.48550/arXiv.2510.01179).

\[Liu24o\] W. Liu *et al.*, “ToolACE: Winning the Points of LLM Function Calling,” *ArXiv*, vol. abs/2409.00920, Sep. 2024, doi: [10.48550/arXiv.2409.00920](https://doi.org/10.48550/arXiv.2409.00920).

\[Li25at\] M. Li *et al.*, “From Evidence to Trajectory: Abductive Reasoning Path Synthesis for Training Retrieval-Augmented Generation Agents,” *ArXiv*, vol. abs/2509.23071, Sep. 2025, doi: [10.48550/arXiv.2509.23071](https://doi.org/10.48550/arXiv.2509.23071).

\[Tia26\] X. Tian *et al.*, “ASTRA: Automated Synthesis of agentic Trajectories and Reinforcement Arenas,” *ArXiv*, vol. abs/2601.21558, Jan. 2026, doi: [10.48550/arXiv.2601.21558](https://doi.org/10.48550/arXiv.2601.21558).

\[Ver25b\] A. Verma, S. Subramanian, N. Kandasamy, and N. Gupta, “FABRIC: Framework for Agent-Based Realistic Intelligence Creation,” *ArXiv*, vol. abs/2510.17995, Oct. 2025, doi: [10.48550/arXiv.2510.17995](https://doi.org/10.48550/arXiv.2510.17995).

\[Wan25ar\] Z. Wang *et al.*, “SynthAgent: Adapting Web Agents with Synthetic Supervision,” Nov. 08, 2025.
