先给出一版修改后的，我确定后再编辑到文件中。

关于Section 5 部分涉及的论文，其相关总结（大模型总结的）在

针对段落：
```
Structured Memory Graph Construction 把 Agent trajectory 中的实体、关系、状态变化、空间结构、事件依赖或交互历史转化为可检索、可遍历、可更新的图结构记忆。这类方法的目标不是生成可执行动作，也不是归纳任务流程，而是构建 Agent 对环境、任务世界、历史经验或多智能体交互关系的结构化表示。Agent 的许多经验不适合表达为线性文本或固定流程，而更适合组织为关系结构：环境对象间有空间关系，动作会改变状态，历史事件间有时间或因果联系，多智能体交互中存在角色、信息流与依赖。若这些关系仅以 raw log 或自然语言 note 存储，后续 Agent 难以做精确检索、局部更新与多跳推理。

AriGraph [Ano24] 从每步 textual observation 抽取 semantic triplet 加入 semantic memory，同时把完整 observation 作为 episodic vertex 与当步 triplet 相连，形成同时编码世界知识与情节历史的 knowledge graph world model，环境状态变化时删除被推翻的旧关系。G-Memory [Zha25] 面向多智能体系统，把协作中的 atomic utterance 组织为 interaction graph，把整次 query 实例化为 query node，再由 LLM 总结出 insight node，形成 interaction/query/insight 三层图，支持按 query 做上下双向 traversal。A-MEM [Xu25b] 把每次交互转成带 keyword、tag、contextual description 与 embedding 的 atomic note，通过 link generation 在新旧 note 间建立语义关系，新经验触发对旧 note 的重写。MobileGPT [Lee23] 通过 Explore-Select-Derive 流程把 mobile app 已完成任务转写为 task/sub-task/primitive action 层级，并把页面与子任务关系组织为 transition graph（节点为功能等价的 app page，边为可复用 sub-task）。Environment Maps [Fen26] 把 browser trace、DOM 与 screenshot 编译为 JSON 环境地图，含 context node、parameterized action node、workflow order 与 tacit knowledge。BrainMem [Ma26] 在 embodied 场景维护 Trajectory KG（action-state transition）与 Spatial KG（room-object 空间关系）双图，episode 结束后由 Experience Agent 把成功轨迹提炼为 generalizable pattern、失败轨迹经 guided retry 压缩为 symbolic guideline。

Structured Memory Graph 与 Procedural Workflow 的区别在图的语义功能：workflow graph 回答"任务应如何执行"，节点与边表示步骤顺序、控制流或任务依赖；memory graph 回答"环境中有什么、状态如何变化、历史经验间有什么关系"，节点与边表示实体、状态、事件、空间或交互关系。这类方法的优势是支持关系级别的记忆复用，图结构便于局部更新，适合 embodied agent、web agent 与多智能体系统的 long-horizon planning 与 state tracking。困难是图抽取容易产生错误实体与错误关系，图记忆随时间增长出现 memory bloat、过时信息与 retrieval noise，通常需配套 graph update、conflict resolution、pruning 与 confidence estimation。
```

我的意见：
1. “实体、关系、状态变化、空间结构、事件依赖或交互历史转化为可检索、可遍历、可更新的图结构记忆”，举了几个例子，可能会有一些语义上的重复。
2. “这类方法的目标不是生成可执行动作，也不是归纳任务流程” 感觉可以去掉
3. “Agent 的许多经验不适合表达为线性文本或固定流程，而更适合组织为关系结构：环境对象间有空间关系，动作会改变状态，历史事件间有时间或因果联系，多智能体交互中存在角色、信息流与依赖。” 这句感觉和第一句的内容有部分重复。可能需要再思考一下该怎么写。
4. 工作描述段 的英文感觉还是有点太多了。另外，每篇论文的描述长度都差不多，都比较详细。可能还是需要详略得当一些。可能不是每一篇都需要描述，我不知道是不是有一两篇可以合并在一起来描述，就是一句话内包含两个工作的描述，这两个工作的机制可能是类似的。
5.  最后一段话可以移到3.2.4的Discussion部分。

你有意见也可以提出。

注意：**独立评估**：从客观、专业的角度判断该修改意见是否合理。不要迎合我的立场，给出有依据的理由（逻辑、学术规范、表达效果等）；

我准备为 3.1 和 3.2 分别设计一个表格，这个表格是对对应部分论文的一个归纳、汇总。设计一下这两个表格的表头。


整体上挺好的，但是我觉得这两个表都少一列，就是 检索的方式。从经验库中检索到合适的经验对 narrative 的经验非常重要。