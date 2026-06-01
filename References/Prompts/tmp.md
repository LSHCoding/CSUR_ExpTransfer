先给出一版修改后的，我确定后再编辑到文件中。

关于Section 5 部分涉及的论文，其相关总结（大模型总结的）在

针对段落：
```

```

针对你的改写稿，我的意见：
1. 我觉得 6.1.1 最大的问题是，分的 5 个子类好像和 6.1.1 的引入段没有对应起来。另外我感觉 6.1.1 的 5 个子类好像也不是很合理。你参考相关论文的总结（P6.describe.md），尝试重新对这部分的论文进行分类，我感觉最多最多不能超过超过 4 类。另外目前每类的名字感觉也有问题。很多类的名字，读起来感觉怪怪的。

你有意见也可以提出。

注意：**独立评估**：从客观、专业的角度判断该修改意见是否合理。不要迎合我的立场，给出有依据的理由（逻辑、学术规范、表达效果等）；


我的一些意见：
1. “目标端是 agent trajectories、tool-use demonstrations、GUI/web interaction traces、step-level labels、critiques、preference annotations 等(承载参数的模型可由 LLM、VLM、VLA 任意 modality 实现)” 中，不同的示例之间有重复，比如 “tool-use demonstrations” 也可以算是 “agent trajectories”。其实主要分为 2 类，Policy 尝试的 Agent trajectory，和 Evaluator 产生的 XXX（你来想一个总括的词）。 注意，举的例子之间最好不要有语义的重复。“(承载参数的模型可由 LLM、VLM、VLA 任意 modality 实现)” 可以去掉
2. “它与 Policy Internalization 方向相反——后者把离散经验写入参数,本路径从参数中读出可复用的经验表达,仍满足经验语义锚定与经验内容承载两个条件。” 感觉意思有点重复。放在 Section 8 可能比较好，先注释掉。
3. “与其余六条路径的真正差异在 source 的形态:它不是一条确定的 trajectory,而是聚合态的参数” 这句话也有问题。 什么是聚合态的参数？P6 的source 也是参数。
4. “聚合-采样这一性质带来两个组织性后果:采样有方差,低质量样本须由 verifier 或 filter 事后剔除,本路径方法几乎无一例外挂载验证环节;采样可重复并保留最优样本,带来 best-of-N 效应——在筛选后的 teacher 数据上训练的 student,其可靠性可高于 teacher 单次采样的平均水平。” 一方面，写了用 “verifier 或 filter” 过滤，感觉和 P5，P6 分不清楚了，另一方面，感觉这句话放到 Section 8 比较合适。整个 6.2 关注的是如何将参数中的经验外化出来，至于外化出来的样本如何 verifier 或 filter 事后剔除，则不是这部分主要关心的。
5. “分界在 Evaluator 判断的去向——被物化为独立可复用的监督数据则归后者,仅作内部过滤开关则仍是前者的质量控制环节。” 去掉，你的这个解释并不清楚，而且容易搞混。
6. “(消费方式是 SFT 还是 RL 不改变 artifact 的载体属性,归类依外化 artifact 本身的形态)” 去掉。
7. “组织轴是环境合成度,锚定在 observation o上:” 这句话有点像元分类标准，这种风格的叙述不适合出现在 Survey 中
8. “Teacher 在真实网站、MCP server 或操作系统上交互”，3 个例子太具体了。不适合放在开头的引入局。可以改为与真实环境做交互，比如 XXX 的风格
9. “Log26b” 的“[]” 好像漏掉了
10. “,失去真实环境的客观性” 建议放到 discussion 中
11. “Xu26e”的“[]” 好像漏掉了
12. “以上目标载体多为 Narrative trajectory,本路径同样支持 Schematic 形态:FABRIC [Ver25b] 经 LLM-only pipeline 生成 task/tool schema、policy pseudocode、dialogue 与 execution trace,其中 pseudocode 与 schema 属 Schematic Tokenized,构成 Parametric Externalization → Schematic 子格;TOUCAN 与 ToolACE 的 tool-call 部分亦含明显 Schematic 成分。” 先注释掉。
13. “student、agent、data filtering 或 reward-model training 消费;”，一个是举例子可能有语义重复，另一个是“消费”太口语化了
14. “与 Demonstration Externalization 外化"如何行动"不同,” 感觉可以去掉
15. “critique、step-level label、action correctness、progress label、preference pair、verification trace 与 failure diagnosis” 思考一下有没有语义重复
16. “——它同时外化 Policy 与 Evaluator 两端,evaluator 判断被独立物化为后两者的内容主体,超出了通常的过滤开关角色。” 感觉可以去掉。
17. 6.2.3 discussion 也需要再重新思考一下。
18. “一次性推理换取近乎任意规模、可定向的监督数据”，一次换任意？感觉这个说法有点矛盾。第一段的用词要再仔细思考一下。
19. “本路径也是 {teacher} 这一经验来源的制造工艺,{teacher}-sourced experience 几乎全部经由它进入语料;它与 Policy Internalization 构成方向相反的对偶,二者常以 P7 → P5 串接——teacher 外化产生 student 训练数据,student 再做 internalization。”，不要用 制作工艺 这种类比。Survey 中应该用直接、准确的表述。


1. “Refinement-Mediated Policy Internalization（§7.2）的衔接作用于单条经验的内容,先对个别 trajectory 反思、修复或抽象,再内化进 Policy。” 它的衔接不一定是作用于单条经验的内容，而且反思的得到的东西也不一定是根据一条 trajectory 得到的，所以我觉得这个地方表述有误。
2. “Policy 行为随训练漂移,静态 Evaluator 会 stale”，我觉得 stale 还是翻译出来比较好。
3. “标准 actor–critic 中 critic 的常规联合更新不归入本类,只有 Evaluator 与 Policy 的协同演化本身作为被贡献的设计要素时才计入。” 这句话我觉得可以不要，因为前面的表述已经包含了这句话的意思。
4. “ECHO [Li26l] 把 critic staleness 列为 open-world agent learning 的核心障碍,policy 产生 on-policy trajectory,critic 给出多视角自然语言诊断,policy 据此做 conditional refinement,二者在初始轨迹、诊断、修正轨迹上做 dual-track GRPO 更新,并以 saturation-aware gain shaping 维持 critic 对高分区间细微改进的敏感性。” 这句话中英文太多了，而且有特别多的技术细节，反而好像没有紧扣这个字节的主题。
5. “同一耦合在其他场景延伸出变体。”，这句话的感觉像是前面几个工作是基础，接下来的几个工作是延伸。但是它们时间上的先后顺序好像不是这样的，所以我觉得这句话的表述会有一些歧义。
6. 在整个“7.1 Evaluator–Policy Co-Evolution”，我觉得方法的表述有一些相对集中的问题。第一个是英文过多，第二个是每个方法好像描述得都很详细。我希望的表述是，开始一两个比较详细，后面的工作着重突出增量的部分。另外这些方法好像是按领域来区分的，不能说一定不合适，但是可以思考一下有没有更好的方式。



针对 “7.2 Refinement-Mediated Policy Internalization” 部分

1. “转化为更可学习的 refined artifact”，这个更可学习，感觉表述的有问题，理论上来说 “refined artifact” 是一种更难学习的东西。当然，这个更难学习是指学习到参数当中。
2. “对 trajectory 反思、修复、校准、净化、补写或抽象”，感觉举的例子很多，可以思考一下是否有语音上的重复
3. “本节方法否定"raw trajectory 本身即可靠监督”，这个否定的表述感觉太绝对了。因为大部分的还是用raw trajectory来进行监督的。
4. “refined artifact 进入训练而非停留在 inference-time context,这一点区别于 §3 以保留供检索为目的的 Narrative Abstraction。”，这个表述感觉有点冗余。
5. “一类工作” 感觉可以删掉
6. 同样，在整个“Refinement-Mediated Policy Internalization”，我觉得方法的表述有一些相对集中的问题。第一个是英文过多，第二个是每个方法好像描述得都很详细。我希望的表述是，开始一两个比较详细，后面的工作着重突出增量的部分。
7. “提示被逐轮压入 LoRA adapter” 感觉有点太技术细节了


针对 “7.3 Generative Experience Curation” 部分

1. “Policy/Teacher”， “Policy 或 teacher model” 感觉这个policy和teacher其实是指同一个东西，我建议还是用policy
2. “trajectory、demonstration、interaction trace 或 synthetic task”，感觉有明显的语义上重复
3. “经验需被主动扩展并被质量控制。” 感觉有语病
4. 同样，在整个“7.3 Generative Experience Curation”，我觉得方法的表述有一些相对集中的问题。第一个是英文过多，第二个是每个方法好像描述得都很详细。我希望的表述是，开始一两个比较详细，后面的工作着重突出增量的部分。





先给出一版修改后的预览后，等我通过后再编辑进文件。

查看关于每篇论文的总结（在文件`paper_summary/P4.describe.md` 和 `paper_summary/P5.describe.md` ）,不要按领域来分，而是按 Evaluator output 的信号来分，比如二分的，更细分类的等。这种分类只是我的提议，你可以看看有没有更好的分类方式。

你可以查看关于每篇论文的总结（在文件`paper_summary/P4.describe.md` 和 `paper_summary/P5.describe.md` ）
先认识思考一下该怎么修改，思考清楚之后再开始修改，给出一版修改的，但是先不要对原文进行编辑（需要等我给意见并确认了，再编辑）。

评估器信号写入 policy 的吸收机制

要求：每篇工作的的描述应该贴着对应段、对应章节的主题来写，一些无关的信息不用保留（比如一些无关紧要的技术细节），后面的论文应该关注带来的增量信息。整个描述都应该是详略得当，而不是全部都非常的详细；对于某些有举例子的地方，要注意是否有重复（比如 scalar reward、trajectory-level score、pairwise preference 或 chosen/rejected label）；该翻译为中文的地方翻译为中文（除了英文的专有名词）。重构完，长度应该会精简一些。