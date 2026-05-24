# Experience transformation open problems

# 经验转化的开放问题

##### [**Undermind**](https://undermind.ai)

##### [**Undermind**](https://undermind.ai) 资料源

---


## Table of Contents

- [Challenges](#challenges)
  - [Memory integration is brittle and often damages the base policy](#memory-integration-is-brittle-and-often-damages-the-base-policy)
  - [Applicability is the real bottleneck, not raw recall](#applicability-is-the-real-bottleneck-not-raw-recall)
  - [Compression choices are still under-theorized](#compression-choices-are-still-under-theorized)
  - [Lifecycle management remains heuristic and under-specified](#lifecycle-management-remains-heuristic-and-under-specified)
  - [Evaluation settings still hide the hardest failure modes](#evaluation-settings-still-hide-the-hardest-failure-modes)
  - [Transfer across tasks, roles, and embodiments is still thinly evidenced](#transfer-across-tasks-roles-and-embodiments-is-still-thinly-evidenced)
- [Future directions](#future-directions)
  - [Applicability-aware memory access and controlled abstention](#applicability-aware-memory-access-and-controlled-abstention)
  - [Adaptive multi-granular memory rather than single-carrier commitment](#adaptive-multi-granular-memory-rather-than-single-carrier-commitment)
  - [Grounded validation and memory credit assignment](#grounded-validation-and-memory-credit-assignment)
  - [Learned lifecycle management and explicit repository structure](#learned-lifecycle-management-and-explicit-repository-structure)
  - [Stronger transfer studies with explicit interface adaptation](#stronger-transfer-studies-with-explicit-interface-adaptation)
  - [Harder long-run benchmarks that expose drift, contamination, and failure-derived learning](#harder-long-run-benchmarks-that-expose-drift-contamination-and-failure-derived-learning)
- [References](#references)

## Challenges

## 挑战

| Challenge | What the recent papers show | Why the literature is still thin | Core support |
|:---|:---|:---|:---|
| Memory integration is brittle | Naive concatenation, large history windows, or uncalibrated gates often hurt more than they help | The field still lacks a general rule for where memory should enter a frozen model and when it should stay out | \[Sun26\], \[Koo25\], \[Gao26\], \[Shi25\], \[Wu22\] |
| Applicability is the real bottleneck | Similarity-based retrieval often returns plausible but decision-irrelevant memories | Most methods still score relevance by surface similarity or fixed temporal proximity rather than task-conditional usefulness | \[Li25g\], \[Guo26\], \[Zhu26\], \[Che25b\], \[Wu25e\] |
| Compression choices are under-theorized | One-token, fixed-token, and short-KV memories can work, but only inside narrow capacity ranges | There is still no principled account of what information must survive transformation for different task types | \[Wu25c\], \[Hou26\], \[Shi25\], \[Sun26\], \[Yu26d\] |
| Lifecycle management is mostly heuristic | Pruning, merging, replacement, and forgetting are controlled by thresholds, FIFO buffers, or conservative prompts | The literature knows memory banks drift, but does not yet know how to maintain them with stable long-run criteria | \[Zhu26\], \[Lin25d\], \[Sun26\], \[Wu25c\], \[Fu26\] |
| Evaluation still flatters current methods | Many results rely on filtered data, static stores, bounded horizons, and benchmark-specific reward signals | The strongest claims concern continual reuse, but most evaluations remain short, curated, and success-biased | \[Gup26\], \[Zhu26\], \[Lin25d\], \[Che25b\], \[Gao26\] |
| Transfer remains narrower than the rhetoric | Memory often helps within a task family, role, embodiment, or benchmark, but weakens across shifts | The field still lacks strong evidence that transformed experience is broadly portable rather than locally useful | \[Fu26\], \[Koo25\], \[Li25g\], \[Guo26\], \[Gup26\] |

| 挑战 | 近期论文显示的现象 | 文献仍然薄弱的原因 | 核心依据 |
|:---|:---|:---|:---|
| 记忆整合具有脆弱性 | 朴素拼接、大历史窗口或未经校准的门控常常弊大于利 | 该领域仍缺少通用规则，用来判断记忆应在冻结模型的何处进入，以及何时应被排除在外 | \[Sun26\], \[Koo25\], \[Gao26\], \[Shi25\], \[Wu22\] |
| 适用性才是真正瓶颈 | 基于相似度的检索常返回看似合理却与决策无关的记忆 | 多数方法仍按表层相似度或固定时间邻近性给相关性打分，而非按任务条件下的有用性评估 | \[Li25g\], \[Guo26\], \[Zhu26\], \[Che25b\], \[Wu25e\] |
| 压缩选择仍缺少理论化解释 | 单 token、固定 token 与短 KV 记忆可以有效，但只在较窄容量区间内成立 | 对不同任务类型而言，转化后哪些信息必须保留下来，仍缺少原则性解释 | \[Wu25c\], \[Hou26\], \[Shi25\], \[Sun26\], \[Yu26d\] |
| 生命周期管理多为启发式 | 剪枝、合并、替换与遗忘由阈值、先进先出缓冲区或保守提示控制 | 文献已经认识到记忆库会漂移，但仍不知道如何用稳定的长期准则维护它们 | \[Zhu26\], \[Lin25d\], \[Sun26\], \[Wu25c\], \[Fu26\] |
| 评估仍会美化现有方法 | 许多结果依赖过滤数据、静态存储、有界时域与面向基准的奖励信号 | 最强的论断关注持续复用，但多数评估仍短程、经策划且偏向成功样本 | \[Gup26\], \[Zhu26\], \[Lin25d\], \[Che25b\], \[Gao26\] |
| 迁移证据比论述更窄 | 记忆往往在同一任务族、角色、具身形态或基准内有帮助，但在跨分布变化下减弱 | 该领域仍缺少强证据证明转化后的经验具有广泛可移植性，而非仅具局部有用性 | \[Fu26\], \[Koo25\], \[Li25g\], \[Guo26\], \[Gup26\] |

### Memory integration is brittle and often damages the base policy

### 记忆整合具有脆弱性，并且常常损害基础策略

A recurring hidden result is that memory is not helpful by default. In \[Sun26\], the main story is about temporal KV memory, but Table IV shows that the memory mechanism becomes useful only after two additional controls are added. KV memory by itself gives only a small gain over the base policy, concatenation collapses performance almost completely, and residual loading without norm preservation drops below the memoryless baseline. The paper therefore quietly narrows its claim from “plug-and-play temporal memory” to a much stricter claim: memory helps only when it is injected at the right layers, with the right temporal bias, and with careful magnitude control. \[Koo25\] reports the same shape from another angle. HAMLET outperforms raw multi-frame history, yet Table 5 shows a peak around history length 8 and then a decline as longer histories are added. \[Shi25\] likewise finds that memory length 16 is best in one benchmark while much longer memory is needed in harder real-world tasks, so the “right” amount of memory is task-specific rather than a monotone scaling axis.

一个反复出现的隐性结果是：记忆默认并不有益。在 \[Sun26\] 中，主线讨论时间 KV 记忆，但表 IV 显示，只有加入两个额外控制后，记忆机制才真正有用。单独的 KV 记忆相较基础策略只带来小幅增益，拼接几乎使性能完全崩塌，而没有范数保持的残差加载会跌到无记忆基线以下。该论文实际把论断从“即插即用的时间记忆”收窄为更严格的主张：只有在合适层注入、带有合适时间偏置，并经过谨慎幅度控制时，记忆才有帮助。\[Koo25\] 从另一角度报告了相同形态。HAMLET 优于原始多帧历史，但表 5 显示性能在历史长度约为 8 时达到峰值，继续加入更长历史后开始下降。\[Shi25\] 同样发现，在一个基准中记忆长度 16 最好，而更难的真实世界任务需要长得多的记忆，因此“合适”的记忆量依赖任务，并非单调扩展轴。

The robotic policy papers make the same point even more sharply. \[Gao26\] shows that long history hurts on mostly Markovian tasks, and that the memory gate cannot simply be trained jointly because it learns the degenerate always-on solution that fits training error but hurts generalization. Their calibration stage is a tacit admission that deciding when not to use memory is at least as important as designing the memory itself. \[Wu22\] is an earlier precursor of the same issue. Its kNN memory improves performance only for a small subset of tokens, shows layer sensitivity, and sometimes worsens predictions when the memory gets larger because the right neighbor falls out of the top-k set. Taken together, these papers imply that “more history” is still a poor design rule. That broader claim is an inference, but it is strongly supported by repeated ablations showing that memory works only inside narrow integration regimes \[Sun26, Koo25, Gao26, Shi25, Wu22\].

机器人策略论文把同一问题表现得更尖锐。\[Gao26\] 显示，长历史会损害大体马尔可夫的任务，而且记忆门控不能简单地联合训练，因为它会学到退化的常开解法：该解法贴合训练误差，却损害泛化。其校准阶段默认承认，决定何时不使用记忆，至少与设计记忆本身同样重要。\[Wu22\] 是这一问题的较早先例。其 kNN 记忆只对一小部分 token 提升性能，表现出层敏感性，并且当记忆变大时有时会恶化预测，因为正确邻居会掉出 top-k 集合。合在一起看，这些论文暗示“更多历史”仍是一条糟糕的设计规则。这个更宽的判断是一种推断，但多项消融反复显示，记忆只在狭窄的整合机制内有效 \[Sun26, Koo25, Gao26, Shi25, Wu22\]。

What matters for the survey is that this is not just an engineering nuisance. It means current work has not yet solved the model-interface problem. A transformed artifact can be good in itself and still be harmful because the consumer model cannot absorb it without distribution shift, stale emphasis, or context interference. The literature has many memory designs, but it still lacks a general account of how a frozen policy should expose “ports” for externalized experience.

对这篇综述而言，关键在于这并不只是工程层面的麻烦。它意味着当前工作尚未解决模型接口问题。一个转化产物本身可以很好，但仍可能有害，因为消费模型无法在不引入分布偏移、过时强调或上下文干扰的情况下吸收它。文献已经提出许多记忆设计，但对于冻结策略应如何为外部化经验暴露“接口”，仍缺少一般性解释。

### Applicability is the real bottleneck, not raw recall

### 适用性是真正瓶颈，而不是原始回忆能力

The strongest cross-paper pattern is that retrieval errors are usually not misses but false positives. \[Li25g\] makes this explicit. Its memory-aware prompting pipeline already assumes stage-structured demonstrations, then narrows retrieval further with a neighbor-stage rule because full search is too expensive and because similar motion windows can occur at different task stages. That design choice works, but it reveals a deeper weakness: the system does not know whether a retrieved demonstration is functionally applicable, only whether it is nearby in an imposed stage graph. \[Guo26\] surfaces the same issue in a harsher form. Their discrete `Memory Bank` baseline stays near chance on the classification metric under perceptual aliasing, which shows that visually similar recalls can be decisively wrong when identical-looking scenes encode different hidden histories.

跨论文最强的模式是：检索错误通常不是漏检，而是假阳性。\[Li25g\] 明确呈现了这一点。其记忆感知提示流水线已经假设示范具有阶段结构，随后又用邻近阶段规则进一步收窄检索范围，因为全量搜索代价过高，而且相似运动窗口可能出现在不同任务阶段。这个设计选择是有效的，但也暴露了更深层弱点：系统并不知道检索到的示范在功能上是否适用，只知道它在一个人为设定的阶段图中是否邻近。\[Guo26\] 以更严苛的形式凸显了同一问题。其离散 `Memory Bank` 基线在感知混淆条件下的分类指标接近随机水平，表明当外观相同的场景编码不同隐藏历史时，视觉相似的回忆可能会明确地导向错误。

GUI and reasoning papers show the same retrieval pathology in different carriers. In \[Zhu26\], pure FAISS retrieval underperforms the seed-and-expand graph strategy because the nearest memories are often too similar at the screen level and too narrow at the strategic level. In \[Che25b\], reused reasoning logs improve aggregate accuracy, but Table 3 also records a substantial number of correct-to-incorrect flips once logs are injected. Those flips matter more than the average gain because they show that reusable computation can act as a misleading prior rather than a neutral hint. \[Wu25e\] reports a related limitation for continuous GUI memory: it scales better than text memory, yet the paper still warns about retrieval drift under extreme UI shifts and explicitly calls for uncertainty-aware retrieval.

GUI 与推理论文在不同载体中展示了相同的检索病理。在 \[Zhu26\] 中，纯 FAISS 检索弱于种子扩展图策略，因为最近邻记忆往往在屏幕层面过于相似，在策略层面又过于狭窄。在 \[Che25b\] 中，复用推理日志提升了总体准确率，但表 3 也记录了日志注入后相当数量的由正确转为错误的翻转。这些翻转比平均增益更关键，因为它们显示可复用计算可能充当误导性先验，而非中性提示。\[Wu25e\] 报告了连续 GUI 记忆的相关局限：它比文本记忆更具扩展性，但论文仍警示极端界面变化下的检索漂移，并明确呼吁不确定性感知检索。

This matters because much of the literature still treats retrieval as a front-end module. The evidence says it is the core unresolved problem. Current systems do not yet represent the applicability conditions of a memory item, the downside risk of using it, or the cues that should trigger abstention. A promising memory can therefore fail for reasons that have little to do with memory capacity and everything to do with choosing the wrong prior at the wrong moment. Nearby procedural-memory work reinforces this reading. \[Fan25\] finds that performance peaks and then declines when too many memories are retrieved, and \[Wan24\] shows that offline and online workflow memories interfere rather than compose cleanly.

这个问题重要，是因为大量文献仍把检索视为前端模块。证据表明，它才是核心未解问题。当前系统尚未表示单个记忆项的适用条件、使用它的下行风险，或应触发拒用的线索。因此，一个看似有前景的记忆可能失败，而失败原因与记忆容量关系很小，几乎完全取决于是否在错误时刻选择了错误先验。邻近的程序性记忆工作也强化了这一解读。\[Fan25\] 发现，当检索到过多记忆时，性能先达到峰值随后下降；\[Wan24\] 则显示离线与在线工作流记忆会相互干扰，而无法干净组合。

### Compression choices are still under-theorized

### 压缩选择仍缺少理论化解释

The field now has many successful compression tricks, but much weaker evidence about what they preserve and what they destroy. \[Wu25c\] is the cleanest example. TokMem shows that a single token can encode a reusable procedure surprisingly well, but the paper also reveals how fragile that regime is. It needs a special adaptation phase for compositional tool use, routing accuracy declines as the task bank grows toward one thousand procedures, and the whole setup depends on manually decomposed procedural data. The strong result is real, but so is the hidden assumption: the procedure must already be packaged into a form that can fit inside one token’s learned role. \[Hou26\] reports a related constraint. FlashMem gains much of its efficiency from using a fixed number of latent tokens and a shallow consolidator, but the method is threshold-sensitive, requires domain-adaptive distillation on high-quality traces, and still consumes virtual token budget inside the forward pass.

该领域已经有许多成功的压缩技巧，但对于它们保留了什么、破坏了什么，证据要弱得多。\[Wu25c\] 是最清楚的例子。TokMem 表明，单个 token 可以出人意料地很好编码可复用过程，但论文也揭示了这种机制有多脆弱。它需要面向组合式工具使用的特殊适配阶段；随着任务库增长到接近一千个过程，路由准确率会下降；整个设置依赖人工分解的程序性数据。强结果是真实的，隐藏假设也是真实的：过程必须已经被打包成一种能适配单个 token 学习角色的形式。\[Hou26\] 报告了相关约束。FlashMem 的效率很大程度来自固定数量的隐空间 token 与浅层整合器，但该方法对阈值敏感，需要在高质量轨迹上做领域自适应蒸馏，并且在前向传播中仍消耗虚拟 token 预算。

Embodied papers show that the compression problem is not only about capacity but about content type. \[Shi25\] performs best only when perceptual and cognitive memory are both present. Removing either one causes a large drop, which means a single semantic summary is not enough and a pure perceptual replay is not enough either. \[Sun26\] similarly shows that capacity 8 can outperform 32 because stale or redundant frames become harmful when the horizon is expanded without better filtering. \[Yu26d\] decouples visual perception memory from thinking memory and gets clear gains from the split, but the paper’s own use of a fixed memory cap and entropy-triggered orchestration leaves open whether the current latent budget is enough for much longer interactions.

具身论文显示，压缩问题并不只关乎容量，也关乎内容类型。\[Shi25\] 只有在感知记忆与认知记忆同时存在时表现最好。移除任一者都会造成大幅下降，这意味着单一语义摘要不够，纯感知回放也不够。\[Sun26\] 同样显示，容量 8 可以优于 32，因为当时域扩展却没有更好过滤时，陈旧或冗余帧会变得有害。\[Yu26d\] 将视觉感知记忆与思维记忆解耦，并从这种拆分中获得清晰增益，但论文自身使用固定记忆上限和熵触发编排，仍留下一个开放问题：当前隐空间预算是否足以支撑长得多的交互。

The deeper gap is that the literature still lacks a task-sensitive theory of what should survive transformation. Some tasks need exact spatial residue. Some need subgoal order. Some need only a high-level policy sketch. The present evidence supports the practical claim that memory form should vary by task, but it does not yet yield a principled criterion for choosing among one-token procedures, latent summaries, KV traces, scene maps, or mixed stores. That broader claim is an inference from the repeated capacity sweet spots and dual-memory wins across \[Wu25c\], \[Hou26\], \[Shi25\], \[Sun26\], and \[Yu26d\].

更深层缺口在于，文献仍缺少关于哪些信息应在转化后保留下来的任务敏感理论。有些任务需要精确空间残留，有些任务需要子目标顺序，有些任务只需要高层策略草图。现有证据支持一个实践判断：记忆形式应随任务变化，但还没有给出原则性标准，来在单 token 过程、隐空间摘要、KV 轨迹、场景地图或混合存储之间做选择。这个更宽的判断来自对 \[Wu25c\]、\[Hou26\]、\[Shi25\]、\[Sun26\] 与 \[Yu26d\] 中反复出现的容量甜点和双记忆收益的推断。

### Lifecycle management remains heuristic and under-specified

### 生命周期管理仍是启发式的，且定义不足

Once memory persists beyond a single episode, most systems fall back on hand-built maintenance rules. \[Zhu26\] is especially revealing because it is unusually explicit. HYMEM uses an ADD, MERGE, REPLACE pipeline, but the update logic is driven by a VLM judge and highly restrictive prompts telling the model to be “very conservative” and to separate operational errors from genuine memory relevance problems. This is useful engineering, but it also exposes the absence of a learned or theoretically grounded maintenance rule. \[Lin25d\] has the same pattern in a different modality. EchoVLA’s scene memory depends on a discrepancy threshold to decide when the voxel map should be updated. Table 4 shows a narrow sweet spot, which means the long-term representation is only as good as a manually tuned update frequency.

一旦记忆持续超过单个 episode，多数系统便退回到手工维护规则。\[Zhu26\] 尤其有启发性，因为它罕见地明确。HYMEM 使用 ADD、MERGE、REPLACE 流水线，但更新逻辑由 VLM 裁判器和高度限制性的提示驱动，提示要求模型“非常保守”，并区分操作错误与真正的记忆相关性问题。这是有用的工程设计，但也暴露了缺少学习得到或具有理论基础的维护规则。\[Lin25d\] 在另一模态中呈现相同模式。EchoVLA 的场景记忆依赖差异阈值来决定何时更新体素地图。表 4 显示了狭窄的甜点，意味着长期表示的质量受制于手工调节的更新频率。

Other papers arrive at the same point through different mechanisms. \[Sun26\] uses FIFO temporal memory with fixed decay, even though the paper itself notes that irrelevant frames eventually dominate. \[Wu25c\] needs explicit renormalization to keep newly learned memory tokens from overpowering old ones through norm inflation. \[Fu26\] proposes a shared experience bank with role-specific latent composition, but the paper leaves open how that bank should grow, what should be retained, and how clutter should be controlled as the number of roles and episodes rises. The hidden consensus is that maintenance is crucial, yet it is rarely the object of learning.

其他论文通过不同机制抵达同一点。\[Sun26\] 使用带固定衰减的先进先出时间记忆，尽管论文自身指出无关帧最终会占据主导。\[Wu25c\] 需要显式重归一化，以防新学习的记忆 token 通过范数膨胀压过旧记忆。\[Fu26\] 提出带有角色特定隐空间组合的共享经验库，但论文没有回答随着角色和 episode 数量增加，该库应如何增长、应保留什么，以及应如何控制杂乱。隐含共识是维护至关重要，但它很少成为学习对象。

This matters because the survey topic is not just one-shot retrieval but experience reuse over time. Without strong maintenance, memory stores become repositories of obsolete habits, near-duplicates, and silently conflicting strategies. The literature has begun to recognize the problem, but most current solutions are still threshold policies disguised as memory architectures. Nearby work on procedural memory and workflows sharpens the same point. \[Fan25\] reports degradation when retrieval pools get too large, and \[Wan24\] shows that new online workflows can be impaired by old offline ones rather than refined by them.

这一点重要，是因为本文综述的主题不只是一次性检索，而是经验随时间复用。若缺少强维护机制，记忆存储会变成过时习惯、近重复项和隐性冲突策略的仓库。文献已经开始识别这个问题，但多数现有方案仍是伪装成记忆架构的阈值策略。关于程序性记忆和工作流的邻近研究进一步凸显了同一点。\[Fan25\] 报告称，当检索池过大时性能会退化；\[Wan24\] 显示新的在线工作流可能被旧的离线工作流损害，而非得到精炼。

### Evaluation settings still hide the hardest failure modes

### 评估设置仍遮蔽最困难的失败模式

Many of the strongest results are produced under settings that filter out exactly the kinds of messiness that future systems must survive. \[Gup26\] is a good example. ReasonCACHE makes a strong case for trainable prefix memory, but the paper filters OpenThoughts-3 to shorter traces, uses budget forcing on GPQA because long-generation inference is brittle, and shows that the headline claim does not extend to AIME, where no method beats the base model. The paper is still valuable, but its success is narrower than the top-line framing suggests. \[Zhu26\] builds its structured GUI memory from successful trajectories and skips tasks when websites are no longer accessible. \[Lin25d\] trains on quality-gated mobile-manipulation data with zero-collision, fully successful trajectories, which improves experimental cleanliness but weakens the link to failure-rich continual learning.

许多最强结果都产生在过滤掉未来系统必须承受的复杂性的设置下。\[Gup26\] 是一个典型例子。ReasonCACHE 为可训练前缀记忆提供了有力论据，但该论文将 OpenThoughts-3 过滤为较短轨迹，在 GPQA 上使用预算强制，因为长生成推理很脆弱，并且显示其标题式主张并不能扩展到 AIME，在那里没有任何方法超过基础模型。该论文仍有价值，但其成功范围比顶层叙述所暗示的更窄。\[Zhu26\] 从成功轨迹构建结构化 GUI 记忆，并在网站不再可访问时跳过任务。\[Lin25d\] 在质量门控的移动操控数据上训练，数据包含零碰撞、完全成功的轨迹，这提升了实验洁净度，却削弱了它与富含失败样本的持续学习之间的关联。

The same convenience appears in reasoning and policy-memory work. \[Che25b\] evaluates with a static offline log store rather than an online self-growing store, which avoids compounding contamination from bad logs. \[Gao26\] demonstrates very long memory windows only after freezing visual features and caching them, leaving open whether equally long history remains practical in end-to-end learning. \[Zho25b\] depends on environments with clear verifiable rewards, and explicitly flags open-ended reward settings as future work rather than current competence. \[Guo26\] and \[Koo25\] test demanding long-horizon tasks, but still within bounded benchmark families rather than open-world drift.

同样的便利性也出现在推理与策略记忆工作中。\[Che25b\] 使用静态离线日志存储进行评估，而不是在线自增长存储，因而避免了坏日志带来的复合污染。\[Gao26\] 只有在冻结并缓存视觉特征之后，才展示很长的记忆窗口，这留下了一个问题：同样长的历史在端到端学习中是否仍然可行。\[Zho25b\] 依赖具有清晰可验证奖励的环境，并明确把开放式奖励设置标为未来工作，而非当前能力。\[Guo26\] 与 \[Koo25\] 测试了有挑战性的长时域任务，但仍处在有界基准族内部，而不是开放世界漂移中。

The field therefore has a mismatch between its stated target and its evaluation regime. The stated target is continual transformation and reuse of interaction experience. The common evaluation regime is curated, short-horizon, and success-conditioned. This mismatch matters because many open problems only appear when memory becomes stale, when failure data enters the bank, or when the environment changes faster than the stored abstraction. That conclusion is an inference, but it is difficult to avoid once the methods and datasets are read closely \[Gup26, Zhu26, Lin25d, Che25b, Zho25b\].

因此，该领域的声明目标与评估机制之间存在错配。声明目标是交互经验的持续转化与复用。常见评估机制则经过策划、时域较短，并且以成功样本为条件。这种错配很关键，因为许多开放问题只会在记忆变旧、失败数据进入记忆库，或环境变化快于已存抽象时出现。这个结论是一种推断，但在细读方法和数据集后很难回避 \[Gup26, Zhu26, Lin25d, Che25b, Zho25b\]。

### Transfer across tasks, roles, and embodiments is still thinly evidenced

### 跨任务、角色与具身形态的迁移证据仍然薄弱

Many papers talk as if transformed experience should travel well, but the actual evidence is much more local. \[Fu26\] shows strong gains from role-conditioned latent memories, and its “without role” ablation drops most on more complex multi-agent systems. That is a positive result, but it also means the memory is not simply reusable knowledge. It is knowledge customized to a role profile. \[Koo25\] reports that a history-aware memory module can transfer across datasets, yet the cross-dataset score remains slightly below in-distribution training. \[Li25g\] closes with a call for generalized memory prompts precisely because the current system needs task-specific stage construction and aligned demonstrations. \[Guo26\] likewise points to cross-embodiment transfer as future work rather than current evidence.

许多论文的表述仿佛转化后的经验应当易于迁移，但实际证据更具局部性。\[Fu26\] 显示角色条件化隐空间记忆带来强增益，而其“无角色”消融在更复杂的多智能体系统上下降最大。这是正向结果，但也意味着这种记忆并不只是可复用知识。它是针对角色画像定制的知识。\[Koo25\] 报告历史感知记忆模块可以跨数据集迁移，但跨数据集分数仍略低于分布内训练。\[Li25g\] 在结尾呼吁泛化的可复用记忆提示，原因正是当前系统需要任务特定阶段构建和对齐示范。\[Guo26\] 同样把跨具身形态迁移指向未来工作，而非当前证据。

The reasoning papers tell a similar story. \[Gup26\] argues that ReasonCACHE can match or beat in-weight adaptation on several benchmarks, but not on the hardest math setting in the paper. \[Che25b\] reuses logs effectively within dataset families, yet its whole setup depends on logs drawn from the same task distribution. \[Wu25c\] shows impressive scale in procedural memory, but its gains rely on procedural decomposition and a backbone already aligned enough to use the learned token. Even when transfer works, it often works because the author carefully preserves the consumer’s expected interface rather than because the transformed experience is truly model-agnostic.

推理论文给出了相似图景。\[Gup26\] 认为 ReasonCACHE 在若干基准上可以匹配或超过权重内适配，但在论文中最困难的数学设置上不能做到。\[Che25b\] 在数据集族内部有效复用日志，但整个设置依赖来自同一任务分布的日志。\[Wu25c\] 在程序性记忆上展示了可观规模，但其增益依赖过程分解，以及已经足够对齐、能够使用所学 token 的主干模型。即使迁移有效，也常常是因为作者谨慎保留了消费模型预期的接口，而非因为转化后的经验真正与模型无关。

This challenge matters for a survey on carrier transformation because portability is one of the main promised benefits of externalized experience. The present literature gives real but partial support for that promise. It shows that transformed experience can travel across some model sizes, frameworks, and tasks. It does not yet show that the same artifact remains reliable under large shifts in embodiment, role structure, reward semantics, or environment dynamics. Nearby procedural-memory results point in the same direction. \[Fan25\] finds transfer from stronger to weaker agents, but only after careful key design and bounded retrieval.

这一挑战对载体转化综述很重要，因为可移植性是外部化经验承诺的主要收益之一。现有文献为这一承诺提供了真实但部分的支持。它显示转化后的经验可以跨一些模型规模、框架和任务流动。它尚未显示同一产物在具身形态、角色结构、奖励语义或环境动力学发生大幅变化时仍然可靠。邻近的程序性记忆结果指向相同方向。\[Fan25\] 发现经验可以从更强智能体迁移到更弱智能体，但前提是进行了谨慎的键设计并限制了检索范围。

## Future directions

## 未来方向

| Direction | What concrete progress would look like | Core support |
|:---|:---|:---|
| Applicability-aware memory access | Retrieval decisions carry uncertainty, abstention, and fallback logic rather than pure nearest-neighbor selection | \[Wu25e\], \[Gao26\], \[Zhu26\], \[Li25g\], \[Che25b\] |
| Adaptive multi-granular memory | Agents switch among perceptual, procedural, latent, and structured forms rather than committing to one carrier per system | \[Shi25\], \[Yu26d\], \[Wu25c\], \[Hou26\], \[Guo26\] |
| Grounded validation and memory credit assignment | Systems can tell which memory item caused improvement and reject updates that pass superficial checks but fail in the environment | \[Zho25b\], \[Wu25e\], \[Zhu26\], \[Che25b\], \[Guo26\] |
| Learned lifecycle management | Update, merge, archive, and retirement policies become trainable and benchmarked rather than prompt- or threshold-driven | \[Zhu26\], \[Lin25d\], \[Sun26\], \[Wu25c\], \[Fu26\] |
| Stronger transfer studies | Memory artifacts are tested across roles, backbones, embodiments, and domains with explicit interface adaptation | \[Fu26\], \[Koo25\], \[Li25g\], \[Guo26\], \[Gup26\] |
| Harder long-run benchmarks | Evaluation includes drift, stale memory, failure-derived updates, and online self-contamination | \[Gup26\], \[Zhu26\], \[Lin25d\], \[Che25b\], \[Gao26\] |

| 方向 | 具体进展的形态 | 核心依据 |
|:---|:---|:---|
| 适用性感知的记忆访问 | 检索决策携带不确定性、拒用与回退逻辑，而不是纯最近邻选择 | \[Wu25e\], \[Gao26\], \[Zhu26\], \[Li25g\], \[Che25b\] |
| 自适应多粒度记忆 | 智能体在感知型、程序型、隐空间与结构化形式之间切换，而不是每个系统绑定一个载体 | \[Shi25\], \[Yu26d\], \[Wu25c\], \[Hou26\], \[Guo26\] |
| 有根基的验证与记忆信用分配 | 系统能够判断哪个记忆项导致了改进，并拒绝那些通过表层检查却在环境中失败的更新 | \[Zho25b\], \[Wu25e\], \[Zhu26\], \[Che25b\], \[Guo26\] |
| 学习得到的生命周期管理 | 更新、合并、归档与退役策略变为可训练、可基准评测的对象，而非由提示或阈值驱动 | \[Zhu26\], \[Lin25d\], \[Sun26\], \[Wu25c\], \[Fu26\] |
| 更强的迁移研究 | 在显式接口适配下，跨角色、主干模型、具身形态和领域测试记忆产物 | \[Fu26\], \[Koo25\], \[Li25g\], \[Guo26\], \[Gup26\] |
| 更难的长期运行基准 | 评估包含漂移、陈旧记忆、由失败样本派生的更新，以及在线自污染 | \[Gup26\], \[Zhu26\], \[Lin25d\], \[Che25b\], \[Gao26\] |

### Applicability-aware memory access and controlled abstention

### 适用性感知的记忆访问与受控拒用

A high-value direction is to treat memory use as a risky action rather than a free benefit. Several papers already point there. \[Wu25e\] explicitly calls for uncertainty-aware retrieval in GUI agents. \[Gao26\] shows that a gate deciding whether to consult history is essential because always-on memory hurts on simple tasks. \[Zhu26\] demonstrates that diversity-aware graph expansion beats pure similarity search, which suggests that applicability is not captured by nearest-neighbor distance alone. \[Li25g\] hard-codes a stage-local search window because unrestricted retrieval is both expensive and ambiguous. \[Che25b\] shows why this matters on reasoning tasks: reused logs can turn correct answers into incorrect ones when the wrong prior is activated.

一个高价值方向是把记忆使用视为有风险的动作，而非无成本收益。已有多篇论文指向这里。\[Wu25e\] 明确呼吁 GUI 智能体中的不确定性感知检索。\[Gao26\] 显示，决定是否查询历史的门控是必要的，因为常开记忆会损害简单任务。\[Zhu26\] 证明，多样性感知的图扩展优于纯相似度搜索，提示适用性无法仅由最近邻距离捕捉。\[Li25g\] 硬编码阶段局部搜索窗口，因为无约束检索既昂贵又含混。\[Che25b\] 显示了这在推理任务中为何重要：当错误先验被激活时，复用日志会把正确答案变成错误答案。

Concrete progress would look like memory items carrying explicit applicability metadata, confidence estimates, and interruption conditions. Retrieval should be evaluated against an abstain baseline, not only against weaker retrieval. The right question is not “did the nearest memory help on average,” but “did the system know when memory would be more dangerous than useful.” Verification could measure negative-transfer rate, recovery after a bad retrieval, and calibration between uncertainty and memory usage. That would move the field beyond similarity search and fixed temporal windows.

具体进展可以表现为：记忆项携带显式适用性元数据、置信度估计和中断条件。检索应与拒用基线比较，而不只与更弱检索方法比较。合适的问题并非“最近记忆平均是否有帮助”，而是“系统是否知道何时记忆会比有用更危险”。验证可以测量负迁移率、错误检索后的恢复能力，以及不确定性与记忆使用之间的校准关系。这样的评估会推动该领域走出相似度搜索和固定时间窗口。

### Adaptive multi-granular memory rather than single-carrier commitment

### 自适应多粒度记忆，而非绑定单一载体

The recent literature already hints that no single carrier is enough. \[Shi25\] needs both perceptual and cognitive memory. \[Yu26d\] gets gains by separating latent perception memory from latent thinking memory. \[Wu25c\] shows that one-token procedural memory can work for compact reusable procedures, but only after decomposition and adaptation. \[Hou26\] shows that a small latent consolidator can stabilize reasoning efficiently, while \[Guo26\] argues that purely semantic memory misses the perceptual residue needed under aliasing. These results do not point to a winner. They point to a division of labor.

近期文献已经暗示，没有任何单一载体是充分的。\[Shi25\] 同时需要感知记忆与认知记忆。\[Yu26d\] 通过分离隐空间感知记忆与隐空间思维记忆获得增益。\[Wu25c\] 显示，单 token 程序性记忆可以服务于紧凑的可复用过程，但只有经过分解与适配后才成立。\[Hou26\] 显示，小型隐空间整合器能够高效稳定推理，而 \[Guo26\] 认为纯语义记忆会遗漏感知混淆下所需的感知残留。这些结果没有指向赢家，而是指向分工关系。

Concrete progress would mean systems that choose the memory form dynamically. A manipulation agent might preserve spatial traces early in a task, then consolidate them into a procedural sketch once the environment becomes predictable. A reasoning agent might keep a dense latent summary while the problem is live, then externalize a textual or structured artifact only after validation. This broader direction is partly an inference, but it is the most natural synthesis of the repeated dual-memory and split-function results across \[Shi25\], \[Yu26d\], \[Wu25c\], \[Hou26\], and \[Guo26\]. Strong evidence would come from papers that compare dynamic carrier switching against fixed-carrier baselines while measuring both success and maintenance cost.

具体进展意味着系统能够动态选择记忆形式。操控智能体可以在任务早期保留空间轨迹，待环境变得可预测后再将其整合成程序草图。推理智能体可以在问题仍在进行时保留稠密隐空间摘要，经过验证后再外部化为文本或结构化产物。这个更宽方向部分来自推断，但它是对 \[Shi25\]、\[Yu26d\]、\[Wu25c\]、\[Hou26\] 与 \[Guo26\] 中反复出现的双记忆和功能拆分结果的自然综合。强证据将来自把动态载体切换与固定载体基线进行比较，并同时测量成功率和维护成本的论文。

### Grounded validation and memory credit assignment

### 有根基的验证与记忆信用分配

A major open direction is to make memory updates auditable. \[Zho25b\] already shows that reward shaping can backfire when the agent optimizes formatting rather than content, which is a reminder that easy-to-check signals can become misleading objectives. \[Wu25e\] explicitly names RL-integrated credit assignment as future work. \[Zhu26\] spends substantial prompt budget distinguishing operational mistakes from memory-relevance errors, which implies that current systems still confuse execution failure with memory failure. \[Che25b\] provides a clean motivation from the opposite side: logs sometimes hurt, but the method does not know which stored item caused the damage. \[Guo26\] shows that similarity retrieval can fail badly under aliasing, which in turn makes it hard to tell whether a poor action came from a bad memory, a bad readout, or weak perception.

一个主要开放方向是让记忆更新可审计。\[Zho25b\] 已经显示，当智能体优化格式而非内容时，奖励塑形可能适得其反，这提醒我们，易检查信号可能变成误导性目标。\[Wu25e\] 明确把整合强化学习的信用分配列为未来工作。\[Zhu26\] 花费大量提示预算来区分操作失误与记忆相关性错误，这意味着当前系统仍会混淆执行失败和记忆失败。\[Che25b\] 从相反方向给出了清晰动机：日志有时会造成损害，但该方法不知道是哪一个存储项造成了损害。\[Guo26\] 显示，相似度检索会在混淆条件下严重失败，这又使人很难判断糟糕动作来自坏记忆、坏读出，还是弱感知。

Concrete progress would look like patch-level and item-level tests. A new memory item should be accepted because it improves controlled rollouts, not because it looks coherent or because a judge model prefers it. A system should also record whether a retrieved memory was actually attended to and whether removing it would have changed the decision. Useful benchmarks could score causal utility per memory item, false acceptance of harmful updates, and the system’s ability to localize which stored experience changed the trajectory.

具体进展可以表现为补丁级和条目级测试。新记忆项应因为能改善受控采样轨迹而被接收，而不是因为看起来连贯，或因为裁判模型偏好它。系统还应记录检索到的记忆是否真的被关注，以及移除它是否会改变决策。有用的基准可以为每个记忆项的因果效用、有害更新的错误接收，以及系统定位哪个已存经验改变了轨迹的能力打分。

### Learned lifecycle management and explicit repository structure

### 学习得到的生命周期管理与显式仓库结构

The current literature has already shown that memory maintenance cannot stay an implementation detail. \[Zhu26\] relies on judge-mediated add, merge, and replace operations. \[Lin25d\] depends on discrepancy thresholds to stabilize a 3D scene map. \[Sun26\] uses fixed decay over temporal KV states, and \[Wu25c\] requires explicit renormalization to stop new memories from suppressing old ones. \[Fu26\] opens the door to role-conditioned latent composition, but a much larger unanswered question is how shared multi-agent repositories should be governed as the number of roles, tasks, and interaction histories grows.

当前文献已经表明，记忆维护不能停留为实现细节。\[Zhu26\] 依赖裁判器介导的添加、合并与替换操作。\[Lin25d\] 依赖差异阈值来稳定 3D 场景地图。\[Sun26\] 对时间 KV 状态使用固定衰减，\[Wu25c\] 则需要显式重归一化，以阻止新记忆压制旧记忆。\[Fu26\] 为角色条件化隐空间组合打开了入口，但一个大得多的未解问题是：随着角色、任务和交互历史数量增长，共享多智能体仓库应如何治理。

Concrete progress would mean trainable maintenance policies and explicit repository structure. Memory systems could separate active working memory from archived memory, record supersession links, keep rare but high-value exceptions, and learn when a retrieved item should be revised instead of reused. Evaluation should report churn, contradiction rate, stale-memory rate, and recovery after a bad update. This would turn lifecycle quality into a first-class research target rather than a set of hidden heuristics.

具体进展意味着可训练维护策略和显式仓库结构。记忆系统可以分离活跃工作记忆与归档记忆，记录替代链接，保留罕见但高价值的例外，并学习何时应修订而不是复用检索项。评估应报告周转率、矛盾率、陈旧记忆率以及错误更新后的恢复情况。这会把生命周期质量变成一类一等研究目标，而非一组隐藏启发式。

### Stronger transfer studies with explicit interface adaptation

### 带有显式接口适配的更强迁移研究

A promising direction is to stop treating transfer as a side effect and make it the main object of measurement. \[Fu26\] shows that role-specific latent memory matters more as coordination grows more complex. \[Koo25\] shows partial cross-dataset transfer for history-aware policies. \[Li25g\] directly frames generalized reusable memory prompts as future work. \[Guo26\] calls out cross-embodiment transfer. \[Gup26\] shows that a frozen backbone can learn reusable reasoning traces without weight updates, but also exposes where that promise fails on harder tasks.

一个有前景的方向是停止把迁移当作副作用，并把它作为主要测量对象。\[Fu26\] 显示，随着协作变得更复杂，角色特定隐空间记忆更重要。\[Koo25\] 显示历史感知策略具有部分跨数据集迁移能力。\[Li25g\] 直接把泛化的可复用记忆提示定义为未来工作。\[Guo26\] 点出了跨具身形态迁移。\[Gup26\] 显示冻结主干无需权重更新也能学习可复用推理轨迹，但也暴露出这一承诺在更难任务上失效的位置。

Concrete progress would involve evaluating the same transformed artifact across different consumers. The report of a memory method should separate the author model, the adaptation layer, and the executor model. In robotics, the same episodic abstraction should be tested across camera layouts or arm configurations. In multi-agent settings, a memory written for one role topology should be tested on another. In reasoning systems, the same cached procedure should be transferred across model scales and prompt styles. Progress would be visible when transfer degrades gracefully and the interface work needed for reuse becomes measurable rather than hidden.

具体进展会包括跨不同消费模型评估同一转化产物。记忆方法的报告应区分作者模型、适配层和执行模型。在机器人任务中，同一 episode 抽象应跨相机布局或机械臂配置测试。在多智能体设置中，为一种角色拓扑写成的记忆应在另一种拓扑上测试。在推理系统中，同一个缓存过程应跨模型规模和提示风格迁移。当迁移能够平滑退化，且复用所需的接口工作变得可测而非隐藏时，进展就会变得可见。

### Harder long-run benchmarks that expose drift, contamination, and failure-derived learning

### 揭示漂移、污染与失败样本学习的更难长期运行基准

The next benchmark wave should target the conditions that current papers mostly avoid. \[Gup26\] still works in verifiable reasoning settings with filtered traces. \[Zhu26\] constructs memory from successful trajectories and skips inaccessible sites. \[Lin25d\] trains on quality-controlled mobile-manipulation data. \[Che25b\] uses a static offline log store instead of online self-growing memory. \[Gao26\] shows long buffers in controlled robotic settings but not a full continual online loop. These choices are understandable, but they also reveal what the field has not yet tested.

下一波基准应针对当前论文大多避开的条件。\[Gup26\] 仍在带有过滤轨迹的可验证推理设置中工作。\[Zhu26\] 从成功轨迹构建记忆，并跳过无法访问的网站。\[Lin25d\] 在经过质量控制的移动操控数据上训练。\[Che25b\] 使用静态离线日志存储，而不是在线自增长记忆。\[Gao26\] 在受控机器人设置中展示长缓冲区，但没有展示完整的持续在线循环。这些选择可以理解，但也揭示了该领域尚未测试的内容。

Concrete progress would look like benchmarks with interface drift, delayed rewards, stale memory traps, mixed success and failure histories, and online memory growth under contamination risk. For agentic reasoning, that means letting bad logs enter the store and measuring whether maintenance can recover. For GUI agents, it means websites or apps changing during the experiment. For robotics, it means repeated sessions with altered layouts, occlusion, or sensor drift. A memory method should then be judged not only by short-term success but by how safely and efficiently it keeps learning after its own store has become part of the environment.

具体进展可以表现为包含接口漂移、延迟奖励、陈旧记忆陷阱、成功与失败混合历史，以及污染风险下在线记忆增长的基准。对于智能体式推理，这意味着允许坏日志进入存储，并测量维护机制能否恢复。对于 GUI 智能体，这意味着网站或应用在实验期间发生变化。对于机器人，这意味着在布局改变、遮挡或传感器漂移条件下反复运行会话。记忆方法的评判不应只看短期成功，还应看当自身存储已经成为环境的一部分后，它能多安全、多高效地持续学习。

---

## References

\[Sun26\] J. Sun *et al.*, “TempoFit: Plug-and-Play Layer-Wise Temporal KV Memory for Long-Horizon Vision-Language-Action Manipulation,” Mar. 08, 2026.

\[Koo25\] M. Koo *et al.*, “HAMLET: Switch your Vision-Language-Action Model into a History-Aware Policy,” *ArXiv*, vol. abs/2510.00695, Oct. 2025, doi: [10.48550/arXiv.2510.00695](https://doi.org/10.48550/arXiv.2510.00695).

\[Gao26\] Y. Gao, J. Liu, S. Li, and S. Song, “Gated Memory Policy,” Apr. 21, 2026.

\[Shi25\] H. Shi *et al.*, “MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation,” *ArXiv*, vol. abs/2508.19236, Aug. 2025, doi: [10.48550/arXiv.2508.19236](https://doi.org/10.48550/arXiv.2508.19236).

\[Wu22\] Y. Wu, M. Rabe, D. S. Hutchins, and C. Szegedy, “Memorizing Transformers,” *ArXiv*, vol. abs/2203.08913, Mar. 2022, doi: [10.48550/arXiv.2203.08913](https://doi.org/10.48550/arXiv.2203.08913).

\[Li25g\] R. Li *et al.*, “MAP-VLA: Memory-Augmented Prompting for Vision-Language-Action Model in Robotic Manipulation,” *ArXiv*, vol. abs/2511.09516, Nov. 2025, doi: [10.48550/arXiv.2511.09516](https://doi.org/10.48550/arXiv.2511.09516).

\[Guo26\] X. Guo *et al.*, “Chameleon: Episodic Memory for Long-Horizon Robotic Manipulation,” Mar. 25, 2026.

\[Zhu26\] S. Zhu, W. Wu, K. Zhou, S. Wang, and B. Huang, “Hybrid Self-evolving Structured Memory for GUI Agents,” Mar. 11, 2026.

\[Che25b\] P. Chen, Y. Zhang, D. Roth, S. Madden, J. Andreas, and M. J. Cafarella, “Log-Augmented Generation: Scaling Test-Time Reasoning with Reusable Computation,” *ArXiv*, vol. abs/2505.14398, May 2025, doi: [10.48550/arXiv.2505.14398](https://doi.org/10.48550/arXiv.2505.14398).

\[Wu25e\] W. Wu *et al.*, “Auto-scaling Continuous Memory for GUI Agent,” *ArXiv*, vol. abs/2510.09038, Oct. 2025, doi: [10.48550/arXiv.2510.09038](https://doi.org/10.48550/arXiv.2510.09038).

\[Wu25c\] Z. Wu, Y. Hao, and L. Mou, “TokMem: One-Token Procedural Memory for Large Language Models,” Oct. 01, 2025.

\[Hou26\] Y. Hou, Z. Chen, T. Wan, and Z. Qin, “FlashMem: Distilling Intrinsic Latent Memory via Computation Reuse,” *ArXiv*, vol. abs/2601.05505, Jan. 2026, doi: [10.48550/arXiv.2601.05505](https://doi.org/10.48550/arXiv.2601.05505).

\[Yu26d\] X. Yu *et al.*, “Dual Latent Memory for Visual Multi-agent System,” *ArXiv*, vol. abs/2602.00471, Jan. 2026, doi: [10.48550/arXiv.2602.00471](https://doi.org/10.48550/arXiv.2602.00471).

\[Lin25d\] M. Lin *et al.*, “EchoVLA: Synergistic Declarative Memory for VLA-Driven Mobile Manipulation,” Nov. 22, 2025.

\[Fu26\] M. Fu *et al.*, “LatentMem: Customizing Latent Memory for Multi-Agent Systems,” *ArXiv*, vol. abs/2602.03036, Feb. 2026, doi: [10.48550/arXiv.2602.03036](https://doi.org/10.48550/arXiv.2602.03036).

\[Gup26\] S. Gupta *et al.*, “ReasonCACHE: Teaching LLMs To Reason Without Weight Updates,” *ArXiv*, vol. abs/2602.02366, Feb. 2026, doi: [10.48550/arXiv.2602.02366](https://doi.org/10.48550/arXiv.2602.02366).

\[Fan25\] R. Fang *et al.*, “Memp: Exploring Agent Procedural Memory,” *ArXiv*, vol. abs/2508.06433, Aug. 2025, doi: [10.48550/arXiv.2508.06433](https://doi.org/10.48550/arXiv.2508.06433).

\[Wan24\] Z. Wang, J. Mao, D. Fried, and G. Neubig, “Agent Workflow Memory,” *ArXiv*, vol. abs/2409.07429, Sep. 2024, doi: [10.48550/arXiv.2409.07429](https://doi.org/10.48550/arXiv.2409.07429).

\[Zho25b\] Z. Zhou *et al.*, “MEM1: Learning to Synergize Memory and Reasoning for Efficient Long-Horizon Agents,” *ArXiv*, vol. abs/2506.15841, Jun. 2025, doi: [10.48550/arXiv.2506.15841](https://doi.org/10.48550/arXiv.2506.15841).
