# CSUR Survey 写作规律分析报告

> **分析材料**：4 篇 ACM CSUR 风格 Survey（均使用 acmart 模板）：
> 1. *A Survey on Inference Optimization Techniques for Mixture of Experts Models*（MoE 论文）
> 2. *A Survey on the Optimization of Large Language Model-based Agents*（Agent Opt 论文）
> 3. *Generalizability of Large Language Model-Based Agents: A Comprehensive Survey*（Generalizability 论文）
> 4. *Prompting Frameworks for Large Language Models: A Survey*（Prompting 论文）

---

## A. CSUR Survey 的核心特质

CSUR reviewer 看重的不是文献数量，而是**分析框架的自洽性**：taxonomy 必须对全文起到组织作用，而非仅作为分类练习。每篇被录用的论文都有一个"本文是第一个系统化研究 X 的 survey"的明确声明——这个声明必须被具体证据支撑，而非泛泛而言。

所有 4 篇论文共享一个核心写作哲学：**先定义边界，再填充内容**。Introduction 必须完成 scope 声明（包含什么、排除什么），否则 reviewer 会质疑 survey 的系统性。

CSUR 要求的分析深度远超文献罗列——每个子类别的结束处必须有"跨篇对比"或"趋势总结"，表格和图表要能独立传达信息而非仅辅助正文。

---

## B. 六个维度的横向分析

### 维度 1：宏观结构与章节逻辑

#### 普遍规律

**4 篇论文的章节序列高度一致**，遵循以下模式：

```
Introduction
  └─ Background / Fundamentals（技术前置知识）
       └─ Taxonomy 章节或在 Introduction 中直接呈现分类树
            └─ Core 章节组（每章对应 taxonomy 的一个分支）
                 └─ Datasets / Evaluation / Applications（验证性内容）
                      └─ Challenges & Future Directions
                           └─ Conclusion
```

**具体分布**：
- MoE 论文：Background（1节）+ Core（3节：Model / System / Hardware）+ Future（1节）≈ 结构最清晰，三级 taxonomy 直接映射为三章
- Agent Opt 论文：Background + Core（2节：Parameter-driven / Parameter-free）+ 支撑内容（Frameworks、Datasets、Applications）+ Challenges
- Generalizability 论文：Architecture（定义框架）+ Measure（度量）+ Improve（3个子方向）+ Framework-vs-Agent（特殊分析层）+ Conclusion
- Prompting 论文：Background + Survey Overview + Taxonomy + Comparisons + Related Tools + Future

**各章篇幅占比的普遍规律**（基于章节数量估算）：
- Introduction：约 8–12%（CSUR 的 Introduction 远比顶会论文长）
- Background/Fundamentals：约 5–10%
- Core taxonomy 章节：约 55–70%（主体）
- Challenges & Future Directions：约 10–15%（远比顶会长）
- 其他（Conclusion、Datasets 等）：约 5–10%

**Taxonomy 章节的位置与功能**：

4 篇论文中，taxonomy 都不是独立章节——它要么在 Introduction 中就以图/树的形式预呈（MoE 论文在 Introduction 中直接给出全局分类树 Figure 1，覆盖所有文献），要么在第一个核心章节的开头以 definition + framework 的方式给出。其功能是**结构性的，而非装饰性的**：后续每个 section 标题直接呼应 taxonomy 的某一节点。

原文证据：
- MoE 论文 Introduction："We propose a taxonomical framework that categorizes optimization approaches into model-level, system-level, and hardware-level optimizations... as illustrated in Figure 1." → 随后 Section 3、4、5 直接对应这三层
- Agent Opt 论文 Introduction："we categorize methods into parameter-driven and parameter-free optimization strategies" → Section 3、4 对应
- Generalizability 论文 Introduction 的 Contributions 部分："We introduce a structured taxonomy that covers both measurement and improvement" → 后续章节完全按此展开

**章节之间的逻辑递进机制**：

CSUR 论文不是将各章"并列陈述"，而是构造**逐步深入的逻辑链条**。常见两种机制：

1. **System-stack 递进**（如 MoE）：Model level → System level → Hardware level，每层的问题不能被上层解决，形成"向下深入"的逻辑
2. **分析维度递进**（如 Generalizability）：先定义概念（Architecture）→ 再度量（Measure）→ 再改进（Improve）→ 最后对比（Frameworks vs. Agents），形成"问题–度量–方法–反思"的闭环

#### 与顶会论文的对比

| 维度 | CSUR | NeurIPS / ACL / CVPR |
|------|------|----------------------|
| 章节数量 | 7–10 章 | 4–6 节 |
| Background 章节 | 独立成章，详述前置知识 | 通常融入 Introduction 或 Related Work |
| Related Work | 独立处理 + 显式对比矩阵 | 单独一节，1–2 页 |
| Future Directions | 独立章节，1500–3000 词 | 最后一段，100–300 词 |
| Taxonomy | 全文骨架，每章对应一个节点 | 仅用于 Related Work 分类 |

---

### 维度 2：Introduction 的论证结构

#### a) 领域重要性的建立方式

**普遍规律**：第 1–2 段，以具体产品/模型名称 + 具体能力 + 引用统计数据建立重要性，不做泛泛声明。

原文例句：
- MoE："Models like GPT-4, Claude, and Gemini have achieved remarkable performance in tasks ranging from natural language understanding to complex reasoning and code generation."（第1段）
- Prompting："Since the release of ChatGPT, which attracted widespread social attention... resulting in a number of amazing products such as PaLM, GPT-4, and LLaMA."（第1段）
- Agent Opt："LLMs... have achieved remarkable success, demonstrating exceptional capabilities in language understanding, reasoning, planning and complex decision-making."（第1段）

**修辞手段**：用已知的、读者认可的系统（GPT-4、Claude、ChatGPT）作为锚点，再从锚点引出本文关注的问题。不用数据统计，用"社会影响"类表述。

#### b) 现有研究"分散/不系统"的论证

**普遍规律**：用 2–3 段描述领域现状的具体问题，不用"existing works are insufficient"之类空洞声明，而是列举**具体的技术局限**。

原文例句：
- Agent Opt："however, these approaches often require extensive training, rely on well-defined state and action spaces, and struggle with generalization across diverse tasks."（段落中间，不在段末）
- MoE："the dynamic nature of expert activation patterns introduces complexity in resource management and scheduling that is not present in traditional dense models."（具体到"not present in traditional dense models"）
- Generalizability："First, a key obstacle is the lack of a standardized, universally accepted framework to define the boundaries of agent generalizability."（在 Challenges subsection 中，直接点出问题是"缺乏标准化框架"而非泛泛说"研究不足"）

**有说服力的关键**：不是说"previous works didn't do X"，而是解释"why X has been hard to do"——说明问题难度，说服 reviewer 这不是前人疏忽，而是确实存在技术壁垒。

#### c) 现有 Survey 局限的表达方式

**普遍规律**：4 篇论文都有独立的"Comparison to related surveys"段落或小节，不在正文中散布对前人的批评。

原文例句：
- Agent Opt（独立加粗小节）："While LLM-based agents have attracted increasing attention, existing surveys primarily focus on general LLM optimization or specific agent components such as planning, memory, and multi-agent coordination. However, they do not treat LLM-based agent optimization as a distinct research topic."
- Generalizability（独立 subsection，含 3 个加粗子段）："Existing surveys have broadly examined agent performance in terms of accuracy, security, privacy, and fairness. However, generalizability has received limited attention. In particular, there are a) no formal definition of agent generalizability, b) no established benchmarks for fair, standardized comparisons, and c) no comprehensive summary of methods aimed at improving it."
- MoE："While there are related surveys on LLM efficiency and MoE architectures, our work is the first to specifically focus on inference optimization techniques for MoE models."
- Prompting："there is currently a lack of but an urgent need of systematic literature and standardized terminology for introducing and comparing these tools"

**不贬低前人的技巧**：只说"they focus on X, but not Y"，不说"they are wrong"或"they are incomplete"。Generalizability 论文最精准：先承认前人的贡献（"broadly examined... in terms of accuracy, security, privacy, fairness"），再指出本文的独特角度（"generalizability has received limited attention"）。

#### d) Contribution 的引出方式

**普遍规律**：在 scope 声明之后，以"Our contributions are as follows"或"We make the following contributions"引出 bullet list，通常 3–5 条，每条以动词（"We present", "We introduce", "We categorize"）开头。

原文例句：
- Agent Opt："**Our key contributions** can be summarized as follows: (1) We present a comprehensive survey... (2) We categorize optimization methods... (3) We summarize widely used open-source frameworks, evaluation, datasets..."
- Generalizability：5 条 contributions，每条均以"It is the first to..."或"It provides the first..."开头，强调"首次性"
- Prompting："we make the following main contributions: We introduce the concept of Prompting Frameworks... We categorize the existing Prompting Frameworks into 3 classes... We conduct extensive research beyond the scope..."

**高频句型**：
- "To the best of our knowledge, this is the first systematic review dedicated to..."
- "We propose a [formal definition / taxonomy / framework] for..."
- "We provide a comprehensive survey... and discuss current challenges and future directions."

#### e) Scope 边界的声明方式

**普遍规律**：所有 4 篇论文都有独立的 scope 声明段落（有时以加粗方式标注），明确说明包含和排除的内容。

原文例句（Agent Opt，最规范）：
"**Scope and rationales.** (1) We survey only LLM-based agent optimization methods aimed at enhancing agent capabilities... We exclude works centered on general LLM efficiency, role-playing, or dialogue; (2) Our selection includes papers from top AI and NLP conferences and journals, as well as recent high-impact arXiv preprints...; (3) We focus on studies since 2022..."

Prompting 论文相对弱：scope 隐含在 taxonomy 的四个特性定义中（modularity、abstraction、extensibility、standardization），没有明确说"我们不包含 X"。

**CSUR reviewer 关注的是**：scope 是否包含了论文的纳入标准（哪些文献被选入、时间范围）、是否明确了排除项。

#### f) Roadmap 段落

**普遍规律**：每篇论文的 Introduction 最后一个段落必然是 roadmap，句式固定：

"The remainder of this paper is organized as follows. Section X provides/presents/introduces [content]. Section Y describes/discusses [content]. Section Z reviews [content]. Finally, Section N concludes the paper."

4 篇论文的 roadmap 段落均为这种固定格式，无例外。Agent Opt 论文附加了一张 Figure（paper organization 的树状图），作为视觉版 roadmap。

---

### 维度 3：Taxonomy / Framework 的构建与辩护

#### 分类轴的选择与辩护

4 篇论文的分类轴都经过显式辩护，不是直接声明。

**辩护方式 1（架构层次轴）**：MoE 论文以"系统栈"为轴，辩护是隐式的——模型级/系统级/硬件级对应不同的工程抽象层次，读者无需说服就能接受。

**辩护方式 2（机制维度轴）**：Agent Opt 论文以"是否修改参数"为轴，辩护是显式的："Parameter-driven optimization refers to adjusting LLM parameters... In contrast, Parameter-free... aim to improve agent behavior without modifying model parameters." 轴的选择基于**工程决策层面的本质区别**，而非表面特征。

**辩护方式 3（交互模式轴）**：Prompting 论文以"与 LLM 交互的方式"为轴："Taking into consideration the technical features, design objectives, and application scenarios... different types of prompting frameworks manifest this enhancement effect from different perspectives." 然后对 LLM-SH / LLM-LNG / LLM-RSTR 三类做区分。

**辩护方式 4（分析对象轴）**：Generalizability 论文以"度量维度"和"改进对象"为双轴，辩护来自形式化定义的推导："We evaluate agent generalizability across four dimensions of increasing difficulty: instruction-level, task-level, environment-level, domain-level."（直接从定义推导出分类轴）

**核心规律**：CSUR 要求的辩护是"为什么用这个轴比其他轴更好"，不是"这个轴是什么"。Agent Opt 和 Generalizability 论文做到了，MoE 论文和 Prompting 论文则依赖隐式共识。

#### 正交性与模糊边界的处理

4 篇论文都处理了分类的模糊性，但方式不同：

- MoE 论文：直接承认同一技术（如 HOBBIT）同时出现在多个子类中（Expert Prefetching + Expert Caching + Expert Loading），通过分析其"主要功能"决定归类。
- Prompting 论文（最直接）："it is important to note that these three types of prompting frameworks are often compatible with each other... multiple different categories of prompting framework can be used in parallel within the same task-solving process."——主动说明非正交性，并论证这不影响分类有效性。
- Generalizability 论文：通过形式化定义的精确性来保证正交性（4个维度 instruction/task/environment/domain 被明确区分）。

#### Taxonomy 图的功能

4 篇论文的 taxonomy 图均非装饰性——它是**文献地图**（直接在图中标注文献引用）+**章节导航**（图的结构直接映射为章节结构）。

原文证据：
- MoE 论文 Figure 1（全局分类树）：树的每个叶节点直接列出对应文献的 cite key，图的三个分支对应后续 3 个 section 标题
- Agent Opt 论文：Figure（paper organization）直接标注每个方格中论文采用的方法类别
- Prompting 论文：Table 1（Representative Works of Prompting Frameworks）按分类列举代表性工作，表格直接在正文分类讨论中被引用

**CSUR 的标准**：taxonomy 图必须是"可操作的"——读者看完图就能定位任何具体工作在 survey 中的位置。

#### 与顶会论文的对比

| 维度 | CSUR | 顶会 Related Work |
|------|------|-------------------|
| 分类轴 | 明确选择 + 显式辩护 | 通常无辩护，直接分组 |
| 覆盖范围 | 力求穷举，包含所有主要工作 | 选择性引用支持本文观点的工作 |
| 图表 | 文献地图，直接标注引用 | 偶尔有示意图，不标注具体文献 |
| 边界模糊性 | 显式说明并处理 | 通常忽略 |

---

### 维度 4：文献综述——综合分析 vs. 流水账

#### 平衡"覆盖广度"与"分析深度"的机制

4 篇论文的核心策略：**分层处理**。粗粒度分类用表格覆盖，细粒度分析用正文展开。

原文证据：
- MoE 论文：Table 1 用一张表格覆盖 20+ SoTA MoE 模型的技术参数（Parameters, Experts, Layers, Heads 等），让正文从技术参数比较中解脱，专注于分析**技术趋势**（"chronological progression from 2022 to late 2024 demonstrates increasing model sizes and architectural sophistication"）
- Agent Opt 论文：Table（Fine-Tuning 对比，30+ rows）覆盖所有方法的数据来源、过滤方式、微调策略、基础模型，让正文专注于**机制分析**而非枚举
- Prompting 论文：通过 capability matrix 图（所有 frameworks × 所有 dimensions）覆盖所有比较，正文专注于每个维度的**总结性判断**（以 tcolorbox 方框标注）

#### 10+ 篇论文的子节组织方式

所有 4 篇论文均使用**机制聚类**而非时间顺序：

- MoE 论文 Expert Offloading 节：按 Expert Prefetching → Expert Caching → Expert Loading → CPU Assisting 分小节，每小节收录 5–10 篇论文，按"机制关键点"而非"发表时间"排序
- Agent Opt 论文 Fine-Tuning 节：按 Trajectory Construction（generation + filtering + MA + LQ 4个维度）→ Fine-Tuning Approach 分层描述
- Generalizability 论文 Datasets 节：按环境类型（Navigation / Household / Web / OS）分组，每组内 3–5 篇论文

**机制聚类的优点**：读者能看到同一机制的不同实现之间的对比，而非孤立地看每篇论文。

#### 分析性断言 vs. 描述性陈述的比例

4 篇论文中，分析性断言约占 30–40%，描述性陈述占 60–70%。**关键不是比例，而是分析性断言的位置**——它们集中出现在：
1. 每个小节的**最后 1–2 句**（总结性断言）
2. 表格的**caption 或注释**中
3. 直接对比两种方法时的**对比句**

原文例句（分析性断言）：
- MoE："Fiddler achieves a significant speedup compared to other systems, as it effectively utilizes the CPU to assist computation in GPU-limited environments."（Table caption，给出 why）
- Agent Opt："SFT enhances task alignment by adjusting model responses to specific instructions, but is limited in its ability to cultivate the complex reasoning processes and adaptive behaviors required for agent-like performance."（分析 SFT 的限制）
- Generalizability："The key distinction is that: a generalizable framework with fine-tuning data for any scenario can enable the agent to achieve high accuracy on that specific scenario, but may not on other scenario different from the fine-tuning dataset. In contrast, a generalizable agent can achieve consistent accuracy across different scenarios"（直接的对比性分析断言）

#### 表格、对比矩阵的功能

- **能独立传达信息**：MoE 论文的性能对比表（Speedup、Metric、Baseline、Main Techniques）即使不读正文也能理解各方法的相对优劣
- **必须依赖正文**：Prompting 论文的 capability matrix 需要正文解释每个维度的含义，但图本身作为"全景参考"仍有独立价值

**普遍规律**：表格至少要包含一列"主要机制/核心特点"（而非仅堆叠数字）才能真正服务于分析。

#### 与顶会论文的对比

| 维度 | CSUR | 顶会 Related Work |
|------|------|-------------------|
| 篇幅 | 每个核心章 10–25 页 | Related Work 节 1–3 页 |
| 表格 | 30+ 行的系统对比表 | 偶尔有 5–8 行的小表 |
| 分析深度 | 有机制对比、代价-收益权衡 | 主要是"某某做了 X，某某做了 Y" |
| 总结判断 | 每个子节末尾给出 takeaway | 通常没有子节级别的总结 |

---

### 维度 5：Challenges / Future Directions 的写法

#### 与 Taxonomy 的对应关系

**普遍规律**：4 篇论文的 Challenges 节都从 taxonomy 的某个层次**自然导出**，不是独立列举。

- MoE 论文（最系统）：Future Directions 按"3 个基础维度"组织（Computing Infrastructure / Operational Requirements / Development Ecosystem），对应 taxonomy 的三个层次（Model/System/Hardware）的跨层挑战
- Agent Opt 论文：5 个 challenges 对应 taxonomy 的 5 个关键缺口（算法适应性、评估标准化、效率约束、安全鲁棒性、多智能体优化）
- Generalizability 论文：3 个 future directions 精确对应 Introduction 中提出的 3 个 challenges（标准化框架 → 度量与改进方法 → framework 与 agent 的区别）——首尾呼应
- Prompting 论文：Future Directions 的 5 个方向（streamlined / secure / versatile / standardized / organic ecosystem）对应 Limitations 节中指出的 5 类问题

#### 每个 Challenge/Future Direction 的内部论证结构

4 篇论文中，较强的 challenge 写法遵循以下结构：
**问题陈述 → 为什么难（技术壁垒）→ 已有尝试及其不足 → 具体的研究方向**

原文例证（Generalizability，最完整）：
- 问题陈述："Novel Architectural Frameworks for Component Coordination"
- 为什么难："Current systems typically rely on the backbone LLM to directly orchestrate heterogeneous modules, which can limit generalizability."
- 具体方向："We propose investigating central coordination units that manage interactions across these components of different configurations, resolve incompatibilities, and optimize information flow."

对比（Prompting 论文，较弱）：
- 仅有方向性描述（"More streamlined"、"More secure"），无"为什么现在做不到"的论证

#### Future Directions 的具体程度

MoE 和 Generalizability 论文的 future directions 更接近**可操作的研究问题**：
- MoE："the development of specialized circuits for expert routing... Memory hierarchies optimized for sparse parameter access... neuromorphic computing systems with their inherent support for sparse, event-driven computation"（具体到硬件类型）
- Generalizability："A hierarchical domain-task ontology... could leverage established industry classification systems such as the North American Industry Classification System (NAICS)"（具体到使用哪种已有分类系统）

Prompting 论文的 future directions 较泛：
- "The next-generation prompting framework should be more streamlined, more secure, more versatile, and more standardized"（没有技术路径）

**结论**：具体可操作的 future directions（含技术方向而非仅方向词）更有说服力，在 CSUR 中更常见于技术性强的 survey。

---

### 维度 6：高频写作模式

#### 过渡句模板（章节/小节之间）

**章节开头定位句**（说明本章在全文中的位置）：

1. "In this section, we discuss how [method category] methods improve the performance of [object]. Specifically, we categorize these methods into [N] main [technical approaches] according to [classification criterion]."
   —— Agent Opt，§3 开头

2. "This section introduces the [X] and ecosystem context of [object]. We begin by [task 1], describing [content]. We then discuss [task 2], identifying [content]. Finally, we examine [task 3], to highlight [content]."
   —— Generalizability，§2 开头

3. "[X]-level optimizations aim to [goal] through [mechanism]. These optimizations can be broadly categorized into [N] main areas: [list]. [Topic 1] focuses on [content], while [Topic 2] aims to [content]. [Topic 3] concentrates on [content]. Figure X illustrates the detailed taxonomy of [X]-level optimization that is described in this section."
   —— MoE，§3/4/5 开头模式

4. "After [elucidating / introducing / providing] [content from previous section], in this section, we [present / provide / introduce] [this section's content]."
   —— Prompting，多处过渡

**小节/子节之间过渡**：

5. "Beyond [single/individual] [settings], [method] extends these principles to [broader settings]."
   —— Agent Opt，§2.1 到 §2.2 的过渡

6. "In addition to [technique A discussed above], [technique B] presents another approach..."
   —— MoE，Expert Offloading 子节之间过渡

#### 比较性表达模板（A 与 B 的区别）

1. "**Comparison with [related concept].** [Related concept] focuses on '[description A]', aiming to [goal A]. In contrast, [this paper's concept] addresses '[description B]', emphasizing [goal B]."
   —— Agent Opt："Comparison with LLM parameter optimization. Parameter-driven LLM optimization focuses on 'how to create a better model'... In contrast, LLM-based agent parameter optimization addresses 'how to better use the model to solve complex agent tasks'"

2. "The key distinction is that: [A] can [positive aspect of A], but may not [limitation of A]. In contrast, [B] can [advantage of B], especially [specific condition]."
   —— Generalizability："The key distinction is that: a generalizable framework with fine-tuning data for any scenario can enable the agent to achieve high accuracy on that specific scenario, but may not on other scenario different from the fine-tuning dataset. In contrast, a generalizable agent can achieve consistent accuracy across different scenarios, especially those that differ from its fine-tuning dataset."

3. "In summary, in terms of [comparison dimension], [A] surpasses [B], which in turn surpasses [C]."
   —— Prompting（tcolorbox 中）："In summary, in terms of compatibility with programming languages, LLM-SH surpasses LLM-RSTR, which in turn surpasses LLM-LNG."

#### Limitation 表达模板

1. "Although [method] can [positive aspect], [specific limitation], limiting [consequence]."
   —— Agent Opt："although advanced reasoning models can enhance decision quality, their integration typically increases inference depth and cumulative token cost, limiting the practicality of deploying LLM-based agents in demanding operational environments."

2. "Existing mitigation strategies... have practical limitations. [Approach A] can [problem of A]; meanwhile, [Approach B] may not be feasible due to [specific constraint]."
   —— Generalizability："Existing mitigation strategies... have practical limitations. Prompting can increase inference latency and is sensitive to prompt structure; meanwhile, fine-tuning may not be feasible due to model accessibility constraints, lack of component-specific training data, or the risk of catastrophic forgetting."

3. "While [method] demonstrates [positive result], this method is highly dependent on [precondition], which reduces its flexibility... and may negatively affect [metric]."
   —— MoE："However, this method is highly dependent on the profiled dataset, which reduces its flexibility across different environments and may negatively affect accuracy."（关于 EdgeMoE 的 limitation）

#### Contribution 声明模板

1. "To the best of our knowledge, this is the first [survey/systematic review] dedicated to [specific topic]. It [provides / introduces / examines] [specific contribution]."
   —— Agent Opt："This is the first survey on LLM-based agent optimization techniques, facilitating a clearer understanding and comparison of existing methods and providing directions for future research."

2. "While [existing work] has broadly examined [topic], our survey offers a more comprehensive and structured treatment of [specific angle]."
   —— Generalizability："While several recent surveys have addressed aspects of LLM-based agents, they fall short in several key areas. This survey offers a more comprehensive and structured treatment of generalizability in LLM-based agents, addressing notable gaps across three dimensions."

3. "We [propose/introduce/present] a [taxonomical/formal/structured] framework that categorizes [objects] into [N categories]. This framework provides a [structured approach / comprehensive overview] and identifies [key challenges / promising research directions]."
   —— MoE："We propose a taxonomical framework that categorizes optimization approaches into model-level, system-level, and hardware-level optimizations... This framework provides a structured approach to understanding and comparing different optimization techniques."

---

## C. 推荐写作框架（通用 Outline）

以下基于 4 篇分析论文归纳，适用于 CSUR 55–75 页长文：

```
§1 Introduction                              [约 8–10%篇幅]
   1.1  领域重要性 + 具体问题的引出           [2–3 段]
   1.2  现有方法的技术局限（非泛泛批评）       [2–3 段]
   1.3  现有 Survey 的 gap（独立段落）         [1 段或加粗小节]
   1.4  本文 taxonomy 的核心思路 + 图/树       [1 段 + Figure 1]
   1.5  Scope & Rationales（明确纳入/排除标准）[1 段，可加粗标注]
   1.6  Contributions（bullet list，3–5 条）   [1 段 + list]
   1.7  Paper Organization（roadmap）          [1 段]

§2 Background / Preliminaries               [约 5–8%篇幅]
   核心功能：确保读者具备后续章节所需前置知识
   不是做文献综述，而是定义本文使用的概念、符号、基础模型结构

§3–(N-2) Core Taxonomy Chapters             [约 55–65%篇幅]
   每章对应 taxonomy 的一个分支
   章节开头：重申该层/该类别在 taxonomy 中的位置
   章节结构：子分类定义 → 代表性方法介绍（含表格）→ 跨方法对比分析
   每个子节末尾：总结性断言（趋势、优劣权衡）
   
§(N-1) Datasets / Evaluation / Applications [约 5–8%篇幅]
   （可选，视 survey 类型决定是否包含）
   不只是列举数据集，要分析各数据集对 survey 主题的覆盖盲点

§N Open Challenges & Future Directions      [约 10–13%篇幅]
   每个 challenge 对应 taxonomy 中的一个未解决问题
   内部结构：问题描述 → 技术难点 → 已有尝试及不足 → 具体研究方向
   
§(N+1) Conclusion                           [约 2–3%篇幅]
   简短：2–4 段，重述 taxonomy、主要发现、意义
   不引入新内容，不重复 Future Directions 的细节
```

**二级标题建议**：

| 章节 | 二级标题类型 | 核心功能 |
|------|------------|----------|
| Introduction | 1.3 Comparison with Related Surveys | 区分本文与前人 Survey 的差异 |
| Introduction | 1.5 Scope and Rationales | 明确 survey 边界 |
| Core Chapters | X.Y.Z Method A | 每个方法或方法类别的深度分析 |
| Core Chapters | X.Y Performance/Summary | 跨方法对比与总结 |
| Challenges | N.M [Challenge Name] | 每个 challenge 独立小节 |

---

## D. 高频句型与过渡模板汇总

### D.1 章节开头定位句

**场景：章节开头，说明本章在全文中的位置**
> "[X]-level optimizations aim to [goal] through systematic improvements in [mechanism 1], [mechanism 2], and [mechanism 3]. These optimizations can be broadly categorized into [N] main areas. [Area 1] focuses on..., while [Area 2] aims to..., [Area 3] concentrates on.... Figure X illustrates the detailed taxonomy that is described in this section."

**场景：章节开头，以比较引入**
> "Comparison with [related concept]. [Related concept] focuses on '[description A]', aiming to [goal A]... In contrast, [this section's concept] addresses '[description B]', emphasizing [goal B] in [domain]."

### D.2 比较性表达

**场景：对比两类方法的根本区别**
> "The key distinction is that: [A] [positive result], but [limitation]. In contrast, [B] [advantage], especially [condition]."

**场景：对比多类方法的排序关系**
> "In summary, in terms of [dimension], [A] surpasses [B], which in turn surpasses [C]."

**场景：说明两个概念的差异，避免混淆**
> "The distinction lies in the fact that [concept A]... emphasizes [aspect A]. On the other hand, [concept B]... focuses on [aspect B]."

### D.3 Limitation 表达

**场景：承认某方法局限，不显得主观**
> "Although [method] can [positive], [specific condition] can [negative consequence], limiting [downstream impact]."

**场景：对比已有工作的局限**
> "Existing [approaches / mitigation strategies]... have practical limitations. [Approach A] can [problem A]; meanwhile, [Approach B] may not be feasible due to [specific constraint], [specific constraint], or [risk]."

**场景：指出某方法的适用边界**
> "While [method] demonstrates [positive result], this method is highly dependent on [precondition], which reduces its flexibility... and may negatively affect [metric] under [condition]."

### D.4 Contribution 声明

**场景：声明"第一个"**
> "To the best of our knowledge, this is the first [systematic review / comprehensive survey] dedicated to [specific topic]."

**场景：区分本文与前人 survey**
> "While [prior survey / prior work] has broadly examined [topic] in terms of [aspect 1, aspect 2], our survey focuses specifically on [angle], introduces the first [definition/taxonomy], and proposes [structured taxonomy / method]."

**场景：用三段式声明贡献**
> "We [verb] a [type] [framework / survey / analysis]... This [noun] provides [value] and identifies [key contribution]."

### D.5 子节总结句（位于子节末尾）

**场景：总结一组方法的共同趋势**
> "These advancements highlight the [potential / trend] of [technique] to [achievement], improving [agents' / models'] [capability] in [setting]."

**场景：指出某类方法的关键开放问题**
> "Addressing [challenge] holds the potential to substantially enhance [property] of [object] across [diverse / complex / heterogeneous] environments."

### D.6 Future Direction 写法

**场景：引出一个 future direction**
> "We see promising opportunities in developing [specific method type] that [achieve X]. Current systems [limitation]. We propose investigating [approach] that [mechanism], [mechanism], and [mechanism]."

**场景：结束 future directions 段落，给出更大意义**
> "Addressing these [architectural / methodological] challenges by [approach] holds the potential to substantially enhance [property] and more broadly, [higher-level property], of [object] across [complex / diverse] environments."

---

## E. CSUR 关键质量信号（按重要性排序）

1. **Taxonomy 是否是全文的骨架**：若 taxonomy 图与章节结构不对应，reviewer 会认为论文缺乏系统性（最高优先级）

2. **"第一篇"声明是否被证据支撑**：必须有具体的 related survey 对比段落，证明本文角度与前人不同；空洞声明会被直接质疑

3. **Scope 边界是否明确**：必须说明哪些工作被包含、哪些被排除、时间范围——没有边界声明的 survey 会被认为不系统

4. **贡献与 related surveys 的 gap 是否对应**：Introduction 中 identified 的 gap 必须在 contributions 中逐一被填补，否则会被认为论文承诺了但没有兑现

5. **Future Directions 是否来自 taxonomy 的自然导出**：独立列举的 challenges 没有来自 survey 分析的证据支撑，会被认为是空洞展望

6. **表格是否能独立传达核心对比**：如果表格的信息量不足以区分各方法（如只有名称没有维度比较），reviewer 会认为文献综述的深度不够

7. **每个子节是否以分析性断言结尾**：只描述不分析的子节会被认为是"literature listing"而非"survey"

---

## F. 三个最常见的致命错误

### 错误 1：Taxonomy 与章节结构脱节

**表现**：论文在 Introduction 给出了一个 taxonomy（比如分为 A/B/C 三类），但后续章节按照完全不同的顺序或粒度组织（比如按照 X/Y/Z 分章），导致 taxonomy 图悬空，没有任何章节直接对应。

**为何致命**：CSUR reviewer 会认为 survey 缺乏系统性框架，taxonomy 只是装饰，论文实质上是文献罗列。

**改正方向**：先确定 taxonomy，再设计章节结构，二者必须一一对应。MoE 论文是最好的反面参考——taxonomy 的三个节点直接成为 Section 3/4/5 的标题。

---

### 错误 2：Related Survey 对比的缺失或虚弱

**表现**：只有一句话说"existing surveys focus on X but not Y"，没有具体列出哪几篇 survey、它们各自的 focus 是什么、在哪个具体维度上与本文不同。

**为何致命**：这是 CSUR 最高频的 reject 原因之一。Reviewer 无法判断本文是否真的填补了 gap，还是重复了已有工作。

**改正方向**：用 Generalizability 论文的三段式结构——每段用加粗 header 标明一个维度，每段先承认前人贡献，再指出本文独特的角度，并具体列出哪几篇前人 survey 没有涵盖的内容。

---

### 错误 3：Future Directions 与 Survey 内容脱节

**表现**：Challenges 节中列举的研究方向来自对领域的宏观判断，而非从 survey 正文中被 identified 的具体问题推导而来；或者 Future Directions 只有方向词（"more efficient"、"more robust"）而无技术路径。

**为何致命**：CSUR 定位是"通过综述发现规律、提出系统性方向"，而非只是整理文献。脱节的 Future Directions 让 reviewer 认为论文的分析没有产生洞见。

**改正方向**：每个 future direction 必须有对应的正文证据——某个问题在某个子节中被反复提及但没有好的解决方案，才应该出现在 Challenges 节中。参考 Generalizability 论文：Introduction 中明确说了 3 个 challenges，Conclusion 的 Future Directions 一一对应，形成完整的论证闭环。

---

## 写作检查清单

### 结构完整性（8条）

- [ ] Introduction 中是否有独立的"Comparison with Related Surveys"段落或小节，而非分散在正文中？
- [ ] Introduction 中是否有明确的"Scope and Rationales"声明，含纳入标准、排除项、时间范围？
- [ ] Taxonomy 图是否在 Introduction 或 Taxonomy 章节中出现，且图中直接标注了代表性文献引用？
- [ ] 每个 Core 章节的标题是否与 taxonomy 图中的节点直接对应？
- [ ] Introduction 的 roadmap 段落是否完整覆盖所有章节（"Section X presents... Section Y discusses..."）？
- [ ] Challenges & Future Directions 章节是否独立成章（而非作为结论的一个段落）？
- [ ] Conclusion 是否简短（2–4 段），不引入新内容，不重复 Future Directions 的细节？
- [ ] 论文是否有 Survey Methodology/Overview 节，说明文献搜集方法（搜索词、数据库、筛选标准）？

### Taxonomy / Framework 质量（6条）

- [ ] Taxonomy 的分类轴是否给出了显式辩护，而非直接声明？（"我们使用 X 轴，因为..."）
- [ ] 对于分类边界模糊的案例，是否有显式说明并给出处理方式？
- [ ] Taxonomy 图是否是"文献地图"（叶节点包含具体文献引用），而非仅有类别名称？
- [ ] 每个 Core 章节开头是否重申该章在 taxonomy 中的位置？
- [ ] 是否有至少一处显式对比，说明"为什么选择这个分类轴而不是其他常见轴"？
- [ ] Formal Definition（如果给出）是否与 taxonomy 的分类逻辑保持一致？

### 文献综述深度（8条）

- [ ] 每个子节涉及 10+ 篇论文时，是否采用机制聚类（而非时间顺序或随机枚举）组织？
- [ ] 是否有至少一张大型对比表（10+ 行、多维度），覆盖该类别中的主要方法？
- [ ] 对比表中是否至少有一列描述"核心机制/主要技术"（而非只有数字指标）？
- [ ] 每个子节是否以分析性断言（而非描述性陈述）结尾？
- [ ] 对比不同方法时，是否使用了"X 与 Y 的区别在于..."的分析句式，而非"X 做了..., Y 做了..."的并列描述？
- [ ] 是否避免了"流水账"式的逐篇摘要（即不出现"Paper A proposes..., Paper B presents..., Paper C introduces..."的连续列举）？
- [ ] 是否对主要技术趋势给出了时间演进的描述（"early work / recent work / emerging direction"）？
- [ ] 表格和图是否可以独立传达核心对比信息，无需完全依赖正文？

### 写作规范性（6条）

- [ ] Contribution 声明中是否至少有一条使用了"To the best of our knowledge, this is the first..."句式？
- [ ] 所有 Limitation 表达是否避免了主观性批评（如"previous work is incomplete"），改用"focuses on X but not Y"句式？
- [ ] Future Directions 中的每个方向是否有具体的技术路径（而非仅有方向词如"more efficient"）？
- [ ] 相关 survey 对比段落是否先承认前人贡献，再指出本文独特角度（而非直接批评前人）？
- [ ] 每个章节是否有开头定位句（说明本章在全文 taxonomy 中的位置）和结尾总结句（给出该章的 key takeaway）？
- [ ] Introduction 中 identified 的所有 gap 是否都在 contributions 中被对应的贡献填补（一一对应关系是否清晰）？
