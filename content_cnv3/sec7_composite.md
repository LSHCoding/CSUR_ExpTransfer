# 7. Composite Transformations

§3–§6 的单路径各刻画经验在一对载体之间的单步转化。另一类方法把多个转化步骤串接或闭合成 pipeline,经验在 Narrative Tokenized、Schematic Tokenized、Policy 参数与 Evaluator 参数之间连续流动,相邻步骤的衔接机制（integration mechanism）本身是方法的主要贡献,而非任一单步转化。原始 agent trajectory 同时含有可复用策略、局部有效动作与噪声行为,单步转化难以分别处置这些异质信号;composite 以多阶段加工把它们组织成更可靠的训练、评估或改进信号。

本章识别出三种 composition pattern,各自的衔接机制作用于不同对象。Evaluator–Policy Co-Evolution（§7.1）的衔接作用于 Evaluator 与 Policy 两组参数之间的耦合,二者围绕新产生的经验相互校准、共同演化。Refinement-Mediated Policy Internalization（§7.2）的衔接作用于经验的内容,先把原始 trajectory 修正、补写或抽象,再内化进 Policy。Generative Experience Curation（§7.3）的衔接作用于经验集合的生成与分布,决定哪些经验被产生、哪些被保留、整体分布如何构成,再用于改进 Policy。

## 7.1 Evaluator–Policy Co-Evolution

Evaluator–Policy Co-Evolution 指 Evaluator 参数与 Policy 参数围绕 agent experience 相互校准、共同演化。抽象结构是经 Tokenized 中介的闭环:Policy 在环境中 rollout 产生新经验,这些 trajectory 一方面更新或校准 Evaluator 的评价能力,另一方面经 Evaluator 的 reward、critique、preference 或 verification 信号反向更新 Policy。Policy 行为随训练漂移,静态 Evaluator 会过时——识别不出新型失败模式、对新策略给出错误评价,Policy 也可能过拟合 Evaluator 偏差;让 Evaluator 跟随 Policy 演化以阻断这一退化。

co-evolution 最常见的形态是 Evaluator 与 Policy 作为两个独立模块交替更新。UI-Genie [Xia25e] 是一个完整实例:GUI agent 在环境中探索,reward model 为候选动作打分、筛出高价值行为回流为 policy 的监督,失败轨迹经后续 rollout 重新标注为可学习的步级信号、反过来刷新 reward model;两者多轮交替,reward model 始终跟随 agent 新探索的轨迹更新而不对新行为失效。MagicGUI-RMS [Li26n] 改用两个 reward model 分工,一个领域专用、一个冻结的通用模型,前者认可的动作回流为 agent 监督,两者判断分歧的样本回流为前者的训练数据。ECHO [Li26l] 把 critic 过时直接列为核心问题,其 critic 产出自然语言诊断而非标量分数,policy 据诊断修正、二者同步更新,使 critic 持续跟随 policy 的失败模式。RL Tango [Zha25y] 在数学推理中交替训练 generator 与 verifier,verifier 仅以最终答案的对错为学习信号,却产出塑造 generator 的步级验证反馈,generator 的新解法又不断给 verifier 提出新的判别难点。

RLAnything [Wan26u] 把这种耦合从两方扩展到 policy、reward model 与环境三方:reward model 随 policy 轨迹更新并反向驱动 policy,其归纳出的失败模式还用于动态调节任务难度。

Self-Guide [Wan26aj] 走到 Evaluator 与 Policy 共享参数的极限:同一个 agent 每步先生成一段 verbal self-guidance,该信号既在推理时引导动作、又在训练时充当内部奖励,闭环退化为单一模型上的 self-rewarding 回路。

## 7.2 Refinement-Mediated Policy Internalization

Refinement-Mediated Policy Internalization 先把原始 agent experience 加工成监督质量更高的 refined artifact,再内化进 Policy 参数,典型结构是 Narrative Tokenized → Narrative/Schematic Tokenized → Policy 参数。衔接机制作用于经验的内容——对 trajectory 修正、补写或抽象,改变其作为监督信号的语义。这类方法的前提是 raw trajectory 直接作监督仍有改进空间:失败轨迹可能含有正确前缀与局部有效动作,成功轨迹可能含有冗余动作或不可迁移的 shortcut,先经加工再写入参数能提升信号质量。区别于 §3 供检索的 Narrative Abstraction,本节 artifact 进入参数训练。

**Failure-Trajectory Rewriting.** 把失败或偏离轨迹改写为可用监督,最直接的形态是定位首个错误步骤、接上修正后续。Agent-R [Yua25c] 从 actor 自己的 MCTS 搜索树中区分成功与失败轨迹,定位失败轨迹的首个错误步,截断其后续、接上正确分支并插入修正信号,再以 SFT 把这一修正内化进参数。STeCa [Wan25x] 把粒度细到单步,用 Monte Carlo continuation 定位首个偏离 expert path 的动作,改写为带反思的修正动作后替换原片段。LEAFE [Ge26] 在 rollback tree 上为每个回滚点生成自然语言 summary 指导改进分支,再通过 counterfactual distillation 让 policy 在不读 summary 的条件下直接复现修正动作。CLEANER [Xu26j] 针对工具调用轨迹的噪声,在报错后按语义相似度自适应地决定只改代码、还是连同 reasoning 一起深改,把轨迹净化为干净版本。AgentHER [Din26] 改的不是动作而是目标:保持轨迹不变,按其实际达成的结果逆向生成一个被它满足的新目标,把失败运行重标为成功 demonstration。

**Posterior Reasoning Construction.** 为缺乏解释的轨迹补写推理或反思层,使只有动作的执行记录具备可训练的推理结构。ReAct Meets ActRe [Yan24m] 让 agent 探索得到动作序列后,由固定的 ActRe 模块反向补写每步的 reasoning,把无解释的动作序列重构为可训练的 ReAct 式轨迹,再经 contrastive self-training 内化。GUI-Reflection [Wu25b] 离线伪造错误、在线挖掘失败,自动构造含验证、回退、重试的反思行为数据,让 GUI model 习得反思与纠错。

**Privileged Abstraction Distillation.** 把轨迹抽象为更高层的 skill、knowledge 或 hint,作为训练期的特权信息蒸馏入不访问它的 student policy。Skill-SD [Wan26al] 把多轮轨迹总结为含成功分析、错误分析与 golden workflow 的结构化 skill,只注入 teacher、不给 student,再通过 reverse-KL 把 teacher 在 skill 引导下的改进分布蒸馏进无 skill 的 student。Online Experiential Learning [Ye26f] 把在线轨迹递增提炼为可迁移经验,同样经 context distillation 把带经验的 teacher 压成无经验的 student,并以对照实验证明先抽取再内化优于直接训练 raw trajectory。Memento No More [Ala25] 以纠正性 hint 为中介,reviewer 识别错误模式给出针对性 hint,teacher 在 hint 下产生更优行为,student 在不接收 hint 的条件下学会复现。

## 7.3 Generative Experience Curation

Generative Experience Curation 以经验的生成与分布构造为核心衔接机制,典型结构是 Policy 参数 → Tokenized → Policy 参数。policy 先外化出 trajectory 或 synthetic task,这些 Tokenized experience 随后被验证、筛选、搜索或重标,构造成贴近目标分布的训练数据,再用于改进 Policy。衔接机制作用于经验集合的生成与分布而非经验内容本身——决定哪些经验被产生、哪些被保留、整体分布如何构成。其前提是有限交互经验不足以支撑可靠的 policy learning,需主动扩展经验来源并控制其质量。

**Exploration-Driven Synthesis.** 以探索或合成主动扩展经验来源。OS-Genesis [Sun24b] 是一条典型路线:agent 在 GUI 环境中做交互式遍历、收集动作轨迹,再从观察到的功能反向合成高层任务、执行得到完整轨迹,并由一个 trajectory reward model 按完成度与连贯性打分、按分采样进训练集。AgentTrek [Xu24] 把任务来源换成网页教程,将其标准化为结构化任务规格后驱动 agent 在真实页面复现、生成多模态轨迹,再由 VLM 校验指令遵循与目标完成。AutoSurfer [Fai26] 以广度优先方式系统遍历网站、发现并组合任务,再让 agent 在真实站点补全为完整轨迹。OpenWebVoyager [He24e] 不依赖外部任务源,先以模仿学习得到初始 policy、再在自生成任务上探索,由冻结的 GPT-4o 对 rollout 做轨迹级拒绝采样,只把判为成功的轨迹混入下一轮训练。Bootstrapping Language-Guided Navigation [Wan24ad] 让 instruction generator 与 navigator 互相促进,navigator 用 SPL、nDTW 筛出高保真样本反向刷新 generator,形成自精炼飞轮。BLAZER [Das25] 则由强模型在模拟器中零样本生成控制程序,只保留可执行成功者去微调较小的操作模型。

**Quality Filtering.** 对生成的经验做验证与筛选,决定哪些经验、以何种粒度进入训练。[He25g] 指出整体成功的 CUA 轨迹仍含大量局部次优动作,于是对每一步打 0–10 质量分,只让高分步贡献监督损失、低分步仅作上下文保留。Language Feedback Model [Zho24e] 先把大模型对每个动作是否可取的反馈蒸馏成一个小型反馈模型,再用它筛出 rollout 中值得模仿的片段。DigiRL [Bai24] 在真实移动端用 Gemini 做二值评估,再以任务级 curriculum 与步级 doubly-robust 筛选选出最值得学的任务与动作。WebRL [Qi24] 从失败集扩展出新任务,先按难度与可行性筛任务,rollout 后再由 outcome reward model 与 actor 置信度筛出可用经验。PLD [Xia25h] 与 VARP [Sin25b] 把筛选前移到数据构造:前者用 residual actor 探查 base 模型的失败区、经 hybrid rollout 专门收集含恢复行为且贴近部署分布的成功轨迹,后者把 3D 运动投影成末帧上的 2D sketch、由冻结 VLM 生成 preference 标签训练 reward model 并丢弃无差别样本。

**Search-Based Preference Construction.** 以结构化 search 把单线轨迹重组为更密集的偏好或路径集合。MCTS-EP [Xu25q] 用 MCTS 扩展 embodied 轨迹空间,既提取成功路径做 SFT,又在分支节点按长程 value 构造偏好对做 DPO。Agent Q [Put24] 同样基于 MCTS 搜索树,结合节点 Q 值与 AI critique 把同层动作编译成节点级偏好再做 DPO。Trial and Error [Son24] 不用搜索树,直接收集失败轨迹、与专家成功轨迹配成失败—成功对比对做 DPO。Watch Every Step [Xio24] 用 Monte Carlo continuation 估计专家步与 agent 采样替代步的回报差,据此构造步级与轨迹级偏好对,以 step-DPO、outcome-DPO 与 SFT 联合把过程层面的局部优劣写入 policy。

## 7.4 Discussion

Composite 区别于单路径之处,是把经验从原始日志到可学习信号的中间加工本身当成设计对象。单路径要么默认这段加工不存在、直接以 raw trajectory 作监督,要么把它交给某个固定机制;composite 把它拆开、显式化,失败轨迹于是能被回收为修正后的监督,过程级信号能由闭环中的 Evaluator 持续供给,训练数据的分布能被主动构造——这些都是单步转化够不到的。代价与这份能力同源:被显式化的每个中间环节都可能出错,误差沿链累积。

出错以何种形式发生,取决于 pattern 把这段加工的着力点放在哪里:Evaluator 与 Policy 的耦合、单条经验的内容、还是经验集合的分布。耦合一侧,Evaluator 的训练数据若只来自当前 Policy,二者会一起滑向对外部任务无效的局部最优;内容一侧,refinement 一旦误判失败原因、或把偶然当通则,污染的就是监督信号本身;集合一侧,verifier 与 filter 的偏差被筛选反复放大,缺乏多样性约束的 flywheel 收敛到越来越窄的经验。三种失效追到同一处——加工被交给一个本身会出错的中介(Evaluator、refiner 或 verifier),它的偏差顺着 pipeline 成为结果的偏差;这类偏差又难以单独归因,中间环节的作用只能从最终性能间接读出、与其余环节交缠在一起,composite 的可信度因此高度依赖消融实验的完整性。

能否在中间环节施加纠错,取决于它是否可被外部检视——这一要求把几乎所有 composite 推向 Tokenized 中转,哪怕源端或终端是 Parametric:Tokenized 经验能被 verifier、reviewer、grader、reflection 直接读取、打分、改写,质控才能介入。Latent 作为单步转化(§4)已相当成熟,却几乎不进入 composite 的中间环节——它缺少让外部模块插入评估或修复的接口,一旦写错便难在闭环里被发现。

中间环节的设计成本同样解释了三类工作的数量分布。Refinement-Mediated Policy Internalization 借 LLM 已有的 reflection 能力即可启动,Generative Experience Curation 多半能复用现成的 reward model 或 verifier 做筛选,两者门槛低、实例也最多;Evaluator–Policy Co-Evolution 要专门设计 Evaluator 与 Policy 的同步更新、还要抑制 co-adaptation,门槛高、实例稀少。pattern 的边界本身也不密封:RLAnything 在 Evaluator–Policy 耦合之外让任务难度随失败模式调整,同时触及集合分布的构造;这类跨 pattern 的复合形态,连同 composite 与单路径之间的逐项比较,留待 §8。