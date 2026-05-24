根据下面的写作原则，重写一下 sec5 部分的内容。

sec5部分：`sec5_tokenized_to_parametric.md`
sec5部分的论文概况：`P4.describe.md`和`P5.describe.md`
注意：修改后的内容应该是可以直接放到survey中的中文版（也就是可以直接用于survey英文版对应的中文版）


# pathway 章节的写作准则

你正在协助撰写/修订一篇投稿 ACM CSUR 的综述，主题为 LLM-based Agent 的 Experience Transformation。该 survey 以 Transformation Pathway 为组织主轴。本提示词只适用于 §3–§7 的 pathway 文献分类章节，规定「单个 pathway 章节应当呈现的样子」。整篇 survey 的 Introduction、§2、§8 等不在本提示词范围内。

以下是章节文本在任何阶段都应满足的属性。初次撰写即按此写出，重写即向此收敛；它们描述成品的状态，不是某个环节才执行的动作。

## 1. 统一的章节结构

所有 pathway 章节共用同一体例：

- 每个子类以一句「机制定义句」开头，说清这一类靠什么专用机制获得目标载体；
- 文献以连续句串联、分类判断前置（先定性这组工作属于哪一类，再展开），不逐篇平铺罗列；
- 所有 trade-off、优劣、梯度对比集中在该章节的 Discussion，不在各子节重复。

子类内部的行文骨架可参照下例（仅示范结构，非内容深度）：

> [机制定义句：本子类是什么、靠什么机制]。[该机制为何有用，一句]。The most straightforward example of which is [工作 A]，[A 如何体现该机制]。Building on that，[工作 B] [B 在 A 之上的改动]。Similarly，[工作 C] [C 的做法]。[若存在共性局限] While [该机制] is not without challenges，[局限是什么]。To address this，[工作 D] [D 的应对]。

结构要点：① 范畴句永远在段首、不加修饰；② 各工作用引入词串成一条连续链，读者一眼看出它们是并列实例而非独立罗列；③ 若该子类的工作共享某一局限，用显式转折把 problem→solution 弧画出来。

骨架中的衔接词（The most straightforward / Building on that / Similarly / While… To address this…）仅示范连接的位置与功能，不是逐字复用的模板。实际撰写时按工作之间的真实关系选词并保持变化——递进、并列、对比、转折各有相应表达，不要所有段落、所有工作都套同一组衔接词，否则清晰会变成机械。中文版用对应的中文连接词。

注意：此为段落级骨架，不替代 Discussion；子类内部仍应贯彻准则 3（无冗余），章节层面的跨子类对比仍由 Discussion 承担。

## 2. 章节引入段与 Discussion 的分工

此处「引入段」指 pathway 章节自身的章首引入段，非整篇 survey 的 Introduction。

- 引入段只回答「这条 pathway 是什么、为何重要」，一两句，不展开。
- Discussion 给出跨子类对比，以及一个只有综合本章节全部文献才能得出的判断；凡能从正文直接推出的内容，不属于 Discussion。

## 3. 无冗余

文本不携带冗余信息。冗余指换一种说法把同一件事再说一遍——同义复述、反复铺垫、已在别处说过的内容再次出现。每一句都应携带前文尚未给出的信息。注意区分：承担 scope 界定或定位功能的短句（载体边界澄清、precursor 说明等）即使简短也不是冗余，删去会造成内部不一致或令读者归错类的句子必须保留。

## 4. Scope 始终明确

- 每篇被引工作，其满足纳入判据（决策过程语义、异构动作空间）的理由在文中可一句话说清。
- precursor、边界（boundary）、不完全合规的工作，在正文中显式标明身份，不与合规实例并列而不加说明。

## 5. 分类「做出来」，不「讲出来」

章节正文直接按分类组织文献，不含「本节将沿 X、Y 两维度区分」这类元叙述；「为什么这样分类」的 rationale 不在 pathway 章节内论证。

## 6. 术语精确且一致

- 全程使用统一术语：Carrier 命名（Tokenized / Narrative / Schematic / Latent / Parametric / Policy / Evaluator）、大小写、领域缩写前后一致。
- 同一对象只用一个术语指代，不用近义词轮换；不用宽泛词替代精确术语（如以 "hidden states" 笼统覆盖实际为 KV cache 的载体）。
- Modality 只作正交属性出现，不与 Carrier 类别并列。

## 7. 内部一致

交叉引用成立；引入段与 Discussion 与正文相互对得上；不存在被删概念仍在别处被引用的情况。

## 中文表达

直接陈述，不用反问句、不做铺垫式提问；不用「需要注意的是 / 值得指出的是」等提示语；不用「不是…而是…」作段落收尾；不用「从而 / 进而 / 综上所述」类报告腔；段落不以「由此可见 / 这说明」式总结句结尾。
