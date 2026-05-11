## 三、学术英语写作核心规则

### 3.1 简洁性（Conciseness）

**1. 删除冗余**：冗余是指那些即使删除也不影响含义、但删除后能让文本更精炼、更易跟随的词或短语。把"due to the fact that"换成"because"，"In the form of"换成"As"，"In many cases"换成"Often"，"has the ability to"换成"can"。

**2. 避免名词化（Nominalization）**：把动作埋在名词里会削弱句子。关注"真正的"动词，避免将动词或副词转成名词再搭配弱动词，例如不要写"to effect an installation, to conduct an analysis, to give consideration"，而要写"to install, to analyze, to consider"。

**3. 不要把主题埋在介词短语里**："The use of this method would eliminate the problem"应改为"This method would eliminate the problem"。

**4. 句子要短**：长句会损害可读性。Watson 与 Crick 的 DNA 双螺旋诺奖论文只有两页——"简洁是终极的优雅"，过度修饰的写作让人分心、乏味，给读者带来负担；信息的传递反而在简洁精确的写作中更具说服力。

### 3.2 清晰性（Clarity）

**1. 主动语态优先**：主动语态把焦点放在执行动作的主语上，使句子更清晰、更简洁。不要写"The study was conducted by the researcher"，而要写"The researcher conducted the study"。识别被动语态的方法是寻找"to be"形式（is, am, are, was, were, be, been, being）加过去分词（通常是 -ed 动词）。但 Methods 部分可以使用被动语态，在某些学术学科或论文的特定章节（如 Methods），被动语态可能更合适甚至必要；关键是理解两种语态各自的优势。

**2. 信息位置原则**：把新信息、技术术语或长而复杂的短语放在句末以获得强调，避免读者混淆。开头放已知信息（given），结尾放新信息（new），这是英文段落连贯的核心。

**3. 平行结构（Parallelism）**：将并列成分保持在相同的语法结构中。例如列举 Agent 的三种能力时，要么都用名词（"reasoning, planning, and tool use"），要么都用动名词（"reasoning, planning, and using tools"），不能混用。

**4. 修饰语紧贴被修饰对象**：让修饰语靠近它所修饰的成分，避免悬垂修饰（dangling modifier）。

### 3.3 一致性（Consistency）

保持写作的一致性与逻辑流：在连字符、度量单位、标点、语法、符号、大小写和缩略词的使用上保持一致。具体到 AI Agent 综述：术语首次出现时给出全称+缩写（如 "Large Language Model (LLM)"），后续统一使用缩写；对同一概念不要交替使用不同译名（例如不要时而用 "agentic reasoning" 时而用 "agent reasoning"）。

---

## 四、Chinese 作者最常见的 Chinglish 错误

这是中文母语者写英文 Survey 最容易踩的坑：

**1. 多余的名词与动词**：中国作者写的英文常含有不必要的词或短语。例如"A steady growth in GDP is necessary for attainment of economic prosperity"中的"attainment"是多余的，应改为"A steady growth in GDP is necessary for economic prosperity"。

**2. 冗余双胞胎（Redundant Twins）**：两个意思几乎相同的词被并列使用。例如 "various and different methods"、"final and ultimate goal"、"basic and fundamental concept"——只保留其中一个即可。

**3. 句子构造问题**：句子构造是中国科技工程领域学者最大的语言挑战，其次是词汇选择、衔接手段、连贯性和语法。具体表现包括：
- 主语不明确（中文允许省主语，英文不允许）；
- 喜欢用 "It is ... that ..." 强调句但用得过多；
- "Although ... but ..."、"Because ... so ..." 同时使用（英文中只能用一个）。

**4. 过度使用空泛副词**：避免 "very"、"quite"、"really"、"obviously"、"clearly"——这些词在学术英语中要么删掉，要么替换为更精确的副词（如 "substantially"、"markedly"）。

---

## 五、时态与人称的具体规则

| 章节 | 推荐时态 | 说明 |
|---|---|---|
| Abstract | 一般现在时为主 | 描述论文做了什么、贡献是什么 |
| Introduction | 一般现在时 | 描述领域现状与共识 |
| Related Work / 引用他人工作 | 一般过去时 或 现在完成时 | "Wang et al. proposed..." 或 "Recent studies have shown..." |
| 描述本综述的章节安排 | 一般现在时 | "Section 3 presents..." |
| 描述实验或方法 | 一般过去时（被动语态可接受） | "The model was trained on..." |
| Conclusion | 一般现在时 + 现在完成时 | 总结贡献 |

人称方面：使用正式的学术语言，避免口语和个人观点（除非明确要求）；语调应当是分析性和客观的。"We"在综述中是被广泛接受的（"We classify ... into three categories"），但应避免 "I" 和 "you"。

---

## 六、引用与参考文献规则

1. **首次提及作者**：使用全名或姓+名首字母，并配 et al.（≥3 作者时）。
2. **方法命名**：算法/系统首字母大写并保持一致（如 "AutoSurvey"、"SurveyForge"）。
3. **避免"二手引用"**：不要引用 A 引用了 B 的内容而自己却没读过 B 的原文。
4. **引用密度**：综述的核心段落每 1–2 句应有引用支撑；但避免 "[1,2,3,4,5,6,7,8]" 式的堆砌——挑选最具代表性的 2–3 篇。
5. References 部分必须提供文中引用的所有来源的完整列表，确保正确归属，并严格遵循目标期刊/会议格式（ACM、IEEE、Springer LNCS 等）。
