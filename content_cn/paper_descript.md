
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
