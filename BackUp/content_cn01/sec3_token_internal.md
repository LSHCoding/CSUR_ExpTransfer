# Tokenized-to-Tokenized Transformations


## Narrative-to-Narrative Experience Transformation

第一类转化路径是 Narrative-to-Narrative Experience Transformation，即将 narrative tokenized agent experience 转化为更高层的 narrative artifact。这里的源经验通常来自 agent 在序贯决策过程中产生的具体轨迹，例如 task execution log、reasoning trace、tool-use trajectory、web navigation history、GUI interaction trace、robot execution record、multi-turn dialogue history 或 failure episode。这些轨迹记录了 agent 在特定上下文下如何观察、推理、行动并接收环境反馈，因此可以被视为对 \(e=(c,a,o,f)\) 的自然语言或多模态序列化记录。

P1 路径的目标不是改变经验的载体层级，而是在 narrative tokenized 层内部完成抽象、压缩、重写或归纳。转化后的 artifact 仍然是弱形式化的 tokenized 表达，例如 reflection、summary、lesson、failure explanation、heuristic、guideline、insight、mistake pattern、natural-language skill、manual entry 或 experience note。它们通常通过 retrieval-augmented prompting 或 direct prompt injection 被后续 agent 消费，而不是被 parser、executor、graph traversal module 或训练过程直接处理。

因此，这一路径与 Narrative-to-Schematic Transformation 有明确区别。即使目标 artifact 表面上呈现为编号列表、规则集合或 skill description，只要其下游复用仍依赖 language understanding，而不是依赖专门的执行器、解析器或结构化遍历机制，它仍然属于 P1。相反，如果经验被转化为 code、workflow、decision tree、knowledge graph、action schema、API routine 或可执行 procedure，则应归入 P2。P1 也不同于 Parametric-to-Tokenized externalization：P1 的输入必须是具体 agent trajectory 或 interaction log，而不是模型仅凭参数知识生成的 guideline 或 instruction。

由于不同论文常常使用 reflection、memory、skill、guideline、insight 等术语指代机制上并不相同的对象，本文不按照 artifact 的表面名称组织 P1 方法。相反，我们按照经验抽象所依赖的轨迹粒度来划分这一类方法：Per-Trajectory Experience Abstraction 主要从单条轨迹中抽象局部经验；Cross-Trajectory Experience Induction 从多条轨迹中归纳共性规律；Dual-Granularity Experience Consolidation 则同时包含单轨迹写入与跨轨迹整合，使 narrative memory 随交互持续演化。


### Per-Trajectory Experience Abstraction

Per-Trajectory Experience Abstraction 指的是以单条 agent trajectory、episode、trial 或局部 execution log 为主要输入，将一次具体执行经验抽象为更高层的自然语言经验 artifact。这类方法通常在任务结束、失败发生、环境反馈返回或一次 trial 完成后触发，通过 reflection、summarization、critique、failure explanation 或 hindsight rewriting 等方式，把原始轨迹压缩为可在后续任务中复用的文本经验。

这类 artifact 可以表现为 episode-level reflection、trajectory summary、failure diagnosis、lesson learned、hindsight note、local tip 或 correction suggestion。它们的共同点不是名称，而是来源粒度：artifact 主要由单条轨迹内部的信息抽象而来。换言之，方法关注的是如何从一次具体经历中提炼出对下一次决策有帮助的局部经验。

这类方法的基本思想是，单次执行轨迹本身已经包含可复用的经验信号。一次失败轨迹可能揭示错误假设、无效动作、遗漏约束或不恰当的工具调用；一次成功轨迹也可能包含有效的分解策略、搜索路径或环境交互模式。通过语言模型对这些轨迹进行事后解释和压缩，agent 可以把原本冗长、低层、任务绑定的历史记录转化为更短、更抽象、更容易注入上下文的经验描述。

Per-Trajectory Experience Abstraction 的主要优势是反应快、成本相对低，并且不依赖大量历史数据。它特别适合 trial-and-error setting、online adaptation 和任务分布较窄的场景。在这些场景中，agent 只需要从最近一次失败或成功中提取经验，就可能在下一次尝试中避免重复错误或复用有效策略。

然而，这类方法的局限也很明显。由于抽象主要依赖单条轨迹，它容易受到偶然因素和错误归因的影响。一次失败并不一定意味着其中所有动作都是错误的，一次成功也不一定说明其中所有策略都具有泛化性。如果 reflection 或 failure explanation 将偶然现象误写成通用经验，后续 agent 可能会被误导。此外，单轨迹 artifact 通常与原始任务上下文绑定较强，因此跨任务迁移能力有限。它更适合作为局部 adaptation 的机制，而不是稳定经验规律的来源。

论文：
- Reflexion: Language Agents with Verbal Reinforcement Learning
- Reflection-Based Memory For Web Navigation Agents
- REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction
- MemOrb: A Plug-and-Play Verbal-Reinforcement Memory Layer for E-Commerce Customer Service
- Sample-Efficient Online Learning in LM Agents via Hindsight Trajectory Rewriting
- Self-Generated In-Context Examples Improve LLM Agents for Sequential Decision-Making Tasks  


### Cross-Trajectory Experience Induction

Cross-Trajectory Experience Induction 指的是以多条 trajectories、demonstrations、rollouts、failure cases 或 historical interactions 为输入，通过比较、聚类、筛选、合并或归纳，抽取更稳定、更通用、更可迁移的 narrative artifact。与单轨迹方法不同，这类方法并不满足于解释某一次执行为什么成功或失败，而是试图从多次经验中发现反复出现的模式。

这类 artifact 可以表现为 rule、guideline、heuristic、insight、do-and-don't list、mistake pattern、natural-language skill、manual entry 或 procedural tip。它们的共同点是：目标经验不是单条轨迹的直接摘要，而是跨多条轨迹归纳得到的共性知识。例如，多个失败轨迹可能共同暴露一种错误操作模式；多个成功轨迹可能共享某种有效的任务分解策略；不同任务中的相似交互片段也可能被抽象为可迁移的 natural-language skill。

Cross-Trajectory Experience Induction 的核心思想是，可迁移经验通常来自多次执行之间的稳定结构，而不是来自单次执行中的偶然片段。通过对成功与失败轨迹进行对比，方法可以识别哪些行为与任务完成更相关，哪些错误在不同上下文中反复出现，哪些约束或策略具有更强的跨任务适用性。由此得到的 artifact 往往比单条 reflection 更抽象，也更接近 agent 可长期复用的经验规律。

这类方法的主要优势是泛化能力更强。由于 artifact 来自多条经验之间的归纳，它更有可能过滤掉单次轨迹中的偶然噪声，并保留在多个任务或多个 episode 中稳定出现的有效模式。因此，Cross-Trajectory Experience Induction 适合用于构建 rule bank、guideline library、mistake notebook、experience bank 或 natural-language skill repository，并在新任务中通过检索或条件选择进行复用。

不过，这类方法也引入了新的挑战。首先，它通常需要积累足够多的轨迹，因此冷启动能力弱于单轨迹抽象。其次，多轨迹归纳存在过度抽象风险：模型可能把特定环境中的局部规律错误地上升为通用规则。第三，不同轨迹可能支持相互冲突的经验结论，例如某一策略在一个任务中有效、在另一个任务中失败。若缺少冲突检测、适用条件建模或经验筛选机制，归纳后的 artifact 可能变得含混、冗余甚至相互矛盾。因此，这类方法往往需要额外关注经验选择、聚类质量、规则适用范围和 artifact 一致性。

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



### Dual-Granularity Experience Consolidation

Dual-Granularity Experience Consolidation 指的是同时包含单轨迹层面的经验写入与多轨迹层面的经验整合的方法。系统通常先从每条新 trajectory 中抽取局部 reflection、summary、lesson 或 episode memory，再随着交互经验不断积累，对这些局部 artifact 进行合并、去重、重写、压缩、筛选、层级化、淘汰或版本更新，从而形成持续演化的 narrative memory store。

这类方法的核心问题不只是“如何从一次经验中生成一个 artifact”，也不只是“如何从一批轨迹中归纳一组规则”，而是如何连接这两个过程：新的单次经验如何进入长期记忆，已有记忆如何被更新，重复或低价值经验如何被合并或删除，过时经验如何被淘汰，局部 episode memory 如何逐渐上升为更稳定的 cross-episode insight 或 procedural memory。

Dual-Granularity Experience Consolidation 的基本思想是，agent experience 应被视为持续生长的记忆生态，而不是一次性生成的静态文本。每次交互都会产生新的局部经验，但这些经验如果只是简单累积，会导致 memory store 冗余、噪声增加、检索困难和上下文污染。因此，这类方法通常会引入 memory controller、retriever、refiner、utility scorer、consolidator 或 forgetting mechanism，对经验 artifact 的生命周期进行管理。

这类方法的优势在于能够同时兼顾快速适应与长期积累。单轨迹写入使 agent 可以及时吸收最近经验，跨轨迹整合则使系统能够逐渐形成更稳定、更紧凑、更可迁移的经验结构。相比只做 episode-level reflection 的方法，Dual-Granularity 方法更适合 long-horizon tasks、cross-session interaction、continual learning 和 open-ended agent deployment。相比一次性的 batch induction，它又更强调在线更新和长期维护，使 memory 能够随任务分布和环境反馈变化而持续调整。

但 Dual-Granularity Experience Consolidation 也是 P1 中边界最复杂的一类。一方面，随着 memory store 变得更加结构化，方法可能逐渐接近 P2：如果经验被组织为可执行 workflow、formal procedure、knowledge graph、API schema 或 hard rule checker，那么目标载体已经不再是单纯的 narrative tokenized artifact。另一方面，若系统把 narrative artifact 进一步用于 fine-tuning、reward model training 或 policy update，则整体方法可能构成 Composite pipeline，而 P1 只是其中一个子步骤。因此，在讨论这类方法时，需要明确区分 narrative memory 的生成与维护机制、结构化执行机制以及后续参数化学习机制之间的边界。

总体而言，Dual-Granularity Experience Consolidation 代表了 P1 路径中更系统化的发展方向。它将单次经验抽象、多次经验整合和长期记忆管理连接起来，使 agent 能够从孤立的 execution logs 中逐步构建可持续复用的 narrative experience store。然而，其有效性不仅取决于 artifact 生成质量，也取决于 memory selection、retrieval、consolidation、conflict resolution 和 staleness handling 等管理机制。

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
  - 注：如果其 app memory 主要是可 replay / executable procedure，则应转入 P2 或 Composite。
- Get Experience from Practice: LLM Agents with Record & Replay  
  - 注：record-and-replay 机制较强，若包含 workflow/check function，应优先放入 P2 或 Composite。
- Mirage-1: Augmenting and Updating GUI Agent with Hierarchical Multimodal Skills  
  - 注：若 hierarchical skills 被结构化搜索或执行模块消费，则更接近 P2/Composite。
- Meta-Policy Reflexion: Reusable Reflective Memory and Rule Admissibility for Resource-Efficient LLM Agent  
  - 注：由于包含 rule admissibility / hard rule checking，建议主归 P2 或 Composite，仅作为 P1 边界案例。
- Learning from Online Videos at Inference Time for Computer-Use Agents  
  - 注：更接近 video-to-demonstration / structured trajectory reuse，建议作为 P2 或 raw demonstration reuse 边界案例。

## Narrative-to-Schematic Experience Transformation

第二类转化路径是 Narrative-to-Schematic Experience Transformation，即将 narrative tokenized agent experience 转化为具有显式结构约束的 schematic tokenized artifact。这里的源经验通常来自 agent 在序贯决策过程中产生的具体轨迹，例如 tool-use trajectory、web navigation history、GUI interaction trace、mobile operation log、embodied execution record、multi-agent interaction history、reasoning-action trace 或 task failure episode。这些轨迹以自然语言、代码调用、界面操作、环境反馈或多模态 observation 的形式记录了 agent 在具体上下文中如何观察、推理、行动并接收结果，因此可以被视为对 \(e=(c,a,o,f)\) 的离散序列化记录。

P2 路径的核心不是简单压缩或总结轨迹，而是将原始 narrative experience 形式化为可被解析、执行、遍历、实例化或调度的结构化 artifact。典型目标载体包括 executable code skill、API routine、parameterized action schema、workflow、DAG、hierarchical procedure、task tree、knowledge graph、episodic graph、environment map、state-transition graph 或 structured memory graph。这些 artifact 仍然以 tokenized 形式存在，并在后续决策中通过 retrieval、prompt injection、executor loading、graph traversal 或 workflow scheduling 被消费；它们不被直接压缩为连续向量，也不通过训练固化进模型参数。

因此，P2 与 P1 的关键区别不在于 artifact 是否“看起来有结构”，而在于这种结构是否在下游复用中发挥机制性作用。编号列表、自然语言 guideline、reflection、lesson 或 skill description 即使具有表面格式，只要后续 agent 主要依赖 language understanding 自由阅读，它们仍属于 Narrative-to-Narrative Transformation。相反，如果经验被转化为可以调用的代码函数、可实例化的 workflow、可检查 precondition/postcondition 的 procedure、可遍历的 graph，或可 grounding 到当前环境的 action schema，则属于 P2。

P2 也不同于 Parametric-to-Tokenized externalization。P2 的输入必须是具体的 agent trajectory、execution log 或 interaction record，模型在其中扮演 abstractor、formalizer 或 synthesizer 的角色；如果 artifact 主要由模型根据任务描述或内化知识直接生成，而没有具体轨迹作为输入，则更接近 Parametric-to-Tokenized pathway。此外，如果 schematic artifact 只是后续 SFT/RL 的中间数据预处理，而论文的核心贡献是把经验内化进 policy parameters，则应归入 Composite 或 Tokenized-to-Parametric pathway，而不是纯 P2。

由于 P2 方法的 artifact 形态差异很大，本文不按照任务领域划分这一类方法。Web、GUI、mobile、embodied、tool-use 和 multi-agent 只是应用场景，不能作为 taxonomy 的主轴。我们按照转化后 schematic artifact 在后续 agent 决策中的主要语义功能，将 P2 方法划分为三类：Programmatic Skill Construction 将经验转化为可调用的动作单元；Procedural Workflow Induction 将经验转化为多步任务流程结构；Structured Memory Graph Construction 将经验转化为环境、状态或交互关系的图结构表示。除此之外，一些方法产生的 artifact 介于 narrative 与 schematic 之间，或同时混合多种结构形式，本文将其作为 boundary cases 单独讨论。

对于图状 artifact，本文按照其主要语义功能而不是表面拓扑形态进行分类。若图主要编码任务执行顺序、步骤依赖、控制流或阶段结构，则归入 Procedural Workflow Induction；若图主要编码实体、状态、空间关系、环境知识、情节记忆或交互历史，则归入 Structured Memory Graph Construction。这个区分有助于避免将所有 workflow graph、memory graph 和 environment graph 混为一类。

### Programmatic Skill Construction

Programmatic Skill Construction 指的是从具体 agent trajectories 中构建可调用、可执行或可参数化的技能单元，使 agent 能够在后续任务中直接调用这些技能，而不是重新从低层动作开始规划。这类方法的源经验通常是成功或经过筛选的执行轨迹，其中包含 agent 在环境中完成某类子任务时采取的动作序列、工具调用、界面操作、代码执行记录、环境反馈以及错误修正过程。转化后的 artifact 通常表现为 code skill、Python function、JavaScript routine、Playwright API、symbolic program、parameterized action program、replayable action chain 或 callable skill interface。

这类方法的关键特征是，目标 artifact 主要承担“动作压缩”或“动作空间扩展”的功能。原本需要多步低层操作完成的行为，被抽象为一个高层可调用单元。后续 agent 在相似任务中不必重新生成完整操作序列，而是可以检索、实例化并调用已有 skill。与自然语言 skill description 不同，programmatic skill 的复用不完全依赖 LLM 的自由理解，而是通常可以被 executor、runtime、browser automation framework、code interpreter 或 environment interface 直接执行。

这一路线的基本思想是，许多 agent 失败并不是因为缺乏高层任务理解，而是因为需要反复完成低层、繁琐且容易出错的操作。如果成功轨迹中的有效操作序列能够被封装成可执行程序，agent 就可以把曾经通过 trial-and-error 获得的经验转化为稳定的操作能力。随着 skill library 增长，agent 的有效 action space 也随之扩展：它不仅可以选择原始 primitive actions，还可以选择由历史经验构建出来的 composite actions。

Programmatic Skill Construction 通常包含若干关键步骤。首先，系统需要从历史轨迹中筛选出成功或高质量片段，避免把错误操作固化为 skill。其次，系统需要对具体轨迹进行抽象，将任务绑定的变量、界面元素、对象名称或参数值泛化为可实例化的输入参数。第三，系统需要生成可执行 skill body，并为其补充名称、描述、参数类型、适用条件、前置状态、后置效果或调用示例。最后，许多方法还会通过 execution feedback、unit test、environment verification 或 iterative debugging 检查 skill 的有效性，然后才将其写入 skill library。

这类方法的优势在于可执行性、可验证性和可组合性较强。由于 artifact 是程序化或半程序化的，系统可以通过运行结果判断 skill 是否有效，也可以在更复杂任务中组合多个 skill。与 raw trajectory retrieval 相比，programmatic skill 更短、更抽象，并且能够直接介入行动层；与自然语言 reflection 相比，它更不容易停留在“建议”层面，而是转化为实际可调用能力。

然而，这类方法也有明显局限。首先，programmatic skill 对环境接口稳定性高度敏感。网页结构、GUI 元素、API 参数或 embodied environment 状态发生变化时，原有 skill 可能失效。其次，skill 的泛化边界难以确定：一个在特定页面、特定对象或特定任务中有效的程序，未必能安全迁移到表面相似的新情境。第三，skill library 持续增长后容易出现重复技能、过时技能、依赖冲突和组合错误。因此，Programmatic Skill Construction 往往需要配套的 skill selection、deduplication、versioning、testing、debugging 和 stale detection 机制。

从 P2 的角度看，Programmatic Skill Construction 是最强形式的 schematic transformation 之一。它不仅把经验从 narrative trajectory 转化为结构化 artifact，而且进一步使 artifact 具备执行语义。其关键问题不再只是“如何总结经验”，而是“如何把经验安全地编译成可复用动作”。

论文：
- Voyager: An Open-Ended Embodied Agent with Large Language Models
- SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills
- WebXSkill: Skill Learning for Autonomous Web Agents
- Inducing Programmatic Skills for Agentic Tasks
- Evolving Programmatic Skill Networks
- MobileGPT: Augmenting LLM with Human-like App Memory for Mobile Task Automation
- Beyond Training: Enabling Self-Evolution of Agents with MOBIME
- AutoRefine: From Trajectories to Reusable Expertise for Continual LLM Agent Refinement

### Procedural Workflow Induction

Procedural Workflow Induction 指的是从多步 agent trajectories 中归纳出可复用的任务流程结构，例如 workflow、DAG、hierarchical procedure、task tree、stage-action hierarchy、procedural memory 或 workflow template。这类方法关注的不是把某一段动作封装成单个可调用 skill，而是抽象出完成一类任务所需的阶段划分、步骤顺序、依赖关系、控制流、条件分支、前置条件和后置状态。

这类方法的源经验通常是完整任务执行轨迹，而不是单个局部动作片段。轨迹中包含 agent 如何理解任务、如何分解目标、按什么顺序调用工具或执行操作、在何处根据观察结果调整策略，以及最终如何达到成功或失败状态。转化后的 artifact 通常保留任务执行的过程结构，使后续 agent 能够按照该结构进行 planning、retrieval、instantiation、checking 或 execution。

Procedural Workflow Induction 的核心思想是，许多复杂任务的可复用经验并不体现在某个孤立动作中，而体现在任务执行过程的组织方式中。成功轨迹往往包含稳定的阶段模式，例如先收集信息，再筛选候选项，再验证约束，最后执行提交；失败轨迹也可能揭示某些步骤顺序、依赖检查或条件判断的缺失。通过从轨迹中归纳 workflow，agent 可以获得一种比单步 skill 更高层的 procedural scaffold，用于指导未来任务的整体执行。

这类 artifact 的 schematic 性体现在其显式过程结构上。一个 workflow 或 procedure 通常包含多个节点，每个节点对应一个子任务、工具调用、动作阶段、状态检查或决策点；边则表示时间顺序、数据依赖、控制依赖、条件跳转或并行关系。一些方法还会为节点附加 precondition、postcondition、input/output schema、tool specification、exception handling rule 或 confidence score。后续 agent 可以根据当前任务检索相似 workflow，实例化其中的变量，检查当前状态是否满足前置条件，并按照 workflow 的阶段结构逐步执行。

与 Programmatic Skill Construction 相比，Procedural Workflow Induction 的粒度更高。前者把经验转化为可调用动作单元，强调 executable skill；后者把经验转化为任务流程结构，强调 task-level control flow。一个程序化 skill 可以是 workflow 中的一个节点，而一个 workflow 可以调度多个 skill、工具或子任务。因此，两者可以组合，但在 taxonomy 中应按照 artifact 的主要功能区分：如果 artifact 主要扩展 action space，则归入 Programmatic Skill Construction；如果 artifact 主要组织多步任务执行过程，则归入 Procedural Workflow Induction。

这类方法的优势在于可解释性和可控性较强。相比直接检索 raw trajectories，workflow artifact 更短、更抽象，也更容易定位任务中的关键阶段。相比自然语言总结，workflow 可以显式表达步骤依赖、执行顺序和状态检查，因此更适合 long-horizon task planning、tool-use orchestration、web navigation、mobile automation 和 multi-stage reasoning tasks。对于复杂任务，workflow 还可以帮助 agent 避免遗漏必要步骤，减少重复探索，并在失败时定位是哪一阶段出了问题。

Procedural Workflow Induction 的主要挑战在于抽象粒度控制。若 workflow 过于具体，它会退化为对历史轨迹的浅层回放，难以泛化到新任务；若 workflow 过于抽象，它又可能丢失关键上下文、工具约束或状态条件，导致后续执行失败。此外，workflow induction 往往需要判断哪些步骤是任务本质结构，哪些只是偶然路径。这一判断如果依赖单条轨迹，容易产生错误归因；如果依赖多条轨迹，又需要解决轨迹对齐、步骤聚类、变量泛化和冲突合并等问题。

另一个重要问题是 workflow drift。网页、软件、工具接口或环境状态变化后，原先有效的 workflow 可能不再适用。因此，高质量的 Procedural Workflow Induction 通常需要配套的 consistency checking、precondition verification、workflow rewriting、merge、deduplication 和 update 机制。长期来看，这类方法的关键不只是生成 workflow，而是维护一个可增长、可修订、可验证的 procedural memory。

论文：
- WorkflowGen: an adaptive workflow generation mechanism driven by trajectory experience
- FlowMind: Execute-Summarize for Structured Workflow Generation from LLM Reasoning
- Enhancing Web Agents with a Hierarchical Memory Tree
- Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement
- Beyond Training: Enabling Self-Evolution of Agents with MOBIME
- Environment Maps: Structured Environmental Representations for Long-Horizon Agents
- Agent Workflow Memory
- Skill-Pro: Learning Reusable Skills from Experience via Non-Parametric PPO for LLM Agents

### Structured Memory Graph Construction

Structured Memory Graph Construction 指的是将 agent trajectories 中出现的实体、关系、状态变化、空间结构、事件依赖或交互历史转化为可检索、可遍历、可更新的图结构记忆。这类方法的目标不是直接生成一个可执行动作，也不是主要归纳任务流程，而是构建 agent 对环境、任务世界、历史经验或多智能体交互关系的结构化表示。

这类方法的源经验通常来自 agent 与环境的持续交互过程，例如 text-game exploration、embodied navigation、web interaction、mobile operation、multi-agent collaboration 或 long-horizon task execution。轨迹中包含 agent 观察到的对象、位置、状态、事件、动作后果、用户偏好、任务上下文、角色关系或历史对话。转化后的 artifact 可以表现为 knowledge graph、episodic graph、semantic graph、scene graph、spatial-object graph、state-transition graph、interaction graph、query graph、environment map 或 world model graph。

Structured Memory Graph Construction 的基本思想是，agent 的许多经验并不适合被表达为线性文本或固定流程，而更适合被组织为关系结构。环境中的对象之间有空间关系，动作会改变状态，历史事件之间存在时间或因果联系，多智能体交互中存在角色、任务、信息流和依赖关系。如果这些关系仅以 raw logs 或自然语言 memory notes 存储，后续 agent 很难进行精确检索、局部更新和多跳推理。图结构 memory 则提供了一种更适合组织关系经验的 schematic carrier。

这类 artifact 的 schematic 性主要体现在节点、边和属性的显式结构。节点可以表示对象、地点、状态、事件、任务、角色、查询、记忆片段或环境上下文；边可以表示 spatial relation、temporal relation、causal relation、state transition、interaction dependency、semantic relation 或 memory linkage。后续 agent 可以基于图结构进行 retrieval、subgraph selection、neighbor expansion、graph traversal、world-state checking 或 structured prompting。一些系统还会维护 outdated fact removal、edge confidence、memory decay、utility score 或 graph pruning，以避免图记忆持续膨胀或被过时信息污染。

Structured Memory Graph Construction 与 Procedural Workflow Induction 的区别在于图的语义功能。Workflow graph 主要回答“任务应该如何执行”，其节点和边表示步骤顺序、控制流或任务依赖；memory graph 主要回答“环境中有什么、状态如何变化、历史经验之间有什么关系”，其节点和边表示实体、状态、事件、空间、语义或交互关系。因此，不能仅凭 artifact 是否是 graph 来归类。若图的主要作用是调度任务步骤，应归入 Procedural Workflow Induction；若图的主要作用是存储和检索结构化环境知识或经验关系，则归入 Structured Memory Graph Construction。

这类方法的优势在于能够支持关系级别的记忆复用。相比 raw trajectory retrieval，图结构可以减少无关上下文，并使 agent 聚焦于当前决策所需的实体、状态或关系。相比自然语言 summary，图结构更容易局部更新：当环境中某个对象位置变化、某条关系失效或某段交互结果被新证据覆盖时，系统可以修改相关节点或边，而不必重写整段记忆。对于 embodied agents、text-game agents、web agents 和 multi-agent systems，这种结构化 memory 有助于 long-horizon planning、state tracking 和 context reconstruction。

然而，Structured Memory Graph Construction 也面临明显困难。首先，图抽取过程容易产生错误实体、错误关系或过度细碎的节点，尤其在 observation 噪声较大或环境状态快速变化时更明显。其次，图结构虽然适合存储关系，但许多 LLM agent 最终仍需要将子图序列化为 prompt，这可能削弱 graph traversal 的优势。第三，图记忆随时间增长后可能出现 memory bloat、过时信息、重复节点、冲突边和 retrieval noise。因此，这类方法通常需要 graph update、conflict resolution、pruning、confidence estimation 和 retrieval control 机制。

从 P2 视角看，Structured Memory Graph Construction 代表了从 narrative trajectory 到 relational schematic memory 的转化。它不直接把经验变成动作，也不直接生成完整流程，而是把经验沉淀为可查询的结构化世界知识。其价值在于为 agent 提供比 raw context 更稳定、更可维护的外部认知结构。

论文：
- AriGraph: Learning Knowledge Graph World Models with Episodic Memory for LLM Agents
- G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems
- Environment Maps: Structured Environmental Representations for Long-Horizon Agents
- BrainMem: Brain-Inspired Evolving Memory for Embodied Agent Task Planning
- Beyond Training: Enabling Self-Evolution of Agents with MOBIME
- A-MEM: Agentic Memory for LLM Agents

### Other Schematic Artifacts and Boundary Cases

除上述三类外，还有一些方法产生的 artifact 具有一定结构化特征，但难以被稳定归入某一个 P2 家族。这些方法通常处在 P2 与 P1、P7、Composite 或非 agent setting 的边界上。本文将它们作为 Other Schematic Artifacts and Boundary Cases 单独讨论，而不是强行纳入前三类。

第一类边界情况是 semi-structured narrative artifacts。一些方法将轨迹总结为 workflow、skill、SOP、procedure 或 guideline，但这些 artifact 虽然在表面上具有编号、字段或步骤结构，下游消费时仍主要依赖 LLM 的自然语言理解，而没有 parser、executor、workflow engine 或 graph traversal module 介入。这类方法更接近 Narrative-to-Narrative Transformation。它们可以在 P2 章节中作为边界案例讨论，用来澄清“structured text”并不必然等于 schematic artifact。

第二类边界情况是 hybrid schematic-narrative artifacts。一些方法同时产生 code snippets、subagent patterns、natural-language guidelines、memory notes 或 semi-structured procedures。其中一部分 artifact 具备可执行或可解析结构，另一部分则主要是 narrative advice。对于这类方法，不能简单地按论文术语整体归类，而应分析其核心贡献和主要消费机制。如果系统的关键能力来自 executable skill、workflow schema 或 graph memory，则可以作为 P2 的混合案例；如果结构化部分只是辅助说明，而核心复用依然依赖自然语言提示，则应更谨慎地归入 P1 或 boundary discussion。

第三类边界情况是 source-side ambiguity。某些方法确实生成了 code、workflow 或 graph 等 schematic artifacts，但这些 artifacts 并不是从具体 agent trajectories 中提炼出来的，而是由模型根据任务描述、专家知识、静态文档或参数化能力直接生成。这样的工作虽然在目标 artifact 上看似接近 P2，但其 transformation direction 并不是 Narrative-to-Schematic，而更接近 Parametric-to-Tokenized externalization 或一般的 program/workflow synthesis。因此，P2 纳入标准必须同时检查 source experience 和 target artifact，不能只看产物是否结构化。

第四类边界情况是 composite pipelines。有些系统先将 trajectory 转化为 schematic artifact，然后进一步把这些 artifact 用于数据合成、SFT、RL 或 policy update。在这种情况下，如果论文的核心贡献是从经验到参数的内化，schematic artifact 只是中间表示，则更适合归入 Composite 或 Tokenized-to-Parametric pathway。P2 章节可以引用这些方法说明 schematic artifact 的中介作用，但不应把它们作为纯 P2 方法。

第五类边界情况是 non-agent traces。一些工作从 human demonstrations、system logs、screen recordings 或 creative software traces 中构建 workflow graph 或 action graph。这些 artifact 可能高度 schematic，也可能对 agent design 有启发，但如果源数据不是 LLM-based agent 在序贯决策中产生的 experience loop，则它们不完全满足本文对 agent experience transformation 的定义。它们可以作为相关背景或外部启发，而不应直接纳入 P2 主 taxonomy。

设置这一小节的目的不是扩大 P2 范围，而是明确 P2 的边界。P2 的判定需要同时满足三个条件：第一，输入必须是具体 agent trajectory 或 interaction log；第二，输出必须是具有可解析、可执行或可遍历结构的 schematic artifact；第三，下游复用必须利用这种结构，而不是仅让 LLM 自由阅读文本。只有同时满足这三点，才能构成严格意义上的 Narrative-to-Schematic Experience Transformation。

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