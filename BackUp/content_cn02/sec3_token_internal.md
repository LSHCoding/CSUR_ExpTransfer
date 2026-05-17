# Tokenized-to-Tokenized Transformations

Tokenized-to-Tokenized Transformations 也不同于 Parametric-to-Tokenized externalization，其的输入必须是具体的 agent trajectory、execution log 或 interaction record，模型在其中扮演 abstractor、formalizer 或 synthesizer；若 artifact 主要由模型根据任务描述或内化知识直接生成，而无具体轨迹作为输入，则是 Parametric-to-Tokenized Transformations。

## Narrative-to-Narrative Transformation

Narrative-to-Narrative Experience Transformation 将 narrative tokenized agent experience 转化为更高层的 narrative artifact。源经验来自 agent 序贯决策中产生的具体轨迹：task execution log、reasoning trace、tool-use trajectory、web navigation history、GUI interaction trace、robot execution record、multi-turn dialogue history 或 failure episode。这些轨迹记录了 agent 在特定上下文下如何观察、推理、行动并接收环境反馈，是对 \(e=(c,a,o,f)\) 的自然语言或多模态序列化记录。

P1 的目标不是在载体层级之间移动，而是在 narrative tokenized 层内部完成抽象、压缩、重写或归纳。转化后的 artifact 仍为弱形式化的 tokenized 表达：reflection、summary、lesson、failure explanation、heuristic、guideline、insight、mistake pattern、natural-language skill、manual entry 或 experience note。它们通过 retrieval-augmented prompting 或 direct prompt injection 被后续 agent 消费，而非由 parser、executor、graph traversal module 或训练过程处理。

P1 与 Narrative-to-Schematic Transformation 的区别在于下游消费机制。即使目标 artifact 表面呈现为编号列表、规则集合或 skill description，只要其复用依赖 language understanding 而非专门的执行器、解析器或结构化遍历机制，它仍属于 P1。若经验被转化为 code、workflow、decision tree、knowledge graph、action schema、API routine 或可执行 procedure，则应归入 P2。P1 也不同于 Parametric-to-Tokenized externalization：P1 的输入必须是具体 agent trajectory 或 interaction log，而非模型仅凭参数知识生成的 guideline 或 instruction。

不同论文以 reflection、memory、skill、guideline、insight 等术语指代机制上并不相同的对象，因此本文不按 artifact 的表面名称组织 P1 方法，而是按经验抽象所依赖的轨迹粒度划分：Per-Trajectory Experience Abstraction 从单条轨迹中抽象局部经验；Cross-Trajectory Experience Induction 从多条轨迹中归纳共性规律；Dual-Granularity Experience Consolidation 同时包含单轨迹写入与跨轨迹整合，使 narrative memory 随交互持续演化。


### Per-Trajectory Experience Abstraction

Per-Trajectory Experience Abstraction 以单条 agent trajectory、episode、trial 或局部 execution log 为主要输入，将一次具体执行经验抽象为更高层的自然语言 artifact。这类方法在任务结束、失败发生、环境反馈返回或一次 trial 完成后触发，通过 reflection、summarization、critique、failure explanation 或 hindsight rewriting 将原始轨迹压缩为可复用的文本经验。

artifact 形式包括 episode-level reflection、trajectory summary、failure diagnosis、lesson learned、hindsight note、local tip 或 correction suggestion。它们的共同点在于来源粒度：artifact 主要由单条轨迹内部的信息抽象而来，关注的是如何从一次具体经历中提炼对下一次决策有帮助的局部经验。

单次执行轨迹本身包含可复用的经验信号。失败轨迹可能揭示错误假设、无效动作、遗漏约束或不恰当的工具调用；成功轨迹可能包含有效的分解策略、搜索路径或环境交互模式。用语言模型对这些轨迹进行事后解释和压缩，agent 可以把原本冗长、低层、任务绑定的历史记录转化为更短、更抽象、更易注入上下文的经验描述。

这类方法的主要优势是反应快、成本低、不依赖大量历史数据，适合 trial-and-error setting、online adaptation 和任务分布较窄的场景。agent 只需从最近一次失败或成功中提取经验，就可能在下一次尝试中避免重复错误或复用有效策略。

局限同样明显。抽象主要依赖单条轨迹，容易受偶然因素和错误归因影响。一次失败不代表其中所有动作都错，一次成功也不保证所有策略都具有泛化性。若 reflection 或 failure explanation 将偶然现象误写作通用经验，后续 agent 可能被误导。此外，单轨迹 artifact 与原始任务上下文绑定较强，跨任务迁移能力有限——它更适合局部 adaptation，而非稳定经验规律的来源。

论文：
- Reflexion: Language Agents with Verbal Reinforcement Learning
- Reflection-Based Memory For Web Navigation Agents
- REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction
- MemOrb: A Plug-and-Play Verbal-Reinforcement Memory Layer for E-Commerce Customer Service
- Sample-Efficient Online Learning in LM Agents via Hindsight Trajectory Rewriting
- Self-Generated In-Context Examples Improve LLM Agents for Sequential Decision-Making Tasks
- MemGovern: Enhancing Code Agents through Learning from Governed Human Experiences


Per-Trajectory Experience Abstraction 关注的是如何从单条 agent trajectory 中事后提炼出可复用的文本经验，而不是直接回放原始执行日志。Reflexion [Shi23b] 在每次 trial 后根据失败轨迹与环境反馈生成简短 reflection，并在下一轮尝试中作为 verbal memory 注入 prompt；Reflection-Based Memory for Web Navigation Agents [Aza25] 则将单次网页交互总结为包含有效步骤、站点局限、捷径与改进建议的 Web-Reflection，再通过检索辅助后续导航。两者都体现出同一思路：把一次具体经历压缩成更短、更抽象、也更易复用的自然语言 artifact。

这一机制也出现在具身、对话与代码场景中。REFLECT [Liu23] 将单次机器人执行的多模态观测转写为 failure explanation，并用其指导后续 correction planning；MemOrb [Hua25] 将单轮客服交互总结为可检索的 verbal-reinforcement memory。更进一步，Hindsight Trajectory Rewriting [Hu25] 把失败轨迹事后改写为可复用的合成成功经验，Self-Generated In-Context Examples [Sar25] 从单条成功轨迹中构造可复用的 demonstration，而 MemGovern [Wan26ap] 则将单个代码修复案例提纯为结构化 experience card。尽管这些方法的 artifact 形式不同，它们共享的核心都是：以单次执行经验为输入，在 episode 后进行局部抽象，并将所得文本经验直接用于后续决策。

```
## Per-Trajectory Experience Abstraction

这一路径的代表性工作，将单条 agent trajectory 在任务结束后事后压缩为更短的自然语言经验，再把这些经验作为后续决策的上下文条件，而不是直接回放原始执行日志。Reflexion [Shi23b] 是这一范式的早期代表：agent 在每次 trial 结束后，根据失败轨迹与环境反馈生成简短 reflection，将错误归因、行为教训与改进建议写成 verbal memory，并在下一轮尝试中直接注入 prompt。其关键点不只是“记录失败”，而是把冗长轨迹转成更易复用的语言化经验；论文中的消融也表明，reflection 比直接保留原始 episodic trajectory 更有效。类似地，Reflection-Based Memory for Web Navigation Agents [Aza25] 将单条网页交互轨迹总结为 Web-Reflection，内容覆盖有效步骤、站点功能局限、捷径、失败回溯点与改进建议，再通过语义检索将相关 reflection 回注到新任务中，使 agent 能从一次具体浏览经历中快速提炼出局部但可复用的导航知识。

在具身与交互环境中，per-trajectory abstraction 也常表现为对失败经验的解释性压缩。REFLECT [Liu23] 并不依赖跨 trial 的统计归纳，而是对单次机器人执行中的多模态观测流做分层摘要，在子目标验证失败后生成自然语言 failure explanation，并据此驱动后续 correction planning。MemOrb [Hua25] 则将单轮客服对话及其工具调用轨迹事后总结为策略性 verbal-reinforcement memory，再以可检索的 Orb 单元形式存储，用于后续相似会话中的提示增强。两者都体现出同一设计原则：一次具体经历本身就包含足以支持局部适应的经验信号，关键在于如何把它从低层事件流转写为紧凑、可注入的文本 artifact。

另一些方法进一步放宽了“抽象”的形式，不再局限于显式 critique 或 reflection，但仍保留单轨迹事后转写的核心机制。Hindsight Trajectory Rewriting [Hu25] 在 episode 结束后对失败轨迹进行 hindsight rewriting，将其改写为针对其他潜在目标的合成成功轨迹或更紧凑的 workflow 描述，从而把失败探索转化为可复用的正向 in-context experience。Self-Generated In-Context Examples [Sar25] 则从 agent 自己完成任务的单条成功轨迹中自动构造 self-generated demonstrations，并在后续规划与执行时动态检索这些 examples 作为上下文示例。相比显式“教训总结”，这类方法更接近将一次经历重写为更高质量的示范样本，但本质上仍属于 per-trajectory 的经验压缩与复用。

在代码智能体中，这一路径进一步走向更规范的经验卡片化表达。MemGovern [Wan26ap] 从单个 issue 修复过程中的 governed human experience 出发，将原始修复交互提纯为 problem summary、diagnostic signals、root cause、fix strategy 与 verification 等字段化 textual memory，并在后续代码修复中通过检索支持类比迁移。尽管其表示更结构化，也更强调治理与标准化，但其基本操作单位仍然是一条具体修复经历的事后抽象，而不是跨大量轨迹先做全局规则归纳。
```

### Cross-Trajectory Experience Induction

Cross-Trajectory Experience Induction 以多条 trajectories、demonstrations、rollouts、failure cases 或 historical interactions 为输入，通过比较、聚类、筛选、合并或归纳，抽取更稳定、更通用、更可迁移的 narrative artifact。与单轨迹方法不同，这类方法不满足于解释某一次执行为何成功或失败，而是试图从多次经验中发现反复出现的模式。

artifact 形式包括 rule、guideline、heuristic、insight、do-and-don't list、mistake pattern、natural-language skill、manual entry 或 procedural tip。其共同点是：目标经验并非单条轨迹的直接摘要，而是跨多条轨迹归纳出的共性知识。例如，多个失败轨迹可能共同暴露一种错误操作模式；多个成功轨迹可能共享某种有效的任务分解策略；不同任务中的相似交互片段可能被抽象为可迁移的 natural-language skill。

可迁移经验通常来自多次执行之间的稳定结构，而非单次执行中的偶然片段。通过对比成功与失败轨迹，方法可以识别哪些行为与任务完成更相关，哪些错误在不同上下文中反复出现，哪些约束或策略具有更强的跨任务适用性。得到的 artifact 往往比单条 reflection 更抽象，也更接近 agent 可长期复用的经验规律。

这类方法的主要优势是泛化能力更强。artifact 来自多条经验的归纳，更可能滤掉单次轨迹中的偶然噪声，保留在多个任务或多个 episode 中稳定出现的有效模式。Cross-Trajectory Experience Induction 适合构建 rule bank、guideline library、mistake notebook、experience bank 或 natural-language skill repository，并在新任务中通过检索或条件选择复用。

挑战也同样存在。它需要积累足够多的轨迹，冷启动能力弱于单轨迹抽象。多轨迹归纳存在过度抽象风险：模型可能把特定环境中的局部规律错误上升为通用规则。不同轨迹可能支持相互冲突的经验结论——某一策略在一个任务中有效，在另一个任务中失败。若缺少冲突检测、适用条件建模或经验筛选机制，归纳后的 artifact 可能含混、冗余甚至相互矛盾。这类方法需要额外关注经验选择、聚类质量、规则适用范围和 artifact 一致性。

论文：
- ExpeL: LLM Agents Are Experiential Learners
- AutoGuide: Automated Generation and Selection of Context-Aware Guidelines for Large Language Model Agents
- Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills
- Skill Set Optimization: Reinforcing Language Model Behavior via Transferable Skills
- SWE-Exp: Experience-Driven Software Issue Resolution
- Mistake Notebook Learning: Batch-Clustered Failures for Training-Free Agent Adaptation
- AutoManual: Constructing Instruction Manuals by LLM Agents via Interactive Environmental Learning
- Procedural Knowledge at Scale Improves Reasoning  
  - 注：偏 reasoning/procedural knowledge，相比标准 P1 的 agent 经验轨迹要求更弱，建议作为相邻工作或边界案例。
- Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory  
  - 注：包含 strategies、code snippets、insights，部分 artifact 可能偏 S-Tok，建议作为边界案例。
- Agent KB: Leveraging Cross-Domain Experience for Agentic Problem Solving  
  - 注：若强调 cross-domain experience aggregation，可放本组；若强调 structured KB / API / workflow，则更接近 P2 或 Composite。

```
## Cross-Trajectory Experience Induction

Cross-Trajectory Experience Induction 关注的不是单次 trajectory 的事后解释，而是从多条 trajectories、demonstrations、rollouts、failure cases 或 historical interactions 中归纳可稳定复用的经验模式，并将其转化为可在后续任务中调用的 narrative artifact。相较于单轨迹 reflection，这类方法更强调跨 episode 的重复结构识别，即从多次执行中抽取那些在不同任务或不同情境下反复出现的有效策略、失败模式与行为约束，并将其组织为 rule、guideline、insight、mistake pattern 或 natural-language skill [Zha23c, Fu24, Ni26, Su25]。

一条路径是基于成功失败对比的跨轨迹归纳。这类方法将成功与失败之间的差异视为经验抽取的主要信号，通过比较优劣轨迹、定位关键分叉点或聚合失败案例，提炼能够跨任务迁移的经验规则。ExpeL 同时利用失败-成功轨迹对与跨任务成功案例集合，通过 insight extraction 生成高层 natural-language insights，并借助 add、edit、upvote、downvote 等操作持续维护经验库，使经验积累从离散 reflection 走向可演化的 rule bank [Zha23c]。AutoGuide 则围绕 contrasting trajectories 展开，在同一任务的优劣轨迹中定位首次偏离步骤，并通过 context identification 与 guideline extraction 生成与局部 context 绑定的 guideline，将“在何种情境下应采取何种动作”显式编码为可检索知识 [Fu24]。Mistake Notebook Learning 进一步将关注点集中于 failure cluster：它先对一批失败轨迹做 subject clustering，再在 cluster level 抽取共性的错误根源、纠正策略与 anti-pattern，形成结构化 mistake notes，并仅在更新确实改善性能时才将其纳入记忆，以抑制偶然失败带来的噪声 [Su25]。在软件工程场景中，SWE-Exp 同时从成功修复轨迹与失败反思中提取 comprehension experience 和 modification experience，并在新 issue 上经过 retrieval、reranking 与 rewriting 后复用，从而将正反两类历史案例转化为可迁移的问题理解与修改策略 [Che25d]。AutoManual 也遵循相似思路：它显式区分 direct success、indirect success 与 failure 三类交互结果，并据此触发不同的 rule generation 与 update 逻辑，再通过 consolidator 与 formulator 将分散经验汇编为统一的 instruction manual [Che24]。

另一条路径是基于多轨迹聚合的跨轨迹归纳。这类方法不以显式的成功失败对比为中心，而是直接从 trajectory collection 中提取重复出现的稳定模式，并将其整理为可复用的自然语言经验单元。Trace2Skill 从并行收集的大量成功与失败轨迹中分别生成局部 skill patches，再通过 hierarchical patch merge 保留跨轨迹反复出现的 prevalent patterns，最终形成包含 natural-language SOP 与辅助资源的 skill directory，其核心在于多轨迹层面的归并与整合，而非单条轨迹上的顺序修补 [Ni26]。Skill Set Optimization 则从多条历史轨迹中提取高奖励且 embedding space 中相似的子轨迹对，再由 LLM 将这些重复出现的局部过程概括为 subgoal 与 instructions，从而构造可检索的 transferable skill set；其归纳过程建立在跨轨迹子过程匹配、评分与后续收益驱动的 refinement 之上 [Not24]。Dynamic Cheatsheet 将测试时积累的多次解题轨迹持续交由 Memory Curator 处理，从中提炼 strategy、solution sketch、code snippet 与 insight，并对已有条目执行 revision、replacement、merging 与 compression，使经验库随交互过程不断演化 [Suz25]。Procedural Knowledge at Scale Improves Reasoning 则从大规模 reasoning traces 中解构出 subquestion-subroutine 对，构建可检索的 procedural knowledge store，并在后续推理过程中按需调用这些 subroutine 作为 problem-solving prior [Wu26]。

总体而言，这两条路径共享同一经验转化逻辑，即将原始 trajectory 从一次性历史记录转化为跨任务可复用的 narrative artifact。前者更依赖 success-failure contrast 来提炼 rule、guideline 与 mistake pattern，后者则更强调在 trajectory collection 上进行 aggregation、merging 与 compression，以抽取稳定的经验结构 [Fu24, Su25, Ni26, Not24]。二者共同提升了经验复用的泛化性，并在一定程度上滤除了单次交互中的偶然噪声，但同时也面临过度归纳、适用范围不清与经验冲突等问题，因此往往需要额外的 selection、updating 与 consistency maintenance 机制 [Che24, Che25d, Suz25]。
```

### Dual-Granularity Experience Consolidation

Dual-Granularity Experience Consolidation 同时包含单轨迹层面的经验写入与多轨迹层面的经验整合。系统通常先从每条新 trajectory 中抽取局部 reflection、summary、lesson 或 episode memory，再随着交互经验积累，对这些局部 artifact 进行合并、去重、重写、压缩、筛选、层级化、淘汰或版本更新，形成持续演化的 narrative memory store。

这类方法的核心问题不只是”如何从一次经验中生成一个 artifact”，也不只是”如何从一批轨迹中归纳一组规则”，而是如何连接这两个过程：新经验如何进入长期记忆，已有记忆如何被更新，重复或低价值经验如何被合并或删除，过时经验如何被淘汰，局部 episode memory 如何逐渐上升为更稳定的 cross-episode insight。

其基本思路是，agent experience 应被视为持续生长的记忆生态。每次交互产生新的局部经验，但简单累积会导致 memory 冗余、噪声增加、检索困难和上下文污染。因此这类方法通常引入 memory controller、retriever、refiner、utility scorer、consolidator 或 forgetting mechanism，管理经验 artifact 的生命周期。

这类方法的优势在于同时兼顾快速适应与长期积累。单轨迹写入使 agent 及时吸收最近经验，跨轨迹整合使系统逐渐形成更稳定、更紧凑、更可迁移的经验结构。相比只做 episode-level reflection 的方法，Dual-Granularity 方法更适合 long-horizon tasks、cross-session interaction、continual learning 和 open-ended agent deployment。相比一次性 batch induction，它更强调在线更新和长期维护，使 memory 能随任务分布和环境反馈变化持续调整。

Dual-Granularity Experience Consolidation 代表了 P1 路径中更系统化的发展方向。它将单次经验抽象、多次经验整合和长期记忆管理连接起来，使 agent 能够从孤立的 execution logs 中逐步构建可持续复用的 narrative experience store。其有效性不仅取决于 artifact 生成质量，也取决于 memory selection、retrieval、consolidation、conflict resolution 和 staleness handling 等管理机制。

论文：
- CLIN: A Continually Learning Language Agent for Rapid Task Adaptation and Generalization
- R2D2: Remembering, Replaying and Dynamic Decision Making with a Reflective Agentic Memory
- Darwinian Memory: A Training-Free Self-Regulating Memory System for GUI Agent Evolution
- M2: Dual-Memory Augmentation for Long-Horizon Web Agents via Trajectory Summarization and Insight Retrieval
- Learning on the Job: An Experience-Driven Self-Evolving Agent for Long-Horizon Tasks
- Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution
- Contextual Experience Replay for Self-Improvement of Language Agents
- AutoSkill: Experience-Driven Lifelong Learning via Skill Self-Evolution
- GUI-explorer: Autonomous Exploration and Mining of Transition-aware Knowledge for GUI Agent
- SkillClaw: Let Skills Evolve Collectively with Agentic Evolver
- Coarse-to-Fine Grounded Memory for LLM Agent Planning
- H2R: Hierarchical Hindsight Reflection for Multi-Task LLM Agents
- Memp: Exploring Agent Procedural Memory
- What Deserves Memory: Adaptive Memory Distillation for LLM Agents
- Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models
- SkillX: Automatically Constructing Skill Knowledge Bases for Agents
- WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance
- MobileGPT: Augmenting LLM with Human-like App Memory for Mobile Task Automation  

边界论文
- Get Experience from Practice: LLM Agents with Record & Replay  
- Mirage-1: Augmenting and Updating GUI Agent with Hierarchical Multimodal Skills  
- Meta-Policy Reflexion: Reusable Reflective Memory and Rule Admissibility for Resource-Efficient LLM Agent  
- Learning from Online Videos at Inference Time for Computer-Use Agents  

```
Dual-Granularity Experience Consolidation 所关注的，不仅是 agent 如何从单次 trajectory 中生成局部 reflection、summary、 lesson 或 episode memory，也不仅是系统如何从一批历史轨迹中离线归纳较稳定的经验，而是二者之间的持续衔接机制：新经验如何进入长期记忆，既有记忆又如何在后续交互中被重写、合并、筛选、压缩、分层或淘汰。沿着这一方向，较早的工作已开始将 episode-level 写入与 cross-episode 抽象联系起来。CLIN [Maj23] 从单次试错中提炼因果式经验表述，并进一步形成跨 episode 的 meta-memory；R2D2 [Hua25e] 从失败轨迹中生成可回放的修正性反思，并通过全局 replay buffer 与 reflective update 持续替换较弱的旧经验；MobileGPT [Lee23] 虽以 app memory 为核心表述，但其关键同样在于将分散的交互过程逐步沉淀为可跨任务复用的长期经验网络，而非仅保留彼此割裂的 episode 记录。

在此基础上，后续研究进一步把“局部写入—在线调用—长期整合”明确组织为一个闭环式经验生命周期。Learning on the Job [Yan25d] 先从局部成功子任务中写入可复用做法，再在任务完成后执行统一的去重、泛化与高层经验提炼；Remember Me, Refine Me [Cao25] 将单条轨迹转化为更紧凑的经验条目，并依据长期检索效用实施验证、保留与删除；Contextual Experience Replay [Liu25] 在生成新经验时显式参照已有 memory buffer，从而避免重复累积并使当前写入受历史记忆状态约束；What Deserves Memory [Ma25] 则将 episodic integration 与 semantic consolidation 区分处理，通过 merge、conflict resolution 与替换机制管理经验演化。与之相近，Agentic Context Engineering [Zha25f] 将单次交互中产生的局部增量经验持续写入可演化的 context playbook，Memp [Fan25] 通过 trajectory 与高层 script 的联动更新维持长期 procedural memory，H2R [Ye25b] 则把高层 planning insight 与低层 execution insight 统一纳入层级化 hindsight reflection 框架之中，共同体现出从孤立经验缓存走向持续性经验生态管理的趋势。

这一思路随后快速扩展到长时程 web、GUI 与开放环境中的 agent。GUI-explorer [Xie25] 从局部状态转移中抽取细粒度操作知识，并将其持续并入全局知识库；WebCoach [Liu25e] 将完整 session 压缩为 cross-session memory record，以支持后续任务中的经验引导；Darwinian Memory [Mi26b] 进一步引入基于效用、可靠性与时间衰减的记忆更新与淘汰机制，使长期 memory 具备更强的自调节能力；Coarse-to-Fine Grounded Memory [Yan25] 与 M2 [Yan26b] 都体现出“先写入局部轨迹经验，再在多轨迹层面提炼可迁移 insight”的总体思路，只是后者的跨轨迹整合更依赖离线构建的 insight bank。更近期的 AutoSkill [Yan26]、SkillClaw [Ma26b] 与 SkillX [Wan26] 则延续了相同方向：它们不再将每次交互仅仅视为一次性示例，而是将局部经验不断吸收到持续演化的长期知识库中，并通过版本更新、合并与筛选，使经验逐步由 episode-local observation 上升为更稳定的 cross-episode know-how。
```

## Narrative-to-Schematic Experience Transformation

Narrative-to-Schematic Experience Transformation 将 narrative tokenized agent experience 转化为具有显式结构约束的 schematic tokenized artifact。源经验来自 agent 序贯决策中产生的具体轨迹：tool-use trajectory、web navigation history、GUI interaction trace、mobile operation log、embodied execution record、multi-agent interaction history、reasoning-action trace 或 task failure episode。这些轨迹以自然语言、代码调用、界面操作、环境反馈或多模态 observation 的形式记录了 agent 在具体上下文中的观察、推理、行动与结果，是对 \(e=(c,a,o,f)\) 的离散序列化记录。

P2 的核心是将原始 narrative experience 形式化为可被解析、执行、遍历、实例化或调度的结构化 artifact。典型目标载体包括 executable code skill、API routine、parameterized action schema、workflow、DAG、hierarchical procedure、task tree、knowledge graph、episodic graph、environment map、state-transition graph 或 structured memory graph。这些 artifact 仍以 tokenized 形式存在，在后续决策中通过 retrieval、prompt injection、executor loading、graph traversal 或 workflow scheduling 被消费；它们不直接压缩为连续向量，也不通过训练固化进模型参数。

P2 与 P1 的关键区别在于结构是否在下游复用中发挥机制性作用。编号列表、自然语言 guideline、reflection、lesson 或 skill description 即使具有表面格式，只要后续 agent 主要依赖 language understanding 自由阅读，仍属 Narrative-to-Narrative Transformation。若经验被转化为可调用的代码函数、可实例化的 workflow、可检查 precondition/postcondition 的 procedure、可遍历的 graph，或可 grounding 到当前环境的 action schema，则属于 P2。

P2 方法的 artifact 形态差异很大，本文不按任务领域划分，而是按转化后 schematic artifact 在后续 agent 决策中的主要语义功能分为三类：Programmatic Skill Construction 将经验转化为可调用的动作单元；Procedural Workflow Induction 将经验转化为多步任务流程结构；Structured Memory Graph Construction 将经验转化为环境、状态或交互关系的图结构表示。一些方法产生的 artifact 介于 narrative 与 schematic 之间，或混合多种结构形式，作为 boundary cases 单独讨论。

对于图状 artifact，本文按其主要语义功能而非表面拓扑形态分类。若图主要编码任务执行顺序、步骤依赖、控制流或阶段结构，归入 Procedural Workflow Induction；若图主要编码实体、状态、空间关系、环境知识、情节记忆或交互历史，归入 Structured Memory Graph Construction。这一区分有助于避免将 workflow graph、memory graph 和 environment graph 混为一类。

### Programmatic Skill Construction

Programmatic Skill Construction 从具体 agent trajectories 中构建可调用、可执行或可参数化的技能单元，使 agent 在后续任务中直接调用这些技能，而非从低层动作开始重新规划。源经验通常是成功或经过筛选的执行轨迹，包含 agent 在环境中完成某类子任务时采取的动作序列、工具调用、界面操作、代码执行记录、环境反馈及错误修正过程。转化后的 artifact 表现为 code skill、Python function、JavaScript routine、Playwright API、symbolic program、parameterized action program、replayable action chain 或 callable skill interface。

这类方法的关键特征是，目标 artifact 主要承担”动作压缩”或”动作空间扩展”功能。原本需要多步低层操作完成的行为被抽象为一个高层可调用单元。后续 agent 在相似任务中不必重新生成完整操作序列，而是可以检索、实例化并调用已有 skill。与自然语言 skill description 不同，programmatic skill 的复用不完全依赖 LLM 的自由理解——它们通常可被 executor、runtime、browser automation framework、code interpreter 或 environment interface 直接执行。

许多 agent 失败并非因为缺乏高层任务理解，而是因为需要反复完成低层、繁琐且易出错的操作。若成功轨迹中的有效操作序列能被封装成可执行程序，agent 便能把曾经通过 trial-and-error 获得的经验转化为稳定的操作能力。随着 skill library 增长，agent 的有效 action space 也随之扩展：它不仅可以选择原始 primitive actions，还可选择由历史经验构建出的 composite actions。

Programmatic Skill Construction 通常包含若干关键步骤：从历史轨迹中筛选成功或高质量片段，避免将错误操作固化为 skill；对具体轨迹进行抽象，将任务绑定的变量、界面元素、对象名称或参数值泛化为可实例化的输入参数；生成可执行 skill body，并补充名称、描述、参数类型、适用条件、前置状态、后置效果或调用示例；许多方法还会通过 execution feedback、unit test、environment verification 或 iterative debugging 检查 skill 有效性后再写入 skill library。

这类方法的优势在于可执行性、可验证性和可组合性较强。artifact 是程序化或半程序化的，系统可以通过运行结果判断 skill 是否有效，也可在更复杂任务中组合多个 skill。与 raw trajectory retrieval 相比，programmatic skill 更短、更抽象，能直接介入行动层；与自然语言 reflection 相比，它不容易停留在”建议”层面。

局限也同样明显。programmatic skill 对环境接口稳定性高度敏感——网页结构、GUI 元素、API 参数或 embodied environment 状态变化时，原有 skill 可能失效。skill 的泛化边界难以确定：一个在特定页面、特定对象或特定任务中有效的程序，未必能安全迁移到表面相似的新情境。skill library 持续增长后容易出现重复技能、过时技能、依赖冲突和组合错误。Programmatic Skill Construction 往往需要配套的 skill selection、deduplication、versioning、testing、debugging 和 stale detection 机制。

论文：
- Voyager: An Open-Ended Embodied Agent with Large Language Models
- SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills
- WebXSkill: Skill Learning for Autonomous Web Agents
- Inducing Programmatic Skills for Agentic Tasks
- Evolving Programmatic Skill Networks
- MobileGPT: Augmenting LLM with Human-like App Memory for Mobile Task Automation
- Beyond Training: Enabling Self-Evolution of Agents with MOBIME
- AutoRefine: From Trajectories to Reusable Expertise for Continual LLM Agent Refinement

```
## Programmatic Skill Construction

Programmatic Skill Construction 的共同目标，不是把 trajectory 保留为可检索的 past episode，也不是把经验压缩成自然语言提示，而是将成功执行中稳定、可迁移的操作结构编译为可调用的高层技能单元，使 agent 在后续任务中能够直接调用这些技能，而不必从 primitive actions 重新展开完整规划 [Wan23c, Wan25d, Zhe25c, Wan26d]。这一路径的关键价值在于，经验被转化为可执行接口后，可以直接扩展 action space；同时，skill body 还能接受 execution-based verification、unit testing 和 environment-grounded debugging，因此比自然语言反思更容易形成稳定、可组合的复用能力 [Wan25d, Zhe25c, Shi26]。

一类代表性工作关注从成功轨迹中直接诱导 skill 并写入 skill library。Voyager [Wan23c] 将 Minecraft 中经过 environment feedback、execution error 和 self-verification 逐步打磨成功的 JavaScript action programs 沉淀为 executable skills，在新任务中按语义检索后作为高层代码组件复用。ASI [Wan25d] 则从 agent 自身成功的 web trajectories 中清洗出高质量 action subsequences，诱导出 parameterized Python skills，并要求用新 skill 重写原轨迹再重新执行，只有能够复现成功的 skill 才能入库，从而把 trajectory abstraction 与 execution-grounded re-verification 紧密结合。移动端的 MobileGPT [Lee23] 体现了相近思路，只是其产物更接近 parameterized routine 和 replayable action chain：系统将 app interaction history 组织为 transition graph，并把 sub-task 存成可实例化的 function-call style memory，以压缩低层 GUI 操作。

另一类工作进一步把 skill construction 推进为持续的 discovery、practice 与 refinement 流程。SkillWeaver [Zhe25c] 让 web agent 通过自提出任务和反复 practice 收集成功轨迹，再把 state-action sequences 抽象为带 generalized parameters 的 Python plus Playwright APIs，并通过 unit tests、execution feedback 和 iterative debugging 持续修补这些 API。WebXSkill [Wan26d] 则更强调 environment grounding：它从 synthetic web trajectories 中抽取可复用 action subsequences，编译为带 typed parameters、element references 与 step-level guidance 的 JSON skills，并按 URL pattern 组织为 skill graph，使 artifact 既可被 runtime 直接执行，也可作为高层模板供 agent 自适应展开。

更近期的工作开始把重点从“生成单个 skill”转向“维护持续增长的 skill ecology”。PSN [Shi26] 将 skill 表示为带 explicit preconditions、postconditions 和 subskill dependency 的 symbolic programs，并允许系统在长期任务流中对这些技能进行组合、修补、抽象与重构。MOBIMEM [Liu25i] 在 mobile agent 中把 trajectories 与 user corrections 编译为 multi-level experience templates、ActTree 和 ActChain，并通过 exception-driven updating 与 stale detection 持续修正旧经验。AutoRefine [Qiu26] 则从成功与失败轨迹的对比分析中抽取 skill patterns 与 subagent patterns，将复杂子任务封装为可调用的 reusable expertise。总体来看，这一方向的挑战已不再只是如何从 trajectory 编译出 skill，而 increasingly 在于后续的 selection、deduplication、debugging 和 versioned evolution [Shi26, Liu25i, Qiu26]。
```

### Procedural Workflow Induction

Procedural Workflow Induction 从多步 agent trajectories 中归纳可复用的任务流程结构：workflow、DAG、hierarchical procedure、task tree、stage-action hierarchy、procedural memory 或 workflow template。这类方法关注的不是把某一段动作封装成单个可调用 skill，而是抽象出完成一类任务所需的阶段划分、步骤顺序、依赖关系、控制流、条件分支、前置条件和后置状态。

源经验通常是完整任务执行轨迹，包含 agent 如何理解任务、分解目标、按什么顺序调用工具或执行操作、在何处根据观察调整策略，以及最终如何达到成功或失败状态。转化后的 artifact 保留任务执行的过程结构，使后续 agent 能按该结构进行 planning、retrieval、instantiation、checking 或 execution。

许多复杂任务的可复用经验并不体现在某个孤立动作中，而体现在任务执行过程的组织方式中。成功轨迹往往包含稳定的阶段模式——先收集信息，再筛选候选项，再验证约束，最后执行提交；失败轨迹也可能揭示步骤顺序、依赖检查或条件判断的缺失。通过从轨迹中归纳 workflow，agent 获得一种比单步 skill 更高层的 procedural scaffold，用于指导未来任务的整体执行。

这类 artifact 的 schematic 性体现在显式过程结构上。一个 workflow 或 procedure 包含多个节点，每个节点对应一个子任务、工具调用、动作阶段、状态检查或决策点；边表示时间顺序、数据依赖、控制依赖、条件跳转或并行关系。一些方法还会为节点附加 precondition、postcondition、input/output schema、tool specification、exception handling rule 或 confidence score。后续 agent 可根据当前任务检索相似 workflow，实例化变量，检查当前状态是否满足前置条件，并按 workflow 的阶段结构逐步执行。

与 Programmatic Skill Construction 相比，Procedural Workflow Induction 的粒度更高。前者把经验转化为可调用动作单元，强调 executable skill；后者把经验转化为任务流程结构，强调 task-level control flow。一个程序化 skill 可以是 workflow 中的一个节点，一个 workflow 可以调度多个 skill、工具或子任务，两者可以组合使用。在 taxonomy 中，若 artifact 主要扩展 action space，归入 Programmatic Skill Construction；若 artifact 主要组织多步任务执行过程，归入 Procedural Workflow Induction。

这类方法的优势在于可解释性和可控性较强。相比直接检索 raw trajectories，workflow artifact 更短、更抽象、更易定位任务中的关键阶段。相比自然语言总结，workflow 显式表达步骤依赖、执行顺序和状态检查，更适合 long-horizon task planning、tool-use orchestration、web navigation、mobile automation 和 multi-stage reasoning tasks。workflow 还可帮助 agent 避免遗漏必要步骤，减少重复探索，并在失败时定位出问题的阶段。

主要挑战在于抽象粒度控制。workflow 过于具体则退化为对历史轨迹的浅层回放，难以泛化到新任务；过于抽象则可能丢失关键上下文、工具约束或状态条件。workflow induction 需要判断哪些步骤是任务本质结构，哪些只是偶然路径——依赖单条轨迹容易产生错误归因，依赖多条轨迹又需要解决轨迹对齐、步骤聚类、变量泛化和冲突合并等问题。

另一个问题是 workflow drift：网页、软件、工具接口或环境状态变化后，原先有效的 workflow 可能不再适用。高质量的 Procedural Workflow Induction 通常需要配套 consistency checking、precondition verification、workflow rewriting、merge、deduplication 和 update 机制。长期来看，这类方法的关键不只是生成 workflow，而是维护一个可增长、可修订、可验证的 procedural memory。

论文：
- WorkflowGen: an adaptive workflow generation mechanism driven by trajectory experience
- FlowMind: Execute-Summarize for Structured Workflow Generation from LLM Reasoning
- Enhancing Web Agents with a Hierarchical Memory Tree
- Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement
- Beyond Training: Enabling Self-Evolution of Agents with MOBIME
- Environment Maps: Structured Environmental Representations for Long-Horizon Agents
- Agent Workflow Memory
- Skill-Pro: Learning Reusable Skills from Experience via Non-Parametric PPO for LLM Agents

```
Procedural Workflow Induction 关注将 agent 在长程任务中的交互经验转化为可复用的过程结构，使后续系统复用的不再是原始 trajectories 本身，而是其中较稳定的阶段划分、步骤顺序、依赖关系与状态约束。与将经验封装为单个 callable skill 的方法不同，这一方向强调 task-level control flow 的抽象，即将经验编译为能够支持 planning、instantiation、checking 与 execution 的 procedural scaffold [Wan24, Wei26, Liu26, Tan26, For25, Liu25i, Fen26]。

现有 large model based agent 工作大体呈现出一条由浅入深的演进脉络。较早一类方法直接从多步执行轨迹中归纳 workflow 模板，用抽象步骤序列替代对历史示例的逐段模仿。Agent Workflow Memory 从 web trajectories 中提取重复出现的 routines，并通过槽位化去除实例细节，使 workflow 成为可跨任务检索与复用的过程记忆 [Wan24]。WorkflowGen 进一步将历史执行经验组织为 generalized workflow templates，并根据当前任务与既有经验的匹配程度，在直接复用、局部重写与重新生成之间自适应切换，从而把 workflow reuse 明确提升为一种受经验驱动的控制机制 [Wei26]。与此不同，FlowMind 强调将任务求解与结构抽象解耦，先通过执行获得 reasoning and tool traces，再在独立阶段中将其重建为显式 workflow graph，从而提高复杂控制流归纳的稳定性 [Liu26]。

在此基础上，后续工作开始强调 workflow 的层级化表示及其在新环境中的可对齐性。Hierarchical Memory Tree 将 web experience 重写为 intent, stage, action 三层结构，并在 stage 层显式引入 pre-condition 与 post-condition，使 agent 能够依据当前观测判断所处阶段，再将抽象动作映射到具体页面，从而缓解跨站点场景中的 workflow mismatch [Tan26]。MACLA 则把交互经验压缩为带 goal, precondition, abstract action sequence, and postcondition 的 procedures，并进一步组合出更高层的 meta-procedures；其关键推进在于，procedure 不再只是静态存储项，而成为可被选择、比较、修订与维护的层级 procedural memory [For25]。类似地，MOBIMEM 将 execution logic 提炼为带参数槽位和依赖关系的 multi-level templates，使 workflow induction 成为更大规模 memory-centric agent architecture 的组成部分，而非单独的检索模块 [Liu25i]。

另一条值得注意的趋势，是将 workflow 视为环境结构化表征中的一个组成层次，而不仅是单个任务模板。Environment Maps 将 screen recordings 与 execution traces 编译为持久化的环境表示，在 contexts、parameterized actions 与 tacit knowledge 之外显式保留 observed workflows，从而使过程结构成为 long-horizon planning 与 environment interaction 的可查询对象 [Fen26]。相比之下，Skill-Pro 虽然同样从经验中归纳多步 procedural units，并显式描述 activation, execution, and termination conditions，但其最终产物是可调用 skill pool，而非用于组织整类任务执行的 workflow structure，因此更适合作为 Programmatic Skill Construction 的边界案例，而非 Procedural Workflow Induction 的核心成员 [Mi26]。

总体来看，这一方向的关键进展不在于单纯“记住更多经验”，而在于从经验中提炼出更稳定、更显式、也更易维护的过程组织形式。随着 agent 任务从短程单轮决策走向跨页面、跨工具、跨阶段的长程执行，workflow-like artifact 正逐渐成为连接 trajectory experience 与 future control 的重要中间表示 [Wan24, Tan26, For25, Fen26]。

```
 
### Structured Memory Graph Construction

Structured Memory Graph Construction 将 agent trajectories 中出现的实体、关系、状态变化、空间结构、事件依赖或交互历史转化为可检索、可遍历、可更新的图结构记忆。这类方法的目标不是直接生成可执行动作，也不是主要归纳任务流程，而是构建 agent 对环境、任务世界、历史经验或多智能体交互关系的结构化表示。

源经验来自 agent 与环境的持续交互：text-game exploration、embodied navigation、web interaction、mobile operation、multi-agent collaboration 或 long-horizon task execution。轨迹中包含 agent 观察到的对象、位置、状态、事件、动作后果、用户偏好、任务上下文、角色关系或历史对话。转化后的 artifact 表现为 knowledge graph、episodic graph、semantic graph、scene graph、spatial-object graph、state-transition graph、interaction graph、query graph、environment map 或 world model graph。

agent 的许多经验不适合被表达为线性文本或固定流程，而更适合组织为关系结构。环境中的对象之间有空间关系，动作会改变状态，历史事件之间存在时间或因果联系，多智能体交互中存在角色、任务、信息流和依赖关系。若这些关系仅以 raw logs 或自然语言 memory notes 存储，后续 agent 很难进行精确检索、局部更新和多跳推理。图结构 memory 提供了一种更适合组织关系经验的 schematic carrier。

这类 artifact 的 schematic 性体现在节点、边和属性的显式结构。节点可表示对象、地点、状态、事件、任务、角色、查询、记忆片段或环境上下文；边可表示 spatial relation、temporal relation、causal relation、state transition、interaction dependency、semantic relation 或 memory linkage。后续 agent 可基于图结构进行 retrieval、subgraph selection、neighbor expansion、graph traversal、world-state checking 或 structured prompting。一些系统还会维护 outdated fact removal、edge confidence、memory decay、utility score 或 graph pruning，避免图记忆持续膨胀或被过时信息污染。

Structured Memory Graph Construction 与 Procedural Workflow Induction 的区别在于图的语义功能。Workflow graph 回答”任务应该如何执行”，其节点和边表示步骤顺序、控制流或任务依赖；memory graph 回答”环境中有什么、状态如何变化、历史经验之间有什么关系”，其节点和边表示实体、状态、事件、空间、语义或交互关系。不能仅凭 artifact 是否是 graph 归类。若图的主要作用是调度任务步骤，归入 Procedural Workflow Induction；若图的主要作用是存储和检索结构化环境知识或经验关系，归入 Structured Memory Graph Construction。

这类方法的优势在于支持关系级别的记忆复用。相比 raw trajectory retrieval，图结构可减少无关上下文，使 agent 聚焦于当前决策所需的实体、状态或关系。相比自然语言 summary，图结构更容易局部更新：当某对象位置变化、某条关系失效或某段交互结果被新证据覆盖时，系统可修改相关节点或边，不必重写整段记忆。对于 embodied agents、text-game agents、web agents 和 multi-agent systems，这种结构化 memory 有助于 long-horizon planning、state tracking 和 context reconstruction。

困难也同样存在。图抽取过程容易产生错误实体、错误关系或过度细碎的节点，在 observation 噪声较大或环境状态快速变化时尤其明显。图结构虽然适合存储关系，但许多 LLM agent 最终仍需将子图序列化为 prompt，这可能削弱 graph traversal 的优势。图记忆随时间增长后可能出现 memory bloat、过时信息、重复节点、冲突边和 retrieval noise。这类方法通常需要 graph update、conflict resolution、pruning、confidence estimation 和 retrieval control 机制。

论文：
- AriGraph: Learning Knowledge Graph World Models with Episodic Memory for LLM Agents
- G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems
- Environment Maps: Structured Environmental Representations for Long-Horizon Agents
- BrainMem: Brain-Inspired Evolving Memory for Embodied Agent Task Planning
- Beyond Training: Enabling Self-Evolution of Agents with MOBIME
- A-MEM: Agentic Memory for LLM Agents

```

Structured Memory Graph Construction 的关键，不在于产物表面上是否是 graph，而在于它将 agent 在持续交互中积累的经验，从线性的 trajectory、对话日志或自然语言 memory notes，转化为可显式操作的关系结构，使系统能够围绕实体、事件、状态与交互依赖进行检索、更新与推理。与 raw trajectory retrieval 相比，这类方法试图直接保存经验中的 relational structure，从而减少后续决策时无关上下文的干扰，并支持局部修改与多跳访问。AriGraph [Ano24] 是这一思路的代表，它在 text-game 场景中将每一步文本观测抽取为 semantic triplets，并进一步与按时间组织的 episodic nodes 相连，形成同时编码世界知识与情节历史的 knowledge graph world model；当环境状态变化时，系统还会删除被新观测推翻的旧关系，使图记忆能够随交互持续演化，而不是停留在静态知识存储。

这一思路随后被推广到更复杂的交互关系建模中。G-Memory [Zha25] 面向 multi-agent systems，将协作中的 utterance、task query 与 distilled insight 组织为三层层次化图记忆，使系统能够在细粒度交互证据与高层协作经验之间双向追踪；其核心不是归纳任务执行步骤，而是沉淀多智能体协作过程中形成的角色关系、任务关联与经验依赖。进一步地，MOBIMEM [Liu25i] 将结构化记忆扩展为更完整的 self-evolving memory substrate：它一方面用 DisGraph 组织 user profile 中的概念与实体关系，另一方面把任务经验表示为 DAG-like templates，并结合动作级结构支持复用与更新，从而把 profile understanding、experience reuse 与 self-evolution 统一到同一套结构化记忆框架中。相比之下，A-MEM [Xu25b] 采用了更开放的 graph-like memory form，将交互经验拆解为带有关键词、标签、上下文描述与相互链接的 atomic notes，并通过 LLM 持续生成和修订 note 之间的连接，使记忆网络能够随新经验不断重组。整体来看，这些方法虽然结构约束程度不同，但共享同一转化逻辑：它们都不满足于把经验保存为可读文本，而是试图把经验中的关系性内容外化为 schematic memory，以支持更精确的 retrieval、局部更新与跨时间的结构化复用。
```

### Other Schematic Artifacts and Boundary Cases

除上述三类外，还有一些方法产生的 artifact 具有一定结构化特征，但难以稳定归入某一个 P2 家族，它们通常处于 P2 与 P1、P7、Composite 或非 agent setting 的边界上。本文将其作为 Other Schematic Artifacts and Boundary Cases 单独讨论。

第一类边界情况是 semi-structured narrative artifacts。一些方法将轨迹总结为 workflow、skill、SOP、procedure 或 guideline，这些 artifact 虽在表面上具有编号、字段或步骤结构，下游消费时仍主要依赖 LLM 的自然语言理解，无 parser、executor、workflow engine 或 graph traversal module 介入。这类方法更接近 Narrative-to-Narrative Transformation，可作为边界案例澄清”structured text”并不必然等于 schematic artifact。

第二类边界情况是 hybrid schematic-narrative artifacts。一些方法同时产生 code snippets、subagent patterns、natural-language guidelines、memory notes 或 semi-structured procedures，部分具备可执行或可解析结构，部分主要是 narrative advice。对这类方法，不能简单按论文术语整体归类，而应分析其核心贡献和主要消费机制。若系统的关键能力来自 executable skill、workflow schema 或 graph memory，可作为 P2 的混合案例；若结构化部分只是辅助说明，核心复用仍依赖自然语言提示，则应归入 P1 或 boundary discussion。

第三类边界情况是 source-side ambiguity。某些方法确实生成了 code、workflow 或 graph 等 schematic artifacts，但这些 artifacts 并非从具体 agent trajectories 中提炼，而是由模型根据任务描述、专家知识、静态文档或参数化能力直接生成。这类工作在目标 artifact 上看似接近 P2，但 transformation direction 并非 Narrative-to-Schematic，而更接近 Parametric-to-Tokenized externalization 或一般的 program/workflow synthesis。P2 纳入标准必须同时检查 source experience 和 target artifact，不能只看产物是否结构化。

第四类边界情况是 composite pipelines。有些系统先将 trajectory 转化为 schematic artifact，再将这些 artifact 用于数据合成、SFT、RL 或 policy update。若论文的核心贡献是从经验到参数的内化，schematic artifact 只是中间表示，则更适合归入 Composite 或 Tokenized-to-Parametric pathway。P2 章节可引用这些方法说明 schematic artifact 的中介作用，但不作为纯 P2 方法。

第五类边界情况是 non-agent traces。一些工作从 human demonstrations、system logs、screen recordings 或 creative software traces 中构建 workflow graph 或 action graph。这些 artifact 可能高度 schematic，也可能对 agent design 有启发，但若源数据不是 LLM-based agent 在序贯决策中产生的 experience loop，则不完全满足本文对 agent experience transformation 的定义。它们可作为相关背景或外部启发，不直接纳入 P2 主 taxonomy。

设置这一小节目的不是扩大 P2 范围，而是明确 P2 的边界。P2 的判定需同时满足三个条件：输入必须是具体 agent trajectory 或 interaction log；输出必须是具有可解析、可执行或可遍历结构的 schematic artifact；下游复用必须利用这种结构，而非仅让 LLM 自由阅读文本。三点同时满足，才构成严格意义上的 Narrative-to-Schematic Experience Transformation。

论文：
- Agent Workflow Memory
- Skill-Pro: Learning Reusable Skills from Experience via Non-Parametric PPO for LLM Agents
- AutoRefine: From Trajectories to Reusable Expertise for Continual LLM Agent Refinement
- A-MEM: Agentic Memory for LLM Agents
- From Logs to Agents: Reconstructing High-Level Creative Workflows from Low-Level Raw System Traces
- Workflow Graphs: A Computational Model of Collective Task Strategies for 3D Design Software
- Meta-Agent-Workflow: Streamlining Tool Usage in LLMs through Workflow Construction, Retrieval, and Refinement
- A²Flow: Automating Agentic Workflow Generation via Self-Adaptive
- In-Context Ensemble Learning from Pseudo Labels Improves Video-Language Models for Low-Level Workflow Understanding