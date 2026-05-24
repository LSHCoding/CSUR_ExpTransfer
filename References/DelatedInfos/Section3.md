
# 3.1.2

Hindsight Trajectory Rewriting [Hu25] 从单条失败轨迹经 hindsight rewriting 重写出针对可达替代目标的合成成功 workflow，写入 replay buffer，当同一目标出现更短更优版本时 buffer 会替换旧条目。

Learning on the Job [Yan25d] 把长程交互分别转成 strategic memory 的 dilemma-strategy 对、procedural memory 的 SOP 与 tool memory 的操作提示，任务后统一做 refinement、integration 与 deduplication。

**Narrative Abstraction 边界案例。** 一些技能或过程库的结构化、多模态程度更高，处在 Narrative Abstraction 与 Schematic Formalization 的边界。SkillX [Wan26] 构建 planning、functional、atomic 三层 SkillKB，经 merge、filter 与 exploratory expansion 持续优化，其 functional 与 atomic 层的结构化程度明显更强。Skill Set Optimization [Not24] 从 actor 历史中抽取高价值 subtrajectory，概括成带 subgoal 与编号指令的 skill，skill set 依实际 observed value 被持续筛除与替换。Memp [Fan25] 同时容纳 verbatim trajectory 与 abstract script 两种形态的 procedural memory，在成功或失败后执行 add、adjust、delete，并可把新旧信息合成 revised memory。GUI-explorer [Xie25] 为每次状态转移抽出 visual key 与对应 textual operational value，当 key 匹配而 value 足够不同时把新值并入旧条目，产物是带视觉键的多模态条目，但复用仍靠阅读。Get Experience from Practice [Fen25] 把多轮 interaction trace 总结为高层 procedural experience、低层执行 experience 与配套 check function，低层项可直接转为 API 调用或脚本，这部分明显带可执行性，与纯 Narrative artifact 有距离、接近 Schematic Formalization。

# 3.1.3

经验来源以 Agent 自生成轨迹为主。MemGovern 取自人类修复记录、Wu26 取自 teacher 合成 traces 属于例外。经验来源与 Static/Dynamic 的划分正交，不改变 pathway 归属。多模态以正交属性形式进入 Narrative Abstraction：REFLECT 处理机器人多模态观测流，GUI-explorer [Xie25] 与 Mirage-1 [Xie25b] 的技能条目带视觉键——这些工作并未因模态不同而走单独路径，只在各自类别内呈现实现差异。

# 3.2.1

Skill-Pro [Mi26] 的 artifact 形态是自然语言而非代码，但仍归入本类：它从成功失败轨迹通过 hindsight attribution 抽取 semantic gradient，聚合为 skill 候选后再经 PPO-style trust-region gate 检验其 counterfactual advantage 是否足够，产物是 activation condition、execution procedure、termination condition 三元组，下游 Agent 在 Skill-MDP 中先选中一个 skill 再由冻结 LLM 在其约束下生成 primitive action。它是一个整体可选、可启停的动作单元，这一调度地位而非代码形态决定了它属于 skill。

PSN [Shi26] 与 AutoRefine [Qiu26] 的 artifact 跨越 skill 与 workflow 两类语义功能。PSN 把 skill 表示为带 executable control flow、precondition、postcondition 与 CHILDREN 调用关系的 symbolic program，Agent 在 skill network 上做 backward-chaining 规划，并利用持续 execution trace 驱动 failure credit assignment、局部补丁、冗余合并与在线 structural refactoring。AutoRefine 跨成功失败轨迹做对比抽取，产物分为 Skill Pattern（带步骤的自然语言 guideline 或 code snippet）与 Subagent Pattern（带独立 system prompt、reasoning loop 与内部 memory 的 specialized subagent，经 hierarchical delegation 使用），后者功能更接近 workflow 中的子任务调度。

# 3.2.4 Boundary Cases and Scope Clarification

上述三子类内已标注若干跨语义功能的工作：PSN 与 AutoRefine 跨 skill 与 workflow，MOBIMEM 跨 workflow 与 graph，Environment Maps 与 BrainMem 跨 graph 与其他功能。这些工作均给定单一主归属，不重复展开。其中 BrainMem 的 semantic guideline 蒸馏属 Narrative Abstraction，是真正横跨 Narrative Abstraction/Schematic Formalization 的工作。

**Hybrid schematic-narrative artifact。** 一些方法将轨迹总结为 workflow、SOP 或 guideline，artifact 表面带字段或编号，但下游消费仍主要依赖 LLM 自然语言理解、无 parser 或 graph traversal 介入——这类方法更接近 Narrative Abstraction。Agent KB [Tan25] 从多种 agent framework 的异构轨迹构建跨域经验库，experience unit 同时含 structured predicate 与 narrative text，带 self-evolving memory（新条目加入、LLM ranker 去重、基于 recency/frequency/transfer success 的 eviction），按结构形态属弱 Schematic Formalization，作为 hybrid 边界文献处理。

**Non-agent / human-software-trace 来源。** 一批工作从人类使用软件的低层事件流构建 workflow。From Logs to Agents [Jo26] 从创意软件的 raw system trace 重建 creative workflow DAG；In-Context Ensemble Learning [Xu24b] 从 human demonstration video 聚合出 SOP；Workflow Graphs [Cha20] 从人类 3D 建模 trace 构建 W-graph。这三者的源数据是人类软件使用记录而非 LLM agent 的交互轨迹，目标偏向过程理解与文档化，不纳入 Schematic Formalization 主 taxonomy。Cha20 的 W-graph 作为方法学前身、Jo26 与 Xu24b 作为 workflow 重建的外延参照，可在相关讨论中引用。需区分的是 Project_Infos 允许的 {human} 来源：Agent Workflow Memory 的离线人类标注经验、A2Flow 的 expert demonstration 仍属 Schematic Formalization，因为其示范本身具备决策过程语义与异构动作空间。判定排除与否，看的是源数据是否承载序贯决策语义，与来源是人类还是 agent 无关。

**Source-side ambiguity。** 某些工作生成 code、workflow 或 graph，但 artifact 并非从具体轨迹提炼，而是模型据任务描述、专家知识或参数化能力直接生成。这类更接近 Parametric Externalization 或一般的 program/workflow synthesis，不计入 Schematic Formalization。

**Composite pipeline。** 一些系统先把 trajectory 转为 Schematic artifact，再将其用于数据合成、SFT 或 RL。若论文核心贡献是从经验到参数的内化、Schematic artifact 仅作中间表示，归入 §7 Composite 或 Tokenized-to-Parametric pathway。Schematic Formalization 章节可引用它们说明 Schematic artifact 的中介作用，但不作为纯 Schematic Formalization 方法。