

# Tokenized-to-Tokenized Transformations

本部分的Paper，在分类的时候：
- 没有按照产物来分。因为，即使是同一个名词，在不同论文中，其指代的含义是不一样的
- 没有按照提取方式来分。一篇论文会包含多种提取方式。很多操作方式的边界难以界定。


## Narrative → Narrative


### Single-Trajectory Extraction
- 核心特点：基于单个 session 轨迹来提取 token-level 的经验。一个 session 可以有多轮的action。给定一条交互轨迹，LLM 可以从中提取出不同类型的经验：知道哪里错了，下次该怎么做的纠错型经验；具有条件结构的指导型经验；降低上下文占用的压缩型经验；

- 核心特点
- 代表工作：
  - Reflexion：读取一条 episode 的 trajectory + feedback signal（标量或自由文本），LLM 生成一条 verbal reflection 存入 episodic buffer。
  - CLIN：每次 trial 后，从单条交互轨迹中更新因果抽象记忆（而非通用"helpful hints"）。
  - ReAP：从单个 web navigation trajectory（成功或失败）中生成 self-reflection
  - REFLECT：从单次机器人失败的多传感器观测（多模态数据），生成该次执行对应的分层摘要，然后再用 LLM 去做失败解释与纠错计划。
  - R2D2：Remember paradigm 重建 web 环境减少导航错误；Reflect paradigm 从错误中学习改进策略
  - Darwinian Memory: 将复杂轨迹分解为独立可复用单元，实施 Utility-driven Natural Selection 追踪每个单元的 survival value，主动修剪次优路径并抑制高风险计划；通过进化压力促使 agent 衍生出更优策略。
  - Sample-Efficient Online Learning：ECHO 借鉴 RL 中的 hindsight experience replay：hindsight rule 用 LLM 识别失败尝试中可达到的替代子目标，生成优化轨迹（将失败转化为合成正例）；update rule 维持压缩轨迹表示存于 memory。
  - M2: 双层记忆：Dynamic Trajectory Summarization (Internal Memory) 将冗长交互历史压缩为简洁状态更新 (P1 压缩)；Insight Retrieval Augmentation (External Memory) 从离线 insight bank 检索可操作指南注入 agent 
  - MemOrb: 将多轮交互蒸馏为紧凑的策略反思（strategy reflections），存入共享记忆库；通过检索这些反思指导 agent 决策。
  - Learning on the Job: MUSE 在每次 sub-task 执行后自主反思轨迹，将原始轨迹转化为结构化经验并整合回分层 Memory Module。
  - Procedural Knowledge at Scale Improves Reasoning：将已有的大规模分步推理轨迹分解为 self-contained subquestion-subroutine pairs（3200万条），每条是紧凑的程序性知识（"如何重述问题、选择方法、在需要时验证或回溯"）
  - MobileGPT:模拟人类与移动 app 交互的认知过程（explore→select→derive→recall），将任务过程分解为更小的模块化子任务；子任务具有结构性、可复用、可重排和可适配特征。
  - WebCoach：三个组件：WebCondenser 将原始导航日志标准化为简洁摘要 (P1 抽象)；External Memory Store 以 episodic experiences 形式组织完整轨迹；Coach 检索相关经验并决定是否注入建议。
  - Learning from Online Videos at Inference Time for Computer-Use Agents:VLM 推断 UI actions，将视频分割为 action 短子序列并分配 textual objective；两阶段选择机制在推理时每步动态选择最相关的 trajectory 片段注入。源经验来自人类视频教程，跨模态转化后以 Narrative 形式指导 agent。
  


- Reflexion: language agents with verbal reinforcement learning
- CLIN: A Continually Learning Language Agent for Rapid Task Adaptation and Generalization
- Reflection-Based Memory For Web navigation Agents
- REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction
- R2D2: Remembering, Replaying and Dynamic Decision Making with a Reflective Agentic Memory
- Darwinian Memory: A Training-Free Self-Regulating Memory System for GUI Agent Evolution
- Sample-Efficient Online Learning in LM Agents via Hindsight Trajectory Rewriting
- M2: Dual-Memory Augmentation for Long-Horizon Web Agents via Trajectory Summarization and Insight Retrieval
- MemOrb: A Plug-and-Play Verbal-Reinforcement Memory Layer for E-Commerce Customer Service
- Learning on the Job: An Experience-Driven Self-Evolving Agent for Long-Horizon Tasks
- Procedural Knowledge at Scale Improves Reasoning
- MobileGPT: Augmenting LLM with Human-like App Memory for Mobile Task Automation
- WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance
- Learning from Online Videos at Inference Time for Computer-Use Agents








### Cross-Trajectory Induction

- Remember Me, Refine Me:三个机制构成记忆全生命周期：1) multi-faceted distillation 从轨迹中提取成功模式、失败触发因素和比较性见解（对比成功和失败）；2) context-adaptive reuse 通过场景感知索引将历史 insights 适配到新上下文；3) utility-based refinement 自动添加有效记忆、修剪过时记忆，维持紧凑高质量经验池。
- AutoGuide：从离线经验中自动提取 context-aware guidelines，每条 guideline 以简洁自然语言表达并遵循条件结构（明确描述适用上下文）；每条 guideline 主要是从“同一任务的一对对比轨迹”提取的（期望回报更高和更差的对比）。先找出两条轨迹开始分叉（偏离）的那个时间步，然后把分叉之前共享的部分用 context identification 模块总结成一个“context”，再用 guideline extraction 模块产出对应这个 context 的条件式指导。虽然单条 guideline 来自一对对比轨迹，但最终会把来自数据集中大量不同对比轨迹对提取出来的 guideline，按 context 去聚合到一个字典里。
- Trace2Skill:不使用 sequential single-trajectory 方法，而是调度并行 sub-agent fleet 分析多样化执行池；各 sub-agent 提取 trajectory-specific lessons，通过归纳推理层级整合为统一的、无冲突的 skill directory。
- Skill Set Optimization: 从交互轨迹中提取具有高 reward 的常见 subtrajectory，生成为每个 skill 的 subgoal 和 instruction；将 skills 以 in-context 方式提供 LLM actor 以强化高 reward 行为；通过 pruning 持续精炼 skill set。
- Contextual Experience Replay：在推理时累积并合成过去经验为动态记忆缓冲区，经验涵盖环境动态和常见决策模式；agent 在新任务中检索相关知识进行自我增强。
- ExpeL:Agent 自主从训练任务集中收集经验，用自然语言提取知识（不涉及参数更新）；推理时同时召回提取的 insights 和原始 past experiences。
- AutoSkill：从对话和交互轨迹中自动抽象用户偏好和需求为技能，支持持续自我进化；
- GUI-explorer: Function-aware Task Goal Generator 通过分析 GUI structural information 自动构建探索目标以收集多样化轨迹；Transition-aware Knowledge Extractor 通过无监督分析结构化交互三元组 (observation, action, outcome) 的状态转移提取精确 screen-operation logic。knowledge 以 rules/logic 形式存在
- SkillClaw: 持续聚合多用户使用中产生的交互轨迹，autonomous evolver 识别重复行为模式并将其转化为 skill 更新（refining existing skills 或 extending with new capabilities）。核心贡献在跨用户经验聚合和集体进化机制。
- SWE-Exp: 从先前的 agent 修复轨迹中（成功和失败均采集）蒸馏简洁可操作的 issue resolution knowledge；多层次覆盖从 high-level problem comprehension 到 specific code changes。
- Coarse-to-Fine：粗到细三级记忆：coarse-grained focus points 指导训练任务中的经验收集 → hybrid-grained actionable tips 从每次经验中 extract → 推理时遇到异常做 fine-grained key information grounding 实现灵活 self-QA reflection 和计划修正
- Mistake Notebook Learning:不存储原始实例级经验或仅检索成功轨迹，而是从 batch-clustered failures 中提取共享错误模式形成结构化 "mistake notes"；仅在 batch 性能提升时更新外部记忆以确保稳定性。将失败经验转化为可泛化指导。
- Get Experience from Practice: 经典的 record-and-replay 范式引入 AI agent：记录 agent 与环境交互轨迹及内部决策过程 → 摘要为结构化"经验"封装工作流和约束 → 在后续类似任务中重放。
- H2R: Hierarchical Hindsight Reflection 将过去交互按层次解耦蒸馏为高层规划记忆和低层执行记忆；测试时分层检索。核心创新在记忆的分层解耦组织。
- Reflection-Based Memory For Web navigation Agents：ReAP 利用 self-reflections 同时从成功和失败经验中学习；reflections 作为额外上下文注入后续任务。
- Self-Generated In-Context Examples Improve LLM Agents for Sequential Decision-Making Tasks:Agent 从自身成功经验自动改进：积累成功轨迹为 in-context example database；population-based training 做 database-level curation 传播高质量 example 集合；exemplar-level curation 基于经验效用选择性保留轨迹。
- Mirage-1: HMS 将轨迹逐层抽象为 execution skills → core skills → meta-skills 三层知识结构。高层 meta-skills 具有抽象策略特征 (Narrative)


- Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution
- AutoGuide: Automated Generation and Selection of Context-Aware Guidelines for Large Language Model Agents
- Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills
- Skill Set Optimization: Reinforcing Language Model Behavior via Transferable Skills
- Contextual Experience Replay for Self-Improvement of Language Agents
- ExpeL: LLM Agents Are Experiential Learners
- AutoSkill: Experience-Driven Lifelong Learning via Skill Self-Evolution
- GUI-explorer: Autonomous Exploration and Mining of Transition-aware Knowledge for GUI Agent
- SkillClaw: Let Skills Evolve Collectively with Agentic Evolver
- SWE-Exp: Experience-Driven Software Issue Resolution
- Coarse-to-Fine Grounded Memory for LLM Agent Planning
- Mistake Notebook Learning: Batch-Clustered Failures for Training-Free Agent Adaptation
- Get Experience from Practice: LLM Agents with Record & Replay
- H2R: Hierarchical Hindsight Reflection for Multi-Task LLM Agents
- Reflection-Based Memory For Web navigation Agents
- Self-Generated In-Context Examples Improve LLM Agents for Sequential Decision-Making Tasks
- Mirage-1: Augmenting and Updating GUI Agent with Hierarchical Multimodal Skills

### hybrid 


- Memp：将过去 agent 轨迹蒸馏为两个粒度的 Narrative 产物：细粒度 step-by-step 指令和高层 script-like 抽象；通过 Build-Retrieval-Update 动态机制持续更新、修正和淘汰记忆内容（会修改过时记忆），使 procedural memory 随新经验同步演化。
- Dynamic Cheatsheet:在推理时，从之前的 query 解答经验中自动提取和存储累积策略、代码片段和通用问题解决见解；记忆自我策展，聚焦简洁可迁移片段而非完整 transcript；在后续 query 中将这些经验作为额外上下文注入，实现 test-time learning without parameter updates。
- Agent KB:将不同 agent 框架的执行轨迹抽取并标准化为可跨框架检索的结构化经验，在推理时通过两阶段（规划检索与反馈精炼）与一致性门控实现经验共享与迁移，从而提升跨任务与跨系统的 agent 表现。
- AutoManual：三 Agent 架构：Planner 基于当前 rule 编写与环境交互的可执行计划；Builder 通过结构化 rule system 在线更新和管理规则（含 case-conditioned prompting 减少幻觉）；Formulator 将规则编译为综合 manual。
- Meta-Policy Reflexion：将 LLM 生成的 per-episode reflections 整合为结构化的、predicate-like 的 Meta-Policy Memory；在推理时通过 soft memory-guided decoding（偏向与 MPM 一致的动作）和 hard rule admissibility checks（强制执行域约束阻止不安全/无效动作）双重机制复用。将单次反思提升为跨任务可复用的元策略。
- Agentic Context Engineering: 将 contexts 视为 evolving playbooks，通过 generation-reflection-curation 的模块化过程积累和精炼策略；通过 structured incremental updates 防止 context collapse（上下文崩溃——迭代重写导致细节逐渐丧失）；利用自然执行反馈而不需要标注监督。
- What Deserves Memory: NEMORI 以 prediction error 作为经验未来效用的度量标准：Episodic Memory Integration 将原始交互转化为连贯叙事 (Narrative)；Semantic Knowledge Distillation 通过预测误差提取 insights (Narrative)。
- SkillX：三级层次设计：从 raw trajectory 蒸馏为 strategic plans → functional skills → atomic skills 的三层技能层次；Iterative Skills Refinement 基于执行反馈自动修正技能；Exploratory Skills Expansion 主动生成和验证新技能以扩展覆盖范围。

- Memp: Exploring Agent Procedural Memory
- Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory
- Agent KB: Leveraging Cross-Domain Experience for Agentic Problem Solving
- AutoManual: Constructing Instruction Manuals by LLM Agents via Interactive Environmental Learning
- Meta-Policy Reflexion: Reusable Reflective Memory and Rule Admissibility for Resource-Efficient LLM Agent
- Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models
- What Deserves Memory: Adaptive Memory Distillation for LLM Agents
- SkillX: Automatically Constructing Skill Knowledge Bases for Agents


### Discussion


## Narrative → Schematic

### Single-Trajectory Extraction

### Cross-Trajectory Induction


- Traversal-as-Policy:从沙盒执行日志中挖掘成功轨迹中的 state-conditioned action macro，经 merge-check 后编码为 GBT 节点；不安全轨迹触发的 macro 附加 deterministic pre-execution gates，并在 experience-grounded monotonicity 下更新，确保已拒绝的不安全上下文不可重新接纳。


- Traversal-as-Policy: Log-Distilled Gated Behavior Trees as Externalized, Verifiable Policies for Safe, Robust, and Efficient Agents


### hybrid 

LLM 直接提取

- AWM：从训练示例或在线测试查询中收集 agent 交互轨迹，通过 LLM 诱导提取常见复用 routine（workflow），将原始轨迹中重复出现的动作模式抽象为可复用的工作流模板；在后续任务中选择性提供匹配的 workflow 以指导 agent 决策。
- WorkflowGen: 从完整轨迹中提取节点和 workflow 级别的可复用结构化知识；闭环机制通过 trajectory rewriting, experience updating, template induction 仅在可变节点做轻量生成。
- A²Flow: 三阶段：Case-based generation 从 expert demo 生成 operators → Operator Clustering 跨任务初步抽象 → Deep Extraction via long CoT 导出紧凑可泛化执行 operators。operator memory 保留历史输出丰富上下文。
- Meta-Agent-Workflow: 将 LLM 的 tool-reasoning 过程转化为 task-specific workflows（结构化表示）；支持通过不同查询方式检索和基于执行反馈更新。
- FlowMind: Execute-Summarize 解耦执行和构建：先完成任务（执行），再独立从 execution trace 重构结构化 workflow（总结）
- From Logs to Agents: 解析原始 csv/JSON 日志为结构化行为工作流图——将低级系统事件抽象为高级行为 tokens (MODIFY_Prompt, GENERATE_Image 等)，映射创作资产的 provenance 和 flow。low-level system traces → structured workflow graphs 的 P2。
- Workflow Graphs: 从多用户 screen recordings, command logs, 3D model snapshots 构建 W-graphs：编码多用户执行同一 3D 设计任务时方法的收敛和分歧。跨用户经验聚合为结构化图模型 (Schematic)。





- Agent Workflow Memory
- WorkflowGen: an adaptive workflow generation mechanism driven by trajectory experience
- A²Flow: Automating Agentic Workflow Generation via Self-Adaptive 
- Meta-Agent-Workflow: Streamlining Tool Usage in LLMs through Workflow Construction, Retrieval, and Refinement
- FlowMind: Execute-Summarize for Structured Workflow Generation from LLM Reasoning
- From Logs to Agents: Reconstructing High-Level Creative Workflows from Low-Level Raw System Traces
- Workflow Graphs: A Computational Model of Collective Task Strategies for 3D Design Software


参数是：procedural
基于大模型对步骤的理解来执行

- Skill-Pro: 形式化 Skill-MDP 将被动 episodic narrative 转化为可执行 Skill（含 activation/execution/termination 条件）；Non-Parametric PPO 分两阶段运作——semantic gradients 做高质量 candidate generation，PPO Gate 做 robust skill verification（不更新模型参数，而是在语义空间做 PPO 风格的策略优化）；score-based maintenance 维持紧凑高质量 procedural memory。
- AutoRefine: 从执行历史中提取两种形式的经验模式：对于 procedural subtasks 提取专有 subagent（含独立推理和记忆能力）；对于 static knowledge 提取 guidelines 或 code snippets。continuous maintenance mechanism 评分、修剪和合并模式以防止 repository degradation。
- MACLA 将 reasoning 与 learning 解耦：从轨迹中提取可复用 procedure，以 Bayesian posteriors 跟踪其可靠性，通过 contrasting successes and failures（对比精炼）持续改进 procedure 质量。

- Skill-Pro: Learning Reusable Skills from Experience via Non-Parametric PPO for LLM Agents
- AutoRefine: From Trajectories to Reusable Expertise for Continual LLM Agent Refinement
- Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement




- WebXSkill: 从synthetic agent trajectory中，把可执行的“技能”学成“带参数的动作程序 + 每步自然语言指导”的形式，并在“自动执行（grounded）”与“逐步遵循指导（guided）”两种模式下部署，从而提升长流程 Web 代理的成功率与适应/错误恢复能力。


- WebXSkill: Skill Learning for Autonomous Web Agents

生成的可执行 code/API

- Voyager: 通过 iterative prompting mechanism：incorporate environment feedback、execution errors 和 self-verification 三重信号，反复改进生成的程序；成功程序以可执行代码形式存入 skill library。
- Evolving Programmatic Skill Networks：这篇论文展示了如何把具身智能体在任务中的失败/成功经验，通过执行轨迹做分层归因、用maturity门控稳定更新，并在成功后进行语义保持的在线结构重构，转化为不断演化且可复用的符号技能网络。
- SkillWeaver: Agent 在新网站上自主探索发现 skills，通过实践执行获取经验，将实践轨迹蒸馏为可复用的轻量 API；迭代探索持续扩展 API 库。
- Inducing Programmatic Skills for Agentic Tasks：ASI (Agent Skill Induction) 在线交互中诱导、验证和利用程序化 skills：从 web 交互轨迹中提取可复用 action 模式，以程序形式编码，通过 programmatic verification guarantee 确保诱导阶段的正确性；将 click 等 primitive action 组合为 search product 等 higher-level skills。
- MobileGPT: 模拟人类与移动 app 交互的认知过程（explore→select→derive→recall），将任务过程分解为更小的模块化子任务；子任务具有结构性、可复用、可重排和可适配特征。

- Voyager: An Open-Ended Embodied Agent with Large Language Models
- Evolving Programmatic Skill Networks
- SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills
- Inducing Programmatic Skills for Agentic Tasks
- MobileGPT: Augmenting LLM with Human-like App Memory for Mobile Task Automation


Graph:


- A-MEM: 基于 Zettelkasten 原则：新记忆加入时生成包含 contextual descriptions/keywords/tags 的综合笔记；系统分析历史记忆识别相关连接并建立 links；新记忆可以触发已有记忆的 contextual representations 和 attributes 更新。
- AriGraph: Agent 在环境探索中构建并更新整合语义和情景记忆的记忆图（knowledge graph world model）。非结构化探索经验 → 结构化图式世界模型，

- A-MEM: Agentic Memory for LLM Agents
- AriGraph: Learning Knowledge Graph World Models with Episodic Memory for LLM Agents



Tree

- Enhancing Web Agents with a Hierarchical Memory Tree:为此我们提出 Hierarchical Memory Tree (HMT)，一个结构化框架，显式解耦逻辑规划与动作执行。HMT 通过自动抽象流水线从原始轨迹构建三级层级：Intent 层将多样化用户指令映射到标准化任务目标；Stage 层定义以可观察前置条件和后置条件为特征的可复用语义子目标；Action 层存储与可迁移语义元素描述配对的动作模式。


- Enhancing Web Agents with a Hierarchical Memory Tree






- Beyond Training: 三种记忆原语将 agent 进化与模型权重解耦：Profile Memory 以 DisGraph 结构存储用户偏好；Experience Memory 以多级模板实例化任务执行逻辑；Action Memory 记录细粒度交互序列。
- 受组织记忆理论启发，构建三层图层次管理多智能体交互：insight graph 存储高层可泛化见解 (Narrative)，interaction graph 紧凑编码协作经验 (Schematic 图结构)，query graph 连接用户查询。
- Environment Maps: 将 screen recordings 和 execution traces 等多种异构证据整合为结构化图表示：Contexts 抽象位置，Actions 参数化 affordances，Workflows 观察到的轨迹，Tacit Knowledge 领域定义和可复用过程。
- BrainMem: 受人类认知启发，三类记忆协同工作：working memory（即时处理）、episodic memory（交互历史）、semantic memory（结构化知识图谱 + 蒸馏符号化指南）。

- Beyond Training: Enabling Self-Evolution of Agents with MOBIME
- G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems
- Environment Maps: Structured Environmental Representations for Long-Horizon Agents
- BrainMem: Brain-Inspired Evolving Memory for Embodied Agent Task Planning



SOP

- 从人类演示视频生成 SOP：in-context ensemble learning 聚合多个可能 SOP 路径的 pseudo labels，通过 implicit consistency regularization 超越 context window 限制。跨模态 P2：video demo → written SOP (Schematic workflow)。

- In-Context Ensemble Learning from Pseudo Labels Improves Video-Language Models for Low-Level Workflow Understanding