# 1. Introduction

LLM 的应用形态已经从单次响应用户 query 的静态生成器,扩展到了能够在外部环境中持续行动的自主 Agent:调用工具检索信息、操控浏览器完成任务、与其他 Agent 协同完成复杂工作流等。LLM-Based Agent 在感知—决策—执行—观察的闭环中运作,持续产生大量交互记录——推理链、工具调用、环境观测、人类反馈。这些记录是 agent 改进自身决策能力的原始材料,可形式化为四元组 $e = (c, a, o, f)$——分别对应每一步的决策上下文、agent 输出、环境反馈与(可选的)评价信号。社区已围绕"如何将这些原始材料转化为可复用的形式"发展出一系列机制:记忆摘要将原始轨迹提炼为自然语言反思;技能归纳将成功轨迹转化为可复用的代码;soft prompt 训练将经验压缩为连续隐空间表示;奖励建模将人类偏好标注固化为参数化评估器;轨迹微调将筛选后的成功轨迹固化为策略权重;RLHF 将评估信号内化为策略权重的决策偏好。

但当构建 Agent 系统时,真正要面对的问题往往横跨这些机制:同样一份成功轨迹,该提炼成可检索的反思笔记,还是训练成可挂载的 soft prompt?同样要让 Agent 掌握一项能力,该用轨迹微调直接固化到权重里,还是保留为外部可审查的记忆条目?答案分散在 Memory、Post-training 等子领域的文献中——按"组件"(Memory / Planning / Tool Use)或"技术"(RAG / SFT / RLHF)切分的现有分类体系都不直接回答这些问题。

这些机制是同一类操作的不同实例:它们都对经验的表示方式进行了转化,从而在可解释性、推理效率、可编辑性等维度上重新做权衡。考虑同一份成功的 agent 交互轨迹:最直接的做法是把它作为 few-shot 示例放进 prompt——这是经验的直接使用,代价是每次复用都要占用 context 窗口。记忆摘要将这段轨迹提炼为更精炼的反思或规则,仍保留为可读、可编辑的自然语言,但语义密度大幅提升,占用的 context 显著缩减。轨迹微调则将这段轨迹直接训练进模型权重,推理时不再占用任何 context,但是经验从此难以单独审视和逐条修改。记忆摘要、技能归纳、奖励建模、轨迹微调、自生成训练等机制都可以读作这种操作在不同源载体与目标载体之间的实例。我们将这种操作称为 Experience Transformation。

不同的 transformation 路径在不同的载体之间展开。我们按"经验在模型架构中的存在层次"将载体分为三大类:

- Tokenized 载体:以离散 token 序列形式显式进入模型前向传播的经验。内部按形式化程度分为 Narrative(自然语言形式的反思、摘要等)与 Schematic(代码、工作流、知识图谱等结构化形式)两子类。
- Latent 载体:以连续向量或 hidden state 形式存在,直接参与 attention 或 hidden-state 计算的中间表示。
- Parametric 载体:经验固化在神经网络权重中的隐式表示。内部按功能角色分为 Policy(生成 action 的 actor 权重)与 Evaluator(评估 trajectory 的判断器权重)两子类。

这三类载体之间的迁移构成了本文的分析主线。我们将散落在记忆、技能归纳、对齐、自训练等子领域的机制系统化为七条基础转化路径:

- Narrative Abstraction(Narrative → Narrative):同载体内由原始轨迹提炼出反思、规则、摘要等更精炼的自然语言形式。
- Schematic Formalization(Narrative → Schematic):自然语言经验转化为代码、工作流、知识图谱等可符号化执行或图遍历的结构。
- Latent-Space Transformation(Tokenized → Latent):离散 token 形式的经验转化为直接参与模型前向计算的连续向量。
- Evaluator Internalization(Tokenized → Evaluator):轨迹经验固化为参数化的评估能力,如 reward model、process reward model、verifier。
- Policy Internalization(Tokenized → Policy):轨迹经验固化为策略权重的决策能力。
- Evaluator-Driven Optimization(Evaluator → Policy):评估器信号吸收为策略权重中的生成偏好。
- Parametric Externalization(Parametric → Tokenized):隐式权重经验外化为新的 token 化轨迹。

此外,我们识别出将多条基础路径组合的复合模式(composite pipelines),并将其作为独立分析对象。

本文填补了已有综述未覆盖的分析维度。Agent 架构综述按 Memory、Planning、Tool Use 等系统组件梳理 agent 架构,但同一类经验转化操作会跨越这些组件的边界——例如轨迹微调既不属于 Memory 也不属于 Planning,在组件视角下无处安放。记忆系统综述深入刻画 Tokenized 载体内部的存储、检索与遗忘机制,但不讨论经验跨载体的迁移。对齐综述聚焦 Evaluator → Policy 这一条路径上从 RLHF 到 DPO 及其变体的技术演进,过程奖励模型综述集中于 Evaluator 载体本身的设计与训练。这些工作各自在系统架构、单一载体、或单一技术家族内提供了纵深覆盖,但没有任何一篇将经验在不同载体之间的转化作为独立分析维度。本文以经验转化为轴心建立统一分析框架,核心贡献如下:

- (待定)
- (待定)
- (待定)

后续章节安排:Section 2 建立概念体系,Sections 3-6 按源载体类型分组展开七条单路径的文献分析,Section 7 讨论复合路径,Section 8 做跨路径综合与利用分析,Section 9 讨论开放问题与未来方向。
