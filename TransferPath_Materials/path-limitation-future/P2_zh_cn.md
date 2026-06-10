# Experience transformation research gaps

# 经验转化研究缺口

## Table of Contents

- [Experience transformation research gaps](#experience-transformation-research-gaps)
  - [Table of Contents](#table-of-contents)
  - [Challenges](#challenges)
    - [Abstraction unit is still unstable](#abstraction-unit-is-still-unstable)
    - [Retrieval is a source of negative transfer, not just missed opportunity](#retrieval-is-a-source-of-negative-transfer-not-just-missed-opportunity)
    - [Validation is weak and often circular](#validation-is-weak-and-often-circular)
    - [Failure is still poorly transformed](#failure-is-still-poorly-transformed)
    - [Static artifacts break in dynamic environments](#static-artifacts-break-in-dynamic-environments)
    - [Reflecting on experience is itself model-scale sensitive](#reflecting-on-experience-is-itself-model-scale-sensitive)
    - [Lifecycle management is mostly heuristic](#lifecycle-management-is-mostly-heuristic)
    - [Evaluation still lags behind the claims](#evaluation-still-lags-behind-the-claims)
  - [Future directions](#future-directions)
    - [Adaptive multi-granular experience](#adaptive-multi-granular-experience)
    - [Applicability-aware retrieval and controlled fallback](#applicability-aware-retrieval-and-controlled-fallback)
    - [Grounded validation and causal attribution](#grounded-validation-and-causal-attribution)
    - [Failure-native memory design](#failure-native-memory-design)
    - [Lifecycle-aware repositories](#lifecycle-aware-repositories)
    - [Cross-model and cross-domain transfer with interface adaptation](#cross-model-and-cross-domain-transfer-with-interface-adaptation)
    - [Multimodal and grounded state abstractions](#multimodal-and-grounded-state-abstractions)
    - [Better artifact-level benchmarks](#better-artifact-level-benchmarks)
  - [References](#references)

## Challenges

## 挑战

| Challenge | What keeps recurring | Representative anchors |
|:---|:---|:---|
| Abstraction unit is still unstable | The literature does not yet know when experience should remain a note, become a workflow, compile into a skill, or be elevated to a subagent or graph | \[Wan25d\], \[Fan25\], \[Liu26\], \[Qiu26\], \[Cha20\] |
| Retrieval is a source of negative transfer, not just missed opportunity | More memory often hurts once relevance and applicability are imperfect | \[Wan24\], \[Fan25\], \[Cao25\], \[Mi26\], \[Zha25\] |
| Validation is weak and often circular | Many systems rely on self-judgment, exception-free execution, or narrow structural checks rather than grounded success tests | \[Wan23c\], \[Zhe25c\], \[Wan25d\], \[Zha25c\], \[Cao25\] |
| Failure is still poorly transformed | Most pipelines remain success-biased, and failure-derived updates are unstable unless heavily filtered | \[Tan26\], \[Cao25\], \[Ni26\], \[Mi26\], \[Ma26\] |
| Static artifacts break in dynamic environments | Web, GUI, and embodied settings change faster than current memories can adapt | \[Wan24\], \[Tan26\], \[Fen26\], \[Liu25i\], \[Lee23\] |
| Reflecting on experience is itself model-scale sensitive | Strong executors are not always strong skill authors, and weaker models can be overburdened by richer memories | \[Wan23c\], \[Zhe25c\], \[Wan26d\], \[Ni26\], \[Xu25b\] |
| Lifecycle management is mostly heuristic | Pruning, merging, revision, and retirement are driven by hand-tuned thresholds with little theory | \[For25\], \[Qiu26\], \[Mi26\], \[Ma26\], \[Liu25i\] |
| Evaluation still lags behind the claims | Workflow quality, graph fidelity, design cost, and long-run maintenance are rarely measured directly | \[Wei26\], \[Liu26\], \[Ano24\], \[Jo26\], \[Zha25c\] |

| 挑战 | 反复出现的现象 | 代表性锚点 |
|:---|:---|:---|
| 抽象单元仍不稳定 | 文献尚不清楚经验何时应保持为笔记、何时应变成工作流、何时应编译为技能，或何时应提升为子智能体或图 | \[Wan25d\], \[Fan25\], \[Liu26\], \[Qiu26\], \[Cha20\] |
| 检索是负迁移来源，而不只是错失机会 | 当相关性和适用性不完美时，更多记忆常会带来损害 | \[Wan24\], \[Fan25\], \[Cao25\], \[Mi26\], \[Zha25\] |
| 验证薄弱且常呈循环性 | 许多系统依赖自我判断、无异常执行或狭窄结构检查，而不是有环境根基的成功测试 | \[Wan23c\], \[Zhe25c\], \[Wan25d\], \[Zha25c\], \[Cao25\] |
| 失败仍未被良好转化 | 多数流水线仍偏向成功样本，失败派生更新若未经重度过滤则不稳定 | \[Tan26\], \[Cao25\], \[Ni26\], \[Mi26\], \[Ma26\] |
| 静态产物会在动态环境中失效 | 网页、图形界面和具身设置的变化快于当前记忆的适配速度 | \[Wan24\], \[Tan26\], \[Fen26\], \[Liu25i\], \[Lee23\] |
| 对经验的反思本身受模型规模影响 | 强执行器并不总是强技能作者，较弱模型可能被更丰富的记忆压垮 | \[Wan23c\], \[Zhe25c\], \[Wan26d\], \[Ni26\], \[Xu25b\] |
| 生命周期管理大多依赖启发式 | 剪枝、合并、修订和退役由手工调节阈值驱动，理论基础很少 | \[For25\], \[Qiu26\], \[Mi26\], \[Ma26\], \[Liu25i\] |
| 评估仍落后于主张 | 工作流质量、图保真度、设计成本和长期维护很少被直接测量 | \[Wei26\], \[Liu26\], \[Ano24\], \[Jo26\], \[Zha25c\] |

### Abstraction unit is still unstable

### 抽象单元仍不稳定

The field has shown that raw trajectories are rarely the right long-term carrier, but it has not settled the unit of transformation. In \[Wan25d\], the paper explicitly treats skill granularity as an open question in Section 7, while its induction prompt quietly imposes a heuristic skill size cap in Appendix A.2. \[Fan25\] reaches a different answer from \[Wan25d\]: scripts alone help transfer, trajectories alone help execution fidelity, and the best results come from keeping both, with Figure 5 and the analysis section showing a non-monotonic relation between retrieved memory volume and success. \[Liu26\] makes the problem even sharper. Appendix E.2 shows that successful execution is not enough for correct workflow generation, because many successful runs still fail to translate into a faithful graph. \[Qiu26\] then splits reusable expertise into two different objects, skills and subagents, but Appendix A.2 admits that the classification boundary between them is not systematically evaluated. Older work in \[Cha20\] had already exposed the same issue in a different language. Section 4.2.3 relies on a tuned similarity threshold to decide whether two traces represent the same workflow state, which is another way of saying that abstraction granularity is doing most of the conceptual work.

该领域已经显示，原始轨迹很少是合适的长期载体，但尚未确定转化单元。在 \[Wan25d\] 中，论文第 7 节明确把技能粒度视为开放问题，而附录 A.2 的归纳提示又悄悄施加了启发式技能大小上限。\[Fan25\] 给出了不同于 \[Wan25d\] 的答案：单独脚本有助于迁移，单独轨迹有助于执行保真度，最好结果来自同时保留二者；图 5 和分析部分显示，检索记忆量与成功率之间存在非单调关系。\[Liu26\] 使问题更加尖锐。附录 E.2 显示，成功执行并不足以生成正确工作流，因为许多成功运行仍无法转化为忠实图。\[Qiu26\] 随后将可复用专长拆成技能和子智能体两个不同对象，但附录 A.2 承认二者的分类边界没有被系统评估。更早的 \[Cha20\] 已经用另一种语言暴露了同一问题。第 4.2.3 节依赖调节后的相似度阈值来判断两条轨迹是否表示同一工作流状态，这等于说抽象粒度承担了大部分概念工作。

What matters for the survey is that these are not cosmetic representation choices. They determine what can be retrieved, verified, transferred, or maintained. A workflow that is too abstract omits exception cases. A programmatic skill that is too concrete overfits interface details. A subagent can preserve procedural logic but adds orchestration overhead. This report treats the broader claim that the field lacks a principled abstraction criterion as an inference, but it is strongly supported by the fact that different papers succeed only after choosing different units of experience and often fail when they push one level too far \[Wan25d, Fan25, Liu26, Qiu26, Cha20\].

对综述而言，关键在于这些并非表层表示选择。它们决定什么可以被检索、验证、迁移或维护。过于抽象的工作流会遗漏例外情形。过于具体的程序化技能会过拟合界面细节。子智能体可以保留程序逻辑，但会增加编排开销。本文档把“该领域缺少原则性抽象标准”这一较宽主张视为推断，但这个推断有强支撑：不同论文往往只有在选择不同经验单元后才成功，而当某一层级被推得过远时又常会失败 \[Wan25d, Fan25, Liu26, Qiu26, Cha20\]。

### Retrieval is a source of negative transfer, not just missed opportunity

### 检索是负迁移来源，而不只是错失机会

A recurring hidden result is that memory can actively hurt. \[Wan24\] reports in Table 11 that offline and online workflow memories do not compose cleanly. The combined setting underperforms the better single-source setting, which means extra experience can reduce rather than increase utility. \[Fan25\] shows the same pattern from another angle. Figure 5 indicates that performance rises only until retrieval reaches a moderate size, then flattens or declines as less accurate or less relevant memories enter context. \[Cao25\] replicates this with a different memory design. Figure 4 and Table 3 show that retrieving more experiences is not monotonically helpful, and the paper’s own limitation section notes that retrieval occurs only once at task start, which makes initial mistakes persist through the whole episode. \[Mi26\] is even more direct. Table 3 shows that replacing score-based maintenance with FIFO causes a collapse in long-run performance, and the paper frames this as evidence that unregulated accumulation creates a toxic procedural prior. In the multi-agent setting, \[Zha25\] finds that expanding the retrieval neighborhood from one hop to two or three hops degrades performance because the additional context is semantically related but not decision-relevant.

一个反复出现的隐性结果是，记忆会主动造成伤害。\[Wan24\] 在表 11 中报告，离线与在线工作流记忆无法干净组合。组合设置弱于更好的单来源设置，意味着额外经验可能降低而非提升效用。\[Fan25\] 从另一角度显示相同模式。图 5 表明，性能只在检索达到适中规模前上升，随后当准确性较低或相关性较弱的记忆进入上下文时趋平或下降。\[Cao25\] 用不同记忆设计复现了这一点。图 4 和表 3 显示，检索更多经验并非单调有益，论文自身 limitations 部分还指出，检索只在任务开始时发生一次，这会使初始错误贯穿整个回合。\[Mi26\] 更直接。表 3 显示，用先进先出替代基于得分的维护会造成长期性能崩塌，论文将其解释为无调节积累会制造有毒程序性先验。在多智能体设置中，\[Zha25\] 发现，将检索邻域从一跳扩展到两跳或三跳会降低性能，因为额外上下文虽有语义相关性，却与决策无关。

This matters because many papers still narrate retrieval as a support module. The evidence says it is often the main failure point. The literature is moving from the question of whether to remember toward the question of how to estimate applicability, downside risk, and interruption conditions before retrieved experience is allowed to shape action. That is especially clear in \[Tan26\], where a confidence-aware fallback is necessary to avoid committing to a low-confidence branch, and in \[Wan26d\], where the Skill Graph is valuable largely because it narrows retrieval to context that is more likely to execute cleanly.

这一点重要，因为许多论文仍把检索叙述为支持模块。证据显示，它往往是主要失败点。文献正在从“是否记忆”的问题转向另一个问题：在允许检索经验塑造动作之前，如何估计适用性、下行风险和中断条件。\[Tan26\] 中这一点尤其清楚：置信度感知回退对于避免投入低置信分支是必要的；在 \[Wan26d\] 中，技能图之所以有价值，很大程度上是因为它把检索收窄到更可能干净执行的上下文。

### Validation is weak and often circular

### 验证薄弱且常呈循环性

Several papers quietly reveal that the hardest part of experience transformation is not extraction but deciding whether the extracted artifact is true. \[Zhe25c\] gives the clearest hidden negative result. Appendix D.2.1 shows that a function can be marked as verified merely by executing without an exception, even when it achieves nothing semantically useful. \[Wan23c\] reports in Section 4 that its self-verification can miss obvious environment-grounded failures, such as not recognizing the right success signal. \[Wan25d\] depends on an LM evaluator both to identify good source episodes and to verify induced skills, and Section 2.3 adds a rewritten trajectory prefix partly because the induced skill might not be used spontaneously enough to test itself cleanly. \[Zha25c\] shows the same circularity at the workflow level. Appendix C reports that adding a Validator operator reduced performance when it relied on self-model judgment rather than environmental feedback. \[Cao25\] also acknowledges in Section 5 that LLM validation may miss nuanced aspects of experience quality.

多篇论文隐性揭示，经验转化最难的部分不是抽取，而是判断抽取得到的产物是否真实。\[Zhe25c\] 给出了最清楚的隐性负结果。附录 D.2.1 显示，一个函数可能仅因执行时没有异常就被标为已验证，即便它没有实现任何语义上有用的事情。\[Wan23c\] 在第 4 节报告，其自验证会漏掉明显有环境根基的失败，例如没有识别正确成功信号。\[Wan25d\] 同时依赖语言模型评估器来识别优质源回合和验证归纳技能，第 2.3 节加入重写轨迹前缀，部分原因是归纳技能可能不会足够自发地被使用，导致难以干净测试自身。\[Zha25c\] 在工作流层面显示了同样的循环性。附录 C 报告称，当 Validator 算子依赖自模型判断而非环境反馈时，加入它反而降低性能。\[Cao25\] 也在第 5 节承认，大型语言模型验证可能漏掉经验质量的细微方面。

The deeper issue is that many memory systems still validate transformed experience with another model artifact derived from the same epistemic source. That creates correlated error. A bad skill can pass because the verifier shares the generator’s blind spot. A brittle workflow can look coherent because the judge rewards plausible structure rather than executable correctness. \[Fen26\] points directly toward the missing alternative in Section 5.5, where the authors argue that descriptive preconditions and effects should be replaced with grounded state observations for real-time validation. Until validation is environment-backed, many gains will remain vulnerable to silent memory pollution.

更深层问题是，许多记忆系统仍用来自同一认知来源的另一个模型产物来验证转化经验。这会造成相关错误。坏技能可能通过，因为验证器共享生成器的盲点。脆弱工作流可能看起来连贯，因为裁判器奖励合理结构，而非可执行正确性。\[Fen26\] 在第 5.5 节直接指向缺失的替代方案，作者主张用有根基的状态观察替代描述性前置条件和效果，以支持实时验证。在验证获得环境支撑前，许多增益仍会暴露于静默记忆污染。

### Failure is still poorly transformed

### 失败仍未被良好转化

The field often claims to learn from failure, but most current systems are still success-biased in what they ultimately preserve. \[Tan26\] builds its hierarchical memory only from successful trajectories in both offline and online settings. \[Cao25\] shows why this bias persists: Table 3 finds that selective addition outperforms full addition, meaning naive inclusion of all experiences injects too much noise. The same paper adds failure-aware reflection, but only after strong filtering and validation. \[Ni26\] offers a useful disagreement here. Section 3.2 reports that success-derived patches are less stable than error-driven updates, and some success-based updates even fall below baseline. That is not evidence that failure is easy to use. It is evidence that current success extraction is often extracting lucky specifics rather than reusable logic. \[Mi26\] depends on hindsight attribution to decide whether initiation, policy, or termination failed, which means failure transformation is only as good as the diagnosing model. \[Ma26\] also suggests a gap between memory-guided action correction and high-level reasoning. Figure 4 shows that BrainMem reduces procedural failures but leaves wrong termination decisions as a large residual category.

该领域常声称从失败中学习，但多数当前系统在最终保留内容上仍偏向成功样本。\[Tan26\] 在离线和在线设置中都只从成功轨迹构建层级记忆。\[Cao25\] 显示了这种偏向为何持续存在：表 3 发现选择性添加优于全量添加，意味着朴素纳入所有经验会注入过多噪声。同一论文加入失败感知反思，但前提是强过滤和验证。\[Ni26\] 在这里提供了有用的不同意见。第 3.2 节报告称，成功派生补丁不如错误驱动更新稳定，一些基于成功的更新甚至低于基线。这并非失败易用的证据，而是说明当前成功抽取常在抽取幸运细节，而非可复用逻辑。\[Mi26\] 依赖后见归因来判断启动、策略还是终止失败，这意味着失败转化的质量受限于诊断模型。\[Ma26\] 也提示，记忆引导的动作修正与高层推理之间存在缺口。图 4 显示，BrainMem 减少了程序性失败，但错误终止决策仍是很大的残余类别。

Taken together, the literature suggests that failure is highly informative but structurally harder to transform than success. Current systems either avoid it, sanitize it heavily, or use it only as contrastive evidence. A mature failure-native pipeline would need to separate failure cause, failed context, attempted repair, and validated fix. That broader claim is an inference, but it follows from the repeated pattern that raw failure experience is too noisy to store directly while filtered failure signals are among the most valuable updates once cleaned \[Cao25, Ni26, Mi26, Ma26\].

合在一起看，文献提示失败信息量很高，但在结构上比成功更难转化。当前系统要么回避它，要么强力清洗它，要么只把它用作对比证据。成熟的失败原生流水线需要分离失败原因、失败上下文、尝试修复和已验证修复。这个较宽主张是一种推断，但它来自一个反复模式：原始失败经验噪声太大，无法直接存储；经过清洗后，过滤失败信号又属于最有价值的更新 \[Cao25, Ni26, Mi26, Ma26\]。

### Static artifacts break in dynamic environments

### 静态产物会在动态环境中失效

Much of the strongest empirical work is in settings where the environment changes enough to expose brittleness but not enough to make learning impossible. \[Wan24\] shows in Figure 7 that static workflows fail when live web interaction inserts unexpected pop-ups or branches that were not part of the induced sequence. \[Tan26\] surfaces a closely related failure in modern single-page applications. Section IV-F and Figure 6 show that URL-based or reload-based verification cannot detect meaningful progress when the page changes without a navigation event. \[Fen26\] makes the same simplifying assumption at map construction time. Section 4 relies on deterministic URL normalization to define contexts, and Section 5.5 explicitly warns that maps become stale as web environments evolve. \[Liu25i\] uses XML-level correctness checks and rollback, which works only when UI structures remain stable enough for exact structural comparison. \[Lee23\] reveals the boundary case on mobile. Section 9 shows that apps without reliable accessibility representations, including Flutter apps and image-heavy interfaces, fall outside the method’s competence.

许多最强实证工作位于这样的设置中：环境变化足以暴露脆弱性，但又不足以让学习变得不可能。\[Wan24\] 在图 7 中显示，当实时网页交互插入不属于归纳序列的意外弹窗或分支时，静态工作流会失败。\[Tan26\] 在现代单页应用中暴露了密切相关的失败。第 IV-F 节和图 6 显示，当页面在没有导航事件的情况下变化时，基于 URL 或重载的验证无法检测有意义的进展。\[Fen26\] 在构建地图时作出相同简化假设。第 4 节依赖确定性 URL 归一化来定义上下文，第 5.5 节明确警告，随着网页环境演化，地图会变旧。\[Liu25i\] 使用 XML 层级正确性检查和回滚，这只有在界面结构稳定到足以进行精确结构比较时才有效。\[Lee23\] 揭示了移动端边界案例。第 9 节显示，缺少可靠无障碍表示的应用，包括 Flutter 应用和图像密集界面，超出该方法能力范围。

The literature therefore still treats transformed experience as more durable than it really is. Many artifacts are snapshots of local regularities rather than robust knowledge. The open problem is not just adaptation after drift. It is encoding what kinds of changes should invalidate a memory in the first place. That gap appears in web workflows, mobile app memory, environment maps, and skill libraries alike \[Wan24, Tan26, Fen26, Liu25i, Lee23\].

因此，文献仍把转化后的经验看得比实际更持久。许多产物只是局部规律快照，而非鲁棒知识。开放问题不只是漂移后的适配，而是首先要编码哪些变化应使记忆失效。这个缺口同时出现在网页工作流、移动应用记忆、环境地图和技能库中 \[Wan24, Tan26, Fen26, Liu25i, Lee23\]。

### Reflecting on experience is itself model-scale sensitive

### 对经验的反思本身受模型规模影响

The ability to use experience and the ability to distill it are not the same capability. \[Wan23c\] already showed a strong dependence on the base model, with Figure 9 reporting a large drop from GPT-4 to GPT-3.5 in open-ended skill discovery. \[Zhe25c\] finds a similar split between author and user. Section 4.3 shows that strong agents can synthesize APIs that weaker agents benefit from, but weaker agents still struggle to pick the right API or supply the right parameters. \[Wan26d\] makes the asymmetry explicit. Table 2 shows that stronger models do best in grounded mode, while weaker ones do better in guided mode, and allowing the weaker model to choose between modes makes performance worse rather than better. \[Ni26\] provides the sharpest evidence. Table 3 shows that a 35B model can outperform a 122B model on the base DocVQA task but still write worse skills, including skills that degrade its own later performance. \[Xu25b\] generalizes the point beyond skills. Section 6 states directly that memory organization quality depends on the underlying model’s summarization and categorization ability.

使用经验的能力和蒸馏经验的能力不是同一种能力。\[Wan23c\] 已经显示出对基础模型的强依赖，图 9 报告了开放式技能发现中从 GPT-4 到 GPT-3.5 的大幅下降。\[Zhe25c\] 发现作者与用户之间存在类似分裂。第 4.3 节显示，强智能体可以合成让弱智能体受益的 API，但弱智能体仍难以选择正确 API 或提供正确参数。\[Wan26d\] 明确化了这种不对称。表 2 显示，强模型在有根基模式中表现最好，弱模型在引导模式中更好，而允许弱模型在模式间自行选择会使性能变差。\[Ni26\] 提供了最尖锐的证据。表 3 显示，35B 模型可以在基础 DocVQA 任务上超过 122B 模型，但仍写出更差技能，包括会降低自身后续性能的技能。\[Xu25b\] 将该点推广到技能之外。第 6 节直接指出，记忆组织质量取决于底层模型的摘要和分类能力。

This matters because some survey narratives implicitly treat experience transformation as an architecture-level improvement that should transfer cleanly across models. The evidence does not support that. There is an author problem, a consumer problem, and an interface problem between them. Stronger models may be needed to create reusable artifacts, but the resulting artifacts may still overwhelm weaker executors if they add decision burden faster than they add guidance \[Zhe25c, Wan26d, Ni26, Xu25b\].

这一点重要，因为一些综述叙事隐含地把经验转化视为架构级改进，并假设它应当能跨模型干净迁移。证据并不支持这种判断。这里同时有作者问题、消费者问题，以及二者之间的接口问题。创建可复用产物可能需要更强模型，但若产物增加决策负担的速度快于增加指导的速度，它们仍可能压垮较弱执行器 \[Zhe25c, Wan26d, Ni26, Xu25b\]。

### Lifecycle management is mostly heuristic

### 生命周期管理大多依赖启发式

Once memory stores grow, most systems fall back on hand-tuned maintenance rules. \[For25\] is unusually transparent about this. Table 8 and Appendix D list threshold-heavy design choices, while Appendix C.7 notes that utility-based pruning can forget rare but critical procedures. The same paper also admits that the sample threshold for contrastive refinement is far below what would be statistically reliable. \[Qiu26\] adds a more sophisticated maintenance mechanism, but it still depends on percentile pruning, semantic merging, and utility scoring heuristics. Figure 3 shows why maintenance matters, because repository size and misuse grow rapidly without it. \[Mi26\] shows the necessity of maintenance from the opposite direction. Table 3 demonstrates that removing score-based survival in favor of FIFO leads to collapse. \[Ma26\] uses a fixed active guideline budget and a hand-weighted utility score, which is practical but clearly not a general solution. \[Liu25i\] adds another scaling sign. Table 3 shows that graph traversal stays cheap while vector retrieval becomes the true bottleneck as the memory bank grows.

一旦记忆存储增长，多数系统会退回到手工调节维护规则。\[For25\] 在这一点上异常透明。表 8 和附录 D 列出大量阈值型设计选择，附录 C.7 则指出，基于效用的剪枝会遗忘罕见但关键的过程。同一论文还承认，对比精炼的样本阈值远低于统计上可靠的水平。\[Qiu26\] 加入更复杂的维护机制，但仍依赖百分位剪枝、语义合并和效用打分启发式。图 3 显示维护为何重要，因为没有维护时，仓库大小和误用会快速增长。\[Mi26\] 从相反方向显示维护必要性。表 3 证明，去掉基于得分的生存机制、改用先进先出会导致崩塌。\[Ma26\] 使用固定活跃指南预算和手工加权效用分数，这很实用，但显然不是一般解。\[Liu25i\] 加入了另一种扩展信号。表 3 显示，图遍历仍然便宜，而随着记忆库增长，向量检索变成真正瓶颈。

The field has not yet developed a good theory of what to keep, merge, archive, or retire. It knows append-only memory is unsustainable, but it still lacks explicit notions of supersession, exception preservation, and deferred archival for rare but important cases. This becomes especially important once transformed experience is treated as a long-lived asset rather than a short prompt cache.

该领域尚未发展出关于保留、合并、归档或退役内容的良好理论。它知道只追加记忆不可持续，但仍缺少显式的替代关系、例外保留，以及面向罕见但重要案例的延迟归档概念。一旦转化经验被当作长期资产，而非短提示缓存，这会变得尤其重要。

### Evaluation still lags behind the claims

### 评估仍落后于主张

Several papers are strong on ideas but weak on direct measurement of the object they actually contribute. \[Wei26\] is the clearest case. Section 4 explicitly states that no quantitative experiments are provided because the dataset pipeline is not ready. \[Liu26\] shows a more subtle evaluation gap. Section C.3 argues that workflow equivalence is hard even for humans, so the paper falls back to pass-style metrics even though the core contribution is workflow generation. \[Ano24\] admits in Appendix C that direct measurement of graph fidelity is extremely difficult, which pushes the evaluation toward proxy measures like growth and update rates instead of semantic correctness. \[Jo26\] proposes workflow reconstruction from logs, but Section 3.1 is built on a pilot dataset of only 563 filtered events and does not test whether the reconstructed history actually improves an agent. \[Zha25c\] adds a different missing metric: design cost. The method searches over multiple reasoning paths and refinement rounds, but the paper does not fully price the meta-cost of creating the optimized workflow.

多篇论文在想法上很强，但对其实际贡献对象的直接测量很弱。\[Wei26\] 是最清楚的案例。第 4 节明确说明，由于数据集流水线尚未准备好，因此没有提供定量实验。\[Liu26\] 显示出更细微的评估缺口。第 C.3 节认为，即使对人类来说，工作流等价性也很难判断，因此论文退回到通过式指标，尽管核心贡献是工作流生成。\[Ano24\] 在附录 C 中承认，直接测量图保真度极其困难，这使评估转向增长率和更新率等代理指标，而不是语义正确性。\[Jo26\] 提出从日志重建工作流，但第 3.1 节建立在仅含 563 个过滤事件的试点数据集上，并未测试重建历史是否真的改善智能体。\[Zha25c\] 加入了另一个缺失指标：设计成本。该方法搜索多条推理路径和多轮精炼，但论文没有充分计价创建优化工作流的元成本。

These are not isolated shortcomings. They show that the field still evaluates end-task success more easily than artifact quality, maintenance burden, or design efficiency. That makes it hard to compare a workflow generator, a map constructor, and a skill library on common terms. It also encourages claims of generality when the actual artifact may be brittle, expensive to build, or only loosely aligned with the intended abstraction target.

这些并非孤立缺点。它们显示，该领域评估最终任务成功要比评估产物质量、维护负担或设计效率容易得多。这使工作流生成器、地图构建器和技能库很难在共同术语下比较。它也会鼓励泛化性主张，即使实际产物可能脆弱、构建昂贵，或只与预期抽象目标松散对齐。

## Future directions

## 未来方向

| Direction | What progress would look like | Core support |
|:---|:---|:---|
| Adaptive multi-granular experience | Agents choose and switch among notes, workflows, skills, and subagents based on task demands | \[Fan25\], \[Wan26d\], \[Qiu26\], \[Liu26\], \[Cha20\] |
| Applicability-aware retrieval and controlled fallback | Memory use becomes uncertainty-aware, interruptible, and branch-sensitive | \[Tan26\], \[Wan26d\], \[For25\], \[Mi26\], \[Zha25\] |
| Grounded validation and causal attribution | Memory updates are accepted because they pass environment-backed tests and can be linked to later gains | \[Zhe25c\], \[Zha25c\], \[Fen26\], \[Ni26\], \[For25\] |
| Failure-native memory design | Failures become first-class reusable objects rather than filtered-away noise | \[Cao25\], \[Ni26\], \[Tan26\], \[Mi26\], \[Ma26\] |
| Lifecycle-aware repositories | Versioning, retirement, archival, and contradiction handling become explicit parts of the memory system | \[For25\], \[Qiu26\], \[Mi26\], \[Liu25i\], \[Ma26\] |
| Cross-model and cross-domain transfer with interface adaptation | Experience is authored by one agent, adapted by another, and evaluated across frameworks and sites | \[Zhe25c\], \[Ni26\], \[Tan25\], \[Tan25b\], \[Fen26\] |
| Multimodal and grounded state abstractions | Agents learn from visual, spatial, and continuous signals rather than only text and static metadata | \[Lee23\], \[Xu24b\], \[Ano24\], \[Ma26\], \[Fen26\] |
| Better artifact-level benchmarks | The field measures workflow equivalence, graph fidelity, design cost, and long-run drift directly | \[Wei26\], \[Liu26\], \[Ano24\], \[Jo26\], \[Zha25c\] |

| 方向 | 进展形态 | 核心依据 |
|:---|:---|:---|
| 自适应多粒度经验 | 智能体按任务需求在笔记、工作流、技能和子智能体之间选择并切换 | \[Fan25\], \[Wan26d\], \[Qiu26\], \[Liu26\], \[Cha20\] |
| 适用性感知检索与受控回退 | 记忆使用变得不确定性感知、可中断且对分支敏感 | \[Tan26\], \[Wan26d\], \[For25\], \[Mi26\], \[Zha25\] |
| 有根基的验证与因果归因 | 记忆更新因通过环境支撑测试且可关联到后续增益而被接收 | \[Zhe25c\], \[Zha25c\], \[Fen26\], \[Ni26\], \[For25\] |
| 失败原生记忆设计 | 失败成为一等可复用对象，而不是被过滤掉的噪声 | \[Cao25\], \[Ni26\], \[Tan26\], \[Mi26\], \[Ma26\] |
| 生命周期感知仓库 | 版本化、退役、归档和矛盾处理成为记忆系统的显式组成部分 | \[For25\], \[Qiu26\], \[Mi26\], \[Liu25i\], \[Ma26\] |
| 带接口适配的跨模型与跨领域迁移 | 经验由一个智能体撰写，由另一个智能体适配，并跨框架和站点评估 | \[Zhe25c\], \[Ni26\], \[Tan25\], \[Tan25b\], \[Fen26\] |
| 多模态且有根基的状态抽象 | 智能体从视觉、空间和连续信号中学习，而不只依赖文本和静态元数据 | \[Lee23\], \[Xu24b\], \[Ano24\], \[Ma26\], \[Fen26\] |
| 更好的产物级基准 | 该领域直接测量工作流等价性、图保真度、设计成本和长期漂移 | \[Wei26\], \[Liu26\], \[Ano24\], \[Jo26\], \[Zha25c\] |

### Adaptive multi-granular experience

### 自适应多粒度经验

One clear direction is to stop treating memory form as a one-time design commitment. \[Fan25\] already shows that hybrid procedural memory outperforms either scripts or verbatim trajectories alone. \[Wan26d\] shows that grounded execution and guided execution each dominate for different model strengths, and the mixed setting can harm weaker models because the choice itself becomes extra reasoning burden. \[Qiu26\] suggests a richer split again by separating stateless skills from stateful subagents, with Figure 2 and the ablations showing that the subagent side matters most on harder tasks. \[Liu26\] indicates that execution-first and plan-first strategies win on different task categories, and \[Cha20\] shows that even defining workflow state granularity is threshold-sensitive.

一个清晰方向是停止把记忆形式当作一次性设计承诺。\[Fan25\] 已经显示，混合程序性记忆优于单独脚本或逐字轨迹。\[Wan26d\] 显示，有根基执行和引导执行分别在不同模型强度下占优，而混合设置会伤害较弱模型，因为选择本身变成额外推理负担。\[Qiu26\] 通过分离无状态技能与有状态子智能体，提出更丰富的拆分；图 2 和消融显示，子智能体侧在更难任务上最关键。\[Liu26\] 表明，执行优先和计划优先策略在不同任务类别上胜出，\[Cha20\] 则显示，即便定义工作流状态粒度也对阈值敏感。

Concrete progress would mean systems that do not merely store multiple forms, but actively decide when to stay abstract and when to drill down. Verification should test whether the chosen abstraction level was appropriate for the situation, not just whether the final task succeeded. A strong paper in this direction would compare dynamic abstraction switching against fixed-representation baselines and show gains in both success and token efficiency.

具体进展意味着系统不只是存储多种形式，还会主动决定何时保持抽象、何时下钻。验证应测试所选抽象层级是否适合情境，而不只是最终任务是否成功。这个方向上的强论文会将动态抽象切换与固定表示基线比较，并在成功率和 token 效率上都显示增益。

### Applicability-aware retrieval and controlled fallback

### 适用性感知检索与受控回退

The next generation of systems should model retrieval as a risky action rather than a free benefit. \[Tan26\] already moves in this direction with confidence-aware fallback. \[Wan26d\] uses a Skill Graph to reduce retrieval-execution mismatch, and \[For25\] uses Bayesian selection rather than flat nearest-neighbor retrieval. \[Mi26\] frames memory survival as a selective process rather than open admission, while \[Zha25\] shows that wider retrieval neighborhoods can lower performance in multi-agent settings.

下一代系统应把检索建模为有风险动作，而非免费收益。\[Tan26\] 已通过置信度感知回退朝此方向推进。\[Wan26d\] 使用技能图来减少检索-执行错配，\[For25\] 使用贝叶斯选择而非扁平最近邻检索。\[Mi26\] 将记忆生存表述为选择性过程，而非开放准入；\[Zha25\] 显示，在多智能体设置中，更宽检索邻域可能降低性能。

Concrete progress would look like memory items carrying explicit applicability conditions, uncertainty estimates, and interruption triggers. A retrieval decision should be judged by whether it improved the trajectory relative to abstaining, not just by whether it looked semantically similar. Evaluation could measure negative transfer rate, branch recovery after a wrong retrieval, and how often the system correctly refuses to use a memory. That would move the field beyond top-k similarity as the dominant retrieval paradigm.

具体进展可以表现为记忆项携带显式适用条件、不确定性估计和中断触发器。检索决策应按它相对于拒用是否改善轨迹来评判，而不只是看起来是否语义相似。评估可以测量负迁移率、错误检索后的分支恢复，以及系统正确拒绝使用记忆的频率。这样会推动该领域越过以 top-k 相似度为主导的检索范式。

### Grounded validation and causal attribution

### 有根基的验证与因果归因

Several papers point toward stronger validation but do not yet deliver it. \[Zhe25c\] shows why exception-free execution is inadequate. \[Zha25c\] shows that self-model validation can actively hurt. \[Fen26\] explicitly calls for grounded state observations rather than descriptive preconditions and effects. \[Ni26\] names the missing piece directly in Section 6 by calling for fine-grained attribution tracking. \[For25\] adds a complementary point from statistics: many current update decisions are made on evidence that is too weak to justify the change.

多篇论文指向更强验证，但尚未真正实现。\[Zhe25c\] 显示为何无异常执行并不充分。\[Zha25c\] 显示自模型验证会主动造成损害。\[Fen26\] 明确呼吁有根基的状态观察，而非描述性前置条件和效果。\[Ni26\] 在第 6 节直接点名缺失环节，呼吁细粒度归因跟踪。\[For25\] 从统计角度补充：许多当前更新决策建立在太弱的证据上，不足以支持改变。

Concrete progress would mean patch-level or memory-item-level testing. A new skill should pass an execution-grounded unit test. A revised workflow should be checked against state transitions, not just a judge score. A system should also be able to answer which stored item caused the later improvement and which parts were ignored. That would support pruning, debugging, and auditing. It would also make it possible to compare different carriers on equal terms by asking how much validated utility they add per update.

具体进展意味着补丁级或记忆项级测试。新技能应通过有执行根基的单元测试。修订后的工作流应根据状态转移检查，而不只是根据裁判分数检查。系统还应能够回答哪个存储项造成了后续改进，以及哪些部分被忽略。这将支持剪枝、调试和审计，也会使不同载体能够在同等条件下比较，即询问每次更新增加了多少已验证效用。

### Failure-native memory design

### 失败原生记忆设计

The literature strongly suggests that failures should become first-class memory objects rather than awkward negatives that get filtered away. \[Cao25\] already uses failure-aware reflection, though the paper also shows that raw full-addition is harmful. \[Ni26\] finds that error-driven updates are more stable than success-driven ones. \[Tan26\] exposes the current limitation by only learning from success. \[Mi26\] demonstrates that failure diagnosis can target different skill components, while \[Ma26\] shows that retry episodes are often where useful semantic memory is actually enriched.

文献强烈提示，失败应成为一等记忆对象，而不是被过滤掉的尴尬负例。\[Cao25\] 已经使用失败感知反思，尽管该论文也显示原始全量添加是有害的。\[Ni26\] 发现错误驱动更新比成功驱动更新更稳定。\[Tan26\] 只从成功中学习，暴露了当前局限。\[Mi26\] 证明失败诊断可以定位到不同技能组件，而 \[Ma26\] 显示重试回合往往才是有用语义记忆真正被丰富的位置。

Concrete progress would look like structured failure artifacts that record cause, violated precondition, attempted repair, and evidence that the repair worked later. Such objects could support taboo memory, avoidance constraints, or escalation rules rather than only positive how-to guidance. Verification should test not only whether the same failure is avoided later, but whether the resulting caution remains local instead of overgeneralizing into harmful conservatism.

具体进展可以表现为结构化失败产物，用来记录原因、被违反的前置条件、尝试修复，以及该修复后来有效的证据。这类对象可以支持禁忌记忆、规避约束或升级规则，而不只是正向操作指南。验证不应只测试后续是否避免了同一失败，还应测试由此产生的谨慎是否保持局部性，避免过度泛化为有害保守。

### Lifecycle-aware repositories

### 生命周期感知仓库

Maintenance should become part of the method, not just an implementation detail. \[For25\] shows why simple utility pruning is unsafe for rare procedures. \[Qiu26\] demonstrates that continual maintenance materially affects repository quality. \[Mi26\] shows that the wrong forgetting rule can collapse long-run performance. \[Liu25i\] exposes scaling pressure through vector retrieval latency, and \[Ma26\] shows that fixed-capacity active memory already forces selection pressure in embodied settings.

维护应成为方法的一部分，而不是实现细节。\[For25\] 显示，简单效用剪枝对罕见过程并不安全。\[Qiu26\] 证明持续维护会实质影响仓库质量。\[Mi26\] 显示，错误遗忘规则会使长期性能崩塌。\[Liu25i\] 通过向量检索延迟暴露扩展压力，\[Ma26\] 则显示，在具身设置中，固定容量活跃记忆已经带来选择压力。

Concrete progress would include version histories, supersession links, rare-case archives, and explicit retirement reasons. A repository should distinguish active cache from long-tail archive instead of forcing all knowledge into one retrieval pool. Benchmarks should report churn, stale-memory rate, contradiction rate, and recovery after a bad update. These metrics would make lifecycle quality measurable rather than anecdotal.

具体进展包括版本历史、替代链接、罕见案例归档和显式退役原因。仓库应区分活跃缓存和长尾归档，而不是强迫所有知识进入同一个检索池。基准应报告周转率、陈旧记忆率、矛盾率和错误更新后的恢复情况。这些指标会让生命周期质量可测，而不是停留在案例叙述。

### Cross-model and cross-domain transfer with interface adaptation

### 带接口适配的跨模型与跨领域迁移

Cross-agent transfer is already one of the most promising signals in the literature, but it remains partial and fragile. \[Zhe25c\] shows that strong agents can write skills that weaker agents profit from. \[Ni26\] complicates that story by showing that execution strength and authoring strength can diverge. \[Tan25\] finds strongly asymmetric transfer across reasoning and software domains, which suggests that some experiences are structurally more portable than others. \[Tan25b\] shows that retrieved workflows degrade sharply as the candidate pool grows, and the Refine module is crucial for adapting a retrieved workflow to the current tool context. \[Fen26\] then shows the current limit, because per-site environment maps do not solve multi-site tasks.

跨智能体迁移已经是文献中最有前景的信号之一，但它仍然局部且脆弱。\[Zhe25c\] 显示，强智能体可以写出弱智能体能受益的技能。\[Ni26\] 通过显示执行强度和撰写强度可能分离，使这个故事变得复杂。\[Tan25\] 发现推理领域与软件领域之间存在强非对称迁移，这提示某些经验在结构上比其他经验更具可移植性。\[Tan25b\] 显示，随着候选池增长，检索到的工作流会急剧退化，而精炼模块对将检索工作流适配到当前工具上下文至关重要。\[Fen26\] 随后显示当前限制，因为按站点构建的环境地图无法解决多站点任务。

Concrete progress would mean separating author model, adaptation layer, and executor model in evaluation. A transferred artifact should be tested across frameworks, sites, or domains with explicit interface translation rather than implicit prompt reuse. This would make it possible to ask not just whether experience transfers, but what proportion of the transfer burden lies in representation, refinement, or execution.

具体进展意味着在评估中分离作者模型、适配层和执行模型。迁移产物应通过显式接口翻译跨框架、站点或领域测试，而不是隐式复用提示。这样就能追问的不只是经验是否迁移，还包括迁移负担中有多大比例来自表示、精炼或执行。

### Multimodal and grounded state abstractions

### 多模态且有根基的状态抽象

A large share of current work still assumes that experience can be summarized textually. Several papers show that this is too narrow. \[Lee23\] fails on apps whose usable state is not recoverable from accessibility metadata. \[Xu24b\] shows that even when models can derive pseudo-labeled text from videos, temporal order remains weak and generated SOPs overspecify steps in the model’s own style rather than the human task granularity. \[Ano24\] explicitly names multimodal observations and procedural memory as future work beyond text-only semantic and episodic graph memory. \[Ma26\] shows that symbolic memory still struggles with continuous spatial orientation in navigation tasks. \[Fen26\] argues that descriptive environment maps should become grounded state models.

当前工作中很大一部分仍假设经验可以用文本摘要。多篇论文显示这过于狭窄。\[Lee23\] 在那些无法从无障碍元数据恢复可用状态的应用上失败。\[Xu24b\] 显示，即使模型能够从视频中导出伪标注文本，时间顺序仍很弱，生成的标准作业程序也会以模型自身风格过度指定步骤，而不是遵循人类任务粒度。\[Ano24\] 明确把多模态观察和程序性记忆列为未来工作，超越仅文本的语义图记忆和情节图记忆。\[Ma26\] 显示，符号记忆在导航任务中仍难处理连续空间方向。\[Fen26\] 主张描述性环境地图应变成有根基的状态模型。

Concrete progress would look like experience transformation that preserves visual and spatial affordances instead of flattening them into text too early. Verification should include whether a transformed artifact retains action-critical spatial relations, temporal order, and perception-dependent cues. This direction is especially important for GUI, mobile, and embodied agents, where the most important experience often lies in what the current text schema throws away.

具体进展可以表现为经验转化保留视觉和空间可供性，而不是过早把它们压平成文本。验证应包括转化产物是否保留动作关键空间关系、时间顺序和依赖感知的线索。这个方向对图形界面、移动端和具身智能体尤其重要，因为最重要的经验常常位于当前文本模式会丢弃的内容中。

### Better artifact-level benchmarks

### 更好的产物级基准

The field needs benchmarks that evaluate the transformed artifact directly. \[Wei26\] explicitly lacks a standard dataset for workflow generation. \[Liu26\] shows that workflow equivalence is hard even for human judges. \[Ano24\] cannot directly measure graph correspondence. \[Jo26\] highlights the lack of large-scale intent-grounded trace data for workflow reconstruction. \[Zha25c\] exposes the need to price the meta-cost of designing an optimized workflow, not just the runtime cost of executing it.

该领域需要能直接评估转化产物的基准。\[Wei26\] 明确缺少用于工作流生成的标准数据集。\[Liu26\] 显示，即使对人类裁判来说，工作流等价性也很难判断。\[Ano24\] 无法直接测量图对应关系。\[Jo26\] 强调缺少用于工作流重建的大规模意图扎根轨迹数据。\[Zha25c\] 暴露出一个需求：需要计价设计优化工作流的元成本，而不只是执行它的运行时成本。

Concrete progress would mean benchmark suites with artifact-level labels or executable checks for workflow equivalence, graph fidelity, maintenance under drift, and design cost. A strong benchmark would also separate build-time cost from use-time benefit. That would make it possible to compare a cheap but brittle memory against an expensive but durable one without hiding the tradeoff inside a single end-task score.

具体进展意味着基准套件包含产物级标签或可执行检查，用于评估工作流等价性、图保真度、漂移下维护和设计成本。强基准还应分离构建时成本与使用时收益。这样就能比较廉价但脆弱的记忆和昂贵但持久的记忆，而不把权衡隐藏在单个最终任务分数中。

---

## References

\[Wan25d\] Z. Wang, A. Gandhi, G. Neubig, and D. Fried, “Inducing Programmatic Skills for Agentic Tasks,” *ArXiv*, vol. abs/2504.06821, Apr. 2025, doi: [10.48550/arXiv.2504.06821](https://doi.org/10.48550/arXiv.2504.06821).

\[Fan25\] R. Fang *et al.*, “Memp: Exploring Agent Procedural Memory,” *ArXiv*, vol. abs/2508.06433, Aug. 2025, doi: [10.48550/arXiv.2508.06433](https://doi.org/10.48550/arXiv.2508.06433).

\[Liu26\] Y. Liu, Z. Zhang, Z. He, and H. Cai, “FlowMind: Execute-Summarize for Structured Workflow Generation from LLM Reasoning,” *ArXiv*, vol. abs/2602.11782, Feb. 2026, doi: [10.48550/arXiv.2602.11782](https://doi.org/10.48550/arXiv.2602.11782).

\[Qiu26\] L. Qiu *et al.*, “AutoRefine: From Trajectories to Reusable Expertise for Continual LLM Agent Refinement,” *ArXiv*, vol. abs/2601.22758, Jan. 2026, doi: [10.48550/arXiv.2601.22758](https://doi.org/10.48550/arXiv.2601.22758).

\[Cha20\] M. Chang, B. Lafreniere, J. Kim, G. Fitzmaurice, and T. Grossman, “Workflow Graphs: A Computational Model of Collective Task Strategies for 3D Design Software,” *Graphics Interface*, pp. 114–124, Apr. 2020, doi: [10.20380/GI2020.13](https://doi.org/10.20380/GI2020.13).

\[Wan24\] Z. Wang, J. Mao, D. Fried, and G. Neubig, “Agent Workflow Memory,” *ArXiv*, vol. abs/2409.07429, Sep. 2024, doi: [10.48550/arXiv.2409.07429](https://doi.org/10.48550/arXiv.2409.07429).

\[Cao25\] Z. Cao *et al.*, “Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution,” *ArXiv*, vol. abs/2512.10696, Dec. 2025, doi: [10.48550/arXiv.2512.10696](https://doi.org/10.48550/arXiv.2512.10696).

\[Mi26\] Q. Mi *et al.*, “Skill-Pro: Learning Reusable Skills from Experience via Non-Parametric PPO for LLM Agents,” Feb. 02, 2026.

\[Zha25\] G.-M. Zhang, M. Fu, G. Wan, M. Yu, K. Wang, and S. Yan, “G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems,” *ArXiv*, vol. abs/2506.07398, Jun. 2025, doi: [10.48550/arXiv.2506.07398](https://doi.org/10.48550/arXiv.2506.07398).

\[Wan23c\] G. Wang *et al.*, “Voyager: An Open-Ended Embodied Agent with Large Language Models,” *ArXiv*, vol. abs/2305.16291, May 2023, doi: [10.48550/arXiv.2305.16291](https://doi.org/10.48550/arXiv.2305.16291).

\[Zhe25c\] B. Zheng *et al.*, “SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills,” *ArXiv*, vol. abs/2504.07079, Apr. 2025, doi: [10.48550/arXiv.2504.07079](https://doi.org/10.48550/arXiv.2504.07079).

\[Zha25c\] M. Zhao *et al.*, “A2Flow: Automating Agentic Workflow Generation via Self-Adaptive Abstraction Operators,” *ArXiv*, vol. abs/2511.20693, Nov. 2025, doi: [10.48550/arXiv.2511.20693](https://doi.org/10.48550/arXiv.2511.20693).

\[Tan26\] Y. Tan, Z. Gao, and X. Wu, “Enhancing Web Agents with a Hierarchical Memory Tree,” Mar. 07, 2026.

\[Ni26\] J. Ni *et al.*, “Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills,” Mar. 26, 2026.

\[Ma26\] X. Ma *et al.*, “BrainMem: Brain-Inspired Evolving Memory for Embodied Agent Task Planning,” Mar. 12, 2026.

\[Fen26\] Y. Feng, C. Sharma, and K. Maamari, “Environment Maps: Structured Environmental Representations for Long-Horizon Agents,” Mar. 24, 2026.

\[Liu25i\] Z. Liu *et al.*, “Beyond Training: Enabling Self-Evolution of Agents with MOBIMEM,” *ArXiv*, vol. abs/2512.15784, Dec. 2025, doi: [10.48550/arXiv.2512.15784](https://doi.org/10.48550/arXiv.2512.15784).

\[Lee23\] S. Lee *et al.*, “MobileGPT: Augmenting LLM with Human-like App Memory for Mobile Task Automation,” *Proceedings of the 30th Annual International Conference on Mobile Computing and Networking*, Dec. 2023, doi: [10.1145/3636534.3690682](https://doi.org/10.1145/3636534.3690682).

\[Wan26d\] Z. Wang *et al.*, “WebXSkill: Skill Learning for Autonomous Web Agents,” Apr. 14, 2026.

\[Xu25b\] W. Xu, Z. Liang, K. Mei, H. Gao, J. Tan, and Y. Zhang, “A-MEM: Agentic Memory for LLM Agents,” *ArXiv*, vol. abs/2502.12110, Feb. 2025, doi: [10.48550/arXiv.2502.12110](https://doi.org/10.48550/arXiv.2502.12110).

\[For25\] S. Forouzandeh, W. Peng, P. Moradi, X. Yu, and M. Jalili, “Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement,” *ArXiv*, vol. abs/2512.18950, Dec. 2025, doi: [10.48550/arXiv.2512.18950](https://doi.org/10.48550/arXiv.2512.18950).

\[Wei26\] R. Wei, S. Wang, and Z. Shi, “WorkflowGen:an adaptive workflow generation mechanism driven by trajectory experience,” Mar. 22, 2026.

\[Ano24\] P. Anokhin, N. Semenov, A. Y. Sorokin, D. Evseev, M. Burtsev, and E. Burnaev, “AriGraph: Learning Knowledge Graph World Models with Episodic Memory for LLM Agents,” *International Joint Conference on Artificial Intelligence*, pp. 12–20, Jul. 2024, doi: [10.48550/arXiv.2407.04363](https://doi.org/10.48550/arXiv.2407.04363).

\[Jo26\] T. H. Jo and K.-H. Hyun, “From Logs to Agents: Reconstructing High-Level Creative Workflows from Low-Level Raw System Traces,” Mar. 08, 2026.

\[Tan25\] X. Tang *et al.*, “Agent KB: Leveraging Cross-Domain Experience for Agentic Problem Solving,” *ArXiv*, vol. abs/2507.06229, Jul. 2025, doi: [10.48550/arXiv.2507.06229](https://doi.org/10.48550/arXiv.2507.06229).

\[Tan25b\] X. Tan *et al.*, “Meta-Agent-Workflow: Streamlining Tool Usage in LLMs through Workflow Construction, Retrieval, and Refinement,” *Companion Proceedings of the ACM on Web Conference 2025*, May 2025, doi: [10.1145/3701716.3715247](https://doi.org/10.1145/3701716.3715247).

\[Xu24b\] M. Xu *et al.*, “In-Context Ensemble Learning from Pseudo Labels Improves Video-Language Models for Low-Level Workflow Understanding,” Sep. 24, 2024.
