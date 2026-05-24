
# Tokenized-to-Tokenized Transformations
## Narrative-to-Narrative Transformation
### Per-Trajectory Experience Abstraction

- Reflexion: Language Agents with Verbal Reinforcement Learning [Shi23b]  
  该方法在每次 trial 结束后，依据失败轨迹与环境反馈生成简短的自然语言 reflection，将一次执行中的错误归因、教训和改进建议压缩成 episode-level verbal memory，并在下一次尝试时直接拼接回 prompt。论文的消融还表明，事后生成的 reflection 比直接回放原始 trajectory 更有效，说明其核心贡献不是“存历史”，而是“把历史抽象成可复用经验”。

- Reflection-Based Memory For Web Navigation Agents [Aza25]  
  该方法面向 web navigation，将单条成功或失败的浏览轨迹事后总结为 Web-Reflection，内容包括有效步骤、站点功能局限、捷径、回溯点与改进建议，并以 task instruction 为键存入 memory。推理时系统检索语义相近的 reflection 注入当前规划，使 agent 能从过去一次具体网页交互中提炼出可跨 session 复用的局部经验。

- REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction [Liu23]  
  REFLECT 将单次机器人执行中的多模态观测流先转成分层事件摘要，再在子目标验证失败时生成自然语言 failure explanation，明确指出失败发生的位置、原因及其与当前计划的关系。该 explanation 进一步驱动后续 correction planning，因此其关键不是跨任务统计学习，而是把一次失败 trial 压缩成可指导下一次修正的文本经验。

- MemOrb: A Plug-and-Play Verbal-Reinforcement Memory Layer for E-Commerce Customer Service [Hua25]  
  MemOrb 在每轮客服任务结束后，对整轮对话轨迹与工具使用过程做 post-hoc reflection，生成简洁的策略性文本总结，并封装为可检索的 Orb memory 单元。它强调从单轮交互中提炼“为什么成功或失败、下次应如何做”的 verbal reinforcement，再通过语义检索把这些经验回注到后续对话中。

- Sample-Efficient Online Learning in LM Agents via Hindsight Trajectory Rewriting [Hu25]  
  该方法并不直接保存失败轨迹，而是在 episode 结束后用 hindsight rewriting 将其重写为针对其他潜在目标的“合成成功轨迹”或更短的 workflow 描述，从而把一次失败探索转化为可复用的正向 in-context experience。相较于原始失败日志，这种事后改写去除了与新目标无关的噪声步骤，保留了可迁移的环境发现与行动结构。

- Self-Generated In-Context Examples Improve LLM Agents for Sequential Decision-Making Tasks [Sar25]  
  该方法让 agent 从自身完成任务的轨迹中自动构造 self-generated in-context examples，并在后续规划与执行时按需检索相似示例作为 prompt 内 demonstration。它更像是把单条成功经验整理成可复用的自然语言 exemplars，而不是生成显式 critique 或 lesson learned，但本质上仍属于 per-trajectory 的经验抽取与上下文复用。

- MemGovern: Enhancing Code Agents through Learning from Governed Human Experiences [Wan26ap]  
  MemGovern 从单个 issue 修复过程中的 governed human experience 中提纯出结构化 experience card，将具体修复案例抽象为 problem summary、diagnostic signals、root cause、fix strategy 和 verification 等文本字段。虽然它比一般 reflection 更规范化、也更接近经验卡片化，但其基本单位仍是一条具体修复经历的事后抽象，再通过检索用于后续代码 agent 的类比修复。

### Cross-Trajectory Experience Induction

#### 核心组

- [Zha23c] ExpeL  
  ExpeL 不再只对单次失败做反思，而是从训练任务池中联合利用“失败-成功对”与跨任务成功轨迹集合，通过 `Insight Extraction` 抽取可迁移的自然语言 insight。其核心是对经验库中的规则做 `ADD / EDIT / UPVOTE / DOWNVOTE` 式迭代维护，使 artifact 成为一个持续演化的经验规则库，而不是单条轨迹的事后总结。

- [Fu24] AutoGuide  
  AutoGuide 从同一任务上的优劣轨迹对中定位首次决策分叉点，再用 `Context Identification` 和 `Guideline Extraction` 将该局部差异归纳成与情境绑定的 guideline。它的关键贡献是把“成功与失败在哪个上下文下分开”显式化，因此得到的是可检索、可条件触发的 context-aware guideline，而非泛泛 reflection。

- [Ni26] Trace2Skill  
  Trace2Skill 先在任务集上并行收集大量成功与失败轨迹，再分别由 `Success Analyst` 和 `Error Analyst` 生成局部 skill patch，最后通过分层 `Patch Merge` 只保留跨轨迹重复出现的“prevalent patterns”。最终 artifact 是一个可直接注入系统提示的技能目录，包含自然语言 SOP 与辅助脚本，强调的是从多条轨迹中归纳稳定技能，而不是沿单条轨迹顺序修修补补。

- [Not24] Skill Set Optimization  
  Skill Set Optimization 从多条历史轨迹中抽取高奖励且在状态-动作嵌入空间相似的子轨迹对，再让 LLM 将这些重复出现的局部模式概括成“subgoal + instructions”形式的 transferable skill。它的 cross-trajectory 性不在于显式 success-failure 对比，而在于对跨轨迹相似子过程做抽取、评分、采样与后续基于收益的剪枝，持续优化一个可检索的 skill set。

- [Che25d] SWE-Exp  
  SWE-Exp 从跨仓库的软件修复轨迹中同时提炼成功经验与失败反思，由 `ExpAgent` 将原始 issue-resolving 过程归纳为 `Comprehension Experience` 和 `Modification Experience` 两类自然语言经验条目。推理时，这些经验不是当作原始示例回放，而是经检索、重排和 `Reuser Agent` 二次适配后，转化为对新 issue 的高层理解视角与修改策略。

- [Su25] Mistake Notebook Learning  
  MNL 聚焦于成批失败轨迹，而不是单次失败；它先按语义主题做 `Subject Clustering`，再在簇级别抽取共性错误、纠正方法与 anti-pattern，形成结构化 mistake note。其关键点是“batch-clustered failures + accept-if-improves”更新准则：只有当新归纳的笔记能提升该批次表现时才写入，从而抑制单条失败带来的偶然噪声和过拟合。

- [Che24] AutoManual  
  AutoManual 让 Planner 在环境中持续交互，再由 Builder 根据 `Direct Success / Indirect Success / Failure` 三类轨迹结果执行差异化规则归纳，通过 `write_rule`、`update_rule` 和 `Consolidator` 将多次交互沉淀为手册式规则系统。与单轨迹 reflection 不同，它最终形成的是跨任务累积、可统一编排的 instruction manual，更接近长期维护的经验操作手册。

#### 边界组

- [Wu26] Procedural Knowledge at Scale Improves Reasoning  
  这篇工作更像 reasoning 侧的边界案例：它把大规模推理轨迹先做 `Trajectory Decomposition`，拆成子问题，再生成对应的 subroutine，构成海量“subquestion-subroutine”程序性知识库。它确实是跨轨迹归纳 procedural knowledge，但输入更偏 reasoning traces，而不是典型 agent 在环境中的交互 episode。

- [Suz25] Dynamic Cheatsheet  
  Dynamic Cheatsheet 通过 `Memory Curator` 从多次测试时解题轨迹中提炼 strategy、solution sketch、code snippet 与 insight，并持续执行修订、替换、合并与压缩。它可放在本组，但属于偏 S-Tok 的边界案例，因为 artifact 已不只是 narrative lesson，而是带结构的 cheatsheet，里面部分条目已接近代码模板和过程化工具。

- [Tan25] Agent KB  
  Agent KB 将来自不同 agent 框架、不同任务域的大量轨迹抽象成统一 schema 的 `Experience Unit`，再通过去重、冲突消解与 utility-based eviction 维护一个可演化的跨域经验库。它可以归入 cross-trajectory induction，因为核心确实是跨任务聚合经验；但它同时明显与 structured KB 路线接壤，因为 artifact 已是显式 schema 化、API 化的知识单元，而非纯自然语言 insight。


### Dual-Granularity Experience Consolidation

#### 核心对应论文

- CLIN [Maj23]：把单次 trial 的成败经验写成因果式 textual abstraction，如“X is necessary for Y”或“X does not contribute to Y”。更关键的是，它再从多轮 episode 中抽取 meta-memory，把局部因果经验继续抽象成跨任务可迁移的高层经验。  

- R2D2 [Hua25e]：对单条 web trajectory 做失败定位、截断回放与反思，生成可复用的 corrective reflection。随后系统把这些 episode 级反思持续写回全局 reflective memory，并通过更新机制用更优轨迹替换旧记忆。  

- Darwinian Memory [Mi26b]：把长轨迹切成以子目标为单位的 plan-trajectory memory entry，而不是直接存整条日志。之后用 evolutionary replacement、survival value 和基于效用与时效的淘汰机制，让跨 episode 的记忆不断被更短、更可靠的新版本取代。  

- Learning on the Job [Yan25d]：先把局部成功子任务写成 SOP 形式的 procedural memory，支持短期快速复用。任务完成后再做全局 deduplication、generalization 与 strategic memory 提炼，把局部 SOP 上升为更稳定的长期知识。  

- Remember Me, Refine Me [Cao25]：从单条轨迹中抽取结构化 experience，尤其强调 keypoint-level procedural memory，而不是保留冗长原始轨迹。之后系统持续跟踪这些 memory 的检索次数与成功效用，做验证、去重和低效记忆删除，是非常标准的 dual-granularity consolidation。  

- Contextual Experience Replay [Liu25]：从每条 trajectory 同时抽取两类经验，局部环境 dynamics 和较高层的 decision-making skills。新经验写入时会显式参考已有 buffer 以避免重复，因此“当前写入”本身就受“历史整合状态”约束。  

- GUI-explorer [Xie25]：从单次 GUI transition 抽取细粒度的 transition-aware knowledge，把局部 state-action-effect 写成可检索知识项。随后通过相似度匹配、拼接合并和知识排序器，把这些局部条目持续并入全局知识库。  

- Coarse-to-Fine Grounded Memory [Yan25]：先把单任务探索得到的 trajectory 存入 experience pool，再按任务聚合成功与失败样本，抽取 consolidated tips dictionary。它明确连接了“单轨迹写入”和“多轨迹对比归纳”，只是后续长期维护机制还不算很强。  

- H2R [Ye25b]：从单条经验里同时写入 high-level planning memory 和 low-level execution memory，并从成功失败对比中提炼 planning insight 与 execution insight。更进一步，这些 insight 不是静态追加，而是通过 add、modify、upvote、downvote 持续更新全局 insight pool。  

- Memp [Fan25]：同时保留 fine-grained trajectory 和 high-level script 两种粒度的 procedural memory。它的关键贡献在于把 memory update 单独做成一个阶段，通过 validation 式 consolidation 和 failure-driven adjustment 来修订、压缩和纠错。  

- What Deserves Memory [Ma25]：先把连续交互切成 narrative episode，再提取 episodic cue 与 semantic insight。之后通过 episodic integration 与 semantic consolidation 做 merge、conflict resolution 和过时知识替换，是少数把“记什么”和“如何整合”同时做深的方法。  

- Agentic Context Engineering [Zha25f]：从单次 reasoning trajectory 中抽取细粒度 delta bullets，而不是整段重写 prompt。随后这些 delta 通过 curator 进入持续演化的 context playbook，并配套做语义去重、lazy refinement 和低效条目裁剪。  

- WebCoach [Liu25e]：把每个完整 browsing episode 压缩成结构化 cross-session memory record，并只持久化“已完成”的 episode，避免把半成品噪声写入长期记忆。虽然它的整合主要体现在持续累积和检索路由，而不是强 merge/prune，但已具备明确的写入—跨 session 复用闭环。  

- MobileGPT [Lee23]：从单次 mobile interaction 中抽取子任务和动作序列，并写入 app-specific transition graph。其长期价值在于把不同任务中的共享 subtask 合并到同一图结构里，使局部操作经验逐渐沉淀为跨任务的 app memory。  

#### 可纳入，但建议在文中注明“偏程序化 skill consolidation”

- AutoSkill [Yan26]：从近期交互中抽取 skill candidate，再与已有 skill bank 做 add、merge 或 discard。它确实有版本化更新、去重和持续演化，但承载物更像显式 skill artifact，而不是典型 narrative memory。  

- SkillClaw [Ma26b]：把多用户 session trajectory 聚合成共享 evidence，再由 agentic evolver 夜间批量更新全局 skill repository。它很强地体现了 cross-episode consolidation，但更接近 collective skill evolution，而不是 episode memory 向 narrative store 的演化。  

- SkillX [Wan26]：从单条成功轨迹抽取 planning、functional 和 atomic 三层 skill，再通过聚类、merge、filter 更新 skill library。它的方法论与 dual-granularity consolidation 很接近，但最终产物是分层技能知识库。  

- M2 [Yan26b]：它有单轨迹 summary 的在线写入，也有多轨迹成功日志蒸馏出的 insight bank，但后者主要是离线构建、在线检索。严格说，它更像“局部在线 summarization + 静态跨轨迹知识库”，弱于真正在线演化的 consolidation。  

#### 边界论文

- Get Experience from Practice [Fen25]：核心是把多条 execution trace 总结为 high-level 和 low-level experience graph，并支持 replay 与 repository update。它是很强的前驱工作，但更偏 record-replay 与经验图编译，而不是 agent 自身的长期 narrative memory 维护。  

- Mirage-1 [Xie25b]：从单条 GUI 轨迹抽取 execution skill，再向上合并为 core skill 和 meta skill。它确实有层级更新，但重点是 hierarchical multimodal skill abstraction 与 planning，不是 memory lifecycle 本身。  

- Meta-Policy Reflexion [Wu25]：把单次失败轨迹反思成结构化规则，并把规则追加到 meta-policy memory 中供后续检索与 admissibility check。它连接了局部反思与长期规则库，但缺少真正成熟的 merge、prune、staleness handling，因此更像 early-stage rule accumulation。  

- Learning from Online Videos at Inference Time [Liu25b]：把在线视频切分成 demonstration trajectories 供当前任务检索使用。它主要是 inference-time external demonstration selection，不是 agent 在自身交互过程中进行长期写入、整合与更新。  


## Narrative-to-Schematic Experience Transformation

### Programmatic Skill Construction

#### 核心论文

| 论文 | 适配度 | 可直接放入正文的 1到2 句表述 |
| --- | --- | --- |
| Voyager [Wan23c] | 核心 | Voyager 将 embodied interaction 中逐步调试成功的 JavaScript action programs 沉淀为可检索的 skill library，并用 description embedding 做索引，在新任务中把这些 code skills 作为高层 action 组件参与后续程序生成。其关键不只是“记住轨迹”，而是把经过 environment feedback、execution error 和 self-verification 稳定下来的操作序列编译成可组合、可执行的技能单元。 |
| SkillWeaver [Zhe25c] | 核心 | SkillWeaver 让 web agent 通过自提出任务与反复 practice 收集成功轨迹，再把 state-action sequences 抽象成带参数的 Python plus Playwright APIs，并通过 unit tests 与 iterative debugging 持续打磨。生成后的 skill 不再是自然语言建议，而是带 function signature、docstring、precondition 和 usage log 的 executable web routine。 |
| WebXSkill [Wan26d] | 核心 | WebXSkill 从 web trajectories 中抽取可复用 action subsequences，将其编译为带 typed parameters、element references 与 step-level guidance 的 JSON skill，并按 URL pattern 组织成 skill graph。它特别强调 skill 的“grounded executability”，使 artifact 既可被 runtime 直接原子执行，也可作为高层引导供 agent 自适应展开。 |
| Inducing Programmatic Skills for Agentic Tasks [Wan25d] | 核心 | ASI 从 agent 自身成功的 web trajectories 中清洗出高质量片段，再诱导出 parameterized Python skills，并通过“用 skill 重写原轨迹再重新执行”的 re-verification 机制过滤无效技能。与 text skill 相比，这类 programmatic skill 具有更清晰的 functional boundary、更强的 execution verifiability，以及更好的长程任务压缩效果。 |
| Evolving Programmatic Skill Networks [Shi26] | 核心 | PSN 将 programmatic skill construction 从“一次性诱导”推进为“持续演化”的 skill network：技能被表示为带 precondition、postcondition 与 children links 的 symbolic programs，并可在执行中被组合、修补、抽象与重构。其重点不只是从轨迹提炼 skill，而是让 skill library 具备 mutation、refactor、deduplication 和 maturity-aware maintenance 的生命周期。 |

#### 边界但值得纳入

| 论文 | 适配度 | 可直接放入正文的 1到2 句表述 |
| --- | --- | --- |
| MobileGPT [Lee23] | 次核心 | MobileGPT 将移动端 app interaction history 组织为 app-specific transition graph，把 sub-task 存成 function-call style 的 parameterized routines，并通过 UI attribute matching 在新任务中回放和适配。它更像“replayable action chain memory”而非完整代码合成，但本质上也在把低层 GUI 操作压缩为可调用的高层操作单元。 |
| Beyond Training: Enabling Self-Evolution of Agents with MOBIMEM [Liu25i] | 次核心 | MOBIMEM 把 mobile trajectories 与 user corrections 编译为 multi-level experience templates，以及支持前缀复用与链式复用的 ActTree 和 ActChain，将 invariant control logic 与 variable slots 分离。它体现的是 program-like memory 的持续演化版本，重点在 template synthesis、exception-driven updating 与 rollback-based stale detection。 |
| AutoRefine [Qiu26] | 边界 | AutoRefine 从成功与失败轨迹的对比分析中抽取 reusable expertise，并把结果分成 lightweight skill patterns 与更复杂的 subagent patterns。它不总是产出纯 executable code，但复杂子任务被封装为可调用的 specialized subagent，因此可以作为 Programmatic Skill Construction 向“callable procedural expertise”扩展的边界案例。 |

### Procedural Workflow Induction

| 论文 | 可用于 Survey 正文的 1–2 句描述 | 归类判断 |
|---|---|---|
| Agent Workflow Memory [Wan24] | 该文从成功的 web trajectories 中抽取可复用 routine，并把实例化细节替换成 slot，形成由 environment description、reasoning、action 组成的 workflow sequence。其核心不是重放完整轨迹，而是诱导可跨任务复用的阶段化流程，并在 offline 与 online 两种模式下持续写入 memory。 | 典型 Procedural Workflow Induction |
| WorkflowGen [Wei26] | 该文把历史执行轨迹抽象成 generalized workflow template，同时区分 fixed node 与 variable node，并保存工具映射、参数 schema、错误指纹与异常规避经验。推理时它按相似度在 direct reuse、rewrite variable nodes、full initialization 三条路由间切换，本质上是“模板化 workflow 重写”而非从头规划。 | 典型 Procedural Workflow Induction |
| FlowMind [Liu26] | 该文提出 Execute-Summarize 两阶段框架，先让 agent 自由完成任务，再在独立 summarize 阶段把 execution trace 重建为结构化 workflow graph。其 workflow 显式编码 sequential、branching、loop 等控制流，并通过黑盒执行验证生成流程是否真的可运行。 | 典型 Procedural Workflow Induction |
| Enhancing Web Agents with a Hierarchical Memory Tree [Tan26] | 该文把原始 web trajectories 归纳成三层 Hierarchical Memory Tree：intent、stage、action，其中 stage 带有显式 pre-condition 与 post-condition，action 存储可迁移的 semantic grounding 而非站点特定 DOM 标识。推理时 planner 先按条件判断当前所处阶段，再由 actor 将抽象动作落到当前页面，专门解决 workflow mismatch。 | 很强的 Procedural Workflow Induction |
| Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement [For25] | 该文把轨迹切分并压缩为 procedure，单个 procedure 包含 goal、precondition、abstract action sequence、postcondition，进一步还会把高频 procedure 序列组合成带 continue、skip、repeat、abort 控制逻辑的 meta-procedure。Bayesian selection 负责按可靠性与上下文效用选取 procedure，contrastive refinement 则利用成功失败对比来收紧条件和修复流程。 | 偏层级 procedural memory，与 workflow induction 高度一致 |
| Beyond Training: Enabling Self-Evolution of Agents with MOBIMEM [Liu25i] | 这篇题名里正式写法是 MOBIMEM。其 Experience Memory 不是保存原始轨迹，而是把移动端执行经验蒸馏为带参数槽位的 multi-level template 和 DAG-style execution logic，再由 scheduler 按依赖关系实例化与并行调度；同时用 Action Memory 处理更细粒度的 UI 操作复用。 | 可放入 Procedural Workflow Induction，但更偏 memory-centric system |
| Environment Maps [Fen26] | 该文把 screen recording 与 execution traces 编译成 Environment Map，统一存储 contexts、parameterized actions、observed workflows 与 tacit knowledge。这里 workflow 不只是步骤摘要，而是环境图中的持久过程结构；论文还直接比较了 raw trajectories 与 structured maps，后者对 long-horizon planning 更有效。 | 可放入 Procedural Workflow Induction，偏结构化环境过程模型 |
| Skill-Pro [Mi26] | 该文把经验转成具备 activation condition、execution procedure、termination condition 的 natural-language skill，并通过 Non-Parametric PPO 生成候选技能，再用 PPO Gate 做历史轨迹上的可靠性验证。虽然 skill 内部有多步 procedure，但其 memory 组织形式是可调用 skill pool，而不是显式 task-level workflow，因此更适合放在 Programmatic Skill Construction。 | 更适合 Programmatic Skill Construction 的边界例子 |


### Structured Memory Graph Construction

| 论文 | 归类判断 | 可直接放进 Survey 正文的 1到2 句描述 |
|---|---|---|
| AriGraph: Learning Knowledge Graph World Models with Episodic Memory for LLM Agents [Ano24] | 核心匹配 | AriGraph 将 text-game 交互中的文本观测持续抽取为 semantic triplets，并与按时间组织的 episodic nodes 共同构成一个可更新的 knowledge graph world model。该图不仅显式维护实体关系与情节关联，还支持过时事实删除与从 semantic relation 到 past episode 的联动检索，从而为后续规划和动作选择提供结构化环境记忆。 |
| G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems [Zha25] | 核心匹配 | G-Memory 将多智能体协作中的对话、任务执行记录与蒸馏出的高层 insight 组织成三层图记忆，即 interaction graph、query graph 和 insight graph。其核心不是诱导固定 workflow，而是把历史协作经验表示为可双向遍历的关系结构，使 agent 能同时追踪细粒度交互证据与高层协作规律。 |
| Environment Maps: Structured Environmental Representations for Long-Horizon Agents [Fen26] | 核心匹配 | Environment Maps 将 browser traces、DOM、accessibility tree 与 screenshot 等交互经验转化为由 contexts、parameterized actions、workflows 和 tacit knowledge 组成的结构化环境地图。该表示以环境情境和可供性为中心，对界面状态与操作关系进行持久化建模，使 agent 可以按需检索局部环境结构，而不必反复依赖原始轨迹。 |
| BrainMem: Brain-Inspired Evolving Memory for Embodied Agent Task Planning [Ma26] | 部分匹配，偏强 | BrainMem 在 embodied task 中同时维护 Spatial KG 与 Trajectory KG，前者编码房间、物体及其空间关系，后者记录动作转移与任务结果，并在 episode 结束后进一步蒸馏为 semantic guidelines。它明显包含 structured memory graph construction，但其贡献也延伸到从 episodic graph 向 procedural and semantic knowledge 的进一步抽象。 |
| Beyond Training: Enabling Self-Evolution of Agents with MOBIMEM [Liu25i] | 部分匹配，偏边界 | MOBIMEM 用 DisGraph 显式组织 user profile 中的概念与实体关系，并结合 DAG-like experience templates、ActTree 和 ActChain 来管理执行经验与动作复用。它适合放在本节，尤其因为其 profile memory 与 experience template 都是对交互经验的结构化重组，但它更像“多种结构化 memory 联合管理”而非单一 memory graph 方法。 |
| A-MEM: Agentic Memory for LLM Agents [Xu25b] | 部分匹配，偏边界 | A-MEM 将轨迹经验拆解为带有 keyword、tag、context description 和 link 的 atomic notes，并通过 LLM 持续生成 note-to-note links 与 memory evolution，形成一个动态互联的 agentic memory network。它确实具有 graph-like structure，但更接近 Zettelkasten 式关系记忆，而不是显式的 environment graph、scene graph 或 state-transition graph。 |


# Tokenized-to-Latent Experience Transformation

## Cache-Based Latent Transformation

| 论文 | 正文可用描述 |
| --- | --- |
| Log-Augmented Generation [Che25b] | Log-Augmented Generation 将过去任务中的 reasoning log 保留下来，但真正复用的不是文本本身，而是这些 log 在 LLM 前向计算后形成的 KV states。方法先按语义检索相关历史 log，再对其 KV cache 做位置对齐后直接注入当前 `past_key_values`，让模型复用过去推理过程对应的内部计算，而不是重新阅读文本并再算一遍。 |
| TempoFit [Sun26] | TempoFit 面向 long-horizon VLA manipulation，将过去视觉观察与语言指令在前缀编码阶段形成的 layer-wise prefix KV states 持久化为 temporal memory。推理时当前 prefix keys 在同一 latent space 中匹配历史 keys，并把检索到的 KV 以 pre-attention residual 的方式写回冻结的 VLA，从而把历史交互直接转化为可消费的内部状态。 |
| Memorizing Transformers [Wu22] | Memorizing Transformers 将长序列中先前 token 的中间层 key value 表示写入外部 kNN memory，并在后续时间步通过近邻检索把这些 latent pairs 重新接入 attention。它本身不是 agent paper，但清楚展示了 token sequence 可被转化为可检索的 latent memory 并直接参与后续 hidden-state computation，因此更适合作为 P3 的机制前驱而非 agent-specific 核心方法。 |

## Prompt-Based Latent Transformation

| 论文 | 正文可用描述 |
| --- | --- |
| MAP-VLA [Li25g] | MAP-VLA 把机器人 manipulation demonstrations 先按阶段切分，再为每个 stage 学习一组 stage-specific memory prompts。底座 VLA 保持冻结，推理时系统根据当前执行片段匹配最相近的历史阶段，并把对应 soft prompt 加到 base prompt embedding 上，使 demonstration 中的阶段经验以连续提示而非文本示例的形式复用。 |
| ReasonCACHE [Gup26] | ReasonCACHE 将大规模 reasoning demonstrations 压缩为各层可训练的 prefix KV pairs，而不是把示例链条塞回上下文或更新模型权重。其核心是用冻结 backbone 加可学习 prefix cache 的方式，把推理经验固化为固定长度的 latent reasoning prior，在测试时作为可重用的 attention 前缀直接调控生成。 |
| TokMem [Wu25c] | TokMem 试图把 procedure-response pairs 中的 procedural knowledge 压缩进单个 memory token embedding，每个 token 同时是离散索引和连续控制向量。底座 LLM 冻结，推理时先根据 query 做 memory routing 选出最相关的一枚 token，再把它插入输入中触发相应 procedure，因此经验复用发生在 embedding-level latent carrier 上而不是自然语言规则上。 |

## Module-Based Latent Transformation

| 论文 | 正文可用描述 |
| --- | --- |
| LatentMem [Fu26] | LatentMem 先从 experience bank 中检索历史多智能体轨迹，再用 role-aware memory composer 把这些 tokenized trajectories 压缩成 agent-specific latent memory matrix。该 memory 直接拼接到当前 agent 的 hidden states 中参与推理，使同一段历史经验能够按不同 agent role 被重新编码和内化。 |
| Dual Latent Memory for Visual Multi-agent System [Yu26d] | Dual Latent Memory 将多智能体交互中的经验拆成 latent perception memory 与 latent thinking memory 两部分，前者保存多粒度视觉表征，后者保存推理轨迹的语义 chunk。系统只在当前 agent 解码不确定时触发读取，并把检索到的 latent units 直接注入 hidden states，从而以连续 memory 而非文本通信来复用先前 agent 的观察与思考。 |
| MemoryVLA [Shi25] | MemoryVLA 把 embodied interaction 中的经验编码为 perceptual tokens 与 cognitive tokens，并写入一个双通道的 Perceptual Cognitive Memory Bank。当前工作记忆通过 cross-attention 检索历史 latent entries，再经门控融合后条件化 diffusion action head，因此过去观察与认知状态不是以 textual memory，而是以长期维护的 latent bank 影响动作预测。 |
| Gated Memory Policy [Gao26] | Gated Memory Policy 面向需要 in-trial 或 cross-trial memory 的机器人任务，把历史图像与动作轨迹编码为缓存状态，并通过一个显式 memory gate 决定何时读取这些 latent history tokens。被激活的历史表示通过 cross-attention 残差接入 policy，使经验以按需调用的内部状态而非外显文本提示参与控制。 |
| HAMLET [Koo25] | HAMLET 为每个时间步学习一组 moment tokens，用它们提取当前场景的紧凑 latent summary，并把这些 summaries 缓存下来形成 history matrix。随后一个轻量 Transformer 在 latent space 中整合这些历史 moment representations，并把聚合后的 history-aware state 与当前表示拼接，令原本 memoryless 的 VLA 获得显式时序经验。 |
| Chameleon [Guo26] | Chameleon 将 long-horizon robotic manipulation 中的多视角视觉与 proprioceptive history 写入分层的 spatiotemporal slot memory，而不是保留文本化日志。其 episodic recall 通过 state-space memory dynamics 从 latent episodic bank 中读出 decision state，再由 rectified-flow policy 直接消费，因此更像是几何 grounded 的持续 latent episodic memory。 |
| EchoVLA [Lin25d] | EchoVLA 构建了 scene memory 加 episodic memory 的双层 declarative memory，其中 scene memory 保存持久空间语义结构，episodic memory 保存时间索引的多模态 interaction tokens。当前观测先检索两类记忆，再通过 coarse-to-fine cross-attention 融合为统一 latent state，用于移动操作中的 base 与 arm 联合决策。 |
| Hybrid Self-evolving Structured Memory for GUI Agents [Zhu26] | 这篇工作不是纯粹 latent memory，而是明显的 hybrid boundary case：它把 GUI trajectories 同时编码为 high-level strategy 与 attribute tags 这类结构化离散节点，以及可直接拼接到 embedding layer 的 low-level trajectory embeddings。其贡献在于展示 GUI 经验可以同时沿 symbolic pathway 与 latent pathway 演化，其中连续部分承担细粒度视觉与操作线索的复用。 |




## Tokenized-to-Evaluator Experience Transformation

### Outcome-supervised Evaluator Internalization

- [Sun25l] **S2J** 将 generative reward model 训练成“先 solve 再 judge”的 pairwise evaluator：模型先对问题自行求解，再结合两份候选回答给出偏好判断，并用 solving reward 与 judging reward 的联合 RL 目标更新参数。其关键点是把“是否能解出题”和“是否能判对优劣”这两个 outcome-level 信号共同内化进 judge 权重，从而缩小 solving ability 与 judging ability 之间的 gap。

- [Xu25i] **J4R** 将 pairwise LLM judge 作为被训练的 evaluator，本质上学习对完整 response pair 给出全局优劣判断，而不是监督中间推理步骤。其核心创新是提出 EIS-GRPO，通过对同一比较样本构造等价初始状态如 response order swap，并用 RL 强化最终 judgment correctness 与 position-robust consistency，使 judge 参数内化更稳定的 outcome-level preference semantics。

- [Wan24l] **RL-VLM-F** 不是直接把 prompt-only VLM 当 reward 用，而是先让 GPT-4V 或 Gemini-Pro 对 observation image pair 产生偏好标签，再训练一个参数化 reward model 作为真正用于 RL 的 evaluator。该方法的关键是把 foundation model 给出的 pairwise visual preference 蒸馏进 CNN 或 ResNet reward function，用 Bradley-Terry 式损失学习 outcome-level preference，从而把离散反馈转成可复用的环境内奖励。

- [Ala24] **Video-Language Critic** 训练一个 video-language critic，对 partial video history 与 language instruction 输出标量匹配分数，并将其作为 transferable reward function。它的关键做法是把视频-文本对齐信号与成功轨迹上的 temporal ranking 结合起来，使 evaluator 在没有逐步人工标注的情况下，从 episode-level caption 与成功时序中内化“越接近完成越高分”的全局评估语义。

- [Wu26e] **Large Reward Models** 将 Qwen3-VL 微调为通用机器人 reward generator，学习三类 outcome-oriented supervision：temporal contrastive reward、absolute progress reward 与 task completion reward。其关键思想是利用大规模无标签视频的时间单调性自动构造 frame pair 与 progress bin 监督，把 rollout 中隐含的完成度语义写入 evaluator 参数，形成可直接驱动在线 RL 的 dense reward engine。

- [Lee26b] **RoboReward** 训练通用 vision-language reward model，对完整 rollout video 与 task instruction 输出 1 到 5 的 episodic progress score，而不是对单步动作做局部判别。它的关键创新是通过 counterfactual relabeling 与 negative clipping，把原本多为成功轨迹的数据自动扩展成带有分级失败和部分完成标签的奖励数据，从而把 trajectory-level outcome semantics 内化为可泛化的 evaluator。

- [Mah24b] **Generative Reward Models** 将 reward modeling 改写为 next-token generation：evaluator 不再输出一个标量 head，而是生成 preference verdict，必要时还可先生成 CoT rationale 再给出结论。其核心方法是用完整 response pair 的 preference outcome 对 generative judge 进行 SFT 或 DPO 训练，并进一步用 STaR 式自举让“能导向正确 verdict 的 reasoning pattern”沉淀到 evaluator 参数中。

- [Liu25w] **VLP** 学习一个 trajectory-wise vision-language preference model，对完整 manipulation video 在给定 instruction 下输出全局偏好分数。它通过 ITP、ILP、IVP 三类 trajectory-pair preference 构造，把 expert、medium、random 等不同质量轨迹之间的 outcome-level ordering 用 Bradley-Terry 损失内化为 evaluator，从而为 embodied manipulation 提供可迁移的 preference-based reward signal。

- [Ma23d] **LIV** 将 language-image representation learning 与 reward learning 合并起来，从 action-free video 与 language annotation 中学习一个既能表征目标又能提供 reward 的 value-like evaluator。其关键不是逐动作监督，而是利用 trajectory toward goal 的时序结构和最终 outcome 对齐信号，用 VIP-I 与 InfoNCE 联合目标把“接近目标状态”的评估能力写入视觉-语言表示空间。

- [Du23] **Vision-Language Models as Success Detectors** 将 success detection 重新表述为 SuccessVQA，并通过微调 Flamingo 把轨迹是否达成任务的全局判定能力写入参数化 evaluator。该模型以图像或短视频片段和任务描述为输入，输出 yes or no 成功判断，本质上学习的是 episode outcome-level success semantics，而非中间步骤质量。

- [Qi24] **WebRL** 在整体自进化 RL 框架中训练了一个 outcome-supervised reward model，用用户指令、历史动作和最终网页状态来预测整条 web trajectory 是否成功完成任务。其关键点是把环境给出的最终成败信号内化为 ORM 参数，使 evaluator 成为 web agent 在线强化学习中的粗粒度终局 reward provider。

- [Son26d] **Video-Based Reward Modeling for Computer-Use Agents** 训练 Execution Video Reward Model，仅基于 user instruction 和 execution video sequence 对完整 computer-use trajectory 给出 success or failure judgment。该方法把视频执行结果中的全局完成语义内化进多模态 evaluator，并通过 video-level reward modeling 替代对内部 reasoning 或 action log 的依赖。

### Process-supervised Evaluator Internalization

- Let’s Verify Step by Step [Lig23]  
  该工作系统性确立了 process reward modeling 范式，用人工 step annotation 训练 PRM 对每个 reasoning step 输出 positive、negative 或 neutral 判断。其关键意义在于证明：相比只看最终答案的 outcome reward，step-level evaluator 更能支持 test-time reranking 与 search。

- Improve Mathematical Reasoning in Language Models by Automated Process Supervision [Luo24]  
  该方法用 rollout 与 binary search 自动定位 first error，并把前缀的可完成性转化为 soft process label 来训练 PRM。它表明过程监督不一定依赖昂贵的人类逐步标注，也可以由自动化搜索与 completion statistics 大规模构造。

- Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning [Set24]  
  该文强调过程监督不应只判断当前步骤是否正确，而应评估该步骤是否真正提高未来成功概率，因此训练 evaluator 去预测 step-level advantage。相比 correctness-only PRM，这种 progress-aware verifier 更适合为 search 和 RL 提供 dense reward。

- Process Reward Model with Q-Value Rankings [Li24m]  
  该工作将 PRM 的训练目标从逐步独立分类改写为 Q-value ranking，要求正确推理步骤随过程推进呈现更高价值，而错误步骤导致显著价值断裂。这样学到的 evaluator 更接近 value-style critic，而非单纯的局部正确性分类器。

- Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision [Pal25]  
  该方法在 step-level reward judgment 之前先区分 math error 与 consistency error 等层级化错误类型，再汇总为最终 reward 信号。它说明 process-supervised evaluator 可以先内化更细粒度的 error semantics，再压缩成可用于搜索的标量化过程监督。

- Better Process Supervision with Bi-directional Rewarding Signals [Che25s]  
  该工作联合训练 reward head 与 value head，让 evaluator 同时编码“当前这一步是否好”和“当前前缀未来是否还有希望”。这种双向信号把标准 PRM 从单纯的历史一致性判断，推进到兼顾前瞻性的 process evaluator。

- AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress [Xi25b]  
  该方法将 agent 中间决策分解为 Promise 与 Progress 两类局部信号，分别对应 action-value 与 advantage，并通过 TD 与 GAE 从 rollout 自动估计 pseudo-label。训练后的 evaluator 可直接用于 beam search、Best-of-N 和 RL，因此是 reasoning PRM 向 agentic setting 迁移的代表性工作。

- ProgRM: Build Better GUI Agents with Progress Rewards [Zha25z]  
  该工作不直接判断 GUI 动作对错，而是学习每一步对任务完成度的 progress value，并通过 LCS-based self-annotation 从成功轨迹中自动抽取关键步骤与相对进度。这样得到的 evaluator 更适合作为 long-horizon GUI task 的 dense local reward。

- Building Autonomous GUI Navigation via Agentic-Q Estimation and Step-Wise Policy Optimization [Wan26s]  
  该方法训练 step-wise 的 Agentic-Q evaluator，把 state-thought-action 三元组映射到成功概率，并将最终 outcome 向前传播为局部监督。它代表了 process evaluator 向 Q-like value model 的进一步推进，使 evaluator 可以直接支撑 step-wise policy optimization。

- GUI-Shepherd: Reliable Process Reward and Verification for Long-Sequence GUI Tasks [Che25h]  
  该工作面向 long-horizon GUI task 训练 step-level binary PRM，对 state-action 对直接输出 positive 或 negative judgment。其 evaluator 同时服务于 candidate action reranking 与在线 RL dense reward，体现了 process evaluator 在 GUI agent 中的双重用途。

- Advancing Mobile GUI Agents: A Verifier-Driven Approach to Practical Deployment [Dai25]  
  该文训练 generative verifier，对每一步 GUI decision 做 pairwise process preference 学习，使正确动作与多个错误动作之间形成稳定的分数差距。与只在任务结束后判断成败的方法不同，它把局部 action quality 显式内化进 verifier 参数中。

- IntentScore: Intent-Conditioned Action Evaluation for Computer-Use Agents [Che26s]  
  该工作训练轻量级 intent-conditioned action evaluator，对 state-action-intent 三元组输出 per-step correctness score，用于低延迟的 candidate reranking。它说明 process-supervised evaluator 不一定依赖大型生成式 judge，也可以由专门设计的小型 reward model 实现。

- GAIA: A Data Flywheel System for Training GUI Test-Time Scaling Critic Models [Wan26p]  
  该方法训练 step-level binary GUI critic，直接判断候选动作是 correct 还是 wrong，并通过 data flywheel 持续纳入真实 agent rollout 中的错误样本。其关键贡献在于把动态演化的 agent error distribution 转化为可持续更新的过程监督数据源。

- SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents [Dih26]  
  该工作面向 code agent，将读文件、编辑代码、运行测试等中间动作转化为 heuristic progress reward，并据此训练 PRM 预测局部动作价值。训练后的 evaluator 不只判断最终 patch 是否成功，而是为每一步 repository interaction 提供可搜索的局部 reward。


### Diagnostic-feedback Evaluator Internalization

- [Dua24] AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation  
  AHA 将 robotic failure evaluation 从单纯的 success or failure classification 改写为 free-form failure reasoning task，训练 VLM 对 manipulation 关键帧序列输出失败判断及自然语言 failure explanation。其核心方法是用 FailGen 程序化构造带失败类型与解释的数据，使 evaluator 能为 replanning、sub-task verification 和 reward refinement 提供可解释的诊断反馈。

- [Qi26] Self-Refining Vision Language Model for Robotic Failure Detection and Reasoning  
  该工作训练 ARMOR 同时输出 binary failure detection 和 open-ended failure reasoning，并通过 sparse detection labels 加 dense reasoning labels 的异质监督联合优化 evaluator。其关键点是用 iterative self-refinement 提升 failure explanation 质量，使模型不仅判断失败，还解释失败机制并支持 correction。

- [Wu25m] OS-Oracle: A Comprehensive Framework for Cross-Platform GUI Critic Models  
  OS-Oracle 将 GUI critic 建模为“rationale generation + yes or no judgment”的统一任务，而不是纯二分类器。作者通过跨平台 GUI 正负样本合成、rationale 标注、SFT 与 CP-GRPO 训练 critic，使其能对单步 GUI 动作给出具解释性的错误分析与判定。

- [Wan25q] Look Before You Leap: A GUI-Critic-R1 Model for Pre-Operative Error Diagnosis in GUI Automation  
  GUI-Critic-R1 是一个 pre-operative critic，在动作执行前生成 observation、possible result、critique、correctness score 和 corrective suggestion。其方法上先用 reasoning-bootstrapped CoT 数据做冷启动，再用 suggestion-aware GRPO 强化 critique 与 suggestion 质量，使 evaluator 直接承担 pre-action diagnosis 和 repair guidance。

- [Zha26ab] WebArbiter: A Principle-Guided Reasoning Process Reward Model for Web Agents  
  WebArbiter 将 web-agent evaluator 设计为 principle-guided generative PRM，先诱导与当前网页任务相关的 principles，再生成 structured justification 和最终 verdict。它的关键贡献是把可审计的 reasoning chain 与 reward estimation 合并，让 evaluator 不仅给出判断，还解释动作为何符合或违背任务推进原则。

- [Cha25b] Web-Shepherd: Advancing PRMs for Reinforcing Web Agents  
  Web-Shepherd 将 web-agent process evaluation 扩展为 checklist-grounded generative judging：模型先生成 task-specific checklist，再对当前动作输出 textual feedback，并逐项判断子目标是 Yes、No 还是 In Progress。虽然最终可转成 dense reward，但其关键创新在于把对网页状态、任务进展和动作偏差的解释性评估内化进 evaluator 参数。

- [Sch26] SOLE-R1: Video-Language Reasoning as the Sole Reward for On-Robot Reinforcement Learning  
  SOLE-R1 训练一个 video-language reward model，同时输出自然语言 reasoning 与 dense progress estimate，并将其作为 on-robot RL 的 sole reward。与仅给 scalar reward 的 reward model 不同，它会显式说明当前状态是前进、停滞还是倒退，以及尚缺失的子目标，因此具有明显的 diagnostic-feedback 特征。

- [Xu25h] Hybrid Reward Normalization for Process-supervised Non-verifiable Agentic Tasks  
  该工作中的 PPRM 将 search-agent 的过程评估建模为 principle-grounded generative critique：模型先动态选择 relevant principles，再在 analysis 中解释当前步骤在 correctness、relevance、consistency 等维度上的表现，最后输出可归一化分数。其关键点是把文本化原则分析与 process reward 结合，使 evaluator 同时具备可解释反馈和训练信号功能。

- [Li26l] No More Stale Feedback: Co-Evolving Critics for Open-World Agent Learning  
  ECHO 训练一个随 policy 同步演化的 linguistic critic，输出自然语言 diagnosis 与 concise actionable critique，而不是固定的静态 reward。它通过 dual-track GRPO 和基于 refinement gain 的 critic reward 更新 critic，使反馈持续适配 agent 不断变化的错误模式。

- [Zha26z] Don’t Act Blindly: Robust GUI Automation via Action-Effect Verification and Self-Correction  
  VeriGUI 将 GUI agent 的自检过程写成 Thinking, Verification, Action, Expectation 闭环，在失败时显式生成 Diagnose 与 Recovery 内容。其两阶段训练先用 synthetic failure trajectories 做 robust SFT，再用带 asymmetric verification rewards 的 GRPO 强化 honest verification 和 self-correction。

- [Zha26ac] AgentV-RL: Scaling Reward Modeling with Agentic Verifier  
  AgentV-RL 将 verifier 训练成一个 multi-turn, tool-using, deliberative evaluator，输出 reasoning trace、tool interaction 和最终 True or False verdict。其关键思想是把 reward modeling 从单步打分扩展为 agentic verification process，并通过 RL 将这种可解释审查能力蒸馏进单一 verifier 模型。

- [Xie25c] Teaching Language Models to Critique via Reinforcement Learning  
  该工作训练 code critique model 输出 analysis、actionable improvement suggestions 和 final judgment，并以“下游修复后代码是否通过 tests”作为 RL 信号。它突出说明了 diagnostic evaluator 的目标不是更准地打分，而是生成更有助于 repair 的反馈。

- [Yan25u] DeepCritic: Deliberate Critique with Large Language Models  
  DeepCritic 对 reasoning trajectory 的每一步生成长文本 critique、step judgment 与 first-error localization，而不是仅输出 step score。方法上先用 deliberate critique SFT 教会模型深度批判格式，再用 RL 依据最终判断正确性强化 critique 质量。

- [Xi24] Enhancing LLM Reasoning via Critique Models with Test-Time and Training-Time Supervision  
  该工作训练 critique model 对推理步骤进行 error identification 与 textual feedback generation，并将其同时用于 test-time refinement 和 training-time self-improvement。其关键方法是自动构造 flawed reasoning paths 与 critique supervision，使 evaluator 学会指出具体推理错误并提供修正线索。

- [Xio25c] StepWiser: Stepwise Generative Judges for Wiser Reasoning  
  StepWiser 将 stepwise judging 从黑箱式 PRM 改写为 generative meta-reasoning task，让 judge 先输出 analytical rationale，再给出 chunk-level verdict。其标签通过 Monte Carlo rollout 比较 chunk 前后价值变化自动构造，因此 evaluator 学到的不是简单分类边界，而是对 reasoning 片段质量的文本化诊断。

- [Aky23] RL4F: Generating Natural Language Feedback with Reinforcement Learning for Repairing Model Outputs  
  RL4F 训练一个 critique generator 输出自然语言反馈，而非标量 reward，并用“反馈是否帮助固定模型修复输出”作为 PPO 奖励。它展示了 diagnostic evaluator 可以直接面向 repair usefulness 优化，而不必退化为 reward scoring。


## Tokenized-to-Policy Experience Transformation

### Imitation-based Policy Internalization

- [Pat24] Large Language Models Can Self-Improve At Web Agent Tasks  
  该工作让 web agent 在真实网页环境中自生成交互轨迹，再结合环境报错与 self-critique 过滤出 plausible trajectories，并进一步合成域外网页任务与解法轨迹，最终用自回归 SFT 将这些经验内化到 policy 参数中。其核心不是 RL，而是把环境反馈当作数据筛选器，用 filtered synthetic trajectories 驱动 supervised self-improvement。

- [Lai25d] AndroidGen: Building an Android Language Agent under Data Scarcity  
  AndroidGen 面向移动端 data scarcity，利用 GPT-4o 在 AndroidWorld 中生成操作轨迹，并通过 StepCritic 将任务分解为 sub-goals，对轨迹做细粒度完成度评估与筛选，再配合 trajectory augmentation 扩充高质量示范。最终训练仍以 LoRA-SFT 为主，本质上是把筛选后的 Android interaction trajectories 作为 behavior cloning 数据来内化 agent policy。

- [Pap25b] AppVLM: A Lightweight Vision Language Model for Online App Control  
  AppVLM 先在 AndroidControl 的人类示范上做 SFT，再让轻量级 VLM 在 AndroidWorld 中在线探索，只保留成功轨迹并继续用 SFT loss 迭代更新模型。虽然作者称之为 Reinforce Fine-Tuning，但全文明确区分它与 policy-gradient RL，实质是基于 rejection sampling 的 iterative imitation。

- [Pah25] Explorer: Scaling Exploration-driven Web Trajectory Synthesis for Multimodal Web Agents  
  Explorer 用 GPT-4o 驱动多智能体式的数据合成流水线，在真实网页中通过 task proposing、task refinement、task summarization 与 task verification 生成并筛选大规模成功轨迹。学生模型随后在这些 synthesized web trajectories 上做监督微调，因此经验转化的关键是 exploration-driven data construction followed by SFT，而非在线 reward optimization。

- [Gan25b] Go-Browse: Training Web Agents with Structured Exploration  
  Go-Browse 将网页探索组织成带 URL frontier 的 structured exploration，通过任务提议、可行性检查和成功轨迹采样来系统收集 grounded demonstrations。其 policy 训练阶段直接在 success trajectories 上进行 SFT，反馈信号主要负责判定哪些轨迹值得进入模仿学习数据集。

- [Hu25i] WebCoT: Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback  
  WebCoT 将 reflection、branching 与 rollback 过程中隐含的推理经验重构为显式 Chain-of-Thought，把原本推理时的搜索与恢复机制压缩成可学习的 reasoning traces。随后模型通过 cumulative SFT 同时模仿 thought 和 action，从而把 web navigation 中的高阶推理模式直接内化到 backbone policy。

- [Zen23d] AgentTuning: Enabling Generalized Agent Abilities for LLMs  
  AgentTuning 从 WebShop、Mind2Web、ALFWorld、数据库和操作系统等多类 agent 环境中收集 GPT-4 成功交互轨迹，并统一转换成多轮对话式的 thought-action training samples。该方法用混合 instruction tuning 将 agent trajectories 与通用指令数据联合训练，使模型把跨环境的 tool use、planning 与 action formatting 经验直接吸收到参数中。

- [Xu24] AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials  
  AgentTrek 先从互联网上抽取 web tutorials，将其结构化为可执行的 step-by-step instructions，再让 VLM agent 在真实浏览器环境中做 guided replay，生成并验证高质量 demonstrations。最终模型在这些 tutorial-guided trajectories 上进行 SFT，因此其核心是由外部教程与环境交互共同构造 imitation data，再完成 policy internalization。

- [Mur24b] NNetNav: Unsupervised Learning of Browser Agents Through Environment Interaction in the Wild  
  NNetNav 先让 browser agent 在真实网站中进行无目标探索，再对交互轨迹做 hindsight relabeling，将状态变化反标为可执行 instruction，并重写与之对齐的动作序列。最后通过 supervised fine-tuning 在这些 synthetic demonstrations 上训练 policy，环境反馈主要用于轨迹标注与剪枝，而非直接进入 RL 优化目标。

- [Pan24] Training Software Engineering Agents and Verifiers with SWE-Gym  
  SWE-Gym 从可执行的软件工程环境中采样 agent trajectories，并利用 unit-test feedback 过滤出成功的代码修改与工具使用过程，再通过 rejection-sampling fine-tuning 更新 actor。尽管论文同时训练 verifier，但 actor 的经验内化机制本质上仍是 filtered behavior cloning，即将成功的 software engineering trajectories 直接转化为 policy weights。


### Reward-based Policy Internalization

#### Web, tool, SQL, SWE

| 论文 | 可用于正文的 1到2 句描述 |
|---|---|
| Training Long-Context, Multi-Turn Software Engineering Agents with Reinforcement Learning [Gol25] | 该工作面向长上下文、多轮 Software Engineering agent，先用通过 unit test 的成功轨迹做 RFT 热启动，再用 DAPO 做在线 RL。其核心奖励直接来自可执行环境中的 test pass/fail 与长度惩罚，因此把代码编辑与交互经验直接内化为 policy weights。 |
| WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning [Wei25] | 该工作将 WebArena 中的多轮网页交互建模为端到端 RL，使用 M-GRPO 在同一任务上并行采样多条 browser trajectories。奖励完全由 URL match、string match 和 Playwright-based program verification 给出，是典型的 outcome-level verifiable reward 优化。 |
| Agentic Reinforced Policy Optimization [Don25d] | 该论文提出 ARPO，在 multi-turn tool-use agent 中用 entropy-based adaptive rollout 在高不确定性步骤触发分支采样，再用 advantage attribution estimation 做细粒度 credit assignment。奖励由答案正确性、格式约束和多工具协同使用的规则项构成，不依赖训练出的 judge。 |
| Information Gain-based Policy Optimization [Wan25y] | 该方法在最终 outcome reward 之外，引入 turn-level Information Gain 作为 intrinsic reward，用每一轮观测对正确答案 log-prob 的增量来缓解长程 credit assignment。它本质上是在 GRPO 框架里把 search interaction 的信息价值直接变成 policy update 信号。 |
| ToolRL: Reward is All Tool Learning Needs [Qia25b] | 该工作把 tool-use 训练表述为纯 reward-driven 的 GRPO 学习问题，奖励由 format 合法性与 tool name、parameter name、parameter content 的细粒度匹配组成。它强调无需依赖大规模 SFT 轨迹，仅凭可验证工具调用奖励即可内化工具使用能力。 |
| SQL-Trail: Multi-Turn Reinforcement Learning with Interleaved Feedback for Text-to-SQL [Hua26d] | 该论文让 agent 在数据库环境中进行多轮 reason-execute-observe 交互，并以 SQL execution correctness 为核心奖励，同时辅以 syntax、schema grounding、turn budget 等 shaping 项。方法上采用改进的 GRPO 与 adaptive turn-budget，使 Text-to-SQL 的离散交互经验直接沉淀进 policy。 |
| SQL-ASTRA: Alleviating Sparse Feedback in Agentic SQL via Column-Set Matching and Trajectory Aggregation [Li26r] | 该工作针对 agentic SQL 的极稀疏执行反馈，设计了 step-level Column-Set Matching Reward 和 trajectory-level Aggregated Trajectory Reward。它用 GRPO 将多轮数据库交互中的局部结构正确性与全局执行正确性一并转成 policy 学习信号。 |
| Reinforcement Learning for Long-Horizon Interactive LLM Agents [Che25af] | 该论文提出 LOOP，在 AppWorld 这类 stateful multi-app 环境中，用 leave-one-out PPO 训练能执行长程 API 交互的 LLM agents。奖励来自最终单元测试通过比例，且通过多 rollout 的 leave-one-out baseline 避免额外 critic。 |
| AgentRL: Scaling Agentic Reinforcement Learning with a Multi-Turn, Multi-Task Framework [Zha25ag] | 该工作更像一个面向 agent RL 的系统化训练框架，把多任务、多环境的 verifiable reward 统一到异步 rollout-training pipeline 中。其关键贡献是 cross-policy sampling 与 task advantage normalization，使多轮、多任务 agent experience 能稳定转化为共享 policy 参数。 |
| AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning [Xi25c] | 该论文提出 AgentGym-RL 和 ScalingInter-RL，从短 horizon 逐步扩展到长 horizon，以 curriculum 方式训练多轮 LLM agents。奖励直接来自环境 outcome reward，重点不是 reward 设计本身，而是让长程交互经验能被更稳定地吸收到 policy 中。 |
| Q-SFT: Q-Learning for Language Models via Supervised Fine-Tuning [Hon24] | 该工作将 offline RL 改写成 weighted SFT 目标，用 Bellman backup 产生的权重直接调节 action token 的交叉熵损失。虽然形式上接近 supervised fine-tuning，但其训练信号本质上来自环境 reward 与未来回报估计，因此仍属于 reward-grounded policy internalization。 |
| RLVMR: Reinforcement Learning with Verifiable Meta-Reasoning Rewards for Robust Long-Horizon Agents [Zha25ao] | 该论文显式奖励 `<planning>`, `<explore>`, `<reflection>` 等 meta-reasoning 行为，只要这些行为可由轨迹结果与状态变化规则验证，就给予 dense process reward。它将长程 agent 经验中“哪些思维动作值得强化”编码成可验证的 step-level reward，再用 GRPO-MR 更新 policy。 |

#### GUI 与 computer-use

| 论文 | 可用于正文的 1到2 句描述 |
|---|---|
| GUI-R1: A Generalist R1-Style Vision-Language Action Model For GUI Agents [Luo25b] | 该工作把 GUI action prediction 写成 R1-style reinforcement fine-tuning，采用 GRPO 在 unified action space 上优化 `<think> + action` 输出。奖励完全由格式合法性、action type 匹配、点击点落框和输入文本语义匹配等规则化信号构成。 |
| AgentCPM-GUI: Building Mobile-Use Agents with Reinforcement Fine-Tuning [Zha25an] | 该论文在感知预训练和 SFT 之后，引入基于 GRPO 的 Reinforcement Fine-Tuning 来提升 mobile GUI agent 的 reasoning 与 action selection。其奖励来自 JSON 格式检查、语义正确性和点击坐标是否落入 ground-truth box 等可验证规则。 |
| UI-S1: Advancing GUI Automation via Semi-online Reinforcement Learning [Lu25j] | 该方法提出 semi-online RL，在离线 GUI 轨迹上模拟在线 rollout，使模型在自己的历史上继续决策而非总跟随专家轨迹。它用 step-level 与 episode-level advantage 联合优化 policy，奖励来自动作类型、格式和 exact action match 等非参数化信号。 |
| ARPO: End-to-End Policy Optimization for GUI Agents with Experience Replay [Lu25f] | 该工作面向 OSWorld 中的长程 GUI 任务，将 GRPO 与 successful trajectory replay buffer 结合，在全失败时注入历史正样本避免梯度消失。奖励由任务成功与 action format penalty 直接定义，是 replay-enhanced reward-based internalization 的代表。 |
| Generalization in Online Reinforcement Learning for Mobile Agents [Gu26b] | 该论文在 AndroidWorld-Generalization 中系统研究 mobile agent 的在线 RL 泛化问题，训练信号就是 terminal success/failure 的稀疏二元奖励。其贡献更偏训练系统与泛化设定，但本质仍是把在线 GUI 交互经验通过 GRPO 吸收到 policy 中。 |
| Succeed or Learn Slowly: Sample Efficient Off-Policy Reinforcement Learning for Mobile App Control [Pap25c] | 该工作提出 SoLS 和 Successful Transition Replay，在 AndroidWorld 上对成功样本做更激进的更新、对失败样本做更保守的正则化更新。它通过 off-policy replay 提升移动端 GUI 控制中的样本效率，是 reward-based off-policy assimilation 的典型例子。 |

#### Embodied 与 VLA

| 论文 | 可用于正文的 1到2 句描述 |
|---|---|
| Improving Vision-Language-Action Model with Online Reinforcement Learning [Guo25d] | 该论文提出 iRe-VLA，在 RL 阶段仅更新 action head 用稀疏 binary success reward 做在线探索，再把发现的成功轨迹回流到 supervised stage 进行全模型 LoRA 微调。其核心思想是用 environment success signal 驱动大 VLA 模型稳定吸收新经验。 |
| SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning [Li25aa] | 该工作将 VLA 训练扩展到真正的在线交互 setting，用 outcome-level binary reward 和 critic-free GRPO 直接优化 action token。它还结合 dynamic sampling、高温采样和更宽的 clipping 区间，鼓励机器人发现示范数据外的新策略。 |
| Fine-Tuning Large Vision-Language Models as Decision-Making Agents via Reinforcement Learning [Zha24s] | 该论文较早展示了可将全参数 VLM 直接当作决策 policy，用 PPO 在 ALFWorld、Blackjack 和视觉推理环境中基于环境奖励进行微调。其关键技术点是把 CoT 与 action 解耦计分，避免长 reasoning token 淹没真正的 action learning signal。 |
| LongNav-R1: Horizon-Adaptive Multi-Turn RL for Long-Horizon VLA Navigation [Hu26e] | 该工作把 embodied navigation 重写为 multi-turn VLA 对话，并提出 HAPO，用基于时间核回归的非参数 baseline 做 horizon-adaptive advantage estimation。奖励来自 geodesic distance 改善和 SPL 等环境指标，因此非常符合 long-horizon reward-based internalization。 |
| Large Language Models as Generalizable Policies for Embodied Tasks [Szo23] | 该论文将冻结的 LLaMA 接成具身 policy，用 DD-PPO 在 Habitat rearrangement 任务上基于 success、subgoal、invalid action penalty 等环境奖励训练 action head。它代表了把语言模型直接当作 embodied policy 并用 RL 内化交互经验的早期路线。 |
| Grounding Large Language Models in Interactive Environments with Online Reinforcement Learning [Car23] | 该工作提出 GLAM，在 BabyAI-Text 中用 PPO 对 FLAN-T5 做在线 RL，使其从文本观测中学会 grounded action selection。奖励仅由任务完成与步数惩罚给出，是较早的 “LLM as policy” 在线 grounded RL 代表。 |

#### 通用 RL 优化与 credit assignment 方法

| 论文 | 可用于正文的 1到2 句描述 |
|---|---|
| EPO: Entropy-regularized Policy Optimization for LLM Agents Reinforcement Learning [Xu25k] | 该论文关注长程 multi-turn agent RL 中的 exploration-exploitation cascade failure，在 PPO 或 GRPO 外层加入 trajectory-level entropy regularization 与 entropy smoothing。它不改变 reward 来源，而是通过熵约束让稀疏 outcome reward 更稳定地塑造 policy。 |
| Agentic Entropy-Balanced Policy Optimization [Don25c] | 该工作提出 AEPO，用 entropy pre-monitoring 做 tree-structured rollout 分配，并在更新阶段用 entropy-aware advantage estimation 防止高熵 token 的梯度被过度裁剪。方法仍基于 outcome reward，但将不确定性显式纳入多轮 agent 的 policy optimization。 |
| Harnessing Uncertainty: Entropy-Modulated Policy Gradients for Long-Horizon LLM Agents [Wan25ad] | 该方法在全局 trajectory reward 上叠加基于 step entropy 的梯度调制和 Future Clarity Bonus，从而把“高不确定度步骤”的探索价值显式纳入 advantage。它本质上是在 sparse reward setting 下做 uncertainty-shaped credit redistribution。 |
| Group-in-Group Policy Optimization for LLM Agent Training [Fen25c] | 该论文提出 GiGPO，通过 anchor state grouping 在同一初始任务下比较不同轨迹中到达相同状态后的动作优劣，从而同时构造 episode-level 与 step-level 相对优势。其核心不是新 reward，而是把同一批 rollout 内部的状态对齐用于更精确的 long-horizon credit assignment。 |
| Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs [Li25ae] | 该工作把 multi-turn LLM interaction 明确建模为 turn-level MDP，把整段回复视为一个 action，并用可学习 critic 做 turn-level GAE。相比 token-level PPO 或 trajectory-level GRPO，它更直接地把环境反馈归因到回合级决策单元。 |



| 标题 | 可用于正文的 1到2 句描述 |
|---|---|
| ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL [Zho24f] | ArCHer 将 multi-turn language agent 训练拆成两个层次：高层在 utterance level 上学习价值函数，低层在 token level 上用 policy gradient 学习具体生成策略，从而缓解长程交互中的奖励传播困难。其关键点是把环境返回的外部任务奖励先汇聚为回合级决策信号，再把这些信号传递给底层 token policy，使多轮语言动作能够被更稳定地内化进 policy weights。 |
| WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning [Wei25] | WebAgent-R1 将网页交互过程直接作为 end-to-end multi-turn RL 问题来训练，使用 M-GRPO 对同一 web task 并行采样多条 browser trajectories，并以相对优势更新 policy。奖励完全由 URL match、string match 和 Playwright-based program verification 给出，因此它学习的不是对示范网页轨迹的模仿，而是对“哪些网页操作最终在环境里可验证地成功”的直接内化。 |
| Training Long-Context, Multi-Turn Software Engineering Agents with Reinforcement Learning [Gol25] | 该工作面向长上下文的 Software Engineering agent，先用能通过测试的成功轨迹做 Rejection Fine-Tuning 热启动，再用 DAPO 在真实软件环境中继续做在线优化。其 reward 直接来自 unit test pass or fail 与 trajectory length penalty，因此模型学习的是如何在多轮代码编辑、工具调用和环境观察中形成真正可执行的修复策略，而不是仅复述已有 patch pattern。 |
| Agentic Reinforced Policy Optimization [Don25d] | ARPO 针对 multi-turn tool-use agent 中 reward 稀疏且 credit assignment 粗糙的问题，在高不确定性步骤触发 entropy-based adaptive rollout，对局部分支做额外探索。随后它用 advantage attribution estimation 区分共享前缀与分支后动作的贡献，将 correctness、format 和 multi-tool collaboration 的规则奖励更细粒度地分配到具体决策步骤上。 |
| Information Gain-based Policy Optimization: A Simple and Effective Approach for Multi-Turn LLM Agents [Wan25y] | IGPO 在最终 outcome reward 之外，引入 turn-level Information Gain reward，用每一轮交互后正确答案 log-prob 的增量来衡量该轮观察是否真正带来了信息。这样，search agent 不再只在轨迹结束后收到一次成败信号，而是能把“哪一次查询、哪一次观察真正推进了解题”直接转化为 policy update。 |
| ToolRL: Reward is All Tool Learning Needs [Qia25b] | ToolRL 将 tool-integrated reasoning 直接表述为 reward-driven policy optimization，而不是先依赖大量工具调用示范做 SFT。它把奖励细化为 format correctness 以及 tool name、parameter name、parameter content 的层级匹配分数，再用 GRPO 让模型从环境可验证的工具调用结果中内化工具选择与参数配置能力。 |
| SQL-Trail: Multi-Turn Reinforcement Learning with Interleaved Feedback for Text-to-SQL [Hua26d] | SQL-Trail 让 agent 在数据库环境中反复执行 “reason–execute–observe” 循环，通过执行结果、报错信息和中间观察逐步修正 SQL，而不是一次性生成最终查询。其训练信号以 final execution correctness 为核心，并叠加 syntax validity、schema grounding 和 turn-budget shaping，使 policy 学到的是多轮数据库交互中的可执行推理策略。 |
| SQL-ASTRA: Alleviating Sparse Feedback in Agentic SQL via Column-Set Matching and Trajectory Aggregation [Li26r] | SQL-ASTRA 针对 agentic SQL 场景中“只有最终执行对错”的极稀疏反馈，设计了 step-level Column-Set Matching Reward，从中间执行结果中提取局部结构正确性。进一步地，它用 Aggregated Trajectory Reward 将多轮交互中的改进与退化统一聚合成轨迹级训练信号，从而让 policy 不只学习最终答对，还学习沿途哪些修正方向是有效的。 |
| Reinforcement Learning for Long-Horizon Interactive LLM Agents [Che25af] | 该工作在 AppWorld 这类 stateful、多应用、多 API 的真实交互环境中训练长程 LLM agents，并提出 LOOP 以多 rollout 的 leave-one-out advantage 代替显式 critic。奖励由任务结束时 unit tests 的通过比例直接给出，因此模型内化的是长链 API 调用、代码执行与状态更新中哪些行为组合真正能够完成任务。 |
| AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning [Xi25c] | AgentGym-RL 提出一个统一的 multi-turn RL 训练框架，并通过 ScalingInter-RL 从短 horizon 逐步过渡到长 horizon，让 agent 先学会基础交互，再学习更深层的探索与规划。它的核心价值不在于特定 reward engineering，而在于展示了如何把环境 outcome reward 与逐步扩展的交互长度结合起来，稳定地把长程决策经验沉淀进通用 agent policy。 |
| EPO: Entropy-regularized Policy Optimization for LLM Agents Reinforcement Learning [Xu25k] | EPO 针对 multi-turn LLM agent 在稀疏奖励下容易出现的 exploration-exploitation cascade failure，在 PPO 或 GRPO 外层加入 trajectory-level entropy regularization 与 entropy smoothing。它并不改变 reward 来源，而是通过约束长轨迹训练中的熵演化，让 outcome reward 更稳定地塑造 policy，避免 agent 过早坍缩到低探索、低回报的局部策略。 |
| Group-in-Group Policy Optimization for LLM Agent Training [Fen25c] | GiGPO 观察到，长程 agent 任务里仅按整条轨迹成败来归因过于粗糙，于是提出 anchor state grouping，把不同 rollout 中到达相同环境状态的动作放在一起比较。这样它同时构造 episode-level 与 step-level relative advantage，在不依赖额外 critic 的前提下，把环境奖励更精确地分配到关键中间决策。 |
| Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs [Li25ae] | Turn-PPO 明确把 multi-turn interaction 建模为 turn-level MDP，将整段回复而非单个 token 视为一个 action，再用 critic 在回合粒度上做 GAE。相比 token-level PPO 或 trajectory-level GRPO，这种做法更贴合 agent 的真实决策单位，因此能把环境反馈更稳地对齐到每一轮 reasoning 或 tool-use 决策。 |

### Preference-based Policy Internalization

可以，下面这版更接近可直接放进综述正文的表述。

| 标题 | 可用于正文的 1 到 2 句描述 |
|---|---|
| Direct Multi-Turn Preference Optimization for Language Agents [Shi24c] | [Shi24c] 面向 language agent 的多轮交互场景，将 DPO 从单轮 response preference 扩展到 multi-turn trajectory preference，并通过引入 state-action occupancy measure 与 length normalization，解决长轨迹下 preference objective 难以直接成立的问题。该方法通常以 expert trajectory 为 preferred sample、以模型生成的较差轨迹为 dispreferred sample，将轨迹级相对优劣直接内化到 policy weights 中。 |
| Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents [Son24] | [Son24] 提出 Exploration-based Trajectory Optimization，先用 expert trajectory 对 agent 做 behavior cloning，再让当前 policy 在环境中主动探索，把成功示范与探索过程中产生的失败 trajectory 组成 preference pairs，并用 DPO 持续更新 policy。其关键点在于不丢弃 failed experience，而是把失败轨迹显式转化为 negative supervision，使模型同时学会复现正确行为与规避错误决策路径。 |
| Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards [Da25] | [Da25] 针对 software engineering agent 中奖励稀疏的问题，引入 guidance 机制帮助模型探索更可能成功的代码修复轨迹，再依据 unit tests 的 pass fail 结果，把通过测试与未通过测试的 trajectory 组织成 preference pairs，并通过 DPO 完成 policy update。该方法的核心不是直接做高方差在线 RL，而是把 verifiable environment feedback 压缩为离散的相对偏好信号，从而将修复经验稳定地内化到 actor parameters。 |
| Advancing Tool-Augmented Large Language Models: Integrating Insights from Errors in Inference Trees [Che24k] | [Che24k] 从 tool-use agent 的 inference tree 中系统挖掘原本被忽略的失败分支，将成功路径上的关键步骤与同层失败兄弟节点配对，构造成 step-level preference data，并在成功轨迹 SFT 之后进一步使用 DPO 优化 policy。该方法的关键贡献是把 tree search 中的 error path 转化为可学习的 negative preference，使模型不仅模仿正确工具调用流程，也学会避免无效 API 调用与错误推理分支。 |
| Solving the Granularity Mismatch: Hierarchical Preference Learning for Long-Horizon LLM Agents [Gao25c] | [Gao25c] 指出长程 agent 中 trajectory-level preference 过粗、step-level preference 又过细，提出 Hierarchical Preference Learning，同时结合 trajectory-level、group-level 与 step-level 三种粒度的 DPO 信号来训练 policy。其核心做法是先将 expert trajectory 划分为语义连贯的 action groups，再为这些局部子任务构造 preferred dispreferred 对比样本，并配合双层 curriculum 逐步学习，从而改善长程任务中的 credit assignment。 |
| WEPO: Web Element Preference Optimization for LLM-based Web Navigation [Liu25z] | [Liu25z] 面向 web navigation 中元素定位困难的问题，提出 Web Element Preference Optimization，将 ground-truth action 作为 preferred sample，并基于 DOM tree 结构用启发式规则采样非目标元素构造 dispreferred actions，再通过 DPO 微调 policy。与完整 trajectory preference 不同，该方法把偏好学习聚焦到 action candidate 尤其是 web element selection 层面，使模型在复杂页面中更好地区分目标控件与干扰元素。 |


## Parametric Evaluator-to-Policy Transformation

### Outcome Feedback-to-Policy Transfer

| 标题 | 可用于正文的 1到2 句描述 |
| --- | --- |
| Constitutional AI: Harmlessness from AI Feedback [Bai22b] | 该文提出 Constitutional AI，将一组自然语言 constitution principles 用于引导 AI model 对成对完整 responses 进行偏好判断，并用这些 AI preferences 训练 preference model。随后 policy 通过 RLAIF 针对该参数化 preference model 做强化学习，从而把 evaluator 所体现的 harmlessness criterion 持久迁移到 policy 权重中。 |
| RLAIF vs. RLHF: Scaling Reinforcement Learning from Human Feedback with AI Feedback [Lee23b] | 该文系统比较了 RLHF 与 RLAIF，核心做法是用 off-the-shelf LLM 对完整输出给出 outcome-level 评分或偏好，再将该信号转成 reward model 或直接作为 RL reward 来更新 policy。特别是 d-RLAIF 版本绕过了单独 reward model 训练，直接把 LLM judge 的整体质量判断蒸馏为 policy 的生成偏好。 |
| Direct Language Model Alignment from Online AI Feedback [Guo24] | 该文提出 OAIF，让 LLM annotator 在线比较当前 policy 生成的两个完整 responses，并实时构造 chosen-rejected preference pairs。与离线 preference optimization 不同，它直接在 on-policy 分布上用 DPO、IPO 或 SLiC 更新 policy，从而把 evaluator 的 outcome-level 偏好持续吸收到模型参数中。 |
| Self-Rewarding Language Models [Yua24] | 该文让同一模型同时承担 generator 和 judge 两种角色：模型先为同一指令生成多个完整候选答案，再以 LLM-as-a-Judge 方式对这些 outcomes 打分，并选出高分与低分样本构造偏好对。通过 iterative DPO，模型把自身 evaluator 所表达的 response-level quality judgment 反复蒸馏回 policy，形成生成与评估能力共同提升的自奖励循环。 |
| RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment [Don23] | 该文提出 Reward-Ranked FineTuning，不用 PPO，而是先从当前 policy 采样多个完整候选输出，再用 reward model 对它们做 outcome-level 排序，只保留最高分样本进行 SFT。其关键思想是把 evaluator 的整体偏好先转成 filtered distillation data，再以监督微调的方式写入 policy 参数。 |
| BOND: Aligning LLMs with Best-of-N Distillation [Ses24] | 该文关注如何把推理时的 Best-of-N sampling 效果蒸馏为单次采样 policy：reward model 先定义完整输出上的 BoN 偏好分布，再通过结合 forward KL 与 backward KL 的 Jeffreys divergence 进行分布匹配。这样，policy 学到的是 evaluator 支持的 outcome-level selection behavior，而不再依赖测试时反复采样和重排序。 |
| BoNBoN Alignment for Large Language Models and the Sweetness of Best-of-n Sampling [Gui24] | 该文从理论上刻画了 Best-of-n 分布的最优性，并据此把 reward-model-guided 的 outcome selection 转化为可训练目标。具体做法结合对最佳样本的 SFT-BoN 与利用最好样本和最差样本的 IPO-BoN，对 policy 进行参数更新，使其在单次生成时逼近 evaluator 所偏好的 BoN 行为。 |
| Meta-Rewarding Language Models: Self-Improving Alignment with LLM-as-a-Meta-Judge [Wu24d] | 该文构建了 actor、judge、meta-judge 三位一体的自进化框架：judge 对完整 responses 给出 rubric-based outcome scores，meta-judge 再评估 judge 的判断质量，并把这些结果转化为新的 preference data。policy 通过 DPO 吸收高质量 judge 信号，而 judge 本身也在迭代中被更新，因此形成了 outcome feedback transfer 与 evaluator co-improvement 同时发生的闭环。 |
| Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards [Ack26] | 该文研究 RLHF 与 RLVR 中 outcome-level proxy reward 驱动的 policy 更新为何会产生 reward hacking，并指出问题在于 policy 对 evaluator 奖励地形中尖锐高点的过度利用。方法上它在 REINFORCE 或 GRPO 更新中加入 gradient regularization，使 policy 更倾向于落在平坦且更稳健的高奖励区域，因此更像 evaluator-to-policy transfer 的稳定化机制。 |
| Reinforcement Learning from Meta-Evaluation: Aligning Language Models Without Ground-Truth Labels [Ren26b] | 该文让一个或多个 LLM evaluator 针对完整 response 回答 meta-questions，并把 evaluator 对目标答案如 “YES” 的 log-prob 聚合成 scalar reward。该 reward 再通过 CISPO 这一类 GRPO 变体更新 policy，从而把 evaluator 的整体判断能力直接转化为无需 ground-truth labels 的 outcome-level policy learning signal。 |
| Policy Filtration for RLHF to Mitigate Noise in Reward Models [She24c] | 该文保留了标准 RLHF 的基本结构，即先由训练好的 reward model 对完整 response 打 outcome-level 分数，再通过 PPO 更新 policy。它的关键创新是 policy filtration，只让 reward model 最可靠的高分或低分样本进入训练缓冲区，以减少 noisy evaluator 对 policy transfer 的误导。 |
| Reward Model Routing in Alignment [Wu25x] | 该文不依赖单一 reward model，而是维护一个由多个 trained reward models 组成的 evaluator pool，并用 Bayesian router 为每个 query 动态选择最合适的 reward source。被选中的 evaluator 对完整候选回答给出 pairwise preference，随后这些 chosen-rejected pairs 被送入 online DPO，从而把多种 evaluator 的 outcome preference 有选择地蒸馏进 policy。 |
| The Perfect Blend: Redefining RLHF with Mixture of Judges [Xu24d] | 该文提出 Mixture of Judges 框架，对完整生成结果施加 outcome-level 约束判断，并将 satisfied 或 violated 的 judge outputs 注入 CRPG、CODPO 和 CRRAFT 等不同 policy optimization 接口。其核心不是单一 reward maximization，而是让多种 judges 共同决定哪些完整行为可被 policy 持久吸收。 |
| Robust Preference Optimization through Reward Model Distillation [Fis24] | 该文先显式训练 reward model，再把 reward model 对候选输出对的 reward difference 直接 distill 到 policy 的隐式 reward 表示中，而不是只用离散 preference labels 做普通 DPO。进一步地，pessimistic distillation 通过 reward model family 的最坏情况目标与 KL regularization 提高鲁棒性，使 policy 学到的是 evaluator 更稳健的整体偏好结构。 |
| DPO Learning with LLMs-Judge Signal for Computer Use Agents [Luo25f] | 该文在 computer-use 场景中使用 prompted GPT-4o 对完整候选操作结果打 0 到 100 分，再把这些 outcome scores 组装成 ground-truth vs model 和 model vs model 的 preference pairs，对 UI-TARS-2B 做 DPO。其关键点在于 judge 只在训练阶段提供整体质量判断，而这些判断最终被吸收到 agent policy 权重中，使推理时无需再调用 evaluator。 |

### Process Feedback-to-Policy Transfer


| 标题 | 可用于正文的 1到2 句描述 |
|---|---|
| [Din25b] FAPO: Flawed-Aware Policy Optimization for Efficient and Reliable Reasoning | 该文先训练一个 generative reward model 来识别 answer-correct but process-flawed 的推理轨迹，并定位 first incorrect step；再把这种 flawed-positive diagnosis 转化为写入 GRPO 的动态 penalty，使 policy 不仅追求最终答案正确，也逐步压制“结果对但过程错”的中间推理模式。其关键点在于把 evaluator 的过程级错误定位能力转成 policy update 中的 advantage shaping，从而提升 reasoning reliability。 |
| [Zho25p] SWEET-RL: Training Multi-Turn LLM Agents on Collaborative Reasoning Tasks | 该文针对 multi-turn collaborative reasoning agent，训练一个 turn-level critic，并在训练 critic 时引入 actor 在推理时看不到的 privileged information，以直接学习每轮 action 的 advantage。随后它用该 critic 对每轮候选动作进行排序，构造 chosen and rejected action pairs，再通过 DPO 把这种 turn-wise credit assignment 蒸馏进 policy 参数。 |
| [Che25v] Stepwise Guided Policy Optimization: Coloring Your Incorrect Reasoning in GRPO | 该文引入一个 step-wise judge 顺序检查 reasoning trajectory，定位 first incorrect step，并把“正确前缀长度占整条轨迹的比例”定义为 Reasoning Trajectory Score。该分数替代了 GRPO 对错误样本统一给 0 的做法，使 all-negative groups 内部也能形成可学习的差异化优势信号，从而让 policy 学到“哪一段推理更接近正确解”。 |
| [Cha24b] Dense Reward for Free in Reinforcement Learning from Human Feedback | 该文并不额外构造 process labels，而是从已训练 Transformer reward model 的最终评分过程中提取 attention-based credit attribution，把原本只在序列末端产生的 scalar reward 自动分解为 token-level dense rewards。随后这些 dense process signals 被直接送入 PPO 式 RLHF 更新，使 reward model 中隐含的局部评价能力持续吸收到 policy 参数中，并显著缓解长序列训练中的 credit assignment 问题。 |
| [Wan26ac] Enhancing LLM-based Search Agents via Contribution Weighted Group Relative Policy Optimization | 该文面向 search agent 的多轮轨迹，用 LLM judge 按 retrieval utility 与 reasoning correctness 对每一轮进行评价，并将结果归一化为 round-level contribution weights。训练时这些权重不直接充当 reward，而是用于重分配 trajectory-level GRPO advantage，使 policy 更强地强化真正推进最终成功的关键搜索轮次与中间推理步骤。 |
| [Xu25h] Hybrid Reward Normalization for Process-supervised Non-verifiable Agentic Tasks | 该文针对 non-verifiable 的 multi-turn agent task，引入一个 principle-based process reward model，对每个 turn 的 correctness、relevance 与 coherence 给出过程分数。随后它通过 ReNorm 将 step-level process reward 与 sparse outcome reward 统一校准后送入 GAE 和 PPO，使 policy 能从长程 search trajectory 的中间行为中获得稳定而细粒度的学习信号。 |
| [Wan26s] Building Autonomous GUI Navigation via Agentic-Q Estimation and Step-Wise Policy Optimization | 该文先训练一个 Agentic-Q evaluator，对 GUI 环境中的 state-action pair 估计 future return，把原本稀疏的任务成败信号转化为 step-wise value feedback。之后在 Step-Wise Policy Optimization 中，policy 在每一步采样候选动作并由 Agentic-Q 打分，再将这些局部价值信号接入 GRPO、RLOO 或 REINFORCE++ 式更新，从而把 evaluator 的局部判断能力吸收到 GUI agent 的参数中。 |
| [Li26p] OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards | 该文将长程 GUI trajectory 分解为一系列 milestones，并通过 selector、verifier、reviewer 与 judge 组成的 critic framework 对中间进展进行逐步验证与校准。训练时，这些 milestone-level process judgments 被汇总成 online RL 的 reward signal，用于 GRPO 更新 policy，使 agent 学到的不只是最终是否完成任务，还包括哪些中间 GUI 操作真正推进了任务状态。 |


### Diagnostic Feedback-to-Policy Transfer

| 标题 | 匹配程度 | 可用于正文的 1到2 句描述 |
|---|---|---|
| [Zha26am] SRR-Judge: Step-Level Rating and Refinement for Enhancing Search-Integrated Reasoning in Search Agents | 强匹配 | SRR-Judge 面向 search-integrated reasoning agent，对每个 thought-action step 同时生成 step-level rating、错误解释以及 refined thought 和 refined action，并据此把低质量搜索推理轨迹改写为可训练的高质量版本。其核心训练接口是将这些带有诊断与修正信息的 refined trajectories 经过质量过滤后用于多轮 rejection-sampling fine-tuning，使 policy 内化“哪里错了以及应如何改”的 step-wise search behavior。 |
| [Hon25c] Natural Language Actor-Critic: Scalable Off-Policy Learning in Language Space | 强匹配 | Natural Language Actor-Critic 用 language successor model 预测某个动作后的未来 rollout 摘要，再由 language evaluator 基于这些 future summaries 生成带理由的 textual critique 和 optimality judgment，而不是只输出 scalar value。随后 refinement policy 依据这类语言化诊断生成改进动作，并将其蒸馏回基础 policy，因此 critic 的评估能力是以自然语言解释与修正建议的形式被持久写入 actor 参数。 |
| [Wan26ad] OpenClaw-RL: Train Any Agent Simply by Talking | 强匹配 | OpenClaw-RL 从真实交互产生的 next-state signal 中抽取 concise hindsight hints，将环境回应中的纠错信息转化为 action directive 和 correction-oriented textual feedback，而不是仅压缩成二值 reward。其提出的 Hindsight-Guided On-Policy Distillation 用“带 hint 的 teacher 分布”与“原始 student 分布”之间的 token-level directional advantage 更新 policy，使 conversational diagnostic feedback 直接转化为参数化行为改进。 |
| [Yua25c] Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training | 强匹配 | Agent-R 通过搜索轨迹中的分叉结构定位 failed trajectory 的 first error step，并在错误前缀与正确后续之间插入 revision signal，从而构造显式的 reflection-plus-revision training instances。模型随后以迭代 SFT 的方式学习在多轮交互中主动生成反思语句并切换到修正后的行动路径，因此 evaluator 识别出的失败原因与修正方向被直接吸收到 policy 权重中。 |
| [Fu25d] AgentRefine: Enhancing Agent Generalization through Refinement Tuning | 强匹配 | AgentRefine 构造 multi-turn error-refine trajectories，由强模型扮演的 Dungeon Master 针对 parameter error、logical error 和 location error 等失败类型给出环境式诊断信号，并展示后续 refined action。训练时模型保留错误步骤作为上下文，但仅对修正步骤计算损失，从而把“看到错误诊断后如何改正”的能力直接写入 agent policy，而不是只把失败样本筛掉。 |
| [Li26l] No More Stale Feedback: Co-Evolving Critics for Open-World Agent Learning | 强匹配 | 这篇工作训练一个 co-evolving linguistic critic，为开放世界 agent 的失败轨迹生成简短但高信息量的 natural-language critiques，明确指出行为缺陷并给出 high-level improvement guidance。actor 在这些 critique 条件下生成 refined trajectories，并通过同步的 dual-track GRPO 持续更新 actor 与 critic，因此它既是 diagnostic feedback-to-policy transfer 的强例子，也体现了 evaluator–policy co-evolution 的更强形态。 |
| [Pan24b] Autonomous Evaluation and Refinement of Digital Agents | 边界匹配 | 该工作使用 multimodal evaluator 对数字 agent 的整条轨迹或单步行为给出 success、failure、progress 等判断，并常伴随自然语言 reasoning，用于识别遗漏步骤、约束违背或状态理解错误。它一方面把这些评估结果用于 test-time reflection and retry，另一方面也用 evaluator 过滤出的高质量 state-action pairs 进行 behavior cloning 更新 policy；但参数更新阶段主要消费的是筛选标签而非完整 critique 文本，因此更适合作为 diagnostic transfer 的边界案例。 |
| [Zho24e] Policy Improvement using Language Feedback Models | 边界匹配 | 这篇工作先让强 LLM 生成 language feedback，包括 productive step 判断、helpful step 列表，以及在 LFMD 版本中进一步给出 intent summary、原因解释和 strategy advice，再把这些反馈蒸馏成一个较小的 Language Feedback Model。随后 policy 并不是直接模仿 critique 文本本身，而是利用 LFM 识别出的 desirable actions 做离线 imitation learning，因此它体现了 evaluator 诊断能力经由数据筛选间接转移到 policy 的路径。 |
| [Din26e] AdaRubric: Task-Adaptive Rubrics for LLM Agent Evaluation | 边界匹配 | AdaRubric 为不同 agent task 自动生成 task-adaptive rubrics，将轨迹按多个能力维度进行 step-wise 打分与置信度加权聚合，并用 DimensionAwareFilter 排除那些总体分数尚可但在关键维度上失败的轨迹。其后续通过 preference pair construction 配合 DPO 或 PPO 更新 policy，因此 transferred signal 的确来自 evaluator 所学的多维诊断标准，但主要进入训练的是结构化 rubric score 和 filtering outcome，而非长篇自然语言 critique。 |

## Parametric-to-Tokenized Experience Transformation

### Demonstration Externalization


## 应纳入正文

| 标题 | 匹配程度 | 可用于正文的 1到2 句描述 |
| --- | --- | --- |
| Explorer [Pah25] | 高 | Explorer 让 GPT-4o 在真实网页中以 exploration-driven 方式自主发现任务、执行多步交互，并通过 proposer, refiner, summarizer, verifier 流水线生成带截图、Accessibility Tree、动作序列与任务总结的 multimodal web trajectories。其核心贡献是把强 teacher 的网页操作能力外化为可筛选、可归档、可用于 student SFT 的 demonstration corpus。 |
| Towards Internet-Scale Training For Agents [Tra25] | 高 | InSTA 将强模型在真实互联网中的浏览、推理与操作能力外化为大规模 web trajectories 和 judge traces，形成面向 student agent 的 internet-scale training data。该方法的关键不只是自动采样任务，而是通过 judge-based filtering 只保留高质量成功轨迹，使小模型能够从 teacher 生成的 reasoning-action demonstrations 中继承网页代理能力。 |
| RAGShaper [Tao26] | 高 | RAGShaper 先构造带 distractor 的信息树与多跳问题，再诱导强 teacher 在受控检索环境中生成包含 thought, retrieval action, observation 和 final answer 的 agentic RAG trajectories。其重点是把 teacher 已内化的复杂检索、抗干扰和证据整合能力外化为可直接监督 student 的 reasoning-action data。 |
| Structured Distillation of Web Agent Capabilities Enables Generalization [Lu26] | 高 | 该工作通过 Agent-as-Annotators 框架，让 Gemini teacher 在网页环境中生成带结构化 reasoning block 的成功轨迹，并借助 evaluation hints 与 judge 过滤形成高质量 web SFT 数据。它体现了从 frontier web agent capability 到 structured tokenized demonstrations 的直接外化，而非仅生成普通问答数据。 |
| TOUCAN [Xu25o] | 高 | TOUCAN 在真实 MCP environments 中让多个强模型合成任务并执行完整的 tool-use rollouts，记录 planning、tool call、tool response 与 final answer，再通过 task-level 与 trajectory-level 双重过滤形成大规模 tool-agentic corpus。它将 teacher 的真实工具编排能力外化为高保真、多轮、可验证的训练轨迹。 |
| From Evidence to Trajectory [Li25at] | 高 | EviPath 从 gold evidence 反推 abductive reasoning path，再由强模型生成包含 planning、sub-question decomposition 与 evidence-grounded answering 的 RAG trajectories。该方法的关键在于，它不是从真实日志压缩经验，而是直接从 teacher 的参数化推理能力中读出可供 student 学习的 evidence-to-trajectory demonstrations。 |
| LLMs as Scalable, General-Purpose Simulators For Evolving Digital Agent Training [Wan25as] | 高 | 这篇工作把 GPT-4o 系模型同时用作 UI simulator 和 teacher agent，在模拟环境中生成带 state transition、reasoning thought、step summary 与 instruction wrapper 的交互轨迹，再用于训练 web 与 mobile agent。其核心不是 memory distillation，而是把强模型对数字环境动态的隐式理解外化为可训练 demonstrations。 |
| SynthAgent [Wan25ar] | 高 | SynthAgent 通过 GPT-4.1 在新网页环境中先做 element-level exploration 和 task synthesis，再在收集过程中动态修正任务、在收集后全局 refine 轨迹，最终得到更贴合目标网页分布的 synthetic supervision。它展示了如何把 teacher 的环境适应能力外化为高质量 site-specific web trajectories，并用于 student web agent 的快速适配。 |
| Fara-7B [Awa25] | 高 | Fara-7B 先用由强模型驱动的 FaraGen 生成 computer-use trajectories，再通过 alignment verifier、rubric verifier 和 multimodal verifier 三重验证筛出高质量 GUI demonstrations，用于训练紧凑型 agentic model。该方法的代表性在于，它把昂贵 closed teacher 的 computer-use competence 转化成可规模化复用的 screenshot-thought-action corpus。 |
| ToolMind Technical Report [Yan25ab] | 高 | ToolMind 通过 user agent、assistant agent 和 tool agent 的多智能体模拟，生成带 `<think>`、`<tool_call>` 与 `<tool_response>` 的多轮工具交互轨迹，并在 trajectory-level 与 turn-level 做细粒度过滤。其贡献是把强模型的工具调用与多轮协商能力外化为 reasoning-enhanced tool-use dialogues，供 student 模型直接 SFT。 |
| OpenMobile [Che26d] | 高 | OpenMobile 先基于环境记忆合成复杂 mobile tasks，再通过 policy-switching rollout 让 student 先执行、expert 在偏离时接管修正，最终保留 corrected trajectories 与 step-level CoT 作为训练数据。它外化的不只是最终动作序列，还包括专家介入时暴露出的纠错性操作经验。 |
| Learning with Challenges [Kan26b] | 高 | 该方法先评估 student 的能力边界，再利用多智能体生成器合成难度自适应的 mobile GUI trajectories，并反向补出 step-level thoughts 与 task instructions。其核心思想是按 student 的 learning frontier 定制外化 demonstrations，使 teacher 生成的数据既可学又具有挑战性。 |
| APIGen-MT [Pra25b] | 高 | APIGen-MT 先生成 task blueprint 和 ground-truth action sequence，再通过 simulated agent-human interplay 合成多轮 function-calling dialogues，并用 rejection sampling 只保留最终状态与 blueprint 一致的轨迹。它将 teacher 对多轮 API 协作与用户澄清流程的隐式能力外化为可验证的 tool-use demonstrations。 |
| ToolAlpaca [Tan23] | 高 | ToolAlpaca 用 ChatGPT 分别扮演 user、assistant 和 tool executor，通过多智能体 simulation 生成 `{Instruction, Actions, Response}` 形式的工具使用轨迹，再以此微调 Vicuna 类 student。它是较早清晰展示 parametric tool-use competence 向 tokenized demonstrations 外化的代表性工作。 |
| APIGen [Liu24n] | 高 | APIGen 让强模型基于真实可执行 API 自动生成自然语言 query 与结构化 function-calling answers，并通过 format、execution 与 semantic 三层检查筛出高质量样本。尽管其交互深度较浅，但它仍然体现了将 teacher 的函数调用知识外化为 verifiable token artifacts 以训练 student 的典型路径。 |
| ToolACE [Liu24o] | 高 | ToolACE 先自动扩充 API pool，再用多智能体 self-guided dialogue generation 合成单步、并行、依赖等多种复杂工具调用对话，并通过 dual-layer verification 过滤。它的重要性在于把 frontier LLM 的 API orchestration 能力外化成覆盖更高组合复杂度的 tool-use training dialogues。 |
| AutoSurfer [Fai26] | 高 | AutoSurfer 让 GPT-4.1 先系统性 surf 真实网站、发现功能空间，再据此合成任务并精炼为包含页面状态、动作历史、下一步动作与推理的 web task tuples。它强调先探索再建模，把 teacher 对网站 affordance 的理解外化为更贴近真实网页结构的 SFT demonstrations。 |
| Scalable Data Synthesis for Computer Use Agents with Step-Level Filtering [He25g] | 高 | WebSTAR 先利用强 computer-use teacher 生成 GUI 或 web trajectories，再用 o4-mini 做 post-hoc thought augmentation 和 step-level filtering，仅保留高质量步骤用于 student 训练。该工作凸显了 demonstration externalization 中一个关键变体，即不仅外化轨迹，还对轨迹内部步骤做再评分与重写，以提升监督信号密度。 |
| ANCHOR [Wei26b] | 中高 | ANCHOR 从少量高质量 seed GUI trajectories 中识别 branch points，再由强模型围绕这些分支扩展新任务和新轨迹，并用 trajectory-level 与 step-level filtering 清洗结果。它说明 demonstration externalization 可以建立在已有成功前缀之上，通过 teacher 的分支扩展能力生成更丰富、更长程的可训练 demonstrations。 |

## 边界案例

| 标题 | 匹配程度 | 可用于正文的 1到2 句描述 |
| --- | --- | --- |
| FABRIC [Ver25b] | 边界 | FABRIC 通过 LLM-only pipeline 生成 task description、tool definition、policy pseudocode、dialogue 与 execution trace 等 agentic records，最终形成 training-ready synthetic data。它与 Demonstration Externalization 相邻，但外化对象不只是行为示范，还包含较强的程序骨架与任务 schema，因此更像一个面向 enterprise agent 的综合数据工厂。 |
| AgentSynth [Xie25e] | 边界 | AgentSynth 通过多代理协作，将简单子任务执行轨迹逐步合成为更长程、更困难的 computer-use tasks 与 corresponding trajectories，用于训练和评测 generalist computer-use agents。它确实外化了 demonstrations，但方法重心同样明显放在 scalable task generation 与 benchmark construction 上。 |
| ASTRA [Tia26] | 边界 | ASTRA 同时合成 tool-use trajectories 与 reinforcement arenas，让 student 先从合成 demonstrations 做 SFT，再在外化出来的环境中继续 RL。由于其外化对象既包括行为轨迹，也包括可交互训练环境和奖励结构，它处在 demonstration externalization 与 composite training pipeline 的交界处。 |
| Mock Worlds, Real Skills [Lu26j] | 边界 | 这篇工作通过强 teacher 生成 synthetic tasks、mock tool ecosystems、high-level workflows 与 task-level rubrics，再在模拟环境中训练小型 agentic model。它包含明显的外化成分，但更核心的贡献是把“任务、环境、评价准则”整体造出来，而不只是外化一批 student 直接模仿的 demonstrations。 |
| Controllable and Verifiable Tool-Use Data Synthesis for Agentic Reinforcement Learning [Xu26e] | 边界 | COVERT 先由 LLM 合成带 oracle tool call、oracle output 与 oracle answer 的可验证 tool-use instances，再通过 oracle-preserving augmentation 构造成可供 RL 使用的训练环境。它与 Demonstration Externalization 接壤，但其主要下游消费方式是在线 RL 而非纯 imitation-style student learning。 |
| Step-GUI Technical Report [Yan25x] | 边界 | Step-GUI 将已有轨迹进一步抽取和重写为进度追踪、状态总结、自我反思、动作预测等七类结构化 CoT 训练数据，用于冷启动 SFT 与后续 RLVR。它与 P7 的相似之处在于 externalize 了可训练 token artifacts，但更像“轨迹后处理与经验重写”，因而也可视为 trajectory-to-token distillation 与 composite pipeline 的边界案例。 |

### Evaluative Supervision Externalization

## 主例

| 标题 | 匹配程度 | 可用于正文的 1到2 句描述 |
|---|---|---|
| [He25g] Scalable Data Synthesis for Computer Use Agents with Step-Level Filtering | 主例 | 该工作先用强 CUA 生成 noisy computer-use trajectories，再由 o4-mini 对每一步动作进行 correctness 与 optimality grading，并附带 screenshot analysis、action review 与 alternative analysis 等 reasoning-rich step annotations，从而把 evaluator 的判断外化为可保存的 graded step-level supervision。基于这些 artifact，作者构建了 WebSTAR 和 WebSCORE，前者用于训练 student computer-use agent，后者进一步蒸馏出可高效部署的 StepRM，体现了从参数化评估能力到 tokenized evaluative data 的完整外化链条。 |
| [Log26b] Scaling Web Agent Training through Automatic Data Generation and Fine-grained Evaluation | 主例 | 该工作用 LLM 或 VLM judge 从 web task 中抽取显式 constraints，并在轨迹的每个时间步评估 constraint satisfaction state，形成细粒度的 CSR progress signal；这些评估信号进一步驱动 prefix extraction 与 hindsight relabeling，使部分成功轨迹也能转化为可训练样本。其关键不只是过滤成功与失败，而是把 judge 的进度判断物化为可复用的 progress annotations 与 relabeled training artifacts，用于蒸馏 student web agent。 |
| [Lu25e] STEVE: A Step Verification Pipeline for Computer-use Agent Training | 主例 | STEVE 使用 GPT-4o 作为 step verifier，比较动作执行前后的屏幕状态，对每一步生成 binary correctness label，并保留与判断相关的 verification reasoning，从而把强 VLM 的评估能力转化为 step-verified trajectory data。作者再用这些步骤级验证数据通过 KTO 优化 7B 开源 computer-use agent，说明 verifier 输出本身已成为可独立消费的训练监督，而不只是内部质量控制。 |
| [Yan25x] Step-GUI Technical Report | 主例 | Step-GUI 提出 Calibrated Step Reward System，先用轨迹级 verifier 建立可靠的质量锚点，再由强多模态 thinking model 把这些验证结果转写为 progress tracking、state summary、effect prediction、self-reflection、state verification、intent execution 与 action prediction 等七类结构化 step-level supervision。它的核心贡献不是单纯扩充 demonstrations，而是将稀疏的轨迹级成败判断外化为密集的过程性监督 artifact，并把这些 artifact 直接喂给后续 agent 训练。 |

## 边界案例

| 标题 | 匹配程度 | 可用于正文的 1到2 句描述 |
|---|---|---|
| [Wan25x] STeCa: Step-level Trajectory Calibration for LLM Agent Learning | 边界案例 | STeCa 先通过 Monte Carlo 采样比较 expert action 与 exploratory action 的 step-level reward，识别轨迹中的偏离步骤，再调用 LLM 生成 reflective thoughts 与 calibrated actions，把失败步骤改写为带有反思和修正信息的 calibrated trajectory。它确实把评估结果外化为可训练的文本化修复经验，但其监督信号与 trajectory calibration 紧密耦合，因此位于 evaluative supervision externalization 与 trajectory repair 之间的边界地带。 |
| [Xio24] Watch Every Step! LLM Agent Learning via Iterative Step-level Process Refinement | 边界案例 | 该工作利用 Monte Carlo rollout 将原本稀疏的 outcome reward 细化为 step-level reward，并据此构造 contrastive action pairs 与 step-level preference data，再通过 Step-DPO 和 Outcome-DPO 对 agent 进行迭代优化。由于其关键监督来自对结果奖励的步骤化重分配，而非一个独立 judge 直接外化 critique 或 label，它可以视为本节的边界正例，但不如前述主例那样体现纯粹的 evaluator-to-token 外化。 |
| [Yan25s] The Lighthouse of Language: Enhancing LLM Agents via Critique-Guided Improvement | 边界案例 | CGI 训练一个专门的 critic model，对候选动作从 contribution、feasibility 和 efficiency 等维度给出细粒度评分，并生成自然语言 revision suggestions，再把这些 critique token 交给 actor 做动作精炼，并收集成功 refinement 轨迹继续训练 actor。它清楚展示了 evaluative critique 的外化与再消费，但整体更偏 critique-guided actor improvement pipeline，而不是以独立监督数据集为中心的纯 P7 形态。 |
| [Li26l] No More Stale Feedback: Co-Evolving Critics for Open-World Agent Learning | 边界案例 | ECHO 让 co-evolving critic 针对初始 trajectory 生成多条自然语言 diagnoses，并将这些 critique 直接拼接到原始 query 上，诱导 policy 采样 refined rollouts，从而把 critic 的评估知识显式外化为可被策略读取的 tokenized diagnostic feedback。由于这些 artifact 主要服务于同一个同步演化的 RL loop，而非作为独立、可迁移的数据资产被后续系统消费，这篇更适合作为 P7 与 P6 之间的边界案例。 |


## Composite Experience Transformation Pipelines

### Evaluator–Policy Co-Evolution


| 标题 | 可用于正文的 1到2 句描述 |
| --- | --- |
| UI-Genie [Xia25e] | UI-Genie 提出一个 agent 与 reward model 迭代协同提升的 self-improving pipeline：当前 GUI agent 在环境中探索生成成功与失败轨迹，reward model 一方面用 reward-guided beam search 为探索提供细粒度引导，另一方面又通过对失败轨迹做 continuation rollout 自动挖掘“潜在正确步骤”来持续刷新自身。由此，评价器精度的提升会直接提高后续轨迹筛选与数据构造质量，而更强的 agent 又反过来产生更丰富的经验来训练下一轮 reward model。 |
| MagicGUI-RMS [Li26n] | MagicGUI-RMS 构建了由领域特定奖励模型 DS-RM 与通用奖励模型 GP-RM 组成的分层评估系统，并以 automated feedback reflux 将 policy 与 evaluator 放入同一闭环中：agent 先提出动作，DS-RM 做规则层面的局部诊断与纠偏，GP-RM 再结合长程语义上下文进行仲裁。系统一方面把 GP-RM 认可的高质量动作回流为 agent supervision，另一方面把 DS-RM 与 GP-RM 的分歧样本回流为 evaluator 的增量训练数据，从而实现策略与评估器的双向净化和持续演化。 |
| No More Stale Feedback: Co-Evolving Critics for Open-World Agent Learning [Li26l] | ECHO 直接把 critic staleness 视为 open-world agent learning 的核心障碍，并提出 policy 与 critic 的 synchronized co-evolution loop：policy 先生成 on-policy trajectory，critic 基于该轨迹给出多视角自然语言诊断，policy 再据此执行 conditional refinement。随后两者在同一批由“初始轨迹—诊断—修正轨迹”构成的经验上做 dual-track GRPO 更新，并通过 saturation-aware gain shaping 强化 critic 对高分区间细微改进的敏感性，以避免反馈过时和闭环停滞。 |
| RLAnything: Forge Environment, Policy, and Reward Model in Completely Dynamic RL System [Wan26u] | RLAnything 将 policy、reward model 与 environment 一并纳入 closed-loop optimization：当前 policy 生成的轨迹既作为 policy learning 的经验，也作为 reward model 的训练样本，而 reward model 产出的 step-wise feedback 又与 outcome signal 融合后反过来更新 policy。更进一步，它引入 theory-motivated environment adaptation，依据当前训练状态动态调节任务难度，使 evaluator–policy coupling 不再局限于固定环境中的双模块更新，而扩展为策略、评估器与训练分布共同演进的三元复合闭环。 |
| RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning [Zha25y] | RL Tango 通过交替式强化学习联合训练 generator 与 verifier，使 verifier 不再是静态外部奖励器，而是在 generator 当前 reasoning trajectory 分布上持续更新的 process-level evaluator。其关键点在于 verifier 虽只接受 outcome-level correctness reward，却学习生成 step-level verification feedback，并以此持续塑造 generator 的优化方向；同时，generator 的新轨迹又不断暴露新的验证难点，推动 verifier 一起进化，从而缓解固定 verifier 常见的 reward hacking 与分布外失配问题。 |
| VARP: Reinforcement Learning from Vision-Language Model Feedback with Agent Regularized Preferences [Sin25b] | VARP 针对 VLM preference feedback 难以覆盖完整行为过程的问题，将 trajectory sketch 叠加到终态观测上以提升 VLM 偏好判断的时序可见性，并在此基础上训练 reward model。更关键的是，它在 reward learning 中加入 agent-regularized preferences，使奖励函数显式依赖当前 policy 生成的 rollout 数据而非脱离行为分布独立学习，因此 reward model 会随 policy 能力变化而持续重估偏好边界，再将更新后的奖励继续用于 policy optimization。 |
| EVPO: Explained Variance Policy Optimization for Adaptive Critic Utilization in LLM Post-Training [Pan26] | EVPO 关注的不是单纯“是否使用 critic”，而是 critic 在不同训练阶段是否真的值得信任；为此它以 batch-level explained variance 作为实时判据，在 critic-based advantage estimation 与 batch-mean baseline 之间自适应切换。由于 critic 本身仍随 policy 训练持续更新，EVPO 实际上刻画了一个“critic 成熟度”与 policy 优化节奏相互耦合的过程：当 critic 尚不稳定时抑制其影响，待其逐步学到有效状态信号后再释放其对策略更新的指导作用。 |
| Co-Evolution of Policy and Internal Reward for Language Agents [Wan26aj] | 这篇论文提出 Self-Guide，让同一个 language agent 在每一步先生成短 self-guidance，再将该信号同时作为 inference-time action steering 与 training-time internal reward 的来源，从而把 evaluator 内生化到 policy 自身的生成过程中。随着 policy 提升，模型会产出更可靠的 guidance；而更好的 guidance 又会被转写为更密集的 step-level internal reward 继续优化 policy，形成一个显式的 policy–internal-reward co-evolving loop。 |



### Refinement-Mediated Policy Internalization


| 标题 | 匹配程度 | 可用于正文的 1 到 2 句描述 |
|---|---|---|
| Internalizing Agency from Reflective Experience [Ge26] | 主例 | 该方法将 agent 的失败 rollout 先转化为 rollback target 与 natural-language reflective summary，再据此生成修正分支，并构造不含显式反思文本的 counterfactual training pairs。随后，模型通过 experience-to-policy distillation 学会在原始上下文下直接复现这些修正决策，从而把外显的反思式纠错能力内化为 policy parameter。 |
| Watch Every Step! LLM Agent Learning via Iterative Step-level Process Refinement [Xio24] | 主例 | 该工作并不直接用整条 trajectory 的成败做粗粒度训练，而是利用 Monte Carlo rollout 将 outcome reward 下放到步骤层面，构造 step-level contrastive action pairs 与 trajectory-level preference pairs。模型随后联合 step-DPO、outcome-DPO 与 SFT 学习这些 refined process signals，从而把原始经验中的局部优劣结构写入 policy。 |
| Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training [Yua25c] | 主例 | 该方法从 MCTS 生成的 good 和 bad trajectories 中，构造带有 reflection signal 的 revision trajectories，使模型学习在识别到首个关键错误后及时中断原路径并切换到修正分支。其核心不是直接模仿成功示范，而是通过 first-error localization 与 revised trajectory synthesis，把失败经验加工成可被 policy 内化的反思式监督。 |
| Skill-SD: Skill-Conditioned Self-Distillation for Multi-turn LLM Agents [Wan26al] | 主例 | 这篇工作先将多轮 agent trajectories 总结为结构化 natural-language skills，包含 success analysis、mistake analysis 与 golden workflow，再把这些 skills 仅作为训练期 teacher 的特权信息。student 在不显式访问 skills 的条件下通过 self-distillation 拟合 teacher 分布，从而把 trajectory-level skill abstraction 内化进 policy weights。 |
| Online Experiential Learning for Language Models [Ye26f] | 主例 | 该方法把在线交互轨迹逐步提炼为可迁移的 experiential knowledge，而不是直接在 raw trajectories 上做更新；这些知识随后作为 teacher context，经由 on-policy context distillation 被压缩进 student 参数。作者还直接比较了 raw trajectory 与 extracted knowledge，表明先做经验抽取再做参数内化明显更有效。 |
| STeCa: Step-level Trajectory Calibration for LLM Agent Learning [Wan25x] | 主例 | STeCa 首先检测 trajectory 中第一个真正偏离 expert path 的动作，再生成包含 reflective thought 与 corrected action 的 calibrated trajectory，用以替换原始偏离片段。后续 policy 在这些 step-level calibrated samples 上继续训练，因此其关键贡献在于把 noisy exploration 重新解释为更精确的 corrective supervision。 |
| GUI-Reflection: Empowering Multimodal GUI Models with Self-Reflection Behavior [Wu25b] | 主例 | 该方法通过离线伪造错误与在线挖掘失败轨迹，自动构造包含 reflection thought、rollback 与 correction 的 GUI self-reflection data，而不是直接依赖人工标注的成功示范。模型随后在这些 refined reflection traces 上持续微调，从而把 GUI 场景中的自检与自修复行为内化为端到端策略。 |
| ReAct Meets ActRe: When Language Agents Enjoy Training Data Autonomy [Yan24m] | 主例 | 这篇工作先让 agent 在环境中探索得到动作序列，再利用 ActRe 为这些动作反向补写 posterior reasoning，将原本缺乏解释的 action traces 重构为可训练的 ReAct-style trajectories。随后，模型通过 contrastive self-training 吸收这些由探索经验转化而来的 reasoning-action pairs，实现从 raw exploration 到 policy internalization 的闭环。 |
| CLEANER: Self-Purified Trajectories Boost Agentic Reinforcement Learning [Xu26j] | 主例 | CLEANER 通过 similarity-aware adaptive rollback 将含有错误代码、报错回溯与恢复噪声的原始轨迹，重写为更干净的 self-purified trajectories，从而避免错误上下文污染后续学习。模型随后在 purified paths 上进行 RL 更新，并通过 logit recomputation 减少分布偏移，使 policy 学到的是被净化后的正确推理与工具使用模式。 |
| AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling [Din26] | 主例 | 该方法并不直接丢弃 failed trajectories，而是先从失败轨迹中提取其实际达成的 outcomes，再据此逆向生成与轨迹真实效果一致的 hindsight goals，将失败运行重写为可学习的成功 demonstration。随后，这些 relabeled goal-trajectory pairs 被序列化为 SFT 或 DPO 训练样本，使 policy 能够把失败经验中的局部有效行为内化为参数化能力。 |
| Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents [Son24] | 主例 | 该工作先让 agent 在环境中探索并收集失败轨迹，再将其与成功轨迹构造成 trajectory-level preference pairs，而不是直接在原始 rollout 上做模仿学习或标准 RL。其核心在于把原始 experience 加工为对比式 supervision，再通过 DPO 将“成功优于失败”的偏好结构写入 policy。 |
| Memento No More: Coaching AI Agents to Master Multiple Tasks via Hints Internalization [Ala25] | 主例 | 该方法先由 reviewer 从 agent 轨迹中识别 mistake pattern，并生成针对特定状态的 corrective hints，使 teacher 在这些 hints 引导下输出更优行为分布。随后，student 通过 context distillation 学会在不显式接收 hints 的条件下复现 teacher 行为，从而把外部提示式经验内化为参数中的策略能力。 |
| UI-Genie: A Self-Improving Approach for Iteratively Boosting MLLM-based Mobile GUI Agents [Xia25e] | 边界案例 | UI-Genie 通过 reward-guided trajectory exploration 收集原始 GUI 交互经验，再结合 outcome verification 与 continuation rollout 对成功轨迹和中间步骤进行筛选与重标，构造出更干净的 agent training set 与 reward-model training set。它后续确实用这些 refined trajectories 继续训练 agent，但其中 refinement 主要体现为验证、过滤与 relabeling，因此比显式 reflection 或 repair 型方法更偏数据 flywheel 边界情形。 |
| OpenWebVoyager: Building Multimodal Web Agents via Iterative Real-World Exploration, Feedback and Optimization [He24e] | 边界案例 | 该方法让 web agent 在真实网站上自主探索生成 multimodal trajectories，再用 GPT-4o 作为 auto evaluator 对这些轨迹进行 rejection sampling，只保留被判定为成功的高质量样本。保留下来的 refined trajectories 会并入后续 SFT 数据中继续优化 policy，因此它具备“经验筛选后再内化”的复合链条，但中间产物主要是 filtered successful traces，refinement 机制相对较弱。 |
| Policy Improvement using Language Feedback Models [Zho24e] | 边界案例 | 这篇工作先从大模型反馈中蒸馏出一个 Language Feedback Model，再由该模型对 agent rollout 中的局部动作进行 desirability 判断，从原始经验里筛出更值得模仿的行为片段。最终 policy 通过 imitation learning 吸收这些经过反馈模型提纯的行为数据，但其中间环节更像 evaluator-mediated filtering，因此更适合作为本小节与 evaluator pathway 之间的边界案例。 |
| RetroAgent: From Solving to Evolving via Retrospective Dual Intrinsic Feedback [Zha26] | 边界案例 | RetroAgent 将原始 trajectories 事后转化为两类 refined feedback，一类是用于 RL 更新的 intrinsic numerical reward，另一类是可操作的 textual lessons，并通过双通路共同推动 policy improvement。由于其一条主支路更接近 reward shaping，另一条又保留了显著的 memory use 成分，因此它更适合作为 refinement-mediated internalization 与 evaluator-shaped policy learning 之间的边界案例。 |
| VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought [Sar24b] | 边界案例 | 该方法先把 noisy embodied trajectories 提炼为包含因果解释、状态变化与子目标结构的 embodied programs of thought，再将这些 refined artifacts 同时用于 retrieval 和 supervised fine-tuning。若强调其 SFT 分支，它可视为“经验先抽象再内化”的复合路径；但由于其 memory-writing 与 inference-time reuse 同样关键，更适合作为本小节与 memory-oriented composite methods 之间的边界案例。 |


### Other Composite Experience Pipelines

| 标题 | 匹配程度 | 可用于正文的 1到2 句描述 |
| --- | --- | --- |
| OS-Genesis [Sun24b] | 强相关 | OS-Genesis 不是先给任务再采轨迹，而是先在 GUI 环境中做 interaction-driven traversal，收集 action-centered traces，再反向合成 high-level tasks，并用 trajectory reward model 对生成出的完整轨迹进行分级采样。其关键贡献在于把 exploratory interaction 依次转化为 synthesized task、scored trajectory 和 training supervision，使 experience generation 与 downstream policy training 被一个显式的质量控制链条连接起来。 |
| OpenWebVoyager [He24e] | 强相关 | OpenWebVoyager 先用 imitation learning 得到初始 web policy，再让 agent 在真实网页上持续 self-exploration，并由外部 judge 对探索轨迹做 trajectory-level rejection sampling，只将 judged-good trajectories 回灌到下一轮训练。该方法的核心不是普通 online data collection，而是 exploration, external judging, and selective policy optimization 组成的闭环式 composite pipeline。 |
| AgentTrek [Xu24] | 强相关 | AgentTrek 将 web tutorials 先转写为结构化 task specifications，再在真实环境中执行 guided replay 生成 multimodal trajectories，并通过 VLM evaluator 做 instruction adherence 与 goal completion 验证，最终把筛选后的轨迹用于 agent training。它的关键在于 tutorial text 并不直接训练 policy，而是先被组织成可执行 task scaffold，再转化为 verified interaction experience。 |
| Bootstrapping Language-Guided Navigation Learning with Self-Refining Data Flywheel [Wan24ad] | 强相关 | 该文构造了一个 generator–navigator self-refining flywheel：instruction generator 从无标注轨迹生成指令，navigator 再根据 SPL 和 nDTW 等执行一致性指标筛选高保真样本，这些样本反过来用于提升 generator，并继续产生更好的 navigator training data。其核心贡献是让生成模型与执行模型通过 fidelity-based filtering 共同塑造可训练经验，而不是单向的数据合成。 |
| MCTS-EP [Xu25q] | 强相关 | MCTS-EP 用 MCTS 在 embodied environment 中扩展 trajectory space，不仅提取成功路径，还在分支节点上根据搜索得到的 long-horizon value 构造 preference pairs，然后分别用于 SFT 和 DPO 更新 policy。这里 search 不是辅助推理，而是将原始交互经验重组为 success trajectories 与 structured preferences 两种可训练载体的关键中介。 |
| Self-Improving Vision-Language-Action Models with Data Generation via Residual RL [Xia25h] | 强相关 | PLD 先训练 residual actor 去 probe base VLA 的 failure regions，再通过 hybrid rollout 收集既贴近 base-policy deployment distribution、又包含 recovery behavior 的成功轨迹，最后将这些经过分布校准的轨迹蒸馏回 generalist VLA。该方法的重点不在 residual RL 本身，而在 probe, curate, distill 三阶段如何把 failure-targeted exploration 转化为更适合 generalist internalization 的数据。 |
| Scalable Data Synthesis for Computer Use Agents with Step-Level Filtering [He25g] | 强相关 | 该文从强 CUA 的 noisy successful rollouts 出发，对每一步动作进行 step-level grading，只让高质量 steps 贡献监督损失，同时保留错误步骤作为上下文，最终据此训练更强的 policy，并进一步蒸馏出 StepRM。其方法贡献在于把表面上“成功”的 trajectory 重新分解为 graded local experience，从而将噪声 rollout 转化为可靠 supervision。 |
| Trial and Error [Son24] | 强相关 | Trial and Error 让 agent 在环境中主动探索并收集失败轨迹，再把 failure–success pairs 转成 DPO 所需的 contrastive training data，以此替代直接做高方差在线 RL。其复合性体现在：原始交互经验先被重解释为 preference-style supervision，再被用于 policy internalization。 |
| AutoSurfer [Fai26] | 强相关 | AutoSurfer 先以 breadth-first 方式系统探索网站，获得覆盖更全面的页面和 action traces，再基于这些 exploration trajectories 合成 grounded tasks，并利用同一批探索轨迹作为 hints 去引导 trajectory refinement，最终转成 SFT 数据训练 web agent。它的关键不是单次数据合成，而是将 website coverage, task synthesis, trajectory refinement 串成一个显式的 generate-organize-train pipeline。 |
| WebRL [Qi24] | 强相关 | WebRL 先从 failure set 出发生成新的 curriculum tasks，并通过 critic-based difficulty filtering 与 feasibility filtering 筛选任务；agent rollout 后，再由 outcome reward model 和 actor-confidence replay filtering 选择可用经验，最后联合更新 actor 与 critic。该方法的核心是把 task generation、experience selection 与 off-policy RL 串成一条自演化的数据管线，而不是简单的 online RL。 |
| Agent Q [Put24] | 强相关 | Agent Q 通过 MCTS 在环境中生成搜索树和多分支轨迹，并结合 critic ranking 与 outcome reward 形成 node-level preference signal，再将这些 search-derived preferences 转化为 DPO 训练数据以更新 policy。其关键贡献在于把 search experience 从“探索过程”进一步编译为可监督的 preference artifacts，从而实现 search-to-policy 的复合转化。 |
| DigiRL [Bai24] | 强相关 | DigiRL 在真实 device environment 中做 autonomous rollouts，并用 VLM-based AutoEval 为轨迹提供奖励信号，随后同时进行 instruction-level curriculum selection 与 step-level doubly-robust filtering，再以 advantage-weighted regression 更新 policy。它的关键不只是 autonomous RL，而是将原始交互数据经过多级评估与筛选后，转化为更稳定、更高价值的训练经验。 |
| BLAZER [Das25] | 强相关 | BLAZER 使用强 LLM 在 simulator 中零样本生成 manipulation demonstrations，再通过环境执行验证仅保留成功样本，最后用这些 automatically verified demonstrations 微调较小的 manipulation agent。它代表了一类典型的 simulator-backed generate-verify-train pipeline，其中 synthetic experience 的可靠性来自执行验证而非人工标注。 |
