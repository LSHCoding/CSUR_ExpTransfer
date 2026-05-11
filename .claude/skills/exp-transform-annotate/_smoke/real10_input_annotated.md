[Title]: A-MEM: Agentic Memory for LLM Agents
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: 历史 LLM agent 的 raw memories（任务交互记录）
- [Target Experience]: Zettelkasten-style 知识网络——节点是带 structured attributes（contextual descriptions、keywords、tags）的 NL 笔记，节点间有动态建立的相似性链接
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 知识网络支持 dynamic indexing 与 grounded retrieval；新 memory 加入还会触发 historical memories 的 attribute 更新（"memory evolution"），让网络持续 refine 自身表示
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 每次新 memory 加入时，LLM 生成 comprehensive note，附 structured attributes（NL 描述 + keywords + tags），并 analyze 历史 memories 找出 meaningful similarities、建立链接，构成 interconnected knowledge network。提取过程的迭代逻辑：每次新 memory 加入触发 network-wide refinement；过滤准则是相似性（"meaningful similarities exist"），具体相似度度量摘要未明示。结构产物（带 tag 的节点 + 链接）符合 §2.2.3 中 knowledge graph / sentence graph / structured library 的 Schematic 特征，故归为 P2。

[Title]: ABot-Claw: A Foundation for Persistent, Cooperative, and Self-Evolving Robotic Agents
- [Pathway]: Annotation Failed
- [Mechanism]: Abstract 描述的是 embodied agent 的系统架构集成方式（embodiment interface + multimodal memory + critic-based feedback），未刻画任何具体的 source-experience → target-carrier 转化管道。multimodal memory 标榜 "persistent context retention and grounded retrieval"（属于 N-Tok 的原始存储 + 检索机制，不构成 Transformation）；generalist reward model 用于 online evaluation，但摘要未说明该 RM 是否从 agent 经验训练而来；"self-evolving" 为宣传性表述，机制层面无具体证据。

[Title]: AFlow: Automating Agentic Workflow Generation
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: 工作流候选执行后的 raw execution feedback（rollout trace + reward signal）+ 跨轮累积的 tree-structured search experience
- [Target Experience]: 优化后的 code-represented workflow（LLM-invoking nodes + edges 构成的 DAG）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 优化后的 workflow code 在 agent 推理时直接调度执行，使小模型在特定任务上以 GPT-4o 4.55% 的成本超越其表现
- [Method]: ⟨MCTS⟩
- [Mechanism]: 把 workflow optimization 形式化为对 code-represented workflow 空间的搜索，MCTS 节点是 workflow 变体；rollout 时执行候选 workflow 并以 execution feedback 作为奖励信号；按 UCB 策略选择扩展节点，对 workflow code 做 iterative modification；tree-structured experience 跨轮累积，引导后续修改。源端是 rollout 阶段的 raw 执行经验（Narrative observations + reward），目标端是搜索末态的可执行 workflow 代码（Schematic），对应 P2 的 intra-Tokenized formalization。

[Title]: ALFWorld: Aligning Text and Embodied Environments for Interactive Learning
- [Pathway]: Annotation Failed
- [Mechanism]: Abstract 主体贡献是 simulator infrastructure（对齐 TextWorld 与 ALFRED）和 BUTLER 这一 demo agent。对 BUTLER 的训练机制（IL / RL）、数据来源、text→visual 的迁移是 weight-level transfer 还是 inference-time grounding，以及 modular pipeline（language understanding / planning / navigation / visual scene understanding）各部分是否经历独立训练，摘要均未说明。simulator 本身不构成 Transformation；BUTLER 的训练细节信息不足以支持 Pathway 判定，故标 Annotation Failed。

[Title]: ATLaS: Agent Tuning via Learning Critical Steps
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Expert trajectories（按"critical step"过滤后仅保留约 30%）
- [Target Experience]: Agent base LLM 的 policy 权重
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {human}
- [Utilization]: 微调后的 LLM 作为 generalist agent 在多种环境与任务中直接执行，保持 base LLM 通用能力同时提升 agent 任务表现
- [Method]: ⟨SFT⟩
- [Mechanism]: ATLaS 在常规 SFT 之前增加 critical-step 选择：在 expert trajectory 中识别 planning、复杂中间子任务推理、strategic decision-making 等"关键步骤"（具体识别方法摘要未明示），仅对这约 30% 步骤做 supervised next-token cross-entropy 微调；其余步骤被丢弃，避免 full-trajectory behavior cloning 带来的 expert bias 与 OOD 退化。监督信号来自 expert action token，损失为标准 SFT cross-entropy；优化目标是降低对 expert 全轨迹过拟合、提升跨环境泛化。critical-step 过滤是该方法的核心创新点，但因其本身只对原 trajectory 做子集选择而未生成新载体（不满足 §2.3 Embodiment 条件下的"独立目标载体"），故未将其拆为独立 Pathway，而归并入 P5 method 内部的数据构造机制。

[Title]: Act Wisely: Cultivating Meta-Cognitive Tool Use in Agentic Multimodal Models
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: 多模态 agent 的 rollout trajectories（含 accuracy reward 与 tool-usage 信号）
- [Target Experience]: 多模态 agent policy 权重（结果模型为 Metis）
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {self}
- [Utilization]: 训练后的 Metis 推理时按权重直接生成 tool-calling 决策，blind tool invocation 数量级地减少，同时推理准确率提升
- [Method]: ⟨RL: HDPO⟩
- [Mechanism]: HDPO 摒弃 scalarized reward（accuracy − λ·tool_use 的加权求和会陷入"过强抑制必要工具使用 vs. 被 advantage 方差淹没"两难），改为维持两条正交优化通道：(1) accuracy channel 在所有 trajectory 上正常优化任务正确性 advantage；(2) efficiency channel 仅在已经准确的 trajectory 子集内施加 tool-use penalty，做 conditional advantage estimation。两通道解耦让 agent 自然进入 cognitive curriculum——先掌握任务正确性，再精炼 tool-use 经济性。源经验为 self-generated rollouts，目标是 policy 权重，符合 P5 trajectories → policy 路径。
> New tag: ⟨RL: HDPO⟩ — 在 DPO 系偏好优化基础上引入双正交通道与 conditional advantage estimation 的变体；与 ⟨RL: DPO⟩（单通道偏好对齐）和 ⟨RL: PPO⟩（单通道 advantage 估计）在结构上存在判别性差异——HDPO 把"是否在 reward-positive 子集内"作为 advantage 估计的条件门控，复用既有标签会丢失这一双通道 + 条件门控特征。

[Title]: Agent Learning via Early Experience
- [Pathway]: Policy → Narrative → Policy
- [Source Experience]: 当前 policy 在线 rollout 出的 interaction data（"early experience"），含 (state, action, future_state) 元组；strategy 2 中还包含对 suboptimal actions 的 reflection
- [Target Experience]: 更新后的语言 agent policy 权重
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 训练后的 policy 在 8 个环境中 in-domain 与 OOD 都获得提升；在有可验证 reward 的环境中可作为后续 RL 的初始化基础（"bridge between imitation learning and fully experience-driven agents"）
- [Method]: ⟨SFT⟩
- [Mechanism]: 论文的核心贡献是"early experience"自生成环路——对应 Project_Infos.md §4 明示的 "Policy → Raw → Policy 自生成环路" 这条 composite，论文衔接机制的特色在于用 future state 替代 reward 作为闭环监督信号，从而摆脱对外部可验证奖励的依赖、扩展到 websites 等 reward-sparse 环境。摘要并列两条具体实现策略：
  · **Strategy 1（Implicit world modeling）**：当前 policy 生成 rollout（Policy → Narrative，对应 P7 形态的自生成）；(state, action, future_state) 元组作为 next-state-prediction-style 监督信号更新 policy（Narrative → Policy，对应 P5），构成 Policy → Narrative → Policy 闭环。
  · **Strategy 2（Self-reflection）**：当前 policy 生成包含 suboptimal actions 的 rollout（Policy → Narrative，对应 P7 形态的自生成）；agent 对 suboptimal actions 做反思（Narrative → Narrative，对应 P1 内部 refinement）；raw rollout + reflection 的合并经验作为监督信号更新 policy（Narrative → Policy，对应 P5），构成 Policy → Narrative → Policy 闭环（中间 Narrative 阶段含 P1）。
  两条策略并列共享同一闭环骨架，差异在中间 Narrative 阶段是否带 reflection refinement。

[Title]: Agent S2: A Compositional Generalist-Specialist Framework for Computer Use Agents
- [Pathway]: Annotation Failed
- [Mechanism]: Abstract 描述的是组合式推理架构——cognitive 任务分派给 generalist 与 specialist 模型，配合 Mixture-of-Grounding（GUI 定位）与 Proactive Hierarchical Planning（多时间尺度计划修正）两项推理技术。两项技术的训练 / 学习层面机制（specialist 模型从何而来、是否由 agent 经验训练）摘要均未说明。本质上是 inference-time 组合策略，未刻画 source-experience → target-carrier 的转化管道。

[Title]: Agent S: An Open Agentic Framework that Uses Computers Like a Human
- [Pathway]: Annotation Failed
- [Mechanism]: Abstract 提出 "experience-augmented hierarchical planning" 与 Agent-Computer Interface (ACI) 两项贡献。前者声称 "learns from external knowledge search and internal experience retrieval at multiple levels"，但 internal experience 以何种载体存储、是否经过形式化或抽象、retrieval 是 raw RAG 还是结构化 traversal——摘要均未明示。无法判定 experience 是否经历了 §2.3 双条件下的 Transformation，只能确认存在 retrieval 行为，故标 Annotation Failed 等待正文细节。

[Title]: Agent Workflow Memory
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: 过去 web navigation 任务的 raw trajectories（既覆盖 training examples 也覆盖 online test queries）
- [Target Experience]: Commonly reused routines / workflows（带步骤拓扑的 procedural template，library 形式存储）
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: workflow 按相似度 selectively 召回拼入 agent 后续生成的 prompt context，引导多步行动；offline 模式在训练集上预先 induce，online 模式在 test query 流中即时 induce
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: AWM 通过 LLM 对过去 trajectories 做 induction，提取"commonly reused"的子序列作为 routine（workflow），存入 workflow library；filter 准则是"common reuse"（频次或相似度，摘要未细化）。两种触发模式：offline 对 training set 全体 induce、online 在测试时增量 induce。注入方式为 selective prompting——根据任务相似度从 library 召回相关 routine 拼入 context。源是 raw 交互轨迹（Narrative），目标是带步骤拓扑结构的 workflow（Schematic Tokenized，按 Project_Infos.md §2.2.3 程序化产物归类即使以 NL 模板形式存在也属此），故归 P2；与 AFlow 同列，区别在 AFlow 用 MCTS 显式优化 code workflow，AWM 用 LLM induction 提取 NL workflow。

## New Tags Introduced
- ⟨RL: HDPO⟩ —— Hierarchical / dual-channel DPO 变体，维持 accuracy 与 efficiency 两条正交优化通道，efficiency 通道只在 accuracy-positive 子集内做 conditional advantage estimation；与 ⟨RL: DPO⟩（单通道偏好对齐）与 ⟨RL: PPO⟩（单通道 advantage 估计）存在判别性差异，复用任一既有标签会丢失"双通道 + 条件门控"特征。首次出现：「Act Wisely: Cultivating Meta-Cognitive Tool Use in Agentic Multimodal Models」

## Annotation Failures
- 「ABot-Claw: A Foundation for Persistent, Cooperative, and Self-Evolving Robotic Agents」（block #2）—— Abstract 为系统架构集成层面描述，未刻画 source-experience → target-carrier 的转化管道；reward model 与 multimodal memory 的训练 / 形式化机制信息不足。
- 「ALFWorld: Aligning Text and Embodied Environments for Interactive Learning」（block #4）—— 主体贡献为 simulator + benchmark；BUTLER agent 的训练方法（IL/RL）、数据来源、text→visual 迁移机制摘要均未说明。
- 「Agent S2: A Compositional Generalist-Specialist Framework for Computer Use Agents」（block #8）—— Abstract 仅描述 inference-time 组合推理架构（Mixture-of-Grounding、Proactive Hierarchical Planning），未涉及 carrier 间的训练或形式化转化。
- 「Agent S: An Open Agentic Framework that Uses Computers Like a Human」（block #9）—— "Experience-augmented hierarchical planning" 与 "internal experience retrieval" 的具体载体组织、形式化或训练机制摘要均未明示，无法判定是否构成 §2.3 意义下的 Transformation。
