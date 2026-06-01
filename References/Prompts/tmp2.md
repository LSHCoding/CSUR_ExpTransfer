先给出一版修改后的，我确定后再编辑到文件中。

关于Section 5 部分涉及的论文，其相关总结（大模型总结的）在

针对段落：
```
### 6.1.1 Discriminative Outcome Evaluator-to-Policy Transfer

判别式 outcome 评估器对完整输出或完整 trajectory 给出 scalar reward、trajectory-level score、pairwise preference 或 chosen/rejected label,policy 经 RLHF/RLAIF、preference optimization 或 filtered SFT 把这些可比较信号写入参数。这一格直接继承经典 RLHF 流水线,与现成的对齐工具链接口稳定。

**经典 RLHF 与 AI feedback 替代人类反馈。** Constitutional AI [Bai22b] 的 RL-CAI 阶段是这一格的母本:constitution-guided AI judge 对完整回答给偏好,训练出 preference model 后经 RLAIF 把 harmlessness 判断写入 policy。RLAIF [Lee23b] 沿同一思路系统比较了 off-the-shelf LLM 充当偏好标注与直接给分两种用法——canonical RLAIF 仍先训 RM,d-RLAIF 则把 judge score 当在线 reward;judge 为通用 LLM、不针对具体 agent experience 训练,对经验语义锚定较弱,在归属上属边界。

**在线化与自反式评估。** 把偏好标注从离线移到在线可避免 RM 随 policy 漂移而 off-distribution。OAIF [Guo24] 让在线 LLM annotator 对当前 policy 采样出的完整回答对给偏好,偏好不再蒸馏成独立 RM 而是直接进入 DPO/IPO/SLiC,保证监督分布始终 on-policy。自反式 Evaluator-Driven Optimization 进一步让源评估器与目标 policy 共享同一组参数:Self-Rewarding Language Models [Yua24] 让同一模型既作 generator 又作 judge,自评分构造 winner-loser pairs 后以 iterative DPO 回灌;Meta-Rewarding Language Models [Wu24d] 在此之上加入 meta-judge 改进 judge 自身评分质量,形成 actor/judge/meta-judge 共演化。

**Best-of-N distillation 与 filtered SFT。** 这组工作不走 on-policy RL,而是用评估器筛出高分样本后做监督式写入,以更低算力逼近 RL 的对齐效果。RAFT [Don23] 用 RM 对同 prompt 多条回答打分、保留 best-of-K 做 SFT。BOND [Ses24] 把推理时的 Best-of-N selection 蒸馏为单次采样 policy,以 forward/backward KL 逼近 RM 定义的 BoN 分布。BoNBoN [Gui24] 离线刻画 best-of-n 分布,通过 SFT-BoN 与 IPO-BoN 把最优与最差样本同时纳入。在 agent 域,[Gon24b] 的 critic LLM 对整条 trajectory 评分,top p% 高分轨迹作为伪示范配合通用数据做迭代 SFT。

**稳定性、去偏与多评估器。** policy 持续针对一个 imperfect 评估器优化会放大 reward hacking、length bias 与 judge bias,这组工作针对这一点设计 regularization 与 ensembling 机制。[Ack26] 把 reward hacking 解释为 policy 利用 proxy reward 的尖锐高点,在 Dr.GRPO 风格的 RL 目标上加入 gradient regularization 与 reference reset。Policy Filtration [She24c] 只让 RM 最可靠的高低分样本进入 PPO buffer。[Wu25x] 用 Bayesian router 在多个 trained RM 间按 query 动态选路,将 routed preference pairs 用于 online DPO。Mixture of Judges [Xu24d] 把 calibrated RM、LLM judges 与 rule-based constraint judges 的判断注入 CRPG/CODPO/CRRAFT,以多评估器结构抑制单点偏置——其中规则约束部分严格而言不属 Evaluator-Driven Optimization,但参数化评估器仍是核心信号源。[Fis24] 把 RM 的 reward difference 蒸馏进 policy 的 implicit reward,用 L2 distillation loss 加 forward KL 正则做离线更新。[Ren26b] 让 LLM judge 通过 meta-question 的 YES 概率合成 scalar reward,经 GRPO/CISPO 更新 policy;其 judge 可 frozen、self-eval 或 ensemble,与 [Lee23b] 同属 off-the-shelf judge 边界。

**步级诊断压缩为轨迹标量。** 评估器内部具备步级诊断能力,但落到 policy 上的 artifact 仍是轨迹级标量,粒度归属以后者为准。FAPO [Din25b] 的 generative RM 定位 first invalid step,该诊断被压缩成对整条 rollout 的 penalty 后才进入 GRPO。[Che25v] 的 step-wise judge 对推理链做 first-error identification,转成 trajectory 的 partial-correctness 标量,使 all-negative groups 也能产生梯度。OS-Themis [Li26p] 内部含 milestone verifier 与 trajectory judge,但在线 RL 主信号是 trajectory-level reward。
```

针对你的改写稿，我的意见：
1. 我觉得 6.1.1 最大的问题是，分的 5 个子类好像和 6.1.1 的引入段没有对应起来。另外我感觉 6.1.1 的 5 个子类好像也不是很合理。你参考相关论文的总结（P6.describe.md），尝试重新对这部分的论文进行分类，我感觉最多最多不能超过超过 4 类。另外目前每类的名字感觉也有问题。很多类的名字，读起来感觉怪怪的。

你有意见也可以提出。

注意：**独立评估**：从客观、专业的角度判断该修改意见是否合理。不要迎合我的立场，给出有依据的理由（逻辑、学术规范、表达效果等）；


1. “这一格直接继承经典 RLHF 流水线,与现成对齐工具链接口稳定。” 感觉可以去掉
2. “等 RL 目标最大化它”，不知道这个目标是指什么？
3. “的 RL-CAI 阶段是这一类的母本:” 感觉最好不要给出这个带主观的判断，建议去掉，直接进行描述
4. “系统比较了 AI 反馈的两种用法”，但是后面也没有比较相关的结论？如果没有的话，感觉不要这个半句会比较好。
5. “,与下文 [Ren26b] 同属 off-the-shelf judge 边界”，感觉去掉会比较好一点
6. “另两项针对 policy 长期优化 imperfect 评估器引发的 reward hacking”，感觉直接说 “XXX 和 XXX 针对 policy 长期优化 imperfect 评估器引发的 reward hacking”。然后后面再给出一点详细的描述。
7. “还有一组评估器具备步级诊断、但压缩为轨迹标量后才进 RL 的工作落在 outcome 一侧(与 §6.1.3 接壤)”的问题和 6 是一样的。
8. “另两项提升偏好优化的稳健性:[Wu25x] 用 Bayesian router 按 query 在多个 RM 间动态选路,把路由后的偏好对送入 online DPO;[Fis24] 在离线设置下把 RM 的 reward difference 经 L2 distillation 与 forward KL 正则蒸馏进 policy 的 implicit reward,提升 label bias、distribution shift 下的稳定性。” 的问题和 6，7 是一样的。
9. “在 agent 域,”，本身就是 Agent 领域，这个可以去掉。


先给出一版修改后的预览后，等我通过后再编辑进文件。

查看关于每篇论文的总结（在文件`paper_summary/P4.describe.md` 和 `paper_summary/P5.describe.md` ）,不要按领域来分，而是按 Evaluator output 的信号来分，比如二分的，更细分类的等。这种分类只是我的提议，你可以看看有没有更好的分类方式。

你可以查看关于每篇论文的总结（在文件`paper_summary/P4.describe.md` 和 `paper_summary/P5.describe.md` ）
先认识思考一下该怎么修改，思考清楚之后再开始修改，给出一版修改的，但是先不要对原文进行编辑（需要等我给意见并确认了，再编辑）。

评估器信号写入 policy 的吸收机制

要求：每篇工作的的描述应该贴着对应段、对应章节的主题来写，一些无关的信息不用保留（比如一些无关紧要的技术细节），后面的论文应该关注带来的增量信息。整个描述都应该是详略得当，而不是全部都非常的详细；对于某些有举例子的地方，要注意是否有重复（比如 scalar reward、trajectory-level score、pairwise preference 或 chosen/rejected label）；该翻译为中文的地方翻译为中文（除了英文的专有名词）。重构完，长度应该会精简一些。