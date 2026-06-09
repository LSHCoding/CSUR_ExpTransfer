# 8. Cross-Pathway Synthesis

§3–§7 按转化路径逐一梳理了社区将 agent experience 从一种载体重新表示为另一种载体的机制。但构建 agent 系统时面临的问题天然横跨这些路径:同一份 trajectory,该走 P1 提炼成 reflection 供检索复用,还是走 P5 固化进权重以换取零边际推理成本?决定一旦做出,经验的可解释性、可编辑性、推理效率、维护成本便被锁定在一个特定的 trade-off 剖面上,后续修正代价高昂。现有文献按"组件"(Memory / Planning / Tool Use)或"技术"(RAG / SFT / RLHF)切分,都无法为这类跨路径选择提供分析工具——它们各自在单一载体或单一路径内部提供纵深覆盖,但没有一个框架告诉你不同路径在什么条件下更优,以及为什么更优。

本章从 §3–§7 的 method-level 细节中抽身,站到 pathway-level 和 carrier-level 做结构性合成。它不引入新文献,而是用已有的文献证据建立三条生成性原则(§8.1),用这些原则统一解释七条路径的生产代价差异(§8.2)与五类载体的消费特性差异(§8.3),最后将这些差异放入任务约束的透镜下交叉,推导利用驱动的路径选择逻辑(§8.4)。

## 8.1 Three Generative Principles

§2.3 定义了五类载体在 Tokenized → Latent → Parametric 谱系上的位置,§2.4 定义了七条转化路径的源端与目标端。但载体分类和路径定义回答的是"是什么",没有回答"为什么"——为什么 Narrative 的消费成本是按次支付的 context token,而 Policy 是零边际?为什么 Tokenized → Tokenized 的两条路径只需 LLM inference,而 Tokenized → Parametric 的三条路径都需要 gradient-based training?为什么复合路径(§7)主要围绕 Policy 展开,而 Evaluator 几乎总是终点站?

这些不是孤立的经验观察。它们背后有三条结构性约束——carrier 的存在形式、形式化程度、功能角色——各自锁定了该载体及其生产路径在某个维度上的行为。本节将这三条约束显式化为生成性原则,作为后续三节分析的统一坐标。

### 8.1.1 Existence-Level Principle

> Carrier 在 Tokenized → Latent → Parametric 谱系上的位置,同时决定了它的消费接口、每用成本、控制自由度与可追溯性。这些维度不是独立变化的——它们被存在层次单调地锁定。

推导从 agent 决策规则 $a_t \sim \pi_\theta(\cdot \mid c_t)$ 出发。经验的消费方式只有两种结构可能:经验进入 $c_t$(外部、显式,参与当前上下文的前向传播),或经验进入 $\theta$(内部、隐式,固化在模型参数或中间状态中)。Carrier 的存在层次决定了它走哪条路。

Tokenized 载体以离散符号存在于模型外部。它的消费接口必然是 context injection——经验必须先被检索、再被编码进 $c_t$。每用成本因此包含检索延迟与 context processing 的 prefill 开销,且随经验体量增长而恶化(context window 容量有限、检索精度随 store 增大而下降)。但离散符号的另一面是独立可寻址:每条 reflection、每条 rule 可被单独定位、阅读、编辑或删除,无需触动其他条目。控制自由度高,可追溯性高——你可以追问"这条决策引用了哪条经验",并得到可读的答案。

Parametric 载体以连续权重存在于模型内部。它的消费接口必然是 forward-pass computation——权重恒在,前向传播自动激活,不需要检索、不需要额外 context token。每用成本为零边际。但权重的代价是丧失独立寻址:单条经验的贡献被 batch 梯度累积所淹没,无法在推理时选择性激活"这一条经验而非那一条"。控制自由度近乎零——你不重新训练就无法增删改任何经验。可追溯性近乎零——你无法追问"这个决策用了训练集中的哪条轨迹"。

Latent 载体位于两者之间。消费接口是 forward pass 中的 attention integration——不需要额外的 token 编码,但需要选择加载哪个 latent bank 或哪些 KV cache。每用成本低但不为零(attention 计算本身有开销,latent bank 的检索也有开销)。连续向量不可直接阅读,但可被选择性加载(选哪个 session、哪个 bank)。控制自由度与可追溯性居中。

沿 Tokenized → Latent → Parametric 谱系,图 8.1 刻画了一条单调曲线:

```
可解释性 / 可编辑性 / 可追溯性 / 控制自由度
    ↘
      Tokenized ──── Latent ──── Parametric
                                        ↗
              推理效率 / 体量可伸缩性
```

这不是五类载体的经验总结,是存在层次的结构推论。由此得出一个强的否定性陈述:**没有任何 carrier 可以同时拥有"零边际推理成本"和"高可解释性"。** 声称"既快又透明"的方案必然在载体的存在层次上有模糊——它要么实际上在维护一份 Tokenized 副本供审计(那是两套载体,不是一套),要么"透明"指的是某种近似解释(probing、attribution)而非真正的可读。

存在层次原则贯穿 §8 的全部后续分析。对 §8.2(生产侧),转化路径是跨存在层次(P3/P4/P5/P7)还是同层内(P1/P2/P6),比目标 carrier 的选择更根本地决定了生产成本与信息损失的规模。对 §8.3(消费侧),五类载体的消费画像不是五个独立的数据点,而是同一条曲线上沿谱系位置的五个采样点。对 §8.4(选择侧),利用驱动的选择在根子上是存在层次的选择——先决定经验应该放在谱系的哪个区间,再在区间内选具体的 carrier 子类。

### 8.1.2 Formalization Principle

> 在 Tokenized 层内,Narrative → Schematic 的形式化程度差异决定了经验是被理解消费还是被机制性消费,进而决定了产物的可验证性属于不同类别——而非不同程度的"高可验证性"。

存在层次原则解释了 Tokenized 与 Parametric 之间的差异。但 Tokenized 层内部有两个子类——Narrative($\mathcal{C}^T_N$)与 Schematic($\mathcal{C}^T_S$)——它们共享 context injection 的消费接口,却在可验证性上存在同质异构的差异。这个差异无法被存在层次原则解释(两者在同一层次),需要第二条原则。

Narrative 通过 language / multimodal understanding 消费。Agent 将一段 reflection、一条 rule、一组 summary 注入 context,依赖模型的语言理解能力从中提取决策指导。它的验证只能靠"读"——人类审阅者或强 LLM 判断这段经验的内容是否正确、是否与当前任务相关、是否与已有经验冲突。这种验证是语义级的,覆盖"说得对不对"。但它有三个内在局限:(i) 主观——两个审阅者可能对同一 reflection 的质量判断不同;(ii) 不保证执行——一段被判定为"正确"的 reflection 可能在实践中无法被 agent 有效使用,即"说得对但做不到";(iii) 验证据的是语言理解能力,而 agent 在推理时的语言理解可能与验证者不同。

Schematic 通过 parsing / execution / traversal 消费。一段 code skill 被 executor 执行,一个 workflow DAG 被 engine 遍历,一个 knowledge graph 被 graph query 检索。它们的验证靠"跑"——execution test 给出客观的通过/失败信号,parsing 给出客观的语法正确/错误信号。这种验证是形式级的,覆盖"跑不跑得通"。它不依赖主观判断,测试覆盖度是可量化、可扩展的。但它的盲区恰是 Narrative 验证的强项:一段"跑得通"的 code skill 可能实现的是错误的功能,一个"语法正确"的 workflow 可能编码了错误的任务分解。

两种验证覆盖不同类别的错误。Narrative 验证漏掉的是"说得好但做不到"的经验,Schematic 验证漏掉的是"跑得通但方向错"的经验。两者都是"高可验证性",但不是同一种可验证性——不是程度的差异,是类别的差异。

形式化原则的分析后果直接进入 §8.2 的路径对比和 §8.4 的安全性约束分析。对 §8.2:P1 和 P2 虽然同属 Tokenized → Tokenized 同层转化,但 Output Verifiability 是不同质的——P1 的验证是"读"的主观判断,P2 的验证是"跑"的客观测试。对 §8.4:当任务的安全关键性来自"不能做错事"(execution safety),应偏向 Schematic——可以在部署前通过 testing gate 阻断错误 action;当安全关键性来自"不能理解错"(semantic safety),应偏向 Narrative——人类可以在经验进入 context 前审查其内容。

### 8.1.3 Functional-Role Principle

> 在 Parametric 层内,Policy → Evaluator 的功能角色差异决定了载体在 pathway 图中的拓扑位置——Policy 是枢纽节点,Evaluator 是汇节点。这不是经验观察,是功能角色的定义直接蕴含的图论性质。

存在层次原则解释了 Parametric 层与 Tokenized 层的差异。但 Parametric 层内部有两个功能角色截然不同的子类——Policy($\mathcal{C}^P_\pi$)与 Evaluator($\mathcal{C}^P_\phi$)。两者的消费接口都是 forward-pass computation,成本为零边际,可追溯性都近乎零。但它们在一个关键维度上分化:它们在 pathway 图中能走到哪里。

Policy 的功能角色是产生 action。Action 在环境中执行后产生新的 trajectory(observation 序列)。Trajectory 是 Tokenized 载体——这意味着 Policy 的每一次使用都自动产生可被任何以 Tokenized 为源的 pathway(P1/P2/P4/P5/P7)消费的产物。Policy 通过 P7(Parametric Externalization)显式外化、通过 rollout 隐式外化,重新进入整个 pathway 图。在 7 条路径构成的有向图中,Policy 可以通过 P7 出、通过 P5 回,形成闭环——它是强连通分量成员。

Evaluator 的功能角色是产生评估信号——标量分数、偏好标签、critique 文本。评估信号只有一种有意义的消费方式:用于更新、选择或引导 Policy。如果不与 Policy 结合(P6),评估信号无处可去。在 pathway 图中,Evaluator 只有入边 P4(Evaluator Internalization)和出边 P6(Evaluator-Driven Optimization)。它是汇节点。

这条原则不是经验性的——不是因为社区尚未探索 Evaluator 的其他下游用法,而是评估信号的语义本身就是"对行为的判断",它的消费方天然是行为的生产者。你可以想象用 Evaluator 信号来更新另一个 Evaluator(那是 P4 的增量训练,不构成新 pathway),或用 Evaluator 信号来筛选 Tokenized 经验(那是 Evaluator 作为 filter 在 P1/P5 的 preprocessing 中使用,不建立 Evaluator → Tokenized 的独立转化路径)。这些都不是 Evaluator 作为源端进入新 pathway,而是 Evaluator 作为工具辅助已有 pathway。独立的新 pathway 要求 Evaluator 的经验被重新表示为另一种载体——这等价于把评估标准转化为生成能力,而唯一已知的机制就是 P6。

功能角色原则解释了 §7 中一个显著的模式:复合路径主要围绕 Policy 构建。§7 识别的三类 composition pattern 中,Evaluator–Policy Co-Evolution(§7.1)的衔接作用于 Evaluator 与 Policy 之间的耦合,Refinement-Mediated Policy Internalization(§7.2)以 Policy 为终点,Generative Experience Curation(§7.3)以 Policy → Tokenized → Policy 的自生成环为核心。这不是研究偏好的偶然——Policy 在图中的 hub 位置使其天然成为复合路径的锚定节点。Evaluator 则相反:一旦经验到达 Evaluator,它在 pathway 图中的旅程就结束了(唯一的出路是进 Policy)。选择 Evaluator 作为目标载体,意味着接受经验管理的终端化。

三条原则覆盖了 carrier 空间中的三个正交轴:存在层次(经验在架构中的位置)、形式化程度(在 Tokenized 层内,经验的消费方式)、功能角色(在 Parametric 层内,经验在 pathway 图中的拓扑命运)。每条 carrier 在这三个轴上的坐标——而非它叫什么名字——决定了它的生产代价画像(§8.2)和消费代价画像(§8.3)。后续两节的每一个分析维度,都可以追溯到这三条原则中的至少一条。

---

## 8.2 Pathway Trade-off Comparison

Pathway comparison 的分析对象是**转化操作本身的结构特性**,而非目标载体的静态属性。这条边界线在写作上极易越过却必须守住:本节的目标不是比"Policy 和 Narrative 谁更可解释"——那是 §2.3 已经完成的 carrier 属性比较。本节的目标是比"从 trajectory 到 reflection 的转化(P1)和从 trajectory 到 policy weights 的转化(P5)在信息损失、生产成本、增量能力上的差异"。前者比的是载体,后者比的是转化——角度不同,结论不同。

例:"Policy 可解释性低"是 Policy carrier 的属性,如果用它描述 P5 的 trade-off,它同样适用于 P4(也是 Parametric 产物),却不适于 P6(产物也是 Policy,但代价画像完全不同)。真正属于 P5 的 trade-off 是:它需要大规模 trajectory 作为输入,通过 gradient-based training 执行转化,信息损失可能来自欠拟合或 reward hacking 而非有意抽象,产物不可追溯到单条源经验,新增经验需要重新训练。这些是 P1 完全没有的特性——不是程度差异,是结构性差异。

下面按转化操作的三个截面——输入侧、转化过程、输出侧——组织七个维度的分析。同一截面内的维度共享视角,便于跨路径对比。

### 8.2.1 Input-Side Dimensions

#### Source Carrier

源载体类型直接来自 pathway 定义。7 条路径的源端分属两个集合:以 Tokenized 为源的有 P1/P2/P3/P4/P5(共五条),以 Parametric 为源的有 P6/P7(共两条)。Tokenized 源的共同特征是输入可读、可审计、可逐条筛选——你可以检查每条 trajectory 的质量再决定是否用于转化。Parametric 源的共同特征是输入不透明——P6 以 Evaluator 权重为源,P7 以 Policy 权重为源,两者的内部经验分布都无法直接检查,转化质量高度依赖源权重的质量与校准状态。

这个维度是恒定的,列出的目的不是比较,而是为每行建立身份。

#### Data Prerequisite

七条路径对输入数据的要求差异跨三个维度。

**Volume**。单条 trajectory 的粒度区分了轻量转化与重训练转化。P1(单轨迹变体,如 Reflexion [Shi23b])和 P2(单 skill 生成,如 Voyager [Wan23c])可以在一次 trial 结束后立即执行,不需要等待经验积累。P1 的跨轨迹变体(如 AutoGuide [Fu24]、ExpeL [Zha23c])和 P7 需要多条 trajectory。P3(Cache-Based)跟随一次 session 即可构建。P3(Prompt/Module-Based)、P4、P5 需要大规模训练数据——从数百到数百万条 trajectory 不等。P6 的数据量需求取决于 Evaluator 的类型与部署方式:online RL(如 OAIF [Guo24])在 rollout 流上持续更新,所需 trajectory 量由训练步数决定;offline DPO 则需要预先构造的 preference pair 集合。

**Quality Signal**。监督信号的类型决定了哪些经验可以被转化。基本梯度如下:

- **仅需 trajectory 本身**(无显式监督):P1 和 P2 可以从未标注 trajectory 中抽取 insight、skill、workflow,不要求 success/failure 标签。失败轨迹可以通过事后分析暴露错误模式(如 Reflexion 的 failure reflection),成功轨迹可以用于归纳可复用策略。
- **需要 outcome-level 信号**(弱监督):P4 的 outcome-supervised Evaluator 需要 trajectory-level 的 success/failure 判断或 pairwise preference。P5(SFT 变体)通常需要筛选后的成功轨迹或高质量 demonstration。P7 的 generation quality 常依赖采样时的 outcome 筛选。
- **需要 process-level 信号**(过程监督):P4 的 process-supervised Evaluator(如 PRM)需要 step-level 的正确性标注。P6 的 discriminative process evaluator 变体需要步级价值估计或质量分。
- **需要人类偏好标注**(强监督):P4 的 RM training 的标准范式需要 human preference label。P6 的 canonical RLHF 管线共享这一需求。
- **需要成功信号 + 环境执行反馈**:P2 的 Programmatic Skill Construction 除 trajectory 外还需要执行验证闭环——code skill 生成后需在环境中实际运行并通过测试才入库。

**Source Diversity**。经验来源限制了转化的适用范围。P1/P2/P3/P5/P7 可以使用 agent self-generated trajectory,也可使用 human demonstration 或 teacher model 合成的数据。P4 的 RM training 通常依赖 human label,但 AI-generated preference(如 Constitutional AI [Bai22b])在逐步减少对人类标注的依赖。P6 的 Evaluator-to-Policy 环节原则上不接触原始经验来源——它的输入是 Evaluator 产出的信号,经验来源的多样性已在 P4 阶段被折叠进 Evaluator 权重。

#### Input Robustness

转化操作对噪声输入的容忍度差异悬殊。P1 的设计天然包含噪声处理:reflection 机制专门从失败轨迹中提取诊断信息,跨轨迹归纳机制通过多轨迹比较滤除偶然因素——噪声恰是 P1 的输入素材。P2 的 Programmatic Skill Construction 通过 execution verification 过滤噪声:不合格的 skill 在测试阶段被淘汰,不入库。P3(Cache-Based)直接保存前向传播产生的 KV,不主动去噪——噪声轨迹的 KV 同样被保存,检索时可能被召回。

P5(SFT)对噪声敏感。训练数据中的低质量 trajectory 会直接降低 policy 质量。社区的做法是预先筛选——仅用成功轨迹或高分 trajectory 做 SFT,但筛选标准本身可能引入 bias(只保留某种风格的 trajectory)。P5(RL)对噪声的敏感度进一步放大:reward hacking 恰恰是 policy 利用了 reward signal 中未被意图的噪声模式。P4 的标注噪声(标注者不一致、偏好标签错误)会直接进入 Evaluator 的权重,且难以事后检测。P6 的输入噪声来自 Evaluator 本身——一个校准偏差的 Evaluator 会系统性误导 Policy。

---

### 8.2.2 Process-Side Dimensions

过程侧四个维度构成了 pathway comparison 的分析核心。它们刻画转化操作本身的代价、信息动态与维护特性,是 carrier 属性完全覆盖不到的。

#### Transformation Semantics

转化操作对经验做了什么性质的重新表示?这是对一条 pathway 最基础的定性——不同的转化语义决定了信息被如何组织,以及哪些后续操作是可能的。

**P1 Narrative Abstraction** 执行语义抽象:原始 trajectory 中的具体步骤、时序细节、环境特异性被过滤,保留跨任务可迁移的规则、模式、洞察。它不改变信息的存在层次(tokenized 层内),但改变信息的组织方式——从按时间展开的序列($e_1, e_2, ..., e_T$)变为按主题或功能组织的条目(reflection about X, rule about Y)。这种重新组织的代价是序列中的因果结构可能丢失——reflection "在这个场景下应该先检查 B 再做 A"省略了原始 trajectory 中发现这一规则的具体失败过程,未来 agent 只能信任这条结论而无法回溯其经验依据。

**P2 Schematic Formalization** 执行结构形式化:从自然语言的 trajectory 中抽取可被 parser 或 executor 识别的语法结构。它不直接做语义抽象——Voyager 生成的 Mineflayer JavaScript program 保留了 trajectory 中的具体动作,但将它们编织为带控制流(loop、conditional)和参数化的可执行单元。形式化的增益是精确性:code skill 的行为是确定性的(给定输入,输出可复现),不像 Narrative reflection 那样可能被模型在不同 context 下做出不同解读。形式化的代价是自然语言中的"软信息"——隐含假设、情境 nuance、未言明的约束——在形式化过程中可能被丢弃,因为它们无法被结构语法捕捉。

**P3 Latent-Space Transformation** 执行连续压缩:离散 token 序列 → 连续向量表示。这类转化的独特之处在于它保留的不是经验的语义内容,而是模型处理经验时的内部计算状态——各层的 hidden representation、attention 对历史的组织、模型"消化"这段经验后的理解。这些状态无法被 token 序列完整还原(否则不需要 latent),是离散表示的有损补充。压缩的产物不具符号可读性,但可以直接参与后续的 attention 计算而无须重新编码。

**P4 Evaluator Internalization** 执行评估能力内化:interaction experience → judgment function。源经验的 action 与 outcome 之间的关联被学习为一个从 $(c,a,o)$ 到评价信号的映射。转化的关键操作是泛化——训练后的 Evaluator 必须对未见过的 trajectory 也能给出准确判断,而非仅记忆训练集中的 $(c,a,o)$ → label 对。这个泛化步骤同时是价值来源(学到训练集中未覆盖的评估模式)和风险来源(泛化错误导致系统性误判)。

**P5 Policy Internalization** 执行决策能力内化:interaction experience → generation function。与 P4 的对称处在于两者都是 Tokenized → Parametric,都依赖 gradient-based training。不对称处在于 P4 学的是"判断",P5 学的是"执行"——前者的输出是评价信号(低维:标量或 preference),后者的输出是 action(高维:token 序列或工具调用)。高维输出的学习天然更困难、需要更多数据、更不稳定。

**P6 Evaluator-Driven Optimization** 执行偏好迁移:Evaluator 的判断能力 → Policy 的生成偏好。这一步转化的核心操作不是学习新能力——Policy 在 P5 阶段已经具备了基础执行能力——而是调整 Policy 在多个可行 action 之间的选择倾向,使其偏向 Evaluator 认为更好的那些。转化的关键是信号效率:Evaluator 对一条 trajectory 的标量判断需要能被分解为对 trajectory 中每个决策步骤的信用分配(credit assignment)。这一步的困难——也是 RLHF 与 DPO 等方法论之争的实质——在于如何从 trajectory-level 的评价信号中还原出 step-level 的学习信号。

**P7 Parametric Externalization** 执行知识外化:隐式的权重知识 → 显式的 token 序列。这是七条路径中唯一将存在层次从内部移向外部的转化,方向与 P3/P4/P5 相反。转化的核心机制是采样——从 Policy 或 Evaluator 的权重中通过 generation 抽取具体的行为实例(trajectory、demonstration、critique)。采样的根本局限在于:能从权重中提取的只是权重所编码知识的一个样本,不是知识的全部。不同的采样策略(温度、prompt、任务分布)产生不同的外化结果,不存在"完备外化"。

#### Production Mechanism

转化靠什么计算基础设施来执行?这一维度的分析价值在于直接决定工程可行性——你能否负担这条 pathway 不取决于它"好不好",而取决于你是否有对应的计算资源。

**LLM inference(prompting)**是 P1 和 P2 的主流生产机制。成本模型是按 token 计费的 API call:单次转化的资源需求极低(一条 trajectory → 一段 reflection,通常几千 token 的输入 + 几百 token 的输出)。不需要 GPU 集群,不需要训练数据管理。局限性在于转化质量受限于 prompt 设计与模型的 instruction-following 能力——你无法像训练那样系统性优化转化行为。

**Gradient-based training**是 P3(Prompt/Module-Based)、P4、P5、P6 的生产机制。成本模型跨数量级变化:SFT 若干 GPU-hour;RLHF 完整管线(含 RM training + PPO/DPO)几十到几百 GPU-hour;大规模 reasoning model 的训练可达数千 GPU-hour。除直接算力外,还涉及训练数据管理、checkpoint 选择、超参搜索等基础设施开销。

**Gradient-free persistence**是 P3(Cache-Based)的特殊机制:不需要训练,直接保存前向传播产生的 KV cache 或 hidden state。成本极低——本质上是存储成本 + 一次前向传播的计算。但代价是不跨 session、不泛化、随存储量增长检索效率下降。

**Execution + verification loop**是 P2(Programmatic Skill)的附加机制。LLM 生成的 code skill 在入库前需在环境中实际执行并验证——通过则入库,失败则丢弃或修正后重试。执行验证的成本取决于环境:web agent 的 browser automation 验证秒级,Minecraft 的 skill 验证可能分钟级,embodied 的真实环境验证更慢。这一环是 P2 相比 P1 特有的生产开销——P1 不需要产物验证(因为验证是主观的"读"),P2 通过客观执行信号过滤了不合格产物。

#### Information Dynamics

这是 pathway comparison 中最核心也最易被忽略的维度。转化操作同时做三件事——保留信息、丢失信息、生成新信息——三条线在每条路径上的权重与性质截然不同。

**Information Preservation**。转化保留了源经验的什么?

P1 保留的是源 trajectory 中反复出现的模式、因果关联、成功/失败条件。单条 trajectory 的偶然细节(某次工具调用的具体参数值、某段推理的确切措辞)被过滤。保留的是可跨任务迁移的语义内容。

P2 保留的是源 trajectory 中的过程结构与动作序列。Voyager 的 JS program 保留了 crafting 的标准操作流程,AWM [Wan24] 的 workflow trajectory 保留了任务执行的阶段划分与步骤顺序。被保留的是"怎么做"的程序知识,而非"为什么这么做"的语义解释。

P3 保留的是模型处理源经验时的内部计算状态——各层的 hidden activation、attention 的 key-value 对。这些状态包含 token 序列无法完整编码的信息:模型对长程依赖的隐式追踪、对歧义的消解、对上下文的动态加权。它们是"模型如何理解这段经验"的计算痕迹。

P4 和 P5 保留的是训练数据中的统计规律——判断规律(Evaluator)或决策规律(Policy)。单条经验的贡献被 batch 梯度累积所稀释,不可区分解构。保留的是总体分布,不是个体经验。

P6 保留的是 Evaluator 的判断偏好——什么行为是好的、什么是不好的。但这个保留经过两重有损压缩:第一重是 P4 阶段从 trajectory 到 Evaluator 的压缩,第二重是 P6 阶段从 Evaluator 信号到 Policy 权重的压缩。双重重压缩后,原始 trajectory 中的经验语义已不可辨识。

P7 保留的是权重中编码的行为能力——它能做什么。但保留下来的只是这个能力的一次采样,不是能力的完整描述。

**Information Loss**。关键区分是 lossy-by-design 与 lossy-by-limitation。

Lossy-by-design 是转化语义的内在要求——损失是故意的,损失的类别是可控的。P1 的抽象必然丢弃细节:P1 从十条同一任务的失败 trajectory 中提炼出一条规则"在执行 A 之前必须先检查 B",十条 trajectory 各自失败的特定上下文被丢弃了,但保留了跨实例的共性模式。P2 的形式化必然丢弃自然语言的软信息:workflow 中的 step "navigate to login page" 不编码 login page 在不同网站上的视觉差异,这些 nuance 在形式化中被牺牲。

Lossy-by-limitation 是转化机制的工程局限——损失不是故意的,损失的类别不可控。P5 SFT 的欠拟合可能导致某些行为模式完全未被学习;RL reward hacking 可能导致 policy 学会了最大化 reward signal 的捷径而非真正提升任务性能。P3 的 KV 保存受限于存储容量——长程 trajectory 的 KV 必须经过 eviction 或 compression,哪些信息被丢弃由 eviction policy 决定,而非由经验的重要性决定。

Lossy-by-design 和 lossy-by-limitation 在生产侧的恢复路径截然不同。前者的恢复不改变转化方法本身——你可以保留原始 trajectory 作为 footnote(如 reflection 附带源 trajectory 的引用),但抽象和形式化本身的设计不变。后者的恢复需要改进转化方法——更好的 SFT 数据筛选、reward shaping、更优的 KV eviction 策略——这是工程改进,不是框架层面的设计取舍。

**Information Gain**。转化是否产生了源经验中不显式存在的新信息?

P1 的多轨迹归纳是信息增益最明确的 case:对十条 trajectory 的比较可以产生"这类失败在 X 条件下有 80% 的发生率"这类统计性知识——它不来自任何单条 trajectory,而出自跨 trajectory 的比较操作本身。这是真正的信息增益,不隐含在任何源轨迹中。

P2 的 formalism 也可以产生增益:原始 trajectory 中步骤之间的依赖关系是隐式的(agent 每次都先做 B 再做 C,但从未被显式标注为依赖),形式化为 workflow DAG 时这个依赖被显式编码。增益不是新事实,而是现有事实的显式化——信息的组织方式变了,使下游可以机制性地而非语义性地使用这个依赖。

P3 的 latent 可以捕获离散 token 未显式编码的统计规律——例如模型在处理某段 trajectory 时某个 attention head 持续关注某个 token 位置,这个 pattern 不来自 trajectory 的显式内容,而是来自模型对它的处理方式。

P6 可能出现一种特殊的信息增益:Evaluator 的信号可能引导 Policy 发现单靠 trajectory 演示无法学到的行为模式——例如 Evaluator 偏好"简洁且准确的回答",Policy 可能在 RL 过程中自发探索到了 trajectory demonstration 中从未出现的简洁表达方式。这种增益是 search + reward 的威力,但同时也是风险——探索到的"新行为"可能是 reward hacking 的产物。

P7 的信息增益可能为负。Policy 外化产生的 trajectory 可能包含 Policy 的 hallucination——权重的采样噪声被当作知识外化。这些 hallucination 在源 Policy 权重中不构成"知识",但外化后表现得像是经验。

**Traceability**。转化产物的哪些部分能对应回源经验的哪些片段?

这个维度的分析价值不在于可解释性本身(那是 §2.3 的 carrier 属性),而在于它决定了**经验被外部 audit 或纠错时,问题是出在源经验上还是出在转化操作上**。

P1 的可追溯性最高。Reflection "在执行 A 之前必须先检查 B"可以附带引用——"见 episode #42 step 7 和 episode #58 step 4"——这是在 tokenized 同层内转化的结构性便利。P2 的可追溯性居中:workflow 的每个阶段可以对应到源 trajectory 的时间段,但对应关系经过泛化(源 trajectory 中该阶段可能跨 3 到 7 步,workflow 中标准化为 5 步)。

P3 的可追溯性断崖式下降。连续向量中的每个维度都不对应任何 token——你可以通过 probing 找到某些维度对某些语义属性的敏感度,但无法追问"这条 KV 来自哪条 trajectory 的哪个 token position"。

P4 和 P5 的可追溯性近乎零。一次权重更新是 batch 中所有样本的梯度累积——你可以计算出单条样本对某次更新的贡献幅度(通过梯度范数),但无法在最终权重中定位"这条经验对应的权重模式"。这不是工程精度问题——是 batch training 的结构性限制。

P6 的可追溯性比 P5 更差:经过 Evaluator → Policy 的转化,信号的源头(原始 trajectory)已不可追溯,只能追溯到"这个 Evaluator 在这次 rollout 中给了这个分数",而 Evaluator 为什么给这个分数——又回到了 P4 的不可追溯。

P7 的可追溯性特殊:产物(tokenized trajectory)本身是可读、可追溯的——你可以逐句检查。但它无法追溯回产生它的权重中的具体成分——你看到的是 Policy 的"行为",不是 Policy 的"知识结构"。溯源链在 P7 的采样步骤断裂。

#### Incrementality

新经验持续到来时,转化操作能否增量执行?这一维度的分析价值在于它决定经验管理系统的**可持续性**——如果每次新增经验都需要从头重做转化,系统的寿命被转化成本硬性限制。

P1(Static Store)的增量性最强:新 trajectory → LLM inference 生成新 reflection → 追加写入 store。已有条目不受影响。开销与新增经验量成线性,不随已有经验总量增长。

P1(Dynamic Store)的增量性带级联:新条目可能触发对旧条目的 merge(合并语义相近者)、prune(淘汰低效用者)或 edit(修正冲突)。级联范围受限于与新条目相关的局部条目,通常不触发全库重构。开销仍是 sub-linear(级联范围不随总条目数线性增长)。

P2(Programmatic Skill)的增量性类似 P1 Static:新 skill 独立生成、独立测试、独立入库。已有 skill 不受影响。但 P2(Procedural Workflow)的增量更新可能触发 workflow 版本管理问题——如果新经验揭露了旧 workflow 中的错误步骤,需要决定是修正旧版本还是创建新版本。

P3(Cache-Based)天然增量:新 session 产生新 KV cache,旧 session 的 KV 保持不变。跨 session 的增量性体现在 memory store 的 append 而非 update。P3(Prompt/Module-Based)需要 batch retrain:新增经验后需要重新训练 soft prompt 或 memory module。可热启动(从旧 checkpoint 继续训练),但新数据会改变所有已学得的 latent 表示——不可做单条经验的增量更新。

P4 和 P5 的增量性最弱:标准的 preference model training 和 SFT/RL 需要 batch retrain。新增训练数据意味着要么重新训练(算力开销与数据量成线性以上),要么 fine-tune(新数据会覆盖旧数据中的模式,catastrophic forgetting 风险)。Online RL(P5 和 P6)可以逐 batch 增量更新,但每步更新只使用当前 batch 的信息,旧 batch 的经验效果随时间衰减——这不是真正的"增量",而是"遗忘旧经验,仅依赖近端经验"。

P7 的增量性依赖源(Policy 或 Evaluator)的增量性。如果 Policy 本身是通过 online RL 持续更新的,那么 P7 的每次外化反映的是当前最新的 Policy 状态。如果 Policy 是 batch retrain 的,那么 P7 也以 batch 方式运行。

Incrementality 的维度与 §8.4 的时序演化分析直接对接。如果系统预期长期运行且经验持续增长,选择不可增量的 pathway(P4/P5)意味着要么接受定期重训练的算力开销,要么接受经验利用率的随时间衰减。这是场景推荐的一个硬约束。

#### Output Verifiability

转化完成后,能否独立验证转化操作本身是否成功?注意这不是目标载体的可解释性(那是消费侧的问题,在 §8.3 分析),而是**产物的质量能否在不依赖下游任务表现的情况下被判定**。

P1 的 Output Verifiability 是直接但主观的:生成的 reflection 可以被人类或强 LLM 阅读,判断内容是否合理、是否与源 trajectory 一致、是否包含明显错误。这是一个 qualitative check,不是 quantitative test——两个审阅者可能判断不同。P1 没有失败的客观判据——一段 reflection 可以"大致正确但有误导性"而仍被判定为可用。

P2(Programmatic Skill)的 Output Verifiability 是客观且自动化的:生成的 code skill 在环境中执行,通过/失败是二值信号。这是一个 quantitative test——你可以统计 skill 的 test pass rate。但测试的完备性无法保证:一个通过所有现有测试的 skill 可能在未覆盖的 corner case 中失败。这是一个 coverage 问题,不是 objectivity 问题。

P2(Workflow/Graph)的 Output Verifiability 居中:workflow 的结构正确性可以通过静态分析检查(所有步骤的依赖被满足、无死循环、输入输出类型匹配),但 workflow 的任务完备性(是否覆盖了所有必要的处理分支)无法自动验证——需要人类判断或端到端测试。

P3 的 Output Verifiability 最弱。Latent 表示的质量没有独立的评估标准——你只能通过 ablation(去掉这个 latent bank 后 agent 的性能变化)间接推断,而这种推断混淆了 latent 表示的质量与 latent 表示的使用方式。同一组高质量的 KV cache 如果被不当的检索策略选错,其在 ablation 中的表现也会差。

P4 的 Output Verifiability 弱且间接。Evaluator 的质量通常通过两个层级的 proxy 评估:(i) 与 human label 的一致性(但 human label 本身有噪声,且分布可能不同于 Evaluator 的训练分布);(ii) 在下游 P6 中的效用(但 Policy 训练受多个因素影响,Evaluator 质量的贡献无法被单独分离)。

P5 的 Output Verifiability 只能通过 rollout 间接评估:新 policy 在 hold-out task 上的表现是否优于旧 policy。但这个比较混淆了多个因素——新 trajectory 的质量、训练的超参、旧 policy 本身的表现天花板。一个"没有退化的"policy 可能是在训练中被 noise 主导更新,而非经验的有效固化。

P6 面临循环验证风险:用 Evaluator 评分来训练 Policy,再用 Policy 的表现来验证 Evaluator 的质量——两个评估互相参照,没有独立的外部 ground truth。这在 P4 和 P5 各自的验证已经较弱的基础上,进一步增加了验证的不确定性。

这一维度直接连接 verifiability → correctability → maintainability 的结构规律。如果你无法独立验证一次转化是否成功,你就无法判断什么时候需要纠正,也就无法在长期运行中维护经验质量。§8.4 的选择逻辑中,Output Verifiability 低的 path 在需要长期维护的场景中处于系统性劣势。

---

### 8.2.3 Output-Side Dimension: Composability

Pathway 的产物能否直接作为另一个 pathway 的输入?这个维度刻画了 pathway 在七条路径构成的有向图中的出度——它决定了经验在载体系统中的"流动性"。

Composability 的差异不是经验性的而是结构性的——它由功能角色原则(§8.1.3)所蕴含。Policy 产生 action,action 产生 trajectory,trajectory 可被任何以 Tokenized 为源的路径消费——Policy 的 Composability 来自它的功能定义,不是社区探索的偶然结果。Evaluator 产生评估信号,评估信号的语义就是"对行为的判断",它的唯一消费方是行为的生产者——Evaluator 的 Composability 为 1(仅 P6)同样是功能定义的结构推论。

P1(Narrative)是出度最高的节点。Narrative artifact(reflection, rule, insight)可以:
- 作为 P2 的输入(从 reflection 中抽取可形式的操作流程)
- 作为 P3 的输入(将 reflection 压缩为 latent 用于快速上下文注入)
- 作为 P4 的输入(从 reflection 与被其修正的 trajectory 对的比较中训练 Evaluator)
- 作为 P5 的输入(reflection 作为 trajectory 的补充或替代监督信号)
- 被直接消费(作为 retrieval 结果注入 context)

P2(Schematic)的出度中等。Schematic artifact 的主要下游是:
- P5 的输入(skill 作为 action space 的扩展,或 skill execution trace 作为训练数据)
- 被直接执行消费

P3(Latent)目前几乎没有作为新 pathway 源端的文献。这反映了一个深层不对称:Tokenized → Latent 有清晰的动机(保留计算状态、降低 context 开销),但 Latent → Tokenized 或 Latent → Parametric 缺乏对称的动机——如果你要把 latent 再转化为 tokenized,不如直接保留原始 tokenized 经验;如果你要把 latent 固化进权重,那就是 P5 的一种变体而非独立的新路径。Latent 在 pathway 图中的角色是"中间站"——经验进入后通常停在 latent 形态供消费,而非以此为起点继续转化。

P4(Evaluator)的出度为 1:只能进 P6。这在功能角色原则中已论证。

P5(Policy)的出度为 2:可以进 P7(显式外化),也可以通过 rollout 隐式地进任何以 Tokenized 为源的路径。Policy 的 Composability 使它在复合路径中充当枢纽——自生成环(Policy → rollout → Tokenized → P5)、Evaluator–Policy Co-Evolution(Policy → rollout → P4 → P6 → Policy)都依赖 Policy 的这一个结构特性。

P6(Evaluator-Driven Optimization)的产物是 Policy,因此出度同 P5。

P7(Parametric Externalization)的产物是 Tokenized trajectory,Demonstration,因此出度同 P1——理论上可以进入任何以 Tokenized 为源的 pathway。P7 是 pathway 图的闭环节点:**Policy → P7 → Tokenized → P5 → Policy 构成自生成环**,这是 §7.3 Generative Experience Curation 的结构基础。

表 8.1 汇总了七条路径在七个维度上的对比。

| Pathway | Source | Data Prerequisite | Production Mechanism | Info Loss Type | Traceability | Incrementality | Output Verifiability |
|---------|--------|-------------------|---------------------|----------------|-------------|----------------|---------------------|
| P1 Narrative Abstraction | $\mathcal{C}^T_N$ | Low volume; no labels needed; self-gen or human | LLM inference | Lossy-by-design (abstraction) | High (artifact → source episode) | Incremental (append) / Incremental with merge (dynamic) | Direct but subjective (reading) |
| P2 Schematic Formalization | $\mathcal{C}^T_N$ | Low–medium volume; no labels needed; self-gen or human | LLM inference + execution verification | Lossy-by-design (formalization) | Medium (structure → trajectory segment) | Incremental (append skill) | Objective but coverage-limited (execution test) |
| P3 Latent-Space | $\mathcal{C}^T$ | Session: minimal; Trained: large volume; no labels (Cache-Based) or labels needed (Module-Based) | Forward pass + KV persistence / Gradient-based training | Lossy-by-design (compression) | Low (vector → batch) | Session: per-session incremental; Trained: batch retrain | Weak (ablation only) |
| P4 Evaluator Internalization | $\mathcal{C}^T$ | Large volume; outcome or process labels needed; human or teacher | Gradient-based training | Mix (compression by-design + training loss by-limitation) | Very low (weight update → batch) | Batch retrain / Full retrain | Weak-indirect (proxy via human agreement or P6 utility) |
| P5 Policy Internalization | $\mathcal{C}^T$ | Large volume; labels from outcome-filtered or none (RL); self-gen or human | Gradient-based training | Mix (compression by-design + underfitting/reward hacking by-limitation) | Very low (weight update → batch) | Batch retrain / Online iterative | Behavioral only (rollout comparison) |
| P6 Evaluator-Driven Opt. | $\mathcal{C}^P_\phi$ | Medium–large volume (dependent on Evaluator); Evaluator signals as implicit labels | Gradient-based training (RL / DPO) | Double compression (P4 loss + P6 loss) | Near-zero (two-step removed from source) | Online iterative | Circular risk (Evaluator ⇄ Policy) |
| P7 Parametric Externalization | $\mathcal{C}^P$ | No training; sampling quality depends on prompt design | Sampling from trained model | Lossy-by-design (sampling) + hallucination risk | Medium (artifact readable, but cannot trace back to weight components) | Follows source model update | Artifact is readable, but completeness unverifiable |

这张表不是 §3–§6 的摘要——它的行是 pathway,不是 method。单元格填写的是 structural constraint,不是 literature count。以 P1 的 Incrementality 为例,表里写的是"Incremental (append) / Incremental with merge (dynamic)",这两个取值对应 §3.1 中 Static Store 与 Dynamic Store 两类方法的结构性差异,而不是具体工作的名字。读者若需了解哪些工作属于 Static、哪些属于 Dynamic,回查 §3.1 的表格和 prose。

表 8.1 是 §8.2 的产出,也是 §8.4 Phase 5(Production Path Selection)的数据基础。三种截面维度——输入侧、过程侧、输出侧——各有分工:输入侧决定了你能为这条 path 提供什么质量的原料;过程侧决定了你能否负担转化本身的计算和人力开销;输出侧决定了产物在后续经验管理系统中的流动性。

---

*(§8.3 Carrier Utilization Analysis 和 §8.4 Utilization-Driven Pathway Selection 待续。)*
