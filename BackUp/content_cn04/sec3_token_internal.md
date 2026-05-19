# §3 Tokenized 内部转化（Tokenized-to-Tokenized Transformations, P1 + P2）

本章讨论经验在 Tokenized 载体层级内部的两种转化方式：P1（Narrative → Narrative）与 P2（Narrative → Schematic）。两条路径共享同一源端——Agent 序贯决策中产生的具体轨迹（task execution log、reasoning trace、tool-use trajectory、web navigation history、GUI interaction trace 或 embodied execution record），区别在于目标载体的形式化程度与下游消费机制。

Tokenized-to-Tokenized 转化与 Parametric-to-Tokenized 外化有明确区分：前者的输入必须是具体 Agent trajectory、execution log 或 interaction record，模型在其中扮演 abstractor、formalizer 或 synthesizer；若 artifact 主要由模型根据任务描述或内化知识直接生成，而无具体轨迹作为输入，则属于 P7。

## §3.1 Narrative-to-Narrative Transformation（P1）

P1 将 Narrative Tokenized Agent Experience 转化为更高层的 Narrative artifact。源经验来自 Agent 在特定上下文下如何观察、推理、行动并接收环境反馈的自然语言或多模态序列化记录。P1 的目标不是在载体层级之间移动，而是在 Narrative Tokenized 层内部完成抽象、压缩、重写或归纳。转化后的 artifact 仍为弱形式化的 Tokenized 表达——reflection、summary、lesson、failure explanation、heuristic、guideline、insight、mistake pattern 或 natural-language skill——通过 retrieval-augmented prompting 或 direct prompt injection 被后续 Agent 消费，而非由 parser、executor、graph traversal module 或训练过程处理。

P1 与 P2 的区分依据是下游消费机制而非 artifact 表面形式。即使 artifact 呈现为编号列表、规则集合或 skill description，只要其复用依赖 language understanding 而非专门的执行器、解析器或结构化遍历机制，仍属 P1。若经验被转化为 code、workflow、decision tree、knowledge graph、action schema 或可执行 procedure，则归入 P2。

P1 与 P7 的区分同样明确：P1 的输入必须是具体 Agent trajectory 或 interaction log，而非模型仅凭参数知识生成的 guideline 或 instruction。

不同论文以 reflection、memory、skill、guideline、insight 等术语指代机制上并不相同的对象。本文不按 artifact 的表面名称组织，而按经验抽象所依赖的轨迹粒度划分：**Per-Trajectory Experience Abstraction**（从单条轨迹中抽象局部经验）、**Cross-Trajectory Experience Induction**（从多条轨迹中归纳共性规律）和 **Dual-Granularity Experience Consolidation**（同时包含单轨迹写入与跨轨迹整合，使 Narrative memory 随交互持续演化）。

### §3.1.1 Per-Trajectory Experience Abstraction

Per-Trajectory Experience Abstraction 以单条 Agent trajectory、episode、trial 或局部 execution log 为主要输入，将一次具体执行经验抽象为更高层的自然语言 artifact。这类方法在任务结束、失败发生、环境反馈返回或一次 trial 完成后触发，通过 reflection、summarization、critique、failure explanation 或 hindsight rewriting 将原始轨迹压缩为可复用的文本经验。

Artifact 形式包括 episode-level reflection、trajectory summary、failure diagnosis、lesson learned、hindsight note、local tip 或 correction suggestion。它们的共同点在于来源粒度：artifact 主要由单条轨迹内部的信息抽象而来，关注从一次具体经历中提炼对下一次决策有帮助的局部经验。

单次执行轨迹本身包含可复用的经验信号：失败轨迹可能揭示错误假设、无效动作、遗漏约束或不恰当的工具调用；成功轨迹可能包含有效的分解策略、搜索路径或环境交互模式。用语言模型对这些轨迹进行事后解释和压缩，Agent 可以把原本冗长、低层、任务绑定的历史记录转化为更短、更抽象、更易注入上下文的经验描述。这类方法的主要优势是反应快、成本低、不依赖大量历史数据，适合 trial-and-error setting、online adaptation 和任务分布较窄的场景。

局限同样明显。抽象主要依赖单条轨迹，容易受偶然因素和错误归因影响——一次失败不代表其中所有动作都错，一次成功也不保证所有策略都具有泛化性。若 reflection 或 failure explanation 将偶然现象误写作通用经验，后续 Agent 可能被误导。单轨迹 artifact 与原始任务上下文绑定较强，跨任务迁移能力有限，更适合局部 adaptation 而非稳定经验规律的来源。

**代表性工作。** Reflexion [Shi23b] 是这一范式的早期代表：Agent 在每次 trial 结束后，根据失败轨迹与环境反馈生成简短 reflection，将错误归因、行为教训与改进建议写成 verbal memory，并在下一轮尝试中直接注入 prompt。消融实验表明，事后生成的 reflection 比直接回放原始 episodic trajectory 更有效。类似地，Reflection-Based Memory for Web Navigation Agents [Aza25] 将单条网页交互轨迹总结为 Web-Reflection，内容覆盖有效步骤、站点功能局限、捷径、失败回溯点与改进建议，再通过语义检索将相关 reflection 回注到新任务中。

在具身与交互环境中，REFLECT [Liu23] 对单次机器人执行中的多模态观测流做分层摘要，在子目标验证失败后生成自然语言 failure explanation，并据此驱动后续 correction planning。MemOrb [Hua25] 将单轮客服对话及其工具调用轨迹事后总结为策略性 verbal-reinforcement memory，再以可检索的 Orb 单元形式存储。

另一些方法放宽了"抽象"的形式，不再局限于显式 critique 或 reflection，但仍保留单轨迹事后转写的核心机制。Hindsight Trajectory Rewriting [Hu25] 在 episode 结束后对失败轨迹进行 hindsight rewriting，将其改写为针对其他潜在目标的合成成功轨迹或更紧凑的 workflow 描述，从而把失败探索转化为可复用的正向 in-context experience。Self-Generated In-Context Examples [Sar25] 从 Agent 自己完成任务的单条成功轨迹中自动构造 self-generated demonstrations，并在后续规划与执行时动态检索这些 examples。在代码智能体中，MemGovern [Wan26ap] 从单个 issue 修复过程中的 governed human experience 出发，将原始修复交互提纯为 problem summary、diagnostic signals、root cause、fix strategy 与 verification 等字段化 textual memory。

### §3.1.2 Cross-Trajectory Experience Induction

Cross-Trajectory Experience Induction 以多条 trajectories、demonstrations、rollouts、failure cases 或 historical interactions 为输入，通过比较、聚类、筛选、合并或归纳，抽取更稳定、更通用、更可迁移的 Narrative artifact。与单轨迹方法不同，这类方法不满足于解释某一次执行为何成功或失败，而是从多次经验中发现反复出现的模式。

Artifact 形式包括 rule、guideline、heuristic、insight、do-and-don't list、mistake pattern、natural-language skill 或 procedural tip。可迁移经验通常来自多次执行之间的稳定结构——通过对比成功与失败轨迹，方法可以识别哪些行为与任务完成更相关，哪些错误在不同上下文中反复出现，哪些约束或策略具有更强的跨任务适用性。

这类方法的主要优势是泛化能力更强：artifact 来自多条经验的归纳，更可能滤掉单次轨迹中的偶然噪声，保留在多个任务或多个 episode 中稳定出现的有效模式。局限在于冷启动能力弱于单轨迹抽象，存在过度抽象风险（模型可能把特定环境中的局部规律错误上升为通用规则），且不同轨迹可能支持相互冲突的经验结论，需要额外的冲突检测、适用条件建模或经验筛选机制。

**基于成功失败对比的跨轨迹归纳。** ExpeL [Zha23c] 联合利用失败-成功轨迹对与跨任务成功案例集合，通过 insight extraction 生成高层 natural-language insights，并借助 add、edit、upvote、downvote 等操作持续维护经验库，使经验积累从离散 reflection 走向可演化的 rule bank。AutoGuide [Fu24] 在同一任务的优劣轨迹中定位首次偏离步骤，通过 context identification 与 guideline extraction 生成与局部 context 绑定的 guideline。Mistake Notebook Learning [Su25] 先对一批失败轨迹做 subject clustering，再在 cluster level 抽取共性的错误根源与 anti-pattern，并仅在更新确实改善性能时才纳入记忆。SWE-Exp [Che25d] 同时从成功修复轨迹与失败反思中提取 comprehension experience 和 modification experience，在新 issue 上经过 retrieval、reranking 与 rewriting 后复用。AutoManual [Che24] 显式区分 direct success、indirect success 与 failure 三类交互结果，并据此触发不同的 rule generation 与 update 逻辑。

**基于多轨迹聚合的跨轨迹归纳。** Trace2Skill [Ni26] 从并行收集的大量成功与失败轨迹中分别生成局部 skill patches，再通过 hierarchical patch merge 保留跨轨迹反复出现的 prevalent patterns，最终形成 skill directory。Skill Set Optimization [Not24] 从多条历史轨迹中提取高奖励且 embedding space 中相似的子轨迹对，再由 LLM 概括为 subgoal 与 instructions，构造可检索的 transferable skill set。Dynamic Cheatsheet [Suz25] 将测试时积累的多次解题轨迹持续交由 Memory Curator 处理，从中提炼 strategy、solution sketch、code snippet 与 insight，并对已有条目执行 revision、replacement、merging 与 compression。Procedural Knowledge at Scale Improves Reasoning [Wu26] 从大规模 reasoning traces 中解构出 subquestion-subroutine 对，构建可检索的 procedural knowledge store。

总体而言，这两条思路共享同一经验转化逻辑：将原始 trajectory 从一次性历史记录转化为跨任务可复用的 Narrative artifact。前者更依赖 success-failure contrast 来提炼 rule 与 guideline，后者更强调在 trajectory collection 上进行 aggregation、merging 与 compression。二者共同提升了经验复用的泛化性，并在一定程度上滤除了单次交互中的偶然噪声，但同时也面临过度归纳、适用范围不清与经验冲突等问题。

### §3.1.3 Dual-Granularity Experience Consolidation

Dual-Granularity Experience Consolidation 同时包含单轨迹层面的经验写入与多轨迹层面的经验整合。系统通常先从每条新 trajectory 中抽取局部 reflection、summary、lesson 或 episode memory，再随着交互经验积累，对这些局部 artifact 进行合并、去重、重写、压缩、筛选、层级化、淘汰或版本更新，形成持续演化的 Narrative memory store。

这类方法的核心问题不只是"如何从一次经验中生成一个 artifact"，也不只是"如何从一批轨迹中归纳一组规则"，而是如何连接这两个过程：新经验如何进入长期记忆，已有记忆如何被更新，重复或低价值经验如何被合并或删除，过时经验如何被淘汰，局部 episode memory 如何逐渐上升为更稳定的 cross-episode insight。

**代表性工作。** CLIN [Maj23] 从单次试错中提炼因果式经验表述（如"X is necessary for Y"），并进一步形成跨 episode 的 meta-memory。R2D2 [Hua25e] 从失败轨迹中生成可回放的修正性反思，并通过全局 replay buffer 与 reflective update 持续替换较弱的旧经验。Darwinian Memory [Mi26b] 将长轨迹切成以子目标为单位的 plan-trajectory memory entry，用基于效用、可靠性与时间衰减的 evolutionary replacement 机制管理长期记忆。

Learning on the Job [Yan25d] 先将局部成功子任务写成 SOP 形式的 procedural memory，任务完成后再做全局 deduplication、generalization 与 strategic memory 提炼。Remember Me, Refine Me [Cao25] 从单条轨迹中抽取 keypoint-level procedural memory，持续跟踪检索次数与成功效用，做验证、去重和低效记忆删除。Contextual Experience Replay [Liu25] 从每条 trajectory 同时抽取局部环境 dynamics 与较高层的 decision-making skills，且新经验写入时显式参考已有 buffer 以避免重复。What Deserves Memory [Ma25] 将 episodic integration 与 semantic consolidation 区分处理，通过 merge、conflict resolution 与替换机制管理经验演化。Agentic Context Engineering [Zha25f] 将单次交互中产生的局部增量经验持续写入可演化的 context playbook。

在长时程 web、GUI 与开放环境 Agent 中，GUI-explorer [Xie25] 从局部状态转移中抽取细粒度操作知识，并将其持续并入全局知识库。WebCoach [Liu25e] 将完整 session 压缩为 cross-session memory record。H2R [Ye25b] 将高层 planning insight 与低层 execution insight 统一纳入层级化 hindsight reflection 框架。Coarse-to-Fine Grounded Memory [Yan25] 先把单任务探索得到的 trajectory 存入 experience pool，再按任务聚合成功与失败样本，抽取 consolidated tips dictionary。Memp [Fan25] 同时保留 fine-grained trajectory 与 high-level script 两种粒度的 procedural memory，通过 validation 式 consolidation 和 failure-driven adjustment 来修订、压缩和纠错。

更近期的 AutoSkill [Yan26]、SkillClaw [Ma26b] 与 SkillX [Wan26] 延续了相同方向：它们不再将每次交互仅仅视为一次性示例，而是将局部经验不断吸收到持续演化的长期知识库中，并通过版本更新、合并与筛选，使经验逐步由 episode-local observation 上升为更稳定的 cross-episode know-how。这些方法更偏 programmatic skill consolidation，承载物更接近显式 skill artifact 而非典型 Narrative memory，可作为边界案例。

**路径总结。** P1 三类方法构成了一条从局部到全局、从静态到动态的经验抽象谱系：Per-Trajectory Abstraction 提供了最低延迟、最低数据需求的局部适应能力；Cross-Trajectory Induction 提供了更强的泛化性和稳定性；Dual-Granularity Consolidation 则代表了 P1 中更系统化的发展方向，将单次经验抽象、多次经验整合和长期记忆管理连接起来，使 Agent 能够从孤立的 execution logs 中逐步构建可持续复用的 Narrative experience store。

## §3.2 Narrative-to-Schematic Transformation（P2）

P2 将 Narrative Tokenized Agent Experience 转化为具有显式结构约束的 Schematic Tokenized artifact。源经验来自 Agent 序贯决策中产生的具体轨迹。P2 的核心是将原始 Narrative experience 形式化为可被解析、执行、遍历、实例化或调度的结构化 artifact。典型目标载体包括 executable code skill、API routine、parameterized action schema、workflow、DAG、hierarchical procedure、task tree、knowledge graph、episodic graph、environment map、state-transition graph 或 structured memory graph。

P2 的判定需同时满足三个条件：输入必须是具体 Agent trajectory 或 interaction log；输出必须是具有可解析、可执行或可遍历结构的 Schematic artifact；下游复用必须利用这种结构，而非仅让 LLM 自由阅读文本。P2 与 P1 的关键区别在于结构是否在下游复用中发挥机制性作用。

本文按转化后 Schematic artifact 在后续 Agent 决策中的主要语义功能分为三类：**Programmatic Skill Construction**（将经验转化为可调用的动作单元）、**Procedural Workflow Induction**（将经验转化为多步任务流程结构）和 **Structured Memory Graph Construction**（将经验转化为环境、状态或交互关系的图结构表示）。一些方法产生的 artifact 介于 Narrative 与 Schematic 之间，或混合多种结构形式，作为 boundary cases 在 §3.2.4 单独讨论。

对于图状 artifact，按主要语义功能而非表面拓扑形态分类：若图主要编码任务执行顺序、步骤依赖、控制流或阶段结构，归入 Procedural Workflow Induction；若图主要编码实体、状态、空间关系、环境知识、情节记忆或交互历史，归入 Structured Memory Graph Construction。

### §3.2.1 Programmatic Skill Construction

Programmatic Skill Construction 从具体 Agent trajectories 中构建可调用、可执行或可参数化的技能单元，使 Agent 在后续任务中直接调用这些技能，而非从低层动作开始重新规划。源经验通常是成功或经过筛选的执行轨迹，转化后的 artifact 表现为 code skill、Python function、parameterized action program 或 callable skill interface。

这类方法的关键特征是，目标 artifact 主要承担"动作压缩"或"动作空间扩展"功能。原本需要多步低层操作完成的行为被抽象为一个高层可调用单元。与自然语言 skill description 不同，programmatic skill 的复用不完全依赖 LLM 的自由理解——它们通常可被 executor、runtime、browser automation framework 或 environment interface 直接执行。

**代表性工作。** Voyager [Wan23c] 将 Minecraft 中经过 environment feedback、execution error 和 self-verification 逐步打磨成功的 JavaScript action programs 沉淀为 executable skills，在新任务中按语义检索后作为高层代码组件复用。ASI [Wan25d] 从 Agent 自身成功的 web trajectories 中清洗出高质量 action subsequences，诱导出 parameterized Python skills，并要求用新 skill 重写原轨迹再重新执行——只有能够复现成功的 skill 才能入库，从而把 trajectory abstraction 与 execution-grounded re-verification 紧密结合。MobileGPT [Lee23] 将 app interaction history 组织为 transition graph，把 sub-task 存成可实例化的 function-call style memory，以压缩低层 GUI 操作。

SkillWeaver [Zhe25c] 让 web agent 通过自提出任务和反复 practice 收集成功轨迹，再把 state-action sequences 抽象为带 generalized parameters 的 Python plus Playwright APIs，并通过 unit tests、execution feedback 和 iterative debugging 持续修补。WebXSkill [Wan26d] 从 synthetic web trajectories 中抽取可复用 action subsequences，编译为带 typed parameters、element references 与 step-level guidance 的 JSON skills，并按 URL pattern 组织为 skill graph。PSN [Shi26] 将 skill 表示为带 explicit preconditions、postconditions 和 subskill dependency 的 symbolic programs，允许系统在长期任务流中对这些技能进行组合、修补、抽象与重构。MOBIMEM [Liu25i] 在 mobile agent 中把 trajectories 与 user corrections 编译为 multi-level experience templates 和 ActChain，并通过 exception-driven updating 与 stale detection 持续修正旧经验。AutoRefine [Qiu26] 从成功与失败轨迹的对比分析中抽取 skill patterns 与 subagent patterns，将复杂子任务封装为可调用的 reusable expertise。

Programmatic Skill Construction 的优势在于可执行性、可验证性和可组合性较强，artifact 可通过运行结果判断有效性，也可在更复杂任务中组合多个 skill。局限在于对环境接口稳定性高度敏感，skill 泛化边界难以确定，skill library 持续增长后需配套 selection、deduplication、versioning 和 stale detection 机制。

### §3.2.2 Procedural Workflow Induction

Procedural Workflow Induction 从多步 Agent trajectories 中归纳可复用的任务流程结构：workflow、DAG、hierarchical procedure、task tree、stage-action hierarchy 或 workflow template。这类方法关注的不是把某一段动作封装成单个可调用 skill，而是抽象出完成一类任务所需的阶段划分、步骤顺序、依赖关系、控制流、条件分支、前置条件和后置状态。

许多复杂任务的可复用经验并不体现在某个孤立动作中，而体现在任务执行过程的组织方式中。成功轨迹往往包含稳定的阶段模式：先收集信息，再筛选候选项，再验证约束，最后执行提交；失败轨迹也可能揭示步骤顺序、依赖检查或条件判断的缺失。通过从轨迹中归纳 workflow，Agent 获得一种比单步 skill 更高层的 procedural scaffold。

与 Programmatic Skill Construction 相比，Procedural Workflow Induction 的粒度更高：前者把经验转化为可调用动作单元，强调 executable skill；后者把经验转化为任务流程结构，强调 task-level control flow。一个 programmatic skill 可以是 workflow 中的一个节点，一个 workflow 可以调度多个 skill、工具或子任务。

**代表性工作。** Agent Workflow Memory [Wan24] 从 web trajectories 中提取重复出现的 routines，并通过槽位化去除实例细节，使 workflow 成为可跨任务检索与复用的过程记忆。WorkflowGen [Wei26] 将历史执行经验组织为 generalized workflow templates，并根据当前任务与既有经验的匹配程度，在直接复用、局部重写与重新生成之间自适应切换。FlowMind [Liu26] 先通过执行获得 reasoning and tool traces，再在独立阶段中将其重建为显式 workflow graph，编码 sequential、branching、loop 等控制流。Hierarchical Memory Tree [Tan26] 将 web experience 重写为 intent、stage、action 三层结构，在 stage 层显式引入 pre-condition 与 post-condition，使 Agent 能够依据当前观测判断所处阶段，再将抽象动作映射到具体页面。MACLA [For25] 把交互经验压缩为带 goal、precondition、abstract action sequence 和 postcondition 的 procedures，进一步组合出带 continue、skip、repeat、abort 控制逻辑的 meta-procedures，并通过 Bayesian selection 与 contrastive refinement 持续维护。

MOBIMEM [Liu25i] 将 execution logic 提炼为带参数槽位和依赖关系的 multi-level templates。Environment Maps [Fen26] 将 screen recordings 与 execution traces 编译为持久化的环境表示，在 contexts、parameterized actions 与 tacit knowledge 之外显式保留 observed workflows，使过程结构成为 long-horizon planning 的可查询对象。Skill-Pro [Mi26] 虽从经验中归纳多步 procedural units 并显式描述 activation、execution 和 termination conditions，但其最终产物是可调用 skill pool 而非用于组织整类任务执行的 workflow structure，更适合作为 Programmatic Skill Construction 的边界案例。

Procedural Workflow Induction 的优势在于可解释性和可控性较强，workflow artifact 更短、更抽象、更易定位任务中的关键阶段，且显式表达步骤依赖和执行顺序。主要挑战在于抽象粒度控制——workflow 过于具体则难以泛化，过于抽象则可能丢失关键上下文——以及 workflow drift 问题：环境状态变化后原有 workflow 可能不再适用，需配套 consistency checking、precondition verification 和更新机制。

### §3.2.3 Structured Memory Graph Construction

Structured Memory Graph Construction 将 Agent trajectories 中出现的实体、关系、状态变化、空间结构、事件依赖或交互历史转化为可检索、可遍历、可更新的图结构记忆。这类方法的目标不是直接生成可执行动作，也不是主要归纳任务流程，而是构建 Agent 对环境、任务世界、历史经验或多智能体交互关系的结构化表示。

Agent 的许多经验不适合被表达为线性文本或固定流程，而更适合组织为关系结构：环境中的对象之间有空间关系，动作会改变状态，历史事件之间存在时间或因果联系，多智能体交互中存在角色、任务、信息流和依赖关系。若这些关系仅以 raw logs 或自然语言 memory notes 存储，后续 Agent 很难进行精确检索、局部更新和多跳推理。

**代表性工作。** AriGraph [Ano24] 在 text-game 场景中将每一步文本观测抽取为 semantic triplets，并与按时间组织的 episodic nodes 相连，形成同时编码世界知识与情节历史的 knowledge graph world model；当环境状态变化时，系统还会删除被新观测推翻的旧关系。G-Memory [Zha25] 面向 multi-agent systems，将协作中的 utterance、task query 与 distilled insight 组织为 interaction graph、query graph 和 insight graph 三层层次化图记忆，使系统能够在细粒度交互证据与高层协作经验之间双向追踪。MOBIMEM [Liu25i] 用 DisGraph 组织 user profile 中的概念与实体关系，同时把任务经验表示为 DAG-like templates，结合动作级结构支持复用与更新。A-MEM [Xu25b] 将交互经验拆解为带有 keyword、tag、context description 与相互链接的 atomic notes，通过 LLM 持续生成和修订 note 之间的连接，使记忆网络随新经验不断重组。BrainMem [Ma26] 在 embodied task 中同时维护 Spatial KG 与 Trajectory KG，并在 episode 结束后进一步蒸馏为 semantic guidelines。

Structured Memory Graph Construction 与 Procedural Workflow Induction 的区别在于图的语义功能：workflow graph 回答"任务应该如何执行"，其节点和边表示步骤顺序、控制流或任务依赖；memory graph 回答"环境中有什么、状态如何变化、历史经验之间有什么关系"，其节点和边表示实体、状态、事件、空间或交互关系。

这类方法的优势在于支持关系级别的记忆复用，图结构更容易局部更新，适合 embodied agents、web agents 和 multi-agent systems 的 long-horizon planning 和 state tracking。困难在于图抽取过程容易产生错误实体和错误关系，图记忆随时间增长后可能出现 memory bloat、过时信息和 retrieval noise，通常需要配套 graph update、conflict resolution、pruning 和 confidence estimation 机制。

### §3.2.4 Other Schematic Artifacts and Boundary Cases

除上述三类外，还有一些方法产生的 artifact 具有一定结构化特征，但难以稳定归入某一个 P2 子类。本文将其作为 boundary cases 单独讨论，同时明确 P2 的边界。

**Semi-structured Narrative artifacts。** 一些方法将轨迹总结为 workflow、skill、SOP 或 guideline，这些 artifact 虽在表面上具有编号、字段或步骤结构，下游消费时仍主要依赖 LLM 的自然语言理解，无 parser、executor 或 graph traversal module 介入。这类方法更接近 P1，可作为边界案例澄清"structured text"并不必然等于 Schematic artifact。

**Hybrid schematic-narrative artifacts。** 一些方法同时产生 code snippets、natural-language guidelines、memory notes 或 semi-structured procedures。对此类方法不能简单按论文术语整体归类，而应分析核心贡献和主要消费机制。若系统的关键能力来自 executable skill、workflow schema 或 graph memory，可作为 P2 的混合案例；若结构化部分只是辅助说明，核心复用仍依赖自然语言提示，则应归入 P1。

**Source-side ambiguity。** 某些方法确实生成了 code、workflow 或 graph 等 Schematic artifacts，但这些 artifacts 并非从具体 Agent trajectories 中提炼，而是由模型根据任务描述、专家知识或参数化能力直接生成。这类工作更接近 P7（Parametric-to-Tokenized externalization）或一般的 program/workflow synthesis。

**Composite pipelines。** 有些系统先将 trajectory 转化为 Schematic artifact，再将这些 artifact 用于数据合成、SFT 或 RL。若论文核心贡献是从经验到参数的内化，Schematic artifact 只是中间表示，则更适合归入 Composite（§7）或 Tokenized-to-Parametric pathway。P2 章节可引用这些方法说明 Schematic artifact 的中介作用，但不作为纯 P2 方法。

**Non-agent traces。** 从 human demonstrations、system logs 或 screen recordings 中构建 workflow graph 或 action graph 的工作，若源数据不是 LLM-based Agent 在序贯决策中产生的 experience loop，则不纳入 P2 主 taxonomy，可作为相关背景或外部启发。




