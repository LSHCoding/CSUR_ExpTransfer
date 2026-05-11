[Title]: Agent KB: Leveraging Cross-Domain Experience for Agentic Problem Solving
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: raw trajectories from heterogeneous agent frameworks (smolagents, OpenHands, OWL) across diverse benchmarks
- [Target Experience]: structured knowledge base entries comprising cross-domain workflows and diagnostic fixes
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: hybrid retrieval at inference time — planning stage seeds agents with cross-domain workflows, feedback stage applies targeted diagnostic fixes; disagreement gate filters knowledge interference
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 将来自多个 agent 框架的原始轨迹聚合为统一的结构化知识库，提供轻量级 API。混合检索分两阶段运作：规划阶段检索跨域工作流以初始化 agent 策略，反馈阶段在执行偏离时检索诊断修复方案。disagreement gate 确保检索到的知识增强而非干扰推理，解决跨框架知识干扰问题。

[Title]: SkillX: Automatically Constructing Skill Knowledge Bases for Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: raw execution trajectories from a strong backbone agent (GLM-4.6) across diverse tasks
- [Target Experience]: three-tiered hierarchical skill library (strategic plans → functional skills → atomic skills), iteratively refined and expanded
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: plug-and-play skill knowledge base reusable across different agents and environments; transferred to weaker base agents for performance improvement
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 三项协同创新：(i) Multi-Level Skills Design 将原始轨迹蒸馏为三层层级——strategic plans、functional skills 与 atomic skills——捕获不同抽象层次；(ii) Iterative Skills Refinement 基于执行反馈自动修订 skills 以提升库质量；(iii) Exploratory Skills Expansion 主动生成并验证超出种子训练数据的新 skills 以扩大覆盖范围。所得 SkillKB 全自动化且可复用，无需参数更新。

[Title]: Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: a diverse pool of agent execution trajectories across spreadsheet, VisionQA, and math reasoning domains
- [Target Experience]: a unified, conflict-free declarative skill directory — comprehensive natural language guides distilled via holistic analysis
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: declarative skills applied at inference time as guidance; transferable across LLM scales without parameter updates, retrieval modules, or model-specific tuning
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 派遣并行 sub-agent 舰队对多样化执行池进行整体分析，而非对单个轨迹逐条反应。每个 sub-agent 提取轨迹特定的教训，随后通过归纳推理层次化整合为统一、无冲突的 skill 目录。显式规避了对轨迹局部特性的顺序过拟合。Skills 为声明式自然语言形式，可跨 LLM 规模迁移——例如 Qwen3.5-35B 演化的 skills 将 Qwen3.5-122B agent 提升达 57.65 个绝对百分点。

[Title]: Memp: Exploring Agent Procedural Memory
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: past agent task execution trajectories
- [Target Experience]: dual-form procedural memory — fine-grained step-by-step instructions and higher-level script-like abstractions
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: retrieval at inference time for analogous tasks; memory repository migrates from stronger to weaker models with retained performance gains
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 将过往 agent 轨迹蒸馏为双形式程序性记忆：细粒度逐步指令捕获执行细节，高层脚本式抽象提供浓缩的任务模式。动态维护机制在新经验到达时持续更新、修正与淘汰记忆内容。该程序性记忆与模型无关——由强模型构建的记忆迁移至弱模型时仍保留价值。全程推理时运作，无参数更新。

[Title]: AgentDistill: Training-Free Agent Distillation with Generalizable MCP Boxes
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: teacher agent's task-solving behavior and operational knowledge, expressed through its interactions with planning, memory, and tool-use tasks
- [Target Experience]: structured, reusable Model-Context-Protocol (MCP) boxes — modular task-solving units with formal API interfaces
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: direct reuse by student agents at inference time without any training; MCP boxes encapsulate reusable task-solving protocols enabling cross-domain generalization
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Teacher agent 自主生成结构化 MCP (Model-Context-Protocol) box——具有形式化接口的可复用任务解决模块——通过将其操作知识蒸馏为结构化协议。与传统蒸馏重放轨迹或模仿逐步动作不同，AgentDistill 产出可复用的结构化模块。Student agent 在推理时直接调用这些 MCP box，实现免训练的知识迁移，可跨域泛化。该框架不同于标准 P7（外部化），因为源是 teacher 的任务解决行为（Narrative）而非其参数权重；亦不同于 P5，因为不发生策略训练。

[Title]: AutoRefine: From Trajectories to Reusable Expertise for Continual LLM Agent Refinement
- [Pathway]: Narrative → Narrative (P1) with parallel Narrative → Schematic (P2) for code snippets
- [Source Experience]: agent execution histories across ALFWorld, ScienceWorld, and TravelPlanner
- [Target Experience]: dual-form Experience Patterns — specialized subagents with independent reasoning and memory (for procedural subtasks), and skill patterns as guidelines or code snippets (for static knowledge)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: continual refinement — patterns retrieved for new tasks, reused across task instances; maintenance prevents repository degradation over time
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 提取双形式 Experience Pattern 以克服扁平文本知识的局限。对程序性子任务，提取专用 subagent——具有独立推理和记忆的封装 agent 模块，捕获复杂子任务的程序逻辑。对静态声明式知识，提取 skill pattern 作为自然语言指南或代码片段（代码片段路径为 P2: N→S）。持续维护机制对 patterns 进行评分、剪枝与合并，防止仅追加式记忆系统中累积驱动的退化。双形式提取是本文相比先前仅产出扁平文本工作的核心贡献。

[Title]: Skill-Pro: Learning Reusable Skills from Experience via Non-Parametric PPO for LLM Agents
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: episodic interaction narratives from agent task execution
- [Target Experience]: executable Skills with formally defined activation, execution, and termination conditions, managed via a Skill-MDP
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: reusable across in-domain, cross-task, and cross-agent scenarios with extreme memory compression; score-based maintenance sustains compact procedural memory
- [Method]: ⟨hybrid⟩
- [Mechanism]: 通过 Skill-MDP 框架将被动的 episodic narrative 形式化为可执行 Skill，每个 Skill 由显式的激活、执行与终止条件定义，确保可执行性。核心方法 Non-Parametric PPO 无需参数更新：语义梯度（LLM 生成的文本批评）驱动高质量候选 Skill 生成，PPO Gate 在准入前对候选 Skill 执行鲁棒验证。此为 P2 (N→S)，因为转化产出的是带形式条件的可执行 Skill 结构而非叙述性描述——Skill-MDP 形式化与 PPO Gate 验证构成超越单纯抽象的形式化步骤。

[Title]: Compiled Memory: Not More Information, but More Precise Instructions for Language Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: accumulated task successes and failures from agent execution on CUAD contract analysis and HotpotQA
- [Target Experience]: evolved system prompt with learned sub-bullets — precise, verified instructions distilled from task experience
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: rewritten system prompt governs agent behavior at inference time; compiled knowledge transfers across models (GPT-4o → Claude Sonnet 4.5)
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Atlas 将记忆视为蒸馏而非存储。从 agent 成功与失败中提取的事实通过三步 promotion gate 进行验证（确保训练信号约束：演化后的 prompt 恰好学习所教内容，不多不少）。验证后的事实通过以学习到的子要点重写 agent system prompt 的方式交付——交付方式是指令重写而非上下文注入。关键在于，编译后的知识是 task-shaped 而非 model-shaped，可实现跨模型迁移而不退化。

[Title]: Traversal-as-Policy: Log-Distilled Gated Behavior Trees as Externalized, Verifiable Policies for Safe, Robust, and Efficient Agents
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: sandboxed OpenHands execution logs from successful and unsafe trajectories across software, web, reasoning, and safety benchmarks
- [Target Experience]: a single executable Gated Behavior Tree (GBT) — each node encodes a state-conditioned action macro with pre-execution safety gates
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: GBT traversal replaces unconstrained LLM generation as the control policy at runtime; the visited path forms compact spine memory replacing full transcript replay
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 将 OpenHands 执行日志蒸馏为 Gated Behavior Tree (GBT)——一种形式化的可执行控制结构。每个树节点编码一个状态条件化的 action macro，从成功轨迹中挖掘并经合并校验得到。不安全轨迹涉及的 macros 接受确定性执行前门控，基于结构化工具上下文与有界历史，并在经验基单调性下更新（先前拒绝的不安全上下文不可重新准入）。运行时，轻量级 traverser 将基模型意图匹配至子 macros，在全局与节点局部门控下一次执行一个 macro，卡住时执行风险感知的最短路径恢复至可行成功叶节点。访问路径形成紧凑 spine memory。此为 P2 (N→S)，因为转化产出的是形式化可执行树结构——非叙事性引导，而是可验证的控制策略。

[Title]: SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning
- [Pathway]: Narrative → Narrative → Policy (§8.3)
- [Source Experience]: raw agent trajectories from task execution
- [Target Experience]: hierarchical skill library (SkillBank) + updated policy weights via RL
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: skill retrieval augments agent reasoning during RL-based policy improvement; skill library co-evolves with policy for recursive enhancement
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 复合流水线分两阶段。阶段一 (P1)：基于经验的蒸馏从原始轨迹构建层次化 SkillBank，提取高层可复用行为模式，token 占用大幅缩减。阶段二（P5 with skill augmentation）：自适应检索在基于 RL 的策略训练中提供通用与任务特定 skill 启发，skill 库通过递归演化与 agent 策略协同进化——随着策略改进，新经验反馈回 skill 发现，精化后的 skills 进一步增强策略训练。复合路径为 N→N (skill 提取) → Policy (RL 训练)，对应 §8.3 (Narrative → Narrative → Policy)。论文贡献在于连接 skill 发现与基于 RL 策略改进的协同演化循环中的整合机制。

[Title]: Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: agent interaction experiences from BFCL-V3 and AppWorld task execution
- [Target Experience]: multi-faceted procedural memory entries — success patterns, failure trigger analyses, and comparative insights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: context-adaptive reuse via scenario-aware indexing; utility-based refinement maintains compact, high-quality memory pool; memory scaling effect enables smaller models with memory to outperform larger memoryless models
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: ReMe 以三种机制贯穿完整记忆生命周期进行创新。(1) 多面蒸馏通过识别成功模式、分析失败触发因素并生成对比洞察来提取细粒度经验——超越简单的成功/失败日志记录。(2) 上下文自适应复用通过场景感知索引而非朴素相似度检索，将历史洞察适配至新上下文。(3) 基于效用的精化自主添加有效记忆并淘汰过时记忆，解决仅追加式档案的被动累积问题。全程推理时运作；记忆缩放效应显示 Qwen3-8B+ReMe 超越无记忆的 Qwen3-14B。

[Title]: Agent Workflow Memory
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: agent trajectories from web navigation tasks across Mind2Web and WebArena (1000+ tasks, 200+ domains)
- [Target Experience]: commonly reused routines (workflows) — induced action patterns representing reusable task-solving procedures
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: workflows selectively provided to agent to guide subsequent action generation; applicable both offline (pre-induced from training examples) and online (induced on the fly from test queries)
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 通过识别重复出现的动作子序列从 agent 轨迹中归纳常用例程（workflows）。灵活支持离线模式（部署前从训练样本预归纳 workflows）与在线模式（测试时从查询中即时归纳 workflows）。检索到的 workflows 被注入 agent 上下文以指导后续动作生成，减少探索步骤。在跨任务、跨网站与跨域评估中随训练-测试分布差异扩大仍能鲁棒泛化。

[Title]: Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: natural execution feedback from agent task performance — task outcomes and failure signals, without labeled supervision
- [Target Experience]: evolving context playbooks — accumulations of refined strategies organized as system prompts and agent memory
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: offline optimization of system prompts and online optimization of agent memory; strategies are refined based on task outcomes without human labels
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: ACE 将 context 视为不断演化的 playbook，通过生成、反思与策展的模块化循环积累、精化并组织策略。结构化增量更新防止两种失败模式：简洁偏差（为追求简洁摘要而丢弃领域洞察）与上下文坍缩（迭代重写随时间侵蚀细节）。该框架利用自然执行反馈在无标注监督下自适应——策略基于是否改善任务结果而被生成、测试与精化。在 agent 与领域特定 benchmark 上持续优于静态基线。

[Title]: SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: web interaction practice experiences — agents autonomously explore websites, execute skills, and observe outcomes
- [Target Experience]: robust, parameterized skill APIs — lightweight, plug-and-play executable interfaces encapsulating web interaction patterns
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: APIs plug-and-play for web agents on WebArena and real-world websites; APIs synthesized by strong agents transfer to weaker agents with up to 54.3% improvement
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: SkillWeaver 通过三阶段循环在新网站上实现自主 skill 发现：(1) skill 发现——agent 探索网站并识别可操作的交互模式；(2) skill 练习——agent 执行已发现 skills 以收集练习经验；(3) skill 蒸馏——练习经验被蒸馏为鲁棒的参数化 API。迭代探索持续扩展轻量级即插即用 API 库。此为 P2 (N→S)，因为输出是可执行 API——结构化的参数化程序接口——而非叙事性引导。API 可跨 agent 迁移，无需参数更新。

[Title]: What Deserves Memory: Adaptive Memory Distillation for LLM Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: raw interaction sequences from agent task execution
- [Target Experience]: coherent episodic narratives + distilled semantic insights, filtered by prediction error as a data-driven retention criterion
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: agnostic to downstream memory management; distilled insights support efficient memory retention and retrieval for agent reasoning
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: NEMORI 以数据驱动的标准——可预测性——替代基于启发式的记忆设计（重要性评分、情感标签、事实模板）。两个级联模块：(1) Episodic Memory Integration 将原始交互转化为连贯叙事；(2) Semantic Knowledge Distillation 通过预测误差提取洞察——结果偏离预期最大的经验被视为最有保留价值。核心洞见是观察交互序列的内蕴属性（可预测性）为判定何者值得记忆提供了对设计者强加启发式的可行替代方案。

[Title]: Don't Retrieve, Navigate: Distilling Enterprise Knowledge into Navigable Agent Skills for QA and RAG
- [Pathway]: Out of Scope
- [Mechanism]: 源为静态企业文档语料，而非具有可映射至 (c,a,o,f) 决策过程语义的 agent 经验。转化流水线（文档聚类、LLM 摘要生成、可导航 skill tree 物化）将文档语料转化为用于导航式检索的结构化层级，属于面向 RAG 的知识组织范畴而非 agent 经验转化。agent 对树的导航是检索策略，非经验复用。

[Title]: ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: agent's self-judged successful and failed interaction experiences from web browsing and software engineering tasks
- [Target Experience]: generalizable reasoning strategies distilled into a memory bank, iteratively enriched via memory-aware test-time scaling
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: retrieved at test time to inform agent interaction; new learnings integrated back after each task; synergy with test-time scaling amplifies both memory quality and task performance
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 将自我判定的成功与失败经验中的可泛化推理策略蒸馏至 ReasoningBank。关键创新 Memory-Aware Test-Time Scaling (MaTTS) 在测试时放大 agent 交互，生成丰富多样的经验，为记忆合成提供更丰富的对比信号。这形成协同循环：更好的记忆引导更有效的 scaling，更丰富的 scaling 经验产出更高质量的记忆——建立了完全在 Narrative 域内的自强化 P1 循环。无参数更新；agent 纯粹通过记忆精化实现自我进化。这是纯 P1 (N→N) 精化循环而非 Policy → Narrative → Policy 复合，因为策略权重全程冻结。
[Title]: Inducing Programmatic Skills for Agentic Tasks
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: raw web interaction trajectories (N-Tok), consisting of primitive action sequences (click, type, etc.) and task outcomes on WebArena
- [Target Experience]: programmatic skills (S-Tok) — executable code/scripts that compose primitive actions into higher-level parameterized skills (e.g., search product, plan route), verified through programmatic checks during induction
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: induced skills are composed as higher-level actions to reduce step count (10.7–15.3% reduction) and reused across websites; incompatible skills are updated for website changes; no parameter updates required
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: ASI 即时运行三阶段循环——(1) Induce：LLM 分析原始动作轨迹，假设程序化 skill 实现；(2) Verify：程序化验证（执行检查）滤除错误 skills，提供文本式 skill 提取所缺乏的保证；(3) Utilize：已验证 skills 在推理时替代原始动作序列。程序优于文本 skills，因为在归纳过程中可进行确定性验证，这解释了相比文本 skill 方案的 11.3% 增益。
[Title]: SCOPE: Prompt Evolution for Enhancing Agent Effectiveness
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: execution traces (N-Tok) containing recurring Corrective failures (immediate errors) and Enhancement failures (suboptimal strategies), recorded from agent runs on HLE benchmark
- [Target Experience]: evolved system prompt (N-Tok) — a set of guidelines synthesized from traces, organized by a Dual-Stream mechanism into tactical rules (resolving specific error patterns) and strategic principles (evolving long-term heuristics)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: the evolved prompt replaces the static system prompt for subsequent tasks, improving HLE success rate from 14.23% to 38.64% without human intervention
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: SCOPE 将上下文管理构建为在线优化。双流合成：一流从错误轨迹中提取战术特异性（什么失败及为何失败），另一流提取战略通用性（跨任务模式）。Perspective-Driven Exploration 通过促使 agent 为同一上下文生成替代行动方案来多样化策略池，提升演化 prompt 中存在正确策略的概率。演化后的 prompt 是轨迹分析的直接产物——无参数更新。
[Title]: FLEX: Continuous Agent Evolution via Forward Learning from Experience
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: raw task execution trajectories (N-Tok) with success/failure outcomes across mathematical reasoning (AIME25), chemical retrosynthesis (USPTO50k), and protein fitness prediction (ProteinGym)
- [Target Experience]: structured experience library (N-Tok) — a curated collection of reflections, lessons, and strategies distilled from continual reflection on successes and failures during environment interaction
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: the experience library is consulted during new task episodes; experiences are inheritable across agents (experience inheritance phenomenon); supports a scaling law of experiential growth — more accumulated experience yields monotonically improving performance
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: FLEX 无梯度。每个任务 episode 后，agent 执行结构化反思：分析成功之处、失败之处及其原因，然后将这些观察蒸馏为经验库中的可复用条目。该库被组织用于后续任务中的检索。关键的是，库具有可继承性——以另一个 agent 的经验库初始化的 agent 超越从零开始的 agent，表明经验编码在 tokenized 载体而非模型特定参数中。scaling law 显示 agent 性能随库规模增长而可预测地提升。
[Title]: Learning on the Job: An Experience-Driven Self-Evolving Agent for Long-Horizon Tasks
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: raw sub-task execution trajectories (N-Tok) from long-horizon task decomposition and execution across multiple applications in the TAC productivity benchmark
- [Target Experience]: structured hierarchical experience (N-Tok) stored in a Memory Module, organized by abstraction level — from fine-grained sub-task lessons to coarse task-level plans
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: the Memory Module is queried during planning (to propose sub-task decompositions) and during execution (to guide action selection); accumulated experience transfers zero-shot to new tasks; enables the agent to evolve beyond static pretrained parameters
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: MUSE 组织层次化 Memory Module。每次子任务执行后，agent 自主反思其轨迹并通过基于 LLM 的抽象将原始轨迹转化为结构化经验。该经验在适当层级被整合回 Memory Module。模块因此随时间增长——完成更多任务的 agent 积累更丰富的经验，展现出越来越优越的任务完成能力。层次化设计确保细粒度子任务策略与高层计划均被捕获且可复用。
[Title]: AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials
- [Pathway]: Policy → Narrative → Policy (§8.7, P7+P5)
- [Source Experience]: publicly available web tutorials (human-generated, N-Tok) harvested from the internet, transformed into structured task specifications; teacher VLM agent executes these instructions in real web environments to produce multimodal trajectories
- [Target Experience]: student GUI agent policy weights (π-Par) trained via SFT on the synthesized trajectory dataset, covering both text-based HTML observations with function-calling API actions and vision-based screenshot observations with pixel-level actions
- [Source Modality]: [cross-modal]
- [Target Modality]: [cross-modal]
- [Experience Source]: {teacher}
- [Utilization]: the trained student agent achieves SOTA on WebArena (text-based) and ScreenSpot Web / Multimodal Mind2Web (visual web grounding); deployment cost is $0.55 per high-quality trajectory without human annotators
- [Method]: ⟨SFT⟩
- [Mechanism]: 三阶段合成流水线：(1) 专用分类模型从互联网收割并过滤 tutorial 类文本；(2) LLM 将这些文本转化为含逐步指令的结构化任务规范；(3) VLM agent 在真实浏览器环境中执行这些指令，产生多模态轨迹（HTML + screenshots + CoT 推理 + actions），同时基于 VLM 的评估器验证轨迹正确性。主要贡献在于合成流水线设计——将人类 web 知识转化为 agent 可执行的轨迹。下游对这些轨迹的 SFT 构成 P5 分支。
[Title]: Get Experience from Practice: LLM Agents with Record & Replay
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: agent interaction traces (N-Tok) recording both the environment interaction sequence and the internal decision process during task execution
- [Target Experience]: structured multi-level experience (N-Tok) — an abstracted representation encapsulating workflow steps and constraints, balanced across specificity (task-level details) and generality (cross-task patterns)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self} / {human}
- [Utilization]: stored experiences are replayed in subsequent similar tasks to guide agent behavior; supports multiple application modes: user-recorded task demonstration, large-small model collaboration, and privacy-aware agent execution; an envisioned experience repository enables cross-agent knowledge sharing
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: AgentRR 适配经典的 record-and-replay 范式。录制阶段，框架同时捕获 agent 与环境的交互轨迹及其内部决策过程。摘要阶段，多层次抽象方法将轨迹压缩为结构化经验——平衡特异性（保留任务相关细节）与通用性（支持跨任务复用）。check function 机制作为信任锚，验证重放经验的完整性与安全性。经验可源自 agent 自身执行 ({self}) 或用户录制的演示 ({human})。
[Title]: Explorer: Scaling Exploration-driven Web Trajectory Synthesis for Multimodal Web Agents
- [Pathway]: Policy → Narrative → Policy (§8.7, P7+P5)
- [Source Experience]: diverse web task intents generated through extensive exploration; an LMM agent navigates 49K unique URLs, producing 94K+ successful multimodal trajectories with 720K screenshots and 33M web elements
- [Target Experience]: Explorer model weights (π-Par) — a multimodal web agent policy trained via SFT on the synthesized trajectory dataset
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {teacher}
- [Utilization]: the trained Explorer agent is evaluated on both offline (Mind2Web, Multimodal-Mind2Web) and online (Mind2Web-Live, MiniWob++) benchmarks; data scaling is identified as a key driver of capability improvement
- [Method]: ⟨SFT⟩
- [Mechanism]: 合成配方分两阶段：(1) 探索——LMM agent 广泛浏览 web 以发现多样化任务意图，使用精化确保任务质量；(2) 执行——agent 完成这些任务，生成多模态轨迹（screenshots + actions + reasoning）。每条成功轨迹平均成本 28 美分。主要贡献在于探索驱动的合成方法论（P7 分支）。下游 SFT 在此数据集上训练 Explorer（P5 分支）。所得 94K 轨迹数据集是同类中规模最大、最多样化的。
[Title]: Contextual Experience Replay for Self-Improvement of Language Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: past task execution experiences (N-Tok) from web navigation tasks on WebArena and VisualWebArena, encompassing environment dynamics (what actions lead to what page states) and common decision-making patterns
- [Target Experience]: dynamic memory buffer (N-Tok) — synthesized, compressed representations of environment dynamics and recurring decision patterns, updated as new experiences accumulate
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {self}
- [Utilization]: relevant experiences are retrieved and injected into the agent's context window for new tasks, enabling training-free self-improvement; on VisualWebArena achieves 31.9%, on WebArena achieves 36.7% (51.0% relative improvement over GPT-4o baseline)
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: CER 完全在 agent 的 context window 内运行，无需参数更新。agent 完成任务后，轨迹被积累并由 LLM 合成为紧凑的动态 memory buffer。合成提取两类知识：环境动态（action → observation 的因果模式）和决策模式（哪些策略在何种上下文中有效）。面对新任务时，CER 检索最相关的合成经验并扩充 agent 的上下文。buffer 是动态的——新经验被纳入，过时经验被淘汰。全程 training-free：所有转化均通过 LLM 文本处理完成。
[Title]: Towards Internet-Scale Training For Agents
- [Pathway]: Policy → Narrative → Policy (§8.7, P7+P5)
- [Source Experience]: 150K websites annotated with agentic tasks by an LLM; teacher LLM agents (Qwen 3 235B) execute these tasks to produce trajectories, filtered by an LLM judge (82.6% accuracy) for success
- [Target Experience]: student agent policy weights (π-Par) — Qwen 3 1.7B fine-tuned on the filtered trajectory dataset, achieving 56.9% success rate competitive with frontier LLMs
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: the 1.7B student agent reaches 94.7% of Gemini 2.5 Flash performance while being orders of magnitude smaller and faster; code, models, and data released publicly
- [Method]: ⟨SFT⟩
- [Mechanism]: 三阶段 internet-scale pipeline：(1) Site Annotation——LLM 为 150K 网站标注 agentic tasks（以 97% 准确率识别有害内容作为数据筛选工具）；(2) Trajectory Generation——LLM agent 完成这些任务并生成轨迹；(3) Trajectory Filtering——LLM 评判轨迹成功与否（82.6% 准确率），仅保留高质量数据。核心贡献在于端到端合成 pipeline 在无需人工标注的条件下实现 internet scale（P7 分支）。筛选后的轨迹用于对小型 student model 进行 SFT（P5 分支）。从 teacher 到 student 的 235x 压缩下仍保持有竞争力的性能，体现了 pipeline 的有效性。
[Title]: RAGShaper: Eliciting Sophisticated Agentic RAG Skills via Automated Data Synthesis
- [Pathway]: Policy → Narrative → Policy (§8.7, P7+P5)
- [Source Experience]: teacher agent trajectories elicited through constrained navigation over InfoCurator-built information trees, explicitly demonstrating error correction and noise rejection behaviors under adversarial distractor conditions
- [Target Experience]: student RAG agent policy weights (π-Par) trained on the synthesized corpus, exhibiting superior robustness in noise-intensive and complex retrieval tasks
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: the trained student agent outperforms existing baselines on complex RAG tasks requiring error recovery and distractor rejection; the synthesis framework automates construction of realistic, noisy training data that manual annotation cannot scale to produce
- [Method]: ⟨SFT⟩
- [Mechanism]: RAGShaper 的合成框架包含两个创新组件：(1) InfoCurator——构建密集 information tree，在 Perception（表层噪声）和 Cognition（语义混淆）两个层面注入对抗性干扰项，营造逼真的检索挑战；(2) Constrained Navigation——迫使 teacher agent 在约束条件下导航这些信息树，激发错误纠正与噪声拒绝行为，生成显式展示恢复策略的轨迹。核心贡献在合成方法学（P7 分支），尤其是 constrained navigation 策略迫使 teacher 展现目标行为。下游 SFT 在这些轨迹上训练出鲁棒的 student agent（P5 分支）。
[Title]: Structured Distillation of Web Agent Capabilities Enables Generalization
- [Pathway]: Policy → Narrative → Policy (§8.7, P7+P5)
- [Source Experience]: synthetic web navigation trajectories generated by a teacher LLM (Gemini 3 Pro) across six web environments, structured by three modular LLM roles — Task Designer, Annotator, and Supervisor — that mirror human annotation workflows
- [Target Experience]: student agent policy weights (π-Par) — a 9B model fine-tuned via pure SFT on 2,322 quality-filtered trajectories, achieving 41.5% on WebArena
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: the trained 9B student surpasses closed-source models (Claude 3.5 Sonnet 36.0%, GPT-4o 31.5%) on WebArena; capabilities transfer to unseen environments (18.2pp gain on WorkArena L1); local deployment without third-party API dependency
- [Method]: ⟨SFT⟩
- [Mechanism]: Agent-as-Annotators 以类比人工标注的方式组织轨迹生成：Task Designer 提出多样化的 web 任务，Annotator（teacher agent）执行任务生成包含推理轨迹与评估提示的轨迹，Supervisor（LLM judge）进行质量筛选（从 3,000 条轨迹中保留 2,322 条）。消融实验确认每个组件均有贡献：Judge 筛选、评估提示和推理轨迹各自贡献可测量的增益。核心贡献在于结构化的角色分工合成框架（P7 分支）。在筛选后轨迹上进行纯 SFT 产生 student agent（P5 分支），证明从单个 frontier teacher 进行结构化合成足以训练有竞争力的本地可部署 agent。
[Title]: Meta-Policy Reflexion: Reusable Reflective Memory and Rule Admissibility for Resource-Efficient LLM Agent
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: episodic task execution traces (N-Tok) from AlfWorld-based text environments, containing both successful action sequences and failure patterns that require correction
- [Target Experience]: structured Meta-Policy Memory (N-Tok) — a consolidated set of predicate-like rules distilled from LLM-generated reflections, stored as reusable corrective knowledge external to model weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: the MPM is applied at inference time through two complementary mechanisms: (1) soft memory-guided decoding biases generation toward memory-consistent actions, and (2) hard rule admissibility checks (HAC) enforce domain constraints to block unsafe/invalid actions; no weight updates required
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: MPR 通过将逐任务的临时反思整合为持久的、结构化的 Meta-Policy Memory 来扩展标准 Reflexion。整合过程将任务特定的反思轨迹抽象为谓词式规则（例如"若条件 X 成立，则动作 Y 无效"）。这些规则被形式化为 MPM 表示，配备定义的更新与解码算法。推理时，soft guidance 调节 token 概率分布，而 HAC 施加 hard constraints——违反储存规则的动作被确定性阻断。混合应用（soft + hard）兼顾灵活性与安全性。memory 是外部化的——无模型权重更新——实现资源高效的部署。
[Title]: WebXSkill: Skill Learning for Autonomous Web Agents
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: synthetic web agent trajectories (N-Tok) from readily available sources, containing action sequences for browser tasks such as navigation, form filling, and product search
- [Target Experience]: executable skills (S-Tok) — each skill pairs a parameterized action program (code) with step-level natural language guidance, organized into a URL-based graph for context-aware retrieval
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}
- [Utilization]: skills are deployed in two modes: (1) grounded mode — fully automated multi-step execution where the parameterized program runs directly; (2) guided mode — skills serve as step-by-step NL instructions that the agent follows with its native planning. Improves success rate by up to 9.8pp on WebArena and 12.9pp on WebVoyager
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: WebXSkill 解决纯文本 workflow skills（不可执行）与纯代码 skills（对 agent 不透明）之间的 grounding gap。三个阶段：(1) Skill Extraction——通过模式挖掘从合成轨迹中提取可复用的动作子序列，抽象为参数化 skill（动作程序 + NL 描述）；(2) Skill Organization——将 skills 索引为基于 URL 的图，节点为网页，边为在页面间转移的 skill，实现上下文感知的检索；(3) Skill Deployment——grounded mode 直接执行动作程序，guided mode 将 NL 指导暴露给 agent 的 planner。配对表示（code + NL）是核心创新：code 确保可执行性，NL 确保可解释性与适应性。
[Title]: XSkill: Continual Learning from Experience and Skills in Multimodal Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: multi-path rollout trajectories (N-Tok) from multimodal agents operating across diverse domains with multiple tools, containing both successful and failed action sequences grounded in visual observations
- [Target Experience]: dual-stream knowledge repository (N-Tok) — one stream for experiences (concise action-level guidance for tool selection and decision-making) and one stream for skills (structured task-level guidance for planning and tool orchestration)
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {self}
- [Utilization]: both knowledge streams are retrieved and adapted to the current visual context during inference; usage history feeds back into accumulation to form a continual learning loop; the two streams play complementary roles — experiences influence tool-use decisions, skills influence planning behavior; demonstrates zero-shot generalization to new domains
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: XSkill 将提取和检索均扎根于视觉观测。在积累阶段，来自 multi-path rollout 的轨迹经过视觉扎根的摘要（结合视觉状态压缩动作序列）和跨 rollout 评判（比较同一任务的多次尝试以识别鲁棒模式）处理。由此产生两个不同的知识流：experiences 捕获细粒度的动作级启发式（例如"当看到 UI 元素 X 时，优先采用 tool Y"），skills 捕获结构化的任务级规划（例如"为达成目标 G，先执行 A，再执行 B，再执行 C"）。推理时，两者基于视觉相似性被检索并适配。continual learning loop 意味着使用结果反馈至积累过程，逐步精化两个知识流。
[Title]: CLIN: A Continually Learning Language Agent for Rapid Task Adaptation and Generalization
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: trial execution outcomes (N-Tok) from ScienceWorld tasks, including successful and failed action sequences across varied environments and tasks (e.g., growing a plant, melting ice)
- [Target Experience]: persistent dynamic textual memory (N-Tok) centered on causal abstractions — rules of the form "action X in context Y leads to outcome Z" — rather than generic helpful hints
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: the causal memory is consulted during new trials to guide action selection; it transfers across environments (+4pp zero-shot) and tasks (+13pp zero-shot); continues updating in new settings for further improvement (+17pp/+7pp); no parameter updates required
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: CLIN 维护一个持久的文本记忆，每次 trial 后更新。关键设计选择在于表示形式：因果抽象而非通用提示。每次 trial 后，agent 分析发生的情况并提取因果关系（例如"将冰放入热容器会导致冰融化"）。这些因果规则被储存，按与当前任务上下文的相关性检索，用于指导动作选择。记忆是动态的——每次 trial 后更新，逐步积累知识。与 Reflexion（生成任务特定的反思）不同，CLIN 的因果抽象为跨任务迁移而设计：一个 ScienceWorld 任务中学到的物理动态因果知识可应用于其他任务。持续更新机制使 agent 在同一任务的反复 trial 中单调提升（+23pp over Reflexion），同时在全新任务上实现 zero-shot 提升。
[Title]: Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks
- [Pathway]: Narrative → Narrative (P1) + Narrative → Schematic (P2) [parallel dual-pathway]
- [Source Experience]: mobile device interaction trajectories (N-Tok) from a hierarchical multi-agent system — Manager plans, Perceptor/Observer/Operator execute, Action Reflector verifies, Notetaker aggregates
- [Target Experience]: dual-form long-term memory: Tips (N-Tok) — general guidance and lessons on effective environment interaction; Shortcuts (S-Tok) — reusable executable sequences of atomic operations tailored for specific subroutines
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Tips guide the Manager's planning and the Operator's action selection during new tasks; Shortcuts are directly executed for recurring subroutines, bypassing step-by-step reasoning; together they yield a 22% absolute improvement over previous SOTA across three foundation model backbones on Mobile-Eval-E
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Mobile-Agent-E 的 self-evolution 模块维护具有两种不同 carrier 类型的长期记忆。Tips（P1: N→N）由 Action Reflector 和 Notetaker 从执行结果中提取——当某个动作以显著方式失败或成功时，框架将教训抽象为 Tip（例如"点击小图标之前先放大"）。Shortcuts（P2: N→S）从重复的动作序列中挖掘——当相同的基本操作序列（tap, swipe, type）多次成功完成某个子程序时，被提升为 Shortcut 并存储为可执行宏。分层 agent 架构（Manager + 四个下属）提供结构化的角色分工，自然地产生两种形式的经验：Action Reflector 识别教训（→Tips），而 Operator 的重复执行模式成为 Shortcuts。两者在后续任务中基于任务相似性被检索。
[Title]: TOUCAN: Synthesizing 1.5M Tool-Agentic Data from Real-World MCP Environments
- [Pathway]: Policy → Narrative → Policy (§8.7, P7+P5)
- [Source Experience]: 1.5M tool-use trajectories synthesized from nearly 500 real-world Model Context Protocol (MCP) servers, with queries produced by 5 distinct models, trajectories generated by 3 teacher models using 2 agentic frameworks, and validated through rule-based and model-based checks
- [Target Experience]: student tool-agent policy weights (π-Par) fine-tuned on the Toucan dataset, outperforming larger closed-source counterparts on BFCL V3 and advancing the Pareto frontier on MCP-Universe Bench
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: the Toucan dataset is released as the largest publicly available permissively licensed tool-agentic dataset; models fine-tuned on it push the Pareto frontier on tool-use benchmarks, enabling open-source agents to compete with closed-source alternatives
- [Method]: ⟨SFT⟩
- [Mechanism]: Toucan 合成 pipeline：(1) Query Generation ——五个不同模型产生涵盖多样 MCP 环境的广谱 tool-use queries；(2) Model-Based Quality Filtering——按多样性、现实性和复杂度筛选 queries；(3) Trajectory Generation——三个 teacher model 使用两种 agentic framework 针对真实 MCP servers 执行 queries，产生 multi-turn、multi-tool 交互轨迹；(4) Validation——严格的基于规则检查（格式、工具调用合法性）和基于模型的检查（任务完成情况）；(5) Extension——三种机制使任务多样化并模拟 multi-turn 对话。 核心贡献在于利用真实 MCP 环境而非模拟环境的数据集构建方法学（P7 分支）。下游 SFT 在 Toucan 上训练出有竞争力的 tool-use agent（P5 分支）。使用真实 MCP servers 将 Toucan 与此前依赖合成或简化工具环境的数据集区分开来。

[Title]: SkillDroid: Compile Once, Reuse Forever
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: LLM-guided GUI interaction trajectories on mobile apps
- [Target Experience]: Parameterized skill templates (sequences of UI actions with weighted element locators and typed parameter slots)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 将 skill templates 重放于未来任务调用，无需 LLM 推理，减少推理成本并提升可靠性
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: LLM 引导的 GUI 轨迹被编译为结构化 skill templates（参数化 UI 动作序列，含加权元素定位器与类型化参数槽）。Matching cascade（regex patterns + embedding similarity + app filtering）将新指令路由至已存储 skills。Failure-learning layer 在 skill 可靠性下降时触发重编译。Skill replay 机制以零 LLM 调用实现 2.4x 加速，系统 success rate 随使用从 87% 收敛至 91%。

[Title]: G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Multi-agent collaboration trajectories (inter-agent communication, task execution records)
- [Target Experience]: Three-tier graph hierarchy: high-level generalizable insights + fine-grained condensed interaction trajectories
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 检索到的 insights 与轨迹在后续任务中指导 multi-agent 决策
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 将 MAS 交互轨迹组织为三层图结构（insight / query / interaction graphs）。双向记忆遍历同时检索高层可泛化洞察（cross-trial knowledge）与细粒度压缩交互轨迹（prior collaboration experience）。新任务执行后整个层级通过 assimilating new collaborative trajectories 演化，实现 agent team 的渐进式自我进化。全程无参数更新，不改动原始 MAS 框架。

[Title]: Steve-Evolving: Open-World Embodied Self-Evolution via Fine-Grained Diagnosis and Dual-Track Knowledge Distillation
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Embodied interaction trajectories in Minecraft (subgoal attempts with compositional diagnosis signals beyond binary outcomes)
- [Target Experience]: Reusable skills with explicit preconditions and verification criteria (formalized procedural knowledge) + executable guardrails that capture failure root causes and forbid risky operations at subgoal and task granularities (S-Tok)
- [Source Modality]: [embodied]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Skills and guardrails injected into LLM planner for knowledge-driven closed-loop control; guardrails forbid dangerous operations at both subgoal and task granularities
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 三阶段闭环：(1) Experience Anchoring——每次 subgoal 尝试被固化为结构化经验元组（pre-state, action, diagnosis-result, post-state），配备多维索引（条件签名、空间哈希、语义标签）与滚动摘要； (2) Experience Distillation——成功轨迹被泛化为具有显式 preconditions 和 verification criteria 的可复用 skills，同时失败被蒸馏为捕获根因的可执行 guardrails，在 subgoal 和 task 两个粒度上具备禁止操作语义（P2: N→S）； (3) Knowledge-Driven Closed-Loop Control——检索到的 skills 与 guardrails 注入 LLM planner，diagnosis 触发的局部重规划在线更新活跃约束。 Skills 和 guardrails 是 Schematic 的，因为它们携带形式化 preconditions、verification criteria 和可执行禁止语义——而不仅仅是关于什么成功或失败的叙事性描述。无参数更新。

[Title]: M2: Dual-Memory Augmentation for Long-Horizon Web Agents via Trajectory Summarization and Insight Retrieval
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Verbose multimodal web navigation interaction history (screenshots + actions)
- [Target Experience]: Concise state summaries (internal memory) + actionable guidelines (external memory from offline insight bank)
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 压缩 internal memory 减少上下文长度; 检索 external insights 以可操作指南引导 agent
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 双层 training-free memory：(1) Dynamic Trajectory Summarization（Internal Memory）将冗长的多模态交互历史压缩为简洁状态更新；(2) Insight Retrieval Augmentation（External Memory）从离线 insight bank 中检索可操作指南。两者协同实现上下文效率优化与决策鲁棒性增强，在 Qwen3-VL-32B 上 success rate 提升达 19.6% 并减少 58.7% token 消耗。

[Title]: APEX-EM: Non-Parametric Online Learning for Autonomous Agents via Structured Procedural-Episodic Experience Replay
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Full procedural-episodic execution traces (planning steps, artifacts, iteration history with error analysis, quality scores)
- [Target Experience]: Structured experience representations serving as positive (successful plans) and negative (failure with error annotations) in-context examples
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 通过 Plan-Retrieve-Generate-Iterate-Ingest (PRGII) workflow 将正/负经验作为 in-context examples 注入后续任务执行
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 将每次执行的完整 procedural-episodic trace（planning steps, artifacts, iteration history, error analysis, quality scores）编码为结构化经验表示。Hybrid retrieval 结合 semantic search、structural signature matching 与 plan DAG traversal，实现跨任务结构化迁移——即使任务间无词汇重叠，只要操作结构相似即可复用。成功经验作为正面 in-context example，失败经验作为含结构化错误标注的负面 example。Task Verifiers 提供多维奖励信号。在 KGQAGen-10k 上 +48.3pp，超过 oracle-retrieval upper bound。

[Title]: Reflexion: language agents with verbal reinforcement learning
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Raw task execution trajectories with task feedback signals (scalar values or free-form language)
- [Target Experience]: Reflective text (verbal reflections) stored in episodic memory buffer
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 反思文本在后续 trial 中作为额外上下文参与决策，通过 linguistic feedback 实现强化学习效果
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Agent 在 task feedback signals 上执行 verbal reflection，生成反思文本存入 episodic memory buffer。在后续 trial 中，episodic memory 中的反思文本作为额外上下文参与决策，通过 linguistic feedback 而非 weight update 实现强化学习。支持多种 feedback 类型（scalar values 或 free-form language）和来源（external 或 internally simulated）。在 HumanEval 上达到 91% pass@1，超越 GPT-4 的 80%。

[Title]: Evolving Programmatic Skill Networks
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Embodied interaction experience in open-ended environments (MineDojo, Crafter)
- [Target Experience]: Executable symbolic programs (skills) forming a compositional network that evolves through experience
- [Source Modality]: [embodied]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Skills 组合与复用于新任务; network 通过持续经验不断扩展
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: PSN 定义三个 LLM 驱动的核心机制：(1) REFLECT：对 skill compositions 进行结构化故障定位；(2) Progressive optimization with maturity-aware update gating：稳定可靠 skills 的同时保持对不确定 skills 的可塑性；(3) Canonical structural refactoring under rollback validation：维护网络紧凑性。Skills 是可执行符号程序（Schematic），形成可通过经验不断演化的组合网络。论文指出 PSN 的学习动态与神经网络训练存在结构平行性。无参数更新。

[Title]: From Evidence to Trajectory: Abductive Reasoning Path Synthesis for Training Retrieval-Augmented Generation Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Evidence-anchored synthetic reasoning paths (teacher-synthesized agent-environment interaction trajectories)
- [Target Experience]: Updated policy weights (π-Par) via SFT
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: 训练 8B model 成为 RAG agent，具备 task decomposition、retriever invocation 与 stepwise decision-making 能力
- [Method]: ⟨SFT⟩
- [Mechanism]: EviPath 三阶段合成 pipeline：(i) Abductive Subtask Planning：将问题分解为子问题，基于依赖关系迭代规划最优解路径；(ii) Faithful Sub-question Answering：以支持证据构建 proxy environment 生成每步推理与答案；(iii) Conversational Fine-Tuning：将完整 agent-environment 交互轨迹格式化为对话形式，通过 SFT 训练 student model。核心贡献在 data synthesis paradigm（从证据出发逆向合成推理路径而非从 LLM 直接生成），最终转化路径为 synthetic trajectory (Narrative) → policy weights (π-Par) 的 P5 单步。在 open-domain QA 上 8B model 达 14.7% absolute EM gain。

[Title]: Distilling LLM Agent into Small Models with Retrieval and Code Tools
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Teacher LLM agent-generated trajectories (reasoning + retrieval + code tool-use behavior)
- [Target Experience]: Updated small LM policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: 训练 0.5B-3B sLM 具备 tool-use agent 能力，在 factoid 与数学推理任务上替代大模型部署
- [Method]: ⟨SFT⟩
- [Mechanism]: Teacher LLM agent 通过 first-thought prefix prompting（在 trajectory 开头预设推理方向）增强生成轨迹质量，产生包含 reasoning 与 retrieval/code tool-use 的完整行为轨迹。Student sLM 通过 SFT 学习复现 teacher 的完整任务解决行为。Inference 时 self-consistent action generation 提升小模型鲁棒性。本质为 teacher trajectory (Narrative) → student policy weights (π-Par) 的标准 P5 蒸馏路径。

[Title]: NNetNav: Unsupervised Learning of Browser Agents Through Environment Interaction in the Wild
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Self-generated browser interaction demonstrations (unsupervised exploration + retroactive hierarchical labeling)
- [Target Experience]: Updated policy weights (π-Par) via SFT
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 训练 Llama-3.1-8B 成为 browser agent，在 WebArena 和 WebVoyager 上执行导航任务
- [Method]: ⟨SFT⟩
- [Mechanism]: 利用指令的层次结构使探索空间可处理：对任意网站，exploration policy 生成交互 episodes。通过 hierarchical instruction decomposition 将复杂指令分解为子任务，逆向标注有意义的 sub-task 轨迹；当中间轨迹无法标注为有意义子任务时自动剪枝，以此修剪指数级探索空间。10k 自生成 demonstrations 通过 SFT 训练 browser agent。WebArena 上 16% success rate（+15pts over zero-shot），WebVoyager 上 35%（+31pts）。{self} 已捕获数据由 agent 自身探索生成。

[Title]: TimeWarp: Evaluating Web Agents by Revisiting the Past
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Teacher-generated web interaction trajectories collected across multiple UI versions via plan distillation
- [Target Experience]: Updated policy weights (π-Par) via behavior cloning
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}
- [Utilization]: 训练 web agent 对不同 UI 版本具备跨时间鲁棒性
- [Method]: ⟨SFT⟩
- [Mechanism]: TimeTraj 使用 plan distillation 从 teacher model 收集跨多个 UI 版本的轨迹：teacher 产生 high-level plans，在不同版本的 web 环境中展开为具体交互轨迹。Student agent 通过 BC-variant 在这些多样化轨迹上训练，获得对 UI 变化的鲁棒性（Qwen-3 4B 从 20.4%→37.7%，Llama-3.1 8B 从 0%→27.0%）。论文同时贡献 TimeWarp benchmark（以容器化环境模拟 web 演化的六个 UI 版本）。核心贡献在"收集 plans 而非 trajectories"的范式转移。

[Title]: SKILLFOUNDRY: Building Self-Evolving Agent Skill Libraries from Heterogeneous Scientific Resources
- [Pathway]: Out of Scope
- [Mechanism]: 来源是异构的科学资源（repositories, APIs, scripts, notebooks, documentation, papers）——外部知识工件，而非具有 (c,a,o,f) 语义的 agent 决策经验。pipeline 将非结构化文档转化为可执行 skill packages，这属于知识工程任务而非 agent 经验转化。没有 agent-environment 交互轨迹作为源经验。

[Title]: Learn-by-interact: A Data-Centric Framework for Self-Adaptive Agents in Realistic Environments
- [Pathway]: Narrative → Policy (P5); also Narrative → Narrative (P1) for ICL usage
- [Source Experience]: Teacher-synthesized agent-environment interaction trajectories (via backward construction from documentation)
- [Target Experience]: Updated policy weights (π-Par) via SFT, or in-context examples for ICL
- [Source Modality]: [cross-modal]
- [Target Modality]: [cross-modal]
- [Experience Source]: {teacher}
- [Utilization]: Adapting LLM agents to given environments without human annotations; spans SWE-bench (coding), WebArena (web), OSWorld (desktop), Spider2-V (vision)
- [Method]: ⟨hybrid⟩
- [Mechanism]: Backward construction 合成范式：从 environment documentation 出发，先合成 agent-environment 交互轨迹，再从交互历史中总结/抽象出 instruction（与常规"从 instruction 到 trajectory"方向相反）。用于两种场景：(1) training-free ICL：通过 agent-optimized retrieval 将合成轨迹作为 in-context examples（P1）；(2) training-based SFT：合成数据用于微调（P5）。ICL 场景下 Claude-3.5 提升达 12.2%，训练场景下 Codestral-22B 提升达 19.5%。Backward construction 单独贡献 14.0% 训练提升。

[Title]: Meta Context Engineering via Agentic Skill Evolution
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Context artifacts execution feedback (base agent's training rollouts and evaluations) + history of engineering skills and their outcomes
- [Target Experience]: Refined context engineering skills (code, structured files) + optimized context artifacts
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 优化后的 context 与 skills 在 inference 时注入，跨五个领域持续提升 LLM 表现（相对提升 5.6-53.8%）
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 双层协同演化：(1) Meta-level agent 通过 agentic crossover（在 skills 历史、执行记录与评估上的 deliberative search）精化 context engineering skills（Schematic: code/flexible files）；(2) Base-level agent 执行这些 skills，从 training rollouts 中学习并优化 context artifacts（flexible files and code）。两级形成协同演化：meta-agent 从 base-agent 的执行反馈中学习改进 skills（Narrative → Schematic），改进后的 skills 产生更优 context，更优 context 又为 meta-agent 提供更丰富反馈。全程无模型参数更新。

[Title]: LLMs as Scalable, General-Purpose Simulators For Evolving Digital Agent Training
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Simulated UI interaction trajectories (teacher LLM as world simulator generating structured UI states and transitions)
- [Target Experience]: Updated policy weights (π-Par) via SFT
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}
- [Utilization]: 训练 digital agents 在 WebArena 和 AndroidWorld 上执行任务; UI-Simulator-Grow 以 Llama-3-8B 达到 Llama-3-70B 性能
- [Method]: ⟨SFT⟩
- [Mechanism]: UI-Simulator 以 LLM 作为 world simulator：digital world simulator 生成多样化 UI states，guided rollout process 产生连贯探索，trajectory wrapper 产出高质量多样化训练轨迹。UI-Simulator-Grow 通过优先处理高影响力任务并合成 informative trajectory variants 实现 targeted scaling——以更弱的 teacher model 和更少的合成数据匹配更强 baseline。Agent 在合成轨迹上通过 SFT 训练。转化路径为 synthetic trajectory (Narrative) → policy weights (π-Par) 的标准 P5，核心创新在 simulator 范式以替代真实 UI 交互。

[Title]: Unifying Dynamic Tool Creation and Cross-Task Experience Sharing through Cognitive Memory Architecture
- [Pathway]: Narrative → Schematic (P2); also Narrative → Narrative (P1) for experience sharing
- [Source Experience]: Raw task execution trajectories with success/failure patterns across diverse tasks
- [Target Experience]: Dynamically created tools (iterative code generation in sandbox) + structured episodic/semantic memories
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 创建的工具与共享经验用于解决新任务; curriculum learning 策略调度训练
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Hierarchical cognitive memory architecture（procedural, semantic, episodic components）支持两条并行的经验转化路径：(1) Dynamic tool creation（主路径 P2）：在 sandbox 环境中通过迭代代码生成将问题解决经验转化为可执行工具（Narrative → Schematic: code）；(2) Cross-task experience sharing（辅助路径 P1）：通过 episodic memory retrieval with semantic similarity matching 复用过往成功执行模式（Narrative → Narrative: insights）。Curriculum learning 通过 agent-ensemble difficulty re-estimation 调度训练。GAIA benchmark 上 Pass@1 达 81.8%。

[Title]: FABRIC: Framework for Agent-Based Realistic Intelligence Creation
- [Pathway]: Policy → Narrative (P7)
- [Source Experience]: LLM parametric knowledge (prompted and constrained to generate structured agentic records)
- [Target Experience]: Machine-parseable agentic interaction records (task specifications, tool definitions, policy pseudocode, NL exchanges, execution traces)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: 生成的 agentic data 作为下游 agent training（P5）的输入; 论文本身不执行训练
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 以 LLM-only pipeline 将 modular pipelines 分解为生成完整交互记录的子任务（task specifications, tool definitions, policy pseudocode, NL exchanges, execution traces）。通过 constrained generation formats + JSON-schema validation + judge-based filtering 确保记录符合严格语法/语义约束，实现 inputs/outputs/tool calls 间的 faithful alignment。支持 multi-task 与 multi-turn agent interactions。本质为 Parametric (LLM weights) → Tokenized (structured agentic records) 的 P7 外部化过程，但论文聚焦于 schema 设计、prompt 原则与 pipeline 架构这些工程方法论，不涉及对"隐式经验"的有意识提取。论文产物是用于下游 P5 转化的数据基础设施。

[Title]: Mock Worlds, Real Skills: Building Small Agentic Language Models with Synthetic Tasks, Simulated Environments, and Rubric-Based Rewards
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Teacher LLM-synthesized diverse tool-use tasks with mock tool ecosystems and rubric-based reward specifications
- [Target Experience]: Small language model policy weights trained via RL on synthetic interaction trajectories
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Trained small model executes agentic tool-use tasks, actively querying users for missing information, using internalized capabilities
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: Teacher LLM 合成多样化工具使用环境、新颖任务和 mock tool ecosystem；指令被有意低详设计以迫使 agent 向 user simulator 查询缺失细节；trainee agent 与模拟环境交互，task-level rubric 从子目标完成度、user-agent 交互质量和违规行为规避中计算结构化奖励信号；small LM 策略通过 RL 在这些合成轨迹上训练，将工具使用 agent 能力内化，无需依赖真实世界 API 不稳定性。

[Title]: CASCADE: Cumulative Agentic Skill Creation through Autonomous Development and Evolution
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Agent web exploration and tool interaction trajectories in scientific computing domains
- [Target Experience]: Executable skill code accumulated in a shared skill library
- [Source Modality]: [txt]
- [Target Modality]: [txt] (code)
- [Experience Source]: {self}
- [Utilization]: Executable skills are shared across agents and scientists for materials science and chemistry research tasks
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Agent 通过两项 meta-skill 自主探索 web 并与外部工具交互：(a) 通过 web search、代码提取和 memory 利用进行持续学习；(b) 通过 introspection 和 knowledge graph 探索进行自我反思；相关代码片段和程序性知识从交互轨迹中提取，编码为可执行 skill，并在不断增长的 skill library 中累积；memory consolidation 通过 human-agent 协作进一步精炼 library；skill 跨 agent 和 scientist 共享，实现累积能力增长而无需参数更新。

[Title]: CoEvoSkills: Self-Evolving Agent Skills via Co-Evolutionary Verification
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Agent task execution attempts and prior skill generation outcomes
- [Target Experience]: Multi-file executable skill packages (structured code artifacts)
- [Source Modality]: [txt]
- [Target Modality]: [txt] (code)
- [Experience Source]: {self}
- [Utilization]: Generated skill packages are deployed for multi-step professional tasks, generalizable across LLM backends
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Skill Generator 基于执行反馈迭代提议和精炼多文件 skill package；Surrogate Verifier 与 Generator 共同进化，在无 ground-truth 测试内容访问权限的情况下提供关于 skill 质量的有信息量且可操作的反馈；co-evolutionary loop 运行方式为：Generator 利用 Verifier 批评改进 skill，同时 Verifier 从 Generator 输出中改进其评估启发式；收敛后的 skill package 作为可复用、可共享的 artifact 部署；共同进化取代了手工 skill authoring 和 human-machine cognitive alignment 的需求。

[Title]: SynthAgent: Adapting Web Agents with Synthetic Supervision
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: LLM-synthesized web tasks and agent-collected trajectories, dual-refined for quality
- [Target Experience]: Fine-tuned open-source web agent policy weights
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}
- [Utilization]: Fine-tuned agent performs web navigation tasks on previously unseen target websites
- [Method]: ⟨SFT⟩
- [Mechanism]: LLM 通过对目标网站上 web element 的分类探索合成多样化 web 任务；agent 执行任务以收集交互轨迹；收集过程中，仅当 observation 冲突暴露幻觉时才精炼任务，以保持任务一致性；收集完成后，利用全局上下文的轨迹精炼去除噪声和错位 action；双重精炼的合成轨迹用于通过 SFT 微调开源 web agent，使其在不依赖人类示范的情况下适应新网站环境。

[Title]: Aligning Agentic World Models via Knowledgeable Experience Learning
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Embodied agent interaction trajectories with physical environment feedback (EB-ALFRED, EB-Habitat)
- [Target Experience]: Symbolic World Knowledge Repository containing physical feasibility constraints and task-optimal strategies
- [Source Modality]: [embodied]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Retrieved world knowledge constrains agent planning at inference to avoid physically infeasible (hallucinated) actions
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Agent 与 embodied 环境交互；Process Experience 通过分析 agent 规划违反物理定律的预测误差，提取物理可行性约束；Goal Experience 从成功轨迹中提取任务最优策略；两者被合成为显式规则存入符号化 World Knowledge Repository；推理时，检索相关约束和策略并注入 planning prompt，弥合语义知识与程序性根基之间的模态断裂，无需参数更新；展示跨模型和跨环境迁移能力。

[Title]: AutoGuide: Automated Generation and Selection of Context-Aware Guidelines for Large Language Model Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Agent offline execution trajectories in web navigation and sequential decision-making tasks
- [Target Experience]: Context-aware conditional guidelines in concise natural language (context-condition → recommended action)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Guidelines are retrieved by matching current context and injected into the agent prompt for informed decision-making
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Agent 从 web navigation 及其他 sequential task 的离线经验中积累执行轨迹；LLM 分析这些轨迹，提取简洁的上下文条件 guideline，以自然语言规则形式表达适用上下文与推荐 action；测试时，agent 当前决策上下文与 guideline 前提条件匹配，相关 guideline 作为聚焦知识注入 prompt，取代提供无差别示例的低效 demonstration-based in-context learning 范式。

[Title]: Natural-Language Agent Harnesses
- [Pathway]: Out of Scope
- [Mechanism]: 论文聚焦于将 agent harness（控制逻辑）外部化为可移植的自然语言 artifact，用于科学研究和可迁移性。Harness 是 agent orchestration 的控制机制，而非具有 (c,a,o,f) 语义的 agent-环境交互经验。不涉及来自 agent 交互轨迹的经验转化；核心贡献在于为可移植性而进行的表示格式转换（基于代码的 harness 逻辑 → NL harness 规范），而非提取和复用决策过程经验。

[Title]: Memory Transfer Learning: How Memories are Transferred Across Domains in Coding Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Coding agent execution traces across heterogeneous task domains, at four representation levels from concrete traces to abstract insights
- [Target Experience]: Cross-domain memory representations (primarily meta-knowledge such as validation routines and debugging strategies)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Retrieved cross-domain memories guide coding agents when solving tasks in new domains
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Coding agent 来自多个异构领域的执行轨迹以四个表示层级（具体轨迹 → 抽象洞察）存储；跨六个 coding benchmark 的实证研究表明，高层抽象洞察（meta-knowledge：validation routine、debugging strategy）跨领域正向迁移（平均 +3.7%），而低层任务特定轨迹因其过度特异性导致负迁移；抽象层级是迁移性的首要决定因素；迁移效果随 memory pool 规模扩大而增强；memory 可在不同模型间迁移；建立了超越单领域孤立使用的跨领域 memory 利用经验设计原则。

[Title]: Structured Agent Distillation for Large Language Model
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Teacher LLM agent ReAct-style decision trajectories segmented into [REASON] and [ACT] spans
- [Target Experience]: Smaller student language model policy weights with preserved reasoning-action alignment
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Compact student agent performs interactive decision-making tasks (ALFWorld, HotPotQA-ReAct, WebShop) without the large teacher
- [Method]: ⟨SFT⟩
- [Mechanism]: Teacher LLM agent 在交互任务上生成 ReAct 风格决策轨迹（交错推理与工具使用 action）；轨迹被分割为 [REASON] 和 [ACT] 段落；施加段落特定蒸馏损失：推理段落对齐 student 推理与 teacher 推理，action 段落对齐 student action 与 teacher action；这种结构感知监督不同于标准 token 级蒸馏，更好地保留了 teacher 的决策过程语义；student model 以最小性能下降实现显著压缩，优于 token 级和 imitation learning baseline。

[Title]: Investigate-Consolidate-Exploit: A General Strategy for Inter-Task Agent Self-Evolution
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Agent planning and execution trajectories across diverse tasks
- [Target Experience]: Simplified, reusable workflows and pipelines (structured procedural knowledge)
- [Source Modality]: [txt]
- [Target Modality]: [txt] (structured workflows)
- [Experience Source]: {self}
- [Utilization]: Consolidated workflows are exploited during subsequent task execution, reducing API calls and lowering model capability requirements
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Investigate 阶段：agent 在任务求解过程中动态记录规划与执行轨迹；Consolidate 阶段：多任务轨迹被分析并整合为简化、可复用的 workflow 和 pipeline，形成结构化程序性知识（S-Tok）；Exploit 阶段：面对新任务时，整合后的 workflow 被检索复用，大幅减少 API 调用（最高 80%），使较弱模型（GPT-3.5）能匹敌未经处理的更强模型（GPT-4）的性能；跨任务知识迁移代表了从任务内学习到真正跨任务自我进化的范式转变。

[Title]: Training-Free Group Relative Policy Optimization
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Group rollouts from LLM agent on specialized domain tasks with minimal ground-truth data
- [Target Experience]: Distilled experiential knowledge serving as a "token prior" (textual guidance)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Token prior is integrated into LLM API calls at inference to shift output distribution toward higher-quality behavior
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Agent 对每个训练样本生成多个 group rollout；在每组内，语义相对优势（而非数值奖励）识别更高质量输出；高质量经验知识在极少量 ground-truth 数据上通过多轮学习迭代蒸馏；蒸馏所得知识形成"token prior"——捕捉行为模式的文本引导；推理时，token prior 无缝集成到 LLM API 调用中，将输出分布转向更高质量的 agent 行为；完全不依赖参数更新即可达到类 RL 的分布效应（类似 GRPO），仅需几十个训练样本。

[Title]: TAME: A Trustworthy Test-Time Evolution of Agent Memory with Systematic Benchmarking
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Agent task execution trajectories and historical safety/utility feedback signals
- [Target Experience]: Dual memory: executor memory (generalizable methodologies) and evaluator memory (safety/utility assessment heuristics)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Executor memory guides task performance; evaluator memory acts as a safety guardrail filtering drafts before execution
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Agent 执行任务生成轨迹；executor memory 从成功执行模式中蒸馏可泛化的方法论；evaluator memory 独立地从历史反馈中精炼安全性和效用评估；闭合进化循环：memory filtering 检索相关知识 → draft generation 提出 action → trustworthy refinement 应用 evaluator memory 检查草稿安全性 → 执行产生新经验 → 双轨 memory 更新将新经验整合入 executor 和 evaluator memory 两者；双 memory 设计缓解"Agent Memory Misevolution"——良性任务进化过程中安全性可信度退化的问题；实现可信度与任务性能的联合提升。

[Title]: Meta-Harness: End-to-End Optimization of Model Harnesses
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Execution traces, scores, and source code of all prior harness candidates
- [Target Experience]: Optimized harness code determining information storage, retrieval, and presentation logic
- [Source Modality]: [txt]
- [Target Modality]: [txt] (code)
- [Experience Source]: {self}
- [Utilization]: Discovered harness code is deployed to improve LLM application performance with better context management and lower token usage
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Agentic proposer 迭代生成 harness code 候选；每个候选在目标任务上执行，产生分数和执行轨迹；proposer 通过文件系统接口访问所有先前候选的完整历史（源代码、分数、执行轨迹）；proposer 利用这一丰富的经验信号——比先前 text optimizer 使用的压缩文本反馈更丰富——来提议改进的 harness code；外层搜索发现的 harness 在 text classification、math reasoning 和 agentic coding 任务上超越手工设计的 baseline，且使用更少 context token；harness code 即优化 artifact，无模型权重更新。

[Title]: EE-MCP: Self-Evolving MCP-GUI Agents via Automated Environment Generation and Experience Learning
- [Pathway]: Narrative → Policy (P5) + Narrative → Narrative (P1), composite
- [Source Experience]: Agent trajectories collected in auto-generated MCP-GUI desktop application environments
- [Target Experience]: (P5) Distilled policy weights for MCP-dominant tasks; (P1) Experience bank of LLM-learned rules for GUI-intensive tasks
- [Source Modality]: [GUI]
- [Target Modality]: [GUI] + [txt]
- [Experience Source]: {self}
- [Utilization]: Distilled policy executes structured API (MCP) tasks; experience bank rules guide visual GUI interactions at inference
- [Method]: ⟨hybrid⟩
- [Mechanism]: Framework 自动生成同时具有 MCP（结构化 API）和 GUI 接口的桌面应用环境，并验证其正确性；agent 通过交互收集轨迹；gap-driven task synthesis 创建多样化训练场景；quality-filtered training 施加应用感知的机制选择：对 MCP 主导任务，轨迹用于通过 SFT 蒸馏策略权重（P5，+17.8pp）；对 GUI 密集型任务，轨迹对比产生 LLM 学习的操作规则，累积于 experience bank 中用于推理时引导而无需微调（P1，+10.0pp）；系统化跨应用分析揭示蒸馏与经验增强针对根本不同的失败模式，需要组合感知的机制选择而非一刀切方案。

[Title]: AlphaOPT: Formulating Optimization Programs with Self-Improving LLM Experience Library
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: LLM's prior optimization modeling attempts (failed and successful), grounded by solver execution feedback
- [Target Experience]: Structured experience library of reusable optimization modeling principles and constraint patterns
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Retrieved modeling principles guide LLM in translating new NL problem descriptions into correct mathematical formulations and solver code
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Library Learning 阶段：当 LLM 尝试未能产生正确的优化 formulation 时，solver 执行反馈识别错误，从失败尝试中提取结构化洞察（建模原则、约束模式、formulation 模板）；Library Evolution 阶段：基于任务间聚合证据精炼存储洞察的适用性——低效用洞察被剪枝，重叠洞察被合并——维持有界 library 增长；测试时，相关洞察在上下文内检索，引导 LLM 将自然语言问题描述转化为正确的数学 formulation 和可执行 solver code；性能随训练数据规模扩展（100→300 项，65%→72%）；无参数更新，改进完全源于以 solver 反馈为根基的结构化经验累积。

[Title]: Sub-goal Distillation: A Method to Improve Small Language Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Teacher LLM-annotated oracle trajectories with hierarchical sub-goal decomposition
- [Target Experience]: Fine-tuned small LM (770M parameters) policy weights for planning and execution modules
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Small LM agent plans via sub-goal generation and executes via elementary actions without any real-time LLM access
- [Method]: ⟨SFT⟩
- [Mechanism]: Teacher LLM 首先用层次化 sub-goal 序列标注 oracle 任务完成路径（Narrative 精炼：原始轨迹 → sub-goal 标注轨迹）；planning module 随后通过 SFT 微调以根据任务上下文生成 sub-goal；execution module 单独通过 SFT 微调以使用 elementary action 完成 sub-goal；推理时，small LM agent 在完全不访问 LLM 的情况下运行：planner 将任务分解为 sub-goal，executor 用 primitive action 执行每个 sub-goal；层次化 sub-goal 抽象弥合了大型 teacher 与 770M 参数 student 之间的能力差距，在 ScienceWorld 上比仅基于 elementary action 的标准 imitation learning 绝对提升 16.7%。

[Title]: RetroAgent: From Solving to Evolving via Retrospective Dual Intrinsic Feedback
- [Pathway]: Narrative → Policy (P5) + Narrative → Narrative (P1), composite
- [Source Experience]: Agent interaction trajectories with hindsight self-reflection on incremental subtask progress
- [Target Experience]: (P5) RL-updated policy weights guided by dual intrinsic feedback; (P1) Memory buffer of distilled reusable textual lessons
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Updated policy generates better actions; memory buffer lessons are retrieved via SimUtil-UCB to guide test-time decision-making
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: Agent 与环境交互生成轨迹；hindsight self-reflection 机制产生双重内在信号：(1) 内在数值反馈通过追踪相对于先前尝试的实时增量子任务进展来奖励有前景的探索，作为 online RL（GRPO 风格）策略更新中的辅助奖励（P5）；(2) 内在语言反馈从轨迹分析中蒸馏可复用的文本经验存入 memory buffer（P1）；测试时，Similarity&Utility-Aware UCB (SimUtil-UCB) 检索平衡相关性、历史效用和探索性，注入相关文本经验以辅助决策；双反馈设计使策略在受益于显式经验复用的同时内化探索激励，在 ALFWorld 上超标准 GRPO +18.3%，WebShop +15.4%，Sokoban +27.1%，MineSweeper +8.9%。

[Title]: WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: raw multimodal web navigation logs (trajectories with screenshots, actions, observations)
- [Target Experience]: condensed episodic summaries + task-specific coach advice (N-Tok)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: runtime hooks inject retrieved advice as in-context guidance; continuous curation of new trajectories enables self-evolution
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: WebCondenser 将原始多模态 navigation log 标准化为简洁文本摘要。External Memory Store 将完整轨迹组织为按相似度和新近度索引的 episodic experience。Coach 检索相关经验并通过 runtime hook 决定是否将任务特定 advice 注入 agent 上下文。Memory 持续整理新 navigation 轨迹以实现无需任何参数更新的自我进化。

[Title]: ArcMemo: Abstract Reasoning Composition with Lifelong LLM Memory
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: reasoning solution traces (chain-of-thought rollouts on ARC-AGI tasks)
- [Target Experience]: reusable, modular abstract concepts distilled into natural language (N-Tok)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: selectively retrieved and integrated into prompt for new queries; dynamically updated during test-time, enabling continual learning without weight updates
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 超越 instance-based memory（精确查询/响应对），迈向 concept-level memory：从解答轨迹中抽象出可复用的模块化概念并以自然语言存储。对新查询，选择性检索相关概念并集成入 prompt。Memory 在测试时动态更新，抽象概念被证明在所有推理计算规模下是最一致的设计。无参数更新——纯粹通过概念 memory 累积实现的测试时持续学习。

[Title]: Sample-Efficient Online Learning in LM Agents via Hindsight Trajectory Rewriting
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: failed interaction trajectories (suboptimal action sequences with environmental feedback)
- [Target Experience]: hindsight-optimized trajectories rewriting what could have been achieved + compressed memory representations (N-Tok)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: synthetic positive examples retrieved from memory for future similar situations; compressed representations enable efficient storage and comparison
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 将 RL 中的 hindsight experience replay 适配至 LM agent：(1) hindsight rule 利用 LM 自身识别在失败尝试中本可达到的相关替代 subgoal，并生成反事实优化轨迹；(2) update rule 在 memory 中维护压缩的轨迹表示。有效地从不成功交互中创造合成正例，显著提升样本效率。无参数更新——完全通过 prompt engineering 和 memory management 运作。

[Title]: From Procedural Skills to Strategy Genes: Towards Experience-Driven Test-Time Evolution
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: agent execution trajectories across scientific code-solving scenarios
- [Target Experience]: compact "Gene" representations — structured, control-oriented symbolic objects with editable structure (S-Tok)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: injected as test-time control primitives; attached failure history enables iterative accumulation; editable structure supports targeted refinement
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 将 agent 执行轨迹蒸馏为紧凑的"Gene"表示——结构化的、面向控制的符号对象，与面向文档的"Skill"包形成对比。论文证明表示格式是一阶因素：紧凑的 Gene 表示比冗长的 Skill 文档产生更强的控制力。Gene 通过可编辑结构、从失败历史中蒸馏紧凑警告以及结构扰动鲁棒性支持迭代经验累积。核心洞见是经验编码格式——而非体量——决定复用有效性。

[Title]: Memory Intelligence Agent
- [Pathway]: Narrative → Policy → Narrative, composite P5+P7 (§8.1)
- [Source Experience]: compressed historical search trajectories stored in non-parametric Manager memory (N-Tok)
- [Target Experience]: Planner (parametric memory agent) weights trained to produce search plans (π-Par); Executor uses plans to produce new trajectories (N-Tok)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Planner generates search plans consumed by Executor; Executor trajectories feed back to update both parametric and non-parametric memory in a bidirectional conversion loop
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 三组件架构：Memory Manager（非参数化，存储压缩的历史搜索轨迹），Planner（参数化记忆 agent，生成搜索计划），Executor（根据计划搜索和分析信息）。采用交替强化学习增强 Planner-Executor 协作。参数化（Planner）与非参数化（Manager）记忆之间的双向转换循环是核心创新：压缩轨迹→通过 RL 更新 Planner 权重（P5），Planner 权重→生成搜索计划（P7），计划→新轨迹→压缩回 Manager（P1），形成自进化闭环。Planner 在 test-time 通过即时更新持续进化。

[Title]: A-MEM: Agentic Memory for LLM Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: agent interaction experiences (raw trajectories, conversation logs, tool-use records)
- [Target Experience]: structured Zettelkasten notes with contextual descriptions, keywords, tags, and inter-note links (N-Tok)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: dynamic indexing and linking enables context-aware retrieval during inference; memory network continuously refines understanding as new memories are integrated
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 将 Zettelkasten 原则应用于 agent 记忆：当新记忆加入时，系统生成包含结构化属性（上下文描述、关键词、标签）的综合笔记。分析历史记忆以识别相关连接，在存在有意义相似性之处建立链接。新记忆触发对已有历史记忆的上下文表示和属性的更新，使记忆网络能够持续细化其理解。将结构化组织与 agent 驱动的决策相结合，实现自适应的、上下文感知的记忆管理，无需参数更新。

[Title]: Metacognitive Reuse: Turning Recurring LLM Reasoning Into Concise Behaviors
- [Pathway]: Narrative → Narrative (P1) [primary]; Narrative → Policy (P5) [setting 3 extension]
- [Source Experience]: recurring reasoning fragments from the model's own chain-of-thought traces
- [Target Experience]: concise "behaviors" (name + instruction pairs) stored in a behavior handbook (N-Tok); for setting 3, behavior-conditioned SFT data → policy weights (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: (1) behavior-conditioned inference: behaviors retrieved in-context reduce reasoning tokens by up to 46% while maintaining accuracy; (2) behavior-guided self-improvement: model improves future reasoning using own extracted behaviors, +10% accuracy over critique-and-revise; (3) behavior-conditioned SFT: more effective at converting non-reasoning models into reasoning models than vanilla SFT
- [Method]: ⟨LLM-extract⟩ [settings 1–2]; ⟨SFT⟩ [setting 3]
- [Mechanism]: LLM 对自身先前的推理轨迹进行元认知分析，识别重复出现的推导模式，并将其转化为简洁、可复用的"行为"（名称+指令对）。这些行为存储于行为手册中。三种使用模式：推理时通过上下文检索（减少 token 消耗同时保持准确性），通过行为引导的 critique-and-revise 实现无需参数更新的自我改进，以及对行为条件化的推理轨迹进行 SFT 以将程序性提示蒸馏到模型参数中。核心洞察在于将缓慢的推导转化为快速的程序性提示——模型学习的是如何推理，而不仅仅是得出什么结论。

[Title]: Trajectory-Informed Memory Generation for Self-Improving Agent Systems
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: agent execution trajectories with detailed reasoning patterns, decision attribution, and outcome signals
- [Target Experience]: structured guidance tips in three categories: strategy tips (from successes), recovery tips (from failure handling), optimization tips (from inefficient but successful executions) (N-Tok)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: retrieved and injected into agent prompts based on multi-dimensional similarity matching (task structure, error patterns, decision context)
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 四阶段流水线：(1) Trajectory Intelligence Extractor 对 agent 推理模式进行语义分析；(2) Decision Attribution Analyzer 识别哪些具体决策和推理步骤导致了失败、恢复或低效；(3) Contextual Learning Generator 生成三类指导——来自成功模式的策略提示、来自失败处理经验的恢复提示、来自低效但成功执行的优化提示；(4) Adaptive Memory Retrieval System 基于多维度相似性将相关经验注入 agent prompt。与通用记忆系统不同，该框架理解执行模式、提取带有溯源的结构化经验、并检索适配特定任务上下文的指导。无参数更新。

[Title]: ANCHOR: Branch-Point Data Generation for GUI Agents
- [Pathway]: Narrative → Policy (P5) [primary downstream]; Narrative → Narrative (P1) [data expansion component]
- [Source Experience]: seed GUI demonstration trajectories (human demonstrations + agent rollouts with screenshots, actions, state changes)
- [Target Experience]: expanded GUI trajectory dataset (N-Tok) → fine-tuned GUI agent policy weights (π-Par)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {human} [seed demonstrations]; {teacher} [synthetic expansion via executing agent + verifier]
- [Utilization]: SFT of GUI agent on expanded, quality-filtered trajectories for improved desktop task execution
- [Method]: ⟨SFT⟩
- [Mechanism]: 从少量经验证的种子演示出发，识别对应有意义 GUI 状态变化的分支点，并基于当前 GUI 上下文提出新的、状态锚定的任务变体。执行 agent 遵循提议的指令生成新轨迹，同时验证器通过状态感知检查和轨迹级一致性强制任务完成。任务条件化的步骤级过滤移除无根据的动作并对分支后片段去噪。扩展并清洗后的轨迹语料库用于通过 SFT 微调 GUI agent 策略权重（P5）。分支点扩展（P1: N→N）作为数据引擎驱动 P5 训练步骤。

[Title]: Co-Evolving LLM Decision and Skill Bank Agents for Long-Horizon Tasks
- [Pathway]: Narrative → Schematic → Policy, composite P2+P5 (§8.5)
- [Source Experience]: agent rollouts in game environments (unlabeled action-observation sequences)
- [Target Experience]: structured skills with contracts extracted by skill bank agent (S-Tok); improved decision agent policy for skill retrieval and action generation (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: decision agent retrieves skills from skill bank as in-context guidance for action taking; both agents co-evolve — skill bank refines skills from new rollouts, decision agent learns better retrieval and action generation
- [Method]: ⟨hybrid⟩
- [Mechanism]: 两个交互 agent 的协同进化框架：(1) skill bank agent 从 decision agent 的无标签 rollout 中发现可复用技能，以显式契约（前置条件、后置效果）提取为结构化的 schematic 表示（P2: N→Schematic）；(2) LLM decision agent 从该可学习技能库中检索技能以指导动作执行。通过迭代协同进化，技能库持续提取、细化和更新技能，而 decision agent 学会同时改进技能检索和动作生成——后者意味着策略层面的提升（P5）。该复合模式为 §8.5（Narrative → Schematic → Policy/Workflow），其中结构化技能提取在原始经验与策略改进之间充当中介。

[Title]: ExpeL: LLM Agents Are Experiential Learners
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: agent experiences autonomously gathered from a collection of training tasks (success/failure trajectories)
- [Target Experience]: extracted insights and knowledge expressed in natural language (N-Tok)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: recalled at inference time as in-context knowledge to inform decision-making on new tasks; cross-task transfer learning demonstrated
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Agent 在无人类监督的情况下从一组训练任务中自主收集经验。利用 LLM 通过自然语言提取从这些经验中提取可泛化的知识和洞察。推理时，agent 从其记忆中检索相关的提取洞察和过往经验以做出明智决策。性能随经验积累而持续提升。无参数更新——纯粹的提取和上下文内复用。随着提取的知识在任务分布间泛化，展现出涌现的迁移学习能力。

[Title]: The World Leaks the Future: Harness Evolution for Future Prediction Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: prediction trajectories with temporal contrasts on unresolved questions (earlier vs. later predictions exposing omissions in factor tracking, evidence gathering, uncertainty handling)
- [Target Experience]: reusable guidance written into a persistent future prediction harness (N-Tok); covers factor tracking, evidence gathering and interpretation, uncertainty handling
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: guidance from the harness injected into future predictions on the same question (before outcome known); after resolution, final outcome provides retrospective validation before harness is carried forward to subsequent questions
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 保持基座模型冻结，转而更新一个持久化的预测 harness。当同一未解决问题随时间被重新审视时，通过对比早期和后期预测来提取"内部反馈"，识别早期预测过程中的遗漏（因素追踪缺口、证据解读错误、不确定性校准偏差）。将可复用的指导写回 harness，使该问题的后续预测在结果揭晓前就已改进。问题解决后，最终结果提供回顾性检验，更新后的 harness 继续用于后续问题。这利用了时间信息泄露——世界渐进地揭示信息——在无需等待最终结果的情况下提取监督信号。

[Title]: Towards Autonomous Memory Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: agent interactions combined with actively acquired external knowledge (self-generated signals, teacher model outputs, tool-verified research, expert feedback)
- [Target Experience]: validated, curated knowledge entries in external memory with cost-aware provenance (N-Tok)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self} + {teacher} + {human}
- [Utilization]: retrieved during inference for decision-making; semantic-aware Thompson sampling balances exploration and exploitation over memories
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 主动而非被动的记忆获取：(1) 成本感知的知识提取级联从廉价的自生成/教师信号逐步升级到工具验证的研究，仅在必要时才使用昂贵的人类专家反馈；(2) 语义感知的 Thompson 采样平衡探索（获取新知识）与利用（使用已有记忆），缓解冷启动偏差。记忆被主动获取、经验证来源验证、并经过质量策展。无 LLM 训练——纯粹的记忆提取与管理。在某些基准上通过更优的知识质量而非策略更新超越了基于 RL 的优化方法。

[Title]: OS-Copilot: Towards Generalist Computer Agents with Self-Improvement
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: task execution trajectories across diverse OS applications (web, code terminals, files, multimedia, third-party apps)
- [Target Experience]: accumulated reusable skills for various applications and interaction patterns (N-Tok)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: retrieved from persistent memory as in-context guidance for new tasks; skills transfer across unseen applications
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: FRIDAY agent 基于 OS-Copilot 框架构建，与全面的操作系统元素（网页、代码终端、文件、多媒体、第三方应用）交互。每次任务后，agent 从执行轨迹中提取可复用的技能和交互知识，并将其累积到持久记忆中。对于新任务——包括在之前未见过的应用上——相关技能被检索并作为上下文内指导注入。自我改进通过不断增长的技能积累而非参数更新实现：agent 的能力随技能库扩展而增强。通过跨应用技能迁移在 GAIA 上比先前方法提升 35%。

[Title]: ICAL: Continual Learning of Multimodal Agents by Transforming Trajectories into Actionable Insights
- [Pathway]: Narrative → Narrative (P1) [primary]; Narrative → Policy (P5) [fine-tuning extension]
- [Source Experience]: sub-optimal multimodal demonstrations (noisy trajectories in TEACh, VisualWebArena, Ego4D) with human feedback
- [Target Experience]: cognitive abstractions annotated as general programs — task relationships, object state changes, temporal subgoals, task construals (N-Tok); optionally, fine-tuned policy weights (π-Par)
- [Source Modality]: [cross-modal]
- [Target Modality]: [cross-modal]
- [Experience Source]: {human} [feedback]; {self} [trajectories]
- [Utilization]: retrieved as in-context exemplars for retrieval-augmented LLM/VLM agents; optionally used as SFT data for additional policy improvement
- [Method]: ⟨LLM-extract⟩ [primary]; ⟨SFT⟩ [extension]
- [Mechanism]: 给定含噪的多模态演示，VLM 将轨迹抽象为通用程序：修正低效动作并标注四类认知抽象——任务关系、物体状态变化、时序子目标、任务诠释。这些抽象通过人类反馈在 agent 尝试在相似环境中执行的过程中交互式细化和适应。生成的抽象作为高质量范例用于 prompt 中的上下文学习，显著优于缺乏此类认知标注的演示。在这些检索增强轨迹上进行微调可获得进一步改进（P5 扩展）。关键创新在于从次优数据中提取结构化认知洞察——而不仅仅是清洗后的动作序列。

[Title]: Agent Planning with World Knowledge Model
- [Pathway]: Narrative → Policy (P5) [primary training]; Policy → Narrative (P7) [knowledge generation at inference]
- [Source Experience]: expert demonstrations + agent-sampled trajectories from interactive planning tasks (c, a, o, f across ScienceWorld, ALFWorld, WebShop)
- [Target Experience]: parametric World Knowledge Model (WKM) weights encoding prior task knowledge and dynamic state knowledge (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human} [expert trajectories]; {self} [sampled trajectories]
- [Utilization]: WKM generates prior task knowledge to guide global planning and dynamic state knowledge to assist local planning; the generated knowledge is fed as context to the agent planner
- [Method]: ⟨SFT⟩
- [Mechanism]: Agent 模型从专家演示和自采样轨迹中通过 LLM 提取自合成知识（任务特定的先验、状态转移模式）（N→N）。这些合成知识随后通过 SFT 用于训练一个独立的参数化 World Knowledge Model（WKM），将规划相关知识内化到模型权重中（P5: N→Policy）。推理时，WKM 从其参数化编码中生成先验任务知识（用于全局规划）和动态状态知识（用于局部规划），将其作为 token 化上下文馈送给 agent planner（P7: Policy→Narrative）。WKM 有效地充当一个参数化知识仓库，按需外化学习到的规划启发式。弱 WKM 可以指导强 agent 模型的规划，且 WKM 训练可泛化到未见任务。

[Title]: Training LLM Agents for Spontaneous, Reward-Free Self-Evolution via World Knowledge Exploration
- [Pathway]: Narrative → Policy (P5) [training phase]; Policy → Narrative (P7) [inference phase, native self-evolution]
- [Source Experience]: agent exploration trajectories in web environments + self-generated world knowledge (N-Tok)
- [Target Experience]: agent policy weights internalizing the meta-capability to explore and summarize world knowledge (π-Par)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: at inference, the trained policy spontaneously explores unknown environments and generates useful world knowledge without any external rewards or human instructions; the generated knowledge directly improves task success rates
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 面向自进化的 Meta-RL 范式：训练期间，agent 探索环境并生成世界知识摘要。基于结果的奖励衡量这些自生成知识对 agent 下游任务成功率的提升程度。策略通过 RL 更新，将探索和知识生成能力内化（P5）。推理时，agent 无需外部奖励——它自发地通过探索未知环境并从训练得到的参数化能力中生成有用的世界知识，实现"原生自进化"（P7）。以此方式训练的紧凑 14B 模型性能超过无辅助的 Gemini-2.5-Flash。与标准 P5 的关键区别在于，训练目标不是任务性能本身，而是通过知识生成实现自进化的元能力。

[Title]: View-oriented Conversation Compiler for Agent Trace Analysis
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: raw agent JSONL conversation logs containing nested tool calls, CoT reasoning blocks, sub-agent invocations, context-window compaction boundaries, and harness-injected system directives
- [Target Experience]: a family of compiled structured views — full view (lossless canonical transcript with line-number coordinate system), UI view (reconstructing the interaction as the user perceived it), adaptive view (structure-preserving projection governed by a relevance predicate)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: views replace raw JSONL as reflector input for context engineering; improves downstream pass rates while cutting reflector token consumption by 50-67%
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 一个确定性编译器流水线（词法分析、语法分析、中间表示、降层、输出）将原始 agent JSONL 日志转换为一族形式化结构化的视图。全量视图保留完整转录并作为规范的行号坐标系统。UI 视图从用户视角重建交互过程。自适应视图应用由相关性谓词控制的结构保持投影。该转化为 P2，因为编译器引入了形式化解析和中间表示阶段，生成具有显式坐标系统和谓词的结构化视图——这是超出单纯抽象或摘要的形式化步骤。编译器本身是确定性算法而非基于 LLM，但转化过程无需训练。

[Title]: PlugMem: A Task-Agnostic Plugin Memory Module for LLM Agents
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: episodic memories from agent interactions across heterogeneous tasks
- [Target Experience]: compact, extensible knowledge-centric memory graph explicitly representing propositional knowledge (facts about the world) and prescriptive knowledge (action guidelines)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: plug-and-play memory module attachable to arbitrary LLM agents without task-specific redesign; efficient retrieval and reasoning over task-relevant abstract knowledge rather than verbose raw trajectories
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 将情景记忆结构化为以知识为中心的记忆图谱，其中记忆访问和组织的单位是抽象知识而非实体或文本块（区别于 GraphRAG）。借鉴认知科学，图谱显式表示两种知识类型：命题性知识（关于环境的事实断言）和规定性知识（面向行动的规则和指南）。这种图谱表示使得紧凑存储和高效知识检索成为可能。从叙事性情景记忆到形式类型化知识图谱的转化构成 P2，因为输出是具有显式知识类型语义的结构化图谱，而非自由文本摘要。

[Title]: SkillCraft: Can LLM Agents Learn to Use Tools Skillfully?
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: tool-use interaction experience from long-horizon, compositionally diverse tasks
- [Target Experience]: executable Skill compositions — persistent, cached, higher-level compositions of atomic tools with explicit invocation interfaces
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: cached Skills reused inside and across tasks, reducing token usage by up to 80%; persistent library accumulates composable capabilities over time
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Agent 通过轻量级评估协议将原子工具自动组合为更高层的可执行 Skill。这些 Skill 被缓存在持久化库中并在跨任务间复用。Skill 是可执行的工具组合（Schematic：具有定义好的调用接口的结构化工作流），而非描述性的自然语言指南（Narrative）。该转化为 P2，因为 agent 将一次性的工具使用轨迹形式化为可复用、可执行的组合单元——Skill 具有定义良好的结构（原子工具调用的组合），可以确定性调用，区别于叙事性的技能描述。

[Title]: WorkflowGen: an adaptive workflow generation mechanism driven by trajectory experience
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: full execution trajectories from LLM agent workflows, including both successful and failed episodes
- [Target Experience]: reusable workflow templates with structured knowledge artifacts — error fingerprints, optimal tool mappings, parameter schemas, execution paths, exception-avoidance strategies — organized at node and workflow levels
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: three-tier adaptive routing dynamically selects among direct template reuse, rewriting-based generation, and full initialization based on query similarity; reduces token consumption by over 40% and improves success rate by 20% on medium-similarity queries
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 捕获完整执行轨迹并在节点层面（单个工具调用）和工作流层面（完整执行序列）提取可复用知识。提取的产物包括：错误指纹（预测失败的模式）、最优工具映射（哪个工具用于哪个子任务）、参数 schema（预期输入/输出形态）、执行路径（成功序列）、异常避免策略。闭环机制执行轨迹重写、经验更新和模板归纳以维护模板。该转化为 P2，因为提取的产物是具有类型化槽位的结构化模板（参数 schema、作为形式化序列的执行路径、作为结构化关联的工具映射）——这些是 Schematic 而非自由文本 Narrative。

[Title]: GUI-ReWalk: Massive Data Generation for GUI Agent via Stochastic Exploration and Intent-Aware Reasoning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: synthetic GUI interaction trajectories generated through stochastic exploration (emulating human trial-and-error) and reasoning-guided phases (inferred goals driving coherent interactions), with multi-stride task generation for long-horizon cross-application workflows
- [Target Experience]: VLM policy weights (Qwen2.5-VL-7B fine-tuned on the GUI-ReWalk dataset)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}
- [Utilization]: SFT on the synthesized dataset to train a GUI agent policy that achieves superior coverage, higher trajectory entropy, and more realistic user intent modeling across Screenspot-Pro, OSWorld-G, UI-Vision, AndroidControl, and GUI-Odyssey
- [Method]: ⟨SFT⟩
- [Mechanism]: GUI-ReWalk 通过两阶段过程合成 GUI 轨迹：随机探索通过模拟人类的试错行为确保多样性，随后推理引导阶段利用推断的目标驱动连贯且有目的的交互。多步长任务生成构建长时程跨应用工作流。合成的轨迹编码决策过程语义（c=GUI 截图状态，a=点击/输入坐标，o=屏幕转移）。这些通过 SFT 在 Qwen2.5-VL-7B 上内化为策略权重。此为 P5，因为主要转化是 Tokenized（GUI 轨迹）→ Parametric Policy（VLM 权重），数据由教师合成流水线生成，而非 agent 自身的交互。

[Title]: AutoHarness: improving LLM agents by automatically synthesizing a code harness
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: environment feedback from game interactions — illegal move rejections, game outcomes, and execution traces — accumulated over a small number of iterative refinement rounds
- [Target Experience]: a code harness that prevents illegal moves by wrapping agent outputs with validation logic; in the extreme case, the entire decision policy compiled into executable code that eliminates LLM calls at decision time
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: harness wraps agent actions at inference time to block illegal moves; code policy replaces the LLM entirely, enabling the smaller Gemini-2.5-Flash to outperform larger models like Gemini-2.5-Pro and GPT-5.2-High
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 通过多轮环境锚定的反馈迭代细化代码 harness：LLM 提出 harness、在游戏环境中测试、接收执行反馈（非法动作错误、成功/失败信号）、并优化代码。harness 将环境约束编码为可执行的验证逻辑（Schematic）。在极端情况下，所有决策逻辑被编译为 code policy——一个完全可执行的程序，在决策时替代 LLM。此为 P2，因为叙事形式的环境反馈（错误轨迹）通过迭代细化驱动结构化代码制品（Schematic）的生成，底层模型无参数更新。

[Title]: REVERE: Reflective Evolving Research Engineer for Scientific Workflows
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: cross-repository execution trajectories from research coding tasks, spanning heterogeneous repositories, underspecified environments, and weak feedback signals
- [Target Experience]: reusable heuristics, refined system prompts, task-prompt templates, and a cumulative cheatsheet — all textual artifacts that encode distilled failure patterns and solution strategies
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: targeted edits injected into three configurable fields (system prompt, task-prompt template, cumulative cheatsheet) to improve agent performance on SUPER (+4.50%), ResearchCodeBench (+3.51%), and ScienceAgentBench (+4.89%)
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 分析跨多个研究仓库的执行轨迹，通过跨任务的 Global Training Context 识别重复出现的失败模式，而非依赖局部每任务信号。将识别出的失败模式蒸馏为可复用的启发式，并对三个可配置字段进行精准编辑：系统 prompt、任务 prompt 模板、累积备忘单。与先前的 prompt 优化方法不同（全量 prompt 重写导致知识丢失，或非结构化合并），REVERE 采用精准编辑，在保留累积知识的同时解决特定失败模式。输出为 P1：所有目标产物（启发式、备忘单、prompt 细化）保持在 Narrative 形式，无参数更新，无形式化结构引入。

[Title]: Towards Reliable Generation of Executable Workflows by Foundation Models
- [Pathway]: Out of Scope
- [Mechanism]: 该论文引入静态分析器（Timon）和基于 FM 的修复工具（Pumbaa）来检测和修复基础模型生成的 DSL 工作流中的缺陷。缺陷分类法（20 种类型）由作者人工策展，并非从 agent 决策经验中提取。工作流生成与修复循环缺乏 agent 决策上下文（c,a,o,f）语义——它操作于形式化的 DSL 规范，没有 agent 与环境交互。不存在跨 carrier 的经验转化；该论文解决的是 FM 生成代码的软件工程可靠性问题，而非 agent 经验复用。

[Title]: UMEM: Unified Memory Extraction and Management Framework for Generalizable Memory
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: agent interaction experience across diverse tasks and semantically related query clusters
- [Target Experience]: extracted generalizable memories — textual insights distilled from experience, optimized for utility across semantically related tasks rather than individual instances
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: extracted memories guide agent behavior on future tasks; monotonic improvement during continuous self-evolution across five benchmarks with up to 10.67% gains in multi-turn interactive tasks
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 通过 GRPO 训练 LLM 联合优化记忆提取（从经验中蒸馏洞察）和记忆管理（更新记忆库）。关键创新是 Semantic Neighborhood Modeling：不按单个实例评估记忆效用（会引入实例特异性噪声），而是通过邻域级边际效用奖励在语义相关查询簇上衡量效用。该奖励驱动 GRPO 对提取模型权重的优化，使提取器学会生成可在相似任务间泛化的记忆。提取模型的权重通过 GRPO 进行参数化更新，但提取出的输出保持在 Narrative 形式（文本洞察）。主路径为 P1（agent 经验→文本记忆），GRPO 作为提取策略的优化方法而非目标 carrier。

[Title]: ELITE: Experiential Learning and Intent-Aware Transfer for Self-improving Embodied Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: embodied agent execution trajectories in EB-ALFRED and EB-Habitat, including both successful and failed interactions with physical environments
- [Target Experience]: an evolving strategy pool — reusable textual strategies extracted via self-reflection and maintained through structured refinement operations (add, merge, prune)
- [Source Modality]: [embodied]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: intent-aware retrieval identifies procedurally similar tasks and injects relevant strategies as guidance during execution; achieves 9% and 5% improvement over base VLMs in online setting without supervision; generalizes to unseen task categories
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 自反身知识构建分析具身执行轨迹以提取可复用策略——识别什么有效、什么失败及其原因——并将其以文本描述形式存储在不断演化的策略池中。结构化细化操作（新增策略、合并冗余策略、剪枝过时策略）随时间维护策略池质量。意图感知检索基于过程相似性将当前任务上下文与已存储策略匹配，并注入最相关的策略作为指导。该转化为 P1，因为具身交互轨迹被抽象为文本策略（Narrative 形式），涉及从 [embodied] 源模态到 [txt] 目标模态的跨越。无参数更新参与。

[Title]: Compiling Deterministic Structure into SLM Harnesses
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: teacher model's natural-language critiques based on execution outcomes of SLM-generated workflow artifacts, serving as directional gradients in discrete semantic space
- [Target Experience]: discrete execution plans — DAG topologies specifying workflow structure, deterministic code harnesses with per-node optimization of code-vs-LLM placement, and system prompts
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: compiled workflows execute with deterministic structure — capability offloading delegates unreliable subtasks to Python, structural consensus wraps variance-sensitive steps in fan-out/fan-in subgraphs with deterministic voting; achieves +26.3% to +34.3% absolute gains over prompt optimizers on GSM-Hard
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: SGDe（Semantic Gradient Descent）在离散语义空间中运行：前沿教师基于执行结果生成对 SLM 工作流制品的自然语言 critique。这些 critique 作为方向性梯度，迭代引导 SLM 将其工作流细化为 DAG 拓扑、系统 prompt 和确定性代码。教师编译两种特定的确定性结构：capability offloading（识别哪些子任务应委托给 Python 执行，哪些保留为 LLM 调用，依据执行轨迹逐节点优化）和 structural consensus（将方差敏感步骤包装在具有确定性投票的 fan-out/fan-in 子图中）。该转化为 P2，因为教师的叙事 critique 通过迭代编译过程驱动形式化 Schematic 制品（DAG 拓扑、可执行代码）的生成。基于 PAC 学习形式化，样本复杂度上界使得仅需三个训练示例即可收敛。

[Title]: From Experience to Strategy: Empowering LLM Agents with Trainable Graph Memory
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: raw agent trajectories from complex, open-ended task environments
- [Target Experience]: multi-layered trainable graph memory — decision paths structured as a state machine (Schematic) and high-level strategic meta-cognition (Narrative) distilled from the graph; graph edges carry RL-optimized utility weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: RL-optimized meta-cognition dynamically integrated into LLM agent reasoning via meta-cognitive prompting; graph provides robust generalization and consistent benefits during RL training
- [Method]: ⟨hybrid⟩
- [Mechanism]: 将原始 agent 轨迹抽象为组织成状态机的结构化决策图，捕捉显式状态转移的决策路径。从该图中蒸馏出高层战略元认知（人类可理解的战略原则）。基于 RL 的权重优化过程根据下游任务的奖励反馈估计每个元认知节点的经验效用，使图记忆具有自适应能力。优化后的策略通过元认知提示引导 agent。主转化为 P2：轨迹 → 结构化决策图（Schematic 状态机）。方法为 hybrid，因为结合了基于 LLM 的图构建与基于 RL 的图效用参数权重优化。

[Title]: EchoTrail-GUI: Building Actionable Memory for GUI Agents via Critic-Guided Self-Exploration
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: autonomous GUI exploration trajectories generated by the agent interacting with GUI environments across diverse tasks
- [Target Experience]: curated database of successful task trajectories, validated and filtered by a reward model to retain only high-quality episodes
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: most relevant past trajectories retrieved and injected as in-context demonstrations to guide agent reasoning and actions on new GUI tasks; improves task success rate and operational efficiency on Android World and AndroidLab
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 三阶段框架：（1）Experience Exploration——agent 自主与 GUI 环境交互构建轨迹数据库，reward model 验证每条轨迹并仅保留成功 episode；（2）Memory Injection——接收新任务时，系统通过相似度搜索检索最相关的历史轨迹；（3）GUI Task Inference——将检索到的轨迹作为 in-context demonstration 注入。转化为 P1：原始探索轨迹通过 critic 引导的过滤被策展为经过验证的轨迹数据库。critic（reward model）引入质量门槛，但输出保持 Narrative 形态（GUI 交互序列作为 demonstration），无参数更新，未引入形式化结构。

[Title]: AgentSynth: Scalable Task Generation for Generalist Computer-Use Agents
- [Pathway]: Out of Scope
- [Mechanism]: AgentSynth 是一个 benchmark 和任务生成 pipeline，利用信息不对称从简单子任务构建复合任务。论文的主要贡献是生成包含 6000+ 个任务、难度可控的多样化 benchmark 用于评估 computer-use agent。生成的任务和轨迹并非从已有 agent 经验中导出或转化——它们是用于评估目的的全新（de novo）合成构造。不存在以 (c,a,o,f) 语义在不同 carrier 之间转换的经验转化机制。论文属于 benchmark 构建领域而非经验转化。

[Title]: AutoSkill: Experience-Driven Lifelong Learning via Skill Self-Evolution
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: user dialogue and interaction traces across multiple sessions, capturing stable user preferences, requirements, and interaction patterns
- [Target Experience]: standardized skill representations — natural language documents encoding user-specific preferences (e.g., reducing hallucinations, following writing conventions, avoiding technical jargon) with a defined lifecycle of creation, refinement, merging, and deprecation
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: model-agnostic plugin layer dynamically injects relevant skills into future requests; skills are composable and transferable across agents, users, and tasks
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 从用户对话和交互轨迹中抽象技能，识别跨 session 持续存在的稳定用户偏好和需求。技能表示为标准化自然语言文档，并通过持续自演化生命周期进行管理：从交互模式创建新技能，基于新证据精炼已有技能，合并冗余技能，废弃过时技能。相关技能被动态检索并注入未来请求的 prompt。转化为 P1，因为短暂的交互轨迹被蒸馏为可复用的文本技能表示（Narrative 形态），底层模型无参数更新。

[Title]: Unlocking Implicit Experience: Synthesizing Tool-Use Trajectories from Text
- [Pathway]: Out of Scope
- [Mechanism]: GEM pipeline 从通用文本语料（而非 agent 决策经验）中提取多轮 tool-use 轨迹。尽管论文主张文本语料包含"隐式经验"，但源材料缺乏本 Survey 纳入标准所要求的 agent 特定决策上下文、异构动作空间以及 (c,a,o,f) 语义。转化是从非结构化自然语言文本到结构化 tool-use 轨迹——一种有趣的数据合成方法，但源端并非 agent 经验。后续 SFT 步骤训练 Trajectory Synthesizer 是从 pipeline 进行的模型蒸馏，而非经验到策略的转化。

[Title]: Fara-7B: An Efficient Agentic Model for Computer Use
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: synthetic multi-step web interaction trajectories generated by FaraGen — diverse tasks proposed from frequently used websites, multiple solution attempts per task, successful trajectories filtered by multiple verifiers
- [Target Experience]: VLM policy weights (Fara-7B, a 7B native computer-use agent that perceives via screenshots and acts via predicted coordinates)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}
- [Utilization]: Fara-7B operates as a compact, on-device CUA model; outperforms comparable-size CUA models on WebVoyager, Online-Mind2Web, and WebTailBench, and is competitive with much larger frontier models
- [Method]: ⟨SFT⟩
- [Mechanism]: FaraGen 通过一个 pipeline 合成多样化 web 任务轨迹：提出任务、生成多个求解尝试、使用多个 verifier 过滤成功轨迹，每条经过验证的轨迹成本约 $1。经验证的轨迹编码了决策过程语义（c=网页截图, a=预测的点击/输入/滚动坐标, o=页面转移）。这些轨迹通过 SFT 被内化到 7B VLM 的策略权重中，产生 Fara-7B。此为 P5，因为主转化是 Tokenized（GUI 轨迹）→ Parametric Policy（VLM 权重 via SFT）。经验由 teacher（FaraGen 合成 pipeline）生成，而非来自 agent 自身交互。
[Title]: ToolMind Technical Report: A Large-Scale, Reasoning-Enhanced Tool-Use Dataset
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: synthetic multi-turn tool-use dialogues generated by a multi-agent framework across 20k+ tools, with realistic user-assistant-tool interactions governed by a function graph derived from parameter correlations
- [Target Experience]: policy weights of fine-tuned LLMs encoding tool-use competence and self-corrective reasoning capability
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: fine-tuned models directly execute tool-use tasks at inference time without external augmentation; the internalized self-corrective reasoning signals enable robust tool-use learning
- [Method]: ⟨SFT⟩
- [Mechanism]: multi-agent 框架首先基于工具间参数相关性构建函数图，然后模拟真实的 user-assistant-tool 交互生成 160k 合成轨迹。关键创新在于，pipeline 在轨迹级验证之外还施加了细粒度的 turn-level filtering——每个 turn 被单独评估，在进入训练语料之前剔除错误或次优步骤。这防止了训练过程中的误差放大，同时保留了自我修正推理信号（先出错后自纠的 turn）。过滤后的轨迹用于标准 SFT，将 tool-use 能力内化至模型策略权重。turn-level filtering 是核心质量控制创新，但轴心 pathway 为 P5：清洗后的 tokenized 轨迹 → parametric policy。

[Title]: TED: Training-Free Experience Distillation for Multimodal Reasoning
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: student model's multiple reasoning trajectories on multimodal reasoning tasks, alongside teacher model's independent solution and ground-truth answers
- [Target Experience]: a compact set of generalized experiences (extracted reasoning patterns and corrective heuristics) injected into the student's prompt as in-context guidance
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {teacher}
- [Utilization]: experiences injected into student prompt at inference time to improve reasoning without any parameter updates; experience bank continuously refined and compressed over time
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 对每个输入，student 生成多条推理轨迹，teacher 独立产生自身解答。teacher 对照自身推理和 ground-truth 答案比较 student 的轨迹，提取捕获有效推理模式的泛化经验。这些经验跨样本持续精炼和更新。为防止无界膨胀和噪声累积，经验压缩机制追踪使用统计并有选择地合并、重写或移除低效用经验。区分性特征在于更新目标是 student 的 in-context experience bank 而非模型参数——在不进行训练的情况下实现有意义的知识迁移。此为 P1（N→N），因为 teacher 将原始 student 轨迹转化为精炼的、可泛化的推理启发式，目标载体保持 narrative tokenized（in-context prompt injection）。

[Title]: ASDA: Automated Skill Distillation and Adaptation for Financial Reasoning
- [Pathway]: Narrative → Narrative (P1) with parallel Narrative → Schematic (P2) for code templates
- [Source Experience]: student model's failure cases on financial reasoning tasks, classified by subfield and error type
- [Target Experience]: structured skill files containing reasoning procedures (N-Tok), code templates (S-Tok), and worked examples (N-Tok), adhering to the Agent Skills open standard
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: skill files dynamically injected during inference for domain adaptation without weight access or retraining; artifacts are human-readable, version-controlled, and auditable
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: teacher 模型通过迭代式纠错学习分析 student 模型在金融推理任务上的 failure case。failure 按子领域和错误类型聚类，随后 teacher 合成包含三类制品的 skill file：自然语言推理过程（N-Tok, P1）、可执行代码模板（S-Tok, P2）和已解答示例（N-Tok, P1）。这些 skill file 在推理时被动态注入 student 的 context。整个框架完全无参数更新。并行的 P2（N→S）组件（代码模板）将 ASDA 与纯 P1 方法区分开来——代码模板是结构化、可执行的制品，而非叙事性描述。但主导机制为 P1（failure 分析 → 叙事性推理过程），代码模板作为补充形式化手段。

[Title]: Controllable and Verifiable Tool-Use Data Synthesis for Agentic Reinforcement Learning
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: synthetic tool-use trajectories generated through a two-stage pipeline — reliable base trajectories via self-evolving synthesis, then augmented via oracle-preserving environmental perturbations (distractor tools, ambiguous queries, noisy tool outputs)
- [Target Experience]: policy weights of RL-optimized tool-calling LLMs, encoding robustness to ambiguity and unreliable tool feedback
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: RL-trained policies directly execute tool-calling at inference time; the oracle-preserving design enables automatic reward computation without human labeling
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: 两阶段 pipeline。Stage 1：自演化合成结合多级验证生成可靠的基础 tool-use 轨迹。Stage 2：oracle-preserving 增强系统性地增加环境复杂度——引入 distractor tool、间接用户查询和噪声工具输出——同时严格保留 oracle tool call 和最终答案作为 ground truth。这种设计通过参考匹配（标准情况）和轻量 judge 辅助验证（错误检测行为）直接实现自动 reward 计算，使得在没有人工标注的情况下对 tool-calling 策略进行 RL 优化成为可能。轴心 pathway 为 P5：合成轨迹 → 基于 RL 的策略优化。oracle-preserving 增强策略是关键机制创新：它创建了可验证的训练信号，使 RL 在 tool-use 场景中切实可行。

[Title]: ASTRA: Automated Synthesis of agentic Trajectories and Reinforcement Arenas
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: diverse tool-use trajectories synthesized from tool-call graph topology, paired with decomposed question-answer traces converted into code-executable verifiable RL environments
- [Target Experience]: policy weights of tool-augmented LLMs trained via integrated SFT + online RL, encoding transferable tool-use competence and interaction efficiency
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: trained models directly execute multi-turn tool-use tasks; the verifiable environment design enables deterministic reward computation for online RL without manual feedback
- [Method]: ⟨hybrid⟩
- [Mechanism]: ASTRA 整合了两个互补的合成组件。第一，轨迹合成 pipeline 利用 tool-call graph 的静态拓扑生成结构上有依据的、多样化的轨迹，以建立广泛的 tool-use 能力。第二，环境合成框架将分解后的问答轨迹转换为独立的、代码可执行的、规则可验证的环境，支持确定性的多轮 RL，并提供平衡任务完成与交互效率的轨迹级 reward。统一训练方法将 SFT 与 online RL 相结合。关键机制创新在于可验证环境合成：通过将 QA 轨迹转换为可执行环境，消除了通常限制 tool-use 训练中 RL 应用的验证瓶颈。轴心 pathway 为 P5。

[Title]: Embodied CoT Distillation From LLM To Off-the-shelf Agents
- [Pathway]: Narrative → Policy (P5) with Narrative → Schematic (P2) for embodied knowledge graph
- [Source Experience]: embodied reasoning trajectories generated by a large LLM through embodied in-context learning and self-verification, with intermediate rationales structured via an embodied knowledge graph
- [Target Experience]: policy weights of small language models (sLMs) for both reasoning-policy and planning-policy, deployable on off-the-shelf devices
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}
- [Utilization]: sLM-based policies deployed on capacity-limited devices for real-time embodied task execution; reasoning-policy generates rationales, planning-policy renders optimized plans guided by those rationales
- [Method]: ⟨SFT⟩
- [Mechanism]: DeDa 将决策过程构建为两级层次结构：生成有效推理依据的 reasoning-policy，以及在这些依据引导下产生优化计划的 planning-policy。大型 LLM 通过 embodied ICL 和自我验证生成 embodied reasoning 轨迹，作为将两个策略蒸馏到 sLM 中的训练数据。为提升中间推理依据的质量，embodied knowledge graph（P2: N→S）将 embodied 任务知识组织为结构化图表示，contrastively prompted attention model 支持通过单次推理生成多条推理依据。轴心 pathway 为 P5：teacher 生成的 embodied 轨迹 → sLM 策略权重 via SFT。embodied KG 是辅助性的 P2 机制，用于结构化领域知识。

[Title]: Scalable Data Synthesis for Computer Use Agents with Step-Level Filtering
- [Pathway]: Narrative → Policy (P5) with Narrative → Evaluator (P4) for StepRM
- [Source Experience]: noisy rollout trajectories from a strong CUA (OpenAI computer-use-preview), with individual steps graded and reasoning-augmented via step-level filtering
- [Target Experience]: (P5) policy weights of trained VLM-based CUA models (Qwen-2.5-VL 7B/32B) encoding GUI operation competence; (P4) evaluator weights of StepRM — a 7B multimodal process reward model distilled from o4-mini grading judgments
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}
- [Utilization]: SFT-trained CUAs directly operate GUI interfaces at inference time; StepRM provides step-level grading for process supervision in future training pipelines
- [Method]: ⟨SFT⟩
- [Mechanism]: 核心创新是 step-level filtering：不是丢弃整个有噪 CUA rollout，而是根据任务进展单独评估每个动作步骤，仅保留正确步骤。reasoning augmentation 用规划上下文丰富保留的步骤。这产生了 WebSTAR（13.3K 轨迹，267K 分级步骤）。在 WebSTAR 上进行 SFT 训练 CUA 策略（P5）。独立地，来自 o4-mini 的 step-level grading 被蒸馏为 StepRM——一个 7B 多模态 PRM（P4），以远低于 teacher 的部署成本匹配其评分质量。两条 pathway 是论文中的独立贡献：P5（step-filtered 数据 → CUA 策略）和 P4（分级步骤数据 → evaluator 权重）。P5 pathway 是主要系统贡献；StepRM 是用于未来基于 RL 训练的辅助工具。

[Title]: Symbiotic Cooperation for Web Agents: Harnessing Complementary Strengths of Large and Small LLMs
- [Pathway]: Policy → Narrative → Policy (§8.1)
- [Source Experience]: web interaction trajectories generated by large LLMs exploring web environments, enriched by divergent action choices from distilled small LLMs that explore novel trajectories
- [Target Experience]: improved policy weights for both large LLM agents and small LLM agents through iterative mutual enhancement
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher} (large LLM) and {self} (small LLM rollouts)
- [Utilization]: both large and small LLM agents operate web tasks at inference time; the iterative loop produces symbiotic improvement where each model type enhances the other
- [Method]: ⟨SFT⟩
- [Mechanism]: AgentSymbiotic 在迭代循环中将数据合成与任务执行耦合。大型 LLM 生成高质量 web 交互轨迹，用于通过 SFT 蒸馏小型 LLM（P5）。关键之处在于，蒸馏后的小型 LLM——由于其不同的推理能力——经常选择与大 teacher 不同的动作，从而探索出新颖轨迹，丰富合成数据池。这些新颖轨迹被反馈以进一步改进两个模型。两项创新解决 small-LLM 瓶颈：speculative data synthesis 缓解蒸馏中的 off-policy bias，multi-task learning 提升 student 推理能力。复合模式为 Policy（large LLM）→ Narrative（轨迹）→ Policy（small LLM）→ Narrative（发散轨迹）→ Policy（两个模型），形成迭代的 Policy→Narrative→Policy 循环，匹配 §8.1。论文的贡献在于整合机制：将模型间发散作为探索来源，而非将其作为噪声进行压制。

[Title]: EvoSkill: Automated Skill Discovery for Multi-Agent Systems
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: agent execution failures from task attempts on grounded reasoning (OfficeQA) and search-augmented QA (SealQA) benchmarks
- [Target Experience]: structured, reusable skill folders containing executable workflows and code — materialized as schematized artifacts governed by a Pareto frontier selection mechanism
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: skill folders retrieved and executed at inference time; skills transfer zero-shot across tasks (SealQA skills improve BrowseComp by 5.3%) without modification or parameter updates
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: EvoSkill 通过迭代式 failure 分析运作：分析执行 failure 以识别缺失或缺陷能力，然后提出新技能或对已有技能的编辑，并将其物化为包含可执行代码和工作流的结构化、可复用 skill folder。在 agent program 上的 Pareto frontier 选择机制决定保留——只有提升留出验证集性能的技能被保留，底层模型保持冻结。此为 P2（N→S），因为输出制品是具有形式化接口的可执行代码和结构化工作流，而非叙事性指导。基于 Pareto 的选择机制将 EvoSkill 与简单的追加式技能累积区分开来：它主动策展技能库，移除退化。zero-shot 跨任务迁移表明技能捕获的是任务通用的模式，而非 benchmark 特定的启发式。

[Title]: WebWorld: A Large-Scale World Model for Web Agent Training
- [Pathway]: Policy → Narrative (P7) + Narrative → Policy (P5)
- [Source Experience]: (for world model) 1M+ open-web interactions encoding real web dynamics — page transitions, form submissions, search results; (for agent) synthetic trajectories generated by the world model
- [Target Experience]: (P7) synthetic web interaction trajectories from the world model, covering reasoning, multi-format data, and 30+ step simulations; (P5) policy weights of web agents (Qwen3-14B) trained on synthetic trajectories
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher} (web interaction data for world model training); {teacher} (world model for agent training)
- [Utilization]: world model generates diverse synthetic trajectories for agent SFT and inference-time search; trained agents operate real web tasks; world model also functions as a search-time simulator outperforming GPT-5
- [Method]: ⟨SFT⟩
- [Mechanism]: WebWorld 引入一个基于 1M+ 交互训练的大规模开放 web 模拟器，作为 world model 运行。机制链为：（1）真实 web 交互 → world model 参数 via 训练（P5，系统构建内部步骤）；（2）训练后的 world model 大规模生成合成 web 交互轨迹——推理轨迹、多格式页面转移、30+ 步长程模拟（P7: π-Par→N-Tok，核心贡献）；（3）合成轨迹 → web agent 策略 via SFT（P5）。关键创新在于 world model 作为 tokenized 经验的参数化生成器：它将 web 动力学内化到权重中，然后将其外化为多样化、可控的合成轨迹，克服了真实世界训练约束（网络延迟、速率限制、安全风险）。该 P7 转化是论文的独特贡献——world model 作为可复用的经验放大器，产生与 Gemini-3-Pro 质量匹配的训练数据。跨领域泛化至代码、GUI 和游戏环境进一步验证了 world model 所捕获的知识。

[Title]: Scaling Web Agent Training through Automatic Data Generation and Fine-grained Evaluation
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: web interaction trajectories automatically generated by strong models, with partially successful trajectories retained via constraint-based fine-grained progress evaluation
- [Target Experience]: policy weights of a distilled student model that matches or exceeds commercial systems at significantly smaller scale
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}
- [Utilization]: distilled student model directly executes web tasks at inference time without external augmentation
- [Method]: ⟨SFT⟩
- [Mechanism]: 关键机制创新是基于约束的轨迹评估，提供对任务完成进度的细粒度评估。二元成功/失败过滤会丢弃包含正确子序列的部分成功轨迹，而基于约束的框架从中识别并保留有用的动作片段，显著扩大可用训练数据池。这个丰富的数据集用于标准 SFT，将 web agent 能力蒸馏到更小的 student 模型。轴心 pathway 为 P5：自动生成并过滤的轨迹 → student 策略权重。基于约束的评估是使 P5 在大规模下有效运作而无需人工标注的数据质量机制。

[Title]: OpenMobile: Building Open Mobile Agents with Task and Trajectory Synthesis
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: synthetic mobile task instructions and interaction trajectories generated through two complementary mechanisms: (1) a global environment memory constructed from exploration that grounds diverse task instructions, and (2) policy-switching between learner and expert models that captures error-recovery patterns
- [Target Experience]: policy weights of fine-tuned VLM-based mobile agents (Qwen2.5-VL and Qwen3-VL) encoding broad mobile operation competence including error recovery
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}
- [Utilization]: fine-tuned VLMs directly execute mobile tasks at inference time; open-source release of data and code bridges the data gap in mobile agent research
- [Method]: ⟨SFT⟩
- [Mechanism]: OpenMobile 通过两项合成创新解决 mobile agent 训练中的封闭数据问题。第一，可扩展的任务合成 pipeline：从系统探索中构建 global environment memory，然后利用它生成覆盖环境功能的多样化且接地气的任务指令。第二，policy-switching trajectory rollout 策略：框架在数据收集过程中交替使用 learner 和 expert 模型，确保 error-recovery 数据与 expert demonstration 同时被捕获——这些模式在标准模仿学习中通常缺失。合成轨迹用于对 VLM-based mobile agent 进行 SFT。轴心 pathway 为 P5。policy-switching 策略是关键机制贡献：它解决了 demonstration-only 数据与 error 不可避免的真实部署之间的分布不匹配。

[Title]: Learning with Challenges: Adaptive Difficulty-Aware Data Generation for Mobile GUI Agent Training
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: GUI interaction trajectories synthesized by a multi-agent controllable generator, with task difficulty explicitly sampled from a distribution aligned to the agent's dynamically profiled capability frontier along structural (trajectory length) and semantic (task goal) dimensions
- [Target Experience]: policy weights of GUI agents trained on capability-aligned trajectories, achieving 1.57x average performance improvement across benchmarks
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}
- [Utilization]: trained GUI agents directly operate mobile interfaces at inference time without external augmentation
- [Method]: ⟨SFT⟩
- [Mechanism]: MobileGen 的核心创新是数据生成中的自适应难度对齐。它将任务难度显式解耦为结构维度（轨迹长度、动作数量）和语义维度（任务目标复杂度）。框架在策展的先验数据集上迭代评估 target agent，构建其在两个维度上能力前沿的系统画像——识别 agent 在何处成功、何处失败。然后从该前沿计算难度概率分布，并据此采样下一轮训练的目标准度。multi-agent controllable generator 合成匹配采样难度的轨迹。这创建了一个训练数据难度跟踪 agent 能力扩展的 curriculum，避免了不匹配问题（过易数据无学习效果；过难数据产生噪声）。轴心 pathway 为 P5：难度对齐的轨迹 → GUI agent 策略 via SFT。能力前沿画像是使 P5 训练数据高效的关键机制。

[Title]: Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: raw computer interaction trajectories comprising states (screenshots/DOM) and actions on MiniWoB++ and Mind2Web benchmarks
- [Target Experience]: state-abstracted exemplar trajectories stored in an embedding-indexed memory bank, retrieved via similarity search for in-context prompting
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: retrieved exemplar trajectories prompt the LLM with complete state-action sequences at inference time, improving multi-step decision-making; memory enables generalization to novel tasks via similarity-based retrieval
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Synapse 通过 state abstraction 转化原始计算机交互状态——从原始状态中过滤掉与任务无关的 DOM 元素和视觉区域，产生压缩的状态表示。这些抽象状态与动作配对，形成完整 exemplar 轨迹，存储在 embedding 索引的记忆库中。推理时，相似度搜索检索相关 exemplar 用于 trajectory-as-exemplar prompting，LLM 看到完整的状态-动作序列而非高层计划或多选题。从原始状态到抽象状态的转化构成基本的 P1（N→N）精炼：原始感知 token 序列 → 过滤后的、任务相关的 token 序列。抽象是领域特定的（DOM/视觉过滤）而非语义的（规则/洞察），使其成为抽象下界的弱 P1——经验形态保持 narrative tokenized，仅通过相关性过滤进行压缩。

[Title]: SAGER: Self-Evolving User Policy Skills for Recommendation Agent
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: per-user recommendation failures — interaction logs where the agent's recommended items were rejected, including the decision context and the agent's CoT reasoning that produced the failed recommendation
- [Target Experience]: a per-user structured natural-language policy skill document encoding personalized decision principles, continuously refined through incremental contrastive analysis
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: the evolved skill document is injected at inference time to personalize the agent's reasoning process for that specific user; gains are orthogonal to semantic memory accumulation, confirming that personalizing reasoning is a distinct improvement source
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: SAGER 解决的是不断演化的 per-user semantic memory（Agent 对用户偏好知道了什么）与静态 reasoning logic（Agent 如何做决策）之间的不对称。当推荐失败时，增量对比 chain-of-thought 引擎通过对接受物品和拒绝物品进行对比，同时保留已累积的先验原则，诊断推理缺陷。诊断出的缺陷被蒸馏为 per-user policy skill document 的修订——一份编码个性化决策原则的结构化自然语言文档。双表示 skill 架构将丰富的演化基底（用于详细推理捕捉）与轻量的 inference-time injection（用于高效上下文使用）解耦。演化后的 skill 在 skill-augmented listwise reasoning 过程中被注入，创建精细的决策边界，使 skill 提供真正的判别价值。这是一个纯 P1（N→N）循环：failure experiences → refined decision principles → 作为 narrative guidance 被重用。与标准 memory 系统的关键区别在于，skills 演化的是推理过程本身，而不仅仅是积累偏好事实。

[Title]: Learning to Share: Selective Memory for Efficient Parallel Agentic Systems
- [Pathway]: Out of Scope
- [Mechanism]: LTS 解决的是并行 agent 团队的 memory 管理——一个轻量级 controller 决定哪些中间 agent steps（reasoning traces、tool outputs）进入全局共享 memory bank，哪些保持私有。controller 通过逐步 RL 训练以优化准入决策。然而，准入的内容以原始中间步骤的形式被重用——不存在 experience 向不同 carrier 或抽象层次的转化。这是 memory 准入/选择机制，而非 experience transformation。controller 的训练（对准入决策的 RL）不构成 experience transformation，因为目标是对 memory 访问的门控策略，而非将 experience 语义编码为新的形式。超出本 survey 范围：experience 本身（中间 agent steps）未经历任何表示变化——仅进行了选择和路由。

[Title]: SkillGraph: Self-Evolving Multi-Agent Collaboration with Multimodal Graph Topology
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: failure cases from multi-agent visual reasoning tasks — instances where the collaboration topology or individual agent reasoning produced incorrect outcomes
- [Target Experience]: a self-evolving multimodal Skill Bank containing distilled reasoning heuristics, whose embeddings condition a dynamic collaboration graph topology
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {self}
- [Utilization]: skill embeddings condition the Multimodal Graph Transformer (MMGT) to predict query-adapted collaboration graphs; updated skills feed back into MMGT to enable topology adaptation alongside capability growth
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: SkillGraph 通过两个交互组件共同演化 agent 专业能力和通信拓扑。Skill Designer 分析 failure cases 以蒸馏 reasoning heuristics，构建自演化的 multimodal Skill Bank。这些 heuristics 被编码为 skill embeddings 输入到 Multimodal Graph Transformer（MMGT）中，MMGT 编码 visual tokens、instruction semantics 和活跃的 skill embeddings，预测以 query 为条件的 collaboration graph——用动态、内容感知的信息流取代固定的手工路由。随着 Skill Bank 因新的 heuristics 而演化，更新后的 skill embeddings 反馈回 MMGT，使拓扑能够随能力增长而适配。experience transformation 轴是 P1（N→N）：failure cases → 蒸馏后的 reasoning heuristics 存储在 Skill Bank 中。用于调节 MMGT 的 skill embeddings 是对这些 heuristics 的编码以用于图计算，而非 experience 向不同 carrier 的转化——核心 experience 内容仍然是 narrative heuristics。Skill Designer 与 MMGT 之间的自演化循环构成了本文的整合贡献，但转化本身是 P1。
[Title]: AdaExplore: Failure-Driven Adaptation and Diversity-Preserving Search for Efficient Kernel Generation
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: execution feedback from LLM agent's kernel code generation attempts — failed and suboptimal generations with compiler/runtime error signals
- [Target Experience]: reusable memory of validity rules distilled from recurring failures, constraining subsequent generation to the feasible set
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: validity rules injected as constraints during subsequent kernel generation to keep outputs within the feasible set; combined with diversity-preserving tree search for optimization
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 两个互补阶段，均 training-free。Stage 1（failure-driven adaptation，P1）：agent 合成 kernel 任务，执行它们，并将反复出现的 failure patterns 转化为可重用的 validity rules memory——这些规则将后续生成约束在 Triton 领域特定限制的可行集合内。Stage 2（diversity-preserving search）：候选 kernels 被组织为树结构，在小范围局部精化和较大结构性重新生成之间交替，以探索超出局部最优的优化前景。随着观察到更多失败，Stage 1 积累的 validity rules 价值不断复合。无参数更新——所有改进来源于 narrative experience 积累和结构化搜索。

[Title]: MetaClaw: Just Talk -- An Agent That Meta-Learns and Evolves in the Wild
- [Pathway]: Policy → Narrative → Narrative → Policy (§8.1 + P1 refinement)
- [Source Experience]: agent's own failure trajectories from task execution on diverse workloads across 20+ channels (N-Tok)
- [Target Experience]: refined behavioral skills synthesized via LLM evolver (N-Tok, P1) + updated policy weights via LoRA SFT and RL-PRM (π-Par, P5)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: skills enable immediate zero-downtime adaptation via fast skill injection; policy weights provide permanent capability improvement; skills and policy mutually reinforce through the iterative loop
- [Method]: ⟨LLM-extract⟩ + ⟨SFT⟩ + ⟨RL: PPO⟩
- [Mechanism]: MetaClaw 运行一个包含两个互补机制的自演化循环。(1) Skill-driven fast adaptation：LLM evolver 分析 failure trajectories 并合成新的 behavioral skill descriptions——从原始 failure logs 到结构化 skill narratives 的 P1（N→N）精化——实现无需重新训练的即时适配。(2) Opportunistic policy optimization：合成后的 skills 结合高质量 trajectories 作为 cloud LoRA SFT 和 RL-PRM policy optimization（P5：N→Policy）的训练数据，由 Opportunistic Meta-Learning Scheduler（OMLS）触发，该调度器通过系统不活动和日历数据检测用户非活跃窗口。两个机制形成相互强化循环：精化的 policy 为 skill synthesis 生成更高质量的 trajectories（Policy→Narrative），而更丰富的 skills 为 policy optimization 提供更好的训练数据（Narrative→Policy）。这是典型的 Policy→Narrative→Policy self-generation composite（§8.1），其中 Narrative 阶段包含 P1 refinement（raw failures → distilled skills）。versioning 机制通过分离 support 和 query 数据来防止数据污染。

[Title]: APIGen-MT: Agentic Pipeline for Multi-Turn Data Generation via Simulated Agent-Human Interplay
- [Pathway]: Policy → Narrative → Policy (P7 → P5)
- [Source Experience]: teacher LLM's parametric knowledge externalized through agentic task blueprint generation and simulated human-agent interplay
- [Target Experience]: verified multi-turn interaction trajectories with ground-truth actions (N-Tok, P7) + xLAM-2-fc-r policy weights from 1B to 70B (π-Par, P5)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: synthetic trajectories used for SFT of the xLAM-2-fc-r model family; models outperform GPT-4o and Claude 3.5 on τ-bench and BFCL
- [Method]: ⟨LLM-extract⟩ + ⟨SFT⟩
- [Mechanism]: 两阶段数据合成。Phase 1：teacher LLM 生成带有 ground-truth actions 的详细 task blueprints；由 LLM reviewers 委员会和迭代 feedback loops 验证 blueprint 正确性。Phase 2：经过验证的 blueprints 通过 simulated agent-human interplay 转化为完整的 multi-turn interaction trajectories。这构成 P7（Parametric→Tokenized）：teacher LLM 关于 agent interactions 的 implicit knowledge 被外化为 explicit、verified tokenized form。合成管线是主要贡献——验证架构（committee review + iterative feedback）是核心创新。生成的 5K trajectories 随后通过 SFT 用于微调 xLAM-2-fc-r model family（P5：Tokenized→Policy）。composite P7→P5 并非 self-generation loop；数据从 teacher 到 student 单向流动。

[Title]: ToolAlpaca: Generalized Tool Learning for Language Models with 3000 Simulated Cases
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: synthetic tool-use interaction corpus generated by a multi-agent simulation environment spanning 400+ real-world APIs across 50 categories (N-Tok)
- [Target Experience]: policy weights of ToolAlpaca-7B and ToolAlpaca-13B encoding generalized tool-use capability (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: fine-tuned compact LMs directly execute tool-use tasks at inference time, including previously unseen tools without tool-specific training
- [Method]: ⟨SFT⟩
- [Mechanism]: 多 agent simulation environment 通过让多个 LLM agents 与涵盖 50 个类别的 real-world tool APIs 交互，自动生成多样化的 tool-use corpus（3,938 个实例）。corpus 被格式化为 tool-use interaction trajectories。compact LMs 通过标准 SFT 在该 corpus 上微调，将通用的 tool-use patterns 内化到 policy weights 中。研究问题——较小的 LMs 是否能在无需 tool-specific training 的情况下实现 generalized tool-use——驱动了 P5 轴 pathway：synthetic trajectories 是手段，编码在结果 policy 中的 generalized tool-use capability 是目的。multi-agent simulation 作为数据生成策略具有创新性，但与 APIGen/APIGen-MT 不同，本文的框架以学习结果为中心，而非将合成管线作为独立贡献。

[Title]: APIGen: Automated Pipeline for Generating Verifiable and Diverse Function-Calling Datasets
- [Pathway]: Policy → Narrative → Policy (P7 → P5)
- [Source Experience]: teacher LLM's parametric knowledge externalized into function-calling scenarios using 3,673 executable APIs across 21 categories
- [Target Experience]: verified function-calling datasets with format/execution/semantic guarantees (N-Tok, P7) + function-calling agent policy weights achieving SOTA on Berkeley Function-Calling Benchmark (π-Par, P5)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: 60K-entry verified dataset for training function-calling agents; 7B model achieves SOTA, 1B model surpasses GPT-3.5-Turbo and Claude-3 Haiku
- [Method]: ⟨LLM-extract⟩ + ⟨SFT⟩
- [Mechanism]: APIGen 收集 3,673 个跨 21 个类别的 executable APIs，使用 teacher LLM 生成多样化的 function-calling scenarios。区分性机制是三层 hierarchical verification：format checking（语法有效性）、actual function execution（运行时正确性）和 semantic verification（任务对齐）。只有通过全部三个阶段的数据进入 training corpus。这构成 P7（Parametric→Tokenized）：teacher LLM 的 implicit function-calling knowledge 被外化为 verified tokenized data，验证管线是主要贡献。经过验证的数据集用于通过 SFT 微调模型（P5）。composite 为 P7→P5，重点在合成阶段；模型训练作为数据质量的验证。

[Title]: ToolACE: Winning the Points of LLM Function Calling
- [Pathway]: Policy → Narrative → Policy (P7 → P5)
- [Source Experience]: teacher LLM's parametric knowledge externalized through self-evolution synthesis across a curated pool of 26,507 diverse APIs
- [Target Experience]: accurate and complex tool-learning dialog corpus with dual-layer verification (N-Tok, P7) + tool-calling policy weights achieving SOTA on Berkeley Function-Calling Leaderboard (π-Par, P5)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: synthetic dialogs used to train 8B models that rival the latest GPT-4 models on the BFCL benchmark
- [Method]: ⟨LLM-extract⟩ + ⟨SFT⟩
- [Mechanism]: ToolACE 采用 self-evolution synthesis 流程：teacher LLM 迭代精化和扩展一个 API pool 至 26,507 个多样化 APIs，然后通过 multi-agent interplay 与 formalized thinking process 生成复杂的 tool-use dialogs。dual-layer verification system 结合 rule-based checks（结构有效性）和 model-based checks（语义正确性）确保数据准确性。这是 P7（Parametric→Tokenized）：self-evolution synthesis pipeline 是核心机制创新，将 teacher 的 tool-use knowledge 外化为 verified dialog 形式。经过验证的 dialogs 用于 SFT（P5），生成在 BFCL 上媲美 GPT-4 的 8B 模型。composite P7→P5，合成管线为主要贡献。

[Title]: Large Language Model as a Policy Teacher for Training Reinforcement Learning Agents
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: high-level instructions and guidance provided by a teacher LLM agent for embodied sequential decision-making tasks in MiniGrid and Habitat (N-Tok)
- [Target Experience]: policy weights of a smaller, specialized student RL agent that surpasses the teacher on the target task (π-Par)
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}
- [Utilization]: student RL agent operates autonomously in embodied environments without the high deployment cost and latency of an LLM-based teacher
- [Method]: ⟨RL: PPO⟩
- [Mechanism]: teacher LLM agent 为 embodied tasks（MiniGrid、Habitat）提供针对性的 high-level instructions。student RL agent 将这些 teacher guidance 作为先验知识纳入，通过带有 environment feedback 的 RL training 将 LLM 的战略理解蒸馏到自己的 policy 中。student 的训练所需 environment data 显著少于从零训练，因为 teacher 的指导减少了探索负担。通过持续的 environment interaction，student 最终在目标任务上超越 teacher 的能力。这是 P5（Tokenized→Policy）：teacher 的 tokenized instructions 被内化到 student 的 parametric policy 中。本文的贡献是整合机制——如何有效使用 LLM-generated instructions 作为 RL agents 的训练信号——而非数据合成管线本身。关键的是，这并非 self-generation loop：teacher 和 student 是不同的模型，且 student 不生成自己的训练数据。

[Title]: Policy Improvement using Language Feedback Models
- [Pathway]: Narrative → Evaluator → Policy (§8.2, P4+P6)
- [Source Experience]: visual agent trajectories verbalized into language descriptions paired with LLM-provided feedback identifying which actions constitute desirable behavior (N-Tok)
- [Target Experience]: LFM evaluator weights trained to predict action desirability from verbalized trajectories (V-Par, P4) + improved policy weights via LFM-guided imitation learning (π-Par, P6)
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {teacher}
- [Utilization]: LFM identifies desirable behavior for imitation learning, improving task-completion over behavioral cloning baselines; LFM generalizes to unseen environments; can provide human-interpretable feedback
- [Method]: ⟨SFT⟩ + imitation learning
- [Mechanism]: pipeline 包含两个阶段。Stage 1（P4）：agents 的 visual trajectories 被语言化为 language descriptions；LLM 提供 feedback，标注哪些 actions 有助于完成任务，哪些没有。这些（verbalized trajectory, desirability label）数据通过 SFT 用于训练 Language Feedback Model（LFM）——一个 evaluator（V-Par），从 language descriptions 预测 action desirability。Stage 2（P6）：训练后的 LFM 评估来自 behavioral cloning 的 demonstration data，过滤掉 undesirable actions。过滤后的 demonstrations 用于 imitation learning 训练改进的 policy。这是 §8.2 composite（N→Evaluator→Policy）。整合机制——使用 language 作为 evaluator training 的媒介，然后使用 evaluator 过滤 training data 以进行 policy improvement——使得能够利用 LLM feedback 而无须在部署时使用 LLM。LFM 比直接使用 LLM 进行 action prediction 成本显著更低，并通过 adaptation 泛化到 unseen environments。

[Title]: Policy Learning with a Language Bottleneck
- [Pathway]: Policy → Narrative → Policy (§8.1, P7+P5)
- [Source Experience]: agent's own behavioral data generated by the current policy across diverse tasks — two-player signaling game, maze navigation, image reconstruction, robot grasp planning (N-Tok)
- [Target Experience]: linguistic rules capturing high-level behavioral strategies (N-Tok, P7) + improved policy weights generalizable across task variations (π-Par, P5)
- [Source Modality]: [cross-modal]
- [Target Modality]: [cross-modal]
- [Experience Source]: {self}
- [Utilization]: linguistic rules make policy behavior interpretable and generalizable; rules can be shared with human users for improved human-AI coordination
- [Method]: ⟨LLM-extract⟩ + ⟨RL⟩
- [Mechanism]: PLLB 实现了一个"language bottleneck"，在 policy refinement 之前强制 agent 行为通过 explicit linguistic representation。每次迭代中：(1) 当前 policy 在 task instances 中生成 behaviors；(2) language model 分析这些 behaviors 并提取 linguistic rules，捕捉 rewarding behaviors 背后的 high-level strategies——这是 P7（Policy→Narrative）：policy 的 implicit behavioral knowledge 被外化为 explicit、human-readable rules；(3) 这些 rules 通过约束或指导学习来引导后续的 policy update 步骤，即使单个 rule 不足以描述整个 complex policy——这是 P5（Narrative→Policy）。迭代交替产生越来越可解释和可泛化的 policies。这是典型的 §8.1 self-generation composite（Policy→Narrative→Policy），其中"language bottleneck"是整合机制：通过强制所有 behavioral knowledge 经过 explicit linguistic intermediate，框架实现了直接 policy-to-policy distillation 无法达到的可解释性和泛化性。本文的贡献是整合机制本身——迭代 rule-policy 交替——而非任何孤立的单一 pathway。

[Title]: AgentTuning: Enabling Generalized Agent Abilities for LLMs
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: high-quality agent interaction trajectories in the AgentInstruct dataset, covering planning, memory, and tool-use agent tasks (N-Tok)
- [Target Experience]: AgentLM policy weights (7B, 13B, 70B) for the Llama 2 series, encoding generalized agent capabilities while preserving general language competence (π-Par)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: AgentLM models directly perform agent tasks at inference time; AgentLM-70B matches GPT-3.5-turbo on unseen agent tasks
- [Method]: ⟨SFT⟩
- [Mechanism]: AgentInstruct 是一个轻量级 instruction-tuning 数据集，包含跨 planning、memory 与 tool-use agent 领域的高质量交互轨迹。混合 instruction-tuning 策略将 AgentInstruct 与开源通用领域指令结合。Llama 2 系列通过 SFT 在该混合语料上进行微调。标准的 P5（Narrative→Policy）路径：精选的 agent 交互轨迹被内化至 policy weights。关键设计选择在于混合训练策略——将 agent 特定数据与通用指令混合——确保生成的 AgentLM 模型在获得 agent 能力的同时不牺牲通用语言能力。论文的贡献在于证明开源 LLM 可通过 targeted instruction tuning 在 agent 任务上匹配商业模型，而非数据生成机制本身。

[Title]: GuardAgent: Safeguard LLM Agents by a Guard Agent via Knowledge-Enabled Reasoning
- [Pathway]: Out of Scope
- [Mechanism]: GuardAgent 通过将文本 guard request 翻译为可执行 guardrail code，对目标 LLM agent 的 inputs/outputs 执行安全检查。两步流程：planning（分析 guard request 创建 task plan）与 code generation（通过 API 调用生成 guardrail code）。使用从 memory module 检索的 in-context demonstrations；无 LLM 训练或参数更新。guard agent 是作用于目标 agent 输入/输出的安全过滤器——并不在 carrier 之间转化目标 agent 的经验。不存在映射到 7 条 pathway 中任何一条的机制：agent experience 未发生向不同表征形式的 carrier transformation。论文贡献在于安全工程（guardrail architecture, benchmark construction），而非本 Survey 定义的 experience transformation。

[Title]: MobileGPT: Augmenting LLM with Human-like App Memory for Mobile Task Automation
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: raw mobile app interaction traces from task demonstration or exploration, capturing screen states, touch actions, and app transitions (N-Tok)
- [Target Experience]: modular, reusable sub-task procedures stored in structured app memory — each sub-task encodes a self-contained action sequence with explicit preconditions and effects (S-Tok)
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {human}
- [Utilization]: modular sub-tasks are retrieved, re-arranged, and adapted at inference time for novel task contexts; structured decomposition reduces latency by 62.5% and cost by 68.8% vs. GPT-4 baseline
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: MobileGPT 通过四阶段模拟人类与移动 app 交互的认知过程：explore（导航 app 发现交互模式）、select（识别任务相关交互片段）、derive（将原始交互轨迹分解为具有显式接口的结构化、模块化子任务过程）与 recall（为新任务实例检索并组合子任务）。derive 阶段构成 P2（Narrative→Schematic）：原始 GUI 交互轨迹（屏幕状态与动作序列）被转化为具有形式化 precondition、动作序列与预期结果的结构化子任务过程。这些子任务存储于 app memory，在推理时组合使用。模块化结构使得将子任务重新用于不同目标时能达到近乎完美的 adaptation accuracy（98.75%）。论文贡献在于实现一次学习多次复用的 memory architecture；P2 提取机制是核心 experience transformation。

[Title]: Distilling Script Knowledge from Large Language Models for Constrained Language Planning
- [Pathway]: Policy → Narrative → Policy (P7 → P5)
- [Source Experience]: teacher LLM's parametric script knowledge for constrained planning goals (e.g., "make a cake for diabetics") with multi-facet constraints
- [Target Experience]: Coscript dataset of 55,000 verified constrained planning scripts (N-Tok, P7) + smaller LM policy weights encoding constrained planning ability (π-Par, P5)
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Coscript dataset used to endow smaller LMs with constrained language planning ability via SFT; smaller LMs directly generate constraint-satisfying plans at inference time
- [Method]: ⟨LLM-extract⟩ + ⟨SFT⟩
- [Mechanism]: Teacher LLM 通过 over-generate-then-filter 方法为 constrained language planning 目标生成多样化候选 scripts。核心机制是 constraint faithfulness filtering：生成 scripts 经多面约束检验，仅保留约束满足的 scripts。这构成了 Coscript——包含 55,000 个已验证 scripts 的数据集。这是 P7（Policy→Narrative）：teacher LLM 关于 constraint satisfaction 的隐含 script planning 知识被外化为显式、经过验证的 tokenized 数据集。over-generate-then-filter 策略是合成创新。Coscript 随后通过 SFT 用于微调较小 LM（P5: Narrative→Policy），将 teacher 的 constrained planning 能力蒸馏至 compact models。复合路径为 P7→P5，distillation pipeline（over-generate-then-filter synthesis）是主要贡献，与论文标题以 distillation 为核心机制一致。
