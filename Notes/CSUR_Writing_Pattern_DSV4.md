# CSUR Survey 写作规律分析报告

> 分析对象：4 篇 ACM Computing Surveys (CSUR) 已发表/在审 Survey 论文
>
> 1. **MoE-Inf** — *A Survey on Inference Optimization Techniques for Mixture of Experts Models*
> 2. **Agent-Opt** — *A Survey on the Optimization of Large Language Model-based Agents*
> 3. **Agent-Gen** — *Generalizability of Large Language Model-Based Agents: A Comprehensive Survey*
> 4. **Prompt-FW** — *Prompting Frameworks for Large Language Models: A Survey*

---

## A. CSUR Survey 的核心特质

CSUR 偏爱的 Survey 不是"文献列表 + 简单归类"，而是一个**自洽的知识体系**：taxonomy 是全文的骨架而非装饰，每一章从 taxonomy 的一个分支展开，章节之间形成论证递进而非平行堆叠。Reviewer 最在意三件事：(1) taxonomy 的分类轴是否有显式辩护（为什么用这个轴而不是别的轴），(2) 文献综述是否有分析深度而非流水账（每 10+ 篇论文是否有统一的组织逻辑），(3) challenges/future directions 是否从前文的 gap analysis 中自然导出，而非凭空列举。一篇 CSUR 若缺少这三者中的任一，大概率被 major revision 或 reject。

---

## B. 六个维度的横向分析

### 维度 1：宏观结构与章节逻辑

#### 普遍规律

**1.1 典型章节序列与篇幅占比**

四篇论文的章节序列高度一致，可归纳为以下模板：

| 章节 | 典型占比 | 功能 |
|------|---------|------|
| Introduction (§1) | 8–12% | 建立问题、声明 gap、引出 taxonomy、列出 contribution、给出 roadmap |
| Background / Preliminaries (§2) | 8–15% | 定义核心概念、建立术语体系、为 taxonomy 提供概念基础 |
| Taxonomy + 主体分析章节 (§3–§N) | 50–60% | 按 taxonomy 分支展开文献综述，每章对应一个分类维度 |
| Challenges / Future Directions | 8–15% | 从前文 gap 导出 open problems |
| Conclusion | 3–5% | 总结核心发现 |

**原文证据：**

- MoE-Inf: `Introduction → Fundamentals of Mixture of Experts → Model-level Optimizations → System-level Optimizations → Hardware-Level Optimization → Future Directions and Open Challenges → Conclusion`
- Agent-Opt: `Introduction → Background → Parameter-driven Optimization → Parameter-free Optimization → Open-source Frameworks → Datasets → Applications → Challenges → Conclusion`
- Agent-Gen: `Introduction → LLM-based Agents and Ecosystems → Measuring Generalizability → Improving (LLM) → Improving (Components) → Improving (Interaction) → Generalizable Methods → Conclusion`
- Prompt-FW: `Introduction → Background → Survey Overview → State-of-the-art Prompting Framework → Related Prompting Tools → Comparisons and Challenges → Future Directions and Conclusion`

**1.2 Taxonomy / Framework 章节的位置与功能**

在所有四篇论文中，taxonomy 均在 Introduction 之后的第一个或第二个章节中出现，承担"全文导航地图"的功能：

- MoE-Inf：taxonomy 在 Introduction 中以 Figure 1 (forest tree) 呈现，随后 Section 2 (Fundamentals) 建立概念基础，Sections 3–5 严格按 taxonomy 的三层展开
- Agent-Opt：taxonomy 在 Introduction 中声明（parameter-driven vs. parameter-free），Section 3 和 Section 4 分别对应这两类
- Agent-Gen：taxonomy 在 Introduction 中以"三个核心挑战"的形式引出，随后各章对应：测量 → 改进（LLM层/组件层/交互层）→ 框架与 Agent 的关系
- Prompt-FW：taxonomy 在 Section 4 (State-of-the-art) 中以"三层分类 + 四层生命周期"的双重结构呈现

**关键规律：Taxonomy 不是独立的一章，而是 Introduction 的后半部分（贡献声明中）和主体章节之间的"铰链"。Introduction 提出分类逻辑，主体章节按分类展开。**

**1.3 章节间的逻辑递进机制**

四篇论文均非章节简单并列，而是使用以下显式机制建立递进：

**(a) Taxonomy 驱动的层级递进（MoE-Inf 最典型）**

从 model-level → system-level → hardware-level 是抽象层次从高到低的递进。Section 3 末尾埋下伏笔：
> "While model-level optimizations improve the inherent efficiency of MoE architectures, their practical deployment requires system-level support..."

**(b) 从"是什么"到"怎么测"到"怎么改进"的认知递进（Agent-Gen 最典型）**

Architecture (§2) → Measurement (§3) → Improvement (§4–6) → Framework→Agent translation (§7)。这是典型的"定义→评估→改进→反思"学术论证链。

**(c) 从"核心方法"到"辅助基础设施"到"应用"的范围递进（Agent-Opt）**

Parameter-driven (§3) → Parameter-free (§4) → Frameworks (§5) → Datasets (§6) → Applications (§7) → Challenges (§8)

**(d) 过渡句显式标记递进逻辑**

Prompt-FW 在 Section 3 (Survey Overview) 和 Section 4 (State-of-the-art) 之间使用：
> "By combining LLMs with the Prompting Framework, the limitations of LLMs can be mitigated to some extent, enabling the realization of more astonishing capabilities. Therefore, in this section, we provide a systematic and comprehensive definition..."

**1.4 跨所有论文的普遍规律总结**

1. **Background 章节从不缺席**：即使读者是领域专家，CSUR 也要求作者建立统一的术语和概念框架
2. **主体章节严格对应 taxonomy**：不存在"独立于 taxonomy 之外"的综述章节
3. **Challenges 放在结论之前**：形成"综述→反思→展望"的完整弧线
4. **Conclusion 短小精悍**：通常 2–4 段，只做总结不做新论证

#### 与顶会论文的对比

| 维度 | CSUR Survey | 顶会 Paper (NeurIPS/ACL/ICML) |
|------|-------------|------------------------------|
| 章节数量 | 7–9 个 numbered sections | 通常 4–6 个 sections |
| Background 章节 | 独立成章，8–15% 篇幅 | 通常融入 Introduction 或省略 |
| Taxonomy 位置 | 全文核心骨架，所有主体章节由此展开 | Related Work 中的简单分类（1–2 段） |
| 逻辑递进 | 多层递进（认知链/抽象层次/方法→应用） | 通常单线递进（问题→方法→实验） |
| Challenges 章节 | 独立成章，从前文 gap 导出 | 通常 1–2 段在 Conclusion 中 |
| Paper roadmap | 独立段落，通常带 Figure 引用 | 通常 1–2 句 |

**本质差异：CSUR Survey 的章节结构是"taxonomy 驱动的树状展开"，顶会 paper 是"方法驱动的线性论证"。CSUR 读者期望在任何时候都知道自己在 taxonomy 的哪个位置；顶会读者只关心"这个方法为什么有效"。**

---

### 维度 2：Introduction 的论证结构

#### 普遍规律：Introduction 的标准 6 步论证模型

四篇论文的 Introduction 均遵循一个高度一致的论证模板，每步有特定修辞策略：

#### a) 领域重要性的建立方式（第 1–2 段）

**策略：从宏观趋势下沉到具体技术瓶颈。**

- MoE-Inf 第 1 段：LLM 的成功 → 规模扩展带来的效率挑战 → MoE 作为解决方案
- Agent-Opt 第 1 段：AI agent 的历史演进 → LLM 作为 agent 的革命性能力
- Agent-Gen 第 1–2 段：LLM 的泛化能力 → agent 范式 → generalizability 的关键性
- Prompt-FW 第 1–2 段：ChatGPT 引发 LLM 革命 → "Pre-train, Prompt, Predict" 范式转移 → prompt 的核心作用

**共同特征：第一段从不直接进入本文主题，而是建立更大的领域语境。惯用句式是"X has emerged/revolutionized/demonstrated remarkable capabilities"。**

原文高频句式：
> "Large language models (LLMs) have revolutionized artificial intelligence, demonstrating unprecedented capabilities across various domains..." (MoE-Inf)
> "The development of autonomous agents has been a long-term pursuit in Artificial Intelligence (AI)." (Agent-Opt)
> "Large Language Models (LLMs) have demonstrated impressive capabilities across a broad range of tasks..." (Agent-Gen)

#### b) 现有研究"分散/不系统"的论证方式（第 2–3 段）

**策略：不是简单断言"缺乏系统综述"，而是具体指出分散的表现形式。**

- Agent-Gen 最为出色——指出 "studies often make inconsistent claims about generalizability, each using different levels of granularity"，然后给出具体例子："one agent may claim generalizability by performing object manipulation tasks across various indoor environments... another by executing similar tasks in both indoor and outdoor settings"
- Agent-Opt 指出 "existing techniques...fail to fully address the challenges of decision-making, long-term planning, and adaptability"
- MoE-Inf 指出 "a critical gap in the existing literature is the absence of a systematic framework for analyzing and developing comprehensive inference optimization solutions"
- Prompt-FW 指出 "the rapid pace of development...making it difficult to track and stay informed about the multitude of methods dispersed across GitHub, preprint papers, Twitter, and top conferences"

**关键规律：论证"分散"时必须给出具体证据——引用具体论文、具体数据集、具体评估维度来说明不统一之处，而非空泛地说"缺乏系统综述"。**

原文高频句式：
> "Although numerous recent studies have explored various strategies...a systematic review summarizing and comparing these methods from a holistic perspective remains lacking." (Agent-Opt)
> "Existing surveys often treat LLM-based agents as monolithic systems or focus exclusively on the backbone LLM, overlooking the role of agent specialized components..." (Agent-Gen)

#### c) 现有 Survey 局限的表达方式（专门的"Comparison to related surveys"段落）

**这是 CSUR Introduction 区别于顶会论文的最显著特征——几乎每篇都有一个独立段落或子节专门比较现有 survey。**

- Agent-Opt 使用粗体标签 `\textbf{Comparison to related surveys.}`：指出已有 survey "primarily focus on general LLM optimization or specific agent components...However, they do not treat LLM-based agent optimization as a distinct research topic"
- Agent-Gen 使用独立子节 `\subsection{Distinctions from Related Surveys}`：从三个维度（Formal Definition, Component-Level Analysis, Framework vs. Agent）逐一对比
- MoE-Inf 在 Introduction 末段嵌入："While there are related surveys on LLM efficiency and MoE architectures, our work is the first to specifically focus on inference optimization techniques"
- Prompt-FW 虽未设专门段落，但在其贡献列表中强调 "comprehensive and systematic survey"

**关键策略：不贬低前人，而是精确识别"他们覆盖了什么 + 他们没覆盖什么"。使用 "primarily focus on...however, they do not..." 结构而非 "failed to" 或 "neglected"。**

#### d) Taxonomy / Framework / Contribution 的引出方式

**策略：Taxonomy 在 Introduction 中作为 contribution 的核心部分被引入，而非等到正文中才出现。**

- Agent-Opt：`Specifically, \textbf{Parameter-driven Optimization} refers to...\textbf{Parameter-free Optimization} methods...`
- Agent-Gen：提出三个 challenges 作为文章的组织框架，然后将贡献一一对应到每个 challenge
- MoE-Inf：`We propose a taxonomical framework that categorizes optimization approaches into model-level, system-level, and hardware-level optimizations`
- Prompt-FW：`We define the lifecycle of the PF as a hierarchical structure, from bottom to top, namely: Data Level, Base Level, Execute Level, and Service Level`

**所有四篇都在 Introduction 中给出了 taxonomy 的核心分类轴。**

#### e) Scope 边界的声明方式

**策略：使用显式的范围声明段落，明确包含什么、排除什么。**

- Agent-Opt 使用粗体标签 `\textbf{Scope and rationales.}`：

> "(1) We survey only LLM-based agent optimization methods aimed at enhancing agent capabilities...We exclude works centered on general LLM efficiency, role-playing, or dialogue; (2) Our selection includes papers from top AI and NLP conferences and journals...; (3) We focus on studies since 2022..."

- Prompt-FW 通过定义 "four essential properties: modularity, abstraction, extensibility, and standardization" 来划定边界，并在 Section 5 (Related Prompting Tools) 中明确区分哪些工具 "do not possess all four fundamental characteristics"
- Agent-Gen 通过在 Introduction 中给出 generalizability 的 formal definition 来确立 scope 边界

**关键规律：Scope 声明越具体越好——明确时间范围（since 2022）、来源范围（top conferences + arXiv）、排除项（what is explicitly excluded）。**

#### f) Paper roadmap 段落的写法

**策略：每条 roadmap 条目对应一个 section，包含 section 编号 + 简短内容描述。**

- Agent-Opt：

> "\textbf{Organization of this survey.} The schematic layout of this manuscript is illustrated in Figure \ref{paper organization}. Section \ref{sec2} provides the background knowledge...Section \ref{sec3} systematically reviews...Section \ref{sec4} classifies...Section \ref{sec5} introduces...Section \ref{sec6} presents...Section \ref{sec7} reviews...Section \ref{sec8} highlights..."

- Agent-Gen 的 roadmap 最为详细，不仅给出 section 编号，还给出该 section 的论证目的：

> "We begin by introducing the architecture and ecosystem of LLM-based agents in Section \ref{sec:SA_architecture}, detailing the functionality of each component...and explaining why generalizability is essential...We then review existing approaches to measuring agent generalizability in Section \ref{sec:measure_generalizability}..."

**所有 roadmap 段落均遵循 "Section X does Y" 的固定句式。**

#### 与顶会论文的对比

| 维度 | CSUR Survey | 顶会 Paper |
|------|-------------|-----------|
| Introduction 长度 | 3–6 页 | 1–2 页 |
| Comparison to related surveys | 独立段落/子节，必选 | 通常没有或有 1 句 |
| Scope 声明 | 显式段落，列排除项 | 通常隐含 |
| Taxonomy 出现位置 | Introduction 中就已提出分类 | 在 Method/Related Work 中 |
| Contribution 列表 | 通常 3–5 条，每条对应后文章节 | 通常 2–3 条 |
| Paper roadmap | 详尽，每个 section 都有描述 | 1–2 句 |

**本质差异：CSUR Introduction 是"全文的微缩版"——读完 Introduction 就能理解整篇文章的 taxonomy、论证结构和主要结论。顶会 Introduction 是"钩子"——目标是让读者想继续读下去。**

---

### 维度 3：Taxonomy / Framework 的构建与辩护

#### 普遍规律

**3.1 分类轴的选择与辩护**

四篇论文在分类轴的辩护上投入程度不同，但都有自己的辩护方式：

- **Agent-Gen（最充分的辩护）**：分类轴选择并非直接声明，而是通过识别领域的"三个核心挑战"来自然引出。每个挑战对应一个分类维度。这种辩护方式最有力：分类是"解决问题的必然逻辑"而非"作者的偏好分类"。

- **MoE-Inf**：分类轴（model / system / hardware）基于计算机系统的经典抽象层次，这在系统领域是自明的。作者通过在 Introduction 中分别阐述三层各自面临的独特挑战来间接辩护这个分类。

- **Agent-Opt**：分类轴（parameter-driven vs. parameter-free）以是否修改模型参数为界。辩护方式较简洁，通过指出 "These two categories address fundamentally different aspects of agent optimization" 来建立二分法。

- **Prompt-FW**：使用双重分类结构（三层类型分类 × 四层生命周期）。辩护体现在对每个分类的详细概念化定义中（Section 4.1 Conceptualization），并用四种 essential properties 来界定分类边界。

**普遍规律：CSUR 并不总是有显式的"为什么选这个分类轴"段落（这是与博士论文的区别），但分类的逻辑必然性必须能从领域挑战中自然读出。**

**3.2 分类正交性与边界模糊性处理**

- MoE-Inf 的分类正交性最强：model / system / hardware 是互不重叠的抽象层次
- Agent-Opt 的二分法边界清晰（是否修改参数），但在 hybrid optimization 部分承认了边界模糊性
- Agent-Gen 使用多维度正交分类（改进对象：LLM / components / interaction），每个维度互不重叠
- Prompt-FW 承认三类框架 "are often compatible with each other...depending on the requirements, multiple different categories of prompting framework can be used in parallel"

**处理边界模糊性的策略：**
- Agent-Opt 在 hybrid optimization (§3.3) 中承认融合方法的合法性
- Prompt-FW 直接声明 "multiple different categories...can be used in parallel"
- Agent-Gen 在 Generalizable Frameworks vs. Agents (§7) 中探讨两个概念的交叉地带

**3.3 Taxonomy 图的功能定位**

四篇论文的 taxonomy 图均为**功能性（非装饰性）**：

- **MoE-Inf**：Figure 1 是一个完整的 forest tree，每个叶子节点列出具体论文引用。Figure 3 在每个子类下进一步展开。后文 Sections 3–5 严格按这棵树的结构展开
- **Agent-Opt**：Figure 1 是论文组织概览图，标注了各 section 之间的关系
- **Agent-Gen**：Figure 1 是 agent 架构图，直接对应 Section 2 的展开
- **Prompt-FW**：Figure 2 (workflow diagram) 和 Figure 3 (timeline) 都是功能性图示

**关键规律：后文各章节直接由 taxonomy 图展开。如果删掉 taxonomy 图，论文的组织逻辑仍然清晰但会失去导航地图。**

#### 与顶会论文的对比

| 维度 | CSUR Survey | 顶会 Related Work |
|------|-------------|-------------------|
| Taxonomy 功能 | 全文骨架，每个叶子节点对应章节 | 背景铺垫，通常不驱动正文组织 |
| 分类辩护 | 至少通过领域挑战间接辩护 | 通常无显式辩护 |
| 分类粒度 | 2–4 层深度 | 通常 1–2 层 |
| Taxonomy 图 | 树状/层级图，含具体论文引用 | 通常无图或有简单框图 |
| 与后文的关系 | 严格对应，每章对应分类的一个分支 | 不要求对应 |

**本质差异：CSUR 的 taxonomy 是"论文的结构性承诺"——一旦在 Introduction 中定义了分类，正文必须逐项兑现。顶会 related work 的分类是"信息组织工具"——可以灵活调整。**

---

### 维度 4：文献综述——综合分析 vs 流水账

#### 普遍规律

**4.1 覆盖大量文献与保持分析深度的平衡策略**

四篇论文使用以下策略在"覆盖面"和"深度"之间取得平衡：

**(a) 金字塔结构：从总到分**

每章开头先给出该章覆盖的所有子类的 overview（1–2 段），然后逐个子类深入分析。每个子类内再使用相同的金字塔结构。

- MoE-Inf Section 3 开头：

> "Model-level optimizations aim to enhance the inherent structure and efficiency of MoE models through systematic improvements in architecture, parameter optimization, and algorithmic design. These optimizations can be broadly categorized into three main areas: efficient model architecture design, model compression techniques, and algorithmic improvements."

**(b) 先分类后举例，而非逐个罗列**

一个小节内涉及 10+ 篇论文时，组织方式按**机制/方法聚类**，而非按时间或作者：

- Agent-Opt 的 Table 1 列出了 30+ 种方法，按 6 个维度（Generation, Filtering, MA, LQ, Fine-tune Approach, Base Model）并列比较
- MoE-Inf 在 taxonomy tree 的每个叶子节点下列举相关论文，按子类别（如 "Expert Pruning", "Expert Quantization", "Expert Distillation"）聚类

**(c) "代表作详述 + 其余列表"模式**

- Agent-Opt §3.1：对 AgentTuning 和 SMART 等方法展开详细分析（3–5 段），对剩余方法通过表格集中呈现
- Prompt-FW：对 LangChain、Semantic Kernel 详述，对其余框架通过 capability matrix（Figure 5）一目了然地呈现

**4.2 分析性断言 vs 描述性断言的比例**

从四篇论文中抽样分析：

- **Agent-Gen** 最高：在 Section 2.1.2 (Limitations) 中，几乎每句话都是分析性的："One key limitation lies in the lack of effective communication channels...For example...This conflicting objectives are both valid..."
- **MoE-Inf** 中等偏高：在 model compression 部分，"While sparse activation theoretically reduces computational demands, the overhead from expert routing, communication, and load balancing can lead to significant energy costs" ——从为什么好到为什么还不够好
- **Agent-Opt** 中等：在比较 RL 方法时，分析了 PPO vs. DPO 的适用场景差异："Algorithms like PPO are effective for policy optimization but computationally expensive, while DPO simplifies training but is primarily suited for single-step optimization"
- **Prompt-FW** 较低：更多是概念定义和分类描述，分析性断言较少

**高质量 Survey 的分析性断言占比应在 30–50%（即每 2–3 句描述后应有 1 句分析）。**

**4.3 表格与对比矩阵的功能**

四篇论文均重度使用表格，且表格设计遵循**自包含原则**（可脱离正文独立传达信息）：

- Agent-Opt 的 Table 1（30+ methods × 6 dimensions）：读者扫一眼即可了解全貌
- Agent-Gen 的 Table 1（stakeholder perspectives）：每个 stakeholder 的 role, motivation, why generalizability matters 三个维度独立传达
- Prompt-FW 的 Table 1（representative works by category）：分类 × 子类 × 代表作
- MoE-Inf 的 Table 1（SoTA MoE models）：模型规格参数表

**优质表格的共同特征：**
1. 表头设计精确到可独立理解（不需要正文补充）
2. 至少 3 个维度（单维度表格等于列表，不是分析工具）
3. Caption 不仅说"是什么"还说"比较了什么"

**4.4 单个子节处理大量文献的组织方式（核心技巧）**

Agent-Opt §3.1 面对 30+ 篇 fine-tuning 相关论文：
- 第 1 段：此类方法的总览（why this category exists）
- 第 2 段：核心工作流（trajectory construction → fine-tuning）
- 表格：所有方法的六维对比
- 后续段落：按子维度展开（data generation → data filtering → fine-tuning strategies），每个子维度选取 3–5 篇代表作深入分析
- 每段末尾：该子维度的核心发现或 open question

MoE-Inf §3.2 (Model Compression) 面对 30+ 篇：
- 先按子类（Pruning / Quantization / Distillation / Decomposition）聚类
- 每个子类一个子节，每个子节内先总述原理，再列出代表性工作及其 trade-off

#### 与顶会论文的对比

| 维度 | CSUR Survey | 顶会 Related Work |
|------|-------------|-------------------|
| 文献覆盖量 | 100–300+ 篇 | 20–50 篇 |
| 组织逻辑 | 按机制/方法聚类，多层级 | 按时间或粗略类别 |
| 分析深度 | 每类方法有比较性分析 | 通常描述性为主 |
| 表格功能 | 多维对比矩阵，自包含 | 通常无表格 |
| 分析性断言比例 | 30–50% | 10–20% |
| 每篇文献的讨论深度 | 关键文献 2–5 段，其余列表 | 每篇 1–2 句 |

**本质差异：CSUR 的文献综述目标是"建立知识体系"（synthesis），顶会 related work 的目标是"定位本文贡献"（positioning）。前者要求读者读完能独立判断方法优劣；后者只需要读者知道本文与前人的不同。**

---

### 维度 5：Challenges / Future Directions 的写法

#### 普遍规律

**5.1 Challenges 与 Taxonomy 的关系：自然导出 vs 独立列举**

- **MoE-Inf（自然导出，最佳实践）**：Challenges 部分 (§6) 的三个子维度——Computing Infrastructure Optimization, Operational Challenges, Development Support Ecosystem——直接对应前文 taxonomy 的三个层次（model / system / hardware）中暴露出的未解决问题。例如，"Hardware Integration" 直接回应 §5 (Hardware-Level) 中 "current hardware platforms, optimized primarily for dense computations" 的局限性。

- **Agent-Gen（自然导出）**：三个 future directions——Novel Architectural Frameworks, Standardized Frameworks, Benchmarks——分别对应前文的 architectural limitations（§2）、measurement gaps（§3）、和 framework-agent gap（§7）。

- **Agent-Opt（混合型）**：部分 challenges（Algorithm Adaptability, Standardized Evaluation, Multi-Agent Optimization）从前文自然导出，部分（Safety and Robustness）虽未在前文深度展开但与领域相关。

- **Prompt-FW（偏向独立列举）**：Future directions（more streamlined, more secure, more versatile, more standardized, organic ecosystem）更像愿景宣言，与前文的具体分析连接较弱。

**普遍规律：最强的 CSUR 使其 challenges 成为"前文 gap analysis 的必然结论"。Reviewer 会检查 "这个 challenge 在前文中是否有 evidence"。**

**5.2 单个 Challenge 的内部论证结构**

优质 challenge 的内部论证结构为：

1. **问题陈述**（当前方法在什么场景下失败）
2. **为什么难**（技术瓶颈的根因分析）
3. **为什么重要**（不解决的后果）
4. **可能方向**（具体的、可操作的研究路线）

- Agent-Opt §8.2 (Cost and Efficiency Constraints) 完美遵循此结构：
  - 问题：LLM-based agents face substantial cost and efficiency constraints
  - 为什么难：Multi-turn interaction and extended reasoning chains amplify latency and token consumption
  - 为什么重要：limiting the practicality of deploying LLM-based agents in demanding operational environments
  - 可能方向：context optimization, adaptive memory mechanisms, inference-efficient prompt engineering

- MoE-Inf §6.1.2 (Energy Efficiency) 同样遵循：
  - 问题：energy consumption patterns of MoE models present unique challenges
  - 为什么难：overhead from expert routing, communication, and load balancing
  - 为什么重要：environmental impact becomes more significant
  - 可能方向：carbon-aware deployment strategies, comprehensive energy accounting frameworks

**5.3 Future Directions 的具体程度**

- **Agent-Gen（最具体）**：每个 direction 包含可操作的研究建议，如 "A promising direction is to enhance intra-agent communication protocols that allow components to share operational intents..."
- **MoE-Inf（具体）**：每个 direction 给出了具体的技术路线，如 "carbon-aware deployment strategies"、"specialized circuits for expert routing"
- **Agent-Opt（中等）**：给出了方向但部分较宽泛，如 "Exploring hybrid approaches"
- **Prompt-FW（较泛）**：以形容词驱动（more streamlined, more secure...）而非具体研究问题驱动

**更有说服力的写法是"可证伪的研究问题"，如 Agent-Gen 中的 "determining how to train this coordination unit remains an open question -- should it be optimized end-to-end?"——这个问题可以被后续研究回答"是"或"否"。**

---

### 维度 6：高频写作模式（直接可复用）

#### 6.1 过渡句模板

**章节间过渡（从小节回到大节的逻辑链）：**

**(a) 从局限性过渡到解决方案：**

> "However, the foundational architecture of vanilla LLMs is inherently designed for next-token prediction rather than autonomous decision-making, limiting their effectiveness in complex agent environments." (Agent-Opt, Introduction)

**(b) 从上层优化过渡到底层优化：**

> "While model-level optimizations improve the inherent efficiency of MoE architectures, their practical deployment requires system-level support..." (MoE-Inf, §3→§4 过渡逻辑，基于内容推断)

**(c) 从一个分类过渡到互补分类：**

> "In addition, we outline Parameter-free Optimization methods, which aim to improve agent behavior without modifying model parameters." (Agent-Opt, Introduction)

**(d) 从定义过渡到分类：**

> "Taking into consideration the technical features, design objectives, and application scenarios, the current prompting framework can be broadly covered by three types..." (Prompt-FW, §4.2)

**(e) 从总览过渡到详述：**

> "We begin by presenting a modular view of agent architectures...We then discuss current architectural limitations...Finally, we examine multi-stakeholder perspectives..." (Agent-Gen, §2 intro)

#### 6.2 比较性表达模板

**(a) "Unlike X, which does A, Y does B" 模式：**

> "Unlike conventional RL-based agents, which optimize explicit reward-driven policies, LLM-based agents operate through text-based instructions and prompt templates and in-context learning (ICL), allowing greater flexibility and generalization." (Agent-Opt, Introduction)

**(b) "While X...Y..." 对比模式：**

> "While tool-augmented LLMs can call external functions, they remain fundamentally reactive, executing tools only when prompted. In contrast, LLM-based agents employ the model as a cognitive core within an agentic workflow, enabling the system to initiate actions, plan strategically, select tools autonomously..." (Agent-Opt, Introduction)

**(c) "The key distinction is that..." 精确区分模式：**

> "The key distinction is that: a generalizable framework with fine-tuning data for any scenario can enable the agent to achieve high accuracy on that specific scenario, but may not on other scenario different from the fine-tuning dataset. In contrast, a generalizable agent can achieve consistent accuracy across different scenarios..." (Agent-Gen, Introduction)

#### 6.3 Limitation 表达模板

**(a) 用 "may / might / can" 替代绝对判断：**

> "Agent-based agents remain vulnerable to prompt injection and jailbreak attacks, where crafted inputs can override intended behaviors..." (Agent-Opt, §8) ——用 "can" 而非 "will"

**(b) "A promising direction is..." 建设性批评模式：**

> "A promising direction is to enhance intra-agent communication protocols that allow components to share operational intents or assumptions, enabling them to adjust their operations accordingly." (Agent-Gen, §2.1.2) ——不说 "X is bad"，而说 "更好的方向是..."

**(c) 识别 trade-off 而非单一缺陷：**

> "These conflicting objectives are both valid: the perception and processing unit aims to optimize generalizability and efficiency, while the backbone LLM requires detailed observations to ensure high task-specific accuracy..." (Agent-Gen, §2.1.2)

#### 6.4 Contribution 声明模板

**(a) 列表式（最常用）：**

> "\textbf{Our key contributions} can be summarized as follows:
> \begin{itemize}
>     \item We present a comprehensive survey focused on...To the best of our knowledge, this is the first systematic review dedicated to this line of research.
>     \item We categorize...and analyze them in depth from both algorithmic and workflow perspectives...
>     \item We summarize widely used open-source frameworks, evaluation, datasets...
> \end{itemize}" (Agent-Opt, Introduction)

**(b) 对应挑战式（Agent-Gen 独有，最强）：**

> "This survey provides a comprehensive review...and addresses the three fundamental challenges.
> First, we identify a key gap in the formal definition...To address this, we propose...
> Second, although prior studies have explored aspects of the second challenge...We address this by introducing...
> Third, we examine the often-overlooked distinction between...We formally define both and clarify their differences..."

**这种"挑战→贡献"映射的写法最为有力，因为它将 contribution 置于问题语境中。**

---

## C. 推荐写作框架（通用 Outline）

以下 outline 综合四篇论文的共性结构，适用于任何领域的 CSUR Survey：

```
§1 Introduction                                    [10–12%]
   1.1 领域背景与重要性                              (2–3 段)
   1.2 现有研究分布与不足                            (2–3 段)
   1.3 现有 Survey 的局限 (Comparison to Related Surveys) (2–4 段)
   1.4 本文 Taxonomy 的提出与辩护                    (1–2 段)
   1.5 Scope 与论文筛选标准                          (1 段)
   1.6 Contributions                                (列表)
   1.7 Paper Organization (roadmap)                  (1 段 + Figure)

§2 Background / Preliminaries                      [8–12%]
   2.1 核心概念的形式化定义
   2.2 术语体系建立
   2.3 概念框架图 (Figure)

§3–§N 主体章节（按 Taxonomy 展开）                  [50–60%]
   每章结构：
   §X 章标题 (= Taxonomy 的一个分支)
      §X.1 本章总览与分类逻辑 (1–2 段)
      §X.2 子类 A 综述 (分析性总述 → 代表作详析 → 对比表)
      §X.3 子类 B 综述
      ...
      §X.K 本章小结与开放问题 (可选)

§N+1 Challenges / Future Directions                [10–15%]
   N+1.1 Challenge 1 (从前文 §X 中的 gap 导出)
   N+1.2 Challenge 2
   N+1.3 Challenge 3
   ...

§N+2 Conclusion                                    [3–5%]
   总结核心发现 + 重申贡献 + 展望
```

**篇幅建议（以 55–75 页为目标）：**
- Introduction: 5–8 页
- Background: 5–8 页
- 主体章节: 30–40 页（每章 8–15 页）
- Challenges: 8–12 页
- Conclusion: 2–3 页

---

## D. 高频句型与过渡模板汇总

### D.1 过渡句模板

| 使用场景 | 模板 |
|---------|------|
| 章首总述 | "This section reviews/discusses/examines..., categorizing them into...We first...then...finally..." |
| 从问题到方案 | "To address these challenges, recent studies have explored..." |
| 从分类 A 到分类 B | "In addition to [A], we also outline [B], which..." / "While [A] focuses on..., [B] addresses..." |
| 从宏观到微观 | "Building on this foundation, we now turn to..." / "With this framework in place, we next examine..." |
| 从综述到反思 | "Despite these advances, several challenges remain..." / "Although we reviewed a rich body of literature, many important challenges remain open." |

### D.2 比较性表达模板

| 使用场景 | 模板 |
|---------|------|
| 本质区分 | "Unlike X, which [feature], Y [feature]..." / "The key distinction is that..." |
| 互补关系 | "While X excels at..., Y provides..." / "X and Y address complementary aspects of..." |
| Trade-off 分析 | "X offers [advantage] but at the cost of [disadvantage]; Y, in contrast, prioritizes..." |
| 演进关系 | "Early approaches focused on...; more recent work has shifted toward..." |

### D.3 Limitation 表达模板

| 使用场景 | 模板 |
|---------|------|
| 以 may/can 替代绝对判断 | "...can lead to..." / "...may result in..." (而非 "...will cause...") |
| 建设性批评 | "A promising direction is to..." / "Future research should focus on developing..." |
| Trade-off 表述 | "These conflicting objectives are both valid: on one hand...on the other hand..." |
| 保留判断 | "remains underexplored" / "has received relatively less attention" |

### D.4 Contribution 声明模板

| 使用场景 | 模板 |
|---------|------|
| 标准列表式 | "Our key contributions can be summarized as follows: (1) We present...; (2) We categorize...; (3) We summarize..." |
| 挑战对应式 | "This survey addresses three fundamental challenges. First, we identify...To address this, we...Second,..." |
| 首发性声明 | "To the best of our knowledge, this is the first systematic review dedicated to..." |
| 资源贡献式 | "A curated collection of the surveyed works is provided at [GitHub URL]." |

---

## E. CSUR 关键质量信号（按重要性排序）

1. **Taxonomy 的逻辑自洽性**：如果 taxonomy 的分类轴缺乏显式或隐式辩护，reviewer 会质疑"为什么用这个分类而不是别的分类"。这是最致命的缺陷——因为整篇文章的结构都建立在此之上。

2. **Gap analysis 的说服力**：如果只是泛泛地说"现有综述不系统"而没有引用具体证据（哪些综述、覆盖了什么、遗漏了什么），Introduction 的说服力归零。

3. **文献综述的分析深度**：如果主体章节读起来像"X 做了 A，Y 做了 B，Z 做了 C"的流水账，会被直接判定为"descriptive rather than analytical"（major revision 最常见原因）。

4. **Challenges 与 Taxonomy 的连接**：Reviewer 一定会检查 "Challenges 章节是否有前文 basis"。凭空出现的 challenge = 论证断裂。

5. **Scope 边界的清晰度**：如果没有明确说明包含什么、排除什么（以及为什么），reviewer 会不断追问"为什么没有覆盖 X 领域/方法"。

6. **表格和图示的功能性**：装饰性的 taxonomy figure 会降低而非提高评价。每个图/表必须能独立传达信息。

7. **Writing 的规范性**：CSUR 对学术写作规范的要求高于顶会——paper roadmap、过渡句、引用覆盖（至少 100–200 篇参考文献）都是必选项。

---

## F. 三个最常见的致命错误

### 致命错误 1：Taxonomy 与正文脱节

**表现：** Introduction 中提出了一个漂亮的 taxonomy 图，但正文各章节并不严格按照 taxonomy 的分支展开，或者某些 taxonomy 分支没有对应的章节。

**改正方向：** 
- 写作顺序应是：先确定 taxonomy → 按 taxonomy 分配章节 → 每章严格对应一个分类维度
- 写完后做一个"逆向检查"：列出 taxonomy 的每个叶子节点，确认正文中都有对应的深入讨论
- 参考 Agent-Gen 的做法——Introduction 中声明"三个 challenges"，正文每个大章对应解决一个 challenge

### 致命错误 2：描述性综述而非分析性综述

**表现：** 每篇论文用 1–2 句话概括（"X proposed method Y, which does Z"），没有跨论文的比较、没有 trade-off 分析、没有方法优劣的判断。

**改正方向：**
- 使用"聚类 + 分析"结构替代"逐篇摘要"
- 每 2–3 句描述后必有 1 句分析
- 使用多维对比表替代纯文本列表
- 参考 Agent-Opt 的做法：先用表格呈现 30 篇论文的六维对比，再选取代表作深入分析
- 在每章/每子节末尾给出 "key insights" 或 "summary of findings"

### 致命错误 3：Challenges 泛泛而谈

**表现：** Future directions 是一组形容词（"more efficient", "more robust", "more scalable"），没有可操作的研究问题，没有与正文的 gap 建立连接，没有指出"为什么这个 challenge 是难的"。

**改正方向：**
- 每个 challenge 必须能从正文的某个具体 gap 追溯到
- 每个 challenge 必须包含"为什么难"的根因分析（技术瓶颈，而非资源不足）
- 优先使用可证伪的表述（"determining how to train this coordination unit remains an open question — should it be optimized end-to-end?"）而非形容词堆砌
- 参考 MoE-Inf 的 challenge 结构：问题 → 为什么难（技术根因）→ 为什么重要 → 可能方向
- 每个 challenge 应至少 2–3 段，不能只是一个 bullet point

---

## 写作检查清单

### 结构完整性（8 条）

- [ ] Introduction 是否包含全部 7 个子部分（背景→问题→gap→taxonomy→scope→contributions→roadmap）？
- [ ] 是否有独立成章的 Background / Preliminaries 章节？
- [ ] 主体章节是否与 Introduction 中声明的 taxonomy 严格对应？
- [ ] 是否有独立的 Challenges / Future Directions 章节（而非仅 1–2 段在 Conclusion 中）？
- [ ] Paper roadmap 是否引用了每个 section 的编号和简短内容描述？
- [ ] Conclusion 是否简洁（2–4 段），不引入新论证？
- [ ] 参考文献数量是否达到 100–200+ 篇？
- [ ] 是否提供了 curated repository / website 供读者跟踪最新进展？

### Taxonomy / Framework 质量（6 条）

- [ ] Taxonomy 的分类轴是否给出了显式或隐式辩护（通过领域挑战间接辩护可接受）？
- [ ] 分类的边界是否清晰？是否处理了边界模糊性（如 hybrid 方法）？
- [ ] Taxonomy 图是否是功能性的（后文各章节直接由此展开）？
- [ ] 分类是否正交？如果不正交，是否有意为之且有说明？
- [ ] Taxonomy 的几个分支的篇幅是否大致均衡（或显著不均衡有明确理由）？
- [ ] 是否在 Introduction 中就给出了 taxonomy 的核心分类轴？

### 文献综述深度（8 条）

- [ ] 每个主体章节是否有开头的总览段落（该章的组织逻辑和分类逻辑）？
- [ ] 当一个小节涉及 10+ 篇论文时，是否按机制/方法聚类而非逐一列举？
- [ ] 是否使用多维对比表（3 个维度以上）来辅助文献综述？
- [ ] 表格是否能脱离正文独立传达信息（表头精确、caption 说明比较维度）？
- [ ] 分析性断言（trade-off / why / why not）的比例是否达到 30–50%？
- [ ] 是否对关键代表作进行了深入分析（2–5 段），而非所有论文同等对待？
- [ ] 每章/每子节末尾是否有分析性小结（key insights / summary of findings）？
- [ ] 是否有跨论文的比较分析，而非仅对单篇论文的描述？

### 写作规范性（6 条）

- [ ] 是否使用 "Comparison to related surveys" 独立段落/子节来定位本文？
- [ ] Scope 声明是否明确列出包含和排除的内容，并给出理由？
- [ ] 是否使用 "To the best of our knowledge, this is the first..." 来声明首发性？
- [ ] Limitation 表述是否使用 may/can/trade-off 等软化策略，避免绝对判断？
- [ ] 章节间是否有显式的过渡句（而非直接跳到下一章）？
- [ ] Contribution 声明是否与后文章节一一对应（每个 contribution 能在后文找到落地章节）？

---

> **报告生成日期：** 2026-04-30
>
> **分析对象：** 4 篇 CSUR Survey 论文（MoE Inference Optimization / LLM Agent Optimization / Agent Generalizability / Prompting Frameworks）
