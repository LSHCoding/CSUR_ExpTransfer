# Section 3 Taxonomy V2: P1 论文按提取模式二分

> **核心诊断**：V1 的 M1.1（纠错型反思）/ M1.2（规程型提取）/ M1.3（压缩型摘要）三类边界模糊，大量论文交叉——例如 ReAP 被归入 M1.1，但机制描述随即指出其"reflections 可跨任务迁移"，与后面的跨轨迹归纳类直接矛盾。问题根源在于 **M1 以"输出内容类型"（反思 vs 规则 vs 摘要）作为分类轴，而内容类型本质上是连续的，无法形成互斥的类别边界**。
>
> **V2 方案**：按**提取操作所需的输入单位**二分——**Single-Trajectory Extraction** 与 **Cross-Trajectory Induction**。这条分割线是离散的、可操作的、在方法论上有实质区分度。

---

## 判定准则

| 维度 | Single-Trajectory Extraction | Cross-Trajectory Induction |
| :--- | :--- | :--- |
| **最小输入** | 一条轨迹即可完成提取 | 必须同时面对多条轨迹才能完成归纳 |
| **核心操作** | 阅读单条轨迹 → 输出变换后内容（反思/规则/摘要/指南） | 跨轨迹比较/聚合/对齐/聚类/频率统计/奖励加权 → 浮现跨轨迹模式 |
| **LLM 角色** | 直接执行转化（归纳推理发生在单轨迹内部） | 组件角色（候选生成、特征提取），统计/聚合过程决定"什么是模式" |
| **可并行性** | 每条轨迹可独立并行处理 | 需要轨迹集合作为整体输入，不可拆分为独立单轨迹操作 |
| **典型产物** | 单次教训、条件化规则、压缩摘要、认知注释 | 共享技能库、跨任务工作流、统计显著模式、对比洞察 |
| **关键判据** | 如果只给一条轨迹，方法的核心提取逻辑仍能完整运行 | 如果只给一条轨迹，方法的核心提取逻辑无法运行（需要频率/聚类/对比/聚合） |

### 边界澄清

- **多条轨迹依次处理 ≠ Cross-Trajectory**：如 Reflexion 每条轨迹独立生成反思，只是把多条反思存入同一 buffer，这不改变提取操作的单轨迹性质。
- **单条轨迹内部的跨时间步聚合 ≠ Cross-Trajectory**：如 Generative Agents 从同一 agent 的连续 observation stream 中合成高层反思，输入仍是单一连续经验流（一条"生命轨迹"），属于 Single-Trajectory。
- **需要正负例对的对比提取 → Cross-Trajectory**：如 ReMe 的 comparative insights 需要同时面对成功和失败轨迹才能生成对比洞察。
- **表示层面的创新不改变提取模式**：如 PolySkill 的多态表示（解耦目标与实现）是 skill 如何被组织/表示的选择，提取本身仍可逐网站独立完成。

---

## Category 1: Single-Trajectory Extraction

**定义**：提取操作以单条轨迹为基本输入单位。给定一条完整的（或正在进行的）交互轨迹，LLM 直接从中提取结构化程度不同的知识产物——反思、规则、摘要、指南、认知注释等。多条轨迹可以依次独立处理并累积，但提取逻辑本身不需要跨轨迹比较。

**共性**：如果 prompt 和 trajectory 不变，输出就确定；转化质量完全依赖 LLM 的单轨迹归纳推理能力；每条轨迹可独立并行处理。

### 1.1 纠错型反思（Corrective Reflection）

从单条失败（或成功）轨迹中提取"哪里错了、下次怎么做"。与 V1 M1.1 的核心区别：此处强调每次反思的提取是单轨迹操作，反思的跨任务迁移是**使用方式**而非**提取方式**。

1. **Reflexion** — 读取一条 episode 的 trajectory + feedback signal（标量或自由文本），LLM 生成一条 verbal reflection 存入 episodic buffer。每次反思提取是独立的单轨迹操作。
2. **CLIN** — 每次 trial 后从单条交互轨迹中更新因果抽象记忆。per-trial、per-trajectory 提取。
3. **ReAP (Reflection-Augment Planning)** — 从单个 web navigation 经验（成功或失败）中生成 self-reflection。reflections 可跨任务迁移复用，但每条 reflection 的提取是单轨迹操作。
4. **REFLECT** — 从单次机器人失败的多传感器观测 → 层次化摘要 → failure explanation → corrected plan。链式 P1，全程单轨迹。
5. **Generative Agents** — observation → planning → reflection 循环。reflection 机制从 agent 自身连续经验流（单条生命轨迹）中定期合成高层反思。输入是单一连续经验流，非跨轨迹比较。
6. **R2D2 (Reflect 部分)** — 从单次 web navigation 错误中分析原因并精炼策略。单轨迹反思。Remember 部分产出 P2 页面地图，此处仅涉及 Reflect。

### 1.2 规程型提取（Procedural Extraction）

从单条轨迹中提取具有条件结构（"在 X 情况下做 Y"）的指导性知识。与 1.1 的区别：输出是"know-how 规则"而非"错误教训"；与 V1 M1.2 的区别：去除了实际依赖跨轨迹归纳的论文。

7. **AutoGuide** — 从离线经验中自动生成 context-aware guidelines。每条 guideline 从单条经验独立提取，条件结构描述适用上下文。
8. **AutoManual** — Planner 基于规则生成计划，Builder 逐交互更新规则，Formulator 编译为 manual。规则更新是 per-interaction 的单轨迹操作。
9. **MPR (Meta-Policy Reflexion)** — 将 per-episode reflections 整合为结构化 predicate-like Meta-Policy Memory。每条 reflection 是 per-episode 提取，整合是元层面的结构化为统一记忆体。
10. **NEMORI** — Episodic Memory Integration 将单条原始交互转为连贯叙事；Semantic Knowledge Distillation 以单序列内的 prediction error 提取 insights。两阶段均为单轨迹操作。
11. **Dynamic Cheatsheet** — 从单个 query 解答经验中提取简洁可迁移的代码片段/策略/洞察。每次提取独立。
12. **ACE (Agentic Context Engineering)** — generation-reflection-curation 模块化过程，每次从单条执行反馈中积累和精炼策略。structured incremental updates 防止 context collapse。
13. **Atlas (Compiled Memory)** — 从单次 agent 成功/失败中提取事实，经三步 promotion gate 验证后以 sub-bullets 重写 system prompt。单轨迹事实提取。
14. **CER (Contextual Experience Replay)** — 积累和合成过去经验到动态记忆缓冲区。每条经验独立被存储和合成，无需跨轨迹比较。
15. **Coarse-to-Fine Grounded Memory** — coarse-grained focus points 指导单任务经验收集 → hybrid-grained actionable tips 从每次经验提取 → fine-grained key information 做 self-QA reflection。三级均为单轨迹内操作。

### 1.3 压缩型摘要（Compressive Summarization）

以降上下文窗口占用为首要目标的单轨迹压缩。与 1.1/1.2 的区别：压缩效率是设计的核心约束；与 V1 M1.3 的区别：去除了实际依赖跨轨迹机制的论文。

16. **WebCoach** — WebCondenser 将单条原始导航日志标准化为简洁摘要。每条轨迹独立压缩。
17. **M² (Internal Memory 部分)** — Dynamic Trajectory Summarization 将单条冗长交互历史压缩为简洁状态更新。External Memory 的 insight retrieval 是检索机制，非提取。
18. **HiAgent** — 以子目标为记忆块层级管理单条轨迹的 working memory：用 summarized observations 替换先前子目标，仅保留当前子目标相关 action-observation pairs。
19. **MemOrb** — 将单次多轮客服交互蒸馏为紧凑策略反思，存入共享记忆库。per-interaction 蒸馏。
20. **HELPER** — 将单次人机对话与 action program 配对存入外部记忆。per-dialogue 记忆创建。
21. **AgentRR** — 记录单条 agent 交互轨迹及内部决策过程 → 摘要为结构化"经验"封装工作流和约束 → 后续 replay。per-trajectory 记录和摘要。
22. **ShowUI-Aloha** — Recorder → Learner → Planner → Executor 四组件将单条 human screen recording 转化为结构化 agent task。per-demonstration 转化。
23. **R+X** — VLM 从单条长视频中检索相关片段，in-context imitation 执行 skill。per-video 检索和条件化。
24. **MaP-AVR** — 将单次 planned result 抽象为 meta-actions（三要素），RAG 检索 demonstrations 辅助 ICL。per-demonstration 抽象。
25. **Automatic Control Agent** — experience library（向量数据库）存储从单次模拟交互和 LLM 推理中合成的知识。per-interaction 知识合成。
26. **Learning from Online Videos** — VLM 将单条视频分割为 action 短子序列并分配 textual objective，推理时动态选择。per-video 分割和标注。

### 1.4 单轨迹认知抽象与精炼

从单条轨迹（含人类反馈迭代）中提取认知抽象（因果关系、状态变化、子目标等），或通过执行反馈对单次提取结果进行迭代精炼。这些论文的共同点是提取操作本身不依赖跨轨迹信号——反馈/迭代是对同一条轨迹提取结果的修正，而非跨轨迹聚合。

27. **ICAL (In-Context Abstraction Learning)** — VLM 从单条次优 demonstration 抽象出通用策略和认知注释（因果关系、物体状态变化、时间子目标）。人类反馈在多轮中迭代精炼同一抽象，但抽象操作本身是 per-demonstration。
28. **PolySkill** — Agent 在多个网站交互中学习可泛化技能。核心创新在技能表示（多态抽象：解耦目标与实现），技能的提取本身可在单个网站上独立完成。多网站交互是泛化评估场景而非提取机制的跨轨迹要求。
29. **MemP** — 将单条 agent 轨迹蒸馏为细粒度逐步指令和高层脚本式抽象。Build-Retrieval-Update 动态机制持续更新记忆，但每次蒸馏是 per-trajectory。
30. **MUSE** — 每个子任务执行后 agent 自主反思单条轨迹，将原始轨迹转化为结构化经验并整合回 Memory Module。per-subtask 反思。
31. **UI-Evol** — Retrace Stage 从单次实际交互提取忠实 action sequence；Critique Stage 与 external references 对比精炼。per-interaction 两阶段。
32. **EchoTrail-GUI** — Experience Exploration 中 agent 自主探索 GUI 并收集单条成功轨迹（reward model 验证）；Memory Injection 检索相关轨迹；GUI Task Inference 注入。每条轨迹独立收集。
33. **REMEMBERER** — LLM 配备长期经验记忆构成半参数 RL agent。单条 episode 的经验作为 episodic memory 存储；RLEM 利用 RL 信号决定记忆内容的更新/保留，但经验提取本身是 per-episode。
34. **ECHO** — 借鉴 RL hindsight experience replay：对单条失败轨迹，LLM 识别可达到的替代子目标，生成反事实优化轨迹。核心操作是 per-trajectory 的 counterfactual rewriting。
35. **H²R** — 从单次 agent-环境交互中解耦蒸馏为高层规划记忆和低层执行记忆。per-interaction 分层蒸馏。
36. **Learn-by-interact** — backward construction 将单条 agent-环境交互历史总结或抽象为 instructions。per-history 的摘要化。当用于 SFT 时有 P5 二次转化。
37. **BAGEL** — 两 noisy LM 组件间 round-trip 迭代：LM labeler 将单条 trajectory 转为 synthetic instruction，zero-shot LM agent 映射为 refined trajectory。多轮迭代作用在同一 trajectory-instruction 对上，本质是单轨迹自举优化。
38. **Memex(RL)** — 对单条轨迹做 compact structured summaries + stable indices，完整交互存于外部数据库。RL 训练 agent 决定读写策略，但 summarization 本身是 per-trajectory。

### 1.5 P1+P2 论文的单轨迹 P1 组件

以下论文同时产出 Narrative 和 Schematic 两种载体，其中 Narrative（P1）部分的提取逻辑属于单轨迹操作。

39. **Demo2Code (Stage 1 P1 部分)** — recursive summarization 将单条冗长 demonstration 压缩为 concise specification。per-demonstration 压缩。
40. **AutoRefine (P1 guidelines 部分)** — 从单次执行历史中提取 guidelines（静态知识）。Procedural subtask 的 subagent 提取含 P2 特征。
41. **ViReSkill (P1 replanning 部分)** — 失败时 vision-grounded replanner 基于当前场景生成新动作序列（Narrative）。per-attempt 重规划。
42. **HMT (P1 Intent + Stage 层)** — Intent 层统一 user instruction 为任务目标（Narrative），Stage 层定义可复用语义子目标（Narrative）。从单条原始轨迹逐层抽象。
43. **BrainMem (P1 symbolic guidelines 部分)** — 从单次具身交互历史中蒸馏符号化指南（Narrative）。
44. **G-Memory (P1 insight graph 部分)** — insight graph 从单次 multi-agent 协作中存储高层可泛化见解（Narrative）。
45. **Mirage-1 (P1 meta-skills 部分)** — HMS 将单条轨迹逐层抽象为 execution skills → core skills → meta-skills。高层 meta-skills 具有抽象策略特征（Narrative），提取是逐轨迹逐层进行。
46. **MOBIMEM (P1 memory primitives 部分)** — Profile Memory、Experience Memory（多级模板）、Action Memory 从单次交互中提取 Narrative 记忆原语。
47. **Neuro-Symbolic Dual Memory (P1 Progress Memory 部分)** — 从单条成功轨迹中提取语义蓝图（Narrative）指导全局任务推进。
48. **Memento (P1 episodic memory 部分)** — episodic memory 存储单条过去经验（Narrative）。neural case-selection policy 涉及 P5 组件。

---

## Category 2: Cross-Trajectory Induction

**定义**：提取操作必须以多条轨迹的集合作为输入。单条轨迹不足以完成转化——模式（常见工作流、可复用技能、共享知识、区分性特征）只有在跨实例聚合、比较、对齐、聚类或统计时才浮现。核心操作是"找共性"或"找差异"：某模式是否经常出现、是否跨任务复用、是否与正面结果关联、是否区分成功与失败。

**共性**：需要轨迹集合作为输入；核心计算包含统计聚合（频率/聚类/对齐/合并/奖励加权）或显式跨轨迹对比；LLM 降级为组件（候选生成器、特征提取器），统计过程/对比逻辑决定"什么是模式"。

### 2.1 频率/共现/奖励加权驱动

跨轨迹统计信号是模式浮现的核心驱动力：高频共现的子序列被提取为工作流/技能，高奖励轨迹的片段被加权升权。

1. **Agent KB** — 跨异构 agent 框架（smolagents, OpenHands, OWL）聚合轨迹到结构化知识库。hybrid retrieval 以跨域 workflow 种子 agent。提取机制本质是跨框架轨迹聚合，无法在单框架单轨迹上完成。
2. **APEX-EM** — Task Verifiers 提供多维 reward 信号，成功经验为正例、失败经验为负例（含结构化错误注释）。hybrid retrieval（semantic search + structural signature matching + plan DAG traversal）依赖跨轨迹的正负例分布。核心操作需要多条轨迹以区分正负例。
3. **SSO (Skill Set Optimization)** — 提取高奖励**公共**子轨迹生成子目标和指令。pruning 基于跨轨迹 reward 信号（不再产生高奖励的技能被剪枝）。"公共子轨迹"的识别和剪枝决策均依赖跨轨迹统计。
4. **Self-Generated In-Context Examples** — population-based training 做 database-level curation（传播高质量 example 集合），exemplar-level curation 基于经验效用（跨多条轨迹的 empirical utility）选择性保留。curation 决策必须建立在轨迹集合之上。

### 2.2 层次化对齐合并

将多条轨迹的相似片段对齐、合并、逐层抽象为统一的层次化表示。核心挑战是跨轨迹的去重、冲突消解和粒度统一。

5. **Trace2Skill** — 调度并行 sub-agent fleet 分析**多样化执行池**，提取 trajectory-specific lessons，通过归纳推理**层次化合并**为统一的、无冲突的 skill directory。核心创新恰在于从分散轨迹片段到统一 skill guide 的跨轨迹归纳整合。明确拒绝 sequential single-trajectory 方法。
6. **SkillX** — 三级技能层次（strategic plans → functional skills → atomic skills）+ Iterative Skills Refinement + Exploratory Skills Expansion。从多条 raw trajectories 中蒸馏统一技能层次，跨轨迹去重和泛化。
7. **SkillNet** — 开放基础设施，从**异构源**创建技能并在统一本体论中建立关系连接。超 20 万技能的跨源聚合和组织。
8. **AutoSkill** — 从**跨 session** 的对话和交互轨迹中自动派生、维护和复用技能。技能的生命周期管理（派生、精炼、废弃）需要跨 session 的累积信号。
9. **SWE-Exp** — 多面经验库捕获**多条**成功和失败修复尝试，多层次提取可复用 issue 解决知识（从高层问题理解到具体代码变更）。跨 issue 的知识提取。
10. **Reasoning Memory** — 将大规模逐步推理轨迹（**3200 万条**）分解为 self-contained subquestion-subroutine pairs。分解操作本身是单轨迹，但 subroutine 的提取和价值判断来自跨轨迹的统计显著性——哪些 subquestion 反复出现、哪些 subroutines 被频繁复用。本质上是一个跨轨迹的语料库级归纳过程。

### 2.3 对比差异提取

显式构造跨轨迹对比对（成功 vs 失败、实际 vs 反事实），从差异信号中提取区分性知识。与 V1 M3 的核心区别：此处强调对比是跨轨迹操作的本质属性，而非可选特征。

11. **ReMe** — Multi-faceted distillation 同时识别成功模式、分析失败触发因素、**生成对比洞察**（comparative insights）。context-adaptive reuse 通过 scenario-aware indexing 跨上下文适配。核心转化是差异提取——在什么条件下成功/失败——必须同时面对成功和失败轨迹。
12. **MNL (Mistake Notebook Learning)** — 从**批处理聚类**失败中自策展可泛化指导，将共享错误模式蒸馏为结构化"错误笔记"。仅在 batch 性能提升时更新外部记忆。核心机制（batch clustering of failures → shared error patterns）必须建立在多条失败轨迹之上。
13. **Recon-Act (P1 hints 部分)** — Reconnaissance Team **对比错误和成功轨迹**推断补救措施，抽象为 unified generalized tools（hints 形式，Narrative）。对比操作是跨轨迹的。
14. **EE-MCP (P1 experience bank 部分)** — experience bank 从 **trajectory comparison** 中积累 LLM-learned rules。规则的质量和泛化性依赖跨轨迹比较。
15. **MACLA** — **2851 条轨迹压缩为 187 个 procedure** + contrastive refinement **对比精炼**程序（contrasting successes and failures）。跨轨迹压缩和跨轨迹对比均为方法核心。Bayesian posteriors 追踪程序可靠性——可靠性估计也是跨轨迹的。

### 2.4 进化/优化驱动的跨轨迹种群管理

种群级别的选择、变异、适应度评估驱动经验库或技能集的演化。核心是跨轨迹的 population-level 信号。

16. **DMS (Darwinian Memory System)** — 记忆作为动态生态系统受"适者生存"法则支配。Utility-driven Natural Selection 追踪每个单元的 **survival value**——survival value 是跨多条轨迹累积的统计量，不是单轨迹属性。主动剪枝和抑制依赖跨轨迹的种群竞争。
17. **MemEvolve** — 元进化框架联合演化 agent 的经验知识和**记忆架构本身**。EvolveLab 将 12 个代表性记忆系统蒸馏为模块化设计空间。跨任务、跨 LLM 的元进化必须在多条轨迹上评估架构的适应度。
18. **MemSkill** — Designer 定期审查困难案例（**collectively**），基于多条交互轨迹中的失败模式进化 skill set。Controller 的 skill-selection policy 和 Designer 的 skill set 进化均依赖跨轨迹信号。
19. **SkillClaw** — **跨用户和跨时间**交互作为改进技能的主要信号。autonomous evolver 处理聚合轨迹，识别**重复**行为模式并转化为技能更新。跨用户聚合是跨轨迹的天然要求。

### 2.5 P1+P2 论文的跨轨迹 P1 组件

20. **GUI-explorer (P1 rules 部分)** — Transition-aware Knowledge Extractor 通过**无监督分析**结构化交互三元组（observation, action, outcome）的**状态转移**提取精确 screen-operation logic。分析操作依赖多条轨迹中状态转移的统计规律。
21. **ExpeL** — 从**训练任务集**中自主收集经验，用自然语言提取知识。提取操作以任务集合为单位（"from a collection of training tasks"），非逐任务独立提取。

---

## 分类统计

| 类别 | 论文数 | 占比 |
| :--- | :--: | :--: |
| **Single-Trajectory Extraction** | **48** | 69.6% |
| 　├ 1.1 纠错型反思 | 6 | — |
| 　├ 1.2 规程型提取 | 9 | — |
| 　├ 1.3 压缩型摘要 | 11 | — |
| 　├ 1.4 单轨迹认知抽象与精炼 | 12 | — |
| 　└ 1.5 P1+P2 单轨迹 P1 组件 | 10 | — |
| **Cross-Trajectory Induction** | **21** | 30.4% |
| 　├ 2.1 频率/共现/奖励加权驱动 | 4 | — |
| 　├ 2.2 层次化对齐合并 | 6 | — |
| 　├ 2.3 对比差异提取 | 5 | — |
| 　├ 2.4 进化/优化驱动的跨轨迹种群管理 | 4 | — |
| 　└ 2.5 P1+P2 跨轨迹 P1 组件 | 2 | — |
| **合计** | **69** | 100% |

> 注：子类标签（1.1–1.5, 2.1–2.5）保留自 V1 的语义区分（反思/规程/摘要/认知抽象、频率/对齐/对比/进化），但仅作为二级线索，不作为互斥分类轴。一级分类轴为 Single vs Cross。

---

## 与 V1 的关键差异

| 论文 | V1 归类 | V2 归类 | 重分类理由 |
| :--- | :--- | :--- | :--- |
| ExpeL | M1.2 规程型提取 | Cross 2.5 | "从训练任务集中"提取——输入是任务集合，非单任务 |
| SSO | M4.1 Skill 精炼 | Cross 2.1 | "提取高奖励**公共**子轨迹"——"公共"要求跨轨迹频率分析 |
| ReMe | M3.1 自然结果对比 | Cross 2.3 | "生成**对比**洞察"——对比操作必须同时面对成功和失败轨迹 |
| MACLA | M5.2 贝叶斯推断 | Cross 2.3 | 2851→187 压缩 + contrastive refinement 对比精炼均跨轨迹 |
| DMS | M5.3 进化计算 | Cross 2.4 | survival value 是跨轨迹种群统计量，非单轨迹属性 |
| MemEvolve | M5.3 进化计算 | Cross 2.4 | 元进化需跨任务评估架构适应度 |
| MemSkill | M5.4 策略梯度风格 | Cross 2.4 | Designer 审查困难案例集合进化 skill set |
| SkillClaw | M4.4 多 Agent 反馈 | Cross 2.4 | 跨用户、跨时间聚合——天然跨轨迹 |
| GUI-explorer | M4.1 双形态产出 | Cross 2.5 | Transition-aware 提取需无监督分析多条状态转移 |
| Recon-Act | M4.4 多 Agent 反馈 | Cross 2.3 | "**对比**错误和成功轨迹"——显式跨轨迹对比 |
| EE-MCP | Cross-Section | Cross 2.3 | "trajectory **comparison**"——比较是核心操作 |
| Learn-by-interact | M2.4 自举式合成 | Single 1.4 | backward construction 是 per-history 摘要化，非跨轨迹 |
| BAGEL | M2.4 自举式合成 | Single 1.4 | round-trip 迭代作用在同一 trajectory-instruction 对上 |
| PolySkill | M4.1 Skill 精炼 | Single 1.4 | 核心创新在表示（多态），提取本身可逐网站独立完成 |
| Generative Agents | M1.1 纠错型反思 | Single 1.1 | 反思来自同一 agent 的连续经验流（单条生命轨迹），非跨 agent 比较 |

---

## 排除论文

以下论文在 V1 中已被排除，V2 维持排除：

### 编译器/过程挖掘范式（6 篇）
- VCC (View-oriented Conversation Compiler)
- Workflow Graphs
- From Logs to Agents
- Skill Learning Using Process Mining
- In-Context Ensemble Learning from Pseudo Labels
- Code Models are Zero-shot Precondition Reasoners

### 检索机制作为主要贡献（3 篇）
- Synapse — state abstraction + trajectory-as-exemplar prompting，转化机制浅（仅存储轨迹为 exemplars）
- TRAD — step-level thought retrieval，核心在检索粒度而非经验转化
- MemGPT — virtual context management (OS 类比分层记忆)，基础设施层面

### Benchmark（4 篇）
- SkillFlow, SkillLearnBench, A Benchmark for Procedural Memory Retrieval, How Well Do Agentic Skills Work in the Wild

### Out of Scope / 转化机制极浅（4 篇）
- GraSP — 技能编排（orchestration），非经验转化
- Keypoint Action Tokens (KAT) — 表示工程（tokenization scheme），缺乏转化核心机制
- From Procedural Skills to Strategy Genes — 表示格式的经验研究，转化机制本身简单
- MobileGPT — 任务分解 + record-replay，转化机制极浅

### 内部去重（2 篇）
- A²Flow（AAAI + arXiv 两版，以 arXiv 版为准）
- ICAL（NeurIPS 短版 + arXiv 长版，以 NeurIPS 版为准）

---

## 使用说明

1. **一级分类（Single vs Cross）是互斥的**：每篇论文的提取机制本质上要么只需要单条轨迹，要么必须多条轨迹。不存在既是 Single 又是 Cross 的情况。
2. **二级标签（反思/规程/摘要/认知抽象、频率/对齐/对比/进化）是语义线索**：用于在各自大类内部提供额外的机制区分，但不作为互斥轴。同一篇论文可能同时具有反思和规程特征，这不构成分类矛盾。
3. **P1+P2 论文的 P1 组件单独列出**：因为这些论文的 P1 部分和 P2 部分可能分属不同的大类（如 Recon-Act 的 P1 hints 是 Cross-Trajectory，P2 rule-based codes 是 P2），在各自类别中分别讨论。
4. **边界争议**：部分论文（如 PolySkill、BAGEL、Generative Agents）的分类可能存在不同解读。这些在各自条目中标注了判定依据，供后续讨论修正。
