---
name: survey-translate
description: 将中文 Markdown 学术内容翻译为英文 LaTeX 并反 AI 润色。当用户要求翻译论文章节、将中文综述内容转为英文、翻译 markdown 到 tex、翻译成英文 LaTeX、翻译这段、翻译并润色、对 tex 做反 AI 检查时触发。适用于 ACM Computing Surveys 等计算机领域综述论文。
---

# Survey Academic Translation & Polish

两阶段工作流。用户可能只要求其中某一阶段，根据用户指令判断。

## 核心约束

1. **严格忠实原文**。翻译和润色都必须严格对照中文原文的意思，严禁擅自添加内容、重构论证结构、扩展论述、补充原文没有的信息或例子。
2. **去除 Markdown 格式**。中文原文中的加粗（`**text**`）和斜体（`*text*`）不应出现在输出的 LaTeX 中——既不要保留 markdown 标记，也不要转换为 `\textbf{}` 或 `\textit{}`。
3. **仅输出正文片段**。输出的是某个 .tex 文件中的一部分正文内容，不要添加 `\section{}`、`\begin{document}`、`\end{document}` 等文档结构命令，也不要加 preamble。如果原文包含 `\section{}` 或 `\subsection{}` 则保留。
4. **保持 LaTeX 命令**。原文中的 `\cite{}`、`\ref{}`、`\label{}` 等 LaTeX 命令原样保留。

---

## 阶段一：中文 Markdown → 英文 LaTeX

用户会说"翻译 xxx.md 到 xxx.tex"或类似表述。

### 步骤

1. 用 Read 读取用户指定的中文 .md 文件
2. 将中文内容翻译为英文 LaTeX
3. 将翻译结果写入用户指定的 .tex 文件（用 Write）
4. 简要告知用户翻译完成，请用户审查

### 翻译规范

**忠实度**：每个句子的信息量、论点、限定条件（only, mainly, typically, in some cases 等）、因果关系必须与中文原文一致。不合并、不拆分、不重组原文的论证顺序。

**格式处理**：
- 去除所有 `**bold**` 和 `*italic*` markdown 标记
- 如原文有 markdown 列表（`-` 或 `1.`），转为 LaTeX 的 `itemize` 或 `enumerate` 环境
- 如原文有 markdown 表格，转为 LaTeX `tabular` 环境
- 原文中的数学公式（`$...$` 或 `$$...$$`）原样保留，行间公式统一用 `$$...$$`
- 原文中的 `\cite{}`、`\ref{}`、`\label{}`、`\textit{}` 等 LaTeX 命令原样保留

**学术英语规范**（详见 `references/writing_rules.md`）：

| 维度 | 要点 |
|------|------|
| 简洁 | 删除冗余（due to the fact that → because），避免名词化（conduct an analysis → analyze），主语不要埋在介词短语里，句子保持简短 |
| 清晰 | 优先主动语态（Methods 部分可用被动），新信息放句末，平行结构一致（不要混用名词和动名词并列），修饰语紧贴被修饰对象 |
| 一致 | 术语首次出现给全称+缩写，后续统一用缩写；同一概念不交替使用不同译名 |
| 避免 Chinglish | 删除多余名词/动词；不并列近义双胞胎（various and different → various）；不用 "Although ... but ..." 或 "Because ... so ..."；删除 very/quite/really/obviously/clearly 等空泛副词 |
| 时态 | 描述他人工作用一般过去时或现在完成时（"Wang et al. proposed..."），描述本综述章节安排用一般现在时（"Section 3 presents..."） |
| 人称 | 综述中可用 "we"（"We classify ... into three categories"），避免 "I" 和 "you" |
| 引用 | 核心论述每 1-2 句应有引用支撑；避免 `[1,2,3,4,5,6,7,8]` 式堆砌，选最具代表性的 2-3 篇 |

---

## 阶段二：反 AI 味道润色

用户会说"润色 xxx.tex"、"检查 AI 味道"、"反 AI 润色"等。

### 步骤

1. 用 Read 读取已翻译的 .tex 文件，同时回顾对应的中文原文（如用户提供了中文源文件路径）
2. 以 `references/anti_ai_voice_rules.md` 为检查清单逐项排查
3. 修改违规处，将润色后的内容写回 .tex 文件（用 Write）
4. 简要列出主要修改的问题类型（例如"删除了 3 处 LLM 标志词、拆分了一个分号链长句、将 2 处段末重复总结改为具体推论"）

### 检查维度

参照 `references/anti_ai_voice_rules.md`，重点检查：

- **句子节奏 (R1-R6)**：是否有连续多句长度相近？是否有堆砌的排比结构？em dash 是否超过 1 个/段？
- **用词 (R7-R11)**：是否有 delve/tapestry/nuanced/underscore/pivotal/paramount/leverage/robust/crucial/vital/profound 等 LLM 标志词？是否有可删除的 key/core/fundamental 等空泛强调词？是否有 embody/capture/reflect 等模糊承载动词？是否有不必要的名词化？
- **论证姿态 (R12-R16)**：是否每段都空谈 limitations？是否有 "it is worth noting"、"interestingly"、"notably" 等元评论？段末是否在重复总结？是否有 "A central question is whether..." 等虚假问题开头？引用是否具体命名了工作而非堆砌编号？
- **段落结构 (R17-R20)**：是否每段都按 intro-body-conclusion 模式？小节开头是否都模板化（"In this section, we..."）？主题句是否有具体内容而非类别标签？
- **Survey 专项 (R21-R25)**：是否有 "remains underexplored"、"To bridge this gap" 等 gap-filling 陈词滥调？比较性断言是否有参照点？正文中是否宣告了 "We propose" 等贡献声明？

### 校准

目标是**低浓度**而非零出现。学术英语需要适量的抽象名词、平行结构和 hedging。一段话用一次 "however" 没问题；用三次加两个 em dash 加一个 "crucially" 就不行。按**密度约束**来把握，不要过度润色导致文风生硬。

---

## 沟通规范

与用户沟通时使用中文，遵循 CLAUDE.md 中的 Chinese Anti-AI Patterns：
- 不写段末收尾总结句（"这说明"、"由此可见"）
- 不用三段式排比（"首先...其次...最后..."）
- 不写升华句、对比框架、提示语引导、报告腔、形式感连接词

保持客观专业的 CSUR 审稿人立场。如发现原文存在论证偏差、分类混淆或文献盲区，直接指出并给出依据，不迎合。
