# Section 3 Taxonomy: P1 & P2 文献按转化操作机制分类（修正版）

> 参与分类论文：~85 篇
> P1 = Narrative → Narrative（同层语义抽象：输出为自然语言反思/指南/技能描述/摘要）
> P2 = Narrative → Schematic（同层形式化：输出为可执行代码/API/图/工作流模板/状态机等强结构化形式）
> 源文件 110 篇，去重后 ~108 篇独立工作。排除：编译器/过程挖掘范式、检索机制主导、Benchmark、Out of Scope、P5 跨 Section 论文。
>
> **P1/P2 判定依据**：以 annotated file 的 Pathway 标注为准。关键区分——Skill 类论文：自然语言描述的 skill/guideline/instruction 属于 P1；可执行代码 skill/API/programmatic skill 属于 P2。

---

## M1 — 提示驱动的直接提取（Prompting-Based Direct Extraction）

**驱动力**：LLM 的内部推理能力。无外部反馈循环，无跨轨迹统计，无显式验证步骤。转化机制即 LLM 在单次（或链式但无外部反馈循环的）推理 pass 中阅读一条或多条轨迹，直接输出变换后内容。

**核心特征**：如果 prompt 和 trajectory 不变，输出就确定；转化质量完全依赖 LLM 的归纳推理能力；可能涉及多次 LLM 调用但不构成"执行→反馈→修正"闭环。

### M1 子类总览

| 子类 | 共性机制 | P1 代表工作 | P2 代表工作 |
| :--- | :--- | :--- | :--- |
| M1.1 纠错型反思（Corrective Reflection） | LLM 阅读失败/成功轨迹，提取"哪里错了、下次怎么做"的教训，输出自由文本反思 | Reflexion, CLIN, ReAP, REFLECT, Generative Agents, R2D2 | — |
| M1.2 规程型提取（Procedural Extraction） | LLM 从轨迹中归纳"在 X 条件下做 Y"的条件化规则/指南/playbook | AutoGuide, AutoManual, MPR, NEMORI, Dynamic Cheatsheet, ACE, Atlas, ExpeL, CER, Coarse-to-Fine Grounded Memory | — |
| M1.3 压缩型摘要（Compressive Summarization） | 以降上下文长度为首要目标的轨迹压缩，保留决策关键信息 | WebCoach, M², HiAgent, MemOrb, HELPER, AgentRR, ShowUI-Aloha, R+X, MaP-AVR, Automatic Control Agent | AndroTMem, MapAgent, FlowMind |
| M1.4 多模态提取（Multimodal Extraction） | 输入涉及视觉/视频信号，(V)LM 承担提取 | Learning from Online Videos, ICAL（提取阶段） | Demo2Code（P1+P2） |

> 注：M1.4 与 M1.1–M1.3 非互斥。按 Project_Infos 原则，modality 是正交属性。此处列出的多模态论文分别归入对应的内容子类。

---

### P1 论文（Narrative → Narrative）

#### M1.1 纠错型反思（Corrective Reflection）

**共性机制**：Agent 执行任务后，LLM 被提示回顾轨迹中的错误或成功模式，输出自然语言反思文本。反思存入记忆缓冲区，在后续任务中作为 in-context 指导注入。

1. **Reflexion: language agents with verbal reinforcement learning** — 基于任务反馈信号（标量或自由文本）生成语言化反思，存入 episodic memory buffer，在后续 trial 中注入 context。不更新模型权重。
2. **CLIN: A Continually Learning Language Agent for Rapid Task Adaptation and Generalization** — 以因果抽象为中心的持久动态文本记忆，每次 trial 后更新，使 agent 在多任务、多环境中持续改进。关键是提取因果关系而非通用提示。
3. **ReAP (Reflection-Augment Planning): Reflection-Based Memory For Web Navigation Agents** — 利用成功和失败经验的自我反思增强 web navigation 规划，reflections 可跨任务迁移。
4. **R2D2: Remembering, Replaying and Dynamic Decision Making with a Reflective Agentic Memory** — Remember & Reflect 双范式：Reflect 从错误中学习并精炼策略（P1），Remember 构建页面"地图"（P2）。双产出并列。
5. **REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction** — 基于多传感器观测生成层次化摘要，LLM 推理失败原因，指导语言规划器修正。链式 P1：multisensory → summary → explanation → corrected plan。
6. **Generative Agents: Interactive Simulacra of Human Behavior** — 范式性 P1 工作：observation（存储经验为 NL 记录）→ planning（基于记忆规划）→ reflection（随时间合成为更高层反思）。

---

#### M1.2 规程型提取（Procedural Extraction）

**共性机制**：LLM 从轨迹中提取超越单条反思的、具有条件结构和复用价值的指导性知识。输出比 M1.1 更结构化（条件触发逻辑），但仍为自然语言。关键区分：输出是"know-how 规则"而非"错误教训"。

7. **AutoGuide: Automated Generation and Selection of Context-Aware Guidelines** — 从离线经验中自动生成条件化指南（"在 X 上下文中适用 Y"），克服 demonstration-based ICL 在陌生领域的局限。
8. **AutoManual: Constructing Instruction Manuals by LLM Agents via Interactive Environmental Learning** — Planner 基于规则生成计划，Builder 通过结构化 rule system 在线更新规则（case-conditioned prompting 减少幻觉），Formulator 编译为综合 manual。
9. **MPR (Meta-Policy Reflexion): Reusable Reflective Memory and Rule Admissibility** — 将 LLM 反思整合为结构化谓词式 Meta-Policy Memory，通过 soft memory-guided decoding 和 hard rule admissibility checks (HAC) 在推理时复用。
10. **NEMORI (What Deserves Memory): Adaptive Memory Distillation for LLM Agents** — 以 prediction error 作为"什么值得保留"的度量：Episodic Memory Integration 将原始交互转为连贯叙事，Semantic Knowledge Distillation 通过预测误差提取洞察。数据驱动替代启发式记忆设计。
11. **Dynamic Cheatsheet (DC): Test-Time Learning with Adaptive Memory** — 推理时自策展记忆，存储和复用累积的策略、代码片段和洞察，无需 labels 或 human feedback。聚焦简洁、可迁移的片段。
12. **ACE (Agentic Context Engineering): Evolving Contexts for Self-Improving Language Models** — 将上下文视为演化 playbook，通过 generation-reflection-curation 模块化过程积累和精炼策略。structured incremental updates 防止 context collapse。
13. **Atlas (Compiled Memory): Not More Information, but More Precise Instructions** — 记忆是蒸馏而非存储，交付是 prompt rewriting 而非 context injection。三步 promotion gate 验证后以学得的 sub-bullets 重写 system prompt。关键属性：training signal constraint——学得的 prompt 精确反映所学内容。
14. **ExpeL: LLM Agents Are Experiential Learners** — 从训练任务集中自主收集经验，用自然语言提取知识；推理时召回提取的 insights 和 past experiences。
15. **CER (Contextual Experience Replay): Contextual Experience Replay for Self-Improvement** — 积累和合成过去经验到动态记忆缓冲区，涵盖环境动态和常见决策模式，检索相关知识增强 agent 适应性。
16. **Coarse-to-Fine Grounded Memory for LLM Agent Planning** — 粗到细三级记忆：coarse-grained focus points 指导经验收集 → hybrid-grained actionable tips 从每次经验提取 → fine-grained key information 做 self-QA reflection。

---

#### M1.3 压缩型摘要（Compressive Summarization）

**共性机制**：以降上下文窗口占用为首要目标，将冗长轨迹压缩为紧凑摘要。与 M1.1/M1.2 的关键区别：压缩效率是设计的核心约束，输出保留决策关键信息（状态转移、关键中间结果），丢弃冗余细节。

17. **WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance** — WebCondenser 将原始导航日志标准化为简洁摘要；External Memory Store 组织完整轨迹；Coach 检索并决定是否注入建议。持续策展 episodic memory 实现 self-evolution。
18. **M²: Dual-Memory Augmentation for Long-Horizon Web Agents** — 双层记忆：Internal Memory (Dynamic Trajectory Summarization) 压缩冗长历史为简洁状态更新；External Memory (Insight Retrieval Augmentation) 从离线洞察库检索指南。
19. **HiAgent: Hierarchical Working Memory Management for Solving Long-Horizon Agent Tasks** — 以子目标为记忆块层次化管理 working memory：LLM 先制定子目标，主动用 summarized observations 替换先前子目标，仅保留当前子目标相关的 action-observation pairs。
20. **MemOrb: A Plug-and-Play Verbal-Reinforcement Memory Layer for E-Commerce Customer Service** — 从多轮交互中蒸馏紧凑策略反思，存入共享记忆库，检索后指导决策。强调 consistency 指标（Passᵏ）衡量跨试验可靠性。
21. **HELPER: Open-Ended Instructable Embodied Agents with Memory-Augmented Large Language Models** — 外部记忆存储语言-程序对，部署期间通过人机对话扩充记忆，检索增强 LLM prompting 将自由形式对话解析为动作程序。
22. **AgentRR (Get Experience from Practice): LLM Agents with Record & Replay** — 多级经验抽象方法 + check function 机制：记录 agent 交互轨迹和内部决策过程，摘要为封装工作流和约束的结构化"经验"，在后续相似任务中 replay。
23. **ShowUI-Aloha: Human-Taught GUI Agent** — 四组件 pipeline：Recorder 捕获屏幕和用户交互 → Learner 语义解释为 NL captions → Planner 制定高层 action plan → Executor 执行。human demonstration → structured agent task 的转化。
24. **R+X: Retrieval and Execution from Everyday Human Videos** — VLM 从无标签第一人称人类视频中检索相关片段，in-context imitation learning (KAT) 执行 skill。跨模态转化。
25. **MaP-AVR: A Meta-Action Planner for Agents Leveraging Vision Language Models and RAG** — 将 planned result 抽象为 meta-actions（三要素：move/rotate, end-effector status change, environment relationship），RAG 检索 demonstrations 辅助 in-context learning。
26. **Automatic Control With Human-Like Reasoning: Exploring Language Model Embodied Air Traffic Agents** — experience library（向量数据库）存储从模拟交互和 LLM 推理中合成的知识，后续检索增强决策。
27. **Learning from Online Videos at Inference Time for Computer-Use Agents** — VLM 推断 UI actions，将视频分割为 action 短子序列并分配 textual objective；推理时每步动态选择最相关 trajectory 片段注入。

---

### P2 论文（Narrative → Schematic）

28. **AndroTMem: From Interaction Trajectories to Anchored Memory in Long-Horizon GUI Agents** — Anchored State Memory (ASM) 将交互序列表示为紧凑的因果链接中间状态 anchor 集（Schematic 结构化因果链）。诊断发现长序列性能下降主要由 within-task memory failures 驱动。
29. **MapAgent: Trajectory-Constructed Memory-Augmented Planning for Mobile Task Automation** — 将任务执行轨迹转化为结构化 page-memory database：每页提取为紧凑快照（含 UI layout 和 functional context），粗到细检索注入 LLM planner。
30. **FlowMind: Execute-Summarize for Structured Workflow Generation from LLM Reasoning** — Execute-Summarize 解耦执行和构建：先完成任务，再独立从 execution trace 重构结构化 workflow。分离避免两过程相互干扰。
31. **Demo2Code: From Summarizing Demonstrations to Synthesizing Code via Extended Chain-of-Thought** — 链式 P1+P2：Stage 1 (P1) recursive summarization 将冗长 demonstration 压缩为 concise specification；Stage 2 (P2) code synthesis 从 specification 递归展开生成可执行 robot task code。

---

## M2 — 跨轨迹统计模式归纳（Cross-Trajectory Pattern Induction）

**驱动力**：数据中的统计规律。单条轨迹不足以完成转化——模式只有在跨实例聚合时（频率、聚类、奖励加权、对齐合并）才浮现。核心操作是"找共性"：某模式是否经常出现、是否跨任务复用、是否与正面结果关联。

**核心特征**：需要轨迹集合作为输入；核心计算是统计聚合（频率/聚类/对齐/合并）而非 LLM 单 pass 推理；输出是"典型模式"——常见工作流、可复用技能、共享知识库；LLM 角色是组件（候选生成器、特征提取器），统计过程决定"什么是模式"。

### M2 子类总览

| 子类 | 共性机制 | 代表工作 |
| :--- | :--- | :--- |
| M2.1 频率/共现驱动（Frequency/Co-occurrence Driven） | 统计子序列的共现频率或跨任务复用率，高频模式被提取 | AWM（P2）, Agent KB（P1） |
| M2.2 奖励/结果加权（Reward/Outcome Weighted） | 按成功率或奖励信号加权聚合 | APEX-EM（P1） |
| M2.3 层次化对齐合并（Hierarchical Alignment & Merging） | 将多条轨迹的相似片段对齐、合并、逐层抽象为统一的层次化表示 | Trace2Skill, SkillX, SkillNet, AutoSkill, SWE-Exp, Reasoning Memory（均为 P1） |
| M2.4 自举式合成（Self-Bootstrapping Synthesis） | 无 ground-truth label，通过模型间往返、自我标注或合成-过滤管线生成训练信号 | BAGEL, Learn-by-interact, Self-Generated In-Context Examples（均为 P1）, A²Flow（P2）, APC（P2） |

---

### P1 论文（Narrative → Narrative）

#### M2.1 频率/共现驱动

32. **Agent KB: Leveraging Cross-Domain Experience for Agentic Problem Solving** — 跨异构 agent 框架聚合轨迹到结构化知识库。hybrid retrieval 两阶段：planning 以跨域 workflow 种子 agent，feedback 施加定向诊断修复。disagreement gate 确保检索知识增强而非干扰推理。经验形式为 Narrative workflows + fixes。

#### M2.2 奖励/结果加权

33. **APEX-EM: Non-Parametric Online Learning for Autonomous Agents via Structured Procedural-Episodic Experience Replay** — PRGII workflow 配合 Task Verifiers 提供多维 reward 信号。成功经验作为正例 in-context examples，失败经验作为负例含结构化错误注释。hybrid retrieval 结合 semantic search + structural signature matching + plan DAG traversal。

#### M2.3 层次化对齐合并

34. **Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills** — 调度并行 sub-agent fleet 分析多样化执行池，提取 trajectory-specific lessons，通过归纳推理层次化合并为统一的、无冲突的 skill directory（自然语言指南）。技能可跨 LLM 规模迁移。
35. **SkillX: Automatically Constructing Skill Knowledge Bases for Agents** — 三级技能层次设计（strategic plans → functional skills → atomic skills）+ 迭代技能精炼 + 探索性技能扩展。plug-and-play 技能知识库跨 agent 和环境复用。技能为自然语言描述。
36. **SkillNet: Create, Evaluate, and Connect AI Skills** — 开放基础设施，统一本体论中从异构源创建技能，建立关系连接，多维评估（Safety, Completeness, Executability, Maintainability, Cost-awareness）。超 20 万技能的仓库。
37. **AutoSkill: Experience-Driven Lifelong Learning via Skill Self-Evolution** — 从对话和交互轨迹中自动派生、维护和复用技能（自然语言描述）。模型无关的插件层，支持跨 agent、用户和任务的技能共享。
38. **SWE-Exp: Experience-Driven Software Issue Resolution** — 多面经验库捕获成功和失败修复尝试，多层次提取可复用 issue 解决知识（从高层问题理解到具体代码变更）。从试错探索转向经验驱动的 issue 解决。
39. **Reasoning Memory (Procedural Knowledge at Scale Improves Reasoning)** — 将大规模逐步推理轨迹（3200 万条）分解为 self-contained subquestion-subroutine pairs。推理时 in-thought prompt 让模型口头化核心子问题，检索相关 subroutines 作为隐式程序先验。

#### M2.4 自举式合成

40. **BAGEL: Bootstrapping Agents by Guiding Exploration with Language** — 两含噪 LM 组件间 round-trip 迭代：LM labeler 将 trajectory 转为 synthetic instruction，zero-shot LM agent 将 instruction 映射为 refined trajectory。将初始轨迹分布快速转化为 well-described by NL 的状态。
41. **Learn-by-interact: A Data-Centric Framework for Self-Adaptive Agents in Realistic Environments** — 基于文档合成 agent-环境交互轨迹，通过"backward construction"（摘要化或抽象化交互历史）构建 instructions。合成数据用于 ICL 和 SFT training。
42. **Self-Generated In-Context Examples Improve LLM Agents for Sequential Decision-Making Tasks** — 从自身成功经验自动构建和精炼自生成轨迹数据库。population-based training 做 database-level curation，exemplar-level curation 基于经验效用选择性保留。

---

### P2 论文（Narrative → Schematic）

43. **AWM (Agent Workflow Memory)** — 从训练示例（离线）或测试查询（在线）中诱导常见复用 routine（workflow），选择性提供给 agent 引导后续生成。频率驱动的跨轨迹 workflow 提取。
44. **A²Flow: Automating Agentic Workflow Generation via Self-Adaptive Abstraction Operators** — 三阶段操作符提取：Case-based generation → Operator Clustering（跨任务初步抽象）→ Deep Extraction（long CoT 导出紧凑可泛化执行 operators）。operator memory 保留历史输出。
45. **APC (Agentic Plan Caching): Test-Time Memory for Fast and Cost-Efficient LLM Agents** — 从完成执行的 planning stage 提取结构化 plan templates；keyword extraction 匹配新请求，轻量模型适配 template 到 task-specific plan。不同于 semantic caching，提取和复用 plan 结构骨架。

---

## M3 — 对比差异提取（Contrastive Differential Extraction）

**驱动力**：成功与失败之间的差异信号。转化不是找"典型模式是什么"，而是找"什么区分了成功和失败"。核心操作是配对比较——显式构造正负例对，从中提取区分性、纠错性知识。

**核心特征**：依赖正负例对（成功轨迹 vs 失败轨迹，或实际 vs 反事实）；输出是条件性、纠错性知识（"在 X 情况下不要做 Y"、"为什么失败"、"什么条件下切换策略"）；与 M2 的本质区别：M2 找共性回答"应该做什么"，M3 找差异回答"为什么失败、如何避免"。

### M3 子类总览

| 子类 | 共性机制 | 代表工作 |
| :--- | :--- | :--- |
| M3.1 自然结果对比（Natural Outcome Contrast） | 以环境返回的成功/失败作为天然标签，直接对比成功与失败轨迹 | ReMe（P1） |
| M3.2 反事实生成（Counterfactual Generation） | LLM 主动生成优化轨迹或子目标，构造人工对比对 | ECHO, H²R（均为 P1） |
| M3.3 纯失败端抽象（Failure-Only Abstraction） | 不显式构造成功对比对，仅从失败中聚类提取共性错误模式 | MNL（P1） |

---

### P1 论文（Narrative → Narrative）

46. **ReMe (Remember Me, Refine Me): A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution** — Multi-faceted distillation 同时识别成功模式、分析失败触发因素、生成对比洞察。核心转化是差异提取——在什么条件下成功/失败，产生区分性而非典型性知识。另含 context-adaptive reuse 和 utility-based refinement。
47. **ECHO (Experience Consolidation via Hindsight Optimization): Sample-Efficient Online Learning in LM Agents via Hindsight Trajectory Rewriting** — 将 RL 的 hindsight experience replay 适配给 LM agent：对失败尝试生成反事实优化轨迹，从失败交互中创建合成正例。hindsight rule 用 LLM 识别替代子目标，update rule 维护压缩轨迹表示。
48. **H²R (Hierarchical Hindsight Reflection): Hierarchical Hindsight Reflection for Multi-Task LLM Agents** — 层次化事后反思：解耦高层规划记忆与低层执行记忆，从过去交互中蒸馏层次化知识。测试时分别检索高层和低层记忆。
49. **MNL (Mistake Notebook Learning): Batch-Clustered Failures for Training-Free Agent Adaptation** — 从批处理聚类失败中自策展可泛化指导，将共享错误模式蒸馏为结构化"错误笔记"。仅在 batch 性能提升时更新外部记忆。结合 test-time scaling 主动引导搜索避开已知陷阱。

---

## M4 — 反馈驱动的迭代闭环精炼（Feedback-Driven Iterative Closed-Loop Refinement）

**驱动力**：环境/执行/人类/AI 的反馈信号，通过多轮"生成 → 应用 → 获得反馈 → 修正"循环逐步提升转化质量。LLM 充当隐式优化器——优化逻辑在 LLM 内部（通过自然语言 prompting 实现），而非外部数学算法。

**核心特征**：多轮迭代是必需的（不存在"一次提取完成"）；反馈信号来自实际执行或交互（环境报错、执行成功/失败、人类评价、其他 Agent 分析）；每轮输出是下一轮的输入或修正依据；与 M1 的根本区别：闭环和外部反馈是方法不可移除的核心组件；与 M5 的根本区别：优化器是 LLM（通过 prompting），而非形式化数学算法。

### M4 子类总览

| 子类 | 共性机制 | 代表工作 |
| :--- | :--- | :--- |
| M4.1 环境执行反馈 — Skill 精炼 | 执行后环境返回成功/失败/报错，据此修正 skill | Voyager（P2）, ASI（P2）, SkillWeaver（P2）, TroVE（P2）, ReGAL（P2）, PSN（P2）, WebXSkill（P2）, PolySkill（P1）, SSO（P1）, MemP（P1） |
| M4.1 环境执行反馈 — 结构化表示构建 | 将交互轨迹迭代构建为图/树/状态机等结构化表示 | ActionEngine（P2）, AriGraph（P2）, Environment Maps（P2）, PG-Agent（P2）, HMT（P1+P2）, BrainMem（P1+P2）, GUI-explorer（P1+P2） |
| M4.1 环境执行反馈 — Workflow/模板精炼 | 将执行轨迹迭代精炼为 workflow 或模板 | WorkflowGen（P2）, Meta-Agent-Workflow（P2）, Mirage-1（P1+P2）, AutoRefine（P1+P2）, MUSE（P1） |
| M4.1 环境执行反馈 — 记忆维护与演化 | 通过反馈驱动的评分/剪枝/合并持续维护经验库 | MemP（P1）, AutoRefine（P1+P2）, MUSE（P1）, G-Memory（P1+P2）, UI-Evol（P1）, EchoTrail-GUI（P1） |
| M4.2 自检反馈（Self-Verification Feedback） | Agent 自己评估输出质量，无外部环境信号 | AutoRefine（部分）, PSN（maturity-aware gating 含自检成分） |
| M4.3 人类反馈（Human Feedback） | 人类提供纠正、偏好或示范 | ICAL（P1） |
| M4.4 多 Agent 交叉反馈（Multi-Agent Cross-Feedback） | 一个 Agent 的输出被另一个 Agent 分析/批判/改进 | Recon-Act（P1+P2）, SkillClaw（P1） |

> 注：M4.2 自检反馈通常作为 M4.1 的补充机制出现，不设独立子节。上表中有交叉的论文（如 AutoRefuse 同时出现在结构化表示和工作流精炼），以主要贡献归类。

---

### P1 论文（Narrative → Narrative）

#### M4.1 环境执行反馈 — Skill/知识精炼

50. **ICAL (In-Context Abstraction Learning) / VLM Agents Generate Their Own Memories** — VLM 从次优 demonstration 抽象出通用策略和认知注释，通过人类反馈（M4.3）在相似环境中迭代精炼。随着 example library 增长，抽象新例子的效率提高。当这些抽象 exemplars 用于 fine-tuning 时产生 P5 二次转化，但论文主体贡献在 P1 阶段。
51. **PolySkill: Learning Generalizable Skills Through Polymorphic Abstraction** — 借鉴软件工程多态概念，将 skill 的抽象目标与具体实现解耦。Agent 在多个网站交互中通过探索学习可泛化技能，以自然语言描述为主。核心创新在 skill 表示方式。
52. **SSO (Skill Set Optimization): Reinforcing Language Model Behavior via Transferable Skills** — 提取高奖励公共子轨迹生成子目标和指令（M2）→ 以 in-context 方式注入 LLM actor → 剪枝不再产生高奖励的技能（M4 维护）。技能为自然语言 subgoal + instruction 对。
53. **MemP (Memp): Exploring Agent Procedural Memory** — 将过去 agent 轨迹蒸馏为细粒度逐步指令和高层脚本式抽象（P1）。动态机制持续更新、纠正和弃用记忆内容。程序记忆从强模型迁移到弱模型也能产生显著增益。
54. **MUSE (Learning on the Job): An Experience-Driven Self-Evolving Agent for Long-Horizon Tasks** — 层次化 Memory Module 组织不同层次的经验。每个子任务执行后 agent 自主反思轨迹，将原始轨迹转化为结构化经验并整合回 Memory Module。积累的经验展现 zero-shot generalization。
55. **UI-Evol: Automatic Knowledge Evolving for Computer Use Agents** — 解决 knowledge-execution gap（90% 正确知识仅 41% 执行成功率）：Retrace Stage 从实际交互提取忠实 action sequence，Critique Stage 将 Retrace 序列与 external references 对比精炼知识。
56. **EchoTrail-GUI: Building Actionable Memory for GUI Agents via Critic-Guided Self-Exploration** — 三阶段：Experience Exploration（自主探索 GUI，reward model 验证成功轨迹）→ Memory Injection（检索最相关 past trajectories）→ GUI Task Inference（作为 in-context memory 注入）。

---

### P1+P2 论文（同时产出 Narrative 和 Schematic）

#### M4.1 环境执行反馈 — 双形态产出

57. **AutoRefine: From Trajectories to Reusable Expertise for Continual LLM Agent Refinement** — 双形态经验模式：程序性子任务提取为专有 subagent（P1 + P2），静态知识提取为 guidelines 或 code snippets（P1 + P2）。持续维护机制评分、剪枝和合并模式。
58. **ViReSkill: Vision-Grounded Replanning with Skill Memory for LLM-Based Planning in Lifelong Robot Learning** — 失败时 vision-grounded replanner 生成新动作序列（P1）；成功时执行计划存储为可复用 skill 并在未来 replay（含可执行性，P2 特征）。
59. **HMT (Hierarchical Memory Tree): Enhancing Web Agents with a Hierarchical Memory Tree** — 自动抽象管道构建三层层次：Intent 层统一 user instruction 为任务目标（P1），Stage 层定义可复用语义子目标（P1），Action 层存储 action patterns 配可迁移语义元素描述（P2 特征）。
60. **BrainMem: Brain-Inspired Evolving Memory for Embodied Agent Task Planning** — 三类记忆协同：episodic memory（P1 交互历史），semantic memory（结构化知识图谱 P2 + 蒸馏符号指南 P1）。持续将具身交互历史转化为两类产物。
61. **G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems** — 三层图层次：insight graph 存储高层可泛化见解（P1），interaction graph 紧凑编码协作经验（P2 图结构），query graph 连接用户查询。任务执行后整个层次吸收新轨迹演化。
62. **GUI-explorer: Autonomous Exploration and Mining of Transition-aware Knowledge for GUI Agent** — Function-aware Task Goal Generator 基于 GUI 结构信息自动构建探索目标收集轨迹；Transition-aware Knowledge Extractor 通过无监督分析结构化交互三元组提取 screen-operation logic（兼有 P1 规则描述和 P2 结构化逻辑）。
63. **Recon-Act: A Self-Evolving Multi-Agent Browser-Use System via Web Reconnaissance, Tool Generation, and Task Execution** — Reconnaissance Team 对比错误和成功轨迹推断补救措施，抽象为 unified generalized tools：以 hints（P1）或 rule-based codes（P2）两种形式表达。closed-loop pipeline: data-tools-action-feedback。
64. **Mirage-1: Augmenting and Updating GUI Agent with Hierarchical Multimodal Skills** — HMS 将轨迹逐层抽象为 execution skills → core skills → meta-skills。高层 meta-skills 具有抽象策略特征（P1），低层 execution skills 接近可执行操作序列（P2）。SA-MCTS 利用技能减少在线 tree exploration 的动作搜索空间。

---

### P2 论文（Narrative → Schematic）

#### M4.1 环境执行反馈 — 可执行 Skill/API/函数库

65. **Voyager: An Open-Ended Embodied Agent with Large Language Models** — 迭代提示机制结合环境反馈、执行错误和自验证进行程序改进。技能以可执行 JavaScript 代码形式存储、检索和组合。三个关键组件：自动课程、代码技能库、迭代提示机制。
66. **ASI (Agent Skill Induction): Inducing Programmatic Skills for Agentic Tasks** — 在线诱导、验证和利用基于程序的技能。programmatic verification guarantee 确保诱导阶段正确性。将 primitive actions 组合为 higher-level skills，提升效率。
67. **SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills** — 自主发现技能 → 执行练习 → 蒸馏为可复用轻量 API。迭代探索持续扩展 API 库。强 agent 合成的 API 可迁移给弱 agent。
68. **TroVE: Inducing Verifiable and Efficient Toolboxes for Solving Programmatic Tasks** — 通过"generating via using, growing, and periodically trimming"循环：从已有程序识别可复用模式合成为高层函数，周期修剪 toolbox。函数库比 baseline 小 79-98%。
69. **ReGAL: Refactoring Programs to Discover Generalizable Abstractions** — 通过代码重构（restructuring without changing execution output）迭代发现可复用函数库，执行验证和精炼。发现的 abstractions 封装 frequent subroutines 和 environment dynamics。
70. **PSN (Evolving Programmatic Skill Networks): Programmatic Skill Network** — REFLECT 对 skill composition 做结构化故障定位；maturity-aware update gating 做渐进优化（稳定 skill 保持、不确定 skill 保留可塑性）；canonical structural refactoring with rollback validation 维持紧凑性。
71. **WebXSkill: Skill Learning for Autonomous Web Agents** — 可执行 skill 配对参数化动作程序和步骤级 NL 指导。skill extraction 从 synthetic trajectory 挖掘可复用 action subsequence 并抽象为参数化 skill；skill organization 按 URL-based graph 索引。两种部署模式：grounded（全自动执行）和 guided（作为 step-by-step 指令）。

#### M4.1 环境执行反馈 — 结构化表示（图/树/状态机）

72. **ActionEngine: From Reactive to Programmatic GUI Agents via State Machine Memory** — Crawling Agent 通过离线探索构建 GUI 的可更新状态机记忆（Schematic），Execution Agent 利用记忆合成完整可执行 Python 程序。执行失败触发 vision-based re-grounding fallback 修复并更新记忆。
73. **AriGraph: Learning Knowledge Graph World Models with Episodic Memory for LLM Agents** — Agent 在环境探索中构建并更新融合语义和情景记忆的记忆图（knowledge graph world model）。非结构化探索经验 → 结构化图式世界模型。
74. **Environment Maps: Structured Environmental Representations for Long-Horizon Agents** — 将 screen recordings 和 execution traces 等异构证据整合为结构化图：Contexts（抽象位置）、Actions（参数化 affordances）、Workflows（观察轨迹）、Tacit Knowledge（领域知识和可复用程序）。
75. **PG-Agent: An Agent Powered by Page Graph** — 自动化管道将 sequential episodes 转化为 page graphs，显式建模页面间通过 action 连接的图结构。RAG 检索 page graph 中的可靠感知指南注入 multi-agent framework。

#### M4.1 环境执行反馈 — Workflow/模板精炼

76. **WorkflowGen: An Adaptive Workflow Generation Mechanism Driven by Trajectory Experience** — 闭环机制通过 trajectory rewriting, experience updating, template induction 仅在可变节点做轻量生成。三级自适应路由：direct reuse, rewriting-based generation, full initialization。
77. **Meta-Agent-Workflow: Streamlining Tool Usage in LLMs through Workflow Construction, Retrieval, and Refinement** — 基于执行反馈创建、检索和精炼 agent workflow。将 LLM 工具推理过程转化为任务特定 workflow，支持可视化界面配置（工业应用导向）。

#### M4.4 多 Agent 交叉反馈

78. **SkillClaw: Let Skills Evolve Collectively with Agentic Evolver** — 跨用户和跨时间交互作为改进技能的主要信号。autonomous evolver 处理聚合轨迹，识别重复行为模式并转化为技能更新（精炼现有或扩展新能力）。共享仓库跨用户同步。技能为自然语言描述（P1）。

---

## M5 — 形式化优化驱动（Formal Optimization-Guided Transformation）

**驱动力**：显式的数学目标函数 + 原则性更新规则。优化器不是 LLM，而是一个外部形式化算法（RL、贝叶斯推断、进化算法、策略梯度）。LLM 降级为组件（候选生成器、特征提取器），优化决策——更新什么、保留什么、探索什么——由算法而非 LLM 做出。

**核心特征**：有显式数学目标（expected utility、Bellman equation、fitness function、posterior probability）；更新规则是原则性的（gradient、Bayes rule、selection operator）；LLM 不决定"如何优化"；与 M4 的根本区别：优化器是算法而非 LLM。

### M5 子类总览

| 子类 | 共性机制 | 代表工作 |
| :--- | :--- | :--- |
| M5.1 强化学习（Reinforcement Learning） | 显式 MDP 建模 + 奖励最大化驱动策略更新 | REMEMBERER（P1）, Memento（P1+P5） |
| M5.2 贝叶斯推断（Bayesian Inference） | 概率信念更新追踪可靠性，expected-utility 驱动选择 | MACLA（P1） |
| M5.3 进化计算（Evolutionary Computation） | 种群选择、变异、适应度评估驱动经验库演化 | DMS（P1）, MemEvolve（P1） |
| M5.4 策略梯度风格（Policy Gradient-Style） | 借用 RL 策略梯度框架，通过 LLM 语义操作实现梯度模拟 | Skill-Pro（P2）, MemSkill（P1） |

---

### P1 论文（Narrative → Narrative）

79. **REMEMBERER: Large Language Models Are Semi-Parametric Reinforcement Learning Agents** — LLM 配备长期经验记忆构成半参数 RL agent。RLEM (Reinforcement Learning with Experience Memory) 利用 RL 信号更新记忆内容（不更新 LLM 参数），从成功和失败经验中学习并进化。
80. **MACLA: Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement** — Bayesian posteriors 追踪程序可靠性 → expected-utility scoring 选择动作 → contrastive refinement 对比精炼程序。2851 条轨迹压缩为 187 个程序，构建记忆仅需 56 秒（比 SOTA 参数训练 baseline 快 2800 倍）。程序以自然语言描述形式存在（P1）。
81. **DMS (Darwinian Memory System): A Training-Free Self-Regulating Memory System for GUI Agent Evolution** — 记忆作为动态生态系统受"适者生存"法则支配。将复杂轨迹分解为独立可复用单元，Utility-driven Natural Selection 追踪每个单元的 survival value，主动剪枝次优路径并抑制高风险计划。
82. **MemEvolve: Meta-Evolution of Agent Memory Systems** — 联合演化 agent 的经验知识和记忆架构本身。EvolveLab 将 12 个代表性记忆系统蒸馏为模块化设计空间（encode, store, retrieve, manage），提供标准化实现基底和公平实验场。
83. **MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents** — 将静态 hand-designed memory operations 重新定义为可学习和可进化的 memory skills。Controller 学习 skill selection → Executor 生成 skill-guided memories → Designer 进化 skill set。闭环改进 skill-selection policy 和 skill set 自身。

---

### P2 论文（Narrative → Schematic）

84. **Skill-Pro: Learning Reusable Skills from Experience via Non-Parametric PPO for LLM Agents** — 形式化 Skill-MDP，将被动 episodic narrative 转化为由 activation/execution/termination 条件定义的可执行 Skill（P2）。Non-Parametric PPO：semantic gradients 做高质量候选生成 + PPO Gate 做鲁棒技能验证。score-based maintenance 维持紧凑高质量程序记忆。

---

### 跨 Section 论文（含 P5 组件，本节仅涉及 P1 部分）

85. **EE-MCP: Self-Evolving MCP-GUI Agents via Automated Environment Generation and Experience Learning** — 双轨 self-evolution：experience bank 从 trajectory comparison 积累规则实现推理时改进（P1，本节相关）；distillation 将轨迹转化为 SFT 训练数据更新 policy（P5，§5 相关）。
86. **Memento: Fine-tuning LLM Agents without Fine-tuning LLMs** — Memory-augmented MDP + neural case-selection policy + online RL。episodic memory 存储过去经验（P1，本节相关），neural case-selection policy 涉及轻量参数训练（P5，§5 相关）。

---

## 排除论文清单

### 编译器/过程挖掘范式（6 篇）
- **VCC (View-oriented Conversation Compiler)** — 编译器方法（lex, parse, IR, lower, emit），infrastructural tooling
- **Workflow Graphs** — 多用户 screen recordings + command logs → W-graphs，计算管线
- **From Logs to Agents** — csv/JSON logs → behavioral workflow graphs，过程挖掘
- **Skill Learning Using Process Mining** — process discovery + process models + conformance checking
- **In-Context Ensemble Learning from Pseudo Labels** — video → SOP via in-context ensemble learning
- **Code Models are Zero-shot Precondition Reasoners** — code representations for action preconditions

### 检索机制作为主要贡献（4 篇）
- **Memex(RL)** — indexed experience memory + RL 优化读写策略
- **TRAD** — step-level thought retrieval + aligned decision
- **Synapse** — state abstraction + trajectory-as-exemplar prompting + exemplar memory
- **MemGPT** — virtual context management (OS 类比分层记忆)

### Benchmark（4 篇）
- **SkillFlow: Benchmarking Lifelong Skill Discovery and Evolution**
- **SkillLearnBench: Benchmarking Continual Learning Methods for Agent Skill Generation**
- **A Benchmark for Procedural Memory Retrieval in Language Agents**
- **How Well Do Agentic Skills Work in the Wild: Benchmarking LLM Skill Usage**

### Out of Scope / Annotation Failed（3 篇）
- **GraSP** — annotated file 标注为 Out of Scope：工作聚焦于已有 skills 的组合编排（orchestration），不涉及从经验生成新载体产物
- **Keypoint Action Tokens (KAT)** — annotated file 标注为 Annotation Failed：表示工程（tokenization scheme），缺乏经验转化核心机制
- **From Procedural Skills to Strategy Genes** — 表示格式的经验研究（Gene vs Skill vs freeform text），转化机制本身简单

### 其他排除（4 篇）
- **MobileGPT** — 任务分解 + record-replay，转化机制极浅
- **A-MEM** — Zettelkasten 记忆组织架构，转化本身是简单 LLM 调用
- **R2D2** — 已在 M1.1 列入（Reflect 部分为有效 P1 转化）
- *注：R2D2 同时产出 P1（Reflect）和 P2（Remember），以 Reflect 的 P1 反思为主要转化贡献归入 M1.1*

### 重复论文（去重 2 篇）
- **A²Flow** 出现两次（AAAI 版 + arXiv 版），以 arXiv 版为准
- **ICAL** 出现两次（NeurIPS 短版 + arXiv 长版"Continual Learning"），以 NeurIPS 版为准

---

## 分类统计

| 类别 | P1 | P2 | P1+P2 | 合计 |
| :--- | :-- | :-- | :-- | :-- |
| M1 提示驱动直接提取 | 27 | 4 | 0 | **31** |
| M2 跨轨迹统计模式归纳 | 11 | 3 | 0 | **14** |
| M3 对比差异提取 | 4 | 0 | 0 | **4** |
| M4 反馈驱动迭代闭环精炼 | 8 | 12 | 8 | **28** |
| M5 形式化优化驱动 | 5 | 1 | 0 | **6** |
| 跨 Section（含 P5） | 1 | 0 | 1 | **2** |
| 排除 | — | — | — | **22** |

> 注：P1+P2 列的论文同时产出两种载体形式，在对应子类中已标注具体哪部分为 P1、哪部分为 P2。跨 Section 论文（EE-MCP, Memento）的 P1 组件计入本节，P5 组件归入 §5。

### 与上一版的主要修正

| 修正项 | 旧版 | 新版 | 原因 |
| :--- | :--- | :--- | :--- |
| M4 P2 数量 | 30 | 12 (+8 P1+P2) | "技能"类论文多为 NL 描述（P1），仅可执行代码/API 为 P2 |
| M5 P2 数量 | 6 | 1 | DMS/MemEvolve/MemSkill/REMEMBERER 均为 P1（NL 形式的经验/程序/记忆） |
| M2 P1/P2 分布 | P1 3 / P2 11 | P1 11 / P2 3 | Trace2Skill/SkillX/SkillNet/AutoSkill/SWE-Exp 等均为 NL 技能描述（P1） |
| GraSP | M4 P2 | 排除 | Annotated file 标注 Out of Scope（技能编排，非经验转化） |
| HELPER | M4 P1 | M1 P1 | 转化机制为简单 LLM 解析+存储，无迭代精炼闭环 |
| AgentRR | M1 P2 | M1 P1 | 多级经验抽象产出为 NL 描述的经验+约束，非可执行结构 |

---

## 交叉维度编织指南

以下维度不作为独立分类轴，但在每个机制类别的 Discussion 中作为对比分析线索：

| 交叉维度 | M1 | M2 | M3 | M4 | M5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Online vs Offline** | 偏 online | 偏 offline | 两者都有 | 偏 online | offline 训练 + online 推理 |
| **Static vs Dynamic Update** | 多为 static | 多为 static | 多为 static | 几乎都是 dynamic | dynamic |
| **Append-only vs Append+Modify** | 多为 append-only | 多为 append-only | 多为 append-only | 修改/剪枝/合并为主 | 原则性更新 |
| **主导反馈来源** | 无 | 统计信号 | 环境 outcome 对比 | 环境/人类/Agent 执行反馈 | 数学信号（reward/scalar） |
| **Single-Traj vs Multi-Traj** | 偏 single-traj | 必须 multi-traj | 需正负至少两条 | 偏 multi-episode | 需大量经验 |
| **Single-Agent vs Multi-Agent** | 均为 single-agent | 少数 multi-agent | 均为 single-agent | 少数 multi-agent | 均为 single-agent |
| **Linear vs Hierarchical Extraction** | 两者都有 | 层次化为主 | 多为线性 | 两者都有 | 算法决定 |
