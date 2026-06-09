# Project Context: ACM CSUR Survey — Agent Experience Transformation

## 1. 项目概述

撰写一篇投稿 **ACM Computing Surveys (CSUR)** 的期刊长文，主题为 LLM-based Agent 的 **Experience Transformation**——交互经验在不同载体之间的转化与复用机制。

**研究背景**：从静态大模型（LLM、VLM 等）到自主 Agent 的转变带来一个根本变化——Agent 在持续的 *experience loop* 中运作：在具体决策上下文下尝试任务、产生异构动作（推理轨迹、工具调用、环境控制等）、观察环境返回的客观后果，并可选地接收评价反馈。这些累积的决策证据即 *agent experience*，最初以 trajectory（即 raw experience，可能跨模态）的形式存在。直接保留 trajectory 并通过检索复用（如 RAG）虽然直观，但在长程 Agent、test-time search、过程级监督等近期趋势的推动下，于规模上迅速变得昂贵且脆弱：上下文窗口受限阻碍长期保留、检索延迟拖慢决策、单条 episode 的噪声妨碍跨任务泛化。社区由此发展出多种存储与复用经验的机制，对应不同的载体形式，各自呈现不同的 reusability / verifiability / cost / robustness trade-off 画像；不存在普适最优载体，最优选择依赖下游任务的约束。

**核心立意**：不按传统的"组件"（Memory / Planning / Tool Use）或"技术"（SFT / RAG / RLHF）维度分类，而是以 **Experience 的 Transformation 与 Utilization** 为主线，将 memory、evaluator、training 视为同一语义记录在不同载体间的 representation-to-representation pathway，在统一框架下比较其 trade-off，并分析 LLM-based Agent 如何将交互经验转化为不同形式的载体、并在不同决策场景中复用。

---

## 2. 核心定义

本节给出三组核心定义：经验的语义记录（§2.1）、经验形式的分类轴（§2.2）、以及经验转化的判定标准（§2.3）。三者之中，§2.1 是基本单元，§2.2 是描述载体的坐标系，§2.3 定义本 Survey 主轴所依据的转化关系。

### 2.1 Experience（经验）

最小语义记录定义为模态无关的四元组：

$$e = (c, a, o, f)$$


| 元素              | 必需性 | 含义                          | 多模态示例                                      |
| --------------- | --- | --------------------------- | ------------------------------------------ |
| Context $c$     | 必需  | Agent 决策前可获得的信息             | 文本指令、GUI 截图、摄像头图像、音频                       |
| Action $a$      | 必需  | Agent 当前步骤的输出               | CoT 推理、工具调用、屏幕坐标点击、motor commands          |
| Observation $o$ | 可选  | 环境返回的客观后果                   | 执行报错、渲染后网页截图、传感器状态                         |
| Feedback $f$    | 可选  | 对 $(c,a,o)$ 或 $(c,a)$ 的评价信号 | Scalar reward、Textual critique、Visual diff |

一条 trajectory 即 $e$ 的有序序列；后文 “raw experience” 默认指 trajectory 形式。


### 2.2 Experience Carrier（经验载体）

**定位说明**：Experience Carrier 仅是**经验形式的分类轴**，用以刻画"经验以何种形式存在于模型架构中"，是描述 Transformation 源端与目标端的基础语汇。本 Survey 的组织主轴并非 Carrier 本身，而是 **Transformation Pathway**——经验在不同 Carrier 之间的转化路径（详见 §4、§5）。Carrier 分类的作用是为路径分析提供共同的坐标系，使不同 pathway 的源端、目标端、以及跨 pathway 比较有统一基底。

#### 2.2.1 设计原则

Carrier 分类轴是 Transformation 分析的基础坐标。我们不按传统维度（modality、technique、component）组织，而是沿**"经验在模型架构中的存在层次"**这条主轴切分，基于三点考虑：

第一，存在层次直接映射到 Agent 系统关心的核心 trade-off——interpretability、inference cost、editability，使分类本身携带分析维度，便于后续在 pathway 层级做 trade-off 对比。

第二，存在层次与 modality 正交——任意模态的经验都可以存在于 Tokenized、Latent 或 Parametric 任一层次，多模态工作由此自然融入框架而不必开辟特殊通道。

第三，存在层次直接对应载体形式的根本差异——从 Tokenized 到 Parametric 是载体存在形式的重组。虽然 Transformation 判定标准不要求载体类型必须改变（同层如 Narrative → Narrative 同样可以构成合法的 Transformation），但存在层次作为分类轴最有效地捕捉跨载体 Transformation 的结构差异，从而最大化 pathway 分类的判别力。

#### 2.2.2 顶层三类与连续谱

按经验在模型架构中的存在层次，顶层三分统一为 **Tokenized, Latent, and Parametric Carriers**：

**Tokenized Carriers（Token 化载体）**：以离散 token 序列形式显式进入模型前向传播的经验载体。涵盖 text tokens、code tokens、visual patch tokens、action tokens、serialized structural tokens（如序列化 graph / code / workflow）等，不限于自然语言文本。占用 context window，推理时需完整处理；其中自然语言与代码通常可直接读写编辑，patch / action / 结构化序列则未必具有人类可读性。内部按形式化程度再分 **Narrative** 与 **Schematic** 两子类（见 §2.2.3）。

**Latent Carriers（隐空间载体）**：以连续向量 / hidden state 形式存在，直接参与模型 attention 或 hidden-state 计算的中间表示。不等同于离散 token，也不固化在权重中，是介于两者之间的桥梁层。省去前置编码开销，但对人类不可直接阅读。涵盖 KV cache、activation memory、prefix cache、learnable soft prompts、continuous memory tokens、trained memory composers。可视需要区分 session-scoped（无需训练，如 KV cache）与跨 session 可复用（需训练，如 soft prompts）两种实现形态，但不作为正式分类子类。

**Parametric Carriers（参数化载体）**：经验固化在神经网络权重分布中，完全隐式。推理时不占用 context、直接前向传播输出；修改需再训练，可编辑性最低。内部按功能角色再分 **Policy** 与 **Evaluator** 两子类（见 §2.2.4）。

三类构成连续谱：

> **Tokenized → Latent → Parametric**
> 沿此谱从左到右：interpretability ↓，inference efficiency ↑,editability ↓，存储位置从外部数据库 / prompt → GPU memory → model checkpoint。

**术语说明**：Tokenized 的判定依据是计算入口而非表面模态。自然语言日志、code、视觉 patch token、GUI / action token、序列化 graph / code / workflow token 均归此类。

#### 2.2.3 Tokenized 子类：Narrative vs. Schematic

按**形式化程度**进一步划分：

**Narrative Tokenized（叙事型）**：以自然语言或感知顺序组织的弱形式化载体，通过 language / multimodal understanding 复用。

- 文本形式：trajectories、reflections、summaries、rules、insights、hints、guidelines、skill descriptions
- 多模态形式：screenshot / video sequences、audio traces、interleaved visual-textual interaction logs

**Schematic Tokenized（图式型）**：以语法结构或拓扑结构组织的强形式化载体，通过 parsing、execution 或 graph traversal 复用。

- 程序化：code libraries、workflows、SOPs、API specifications、composite actions
- 图结构：knowledge graphs、sentence graphs、decision trees、execution graphs
- 其他结构化：typed skill libraries、cheatsheets

两子类都可承载任意模态的经验，多模态以标签属性而非独立载体类别参与分析。

#### 2.2.4 Parametric 子类：Policy vs. Evaluator

按**功能角色**划分：

**Policy Parameters（策略参数）**：生成 action 的 actor 权重，涵盖 LLM agent 权重、VLA 权重、GUI agent 权重、LoRA adapters。

**Evaluator Parameters（评估器参数）**：评估 $(c,a,o,f)$ 的判断器权重，涵盖 reward models、process reward models (PRM)、verifiers、critics、VLM judges。

此划分与 Transformation 路径组织直接相关——Evaluator 参数既可作为 Transformation 的产物（Tokenized → Evaluator），也可作为产生新 Transformation 的中间状态（Evaluator → Policy via RLHF）。

#### 2.2.5 正交属性

以下三个维度作为**每个 carrier 实例的属性标签**而非分类维度，以保持分类的正交性，同时在 pathway 分析中作为编织维度：


| 属性                    | 取值                                                                     | 使用场景                                                         |
| --------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------ |
| **Modality**          | textual / visual / auditory / GUI / embodied-sensor / cross-modal      | 在每条 pathway 中讨论"该 pathway 在不同模态下的实现差异"                       |
| **Abstraction level** | raw / refined                                                          | 区分 trajectory 与 refined derivatives；主要在 Tokenized 层内体现 |
| **Experience Source**            | agent self-generated / human demonstration / teacher model synthesized | 用于讨论经验来源对 pathway 选择的影响                                      |


#### 2.2.6 边界澄清

**Trajectory（raw experience）的定位**：trajectory——即 raw experience 的默认形式——本身是最低抽象程度的 Narrative Tokenized 载体（"零度抽象"特例），而非独立于 carrier 体系之外的东西。Transformation 通常以 trajectory 为起点，目标是提升抽象程度（Narrative refined）、改变形式化程度（Narrative → Schematic）或改变存在层次（Tokenized → Latent / Parametric）。

**Embedding 的分层归属**：按用途区分——

- Embedding 作为**外部 memory 的检索索引**（retrieve 后再进入 context）：不归入 Latent，而归入所索引 Tokenized 内容的附加机制；
- Embedding 作为**可学习的 memory 表示**（不解码回 token，直接参与模型 attention）：归入 Latent。

#### 2.2.7 总览

```
                Tokenized Carriers ──────── Latent Carriers ──────── Parametric Carriers
                (context-addressable      (continuous vectors)       (network weights)
                 token sequences)
                    │                                                       │
        ┌───────────┴───────────┐                               ┌───────────┴───────────┐
   Narrative              Schematic                            Policy            Evaluator
   (reflections,          (code,        (KV cache,            (VLA, LLM         (RM, PRM,
    trajectories,         workflows,    soft prompts,          agents)            verifier)
    screenshots)           graphs)       mem tokens)

         ←──── token-level → latent-state-level → parameter-level ────→
         ←──── interpretability / editability 递减，inference efficiency 递增 ────→

 Modality (textual / visual / GUI / embodied) ─── 正交属性，贯穿所有 carrier
 Abstraction (raw / refined) ─────────────────── 正交属性，主要在 Tokenized 层内体现
 Source (self / human / teacher) ──────────────── 正交属性，对所有 carrier 可标注
```

### 2.3 Experience Transformation（经验转化）—— 判定标准

经验转化指经验 $e=(c,a,o,f)$ 或其派生物被**重新表示**，记为 $\mathcal{T}: \mathcal{C}_{\text{src}} \rightarrow \mathcal{C}_{\text{tgt}}$。重新表示要求目标载体是从源经验重新推导或编码而来的新形式：抽象层级的提升（trajectories → reflections）、形式化程度的改变（trajectories → code）、存在层次的迁移（tokenized → parametric）、参数化载体内部的功能角色转变（evaluator → policy）。源端与目标端是否同属一个顶层类别不影响判定——Narrative → Narrative 的语义抽象同样产生新形式。

只搬运而不重新表示原始记录的操作不在此列：重新序列化（同一 trajectory 的 JSON ↔ Markdown）改写的是语法，子集筛选与轨迹截断保留的是原始记录的一部分或一个前缀，留存内容仍以原形式存在，未被编码成新载体。判别二者的正面标准是目标是否承载了从源经验**派生**出的语义内容：换语法、取子集、截前缀不产生新内容，被排除在外；reflection 中的规则、code 中抽象出的过程、graph 中抽取的类型化关系、soft prompt 或权重中学到的表示，则是源记录里并不显式存在、须经推导或学习才得到的，属于转化。

---

## 3. Scope 边界

### 3.1 纳入标准

数据必须同时满足：

1. **具备决策过程语义**：可映射为 $e=(c,a,o,f)$ 结构。
2. **异构动作空间**：Action $a$ 属于 LLM-based system 的 heterogeneous action space（推理轨迹、工具调用、规划分解、环境控制、多智能体通信等）。

经验来源不限（Agent 自身轨迹 / 人类专家示范 / Teacher model 合成数据）。Inclusion 基于底层机制而非论文的自我定位——无论原始表述是 "self-play"、"bootstrapping" 还是 "iterative self-training"，只要满足上述标准即可。

### 3.2 排除标准

- 静态语料预训练（无决策过程语义）。
- 单步分类 / 标注任务的 SFT（非异构动作空间）。
- 纯模型蒸馏 Parametric → Parametric（经验语义链断裂）。
- 纯图像分类 / 视觉基础模型训练（无序贯决策语义）。
- 非 LLM-based 系统（传统 RL 等）。

### 3.3 Agent 的定义策略

以 Agent（有明确环境交互的系统）为核心锚点，但承认 Transformation 机制跨越 agent / non-agent 边界。对 Agent 采用广义定义：核心特征是"在任务上下文中进行序贯决策"，environment 可以是 reasoning verification、tool execution、physical world 等不同层次。

---

## 4. 已知转化路径

以下 7 条为前期梳理的基础单路径，用新 Carrier 术语表述。多模态作为正交属性编织入每条路径，不开辟独立路径。多模态场景下可能涌现的新路径需保持开放探索。

1. **Narrative → Narrative**（intra-tokenized abstraction）：trajectories → reflections / rules / summaries / insights。同层语义抽象，源与目标都是 Narrative Tokenized。
2. **Narrative → Schematic**（intra-tokenized formalization）：trajectories → code / workflows / SOPs / graphs。同层形式化。
3. **Tokenized → Latent**（latent compression）：trajectories → KV cache / soft prompts / continuous memory tokens。跨层压缩。
4. **Tokenized → Parametric (Evaluator)**（evaluator internalization）：trajectories → RM / PRM / verifier / judge。经验固化为评估能力。
5. **Tokenized → Parametric (Policy)**（policy internalization）：trajectories → policy weights via SFT / RL。经验固化为决策能力。
6. **Parametric (Evaluator) → Parametric (Policy)**（preference alignment）：RM 信号 → policy weights via RLHF / DPO。参数间转化。
7. **Parametric → Tokenized**（knowledge externalization）：权重 → synthetic trajectories / demonstrations。隐式经验外化为显式载体。

**复合路径（Composite Pipelines）的处理**：区分两种情况——

- **单篇论文中偶现的两条相对独立的转化**（例如一篇论文顺带做了 trajectory → reflection 与 trajectory → policy 两件彼此独立的事）：在对应的单路径 Section 分别引用相关片段。
- **单篇论文将多路径链式组合作为整体方法**（例如 Narrative Tokenized → Schematic Tokenized → Parametric、Tokenized → Latent → Parametric、或 Policy → Trajectory → Policy 的自生成环路）：这类工作的贡献点恰在路径间的衔接机制（integration mechanism），而非任一 pathway 本身。此类工作在独立的 **Composite Pipelines Section** 作为 first-class 对象 anatomy，重点分析 integration mechanism、以及 compose 相对单路径的优缺点。

---

## 5. Survey 结构决策

主体按 Transformation Pathway 组织，每条 pathway 的叙事链：引入段 → 该 pathway 文献分类后的子部分（多模态工作自然融入） → Discussion。

**Section 结构分层**：

- **Sections 3–6**：7 条单路径分组呈现（按 Carrier 源端聚合为 4 个 Section）。
- **Section 7 — Composite Pipelines（独立章节，核心差异化贡献 1）**：对将多路径链式复合作为整体方法的论文做 anatomy。识别 composition pattern；对每种 pattern 给出定义、代表工作、integration mechanism 分析；最后是整体讨论。
- **Section 8 — Cross-Pathway Synthesis（核心差异化贡献 2）**：
  1. Pathway trade-off comparison
  2. Utilization 对比分析
  3. Utilization-driven pathway selection（场景化推荐）

目录的结构如下：
1. Introduction
2. Preliminaries: Experience, Carriers, and Transformations
3. Tokenized-to-Tokenized Transformations
4. Tokenized-to-Latent Transformations
5. Tokenized-to-Parametric Transformations
6. Parametric-Source Transformations
7. Composite Transformations
8. Pathway-Level Analysis
9. Open Problems and Future Directions

---

## 6. 协作指令

在后续讨论、文献分析、大纲调整和正文撰写中，遵循以下原则：

1. **紧扣 Transformation 机制**：分析任何文献时，首先识别源经验、目标载体、所属 Pathway；对复合论文，首先识别其整体 pipeline 形状（constituent pathways + integration mechanism）。
2. **严格把控边界**：纳入判定检验异构动作空间条件；转化判定检验经验是否被重新表示为新形式（抽象层级提升 / 形式化 / 存在层次迁移），而非仅搬运原始记录（重新序列化、子集筛选、轨迹截断不计为转化）。
3. **超越列举，追求深度分析**：不停留在"某论文做了什么转化"的浅层总结，主动拔高到 trade-off 对比、composition pattern 发掘、utilization 驱动力分析。
4. **开放探索新路径与新 pattern**：对不符合已知 7 条路径的新转化形式、或不符合已知 composition patterns 的新整合模式，敏锐识别并抽象为新 Pathway / Pattern。
5. **严格使用新 Carrier 术语**：分析任何工作时，Carrier 命名使用 Tokenized (Narrative / Schematic) / Latent / Parametric (Policy / Evaluator)。旧术语（Textual、Structured、Multimodal Raw 等）仅在说明"与既有分类的对应关系"或引用论文原文时提及，正文分析一律用新术语。Modality 以正交属性形式出现，不与 Carrier 类别并列。

