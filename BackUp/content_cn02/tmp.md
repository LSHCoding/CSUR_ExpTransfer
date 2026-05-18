
1. Agent KB 我感觉不属于目前这个子类，暂时去掉。剩下的两个边界组我觉得是属于目前这个之类的。
2. 把这 9 篇再整理成一个更“CSUR 正文风格”的小段落版。不同的论文之间要有逻辑的组织，并且采用“先总述，后逐类点名”的风格。

理论上，程序性结构的技能是不属于这 Narrative 的，而是 Schematic。但是很多论文混用了各种名称，比如 skill 这些（造成同一个名字，实际的指代物不一样；或者实际上同一个东西，但是名字叫法不一样）。但是目前根据我的判断，它们产物的程序性结构还不够强，所以我是仍然归入了 Narrative。你在表述的时候，可以弱化一下程序性、结构化这些词。

1. 我不建议按照产物来分。
2. 我觉得一二组的区别就是，第一组更强调成功和失败的对比，第二组则是从多条轨迹归纳（没有强调成功和失败的对比）。两者是平行的关系，没有谁比谁好。

整理成一个更“CSUR 正文风格”的小段落版。不同的论文之间要有逻辑的组织（不建议按照产物来分），并且采用“先总述，后逐类点名”的风格。


在当前 project 的所有文献中，还有没有能匹配当前主题的论文？

我觉得适合当前子类的论文有：

将这15篇论文的标题，以Markdown无序列表的形式输出。

将强相关的这几篇论文，以表格的形式，给出每篇论文可直接写进正文的描述 （ 1～2 句描述其关键思想和方法）。表格有 2 列，标题和 可用于正文的 1到2 句描述（对于再次搜索的部分，你目前的这个总结描述太简略了）。

将应纳入强相关的这些篇论文，以表格的形式，给出每篇论文可直接写进正文的描述 （ 1～2 句描述其关键思想和方法）。表格有 3 列，标题、匹配程度 和 可用于正文的 1到2 句描述（对于再次搜索的部分，你目前的这个总结描述太简略了）。

整理成一个更“CSUR 正文风格”的小段落版。语气统一、长度更接近正式综述稿（中文版）。不同的论文之间要有逻辑的组织，并且采用“先总述，后逐类点名”的风格。重点关注强匹配的论文，弱化边界匹配的论文。

将强相关的这些篇论文的标题，以Markdown无序列表的形式输出。



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

已知转化路径

以下 7 条为前期梳理的基础单路径，用新 Carrier 术语表述。多模态作为正交属性编织入每条路径，不开辟独立路径。多模态场景下可能涌现的新路径需保持开放探索。

1. **Narrative → Narrative**（intra-tokenized abstraction）：raw logs → reflections / rules / summaries / insights。同层语义抽象，源与目标都是 Narrative Tokenized。
2. **Narrative → Schematic**（intra-tokenized formalization）：logs → code / workflows / SOPs / graphs。同层形式化。
3. **Tokenized → Latent**（latent compression）：raw trajectories → KV cache / soft prompts / continuous memory tokens。跨层压缩。
4. **Tokenized → Parametric (Evaluator)**（evaluator internalization）：trajectories → RM / PRM / verifier / judge。经验固化为评估能力。
5. **Tokenized → Parametric (Policy)**（policy internalization）：trajectories → policy weights via SFT / RL。经验固化为决策能力。
6. **Parametric (Evaluator) → Parametric (Policy)**（preference alignment）：RM 信号 → policy weights via RLHF / DPO。参数间转化。
7. **Parametric → Tokenized**（knowledge externalization）：权重 → synthetic trajectories / demonstrations。隐式经验外化为显式载体。

**复合路径（Composite Pipelines）的处理**：区分两种情况——

- **单篇论文中偶现的两条相对独立的转化**（例如一篇论文顺带做了 raw → reflection 与 raw → policy 两件彼此独立的事）：在对应的单路径 Section 分别引用相关片段。
- **单篇论文将多路径链式组合作为整体方法**（例如 Narrative Tokenized → Schematic Tokenized → Parametric、Tokenized → Latent → Parametric、或 Policy → Raw → Policy 的自生成环路）：这类工作的贡献点恰在路径间的衔接机制（integration mechanism），而非任一 pathway 本身。此类工作在独立的 **Composite Pipelines Section** 作为 first-class 对象 anatomy，重点分析 integration mechanism、以及 compose 相对单路径的优缺点。

从当前项目的所有文献中，先找出 和 主题是 Survey 相关的论文，从中筛选出和 Tokenized → Parametric (Evaluator) 相关的论文。查看一下相关的 Survey 都是如何对 Tokenized → Parametric (Evaluator) 进行分类和分析的。

