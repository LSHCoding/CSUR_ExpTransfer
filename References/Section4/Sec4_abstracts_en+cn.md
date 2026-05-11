Title: Auto-scaling Continuous Memory for GUI Agent

URL: https://doi.org/10.48550/arXiv.2510.09038

Abstract: We study how to endow GUI agents with scalable memory that help generalize across unfamiliar interfaces and long-horizon tasks. Prior GUI agents compress past trajectories into text tokens, which balloons context length and misses decisive visual cues (e.g., exact widget size and position). We propose a continuous memory that encodes each GUI trajectory into a fixed-length sequence of continuous embeddings using the VLM itself as an encoder; these embeddings are plugged directly into the backbone's input layer, sharply reducing context cost while preserving fine-grained visual information. As memory size and retrieval depth increase, performance improves monotonically, unlike text memories that degrade with long prompts. To grow memory at low cost, we introduce an auto-scaling data flywheel that (i) discovers new environments via search, (ii) synthesizes tasks with an open-source VLM, (iii) rolls out trajectories with the agent, and (iv) verifies success with the same VLM. Using this pipeline, we collect 100k+ trajectories for about \$4000 and fine-tune only the memory encoder (LoRA on a Q-Former, 1.2\% parameters) with 1,500 samples. On real-world GUI benchmarks, our memory-augmented agent consistently improves success rates under long horizons and distribution shifts. Notably, Qwen-2.5-VL-7B + continuous memory achieves performance comparable to state-of-the-art closed-source models (e.g., GPT-4o, Claude-4).

中文翻译：本文研究如何为 GUI agent 赋予可扩展的记忆能力，使其能够泛化到不熟悉的界面和长 horizon 任务。现有 GUI agent 将过去轨迹压缩为文本 token，导致上下文长度膨胀且丢失关键视觉线索（如控件精确尺寸和位置）。我们提出一种连续记忆机制，利用 VLM 自身作为编码器，将每条 GUI 轨迹编码为固定长度的连续嵌入序列；这些嵌入直接接入骨干网络的输入层，在大幅降低上下文开销的同时保留细粒度视觉信息。随着记忆容量和检索深度的增加，性能单调提升，与文本记忆在长提示下退化形成对比。为了低成本扩展记忆，我们引入自动扩展的数据飞轮：(i) 通过搜索发现新环境，(ii) 用开源 VLM 合成任务，(iii) 用 agent 执行轨迹，(iv) 用同一 VLM 验证成功。通过该流水线，我们以约 4000 美元收集了 10 万+ 条轨迹，仅用 1500 样本微调记忆编码器（在 Q-Former 上做 LoRA，1.2% 参数）。在真实 GUI 基准上，记忆增强的 agent 在长 horizon 和分布偏移下持续提升成功率。Qwen-2.5-VL-7B + 连续记忆达到了与最先进闭源模型（如 GPT-4o、Claude-4）相当的性能。

------

Title: Log-Augmented Generation: Scaling Test-Time Reasoning with Reusable Computation

URL: https://doi.org/10.48550/arXiv.2505.14398

Abstract: While humans naturally learn and adapt from past experiences, large language models (LLMs) and their agentic counterparts struggle to retain reasoning from previous tasks and apply them in future contexts. To address this limitation, we propose a novel framework, log-augmented generation (LAG) that directly reuses prior computation and reasoning from past logs at test time to enhance model's ability to learn from previous tasks and perform better on new, unseen challenges, all while keeping the system efficient and scalable. Specifically, our system represents task logs using key-value (KV) caches, encoding the full reasoning context of prior tasks while storing KV caches for only a selected subset of tokens. When a new task arises, LAG retrieves the KV values from relevant logs to augment generation. Our approach differs from reflection-based memory mechanisms by directly reusing prior reasoning and computations without requiring additional steps for knowledge extraction or distillation. Our method also goes beyond existing KV caching techniques, which primarily target efficiency gains rather than improving accuracy. Experiments on knowledge- and reasoning-intensive datasets demonstrate that our method significantly outperforms standard agentic systems that do not utilize logs, as well as existing solutions based on reflection and KV cache techniques.

中文翻译：人类能够自然地从过去经验中学习和适应，但大语言模型（LLM）及其 agent 形态在保留先前任务的推理并将其应用于未来上下文方面存在困难。为解决这一局限，我们提出 Log-Augmented Generation（LAG），一种在测试时直接复用先前日志中的计算和推理来增强模型学习能力并提升在新任务上表现的框架，同时保持系统高效且可扩展。具体而言，系统使用 KV cache 表示任务日志，编码先前任务的完整推理上下文，同时仅存储选定 token 子集的 KV cache。当新任务到来时，LAG 从相关日志中检索 KV 值以增强生成。该方法与基于反思的记忆机制不同之处在于直接复用先前的推理和计算，无需额外的知识提取或蒸馏步骤。该方法也超越了现有的 KV cache 技术——后者主要面向效率提升而非精度改进。在知识密集和推理密集型数据集上的实验表明，该方法显著优于不使用日志的标准 agent 系统以及基于反思和 KV cache 的现有方案。

------

Title: Cartridges: Lightweight and general-purpose long context representations via self-study

URL: https://doi.org/10.48550/arXiv.2506.06266

Abstract: Large language models are often used to answer queries grounded in large text corpora (e.g. codebases, legal documents, or chat histories) by placing the entire corpus in the context window and leveraging in-context learning (ICL). Although current models support contexts of 100K-1M tokens, this setup is costly to serve because the memory consumption of the KV cache scales with input length. We explore an alternative: training a smaller KV cache offline on each corpus. At inference time, we load this trained KV cache, which we call a Cartridge, and decode a response. Critically, the cost of training a Cartridge can be amortized across all the queries referencing the same corpus. However, we find that the naive approach of training the Cartridge with next-token prediction on the corpus is not competitive with ICL. Instead, we propose self-study, a training recipe in which we generate synthetic conversations about the corpus and train the Cartridge with a context-distillation objective. We find that Cartridges trained with self-study replicate the functionality of ICL, while being significantly cheaper to serve. On challenging long-context benchmarks, Cartridges trained with self-study match ICL performance while using 38.6x less memory and enabling 26.4x higher throughput. Self-study also extends the model's effective context length (e.g. from 128k to 484k tokens on MTOB) and surprisingly, leads to Cartridges that can be composed at inference time without retraining.

中文翻译：大语言模型常被用于回答基于大型文本语料（如代码库、法律文档或聊天记录）的查询，方法是将整个语料放入上下文窗口并利用上下文学习（ICL）。尽管当前模型支持 100K-1M token 的上下文，但这种设置服务成本高昂，因为 KV cache 的内存消耗随输入长度线性增长。我们探索了一种替代方案：离线为每个语料训练一个更小的 KV cache。推理时加载这个训练好的 KV cache（称为 Cartridge）并解码响应。关键是，训练 Cartridge 的成本可以在引用同一语料的所有查询中摊销。然而，我们发现单纯用语料上的下一 token 预测来训练 Cartridge 无法与 ICL 竞争。为此，我们提出 self-study——一种生成关于语料的合成对话并用上下文蒸馏目标训练 Cartridge 的训练方法。通过 self-study 训练的 Cartridge 复现了 ICL 的功能，同时服务成本显著更低。在具有挑战性的长上下文基准上，self-study 训练的 Cartridge 在内存减少 38.6 倍、吞吐量提升 26.4 倍的情况下匹配 ICL 性能。Self-study 还扩展了模型的有效上下文长度（如在 MTOB 上从 128K 扩展到 484K token），并且出人意料地，Cartridge 可以在推理时组合而无需重新训练。

------

Title: FlashMem: Distilling Intrinsic Latent Memory via Computation Reuse

URL: https://doi.org/10.48550/arXiv.2601.05505

Abstract: The stateless architecture of Large Language Models inherently lacks the mechanism to preserve dynamic context, compelling agents to redundantly reprocess history to maintain long-horizon autonomy. While latent memory offers a solution, current approaches are hindered by architectural segregation, relying on auxiliary encoders that decouple memory from the reasoning backbone. We propose FlashMem, a framework that distills intrinsic memory directly from transient reasoning states via computation reuse. Leveraging the property that internal representations uniquely encode input trajectories, FlashMem identifies the last hidden state as a sufficient statistic for the interaction history. This enables a Shared-KV Consolidator to synthesize memory by attending directly to the backbone's frozen cache, eliminating redundant re-parameterization. Furthermore, a parameter-free Cognitive Monitor leverages attention entropy to adaptively trigger consolidation only when high epistemic uncertainty is detected. Experiments demonstrate that FlashMem matches the performance of heavy baselines while reducing inference latency by 5 times, effectively bridging the gap between efficiency and persistent cognition.

中文翻译：大语言模型的无状态架构本质上缺乏保持动态上下文的机制，迫使 agent 冗余重复处理历史以维持长 horizon 自主性。虽然隐式记忆提供了一种解决方案，但当前方法受限于架构隔离——依赖辅助编码器将记忆与推理骨干解耦。我们提出 FlashMem，一种通过计算复用从瞬态推理状态中直接蒸馏内在记忆的框架。利用内部表示唯一编码输入轨迹的性质，FlashMem 将最后一个隐藏状态识别为交互历史的充分统计量。这使得共享 KV 整合器能够通过直接关注骨干网络的冻结缓存来合成记忆，消除了冗余的重参数化。此外，一个无参数的认知监视器利用注意力熵自适应地在检测到高认知不确定性时触发整合。实验表明，FlashMem 在匹配重量级基线性能的同时将推理延迟降低 5 倍，有效弥合了效率与持续认知之间的鸿沟。

------

Title: MemGen: Weaving Generative Latent Memory for Self-Evolving Agents

URL: https://doi.org/10.48550/arXiv.2509.24704

Abstract: Agent memory shapes how Large Language Model (LLM)-powered agents, akin to the human brain, progressively refine themselves through environment interactions. Existing paradigms remain constrained: parametric memory forcibly adjusts model parameters, and retrieval-based memory externalizes experience into structured databases, yet neither captures the fluid interweaving of reasoning and memory that underlies human cognition. To address this gap, we propose MemGen, a dynamic generative memory framework that equips agents with a human-esque cognitive faculty. It consists of a \textit{memory trigger}, which monitors the agent's reasoning state to decide explicit memory invocation, and a \textit{memory weaver}, which takes the agent's current state as stimulus to construct a latent token sequence as machine-native memory to enrich its reasoning. In this way, MemGen enables agents to recall and augment latent memory throughout reasoning, producing a tightly interwoven cycle of memory and cognition. Extensive experiments across eight benchmarks show that MemGen surpasses leading external memory systems such as ExpeL and AWM by up to $38.22\%$, exceeds GRPO by up to $13.44\%$, and exhibits strong cross-domain generalization ability. More importantly, we find that without explicit supervision, MemGen spontaneously evolves distinct human-like memory faculties, including planning memory, procedural memory, and working memory, suggesting an emergent trajectory toward more naturalistic forms of machine cognition.

中文翻译：Agent 记忆塑造了 LLM agent 类似人脑那样通过环境交互逐步自我精炼的方式。现有范式仍存在局限：参数化记忆强制调整模型参数，检索式记忆将经验外化为结构化数据库，但两者都无法捕捉人类认知中推理与记忆的流动交织。为解决这一鸿沟，我们提出 MemGen，一种动态生成式记忆框架，为 agent 赋予类人的认知能力。它包含一个记忆触发器，监控 agent 的推理状态以决定是否显式调用记忆；以及一个记忆编织器，以 agent 当前状态为刺激，构建隐式 token 序列作为机器原生记忆以丰富其推理。通过这种方式，MemGen 使 agent 能够在推理过程中回忆和增强隐式记忆，形成记忆与认知紧密交织的循环。在八个基准上的大量实验表明，MemGen 超越 ExpeL 和 AWM 等领先外部记忆系统多达 38.22%，超过 GRPO 多达 13.44%，并展现出强大的跨域泛化能力。更重要的是，我们发现在没有显式监督的情况下，MemGen 自发演化出不同的人类记忆能力，包括规划记忆、程序性记忆和工作记忆，暗示着向更自然的机器认知形式的涌现轨迹。

------

Title: MEM1: Learning to Synergize Memory and Reasoning for Efficient Long-Horizon Agents

URL: https://doi.org/10.48550/arXiv.2506.15841

Abstract: Modern language agents must operate over long-horizon, multi-turn interactions, where they retrieve external information, adapt to observations, and answer interdependent queries. Yet, most LLM systems rely on full-context prompting, appending all past turns regardless of their relevance. This leads to unbounded memory growth, increased computational costs, and degraded reasoning performance on out-of-distribution input lengths. We introduce MEM1, an end-to-end reinforcement learning framework that enables agents to operate with constant memory across long multi-turn tasks. At each turn, MEM1 updates a compact shared internal state that jointly supports memory consolidation and reasoning. This state integrates prior memory with new observations from the environment while strategically discarding irrelevant or redundant information. To support training in more realistic and compositional settings, we propose a simple yet effective and scalable approach to constructing multi-turn environments by composing existing datasets into arbitrarily complex task sequences. Experiments across three domains, including internal retrieval QA, open-domain web QA, and multi-turn web shopping, show that MEM1-7B improves performance by 3.5x while reducing memory usage by 3.7x compared to Qwen2.5-14B-Instruct on a 16-objective multi-hop QA task, and generalizes beyond the training horizon. Our results demonstrate the promise of reasoning-driven memory consolidation as a scalable alternative to existing solutions for training long-horizon interactive agents, where both efficiency and performance are optimized.

中文翻译：现代语言 agent 必须运行在长 horizon、多轮交互中，需要检索外部信息、适应观察结果并回答相互依赖的查询。然而，大多数 LLM 系统依赖全上下文提示，将所有历史轮次追加而不考虑相关性。这导致无界的内存增长、增加的计算成本以及在分布外输入长度上退化的推理性能。我们引入 MEM1，一种端到端强化学习框架，使 agent 能够以恒定内存在长多轮任务中运行。每轮 MEM1 更新一个紧凑的共享内部状态，同时支持记忆整合与推理。该状态将先前记忆与环境新观察整合，同时策略性地丢弃无关或冗余信息。为支持在更真实和组合性设置下的训练，我们提出一种简单有效且可扩展的方法，通过组合现有数据集构建任意复杂任务序列的多轮环境。跨三个领域（内部检索 QA、开放域 Web QA 和多轮 Web 购物）的实验表明，MEM1-7B 在 16 目标多跳 QA 任务上比 Qwen2.5-14B-Instruct 性能提升 3.5 倍，同时内存使用减少 3.7 倍，并能泛化到训练 horizon 之外。

------

Title: 3DLLM-Mem: Long-Term Spatial-Temporal Memory for Embodied 3D Large Language Model

URL: https://doi.org/10.48550/arXiv.2505.22657

Abstract: Humans excel at performing complex tasks by leveraging long-term memory across temporal and spatial experiences. In contrast, current Large Language Models (LLMs) struggle to effectively plan and act in dynamic, multi-room 3D environments. We posit that part of this limitation is due to the lack of proper 3D spatial-temporal memory modeling in LLMs. To address this, we first introduce 3DMem-Bench, a comprehensive benchmark comprising over 26,000 trajectories and 2,892 embodied tasks, question-answering and captioning, designed to evaluate an agent's ability to reason over long-term memory in 3D environments. Second, we propose 3DLLM-Mem, a novel dynamic memory management and fusion model for embodied spatial-temporal reasoning and actions in LLMs. Our model uses working memory tokens, which represents current observations, as queries to selectively attend to and fuse the most useful spatial and temporal features from episodic memory, which stores past observations and interactions. Our approach allows the agent to focus on task-relevant information while maintaining memory efficiency in complex, long-horizon environments. Experimental results demonstrate that 3DLLM-Mem achieves state-of-the-art performance across various tasks, outperforming the strongest baselines by 16.5% in success rate on 3DMem-Bench's most challenging in-the-wild embodied tasks.

中文翻译：人类擅长通过利用跨时间和空间的长期记忆来执行复杂任务。相比之下，当前大语言模型（LLM）难以在动态、多房间 3D 环境中有效规划和行动。我们认为这一局限部分源于 LLM 缺乏适当的 3D 时空记忆建模。为此，我们首先引入 3DMem-Bench，一个包含超过 26000 条轨迹和 2892 个具身任务（包括问答和描述）的综合基准，旨在评估 agent 在 3D 环境中基于长期记忆进行推理的能力。其次，我们提出 3DLLM-Mem，一种用于 LLM 中具身时空推理和行动的新型动态记忆管理与融合模型。该模型使用工作记忆 token（表示当前观察）作为查询，选择性地关注和融合来自情节记忆（存储过去观察和交互）中最有用的时空特征。该方法使 agent 能够在复杂、长 horizon 环境中专注于任务相关信息的同时保持记忆效率。实验结果表明，3DLLM-Mem 在各项任务上达到了最先进性能，在 3DMem-Bench 最具挑战性的真实具身任务上成功率超越最强基线 16.5%。

------

Title: MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation

URL: https://doi.org/10.48550/arXiv.2508.19236

Abstract: Temporal context is essential for robotic manipulation because such tasks are inherently non-Markovian, yet mainstream VLA models typically overlook it and struggle with long-horizon, temporally dependent tasks. Cognitive science suggests that humans rely on working memory to buffer short-lived representations for immediate control, while the hippocampal system preserves verbatim episodic details and semantic gist of past experience for long-term memory. Inspired by these mechanisms, we propose MemoryVLA, a Cognition-Memory-Action framework for long-horizon robotic manipulation. A pretrained VLM encodes the observation into perceptual and cognitive tokens that form working memory, while a Perceptual-Cognitive Memory Bank stores low-level details and high-level semantics consolidated from it. Working memory retrieves decision-relevant entries from the bank, adaptively fuses them with current tokens, and updates the bank by merging redundancies. Using these tokens, a memory-conditioned diffusion action expert yields temporally aware action sequences. We evaluate MemoryVLA on 150+ simulation and real-world tasks across three robots. On SimplerEnv-Bridge, Fractal, LIBERO-5 suites and Mikasa-Robo, it achieves 71.9%, 72.7%, 96.5%, and 41.2% success rates, respectively, all outperforming state-of-the-art baselines CogACT and pi-0, with a notable +14.6 gain on Bridge and +11.8 gain on Mikasa-Robo. On 12 real-world tasks spanning general skills and long-horizon temporal dependencies, MemoryVLA achieves 84.0% success rate, with long-horizon tasks showing a +26 improvement over state-of-the-art baseline. Project Page: https://shihao1895.github.io/MemoryVLA

中文翻译：时间上下文对机器人操作至关重要，因为此类任务本质上是非马尔科夫的，但主流 VLA 模型通常忽略这一点，难以处理长 horizon、时间依赖的任务。认知科学表明，人类依赖工作记忆缓冲短暂表征用于即时控制，而海马系统则保留精确的情节细节和过去经验的语义要旨用于长期记忆。受这些机制启发，我们提出 MemoryVLA，一种面向长 horizon 机器人操作的"认知-记忆-行动"框架。预训练的 VLM 将观察编码为形成工作记忆的感知和认知 token，而感知-认知记忆库则存储由工作记忆整合而来的低级细节和高级语义。工作记忆从记忆库中检索决策相关条目，自适应地将其与当前 token 融合，并通过合并冗余来更新记忆库。利用这些 token，一个记忆条件的扩散动作专家生成具有时间感知的动作序列。我们在三台机器人上评估了 MemoryVLA 在 150+ 仿真和真实任务上的表现。在 SimplerEnv-Bridge、Fractal、LIBERO-5 套件和 Mikasa-Robo 上分别达到 71.9%、72.7%、96.5% 和 41.2% 成功率，均超越最先进基线 CogACT 和 π0，其中 Bridge 提升 +14.6，Mikasa-Robo 提升 +11.8。在 12 个涵盖通用技能和长 horizon 时间依赖的真实任务上，MemoryVLA 达到 84.0% 成功率，长 horizon 任务比最先进基线提升 +26。

------

Title: MAP-VLA: Memory-Augmented Prompting for Vision-Language-Action Model in Robotic Manipulation

URL: https://doi.org/10.48550/arXiv.2511.09516

Abstract: Pre-trained Vision-Language-Action (VLA) models have achieved remarkable success in improving robustness and generalization for end-to-end robotic manipulation. However, these models struggle with long-horizon tasks due to their lack of memory and reliance solely on immediate sensory inputs. To address this limitation, we propose Memory-Augmented Prompting for Vision-Language-Action model (MAP-VLA), a novel framework that empowers pre-trained VLA models with demonstration-derived memory prompts to augment action generation for long-horizon robotic manipulation tasks. To achieve this, MAP-VLA first constructs a memory library from historical demonstrations, where each memory unit captures information about a specific stage of a task. These memory units are implemented as learnable soft prompts optimized through prompt tuning. Then, during real-time task execution, MAP-VLA retrieves relevant memory through trajectory similarity matching and dynamically integrates it into the VLA model for augmented action generation. Importantly, this prompt tuning and retrieval augmentation approach operates as a plug-and-play module for a frozen VLA model, offering a lightweight and flexible solution to improve task performance. Experimental results show that MAP-VLA delivers up to 7.0% absolute performance gains in the simulation benchmark and 25.0% on real robot evaluations for long-horizon tasks, surpassing the current state-of-the-art methods.

中文翻译：预训练的视觉-语言-动作（VLA）模型在端到端机器人操作的鲁棒性和泛化方面取得了显著成功。然而，这些模型难以处理长 horizon 任务，因为缺乏记忆且仅依赖即时感官输入。为此，我们提出 MAP-VLA（Memory-Augmented Prompting for VLA），一种用演示派生的记忆提示来增强预训练 VLA 模型以支持长 horizon 机器人操作任务的新框架。MAP-VLA 首先从历史演示中构建记忆库，每个记忆单元捕获任务特定阶段的信息。这些记忆单元实现为通过提示微调优化的可学习软提示。在实时任务执行期间，MAP-VLA 通过轨迹相似度匹配检索相关记忆，并将其动态集成到 VLA 模型中以增强动作生成。该提示微调和检索增强方法作为冻结 VLA 模型的即插即用模块运行，提供了轻量灵活的方案来提升任务性能。实验结果表明，MAP-VLA 在仿真基准中实现高达 7.0% 的绝对性能提升，在长 horizon 任务的真实机器人评估中提升 25.0%，超越当前最先进方法。

------

Title: Towards General Continuous Memory for Vision-Language Models

URL: https://doi.org/10.48550/arXiv.2505.17670

Abstract: Language models (LMs) and their extension, vision-language models (VLMs), have achieved remarkable performance across various tasks. However, they still struggle with complex reasoning tasks that require multimodal or multilingual real-world knowledge. To support such capabilities, an external memory system that can efficiently provide relevant multimodal information is essential. Existing approaches generally concatenate image and text tokens into a long sequence as memory, which, however, may drastically increase context length and even degrade performance. In contrast, we propose using continuous memory, a compact set of dense embeddings to more effectively and efficiently represent multimodal and multilingual knowledge. Our key insight is that a VLM can serve as its own continuous memory encoder. We empirically show that this design improves performance on complex multimodal reasoning tasks. Building on this, we introduce a data-efficient and parameter-efficient method to fine-tune the VLM into a memory encoder, requiring only 1.2% of the model's parameters and a small corpus of 15.6K self-synthesized samples. Our approach CoMEM utilizes VLM's original capabilities to encode arbitrary multimodal and multilingual knowledge into just 8 continuous embeddings. Since the inference-time VLM remains frozen, our memory module is plug-and-play and can be flexibly integrated as needed. Extensive experiments across eight multimodal reasoning benchmarks demonstrate the effectiveness of our approach.

中文翻译：语言模型（LM）及其扩展视觉-语言模型（VLM）在各项任务上取得了显著性能。然而，它们在需要多模态或多语言真实世界知识的复杂推理任务上仍存在困难。为支持此类能力，一个能高效提供相关多模态信息的外部记忆系统至关重要。现有方法通常将图像和文本 token 连接为长序列作为记忆，但这可能急剧增加上下文长度甚至降低性能。相比之下，我们提出使用连续记忆——一组紧凑的稠密嵌入来更有效高效地表示多模态和多语言知识。我们的核心洞察是 VLM 可以作为自身的连续记忆编码器。我们经验性地表明，该设计提升了复杂多模态推理任务的性能。在此基础上，我们引入一种数据高效且参数高效的方法将 VLM 微调为记忆编码器，仅需模型 1.2% 的参数和 15.6K 自合成样本的小型语料库。我们的方法 CoMEM 利用 VLM 的原始能力将任意多模态和多语言知识编码为仅 8 个连续嵌入。由于推理时 VLM 保持冻结，记忆模块是即插即用的，可根据需要灵活集成。在八个多模态推理基准上的广泛实验证明了方法的有效性。

------

Title: Dual Latent Memory for Visual Multi-agent System

URL: https://doi.org/10.48550/arXiv.2602.00471

Abstract: While Visual Multi-Agent Systems (VMAS) promise to enhance comprehensive abilities through inter-agent collaboration, empirical evidence reveals a counter-intuitive"scaling wall": increasing agent turns often degrades performance while exponentially inflating token costs. We attribute this failure to the information bottleneck inherent in text-centric communication, where converting perceptual and thinking trajectories into discrete natural language inevitably induces semantic loss. To this end, we propose L$^{2}$-VMAS, a novel model-agnostic framework that enables inter-agent collaboration with dual latent memories. Furthermore, we decouple the perception and thinking while dynamically synthesizing dual latent memories. Additionally, we introduce an entropy-driven proactive triggering that replaces passive information transmission with efficient, on-demand memory access. Extensive experiments among backbones, sizes, and multi-agent structures demonstrate that our method effectively breaks the"scaling wall"with superb scalability, improving average accuracy by 2.7-5.4% while reducing token usage by 21.3-44.8%. Codes: https://github.com/YU-deep/L2-VMAS.

中文翻译：视觉多 agent 系统（VMAS）虽有望通过 agent 间协作增强综合能力，但实证证据揭示了一个反直觉的"扩展墙"：增加 agent 轮次往往降低性能，同时指数级膨胀 token 成本。我们将这一失败归因于以文本为中心的通信中固有的信息瓶颈——将感知和思维轨迹转换为离散自然语言不可避免地导致语义损失。为此，我们提出 L²-VMAS，一种模型无关的新框架，通过双隐式记忆实现 agent 间协作。我们解耦感知与思考，动态合成双隐式记忆。此外，我们引入熵驱动的主动触发机制，以高效的按需记忆访问替代被动信息传输。在不同骨干、规模和多种 agent 结构上的大量实验表明，该方法有效打破了"扩展墙"，具有卓越的可扩展性，平均准确率提升 2.7-5.4%，同时 token 使用量减少 21.3-44.8%。

------

Title: Latent Context Compilation: Distilling Long Context into Compact Portable Memory

URL: https://doi.org/10.48550/arXiv.2602.21221

Abstract: Efficient long-context LLM deployment is stalled by a dichotomy between amortized compression, which struggles with out-of-distribution generalization, and Test-Time Training, which incurs prohibitive synthetic data costs and requires modifying model weights, creating stateful parameters that complicate concurrent serving. We propose Latent Context Compilation, a framework that fundamentally shifts context processing from adaptation to compilation. By utilizing a disposable LoRA module as a compiler, we distill long contexts into compact buffer tokens -- stateless, portable memory artifacts that are plug-and-play compatible with frozen base models. Crucially, we introduce a self-aligned optimization strategy that eliminates the need for synthetic context-relevant QA pairs. By regularizing context reconstruction task with context-agnostic random queries, we force compressed tokens to reside within the model's existing instruction-following manifold. Experiments with Llama-3.1-8B demonstrate that Latent Context Compilation preserves fine-grained details and reasoning capabilities where prior methods falter, effectively decoupling memory density from model parameters even at a 16x compression ratio.

中文翻译：高效的长上下文 LLM 部署受困于一种二分法：摊销压缩难以处理分布外泛化，而测试时训练则产生难以承受的合成数据成本并需要修改模型权重，创建有状态参数使并发服务复杂化。我们提出 Latent Context Compilation，一种从根本上将上下文处理从适配转变为编译的框架。通过使用一次性 LoRA 模块作为编译器，我们将长上下文蒸馏为紧凑的缓冲 token——一种无状态、可移植的记忆构件，与冻结的基础模型即插即用兼容。关键的是，我们引入一种自对齐优化策略，消除了对合成上下文相关 QA 对的需求。通过用上下文无关的随机查询对上下文重建任务进行正则化，我们迫使压缩 token 驻留在模型现有的指令遵循流形中。使用 Llama-3.1-8B 的实验表明，Latent Context Compilation 在先前方法失败的地方保留了细粒度细节和推理能力，即使在 16 倍压缩比下也有效解耦了记忆密度与模型参数。

------

Title: In-context Autoencoder for Context Compression in a Large Language Model

URL: https://doi.org/10.48550/arXiv.2307.06945

Abstract: We propose the In-context Autoencoder (ICAE), leveraging the power of a large language model (LLM) to compress a long context into short compact memory slots that can be directly conditioned on by the LLM for various purposes. ICAE is first pretrained using both autoencoding and language modeling objectives on massive text data, enabling it to generate memory slots that accurately and comprehensively represent the original context. Then, it is fine-tuned on instruction data for producing desirable responses to various prompts. Experiments demonstrate that our lightweight ICAE, introducing about 1% additional parameters, effectively achieves $4\times$ context compression based on Llama, offering advantages in both improved latency and GPU memory cost during inference, and showing an interesting insight in memorization as well as potential for scalability. These promising results imply a novel perspective on the connection between working memory in cognitive science and representation learning in LLMs, revealing ICAE's significant implications in addressing the long context problem and suggesting further research in LLM context management. Our data, code and models are available at https://github.com/getao/icae.

中文翻译：我们提出上下文自编码器（ICAE），利用大语言模型（LLM）的能力将长上下文压缩为紧凑的记忆槽，LLM 可以直接以其为条件用于各种目的。ICAE 首先使用自编码和语言建模目标在大量文本数据上预训练，使其能够生成准确且全面表示原始上下文的记忆槽。然后在指令数据上微调，以对各种提示产生理想响应。实验表明，我们轻量的 ICAE（引入约 1% 额外参数）基于 Llama 有效实现了 4 倍上下文压缩，在推理延迟和 GPU 内存成本方面均具优势，并在记忆机制上展现有趣的洞见及可扩展性潜力。这些有希望的结果暗示了认知科学中的工作记忆与 LLM 中的表示学习之间的新联系，揭示了 ICAE 在解决长上下文问题上的重要意义，并为 LLM 上下文管理指出了进一步研究方向。

------

Title: Adapting Language Models to Compress Contexts

URL: https://doi.org/10.48550/arXiv.2305.14788

Abstract: Transformer-based language models (LMs) are powerful and widely-applicable tools, but their usefulness is constrained by a finite context window and the expensive computational cost of processing long text documents. We propose to adapt pre-trained LMs into AutoCompressors. These models are capable of compressing long contexts into compact summary vectors, which are then accessible to the model as soft prompts. Summary vectors are trained with an unsupervised objective, whereby long documents are processed in segments and summary vectors from all previous segments are used in language modeling. We fine-tune OPT models on sequences of up to 30,720 tokens and show that AutoCompressors can utilize long contexts to improve perplexity. We evaluate AutoCompressors on in-context learning by compressing task demonstrations. We find that summary vectors are good substitutes for plain-text demonstrations, increasing accuracy while reducing inference cost. Finally, we explore the benefits of pre-computing summary vectors for large corpora by applying summary vectors to retrieval-augmented language modeling. Overall, AutoCompressors emerge as a simple and inexpensive solution for extending the context window of LMs while speeding up inference over long contexts.

中文翻译：基于 Transformer 的语言模型（LM）是强大且应用广泛的工具，但其实用性受限于有限的上下文窗口和处理长文本的高昂计算成本。我们提出将预训练 LM 适配为 AutoCompressors。这些模型能够将长上下文压缩为紧凑的摘要向量，摘要向量作为软提示可供模型访问。摘要向量通过无监督目标训练，长文档分段处理，所有先前段的摘要向量用于语言建模。我们在最长 30720 token 的序列上微调 OPT 模型，表明 AutoCompressors 可以利用长上下文改善困惑度。我们通过压缩任务演示评估 AutoCompressors 在上下文学习上的表现，发现摘要向量是纯文本演示的良好替代，在提高准确率的同时降低推理成本。最后，我们探索了为大语料库预计算摘要向量的收益，将其应用于检索增强的语言建模。总体而言，AutoCompressors 成为扩展 LM 上下文窗口并加速长上下文推理的一种简单低成本的解决方案。

------

Title: LatentMem: Customizing Latent Memory for Multi-Agent Systems

URL: https://doi.org/10.48550/arXiv.2602.03036

Abstract: Large language model (LLM)-powered multi-agent systems (MAS) demonstrate remarkable collective intelligence, wherein multi-agent memory serves as a pivotal mechanism for continual adaptation. However, existing multi-agent memory designs remain constrained by two fundamental bottlenecks: (i) memory homogenization arising from the absence of role-aware customization, and (ii) information overload induced by excessively fine-grained memory entries. To address these limitations, we propose LatentMem, a learnable multi-agent memory framework designed to customize agent-specific memories in a token-efficient manner. Specifically, LatentMem comprises an experience bank that stores raw interaction trajectories in a lightweight form, and a memory composer that synthesizes compact latent memories conditioned on retrieved experience and agent-specific contexts. Further, we introduce Latent Memory Policy Optimization (LMPO), which propagates task-level optimization signals through latent memories to the composer, encouraging it to produce compact and high-utility representations. Extensive experiments across diverse benchmarks and mainstream MAS frameworks show that LatentMem achieves a performance gain of up to $19.36$% over vanilla settings and consistently outperforms existing memory architectures, without requiring any modifications to the underlying frameworks.

中文翻译：大语言模型（LLM）驱动的多 agent 系统（MAS）展现出显著的集体智能，其中多 agent 记忆作为持续适应的关键机制。然而，现有多 agent 记忆设计仍受限于两个根本瓶颈：(i) 因缺乏角色感知定制而产生的记忆同质化，以及 (ii) 过于细粒度的记忆条目导致的信息过载。为解决这些局限，我们提出 LatentMem，一种可学习的多 agent 记忆框架，旨在以 token 高效的方式定制 agent 专属记忆。具体而言，LatentMem 包含一个以轻量形式存储原始交互轨迹的经验库，以及一个以检索到的经验和 agent 特定上下文为条件合成紧凑隐式记忆的记忆编写器。此外，我们引入隐式记忆策略优化（LMPO），通过隐式记忆将任务级优化信号传播到编写器，促使其产生紧凑且高价值的表示。跨多种基准和主流 MAS 框架的大量实验表明，LatentMem 在原始设置上实现高达 19.36% 的性能提升，并在不修改底层框架的情况下始终优于现有记忆架构。

------

Title: ReasonCACHE: Teaching LLMs To Reason Without Weight Updates

URL: https://doi.org/10.48550/arXiv.2602.02366

Abstract: Can Large language models (LLMs) learn to reason without any weight update and only through in-context learning (ICL)? ICL is strikingly sample-efficient, often learning from only a handful of demonstrations, but complex reasoning tasks typically demand many training examples to learn from. However, naively scaling ICL by adding more demonstrations breaks down at this scale: attention costs grow quadratically, performance saturates or degrades with longer contexts, and the approach remains a shallow form of learning. Due to these limitations, practitioners predominantly rely on in-weight learning (IWL) to induce reasoning. In this work, we show that by using Prefix Tuning, LLMs can learn to reason without overloading the context window and without any weight updates. We introduce $\textbf{ReasonCACHE}$, an instantiation of this mechanism that distills demonstrations into a fixed key-value cache. Empirically, across challenging reasoning benchmarks, including GPQA-Diamond, ReasonCACHE outperforms standard ICL and matches or surpasses IWL approaches. Further, it achieves this all while being more efficient across three key axes: data, inference cost, and trainable parameters. We also theoretically prove that ReasonCACHE can be strictly more expressive than low-rank weight update since the latter ties expressivity to input rank, whereas ReasonCACHE bypasses this constraint by directly injecting key-values into the attention mechanism. Together, our findings identify ReasonCACHE as a middle path between in-context and in-weight learning, providing a scalable algorithm for learning reasoning skills beyond the context window without modifying parameters. Our project page: https://reasoncache.github.io/

中文翻译：大语言模型（LLM）能否在没有任何权重更新的情况下仅通过上下文学习（ICL）学会推理？ICL 样本效率惊人，通常仅从少量演示中学习，但复杂推理任务通常需要大量训练示例。然而，通过添加更多演示来简单扩展 ICL 在此规模下失效：注意力成本二次增长，性能在更长上下文中饱和甚至退化，且该方法仍是浅层学习。由于这些局限，实践者主要依赖权重学习（IWL）来诱导推理。本文中，我们展示通过使用 Prefix Tuning，LLM 可以在不过载上下文窗口且无权重更新的情况下学会推理。我们引入 ReasonCACHE，该机制将演示蒸馏为固定的键值缓存。在包括 GPQA-Diamond 在内的挑战性推理基准上，ReasonCACHE 优于标准 ICL，并匹配或超越 IWL 方法，同时在数据、推理成本和可训练参数三个关键轴上更加高效。我们还从理论上证明 ReasonCACHE 可以严格比低秩权重更新更具表达力，因为后者将表达力绑定于输入秩，而 ReasonCACHE 通过直接向注意力机制注入键值绕过了这一限制。这些发现共同确立了 ReasonCACHE 作为上下文学习与权重学习之间的中间路径，为在不修改参数的情况下学习超出上下文窗口的推理技能提供了可扩展的算法。

------

Title: GradMem: Learning to Write Context into Memory with Test-Time Gradient Descent

URL: https://www.semanticscholar.org/paper/82c0b4a4c4e9fd48077f97ece80956ae1e7d97b3

Abstract: Many large language model applications require conditioning on long contexts. Transformers typically support this by storing a large per-layer KV-cache of past activations, which incurs substantial memory overhead. A desirable alternative is ompressive memory: read a context once, store it in a compact state, and answer many queries from that state. We study this in a context removal setting, where the model must generate an answer without access to the original context at inference time. We introduce GradMem, which writes context into memory via per-sample test-time optimization. Given a context, GradMem performs a few steps of gradient descent on a small set of prefix memory tokens while keeping model weights frozen. GradMem explicitly optimizes a model-level self-supervised context reconstruction loss, resulting in a loss-driven write operation with iterative error correction, unlike forward-only methods. On associative key--value retrieval, GradMem outperforms forward-only memory writers with the same memory size, and additional gradient steps scale capacity much more effectively than repeated forward writes. We further show that GradMem transfers beyond synthetic benchmarks: with pretrained language models, it attains competitive results on natural language tasks including bAbI and SQuAD variants, relying only on information encoded in memory.

中文翻译：许多大语言模型应用需要以长上下文为条件。Transformer 通常通过存储每层过去激活的大规模 KV cache 来支持这一点，这带来了大量内存开销。一个理想的替代方案是压缩记忆：读取一次上下文，将其存储在紧凑状态中，并从该状态回答多个查询。我们在上下文移除设置中研究此问题——模型必须在推理时无原始上下文访问的情况下生成答案。我们引入 GradMem，通过逐样本测试时优化将上下文写入记忆。给定上下文，GradMem 对一小组前缀记忆 token 执行几步梯度下降，同时保持模型权重冻结。GradMem 显式优化模型级的自监督上下文重建损失，产生一种具有迭代纠错的损失驱动写操作，与仅前向方法不同。在关联键值检索上，GradMem 在同记忆大小下优于前向记忆写入器，且额外梯度步比重复前向写入更有效地扩展容量。我们进一步展示 GradMem 可迁移到合成基准之外：使用预训练语言模型，在包括 bAbI 和 SQuAD 变体的自然语言任务上取得竞争性结果，仅依赖记忆中的编码信息。

------

Title: Deliberation in Latent Space via Differentiable Cache Augmentation

URL: https://doi.org/10.48550/arXiv.2412.17747

Abstract: Techniques enabling large language models (LLMs) to"think more"by generating and attending to intermediate reasoning steps have shown promise in solving complex problems. However, the standard approaches generate sequences of discrete tokens immediately before responding, and so they can incur significant latency costs and be challenging to optimize. In this work, we demonstrate that a frozen LLM can be augmented with an offline coprocessor that operates on the model's key-value (kv) cache. This coprocessor augments the cache with a set of latent embeddings designed to improve the fidelity of subsequent decoding. We train this coprocessor using the language modeling loss from the decoder on standard pretraining data, while keeping the decoder itself frozen. This approach enables the model to learn, in an end-to-end differentiable fashion, how to distill additional computation into its kv-cache. Because the decoder remains unchanged, the coprocessor can operate offline and asynchronously, and the language model can function normally if the coprocessor is unavailable or if a given cache is deemed not to require extra computation. We show experimentally that when a cache is augmented, the decoder achieves lower perplexity on numerous subsequent tokens. Furthermore, even without any task-specific training, our experiments demonstrate that cache augmentation consistently reduces perplexity and improves performance across a range of reasoning-intensive tasks.

中文翻译：通过生成并关注中间推理步骤来让大语言模型（LLM）"更多思考"的技术在解决复杂问题方面显示出前景。然而，标准方法在响应之前生成离散 token 序列，可能产生显著的延迟成本且难以优化。本工作中，我们展示一个冻结的 LLM 可以通过一个在其 KV cache 上运行的离线协处理器进行增强。该协处理器用一组隐式嵌入增强缓存，旨在提升后续解码的保真度。我们使用解码器的语言建模损失在标准预训练数据上训练该协处理器，同时保持解码器自身冻结。该方法使模型能够以端到端可微分的方式学习如何将额外计算蒸馏到其 KV cache 中。由于解码器保持不变，协处理器可以离线异步运行，语言模型在协处理器不可用或某缓存被认为无需额外计算时可正常运行。实验表明，当缓存被增强时，解码器在大量后续 token 上实现了更低的困惑度。即使在没有任何任务特定训练的情况下，实验证明缓存增强在一系列推理密集型任务上持续降低困惑度并提升性能。

------

Title: Trained Persistent Memory for Frozen Encoder--Decoder LLMs: Six Architectural Methods

URL: https://www.semanticscholar.org/paper/9f161d4dd64525a06f7a36b702193ddacee1b705

Abstract: Frozen encoder--decoder language models are stateless: the latent representation is discarded after every forward pass, so no information persists across sessions. This paper presents a \textbf{proof-of-concept pilot study} showing that persistent memory in the \emph{continuous latent space} of a frozen LLM is feasible -- even under severe resource constraints (a single frozen Flan-T5-XL backbone, small trainable adapters, a single dataset). We implement six architectural methods spanning three injection points and four write mechanisms; unlike text-level memory systems, every write and read is a differentiable operation on dense vectors. After training only the adapter, the memory bank continues to accumulate at inference time without gradients, enabling \emph{conversational learning}. Under a forgetting-curve evaluation on LoCoMo at two capacity scales (1$\times$ and 10$\times$), the stateless baseline scores exactly zero; at 10$\times$ all six trained adapters produce positive memory-recall curves; at 1$\times$ three methods collapse, revealing capacity as a critical design parameter. Because the memory bank is a compact numerical array, it can be scaled to arbitrarily large capacity without altering the backbone. We argue that full end-to-end training with larger models, larger data, and orders-of-magnitude larger memory will yield substantially stronger results; this pilot study establishes the feasibility baseline and design-space taxonomy that such efforts require.

中文翻译：冻结的编码器-解码器语言模型是无状态的：潜在表示在每次前向传递后被丢弃，因此没有信息在会话间持久化。本文展示了一项概念验证初步研究，表明在冻结 LLM 的连续隐空间中的持久记忆是可行的——即使在严格资源约束下（单个冻结的 Flan-T5-XL 骨干、小型可训练适配器、单一数据集）。我们实现了六种架构方法，涵盖三个注入点和四种写入机制；与文本级记忆系统不同，每次读写都是对稠密向量的可微分操作。仅训练适配器后，记忆库在推理时无需梯度即可继续积累，实现了对话式学习。在 LoCoMo 上的遗忘曲线评估中（两种容量规模：1 倍和 10 倍），无状态基线得分为零；在 10 倍容量下所有六个训练过的适配器产生正的记忆召回曲线；在 1 倍容量下三种方法崩溃，揭示了容量作为关键设计参数。由于记忆库是紧凑的数值数组，可以扩展到任意大容量而不改变骨干。我们认为，使用更大模型、更大数据和数量级更大的记忆进行完全端到端训练将产生显著更强的结果；本初步研究建立了此类努力所需的可行性基线和设计空间分类法。

------

Title: Trained Persistent Memory for Frozen Decoder-Only LLMs

URL: https://www.semanticscholar.org/paper/773eaad8149fa93df7a0c411f131980d69efdf57

Abstract: Decoder-only language models are stateless: hidden representations are discarded after every forward pass and nothing persists across sessions. Jeong (2026a) showed that trained memory adapters give a frozen encoder-decoder backbone persistent latent-space memory, building on the lateral-memory framework of Jeong (2026b,c). Here we ask whether the same principle transfers to the decoder-only setting, where no cross-attention pathway exists and memory must enter through self-attention alone. We adapt six methods -- prefix, parallel cross-attention, KV extension, Hebbian memory, context-gated branch, and slot-based sparse write -- to a frozen GPT-2, training only a small adapter $\theta_{mem}$. The write rule is shared; only the read injection changes from decoder cross-attention to self-attention KV prefix or parallel branch. On LoCoMo we find a striking inductive-bias dichotomy: at $1\times$ capacity, three methods with strong architectural priors -- cross-attention (M.2), Hebbian (M.4), and slot write (M.6) -- achieve retained-memory scores of $7-18\%$ and knowledge gains $\Delta K$ of $7-10$, while the other three fail ($<0.4\%$). At $10\times$ capacity all six converge, showing the gap is architectural, not fundamental. Together with the encoder-decoder results of Jeong (2026a) and the brain-inspired modules of Jeong (2026b,c), these findings establish persistent latent-space memory as a general paradigm spanning major transformer families.

中文翻译：仅解码器语言模型是无状态的：隐藏表示在每次前向传递后被丢弃，没有信息在会话间持久化。Jeong (2026a) 展示了训练的记忆适配器可以为冻结的编码器-解码器骨干提供持久的隐空间记忆，建立在 Jeong (2026b,c) 的横向记忆框架之上。本文探讨同一原理是否能迁移到仅解码器设置——其中没有交叉注意力路径，记忆必须仅通过自注意力进入。我们将六种方法——前缀、并行交叉注意力、KV 扩展、Hebbian 记忆、上下文门控分支和基于槽的稀疏写入——适配到冻结的 GPT-2，仅训练一个小型适配器。写入规则共享；仅读取注入从解码器交叉注意力变为自注意力 KV 前缀或并行分支。在 LoCoMo 上我们发现了一个显著的归纳偏置二分法：在 1 倍容量下，三种具有强架构先验的方法——交叉注意力（M.2）、Hebbian（M.4）和槽写入（M.6）——达到 7-18% 的保留记忆分数和 7-10 的知识增益，而其他三种失败（<0.4%）。在 10 倍容量下所有六种方法收敛，表明差距是架构性的而非根本性的。结合 Jeong (2026a) 的编码器-解码器结果和 Jeong (2026b,c) 的脑启发模块，这些发现确立了持久隐空间记忆作为跨主要 Transformer 家族的通用范式。

------

Title: Hybrid Self-evolving Structured Memory for GUI Agents

URL: https://www.semanticscholar.org/paper/1a17eebc5611e32d6738a8bb36f4f18c05771a81

Abstract: The remarkable progress of vision-language models (VLMs) has enabled GUI agents to interact with computers in a human-like manner. Yet real-world computer-use tasks remain difficult due to long-horizon workflows, diverse interfaces, and frequent intermediate errors. Prior work equips agents with external memory built from large collections of trajectories, but relies on flat retrieval over discrete summaries or continuous embeddings, falling short of the structured organization and self-evolving characteristics of human memory. Inspired by the brain, we propose Hybrid Self-evolving Structured Memory (HyMEM), a graph-based memory that couples discrete high-level symbolic nodes with continuous trajectory embeddings. HyMEM maintains a graph structure to support multi-hop retrieval, self-evolution via node update operations, and on-the-fly working-memory refreshing during inference. Extensive experiments show that HyMEM consistently improves open-source GUI agents, enabling 7B/8B backbones to match or surpass strong closed-source models; notably, it boosts Qwen2.5-VL-7B by +22.5% and outperforms Gemini2.5-Pro-Vision and GPT-4o.

中文翻译：视觉-语言模型（VLM）的显著进展使 GUI agent 能够以类人方式与计算机交互。然而，由于长 horizon 工作流、多样化的界面和频繁的中间错误，真实世界的计算机使用任务仍然困难。先前工作为 agent 配备从大量轨迹集合构建的外部记忆，但依赖于在离散摘要或连续嵌入上的平面检索，远不及人类记忆的结构化组织和自我演化特性。受大脑启发，我们提出 Hybrid Self-evolving Structured Memory（HyMEM），一种将离散高级符号节点与连续轨迹嵌入耦合的图记忆。HyMEM 维护图结构以支持多跳检索、通过节点更新操作实现的自我演化，以及推理时的即时工作记忆刷新。大量实验表明，HyMEM 持续提升开源 GUI agent，使 7B/8B 骨干模型匹配或超越强大的闭源模型；值得注意的是，它将 Qwen2.5-VL-7B 提升 +22.5%，超越 Gemini2.5-Pro-Vision 和 GPT-4o。

------

Title: TempoFit: Plug-and-Play Layer-Wise Temporal KV Memory for Long-Horizon Vision-Language-Action Manipulation

URL: https://www.semanticscholar.org/paper/12315b5e7d40edfdd4821f8e987d902964de132f

Abstract: Pretrained Vision-Language-Action (VLA) policies have achieved strong single-step manipulation, but their inference remains largely memoryless, which is brittle in non-Markovian long-horizon settings with occlusion, state aliasing, and subtle post-action changes. Prior approaches inject history either by stacking frames, which scales visual tokens and latency while adding near-duplicate pixels, or by learning additional temporal interfaces that require (re-)training and may break the original single-frame inference graph. We present TempoFit, a training-free temporal retrofit that upgrades frozen VLAs through state-level memory. Our key insight is that prefix attention K/V already form a model-native, content-addressable runtime state; reusing them across timesteps introduces history without new tokens or trainable modules. TempoFit stores layer-wise FIFO prefix K/V at selected intermediate layers, performs parameter-free K-to-K retrieval with Frame-Gap Temporal Bias (FGTB), a fixed recency bias inspired by positional biases in NLP, to keep decisions present-dominant, and injects the retrieved context via pre-attention residual loading with norm-preserving rescaling to avoid distribution shift under frozen weights. On LIBERO-LONG, TempoFit improves strong pretrained backbones by up to +4.0% average success rate while maintaining near-real-time latency, and it transfers consistently to CALVIN and real-robot long-horizon tasks.

中文翻译：预训练的视觉-语言-动作（VLA）策略已在单步操作上取得强大性能，但其推理仍基本无记忆，在具有遮挡、状态混淆和细微动作后变化的非马尔科夫长 horizon 设置中脆弱。先前方法或通过堆叠帧注入历史——这膨胀视觉 token 和延迟同时添加几乎重复的像素——或通过引入需要（重新）训练且可能破坏原始单帧推理图的额外时间接口。我们提出 TempoFit，一种无需训练的时序改造方法，通过状态级记忆升级冻结的 VLA。我们核心洞察是前缀注意力 K/V 已经形成模型原生的、内容可寻址的运行时状态；跨时间步复用它们可以在不引入新 token 或可训练模块的情况下引入历史。TempoFit 在选定的中间层存储逐层 FIFO 前缀 K/V，执行无参数 K-to-K 检索，并采用 Frame-Gap Temporal Bias（FGTB）——一种受 NLP 中位置偏置启发的固定新近偏置——以保持决策以当前为主，并通过保持范数的重新缩放以预注意力残差加载的方式注入检索到的上下文，避免冻结权重下的分布偏移。在 LIBERO-LONG 上，TempoFit 将强大预训练骨干的平均成功率提升高达 +4.0%，同时保持接近实时的延迟，并持续迁移到 CALVIN 和真实机器人长 horizon 任务。

------

Title: Online Adaptation of Language Models with a Memory of Amortized Contexts

URL: https://doi.org/10.48550/arXiv.2403.04317

Abstract: Due to the rapid generation and dissemination of information, large language models (LLMs) quickly run out of date despite enormous development costs. To address the crucial need to keep models updated, online learning has emerged as a critical tool when utilizing LLMs for real-world applications. However, given the ever-expanding corpus of unseen documents and the large parameter space of modern LLMs, efficient adaptation is essential. To address these challenges, we propose Memory of Amortized Contexts (MAC), an efficient and effective online adaptation framework for LLMs with strong knowledge retention. We propose a feature extraction and memory-augmentation approach to compress and extract information from new documents into compact modulations stored in a memory bank. When answering questions, our model attends to and extracts relevant knowledge from this memory bank. To learn informative modulations in an efficient manner, we utilize amortization-based meta-learning, which substitutes an otherwise required optimization process with a single forward pass of the encoder. Subsequently, we learn to choose from and aggregate selected documents into a single modulation by conditioning on the question, allowing us to adapt a frozen language model during test time without requiring further gradient updates. Our experiment demonstrates the superiority of MAC in multiple aspects, including online adaptation performance, time, and memory efficiency. In addition, we show how MAC can be combined with and improve the performance of popular alternatives such as retrieval augmented generations (RAGs). Code is available at: https://github.com/jihoontack/MAC.

中文翻译：由于信息的快速生成和传播，大语言模型（LLM）尽管开发成本巨大但迅速过时。为满足保持模型更新的关键需求，在线学习已成为在真实应用中使用 LLM 的关键工具。然而，鉴于不断扩展的未见文档语料和现代 LLM 的大参数空间，高效适配至关重要。为应对这些挑战，我们提出 Memory of Amortized Contexts（MAC），一种具有强知识保留的高效在线适配框架。我们提出特征提取和记忆增强方法，将新文档中的信息压缩提取为存储在记忆库中的紧凑调制。回答问题时，模型关注并从此记忆库中提取相关知识。为高效学习有信息量的调制，我们利用基于摊销的元学习，用编码器的单次前向传递替代原本需要的优化过程。随后，我们学习以问题为条件选择并聚合选定文档为单一调制，允许在测试时适配冻结语言模型而无需进一步梯度更新。实验证明了 MAC 在多个方面的优越性，包括在线适配性能、时间和内存效率。我们还展示了 MAC 如何与检索增强生成（RAG）等流行方案结合并提升其性能。

------

Title: Compressed Context Memory For Online Language Model Interaction

URL: https://doi.org/10.48550/arXiv.2312.03414

Abstract: This paper presents a context key/value compression method for Transformer language models in online scenarios, where the context continually expands. As the context lengthens, the attention process demands increasing memory and computations, which in turn reduces the throughput of the language model. To address this challenge, we propose a compressed context memory system that continually compresses the accumulating attention key/value pairs into a compact memory space, facilitating language model inference in a limited memory space of computing environments. Our compression process involves integrating a lightweight conditional LoRA into the language model's forward pass during inference, without the need for fine-tuning the model's entire set of weights. We achieve efficient training by modeling the recursive compression process as a single parallelized forward computation. Through evaluations on conversation, personalization, and multi-task learning, we demonstrate that our approach achieves the performance level of a full context model with $5\times$ smaller context memory size. We further demonstrate the applicability of our approach in a streaming setting with an unlimited context length, outperforming the sliding window approach. Codes are available at https://github.com/snu-mllab/context-memory.

中文翻译：本文针对在线场景中上下文不断扩展的 Transformer 语言模型提出了上下文键值压缩方法。随着上下文增长，注意力过程需要越来越多的内存和计算，从而降低了语言模型的吞吐量。为应对这一挑战，我们提出了一种压缩上下文记忆系统，持续将累积的注意力键值对压缩到紧凑的记忆空间中，使语言模型推理能在计算环境有限的内存空间中进行。压缩过程涉及在推理时将轻量条件 LoRA 集成到语言模型的前向传递中，无需微调模型全部权重。我们通过将递归压缩过程建模为单次并行前向计算来实现高效训练。在对话、个性化和多任务学习上的评估表明，我们的方法以 5 倍更小的上下文内存达到了全上下文模型的性能水平。我们进一步展示了方法在无限上下文长度的流式场景中的适用性，优于滑动窗口方法。

------

Title: EchoVLA: Synergistic Declarative Memory for VLA-Driven Mobile Manipulation

URL: https://www.semanticscholar.org/paper/2e5dabf10c264b1fa3f53d76ea3bb8f15fa89f93

Abstract: Recent progress in Vision-Language-Action (VLA) models has enabled embodied agents to interpret multimodal instructions and perform complex tasks. However, existing VLAs are mostly confined to short-horizon, table-top manipulation, lacking the memory and reasoning capability required for mobile manipulation, where agents must coordinate navigation and manipulation under changing spatial contexts. In this work, we present EchoVLA, a memory-aware VLA model for mobile manipulation. EchoVLA incorporates a synergistic declarative memory inspired by the human brain, consisting of a scene memory that maintains a collection of spatial-semantic maps and an episodic memory that stores task-level experiences with multimodal contextual features. The two memories are individually stored, updated, and retrieved based on current observations, task history, and instructions, and their retrieved representations are fused via coarse- and fine-grained attention to guide base-arm diffusion policies. To support large-scale training, we further introduce MoMani, an automated benchmark that generates expert-level trajectories through multimodal large language model (MLLM)-guided planning and feedback-driven refinement, supplemented with real-robot demonstrations. Comprehensive simulated and real-world results demonstrate that EchoVLA substantially improves overall performance, e.g., it achieves the highest success rates of 0.52 on manipulation/navigation tasks and 0.31 on mobile manipulation tasks in simulation, exceeding the strong baseline $\pi_{0.5}$ by +0.20 and +0.11, respectively.

中文翻译：近期视觉-语言-动作（VLA）模型的进展使具身 agent 能够解释多模态指令并执行复杂任务。然而，现有 VLA 大多局限于短 horizon 桌面操作，缺乏移动操作所需的记忆和推理能力——移动操作中 agent 必须在变化的空间上下文中协调导航和操作。本文中，我们提出 EchoVLA，一种面向移动操作的记忆感知 VLA 模型。EchoVLA 融合了受人脑启发的协同陈述性记忆，包括维护空间语义地图集合的场景记忆和存储任务级经验及多模态上下文特征的情节记忆。两种记忆根据当前观察、任务历史和指令分别存储、更新和检索，其检索到的表示通过粗粒度和细粒度注意力融合以引导基座-臂部扩散策略。为支持大规模训练，我们进一步引入 MoMani，一种通过 MLLM 引导的规划和反馈驱动精炼生成专家级轨迹的自动化基准，辅以真实机器人演示。综合仿真和真实结果表明，EchoVLA 大幅提升了整体性能，如在仿真中操作/导航任务最高成功率 0.52，移动操作任务 0.31，分别超出强基线 π₀.₅ 达 +0.20 和 +0.11。

------

Title: KEEP: A KV-Cache-Centric Memory Management System for Efficient Embodied Planning

URL: https://doi.org/10.48550/arXiv.2602.23592

Abstract: Memory-augmented Large Language Models (LLMs) have demonstrated remarkable capability for complex and long-horizon embodied planning. By keeping track of past experiences and environmental states, memory enables LLMs to maintain a global view, thereby avoiding repetitive exploration. However, existing approaches often store the memory as raw text, leading to excessively long prompts and high prefill latency. While it is possible to store and reuse the KV caches, the efficiency benefits are greatly undermined due to frequent KV cache updates. In this paper, we propose KEEP, a KV-cache-centric memory management system for efficient embodied planning. KEEP features 3 key innovations: (1) a Static-Dynamic Memory Construction algorithm that reduces KV cache recomputation by mixed-granularity memory group; (2) a Multi-hop Memory Re-computation algorithm that dynamically identifies important cross-attention among different memory groups and reconstructs memory interactions iteratively; (3) a Layer-balanced Memory Loading that eliminates unbalanced KV cache loading and cross-attention computation across different layers. Extensive experimental results have demonstrated that KEEP achieves 2.68x speedup with negligible accuracy loss compared with text-based memory methods on ALFRED dataset. Compared with the KV re-computation method CacheBlend (EuroSys'25), KEEP shows 4.13% success rate improvement and 1.90x time-to-first-token (TTFT) reduction. Our code is available on https://github.com/PKU-SEC-Lab/KEEP_Embodied_Memory.

中文翻译：记忆增强的大语言模型（LLM）在复杂和长 horizon 具身规划中展现了显著能力。通过跟踪过去经验和环境状态，记忆使 LLM 能够保持全局视图，从而避免重复探索。然而，现有方法通常将记忆存储为原始文本，导致提示过长和预填充延迟高。虽然可以存储和复用 KV cache，但由于频繁的 KV cache 更新，效率收益大打折扣。本文中，我们提出 KEEP，一种以 KV cache 为中心的记忆管理系统，用于高效具身规划。KEEP 具有三项关键创新：(1) 静态-动态记忆构建算法，通过混合粒度记忆组减少 KV cache 重计算；(2) 多跳记忆重计算算法，动态识别不同记忆组间的重要交叉注意力，迭代重建记忆交互；(3) 层平衡记忆加载，消除不同层间的不平衡 KV cache 加载和交叉注意力计算。大量实验表明，在 ALFRED 数据集上，KEEP 相比基于文本的记忆方法实现了 2.68 倍加速且精度损失可忽略。相比 KV 重计算方法 CacheBlend（EuroSys'25），KEEP 成功率提升 4.13%，首 token 时间（TTFT）减少 1.90 倍。

------

Title: Vision-Language Memory for Spatial Reasoning

URL: https://doi.org/10.48550/arXiv.2511.20644

Abstract: Spatial reasoning is a critical capability for intelligent robots, yet current vision-language models (VLMs) still fall short of human-level performance in video-based spatial reasoning. This gap mainly stems from two challenges: a semantic-geometric misalignment that prevents consistent 3D understanding, and the absence of persistent memory to retain 3D representation and understanding over time. To address these limitations, we present VLM$^2$, a Vision-Language Model with persistent Memory for spatial reasoning with a view-consistent, 3D-aware representation purely from 2D video. Specifically, to enhance long-horizon reasoning, we incorporate a dual-memory module, consisting of a working memory that operates as a sliding window to focus on immediate context, and an episodic memory that consolidates and stores critical long-term information. This design enables efficient and long-horizon spatial reasoning with a fixed computational cost. Extensive experiments on multiple benchmarks show that VLM$^2$ achieves state-of-the-art performance among video-only models, significantly advancing the frontier of visual-spatial intelligence.

中文翻译：空间推理是智能机器人的关键能力，但当前视觉-语言模型（VLM）在基于视频的空间推理上仍低于人类水平。这一差距主要源于两个挑战：语义-几何失配阻碍了一致的 3D 理解，以及缺乏持久记忆来随时间保留 3D 表示和理解。为解决这些局限，我们提出 VLM²，一种具有持久记忆的视觉-语言模型，用于从纯 2D 视频中进行视角一致的 3D 感知空间推理。具体而言，为增强长 horizon 推理，我们引入双记忆模块，包括作为滑动窗口关注即时上下文的工作记忆，以及整合存储关键长期信息的情节记忆。这一设计使长 horizon 空间推理能以固定计算开销高效进行。在多个基准上的大量实验表明，VLM² 在纯视频模型中达到最先进性能，显著推动了视觉空间智能的前沿。

------

Title: In-context Vectors: Making In Context Learning More Effective and Controllable Through Latent Space Steering

URL: https://doi.org/10.48550/arXiv.2311.06668

Abstract: Large language models (LLMs) demonstrate emergent in-context learning capabilities, where they adapt to new tasks based on example demonstrations. However, in-context learning has seen limited effectiveness in many settings, is difficult to quantitatively control and takes up context window space. To overcome these limitations, we propose an alternative approach that recasts in-context learning as in-context vectors (ICV). Using ICV has two steps. We first use a forward pass on demonstration examples to create the in-context vector from the latent embedding of the LLM. This vector captures essential information about the intended task. On a new query, instead of adding demonstrations to the prompt, we shift the latent states of the LLM using the ICV. The ICV approach has several benefits: 1) it enables the LLM to more effectively follow the demonstration examples; 2) it's easy to control by adjusting the magnitude of the ICV; 3) it reduces the length of the prompt by removing the in-context demonstrations; 4) ICV is computationally much more efficient than fine-tuning. We demonstrate that ICV achieves better performance compared to standard in-context learning and fine-tuning on diverse tasks including safety, style transfer, role-playing and formatting. Moreover, we show that we can flexibly teach LLM to simultaneously follow different types of instructions by simple vector arithmetics on the corresponding ICVs.

中文翻译：大语言模型（LLM）展现出涌现的上下文学习能力，能够基于示例演示适应新任务。然而，上下文学习在许多设置中效果有限，难以量化控制且占用上下文窗口空间。为克服这些局限，我们提出将上下文学习重新定义为上下文向量（ICV）的替代方法。使用 ICV 分两步：首先对演示示例执行前向传递，从 LLM 的潜在嵌入创建上下文向量，该向量捕获关于目标任务的基本信息。对新查询，我们不将演示添加到提示中，而是使用 ICV 偏移 LLM 的潜在状态。ICV 方法有多项优势：1) 使 LLM 更有效地遵循演示示例；2) 通过调节 ICV 的强度易于控制；3) 通过移除上下文演示减少提示长度；4) ICV 计算上比微调高效得多。我们证明 ICV 在包括安全、风格迁移、角色扮演和格式化的多样化任务上比标准上下文学习和微调取得更好性能。此外，我们展示了可以通过对相应 ICV 进行简单的向量算术来灵活地让 LLM 同时遵循不同类型指令。

------

Title: VPWEM: Non-Markovian Visuomotor Policy with Working and Episodic Memory

URL: https://www.semanticscholar.org/paper/a56957384e9a8c3ab18d5f3921c1a332b8d6440e

Abstract: Imitation learning from human demonstrations has achieved significant success in robotic control, yet most visuomotor policies still condition on single-step observations or short-context histories, making them struggle with non-Markovian tasks that require long-term memory. Simply enlarging the context window incurs substantial computational and memory costs and encourages overfitting to spurious correlations, leading to catastrophic failures under distribution shift and violating real-time constraints in robotic systems. By contrast, humans can compress important past experiences into long-term memories and exploit them to solve tasks throughout their lifetime. In this paper, we propose VPWEM, a non-Markovian visuomotor policy equipped with working and episodic memories. VPWEM retains a sliding window of recent observation tokens as short-term working memory, and introduces a Transformer-based contextual memory compressor that recursively converts out-of-window observations into a fixed number of episodic memory tokens. The compressor uses self-attention over a cache of past summary tokens and cross-attention over a cache of historical observations, and is trained jointly with the policy. We instantiate VPWEM on diffusion policies to exploit both short-term and episode-wide information for action generation with nearly constant memory and computation per step. Experiments demonstrate that VPWEM outperforms state-of-the-art baselines including diffusion policies and vision-language-action (VLA) models by more than 20% on the memory-intensive manipulation tasks in MIKASA and achieves an average 5% improvement on the mobile manipulation benchmark MoMaRT. Code is available at https://github.com/HarryLui98/code_vpwem.

中文翻译：从人类演示的模仿学习在机器人控制中取得了显著成功，但大多数视觉运动策略仍以单步观察或短上下文历史为条件，使其难以应对需要长期记忆的非马尔科夫任务。简单扩大上下文窗口会带来大量计算和内存成本，并鼓励过拟合到虚假相关，在分布偏移下导致灾难性失败并违反机器人系统的实时约束。相比之下，人类可以将重要的过去经验压缩为长期记忆，并在整个生命周期中利用它们解决任务。本文中，我们提出 VPWEM，一种配备工作记忆和情节记忆的非马尔科夫视觉运动策略。VPWEM 保留最近观察 token 的滑动窗口作为短期工作记忆，并引入基于 Transformer 的上下文记忆压缩器，将窗口外的观察递归转换为固定数量的情节记忆 token。该压缩器使用对过去摘要 token 缓存的自注意力和对历史观察缓存的交叉注意力，并与策略联合训练。我们将 VPWEM 实例化到扩散策略上，以几乎恒定的每步内存和计算同时利用短期和整个 episode 的信息进行动作生成。实验表明，VPWEM 在 MIKASA 的记忆密集型操作任务上比最先进基线（包括扩散策略和 VLA 模型）提升超过 20%，在移动操作基准 MoMaRT 上实现平均 5% 的提升。

------

Title: Memorizing Transformers

URL: https://doi.org/10.48550/arXiv.2203.08913

Abstract: Language models typically need to be trained or finetuned in order to acquire new knowledge, which involves updating their weights. We instead envision language models that can simply read and memorize new data at inference time, thus acquiring new knowledge immediately. In this work, we extend language models with the ability to memorize the internal representations of past inputs. We demonstrate that an approximate kNN lookup into a non-differentiable memory of recent (key, value) pairs improves language modeling across various benchmarks and tasks, including generic webtext (C4), math papers (arXiv), books (PG-19), code (Github), as well as formal theorems (Isabelle). We show that the performance steadily improves when we increase the size of memory up to 262K tokens. On benchmarks including code and mathematics, we find that the model is capable of making use of newly defined functions and theorems during test time.

中文翻译：语言模型通常需要训练或微调来获取新知识，这涉及更新其权重。我们设想语言模型可以在推理时简单地读取和记忆新数据，从而立即获取新知识。本文中，我们扩展语言模型使其能够记忆过去输入的内部表示。我们证明，对近期（键，值）对的近似 kNN 查找（不可微分记忆）在各类基准和任务上改善了语言建模，包括通用网页文本（C4）、数学论文（arXiv）、书籍（PG-19）、代码（GitHub）以及形式化定理（Isabelle）。我们表明，当记忆大小增加到最多 262K token 时性能稳步提升。在包括代码和数学的基准上，我们发现模型能够在测试时利用新定义的函数和定理。

------

Title: Self-Consolidation for Self-Evolving Agents

URL: https://doi.org/10.48550/arXiv.2602.01966

Abstract: While large language model (LLM) agents have demonstrated impressive problem-solving capabilities, they typically operate as static systems, lacking the ability to evolve through lifelong interaction. Existing attempts to bridge this gap primarily rely on retrieving successful past trajectories as demonstrations. However, this paradigm faces two critical limitations. First, by focusing solely on success, agents overlook the rich pedagogical value embedded in failed attempts, preventing them from identifying and avoiding recurrent pitfalls. Second, continually accumulating textual experiences not only increases the time consumption during retrieval but also inevitably introduces noise and exhausts the largest context window of current LLMs. To address these challenges, we propose a novel self-evolving framework for LLM agents that introduces a complementary evolution mechanism: First, a contrastive reflection strategy is introduced to explicitly summarize error-prone patterns and capture reusable insights. Second, we propose a self-consolidation mechanism that distills non-parametric textual experience into compact learnable parameters. This enables the agent to internalize extensive historical experience directly into its latent space. Extensive experiments demonstrate the advantages of our method in long-term agent evolution.

中文翻译：虽然大语言模型（LLM）agent 已展现出令人印象深刻的问题解决能力，但它们通常作为静态系统运行，缺乏通过终身交互进行演化的能力。现有尝试弥合这一差距的方法主要依赖检索过去的成功轨迹作为演示。然而，这一范式面临两个关键局限。首先，仅关注成功，agent 忽视了失败尝试中蕴含的丰富教学价值，无法识别和规避反复出现的陷阱。其次，持续积累文本经验不仅增加了检索时的时间消耗，还不可避免地引入噪声并耗尽当前 LLM 的最大上下文窗口。为应对这些挑战，我们提出一种新颖的 LLM agent 自演化框架，引入互补的演化机制：第一，对比反思策略显式总结易出错模式并捕获可复用的洞见。第二，我们提出自整合机制，将非参数化文本经验蒸馏为紧凑的可学习参数。这使 agent 能够将大量历史经验直接内化到其隐空间中。大量实验证明了我们方法在长期 agent 演化中的优势。

------

Title: MemoryPrompt: A Light Wrapper to Improve Context Tracking in Pre-trained Language Models

URL: https://doi.org/10.48550/arXiv.2402.15268

Abstract: Transformer-based language models (LMs) track contextual information through large, hard-coded input windows. We introduce MemoryPrompt, a leaner approach in which the LM is complemented by a small auxiliary recurrent network that passes information to the LM by prefixing its regular input with a sequence of vectors, akin to soft prompts, without requiring LM finetuning. Tested on a task designed to probe a LM’s ability to keep track of multiple fact updates, a MemoryPrompt-augmented LM outperforms much larger LMs that have access to the full input history. We also test MemoryPrompt on a long-distance dialogue dataset, where its performance is comparable to that of a model conditioned on the entire conversation history. In both experiments we also observe that, unlike full-finetuning approaches, MemoryPrompt does not suffer from catastrophic forgetting when adapted to new tasks, thus not disrupting the generalist capabilities of the underlying LM.

中文翻译：基于 Transformer 的语言模型（LM）通过大型硬编码输入窗口跟踪上下文信息。我们引入 MemoryPrompt，一种更轻量的方法，用一个小的辅助递归网络补充 LM，该网络通过在其常规输入前添加向量序列（类似软提示）向 LM 传递信息，无需 LM 微调。在旨在探测 LM 跟踪多个事实更新能力的任务上测试，MemoryPrompt 增强的 LM 优于能访问完整输入历史的更大 LM。我们还在长距离对话数据集上测试了 MemoryPrompt，其性能与以整个对话历史为条件的模型相当。在两个实验中我们还观察到，与完全微调方法不同，MemoryPrompt 在适应新任务时不会遭受灾难性遗忘，因此不会破坏底层 LM 的通用能力。

------

Title: VisMem: Latent Vision Memory Unlocks Potential of Vision-Language Models

URL: https://doi.org/10.48550/arXiv.2511.11007

Abstract: Despite the remarkable success of Vision-Language Models (VLMs), their performance on a range of complex visual tasks is often hindered by a"visual processing bottleneck": a propensity to lose grounding in visual evidence and exhibit a deficit in contextualized visual experience during prolonged generation. Drawing inspiration from human cognitive memory theory, which distinguishes short-term visually-dominant memory and long-term semantically-dominant memory, we propose VisMem, a cognitively-aligned framework that equips VLMs with dynamic latent vision memories, a short-term module for fine-grained perceptual retention and a long-term module for abstract semantic consolidation. These memories are seamlessly invoked during inference, allowing VLMs to maintain both perceptual fidelity and semantic consistency across thinking and generation. Extensive experiments across diverse visual benchmarks for understanding, reasoning, and generation reveal that VisMem delivers a significant average performance boost of 11.0% relative to the vanilla model and outperforms all counterparts, establishing a new paradigm for latent-space memory enhancement. The code will be available: https://github.com/YU-deep/VisMem.git.

中文翻译：尽管视觉-语言模型（VLM）取得了显著成功，但在一系列复杂视觉任务上的性能常受"视觉处理瓶颈"阻碍：在长时间生成过程中倾向于丧失对视觉证据的 grounding，并表现出情境化视觉经验的缺失。受人类认知记忆理论启发——区分短期视觉主导记忆和长期语义主导记忆——我们提出 VisMem，一个认知对齐的框架，为 VLM 赋予动态隐式视觉记忆，包括用于细粒度感知保留的短期模块和用于抽象语义整合的长期模块。这些记忆在推理时无缝调用，使 VLM 在思维和生成过程中同时保持感知保真度和语义一致性。在理解、推理和生成等多种视觉基准上的大量实验表明，VisMem 相比原始模型平均性能提升 11.0%，超越所有对照方法，建立了隐空间记忆增强的新范式。

------

Title: TokMem: One-Token Procedural Memory for Large Language Models

URL: https://www.semanticscholar.org/paper/68429e12cf5c4083f6dcee71dc76e844ec511a41

Abstract: Large language models are typically controlled via prompts, which must be repeatedly re-processed for every new query and are difficult to reuse modularly. We introduce TokMem, a procedural memory framework that compiles each reusable task procedure into a single trainable memory token. Each token serves as both a procedure index and a generation control signal that steers generation, enabling targeted behaviors with constant-size overhead. TokMem keeps the backbone LLM frozen and stores procedural knowledge entirely in these dedicated units, so new procedures can be added continually without interfering with existing ones. We evaluate TokMem on two settings: atomic recall over 1,000 Super-Natural Instructions tasks and compositional recall on multi-step function-calling. Our results show that TokMem consistently outperforms retrieval-augmented prompting while avoiding repeated context overhead. Moreover, it matches or exceeds parameter-efficient fine-tuning with substantially fewer trainable parameters.

中文翻译：大语言模型通常通过提示控制，提示必须对每个新查询反复重新处理，且难以模块化复用。我们引入 TokMem，一种程序性记忆框架，将每个可复用任务过程编译为单个可训练记忆 token。每个 token 既是过程索引也是生成控制信号，引导生成实现目标行为，且开销恒定。TokMem 保持骨干 LLM 冻结，将程序性知识完全存储在这些专用单元中，因此可以持续添加新过程而不干扰现有过程。我们在两种设置下评估 TokMem：在 1000 个 Super-Natural Instructions 任务上的原子回忆和在多步函数调用上的组合回忆。结果表明，TokMem 持续优于检索增强提示，同时避免了重复的上下文开销。此外，它以显著更少的可训练参数匹配或超越参数高效微调。

------

Title: Implicit In-context Learning

URL: https://doi.org/10.48550/arXiv.2405.14660

Abstract: In-context Learning (ICL) empowers large language models (LLMs) to swiftly adapt to unseen tasks at inference-time by prefixing a few demonstration examples before queries. Despite its versatility, ICL incurs substantial computational and memory overheads compared to zero-shot learning and is sensitive to the selection and order of demonstration examples. In this work, we introduce Implicit In-context Learning (I2CL), an innovative paradigm that reduces the inference cost of ICL to that of zero-shot learning with minimal information loss. I2CL operates by first generating a condensed vector representation, namely a context vector, extracted from the demonstration examples. It then conducts an inference-time intervention through injecting a linear combination of the context vector and query activations back into the model's residual streams. Empirical evaluation on nine real-world tasks across three model architectures demonstrates that I2CL achieves few-shot level performance at zero-shot inference cost, and it exhibits robustness against variations in demonstration examples. Furthermore, I2CL facilitates a novel representation of task-ids, enhancing task similarity detection and fostering effective transfer learning. We also perform a comprehensive analysis and ablation study on I2CL, offering deeper insights into its internal mechanisms. Code is available at https://github.com/LzVv123456/I2CL.

中文翻译：上下文学习（ICL）使大语言模型（LLM）能够在推理时通过在查询前添加少量演示示例快速适应未见任务。尽管灵活，ICL 相比零样本学习产生大量计算和内存开销，且对演示示例的选择和顺序敏感。本文中，我们引入隐式上下文学习（I2CL），一种创新范式，将 ICL 的推理成本降至零样本学习水平且信息损失最小。I2CL 首先生成压缩向量表示——上下文向量——从演示示例中提取。然后通过将上下文向量和查询激活的线性组合注入模型的残差流，进行推理时干预。在三个模型架构的九个真实任务上的实证评估表明，I2CL 以零样本推理成本达到少样本性能水平，并对演示示例的变化表现出鲁棒性。此外，I2CL 促进了一种新的任务 ID 表示，增强任务相似度检测并支持高效迁移学习。我们对 I2CL 进行了全面的分析和消融研究，提供对其内部机制的更深入洞察。

------

Title: ReMem-VLA: Empowering Vision-Language-Action Model with Memory via Dual-Level Recurrent Queries

URL: https://www.semanticscholar.org/paper/f388b0146fe0fbd0d36ba16043448cf558d93f33

Abstract: Vision-language-action (VLA) models for closed-loop robot control are typically cast under the Markov assumption, making them prone to errors on tasks requiring historical context. To incorporate memory, existing VLAs either retrieve from a memory bank, which can be misled by distractors, or extend the frame window, whose fixed horizon still limits long-term retention. In this paper, we introduce ReMem-VLA, a Recurrent Memory VLA model equipped with two sets of learnable queries: frame-level recurrent memory queries for propagating information across consecutive frames to support short-term memory, and chunk-level recurrent memory queries for carrying context across temporal chunks for long-term memory. These queries are trained end-to-end to aggregate and maintain relevant context over time, implicitly guiding the model's decisions without additional training or inference cost. Furthermore, to enhance visual memory, we introduce Past Observation Prediction as an auxiliary training objective. Through extensive memory-centric simulation and real-world robot experiments, we demonstrate that ReMem-VLA exhibits strong memory capabilities across multiple dimensions, including spatial, sequential, episodic, temporal, and visual memory. ReMem-VLA significantly outperforms memory-free VLA baselines $\pi$0.5 and OpenVLA-OFT and surpasses MemoryVLA on memory-dependent tasks by a large margin.

中文翻译：用于闭环机器人控制的视觉-语言-动作（VLA）模型通常在马尔科夫假设下建模，使其在需要历史上下文的任务上容易出错。为引入记忆，现有 VLA 要么从记忆库检索（可能被干扰项误导），要么扩展帧窗口（其固定 horizon 仍限制长期保留）。本文中，我们引入 ReMem-VLA，一种配备两组可学习查询的循环记忆 VLA 模型：帧级循环记忆查询用于跨连续帧传播信息以支持短期记忆，块级循环记忆查询用于跨时间块传递上下文以支持长期记忆。这些查询端到端训练，随时间聚合和维持相关上下文，隐式引导模型决策，无需额外训练或推理成本。此外，为增强视觉记忆，我们引入过去观察预测作为辅助训练目标。通过大量以记忆为中心的仿真和真实机器人实验，我们证明 ReMem-VLA 在空间、序列、情节、时序和视觉记忆等多个维度上展现了强大的记忆能力。ReMem-VLA 显著优于无记忆 VLA 基线 π0.5 和 OpenVLA-OFT，并在记忆依赖任务上大幅超越 MemoryVLA。

------

Title: Streaming Video Question-Answering with In-context Video KV-Cache Retrieval

URL: https://doi.org/10.48550/arXiv.2503.00540

Abstract: We propose ReKV, a novel training-free approach that enables efficient streaming video question-answering (StreamingVQA), by seamlessly integrating with existing Video Large Language Models (Video-LLMs). Traditional VideoQA systems struggle with long videos, as they must process entire videos before responding to queries, and repeat this process for each new question. In contrast, our approach analyzes long videos in a streaming manner, allowing for prompt responses as soon as user queries are received. Building on a common Video-LLM, we first incorporate a sliding-window attention mechanism, ensuring that input frames attend to a limited number of preceding frames, thereby reducing computational overhead. To prevent information loss, we store processed video key-value caches (KV-Caches) in RAM and disk, reloading them into GPU memory as needed. Additionally, we introduce a retrieval method that leverages an external retriever or the parameters within Video-LLMs to retrieve only query-relevant KV-Caches, ensuring both efficiency and accuracy in question answering. ReKV enables the separation of video encoding and question-answering across different processes and GPUs, significantly enhancing the efficiency of StreamingVQA. Through comprehensive experimentation, we validate the efficacy and practicality of our approach, which significantly boosts efficiency and enhances applicability over existing VideoQA models.

中文翻译：我们提出 ReKV，一种无需训练的新方法，通过与现有视频大语言模型（Video-LLM）无缝集成实现高效的流式视频问答（StreamingVQA）。传统 VideoQA 系统难以处理长视频，因为必须在回答查询前处理整个视频，并对每个新问题重复此过程。相比之下，我们的方法以流式方式分析长视频，允许在收到用户查询后即时响应。基于通用 Video-LLM，我们首先引入滑动窗口注意力机制，确保输入帧仅关注有限数量的前序帧，从而降低计算开销。为防止信息丢失，我们将处理过的视频 KV cache 存储在 RAM 和磁盘中，根据需要重新加载到 GPU 内存。此外，我们引入一种检索方法，利用外部检索器或 Video-LLM 内部参数仅检索与查询相关的 KV cache，确保问答的效率和准确性。ReKV 实现了视频编码和问答在不同进程和 GPU 上的分离，显著提升了 StreamingVQA 的效率。通过全面实验，我们验证了方法的有效性和实用性，显著提升了效率并增强了相对于现有 VideoQA 模型的适用性。

------

Title: HAMLET: Switch your Vision-Language-Action Model into a History-Aware Policy

URL: https://doi.org/10.48550/arXiv.2510.00695

Abstract: Inherently, robotic manipulation tasks are history-dependent: leveraging past context could be beneficial. However, most existing Vision-Language-Action models (VLAs) have been designed without considering this aspect, i.e., they rely solely on the current observation, ignoring preceding context. In this paper, we propose HAMLET, a scalable framework to adapt VLAs to attend to the historical context during action prediction. Specifically, we introduce moment tokens that compactly encode perceptual information at each timestep. Their representations are initialized with time-contrastive learning, allowing them to better capture temporally distinctive aspects. Next, we employ a lightweight memory module that integrates the moment tokens across past timesteps into memory features, which are then leveraged for action prediction. Through empirical evaluation, we show that HAMLET successfully transforms a state-of-the-art VLA into a history-aware policy, especially demonstrating significant improvements on long-horizon tasks that require historical context. In particular, on top of GR00T N1.5, HAMLET achieves an average success rate of 76.4% on history-dependent real-world tasks, surpassing the baseline performance by 47.2%. Furthermore, HAMLET pushes prior art performance from 64.1% to 66.4% on RoboCasa Kitchen (100-demo setup) and from 95.6% to 97.7% on LIBERO, highlighting its effectiveness even under generic robot-manipulation benchmarks.

中文翻译：机器人操作任务本质上是历史依赖的：利用过去的上下文可能是有益的。然而，大多数现有视觉-语言-动作模型（VLA）在设计时未考虑这一点，即它们仅依赖当前观察，忽略前序上下文。本文中，我们提出 HAMLET，一种将 VLA 适配为在动作预测时关注历史上下文的可扩展框架。具体而言，我们引入 moment token，在每个时间步紧凑编码感知信息。它们的表示通过时间对比学习初始化，使其更好地捕获时间上的区分性特征。接着，我们采用轻量记忆模块，将跨过去时间步的 moment token 集成为记忆特征，然后用于动作预测。通过实证评估，我们证明 HAMLET 成功将最先进的 VLA 转化为历史感知策略，尤其在需要历史上下文的长 horizon 任务上展现显著提升。在 GR00T N1.5 之上，HAMLET 在历史依赖的真实任务上达到 76.4% 的平均成功率，超出基线 47.2%。此外，HAMLET 将 RoboCasa Kitchen（100 演示设置）上的先前最佳性能从 64.1% 推到 66.4%，将 LIBERO 从 95.6% 推到 97.7%，突显其在通用机器人操作基准上的有效性。

------

Title: ContextVLA: Vision-Language-Action Model with Amortized Multi-Frame Context

URL: https://doi.org/10.48550/arXiv.2510.04246

Abstract: Leveraging temporal context is crucial for success in partially observable robotic tasks. However, prior work in behavior cloning has demonstrated inconsistent performance gains when using multi-frame observations. In this paper, we introduce ContextVLA, a policy model that robustly improves robotic task performance by effectively leveraging multi-frame observations. Our approach is motivated by the key observation that Vision-Language-Action models (VLA), i.e., policy models built upon a Vision-Language Model (VLM), more effectively utilize multi-frame observations for action generation. This suggests that VLMs'inherent temporal understanding capability enables them to extract more meaningful context from multi-frame observations. However, the high dimensionality of video inputs introduces significant computational overhead, making VLA training and inference inefficient. To address this, ContextVLA compresses past observations into a single context token, allowing the policy to efficiently leverage temporal context for action generation. Our experiments show that ContextVLA consistently improves over single-frame VLAs and achieves the benefits of full multi-frame training but with reduced training and inference times.

中文翻译：利用时间上下文对部分可观察机器人任务的成功至关重要。然而，先前行为克隆工作在利用多帧观察时表现出不一致的性能收益。本文中，我们引入 ContextVLA，一种通过有效利用多帧观察来稳健提升机器人任务表现的策略模型。我们的方法受以下关键观察启发：构建在视觉-语言模型（VLM）之上的视觉-语言-动作模型（VLA）能更有效地利用多帧观察进行动作生成。这表明 VLM 固有的时间理解能力使其能够从多帧观察中提取更有意义的上下文。然而，视频输入的高维度引入了显著计算开销，使 VLA 训练和推理效率低下。为此，ContextVLA 将过去观察压缩为单个上下文 token，使策略能高效利用时间上下文进行动作生成。实验表明，ContextVLA 持续优于单帧 VLA，并实现了完全多帧训练的收益，但训练和推理时间更短。

------

Title: Cache-to-Cache: Direct Semantic Communication Between Large Language Models

URL: https://doi.org/10.48550/arXiv.2510.03215

Abstract: Multi-LLM systems harness the complementary strengths of diverse Large Language Models, achieving performance and efficiency gains that are not attainable by a single model. In existing designs, LLMs communicate through text, forcing internal representations to be transformed into output token sequences. This process both loses rich semantic information and incurs token-by-token generation latency. Motivated by these limitations, we ask: Can LLMs communicate beyond text? Oracle experiments show that enriching the KV-Cache semantics can improve response quality without increasing cache size, supporting KV-Cache as an effective medium for inter-model communication. Thus, we propose Cache-to-Cache (C2C), a new paradigm for direct semantic communication between LLMs. C2C uses a neural network to project and fuse the source model's KV-cache with that of the target model to enable direct semantic transfer. A learnable gating mechanism selects the target layers that benefit from cache communication. Compared with text communication, C2C utilizes the deep, specialized semantics from both models, while avoiding explicit intermediate text generation. Experiments show that C2C achieves 6.4-14.2% higher average accuracy than individual models. It further outperforms the text communication paradigm by approximately 3.1-5.4%, while delivering an average 2.5x speedup in latency. Our code is available at https://github.com/thu-nics/C2C.

中文翻译：多 LLM 系统利用不同大语言模型的互补优势，实现了单一模型无法企及的性能和效率提升。在现有设计中，LLM 通过文本通信，迫使内部表示被转换为输出 token 序列。这一过程既丢失了丰富的语义信息，又产生了逐 token 生成延迟。受这些局限性的驱动，我们提出：LLM 能否超越文本通信？Oracle 实验表明，丰富 KV cache 的语义可以在不增加缓存大小的情况下提升响应质量，支持 KV cache 作为模型间通信的有效媒介。因此，我们提出 Cache-to-Cache（C2C），一种 LLM 间直接语义通信的新范式。C2C 使用神经网络将源模型的 KV cache 投影并与目标模型的融合，以实现直接语义迁移。可学习的门控机制选择受益于缓存通信的目标层。与文本通信相比，C2C 利用了两个模型深层的专门语义，同时避免了显式的中间文本生成。实验表明，C2C 的平均准确率比单个模型高 6.4-14.2%，比文本通信范式高约 3.1-5.4%，同时延迟平均加速 2.5 倍。

------

Title: MA-LMM: Memory-Augmented Large Multimodal Model for Long-Term Video Understanding

URL: https://doi.org/10.1109/CVPR52733.2024.01282

Abstract: With the success of large language models (LLMs), integrating the vision model into LLMs to build vision-language foundation models has gained much more interest recently. However, existing LLM-based large multimodal models (e.g., Video-LLaMA, VideoChat) can only take in a limited number of frames for short video understanding. In this study, we mainly focus on designing an efficient and effective model for long-term video understanding. Instead of trying to process more frames simultaneously like most existing work, we propose to process videos in an online manner and store past video information in a memory bank. This allows our model to reference historical video content for long-term analysis without exceeding LLMs' context length constraints or GPU memory limits. Our memory bank can be seamlessly integrated into current multimodal LLMs in an off-the-shelf manner. We conduct extensive experiments on various video understanding tasks, such as long-video understanding, video question answering, and video captioning, and our model can achieve state-of-the-art performances across multiple datasets.

中文翻译：随着大语言模型（LLM）的成功，将视觉模型集成到 LLM 中以构建视觉-语言基础模型近来获得了更多关注。然而，现有的基于 LLM 的大多模态模型（如 Video-LLaMA、VideoChat）只能接受有限数量的帧进行短视频理解。本研究中，我们主要聚焦于设计一个高效的长视频理解模型。与大多数现有工作试图同时处理更多帧不同，我们提出以在线方式处理视频并将过去的视频信息存储在记忆库中。这使我们的模型能够在不超过 LLM 上下文长度约束或 GPU 内存限制的情况下参考历史视频内容进行长期分析。我们的记忆库可以以即插即用的方式无缝集成到当前多模态 LLM 中。我们在长视频理解、视频问答和视频描述等多种视频理解任务上进行了广泛实验，模型在多个数据集上达到了最先进性能。

------

Title: AstraNav-Memory: Contexts Compression for Long Memory

URL: https://doi.org/10.48550/arXiv.2512.21627

Abstract: Lifelong embodied navigation requires agents to accumulate, retain, and exploit spatial-semantic experience across tasks, enabling efficient exploration in novel environments and rapid goal reaching in familiar ones. While object-centric memory is interpretable, it depends on detection and reconstruction pipelines that limit robustness and scalability. We propose an image-centric memory framework that achieves long-term implicit memory via an efficient visual context compression module end-to-end coupled with a Qwen2.5-VL-based navigation policy. Built atop a ViT backbone with frozen DINOv3 features and lightweight PixelUnshuffle+Conv blocks, our visual tokenizer supports configurable compression rates; for example, under a representative 16$\times$ compression setting, each image is encoded with about 30 tokens, expanding the effective context capacity from tens to hundreds of images. Experimental results on GOAT-Bench and HM3D-OVON show that our method achieves state-of-the-art navigation performance, improving exploration in unfamiliar environments and shortening paths in familiar ones. Ablation studies further reveal that moderate compression provides the best balance between efficiency and accuracy. These findings position compressed image-centric memory as a practical and scalable interface for lifelong embodied agents, enabling them to reason over long visual histories and navigate with human-like efficiency.

中文翻译：终身具身导航要求 agent 跨任务积累、保留和利用空间语义经验，从而在新环境中高效探索，在熟悉环境中快速到达目标。虽然以对象为中心的记忆可解释，但依赖检测和重建流水线限制了鲁棒性和可扩展性。我们提出一种以图像为中心的记忆框架，通过与基于 Qwen2.5-VL 的导航策略端到端耦合的高效视觉上下文压缩模块实现长期隐式记忆。基于具有冻结 DINOv3 特征的 ViT 骨干和轻量 PixelUnshuffle+Conv 块，我们的视觉分词器支持可配置的压缩率；例如在 16 倍压缩代表性设置下，每张图像编码约 30 个 token，将有效上下文容量从数十张扩展到数百张图像。在 GOAT-Bench 和 HM3D-OVON 上的实验表明，我们的方法达到了最先进的导航性能，改善了不熟悉环境中的探索并缩短了熟悉环境中的路径。消融研究进一步揭示，适度压缩提供了效率与准确率之间的最佳平衡。这些发现将压缩图像中心记忆定位为终身具身 agent 实用且可扩展的接口，使其能够对长视觉历史进行推理并以类人效率导航。

------

Title: Streaming Long Video Understanding with Large Language Models

URL: https://doi.org/10.48550/arXiv.2405.16009

Abstract: This paper presents VideoStreaming, an advanced vision-language large model (VLLM) for video understanding, that capably understands arbitrary-length video with a constant number of video tokens streamingly encoded and adaptively selected. The challenge of video understanding in the vision language area mainly lies in the significant computational burden caused by the great number of tokens extracted from long videos. Previous works rely on sparse sampling or frame compression to reduce tokens. However, such approaches either disregard temporal information in a long time span or sacrifice spatial details, resulting in flawed compression. To address these limitations, our VideoStreaming has two core designs: Memory-Propagated Streaming Encoding and Adaptive Memory Selection. The Memory-Propagated Streaming Encoding architecture segments long videos into short clips and sequentially encodes each clip with a propagated memory. In each iteration, we utilize the encoded results of the preceding clip as historical memory, which is integrated with the current clip to distill a condensed representation that encapsulates the video content up to the current timestamp. After the encoding process, the Adaptive Memory Selection strategy selects a constant number of question-related memories from all the historical memories and feeds them into the LLM to generate informative responses. The question-related selection reduces redundancy within the memories, enabling efficient and precise video understanding. Meanwhile, the disentangled video extraction and reasoning design allows the LLM to answer different questions about a video by directly selecting corresponding memories, without the need to encode the whole video for each question. Our model achieves superior performance and higher efficiency on long video benchmarks, showcasing precise temporal comprehension for detailed question answering.

中文翻译：本文提出 VideoStreaming，一种用于视频理解的高级视觉-语言大模型（VLLM），能够以恒定数量的视频 token 流式编码和自适应选择来理解任意长度视频。视觉语言领域视频理解的挑战主要在于从长视频中提取的大量 token 造成的显著计算负担。先前工作依赖稀疏采样或帧压缩来减少 token，但这些方法要么忽略长时间跨度中的时间信息，要么牺牲空间细节，导致有缺陷的压缩。为解决这些局限，我们的 VideoStreaming 有两大核心设计：Memory-Propagated Streaming Encoding 和 Adaptive Memory Selection。Memory-Propagated Streaming Encoding 架构将长视频分割为短视频片段，通过传播的记忆依次编码每个片段。在每次迭代中，我们利用前一片段的编码结果作为历史记忆，与当前片段整合以蒸馏出浓缩表示，囊括截至当前时间戳的视频内容。编码过程后，Adaptive Memory Selection 策略从所有历史记忆中选择恒定数量的问题相关记忆，输入 LLM 生成有信息量的响应。问题相关选择减少了记忆中的冗余，实现了高效精确的视频理解。同时，解耦的视频提取和推理设计允许 LLM 通过直接选择相应记忆来回答关于同一视频的不同问题，无需为每个问题重新编码整个视频。我们的模型在长视频基准上达到了优越性能且效率更高，展现了精确的时间理解能力用于详细问答。

------

Title: Long Context Compression with Activation Beacon

URL: https://www.semanticscholar.org/paper/f69f494ab691481ec353da4be480b334fada6607

Abstract: Long context compression is a critical research problem due to its significance in reducing the high computational and memory costs associated with LLMs. In this paper, we propose Activation Beacon, a plug-in module for transformer-based LLMs that targets effective, efficient, and flexible compression of long contexts. To achieve this, our method introduces the following technical designs. 1) We directly compress the activations (i.e. keys and values at every layer), rather than leveraging soft prompts to relay information (which constitute a major bottleneck to encapsulate the complex information within long contexts). 2) We tailor the compression workflow, where each fine-grained input unit is progressively compressed, enabling high-quality compression and efficient computation during both training and inference. 3) We train the model through compression-based auto-regression, making full use of plain texts and instructional data to optimize the model's compression performance. 4) During training, we randomly sample a compression ratio at each step, teaching the model to support a wide range of compression configurations. Extensive evaluations are conducted on various long-context tasks whose lengths (e.g., 128K) may far exceed the maximum training length (20K), such as document understanding, few-shot learning, and Needle-in-a-Haystack. Whilst existing methods struggle to handle these challenging tasks, Activation Beacon maintains a comparable performance to the uncompressed baseline across various scenarios, achieving a 2x acceleration in inference time and an 8x reduction of memory costs for KV cache. Our data, model, and code have been released at \url{https://github.com/FlagOpen/FlagEmbedding/}.

中文翻译：长上下文压缩因对降低 LLM 高计算和内存成本的重要性而成为一个关键研究问题。本文中，我们提出 Activation Beacon，一种用于基于 Transformer 的 LLM 的插件模块，旨在对长上下文进行有效、高效和灵活的压缩。为实现这一目标，我们的方法引入了以下技术设计：1) 我们直接压缩激活（即每层的键和值），而非利用软提示来传递信息（后者构成封装长上下文中复杂信息的主要瓶颈）。2) 我们定制了压缩工作流，每个细粒度输入单元被逐步压缩，在训练和推理中实现高质量压缩和高效计算。3) 我们通过基于压缩的自回归训练模型，充分利用纯文本和指令数据优化模型的压缩性能。4) 训练中我们每步随机采样压缩比，使模型学会支持广泛的压缩配置。在长度（如 128K）可能远超最大训练长度（20K）的各种长上下文任务上进行了广泛评估，如文档理解、少样本学习和大海捞针。现有方法难以应对这些挑战性任务，而 Activation Beacon 在各种场景下保持了与无压缩基线相当的性能，实现了推理时间 2 倍加速和 KV cache 内存成本 8 倍降低。

------

Title: StreamMem: Query-Agnostic KV Cache Memory for Streaming Video Understanding

URL: https://doi.org/10.48550/arXiv.2508.15717

Abstract: Multimodal large language models (MLLMs) have made significant progress in visual-language reasoning, but their ability to efficiently handle long videos remains limited. Despite recent advances in long-context MLLMs, storing and attending to the key-value (KV) cache for long visual contexts incurs substantial memory and computational overhead. Existing visual compression methods require either encoding the entire visual context before compression or having access to the questions in advance, which is impractical for long video understanding and multi-turn conversational settings. In this work, we propose StreamMem, a query-agnostic KV cache memory mechanism for streaming video understanding. Specifically, StreamMem encodes new video frames in a streaming manner, compressing the KV cache using attention scores between visual tokens and generic query tokens, while maintaining a fixed-size KV memory to enable efficient question answering (QA) in memory-constrained, long-video scenarios. Evaluation on three long video understanding and two streaming video question answering benchmarks shows that StreamMem achieves state-of-the-art performance in query-agnostic KV cache compression and is competitive with query-aware compression approaches.

中文翻译：多模态大语言模型（MLLM）在视觉-语言推理方面取得了显著进展，但其高效处理长视频的能力仍然有限。尽管长上下文 MLLM 近期有所进展，但为长视觉上下文存储和关注 KV cache 带来了大量内存和计算开销。现有视觉压缩方法要么需要在压缩前编码整个视觉上下文，要么需要提前获取问题，这对长视频理解和多轮对话场景不实用。本文中，我们提出 StreamMem，一种用于流式视频理解的与查询无关的 KV cache 记忆机制。具体而言，StreamMem 以流式方式编码新视频帧，利用视觉 token 和通用查询 token 之间的注意力分数压缩 KV cache，同时保持固定大小的 KV 记忆，以在内存受限的长视频场景中实现高效问答。在三个长视频理解和两个流式视频问答基准上的评估表明，StreamMem 在查询无关的 KV cache 压缩方面达到最先进性能，且与查询感知压缩方法具有竞争力。

------

Title: Scaling the Long Video Understanding of Multimodal Large Language Models via Visual Memory Mechanism

URL: https://www.semanticscholar.org/paper/f1e226a807b3459caa7484a7f6540ae9df0040b8

Abstract: Long video understanding is a key challenge that plagues the advancement of \emph{Multimodal Large language Models} (MLLMs). In this paper, we study this problem from the perspective of visual memory mechanism, and proposed a novel and training-free approach, termed \emph{Flexible Memory} (\textbf{FlexMem}). In principle, FlexMem aims to mimic human behavior of video watching, \emph{i.e.}, continually watching video content and recalling the most relevant memory fragments to answer the question. In this way, FlexMem can help MLLMs achieve video understanding of infinite lengths, unlike previous methods that process all video information at once and have input upper-limit. Concretely, FlexMem first consider the visual KV caches as the memory sources, and realize the effective memory transfer and writing via a dual-pathway compression design. Afterwards, FlexMem also explores different memory reading strategies for the diverse video understanding tasks, including the popular streaming one. To validate FlexMem, we apply it to two popular video-MLLMs, and conduct extensive experiments on five long video and one streaming video task. The experimental results show that on \textbf{a single 3090 GPU}, our FlexMem can achieve obvious improvements than existing efficient video understanding methods and process more than \textbf{1k frames}, which also helps the base MLLMs achieve comparable or even better performance than SOTA MLLMs on some benchmarks, \emph{e.g.} , GPT-4o and Gemini-1.5 Pro.

中文翻译：长视频理解是困扰多模态大语言模型（MLLM）发展的关键挑战。本文中，我们从视觉记忆机制的角度研究此问题，提出了一种无需训练的新方法——Flexible Memory（FlexMem）。原则上，FlexMem 旨在模仿人类观看视频的行为：持续观看视频内容并回忆最相关的记忆片段来回答问题。通过这种方式，FlexMem 可以帮助 MLLM 实现无限长度的视频理解，不同于先前一次性处理所有视频信息且存在输入上限的方法。具体而言，FlexMem 首先将视觉 KV cache 视为记忆源，通过双路径压缩设计实现有效的记忆迁移和写入。随后，FlexMem 还为不同的视频理解任务探索了不同的记忆读取策略，包括流行的流式场景。为验证 FlexMem，我们将其应用于两种流行的视频 MLLM，在五个长视频和一个流式视频任务上进行了大量实验。结果表明，在单张 3090 GPU 上，FlexMem 相比现有高效视频理解方法可取得明显改进，并能处理超过 1K 帧，还帮助基础 MLLM 在某些基准上达到与 GPT-4o 和 Gemini-1.5 Pro 等 SOTA MLLM 相当甚至更好的性能。

------

Title: HERMES: KV Cache as Hierarchical Memory for Efficient Streaming Video Understanding

URL: https://doi.org/10.48550/arXiv.2601.14724

Abstract: Recent advancements in Multimodal Large Language Models (MLLMs) have demonstrated significant improvement in offline video understanding. However, extending these capabilities to streaming video inputs, remains challenging, as existing models struggle to simultaneously maintain stable understanding performance, real-time responses, and low GPU memory overhead. To address this challenge, we propose HERMES, a novel training-free architecture for real-time and accurate understanding of video streams. Based on a mechanistic attention investigation, we conceptualize KV cache as a hierarchical memory framework that encapsulates video information across multiple granularities. During inference, HERMES reuses a compact KV cache, enabling efficient streaming understanding under resource constraints. Notably, HERMES requires no auxiliary computations upon the arrival of user queries, thereby guaranteeing real-time responses for continuous video stream interactions, which achieves 10$\times$ faster TTFT compared to prior SOTA. Even when reducing video tokens by up to 68% compared with uniform sampling, HERMES achieves superior or comparable accuracy across all benchmarks, with up to 11.4% gains on streaming datasets.

中文翻译：多模态大语言模型（MLLM）的最新进展在离线视频理解方面展现了显著提升。然而，将这些能力扩展到流式视频输入仍然具有挑战性，因为现有模型难以同时保持稳定的理解性能、实时响应和低 GPU 内存开销。为应对这一挑战，我们提出 HERMES，一种无需训练的新型架构，用于实时精确理解视频流。基于对注意力机制的机制性研究，我们将 KV cache 概念化为一种层次化记忆框架，以多种粒度封装视频信息。推理时，HERMES 复用紧凑的 KV cache，在资源约束下实现高效的流式理解。值得注意的是，HERMES 在用户查询到达时无需辅助计算，从而保证连续视频流交互的实时响应，比先前 SOTA 快 10 倍 TTFT。即使与均匀采样相比将视频 token 减少高达 68%，HERMES 在所有基准上仍达到优越或相当精度，在流式数据集上最高提升 11.4%。

------

Title: XC-Cache: Cross-Attending to Cached Context for Efficient LLM Inference

URL: https://doi.org/10.48550/arXiv.2404.15420

Abstract: In-context learning (ICL) approaches typically leverage prompting to condition decoder-only language model generation on reference information. Just-in-time processing of a context is inefficient due to the quadratic cost of self-attention operations, and caching is desirable. However, caching transformer states can easily require almost as much space as the model parameters. When the right context isn't known in advance, caching ICL can be challenging. This work addresses these limitations by introducing models that, inspired by the encoder-decoder architecture, use cross-attention to condition generation on reference text without the prompt. More precisely, we leverage pre-trained decoder-only models and only train a small number of added layers. We use Question-Answering (QA) as a testbed to evaluate the ability of our models to perform conditional generation and observe that they outperform ICL, are comparable to fine-tuned prompted LLMs, and drastically reduce the space footprint relative to standard KV caching by two orders of magnitude.

中文翻译：上下文学习（ICL）方法通常利用提示来条件化解码器语言模型在参考信息上的生成。由于自注意力操作的二次成本，即时处理上下文效率低下，缓存是理想的。然而，缓存 Transformer 状态几乎需要与模型参数相当的空间。当正确的上下文事先未知时，缓存 ICL 可能具有挑战性。本文通过引入受编码器-解码器架构启发的模型来解决这些局限——使用交叉注意力在无提示的情况下条件化参考文本生成。具体而言，我们利用预训练的仅解码器模型，仅训练少量新增层。我们使用问答（QA）作为测试平台评估模型执行条件生成的能力，观察到它们优于 ICL，与微调提示 LLM 相当，并相对于标准 KV cache 将空间占用大幅降低两个数量级。

------

Title: Dejavu: Towards Experience Feedback Learning for Embodied Intelligence

URL: https://www.semanticscholar.org/paper/46cb65f10ff7410b4d1195ac22bda6a76f29784b

Abstract: Embodied agents face a fundamental limitation: once deployed in real-world environments, they cannot easily acquire new knowledge to improve task performance. In this paper, we propose Dejavu, a general post-deployment learning framework that augments a frozen Vision-Language-Action (VLA) policy with retrieved execution memories through an Experience Feedback Network (EFN). EFN identifies contextually relevant prior action experiences and conditions action prediction on the retrieved guidance. We train EFN with reinforcement learning and semantic similarity rewards, encouraging the predicted actions to align with past behaviors under the current observation. During deployment, EFN continually expands its memory with new trajectories, enabling the agent to exhibit ``learning from experience.''Experiments across diverse embodied tasks show that EFN improves adaptability, robustness, and success rates over frozen baselines. Our Project Page is https://dejavu2025.github.io/.

中文翻译：具身 agent 面临根本性限制：一旦部署到真实环境，它们难以获取新知识来改善任务性能。本文中，我们提出 Dejavu，一种通用的部署后学习框架，通过经验反馈网络（EFN）用检索到的执行记忆来增强冻结的视觉-语言-动作（VLA）策略。EFN 识别上下文相关的先前动作经验，并以检索到的指导来条件化动作预测。我们用强化学习和语义相似度奖励训练 EFN，鼓励预测动作在当前观察下与过去行为对齐。部署期间，EFN 持续用新轨迹扩展记忆，使 agent 展现"从经验中学习"的能力。跨多种具身任务的实验表明，EFN 在冻结基线上提升了适应性、鲁棒性和成功率。

------

Title: Generative Adapter: Contextualizing Language Models in Parameters with A Single Forward Pass

URL: https://doi.org/10.48550/arXiv.2411.05877

Abstract: Large language models (LMs) are typically adapted to improve performance on new contexts (\eg text prompts that define new tasks or domains) through fine-tuning or prompting. However, there is an accuracy compute tradeoff -- fine-tuning incurs significant training cost and prompting increases inference overhead. We introduce $GenerativeAdapter$, an effective and efficient adaptation method that directly maps new contexts to low-rank LM adapters, thereby significantly reducing inference overhead with no need for finetuning. The adapter generator is trained via self-supervised learning, and can be used to adapt a single frozen LM for any new task simply by mapping the associated task or domain context to a new adapter. We apply $GenerativeAdapter$ to two pretrained LMs (Mistral-7B-Instruct and Llama2-7B-Chat) and evaluate the adapted models in three adaption scenarios: knowledge acquisition from documents, learning from demonstrations, and personalization for users. In StreamingQA, our approach is effective in injecting knowledge into the LM's parameters, achieving a 63.5% improvement in F1 score over the model with supervised fine-tuning (from $19.5$ to $31.5$) for contexts as long as 32K tokens. In the MetaICL in-context learning evaluation, our method achieves an average accuracy of $44.9$ across 26 tasks, outperforming the base model. On MSC, our method proves to be highly competitive in memorizing user information from conversations with a 4x reduction in computation and memory costs compared to prompting with full conversation history. Together, these results suggest that $GenerativeAdapter$ should allow for general adaption to a wide range of different contexts.

中文翻译：大语言模型（LM）通常通过微调或提示来适应新上下文（如定义新任务或领域的文本提示）以提升性能。然而，存在准确率与计算的权衡——微调带来显著的训练成本，提示增加推理开销。我们引入 GenerativeAdapter，一种有效且高效的适配方法，直接将新上下文映射为低秩 LM 适配器，从而大幅降低推理开销且无需微调。适配器生成器通过自监督学习训练，可用于为任何新任务适配单个冻结 LM，只需将相关的任务或领域上下文映射为新适配器。我们将 GenerativeAdapter 应用于两个预训练 LM（Mistral-7B-Instruct 和 Llama2-7B-Chat），在三种适配场景中评估：从文档获取知识、从演示中学习和用户个性化。在 StreamingQA 中，我们的方法有效将知识注入 LM 参数，在长达 32K token 的上下文中 F1 分数比监督微调模型提升 63.5%（从 19.5 到 31.5）。在 MetaICL 上下文学习评估中，方法在 26 个任务上平均准确率 44.9，优于基础模型。在 MSC 上，方法在从对话记忆用户信息方面表现出高度竞争力，相比以完整对话历史为条件的提示，计算和内存成本降低 4 倍。这些结果表明 GenerativeAdapter 应能广泛适配各种不同上下文。

------

Title: Dolphin: Long Context as a New Modality for Energy-Efficient On-Device Language Models

URL: https://doi.org/10.48550/arXiv.2408.15518

Abstract: This paper presents Dolphin, a novel decoder-decoder architecture for energy-efficient processing of long contexts in language models. Our approach addresses the significant energy consumption and latency challenges inherent in on-device models. Dolphin employs a compact 0.5B parameter decoder to distill extensive contextual information into a memory embedding, substantially reducing the input length for the primary 7B parameter decoder model. Inspired by vision-language models, we repurpose the image embedding projector to encode long textual contexts, effectively treating extended context as a distinct modality. This innovative method enables processing of substantially longer contexts without the typical computational overhead associated with extended input sequences. Empirical evaluations demonstrate a 10-fold improvement in energy efficiency and a 5-fold reduction in latency compared to conventional full-length context processing methods without losing quality of the response. Our work contributes to the development of more sustainable and scalable language models for on-device applications, addressing the critical need for energy-efficient and responsive AI technologies in resource-constrained environments while maintaining the accuracy to understand long contexts. This research has implications for the broader field of natural language processing, particularly in the domain of efficient model design for resource-limited settings. By enabling more sophisticated AI capabilities on edge devices, Dolphin paves the way for advanced language processing in a wide range of applications where computational resources are at a premium. The Dolphin model is publicly available at https://huggingface.co/NexaAIDev/Dolphin.

中文翻译：本文提出 Dolphin，一种用于语言模型中长上下文能效处理的新型解码器-解码器架构。我们的方法解决了端侧模型中固有的显著能耗和延迟挑战。Dolphin 采用紧凑的 0.5B 参数解码器将大量上下文信息蒸馏为记忆嵌入，大幅缩短了主 7B 参数解码器模型的输入长度。受视觉-语言模型启发，我们重新利用图像嵌入投影器来编码长文本上下文，有效将扩展上下文视为独特模态。这一创新方法能够处理显著更长的上下文，而无需伴随扩展输入序列的典型计算开销。实验评估表明，与传统全长度上下文处理方法相比，能效提升 10 倍，延迟降低 5 倍，且不损失响应质量。我们的工作有助于为端侧应用开发更可持续和可扩展的语言模型，满足在资源受限环境中对能效高且响应迅速的 AI 技术的关键需求，同时保持理解长上下文的准确性。这项研究对自然语言处理更广泛领域具有启示意义，特别是在资源受限场景的高效模型设计领域。通过在边缘设备上实现更复杂的 AI 能力，Dolphin 为在计算资源有限的广泛应用中实现高级语言处理铺平了道路。

------

Title: VideoScan: Enabling Efficient Streaming Video Understanding via Frame-level Semantic Carriers

URL: https://doi.org/10.48550/arXiv.2503.09387

Abstract: This paper introduces VideoScan, an efficient vision-language model (VLM) inference framework designed for real-time video interaction that effectively comprehends and retains streamed video inputs while delivering rapid and accurate responses. A longstanding challenge in video understanding--particularly for long-term or real-time applications--stems from the substantial computational overhead caused by the extensive length of visual tokens. To address this, VideoScan employs a single semantic carrier token to represent each frame, progressively reducing computational and memory overhead during its two-phase inference process: prefilling and decoding. The embedding of the semantic carrier token is derived from an optimized aggregation of frame-level visual features, ensuring compact yet semantically rich representations. Critically, the corresponding key-value pairs are trained to retain contextual semantics from prior frames, enabling efficient memory management without sacrificing temporal coherence. During inference, the visual tokens of each frame are processed only once during the prefilling phase and subsequently discarded in the decoding stage, eliminating redundant computations. This design ensures efficient VLM inference even under stringent real-time constraints. Comprehensive experiments on diverse offline and online benchmarks demonstrate that LLaVA-Video, supported by our method, achieves up to $\sim 5\times$ and $1.29\times$ speedups compared to its original version and previous efficient streaming video understanding approaches, respectively. Crucially, these improvements are attained while maintaining competitive performance and ensuring stable GPU memory consumption (consistently $\sim 18$GB, independent of video duration).

中文翻译：本文介绍 VideoScan，一种高效的视觉-语言模型（VLM）推理框架，专为实时视频交互设计，能有效理解并保留流式视频输入，同时提供快速准确的响应。视频理解中长期存在的挑战——尤其对于长期或实时应用——源于大量视觉 token 带来的显著计算开销。为此，VideoScan 使用单个语义载体 token 表示每帧，在其两阶段推理过程（预填充和解码）中逐步降低计算和内存开销。语义载体 token 的嵌入来自帧级视觉特征的优化聚合，确保紧凑但语义丰富的表示。关键的是，相应的键值对被训练以保留前序帧的上下文语义，在不牺牲时间一致性的前提下实现高效内存管理。推理时，每帧的视觉 token 仅在预填充阶段处理一次，随后在解码阶段丢弃，消除了冗余计算。这一设计即使在严格实时约束下也确保了高效 VLM 推理。在多样化离线和在线基准上的全面实验表明，LLaVA-Video 在方法支持下，比其原始版本和先前的高效流式视频理解方法分别实现高达约 5 倍和 1.29 倍的加速。关键的是，这些改进在保持竞争性能且 GPU 内存消耗稳定（始终约 18GB，与视频时长无关）的情况下达成。

------

Title: CompLLM: Compression for Long Context Q&A

URL: https://doi.org/10.48550/arXiv.2509.19228

Abstract: Large Language Models (LLMs) face significant computational challenges when processing long contexts due to the quadratic complexity of self-attention. While soft context compression methods, which map input text to smaller latent representations, have shown promise, their real-world adoption is limited. Existing techniques typically compress the context as a single unit, which leads to quadratic compression complexity and an inability to reuse computations across queries with overlapping contexts. In this work, we introduce CompLLM, a soft compression technique designed for practical deployment. Instead of processing the context holistically, CompLLM divides it into segments and compresses each one independently. This simple design choice yields three critical properties: efficiency, as the compression step scales linearly with the context length; scalability, enabling models trained on short sequences (e.g., 1k tokens) to generalize to contexts of 100k tokens; and reusability, allowing compressed segments to be cached and reused across different queries. Our experiments show that with a 2x compression rate, at high context lengths CompLLM speeds up Time To First Token (TTFT) by up to 4x and reduces the KV cache size by 50%. Furthermore, CompLLM achieves performance comparable to that obtained with the uncompressed context, and even surpasses it on very long sequences, demonstrating its effectiveness and practical utility.

中文翻译：大语言模型（LLM）在长上下文处理中由于自注意力的二次复杂度面临显著的计算挑战。尽管将输入文本映射为更小隐式表示的软上下文压缩方法已展现前景，但其实际采用有限。现有技术通常将上下文作为单一单元压缩，导致二次压缩复杂度且无法在具有重叠上下文的查询间复用计算。本文中，我们引入 CompLLM，一种为实际部署设计的软压缩技术。CompLLM 不整体处理上下文，而是将其分为段并独立压缩每段。这一简单设计选择产生了三个关键特性：效率——压缩步骤随上下文长度线性扩展；可扩展性——使在短序列（如 1k token）上训练的模型能泛化到 100k token 的上下文；可复用性——允许压缩段被缓存并在不同查询间复用。实验表明，在 2 倍压缩率下，高上下文长度时 CompLLM 将首 token 时间（TTFT）加速高达 4 倍，并将 KV cache 大小减少 50%。此外，CompLLM 达到与无压缩上下文相当的性能，在极长序列上甚至超越，证明了其有效性和实际价值。

------

Title: Combee: Scaling Prompt Learning for Self-Improving Language Model Agents

URL: https://www.semanticscholar.org/paper/473b381d69441e1b49c89a6071ea6411a0c68ec2

Abstract: Recent advances in prompt learning allow large language model agents to acquire task-relevant knowledge from inference-time context without parameter changes. For example, existing methods (like ACE or GEPA) can learn system prompts to improve accuracy based on previous agent runs. However, these methods primarily focus on single-agent or low-parallelism settings. This fundamentally limits their ability to efficiently learn from a large set of collected agentic traces. It would be efficient and beneficial to run prompt learning in parallel to accommodate the growing trend of learning from many agentic traces or parallel agent executions. Yet without a principled strategy for scaling, current methods suffer from quality degradation with high parallelism. To improve both the efficiency and quality of prompt learning, we propose Combee, a novel framework to scale parallel prompt learning for self-improving agents. Combee speeds up learning and enables running many agents in parallel while learning from their aggregate traces without quality degradation. To achieve this, Combee leverages parallel scans and employs an augmented shuffle mechanism; Combee also introduces a dynamic batch size controller to balance quality and delay. Evaluations on AppWorld, Terminal-Bench, Formula, and FiNER demonstrate that Combee achieves up to 17x speedup over previous methods with comparable or better accuracy and equivalent cost.

中文翻译：提示学习的最新进展使大语言模型 agent 能够在无需参数变更的情况下从推理时上下文获取任务相关知识。例如，现有方法（如 ACE 或 GEPA）可以学习系统提示，基于先前的 agent 运行提升准确率。然而，这些方法主要关注单 agent 或低并行度设置，从根本上限制其从大量收集的 agent 轨迹中高效学习的能力。以并行方式运行提示学习，以适应从许多 agent 轨迹或并行 agent 执行中学习的增长趋势，将是高效和有益的。但在没有原则性扩展策略的情况下，当前方法在高并行度下质量下降。为同时提升提示学习的效率和质量，我们提出 Combee，一种扩展并行提示学习以支持自改进 agent 的新框架。Combee 加速学习，并支持在并行运行许多 agent 的同时从其聚合轨迹学习而无质量下降。为此，Combee 利用并行扫描并采用增强的洗牌机制；还引入动态批量大小控制器以平衡质量和延迟。在 AppWorld、Terminal-Bench、Formula 和 FiNER 上的评估表明，Combee 相比先前方法实现高达 17 倍加速，准确率相当或更好，成本相同。

------

Title: Latent Collaboration in Multi-Agent Systems

URL: https://doi.org/10.48550/arXiv.2511.20639

Abstract: Multi-agent systems (MAS) extend large language models (LLMs) from independent single-model reasoning to coordinative system-level intelligence. While existing LLM agents depend on text-based mediation for reasoning and communication, we take a step forward by enabling models to collaborate directly within the continuous latent space. We introduce LatentMAS, an end-to-end training-free framework that enables pure latent collaboration among LLM agents. In LatentMAS, each agent first performs auto-regressive latent thoughts generation through last-layer hidden embeddings. A shared latent working memory then preserves and transfers each agent's internal representations, ensuring lossless information exchange. We provide theoretical analyses establishing that LatentMAS attains higher expressiveness and lossless information preservation with substantially lower complexity than vanilla text-based MAS. In addition, empirical evaluations across 9 comprehensive benchmarks spanning math and science reasoning, commonsense understanding, and code generation show that LatentMAS consistently outperforms strong single-model and text-based MAS baselines, achieving up to 14.6% higher accuracy, reducing output token usage by 70.8%-83.7%, and providing 4x-4.3x faster end-to-end inference. These results demonstrate that our new latent collaboration framework enhances system-level reasoning quality while offering substantial efficiency gains without any additional training. Code and data are fully open-sourced at https://github.com/Gen-Verse/LatentMAS.

中文翻译：多 agent 系统（MAS）将大语言模型（LLM）从独立的单模型推理扩展到协调的系统级智能。现有 LLM agent 依赖基于文本的中介进行推理和通信，我们向前迈进一步，使模型能够在连续潜在空间中直接协作。我们引入 LatentMAS，一种无需端到端训练的框架，使 LLM agent 之间能够进行纯潜在协作。在 LatentMAS 中，每个 agent 首先通过最后一层隐藏嵌入进行自回归潜在思维生成。共享的潜在工作记忆随后保存和传输每个 agent 的内部表示，确保无损信息交换。我们提供理论分析，证明 LatentMAS 比普通的基于文本的 MAS 具有更高的表达能力和无损的信息保存，且复杂度显著更低。此外，跨数学和科学推理、常识理解和代码生成等 9 个综合基准的实证评估表明，LatentMAS 持续优于强单模型和基于文本的 MAS 基线，准确率提升高达 14.6%，输出 token 使用减少 70.8%-83.7%，端到端推理速度加速 4x-4.3x。这些结果表明我们的新型潜在协作框架在提升系统级推理质量的同时提供了显著的效率收益，无需任何额外训练。

------

Title: Accelerating Language Model Workflows with Prompt Choreography

URL: https://doi.org/10.48550/arXiv.2512.23049

Abstract: '
 Large language models are increasingly deployed in multi-agent workflows. We introduce Prompt Choreography, a framework that efficiently executes LLM workflows by maintaining a dynamic, global KV cache. Each LLM call can attend to an arbitrary, reordered subset of previously encoded messages. Parallel calls are supported. Though caching messages’ encodings sometimes gives different results from re-encoding them in a new context, we show in diverse settings that fine-tuning the LLM to work with the cache can help it mimic the original results. Prompt Choreography significantly reduces per-message latency (2.0–6.2× faster time-to-first-token) and achieves substantial end-to-end speedups (>2.2×) in some workflows dominated by redundant computation.

中文翻译：大语言模型越来越多地部署在多 agent 工作流中。我们引入 Prompt Choreography，一种通过维护动态全局 KV cache 高效执行 LLM 工作流的框架。每次 LLM 调用可以关注先前已编码消息的任意重排序子集，支持并行调用。尽管缓存消息编码有时会产生与在新上下文中重新编码不同的结果，我们在多样化设置中表明，微调 LLM 以适配缓存可以帮助其模仿原始结果。Prompt Choreography 显著降低了每消息延迟（TTFT 加速 2.0-6.2 倍），并在一些受冗余计算主导的工作流中实现了显著的端到端加速（>2.2 倍）。

------

Title: Learning to Compress Prompts with Gist Tokens

URL: https://doi.org/10.48550/arXiv.2304.08467

Abstract: Prompting is the primary way to utilize the multitask capabilities of language models (LMs), but prompts occupy valuable space in the input context window, and repeatedly encoding the same prompt is computationally inefficient. Finetuning and distillation methods allow for specialization of LMs without prompting, but require retraining the model for each task. To avoid this trade-off entirely, we present gisting, which trains an LM to compress prompts into smaller sets of"gist"tokens which can be cached and reused for compute efficiency. Gist models can be trained with no additional cost over standard instruction finetuning by simply modifying Transformer attention masks to encourage prompt compression. On decoder (LLaMA-7B) and encoder-decoder (FLAN-T5-XXL) LMs, gisting enables up to 26x compression of prompts, resulting in up to 40% FLOPs reductions, 4.2% wall time speedups, and storage savings, all with minimal loss in output quality.

中文翻译：提示是利用语言模型（LM）多任务能力的主要方式，但提示占用输入上下文窗口中的宝贵空间，且反复编码同一提示在计算上是低效的。微调和蒸馏方法允许 LM 专业化而无需提示，但要求为每个任务重新训练模型。为完全避免这一权衡，我们提出 gisting，训练 LM 将提示压缩为更小的"gist" token 集合，可缓存复用以提高计算效率。Gist 模型可以通过简单地修改 Transformer 注意力掩码以鼓励提示压缩，以不高于标准指令微调的额外成本进行训练。在解码器（LLaMA-7B）和编码器-解码器（FLAN-T5-XXL）LM 上，gisting 实现高达 26 倍提示压缩，带来最多 40% FLOPs 降低、4.2% 挂钟时间加速和存储节省，同时输出质量损失极小。

------

Title: RelayCaching: Accelerating LLM Collaboration via Decoding KV Cache Reuse

URL: https://www.semanticscholar.org/paper/dac0bf8e7a86c16963090f705c40d65203f38f2f

Abstract: The increasing complexity of AI tasks has shifted the paradigm from monolithic models toward multi-agent large language model (LLM) systems. However, these collaborative architectures introduce a critical bottleneck: redundant prefill computation for shared content generated by previous agents, which significantly increases KV cache memory usage and time-to-first-token (TTFT). While various KV cache methods have been proposed to mitigate prefill redundancy, they either fail to maintain accuracy on agent-generated outputs or exhibit low reuse rates due to rigid constraints. We present RelayCaching, a training-free inference method that directly reuses decoding phase KV caches from previous agents in subsequent prefill phases. Our key insight is that KV caches for identical content are highly consistent across phases, while prefix-induced deviations are sparse and localized within a limited range of layers and token positions. By selectively recomputing KV caches at these positions, RelayCaching preserves model accuracy with minimal overhead, yielding a superior accuracy-efficiency trade-off over existing methods. Experiments on diverse collaborative LLM tasks spanning mathematical reasoning, general knowledge, and code generation demonstrate that RelayCaching achieves over 80% KV cache reuse, reduces TTFT by up to $4.7\times$ compared to the standard pipeline, all with negligible accuracy degradation.

中文翻译：AI 任务日益增长的复杂性使范式从单体模型转向多 agent 大语言模型（LLM）系统。然而，这些协作架构引入了关键瓶颈：对先前 agent 生成的共享内容进行冗余预填充计算，显著增加了 KV cache 内存使用和首 token 时间（TTFT）。尽管提出了各种 KV cache 方法来缓解预填充冗余，但它们要么无法在 agent 生成的输出上保持准确率，要么因刚性约束而呈现低复用率。我们提出 RelayCaching，一种无需训练的推理方法，直接在后续预填充阶段复用先前 agent 的解码阶段 KV cache。我们核心洞察是，相同内容的 KV cache 跨阶段高度一致，而前缀诱导的偏差稀疏且局限在有限范围的层和 token 位置内。通过在这些位置选择性重计算 KV cache，RelayCaching 以最小开销保持模型准确率，在准确率-效率权衡上优于现有方法。跨数学推理、通用知识和代码生成等多样化协作 LLM 任务的实验表明，RelayCaching 实现超过 80% 的 KV cache 复用率，相比标准流水线 TTFT 降低高达 4.7 倍，且精度损失可忽略。

------

Title: video-SALMONN S: Streaming Audio-Visual LLMs Beyond Length Limits via Memory

URL: https://doi.org/10.48550/arXiv.2510.11129

Abstract: Continuous, high-frame-rate, high-resolution processing of long video streams is critical for future AI agents, yet current video-understanding LLMs struggle to scale. Offline, fixed-frame-number methods require the stream length to adapt frame rates; streaming methods constrain memory by merging or discarding tokens, losing information. We propose video-SALMONN S, a streaming audio-visual LLM that, to our knowledge, is the first to process 3-hour videos at 1 FPS and 360p resolution under a fixed memory budget. Our model introduces (i) a test-time-training (TTT) memory module that continually updates token representations to capture long-range dependencies by replacing token merging, and (ii) a prompt-dependent memory reader that selectively retrieves context-relevant content from fixed-size memory. The TTT module is optimised with a Hessian-free conjugate-gradient procedure (TTT_HF) for efficient adaptation. On long-video benchmarks (Video-MME, LVBench, VideoEvalPro), video-SALMONN S sustains high-quality understanding on multi-hour videos with 10k frames and 1M tokens. Our 8B-parameter model achieves 74.2% overall and 67.8% on the Video-MME long split, outperforming both offline and streaming baselines.

中文翻译：对长视频流的连续、高帧率、高分辨率处理对未来 AI agent 至关重要，但当前视频理解 LLM 难以扩展。离线固定帧数方法需要调整流长度以适应帧率；流式方法通过合并或丢弃 token 来约束内存，丢失信息。我们提出 video-SALMONN S，一种流式音视频 LLM，据我们所知是首个在固定内存预算下以 1 FPS 和 360p 分辨率处理 3 小时视频的模型。模型引入 (i) 测试时训练（TTT）记忆模块，持续更新 token 表示以捕获长距离依赖，替代 token 合并；(ii) 提示依赖的记忆读取器，从固定大小记忆中选择性检索上下文相关内容。TTT 模块通过 Hessian-free 共轭梯度过程（TTT_HF）优化以实现高效适配。在长视频基准（Video-MME、LVBench、VideoEvalPro）上，video-SALMONN S 在包含 10k 帧和 1M token 的数小时视频上保持了高质量理解。我们的 8B 参数模型在 Video-MME 长分割上达到 74.2% 总体和 67.8% 的准确率，优于离线和流式基线。

------

Title: Dynamic Long Context Reasoning over Compressed Memory via End-to-End Reinforcement Learning

URL: https://doi.org/10.48550/arXiv.2602.08382

Abstract: Large Language Models (LLMs) face significant challenges in long-context processing, including quadratic computational costs, information forgetting, and the context fragmentation inherent in retrieval-augmented generation (RAG). We propose a cognitively inspired framework for efficient long-context inference based on chunk-wise compression and selective memory recall, rather than processing all raw tokens. The framework segments long inputs into chunks and encodes each chunk into compressed memory representations using a learned compressor. A gating module dynamically selects relevant memory blocks, which are then iteratively processed by a reasoning module with an evolving working memory to solve downstream tasks. The compressor and reasoner are jointly optimized via end-to-end reinforcement learning, while the gating module is trained separately as a classifier. Experimental results show that the proposed method achieves competitive accuracy on multi-hop reasoning benchmarks such as RULER-HQA, extrapolates context length from 7K to 1.75M tokens, and offers a favorable accuracy-efficiency trade-off compared to strong long-context baselines. In particular, it achieves up to a 2 times reduction in peak GPU memory usage and a 6 times inference speedup over MemAgent.

中文翻译：大语言模型（LLM）在长上下文处理中面临显著挑战，包括二次计算成本、信息遗忘和检索增强生成（RAG）固有的上下文碎片化。我们提出一种受认知启发的框架，基于逐块压缩和选择性记忆召回进行高效长上下文推理，而非处理所有原始 token。该框架将长输入分割为块，使用学习的压缩器将每个块编码为压缩记忆表示。门控模块动态选择相关记忆块，然后由推理模块通过不断演化的进行迭代处理以解决下游任务。压缩器和推理器通过端到端强化学习联合优化，门控模块作为分类器单独训练。实验结果表明，该方法在 RULER-HQA 等多跳推理基准上达到竞争性准确率，将上下文长度从 7K 外推到 1.75M token，并在准确率-效率权衡上优于强长上下文基线。特别是，相比 MemAgent，峰值 GPU 内存使用减少高达 2 倍，推理加速 6 倍。

------

Title: PolarMem: A Training-Free Polarized Latent Graph Memory for Verifiable Multimodal Agents

URL: https://doi.org/10.48550/arXiv.2602.00415

Abstract: As multimodal agents evolve from passive observers to long-horizon decision-makers, they require memory systems that provide not just information availability but logical verifiability. A fundamental limitation of current architectures is the epistemic asymmetry inherent in probabilistic vision-language models and dense associative memories: they conflate semantic affinity with factual existence and structurally fail to encode negative constraints. To this end, we introduce PolarMem, a training-free Polarized Latent Graph Memory designed to ground agent reasoning in verifiable evidence. PolarMem transforms fuzzy perceptual likelihoods into discrete logical constraints through non-parametric distributional partitioning. Furthermore, it employs a polarized graph topology with orthogonal inhibitory connections to explicitly store verified negation as a primary cognitive state. At inference time, we enforce a logic-dominant retrieval paradigm, suppressing hallucinatory patterns that violate negative constraints. Extensive evaluation across eight frozen Vision--Language Models and six benchmarks demonstrates that PolarMem functions as a robust cognitive system, establishing a foundation for verifiable multimodal agents. Our code is available at https://github.com/czs-ict/PolarMem.

中文翻译：随着多模态 agent 从被动观察者演变为长 horizon 决策者，它们需要不仅提供信息可用性、而且提供逻辑可验证性的记忆系统。当前架构的一个根本局限在于概率视觉-语言模型和稠密关联记忆中固有的认知不对称性：它们将语义相似性与事实存在混为一谈，且在结构上无法编码否定约束。为此，我们引入 PolarMem，一种无需训练的极化潜在图记忆，旨在将 agent 推理建立在可验证的证据之上。PolarMem 通过非参数分布划分将模糊的感知似然性转化为离散逻辑约束。此外，它利用具有正交抑制连接的极化图拓扑，显式地将经过验证的否定作为初级认知状态存储。推理时，我们强制采用逻辑主导的检索范式，抑制违反否定约束的幻觉模式。在八个冻结的视觉-语言模型和六个基准上的广泛评估表明，PolarMem 作为鲁棒的认知系统运作，为可验证的多模态 agent 建立了基础。

------

Title: KV Packet: Recomputation-Free Context-Independent KV Caching for LLMs

URL: https://www.semanticscholar.org/paper/a0dc71aedf2a8af9df827b221bd79ad89a165f9a

Abstract: Large Language Models (LLMs) rely heavily on Key-Value (KV) caching to minimize inference latency. However, standard KV caches are context-dependent: reusing a cached document in a new context requires recomputing KV states to account for shifts in attention distribution. Existing solutions such as CacheBlend, EPIC, and SAM-KV mitigate this issue by selectively recomputing a subset of tokens; however, they still incur non-negligible computational overhead (FLOPs) and increased Time-to-First-Token (TTFT) latency. In this paper, we propose KV Packet, a recomputation-free cache reuse framework that treats cached documents as immutable ``packets''wrapped in light-weight trainable soft-token adapters, which are trained via self-supervised distillation to bridge context discontinuities. Experiments on Llama-3.1 and Qwen2.5 demonstrate that the proposed KV Packet method achieves near-zero FLOPs and lower TTFT than recomputation-based baselines, while retaining F1 scores comparable to those of the full recomputation baseline.

中文翻译：大语言模型（LLM）严重依赖键值（KV）缓存来最小化推理延迟。然而，标准 KV 缓存是上下文依赖的：在新上下文中复用缓存文档需要重计算 KV 状态以应对注意力分布的变化。现有解决方案如 CacheBlend、EPIC 和 SAM-KV 通过选择性重计算 token 子集来缓解此问题，但仍产生不可忽略的计算开销（FLOPs）和增加的首 token 时间（TTFT）延迟。本文中，我们提出 KV Packet，一种无需重计算的缓存复用框架，将缓存文档视为不可变的"数据包"，包裹在轻量可训练的软 token 适配器中，通过自监督蒸馏训练以桥接上下文不连续性。在 Llama-3.1 和 Qwen2.5 上的实验表明，KV Packet 方法相比基于重计算的基线实现了接近零 FLOPs 和更低的 TTFT，同时保持了与完全重计算基线相当的 F1 分数。

------

Title: Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices

URL: https://www.semanticscholar.org/paper/21f7432b421d87313a3d715fc7e1321fd679bd1e

Abstract: Multi-agent LLM systems on edge devices face a memory management problem: device RAM is too small to hold every agent's KV cache simultaneously. On Apple M4 Pro with 10.2 GB of cache budget, only 3 agents fit at 8K context in FP16. A 10-agent workflow must constantly evict and reload caches. Without persistence, every eviction forces a full re-prefill through the model -- 15.7 seconds per agent at 4K context. We address this by persisting each agent's KV cache to disk in 4-bit quantized format and reloading it directly into the attention layer, eliminating redundant O(n) prefill computation via direct cache restoration. The system comprises three components: a block pool providing per-agent isolated Q4 KV caches in safetensors format, a BatchQuantizedKVCache for concurrent inference over multiple agents'quantized caches, and cross-phase context injection that accumulates attention state across conversation phases without re-computation. Evaluated on three architectures (Gemma 3 12B, dense GQA, 48 layers; DeepSeek-Coder-V2-Lite 16B, MoE MLA, 27 layers; Llama 3.1 8B, dense GQA, 32 layers), cache restoration reduces time-to-first-token by up to 136x (Gemma: 22--136x at 4K--32K; DeepSeek: 11--76x at 4K--32K; Llama: 24--111x at 4K--16K; 3--10x at 1K). Q4 quantization fits 4x more agent contexts into fixed device memory than FP16. Perplexity measured with actual Q4 KV caches shows -0.7% for Gemma, +2.8% for Llama, and +3.0% for DeepSeek. Open-source at https://github.com/yshk-mxim/agent-memory

中文翻译：边缘设备上的多 agent LLM 系统面临内存管理问题：设备 RAM 太小，无法同时容纳每个 agent 的 KV 缓存。在具备 10.2 GB 缓存预算的 Apple M4 Pro 上，在 FP16 下 8K 上下文仅能容纳 3 个 agent。10 agent 工作流必须不断驱逐和重新加载缓存。没有持久化，每次驱逐强制通过模型进行完全重新预填充——在 4K 上下文下每个 agent 15.7 秒。我们通过将每个 agent 的 KV 缓存以 4 位量化格式持久化到磁盘，并将其直接重新加载到注意力层来解决此问题，通过直接缓存恢复消除冗余的 O(n) 预填充计算。系统包含三个组件：提供逐 agent 隔离的 Q4 KV 缓存（safetensors 格式）的块池、用于在多个 agent 的量化缓存上进行并发推理的 BatchQuantizedKVCache，以及跨对话阶段累积注意力状态而无需重计算的跨阶段上下文注入。在三种架构上评估（Gemma 3 12B、dense GQA、48 层；DeepSeek-Coder-V2-Lite 16B、MoE MLA、27 层；Llama 3.1 8B、dense GQA、32 层），缓存恢复将首 token 时间减少高达 136 倍（Gemma：在 4K-32K 下 22-136x；DeepSeek：在 4K-32K 下 11-76x；Llama：在 4K-16K 下 24-111x；在 1K 下 3-10x）。Q4 量化在固定设备内存中容纳的 agent 上下文比 FP16 多 4 倍。使用实际 Q4 KV 缓存测量的困惑度显示 Gemma -0.7%、Llama +2.8%、DeepSeek +3.0%。

------

Title: Memory3: Language Modeling with Explicit Memory

URL: https://doi.org/10.4208/jml.240708

Abstract: The training and inference of large language models (LLMs) are together a costly process that transports knowledge from raw data to meaningful computation. Inspired by the memory hierarchy of the human brain, we reduce this cost by equipping LLMs with explicit memory, a memory format cheaper than model parameters and text retrieval-augmented generation (RAG). Conceptually, with most of its knowledge externalized to explicit memories, the LLM can enjoy a smaller parameter size, training cost, and inference cost, all proportional to the amount of remaining"abstract knowledge". As a preliminary proof of concept, we train from scratch a 2.4B LLM, which achieves better performance than much larger LLMs as well as RAG models, and maintains higher decoding speed than RAG. The model is named $\text{Memory}^3$, since explicit memory is the third form of memory in LLMs after implicit memory (model parameters) and working memory (context key-values). We introduce a memory circuitry theory to support the externalization of knowledge, and present novel techniques including a memory sparsification mechanism that makes storage tractable and a two-stage pretraining scheme that facilitates memory formation.

中文翻译：大语言模型（LLM）的训练和推理共同构成将知识从原始数据传输到有意义计算的高成本过程。受人脑记忆层次结构启发，我们通过为 LLM 配备显式记忆来降低成本——一种比模型参数和文本检索增强生成（RAG）更便宜的記憶格式。概念上，在大部分知识外化到显式记忆后，LLM 可以享有更小的参数规模、训练成本和推理成本，均与剩余"抽象知识"量成比例。作为初步概念验证，我们从头训练了一个 2.4B 的 LLM，其性能优于更大的 LLM 和 RAG 模型，且保持比 RAG 更高的解码速度。模型被命名为 Memory³，因为显式记忆是 LLM 中继隐式记忆（模型参数）和工作记忆（上下文键值）之后的第三种记忆形式。我们引入记忆电路理论来支持知识外化，并提出包括使存储变得可操作的记忆稀疏化机制和促进记忆形成的两阶段预训练方案等新技术。

------

Title: KV Cache Steering for Controlling Frozen LLMs

URL: https://www.semanticscholar.org/paper/86b374ffbb5e7c56e4436027132d32ca306f8de6

Abstract: We propose cache steering, a lightweight method for implicit steering of language models via a one-shot intervention applied directly to the key-value cache. To validate its effectiveness, we apply cache steering to induce chain-of-thought reasoning in small language models. Our approach constructs steering vectors from reasoning traces, obtained either from teacher models (e.g., GPT-4o) or existing human annotations, that shift model behavior toward more explicit, multi-step reasoning without fine-tuning or prompt modifications. Experimental evaluations on diverse reasoning benchmarks demonstrate that cache steering improves both the qualitative structure of model reasoning and quantitative task performance. Additional experiments show that the method also scales to larger models and yields further gains on challenging datasets such as GPQA and MATH. Compared to prior activation steering techniques that require continuous interventions, our one-shot cache steering offers substantial advantages in terms of inference latency, hyperparameter stability, and ease of integration with existing inference APIs. Beyond mere reasoning induction, we show that cache steering enables controllable transfer of reasoning styles (e.g., stepwise, causal, analogical), making it a practical tool for behavior-level guidance of language models.

中文翻译：我们提出 cache steering，一种通过对 KV 缓存直接应用一次性干预的轻量隐式引导语言模型方法。为验证其有效性，我们将 cache steering 应用于在小型语言模型中诱导思维链推理。我们的方法从推理轨迹构建引导向量，这些轨迹从教师模型（如 GPT-4o）或现有人类标注中获得，将模型行为引向更显式的多步推理，无需微调或提示修改。在多样化推理基准上的实验评估表明，cache steering 改善了模型推理的定性结构和定量任务性能。额外实验表明，该方法在更大模型上也有效，并在 GPQA 和 MATH 等挑战性数据集上取得进一步收益。与需要持续干预的先前进激活引导技术相比，我们的一次性 cache steering 在推理延迟、超参数稳定性和与现有推理 API 集成便利性方面提供了显著优势。除了单纯的推理诱导外，我们展示 cache steering 能够实现推理风格（如逐步、因果、类比）的可控迁移，使其成为语言模型行为级引导的实用工具。

------

Title: Gated Memory Policy

URL: https://www.semanticscholar.org/paper/1a322e17cbf608264eb8d100f18da06a9f1b3bf5

Abstract: Robotic manipulation tasks exhibit varying memory requirements, ranging from Markovian tasks that require no memory to non-Markovian tasks that depend on historical information spanning single or multiple interaction trials. Surprisingly, simply extending observation histories of a visuomotor policy often leads to a significant performance drop due to distribution shift and overfitting. To address these issues, we propose Gated Memory Policy (GMP), a visuomotor policy that learns both when to recall memory and what to recall. To learn when to recall memory, GMP employs a learned memory gate mechanism that selectively activates history context only when necessary, improving robustness and reactivity. To learn what to recall efficiently, GMP introduces a lightweight cross-attention module that constructs effective latent memory representations. To further enhance robustness, GMP injects diffusion noise into historical actions, mitigating sensitivity to noisy or inaccurate histories during both training and inference. On our proposed non-Markovian benchmark MemMimic, GMP achieves a 30.1% average success rate improvement over long-history baselines, while maintaining competitive performance on Markovian tasks in RoboMimic. All code, data and in-the-wild deployment instructions are available on our project website https://gated-memory-policy.github.io/.

中文翻译：机器人操作任务表现出不同的记忆需求，从无需记忆的马尔科夫任务到依赖跨单次或多次交互试验的历史信息的非马尔科夫任务。令人惊讶的是，简单扩展视觉运动策略的观察历史往往由于分布偏移和过拟合导致显著的性能下降。为解决这些问题，我们提出 Gated Memory Policy（GMP），一种同时学习何时召回记忆和召回什么的视觉运动策略。为学习何时召回记忆，GMP 采用学到的记忆门机制，仅在必要时选择性激活历史上下文，提升鲁棒性和响应性。为高效学习召回什么，GMP 引入轻量交叉注意力模块构建有效的潜在记忆表示。为进一步增强鲁棒性，GMP 向历史动作注入扩散噪声，在训练和推理期间缓解对有噪或不准确历史的敏感性。在我们提出的非马尔科夫基准 MemMimic 上，GMP 相比长历史基线实现 30.1% 的平均成功率提升，同时在 RoboMimic 的马尔科夫任务上保持竞争性能。

------

Title: Chameleon: Episodic Memory for Long-Horizon Robotic Manipulation

URL: https://www.semanticscholar.org/paper/21a529a956771b0c5c07e254409ff2f361cd4262

Abstract: Robotic manipulation often requires memory: occlusion and state changes can make decision-time observations perceptually aliased, making action selection non-Markovian at the observation level because the same observation may arise from different interaction histories. Most embodied agents implement memory via semantically compressed traces and similarity-based retrieval, which discards disambiguating fine-grained perceptual cues and can return perceptually similar but decision-irrelevant episodes. Inspired by human episodic memory, we propose Chameleon, which writes geometry-grounded multimodal tokens to preserve disambiguating context and produces goal-directed recall through a differentiable memory stack. We also introduce Camo-Dataset, a real-robot UR5e dataset spanning episodic recall, spatial tracking, and sequential manipulation under perceptual aliasing. Across tasks, Chameleon consistently improves decision reliability and long-horizon control over strong baselines in perceptually confusable settings.

中文翻译：机器人操作通常需要记忆：遮挡和状态变化可能使决策时的观察在感知上混淆，使得动作选择在观察层面是非马尔科夫的——因为相同的观察可能来自不同的交互历史。大多数具身 agent 通过语义压缩轨迹和基于相似度的检索来实现记忆，这丢弃了可消除歧义的细粒度感知线索，并可能返回感知相似但决策无关的 episode。受人类情节记忆启发，我们提出 Chameleon，写入几何基础的的多模态 token 以保留可消除歧义的上下文，并通过可微分记忆栈产生目标导向的召回。我们还引入 Camo-Dataset，一个涵盖情节回忆、空间跟踪和感知混淆下顺序操作的真实 UR5e 机器人数据集。跨任务，Chameleon 在感知易混淆的设置中，始终改善了决策可靠性和长 horizon 控制，优于强基线。

------

Title: Memo: Training Memory-Efficient Embodied Agents with Reinforcement Learning

URL: https://doi.org/10.48550/arXiv.2510.19732

Abstract: To enable embodied agents to operate effectively over extended timeframes, it is crucial to develop models that form and access memories to stay contextualized in their environment. In the current paradigm of training transformer-based policies for embodied sequential decision-making tasks, visual inputs often overwhelm the context limits of transformers, while humans can maintain and utilize a lifetime of experience compressed as memories. Significant compression is possible in principle, as much of the input is irrelevant and can be abstracted. However, existing approaches predominantly focus on either recurrent models with fixed-size memory or transformers with full-context reliance. In this work, we propose Memo, a transformer-based architecture and training recipe for reinforcement learning (RL) on memory-intensive, long-horizon tasks. Memo incorporates the creation and retrieval of memory by interleaving periodic summarization tokens with the inputs of a model during training. We demonstrate Memo's effectiveness on a gridworld meta-RL benchmark and a multi-object navigation task in photo-realistic indoor settings. Memo outperforms naive long-context transformer baselines while being more compute and storage efficient. Additionally, Memo generalizes better to longer contexts at inference time and remains robust in streaming settings, where historical context must be truncated to fit inference constraints. Our code is available at: https://github.com/gunshi/memo.

中文翻译：为使具身 agent 能在长时间范围内有效运行，开发能够形成和访问记忆以保持环境上下文的模型至关重要。在训练用于具身序列决策任务的基于 Transformer 的策略的当前范式中，视觉输入往往压倒了 Transformer 的上下文限制，而人类可以维持和利用压缩为记忆的终身经验。显著压缩在原则上是可能的，因为大量输入无关且可被抽象。然而，现有方法主要关注具有固定大小记忆的循环模型或依赖全上下文的 Transformer。本文中，我们提出 Memo，一种用于记忆密集型长 horizon 任务强化学习（RL）的基于 Transformer 的架构和训练方法。Memo 通过在训练期间将周期性摘要 token 与模型输入交织来纳入记忆的创建和检索。我们在网格世界元 RL 基准和逼真室内多目标导航任务上展示了 Memo 的有效性。Memo 优于朴素的的长上下文 Transformer 基线，同时计算和存储效率更高。此外，Memo 在推理时对更长上下文泛化更好，并在历史上下文必须截断以适应推理约束的流式设置中保持鲁棒性。

------

Title: EpiCache: Episodic KV Cache Management for Long Conversational Question Answering

URL: https://doi.org/10.48550/arXiv.2509.17396

Abstract: Modern large language models (LLMs) extend context lengths to millions of tokens, enabling coherent, personalized responses grounded in long conversational histories. This ability, however, hinges on Key-Value (KV) caching, whose memory grows linearly with dialogue length and quickly becomes the bottleneck in resource-constrained environments. An active line of research for reducing memory bottleneck is KV cache compression, which seeks to limit cache size while preserving accuracy. Yet existing methods face two major limitations: (i) evicting the KV cache after full-context prefill causes unbounded peak memory, and (ii) query-dependent eviction narrows the cache to a single query, leading to failure cases in multi-turn conversations. We introduce EpiCache, a training-free KV cache management framework for long conversational question answering (LongConvQA) under fixed memory budgets. EpiCache bounds cache growth through block-wise prefill and preserves topic-relevant context via episodic KV compression, which clusters conversation history into coherent episodes and applies episode-specific KV cache eviction. We further design an adaptive layer-wise budget allocation strategy that measures each layer's sensitivity to eviction and distributes the memory budget across layers accordingly. Across three LongConvQA benchmarks, EpiCache improves accuracy by up to 40%, maintains near-full KV accuracy under 4-6x compression, and reduces latency/memory by up to 2.4x/3.5x, enabling efficient multi-turn interaction under strict resource limits. Our code is available at https://github.com/apple/ml-epicache.

中文翻译：现代大语言模型（LLM）将上下文长度扩展到数百万 token，使基于长对话历史的连贯、个性化响应成为可能。然而，这一能力依赖键值（KV）缓存，其内存随对话长度线性增长，在资源受限环境中迅速成为瓶颈。一条活跃的降低内存瓶颈的研究路线是 KV 缓存压缩，旨在在保持准确率的同时限制缓存大小。但现有方法面临两个主要局限：(i) 在全上下文预填充后驱逐 KV 缓存导致无界峰值内存；(ii) 查询依赖的驱逐将缓存窄化到单一查询，在多轮对话中导致失败案例。我们引入 EpiCache，一种固定内存预算下用于长对话问答（LongConvQA）的无需训练的 KV 缓存管理框架。EpiCache 通过逐块预填充限制缓存增长，通过情节式 KV 压缩保持主题相关上下文——将对话历史聚类为连贯情节并对每个情节应用情节特定的 KV 缓存驱逐。我们进一步设计了一种自适应逐层预算分配策略，测量每层对驱逐的敏感度并据此在各层间分配内存预算。跨三个 LongConvQA 基准，EpiCache 将准确率提升高达 40%，在 4-6 倍压缩下保持接近全 KV 准确率，延迟/内存降低高达 2.4x/3.5x，在严格资源限制下实现高效多轮交互。

------

Title: ELMUR: External Layer Memory with Update/Rewrite for Long-Horizon RL

URL: https://doi.org/10.48550/arXiv.2510.07151

Abstract: Real-world robotic agents must act under partial observability and long horizons, where key cues may appear long before they affect decision making. However, most modern approaches rely solely on instantaneous information, without incorporating insights from the past. Standard recurrent or transformer models struggle with retaining and leveraging long-term dependencies: context windows truncate history, while naive memory extensions fail under scale and sparsity. We propose ELMUR (External Layer Memory with Update/Rewrite), a transformer architecture with structured external memory. Each layer maintains memory embeddings, interacts with them via bidirectional cross-attention, and updates them through an Least Recently Used (LRU) memory module using replacement or convex blending. ELMUR extends effective horizons up to 100,000 times beyond the attention window and achieves a 100% success rate on a synthetic T-Maze task with corridors up to one million steps. In POPGym, it outperforms baselines on more than half of the tasks. On MIKASA-Robo sparse-reward manipulation tasks with visual observations, it nearly doubles the performance of strong baselines, achieving the best success rate on 21 out of 23 tasks and improving the aggregate success rate across all tasks by about 70% over the previous best baseline. These results demonstrate that structured, layer-local external memory offers a simple and scalable approach to decision making under partial observability. Code and project page: https://elmur-paper.github.io/.

中文翻译：真实世界的机器人 agent 必须在部分可观察和长 horizon 下行动，其中关键线索可能在影响决策之前很久就已出现。然而，大多数现代方法仅依赖即时信息，不融入过去的洞见。标准循环或 Transformer 模型在保留和利用长期依赖方面存在困难：上下文窗口截断历史，而朴素的记忆扩展在规模和稀疏性下失败。我们提出 ELMUR（External Layer Memory with Update/Rewrite），一种具有结构化外部记忆的 Transformer 架构。每层维护记忆嵌入，通过双向交叉注意力与其交互，并通过使用替换或凸混合的 LRU 记忆模块更新它们。ELMUR 将有效 horizon 扩展到注意力窗口的 100,000 倍之外，在长达百万步走廊的合成 T-Maze 任务上实现 100% 成功率。在 POPGym 中，其在超过一半任务上优于基线。在 MIKASA-Robo 的稀疏奖励操作任务（含视觉观察）上，它将强基线性能几乎翻倍，在 23 个任务中的 21 个上达到最佳成功率，所有任务聚合成功率比先前最佳基线提升约 70%。这些结果表明，结构化的逐层局部外部记忆为部分可观察下的决策提供了一种简单且可扩展的方法。

------

Title: Locas: Your Models are Principled Initializers of Locally-Supported Parametric Memories

URL: https://doi.org/10.48550/arXiv.2602.05085

Abstract: In this paper, we aim to bridge test-time-training with a new type of parametric memory that can be flexibly offloaded from or merged into model parameters. We present Locas, a Locally-Supported parametric memory that shares the design of FFN blocks in modern transformers, allowing it to be flexibly permanentized into the model parameters while supporting efficient continual learning. We discuss two major variants of Locas: one with a conventional two-layer MLP design that has a clearer theoretical guarantee; the other one shares the same GLU-FFN structure with SOTA LLMs, and can be easily attached to existing models for both parameter-efficient and computation-efficient continual learning. Crucially, we show that proper initialization of such low-rank sideway-FFN-style memories -- performed in a principled way by reusing model parameters, activations and/or gradients -- is essential for fast convergence, improved generalization, and catastrophic forgetting prevention. We validate the proposed memory mechanism on the PG-19 whole-book language modeling and LoCoMo long-context dialogue question answering tasks. With only 0.02\% additional parameters in the lowest case, Locas-GLU is capable of storing the information from past context while maintaining a much smaller context window. In addition, we also test the model's general capability loss after memorizing the whole book with Locas, through comparative MMLU evaluation. Results show the promising ability of Locas to permanentize past context into parametric knowledge with minimized catastrophic forgetting of the model's existing internal knowledge.

------

中文翻译：本文旨在将测试时训练与一种新型参数化记忆桥接，这种记忆可以灵活地从模型参数卸载或合并到模型参数中。我们提出 Locas，一种局部支持的参数化记忆，共享现代 Transformer 中 FFN 块的设计，使其可以灵活地永久化到模型参数中，同时支持高效的持续学习。我们讨论了两种主要的 Locas 变体：一种采用常规两层 MLP 设计，具有更清晰的理论保证；另一种共享与 SOTA LLM 相同的 GLU-FFN 结构，可轻松附着于现有模型，实现参数高效和计算高效的持续学习。关键的是，我们表明，对此类低秩侧旁 FFN 风格记忆的恰当初始化——以原则性方式通过复用模型参数、激活和/或梯度进行——对于快速收敛、改善泛化和防止灾难性遗忘至关重要。我们在 PG-19 全书语言建模和 LoCoMo 长对话问答任务上验证了所提出的记忆机制。在最低仅 0.02% 额外参数的情况下，Locas-GLU 能够存储过去上下文的信息，同时维持小得多的上下文窗口。此外，我们还通过对比 MMLU 评估测试了使用 Locas 记忆全书后模型的通用能力损失。结果表明，Locas 有望将过去上下文永久化到参数化知识中，同时将模型现有内部知识的灾难性遗忘最小化。