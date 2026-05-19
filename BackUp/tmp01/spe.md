[Title]: Generative Adapter: Contextualizing Language Models in Parameters with A Single Forward Pass
- [Pathway]: Out of Scope
- [Mechanism]: 将新上下文（documents, demonstrations, conversations）通过 single forward pass 直接映射为 low-rank LM adapters (Policy params)。源端为任意文本上下文，属于通用 LLM adaptation 技术（knowledge acquisition, ICL, personalization），非 agent 决策经验转化。不满足 §3.1 纳入标准。


[Title]: MemGen: Weaving Generative Latent Memory for Self-Evolving Agents
- [Pathway]: Narrative → Latent (P3)
- [Source Experience]: Agent's current reasoning state / interaction context
- [Target Experience]: Generative latent memory tokens（machine-native memory sequence）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在 agent reasoning 过程中动态生成 latent memory tokens 以 enrich reasoning，形成 memory 与 cognition 的 interwoven cycle
- [Method]: 不清楚（abstract 未明示 memory trigger 和 memory weaver 的训练方式）
- [Mechanism]: 两个组件协同工作：memory trigger 监控 agent reasoning state，决定何时显式调用 memory；memory weaver 以 agent 当前 hidden state 为 stimulus，生成 latent token sequence 作为 machine-native memory。这些 latent tokens 被注入当前推理过程，实现对 past experience 的动态 recall 和 augmentation。abstract 声称在无 explicit supervision 的情况下，MemGen 自发涌现出 planning memory、procedural memory、working memory 等类人记忆类型。


[Title]: Self-Consolidation for Self-Evolving Agents
- [Pathway]: Narrative → Narrative → Policy (P1 + P5, §8.3 composite)
- [Source Experience]: Agent interaction trajectories（both successful and failed attempts）
- [Target Experience]: Compact learnable parameters（policy weights，internalizing historical experience）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 使 agent 在 lifelong interaction 中持续进化，避免重复犯错
- [Method]: ⟨LLM-extract⟩（contrastive reflection, P1）, ⟨SFT⟩（self-consolidation into parameters, P5）
- [Mechanism]: Stage 1 (P1): contrastive reflection strategy 从成功和失败轨迹中显式总结 error-prone patterns 和 reusable insights，将 raw trajectories (Narrative) 提炼为 refined textual experience (Narrative)，此步利用失败样本的 pedagogical value 形成对比学习信号。Stage 2 (P5): self-consolidation mechanism 将 refined textual experience 蒸馏为 compact learnable parameters (Policy)，使 agent 将 extensive historical experience 内化到 latent space 权重中。整体构成 §8.3 的 Narrative (raw) → Narrative (refined) → Policy 复合路径：contribution 在于两阶段间的衔接机制（contrastive reflection 降低噪声 → self-consolidation 以低噪 refined Narrative 做 SFT）。


[Title]: Dejavu: Towards Experience Feedback Learning for Embodied Intelligence
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: Prior execution trajectories in embodied tasks（stored as execution memories）
- [Target Experience]: Experience Feedback Network (EFN) weights — learned retrieval + conditioning mechanism for action prediction
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: EFN 在推理时识别 contextually relevant prior action experiences，conditioning action prediction on retrieved guidance，实现 post-deployment "learning from experience"
- [Method]: ⟨RL⟩（reinforcement learning with semantic similarity rewards）
- [Mechanism]: EFN 将 past execution trajectories (Narrative, stored as memory) 通过 RL 训练转化为 retrieval + conditioning 能力 (Policy weights)。训练信号来自 semantic similarity rewards：鼓励在当前 observation 下预测的 actions 与 past successful behaviors 对齐。部署后 EFN 持续用新 trajectories 扩展 memory，agent 无需 weight update 即可从经验中学习。核心转化是 past experience (Narrative) → EFN policy weights (Policy, P5)，但推理时仍保留 Narrative 形式的 memory 作为检索基底——形成 Policy learns to use Narrative 的混合模式。