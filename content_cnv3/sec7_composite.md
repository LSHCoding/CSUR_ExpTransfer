# 7. Composite Transformations

§3–§6 讨论的 7 条单路径刻画了经验在单一载体对之间的一次转化。LLM-based Agent 文献中还存在一类更复杂的方法：它们把多个 transformation steps 组织成链式或闭环式 pipeline，经验在 Narrative Tokenized、Schematic Tokenized、Policy 参数与 Evaluator 参数之间连续流动，而相邻步骤之间的衔接机制（integration mechanism）本身构成方法的主要贡献。

判定一项工作是否属于 Composite，关键不在于它是否包含多个操作步骤，而在于这些步骤之间是否存在实质性的衔接机制。一篇论文若先生成 agent trajectories、再用它们训练 policy，中间只是常规数据收集与常规 fine-tuning，更适合归入单步 P5；只有当论文的核心贡献落在如何筛选、修复、校准、重标、验证或闭环调度这些中间经验、使其能被下游 policy 或 evaluator 有效消费时，才归入 Composite。

本章将 Composite Pipelines 划分为三类，分界依据一条统一的判据轴——衔接机制作用在哪个载体结点上：

- **§7.1 Evaluator–Policy Co-Evolution**：衔接机制是一个 learned evaluator 与 policy 的相互校准。Evaluator 参数被刻意设计为随 evolving policy 持续刷新或重训，二者在同一闭环中互相塑造。标准 actor–critic 中 critic 的常规联合更新不构成此类衔接——只有当"评估器与策略的协同演化"本身是被贡献的设计要素时才纳入。
- **§7.2 Refinement-Mediated Policy Internalization**：衔接机制作用于单条经验的内容。对个别 trajectory 做反思、修复、校准、净化、补写或抽象，改变其作为监督信号的内容，再将 refined artifact 内化进 Policy 参数。
- **§7.3 Generative Experience Curation**：衔接机制作用于经验集合的生成与分布。通过探索、合成或搜索产生原本不存在的经验，并通过验证、筛选、选择构造其分布，再将经过筛炼的 experience set 用于 Policy 更新。

§7.2 与 §7.3 的一句话分界：§7.2 改写经验的内容，§7.3 构造经验的集合。一项工作若同时含两种操作，按其 headline 贡献归位。

与判据轴正交的是 composition topology：链式（chain，经验沿 Narrative → Schematic → Parametric 方向单向流动）与闭环式（loop，下游产物回流上游、迭代多轮）。拓扑不作为分类主轴，而作为每条 pattern 的属性描述——§7.1 几乎全为闭环，§7.2 几乎全为链式，§7.3 二者兼有。

<!-- 两点 scope 边界：其一，本章所有 composite 的中间与终端载体都落在 Tokenized 与 Parametric 上——以 Latent 为中间或终端载体的 composite pipeline 在文献中未找到典型代表，这既可能是真实空白，也可能反映该方向尚未成熟。其二，本章绝大多数工作以 Policy 参数内化为终点，以"更优的 Tokenized artifact 而不做参数更新"为终端的 composite 仅在边界案例中部分出现。 -->

与单路径相比，Composite 方法通常具有更强的经验利用能力——原始 agent trajectory 中混杂着成功策略、失败动作、局部正确步骤、环境反馈、错误恢复与噪声行为，Composite pipeline 通过多阶段转化把这些信号组织成更可靠的训练、评估或改进机制。代价是更容易受到衔接误差、错误反馈累积、分布漂移与闭环坍缩的影响。

## 7.1 Evaluator–Policy Co-Evolution

Evaluator–Policy Co-Evolution 指 Evaluator 参数与 Policy 参数围绕 Agent experience 相互校准、共同演化的复合路径。其抽象结构可写为经 Tokenized 中介的闭环：Policy 在环境中 rollout 产生新的行为分布与交互经验（Tokenized），这些经验被用于更新或校准 Evaluator 的评价能力；Evaluator 再通过 reward、critique、preference、verification 或 process feedback 反向塑造 Policy 更新。Policy 与 Evaluator 之间并非直接的参数到参数转化——经验先以 trajectory 形式外化为 Tokenized 载体，再分别驱动两端的参数更新，闭环的真实结构带有一个 Tokenized waypoint。

判据落在"evaluator–policy 的协同演化是否是被贡献的衔接机制"上。在 open-world、GUI 与 embodied 场景中，Policy 的行为随训练不断漂移，静态 Evaluator 很容易 stale：它可能识别不出新型失败模式，也可能对新策略产生错误评价；若仍用旧 Evaluator 监督新 Policy，Policy 可能过拟合 Evaluator 的偏差，甚至通过 reward hacking 获得高分而不真正提升能力。本节纳入的工作都把这一问题作为命名的设计目标，并给出了让 Evaluator 跟随 Policy 演化的具体机制。

**核心组——双向刷新的评估器闭环。** UI-Genie [Xia25e] 把 GUI agent 与 reward model 放进多轮 self-improving loop：agent 的探索轨迹一方面被 reward-guided beam search 用于筛选高价值行为，另一方面失败轨迹经 continuation rollout 自动转化为新的 step-level supervision 来刷新 reward model。MagicGUI-RMS [Li26n] 构建 DS-RM 与 GP-RM 的分层评估系统，并以 automated feedback reflux 把策略与评估器放进同一闭环——GP-RM 认可的高质量动作回流为 agent supervision，DS-RM 与 GP-RM 的分歧样本回流为 evaluator 增量训练数据。ECHO [Li26l] 直接把 critic staleness 列为 open-world agent learning 的核心障碍：policy 生成 on-policy trajectory，critic 给出多视角自然语言诊断，policy 据此做 conditional refinement，两者在"初始轨迹—诊断—修正轨迹"上做 dual-track GRPO 更新，并以 saturation-aware gain shaping 维持 critic 对高分区间细微改进的敏感性。

**reasoning 与 embodied 场景的扩展。** RL Tango [Zha25y] 在推理设定中交替训练 generator 与 verifier，使 verifier 在 generator 当前推理轨迹分布上持续更新——verifier 只接收 outcome-level correctness reward，却学习产出 step-level verification feedback 来塑造 generator，而 generator 的新轨迹又不断暴露新的验证难点。RLAnything [Wan26u]<!-- TODO: describe 判为跨类(§7.1+§7.3),因其 failure-driven task synthesis 作用于经验集合分布 --> 把 evaluator–policy 耦合扩展为"policy–reward–environment"三元闭环：reward model 由 evolving policy 的轨迹持续更新，其 step-wise feedback 与 outcome signal 一起反向驱动 policy，同时引入 theory-motivated environment adaptation 动态调节任务难度。

**弱耦合与极限形态。** VARP [Sin25b]<!-- TODO: pathway 归类存疑,describe 判为 §7.3 而非 §7.1,因其关键机制作用于经验集合的生成与筛炼 --> 在 embodied RL 中通过 agent-regularized preferences 让 reward learning 显式依赖当前 policy 的 rollout 数据，使 reward model 随 policy 能力变化重估偏好边界。其耦合强度弱于核心组——evaluator 不是被专门 refresh 机制重训，而是经正则项与当前行为分布绑定——但评估能力确实随策略演化。Self-Guide [Wan26aj] 让同一个 language agent 每步先生成短 self-guidance，该信号同时作为 inference-time action steering 与 training-time internal reward。evaluator 被内生进 policy 自身，不存在独立的第二个 Parametric 载体，闭环结构退化为单一载体上的 self-rewarding 回路。其 co-evolution 逻辑仍然成立，作为评估器与策略共享参数的极限案例标注。

**Integration mechanism 类型学与失效模式。** 衔接机制包括：alternating update（generator/policy 与 verifier/evaluator 交替优化，如 RL Tango）、feedback reflux（高质量动作回流为 supervision，分歧样本回流为再训练数据，如 MagicGUI-RMS）、continuation rollout/hard negative mining（从失败轨迹挖掘潜在正确步骤刷新评估器，如 UI-Genie）、critic refresh + dual-track optimization（critic 随 policy 同步更新，如 ECHO）、policy-conditioned evaluator training（reward 学习显式依赖当前 rollout 分布，如 VARP/RLAnything）、internalized self-guidance（evaluator 函数由 policy 自身生成，如 Self-Guide）。共同目标是防止 Evaluator 与 Policy 脱节。主要风险是 co-adaptation bias：若 Evaluator 的训练数据主要来自当前 Policy，它会继承 Policy 的探索盲区与行为偏差，二者可能共同收敛到一个对外部任务无效的局部最优。评价时应重点考察闭环中是否引入外部验证、hard negatives、独立 evaluator refresh 或显式 anti-collapse 机制。

## 7.2 Refinement-Mediated Policy Internalization

Refinement-Mediated Policy Internalization 指先把原始 agent experience 转化为更可学习的 refined artifact、再将其内化进 Policy 参数的复合路径，典型结构是 Narrative Tokenized → Narrative/Schematic Tokenized → Policy 参数。源经验通常是 raw trajectory、failure episode、reasoning trace、tool-use log、GUI interaction trace 或 embodied execution record。

判据是衔接机制作用于单条经验的内容——对个别轨迹做反思、修复、校准、净化、补写或抽象，重新解释其作为监督信号的内容。关键假设是 Agent 的历史经验并不天然等价于可学习监督：失败轨迹中可能含有正确前缀与局部有效动作，成功轨迹中也可能含有冗余动作或不可迁移的 shortcut。与单步 P1 的区别在于 refined artifact 会进入训练而非停留在 inference-time context；与直接 P5 的区别在于它否定"raw trajectory 本身即可靠监督"这一假设，要求经验在写入参数之前先被改写。与 §7.3 的分界在于操作对象——本节改写单条经验的内部内容，§7.3 构造经验集合的分布。

**失败经验的反思、修复与重写。** <!-- TODO: 补充方法名缩写 --> [Ge26] 把失败 rollout 提炼为 rollback target 与 reflective summary，据此生成修正分支，通过 counterfactual distillation 使模型在不显式依赖反思文本的条件下复现修正决策，把外显的 reflective agency 内化为参数能力。Agent-R [Yua25c] 从 MCTS 生成的 good 与 bad trajectories 中构造带 reflection signal 的 revision trajectory，使模型学会在识别到首个关键错误后及时切换到修正路径。STeCa [Wan25x] 把修复粒度细化到步骤层面：定位第一个偏离 expert path 的动作，生成含 reflective thought 与 corrected action 的 calibrated trajectory 替换原始偏离片段。CLEANER [Xu26j] 针对工具调用与代码执行中的噪声污染，用 similarity-aware adaptive rollback 把含错误上下文的轨迹纯化为 self-purified trajectories。AgentHER [Din26] 不丢弃失败轨迹，而是从中提取其实际达成的 outcome、逆向生成 hindsight goal，把失败运行重写为与真实效果一致的成功 demonstration。

**过程结构的补写与重构。** Watch Every Step! [Xio24]<!-- TODO: pathway 归类存疑,describe 判为 §7.3 而非 §7.2,因其机制作用于 step-pair 构造与筛选而非改写轨迹内容 --> 用 Monte Carlo rollout 把稀疏 outcome reward 下放到具体步骤，构造 step-level contrastive pairs 与 trajectory-level preference pairs，通过 step-DPO、outcome-DPO 与 SFT 的联合优化把过程层面的局部优劣结构写入 policy。ReAct Meets ActRe [Yan24m] 让 agent 探索得到动作序列后，用 ActRe 为这些动作反向补写 posterior reasoning，把原本缺乏解释的 action traces 重构为可训练的 ReAct-style trajectories，再经 contrastive self-training 内化。GUI-Reflection [Wu25b] 通过离线伪造错误与在线挖掘失败轨迹，自动构造含 reflection thought、rollback 与 correction 的 GUI self-reflection data。

**Skill/Hint 抽象后蒸馏。** Skill-SD [Wan26al] 先把多轮 agent trajectories 总结为结构化 natural-language skills（success analysis、mistake analysis、golden workflow），再把这些 skills 仅作为训练期 teacher 的特权信息，通过 self-distillation 吸收进不显式访问 skills 的 student policy。Online Experiential Learning [Ye26f] 把在线交互轨迹递增式提炼为 experiential knowledge，经 on-policy context distillation 将"带知识的 teacher"压缩为"无知识的 student"，并通过对照实验表明先抽取经验再内化优于直接训练 raw trajectory。Memento No More [Ala25] 以 corrective hints 为中介：reviewer 从轨迹识别错误模式并生成针对性提示，teacher 在 hints 引导下产生更优行为分布，student 经 context distillation 学会在不接收 hints 的条件下复现这些行为。

**Integration mechanism 类型学与失效模式。** 衔接机制包括：first-error localization（定位轨迹中首个关键偏离动作，如 Agent-R/STeCa）、counterfactual branch construction（据失败点生成不含反思文本的修正分支，如 Ge26）、hindsight relabeling（按实际 outcome 逆向重写失败轨迹的目标，如 AgentHER）、similarity-aware purification（剔除错误上下文纯化轨迹，如 CLEANER）、posterior reasoning synthesis（为 action trace 反向补写推理，如 ReAct + ActRe）、step-level process decomposition（把 outcome 信号下放到步骤，如 Watch Every Step!）、skill/hint abstraction + privileged-info distillation（抽象为结构化 skill/hint 后蒸馏，如 Skill-SD）。

这类方法的优势在于能更充分利用失败经验与过程经验——传统 imitation learning 偏重成功 demonstrations，本节方法可从失败轨迹提取错误模式、反事实修正与改进行为。失效模式集中在 refinement 步骤本身的脆弱性：错误定位失败原因、把偶然因素解释为通用规律、过度依赖强 teacher model，以及 refined artifact 抽象程度失控。评价时应检验 refinement 是否经过消融——若移除 refinement 步骤、直接训练 raw trajectory 的对照实验缺失，"经验需被改写"这一核心假设就未被验证。

## 7.3 Generative Experience Curation

Generative Experience Curation 指以经验的生成与分布构造为核心衔接机制的复合路径。典型结构是 Policy/Teacher 参数 → Tokenized → Policy 参数：Policy 或 teacher model 先外化出 trajectories、demonstrations、interaction traces 或 synthetic tasks，这些 Tokenized experience 随后被验证、筛选、选择、搜索或重标，构造成贴近目标分布的训练数据，最后用于改进 Policy 参数。

判据是衔接机制作用于经验集合的生成与分布而非单条经验的内容。本节方法不改写个别轨迹的内部内容，而是决定哪些经验被产生、哪些被保留、整体分布如何构成。其核心假设是有限的交互经验不足以支撑可靠的 policy learning——经验需要被主动扩展（探索、合成、搜索）并被质量控制（验证、筛选、评分），真正决定方法效果的是这些中间步骤如何把原始 agent experience 变成规模更大、质量更高、分布更合理的学习信号。

**探索与合成驱动的经验生成。** OS-Genesis [Sun24b] 不先给任务再采轨迹，而是先在 GUI 环境做 interaction-driven traversal、收集 action-centered traces，再反向合成 high-level tasks，并用 trajectory reward model 对完整轨迹做分级采样。AgentTrek [Xu24] 把 web tutorials 转写为结构化 task specifications，在真实环境执行 guided replay 生成 multimodal trajectories，经 VLM evaluator 验证 instruction adherence 与 goal completion。AutoSurfer [Fai26] 以 breadth-first 方式系统探索网站、获得覆盖更全面的 action traces，据此合成 grounded tasks，并用同一批探索轨迹作为 hints 引导 trajectory refinement。OpenWebVoyager [He24e] 先经 imitation learning 得到初始 web policy，再让 agent 在真实网页持续 self-exploration，由固定的外部 judge（GPT-4o）对 rollout 做 trajectory-level rejection sampling，只把 judged-good trajectories 回灌后续训练。Bootstrapping Language-Guided Navigation [Wan24ad] 构造 generator–navigator self-refining flywheel：instruction generator 从无标注轨迹生成指令，navigator 依执行一致性指标筛选高保真样本，这些样本反过来提升 generator——这是本节少见的闭环拓扑，但回流的是经验质量而非评估器参数。BLAZER [Das25] 用强 LLM 在 simulator 中零样本生成 manipulation demonstrations，经环境执行验证仅保留成功样本。

**验证与筛选为核心的经验筛炼。** Scalable Data Synthesis with Step-Level Filtering [He25g] 指出即便整体成功的 CUA trajectories 也含大量局部错误或次优动作，因此对每一步做 step-level grading，只让高质量 steps 贡献监督损失、同时保留错误步骤作为上下文。Language Feedback Model [Zho24e] 先从大模型反馈蒸馏出一个 Language Feedback Model，再用它对 rollout 中的局部动作做 desirability 判断、筛出更值得模仿的行为片段，经 imitation learning 吸收。DigiRL [Bai24] 在真实 device environment 做 autonomous rollouts，用固定的 VLM-based AutoEval 提供奖励信号，再做 instruction-level curriculum selection 与 step-level doubly-robust filtering，以 advantage-weighted regression 更新 policy。WebRL [Qi24] 从 failure set 生成新的 curriculum tasks，经 critic-based difficulty filtering 与 feasibility filtering 筛选任务，agent rollout 后再由 outcome reward model 与 actor-confidence replay filtering 选择可用经验。PLD [Xia25h] 先训练 residual actor 去 probe base VLA 的 failure regions，再通过 hybrid rollout 收集既贴近 base-policy deployment distribution、又含 recovery behavior 的成功轨迹，最后蒸馏回 generalist VLA。

**Search 结构化的经验重组。** MCTS-EP [Xu25q] 用 MCTS 在 embodied environment 扩展 trajectory space，不仅提取成功路径，还在分支节点上据搜索得到的 long-horizon value 构造 preference pairs，分别用于 SFT 与 DPO——search 在此把原始交互经验重组为 success trajectories 与 structured preferences 两种可训练载体。Agent Q [Put24] 通过 MCTS 生成搜索树与多分支轨迹，结合 critic ranking 与 outcome reward 形成 node-level preference signal，再编译成 DPO 训练数据。Trial and Error [Son24] 让 agent 主动探索并显式收集失败轨迹，再把 failure–success pairs 转成 DPO 所需的 contrastive training data——它不改写单条轨迹的内容，而是通过配对在集合层面构造对比式监督，故归本节而非 §7.2。

**Integration mechanism 类型学与失效模式。** 衔接机制包括：interaction-driven traversal（无任务先导地探索环境收集 traces）、reverse task synthesis（从 traces 反向合成 high-level tasks）、search-tree expansion → preference compilation（搜索树编译为 node-level preference）、learned/metric-based filtering（用学习评估器或执行指标筛选经验）、step-level grading（子轨迹粒度评分后选择监督 step）、rejection sampling（固定 judge 对 rollout 做轨迹级取舍）、curriculum generation（从失败集生成新任务并按难度过滤）、contrastive pairing（配对成功/失败轨迹构造偏好数据）。

失效模式集中在三处：分布漂移——生成的经验偏离目标部署分布，PLD 对 distribution-aligned data 的强调正是针对此；verifier/filter 不可靠——固定 judge 或 reward model 的偏差会被筛选机制放大、污染整个训练集；exploration coverage 不足与闭环 mode collapse——self-refining flywheel 若缺乏多样性约束会收敛到狭窄的经验子空间。评价时应检验生成—筛选机制是否经过消融、verifier 的可靠性是否被独立验证、synthetic task 与真实任务的语义错配是否被检测。

## 7.4 Discussion

三类复合路径对应三种 integration logic：Evaluator–Policy Co-Evolution 处理评估与决策能力的动态匹配，问题是如何在避免 co-adaptation bias 的前提下让 Evaluator 随 Policy 共同演化；Refinement-Mediated Policy Internalization 处理经验可学习性的提升，问题是如何通过反思、修复、校准、净化或抽象把混杂的 raw experience 改写为更稳定的 training signal；Generative Experience Curation 处理经验空间的主动扩展与组织，问题是如何通过生成、探索、搜索与筛选把有限交互经验构造成分布更合理的训练数据。三类的分界由统一判据轴给出——衔接机制作用于参数载体对（§7.1）、单条经验的内容（§7.2）、还是经验集合的分布（§7.3）。

Composite 方法的潜在收益是能利用失败经验、过程反馈、synthetic experience、search results 与 evaluator signals 这些单路径难以独立覆盖的经验来源。代价是每个中间步骤都可能引入新的噪声、偏差或错误归因，且错误会沿复合链累积放大。评价一条 Composite pipeline 时应考察四点：integration mechanism 是否必要（移除该步骤的对照实验是否存在）、是否经过消融验证、是否具备防止错误经验累积的环节（外部验证、anti-collapse、独立 refresh），以及是否真正提升了 Agent 在新任务与新环境中的泛化能力。

<!-- 本章暴露出文献分布上的两处空白：以 Latent 载体为中间或终端的 composite 几乎不存在——§4 已表明 Tokenized → Latent 的单步转化是成熟方向，二者之间存在尚未被探索的组合空间；以"更优 Tokenized artifact 而不做参数更新"为终端的 composite 同样稀少，这类 memory-terminal 复合路径值得作为独立形态进一步考察。 -->
