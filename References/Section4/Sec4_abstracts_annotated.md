[Title]: Auto-scaling Continuous Memory for GUI Agent
- [Pathway]: Narrative → Latent (P3)
- [Source Experience]: GUI interaction trajectories（screenshots + actions + outcomes）
- [Target Experience]: Continuous memory embeddings（fixed-length latent representation via Q-Former）
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 作为 continuous memory 插入 backbone 的 input layer，在 long-horizon 和 distribution shift 场景下增强 agent 的决策能力
- [Method]: ⟨SFT⟩
- [Mechanism]: 用 VLM 作为 encoder，将每条 GUI trajectory 编码为固定长度的 continuous embeddings（通过 Q-Former 架构）；Q-Former 的 LoRA 参数在 trajectory 数据上以 SFT 训练，使 continuous embeddings 保留 fine-grained visual information 同时大幅减少 context 占用。数据获取通过 auto-scaling flywheel（搜索环境 → VLM 合成任务 → agent rollout → VLM 验证）自动扩展——此 flywheel 构成 Policy → Narrative → Latent 的复合数据管道（agent policy rollout 产生 trajectory → 用于训练 memory encoder），但 flywheel 是 data generation infrastructure 而非论文的核心 transformation mechanism，主路径仍为 P3。推理时检索相关 past trajectory embeddings 并插入 backbone 的 input layer。

[Title]: Log-Augmented Generation: Scaling Test-Time Reasoning with Reusable Computation
- [Pathway]: Tokenized → Latent (P3)
- [Source Experience]: Past task execution logs / reasoning trajectories
- [Target Experience]: KV caches（selectively stored subset of tokens' KV values）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在新任务推理时检索相关 past logs 的 KV values 直接 augment 当前 generation
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 在 past task 执行过程中，LLM 自然产生 KV caches；LAG 选择性地存储部分 tokens 的 KV caches 作为 past reasoning 的 latent 表示。新任务到来时，检索 relevant logs 的 KV values，直接注入当前 forward pass 以 augment generation。与 reflection-based memory 的区别在于跳过了 knowledge extraction / distillation 步骤，直接复用 prior computation。核心转化机制是 token-level forward pass 副产品（KV cache）的选择性保存与检索式复用。

[Title]: Cartridges: Lightweight and general-purpose long context representations via self-study
- [Pathway]: Out of Scope
- [Mechanism]: 该工作的源端为静态文本语料（codebases、legal documents、chat histories），通过 self-study 生成 synthetic conversations 后以 context-distillation objective 训练压缩的 KV cache（Cartridge）。源端缺乏决策过程语义（无 (c,a,o,f) 结构），本质是静态语料的上下文压缩与高效 serving 技术，属于 §3.2「静态语料预训练」排除范畴。

[Title]: FlashMem: Distilling Intrinsic Latent Memory via Computation Reuse
- [Pathway]: Narrative → Latent (P3)
- [Source Experience]: Agent interaction history / transient reasoning states
- [Target Experience]: Consolidated latent memory（通过 Shared-KV Consolidator 从 frozen KV cache 合成）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 为 long-horizon autonomous agent 提供 persistent cognition 能力，避免重复处理完整 history
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 利用内部表示唯一编码输入轨迹的性质，将 last hidden state 视为 interaction history 的 sufficient statistic。Shared-KV Consolidator 直接 attend 到 backbone 的 frozen KV cache 上合成 consolidated latent memory，省去额外的 re-parameterization（与需要独立 encoder 的方法不同）。parameter-free Cognitive Monitor 基于 attention entropy 自适应地在检测到高认知不确定性时触发 consolidation。核心创新在 Latent 层的 computation reuse：不训练新 encoder，而是从已有 forward pass 产物（KV cache）中蒸馏 memory。

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

[Title]: MEM1: Learning to Synergize Memory and Reasoning for Efficient Long-Horizon Agents
- [Pathway]: Narrative → Latent (P3)
- [Source Experience]: Multi-turn interaction trajectories（observations, retrieved information, agent responses）
- [Target Experience]: Compact shared internal state（joint memory + reasoning state，跨 turn 持续更新）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在 long-horizon multi-turn tasks 中以 constant memory 支持 memory consolidation 与 reasoning，替代 full-context prompting
- [Method]: ⟨RL⟩
- [Mechanism]: 每个 turn，agent 将新的 environment observations 与 prior internal state 整合，通过 learned consolidation mechanism 更新 compact internal state，同时 strategically discard irrelevant / redundant information。整个框架以 end-to-end RL 训练，使 agent 学会在 constant memory budget 下进行 reasoning-driven memory consolidation。训练环境通过组合现有数据集构造 arbitrarily complex multi-turn task sequences。
> New tag: ⟨RL⟩ — 通用强化学习标签（abstract 未指定具体 RL 变体如 PPO/GRPO，仅表述为 "end-to-end reinforcement learning"）

[Title]: 3DLLM-Mem: Long-Term Spatial-Temporal Memory for Embodied 3D Large Language Model
- [Pathway]: Out of Scope
- [Mechanism]: 系统通过 working memory tokens (Latent) 作为 queries，cross-attend 到 episodic memory 中的 past observations and interactions，产生 fused spatial-temporal features。核心操作是 attention-based feature fusion within the Latent space（working memory 和 episodic memory 的表示均在连续向量空间中交互），不构成跨 carrier 的经验转化——源经验保持在 episodic memory 中的原有载体形式，attention fusion 是标准 transformer 操作而非 deliberate carrier transformation。属于 memory architecture / retrieval 设计，不满足经验转化的 Embodiment 条件（目标载体未编码源经验的语义内容，仅通过注意力加权融合）。

[Title]: MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation
- [Pathway]: Narrative → Latent (P3)
- [Source Experience]: Embodied interaction history（visual observations + actions + outcomes across long-horizon manipulation）
- [Target Experience]: Perceptual-Cognitive Memory Bank entries（low-level perceptual details + high-level semantics，consolidated from working memory）
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 通过 working memory 检索 memory bank 中 decision-relevant entries，与 current tokens 自适应融合后 conditioning diffusion action expert 生成 temporally aware action sequences
- [Method]: ⟨SFT⟩
- [Mechanism]: Pretrained VLM 将 observation 编码为 perceptual + cognitive tokens 构成 working memory；working memory 的内容经 consolidation（合并冗余信息）后存入 Perceptual-Cognitive Memory Bank，后者分离存储 low-level details 与 high-level semantics。推理时 working memory 从 bank 检索 decision-relevant entries 并自适应融合，conditioning diffusion action expert 输出时序感知的动作序列。整个 memory consolidation 与 retrieval 机制通过训练获得（memory-conditioned diffusion action head），将 raw interaction history 逐步 consolidate 为结构化的 latent memory bank。

[Title]: MAP-VLA: Memory-Augmented Prompting for Vision-Language-Action Model in Robotic Manipulation
- [Pathway]: Narrative → Latent (P3)
- [Source Experience]: Historical demonstration trajectories（task-stage-specific human demonstrations）
- [Target Experience]: Learnable soft prompts（memory units optimized via prompt tuning）
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {human}
- [Utilization]: 实时推理时通过 trajectory similarity matching 检索 relevant memory soft prompts，动态集成到 frozen VLA 中以 augment action generation
- [Method]: ⟨SFT⟩
- [Mechanism]: 第一阶段（memory construction）：从 historical human demonstrations 中按 task stage 切分 trajectory 片段，每段通过 prompt tuning 优化为 learnable soft prompt（Latent carrier），形成 memory library；soft prompt 的训练目标是最小化基于该 stage context 的 action prediction error。第二阶段（inference）：实时执行时通过 trajectory similarity matching 检索最相关的 stage memory soft prompts，将其拼接到 frozen VLA 的输入层以 augment action generation。plug-and-play 设计意味着 soft prompts 作为独立 memory module 作用，不修改 VLA 权重。

[Title]: Towards General Continuous Memory for Vision-Language Models
- [Pathway]: Out of Scope
- [Mechanism]: 该工作将 VLM 微调为 continuous memory encoder，将 multimodal / multilingual knowledge 压缩为 8 个 continuous embeddings，用于增强 complex multimodal reasoning。源端为静态多模态知识（text + images），非 agent 决策过程经验（无 (c,a,o,f) 结构），属于 §3.2「静态语料预训练」排除范畴——本质是 knowledge compression 而非 experience transformation。

[Title]: Dual Latent Memory for Visual Multi-agent System
- [Pathway]: Narrative → Latent (P3)
- [Source Experience]: Visual multi-agent perception and thinking trajectories（perceptual + reasoning trajectories in collaborative tasks）
- [Target Experience]: Dual latent memories（decoupled perception memory + thinking memory）
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {self}
- [Utilization]: 在 inter-agent collaboration 中以 on-demand latent memory access 替代被动文本通信，打破 text-centric communication 的 information bottleneck
- [Method]: 不清楚（abstract 描述了 dual latent memory 的合成与 entropy-driven triggering 机制，但未指明 memory 合成模块的训练方式）
- [Mechanism]: 将 visual MAS 中的 perception 和 thinking 解耦，分别动态合成为 dual latent memories。entropy-driven proactive triggering 机制根据信息熵主动触发 on-demand memory access，替代传统的被动文本信息传递。核心动机是避免将 perceptual / thinking trajectories 转换为离散自然语言时的 semantic loss，直接在 latent space 进行 inter-agent memory 共享。

[Title]: Latent Context Compilation: Distilling Long Context into Compact Portable Memory
- [Pathway]: Out of Scope
- [Mechanism]: 使用 disposable LoRA module 作为 compiler，将长文本上下文蒸馏为 compact buffer tokens（stateless portable memory artifacts）。源端为任意长文本上下文（documents 等），非 agent 决策过程经验。属于 §3.2「静态语料预训练」排除范畴——本质是 LLM serving 的 context compression 技术。

[Title]: In-context Autoencoder for Context Compression in a Large Language Model
- [Pathway]: Out of Scope
- [Mechanism]: 使用 ICAE（In-context Autoencoder）将长文本上下文压缩为 compact memory slots，pretraining 使用 autoencoding + language modeling objectives。源端为 massive text data / 长文本上下文，非 agent 决策过程经验。属于 §3.2「静态语料预训练」排除范畴——本质是 LLM context window 扩展与压缩技术。

[Title]: Adapting Language Models to Compress Contexts
- [Pathway]: Out of Scope
- [Mechanism]: 将 pre-trained LM 适配为 AutoCompressors，将长文档分段压缩为 summary vectors（soft prompts）。源端为静态长文本文档（用于 language modeling / ICL demonstrations / retrieval-augmented LM），非 agent 决策过程经验。属于 §3.2「静态语料预训练」排除范畴——本质是 LLM context window 扩展技术。

[Title]: LatentMem: Customizing Latent Memory for Multi-Agent Systems
- [Pathway]: Narrative → Latent (P3)
- [Source Experience]: Raw multi-agent interaction trajectories（experience bank 中存储）
- [Target Experience]: Compact role-customized latent memories（via memory composer）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 为 MAS 中每个 agent 提供 role-aware customized latent memory，以 token-efficient 方式支持 continual adaptation
- [Method]: ⟨RL⟩
- [Mechanism]: 两阶段架构：experience bank 以 lightweight form 存储 raw interaction trajectories（Narrative）；memory composer 以 retrieved experience + agent-specific context 为条件，合成 compact latent memories（Latent）。核心训练机制为 Latent Memory Policy Optimization (LMPO)：将 task-level optimization signals 通过 latent memories 反向传播到 composer，鼓励其产生 compact 且 high-utility 的 latent representations。LMPO 是专为 latent memory 合成设计的 RL-style optimization。
> New tag: 此论文引入 LMPO（Latent Memory Policy Optimization），属 ⟨RL⟩ 的新具体变体，但目前 ⟨RL⟩ 标签已足够覆盖，不新增子标签。

[Title]: ReasonCACHE: Teaching LLMs To Reason Without Weight Updates
- [Pathway]: Out of Scope
- [Mechanism]: 使用 Prefix Tuning 将 task demonstrations 蒸馏为 fixed KV cache，使 LLM 在不更新权重的情况下学习推理。源端为静态推理样例（GPQA-Diamond 等 benchmark 的 few-shot demonstrations），非 agent 与环境交互产生的决策经验（无 observation/feedback 闭环）。属于 §3.2「静态语料预训练」排除范畴——本质是 ICL 效率优化与 context compression 技术。

[Title]: GradMem: Learning to Write Context into Memory with Test-Time Gradient Descent
- [Pathway]: Out of Scope
- [Mechanism]: 通过 test-time gradient descent 将长文本上下文写入 prefix memory tokens，优化 self-supervised context reconstruction loss。源端为静态文本上下文（associative retrieval、bAbI、SQuAD 等 QA passages），非 agent 决策过程经验（无 (c,a,o,f) 结构）。属于 §3.2「静态语料预训练」排除范畴——本质是 context compression 技术。

[Title]: Deliberation in Latent Space via Differentiable Cache Augmentation
- [Pathway]: Out of Scope
- [Mechanism]: 训练 offline coprocessor 在 frozen LLM 的 KV cache 中注入 latent embeddings 以增强后续 decoding。coprocessor 使用 standard pretraining data 的 language modeling loss 训练。源端为静态预训练语料，非 agent 决策过程经验。属于 §3.2「静态语料预训练」排除范畴。

[Title]: Trained Persistent Memory for Frozen Encoder--Decoder LLMs: Six Architectural Methods
- [Pathway]: Narrative → Latent (P3)
- [Source Experience]: Conversation history / interaction context（LoCoMo dataset 对话记录）
- [Target Experience]: Persistent latent memory bank（continuous dense vectors，跨 session 累积）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在 conversational learning 场景中跨 session 持久化记忆，使 frozen backbone 具备持续学习能力
- [Method]: ⟨SFT⟩
- [Mechanism]: 在 frozen encoder-decoder LLM 上训练小型 memory adapter（θ_mem），实现六种 differentiable read/write 架构方法（三种 injection points × 四种 write mechanisms）。每次 write 将当前 conversation context 通过 differentiable operation 写入 persistent latent memory bank（dense vectors）；read 时从 bank 中检索并通过 cross-attention 注入 decoder。训练仅更新 adapter 参数，推理时 memory bank 可无梯度持续累积。核心贡献是建立了 latent persistent memory 的架构设计空间（design-space taxonomy）和 feasibility baseline。

[Title]: Trained Persistent Memory for Frozen Decoder-Only LLMs
- [Pathway]: Narrative → Latent (P3)
- [Source Experience]: Conversation history / interaction context（LoCoMo dataset）
- [Target Experience]: Persistent latent memory bank（adapted for decoder-only self-attention injection）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 为 decoder-only LLM 提供跨 session persistent memory，证明 latent persistent memory 范式在 decoder-only 架构上同样可行
- [Method]: ⟨SFT⟩
- [Mechanism]: 将 #19 的六种 persistent memory 方法从 encoder-decoder 适配到 decoder-only 架构（frozen GPT-2），关键变化是 read injection 从 cross-attention 改为 self-attention KV prefix 或 parallel branch。训练仅更新小型 memory adapter θ_mem。发现强 inductive bias 的方法（cross-attention、Hebbian、slot write）在低容量下表现更好，高容量下所有方法收敛。与 #19 一起建立了 latent persistent memory 作为跨 transformer 家族的通用范式。

[Title]: Hybrid Self-evolving Structured Memory for GUI Agents
- [Pathway]: Narrative → Schematic (P2)（主路径）；Narrative → Latent (P3)（并列分支）
- [Source Experience]: GUI agent interaction trajectories（long-horizon computer-use tasks）
- [Target Experience]: Graph-based hybrid memory — discrete high-level symbolic graph nodes（S-Tok）+ continuous trajectory embeddings（Lat）
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 通过 graph structure 支持 multi-hop retrieval，node update operations 支持 self-evolution，on-the-fly working-memory refreshing 支持推理时记忆刷新
- [Method]: 不清楚（abstract 未明示 graph 构建与 node update 的训练方式）
- [Mechanism]: 从 GUI agent 的交互轨迹同时构建两类载体：(1) 离散的高层 symbolic graph nodes（Schematic, P2），组织为 graph structure 以支持 multi-hop 检索与 node-level self-evolution；(2) continuous trajectory embeddings（Latent, P3），捕捉细粒度轨迹信息。两类载体耦合在同一 graph-based memory 中，推理时通过 working-memory refreshing 动态更新。multi-target 并列模式（§8.8），不构成链式衔接。

[Title]: TempoFit: Plug-and-Play Layer-Wise Temporal KV Memory for Long-Horizon Vision-Language-Action Manipulation
- [Pathway]: Narrative → Latent (P3)
- [Source Experience]: Past timesteps' visual observations and actions in manipulation tasks
- [Target Experience]: Layer-wise FIFO prefix KV caches with Frame-Gap Temporal Bias（training-free temporal memory state）
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 在 long-horizon non-Markovian manipulation 中为 frozen VLA 提供 temporal history，消除 occlusion / state aliasing 导致的决策失败
- [Method]: ⟨LLM-extract⟩（training-free，无参数更新）
- [Mechanism]: 利用 VLA forward pass 自然产生的 prefix attention KV caches 作为 model-native content-addressable runtime state。在每个 timestep，将选定中间层的 prefix KV 按 FIFO 存储在 layer-wise memory 中。推理时通过 parameter-free K-to-K retrieval + Frame-Gap Temporal Bias（FGTB, fixed recency bias）检索相关 past KV，以 pre-attention residual loading + norm-preserving rescaling 注入当前 forward pass。完全 training-free，不修改 frozen VLA 权重。核心创新是 KV cache 跨 timestep 复用的 training-free 机制。

[Title]: Online Adaptation of Language Models with a Memory of Amortized Contexts
- [Pathway]: Out of Scope
- [Mechanism]: 将新文档通过 feature extraction + amortization-based meta-learning 压缩为 compact modulations 存储在 memory bank 中，用于在线适应 LLM 知识。源端为静态文本文档（unseen documents for knowledge updating），非 agent 决策过程经验。属于 §3.2「静态语料预训练」排除范畴——本质是 online knowledge adaptation 技术。

[Title]: Compressed Context Memory For Online Language Model Interaction
- [Pathway]: Out of Scope
- [Mechanism]: 使用 conditional LoRA 持续将累积的 attention KV pairs 压缩为 compact memory space。源端为在线对话/交互的 accumulating context（conversation, personalization, multi-task learning），非 agent 决策经验（无 (c,a,o,f) 结构）。属于 §3.2 排除范畴——本质是 online context compression for LLM serving。

[Title]: EchoVLA: Synergistic Declarative Memory for VLA-Driven Mobile Manipulation
- [Pathway]: Narrative → Schematic (P2)（主路径 scene memory）；Narrative → Latent (P3)（并列分支 episodic memory）
- [Source Experience]: Mobile manipulation trajectories（navigation + manipulation with multimodal observations）
- [Target Experience]: Scene memory（spatial-semantic maps, S-Tok）+ Episodic memory（task-level multimodal contextual features, Lat）
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}（MLLM-guided planning + expert-level trajectories）, {human}（real-robot demonstrations）
- [Utilization]: 两种 memory 的 retrieved representations 通过 coarse- and fine-grained attention 融合后 conditioning base-arm diffusion policies，指导 mobile manipulation 动作生成
- [Method]: ⟨SFT⟩（imitation learning from expert trajectories）
- [Mechanism]: 从 mobile manipulation 交互中同时构建两类并列 memory：(1) Scene memory（Schematic, P2）维护 spatial-semantic maps 的 collection，提供空间定位与导航上下文；(2) Episodic memory（Latent, P3）存储 task-level experiences with multimodal contextual features。两种 memory 独立存储、更新与检索，其 representations 通过 coarse- and fine-grained attention 融合后 conditioning diffusion action policies。multi-target 并列模式（§8.8），两 memory 共享同源经验但不构成链式衔接。训练数据通过 MLLM-guided planning + feedback-driven refinement 自动生成（MoMani benchmark）。

[Title]: KEEP: A KV-Cache-Centric Memory Management System for Efficient Embodied Planning
- [Pathway]: Narrative → Latent (P3)
- [Source Experience]: Embodied planning experiences（past experiences and environmental states in long-horizon tasks）
- [Target Experience]: Efficiently managed KV caches（via Static-Dynamic Memory Construction, Multi-hop Re-computation, Layer-balanced Loading）
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 为 embodied planning LLM 提供高效 KV cache 记忆管理，避免 raw text memory 的过长 prompts 和高 prefill latency
- [Method]: ⟨LLM-extract⟩（memory management 层面 training-free，核心是算法优化而非模型训练）
- [Mechanism]: 三类 KV cache 管理创新：(1) Static-Dynamic Memory Construction——混合粒度 memory group 减少 KV cache recomputation；(2) Multi-hop Memory Re-computation——动态识别跨 memory group 的重要 cross-attention 并迭代重建 memory interactions；(3) Layer-balanced Memory Loading——消除跨层不均衡的 KV cache loading。底层经验转化仍为 P3（interaction history → KV cache），贡献在 KV cache 管理效率的系统层面优化。

[Title]: Vision-Language Memory for Spatial Reasoning
- [Pathway]: Narrative → Latent (P3)
- [Source Experience]: Video-based spatial observations（2D video of 3D environments）
- [Target Experience]: Consolidated episodic memory（critical long-term 3D-aware spatial representations）+ working memory（sliding window of immediate context）
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 为 robot spatial reasoning 提供 persistent 3D-aware memory，支持 long-horizon spatial reasoning with fixed computational cost
- [Method]: 不清楚（abstract 描述了 dual-memory 架构但未指明 memory consolidation 的训练方式）
- [Mechanism]: 两种 memory 协同：working memory 以 sliding window 聚焦 immediate spatial context（Tokenized）；episodic memory consolidates 并存储 critical long-term 3D 空间信息（Latent，从 2D video 中构建 view-consistent 3D-aware representation）。episodic memory 的 consolidation 过程实现从 sequential video observations (Narrative) 到 compressed latent spatial representations 的转化 (P3)。

[Title]: In-context Vectors: Making In Context Learning More Effective and Controllable Through Latent Space Steering
- [Pathway]: Out of Scope
- [Mechanism]: 从 demonstration examples 的 forward pass 中提取 latent embedding 作为 in-context vector (ICV)，用于 steering LLM latent states。源端为静态 task demonstrations（safety, style transfer, role-playing 等），非 agent 决策过程经验。属于 §3.2 排除范畴——本质是 ICL 的 latent space 替代方案，不涉及 agent experience transformation。

[Title]: VPWEM: Non-Markovian Visuomotor Policy with Working and Episodic Memory
- [Pathway]: Narrative → Latent (P3)
- [Source Experience]: Historical visual observations beyond working memory window（out-of-window embodied observations）
- [Target Experience]: Fixed number of episodic memory tokens（compressed via Transformer-based contextual memory compressor）
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {human}（imitation learning from human demonstrations）
- [Utilization]: 与 working memory（sliding window of recent tokens）共同 conditioning diffusion policy，生成 temporally aware action sequences
- [Method]: ⟨SFT⟩（imitation learning，compressor 与 policy 联合训练）
- [Mechanism]: Transformer-based contextual memory compressor 递归地将超出 working memory window 的历史 observations 压缩为固定数量的 episodic memory tokens (Latent)。compressor 使用 self-attention over past summary tokens cache + cross-attention over historical observations cache，与 policy 以 imitation learning 联合训练。核心转化是 sequential visual observations (Narrative) → compressed episodic memory tokens (Latent, P3)，每步 memory 和计算量近乎恒定。

[Title]: Memorizing Transformers
- [Pathway]: Out of Scope
- [Mechanism]: 通过 approximate kNN lookup 在 non-differentiable memory 中存储和检索 past inputs 的 internal representations（key-value pairs），增强语言模型的推理时记忆能力。源端为任意文本输入（webtext, math papers, code 等），属于通用语言模型架构增强，非 agent 决策经验转化。不满足 §3.1 的决策过程语义要求。

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

[Title]: MemoryPrompt: A Light Wrapper to Improve Context Tracking in Pre-trained Language Models
- [Pathway]: Out of Scope
- [Mechanism]: 使用小型辅助 recurrent network 将对话历史和 fact updates 编码为 soft prompt vectors（Latent），prefix 到 LM 输入。源端为对话上下文追踪任务（fact updates tracking, long-distance dialogue），属于语言理解任务而非 agent 决策经验（无异构动作空间的环境交互）。不符合 §3.1 的纳入标准。

[Title]: VisMem: Latent Vision Memory Unlocks Potential of Vision-Language Models
- [Pathway]: Out of Scope
- [Mechanism]: 为 VLM 添加 dynamic latent vision memories（short-term perceptual + long-term semantic），解决 prolonged generation 中的 visual processing bottleneck。源端为静态 visual input 在生成过程中的视觉特征，属于 VLM 推理增强而非 agent 与环境交互的决策经验转化。不符合 §3.1 的纳入标准。

[Title]: TokMem: One-Token Procedural Memory for Large Language Models
- [Pathway]: Out of Scope
- [Mechanism]: 将 reusable task procedure 编译为单一 trainable memory token（Latent），用于控制 LLM 行为。源端为静态 task instructions（Super-Natural Instructions, function-calling specs），属于 task procedure compilation 而非 agent 与环境交互的决策经验转化。不符合 §3.1 的纳入标准。

[Title]: Implicit In-context Learning
- [Pathway]: Out of Scope
- [Mechanism]: 从 demonstration examples 提取 condensed context vector（Latent），通过 inference-time residual stream intervention 替代显式 ICL。源端为静态 task demonstrations，非 agent 决策经验。属于 §3.2 排除范畴——本质是 ICL 效率优化技术。

[Title]: ReMem-VLA: Empowering Vision-Language-Action Model with Memory via Dual-Level Recurrent Queries
- [Pathway]: Narrative → Latent (P3)
- [Source Experience]: Historical visual observations across consecutive frames and temporal chunks in closed-loop robot control
- [Target Experience]: Dual-level recurrent memory queries — frame-level (short-term) + chunk-level (long-term) memory representations
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 在 closed-loop robot control 中隐式引导 action prediction，使 VLA 突破 Markov 假设限制，处理需要 historical context 的任务
- [Method]: ⟨SFT⟩（end-to-end training with Past Observation Prediction auxiliary objective）
- [Mechanism]: 两组 learnable recurrent queries 在推理过程中持续聚合和维持 temporal context：frame-level queries 在连续帧间传播 short-term 信息，chunk-level queries 在 temporal chunks 间传输 long-term 上下文。queries 通过 end-to-end 训练学会选择性聚合 relevant historical context，无需 external memory bank retrieval。Past Observation Prediction 作为 auxiliary objective 增强 visual memory。与 MemoryVLA 的 external memory bank 方案不同，ReMem-VLA 采用 recurrent queries 实现 implicit memory，避免 explicit retrieval 中的 distractor 干扰。

[Title]: Streaming Video Question-Answering with In-context Video KV-Cache Retrieval
- [Pathway]: Out of Scope
- [Mechanism]: 通过 sliding-window attention + KV cache 存储/检索实现流式视频 QA。源端为流式视频帧，属于 VideoQA 效率优化而非 agent 决策经验转化。不满足 §3.1 的决策过程语义要求。

[Title]: HAMLET: Switch your Vision-Language-Action Model into a History-Aware Policy
- [Pathway]: Narrative → Latent (P3)
- [Source Experience]: Historical visual observations at each timestep in robotic manipulation
- [Target Experience]: Memory features（moment tokens integrated across past timesteps via lightweight memory module）
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: conditioning action prediction on historical context，使原本 Markovian VLA 变为 history-aware policy
- [Method]: ⟨SFT⟩（time-contrastive learning for moment token initialization + end-to-end training of memory module）
- [Mechanism]: 每个 timestep 的 perceptual information 被压缩为 moment token（Latent）。moment tokens 通过 time-contrastive learning 初始化，使其更好地捕捉 temporally distinctive aspects。lightweight memory module 将 past timesteps 的 moment tokens 整合为 memory features，用于 conditioning action prediction。整体将 sequential visual observations (Narrative) 通过 moment token encoding + temporal integration 转化为 memory features (Latent, P3)，使 VLA 无需 external memory bank 即可利用历史上下文。

[Title]: ContextVLA: Vision-Language-Action Model with Amortized Multi-Frame Context
- [Pathway]: Narrative → Latent (P3)
- [Source Experience]: Multi-frame visual observations in partially observable robotic tasks
- [Target Experience]: Single context token（compressed multi-frame temporal context）
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 在 behavior cloning 中以压缩后的单 token 为 policy 提供 multi-frame temporal context，提升 partially observable 场景下的动作预测
- [Method]: ⟨SFT⟩（behavior cloning with amortized context compression）
- [Mechanism]: 利用 VLM backbone 的 inherent temporal understanding capability 从 multi-frame observations 中提取 meaningful context，将 past observations 压缩为 single context token (Latent)。该 token 作为 amortized temporal context 在 action generation 时 conditioning policy，避免 full multi-frame 的高计算开销同时保持 temporal context 的益处。核心转化是 multi-frame visual observations (Narrative, [embodied]) → single context token (Latent, P3)。

[Title]: Cache-to-Cache: Direct Semantic Communication Between Large Language Models
- [Pathway]: Out of Scope
- [Mechanism]: 使用神经网络将 source model 的 KV cache 投影并融合到 target model 的 KV cache，实现 LLM 间的直接语义传输。源端为任意 LLM 处理内容的 KV cache，属于 inter-model communication protocol 而非 agent 经验转化。缺乏 §3.1 的决策过程语义结构（无 (c,a,o,f) 闭环）。

[Title]: MA-LMM: Memory-Augmented Large Multimodal Model for Long-Term Video Understanding
- [Pathway]: Out of Scope
- [Mechanism]: 以 online manner 处理视频并将 past video information 存储在 memory bank 中，用于 long-term video understanding (QA, captioning)。源端为视频内容，非 agent 决策经验。不满足 §3.1 的决策过程语义要求与异构动作空间条件。

[Title]: AstraNav-Memory: Contexts Compression for Long Memory
- [Pathway]: Narrative → Latent (P3)
- [Source Experience]: Visual observations during lifelong embodied navigation（spatial-semantic experience across tasks and environments）
- [Target Experience]: Compressed image-centric memory（visual context compression via ViT + PixelUnshuffle+Conv tokenizer, ~30 tokens per image at 16× compression）
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 为 lifelong embodied navigation agent 提供 compressed visual history memory，使其在 novel 和 familiar 环境中高效探索与导航
- [Method]: ⟨SFT⟩（visual tokenizer end-to-end coupled with navigation policy training）
- [Mechanism]: visual tokenizer（ViT backbone + frozen DINOv3 features + lightweight PixelUnshuffle+Conv blocks）将每帧导航观测 (Narrative, [embodied]) 编码为约 30 tokens 的 compressed visual representation (Latent)，支持可配置压缩率。通过 end-to-end 与 Qwen2.5-VL navigation policy 联合训练，使压缩 tokens 保留 navigation-relevant spatial-semantic 信息。有效 context capacity 从数十张图像扩展到数百张，实现 lifelong visual memory。

[Title]: Streaming Long Video Understanding with Large Language Models
- [Pathway]: Out of Scope
- [Mechanism]: Memory-Propagated Streaming Encoding 将长视频分段编码，每段以前段 encoded results 为 historical memory 进行压缩。源端为视频内容，用于 video QA 和 temporal comprehension。非 agent 决策经验转化。不满足 §3.1 纳入标准。

[Title]: Long Context Compression with Activation Beacon
- [Pathway]: Out of Scope
- [Mechanism]: 直接压缩 transformer 每层的 activations (keys & values)，通过 compression-based auto-regression 训练。源端为长文本上下文（document understanding, few-shot learning, Needle-in-a-Haystack），非 agent 决策经验。属于通用 LLM context compression 技术。

[Title]: StreamMem: Query-Agnostic KV Cache Memory for Streaming Video Understanding
- [Pathway]: Out of Scope
- [Mechanism]: 以 streaming manner 编码新视频帧，使用 attention scores between visual tokens and generic query tokens 压缩 KV cache。源端为流式视频帧，用于 video QA。非 agent 经验转化。不满足 §3.1 纳入标准。

[Title]: Scaling the Long Video Understanding of Multimodal Large Language Models via Visual Memory Mechanism
- [Pathway]: Out of Scope
- [Mechanism]: 以 visual KV caches 为 memory sources，通过 dual-pathway compression 实现 memory transfer/writing 和 reading。源端为视频的 visual KV caches，用于 long video understanding (GPT-4o/Gemini-1.5 Pro 级别的 video QA)。非 agent 经验转化。不满足 §3.1 纳入标准。

[Title]: HERMES: KV Cache as Hierarchical Memory for Efficient Streaming Video Understanding
- [Pathway]: Out of Scope
- [Mechanism]: 将 KV cache 概念化为 hierarchical memory framework，以多粒度封装视频信息。training-free，复用 compact KV cache 实现流式视频理解的实时响应。源端为视频流，非 agent 经验。不满足 §3.1 纳入标准。

[Title]: XC-Cache: Cross-Attending to Cached Context for Efficient LLM Inference
- [Pathway]: Out of Scope
- [Mechanism]: 使用 cross-attention（而非 self-attention prompting）condition generation on reference text，训练少量新增层的 cross-attention cache。源端为 QA reference text，属于 ICL 效率优化。不满足 §3.1 纳入标准。

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

[Title]: Generative Adapter: Contextualizing Language Models in Parameters with A Single Forward Pass
- [Pathway]: Out of Scope
- [Mechanism]: 将新上下文（documents, demonstrations, conversations）通过 single forward pass 直接映射为 low-rank LM adapters (Policy params)。源端为任意文本上下文，属于通用 LLM adaptation 技术（knowledge acquisition, ICL, personalization），非 agent 决策经验转化。不满足 §3.1 纳入标准。

[Title]: Dolphin: Long Context as a New Modality for Energy-Efficient On-Device Language Models
- [Pathway]: Out of Scope
- [Mechanism]: 使用 compact 0.5B decoder 将长文本上下文蒸馏为 memory embedding，减少 primary decoder 的输入长度。源端为任意长文本上下文，属于 on-device LLM 的 energy-efficient context processing。不满足 §3.1 纳入标准。

[Title]: VideoScan: Enabling Efficient Streaming Video Understanding via Frame-level Semantic Carriers
- [Pathway]: Out of Scope
- [Mechanism]: 每帧用 single semantic carrier token 表示，KV pairs 训练以保留前帧 contextual semantics。源端为流式视频帧，用于 video understanding。非 agent 决策经验转化。不满足 §3.1 纳入标准。

[Title]: CompLLM: Compression for Long Context Q&A
- [Pathway]: Out of Scope
- [Mechanism]: 将长文本上下文分段独立压缩为 latent representations，支持线性复杂度压缩和跨 query 复用。源端为 long text contexts for QA，属于通用 context compression 技术。不满足 §3.1 纳入标准。

[Title]: Combee: Scaling Prompt Learning for Self-Improving Language Model Agents
- [Pathway]: Policy → Narrative → Narrative (P7 + P1 composite; prompt-level self-improvement loop, 非 weight-level §8.1)
- [Source Experience]: Agent execution traces（aggregate agentic traces from multiple parallel agent runs）
- [Target Experience]: Optimized system prompts（learned task-relevant knowledge in textual prompt form）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 作为 system prompt 注入 agent，提升后续任务执行准确率，实现 self-improving；improved prompts 使 agent 产生更高质量的 traces，形成持续的 prompt-level 自改进循环
- [Method]: ⟨LLM-extract⟩（prompt learning from aggregate traces, no parameter update）
- [Mechanism]: 两阶段复合：(1) P7 (Policy → Narrative)：agent policy 执行任务产生 execution traces（Narrative），此步将 policy 的隐式决策能力外化为显式轨迹文本；(2) P1 (Narrative → Narrative)：通过 parallel scans + augmented shuffle mechanism + dynamic batch size controller 从 aggregate traces 中学习 optimized system prompts。核心创新在 P1 的 scaling——将 prompt learning 扩展到高并行度（up to 17× speedup）。整体构成 prompt-level self-improvement loop：improved prompts → better agent behavior → better traces → further prompt improvement，闭环在 Narrative 层而非 Parametric 层（无 weight update），与 §8.1 weight-level loop 形成对比。

[Title]: Latent Collaboration in Multi-Agent Systems
- [Pathway]: Out of Scope
- [Mechanism]: 各 agent 通过 last-layer hidden embeddings 生成 auto-regressive latent thoughts，shared latent working memory 保存并传输 internal representations，实现纯 latent 多智能体协作。属于 inter-agent communication protocol（Latent → Latent 传输），源端为 agent hidden states 用于 math/science reasoning 等静态任务，缺乏环境交互的 (c,a,o,f) 闭环。不属于跨 carrier 的经验转化。

[Title]: Accelerating Language Model Workflows with Prompt Choreography
- [Pathway]: Out of Scope
- [Mechanism]: 维护 dynamic global KV cache，每个 LLM call 可 attend to 任意重排的 previously encoded messages 子集。属于 multi-agent LLM workflow 的 KV cache 管理与计算效率优化，非 agent 经验转化。不满足 §3.1 纳入标准。

[Title]: Learning to Compress Prompts with Gist Tokens
- [Pathway]: Out of Scope
- [Mechanism]: 训练 LM 将 prompts 压缩为 gist tokens (Latent)，通过修改 attention mask 实现 prompt compression。源端为静态 task prompts，属于通用 prompt compression 技术。非 agent 经验转化。不满足 §3.1 纳入标准。

[Title]: RelayCaching: Accelerating LLM Collaboration via Decoding KV Cache Reuse
- [Pathway]: Out of Scope
- [Mechanism]: 直接复用 previous agents 的 decoding phase KV caches 到 subsequent agents 的 prefill phase，选择性重计算 prefix-induced deviation 位置的 KV。属于 multi-agent LLM 系统的 KV cache 复用与计算效率优化，非 agent 经验转化。不满足 §3.1 纳入标准。

[Title]: video-SALMONN S: Streaming Audio-Visual LLMs Beyond Length Limits via Memory
- [Pathway]: Out of Scope
- [Mechanism]: test-time-training (TTT) memory module 持续更新 token representations 以捕捉 long-range dependencies，prompt-dependent memory reader 选择性检索。源端为音视频流（3-hour videos at 1 FPS），用于 video understanding。非 agent 经验转化。不满足 §3.1 纳入标准。

[Title]: Dynamic Long Context Reasoning over Compressed Memory via End-to-End Reinforcement Learning
- [Pathway]: Out of Scope
- [Mechanism]: 将 long inputs 分块编码为 compressed memory representations，gating module 动态选择相关 memory blocks，reasoning module 迭代处理。compressor 和 reasoner 通过 end-to-end RL 联合优化。源端为 long text inputs (multi-hop reasoning benchmarks)，属于 long-context reasoning 效率优化。非 agent 与环境交互的决策经验。不满足 §3.1 纳入标准。

[Title]: PolarMem: A Training-Free Polarized Latent Graph Memory for Verifiable Multimodal Agents
- [Pathway]: Narrative → Schematic (P2)（主路径 graph topology）；Narrative → Latent (P3)（并列分支 latent node representations）
- [Source Experience]: Multimodal agent perceptual inputs（fuzzy perceptual likelihoods from frozen VLMs）
- [Target Experience]: Polarized latent graph memory — graph topology with orthogonal inhibitory connections (S-Tok) + latent node representations (Lat) — 显式编码 verified negation
- [Source Modality]: [cross-modal]
- [Target Modality]: [cross-modal]
- [Experience Source]: {self}
- [Utilization]: 在推理时通过 logic-dominant retrieval paradigm 为 multimodal agent 提供 verifiable evidence grounding，suppress hallucinatory patterns that violate negative constraints
- [Method]: ⟨LLM-extract⟩（training-free, non-parametric distributional partitioning）
- [Mechanism]: 两阶段 training-free 转化：(1) non-parametric distributional partitioning 将 VLM 的 fuzzy perceptual likelihoods (Narrative) 转化为 discrete logical constraints，构建 polarized graph topology with orthogonal inhibitory connections (Schematic, P2)；(2) graph nodes 同时携带 latent representations (Latent, P3) 编码感知信息。关键创新是 polarized graph 结构：explicitly store verified negation as a primary cognitive state（而非仅存正例），通过 inhibitory connections 实现逻辑约束。推理时 logic-dominant retrieval 抑制违反 negative constraints 的 hallucinatory patterns。multi-target 并列模式（§8.8）。

[Title]: KV Packet: Recomputation-Free Context-Independent KV Caching for LLMs
- [Pathway]: Out of Scope
- [Mechanism]: 将 cached documents 封装为 immutable KV "packets"，通过 lightweight trainable soft-token adapters 桥接 context discontinuities，实现跨上下文 recomputation-free KV cache 复用。源端为静态文档，属于 KV cache 复用效率优化。不满足 §3.1 纳入标准。

[Title]: Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices
- [Pathway]: Narrative → Latent (P3)（底层转化为 forward pass 自然产物；论文贡献在 persistence / quantization 系统层）
- [Source Experience]: Multi-agent conversation / interaction context
- [Target Experience]: Persistent Q4-quantized KV caches（disk-persisted, directly reloadable into attention layers）
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 在 edge device 上为 multi-agent LLM 系统提供跨 session persistent KV cache，消除反复 re-prefill 的计算开销
- [Method]: ⟨LLM-extract⟩（training-free, 贡献在 Q4 quantization + persistence 系统而非模型训练）
- [Mechanism]: 底层经验转化仍为 P3：multi-agent interaction context (Narrative) 通过 forward pass 自然产生 KV caches (Latent)。论文的系统层面贡献是：(1) block pool 提供 per-agent isolated Q4 KV caches in safetensors format；(2) BatchQuantizedKVCache 支持多 agent quantized caches 的并发推理；(3) cross-phase context injection 跨对话阶段累积 attention state 无需重计算。Q4 quantization 使相同 memory budget 下可容纳 4× agent contexts，cache restoration 实现 up to 136× TTFT reduction。

[Title]: Memory3: Language Modeling with Explicit Memory
- [Pathway]: Out of Scope
- [Mechanism]: 提出 explicit memory 作为 LLM 的第三种记忆形式（继 implicit memory/model parameters 和 working memory/context KV 之后），使用 memory sparsification mechanism 和 two-stage pretraining 将知识 externalize 到 sparse key-value store。源端为 pretraining data（raw text），属于 LLM 知识存储架构设计。非 agent 决策经验转化。不满足 §3.1 纳入标准。

[Title]: KV Cache Steering for Controlling Frozen LLMs
- [Pathway]: Out of Scope
- [Mechanism]: 从 teacher model 或 human annotations 的 reasoning traces 构建 steering vectors，以 one-shot intervention 注入 KV cache 以控制 LLM 推理行为（CoT induction, reasoning style transfer）。源端为 static reasoning traces（teacher demonstrations），属于 LLM behavior steering 技术。非 agent 与环境交互的决策经验转化。不满足 §3.1 纳入标准。

[Title]: Gated Memory Policy
- [Pathway]: Narrative → Latent (P3)
- [Source Experience]: Historical observations and actions in robotic manipulation（spanning Markovian to non-Markovian tasks）
- [Target Experience]: Latent memory representations（via lightweight cross-attention module with learned gating）
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: conditioning visuomotor action prediction on selectively activated historical context, 在需要记忆时调用、不需要时保持 reactive
- [Method]: ⟨SFT⟩（behavior cloning with learned memory gate + cross-attention）
- [Mechanism]: 两个关键 learned 机制：(1) memory gate 学习 when to recall——仅在必要时选择性激活 history context，增强鲁棒性和反应性；(2) lightweight cross-attention module 学习 what to recall——从历史观测和动作中构建 effective latent memory representations (Latent, P3)。额外引入 diffusion noise injection 到历史动作中以增强对 noisy/inaccurate histories 的鲁棒性。整体将 historical observations (Narrative, [embodied]) 通过 gated cross-attention 转化为 latent memory representations。

[Title]: Chameleon: Episodic Memory for Long-Horizon Robotic Manipulation
- [Pathway]: Narrative → Latent (P3)
- [Source Experience]: Embodied interaction history under perceptual aliasing（geometry-grounded multimodal observations + actions）
- [Target Experience]: Geometry-grounded multimodal memory tokens in differentiable memory stack
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 通过 goal-directed recall 从 differentiable memory stack 中检索 disambiguating context，解决 perceptual aliasing 导致的非马尔可夫决策问题
- [Method]: ⟨SFT⟩（differentiable memory stack 与 policy 联合训练）
- [Mechanism]: 与基于 semantic compression + similarity retrieval 的传统方法不同，Chameleon 写入 geometry-grounded multimodal tokens（保留 fine-grained disambiguating perceptual cues）到 differentiable memory stack (Latent)。memory stack 支持 goal-directed recall：以当前任务目标为条件进行 differentiable retrieval，避免返回 perceptually similar but decision-irrelevant episodes。核心转化是从 raw embodied observations (Narrative, [embodied]) 到 geometry-preserving latent memory tokens (Latent, P3) 的 differentiable write + goal-directed read。

[Title]: Memo: Training Memory-Efficient Embodied Agents with Reinforcement Learning
- [Pathway]: Narrative → Latent (P3)
- [Source Experience]: Visual inputs and interaction history in memory-intensive long-horizon embodied RL tasks
- [Target Experience]: Periodic summarization tokens（compressed memory representations interleaved with inputs）
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 在 RL 训练和推理中以 compressed memory tokens 替代 full context，使 transformer policy 在 memory-intensive long-horizon 任务中保持 efficiency 和 robustness
- [Method]: ⟨RL⟩（RL training with interleaved periodic summarization）
- [Mechanism]: 训练过程中 periodic summarization tokens 被 interleave 到 input sequence 中，学会将过去的 visual inputs 和交互历史 (Narrative) 压缩为 compact memory representations (Latent, P3)。这些 summarization tokens 在后续步骤中被检索和利用，替代 naive long-context 方法。相比 full-context transformers，Memo 在 compute/storage 上更高效，并 generalize 到更长的 inference-time contexts 和 streaming settings。

[Title]: EpiCache: Episodic KV Cache Management for Long Conversational Question Answering
- [Pathway]: Out of Scope
- [Mechanism]: 通过 block-wise prefill 限制 KV cache 峰值增长，episodic KV compression 将对话历史聚类为 coherent episodes 并进行 episode-specific eviction。源端为 long conversation history，属于 conversational QA 的 KV cache 管理效率优化。非 agent 决策经验转化（无 (c,a,o,f) 决策闭环）。不满足 §3.1 纳入标准。

[Title]: ELMUR: External Layer Memory with Update/Rewrite for Long-Horizon RL
- [Pathway]: Narrative → Latent (P3)
- [Source Experience]: Long-horizon interaction history under partial observability（sparse reward manipulation, visual observations）
- [Target Experience]: Layer-local external memory embeddings（per-layer, updated via LRU with replacement or convex blending）
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: 在各 transformer layer 中通过 bidirectional cross-attention 与 memory embeddings 交互，为 partially observable long-horizon 决策提供 structured external memory
- [Method]: ⟨RL⟩（RL training with structured external memory architecture）
- [Mechanism]: 每层 transformer 维护 external memory embeddings。推理时通过 bidirectional cross-attention 与 memory 交互，memory 通过 LRU module 以 replacement 或 convex blending 方式更新。核心转化：long-horizon interaction history (Narrative, [embodied]) 通过 layer-wise cross-attention + LRU update 被逐步 consolidate 到 per-layer memory embeddings (Latent, P3)。有效 horizon 可扩展至 attention window 的 100,000 倍。与 global memory 方案不同，layer-local 设计使 memory 结构化地分布在各 abstraction level。

[Title]: Locas: Your Models are Principled Initializers of Locally-Supported Parametric Memories
- [Pathway]: Out of Scope
- [Mechanism]: 将 past context 通过 low-rank sideway-FFN-style memory (Locas) 存储为 parametric memory，可 flexibly offload 或 merge 进 model parameters。源端为 long text/dialogue context（PG-19 language modeling, LoCoMo dialogue QA），属于 continual learning 与 parametric context storage 技术。非 agent 决策经验转化。不满足 §3.1 纳入标准。


## Summary

- Total papers parsed: 71
- In-scope (annotated with Pathway): 30
- Out of Scope: 41
- Annotation Failures: 0
- Parser Errors: 0

### In-Scope Pathway Distribution

| Pathway | Count | Paper Indices |
|---------|-------|--------------|
| P3 (Narrative → Latent) | 23 | #1, #2, #4, #5, #6, #8, #9, #11, #15, #19, #20, #22, #26, #27, #29, #36, #38, #39, #42, #66, #67, #68, #70 |
| P3 (systems contribution) | 1 | #63 |
| P2 + P3 (multi-target, §8.8) | 3 | #21, #25, #61 |
| P7 + P1 composite (prompt-level self-improvement) | 1 | #54 |
| P1 + P5 composite (§8.3) | 1 | #31 |
| P5 (Narrative → Policy) | 1 | #49 |

### Out-of-Scope Categories

- **静态语料 / 上下文压缩**（无决策过程语义）：#3, #10, #12, #13, #14, #16, #17, #18, #23, #24, #28, #30, #32, #33, #34, #35, #41, #43, #44, #45, #46, #47, #48, #50, #51, #52, #53, #56, #57, #58, #59, #60, #62, #64, #65, #69, #71 — 共 37 篇
- **Memory architecture / retrieval 设计**（非跨载体经验转化）：#7（3DLLM-Mem，attention-based feature fusion within Latent space）
- **通用语言模型架构 / 非 agent 系统**：2 篇
  - #30 Memorizing Transformers（通用 LM kNN memory 增强）
  - #55 LatentMAS（多智能体 latent 通信协议，静态推理任务）
- **LLM 间通信协议**：#40 Cache-to-Cache

### Key Observations

1. **P3 占据绝对主导**：30 篇 in-scope 论文中 27 篇（90%）涉及 Narrative → Latent 转化（含 multi-target 和 systems 贡献），反映当前文献将 Latent memory（KV cache、continuous embeddings、soft prompts 等）作为核心经验载体。
2. **多篇论文本质是 context compression 而非 experience transformation**：41 篇 Out of Scope 论文中绝大部分属于通用 LLM 上下文压缩 / 视频理解 memory 架构，缺乏 agent 决策过程的 (c,a,o,f) 语义闭环。这些工作技术上与 P3 论文有交集（都涉及 token → latent compression），但在 Scope 定义下不属于 experience transformation。
3. **Embodied / VLA 记忆系统是 P3 的主要应用场景**：In-scope P3 论文中约一半（#8, #9, #22, #25, #26, #29, #36, #38, #39, #42, #66, #67, #68, #70）明确针对 robotic manipulation / embodied navigation，说明 VLA 领域对 temporal memory 的需求正快速推动 Latent carrier 的研究。
4. **复合路径与 P1/P5/P7 在 Section 4 文献中占比极低**：#31（P1+P5 composite, §8.3）、#54（P7+P1 composite, prompt-level self-improvement）、#49（P5）涉及非 P3 路径。P4/P6 在此批次中未出现。这一分布与 Section 4 的文献检索范围（侧重 memory systems）一致——memory 工作自然偏向 Tokenized → Latent 的压缩转化，而非 evaluator training 或 parametric 转化。
5. **Combee (#54) 是本批次中唯一涉及 P7 的论文**：agent policy 外化 execution traces (P7) + prompt learning 优化为 system prompts (P1)，形成 prompt-level self-improvement loop。与 weight-level §8.1 loop 的关键区别：闭环在 Narrative 层（通过 system prompt）而非 Parametric 层（无 weight update），是一个值得在 Composite Pipelines Section 讨论的变体。

## New Tags Introduced
- ⟨RL⟩ —— 通用强化学习标签，用于 abstract 仅表述为 "reinforcement learning" 而未指定具体变体（如 PPO/GRPO/DPO/ReST）的论文。首次出现：「MEM1」（#6）；后续用于 #15 (LatentMem/LMPO), #49 (Dejavu), #68 (Memo), #70 (ELMUR)

## Annotation Failures
（无）

## Parser Errors
（无）
