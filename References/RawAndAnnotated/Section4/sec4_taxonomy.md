
排除单纯压缩的，只保留有复用的。





直接提取

- Log-Augmented Generation：LAG 选择性地存储部分 tokens 的 KV caches 作为 past reasoning 的 latent 表示。新任务到来时，检索 relevant logs 的 KV values，直接注入当前 forward pass 以 augment generation。
- TempoFit：利用 VLA forward pass 自然产生的 prefix attention KV caches 作为 model-native content-addressable runtime state。在每个 timestep，将选定中间层的 prefix KV 按 FIFO 存储在 layer-wise memory 中。推理时通过 parameter-free K-to-K retrieval + Frame-Gap Temporal Bias（FGTB, fixed recency bias）检索相关 past KV，以 pre-attention residual loading + norm-preserving rescaling 注入当前 forward pass。完全 training-free
- Memorizing Transformers：通过 approximate kNN lookup 在 non-differentiable memory 中存储和检索 past inputs 的 internal representations（key-value pairs），增强语言模型的推理时记忆能力。



论文：
- Log-Augmented Generation: Scaling Test-Time Reasoning with Reusable Computation
- TempoFit: Plug-and-Play Layer-Wise Temporal KV Memory for Long-Horizon Vision-Language-Action Manipulation
- Memorizing Transformers


通过 prefix-Tuning 的方式，学习一个 learnable soft prompt

- MAP-VLA：第一阶段（memory construction）：从 historical human demonstrations 中按 task stage 切分 trajectory 片段，每段通过 prompt tuning 优化为 learnable soft prompt（Latent carrier），形成 memory library；soft prompt 的训练目标是最小化基于该 stage context 的 action prediction error。第二阶段（inference）：实时执行时通过 trajectory similarity matching 检索最相关的 stage memory soft prompts，将其拼接到 frozen VLA 的输入层以 augment action generation。
- 使用 Prefix Tuning 将 task demonstrations 蒸馏为 fixed KV cache，使 LLM 在不更新权重的情况下学习推理。
- TokMem：将 reusable task procedure 编译为单一 trainable memory token（Latent），用于控制 LLM 行为。


论文：
- MAP-VLA: Memory-Augmented Prompting for Vision-Language-Action Model in Robotic Manipulation
- ReasonCACHE: Teaching LLMs To Reason Without Weight Updates
- TokMem: One-Token Procedural Memory for Large Language Models


训练一个额外的模块，基于检索的文本和agent-specific context，生成 latent
- LatentMem：两阶段架构：experience bank 以 lightweight form 存储 raw interaction trajectories（Narrative）；memory composer 以 retrieved experience + agent-specific context 为条件，合成 compact latent memories（Latent）。核心训练机制为 Latent Memory Policy Optimization (LMPO)：将 task-level optimization signals 通过 latent memories 反向传播到 composer，鼓励其产生 compact 且 high-utility 的 latent representations。


论文
- LatentMem: Customizing Latent Memory for Multi-Agent Systems


没有中间隐藏层的
- MemoryVLA：Pretrained VLM 将 observation 编码为 perceptual + cognitive tokens 构成 working memory；working memory 的内容经 consolidation（合并冗余信息）后存入 Perceptual-Cognitive Memory Bank，后者分离存储 low-level details 与 high-level semantics。推理时 working memory 从 bank 检索 decision-relevant entries 并自适应融合，conditioning diffusion action expert 输出时序感知的动作序列。整个 memory consolidation 与 retrieval 机制通过训练获得（memory-conditioned diffusion action head），将 raw interaction history 逐步 consolidate 为结构化的 latent memory bank
- Dual Latent Memory：将 visual MAS 中的 perception 和 thinking 解耦，分别动态合成为 dual latent memories。entropy-driven proactive triggering 机制根据信息熵主动触发 on-demand memory access，替代传统的被动文本信息传递。核心动机是避免将 perceptual / thinking trajectories 转换为离散自然语言时的 semantic loss，直接在 latent space 进行 inter-agent memory 共享。
- Hybrid Self-evolving Structured Memory for GUI Agents：从 GUI agent 的交互轨迹同时构建两类载体：(1) 离散的高层 symbolic graph nodes（Schematic, P2），组织为 graph structure 以支持 multi-hop 检索与 node-level self-evolution；(2) continuous trajectory embeddings（Latent, P3），捕捉细粒度轨迹信息。
- EchoVLA：从 mobile manipulation 交互中同时构建两类并列 memory：(1) Scene memory（Schematic, P2）维护 spatial-semantic maps 的 collection，提供空间定位与导航上下文；(2) Episodic memory（Latent, P3）存储 task-level experiences with multimodal contextual features。两种 memory 独立存储、更新与检索，其 representations 通过 coarse- and fine-grained attention 融合后 conditioning diffusion action policies。


论文：
- MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation
- Dual Latent Memory for Visual Multi-agent System
- Hybrid Self-evolving Structured Memory for GUI Agents
- EchoVLA: Synergistic Declarative Memory for VLA-Driven Mobile Manipulation



待定：
- MEM1: Learning to Synergize Memory and Reasoning for Efficient Long-Horizon Agents
- HAMLET: Switch your Vision-Language-Action Model into a History-Aware Policy
- Chameleon: Episodic Memory for Long-Horizon Robotic Manipulation
- Gated Memory Policy