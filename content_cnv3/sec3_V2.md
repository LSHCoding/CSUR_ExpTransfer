# 3. Tokenized-to-Tokenized Transformations

本章讨论经验在 Tokenized 载体层级内部的两种转化方式：Narrative Abstraction（Narrative → Narrative）与 Schematic Formalization（Narrative → Schematic）。两条路径共享同一源端——Agent 序贯决策中产生的具体轨迹（task execution log、reasoning trace、tool-use trajectory、web navigation history、GUI interaction trace 或 embodied execution record），区别在于目标载体的形式化程度与下游使用机制。Tokenized-to-Tokenized与 Parametric-to-Tokenized 外化有明确区分：前者的输入必须是具体 Agent trajectory、execution log 或 interaction record，模型在其中扮演 abstractor、formalizer 或 synthesizer；若 artifact 主要由模型根据任务描述或内化知识直接生成、无具体轨迹作为输入，则属于后者。

<!-- Narrative Abstraction 与 Schematic Formalization 的归类不采用论文自报术语。文献中 skill、experience、memory、procedure 等词存在严重的同名异物与同物异名：Voyager 的 skill 是可执行 JavaScript 代码，ExpeL 的 insight 是自然语言规则，A-MEM 的 memory 是图节点。归类基于两个可观测属性：artifact 的结构形态（自然语言文本 / 可解析可执行结构 / 关系图），以及下游消费机制（依赖 LLM 阅读理解，还是依赖 executor/parser/graph traversal）。论文原文术语仅在做具体介绍时保留。-->

## 3.1 Narrative Abstraction:Narrative-to-Narrative Transformation

Narrative Abstraction 将 Narrative Tokenized Agent Experience 转化为更高层的 Narrative artifact。源经验是 Agent 在具体上下文下观察、推理、行动并接收环境反馈所产生的自然语言或多模态序列化记录。Narrative Abstraction 不改变经验所处的载体层级——源端与目标端都在 Tokenized 层内的弱形式化区间——它在该层内完成抽象、压缩、重写或归纳。转化后的 artifact 包括 reflection、summary、lesson、rule、guideline、insight、causal statement 与 natural-language skill等等，后续 Agent 通过 language / multimodal understanding 直接阅读这些 artifact，经 retrieval-augmented prompting 或 prompt injection 进入决策上下文，而非交由 parser、executor、graph traversal 或训练过程处理。

<!-- Narrative Abstraction 内部组织依据经验库的维护方式而非 artifact 的表面名称或抽象所依赖的轨迹数量。Static Memory Store 与 Dynamic Memory Store 的判别点是已有条目是否会被回改——只增不改的库属 Static，涉及改写、合并、淘汰、替换或版本更新的库属 Dynamic。这一划分较按轨迹粒度的分类更能捕捉方法在长期可维护性上的结构性差异。 -->

### 3.1.1 Static Memory Store

Static Memory Store 类方法把经验抽象的产物当作只读资产积累。经验库的具体形态不一：有的是任务内临时缓存，任务结束即弃；有的是构建后不再回改的持久库；有的在抽象前先对原始轨迹做过滤。共性是条目一旦写入便不再被编辑或合并，经验质量由单次抽象的好坏决定，系统在长期使用中没有自我纠错环节。实现简单、行为可预测，代价是错误一旦进入库便会持续影响后续决策。

**Single-Trajectory Experience Abstraction.** 单轨迹经验抽象以一条 Agent trajectory、episode 或局部 execution log 为输入，把一次具体执行压缩为更高层的自然语言 artifact。触发时机通常是任务结束、失败发生或一次 trial 完成，手段包括 reflection、summarization、critique、failure explanation。单条轨迹本身已携带可复用信号：失败轨迹可能暴露错误假设、无效动作或遗漏约束，成功轨迹可能包含有效的分解策略或环境交互模式。反应快、成本低、不依赖历史数据积累，适合 trial-and-error、online adaptation 与任务分布较窄的场景；局限在于抽象依据单条轨迹，容易把偶然因素误写为通用经验，且与原任务上下文绑定较强，跨任务迁移能力有限。

Reflexion [Shi23b] 是这一范式的早期代表。Agent 在每次 trial 结束后，依据失败轨迹与环境反馈生成简短 reflection，将错误归因与改进建议写成 verbal memory 拼接进下一轮 prompt。Reflection-Based Memory for Web Navigation Agents [Aza25] 将单条网页浏览轨迹总结为 Web-Reflection，内容覆盖有效步骤、站点功能局限、捷径与失败回溯点，以任务 embedding 为键存入 key-value 知识库，测试时检索 top-k 注入 prompt。MemOrb [Hua25] 在客服场景下把每轮对话及其工具调用轨迹事后压缩为一个 Orb，以 observation、emotion、outcome、context 与策略性反思组成的多字段结构存入可检索层，后续对话按需取回，其 rewrite 环节针对查询而非已有 Orb 条目。Procedural Knowledge at Scale Improves Reasoning [Wu26] 从 teacher model 合成的大规模 reasoning traces 中解构出 subquestion-subroutine 对，构成静态 procedural datastore，推理时模型先 verbalize 当前子问题再检索对应 subroutine 作为 hint。

REFLECT [Liu23] 处理机器人单次执行的多模态观测流，先把 RGB-D 视频、音频与状态记录转为 scene graph、事件级 caption 与 subgoal-level summary，再做分层摘要，并在子目标验证失败时生成 failure explanation 驱动 correction planning。该工作不维护跨 episode 的持久库，整个流程是一次性的单轨迹总结。WebCoach [Liu25e] 把每个已完成的 web episode 压缩为 3–5 句 summary，保留 success status 与 fail mode 等字段后存入 External Memory Store，只持久化已完成 episode、丢弃半成品过程。

在代码域，SWE-Exp [Che25d] 从单次 repair trajectory 中分别提炼 comprehension experience 与 modification experience，形成带 perspective、modification、issue type 的 experience bank 条目。MemGovern [Wan26ap] 从 GitHub issue、PR、patch 的闭环修复记录中提纯 Experience Card，经 checklist 式 refine loop 保证字段质量，产物分 Index 层与 Resolution 层。其经验源是 governed human experience 而非 Agent 自身试错——与本节多数工作不同，但纳入标准对经验来源不设限，人类示范同样合法。

<!-- Meta-Policy Reflexion [Wu25] 把失败 episode 的 retrospective reflection 写成带权重的 predicate-like 规则，测试阶段 memory 冻结，Agent 检索规则注入 prompt 并做 admissibility check。规则在测试期不再变动，归 Static；其规则形式更形式化，接近轻量 rule set，但复用仍靠阅读而非执行，归 Narrative Abstraction。 -->


**Multi-Trajectory Experience Induction.** 多轨迹经验归纳以多条 trajectories、demonstrations 或 failure cases 为输入，通过比较、聚类或合并抽取更稳定、更可迁移的 Narrative artifact。可迁移经验通常来自多次执行之间反复出现的稳定结构——对成功与失败轨迹做对照可以识别哪些行为与任务完成更相关、哪些错误跨上下文反复出现。相比单轨迹抽象，这类方法更可能滤掉单次轨迹的偶然噪声，代价是冷启动能力弱，且存在过度归纳的风险——把特定环境中的局部规律错误上升为通用规则。

AutoGuide [Fu24] 从同一任务的优劣轨迹对中定位首次决策分叉点，围绕分叉动作抽出与上下文绑定的 guideline，写成 when-context then-action 形式并按 context 建成字典。单个 guideline 依赖一对成功与失败轨迹的对照，是 pairwise contrastive extraction。Coarse-to-Fine Grounded Memory [Yan25] 先从环境基础信息与离线 trial-and-error 轨迹得到 coarse focus points，再比较成功与失败轨迹提炼 hybrid-grained tips，其长期可复用部分主要是 tips dictionary。M2 [Yan26b] 把单轨迹压缩与多轨迹归纳放在同一系统的两层记忆里——internal memory 在每步把 observation、thought、action 压成简短状态摘要，external insight bank 从历史成功日志中提炼 topic-tagged insights。


### 3.1.2 Dynamic Memory Store

Dynamic Memory Store 类方法把经验库当作随交互持续演化的对象。系统不仅写入新经验，还对已有条目做改写、合并、淘汰、替换或版本更新，使经验库在长期使用中具备自我纠错与去冗的能力。核心问题不再只是"如何从一次经验生成一个 artifact"，而是经验如何进入长期记忆、已有记忆如何被更新、重复或过时条目如何被合并或删除。

**规则与 insight 库的显式编辑。** 一类工作维护自然语言规则或 insight 库，并把编辑与投票写成显式 memory operation。ExpeL [Zha23c] 从成功轨迹池与失败-成功对中抽取可迁移 insight，对已有条目执行 ADD、EDIT、UPVOTE、DOWNVOTE，每条 insight 带重要度评分。H2R [Ye25b] 把 hindsight reflection 拆成高层 planning memory 与低层 execution memory，支持 add、modify、upvote、downvote。AutoManual [Che24] 让 Planner 在环境中交互，Builder 按 direct success、indirect success、failure 三类结果差异化地抽取规则，Consolidator 合并冗余、删除过时项，Formulator 整理成 Markdown manual。Agentic Context Engineering [Zha25f] 由 Reflector 从 reasoning trajectory 抽出 insight、failure mode 与 strategy bullet，Curator 将它们作为 delta 合并进 Context Playbook，配套语义去重与低效条目裁剪。

**替换、淘汰与 survival 评分。** 另一类工作以替换、淘汰或 survival 评分驱动经验库收敛。Darwinian Memory [Mi26b] 把 GUI 经验写成以 precondition 与 goal 为索引的 memory unit，通过 evolutionary replacement、survival-based pruning 与 reputation-style inhibition 调节记忆库。R2D2 [Hua25e] 从历史 web 轨迹中截断纠错并生成可回放的修正性反思，通过 replay buffer 与 reflective update 持续替换较弱旧经验。Remember Me, Refine Me [Cao25] 从单条轨迹中抽取 keypoint-level procedural memory，持续跟踪检索与成功效用，做验证、去重和低效记忆删除——其动态性主要来自删除与筛选而非逐字重写。Mistake Notebook Learning [Su25] 以一批失败样本为更新单元，先按 subject 聚类再生成 mistake note，每轮经 post-update evaluation 整体验证后才接受，更新为批量而非在线逐条。

**技能库的持续演化。** 围绕 skill 的工作把单次经验不断吸收进持续演化的技能库。Trace2Skill [Ni26] 由并行 analyst 对各条轨迹提出局部 patch，经分层 merge 与 conflict-free consolidation 合成可迁移 skill，产物为 SKILL.md 技能文档，已有文档可在 deepening mode 下被进一步改写。AutoSkill [Yan26] 从用户交互信号中抽取 skill candidate，经 judge 决定 add、merge 或 discard，对保留技能做版本化演化。SkillClaw [Ma26b] 汇总多用户、多 agent 的真实使用 session，由 Agentic Evolver 判定 create、refine 或 skip，经验证后同步回共享 SkillHub。

**多层级经验库的并行演化。** 还有一类工作并行维护多个语义分工不同的演化库。What Deserves Memory [Ma25] 用 episode 与 anticipatory schema 的 prediction error 判定信息保留价值，蒸馏成 semantic knowledge，并把连续 episode 融合成 narrative episodic memory，两层库均执行 merge 与 conflict replacement。CLIN [Maj23] 从每次 trial 抽取因果式语言陈述，并由优质 memory 总结出跨 episode 的 meta-memory，每次 trial 后生成更新版本。Contextual Experience Replay [Liu25] 从每条 trajectory 同时抽取局部环境 dynamics 与较高层 decision-making skills，写入时显式参考已有内容以避免重复。Dynamic Cheatsheet [Suz25] 的更新对象是整份文档而非单个条目——Curator 对解题轨迹做 usefulness 与 generalizability 评估，把可迁移内容蒸馏进 cheatsheet，并对条目执行改写、删除、合并与压缩以控制长度。

### 3.1.3 Discussion

Static 库实现简单、行为可预测、运行期开销低，但经验质量在写入时即被锁定，一条被误写的 reflection 会持续影响后续检索。Dynamic 库通过 merge、replacement、pruning 在长期使用中收敛，更能滤除单次抽象的偶然噪声，代价是引入冲突消解、staleness 判定、版本管理等额外机制，行为更难复现，淘汰策略本身可能误删仍然有用的条目。在 Static 内部，单轨迹抽象延迟低、数据需求小、冷启动表现好，适合任务分布窄、需要快速适应的场景；多轨迹归纳通过跨轨迹对照获得更强的泛化性与抗噪性，代价是冷启动能力弱且不同轨迹可能支持相互冲突的结论。


## 3.2 Schematic Formalization: Narrative-to-Schematic Transformation

Schematic Formalization 将 Narrative Tokenized Agent Experience 转化为具有显式结构约束的 Schematic Tokenized artifact。源经验是 Agent 序贯决策中产生的具体轨迹。转化的核心动作是把弱形式化的 Narrative experience 形式化为可被解析、执行、遍历、实例化或调度的结构化 artifact。典型目标载体包括 executable code skill、parameterized action program、workflow、hierarchical procedure、task tree、knowledge graph、state-transition graph 与 structured memory graph。

<!-- 判定一项工作属于 Schematic Formalization 需同时满足三个条件：输入是具体 Agent trajectory 或 interaction log（区别于 Parametric Externalization 中模型凭参数知识直接生成 artifact）；输出是具有可解析、可执行或可遍历结构的 Schematic artifact；下游复用机制性地利用这种结构（区别于 Narrative Abstraction 中仅让 LLM 自由阅读其文本表面）。第三个条件是 Schematic Formalization 与 Narrative Abstraction 的关键分界。 -->

本文按转化后 Schematic artifact 在后续 Agent 决策中承担的主要语义功能分为三类：Programmatic Skill Construction（经验转化为可调用的动作单元）、Procedural Workflow Induction（经验转化为多步任务流程结构）与 Structured Memory Graph Construction（经验转化为环境、状态或交互关系的图结构）。对图状 artifact，按主要语义功能而非表面拓扑分类：若图主要编码任务执行顺序、步骤依赖、控制流或阶段结构，归入 Procedural Workflow Induction；若图主要编码实体、状态、空间关系、环境知识或交互历史，归入 Structured Memory Graph Construction。

### 3.2.1 Programmatic Skill Construction

Programmatic Skill Construction 从具体 Agent trajectory 中构建可调用、可执行或可参数化的技能单元，使 Agent 在后续任务中直接调用该单元，而非从低层动作重新规划。源经验通常是成功或经筛选的执行轨迹，转化后的 artifact 表现为 code skill、parameterized action program 或 callable skill interface。这类 artifact 的功能是"动作压缩"或"动作空间扩展"：原本需多步低层操作完成的行为被抽象为一个高层可调用单元，通常可被 executor、runtime 或 browser automation framework 直接执行。

<!-- 本子类与 §3.2.2 的划分不取决于 artifact 内部是否含多步过程或前后置条件——这两个特征在两类中都普遍存在。判据是 artifact 在下游决策中的调度地位：Programmatic Skill 是一个整体可选、可启停的动作单元，Agent 在动作空间中将其作为单个高层动作选中并执行；Procedural Workflow 则是组织整类任务执行的流程结构，planner 在其阶段间导航、依据当前观测判断所处阶段。一个 skill 可以充当 workflow 中的一个节点。 -->

Voyager [Wan23c] 在 Minecraft 中通过 iterative prompting 反复生成、执行、修正 action program，只有经环境反馈、执行报错与 self-verification 验证通过的程序才写入 skill library。库以 skill description 的 embedding 为索引、值为可执行的 Mineflayer JavaScript 程序，新任务按 task plan 与环境反馈检索 top-k skills 放入 prompt 供组合调用。ASI [Wan25d] 从 Agent 在线求解中被 evaluator 判为成功的 episode 出发，清洗掉报错步骤后由 induction module 诱导出 typed Python functions，并把原轨迹重写为调用新 skill 的版本再 re-execute——只有重写后仍能复现成功的 skill 才入库。SkillWeaver [Zhe25c] 让 web agent 在自动课程驱动下自主 practice，用 reward model 识别成功行为，把 state-action 序列提示 LLM 生成带 typed parameters 的 Playwright API，再以 unit test、静态分析与环境反馈持续 honing。WebXSkill [Wan26d] 从更强 teacher model 在 WebArena 与 WebVoyager 上合成的 trajectory 中抽取 action subsequence，抽象为带 typed parameters 与 step-level guidance 的 JSON skill，并按 URL pattern 组织为 skill graph。

Programmatic Skill Construction 的优势在于可执行性、可验证性与可组合性：artifact 可通过运行结果判断有效性，也可在复杂任务中组合多个 skill。代价是对环境接口稳定性高度敏感，skill 库持续增长后需配套 selection、deduplication、versioning 与 stale detection。

### 3.2.2 Procedural Workflow Induction

Procedural Workflow Induction 从多步 Agent trajectory 中归纳可复用的任务流程结构：workflow、DAG、hierarchical procedure、task tree 或 stage-action hierarchy。这类方法抽象的不是单个可调用动作，而是完成一类任务所需的阶段划分、步骤顺序、依赖关系、控制流、条件分支与前后置状态。许多复杂任务的可复用经验体现在执行过程的组织方式中——成功轨迹常含稳定的阶段模式（先收集信息、再筛选候选、再验证约束、最后提交），失败轨迹可能暴露步骤顺序或依赖检查的缺失。与 Programmatic Skill 相比，workflow 的粒度更高：一个 skill 可以是一个 workflow 节点，一个 workflow 可调度多个 skill、工具或子任务。

Agent Workflow Memory [Wan24] 从 web agent 的 canonical experience 中抽取 recurring sub-routine，产物是由 environment description、reasoning 与 action program 组成的 workflow trajectory。支持离线（人类标注或模型合成经验）与在线（仅对 evaluator 判正的轨迹做归纳）两种模式。WorkflowGen [Wei26] 在 node 与 workflow 两个粒度抽取经验，把结构相同的轨迹聚类合并为 generalized workflow template，节点带 fixed/generatable 标记，推理时按相似度做三级路由。Hierarchical Memory Tree [Tan26] 把成功 web 轨迹切成 subgoal segment，构造 intent/stage/action 三层树，stage 层带显式 pre/postcondition，叶层以 semantic element description 替代具体 DOM 标识。MACLA [For25] 把轨迹分段为 atomic procedure（goal、precondition、action sequence、postcondition 四元组），反复带来成功的 procedure 序列进一步抽象为带 continue/skip/repeat/abort 控制逻辑的 meta-procedure，并通过 contrastive refinement 与 reliability-based pruning 持续更新。MOBIMEM [Liu25i] 把 mobile 执行经验与用户纠错蒸馏为带参数槽位的 multi-level experience template（高层编码任务级 control flow，低层保存具体 UI step），并通过 exception-driven updating 与 rollback-based stale detection 持续修正旧经验。A2Flow [Zha25c] 从 expert demonstration 与 task-resolution 数据出发，把 case 级示范转成 code-based workflow 与初始 operator，经 operator clustering 得到 task-aware abstract operator，再用 MCTS 在节点、边与 operator 构成的搜索空间中优化整体流程，产物是可直接执行的 directed workflow graph。FlowMind [Liu26] 采用 Execute-Summarize 两阶段：先让模型借工具完成任务并记录 execution trace，再在独立 summarize 阶段用 graph-building tool 抽取 essential step、dependency 与 control flow，构成带 sequencing、branching、iteration 的 workflow graph。

Procedural Workflow Induction 的优势在于可解释性与可控性：workflow artifact 更短、更抽象，显式表达步骤依赖与执行顺序，便于定位任务的关键阶段。主要挑战是抽象粒度控制——过于具体则难泛化，过于抽象则丢失关键上下文——以及 workflow drift：环境状态变化后原 workflow 可能失效，需配套 consistency checking、precondition verification 与更新机制。

### 3.2.3 Structured Memory Graph Construction

Structured Memory Graph Construction 把 Agent trajectory 中的实体、关系、状态变化、空间结构、事件依赖或交互历史转化为可检索、可遍历、可更新的图结构记忆。这类方法的目标不是生成可执行动作，也不是归纳任务流程，而是构建 Agent 对环境、任务世界、历史经验或多智能体交互关系的结构化表示。Agent 的许多经验不适合表达为线性文本或固定流程，而更适合组织为关系结构：环境对象间有空间关系，动作会改变状态，历史事件间有时间或因果联系，多智能体交互中存在角色、信息流与依赖。若这些关系仅以 raw log 或自然语言 note 存储，后续 Agent 难以做精确检索、局部更新与多跳推理。

AriGraph [Ano24] 从每步 textual observation 抽取 semantic triplet 加入 semantic memory，同时把完整 observation 作为 episodic vertex 与当步 triplet 相连，形成同时编码世界知识与情节历史的 knowledge graph world model，环境状态变化时删除被推翻的旧关系。G-Memory [Zha25] 面向多智能体系统，把协作中的 atomic utterance 组织为 interaction graph，把整次 query 实例化为 query node，再由 LLM 总结出 insight node，形成 interaction/query/insight 三层图，支持按 query 做上下双向 traversal。A-MEM [Xu25b] 把每次交互转成带 keyword、tag、contextual description 与 embedding 的 atomic note，通过 link generation 在新旧 note 间建立语义关系，新经验触发对旧 note 的重写。MobileGPT [Lee23] 通过 Explore-Select-Derive 流程把 mobile app 已完成任务转写为 task/sub-task/primitive action 层级，并把页面与子任务关系组织为 transition graph（节点为功能等价的 app page，边为可复用 sub-task）。Environment Maps [Fen26] 把 browser trace、DOM 与 screenshot 编译为 JSON 环境地图，含 context node、parameterized action node、workflow order 与 tacit knowledge。BrainMem [Ma26] 在 embodied 场景维护 Trajectory KG（action-state transition）与 Spatial KG（room-object 空间关系）双图，episode 结束后由 Experience Agent 把成功轨迹提炼为 generalizable pattern、失败轨迹经 guided retry 压缩为 symbolic guideline。

Structured Memory Graph 与 Procedural Workflow 的区别在图的语义功能：workflow graph 回答"任务应如何执行"，节点与边表示步骤顺序、控制流或任务依赖；memory graph 回答"环境中有什么、状态如何变化、历史经验间有什么关系"，节点与边表示实体、状态、事件、空间或交互关系。这类方法的优势是支持关系级别的记忆复用，图结构便于局部更新，适合 embodied agent、web agent 与多智能体系统的 long-horizon planning 与 state tracking。困难是图抽取容易产生错误实体与错误关系，图记忆随时间增长出现 memory bloat、过时信息与 retrieval noise，通常需配套 graph update、conflict resolution、pruning 与 confidence estimation。

