Title: GUI-Shepherd: Reliable Process Reward and Verification for Long-Sequence GUI Tasks

URL: https://doi.org/10.48550/arXiv.2509.23738

Abstract: Autonomous agents for long-sequence Graphical User Interface tasks are hindered by sparse rewards and the intractable credit assignment problem. To address these challenges, we introduce GUI-Shepherd, a Process Reward Model that provides dense, step-by-step feedback to guide agents. GUI-Shepherd is trained on a diverse large-scale data set of $52$k interactions that features human-annotated scores and GPT-4o generated rationales, enabling it to serve both as a reward provider for RL training and as a verifier for inference. As far as we know, we are the first to conduct a systematic study of process supervision in GUI agents, across diverse settings from online long-horizon tasks to offline single-step prediction. On the online AndroidWorld benchmark, GUI-Shepherd improves success rate by $7.7$ points via multi-turn online PPO, significantly outperforming Outcome Reward Model based competitors. When used as an inference verifier, it brings $5.1$ points improvements. The benefits generalize to the offline AndroidControl benchmark, with gains of $2.2$ points as a reward provider and $4.3$ points as a verifier. Collectively, our results establish that high-fidelity process supervision is critical for building more capable GUI agents and present a generalizable solution.

中文翻译：长序列GUI任务的自主Agent受困于稀疏奖励和难以处理的信用分配问题。为解决这些问题，我们提出GUI-Shepherd，一个过程奖励模型，提供密集的逐步反馈来引导Agent。GUI-Shepherd在包含52k条交互的大规模多样化数据集上训练，具有人工标注分数和GPT-4o生成的推理说明，使其既可作为RL训练的奖励提供者，也可作为推理验证器。据我们所知，我们是首个对GUI Agent中的过程监督进行系统研究的工作，覆盖从在线长时域任务到离线单步预测的多种场景。在在线AndroidWorld基准上，GUI-Shepherd通过多轮在线PPO将成功率提升7.7个百分点，显著优于基于结果奖励模型的竞品方法。作为推理验证器使用时，带来5.1个百分点的提升。其收益可泛化到离线AndroidControl基准，作为奖励提供者提升2.2个百分点，作为验证器提升4.3个百分点。总体而言，我们的结果表明高保真过程监督对于构建能力更强的GUI Agent至关重要，并提供了一个可泛化的解决方案。

------

Title: Web-Shepherd: Advancing PRMs for Reinforcing Web Agents

URL: https://doi.org/10.48550/arXiv.2505.15277

Abstract: Web navigation is a unique domain that can automate many repetitive real-life tasks and is challenging as it requires long-horizon sequential decision making beyond typical multimodal large language model (MLLM) tasks. Yet, specialized reward models for web navigation that can be utilized during both training and test-time have been absent until now. Despite the importance of speed and cost-effectiveness, prior works have utilized MLLMs as reward models, which poses significant constraints for real-world deployment. To address this, in this work, we propose the first process reward model (PRM) called Web-Shepherd which could assess web navigation trajectories in a step-level. To achieve this, we first construct the WebPRM Collection, a large-scale dataset with 40K step-level preference pairs and annotated checklists spanning diverse domains and difficulty levels. Next, we also introduce the WebRewardBench, the first meta-evaluation benchmark for evaluating PRMs. In our experiments, we observe that our Web-Shepherd achieves about 30 points better accuracy compared to using GPT-4o on WebRewardBench. Furthermore, when testing on WebArena-lite by using GPT-4o-mini as the policy and Web-Shepherd as the verifier, we achieve 10.9 points better performance, in 10 less cost compared to using GPT-4o-mini as the verifier. Our model, dataset, and code are publicly available at LINK.

中文翻译：Web导航是一个独特的领域，可以自动化许多重复的现实任务，且具有挑战性，因为它需要超越典型多模态大语言模型（MLLM）任务的长时域序贯决策。然而，到目前为止，仍未出现可在训练和测试阶段使用的专用Web导航奖励模型。尽管速度和成本效益很重要，先前工作多使用MLLM作为奖励模型，这对实际部署构成了重大制约。本文中，我们提出首个过程奖励模型（PRM）Web-Shepherd，能够在步骤级别评估Web导航轨迹。为此，我们首先构建了WebPRM Collection，一个包含40K步骤级偏好对和标注检查清单的大规模数据集，涵盖不同领域和难度级别。其次，我们还引入了WebRewardBench，这是首个用于评估PRM的元评估基准。实验中，我们观察到Web-Shepherd在WebRewardBench上的准确率比GPT-4o高出约30个百分点。同时，在以GPT-4o-mini为策略、Web-Shepherd为验证器在WebArena-lite上测试时，性能提升10.9个百分点，成本仅为使用GPT-4o-mini作验证器的十分之一。我们的模型、数据集和代码已在LINK公开。

------

Title: OS-Oracle: A Comprehensive Framework for Cross-Platform GUI Critic Models

URL: https://doi.org/10.48550/arXiv.2512.16295

Abstract: With VLM-powered computer-using agents (CUAs) becoming increasingly capable at graphical user interface (GUI) navigation and manipulation, reliable step-level decision-making has emerged as a key bottleneck for real-world deployment. In long-horizon workflows, errors accumulate quickly and irreversible actions can cause unintended consequences, motivating critic models that assess each action before execution. While critic models offer a promising solution, their effectiveness is hindered by the lack of diverse, high-quality GUI feedback data and public critic benchmarks for step-level evaluation in computer use. To bridge these gaps, we introduce OS-Oracle that makes three core contributions: (1) a scalable data pipeline for synthesizing cross-platform GUI critic data; (2) a two-stage training paradigm combining supervised fine-tuning (SFT) and consistency-preserving group relative policy optimization (CP-GRPO); (3) OS-Critic Bench, a holistic benchmark for evaluating critic model performance across Mobile, Web, and Desktop platforms. Leveraging this framework, we curate a high-quality dataset containing 310k critic samples. The resulting critic model, OS-Oracle-7B, achieves state-of-the-art performance among open-source VLMs on OS-Critic Bench, and surpasses proprietary models on the mobile domain. Furthermore, when serving as a pre-critic, OS-Oracle-7B improves the performance of native GUI agents such as UI-TARS-1.5-7B in OSWorld and AndroidWorld environments. The code is open-sourced at https://github.com/numbmelon/OS-Oracle.

中文翻译：随着VLM驱动的计算机使用Agent（CUA）在GUI导航和操作方面能力日益增强，可靠的步骤级决策已成为实际部署的关键瓶颈。在长时域工作流中，错误会快速累积，不可逆操作可能引发非预期后果，这催生了对每次执行前评估动作的评判模型的需求。尽管评判模型提供了有前景的解决方案，但其有效性受限于缺乏多样化、高质量的GUI反馈数据和用于步骤级评估的公开评判基准。为弥补这些空白，我们提出OS-Oracle，做出三项核心贡献：(1) 可扩展的跨平台GUI评判数据合成管线；(2) 结合监督微调（SFT）与一致性保持分组相对策略优化（CP-GRPO）的两阶段训练范式；(3) OS-Critic Bench，一个跨移动端、Web端和桌面端的评判模型性能的整体基准。利用该框架，我们构建了包含310k个评判样本的高质量数据集。所得评判模型OS-Oracle-7B在OS-Critic Bench上取得开源VLM中最优性能，并在移动端领域超越商业模型。此外，作为预评判器，OS-Oracle-7B在OSWorld和AndroidWorld环境中提升了UI-TARS-1.5-7B等原生GUI Agent的性能。

------

Title: The Art of Building Verifiers for Computer Use Agents

URL: https://www.semanticscholar.org/paper/bba585a56bf7c9a861de68165a30c57c3f5b9388

Abstract: Verifying the success of computer use agent (CUA) trajectories is a critical challenge: without reliable verification, neither evaluation nor training signal can be trusted. In this paper, we present lessons learned from building a best-in-class verifier for web tasks we call the Universal Verifier. We design the Universal Verifier around four key principles: 1) constructing rubrics with meaningful, non-overlapping criteria to reduce noise; 2) separating process and outcome rewards that yield complementary signals, capturing cases where an agent follows the right steps but gets blocked or succeeds through an unexpected path; 3) distinguishing between controllable and uncontrollable failures scored via a cascading-error-free strategy for finer-grained failure understanding; and 4) a divide-and-conquer context management scheme that attends to all screenshots in a trajectory, improving reliability on longer task horizons. We validate these findings on CUAVerifierBench, a new set of CUA trajectories with both process and outcome human labels, showing that our Universal Verifier agrees with humans as often as humans agree with each other. We report a reduction in false positive rates to near zero compared to baselines like WebVoyager ($\geq$ 45\%) and WebJudge ($\geq$ 22\%). We emphasize that these gains stem from the cumulative effect of the design choices above. We also find that an auto-research agent achieves 70\% of expert quality in 5\% of the time, but fails to discover all strategies required to replicate the Universal Verifier. We open-source our Universal Verifier system along with CUAVerifierBench; available at https://github.com/microsoft/fara.

中文翻译：验证计算机使用Agent（CUA）轨迹的成功是一个关键挑战：没有可靠的验证，评估信号和训练信号都无法信任。本文中，我们分享了构建一流Web任务验证器Universal Verifier的经验教训。我们围绕四个关键原则设计Universal Verifier：1）构建具有有意义且非重叠标准的评分量规以减少噪声；2）分离过程奖励和结果奖励以产生互补信号，捕捉Agent执行正确步骤但受阻或通过意外路径成功的情况；3）通过无级联错误策略区分可控与不可控失败，实现更细粒度的失败理解；4）采用分治上下文管理方案关注轨迹中所有截图，提升更长任务时域的可靠性。我们在CUAVerifierBench上验证了这些发现，结果显示Universal Verifier与人类的一致性不亚于人类之间的一致性。我们的误报率比WebVoyager（≥45%）和WebJudge（≥22%）等基线降低到接近零。这些收益源自上述设计选择的累积效应。自动研究Agent在5%的时间内达到专家质量的70%，但未能发现复现Universal Verifier所需的所有策略。

------

Title: Autonomous Evaluation and Refinement of Digital Agents

URL: https://doi.org/10.48550/arXiv.2404.06474

Abstract: We show that domain-general automatic evaluators can significantly improve the performance of agents for web navigation and device control. We experiment with multiple evaluation models that trade off between inference cost, modularity of design, and accuracy. We validate the performance of these models in several popular benchmarks for digital agents, finding between 74.4 and 92.9% agreement with oracle evaluation metrics. Finally, we use these evaluators to improve the performance of existing agents via fine-tuning and inference-time guidance. Without any additional supervision, we improve state-of-the-art performance by 29% on the popular benchmark WebArena, and achieve around 75% relative improvement in device control settings.

中文翻译：我们展示了领域通用的自动评估器可以显著提升Web导航和设备控制Agent的性能。我们实验了多种在推理成本、设计模块化和准确率之间权衡的评估模型。在多个主流的数字Agent基准上验证了这些模型的性能，与Oracle评估指标的一致性在74.4%到92.9%之间。最后，我们使用这些评估器通过微调和推理时引导来提升现有Agent的性能。在没有任何额外监督的情况下，我们在主流基准WebArena上将最优性能提升了29%，在设备控制场景中取得了约75%的相对提升。

------

Title: OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards

URL: https://www.semanticscholar.org/paper/f91b1843f32aebe9dc1a904d528e8f35967fc834

Abstract: Reinforcement Learning (RL) has the potential to improve the robustness of GUI agents in stochastic environments, yet training is highly sensitive to the quality of the reward function. Existing reward approaches struggle to achieve both scalability and performance. To address this, we propose OS-Themis, a scalable and accurate multi-agent critic framework. Unlike a single judge, OS-Themis decomposes trajectories into verifiable milestones to isolate critical evidence for decision making and employs a review mechanism to strictly audit the evidence chain before making the final verdict. To facilitate evaluation, we further introduce OmniGUIRewardBench (OGRBench), a holistic cross-platform benchmark for GUI outcome rewards, where all evaluated models achieve their best performance under OS-Themis. Extensive experiments on AndroidWorld show that OS-Themis yields a 10.3% improvement when used to support online RL training, and a 6.9% gain when used for trajectory validation and filtering in the self-training loop, highlighting its potential to drive agent evolution.

中文翻译：强化学习（RL）有潜力提升GUI Agent在随机环境中的鲁棒性，但训练对奖励函数质量高度敏感。现有奖励方法难以同时实现可扩展性和高性能。为此，我们提出OS-Themis，一个可扩展且精确的多Agent评判框架。与单一评判器不同，OS-Themis将轨迹分解为可验证的里程碑以隔离决策关键证据，并采用审查机制在做出最终裁决前严格审计证据链。为便于评估，我们还引入了OmniGUIRewardBench（OGRBench），一个跨平台的GUI结果奖励整体基准，所有评估模型在OS-Themis下均达到最佳性能。在AndroidWorld上的大量实验表明，OS-Themis在支持在线RL训练时带来10.3%的改进，在自训练循环中用于轨迹验证和过滤时带来6.9%的增益，凸显其驱动Agent进化的潜力。

------

Title: Scaling Agents for Computer Use

URL: https://www.semanticscholar.org/paper/1121b26ee51a0765ca5bc2f4df2860254ae9e2d0

Abstract: Computer-use agents (CUAs) hold promise for automating everyday digital tasks, but their performance on long-horizon, complex problems remains unreliable. Single-rollout execution is brittle, with small errors compounding over time and leading to high variance in outcomes. While prior work has attempted to scale within a single rollout, such approaches have yielded limited gains. Scaling over multiple rollouts offers a more promising alternative but doing so effectively is challenging due to the difficulty of evaluating and selecting among long-horizon agent behaviors. We introduce Behavior Judge (BJudge), which addresses this challenge by representing agent executions as behavior narratives and comparing candidate behaviors at this level, substantially improving robustness and success rates. Using multiple rollouts, BJudge establishes a new state of the art (SoTA) in OSWorld at 72.6%, significantly outperforming prior methods and surpassing human-level performance at 72.36%, with comprehensive ablations validating key design choices. We further demonstrate strong generalization results to different operating systems on WindowsAgentArena and AndroidWorld. Crucially, our results highlight the strong effectiveness of scaling CUAs, when you do it right: effective scaling requires structured trajectory understanding and selection, and BJudge provides a practical framework to achieve this.

中文翻译：计算机使用Agent（CUA）有望自动完成日常数字任务，但在长时域、复杂问题上的表现仍不可靠。单次执行脆弱，小错误随时间累积导致结果高方差。先前工作尝试在单次执行内扩展，收效有限。多轮执行扩展提供了更有前景的替代方案，但由于难以评估和选择长时域Agent行为，有效实施具有挑战性。我们引入Behavior Judge（BJudge），通过将Agent执行表示为行为叙述并在该层面比较候选行为，大幅提升鲁棒性和成功率。利用多次执行，BJudge在OSWorld上以72.6%达到新最优，显著超越此前方法并超过人类水平（72.36%），全面的消融实验验证了关键设计选择。我们还展示了在WindowsAgentArena和AndroidWorld上跨操作系统的强泛化结果。关键发现是：正确实施时，扩展CUA非常有效；有效扩展需要结构化的轨迹理解与选择，BJudge提供了一个实用框架来实现这一点。

------

Title: Look Before You Leap: A GUI-Critic-R1 Model for Pre-Operative Error Diagnosis in GUI Automation

URL: https://doi.org/10.48550/arXiv.2506.04614

Abstract: In recent years, Multimodal Large Language Models (MLLMs) have been extensively utilized for multimodal reasoning tasks, including Graphical User Interface (GUI) automation. Unlike general offline multimodal tasks, GUI automation is executed in online interactive environments, necessitating step-by-step decision-making based on real-time status of the environment. This task has a lower tolerance for decision-making errors at each step, as any mistakes may cumulatively disrupt the process and potentially lead to irreversible outcomes like deletions or payments. To address these issues, we introduce a pre-operative critic mechanism that provides effective feedback prior to the actual execution, by reasoning about the potential outcome and correctness of actions. Specifically, we propose a Suggestion-aware Gradient Relative Policy Optimization (S-GRPO) strategy to construct our pre-operative critic model GUI-Critic-R1, incorporating a novel suggestion reward to enhance the reliability of the model's feedback. Furthermore, we develop a reasoning-bootstrapping based data collection pipeline to create a GUI-Critic-Train and a GUI-Critic-Test, filling existing gaps in GUI critic data. Static experiments on the GUI-Critic-Test across both mobile and web domains reveal that our GUI-Critic-R1 offers significant advantages in critic accuracy compared to current MLLMs. Dynamic evaluation on GUI automation benchmark further highlights the effectiveness and superiority of our model, as evidenced by improved success rates and operational efficiency.

中文翻译：近年来，多模态大语言模型（MLLM）被广泛用于多模态推理任务，包括GUI自动化。与一般的离线多模态任务不同，GUI自动化在在线交互环境中执行，需要基于环境实时状态进行逐步决策。该任务对每一步的决策错误容忍度更低，因为任何错误都可能累积性破坏过程并可能导致不可逆的后果（如删除或支付）。为解决这些问题，我们引入了术前评判机制，通过对动作潜在结果和正确性的推理，在实际执行前提供有效反馈。具体而言，我们提出Suggestion-aware Gradient Relative Policy Optimization（S-GRPO）策略来构建术前评判模型GUI-Critic-R1，引入新颖的建议奖励来增强模型反馈的可靠性。此外，我们开发了基于推理自举的数据收集管道，创建了GUI-Critic-Train和GUI-Critic-Test，填补了GUI评判数据的空白。在跨移动端和Web端的GUI-Critic-Test上的静态实验表明，GUI-Critic-R1在评判准确率上相比现有MLLM具有显著优势。在GUI自动化基准上的动态评估进一步验证了模型的有效性和优越性，表现为更高的成功率和操作效率。

------

Title: Let's Verify Step by Step

URL: https://doi.org/10.48550/arXiv.2305.20050

Abstract: In recent years, large language models have greatly improved in their ability to perform complex multi-step reasoning. However, even state-of-the-art models still regularly produce logical mistakes. To train more reliable models, we can turn either to outcome supervision, which provides feedback for a final result, or process supervision, which provides feedback for each intermediate reasoning step. Given the importance of training reliable models, and given the high cost of human feedback, it is important to carefully compare the both methods. Recent work has already begun this comparison, but many questions still remain. We conduct our own investigation, finding that process supervision significantly outperforms outcome supervision for training models to solve problems from the challenging MATH dataset. Our process-supervised model solves 78% of problems from a representative subset of the MATH test set. Additionally, we show that active learning significantly improves the efficacy of process supervision. To support related research, we also release PRM800K, the complete dataset of 800,000 step-level human feedback labels used to train our best reward model.

中文翻译：近年来，大语言模型在执行复杂多步推理方面取得了巨大进步。然而，即使是最先进的模型仍然经常出现逻辑错误。为训练更可靠的模型，我们可以采用结果监督（为最终结果提供反馈）或过程监督（为每个中间推理步骤提供反馈）。鉴于训练可靠模型的重要性以及人类反馈的高昂成本，仔细比较两种方法至关重要。近期工作已开始这一比较，但许多问题仍未解决。我们进行了自己的研究，发现在训练模型解决具有挑战性的MATH数据集问题时，过程监督显著优于结果监督。我们的过程监督模型解决了MATH测试集代表性子集中78%的问题。此外，我们证明主动学习显著提升了过程监督的效率。为支持相关研究，我们还发布了PRM800K，这是用于训练我们最佳奖励模型的800,000个步骤级人类反馈标签的完整数据集。

------

Title: AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress

URL: https://doi.org/10.1145/3774904.3792551

Abstract: Despite rapid development, large language models (LLMs) still encounter challenges in multi-turn decision-making tasks (i.e., agent tasks) like web shopping and browser navigation, which require making a sequence of intelligent decisions based on environmental feedback. Previous work for LLM agents typically relies on elaborate prompt engineering or fine-tuning with expert trajectories to improve performance. In this work, we take a different perspective: we explore constructing process reward models (PRMs) to evaluate each decision and guide the agent's decision-making process. Unlike LLM reasoning, where each step is scored based on correctness, actions in agent tasks do not have a clear-cut correctness. Instead, they should be evaluated based on their proximity to the goal and the progress they have made. Building on this insight, we propose a re-defined PRM for agent tasks, named AgentPRM, to capture both the interdependence between sequential decisions and their contribution to the final goal. This enables better progress tracking and exploration-exploitation balance. To scalably obtain labeled data for training AgentPRM, we employ a Temporal Difference-based (TD-based) estimation method combined with Generalized Advantage Estimation (GAE), which proves more sample-efficient than prior methods. Extensive experiments across different agentic tasks show that AgentPRM is over 8× more compute-efficient than baselines, and it demonstrates robust improvement when scaling up test-time compute. Moreover, we perform detailed analyses to show how our method works and offer more insights, e.g., applying AgentPRM to the reinforcement learning of LLM agents.

中文翻译：尽管发展迅速，大语言模型（LLM）在多轮决策任务（即Agent任务）如Web购物和浏览器导航中仍面临挑战，这些任务需要基于环境反馈做出一系列智能决策。先前LLM Agent的工作通常依赖于精细的提示工程或专家轨迹微调来提升性能。本文中，我们采用不同视角：探索构建过程奖励模型（PRM）来评估每一步决策并引导Agent的决策过程。与LLM推理不同（每步根据正确性评分），Agent任务中的动作没有明确的正确性。相反，应基于其与目标的接近程度和已取得的进展来评估。基于这一洞察，我们提出重新定义的Agent任务PRM——AgentPRM，捕捉序贯决策之间的相互依赖及其对最终目标的贡献。这使得更好的进度跟踪和探索-利用平衡成为可能。为规模化获取训练AgentPRM的标注数据，我们采用基于时间差分（TD）的估计方法结合广义优势估计（GAE），比先前方法样本效率更高。在多种Agent任务上的大量实验表明，AgentPRM的计算效率比基线高8倍以上，在扩展测试时计算时展现出稳健的性能提升。

------

Title: GAIA: A Data Flywheel System for Training GUI Test-Time Scaling Critic Models

URL: https://doi.org/10.48550/arXiv.2601.18197

Abstract: While Large Vision-Language Models (LVLMs) have significantly advanced GUI agents'capabilities in parsing textual instructions, interpreting screen content, and executing tasks, a critical challenge persists: the irreversibility of agent operations, where a single erroneous action can trigger catastrophic deviations. To address this, we propose the GUI Action Critic's Data Flywheel System (GAIA), a training framework that enables the models to have iterative critic capabilities, which are used to improve the Test-Time Scaling (TTS) of basic GUI agents'performance. Specifically, we train an Intuitive Critic Model (ICM) using positive and negative action examples from a base agent first. This critic evaluates the immediate correctness of the agent's intended actions, thereby selecting operations with higher success probability. Then, the initial critic guides agent actions to collect refined positive/negative samples, initiating the self-improving cycle. The augmented data then trains a second-round critic with enhanced discernment capability. We conduct experiments on various datasets and demonstrate that the proposed ICM can improve the test-time performance of various closed-source and open-source models, and the performance can be gradually improved as the data is recycled. The code and dataset will be publicly released.

中文翻译：尽管大视觉语言模型（LVLM）显著提升了GUI Agent解析文本指令、解释屏幕内容和执行任务的能力，一个关键挑战依然存在：Agent操作的不可逆性，单个错误动作可能触发灾难性偏离。为此，我们提出GUI Action Critic's Data Flywheel System（GAIA），一个训练框架使模型具备迭代评判能力，用于提升基础GUI Agent的测试时扩展（TTS）性能。具体而言，我们首先使用基础Agent的正负动作示例训练一个直觉评判模型（ICM）。该评判器评估Agent意图动作的即时正确性，从而选择具有更高成功概率的操作。然后，初始评判器指导Agent动作以收集精炼的正负样本，启动自我改进循环。增强的数据随后训练第二轮具有更强辨别能力的评判器。我们在多种数据集上进行了实验，证明所提出的ICM可以提升多种闭源和开源模型的测试时性能，且性能可随着数据循环利用逐步提升。

------

Title: Advancing Mobile GUI Agents: A Verifier-Driven Approach to Practical Deployment

URL: https://doi.org/10.48550/arXiv.2503.15937

Abstract: We propose V-Droid, a mobile GUI task automation agent. Unlike previous mobile agents that utilize Large Language Models (LLMs) as generators to directly generate actions at each step, V-Droid employs LLMs as verifiers to evaluate candidate actions before making final decisions. To realize this novel paradigm, we introduce a comprehensive framework for constructing verifier-driven mobile agents: the discretized action space construction coupled with the prefilling-only workflow to accelerate the verification process, the pair-wise progress preference training to significantly enhance the verifier's decision-making capabilities, and the scalable human-agent joint annotation scheme to efficiently collect the necessary data at scale. V-Droid obtains a substantial task success rate across several public mobile task automation benchmarks: 59.5% on AndroidWorld, 38.3% on AndroidLab, and 49% on MobileAgentBench, surpassing existing agents by 5.2%, 2.1%, and 9%, respectively. Furthermore, V-Droid achieves a remarkably low latency of 4.3s per step, which is 6.1x faster compared with existing mobile agents. The source code is available at https://github.com/V-Droid-Agent/V-Droid.

中文翻译：我们提出V-Droid，一个移动端GUI任务自动化Agent。与以往每一步直接使用大语言模型（LLM）作为生成器来直接生成动作的移动端Agent不同，V-Droid将LLM用作验证器，在做出最终决策前评估候选动作。为实现这一新范式，我们引入了一个全面的框架：离散化动作空间构建配合仅预填充工作流加速验证过程，成对进度偏好训练显著增强验证器的决策能力，以及可扩展的人机联合标注方案高效规模化收集必要数据。V-Droid在多个公开移动端任务自动化基准上取得了显著的任务成功率：AndroidWorld上59.5%，AndroidLab上38.3%，MobileAgentBench上49%，分别超越现有Agent 5.2%、2.1%和9%。此外，V-Droid实现了每步仅4.3秒的极低延迟，比现有移动端Agent快6.1倍。

------

Title: WebArbiter: A Principle-Guided Reasoning Process Reward Model for Web Agents

URL: https://doi.org/10.48550/arXiv.2601.21872

Abstract: Web agents hold great potential for automating complex computer tasks, yet their interactions involve long-horizon, sequential decision-making with irreversible actions. In such settings, outcome-based supervision is sparse and delayed, often rewarding incorrect trajectories and failing to support inference-time scaling. This motivates the use of Process Reward Models (WebPRMs) for web navigation, but existing approaches remain limited: scalar WebPRMs collapse progress into coarse, weakly grounded signals, while checklist-based WebPRMs rely on brittle template matching that fails under layout or semantic changes and often mislabels superficially correct actions as successful, providing little insight or interpretability. To address these challenges, we introduce WebArbiter, a reasoning-first, principle-inducing WebPRM that formulates reward modeling as text generation, producing structured justifications that conclude with a preference verdict and identify the action most conducive to task completion under the current context. Training follows a two-stage pipeline: reasoning distillation equips the model with coherent principle-guided reasoning, and reinforcement learning corrects teacher biases by directly aligning verdicts with correctness, enabling stronger generalization. To support systematic evaluation, we release WebPRMBench, a comprehensive benchmark spanning four diverse web environments with rich tasks and high-quality preference annotations. On WebPRMBench, WebArbiter-7B outperforms the strongest baseline, GPT-5, by 9.1 points. In reward-guided trajectory search on WebArena-Lite, it surpasses the best prior WebPRM by up to 6.4 points, underscoring its robustness and practical value in complex web tasks.

中文翻译：Web Agent在自动化复杂计算机任务方面潜力巨大，但其交互涉及长时域、序贯决策，且包含不可逆操作。在这种设定下，基于结果的监督稀疏且延迟，经常奖励错误的轨迹，且无法支持推理时扩展。这促使了Web导航过程奖励模型（WebPRM）的使用，但现有方法仍存在局限：标量WebPRM将进展坍缩为粗糙、依据薄弱的信号，而基于检查清单的WebPRM依赖脆弱的模板匹配，在布局或语义变化下失效，并常常将表面正确的动作错误标注为成功，提供的洞察和可解释性有限。为解决这些挑战，我们提出WebArbiter，一个推理优先、原则引导的WebPRM，将奖励建模形式化为文本生成，产生结构化论证并以偏好裁决和动作推荐作结。训练遵循两阶段管线：推理蒸馏为模型配备连贯的原则引导推理能力，强化学习通过直接对齐裁决与正确性来纠正教师偏差，实现更强的泛化。为支持系统性评估，我们发布了WebPRMBench，一个覆盖四个多样化Web环境、具有丰富任务和高质量偏好标注的综合基准。在WebPRMBench上，WebArbiter-7B比最强基线GPT-5高出9.1个点。在WebArena-Lite的奖励引导轨迹搜索中，比此前最佳WebPRM最高提升6.4个点。

------

Title: Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning

URL: https://doi.org/10.48550/arXiv.2410.08146

Abstract: A promising approach for improving reasoning in large language models is to use process reward models (PRMs). PRMs provide feedback at each step of a multi-step reasoning trace, potentially improving credit assignment over outcome reward models (ORMs) that only provide feedback at the final step. However, collecting dense, per-step human labels is not scalable, and training PRMs from automatically-labeled data has thus far led to limited gains. To improve a base policy by running search against a PRM or using it as dense rewards for reinforcement learning (RL), we ask:"How should we design process rewards?". Our key insight is that, to be effective, the process reward for a step should measure progress: a change in the likelihood of producing a correct response in the future, before and after taking the step, corresponding to the notion of step-level advantages in RL. Crucially, this progress should be measured under a prover policy distinct from the base policy. We theoretically characterize the set of good provers and our results show that optimizing process rewards from such provers improves exploration during test-time search and online RL. In fact, our characterization shows that weak prover policies can substantially improve a stronger base policy, which we also observe empirically. We validate our claims by training process advantage verifiers (PAVs) to predict progress under such provers, and show that compared to ORMs, test-time search against PAVs is $>8\%$ more accurate, and $1.5-5\times$ more compute-efficient. Online RL with dense rewards from PAVs enables one of the first results with $5-6\times$ gain in sample efficiency, and $>6\%$ gain in accuracy, over ORMs.

中文翻译：改进大语言模型推理的一个有前景的方法是使用过程奖励模型（PRM）。PRM在多步推理轨迹的每一步提供反馈，相比仅在最终步提供反馈的结果奖励模型（ORM），可能改善信用分配。然而，收集密集的逐步人类标签无法规模化，而基于自动标注数据训练的PRM迄今收益有限。为通过基于PRM的搜索或将其作为强化学习的密集奖励来改进基础策略，我们追问：应该如何设计过程奖励。我们的核心洞察是：要有效，每一步的过程奖励应衡量进展——即在该步前后，未来产生正确响应可能性的变化，对应RL中步骤级优势的概念。关键的是，这个进展应在一个不同于基础策略的证明策略下衡量。我们从理论上刻画了好的证明器集合，结果表明从此类证明器优化过程奖励能改善测试时搜索和在线RL中的探索。事实上，我们的刻画表明弱证明策略可以显著改进强基础策略，我们也经验性地观察到了这一点。我们通过训练过程优势验证器（PAV）来预测此类证明器下的进展以验证我们的主张，结果表明，相比ORM，基于PAV的测试时搜索准确率提升超过8%，计算效率提升1.5-5倍。使用PAV密集奖励的在线RL实现了样本效率5-6倍提升和准确率超过6%提升的首批结果之一。

------

Title: Video-Based Reward Modeling for Computer-Use Agents

URL: https://www.semanticscholar.org/paper/1e898ee0ab5821caefb7d4d2c089d72272f27934

Abstract: Computer-using agents (CUAs) are becoming increasingly capable; however, it remains difficult to scale evaluation of whether a trajectory truly fulfills a user instruction. In this work, we study reward modeling from execution video: a sequence of keyframes from an agent trajectory that is independent of the agent's internal reasoning or actions. Although video-execution modeling is method-agnostic, it presents key challenges, including highly redundant layouts and subtle, localized cues that determine success. We introduce Execution Video Reward 53k (ExeVR-53k), a dataset of 53k high-quality video--task--reward triplets. We further propose adversarial instruction translation to synthesize negative samples with step-level annotations. To enable learning from long, high-resolution execution videos, we design spatiotemporal token pruning, which removes homogeneous regions and persistent tokens while preserving decisive UI changes. Building on these components, we fine-tune an Execution Video Reward Model (ExeVRM) that takes only a user instruction and a video-execution sequence to predict task success. Our ExeVRM 8B achieves 84.7% accuracy and 87.7% recall on video-execution assessment, outperforming strong proprietary models such as GPT-5.2 and Gemini-3 Pro across Ubuntu, macOS, Windows, and Android, while providing more precise temporal attribution. These results show that video-execution reward modeling can serve as a scalable, model-agnostic evaluator for CUAs.

中文翻译：计算机使用Agent（CUA）正变得日益强大，但评估其轨迹是否真正满足用户指令仍难以规模化。本文中，我们研究基于执行视频的奖励建模：从Agent轨迹中提取的关键帧序列，独立于Agent的内部推理或动作。尽管视频执行建模是方法无关的，但它面临关键挑战，包括高度冗余的布局和决定成败的微妙局部线索。我们引入Execution Video Reward 53k（ExeVR-53k），一个包含53k高质量视频-任务-奖励三元组的数据集。我们进一步提出对抗性指令翻译来合成具有步骤级标注的负样本。为从长时、高分辨率执行视频中学习，我们设计了时空token剪枝方法，移除同质区域和持续token，同时保留决定性的UI变化。基于这些组件，我们微调了一个Execution Video Reward Model（ExeVRM），仅以用户指令和视频执行序列为输入，预测任务成功。我们的ExeVRM 8B在视频执行评估上达到84.7%准确率和87.7%召回率，在Ubuntu、macOS、Windows和Android上超越GPT-5.2和Gemini-3 Pro等强商业模型，同时提供更精确的时间归因。

------

Title: Improve Mathematical Reasoning in Language Models by Automated Process Supervision

URL: https://www.semanticscholar.org/paper/f32bcc2155997110a7905da050df4c8404867b24

Abstract: Complex multi-step reasoning tasks, such as solving mathematical problems or generating code, remain a significant hurdle for even the most advanced large language models (LLMs). Verifying LLM outputs with an Outcome Reward Model (ORM) is a standard inference-time technique aimed at enhancing the reasoning performance of LLMs. However, this still proves insufficient for reasoning tasks with a lengthy or multi-hop reasoning chain, where the intermediate outcomes are neither properly rewarded nor penalized. Process supervision addresses this limitation by assigning intermediate rewards during the reasoning process. To date, the methods used to collect process supervision data have relied on either human annotation or per-step Monte Carlo estimation, both prohibitively expensive to scale, thus hindering the broad application of this technique. In response to this challenge, we propose a novel divide-and-conquer style Monte Carlo Tree Search (MCTS) algorithm named \textit{OmegaPRM} for the efficient collection of high-quality process supervision data. This algorithm swiftly identifies the first error in the Chain of Thought (CoT) with binary search and balances the positive and negative examples, thereby ensuring both efficiency and quality. As a result, we are able to collect over 1.5 million process supervision annotations to train Process Reward Models (PRMs). This fully automated process supervision alongside the weighted self-consistency algorithm is able to enhance LLMs' math reasoning performances. We improved the success rates of the instruction-tuned Gemini Pro model from 51\% to 69.4\% on MATH500 and from 86.4\% to 93.6\% on GSM8K. Similarly, we boosted the success rates of Gemma2 27B from 42.3\% to 58.2\% on MATH500 and from 74.0\% to 92.2\% on GSM8K. The entire process operates without any human intervention or supervision, making our method both financially and ...

中文翻译：复杂多步推理任务（如解决数学问题或生成代码）即使对最先进的大语言模型（LLM）而言仍是一个显著障碍。使用结果奖励模型（ORM）验证LLM输出是一种标准的推理时技术，旨在增强LLM的推理性能。然而，对于具有冗长或多跳推理链的推理任务，由于中间结果既未得到适当的奖励也未受到惩罚，该技术仍显不足。过程监督通过在推理过程中分配中间奖励来解决这一局限。迄今，收集过程监督数据的方法依赖人类标注或逐步蒙特卡洛估计，两者规模化成本都极高。为应对这一挑战，我们提出了一种新颖的分治式蒙特卡洛树搜索（MCTS）算法OmegaPRM，用于高效收集高质量过程监督数据。该算法通过二分搜索快速定位思维链（CoT）中的首个错误，并平衡正负样本。结果，我们能够收集超过150万条过程监督标注来训练过程奖励模型（PRM）。这种全自动过程监督与加权自一致性算法相结合，增强了LLM的数学推理性能。我们将Gemini Pro模型的成功率在MATH500上从51%提升至69.4%，在GSM8K上从86.4%提升至93.6%。类似地，我们将Gemma2 27B的成功率在MATH500上从42.3%提升至58.2%，在GSM8K上从74.0%提升至92.2%。整个过程无需任何人类干预或监督。

------

Title: UI-Genie: A Self-Improving Approach for Iteratively Boosting MLLM-based Mobile GUI Agents

URL: https://doi.org/10.48550/arXiv.2505.21496

Abstract: In this paper, we introduce UI-Genie, a self-improving framework addressing two key challenges in GUI agents: verification of trajectory outcome is challenging and high-quality training data are not scalable. These challenges are addressed by a reward model and a self-improving pipeline, respectively. The reward model, UI-Genie-RM, features an image-text interleaved architecture that efficiently pro- cesses historical context and unifies action-level and task-level rewards. To sup- port the training of UI-Genie-RM, we develop deliberately-designed data genera- tion strategies including rule-based verification, controlled trajectory corruption, and hard negative mining. To address the second challenge, a self-improvement pipeline progressively expands solvable complex GUI tasks by enhancing both the agent and reward models through reward-guided exploration and outcome verification in dynamic environments. For training the model, we generate UI- Genie-RM-517k and UI-Genie-Agent-16k, establishing the first reward-specific dataset for GUI agents while demonstrating high-quality synthetic trajectory gen- eration without manual annotation. Experimental results show that UI-Genie achieves state-of-the-art performance across multiple GUI agent benchmarks with three generations of data-model self-improvement. We open-source our complete framework implementation and generated datasets to facilitate further research in https://github.com/Euphoria16/UI-Genie.

中文翻译：本文中我们介绍UI-Genie，一个自我改进框架，解决GUI Agent中的两个关键挑战：轨迹结果的验证困难和高质量训练数据无法规模化。这些挑战分别通过奖励模型和自我改进管线来解决。奖励模型UI-Genie-RM采用图文交错架构，高效处理历史上下文并统一动作级和任务级奖励。为支持UI-Genie-RM的训练，我们开发了精心设计的数据生成策略，包括基于规则的验证、受控轨迹破坏和困难负样本挖掘。为解决第二个挑战，自我改进管线通过奖励引导的探索和动态环境中的结果验证，同步增强Agent和奖励模型，逐步扩展可解决的复杂GUI任务。为训练模型，我们生成了UI-Genie-RM-517k和UI-Genie-Agent-16k，建立了首个GUI Agent专用奖励数据集，同时展示无需人工标注的高质量合成轨迹生成。实验结果表明，经过三代数据-模型自我改进，UI-Genie在多个GUI Agent基准上达到最优性能。

------

Title: IntentScore: Intent-Conditioned Action Evaluation for Computer-Use Agents

URL: https://www.semanticscholar.org/paper/3d10fbb268db72400148bca70f0cdab26338cb1d

Abstract: Computer-Use Agents (CUAs) leverage large language models to execute GUI operations on desktop environments, yet they generate actions without evaluating action quality, leading to irreversible errors that cascade through subsequent steps. We propose IntentScore, a plan-aware reward model that learns to score candidate actions from 398K offline GUI interaction steps spanning three operating systems. IntentScore trains with two complementary objectives: contrastive alignment for state-action relevance and margin ranking for action correctness. Architecturally, it embeds each candidate's planning intent in the action encoder, enabling discrimination between candidates with similar actions but different rationales. IntentScore achieves 97.5% pairwise discrimination accuracy on held-out evaluation. Deployed as a re-ranker for Agent S3 on OSWorld, an environment entirely unseen during training, IntentScore improves task success rate by 6.9 points, demonstrating that reward estimation learned from heterogeneous offline trajectories generalizes to unseen agents and task distributions.

中文翻译：计算机使用Agent（CUA）利用大语言模型在桌面环境上执行GUI操作，但它们在生成动作时不评估动作质量，导致不可逆错误在后续步骤中级联传播。我们提出IntentScore，一个计划感知的奖励模型，从398K个离线GUI交互步骤（跨三个操作系统）学习为候选动作评分。IntentScore使用两个互补目标进行训练：状态-动作相关性的对比对齐和动作正确性的边际排序。在架构上，它在动作编码器中嵌入每个候选动作的计划意图，能够区分动作相似但推理逻辑不同的候选。IntentScore在留出评估上达到97.5%的成对判别准确率。作为Agent S3在OSWorld上的重排序器（该环境在训练期间完全未见），IntentScore将任务成功率提升6.9个百分点，表明从异构离线轨迹学到的奖励估计可泛化到未见Agent和任务分布。

------

Title: ProgRM: Build Better GUI Agents with Progress Rewards

URL: https://doi.org/10.48550/arXiv.2505.18121

Abstract: LLM-based (Large Language Model) GUI (Graphical User Interface) agents can potentially reshape our daily lives significantly. However, current LLM-based GUI agents suffer from the scarcity of high-quality training data owing to the difficulties of trajectory collection and reward annotation. Existing works have been exploring LLMs to collect trajectories for imitation learning or to offer reward signals for online RL training. However, the Outcome Reward Model (ORM) used in existing works cannot provide finegrained feedback and can over-penalize the valuable steps in finally failed trajectories. To this end, we propose Progress Reward Model (ProgRM) to provide dense informative intermediate rewards by predicting a task completion progress for each step in online training. To handle the challenge of progress reward label annotation, we further design an efficient LCS-based (Longest Common Subsequence) self-annotation algorithm to discover the key steps in trajectories and assign progress labels accordingly. ProgRM is evaluated with extensive experiments and analyses. Actors trained with ProgRM outperform leading proprietary LLMs and ORM-trained actors, illustrating the effectiveness of ProgRM. The codes for experiments will be made publicly available upon acceptance.

中文翻译：基于LLM的GUI Agent有潜力显著重塑日常生活。然而，由于轨迹收集和奖励标注的困难，当前基于LLM的GUI Agent面临高质量训练数据稀缺的问题。现有工作探索使用LLM收集轨迹用于模仿学习，或为在线RL训练提供奖励信号。然而，现有工作中使用的结果奖励模型（ORM）无法提供细粒度反馈，且可能对最终失败轨迹中的有价值步骤过度惩罚。为此，我们提出进度奖励模型（ProgRM），通过预测每一步的任务完成进度，在在线训练中提供密集的信息性中间奖励。为应对进度奖励标签标注的挑战，我们进一步设计了基于最长公共子序列（LCS）的高效自标注算法，发现轨迹中的关键步骤并相应分配进度标签。大量实验和分析验证了ProgRM。使用ProgRM训练的Actor超越领先的商业LLM和ORM训练的Actor，说明了ProgRM的有效性。

------

Title: Generative Verifiers: Reward Modeling as Next-Token Prediction

URL: https://doi.org/10.48550/arXiv.2408.15240

Abstract: Verifiers or reward models are often used to enhance the reasoning performance of large language models (LLMs). A common approach is the Best-of-N method, where N candidate solutions generated by the LLM are ranked by a verifier, and the best one is selected. While LLM-based verifiers are typically trained as discriminative classifiers to score solutions, they do not utilize the text generation capabilities of pretrained LLMs. To overcome this limitation, we instead propose training verifiers using the ubiquitous next-token prediction objective, jointly on verification and solution generation. Compared to standard verifiers, such generative verifiers (GenRM) can benefit from several advantages of LLMs: they integrate seamlessly with instruction tuning, enable chain-of-thought reasoning, and can utilize additional test-time compute via majority voting for better verification. We demonstrate that GenRM outperforms discriminative, DPO verifiers, and LLM-as-a-Judge, resulting in large performance gains with Best-of-N, namely 5% $\rightarrow$ 45.3% on algorithmic tasks and 73% $\rightarrow$ 93.4% on GSM8K. In easy-to-hard generalization settings, we observe improvements of 28% $\rightarrow$ 44.6% on MATH, and 37.9% $\rightarrow$ 53.5% on MMLU abstract algebra. Furthermore, we find that training GenRM with synthetic verification rationales is sufficient to pick out subtle errors on math problems. Finally, we demonstrate that GenRM scales favorably with model size and test-time compute.

中文翻译：验证器或奖励模型通常用于增强大语言模型（LLM）的推理性能。常见方法是Best-of-N方法，由验证器对LLM生成的N个候选解进行排序，选择最佳解。虽然基于LLM的验证器通常被训练为判别式分类器来评分，但它们并未利用预训练LLM的文本生成能力。为克服这一局限，我们转而使用下一token预测目标来训练验证器，联合进行验证和解答生成。与标准验证器相比，这种生成式验证器（GenRM）享有LLM的多项优势：与指令微调无缝集成、支持思维链推理，以及可通过多数投票利用额外测试时计算获得更佳验证。我们证明GenRM优于判别式验证器和DPO验证器以及LLM-as-a-Judge，在Best-of-N上带来显著性能增益，即算法任务上从5%提升至45.3%，GSM8K上从73%提升至93.4%。在简单到困难泛化设定中，MATH上从28%提升至44.6%，MMLU抽象代数上从37.9%提升至53.5%。此外，仅使用合成验证推理训练GenRM就足以发现数学问题中的细微错误。GenRM随模型规模和测试时计算呈现良好的扩展行为。

------

Title: MagicGUI-RMS: A Multi-Agent Reward Model System for Self-Evolving GUI Agents via Automated Feedback Reflux

URL: https://doi.org/10.48550/arXiv.2601.13060

Abstract: Graphical user interface (GUI) agents are rapidly progressing toward autonomous interaction and reliable task execution across diverse applications. However, two central challenges remain unresolved: automating the evaluation of agent trajectories and generating high-quality training data at scale to enable continual improvement. Existing approaches often depend on manual annotation or static rule-based verification, which restricts scalability and limits adaptability in dynamic environments. We present MagicGUI-RMS, a multi-agent reward model system that delivers adaptive trajectory evaluation, corrective feedback, and self-evolving learning capabilities. MagicGUI-RMS integrates a Domain-Specific Reward Model (DS-RM) with a General-Purpose Reward Model (GP-RM), enabling fine-grained action assessment and robust generalization across heterogeneous GUI tasks. To support reward learning at scale, we design a structured data construction pipeline that automatically produces balanced and diverse reward datasets, effectively reducing annotation costs while maintaining sample fidelity. During execution, the reward model system identifies erroneous actions, proposes refined alternatives, and continuously enhances agent behavior through an automated data-reflux mechanism. Extensive experiments demonstrate that MagicGUI-RMS yields substantial gains in task accuracy, behavioral robustness. These results establish MagicGUI-RMS as a principled and effective foundation for building self-improving GUI agents driven by reward-based adaptation.

中文翻译：GUI Agent正快速迈向跨多样化应用的自主交互和可靠任务执行。然而，两个核心挑战仍未解决：自动化评估Agent轨迹和大规模生成高质量训练数据以实现持续改进。现有方法往往依赖人工标注或静态规则验证，限制了可扩展性和动态环境中的适应性。我们提出MagicGUI-RMS，一个多Agent奖励模型系统，提供自适应轨迹评估、纠正反馈和自我进化学习能力。MagicGUI-RMS将领域专用奖励模型（DS-RM）与通用奖励模型（GP-RM）集成，实现细粒度动作评估和跨异构GUI任务的鲁棒泛化。为支持规模化奖励学习，我们设计了结构化数据构建管线，自动产生平衡且多样化的奖励数据集，有效降低标注成本同时维持样本保真度。执行过程中，奖励模型系统识别错误动作，提出精炼替代方案，并通过自动化数据回流机制持续增强Agent行为。大量实验表明MagicGUI-RMS在任务准确率和行为鲁棒性方面带来显著增益。

------

Title: WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning

URL: https://doi.org/10.48550/arXiv.2411.02337

Abstract: Large language models (LLMs) have shown remarkable potential as autonomous agents, particularly in web-based tasks. However, existing LLM web agents heavily rely on expensive proprietary LLM APIs, while open LLMs lack the necessary decision-making capabilities. This paper introduces WebRL, a self-evolving online curriculum reinforcement learning framework designed to train high-performance web agents using open LLMs. WebRL addresses three key challenges in building LLM web agents, including the scarcity of training tasks, sparse feedback signals, and policy distribution drift in online learning. Specifically, WebRL incorporates 1) a self-evolving curriculum that generates new tasks from unsuccessful attempts, 2) a robust outcome-supervised reward model (ORM), and 3) adaptive reinforcement learning strategies to ensure consistent improvements. We apply WebRL to transform open Llama-3.1 and GLM-4 models into proficient web agents. On WebArena-Lite, WebRL improves the success rate of Llama-3.1-8B from 4.8% to 42.4%, and from 6.1% to 43% for GLM-4-9B. These open models significantly surpass the performance of GPT-4-Turbo (17.6%) and GPT-4o (13.9%) and outperform previous state-of-the-art web agents trained on open LLMs (AutoWebGLM, 18.2%). Our findings demonstrate WebRL's effectiveness in bridging the gap between open and proprietary LLM-based web agents, paving the way for more accessible and powerful autonomous web interaction systems.

中文翻译：大语言模型（LLM）在自主Agent方面展现了显著潜力，尤其在基于Web的任务中。然而，现有LLM Web Agent严重依赖昂贵的商业LLM API，而开源LLM缺乏必要的决策能力。本文提出WebRL，一个自我进化在线课程强化学习框架，旨在使用开源LLM训练高性能Web Agent。WebRL解决了构建LLM Web Agent的三个关键挑战：训练任务稀缺、反馈信号稀疏以及在线学习中的策略分布漂移。具体而言，WebRL包含：(1)自我进化课程，从失败尝试中生成新任务；(2)鲁棒的结果监督奖励模型（ORM）；(3)自适应强化学习策略，确保持续改进。我们应用WebRL将开源Llama-3.1和GLM-4模型转化为熟练的Web Agent。在WebArena-Lite上，WebRL将Llama-3.1-8B的成功率从4.8%提升至42.4%，将GLM-4-9B从6.1%提升至43%。这些开源模型显著超越GPT-4-Turbo（17.6%）和GPT-4o（13.9%），并超过此前最优的开源LLM Web Agent（AutoWebGLM，18.2%）。

------

Title: Solving math word problems with process- and outcome-based feedback

URL: https://doi.org/10.48550/arXiv.2211.14275

Abstract: Recent work has shown that asking language models to generate reasoning steps improves performance on many reasoning tasks. When moving beyond prompting, this raises the question of how we should supervise such models: outcome-based approaches which supervise the final result, or process-based approaches which supervise the reasoning process itself? Differences between these approaches might naturally be expected not just in final-answer errors but also in reasoning errors, which can be difficult to detect and are problematic in many real-world domains such as education. We run the first comprehensive comparison between process- and outcome-based approaches trained on a natural language task, GSM8K. We find that pure outcome-based supervision produces similar final-answer error rates with less label supervision. However, for correct reasoning steps we find it necessary to use process-based supervision or supervision from learned reward models that emulate process-based feedback. In total, we improve the previous best results from 16.8% $\to$ 12.7% final-answer error and 14.0% $\to$ 3.4% reasoning error among final-answer-correct solutions.

中文翻译：近期工作表明，要求语言模型生成推理步骤可以改善许多推理任务的性能。超出提示工程之外，这引发了我们应该如何监督此类模型的问题：监督最终结果的结果驱动方法，还是监督推理过程本身的过程驱动方法？这两种方法之间的差异自然可能不仅体现在最终答案错误上，也体现在推理错误上，后者难以检测，在教育等许多现实领域都存在问题。我们开展了过程驱动和结果驱动方法在自然语言任务GSM8K上的首次全面比较。我们发现纯结果监督在更少的标签监督下产生相似的最终答案错误率。然而，对于正确的推理步骤，我们发现需要使用过程监督或模拟过程反馈的学习奖励模型的监督。总体而言，我们将此前最优结果从16.8%的最终答案错误率降至12.7%，并将答案正确的解中推理错误率从14.0%降至3.4%。

------

Title: SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from Experience

URL: https://doi.org/10.48550/arXiv.2508.04700

Abstract: Repurposing large vision-language models (LVLMs) as computer use agents (CUAs) has led to substantial breakthroughs, primarily driven by human-labeled data. However, these models often struggle with novel and specialized software, particularly in scenarios lacking human annotations. To address this challenge, we propose SEAgent, an agentic self-evolving framework enabling CUAs to autonomously evolve through interactions with unfamiliar software. Specifically, SEAgent empowers computer-use agents to autonomously master novel software environments via experiential learning, where agents explore new software, learn through iterative trial-and-error, and progressively tackle auto-generated tasks organized from simple to complex. To achieve this goal, we design a World State Model for step-wise trajectory assessment, along with a Curriculum Generator that generates increasingly diverse and challenging tasks. The agent's policy is updated through experiential learning, comprised of adversarial imitation of failure actions and Group Relative Policy Optimization (GRPO) on successful ones. Furthermore, we introduce a specialist-to-generalist training strategy that integrates individual experiential insights from specialist agents, facilitating the development of a stronger generalist CUA capable of continuous autonomous evolution. This unified agent ultimately achieves performance surpassing ensembles of individual specialist agents on their specialized software. We validate the effectiveness of SEAgent across five novel software environments within OS-World. Our approach achieves a significant improvement of 23.2% in success rate, from 11.3% to 34.5%, over a competitive open-source CUA, i.e., UI-TARS.

中文翻译：将大视觉语言模型（LVLM）重新用作计算机使用Agent（CUA）已带来实质性突破，主要由人工标注数据驱动。然而，这些模型常常难以应对新颖和专用软件，尤其在缺乏人工标注的场景中。为解决这一挑战，我们提出SEAgent，一个Agent自我进化框架，使CUA能够通过与陌生软件的交互自主进化。具体而言，SEAgent通过经验学习赋予CUA自主掌握新软件环境的能力：Agent探索新软件，通过迭代试错学习，逐步解决从简单到复杂的自动生成任务。为实现这一目标，我们设计了用于逐步轨迹评估的世界状态模型，以及生成日益多样化和挑战性任务的课程生成器。Agent策略通过经验学习更新，包括对失败动作的对抗模仿和对成功动作的分组相对策略优化（GRPO）。我们还引入了从专家到通才的训练策略，整合来自专家Agent的个体经验洞察，促进更强通用CUA的发展，能够持续自主进化。在OS-World中五个新软件环境上验证了SEAgent的有效性，我们的方法取得23.2%的成功率显著提升（从11.3%到34.5%），超越竞品开源CUA UI-TARS。

------

Title: Vision-Language Models as Success Detectors

URL: https://doi.org/10.48550/arXiv.2303.07280

Abstract: Detecting successful behaviour is crucial for training intelligent agents. As such, generalisable reward models are a prerequisite for agents that can learn to generalise their behaviour. In this work we focus on developing robust success detectors that leverage large, pretrained vision-language models (Flamingo, Alayrac et al. (2022)) and human reward annotations. Concretely, we treat success detection as a visual question answering (VQA) problem, denoted SuccessVQA. We study success detection across three vastly different domains: (i) interactive language-conditioned agents in a simulated household, (ii) real world robotic manipulation, and (iii)"in-the-wild"human egocentric videos. We investigate the generalisation properties of a Flamingo-based success detection model across unseen language and visual changes in the first two domains, and find that the proposed method is able to outperform bespoke reward models in out-of-distribution test scenarios with either variation. In the last domain of"in-the-wild"human videos, we show that success detection on unseen real videos presents an even more challenging generalisation task warranting future work. We hope our initial results encourage further work in real world success detection and reward modelling.

中文翻译：检测成功行为对训练智能Agent至关重要。因此，可泛化的奖励模型是Agent能够泛化其行为的前提条件。本文中我们专注于开发鲁棒的成功检测器，利用大型预训练视觉语言模型（Flamingo）和人类奖励标注。我们研究成功检测跨三个截然不同的领域：(i) 模拟家居环境中的交互式语言条件Agent；(ii) 真实世界的机器人操作；(iii) 开放环境人类第一人称视频。我们研究了基于Flamingo的成功检测模型在前两个领域中面对未见语言和视觉变化的泛化性质，发现所提方法能在具有任一变化的分布外测试场景中超越定制奖励模型。在最后一个开放人类视频领域，我们发现在未见真实视频上的成功检测是一项更具挑战性的泛化任务，值得未来工作。我们希望初步结果能鼓励在真实世界成功检测和奖励建模方面的进一步研究。

------

Title: StepWiser: Stepwise Generative Judges for Wiser Reasoning

URL: https://doi.org/10.48550/arXiv.2508.19229

Abstract: As models increasingly leverage multi-step reasoning strategies to solve complex problems, supervising the logical validity of these intermediate steps has become a critical research challenge. Process reward models address this by providing step-by-step feedback, but current approaches have two major drawbacks: they typically function as classifiers without providing explanations, and their reliance on supervised fine-tuning with static datasets limits generalization. Inspired by recent advances, we reframe stepwise reward modeling from a classification task to a reasoning task itself. We thus propose a generative judge that reasons about the policy model's reasoning steps (i.e., meta-reasons), outputting thinking tokens before delivering a final verdict. Our model, StepWiser, is trained by reinforcement learning using relative outcomes of rollouts. We show it provides (i) better judgment accuracy on intermediate steps than existing methods; (ii) can be used to improve the policy model at training time; and (iii) improves inference-time search.

中文翻译：随着模型越来越多地利用多步推理策略来解决复杂问题，监督这些中间步骤的逻辑有效性已成为关键研究挑战。过程奖励模型通过提供逐步反馈来应对这一问题，但当前方法有两个主要缺陷：它们通常作为分类器运行而不提供解释，且依赖于静态数据集上的监督微调，限制了泛化能力。受近期进展启发，我们将逐步奖励建模从分类任务重新构建为推理任务本身。因此我们提出生成式评判器，对策略模型的推理步骤进行推理（即元推理），在给出最终裁决前输出思考token。我们的模型StepWiser通过强化学习使用rollout的相对结果进行训练。我们证明其：(i) 在中间步骤的判断准确率上优于现有方法；(ii) 可用于训练阶段改进策略模型；(iii) 改善了推理时搜索。

------

Title: GroundedPRM: Tree-Guided and Fidelity-Aware Process Reward Modeling for Step-Level Reasoning

URL: https://doi.org/10.48550/arXiv.2510.14942

Abstract: Process Reward Models (PRMs) aim to improve multi-step reasoning in Large Language Models (LLMs) by supervising intermediate steps and identifying errors. However, building effective PRMs remains challenging due to the lack of scalable, high-quality annotations. Existing approaches rely on costly human labeling, LLM-based self-evaluation that is prone to hallucination, or Monte Carlo (MC) estimation, which infers step quality solely from rollout outcomes and often introduces noisy, misaligned supervision due to credit misattribution. These issues result in three core limitations: noisy rewards, low factual fidelity, and misalignment with step-level reasoning objectives. To address these challenges, we introduce GroundedPRM, a tree-guided and fidelity-aware framework for automatic process supervision. To reduce reward noise and enable fine-grained credit assignment, we construct structured reasoning paths via Monte Carlo Tree Search (MCTS). To eliminate hallucinated supervision, we validate each intermediate step using an external tool, providing execution-grounded correctness signals. To combine both step-level validation and global outcome assessment, we design a hybrid reward aggregation mechanism that fuses tool-based verification with MCTS-derived feedback. Finally, we format the reward signal into a rationale-enhanced, generative structure to promote interpretability and compatibility with instruction-tuned LLMs. GroundedPRM is trained on only 40K automatically labeled samples, amounting to just 10% of the data used by the best-performing PRM trained with auto-labeled supervision. Nevertheless, it achieves up to a 26% relative improvement in average performance on ProcessBench. When used for reward-guided greedy search, GroundedPRM outperforms even PRMs trained with human-labeled supervision, offering a scalable and verifiable path toward high-quality process-level reasoning.

中文翻译：过程奖励模型（PRM）旨在通过监督中间步骤和识别错误来改进大语言模型（LLM）的多步推理。然而，由于缺乏可扩展的高质量标注，构建有效的PRM仍具挑战。现有方法依赖昂贵的人类标注、易产生幻觉的LLM自评估，或蒙特卡洛估计——后者仅从rollout结果推断步骤质量，常因信用错误归因引入噪声和偏差监督。这些问题导致三个核心局限：噪声奖励、低保真度和与步骤级推理目标的失配。为解决这些挑战，我们提出GroundedPRM，一个树引导且保真度感知的自动过程监督框架。为减少奖励噪声并实现细粒度信用分配，我们通过蒙特卡洛树搜索（MCTS）构建结构化推理路径。为消除幻觉监督，我们使用外部工具验证每个中间步骤，提供执行基础的信号。为结合步骤级验证和全局结果评估，我们设计了混合奖励聚合机制，融合工具验证与MCTS衍生反馈。最后，我们将奖励信号格式化为推理增强的生成结构以提升可解释性。GroundedPRM仅在40K自动标注样本上训练，仅为最佳性能自动标注PRM所用数据的10%，却在ProcessBench上平均性能相对提升高达26%。在奖励引导的贪婪搜索中，GroundedPRM甚至超越使用人工标注训练的PRM。

------

Title: OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis

URL: https://doi.org/10.48550/arXiv.2412.19723

Abstract: Graphical User Interface (GUI) agents powered by Vision-Language Models (VLMs) have demonstrated human-like computer control capability. Despite their utility in advancing digital automation, a critical bottleneck persists: collecting high-quality trajectory data for training. Common practices for collecting such data rely on human supervision or synthetic data generation through executing pre-defined tasks, which are either resource-intensive or unable to guarantee data quality. Moreover, these methods suffer from limited data diversity and significant gaps between synthetic data and real-world environments. To address these challenges, we propose OS-Genesis, a novel GUI data synthesis pipeline that reverses the conventional trajectory collection process. Instead of relying on pre-defined tasks, OS-Genesis enables agents first to perceive environments and perform step-wise interactions, then retrospectively derive high-quality tasks to enable trajectory-level exploration. A trajectory reward model is then employed to ensure the quality of the generated trajectories. We demonstrate that training GUI agents with OS-Genesis significantly improves their performance on highly challenging online benchmarks. In-depth analysis further validates OS-Genesis's efficiency and its superior data quality and diversity compared to existing synthesis methods. Our codes, data, and checkpoints are available at https://qiushisun.github.io/OS-Genesis-Home/.

中文翻译：由视觉语言模型（VLM）驱动的GUI Agent已展示出类人的计算机控制能力。尽管它们在推动数字自动化方面具有实用性，但一个关键瓶颈依然存在：为训练收集高质量的轨迹数据。现有的数据收集实践依赖人类监督或通过执行预定义任务合成数据，这些方法要么资源密集，要么无法保证数据质量，且面临数据多样性有限以及合成数据与真实环境存在显著差距的问题。为应对这些挑战，我们提出OS-Genesis，一种新颖的GUI数据合成管线，逆向了传统的轨迹收集流程。OS-Genesis不依赖预定义任务，而是让Agent首先感知环境并执行逐步交互，然后回溯性地推导出高质量任务以实现轨迹级探索。随后使用轨迹奖励模型确保生成轨迹的质量。我们证明使用OS-Genesis训练GUI Agent能显著提升其在极具挑战性的在线基准上的性能。深入分析进一步验证了OS-Genesis的效率及其相较现有合成方法在数据质量和多样性上的优越性。

------

Title: RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning

URL: https://doi.org/10.48550/arXiv.2505.15034

Abstract: Reinforcement learning (RL) has recently emerged as a compelling approach for enhancing the reasoning capabilities of large language models (LLMs), where an LLM generator serves as a policy guided by a verifier (reward model). However, current RL post-training methods for LLMs typically use verifiers that are fixed (rule-based or frozen pretrained) or trained discriminatively via supervised fine-tuning (SFT). Such designs are susceptible to reward hacking and generalize poorly beyond their training distributions. To overcome these limitations, we propose Tango, a novel framework that uses RL to concurrently train both an LLM generator and a verifier in an interleaved manner. A central innovation of Tango is its generative, process-level LLM verifier, which is trained via RL and co-evolves with the generator. Importantly, the verifier is trained solely based on outcome-level verification correctness rewards without requiring explicit process-level annotations. This generative RL-trained verifier exhibits improved robustness and superior generalization compared to deterministic or SFT-trained verifiers, fostering effective mutual reinforcement with the generator. Extensive experiments demonstrate that both components of Tango achieve state-of-the-art results among 7B/8B-scale models: the generator attains best-in-class performance across five competition-level math benchmarks and four challenging out-of-domain reasoning tasks, while the verifier leads on the ProcessBench dataset. Remarkably, both components exhibit particularly substantial improvements on the most difficult mathematical reasoning problems. Code is at: https://github.com/kaiwenzha/rl-tango.

中文翻译：强化学习（RL）最近成为增强大语言模型（LLM）推理能力的引人注目方法，其中LLM生成器作为策略由验证器（奖励模型）引导。然而，当前LLM的RL后训练方法通常使用固定的（基于规则或冻结预训练）或通过监督微调（SFT）判别式训练的验证器。此类设计易受奖励黑客攻击且在训练分布外泛化较差。为克服这些局限，我们提出Tango，一个新颖框架，使用RL以交错方式同时训练LLM生成器和验证器。Tango的核心创新是其生成式、过程级LLM验证器，该验证器通过RL训练并与生成器共同进化。重要的是，验证器仅基于结果级验证正确性奖励进行训练，无需明确的过程级标注。这种生成式RL训练验证器相比确定性或SFT训练验证器展现出更好的鲁棒性和更强的泛化能力，促进了与生成器的有效相互强化。在7B/8B规模模型中，Tango的两个组件均取得最优结果：生成器在五个竞赛级数学基准上取得最佳性能，验证器在ProcessBench上领先。两个组件在最困难的数学推理问题上改善尤为显著。

------

Title: SOLE-R1: Video-Language Reasoning as the Sole Reward for On-Robot Reinforcement Learning

URL: https://www.semanticscholar.org/paper/5554407b7bfd03db757ead480f520135d3df933f

Abstract: Vision-language models (VLMs) have shown impressive capabilities across diverse tasks, motivating efforts to leverage these models to supervise robot learning. However, when used as evaluators in reinforcement learning (RL), today's strongest models often fail under partial observability and distribution shift, enabling policies to exploit perceptual errors rather than solve the task. To address this limitation, we introduce SOLE-R1 (Self-Observing LEarner), a video-language reasoning model explicitly designed to serve as the sole reward signal for online RL. Given only raw video observations and a natural-language goal, SOLE-R1 performs per-timestep spatiotemporal chain-of-thought (CoT) reasoning and produces dense estimates of task progress that can be used directly as rewards. To train SOLE-R1, we develop a large-scale video trajectory and reasoning synthesis pipeline that generates temporally grounded CoT traces aligned with continuous progress supervision. This data is combined with foundational spatial and multi-frame temporal reasoning, and used to train the model with a hybrid framework that couples supervised fine-tuning with RL from verifiable rewards. Across four different simulation environments and a real-robot setting, SOLE-R1 enables zero-shot online RL from random initialization: robots learn previously unseen manipulation tasks without ground-truth rewards, success indicators, demonstrations, or task-specific tuning. SOLE-R1 succeeds on 24 unseen tasks and substantially outperforms strong vision-language rewarders, including GPT-5 and Gemini-3-Pro, while exhibiting markedly greater robustness to reward hacking.

中文翻译：视觉语言模型（VLM）在多样化任务中展现了令人印象深刻的能力，推动了利用这些模型监督机器人学习的努力。然而，在强化学习（RL）中用作评估器时，现今最强的模型常在部分可观测性和分布偏移下失效，使策略得以利用感知错误而非真正解决任务。为克服这一局限，我们引入SOLE-R1（Self-Observing LEarner），一个专为在线RL提供唯一奖励信号的视频语言推理模型。仅以原始视频观测和自然语言目标为输入，SOLE-R1执行逐时间步的时空思维链（CoT）推理，生成可用于直接作为奖励的任务进度密集估计。为训练SOLE-R1，我们开发了大规模视频轨迹与推理合成管线，生成与连续进度监督对齐的时间基准CoT轨迹。在四个不同仿真环境和一个真实机器人场景中，SOLE-R1实现了从随机初始化的零样本在线RL：机器人无需真实奖励、成功指示器、演示或任务特定调优即可学习此前未见的操作任务。SOLE-R1在24个未见任务上成功，大幅超越强视觉语言奖励模型（包括GPT-5和Gemini-3-Pro），同时对奖励黑客具有显著更强的鲁棒性。

------

Title: BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism

URL: https://doi.org/10.48550/arXiv.2505.20660

Abstract: Graphical User Interface (GUI) agents have gained substantial attention due to their impressive capabilities to complete tasks through multiple interactions within GUI environments. However, existing agents primarily focus on enhancing the accuracy of individual actions and often lack effective mechanisms for detecting and recovering from errors. To address these shortcomings, we propose the BacktrackAgent, a robust framework that incorporates a backtracking mechanism to improve task completion efficiency. BacktrackAgent includes verifier, judger, and reflector components as modules for error detection and recovery, while also applying judgment rewards to further enhance the agent's performance. Additionally, we develop a training dataset specifically designed for the backtracking mechanism, which considers the outcome pages after action executions. Experimental results show that BacktrackAgent has achieved performance improvements in both task success rate and step accuracy on Mobile3M and Auto-UI benchmarks. Our data and code will be released upon acceptance.

中文翻译：GUI Agent因在GUI环境中通过多次交互完成任务的能力而受到广泛关注。然而，现有Agent主要聚焦于提升单个动作的准确率，通常缺乏有效的错误检测和恢复机制。为解决这些不足，我们提出BacktrackAgent，一个包含回溯机制的鲁棒框架，提升任务完成效率。BacktrackAgent包含验证器、评判器和反思器组件作为错误检测和恢复模块，同时应用判断奖励进一步增强Agent性能。此外，我们开发了专为回溯机制设计的训练数据集，考虑动作执行后的结果页面。实验结果表明，BacktrackAgent在Mobile3M和Auto-UI基准上的任务成功率和步骤准确率均取得了性能提升。

------

Title: Multi-step Problem Solving Through a Verifier: An Empirical Analysis on Model-induced Process Supervision

URL: https://doi.org/10.48550/arXiv.2402.02658

Abstract: Process supervision, using a trained verifier to evaluate the intermediate steps generated by a reasoner, has demonstrated significant improvements in multi-step problem solving. In this paper, to avoid the expensive effort of human annotation on the verifier training data, we introduce Model-induced Process Supervision (MiPS), a novel method for automating data curation. MiPS annotates an intermediate step by sampling completions of this solution through the reasoning model, and obtaining an accuracy defined as the proportion of correct completions. Inaccuracies of the reasoner would cause MiPS underestimating the accuracy of intermediate steps, therefore, we suggest and empirically show that verification focusing on high predicted scores of the verifier shall be preferred over that of low predicted scores, contrary to prior observations on human curated data. Our approach significantly improves the performance of PaLM 2 on math and coding tasks (accuracy +0.67% on GSM8K, +4.16% on MATH, +0.92% on MBPP compared with an output supervision trained verifier). Additionally, our study demonstrates that the verifier exhibits strong generalization ability across different reasoning models.

中文翻译：过程监督，使用训练好的验证器评估推理器生成的中间步骤，已在多步问题求解中展示出显著改进。本文为规避验证器训练数据人工标注的高昂成本，引入模型诱导过程监督（MiPS），一种自动化数据整理的新方法。MiPS通过推理模型采样某个解的补全，并将正确补全的比例定义为准确率来标注中间步骤。推理器的误差会导致MiPS低估中间步骤的准确率，因此我们建议并经验性证明，应优先关注验证器高预测分数而非低预测分数的验证，这与在人工整理数据上的先前观察相反。我们的方法显著提升了PaLM 2在数学和编码任务上的性能（相比结果监督训练的验证器，GSM8K准确率+0.67%，MATH +4.16%，MBPP +0.92%）。此外，我们的研究表明验证器在不同推理模型间展现出强泛化能力。

------

Title: RL-VLM-F: Reinforcement Learning from Vision Language Foundation Model Feedback

URL: https://doi.org/10.48550/arXiv.2402.03681

Abstract: Reward engineering has long been a challenge in Reinforcement Learning (RL) research, as it often requires extensive human effort and iterative processes of trial-and-error to design effective reward functions. In this paper, we propose RL-VLM-F, a method that automatically generates reward functions for agents to learn new tasks, using only a text description of the task goal and the agent's visual observations, by leveraging feedbacks from vision language foundation models (VLMs). The key to our approach is to query these models to give preferences over pairs of the agent's image observations based on the text description of the task goal, and then learn a reward function from the preference labels, rather than directly prompting these models to output a raw reward score, which can be noisy and inconsistent. We demonstrate that RL-VLM-F successfully produces effective rewards and policies across various domains - including classic control, as well as manipulation of rigid, articulated, and deformable objects - without the need for human supervision, outperforming prior methods that use large pretrained models for reward generation under the same assumptions. Videos can be found on our project website: https://rlvlmf2024.github.io/

中文翻译：奖励工程长期以来是强化学习（RL）研究的挑战，通常需要大量人力和反复试错来设计有效的奖励函数。本文我们提出RL-VLM-F，一种自动为Agent学习新任务生成奖励函数的方法，仅使用任务目标的文本描述和Agent的视觉观测，通过利用视觉语言基础模型（VLM）的反馈。我们方法的关键是向这些模型查询，基于任务目标的文本描述对Agent图像观测对给出偏好，然后从偏好标签学习奖励函数，而非直接提示这些模型输出原始奖励分数（后者可能噪声大且不一致）。我们证明RL-VLM-F在多个领域——包括经典控制以及刚体、关节体和可变形物体的操作——成功生成有效的奖励和策略，无需人类监督，在相同假设下超越了使用大型预训练模型进行奖励生成的先前方法。

------

Title: A Rubric-Supervised Critic from Sparse Real-World Outcomes

URL: https://www.semanticscholar.org/paper/3e154076350aa7d6e868dc5afebcb231f007c0af

Abstract: Academic benchmarks for coding agents tend to reward autonomous task completion, measured by verifiable rewards such as unit-test success. In contrast, real-world coding agents operate with humans in the loop, where success signals are typically noisy, delayed, and sparse. How can we bridge this gap? In this paper, we propose a process to learn a"critic"model from sparse and noisy interaction data, which can then be used both as a reward model for either RL-based training or inference-time scaling. Specifically, we introduce Critic Rubrics, a rubric-based supervision framework with 24 behavioral features that can be derived from human-agent interaction traces alone. Using a semi-supervised objective, we can then jointly predict these rubrics and sparse human feedback (when present). In experiments, we demonstrate that, despite being trained primarily from trace-observable rubrics and sparse real-world outcome proxies, these critics improve best-of-N reranking on SWE-bench (Best@8 +15.9 over Random@8 over the rerankable subset of trajectories), enable early stopping (+17.7 with 83% fewer attempts), and support training-time data curation via critic-selected trajectories.

中文翻译：编码Agent的学术基准倾向于奖励自主任务完成，以可验证奖励如单元测试通过衡量。相比之下，现实世界的编码Agent与人类协同运作，其中成功信号通常是嘈杂、延迟且稀疏的。我们如何弥合这一差距？本文中我们提出一种从稀疏且嘈杂的交互数据中学习critic模型的方法，该模型随后可用作RL训练或推理时扩展的奖励模型。具体而言，我们引入Critic Rubrics，一个基于量规的监督框架，具有24个可从人-Agent交互轨迹中导出的行为特征。使用半监督目标，我们可以联合预测这些量规和稀疏的人类反馈。尽管主要从轨迹可观察量规和稀疏真实世界结果代理训练，这些critic在SWE-bench上改善了Best-of-N重排序（Best@8 +15.9），实现了早期停止（+17.7，尝试次数减少83%），并通过critic选择的轨迹支持训练时数据管理。

------

Title: RoboReward: General-Purpose Vision-Language Reward Models for Robotics

URL: https://doi.org/10.48550/arXiv.2601.00675

Abstract: A well-designed reward is critical for effective reinforcement learning-based policy improvement. In real-world robotics, obtaining such rewards typically requires either labor-intensive human labeling or brittle, handcrafted objectives. Vision-language models (VLMs) have shown promise as automatic reward models, yet their effectiveness on real robot tasks is poorly understood. In this work, we aim to close this gap by introducing (1) RoboReward, a robotics reward dataset and benchmark built on large-scale real-robot corpora from Open X-Embodiment (OXE) and RoboArena, and (2) vision-language reward models trained on this dataset (RoboReward 4B/8B). Because OXE is success-heavy and lacks failure examples, we propose a negative examples data augmentation pipeline that generates calibrated negative and near-misses via counterfactual relabeling of successful episodes and temporal clipping to create partial-progress outcomes from the same videos. Using this framework, we build a large training and evaluation dataset spanning diverse tasks and embodiments to test whether state-of-the-art VLMs can reliably provide rewards for robot learning. Our evaluation of open and proprietary VLMs finds that no model excels across tasks, highlighting substantial room for improvement. We then train general-purpose 4B- and 8B-parameter models that outperform much larger VLMs in assigning rewards for short-horizon robotic tasks. Finally, we deploy the 8B model in real-robot reinforcement learning and find that it improves policy learning over Gemini Robotics-ER 1.5 while narrowing the gap to RL training with human-provided rewards. We release the full dataset, trained reward models, and evaluation suite on our website to advance the development of general-purpose reward models in robotics: https://crfm.stanford.edu/helm/robo-reward-bench (project website).

中文翻译：精心设计的奖励对有效的基于强化学习的策略改进至关重要。在真实世界机器人学中，获取此类奖励通常需要劳动密集的人工标注或脆弱的硬编码目标。视觉语言模型（VLM）作为自动奖励模型展现出前景，但它们在真实机器人任务上的有效性却知之甚少。本文中我们旨在弥合这一差距，通过引入：(1) RoboReward，一个基于大规模真实机器人语料（Open X-Embodiment和RoboArena）构建的机器人奖励数据集和基准；(2) 在此数据集上训练的视觉语言奖励模型（RoboReward 4B/8B）。由于OXE以成功样本为主，缺乏失败示例，我们提出负样本数据增强管线，通过成功片段的counterfactual relabeling和时间裁剪来生成校准的负样本和接近失败的样本。使用该框架，我们构建了跨多样化任务和具身的大规模训练和评估数据集。我们对开源和商业VLM的评估发现，没有模型在所有任务上都表现卓越，凸显了显著的改进空间。我们随后训练了通用的4B和8B参数模型，在短时域机器人任务中分配奖励方面超越了规模大得多的VLM。最后，我们将8B模型部署到真实机器人强化学习中，发现它比Gemini Robotics-ER 1.5改善了策略学习，同时缩小了与人工提供奖励的RL训练的差距。

------

Title: CUARewardBench: A Benchmark for Evaluating Reward Models on Computer-using Agent

URL: https://doi.org/10.48550/arXiv.2510.18596

Abstract: Computer-using agents (CUAs) enable task completion through natural interaction with operating systems and software interfaces. While script-based verifiers are widely adopted for evaluation, they suffer from limited scalability and inability to provide step-wise assessment. Reward models offer promising alternatives, but their effectiveness on CUA evaluation remains largely underexplored. To address this gap, we present CUARewardBench, comprising four key contributions: (1) First-ever Comprehensive CUA Reward Benchmark: We introduce the first benchmark for evaluating both outcome reward models (ORM) and process reward models (PRM) on CUA tasks, enabling systematic assessment across trajectory-level and step-level evaluation. (2) Diverse, Practical and Reliable Dataset: CUARewardBench encompasses trajectories from 10 software categories and 7 agent architectures with varying performance levels (25.9%-50.8% success rates). All trajectories are expertly annotated through carefully designed protocols, with rigorous quality control to ensure reliability and practical applicability. (3) Comprehensive Analysis and Insights: Through extensive experiments across 7 vision-language models and 3 prompt templates, we reveal critical limitations of current CUA RMs, including insufficient visual reasoning capabilities, knowledge deficiencies, and the superiority of general VLMs over specialized CUA models for reward evaluation. (4) Unanimous Prompt Ensemble (UPE): Based on the insights from our comprehensive analysis, we propose UPE, a novel ensemble method that significantly enhances reward model reliability through strict unanimous voting and strategic prompt-template configurations. UPE achieves 89.8% precision and 93.3% NPV for ORM, and 81.7% precision and 85.1% NPV for PRM, substantially outperforming single VLMs and traditional ensemble approaches.

中文翻译：计算机使用Agent（CUA）通过与操作系统和软件界面的自然交互完成任务。虽然基于脚本的验证器被广泛用于评估，但它们面临可扩展性有限和无法提供步骤级评估的问题。奖励模型提供了有前景的替代方案，但它们在CUA评估上的有效性在很大程度上尚未被探索。为填补这一空白，我们提出CUARewardBench，包含四个关键贡献：(1)首个全面的CUA奖励基准，用于评估CUA任务中结果奖励模型（ORM）和过程奖励模型（PRM），实现对轨迹级和步骤级评估的系统评价。(2)多样化、实用且可靠的数据集，涵盖来自10个软件类别和7种Agent架构的轨迹，具有不同性能水平（25.9%-50.8%成功率），所有轨迹经过精心设计的协议由专家标注并经过严格质量控制。(3)全面分析和洞察，通过对7个视觉语言模型和3种提示模板的广泛实验，揭示了当前CUA奖励模型的关键局限，包括视觉推理能力不足和通用VLM在奖励评估上优于专用CUA模型。(4)一致提示集成（UPE），一种通过严格一致投票和策略性提示模板配置显著增强奖励模型可靠性的新颖集成方法。UPE为ORM达到89.8%精确率和93.3%阴性预测值，为PRM达到81.7%精确率和85.1%阴性预测值，大幅超越单一VLM和传统集成方法。

------

Title: GUIDE: Interpretable GUI Agent Evaluation via Hierarchical Diagnosis

URL: https://www.semanticscholar.org/paper/ca060bc50ce301a3ce6c9c595821d5a1f2485b3f

Abstract: Evaluating GUI agents presents a distinct challenge: trajectories are long, visually grounded, and open-ended, yet evaluation must be both accurate and interpretable. Existing approaches typically apply a single holistic judgment over the entire action-observation sequence-a strategy that proves unreliable on long-horizon tasks and yields binary verdicts offering no insight into where or why an agent fails. This opacity limits the utility of evaluation as a diagnostic tool for agent development. We introduce GUIDE (GUI Understanding and Interpretable Diagnostic Evaluation), a framework that decomposes trajectory assessment into three sequential stages mirroring the compositional structure of GUI tasks. Trajectory Segmentation partitions the full trace into semantically coherent subtask units. Subtask Diagnosis evaluates each unit in context, assigning a completion verdict and generating a structured error analysis with corrective recommendations. Overall Summary aggregates per-subtask diagnoses into a task-level judgment. By operating on bounded subtask segments rather than full trajectories, GUIDE mitigates the context overload that degrades existing evaluators as task complexity grows. We validate GUIDE on three benchmarks: an industrial e-commerce dataset of 932 trajectories, AGENTREWARDBENCH spanning five web agent tasks with 1302 trajectories, and AndroidBench for mobile device control. Across all settings, GUIDE substantially outperforms existing evaluators-achieving up to 5.35 percentage points higher accuracy than the strongest baseline-while producing structured diagnostic reports that directly inform agent improvement.

中文翻译：评估GUI Agent面临独特挑战：轨迹长、视觉锚定且开放式，但评估必须既准确又可解释。现有方法通常对整个动作-观测序列施加单一整体判断——这种策略在长时域任务上被证明不可靠，且产生二值裁决无法揭示Agent在何处或为何失败的洞见。我们引入GUIDE（GUI Understanding and Interpretable Diagnostic Evaluation），一个将轨迹评估分解为三个序贯阶段的框架：轨迹分割将完整轨迹划分为语义连贯的子任务单元；子任务诊断在上下文中评估每个单元，分配完成裁决并生成结构性错误分析与纠正建议；整体摘要将逐子任务诊断聚合为任务级判断。通过在受限子任务片段而非完整轨迹上操作，GUIDE缓解了随任务复杂度增长而降低现有评估器性能的上下文过载问题。我们在三个基准上验证GUIDE，包含932条轨迹的工业电商数据集、跨五个Web Agent任务含1302条轨迹的AGENTREWARDBENCH，以及移动设备控制的AndroidBench。在所有场景中，GUIDE大幅超越现有评估器，准确率最高提升5.35个百分点，同时产出可直接指导Agent改进的结构化诊断报告。

------

Title: Let's reward step by step: Step-Level reward model as the Navigators for Reasoning

URL: https://doi.org/10.48550/arXiv.2310.10080

Abstract: Recent years have seen considerable advancements in multi-step reasoning with Large Language Models (LLMs). The previous studies have elucidated the merits of integrating feedback or search mechanisms during model inference to improve the reasoning accuracy. The Process-Supervised Reward Model (PRM), typically furnishes LLMs with step-by-step feedback during the training phase, akin to Proximal Policy Optimization (PPO) or reject sampling. Our objective is to examine the efficacy of PRM in the inference phase to help discern the optimal solution paths for multi-step tasks such as mathematical reasoning and code generation. To this end, we propose a heuristic greedy search algorithm that employs the step-level feedback from PRM to optimize the reasoning pathways explored by LLMs. This tailored PRM demonstrated enhanced results compared to the Chain of Thought (CoT) on mathematical benchmarks like GSM8K and MATH. Additionally, to explore the versatility of our approach, we develop a novel method to automatically generate step-level reward dataset for coding tasks and observed similar improved performance in the code generation tasks. Thus highlighting the robust nature of our reward-model-based approach to inference for reasoning tasks.

中文翻译：近年来，大语言模型（LLM）在多步推理方面取得了长足进步。先前研究阐明了在模型推理过程中整合反馈或搜索机制以提高推理准确性的优势。过程监督奖励模型（PRM）通常在训练阶段为LLM提供逐步反馈，类似于PPO或拒绝采样。我们的目标是在推理阶段检验PRM的有效性，帮助识别多步任务（如数学推理和代码生成）的最优解路径。为此，我们提出一种启发式贪心搜索算法，利用PRM的步骤级反馈来优化LLM探索的推理路径。这种定制的PRM在GSM8K和MATH等数学基准上展现了优于思维链（CoT）的结果。此外，为探索方法的通用性，我们开发了一种新方法来自动生成编码任务的步骤级奖励数据集，并在代码生成任务中观察到类似的性能提升，从而凸显了基于奖励模型的推理方法的鲁棒性。

------

Title: Process Reward Model with Q-Value Rankings

URL: https://doi.org/10.48550/arXiv.2410.11287

Abstract: Process Reward Modeling (PRM) is critical for complex reasoning and decision-making tasks where the accuracy of intermediate steps significantly influences the overall outcome. Existing PRM approaches, primarily framed as classification problems, employ cross-entropy loss to independently evaluate each step's correctness. This method can lead to suboptimal reward distribution and does not adequately address the interdependencies among steps. To address these limitations, we introduce the Process Q-value Model (PQM), a novel framework that redefines PRM in the context of a Markov Decision Process. PQM optimizes Q-value rankings based on a novel comparative loss function, enhancing the model's ability to capture the intricate dynamics among sequential decisions. This approach provides a more granular and theoretically grounded methodology for process rewards. Our extensive empirical evaluations across various sampling policies, language model backbones, and multi-step reasoning benchmarks show that PQM outperforms classification-based PRMs. The effectiveness of the comparative loss function is highlighted in our comprehensive ablation studies, confirming PQM's practical efficacy and theoretical advantage.

中文翻译：过程奖励建模（PRM）对于复杂的推理和决策任务至关重要，其中中间步骤的准确性显著影响整体结果。现有PRM方法主要被框定为分类问题，使用交叉熵损失独立评估每一步的正确性。这种方法可能导致次优的奖励分配，且未充分处理步骤间的相互依赖关系。为克服这些局限，我们引入过程Q值模型（PQM），一种在马尔可夫决策过程框架下重新定义PRM的新框架。PQM基于新颖的比较损失函数优化Q值排序，增强模型捕捉序贯决策间复杂动态的能力。该方法为过程奖励提供了更细粒度和更有理论依据的方法论。我们在不同采样策略、语言模型骨干和多步推理基准上的广泛实证评估表明，PQM优于基于分类的PRM。全面消融研究凸显了比较损失函数的有效性，确认了PQM的实践效能和理论优势。

------

Title: Large Reward Models: Generalizable Online Robot Reward Generation with Vision-Language Models

URL: https://www.semanticscholar.org/paper/b0bede4b92fe9fc0ff118673c6df52478d185294

Abstract: Reinforcement Learning (RL) has shown great potential in refining robotic manipulation policies, yet its efficacy remains strongly bottlenecked by the difficulty of designing generalizable reward functions. In this paper, we propose a framework for online policy refinement by adapting foundation VLMs into online reward generators. We develop a robust, scalable reward model based on a state-of-the-art VLM, trained on a large-scale, multi-source dataset encompassing real-world robot trajectories, human-object interactions, and diverse simulated environments. Unlike prior approaches that evaluate entire trajectories post-hoc, our method leverages the VLM to formulate a multifaceted reward signal comprising process, completion, and temporal contrastive rewards based on current visual observations. Initializing with a base policy trained via Imitation Learning (IL), we employ these VLM rewards to guide the model to correct sub-optimal behaviors in a closed-loop manner. We evaluate our framework on challenging long-horizon manipulation benchmarks requiring sequential execution and precise control. Crucially, our reward model operates in a purely zero-shot manner within these test environments. Experimental results demonstrate that our method significantly improves the success rate of the initial IL policy within just 30 RL iterations, demonstrating remarkable sample efficiency. This empirical evidence highlights that VLM-generated signals can provide reliable feedback to resolve execution errors, effectively eliminating the need for manual reward engineering and facilitating efficient online refinement for robot learning.

中文翻译：强化学习（RL）在精炼机器人操作策略方面展现了巨大潜力，但其有效性仍被设计可泛化奖励函数的困难严重制约。本文中我们提出一个在线策略精炼框架，通过将基础VLM适配为在线奖励生成器。我们基于最先进的VLM开发了一个鲁棒、可扩展的奖励模型，在包含真实世界机器人轨迹、人物交互和多样化仿真环境的大规模多源数据集上训练。不同于先前事后评估整个轨迹的方法，我们的方法利用VLM基于当前视觉观测制定多方面奖励信号，包括过程奖励、完成奖励和时间对比奖励。以通过模仿学习训练的基础策略为起点，我们使用这些VLM奖励以闭环方式引导模型纠正次优行为。我们在需要序贯执行和精确控制的挑战性长时域操作基准上评估了框架。关键的是，我们的奖励模型在这些测试环境中以纯零样本方式运行。实验结果表明，我们的方法仅在30轮RL迭代内就显著提升了初始IL策略的成功率，展现了卓越的样本效率。这一实证证据凸显了VLM生成的信号可以提供可靠反馈来解决执行错误，有效消除了对手动奖励工程的需求。

------

Title: AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation

URL: https://doi.org/10.48550/arXiv.2410.00371

Abstract: Robotic manipulation in open-world settings requires not only task execution but also the ability to detect and learn from failures. While recent advances in vision-language models (VLMs) and large language models (LLMs) have improved robots' spatial reasoning and problem-solving abilities, they still struggle with failure recognition, limiting their real-world applicability. We introduce AHA, an open-source VLM designed to detect and reason about failures in robotic manipulation using natural language. By framing failure detection as a free-form reasoning task, AHA identifies failures and provides detailed, adaptable explanations across different robots, tasks, and environments. We fine-tuned AHA using FailGen, a scalable framework that generates the first large-scale dataset of robotic failure trajectories, the AHA dataset. FailGen achieves this by procedurally perturbing successful demonstrations from simulation. Despite being trained solely on the AHA dataset, AHA generalizes effectively to real-world failure datasets, robotic systems, and unseen tasks. It surpasses the second-best model (GPT-4o in-context learning) by 10.3% and exceeds the average performance of six compared models including five state-of-the-art VLMs by 35.3% across multiple metrics and datasets. We integrate AHA into three manipulation frameworks that utilize LLMs/VLMs for reinforcement learning, task and motion planning, and zero-shot trajectory generation. AHA's failure feedback enhances these policies' performances by refining dense reward functions, optimizing task planning, and improving sub-task verification, boosting task success rates by an average of 21.4% across all three tasks compared to GPT-4 models.

中文翻译：开放世界中的机器人操作不仅需要任务执行，还需要检测并学习失败的能力。尽管视觉语言模型（VLM）和大语言模型（LLM）的最新进展改善了机器人的空间推理和问题解决能力，但它们在失败识别方面仍存在困难，限制了其在真实世界的适用性。我们引入AHA，一个开源VLM，旨在用自然语言检测和推理机器人操作中的失败。通过将失败检测构建为自由形式推理任务，AHA识别失败并跨不同机器人、任务和环境提供详细、可适应的解释。我们使用FailGen微调AHA，FailGen是一个可扩展框架，生成了首个大规模机器人失败轨迹数据集——AHA数据集。FailGen通过对仿真中的成功演示进行程序性扰动来实现这一点。尽管仅在AHA数据集上训练，AHA有效泛化到真实世界失败数据集、机器人系统和未见任务。它比第二名模型（GPT-4o上下文学习）高出10.3%，超过包括五个最先进VLM在内的六个比较模型的平均性能35.3%。我们将AHA集成到三个利用LLM/VLM进行强化学习、任务与运动规划以及零样本轨迹生成的操控框架中。AHA的失败反馈通过精炼密集奖励函数、优化任务规划和改进子任务验证来增强这些策略，在所有三个任务中任务成功率平均提升21.4%。

------

Title: "Are We Done Yet?": A Vision-Based Judge for Autonomous Task Completion of Computer Use Agents

URL: https://doi.org/10.48550/arXiv.2511.20067

Abstract: Computer Use Agents (CUAs) are designed to autonomously operate digital interfaces, yet they often fail to reliably determine whether a given task has been completed. We present an autonomous evaluation and feedback framework that uses vision-language models to assess task completion directly from screenshots and task descriptions. Our dataset covers 42 built-in macOS applications and 1,260 human-labeled tasks across a wide range of scenarios. Our framework achieves up to 73 percent accuracy in task success detection and yields an average relative improvement of 27 percent in overall task success when evaluator feedback is applied. These results show that vision-based evaluation can serve as an effective feedback mechanism that improves the reliability and self-correction of autonomous computer-use agents.

中文翻译：计算机使用Agent（CUA）旨在自主操作数字界面，但它们往往无法可靠判断给定任务是否已完成。我们提出一个自主评估和反馈框架，使用视觉语言模型直接从截图和任务描述评估任务完成情况。我们的数据集覆盖42个内置macOS应用和1260个人工标注任务，涵盖广泛的场景。我们的框架在任务成功检测中达到最高73%的准确率，应用评估器反馈后总体任务成功率平均相对提升27%。这些结果表明基于视觉的评估可作为有效反馈机制，提升自主计算机使用Agent的可靠性和自我纠错能力。

------

Title: Critique-out-Loud Reward Models

URL: https://www.semanticscholar.org/paper/2f112209675710d3ec2d6f1d06bbdc74e9bc60af

Abstract: Traditionally, reward models used for reinforcement learning from human feedback (RLHF) are trained to directly predict preference scores without leveraging the generation capabilities of the underlying large language model (LLM). This limits the capabilities of reward models as they must reason implicitly about the quality of a response, i.e., preference modeling must be performed in a single forward pass through the model. To enable reward models to reason explicitly about the quality of a response, we introduce Critique-out-Loud (CLoud) reward models. CLoud reward models operate by first generating a natural language critique of the assistant's response that is then used to predict a scalar reward for the quality of the response. We demonstrate the success of CLoud reward models for both Llama-3-8B and 70B base models: compared to classic reward models CLoud reward models improve pairwise preference classification accuracy on RewardBench by 4.65 and 5.84 percentage points for the 8B and 70B base models respectively. Furthermore, CLoud reward models lead to a Pareto improvement for win rate on ArenaHard when used as the scoring model for Best-of-N. Finally, we explore how to exploit the dynamic inference compute capabilities of CLoud reward models by performing self-consistency decoding for reward prediction.

中文翻译：传统上，用于从人类反馈强化学习（RLHF）的奖励模型被训练为直接预测偏好分数，而不利用底层大语言模型（LLM）的生成能力。这限制了奖励模型的能力，因为它们必须隐式推理响应的质量，即偏好建模必须在模型的单次前向传播中完成。为使奖励模型能够显式推理响应质量，我们引入Critique-out-Loud（CLoud）奖励模型。CLoud奖励模型首先对助手响应生成自然语言批判，然后基于批判预测响应质量的标量奖励。我们展示了CLoud奖励模型在Llama-3-8B和70B基座模型上的成功：相比经典奖励模型，CLoud奖励模型在RewardBench上的成对偏好分类准确率分别提升4.65和5.84个百分点。此外，CLoud奖励模型在用于Best-of-N评分时在ArenaHard上实现了Pareto改进。最后，我们探索了通过自一致性解码进行奖励预测来利用CLoud奖励模型动态推理计算能力的方法。

------

Title: SAFE: Multitask Failure Detection for Vision-Language-Action Models

URL: https://doi.org/10.48550/arXiv.2506.09937

Abstract: While vision-language-action models (VLAs) have shown promising robotic behaviors across a diverse set of manipulation tasks, they achieve limited success rates when deployed on novel tasks out of the box. To allow these policies to safely interact with their environments, we need a failure detector that gives a timely alert such that the robot can stop, backtrack, or ask for help. However, existing failure detectors are trained and tested only on one or a few specific tasks, while generalist VLAs require the detector to generalize and detect failures also in unseen tasks and novel environments. In this paper, we introduce the multitask failure detection problem and propose SAFE, a failure detector for generalist robot policies such as VLAs. We analyze the VLA feature space and find that VLAs have sufficient high-level knowledge about task success and failure, which is generic across different tasks. Based on this insight, we design SAFE to learn from VLA internal features and predict a single scalar indicating the likelihood of task failure. SAFE is trained on both successful and failed rollouts and is evaluated on unseen tasks. SAFE is compatible with different policy architectures. We test it on OpenVLA, $\pi_0$, and $\pi_0$-FAST in both simulated and real-world environments extensively. We compare SAFE with diverse baselines and show that SAFE achieves state-of-the-art failure detection performance and the best trade-off between accuracy and detection time using conformal prediction. More qualitative results and code can be found at the project webpage: https://vla-safe.github.io/

中文翻译：尽管视觉语言动作模型（VLA）在多样化操作任务上展现了有前景的机器人行为，它们在开箱即用于新任务时取得的成功率有限。为使这些策略能安全地与环境交互，我们需要能及时发出警报的失败检测器，使机器人可以停止、回退或寻求帮助。然而，现有失败检测器仅在一个或几个特定任务上训练和测试，而通用VLA需要检测器泛化并在未见任务和新环境中检测失败。本文中我们引入多任务失败检测问题，并提出SAFE，一种面向通用机器人策略（如VLA）的失败检测器。我们分析了VLA特征空间，发现VLA具有关于任务成功和失败的充分高层知识，这些知识跨不同任务是通用的。基于这一洞察，我们设计SAFE从VLA内部特征学习，预测表示任务失败可能性的单一标量。SAFE在成功和失败的rollout上训练，在未见任务上评估。我们在仿真和真实环境中对OpenVLA、pi_0和pi_0-FAST进行了广泛测试。结果表明SAFE在使用共形预测实现失败检测性能最优以及准确率和检测时间之间的最佳权衡。

------

Title: OS-Sentinel: Towards Safety-Enhanced Mobile GUI Agents via Hybrid Validation in Realistic Workflows

URL: https://doi.org/10.48550/arXiv.2510.24411

Abstract: Computer-using agents powered by Vision-Language Models (VLMs) have demonstrated human-like capabilities in operating digital environments like mobile platforms. While these agents hold great promise for advancing digital automation, their potential for unsafe operations, such as system compromise and privacy leakage, is raising significant concerns. Detecting these safety concerns across the vast and complex operational space of mobile environments presents a formidable challenge that remains critically underexplored. To establish a foundation for mobile agent safety research, we introduce MobileRisk-Live, a dynamic sandbox environment accompanied by a safety detection benchmark comprising realistic trajectories with fine-grained annotations. Built upon this, we propose OS-Sentinel, a novel hybrid safety detection framework that synergistically combines a Formal Verifier for detecting explicit system-level violations with a VLM-based Contextual Judge for assessing contextual risks and agent actions. Experiments show that OS-Sentinel achieves 10%-30% improvements over existing approaches across multiple metrics. Further analysis provides critical insights that foster the development of safer and more reliable autonomous mobile agents. Our code and data are available at https://github.com/OS-Copilot/OS-Sentinel.

中文翻译：由视觉语言模型（VLM）驱动的计算机使用Agent展示了在移动端等数字环境中操作的人类水平能力。尽管这些Agent在推进数字自动化方面前景广阔，但其潜在的不安全操作（如系统破坏和隐私泄露）正引发重大担忧。在移动环境广阔而复杂的操作空间中检测这些安全问题构成巨大挑战，且尚未被充分探索。为给移动Agent安全研究奠定基础，我们引入MobileRisk-Live，一个动态沙盒环境，伴随包含真实轨迹和细粒度标注的安全检测基准。在此基础上，我们提出OS-Sentinel，一个新颖的混合安全检测框架，将用于检测显式系统级违规的形式验证器与用于评估上下文风险和Agent动作的基于VLM的上下文评判器协同结合。实验表明OS-Sentinel在多个指标上超越现有方法10%-30%。进一步分析提供了促进更安全可靠自主移动Agent发展的关键洞察。

------

Title: Entropy-Regularized Process Reward Model

URL: https://doi.org/10.48550/arXiv.2412.11006

Abstract: Large language models (LLMs) have shown promise in performing complex multi-step reasoning, yet they continue to struggle with mathematical reasoning, often making systematic errors. A promising solution is reinforcement learning (RL) guided by reward models, particularly those focusing on process rewards, which score each intermediate step rather than solely evaluating the final outcome. This approach is more effective at guiding policy models towards correct reasoning trajectories. In this work, we propose an entropy-regularized process reward model (ER-PRM) that integrates KL-regularized Markov Decision Processes (MDP) to balance policy optimization with the need to prevent the policy from shifting too far from its initial distribution. We derive a novel reward construction method based on the theoretical results. Our theoretical analysis shows that we could derive the optimal reward model from the initial policy sampling. Our empirical experiments on the MATH and GSM8K benchmarks demonstrate that ER-PRM consistently outperforms existing process reward models, achieving 1% improvement on GSM8K and 2-3% improvement on MATH under best-of-N evaluation, and more than 1% improvement under RLHF. These results highlight the efficacy of entropy-regularization in enhancing LLMs'reasoning capabilities.

中文翻译：大语言模型（LLM）在执行复杂多步推理方面展现了潜力，但在数学推理上仍持续挣扎，经常犯系统性错误。一个有前景的解决方案是由奖励模型引导的强化学习（RL），特别是关注过程奖励的模型，它对每个中间步骤评分，而非仅评估最终结果。本文中，我们提出熵正则化过程奖励模型（ER-PRM），集成了KL正则化马尔可夫决策过程（MDP），平衡策略优化与防止策略偏离初始分布过远的需求。基于理论结果，我们推导出一种新的奖励构建方法。我们的理论分析表明我们可以从初始策略采样推导出最优奖励模型。在MATH和GSM8K基准上的实验表明，ER-PRM在best-of-N评估下始终优于现有过程奖励模型，在GSM8K上取得1%的提升，MATH上2-3%的提升，在RLHF下超过1%的提升。这些结果凸显了熵正则化在增强LLM推理能力方面的有效性。

------

Title: Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning

URL: https://doi.org/10.48550/arXiv.2505.14069

Abstract: Retrieval-augmented generation (RAG) enhances the text generation capabilities of large language models (LLMs) by integrating external knowledge and up-to-date information. However, traditional RAG systems are limited by static workflows and lack the adaptability required for multistep reasoning and complex task management. To address these limitations, agentic RAG systems (e.g., DeepResearch) have been proposed, enabling dynamic retrieval strategies, iterative context refinement, and adaptive workflows for handling complex search queries beyond the capabilities of conventional RAG. Recent advances, such as Search-R1, have demonstrated promising gains using outcome-based reinforcement learning, where the correctness of the final answer serves as the reward signal. Nevertheless, such outcome-supervised agentic RAG methods face challenges including low exploration efficiency, gradient conflict, and sparse reward signals. To overcome these challenges, we propose to utilize fine-grained, process-level rewards to improve training stability, reduce computational costs, and enhance efficiency. Specifically, we introduce a novel method ReasonRAG that automatically constructs RAG-ProGuide, a high-quality dataset providing process-level rewards for (i) query generation, (ii) evidence extraction, and (iii) answer generation, thereby enhancing model inherent capabilities via process-supervised reinforcement learning. With the process-level policy optimization, the proposed framework empowers LLMs to autonomously invoke search, generate queries, extract relevant evidence, and produce final answers. Compared to existing approaches such as Search-R1 and traditional RAG systems, ReasonRAG, leveraging RAG-ProGuide, achieves superior performance on five benchmark datasets using only 5k training instances, significantly fewer than the 90k training instances required by Search-R1.

中文翻译：检索增强生成（RAG）通过集成外部知识和最新信息增强了大语言模型（LLM）的文本生成能力。然而，传统RAG系统受限于静态工作流，缺乏多步推理和复杂任务管理所需的适应性。为解决这些局限，Agent化RAG系统（如DeepResearch）被提出，实现了动态检索策略、迭代上下文精炼和自适应工作流来处理超越传统RAG能力的复杂搜索查询。Search-R1等近期进展展示了使用基于结果强化学习的有希望收益，其中最终答案的正确性作为奖励信号。然而，此类结果监督的Agent化RAG方法面临探索效率低、梯度冲突和奖励信号稀疏等挑战。为克服这些挑战，我们提出利用细粒度过程级奖励来提升训练稳定性和效率。具体而言，我们引入新方法ReasonRAG，自动构建RAG-ProGuide，一个高质量数据集，为查询生成、证据提取和答案生成提供过程级奖励，从而通过过程监督强化学习增强模型固有能力。与Search-R1和传统RAG系统相比，ReasonRAG利用RAG-ProGuide在仅5k训练实例上在五个基准数据集上取得更优性能，显著少于Search-R1所需的90k训练实例。

------

Title: Video-Language Critic: Transferable Reward Functions for Language-Conditioned Robotics

URL: https://doi.org/10.48550/arXiv.2405.19988

Abstract: Natural language is often the easiest and most convenient modality for humans to specify tasks for robots. However, learning to ground language to behavior typically requires impractical amounts of diverse, language-annotated demonstrations collected on each target robot. In this work, we aim to separate the problem of what to accomplish from how to accomplish it, as the former can benefit from substantial amounts of external observation-only data, and only the latter depends on a specific robot embodiment. To this end, we propose Video-Language Critic, a reward model that can be trained on readily available cross-embodiment data using contrastive learning and a temporal ranking objective, and use it to score behavior traces from a separate actor. When trained on Open X-Embodiment data, our reward model enables 2x more sample-efficient policy training on Meta-World tasks than a sparse reward only, despite a significant domain gap. Using in-domain data but in a challenging task generalization setting on Meta-World, we further demonstrate more sample-efficient training than is possible with prior language-conditioned reward models that are either trained with binary classification, use static images, or do not leverage the temporal information present in video data.

中文翻译：自然语言往往是人类为机器人指定任务的最简单、最便捷的方式。然而，学习将语言落实到行为通常需要在每台目标机器人上收集大量不切实际的、多样化的语言标注演示。本文中我们旨在将完成什么与如何完成的问题分离开来，因为前者可以从大量外部纯观测数据中受益，而仅后者依赖于特定的机器人具身。为此，我们提出Video-Language Critic，一个可以使用对比学习和时间排序目标在现成的跨具身数据上训练的奖励模型，用于为独立Actor的行为轨迹评分。在Open X-Embodiment数据上训练时，尽管存在显著的领域差距，我们的奖励模型使Meta-World任务上的策略训练样本效率比仅稀疏奖励提高了2倍。在Meta-World上使用域内数据但处于挑战性的任务泛化设置中，我们进一步展示了比先前语言条件奖励模型更具样本效率的训练。

------

Title: SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents

URL: https://www.semanticscholar.org/paper/38bde8d7e83c0c0b06e182926285ad6934cf988c

Abstract: Automating real-world software engineering tasks remains challenging for large language model (LLM)-based agents due to the need for long-horizon reasoning over large, evolving codebases and making consistent decisions across interdependent actions. Existing approaches typically rely on static prompting strategies or handcrafted heuristics to select actions such as code editing, file navigation, and test execution, but they lack fine-grained feedback on intermediate decisions. This leads to inefficient exploration, error propagation, and brittle solution trajectories. To address this limitation, we propose SWE-Shepherd, a framework that introduces Process Reward Models (PRMs) to provide dense, step-level supervision for repository-level code agents. Using trajectories from SWE-Bench, we construct an action-level reward dataset and train a lightweight reward model on a base LLM to estimate the usefulness of intermediate actions. During inference, the PRM evaluates candidate actions and guides the agent toward higher-reward decisions without requiring full reinforcement learning. Experiments on SWE-Bench Verified demonstrate improved interaction efficiency and action quality, while also highlighting challenges in aligning intermediate rewards with final task success.

中文翻译：基于大语言模型（LLM）的Agent在自动化真实世界软件工程任务方面仍面临挑战，因为需要对大型、不断演化的代码库进行长时域推理，并在相互依赖的动作间做出一致决策。现有方法通常依赖静态提示策略或手工启发式规则来选择代码编辑、文件导航和测试执行等动作，但缺乏对中间决策的细粒度反馈，导致探索效率低下和脆弱的解轨迹。为克服这一局限，我们提出SWE-Shepherd，一个引入过程奖励模型（PRM）为仓库级代码Agent提供密集步骤级监督的框架。使用SWE-Bench的轨迹，我们构建了动作级奖励数据集，并在基座LLM上训练轻量奖励模型来估计中间动作的有用性。推理时，PRM评估候选动作并引导Agent朝向更高奖励的决策。在SWE-Bench Verified上的实验表明交互效率和动作质量得到改善，同时也揭示了将中间奖励与最终任务成功对齐的挑战。

------

Title: Adapt2Reward: Adapting Video-Language Models to Generalizable Robotic Rewards via Failure Prompts

URL: https://doi.org/10.48550/arXiv.2407.14872

Abstract: For a general-purpose robot to operate in reality, executing a broad range of instructions across various environments is imperative. Central to the reinforcement learning and planning for such robotic agents is a generalizable reward function. Recent advances in vision-language models, such as CLIP, have shown remarkable performance in the domain of deep learning, paving the way for open-domain visual recognition. However, collecting data on robots executing various language instructions across multiple environments remains a challenge. This paper aims to transfer video-language models with robust generalization into a generalizable language-conditioned reward function, only utilizing robot video data from a minimal amount of tasks in a singular environment. Unlike common robotic datasets used for training reward functions, human video-language datasets rarely contain trivial failure videos. To enhance the model's ability to distinguish between successful and failed robot executions, we cluster failure video features to enable the model to identify patterns within. For each cluster, we integrate a newly trained failure prompt into the text encoder to represent the corresponding failure mode. Our language-conditioned reward function shows outstanding generalization to new environments and new instructions for robot planning and reinforcement learning.

中文翻译：通用机器人在现实中执行广泛指令跨各种环境运行至关重要。对这类机器人Agent的强化学习和规划而言，核心在于可泛化的奖励函数。视觉语言模型（如CLIP）的最新进展在深度学习领域展现了卓越性能，为开放领域视觉识别铺平了道路。然而，在多个环境中收集机器人执行各种语言指令的数据仍是挑战。本文旨在将具有鲁棒泛化能力的视频语言模型转化为可泛化的语言条件奖励函数，仅利用单一环境中少量任务的机器人视频数据。与用于训练奖励函数的常见机器人数据集不同，人类视频语言数据集很少包含平凡失败视频。为增强模型区分成功与失败机器人执行的能力，我们对失败视频特征进行聚类，使模型能识别其中的模式。对每个簇，我们将新训练的失败提示集成到文本编码器中以表示对应的失败模式。我们的语言条件奖励函数在机器人规划和强化学习中展现出对新环境和新指令的出色泛化能力。

------

Title: Accurate Failure Prediction in Agents Does Not Imply Effective Failure Prevention

URL: https://doi.org/10.48550/arXiv.2602.03338

Abstract: Proactive interventions by LLM critic models are often assumed to improve reliability, yet their effects at deployment time are poorly understood. We show that a binary LLM critic with strong offline accuracy (AUROC 0.94) can nevertheless cause severe performance degradation, inducing a 26 percentage point (pp) collapse on one model while affecting another by near zero pp. This variability demonstrates that LLM critic accuracy alone is insufficient to determine whether intervention is safe. We identify a disruption-recovery tradeoff: interventions may recover failing trajectories but also disrupt trajectories that would have succeeded. Based on this insight, we propose a pre-deployment test that uses a small pilot of 50 tasks to estimate whether intervention is likely to help or harm, without requiring full deployment. Across benchmarks, the test correctly anticipates outcomes: intervention degrades performance on high-success tasks (0 to -26 pp), while yielding a modest improvement on the high-failure ALFWorld benchmark (+2.8 pp, p=0.014). The primary value of our framework is therefore identifying when not to intervene, preventing severe regressions before deployment.

中文翻译：LLM评判模型的主动干预常被认为能提升可靠性，但其在部署时的效果却知之甚少。我们发现一个离线准确率很高（AUROC 0.94）的二值LLM评判器仍可能导致严重的性能退化，在一个模型上引发26个百分点的下降，而对另一个模型几乎无影响。这种变异性表明仅靠LLM评判准确率不足以判断干预是否安全。我们识别出中断-恢复权衡：干预可能挽救失败的轨迹，但也可能中断本会成功的轨迹。基于这一洞察，我们提出一种部署前测试，使用50个任务的小规模试点来估计干预是有益还是有害，无需完整部署。跨基准测试中，该测试正确预见了结果：干预在高成功率任务上降低性能（0到-26 pp），而在高失败的ALFWorld基准上产生适度改善（+2.8 pp, p=0.014）。因此，我们框架的主要价值在于识别何时不应干预，在部署前防止严重的性能退化。

------

Title: Self-Generated Critiques Boost Reward Modeling for Language Models

URL: https://doi.org/10.48550/arXiv.2411.16646

Abstract: Reward modeling is crucial for aligning large language models (LLMs) with human preferences, especially in reinforcement learning from human feedback (RLHF). However, current reward models mainly produce scalar scores and struggle to incorporate critiques in a natural language format. We hypothesize that predicting both critiques and the scalar reward would improve reward modeling ability. Motivated by this, we propose Critic-RM, a framework that improves reward models using self-generated critiques without extra supervision. Critic-RM employs a two-stage process: generating and filtering high-quality critiques, followed by joint fine-tuning on reward prediction and critique generation. Experiments across benchmarks show that Critic-RM improves reward modeling accuracy by 3.7%-7.3% compared to standard reward models and LLM judges, demonstrating strong performance and data efficiency. Additional studies further validate the effectiveness of generated critiques in rectifying flawed reasoning steps with 2.5%-3.2% gains in improving reasoning accuracy.

中文翻译：奖励建模对于使大语言模型（LLM）与人类偏好对齐至关重要，特别是在从人类反馈强化学习（RLHF）中。然而，当前奖励模型主要产生标量分数，难以纳入自然语言形式的批判。我们假设同时预测批判和标量奖励将提升奖励建模能力。受此启发，我们提出Critic-RM，一个使用自生成批判在无额外监督下改进奖励模型的框架。Critic-RM采用两阶段过程：生成和过滤高质量批判，然后联合微调奖励预测和批判生成。跨基准实验表明，Critic-RM将奖励建模准确率比标准奖励模型和LLM评判器提升3.7%-7.3%，展示了强大的性能和数据效率。进一步研究验证了生成批判在纠正有缺陷推理步骤方面的有效性，推理准确率改善2.5%-3.2%。

------

Title: CORA: Conformal Risk-Controlled Agents for Safeguarded Mobile GUI Automation

URL: https://www.semanticscholar.org/paper/7d5756679d40ae4e27cd04b2d6865571f838f46c

Abstract: Graphical user interface (GUI) agents powered by vision language models (VLMs) are rapidly moving from passive assistance to autonomous operation. However, this unrestricted action space exposes users to severe and irreversible financial, privacy or social harm. Existing safeguards rely on prompt engineering, brittle heuristics and VLM-as-critic lack formal verification and user-tunable guarantees. We propose CORA (COnformal Risk-controlled GUI Agent), a post-policy, pre-action safeguarding framework that provides statistical guarantees on harmful executed actions. CORA reformulates safety as selective action execution: we train a Guardian model to estimate action-conditional risk for each proposed step. Rather than thresholding raw scores, we leverage Conformal Risk Control to calibrate an execute/abstain boundary that satisfies a user-specified risk budget and route rejected actions to a trainable Diagnostician model, which performs multimodal reasoning over rejected actions to recommend interventions (e.g., confirm, reflect, or abort) to minimize user burden. A Goal-Lock mechanism anchors assessment to a clarified, frozen user intent to resist visual injection attacks. To rigorously evaluate this paradigm, we introduce Phone-Harm, a new benchmark of mobile safety violations with step-level harm labels under real-world settings. Experiments on Phone-Harm and public benchmarks against diverse baselines validate that CORA improves the safety--helpfulness--interruption Pareto frontier, offering a practical, statistically grounded safety paradigm for autonomous GUI execution. Code and benchmark are available at cora-agent.github.io.

中文翻译：由视觉语言模型（VLM）驱动的GUI Agent正从被动辅助快速转向自主操作。然而，这种不受限的动作空间使用户面临严重且不可逆的财务、隐私或社交损害。现有安全防护依赖提示工程、脆弱的启发式方法和VLM作为评判器，缺乏形式化验证和用户可调保证。我们提出CORA（COnformal Risk-controlled GUI Agent），一个策略后、动作前的安全防护框架，为有害执行动作提供统计保证。CORA将安全重构为选择性动作执行：我们训练Guardian模型为每个建议步骤估计动作条件风险。我们不直接对原始分数设阈值，而是利用共形风险控制来校准执行/放弃边界，满足用户指定的风险预算，并将被拒绝的动作路由到可训练的Diagnostician模型，该模型对被拒绝动作执行多模态推理以推荐干预措施（如确认、反思或中止）。Goal-Lock机制将评估锚定在经澄清的冻结用户意图上，以抵御视觉注入攻击。为严格评估这一范式，我们引入Phone-Harm，一个新基准，在真实世界设置下包含步骤级危害标签。实验验证了CORA改善了安全-有用性-中断的Pareto前沿，为自主GUI执行提供了实用、有统计基础的安全范式。

------

Title: Better Process Supervision with Bi-directional Rewarding Signals

URL: https://doi.org/10.48550/arXiv.2503.04618

Abstract: Process supervision, i.e., evaluating each step, is critical for complex large language model (LLM) reasoning and test-time searching with increased inference compute. Existing approaches, represented by process reward models (PRMs), primarily focus on rewarding signals up to the current step, exhibiting a one-directional nature and lacking a mechanism to model the distance to the final target. To address this problem, we draw inspiration from the A* algorithm, which states that an effective supervisory signal should simultaneously consider the incurred cost and the estimated cost for reaching the target. Building on this key insight, we introduce BiRM, a novel process supervision model that not only evaluates the correctness of previous steps but also models the probability of future success. We conduct extensive experiments on mathematical reasoning tasks and demonstrate that BiRM provides more precise evaluations of LLM reasoning steps, achieving an improvement of 3.1% on Gaokao2023 over PRM under the Best-of-N sampling method. Besides, in search-based strategies, BiRM provides more comprehensive guidance and outperforms ORM by 5.0% and PRM by 3.8% respectively on MATH-500.

中文翻译：过程监督，即评估每个步骤，对于复杂的大语言模型（LLM）推理和使用更多推理计算的测试时搜索至关重要。以过程奖励模型（PRM）为代表的现有方法主要关注到当前步骤为止的奖励信号，表现出单向性，缺乏对到最终目标距离的建模机制。为解决此问题，我们从A*算法获得启发：有效的监督信号应同时考虑已产生成本和到达目标的估计成本。基于这一关键洞察，我们引入BiRM，一种新颖的过程监督模型，不仅评估之前步骤的正确性，还建模未来成功的概率。我们在数学推理任务上进行了广泛实验，证明BiRM为LLM推理步骤提供更精确的评估，在Best-of-N采样方法下，Gaokao2023上比PRM提升3.1%。此外，在基于搜索的策略中，BiRM提供更全面的引导，在MATH-500上分别比ORM和PRM高出5.0%和3.8%。

------

Title: Don't Act Blindly: Robust GUI Automation via Action-Effect Verification and Self-Correction

URL: https://www.semanticscholar.org/paper/5ffe6f76d0b3e56b441955ba20dc4fa23d91412b

Abstract: Autonomous GUI agents based on vision-language models (VLMs) often assume deterministic environment responses, generating actions without verifying whether previous operations succeeded. In real-world settings with network latency, rendering delays, and system interruptions, this assumption leads to undetected action failures, repetitive ineffective behaviors, and catastrophic error accumulation. Moreover, learning robust recovery strategies is challenging due to the high cost of online interaction and the lack of real-time feedback in offline datasets.We propose VeriGUI (Verification-driven GUI Agent), which explicitly models action outcomes and recovery under noisy environments. VeriGUI introduces a Thinking--Verification--Action--Expectation (TVAE) framework to detect failures and guide corrective reasoning, and a two-stage training pipeline that combines Robust SFT with synthetic failure trajectories and GRPO with asymmetric verification rewards. We further construct a Robustness Benchmark based on AndroidControl to evaluate failure recognition and correction. Experiments show that VeriGUI significantly reduces failure loops and improves recovery success while maintaining competitive standard task performance.

中文翻译：基于视觉语言模型（VLM）的自主GUI Agent通常假设确定性环境响应，生成动作时不验证先前操作是否成功。在具有网络延迟、渲染延迟和系统中断的真实世界设置中，这一假设导致未被检测到的动作失败、重复无效行为和灾难性错误累积。此外，由于在线交互成本高以及离线数据集缺乏实时反馈，学习鲁棒的恢复策略具有挑战性。我们提出VeriGUI（Verification-driven GUI Agent），显式建模噪声环境下的动作结果与恢复。VeriGUI引入Thinking-Verification-Action-Expectation（TVAE）框架来检测失败并指导纠错推理，以及一个两阶段训练管线，结合鲁棒SFT（含合成失败轨迹）和带有非对称验证奖励的GRPO。实验表明VeriGUI显著减少失败循环，提高恢复成功率，同时保持有竞争力的标准任务性能。

------

Title: MotIF: Motion Instruction Fine-Tuning

URL: https://doi.org/10.1109/LRA.2025.3527290

Abstract: While success in many robotics tasks can be determined by only observing the final state and how it differs from the initial state – e.g., if an apple is picked up – many tasks require observing the full motion of the robot to correctly determine success. For example, brushing hair requires repeated strokes that correspond to the contours and type of hair. Prior works often use off-the-shelf vision-language models (VLMs) as success detectors; however, when success depends on the full trajectory, VLMs struggle to make correct judgments for two reasons. First, modern VLMs often use single frames, and thus cannot capture changes over a full trajectory. Second, even if we provide state-of-the-art VLMs with an input of multiple frames, they still fail to correctly detect success due to a lack of robot data. Our key idea is to fine-tune VLMs using abstract representations that are able to capture trajectory-level information such as the path the robot takes by overlaying keypoint trajectories on the final image. We propose motion instruction fine-tuning (MotIF), a method that fine-tunes VLMs using the aforementioned abstract representations to semantically ground the robot's behavior in the environment. To benchmark and fine-tune VLMs for robotic motion understanding, we introduce the MotIF-1K dataset containing 653 human and 369 robot demonstrations across 13 task categories with motion descriptions. MotIF assesses the success of robot motion given task and motion instructions. Our model significantly outperforms state-of-the-art API-based single-frame VLMs and video LMs by at least twice in F1 score with high precision and recall, generalizing across unseen motions, tasks, and environments. Finally, we demonstrate practical applications of MotIF in ranking trajectories on how they align with task and motion descriptions.

中文翻译：虽然许多机器人任务的成功可以通过仅观察最终状态及其与初始状态的差异来判断，但许多任务需要观察机器人的完整运动才能正确判断成功。梳头需要与头发轮廓和类型对应的反复梳理动作。先前工作通常使用现成的视觉语言模型（VLM）作为成功检测器；然而，当成功取决于完整轨迹时，VLM由于通常使用单帧而无法捕捉完整轨迹中的变化，且由于缺乏机器人数据而无法正确检测成功。我们的核心思路是使用能够捕捉轨迹级信息（如机器人路径）的抽象表示来微调VLM，方法是在最终图像上叠加关键点轨迹。我们提出运动指令微调（MotIF），使用上述抽象表示微调VLM的方法，将机器人行为语义锚定在环境中。我们引入MotIF-1K数据集，包含13个任务类别的653个人类和369个机器人演示，附带运动描述。我们的模型在F1分数上显著超越最先进的基于API的单帧VLM和视频语言模型至少两倍，并泛化到未见运动、任务和环境。

------

Title: Enhancing Robotic Manipulation with AI Feedback from Multimodal Large Language Models

URL: https://doi.org/10.48550/arXiv.2402.14245

Abstract: Recently, there has been considerable attention towards leveraging large language models (LLMs) to enhance decision-making processes. However, aligning the natural language text instructions generated by LLMs with the vectorized operations required for execution presents a significant challenge, often necessitating task-specific details. To circumvent the need for such task-specific granularity, inspired by preference-based policy learning approaches, we investigate the utilization of multimodal LLMs to provide automated preference feedback solely from image inputs to guide decision-making. In this study, we train a multimodal LLM, termed CriticGPT, capable of understanding trajectory videos in robot manipulation tasks, serving as a critic to offer analysis and preference feedback. Subsequently, we validate the effectiveness of preference labels generated by CriticGPT from a reward modeling perspective. Experimental evaluation of the algorithm's preference accuracy demonstrates its effective generalization ability to new tasks. Furthermore, performance on Meta-World tasks reveals that CriticGPT's reward model efficiently guides policy learning, surpassing rewards based on state-of-the-art pre-trained representation models.

中文翻译：最近，利用大语言模型（LLM）增强决策过程受到了相当关注。然而，将LLM生成的自然语言文本指令与执行所需的向量化操作对齐构成重大挑战，通常需要任务特定的细节。为规避对任务特定粒度的需求，受基于偏好的策略学习方法的启发，我们研究利用多模态LLM仅从图像输入提供自动偏好反馈来引导决策。本研究中，我们训练了一个多模态LLM，称为CriticGPT，能够理解机器人操作任务中的轨迹视频，充当评判者提供分析和偏好反馈。我们从奖励建模的角度验证了CriticGPT生成偏好标签的有效性。算法偏好准确率的实验评估展示了其对新任务的有效泛化能力。在Meta-World任务上的性能表明CriticGPT的奖励模型有效引导策略学习，超越了基于最先进预训练表示模型的奖励。

------

Title: Towards Policy-Compliant Agents: Learning Efficient Guardrails For Policy Violation Detection

URL: https://doi.org/10.48550/arXiv.2510.03485

Abstract: Autonomous web agents need to operate under externally imposed or human-specified policies while generating long-horizon trajectories. However, little work has examined whether these trajectories comply with such policies, or whether policy violations persist across different contexts such as domains (e.g., shopping or coding websites) and subdomains (e.g., product search and order management in shopping). To address this gap, we introduce PolicyGuardBench, a benchmark of about 60k examples for detecting policy violations in agent trajectories. From diverse agent runs, we generate a broad set of policies and create both within subdomain and cross subdomain pairings with violation labels. In addition to full-trajectory evaluation, PolicyGuardBench also includes a prefix-based violation detection task where models must anticipate policy violations from truncated trajectory prefixes rather than complete sequences. Using this dataset, we train PolicyGuard-4B, a lightweight guardrail model that delivers strong detection accuracy across all tasks while keeping inference efficient. Notably, PolicyGuard-4B generalizes across domains and preserves high accuracy on unseen settings. Together, PolicyGuardBench and PolicyGuard-4B provide the first comprehensive framework for studying policy compliance in web agent trajectories, and show that accurate and generalizable guardrails are feasible at small scales.

中文翻译：自主Web Agent在生成长时域轨迹时需要遵循外部强制或人类指定的策略。然而，少有工作检验这些轨迹是否遵守此类策略，或策略违规是否在不同上下文（如不同领域或子领域）中持续存在。为填补这一空白，我们引入PolicyGuardBench，一个包含约60k样本的基准，用于检测Agent轨迹中的策略违规。我们从多样化Agent运行中生成广泛的策略集，并创建领域内和跨领域的配对及违规标签。除完整轨迹评估外，PolicyGuardBench还包括基于前缀的违规检测任务，模型必须从截断的轨迹前缀预测策略违规。使用该数据集，我们训练了PolicyGuard-4B，一个轻量级护栏模型，在所有任务上提供强检测准确率同时保持推理高效。PolicyGuard-4B跨领域泛化并在未见设定中保持高准确率。PolicyGuardBench和PolicyGuard-4B共同提供了研究Web Agent轨迹中策略合规的首个全面框架，并表明在小规模下准确且可泛化的护栏是可行的。

------

Title: AgentV-RL: Scaling Reward Modeling with Agentic Verifier

URL: https://www.semanticscholar.org/paper/b1cded2126609ed07cac9f05254b0c0f56fc2796

Abstract: Verifiers have been demonstrated to enhance LLM reasoning via test-time scaling (TTS). Yet, they face significant challenges in complex domains. Error propagation from incorrect intermediate reasoning can lead to false positives for seemingly plausible solutions, while lacking external grounding makes verifiers unreliable on computation or knowledge-intensive tasks. To address these challenges, we propose Agentic Verifier, a framework that transforms reward modeling into a multi-turn, tool-augmented deliberative process. We introduce complementary forward and backward agents: one traces solutions from premises to conclusions, while the other re-checks conclusions against their underlying premises. This bidirectional process enables a comprehensive, reliable, and interpretable assessment of solutions. To facilitate practical deployment, we propose AgentV-RL. Through proactive exploration and reinforcement learning, the verifier autonomously interleaves tool-use with internal reasoning. Extensive experiments show that Agentic Verifier yields consistent performance gains under both parallel and sequential TTS. Notably, our 4B variant surpasses state-of-the-art ORMs by 25.2%, positioning it as a promising paradigm for agentic reward modeling.

中文翻译：验证器已被证明可通过测试时扩展（TTS）增强LLM推理。然而，它们在复杂领域中面临重大挑战。来自不正确中间推理的错误传播可能导致表面合理解的误报，而缺乏外部锚定使验证器在计算或知识密集型任务上不可靠。为应对这些挑战，我们提出Agentic Verifier，一个将奖励建模转化为多轮、工具增强审慎过程的框架。我们引入互补的正向和反向Agent：一个从前提追踪到结论的解答，另一个将结论重新对照其底层前提。这一双向过程实现对解的全面、可靠且可解释的评估。为促进实际部署，我们提出AgentV-RL。通过主动探索和强化学习，验证器自主地将工具使用与内部推理交错。大量实验表明Agentic Verifier在并行和序贯TTS下均产生一致性能增益。我们的4B变体超越最先进ORM 25.2%，使其成为Agent奖励建模的有前景范式。

------

Title: Improving Reward Models with Synthetic Critiques

URL: https://doi.org/10.48550/arXiv.2405.20850

Abstract: Reward models (RMs) play a critical role in aligning language models through the process of reinforcement learning from human feedback. RMs are trained to predict a score reflecting human preference, which requires significant time and cost for human annotation. Additionally, RMs tend to quickly overfit on superficial features in the training set, hindering their generalization performance on unseen distributions. We propose a novel approach using synthetic natural language critiques generated by large language models to provide additional feedback, evaluating aspects such as instruction following, correctness, and style. This offers richer signals and more robust features for RMs to assess and score on. We demonstrate that high-quality critiques improve the performance and data efficiency of RMs initialized from different pretrained models, reducing the reliance on costly human annotations. Furthermore, incorporating critiques improves both the interpretability and robustness of RM training.

中文翻译：奖励模型（RM）在通过从人类反馈强化学习对齐语言模型的过程中发挥关键作用。RM被训练为预测反映人类偏好的分数，这需要大量时间和成本进行人工标注。此外，RM倾向于快速过拟合训练集中的表面特征，阻碍其在未见分布上的泛化性能。我们提出一种新颖方法，使用大语言模型生成的合成自然语言批判提供额外反馈，评估指令遵循、正确性和风格等方面。这为RM评估和评分提供了更丰富的信号和更鲁棒的特征。我们证明高质量批判改善了从不同预训练模型初始化的RM的性能和数据效率，减少了对昂贵人工标注的依赖。此外，引入批判提高了RM训练的可解释性和鲁棒性。

------

Title: FuRL: Visual-Language Models as Fuzzy Rewards for Reinforcement Learning

URL: https://doi.org/10.48550/arXiv.2406.00645

Abstract: In this work, we investigate how to leverage pre-trained visual-language models (VLM) for online Reinforcement Learning (RL). In particular, we focus on sparse reward tasks with pre-defined textual task descriptions. We first identify the problem of reward misalignment when applying VLM as a reward in RL tasks. To address this issue, we introduce a lightweight fine-tuning method, named Fuzzy VLM reward-aided RL (FuRL), based on reward alignment and relay RL. Specifically, we enhance the performance of SAC/DrQ baseline agents on sparse reward tasks by fine-tuning VLM representations and using relay RL to avoid local minima. Extensive experiments on the Meta-world benchmark tasks demonstrate the efficacy of the proposed method. Code is available at: https://github.com/fuyw/FuRL.

中文翻译：本文中我们研究如何利用预训练视觉语言模型（VLM）进行在线强化学习（RL）。我们特别关注具有预定义文本任务描述的稀疏奖励任务。我们首先识别了将VLM用作RL任务奖励时的奖励不对齐问题。为解决此问题，我们引入了一种轻量级微调方法，名为Fuzzy VLM reward-aided RL（FuRL），基于奖励对齐和接力RL。具体而言，我们通过微调VLM表示并使用接力RL避免局部最小值，增强SAC/DrQ基线Agent在稀疏奖励任务上的性能。在Meta-world基准任务上的大量实验证明了所提方法的有效性。

------

Title: Scaling Agentic Verifier for Competitive Coding

URL: https://doi.org/10.48550/arXiv.2602.04254

Abstract: Large language models (LLMs) have demonstrated strong coding capabilities but still struggle to solve competitive programming problems correctly in a single attempt. Execution-based re-ranking offers a promising test-time scaling strategy, yet existing methods are constrained by either difficult test case generation or inefficient random input sampling. To address this limitation, we propose Agentic Verifier, an execution-based agent that actively reasons about program behaviors and searches for highly discriminative test inputs that expose behavioral discrepancies among candidate solutions. Through multi-turn interaction with code execution environments, the verifier iteratively refines the candidate input generator and produces targeted counterexamples rather than blindly sampling inputs. We train the verifier to acquire this discriminative input generation capability via a scalable pipeline combining large-scale data synthesis, rejection fine-tuning, and agentic reinforcement learning. Extensive experiments across five competitive programming benchmarks demonstrate consistent improvements over strong execution-based baselines, achieving up to +10-15% absolute gains in Best@K accuracy. Further analysis reveals clear test-time scaling behavior and highlights the verifier's broader potential beyond reranking.

中文翻译：大语言模型（LLM）展现了强大的编码能力，但仍难以在单次尝试中正确解决竞赛编程问题。基于执行的重新排序提供了一种有前景的测试时扩展策略，然而现有方法受制于困难的测试用例生成或低效的随机输入采样。为克服这一局限，我们提出Agentic Verifier，一个基于执行的Agent，主动推理程序行为并搜索能暴露候选解间行为差异的高判别性测试输入。通过多轮与代码执行环境的交互，验证器迭代精炼候选输入生成器，产生有针对性的反例而非盲目采样。我们通过结合大规模数据合成、拒绝微调和Agent强化学习的可扩展管线训练验证器获得这一判别性输入生成能力。在五个竞赛编程基准上的广泛实验展示了持续改进，Best@K准确率绝对增益高达+10-15%。进一步分析揭示了清晰的测试时扩展行为，并凸显了验证器在重排序之外的更广泛潜力。

------

Title: Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision

URL: https://doi.org/10.48550/arXiv.2505.19706

Abstract: Large Language Models (LLMs) are prone to hallucination, especially during multi-hop and reasoning-intensive tasks such as mathematical problem solving. While Outcome Reward Models verify only final answers, Process Reward Models (PRMs) score each intermediate step to steer generation toward coherent solutions. We introduce PathFinder-PRM, a novel hierarchical, error-aware discriminative PRM that first classifies math and consistency errors at each step, then combines these fine-grained signals to estimate step correctness. To train PathFinder-PRM, we construct a 400K-sample dataset by enriching the human-annotated PRM800K corpus and RLHFlow Mistral traces with three-dimensional step-level labels. On PRMBench, PathFinder-PRM achieves a new state-of-the-art PRMScore of 67.7, outperforming the prior best (65.5) while using 3 times less data. When applied to reward guided greedy search, our model yields prm@8 48.3, a +1.5 point gain over the strongest baseline. These results demonstrate that decoupled error detection and reward estimation not only boost fine-grained error detection but also substantially improve end-to-end, reward-guided mathematical reasoning with greater data efficiency.

中文翻译：大语言模型（LLM）容易产生幻觉，尤其是在多跳和推理密集型任务如数学问题求解中。虽然结果奖励模型仅验证最终答案，过程奖励模型（PRM）对每个中间步骤评分以引导生成走向连贯解。我们引入PathFinder-PRM，一种新颖的分层、错误感知判别式PRM，首先在每个步骤分类数学错误和一致性错误，然后结合这些细粒度信号估计步骤正确性。为训练PathFinder-PRM，我们通过用三维步骤级标签增强人工标注的PRM800K语料和RLHFlow Mistral轨迹，构建了400K样本数据集。在PRMBench上，PathFinder-PRM以67.7的PRMScore达到新的最优，超越此前最佳（65.5）且数据使用量减少3倍。应用于奖励引导的贪心搜索时，我们的模型产生prm@8 48.3，比最强基线高出+1.5个点。这些结果表明解耦的错误检测和奖励估计不仅提升了细粒度错误检测，还以更高数据效率大幅改善了端到端奖励引导的数学推理。

------

Title: Enhancing LLM Reasoning via Critique Models with Test-Time and Training-Time Supervision

URL: https://doi.org/10.48550/arXiv.2411.16579

Abstract: Training large language models (LLMs) to spend more time thinking and reflection before responding is crucial for effectively solving complex reasoning tasks in fields such as science, coding, and mathematics. However, the effectiveness of mechanisms like self-reflection and self-correction depends on the model's capacity to accurately assess its own performance, which can be limited by factors such as initial accuracy, question difficulty, and the lack of external feedback. In this paper, we delve into a two-player paradigm that separates the roles of reasoning and critique models, where the critique model provides step-level feedback to supervise the reasoning (actor) model during both test-time and train-time. We first propose AutoMathCritique, an automated and scalable framework for collecting critique data, resulting in a dataset of $76,321$ responses paired with step-level feedback. Fine-tuning language models with this dataset enables them to generate natural language feedback for mathematical reasoning. We demonstrate that the critique models consistently improve the actor's performance on difficult queries at test-time, especially when scaling up inference-time computation. Motivated by these findings, we introduce the critique-based supervision to the actor's self-training process, and propose a critique-in-the-loop self-improvement method. Experiments show that the method improves the actor's exploration efficiency and solution diversity, especially on challenging queries, leading to a stronger reasoning model. Lastly, we take the preliminary step to explore training self-talk reasoning models via critique supervision and showcase its potential. Our code and datasets are at \href{https://mathcritique.github.io/}{https://mathcritique.github.io/}.

中文翻译：训练大语言模型（LLM）在回答前花更多时间思考和反思对于有效解决科学、编程和数学等领域的复杂推理任务至关重要。然而，自反思和自我纠错等机制的有效性取决于模型准确评估自身表现的能力，这受到初始准确率、问题难度和缺乏外部反馈等因素的限制。本文中我们深入探讨将推理和批判模型角色分离的双玩家范式，其中批判模型在测试时和训练时提供步骤级反馈来监督推理（Actor）模型。我们首先提出AutoMathCritique，一个自动且可扩展的批判数据收集框架，产生包含76,321个响应与步骤级反馈配对的数据集。用此数据集微调语言模型使其能够为数学推理生成自然语言反馈。我们证明批判模型在测试时持续改进Actor在困难查询上的表现，尤其在扩展推理时计算时更为显著。受这些发现的启发，我们将基于批判的监督引入Actor的自训练过程，提出批判在循环中的自我改进方法。实验表明该方法改善了Actor的探索效率和解答多样性，尤其在挑战性查询上，从而产生更强的推理模型。

------

Title: EVOLVE-VLA: Test-Time Training from Environment Feedback for Vision-Language-Action Models

URL: https://doi.org/10.48550/arXiv.2512.14666

Abstract: Achieving truly adaptive embodied intelligence requires agents that learn not just by imitating static demonstrations, but by continuously improving through environmental interaction, which is akin to how humans master skills through practice. Vision-Language-Action (VLA) models have advanced robotic manipulation by leveraging large language models, yet remain fundamentally limited by Supervised Finetuning (SFT): requiring hundreds of demonstrations per task, rigidly memorizing trajectories, and failing to adapt when deployment conditions deviate from training. We introduce EVOLVE-VLA, a test-time training framework enabling VLAs to continuously adapt through environment interaction with minimal or zero task-specific demonstrations. The key technical challenge is replacing oracle reward signals (unavailable at test time) with autonomous feedback. We address this through a learned progress estimator providing dense feedback, and critically, we design our framework to ``tame''this inherently noisy signal via two mechanisms: (1) an accumulative progress estimation mechanism smoothing noisy point-wise estimates, and (2) a progressive horizon extension strategy enabling gradual policy evolution. EVOLVE-VLA achieves substantial gains: +8.6\% on long-horizon tasks, +22.0\% in 1-shot learning, and enables cross-task generalization -- achieving 20.8\% success on unseen tasks without task-specific demonstrations training (vs. 0\% for pure SFT). Qualitative analysis reveals emergent capabilities absent in demonstrations, including error recovery and novel strategies. This work represents a critical step toward VLAs that truly learn and adapt, moving beyond static imitation toward continuous self-improvements.

中文翻译：实现真正自适应具身智能需要Agent不仅能模仿静态演示学习，还能通过与环境的持续交互不断改进。视觉语言动作（VLA）模型通过利用大语言模型推进了机器人操控，但仍受到监督微调（SFT）的根本限制：每个任务需要数百个演示，僵化地记忆轨迹，当部署条件偏离训练时无法适应。我们引入EVOLVE-VLA，一个测试时训练框架，使VLA能够在最少或零任务特定演示的情况下通过环境交互持续适应。关键的技术挑战是用自主反馈替代不可用的Oracle奖励信号。我们通过学习得到的进度估计器提供密集反馈，并设计了两个机制来驯服这一固有噪声信号：(1)累积进度估计机制平滑噪声逐点估计；(2)渐进时域扩展策略使策略逐步进化。EVOLVE-VLA取得显著收益：长时域任务+8.6%，单样本学习+22.0%，并实现跨任务泛化——在无任务特定演示训练的情况下达到20.8%成功率（纯SFT为0%）。本工作代表了VLA从静态模仿走向持续自我改进的关键一步。

------

Title: Scaling Autonomous Agents via Automatic Reward Modeling And Planning

URL: https://doi.org/10.48550/arXiv.2502.12130

Abstract: Large language models (LLMs) have demonstrated remarkable capabilities across a range of text-generation tasks. However, LLMs still struggle with problems requiring multi-step decision-making and environmental feedback, such as online shopping, scientific reasoning, and mathematical problem-solving. Unlike pure text data, collecting large-scale decision-making data is challenging. Moreover, many powerful LLMs are only accessible through APIs, which hinders their fine-tuning for agent tasks due to cost and complexity. To address LLM agents' limitations, we propose a framework that can automatically learn a reward model from the environment without human annotations. This model can be used to evaluate the action trajectories of LLM agents and provide heuristics for task planning. Specifically, our approach involves employing one LLM-based agent to navigate an environment randomly, generating diverse action trajectories. Subsequently, a separate LLM is leveraged to assign a task intent and synthesize a negative response alongside the correct response for each trajectory. These triplets (task intent, positive response, and negative response) are then utilized as training data to optimize a reward model capable of scoring action trajectories. The effectiveness and generalizability of our framework are demonstrated through evaluations conducted on different agent benchmarks. In conclusion, our proposed framework represents a significant advancement in enhancing LLM agents' decision-making capabilities. By automating the learning of reward models, we overcome the challenges of data scarcity and API limitations, potentially revolutionizing the application of LLMs in complex and interactive environments. This research paves the way for more sophisticated AI agents capable of tackling a wide range of real-world problems requiring multi-step decision-making.

中文翻译：大语言模型（LLM）在一系列文本生成任务中展现了卓越能力。然而，LLM在需要多步决策和环境反馈的问题上仍面临困难，如在线购物、科学推理和数学问题求解。与纯文本数据不同，大规模收集决策数据具有挑战性。此外，许多强大的LLM仅通过API可访问，这因成本和复杂性阻碍了其针对Agent任务的微调。为解决LLM Agent的局限，我们提出一个框架，可以在无人工标注的情况下从环境自动学习奖励模型。该模型可用于评估LLM Agent的动作轨迹并为任务规划提供启发式指导。具体而言，我们的方法涉及使用一个LLM Agent在环境中随机导航，生成多样化动作轨迹。随后，利用另一个LLM为每条轨迹分配任务意图，并合成一个负响应和正确响应。这些三元组（任务意图、正响应和负响应）随后用作训练数据，优化能够对动作轨迹评分的奖励模型。在不同Agent基准上进行的评估证明了我们框架的有效性和泛化能力。

------

Title: Efficient PRM Training Data Synthesis via Formal Verification

URL: https://www.semanticscholar.org/paper/63ff7a4e5f37821220ef9037d2ad23fad0d6efd6

Abstract: Process Reward Models (PRMs) have emerged as a promising approach for improving LLM reasoning capabilities by providing process supervision over reasoning traces. However, existing approaches for constructing PRM training data remain costly and noisy, as they typically rely on human annotation or sampling-based labeling methods that require repeated LLM calls. In this work, we propose FoVer, a framework that synthesizes PRM training data from formal reasoning tasks by annotating step-level error labels using formal verification tools such as Z3 and Isabelle. By leveraging formal verification, FoVer enables efficient and accurate PRM data construction without requiring human annotation or additional LLM calls. Using FoVer, we create PRM training data from formal logic and theorem proving tasks. Experiments on 12 reasoning benchmarks show that fine-tuning on our training data improves PRMs not only on math and logic reasoning tasks, which are informal variants of the training tasks, but also on NLI and BBH benchmarks, which differ substantially from the tasks used to construct the training data. These results demonstrate the practical effectiveness of FoVer, showing that PRM training data created using formal verification improves PRMs on informal reasoning tasks written in natural language. The datasets, models, and code are provided at https://github.com/psunlpgroup/FoVer.

中文翻译：过程奖励模型（PRM）已成为通过提供推理轨迹过程监督来改进LLM推理能力的有前景方法。然而，构建PRM训练数据的现有方法仍然昂贵且噪声大，因为它们通常依赖人类标注或需要重复LLM调用的基于采样的标注方法。本文中我们提出FoVer，一个从形式推理任务合成PRM训练数据的框架，通过使用形式验证工具（如Z3和Isabelle）标注步骤级错误标签。通过利用形式验证，FoVer实现了高效且精确的PRM数据构建，无需人工标注或额外的LLM调用。使用FoVer，我们从形式逻辑和定理证明任务创建PRM训练数据。在12个推理基准上的实验表明，在我们的训练数据上微调不仅改进了PRM在数学和逻辑推理任务上的表现，还改进了在NLI和BBH基准上的表现，这些基准与构建训练数据所用的任务有显著差异。这些结果展示了FoVer的实际有效性。

------

Title: Teaching Language Models to Critique via Reinforcement Learning

URL: https://doi.org/10.48550/arXiv.2502.03492

Abstract: Teaching large language models (LLMs) to critique and refine their outputs is crucial for building systems that can iteratively improve, yet it is fundamentally limited by the ability to provide accurate judgments and actionable suggestions. In this work, we study LLM critics for code generation and propose $\texttt{CTRL}$, a framework for $\texttt{C}$ritic $\texttt{T}$raining via $\texttt{R}$einforcement $\texttt{L}$earning, which trains a critic model to generate feedback that maximizes correction performance for a fixed generator model without human supervision. Our results demonstrate that critics trained with $\texttt{CTRL}$ significantly enhance pass rates and mitigate compounding errors across both base and stronger generator models. Furthermore, we show that these critic models act as accurate generative reward models and enable test-time scaling through iterative critique-revision, achieving up to 106.1% relative improvements across challenging code generation benchmarks.

中文翻译：教导大语言模型（LLM）批判和精炼自己的输出对构建能迭代改进的系统至关重要，但这从根本上受限于提供准确判断和可操作建议的能力。本文中我们研究代码生成的LLM批判模型，提出CTRL（Critic Training via Reinforcement Learning），一个通过强化学习训练批判模型的框架，使其生成能在无人类监督下最大化固定生成器模型纠正性能的反馈。我们的结果表明，用CTRL训练的批判模型显著提升了基础模型和更强生成器模型的通过率，并减轻了复合错误。此外，我们证明这些批判模型可作为精确的生成式奖励模型，通过迭代批判-修订实现测试时扩展，在具有挑战性的代码生成基准上取得高达106.1%的相对提升。

------

Title: Self-Refining Vision Language Model for Robotic Failure Detection and Reasoning

URL: https://doi.org/10.48550/arXiv.2602.12405

Abstract: Reasoning about failures is crucial for building reliable and trustworthy robotic systems. Prior approaches either treat failure reasoning as a closed-set classification problem or assume access to ample human annotations. Failures in the real world are typically subtle, combinatorial, and difficult to enumerate, whereas rich reasoning labels are expensive to acquire. We address this problem by introducing ARMOR: Adaptive Round-based Multi-task mOdel for Robotic failure detection and reasoning. We formulate detection and reasoning as a multi-task self-refinement process, where the model iteratively predicts detection outcomes and natural language reasoning conditioned on past outputs. During training, ARMOR learns from heterogeneous supervision - large-scale sparse binary labels and small-scale rich reasoning annotations - optimized via a combination of offline and online imitation learning. At inference time, ARMOR generates multiple refinement trajectories and selects the most confident prediction via a self-certainty metric. Experiments across diverse environments show that ARMOR achieves state-of-the-art performance by improving over the previous approaches by up to 30% on failure detection rate and up to 100% in reasoning measured through LLM fuzzy match score, demonstrating robustness to heterogeneous supervision and open-ended reasoning beyond predefined failure modes. We provide dditional visualizations on our website: https://sites.google.com/utexas.edu/armor

中文翻译：推理失败对于构建可靠可信的机器人系统至关重要。先前方法要么将失败推理视为闭集分类问题，要么假设可获得充足的人工标注。真实世界中的失败通常是微妙的、组合性的，难以枚举，而丰富的推理标签获取成本高昂。我们通过引入ARMOR（Adaptive Round-based Multi-task mOdel for Robotic failure detection and reasoning）来解决这一问题。我们将检测和推理形式化为多任务自我精炼过程，其中模型基于过去输出迭代预测检测结果和自然语言推理。训练期间，ARMOR从异构监督中学习——大规模稀疏二值标签和小规模丰富推理标注——通过离线与在线模仿学习的组合进行优化。推理时，ARMOR生成多个精炼轨迹并通过自确定性度量选择最有信心的预测。在多样化环境中的实验表明ARMOR达到最优性能，失败检测率超越先前方法高达30%，通过LLM模糊匹配分数衡量的推理提升高达100%，展示了对异构监督和超越预定义失败模式的开放推理的鲁棒性。

------

Title: No More Stale Feedback: Co-Evolving Critics for Open-World Agent Learning

URL: https://doi.org/10.48550/arXiv.2601.06794

Abstract: Critique-guided reinforcement learning (RL) has emerged as a powerful paradigm for training LLM agents by augmenting sparse outcome rewards with natural-language feedback. However, current methods often rely on static or offline critic models, which fail to adapt as the policy evolves. In on-policy RL, the agent's error patterns shift over time, causing stationary critics to become stale and providing feedback of diminishing utility. To address this, we introduce ECHO (Evolving Critic for Hindsight-Guided Optimization)}, a framework that jointly optimizes the policy and critic through a synchronized co-evolutionary loop. ECHO utilizes a cascaded rollout mechanism where the critic generates multiple diagnoses for an initial trajectory, followed by policy refinement to enable group-structured advantage estimation. We address the challenge of learning plateaus via a saturation-aware gain shaping objective, which rewards the critic for inducing incremental improvements in high-performing trajectories. By employing dual-track GRPO updates, ECHO ensures the critic's feedback stays synchronized with the evolving policy. Experimental results show that ECHO yields more stable training and higher long-horizon task success across open-world environments.

中文翻译：批判引导的强化学习（RL）已成为通过用自然语言反馈增强稀疏结果奖励来训练LLM Agent的强大范式。然而，当前方法通常依赖静态或离线批判模型，这些模型无法随着策略的演进而适应。在在线策略RL中，Agent的错误模式随时间变化，导致静态批判器变得陈旧，其反馈效用递减。为此，我们引入ECHO（Evolving Critic for Hindsight-Guided Optimization），一个通过同步共同进化循环联合优化策略和批判器的框架。ECHO利用级联rollout机制，其中批判器为初始轨迹生成多个诊断，随后策略精炼以实现分组结构化优势估计。我们通过饱和感知增益塑造目标来解决学习平台期挑战，该目标奖励批判器在高性能轨迹中诱导增量改进。通过使用双轨GRPO更新，ECHO确保批判器的反馈与演进的策略保持同步。实验结果表明ECHO在开放世界环境中产生更稳定的训练和更高的长时域任务成功率。

------

Title: SPC: Evolving Self-Play Critic via Adversarial Games for LLM Reasoning

URL: https://doi.org/10.48550/arXiv.2504.19162

Abstract: Evaluating the step-by-step reliability of large language model (LLM) reasoning, such as Chain-of-Thought, remains challenging due to the difficulty and cost of obtaining high-quality step-level supervision. In this paper, we introduce Self-Play Critic (SPC), a novel approach where a critic model evolves its ability to assess reasoning steps through adversarial self-play games, eliminating the need for manual step-level annotation. SPC involves fine-tuning two copies of a base model to play two roles, namely a"sneaky generator"that deliberately produces erroneous steps designed to be difficult to detect, and a"critic"that analyzes the correctness of reasoning steps. These two models engage in an adversarial game in which the generator aims to fool the critic, while the critic model seeks to identify the generator's errors. Using reinforcement learning based on the game outcomes, the models iteratively improve; the winner of each confrontation receives a positive reward and the loser receives a negative reward, driving continuous self-evolution. Experiments on three reasoning process benchmarks (ProcessBench, PRM800K, DeltaBench) demonstrate that our SPC progressively enhances its error detection capabilities (e.g., accuracy increases from 70.8% to 77.7% on ProcessBench) and surpasses strong baselines, including distilled R1 model. Furthermore, SPC can guide the test-time search of diverse LLMs and significantly improve their mathematical reasoning performance on MATH500 and AIME2024, surpassing those guided by state-of-the-art process reward models.

中文翻译：由于获取高质量步骤级监督的难度和成本，评估大语言模型（LLM）推理的逐步可靠性仍具挑战。本文中我们引入自博弈批判（SPC），一种新颖的方法，批判模型通过对抗性自博弈游戏进化其评估推理步骤的能力，无需人工步骤级标注。SPC涉及微调基座模型的两个副本扮演两个角色，即一个狡猾生成器故意产生难以检测的错误步骤，和一个批判器分析推理步骤的正确性。两个模型进行对抗博弈：生成器旨在欺骗批判器，而批判器寻求识别生成器的错误。基于博弈结果使用强化学习，模型迭代改进；每次对抗的胜者获得正奖励，败者获得负奖励，驱动持续自我进化。在三个推理过程基准（ProcessBench、PRM800K、DeltaBench）上的实验表明，我们的SPC逐步增强其错误检测能力（例如ProcessBench上准确率从70.8%提升至77.7%），并超越强基线包括蒸馏R1模型。此外，SPC可以引导多样化LLM的测试时搜索并显著提升其在MATH500和AIME2024上的数学推理性能。

------

Title: Code as Reward: Empowering Reinforcement Learning with VLMs

URL: https://doi.org/10.48550/arXiv.2402.04764

Abstract: Pre-trained Vision-Language Models (VLMs) are able to understand visual concepts, describe and decompose complex tasks into sub-tasks, and provide feedback on task completion. In this paper, we aim to leverage these capabilities to support the training of reinforcement learning (RL) agents. In principle, VLMs are well suited for this purpose, as they can naturally analyze image-based observations and provide feedback (reward) on learning progress. However, inference in VLMs is computationally expensive, so querying them frequently to compute rewards would significantly slowdown the training of an RL agent. To address this challenge, we propose a framework named Code as Reward (VLM-CaR). VLM-CaR produces dense reward functions from VLMs through code generation, thereby significantly reducing the computational burden of querying the VLM directly. We show that the dense rewards generated through our approach are very accurate across a diverse set of discrete and continuous environments, and can be more effective in training RL policies than the original sparse environment rewards.

中文翻译：预训练视觉语言模型（VLM）能够理解视觉概念，描述和分解复杂任务为子任务，并提供任务完成反馈。本文中我们旨在利用这些能力支持强化学习（RL）Agent的训练。原则上VLM非常适合这一目的，因为它们可以自然地分析基于图像的观测并在学习进展上提供反馈（奖励）。然而，VLM推理计算开销大，频繁查询VLM来计算奖励将显著拖慢RL Agent的训练。为应对这一挑战，我们提出Code as Reward（VLM-CaR）框架。VLM-CaR通过代码生成从VLM产生密集奖励函数，从而大幅减轻直接查询VLM的计算负担。我们证明通过此方法生成的密集奖励在多种离散和连续环境中非常精确，并且在训练RL策略时比原始稀疏环境奖励更有效。

------

Title: SCRIBE: Structured Mid-Level Supervision for Tool-Using Language Models

URL: https://doi.org/10.48550/arXiv.2601.03555

Abstract: Training reliable tool-augmented agents remains a significant challenge, largely due to the difficulty of credit assignment in multi-step reasoning. While process-level reward models offer a promising direction, existing LLM-based judges often produce noisy and inconsistent signals because they lack fine-grained, task-specific rubrics to distinguish high-level planning from low-level execution. In this work, we introduce SCRIBE (Skill-Conditioned Reward with Intermediate Behavioral Evaluation), a reinforcement learning framework that intervenes at a novel mid-level abstraction. SCRIBE grounds reward modeling in a curated library of skill prototypes, transforming open-ended LLM evaluation into a constrained verification problem. By routing each subgoal to a corresponding prototype, the reward model is equipped with precise, structured rubrics that substantially reduce reward variance. Experimental results show that SCRIBE achieves state-of-the-art performance across a range of reasoning and tool-use benchmarks. In particular, it improves the AIME25 accuracy of a Qwen3-4B model from 43.3% to 63.3%, and significantly increases success rates in complex multi-turn tool interactions. Further analysis of training dynamics reveals a co-evolution across abstraction levels, where mastery of mid-level skills consistently precedes the emergence of effective high-level planning behaviors. Finally, we demonstrate that SCRIBE is additive to low-level tool optimizations, providing a scalable and complementary pathway toward more autonomous and reliable tool-using agents.

中文翻译：训练可靠的工具增强Agent仍是一个重大挑战，很大程度源于多步推理中的信用分配困难。过程级奖励模型提供了一个有前景的方向，但现有基于LLM的评判器由于缺乏细粒度、任务特定的量规来区分高层规划和低层执行，常常产生嘈杂且不一致的信号。本文中我们引入SCRIBE（Skill-Conditioned Reward with Intermediate Behavioral Evaluation），一个在新型中层抽象上介入的强化学习框架。SCRIBE将奖励建模锚定在精心策划的技能原型库中，将开放式LLM评估转化为受约束的验证问题。通过将每个子目标路由到相应原型，奖励模型配备了精确的结构化量规，显著降低奖励方差。实验结果表明SCRIBE在一系列推理和工具使用基准上取得最优性能。特别是它将Qwen3-4B模型的AIME25准确率从43.3%提升至63.3%，并在复杂多轮工具交互中显著提高成功率。训练动力学的进一步分析揭示了跨抽象层的共同进化，中层技能的掌握先于有效高层规划行为的出现。

------

Title: Uncertainty-Aware Step-wise Verification with Generative Reward Models

URL: https://doi.org/10.48550/arXiv.2502.11250

Abstract: Complex multi-step reasoning tasks, such as solving mathematical problems, remain challenging for large language models (LLMs). While outcome supervision is commonly used, process supervision via process reward models (PRMs) provides intermediate rewards to verify step-wise correctness in solution traces. However, as proxies for human judgement, PRMs suffer from reliability issues, including susceptibility to reward hacking. In this work, we propose leveraging uncertainty quantification (UQ) to enhance the reliability of step-wise verification with generative reward models for mathematical reasoning tasks. We introduce CoT Entropy, a novel UQ method that outperforms existing approaches in quantifying a PRM's uncertainty in step-wise verification. Our results demonstrate that incorporating uncertainty estimates improves the robustness of judge-LM PRMs, leading to more reliable verification.

中文翻译：复杂多步推理任务（如数学问题求解）仍是大语言模型（LLM）面临的挑战。虽然结果监督被普遍使用，但通过过程奖励模型（PRM）的过程监督提供中间奖励来验证解轨迹中的逐步正确性。然而，作为人类判断的代理，PRM存在可靠性问题，包括易受奖励黑客攻击。本文中我们提出利用不确定性量化（UQ）增强生成式奖励模型在数学推理任务中逐步验证的可靠性。我们引入CoT Entropy，一种新颖的UQ方法，在量化PRM逐步验证中的不确定性方面优于现有方法。我们的结果表明纳入不确定性估计提高了评判器LLM PRM的鲁棒性，从而产生更可靠的验证。

------

Title: Natural Language Actor-Critic: Scalable Off-Policy Learning in Language Space

URL: https://doi.org/10.48550/arXiv.2512.04601

Abstract: Large language model (LLM) agents -- LLMs that dynamically interact with an environment over long horizons -- have become an increasingly important area of research, enabling automation in complex tasks involving tool-use, web browsing, and dialogue with people. In the absence of expert demonstrations, training LLM agents has relied on policy gradient methods that optimize LLM policies with respect to an (often sparse) reward function. However, in long-horizon tasks with sparse rewards, learning from trajectory-level rewards can be noisy, leading to training that is unstable and has high sample complexity. Furthermore, policy improvement hinges on discovering better actions through exploration, which can be difficult when actions lie in natural language space. In this paper, we propose Natural Language Actor-Critic (NLAC), a novel actor-critic algorithm that trains LLM policies using a generative LLM critic that produces natural language rather than scalar values. This approach leverages the inherent strengths of LLMs to provide a richer and more actionable training signal; particularly, in tasks with large, open-ended action spaces, natural language explanations for why an action is suboptimal can be immensely useful for LLM policies to reason how to improve their actions, without relying on random exploration. Furthermore, our approach can be trained off-policy without policy gradients, offering a more data-efficient and stable alternative to existing on-policy methods. We present results on a mixture of reasoning, web browsing, and tool-use with dialogue tasks, demonstrating that NLAC shows promise in outperforming existing training approaches and offers a more scalable and stable training paradigm for LLM agents.

中文翻译：大语言模型（LLM）Agent——在长时域上与环境动态交互的LLM——已成为日益重要的研究领域，使涉及工具使用、Web浏览和与人对话的复杂任务自动化成为可能。在缺乏专家演示的情况下，训练LLM Agent依赖策略梯度方法，对（通常稀疏的）奖励函数优化LLM策略。然而，在稀疏奖励的长时域任务中，从轨迹级奖励学习可能噪声大，导致训练不稳定且样本复杂度高。此外，策略改进取决于通过探索发现更好的动作，而动作在自然语言空间中时这可能是困难的。本文中我们提出Natural Language Actor-Critic（NLAC），一种新颖的Actor-Critic算法，使用生成式LLM Critic产生自然语言而非标量值来训练LLM策略。该方法利用LLM的固有能力提供更丰富、更可操作的训练信号；特别是在具有大型开放式动作空间的任务中，解释某个动作为何次优的自然语言说明对于LLM策略推理如何改进其动作极为有用。此外，我们的方法可以off-policy训练而无需策略梯度，提供了比现有on-policy方法更具数据效率和更稳定的替代方案。我们在推理、Web浏览和包含对话的工具使用混合任务上展示了结果，证明NLAC在超越现有训练方法方面展现了前景。

------

Title: DeepCritic: Deliberate Critique with Large Language Models

URL: https://doi.org/10.48550/arXiv.2505.00662

Abstract: As Large Language Models (LLMs) are rapidly evolving, providing accurate feedback and scalable oversight on their outputs becomes an urgent and critical problem. Leveraging LLMs as critique models to achieve automated supervision is a promising solution. In this work, we focus on studying and enhancing the math critique ability of LLMs. Current LLM critics provide critiques that are too shallow and superficial on each step, leading to low judgment accuracy and struggling to offer sufficient feedback for the LLM generator to correct mistakes. To tackle this issue, we propose a novel and effective two-stage framework to develop LLM critics that are capable of deliberately critiquing on each reasoning step of math solutions. In the first stage, we utilize Qwen2.5-72B-Instruct to generate 4.5K long-form critiques as seed data for supervised fine-tuning. Each seed critique consists of deliberate step-wise critiques that includes multi-perspective verifications as well as in-depth critiques of initial critiques for each reasoning step. Then, we perform reinforcement learning on the fine-tuned model with either existing human-labeled data from PRM800K or our automatically annotated data obtained via Monte Carlo sampling-based correctness estimation, to further incentivize its critique ability. Our developed critique model built on Qwen2.5-7B-Instruct not only significantly outperforms existing LLM critics (including the same-sized DeepSeek-R1-distill models and GPT-4o) on various error identification benchmarks, but also more effectively helps the LLM generator refine erroneous steps through more detailed feedback.

中文翻译：随着大语言模型（LLM）的快速发展，为其输出提供准确反馈和可扩展监督已成为紧迫且关键的问题。利用LLM作为批判模型来实现自动监督是一个有前景的解决方案。本文中我们专注于研究和增强LLM的数学批判能力。当前LLM批判器提供的批判过于浅层和表面化，导致判断准确率低，并难以为LLM生成器提供足够反馈来纠正错误。为解决这一问题，我们提出一个新颖有效的两阶段框架来开发能够对数学解的每个推理步骤进行深思熟虑批判的LLM批判器。在第一阶段，我们利用Qwen2.5-72B-Instruct生成4.5K长文本批判作为监督微调的种子数据。每个种子批判由深思熟虑的逐步骤批判组成，包括多视角验证和对每个推理步骤的初始批判的深入 批判。然后，我们使用PRM800K的现有人工标注数据或自动标注数据，对微调模型进行强化学习，进一步激励其批判能力。我们基于Qwen2.5-7B-Instruct构建的批判模型不仅在各种错误识别基准上显著超越现有LLM批判器（包括同规模的DeepSeek-R1蒸馏模型和GPT-4o），还通过更详细的反馈更有效地帮助LLM生成器精炼错误步骤。

------

Title: Policy Improvement using Language Feedback Models

URL: https://doi.org/10.48550/arXiv.2402.07876

Abstract: We introduce Language Feedback Models (LFMs) that identify desirable behaviour - actions that help achieve tasks specified in the instruction - for imitation learning in instruction following. To train LFMs, we obtain feedback from Large Language Models (LLMs) on visual trajectories verbalized to language descriptions. First, by using LFMs to identify desirable behaviour to imitate, we improve in task-completion rate over strong behavioural cloning baselines on three distinct language grounding environments (Touchdown, ScienceWorld, and ALFWorld). Second, LFMs outperform using LLMs as experts to directly predict actions, when controlling for the number of LLM output tokens. Third, LFMs generalize to unseen environments, improving task-completion rate by 3.5-12.0% through one round of adaptation. Finally, LFM can be modified to provide human-interpretable feedback without performance loss, allowing human verification of desirable behaviour for imitation learning.

中文翻译：我们引入语言反馈模型（LFM），它能识别有利行为——即有助于完成指令中指定任务的动作——用于指令遵循中的模仿学习。为训练LFM，我们从大语言模型（LLM）获取关于被语言化描述为文本的视觉轨迹的反馈。首先，通过使用LFM识别有利行为进行模仿，我们在三个不同的语言锚定环境（Touchdown、ScienceWorld和ALFWorld）中超越了强行为克隆基线的任务完成率。其次，在控制LLM输出token数量的情况下，LFM优于将LLM直接预测动作作为专家的方法。第三，LFM泛化到未见环境，通过一轮适应将任务完成率提升3.5-12.0%。最后，LFM可被修改为提供人类可解释的反馈而不损失性能，允许对模仿学习中的有利行为进行人工验证。

------

Title: AURORA: Automated Training Framework of Universal Process Reward Models via Ensemble Prompting and Reverse Verification

URL: https://doi.org/10.1145/3770854.3780168

Abstract: The reasoning capabilities of advanced large language models (LLMs) like o1 have revolutionized artificial intelligence applications. Nevertheless, evaluating and optimizing complex reasoning processes remain significant challenges due to diverse policy distributions and the inherent limitations of human effort and accuracy. In this paper, we present AURORA, a novel automated framework for training universal process reward models (PRMs) using ensemble prompting and reverse verification. The framework employs a two-phase approach: First, it uses diverse prompting strategies and ensemble methods to perform automated annotation and evaluation of processes, ensuring robust assessments for reward learning. Second, it leverages practical reference answers for reverse verification, enhancing the model's ability to validate outputs and improving training accuracy. To assess the framework's performance, we extend beyond the existing ProcessBench benchmark by introducing UniversalBench, which evaluates reward predictions across full trajectories under diverse policy distribtion with long Chain-of-Thought (CoT) outputs. Experimental results demonstrate that AURORA enhances process evaluation accuracy, improves PRMs' accuracy for diverse policy distributions and long-CoT responses.

中文翻译：o1等先进大语言模型（LLM）的推理能力已革新了人工智能应用。然而，由于策略分布的多样性和人类努力与准确性的固有局限，评估和优化复杂推理过程仍是重大挑战。本文中我们提出AURORA，一个使用集成提示和反向验证训练通用过程奖励模型（PRM）的新颖自动化框架。该框架采用两阶段方法：首先使用多样化提示策略和集成方法进行过程的自动标注和评估，确保奖励学习的鲁棒评估。其次利用实际参考答案进行反向验证，增强模型验证输出和提升训练准确率的能力。为评估框架性能，我们在现有ProcessBench基准之外扩展引入了UniversalBench，评估不同策略分布和长思维链（CoT）输出下全轨迹的奖励预测。实验结果表明AURORA提升了过程评估准确率，改善了PRM对不同策略分布和长CoT响应的准确率。

------

Title:Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training

URL: https://doi.org/10.48550/arXiv.2501.11425

Abstract: Large Language Models (LLMs) agents are increasingly pivotal for addressing complex tasks in interactive environments. Existing work mainly focuses on enhancing performance through behavior cloning from stronger experts, yet such approaches often falter in real-world applications, mainly due to the inability to recover from errors. However, step-level critique data is difficult and expensive to collect. Automating and dynamically constructing self-critique datasets is thus crucial to empowering models with intelligent agent capabilities. In this work, we propose an iterative self-training framework, Agent-R, that enables language Agent to Reflect on the fly. Unlike traditional methods that reward or penalize actions based on correctness, Agent-R leverages MCTS to construct training data that recover correct trajectories from erroneous ones. A key challenge of agent reflection lies in the necessity for timely revision rather than waiting until the end of a rollout. To address this, we introduce a model-guided critique construction mechanism: the actor model identifies the first error step (within its current capability) in a failed trajectory. Starting from it, we splice it with the adjacent correct path, which shares the same parent node in the tree. This strategy enables the model to learn reflection based on its current policy, therefore yielding better learning efficiency. To further explore the scalability of this self-improvement paradigm, we investigate iterative refinement of both error correction capabilities and dataset construction. Our findings demonstrate that Agent-R continuously improves the model's ability to recover from errors and enables timely error correction. Experiments on three interactive environments show that Agent-R effectively equips agents to correct erroneous actions while avoiding loops, achieving superior performance compared to baseline methods (+5.59%).

中文翻译：大语言模型（LLM）Agent在交互式环境中解决复杂任务的作用日益关键。现有工作主要聚焦于通过从强专家行为克隆来提升性能，但这些方法在真实应用中常常失败，主要因为无法从错误中恢复。然而，步骤级批判数据难以收集且成本高昂。自动化和动态构建自批判数据集因此对赋予模型智能Agent能力至关重要。本文中我们提出Agent-R，一个迭代自训练框架，使语言Agent能够动态反思。不同于基于正确性奖励或惩罚动作的传统方法，Agent-R利用MCTS构建从错误轨迹恢复到正确轨迹的训练数据。Agent反思的一个关键挑战在于需要及时修正而非等到rollout结束。为此我们引入模型引导的批判构建机制：Actor模型识别失败轨迹中第一个错误步骤，从此处开始将其与共享树中相同父节点的相邻正确路径拼接。这一策略使模型能够基于其当前策略学习反思，因此产生更好的学习效率。在三个交互环境上的实验显示Agent-R有效赋予Agent纠正错误动作同时避免循环的能力，相比基线方法取得卓越性能（+5.59%）。

------

Title: SPARK: Stepwise Process-Aware Rewards for Reference-Free Reinforcement Learning

URL: https://doi.org/10.48550/arXiv.2512.03244

Abstract: Process reward models (PRMs) that provide dense, step-level feedback have shown promise for reinforcement learning, yet their adoption remains limited by the need for expensive step-level annotations or ground truth references. We propose SPARK: a three-stage framework where in the first stage a generator model produces diverse solutions and a verifier model evaluates them using parallel scaling (self-consistency) and sequential scaling (meta-critique). In the second stage, we use these verification outputs as synthetic training data to fine-tune generative process reward models, which subsequently serve as reward signals during training. We show that aggregating multiple independent verifications at the step level produces training data for process reward models that surpass ground-truth outcome supervision, achieving 67.5 F1 on ProcessBench (a benchmark for identifying erroneous steps in mathematical reasoning) compared to 66.4 for reference-guided training and 61.9 for GPT-4o. In the final stage, we apply our generative PRM with chain-of-thought verification (PRM-CoT) as the reward model in RL experiments on mathematical reasoning, and introduce format constraints to prevent reward hacking. Using Qwen2.5-Math-7B, we achieve 47.4% average accuracy across six mathematical reasoning benchmarks, outperforming ground-truth-based RLVR (43.9%). Our work enables reference-free RL training that exceeds ground-truth methods, opening new possibilities for domains lacking verifiable answers or accessible ground truth.

中文翻译：提供密集步骤级反馈的过程奖励模型（PRM）在强化学习中展现了前景，但其采用仍受限于对昂贵步骤级标注或标准答案参考的需求。我们提出SPARK：一个三阶段框架，第一阶段生成器模型产生多样化解，验证器模型使用并行扩展（自一致性）和序贯扩展（元批判）评估它们。第二阶段我们使用这些验证输出作为合成训练数据微调生成式过程奖励模型，其随后在训练中充当奖励信号。我们证明在步骤级聚合多个独立验证产生的过程奖励模型训练数据超越了标准答案结果监督，在ProcessBench上达到67.5 F1。在最后阶段，我们将带有思维链验证的生成式PRM（PRM-CoT）作为奖励模型应用于数学推理的RL实验中，并引入格式约束防止奖励黑客。使用Qwen2.5-Math-7B，我们在六个数学推理基准上达到47.4%的平均准确率，超越基于标准答案的RLVR（43.9%）。

------

Title: VerIF: Verification Engineering for Reinforcement Learning in Instruction Following

URL: https://doi.org/10.48550/arXiv.2506.09942

Abstract: Reinforcement learning with verifiable rewards (RLVR) has become a key technique for enhancing large language models (LLMs), with verification engineering playing a central role. However, best practices for RL in instruction following remain underexplored. In this work, we explore the verification challenge in RL for instruction following and propose VerIF, a verification method that combines rule-based code verification with LLM-based verification from a large reasoning model (e.g., QwQ-32B). To support this approach, we construct a high-quality instruction-following dataset, VerInstruct, containing approximately 22,000 instances with associated verification signals. We apply RL training with VerIF to two models, achieving significant improvements across several representative instruction-following benchmarks. The trained models reach state-of-the-art performance among models of comparable size and generalize well to unseen constraints. We further observe that their general capabilities remain unaffected, suggesting that RL with VerIF can be integrated into existing RL recipes to enhance overall model performance. We have released our datasets, codes, and models to facilitate future research at https://github.com/THU-KEG/VerIF.

中文翻译：使用可验证奖励的强化学习（RLVR）已成为增强大语言模型（LLM）的关键技术，验证工程在其中扮演中心角色。然而，指令遵循中RL的最佳实践仍未被充分探索。本文中我们探索了指令遵循RL中的验证挑战并提出VerIF，一个将基于规则的代码验证与来自大型推理模型（如QwQ-32B）的基于LLM验证相结合的方法。为支持这一方法，我们构建了高质量指令遵循数据集VerInstruct，包含约22,000个实例及相关验证信号。我们使用VerIF对两个模型应用RL训练，在多个代表性指令遵循基准上取得显著改进。训练模型在可比规模的模型中达到最优性能，并对未见约束泛化良好。我们进一步观察到它们的通用能力未受影响，表明使用VerIF的RL可以整合到现有RL配方中以增强模型整体性能。

------

Title: Self-Taught Evaluators

URL: https://doi.org/10.48550/arXiv.2408.02666

Abstract: Model-based evaluation is at the heart of successful model development -- as a reward model for training, and as a replacement for human evaluation. To train such evaluators, the standard approach is to collect a large amount of human preference judgments over model responses, which is costly and the data becomes stale as models improve. In this work, we present an approach that aims to im-prove evaluators without human annotations, using synthetic training data only. Starting from unlabeled instructions, our iterative self-improvement scheme generates contrasting model outputs and trains an LLM-as-a-Judge to produce reasoning traces and final judgments, repeating this training at each new iteration using the improved predictions. Without any labeled preference data, our Self-Taught Evaluator can improve a strong LLM (Llama3-70B-Instruct) from 75.4 to 88.3 (88.7 with majority vote) on RewardBench. This outperforms commonly used LLM judges such as GPT-4 and matches the performance of the top-performing reward models trained with labeled examples.

中文翻译：基于模型的评估是成功模型开发的核心——作为训练的奖励模型以及人类评估的替代。训练此类评估器的标准方法是收集大量人类对模型响应的偏好判断，这成本高昂且随着模型改进数据变得过时。本文中我们提出一种仅使用合成训练数据而无人类标注来改进评估器的方法。从未标注指令出发，我们的迭代自我改进方案生成对比性模型输出，并训练LLM-as-a-Judge产生推理轨迹和最终判断，每次新迭代使用改进后的预测重复训练。在没有任何标注偏好数据的情况下，我们的Self-Taught Evaluator可以将强LLM（Llama3-70B-Instruct）在RewardBench上从75.4提升到88.3（多数投票下88.7）。这超越了常用的LLM评判器如GPT-4，并匹敌使用标注样本训练的顶级奖励模型的性能。

------

Title: Training Language Models to Critique With Multi-agent Feedback

URL: https://doi.org/10.48550/arXiv.2410.15287

Abstract: Critique ability, a meta-cognitive capability of humans, presents significant challenges for LLMs to improve. Recent works primarily rely on supervised fine-tuning (SFT) using critiques generated by a single LLM like GPT-4. However, these model-generated critiques often exhibit flaws due to the inherent complexity of the critique. Consequently, fine-tuning LLMs on such flawed critiques typically limits the model's performance and propagates these flaws into the learned model. To overcome these challenges, this paper proposes a novel data generation pipeline, named MultiCritique, that improves the critique ability of LLMs by utilizing multi-agent feedback in both the SFT and reinforcement learning (RL) stages. First, our data generation pipeline aggregates high-quality critiques from multiple agents instead of a single model, with crucial information as input for simplifying the critique. Furthermore, our pipeline improves the preference accuracy of critique quality through multi-agent feedback, facilitating the effectiveness of RL in improving the critique ability of LLMs. Based on our proposed MultiCritique data generation pipeline, we construct the MultiCritiqueDataset for the SFT and RL fine-tuning stages. Extensive experimental results on two benchmarks demonstrate: 1) the superior quality of our constructed SFT dataset compared to existing critique datasets; 2) additional improvements to the critique ability of LLMs brought by the RL stage. Notably, our fine-tuned 7B model significantly surpasses other advanced 7B-13B open-source models, approaching the performance of advanced 70B LLMs and GPT-4. Codes, datasets and model weights will be publicly available.

中文翻译：批判能力，作为人类的元认知能力，对LLM而言是重大挑战。近期工作主要依赖监督微调（SFT），使用GPT-4等单一LLM生成的批判。然而，这些模型生成的批判由于批判本身的复杂性常常存在缺陷，因此在此类有缺陷的批判上微调LLM通常限制模型性能，并将这些缺陷传播到学习到的模型中。为克服这些挑战，本文提出MultiCritique，一种新颖的数据生成管线，在SFT和强化学习（RL）两阶段利用多Agent反馈提升LLM的批判能力。首先，我们的数据生成管线从多个Agent而非单一模型聚合高质量批判，以关键信息作为输入简化批判过程。此外，我们的管线通过多Agent反馈提高了批判质量的偏好准确率，促进了RL在提升LLM批判能力中的有效性。我们为SFT和RL微调阶段构建了MultiCritiqueDataset。在两个基准上的广泛实验表明：(1)我们构建的SFT数据集相比现有批判数据集的卓越质量；(2)RL阶段为LLM批判能力带来的额外提升。我们的微调7B模型显著超越其他先进7B-13B开源模型，接近先进70B LLM和GPT-4的性能。

------

Title: VARP: Reinforcement Learning from Vision-Language Model Feedback with Agent Regularized Preferences

URL: https://doi.org/10.48550/arXiv.2503.13817

Abstract: Designing reward functions for continuous-control robotics often leads to subtle misalignments or reward hacking, especially in complex tasks. Preference-based RL mitigates some of these pitfalls by learning rewards from comparative feedback rather than hand-crafted signals, yet scaling human annotations remains challenging. Recent work uses Vision-Language Models (VLMs) to automate preference labeling, but a single final-state image generally fails to capture the agent's full motion. In this paper, we present a two-part solution that both improves feedback accuracy and better aligns reward learning with the agent's policy. First, we overlay trajectory sketches on final observations to reveal the path taken, allowing VLMs to provide more reliable preferences-improving preference accuracy by approximately 15-20% in metaworld tasks. Second, we regularize reward learning by incorporating the agent's performance, ensuring that the reward model is optimized based on data generated by the current policy; this addition boosts episode returns by 20-30% in locomotion tasks. Empirical studies on metaworld demonstrate that our method achieves, for instance, around 70-80% success rate in all tasks, compared to below 50% for standard approaches. These results underscore the efficacy of combining richer visual representations with agent-aware reward regularization.

中文翻译：为连续控制机器人设计奖励函数常导致微妙的不对齐或奖励黑客，尤其在复杂任务中。基于偏好的RL通过学习来自比较反馈而非手工信号的奖励来缓解部分陷阱，但规模化人工标注仍具挑战。近期工作使用视觉语言模型（VLM）自动化偏好标注，但单一最终状态图像通常无法捕捉Agent的完整运动。本文中我们提出包含两部分解决方案，既提升反馈准确率又更好对齐奖励学习与Agent策略。首先，我们在最终观测上叠加轨迹草图以揭示Agent经过的路径，使VLM提供更可靠的偏好——在MetaWorld任务中提升偏好准确率约15-20%。其次，我们通过纳入Agent性能来正则化奖励学习，确保奖励模型基于当前策略生成的数据进行优化；这一增加在运动任务中将回合回报提升20-30%。在MetaWorld上的实证研究表明，我们的方法在所有任务中达到约70-80%成功率，而标准方法低于50%。

------

Title: Generative Reward Models

URL: https://doi.org/10.48550/arXiv.2410.12832

Abstract: Reinforcement Learning from Human Feedback (RLHF) has greatly improved the performance of modern Large Language Models (LLMs). The RLHF process is resource-intensive and technically challenging, generally requiring a large collection of human preference labels over model-generated outputs. Reinforcement Learning from AI Feedback (RLAIF) addresses this data collection challenge by leveraging synthetic preferences generated by an LLM. However, recent work has shown that synthetic preferences labels may not align well with human preference judgments. To address this, we propose a hybrid approach that unifies RLHF and RLAIF methodologies. We introduce GenRM, an iterative algorithm that trains an LLM on self-generated reasoning traces, leading to synthetic preference labels matching human preference judgments. Empirically, we show that zero-shot LLM-based judgments under-perform compared to Bradley-Terry reward models on in-distribution tasks (between 9-36%). In contrast, GenRM achieves in-distribution accuracy comparable to Bradley-Terry models, while significantly outperforming them on out-of-distribution tasks (between 10-45%). Moreover, GenRM surpasses the performance of using LLMs as judges on both in-distribution (by 9-31%) and out-of-distribution tasks (by 2- 6%). Our results show that combining the strengths of RLHF and RLAIF offers a promising approach for improving the quality of synthetic preference labels.

中文翻译：从人类反馈强化学习（RLHF）极大地提升了现代大语言模型（LLM）的性能。RLHF过程资源密集且技术复杂，通常需要大量人类对模型生成输出的偏好标注。从AI反馈强化学习（RLAIF）通过利用LLM生成的合成偏好来解决这一数据收集挑战。然而，近期工作表明合成偏好标签可能与人类偏好判断不一致。为应对此问题，我们提出统一RLHF和RLAIF方法论的混合方法。我们引入GenRM，一个迭代算法，在自生成推理轨迹上训练LLM，产生与人类偏好判断匹配的合成偏好标签。经验上，零样本LLM评判在分布内任务上不如Bradley-Terry奖励模型（差距9-36%）。相比之下，GenRM在分布内达到与Bradley-Terry模型可比拟的准确率，在分布外任务上则显著超越（差距10-45%）。此外，GenRM在分布内（9-31%）和分布外任务（2-6%）上均超越LLM作为评判器的性能。

------

Title: LLM Critics Help Catch LLM Bugs

URL: https://doi.org/10.48550/arXiv.2407.00215

Abstract: Reinforcement learning from human feedback (RLHF) is fundamentally limited by the capacity of humans to correctly evaluate model output. To improve human evaluation ability and overcome that limitation this work trains"critic"models that help humans to more accurately evaluate model-written code. These critics are themselves LLMs trained with RLHF to write natural language feedback highlighting problems in code from real-world assistant tasks. On code containing naturally occurring LLM errors model-written critiques are preferred over human critiques in 63% of cases, and human evaluation finds that models catch more bugs than human contractors paid for code review. We further confirm that our fine-tuned LLM critics can successfully identify hundreds of errors in ChatGPT training data rated as"flawless", even though the majority of those tasks are non-code tasks and thus out-of-distribution for the critic model. Critics can have limitations of their own, including hallucinated bugs that could mislead humans into making mistakes they might have otherwise avoided, but human-machine teams of critics and contractors catch similar numbers of bugs to LLM critics while hallucinating less than LLMs alone.

中文翻译：从人类反馈强化学习（RLHF）从根本上受限于人类正确评估模型输出的能力。为提升人类评估能力并克服这一局限，本文训练critic模型来帮助人类更准确地评估模型编写的代码。这些critic本身是通过RLHF训练的LLM，用于撰写自然语言反馈，突出真实世界助手任务中代码的问题。在包含自然发生的LLM错误的代码上，模型撰写的批判在63%的情况下优于人类批判，人类评估发现模型比受薪进行代码审查的人类承包商捕捉到更多错误。我们进一步确认我们微调的LLM批判器能够成功识别ChatGPT训练数据中被评为完美的数百个错误，即使这些任务大多是非代码任务。批判器可能自身也存在局限，包括幻觉错误可能误导人类，但人类-机器批判团队与LLM批判器捕捉相似数量的错误，同时比单独使用LLM产生更少幻觉。

------

Title: Recursive Introspection: Teaching Language Model Agents How to Self-Improve

URL: https://doi.org/10.52202/079017-1754

Abstract:

中文翻译：（摘要为空）

------

Title: Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision

URL: https://doi.org/10.48550/arXiv.2505.20415

Abstract: Large language models (LLMs) have shown strong performance in many reasoning benchmarks. However, recent studies have pointed to memorization, rather than generalization, as one of the leading causes for such performance. LLMs, in fact, are susceptible to content variations, demonstrating a lack of robust planning or symbolic abstractions supporting their reasoning process. To improve reliability, many attempts have been made to combine LLMs with symbolic methods. Nevertheless, existing approaches fail to effectively leverage symbolic representations due to the challenges involved in developing reliable and scalable verification mechanisms. In this paper, we propose to overcome such limitations by synthesizing high-quality symbolic reasoning trajectories with stepwise pseudo-labels at scale via Monte Carlo estimation. A Process Reward Model (PRM) can be efficiently trained based on the synthesized data and then used to select more symbolic trajectories. The trajectories are then employed with Direct Preference Optimization (DPO) and Supervised Fine-Tuning (SFT) to improve logical reasoning and generalization. Our results on benchmarks (i.e., FOLIO and LogicAsker) show the effectiveness of the proposed method with gains on frontier and open-weight models. Moreover, additional experiments on claim verification data reveal that fine-tuning on the generated symbolic reasoning trajectories enhances out-of-domain generalizability, suggesting the potential impact of the proposed method in enhancing planning and logical reasoning.

中文翻译：大语言模型（LLM）在许多推理基准上展现了强性能。然而，近期研究指出记忆而非泛化是此类性能的主要原因之一。事实上LLM容易受到内容变化的影响，展示出缺乏支撑其推理过程的鲁棒规划或符号抽象。为提升可靠性，许多尝试将LLM与符号方法结合。然而，由于开发可靠且可扩展的验证机制所涉及的挑战，现有方法未能有效利用符号表示。本文中我们提出通过蒙特卡洛估计以规模化合成具有逐步伪标签的高质量符号推理轨迹来克服这些局限。过程奖励模型（PRM）可以基于合成数据高效训练，随后用于选择更多符号轨迹。然后这些轨迹与直接偏好优化（DPO）和监督微调（SFT）一起使用，以改进逻辑推理和泛化。我们在FOLIO和LogicAsker基准上的结果展示了所提方法的有效性，在前沿和开源模型上均取得收益。在声明验证数据上的额外实验表明微调增强了域外泛化能力。

------

Title: RM -RF: Reward Model for Run-Free Unit Test Evaluation

URL: https://doi.org/10.48550/arXiv.2601.13097

Abstract: We present RM-RF, a lightweight reward model for run-free evaluation of automatically generated unit tests. Instead of repeatedly compiling and executing candidate tests, RM-RF predicts - from source and test code alone - three execution-derived signals: (1) whether the augmented test suite compiles and runs successfully, (2) whether the generated test cases increase code coverage, and (3) whether the generated test cases improve the mutation kill rate. To train and evaluate RM-RF we assemble a multilingual dataset (Java, Python, Go) of focal files, test files, and candidate test additions labeled by an execution-based pipeline, and we release an associated dataset and methodology for comparative evaluation. We tested multiple model families and tuning regimes (zero-shot, full fine-tuning, and PEFT via LoRA), achieving an average F1 of 0.69 across the three targets. Compared to conventional compile-and-run instruments, RM-RF provides substantially lower latency and infrastructure cost while delivering competitive predictive fidelity, enabling fast, scalable feedback for large-scale test generation and RL-based code optimization.

中文翻译：我们提出RM-RF，一个用于无需运行的自动生成单元测试评估的轻量级奖励模型。RM-RF不重复编译和执行候选测试，而是仅从源代码和测试代码预测三个执行衍生信号：(1)增强的测试套件是否成功编译和运行；(2)生成的测试用例是否增加了代码覆盖率；(3)生成的测试用例是否提高了变异杀死率。为训练和评估RM-RF，我们组装了一个多语言数据集（Java、Python、Go），包含焦点文件、测试文件和候选测试新增，由基于执行的管线标注。我们测试了多种模型家族和调优方案（零样本、全微调和通过LoRA的PEFT），在三个目标上达到平均F1 0.69。与传统编译运行工具相比，RM-RF提供显著更低的延迟和基础设施成本，同时提供有竞争力的预测保真度，为大规模测试生成和基于RL的代码优化提供了快速、可扩展的反馈。

------

Title: I-FailSense: Towards General Robotic Failure Detection with Vision-Language Models

URL: https://doi.org/10.48550/arXiv.2509.16072

Abstract: Language-conditioned robotic manipulation in open-world settings requires not only accurate task execution but also the ability to detect failures for robust deployment in real-world environments. Although recent advances in vision-language models (VLMs) have significantly improved the spatial reasoning and task-planning capabilities of robots, they remain limited in their ability to recognize their own failures. In particular, a critical yet underexplored challenge lies in detecting semantic misalignment errors, where the robot executes a task that is semantically meaningful but inconsistent with the given instruction. To address this, we propose a method for building datasets targeting Semantic Misalignment Failures detection, from existing language-conditioned manipulation datasets. We also present I-FailSense, an open-source VLM framework with grounded arbitration designed specifically for failure detection. Our approach relies on post-training a base VLM, followed by training lightweight classification heads, called FS blocks, attached to different internal layers of the VLM and whose predictions are aggregated using an ensembling mechanism. Experiments show that I-FailSense outperforms state-of-the-art VLMs, both comparable in size and larger, in detecting semantic misalignment errors. Notably, despite being trained only on semantic misalignment detection, I-FailSense generalizes to broader robotic failure categories and effectively transfers to other simulation environments and real-world with zero-shot or minimal post-training. The datasets and models are publicly released on HuggingFace (Webpage: https://clemgris.github.io/I-FailSense/).

中文翻译：开放世界中的语言条件机器人操作不仅需要精确的任务执行，还需要在真实环境中检测失败以实现鲁棒部署。尽管视觉语言模型（VLM）的最新进展显著提升了机器人的空间推理和任务规划能力，但它们在识别自身失败方面仍然有限。特别是，一个关键但未充分探索的挑战在于检测语义不对齐错误，即机器人执行了语义上有意义但与给定指令不一致的任务。为解决此问题，我们提出一种从现有语言条件操作数据集构建针对语义不对齐失败检测数据集的方法。我们还提出I-FailSense，一个开源VLM框架，具有接地仲裁机制，专为失败检测设计。我们的方法基于对基础VLM进行后训练，然后在VLM不同内部层上训练轻量级分类头（称为FS块），其预测通过集成机制聚合。实验表明I-FailSense在检测语义不对齐错误方面超越最先进的VLM。尽管仅在语义不对齐检测上训练，I-FailSense泛化到更广泛的机器人失败类别，并以零样本或最小后训练有效迁移到其他仿真环境和真实世界。

------

Title: Training Turn-by-Turn Verifiers for Dialogue Tutoring Agents: The Curious Case of LLMs as Your Coding Tutors

URL: https://doi.org/10.48550/arXiv.2502.13311

Abstract: Intelligent tutoring agents powered by large language models (LLMs) have been increasingly explored to deliver personalized knowledge in areas such as language learning and science education. However, their capabilities in guiding users to solve complex real-world tasks remain underexplored. To address this limitation, in this work, we focus on coding tutoring, a challenging problem that requires tutors to proactively guide students towards completing predefined coding tasks. We propose a novel agent workflow, Trace-and-Verify (TRAVER), which combines knowledge tracing to estimate a student's knowledge state and turn-by-turn verification to ensure effective guidance toward task completion. We introduce DICT, an automatic evaluation protocol that assesses tutor agents using controlled student simulation and code generation tests. Extensive experiments reveal the challenges of coding tutoring and demonstrate that TRAVER achieves a significantly higher success rate. Although we use code tutoring as an example in this paper, our approach can be extended beyond coding, providing valuable insights into advancing tutoring agents for human task learning.

中文翻译：由大语言模型（LLM）驱动的智能辅导Agent在语言学习和科学教育等领域被越来越多地探索以提供个性化知识传递。然而，它们在引导用户解决复杂真实世界任务方面的能力仍未被充分探索。为解决这一局限，本文中我们聚焦编程辅导，一个需要辅导者主动引导学生完成预定义编程任务的挑战性问题。我们提出一种新颖的Agent工作流Trace-and-Verify（TRAVER），结合知识追踪以估计学生的知识状态和逐轮验证以确保朝向任务完成的有效引导。我们引入DICT，一个使用受控学生仿真和代码生成测试评估辅导Agent的自动评估协议。广泛实验揭示了编程辅导的挑战，并证明TRAVER取得显著更高的成功率。虽然本文以代码辅导为例，我们的方法可扩展到编程之外，为推进面向人类任务学习的辅导Agent提供宝贵见解。

------

Title: Joint Verification and Refinement of Language Models for Safety-Constrained Planning

URL: https://doi.org/10.48550/arXiv.2410.14865

Abstract: Large language models possess impressive capabilities in generating programs (e.g., Python) from natural language descriptions to execute robotic tasks. However, these generated programs often contain errors that violate externally given task specifications. Without an effective method to verify their correctness, the reliable deployment of language models in real-world systems is practically infeasible. We develop a method that converts generated robot programs into an automaton-based representation and verifies them against task-relevant safety specifications. We establish a theorem that any arbitrary combination of the verified programs will also satisfy the safety specifications. Hence, the method eliminates the need to verify complex programs composed of multiple simpler ones, reducing computation complexity. We then introduce an automated fine-tuning procedure that leverages verification outcomes for supervision. By applying the theorem, this procedure only requires training the model to generate safe sub-components, thereby improving training efficiency. Empirical results on robot applications show a 30 percent increase in the probability of generating specification-compliant programs, with training time reduced by half compared to fine-tuning on generating full programs.

中文翻译：大语言模型拥有从自然语言描述生成程序（如Python）来执行机器人任务的卓越能力。然而，这些生成的程序经常包含违反外部给定任务规范的错误。没有有效的方法验证其正确性，语言模型在真实世界系统中的可靠部署几乎不可行。我们开发了一种方法，将生成的机器人程序转换为基于自动机的表示，并针对任务相关的安全规范进行验证。我们建立了一个定理：验证过的程序的任意组合也将满足安全规范。因此，该方法消除了验证由多个简单程序组成的复杂程序的需要，降低了计算复杂度。我们随后引入一个自动微调过程，利用验证结果作为监督。通过应用该定理，此过程只需训练模型生成安全的子组件，从而提高训练效率。机器人应用上的实证结果显示生成规范兼容程序的概率提升30%，训练时间相比微调生成完整程序减少一半。

------

Title: Tool Verification for Test-Time Reinforcement Learning

URL: https://www.semanticscholar.org/paper/c856c2bc3ef2299f76c191750b45617d8215bf02

Abstract: Test-time reinforcement learning (TTRL) has emerged as a promising paradigm for self-evolving large reasoning models (LRMs), enabling online adaptation on unlabeled test inputs via self-induced rewards through majority voting. However, a spurious yet high-frequency unverified consensus can become a biased and reinforced reward signal, leading to incorrect mode collapse. We address this failure mode with T^3RL (Tool-Verification for Test-Time Reinforcement Learning), which introduces test-time tool verification into reward estimation. Concretely, a verifier uses an external tool as evidence (e.g., from code execution) to upweight verified rollouts in a verification-aware voting, producing more reliable pseudo-labels for training. Across various math difficulties (MATH-500, AMC, and AIME 2024) and diverse backbone types, T^3RL significantly improves over TTRL, with larger gains on harder problems. More broadly, T^3RL can be viewed as verified online data synthesis, highlighting test-time tool verification as a key mechanism for stabilizing self-evolution.

中文翻译：测试时强化学习（TTRL）已成为自我进化大推理模型（LRM）的有前景范式，通过多数投票的自诱导奖励实现在未标注测试输入上的在线适应。然而，一个虚假但高频的未经验证共识可能成为有偏且被强化的奖励信号，导致错误模式坍缩。我们通过T^3RL（Tool-Verification for Test-Time Reinforcement Learning）来解决这一失败模式，将测试时工具验证引入奖励估计。具体而言，验证器使用外部工具作为证据（如代码执行）在验证感知的投票中加权验证过的rollout，为训练产生更可靠的伪标签。在涵盖不同数学难度（MATH-500、AMC和AIME 2024）和多样化骨干类型的实验中，T^3RL显著优于TTRL，在更难问题上增益更大。更广泛地，T^3RL可被视为验证的在线数据合成，凸显了测试时工具验证作为稳定自我进化关键机制的重要性。

------

Title: P-Check: Advancing Personalized Reward Model via Learning to Generate Dynamic Checklist

URL: https://doi.org/10.48550/arXiv.2601.02986

Abstract: Recent approaches in personalized reward modeling have primarily focused on leveraging user interaction history to align model judgments with individual preferences. However, existing approaches largely treat user context as a static or implicit conditioning signal, failing to capture the dynamic and multi-faceted nature of human judgment. In this paper, we propose P-Check, a novel personalized reward modeling framework, designed to train a plug-and-play checklist generator that synthesizes dynamic evaluation criteria for guiding the reward prediction. To better align these checklists with personalized nuances, we introduce Preference-Contrastive Criterion Weighting, a training strategy that assigns saliency scores to criteria based on their discriminative power for personalized judgment. We conduct extensive experiments and demonstrate that P-Check not only improves reward accuracy but also enhances downstream personalized generation, and remains robust in OOD scenarios.

中文翻译：个性化奖励建模的近期方法主要聚焦于利用用户交互历史使模型判断与个体偏好对齐。然而，现有方法很大程度上将用户上下文视为静态或隐式条件信号，未能捕捉人类判断的动态和多面性。本文中我们提出P-Check，一种新颖的个性化奖励建模框架，训练一个即插即用的检查清单生成器，合成动态评估标准以指导奖励预测。为使这些检查清单更好地与个性化细微差异对齐，我们引入偏好对比标准加权，一种基于标准对个性化判断的判别力分配显著分数的训练策略。我们进行了广泛实验，证明P-Check不仅提升了奖励准确率，还改善了后续个性化生成，并在OOD场景中保持鲁棒。

------

Title: JudgeLRM: Large Reasoning Models as a Judge

URL: https://doi.org/10.48550/arXiv.2504.00050

Abstract: Large Language Models (LLMs) are increasingly adopted as evaluators, offering a scalable alternative to human annotation. However, existing supervised fine-tuning (SFT) approaches often fall short in domains that demand complex reasoning. Judgment is inherently reasoning-intensive: beyond surface-level scoring, it requires verifying evidence, identifying errors, and justifying decisions. Through the analysis of evaluation tasks, we find a negative correlation between SFT performance gains and the proportion of reasoning-demanding samples, revealing the limits of SFT in such scenarios. To address this, we introduce JudgeLRM, a family of judgment-oriented LLMs, trained using reinforcement learning (RL) with judge-wise, outcome-driven rewards to activate reasoning capabilities. JudgeLRM consistently outperform SFT-tuned baselines in the same size, as well as other RL and SFT variants, and even surpass state-of-the-art reasoning models: notably, JudgeLRM-3B/4B exceeds GPT-4, while JudgeLRM-7B/8B/14B outperforms DeepSeek-R1 by over 2% in F1 score, with particularly strong gains on reasoning-heavy tasks. Our findings underscore the value of RL in unlocking reasoning-aligned LLM judges.

中文翻译：大语言模型（LLM）越来越多地被用作评估器，提供了人类标注的可扩展替代方案。然而，现有监督微调（SFT）方法在需要复杂推理的领域中常常表现不佳。判断本质上是推理密集型任务：超越表面评分，它需要验证证据、识别错误并论证决策。通过对评估任务的分析，我们发现SFT性能增益与需要推理的样本比例呈负相关，揭示了SFT在此类场景中的局限。为应对此问题，我们引入JudgeLRM，一系列面向判断的LLM，使用强化学习（RL）以评判导向、结果驱动的奖励来激活推理能力。JudgeLRM始终优于同规模的SFT基线以及其他RL和SFT变体，甚至超越最先进的推理模型：JudgeLRM-3B/4B超越GPT-4，JudgeLRM-7B/8B/14B在F1分数上超越DeepSeek-R1超过2%，在推理密集型任务上增益尤为显著。

------

Title: Asymmetric Actor-Critic for Multi-turn LLM Agents

URL: https://www.semanticscholar.org/paper/96897d2f30bb852a7988fc68bd7279374f72d26c

Abstract: Large language models (LLMs) exhibit strong reasoning and conversational abilities, but ensuring reliable behavior in multi-turn interactions remains challenging. In many real-world applications, agents must succeed in one-shot settings where retries are impossible. Existing approaches either rely on reflection or post-hoc evaluation, which require additional attempts, or assume fully trainable models that cannot leverage proprietary LLMs. We propose an asymmetric actor-critic framework for reliable conversational agents. A powerful proprietary LLM acts as the actor, while a smaller open-source critic provides runtime supervision, monitoring the actor's actions and intervening within the same interaction trajectory. Unlike training-based actor-critic methods, our framework supervises a fixed actor operating in open-ended conversational environments. The design leverages a generation-verification asymmetry: while high-quality generation requires large models, effective oversight can often be achieved by smaller ones. We further introduce a data generation pipeline that produces supervision signals for critic fine-tuning without modifying the actor. Experiments on $\tau$-bench and UserBench show that our approach significantly improves reliability and task success over strong single-agent baselines. Moreover, lightweight open-source critics rival or surpass larger proprietary models in the critic role, and critic fine-tuning yields additional gains over several state-of-the-art methods.

中文翻译：大语言模型（LLM）展现了强推理和对话能力，但在多轮交互中确保可靠行为仍具挑战。在许多真实世界应用中，Agent必须在无法重试的单次尝试设置中成功。现有方法要么依赖需要额外尝试的反思或事后评估，要么假设模型完全可训练而无法利用商业LLM。我们提出针对可靠对话Agent的非对称Actor-Critic框架。强大的商业LLM充当Actor，较小的开源Critic提供运行时监督，监控Actor的动作并在同一交互轨迹内进行干预。与基于训练的Actor-Critic方法不同，我们的框架监督在开放对话环境中运行的固定Actor。该设计利用了生成-验证的不对称性：高质量生成需要大型模型，而有效监督通常可由较小模型实现。我们进一步引入数据生成管线，在不修改Actor的情况下为Critic微调生成监督信号。在tau-bench和UserBench上的实验表明，我们的方法相比强单Agent基线显著提升了可靠性和任务成功率。轻量级开源Critic在Critic角色中匹配或超越更大的商业模型。

------

Title: Hybrid Reward Normalization for Process-supervised Non-verifiable Agentic Tasks

URL: https://doi.org/10.48550/arXiv.2509.25598

Abstract: Large Language Models (LLMs) increasingly rely on external tools such as search engines to solve complex agentic tasks that require reasoning and external knowledge retrieval. Recently, reinforcement learning with verifiable rewards (RLVR) has demonstrated its effectiveness in advancing capabilities of LLMs by rewarding the final answers via outcome rewards. While straightforward to supervise, outcome rewards only provide sparse signals and delayed feedback, which limits their effectiveness on long trajectories. Process rewards address this by evaluating intermediate steps, providing fine-grained supervision and encouraging grounded problem solving. However, it is notoriously hard to annotate step-wise labels, especially in non-verifiable process without"golden"answers. Furthermore, step-wise judgment requires the balance between local quality with contribution to the final outcome, as optimizing towards higher process reward may not always align with better final outcomes. To address the above challenges, we introduce Principle Process Reward (PPR), an RL approach that unifies principled step-level assessment and outcome verification. We train a principle-based reward model to improve the transparency and reliability of process evaluation, and further introduce a Reward Normalization (ReNorm) strategy to calibrate outcome and process rewards. Experiment results show that PPR achieves state-of-the-art performance across a wide range of benchmarks, demonstrating its impressive robustness and generalization. Our code and model collection is available in this link.

中文翻译：大语言模型（LLM）越来越依赖搜索引擎等外部工具来解决需要推理和外部知识检索的复杂Agent任务。最近，使用可验证奖励的强化学习（RLVR）通过结果奖励对最终答案进行奖励，证明了在推进LLM能力方面的有效性。虽然结果奖励监督直接，但仅提供稀疏信号和延迟反馈，限制了其在长轨迹上的有效性。过程奖励通过评估中间步骤来解决这一问题，提供细粒度监督并鼓励有根基的问题求解。然而，标注步骤级标签极其困难，尤其是在没有黄金标准答案的不可验证过程中。此外，步骤级判断需要在局部质量与对最终结果的贡献之间平衡。为解决上述挑战，我们引入Principle Process Reward（PPR），一个将原则化步骤级评估与结果验证统一的RL方法。我们训练基于原则的奖励模型来提升过程评估的透明度和可靠性，并进一步引入Reward Normalization（ReNorm）策略来校准结果奖励和过程奖励。实验结果表明PPR在广泛基准上取得最优性能，展示了令人印象深刻的鲁棒性和泛化能力。

------

Title: Self-critiquing models for assisting human evaluators

URL: https://doi.org/10.48550/arXiv.2206.05802

Abstract: We fine-tune large language models to write natural language critiques (natural language critical comments) using behavioral cloning. On a topic-based summarization task, critiques written by our models help humans find flaws in summaries that they would have otherwise missed. Our models help find naturally occurring flaws in both model and human written summaries, and intentional flaws in summaries written by humans to be deliberately misleading. We study scaling properties of critiquing with both topic-based summarization and synthetic tasks. Larger models write more helpful critiques, and on most tasks, are better at self-critiquing, despite having harder-to-critique outputs. Larger models can also integrate their own selfcritiques as feedback, refining their own summaries into better ones. Finally, we motivate and introduce a framework for comparing critiquing ability to generation and discrimination ability. Our measurements suggest that even large models may still have relevant knowledge they cannot or do not articulate as critiques. These results are a proof of concept for using AI-assisted human feedback to scale the supervision of machine learning systems to tasks that are difficult for humans to evaluate directly. We release our training datasets, as well as samples from our critique assistance experiments.

中文翻译：我们使用行为克隆微调大语言模型来撰写自然语言批判。在基于主题的摘要任务上，我们的模型撰写的批判帮助人类发现他们原本会错过的摘要缺陷。我们的模型帮助发现模型和人类撰写摘要中的自然缺陷，以及人类为故意误导而撰写的摘要中的蓄意缺陷。我们研究了基于主题摘要和合成任务上批判能力的扩展性质。更大的模型撰写更有帮助的批判，且在大多数任务上，尽管其输出更难批判，自我批判能力仍更强。更大的模型还能将其自我批判整合为反馈，将自己的摘要精炼为更好的版本。最后，我们提出并引入一个比较批判能力、生成能力和判别能力的框架。我们的测量结果表明，即使大模型可能仍具有它们不能或未以批判形式表达的相关知识。这些结果证明了使用AI辅助人类反馈来将机器学习系统监督扩展到人类难以直接评估的任务的概念验证。

------

Title: VLP: Vision-Language Preference Learning for Embodied Manipulation

URL: https://doi.org/10.48550/arXiv.2502.11918

Abstract: Reward engineering is one of the key challenges in Reinforcement Learning (RL). Preference-based RL effectively addresses this issue by learning from human feedback. However, it is both time-consuming and expensive to collect human preference labels. In this paper, we propose a novel \textbf{V}ision-\textbf{L}anguage \textbf{P}reference learning framework, named \textbf{VLP}, which learns a vision-language preference model to provide preference feedback for embodied manipulation tasks. To achieve this, we define three types of language-conditioned preferences and construct a vision-language preference dataset, which contains versatile implicit preference orders without human annotations. The preference model learns to extract language-related features, and then serves as a preference annotator in various downstream tasks. The policy can be learned according to the annotated preferences via reward learning or direct policy optimization. Extensive empirical results on simulated embodied manipulation tasks demonstrate that our method provides accurate preferences and generalizes to unseen tasks and unseen language instructions, outperforming the baselines by a large margin.

中文翻译：奖励工程是强化学习（RL）的关键挑战之一。基于偏好的RL通过学习人类反馈有效解决了这一问题。然而，收集人类偏好标签既耗时又昂贵。本文中我们提出一种新颖的VLP（Vision-Language Preference learning）框架，学习视觉语言偏好模型为具身操作任务提供偏好反馈。为实现这一目标，我们定义了三类语言条件偏好并构建了视觉语言偏好数据集，包含无需人工标注的通用隐式偏好排序。偏好模型学习提取语言相关特征，随后在各种下游任务中充当偏好标注器。策略可以根据标注的偏好通过奖励学习或直接策略优化来学习。在仿真具身操作任务上的大量实证结果表明，我们的方法提供准确的偏好并泛化到未见任务和未见语言指令，大幅超越基线。

------

Title: Real-Time Verification of Embodied Reasoning for Generative Skill Acquisition

URL: https://doi.org/10.48550/arXiv.2505.11175

Abstract: Generative skill acquisition enables embodied agents to actively learn a scalable and evolving repertoire of control skills, crucial for the advancement of large decision models. While prior approaches often rely on supervision signals from generalist agents (e.g., LLMs), their effectiveness in complex 3D environments remains unclear; exhaustive evaluation incurs substantial computational costs, significantly hindering the efficiency of skill learning. Inspired by recent successes in verification models for mathematical reasoning, we propose VERGSA (Verifying Embodied Reasoning in Generative Skill Acquisition), a framework that systematically integrates real-time verification principles into embodied skill learning. VERGSA establishes 1) a seamless extension from verification of mathematical reasoning into embodied learning by dynamically incorporating contextually relevant tasks into prompts and defining success metrics for both subtasks and overall tasks, and 2) an automated, scalable reward labeling scheme that synthesizes dense reward signals by iteratively finalizing the contribution of scene configuration and subtask learning to overall skill acquisition. To the best of our knowledge, this approach constitutes the first comprehensive training dataset for verification-driven generative skill acquisition, eliminating arduous manual reward engineering. Experiments validate the efficacy of our approach: 1) the exemplar task pool improves the average task success rates by 21%, 2) our verification model boosts success rates by 24% for novel tasks and 36% for encountered tasks, and 3) outperforms LLM-as-a-Judge baselines in verification quality.

中文翻译：生成式技能获取使具身Agent能够主动学习可扩展且不断进化的控制技能库，对大决策模型的发展至关重要。尽管先前方法通常依赖通用Agent（如LLM）的监督信号，但它们在复杂3D环境中的有效性仍不确定；穷尽评估产生巨大的计算成本，显著阻碍技能学习效率。受数学推理验证模型近期成功的启发，我们提出VERGSA（Verifying Embodied Reasoning in Generative Skill Acquisition），一个将实时验证原则系统集成到具身技能学习中的框架。VERGSA建立了：(1)从数学推理验证到具身学习的无缝扩展，通过动态将上下文相关任务纳入提示并定义子任务和整体任务的成功指标；(2)自动化可扩展的奖励标注方案，通过迭代确定场景配置和子任务学习对整体技能获取的贡献来合成密集奖励信号。实验验证了我们方法的有效性：(1)示例任务池将平均任务成功率提升21%，(2)我们的验证模型将新任务成功率提升24%，遇到的任务提升36%，(3)在验证质量上超越LLM-as-a-Judge基线。

------

Title: RL4F: Generating Natural Language Feedback with Reinforcement Learning for Repairing Model Outputs

URL: https://doi.org/10.48550/arXiv.2305.08844

Abstract: Despite their unprecedented success, even the largest language models make mistakes.Similar to how humans learn and improve using feedback, previous work proposed providing language models with natural language feedback to guide them in repairing their outputs. Because human-generated critiques are expensive to obtain, researchers have devised learned critique generators in lieu of human critics while assuming one can train downstream models to utilize generated feedback. However, this approach does not apply to black-box or limited access models such as ChatGPT, as they cannot be fine-tuned. Moreover, in the era of large general-purpose language agents, fine-tuning is neither computationally nor spatially efficient as it results in multiple copies of the network. In this work, we introduce RL4F (Reinforcement Learning for Feedback), a multi-agent collaborative framework where the critique generator is trained to maximize end-task performance of GPT-3, a fixed model more than 200 times its size. RL4F produces critiques that help GPT-3 revise its outputs. We study three datasets for action planning, summarization and alphabetization and show relative improvements up to 10% in multiple text similarity metrics over other learned, retrieval-augmented or prompting-based critique generators.

中文翻译：尽管取得了前所未有的成功，即使最大的语言模型也会犯错。与人类使用反馈学习和改进类似，先前工作提出为语言模型提供自然语言反馈以引导其修复输出。由于人类生成的批判获取成本高昂，研究人员设计了学习到的批判生成器来替代人类批判者，同时假设可以训练下游模型利用生成的反馈。然而，该方法不适用于黑盒或有限访问模型（如ChatGPT），因为它们无法被微调。此外，在大型通用语言Agent时代，微调在计算和空间上都不高效，因为会产生网络的多个副本。本文中我们引入RL4F（Reinforcement Learning for Feedback），一个多Agent协作框架，其中批判生成器被训练为最大化GPT-3（一个体积超过它200倍的固定模型）的最终任务性能。RL4F产生帮助GPT-3修订其输出的批判。我们研究了三个数据集（动作规划、摘要和字母排序），在多个文本相似度指标上相对其他学习、检索增强或基于提示的批判生成器展现了高达10%的相对提升。

------

Title: Learning LLM-as-a-Judge for Preference Alignment

URL: https://www.semanticscholar.org/paper/a5315e5e87354a2320ebb134b92306e71e9a7dda

Abstract:

中文翻译：（摘要为空）

------

Title: LLaVA-Critic-R1: Your Critic Model is Secretly a Strong Policy Model

URL: https://doi.org/10.48550/arXiv.2509.00676

Abstract: In vision-language modeling, critic models are typically trained to evaluate outputs -- assigning scalar scores or pairwise preferences -- rather than to generate responses. This separation from policy models, which produce the responses, is so entrenched that critics are rarely considered for direct policy use. In this work, we challenge this convention. We propose to reorganize preference-labeled critic datasets into verifiable training signals and perform reinforcement learning directly on a base generative model, producing LLaVA-Critic-R1, a multimodal critic trained to optimize preference judgments while retaining full generation ability. Surprisingly, LLaVA-Critic-R1 emerges not only as a top-performing critic but also as a competitive policy model -- matching or surpassing specialized reasoning VLMs trained with in-domain data across 26 visual reasoning and understanding benchmarks, with an average gain of +5.7% over its base model (Qwen-2.5-VL-7B). Extending this approach to existing strong reasoning VLMs yields LLaVA-Critic-R1+, which further advances policy performance without sacrificing critic quality, achieving a SoTA performance of 71.9 on MMMU at the 7B scale. Finally, we show that the enhanced critic ability benefits inference: applying self-critique at test time yields an average +13.8% improvement on five representative reasoning tasks without additional training. Our results reveal that RL training on critic data can produce a unified model excelling at both evaluation and generation, offering a simple path toward scalable, self-improving multimodal systems.

中文翻译：在视觉语言建模中，批判模型通常被训练为评估输出——分配标量分数或成对偏好——而非生成响应。这种与生成响应的策略模型的分离根深蒂固，以至于批判模型很少被考虑直接用作策略。本文中我们挑战这一惯例。我们提出将偏好标注的批判数据集重组为可验证训练信号，直接在基座生成模型上执行强化学习，产生LLaVA-Critic-R1，一个被训练为优化偏好判断同时保留完整生成能力的多模态批判模型。令人惊讶的是，LLaVA-Critic-R1不仅成为顶级批判模型，还成为有竞争力的策略模型——在26个视觉推理和理解基准上匹敌或超越使用域内数据训练的专用推理VLM，相比基座模型（Qwen-2.5-VL-7B）平均提升+5.7%。将这一方法扩展到现有强推理VLM产生LLaVA-Critic-R1+，进一步提升了策略性能而不牺牲批判质量，在7B规模上达到71.9 MMMU的最优性能。最后我们展示了增强的批判能力有益于推理：测试时应用自我批判在五个代表性推理任务上带来平均+13.8%的提升，无需额外训练。

------

Title: HyperClick: Advancing Reliable GUI Grounding via Uncertainty Calibration

URL: https://doi.org/10.48550/arXiv.2510.27266

Abstract: Autonomous Graphical User Interface (GUI) agents rely on accurate GUI grounding, which maps language instructions to on-screen coordinates, to execute user commands. However, current models, whether trained via supervised fine-tuning (SFT) or reinforcement fine-tuning (RFT), lack self-awareness of their capability boundaries, leading to overconfidence and unreliable predictions. We first systematically evaluate probabilistic and verbalized confidence in general and GUI-specific models, revealing a misalignment between confidence and actual accuracy, which is particularly critical in dynamic GUI automation tasks, where single errors can cause task failure. To address this, we propose HyperClick, a novel framework that enhances reliable GUI grounding through uncertainty calibration. HyperClick introduces a dual reward mechanism, combining a binary reward for correct actions with a truncated Gaussian-based spatial confidence modeling, calibrated using the Brier score. This approach jointly optimizes grounding accuracy and confidence reliability, fostering introspective self-criticism. Extensive experiments on seven challenge benchmarks show that HyperClick achieves state-of-the-art performance while providing well-calibrated confidence. By enabling explicit confidence calibration and introspective self-criticism, HyperClick reduces overconfidence and supports more reliable GUI automation.

中文翻译：自主GUI Agent依赖准确的GUI锚定（将语言指令映射到屏幕坐标）来执行用户命令。然而，当前模型无论是通过监督微调（SFT）还是强化微调（RFT）训练，都缺乏对其能力边界的自我意识，导致过度自信和不可靠预测。我们首先系统评估了通用和GUI专用模型中的概率置信度和语言化置信度，揭示了置信度与实际准确率之间的错位，这在动态GUI自动化任务中尤为关键。为解决此问题，我们提出HyperClick，一个通过不确定性校准增强可靠GUI锚定的新框架。HyperClick引入双重奖励机制，将正确动作的二值奖励与基于截断高斯分布的空间置信度建模（使用Brier分数校准）相结合。该方法联合优化锚定准确率和置信度可靠性，培养内省式自我批判。在七个挑战基准上的大量实验表明HyperClick在提供校准良好的置信度的同时达到最优性能。

------

Title: Tapered Off-Policy REINFORCE: Stable and efficient reinforcement learning for LLMs

URL: https://doi.org/10.48550/arXiv.2503.14286

Abstract: We propose a new algorithm for fine-tuning large language models using reinforcement learning. Tapered Off-Policy REINFORCE (TOPR) uses an asymmetric, tapered variant of importance sampling to speed up learning while maintaining stable learning dynamics, even without the use of KL regularization. TOPR can be applied in a fully offline fashion, allows the handling of positive and negative examples in a unified framework, and benefits from the implementational simplicity that is typical of Monte Carlo algorithms. We demonstrate the effectiveness of our approach with a series of experiments on the GSM8K and MATH reasoning benchmarks, finding performance gains for training both a model for solution generation and as a generative verifier. We show that properly leveraging positive and negative examples alike in the off-policy regime simultaneously increases test-time accuracy and training data efficiency, all the while avoiding the ``wasted inference'' that comes with discarding negative examples. We find that this advantage persists over multiple iterations of training and can be amplified by dataset curation techniques, enabling us to match 70B-parameter model performance with 8B language models. As a corollary to this work, we find that REINFORCE's baseline parameter plays an important and unexpected role in defining dataset composition in the presence of negative examples, and is consequently critical in driving off-policy performance.

中文翻译：我们提出一种使用强化学习微调大语言模型的新算法。Tapered Off-Policy REINFORCE（TOPR）使用非对称、渐变的重要性采样变体，加速学习同时保持稳定的学习动态，即使不使用KL正则化。TOPR可以完全离线方式应用，允许在统一框架中处理正例和负例，并享有蒙特卡洛算法典型的实现简单性。我们通过在GSM8K和MATH推理基准上的一系列实验证明了方法的有效性，发现训练解答生成模型和生成式验证器均获得性能增益。我们证明在离线策略机制中同时适当地利用正例和负例能同时提高测试时准确率和训练数据效率，同时避免丢弃负例带来的浪费推理。我们发现这一优势在多个训练迭代中持续存在，并可通过数据集整理技术放大，使我们能够用8B语言模型匹敌70B参数模型性能。REINFORCE的基线参数在定义数据集构成方面扮演重要且意外关键的角色。

------

Title: SafePred: A Predictive Guardrail for Computer-Using Agents via World Models

URL: https://doi.org/10.48550/arXiv.2602.01725

Abstract: With the widespread deployment of Computer-using Agents (CUAs) in complex real-world environments, prevalent long-term risks often lead to severe and irreversible consequences. Most existing guardrails for CUAs adopt a reactive approach, constraining agent behavior only within the current observation space. While these guardrails can prevent immediate short-term risks (e.g., clicking on a phishing link), they cannot proactively avoid long-term risks: seemingly reasonable actions can lead to high-risk consequences that emerge with a delay (e.g., cleaning logs leads to future audits being untraceable), which reactive guardrails cannot identify within the current observation space. To address these limitations, we propose a predictive guardrail approach, with the core idea of aligning predicted future risks with current decisions. Based on this approach, we present SafePred, a predictive guardrail framework for CUAs that establishes a risk-to-decision loop to ensure safe agent behavior. SafePred supports two key abilities: (1) Short- and long-term risk prediction: by using safety policies as the basis for risk prediction, SafePred leverages the prediction capability of the world model to generate semantic representations of both short-term and long-term risks, thereby identifying and pruning actions that lead to high-risk states; (2) Decision optimization: translating predicted risks into actionable safe decision guidances through step-level interventions and task-level re-planning. Extensive experiments show that SafePred significantly reduces high-risk behaviors, achieving over 97.6% safety performance and improving task utility by up to 21.4% compared with reactive baselines.

中文翻译：随着计算机使用Agent（CUA）在复杂真实环境中的广泛部署，普遍存在的长期风险往往导致严重且不可逆的后果。现有CUA护栏大多采用被动响应方式，仅在当前观测空间内约束Agent行为。虽然这些护栏可以防止即时短期风险（如点击钓鱼链接），但无法主动规避长期风险：看似合理的动作可能导致延迟出现的高风险后果（如清除日志导致未来审计无法追踪），响应式护栏在当前观测空间内无法识别这些风险。为克服这些局限，我们提出预测性护栏方法，核心思路是将预测的未来风险与当前决策对齐。基于此方法，我们提出SafePred，一个为CUA建立风险到决策循环以确保安全Agent行为的预测性护栏框架。SafePred支持两项关键能力：(1)短期和长期风险预测：以安全策略为风险预测基础，利用世界模型的预测能力生成风险的语义表示；(2)决策优化：通过步骤级干预和任务级重规划将预测风险转化为可操作的安全决策指导。大量实验表明SafePred显著减少了高风险行为，安全性能超过97.6%，任务效用相比被动响应基线提升高达21.4%。

------

Title: Evaluating Judges as Evaluators: The JETTS Benchmark of LLM-as-Judges as Test-Time Scaling Evaluators

URL: https://doi.org/10.48550/arXiv.2504.15253

Abstract: Scaling test-time computation, or affording a generator large language model (LLM) extra compute during inference, typically employs the help of external non-generative evaluators (i.e., reward models). Concurrently, LLM-judges, models trained to generate evaluations and critiques (explanations) in natural language, are becoming increasingly popular in automatic evaluation. Despite judge empirical successes, their effectiveness as evaluators in test-time scaling settings is largely unknown. In this paper, we introduce the Judge Evaluation for Test-Time Scaling (JETTS) benchmark, which evaluates judge performance in three domains (math reasoning, code generation, and instruction following) under three task settings: response reranking, step-level beam search, and critique-based response refinement. We evaluate 10 different judge models (7B-70B parameters) for 8 different base generator models (6.7B-72B parameters). Our benchmark shows that while judges are competitive with outcome reward models in reranking, they are consistently worse than process reward models in beam search procedures. Furthermore, though unique to LLM-judges, their natural language critiques are currently ineffective in guiding the generator towards better responses.

中文翻译：扩展测试时计算，或为生成器大语言模型（LLM）在推理期间提供额外计算资源，通常依赖外部非生成评估器（即奖励模型）的帮助。同时，LLM评判器——被训练为以自然语言生成评估和批判的模型——在自动评估中正变得越来越流行。尽管评判器在经验上取得了成功，但它们在测试时扩展场景中作为评估器的有效性在很大程度上是未知的。本文中我们引入Judge Evaluation for Test-Time Scaling（JETTS）基准，在三个领域（数学推理、代码生成和指令遵循）和三个任务设置（响应重排序、步骤级束搜索和基于批判的响应精炼）下评估评判器性能。我们为8个不同的基础生成器模型评估了10个不同的评判器模型。我们的基准显示，虽然评判器在重排序中与结果奖励模型有竞争力，但在束搜索过程中它们始终不如过程奖励模型。此外，尽管LLM评判器独有自然语言批判能力，其自然语言批判目前在引导生成器产生更好响应方面效果不佳。

------

Title: J4R: Learning to Judge with Equivalent Initial State Group Relative Policy Optimization

URL: https://doi.org/10.48550/arXiv.2505.13346

Abstract: To keep pace with the increasing pace of large language models (LLM) development, model output evaluation has transitioned away from time-consuming human evaluation to automatic evaluation, where LLMs themselves are tasked with assessing and critiquing other model outputs. LLM-as-judge models are a class of generative evaluators that excel in evaluating relatively simple domains, like chat quality, but struggle in reasoning intensive domains where model responses contain more substantive and challenging content. To remedy existing judge shortcomings, we explore training judges with reinforcement learning (RL). We make three key contributions: (1) We propose the Equivalent Initial State Group Relative Policy Optimization (EIS-GRPO) algorithm, which allows us to train our judge to be robust to positional biases that arise in more complex evaluation settings. (2) We introduce ReasoningJudgeBench, a benchmark that evaluates judges in diverse reasoning settings not covered by prior work. (3) We train Judge for Reasoning (J4R), a 7B judge trained with EIS-GRPO that outperforms GPT-4o and the next best small judge by 6.7% and 9%, matching or exceeding the performance of larger GRPO-trained judges on both JudgeBench and ReasoningJudgeBench.

中文翻译：为跟上大语言模型（LLM）发展的加速步伐，模型输出评估已从耗时的人类评估转向自动评估，其中LLM本身被赋予评估和批判其他模型输出的任务。LLM-as-judge模型是一类生成式评估器，在评估相对简单的领域表现出色，但在模型响应包含更实质性挑战内容的推理密集型领域则表现挣扎。为弥补现有评判器的不足，我们探索使用强化学习（RL）训练评判器。我们做出了三个关键贡献：(1)提出等效初始状态分组相对策略优化（EIS-GRPO）算法，使我们能够训练评判器对更复杂评估场景中出现的位置偏差保持鲁棒。(2)引入ReasoningJudgeBench，一个评估评判器在先前工作未覆盖的多样化推理场景中表现的基准。(3)训练J4R（Judge for Reasoning），一个使用EIS-GRPO训练的7B评判器，在JudgeBench和ReasoningJudgeBench上均超越GPT-4o和次优小评判器6.7%和9%，匹敌或超越更大GRPO训练评判器的性能。

------

Title: Reward Modeling from Natural Language Human Feedback

URL: https://doi.org/10.48550/arXiv.2601.07349

Abstract: Reinforcement Learning with Verifiable reward (RLVR) on preference data has become the mainstream approach for training Generative Reward Models (GRMs). Typically in pairwise rewarding tasks, GRMs generate reasoning chains ending with critiques and preference labels, and RLVR then relies on the correctness of the preference labels as the training reward. However, in this paper, we demonstrate that such binary classification tasks make GRMs susceptible to guessing correct outcomes without sound critiques. Consequently, these spurious successes introduce substantial noise into the reward signal, thereby impairing the effectiveness of reinforcement learning. To address this issue, we propose Reward Modeling from Natural Language Human Feedback (RM-NLHF), which leverages natural language feedback to obtain process reward signals, thereby mitigating the problem of limited solution space inherent in binary tasks. Specifically, we compute the similarity between GRM-generated and human critiques as the training reward, which provides more accurate reward signals than outcome-only supervision. Additionally, considering that human critiques are difficult to scale up, we introduce Meta Reward Model (MetaRM) which learns to predict process reward from datasets with human critiques and then generalizes to data without human critiques. Experiments on multiple benchmarks demonstrate that our method consistently outperforms state-of-the-art GRMs trained with outcome-only reward, confirming the superiority of integrating natural language over binary human feedback as supervision.

中文翻译：基于偏好数据的可验证奖励强化学习（RLVR）已成为训练生成式奖励模型（GRM）的主流方法。通常在成对奖励任务中，GRM生成以批判和偏好标签结尾的推理链，RLVR随后依赖偏好标签的正确性作为训练奖励。然而，本文中我们证明这种二分类任务使GRM容易在没有合理批判的情况下猜测正确结果。因此，这些虚假成功在奖励信号中引入大量噪声，从而损害强化学习的有效性。为解决这一问题，我们提出从自然语言人类反馈进行奖励建模（RM-NLHF），利用自然语言反馈获取过程奖励信号，从而缓解二值任务固有解空间有限的问题。具体而言，我们计算GRM生成批判与人类批判之间的相似度作为训练奖励，这提供了比仅结果监督更准确的奖励信号。此外，考虑到人类批判难以规模化，我们引入元奖励模型（MetaRM），从具有人类批判的数据集中学习预测过程奖励，然后泛化到无人类批判的数据。在多个基准上的实验表明，我们的方法始终优于仅使用结果奖励训练的最先进GRM，确认了整合自然语言而非二值人类反馈作为监督的优越性。

------

Title: Agent-RewardBench: Towards a Unified Benchmark for Reward Modeling across Perception, Planning, and Safety in Real-World Multimodal Agents

URL: https://doi.org/10.48550/arXiv.2506.21252

Abstract:

中文翻译：（摘要为空）

------

Title: Scaling Reward Modeling without Human Supervision

URL: https://www.semanticscholar.org/paper/a39068cc41776b34cd9b8a3a016579c01b953195

Abstract: Learning from feedback is an instrumental process for advancing the capabilities and safety of frontier models, yet its effectiveness is often constrained by cost and scalability. We present a pilot study that explores scaling reward models through unsupervised approaches. We operationalize reward-based scaling (RBS), in its simplest form, as preference learning over document prefixes and suffixes drawn from large-scale web corpora. Its advantage is demonstrated in various aspects: despite using no human annotations, training on 11M tokens of math-focused web data yields steady gains on RewardBench v1 and v2, and these improvements consistently transfer across diverse initialization backbones spanning model families and scales. Across models, our method improves RewardBench v2 accuracy by up to +7.7 points on average, with gains of up to +16.1 on in-domain math subsets and consistent improvements on out-of-domain safety and general subsets. When applied to best-of-N selection and policy optimization, these reward models substantially improve downstream math performance and match or exceed strong supervised reward model baselines of similar size. Overall, we demonstrate the feasibility and promise of training reward models without costly and potentially unreliable human annotations.

中文翻译：从反馈中学习是推进前沿模型能力和安全性的关键过程，但其有效性常受成本和可扩展性的制约。我们展示一项探索通过无监督方法扩展奖励模型的先导研究。我们以最简单的形式将基于奖励的扩展（RBS）操作化为对从大规模Web语料中提取的文档前缀和后缀的偏好学习。其优势体现在多个方面：尽管未使用任何人工标注，在1100万tokens的数学主题Web数据上训练能在RewardBench v1和v2上产生稳步提升，且这些改进在跨模型家族和规模的不同初始化骨干之间保持一致迁移。跨模型，我们的方法将RewardBench v2准确率平均提升高达+7.7个点，其中域内数学子集提升高达+16.1，域外安全和通用子集也有持续改善。当应用于best-of-N选择与策略优化时，这些奖励模型大幅提升下游数学性能，并匹敌或超越类似规模的强监督奖励模型基线。我们展示了无需昂贵且可能不可靠的人工标注来训练奖励模型的可行性和前景。

------

Title: Evaluating Robustness of Reward Models for Mathematical Reasoning

URL: https://doi.org/10.48550/arXiv.2410.01729

Abstract: Reward models are key in reinforcement learning from human feedback (RLHF) systems, aligning the model behavior with human preferences. Particularly in the math domain, there have been plenty of studies using reward models to align policies for improving reasoning capabilities. Recently, as the importance of reward models has been emphasized, RewardBench is proposed to understand their behavior. However, we figure out that the math subset of RewardBench has different representations between chosen and rejected completions, and relies on a single comparison, which may lead to unreliable results as it only see an isolated case. Therefore, it fails to accurately present the robustness of reward models, leading to a misunderstanding of its performance and potentially resulting in reward hacking. In this work, we introduce a new design for reliable evaluation of reward models, and to validate this, we construct RewardMATH, a benchmark that effectively represents the robustness of reward models in mathematical reasoning tasks. We demonstrate that the scores on RewardMATH strongly correlate with the results of optimized policy and effectively estimate reward overoptimization, whereas the existing benchmark shows almost no correlation. The results underscore the potential of our design to enhance the reliability of evaluation, and represent the robustness of reward model. We make our code and data publicly available.

中文翻译：奖励模型是从人类反馈强化学习（RLHF）系统中使模型行为与人类偏好对齐的关键。尤其在数学领域，已有大量研究使用奖励模型对齐策略以提升推理能力。最近，随着奖励模型重要性的强调，RewardBench被提出以理解它们的行为。然而，我们发现RewardBench的数学子集中在被选择和被拒绝的补全之间具有不同的表示，且依赖单一比较，这可能由于仅看到孤立案例而导致不可靠的结果。因此，它未能准确呈现奖励模型的鲁棒性，导致对其性能的误解并可能导致奖励黑客。本文中我们引入奖励模型可靠评估的新设计，并构建了RewardMATH来验证这一点，一个有效表示数学推理任务中奖励模型鲁棒性的基准。我们证明RewardMATH上的分数与优化策略的结果强相关，并有效估计奖励过度优化，而现有基准几乎不显示相关性。结果凸显了我们设计在增强评估可靠性和表示奖励模型鲁棒性方面的潜力。

------

Title: LIV: Language-Image Representations and Rewards for Robotic Control

URL: https://doi.org/10.48550/arXiv.2306.00958

Abstract: We present Language-Image Value learning (LIV), a unified objective for vision-language representation and reward learning from action-free videos with text annotations. Exploiting a novel connection between dual reinforcement learning and mutual information contrastive learning, the LIV objective trains a multi-modal representation that implicitly encodes a universal value function for tasks specified as language or image goals. We use LIV to pre-train the first control-centric vision-language representation from large human video datasets such as EpicKitchen. Given only a language or image goal, the pre-trained LIV model can assign dense rewards to each frame in videos of unseen robots or humans attempting that task in unseen environments. Further, when some target domain-specific data is available, the same objective can be used to fine-tune and improve LIV and even other pre-trained representations for robotic control and reward specification in that domain. In our experiments on several simulated and real-world robot environments, LIV models consistently outperform the best prior input state representations for imitation learning, as well as reward specification methods for policy synthesis. Our results validate the advantages of joint vision-language representation and reward learning within the unified, compact LIV framework.

中文翻译：我们提出LIV（Language-Image Value learning），一个从无动作视频和文本标注中学习视觉语言表示和奖励的统一目标。利用对偶强化学习和互信息对比学习之间的新颖联系，LIV目标训练一个多模态表示，该表示隐式编码了以语言或图像目标指定的任务的通用价值函数。我们使用LIV从大规模人类视频数据集（如EpicKitchen）预训练首个以控制为中心的视觉语言表示。仅给出语言或图像目标，预训练的LIV模型可以为未见环境中未见机器人或人类尝试该任务的视频的每一帧分配密集奖励。此外，当有部分目标领域特定数据时，同一目标可用于微调和改进LIV乃至其他预训练表示，用于该领域的机器人控制和奖励指定。在多个仿真和真实世界机器人环境实验中，LIV模型在模仿学习的输入状态表示以及策略合成的奖励指定方法上始终优于此前最佳方法。

------

Title: Real-World Offline Reinforcement Learning from Vision Language Model Feedback

URL: https://doi.org/10.1109/IROS60139.2025.11246918

Abstract: Offline reinforcement learning can enable policy learning from pre-collected, sub-optimal datasets without online interactions. This makes it ideal for real-world robots and safety-critical scenarios, where collecting online data or expert demonstrations is slow, costly, and risky. However, most existing offline RL works assume the dataset is already labeled with the task rewards, a process that often requires significant human effort, especially when ground-truth states are hard to ascertain (e.g., in the real-world). In this paper, we build on prior work, specifically RL-VLM-F, and propose a novel system that automatically generates reward labels for offline datasets using preference feedback from a vision-language model and a text description of the task. Our method then learns a policy using offline RL with the reward-labeled dataset. We demonstrate the system’s applicability to a complex real-world robot-assisted dressing task, where we first learn a reward function using a vision-language model on a sub-optimal offline dataset, and then we use the learned reward to employ Implicit Q learning to develop an effective dressing policy. Our method also performs well in simulation tasks involving the manipulation of rigid and deformable objects, and significantly outperforms baselines such as behavior cloning and inverse RL. In summary, we propose a new system that enables automatic reward labeling and policy learning from unlabeled, sub-optimal offline datasets. Videos can be found on our project website1.

中文翻译：离线强化学习可以从预收集的次优数据集学习策略而无需在线交互。这使其成为真实世界机器人和安全关键场景的理想选择，在这些场景中收集在线数据或专家演示缓慢、昂贵且有风险。然而，大多数现有离线RL工作假设数据集已标注了任务奖励，这一过程通常需要大量人类努力。本文中我们基于先前工作提出一个新颖系统，使用视觉语言模型的偏好反馈和任务的文本描述自动为离线数据集生成奖励标签。我们的方法随后使用奖励标注的数据集通过离线RL学习策略。我们展示了该系统在一个复杂的真实世界机器人辅助穿衣任务上的适用性：我们首先使用视觉语言模型在次优离线数据集上学习奖励函数，然后使用学到的奖励应用隐式Q学习来开发有效的穿衣策略。我们的方法在涉及刚体和可变形物体操作的仿真任务中也表现良好，并显著超越行为克隆和逆RL等基线。

------

Title: Learning and Leveraging Verifiers to Improve Planning Capabilities of Pre-trained Language Models

URL: https://doi.org/10.48550/arXiv.2305.17077

Abstract: There have been wide spread claims in the literature about the emergent reasoning capabilities of Pretrained Large Language Models. However, recent studies, have found that their ability to plan remains questionable. Through our experiments using GPT-2, we empirically demonstrate that the performance of a finetuned baseline remains poor because it violates pre-conditions of actions in the plans that it generates. To improve the planning capabilities of a finetuned LLM, we train a verifier, which can classify actions as being valid or invalid in a particular state. By randomly sampling actions from the same dataset, we generate examples of invalid actions which are then used to train a verifier which can check for action applicability. In the presence of diverse sampling from a generator and a verifier which can prune invalid trajectories, we show significant gains in the success rate on the Blocksworld domain. Additionally, we show that finetuning the GPT-2 generator itself to create the verifier generalizes better than finetuning the base GPT-2. Lastly, we investigate the role of the sampling temperature which can be used to control the exploration-exploitation tradeoff.

中文翻译：文献中广泛声称预训练大语言模型具有涌现推理能力。然而，近期研究发现它们的规划能力仍然存疑。通过使用GPT-2进行实验，我们经验性地证明微调基线的表现仍然较差，因为它违反了其生成计划中动作的前提条件。为改进微调LLM的规划能力，我们训练了一个验证器，可以对动作在特定状态下是否有效进行分类。通过从同一数据集中随机采样动作，我们生成无效动作的示例，然后用于训练可检查动作适用性的验证器。在多样化的生成器采样和能剪枝无效轨迹的验证器共同作用下，我们在Blocksworld领域中展示了成功率的显著提升。此外，我们证明微调GPT-2生成器本身来创建验证器比微调基础GPT-2泛化得更好。最后，我们研究了采样温度的作用，它可用于控制探索-利用的权衡。

------

Title: Interpretable Preferences via Multi-Objective Reward Modeling and Mixture-of-Experts

URL: https://doi.org/10.48550/arXiv.2406.12845

Abstract: Reinforcement learning from human feedback (RLHF) has emerged as the primary method for aligning large language models (LLMs) with human preferences. The RLHF process typically starts by training a reward model (RM) using human preference data. Conventional RMs are trained on pairwise responses to the same user request, with relative ratings indicating which response humans prefer. The trained RM serves as a proxy for human preferences. However, due to the black-box nature of RMs, their outputs lack interpretability, as humans cannot intuitively understand why an RM thinks a response is good or not. As RMs act as human preference proxies, we believe they should be human-interpretable to ensure that their internal decision processes are consistent with human preferences and to prevent reward hacking in LLM alignment. To build RMs with interpretable preferences, we propose a two-stage approach: i) train an Absolute-Rating Multi-Objective Reward Model (ArmoRM) with multi-dimensional absolute-rating data, each dimension corresponding to a human-interpretable objective (e.g., honesty, verbosity, safety); ii) employ a Mixture-of-Experts (MoE) strategy with a gating network that automatically selects the most suitable reward objectives based on the context. We efficiently trained an ArmoRM with Llama-3 8B and a gating network consisting of a shallow MLP on top of the ArmoRM. Our trained model, ArmoRM-Llama3-8B, obtains state-of-the-art performance on RewardBench, a benchmark evaluating RMs for language modeling. Notably, the performance of our model surpasses the LLM-as-a-judge method with GPT-4 judges by a margin, and approaches the performance of the much larger Nemotron-4 340B reward model.

中文翻译：从人类反馈强化学习（RLHF）已成为使大语言模型（LLM）与人类偏好对齐的主要方法。RLHF过程通常从使用人类偏好数据训练奖励模型（RM）开始。传统RM在相同用户请求的成对响应上训练，相对评分指示人类偏好哪个响应。训练好的RM充当人类偏好的代理。然而，由于RM的黑盒性质，其输出缺乏可解释性，人类无法直观理解RM为何认为一个响应好或不好。由于RM充当人类偏好代理，我们认为它们应是人类可解释的，以确保其内部决策过程与人类偏好一致并防止LLM对齐中的奖励黑客。为构建具有可解释偏好的RM，我们提出一种两阶段方法：i)使用多维绝对评分数据训练绝对评分多目标奖励模型（ArmoRM），每个维度对应人类可解释的目标（如诚实性、详细程度、安全性）；ii)采用混合专家（MoE）策略，配合门控网络根据上下文自动选择最合适的奖励目标。我们使用Llama-3 8B高效训练了ArmoRM，并在ArmoRM之上使用浅层MLP作为门控网络。我们训练的ArmoRM-Llama3-8B在RewardBench上取得最优性能，超过使用GPT-4评判器的LLM-as-a-judge方法，并接近大得多的Nemotron-4 340B奖励模型的性能。

------

Title: Generative Judge for Evaluating Alignment

URL: https://doi.org/10.48550/arXiv.2310.05470

Abstract: The rapid development of Large Language Models (LLMs) has substantially expanded the range of tasks they can address. In the field of Natural Language Processing (NLP), researchers have shifted their focus from conventional NLP tasks (e.g., sequence tagging and parsing) towards tasks that revolve around aligning with human needs (e.g., brainstorming and email writing). This shift in task distribution imposes new requirements on evaluating these aligned models regarding generality (i.e., assessing performance across diverse scenarios), flexibility (i.e., examining under different protocols), and interpretability (i.e., scrutinizing models with explanations). In this paper, we propose a generative judge with 13B parameters, Auto-J, designed to address these challenges. Our model is trained on user queries and LLM-generated responses under massive real-world scenarios and accommodates diverse evaluation protocols (e.g., pairwise response comparison and single-response evaluation) with well-structured natural language critiques. To demonstrate the efficacy of our approach, we construct a new testbed covering 58 different scenarios. Experimentally, Auto-J outperforms a series of strong competitors, including both open-source and closed-source models, by a large margin. We also provide detailed analysis and case studies to further reveal the potential of our method and make a variety of resources public at https://github.com/GAIR-NLP/auto-j.

中文翻译：大语言模型（LLM）的快速发展大幅扩展了它们可以处理的任务范围。在自然语言处理（NLP）领域，研究者的焦点已从传统NLP任务转向围绕与人类需求对齐的任务。这种任务分布的变化对评估这些对齐模型提出了新要求，涉及通用性（即评估跨多样化场景的性能）、灵活性（即在不同协议下检验）和可解释性（即通过解释审查模型）。本文中我们提出Auto-J，一个具有13B参数的生成式评判器，旨在应对这些挑战。我们的模型在大量真实世界场景下的用户查询和LLM生成响应上训练，并以结构良好的自然语言批判适应多样化评估协议（如成对响应比较和单响应评估）。为证明我们方法的有效性，我们构建了一个覆盖58个不同场景的新测试平台。实验上，Auto-J以大幅优势超越了一系列强竞争对手，包括开源和闭源模型。

------

Title: Improve LLM-as-a-Judge Ability as a General Ability

URL: https://doi.org/10.48550/arXiv.2502.11689

Abstract: LLM-as-a-Judge leverages the generative and reasoning capabilities of large language models (LLMs) to evaluate LLM responses across diverse scenarios, providing accurate preference signals. This approach plays a vital role in aligning LLMs with human values, ensuring ethical and reliable AI outputs that align with societal norms. Recent studies have raised many methods to train LLM as generative judges, but most of them are data consuming or lack accuracy, and only focus on LLM's judge ability. In this work, we regard judge ability as a general ability of LLM and implement a two-stage training approach, comprising supervised fine-tuning (SFT) warm-up and direct preference optimization (DPO) enhancement, to achieve judge style adaptation and improve judgment accuracy. Additionally, we introduce an efficient data synthesis method to generate judgmental content. Experimental results demonstrate that our approach, utilizing only about 2% to 40% of the data required by other methods, achieves SOTA performance on RewardBench. Furthermore, our training method enhances the general capabilities of the model by constructing complicated judge task, and the judge signals provided by our model have significantly enhanced the downstream DPO training performance of our internal models in our test to optimize policy model with Judge Model. We also open-source our model weights and training data to facilitate further research.

中文翻译：LLM-as-a-Judge利用大语言模型（LLM）的生成和推理能力在多样化场景中评估LLM响应，提供准确的偏好信号。该方法在使LLM与人类价值对齐中发挥关键作用。近期研究提出了许多训练LLM作为生成式评判器的方法，但其中大多数数据消耗大或缺乏准确性，且仅关注LLM的评判能力。本文中我们将评判能力视为LLM的一种通用能力，实施两阶段训练方法，包括监督微调（SFT）预热和直接偏好优化（DPO）增强，以实现评判风格适应和提升判断准确率。此外，我们引入一种高效数据合成方法生成判断内容。实验结果表明，我们的方法仅使用其他方法约2%到40%的数据，在RewardBench上达到最优性能。此外，我们的训练方法通过构建复杂评判任务增强了模型的通用能力，我们模型提供的评判信号显著改善了下游DPO训练性能。

------

Title: S2J: Bridging the Gap Between Solving and Judging Ability in Generative Reward Models

URL: https://doi.org/10.48550/arXiv.2509.22099

Abstract: With the rapid development of large language models (LLMs), generative reward models (GRMs) have been widely adopted for reward modeling and evaluation. Previous studies have primarily focused on training specialized GRMs by optimizing them on preference datasets with the judgment correctness as supervision. While it's widely accepted that GRMs with stronger problem-solving capabilities typically exhibit superior judgment abilities, we first identify a significant solve-to-judge gap when examining individual queries. Specifically, the solve-to-judge gap refers to the phenomenon where GRMs struggle to make correct judgments on some queries (14%-37%), despite being fully capable of solving them. In this paper, we propose the Solve-to-Judge (S2J) approach to address this problem. Specifically, S2J simultaneously leverages both the solving and judging capabilities on a single GRM's output for supervision, explicitly linking the GRM's problem-solving and evaluation abilities during model optimization, thereby narrowing the gap. Our comprehensive experiments demonstrate that S2J effectively reduces the solve-to-judge gap by 16.2%, thereby enhancing the model's judgment performance by 5.8%. Notably, S2J achieves state-of-the-art (SOTA) performance among GRMs built on the same base model while utilizing a significantly smaller training dataset. Moreover, S2J accomplishes this through self-evolution without relying on more powerful external models for distillation.

中文翻译：随着大语言模型（LLM）的快速发展，生成式奖励模型（GRM）已被广泛用于奖励建模和评估。先前研究主要聚焦于通过以判断正确性为监督在偏好数据集上优化来训练专用GRM。虽然普遍认为具有更强问题求解能力的GRM通常展现更优的判断能力，但我们首先识别出在检查单个查询时存在显著的求解-判断差距。具体而言，求解-判断差距指GRM在某些查询上难以做出正确判断（14%-37%），尽管它们完全有能力求解这些查询。本文中我们提出Solve-to-Judge（S2J）方法来解决这一问题。S2J同时利用单个GRM输出中的求解和判断能力作为监督，在模型优化期间明确连接GRM的问题求解和评估能力，从而缩小差距。我们的全面实验表明S2J有效将求解-判断差距缩小16.2%，从而将模型判断性能提升5.8%。S2J在基于相同基座模型构建的GRM中取得最优性能，同时使用显著更小的训练数据集，并通过自我进化实现这一点。

------

Title: Bringing Value Models Back: Generative Critics for Value Modeling in LLM Reinforcement Learning

URL: https://www.semanticscholar.org/paper/c6b24f2a4b58e5faa364b53fbb4f84b9a9330817

Abstract: Credit assignment is a central challenge in reinforcement learning (RL). Classical actor-critic methods address this challenge through fine-grained advantage estimation based on a learned value function. However, learned value models are often avoided in modern large language model (LLM) RL because conventional discriminative critics are difficult to train reliably. We revisit value modeling and argue that this difficulty is partly due to limited expressiveness. In particular, representation complexity theory suggests that value functions can be hard to approximate under the one-shot prediction paradigm used by existing value models, and our scaling experiments show that such critics do not improve reliably with scale. Motivated by this observation, we propose Generative Actor-Critic (GenAC), which replaces one-shot scalar value prediction with a generative critic that performs chain-of-thought reasoning before producing a value estimate. We further introduce In-Context Conditioning, which helps the critic remain calibrated to the current actor throughout training. GenAC improves value approximation, ranking reliability, and out-of-distribution generalization, and these gains translate into stronger downstream RL performance than both value-based and value-free baselines. Overall, our results suggest that stronger value modeling is a promising direction for improving credit assignment in LLM reinforcement learning.

中文翻译：信用分配是强化学习（RL）的核心挑战。经典Actor-Critic方法通过学习值函数基于细粒度优势估计来解决这一挑战。然而，在现代大语言模型（LLM）RL中，由于传统判别式Critic难以可靠训练，学习的值模型往往被回避。我们重新审视值建模，认为这一困难部分源于有限的表达能力。具体而言，表示复杂性理论表明在现有值模型使用的单次预测范式下价值函数可能难以近似，我们的扩展实验显示此类Critic并不随规模可靠改进。受此观察启发，我们提出生成式Actor-Critic（GenAC），用执行思维链推理后再产生值估计的生成式Critic取代单次标量值预测。我们进一步引入上下文条件化，帮助Critic在整个训练过程中保持对当前Actor的校准。GenAC改善了值近似、排序可靠性和分布外泛化，这些改进转化为比基于值和无值基线更强的下游RL性能。

------

Title: Multimodal Reinforcement Learning with Agentic Verifier for AI Agents

URL: https://doi.org/10.48550/arXiv.2512.03438

Abstract: Agentic reasoning models trained with multimodal reinforcement learning (MMRL) have become increasingly capable, yet they are almost universally optimized using sparse, outcome-based rewards computed based on the final answers. Richer rewards computed from the reasoning tokens can improve learning significantly by providing more fine-grained guidance. However, it is challenging to compute more informative rewards in MMRL beyond those based on outcomes since different samples may require different scoring functions and teacher models may provide noisy reward signals too. In this paper, we introduce the Argos (Agentic Reward for Grounded&Objective Scoring), a principled reward agent to train multimodal reasoning models for agentic tasks. For each sample, Argos selects from a pool of teacher-model derived and rule-based scoring functions to simultaneously evaluate: (i) final response accuracy, (ii) spatiotemporal localization of referred entities and actions, and (iii) the quality of the reasoning process. We find that by leveraging our agentic verifier across both SFT data curation and RL training, our model achieves state-of-the-art results across multiple agentic tasks such as spatial reasoning, visual hallucination as well as robotics and embodied AI benchmarks. Critically, we demonstrate that just relying on SFT post-training on highly curated reasoning data is insufficient, as agents invariably collapse to ungrounded solutions during RL without our online verification. We also show that our agentic verifier can help to reduce reward-hacking in MMRL. Finally, we also provide a theoretical justification for the effectiveness of Argos through the concept of pareto-optimality.

中文翻译：使用多模态强化学习（MMRL）训练的Agent推理模型能力日益增强，但它们几乎普遍使用基于最终答案计算的稀疏结果奖励进行优化。从推理token计算更丰富的奖励可以通过提供更细粒度引导来显著改善学习。然而，在MMRL中计算超越结果的信息性奖励具有挑战性，因为不同样本可能需要不同的评分函数，教师模型也可能提供噪声奖励信号。本文中我们引入Argos（Agentic Reward for Grounded&Objective Scoring），一个原则化奖励Agent，用于为Agent任务训练多模态推理模型。对每个样本，Argos从教师模型衍生和基于规则的评分函数池中选择，同时评估：(i)最终响应准确率，(ii)所引用实体和动作的时空定位，(iii)推理过程质量。通过利用我们的Agent验证器，模型在多个Agent任务上取得最优结果。关键的是，我们证明仅依赖SFT后训练是不够的，因为在没有在线验证的情况下Agent在RL期间不可避免地坍缩为无根基的解。我们还通过帕累托最优性概念为Argos的有效性提供了理论论证。

------

Title: AutoGLM: Autonomous Foundation Agents for GUIs

URL: https://doi.org/10.48550/arXiv.2411.00820

Abstract: We present AutoGLM, a new series in the ChatGLM family, designed to serve as foundation agents for autonomous control of digital devices through Graphical User Interfaces (GUIs). While foundation models excel at acquiring human knowledge, they often struggle with decision-making in dynamic real-world environments, limiting their progress toward artificial general intelligence. This limitation underscores the importance of developing foundation agents capable of learning through autonomous environmental interactions by reinforcing existing models. Focusing on Web Browser and Phone as representative GUI scenarios, we have developed AutoGLM as a practical foundation agent system for real-world GUI interactions. Our approach integrates a comprehensive suite of techniques and infrastructures to create deployable agent systems suitable for user delivery. Through this development, we have derived two key insights: First, the design of an appropriate"intermediate interface"for GUI control is crucial, enabling the separation of planning and grounding behaviors, which require distinct optimization for flexibility and accuracy respectively. Second, we have developed a novel progressive training framework that enables self-evolving online curriculum reinforcement learning for AutoGLM. Our evaluations demonstrate AutoGLM's effectiveness across multiple domains. For web browsing, AutoGLM achieves a 55.2% success rate on VAB-WebArena-Lite (improving to 59.1% with a second attempt) and 96.2% on OpenTable evaluation tasks. In Android device control, AutoGLM attains a 36.2% success rate on AndroidLab (VAB-Mobile) and 89.7% on common tasks in popular Chinese APPs.

中文翻译：我们提出AutoGLM，ChatGLM系列的新成员，旨在作为通过GUI自主控制数字设备的基础Agent。虽然基础模型擅长获取人类知识，但在动态真实环境中的决策往往存在困难。聚焦Web浏览器和手机作为代表性GUI场景，我们开发了AutoGLM作为面向真实世界GUI交互的实用基础Agent系统。我们的方法整合了一套全面的技术和基础设施。通过这一开发过程，我们推导出两个关键洞察：第一，为GUI控制设计适当的中间接口至关重要，可实现规划和锚定行为的分离，这两者分别需要对灵活性和准确率的不同优化。第二，我们开发了一种新颖的渐进式训练框架，使AutoGLM能够进行自我进化的在线课程强化学习。对于Web浏览，AutoGLM在VAB-WebArena-Lite上达到55.2%成功率（第二次尝试提升至59.1%），在OpenTable评估任务上达到96.2%。在Android设备控制中，AutoGLM在AndroidLab（VAB-Mobile）上达到36.2%成功率，在流行中文APP的常见任务上达到89.7%。

------

Title: Is Your LLM Secretly a World Model of the Internet? Model-Based Planning for Web Agents

URL: https://doi.org/10.48550/arXiv.2411.06559

Abstract: Language agents based on large language models (LLMs) have demonstrated great promise in automating web-based tasks. Recent work has shown that incorporating advanced planning algorithms, e.g., tree search, is advantageous over reactive planning for web agents. However, unlike simulated sandbox environments, real-world environments such as the web are rife with irreversible actions. This undermines the feasibility of backtracking, a cornerstone of (tree) search. Overly relying on test-time search also hurts efficiency. We advocate model-based planning for web agents that employs a world model to simulate and deliberate over the outcome of each candidate action before committing to one. We systematically explore this paradigm by (1) Proposing a model-based planning framework, WebDreamer, which employs LLMs to serve as both world models and value functions; (2) Training specialized LLMs as world models with a scalable data synthesis pipeline. Empirical results demonstrate that WebDreamer achieves substantial performance improvements over reactive baselines. It is competitive, while being 4-5 times more efficient, with tree search in sandbox environments (VisualWebArena) and also works effectively on real-world websites (Online-Mind2Web and Mind2Web-Live). Furthermore, our trained world model, Dreamer-7B, performs comparable to GPT-4o, highlighting the potential of specialized world models for efficient and effective planning in complex web environments.

中文翻译：基于大语言模型（LLM）的语言Agent在自动化Web任务方面展现了巨大前景。近期工作表明，相比反应式规划，纳入树搜索等高级规划算法对Web Agent更有利。然而，与仿真沙盒环境不同，Web等真实环境充满不可逆操作，破坏了回溯的可行性，而回溯是树搜索的基石。过度依赖测试时搜索也损害效率。我们倡导基于模型的Web Agent规划，使用世界模型在提交动作前模拟和权衡每个候选动作的结果。我们通过以下方式系统探索这一范式：(1)提出基于模型的规划框架WebDreamer，使用LLM同时充当世界模型和价值函数；(2)通过可扩展的数据合成管线训练专用LLM作为世界模型。实证结果表明WebDreamer相比反应式基线实现显著性能提升。在沙盒环境（VisualWebArena）中，它的竞争力与树搜索相当，而效率高出4-5倍，并在真实世界网站上有效运行。我们训练的世界模型Dreamer-7B表现与GPT-4o相当，凸显专用世界模型在复杂Web环境中高效且有效规划的潜力。

------

Title: Constitutional AI: Harmlessness from AI Feedback

URL: https://doi.org/10.48550/arXiv.2212.08073

Abstract: As AI systems become more capable, we would like to enlist their help to supervise other AIs. We experiment with methods for training a harmless AI assistant through self-improvement, without any human labels identifying harmful outputs. The only human oversight is provided through a list of rules or principles, and so we refer to the method as 'Constitutional AI'. The process involves both a supervised learning and a reinforcement learning phase. In the supervised phase we sample from an initial model, then generate self-critiques and revisions, and then finetune the original model on revised responses. In the RL phase, we sample from the finetuned model, use a model to evaluate which of the two samples is better, and then train a preference model from this dataset of AI preferences. We then train with RL using the preference model as the reward signal, i.e. we use 'RL from AI Feedback' (RLAIF). As a result we are able to train a harmless but non-evasive AI assistant that engages with harmful queries by explaining its objections to them. Both the SL and RL methods can leverage chain-of-thought style reasoning to improve the human-judged performance and transparency of AI decision making. These methods make it possible to control AI behavior more precisely and with far fewer human labels.

中文翻译：随着AI系统能力的增强，我们希望借助它们的帮助来监督其他AI。我们实验了通过自我改进训练无害AI助手的方法，无需任何识别有害输出的人类标签。唯一的人类监督通过一系列规则或原则提供，因此我们将该方法称为Constitutional AI。过程包含监督学习和强化学习两个阶段。在监督阶段，我们从初始模型采样，然后生成自我批判和修订，随后在修订后的响应上微调原始模型。在RL阶段，我们从微调模型采样，使用一个模型评估两个样本中哪个更好，然后从这个AI偏好数据集训练偏好模型。我们随后使用偏好模型作为奖励信号进行RL训练，即使用从AI反馈的RL（RLAIF）。结果我们能够训练出一个无害但不回避的AI助手，它通过解释其反对意见来回应有害查询。SL和RL方法都可以利用思维链式推理来提升人类判断的性能和AI决策的透明度。

------

Title: RewardBench: Evaluating Reward Models for Language Modeling

URL: https://doi.org/10.48550/arXiv.2403.13787

Abstract: Reward models (RMs) are at the crux of successfully using RLHF to align pretrained models to human preferences, yet there has been relatively little study that focuses on evaluation of those models. Evaluating reward models presents an opportunity to understand the opaque technologies used for alignment of language models and which values are embedded in them. Resources for reward model training and understanding are sparse in the nascent open-source community around them. To enhance scientific understanding of reward models, we present RewardBench, a benchmark dataset and code-base for evaluation. The RewardBench dataset is a collection of prompt-chosen-rejected trios spanning chat, reasoning, and safety, to benchmark how reward models perform on challenging, structured and out-of-distribution queries. We create specific comparison datasets for RMs that have subtle, but verifiable reasons (e.g. bugs, incorrect facts) why one answer should be preferred to another. On the RewardBench leaderboard, we evaluate reward models trained with a variety of methods, such as the direct MLE training of classifiers and the implicit reward modeling of Direct Preference Optimization (DPO). We present many findings on propensity for refusals, reasoning limitations, and instruction following shortcomings of various reward models towards a better understanding of the RLHF process.

中文翻译：奖励模型（RM）是成功使用RLHF将预训练模型与人类偏好对齐的关键，但相对较少有研究聚焦于这些模型的评估。评估奖励模型提供了理解用于语言模型对齐的不透明技术及其所嵌入价值观的机会。围绕它们的开源社区中，奖励模型训练和理解的资源稀缺。为增强对奖励模型的科学理解，我们提出RewardBench，一个用于评估的基准数据集和代码库。RewardBench数据集是涵盖对话、推理和安全的提示-被选择-被拒绝三元组集合，用于基准测试奖励模型在具有挑战性、结构化和分布外查询上的表现。我们创建了特定的比较数据集，包含微妙但可验证的原因说明为何一个答案应优于另一个。在RewardBench排行榜上，我们评估了使用多种方法训练的奖励模型，如分类器的直接MLE训练和DPO的隐式奖励建模。我们呈现了许多发现，包括各种奖励模型拒绝倾向、推理局限和指令遵循缺陷。

------

Title: RLAC: Reinforcement Learning with Adversarial Critic for Free-Form Generation Tasks

URL: https://doi.org/10.48550/arXiv.2511.01758

Abstract: Open-ended generation tasks require outputs to satisfy diverse and often implicit task-specific evaluation rubrics. The sheer number of relevant rubrics leads to prohibitively high verification costs and incomplete assessments of a response, making reinforcement learning (RL) post-training with rubric-based rewards difficult to scale. This problem is exacerbated by the fact that often the best way to combine these rubrics into one single reward is also highly prompt-specific. We propose Reinforcement Learning with Adversarial Critic (RLAC), a post-training approach that addresses these challenges via dynamic rubric verification. Our approach employs a large language model (LLM) as a critic that dynamically identifies only the most likely failure modes (e.g., a factual error or unhandled edge case), which are then verified by an external validator to optimize both generator and critic jointly. By training both the generator and the critic, this game enhances the critic's error detection and the generator's output quality while reducing required verifications. Our experiments demonstrate that RLAC improves factual accuracy in text generation and correctness in code generation, while also outperforming exhaustive verification and reward model methods. We show that dynamic critics are more effective than fixed critics, showcasing the potential of RLAC for scaling RL post-training to free-form generation tasks.

中文翻译：开放式生成任务要求输出满足多样化且常为隐式的任务特定评估量规。大量相关量规导致验证成本极高和响应评估不完整，使得使用基于量规奖励的强化学习（RL）后训练难以扩展。这一问题因组合这些量规为一个单一奖励的最佳方式也高度依赖具体提示而加剧。我们提出RLAC（Reinforcement Learning with Adversarial Critic），一种通过动态量规验证应对这些挑战的后训练方法。我们的方法使用大语言模型（LLM）作为批判器，动态识别仅最可能的失败模式（如事实错误或未处理的边界情况），然后由外部验证器验证，联合优化生成器和批判器。通过同时训练生成器和批判器，这一博弈增强了批判器的错误检测能力和生成器的输出质量，同时减少了所需验证次数。实验表明RLAC提升了文本生成中的事实准确率和代码生成中的正确性，同时优于穷尽验证和奖励模型方法。

------

Title: RLHF Workflow: From Reward Modeling to Online RLHF

URL: https://doi.org/10.48550/arXiv.2405.07863

Abstract: We present the workflow of Online Iterative Reinforcement Learning from Human Feedback (RLHF) in this technical report, which is widely reported to outperform its offline counterpart by a large margin in the recent large language model (LLM) literature. However, existing open-source RLHF projects are still largely confined to the offline learning setting. In this technical report, we aim to fill in this gap and provide a detailed recipe that is easy to reproduce for online iterative RLHF. In particular, since online human feedback is usually infeasible for open-source communities with limited resources, we start by constructing preference models using a diverse set of open-source datasets and use the constructed proxy preference model to approximate human feedback. Then, we discuss the theoretical insights and algorithmic principles behind online iterative RLHF, followed by a detailed practical implementation. Our trained LLM achieves impressive performance on LLM chatbot benchmarks, including AlpacaEval-2, Arena-Hard, and MT-Bench, as well as other academic benchmarks such as HumanEval and TruthfulQA. We have shown that supervised fine-tuning (SFT) and iterative RLHF can obtain state-of-the-art performance with fully open-source datasets. Further, we have made our models, curated datasets, and comprehensive step-by-step code guidebooks publicly available. Please refer to https://github.com/RLHFlow/RLHF-Reward-Modeling and https://github.com/RLHFlow/Online-RLHF for more detailed information.

中文翻译：本技术报告呈现了在线迭代从人类反馈强化学习（RLHF）的工作流程，近期大语言模型（LLM）文献广泛报告其大幅超越离线对应方法。然而，现有开源RLHF项目仍主要局限于离线学习设置。本技术报告旨在填补这一空白，提供易于复现的在线迭代RLHF详细方案。特别是，由于在线人类反馈对资源有限的开源社区通常不可行，我们首先使用多样化开源数据集构建偏好模型，并将构建的代理偏好模型用于近似人类反馈。然后，我们讨论在线迭代RLHF背后的理论洞察和算法原理，随后是详细的实践实现。我们训练的LLM在AlpacaEval-2、Arena-Hard和MT-Bench等LLM聊天基准上取得令人印象深刻的性能。我们证明监督微调（SFT）和迭代RLHF可以仅用全开源数据集取得最优性能。

------

Title: Zero-Shot Reward Specification via Grounded Natural Language

URL: https://www.semanticscholar.org/paper/a09560239e398fe8aea05856823b46219a7dc539

Abstract: Reward signals in reinforcement learning are expensive to design and often require access to the true state which is not available in the real world. Common alternatives are usually demonstrations or goal images which can be labor-intensive to collect. On the other hand, text descriptions provide a general, natural, and low-effort way of commu-nicating the desired task. However, prior works in learning text-conditioned policies still rely on rewards that are defined using either true state or labeled expert demonstrations. We use recent de-velopments in building large-scale visuolanguage models like CLIP to devise a framework that generates the task reward signal just from goal text description and raw pixel observations which is then used to learn the task policy. We evaluate the proposed framework on control and robotic manipulation tasks. Finally, we distill the individual task policies into a single goal text conditioned policy that can generalize in a zero-shot manner to new tasks with unseen objects and unseen goal text descriptions.

中文翻译：强化学习中的奖励信号设计成本高昂，且通常需要访问在真实世界中不可用的真实状态。常见替代方案通常是演示或目标图像，收集起来可能劳动密集。另一方面，文本描述提供了一种通用、自然且低投入的传达所需任务的方式。然而，学习文本条件策略的先前工作仍依赖使用真实状态或标注专家演示定义的奖励。我们利用构建大规模视觉语言模型（如CLIP）的最新进展，设计了一个仅从目标文本描述和原始像素观测生成任务奖励信号的框架，随后用于学习任务策略。我们在控制和机器人操作任务上评估了所提框架。最后，我们将各个任务策略蒸馏为单一目标文本条件策略，该策略能够以零样本方式泛化到具有未见物体和未见目标文本描述的新任务。

------
