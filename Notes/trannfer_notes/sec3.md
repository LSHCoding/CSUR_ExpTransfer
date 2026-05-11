分析的维度：
- online VS offline
- static experience VS dynamic update experience
- dynamic： 当初持续追加 vs 追加+修改之前的
- human feedback VS Agent feedback VS environment feedback
- 线性提取 VS 层次性提取
- 单条轨迹中学习、多条轨迹中学习
- Single Agent 提取、Multi Agent 提取
- 直接提取、带反馈的提取、有强化学习的提取、基于贝叶斯的提取

因果 Experience
类强化学习、贝叶斯后验
符号主义

从失败中学习、正 + 负、直接从 case 中



Memory 的多层次设计 与 检索
经验的沉淀和复用
Agent 的架构

Experience 用于指导 reasoning
Memory 用于记住和检索



我选择用方案B，5类

我的一些意见：
1. 编译器/过程挖掘范式 这些论文先为待定论文，不参与分类
2. 检索机制作为转化，看起来不像是本篇 Survey 的范畴，也先列为待定论文，不参与分类
3. 纯 Benchmark 论文不纳入分类

和方案 A 相比，我感觉方案 B 很好一些。但是我也有些问题（客观的和我讨论，不要迎合我的想法）：
1. 我看到，即使同一个论文也会被分为 2 类里面，比如 SkillClaw，SSO。大概是这些论文确实涉及到 2 种或更多的转化操作。我倾向于用论文主打的卖点来决定最终归属，你感觉怎么样？
2. 另外，每一个大类，之类的分法，你还要再仔细琢磨一下。

我的意见：
1. Skill-Pro 归 M5
2. M4.1（环境反馈）暂时不拆
3. AutoSkill 归到 M2，MemSkill归 M4
4. 接受这种不均匀

现在完整的输出一遍我们讨论的结果，以及论文的分类，要求如下：
1. 你要给出每个大类和子类的中英文名字（最好有一定的对称性，同时让人一看就知道是什么意思）
2. P1 和 P2 分开输出
3. 每个大类输出：名字，驱动力、核心特征，对应工作的子分类表、子类的共性机制、对应工作的论文标题。下面是一个大类的示列
4. 这些内容以 markdown 格式输出在文件夹 `Section3` 中，文件名是 ` Section3_Taxonomy.md`
5. 待定，以及 benchmark 的论文，按类别放在文件的最后面

这个示例只是一个形式，内容不一定对。

```
M1 — 提示驱动的直接提取（Prompting-Based Direct Extraction）

驱动力：LLM 的内部推理能力。 无外部反馈循环，无跨轨迹统计，无验证步骤。转化机制即 LLM 在单次（或少量）推理 pass 中阅读轨迹并输出变换后内容。

核心特征：如果 prompt 和 trajectory 不变，输出就确定；质量完全依赖 LLM 的归纳推理能力。

| 子类 | 代表工作 |
| :--- | :--- |
| 逐条轨迹反思 | Reflexion, CLIN, ReAP, R2D2, REFLECT, Generative Agents |
| 条件化指南/规则提取 | AutoGuide, AutoManual, MPR, NEMORI |
| 上下文/系统提示工程 | ACE, Atlas (Compiled Memory), VCC |
| 多模态反思 | ICAL (VLM 反思阶段), ViReSkill |
| 摘要/压缩 | WebCoach (WebCondenser), M² (Dynamic Trajectory Summarization), AndroTMem, HiAgent, MemGPT |

M1.1 纠错型反思（Corrective Reflection）——提取"哪里做错了、下次怎么做"的经验教训，输出自然语言反思文本
M1.2 规程型提取（Procedural Extraction）——提取"在什么条件下做什么"的指导性知识，输出条件化规则/指南/playbook
M1.3 压缩型摘要（Compressive Summarization）——以降低上下文长度为首要目标，保留决策关键信息
M1.4 多模态反思（Multimodal Reflection）——输入或输出涉及视觉等多模态

论文：
1. Reflexion: language agents with verbal reinforcement learning
2. CLIN: A Continually Learning Language Agent for Rapid Task Adaptation and Generalization
...
...

```

