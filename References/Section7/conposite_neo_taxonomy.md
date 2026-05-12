
# π-Par → N-Tok → π-Par


- Self-Improving Loops for Visual Robotic Planning
- SILVR 让 in-domain video model 在指定任务上生成 self-produced trajectories，并将这些在线行为反馈到模型训练中，多轮更新 visual planner，在无人工 reward/expert demos 情况下提升 robotic planning performance。

- BLAZER: Bootstrapping LLM-based Manipulation Agents with Zero-Shot Data Generation
- LLM planner 在 simulation 中自动生成 diverse manipulation demonstrations，筛选 successful examples 后用于 finetune LLM policy，并迁移到 sensor-based real manipulation。

- Co-Evolving Agents: Learning from Failures as Hard Negatives
- failure agent 通过 preference optimization 学习生成接近成功但仍失败的 hard negatives；target agent 将这些 informative failures 纳入优化，将原始失败经验转成 structured learning signals。

- AutoSurfer -- Teaching Web Agents through Comprehensive Surfing, Learning, and Modeling
- AutoSurfer 系统探索网站页面与 GUI elements，利用 exploration trajectories 指导 task synthesis，并将同一轨迹作为 hints 引导 agent trajectory refinement；最终数据用于 fine-tuning web agents。

- Self-Supervised Bootstrapping of Action-Predictive Embodied Reasoning
- R&B-EnCoRe 将 embodied reasoning 视作 latent variable，通过 importance-weighted variational inference 选择与成功控制最相关的 reasoning，生成 refined training dataset，再蒸馏进 VLA policy。摘要没有说明外部交互 reward，因此 source 记为 teacher/model-generated。

- Bootstrapping Language-Guided Navigation Learning with Self-Refining Data Flywheel
- generator 先产生 instruction-trajectory data pool 训练 navigator；trained navigator 过滤数据池得到高保真数据，再训练更好的 generator；更好的 generator 又产出下一轮 navigator 数据，形成 P7/P5 flywheel。

- MCTS-EP: Empowering Embodied Planning with Online Preference Optimization
- MCTS-enhanced agent 与 embodied environments 交互，收集 preference data；efficient multimodal reasoning 处理视觉/文本任务，iterative training pipeline 将 preference signal 内化到 embodied planning policy。


- Self-Improving LLM Agents at Test-Time
- agent 先识别自己 struggling 的样本，再由同一模型或 stronger teacher 生成相似训练样本，最后在 test-time fine-tuning 中把这些新样本内化为 policy adaptation。

- Iterative Trajectory Exploration for Multimodal Agents
- SPORT 先由语言模型合成多模态任务，再交替执行 step sampling 和 step verification；verifier 的 AI feedback 构成 step-wise preference data，随后通过 preference tuning 更新 controller policy。

- Hi-WM: Human-in-the-World-Model for Scalable Robot Post-Training
- Stage 1 对应 P7：base policy 在 world model 中 closed-loop rollout，并在失败状态缓存、回滚、分支；human 在 world model 中给出短 corrective actions，产生 dense correction trajectories；Stage 2 对应 P5：这些纠正轨迹进入 post-training 数据集更新 policy。

- Internalizing Agency from Reflective Experience
- Stage 1 对应 P7/P1：agent 在探索中总结环境反馈为 actionable experience，回溯到早期决策点并基于该经验探索修正分支；Stage 2 对应 P5：这些 experience-guided corrections 通过 SFT 内化到 policy。

- LLMs as Scalable, General-Purpose Simulators For Evolving Digital Agent Training
- Stage 1 对应 P7：LLM simulator 生成 UI states/transitions 并通过 guided rollout 包装为 coherent trajectories；Stage 2 对应 P5：trajectory wrapper 和 grow strategy 产出的数据被用于持续训练 digital agents。

- Mobile-Agent-v3: Fundamental Agents for GUI Automation
- Stage 1 对应 P7：Self-Evolving GUI Trajectory Production 在多平台虚拟环境中自动生成 query、验证正确性并迭代 refine trajectories；Stage 2 对应 P5：这些轨迹与异步 RL/TRPO-style online training 共同更新 GUI agent policy。

- Self-Improving Vision-Language-Action Models with Data Generation via Residual RL
-  Stage 1 对应 P7：lightweight residual actors 以 RL 探测 VLA failure regions 并收集 recovery-oriented trajectories；Stage 2 对应 P5：hybrid rollout 和 distribution-aware replay 筛选部署分布一致的数据，再用 SFT 蒸馏回 VLA。

- Scalable Data Synthesis for Computer Use Agents with Step-Level Filtering
- Stage 1 对应 P7：teacher CUA rollouts 外化为大量 GUI trajectories；Stage 2 对应 P1/P5：step-level filtering 保留正确步骤并补充 reasoning augmentation，形成 WebSTAR 后对 CUA policy 做 SFT；另有 Narrative → Evaluator 分支训练 StepRM。

- OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis
- Stage 1 对应 P7：现有 GUI agent 先探索环境并产生轨迹，再 retrospectively derive tasks；Stage 2 对应 P5：经 trajectory reward model 过滤后的高质量轨迹被用作 GUI agent training data。

- Watch Every Step! LLM Agent Learning via Iterative Step-level Process Refinement
- Stage 1 对应 P1：agent 沿 expert trajectory 探索并生成新动作，Monte Carlo step-level reward 与专家步骤比较后定位 discrepancy，形成 contrastive action pairs；Stage 2 对应 P5：这些 process-refined pairs 被用于训练 agent policy。


- Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training
- Stage 1 对应 P7：当前 actor 和 MCTS 生成错误轨迹、正确相邻路径和 error-step signals；Stage 2 对应 P5：从首个错误步骤开始拼接相邻正确路径，得到可训练的 critique/correction 数据，并迭代更新模型恢复能力。


- Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents
- Stage 1 对应 P7：agent 与环境交互收集失败轨迹，并与较优轨迹形成 preference pairs；Stage 2 对应 P5：DPO/contrastive learning 将这些偏好经验内化到 open LLM agent policy 中。



- OpenWebVoyager: Building Multimodal Web Agents via Iterative Real-World Exploration, Feedback and Optimization
- base model 先通过 imitation learning 获得基础能力；之后每轮由 agent 探索 open web 产生轨迹，general-purpose model 评价轨迹质量，优质轨迹再用于 policy improvement，构成 P7 到 P5 的循环。


# N-Tok → V-Par → π-Par

- The Lighthouse of Language: Enhancing LLM Agents via Critique-Guided Improvement
- CGI 将 actor 的环境探索轨迹转为 critic 训练信号，使 critic 学会生成细粒度 assessment 与 actionable revisions；actor 再学习利用这些 critiques，形成 evaluator-to-policy 的迭代改进。

- UI-Genie: A Self-Improving Approach for Iteratively Boosting MLLM-based Mobile GUI Agents
- Stage 1 对应 P4：通过规则验证、controlled corruption 和 hard negative mining 构造 reward-specific GUI 数据训练 UI-Genie-RM；Stage 2 对应 P6：reward model 在动态环境中指导探索和验证，生成 UI-Genie-Agent 数据并提升 agent policy。

- MagicGUI-RMS: A Multi-Agent Reward Model System for Self-Evolving GUI Agents via Automated Feedback Reflux
- Stage 1 对应 P4：结构化数据构造管线把 GUI trajectories 转成 reward learning datasets，训练 domain-specific 与 general-purpose RMs；Stage 2 对应 P6：RMS 在执行中识别错误动作、提出替代动作并通过 feedback reflux 更新 agent behavior。

- No More Stale Feedback: Co-Evolving Critics for Open-World Agent Learning
- 轨迹和多重 diagnoses 被用于训练随 policy 同步演化的 critic；critic 通过 saturation-aware gain shaping 被奖励为高分轨迹带来 incremental improvements，随后 dual-track GRPO 同时更新 critic 与 policy，避免 static critic 反馈 stale。

- Policy Improvement using Language Feedback Models
- Stage 1 对应 P4：visual trajectories 被 verbalized 后交给 LLM 产生 feedback，用于训练 LFM 判断 desirable actions；Stage 2 对应 P6：LFM 选择值得模仿的行为作为 imitation-learning 信号，提升 instruction-following policies。

- RLAnything: Forge Environment, Policy, and Reward Model in Completely Dynamic RL System
- RLAnything 从环境交互经验中同时优化 reward model 与 policy：RM 通过 consistency feedback 更新，policy 通过 step-wise/outcome feedback 和 RM signals 更新，environment adaptation 又利用二者 critic feedback 放大学习信号。

- LAGEA: Language Guided Embodied Agents for Robotic Manipulation
- VLM 将每次尝试总结为 schema-constrained reflection，定位 decisive trajectory moments 并与 visual state 对齐；goal progress 与 feedback agreement 被转成 bounded step-wise shaping rewards，随后用于 RL policy improvement。



# N-Tok (raw) → N-Tok (refined) → π-Par

- Skill-SD: [Abs: "turns agent's own trajectories into dynamic training-only supervision; importance-weighted reverse-KL loss for gradient-correct token-level distillation"]


- Online experiential learning for language models. 
- Privileged information distillation for language models.


# Policy → Narrative → Evaluator

- Scaling Autonomous Agents via Automatic Reward Modeling And Planning
- Stage 1 对应 P7：一个 LLM-based agent 随机探索环境并生成 diverse action trajectories；Stage 2 对应 P4：另一个 LLM 为每条轨迹分配 task intent、positive response 和 negative response，triplets 用于训练 reward model。

# 待定

- STeCa: Step-level Trajectory Calibration for LLM Agent Learning
- GUI-Reflection: Empowering Multimodal GUI Models with Self-Reflection Behavior
- RetroAgent: From Solving to Evolving via Retrospective Dual Intrinsic Feedback
- R3L: Reflect-then-Retry Reinforcement Learning with Language-Guided Exploration, Pivotal Credit, and Positive Amplification
- ReAct Meets ActRe: When Language Agents Enjoy Training Data Autonomy
- Reflection-Based Task Adaptation for Self-Improving VLA
- VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought
- Pre-Trained Language Models for Interactive Decision-Making
- CLEANER: Self-Purified Trajectories Boost Agentic Reinforcement Learning
- Weak-to-Strong Generalization with Failure Trajectories: A Tree-based Approach to Elicit Optimal Policy in Strong Models