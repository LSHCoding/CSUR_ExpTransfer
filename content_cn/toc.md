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

下面 Survey 中涉及的一个小节，以及和这个小节对应的论文，你需要找到这个小节对应的论文，每个论文用 1～2 描述其关键思想和方法（可以放在 Survey 的正文中使用，输出为中文，专有名词仍然使用英文）。不能只看论文的标题和摘要，要读论文的内容。我给的论文，虽然是人工筛选的，但是也并不完全确实 100% 是匹配的。