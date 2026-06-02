# 3. Tokenized-to-Tokenized Transformations

本章讨论经验在 Tokenized 载体层级内部的两种转化方式：Narrative Abstraction（Narrative → Narrative）与 Schematic Formalization（Narrative → Schematic）。两条路径共享同一源端——Agent 序贯决策中产生的具体轨迹（reasoning trace、tool-use trajectory、GUI interaction trace 或 embodied execution record）。Narrative Abstraction 的目标 artifact 保持为自然语言形式（reflection、rule、insight 等），下游通过 language / multimodal understanding 直接阅读复用；Schematic Formalization 的目标 artifact 具有显式结构约束（code、workflow、graph 等），下游通过 parser、executor 或 graph traversal 机制性地利用其结构。本章两条路径与 Parametric Externalization 有明确边界：前者以具体 Agent 交互轨迹为输入，模型在其中扮演 abstractor、formalizer 或 synthesizer；若 artifact 主要由模型根据任务描述或内化知识直接生成、无具体轨迹作为输入，则属于后者。

<!-- Narrative Abstraction 与 Schematic Formalization 的归类不采用论文自报术语。文献中 skill、experience、memory、procedure 等词存在严重的同名异物与同物异名：Voyager 的 skill 是可执行 JavaScript 代码，ExpeL 的 insight 是自然语言规则，A-MEM 的 memory 是图节点。归类基于两个可观测属性：artifact 的结构形态（自然语言文本 / 可解析可执行结构 / 关系图），以及下游消费机制（依赖 LLM 阅读理解，还是依赖 executor/parser/graph traversal）。论文原文术语仅在做具体介绍时保留。-->

## 3.1 Narrative Abstraction:Narrative-to-Narrative Transformation

Narrative Abstraction 通过抽象、压缩、重写或归纳，从 raw Narrative trajectory 派生出新的 Narrative artifact——转化全程在 Tokenized 层内完成。转化后的 artifact 形态包括 reflection、summary、rule、insight、skill 等，后续 Agent 通过 retrieval 将其作为 in-context guidance 注入决策上下文，依靠 language / multimodal understanding 直接阅读复用。本节按经验库的维护方式将方法分为两类：Static Experience Store 中条目写入后不再回改，Dynamic Experience Store 则涉及改写、合并或淘汰。

### 3.1.1 Static Experience Store

Static Experience Store 类方法把经验抽象的产物作为只增不改的条目累积。经验库的具体形态不一：有的是任务内临时缓存，任务结束即弃；有的是构建后不再回改的持久库。共性是条目一旦写入便不再被编辑或合并。按抽象所依据的轨迹数量分为 Single-Trajectory Experience Abstraction 与 Multi-Trajectory Experience Induction 两类。

**Single-Trajectory Experience Abstraction.** 以单条 Agent trajectory 或其局部片段为输入，在一次执行或 trial 结束后，通过 reflection、summarization、critique 或 failure explanation 派生出 Narrative artifact。这类方法的基本假设是，单条轨迹本身承载了可供诊断的决策信息——失败轨迹可能暴露错误假设、无效动作或遗漏约束，成功轨迹可能包含有效的分解策略或环境交互模式。

Reflexion [Shi23b] 是这一范式的早期代表。Agent 在每次 trial 结束后，依据失败轨迹与环境反馈生成简短 reflection，将错误归因与改进建议拼接进下一轮 prompt。ReAP [Aza25] 将单条网页浏览轨迹总结为 Web-Reflection，内容覆盖有效步骤、站点功能局限、捷径与失败回溯点。MemOrb [Hua25] 在客服场景下把每轮对话及其工具调用轨迹事后压缩为一个 Orb，以 observation、emotion、outcome、context 与策略性反思组成多字段结构。Wu et al. [Wu26] 从 teacher model 合成的大规模推理轨迹中解构出 subquestion-subroutine 对，构成静态 procedural datastore，推理时模型先表述当前子问题再检索对应 subroutine 作为 hint。REFLECT [Liu23] 对机器人单次执行的多模态观测流（RGB-D 视频、音频与状态记录）做分层摘要——逐级提取 scene graph、事件级描述与子目标级摘要——并在子目标验证失败时生成 failure explanation 驱动纠错规划。WebCoach [Liu25e] 把每个已完成的 web episode 压缩为 3–5 句 summary，保留成功状态与失败模式等字段后存入 External Memory Store。在代码域，SWE-Exp [Che25d] 与 MemGovern [Wan26ap] 都从修复闭环中提纯结构化经验条目：SWE-Exp 从单次 repair trajectory 中分别提炼 comprehension experience 与 modification experience，形成带 perspective、modification、issue type 的 experience bank 条目；MemGovern 从 GitHub issue、PR、patch 的闭环修复记录中提纯 Experience Card，经 checklist 式 refine loop 保证字段质量。

<!-- Meta-Policy Reflexion [Wu25] 把失败 episode 的 retrospective reflection 写成带权重的 predicate-like 规则，测试阶段 memory 冻结，Agent 检索规则注入 prompt 并做 admissibility check。规则在测试期不再变动，归 Static；其规则形式更形式化，接近轻量 rule set，但复用仍靠阅读而非执行，归 Narrative Abstraction。 -->


**Multi-Trajectory Experience Induction.** 以多条 Agent trajectory 为输入，通过比较、聚类或合并抽取可迁移的 Narrative artifact。这类方法的基本假设是，单条轨迹中的偶然因素会在跨轨迹比较中被识别并过滤，反复出现的模式或错误则会浮现为更稳定的归纳结果。

AutoGuide [Fu24] 从同一任务的优劣轨迹对中定位首次决策分叉点，围绕分叉动作抽出与上下文绑定的 guideline，写成 when-context then-action 形式并按 context 建索引。CFGM [Yan25] 先从环境基础信息与离线 trial-and-error 轨迹得到 coarse focus points，再比较成功与失败轨迹提炼 hybrid-grained tips。M2 [Yan26b] 的 external insight bank 从历史成功日志中提炼 topic-tagged insights。


### 3.1.2 Dynamic Experience Store

Dynamic Experience Store 类方法把经验库当作随交互持续演化的对象。系统不仅写入新经验，还对已有条目做改写、合并、淘汰，使经验库在长期使用中具备自我纠错与去冗的能力。下文按四种代表性维护实践组织讨论：Operation-Driven Editing、Survival-Driven Pruning、Skill Library Curation、Multi-Tier Co-Evolution。

**Operation-Driven Editing.** 一类工作维护自然语言规则或 insight 库，并把编辑与投票写成显式 memory operation。ExpeL [Zha23c] 从成功轨迹池与失败-成功对中抽取可迁移 insight，对已有条目执行 add、edit、upvote、downvote。H2R [Ye25b] 把 hindsight reflection 拆成高层 planning memory 与低层 execution memory，支持 add、modify、upvote、downvote。AutoManual [Che24] 按 direct success、indirect success、failure 三类结果差异化抽取规则，并通过专门的 consolidation 与 formulation 阶段合并冗余、整理为 Markdown manual。ACE [Zha25f] 由 Reflector 从 reasoning trajectory 抽出 insight、failure mode 与 strategy bullet，Curator 将它们作为 delta 合并进 Context Playbook，配套语义去重与低效条目裁剪。Dynamic Cheatsheet [Suz25] 由 Curator 对解题轨迹做 usefulness 与 generalizability 评估，把可迁移内容蒸馏进 cheatsheet，并对条目执行改写、删除、合并与压缩以控制长度。

**Survival-Driven Pruning.** 另一类工作以替换、淘汰或 survival 评分驱动经验库收敛。Darwinian Memory [Mi26b] 把 GUI 经验写成以 precondition 与 goal 为索引的 memory unit，通过 evolutionary replacement、survival-based pruning 与 reputation-style inhibition 调节记忆库。R2D2 [Hua25e] 从历史 web 轨迹中截断纠错并生成可回放的修正性反思，通过 replay buffer 与 reflective update 持续替换较弱旧经验。Remember Me, Refine Me [Cao25] 从单条轨迹中抽取 keypoint-level procedural memory，持续跟踪检索与成功效用，做验证、去重和低效记忆删除。Mistake Notebook Learning [Su25] 以一批失败样本为更新单元，先按 subject 聚类再生成 mistake note，每轮经 post-update evaluation 整体验证后才接受。

**Skill Library Curation.** 围绕 skill 的工作把单次经验吸收进持续演化的技能库。Trace2Skill [Ni26] 由并行 analyst 对各条轨迹提出局部 patch，经分层 merge 与 conflict-free consolidation 合成可迁移 skill，已有 skill 可在 deepening mode 下被进一步改写。AutoSkill [Yan26] 从用户交互信号中抽取 skill candidate，经 judge 决定 add、merge 或 discard。SkillClaw [Ma26b] 汇总多用户、多 agent 的真实使用 session，由 Agentic Evolver 判定 create、refine 或 skip，经验证后同步回共享 SkillHub。

**Multi-Tier Co-Evolution.** 还有一类工作并行维护多个语义分工不同的演化库。Nemori [Ma25] 用 episode 与 anticipatory schema 的 prediction error 判定信息保留价值，蒸馏成 semantic knowledge，并把连续 episode 融合成 narrative episodic memory，两层库均执行 merge 与 conflict replacement。CLIN [Maj23] 从每次 trial 抽取因果式语言陈述，并由优质 memory 总结出跨 episode 的 meta-memory，每次 trial 后生成更新版本。CER [Liu25] 从每条 trajectory 同时抽取局部环境 dynamics 与较高层 decision-making skills，写入时显式参考已有内容以避免重复。

**Table 3.1.** Overview of Narrative Abstraction methods. 

<!-- 列定义：**Store Type** 记录经验库的维护模式（条目写入后是否被回改）；**Abstraction Source** 记录单次抽象所依据的轨迹数量；**Update Mechanism** 记录经验库中条目随时间变化的方式；**Artifact Form** 记录转化产物的具体表现形式；**Retrieval Mechanism** 记录从经验库中选取条目进入决策上下文的方式；**Domain** 记录工作的实验场景或目标领域。各列取值集合：Store Type ∈ {`Static`, `Dynamic`}；Abstraction Source ∈ {`Single-trajectory`, `Multi-trajectory`}；Update Mechanism ∈ {`append-only`, `operation-edit`, `survival-prune`, `skill-curate`, `multi-tier`}；Artifact Form ∈ {`reflection`, `summary`, `rule`, `insight`, `skill`, `multi-field record`, `procedural pair`}；Retrieval Mechanism ∈ {`always-on prepend`, `embedding similarity`, `keyed lookup`, `graph traversal`, `hierarchical drilldown`, `task-routed`}；Domain ∈ {`text`, `web`, `GUI`, `mobile`, `embodied`, `code`, `multi-agent`, `customer-service`}。 -->

| Work | Store Type | Abstraction Source | Update Mechanism | Artifact Form | Retrieval Mechanism | Domain |
|------|------------|--------------------|------------------|---------------|---------------------|--------|
|      |            |                    |                  |               |                     |        |

### 3.1.3 Discussion

Static 库实现简单、行为可预测、运行期开销低，但经验质量在写入时即被锁定，一条被误写的 reflection 会持续影响后续检索。Dynamic 库通过 merge、replacement、pruning 在长期使用中收敛，更能滤除单次抽象的偶然噪声，代价是引入冲突消解、staleness 判定、版本管理等额外机制，行为更难复现，淘汰策略本身可能误删仍然有用的条目。在 Static 内部，单轨迹抽象延迟低、数据需求小、冷启动表现好，适合任务分布窄、需要快速适应的场景；多轨迹归纳通过跨轨迹对照获得更强的泛化性与抗噪性，代价是冷启动能力弱、不同轨迹可能支持相互冲突的结论，且存在过度归纳的风险——把特定环境中的局部规律错误上升为通用规则。


## 3.2 Schematic Formalization: Narrative-to-Schematic Transformation

Schematic Formalization 从 raw Narrative trajectory 派生出具有显式结构、可被解析、执行或遍历的 Schematic artifact。本节按 Schematic artifact 在后续 Agent 决策中承担的主要语义功能分为三类：Programmatic Skill Construction、Procedural Workflow Induction 与 Structured Memory Graph Construction。

<!-- 判定一项工作属于 Schematic Formalization 需同时满足三个条件：输入是具体 Agent trajectory 或 interaction log（区别于 Parametric Externalization 中模型凭参数知识直接生成 artifact）；输出是具有可解析、可执行或可遍历结构的 Schematic artifact；下游复用机制性地利用这种结构（区别于 Narrative Abstraction 中仅让 LLM 自由阅读其文本表面）。第三个条件是 Schematic Formalization 与 Narrative Abstraction 的关键分界。 -->

### 3.2.1 Programmatic Skill Construction

Programmatic Skill Construction 从具体 Agent trajectory 中构建可调用的 code skill，使 Agent 在后续任务中将其作为高层动作单元直接调用，而非从低层动作重新规划。源经验通常是成功或经筛选的执行轨迹，产物可被 executor、runtime 或 browser automation framework 直接执行。

<!-- 本子类与 §3.2.2 的划分不取决于 artifact 内部是否含多步过程或前后置条件——这两个特征在两类中都普遍存在。判据是 artifact 在下游决策中的调度地位：Programmatic Skill 是一个整体可选、可启停的动作单元，Agent 在动作空间中将其作为单个高层动作选中并执行；Procedural Workflow 则是组织整类任务执行的流程结构，planner 在其阶段间导航、依据当前观测判断所处阶段。一个 skill 可以充当 workflow 中的一个节点。 -->

Voyager [Wan23c] 在 Minecraft 中通过 iterative prompting 反复生成、执行、修正 action program，只有经环境反馈、执行报错与 self-verification 验证通过的程序才以 Mineflayer JavaScript program 形式写入 skill library。ASI [Wan25d] 从 Agent 在线求解中被 evaluator 判为成功的 episode 出发，清洗掉报错步骤后由 induction module 诱导出 typed Python functions，并把原轨迹重写为调用新 skill 的版本再 re-execute——只有重写后仍能复现成功的 skill 才入库。SkillWeaver [Zhe25c] 让 web agent 在自动课程驱动下自主练习，由 reward model 判别成功行为，把 state-action 序列交由 LLM 生成带 typed parameters 的 Playwright API，再以 unit test、静态分析与环境反馈持续打磨。WebXSkill [Wan26d] 从更强 teacher model 在 WebArena 与 WebVoyager 上合成的 trajectory 中抽取动作子序列，抽象为带 typed parameters 与 step-level guidance 的 JSON skill，并按 URL pattern 组织为 skill graph。

### 3.2.2 Procedural Workflow Induction

Procedural Workflow Induction 从多步 Agent trajectory 中归纳可复用的任务流程结构，artifact 表现为 workflow、hierarchical procedure 或 task tree，编码阶段划分、步骤顺序、依赖关系与前后置状态。这类方法的基本假设是，许多复杂任务的可复用经验体现在执行过程的组织方式中——成功轨迹常含稳定的阶段模式，失败轨迹可能暴露步骤顺序或依赖检查的缺失。

AWM [Wan24] 从 web agent 的典型经验中抽取 recurring sub-routine，产物是由环境描述、推理与动作程序组成的 workflow trajectory。WorkflowGen [Wei26] 在节点与 workflow 两个粒度抽取经验，把结构相同的轨迹聚类合并为 generalized workflow template。HMT [Tan26] 与 MACLA [For25] 都通过切分轨迹后做分层抽象与显式条件标注：HMT 构造 intent/stage/action 三层树，stage 层带 pre/postcondition；MACLA 把轨迹分段为 atomic procedure（goal、precondition、action sequence、postcondition 四元组），并将过程序列抽象为带 continue/skip/repeat/abort 控制逻辑的 meta-procedure。MOBIMEM [Liu25i] 把移动端执行经验与用户纠错蒸馏为带参数槽位的 multi-level experience template，并通过异常驱动更新与基于回滚的过期检测持续修正旧经验。A2Flow [Zha25c] 从专家示范与 task-resolution 数据出发，把 case 级示范转成代码形式的 workflow 与初始 operator，再用 MCTS 在节点、边与 operator 构成的搜索空间中优化整体流程。FlowMind [Liu26] 采用 Execute-Summarize 两阶段：先让模型借工具完成任务并记录执行轨迹，再在独立摘要阶段抽取关键步骤、依赖与控制流构成 workflow graph。

### 3.2.3 Structured Memory Graph Construction

Structured Memory Graph Construction 把 Agent trajectory 中的实体与关系转化为可遍历、可更新的图结构记忆。Agent 的许多经验更适合组织为关系结构而非线性文本——环境对象间有空间关系，动作会改变状态，历史事件间有时间或因果联系，多智能体交互中存在角色、信息流与依赖。若这些关系仅以 raw log 或自然语言 note 存储，后续 Agent 难以做精确检索、局部更新与多跳推理。

AriGraph [Ano24] 与 A-MEM [Xu25b] 都把单步交互转为带语义结构的原子单元，并在新旧单元间建立关系：AriGraph 从每步文本观测抽取 semantic triplet 加入 semantic memory，环境状态变化时删除被推翻的旧关系；A-MEM 把每次交互转成带 keyword、tag 与 embedding 的 atomic note，通过 link generation 在新旧 note 间建立语义关系，新经验触发对旧 note 的重写。G-Memory [Zha25] 面向多智能体系统，把协作中的原子语句组织为 interaction graph，把整次查询实例化为 query node，再由 LLM 总结出 insight node，形成 interaction/query/insight 三层图。MobileGPT [Lee23] 通过 Explore-Select-Derive 流程把移动应用已完成任务转写为 task/sub-task/primitive action 层级，并把页面与子任务关系组织为 transition graph。Environment Maps [Fen26] 把浏览轨迹、DOM 与截图编译为 JSON 环境地图，含 context node、parameterized action node、workflow order 与 tacit knowledge。BrainMem [Ma26] 在具身场景维护 Trajectory KG（action-state transition）与 Spatial KG（room-object 空间关系）双图，episode 结束后由 Experience Agent 把成功轨迹提炼为通用模式、失败轨迹经 guided retry 压缩为符号化准则。

**Table 3.2.** Overview of Schematic Formalization methods. 

<!-- 列定义：**Artifact Category** 记录转化产物在 §3.2 中所属的语义功能类别；**Artifact Form** 记录转化产物的具体结构形态；**Downstream Mechanism** 记录下游 Agent 使用 artifact 的方式；**Retrieval Mechanism** 记录从 artifact 库中选取目标条目的方式；**Hierarchical Structure** 记录 artifact 是否带有多层级抽象结构；**Domain** 记录工作的实验场景或目标领域。各列取值集合：Artifact Category ∈ {`Programmatic Skill`, `Procedural Workflow`, `Structured Memory Graph`}；Artifact Form ∈ {`code skill`, `JSON skill`, `workflow trajectory`, `workflow template`, `hierarchical tree`, `transition graph`, `knowledge graph`, `environment map`}；Downstream Mechanism ∈ {`execute`, `parse-and-instantiate`, `traverse`}；Retrieval Mechanism ∈ {`embedding similarity`, `keyed lookup`, `URL pattern matching`, `graph traversal`, `task-routed`, `hierarchical drilldown`}；Hierarchical Structure ∈ {`flat`, `multi-level`}；Domain ∈ {`Minecraft`, `web`, `mobile`, `multi-agent`, `embodied`, `code`}。 -->

| Work | Artifact Category | Artifact Form | Downstream Mechanism | Retrieval Mechanism | Hierarchical Structure | Domain |
|------|-------------------|---------------|----------------------|---------------------|------------------------|--------|
|      |                   |               |                      |                     |                        |        |

### 3.2.4 Discussion

Programmatic Skill Construction 的优势在于可执行性、可验证性与可组合性：artifact 可通过运行结果判断有效性，也可在复杂任务中组合多个 skill。代价是对环境接口稳定性高度敏感，skill 库持续增长后需配套 selection、deduplication、versioning 与 stale detection。

Procedural Workflow Induction 的优势在于可解释性与可控性：workflow artifact 更短、更抽象，显式表达步骤依赖与执行顺序，便于定位任务的关键阶段。主要挑战是抽象粒度控制——过于具体则难泛化，过于抽象则丢失关键上下文——以及 workflow drift：环境状态变化后原 workflow 可能失效，需配套 consistency checking、precondition verification 与更新机制。

Structured Memory Graph 的优势是支持关系级别的记忆复用，图结构便于局部更新，适合 embodied agent、web agent 与多智能体系统的 long-horizon planning 与 state tracking。困难是图抽取容易产生错误实体与错误关系，图记忆随时间增长出现 memory bloat、过时信息与 retrieval noise，通常需配套 graph update、conflict resolution、pruning 与 confidence estimation。

三类 artifact 在功能上互补：与 Programmatic Skill 相比，workflow 的粒度更高——一个 skill 可以是一个 workflow 节点，一个 workflow 可调度多个 skill、工具或子任务；与 Procedural Workflow 相比，Structured Memory Graph 编码的是"环境中有什么、状态如何变化、历史经验间有什么关系"而非"任务应如何执行"，前者用节点与边表示实体、状态、事件、空间或交互关系，后者用节点与边表示步骤顺序、控制流或任务依赖。