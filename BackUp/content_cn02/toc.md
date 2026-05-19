Tokenized-to-Tokenized Transformations
    Narrative-to-Narrative Transformation
        Per-Trajectory Experience Abstraction
        Cross-Trajectory Experience Induction
        Dual-Granularity Experience Consolidation
    Narrative-to-Schematic Transformation
        Programmatic Skill Construction
        Procedural Workflow Induction
        Structured Memory Graph Construction
Tokenized-to-Latent Transformation
    Cache-Based Latent Transformation
    Prompt-Based Latent Transformation
    Module-Based Latent Transformation
Tokenized-to-Parametric Transformation
    Tokenized-to-Evaluator Transformation
        Outcome-supervised Evaluator Internalization
        Process-supervised Evaluator Internalization
        Diagnostic-feedback Evaluator Internalization
    Tokenized-to-Policy Transformation
        Imitation-based Policy Internalization
        Reward-based Policy Internalization
        Preference-based Policy Internalization
Parametric-Source Transformations
    Evaluator-to-Policy Transformation
        Outcome Reward-to-Policy Transformation
        Process Reward-to-Policy Transformation
        Diagnostic Feedback-to-Policy Transformation
    Parametric-to-Tokenized Experience Transformation
        Demonstration Externalization
        Evaluative Supervision Externalization
Composite Pipline
    Evaluator–Policy Co-Evolution
    Refine and Policy Internalization


你是一位资深的 AI 研究者，正在协助我完成一篇投稿 ACM Computing Surveys (CSUR) 的综述论文的一个具体分析任务。

综述题为 **Experience Transformation in LLM-based Agents**——研究 LLM-based Agent 的"交互经验"在不同载体之间的转化与复用机制。

**核心立意**：从静态大模型（LLM、VLM 等）到自主 Agent 的转变带来一个根本变化——Agent 在持续的 *experience loop* 中运作：在具体决策上下文下尝试任务、产生异构动作（推理轨迹、工具调用、环境控制等）、观察环境反馈，并可选地接收评价信号。这些累积的决策证据即 *agent experience*。社区由此发展出多种存储与复用经验的机制，对应不同的载体形式。综述不按传统的"组件"（Memory / Planning / Tool Use）或"技术"（SFT / RAG / RLHF）维度分类，而是以 **Experience 的 Transformation Pathway** 为主线，将 memory、evaluator、training 视为同一经验语义在不同载体间的 representation-to-representation pathway。

按"经验在模型架构中的存在层次"分为三类，存在 **Tokenized → Latent → Parametric** 的连续谱（interpretability 递减、inference efficiency 递增、editability 递减）：

| 载体 | 简称 | 定义 |
|---|---|---|
| Narrative Tokenized | N-Tok | 弱形式化离散 token 载体，依自然语言 / 感知顺序组织，通过 language / multimodal understanding 复用（反思、规则、摘要、screenshot 序列等） |
| Schematic Tokenized | S-Tok | 强形式化离散 token 载体，依语法 / 拓扑结构组织，通过 parsing / execution / graph traversal 复用（code、workflow、KG、SOP 等） |
| Latent | Lat | 连续向量 / hidden state 载体，直接参与 attention 或 hidden-state 计算（KV cache、soft prompt、memory token 等） |
| Policy Parameter | π-Par | 固化在权重中的决策能力（actor，生成 action） |
| Evaluator Parameter | V-Par | 固化在权重中的评估能力（RM / PRM / verifier / critic / judge） |

下面 Survey 中涉及的一个小节，以及和这个小节对应的论文，你需要找到这个小节对应的论文，每个论文用 1～2 句描述其关键思想和方法（可以放在 Survey 的正文中使用，输出为中文，专有名词仍然使用英文）。不能只看论文的标题和摘要，要读论文的内容。我给的论文，虽然是人工筛选的，但是也并不完全确实 100% 是匹配的。


现在，我准备重写一下 P6 这部分的内容。我准备准备借助大模型来帮助我快速的读论文。我已经有 P6 这部分的论文列表了，并且有也有相关的论文全文。我希望大模型能够读对应的英文，并对每篇论文以表格格式进行总结，每篇论文的总结包括论文的标题、2～3句描述其关键思想和方法（详细一点，后续会用大模型根据这个总结的内容来写 Survey）、领域、方法缩写、备注。你帮我写一下提示词，特别是其中的分类轴要写清楚。 下面是和 P6 对称的 P4 的读论文的提示词，你可以参考。


---

# 提示词

你是一位熟悉 LLM-based Agent 与 reward modeling 文献的研究助理。我会给你一篇或多篇英文论文的全文。你的任务是阅读每篇全文,并按下方规定的表格格式为每篇论文输出一行总结。

## 背景:本次工作的分析框架

这些论文属于一个 survey 的同一节,主题是 **Tokenized-to-Evaluator Transformation**——即把 agent 的交互经验(trajectory、reasoning trace、tool-use log、preference pair、execution outcome 等离散经验)通过**训练**内化进一个评估器(Evaluator)的参数中。训练后的 Evaluator 形态包括 reward model、process reward model、verifier、critic、judge、value model、failure detector 等。

判定一篇论文是否属于本范围,看一个硬标准:**Evaluator 的参数是否被经验数据实质性更新**。只在推理时用 prompt 激发已有模型评估能力、参数不更新的 prompted LLM-as-a-judge **不属于**本范围——如果你判断某篇论文只是 prompted judge 而无参数训练,请在备注里明确指出。训练方法不限(SFT、RL、self-training、对比学习等都可以),判定只看参数是否被更新。

## 你要填的两条核心分类轴

每篇论文必须沿以下两条**相互独立**的轴各给出一个取值。这两条轴是分开判断的,不要让一条的取值影响另一条。

### 轴一:粒度(Granularity)—— 监督信号分配在什么范围上

判断**训练时的监督信号 / label 被分配到哪个层级**:

- **outcome**:监督信号分配在**完整输出 / 完整轨迹 / 完整 episode** 这一整体层级上。典型形态——判断最终答案是否正确、任务整体是否完成、两个完整 response 哪个更好、整条 trajectory 在某 criterion 下是否更优。Evaluator 对"一个完整候选行为"给出一个整体判断。
- **process**:监督信号分配在**中间步骤 / 动作前缀 / 单个 decision** 这一局部层级上。典型形态——对每个 reasoning step、每个 tool call、每个 GUI action、每个 state-action 对给出局部评价(是否正确、是否有进展、step-level advantage、Q-value、progress value 等)。

判定要点:
- 看的是**监督信号的分配粒度**,不是论文研究的任务有多少步。一个多步 agent 任务,如果 Evaluator 只在最终成败上拿到 label,它仍是 **outcome**。
- 若论文同时训练 outcome-level 与 process-level 两种信号(例如联合学 reward 头和 step-wise value 头),填 **outcome+process**,并在备注里说明。
- 难以判断时,问:"这个 Evaluator 训练时,label 是挂在整条轨迹上,还是挂在某一步上?"

### 轴二:产物形态(Output Form)—— 训练后的 Evaluator 输出什么

判断**训练完成后,Evaluator 在推理时输出的产物是什么形态**:

- **scalar**:产物是标量分数,或可直接塌缩为标量的信号(单个数值分、binary 正确性 0/1、pairwise 偏好概率、多维 reward 向量)。核心特征——产物可直接作为数值信号被下游消费,不携带自然语言解释。
- **non-scalar**:产物是自然语言或结构化的**生成式内容**——natural-language critique、error diagnosis、failure explanation、verification rationale、repair suggestion、structured justification 等。核心特征——产物携带"为什么"和"怎么改"的语义信息,而不只是"好/坏"。

判定要点:
- 看的是 Evaluator 推理时**实际吐出的东西**。一个模型若先生成一段 reasoning/critique 文本、最后再给一个分数,只要那段文本是产物的一部分且对下游有用,归 **non-scalar**;若 reasoning 只是内部 CoT、最终对外只暴露一个分数,归 **scalar**。
- generative reward model 不必然是 non-scalar——若它"生成"的只是 verdict token 然后被读成标量分,本质仍是 scalar。关键看产物里有没有可被人读取、可指导修正的语义内容。
- 若论文的 Evaluator 同时输出标量分**和**自然语言诊断(两者都是有意设计的对外产物),填 **scalar+non-scalar**,并在备注里说明。

### 两条轴正交,会出现全部四种组合

不要默认 process 就配 non-scalar、outcome 就配 scalar。四种组合都真实存在:scalar outcome RM、non-scalar outcome judge(如对完整轨迹做 free-form failure reasoning)、scalar process PRM(如 step-level binary PRM)、non-scalar process critic(如对每一步生成长文本 critique)。请独立判断每一条轴。

## 输出格式

输出 Markdown 表格行(不含表头,表头我已有),六列,顺序固定:

| 列 | 内容要求 |
|---|---|
| 引用标识 | 如 [Pat24] |
| 标题 | 论文标题原文 |
| 关键思想与方法 | 这一列会被直接用于撰写 survey 正文,务必详细、具体、信息密集,**4-6 句**。需覆盖:(1) 这篇论文用什么**经验数据**作为训练来源(human step annotation、self-play rollout、preference pair、execution video、counterfactual relabeled data 等);(2) 用什么**训练方法**把经验内化进 Evaluator(具体到方法名,如 GRPO、Bradley-Terry、binary search rollout 定位 first error、TD/GAE 估计 step-wise pseudo-label、对比学习等);(3) 训练后的 Evaluator **学到了什么评估能力**;(4) **产物的具体形态**——不要只说 scalar/non-scalar,要说清它具体输出什么(例如"对每个 reasoning step 输出 positive/negative/neutral 三分类标签""生成包含 observation analysis、critique、corrective suggestion 的结构化文本再附一个 correctness score""对完整 web trajectory 输出单一 success/failure 二值判断"),以及该产物如何被下游使用(若论文有提及)。避免泛泛而谈,不要写"训练了一个 reward model"这种无信息量的句子。 |
| 粒度 | outcome / process / outcome+process 三者之一 |
| 产物 | scalar / non-scalar / scalar+non-scalar 三者之一 |
| 领域 | 论文针对的 agent 领域,如 reasoning(math)、web、GUI / computer-use、code、embodied / robotics、general 等 |
| 备注 | 仅在以下情况填写,否则留空:(a) 你对粒度或产物的判定不确定,说明理由与你倾向的取值;(b) 该论文可能不属于本范围(疑似 prompted judge 无参数更新、或经验语义不成立);(c) 出现 outcome+process 或 scalar+non-scalar 组合,说明具体情况。 |

## 执行要求

- 基于论文全文判断,不要只看 abstract。粒度和产物形态这两条轴,以及"关键思想与方法"中的方法细节,经常要读到 method 章节才能确定。
- 如果全文信息不足以确定某条轴的取值,不要猜——在备注里写明信息缺失,并给出你基于现有信息的最可能判断。
- "关键思想与方法"一列写中文,专业名词保留英文;标题保留英文原文。
- 如果我一次给了多篇论文,为每篇各输出一行,顺序与我给出的顺序一致;每行之间不要插入空行或额外说明文字。
- 只根据论文实际内容总结,不要推断或补充论文未写的东西;论文没提的字段写「未明确」。



# 任务

你是一名熟悉 LLM-based Agent 与强化学习的研究助理。我会提供若干篇英文论文全文,它们都属于一篇综述中「P5:Tokenized-to-Policy Transformation」一节的文献。请阅读每篇论文,按下方字段与分类轴,为每篇输出一行表格总结。总结用于后续撰写综述正文,描述需具体、信息密集,不要泛泛而谈。

输出语言:中文,专业术语保留英文。

# 背景:P5 是什么

P5 指把离散化的 Agent 交互经验(自然语言轨迹、工具调用记录、代码编辑历史、GUI 操作序列、reasoning chains 等 Tokenized 形式)内化进 Policy/Actor 的模型参数,使模型不再依赖显式检索或重放原始经验即可决策。本节只关心「经验如何被组织成训练信号、并改变 policy 权重」。

# 分类轴(最重要,严格执行)

判定依据只有一条:**真正更新 policy 权重的核心监督信号是什么**。据此分三个子类:

**① Imitation-based** — 核心更新方式是 supervised loss(SFT / behavior cloning / rejection-sampling fine-tuning)施加在示范轨迹上。环境反馈 / 任务结果只用于筛选、清洗、重构、标注训练样本,本身不作为优化目标进入 loss。

**② Reward-based** — 核心训练信号是非参数化、可程序验证的环境反馈(unit test 通过与否、code / SQL execution correctness、task success flag、string / URL match、rule-based verifier、ground-truth match 等),且该信号直接作为 reward 进入 policy-gradient 类优化(PPO / GRPO / DAPO / RLOO 等)。

**③ Preference-based** — 核心 objective 是 preference / trajectory-pair optimization(DPO / DMPO 等),偏好标签来自非参数化信号(执行成功、任务完成、测试通过、人工或规则比较得出的轨迹优劣)。

判定优先级与易错点:
- 按**实际机制**分类,不按论文自称。一篇论文自称 "RL" / "self-improvement" / "bootstrapping",但实际只是在过滤后的成功轨迹上做 supervised fine-tuning → 归 Imitation。务必到 method 部分确认 loss 形式。
- 论文若分阶段(如先 SFT 热启动再 RL),按**最终 / 核心的 policy 更新方式**归类,次要阶段写进备注。
- actor-critic 里的 value critic **不**使该工作变成 evaluator-mediated:critic 是 RL 算法内部从环境 reward bootstrap 出来的辅助件,reward 来源仍是环境,这类工作仍归 Reward-based。

# 三条边界(命中则在备注标记,不要强行塞进三类)

**[P6-边界]** — 若 reward 或 preference 标签的核心来源是 trained reward model / PRM / LLM-as-a-judge 等**参数化 evaluator**,该工作偏向 P6 而非 P5。仍输出该行,备注首位标 `[P6-边界]` 并一句话说明 evaluator 形态。

**[Composite]** — 若经验进入 policy 之前先被转化成另一种 carrier——例如被重构成显式 CoT(Narrative→Narrative)、被转写成可执行 procedural guidance / code(Narrative→Schematic)、或先被压成 latent 表示——该工作形态是 P1→P5 / P2→P5 / P3→P5 的链式组合。仍输出该行,备注标 `[Composite: Px→P5]` 并说明跨了哪一步。

**[疑似越界]** — 若论文实际并未更新 policy 权重(如仅 prompt-level / inference-time 方法),标记并简述理由。

# 每篇论文输出以下字段(表格一行)

| 字段 | 要求 |
|---|---|
| 引用标识 | 若我在提供论文时附了 citation key(如 [Pat24]),填入;否则留空 |
| 论文标题 | 英文原标题 |
| 关键思想与方法 | 2–4 句,必须明确写出三件事:(a) 源经验是什么形式、来自哪里(self / human / teacher);(b) 监督信号是什么;(c) policy 如何被更新(具体算法名)。若有特别设计——credit assignment 粒度、reward 结构分解、exploration 机制、replay buffer / curriculum 等——一并点出。要具体,不要用「提升了性能」这类空话 |
| 领域 | 如 GUI agent / web navigation / software engineering / tool use / embodied-VLA / math reasoning / text-to-SQL / general agent |
| 方法缩写 | 用 ⟨SFT⟩ / ⟨RL: PPO⟩ / ⟨RL: GRPO⟩ / ⟨RL: DPO⟩ / ⟨RL: ReST⟩ / ⟨hybrid⟩ 等标签,并补上论文使用的具体算法名(如 DAPO、M-GRPO、GiGPO、DD-PPO) |
| 子类归属 | Imitation-based / Reward-based / Preference-based 三选一 |
| 备注 | 边界标记([P6-边界] / [Composite] / [疑似越界])放最前;其余可写:online / offline、experience source、能力边界相关特点、与同类工作的对照点、任何影响归类的不确定性 |

# 其他要求
- 只根据论文实际内容总结,不要推断或补充论文未写的东西;论文没提的字段写「未明确」。
- 基于论文全文判断,不要只看 abstract。
- 分类拿不准时,给出判断 + 在备注说明依据和不确定点,不要静默归类。
- 多篇论文合并进同一张表,每篇一行。

备注：
我给的论文，虽然是人工筛选的，但是也并不完全确实 100% 是完全对的。

下面是待阅读的论文：

Imitation-based Policy Internalization
论文：
- Large Language Models Can Self-Improve At Web Agent Tasks
- AndroidGen: Building an Android Language Agent under Data Scarcity
- AppVLM: A Lightweight Vision Language Model for Online App Control
- Explorer: Scaling Exploration-driven Web Trajectory Synthesis for Multimodal Web Agents
- Go-Browse: Training Web Agents with Structured Exploration
- WebCoT: Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback
- AgentTuning: Enabling Generalized Agent Abilities for LLMs
- AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials
- NNetNav: Unsupervised Learning of Browser Agents Through Environment Interaction in the Wild
- Training Software Engineering Agents and Verifiers with SWE-Gym

Reward-based Policy Internalization
论文：
- Grounding Large Language Models in Interactive Environments with Online Reinforcement Learning [Car23]
- Large Language Models as Generalizable Policies for Embodied Tasks [Szo23]
- ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL [Zho24f]
- WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning [Wei25]
- Training Long-Context, Multi-Turn Software Engineering Agents with Reinforcement Learning [Gol25]
- GUI-R1: A Generalist R1-Style Vision-Language Action Model For GUI Agents [Luo25b]
- Improving Vision-Language-Action Model with Online Reinforcement Learning [Guo25d]
- AgentCPM-GUI: Building Mobile-Use Agents with Reinforcement Fine-Tuning [Zha25an]
- SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning [Li25aa]
- Fine-Tuning Large Vision-Language Models as Decision-Making Agents via Reinforcement Learning [Zha24s]
- AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning [Xi25c]
- Agentic Reinforced Policy Optimization [Don25d]
- AgentRL: Scaling Agentic Reinforcement Learning with a Multi-Turn, Multi-Task Framework [Zha25ag]
- Information Gain-based Policy Optimization: A Simple and Effective Approach for Multi-Turn LLM Agents [Wan25y]
- UI-S1: Advancing GUI Automation via Semi-online Reinforcement Learning [Lu25j]
- EPO: Entropy-regularized Policy Optimization for LLM Agents Reinforcement Learning [Xu25k]
- SQL-Trail: Multi-Turn Reinforcement Learning with Interleaved Feedback for Text-to-SQL [Hua26d]
- LongNav-R1: Horizon-Adaptive Multi-Turn RL for Long-Horizon VLA Navigation [Hu26e]
- Agentic Entropy-Balanced Policy Optimization [Don25c]
- Harnessing Uncertainty: Entropy-Modulated Policy Gradients for Long-Horizon LLM Agents [Wan25ad]
- ARPO: End-to-End Policy Optimization for GUI Agents with Experience Replay [Lu25f]
- Group-in-Group Policy Optimization for LLM Agent Training [Fen25c]
- ToolRL: Reward is All Tool Learning Needs [Qia25b]
- Generalization in Online Reinforcement Learning for Mobile Agents [Gu26b]
- Reinforcement Learning for Long-Horizon Interactive LLM Agents [Che25af]
- Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs [Li25ae]
- Q-SFT: Q-Learning for Language Models via Supervised Fine-Tuning [Hon24]
- SQL-ASTRA: Alleviating Sparse Feedback in Agentic SQL via Column-Set Matching and Trajectory Aggregation [Li26r]
- RLVMR: Reinforcement Learning with Verifiable Meta-Reasoning Rewards for Robust Long-Horizon Agents [Zha25ao]
- Succeed or Learn Slowly: Sample Efficient Off-Policy Reinforcement Learning for Mobile App Control [Pap25c]

Preference-based Policy Internalization
论文：
- Direct Multi-Turn Preference Optimization for Language Agents
- Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents
- Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards
- Advancing Tool-Augmented Large Language Models: Integrating Insights from Errors in Inference Trees
- Solving the Granularity Mismatch: Hierarchical Preference Learning for Long-Horizon LLM Agents
- WEPO: Web Element Preference Optimization for LLM-based Web Navigation


# P6 论文阅读提示词：Evaluator → Policy Transformation

你是一位熟悉 LLM-based Agent、RLHF 与 preference alignment 文献的研究助理。我会给你一篇或多篇英文论文的全文。你的任务是阅读每篇全文，并按下方规定的表格格式为每篇论文输出一行总结。

## 背景

这些论文属于一个 survey 的同一节，主题是 **Evaluator-to-Policy Transformation (P6)**——已内化在参数化评估器（reward model、PRM、verifier、critic、judge、value model 等）中的评价能力，通过训练信号转移到 Policy 参数中。

P6 的判定标准：存在一个参数化 Evaluator 产生评价信号，且该信号被用于**更新 Policy 参数**。若 Evaluator 只在推理时使用（reranking、best-of-N、MCTS 引导等）而 Policy 权重未更新，不属于 P6。若信号源是纯规则或环境内置 reward（代码执行通过/失败、game score），不属于 P6（归 P5）。

## 两条分类轴

### 轴一：反馈粒度（Granularity）—— Evaluator 的反馈信号作用在什么层级

- **outcome**：Evaluator 对**完整输出 / 完整轨迹 / 完整 episode** 给出整体评价，该信号驱动 Policy 更新。如：对完整 response 打分、比较两个完整回答的优劣、判断整条轨迹成功/失败。
- **process**：Evaluator 对**中间步骤 / 局部动作 / reasoning prefix / state-action pair** 给出局部评价，该信号驱动 Policy 更新。如：对每个 reasoning step 打分、定位 first error step、per-action Q-value、turn-level advantage。

判定看 Evaluator 信号的分配粒度。多步 agent 若只从 ORM 拿整条轨迹总分，仍是 outcome（PPO 内部的 GAE 分配不改变这一点）。若 step-level 信息仅用于汇总出一个 trajectory score 而 policy 只接收轨迹级偏好，仍归 outcome。

### 轴二：反馈形态（Feedback Form）—— 驱动 Policy 更新的 Evaluator 产物是什么形态

- **判别式（discriminative）**：Evaluator 产出**标量信号或可直接塌缩为标量的判断**——数值分数、binary 正确性、pairwise 偏好概率、多维 reward 向量、first-error-step 定位索引等。核心特征：产物是"好不好"或"哪个更好"的判断，不携带自然语言解释。
- **生成式（generative）**：Evaluator 产出**自然语言或结构化的生成内容**——critique、failure explanation、error analysis、refinement suggestion、corrected step、revised trajectory、action directive 等。核心特征：产物携带"为什么不好""应该怎么改"的语义信息。

判定看**实际进入 Policy 训练的 feedback artifact**。若 Evaluator 先生成 critique 再输出 scalar score，且进入 Policy 训练的只有 score，归判别式。若修正后的轨迹被用作 SFT target，归生成式。若两种产物都被 Policy 训练消费，填 **判别式+生成式**。

### 两条轴正交

不要默认 outcome 配判别式、process 配生成式。四种组合都存在：判别式 outcome（经典 ORM + RLHF）、生成式 outcome（对完整轨迹生成 free-form failure reasoning 后构造训练数据）、判别式 process（step-level binary PRM 驱动 PPO）、生成式 process（对每步生成 critique + refined action 后 SFT）。请独立判断。

## 输出格式

Markdown 表格行（不含表头），七列：

| 列 | 内容要求 |
|---|---|
| 引用标识 | 如 [Bai22b] |
| 标题 | 英文原文 |
| 关键思想与方法 | **4–6 句**，中文撰写，专业名词保留英文。需覆盖：(1) Evaluator 是什么、产出什么形态的 feedback；(2) 该 feedback 通过什么训练机制进入 Policy（写清关键设计，不要只写方法名）；(3) Policy 在什么维度上获得提升；(4) 如有 iterative / co-evolution 结构，描述迭代方式。 |
| 粒度 | outcome / process / outcome+process |
| 形态 | 判别式 / 生成式 / 判别式+生成式 |
| 领域 | 如 reasoning (math)、web、GUI / computer-use、code、embodied、dialogue / chat、safety / alignment、general 等 |
| 备注 | 仅在以下情况填写，否则留空：(a) 对粒度或形态判定不确定；(b) 论文可能不属于 P6；(c) 出现组合取值，说明情况。 |

## 执行要求

- 基于论文全文判断，不要只看 abstract。
- 信息不足时不要猜，在备注里写明并给出倾向判断。
- 多篇论文按给出顺序各输出一行，行间不插入额外文字。
- 只根据论文实际内容总结，论文没提的写「未明确」。
