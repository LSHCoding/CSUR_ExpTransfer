[Title]: Agent Workflow Memory
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Raw interaction trajectories / web navigation logs
- [Target Experience]: Reusable workflows / routines (commonly reused action sequences)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 作为 prompt 中的 workflow 指导注入 agent，用于 guide subsequent generations
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 从训练示例或在线测试查询中收集 agent 交互轨迹，通过 LLM 诱导提取常见复用 routine（workflow），将原始轨迹中重复出现的动作模式抽象为可复用的工作流模板；在后续任务中选择性提供匹配的 workflow 以指导 agent 决策。

[Title]: Memp: Exploring Agent Procedural Memory
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Raw agent trajectories
- [Target Experience]: Fine-grained step-by-step instructions + higher-level script-like abstractions (procedural memory)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 作为 procedural memory repository 在后续类似任务中检索复用
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 将过去 agent 轨迹蒸馏为两个粒度的 Narrative 产物：细粒度 step-by-step 指令和高层 script-like 抽象；通过 Build-Retrieval-Update 动态机制持续更新、修正和淘汰记忆内容，使 procedural memory 随新经验同步演化。

[Title]: Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Raw agent interaction trajectories
- [Target Experience]: Multi-faceted distilled experiences（success patterns, failure triggers, comparative insights）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: context-adaptive reuse：通过 scenario-aware indexing 为新上下文定制历史 insights
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 三个机制构成记忆全生命周期：1) multi-faceted distillation 从轨迹中提取成功模式、失败触发因素和比较性见解；2) context-adaptive reuse 通过场景感知索引将历史 insights 适配到新上下文；3) utility-based refinement 自动添加有效记忆、修剪过时记忆，维持紧凑高质量经验池。

[Title]: Traversal-as-Policy: Log-Distilled Gated Behavior Trees as Externalized, Verifiable Policies for Safe, Robust, and Efficient Agents
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Sandboxed execution logs / trajectories (from OpenHands)
- [Target Experience]: Executable Gated Behavior Tree (GBT) — 结构化、可执行、可验证的控制策略
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 用 GBT traversal 替代自由生成作为 control policy；运行时 lightweight traverser 匹配 base model intent 到 child macros
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 从沙盒执行日志中挖掘成功轨迹中的 state-conditioned action macro，经 merge-check 后编码为 GBT 节点；不安全轨迹触发的 macro 附加 deterministic pre-execution gates，并在 experience-grounded monotonicity 下更新，确保已拒绝的不安全上下文不可重新接纳。是一种从 Narrative 日志到 Schematic 可执行控制策略的强形式化转化。

[Title]: Reflexion: language agents with verbal reinforcement learning
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Task feedback signals (scalar values or free-form language) + trial-and-error trajectories
- [Target Experience]: Reflective text (verbal reflections) stored in episodic memory buffer
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 作为 episodic memory 在后续 trials 中注入以 induce better decision-making
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Agent 收到 task feedback 后，通过 LLM 口头反思失败原因和成功经验，将反思文本存入 episodic memory buffer；在后续试验中将过往反思作为额外上下文注入，实现在无参数更新条件下的 verbal reinforcement learning。

[Title]: AutoGuide: Automated Generation and Selection of Context-Aware Guidelines for Large Language Model Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Offline experiences / interaction histories
- [Target Experience]: Context-aware guidelines（简洁自然语言，遵循条件结构描述适用上下文）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在 agent 当前决策过程中提供 relevant knowledge，克服 demonstration-based in-context learning 的局限
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 从离线经验中自动提取 context-aware guidelines，每条 guideline 以简洁自然语言表达并遵循条件结构（明确描述适用上下文）；在推理时根据当前决策状态选择相关 guideline 注入，为 agent 提供精准的领域知识而不依赖完整 demonstration。

[Title]: CLIN: A Continually Learning Language Agent for Rapid Task Adaptation and Generalization
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Agent-environment interaction trials
- [Target Experience]: Causal abstractions — 以因果抽象为中心的持久动态文本记忆
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在新 trial 中检索相关因果知识以改进决策
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: CLIN 在每次 trial 后更新以因果抽象（而非通用"helpful hints"）为中心的持久文本记忆，从交互经验中提取变量间的因果关系；记忆随 trial 持续更新，使 agent 在冻结模型参数下持续改进，并支持跨任务和跨环境迁移。

[Title]: VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Suboptimal task demonstrations / imperfect trajectories
- [Target Experience]: Generalized strategies and action annotations（cognitive abstractions: causal relationships, object state changes, temporal subgoals, task-relevant visual elements）
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {self}, {human}
- [Utilization]: 作为 retrieval-augmented generation 的 exemplars 或 fine-tuning 的训练数据
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: VLM agent 对不完美 demonstration 进行抽象：修正低效 action、标注认知抽象（因果关系、物体状态变化、时间子目标和任务相关视觉元素）；通过人类反馈在相似环境中迭代精炼。注意：当这些抽象 exemplars 用于 fine-tuning 时，产生 Narrative → Policy (P5) 的二次转化，但论文主体贡献在 P1 阶段。

[Title]: Voyager: An Open-Ended Embodied Agent with Large Language Models
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Interaction feedback, execution errors, and self-verification from Minecraft environment
- [Target Experience]: Executable code skill library（可执行 JavaScript 程序，temporally extended, interpretable, compositional）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: skill library 中的 code skills 在新世界中复用以解决新任务；compounds agent abilities rapidly
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 通过 iterative prompting mechanism：incorporate environment feedback、execution errors 和 self-verification 三重信号，反复改进生成的程序；成功程序以可执行代码形式存入 skill library。以黑盒查询 GPT-4 实现，无参数更新。核心机制是 trajectory → executable code 的 P2 转化。

[Title]: Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Broad execution experience / diverse pool of agent trajectories
- [Target Experience]: Unified, conflict-free skill directory（comprehensive declarative skill guide）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 作为 skill guide 注入 agent prompt；跨 LLM scale 和 OOD setting 转移
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 不使用 sequential single-trajectory 方法，而是调度并行 sub-agent fleet 分析多样化执行池；各 sub-agent 提取 trajectory-specific lessons，通过归纳推理层级整合为统一的、无冲突的 skill directory。核心创新在于从分散轨迹片段到统一 skill guide 的归纳整合机制。

[Title]: Evolving Programmatic Skill Networks
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Interaction experience in embodied environments (MineDojo, Crafter)
- [Target Experience]: Executable symbolic programs forming a compositional Programmatic Skill Network (PSN)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: skill 在后续任务中以组合方式复用；PSN 随经验持续增长和重构
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 三个核心机制：1) REFLECT 对 skill composition 做结构化故障定位；2) maturity-aware update gating 做渐进优化——稳定 skill 保持、不确定 skill 保留可塑性；3) canonical structural refactoring with rollback validation 维持网络紧凑性。PSN 的学习动态呈现与神经网络训练的结构性平行。

[Title]: Skill-Pro: Learning Reusable Skills from Experience via Non-Parametric PPO for LLM Agents
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Interaction experiences / episodic narratives
- [Target Experience]: Executable Skills（defined by activation, execution, and termination conditions）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 作为 procedural memory 在 in-domain, cross-task, cross-agent 场景中复用
- [Method]: ⟨LLM-extract⟩, ⟨RL: PPO⟩
- [Mechanism]: 形式化 Skill-MDP 将被动 episodic narrative 转化为可执行 Skill（含 activation/execution/termination 条件）；Non-Parametric PPO 分两阶段运作——semantic gradients 做高质量 candidate generation，PPO Gate 做 robust skill verification（不更新模型参数，而是在语义空间做 PPO 风格的策略优化）；score-based maintenance 维持紧凑高质量 procedural memory。

[Title]: SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Practice experiences from autonomous website exploration
- [Target Experience]: Reusable APIs（lightweight, plug-and-play, synthesized from practice）
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: API library 持续扩展增强 agent 能力；strong agent 合成的 API 可迁移给 weaker agent 使用
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Agent 在新网站上自主探索发现 skills，通过实践执行获取经验，将实践轨迹蒸馏为可复用的轻量 API；迭代探索持续扩展 API 库。核心转化是 web interaction trajectories → executable API code。

[Title]: Inducing Programmatic Skills for Agentic Tasks
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Web interaction trajectories (online interaction with web environment)
- [Target Experience]: Program-based skills（可执行程序，经 verification 保证正确性）
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 组合 primitive actions 为 higher-level skills；跨网站迁移时复用
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: ASI (Agent Skill Induction) 在线交互中诱导、验证和利用程序化 skills：从 web 交互轨迹中提取可复用 action 模式，以程序形式编码，通过 programmatic verification guarantee 确保诱导阶段的正确性；将 click 等 primitive action 组合为 search product 等 higher-level skills。

[Title]: AutoRefine: From Trajectories to Reusable Expertise for Continual LLM Agent Refinement
- [Pathway]: Narrative → Narrative (P1) + Narrative → Schematic (P2)
- [Source Experience]: Agent execution histories
- [Target Experience]: Dual-form Experience Patterns — specialized subagents (procedural) + skill patterns as guidelines/code snippets (static knowledge)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在 ALFWorld, ScienceWorld, TravelPlanner 中指导 agent 决策
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 从执行历史中提取两种形式的经验模式：对于 procedural subtasks 提取专有 subagent（含独立推理和记忆能力）；对于 static knowledge 提取 guidelines 或 code snippets。continuous maintenance mechanism 评分、修剪和合并模式以防止 repository degradation。过程性知识部分落入 P1（guidelines），程序化/结构化部分落入 P2（code snippets + subagent 定义）。

[Title]: Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Agent trajectories (2851 trajectories compressed into 187 procedures)
- [Target Experience]: Reusable procedures (hierarchical procedural memory, externally stored)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 通过 expected-utility scoring 选择 action，Bayesian posteriors 跟踪可靠性
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: MACLA 将 reasoning 与 learning 解耦：从轨迹中提取可复用 procedure，以 Bayesian posteriors 跟踪其可靠性，通过 contrasting successes and failures（对比精炼）持续改进 procedure 质量；256 秒内从 2851 条轨迹构建 187 个 procedure 的记忆体。Procedure 以自然语言形式存在，属于 Narrative 层内抽象。

[Title]: WebXSkill: Skill Learning for Autonomous Web Agents
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Synthetic agent trajectories from web interaction
- [Target Experience]: Executable skills — parameterized action program + step-level natural language guidance paired
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: 两种部署模式——grounded mode（全自动多步执行）和 guided mode（作为 step-by-step instruction 供 agent 遵循）
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 三个阶段：1) skill extraction 从 synthetic agent trajectory 中挖掘可复用 action subsequence 并抽象为参数化 skill（program + NL guidance paired）；2) skill organization 将 skills 索引到 URL-based graph 做 context-aware retrieval；3) skill deployment 暴露 grounded 和 guided 两种互补模式。核心创新在于 bridging textual workflow skills 和 code-based skills 之间的 grounding gap。

[Title]: Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Accumulated strategies, code snippets, and problem-solving insights from previous test queries
- [Target Experience]: Concise, transferable snippets (self-curated memory of accumulated insights)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在 test-time 注入后续 query 以增强推理，无需 labels 或 human feedback
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 在推理时，从之前的 query 解答经验中自动提取和存储累积策略、代码片段和通用问题解决见解；记忆自我策展，聚焦简洁可迁移片段而非完整 transcript；在后续 query 中将这些经验作为额外上下文注入，实现 test-time learning without parameter updates。

[Title]: Agent KB: Leveraging Cross-Domain Experience for Agentic Problem Solving
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Agent trajectories aggregated from heterogeneous agent frameworks (smolagents, OpenHands, OWL)
- [Target Experience]: Structured knowledge base entries — cross-domain workflows (planning) + diagnostic fixes (feedback)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: hybrid retrieval 分两阶段：planning 以 cross-domain workflows seed agent，feedback 施加 targeted diagnostic fixes
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 跨框架聚合 agent trajectories 到结构化知识库；推理时通过 hybrid retrieval 两阶段注入——planning 阶段以跨领域 workflow 种子 agent 规划，feedback 阶段施加针对性诊断修复；disagreement gate 确保检索知识增强而非干扰推理。核心是跨框架经验聚合与检索，经验形式为 Narrative workflows + fixes。

[Title]: Skill Set Optimization: Reinforcing Language Model Behavior via Transferable Skills
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: High-reward subtrajectories from agent-environment interaction
- [Target Experience]: Transferable skills（subgoals + instructions per skill, refined via pruning）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: in-context 注入 LLM actor 以 reinforce high-reward behaviors
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 从交互轨迹中提取具有高 reward 的常见 subtrajectory，生成为每个 skill 的 subgoal 和 instruction；将 skills 以 in-context 方式提供 LLM actor 以强化高 reward 行为；通过 pruning 持续精炼 skill set。完全在 token 空间运作，无参数更新。

[Title]: AutoManual: Constructing Instruction Manuals by LLM Agents via Interactive Environmental Learning
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Interactive environmental exploration and rule optimization
- [Target Experience]: Comprehensive instruction manual（structured rules → compiled manual）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 自生成 manual 不仅增强 LLM agent 适应性，还可指导 smaller LLM 的规划；human-readable
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 三 Agent 架构：Planner 基于当前 rule 编写与环境交互的可执行计划；Builder 通过结构化 rule system 在线更新和管理规则（含 case-conditioned prompting 减少幻觉）；Formulator 将规则编译为综合 manual。整体流程是 raw interaction → rules (Narrative) → compiled manual (Narrative) 的 P1 链式抽象。

[Title]: Contextual Experience Replay for Self-Improvement of Language Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Past agent experiences in web environments (environment dynamics + decision-making patterns)
- [Target Experience]: Dynamic memory buffer of synthesized experiences
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在 context window 内检索并增强 agent 自身对新任务的知识
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 在推理时累积并合成过去经验为动态记忆缓冲区，经验涵盖环境动态和常见决策模式；agent 在新任务中检索相关知识进行自我增强。training-free，全部在 context window 内运作。

[Title]: Meta-Policy Reflexion: Reusable Reflective Memory and Rule Admissibility for Resource-Efficient LLM Agent
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: LLM-generated reflections from past episodes
- [Target Experience]: Structured Meta-Policy Memory (MPM) — predicate-like, reusable corrective knowledge
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 通过两种互补机制在推理时施加：soft memory-guided decoding + hard rule admissibility checks (HAC)
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 将 LLM 生成的 per-episode reflections 整合为结构化的、predicate-like 的 Meta-Policy Memory；在推理时通过 soft memory-guided decoding（偏向与 MPM 一致的动作）和 hard rule admissibility checks（强制执行域约束阻止不安全/无效动作）双重机制复用。将单次反思提升为跨任务可复用的元策略。

[Title]: Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Execution feedback from agent interactions (natural execution feedback, without labeled supervision)
- [Target Experience]: Evolving playbooks — structured, incremental contexts (strategies accumulated, refined, organized)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 作为 system prompt / agent memory 在 offline 和 online 场景中优化 agent 性能
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 将 contexts 视为 evolving playbooks，通过 generation-reflection-curation 的模块化过程积累和精炼策略；通过 structured incremental updates 防止 context collapse（上下文崩溃——迭代重写导致细节逐渐丧失）；利用自然执行反馈而不需要标注监督。

[Title]: Compiled Memory: Not More Information, but More Precise Instructions for Language Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Agent task experience — facts extracted from agent failures and successes
- [Target Experience]: Evolved system prompt with learned sub-bullets (precise instruction structure)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 通过 instruction rewriting（而非 context injection）deliver：重写 agent 的 system prompt
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Atlas 将累积任务经验编译为 agent 的指令结构：从 agent 成功和失败中提取事实，通过三步 promotion gate 验证，将经验以学得的 sub-bullets 形式重写 system prompt。记忆是蒸馏而非存储，交付方式是 prompt rewriting 而非 context 注入。核心属性是 training signal constraint——学得的 prompt 精确反映所学内容，不外推。

[Title]: ExpeL: LLM Agents Are Experiential Learners
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Agent experiences gathered autonomously from a collection of training tasks
- [Target Experience]: Extracted knowledge in natural language + past experiences (recalled at inference)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在推理时召回提取的 insights 和 past experiences 以做出 informed decisions
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Agent 自主从训练任务集中收集经验，用自然语言提取知识（不涉及参数更新）；推理时同时召回提取的 insights 和原始 past experiences。属于纯 Narrative → Narrative 的同层抽象转化。

[Title]: ActionEngine: From Reactive to Programmatic GUI Agents via State Machine Memory
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: GUI interaction trajectories from offline crawling exploration
- [Target Experience]: Updatable state-machine memory of GUIs（Crawling Agent 构建的结构化状态机）
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Execution Agent 利用 state-machine memory 合成完整可执行 Python 程序进行在线任务执行
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 双 Agent 架构：Crawling Agent 通过离线探索将 GUI 交互轨迹构建为可更新的状态机记忆（Schematic），Execution Agent 将该记忆合成为完整可执行 Python 程序。执行失败时触发 vision-based re-grounding fallback 修复失败动作并更新记忆。核心转化是 GUI interaction traces → state-machine memory → executable Python program。

[Title]: A-MEM: Agentic Memory for LLM Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Historical interaction experiences
- [Target Experience]: Interconnected knowledge network — comprehensive notes with structured attributes (contextual descriptions, keywords, tags) + dynamic links between memories
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 通过动态索引和链接创建互联知识网络，支持 adaptive and context-aware memory management
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 基于 Zettelkasten 原则：新记忆加入时生成包含 contextual descriptions/keywords/tags 的综合笔记；系统分析历史记忆识别相关连接并建立 links；新记忆可以触发已有记忆的 contextual representations 和 attributes 更新。完全在 Narrative token 空间内运作。

[Title]: Enhancing Web Agents with a Hierarchical Memory Tree
- [Pathway]: Narrative → Narrative (P1) + Narrative → Schematic (P2)
- [Source Experience]: Raw web interaction trajectories
- [Target Experience]: Hierarchical Memory Tree (HMT) — three-level hierarchy: Intent (task goals), Stage (reusable semantic subgoals with pre/post-conditions), Action (action patterns with semantic element descriptions)
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: stage-aware inference: Planner 验证 pre-conditions 对齐子目标，Actor 将 semantic descriptions 匹配到目标页面
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 自动化抽象管道从原始轨迹构建三层层次结构：Intent 层统一 user instruction 为标准任务目标 (Narrative)；Stage 层定义可复用语义子目标及可观察 pre/post-conditions (Narrative)；Action 层存储 action patterns 配以可迁移语义元素描述 (Narrative/Schematic 混合)。Intent 和 Stage 层为 Narrative 抽象，Action 层的结构化 patterns 带有 Schematic 特征。

[Title]: Environment Maps: Structured Environmental Representations for Long-Horizon Agents
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Heterogeneous evidence — screen recordings, execution traces
- [Target Experience]: Structured graph with four components: Contexts (abstracted locations), Actions (parameterized affordances), Workflows (observed trajectories), Tacit Knowledge (domain definitions and reusable procedures)
- [Source Modality]: [vis+txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: agent-agnostic, persistent foundation for long-horizon planning; human-interpretable, editable, incrementally refinable
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 将 screen recordings 和 execution traces 等多种异构证据整合为结构化图表示：Contexts 抽象位置，Actions 参数化 affordances，Workflows 观察到的轨迹，Tacit Knowledge 领域定义和可复用过程。是典型的多模态经验 → Schematic graph 的 P2 转化。

[Title]: Beyond Training: Enabling Self-Evolution of Agents with MOBIMEM
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: User interactions + task execution traces in mobile/desktop environments
- [Target Experience]: Three memory primitives — Profile Memory (DisGraph for user preferences), Experience Memory (multi-level templates for execution logic), Action Memory (fine-grained interaction sequences)
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: OS-inspired services orchestrate execution: scheduler coordinates parallel sub-tasks, AgentRR enables safe action reuse, context-aware exception handling
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 三种记忆原语将 agent 进化与模型权重解耦：Profile Memory 以 DisGraph 结构存储用户偏好；Experience Memory 以多级模板实例化任务执行逻辑；Action Memory 记录细粒度交互序列。核心转化是 interaction traces → memory primitives 的 Narrative 抽象，experience templates 部分具有弱 Schematic 特征但主体是 Narrative。

[Title]: G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems
- [Pathway]: Narrative → Narrative (P1) + Narrative → Schematic (P2)
- [Source Experience]: Multi-agent collaboration trajectories and inter-agent interactions
- [Target Experience]: Three-tier graph hierarchy: insight graph (high-level generalizable insights), query graph, interaction graph (fine-grained condensed interaction trajectories)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: bi-directional memory traversal: 同时检索 high-level generalizable insights 和 fine-grained interaction trajectories 以支持跨 trial 知识复用
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 受组织记忆理论启发，构建三层图层次管理多智能体交互：insight graph 存储高层可泛化见解 (Narrative)，interaction graph 紧凑编码协作经验 (Schematic 图结构)，query graph 连接用户查询。Multi-target：同时产出 Narrative (insights) 和 Schematic (graphs)。

[Title]: AutoSkill: Experience-Driven Lifelong Learning via Skill Self-Evolution
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: User dialogue and interaction traces across sessions
- [Target Experience]: Reusable skills — standardized skill representation, composable and transferable
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 动态注入相关 skills 到未来请求中；跨 agents/users/tasks 共享和迁移
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 从对话和交互轨迹中自动抽象用户偏好和需求为技能，支持持续自我进化；作为 model-agnostic plugin layer 运作，不修改底层模型参数。将短暂的交互经验转化为显式、可复用、可组合的 skill 能力。

[Title]: What Deserves Memory: Adaptive Memory Distillation for LLM Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Raw interaction sequences
- [Target Experience]: Coherent narratives (Episodic Memory Integration) + extracted insights via prediction error (Semantic Knowledge Distillation)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 蒸馏后的 insights 供下游 memory management 使用
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: NEMORI 以 prediction error 作为经验未来效用的度量标准：Episodic Memory Integration 将原始交互转化为连贯叙事 (Narrative)；Semantic Knowledge Distillation 通过预测误差提取 insights (Narrative)。以数据驱动方式替代启发式记忆设计，核心问题是如何判定哪些经验值得保留。

[Title]: Darwinian Memory: A Training-Free Self-Regulating Memory System for GUI Agent Evolution
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Complex GUI interaction trajectories (decomposed into independent reusable units)
- [Target Experience]: Self-evolving memory ecosystem — reusable trajectory units tracked by survival value
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Utility-driven Natural Selection: 跟踪 survival value，主动修剪次优路径并抑制高风险计划
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 将复杂轨迹分解为独立可复用单元，实施 Utility-driven Natural Selection 追踪每个单元的 survival value；通过进化压力促使 agent 衍生出更优策略。核心创新在于以自然选择逻辑替代静态累积：记忆是被动态管理的生态系统而非 append-only archive。

[Title]: APEX-EM: Non-Parametric Online Learning for Autonomous Agents via Structured Procedural-Episodic Experience Replay
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Structured procedural-episodic execution traces (planning steps, artifacts, iteration history with error analysis, quality scores)
- [Target Experience]: Positive in-context examples (successful experiences) + negative examples with structured error annotations
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: hybrid retrieval (semantic search + structural signature matching + plan DAG traversal) 用于 in-context learning；成功经验为正例，失败为负例
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: PRGII workflow (Plan-Retrieve-Generate-Iterate-Ingest) 配合 Task Verifiers 提供多维度 reward 信号；structured experience representation 编码每次执行的完整 procedural-episodic trace；dual-outcome Experience Memory 将经验分为正例和带错误标注的负例。经验以 Narrative 形式存储，侧重结构化程度高的轨迹表示。

[Title]: Recon-Act: A Self-Evolving Multi-Agent Browser-Use System via Web Reconnaissance, Tool Generation, and Task Execution
- [Pathway]: Narrative → Narrative (P1) + Narrative → Schematic (P2)
- [Source Experience]: Erroneous and successful browser interaction trajectories
- [Target Experience]: Generalized tools — expressed as hints (Narrative) or rule-based codes (Schematic)
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 注册到 tool archive 供 Action Team 在推理时重新推理使用；closed-loop pipeline: data-tools-action-feedback
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Reconnaissance Team 对比错误和成功轨迹推断补救措施，抽象为统一 generalized tools——以 hints（Narrative）或 rule-based codes（Schematic）两种形式表达，实时注册到 tool archive；Action Team 利用这些工具重新推理过程。双输出形式说明抽象可以同时走 Narrative 和 Schematic 两种路径。

[Title]: Sample-Efficient Online Learning in LM Agents via Hindsight Trajectory Rewriting
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Failed interaction attempts
- [Target Experience]: Optimized trajectories (synthetic positive examples from unsuccessful interactions) + compressed trajectory representations
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 压缩轨迹表示存于 memory 供后续任务复用
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: ECHO 借鉴 RL 中的 hindsight experience replay：hindsight rule 用 LLM 识别失败尝试中可达到的替代子目标，生成优化轨迹（将失败转化为合成正例）；update rule 维持压缩轨迹表示存于 memory。核心创新在于用 LLM 生成反事实轨迹以提升样本效率。

[Title]: BrainMem: Brain-Inspired Evolving Memory for Embodied Agent Task Planning
- [Pathway]: Narrative → Narrative (P1) + Narrative → Schematic (P2)
- [Source Experience]: Interaction histories in 3D embodied environments
- [Target Experience]: Structured knowledge graphs (Schematic) + distilled symbolic guidelines (Narrative)
- [Source Modality]: [embodied]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 使 planner 能检索、推理和适应过往经验；plug-and-play 集成任意 multimodal LLM
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 受人类认知启发，三类记忆协同工作：working memory（即时处理）、episodic memory（交互历史）、semantic memory（结构化知识图谱 + 蒸馏符号化指南）。将具身交互历史持续转化为两类产物：structured KGs (Schematic, P2) 和 symbolic guidelines (Narrative, P1)。Multi-target 论文。

[Title]: M2: Dual-Memory Augmentation for Long-Horizon Web Agents via Trajectory Summarization and Insight Retrieval
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Verbose interaction history (web navigation trajectories) + offline insight bank
- [Target Experience]: Concise state updates (Internal Memory summaries) + actionable guidelines (External Memory insights)
- [Source Modality]: [vis+txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Internal Memory 压缩冗长交互历史为简洁状态更新；External Memory 检索 actionable guidelines 指导 agent
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 双层记忆：Dynamic Trajectory Summarization (Internal Memory) 将冗长交互历史压缩为简洁状态更新 (P1 压缩)；Insight Retrieval Augmentation (External Memory) 从离线 insight bank 检索可操作指南注入 agent (P1 检索复用)。两层同属 Narrative 内转化。

[Title]: REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Multisensory robot observations of past experiences (failed executions)
- [Target Experience]: Hierarchical summary of robot past experiences → failure explanation → corrected plan
- [Source Modality]: [embodied]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: failure explanation 指导 language-based planner 修正失败并完成任务
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 从多传感器观测生成机器人经验的层次化摘要（Narrative），基于摘要查询 LLM 进行失败推理，生成 failure explanation（Narrative），explanation 指导语言规划器修正失败。链式 P1：raw multisensory logs → summary → explanation → corrected plan。

[Title]: SkillX: Automatically Constructing Skill Knowledge Bases for Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Raw trajectories from seed training data
- [Target Experience]: Three-tier skill hierarchy: strategic plans, functional skills, atomic skills
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: plug-and-play skill knowledge base 供跨 agents 和跨 environments 复用
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 三级层次设计：从 raw trajectory 蒸馏为 strategic plans → functional skills → atomic skills 的三层技能层次；Iterative Skills Refinement 基于执行反馈自动修正技能；Exploratory Skills Expansion 主动生成和验证新技能以扩展覆盖范围。完全在 Narrative 空间运作的多层级抽象。

[Title]: GUI-explorer: Autonomous Exploration and Mining of Transition-aware Knowledge for GUI Agent
- [Pathway]: Narrative → Narrative (P1) + Narrative → Schematic (P2)
- [Source Experience]: Diverse trajectories collected by autonomous GUI exploration (structured interaction triples: observation, action, outcome)
- [Target Experience]: Transition-aware Knowledge — precise screen-operation logic extracted via unsupervised analysis of state transitions
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在推理时指导 GUI agent 做精确的 screen-operation 决策
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Function-aware Task Goal Generator 通过分析 GUI structural information 自动构建探索目标以收集多样化轨迹；Transition-aware Knowledge Extractor 通过无监督分析结构化交互三元组 (observation, action, outcome) 的状态转移提取精确 screen-operation logic。knowledge 以 rules/logic 形式存在，兼有 Narrative 描述的规则和 Schematic 结构化逻辑特征。

[Title]: Aligning Progress and Feasibility: A Neuro-Symbolic Dual Memory Framework for Long-Horizon LLM Agents
- [Pathway]: Narrative → Narrative (P1) + Narrative → Schematic (P2)
- [Source Experience]: Successful trajectories (for semantic blueprints) + failed transitions (for feasibility verification)
- [Target Experience]: Progress Memory — semantic blueprints extracted from successful trajectories (Narrative) + Feasibility Memory — executable Python verification functions synthesized from failed transitions (Schematic)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 推理时同时调用两种记忆：Progress Memory 提供全局语义引导，Feasibility Memory 执行严格逻辑验证
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 将 Progress Drift（全局语义漂移）和 Feasibility Violation（局部可行性违反）两种错误显式解耦：neural-network-based Progress Memory 从成功轨迹中提取语义蓝图 (P1)；symbolic-logic-based Feasibility Memory 从失败转移中合成可执行 Python 验证函数 (P2)。双产出分布在 Narrative 和 Schematic 两个层次。

[Title]: SWE-Exp: Experience-Driven Software Issue Resolution
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Prior agent trajectories from software issue resolution (both successful and failed repair attempts)
- [Target Experience]: Multi-faceted experience bank — reusable issue resolution knowledge at different levels (high-level problem comprehension to specific code changes)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在后续 issue 解决中检索复用，实现从 trial-and-error exploration 到 experience-driven resolution 的转变
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 从先前的 agent 修复轨迹中（成功和失败均采集）蒸馏简洁可操作的 issue resolution knowledge；多层次覆盖从 high-level problem comprehension 到 specific code changes。将软件修复经验以 Narrative 知识形式积累和复用。

[Title]: SkillClaw: Let Skills Evolve Collectively with Agentic Evolver
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Cross-user and over-time interaction trajectories
- [Target Experience]: Refined skills and extended capabilities — collective skill set updates shared across users
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 改进在 shared repository 中同步到所有用户，实现跨用户知识迁移和累积能力提升
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 持续聚合多用户使用中产生的交互轨迹，autonomous evolver 识别重复行为模式并将其转化为 skill 更新（refining existing skills 或 extending with new capabilities）。核心贡献在跨用户经验聚合和集体进化机制。

[Title]: PolySkill: Learning Generalizable Skills Through Polymorphic Abstraction
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Agent interaction experiences during web navigation
- [Target Experience]: Generalizable skills — decoupled abstract goal + concrete implementation (polymorphic skill representation)
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在 seen 和 unseen websites 上复用；提升 skill reuse 1.7x
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 借鉴软件工程中的多态概念，将 skill 的抽象目标（what it accomplishes）与具体实现（how it is executed）解耦：同一抽象目标可在不同网站上有多态实现。核心创新在 skill 表示方式而非转化机制本身，但整体属于 trajectory → skill 的 P1 抽象。

[Title]: Coarse-to-Fine Grounded Memory for LLM Agent Planning
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Environmental information and interaction experiences from training tasks
- [Target Experience]: Coarse-grained focus points + actionable hybrid-grained tips + fine-grained key information for self-QA reflection
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 推理时检索 task-relevant experiences 和 tips 支持规划；遇到环境异常时做 fine-grained self-QA reflection
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 粗到细三级记忆：coarse-grained focus points 指导训练任务中的经验收集 → hybrid-grained actionable tips 从每次经验中 extract → 推理时遇到异常做 fine-grained key information grounding 实现灵活 self-QA reflection 和计划修正。完全在 Narrative 空间的多粒度抽象。

[Title]: AndroTMem: From Interaction Trajectories to Anchored Memory in Long-Horizon GUI Agents
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Long interaction sequences with strong step-to-step causal dependencies
- [Target Experience]: Anchored State Memory (ASM) — compact set of causally linked intermediate-state anchors
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: subgoal-targeted retrieval 和 attribution-aware decision making
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 诊断发现随着交互序列增长，性能下降主要由 within-task memory failures 驱动。ASM 将交互序列表示为紧凑的因果链接中间状态 anchor 集，取代 full-sequence replay 和 summary-based baselines。anchors 作为结构化因果链具有 Schematic 特征。

[Title]: MemOrb: A Plug-and-Play Verbal-Reinforcement Memory Layer for E-Commerce Customer Service
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Multi-turn customer service interactions
- [Target Experience]: Compact strategy reflections stored in shared memory bank
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 检索注入以指导后续决策，无需 fine-tuning
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 将多轮交互蒸馏为紧凑的策略反思（strategy reflections），存入共享记忆库；通过检索这些反思指导 agent 决策。完全在 Narrative 空间，强调 verbal reinforcement 和跨 session 一致性。

[Title]: Learning on the Job: An Experience-Driven Self-Evolving Agent for Long-Horizon Tasks
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Sub-task execution trajectories from long-horizon productivity tasks
- [Target Experience]: Structured experience integrated into hierarchical Memory Module
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在后续任务中计划执行长期任务；积累的经验展现 zero-shot generalization 到新任务
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: MUSE 在每次 sub-task 执行后自主反思轨迹，将原始轨迹转化为结构化经验并整合回分层 Memory Module。随着经验积累，agent 表现持续提升。分层记忆组织多种经验水平（diverse levels of experience）用于规划和执行。

[Title]: PG-Agent: An Agent Powered by Page Graph
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Sequential episodes of multi-step operations across GUI pages
- [Target Experience]: Page graphs — explicitly model graph structure of pages connected by actions
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: RAG 技术检索 page graph 中的可靠 perception guidelines；注入 multi-agent framework 以泛化到 unseen scenarios
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 自动化管道将 sequential episodes（按时间排列的 GUI 操作序列）转化为 page graphs，显式建模页面间通过 action 连接的图结构。核心转化是 sequential narrative → graph-structured schematic (P2)。

[Title]: Procedural Knowledge at Scale Improves Reasoning
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Existing corpora of step-by-step reasoning trajectories (32 million compact procedural knowledge entries)
- [Target Experience]: Self-contained subquestion-subroutine pairs — compact procedural knowledge
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: in-thought prompt 让 model verbalize core subquestion，检索相关 subroutines，reason under retrieved subroutines as implicit procedural priors
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 将已有的大规模分步推理轨迹分解为 self-contained subquestion-subroutine pairs（3200万条），每条是紧凑的程序性知识（"如何重述问题、选择方法、在需要时验证或回溯"）。在推理时检索相关 subroutines 作为隐式程序性先验注入推理过程。

[Title]: MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Interaction traces from agent deployment
- [Target Experience]: Evolvable memory skills — structured, reusable routines for extracting, consolidating, and pruning information
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: controller 学习选择相关 skills，executor 生成 skill-guided memories
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 将静态 hand-designed memory operations 重新定义为可学习和可进化的 memory skills（提取、整合、修剪信息的结构化可复用例程）。三层架构：controller 学习 skill selection → executor 生成 skill-guided memories → designer 定期审查困难案例并进化 skill set。形成 skill-selection policy 和 skill set 自身的闭环改进。

[Title]: Mistake Notebook Learning: Batch-Clustered Failures for Training-Free Agent Adaptation
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Continuous streams of tasks and failures across persistent deployment
- [Target Experience]: Structured "mistake notes" — generalizable guidance distilled from batch-clustered shared error patterns
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在推理时用聚合的 failure patterns 主动引导搜索过程远离已知陷阱（integrated with test-time scaling）
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 不存储原始实例级经验或仅检索成功轨迹，而是从 batch-clustered failures 中提取共享错误模式形成结构化 "mistake notes"；仅在 batch 性能提升时更新外部记忆以确保稳定性。将失败经验转化为可泛化指导。

[Title]: MobileGPT: Augmenting LLM with Human-like App Memory for Mobile Task Automation
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Human-like app interaction process: explore, select, derive, recall
- [Target Experience]: Modular sub-tasks — smaller, re-usable, re-arrangeable task procedures
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 子任务可在不同目标中复用、重排和适配
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 模拟人类与移动 app 交互的认知过程（explore→select→derive→recall），将任务过程分解为更小的模块化子任务；子任务具有结构性、可复用、可重排和可适配特征。将交互轨迹结构化为可组合的 module 具有 Schematic 特征。

[Title]: MapAgent: Trajectory-Constructed Memory-Augmented Planning for Mobile Task Automation
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Historical task execution trajectories on mobile devices
- [Target Experience]: Structured page-memory database — each page as compact snapshot capturing UI layout and functional context
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: coarse-to-fine task planning 检索相关页面注入 LLM planner
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: trajectory-based memory mechanism 将任务执行轨迹转化为结构化 page-memory database：每页提取为紧凑快照，同时捕捉 UI layout 和 functional context。从时间序列轨迹到结构化页面数据库属于 P2 转化。

[Title]: WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Raw navigation logs from web browsing sessions
- [Target Experience]: Concise summaries (WebCondenser) + episodic experiences (External Memory Store) → task-specific advice (Coach)
- [Source Modality]: [vis+txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Coach 基于 similarity 和 recency 决定是否通过 runtime hooks 注入 task-specific advice
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 三个组件：WebCondenser 将原始导航日志标准化为简洁摘要 (P1 抽象)；External Memory Store 以 episodic experiences 形式组织完整轨迹；Coach 检索相关经验并决定是否注入建议。持续策展 episodic memory 实现 self-evolution without retraining。

[Title]: Get Experience from Practice: LLM Agents with Record & Replay
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Agent's interaction trace with environment and internal decision process
- [Target Experience]: Structured "experiences" — multi-level abstracted workflows with constraints (encapsulating workflow and constraints)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {human}
- [Utilization]: Replay 在后续类似任务中指导 agent 行为；支持 user-recorded demonstration, large-small model collaboration, privacy-aware execution
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 经典的 record-and-replay 范式引入 AI agent：记录 agent 与环境交互轨迹及内部决策过程 → 摘要为结构化"经验"封装工作流和约束 → 在后续类似任务中重放。多级经验抽象方法在 specificity 和 generality 之间平衡；check function mechanism 作为信任锚确保重放完整性和安全性。

[Title]: ViReSkill: Vision-Grounded Replanning with Skill Memory for LLM-Based Planning in Lifelong Robot Learning
- [Pathway]: Narrative → Narrative (P1) + Narrative → Schematic (P2)
- [Source Experience]: Failed execution attempts (triggering replanning) + successful execution plans
- [Target Experience]: Reusable skills — stored executable plans replayed in future encounters
- [Source Modality]: [embodied]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在 future encounters 中直接重放 skill 而无需额外 LLM/VLM 调用
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 失败时 vision-grounded replanner 基于当前场景生成新动作序列 (Narrative)；成功时执行计划存储为可复用 skill（具有可执行性，含 Schematic 特征）。每次尝试立即扩展 skill set 并稳定后续执行。同时产出 Narrative plan 和 Schematic executable skill。

[Title]: R2D2: Remembering, Replaying and Dynamic Decision Making with a Reflective Agentic Memory
- [Pathway]: Narrative → Schematic (P2) + Narrative → Narrative (P1)
- [Source Experience]: Web navigation experiences (past mistakes + visited pages)
- [Target Experience]: Replay buffer — detailed "map" of previously visited pages (Schematic) + error analysis and strategy refinement (Narrative)
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Remember paradigm 重建 web 环境减少导航错误；Reflect paradigm 从错误中学习改进策略
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Remember & Reflect 双范式：Remember 用 replay buffer 动态重建 web 环境形成页面"地图"(Schematic, P2)；Reflect 通过错误分析和策略精炼学习 (Narrative, P1)。两个产出并列不构成链式衔接。

[Title]: EE-MCP: Self-Evolving MCP-GUI Agents via Automated Environment Generation and Experience Learning
- [Pathway]: Narrative → Narrative (P1) + Narrative → Policy (P5)
- [Source Experience]: Agent-environment interaction trajectories in MCP-GUI hybrid settings
- [Target Experience]: LLM-learned rules in experience bank (Narrative) + training data for distillation (Policy update)
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: experience bank 实现推理时无 fine-tuning 改进 (P1)；distillation 用于 SFT policy (P5)
- [Method]: ⟨LLM-extract⟩, ⟨SFT⟩
- [Mechanism]: 双轨 self-evolution：experience bank 从 trajectory comparison 中积累规则实现推理时改进 (P1)；distillation 将轨迹转化为 SFT 训练数据更新 policy (P5)。GUI-intensive 任务用 experience bank，MCP-dominant 任务用 distillation。Multi-target: 同时产出 Narrative rules 和 Policy (SFT updated weights)。

[Title]: UI-Evol: Automatic Knowledge Evolving for Computer Use Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Actual agent-environment interactions (execution traces)
- [Target Experience]: Refined external knowledge — faithful action sequences + critiqued knowledge
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 作为 refined external knowledge 注入 agent 提升任务执行
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 两阶段解决 knowledge-execution gap（90% 正确知识仅 41% 执行成功率）：Retrace Stage 从实际交互提取忠实 action sequence；Critique Stage 将 Retrace 序列与 external references 对比精炼知识。

[Title]: Open-Ended Instructable Embodied Agents with Memory-Augmented Large Language Models
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Human-robot dialogue (instruction, correction, VLM descriptions) + action plans
- [Target Experience]: Language-program pairs in external memory
- [Source Modality]: [embodied]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: retrieval-augmented LLM prompting：基于当前 dialogue 检索 memories 作 in-context examples
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: HELPER 将人机对话与 action program 配对存入外部记忆；部署中记忆持续扩展以包含用户语言和动作计划对，个性化到用户的语言和 routine。

[Title]: AriGraph: Learning Knowledge Graph World Models with Episodic Memory for LLM Agents
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Environmental exploration experiences (semantic + episodic memories)
- [Target Experience]: Memory graph integrating semantic and episodic memories (knowledge graph world model)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: augmented with planning and decision-making for complex interactive text game tasks
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Agent 在环境探索中构建并更新整合语义和情景记忆的记忆图（knowledge graph world model）。非结构化探索经验 → 结构化图式世界模型，P2。

[Title]: WorkflowGen: an adaptive workflow generation mechanism driven by trajectory experience
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Full task execution trajectories (error fingerprints, optimal tool mappings, parameter schemas, execution paths, exception-avoidance strategies)
- [Target Experience]: Workflow templates at both node and workflow levels — reusable structured knowledge
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 三级自适应路由：direct reuse, rewriting-based generation, full initialization
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 从完整轨迹中提取节点和 workflow 级别的可复用结构化知识；闭环机制通过 trajectory rewriting, experience updating, template induction 仅在可变节点做轻量生成。

[Title]: From Procedural Skills to Strategy Genes: Towards Experience-Driven Test-Time Evolution
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Past execution experiences including failure history
- [Target Experience]: Compact "Gene" — control-oriented, evolution-ready experience encoding
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 作为 test-time control 和 iterative experience accumulation 的 substrate
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 探究经验表示形式的一阶影响：文档化 Skill package 控制不稳定，紧凑 Gene 表示在 one-shot control 和 iterative accumulation 均最优。从经验中蒸馏紧凑控制导向文本对象。核心发现：representation 本身是一阶因素。

[Title]: ICAL: Continual Learning of Multimodal Agents by Transforming Trajectories into Actionable Insights
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Generic sub-optimal multimodal demonstrations with human feedback
- [Target Experience]: Generalized programs with cognitive abstractions (task relationships, object state changes, temporal subgoals, task construals)
- [Source Modality]: [cross-modal]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}, {human}
- [Utilization]: 作为 retrieval-augmented LLM/VLM agent 的 exemplars；也可用于 fine-tuning (二次 P5)
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: VLM 从噪声 demonstration 抽象为通用程序：修正低效 action 并标注认知抽象。通过人类反馈交互精炼。与 Paper #8 为同一工作的长文版。

[Title]: Demo2Code: From Summarizing Demonstrations to Synthesizing Code via Extended Chain-of-Thought
- [Pathway]: Narrative → Narrative → Schematic (P1 + P2)
- [Source Experience]: Demonstrations — long robot task demonstrations
- [Target Experience]: Robot task code (executable programs)
- [Source Modality]: [embodied]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: 生成可执行 robot task code 用于机器人执行
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 两阶段链式转化：Stage 1 (P1): recursive summarization 将冗长 demonstration 压缩为 concise specification (Narrative intermediate)；Stage 2 (P2): code synthesis 从 specification 递归展开函数生成可执行 task code (Schematic)。

[Title]: H2R: Hierarchical Hindsight Reflection for Multi-Task LLM Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Past agent-environment interactions across diverse tasks
- [Target Experience]: Hierarchical memories — decoupled high-level planning memory + low-level execution memory
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 测试时分别检索高层和低层记忆，高效利用任务相关知识
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Hierarchical Hindsight Reflection 将过去交互按层次解耦蒸馏为高层规划记忆和低层执行记忆；测试时分层检索。核心创新在记忆的分层解耦组织。

[Title]: Reflection-Based Memory For Web navigation Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Both successful and failed past web navigation experiences
- [Target Experience]: Self-reflections — learned lessons from both successes and failures
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 跨 web navigation 任务转移复用 reflections
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: ReAP 利用 self-reflections 同时从成功和失败经验中学习；reflections 作为额外上下文注入后续任务。纯 P1。

[Title]: Generative Agents: Interactive Simulacra of Human Behavior
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Complete record of agent's experiences in natural language
- [Target Experience]: Higher-level reflections synthesized over time from accumulated memories
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: reflections 动态检索用于 plan behavior
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 范式性 P1 工作：observation（存储经验为 NL 记录）→ planning（基于记忆规划）→ reflection（随时间合成为更高层反思）。token 空间逐步提升抽象层次。

[Title]: A²Flow: Automating Agentic Workflow Generation via Self-Adaptive Abstraction Operators
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Expert demonstrations + LLM reasoning outputs across tasks
- [Target Experience]: Abstract execution operators — compact reusable building blocks for workflow construction
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}, {teacher}
- [Utilization]: 作为 reusable building blocks 构建 agentic workflow
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 三阶段：Case-based generation 从 expert demo 生成 operators → Operator Clustering 跨任务初步抽象 → Deep Extraction via long CoT 导出紧凑可泛化执行 operators。operator memory 保留历史输出丰富上下文。与 Paper #76 为同一工作复现。

[Title]: MemEvolve: Meta-Evolution of Agent Memory Systems
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Agent interaction experiences across diverse task contexts
- [Target Experience]: Jointly evolved experiential knowledge + memory architecture itself
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 跨任务跨 LLM 迁移；EvolveLab 将 12 种记忆系统统一到模块化设计空间
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 元进化框架同时进化经验内容和记忆架构本身——不仅积累经验，还精炼如何从经验中学习。EvolveLab 提供统一实验场。

[Title]: Agentic Plan Caching: Test-Time Memory for Fast and Cost-Efficient LLM Agents
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Completed agent executions with planning stages
- [Target Experience]: Structured plan templates — extracted, stored, adapted, and reused
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: keyword extraction 匹配新请求到缓存 plan，轻量模型适配 template 到 task-specific plan
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 从完成执行的 planning stage 提取结构化 plan templates；keyword extraction 匹配，轻量模型适配。不同于传统 semantic caching（缓存完整输出），提取和复用 plan 结构骨架（Schematic）。

[Title]: Self-Generated In-Context Examples Improve LLM Agents for Sequential Decision-Making Tasks
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Agent's own successful trajectories from past tasks
- [Target Experience]: Curated database of self-generated in-context examples
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 作为 in-context examples 在后续任务中注入
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Agent 从自身成功经验自动改进：积累成功轨迹为 in-context example database；population-based training 做 database-level curation 传播高质量 example 集合；exemplar-level curation 基于经验效用选择性保留轨迹。纯 P1，全部在 token 空间。

[Title]: Learn-by-interact: A Data-Centric Framework for Self-Adaptive Agents in Realistic Environments
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Agent-environment interaction histories (synthesized trajectories)
- [Target Experience]: Instructions (summaries/abstractions of interaction histories via backward construction)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: 在 training-based (SFT) 和 training-free (ICL) 场景中作为 agent data
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: backward construction 将 agent-environment 交互历史总结或抽象为 instructions；合成数据同时用于 ICL 的 retrieval 和 SFT training。当用于 SFT 时有 P5 二次转化，但主体在 P1 阶段。

[Title]: Learning from Online Videos at Inference Time for Computer-Use Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Online tutorial videos — converted into structured demonstration trajectories
- [Target Experience]: Actionable guidance — dynamically selected trajectory segments as in-context guidance
- [Source Modality]: [vis+txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: 推理时每步动态选择一条 trajectory 作为局部指导注入 context
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: VLM 推断 UI actions，将视频分割为 action 短子序列并分配 textual objective；两阶段选择机制在推理时每步动态选择最相关的 trajectory 片段注入。源经验来自人类视频教程，跨模态转化后以 Narrative 形式指导 agent。

[Title]: Keypoint Action Tokens Enable In-Context Imitation Learning in Robotics
- [Pathway]: Annotation Failed
- [Source Experience]: Visual observations + action trajectories
- [Target Experience]: Tokenized keypoint representations for in-context imitation
- [Source Modality]: [embodied]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: 不清楚
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 将视觉观察和动作轨迹转化为 keypoint action tokens 供 GPT-4 Turbo 进行 few-shot in-context visual imitation learning。此工作将 visual→action 的 demonstration 编码为 token 序列做 in-context learning，不涉及经验在不同载体间的语义转化（不是从经验中提取抽象知识或改变载体形式）。Abstract 描述的是输入输出表示工程（tokenization scheme）而非 experience transformation 机制。若按宽口径可能视为 raw demo → in-context example 的简单包装 (P1 边界)，但缺乏从经验中蒸馏/抽象/转化的核心机制。

[Title]: EchoTrail-GUI: Building Actionable Memory for GUI Agents via Critic-Guided Self-Exploration
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Successful GUI task trajectories validated by a reward model (from autonomous exploration)
- [Target Experience]: Curated database of past trajectories as actionable "memories"
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在 GUI Task Inference 阶段作为 in-context guidance 注入 agent 推理和决策
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 三阶段：Experience Exploration 中 agent 自主探索 GUI 环境，reward model 验证成功轨迹；Memory Injection 中检索最相关 past trajectories；GUI Task Inference 中作为 in-context memory 注入。纯 P1。

[Title]: Mirage-1: Augmenting and Updating GUI Agent with Hierarchical Multimodal Skills
- [Pathway]: Narrative → Narrative (P1) + Narrative → Schematic (P2)
- [Source Experience]: Agent trajectories in GUI environments (offline)
- [Target Experience]: Hierarchical Multimodal Skills (HMS): execution skills → core skills → meta-skills
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Skill-Augmented MCTS (SA-MCTS) 利用 skills 减少在线 tree exploration 的 action search space
- [Method]: ⟨LLM-extract⟩, ⟨MCTS⟩
- [Mechanism]: HMS 将轨迹逐层抽象为 execution skills → core skills → meta-skills 三层知识结构。高层 meta-skills 具有抽象策略特征 (Narrative)，低层 execution skills 接近可执行操作序列 (Schematic)。SA-MCTS 用 MCTS 在 skills 指导下高效在线探索。

[Title]: Meta-Agent-Workflow: Streamlining Tool Usage in LLMs through Workflow Construction, Retrieval, and Refinement
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: LLM tool-reasoning processes / execution traces
- [Target Experience]: Task-specific workflows — structured, retrievable, updatable workflow representations
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 检索 workflows 供不同任务复用；基于执行反馈更新
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 将 LLM 的 tool-reasoning 过程转化为 task-specific workflows（结构化表示）；支持通过不同查询方式检索和基于执行反馈更新。工业应用导向：workflow 可通过可视化界面配置。

[Title]: Memex(RL): Scaling Long-Horizon LLM Agents via Indexed Experience Memory
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Full-fidelity interaction history (tool outputs, intermediate reasoning)
- [Target Experience]: Compact working context (concise structured summaries + stable indices) + external experience database
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: agent 决定何时 dereference index 恢复精确 past evidence 用于当前 subgoal
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: MemexRL 用 RL 训练 agent 学习 indexed memory 的读写策略：什么 summarize、什么 archive、如何 index、何时 retrieve。压缩 context 但不丢弃证据——维持 indexed summaries 在 working context 中，完整交互存储在外部数据库。关键在 RL 训练的 memory management policy 而非经验转化本身，但 summaries 的产生是 P1 抽象。

[Title]: FlowMind: Execute-Summarize for Structured Workflow Generation from LLM Reasoning
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: LLM task execution traces (tool use sequences)
- [Target Experience]: Structured workflows — independently reconstructed from execution traces
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 可靠地将自由形式 LLM reasoning 转化为结构化 workflows
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Execute-Summarize 解耦执行和构建：先完成任务（执行），再独立从 execution trace 重构结构化 workflow（总结）。分离避免两过程相互干扰——解决了"边执行边构建 workflow"的准确性损失问题。

[Title]: Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Complete computer control trajectories (abstracted states + actions)
- [Target Experience]: Exemplars stored in exemplar memory — trajectory-as-exemplar with embedding-based retrieval
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: similarity search 检索 exemplars 作为 in-context learning 的 demonstration
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: state abstraction 过滤不相关信息允许更多 exemplars 进入 context；trajectory-as-exemplar prompting 以完整轨迹（abstracted states + actions）作为 in-context demonstration；exemplar memory 通过 embedding similarity 检索泛化到新任务。

[Title]: BAGEL: Bootstrapping Agents by Guiding Exploration with Language
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Randomly explored trajectories or synthetic instructions (seed set)
- [Target Experience]: Refined demonstrations — well-described trajectories via round-trip LM refinement
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 作为 in-context demonstrations 在测试时适应 zero-shot LM agent
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 通过两 noisy LM component 之间的 round-trip 迭代：LM labeler 将 trajectory 转为 synthetic instruction，zero-shot LM agent 将 instruction 映射为 refined trajectory。多轮迭代使 trajectory 分布收敛至 well-described by NL 的状态。纯 P1：raw trajectory → refined demo。

[Title]: Skill Learning Using Process Mining for Large Language Model Plan Generation
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Execution traces / event logs from LLM plan execution
- [Target Experience]: Process models (structured skill representations) + skill library
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: process discovery for skill acquisition, process models for storage, conformance checking for retrieval
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 将 process mining 技术引入 LLM skill learning：process discovery 从执行日志中获取 skills → process models 存储 skills（结构化流程模型）→ conformance checking 做 skill retrieval。将轨迹经验转化为结构化 process model (Schematic)。

[Title]: MaP-AVR: A Meta-Action Planner for Agents Leveraging Vision Language Models and Retrieval-Augmented Generation
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Human-annotated planning demonstrations (self-augmenting as system succeeds)
- [Target Experience]: Meta-action database — demonstrations abstracted as {move/rotate, end-effector status change, environment relationship}
- [Source Modality]: [embodied]
- [Target Modality]: [txt]
- [Experience Source]: {human}, {self}
- [Utilization]: RAG 检索 database 中 demonstrations 做 in-context learning；database self-augment 持续扩展
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 将 planned result 抽象为 meta-actions（三要素：move/rotate, end-effector status change, environment relationship）；RAG 从 human-annotated + self-augmented database 检索 demonstrations。核心是计划表示的抽象化（Narrative 内）。

[Title]: Large Language Models Are Semi-Parametric Reinforcement Learning Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Past episodes (both success and failure experiences from RL task sets)
- [Target Experience]: Updated long-term experience memory — evolved via Reinforcement Learning with Experience Memory (RLEM)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 作为 long-term experience memory 在后续 episodes 中指导 agent
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: REMEMBERER 将 LLM 配备长期经验记忆，RLEM 利用 RL 信号更新记忆内容（不更新 LLM 参数）；系统从成功和失败经验中学习并进化。"semi-parametric"指参数部分 (LLM) + 非参数部分 (memory) 的组合架构。纯 P1。

[Title]: TRAD: Enhancing LLM Agents with Step-Wise Thought Retrieval and Aligned Decision
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Complete agent trajectories from sequential decision making tasks
- [Target Experience]: Step-level thought demonstrations — retrieved via thought matching with preceding/subsequent steps
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Thought Retrieval 做 step-level demonstration selection；Aligned Decision 补充前后步骤提供容错和平衡
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 不检索完整 trajectory 而检索 step-level thought：Thought Retrieval 通过 thought matching 实现步骤级 demonstration 选择减少噪声；Aligned Decision 补充前后步骤提供对 imperfect thought 的容错。纯 P1，创新在检索粒度。

[Title]: SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents
- [Pathway]: Narrative → Narrative (P1) + Narrative → Schematic (P2)
- [Source Experience]: Task execution trajectories within each task family
- [Target Experience]: Skill patches externalized via trajectory- and rubric-driven updates
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 携带更新后的 skill library 到后续任务
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Agent 从零开始（无预置 skills），按家族顺序解决任务，通过 trajectory- 和 rubric-driven skill patches 外化经验教训。评估 lifelong skill discovery, patching, transfer 及失败模式。是 benchmark 论文，本身不引入新转化机制，但评估了 P1+P2 路径的 lifelong 表现。

[Title]: MemGPT: Towards LLMs as Operating Systems
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Full conversation/document history beyond context window
- [Target Experience]: Managed memory tiers — compressed/summarized context in limited context window
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: virtual context management: 通过 fast/slow memory 之间的数据移动提供 extended context 的 illusion
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 受 OS 分层记忆启发：通过 interrupts 管理控制流，在 fast memory (context window) 和 slow memory (external storage) 之间移动数据。将长对话历史通过 summarization 压缩后移入 context。属于 P1 的记忆管理基础设施。

[Title]: SkillLearnBench: Benchmarking Continual Learning Methods for Agent Skill Generation on Real-World Tasks
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Agent experiences from task execution
- [Target Experience]: Generated skills — evaluated at skill quality, execution trajectory, task outcome levels
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 作为 skills 供 agent 在后续任务中使用
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Benchmark 论文：评估 continual skill learning 方法。关键发现：continual learning 在具有清晰可复用工作流的任务上改善明显，但在开放式任务上挣扎；更强 LLM backbone 并不一致产生更好 skills；多轮迭代中 external feedback 驱动真正改进而 self-feedback alone 引发 recursive drift。

[Title]: ShowUI-Aloha: Human-Taught GUI Agent
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Unstructured human screen recordings (desktop) — mouse clicks, keystrokes, scrolls
- [Target Experience]: Structured, annotated tasks — descriptive NL captions + action plans
- [Source Modality]: [vis+txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: 作为训练/指导数据供 GUI agent 学习
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 四组件 pipeline：Recorder 捕获屏幕和精确用户交互；Learner 语义解释原始交互并翻译为 NL captions；Planner 读取 parsed demonstrations 动态制定高层 action plan；Executor 在 OS 级别忠实执行。核心是 human demonstration → structured agent task 的 P1 转化。

[Title]: R+X: Retrieval and Execution from Everyday Human Videos
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Long unlabelled first-person human videos of everyday tasks
- [Target Experience]: Short relevant video clips (retrieved) → robot skills via in-context imitation
- [Source Modality]: [embodied]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: VLM 检索相关行为片段，in-context imitation learning (KAT) 执行 skill
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: VLM 检索长视频中相关片段（无需标注），in-context imitation learning 将检索片段作为条件执行 skill。利用 KAT (Paper #80) 的 tokenization 方案将 visual demo 转为 in-context example。探索性的 P1 跨模态转化。

[Title]: SkillNet: Create, Evaluate, and Connect AI Skills
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Heterogeneous sources of agent experience
- [Target Experience]: Skills organized in unified ontology — structured, interconnected, multi-dimensionally evaluated
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 20万+ skills 供 agent 在 ALFWorld, WebShop, ScienceWorld 中复用
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 开放基础设施从异构来源创建、评估、组织 AI skills：统一本体论结构化 skills，支持多维度评估 (Safety, Completeness, Executability, Maintainability, Cost-awareness)，建立关系连接。核心是技能基础设施而非新颖转化机制。

[Title]: GraSP: Graph-Structured Skill Compositions for LLM Agents
- [Pathway]: Out of Scope
- [Mechanism]: GraSP 在 skill retrieval 和 execution 之间引入 compilation layer，将 flat skill sets 转化为 typed DAGs with precondition-effect edges，执行 node-level verification 和 locality-bounded repair。工作聚焦于已有 skills 的组合编排（orchestration）而非从经验中生成新 skills。属于 skill utilization/orchestration 层面的贡献，不涉及经验在不同载体间的转化（不满足 Transformation 判定标准：没有从源经验生成新载体产物）。

[Title]: TroVE: Inducing Verifiable and Efficient Toolboxes for Solving Programmatic Tasks
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Primitive function usage in programmatic task solutions
- [Target Experience]: Reusable high-level function toolbox — curated, trimmed, verifiable
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 用 toolbox 中的函数替代 primitive functions 编写更简洁准确的程序
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 通过"generating via using, growing, and periodically trimming"的循环：从已有程序中识别可复用模式合成为高层函数，周期修剪 toolbox 保持紧凑。将程序编写经验转化为可复用函数库 (Schematic)。

[Title]: A Benchmark for Procedural Memory Retrieval in Language Agents
- [Pathway]: Out of Scope
- [Mechanism]: 构建了首个隔离 procedural memory retrieval 与 task execution 的 benchmark。用 ALFWorld 构建 expert 和 LLM-generated trajectory 双语料库，评估六种检索方法。工作聚焦于评估和诊断 retrieval 机制（识别功能等价 procedures 的跨上下文迁移），而非从经验中转化生成新载体产物。不满足 Transformation 判定标准。

[Title]: Memento: Fine-tuning LLM Agents without Fine-tuning LLMs
- [Pathway]: Narrative → Narrative (P1) + Narrative → Policy (P5)
- [Source Experience]: Past agent experiences from deep research tasks
- [Target Experience]: Neural case-selection policy (Memory-augmented MDP with differentiable/non-parametric episodic memory)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: memory-based online RL 通过 memory rewriting mechanism 持续更新 case-selection policy
- [Method]: ⟨LLM-extract⟩, ⟨RL: PPO⟩
- [Mechanism]: 形式化 Memory-augmented MDP：episodic memory 存储过去经验（Narrative），neural case-selection policy 指导 action 决策，通过 memory rewriting 基于环境反馈持续更新。Policy improvement 通过高效 memory reading (retrieval) 实现而非参数更新。核心是 memory rewriting 作为 policy improvement 的替代路径。case-selection policy 涉及轻量参数训练（neural），具有 Narrative → Policy 的 P5 特征。

[Title]: In-Context Ensemble Learning from Pseudo Labels Improves Video-Language Models for Low-Level Workflow Understanding
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Recordings of human demonstrations (video of software workflows)
- [Target Experience]: Standard Operating Procedures (SOP) — step-by-step written workflow guides
- [Source Modality]: [vis+txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: SOP 用于 automated end-to-end software workflow execution
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 从人类演示视频生成 SOP：in-context ensemble learning 聚合多个可能 SOP 路径的 pseudo labels，通过 implicit consistency regularization 超越 context window 限制。跨模态 P2：video demo → written SOP (Schematic workflow)。

[Title]: Code Models are Zero-shot Precondition Reasoners
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Demonstration trajectories of sequential decision-making tasks
- [Target Experience]: Action preconditions in code representation
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: precondition-aware action sampling 确保 policy 预测的 actions 与 preconditions 一致
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 利用预训练 code model 从 demonstration trajectory 中 zero-shot 提取 action preconditions（以代码表示）。extracted preconditions 用于约束 policy 的 action sampling。代码表示的 preconditions 是结构化约束，以 code form 表达从经验中提取的"何时可以执行某动作"的知识。

[Title]: HiAgent: Hierarchical Working Memory Management for Solving Long-Horizon Agent Tasks with Large Language Model
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: In-trial action-observation pairs (working memory)
- [Target Experience]: Subgoal-chunked memory — hierarchically managed working memory with summarized observations
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 仅保留当前 subgoal 相关的 action-observation pairs，用 summarized observations 替换先前 subgoals
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 以 subgoals 作为记忆块层级管理 working memory：LLM 在生成动作前先制定 subgoals，主动决定用 summarized observations 替换先前 subgoals。是 working memory 的管理策略（P1 抽象压缩），不涉及跨载体转化。

[Title]: Automatic Control With Human-Like Reasoning: Exploring Language Model Embodied Air Traffic Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Agent interactions with air traffic simulator
- [Target Experience]: Experience library — vector database storing synthesized knowledge from interactions
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在后续冲突解决中检索合成知识以增强决策；提供 human-level text explanations
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Experience library 是向量数据库存储 agent 从与模拟器交互和 LLM 推理中学到的合成知识。纯 P1：interaction → synthesized knowledge 的 token 空间转化。

[Title]: How Well Do Agentic Skills Work in the Wild: Benchmarking LLM Skill Usage in Realistic Settings
- [Pathway]: Out of Scope
- [Mechanism]: Benchmark 论文研究 skill utility 在 realistic settings 下的退化：agents 需从 34k real-world skills 中自主检索和选择。评估 skill refinement strategies (query-specific/query-agnostic)。聚焦于 skill 使用和检索效果评估，不涉及经验转化为 skills 的过程。不满足 Transformation 判定标准。

[Title]: From Logs to Agents: Reconstructing High-Level Creative Workflows from Low-Level Raw System Traces
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Low-level raw system traces (csv/JSON logs: clicks, parameter tweaks, metadata updates)
- [Target Experience]: Structured behavioral workflow graphs — mapping provenance and flow of creative assets
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: 下游分析 (sequence mining, probabilistic modeling)；"Process-Aware Agents" 的先决条件
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 解析原始 csv/JSON 日志为结构化行为工作流图——将低级系统事件抽象为高级行为 tokens (MODIFY_Prompt, GENERATE_Image 等)，映射创作资产的 provenance 和 flow。low-level system traces → structured workflow graphs 的 P2。

[Title]: View-oriented Conversation Compiler for Agent Trace Analysis
- [Pathway]: Out of Scope
- [Mechanism]: VCC 是一个编译器（lex, parse, IR, lower, emit）将原始 agent JSONL logs 转化为多种结构化视图：full view, UI view, adaptive view。聚焦于 agent trace 的格式转换和表示工程以改善 downstream analysis 质量。属于 infrastructural tooling（trace formatting/compilation），不涉及经验的语义转化或载体间的经验迁移。不满足 Transformation 判定标准。

[Title]: Workflow Graphs: A Computational Model of Collective Task Strategies for 3D Design Software
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Multi-user screen recording videos, command log data, task content history
- [Target Experience]: Workflow graphs (W-graphs) — nodes represent equivalent intermediate task states, edges represent user transitions
- [Source Modality]: [vis+txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: 支持 workflow feedback, on-demand task guidance, instructor dashboards 等 novel user interfaces
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 从多用户 screen recordings, command logs, 3D model snapshots 构建 W-graphs：编码多用户执行同一 3D 设计任务时方法的收敛和分歧。跨用户经验聚合为结构化图模型 (Schematic)。

[Title]: ReGAL: Refactoring Programs to Discover Generalizable Abstractions
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Existing programs (small set of programs written for specific tasks)
- [Target Experience]: Library of reusable functions — discovered through code refactorization without changing execution output
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: 共享函数库使 LLM 更准确地预测程序；封装常用子例程和环境动态
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: gradient-free 方法：从已有程序集中通过代码重构（restructuring without changing execution output）迭代发现可复用函数库，通过执行验证和精炼。abstractions 封装 frequent subroutines 和 environment dynamics。从扁平程序到可复用函数库的 P2。

## Annotation Failures
- 「Keypoint Action Tokens Enable In-Context Imitation Learning in Robotics」(block #80) —— Abstract 描述表示工程（tokenization scheme），将 visual observations 和 action trajectories 编码为 keypoint tokens 供 in-context imitation。不涉及经验在不同载体间的语义转化（没有从经验中蒸馏/抽象/结构化的核心机制）。若按最宽泛口径可能视为 raw demo → in-context example 的简单包装，但缺乏本 Survey 定义的 Transformation 机制。

## New Tags Introduced

无需新增标签——所有标注均使用 Notions.md 现有标签集合完成。

## Parser Errors

无 parser 错误。
