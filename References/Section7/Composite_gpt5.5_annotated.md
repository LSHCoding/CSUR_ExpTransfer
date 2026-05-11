[Title]: BAGEL: Bootstrapping Agents by Guiding Exploration with Language
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: 随机探索轨迹或合成指令
- [Target Experience]: 可检索的 BAGEL demonstrations / refined trajectories
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {teacher}
- [Utilization]: 作为 retrieved demonstrations 通过 in-context learning 适配 zero-shot LM agent
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: LM labeler 将轨迹转成 synthetic instruction，zero-shot LM agent 再把 synthetic instruction 转成 refined trajectory；多轮 round-trip 把初始探索分布转成更能被自然语言描述和检索复用的 demonstration 库。

[Title]: OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis
- [Pathway]: Policy → Narrative → Policy (P7, P5)
- [Source Experience]: GUI agent 在环境中先感知并 step-wise interaction 得到的 trajectories
- [Target Experience]: high-quality GUI trajectory data and trained GUI agents
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: 生成的 trajectories 用于训练 GUI agents，trajectory reward model 用于质量筛选
- [Method]: ⟨hybrid⟩
- [Mechanism]: Stage 1 对应 P7：现有 GUI agent 先探索环境并产生轨迹，再 retrospectively derive tasks；Stage 2 对应 P5：经 trajectory reward model 过滤后的高质量轨迹被用作 GUI agent training data。

[Title]: AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling
- [Pathway]: Narrative → Narrative → Policy (P1, P5)
- [Source Experience]: discarded failed natural-language agent trajectories
- [Target Experience]: relabeled SFT, DPO, and ShareGPT training data and improved agents
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: relabeled data 被打包为 SFT、DPO 和 ShareGPT 训练样本，并在 iterative redeployment 中继续复用
- [Method]: ⟨hybrid⟩
- [Mechanism]: Stage 1 对应 P1：失败轨迹经过 failure classification、outcome extraction、LLM-guided prompt relabeling 和 confidence gating，被改写为可达成替代目标的正样本；Stage 2 对应 P5：这些 relabeled demonstrations 作为 SFT/DPO 训练信号更新 agent policy。

[Title]: Sample-Efficient Online Learning in LM Agents via Hindsight Trajectory Rewriting
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: failed attempts and past interaction trajectories
- [Target Experience]: optimized trajectories for alternative goals and compressed trajectory representations in memory
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: compressed trajectory representations 被维护在 memory 中，用于 novel environments 中更快适配
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: hindsight rule 让 LM 从失败尝试中识别可达成的 subgoals，并生成 counterfactual optimized trajectories；update rule 再将这些轨迹压缩成 memory representation，用于后续在线决策。

[Title]: Autonomous Evaluation and Refinement of Digital Agents
- [Pathway]: Evaluator → Policy (P6)
- [Source Experience]: domain-general automatic evaluators 对 web navigation 和 device control agent 行为的评价信号
- [Target Experience]: fine-tuned or inference-guided digital agents
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: 不清楚
- [Utilization]: evaluator outputs 用于 fine-tuning 和 inference-time guidance，以提升现有 agent performance
- [Method]: ⟨hybrid⟩
- [Mechanism]: 自动 evaluator 先在多个 digital-agent benchmark 中验证与 oracle metrics 的一致性，再作为评价信号驱动 agent refinement；摘要未说明 evaluator 本身如何由轨迹训练得到，因此只标注 evaluator-to-policy 利用阶段。

[Title]: UI-Genie: A Self-Improving Approach for Iteratively Boosting MLLM-based Mobile GUI Agents
- [Pathway]: Narrative → Evaluator → Policy (P4, P6)
- [Source Experience]: historical GUI contexts, rule-based verification signals, corrupted trajectories, hard negatives, and synthetic GUI trajectories
- [Target Experience]: UI-Genie-RM reward model and improved UI-Genie agent models
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {teacher}
- [Utilization]: reward model 提供 action-level 和 task-level rewards，支撑 reward-guided exploration、outcome verification 和 agent/RM 多代 self-improvement
- [Method]: ⟨hybrid⟩
- [Mechanism]: Stage 1 对应 P4：通过规则验证、controlled corruption 和 hard negative mining 构造 reward-specific GUI 数据训练 UI-Genie-RM；Stage 2 对应 P6：reward model 在动态环境中指导探索和验证，生成 UI-Genie-Agent 数据并提升 agent policy。

[Title]: GAIA: A Data Flywheel System for Training GUI Test-Time Scaling Critic Models
- [Pathway]: Policy → Narrative → Evaluator (P7, P4)
- [Source Experience]: base GUI agent 产生的 positive and negative action examples
- [Target Experience]: iterative GUI action critic models
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: critic 在 test-time scaling 中选择更高成功概率的 GUI operations，并继续收集 refined positive/negative samples
- [Method]: ⟨hybrid⟩
- [Mechanism]: Stage 1 对应 P7：base agent 的操作样本被外化为正负 action examples；Stage 2 对应 P4：这些样本训练 Intuitive Critic Model，critic 再指导 agent 产生新样本并训练下一轮 critic，形成 data flywheel。

[Title]: MagicGUI-RMS: A Multi-Agent Reward Model System for Self-Evolving GUI Agents via Automated Feedback Reflux
- [Pathway]: Narrative → Evaluator → Policy (P4, P6)
- [Source Experience]: GUI agent trajectories and automatically constructed balanced reward datasets
- [Target Experience]: DS-RM / GP-RM reward model system and self-evolving GUI agent behavior
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {teacher}
- [Utilization]: reward model system 进行 trajectory evaluation、corrective feedback 和 automated data-reflux，驱动 agent 行为持续增强
- [Method]: ⟨hybrid⟩
- [Mechanism]: Stage 1 对应 P4：结构化数据构造管线把 GUI trajectories 转成 reward learning datasets，训练 domain-specific 与 general-purpose RMs；Stage 2 对应 P6：RMS 在执行中识别错误动作、提出替代动作并通过 feedback reflux 更新 agent behavior。

[Title]: Watch Every Step! LLM Agent Learning via Iterative Step-level Process Refinement
- [Pathway]: Narrative → Narrative → Policy (P1, P5)
- [Source Experience]: expert trajectories, agent-generated exploratory actions, and step-level rewards
- [Target Experience]: contrastive action pairs and trained LLM agents
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {human}
- [Utilization]: contrastive action pairs 作为 agent training data，补充 outcome-only supervision 缺失的 process signal
- [Method]: ⟨hybrid⟩
- [Mechanism]: Stage 1 对应 P1：agent 沿 expert trajectory 探索并生成新动作，Monte Carlo step-level reward 与专家步骤比较后定位 discrepancy，形成 contrastive action pairs；Stage 2 对应 P5：这些 process-refined pairs 被用于训练 agent policy。

[Title]: Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training
- [Pathway]: Policy → Narrative → Policy (P7, P5)
- [Source Experience]: failed trajectories, MCTS tree paths, and current actor model error localization
- [Target Experience]: reflection-oriented correction trajectories and self-trained language agent
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 构造出的 recovery training data 用于 iterative self-training，使 agent 学会及时发现并纠正错误动作
- [Method]: ⟨MCTS⟩, ⟨SFT⟩
- [Mechanism]: Stage 1 对应 P7：当前 actor 和 MCTS 生成错误轨迹、正确相邻路径和 error-step signals；Stage 2 对应 P5：从首个错误步骤开始拼接相邻正确路径，得到可训练的 critique/correction 数据，并迭代更新模型恢复能力。

[Title]: Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents
- [Pathway]: Policy → Narrative → Policy (P7, P5)
- [Source Experience]: environment exploration failures and contrastive trajectory pairs
- [Target Experience]: DPO-updated LLM agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: trajectory preference pairs 用于 DPO-style contrastive policy update，并通过 exploration-training cycle 持续改进 agent
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: Stage 1 对应 P7：agent 与环境交互收集失败轨迹，并与较优轨迹形成 preference pairs；Stage 2 对应 P5：DPO/contrastive learning 将这些偏好经验内化到 open LLM agent policy 中。

[Title]: OpenWebVoyager: Building Multimodal Web Agents via Iterative Real-World Exploration, Feedback and Optimization
- [Pathway]: Policy → Narrative → Policy (P7, P5)
- [Source Experience]: real-world web exploration trajectories and feedback judged by a general-purpose model
- [Target Experience]: improved multimodal web agent policy
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: judged well-performing trajectories are used to optimize the policy over multiple exploration-feedback-optimization iterations
- [Method]: ⟨SFT⟩
- [Mechanism]: base model 先通过 imitation learning 获得基础能力；之后每轮由 agent 探索 open web 产生轨迹，general-purpose model 评价轨迹质量，优质轨迹再用于 policy improvement，构成 P7 到 P5 的循环。

[Title]: OS-Copilot: Towards Generalist Computer Agents with Self-Improvement
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: previous computer-task experiences in web, terminals, files, multimedia, and applications
- [Target Experience]: accumulated skills for FRIDAY
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: accumulated skills are reused to generalize to unseen OS applications and self-improve on Excel and PowerPoint tasks
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 摘要只说明 FRIDAY 通过 previous tasks 积累 skills 并在 general computer tasks 中复用，未细化 skill 表示；按“经验轨迹到可复用技能”的主贡献标注为 P2，但具体抽取规则为不清楚。

[Title]: STeCa: Step-level Trajectory Calibration for LLM Agent Learning
- [Pathway]: Narrative → Narrative → Policy (P1, P5)
- [Source Experience]: exploratory trajectories with step-level reward comparisons
- [Target Experience]: calibrated trajectories and reinforced LLM agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: calibrated trajectories and successful trajectories are used for reinforced training
- [Method]: ⟨hybrid⟩
- [Mechanism]: Stage 1 对应 P1：step-level reward comparison 在探索中识别 suboptimal actions，LLM-driven reflection 将它们改写为 calibrated trajectories；Stage 2 对应 P5：calibrated trajectories 与 successful trajectories 共同作为 reinforced training 信号。

[Title]: UI-Evol: Automatic Knowledge Evolving for Computer Use Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: actual agent-environment interactions and external GUI knowledge references
- [Target Experience]: evolved GUI knowledge with faithful objective action sequences and critiques
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: plug-and-play evolved knowledge is used to improve computer-use task execution and reliability
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Retrace Stage 从真实交互中抽取 objective action sequences，Critique Stage 将这些执行序列与外部参考知识比较，修正 retrieved knowledge 与实际执行之间的 gap；输出仍是可读的 GUI task knowledge。

[Title]: GUI-Reflection: Empowering Multimodal GUI Models with Self-Reflection Behavior
- [Pathway]: Narrative → Narrative → Policy (P1, P5)
- [Source Experience]: existing successful GUI trajectories and online GUI interaction data
- [Target Experience]: reflection/error-correction data and reflection-tuned multimodal GUI models
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {teacher}
- [Utilization]: reflection and error-correction data support offline SFT and iterative online reflection tuning
- [Method]: ⟨SFT⟩, ⟨hybrid⟩
- [Mechanism]: Stage 1 对应 P1：自动数据管线从 successful trajectories 构造 reflection/correction 样本；Stage 2 对应 P5：GUI-specific pretraining、offline SFT 与 online reflection tuning 把这些行为模式内化到 end-to-end multimodal GUI model。

[Title]: Scalable Data Synthesis for Computer Use Agents with Step-Level Filtering
- [Pathway]: Policy → Narrative → Policy (P7, P5)
- [Source Experience]: noisy CUA rollouts from a strong computer-use model
- [Target Experience]: WebSTAR reasoning-rich trajectories and SFT-trained Qwen-VL CUA models
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}
- [Utilization]: filtered trajectories are used for supervised finetuning; graded step-level actions also train StepRM as a secondary evaluator branch
- [Method]: ⟨SFT⟩
- [Mechanism]: Stage 1 对应 P7：teacher CUA rollouts 外化为大量 GUI trajectories；Stage 2 对应 P1/P5：step-level filtering 保留正确步骤并补充 reasoning augmentation，形成 WebSTAR 后对 CUA policy 做 SFT；另有 Narrative → Evaluator 分支训练 StepRM。

[Title]: Self-Improving Vision-Language-Action Models with Data Generation via Residual RL
- [Pathway]: Policy → Narrative → Policy (P7, P5)
- [Source Experience]: residual actor probing trajectories in VLA failure regions
- [Target Experience]: curated deployment-aligned trajectories and improved VLA generalist
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: curated recovery trajectories are distilled back into the VLA generalist with standard SFT
- [Method]: ⟨hybrid⟩
- [Mechanism]: Stage 1 对应 P7：lightweight residual actors 以 RL 探测 VLA failure regions 并收集 recovery-oriented trajectories；Stage 2 对应 P5：hybrid rollout 和 distribution-aware replay 筛选部署分布一致的数据，再用 SFT 蒸馏回 VLA。

[Title]: Mobile-Agent-v3: Fundamental Agents for GUI Automation
- [Pathway]: Policy → Narrative → Policy (P7, P5)
- [Source Experience]: self-evolving GUI trajectories from virtual Android, Ubuntu, macOS, and Windows environments
- [Target Experience]: GUI-Owl / Mobile-Agent-v3 policy models
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {teacher}
- [Utilization]: generated and validated interaction data supports end-to-end GUI training and scalable environment RL
- [Method]: ⟨hybrid⟩
- [Mechanism]: Stage 1 对应 P7：Self-Evolving GUI Trajectory Production 在多平台虚拟环境中自动生成 query、验证正确性并迭代 refine trajectories；Stage 2 对应 P5：这些轨迹与异步 RL/TRPO-style online training 共同更新 GUI agent policy。

[Title]: ANCHOR: Branch-Point Data Generation for GUI Agents
- [Pathway]: Narrative → Narrative → Policy (P1, P5)
- [Source Experience]: verified seed GUI demonstrations and post-branch GUI execution traces
- [Target Experience]: expanded desktop supervision corpus and fine-tuned GUI agents
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {human}, {self}
- [Utilization]: expanded and filtered corpus is used for supervised GUI-agent finetuning
- [Method]: ⟨SFT⟩
- [Mechanism]: Stage 1 对应 P1：从 seed demos 中识别 branch points，基于当前 GUI state 生成 task variants，再由执行 agent 生成新轨迹并由 verifier 检查；Stage 2 对应 P5：task-conditioned step-level filtering 与 denoising 后的 corpus 用于训练 GUI policy。

[Title]: LLMs as Scalable, General-Purpose Simulators For Evolving Digital Agent Training
- [Pathway]: Policy → Narrative → Policy (P7, P5)
- [Source Experience]: LLM-simulated structured UI states, transitions, guided rollouts, and trajectory variants
- [Target Experience]: synthetic UI trajectories and trained digital agents
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}
- [Utilization]: synthesized trajectories train web and Android agents; UI-Simulator-Grow prioritizes high-impact tasks for targeted scaling
- [Method]: ⟨SFT⟩
- [Mechanism]: Stage 1 对应 P7：LLM simulator 生成 UI states/transitions 并通过 guided rollout 包装为 coherent trajectories；Stage 2 对应 P5：trajectory wrapper 和 grow strategy 产出的数据被用于持续训练 digital agents。

[Title]: Guided by Trajectories: Repairing and Rewarding Tool-Use Trajectories for Tool-Integrated Reasoning
- [Pathway]: Narrative → Evaluator → Policy (P4, P6)
- [Source Experience]: candidate tool-use trajectories, repaired trajectories, and original low-quality counterparts
- [Target Experience]: trajectory-level reward model and reliable TIR policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: repaired/high-quality trajectories form an SFT dataset; preference pairs train a trajectory RM that guides RL with outcome and format rewards
- [Method]: ⟨SFT⟩, ⟨hybrid⟩
- [Mechanism]: AutoTraj 先将低质量 tool-use trajectories 由 LLM-as-Repairer 修复，形成高质量 SFT 数据和 repaired-vs-original preference pairs；preference data 训练 trajectory-level RM，RM 再与 outcome/format rewards 共同优化 TIR 行为。

[Title]: Step-GUI Technical Report
- [Pathway]: Narrative → Evaluator → Policy (P4, P6)
- [Source Experience]: model-generated GUI trajectories calibrated by a step reward system
- [Target Experience]: reliable training signals and Step-GUI models
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {teacher}
- [Utilization]: calibrated reward signals power a self-evolving training pipeline for Step-GUI
- [Method]: ⟨hybrid⟩
- [Mechanism]: Calibrated Step Reward System 将模型生成轨迹转成高可靠训练信号；这些 reward-calibrated signals 再驱动 Step-GUI policy training。GUI-MCP 和 AndroidDaily 是接口/benchmark 贡献，非主转化链。

[Title]: Internalizing Agency from Reflective Experience
- [Pathway]: Policy → Narrative → Policy (P7, P5)
- [Source Experience]: exploration trajectories with environment feedback, actionable summaries, and alternative branches
- [Target Experience]: supervised corrections distilled into the agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: experience-guided corrections are used for supervised fine-tuning so the policy can recover in future interactions
- [Method]: ⟨SFT⟩
- [Mechanism]: Stage 1 对应 P7/P1：agent 在探索中总结环境反馈为 actionable experience，回溯到早期决策点并基于该经验探索修正分支；Stage 2 对应 P5：这些 experience-guided corrections 通过 SFT 内化到 policy。

[Title]: RetroAgent: From Solving to Evolving via Retrospective Dual Intrinsic Feedback
- [Pathway]: Policy → Narrative → Policy (P7, P5)
- [Source Experience]: prior attempts, subtask progress, hindsight self-reflections, and textual lessons
- [Target Experience]: intrinsic feedback signals, memory buffer lessons, and RL-trained agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: intrinsic numerical feedback trains the policy; intrinsic language feedback is retrieved from memory for subsequent decisions
- [Method]: ⟨RL: GRPO⟩, ⟨LLM-extract⟩
- [Mechanism]: RetroAgent 将历史尝试转成两类 retrospective feedback：数值反馈用于奖励相对先前尝试的 subtask progress，语言反馈蒸馏 reusable lessons 到 memory buffer；RL 更新 policy，SimUtil-UCB 检索 textual experiences 作为下一轮决策上下文。

[Title]: TRACE: Capability-Targeted Agentic Training
- [Pathway]: Narrative → Schematic → Policy (P2, P5)
- [Source Experience]: successful and failed agent trajectories showing capability deficits
- [Target Experience]: capability-targeted synthetic training environments and LoRA adapters
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: each synthetic environment trains a LoRA adapter via RL, and inference routes to the relevant adapter
- [Method]: ⟨hybrid⟩
- [Mechanism]: Stage 1 对应 P2：TRACE 对比成功/失败轨迹以识别缺失 capability，并合成 rewardable training environments；Stage 2 对应 P5：每个 synthetic environment 用 RL 训练 LoRA adapter，推理时按任务路由到对应 adapter。

[Title]: R3L: Reflect-then-Retry Reinforcement Learning with Language-Guided Exploration, Pivotal Credit, and Positive Amplification
- [Pathway]: Narrative → Narrative → Policy (P1, P5)
- [Source Experience]: failed attempts, language feedback, localized error points, and corrected suffixes
- [Target Experience]: successful reflect-then-retry trajectories and RL-optimized policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: transformed successful trajectories provide positive off-policy training data and contrastive suffix-level credit signals
- [Method]: ⟨hybrid⟩
- [Mechanism]: Stage 1 对应 P1：language feedback 诊断错误并定位 pivotal failure points，将失败尝试从错误点重启并改写为成功轨迹；Stage 2 对应 P5：Pivotal Credit Assignment 只更新分歧 suffix，Positive Amplification 放大成功轨迹信号以稳定 RL。

[Title]: Hi-WM: Human-in-the-World-Model for Scalable Robot Post-Training
- [Pathway]: Policy → Narrative → Policy (P7, P5)
- [Source Experience]: policy rollouts inside a learned world model and human corrective continuations
- [Target Experience]: dense corrective trajectories for robot post-training
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}, {human}
- [Utilization]: corrective trajectories are added back to the training set for post-training robot policies
- [Method]: ⟨SFT⟩
- [Mechanism]: Stage 1 对应 P7：base policy 在 world model 中 closed-loop rollout，并在失败状态缓存、回滚、分支；human 在 world model 中给出短 corrective actions，产生 dense correction trajectories；Stage 2 对应 P5：这些纠正轨迹进入 post-training 数据集更新 policy。

[Title]: ReAct Meets ActRe: When Language Agents Enjoy Training Data Autonomy
- [Pathway]: Policy → Narrative → Policy (P7, P5)
- [Source Experience]: sampled external actions, ActRe rationales, failed tasks, and accumulated successful trajectories
- [Target Experience]: ReAct-style trajectories with posterior reasoning and contrastively self-trained agents
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: successful autonomous trajectories supplement failed trajectories for contrastive self-training across multiple rounds
- [Method]: ⟨hybrid⟩
- [Mechanism]: ActRe prompting agent 为任意 sampled action 生成 posterior reasoning，ReAct-style agent 将 rationale prepend 到 action 形成新轨迹；成功轨迹被选择出来补充失败任务，并通过 policy-gradient contrastive self-training 更新 agent。

[Title]: VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model
- [Pathway]: Narrative → Narrative → Policy (P1, P5)
- [Source Experience]: real-world VLA rollout data including physical interaction failures
- [Target Experience]: synthetic supplemental rollouts and improved VLA policy
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: improved world model generates supplemental synthetic rollouts for VLA policy improvement
- [Method]: ⟨hybrid⟩
- [Mechanism]: Stage 1 对应 P1：real-world rollout data 用于提升 action-conditioned video world model 的物理 fidelity，使其能生成更可靠 synthetic rollouts；Stage 2 对应 P5：synthetic rollout data 被用于改善 VLA model。world model 本身不是当前 carrier 表中的 Policy/Evaluator，因此机制中说明而不单独作为路径节点。

[Title]: Iterative Trajectory Exploration for Multimodal Agents
- [Pathway]: Policy → Narrative → Policy (P7, P5)
- [Source Experience]: synthesized multimodal tasks, sampled steps, verifier feedback, and preference data
- [Target Experience]: SPORT Agent policy after step-wise preference optimization
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: step-wise preference data is used to update the controller policy and generate a more refined SPORT Agent
- [Method]: ⟨hybrid⟩
- [Mechanism]: SPORT 先由语言模型合成多模态任务，再交替执行 step sampling 和 step verification；verifier 的 AI feedback 构成 step-wise preference data，随后通过 preference tuning 更新 controller policy。

[Title]: Reflection-Based Task Adaptation for Self-Improving VLA
- [Pathway]: Narrative → Schematic → Policy (P2, P5)
- [Source Experience]: failure analyses, synthesized dense reward functions, and high-quality successful trajectories
- [Target Experience]: targeted reward functions and adapted VLA policy
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: failure-driven reward functions guide RL exploration; high-quality successful trajectories support quality-guided SFT
- [Method]: ⟨hybrid⟩
- [Mechanism]: Stage 1 对应 P2：VLM causal reasoning 将 failure analysis 转成 targeted dense reward function；Stage 2 对应 P5：reward function 加速 RL，成功轨迹再经 quality-guided SFT grounding policy，缓解 proxy reward hacking。

[Title]: No More Stale Feedback: Co-Evolving Critics for Open-World Agent Learning
- [Pathway]: Narrative → Evaluator → Policy (P4, P6)
- [Source Experience]: policy rollouts, critic diagnoses, and incremental improvement signals
- [Target Experience]: synchronized critic and policy after dual-track GRPO updates
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: evolving critic feedback provides synchronized training signal for on-policy RL
- [Method]: ⟨RL: GRPO⟩
- [Mechanism]: 轨迹和多重 diagnoses 被用于训练随 policy 同步演化的 critic；critic 通过 saturation-aware gain shaping 被奖励为高分轨迹带来 incremental improvements，随后 dual-track GRPO 同时更新 critic 与 policy，避免 static critic 反馈 stale。

[Title]: Self-Improving LLM Agents at Test-Time
- [Pathway]: Policy → Narrative → Policy (P7, P5)
- [Source Experience]: uncertain or difficult test-time agent samples
- [Target Experience]: self-augmented or teacher-augmented training examples and test-time fine-tuned agentic LM
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: generated similar examples are used for test-time fine-tuning on-the-fly
- [Method]: ⟨SFT⟩
- [Mechanism]: agent 先识别自己 struggling 的样本，再由同一模型或 stronger teacher 生成相似训练样本，最后在 test-time fine-tuning 中把这些新样本内化为 policy adaptation。

[Title]: The Lighthouse of Language: Enhancing LLM Agents via Critique-Guided Improvement
- [Pathway]: Narrative → Evaluator → Policy (P4, P6)
- [Source Experience]: actor environment explorations and natural-language critiques
- [Target Experience]: trained critic model and actor model that uses critiques
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: critic-generated actionable feedback guides actor exploration and strategy revision
- [Method]: ⟨hybrid⟩
- [Mechanism]: CGI 将 actor 的环境探索轨迹转为 critic 训练信号，使 critic 学会生成细粒度 assessment 与 actionable revisions；actor 再学习利用这些 critiques，形成 evaluator-to-policy 的迭代改进。

[Title]: VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought
- [Pathway]: Narrative → Narrative → Policy (P1, P5)
- [Source Experience]: imperfect task demonstrations, self-reflection outputs, execution feedback, and human feedback
- [Target Experience]: generalized strategies, action annotations, and ICAL examples
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {self}, {human}
- [Utilization]: ICAL examples are reused through retrieval-augmented generation or fine-tuning
- [Method]: ⟨LLM-extract⟩, ⟨SFT⟩
- [Mechanism]: Stage 1 对应 P1：VLM 将 suboptimal trajectories 抽象为 generalized strategies 与 action annotations，并通过 human feedback 迭代修正 inefficiencies；Stage 2 对应 P5：这些 examples 可进一步用于 fine-tuning，同时也可作为 RAG memory 直接复用。

[Title]: OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards
- [Pathway]: Narrative → Evaluator → Policy (P4, P6)
- [Source Experience]: GUI trajectories decomposed into verifiable milestones and audited evidence chains
- [Target Experience]: OS-Themis critic framework and RL/self-training signals
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {teacher}
- [Utilization]: OS-Themis rewards support online RL training and trajectory validation/filtering in self-training
- [Method]: ⟨hybrid⟩
- [Mechanism]: 轨迹先被分解为 verifiable milestones 并经 review mechanism 审计证据链，形成更可靠的 outcome reward evaluator；该 evaluator 再用于在线 RL 和 self-training 数据过滤。

[Title]: Policy Improvement using Language Feedback Models
- [Pathway]: Narrative → Evaluator → Policy (P4, P6)
- [Source Experience]: visual trajectories verbalized to language descriptions and LLM feedback on desirable behavior
- [Target Experience]: Language Feedback Models and imitation-learning policy improvements
- [Source Modality]: [cross-modal]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}
- [Utilization]: LFM identifies desirable behavior to imitate and can provide human-interpretable feedback for verification
- [Method]: ⟨hybrid⟩
- [Mechanism]: Stage 1 对应 P4：visual trajectories 被 verbalized 后交给 LLM 产生 feedback，用于训练 LFM 判断 desirable actions；Stage 2 对应 P6：LFM 选择值得模仿的行为作为 imitation-learning 信号，提升 instruction-following policies。

[Title]: RLAnything: Forge Environment, Policy, and Reward Model in Completely Dynamic RL System
- [Pathway]: Narrative → Evaluator → Policy (P4, P6)
- [Source Experience]: step-wise signals, outcome signals, consistency feedback, and critic feedback from dynamic environments
- [Target Experience]: jointly optimized reward model and policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: optimized reward-model signals provide integrated feedback for policy training; critic feedback also adapts the environment
- [Method]: ⟨hybrid⟩
- [Mechanism]: RLAnything 从环境交互经验中同时优化 reward model 与 policy：RM 通过 consistency feedback 更新，policy 通过 step-wise/outcome feedback 和 RM signals 更新，environment adaptation 又利用二者 critic feedback 放大学习信号。

[Title]: Pre-Trained Language Models for Interactive Decision-Making
- [Pathway]: Narrative → Narrative → Policy (P1, P5)
- [Source Experience]: expert demonstrations and relabeled failed experiences from active data gathering
- [Target Experience]: self-supervised relabeled data and LM-initialized policy network
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {human}, {self}
- [Utilization]: demonstrations and relabeled failed experiences train/update policies in sequential decision-making environments
- [Method]: ⟨SFT⟩
- [Mechanism]: 初始阶段使用 expert demonstrations 做 behavior cloning；active data gathering 阶段将 failed experiences relabel 为新目标下的可用经验，再在 self-supervised loop 中更新 policy。该工作是广义 LM-based sequential decision-making，边界上接近传统 RL，但摘要明确使用 LM policy 表示 goals/observations/action prediction。

[Title]: OS-Oracle: A Comprehensive Framework for Cross-Platform GUI Critic Models
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: synthesized cross-platform GUI critic samples
- [Target Experience]: OS-Oracle-7B GUI critic model
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {teacher}
- [Utilization]: critic model serves as a pre-critic to improve native GUI agents in OSWorld and AndroidWorld
- [Method]: ⟨SFT⟩, ⟨RL: GRPO⟩
- [Mechanism]: scalable data pipeline 合成 GUI critic data，随后通过 SFT 与 consistency-preserving GRPO 训练 step-level critic；该 evaluator 在推理前评估 GUI actions，提升原生 GUI agents。

[Title]: ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: self-judged successful and failed interaction experiences
- [Target Experience]: generalizable reasoning strategies stored in ReasoningBank
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: relevant memories are retrieved at test time and new learnings are integrated back into the bank
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: agent 对成功/失败经验进行 self-judgment 后蒸馏出 generalizable reasoning strategies；MaTTS 通过分配更多 test-time compute 生成多样经验，利用 contrastive signals 合成更高质量 memory，再反过来指导 scaling。

[Title]: AutoRefine: From Trajectories to Reusable Expertise for Continual LLM Agent Refinement
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: agent execution histories with procedural subtasks and static knowledge
- [Target Experience]: specialized subagents, skill patterns, guidelines, and code snippets
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: maintained Experience Patterns are reused to reduce steps and improve performance across ALFWorld, ScienceWorld, and TravelPlanner
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: AutoRefine 从 execution histories 中抽取 dual-form patterns：procedural subtasks 被形式化为 specialized subagents，static knowledge 被整理为 guidelines/code snippets；维护机制持续 score、prune、merge，防止 repository degradation。

[Title]: Improving Vision-Language-Action Model with Online Reinforcement Learning
- [Pathway]: Policy → Narrative → Policy (P7, P5)
- [Source Experience]: online VLA interactions with simulated and real manipulation environments
- [Target Experience]: improved VLA policy after alternating RL and supervised learning
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: online interaction data drives RL exploration, while supervised learning stabilizes large VLA policy updates
- [Method]: ⟨hybrid⟩
- [Mechanism]: iRe-VLA 在环境中收集 online interaction trajectories，利用 RL 获得探索增益，再交替使用 supervised learning 维持大模型稳定性，把交互经验内化到 VLA policy。

[Title]: Memento No More: Coaching AI Agents to Master Multiple Tasks via Hints Internalization
- [Pathway]: Narrative → Policy (P5)
- [Source Experience]: new agent experiences and human corrective hints
- [Target Experience]: task knowledge and skills internalized into agent weights
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {human}
- [Utilization]: context distillation integrates hints into weights so the agent no longer depends on expanding prompts
- [Method]: ⟨SFT⟩
- [Mechanism]: agent 多轮收集新经验并接收 human hints，随后通过 context distillation training 将这些纠正性自然语言经验写入 Llama-3-based agent weights，以支持多任务 tool use 和 QA sequencing。

[Title]: XSkill: Continual Learning from Experience and Skills in Multimodal Agents
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: multi-path multimodal rollouts and visually grounded critiques
- [Target Experience]: experiences for action-level guidance and skills for task-level planning/tool use
- [Source Modality]: [vis+txt]
- [Target Modality]: [vis+txt]
- [Experience Source]: {self}
- [Utilization]: experiences and skills are retrieved/adapted to the current visual context; usage history feeds back into accumulation
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: XSkill 从 multi-path rollouts 中通过 visually grounded summarization 与 cross-rollout critique 蒸馏两条知识流：action-level experiences 偏 P1，structured task-level skills 偏 P2；主贡献是将经验 formalize 为可检索技能并闭环更新。

[Title]: Memp: Exploring Agent Procedural Memory
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: past agent trajectories
- [Target Experience]: fine-grained step-by-step instructions and higher-level script-like procedural abstractions
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: procedural memory repository is retrieved, updated, corrected, deprecated, and reused for analogous tasks
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Memp 将轨迹蒸馏为可更新的 procedural memory，包括 step instructions 与 script-like abstractions；Build/Retrieval/Update 策略让 repository 随新经验演化并迁移到较弱模型。

[Title]: Voyager: An Open-Ended Embodied Agent with Large Language Models
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: Minecraft environment feedback, execution errors, and self-verification signals
- [Target Experience]: ever-growing executable code skill library
- [Source Modality]: [embodied]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: learned skills are retrieved and composed in-context to solve novel Minecraft tasks
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Voyager 通过 iterative prompting 使用环境反馈、执行错误和 self-verification 改进程序技能，把 trial-and-error experience 转成 temporally extended executable code skills；技能库持续增长并可组合复用。

[Title]: Skill Set Optimization: Reinforcing Language Model Behavior via Transferable Skills
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: common high-reward subtrajectories and environment rewards
- [Target Experience]: transferable skills represented by subgoals and instructions
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: skill set is provided in-context to the LLM actor and pruned/refined by downstream reward outcomes
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: SSO 从高奖励 subtrajectories 中抽取公共片段，生成 subgoals 和 instructions 表示 transferable skills；技能作为 prompt context 强化高奖励行为，并根据后续 reward 进行 pruning/refinement。

[Title]: WebXSkill: Skill Learning for Autonomous Web Agents
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: synthetic web agent trajectories and reusable action subsequences
- [Target Experience]: executable skills with parameterized action programs and step-level natural-language guidance
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {teacher}
- [Utilization]: skills are retrieved by URL graph and used either for grounded execution or guided step-by-step planning
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: WebXSkill 从 trajectories 中挖掘 reusable action subsequences，将其抽象为 parameterized action programs 并配套 step-level guidance，再组织为 URL graph 以支持上下文检索和执行。

[Title]: Failure Makes the Agent Stronger: Enhancing Accuracy through Structured Reflection for Reliable Tool Interactions
- [Pathway]: Narrative → Narrative → Policy (P1, P5)
- [Source Experience]: erroneous tool-call mini trajectories, evidence from previous steps, and corrected calls
- [Target Experience]: structured reflection action data and optimized tool-use policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: reflection-then-call trajectories train the model for multi-turn tool-call error recovery
- [Method]: ⟨hybrid⟩
- [Mechanism]: Stage 1 对应 P1：错误 tool call 被改写为“诊断失败、提出正确 follow-up call”的显式 reflection trajectory；Stage 2 对应 P5：DAPO/GSPO objectives 与 tool-use reward scheme 优化 Reflect-then-Call-then-Final 策略。

[Title]: LaViT: Aligning Latent Visual Thoughts for Multi-modal Reasoning
- [Pathway]: Out of Scope
- [Mechanism]: 摘要聚焦 teacher-student multimodal reasoning distillation 和 visual attention alignment，没有明确 LLM-based agent 的环境交互轨迹或异构 agent action space，属于 Project_Infos.md §3.2 中缺少序贯决策经验语义的边界外工作。

[Title]: Contextual Experience Replay for Self-Improvement of Language Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: past web-navigation experiences, environment dynamics, and decision-making patterns
- [Target Experience]: synthesized dynamic memory buffer
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: relevant memory is retrieved into the context window for training-free inference-time self-improvement
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: CER 累积并综合 past experiences，将环境动态和常见决策模式压缩到 dynamic memory buffer；新任务中通过 context retrieval 注入这些经验，无需参数更新。

[Title]: TAME: A Trustworthy Test-Time Evolution of Agent Memory with Systematic Benchmarking
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: historical feedback, task-utility outcomes, and safety-relevant memory evolution traces
- [Target Experience]: executor memory and evaluator memory
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: executor memory guides task execution, evaluator memory refines safety and utility assessments during benign task evolution
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: TAME 通过 memory filtering、draft generation、trustworthy refinement、execution 和 dual-track memory updating，将历史反馈分别蒸馏为 executor memory 中的方法论和 evaluator memory 中的安全/效用评估准则；这里的 evaluator memory 是文本记忆，不是参数化 Evaluator。

[Title]: Investigate-Consolidate-Exploit: A General Strategy for Inter-Task Agent Self-Evolution
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: planning and execution trajectories across tasks
- [Target Experience]: simplified workflows and pipelines
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: consolidated workflows and pipelines are exploited for improved execution on later tasks
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: ICE 动态 investigate agent trajectories，再将跨任务经验 consolidate 为简化 workflows/pipelines，最后在新任务执行中 exploit 这些 procedural carriers，减少 API calls 和模型能力需求。

[Title]: TGPO: Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning
- [Pathway]: Narrative → Schematic → Policy (P2, P5)
- [Source Experience]: web-agent trajectories, semantically identical states, and process-reward signals
- [Target Experience]: tree-structured trajectory representation and preference-optimized web agent
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: trajectory tree, PRM rewards, and dynamic weighting provide offline RL training signals
- [Method]: ⟨hybrid⟩
- [Mechanism]: Stage 1 对应 P2：TGPO 将多条 trajectories 合并成 tree-structured representation，以消除语义相同状态的 label conflicts；Stage 2 对应 P5：PRM 生成细粒度 rewards，dynamic weighting 强调关键决策点，用于 preference optimization。

[Title]: Agent Workflow Memory
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: past web-navigation task trajectories from offline examples or online test queries
- [Target Experience]: reusable workflows / routines
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {human}
- [Utilization]: workflows are selectively provided to the agent to guide subsequent generations
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: AWM 从训练样本或在线任务轨迹中诱导 commonly reused routines，将 raw task experience formalize 为 workflows；后续任务中按需检索这些 workflows 指导 agent actions。

[Title]: AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials
- [Pathway]: Narrative → Schematic → Policy (P2, P5)
- [Source Experience]: tutorial-like web texts and step-by-step instructions
- [Target Experience]: structured task specifications, verified multimodal web trajectories, and trained GUI agents
- [Source Modality]: [txt]
- [Target Modality]: [GUI]
- [Experience Source]: {human}, {teacher}
- [Utilization]: synthesized trajectories enriched with CoT reasoning are used to train textual and visual web agents
- [Method]: ⟨hybrid⟩
- [Mechanism]: Stage 1 对应 P2：tutorial-like texts 被过滤并转成 structured task specifications；Stage 2 对应 P5：VLM agent 执行这些 specs 生成 GUI trajectories，VLM evaluator 验证正确性后作为 agent training data。

[Title]: CLEANER: Self-Purified Trajectories Boost Agentic Reinforcement Learning
- [Pathway]: Policy → Narrative → Policy (P7, P5)
- [Source Experience]: noisy agentic RL trajectories with execution failures and self-corrections
- [Target Experience]: clean self-purified trajectories and optimized policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: purified paths are used during RL so the model internalizes correct reasoning patterns instead of error-recovery loops
- [Method]: ⟨hybrid⟩
- [Mechanism]: SAAR 在数据收集时利用模型自我纠错能力，按语义相似性从 shallow execution repairs 到 deep reasoning substitutions 自适应替换失败片段，构造 clean trajectories；policy 再从这些 purified paths 中学习。

[Title]: MCTS-EP: Empowering Embodied Planning with Online Preference Optimization
- [Pathway]: Policy → Narrative → Policy (P7, P5)
- [Source Experience]: MCTS-guided embodied exploration trajectories and preference data
- [Target Experience]: preference-optimized embodied LLM agent
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: collected preference data supports iterative online preference optimization
- [Method]: ⟨MCTS⟩, ⟨hybrid⟩
- [Mechanism]: MCTS-enhanced agent 与 embodied environments 交互，收集 preference data；efficient multimodal reasoning 处理视觉/文本任务，iterative training pipeline 将 preference signal 内化到 embodied planning policy。

[Title]: Environment Maps: Structured Environmental Representations for Long-Horizon Agents
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: screen recordings, execution traces, observed workflows, and tacit domain knowledge
- [Target Experience]: structured Environment Map graph with contexts, actions, workflows, and tacit knowledge
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {human}
- [Utilization]: structured graph is provided as a persistent, editable interface for long-horizon planning
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Heterogeneous evidence from past web interactions is consolidated into a graph whose nodes/edges encode abstract locations, parameterized affordances, observed trajectories, and reusable procedures, enabling agents to plan beyond raw session context.

[Title]: WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: raw navigation logs and complete cross-session web trajectories
- [Target Experience]: concise trajectory summaries, episodic memory, and task-specific advice
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: Coach retrieves relevant experiences and injects advice via runtime hooks without retraining
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: WebCondenser 将 raw logs 标准化为 concise summaries，External Memory Store 保存完整 episodic trajectories，Coach 基于相似度和 recency 判断是否注入 task-specific advice；新轨迹持续进入 memory。

[Title]: Scaling Autonomous Agents via Automatic Reward Modeling And Planning
- [Pathway]: Policy → Narrative → Evaluator (P7, P4)
- [Source Experience]: random environment trajectories generated by an LLM-based agent
- [Target Experience]: task-intent / positive / negative triplets and trajectory-scoring reward model
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: learned reward model evaluates LLM-agent trajectories and provides planning heuristics
- [Method]: ⟨hybrid⟩
- [Mechanism]: Stage 1 对应 P7：一个 LLM-based agent 随机探索环境并生成 diverse action trajectories；Stage 2 对应 P4：另一个 LLM 为每条轨迹分配 task intent、positive response 和 negative response，triplets 用于训练 reward model。

[Title]: ExpeL: LLM Agents Are Experiential Learners
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: autonomously gathered training-task experiences
- [Target Experience]: extracted natural-language insights and recalled past experiences
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: insights and past experiences are recalled at inference to support custom decision-making tasks without parametric updates
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: ExpeL agent 在训练任务中自主收集 experiences，并用自然语言提取 reusable knowledge；推理时调用这些 insights 和 past experiences 做决策，避免 fine-tuning proprietary LLMs。

[Title]: SCOPE: Prompt Evolution for Enhancing Agent Effectiveness
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: execution traces and recurring corrective/enhancement failures
- [Target Experience]: evolved prompt guidelines
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: synthesized guidelines update the agent's prompt online to improve context management
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: SCOPE 将 execution traces 中的 failure patterns 转成 prompt-management guidelines；Dual-Stream mechanism 同时生成 tactical fixes 和 strategic principles，Perspective-Driven Exploration 扩大 strategy coverage。

[Title]: Scaling Synthetic Task Generation for Agents via Exploration
- [Pathway]: Policy → Narrative → Policy (P7, P5)
- [Source Experience]: MLLM explorer trajectories over Android and Ubuntu applications
- [Target Experience]: environment-grounded tasks, demonstrations, verifier rewards, and trained UI agents
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {teacher}
- [Utilization]: generated tasks enable demonstration synthesis, SFT, and verifier-reward RL for UI agents
- [Method]: ⟨hybrid⟩
- [Mechanism]: AutoPlay 先让 MLLM explorer 系统探索环境状态和功能，再由 task generator 利用探索轨迹与 guideline prompts 合成 feasible/verifiable tasks；executor/verifier 生成 demos 和 rewards，用于 UI-agent training/RL。

[Title]: Experience-Evolving Multi-Turn Tool-Use Agent with Hybrid Episodic-Procedural Memory
- [Pathway]: Narrative → Schematic → Policy (P2, P5)
- [Source Experience]: accumulated multi-turn tool-use trajectories and successful tool transitions
- [Target Experience]: tool graph with procedural routines and episodic context summaries
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: memory is used for inference-time recall/execution and to bias RL exploration toward successful tool transitions
- [Method]: ⟨LLM-extract⟩, ⟨hybrid⟩
- [Mechanism]: Stage 1 对应 P2：H-EPM 从轨迹中构建 tool graph，边表示 recurring tool-to-tool dependencies，并附加 compact episodic summaries；Stage 2 对应 P5：该 memory-guided RL bias exploration over long trajectories，训练更强 policy。

[Title]: Enhancing Web Agents with a Hierarchical Memory Tree
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: raw web-agent trajectories
- [Target Experience]: three-level Hierarchical Memory Tree with Intent, Stage, and Action levels
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: Planner validates pre/postconditions and Actor grounds stored action descriptions to the current page
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: HMT 自动抽象 raw trajectories：Intent 层标准化目标，Stage 层定义可复用 semantic subgoals 与前后置条件，Action 层存储 action patterns 和 transferable element descriptions，以避免 flat memory 的 workflow mismatch。

[Title]: Bootstrapping Language-Guided Navigation Learning with Self-Refining Data Flywheel
- [Pathway]: Policy → Narrative → Policy (P7, P5)
- [Source Experience]: instruction-trajectory pairs generated by an instruction generator and filtered by a navigator
- [Target Experience]: refined navigation data pool, improved generator, and improved navigator
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}, {self}
- [Utilization]: refined data trains each next-round navigator and generator for language-guided navigation
- [Method]: ⟨SFT⟩
- [Mechanism]: generator 先产生 instruction-trajectory data pool 训练 navigator；trained navigator 过滤数据池得到高保真数据，再训练更好的 generator；更好的 generator 又产出下一轮 navigator 数据，形成 P7/P5 flywheel。

[Title]: ProRe: A Proactive Reward System for GUI Agents via Reasoner-Actor Collaboration
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: GUI trajectories, targeted state-probing interactions, and additional observations collected by evaluator agents
- [Target Experience]: more accurate and verifiable GUI rewards
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}, {teacher}
- [Utilization]: rewards evaluate GUI agents and improve policy agents when integrated with them
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: general-purpose reasoner 为不确定 GUI trajectory 安排 targeted state probing tasks，domain-specific evaluator agents 主动交互收集额外证据，reasoner 再将证据转化为可验证 reward。

[Title]: Agentic Reward Modeling: Verifying GUI Agent via Online Proactive Interaction
- [Pathway]: Narrative → Evaluator (P4)
- [Source Experience]: GUI observations, verifier-agent probing trajectories, and task-completion evidence
- [Target Experience]: agentic interactive verifier / reward signal
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: verifier improves evaluation accuracy and supports test-time scaling for GUI agents
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: VAGEN 将被动视觉评估改为 verifier agent 主动规划验证策略并 probing 环境，收集 latent system state 证据后输出 task-completion verdict/reward。

[Title]: Agent KB: Leveraging Cross-Domain Experience for Agentic Problem Solving
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: problem-solving trajectories from heterogeneous agent frameworks
- [Target Experience]: structured cross-domain knowledge base with workflows and diagnostic fixes
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {human}
- [Utilization]: hybrid retrieval seeds planning with workflows and applies targeted feedback fixes through lightweight APIs
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: AGENT KB 聚合不同 framework 的 trajectories，组织为可 API 访问的 structured KB；retrieval 分为 planning seed 和 feedback diagnostic fix 两阶段，并由 disagreement gate 控制知识干扰。

[Title]: Self-Supervised Bootstrapping of Action-Predictive Embodied Reasoning
- [Pathway]: Narrative → Narrative → Policy (P1, P5)
- [Source Experience]: internet-scale embodied knowledge and model-generated action-predictive reasoning candidates
- [Target Experience]: refined embodiment-specific reasoning training dataset and improved VLA policies
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}
- [Utilization]: refined reasoning dataset is distilled into VLA architectures for manipulation, navigation, and driving embodiments
- [Method]: ⟨SFT⟩
- [Mechanism]: R&B-EnCoRe 将 embodied reasoning 视作 latent variable，通过 importance-weighted variational inference 选择与成功控制最相关的 reasoning，生成 refined training dataset，再蒸馏进 VLA policy。摘要没有说明外部交互 reward，因此 source 记为 teacher/model-generated。

[Title]: AutoSurfer -- Teaching Web Agents through Comprehensive Surfing, Learning, and Modeling
- [Pathway]: Policy → Narrative → Policy (P7, P5)
- [Source Experience]: breadth-first website exploration trajectories and action traces
- [Target Experience]: grounded web tasks, reliable trajectories, and fine-tuned website-specific LLMs
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: generated trajectories are used to fine-tune web agents such as Qwen2.5-VL-7B-Instruct
- [Method]: ⟨SFT⟩
- [Mechanism]: AutoSurfer 系统探索网站页面与 GUI elements，利用 exploration trajectories 指导 task synthesis，并将同一轨迹作为 hints 引导 agent trajectory refinement；最终数据用于 fine-tuning web agents。

[Title]: Bifrost: Steering Strategic Trajectories to Bridge Contextual Gaps for Self-Improving Agents
- [Pathway]: Narrative → Latent (P3)
- [Source Experience]: previously solved task trajectories and context differences to a target task
- [Target Experience]: adapted trajectory steering signals in agent hidden-state representation
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: representation-level trajectory adaptation enables training-free reuse of past trajectories under context mismatch
- [Method]: ⟨hybrid⟩
- [Mechanism]: Bifrost 利用 context-trajectory correlation，把已解决任务轨迹与目标任务上下文差异映射到 shared hidden-state space，在 representation level 精确 steering trajectory reuse；目标 carrier 是 latent steering state，而非显式文本改写。

[Title]: ACON: Optimizing Context Compression for Long-horizon LLM Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: full-context success trajectories, compressed-context failure trajectories, and interaction histories
- [Target Experience]: optimized compression guidelines and concise context condensations
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {teacher}
- [Utilization]: guidelines compress observations/histories; distilled compressors reduce overhead while preserving task performance
- [Method]: ⟨LLM-extract⟩, ⟨SFT⟩
- [Mechanism]: capable LLMs compare paired trajectories where full context succeeds but compressed context fails，分析失败原因并更新 natural-language compression guidelines；这些 guidelines 产生更可靠 condensations，并可蒸馏到小型 compressor。

[Title]: WebCoT: Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback
- [Pathway]: Narrative → Narrative → Policy (P1, P5)
- [Source Experience]: web-agent trajectories exhibiting reflection, lookahead, branching, and rollback
- [Target Experience]: reconstructed CoT rationales and fine-tuned web-agent backbone
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: reconstructed reasoning patterns are distilled into the backbone LLM through fine-tuning
- [Method]: ⟨SFT⟩
- [Mechanism]: Stage 1 对应 P1：WebCoT 从 inference-time trajectory algorithms 中重构 CoT rationales，显式化 reflection/lookahead/branching/rollback 技能；Stage 2 对应 P5：这些 reasoning patterns 通过 fine-tuning 写入 backbone LLM。

[Title]: Weak-to-Strong Generalization with Failure Trajectories: A Tree-based Approach to Elicit Optimal Policy in Strong Models
- [Pathway]: Policy → Schematic → Policy (P7, P5)
- [Source Experience]: weak-model generated success and failure trajectories
- [Target Experience]: trajectory trees and optimized strong-model policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: trajectory trees and MCTS elicit stronger reasoning and decision-making behavior in strong models
- [Method]: ⟨MCTS⟩, ⟨SFT⟩
- [Mechanism]: Stage 1 对应 P7/P2：weak model 外化中间动作轨迹，并将 success/failure experience 组织成 hierarchical trajectory trees；Stage 2 对应 P5：MCTS 基于树结构优化 strong model，使其从成功知识和失败经验中学习。

[Title]: Guiding VLM Agents with Process Rewards at Inference Time for GUI Navigation
- [Pathway]: Evaluator → Narrative
- [Source Experience]: process reward model scores for GUI action candidates
- [Target Experience]: inference-time selected GUI action trajectories with optional reflection/retry
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: 不清楚
- [Utilization]: process rewards guide VLM agents at each inference step without fine-tuning
- [Method]: ⟨hybrid⟩
- [Mechanism]: reward model 在 GUI navigation/control 的每一步给候选动作提供 process supervision，使 VLM agent 选择更优 action；该路径是 Evaluator 参数信号到 live tokenized/action trajectory 的外化式利用，不完全落入 P6，因为摘要没有 policy weight update。

[Title]: VerificAgent: Domain-Specific Memory Verification for Scalable Oversight of Aligned Computer-Use Agents
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: expert-curated domain knowledge, trajectory-based memory growth, and human fact-checking corrections
- [Target Experience]: sanitized persistent memories / frozen safety contract
- [Source Modality]: [GUI]
- [Target Modality]: [txt]
- [Experience Source]: {self}, {human}
- [Utilization]: verified memory constrains future CUA actions and provides auditable guidance without fine-tuning
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: VerificAgent 先用 seed domain knowledge 初始化 memory，再通过 training trajectories 扩展 memory，最后由 human fact-checking 清洗高影响错误，使 persistent memory 成为可审计的 alignment surface。

[Title]: Reflexion: language agents with verbal reinforcement learning
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: task feedback signals from games, compilers, APIs, coding, and reasoning tasks
- [Target Experience]: verbal reflections in episodic memory
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: reflective text memory is maintained and injected into subsequent trials for better decision-making
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Reflexion 将 scalar 或 free-form feedback 转成 verbal self-reflections，并存入 episodic memory；后续 trials 检索这些 reflective texts 来改变 agent 行为，不更新模型参数。

[Title]: BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: GUI action outcomes, outcome pages, verifier/judger signals, and reflector feedback
- [Target Experience]: backtracking-oriented reflection/correction data and judgment rewards
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: verifier, judger, and reflector modules use the data to detect errors, recover, and improve task completion
- [Method]: ⟨hybrid⟩
- [Mechanism]: BacktrackAgent 将 action execution 后的 outcome pages 与判断信号转成 error detection / recovery feedback，并构建 backtracking dataset；摘要未明确说明 policy 参数如何训练，因此主路径标为 tokenized feedback refinement。

[Title]: LAGEA: Language Guided Embodied Agents for Robotic Manipulation
- [Pathway]: Narrative → Evaluator → Policy (P4, P6)
- [Source Experience]: episodic VLM reflections over robotic attempts and visual state alignments
- [Target Experience]: bounded step-wise shaping rewards and RL-trained embodied policy
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}, {teacher}
- [Utilization]: language-derived shaping rewards guide RL exploration and fade as competence improves
- [Method]: ⟨hybrid⟩
- [Mechanism]: VLM 将每次尝试总结为 schema-constrained reflection，定位 decisive trajectory moments 并与 visual state 对齐；goal progress 与 feedback agreement 被转成 bounded step-wise shaping rewards，随后用于 RL policy improvement。

[Title]: A Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: terminal-agent interaction trajectories and noisy terminal observations
- [Target Experience]: structured workflow-adaptive compression rules
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: compression rules filter low-value terminal outputs while preserving task-relevant observations
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: TACO 从 terminal interaction trajectories 中自动发现、refine 和复用 structured compression rules，使不同 repository/command 状态下的观察压缩保持 workflow-adaptive。

[Title]: REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: multisensory robot observations and hierarchical summaries of past failed executions
- [Target Experience]: informative failure explanations
- [Source Modality]: [embodied]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: failure explanations guide a language-based planner to correct the failure and complete the task
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: REFLECT 先把 robot past experiences 由多传感器观察转成 hierarchical summary，再查询 LLM 生成 failure reasoning；这些解释作为 planner 的纠错依据。

[Title]: CLIN: A Continually Learning Language Agent for Rapid Task Adaptation and Generalization
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: repeated trials, varied tasks/environments, and feedback from ScienceWorld interactions
- [Target Experience]: persistent textual memory centered on causal abstractions
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: dynamic memory is updated after each trial and reused for rapid adaptation/generalization without parameter updates
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: CLIN 在每次 trial 后把环境交互经验转成 causal abstractions，而非泛化的 helpful hints；memory 随任务和环境变化持续更新，用于同任务、新环境和新任务的后续决策。

[Title]: LLM-Driven Self-Refinement for Embodied Drone Task Planning
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: continuous drone state evaluations, explanatory feedback, and iterative self-refinement experience base
- [Target Experience]: modified hierarchical Behavior Tree task plans
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: optimized experience base and modified BT plans are deployed for real-world drone task planning
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: SRDrone 用 continuous state evaluation 产生 outcome 判断和 explanatory feedback，再由 hierarchical BT modification model 在 constrained strategy space 中更新 Behavior Tree plans，将经验转成可执行 symbolic plan carrier。

[Title]: Accurate Failure Prediction in Agents Does Not Imply Effective Failure Prevention
- [Pathway]: Out of Scope
- [Mechanism]: 摘要主要是对 LLM critic intervention 的部署风险和 pilot-test 评估方法做实证分析，没有描述把 agent experience 转化为可复用 carrier 的机制；属于 Project_Infos.md §3.2 中“缺少明确 experience transformation”的边界外情况。

[Title]: WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning
- [Pathway]: Annotation Failed
- [Mechanism]: Abstract 为空，无法仅凭摘要判断源经验、目标载体或 Pathway。

[Title]: APEX-EM: Non-Parametric Online Learning for Autonomous Agents via Structured Procedural-Episodic Experience Replay
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: full procedural-episodic execution traces, planning steps, artifacts, iteration histories, error analyses, and quality scores
- [Target Experience]: structured procedural plans and dual-outcome Experience Memory
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: successful experiences serve as positive in-context examples; failures serve as negative examples with structured error annotations
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: APEX-EM 将执行轨迹编码为 structured procedural-episodic representation，并通过 PRGII workflow、Task Verifiers 和 plan DAG traversal 形成可检索 Experience Memory，支持跨领域结构迁移。

[Title]: Beyond Human Preferences: Exploring Reinforcement Learning Trajectory Evaluation and Improvement through LLMs
- [Pathway]: Out of Scope
- [Mechanism]: 摘要描述 LLM 为传统 RL game trajectories 生成偏好并重构 reward functions，policy action space 没有明确属于 LLM-based agent 的异构动作空间；对应 Project_Infos.md §3.2 中非 LLM-based sequential system 的排除边界。

[Title]: Closed-Loop Verbal Reinforcement Learning for Task-Level Robotic Planning
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: physical robot execution traces and structured natural-language feedback from a VLM critic
- [Target Experience]: executable Behavior Trees refined by an LLM actor
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}, {teacher}
- [Utilization]: refined BTs serve as transparent symbolic policies for mobile robot task-level planning
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: VLM critic 观察物理 robot 和执行 traces 产生 causal natural-language feedback，LLM actor 用该反馈直接修改 executable Behavior Trees；policy evolution 发生在 symbolic planning carrier 中，而非梯度参数更新。

[Title]: ReUseIt: Synthesizing Reusable AI Agent Workflows for Web Automation
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: successful and failed web-agent attempts
- [Target Experience]: reusable workflows with execution guards
- [Source Modality]: [GUI]
- [Target Modality]: [GUI]
- [Experience Source]: {self}
- [Utilization]: workflows help agents complete repetitive web tasks with less user guidance and expose progress/failure state to users
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: ReUseIt 从成功和失败尝试中合成 reusable workflows，并加入 execution guards 来检测和修复错误；workflow carrier 比原始轨迹更可执行、可监控。

[Title]: ReGAL: Refactoring Programs to Discover Generalizable Abstractions
- [Pathway]: Out of Scope
- [Mechanism]: 摘要聚焦程序重构和函数库抽象学习，源端是 existing programs 而非 LLM-agent 与环境交互产生的决策经验；缺少 Project_Infos.md §3.1 要求的 agent experience loop 与异构 agent action space。

[Title]: WorkflowGen:an adaptive workflow generation mechanism driven by trajectory experience
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: full trajectories, node-level and workflow-level reusable knowledge, error fingerprints, tool mappings, parameter schemas, execution paths, and exception-avoidance strategies
- [Target Experience]: workflow templates and modular traceable experiences
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: direct reuse, rewriting-based generation, or full initialization are selected by adaptive routing for new queries
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: WorkflowGen 在早期执行中捕获完整 trajectories，抽取节点和 workflow 层经验并通过 template induction 形成 reusable workflow；后续只在 variable nodes 上做 lightweight rewriting 和 experience updating。

[Title]: Co-Evolving Agents: Learning from Failures as Hard Negatives
- [Pathway]: Policy → Narrative → Policy (P7, P5)
- [Source Experience]: target-agent and auxiliary failure-agent predicted failure trajectories
- [Target Experience]: hard negative trajectories and improved target-agent policy
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: hard negatives sharpen the target agent's optimization boundary and improve generalization
- [Method]: ⟨RL: DPO⟩
- [Mechanism]: failure agent 通过 preference optimization 学习生成接近成功但仍失败的 hard negatives；target agent 将这些 informative failures 纳入优化，将原始失败经验转成 structured learning signals。

[Title]: View-oriented Conversation Compiler for Agent Trace Analysis
- [Pathway]: Narrative → Schematic → Narrative
- [Source Experience]: raw agent JSONL logs with nested tool calls, results, reasoning blocks, sub-agent invocations, compaction boundaries, and system directives
- [Target Experience]: structured views and more concise learned memory
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: compiled views replace raw text/JSON/YAML as reflector input, reducing token use and improving pass rates
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: Stage 1 对应 P2：VCC 用 compiler pipeline 将 raw logs 转成 full/UI/adaptive structured views；Stage 2 是 Schematic → Narrative：reflector 基于结构化视图产生更 concise learned memory。已知 P1-P7 不覆盖 Schematic → Narrative 这个后半段。

[Title]: Evolvable Embodied Agent for Robotic Manipulation via Long Short-Term Reflection and Optimization
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: task successes, failures, past experiences, and newly learned lessons
- [Target Experience]: dynamically refined prompts for VLM-based embodied policy planning
- [Source Modality]: [embodied]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: refined prompts support continuous self-evolution without extensive training
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: LSTRO 从 past experiences 和新 lesson 中抽取可用于 prompt refinement 的 reflective knowledge，动态更新 VLM planning prompts，以提升 VIMA-Bench manipulation task success。

[Title]: Self-Corrected Multimodal Large Language Model for End-to-End Robot Manipulation
- [Pathway]: Annotation Failed
- [Mechanism]: Abstract 为空，无法仅凭摘要判断源经验、目标载体或 Pathway。

[Title]: Self-driven Grounding: Large Language Model Agents with Automatical Language-aligned Skill Learning
- [Pathway]: Narrative → Schematic (P2)
- [Source Experience]: LLM-proposed subgoal hypotheses and environment verification outcomes
- [Target Experience]: generalized language-aligned skills
- [Source Modality]: [embodied]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: learned skills are used to accomplish more complex tasks that initially fail verification
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: SDG 先让 LLM 提出 sub-goal hypotheses，再通过环境交互验证可行性；verified subgoals guide generalized skill learning，将自然语言规划经验 grounded 到可复用技能。

[Title]: WorldGUI: An Interactive Benchmark for Desktop GUI Automation from Any Starting Point
- [Pathway]: Out of Scope
- [Mechanism]: 摘要主要贡献是 GUI benchmark 和一个包含 critique stages 的简单框架，未说明从历史交互经验到可复用 memory、workflow、evaluator 或 policy 的转化机制；属于缺少明确 experience transformation 的边界外情况。

[Title]: BLAZER: Bootstrapping LLM-based Manipulation Agents with Zero-Shot Data Generation
- [Pathway]: Policy → Narrative → Policy (P7, P5)
- [Source Experience]: zero-shot LLM-planner generated manipulation demonstrations in simulation
- [Target Experience]: finetuned LLM manipulation policy
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}
- [Utilization]: successful automatically generated examples are used to finetune the LLM and improve planning capability
- [Method]: ⟨SFT⟩
- [Mechanism]: LLM planner 在 simulation 中自动生成 diverse manipulation demonstrations，筛选 successful examples 后用于 finetune LLM policy，并迁移到 sensor-based real manipulation。

[Title]: A Real-to-Sim-to-Real Approach to Robotic Manipulation with VLM-Generated Iterative Keypoint Rewards
- [Pathway]: Narrative → Schematic → Policy (P2, P5)
- [Source Experience]: RGB-D observations, free-form instructions, sampled keypoints, and iterative visual feedback
- [Target Experience]: Python-based keypoint reward functions and RL manipulation policies
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {teacher}
- [Utilization]: generated rewards train RL policies in simulation, then policies are deployed in the real world
- [Method]: ⟨hybrid⟩
- [Mechanism]: Stage 1 对应 P2：VLM 根据 RGB-D scene、language instruction 和 keypoints 生成/修正 Python reward function；Stage 2 对应 P5：reward function 在 reconstructed simulation 中训练 RL policy，再 real-to-sim-to-real 部署。

[Title]: PAACE: A Plan-Aware Automated Agent Context Engineering Framework
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: synthetic agent workflows with stepwise compression supervision and successful teacher demonstrations
- [Target Experience]: plan-aware compressed contexts and compression supervision
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {teacher}
- [Utilization]: compressed contexts reduce context load while preserving agent correctness; distilled PAACE-FT compressors make the transformation cheaper
- [Method]: ⟨SFT⟩
- [Mechanism]: PAACE-Syn 生成带 stepwise compression supervision 的 synthetic workflows，PAACE 通过 next-k-task relevance、plan-structure analysis、instruction co-refinement 和 function-preserving compression 将长 context 转成 plan-aware condensations；PAACE-FT 将该能力蒸馏到小模型。

[Title]: Self-Improving Loops for Visual Robotic Planning
- [Pathway]: Policy → Narrative → Policy (P7, P5)
- [Source Experience]: self-produced visual robotic planning trajectories
- [Target Experience]: iteratively updated in-domain video model / visual planner
- [Source Modality]: [embodied]
- [Target Modality]: [embodied]
- [Experience Source]: {self}
- [Utilization]: self-collected online behaviors are used to update the video model for task-specific visual planning
- [Method]: ⟨SFT⟩
- [Mechanism]: SILVR 让 in-domain video model 在指定任务上生成 self-produced trajectories，并将这些在线行为反馈到模型训练中，多轮更新 visual planner，在无人工 reward/expert demos 情况下提升 robotic planning performance。

## Annotation Failures
- 「WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning」（block #89）—— Abstract 为空，无法仅凭摘要判断源经验、目标载体或 Pathway。
- 「Self-Corrected Multimodal Large Language Model for End-to-End Robot Manipulation」（block #99）—— Abstract 为空，无法仅凭摘要判断源经验、目标载体或 Pathway。
