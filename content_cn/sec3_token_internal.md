

# Tokenized-to-Tokenized Transformations

## Narrative → Narrative


### Single-Trajectory Extraction
- 核心特点：基于单个 session 轨迹来提取 token-level 的经验。一个 session 可以有多轮的action。给定一条交互轨迹，LLM 可以从中提取出不同类型的经验：知道哪里错了，下次该怎么做的纠错型经验；具有条件结构的指导型经验；降低上下文占用的压缩型经验；


**纠错型经验**

- 核心特点
- 代表工作：
  - Reflexion：读取一条 episode 的 trajectory + feedback signal（标量或自由文本），LLM 生成一条 verbal reflection 存入 episodic buffer。
  - CLIN：每次 trial 后，从单条交互轨迹中更新因果抽象记忆（而非通用"helpful hints"）。
  - ReAP：从单个 web navigation trajectory（成功或失败）中生成 self-reflection
  - REFLECT：从单次机器人失败的多传感器观测（多模态数据），生成该次执行对应的分层摘要，然后再用 LLM 去做失败解释与纠错计划。
  - R2D2：Remember paradigm 重建 web 环境减少导航错误；Reflect paradigm 从错误中学习改进策略


- Reflexion: language agents with verbal reinforcement learning
- CLIN: A Continually Learning Language Agent for Rapid Task Adaptation and Generalization
- Reflection-Based Memory For Web navigation Agents
- REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction
- R2D2: Remembering, Replaying and Dynamic Decision Making with a Reflective Agentic Memory

**指导型经验**
- 核心特征：






### Cross-Trajectory Induction


### Discussion


## Narrative → Schematic


LLM 直接提取
- Agent Workflow Memory
- 



