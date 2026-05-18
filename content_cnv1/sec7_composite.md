# §7 Composite Experience Transformation Pipelines

前文讨论的 7 条路径刻画了经验在单一载体对之间的转化。然而 LLM-based Agent 文献中还存在一类更复杂的方法：它们并不只把经验从一种载体转化为另一种载体，而是将多个 transformation steps 组织成一个链式或闭环式 pipeline——经验在 N-Tok、S-Tok、\(\mathcal{C}^P_\pi\) 与 \(\mathcal{C}^P_\phi\) 等多个载体之间连续流动，且相邻转化步骤之间的衔接机制（integration mechanism）本身构成方法的主要贡献。

Composite pipeline 的判定关键不是"方法是否包含多个操作步骤"，而是这些步骤之间是否存在实质性的衔接机制。例如，一篇论文可能先生成 agent trajectories，再用这些 trajectories 训练 policy；如果中间只是常规数据收集与常规 fine-tuning，则更适合归入单步 P5。若论文的核心贡献在于如何筛选、修复、校准、重标、评估或闭环调度这些中间经验，使其能够被下游 policy 或 evaluator 有效消费，则应归入 Composite。

与单 pathway 相比，Composite 方法通常具有更强的经验利用能力——原始 agent trajectory 中同时包含成功策略、失败动作、局部正确步骤、环境反馈、错误恢复过程和噪声行为，Composite pipeline 试图通过多阶段转化把这些混杂的经验信号组织成更可靠的训练、评估或改进机制。但同时也更容易受到衔接误差、错误反馈累积、分布漂移和闭环坍缩的影响。

本文将 Composite Pipelines 划分为三类：**Evaluator–Policy Co-Evolution**（Evaluator 与 Policy 参数在同一学习闭环中相互校准和共同演化）、**Refinement-Mediated Policy Internalization**（先将原始经验转化为更可学习的 refined artifact，再内化进 Policy 参数）和 **Other Composite Experience Pipelines**（以 experience generation、filtering、verification、simulation、search 或 selection 为核心的异质复合路径）。

## §7.1 Evaluator–Policy Co-Evolution

Evaluator–Policy Co-Evolution 指 Evaluator parameter 与 Policy parameter 围绕 Agent experience 进行相互校准和共同演化的复合路径。其抽象结构可表示为 \(\mathcal{C}^P_\pi \leftrightarrow \mathcal{C}^P_\phi\)：Policy 在环境中 rollout 产生新的行为分布和交互经验，Evaluator 根据这些经验更新或校准自身的评价能力；随后 Evaluator 又通过 reward、critique、preference、verification 或 process feedback 反过来塑造 Policy 更新。

这一类方法的核心在于 Evaluator 不是最终产物，也不是固定的外部 reward model，而是 Policy improvement loop 中的动态参与者——评估能力和决策能力在同一个经验闭环中共同演化。在 open-world agent、GUI agent 或 embodied agent 中，Policy 的行为会随着训练不断变化，旧 Evaluator 很容易变得 stale：它可能无法识别新型失败模式，也可能对新策略产生错误评价。若仍用静态 Evaluator 监督不断变化的 Policy，Policy 可能过拟合 Evaluator 的偏差，甚至通过 reward hacking 获得高分但不真正提升任务能力。

**代表性工作。** UI-Genie [Xia25e] 将 GUI agent 与 reward model 放入多轮 self-improving loop：Agent 的探索轨迹一方面被 reward-guided search 用于筛选高价值行为，另一方面失败轨迹又经 continuation rollout 自动转化为新的 step-level supervision 来刷新 reward model。MagicGUI-RMS [Li26n] 通过 DS-RM 与 GP-RM 的分层评估协作及 feedback reflux 机制，把 Agent 执行中的高质量纠偏动作回流为 policy supervision，同时把评估分歧样本回流为 Evaluator 的再训练数据。ECHO [Li26l] 将 critic staleness 明确视为核心问题：采用由初始轨迹、语言诊断与条件修正组成的 synchronized update loop，使 critic 始终跟随当前 policy 的失败模式演化，并借助 saturation-aware gain shaping 保持对高分段细粒度改进的敏感性。

**边界与扩展案例。** RL Tango [Zha25y] 在 reasoning setting 中交替训练 generator 与 verifier，使 verifier 随 generator 的推理轨迹分布共同更新，并以 process-level feedback 反向塑造 generator。VARP [Sin25b] 在 embodied RL 中通过 agent-regularized preferences 让 reward learning 显式依赖当前 policy rollout，缓解奖励模型与行为分布脱节。RLAnything [Wan26u] 将 evaluator–policy coupling 扩展为"policy–reward–environment"三元闭环——reward model 由 evolving policy 的轨迹持续更新，而其 step-wise feedback 又与 outcome signal 一起反向驱动 policy 优化，同时显式引入 environment adaptation。EVPO [Pan26] 展示了一种较弱耦合形式：critic 虽随 policy 持续训练，但论文关注的重点是依据 explained variance 自适应控制 critic 在不同阶段的可用性，更像 critic utilization 与 policy optimization 的动态协调。Co-Evolution of Policy and Internal Reward for Language Agents [Wan26aj] 将 Evaluator 内生化为 policy 自身生成的 self-guidance，形成"更强 policy 产生更好 guidance，更好 guidance 再改进 policy"的自洽闭环。

Evaluator–Policy Co-Evolution 的 integration mechanism 通常包括 alternating update、feedback reflux、hard negative mining、critic refresh、dual-track optimization、policy-conditioned evaluator training 或 evaluator-guided trajectory selection。这些机制的共同目标是防止 Evaluator 与 Policy 脱节。主要优势在于能将"评估经验"和"决策经验"结合起来——Agent trajectory 既可以训练 Evaluator 判断什么行为是合理的，Evaluator 又可以持续改进 Policy。风险在于如果 Evaluator 的训练数据主要来自当前 Policy，它可能继承 Policy 的探索盲区和行为偏差；Evaluator 和 Policy 可能形成共适应偏差。分析这类方法时需重点关注其是否包含外部验证、hard negatives、evaluator refresh 或 anti-collapse 机制。

## §7.2 Refinement-Mediated Policy Internalization

Refinement-Mediated Policy Internalization 指先将原始 agent experience 转化为更可学习的 refined artifact，再将其内化进 Policy parameter 的复合路径。典型结构是 N-Tok → N-Tok/S-Tok → \(\mathcal{C}^P_\pi\)。源经验通常是 Agent 在交互过程中产生的 raw trajectory、failure episode、reasoning trace、tool-use log、GUI interaction trace 或 embodied execution record。

这类方法的核心不是直接把 raw trajectory 训练进 policy，而是先对原始经验进行反思、修复、校准、净化、压缩或形式化，使其变成更适合 policy learning 的中间 artifact。关键假设是：Agent 的历史经验并不天然等价于可学习监督——失败轨迹中可能包含正确的前缀和局部有效动作，成功轨迹中也可能包含冗余动作或不可迁移的 shortcut。Refinement step 的目标是将这些混杂的经验信号重新解释为更稳定、更具因果指向性的 training signal。

与单步 P1 不同：单步 Narrative refinement 通常将 reflection、summary 或 memory 作为 inference-time context 使用，而 Refinement-Mediated Policy Internalization 中 refined artifact 会进一步进入训练过程。与直接 P5 不同：直接训练 raw trajectories 往往假设轨迹本身就是可靠监督信号，而这类方法的核心假设是经验在写入参数之前需要被重新解释。

现有代表性工作大致沿三条机制展开：

**失败经验的反思、修复与重写。** [Ge26] 将失败 rollout 提炼为 rollback target 与 reflective summary，再据此生成修正分支，通过 counterfactual distillation 使模型在不显式依赖反思文本的条件下复现修正决策，从而把外显的 reflective agency 内化为参数能力。[Yua25c] 从 good 与 bad trajectories 中构造带有 reflection signal 的 revision trajectory，使模型学习在识别到首个关键错误后尽早切换到修正路径。[Wan25x] 进一步将修复粒度细化到步骤层面：通过定位第一个偏离 expert path 的动作，生成包含 reflective thought 与 corrected action 的 calibrated trajectory，再据此训练 policy。[Xu26j] 关注工具调用与代码执行中的噪声污染，利用 similarity-aware rollback 将含错误上下文的轨迹纯化为 self-purified trajectories。[Din26] 根据失败轨迹实际达成的 outcome 逆向生成 hindsight goal，把失败运行重写为新的成功 demonstration，再将这些 relabeled samples 用于 SFT 或 DPO。

**长程交互中的过程监督构造。** [Xio24] 利用 Monte Carlo rollout 将稀疏的 outcome reward 下放到具体步骤，构造 step-level contrastive pairs 与 trajectory-level preference pairs，通过 step-DPO、outcome-DPO 与 SFT 的联合优化将过程层面的 refined signal 写入 policy。[Son24] 将失败轨迹与成功轨迹组织为 preference pairs，通过 DPO 让模型学习"成功优于失败"的结构化偏好。[Yan24m] 用 ActRe 为探索得到的动作序列反向补写 posterior reasoning，将原本缺乏解释的 action traces 重构为可训练的 ReAct-style trajectories，再通过 contrastive self-training 实现经验内化。[Wu25b] 面向 GUI agent，通过离线伪造错误与在线挖掘失败轨迹构造 reflection thought、rollback 与 correction 数据。

**Skill/Hint 抽象后蒸馏。** [Wan26al] 先把多轮 agent trajectories 总结为结构化 natural-language skills（success analysis、mistake analysis、golden workflow），再把这些 skills 仅作为训练期 teacher 的特权信息，通过 self-distillation 将其吸收到 student policy。[Ye26f] 将在线交互轨迹递增式提炼为 experiential knowledge，通过 on-policy context distillation 将"带知识的 teacher"压缩为"无知识的 student"。[Ala25] 以 corrective hints 为中介：reviewer 先从轨迹中识别错误模式并生成针对性提示，teacher 在 hints 引导下产生更优行为分布，student 再通过 context distillation 学会在不显式接收 hints 的情况下复现这些行为。

Refinement-Mediated Policy Internalization 的优势在于能够更充分地利用失败经验和过程经验——传统 imitation learning 更依赖成功 demonstrations，而这类方法可以从失败轨迹中提取错误模式、反事实修正和改进行为。局限在于 refinement 本身可能出错（错误定位失败原因或将偶然因素解释为通用规律），可能过度依赖强 teacher model，且 refined artifacts 的抽象程度需要精细控制。

## §7.3 Other Composite Experience Pipelines

Other Composite Experience Pipelines 收纳那些确实满足 Composite 条件，但不以 evaluator–policy co-evolution 或 refinement-mediated policy internalization 为核心的异质复合路径。这类方法中最常见的结构是 \(\mathcal{C}^P_\pi \rightarrow \mathcal{C}^T \rightarrow \mathcal{C}^P_\pi\)：Policy 或 teacher model 首先外化出 trajectories、demonstrations、interaction traces 或 synthetic tasks；随后这些 Tokenized experience 被筛选、验证、选择、重标或组织成训练数据；最后被用于改进 Policy parameter。其核心贡献往往不在于某一次单独的生成或训练，而在于"如何产生足够可靠、足够多样、足够贴近目标分布的 experience，并将其转化为有效 policy update"。

**Exploration 或 Task Synthesis 驱动的数据构造链。** OS-Genesis [Sun24b] 先在环境中进行 interaction-driven traversal，收集 action-centered traces，再反向合成 high-level tasks，借助 trajectory reward model 对生成出的完整轨迹做分级采样。AgentTrek [Xu24] 将 web tutorial 转写为结构化 task specification，在真实环境中执行 guided replay 生成 multimodal trajectories，经由 VLM evaluator 验证。AutoSurfer [Fai26] 以 breadth-first 方式探索网站，基于探索路径合成 grounded tasks，再利用同一批 exploration trajectories 作为 hints 引导 trajectory refinement。OpenWebVoyager [He24e] 先通过 imitation learning 获得初始 web policy，再在真实网页中持续 self-exploration，由外部 judge 对 rollout 结果做 trajectory-level rejection sampling，只把 judged-good trajectories 回灌到后续训练。

**Synthetic/Self-generated Experience 验证与筛选。** Bootstrapping Language-Guided Navigation [Wan24ad] 构造 generator–navigator self-refining flywheel：instruction generator 从无标注轨迹生成指令，navigator 依据执行一致性指标筛选高保真样本，这些样本反过来提升 generator。BLAZER [Das25] 在 simulator 中零样本生成 manipulation demonstrations，环境执行验证成功与否，只有 automatically verified demonstrations 被保留用于微调。Scalable Data Synthesis with Step-Level Filtering [He25g] 指出即便整体成功的 CUA trajectories 也包含大量局部错误或次优动作，因此对每一步执行 step-level grading，只让高质量 steps 贡献监督损失。

**Search 或 Contrastive Restructuring 对经验的再组织。** MCTS-EP [Xu25q] 使用 MCTS 在 embodied environment 中扩展 trajectory space，在分支节点上根据搜索得到的 long-horizon value 构造 preference pairs，分别用于 SFT 与 DPO 更新 policy——search 不只是求解器，而是将原始交互经验重组为 success trajectories 与 structured preferences 两种训练载体的关键中介。Trial and Error [Son24] 让 Agent 主动探索并显式收集 failure trajectories，再把 failure–success pairs 转换为 DPO 所需的 contrastive training data。Agent Q [Put24] 通过 MCTS 生成搜索树和多分支轨迹，结合 critic ranking 与 outcome reward 形成 node-level preference signal，再编译成 DPO 训练数据。

**RL 系统中的 Composite 倾向。** WebRL [Qi24] 通过 failure-driven curriculum generation、task filtering、ORM-based trajectory judging 与 replay selection，把 self-evolving task construction 与 off-policy RL 串成一条数据管线。DigiRL [Bai24] 在真实 device environment 中结合 VLM-based AutoEval、instruction-level curriculum selection 与 step-level filtering，再以 advantage-weighted regression 更新 policy。这些工作共享"先生成或收集经验，再经中间机制重构监督，再做 policy update"的总体框架，但叙述重心更偏向 RL training system。

Overall，Other Composite Pipelines 的共同趋势在于：经验不再被视为可直接回放的原始轨迹，而被当作需要经过二次组织、验证和编译的中间材料。无论是由 exploration 派生 task 再派生 trajectory，还是由 simulator 或自生成 rollout 派生经过筛选的 training data，抑或是由 search tree 和 failure branch 派生 preference-style supervision——真正决定方法效果的，都是这些中间 transformation steps 如何把原始 agent experience 变成更可靠、更高价值、也更可被 Policy 内化的学习信号。

## §7.4 本章小结

Composite Experience Transformation Pipelines 将 Agent experience 的复用从单一载体转化扩展为跨载体、跨模块、跨阶段的链式或闭环过程。三类复合路径揭示了三类不同的 integration logic：Evaluator–Policy Co-Evolution 的核心是评估与决策能力的动态匹配——如何在避免共适应偏差的前提下，让 Evaluator 随 Policy 共同演化；Refinement-Mediated Policy Internalization 的核心是经验可学习性的提升——如何通过反思、修复、校准、净化或抽象，把混杂的 raw experience 转化为更稳定的 training signal；Other Composite Pipelines 的核心是经验空间的主动扩展与组织——如何通过生成、探索、搜索和筛选，把有限的交互经验扩展为规模更大、质量更高、分布更合理的 training data。

Composite 方法的潜在收益在于能够更充分地利用失败经验、过程反馈、synthetic experience、search results 和 evaluator signals——这些都是单 pathway 方法难以独立覆盖的经验来源。但风险也更高：每一个中间步骤都可能引入新的噪声、偏差或错误归因，且错误可能在复合链中累积和放大。因此，在评价 Composite pipeline 时，应重点考察其 integration mechanism 是否必要、是否经过消融验证、是否能防止错误经验累积，以及是否真正提升了 Agent 在新任务和新环境中的泛化能力。
