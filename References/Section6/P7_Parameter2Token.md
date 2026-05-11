Title: Agent KB: Leveraging Cross-Domain Experience for Agentic Problem Solving

URL: https://doi.org/10.48550/arXiv.2507.06229

Abstract: AI agent frameworks operate in isolation, forcing agents to rediscover solutions and repeat mistakes across different systems. Despite valuable problem-solving experiences accumulated by frameworks like smolagents, OpenHands, and OWL, this knowledge remains trapped within individual systems, preventing the emergence of collective intelligence. Current memory systems focus on individual agents or framework-specific demonstrations, failing to enable cross-architecture knowledge transfer. We introduce AGENT KB, a universal memory infrastructure enabling seamless experience sharing across heterogeneous agent frameworks without retraining. AGENT KB aggregates trajectories into a structured knowledge base and serves lightweight APIs. At inference time, hybrid retrieval operates through two stages: planning seeds agents with cross-domain workflows, while feedback applies targeted diagnostic fixes. A disagreement gate ensures retrieved knowledge enhances rather than disrupts reasoning, addressing knowledge interference in cross-framework transfer. We validate AGENT KB across major frameworks on GAIA, Humanity's Last Exam, GPQA, and SWE-bench. Results show substantial improvements across diverse model families: compared to baseline pass@1, smolagents with AGENT KB achieve up to 18.7pp gains at pass@3 (55.2% ->73.9%), while OpenHands improves 4.0pp on SWE-bench pass@1 (24.3% ->28.3%). Similar improvements are observed across all base model families. Ablations confirm that hybrid retrieval and feedback stages are essential, with automatically generated experiences matching manual curation. This establishes the foundation for collective agent intelligence through shared memory infrastructures.

------

Title: SkillX: Automatically Constructing Skill Knowledge Bases for Agents

URL: https://www.semanticscholar.org/paper/24566e0b5989b1b32951ff9a10b6d6b0162683f5

Abstract: Learning from experience is critical for building capable large language model (LLM) agents, yet prevailing self-evolving paradigms remain inefficient: agents learn in isolation, repeatedly rediscover similar behaviors from limited experience, resulting in redundant exploration and poor generalization. To address this problem, we propose SkillX, a fully automated framework for constructing a \textbf{plug-and-play skill knowledge base} that can be reused across agents and environments. SkillX operates through a fully automated pipeline built on three synergistic innovations: \textit{(i) Multi-Level Skills Design}, which distills raw trajectories into three-tiered hierarchy of strategic plans, functional skills, and atomic skills; \textit{(ii) Iterative Skills Refinement}, which automatically revises skills based on execution feedback to continuously improve library quality; and \textit{(iii) Exploratory Skills Expansion}, which proactively generates and validates novel skills to expand coverage beyond seed training data. Using a strong backbone agent (GLM-4.6), we automatically build a reusable skill library and evaluate its transferability on challenging long-horizon, user-interactive benchmarks, including AppWorld, BFCL-v3, and $\tau^2$-Bench. Experiments show that SkillKB consistently improves task success and execution efficiency when plugged into weaker base agents, highlighting the importance of structured, hierarchical experience representations for generalizable agent learning. Our code will be publicly available soon at https://github.com/zjunlp/SkillX.

------

Title: Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills

URL: https://www.semanticscholar.org/paper/8b02872a17028c037e214fef695304494c809411

Abstract: Equipping Large Language Model (LLM) agents with domain-specific skills is critical for tackling complex tasks. Yet, manual authoring creates a severe scalability bottleneck. Conversely, automated skill generation often yields fragile or fragmented results because it either relies on shallow parametric knowledge or sequentially overfits to non-generalizable trajectory-local lessons. To overcome this, we introduce Trace2Skill, a framework that mirrors how human experts author skills: by holistically analyzing broad execution experience before distilling it into a single, comprehensive guide. Instead of reacting sequentially to individual trajectories, Trace2Skill dispatches a parallel fleet of sub-agents to analyze a diverse pool of executions. It extracts trajectory-specific lessons and hierarchically consolidates them into a unified, conflict-free skill directory via inductive reasoning. Trace2Skill supports both deepening existing human-written skills and creating new ones from scratch. Experiments in challenging domains, such as spreadsheet, VisionQA and math reasoning, show that Trace2Skill significantly improves upon strong baselines, including Anthropic's official xlsx skills. Crucially, this trajectory-grounded evolution does not merely memorize task instances or model-specific quirks: evolved skills transfer across LLM scales and generalize to OOD settings. For example, skills evolved by Qwen3.5-35B on its own trajectories improved a Qwen3.5-122B agent by up to 57.65 absolute percentage points on WikiTableQuestions. Ultimately, our results demonstrate that complex agent experience can be packaged into highly transferable, declarative skills -- requiring no parameter updates, no external retrieval modules, and utilizing open-source models as small as 35B parameters.

------

Title: Memp: Exploring Agent Procedural Memory

URL: https://doi.org/10.48550/arXiv.2508.06433

Abstract: Large Language Models (LLMs) based agents excel at diverse tasks, yet they suffer from brittle procedural memory that is manually engineered or entangled in static parameters. In this work, we investigate strategies to endow agents with a learnable, updatable, and lifelong procedural memory. We propose Memp that distills past agent trajectories into both fine-grained, step-by-step instructions and higher-level, script-like abstractions, and explore the impact of different strategies for Build, Retrieval, and Update of procedural memory. Coupled with a dynamic regimen that continuously updates, corrects, and deprecates its contents, this repository evolves in lockstep with new experience. Empirical evaluation on TravelPlanner and ALFWorld shows that as the memory repository is refined, agents achieve steadily higher success rates and greater efficiency on analogous tasks. Moreover, procedural memory built from a stronger model retains its value: migrating the procedural memory to a weaker model can also yield substantial performance gains. Code is available at https://github.com/zjunlp/MemP.

------

Title: AgentDistill: Training-Free Agent Distillation with Generalizable MCP Boxes

URL: https://doi.org/10.48550/arXiv.2506.14728

Abstract: While knowledge distillation has become a mature field for compressing large language models (LLMs) into smaller ones by aligning their outputs or internal representations, the distillation of LLM-based agents, which involve planning, memory, and tool use, remains relatively underexplored. Existing agent distillation methods typically replay full teacher trajectories or imitate step-by-step teacher tool usage, but they often struggle to train student agents to dynamically plan and act in novel environments. We propose AgentDistill, a novel, training-free agent distillation framework that enables efficient and scalable knowledge transfer via direct reuse of Model-Context-Protocols (MCPs), which are structured and reusable task-solving modules autonomously generated by teacher agents. The reuse of these distilled MCPs enables student agents to generalize their capabilities across domains and solve new problems with minimal supervision or human intervention. Experiments on biomedical and mathematical benchmarks demonstrate that our distilled student agents, built on small language models, can achieve performance comparable to advanced systems using large LLMs such as OctoTools (GPT-4o), highlighting the effectiveness of our framework in building scalable and cost-efficient intelligent agents.

------

Title: AutoRefine: From Trajectories to Reusable Expertise for Continual LLM Agent Refinement

URL: https://doi.org/10.48550/arXiv.2601.22758

Abstract: Large language model agents often fail to accumulate knowledge from experience, treating each task as an independent challenge. Recent methods extract experience as flattened textual knowledge, which cannot capture procedural logic of complex subtasks. They also lack maintenance mechanisms, causing repository degradation as experience accumulates. We introduce AutoRefine, a framework that extracts and maintains dual-form Experience Patterns from agent execution histories. For procedural subtasks, we extract specialized subagents with independent reasoning and memory. For static knowledge, we extract skill patterns as guidelines or code snippets. A continuous maintenance mechanism scores, prunes, and merges patterns to prevent repository degradation. Evaluated on ALFWorld, ScienceWorld, and TravelPlanner, AutoRefine achieves 98.4%, 70.4%, and 27.1% respectively, with 20-73% step reductions. On TravelPlanner, automatic extraction exceeds manually designed systems (27.1% vs 12.1%), demonstrating its ability to capture procedural coordination.

------

Title: Skill-Pro: Learning Reusable Skills from Experience via Non-Parametric PPO for LLM Agents

URL: https://www.semanticscholar.org/paper/28f0b6f57e57337c7db267ae4ac52c12cbb5d376

Abstract: LLM-driven agents demonstrate strong performance in sequential decision-making but often rely on on-the-fly reasoning, re-deriving solutions even in recurring scenarios. This insufficient experience reuse leads to computational redundancy and execution instability. To bridge this gap, we propose Skill-Pro, a framework that enables agents to autonomously learn reusable procedural skills from interaction experiences without parameter updates. By formalizing a Skill-MDP, Skill-Pro transforms passive episodic narratives into executable Skills defined by activation, execution, and termination conditions to ensure executability. To achieve reliable reusability without capability degradation, we introduce Non-Parametric PPO, which leverages semantic gradients for high-quality candidate generation and a PPO Gate for robust Skill verification. Through score-based maintenance, Skill-Pro sustains compact, high-quality procedural memory. Experimental results across in-domain, cross-task, and cross-agent scenarios demonstrate that Skill-Pro achieves superior reuse rates and significant performance gains with extreme memory compression. Visualized evolutionary trajectories and Skill distributions further reveal how Skill-Pro transparently accumulates, refines, and reuses procedural knowledge to facilitate long-term autonomy.

------

Title: Compiled Memory: Not More Information, but More Precise Instructions for Language Agents

URL: https://www.semanticscholar.org/paper/62dc0a497a2643f06303a81ee1cb9d7e1167ae7a

Abstract: Existing memory systems for language agents address memory management: how to retrieve and page more information within a context budget. We address a complementary problem -- memory utility: what experience is worth keeping, and how it should change agent behavior. We present Atlas, a memory kernel that compiles accumulated task experience into an agent's instruction structure -- without fine-tuning, RAG, or human intervention. Memory is distillation, not storage; delivery is instruction rewriting, not context injection. Facts extracted from agent failures and successes are verified through a three-step promotion gate and delivered by rewriting the agent's system prompt with learned sub-bullets. On CUAD contract analysis, the evolved prompt improves GPT-4o token-level F1 by $+8.7$pp and precision by $+12.5$pp. On HotpotQA multi-hop QA, joint F1 improves $+3.16$pp. An ablation isolates the mechanism's defining property -- the training signal constraint: the evolved prompt learns exactly what it is taught, and nothing more. Applied to Claude Sonnet~4.5 using the same evolved prompt -- compiled from GPT-4o errors, unchanged -- joint F1 improves $+2.31$pp, with gains concentrating where Claude's stronger baseline leaves the most room -- confirming that the compiled knowledge is task-shaped, not model-shaped.

------

Title: Traversal-as-Policy: Log-Distilled Gated Behavior Trees as Externalized, Verifiable Policies for Safe, Robust, and Efficient Agents

URL: https://www.semanticscholar.org/paper/a4428f2803db336bca7f80a9e24e88110122d8cd

Abstract: Autonomous LLM agents fail because long-horizon policy remains implicit in model weights and transcripts, while safety is retrofitted post hoc. We propose Traversal-as-Policy: distill sandboxed OpenHands execution logs into a single executable Gated Behavior Tree (GBT) and treat tree traversal -- rather than unconstrained generation -- as the control policy whenever a task is in coverage. Each node encodes a state-conditioned action macro mined and merge-checked from successful trajectories; macros implicated by unsafe traces attach deterministic pre-execution gates over structured tool context and bounded history, updated under experience-grounded monotonicity so previously rejected unsafe contexts cannot be re-admitted. At runtime, a lightweight traverser matches the base model's intent to child macros, executes one macro at a time under global and node-local gating, and when stalled performs risk-aware shortest-path recovery to a feasible success leaf; the visited path forms a compact spine memory that replaces transcript replay. Evaluated in a unified OpenHands sandbox on 15+ software, web, reasoning, and safety/security benchmarks, GBT improves success while driving violations toward zero and reducing cost. On SWE-bench Verified (Protocol A, 500 issues), GBT-SE raises success from 34.6% to 73.6%, reduces violations from 2.8% to 0.2%, and cuts token/character usage from 208k/820k to 126k/490k; with the same distilled tree, 8B executors more than double success on SWE-bench Verified (14.0%58.8%) and WebArena (9.1%37.3%).

------

Title: SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning

URL: https://doi.org/10.48550/arXiv.2602.08234

Abstract: Large Language Model (LLM) agents have shown stunning results in complex tasks, yet they often operate in isolation, failing to learn from past experiences. Existing memory-based methods primarily store raw trajectories, which are often redundant and noise-heavy. This prevents agents from extracting high-level, reusable behavioral patterns that are essential for generalization. In this paper, we propose SkillRL, a framework that bridges the gap between raw experience and policy improvement through automatic skill discovery and recursive evolution. Our approach introduces an experience-based distillation mechanism to build a hierarchical skill library SkillBank, an adaptive retrieval strategy for general and task-specific heuristics, and a recursive evolution mechanism that allows the skill library to co-evolve with the agent's policy during reinforcement learning. These innovations significantly reduce the token footprint while enhancing reasoning utility. Experimental results on ALFWorld, WebShop and seven search-augmented tasks demonstrate that SkillRL achieves state-of-the-art performance, outperforming strong baselines over 15.3% and maintaining robustness as task complexity increases. Code is available at this https://github.com/aiming-lab/SkillRL.

------

Title: Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution

URL: https://doi.org/10.48550/arXiv.2512.10696

Abstract: Procedural memory enables large language model (LLM) agents to internalize"how-to"knowledge, theoretically reducing redundant trial-and-error. However, existing frameworks predominantly suffer from a"passive accumulation"paradigm, treating memory as a static append-only archive. To bridge the gap between static storage and dynamic reasoning, we propose $\textbf{ReMe}$ ($\textit{Remember Me, Refine Me}$), a comprehensive framework for experience-driven agent evolution. ReMe innovates across the memory lifecycle via three mechanisms: 1) $\textit{multi-faceted distillation}$, which extracts fine-grained experiences by recognizing success patterns, analyzing failure triggers and generating comparative insights; 2) $\textit{context-adaptive reuse}$, which tailors historical insights to new contexts via scenario-aware indexing; and 3) $\textit{utility-based refinement}$, which autonomously adds valid memories and prunes outdated ones to maintain a compact, high-quality experience pool. Extensive experiments on BFCL-V3 and AppWorld demonstrate that ReMe establishes a new state-of-the-art in agent memory system. Crucially, we observe a significant memory-scaling effect: Qwen3-8B equipped with ReMe outperforms larger, memoryless Qwen3-14B, suggesting that self-evolving memory provides a computation-efficient pathway for lifelong learning. We release our code and the $\texttt{reme.library}$ dataset to facilitate further research.

------

Title: Agent Workflow Memory

URL: https://doi.org/10.48550/arXiv.2409.07429

Abstract: Despite the potential of language model-based agents to solve real-world tasks such as web navigation, current methods still struggle with long-horizon tasks with complex action trajectories. In contrast, humans can flexibly solve complex tasks by learning reusable task workflows from past experiences and using them to guide future actions. To build agents that can similarly benefit from this process, we introduce Agent Workflow Memory (AWM), a method for inducing commonly reused routines, i.e., workflows, and selectively providing workflows to the agent to guide subsequent generations. AWM flexibly applies to both offline and online scenarios, where agents induce workflows from training examples beforehand or from test queries on the fly. We experiment on two major web navigation benchmarks -- Mind2Web and WebArena -- that collectively cover 1000+ tasks from 200+ domains across travel, shopping, and social media, among others. AWM substantially improves the baseline results by 24.6% and 51.1% relative success rate on Mind2Web and WebArena while reducing the number of steps taken to solve WebArena tasks successfully. Furthermore, online AWM robustly generalizes in cross-task, website, and domain evaluations, surpassing baselines from 8.9 to 14.0 absolute points as train-test task distribution gaps widen.

------

Title: Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models

URL: https://doi.org/10.48550/arXiv.2510.04618

Abstract: Large language model (LLM) applications such as agents and domain-specific reasoning increasingly rely on context adaptation: modifying inputs with instructions, strategies, or evidence, rather than weight updates. Prior approaches improve usability but often suffer from brevity bias, which drops domain insights for concise summaries, and from context collapse, where iterative rewriting erodes details over time. We introduce ACE (Agentic Context Engineering), a framework that treats contexts as evolving playbooks that accumulate, refine, and organize strategies through a modular process of generation, reflection, and curation. ACE prevents collapse with structured, incremental updates that preserve detailed knowledge and scale with long-context models. Across agent and domain-specific benchmarks, ACE optimizes contexts both offline (e.g., system prompts) and online (e.g., agent memory), consistently outperforming strong baselines: +10.6% on agents and +8.6% on finance, while significantly reducing adaptation latency and rollout cost. Notably, ACE could adapt effectively without labeled supervision and instead by leveraging natural execution feedback. On the AppWorld leaderboard, ACE matches the top-ranked production-level agent on the overall average and surpasses it on the harder test-challenge split, despite using a smaller open-source model. These results show that comprehensive, evolving contexts enable scalable, efficient, and self-improving LLM systems with low overhead.

------

Title: SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills

URL: https://doi.org/10.48550/arXiv.2504.07079

Abstract: To survive and thrive in complex environments, humans have evolved sophisticated self-improvement mechanisms through environment exploration, hierarchical abstraction of experiences into reuseable skills, and collaborative construction of an ever-growing skill repertoire. Despite recent advancements, autonomous web agents still lack crucial self-improvement capabilities, struggling with procedural knowledge abstraction, refining skills, and skill composition. In this work, we introduce SkillWeaver, a skill-centric framework enabling agents to self-improve by autonomously synthesizing reusable skills as APIs. Given a new website, the agent autonomously discovers skills, executes them for practice, and distills practice experiences into robust APIs. Iterative exploration continually expands a library of lightweight, plug-and-play APIs, significantly enhancing the agent's capabilities. Experiments on WebArena and real-world websites demonstrate the efficacy of SkillWeaver, achieving relative success rate improvements of 31.8% and 39.8%, respectively. Additionally, APIs synthesized by strong agents substantially enhance weaker agents through transferable skills, yielding improvements of up to 54.3% on WebArena. These results demonstrate the effectiveness of honing diverse website interactions into APIs, which can be seamlessly shared among various web agents.

------

Title: What Deserves Memory: Adaptive Memory Distillation for LLM Agents

URL: https://www.semanticscholar.org/paper/c7104ee40e801e802cdd6e85c26f1ca8dcc00b19

Abstract: Memory systems for LLM agents struggle to determine what information deserves retention. Existing approaches rely on predefined heuristics such as importance scores, emotional tags, or factual templates, encoding designer intuition rather than learning from the data itself. Inspired by cognitive ideas, we propose NEMORI, an adaptive memory distillation framework that casts the assessment of experience's future utility as a matter of predictability. Specifically, NEMORI comprises two cascading modules: Episodic Memory Integration transforms raw interactions into coherent narratives, and Semantic Knowledge Distillation extracts insights via prediction error. Centering on distillation, the framework remains agnostic to downstream management. Extensive experiments confirm that NEMORI achieves strong performance, efficiency, and storage reduction. Our work suggests that observing the intrinsic properties of interaction sequences offers a viable, data-driven alternative to heuristic-based memory design. Code: https://github.com/nemori-ai/nemori.

------

Title: Don't Retrieve, Navigate: Distilling Enterprise Knowledge into Navigable Agent Skills for QA and RAG

URL: https://www.semanticscholar.org/paper/7686a9b2f6c929591bbec8ff19029f14a070a620

Abstract: Retrieval-Augmented Generation (RAG) grounds LLM responses in external evidence but treats the model as a passive consumer of search results: it never sees how the corpus is organized or what it has not yet retrieved, limiting its ability to backtrack or combine scattered evidence. We present Corpus2Skill, which distills a document corpus into a hierarchical skill directory offline and lets an LLM agent navigate it at serve time. The compilation pipeline iteratively clusters documents, generates LLM-written summaries at each level, and materializes the result as a tree of navigable skill files. At serve time, the agent receives a bird's-eye view of the corpus, drills into topic branches via progressively finer summaries, and retrieves full documents by ID. Because the hierarchy is explicitly visible, the agent can reason about where to look, backtrack from unproductive paths, and combine evidence across branches. On WixQA, an enterprise customer-support benchmark for RAG, Corpus2Skill outperforms dense retrieval, RAPTOR, and agentic RAG baselines across all quality metrics. We further evaluate generalization on nine RAGBench subsets reformulated as retrieval-stress benchmarks: Corpus2Skill attains the highest macro-average F1 across the full 10-dataset suite and characterizes a clear regime -- single-domain, atomic-document corpora -- where corpus navigation is the right primitive, while flat retrieval remains preferable for open-domain or extractive pools.

------

Title: ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory

URL: https://doi.org/10.48550/arXiv.2509.25140

Abstract: With the growing adoption of large language model agents in persistent real-world roles, they naturally encounter continuous streams of tasks. A key limitation, however, is their failure to learn from the accumulated interaction history, forcing them to discard valuable insights and repeat past errors. We propose ReasoningBank, a novel memory framework that distills generalizable reasoning strategies from an agent's self-judged successful and failed experiences. At test time, an agent retrieves relevant memories from ReasoningBank to inform its interaction and then integrates new learnings back, enabling it to become more capable over time. Building on this powerful experience learner, we further introduce memory-aware test-time scaling (MaTTS), which accelerates and diversifies this learning process by scaling up the agent's interaction experience. By allocating more compute to each task, the agent generates abundant, diverse experiences that provide rich contrastive signals for synthesizing higher-quality memory. The better memory in turn guides more effective scaling, establishing a powerful synergy between memory and test-time scaling. Across web browsing and software engineering benchmarks, ReasoningBank consistently outperforms existing memory mechanisms that store raw trajectories or only successful task routines, improving both effectiveness and efficiency; MaTTS further amplifies these gains. These findings establish memory-driven experience scaling as a new scaling dimension, enabling agents to self-evolve with emergent behaviors naturally arise. Our code can be found at https://github.com/google-research/reasoning-bank.

------

Title: Inducing Programmatic Skills for Agentic Tasks

URL: https://doi.org/10.48550/arXiv.2504.06821

Abstract: To succeed in common digital tasks such as web navigation, agents must carry out a variety of specialized tasks such as searching for products or planning a travel route. To tackle these tasks, agents can bootstrap themselves by learning task-specific skills online through interaction with the web environment. In this work, we demonstrate that programs are an effective representation for skills. We propose agent skill induction (ASI), which allows agents to adapt themselves by inducing, verifying, and utilizing program-based skills on the fly. We start with an evaluation on the WebArena agent benchmark and show that ASI outperforms the static baseline agent and its text-skill counterpart by 23.5% and 11.3% in success rate, mainly thanks to the programmatic verification guarantee during the induction phase. ASI also improves efficiency by reducing 10.7-15.3% of the steps over baselines, by composing primitive actions (e.g., click) into higher-level skills (e.g., search product). We then highlight the efficacy of ASI in remaining efficient and accurate under scaled-up web activities. Finally, we examine the generalizability of induced skills when transferring between websites, and find that ASI can effectively reuse common skills, while also updating incompatible skills to versatile website changes.

------

Title: SCOPE: Prompt Evolution for Enhancing Agent Effectiveness

URL: https://doi.org/10.48550/arXiv.2512.15374

Abstract: Large Language Model (LLM) agents are increasingly deployed in environments that generate massive, dynamic contexts. However, a critical bottleneck remains: while agents have access to this context, their static prompts lack the mechanisms to manage it effectively, leading to recurring Corrective and Enhancement failures. To address this capability gap, we introduce \textbf{SCOPE} (Self-evolving Context Optimization via Prompt Evolution). SCOPE frames context management as an \textit{online optimization} problem, synthesizing guidelines from execution traces to automatically evolve the agent's prompt. We propose a Dual-Stream mechanism that balances tactical specificity (resolving immediate errors) with strategic generality (evolving long-term principles). Furthermore, we introduce Perspective-Driven Exploration to maximize strategy coverage, increasing the likelihood that the agent has the correct strategy for any given task. Experiments on the HLE benchmark show that SCOPE improves task success rates from 14.23\% to 38.64\% without human intervention. We make our code publicly available at https://github.com/JarvisPei/SCOPE.

------

Title: FLEX: Continuous Agent Evolution via Forward Learning from Experience

URL: https://doi.org/10.48550/arXiv.2511.06449

Abstract: Autonomous agents driven by Large Language Models (LLMs) have revolutionized reasoning and problem-solving but remain static after training, unable to grow with experience as intelligent beings do during deployment. We introduce Forward Learning with EXperience (FLEX), a gradient-free learning paradigm that enables LLM agents to continuously evolve through accumulated experience. Specifically, FLEX cultivates scalable and inheritable evolution by constructing a structured experience library through continual reflection on successes and failures during interaction with the environment. FLEX delivers substantial improvements on mathematical reasoning, chemical retrosynthesis, and protein fitness prediction (up to 23% on AIME25, 10% on USPTO50k, and 14% on ProteinGym). We further identify a clear scaling law of experiential growth and the phenomenon of experience inheritance across agents, marking a step toward scalable and inheritable continuous agent evolution. Project Page: https://flex-gensi-thuair.github.io.

------

Title: Learning on the Job: An Experience-Driven Self-Evolving Agent for Long-Horizon Tasks

URL: https://doi.org/10.48550/arXiv.2510.08002

Abstract: Large Language Models have demonstrated remarkable capabilities across diverse domains, yet significant challenges persist when deploying them as AI agents for real-world long-horizon tasks. Existing LLM agents suffer from a critical limitation: they are test-time static and cannot learn from experience, lacking the ability to accumulate knowledge and continuously improve on the job. To address this challenge, we propose MUSE, a novel agent framework that introduces an experience-driven, self-evolving system centered around a hierarchical Memory Module. MUSE organizes diverse levels of experience and leverages them to plan and execute long-horizon tasks across multiple applications. After each sub-task execution, the agent autonomously reflects on its trajectory, converting the raw trajectory into structured experience and integrating it back into the Memory Module. This mechanism enables the agent to evolve beyond its static pretrained parameters, fostering continuous learning and self-evolution. We evaluate MUSE on the long-horizon productivity benchmark TAC. It achieves new SOTA performance by a significant margin using only a lightweight Gemini-2.5 Flash model. Sufficient Experiments demonstrate that as the agent autonomously accumulates experience, it exhibits increasingly superior task completion capabilities, as well as robust continuous learning and self-evolution capabilities. Moreover, the accumulated experience from MUSE exhibits strong generalization properties, enabling zero-shot improvement on new tasks. MUSE establishes a new paradigm for AI agents capable of real-world productivity task automation.

------

Title: AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials

URL: https://doi.org/10.48550/arXiv.2412.09605

Abstract: Graphical User Interface (GUI) agents can automate complex tasks across digital environments, but their development is hindered by the scarcity of high-quality trajectory data for training. Existing approaches rely on expensive human annotation, making them unsustainable at scale. We propose AgentTrek, a scalable data synthesis pipeline that generates web agent trajectories by leveraging publicly available tutorials. Our three-stage method: (1) automatically harvests and filters tutorial-like texts from the internet using a specialized classification model, (2) transforms these texts into structured task specifications with step-by-step instructions, and (3) employs a visual-language model (VLM) agent to execute these instructions in real environments, while a VLM-based evaluator verifies trajectory correctness. The synthesized trajectories encompass multiple modalities, including text-based HTML observations with function-calling API actions, and vision-based screenshot observations with pixel-level actions. This multimodal data, enriched with chain-of-thought reasoning, enables agents to achieve state-of-the-art performance on both textual web browsing benchmarks (e.g., WebArena) and visual web grounding and browsing benchmarks (e.g., ScreenSpot Web and Multimodal Mind2Web). Furthermore, our fully automated approach significantly reduces data collection costs, achieving a cost of just $0.55 per high-quality trajectory without human annotators. Our work demonstrates that guided replay using web tutorials is a practical and scalable strategy for training advanced GUI agents, paving the way for more capable and autonomous digital assistants.

------

Title: Get Experience from Practice: LLM Agents with Record & Replay

URL: https://doi.org/10.48550/arXiv.2505.17716

Abstract: AI agents, empowered by Large Language Models (LLMs) and communication protocols such as MCP and A2A, have rapidly evolved from simple chatbots to autonomous entities capable of executing complex, multi-step tasks, demonstrating great potential. However, the LLMs' inherent uncertainty and heavy computational resource requirements pose four significant challenges to the development of safe and efficient agents: reliability, privacy, cost and performance. Existing approaches, like model alignment, workflow constraints and on-device model deployment, can partially alleviate some issues but often with limitations, failing to fundamentally resolve these challenges. This paper proposes a new paradigm called AgentRR (Agent Record&Replay), which introduces the classical record-and-replay mechanism into AI agent frameworks. The core idea is to: 1. Record an agent's interaction trace with its environment and internal decision process during task execution, 2. Summarize this trace into a structured"experience"encapsulating the workflow and constraints, and 3. Replay these experiences in subsequent similar tasks to guide the agent's behavior. We detail a multi-level experience abstraction method and a check function mechanism in AgentRR: the former balances experience specificity and generality, while the latter serves as a trust anchor to ensure completeness and safety during replay. In addition, we explore multiple application modes of AgentRR, including user-recorded task demonstration, large-small model collaboration and privacy-aware agent execution, and envision an experience repository for sharing and reusing knowledge to further reduce deployment cost.

------

Title: Explorer: Scaling Exploration-driven Web Trajectory Synthesis for Multimodal Web Agents

URL: https://doi.org/10.48550/arXiv.2502.11357

Abstract: Recent success in large multimodal models (LMMs) has sparked promising applications of agents capable of autonomously completing complex web tasks. While open-source LMM agents have made significant advances in offline evaluation benchmarks, their performance still falls substantially short of human-level capabilities in more realistic online settings. A key bottleneck is the lack of diverse and large-scale trajectory-level datasets across various domains, which are expensive to collect. In this paper, we address this challenge by developing a scalable recipe to synthesize the largest and most diverse trajectory-level dataset to date, containing over 94K successful multimodal web trajectories, spanning 49K unique URLs, 720K screenshots, and 33M web elements. In particular, we leverage extensive web exploration and refinement to obtain diverse task intents. The average cost is 28 cents per successful trajectory, making it affordable to a wide range of users in the community. Leveraging this dataset, we train Explorer, a multimodal web agent, and demonstrate strong performance on both offline and online web agent benchmarks such as Mind2Web-Live, Multimodal-Mind2Web, and MiniWob++. Additionally, our experiments highlight data scaling as a key driver for improving web agent capabilities. We hope this study makes state-of-the-art LMM-based agent research at a larger scale more accessible.

------

Title: Contextual Experience Replay for Self-Improvement of Language Agents

URL: https://doi.org/10.48550/arXiv.2506.06698

Abstract: Large language model (LLM) agents have been applied to sequential decision-making tasks such as web navigation, but without any environment-specific experiences, they often fail in these complex tasks. Moreover, current LLM agents are not designed to continually learn from past experiences during inference time, which could be crucial for them to gain these environment-specific experiences. To address this, we propose Contextual Experience Replay (CER), a training-free framework to enable efficient self-improvement for language agents in their context window. Specifically, CER accumulates and synthesizes past experiences into a dynamic memory buffer. These experiences encompass environment dynamics and common decision-making patterns, allowing the agents to retrieve and augment themselves with relevant knowledge in new tasks, enhancing their adaptability in complex environments. We evaluate CER on the challenging WebArena and VisualWebArena benchmarks. On VisualWebArena, CER achieves a competitive performance of 31.9%. On WebArena, CER also gets a competitive average success rate of 36.7%, relatively improving the success rate of the GPT-4o agent baseline by 51.0%. We also conduct a comprehensive analysis on it to prove its efficiency, validity and understand it better.

------

Title: Towards Internet-Scale Training For Agents

URL: https://doi.org/10.48550/arXiv.2502.06776

Abstract: The predominant approach for training web navigation agents is to gather human demonstrations for a set of popular websites and hand-written tasks, but it is becoming clear that human data is an inefficient resource. We develop a pipeline to facilitate internet-scale training for agents without laborious human annotations. In the first stage, an LLM annotates 150k sites with agentic tasks. In the next stage, LLM agents complete tasks and produce trajectories. In the final stage, an LLM filters trajectories by judging their success. Language models are powerful data curation tools, identifying harmful content with an accuracy of 97%, judging successful trajectories with an accuracy of 82.6%, and producing effective data. We train agents based on Qwen 3 1.7B that are competitive with frontier LLMs as web agents, while being smaller and faster. Our top agent reaches a success rate of 56.9%, outperforming the data collection policy Qwen 3 235B, a 235 times larger Llama 4 Maverick, and reaching 94.7% of the performance of Gemini 2.5 Flash. We are releasing code, models and data at: https://data-for-agents.github.io.

------

Title: RAGShaper: Eliciting Sophisticated Agentic RAG Skills via Automated Data Synthesis

URL: https://doi.org/10.48550/arXiv.2601.08699

Abstract: Agentic Retrieval-Augmented Generation (RAG) empowers large language models to autonomously plan and retrieve information for complex problem-solving. However, the development of robust agents is hindered by the scarcity of high-quality training data that reflects the noise and complexity of real-world retrieval environments. Conventional manual annotation is unscalable and often fails to capture the dynamic reasoning strategies required to handle retrieval failures. To bridge this gap, we introduce RAGShaper, a novel data synthesis framework designed to automate the construction of RAG tasks and robust agent trajectories. RAGShaper incorporates an InfoCurator to build dense information trees enriched with adversarial distractors spanning Perception and Cognition levels. Furthermore, we propose a constrained navigation strategy that forces a teacher agent to confront these distractors, thereby eliciting trajectories that explicitly demonstrate error correction and noise rejection. Comprehensive experiments confirm that models trained on our synthesized corpus significantly outperform existing baselines, exhibiting superior robustness in noise-intensive and complex retrieval tasks.

------

Title: Structured Distillation of Web Agent Capabilities Enables Generalization

URL: https://www.semanticscholar.org/paper/be1b1c3582da7646cc6269ef2f1f9ce44bc192b3

Abstract: Frontier LLMs can navigate complex websites, but their cost and reliance on third-party APIs make local deployment impractical. We introduce Agent-as-Annotators, a framework that structures synthetic trajectory generation for web agents by analogy to human annotation roles, replacing the Task Designer, Annotator, and Supervisor with modular LLM components. Using Gemini 3 Pro as teacher, we generate 3,000 trajectories across six web environments and fine-tune a 9B-parameter student with pure supervised learning on the 2,322 that pass quality filtering. The resulting model achieves 41.5% on WebArena, surpassing closed-source models such as Claude 3.5 Sonnet (36.0%) and GPT-4o (31.5%) under the same evaluation protocol, and nearly doubling the previous best open-weight result (Go-Browse, 21.7%). Capabilities transfer to unseen environments, with an 18.2 percentage point gain on WorkArena L1 (an enterprise platform never seen during training) and consistent improvements across three additional benchmarks. Ablations confirm that each pipeline component contributes meaningfully, with Judge filtering, evaluation hints, and reasoning traces each accounting for measurable gains. These results demonstrate that structured trajectory synthesis from a single frontier teacher is sufficient to produce competitive, locally deployable web agents. Project page: https://agent-as-annotators.github.io

------

Title: Meta-Policy Reflexion: Reusable Reflective Memory and Rule Admissibility for Resource-Efficient LLM Agent

URL: https://doi.org/10.48550/arXiv.2509.03990

Abstract: Large language model (LLM) agents achieve impressive single-task performance but commonly exhibit repeated failures, inefficient exploration, and limited cross-task adaptability. Existing reflective strategies (e.g., Reflexion, ReAct) improve per-episode behavior but typically produce ephemeral, task-specific traces that are not reused across tasks. Reinforcement-learning based alternatives can produce transferable policies but require substantial parameter updates and compute. In this work we introduce Meta-Policy Reflexion (MPR): a hybrid framework that consolidates LLM-generated reflections into a structured, predicate-like Meta-Policy Memory (MPM) and applies that memory at inference time through two complementary mechanisms soft memory-guided decoding and hard rule admissibility checks(HAC). MPR (i) externalizes reusable corrective knowledge without model weight updates, (ii) enforces domain constraints to reduce unsafe or invalid actions, and (iii) retains the adaptability of language-based reflection. We formalize the MPM representation, present algorithms for update and decoding, and validate the approach in a text-based agent environment following the experimental protocol described in the provided implementation (AlfWorld-based). Empirical results reported in the supplied material indicate consistent gains in execution accuracy and robustness when compared to Reflexion baselines; rule admissibility further improves stability. We analyze mechanisms that explain these gains, discuss scalability and failure modes, and outline future directions for multimodal and multi-agent extensions.

------

Title: WebXSkill: Skill Learning for Autonomous Web Agents

URL: https://www.semanticscholar.org/paper/f283b199100a8d976d1f3b6a8561f7597c6a068e

Abstract: Autonomous web agents powered by large language models (LLMs) have shown promise in completing complex browser tasks, yet they still struggle with long-horizon workflows. A key bottleneck is the grounding gap in existing skill formulations: textual workflow skills provide natural language guidance but cannot be directly executed, while code-based skills are executable but opaque to the agent, offering no step-level understanding for error recovery or adaptation. We introduce WebXSkill, a framework that bridges this gap with executable skills, each pairing a parameterized action program with step-level natural language guidance, enabling both direct execution and agent-driven adaptation. WebXSkill operates in three stages: skill extraction mines reusable action subsequences from readily available synthetic agent trajectories and abstracts them into parameterized skills, skill organization indexes skills into a URL-based graph for context-aware retrieval, and skill deployment exposes two complementary modes, grounded mode for fully automated multi-step execution and guided mode where skills serve as step-by-step instructions that the agent follows with its native planning. On WebArena and WebVoyager, WebXSkill improves task success rate by up to 9.8 and 12.9 points over the baseline, respectively, demonstrating the effectiveness of executable skills for web agents. The code is publicly available at https://github.com/aiming-lab/WebXSkill.

------

Title: XSkill: Continual Learning from Experience and Skills in Multimodal Agents

URL: https://www.semanticscholar.org/paper/b94a18aa9d6117e602cf45485260ca16936a760b

Abstract: Multimodal agents can now tackle complex reasoning tasks with diverse tools, yet they still suffer from inefficient tool use and inflexible orchestration in open-ended settings. A central challenge is enabling such agents to continually improve without parameter updates by learning from past trajectories. We identify two complementary forms of reusable knowledge essential for this goal: experiences, providing concise action-level guidance for tool selection and decision making, and skills, providing structured task-level guidance for planning and tool use. To this end, we propose XSkill, a dual-stream framework for continual learning from experience and skills in multimodal agents. XSkill grounds both knowledge extraction and retrieval in visual observations. During accumulation, XSkill distills and consolidates experiences and skills from multi-path rollouts via visually grounded summarization and cross-rollout critique. During inference, it retrieves and adapts this knowledge to the current visual context and feeds usage history back into accumulation to form a continual learning loop. Evaluated on five benchmarks across diverse domains with four backbone models, XSkill consistently and substantially outperforms both tool-only and learning-based baselines. Further analysis reveals that the two knowledge streams play complementary roles in influencing the reasoning behaviors of agents and show superior zero-shot generalization.

------

Title: CLIN: A Continually Learning Language Agent for Rapid Task Adaptation and Generalization

URL: https://doi.org/10.48550/arXiv.2310.10134

Abstract: Language agents have shown some ability to interact with an external environment, e.g., a virtual world such as ScienceWorld, to perform complex tasks, e.g., growing a plant, without the startup costs of reinforcement learning. However, despite their zero-shot capabilities, these agents to date do not continually improve over time beyond performance refinement on a specific task. Here we present CLIN, the first language-based agent to achieve this, so that it continually improves over multiple trials, including when both the environment and task are varied, and without requiring parameter updates. Our approach is to use a persistent, dynamic, textual memory centered on causal abstractions (rather than general"helpful hints") that is regularly updated after each trial so that the agent gradually learns useful knowledge for new trials. In the ScienceWorld benchmark, CLIN is able to continually improve on repeated trials on the same task and environment, outperforming state-of-the-art reflective language agents like Reflexion by 23 absolute points. CLIN can also transfer its learning to new environments (or new tasks), improving its zero-shot performance by 4 points (13 for new tasks) and can further improve performance there through continual memory updates, enhancing performance by an additional 17 points (7 for new tasks). This suggests a new architecture for agents built on frozen models that can still continually and rapidly improve over time.

------

Title: Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks

URL: https://doi.org/10.48550/arXiv.2501.11733

Abstract: Smartphones have become indispensable in modern life, yet navigating complex tasks on mobile devices often remains frustrating. Recent advancements in large multimodal model (LMM)-based mobile agents have demonstrated the ability to perceive and act in mobile environments. However, current approaches face significant limitations: they fall short in addressing real-world human needs, struggle with reasoning-intensive and long-horizon tasks, and lack mechanisms to learn and improve from prior experiences. To overcome these challenges, we introduce Mobile-Agent-E, a hierarchical multi-agent framework capable of self-evolution through past experience. By hierarchical, we mean an explicit separation of high-level planning and low-level action execution. The framework comprises a Manager, responsible for devising overall plans by breaking down complex tasks into subgoals, and four subordinate agents--Perceptor, Operator, Action Reflector, and Notetaker--which handle fine-grained visual perception, immediate action execution, error verification, and information aggregation, respectively. Mobile-Agent-E also features a novel self-evolution module which maintains a persistent long-term memory comprising Tips and Shortcuts. Tips are general guidance and lessons learned from prior tasks on how to effectively interact with the environment. Shortcuts are reusable, executable sequences of atomic operations tailored for specific subroutines. The inclusion of Tips and Shortcuts facilitates continuous refinement in performance and efficiency. Alongside this framework, we introduce Mobile-Eval-E, a new benchmark featuring complex mobile tasks requiring long-horizon, multi-app interactions. Empirical results show that Mobile-Agent-E achieves a 22% absolute improvement over previous state-of-the-art approaches across three foundation model backbones. Project page: https://x-plug.github.io/MobileAgent.

------

Title: TOUCAN: Synthesizing 1.5M Tool-Agentic Data from Real-World MCP Environments

URL: https://doi.org/10.48550/arXiv.2510.01179

Abstract: Large Language Model (LLM) agents are rapidly emerging as powerful systems for automating tasks across domains. Yet progress in the open-source community is constrained by the lack of high quality permissively licensed tool-agentic training data. Existing datasets are often limited in diversity, realism, and complexity, particularly regarding multi-tool and multi-turn interactions. To address this gap, we introduce Toucan, the largest publicly available tool-agentic dataset to date, containing 1.5 million trajectories synthesized from nearly 500 real-world Model Context Protocols (MCPs). Unlike prior work, Toucan leverages authentic MCP environments to generate diverse, realistic, and challenging tasks with trajectories involving real tool execution. Our pipeline first produces a broad spectrum of tool-use queries using five distinct models, applies model-based quality filtering, and then generates agentic trajectories with three teacher models using two agentic frameworks. Rigorous rule-based and model-based validation ensures high-quality outputs. We also introduce three extension mechanisms to further diversify tasks and simulate multi-turn conversations. Models fine-tuned on Toucan outperform larger closed-source counterparts on the BFCL V3 benchmark and push the Pareto frontier forward on MCP-Universe Bench.

------

Title: SkillDroid: Compile Once, Reuse Forever

URL: https://www.semanticscholar.org/paper/00521bfc64e3c426ed4d287bc477ff1b3e47411a

Abstract: LLM-based mobile GUI agents treat every task invocation as an independent reasoning episode, requiring a full LLM inference call at each action step. This per-step dependence makes them stateless: a task completed successfully yesterday is re-derived from scratch today, with no improvement in reliability or speed. We present SkillDroid, a three-layer skill agent that compiles successful LLM-guided GUI trajectories into parameterized skill templates (sequences of UI actions with weighted element locators and typed parameter slots) and replays them on future invocations without any LLM calls. A matching cascade (regex patterns, embedding similarity, and app filtering) routes incoming instructions to stored skills, while a failure-learning layer triggers recompilation when skill reliability degrades. Over a 150-round longitudinal evaluation with systematic instruction variation and controlled perturbations, SkillDroid achieves an 85.3% success rate (23 percentage points above a stateless LLM baseline) while using 49% fewer LLM calls. The skill replay mechanism achieves a perfect 1000% success rate across 79 replay rounds at 2.4 times the speed of full LLM execution. Most critically, the system improves with use: its success rate converges upward from 87% to 91%, while the baseline degrades from 80% to 44%.

------

Title: G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems

URL: https://doi.org/10.48550/arXiv.2506.07398

Abstract: Large language model (LLM)-powered multi-agent systems (MAS) have demonstrated cognitive and execution capabilities that far exceed those of single LLM agents, yet their capacity for self-evolution remains hampered by underdeveloped memory architectures. Upon close inspection, we are alarmed to discover that prevailing MAS memory mechanisms (1) are overly simplistic, completely disregarding the nuanced inter-agent collaboration trajectories, and (2) lack cross-trial and agent-specific customization, in stark contrast to the expressive memory developed for single agents. To bridge this gap, we introduce G-Memory, a hierarchical, agentic memory system for MAS inspired by organizational memory theory, which manages the lengthy MAS interaction via a three-tier graph hierarchy: insight, query, and interaction graphs. Upon receiving a new user query, G-Memory performs bi-directional memory traversal to retrieve both $\textit{high-level, generalizable insights}$ that enable the system to leverage cross-trial knowledge, and $\textit{fine-grained, condensed interaction trajectories}$ that compactly encode prior collaboration experiences. Upon task execution, the entire hierarchy evolves by assimilating new collaborative trajectories, nurturing the progressive evolution of agent teams. Extensive experiments across five benchmarks, three LLM backbones, and three popular MAS frameworks demonstrate that G-Memory improves success rates in embodied action and accuracy in knowledge QA by up to $20.89\%$ and $10.12\%$, respectively, without any modifications to the original frameworks. Our codes are available at https://github.com/bingreeky/GMemory.

------

Title: Steve-Evolving: Open-World Embodied Self-Evolution via Fine-Grained Diagnosis and Dual-Track Knowledge Distillation

URL: https://www.semanticscholar.org/paper/8b9d264fab816c9bbcbe6930f81fbabf18bdf9c7

Abstract: Open-world embodied agents must solve long-horizon tasks where the main bottleneck is not single-step planning quality but how interaction experience is organized and evolved. To this end, we present Steve-Evolving, a non-parametric self-evolving framework that tightly couples fine-grained execution diagnosis with dual-track knowledge distillation in a closed loop. The method follows three phases: Experience Anchoring, Experience Distillation, and Knowledge-Driven Closed-Loop Control. In detail, Experience Anchoring solidifies each subgoal attempt into a structured experience tuple with a fixed schema (pre-state, action, diagnosis-result, and post-state) and organizes it in a three-tier experience space with multi-dimensional indices (e.g., condition signatures, spatial hashing, and semantic tags) plus rolling summarization for efficient and auditable recall. To ensure sufficient information density for attribution, the execution layer provides compositional diagnosis signals beyond binary outcomes, including state-difference summaries, enumerated failure causes, continuous indicators, and stagnation/loop detection. Moreover, successful trajectories of Experience Distillation are generalized into reusable skills with explicit preconditions and verification criteria, while failures are distilled into executable guardrails that capture root causes and forbid risky operations at both subgoal and task granularities. Besides, Knowledge-Driven Closed-Loop Control retrieved skills and guardrails are injected into an LLM planner, and diagnosis-triggered local replanning updates the active constraints online, forming a continual evolution process without any model parameter updates. Experiments on the long-horizon suite of Minecraft MCU demonstrate consistent improvements over static-retrieval baselines.

------

Title: M2: Dual-Memory Augmentation for Long-Horizon Web Agents via Trajectory Summarization and Insight Retrieval

URL: https://doi.org/10.48550/arXiv.2603.00503

Abstract: Multimodal Large Language Models (MLLMs) based agents have demonstrated remarkable potential in autonomous web navigation. However, handling long-horizon tasks remains a critical bottleneck. Prevailing strategies often rely heavily on extensive data collection and model training, yet still struggle with high computational costs and insufficient reasoning capabilities when facing complex, long-horizon scenarios. To address this, we propose M$^2$, a training-free, memory-augmented framework designed to optimize context efficiency and decision-making robustness. Our approach incorporates a dual-tier memory mechanism that synergizes Dynamic Trajectory Summarization (Internal Memory) to compress verbose interaction history into concise state updates, and Insight Retrieval Augmentation (External Memory) to guide the agent with actionable guidelines retrieved from an offline insight bank. Extensive evaluations across WebVoyager and OnlineMind2Web demonstrate that M$^2$ consistently surpasses baselines, yielding up to a 19.6% success rate increase and 58.7% token reduction for Qwen3-VL-32B, while proprietary models like Claude achieve accuracy gains up to 12.5% alongside significantly lower computational overhead.

------

Title: APEX-EM: Non-Parametric Online Learning for Autonomous Agents via Structured Procedural-Episodic Experience Replay

URL: https://www.semanticscholar.org/paper/16c110756c0f0395fe9cc9568434d9e5621cd464

Abstract: LLM-based autonomous agents lack persistent procedural memory: they re-derive solutions from scratch even when structurally identical tasks have been solved before. We present APEX-EM, a non-parametric online learning framework that accumulates, retrieves, and reuses structured procedural plans without modifying model weights. APEX-EM introduces: (1) a structured experience representation encoding the full procedural-episodic trace of each execution -- planning steps, artifacts, iteration history with error analysis, and quality scores; (2) a Plan-Retrieve-Generate-Iterate-Ingest (PRGII) workflow with Task Verifiers providing multi-dimensional reward signals; and (3) a dual-outcome Experience Memory with hybrid retrieval combining semantic search, structural signature matching, and plan DAG traversal -- enabling cross-domain transfer between tasks sharing no lexical overlap but analogous operational structure. Successful experiences serve as positive in-context examples; failures as negative examples with structured error annotations. We evaluate on BigCodeBench, KGQAGen-10k, and Humanity's Last Exam using Claude Sonnet 4.5 and Opus 4.5. On KGQAGen-10k, APEX-EM achieves 89.6% accuracy versus 41.3% without memory (+48.3pp), surpassing the oracle-retrieval upper bound (84.9%). On BigCodeBench, it reaches 83.3% SR from a 53.9% baseline (+29.4pp), exceeding MemRL's +11.0pp gain under comparable frozen-backbone conditions (noting backbone differences controlled for in our analysis). On HLE, entity graph retrieval reaches 48.0% from 25.2% (+22.8pp). Ablations show component value is task-dependent: rich judge feedback is negligible for code generation but critical for structured queries (+10.3pp), while binary-signal iteration partially compensates for weaker feedback.

------

Title: Reflexion: language agents with verbal reinforcement learning

URL: https://doi.org/10.52202/075280-0377

Abstract: Large language models (LLMs) have been increasingly used to interact with external environments (e.g., games, compilers, APIs) as goal-driven agents. However, it remains challenging for these language agents to quickly and efficiently learn from trial-and-error as traditional reinforcement learning methods require extensive training samples and expensive model fine-tuning. We propose Reflexion, a novel framework to reinforce language agents not by updating weights, but instead through linguistic feedback. Concretely, Reflexion agents verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer to induce better decision-making in subsequent trials. Reflexion is flexible enough to incorporate various types (scalar values or free-form language) and sources (external or internally simulated) of feedback signals, and obtains significant improvements over a baseline agent across diverse tasks (sequential decision-making, coding, language reasoning). For example, Reflexion achieves a 91% pass@1 accuracy on the HumanEval coding benchmark, surpassing the previous state-of-the-art GPT-4 that achieves 80%. We also conduct ablation and analysis studies using different feedback signals, feedback incorporation methods, and agent types, and provide insights into how they affect performance.

------

Title: Evolving Programmatic Skill Networks

URL: https://doi.org/10.48550/arXiv.2601.03509

Abstract: We study continual skill acquisition in open-ended embodied environments where an agent must construct, refine, and reuse an expanding library of executable skills. We introduce the Programmatic Skill Network (PSN), a framework in which skills are executable symbolic programs forming a compositional network that evolves through experience. PSN defines three core mechanisms instantiated via large language models: (1)REFLECT for structured fault localization over skill compositions, (2) progressive optimization with maturity-aware update gating that stabilizes reliable skills while maintaining plasticity for uncertain ones, and (3) canonical structural refactoring under rollback validation that maintains network compactness. We further show that PSN's learning dynamics exhibit structural parallels to neural network training. Experiments on MineDojo and Crafter demonstrate robust skill reuse, rapid adaptation, and strong generalization across open-ended task distributions.\footnote{We plan to open-source the code.

------

Title: From Evidence to Trajectory: Abductive Reasoning Path Synthesis for Training Retrieval-Augmented Generation Agents

URL: https://doi.org/10.48550/arXiv.2509.23071

Abstract: Retrieval-augmented generation agents development is hindered by the lack of process-level supervision to effectively guide agentic capabilities like task decomposition, retriever invocation, and stepwise decision-making. While reinforcement learning offers a potential solution, it suffers from sparse rewards and the limited reasoning capabilities of large language models (LLMs). Meanwhile, existing data synthesis methods only produce chain-of-thought rationales and fail to model environmental interactions. In this paper, we propose EviPath, an evidence-anchored reasoning path synthesis paradigm for RAG agent development. EviPath comprises: (i) Abductive Subtask Planning, which decomposes the problem into sub-questions and iteratively plans an optimal solution path based on the dependencies between them; (ii) Faithful Sub-question Answering, which uses supporting evidence to construct a proxy environment to generate reasoning thoughts and answers for each sub-question; and (iii) Conversational Fine-Tuning, which formats the complete agent-environment interaction trajectory into a dialogue format suitable for Supervised Fine-Tuning. EviPath allows LLMs to learn complex reasoning and tool-use capabilities directly from synthesized data. Extensive experiments on widely-used question-answering benchmarks show that an 8B parameter model trained with EviPath-synthesized data significantly and consistently outperforms state-of-the-art baselines with a double-digit absolute EM gain of 14.7% in open-domain question answering.

------

Title: Distilling LLM Agent into Small Models with Retrieval and Code Tools

URL: https://doi.org/10.48550/arXiv.2505.17612

Abstract: Large language models (LLMs) excel at complex reasoning tasks but remain computationally expensive, limiting their practical deployment. To address this, recent works have focused on distilling reasoning capabilities into smaller language models (sLMs) using chain-of-thought (CoT) traces from teacher LLMs. However, this approach struggles in scenarios requiring rare factual knowledge or precise computation, where sLMs often hallucinate due to limited capability. In this work, we propose Agent Distillation, a framework for transferring not only reasoning capability but full task-solving behavior from LLM-based agents into sLMs with retrieval and code tools. We improve agent distillation along two complementary axes: (1) we introduce a prompting method called first-thought prefix to enhance the quality of teacher-generated trajectories; and (2) we propose a self-consistent action generation for improving test-time robustness of small agents. We evaluate our method on eight reasoning tasks across factual and mathematical domains, covering both in-domain and out-of-domain generalization. Our results show that sLMs as small as 0.5B, 1.5B, 3B parameters can achieve performance competitive with next-tier larger 1.5B, 3B, 7B models fine-tuned using CoT distillation, demonstrating the potential of agent distillation for building practical, tool-using small agents. Our code is available at https://github.com/Nardien/agent-distillation.

------

Title: NNetNav: Unsupervised Learning of Browser Agents Through Environment Interaction in the Wild

URL: https://www.semanticscholar.org/paper/5115942664d75d29f9f2814d89211af6a169ab05

Abstract: We introduce NNetNav, a method for unsupervised interaction with websites that generates synthetic demonstrations for training browser agents. Given any website, NNetNav produces these demonstrations by retroactively labeling action sequences from an exploration policy. Most work on training browser agents has relied on expensive human supervision, and the limited prior work on such interaction-based techniques has failed to provide effective search through the exponentially large space of exploration. In contrast, NNetNav exploits the hierarchical structure of language instructions to make this search more tractable: Complex instructions are typically decomposable into simpler sub-tasks, allowing NNetNav to automatically prune interaction episodes when an intermediate trajectory cannot be annotated with a meaningful sub-task. \texttt{LLama-3.1-8b} finetuned on 10k NNetNav self-generated demonstrations obtains over 16\% success rate on WebArena, and 35\% on WebVoyager, an improvement of 15pts and 31pts respectively over zero-shot \texttt{LLama-3.1-8b}, outperforming zero-shot GPT-4 and reaching the state-of-the-art among unsupervised methods, for both benchmarks.

------

Title: TimeWarp: Evaluating Web Agents by Revisiting the Past

URL: https://www.semanticscholar.org/paper/70ed2206985e79f642cb82f575bb9a9e1aed22aa

Abstract: The improvement of web agents on current benchmarks raises the question: Do today's agents perform just as well when the web changes? We introduce TimeWarp, a benchmark that emulates the evolving web using containerized environments that vary in UI, design, and layout. TimeWarp consists of three web environments, each with six UI versions spanning different eras of the internet, paired with a set of complex, realistic tasks requiring different forms of web navigation. Our experiments reveal web agents'vulnerability to changes and the limitations of behavior cloning (BC) on single-version trajectories. To address this, we propose TimeTraj, a simple yet effective algorithm that uses plan distillation to collect trajectories across multiple versions. By training agents on teacher rollouts using our BC-variant, we achieve substantial performance gains: $20.4\%\rightarrow37.7\%$ for Qwen-3 4B and $0\%\rightarrow27.0\%$ for Llama-3.1 8B models. We hope our work helps researchers study generalization across web designs and unlock a new paradigm for collecting plans rather than trajectories, thereby improving the robustness of web agents.

------

Title: SKILLFOUNDRY: Building Self-Evolving Agent Skill Libraries from Heterogeneous Scientific Resources

URL: https://www.semanticscholar.org/paper/a372a0c0b139f8ee62c0926d3c1014c92f4d0e06

Abstract: Modern scientific ecosystems are rich in procedural knowledge across repositories, APIs, scripts, notebooks, documentation, databases, and papers, yet much of this knowledge remains fragmented across heterogeneous artifacts that agents cannot readily operationalize. This gap between abundant scientific know-how and usable agent capabilities is a key bottleneck for building effective scientific agents. We present SkillFoundry, a self-evolving framework that converts such resources into validated agent skills, reusable packages that encode task scope, inputs and outputs, execution steps, environment assumptions, provenance, and tests. SkillFoundry organizes a target domain as a domain knowledge tree, mines resources from high-value branches, extracts operational contracts, compiles them into executable skill packages, and then iteratively expands, repairs, merges, or prunes the resulting library through a closed-loop validation process. SkillFoundry produces a substantially novel and internally valid skill library, with 71.1\% of mined skills differing from existing skill libraries such as SkillHub and SkillSMP. We demonstrate that these mined skills improve coding agent performance on five of the six MoSciBench datasets. We further show that SkillFoundry can design new task-specific skills on demand for concrete scientific objectives, and that the resulting skills substantially improve performance on two challenging genomics tasks: cell type annotation and the scDRS workflow. Together, these results show that automatically mined skills improve agent performance on benchmarks and domain-specific tasks, expand coverage beyond hand-crafted skill libraries, and provide a practical foundation for more capable scientific agents.

------

Title: Learn-by-interact: A Data-Centric Framework for Self-Adaptive Agents in Realistic Environments

URL: https://doi.org/10.48550/arXiv.2501.10893

Abstract: Autonomous agents powered by large language models (LLMs) have the potential to enhance human capabilities, assisting with digital tasks from sending emails to performing data analysis. The abilities of existing LLMs at such tasks are often hindered by the lack of high-quality agent data from the corresponding environments they interact with. We propose Learn-by-interact, a data-centric framework to adapt LLM agents to any given environments without human annotations. Learn-by-interact synthesizes trajectories of agent-environment interactions based on documentations, and constructs instructions by summarizing or abstracting the interaction histories, a process called backward construction. We assess the quality of our synthetic data by using them in both training-based scenarios and training-free in-context learning (ICL), where we craft innovative retrieval approaches optimized for agents. Extensive experiments on SWE-bench, WebArena, OSWorld and Spider2-V spanning across realistic coding, web, and desktop environments show the effectiveness of Learn-by-interact in various downstream agentic tasks -- baseline results are improved by up to 12.2\% for ICL with Claude-3.5 and 19.5\% for training with Codestral-22B. We further demonstrate the critical role of backward construction, which provides up to 14.0\% improvement for training. Our ablation studies demonstrate the efficiency provided by our synthesized data in ICL and the superiority of our retrieval pipeline over alternative approaches like conventional retrieval-augmented generation (RAG). We expect that Learn-by-interact will serve as a foundation for agent data synthesis as LLMs are increasingly deployed at real-world environments.

------

Title: Meta Context Engineering via Agentic Skill Evolution

URL: https://doi.org/10.48550/arXiv.2601.21557

Abstract: The operational efficacy of large language models relies heavily on their inference-time context. This has established Context Engineering (CE) as a formal discipline for optimizing these inputs. Current CE methods rely on manually crafted harnesses, such as rigid generation-reflection workflows and predefined context schemas. They impose structural biases and restrict context optimization to a narrow, intuition-bound design space. To address this, we introduce Meta Context Engineering (MCE), a bi-level framework that supersedes static CE heuristics by co-evolving CE skills and context artifacts. In MCE iterations, a meta-level agent refines engineering skills via agentic crossover, a deliberative search over the history of skills, their executions, and evaluations. A base-level agent executes these skills, learns from training rollouts, and optimizes context as flexible files and code. We evaluate MCE across five disparate domains under offline and online settings. MCE demonstrates consistent performance gains, achieving 5.6--53.8% relative improvement over state-of-the-art agentic CE methods (mean of 16.9%), while maintaining superior context adaptability, transferability, and efficiency in both context usage and training.

------

Title: LLMs as Scalable, General-Purpose Simulators For Evolving Digital Agent Training

URL: https://doi.org/10.48550/arXiv.2510.14969

Abstract: Digital agents require diverse, large-scale UI trajectories to generalize across real-world tasks, yet collecting such data is prohibitively expensive in both human annotation, infra and engineering perspectives. To this end, we introduce $\textbf{UI-Simulator}$, a scalable paradigm that generates structured UI states and transitions to synthesize training trajectories at scale. Our paradigm integrates a digital world simulator for diverse UI states, a guided rollout process for coherent exploration, and a trajectory wrapper that produces high-quality and diverse trajectories for agent training. We further propose $\textbf{UI-Simulator-Grow}$, a targeted scaling strategy that enables more rapid and data-efficient scaling by prioritizing high-impact tasks and synthesizes informative trajectory variants. Experiments on WebArena and AndroidWorld show that UI-Simulator rivals or surpasses open-source agents trained on real UIs with significantly better robustness, despite using weaker teacher models. Moreover, UI-Simulator-Grow matches the performance of Llama-3-70B-Instruct using only Llama-3-8B-Instruct as the base model, highlighting the potential of targeted synthesis scaling paradigm to continuously and efficiently enhance the digital agents.

------

Title: Unifying Dynamic Tool Creation and Cross-Task Experience Sharing through Cognitive Memory Architecture

URL: https://doi.org/10.48550/arXiv.2512.11303

Abstract: Large Language Model agents face fundamental challenges in adapting to novel tasks due to limitations in tool availability and experience reuse. Existing approaches either rely on predefined tools with limited coverage or build tools from scratch without leveraging past experiences, leading to inefficient exploration and suboptimal performance. We introduce SMITH (Shared Memory Integrated Tool Hub), a unified cognitive architecture that seamlessly integrates dynamic tool creation with cross-task experience sharing through hierarchical memory organization. SMITH organizes agent memory into procedural, semantic, and episodic components, enabling systematic capability expansion while preserving successful execution patterns. Our approach formalizes tool creation as iterative code generation within controlled sandbox environments and experience sharing through episodic memory retrieval with semantic similarity matching. We further propose a curriculum learning strategy based on agent-ensemble difficulty re-estimation. Extensive experiments on the GAIA benchmark demonstrate SMITH's effectiveness, achieving 81.8% Pass@1 accuracy and outperforming state-of-the-art baselines including Alita (75.2%) and Memento (70.9%). Our work establishes a foundation for building truly adaptive agents that continuously evolve their capabilities through principled integration of tool creation and experience accumulation.

------

Title: FABRIC: Framework for Agent-Based Realistic Intelligence Creation

URL: https://doi.org/10.48550/arXiv.2510.17995

Abstract: Large language models (LLMs) are increasingly deployed as agents, expected to decompose goals, invoke tools, and verify results in dynamic environments. Realizing these capabilities requires access to agentic data-structured interaction records that couple user intents with tool specifications, argument-grounded calls, and verifiable execution traces. However, collecting such data from human annotators is costly, time-consuming, and difficult to scale. We present a unified framework for synthesizing agentic data using only LLMs, without any human-in-the-loop supervision. This framework decomposes generation into modular pipelines that produce complete interaction records spanning task specifications, tool definitions, policy pseudocode, natural language exchanges, and execution traces. Records conform to strict syntactic and semantic constraints, ensuring machine-parseability and faithful alignment across inputs, outputs, and tool calls. Beyond single tasks, there is support for both multi-task and multi-turn agent interactions, enabling the construction of datasets that reflect the full spectrum of tool-use competencies. To ensure quality and consistency, the framework integrates constrained generation formats, JSON-schema validation, and judge-based filtering. This paper formalizes the schema for agentic records, details the prompt design principles that guide generation, and introduces scalable pipelines for high-quality synthetic data. By providing a reproducible, LLM-only alternative to manual collection, hence advancing the development of agentic LLMs capable of robust tool use.

------

Title: Mock Worlds, Real Skills: Building Small Agentic Language Models with Synthetic Tasks, Simulated Environments, and Rubric-Based Rewards

URL: https://doi.org/10.48550/arXiv.2601.22511

Abstract: Small LLMs often struggle to match the agentic capabilities of large, costly models. While reinforcement learning can help, progress has been limited by two structural bottlenecks: existing open-source agentic training data are narrow in task variety and easily solved; real-world APIs lack diversity and are unstable for large-scale reinforcement learning rollout processes. We address these challenges with SYNTHAGENT, a framework that jointly synthesizes diverse tool-use training data and simulates complete environments. Specifically, a strong teacher model creates novel tasks and tool ecosystems, then rewrites them into intentionally underspecified instructions. This compels agents to actively query users for missing details. When handling synthetic tasks, an LLM-based user simulator provides user-private information, while a mock tool system delivers stable tool responses. For rewards, task-level rubrics are constructed based on required subgoals, user-agent interactions, and forbidden behaviors. Across 14 challenging datasets in math, search, and tool use, models trained on our synthetic data achieve substantial gains, with small models outperforming larger baselines.

------

Title: CASCADE: Cumulative Agentic Skill Creation through Autonomous Development and Evolution

URL: https://doi.org/10.48550/arXiv.2512.23880

Abstract: Large language model (LLM) agents currently depend on predefined tools or early-stage tool generation, limiting their adaptability and scalability to complex scientific tasks. We introduce CASCADE, a self-evolving agentic framework representing an early instantiation of the transition from"LLM + tool use"to"LLM + skill acquisition". CASCADE enables agents to master complex external tools and codify knowledge through two meta-skills: continuous learning via web search, code extraction, and memory utilization; self-reflection via introspection, knowledge graph exploration, and others. We evaluate CASCADE on SciSkillBench, a benchmark of 116 materials science and chemistry research tasks. CASCADE achieves a 93.3% success rate using GPT-5, compared to 35.4% without evolution mechanisms. We further demonstrate real-world applications in computational analysis, autonomous laboratory experiments, and selective reproduction of published papers. Along with human-agent collaboration and memory consolidation, CASCADE accumulates executable skills that can be shared across agents and scientists, moving toward scalable AI-assisted scientific research.

------

Title: CoEvoSkills: Self-Evolving Agent Skills via Co-Evolutionary Verification

URL: https://www.semanticscholar.org/paper/ad672be7b481422a99eac7ecfcb95c4877da2767

Abstract: Anthropic proposes the concept of skills for LLM agents to tackle multi-step professional tasks that simple tool invocations cannot address. A tool is a single, self-contained function, whereas a skill is a structured bundle of interdependent multi-file artifacts. Currently, skill generation is not only label-intensive due to manual authoring, but also may suffer from human--machine cognitive misalignment, which can lead to degraded agent performance, as evidenced by evaluations on SkillsBench. Therefore, we aim to enable agents to autonomously generate skills. However, existing self-evolving methods designed for tools cannot be directly applied to skills due to their increased complexity. To address these issues, we propose CoEvoSkills, a self-evolving skills framework that enables agents to autonomously construct complex, multi-file skill packages. Specifically, CoEvoSkills couples a Skill Generator that iteratively refines skills with a Surrogate Verifier that co-evolves to provide informative and actionable feedback without access to ground-truth test content. On SkillsBench, CoEvoSkills achieves the highest pass rate among five baselines on both Claude Code and Codex, and also exhibits strong generalization capabilities to six additional LLMs.

------

Title: SynthAgent: Adapting Web Agents with Synthetic Supervision

URL: https://www.semanticscholar.org/paper/406fe6eb1fe26be46dba5f0279c65d3ce3a76759

Abstract: Web agents struggle to adapt to new websites due to the scarcity of environment specific tasks and demonstrations. Recent works have explored synthetic data generation to address this challenge, however, they suffer from data quality issues where synthesized tasks contain hallucinations that cannot be executed, and collected trajectories are noisy with redundant or misaligned actions. In this paper, we propose SynthAgent, a fully synthetic supervision framework that aims at improving synthetic data quality via dual refinement of both tasks and trajectories. Our approach begins by synthesizing diverse tasks through categorized exploration of web elements, ensuring efficient coverage of the target environment. During trajectory collection, tasks are refined only when conflicts with observations are detected, which mitigates hallucinations while preserving task consistency. After collection, we conduct trajectory refinement with global context to mitigate potential noise or misalignments. Finally, we fine-tune open-source web agents on the refined synthetic data to adapt them to the target environment. Experimental results demonstrate that SynthAgent outperforms existing synthetic data methods, validating the importance of high-quality synthetic supervision. The code is publicly available at https://github.com/aiming-lab/SynthAgent.

------

Title: Aligning Agentic World Models via Knowledgeable Experience Learning

URL: https://doi.org/10.48550/arXiv.2601.13247

Abstract: Current Large Language Models (LLMs) exhibit a critical modal disconnect: they possess vast semantic knowledge but lack the procedural grounding to respect the immutable laws of the physical world. Consequently, while these agents implicitly function as world models, their simulations often suffer from physical hallucinations-generating plans that are logically sound but physically unexecutable. Existing alignment strategies predominantly rely on resource-intensive training or fine-tuning, which attempt to compress dynamic environmental rules into static model parameters. However, such parametric encapsulation is inherently rigid, struggling to adapt to the open-ended variability of physical dynamics without continuous, costly retraining. To bridge this gap, we introduce WorldMind, a framework that autonomously constructs a symbolic World Knowledge Repository by synthesizing environmental feedback. Specifically, it unifies Process Experience to enforce physical feasibility via prediction errors and Goal Experience to guide task optimality through successful trajectories. Experiments on EB-ALFRED and EB-Habitat demonstrate that WorldMind achieves superior performance compared to baselines with remarkable cross-model and cross-environment transferability.

------

Title: AutoGuide: Automated Generation and Selection of Context-Aware Guidelines for Large Language Model Agents

URL: https://doi.org/10.48550/arXiv.2403.08978

Abstract: Recent advances in large language models (LLMs) have empowered AI agents capable of performing various sequential decision-making tasks. However, effectively guiding LLMs to perform well in unfamiliar domains like web navigation, where they lack sufficient knowledge, has proven to be difficult with the demonstration-based in-context learning paradigm. In this paper, we introduce a novel framework, called AutoGuide, which addresses this limitation by automatically generating context-aware guidelines from offline experiences. Importantly, each context-aware guideline is expressed in concise natural language and follows a conditional structure, clearly describing the context where it is applicable. As a result, our guidelines facilitate the provision of relevant knowledge for the agent's current decision-making process, overcoming the limitations of the conventional demonstration-based learning paradigm. Our evaluation demonstrates that AutoGuide significantly outperforms competitive baselines in complex benchmark domains, including real-world web navigation.

------

Title: Natural-Language Agent Harnesses

URL: https://www.semanticscholar.org/paper/88b12da49b820f56f9552d13a3be578de7c6c77b

Abstract: Agent performance increasingly depends on \emph{harness engineering}, yet harness design is usually buried in controller code and runtime-specific conventions, making it hard to transfer, compare, and study as a scientific object. We ask whether the high-level control logic of an agent harness can instead be externalized as a portable executable artifact. We introduce \textbf{Natural-Language Agent Harnesses} (NLAHs), which express harness behavior in editable natural language, and \textbf{Intelligent Harness Runtime} (IHR), a shared runtime that executes these harnesses through explicit contracts, durable artifacts, and lightweight adapters. Across coding and computer-use benchmarks, we conduct controlled evaluations of operational viability, module ablation, and code-to-text harness migration.

------

Title: Memory Transfer Learning: How Memories are Transferred Across Domains in Coding Agents

URL: https://www.semanticscholar.org/paper/1347b3522f49ea2b4ac720bb3fd6023c107b6a5f

Abstract: Memory-based self-evolution has emerged as a promising paradigm for coding agents. However, existing approaches typically restrict memory utilization to homogeneous task domains, failing to leverage the shared infrastructural foundations, such as runtime environments and programming languages, that exist across diverse real-world coding problems. To address this limitation, we investigate \textbf{Memory Transfer Learning} (MTL) by harnessing a unified memory pool from heterogeneous domains. We evaluate performance across 6 coding benchmarks using four memory representations, ranging from concrete traces to abstract insights. Our experiments demonstrate that cross-domain memory improves average performance by 3.7\%, primarily by transferring meta-knowledge, such as validation routines, rather than task-specific code. Importantly, we find that abstraction dictates transferability; high-level insights generalize well, whereas low-level traces often induce negative transfer due to excessive specificity. Furthermore, we show that transfer effectiveness scales with the size of the memory pool, and memory can be transferred even between different models. Our work establishes empirical design principles for expanding memory utilization beyond single-domain silos. Project page: https://memorytransfer.github.io/

------

Title: Structured Agent Distillation for Large Language Model

URL: https://doi.org/10.48550/arXiv.2505.13820

Abstract: Large language models (LLMs) exhibit strong capabilities as decision-making agents by interleaving reasoning and actions, as seen in ReAct-style frameworks. Yet, their practical deployment is constrained by high inference costs and large model sizes. We propose Structured Agent Distillation, a framework that compresses large LLM-based agents into smaller student models while preserving both reasoning fidelity and action consistency. Unlike standard token-level distillation, our method segments trajectories into {[REASON]} and {[ACT]} spans, applying segment-specific losses to align each component with the teacher's behavior. This structure-aware supervision enables compact agents to better replicate the teacher's decision process. Experiments on ALFWorld, HotPotQA-ReAct, and WebShop show that our approach consistently outperforms token-level and imitation learning baselines, achieving significant compression with minimal performance drop. Scaling and ablation results further highlight the importance of span-level alignment for efficient and deployable agents.

------

Title: Investigate-Consolidate-Exploit: A General Strategy for Inter-Task Agent Self-Evolution

URL: https://doi.org/10.48550/arXiv.2401.13996

Abstract: This paper introduces Investigate-Consolidate-Exploit (ICE), a novel strategy for enhancing the adaptability and flexibility of AI agents through inter-task self-evolution. Unlike existing methods focused on intra-task learning, ICE promotes the transfer of knowledge between tasks for genuine self-evolution, similar to human experience learning. The strategy dynamically investigates planning and execution trajectories, consolidates them into simplified workflows and pipelines, and exploits them for improved task execution. Our experiments on the XAgent framework demonstrate ICE's effectiveness, reducing API calls by as much as 80% and significantly decreasing the demand for the model's capability. Specifically, when combined with GPT-3.5, ICE's performance matches that of raw GPT-4 across various agent tasks. We argue that this self-evolution approach represents a paradigm shift in agent design, contributing to a more robust AI community and ecosystem, and moving a step closer to full autonomy.

------

Title: Training-Free Group Relative Policy Optimization

URL: https://doi.org/10.48550/arXiv.2510.08191

Abstract: Recent advances in Large Language Model (LLM) agents have demonstrated their promising general capabilities. However, their performance in specialized real-world domains often degrades due to challenges in effectively integrating external tools and specific prompting strategies. While methods like agentic reinforcement learning have been proposed to address this, they typically rely on costly parameter updates, for example, through a process that uses Supervised Fine-Tuning (SFT) followed by a Reinforcement Learning (RL) phase with Group Relative Policy Optimization (GRPO) to alter the output distribution. However, we argue that LLMs can achieve a similar effect on the output distribution by learning experiential knowledge as a token prior, which is a far more lightweight approach that not only addresses practical data scarcity but also avoids the common issue of overfitting. To this end, we propose Training-Free Group Relative Policy Optimization (Training-Free GRPO), a cost-effective solution that enhances LLM agent performance without any parameter updates. Our method leverages the group relative semantic advantage instead of numerical ones within each group of rollouts, iteratively distilling high-quality experiential knowledge during multi-epoch learning on a minimal ground-truth data. Such knowledge serves as the learned token prior, which is seamlessly integrated during LLM API calls to guide model behavior. Experiments on mathematical reasoning and web searching tasks demonstrate that Training-Free GRPO, when applied to DeepSeek-V3.1-Terminus, significantly improves out-of-domain performance. With just a few dozen training samples, Training-Free GRPO outperforms fine-tuned small LLMs with marginal training data and cost.

------

Title: TAME: A Trustworthy Test-Time Evolution of Agent Memory with Systematic Benchmarking

URL: https://doi.org/10.48550/arXiv.2602.03224

Abstract: Test-time evolution of agent memory serves as a pivotal paradigm for achieving AGI by bolstering complex reasoning through experience accumulation. However, even during benign task evolution, agent safety alignment remains vulnerable-a phenomenon known as Agent Memory Misevolution. To evaluate this phenomenon, we construct the Trust-Memevo benchmark to assess multi-dimensional trustworthiness during benign task evolution, revealing an overall decline in trustworthiness across various task domains and evaluation settings. To address this issue, we propose TAME, a dual-memory evolutionary framework that separately evolves executor memory to improve task performance by distilling generalizable methodologies, and evaluator memory to refine assessments of both safety and task utility based on historical feedback. Through a closed loop of memory filtering, draft generation, trustworthy refinement, execution, and dual-track memory updating, TAME preserves trustworthiness without sacrificing utility. Experiments demonstrate that TAME mitigates misevolution, achieving a joint improvement in both trustworthiness and task performance.

------

Title: Meta-Harness: End-to-End Optimization of Model Harnesses

URL: https://www.semanticscholar.org/paper/64cd8a551607d5d004e37bb0c6cbd6d65241fbfb

Abstract: The performance of large language model (LLM) systems depends not only on model weights, but also on their harness: the code that determines what information to store, retrieve, and present to the model. Yet harnesses are still designed largely by hand, and existing text optimizers are poorly matched to this setting because they compress feedback too aggressively. We introduce Meta-Harness, an outer-loop system that searches over harness code for LLM applications. It uses an agentic proposer that accesses the source code, scores, and execution traces of all prior candidates through a filesystem. On online text classification, Meta-Harness improves over a state-of-the-art context management system by 7.7 points while using 4x fewer context tokens. On retrieval-augmented math reasoning, a single discovered harness improves accuracy on 200 IMO-level problems by 4.7 points on average across five held-out models. On agentic coding, discovered harnesses surpass the best hand-engineered baselines on TerminalBench-2. Together, these results show that richer access to prior experience can enable automated harness engineering.

------

Title: EE-MCP: Self-Evolving MCP-GUI Agents via Automated Environment Generation and Experience Learning

URL: https://www.semanticscholar.org/paper/e06e5eeb506c3926d45063bcb6d6395300a5b14d

Abstract: Computer-use agents that combine GUI interaction with structured API calls via the Model Context Protocol (MCP) show promise for automating software tasks. However, existing approaches lack a principled understanding of how agents should balance these two modalities and how to enable iterative self-improvement across diverse applications. We formulate MCP-GUI interplay as a unified hybrid policy learning problem where the agent learns when each modality provides complementary advantages, and show that distillation and experience augmentation target fundamentally different failure modes - requiring application-aware mechanism selection. Built on this formulation, we propose a self-evolving framework with a fully automatic pipeline that orchestrates automatic environment generation and validation, trajectory collection, gap-driven task synthesis, and quality-filtered training - all without manual intervention. A key innovation is our experience bank, which accumulates LLM-learned rules from trajectory comparison, enabling inference-time improvement without fine-tuning. Systematic \textbf{cross-application analysis} across three desktop applications reveals that the optimal strategy depends on MCP-GUI composition: distillation achieves 77.8\% pass rate on MCP-dominant tasks (+17.8pp), while the experience bank excels on GUI-intensive tasks (+10.0pp).

------

Title: AlphaOPT: Formulating Optimization Programs with Self-Improving LLM Experience Library

URL: https://doi.org/10.48550/arXiv.2510.18428

Abstract: Optimization modeling underlies critical decision-making across industries, yet remains difficult to automate: natural-language problem descriptions must be translated into precise mathematical formulations and executable solver code. Existing LLM-based approaches typically rely on brittle prompting or costly retraining, both of which offer limited generalization. Recent work suggests that large models can improve via experience reuse, but how to systematically acquire, refine, and reuse such experience in structurally constrained settings remains unclear. We present \textbf{AlphaOPT}, a self-improving experience library that enables LLMs to learn optimization modeling knowledge from limited supervision, including answer-only feedback without gold-standard programs, annotated reasoning traces, or parameter updates. AlphaOPT operates in a continual two-phase cycle: a \emph{Library Learning} phase that extracts solver-verified, structured insights from failed attempts, and a \emph{Library Evolution} phase that refines the applicability of stored insights based on aggregate evidence across tasks. This design allows the model to accumulate reusable modeling principles, improve transfer across problem instances, and maintain bounded library growth over time. Evaluated on multiple optimization benchmarks, AlphaOPT steadily improves as more training data become available (65\% $\rightarrow$ 72\% from 100 to 300 training items) and outperforms the strongest baseline by 9.1\% and 8.2\% on two out-of-distribution datasets. These results demonstrate that structured experience learning, grounded in solver feedback, provides a practical alternative to retraining for complex reasoning tasks requiring precise formulation and execution. All code and data are available at: https://github.com/Minw913/AlphaOPT.

------

Title: Sub-goal Distillation: A Method to Improve Small Language Agents

URL: https://doi.org/10.48550/arXiv.2405.02749

Abstract: While Large Language Models (LLMs) have demonstrated significant promise as agents in interactive tasks, their substantial computational requirements and restricted number of calls constrain their practical utility, especially in long-horizon interactive tasks such as decision-making or in scenarios involving continuous ongoing tasks. To address these constraints, we propose a method for transferring the performance of an LLM with billions of parameters to a much smaller language model (770M parameters). Our approach involves constructing a hierarchical agent comprising a planning module, which learns through Knowledge Distillation from an LLM to generate sub-goals, and an execution module, which learns to accomplish these sub-goals using elementary actions. In detail, we leverage an LLM to annotate an oracle path with a sequence of sub-goals towards completing a goal. Subsequently, we utilize this annotated data to fine-tune both the planning and execution modules. Importantly, neither module relies on real-time access to an LLM during inference, significantly reducing the overall cost associated with LLM interactions to a fixed cost. In ScienceWorld, a challenging and multi-task interactive text environment, our method surpasses standard imitation learning based solely on elementary actions by 16.7% (absolute). Our analysis highlights the efficiency of our approach compared to other LLM-based methods. Our code and annotated data for distillation can be found on GitHub.

------

Title: RetroAgent: From Solving to Evolving via Retrospective Dual Intrinsic Feedback

URL: https://www.semanticscholar.org/paper/7846e20ffd11f4b218020a1b84543a7dbcbf45d7

Abstract: Standard reinforcement learning (RL) for large language model (LLM) agents typically optimizes extrinsic rewards, prioritizing isolated task completion over continual adaptation. Consequently, agents often converge to suboptimal policies due to limited exploration. Furthermore, accumulated experience remains implicitly trapped within model parameters, hindering its explicit reuse for guiding future decisions. Inspired by human retrospective self-improvement, we introduce RetroAgent, an online RL framework that trains agents to master complex interactive environments not only by solving tasks, but by evolving under the joint guidance of extrinsic task rewards and retrospective dual intrinsic feedback. Specifically, RetroAgent employs a hindsight self-reflection mechanism that generates two complementary signals: (1) intrinsic numerical feedback, which rewards promising exploration by tracking real-time incremental subtask progress relative to prior attempts; and (2) intrinsic language feedback, which enables explicit experience reuse by distilling reusable lessons into a memory buffer for subsequent decision-making. To effectively leverage these textual experiences, we propose Similarity&Utility-Aware Upper Confidence Bound (SimUtil-UCB), a retrieval strategy that balances relevance, historical utility, and exploration. Extensive experiments across four challenging agentic tasks show that RetroAgent achieves new state-of-the-art (SOTA) performance. Notably, it surpasses Group Relative Policy Optimization (GRPO) baselines by +18.3% on ALFWorld, +15.4% on WebShop, +27.1% on Sokoban, and +8.9% on MineSweeper, while exhibiting strong test-time adaptation and out-of-distribution generalization.

------

Title: WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance

URL: https://doi.org/10.48550/arXiv.2511.12997

Abstract: Multimodal LLM-powered agents have recently demonstrated impressive capabilities in web navigation, enabling agents to complete complex browsing tasks across diverse domains. However, current agents struggle with repetitive errors and lack the ability to learn from past experiences across sessions, limiting their long-term robustness and sample efficiency. We introduce WebCoach, a model-agnostic self-evolving framework that equips web browsing agents with persistent cross-session memory, enabling improved long-term planning, reflection, and continual learning without retraining. WebCoach consists of three key components: (1) a WebCondenser, which standardizes raw navigation logs into concise summaries; (2) an External Memory Store, which organizes complete trajectories as episodic experiences; and (3) a Coach, which retrieves relevant experiences based on similarity and recency, and decides whether to inject task-specific advice into the agent via runtime hooks. This design empowers web agents to access long-term memory beyond their native context window, improving robustness in complex browsing tasks. Moreover, WebCoach achieves self-evolution by continuously curating episodic memory from new navigation trajectories, enabling agents to improve over time without retraining. Evaluations on the WebVoyager benchmark demonstrate that WebCoach consistently improves the performance of browser-use agents across three different LLM backbones. With a 38B model, it increases task success rates from 47% to 61% while reducing or maintaining the average number of steps. Notably, smaller base models with WebCoach achieve performance comparable to the same web agent using GPT-4o.

------

Title: ArcMemo: Abstract Reasoning Composition with Lifelong LLM Memory

URL: https://doi.org/10.48550/arXiv.2509.04439

Abstract: While inference-time scaling enables LLMs to carry out increasingly long and capable reasoning traces, the patterns and insights uncovered during these traces are immediately discarded once the context window is reset for a new query. External memory is a natural way to persist these discoveries, and recent work has shown clear benefits for reasoning-intensive tasks. We see an opportunity to make such memories more broadly reusable and scalable by moving beyond instance-based memory entries (e.g. exact query/response pairs, or summaries tightly coupled with the original problem context) toward concept-level memory: reusable, modular abstractions distilled from solution traces and stored in natural language. For future queries, relevant concepts are selectively retrieved and integrated into the prompt, enabling test-time continual learning without weight updates. Our design introduces new strategies for abstracting takeaways from rollouts and retrieving entries for new queries, promoting reuse and allowing memory to expand with additional experiences. We evaluate on ARC-AGI, a benchmark that stresses compositional generalization and abstract reasoning, making it a natural fit for concept memory. Our method yields a 7.5% relative gain over a strong no-memory baseline with performance continuing to scale with inference compute. We find abstract concepts to be the most consistent memory design, outscoring the baseline at all tested inference compute scales. Moreover, dynamically updating memory during test-time outperforms fixed settings, supporting the hypothesis that accumulating and abstracting patterns enables further solutions in a form of self-improvement. Code is available at https://github.com/matt-seb-ho/arc_memo.

------

Title: Sample-Efficient Online Learning in LM Agents via Hindsight Trajectory Rewriting

URL: https://doi.org/10.48550/arXiv.2510.10304

Abstract: Language model (LM) agents deployed in novel environments often exhibit poor sample efficiency when learning from sequential interactions. This significantly hinders the usefulness of such agents in environments where interaction is costly (for example, when they interact with humans or reset physical systems). While a number of existing LM agent architectures incorporate various mechanisms for experience storage and reflection, they make limited use of LMs'abilities to directly generate or reason about full counterfactual trajectories. We introduce ECHO (Experience Consolidation via Hindsight Optimization), a prompting framework that adapts hindsight experience replay from reinforcement learning for language model agents. ECHO generates optimized trajectories for alternative goals that could have been achieved during failed attempts, effectively creating synthetic positive examples from unsuccessful interactions. Our approach consists of two components: a hindsight rule that uses the language model itself to identify relevant subgoals and generate optimized trajectories, and an update rule that maintains compressed trajectory representations in memory. We evaluate ECHO on stateful versions of XMiniGrid, a text-based navigation and planning benchmark, and PeopleJoinQA, a collaborative information-gathering enterprise simulation. Across both domains, ECHO outperforms vanilla language agent baselines by up to 80%; in XMiniGrid, it also outperforms a number of sophisticated agent architectures including Reflexion and AWM, demonstrating faster adaptation to novel environments through more effective utilization of past experiences.

------

Title: From Procedural Skills to Strategy Genes: Towards Experience-Driven Test-Time Evolution

URL: https://www.semanticscholar.org/paper/79b442e4943aff69119dd4bbabf08191e921d8c7

Abstract: This beta technical report asks how reusable experience should be represented so that it can function as effective test-time control and as a substrate for iterative evolution. We study this question in 4.590 controlled trials across 45 scientific code-solving scenarios. We find that documentation-oriented Skill packages provide unstable control: their useful signal is sparse, and expanding a compact experience object into a fuller documentation package often fails to help and can degrade the overall average. We further show that representation itself is a first-order factor. A compact Gene representation yields the strongest overall average, remains competitive under substantial structural perturbations, and outperforms matched-budget Skill fragments, while reattaching documentation-oriented material usually weakens rather than improves it. Beyond one-shot control, we show that Gene is also a better carrier for iterative experience accumulation: attached failure history is more effective in Gene than in Skill or freeform text, editable structure matters beyond content alone, and failure information is most useful when distilled into compact warnings rather than naively appended. On CritPt, gene-evolved systems improve over their paired base models from 9.1% to 18.57% and from 17.7% to 27.14%. These results suggest that the core problem in experience reuse is not how to supply more experience, but how to encode experience as a compact, control-oriented, evolution-ready object.

------

Title: Memory Intelligence Agent

URL: https://www.semanticscholar.org/paper/130f3ee74fa9b3f4e95d909ffb5b065f0bc74347

Abstract: Deep research agents (DRAs) integrate LLM reasoning with external tools. Memory systems enable DRAs to leverage historical experiences, which are essential for efficient reasoning and autonomous evolution. Existing methods rely on retrieving similar trajectories from memory to aid reasoning, while suffering from key limitations of ineffective memory evolution and increasing storage and retrieval costs. To address these problems, we propose a novel Memory Intelligence Agent (MIA) framework, consisting of a Manager-Planner-Executor architecture. Memory Manager is a non-parametric memory system that can store compressed historical search trajectories. Planner is a parametric memory agent that can produce search plans for questions. Executor is another agent that can search and analyze information guided by the search plan. To build the MIA framework, we first adopt an alternating reinforcement learning paradigm to enhance cooperation between the Planner and the Executor. Furthermore, we enable the Planner to continuously evolve during test-time learning, with updates performed on-the-fly alongside inference without interrupting the reasoning process. Additionally, we establish a bidirectional conversion loop between parametric and non-parametric memories to achieve efficient memory evolution. Finally, we incorporate a reflection and an unsupervised judgment mechanisms to boost reasoning and self-evolution in the open world. Extensive experiments across eleven benchmarks demonstrate the superiority of MIA.

------

Title: A-MEM: Agentic Memory for LLM Agents

URL: https://doi.org/10.48550/arXiv.2502.12110

Abstract: While large language model (LLM) agents can effectively use external tools for complex real-world tasks, they require memory systems to leverage historical experiences. Current memory systems enable basic storage and retrieval but lack sophisticated memory organization, despite recent attempts to incorporate graph databases. Moreover, these systems'fixed operations and structures limit their adaptability across diverse tasks. To address this limitation, this paper proposes a novel agentic memory system for LLM agents that can dynamically organize memories in an agentic way. Following the basic principles of the Zettelkasten method, we designed our memory system to create interconnected knowledge networks through dynamic indexing and linking. When a new memory is added, we generate a comprehensive note containing multiple structured attributes, including contextual descriptions, keywords, and tags. The system then analyzes historical memories to identify relevant connections, establishing links where meaningful similarities exist. Additionally, this process enables memory evolution - as new memories are integrated, they can trigger updates to the contextual representations and attributes of existing historical memories, allowing the memory network to continuously refine its understanding. Our approach combines the structured organization principles of Zettelkasten with the flexibility of agent-driven decision making, allowing for more adaptive and context-aware memory management. Empirical experiments on six foundation models show superior improvement against existing SOTA baselines. The source code for evaluating performance is available at https://github.com/WujiangXu/A-mem, while the source code of the agentic memory system is available at https://github.com/WujiangXu/A-mem-sys.

------

Title: Metacognitive Reuse: Turning Recurring LLM Reasoning Into Concise Behaviors

URL: https://doi.org/10.48550/arXiv.2509.13237

Abstract: Large language models (LLMs) now solve multi-step problems by emitting extended chains of thought. During the process, they often re-derive the same intermediate steps across problems, inflating token usage and latency. This saturation of the context window leaves less capacity for exploration. We study a simple mechanism that converts recurring reasoning fragments into concise, reusable"behaviors"(name + instruction) via the model's own metacognitive analysis of prior traces. These behaviors are stored in a"behavior handbook"which supplies them to the model in-context at inference or distills them into parameters via supervised fine-tuning. This approach achieves improved test-time reasoning across three different settings - 1) Behavior-conditioned inference: Providing the LLM relevant behaviors in-context during reasoning reduces number of reasoning tokens by up to 46% while matching or improving baseline accuracy; 2) Behavior-guided self-improvement: Without any parameter updates, the model improves its own future reasoning by leveraging behaviors from its own past problem solving attempts. This yields up to 10% higher accuracy than a naive critique-and-revise baseline; and 3) Behavior-conditioned SFT: SFT on behavior-conditioned reasoning traces is more effective at converting non-reasoning models into reasoning models as compared to vanilla SFT. Together, these results indicate that turning slow derivations into fast procedural hints enables LLMs to remember how to reason, not just what to conclude.

------

Title: Trajectory-Informed Memory Generation for Self-Improving Agent Systems

URL: https://www.semanticscholar.org/paper/8a2211bea2bef82de683cb8f7499b49f8bd73cad

Abstract: LLM-powered agents face a persistent challenge: learning from their execution experiences to improve future performance. While agents can successfully complete many tasks, they often repeat inefficient patterns, fail to recover from similar errors, and miss opportunities to apply successful strategies from past executions. We present a novel framework for automatically extracting actionable learnings from agent execution trajectories and utilizing them to improve future performance through contextual memory retrieval. Our approach comprises four components: (1) a Trajectory Intelligence Extractor that performs semantic analysis of agent reasoning patterns, (2) a Decision Attribution Analyzer that identifies which decisions and reasoning steps led to failures, recoveries, or inefficiencies, (3) a Contextual Learning Generator that produces three types of guidance -- strategy tips from successful patterns, recovery tips from failure handling, and optimization tips from inefficient but successful executions, and (4) an Adaptive Memory Retrieval System that injects relevant learnings into agent prompts based on multi-dimensional similarity. Unlike existing memory systems that store generic conversational facts, our framework understands execution patterns, extracts structured learnings with provenance, and retrieves guidance tailored to specific task contexts. Evaluation on the AppWorld benchmark demonstrates consistent improvements, with up to 14.3 percentage point gains in scenario goal completion on held-out tasks and particularly strong benefits on complex tasks (28.5~pp scenario goal improvement, a 149\% relative increase).

------

Title: ANCHOR: Branch-Point Data Generation for GUI Agents

URL: https://doi.org/10.48550/arXiv.2602.07153

Abstract: End-to-end GUI agents for real desktop environments require large amounts of high-quality interaction data, yet collecting human demonstrations is expensive and existing synthetic pipelines often suffer from limited task diversity or noisy, goal-drifting trajectories. We present a trajectory expansion framework Anchor that bootstraps scalable desktop supervision from a small set of verified seed demonstrations. Starting from each seed, we identify branch points that correspond to meaningful state changes and propose new, state-grounded task variants conditioned on the current GUI context. An executing agent then follows the proposed instructions to generate new trajectories, while a verifier enforces task completion via state-aware checks and trajectory-level consistency. To improve supervision quality, we further apply task-conditioned step-level filtering to remove ungrounded actions and denoise post-branch segments to maintain coherent intent. Experiments on standard desktop benchmarks, OSWorld and WindowsAgentArena, show that models fine-tuned on our expanded corpus achieve consistent improvements over zero-shot agents and representative synthesis baselines, and generalize across applications and operating systems.

------

Title: Co-Evolving LLM Decision and Skill Bank Agents for Long-Horizon Tasks

URL: https://www.semanticscholar.org/paper/6fbed6c6a5fa6dbdbb06cede77e50318a8499bad

Abstract: Long horizon interactive environments are a testbed for evaluating agents skill usage abilities. These environments demand multi step reasoning, the chaining of multiple skills over many timesteps, and robust decision making under delayed rewards and partial observability. Games are a good testbed for evaluating agent skill usage in environments. Large Language Models (LLMs) offer a promising alternative as game playing agents, but they often struggle with consistent long horizon decision making because they lack a mechanism to discover, retain, and reuse structured skills across episodes. We present COSPLAY, a co evolution framework in which an LLM decision agent retrieves skills from a learnable skill bank to guide action taking, while an agent managed skill pipeline discovers reusable skills from the agents unlabeled rollouts to form a skill bank. Our framework improves both the decision agent to learn better skill retrieval and action generation, while the skill bank agent continually extracts, refines, and updates skills together with their contracts. Experiments across six game environments show that COSPLAY with an 8B base model achieves over 25.1 percent average reward improvement against four frontier LLM baselines on single player game benchmarks while remaining competitive on multi player social reasoning games.

------

Title: ExpeL: LLM Agents Are Experiential Learners

URL: https://doi.org/10.48550/arXiv.2308.10144

Abstract: The recent surge in research interest in applying large language models (LLMs) to decision-making tasks has flourished by leveraging the extensive world knowledge embedded in LLMs. While there is a growing demand to tailor LLMs for custom decision-making tasks, finetuning them for specific tasks is resource-intensive and may diminish the model's generalization capabilities. Moreover, state-of-the-art language models like GPT-4 and Claude are primarily accessible through API calls, with their parametric weights remaining proprietary and unavailable to the public. This scenario emphasizes the growing need for new methodologies that allow learning from agent experiences without requiring parametric updates. To address these problems, we introduce the Experiential Learning (ExpeL) agent. Our agent autonomously gathers experiences and extracts knowledge using natural language from a collection of training tasks. At inference, the agent recalls its extracted insights and past experiences to make informed decisions. Our empirical results highlight the robust learning efficacy of the ExpeL agent, indicating a consistent enhancement in its performance as it accumulates experiences. We further explore the emerging capabilities and transfer learning potential of the ExpeL agent through qualitative observations and additional experiments.

------

Title: The World Leaks the Future: Harness Evolution for Future Prediction Agents

URL: https://www.semanticscholar.org/paper/9f0a7d3cdc3458fecaf1e4062fdb9e2d4dff37fe

Abstract: Many consequential decisions must be made before the relevant outcome is known. Such problems are commonly framed as future prediction, where an LLM agent must form a prediction for an unresolved question using only the public information available at the prediction time. The setting is difficult because public evidence evolves while useful supervision arrives only after the question is resolved, so most existing approaches still improve mainly from final outcomes. Yet final outcomes are too coarse to guide earlier factor tracking, evidence gathering and interpretation, or uncertainty handling. When the same unresolved question is revisited over time, temporal contrasts between earlier and later predictions can expose omissions in the earlier prediction process; we call this signal internal feedback. We introduce Milkyway, a self-evolving agent system that keeps the base model fixed and instead updates a persistent future prediction harness for factor tracking, evidence gathering and interpretation, and uncertainty handling. Across repeated predictions on the same unresolved question, Milkyway extracts internal feedback and writes reusable guidance back into the harness, so later predictions on that question can improve before the outcome is known. After the question is resolved, the final outcome provides a retrospective check before the updated harness is carried forward to subsequent questions. On FutureX and FutureWorld, Milkyway achieves the best overall score among the compared methods, improving FutureX from 44.07 to 60.90 and FutureWorld from 62.22 to 77.96.

------

Title: Towards Autonomous Memory Agents

URL: https://doi.org/10.48550/arXiv.2602.22406

Abstract: Recent memory agents improve LLMs by extracting experiences and conversation history into an external storage. This enables low-overhead context assembly and online memory update without expensive LLM training. However, existing solutions remain passive and reactive; memory growth is bounded by information that happens to be available, while memory agents seldom seek external inputs in uncertainties. We propose autonomous memory agents that actively acquire, validate, and curate knowledge at a minimum cost. U-Mem materializes this idea via (i) a cost-aware knowledge-extraction cascade that escalates from cheap self/teacher signals to tool-verified research and, only when needed, expert feedback, and (ii) semantic-aware Thompson sampling to balance exploration and exploitation over memories and mitigate cold-start bias. On both verifiable and non-verifiable benchmarks, U-Mem consistently beats prior memory baselines and can surpass RL-based optimization, improving HotpotQA (Qwen2.5-7B) by 14.6 points and AIME25 (Gemini-2.5-flash) by 7.33 points.

------

Title: OS-Copilot: Towards Generalist Computer Agents with Self-Improvement

URL: https://doi.org/10.48550/arXiv.2402.07456

Abstract: Autonomous interaction with the computer has been a longstanding challenge with great potential, and the recent proliferation of large language models (LLMs) has markedly accelerated progress in building digital agents. However, most of these agents are designed to interact with a narrow domain, such as a specific software or website. This narrow focus constrains their applicability for general computer tasks. To this end, we introduce OS-Copilot, a framework to build generalist agents capable of interfacing with comprehensive elements in an operating system (OS), including the web, code terminals, files, multimedia, and various third-party applications. We use OS-Copilot to create FRIDAY, a self-improving embodied agent for automating general computer tasks. On GAIA, a general AI assistants benchmark, FRIDAY outperforms previous methods by 35%, showcasing strong generalization to unseen applications via accumulated skills from previous tasks. We also present numerical and quantitative evidence that FRIDAY learns to control and self-improve on Excel and Powerpoint with minimal supervision. Our OS-Copilot framework and empirical findings provide infrastructure and insights for future research toward more capable and general-purpose computer agents.

------

Title: ICAL: Continual Learning of Multimodal Agents by Transforming Trajectories into Actionable Insights

URL: https://doi.org/10.48550/arXiv.2406.14596

Abstract: Large-scale generative language and vision-language models (LLMs and VLMs) excel in few-shot in-context learning for decision making and instruction following. However, they require high-quality exemplar demonstrations to be included in their context window. In this work, we ask: Can LLMs and VLMs generate their own prompt examples from generic, sub-optimal demonstrations? We propose In-Context Abstraction Learning (ICAL), a method that builds a memory of multi-modal experience insights from sub-optimal demonstrations and human feedback. Given a noisy demonstration in a new domain, VLMs abstract the trajectory into a general program by fixing inefficient actions and annotating cognitive abstractions: task relationships, object state changes, temporal subgoals, and task construals. These abstractions are refined and adapted interactively through human feedback while the agent attempts to execute the trajectory in a similar environment. The resulting abstractions, when used as exemplars in the prompt, significantly improve decision-making in retrieval-augmented LLM and VLM agents. Our ICAL agent surpasses the state-of-the-art in dialogue-based instruction following in TEACh, multimodal web agents in VisualWebArena, and action anticipation in Ego4D. In TEACh, we achieve a 12.6% improvement in goal-condition success. In Visual-WebArena, our task success rate improves over the SOTA from 14.3% to 22.7%. In Ego4D action forecasting, we improve over few-shot GPT-4V and remain competitive with supervised models. We show finetuning our retrieval-augmented in-context agent yields additional improvements. Our approach significantly reduces reliance on expert-crafted examples and consistently outperforms in-context learning from action plans that lack such insights.

------

Title: Agent Planning with World Knowledge Model

URL: https://doi.org/10.48550/arXiv.2405.14205

Abstract: Recent endeavors towards directly using large language models (LLMs) as agent models to execute interactive planning tasks have shown commendable results. Despite their achievements, however, they still struggle with brainless trial-and-error in global planning and generating hallucinatory actions in local planning due to their poor understanding of the ``real'' physical world. Imitating humans' mental world knowledge model which provides global prior knowledge before the task and maintains local dynamic knowledge during the task, in this paper, we introduce parametric World Knowledge Model (WKM) to facilitate agent planning. Concretely, we steer the agent model to self-synthesize knowledge from both expert and sampled trajectories. Then we develop WKM, providing prior task knowledge to guide the global planning and dynamic state knowledge to assist the local planning. Experimental results on three complex real-world simulated datasets with three state-of-the-art open-source LLMs, Mistral-7B, Gemma-7B, and Llama-3-8B, demonstrate that our method can achieve superior performance compared to various strong baselines. Besides, we analyze to illustrate that our WKM can effectively alleviate the blind trial-and-error and hallucinatory action issues, providing strong support for the agent's understanding of the world. Other interesting findings include: 1) our instance-level task knowledge can generalize better to unseen tasks, 2) weak WKM can guide strong agent model planning, and 3) unified WKM training has promising potential for further development. The code is available at https://github.com/zjunlp/WKM.

------

Title: Training LLM Agents for Spontaneous, Reward-Free Self-Evolution via World Knowledge Exploration

URL: https://www.semanticscholar.org/paper/28b4eaa34c8918550420d1391071561432ff4cad

Abstract: Most agents today ``self-evolve''by following rewards and rules defined by humans. However, this process remains fundamentally dependent on external supervision; without human guidance, the evolution stops. In this work, we train agents to possess an intrinsic meta-evolution capability to spontaneously learn about unseen environments prior to task execution. To instill this ability, we design an outcome-based reward mechanism that measures how much an agent's self-generated world knowledge improves its success rate on downstream tasks. This reward signal is used exclusively during the training phase to teach the model how to explore and summarize effectively. At inference time, the agent requires no external rewards or human instructions. It spontaneously performs native self-evolution to adapt to unknown environments using its internal parameters. When applied to Qwen3-30B and Seed-OSS-36B, this shift to native evolution yields a 20% performance increase on WebVoyager and WebWalker. Most strikingly, the generated world knowledge even enables a compact 14B Qwen3 model to outperform the unassisted Gemini-2.5-Flash, establishing a new paradigm for truly evolving agents.

------

Title: View-oriented Conversation Compiler for Agent Trace Analysis

URL: https://www.semanticscholar.org/paper/e9e0b1e0aaceb9823d47e4ec43d33d2601b9a96c

Abstract: Agent traces carry increasing analytical value in agentic systems and context engineering, yet most prior work treats conversation format as a trivial implementation detail. Modern agent conversations, however, contain deeply structured content, including nested tool calls and results, chain-of-thought reasoning blocks, sub-agent invocations, context-window compaction boundaries, and harness-injected system directives, whose complexity far exceeds that of simple user-assistant exchanges. Feeding such traces to a reflector or other analytical mechanism in plain text, JSON, YAML, or via grep can materially degrade analysis quality. This paper presents VCC (View-oriented Conversation Compiler), a compiler (lex, parse, IR, lower, emit) that transforms raw agent JSONL logs into a family of structured views: a full view (lossless transcript serving as the canonical line-number coordinate system), a user-interface (UI) view (reconstructing the interaction as the user actually perceived it), and an adaptive view (a structure-preserving projection governed by a relevance predicate). In a context-engineering experiment on AppWorld, replacing only the reflector's input format, from raw JSONL to VCC-compiled views, leads to higher pass rates across all three model configurations tested, while cutting reflector token consumption by half to two-thirds and producing more concise learned memory. These results suggest that message format functions as infrastructure for context engineering, not as an incidental implementation choice.

------

Title: PlugMem: A Task-Agnostic Plugin Memory Module for LLM Agents

URL: https://www.semanticscholar.org/paper/6ae3fb18300289acc53af5535508500992aa185c

Abstract: Long-term memory is essential for large language model (LLM) agents operating in complex environments, yet existing memory designs are either task-specific and non-transferable, or task-agnostic but less effective due to low task-relevance and context explosion from raw memory retrieval. We propose PlugMem, a task-agnostic plugin memory module that can be attached to arbitrary LLM agents without task-specific redesign. Motivated by the fact that decision-relevant information is concentrated as abstract knowledge rather than raw experience, we draw on cognitive science to structure episodic memories into a compact, extensible knowledge-centric memory graph that explicitly represents propositional and prescriptive knowledge. This representation enables efficient memory retrieval and reasoning over task-relevant knowledge, rather than verbose raw trajectories, and departs from other graph-based methods like GraphRAG by treating knowledge as the unit of memory access and organization instead of entities or text chunks. We evaluate PlugMem unchanged across three heterogeneous benchmarks (long-horizon conversational question answering, multi-hop knowledge retrieval, and web agent tasks). The results show that PlugMem consistently outperforms task-agnostic baselines and exceeds task-specific memory designs, while also achieving the highest information density under a unified information-theoretic analysis. Code and data are available at https://github.com/TIMAN-group/PlugMem.

------

Title: SkillCraft: Can LLM Agents Learn to Use Tools Skillfully?

URL: https://doi.org/10.48550/arXiv.2603.00718

Abstract: Real-world tool-using agents operate over long-horizon workflows with recurring structure and diverse demands, where effective behavior requires not only invoking atomic tools but also abstracting, and reusing higher-level tool compositions. However, existing benchmarks mainly measure instance-level success under static tool sets, offering limited insight into agents'ability to acquire such reusable skills. We address this gap by introducing SkillCraft, a benchmark explicitly stress-test agent ability to form and reuse higher-level tool compositions, where we call Skills. SkillCraft features realistic, highly compositional tool-use scenarios with difficulty scaled along both quantitative and structural dimensions, designed to elicit skill abstraction and cross-task reuse. We further propose a lightweight evaluation protocol that enables agents to auto-compose atomic tools into executable Skills, cache and reuse them inside and across tasks, thereby improving efficiency while accumulating a persistent library of reusable skills. Evaluating state-of-the-art agents on SkillCraft, we observe substantial efficiency gains, with token usage reduced by up to 80% by skill saving and reuse. Moreover, success rate strongly correlates with tool composition ability at test time, underscoring compositional skill acquisition as a core capability.

------

Title: WorkflowGen:an adaptive workflow generation mechanism driven by trajectory experience

URL: https://www.semanticscholar.org/paper/5bf8397a0dc2ebb22480f51abf63a0140274b9b8

Abstract: Large language model (LLM) agents often suffer from high reasoning overhead, excessive token consumption, unstable execution, and inability to reuse past experiences in complex tasks like business queries, tool use, and workflow orchestration. Traditional methods generate workflows from scratch for every query, leading to high cost, slow response, and poor robustness. We propose WorkflowGen, an adaptive, trajectory experience-driven framework for automatic workflow generation that reduces token usage and improves efficiency and success rate. Early in execution, WorkflowGen captures full trajectories and extracts reusable knowledge at both node and workflow levels, including error fingerprints, optimal tool mappings, parameter schemas, execution paths, and exception-avoidance strategies. It then employs a closed-loop mechanism that performs lightweight generation only on variable nodes via trajectory rewriting, experience updating, and template induction. A three-tier adaptive routing strategy dynamically selects among direct reuse, rewriting-based generation, and full initialization based on semantic similarity to historical queries. Without large annotated datasets, we qualitatively compare WorkflowGen against real-time planning, static single trajectory, and basic in-context learning baselines. Our method reduces token consumption by over 40 percent compared to real-time planning, improves success rate by 20 percent on medium-similarity queries through proactive error avoidance and adaptive fallback, and enhances deployability via modular, traceable experiences and cross-scenario adaptability. WorkflowGen achieves a practical balance of efficiency, robustness, and interpretability, addressing key limitations of existing approaches.

------

Title: GUI-ReWalk: Massive Data Generation for GUI Agent via Stochastic Exploration and Intent-Aware Reasoning

URL: https://doi.org/10.48550/arXiv.2509.15738

Abstract: Graphical User Interface (GUI) Agents, powered by large language and vision-language models, hold promise for enabling end-to-end automation in digital environments. However, their progress is fundamentally constrained by the scarcity of scalable, high-quality trajectory data. Existing data collection strategies either rely on costly and inconsistent manual annotations or on synthetic generation methods that trade off between diversity and meaningful task coverage. To bridge this gap, we present GUI-ReWalk: a reasoning-enhanced, multi-stage framework for synthesizing realistic and diverse GUI trajectories. GUI-ReWalk begins with a stochastic exploration phase that emulates human trial-and-error behaviors, and progressively transitions into a reasoning-guided phase where inferred goals drive coherent and purposeful interactions. Moreover, it supports multi-stride task generation, enabling the construction of long-horizon workflows across multiple applications. By combining randomness for diversity with goal-aware reasoning for structure, GUI-ReWalk produces data that better reflects the intent-aware, adaptive nature of human-computer interaction. We further train Qwen2.5-VL-7B on the GUI-ReWalk dataset and evaluate it across multiple benchmarks, including Screenspot-Pro, OSWorld-G, UI-Vision, AndroidControl, and GUI-Odyssey. Results demonstrate that GUI-ReWalk enables superior coverage of diverse interaction flows, higher trajectory entropy, and more realistic user intent. These findings establish GUI-ReWalk as a scalable and data-efficient framework for advancing GUI agent research and enabling robust real-world automation.

------

Title: AutoHarness: improving LLM agents by automatically synthesizing a code harness

URL: https://www.semanticscholar.org/paper/f883b7e4d11da6dfd34c17cde0a7b55f10b546d6

Abstract: Despite significant strides in language models in the last few years, when used as agents, such models often try to perform actions that are not just suboptimal for a given state, but are strictly prohibited by the external environment. For example, in the recent Kaggle GameArena chess competition, 78% of Gemini-2.5-Flash losses were attributed to illegal moves. Often people manually write"harnesses"around LLMs to prevent such failures. In this paper, we demonstrate that Gemini-2.5-Flash can automatically synthesize such a code harness, using a small number of rounds of iterative code refinement given feedback from the (game) environment. The resulting harness prevents all illegal moves in 145 different TextArena games (both 1-player and 2-player), enabling the smaller Gemini-2.5-Flash model to outperform larger models, such as Gemini-2.5-Pro. Pushing our technique to the limit, we can get Gemini-2.5-Flash to generate the entire policy in code, thus eliminating the need to use the LLM at decision making time. The resulting code-policy receives a higher average reward than Gemini-2.5-Pro and GPT-5.2-High on 16 TextArena 1-player games. Our results show that using a smaller model to synthesize a custom code harness (or entire policy) can outperform a much larger model, while also being more cost effective.

------

Title: REVERE: Reflective Evolving Research Engineer for Scientific Workflows

URL: https://www.semanticscholar.org/paper/b5d5a21835a527cb2a90225db589eb91d5dd4168

Abstract: Existing prompt-optimization techniques rely on local signals to update behavior, often neglecting broader and recurring patterns across tasks, leading to poor generalization; they further rely on full-prompt rewrites or unstructured merges, resulting in knowledge loss. These limitations are magnified in research-coding workflows, which involve heterogeneous repositories, underspecified environments, and weak feedback, where reproducing results from public codebases is an established evaluation regime. We introduce Reflective Evolving Research Engineer (REVERE), a framework that continuously learns from Global Training Context, recognizes recurring failure modes in cross-repository execution trajectories, distills them into reusable heuristics, and performs targeted edits across three configurable fields: the system prompt, a task-prompt template, and a cumulative cheatsheet. REVERE, via this reflective optimization framework, improves performance over prior state-of-the-art expert-crafted instructions on research coding tasks by 4.50% on SUPER, 3.51% on ResearchCodeBench, and 4.89% on ScienceAgentBench across their respective metrics. These results demonstrate that agents equipped with mechanisms for continual learning and global memory consolidation can meaningfully evolve their capabilities over time.

------

Title: Towards Reliable Generation of Executable Workflows by Foundation Models

URL: https://doi.org/10.1145/3809500

Abstract: Recent advancements in Foundation Models (FMs) have demonstrated significant progress in processing complex natural language to perform intricate tasks. Successfully executing these tasks often requires orchestrating calls to FMs alongside other software components. However, manually decomposing a task into a coherent sequence of smaller, logically aggregated steps, commonly referred to as workflows, demands considerable effort and specialized domain knowledge. While FMs can assist in generating such workflows specified in domain-specific languages (DSLs), achieving accuracy and reliability in this process remains a challenge. We introduce a framework that leverages static analysis feedback to enable FMs to detect and repair defects in the DSL-based workflows they generate. We begin by presenting an initial taxonomy of incidences of defects in FM-generated DSL workflows, categorizing them into 20 distinct types. Furthermore, we observe a high prevalence of defects across FM-generated DSL workflows, with \(89.23\) % of the studied instances containing at least one defect. This high prevalence underscores the magnitude of the problem and the necessity for mitigation strategies. Following this, we demonstrate that nine types of these defects can be effectively identified through static analysis of the workflows. For this purpose, we develop Timon, the first-of-its-kind static analyzer specifically designed for FM-generated DSL workflows. Finally, we show that by incorporating feedback from Timon, we can guide Pumbaa, an FM-based tool, to repair the detected defect incidences. By systematically detecting and repairing defects, our work provides a crucial step towards the reliable and automated generation of executable workflows from natural language requirements.

------

Title: UMEM: Unified Memory Extraction and Management Framework for Generalizable Memory

URL: https://doi.org/10.48550/arXiv.2602.10652

Abstract: Self-evolving memory serves as the trainable parameters for Large Language Models (LLMs)-based agents, where extraction (distilling insights from experience) and management (updating the memory bank) must be tightly coordinated. Existing methods predominately optimize memory management while treating memory extraction as a static process, resulting in poor generalization, where agents accumulate instance-specific noise rather than robust memories. To address this, we propose Unified Memory Extraction and Management (UMEM), a self-evolving agent framework that jointly optimizes a Large Language Model to simultaneous extract and manage memories. To mitigate overfitting to specific instances, we introduce Semantic Neighborhood Modeling and optimize the model with a neighborhood-level marginal utility reward via GRPO. This approach ensures memory generalizability by evaluating memory utility across clusters of semantically related queries. Extensive experiments across five benchmarks demonstrate that UMEM significantly outperforms highly competitive baselines, achieving up to a 10.67% improvement in multi-turn interactive tasks. Futhermore, UMEM maintains a monotonic growth curve during continuous evolution. Codes and models will be publicly released.

------

Title: ELITE: Experiential Learning and Intent-Aware Transfer for Self-improving Embodied Agents

URL: https://www.semanticscholar.org/paper/7d11de2c422dbcaafa40bcb341f7ad705d3300c1

Abstract: Vision-language models (VLMs) have shown remarkable general capabilities, yet embodied agents built on them fail at complex tasks, often skipping critical steps, proposing invalid actions, and repeating mistakes. These failures arise from a fundamental gap between the static training data of VLMs and the physical interaction for embodied tasks. VLMs can learn rich semantic knowledge from static data but lack the ability to interact with the world. To address this issue, we introduce ELITE, an embodied agent framework with {E}xperiential {L}earning and {I}ntent-aware {T}ransfer that enables agents to continuously learn from their own environment interaction experiences, and transfer acquired knowledge to procedurally similar tasks. ELITE operates through two synergistic mechanisms, \textit{i.e.,} self-reflective knowledge construction and intent-aware retrieval. Specifically, self-reflective knowledge construction extracts reusable strategies from execution trajectories and maintains an evolving strategy pool through structured refinement operations. Then, intent-aware retrieval identifies relevant strategies from the pool and applies them to current tasks. Experiments on the EB-ALFRED and EB-Habitat benchmarks show that ELITE achieves 9\% and 5\% performance improvement over base VLMs in the online setting without any supervision. In the supervised setting, ELITE generalizes effectively to unseen task categories, achieving better performance compared to state-of-the-art training-based methods. These results demonstrate the effectiveness of ELITE for bridging the gap between semantic understanding and reliable action execution.

------

Title: Compiling Deterministic Structure into SLM Harnesses

URL: https://www.semanticscholar.org/paper/2120c387ce45f48d25b67dec45f5b1831327068c

Abstract: Enterprise SLM deployment faces epistemic asymmetry: small models cannot self-correct reasoning errors, while frontier LLMs incur prohibitive costs and data sovereignty risks at scale. We propose Semantic Gradient Descent (SGDe), a teacher-student framework that compiles agentic workflows into discrete execution plans--DAG topologies, system prompts, and deterministic code. The trailing e distinguishes this discrete, compilation-based approach from stochastic gradient descent. Operating in discrete semantic space, a frontier teacher generates natural-language critiques that serve as directional gradients to iteratively refine the SLM's workflow artefacts. We formalise SGDe under PAC learning, establishing sample-complexity bounds that enable convergence with as few as three training examples by leveraging the teacher as a statistical prior. On an adversarially synthesized GSM-Hard test set, compiled workflows achieve 91.3% accuracy at m=5 and 99.3% at m=3--a +26.3% to +34.3% absolute gain over state-of-the-art prompt optimisers. Within harness engineering, SGDe treats deterministic code placement (which subtasks to delegate to Python versus retain as LLM calls) as a trace-driven, per-node optimisation target, generalising static whole-problem offloading in PAL and PoT. The teacher compiles two deterministic structures: capability offloading (delegating subtasks to Python when the SLM is unreliable) and structural consensus (wrapping variance-sensitive steps in fan-out/fan-in subgraphs with deterministic voting).

------

Title: From Experience to Strategy: Empowering LLM Agents with Trainable Graph Memory

URL: https://doi.org/10.48550/arXiv.2511.07800

Abstract: Large Language Models (LLMs) based agents have demonstrated remarkable potential in autonomous task-solving across complex, open-ended environments. A promising approach for improving the reasoning capabilities of LLM agents is to better utilize prior experiences in guiding current decisions. However, LLMs acquire experience either through implicit memory via training, which suffers from catastrophic forgetting and limited interpretability, or explicit memory via prompting, which lacks adaptability. In this paper, we introduce a novel agent-centric, trainable, multi-layered graph memory framework and evaluate how context memory enhances the ability of LLMs to utilize parametric information. The graph abstracts raw agent trajectories into structured decision paths in a state machine and further distills them into high-level, human-interpretable strategic meta-cognition. In order to make memory adaptable, we propose a reinforcement-based weight optimization procedure that estimates the empirical utility of each meta-cognition based on reward feedback from downstream tasks. These optimized strategies are then dynamically integrated into the LLM agent's training loop through meta-cognitive prompting. Empirically, the learnable graph memory delivers robust generalization, improves LLM agents'strategic reasoning performance, and provides consistent benefits during Reinforcement Learning (RL) training.

------

Title: EchoTrail-GUI: Building Actionable Memory for GUI Agents via Critic-Guided Self-Exploration

URL: https://doi.org/10.48550/arXiv.2512.19396

Abstract: Contemporary GUI agents, while increasingly capable due to advances in Large Vision-Language Models (VLMs), often operate with a critical limitation: they treat each task in isolation, lacking a mechanism to systematically learn from past successes. This digital''amnesia''results in sub-optimal performance, repeated errors, and poor generalization to novel challenges. To bridge this gap, we introduce EchoTrail-GUI, a novel framework designed to mimic human-like experiential learning by equipping agents with a dynamic, accessible memory. Our framework operates in three distinct stages. First, during Experience Exploration, an agent autonomously interacts with GUI environments to build a curated database of successful task trajectories, validated by a reward model. Crucially, the entire knowledge base construction is thus fully automated, requiring no human supervision. Second, in the Memory Injection stage, upon receiving a new task, our system efficiently retrieves the most relevant past trajectories to serve as actionable''memories''. Finally, during GUI Task Inference, these memories are injected as in-context guidance to inform the agent's reasoning and decision-making process. We demonstrate the efficacy of our approach on benchmarks including Android World and AndroidLab. The results show that EchoTrail-GUI significantly improves the task success rate and operational efficiency of baseline agents, validating the power of structured memory in creating more robust and intelligent GUI automation.

------

Title: AgentSynth: Scalable Task Generation for Generalist Computer-Use Agents

URL: https://doi.org/10.48550/arXiv.2506.14205

Abstract: We introduce AgentSynth, a scalable and cost-efficient pipeline for automatically synthesizing high-quality tasks and trajectory datasets for generalist computer-use agents. Leveraging information asymmetry, AgentSynth constructs subtasks that are simple during generation but significantly more challenging when composed into long-horizon tasks, enabling the creation of over 6,000 diverse and realistic tasks. A key strength of AgentSynth is its ability to precisely modulate task complexity by varying the number of subtasks. Empirical evaluations show that state-of-the-art LLM agents suffer a steep performance drop, from 18% success at difficulty level 1 to just 4% at level 6, highlighting the benchmark's difficulty and discriminative power. Moreover, our pipeline achieves a low average cost of $0.60 per trajectory, orders of magnitude cheaper than human annotations. Our code and data are available at https://github.com/sunblaze-ucb/AgentSynth

------

Title: AutoSkill: Experience-Driven Lifelong Learning via Skill Self-Evolution

URL: https://doi.org/10.48550/arXiv.2603.01145

Abstract: In practical LLM applications, users repeatedly express stable preferences and requirements, such as reducing hallucinations, following institutional writing conventions, or avoiding overly technical wording, yet such interaction experience is seldom consolidated into reusable knowledge. Consequently, LLM agents often fail to accumulate personalized capabilities across sessions. We present AutoSkill, an experience-driven lifelong learning framework that enables LLM agents to automatically derive, maintain, and reuse skills from dialogue and interaction traces. AutoSkill abstracts skills from user experience, supports their continual self-evolution, and dynamically injects relevant skills into future requests without retraining the underlying model. Designed as a model-agnostic plugin layer, it is compatible with existing LLMs and introduces a standardized skill representation for sharing and transfer across agents, users, and tasks. In this way, AutoSkill turns ephemeral interaction experience into explicit, reusable, and composable capabilities. This paper describes the motivation, architecture, skill lifecycle, and implementation of AutoSkill, and positions it with respect to prior work on memory, retrieval, personalization, and agentic systems. AutoSkill highlights a practical and scalable path toward lifelong personalized agents and personal digital surrogates.

------

Title: Unlocking Implicit Experience: Synthesizing Tool-Use Trajectories from Text

URL: https://doi.org/10.48550/arXiv.2601.10355

Abstract: Enabling Large Language Models (LLMs) to effectively utilize tools in multi-turn interactions is essential for building capable autonomous agents. However, acquiring diverse and realistic multi-turn tool-use data remains a significant challenge. In this work, we propose a novel text-based paradigm. We observe that textual corpora naturally contain rich, multi-step problem-solving experiences, which can serve as an untapped, scalable, and authentic data source for multi-turn tool-use tasks. Based on this insight, we introduce GEM, a data synthesis pipeline that enables the generation and extraction of multi-turn tool-use trajectories from text corpora through a four-stage process: relevance filtering, workflow&tool extraction, trajectory grounding, and complexity refinement. To reduce the computational cost, we further train a specialized Trajectory Synthesizer via supervised fine-tuning. This model distills the complex generation pipeline into an efficient, end-to-end trajectory generator. Experiments demonstrate that our GEM-32B achieve a 16.5% improvement on the BFCL V3 Multi-turn benchmark. Our models partially surpass the performance of models trained on {\tau} - bench (Airline and Retail) in-domain data, highlighting the superior generalization capability derived from our text-based synthesis paradigm. Notably, our Trajectory Synthesizer matches the quality of the full pipeline while significantly reducing inference latency and costs.

------

Title: Fara-7B: An Efficient Agentic Model for Computer Use

URL: https://doi.org/10.48550/arXiv.2511.19663

Abstract: Progress in computer use agents (CUAs) has been constrained by the absence of large and high-quality datasets that capture how humans interact with a computer. While LLMs have thrived on abundant textual data, no comparable corpus exists for CUA trajectories. To address these gaps, we introduce FaraGen, a novel synthetic data generation system for multi-step web tasks. FaraGen can propose diverse tasks from frequently used websites, generate multiple solution attempts, and filter successful trajectories using multiple verifiers. It achieves high throughput, yield, and diversity for multi-step web tasks, producing verified trajectories at approximately $1 each. We use this data to train Fara-7B, a native CUA model that perceives the computer using only screenshots, executes actions via predicted coordinates, and is small enough to run on-device. We find that Fara-7B outperforms other CUA models of comparable size on benchmarks like WebVoyager, Online-Mind2Web, and WebTailBench -- our novel benchmark that better captures under-represented web tasks in pre-existing benchmarks. Furthermore, Fara-7B is competitive with much larger frontier models, illustrating key benefits of scalable data generation systems in advancing small efficient agentic models. We are making Fara-7B open-weight on Microsoft Foundry and HuggingFace, and we are releasing WebTailBench.

------

Title: ToolMind Technical Report: A Large-Scale, Reasoning-Enhanced Tool-Use Dataset

URL: https://doi.org/10.48550/arXiv.2511.15718

Abstract: Large Language Model (LLM) agents have developed rapidly in recent years to solve complex real-world problems using external tools. However, the scarcity of high-quality trajectories still hinders the development of stronger LLM agents. Most existing works on multi-turn dialogue synthesis validate correctness only at the trajectory level, which may overlook turn-level errors that can propagate during training and degrade model performance. To address these limitations, we introduce ToolMind, a large-scale, high-quality tool-agentic dataset with 160k synthetic data instances generated using over 20k tools and 200k augmented open-source data instances. Our data synthesis pipeline first constructs a function graph based on parameter correlations and then uses a multi-agent framework to simulate realistic user-assistant-tool interactions. Beyond trajectory-level validation, we employ fine-grained turn-level filtering to remove erroneous or suboptimal steps, ensuring that only high-quality reasoning traces are retained. This approach mitigates error amplification during training while preserving self-corrective reasoning signals essential for robust tool-use learning. Models fine-tuned on ToolMind show significant improvements over baselines on several benchmarks.

------

Title: TED: Training-Free Experience Distillation for Multimodal Reasoning

URL: https://www.semanticscholar.org/paper/c949c744cc5aa59c9037a36024326f60f8546438

Abstract: Knowledge distillation is typically realized by transferring a teacher model's knowledge into a student's parameters through supervised or reinforcement-based optimization. While effective, such approaches require repeated parameter updates and large-scale training data, limiting their applicability in resource-constrained environments. In this work, we propose TED, a training-free, context-based distillation framework that shifts the update target of distillation from model parameters to an in-context experience injected into the student's prompt. For each input, the student generates multiple reasoning trajectories, while a teacher independently produces its own solution. The teacher then compares the student trajectories with its reasoning and the ground-truth answer, extracting generalized experiences that capture effective reasoning patterns. These experiences are continuously refined and updated over time. A key challenge of context-based distillation is unbounded experience growth and noise accumulation. TED addresses this with an experience compression mechanism that tracks usage statistics and selectively merges, rewrites, or removes low-utility experiences. Experiments on multimodal reasoning benchmarks MathVision and VisualPuzzles show that TED consistently improves performance. On MathVision, TED raises the performance of Qwen3-VL-8B from 0.627 to 0.702, and on VisualPuzzles from 0.517 to 0.561 with just 100 training samples. Under this low-data, no-update setting, TED achieves performance competitive with fully trained parameter-based distillation while reducing training cost by over 5x, demonstrating that meaningful knowledge transfer can be achieved through contextual experience.

------

Title: ASDA: Automated Skill Distillation and Adaptation for Financial Reasoning

URL: https://www.semanticscholar.org/paper/960b5b192d32ad89eff70f2f87cd06d127ac9ebc

Abstract: Adapting large language models (LLMs) to specialized financial reasoning typically requires expensive fine-tuning that produces model-locked expertise. Training-free alternatives have emerged, yet our experiments show that leading methods (GEPA and ACE) achieve only marginal gains on the FAMMA financial reasoning benchmark, exposing the limits of unstructured text optimization for complex, multi-step domain reasoning. We introduce Automated Skill Distillation and Adaptation (ASDA), a framework that automatically generates structured skill artifacts through iterative error-corrective learning without modifying model weights. A teacher model analyzes a student model's failures on financial reasoning tasks, clusters errors by subfield and error type, and synthesizes skill files containing reasoning procedures, code templates, and worked examples, which are dynamically injected during inference. Evaluated on FAMMA, ASDA achieves up to +17.33% improvement on arithmetic reasoning and +5.95% on non-arithmetic reasoning, substantially outperforming all training-free baselines. The resulting skill artifacts are human-readable, version-controlled, and compatible with the Agent Skills open standard, offering any organization with a labeled domain dataset a practical and auditable path to domain adaptation without weight access or retraining.

------

Title: Controllable and Verifiable Tool-Use Data Synthesis for Agentic Reinforcement Learning

URL: https://www.semanticscholar.org/paper/fd2ca5fb1acdafabd05a79286e4449017aaeba2c

Abstract: Existing synthetic tool-use corpora are primarily designed for offline supervised fine-tuning, yet reinforcement learning (RL) requires executable environments that support reward-checkable online rollouts. We propose COVERT, a two-stage pipeline that first generates reliable base tool-use trajectories through self-evolving synthesis with multi-level validation, and then applies oracle-preserving augmentations that systematically increase environmental complexity. These augmentations introduce distractor tools, indirect or ambiguous user queries, and noisy, multi-format, or erroneous tool outputs, while strictly preserving oracle tool calls and final answers as ground truth. This design enables automatic reward computation via reference matching for standard cases and lightweight judge-assisted verification for special behaviors such as error detection, supporting RL optimization of tool-calling policies. On Qwen2.5-Instruct-14B, COVERT-RL improves overall accuracy on BFCL v3 from 56.5 to 59.9 and on ACEBench from 53.0 to 59.3, with minimal regressions on general-ability benchmarks; when stacked on SFT, it further reaches 62.1 and 61.8, confirming additive gains. These results suggest that oracle-preserving synthetic environments offer a practical RL refinement stage, complementary to SFT, for improving tool-use robustness under ambiguity and unreliable tool feedback.

------

Title: ASTRA: Automated Synthesis of agentic Trajectories and Reinforcement Arenas

URL: https://doi.org/10.48550/arXiv.2601.21558

Abstract: Large language models (LLMs) are increasingly used as tool-augmented agents for multi-step decision making, yet training robust tool-using agents remains challenging. Existing methods still require manual intervention, depend on non-verifiable simulated environments, rely exclusively on either supervised fine-tuning (SFT) or reinforcement learning (RL), and struggle with stable long-horizon, multi-turn learning. To address these challenges, we introduce ASTRA, a fully automated end-to-end framework for training tool-augmented language model agents via scalable data synthesis and verifiable reinforcement learning. ASTRA integrates two complementary components. First, a pipeline that leverages the static topology of tool-call graphs synthesizes diverse, structurally grounded trajectories, instilling broad and transferable tool-use competence. Second, an environment synthesis framework that captures the rich, compositional topology of human semantic reasoning converts decomposed question-answer traces into independent, code-executable, and rule-verifiable environments, enabling deterministic multi-turn RL. Based on this method, we develop a unified training methodology that integrates SFT with online RL using trajectory-level rewards to balance task completion and interaction efficiency. Experiments on multiple agentic tool-use benchmarks demonstrate that ASTRA-trained models achieve state-of-the-art performance at comparable scales, approaching closed-source systems while preserving core reasoning ability. We release the full pipelines, environments, and trained models at https://github.com/LianjiaTech/astra.

------

Title: Embodied CoT Distillation From LLM To Off-the-shelf Agents

URL: https://doi.org/10.48550/arXiv.2412.11499

Abstract: We address the challenge of utilizing large language models (LLMs) for complex embodied tasks, in the environment where decision-making systems operate timely on capacity-limited, off-the-shelf devices. We present DeDer, a framework for decomposing and distilling the embodied reasoning capabilities from LLMs to efficient, small language model (sLM)-based policies. In DeDer, the decision-making process of LLM-based strategies is restructured into a hierarchy with a reasoning-policy and planning-policy. The reasoning-policy is distilled from the data that is generated through the embodied in-context learning and self-verification of an LLM, so it can produce effective rationales. The planning-policy, guided by the rationales, can render optimized plans efficiently. In turn, DeDer allows for adopting sLMs for both policies, deployed on off-the-shelf devices. Furthermore, to enhance the quality of intermediate rationales, specific to embodied tasks, we devise the embodied knowledge graph, and to generate multiple rationales timely through a single inference, we also use the contrastively prompted attention model. Our experiments with the ALFRED benchmark demonstrate that DeDer surpasses leading language planning and distillation approaches, indicating the applicability and efficiency of sLM-based embodied policies derived through DeDer.

------

Title: Scalable Data Synthesis for Computer Use Agents with Step-Level Filtering

URL: https://doi.org/10.48550/arXiv.2512.10962

Abstract: Computer use agents (CUAs) can operate real-world digital interfaces but remain difficult to train due to the high cost of graphical user interface (GUI) interaction and the scarcity of high-quality trajectory data. Existing datasets rely on human demonstrations, limiting scalability. A natural alternative is to synthesize data from strong CUAs, yet their rollouts are highly noisy, with incorrect or suboptimal actions consisting a large proportion of the steps, making naive imitation ineffective. To tackle this challenge, we introduce a scalable data synthesis pipeline that transforms noisy rollouts into reliable supervision without human annotation. The core idea is step-level filtering, which evaluates actions individually to retain only correct steps, complemented by reasoning augmentation for improved planning. Using this pipeline, we construct WebSTAR, a dataset of 13.3K trajectories and 267K graded, reasoning-rich steps synthesized from OpenAI's computer-use-preview model. We train Qwen-2.5-VL-Instruct models (7B and 32B) on WebSTAR. On WebVoyager, our 7B model surpasses SoTA open-source CUA model UI-TARS-1.5-7B by more than 15% with only supervised finetuning. Building on step-level grading, we further create WebSCORE, a dataset of graded step-level actions, and train StepRM, a 7B multimodal process reward model distilled from o4-mini, which matches its grading quality while being far more efficient to deploy at scale. Our results establish step-level filtering as a key principle for scalable CUA training and construct two new datasets (WebSTAR, WebSCORE) and a lightweight process reward model (StepRM) as practical tools to advance robust and efficient CUAs.

------

Title: Symbiotic Cooperation for Web Agents: Harnessing Complementary Strengths of Large and Small LLMs

URL: https://doi.org/10.48550/arXiv.2502.07942

Abstract: Web browsing agents powered by large language models (LLMs) have shown tremendous potential in automating complex web-based tasks. Existing approaches typically rely on large LLMs (e.g., GPT-4o) to explore web environments and generate trajectory data, which is then used either for demonstration retrieval (for large LLMs) or to distill small LLMs (e.g., Llama3) in a process that remains decoupled from the exploration. In this paper, we propose AgentSymbiotic, an iterative framework that couples data synthesis with task-performance, yielding a"symbiotic improvement"for both large and small LLMs. Our study uncovers a complementary dynamic between LLM types: while large LLMs excel at generating high-quality trajectories for distillation, the distilled small LLMs-owing to their distinct reasoning capabilities-often choose actions that diverge from those of their larger counterparts. This divergence drives the exploration of novel trajectories, thereby enriching the synthesized data. However, we also observe that the performance of small LLMs becomes a bottleneck in this iterative enhancement process. To address this, we propose two innovations in LLM distillation: a speculative data synthesis strategy that mitigates off-policy bias, and a multi-task learning approach designed to boost the reasoning capabilities of the student LLM. Furthermore, we introduce a Hybrid Mode for Privacy Preservation to address user privacy concerns. Evaluated on the WEBARENA benchmark, AgentSymbiotic achieves SOTA performance with both LLM types. Our best Large LLM agent reaches 52%, surpassing the previous best of 45%, while our 8B distilled model demonstrates a competitive 49%, exceeding the prior best of 28%. Code will be released upon acceptance.

------

Title: EvoSkill: Automated Skill Discovery for Multi-Agent Systems

URL: https://www.semanticscholar.org/paper/ce14734e615b845ec2471d9dc3f35d3d68dd5c22

Abstract: Coding agents are increasingly used as general-purpose problem solvers, but their flexibility does not by itself confer the domain expertise needed for specialized tasks. Recent work addresses this through \textit{agent skills}: reusable workflows, and code, that augment agents with domain-specific capabilities. Most skills today are hand-crafted, and existing evolutionary approaches optimize low-level artifacts (e.g. prompts \&code) that are tightly coupled to specific models and tasks. We introduce \textbf{EvoSkill}, a self-evolving framework that automatically discovers and refines agent skills through iterative failure analysis. EvoSkill analyzes execution failures, proposes new skills or edits to existing ones, and materializes them into structured, reusable skill folders. A Pareto frontier of agent programs governs selection, retaining only skills that improve held-out validation performance while the underlying model remains frozen. We evaluate EvoSkill on two benchmarks: OfficeQA, a grounded reasoning benchmark over U.S.\ Treasury data, where it improves exact-match accuracy by \textbf{7.3\%} (60.6\% $\to$ 67.9\%); and SealQA, a search-augmented QA benchmark with noisy retrieval, where it yields a \textbf{12.1\%} gain (26.6\% $\to$ 38.7\%). We also investigate the zero-shot transfer capabilties of skills evolved on one task to the other; in particular: skills evolved from SealQA transfers zero-shot to BrowseComp, improving accuracy by \textbf{5.3\%} without modification demonstrating that skill-level optimization produces transferable capabilities beyond the training task.

------

Title: WebWorld: A Large-Scale World Model for Web Agent Training

URL: https://doi.org/10.48550/arXiv.2602.14721

Abstract: Web agents require massive trajectories to generalize, yet real-world training is constrained by network latency, rate limits, and safety risks. We introduce \textbf{WebWorld} series, the first open-web simulator trained at scale. While existing simulators are restricted to closed environments with thousands of trajectories, WebWorld leverages a scalable data pipeline to train on 1M+ open-web interactions, supporting reasoning, multi-format data, and long-horizon simulations of 30+ steps. For intrinsic evaluation, we introduce WebWorld-Bench with dual metrics spanning nine dimensions, where WebWorld achieves simulation performance comparable to Gemini-3-Pro. For extrinsic evaluation, Qwen3-14B trained on WebWorld-synthesized trajectories improves by +9.2\% on WebArena, reaching performance comparable to GPT-4o. WebWorld enables effective inference-time search, outperforming GPT-5 as a world model. Beyond web simulation, WebWorld exhibits cross-domain generalization to code, GUI, and game environments, providing a replicable recipe for world model construction.

------

Title: Scaling Web Agent Training through Automatic Data Generation and Fine-grained Evaluation

URL: https://doi.org/10.48550/arXiv.2602.12544

Abstract: We present a scalable pipeline for automatically generating high-quality training data for web agents. In particular, a major challenge in identifying high-quality training instances is trajectory evaluation - quantifying how much progress was made towards task completion. We introduce a novel constraint-based evaluation framework that provides fine-grained assessment of progress towards task completion. This enables us to leverage partially successful trajectories, which significantly expands the amount of usable training data. We evaluate our method on a new benchmark we propose called BookingArena, which consists of complex booking tasks across 20 popular websites, and demonstrate that our distilled student model outperforms open-source approaches and matches or exceeds commercial systems, while being a significantly smaller model. Our work addresses the challenge of efficiently creating diverse, realistic web interaction datasets and provides a systematic evaluation methodology for complex structured web tasks.

------

Title: OpenMobile: Building Open Mobile Agents with Task and Trajectory Synthesis

URL: https://www.semanticscholar.org/paper/f34af2d16ac52c93558d81a6095e735ad2a0335a

Abstract: Mobile agents powered by vision-language models have demonstrated impressive capabilities in automating mobile tasks, with recent leading models achieving a marked performance leap, e.g., nearly 70% success on AndroidWorld. However, these systems keep their training data closed and remain opaque about their task and trajectory synthesis recipes. We present OpenMobile, an open-source framework that synthesizes high-quality task instructions and agent trajectories, with two key components: (1) The first is a scalable task synthesis pipeline that constructs a global environment memory from exploration, then leverages it to generate diverse and grounded instructions. and (2) a policy-switching strategy for trajectory rollout. By alternating between learner and expert models, it captures essential error-recovery data often missing in standard imitation learning. Agents trained on our data achieve competitive results across three dynamic mobile agent benchmarks: notably, our fine-tuned Qwen2.5-VL and Qwen3-VL reach 51.7% and 64.7% on AndroidWorld, far surpassing existing open-data approaches. Furthermore, we conduct transparent analyses on the overlap between our synthetic instructions and benchmark test sets, and verify that performance gains stem from broad functionality coverage rather than benchmark overfitting. We release data and code at https://njucckevin.github.io/openmobile/ to bridge the data gap and facilitate broader mobile agent research.

------

Title: Learning with Challenges: Adaptive Difficulty-Aware Data Generation for Mobile GUI Agent Training

URL: https://doi.org/10.48550/arXiv.2601.22781

Abstract: Large-scale, high-quality interaction trajectories are essential for advancing mobile Graphical User Interface (GUI) agents. While existing methods typically rely on labor-intensive human demonstrations or automated model exploration to generate GUI trajectories, they lack fine-grained control over task difficulty. This fundamentally restricts learning effectiveness due to the mismatch between the training difficulty and the agent's capabilities. Inspired by how humans acquire skills through progressively challenging tasks, we propose MobileGen, a novel data generation framework that adaptively aligns training difficulty with the GUI agent's capability frontier. Specifically, MobileGen explicitly decouples task difficulty into structural (e.g., trajectory length) and semantic (e.g., task goal) dimensions. It then iteratively evaluates the agent on a curated prior dataset to construct a systematic profile of its capability frontier across these two dimensions. With this profile, the probability distribution of task difficulty is adaptively computed, from which the target difficulty for the next round of training can be sampled. Guided by the sampled difficulty, a multi-agent controllable generator is finally used to synthesize high-quality interaction trajectories along with corresponding task instructions. Extensive experiments show that MobileGen consistently outperforms existing data generation methods by improving the average performance of GUI agents by 1.57 times across multiple challenging benchmarks. This highlights the importance of capability-aligned data generation for effective mobile GUI agent training.

------

Title: Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control

URL: https://www.semanticscholar.org/paper/eaa7853facb9b49444b48a96192cb4be66b62671

Abstract: Building agents with large language models (LLMs) for computer control is a burgeoning research area, where the agent receives computer states and performs actions to complete complex tasks. Previous computer agents have demonstrated the benefits of in-context learning (ICL); however, their performance is hindered by several issues. First, the limited context length of LLMs and complex computer states restrict the number of exemplars, as a single webpage can consume the entire context. Second, the exemplars in current methods, such as high-level plans and multi-choice questions, cannot represent complete trajectories, leading to suboptimal performance in long-horizon tasks. Third, existing computer agents rely on task-specific exemplars and overlook the similarity among tasks, resulting in poor generalization to novel tasks. To address these challenges, we introduce Synapse, a computer agent featuring three key components: i) state abstraction, which filters out task-irrelevant information from raw states, allowing more exemplars within the limited context, ii) trajectory-as-exemplar prompting, which prompts the LLM with complete trajectories of the abstracted states and actions to improve multi-step decision-making, and iii) exemplar memory, which stores the embeddings of exemplars and retrieves them via similarity search for generalization to novel tasks. We evaluate Synapse on MiniWoB++, a standard task suite, and Mind2Web, a real-world website benchmark. In MiniWoB++, Synapse achieves a 99.2% average success rate (a 10% relative improvement) across 64 tasks using demonstrations from only 48 tasks. Notably, Synapse is the first ICL method to solve the book-flight task in MiniWoB++. Synapse also exhibits a 56% relative improvement in average step success rate over the previous state-of-the-art prompting scheme in Mind2Web.

------

Title: SAGER: Self-Evolving User Policy Skills for Recommendation Agent

URL: https://www.semanticscholar.org/paper/f955baa78eeaefb49c0c0fd1d29056193a2ea2df

Abstract: Large language model (LLM) based recommendation agents personalize what they know through evolving per-user semantic memory, yet how they reason remains a universal, static system prompt shared identically across all users. This asymmetry is a fundamental bottleneck: when a recommendation fails, the agent updates its memory of user preferences but never interrogates the decision logic that produced the failure, leaving its reasoning process structurally unchanged regardless of how many mistakes it accumulates. To address this bottleneck, we propose SAGER (Self-Evolving Agent for Personalized Recommendation), the first recommendation agent framework in which each user is equipped with a dedicated policy skill, a structured natural-language document encoding personalized decision principles that evolves continuously through interaction. SAGER introduces a two-representation skill architecture that decouples a rich evolution substrate from a minimal inference-time injection, an incremental contrastive chain-of-thought engine that diagnoses reasoning flaws by contrasting accepted against unchosen items while preserving accumulated priors, and skill-augmented listwise reasoning that creates fine-grained decision boundaries where the evolved skill provides genuine discriminative value. Experiments on four public benchmarks demonstrate that SAGER achieves state-of-the-art performance, with gains orthogonal to memory accumulation, confirming that personalizing the reasoning process itself is a qualitatively distinct source of recommendation improvement.

------

Title: Learning to Share: Selective Memory for Efficient Parallel Agentic Systems

URL: https://doi.org/10.48550/arXiv.2602.05965

Abstract: Agentic systems solve complex tasks by coordinating multiple agents that iteratively reason, invoke tools, and exchange intermediate results. To improve robustness and solution quality, recent approaches deploy multiple agent teams running in parallel to explore diverse reasoning trajectories. However, parallel execution comes at a significant computational cost: when different teams independently reason about similar sub-problems or execute analogous steps, they repeatedly perform substantial overlapping computation. To address these limitations, in this paper, we propose Learning to Share (LTS), a learned shared-memory mechanism for parallel agentic frameworks that enables selective cross-team information reuse while controlling context growth. LTS introduces a global memory bank accessible to all teams and a lightweight controller that decides whether intermediate agent steps should be added to memory or not. The controller is trained using stepwise reinforcement learning with usage-aware credit assignment, allowing it to identify information that is globally useful across parallel executions. Experiments on the AssistantBench and GAIA benchmarks show that LTS significantly reduces overall runtime while matching or improving task performance compared to memory-free parallel baselines, demonstrating that learned memory admission is an effective strategy for improving the efficiency of parallel agentic systems. Project page: https://joefioresi718.github.io/LTS_webpage/

------

Title: SkillGraph: Self-Evolving Multi-Agent Collaboration with Multimodal Graph Topology

URL: https://www.semanticscholar.org/paper/bcff4bbe521c218a876408e3ee8d38e519f2a0d6

Abstract: Scaling vision-language models into Visual Multiagent Systems (VMAS) is hindered by two coupled issues. First, communication topologies are fixed before inference, leaving them blind to visual content and query context; second, agent reasoning abilities remain static during deployment. These issues reinforce each other: a rigid topology fails to leverage richer agent expertise, while static agents lack incentives to specialize for a given query. We address this with SkillGraph, a joint framework that evolves both agent expertise and communication topology. Within this framework, a Multimodal Graph Transformer (MMGT) encodes visual tokens, instruction semantics and active skill embeddings to predict a query-conditioned collaboration graph, replacing hand-crafted routing with dynamic, content-aware information flow. Complementing this, a Skill Designer distills and refines reasoning heuristics from failure cases, constructing a self-evolving multimodal Skill Bank. Crucially, updated skill embeddings are fed back into the MMGT, enabling the topology to adapt alongside capability growth. Experiments show that SkillGraph achieves consistent improvements across four benchmarks, five common MAS structures and four base models. Code is available at https://github.com/niez233/skillgraph.

------

Title: AdaExplore: Failure-Driven Adaptation and Diversity-Preserving Search for Efficient Kernel Generation

URL: https://www.semanticscholar.org/paper/bd2956a0c5f6788bbb18ad49fc8ce885e84c82ff

Abstract: Recent large language model (LLM) agents have shown promise in using execution feedback for test-time adaptation. However, robust self-improvement remains far from solved: most approaches still treat each problem instance independently, without accumulating reusable knowledge. This limitation is particularly pronounced in domain-specific languages such as Triton, which are underrepresented in LLM pretraining data. Their strict constraints and non-linear optimization landscape further make naive generation and local refinement unreliable. We propose AdaExplore, an agent framework that enables self-improvement via accumulated execution feedback for performance-critical kernel code generation through two complementary stages: failure-driven adaptation and diversity-preserving search, jointly improving correctness and optimization performance without additional fine-tuning or external knowledge. In the adaptation stage, the agent synthesizes tasks and converts recurring failures into a reusable memory of validity rules, helping subsequent generations remain within the feasible set. In the search stage, the agent organizes candidate kernels as a tree and alternates between small local refinements and larger structural regeneration, allowing it to explore the optimization landscape beyond local optima. Experiments on kernel runtime optimization benchmarks validate these gains: AdaExplore achieves 3.12x and 1.72x speedups on KernelBench Level-2 and Level-3, respectively, within 100 steps, and continues to improve with additional computation.

------

Title: MetaClaw: Just Talk -- An Agent That Meta-Learns and Evolves in the Wild

URL: https://www.semanticscholar.org/paper/89648e6e3aa1d96b67311ea62b3903293e6e9a89

Abstract: Large language model (LLM) agents are increasingly used for complex tasks, yet deployed agents often remain static, failing to adapt as user needs evolve. This creates a tension between the need for continuous service and the necessity of updating capabilities to match shifting task distributions. On platforms like OpenClaw, which handle diverse workloads across 20+ channels, existing methods either store raw trajectories without distilling knowledge, maintain static skill libraries, or require disruptive downtime for retraining. We present MetaClaw, a continual meta-learning framework that jointly evolves a base LLM policy and a library of reusable behavioral skills. MetaClaw employs two complementary mechanisms. Skill-driven fast adaptation analyzes failure trajectories via an LLM evolver to synthesize new skills, enabling immediate improvement with zero downtime. Opportunistic policy optimization performs gradient-based updates via cloud LoRA fine-tuning and Reinforcement Learning with a Process Reward Model (RL-PRM). This is triggered during user-inactive windows by the Opportunistic Meta-Learning Scheduler (OMLS), which monitors system inactivity and calendar data. These mechanisms are mutually reinforcing: a refined policy generates better trajectories for skill synthesis, while richer skills provide higher-quality data for policy optimization. To prevent data contamination, a versioning mechanism separates support and query data. Built on a proxy-based architecture, MetaClaw scales to production-size LLMs without local GPUs. Experiments on MetaClaw-Bench and AutoResearchClaw show that skill-driven adaptation improves accuracy by up to 32% relative. The full pipeline advances Kimi-K2.5 accuracy from 21.4% to 40.6% and increases composite robustness by 18.3%. Code is available at https://github.com/aiming-lab/MetaClaw.

------

Title: APIGen-MT: Agentic Pipeline for Multi-Turn Data Generation via Simulated Agent-Human Interplay

URL: https://doi.org/10.48550/arXiv.2504.03601

Abstract: Training effective AI agents for multi-turn interactions requires high-quality data that captures realistic human-agent dynamics, yet such data is scarce and expensive to collect manually. We introduce APIGen-MT, a two-phase framework that generates verifiable and diverse multi-turn agent data. In the first phase, our agentic pipeline produces detailed task blueprints with ground-truth actions, leveraging a committee of LLM reviewers and iterative feedback loops. These blueprints are then transformed into complete interaction trajectories through simulated human-agent interplay. We train a family of models -- the xLAM-2-fc-r series with sizes ranging from 1B to 70B parameters. Our models outperform frontier models such as GPT-4o and Claude 3.5 on $\tau$-bench and BFCL benchmarks, with the smaller models surpassing their larger counterparts, particularly in multi-turn settings, while maintaining superior consistency across multiple trials. Comprehensive experiments demonstrate that our verified blueprint-to-details approach yields high-quality training data, enabling the development of more reliable, efficient, and capable agents. We open-source 5K synthetic data trajectories and the trained xLAM-2-fc-r models to advance research in AI agents. Models at https://huggingface.co/collections/Salesforce/xlam-2-67ef5be12949d8dcdae354c4; Dataset at https://huggingface.co/datasets/Salesforce/APIGen-MT-5k and Website at https://apigen-mt.github.io

------

Title: ToolAlpaca: Generalized Tool Learning for Language Models with 3000 Simulated Cases

URL: https://doi.org/10.48550/arXiv.2306.05301

Abstract: Enabling large language models to utilize real-world tools effectively is crucial for achieving embodied intelligence. Existing approaches to tool learning have either primarily relied on extremely large language models, such as GPT-4, to attain generalized tool-use abilities in a zero-shot manner, or utilized supervised learning to train limited scopes of tools on compact models. However, it remains uncertain whether smaller language models can achieve generalized tool-use abilities without tool-specific training. To address this question, this paper introduces ToolAlpaca, a novel framework designed to automatically generate a diverse tool-use corpus and learn generalized tool-use abilities on compact language models with minimal human intervention. Specifically, ToolAlpaca first automatically creates a highly diversified tool-use corpus by building a multi-agent simulation environment. The corpus contains 3938 tool-use instances from more than 400 real-world tool APIs spanning 50 distinct categories. Subsequently, the constructed corpus is employed to fine-tune compact language models, resulting in two models, namely ToolAlpaca-7B and ToolAlpaca-13B, respectively. Finally, we evaluate the ability of these models to utilize previously unseen tools without specific training. Experimental results demonstrate that ToolAlpaca achieves effective generalized tool-use capabilities comparable to those of extremely large language models like GPT-3.5, demonstrating that learning generalized tool-use ability is feasible for compact language models.

------

Title: APIGen: Automated Pipeline for Generating Verifiable and Diverse Function-Calling Datasets

URL: https://doi.org/10.48550/arXiv.2406.18518

Abstract: The advancement of function-calling agent models requires diverse, reliable, and high-quality datasets. This paper presents APIGen, an automated data generation pipeline designed to synthesize verifiable high-quality datasets for function-calling applications. We leverage APIGen and collect 3,673 executable APIs across 21 different categories to generate diverse function-calling datasets in a scalable and structured manner. Each data in our dataset is verified through three hierarchical stages: format checking, actual function executions, and semantic verification, ensuring its reliability and correctness. We demonstrate that models trained with our curated datasets, even with only 7B parameters, can achieve state-of-the-art performance on the Berkeley Function-Calling Benchmark, outperforming multiple GPT-4 models. Moreover, our 1B model achieves exceptional performance, surpassing GPT-3.5-Turbo and Claude-3 Haiku. We release a dataset containing 60,000 high-quality entries, aiming to advance the field of function-calling agent domains. The dataset is available on Huggingface: https://huggingface.co/datasets/Salesforce/xlam-function-calling-60k and the project homepage: https://apigen-pipeline.github.io/

------

Title: ToolACE: Winning the Points of LLM Function Calling

URL: https://doi.org/10.48550/arXiv.2409.00920

Abstract: Function calling significantly extends the application boundary of large language models, where high-quality and diverse training data is critical for unlocking this capability. However, real function-calling data is quite challenging to collect and annotate, while synthetic data generated by existing pipelines tends to lack coverage and accuracy. In this paper, we present ToolACE, an automatic agentic pipeline designed to generate accurate, complex, and diverse tool-learning data. ToolACE leverages a novel self-evolution synthesis process to curate a comprehensive API pool of 26,507 diverse APIs. Dialogs are further generated through the interplay among multiple agents, guided by a formalized thinking process. To ensure data accuracy, we implement a dual-layer verification system combining rule-based and model-based checks. We demonstrate that models trained on our synthesized data, even with only 8B parameters, achieve state-of-the-art performance on the Berkeley Function-Calling Leaderboard, rivaling the latest GPT-4 models. Our model and a subset of the data are publicly available at https://huggingface.co/Team-ACE.

------

Title: Large Language Model as a Policy Teacher for Training Reinforcement Learning Agents

URL: https://doi.org/10.24963/ijcai.2024/627

Abstract: Recent studies have uncovered the potential of Large Language Models (LLMs) in addressing complex sequential decision-making tasks through the provision of high-level instructions. However, LLM-based agents lack specialization in tackling specific target problems, particularly in real-time dynamic environments. Additionally, deploying an LLM-based agent in practical scenarios can be both costly and time-consuming. On the other hand, reinforcement learning (RL) approaches train agents that specialize in the target task but often suffer from low sampling efficiency and high exploration costs. In this paper, we introduce a novel framework that addresses these challenges by training a smaller, specialized student RL agent using instructions from an LLM-based teacher agent. By incorporating the guidance from the teacher agent, the student agent can distill the prior knowledge of the LLM into its own model. Consequently, the student agent can be trained with significantly less data. Moreover, through further training with environment feedback, the student agent surpasses the capabilities of its teacher for completing the target task. We conducted experiments on challenging MiniGrid and Habitat environments, specifically designed for embodied AI research, to evaluate the effectiveness of our framework. The results clearly demonstrate that our approach achieves superior performance compared to strong baseline methods. Our code is available at https://github.com/ZJLAB-AMMI/LLM4Teach.

------

Title: Policy Improvement using Language Feedback Models

URL: https://doi.org/10.48550/arXiv.2402.07876

Abstract: We introduce Language Feedback Models (LFMs) that identify desirable behaviour - actions that help achieve tasks specified in the instruction - for imitation learning in instruction following. To train LFMs, we obtain feedback from Large Language Models (LLMs) on visual trajectories verbalized to language descriptions. First, by using LFMs to identify desirable behaviour to imitate, we improve in task-completion rate over strong behavioural cloning baselines on three distinct language grounding environments (Touchdown, ScienceWorld, and ALFWorld). Second, LFMs outperform using LLMs as experts to directly predict actions, when controlling for the number of LLM output tokens. Third, LFMs generalize to unseen environments, improving task-completion rate by 3.5-12.0% through one round of adaptation. Finally, LFM can be modified to provide human-interpretable feedback without performance loss, allowing human verification of desirable behaviour for imitation learning.

------

Title: Policy Learning with a Language Bottleneck

URL: https://doi.org/10.48550/arXiv.2405.04118

Abstract: Modern AI systems such as self-driving cars and game-playing agents achieve superhuman performance, but often lack human-like generalization, interpretability, and inter-operability with human users. Inspired by the rich interactions between language and decision-making in humans, we introduce Policy Learning with a Language Bottleneck (PLLB), a framework enabling AI agents to generate linguistic rules that capture the high-level strategies underlying rewarding behaviors. PLLB alternates between a *rule generation* step guided by language models, and an *update* step where agents learn new policies guided by rules, even when a rule is insufficient to describe an entire complex policy. Across five diverse tasks, including a two-player signaling game, maze navigation, image reconstruction, and robot grasp planning, we show that PLLB agents are not only able to learn more interpretable and generalizable behaviors, but can also share the learned rules with human users, enabling more effective human-AI coordination. We provide source code for our experiments at https://github.com/meghabyte/bottleneck .

------

Title: AgentTuning: Enabling Generalized Agent Abilities for LLMs

URL: https://doi.org/10.48550/arXiv.2310.12823

Abstract: Open large language models (LLMs) with great performance in various tasks have significantly advanced the development of LLMs. However, they are far inferior to commercial models such as ChatGPT and GPT-4 when acting as agents to tackle complex tasks in the real world. These agent tasks employ LLMs as the central controller responsible for planning, memorization, and tool utilization, necessitating both fine-grained prompting methods and robust LLMs to achieve satisfactory performance. Though many prompting methods have been proposed to complete particular agent tasks, there is lack of research focusing on improving the agent capabilities of LLMs themselves without compromising their general abilities. In this work, we present AgentTuning, a simple and general method to enhance the agent abilities of LLMs while maintaining their general LLM capabilities. We construct AgentInstruct, a lightweight instruction-tuning dataset containing high-quality interaction trajectories. We employ a hybrid instruction-tuning strategy by combining AgentInstruct with open-source instructions from general domains. AgentTuning is used to instruction-tune the Llama 2 series, resulting in AgentLM. Our evaluations show that AgentTuning enables LLMs' agent capabilities without compromising general abilities. The AgentLM-70B is comparable to GPT-3.5-turbo on unseen agent tasks, demonstrating generalized agent capabilities. We open source the AgentInstruct and AgentLM-7B, 13B, and 70B models at https://github.com/THUDM/AgentTuning, serving open and powerful alternatives to commercial LLMs for agent tasks.

------

Title: GuardAgent: Safeguard LLM Agents by a Guard Agent via Knowledge-Enabled Reasoning

URL: https://doi.org/10.48550/arXiv.2406.09187

Abstract: The rapid advancement of large language models (LLMs) has catalyzed the deployment of LLM-powered agents across numerous applications, raising new concerns regarding their safety and trustworthiness. In addition, existing methods for enhancing the safety of LLMs are not directly transferable to LLM-powered agents due to their diverse objectives and output modalities. In this paper, we propose GuardAgent , the first LLM agent as a guardrail to other LLM agents. Specifically, GuardAgent oversees a target LLM agent by checking whether its inputs/outputs satisfy a set of given guard requests (e.g., safety rules or privacy policies) defined by the users. GuardAgent comprises two steps: 1) creating a task plan by analyzing the provided guard requests, and 2) generating guardrail code based on the task plan and executing the code by calling APIs or using external engines. In both steps, an LLM is utilized as the core reasoning component, supplemented by in-context demonstrations retrieved from a memory module. Such knowledge-enabled reasoning allows GuardAgent to understand various textual guard requests and accurately “translate” them into executable code that provides reliable guardrails. Furthermore, GuardAgent is equipped with an extendable toolbox containing functions and APIs and requires no additional LLM training, which underscores its generalization capabilities and low operational overhead. In addition to GuardAgent , we propose two novel benchmarks: an EICU-AC benchmark for assessing privacy-related access control for healthcare agents and a Mind2Web-SC benchmark for safety evaluation for web agents. We show the effectiveness of GuardAgent on these two benchmarks with 98.7% and 90.0% guarding accuracy in moderating invalid inputs and outputs for the

------

Title: MobileGPT: Augmenting LLM with Human-like App Memory for Mobile Task Automation

URL: https://doi.org/10.1145/3636534.3690682

Abstract: The advent of large language models (LLMs) has opened up new opportunities in the field of mobile task automation. Their superior language understanding and reasoning capabilities allow users to automate complex and repetitive tasks. However, due to the inherent unreliability and high operational cost of LLMs, their practical applicability is quite limited. To address these issues, this paper introduces MobileGPT1, an innovative LLM-based mobile task automator equipped with a human-like app memory. MobileGPT emulates the cognitive process of humans interacting with a mobile app---explore, select, derive, and recall. This approach allows for a more precise and efficient learning of a task's procedure by breaking it down into smaller, modular sub-tasks that can be re-used, re-arranged, and adapted for various objectives. We implement MobileGPT using online LLMs services (GPT-3.5 and GPT-4) and evaluate its performance on a dataset of 185 tasks across 18 mobile apps. The results indicate that MobileGPT can automate and learn new tasks with 82.7% accuracy, and is able to adapt them to different contexts with near perfect (98.75%) accuracy while reducing both latency and cost by 62.5% and 68.8%, respectively, compared to the GPT-4 powered baseline.

------

Title: Distilling Script Knowledge from Large Language Models for Constrained Language Planning

URL: https://doi.org/10.48550/arXiv.2305.05252

Abstract: In everyday life, humans often plan their actions by following step-by-step instructions in the form of goal-oriented scripts. Previous work has exploited language models (LMs) to plan for abstract goals of stereotypical activities (e.g., “make a cake”), but leaves more specific goals with multi-facet constraints understudied (e.g., “make a cake for diabetics”). In this paper, we define the task of constrained language planning for the first time. We propose an over-generate-then-filter approach to improve large language models (LLMs) on this task, and use it to distill a novel constrained language planning dataset, Coscript, which consists of 55,000 scripts. Empirical results demonstrate that our method significantly improves the constrained language planning ability of LLMs, especially on constraint faithfulness. Furthermore, Coscript is demonstrated to be quite effective in endowing smaller LMs with constrained language planning ability.

------