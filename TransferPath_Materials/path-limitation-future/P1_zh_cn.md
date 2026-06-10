# Experience transformation challenges and directions

# 经验转化的挑战与方向

##### [**Undermind**](https://undermind.ai)

##### [**Undermind**](https://undermind.ai) 资料源

---


## Table of Contents

- [Most relevant papers and scope limits](#most-relevant-papers-and-scope-limits)
- [Challenges](#challenges)
  - [Abstraction level is still unstable](#abstraction-level-is-still-unstable)
  - [Retrieval quality is a bottleneck, and the penalty is negative transfer rather than simple no-op failure](#retrieval-quality-is-a-bottleneck-and-the-penalty-is-negative-transfer-rather-than-simple-no-op-failure)
  - [Validation and credit assignment remain weak, especially for failure-derived experience](#validation-and-credit-assignment-remain-weak-especially-for-failure-derived-experience)
  - [Static memory artifacts break in dynamic, partially observable environments](#static-memory-artifacts-break-in-dynamic-partially-observable-environments)
  - [Strong model dependence is much larger than many papers admit](#strong-model-dependence-is-much-larger-than-many-papers-admit)
  - [Memory lifecycle management is underdeveloped and mostly heuristic](#memory-lifecycle-management-is-underdeveloped-and-mostly-heuristic)
  - [Evaluation remains narrower and more convenient than the papers often imply](#evaluation-remains-narrower-and-more-convenient-than-the-papers-often-imply)
  - [Cross-carrier transfer is still mostly aspirational](#cross-carrier-transfer-is-still-mostly-aspirational)
- [Future directions](#future-directions)
  - [Adaptive multi-granular memory](#adaptive-multi-granular-memory)
  - [Stronger validation and causal attribution for memory updates](#stronger-validation-and-causal-attribution-for-memory-updates)
  - [Hybrid carrier pipelines rather than single-carrier commitment](#hybrid-carrier-pipelines-rather-than-single-carrier-commitment)
  - [Continual maintenance with versioning, contradiction handling, and retirement](#continual-maintenance-with-versioning-contradiction-handling-and-retirement)
  - [Better support for learning from failure without poisoning the memory bank](#better-support-for-learning-from-failure-without-poisoning-the-memory-bank)
  - [Cross-model and cross-agent transfer with attention to stylistic mismatch](#cross-model-and-cross-agent-transfer-with-attention-to-stylistic-mismatch)
  - [More realistic benchmarks for memory lifecycle and environment drift](#more-realistic-benchmarks-for-memory-lifecycle-and-environment-drift)
  - [Bridging external memory and parametric learning](#bridging-external-memory-and-parametric-learning)
- [References](#references)

## Most relevant papers and scope limits

## 最相关论文与范围限制

| Paper | Transformation focus | Why it is central | Possible limitations for this survey goal | Evidence anchors |
|:---|:---|:---|:---|:---|
| \[Shi23b\] | Failed episode to verbal reflection reused in context | Early canonical reflection loop for agent self-improvement | Stays within text to text reuse and keeps memory short due to context limits, so it says little about long-run consolidation or non-text carriers | Sec. 4.2, Fig. 4c, Table 3, Sec. 5 |
| \[Zha23c\] | Trajectories and failure success contrasts to cross-task insights | Strong early paper on moving from episodic traces to reusable principles across tasks | Assumes deterministic environments and repeated retries, and insight quality depends strongly on extractor model quality | Sec. 4.1 to 4.4, Table 3, Sec. 6 |
| \[Fu24\] | Contrastive trajectories to context-aware guidelines | Sharp demonstration that localized contrastive abstraction can beat raw demonstration reuse | Needs paired success and failure traces and remains a text-only offline distillation method | Sec. 3.2, Table 4, Fig. 4, Appendix A |
| \[Che24\] | Interactive trajectories to instruction manual rules and code snippets | Important for online rule construction rather than purely offline summarization | Relies heavily on GPT-4-turbo, keeps a small rule budget, and still struggles in larger dynamic settings without retrieval support | Sec. 3.3, Table 4, Appendix A, Appendix D |
| \[Maj23\] | Trial traces to causal abstractions and meta-memory | Distinguishes causal memory from generic advice and shows structure matters | Uses hand-designed templates and natural-language feedback mappings, so abstraction space is narrow and language-centric | Sec. 3.2, Sec. 3.3, Fig. 5d, Sec. 4.3 |
| \[Hu25\] | Failed trajectory to hindsight-rewritten workflows | One of the clearest papers on counterfactual rewriting rather than reflection alone | Still stores experience as natural language workflows and reports infeasible synthesized workflows in execution | Sec. 3.1, Sec. 4.2, Fig. 3, Sec. 5.3 |
| \[Wan24\] | Successful trajectories to parameterized workflows | Canonical workflow-induction paper for web agents | Static workflows are brittle in dynamic pages, and offline plus online workflow memory can interfere rather than compose | Sec. 4.3, Table 8, Table 9, Fig. 7, Table 11 |
| \[Fan25\] | Verbatim trajectories plus abstract scripts to procedural memory | Strong evidence that mixed procedural memory outperforms either concrete or abstract alone | Depends on gold trajectories and similarity-based retrieval, and performance falls when too many memories are retrieved | Sec. 3.1, Table 1, Table 2, Sec. 5 |
| \[Cao25\] | Keypoint trajectories to refined procedural memory with add edit prune | Makes lifecycle management itself part of the contribution rather than a side issue | Retrieval still happens only once at task start, and utility thresholds and self-reflection caps are hand set | Sec. 3.4, Table 2, Table 3, Fig. 4, Sec. 5 |
| \[Ni26\] | Many local lessons to consolidated transferable skills | Important because it studies consolidation and the author user gap directly | Skill authoring depends on model scale and costly agentic analysis, and the framework stays training-free and artifact-centric | Sec. 2.3, Sec. 3.4, Table 3, Sec. 6 |
| \[Wan23c\] | Embodied trajectories to executable code skills | Foundational case where experience becomes callable code rather than advice | Strongly tied to the MineDojo API and text-state interface, with hallucinated mechanics and self-verification failures still common | Sec. 2.3, Sec. 3.4, Fig. 9, Sec. 4 |
| \[Wan26\] | Exploration traces to hierarchical skill knowledge base | Central recent paper on large skill libraries and experience-guided expansion | Retrieval and execution mismatch remains severe enough to require pseudo-plan rewriting, and weaker models over-imitate skills | Sec. 4, Sec. 5.3, Fig. 3, Table 3 |
| \[Xie25\] | GUI interaction triples to transition-aware knowledge | Strong example of local transition mining instead of whole-trajectory memory | Depends on Android metadata and checkpoint restoration, and cross-platform gains are still modest | Sec. 3.1, Table 4, Fig. 4, Appendix G |
| \[Xie25b\] | Offline and online GUI traces to hierarchical multimodal skills | Good evidence for hierarchical abstraction over multimodal GUI history | Requires human success evaluation in the update loop and remains bottlenecked by grounding accuracy | Algorithm 1, Sec. 3.3, Table 3, Appendix A |
| \[Liu25b\] | Online videos to in-context trajectories for computer-use agents | Important boundary paper for importing third-party experience at inference time | Relevant videos exist for only part of the benchmark, and text-only summaries lose important visual detail | Sec. 3.3, Table 2, Table 4, Sec. 4.2 |
| \[Zha25f\] | Iteratively evolving bullet playbooks from feedback | Strong evidence that memory editing granularity matters and that monolithic rewrites collapse | Focuses almost entirely on textual context evolution and depends on a strong reflector and curator | Sec. 3.1, Sec. 4.4, Appendix A.5, Sec. 5 |
| \[Ma25\] | Raw interaction logs to narrative episodes and semantic memory | Valuable because it targets the distillation decision itself rather than a single agent benchmark | Mostly about ingestion-time text distillation and intentionally stays agnostic to downstream reuse mechanisms | Sec. 2.2, Sec. 3, Sec. 4.4, Sec. 5 |
| \[Yan25d\] | Long-horizon trajectories to SOPs and strategic principles | Strong recent self-evolving agent paper that ties memory growth to task iteration | Gains partly ride on the overall architecture, benchmarks can penalize creative valid behavior, and memory stays natural-language based | Sec. 3.3, Fig. 3, Table 3, Table 4, Appendix A.2 |

| 论文 | 转化焦点 | 中心性原因 | 对本文综述目标的潜在限制 | 证据锚点 |
|:---|:---|:---|:---|:---|
| \[Shi23b\] | 失败回合转化为在上下文中复用的语言反思 | 早期具有代表性的智能体自我改进反思循环 | 停留在文本到文本复用，并因上下文限制保持短记忆，因此对长期整合或非文本载体说明有限 | 第 4.2 节，图 4c，表 3，第 5 节 |
| \[Zha23c\] | 轨迹以及失败/成功对照转化为跨任务洞见 | 关于从回合轨迹走向跨任务可复用原则的早期强工作 | 假设确定性环境和重复重试，洞见质量强依赖抽取模型质量 | 第 4.1 至 4.4 节，表 3，第 6 节 |
| \[Fu24\] | 对比轨迹转化为上下文感知指南 | 清楚展示局部对比抽象可优于原始示范复用 | 需要成对成功与失败轨迹，并且仍是纯文本离线蒸馏方法 | 第 3.2 节，表 4，图 4，附录 A |
| \[Che24\] | 交互轨迹转化为说明手册规则和代码片段 | 对在线规则构建很重要，而非仅做离线摘要 | 高度依赖 GPT-4-turbo，规则预算较小，并且在没有检索支持的大规模动态设置中仍有困难 | 第 3.3 节，表 4，附录 A，附录 D |
| \[Maj23\] | 试验轨迹转化为因果抽象与元记忆 | 区分因果记忆和一般建议，并显示结构很重要 | 使用手工模板和自然语言反馈映射，抽象空间较窄且以语言为中心 | 第 3.2 节，第 3.3 节，图 5d，第 4.3 节 |
| \[Hu25\] | 失败轨迹转化为后见重写的工作流 | 关于反事实重写而非单纯反思的清晰论文之一 | 仍以自然语言工作流存储经验，并报告了执行中不可行的合成工作流 | 第 3.1 节，第 4.2 节，图 3，第 5.3 节 |
| \[Wan24\] | 成功轨迹转化为参数化工作流 | 网页智能体工作流归纳的经典论文 | 静态工作流在动态页面中脆弱，离线与在线工作流记忆可能相互干扰，难以组合 | 第 4.3 节，表 8，表 9，图 7，表 11 |
| \[Fan25\] | 逐字轨迹加抽象脚本转化为程序性记忆 | 强证据表明混合程序性记忆优于单独的具体记忆或抽象记忆 | 依赖黄金轨迹和基于相似度的检索，当检索到过多记忆时性能下降 | 第 3.1 节，表 1，表 2，第 5 节 |
| \[Cao25\] | 关键点轨迹经添加、编辑、剪枝转化为精炼程序性记忆 | 将生命周期管理本身作为贡献，而非附属问题 | 检索仍只在任务开始时发生一次，效用阈值和自我反思上限均为手工设定 | 第 3.4 节，表 2，表 3，图 4，第 5 节 |
| \[Ni26\] | 大量局部经验转化为整合后的可迁移技能 | 直接研究整合以及作者-用户差距，因此重要 | 技能撰写依赖模型规模和昂贵的智能体式分析，框架保持免训练且以产物为中心 | 第 2.3 节，第 3.4 节，表 3，第 6 节 |
| \[Wan23c\] | 具身轨迹转化为可执行代码技能 | 经验从建议变为可调用代码的奠基性案例 | 与 MineDojo API 和文本状态接口强绑定，幻觉机制和自验证失败仍常见 | 第 2.3 节，第 3.4 节，图 9，第 4 节 |
| \[Wan26\] | 探索轨迹转化为层级技能知识库 | 关于大规模技能库和经验引导扩展的近期核心论文 | 检索与执行错配仍严重到需要伪计划重写，较弱模型会过度模仿技能 | 第 4 节，第 5.3 节，图 3，表 3 |
| \[Xie25\] | 图形界面交互三元组转化为转移感知知识 | 局部转移挖掘而非整轨迹记忆的强例子 | 依赖 Android 元数据和检查点恢复，跨平台增益仍有限 | 第 3.1 节，表 4，图 4，附录 G |
| \[Xie25b\] | 离线和在线图形界面轨迹转化为层级多模态技能 | 为多模态图形界面历史上的层级抽象提供良好证据 | 更新循环需要人工成功评估，并仍受限于定位准确率 | 算法 1，第 3.3 节，表 3，附录 A |
| \[Liu25b\] | 在线视频转化为计算机使用智能体的上下文内轨迹 | 关于推理时引入第三方经验的重要边界论文 | 相关视频只覆盖部分基准，纯文本摘要会丢失重要视觉细节 | 第 3.3 节，表 2，表 4，第 4.2 节 |
| \[Zha25f\] | 从反馈中迭代演化项目符号式行动手册 | 强证据表明记忆编辑粒度很关键，单体重写会崩塌 | 几乎完全聚焦文本上下文演化，并依赖强反思器和策展器 | 第 3.1 节，第 4.4 节，附录 A.5，第 5 节 |
| \[Ma25\] | 原始交互日志转化为叙事回合和语义记忆 | 有价值，因为它针对蒸馏决策本身，而非单一智能体基准 | 主要讨论摄入时文本蒸馏，并有意不绑定下游复用机制 | 第 2.2 节，第 3 节，第 4.4 节，第 5 节 |
| \[Yan25d\] | 长时域轨迹转化为标准作业程序和策略原则 | 将记忆增长与任务迭代联系起来的近期强自演化智能体论文 | 增益部分来自整体架构，基准可能惩罚有创造性但有效的行为，记忆仍基于自然语言 | 第 3.3 节，图 3，表 3，表 4，附录 A.2 |

## Challenges

## 挑战

### Abstraction level is still unstable

### 抽象层级仍不稳定

The most repeated problem is not whether experience should be stored, but at what level it should be rewritten. If the artifact stays too close to the raw trace, the agent inherits noise, redundancy, and instance-specific clutter. If the artifact is too compressed, it drops exactly the details that make it executable. \[Fu24\] shows this from the guideline side. Increasing the number of retrieved guidelines helps only up to a point, then hurts, with the paper explicitly attributing the decline to overload and irrelevant guidance in complex settings. \[Fan25\] reports the same non-monotonic effect for procedural memory, where too many retrieved memories increase interference and context burden. \[Yan26b\] independently finds that both internal history length and external insight count have a sweet spot, with performance dropping again once the memory becomes too dense. At the opposite extreme, \[Liu23\] shows that a single LLM summary of robot sensory history omits failure-critical facts that the progressive hierarchical summary preserves, and \[Ma25\] explicitly keeps a dual retrieval mode because distilled narratives may lose precision-critical details. The field has therefore not solved the basic compression question. It knows that abstraction helps, but it still lacks a reliable rule for how much detail to retain for planning, execution, and transfer at once.

最反复出现的问题并非经验是否应被存储，而是应在何种层级被重写。若产物过于接近原始轨迹，智能体会继承噪声、冗余和实例特定的杂乱信息。若产物被过度压缩，它又会恰好丢掉使其可执行的细节。\[Fu24\] 从指南侧展示了这一点。增加检索到的指南数量只在一定范围内有帮助，随后会带来损害，论文明确把下降归因于复杂设置中的过载和无关指导。\[Fan25\] 对程序性记忆报告了相同的非单调效应，过多检索记忆会增加干扰和上下文负担。\[Yan26b\] 独立发现，内部历史长度和外部洞见数量都有甜点，一旦记忆过密，性能会再次下降。在另一端，\[Liu23\] 显示，单个 LLM 对机器人感知历史的摘要会遗漏渐进式层级摘要保留下来的失败关键事实，\[Ma25\] 则明确保留双检索模式，因为蒸馏后的叙事可能丢失精度关键细节。因此，该领域尚未解决基本压缩问题。它知道抽象有帮助，但仍缺少可靠规则，用来判断应为规划、执行和迁移同时保留多少细节。

This matters because the carrier form determines the failure mode. Reflection papers can drift toward vague advice. Workflow papers can become brittle scripts. Skill libraries can become overspecialized fragments. A concrete advance would be to evaluate memory systems not only by end-task success, but also by information retention under controlled perturbations. A useful protocol would ask whether the transformed artifact still preserves preconditions, exception cases, and action-critical arguments that were present in the source trajectory. That requirement is an inference from the repeated ablation pattern across \[Fu24\], \[Fan25\], \[Yan26b\], \[Liu23\], and \[Ma25\], not an explicit claim made by any single paper.

这里的关键在于，载体形式决定失败模式。反思论文可能滑向含糊建议。工作流论文可能变成脆弱脚本。技能库可能变成过度特化的碎片。一项具体进展是评估记忆系统时不只看最终任务成功率，也看受控扰动下的信息保留。一个有用协议应询问：转化产物是否仍保留源轨迹中存在的前置条件、例外情形和动作关键参数。这个要求来自 \[Fu24\]、\[Fan25\]、\[Yan26b\]、\[Liu23\] 与 \[Ma25\] 中反复出现的消融模式推断，并非任何单篇论文的显式主张。

### Retrieval quality is a bottleneck, and the penalty is negative transfer rather than simple no-op failure

### 检索质量是瓶颈，其代价是负迁移，而非简单的无操作失败

Many papers quietly show that bad retrieval is worse than no memory. \[Aza25\] reports that reflection memory lowers performance on tasks the base agent already solves, and the degradation is especially visible on Reddit, where reflections reduce performance on both seen and unseen settings. \[Mi26b\] makes the point even more starkly. Its standard goal-based retrieval baseline performs worse than a memory-free baseline because it pollutes the prompt with mismatched history. \[Cao25\] finds that retrieving more experiences eventually degrades performance for the same reason, and \[Che25d\] shows that one retrieved software experience can be better than several because extra experiences impose cognitive burden and sometimes conflict. In \[Wan26\], the mismatch between retrieved skills and actual execution is severe enough that the system inserts a pseudo-plan rewriting stage before retrieval. \[Wan24\] shows a related issue at a different level. Offline and online workflow memories do not compose cleanly. When naively combined, the joint memory performs worse than either source alone.

许多论文隐性显示，糟糕检索比没有记忆更差。\[Aza25\] 报告称，反思记忆会降低基础智能体已经能解决的任务性能，这种退化在 Reddit 上尤其明显，反思会同时降低已见和未见设置的性能。\[Mi26b\] 更直白地展示了这一点。其标准的基于目标的检索基线弱于无记忆基线，因为它用不匹配的历史污染提示。\[Cao25\] 发现，检索更多经验最终也会因同一原因降低性能，\[Che25d\] 则显示，一个被检索的软件经验可能优于多个经验，因为额外经验会带来认知负担，有时还会冲突。在 \[Wan26\] 中，检索技能与实际执行之间的错配严重到系统必须在检索前插入伪计划重写阶段。\[Wan24\] 在另一个层级展示了相关问题。离线和在线工作流记忆无法干净组合。朴素合并时，联合记忆的表现反而弱于任一单一来源。

The hidden content here is that many papers describe retrieval as a support module, but the ablations show it is often the main determinant of whether transformed experience is helpful or toxic. \[Fan25\] finds retrieval key design matters enough that feature-style keys outperform plain query similarity. \[Xie25\] spends 42.9 percent of time in the knowledge ranker, which is a sign that selecting the right experience has become nearly as hard as acting. The field still lacks robust applicability modeling. Current systems mostly rely on embedding similarity, hand-designed schemas, or light reranking, but they rarely estimate the downside risk of a retrieved memory. Progress would look like memory items carrying explicit applicability conditions, uncertainty, and revocation signals, then being judged by whether they help under distribution shift rather than just whether they match semantically.

这里的隐含内容是，许多论文把检索描述为支持模块，但消融显示，它往往是决定转化经验有益还是有毒的主要因素。\[Fan25\] 发现检索键设计足够重要，特征式键优于普通查询相似度。\[Xie25\] 将 42.9% 的时间花在知识排序器上，这表明选择正确经验几乎已经和行动本身一样困难。该领域仍缺少鲁棒的适用性建模。当前系统大多依赖嵌入相似度、手工设计的模式或轻量重排序，但很少估计被检索记忆的下行风险。进展可以表现为记忆项携带显式适用条件、不确定性和撤销信号，然后按其在分布偏移下是否有帮助来评判，而不只是看它们在语义上是否匹配。

### Validation and credit assignment remain weak, especially for failure-derived experience

### 验证和信用分配仍然薄弱，尤其是面向失败样本经验时

The literature repeatedly claims to learn from failure, but the evidence shows that failure is much harder to convert into reusable knowledge than success. \[Shi23b\] names credit assignment directly as a challenge and shows that verbal explanation matters more than merely replaying an episode. Yet the same paper reports local-minimum failures in WebShop and false positives from flaky self-generated tests in coding. \[Sar25\] states that failed trajectories are challenging to operationalize because useful and harmful subsequences are entangled. \[Hu25\] improves on this by rewriting failed trajectories through hindsight, but still reports synthesized workflows that are infeasible or not faithfully followed at execution time. \[Ni26\] observes that success-derived patches are less stable than error-driven updates, while \[Su25\] warns that verifier noise in self-evolution settings can systematically contaminate the mistake notebook even if the accept-if-improves rule blocks some regressions.

文献反复声称可以从失败中学习，但证据显示，失败比成功更难转化为可复用知识。\[Shi23b\] 直接把信用分配列为挑战，并显示语言解释比单纯回放 episode 更重要。然而，同一论文也报告了 WebShop 中的局部最小值失败，以及编码任务中由不稳定自生成测试带来的假阳性。\[Sar25\] 表示，失败轨迹难以操作化，因为有用和有害子序列交织在一起。\[Hu25\] 通过后见重写失败轨迹改进了这一点，但仍报告合成工作流不可行，或在执行时未被忠实遵循。\[Ni26\] 观察到，成功派生补丁不如错误驱动更新稳定，而 \[Su25\] 警告，在自演化设置中，即便“若改进则接收”的规则能阻止部分退化，验证器噪声仍会系统性污染错误笔记本。

This matters because the field often treats failure-derived artifacts as higher-value data, but most current pipelines still rely on weak judges, heuristic filters, or strong foundation models acting as post hoc critics. \[Cao25\] still depends on LLM-based validation. \[Che24\] uses case-conditioned prompting to reduce builder hallucinations but not to eliminate them. \[Xie25b\] keeps a human success signal in the loop for adding successful trajectories. The deeper issue is that there is no settled causal test for whether a transformed lesson actually caused later improvement. \[Ni26\] explicitly points toward attribution tracking and causal effect quantification as future work, which is unusually direct. A mature version of this line of research would need counterfactual replay, patch-level attribution, and failure taxonomies that distinguish wrong abstraction from wrong execution from wrong retrieval.

这很关键，因为该领域常把失败派生产物视为更高价值数据，但多数当前流水线仍依赖弱裁判器、启发式过滤器，或由强基础模型充当事后批评者。\[Cao25\] 仍依赖基于 LLM 的验证。\[Che24\] 使用案例条件化提示来减少构建器幻觉，但不能消除幻觉。\[Xie25b\] 在添加成功轨迹时保留人工成功信号。更深层问题是，尚无稳定的因果测试来判断转化后的经验是否确实造成后续改进。\[Ni26\] 明确把归因跟踪和因果效应量化指向未来工作，这一点相当直接。该研究线的成熟版本需要反事实回放、补丁级归因，以及能区分错误抽象、错误执行和错误检索的失败分类体系。

### Static memory artifacts break in dynamic, partially observable environments

### 静态记忆产物会在动态、部分可观察环境中失效

A broad challenge is that transformed experience is often more stable than the environment it is meant to control. \[Wan24\] shows this clearly with static workflows that fail when an unexpected pop-up changes the interaction path. \[Xie25\] is motivated by the fact that app interfaces update rapidly and differ across platforms, which makes static knowledge stale. \[Liu23\] acknowledges that its robot failure summaries assume a largely static environment outside the robot’s own actions. \[Hua25e\] frames web navigation as an unknown MDP and shows that replay and reflection mainly solve navigation failures, not complex plan execution. \[Liu25b\] exposes the same problem from the video side. Continuous videos must be converted into sparse agent actions, and the resulting trajectories help only when relevant videos exist and remain behaviorally aligned with the current interface.

一个广泛挑战是，转化后的经验常常比它要控制的环境更稳定。\[Wan24\] 用静态工作流清楚展示了这一点：当意外弹窗改变交互路径时，工作流会失败。\[Xie25\] 的动机来自应用界面快速更新且跨平台存在差异，这会使静态知识过时。\[Liu23\] 承认，其机器人失败摘要假设除机器人自身动作外，环境大体静态。\[Hua25e\] 将 Web 导航表述为未知 MDP，并显示回放和反思主要解决导航失败，而非复杂计划执行。\[Liu25b\] 从视频侧暴露了相同问题。连续视频必须转化为稀疏智能体动作，只有当相关视频存在并且与当前界面保持行为对齐时，得到的轨迹才有帮助。

This challenge matters because transformed experience is often treated as durable knowledge, but much of it is really cached adaptation to a moving interface. The issue is not only staleness. It is that many current artifacts do not encode what would invalidate them. \[Mi26b\] is notable for making temporal validity and survival pressure part of the memory design. \[Cao25\] and \[Zha25f\] also move in this direction through pruning, editing, and contradiction management. But most systems still optimize for adding memory, not for detecting expiration. Concrete progress would look like benchmarks where interface drift, hidden state changes, and stochastic branches are first-class evaluation axes, along with memory systems that log why an item was retired.

这一挑战重要，是因为转化后的经验常被当作持久知识，但其中很大一部分其实只是对移动界面的缓存适配。问题不只是过时。许多当前产物没有编码哪些变化会使它们失效。\[Mi26b\] 值得关注，因为它把时间有效性和生存压力纳入记忆设计。\[Cao25\] 与 \[Zha25f\] 也通过剪枝、编辑和矛盾管理朝这个方向推进。但多数系统仍优化添加记忆，而非检测失效。具体进展可以表现为把界面漂移、隐藏状态变化和随机分支作为一等评估轴的基准，以及能记录某个条目为何被退役的记忆系统。

### Strong model dependence is much larger than many papers admit

### 强模型依赖比许多论文承认的更大

A recurring hidden pattern is that the same paper often proves both that experience helps and that only sufficiently capable models can transform or use it well. \[Ni26\] is the clearest example. The 35B model can act reasonably well on DocVQA, but it is a poor skill author, which creates an author-user dissociation between execution skill and reflective skill. \[Liu25e\] makes a closely related point through the cognitive-threshold hypothesis. The 7B backbone fails to benefit from memory and can even regress slightly, while larger backbones gain substantially. \[Wan26\] shows that richer skill hierarchies help stronger models but can hurt weaker ones through over-imitation. \[Suz25\] also reports that adaptive memory works far better for stronger models because weaker ones cannot reliably populate or curate the memory in the first place. \[Hua25\] notes that a frozen base model caps the quality of the reflections it can distill.

一个反复出现的隐性模式是：同一篇论文常常同时证明经验有帮助，也证明只有能力足够的模型才能很好地转化或使用经验。\[Ni26\] 是最清楚的例子。35B 模型可以在 DocVQA 上表现得相当好，但它是糟糕的技能作者，这造成执行技能与反思技能之间的作者-用户分离。\[Liu25e\] 通过认知阈值假说提出密切相关的观点。7B 主干无法从记忆中获益，甚至可能轻微退化，而更大主干获得显著收益。\[Wan26\] 显示，更丰富的技能层级帮助强模型，但会因过度模仿伤害弱模型。\[Suz25\] 也报告称，自适应记忆对强模型有效得多，因为弱模型一开始就无法可靠填充或策展记忆。\[Hua25\] 指出，冻结基础模型会限制其可蒸馏反思的质量上限。

This is important for a survey article because it complicates any simple claim that experience transformation is an architecture-level improvement independent of model scale. In many papers, the transformed artifact is only as good as the model that extracts it and only as useful as the model that can interpret it. That means the field has two distinct transfer problems. One is transfer of experience across tasks. The other is transfer of experience across model capability levels. \[Yan25d\] and \[Wan23c\] are more optimistic because they treat natural-language or code artifacts as model-agnostic, but even they depend on strong generators and verifiers. A strong future benchmark should therefore separate extractor quality, artifact quality, and consumer quality rather than reporting only end-to-end gains.

这对综述文章很重要，因为它使“经验转化是独立于模型规模的架构级改进”这种简单主张变得复杂。在许多论文中，转化产物的质量取决于抽取它的模型，效用又取决于能解释它的模型。这意味着该领域有两个不同迁移问题：一个是经验跨任务迁移，另一个是经验跨模型能力层级迁移。\[Yan25d\] 与 \[Wan23c\] 更乐观，因为它们把自然语言或代码产物视为与模型无关，但即便如此，它们也依赖强生成器和验证器。因此，未来强基准应区分抽取器质量、产物质量和消费模型质量，而不是只报告端到端增益。

### Memory lifecycle management is underdeveloped and mostly heuristic

### 记忆生命周期管理发展不足，且大多依赖启发式

Many papers now recognize that append-only memory is unsustainable, but the actual maintenance logic is still heuristic-heavy. \[Cao25\] uses utility thresholds and retrieval counts to decide what to delete. \[For25\] admits its duplicate and confidence thresholds lack theoretical grounding, and its pruning strategy can forget rare but important procedures. \[Su25\] explicitly calls for consolidation and lifecycle management as the notebook grows. \[Zha25f\] proposes contradiction detection and periodic pruning because evolving playbooks can collapse or accumulate stale entries. \[Mi26b\] gives the most forceful argument, showing how redundant or outdated memory becomes a toxic prior in GUI settings. \[Ma25\] makes a parallel point at ingestion time by arguing that early filtering heuristics create subjective bias or over-storage.

许多论文已经认识到只追加记忆不可持续，但实际维护逻辑仍强依赖启发式。\[Cao25\] 使用效用阈值和检索次数来决定删除什么。\[For25\] 承认其重复项阈值和置信度阈值缺少理论基础，其剪枝策略可能遗忘罕见但重要的过程。\[Su25\] 随着笔记本增长，明确呼吁整合与生命周期管理。\[Zha25f\] 提出矛盾检测和周期性剪枝，因为演化中的行动手册可能崩塌或积累陈旧条目。\[Mi26b\] 给出最有力的论证，显示冗余或过时记忆如何在 GUI 设置中变成有毒先验。\[Ma25\] 在摄入时提出平行观点，认为早期过滤启发式会造成主观偏置或过度存储。

The field therefore has a maintenance problem before it has a scaling problem. The key issue is not just capacity. It is deciding when two memories are duplicates, when they are variants, when one supersedes another, and when a rare item should be preserved despite low use. \[Fan25\] and \[For25\] show that procedural memory quality saturates and then declines once the library grows too large. \[SkillClaw\] is not in the final table, but its six-day user simulation similarly shows rapid early gains followed by plateaus in some categories. The implication, marked here as an inference, is that memory stores need explicit notions of versioning, dominance, and exception preservation rather than raw frequency-based utility alone.

因此，该领域先遇到维护问题，才遇到规模问题。关键不只是容量，而是判断两个记忆何时重复、何时只是变体、何时一个取代另一个，以及罕见条目即便使用率低也应保留的条件。\[Fan25\] 与 \[For25\] 显示，当库过大时，程序性记忆质量会先饱和再下降。\[SkillClaw\] 不在最终表格中，但其为期六天的用户模拟同样显示，早期快速收益之后，一些类别进入平台期。这里标为推断的含义是：记忆存储需要显式的版本化、支配关系和例外保留概念，不能只依赖原始频率式效用。

### Evaluation remains narrower and more convenient than the papers often imply

### 评估仍比论文常暗示的更窄、更便利

A survey discussion section should state plainly that many reported gains are benchmark-conditioned. \[Zha23c\] restricts itself to deterministic environments and even modifies WebShop for reproducibility. \[Fu24\] evaluates WebArena only on Reddit and omits Reflexion there because of token limits. \[Che25d\] excludes same-repository experiences to avoid leakage, which is sensible experimentally but strips away an important real-world source of repeated experience. \[Liu25\] limits VisualWebArena evaluation for cost reasons and relies on a small amount of human-annotated gold data. \[Liu25b\] excludes inaccessible domains and falls back to base performance whenever no matching videos are found. \[Yan25d\] notes that evaluation scripts may penalize creative but valid solutions, which means some apparent agent failures are really evaluator failures.

综述讨论部分应直接说明，许多已报告增益受基准条件约束。\[Zha23c\] 将自身限制在确定性环境中，甚至为可复现性修改 WebShop。\[Fu24\] 只在 Reddit 上评估 WebArena，并因 token 限制在那里省略 Reflexion。\[Che25d\] 为避免泄漏排除同仓库经验，这在实验上合理，却剥离了真实世界中重复经验的重要来源。\[Liu25\] 因成本原因限制 VisualWebArena 评估，并依赖少量人工标注黄金数据。\[Liu25b\] 排除无法访问的域名，并在找不到匹配视频时退回基础性能。\[Yan25d\] 指出评估脚本可能惩罚有创造性但有效的解法，这意味着一些表面上的智能体失败其实是评估器失败。

These choices do not invalidate the papers, but they do mean that the field still lacks a benchmark suite for memory lifecycle, cross-session adaptation, and experience transfer under realistic noise. Existing evaluations overstate maturity when they rely on deterministic resets, strong judges, curated training subsets, or static interfaces. A stronger literature would verify not only whether memory improves average success, but also whether it survives benchmark drift, interface updates, repeated long-term use, and evaluator disagreement.

这些选择不会推翻论文价值，但它们确实意味着，该领域仍缺少面向真实噪声下记忆生命周期、跨会话适配和经验迁移的基准套件。当现有评估依赖确定性重置、强裁判器、策划训练子集或静态界面时，会高估成熟度。更强的文献应验证的不仅是记忆是否提升平均成功率，还包括它是否能承受基准漂移、界面更新、重复长期使用和评估器分歧。

### Cross-carrier transfer is still mostly aspirational

### 跨载体迁移仍主要停留在愿景层面

Although the survey topic is experience transformation across carrier forms, most of the literature still stays inside a single family. \[Shi23b\], \[Zha23c\], \[Fu24\], \[Cao25\], \[Yan25d\], and \[Zha25f\] are primarily text to text. \[Wan23c\] and \[Wan26\] move experience into executable skills, but largely within stable tool interfaces. \[Xie25\] and \[Xie25b\] add multimodal GUI grounding, yet the artifact remains tied to GUI affordances. \[Liu25b\] imports video demonstrations at inference time, but the result is still in-context trajectory guidance rather than durable cross-carrier learning. Even \[Sar25\], which explicitly compares in-context replay and fine-tuning, finds that transforming experience into weights is not uniformly superior.

尽管本文综述主题是跨载体形式的经验转化，多数文献仍停留在单一族内部。\[Shi23b\]、\[Zha23c\]、\[Fu24\]、\[Cao25\]、\[Yan25d\] 和 \[Zha25f\] 主要是文本到文本。\[Wan23c\] 与 \[Wan26\] 将经验转入可执行技能，但大体发生在稳定工具接口内。\[Xie25\] 与 \[Xie25b\] 加入多模态 GUI grounding，但产物仍绑定 GUI 可供性。\[Liu25b\] 在推理时引入视频示范，但结果仍是上下文内轨迹引导，而非持久跨载体学习。即便 \[Sar25\] 明确比较上下文内回放和微调，也发现把经验转化为权重并非一致更优。

The result is a field with many local transformations and few genuine carrier bridges. Very little work studies how a reflection becomes a workflow, how a workflow becomes a skill, how a skill becomes training data, or when external memory should be internalized into parameters. The composite pipelines in this project point to that broader space, but the core literature here still treats carrier choice as a local design decision rather than a full transformation chain. That gap is not just taxonomic. It blocks principled comparison between external memory, executable libraries, and parametric adaptation.

结果是，该领域有许多局部转化，却很少有真正的载体桥接。很少有工作研究反思如何变成工作流、工作流如何变成技能、技能如何变成训练数据，或外部记忆何时应内化到参数中。本项目中的复合流水线指向更广阔的空间，但这里的核心文献仍把载体选择当作局部设计决策，而非完整转化链。这个缺口不只是分类问题。它阻碍了外部记忆、可执行库和参数适配之间的原则性比较。

## Future directions

## 未来方向

### Adaptive multi-granular memory

### 自适应多粒度记忆

Several papers converge on the need for memory systems that can move between granularity levels rather than committing early to one form. \[Fan25\] already shows that scripts and trajectories complement each other. \[Ye25b\] reaches a similar conclusion in a hierarchical hindsight setting, where removing high-level memory hurts more than removing low-level memory, but both matter. \[Yan25\] explicitly separates coarse focus points, hybrid-grained tips, and fine-grained key information, while \[Xie25b\] does the same for execution, core, and meta skills. The obvious next step is not another fixed hierarchy, but adaptive movement across levels during execution.

多篇论文共同指向一种需要：记忆系统应能在粒度层级之间移动，而不是早早绑定一种形式。\[Fan25\] 已经显示，脚本和轨迹彼此互补。\[Ye25b\] 在层级后见设置中得到相似结论：移除高层记忆的伤害大于移除低层记忆，但两者都重要。\[Yan25\] 明确分离粗粒度关注点、混合粒度提示和细粒度关键信息，\[Xie25b\] 则对执行技能、核心技能和元技能做了类似区分。显然的下一步并非另一个固定层级，而是在执行期间进行跨层级自适应移动。

Concrete progress would look like a system that begins with abstract strategic guidance, then drills into local executable detail only when uncertainty rises or grounding fails. Verification should ask not only whether the agent succeeded, but whether the chosen level of abstraction was appropriate for the state. This direction is strongly motivated by existing evidence, even when the papers stop short of stating it so explicitly. The inference comes from the repeated finding that single-level memory either overloads context or omits action-critical detail.

具体进展可以表现为一种系统：以抽象策略指导开始，只在不确定性上升或落地失败时才钻入局部可执行细节。验证不应只问智能体是否成功，还应问所选抽象层级是否适合当前状态。现有证据强烈推动这一方向，即使论文没有如此明确地表述。这个推断来自一个反复发现：单层级记忆要么使上下文过载，要么遗漏动作关键细节。

### Stronger validation and causal attribution for memory updates

### 面向记忆更新的更强验证与因果归因

A second direction is to make memory editing evidence-based rather than heuristic. \[Ni26\] explicitly calls for attribution tracking and automated pruning of ineffective skill sections. \[For25\] proposes hierarchical buffering because flat frequency-based pruning can discard rare but vital procedures. \[Su25\] asks for lifecycle management, and \[Zha25f\] points to contradiction detection and selective unlearning. Across these papers, the missing ingredient is a causal notion of utility.

第二个方向是让记忆编辑基于证据，而非基于启发式。\[Ni26\] 明确呼吁归因跟踪和无效技能片段的自动剪枝。\[For25\] 提出层级缓冲，因为扁平的基于频率的剪枝可能丢弃罕见但关键的过程。\[Su25\] 要求生命周期管理，\[Zha25f\] 则指向矛盾检测和选择性遗忘。这些论文共同缺少的是关于效用的因果概念。

Concrete progress would mean testing a candidate memory item under counterfactual replay, ablation-on-use, or patch-level intervention. If a retrieved rule is ignored, the system should know that. If a workflow only helps because it reminds the model of a hidden precondition, that contribution should be recorded separately from the rest of the workflow. Verification should therefore move beyond LLM-as-judge pass fail labels toward action-level effect estimation. This would directly address the current uncertainty around whether a stored item is genuinely useful or merely correlated with prior success.

具体进展意味着在反事实回放、使用时消融或补丁级干预下测试候选记忆项。如果检索到的规则被忽略，系统应知道这一点。如果一个工作流的帮助只来自提醒模型某个隐藏前置条件，这一贡献应与工作流其他部分分开记录。因此，验证应从 LLM 裁判器式通过/失败标签转向动作级效果估计。这会直接处理当前的不确定性：一个存储项是真正有用，还是仅与先前成功相关。

### Hybrid carrier pipelines rather than single-carrier commitment

### 混合载体流水线，而非绑定单一载体

The literature is ripe for more deliberate movement across carrier forms. \[Wan23c\] shows the value of code skills. \[Wan24\], \[Fan25\], and \[Cao25\] show the value of workflow and procedural memory. \[Sar25\] provides evidence that in-context examples and fine-tuning can trade places depending on the domain. \[Ma25\] focuses on distillation kernels that could feed multiple downstream memory managers. Together these results suggest that the next step is not to pick one carrier, but to learn when to hand off between carriers.

文献已经适合更有意识地跨载体形式移动。\[Wan23c\] 显示代码技能的价值。\[Wan24\]、\[Fan25\] 和 \[Cao25\] 显示工作流与程序性记忆的价值。\[Sar25\] 提供证据表明，上下文内样例和微调可随领域不同而互换位置。\[Ma25\] 聚焦可供多个下游记忆管理器使用的蒸馏内核。合在一起，这些结果提示下一步不应是选择一个载体，而应学习何时在载体之间交接。

Concrete progress would look like pipelines such as trajectory to reflection to workflow to executable skill, or trajectory to notebook entry to curated training example to policy update. Verification should compare full chains against their intermediate stopping points. A paper in this direction would be especially valuable if it measured information loss, transfer gain, and maintenance cost at each stage rather than only reporting the final task score.

具体进展可以表现为轨迹到反思、到工作流、到可执行技能的流水线，或轨迹到笔记本条目、到策展训练样例、到策略更新的流水线。验证应把完整链条与其中间停止点比较。这个方向上的论文若能测量每个阶段的信息损失、迁移增益和维护成本，而不是只报告最终任务得分，将特别有价值。

### Continual maintenance with versioning, contradiction handling, and retirement

### 带版本化、矛盾处理和退役机制的持续维护

The most mature memory papers already hint that long-term performance depends on maintenance more than storage. \[Cao25\] adds selective addition and utility-based deletion. \[Mi26b\] introduces survival-style memory regulation. \[Zha25f\] demonstrates the danger of context collapse under monolithic rewriting and therefore argues for itemized incremental updates. \[Yan26\] uses explicit versioned skills, and \[SkillClaw\] shows iterative evolution over days rather than one-shot construction. The obvious next direction is to make maintenance a first-class object of study.

最成熟的记忆论文已经暗示，长期性能对维护的依赖大于对存储的依赖。\[Cao25\] 加入选择性添加和基于效用的删除。\[Mi26b\] 引入生存式记忆调节。\[Zha25f\] 展示单体重写下上下文崩塌的危险，因此主张条目化增量更新。\[Yan26\] 使用显式版本化技能，\[SkillClaw\] 展示跨天迭代演化，而非一次性构建。显然的下一方向是把维护变成一等研究对象。

Concrete progress would include version graphs, supersession links, contradiction checks, and explicit retirement reasons. Evaluation should report not just bank size and success rate, but churn, redundancy, stale-memory rate, and recovery after erroneous updates. This direction also has practical value for privacy and governance, because selective unlearning is only possible when memory items are explicit, localizable, and versioned.

具体进展包括版本图、替代链接、矛盾检查和显式退役原因。评估不应只报告记忆库大小和成功率，还应报告周转率、冗余度、陈旧记忆率，以及错误更新后的恢复能力。这个方向对隐私和治理也有实践价值，因为只有当记忆项显式、可定位且版本化时，选择性遗忘才可行。

### Better support for learning from failure without poisoning the memory bank

### 更好地支持从失败中学习，同时避免污染记忆库

Failure is too informative to ignore, but current methods still convert it unreliably. \[Shi23b\] depends on accurate self-evaluation. \[Hu25\] improves by rewriting failed trajectories into positive supervision. \[Ye25b\] uses hindsight reflection to infer subgoal structure. \[Su25\] clusters failures into reusable notebook entries. \[Hua25e\] and \[Liu23\] show that failure explanation can expose hidden state and navigation issues that successful traces never reveal. The direction is clear: future systems should treat failures as structured evidence, not just bad traces to discard.

失败含有太多信息，不能忽略，但当前方法对它的转化仍不可靠。\[Shi23b\] 依赖准确自我评估。\[Hu25\] 通过把失败轨迹重写为正向监督来改进。\[Ye25b\] 使用后见反思推断子目标结构。\[Su25\] 将失败聚类为可复用笔记本条目。\[Hua25e\] 与 \[Liu23\] 显示，失败解释可以暴露成功轨迹从未揭示的隐藏状态和导航问题。方向很清楚：未来系统应把失败当作结构化证据，而不是只当作要丢弃的坏轨迹。

Concrete progress would look like memory schemas that separate failure cause, failed context, attempted repair, and verified fix. Verification would need to test whether the lesson helps avoid the same failure family without suppressing legitimate exploration. This is especially important because several papers already show that excessive conservatism and pessimistic reflection can create new errors.

具体进展可以表现为能分离失败原因、失败上下文、尝试修复和已验证修复的记忆模式。验证需要测试该经验是否有助于避免同一失败族，同时不压制合理探索。这一点尤其重要，因为已有多篇论文显示，过度保守和悲观反思会制造新错误。

### Cross-model and cross-agent transfer with attention to stylistic mismatch

### 关注风格错配的跨模型与跨智能体迁移

A major opportunity is to decouple who produces the experience from who consumes it. \[Ni26\] shows that stronger authors can write better skills than weaker ones. \[Liu25e\] shows that self-generated experience can nevertheless be easier to use than stronger foreign demonstrations because style and grounding match the consumer. \[Hua25\] and \[Wan26ap\] both point toward cross-user or governed shared memory. \[Yan26\] goes further by presenting skills as inspectable transferable objects.

一个重要机会是解耦经验生产者和经验消费者。\[Ni26\] 显示，强作者可以比弱作者写出更好的技能。\[Liu25e\] 显示，自生成经验仍可能比更强的外部示范更容易使用，因为风格和 grounding 与消费者匹配。\[Hua25\] 与 \[Wan26ap\] 都指向跨用户或受治理的共享记忆。\[Yan26\] 进一步把技能呈现为可检查的可迁移对象。

The next step is to make transfer itself measurable. Concrete progress would mean reporting extractor model, consumer model, and transfer gap separately, then studying which artifact properties preserve utility across that gap. A useful benchmark would test the same artifact on stronger and weaker agents, as well as on agents with different control styles. This would move the field beyond vague claims of model-agnostic memory.

下一步是让迁移本身可测。具体进展意味着分别报告抽取模型、消费模型和迁移差距，然后研究哪些产物属性能跨越该差距保有效用。一个有用基准会在更强和更弱智能体上测试同一产物，也会在控制风格不同的智能体上测试。这会推动该领域越过关于模型无关记忆的含糊主张。

### More realistic benchmarks for memory lifecycle and environment drift

### 面向记忆生命周期和环境漂移的更真实基准

Many current limitations sections already name the missing settings. \[Aza25\] wants real-world web benchmarks beyond controlled WebArena. \[Liu23\] points to dynamic robot environments. \[Xie25\] highlights frequent app updates. \[Wan24\] exposes brittleness to interface changes. \[Yan25d\] notes that rigid evaluators can mis-score creative solutions. These observations collectively support a benchmark agenda centered on drift, long-term reuse, and open-world evaluation.

许多当前 limitations 部分已经点出了缺失设置。\[Aza25\] 希望看到超越受控 WebArena 的真实世界 Web 基准。\[Liu23\] 指向动态机器人环境。\[Xie25\] 强调应用频繁更新。\[Wan24\] 暴露出对界面变化的脆弱性。\[Yan25d\] 指出僵硬评估器可能错判有创造性的解法。这些观察共同支持以漂移、长期复用和开放世界评估为中心的基准议程。

Concrete progress would be a benchmark suite with repeated sessions, interface updates, partial observability, stale memory traps, and delayed consequences of memory use. Success should be measured not only by immediate task completion, but also by whether the agent learns without contaminating itself over time. That kind of benchmark would make it much easier to compare reflection systems, procedural memory systems, and skill libraries on the same axes.

具体进展将是一个包含重复会话、界面更新、部分可观察性、陈旧记忆陷阱和记忆使用延迟后果的基准套件。成功不应只由即时任务完成衡量，还应由智能体是否能随时间学习且不污染自身来衡量。这类基准会更容易在同一轴线上比较反思系统、程序性记忆系统和技能库。

### Bridging external memory and parametric learning

### 桥接外部记忆与参数化学习

The last major direction is to connect external memory with weight updates instead of treating them as separate paradigms. \[Sar25\] already shows that fine-tuning on accumulated examples helps in some environments but not all. \[Liu25e\] explicitly names direct policy integration as future work. \[Zha25f\] argues that evolving context can serve as a flexible alternative to fine-tuning, which implicitly raises the question of when that alternative stops being enough. \[Ma25\] is especially relevant because its distillation kernel is downstream-agnostic and could, in principle, feed either retrieval systems or training pipelines.

最后一个主要方向是把外部记忆与权重更新连接起来，而不是把它们当作彼此分离的范式。\[Sar25\] 已经显示，在累积样例上微调对某些环境有帮助，但并非对所有环境有帮助。\[Liu25e\] 明确把直接策略整合列为未来工作。\[Zha25f\] 认为演化上下文可作为微调的灵活替代方案，这隐含提出一个问题：这种替代方案何时不再足够。\[Ma25\] 尤其相关，因为它的蒸馏内核与下游无关，原则上可以供检索系统或训练流水线使用。

Concrete progress would look like agents that externalize experience first, validate and maintain it there, then selectively internalize only the stable residue into model updates. Verification should compare whether the internalized knowledge remains robust after the external artifact is removed. That would finally make carrier transformation a longitudinal process rather than a one-step design choice.

具体进展可以表现为智能体先外部化经验，在外部验证和维护，再只把稳定残留选择性内化为模型更新。验证应比较在移除外部产物后，内化知识是否仍保持鲁棒。这样才能最终把载体转化变成纵向过程，而非一步式设计选择。

---

## References

\[Shi23b\] N. Shinn, F. Cassano, B. Labash, A. Gopinath, K. Narasimhan, and S. Yao, “Reflexion: language agents with verbal reinforcement learning,” *Advances in Neural Information Processing Systems 36*, Mar. 2023, doi: [10.52202/075280-0377](https://doi.org/10.52202/075280-0377).

\[Zha23c\] A. Zhao, D. Huang, Q. Xu, M. Lin, Y. Liu, and G. Huang, “ExpeL: LLM Agents Are Experiential Learners,” *AAAI Conference on Artificial Intelligence*, pp. 19632–19642, Aug. 2023, doi: [10.48550/arXiv.2308.10144](https://doi.org/10.48550/arXiv.2308.10144).

\[Fu24\] Y. Fu *et al.*, “AutoGuide: Automated Generation and Selection of Context-Aware Guidelines for Large Language Model Agents,” *ArXiv*, vol. abs/2403.08978, Mar. 2024, doi: [10.48550/arXiv.2403.08978](https://doi.org/10.48550/arXiv.2403.08978).

\[Che24\] M. Chen, Y. Li, Y. Yang, S. Yu, B. Lin, and X. He, “AutoManual: Constructing Instruction Manuals by LLM Agents via Interactive Environmental Learning,” *Advances in Neural Information Processing Systems 37*, May 2024, doi: [10.52202/079017-0019](https://doi.org/10.52202/079017-0019).

\[Maj23\] B. P. Majumder *et al.*, “CLIN: A Continually Learning Language Agent for Rapid Task Adaptation and Generalization,” *ArXiv*, vol. abs/2310.10134, Oct. 2023, doi: [10.48550/arXiv.2310.10134](https://doi.org/10.48550/arXiv.2310.10134).

\[Hu25\] M. Hu, B. V. Durme, J. Andreas, and H. Jhamtani, “Sample-Efficient Online Learning in LM Agents via Hindsight Trajectory Rewriting,” *ArXiv*, vol. abs/2510.10304, Oct. 2025, doi: [10.48550/arXiv.2510.10304](https://doi.org/10.48550/arXiv.2510.10304).

\[Wan24\] Z. Wang, J. Mao, D. Fried, and G. Neubig, “Agent Workflow Memory,” *ArXiv*, vol. abs/2409.07429, Sep. 2024, doi: [10.48550/arXiv.2409.07429](https://doi.org/10.48550/arXiv.2409.07429).

\[Fan25\] R. Fang *et al.*, “Memp: Exploring Agent Procedural Memory,” *ArXiv*, vol. abs/2508.06433, Aug. 2025, doi: [10.48550/arXiv.2508.06433](https://doi.org/10.48550/arXiv.2508.06433).

\[Cao25\] Z. Cao *et al.*, “Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution,” *ArXiv*, vol. abs/2512.10696, Dec. 2025, doi: [10.48550/arXiv.2512.10696](https://doi.org/10.48550/arXiv.2512.10696).

\[Ni26\] J. Ni *et al.*, “Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills,” Mar. 26, 2026.

\[Wan23c\] G. Wang *et al.*, “Voyager: An Open-Ended Embodied Agent with Large Language Models,” *ArXiv*, vol. abs/2305.16291, May 2023, doi: [10.48550/arXiv.2305.16291](https://doi.org/10.48550/arXiv.2305.16291).

\[Wan26\] C. Wang *et al.*, “SkillX: Automatically Constructing Skill Knowledge Bases for Agents,” Apr. 06, 2026.

\[Xie25\] B. Xie *et al.*, “GUI-explorer: Autonomous Exploration and Mining of Transition-aware Knowledge for GUI Agent,” *Annual Meeting of the Association for Computational Linguistics*, pp. 5650–5667, May 2025, doi: [10.48550/arXiv.2505.16827](https://doi.org/10.48550/arXiv.2505.16827).

\[Xie25b\] Y. Xie *et al.*, “Mirage-1: Augmenting and Updating GUI Agent with Hierarchical Multimodal Skills,” *ArXiv*, vol. abs/2506.10387, Jun. 2025, doi: [10.48550/arXiv.2506.10387](https://doi.org/10.48550/arXiv.2506.10387).

\[Liu25b\] Y. Liu *et al.*, “Learning from Online Videos at Inference Time for Computer-Use Agents,” *ArXiv*, vol. abs/2511.04137, Nov. 2025, doi: [10.48550/arXiv.2511.04137](https://doi.org/10.48550/arXiv.2511.04137).

\[Zha25f\] Q. Zhang *et al.*, “Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models,” *ArXiv*, vol. abs/2510.04618, Oct. 2025, doi: [10.48550/arXiv.2510.04618](https://doi.org/10.48550/arXiv.2510.04618).

\[Ma25\] W. Ma, J. Nan, W. Wu, and Y. Chen, “What Deserves Memory: Adaptive Memory Distillation for LLM Agents,” Aug. 05, 2025.

\[Yan25d\] C. Yang *et al.*, “Learning on the Job: An Experience-Driven Self-Evolving Agent for Long-Horizon Tasks,” *ArXiv*, vol. abs/2510.08002, Oct. 2025, doi: [10.48550/arXiv.2510.08002](https://doi.org/10.48550/arXiv.2510.08002).

\[Yan26b\] D. Yan *et al.*, “M2: Dual-Memory Augmentation for Long-Horizon Web Agents via Trajectory Summarization and Insight Retrieval,” *ArXiv*, vol. abs/2603.00503, Feb. 2026, doi: [10.48550/arXiv.2603.00503](https://doi.org/10.48550/arXiv.2603.00503).

\[Liu23\] Z. Liu, A. Bahety, and S. Song, “REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction,” *ArXiv*, vol. abs/2306.15724, Jun. 2023, doi: [10.48550/arXiv.2306.15724](https://doi.org/10.48550/arXiv.2306.15724).

\[Aza25\] R. Azam, A. Vempaty, and A. Jagmohan, “Reflection-Based Memory For Web navigation Agents,” *ArXiv*, vol. abs/2506.02158, Jun. 2025, doi: [10.48550/arXiv.2506.02158](https://doi.org/10.48550/arXiv.2506.02158).

\[Mi26b\] H. Mi *et al.*, “Darwinian Memory: A Training-Free Self-Regulating Memory System for GUI Agent Evolution,” *ArXiv*, vol. abs/2601.22528, Jan. 2026, doi: [10.48550/arXiv.2601.22528](https://doi.org/10.48550/arXiv.2601.22528).

\[Che25d\] S. Chen *et al.*, “SWE-Exp: Experience-Driven Software Issue Resolution,” *ArXiv*, vol. abs/2507.23361, Jul. 2025, doi: [10.48550/arXiv.2507.23361](https://doi.org/10.48550/arXiv.2507.23361).

\[Sar25\] V. Sarukkai, Z. Xie, and K. Fatahalian, “Self-Generated In-Context Examples Improve LLM Agents for Sequential Decision-Making Tasks,” *ArXiv*, vol. abs/2505.00234, May 2025, doi: [10.48550/arXiv.2505.00234](https://doi.org/10.48550/arXiv.2505.00234).

\[Su25\] X. Su, Y. Zhang, H. Luo, X. Liu, and L. Huang, “Mistake Notebook Learning: Batch-Clustered Failures for Training-Free Agent Adaptation,” Dec. 12, 2025.

\[Hua25e\] T. Huang, K. Basu, I. Abdelaziz, P. Kapanipathi, J. May, and M. Chen, “R2D2: Remembering, Replaying and Dynamic Decision Making with a Reflective Agentic Memory,” *Annual Meeting of the Association for Computational Linguistics*, pp. 30318–30330, Jan. 2025, doi: [10.18653/v1/2025.acl-long.1464](https://doi.org/10.18653/v1/2025.acl-long.1464).

\[Liu25e\] G. Liu *et al.*, “WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance,” *ArXiv*, vol. abs/2511.12997, Nov. 2025, doi: [10.48550/arXiv.2511.12997](https://doi.org/10.48550/arXiv.2511.12997).

\[Suz25\] M. Suzgun, M. Yüksekgönül, F. Bianchi, D. Jurafsky, and J. Zou, “Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory,” *ArXiv*, vol. abs/2504.07952, Apr. 2025, doi: [10.48550/arXiv.2504.07952](https://doi.org/10.48550/arXiv.2504.07952).

\[Hua25\] Y. Huang, Y. Liu, R. Zhao, X. Zhong, X.-R. Yue, and L. Jiang, “MemOrb: A Plug-and-Play Verbal-Reinforcement Memory Layer for E-Commerce Customer Service,” *ArXiv*, vol. abs/2509.18713, Sep. 2025, doi: [10.48550/arXiv.2509.18713](https://doi.org/10.48550/arXiv.2509.18713).

\[For25\] S. Forouzandeh, W. Peng, P. Moradi, X. Yu, and M. Jalili, “Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement,” *ArXiv*, vol. abs/2512.18950, Dec. 2025, doi: [10.48550/arXiv.2512.18950](https://doi.org/10.48550/arXiv.2512.18950).

\[Liu25\] Y. Liu, C. Si, K. R. Narasimhan, and S. Yao, “Contextual Experience Replay for Self-Improvement of Language Agents,” *Annual Meeting of the Association for Computational Linguistics*, pp. 14179–14198, Jun. 2025, doi: [10.48550/arXiv.2506.06698](https://doi.org/10.48550/arXiv.2506.06698).

\[Ye25b\] S. Ye, C. Yu, K. Ke, C. Xu, and Y. Wei, “H2R: Hierarchical Hindsight Reflection for Multi-Task LLM Agents,” *2025 IEEE International Conference on Agentic AI (ICA)*, pp. 94–99, Sep. 2025, doi: [10.1109/ICA67499.2025.00030](https://doi.org/10.1109/ICA67499.2025.00030).

\[Yan25\] W. Yang, J. Xiao, H. Zhang, Q. Zhang, Y. Wang, and B. Xu, “Coarse-to-Fine Grounded Memory for LLM Agent Planning,” *Conference on Empirical Methods in Natural Language Processing*, pp. 13029–13056, Aug. 2025, doi: [10.48550/arXiv.2508.15305](https://doi.org/10.48550/arXiv.2508.15305).

\[Yan26\] Y. Yang *et al.*, “AutoSkill: Experience-Driven Lifelong Learning via Skill Self-Evolution,” *ArXiv*, vol. abs/2603.01145, Mar. 2026, doi: [10.48550/arXiv.2603.01145](https://doi.org/10.48550/arXiv.2603.01145).

\[Wan26ap\] Q. Wang *et al.*, “MemGovern: Enhancing Code Agents through Learning from Governed Human Experiences,” *ArXiv*, vol. abs/2601.06789, Jan. 2026, doi: [10.48550/arXiv.2601.06789](https://doi.org/10.48550/arXiv.2601.06789).
