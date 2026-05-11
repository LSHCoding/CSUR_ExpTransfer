[Title]: Reflexion: Verbal Reinforcement Learning
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Raw rollouts with task feedback signals
- [Target Experience]: Natural-language critiques 存入 episodic memory buffer（reflection 集合）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 后续 attempt 时 buffer 整体作为 prompt context 拼入，policy 通过 in-context conditioning 复用历史反思以避免重犯错误
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 每次 rollout 结束后，让 LLM 对 task feedback 做 verbal reflection，把"为什么失败 / 下次怎么改"提炼成自然语言 critique，写入 episodic memory buffer；权重不动，所有性能提升来自 prompt context 中反思文本的递归累积。提取过程的迭代逻辑是 trial-by-trial（最多 5 trials），过滤准则隐含在 LLM 的反思 prompt 中（保留对失败原因的诊断与下一步改进建议），不显式排除任何 trace。

[Title]: WorkflowBoost: Distilling Code-Schema Skills into Agent Policies
- [Pathway]: Narrative → Schematic → Policy
- [Source Experience]: Raw interaction trajectories on tool-use tasks
- [Target Experience]: 中间载体——typed Python workflows with I/O specifications（executable workflow library）；最终载体——agent base model 权重
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: workflow library 既作为可执行模块在推理时被 agent invoke，也作为 SFT 监督的中介信号；最终 policy 权重直接生成 action，对未见任务也可调用或仿造 workflow API 契约
- [Method]: ⟨LLM-extract⟩, ⟨SFT⟩
- [Mechanism]: 两阶段链式组合，贡献点在两段衔接。Stage 1（Narrative → Schematic，对应 P2）：critic model 对每条成功 trajectory 做 LLM-extract，把感知顺序的交互轨迹形式化为带 input/output spec 的 typed Python workflow，构成 executable library。Stage 2（Schematic + Narrative → Policy，对应 P5）：用 (instruction, workflow, trajectory) 三元组对 base model 做 supervised fine-tuning，监督信号是行为示范 trajectory，损失为 next-token cross-entropy；workflow 在输入端起 schema 提示作用，引导 policy 学到"调用既有 workflow 或遵守其 API contract"两种行为。整体路径不命中单一 P 编号，但其两段分别对应 P2 与 P5 的链式复合。

[Title]: Pretraining Vision Foundation Models with Masked Autoencoding
- [Pathway]: Out of Scope
- [Mechanism]: 静态图像 patch 重建的自监督预训练，无 (c,a,o,f) 决策语义、无异构动作空间、非 LLM-based agent system，落入 Project_Infos.md §3.2 的「静态语料预训练」与「纯图像分类 / 视觉基础模型训练」两条排除标准。

[Title]: RAFT-Agent: Reward-Ranked Fine-Tuning for Tool Calling
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Sampled tool-using trajectories with scalar rewards（per-prompt K 条候选）
- [Target Experience]: agent policy 权重
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: SFT 直接更新 policy 权重，迭代后 policy 概率质量集中在 high-reward 轨迹上；推理时按权重直接生成，不再依赖 sampling-time 的 reward 过滤
- [Method]: ⟨RL: RAFT⟩
- [Mechanism]: 三轮 sample-rank-finetune 循环。每轮：(1) 用当前 policy per-prompt 采 K 条候选 trajectory；(2) 按 scalar reward 排序，仅保留高于 per-prompt median 的子集；(3) 在过滤后的子集上做 standard SFT，监督信号是 trajectory 自身（next-token cross-entropy），不计算 rejected sample 的 policy gradient。优化目标等价于在 reward-quantile-filtered 经验分布上做 likelihood maximization，避开 PPO 的 actor-critic 训练成本。
> New tag: ⟨RL: RAFT⟩ — Reward-rAnked Fine-Tuning，按 per-prompt reward 中位数过滤后只对 top-half trajectories 做 SFT 的迭代式 RL；与 ⟨RL: ReST⟩ 都属 sample-then-finetune 类，但 ReST 是 Grow / Improve 二阶段且用全局 reward threshold（或 advantage estimate），RAFT 强调 per-prompt 相对排序，过滤粒度与迭代结构均不同，复用 ⟨RL: ReST⟩ 会丢失"prompt-conditional 相对排序"这一判别特征。

## New Tags Introduced
- ⟨RL: RAFT⟩ —— Reward-rAnked Fine-Tuning：按 per-prompt reward 中位数过滤后只对 top-half trajectories 做 SFT 的迭代式 RL 流程。与 ⟨RL: ReST⟩ 区别在过滤粒度（per-prompt 相对 vs 全局 threshold）与迭代结构（单步 sample-rank-finetune vs Grow / Improve 二阶段）。首次出现：「RAFT-Agent: Reward-Ranked Fine-Tuning for Tool Calling」
