[Title]: Agent KB: Leveraging Cross-Domain Experience for Agentic Problem Solving
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Cross-framework agent problem-solving trajectories and failure/success experiences
- [Target Experience]: Structured knowledge base with reusable workflows, diagnostic fixes, and API-served memory entries
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: At inference time, retrieved workflows seed planning and retrieved diagnostic fixes guide feedback correction across heterogeneous agent frameworks.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 该系统汇聚不同 agent 框架中的轨迹，从中提取可复用的规划经验与失败修复知识，将其组织成共享知识库，并用分歧门控降低跨框架检索带来的干扰。

[Title]: SkillX: Automatically Constructing Skill Knowledge Bases for Agents
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Raw long-horizon agent trajectories from user-interactive environments
- [Target Experience]: Three-tier SkillKB containing strategic plans, functional skills, and atomic skills
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: The plug-and-play skill knowledge base is attached to weaker agents to improve task success and execution efficiency.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 原始轨迹被蒸馏成层级化 skill schema，再根据执行反馈修订，并通过生成与验证新技能来扩展种子数据之外的覆盖范围。

[Title]: Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Diverse execution trajectories and trajectory-specific lessons
- [Target Experience]: Unified conflict-free skill directory / declarative skill guide
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: The evolved skills are supplied to other LLM agents as reusable declarative task skills without parameter updates or retrieval modules.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 并行子 agent 分析大量执行记录，抽取单条轨迹中的局部经验，再通过归纳推理把这些经验合并成统一且无冲突的可迁移 skill directory。

[Title]: Memp: Exploring Agent Procedural Memory
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Past agent trajectories in TravelPlanner and ALFWorld-style tasks
- [Target Experience]: Procedural memory repository with step-by-step instructions and script-like abstractions
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Retrieved procedural memories guide analogous future tasks and can be migrated from stronger to weaker models.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 框架围绕 procedural memory 执行构建、检索、更新、纠错和废弃，使原始轨迹转化为可复用的 step-by-step instructions 与 script-like abstractions，并随新经验持续演化。

[Title]: AgentDistill: Training-Free Agent Distillation with Generalizable MCP Boxes
- [Pathway]: Policy → Schematic (P7)
- [Source Experience]: Teacher agents' implicit planning, memory, and tool-use capabilities
- [Target Experience]: Model-Context-Protocol boxes as structured reusable task-solving modules
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Student agents directly reuse distilled MCP boxes to solve new tasks without retraining or replaying full teacher trajectories.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 教师 agent 将参数中的任务求解策略外化为显式 MCP 模块，用结构化 agent procedure 的直接复用替代逐步模仿或整段轨迹回放。

[Title]: AutoRefine: From Trajectories to Reusable Expertise for Continual LLM Agent Refinement
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Agent execution histories with procedural subtask behavior and static task knowledge
- [Target Experience]: Dual-form Experience Patterns: specialized subagents, guidelines, and code snippets
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Maintained patterns are reused to coordinate procedural subtasks, guide static decisions, reduce steps, and improve future task completion.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 执行历史被拆分为 procedural 与 static 两类内容，分别转化为 subagent 或 skill pattern，再通过评分、剪枝和合并维护库质量。

[Title]: Skill-Pro: Learning Reusable Skills from Experience via Non-Parametric PPO for LLM Agents
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Passive episodic interaction narratives
- [Target Experience]: Executable Skills with activation, execution, and termination conditions
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Verified procedural skills form compact memory that is reused across in-domain, cross-task, and cross-agent settings.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 该方法将问题形式化为 Skill-MDP，用 semantic gradients 生成技能候选，用 PPO Gate 验证可靠性，并通过分数维护把 episodic narratives 转为可执行 procedural memory。

[Title]: Compiled Memory: Not More Information, but More Precise Instructions for Language Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Agent failures and successes during task execution
- [Target Experience]: Learned system-prompt sub-bullets / compiled instruction structure
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: The evolved prompt is reused as the agent's instruction structure, including across models, instead of injecting raw memories.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 从失败和成功中抽取的事实先通过三步 promotion gate，再被写入 system prompt 的 learned sub-bullets，使经验以精确指令形式承载。

[Title]: Traversal-as-Policy: Log-Distilled Gated Behavior Trees as Externalized, Verifiable Policies for Safe, Robust, and Efficient Agents
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Sandboxed OpenHands execution logs, including successful and unsafe traces
- [Target Experience]: Executable Gated Behavior Tree with state-conditioned action macros and safety gates
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: The tree traverser executes matched macros under gates, uses path recovery when stalled, and replaces transcript replay with compact spine memory.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 成功日志被挖掘为 state-conditioned action macro，不安全轨迹生成确定性的 pre-execution gate，再经 merge check 与单调更新形成可验证的控制树。

[Title]: SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning
- [Pathway]: Narrative → Schematic → Policy (P2 + P5)
- [Source Experience]: Raw agent trajectories from ALFWorld, WebShop, and search-augmented tasks
- [Target Experience]: Hierarchical SkillBank and recursively improved agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: SkillBank entries are retrieved as general and task-specific heuristics while the skill library co-evolves with policy learning.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段 1 对应 P2：raw trajectories 被蒸馏成层级 skill library。阶段 2 对应 P5：检索到的技能参与强化学习循环，使 policy improvement 与 skill evolution 相互促进。

[Title]: Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Success patterns, failure triggers, and comparative interaction insights
- [Target Experience]: Compact experience pool of fine-grained textual memories
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Retrieved and context-adapted historical insights guide future BFCL-V3 and AppWorld decisions.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 该框架从每条经验中提取成功模式、失败触发因素和比较性洞见，按场景索引，并通过加入有效 memory 与剪除过时 memory 来维护紧凑经验池。

[Title]: Agent Workflow Memory
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Offline examples or online web-navigation action trajectories
- [Target Experience]: Reusable routines / workflows
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {human}
- [Utilization]: Workflows are selectively supplied to the agent to guide subsequent web-navigation generations.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 该方法从复杂动作轨迹中归纳常用 routines，并在离线或在线场景中复用这些 workflows，以降低长程任务规划成本。

[Title]: Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Execution feedback from agent and domain-specific reasoning runs
- [Target Experience]: Evolving playbooks containing strategies, evidence, and organized context updates
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: The evolved contexts are used as system prompts or online memory to adapt future inference without weight updates.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 该框架通过 generation、reflection 与 curation，把执行反馈转化为结构化的增量 context edits，在多轮更新中保留细粒度策略知识。

[Title]: SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Practice experiences from autonomous website exploration
- [Target Experience]: Lightweight plug-and-play APIs representing reusable web skills
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Synthesized APIs are shared across web agents and transferred from stronger to weaker agents.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 智能体发现网站技能、执行练习任务，再把实践经验蒸馏为稳健 API procedure，并通过迭代探索扩充 API library。

[Title]: What Deserves Memory: Adaptive Memory Distillation for LLM Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Raw interaction sequences
- [Target Experience]: Coherent episodic narratives and prediction-error-based semantic insights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Distilled memory entries are retained for downstream memory management and future agent adaptation.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 该框架先把 raw interactions 整合为连贯 narrative，再用 prediction error 判断哪些 insight 具有未来效用并值得保留。

[Title]: Don't Retrieve, Navigate: Distilling Enterprise Knowledge into Navigable Agent Skills for QA and RAG
- [Pathway]: Out of Scope
- [Mechanism]: 源端是静态文档语料库，不是 grounded in agent trajectories 的决策过程经验，因此落入 Project_Infos.md §3.2 的 static-corpus 边界。

[Title]: ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Self-judged successful and failed interaction experiences
- [Target Experience]: Generalizable reasoning strategies stored in ReasoningBank
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Retrieved reasoning memories inform future interactions and newly learned memories are integrated back during test-time scaling.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 智能体生成多样化经验，用成功与失败之间的对比信号合成更高质量的 reasoning strategy memory，并在持续循环中更新 memory bank。

[Title]: Inducing Programmatic Skills for Agentic Tasks
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Online web-environment interaction experience and primitive action traces
- [Target Experience]: Program-based task-specific skills
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Programmatic skills are verified, reused, and updated for future web activities and cross-website transfer.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 该方法把 primitive actions 组合成更高层级的可执行程序，在 induction 阶段验证程序，并在网站变化时修订不兼容技能。

[Title]: SCOPE: Prompt Evolution for Enhancing Agent Effectiveness
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Execution traces containing corrective and enhancement failures
- [Target Experience]: Evolved prompt guidelines with tactical and strategic rules
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: The evolved prompt guides later agent executions without human intervention.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 该方法从 execution traces 合成 guidelines，将短期错误修复和长期原则分成两条流，并通过 perspective-driven exploration 扩大策略覆盖。

[Title]: FLEX: Continuous Agent Evolution via Forward Learning from Experience
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Successes and failures accumulated during environment interaction
- [Target Experience]: Structured experience library of reflected lessons
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: The library is reused by frozen LLM agents for continuous, inheritable improvement across reasoning and scientific tasks.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 该方法持续反思成功与失败，把得到的 experience objects 存入结构化库，并将其作为无梯度 evolution substrate 在 agent 间继承。

[Title]: Learning on the Job: An Experience-Driven Self-Evolving Agent for Long-Horizon Tasks
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Sub-task execution trajectories in long-horizon productivity tasks
- [Target Experience]: Structured experience entries inside a hierarchical Memory Module
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: The memory module supports planning and execution on later tasks and enables zero-shot improvement on new tasks.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 每个 sub-task 执行后，agent 反思轨迹，将 raw trajectory 转化为 structured experience，并写入供后续规划使用的 hierarchical memory。

[Title]: AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials
- [Pathway]: Narrative → Schematic → Narrative
- [Source Experience]: Public web tutorials containing human procedural task knowledge
- [Target Experience]: Verified multimodal web-agent trajectories with CoT reasoning, HTML/function-call actions, screenshot observations, and pixel actions
- [Source Modality]: [txt]
- [Target Modality]: [GUI]
- [Experience Source]: {human}, {teacher}
- [Utilization]: Synthesized trajectories train advanced GUI agents on textual and visual web browsing benchmarks.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段 1 对应 P2：tutorial text 被过滤并转化为带 step instructions 的结构化任务规格。阶段 2 将规格扩展为经 VLM 执行验证的 GUI 轨迹；该 Schematic → Narrative 扩展不属于七条基础路径，因为源端是 tokenized instructions 而非参数权重。

[Title]: Get Experience from Practice: LLM Agents with Record & Replay
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Agent interaction traces with environment observations and internal decisions
- [Target Experience]: Structured experience objects encoding workflows, constraints, and check functions
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {human}
- [Utilization]: Structured experiences are replayed to guide similar future tasks, support collaboration, and reduce cost.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 该机制记录交互 trace，将其概括为多层 workflow/constraint abstraction，并附加 check function 作为 replay 阶段的完整性与安全性锚点。

[Title]: Explorer: Scaling Exploration-driven Web Trajectory Synthesis for Multimodal Web Agents
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: LMM exploration policy and refinement process over web environments
- [Target Experience]: Large-scale successful multimodal web trajectories and a trained multimodal web agent
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {teacher}
- [Utilization]: The synthesized trajectory dataset is used to train Explorer and study web-agent data scaling.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P7：LMM agent 将 web-control policy 外化为成功的 screenshot/web-element 轨迹。阶段 2 对应 P5：这些 tokenized trajectories 用于监督 multimodal web agent。

[Title]: Contextual Experience Replay for Self-Improvement of Language Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Past web-navigation experiences containing environment dynamics and decision patterns
- [Target Experience]: Dynamic memory buffer of synthesized decision knowledge
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Relevant memory is retrieved into the context window to adapt the agent on new WebArena and VisualWebArena tasks.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 该框架积累过往经验，把它们合成为紧凑的 dynamic memory，并在推理时检索为 contextual guidance。

[Title]: Towards Internet-Scale Training For Agents
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: LLM-generated website tasks, agent-completed trajectories, and LLM success judgments
- [Target Experience]: Effective web-agent trajectory dataset and trained Qwen web agents
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}, {self}
- [Utilization]: Filtered trajectories are used to train smaller web agents that compete with frontier policies.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P7：LLM 标注网站，agent 生成轨迹，LLM 再过滤成功样本，将 web-task behavior 外化为数据。阶段 2 对应 P5：生成的轨迹被内化到 Qwen web-agent weights。

[Title]: RAGShaper: Eliciting Sophisticated Agentic RAG Skills via Automated Data Synthesis
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: Teacher-agent navigation through adversarial retrieval environments
- [Target Experience]: Robust RAG-agent trajectories demonstrating error correction and noise rejection, plus trained models
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: The synthesized corpus trains agentic RAG models to handle noisy, complex retrieval tasks.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P7：RAGShaper 构建含 distractor 的 information trees，并迫使 teacher agent 生成具备纠错和抗噪能力的 retrieval trajectories。阶段 2 对应 P5：模型在合成 demonstrations 上训练。

[Title]: Structured Distillation of Web Agent Capabilities Enables Generalization
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: Gemini 3 Pro teacher web-agent behavior organized through modular annotation roles
- [Target Experience]: Quality-filtered synthetic web trajectories and a fine-tuned 9B student web agent
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}
- [Utilization]: The filtered trajectories are used for supervised fine-tuning of a locally deployable web agent.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P7：frontier teacher 将 web navigation 能力外化为 role-structured trajectories、hints 和 reasoning traces。阶段 2 对应 P5：通过过滤的轨迹被 9B student 以 supervised learning 内化。

[Title]: Meta-Policy Reflexion: Reusable Reflective Memory and Rule Admissibility for Resource-Efficient LLM Agent
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: LLM-generated reflections from failed or inefficient AlfWorld-style episodes
- [Target Experience]: Predicate-like Meta-Policy Memory with soft guidance and hard admissibility rules
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: The memory guides decoding and blocks invalid or unsafe actions through hard rule checks at inference time.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 反思内容被整合为结构化 predicates，并在推理时同时作为 soft memory 指导生成、作为 hard admissibility constraints 约束候选动作。

[Title]: WebXSkill: Skill Learning for Autonomous Web Agents
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Synthetic web-agent trajectories containing reusable action subsequences
- [Target Experience]: Parameterized executable skills paired with step-level natural language guidance and URL graph index
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}, {self}
- [Utilization]: Skills run in grounded mode for automatic execution or guided mode as step-by-step instructions for native planning.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 可复用 subsequences 从轨迹中挖掘出来，被抽象为带 guidance 的 parameterized programs，按 URL graph 组织，并作为 executable web skills 部署。

[Title]: XSkill: Continual Learning from Experience and Skills in Multimodal Agents
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Visually grounded multi-path multimodal rollouts and usage history
- [Target Experience]: Dual knowledge streams: action-level experiences and structured task-level skills
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {self}
- [Utilization]: Retrieved experiences and skills are adapted to the current visual context and fed back into continual accumulation.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 多路径 rollouts 基于视觉观察被总结，并接受 cross-rollout critique；主干 P2 分支蒸馏 task-level structured skills，次要 P1 分支保留 concise action-level guidance。

[Title]: CLIN: A Continually Learning Language Agent for Rapid Task Adaptation and Generalization
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Repeated ScienceWorld trials with environment and task variation
- [Target Experience]: Persistent textual memory centered on causal abstractions
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Updated memory is recalled in later trials and transferred to new environments or new tasks.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 每轮 trial 后，CLIN 更新以 causal abstractions 为核心的动态 memory，使一个任务或环境中的经验可以影响后续决策。

[Title]: Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Past mobile task experiences, action reflections, and information gathered by the hierarchical agent
- [Target Experience]: Long-term memory containing Tips and executable Shortcuts
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Tips guide general interaction and Shortcuts execute reusable subroutines for future long-horizon mobile tasks.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 系统中的 Action Reflector 与 Notetaker 将先前移动端交互转化为通用 lessons 和可复用 operation sequences；可执行 Shortcuts 是 P2 分支，Tips 构成次要 P1 分支。

[Title]: TOUCAN: Synthesizing 1.5M Tool-Agentic Data from Real-World MCP Environments
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: Teacher-model tool-use policies operating in real MCP environments
- [Target Experience]: 1.5M synthetic tool-agentic trajectories and fine-tuned tool agents
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Filtered trajectories are used to fine-tune models for BFCL V3 and MCP-Universe style tool use.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P7：teacher models 与 agentic frameworks 在真实 MCP 环境中生成 tool-execution trajectories。阶段 2 对应 P5：模型通过 fine-tuning 内化生成轨迹。

[Title]: SkillDroid: Compile Once, Reuse Forever
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Successful LLM-guided mobile GUI trajectories and reliability failures
- [Target Experience]: Parameterized skill templates with UI action sequences, weighted element locators, and typed slots
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Stored skills are matched and replayed on future invocations without LLM calls; failures trigger recompilation.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 成功轨迹被编译为可执行 templates，再由 instruction/app matching 路由；当 replay 可靠性下降时，failure-learning 层触发重新编译。

[Title]: G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Multi-agent collaboration trajectories across trials
- [Target Experience]: Three-tier graph hierarchy of insight, query, and interaction graphs
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Bi-directional graph traversal retrieves high-level insights and condensed interaction traces for later multi-agent execution.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 该系统将协作轨迹吸收到 insight、query 和 interaction 三层 graph 中，使 agent teams 能够检索并更新 organizational memory。

[Title]: Steve-Evolving: Open-World Embodied Self-Evolution via Fine-Grained Diagnosis and Dual-Track Knowledge Distillation
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Subgoal attempts with pre-state, action, diagnosis result, post-state, and execution-diagnosis signals
- [Target Experience]: Reusable skills with preconditions and verification criteria, plus executable guardrails
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: Retrieved skills and guardrails are injected into the LLM planner and updated during diagnosis-triggered replanning.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 经验锚定阶段将每次 attempt 固化为 structured tuple；成功经验被泛化为 skills，失败经验被蒸馏为 guardrails，closed-loop control 在在线重规划中更新约束。

[Title]: M2: Dual-Memory Augmentation for Long-Horizon Web Agents via Trajectory Summarization and Insight Retrieval
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Verbose multimodal web interaction histories and offline insight examples
- [Target Experience]: Concise state updates and actionable guideline memories
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Internal summaries compress the active context and external insight retrieval guides future web decisions.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 该框架将动态轨迹总结为 compact state memory，并从离线 insight bank 检索 distilled insights，以降低 context 成本并增强决策稳健性。

[Title]: APEX-EM: Non-Parametric Online Learning for Autonomous Agents via Structured Procedural-Episodic Experience Replay
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Full procedural-episodic traces with plans, artifacts, iteration histories, error analyses, and quality scores
- [Target Experience]: Dual-outcome Experience Memory with structured plans, annotations, and plan DAG traversal
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Successful experiences serve as positive in-context examples and failures as negative structured examples for analogous future tasks.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 该 PRGII loop 吸收 execution traces，附加 verifier reward signals，索引 procedural structure，并通过 semantic、structural 与 DAG similarity 检索 plans。

[Title]: Reflexion: language agents with verbal reinforcement learning
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Trial-and-error task feedback signals and prior agent episodes
- [Target Experience]: Verbal reflections stored in episodic memory
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Reflections are recalled in subsequent trials to induce improved decisions without weight updates.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 智能体将 scalar 或 language feedback 转化为 reflective text，存入 memory，并在后续动作选择时以累积 reflection 作为条件。

[Title]: Evolving Programmatic Skill Networks
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Open-ended embodied task experience and failures in skill compositions
- [Target Experience]: Programmatic Skill Network of executable symbolic programs
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: The skill network enables executable skill reuse, progressive optimization, and generalization across open-ended tasks.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 其中 REFLECT 定位 skill compositions 中的故障，maturity-aware gates 稳定更新，带 rollback validation 的结构重构把经验转为紧凑 program network。

[Title]: From Evidence to Trajectory: Abductive Reasoning Path Synthesis for Training Retrieval-Augmented Generation Agents
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: Teacher LLM abductive planning capability conditioned on supporting evidence
- [Target Experience]: Synthesized agent-environment interaction trajectories for RAG agents and an SFT-trained model
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Complete interaction trajectories are formatted as dialogue data for supervised fine-tuning of RAG agents.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P7：teacher 将 decomposition、retriever invocation 与 stepwise reasoning 外化为 evidence-grounded trajectories。阶段 2 对应 P5：合成 dialogues 用于训练 8B agent model。

[Title]: Distilling LLM Agent into Small Models with Retrieval and Code Tools
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: Teacher LLM-agent trajectories involving reasoning, retrieval, and code-tool actions
- [Target Experience]: Tool-using small language model agents
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Teacher-generated trajectories are used to distill full task-solving behavior into small models; self-consistent action generation improves robustness.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P7：teacher agents 将 reasoning 与 tool-use behavior 外化为 trajectories。阶段 2 对应 P5：small models 通过 agent distillation 内化这些轨迹。

[Title]: NNetNav: Unsupervised Learning of Browser Agents Through Environment Interaction in the Wild
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: Exploration-policy browser action sequences
- [Target Experience]: Retroactively labeled synthetic browser demonstrations and a fine-tuned browser agent
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: The labeled demonstrations are used to fine-tune Llama-3.1-8B for WebArena and WebVoyager tasks.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P7：exploration policy 生成 browser trajectories，并被 retroactive labeling 转为 demonstrations。阶段 2 对应 P5：这些 demonstrations 训练 browser-agent policy。

[Title]: TimeWarp: Evaluating Web Agents by Revisiting the Past
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: Teacher rollouts and distilled plans across multiple historical UI versions
- [Target Experience]: Multi-version web-agent trajectories and behavior-cloned agents
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}
- [Utilization]: TimeTraj uses distilled plans and rollouts to train web agents that generalize across changing UI designs.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P7：teacher rollouts 将跨 UI version 的 web navigation behavior 外化。阶段 2 对应 P5：behavior-cloning variant 将这些轨迹内化到 smaller agents。

[Title]: SKILLFOUNDRY: Building Self-Evolving Agent Skill Libraries from Heterogeneous Scientific Resources
- [Pathway]: Out of Scope
- [Mechanism]: 源端是 repositories、APIs、scripts、notebooks、documentation、databases 和 papers 等 heterogeneous scientific resources，而不是 agent decision-process experience，因此位于 Project_Infos.md §3.2 的 static-resource 边界。

[Title]: Learn-by-interact: A Data-Centric Framework for Self-Adaptive Agents in Realistic Environments
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: LLM-generated agent-environment interaction trajectories conditioned on environment documentation
- [Target Experience]: Synthetic trajectories, abstracted instructions, and adapted LLM agents
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}, {self}
- [Utilization]: The synthesized data are reused both as retrieved ICL examples and as supervised training data for downstream agents.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P7：LLM agents 基于 documentation 将特定环境行为外化为 interaction histories。阶段 2 对应 P5：这些 histories 和 backward-constructed instructions 支持模型训练；并行 P1 分支支持 ICL memory。

[Title]: Meta Context Engineering via Agentic Skill Evolution
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Prior skills, their executions, training rollouts, and evaluations
- [Target Experience]: Co-evolved context artifacts, flexible files, code, and context-engineering skills
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: The evolved skills and context artifacts optimize inference-time context across offline and online domains.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 元层 agent 搜索 skill executions 与 evaluations 的历史，修订 engineering skills，并驱动 base-level agent 从 rollout experience 产出 context files 和 code。

[Title]: LLMs as Scalable, General-Purpose Simulators For Evolving Digital Agent Training
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: LLM simulator's implicit UI-transition and rollout knowledge
- [Target Experience]: Structured UI states, transitions, synthetic trajectories, and trained digital agents
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}
- [Utilization]: UI-Simulator and UI-Simulator-Grow generate data used to train web and Android agents.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P7：simulator 将参数化 UI-world knowledge 外化为 states、transitions 与 guided trajectories。阶段 2 对应 P5：digital-agent models 内化 synthetic trajectories。

[Title]: Unifying Dynamic Tool Creation and Cross-Task Experience Sharing through Cognitive Memory Architecture
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Successful execution patterns and episodic task memories from prior agent runs
- [Target Experience]: Dynamically created tools and hierarchical procedural, semantic, and episodic memory
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: SMITH reuses episodic memories and generated tools for novel GAIA-style tasks.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 系统通过 semantic memory 检索过往 execution patterns，同时在 sandbox 中迭代生成代码，把可复用 task experience 转化为 unified memory/tool hub 下的新工具。

[Title]: FABRIC: Framework for Agent-Based Realistic Intelligence Creation
- [Pathway]: Policy → Schematic (P7)
- [Source Experience]: LLMs' implicit knowledge of tool-use dialogues, task decomposition, and execution traces
- [Target Experience]: Schema-constrained synthetic agentic records with task specifications, tool definitions, policy pseudocode, exchanges, and execution traces
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: The generated records form machine-parseable datasets for developing robust tool-using agentic LLMs.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 仅依赖 LLM 的模块化 pipeline 将参数化 agentic competence 外化为满足语法约束的 records，再用 JSON schema 和 judge-based filtering 做一致性验证。

[Title]: Mock Worlds, Real Skills: Building Small Agentic Language Models with Synthetic Tasks, Simulated Environments, and Rubric-Based Rewards
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: Strong teacher model's tool-use task design policy and simulated user/tool interactions
- [Target Experience]: Synthetic tool-use training data, mock environments, reward rubrics, and improved small LLM agents
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Models train on synthetic data and rubric-based rewards to improve math, search, and tool-use agentic capabilities.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段 1 对应 P7：teacher 创建 tasks、tool ecosystems、underspecified instructions、user simulations、tool responses 与 rubrics，形成 tokenized training environments。阶段 2 对应 P5：small models 从这些 synthetic experiences 中学习 agentic behavior。

[Title]: CASCADE: Cumulative Agentic Skill Creation through Autonomous Development and Evolution
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Agent tool-use, web-search, code-extraction, introspection, and memory-use traces in scientific tasks
- [Target Experience]: Shareable executable scientific skills
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {human}
- [Utilization]: Accumulated skills are shared across agents and scientists for computational analysis, laboratory experiments, and paper reproduction.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 该框架借助 continuous learning 与 self-reflection meta-skills，把科学任务经验和 memory 转为可执行 skills，并在后续 research workflows 中复用。

[Title]: CoEvoSkills: Self-Evolving Agent Skills via Co-Evolutionary Verification
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Skill-generation attempts, verifier feedback, and failure cases on multi-step professional tasks
- [Target Experience]: Complex multi-file skill packages
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Generated skills are used by Claude Code, Codex, and additional LLMs on SkillsBench-style tasks.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 其中 Skill Generator 迭代修订 skill artifacts，Surrogate Verifier 同步演化反馈，使 generation failures 转化为结构化 multi-file skill packages。

[Title]: SynthAgent: Adapting Web Agents with Synthetic Supervision
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: Synthetic web-exploration behavior and refined trajectory collection
- [Target Experience]: Refined synthetic web tasks, denoised trajectories, and fine-tuned web agents
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}, {self}
- [Utilization]: Refined synthetic supervision is used to fine-tune open-source web agents for target environments.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P7：synthetic exploration 与 trajectory collection 将 web-agent behavior 外化为 task/trajectory data。阶段 2 对应 P5：trajectory refinement 为 supervised adaptation 准备数据。

[Title]: Aligning Agentic World Models via Knowledgeable Experience Learning
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Environmental feedback, prediction errors, and successful embodied trajectories
- [Target Experience]: Symbolic World Knowledge Repository containing physical feasibility and task-optimality knowledge
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: Retrieved world knowledge aligns LLM planning with physical feasibility and task optimality across environments.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 来自 prediction errors 的 Process Experience 与来自 successful trajectories 的 Goal Experience 被合成为 symbolic rules，用于无 retraining 的 embodied planning。

[Title]: AutoGuide: Automated Generation and Selection of Context-Aware Guidelines for Large Language Model Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Offline experiences from unfamiliar agent domains such as web navigation
- [Target Experience]: Concise natural-language context-aware guidelines
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {human}
- [Utilization]: Guidelines are selected and supplied to the agent's current decision process instead of full demonstrations.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 离线经验被概括为 conditional natural-language rules，明确每条 guideline 的适用 context，用于替代整段 demonstration retrieval。

[Title]: Natural-Language Agent Harnesses
- [Pathway]: Out of Scope
- [Mechanism]: 摘要讨论的是 harness externalization 与 code-to-text migration 这类设计 artifact，但没有指出 source decision-process experience 如何转化为 reusable experience carrier。

[Title]: Memory Transfer Learning: How Memories are Transferred Across Domains in Coding Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Concrete coding-agent traces and lower-level memory entries from heterogeneous domains
- [Target Experience]: Abstract insights and transferable meta-knowledge such as validation routines
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Abstracted memories are reused across coding benchmarks and even across different models.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 该研究比较从 concrete traces 到 high-level insights 的 memory representations，显示 abstraction 能把 domain-specific traces 转为可迁移 meta-knowledge，而 low-level traces 可能造成 negative transfer。

[Title]: Structured Agent Distillation for Large Language Model
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: Teacher LLM-agent trajectories with interleaved reasoning and actions
- [Target Experience]: Compact student agent model aligned on reasoning and action spans
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Segmented trajectories supervise smaller agents for ALFWorld, HotPotQA-ReAct, and WebShop.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P7：teacher behavior 外化为 ReAct-style trajectories。阶段 2 对应 P5：segment-specific losses 将 reasoning 与 action consistency 内化到 student policy。

[Title]: Investigate-Consolidate-Exploit: A General Strategy for Inter-Task Agent Self-Evolution
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Planning and execution trajectories across tasks
- [Target Experience]: Simplified workflows and pipelines
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Consolidated workflows and pipelines are exploited to reduce API calls and enable weaker models to solve agent tasks.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 该策略调查任务轨迹，将重复 procedure 整合为 reusable workflows/pipelines，并在 inter-task self-evolution 中复用这些结构。

[Title]: Training-Free Group Relative Policy Optimization
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Groups of LLM-agent rollouts and their semantic relative advantages
- [Target Experience]: High-quality experiential knowledge used as a learned token prior
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: The experiential knowledge is integrated during LLM API calls to guide model behavior without parameter updates.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 该方法对 rollout groups 进行语义比较，在多轮 epoch 中蒸馏高质量 experiential knowledge，并将得到的 token prior 注入推理以模拟 GRPO 式行为改变。

[Title]: TAME: A Trustworthy Test-Time Evolution of Agent Memory with Systematic Benchmarking
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Historical feedback from benign task evolution, including task utility and safety signals
- [Target Experience]: Dual executor and evaluator memories
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Executor memory improves task performance, while evaluator memory refines safety and utility assessments during test-time evolution.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 该框架将 memory evolution 分为 executor 与 evaluator 两条轨道，执行 memory filtering、draft generation、trustworthy refinement 与任务执行，再用历史反馈更新两个 textual memory streams。

[Title]: Meta-Harness: End-to-End Optimization of Model Harnesses
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Scores and execution traces of prior harness candidates
- [Target Experience]: Optimized harness code for LLM applications
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Discovered harnesses are reused across online text classification, RAG math reasoning, and agentic coding settings.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 其中 agentic proposer 组件读取 filesystem 中的 prior source code、scores 与 traces，再搜索 harness code，使累积执行经验转化为可复用 controller artifact。

[Title]: EE-MCP: Self-Evolving MCP-GUI Agents via Automated Environment Generation and Experience Learning
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: Automatically generated MCP-GUI environments, collected trajectories, and trajectory comparisons
- [Target Experience]: Quality-filtered training trajectories, trained MCP-GUI policies, and a rule-based experience bank
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}, {self}
- [Utilization]: Distillation improves MCP-dominant tasks, while the experience bank improves GUI-intensive tasks at inference time.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段 1 对应 P7：automatic environment generation 与 trajectory collection 将 MCP-GUI behavior 外化为数据。阶段 2 对应 P5：quality-filtered trajectories 训练 policy；次要 P1 分支从 trajectory comparison 中抽取 rules 写入 experience bank。

[Title]: AlphaOPT: Formulating Optimization Programs with Self-Improving LLM Experience Library
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Failed optimization-modeling attempts and solver feedback
- [Target Experience]: Solver-verified structured insights and reusable modeling principles
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: The experience library guides future optimization formulation and code generation without parameter updates.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 库学习阶段用 solver feedback 从 failed attempts 中抽取 insights，库演化阶段基于跨任务证据修订 insight applicability 并控制库规模。

[Title]: Sub-goal Distillation: A Method to Improve Small Language Agents
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: LLM annotations of oracle interactive-task paths into sub-goal sequences
- [Target Experience]: Sub-goal-annotated data and fine-tuned planning/execution modules
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: The annotated data train a small hierarchical language agent that no longer calls the LLM at inference.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P7：LLM 通过给 oracle paths 标注 sub-goals 外化 planning knowledge。阶段 2 对应 P5：planning 与 execution modules 通过 fine-tuning 内化这些监督信号。

[Title]: RetroAgent: From Solving to Evolving via Retrospective Dual Intrinsic Feedback
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: Online LLM-agent rollouts, extrinsic rewards, hindsight reflections, and intrinsic progress feedback
- [Target Experience]: Textual memory buffer of reusable lessons and an RL-improved agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Textual experiences are retrieved by SimUtil-UCB and RL updates improve future interactive behavior.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段 1 对应 P7：current policy 生成 rollouts 与 hindsight reflections 作为显式 lessons。阶段 2 对应 P5：extrinsic 与 intrinsic feedback 驱动 online RL，检索到的 lessons 支持探索和 adaptation。

[Title]: WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Raw cross-session web navigation logs and complete trajectories
- [Target Experience]: Concise summaries, episodic memories, and task-specific advice
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: The Coach retrieves relevant experiences by similarity and recency, then injects advice through runtime hooks.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 该系统用 WebCondenser 总结 logs，用 External Memory Store 组织 trajectories，再由 Coach 决定是否将 memory advice 注入 future browsing actions。

[Title]: ArcMemo: Abstract Reasoning Composition with Lifelong LLM Memory
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Long reasoning traces produced during ARC-AGI problem solving
- [Target Experience]: Concept-level natural-language memory entries
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Relevant concepts are retrieved and integrated into prompts for later compositional reasoning queries.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 系统从 prior rollouts 中抽象 reusable modular takeaways，存为 natural-language concepts，并在 test-time reasoning 中更新和检索。

[Title]: Sample-Efficient Online Learning in LM Agents via Hindsight Trajectory Rewriting
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Failed sequential interactions and goals/subgoals that could have been achieved
- [Target Experience]: Optimized counterfactual trajectories and compressed trajectory memories
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Rewritten trajectories and compressed memories support faster adaptation in novel environments.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 该方法用 hindsight rule 从 failed attempts 中识别可达成的 alternative goals，生成 synthetic positive trajectories，并用 compressed trajectory representations 更新 memory。

[Title]: From Procedural Skills to Strategy Genes: Towards Experience-Driven Test-Time Evolution
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Prior controlled trials, failure histories, skill fragments, and freeform experience text
- [Target Experience]: Compact Strategy Gene representation with warnings and editable control structure
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Genes function as test-time control objects and as the substrate for iterative experience accumulation.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 经验与 failure history 被压缩为 structured Gene object；失败信息被蒸馏成 compact warnings，避免直接附加冗长历史导致控制信号变弱。

[Title]: Memory Intelligence Agent
- [Pathway]: Narrative → Policy → Narrative (P5 + P7)
- [Source Experience]: Compressed historical search trajectories and open-world reflection/judgment signals
- [Target Experience]: Parametric Planner memory and generated search plans
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Planner-generated search plans guide an Executor, while non-parametric memory and parametric planner updates form a bidirectional evolution loop.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段 1 对应 P5：historical search trajectories 与 cooperation feedback 通过 alternating RL 和 test-time updates 内化到 Planner。阶段 2 对应 P7：Planner 将 parametric memory 外化为 search plans 供后续执行。

[Title]: A-MEM: Agentic Memory for LLM Agents
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: New and historical agent memories from tool-using tasks
- [Target Experience]: Interconnected Zettelkasten-style memory network with notes, tags, attributes, and links
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: The memory network supports adaptive context-aware retrieval for arbitrary LLM agents.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 每条新 memory 被转化为 structured note，再与 historical memories 比较并建立相似性链接，同时触发既有 memory 的 contextual attributes 更新。

[Title]: Metacognitive Reuse: Turning Recurring LLM Reasoning Into Concise Behaviors
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Recurring reasoning fragments in prior multi-step problem-solving traces
- [Target Experience]: Behavior handbook entries consisting of a name and instruction
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Behaviors are provided in-context for future reasoning, used for self-improvement without parameter updates, or used to condition SFT traces.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 模型对 prior traces 做 metacognitive analysis，把重复推导压缩为 concise behaviors，并可把 behavior-conditioned traces 送入次要 P5 SFT 分支。

[Title]: Trajectory-Informed Memory Generation for Self-Improving Agent Systems
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Agent execution trajectories with failures, recoveries, inefficiencies, and successful strategies
- [Target Experience]: Strategy tips, recovery tips, and optimization tips with provenance
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Retrieved tips are injected into prompts based on multi-dimensional task-context similarity.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 语义轨迹分析与 decision attribution 识别哪些步骤导致失败、恢复或低效，learning generator 再把这些信号转化为贴合任务 context 的 textual guidance。

[Title]: ANCHOR: Branch-Point Data Generation for GUI Agents
- [Pathway]: Narrative → Narrative → Policy (P1 + P5)
- [Source Experience]: Verified seed GUI demonstrations and branch-point states
- [Target Experience]: Expanded GUI trajectory corpus and fine-tuned GUI agent models
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {human}, {teacher}
- [Utilization]: Expanded trajectories supervise GUI agents on OSWorld and WindowsAgentArena.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P1：seed demonstrations 被扩展为 coherent task variants，并对 post-branch trajectories 做去噪。阶段 2 对应 P5：expanded narrative trajectory corpus 被 fine-tuned GUI agents 内化。

[Title]: Co-Evolving LLM Decision and Skill Bank Agents for Long-Horizon Tasks
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Unlabeled long-horizon game rollouts from an LLM decision agent
- [Target Experience]: Learnable skill bank with reusable skills and contracts
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: The decision agent retrieves skill-bank entries to guide action generation across long-horizon tasks.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 技能库 agent 从 rollouts 中发现、修订并更新 skills；决策 agent 通过 skill retrieval 改进 action generation。

[Title]: ExpeL: LLM Agents Are Experiential Learners
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Experiences autonomously gathered from training decision-making tasks
- [Target Experience]: Natural-language insights and retained past experiences
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: At inference, the agent recalls extracted insights and past experiences to make task decisions.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 该方法收集任务经验，抽取 reusable natural-language knowledge，并累积为后续决策可调用的 memory，无需参数更新。

[Title]: The World Leaks the Future: Harness Evolution for Future Prediction Agents
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Temporal contrasts between earlier and later predictions plus final outcome checks
- [Target Experience]: Persistent future-prediction harness for factor tracking, evidence gathering, interpretation, and uncertainty handling
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Updated harness guidance improves later predictions on the same unresolved question and is carried forward after outcome resolution.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 该系统从同一 unresolved question 的多次预测中抽取 internal feedback，将 reusable guidance 写入 harness，并用 final outcome 做 retrospective check 后再迁移。

[Title]: Towards Autonomous Memory Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Self signals, teacher signals, tool-verified research, and occasional expert feedback gathered by a memory agent
- [Target Experience]: Validated and curated memory entries
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}, {human}
- [Utilization]: U-Mem retrieves and explores memories under a Thompson-sampling policy to improve verifiable and non-verifiable tasks.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 成本感知的 extraction cascade 在不确定性较高时逐级升级证据来源，semantic-aware sampling 在 memory exploration 与 exploitation 之间做权衡。

[Title]: OS-Copilot: Towards Generalist Computer Agents with Self-Improvement
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Prior computer-control task executions across OS, web, terminal, files, multimedia, and applications
- [Target Experience]: Accumulated skills for FRIDAY
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Learned skills improve control of unseen applications and general computer tasks.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 该系统让 FRIDAY 积累 task-specific control experience，并将其转化为可在后续 Excel、PowerPoint 和通用 OS 任务中复用的 skills。

[Title]: ICAL: Continual Learning of Multimodal Agents by Transforming Trajectories into Actionable Insights
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Noisy multimodal demonstrations, sub-optimal trajectories, and human feedback
- [Target Experience]: General programs annotated with cognitive abstractions such as task relationships, object-state changes, temporal subgoals, and task construals
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {human}, {self}
- [Utilization]: The abstractions are used as prompt exemplars for retrieval-augmented LLM/VLM agents and can support additional fine-tuning.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 视觉语言模型修复低效动作，将轨迹抽象为 program-like exemplars，并在相似环境中尝试执行时通过 human feedback 继续细化这些 abstractions。

[Title]: Agent Planning with World Knowledge Model
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Expert and sampled interactive-planning trajectories
- [Target Experience]: Parametric World Knowledge Model that supplies prior task knowledge and dynamic state knowledge
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {human}, {self}
- [Utilization]: The trained WKM guides global planning and local planning for LLM agents in simulated real-world tasks.
- [Method]: ⟨SFT⟩
- [Mechanism]: 由轨迹派生的 world knowledge 被合成并内化到 parametric model；虽然 WKM 是规划支持模块而非 actor 本身，摘要明确把它置于 LLM-agent planning loop 中。

[Title]: Training LLM Agents for Spontaneous, Reward-Free Self-Evolution via World Knowledge Exploration
- [Pathway]: Narrative → Policy → Narrative (P5 + P7)
- [Source Experience]: Self-generated world knowledge and outcome-based reward during training
- [Target Experience]: Intrinsic meta-evolution policy that generates world knowledge at inference
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: At inference, the trained agent spontaneously summarizes unseen environments and adapts without external rewards.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段 1 对应 P5：reward signals 教会模型如何探索并总结 world knowledge。阶段 2 对应 P7：训练后的 policy 在新环境中把这种能力外化为 tokenized world knowledge。

[Title]: View-oriented Conversation Compiler for Agent Trace Analysis
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Raw agent JSONL logs with nested tool calls, results, reasoning blocks, sub-agent invocations, compaction boundaries, and harness directives
- [Target Experience]: Structured full, UI, and adaptive trace views
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: VCC-compiled views feed reflectors or context-engineering mechanisms, improving pass rates and lowering token consumption.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 编译器解析 raw agent traces，生成 lossless 与 relevance-projected structured views，使下游 reflector 接收组织化经验而不是 raw logs。

[Title]: PlugMem: A Task-Agnostic Plugin Memory Module for LLM Agents
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Episodic memories from heterogeneous LLM-agent tasks
- [Target Experience]: Knowledge-centric memory graph with propositional and prescriptive knowledge units
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: The graph memory is attached unchanged to arbitrary agents for efficient retrieval and reasoning.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 原始 episodic memories 被转化为 abstract knowledge units，再组织成 graph，并按 task-relevant knowledge 检索，避免直接使用冗长 trajectory chunks。

[Title]: SkillCraft: Can LLM Agents Learn to Use Tools Skillfully?
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Tool-use episodes where agents compose atomic tools during long-horizon workflows
- [Target Experience]: Executable Skills formed by higher-level tool compositions
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Skills are cached and reused inside and across tasks to reduce token usage and improve efficiency.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 评测协议让 agent 抽象 recurring atomic tool sequences 为 executable skills，持久化这些 skills，并在 compositional tool-use 任务中复用。

[Title]: WorkflowGen:an adaptive workflow generation mechanism driven by trajectory experience
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Full execution trajectories with node-level and workflow-level signals, error fingerprints, tool mappings, parameter schemas, execution paths, and exception-avoidance strategies
- [Target Experience]: Reusable workflow templates and modular traceable experience records
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Adaptive routing selects direct reuse, trajectory rewriting, or full initialization for new workflow queries.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 该框架捕获早期 trajectories，抽取 node/workflow 级可复用知识，归纳 templates，并在 closed loop 中更新经验，使后续 workflows 尽量只重写 variable nodes。

[Title]: GUI-ReWalk: Massive Data Generation for GUI Agent via Stochastic Exploration and Intent-Aware Reasoning
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: GUI exploration policy behavior combining stochastic exploration and reasoning-guided interaction
- [Target Experience]: Realistic diverse GUI trajectories and a trained Qwen2.5-VL GUI agent
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Synthesized GUI trajectories are used to train and evaluate GUI agents across desktop and mobile benchmarks.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P7：exploration 与 intent-aware reasoning 将 GUI action behavior 外化为 long-horizon trajectories。阶段 2 对应 P5：GUI-ReWalk dataset 训练 VLM-based GUI policy。

[Title]: AutoHarness: improving LLM agents by automatically synthesizing a code harness
- [Pathway]: Policy → Schematic (P7)
- [Source Experience]: Gemini agent's parametric game-playing and code-synthesis capability plus environment feedback from iterative refinement
- [Target Experience]: Custom code harnesses and, in some cases, entire code policies
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Generated harnesses prevent illegal moves or replace LLM decision making with executable code policies.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 模型利用 game environment feedback 将 control policy 外化为 code artifacts，并迭代修订 harness，直到 illegal actions 被阻断。

[Title]: REVERE: Reflective Evolving Research Engineer for Scientific Workflows
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Cross-repository execution trajectories and recurring failure modes in research-coding workflows
- [Target Experience]: Reusable heuristics and targeted edits to system prompt, task-prompt template, and cumulative cheatsheet
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Updated prompts and cheatsheets guide future research-coding executions across benchmarks.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 该框架识别跨任务的 recurring failure patterns，将其蒸馏为 heuristics，并对 system prompt、task-prompt template 和 cumulative cheatsheet 做定向编辑。

[Title]: Towards Reliable Generation of Executable Workflows by Foundation Models
- [Pathway]: Out of Scope
- [Mechanism]: 论文关注从 natural-language requirements 生成并修复 DSL workflows，并使用 static-analysis feedback；摘要没有把源端锚定为累积的 agent decision-process experience。

[Title]: UMEM: Unified Memory Extraction and Management Framework for Generalizable Memory
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Agent interaction experiences clustered into semantic neighborhoods with downstream utility feedback
- [Target Experience]: Generalizable memory bank and an optimized memory extraction/management behavior
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Extracted memories are managed to support continuous multi-turn agent evolution while avoiding instance-specific noise.
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 该框架用 neighborhood-level marginal utility rewards 联合训练 memory extractor/manager，使经验转化为能跨 semantically related queries 泛化的 memories。

[Title]: ELITE: Experiential Learning and Intent-Aware Transfer for Self-improving Embodied Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Embodied execution trajectories and self-reflective interaction experience
- [Target Experience]: Reusable strategies in an evolving strategy pool
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: Intent-aware retrieval applies relevant strategies to procedurally similar embodied tasks.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 自反式知识构建从 execution trajectories 中抽取 strategies，持续精炼 strategy pool，再按 intent 检索相关策略用于迁移。

[Title]: Compiling Deterministic Structure into SLM Harnesses
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Teacher critiques, SLM workflow traces, and per-node reliability failures
- [Target Experience]: Deterministic execution plans, DAG topologies, prompts, and code-placement decisions
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}, {self}
- [Utilization]: Compiled harnesses route unreliable subtasks to deterministic code or consensus structures, improving SLM reasoning reliability.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 语义梯度下降将 teacher 的 natural-language critiques 作为方向性信号，修订 discrete workflow artifacts，并编译 trace-driven deterministic structure。

[Title]: From Experience to Strategy: Empowering LLM Agents with Trainable Graph Memory
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Raw agent trajectories and downstream reward feedback
- [Target Experience]: Multi-layer graph memory with structured decision paths and strategic meta-cognition
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Optimized strategies are dynamically integrated into the LLM agent's training loop through meta-cognitive prompting.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 原始轨迹被抽象成 state-machine decision paths 与 high-level strategies；reinforcement-based utility optimization 对 prompt 中使用的 meta-cognition 赋权。

[Title]: EchoTrail-GUI: Building Actionable Memory for GUI Agents via Critic-Guided Self-Exploration
- [Pathway]: Policy → Narrative (P7)
- [Source Experience]: GUI agent self-exploration policy validated by a reward model
- [Target Experience]: Curated database of successful GUI task trajectories
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Retrieved successful trajectories are injected as in-context actionable memories for later GUI task inference.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 智能体通过 self-exploration 将 GUI-control policy 外化为 successful trajectories，再由 critic/reward model 过滤，并存为可复用 memory。

[Title]: AgentSynth: Scalable Task Generation for Generalist Computer-Use Agents
- [Pathway]: Policy → Narrative (P7)
- [Source Experience]: LLM generator's implicit knowledge of subtasks and long-horizon computer-use task composition
- [Target Experience]: Synthetic computer-use tasks and trajectory datasets
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}
- [Utilization]: Generated tasks and trajectories provide low-cost data for evaluating and training generalist computer-use agents.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 该系统将参数中的 task-composition knowledge 外化为易生成的 subtasks，再把这些 subtasks 组合成长程 computer-use trajectories。

[Title]: AutoSkill: Experience-Driven Lifelong Learning via Skill Self-Evolution
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: User dialogue and interaction traces reflecting stable preferences and requirements
- [Target Experience]: Standardized reusable, composable skill representations
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: Relevant skills are dynamically injected into future requests without retraining the underlying model.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 该框架将反复出现的个性化 interaction experience 抽象为可维护 skill artifacts，使其能演化、迁移，并在 agents、users 和 tasks 间共享。

[Title]: Unlocking Implicit Experience: Synthesizing Tool-Use Trajectories from Text
- [Pathway]: Narrative → Schematic → Narrative
- [Source Experience]: Textual corpora containing multi-step problem-solving experiences
- [Target Experience]: Multi-turn tool-use trajectories and an SFT-trained Trajectory Synthesizer
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}, {teacher}
- [Utilization]: Generated trajectories train tool-use agents, while the Trajectory Synthesizer replaces the full generation pipeline at lower cost.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段 1 对应 P2：text 被过滤并转化为 workflow/tool structure。阶段 2 将这些结构 grounding 并 refine 成 multi-turn tool-use trajectories；该 Schematic → Narrative 扩展属于 tokenized-to-tokenized synthesis，不在七条基础路径内。

[Title]: Fara-7B: An Efficient Agentic Model for Computer Use
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: Synthetic data generator behavior for multi-step web tasks with multiple solution attempts and verifiers
- [Target Experience]: Verified screenshot-coordinate web trajectories and the trained Fara-7B CUA policy
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}
- [Utilization]: Verified trajectories train a compact computer-use agent that perceives screenshots and predicts coordinates.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P7：FaraGen 将 task proposal 与 action policy 外化为 verified web trajectories。阶段 2 对应 P5：Fara-7B 通过 supervised training 内化这些轨迹。

[Title]: ToolMind Technical Report: A Large-Scale, Reasoning-Enhanced Tool-Use Dataset
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: Multi-agent simulated user-assistant-tool interactions over a function graph
- [Target Experience]: Large-scale high-quality tool-agentic dataset and fine-tuned tool-use models
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Fine-grained filtered reasoning traces are used to train models for robust tool-use benchmarks.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P7：multi-agent simulation 将 tool-use reasoning 外化为 interaction traces。阶段 2 对应 P5：models 通过 fine-tuning 内化 turn-level-filtered traces。

[Title]: TED: Training-Free Experience Distillation for Multimodal Reasoning
- [Pathway]: Policy → Narrative (P7)
- [Source Experience]: Teacher model reasoning compared against student multimodal reasoning trajectories and ground-truth answers
- [Target Experience]: Generalized in-context experiences capturing effective reasoning patterns
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {teacher}, {self}
- [Utilization]: Refined experiences are injected into the student's prompt to improve multimodal reasoning without parameter updates.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 教师模型通过比较 student trajectories、自身解法和 ground-truth answer，外化有效 reasoning patterns，并按 usage statistics 压缩这些 experiences。

[Title]: ASDA: Automated Skill Distillation and Adaptation for Financial Reasoning
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Student model failures on financial reasoning tasks and teacher error analysis
- [Target Experience]: Skill files containing reasoning procedures, code templates, and worked examples
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Skill files are dynamically injected during inference for financial reasoning adaptation without weight updates.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 教师模型按 subfield 与 error type 聚类 student failures，再合成包含 procedures、templates 和 examples 的 structured skill artifacts。

[Title]: Controllable and Verifiable Tool-Use Data Synthesis for Agentic Reinforcement Learning
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: Self-evolving synthetic tool-use trajectory generation and oracle-preserving environment augmentations
- [Target Experience]: Reward-checkable online rollout environments and RL-improved tool-calling policies
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Generated trajectories and verifiable environments support RL refinement of tool-calling policies.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段 1 对应 P7：pipeline 将 tool-use behavior 外化为可靠 base trajectories 和更难的 augmented environments。阶段 2 对应 P5：online RL 使用这些 tokenized experiences 上的自动 rewards 改进 policy。

[Title]: ASTRA: Automated Synthesis of agentic Trajectories and Reinforcement Arenas
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: Automated tool-augmented trajectory synthesis and environment synthesis from semantic reasoning traces
- [Target Experience]: Structurally grounded trajectories, code-executable RL arenas, and trained tool-augmented agents
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: The synthesized data and arenas support a unified SFT plus online RL training methodology.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段 1 对应 P7：tool-call topology 与 semantic reasoning 被外化为 trajectories 和 rule-verifiable environments。阶段 2 对应 P5：SFT 与 online RL 将这些 experiences 内化为 agent policies。

[Title]: Embodied CoT Distillation From LLM To Off-the-shelf Agents
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: LLM embodied in-context learning and self-verification traces
- [Target Experience]: Embodied rationales and distilled reasoning/planning policies for small models
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}
- [Utilization]: Distilled policies run on off-the-shelf devices for embodied decision making.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P7：LLM 将 embodied reasoning 外化为 rationales 与 planning data。阶段 2 对应 P5：small reasoning/planning policies 内化这些 tokenized rationales。

[Title]: Scalable Data Synthesis for Computer Use Agents with Step-Level Filtering
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: Noisy rollouts from a strong computer-use-preview model and step-level grading signals
- [Target Experience]: WebSTAR trajectories, WebSCORE graded steps, trained CUA policy, and StepRM process reward model
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}
- [Utilization]: WebSTAR trains CUA policies; WebSCORE trains StepRM for scalable process-level action grading.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P7：strong CUA rollouts 被过滤为 reliable reasoning-rich steps。阶段 2 对应 P5：Qwen-VL CUAs 内化过滤后的轨迹；次要 P4 分支用 graded steps 训练 StepRM。

[Title]: Symbiotic Cooperation for Web Agents: Harnessing Complementary Strengths of Large and Small LLMs
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: Large-LLM web trajectories and divergent small-LLM exploration trajectories
- [Target Experience]: Iteratively enriched synthetic data and improved large/small web-agent policies
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}, {self}
- [Utilization]: Data are reused for distilling small agents and improving large-agent trajectory synthesis in a coupled loop.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段 1 对应 P7：large 与 small agents 将互补 web behaviors 外化为 trajectories。阶段 2 对应 P5：distillation 与 multi-task learning 将 enriched data 内化为更强 web-agent policies。

[Title]: EvoSkill: Automated Skill Discovery for Multi-Agent Systems
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Execution failures from coding-agent tasks
- [Target Experience]: Structured reusable skill folders with workflows and code
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Skills are selected by held-out validation and transferred to related tasks and agents.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 该框架分析 failures，提出新 skills 或编辑既有 skills，将其 materialize 为 structured folders，并只保留在 held-out validation 上有效的 skills。

[Title]: WebWorld: A Large-Scale World Model for Web Agent Training
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: WebWorld parametric simulator trained from open-web interactions
- [Target Experience]: WebWorld-synthesized web trajectories and a trained Qwen web agent
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {teacher}
- [Utilization]: Synthesized trajectories train web agents; the simulator also supports inference-time search as a world model.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P7：trained simulator 将 web dynamics 与 agent behavior 外化为 long-horizon trajectories。阶段 2 对应 P5：Qwen3-14B 内化这些轨迹以提升 WebArena 表现。

[Title]: Scaling Web Agent Training through Automatic Data Generation and Fine-grained Evaluation
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: Automatically generated web-agent trajectories and fine-grained progress evaluations
- [Target Experience]: High-quality training data, partially successful trajectory segments, and a distilled student model
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}, {self}
- [Utilization]: Fine-grained evaluated trajectories train a smaller web-agent student for BookingArena-style tasks.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P7：automatic generation 将 web interaction behavior 外化为 trajectories。阶段 2 对应 P5：constraint-based evaluation 选择可用监督，包括 partially successful trajectories，用于 student distillation。

[Title]: OpenMobile: Building Open Mobile Agents with Task and Trajectory Synthesis
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: Exploration-derived environment memory and learner/expert rollout policies
- [Target Experience]: Grounded mobile instructions, synthetic trajectories, and fine-tuned mobile agents
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {teacher}
- [Utilization]: The released data train Qwen2.5-VL and Qwen3-VL mobile agents and support open mobile-agent research.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P7：environment exploration 与 policy switching 将 mobile task behavior 外化为 instructions 和 trajectories。阶段 2 对应 P5：trained mobile agents 内化这些 synthetic supervision。

[Title]: Learning with Challenges: Adaptive Difficulty-Aware Data Generation for Mobile GUI Agent Training
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: Agent capability profile over prior GUI tasks and multi-agent generated mobile trajectories
- [Target Experience]: Capability-aligned mobile GUI trajectory data and trained GUI agents
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}, {self}
- [Utilization]: Generated trajectories are sampled at suitable difficulty and used for mobile GUI-agent training.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P7：generator 根据 agent capability frontier 外化 tasks 与 trajectories。阶段 2 对应 P5：GUI agents 在 difficulty-aligned trajectories 上训练。

[Title]: Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Complete computer-control demonstrations with states and actions
- [Target Experience]: Abstracted trajectory exemplars stored in exemplar memory
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {human}
- [Utilization]: Similar exemplars are retrieved into prompts to guide long-horizon computer-control tasks.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 该方法过滤 task-irrelevant state details，存储 complete trajectories 作为 exemplars，并按 similarity 检索，使内容仍保持 tokenized 形式但更紧凑可复用。

[Title]: SAGER: Self-Evolving User Policy Skills for Recommendation Agent
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Recommendation failures, accepted items, unchosen items, and per-user interaction history
- [Target Experience]: Dedicated per-user policy skill document with rich evolution substrate and minimal inference-time injection
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: The evolved skill augments listwise reasoning and personalizes the agent's decision process beyond semantic memory.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 该框架对比 accepted 与 unchosen items 来诊断 reasoning flaws，并更新结构化 natural-language policy skill，以编码 personalized decision principles。

[Title]: Learning to Share: Selective Memory for Efficient Parallel Agentic Systems
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Intermediate steps from parallel agent teams and usage-aware credit signals
- [Target Experience]: Learned memory-admission controller for a global shared memory bank
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: The controller decides which intermediate steps should be shared globally to reduce redundant parallel computation.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 分步 RL 结合 usage-aware credit assignment，把哪些 agent steps 对跨团队共享有用这一经验内化为 memory-admission policy。

[Title]: SkillGraph: Self-Evolving Multi-Agent Collaboration with Multimodal Graph Topology
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Visual multi-agent failure cases and reasoning traces
- [Target Experience]: Multimodal Skill Bank of refined reasoning heuristics and adaptive collaboration topology inputs
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {self}
- [Utilization]: Skill embeddings feed the Multimodal Graph Transformer so collaboration graphs adapt with capability growth.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 该框架中的 Skill Designer 从 failure cases 中蒸馏 skill-bank heuristics；更新后的 skill embeddings 再供 MMGT 预测 query-conditioned collaboration topology。

[Title]: AdaExplore: Failure-Driven Adaptation and Diversity-Preserving Search for Efficient Kernel Generation
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Execution feedback from Triton kernel code-generation attempts and recurring failures
- [Target Experience]: Reusable validity rules and candidate-kernel search tree
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Validity rules constrain later generations, while the candidate tree supports local refinement and structural regeneration.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 适应阶段将 recurring failures 转为定义 feasible code regions 的 rules，搜索阶段将 candidate kernels 组织为 tree 以支持更大范围优化。

[Title]: MetaClaw: Just Talk -- An Agent That Meta-Learns and Evolves in the Wild
- [Pathway]: Narrative → Schematic → Policy (P2 + P5)
- [Source Experience]: Failure trajectories and deployed workload traces across OpenClaw channels
- [Target Experience]: Reusable behavioral skill library and LoRA/RL-PRM-optimized base policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Skills provide immediate zero-downtime adaptation; policy optimization runs during inactive windows and generates better future skill-synthesis trajectories.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段 1 对应 P2：LLM evolver 分析 failures 并合成 new skills。阶段 2 对应 P5/P6：cloud LoRA fine-tuning 与带 process reward model 的 RL 更新 base policy，使 skills 与 policy 构成互相增强的循环。

[Title]: APIGen-MT: Agentic Pipeline for Multi-Turn Data Generation via Simulated Agent-Human Interplay
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: LLM-reviewer committee and simulated agent-human interplay
- [Target Experience]: Task blueprints, complete multi-turn interaction trajectories, and trained xLAM-2-fc-r models
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Generated trajectories train function-calling models and are released as a synthetic multi-turn dataset.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P7：LLM reviewers 与 simulators 将 multi-turn function-calling behavior 外化为 blueprints 和 trajectories。阶段 2 对应 P5：xLAM models 内化这些 trajectories。

[Title]: ToolAlpaca: Generalized Tool Learning for Language Models with 3000 Simulated Cases
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: Multi-agent simulation of tool-use cases over real-world APIs
- [Target Experience]: Diversified tool-use corpus and fine-tuned ToolAlpaca models
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: The corpus trains compact language models for generalized unseen-tool use.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P7：simulation 将 tool-use behavior 外化为数千个 tool-use instances。阶段 2 对应 P5：compact LMs 通过 fine-tuning 内化这些 instances。

[Title]: APIGen: Automated Pipeline for Generating Verifiable and Diverse Function-Calling Datasets
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: LLM-based function-calling generation conditioned on executable API specifications
- [Target Experience]: Verifiable function-calling dataset and trained function-calling models
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Curated entries train 1B/7B function-calling models and are released as a dataset.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P7：generation pipeline 将 function-calling behavior 外化为 executable 且 semantically verified 的 records。阶段 2 对应 P5：models 内化这些 tokenized function-calling experiences。

[Title]: ToolACE: Winning the Points of LLM Function Calling
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: Multi-agent synthetic dialogues guided by formalized tool-use thinking and self-evolved API pools
- [Target Experience]: Accurate complex tool-learning data and trained function-calling models
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Synthesized data train 8B models that perform strongly on function-calling leaderboards.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P7：multi-agent interplay 将 tool-use reasoning 与 calls 外化为 verified dialogues。阶段 2 对应 P5：生成数据被 function-calling policies 内化。

[Title]: Large Language Model as a Policy Teacher for Training Reinforcement Learning Agents
- [Pathway]: Out of Scope
- [Mechanism]: 目标是面向 MiniGrid/Habitat 的 smaller specialized traditional RL agent，不是 LLM-based agent，因此落入 Project_Infos.md §3.2 的 non-LLM-based system 边界。

[Title]: Policy Improvement using Language Feedback Models
- [Pathway]: Narrative → Evaluator → Policy (P4 + P6)
- [Source Experience]: Visual trajectories verbalized into language and LLM feedback on desirable behavior
- [Target Experience]: Language Feedback Model and improved imitation-learning policy
- [Source Modality]: [vis+txt]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}
- [Utilization]: The LFM identifies desirable behavior to imitate and can provide human-interpretable feedback for verification.
- [Method]: ⟨hybrid⟩
- [Mechanism]: 阶段 1 对应 P4：LLM 对 verbalized trajectories 的反馈训练 evaluator-like LFM。阶段 2 对应 P6：LFM 选择可模仿行为，作为改进 downstream policy 的反馈信号。

[Title]: Policy Learning with a Language Bottleneck
- [Pathway]: Out of Scope
- [Mechanism]: 摘要把 learned agents 表述为 self-driving、game-playing、robot policies 等 general AI systems，而不是 LLM-based agents；更接近 Project_Infos.md §3.2 下带 language guidance 的 traditional policy learning。

[Title]: AgentTuning: Enabling Generalized Agent Abilities for LLMs
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: AgentInstruct interaction trajectories for planning, memory, and tool use
- [Target Experience]: AgentLM policy weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}, {teacher}
- [Utilization]: The tuned Llama 2 models gain generalized agent capabilities on unseen agent tasks.
- [Method]: ⟨SFT⟩
- [Mechanism]: 高质量 interaction trajectories 与通用 instruction 数据混合，通过 hybrid instruction tuning 内化到模型权重中，增强 LLM agentic policy 并保留一般能力。

[Title]: GuardAgent: Safeguard LLM Agents by a Guard Agent via Knowledge-Enabled Reasoning
- [Pathway]: Out of Scope
- [Mechanism]: 主转化是 user guard requests 到 plans 与 executable guardrail code；尽管用到了 retrieved demonstrations，摘要没有把源端锚定为累积 agent experience。

[Title]: MobileGPT: Augmenting LLM with Human-like App Memory for Mobile Task Automation
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Mobile app exploration and task procedure interactions
- [Target Experience]: Modular sub-task procedures stored in human-like app memory
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {human}
- [Utilization]: Learned procedures are recalled, reused, rearranged, and adapted for different mobile task objectives.
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 该系统探索 apps，选择可复用 procedure，派生 modular sub-tasks，并在后续任务中 recall 这些 procedure，以避免重复完整 LLM reasoning。

[Title]: Distilling Script Knowledge from Large Language Models for Constrained Language Planning
- [Pathway]: Policy → Narrative → Policy (P7 + P5)
- [Source Experience]: LLMs' implicit script-planning knowledge for constrained goals
- [Target Experience]: Coscript dataset of goal-oriented scripts and smaller LMs with constrained planning ability
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: Distilled scripts train smaller LMs to perform constrained language planning with better constraint faithfulness.
- [Method]: ⟨SFT⟩
- [Mechanism]: 阶段 1 对应 P7：large LMs 通过 over-generate-then-filter 外化 constrained scripts，把 planning knowledge 写入 tokenized script data。阶段 2 对应 P5：smaller LMs 内化这些 scripts 以获得 constrained planning ability。
