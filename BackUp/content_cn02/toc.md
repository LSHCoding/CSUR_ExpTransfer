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


现在，我准备重写一下 5.1 这部分的内容。我准备准备借助大模型来帮助我快速的读论文。我已经有 5.1 这部分的论文列表了，并且有也有相关的论文全文。我希望大模型能够读对应的英文，并对每篇论文以表格格式进行总结，每篇论文的总结包括论文的标题、2～3句描述其关键思想和方法（详细一点）、粒度（outcome/process 粒度）、产物（scalar/non-scalar 产物）、领域。你帮我写一下提示词，特别是其中的分类轴要写清楚。

下面是改好的提示词。三处都按你说的调了:产物在"关键思想与方法"里展开说明、那一列整体加详、去掉单篇限制并相应改了批量输出的措辞。

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

下面是待阅读的论文：

