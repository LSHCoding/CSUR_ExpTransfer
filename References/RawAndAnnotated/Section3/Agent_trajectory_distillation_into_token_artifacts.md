# Agent trajectory distillation into token artifacts

##### [**Undermind**](https://undermind.ai)

---

**Research Goal:** Find academic papers on LLM-based, VLM-based, GUI, embodied, tool-use, code, web, and multi-agent systems that perform sequential decision-making in an environment and transform raw interaction trajectories into reusable token-level artifacts that are later consumed in-context for future decisions. The artifact should remain at the token level rather than being absorbed into model weights or latent/continuous representations. Relevant papers may center entirely on this trajectory-to-artifact distillation step or include it as one named module inside a larger agent system, and should surface that module. Include cases where the artifact is built from agent trajectories, human demonstrations, teacher-model traces, or trajectories combined with other inputs, as long as trajectory experience is a core ingredient. Also include systems with explicit retrieval as well as persistent notebooks, manuals, or skill banks that are appended or consulted without an explicit retrieval stage. Target two broad artifact families: (1) natural-language or narrative artifacts such as self-reflections, self-critiques, post-hoc lessons, episodic summaries, extracted rules, heuristics, principles, guidelines, hints, tips, do-and-don’t lists, insight banks, abstracted skill descriptions, error postmortems, growing notebooks of agent experience, and multimodal textual summaries of GUI or embodied trajectories; and (2) structured or schematic artifacts extracted from trajectories, such as reusable code or skill libraries, programmatic action abstractions, workflow graphs or DAGs, standard operating procedures, API or tool specifications mined from logs, action schemas, decision trees, agent knowledge graphs, scene or sentence graphs of agent behavior, typed cheatsheets, parsed templates, executable recipes, and agent-workflow memories. Prioritize papers from 2022–2026, including major ML/NLP/robotics/HCI venues and substantive arXiv preprints, while allowing earlier seminal papers if they established this mechanism. Especially prioritize papers that compare raw trajectory retrieval against distilled or abstracted artifacts, compare unstructured natural-language artifacts against structured or programmatic artifacts on similar tasks, address multimodal settings such as GUI agents, embodied agents, robotics, web agents, or code agents, or study lifelong, continual, or self-evolving agents whose growing external store is a curated library of reusable artifacts rather than a replay buffer for fine-tuning. Also prioritize methods that consolidate, deduplicate, generalize, or version-control the artifact store over time. Exclude papers whose main mechanism is fine-tuning or reinforcement learning from trajectories into model weights, compression into KV cache reuse, prefix or soft prompts, learned memory tokens, or other continuous-vector memories, reward-model or verifier training, generic retrieval-augmented generation over static external corpora not derived from agent decision-making trajectories, pure prompt-engineering or prompt-optimization without an experience-distillation step, single-step classification tasks, static-corpus pretraining, image-only foundation models, and classical non-LLM reinforcement learning.

*Found 110 papers · May 7, 2026 · Estimated coverage of relevant papers: 45%*

## Summary of Results

The field has shifted from replaying whole trajectories toward compiling them into compact external procedures, reflections, and workflow artifacts that are reused in-context, with structured procedural forms often outperforming raw transcripts or demonstrations on long-horizon agent tasks \[1\], \[2\], \[3\], \[4\], \[5\], \[6\].

#### Artifact families

- **Natural-language distillation**: verbal reflections and lessons in episodic buffers \[1\], extracted insights across tasks \[2\], causal abstractions in persistent textual memory \[7\], context-aware guidelines \[8\], and self-generated manuals/rules \[9\].
- **Structured/procedural distillation**: reusable workflows \[3\], stepwise and script-level procedural memory \[10\], hierarchical procedures with success/failure contrast \[11\], executable web/program skills or APIs \[4\], \[12\], skill libraries in embodied settings \[13\], and graph/state-machine memories for GUI/web environments \[6\], \[14\], \[15\].

#### Recurrent design pattern

- Collect trajectories from agent rollouts, demonstrations, or teacher traces.
- Distill into a smaller artifact with explicit applicability conditions, parameters, or subgoals.
- Retrieve or directly append those artifacts at inference.
- Continually **merge, prune, refine, or deprecate** the store rather than append forever \[10\], \[11\], \[16\], \[17\].

#### High-value comparisons

- Programmatic skills beat text-skill variants in web agents \[4\].
- Environment maps outperform access to the raw trajectories used to build them \[6\].
- Multimodal abstraction of imperfect demonstrations yields better reusable examples than raw demos in TEACh and VisualWebArena \[5\].
- Distilled procedural memory transfers across model scales, helping weaker agents inherit stronger agents’ experience \[10\], \[12\].

## Paper Catalog (110 papers)

|  | Year | Cit/yr | Title | Authors | Journal |
|---:|:--:|:--:|:---|:---|:---|
| 1 | 2024 | 77 | Agent Workflow Memory ([link](https://doi.org/10.48550/arXiv.2409.07429)) | Z. Wang, Jiayuan Mao, Daniel Fried, and Graham Neubig | ArXiv |
| 2 | 2025 | 28 | Memp: Exploring Agent Procedural Memory ([link](https://doi.org/10.48550/arXiv.2508.06433)) | Runnan Fang et al. | ArXiv |
| 3 | 2025 | 38 | Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution ([link](https://doi.org/10.48550/arXiv.2512.10696)) | Zouying Cao et al. | ArXiv |
| 4 | 2026 | 4.0 | Traversal-as-Policy: Log-Distilled Gated Behavior Trees as Externalized, Verifiable Policies for Safe, Robust, and Efficient Agents ([link](https://www.semanticscholar.org/paper/a4428f2803db336bca7f80a9e24e88110122d8cd)) | Peiran Li et al. |  |
| 5 | 2023 | 1017 | Reflexion: language agents with verbal reinforcement learning ([link](https://doi.org/10.52202/075280-0377)) | Noah Shinn et al. | Advances in Neural Information Processing Systems 36 |
| 6 | 2024 | 18 | AutoGuide: Automated Generation and Selection of Context-Aware Guidelines for Large Language Model Agents ([link](https://doi.org/10.48550/arXiv.2403.08978)) | Yao Fu et al. | ArXiv |
| 7 | 2023 | 27 | CLIN: A Continually Learning Language Agent for Rapid Task Adaptation and Generalization ([link](https://doi.org/10.48550/arXiv.2310.10134)) | Bodhisattwa Prasad Majumder et al. | ArXiv |
| 8 | 2024 | 22 | VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought ([link](https://doi.org/10.52202/079017-2418)) | Gabriel Sarch et al. | Advances in Neural Information Processing Systems 37 |
| 9 | 2023 | 511 | Voyager: An Open-Ended Embodied Agent with Large Language Models ([link](https://doi.org/10.48550/arXiv.2305.16291)) | Guanzhi Wang et al. | ArXiv |
| 10 | 2026 | 10 | Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills ([link](https://www.semanticscholar.org/paper/8b02872a17028c037e214fef695304494c809411)) | Jingwei Ni et al. |  |
| 11 | 2026 |  | Evolving Programmatic Skill Networks ([link](https://doi.org/10.48550/arXiv.2601.03509)) | Haochen Shi, Xingdi Yuan, and Bang Liu | ArXiv |
| 12 | 2026 | 6.0 | Skill-Pro: Learning Reusable Skills from Experience via Non-Parametric PPO for LLM Agents ([link](https://www.semanticscholar.org/paper/28f0b6f57e57337c7db267ae4ac52c12cbb5d376)) | Qirui Mi et al. |  |
| 13 | 2025 | 48 | SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills ([link](https://doi.org/10.48550/arXiv.2504.07079)) | Boyuan Zheng et al. | ArXiv |
| 14 | 2025 | 38 | Inducing Programmatic Skills for Agentic Tasks ([link](https://doi.org/10.48550/arXiv.2504.06821)) | Z. Wang, Apurva Gandhi, Graham Neubig, and Daniel Fried | ArXiv |
| 15 | 2026 | 4.0 | AutoRefine: From Trajectories to Reusable Expertise for Continual LLM Agent Refinement ([link](https://doi.org/10.48550/arXiv.2601.22758)) | Libin Qiu et al. | ArXiv |
| 16 | 2025 | 10 | Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement ([link](https://doi.org/10.48550/arXiv.2512.18950)) | Saman Forouzandeh, Wei Peng, Parham Moradi, Xinghuo Yu, and Mahdi Jalili | ArXiv |
| 17 | 2026 |  | WebXSkill: Skill Learning for Autonomous Web Agents ([link](https://www.semanticscholar.org/paper/f283b199100a8d976d1f3b6a8561f7597c6a068e)) | Zhaoyang Wang et al. |  |
| 18 | 2025 | 50 | Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory ([link](https://doi.org/10.48550/arXiv.2504.07952)) | Mirac Suzgun, Mert Yüksekgönül, Federico Bianchi, Daniel Jurafsky, and James Zou | ArXiv |
| 19 | 2025 | 52 | Agent KB: Leveraging Cross-Domain Experience for Agentic Problem Solving ([link](https://doi.org/10.48550/arXiv.2507.06229)) | Xiangru Tang et al. | ArXiv |
| 20 | 2024 | 8.0 | Skill Set Optimization: Reinforcing Language Model Behavior via Transferable Skills ([link](https://doi.org/10.48550/arXiv.2402.03244)) | Kolby Nottingham et al. | International Conference on Machine Learning |
| 21 | 2024 | 14 | AutoManual: Constructing Instruction Manuals by LLM Agents via Interactive Environmental Learning ([link](https://doi.org/10.52202/079017-0019)) | Minghao Chen et al. | Advances in Neural Information Processing Systems 37 |
| 22 | 2025 | 24 | Contextual Experience Replay for Self-Improvement of Language Agents ([link](https://doi.org/10.48550/arXiv.2506.06698)) | Yitao Liu, Chenglei Si, Karthik R. Narasimhan, and Shunyu Yao | Annual Meeting of the Association for Computational Linguistics |
| 23 | 2025 | 3.0 | Meta-Policy Reflexion: Reusable Reflective Memory and Rule Admissibility for Resource-Efficient LLM Agent ([link](https://doi.org/10.48550/arXiv.2509.03990)) | Chunlong Wu, Ye Luo, Zhibo Qu, and Min Wang | ArXiv |
| 24 | 2025 | 201 | Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models ([link](https://doi.org/10.48550/arXiv.2510.04618)) | Qizheng Zhang et al. | ArXiv |
| 25 | 2026 |  | Compiled Memory: Not More Information, but More Precise Instructions for Language Agents ([link](https://www.semanticscholar.org/paper/62dc0a497a2643f06303a81ee1cb9d7e1167ae7a)) | James G Rhodes and G. Kang |  |
| 26 | 2023 | 174 | ExpeL: LLM Agents Are Experiential Learners ([link](https://doi.org/10.48550/arXiv.2308.10144)) | Andrew Zhao et al. | AAAI Conference on Artificial Intelligence |
| 27 | 2026 | 2.0 | ActionEngine: From Reactive to Programmatic GUI Agents via State Machine Memory ([link](https://doi.org/10.48550/arXiv.2602.20502)) | Hongbin Zhong et al. | ArXiv |
| 28 | 2025 | 350 | A-MEM: Agentic Memory for LLM Agents ([link](https://doi.org/10.48550/arXiv.2502.12110)) | Wujiang Xu et al. | ArXiv |
| 29 | 2026 | 4.0 | Enhancing Web Agents with a Hierarchical Memory Tree ([link](https://www.semanticscholar.org/paper/bddff0e7853344b7f8e2bccc7e9145630b6e8b3e)) | Yunteng Tan, Zhiqiang Gao, and Xinxiao Wu |  |
| 30 | 2026 |  | Environment Maps: Structured Environmental Representations for Long-Horizon Agents ([link](https://www.semanticscholar.org/paper/8ff9c033934b39ec676e42bc84baa654e2453cc6)) | Yenchia Feng, Chirag Sharma, and Karime Maamari |  |
| 31 | 2025 |  | Beyond Training: Enabling Self-Evolution of Agents with MOBIMEM ([link](https://doi.org/10.48550/arXiv.2512.15784)) | Zibin Liu et al. | ArXiv |
| 32 | 2025 | 44 | G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems ([link](https://doi.org/10.48550/arXiv.2506.07398)) | Gui-Min Zhang et al. | ArXiv |
| 33 | 2026 | 18 | AutoSkill: Experience-Driven Lifelong Learning via Skill Self-Evolution ([link](https://doi.org/10.48550/arXiv.2603.01145)) | Yutao Yang et al. | ArXiv |
| 34 | 2025 | 49 | What Deserves Memory: Adaptive Memory Distillation for LLM Agents ([link](https://www.semanticscholar.org/paper/c7104ee40e801e802cdd6e85c26f1ca8dcc00b19)) | Wenquan Ma, Jiayan Nan, Wenlong Wu, and Yize Chen |  |
| 35 | 2026 | 2.0 | Darwinian Memory: A Training-Free Self-Regulating Memory System for GUI Agent Evolution ([link](https://doi.org/10.48550/arXiv.2601.22528)) | Hongze Mi et al. | ArXiv |
| 36 | 2026 |  | APEX-EM: Non-Parametric Online Learning for Autonomous Agents via Structured Procedural-Episodic Experience Replay ([link](https://www.semanticscholar.org/paper/16c110756c0f0395fe9cc9568434d9e5621cd464)) | Pratyay Banerjee, Masud Moshtaghi, and Ankit Chadha |  |
| 37 | 2025 | 3.3 | Recon-Act: A Self-Evolving Multi-Agent Browser-Use System via Web Reconnaissance, Tool Generation, and Task Execution ([link](https://doi.org/10.48550/arXiv.2509.21072)) | Kaiwen He, Zhiwei Wang, Chenyi Zhuang, and Jinjie Gu | ArXiv |
| 38 | 2025 | 5.3 | Sample-Efficient Online Learning in LM Agents via Hindsight Trajectory Rewriting ([link](https://doi.org/10.48550/arXiv.2510.10304)) | Michael Hu, Benjamin Van Durme, Jacob Andreas, and Harsh Jhamtani | ArXiv |
| 39 | 2026 |  | BrainMem: Brain-Inspired Evolving Memory for Embodied Agent Task Planning ([link](https://www.semanticscholar.org/paper/9e5eb6557069adc35643a2efacd4f5d1670dc348)) | Xiaoyu Ma et al. |  |
| 40 | 2026 |  | M2: Dual-Memory Augmentation for Long-Horizon Web Agents via Trajectory Summarization and Insight Retrieval ([link](https://doi.org/10.48550/arXiv.2603.00503)) | Dawei Yan et al. | ArXiv |
| 41 | 2023 | 76 | REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction ([link](https://doi.org/10.48550/arXiv.2306.15724)) | Zeyi Liu, Arpit Bahety, and Shuran Song | ArXiv |
| 42 | 2026 | 2.0 | SkillX: Automatically Constructing Skill Knowledge Bases for Agents ([link](https://www.semanticscholar.org/paper/24566e0b5989b1b32951ff9a10b6d6b0162683f5)) | Chenxi Wang et al. |  |
| 43 | 2025 | 26 | GUI-explorer: Autonomous Exploration and Mining of Transition-aware Knowledge for GUI Agent ([link](https://doi.org/10.48550/arXiv.2505.16827)) | Bin Xie et al. | Annual Meeting of the Association for Computational Linguistics |
| 44 | 2026 |  | Aligning Progress and Feasibility: A Neuro-Symbolic Dual Memory Framework for Long-Horizon LLM Agents ([link](https://www.semanticscholar.org/paper/d79865a4e99248187eb1fcf28fb2407c261be74d)) | Bin Wen, Ruoxuan Zhang, Yangtao Chen, Hongxia Xie, and Lan-Zhe Guo |  |
| 45 | 2025 | 44 | SWE-Exp: Experience-Driven Software Issue Resolution ([link](https://doi.org/10.48550/arXiv.2507.23361)) | Silin Chen et al. | ArXiv |
| 46 | 2026 |  | SkillClaw: Let Skills Evolve Collectively with Agentic Evolver ([link](https://www.semanticscholar.org/paper/3d795acefb5939ec88767d9a01dffb765fb90111)) | Ziyu Ma et al. |  |
| 47 | 2025 | 11 | PolySkill: Learning Generalizable Skills Through Polymorphic Abstraction ([link](https://doi.org/10.48550/arXiv.2510.15863)) | Simon Yu, Gang Li, Weiyan Shi, and Pengyuan Qi | ArXiv |
| 48 | 2025 | 4.2 | Coarse-to-Fine Grounded Memory for LLM Agent Planning ([link](https://doi.org/10.48550/arXiv.2508.15305)) | Wei Yang et al. | Conference on Empirical Methods in Natural Language Processing |
| 49 | 2026 | 2.0 | AndroTMem: From Interaction Trajectories to Anchored Memory in Long-Horizon GUI Agents ([link](https://www.semanticscholar.org/paper/1b4c03b4374e581df75c8128de879afb2792623c)) | Yi Shi et al. |  |
| 50 | 2025 | 6.5 | MemOrb: A Plug-and-Play Verbal-Reinforcement Memory Layer for E-Commerce Customer Service ([link](https://doi.org/10.48550/arXiv.2509.18713)) | Yizhe Huang et al. | ArXiv |
| 51 | 2025 | 17 | Learning on the Job: An Experience-Driven Self-Evolving Agent for Long-Horizon Tasks ([link](https://doi.org/10.48550/arXiv.2510.08002)) | Cheng Yang et al. | ArXiv |
| 52 | 2025 | 7.2 | PG-Agent: An Agent Powered by Page Graph ([link](https://doi.org/10.1145/3746027.3755189)) | Weizhi Chen et al. | Proceedings of the 33rd ACM International Conference on Multimedia |
| 53 | 2026 |  | Procedural Knowledge at Scale Improves Reasoning ([link](https://www.semanticscholar.org/paper/04c481562585e6c719a7e9f0fad3ccd5170c7dce)) | Di Wu, Devendra Singh Sachan, Wen-tau Yih, and Mingda Chen |  |
| 54 | 2026 | 34 | MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents ([link](https://doi.org/10.48550/arXiv.2602.02474)) | Haozhen Zhang et al. | ArXiv |
| 55 | 2025 | 2.0 | Mistake Notebook Learning: Batch-Clustered Failures for Training-Free Agent Adaptation ([link](https://www.semanticscholar.org/paper/c710f507d19ace6322bf710b4a13f2929c848540)) | Xuanbo Su, Yingfang Zhang, Hao Luo, Xiaoteng Liu, and Leo Huang |  |
| 56 | 2023 | 24 | MobileGPT: Augmenting LLM with Human-like App Memory for Mobile Task Automation ([link](https://doi.org/10.1145/3636534.3690682)) | Sunjae Lee et al. | Proceedings of the 30th Annual International Conference on Mobile Computing and Networking |
| 57 | 2025 | 6.5 | MapAgent: Trajectory-Constructed Memory-Augmented Planning for Mobile Task Automation ([link](https://doi.org/10.48550/arXiv.2507.21953)) | Yibo Kong et al. | ArXiv |
| 58 | 2025 | 10 | WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance ([link](https://doi.org/10.48550/arXiv.2511.12997)) | Genglin Liu et al. | ArXiv |
| 59 | 2025 | 12 | Get Experience from Practice: LLM Agents with Record & Replay ([link](https://doi.org/10.48550/arXiv.2505.17716)) | Erhu Feng et al. | ArXiv |
| 60 | 2025 |  | ViReSkill: Vision-Grounded Replanning with Skill Memory for LLM-Based Planning in Lifelong Robot Learning ([link](https://doi.org/10.48550/arXiv.2509.24219)) | Tomoyuki Kagaya et al. | ArXiv |
| 61 | 2025 | 4.7 | R2D2: Remembering, Replaying and Dynamic Decision Making with a Reflective Agentic Memory ([link](https://doi.org/10.18653/v1/2025.acl-long.1464)) | Tenghao Huang et al. | Annual Meeting of the Association for Computational Linguistics |
| 62 | 2026 |  | EE-MCP: Self-Evolving MCP-GUI Agents via Automated Environment Generation and Experience Learning ([link](https://www.semanticscholar.org/paper/e06e5eeb506c3926d45063bcb6d6395300a5b14d)) | Tian He et al. |  |
| 63 | 2025 | 1.1 | UI-Evol: Automatic Knowledge Evolving for Computer Use Agents ([link](https://doi.org/10.48550/arXiv.2505.21964)) | Ziyun Zhang et al. | ArXiv |
| 64 | 2023 | 16 | Open-Ended Instructable Embodied Agents with Memory-Augmented Large Language Models ([link](https://doi.org/10.48550/arXiv.2310.15127)) | Gabriel Sarch, Yue Wu, Michael J. Tarr, and Katerina Fragkiadaki | ArXiv |
| 65 | 2024 | 32 | AriGraph: Learning Knowledge Graph World Models with Episodic Memory for LLM Agents ([link](https://doi.org/10.48550/arXiv.2407.04363)) | Petr Anokhin et al. | International Joint Conference on Artificial Intelligence |
| 66 | 2026 |  | WorkflowGen:an adaptive workflow generation mechanism driven by trajectory experience ([link](https://www.semanticscholar.org/paper/5bf8397a0dc2ebb22480f51abf63a0140274b9b8)) | Ruocan Wei, Shufeng Wang, and Ziwei Shi |  |
| 67 | 2026 |  | From Procedural Skills to Strategy Genes: Towards Experience-Driven Test-Time Evolution ([link](https://www.semanticscholar.org/paper/79b442e4943aff69119dd4bbabf08191e921d8c7)) | Junjie Wang, Yiming Ren, and Haoyang Zhang |  |
| 68 | 2024 | 1.7 | ICAL: Continual Learning of Multimodal Agents by Transforming Trajectories into Actionable Insights ([link](https://doi.org/10.48550/arXiv.2406.14596)) | Gabriel Sarch et al. | ArXiv |
| 69 | 2023 | 18 | Demo2Code: From Summarizing Demonstrations to Synthesizing Code via Extended Chain-of-Thought ([link](https://doi.org/10.48550/arXiv.2305.16744)) | Huaxiaoyue Wang, Gonzalo Gonzalez-Pumariega, Yash Sharma, and Sanjiban Choudhury | ArXiv |
| 70 | 2025 | 6.3 | H2R: Hierarchical Hindsight Reflection for Multi-Task LLM Agents ([link](https://doi.org/10.1109/ICA67499.2025.00030)) | Shicheng Ye, Chao Yu, Kaiqiang Ke, Chengdong Xu, and Yinqi Wei | 2025 IEEE International Conference on Agentic AI (ICA) |
| 71 | 2025 | 2.2 | Reflection-Based Memory For Web navigation Agents ([link](https://doi.org/10.48550/arXiv.2506.02158)) | Ruhana Azam, Aditya Vempaty, and Ashish Jagmohan | ArXiv |
| 72 | 2023 | 1249 | Generative Agents: Interactive Simulacra of Human Behavior ([link](https://doi.org/10.1145/3586183.3606763)) | J. Park et al. | Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology |
| 73 | 2026 |  | A²Flow: Automating Agentic Workflow Generation via Self-Adaptive Abstraction Operators ([link](https://doi.org/10.1609/aaai.v40i35.40240)) | Mingming Zhao et al. | AAAI Conference on Artificial Intelligence |
| 74 | 2025 | 50 | MemEvolve: Meta-Evolution of Agent Memory Systems ([link](https://doi.org/10.48550/arXiv.2512.18746)) | Guibin Zhang et al. | ArXiv |
| 75 | 2025 | 12 | Agentic Plan Caching: Test-Time Memory for Fast and Cost-Efficient LLM Agents ([link](https://www.semanticscholar.org/paper/cd09ab0315169ce0037dd1cf601f3f24729453f2)) | Qizheng Zhang, Michael Wornow, and K. Olukotun |  |
| 76 | 2025 | 2.0 | A2Flow: Automating Agentic Workflow Generation via Self-Adaptive Abstraction Operators ([link](https://doi.org/10.48550/arXiv.2511.20693)) | Mingming Zhao et al. | ArXiv |
| 77 | 2025 | 9.8 | Self-Generated In-Context Examples Improve LLM Agents for Sequential Decision-Making Tasks ([link](https://doi.org/10.48550/arXiv.2505.00234)) | Vishnu Sarukkai, Zhiqiang Xie, and Kayvon Fatahalian | ArXiv |
| 78 | 2025 | 59 | Learn-by-interact: A Data-Centric Framework for Self-Adaptive Agents in Realistic Environments ([link](https://doi.org/10.48550/arXiv.2501.10893)) | Hongjin Su et al. | ArXiv |
| 79 | 2025 | 4.0 | Learning from Online Videos at Inference Time for Computer-Use Agents ([link](https://doi.org/10.48550/arXiv.2511.04137)) | Yujian Liu et al. | ArXiv |
| 80 | 2024 | 35 | Keypoint Action Tokens Enable In-Context Imitation Learning in Robotics ([link](https://doi.org/10.48550/arXiv.2403.19578)) | Norman Di Palo and Edward Johns | ArXiv |
| 81 | 2025 | 8.0 | EchoTrail-GUI: Building Actionable Memory for GUI Agents via Critic-Guided Self-Exploration ([link](https://doi.org/10.48550/arXiv.2512.19396)) | Runze Li et al. | ArXiv |
| 82 | 2025 | 8.9 | Mirage-1: Augmenting and Updating GUI Agent with Hierarchical Multimodal Skills ([link](https://doi.org/10.48550/arXiv.2506.10387)) | Yuquan Xie et al. | ArXiv |
| 83 | 2025 | 14 | Meta-Agent-Workflow: Streamlining Tool Usage in LLMs through Workflow Construction, Retrieval, and Refinement ([link](https://doi.org/10.1145/3701716.3715247)) | X. Tan et al. | Companion Proceedings of the ACM on Web Conference 2025 |
| 84 | 2026 | 2.0 | Memex(RL): Scaling Long-Horizon LLM Agents via Indexed Experience Memory ([link](https://www.semanticscholar.org/paper/d1ed5cf8419f2e0d78a3511ae37596427e4efcbc)) | Zhenting Wang, Huancheng Chen, Jiayun Wang, and Wei Wei |  |
| 85 | 2026 |  | FlowMind: Execute-Summarize for Structured Workflow Generation from LLM Reasoning ([link](https://doi.org/10.48550/arXiv.2602.11782)) | Yihao Liu, Ziyun Zhang, Zile He, and Hua Cai | ArXiv |
| 86 | 2023 | 44 | Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control ([link](https://www.semanticscholar.org/paper/eaa7853facb9b49444b48a96192cb4be66b62671)) | Longtao Zheng, R. Wang, and Bo An | International Conference on Learning Representations |
| 87 | 2024 | 15 | BAGEL: Bootstrapping Agents by Guiding Exploration with Language ([link](https://doi.org/10.48550/arXiv.2403.08140)) | Shikhar Murty, Christopher D. Manning, Peter Shaw, Mandar Joshi, and Kenton Lee | ArXiv |
| 88 | 2024 | 1.3 | Skill Learning Using Process Mining for Large Language Model Plan Generation ([link](https://doi.org/10.48550/arXiv.2410.12870)) | Andrei Cosmin Redis, M. Sani, Bahram Zarrin, and Andrea Burattin | ArXiv |
| 89 | 2025 |  | MaP-AVR: A Meta-Action Planner for Agents Leveraging Vision Language Models and Retrieval-Augmented Generation ([link](https://doi.org/10.48550/arXiv.2512.19453)) | Zhenglong Guo et al. | ArXiv |
| 90 | 2023 | 15 | Large Language Models Are Semi-Parametric Reinforcement Learning Agents ([link](https://doi.org/10.52202/075280-3419)) | Danyang Zhang et al. | Advances in Neural Information Processing Systems 36 |
| 91 | 2024 | 11 | TRAD: Enhancing LLM Agents with Step-Wise Thought Retrieval and Aligned Decision ([link](https://doi.org/10.1145/3626772.3657788)) | Ruiwen Zhou et al. | Proceedings of the 47th International ACM SIGIR Conference on Research and Development in Information Retrieval |
| 92 | 2026 |  | SkillFlow:Benchmarking Lifelong Skill Discovery and Evolution for Autonomous Agents ([link](https://www.semanticscholar.org/paper/6158fe73b7cb734c2561ae4b28f37f6ccdf54929)) | Ziao Zhang et al. |  |
| 93 | 2023 | 221 | MemGPT: Towards LLMs as Operating Systems ([link](https://doi.org/10.48550/arXiv.2310.08560)) | Charles Packer et al. | ArXiv |
| 94 | 2026 |  | SkillLearnBench: Benchmarking Continual Learning Methods for Agent Skill Generation on Real-World Tasks ([link](https://www.semanticscholar.org/paper/f73d5cb01fb23264ba211fb6305586ed7b31d61c)) | Shan Zhong et al. |  |
| 95 | 2026 | 2.0 | ShowUI-Aloha: Human-Taught GUI Agent ([link](https://doi.org/10.48550/arXiv.2601.07181)) | Yichun Zhang et al. | ArXiv |
| 96 | 2024 | 23 | R+X: Retrieval and Execution from Everyday Human Videos ([link](https://doi.org/10.1109/ICRA55743.2025.11128322)) | Georgios Papagiannis, Norman Di Palo, Pietro Vitiello, and Edward Johns | 2025 IEEE International Conference on Robotics and Automation (ICRA) |
| 97 | 2026 | 20 | SkillNet: Create, Evaluate, and Connect AI Skills ([link](https://www.semanticscholar.org/paper/eb636dedbce820f3cea34264dba85295099cd253)) | Yuanying Liang et al. |  |
| 98 | 2026 |  | GraSP: Graph-Structured Skill Compositions for LLM Agents ([link](https://www.semanticscholar.org/paper/928d9ff76efd60f7f028673d31a50feb51de04d7)) | Tianle Xia et al. |  |
| 99 | 2024 | 20 | TroVE: Inducing Verifiable and Efficient Toolboxes for Solving Programmatic Tasks ([link](https://doi.org/10.48550/arXiv.2401.12869)) | Zhiruo Wang, Daniel Fried, and Graham Neubig | International Conference on Machine Learning |
| 100 | 2025 | 2.0 | A Benchmark for Procedural Memory Retrieval in Language Agents ([link](https://doi.org/10.48550/arXiv.2511.21730)) | Ishant Kohar and Aswanth Krishnan | ArXiv |
| 101 | 2025 | 62 | Memento: Fine-tuning LLM Agents without Fine-tuning LLMs ([link](https://doi.org/10.48550/arXiv.2508.16153)) | Huichi Zhou et al. | ArXiv |
| 102 | 2024 |  | In-Context Ensemble Learning from Pseudo Labels Improves Video-Language Models for Low-Level Workflow Understanding ([link](https://www.semanticscholar.org/paper/78b1eefb8ba798a6b3c69a2d837741cdafcd83d7)) | Moucheng Xu et al. |  |
| 103 | 2023 | 1.2 | Code Models are Zero-shot Precondition Reasoners ([link](https://doi.org/10.48550/arXiv.2311.09601)) | Lajanugen Logeswaran et al. | North American Chapter of the Association for Computational Linguistics |
| 104 | 2024 | 30 | HiAgent: Hierarchical Working Memory Management for Solving Long-Horizon Agent Tasks with Large Language Model ([link](https://doi.org/10.48550/arXiv.2408.09559)) | Mengkang Hu et al. | ArXiv |
| 105 | 2024 | 2.4 | Automatic Control With Human-Like Reasoning: Exploring Language Model Embodied Air Traffic Agents ([link](https://doi.org/10.48550/arXiv.2409.09717)) | Justas Andriuskevicius and Junzi Sun | ArXiv |
| 106 | 2026 |  | How Well Do Agentic Skills Work in the Wild: Benchmarking LLM Skill Usage in Realistic Settings ([link](https://www.semanticscholar.org/paper/c1fd40ee282296d888be84bd0edcc1d7b7167647)) | Yujian Liu et al. |  |
| 107 | 2026 |  | From Logs to Agents: Reconstructing High-Level Creative Workflows from Low-Level Raw System Traces ([link](https://www.semanticscholar.org/paper/b016f293ef6641c5e879e5c83f6330f9b151a6b2)) | Tae Hee Jo and Kyung-Hoon Hyun |  |
| 108 | 2026 |  | View-oriented Conversation Compiler for Agent Trace Analysis ([link](https://www.semanticscholar.org/paper/e9e0b1e0aaceb9823d47e4ec43d33d2601b9a96c)) | Lvmin Zhang and Maneesh Agrawala |  |
| 109 | 2020 | 2.8 | Workflow Graphs: A Computational Model of Collective Task Strategies for 3D Design Software ([link](https://doi.org/10.20380/GI2020.13)) | Minsuk Chang, B. Lafreniere, Juho Kim, G. Fitzmaurice, and Tovi Grossman | Graphics Interface |
| 110 | 2024 | 9.7 | ReGAL: Refactoring Programs to Discover Generalizable Abstractions ([link](https://doi.org/10.48550/arXiv.2401.16467)) | Elias Stengel-Eskin, Archiki Prasad, and Mohit Bansal | ArXiv |

### Paper Details

1\. · 100% match · 2024 · 77 cit/yr\
**Agent Workflow Memory** ([link](https://doi.org/10.48550/arXiv.2409.07429))\
Z. Wang, Jiayuan Mao, Daniel Fried, and Graham Neubig\
*ArXiv* · Sep 11, 2024 · 127 citations

> Despite the potential of language model-based agents to solve real-world tasks such as web navigation, current methods still struggle with long-horizon tasks with complex action trajectories. In contrast, humans can flexibly solve complex tasks by learning reusable task workflows from past experiences and using them to guide future actions. To build agents that can similarly benefit from this process, we introduce Agent Workflow Memory (AWM), a method for inducing commonly reused routines, i.e., workflows, and selectively providing workflows to the agent to guide subsequent generations. AWM flexibly applies to both offline and online scenarios, where agents induce workflows from training examples beforehand or from test queries on the fly. We experiment on two major web navigation benchmarks – Mind2Web and WebArena – that collectively cover 1000+ tasks from 200+ domains across travel, shopping, and social media, among others. AWM substantially improves the baseline results by 24.6% and 51.1% relative success rate on Mind2Web and WebArena while reducing the number of steps taken to solve WebArena tasks successfully. Furthermore, online AWM robustly generalizes in cross-task, website, and domain evaluations, surpassing baselines from 8.9 to 14.0 absolute points as train-test task distribution gaps widen.

------------------------------------------------------------------------

2\. · 100% match · 2025 · 28 cit/yr\
**Memp: Exploring Agent Procedural Memory** ([link](https://doi.org/10.48550/arXiv.2508.06433))\
Runnan Fang et al.\
*ArXiv* · Aug 8, 2025 · 21 citations

> Large Language Models (LLMs) based agents excel at diverse tasks, yet they suffer from brittle procedural memory that is manually engineered or entangled in static parameters. In this work, we investigate strategies to endow agents with a learnable, updatable, and lifelong procedural memory. We propose Memp that distills past agent trajectories into both fine-grained, step-by-step instructions and higher-level, script-like abstractions, and explore the impact of different strategies for Build, Retrieval, and Update of procedural memory. Coupled with a dynamic regimen that continuously updates, corrects, and deprecates its contents, this repository evolves in lockstep with new experience. Empirical evaluation on TravelPlanner and ALFWorld shows that as the memory repository is refined, agents achieve steadily higher success rates and greater efficiency on analogous tasks. Moreover, procedural memory built from a stronger model retains its value: migrating the procedural memory to a weaker model can also yield substantial performance gains. Code is available at https://github.com/zjunlp/MemP.

------------------------------------------------------------------------

3\. · 100% match · 2025 · 38 cit/yr\
**Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution** ([link](https://doi.org/10.48550/arXiv.2512.10696))\
Zouying Cao et al.\
*ArXiv* · Dec 11, 2025 · 19 citations

> Procedural memory enables large language model (LLM) agents to internalize”how-to”knowledge, theoretically reducing redundant trial-and-error. However, existing frameworks predominantly suffer from a”passive accumulation”paradigm, treating memory as a static append-only archive. To bridge the gap between static storage and dynamic reasoning, we propose $`\textbf{ReMe}`$ ($`\textit{Remember Me, Refine Me}`$), a comprehensive framework for experience-driven agent evolution. ReMe innovates across the memory lifecycle via three mechanisms: 1) $`\textit{multi-faceted distillation}`$, which extracts fine-grained experiences by recognizing success patterns, analyzing failure triggers and generating comparative insights; 2) $`\textit{context-adaptive reuse}`$, which tailors historical insights to new contexts via scenario-aware indexing; and 3) $`\textit{utility-based refinement}`$, which autonomously adds valid memories and prunes outdated ones to maintain a compact, high-quality experience pool. Extensive experiments on BFCL-V3 and AppWorld demonstrate that ReMe establishes a new state-of-the-art in agent memory system. Crucially, we observe a significant memory-scaling effect: Qwen3-8B equipped with ReMe outperforms larger, memoryless Qwen3-14B, suggesting that self-evolving memory provides a computation-efficient pathway for lifelong learning. We release our code and the $`\texttt{reme.library}`$ dataset to facilitate further research.

------------------------------------------------------------------------

4\. · 100% match · 2026 · 4.0 cit/yr\
**Traversal-as-Policy: Log-Distilled Gated Behavior Trees as Externalized, Verifiable Policies for Safe, Robust, and Efficient Agents** ([link](https://www.semanticscholar.org/paper/a4428f2803db336bca7f80a9e24e88110122d8cd))\
Peiran Li et al.\
Jan 30, 2026 · 2 citations

> Autonomous LLM agents fail because long-horizon policy remains implicit in model weights and transcripts, while safety is retrofitted post hoc. We propose Traversal-as-Policy: distill sandboxed OpenHands execution logs into a single executable Gated Behavior Tree (GBT) and treat tree traversal – rather than unconstrained generation – as the control policy whenever a task is in coverage. Each node encodes a state-conditioned action macro mined and merge-checked from successful trajectories; macros implicated by unsafe traces attach deterministic pre-execution gates over structured tool context and bounded history, updated under experience-grounded monotonicity so previously rejected unsafe contexts cannot be re-admitted. At runtime, a lightweight traverser matches the base model’s intent to child macros, executes one macro at a time under global and node-local gating, and when stalled performs risk-aware shortest-path recovery to a feasible success leaf; the visited path forms a compact spine memory that replaces transcript replay. Evaluated in a unified OpenHands sandbox on 15+ software, web, reasoning, and safety/security benchmarks, GBT improves success while driving violations toward zero and reducing cost. On SWE-bench Verified (Protocol A, 500 issues), GBT-SE raises success from 34.6% to 73.6%, reduces violations from 2.8% to 0.2%, and cuts token/character usage from 208k/820k to 126k/490k; with the same distilled tree, 8B executors more than double success on SWE-bench Verified (14.0%58.8%) and WebArena (9.1%37.3%).

------------------------------------------------------------------------

5\. · 100% match · 2023 · 1017 cit/yr\
**Reflexion: language agents with verbal reinforcement learning** ([link](https://doi.org/10.52202/075280-0377))\
Noah Shinn et al.\
*Advances in Neural Information Processing Systems 36* · Mar 20, 2023 · 3186 citations

> Large language models (LLMs) have been increasingly used to interact with external environments (e.g., games, compilers, APIs) as goal-driven agents. However, it remains challenging for these language agents to quickly and efficiently learn from trial-and-error as traditional reinforcement learning methods require extensive training samples and expensive model fine-tuning. We propose Reflexion, a novel framework to reinforce language agents not by updating weights, but instead through linguistic feedback. Concretely, Reflexion agents verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer to induce better decision-making in subsequent trials. Reflexion is flexible enough to incorporate various types (scalar values or free-form language) and sources (external or internally simulated) of feedback signals, and obtains significant improvements over a baseline agent across diverse tasks (sequential decision-making, coding, language reasoning). For example, Reflexion achieves a 91% pass@1 accuracy on the HumanEval coding benchmark, surpassing the previous state-of-the-art GPT-4 that achieves 80%. We also conduct ablation and analysis studies using different feedback signals, feedback incorporation methods, and agent types, and provide insights into how they affect performance.

------------------------------------------------------------------------

6\. · 100% match · 2024 · 18 cit/yr\
**AutoGuide: Automated Generation and Selection of Context-Aware Guidelines for Large Language Model Agents** ([link](https://doi.org/10.48550/arXiv.2403.08978))\
Yao Fu et al.\
*ArXiv* · Mar 13, 2024 · 39 citations

> Recent advances in large language models (LLMs) have empowered AI agents capable of performing various sequential decision-making tasks. However, effectively guiding LLMs to perform well in unfamiliar domains like web navigation, where they lack sufficient knowledge, has proven to be difficult with the demonstration-based in-context learning paradigm. In this paper, we introduce a novel framework, called AutoGuide, which addresses this limitation by automatically generating context-aware guidelines from offline experiences. Importantly, each context-aware guideline is expressed in concise natural language and follows a conditional structure, clearly describing the context where it is applicable. As a result, our guidelines facilitate the provision of relevant knowledge for the agent’s current decision-making process, overcoming the limitations of the conventional demonstration-based learning paradigm. Our evaluation demonstrates that AutoGuide significantly outperforms competitive baselines in complex benchmark domains, including real-world web navigation.

------------------------------------------------------------------------

7\. · 100% match · 2023 · 27 cit/yr\
**CLIN: A Continually Learning Language Agent for Rapid Task Adaptation and Generalization** ([link](https://doi.org/10.48550/arXiv.2310.10134))\
Bodhisattwa Prasad Majumder et al.\
*ArXiv* · Oct 16, 2023 · 69 citations

> Language agents have shown some ability to interact with an external environment, e.g., a virtual world such as ScienceWorld, to perform complex tasks, e.g., growing a plant, without the startup costs of reinforcement learning. However, despite their zero-shot capabilities, these agents to date do not continually improve over time beyond performance refinement on a specific task. Here we present CLIN, the first language-based agent to achieve this, so that it continually improves over multiple trials, including when both the environment and task are varied, and without requiring parameter updates. Our approach is to use a persistent, dynamic, textual memory centered on causal abstractions (rather than general”helpful hints”) that is regularly updated after each trial so that the agent gradually learns useful knowledge for new trials. In the ScienceWorld benchmark, CLIN is able to continually improve on repeated trials on the same task and environment, outperforming state-of-the-art reflective language agents like Reflexion by 23 absolute points. CLIN can also transfer its learning to new environments (or new tasks), improving its zero-shot performance by 4 points (13 for new tasks) and can further improve performance there through continual memory updates, enhancing performance by an additional 17 points (7 for new tasks). This suggests a new architecture for agents built on frozen models that can still continually and rapidly improve over time.

------------------------------------------------------------------------

8\. · 100% match · 2024 · 22 cit/yr\
**VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought** ([link](https://doi.org/10.52202/079017-2418))\
Gabriel Sarch et al.\
*Advances in Neural Information Processing Systems 37* · Jun 20, 2024 · 41 citations

> Large-scale generative language and vision-language models (LLMs and VLMs) excel in few-shot learning but require high-quality demonstrations. We propose In-Context Abstraction Learning (ICAL), enabling VLM agents to transform suboptimal trajectories into high-quality training data through self-reflection and human feedback. Given imperfect task demonstrations, a VLM abstracts trajectories into generalized strategies and action annotations by correcting inefficiencies and annotating cognitive abstractions: causal relationships, object state changes, temporal subgoals, and task-relevant visual elements. These annotations are iteratively refined through human feedback during execution in similar environments. The resulting examples significantly improve decision-making when used for retrieval-augmented generation or fine-tuning. As the agent’s example library grows, it becomes more efficient at abstracting new examples, requiring less human feedback and fewer environment interactions. ICAL achieves state-of-the-art results across multiple benchmarks. In TEACh dialogue-based instruction following, combining fine-tuning and retrieval on ICAL examples outperforms raw human demonstrations and expert examples by 17.5% in goal-condition success. In VisualWebArena, retrieval-augmented GPT-4V with ICAL improves task success 1.6x, while fine-tuned Qwen2-VL achieves 2.8x improvement over the base model. In Ego4D action forecasting, we surpass few-shot GPT-4V and remain competitive with supervised models. Our approach scales 2x better than raw demonstrations and significantly reduces manual prompt engineering requirements.

------------------------------------------------------------------------

9\. · 100% match · 2023 · 511 cit/yr\
**Voyager: An Open-Ended Embodied Agent with Large Language Models** ([link](https://doi.org/10.48550/arXiv.2305.16291))\
Guanzhi Wang et al.\
*ArXiv* · May 25, 2023 · 1507 citations

> We introduce Voyager, the first LLM-powered embodied lifelong learning agent in Minecraft that continuously explores the world, acquires diverse skills, and makes novel discoveries without human intervention. Voyager consists of three key components: 1) an automatic curriculum that maximizes exploration, 2) an ever-growing skill library of executable code for storing and retrieving complex behaviors, and 3) a new iterative prompting mechanism that incorporates environment feedback, execution errors, and self-verification for program improvement. Voyager interacts with GPT-4 via blackbox queries, which bypasses the need for model parameter fine-tuning. The skills developed by Voyager are temporally extended, interpretable, and compositional, which compounds the agent’s abilities rapidly and alleviates catastrophic forgetting. Empirically, Voyager shows strong in-context lifelong learning capability and exhibits exceptional proficiency in playing Minecraft. It obtains 3.3x more unique items, travels 2.3x longer distances, and unlocks key tech tree milestones up to 15.3x faster than prior SOTA. Voyager is able to utilize the learned skill library in a new Minecraft world to solve novel tasks from scratch, while other techniques struggle to generalize. We open-source our full codebase and prompts at https://voyager.minedojo.org/.

------------------------------------------------------------------------

10\. · 100% match · 2026 · 10 cit/yr\
**Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills** ([link](https://www.semanticscholar.org/paper/8b02872a17028c037e214fef695304494c809411))\
Jingwei Ni et al.\
Mar 26, 2026 · 5 citations

> Equipping Large Language Model (LLM) agents with domain-specific skills is critical for tackling complex tasks. Yet, manual authoring creates a severe scalability bottleneck. Conversely, automated skill generation often yields fragile or fragmented results because it either relies on shallow parametric knowledge or sequentially overfits to non-generalizable trajectory-local lessons. To overcome this, we introduce Trace2Skill, a framework that mirrors how human experts author skills: by holistically analyzing broad execution experience before distilling it into a single, comprehensive guide. Instead of reacting sequentially to individual trajectories, Trace2Skill dispatches a parallel fleet of sub-agents to analyze a diverse pool of executions. It extracts trajectory-specific lessons and hierarchically consolidates them into a unified, conflict-free skill directory via inductive reasoning. Trace2Skill supports both deepening existing human-written skills and creating new ones from scratch. Experiments in challenging domains, such as spreadsheet, VisionQA and math reasoning, show that Trace2Skill significantly improves upon strong baselines, including Anthropic’s official xlsx skills. Crucially, this trajectory-grounded evolution does not merely memorize task instances or model-specific quirks: evolved skills transfer across LLM scales and generalize to OOD settings. For example, skills evolved by Qwen3.5-35B on its own trajectories improved a Qwen3.5-122B agent by up to 57.65 absolute percentage points on WikiTableQuestions. Ultimately, our results demonstrate that complex agent experience can be packaged into highly transferable, declarative skills – requiring no parameter updates, no external retrieval modules, and utilizing open-source models as small as 35B parameters.

------------------------------------------------------------------------

11\. · 100% match · 2026\
**Evolving Programmatic Skill Networks** ([link](https://doi.org/10.48550/arXiv.2601.03509))\
Haochen Shi, Xingdi Yuan, and Bang Liu\
*ArXiv* · Jan 7, 2026 · 0 citations

> We study continual skill acquisition in open-ended embodied environments where an agent must construct, refine, and reuse an expanding library of executable skills. We introduce the Programmatic Skill Network (PSN), a framework in which skills are executable symbolic programs forming a compositional network that evolves through experience. PSN defines three core mechanisms instantiated via large language models: (1)REFLECT for structured fault localization over skill compositions, (2) progressive optimization with maturity-aware update gating that stabilizes reliable skills while maintaining plasticity for uncertain ones, and (3) canonical structural refactoring under rollback validation that maintains network compactness. We further show that PSN’s learning dynamics exhibit structural parallels to neural network training. Experiments on MineDojo and Crafter demonstrate robust skill reuse, rapid adaptation, and strong generalization across open-ended task distributions.\footnote{We plan to open-source the code.

------------------------------------------------------------------------

12\. · 100% match · 2026 · 6.0 cit/yr\
**Skill-Pro: Learning Reusable Skills from Experience via Non-Parametric PPO for LLM Agents** ([link](https://www.semanticscholar.org/paper/28f0b6f57e57337c7db267ae4ac52c12cbb5d376))\
Qirui Mi et al.\
Feb 2, 2026 · 3 citations

> LLM-driven agents demonstrate strong performance in sequential decision-making but often rely on on-the-fly reasoning, re-deriving solutions even in recurring scenarios. This insufficient experience reuse leads to computational redundancy and execution instability. To bridge this gap, we propose Skill-Pro, a framework that enables agents to autonomously learn reusable procedural skills from interaction experiences without parameter updates. By formalizing a Skill-MDP, Skill-Pro transforms passive episodic narratives into executable Skills defined by activation, execution, and termination conditions to ensure executability. To achieve reliable reusability without capability degradation, we introduce Non-Parametric PPO, which leverages semantic gradients for high-quality candidate generation and a PPO Gate for robust Skill verification. Through score-based maintenance, Skill-Pro sustains compact, high-quality procedural memory. Experimental results across in-domain, cross-task, and cross-agent scenarios demonstrate that Skill-Pro achieves superior reuse rates and significant performance gains with extreme memory compression. Visualized evolutionary trajectories and Skill distributions further reveal how Skill-Pro transparently accumulates, refines, and reuses procedural knowledge to facilitate long-term autonomy.

------------------------------------------------------------------------

13\. · 100% match · 2025 · 48 cit/yr\
**SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills** ([link](https://doi.org/10.48550/arXiv.2504.07079))\
Boyuan Zheng et al.\
*ArXiv* · Apr 9, 2025 · 52 citations

> To survive and thrive in complex environments, humans have evolved sophisticated self-improvement mechanisms through environment exploration, hierarchical abstraction of experiences into reuseable skills, and collaborative construction of an ever-growing skill repertoire. Despite recent advancements, autonomous web agents still lack crucial self-improvement capabilities, struggling with procedural knowledge abstraction, refining skills, and skill composition. In this work, we introduce SkillWeaver, a skill-centric framework enabling agents to self-improve by autonomously synthesizing reusable skills as APIs. Given a new website, the agent autonomously discovers skills, executes them for practice, and distills practice experiences into robust APIs. Iterative exploration continually expands a library of lightweight, plug-and-play APIs, significantly enhancing the agent’s capabilities. Experiments on WebArena and real-world websites demonstrate the efficacy of SkillWeaver, achieving relative success rate improvements of 31.8% and 39.8%, respectively. Additionally, APIs synthesized by strong agents substantially enhance weaker agents through transferable skills, yielding improvements of up to 54.3% on WebArena. These results demonstrate the effectiveness of honing diverse website interactions into APIs, which can be seamlessly shared among various web agents.

------------------------------------------------------------------------

14\. · 100% match · 2025 · 38 cit/yr\
**Inducing Programmatic Skills for Agentic Tasks** ([link](https://doi.org/10.48550/arXiv.2504.06821))\
Z. Wang, Apurva Gandhi, Graham Neubig, and Daniel Fried\
*ArXiv* · Apr 9, 2025 · 41 citations

> To succeed in common digital tasks such as web navigation, agents must carry out a variety of specialized tasks such as searching for products or planning a travel route. To tackle these tasks, agents can bootstrap themselves by learning task-specific skills online through interaction with the web environment. In this work, we demonstrate that programs are an effective representation for skills. We propose agent skill induction (ASI), which allows agents to adapt themselves by inducing, verifying, and utilizing program-based skills on the fly. We start with an evaluation on the WebArena agent benchmark and show that ASI outperforms the static baseline agent and its text-skill counterpart by 23.5% and 11.3% in success rate, mainly thanks to the programmatic verification guarantee during the induction phase. ASI also improves efficiency by reducing 10.7-15.3% of the steps over baselines, by composing primitive actions (e.g., click) into higher-level skills (e.g., search product). We then highlight the efficacy of ASI in remaining efficient and accurate under scaled-up web activities. Finally, we examine the generalizability of induced skills when transferring between websites, and find that ASI can effectively reuse common skills, while also updating incompatible skills to versatile website changes.

------------------------------------------------------------------------

15\. · 100% match · 2026 · 4.0 cit/yr\
**AutoRefine: From Trajectories to Reusable Expertise for Continual LLM Agent Refinement** ([link](https://doi.org/10.48550/arXiv.2601.22758))\
Libin Qiu et al.\
*ArXiv* · Jan 30, 2026 · 2 citations

> Large language model agents often fail to accumulate knowledge from experience, treating each task as an independent challenge. Recent methods extract experience as flattened textual knowledge, which cannot capture procedural logic of complex subtasks. They also lack maintenance mechanisms, causing repository degradation as experience accumulates. We introduce AutoRefine, a framework that extracts and maintains dual-form Experience Patterns from agent execution histories. For procedural subtasks, we extract specialized subagents with independent reasoning and memory. For static knowledge, we extract skill patterns as guidelines or code snippets. A continuous maintenance mechanism scores, prunes, and merges patterns to prevent repository degradation. Evaluated on ALFWorld, ScienceWorld, and TravelPlanner, AutoRefine achieves 98.4%, 70.4%, and 27.1% respectively, with 20-73% step reductions. On TravelPlanner, automatic extraction exceeds manually designed systems (27.1% vs 12.1%), demonstrating its ability to capture procedural coordination.

------------------------------------------------------------------------

16\. · 100% match · 2025 · 10 cit/yr\
**Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement** ([link](https://doi.org/10.48550/arXiv.2512.18950))\
Saman Forouzandeh, Wei Peng, Parham Moradi, Xinghuo Yu, and Mahdi Jalili\
*ArXiv* · Dec 22, 2025 · 5 citations

> We present MACLA, a framework that decouples reasoning from learning by maintaining a frozen large language model while performing all adaptation in an external hierarchical procedural memory. MACLA extracts reusable procedures from trajectories, tracks reliability via Bayesian posteriors, selects actions through expected-utility scoring, and refines procedures by contrasting successes and failures. Across four benchmarks (ALFWorld, WebShop, TravelPlanner, InterCodeSQL), MACLA achieves 78.1 percent average performance, outperforming all baselines. On ALFWorld unseen tasks, MACLA reaches 90.3 percent with 3.1 percent positive generalization. The system constructs memory in 56 seconds, 2800 times faster than the state-of-the-art LLM parameter-training baseline, compressing 2851 trajectories into 187 procedures. Experimental results demonstrate that structured external memory with Bayesian selection and contrastive refinement enables sample-efficient, interpretable, and continually improving agents without LLM parameter updates.

------------------------------------------------------------------------

17\. · 100% match · 2026\
**WebXSkill: Skill Learning for Autonomous Web Agents** ([link](https://www.semanticscholar.org/paper/f283b199100a8d976d1f3b6a8561f7597c6a068e))\
Zhaoyang Wang et al.\
Apr 14, 2026 · 0 citations

> Autonomous web agents powered by large language models (LLMs) have shown promise in completing complex browser tasks, yet they still struggle with long-horizon workflows. A key bottleneck is the grounding gap in existing skill formulations: textual workflow skills provide natural language guidance but cannot be directly executed, while code-based skills are executable but opaque to the agent, offering no step-level understanding for error recovery or adaptation. We introduce WebXSkill, a framework that bridges this gap with executable skills, each pairing a parameterized action program with step-level natural language guidance, enabling both direct execution and agent-driven adaptation. WebXSkill operates in three stages: skill extraction mines reusable action subsequences from readily available synthetic agent trajectories and abstracts them into parameterized skills, skill organization indexes skills into a URL-based graph for context-aware retrieval, and skill deployment exposes two complementary modes, grounded mode for fully automated multi-step execution and guided mode where skills serve as step-by-step instructions that the agent follows with its native planning. On WebArena and WebVoyager, WebXSkill improves task success rate by up to 9.8 and 12.9 points over the baseline, respectively, demonstrating the effectiveness of executable skills for web agents. The code is publicly available at https://github.com/aiming-lab/WebXSkill.

------------------------------------------------------------------------

18\. · 100% match · 2025 · 50 cit/yr\
**Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory** ([link](https://doi.org/10.48550/arXiv.2504.07952))\
Mirac Suzgun, Mert Yüksekgönül, Federico Bianchi, Daniel Jurafsky, and James Zou\
*ArXiv* · Apr 10, 2025 · 54 citations

> Despite their impressive performance on complex tasks, current language models (LMs) typically operate in a vacuum: Each input query is processed separately, without retaining insights from previous attempts. Here, we present Dynamic Cheatsheet (DC), a lightweight framework that endows a black-box LM with a persistent, evolving memory. Rather than repeatedly re-discovering or re-committing the same solutions and mistakes, DC enables models to store and reuse accumulated strategies, code snippets, and general problem-solving insights at inference time. This test-time learning enhances performance substantially across a range of tasks without needing explicit ground-truth labels or human feedback. Leveraging DC, Claude 3.5 Sonnet’s accuracy more than doubled on AIME math exams once it began retaining algebraic insights across questions. Similarly, GPT-4o’s success rate on Game of 24 increased from 10% to 99% after the model discovered and reused a Python-based solution. In tasks prone to arithmetic mistakes, such as balancing equations, DC enabled GPT-4o and Claude to reach near-perfect accuracy by recalling previously validated code, whereas their baselines stagnated around 50%. Beyond arithmetic challenges, DC yields notable accuracy gains on knowledge-demanding tasks. Claude achieved a 9% improvement in GPQA-Diamond and an 8% boost on MMLU-Pro problems. Crucially, DC’s memory is self-curated, focusing on concise, transferable snippets rather than entire transcript. Unlike finetuning or static retrieval methods, DC adapts LMs’ problem-solving skills on the fly, without modifying their underlying parameters. Overall, our findings present DC as a promising approach for augmenting LMs with persistent memory, bridging the divide between isolated inference events and the cumulative, experience-driven learning characteristic of human cognition.

------------------------------------------------------------------------

19\. · 100% match · 2025 · 52 cit/yr\
**Agent KB: Leveraging Cross-Domain Experience for Agentic Problem Solving** ([link](https://doi.org/10.48550/arXiv.2507.06229))\
Xiangru Tang et al.\
*ArXiv* · Jul 8, 2025 · 43 citations

> AI agent frameworks operate in isolation, forcing agents to rediscover solutions and repeat mistakes across different systems. Despite valuable problem-solving experiences accumulated by frameworks like smolagents, OpenHands, and OWL, this knowledge remains trapped within individual systems, preventing the emergence of collective intelligence. Current memory systems focus on individual agents or framework-specific demonstrations, failing to enable cross-architecture knowledge transfer. We introduce AGENT KB, a universal memory infrastructure enabling seamless experience sharing across heterogeneous agent frameworks without retraining. AGENT KB aggregates trajectories into a structured knowledge base and serves lightweight APIs. At inference time, hybrid retrieval operates through two stages: planning seeds agents with cross-domain workflows, while feedback applies targeted diagnostic fixes. A disagreement gate ensures retrieved knowledge enhances rather than disrupts reasoning, addressing knowledge interference in cross-framework transfer. We validate AGENT KB across major frameworks on GAIA, Humanity’s Last Exam, GPQA, and SWE-bench. Results show substantial improvements across diverse model families: compared to baseline pass@1, smolagents with AGENT KB achieve up to 18.7pp gains at pass@3 (55.2% -\>73.9%), while OpenHands improves 4.0pp on SWE-bench pass@1 (24.3% -\>28.3%). Similar improvements are observed across all base model families. Ablations confirm that hybrid retrieval and feedback stages are essential, with automatically generated experiences matching manual curation. This establishes the foundation for collective agent intelligence through shared memory infrastructures.

------------------------------------------------------------------------

20\. · 100% match · 2024 · 8.0 cit/yr\
**Skill Set Optimization: Reinforcing Language Model Behavior via Transferable Skills** ([link](https://doi.org/10.48550/arXiv.2402.03244))\
Kolby Nottingham et al.\
*International Conference on Machine Learning* · Feb 5, 2024 · 18 citations

> Large language models (LLMs) have recently been used for sequential decision making in interactive environments. However, leveraging environment reward signals for continual LLM actor improvement is not straightforward. We propose Skill Set Optimization (SSO) for improving LLM actor performance through constructing and refining sets of transferable skills. SSO constructs skills by extracting common subtrajectories with high rewards and generating subgoals and instructions to represent each skill. These skills are provided to the LLM actor in-context to reinforce behaviors with high rewards. Then, SSO further refines the skill set by pruning skills that do not continue to result in high rewards. We evaluate our method in the classic videogame NetHack and the text environment ScienceWorld to demonstrate SSO’s ability to optimize a set of skills and perform in-context policy improvement. SSO outperforms baselines by 40% in our custom NetHack task and outperforms the previous state-of-the-art in ScienceWorld by 35%.

------------------------------------------------------------------------

21\. · 100% match · 2024 · 14 cit/yr\
**AutoManual: Constructing Instruction Manuals by LLM Agents via Interactive Environmental Learning** ([link](https://doi.org/10.52202/079017-0019))\
Minghao Chen et al.\
*Advances in Neural Information Processing Systems 37* · May 25, 2024 · 27 citations

> Large Language Models (LLM) based agents have shown promise in autonomously completing tasks across various domains, e.g., robotics, games, and web navigation. However, these agents typically require elaborate design and expert prompts to solve tasks in specific domains, which limits their adaptability. We introduce AutoManual, a framework enabling LLM agents to autonomously build their understanding through interaction and adapt to new environments. AutoManual categorizes environmental knowledge into diverse rules and optimizes them in an online fashion by two agents: 1) The Planner codes actionable plans based on current rules for interacting with the environment. 2) The Builder updates the rules through a well-structured rule system that facilitates online rule management and essential detail retention. To mitigate hallucinations in managing rules, we introduce a *case-conditioned prompting* strategy for the Builder. Finally, the Formulator agent compiles these rules into a comprehensive manual. The self-generated manual can not only improve the adaptability but also guide the planning of smaller LLMs while being human-readable. Given only one simple demonstration, AutoManual significantly improves task success rates, achieving 97.4% with GPT-4-turbo and 86.2% with GPT-3.5-turbo on ALFWorld benchmark tasks. The code is available at https://github.com/minghchen/automanual.

------------------------------------------------------------------------

22\. · 100% match · 2025 · 24 cit/yr\
**Contextual Experience Replay for Self-Improvement of Language Agents** ([link](https://doi.org/10.48550/arXiv.2506.06698))\
Yitao Liu, Chenglei Si, Karthik R. Narasimhan, and Shunyu Yao\
*Annual Meeting of the Association for Computational Linguistics* · Jun 7, 2025 · 22 citations

> Large language model (LLM) agents have been applied to sequential decision-making tasks such as web navigation, but without any environment-specific experiences, they often fail in these complex tasks. Moreover, current LLM agents are not designed to continually learn from past experiences during inference time, which could be crucial for them to gain these environment-specific experiences. To address this, we propose Contextual Experience Replay (CER), a training-free framework to enable efficient self-improvement for language agents in their context window. Specifically, CER accumulates and synthesizes past experiences into a dynamic memory buffer. These experiences encompass environment dynamics and common decision-making patterns, allowing the agents to retrieve and augment themselves with relevant knowledge in new tasks, enhancing their adaptability in complex environments. We evaluate CER on the challenging WebArena and VisualWebArena benchmarks. On VisualWebArena, CER achieves a competitive performance of 31.9%. On WebArena, CER also gets a competitive average success rate of 36.7%, relatively improving the success rate of the GPT-4o agent baseline by 51.0%. We also conduct a comprehensive analysis on it to prove its efficiency, validity and understand it better.

------------------------------------------------------------------------

23\. · 100% match · 2025 · 3.0 cit/yr\
**Meta-Policy Reflexion: Reusable Reflective Memory and Rule Admissibility for Resource-Efficient LLM Agent** ([link](https://doi.org/10.48550/arXiv.2509.03990))\
Chunlong Wu, Ye Luo, Zhibo Qu, and Min Wang\
*ArXiv* · Sep 4, 2025 · 2 citations

> Large language model (LLM) agents achieve impressive single-task performance but commonly exhibit repeated failures, inefficient exploration, and limited cross-task adaptability. Existing reflective strategies (e.g., Reflexion, ReAct) improve per-episode behavior but typically produce ephemeral, task-specific traces that are not reused across tasks. Reinforcement-learning based alternatives can produce transferable policies but require substantial parameter updates and compute. In this work we introduce Meta-Policy Reflexion (MPR): a hybrid framework that consolidates LLM-generated reflections into a structured, predicate-like Meta-Policy Memory (MPM) and applies that memory at inference time through two complementary mechanisms soft memory-guided decoding and hard rule admissibility checks(HAC). MPR (i) externalizes reusable corrective knowledge without model weight updates, (ii) enforces domain constraints to reduce unsafe or invalid actions, and (iii) retains the adaptability of language-based reflection. We formalize the MPM representation, present algorithms for update and decoding, and validate the approach in a text-based agent environment following the experimental protocol described in the provided implementation (AlfWorld-based). Empirical results reported in the supplied material indicate consistent gains in execution accuracy and robustness when compared to Reflexion baselines; rule admissibility further improves stability. We analyze mechanisms that explain these gains, discuss scalability and failure modes, and outline future directions for multimodal and multi-agent extensions.

------------------------------------------------------------------------

24\. · 100% match · 2025 · 201 cit/yr\
**Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models** ([link](https://doi.org/10.48550/arXiv.2510.04618))\
Qizheng Zhang et al.\
*ArXiv* · Oct 6, 2025 · 117 citations

> Large language model (LLM) applications such as agents and domain-specific reasoning increasingly rely on context adaptation: modifying inputs with instructions, strategies, or evidence, rather than weight updates. Prior approaches improve usability but often suffer from brevity bias, which drops domain insights for concise summaries, and from context collapse, where iterative rewriting erodes details over time. We introduce ACE (Agentic Context Engineering), a framework that treats contexts as evolving playbooks that accumulate, refine, and organize strategies through a modular process of generation, reflection, and curation. ACE prevents collapse with structured, incremental updates that preserve detailed knowledge and scale with long-context models. Across agent and domain-specific benchmarks, ACE optimizes contexts both offline (e.g., system prompts) and online (e.g., agent memory), consistently outperforming strong baselines: +10.6% on agents and +8.6% on finance, while significantly reducing adaptation latency and rollout cost. Notably, ACE could adapt effectively without labeled supervision and instead by leveraging natural execution feedback. On the AppWorld leaderboard, ACE matches the top-ranked production-level agent on the overall average and surpasses it on the harder test-challenge split, despite using a smaller open-source model. These results show that comprehensive, evolving contexts enable scalable, efficient, and self-improving LLM systems with low overhead.

------------------------------------------------------------------------

25\. · 100% match · 2026\
**Compiled Memory: Not More Information, but More Precise Instructions for Language Agents** ([link](https://www.semanticscholar.org/paper/62dc0a497a2643f06303a81ee1cb9d7e1167ae7a))\
James G Rhodes and G. Kang\
Mar 12, 2026 · 0 citations

> Existing memory systems for language agents address memory management: how to retrieve and page more information within a context budget. We address a complementary problem – memory utility: what experience is worth keeping, and how it should change agent behavior. We present Atlas, a memory kernel that compiles accumulated task experience into an agent’s instruction structure – without fine-tuning, RAG, or human intervention. Memory is distillation, not storage; delivery is instruction rewriting, not context injection. Facts extracted from agent failures and successes are verified through a three-step promotion gate and delivered by rewriting the agent’s system prompt with learned sub-bullets. On CUAD contract analysis, the evolved prompt improves GPT-4o token-level F1 by $`+8.7`$pp and precision by $`+12.5`$pp. On HotpotQA multi-hop QA, joint F1 improves $`+3.16`$pp. An ablation isolates the mechanism’s defining property – the training signal constraint: the evolved prompt learns exactly what it is taught, and nothing more. Applied to Claude Sonnet~4.5 using the same evolved prompt – compiled from GPT-4o errors, unchanged – joint F1 improves $`+2.31`$pp, with gains concentrating where Claude’s stronger baseline leaves the most room – confirming that the compiled knowledge is task-shaped, not model-shaped.

------------------------------------------------------------------------

26\. · 100% match · 2023 · 174 cit/yr\
**ExpeL: LLM Agents Are Experiential Learners** ([link](https://doi.org/10.48550/arXiv.2308.10144))\
Andrew Zhao et al.\
*AAAI Conference on Artificial Intelligence* · Aug 20, 2023 · 473 citations

> The recent surge in research interest in applying large language models (LLMs) to decision-making tasks has flourished by leveraging the extensive world knowledge embedded in LLMs. While there is a growing demand to tailor LLMs for custom decision-making tasks, finetuning them for specific tasks is resource-intensive and may diminish the model’s generalization capabilities. Moreover, state-of-the-art language models like GPT-4 and Claude are primarily accessible through API calls, with their parametric weights remaining proprietary and unavailable to the public. This scenario emphasizes the growing need for new methodologies that allow learning from agent experiences without requiring parametric updates. To address these problems, we introduce the Experiential Learning (ExpeL) agent. Our agent autonomously gathers experiences and extracts knowledge using natural language from a collection of training tasks. At inference, the agent recalls its extracted insights and past experiences to make informed decisions. Our empirical results highlight the robust learning efficacy of the ExpeL agent, indicating a consistent enhancement in its performance as it accumulates experiences. We further explore the emerging capabilities and transfer learning potential of the ExpeL agent through qualitative observations and additional experiments.

------------------------------------------------------------------------

27\. · 100% match · 2026 · 2.0 cit/yr\
**ActionEngine: From Reactive to Programmatic GUI Agents via State Machine Memory** ([link](https://doi.org/10.48550/arXiv.2602.20502))\
Hongbin Zhong et al.\
*ArXiv* · Feb 24, 2026 · 1 citations

> Existing Graphical User Interface (GUI) agents operate through step-by-step calls to vision language models–taking a screenshot, reasoning about the next action, executing it, then repeating on the new page–resulting in high costs and latency that scale with the number of reasoning steps, and limited accuracy due to no persistent memory of previously visited pages. We propose ActionEngine, a training-free framework that transitions from reactive execution to programmatic planning through a novel two-agent architecture: a Crawling Agent that constructs an updatable state-machine memory of the GUIs through offline exploration, and an Execution Agent that leverages this memory to synthesize complete, executable Python programs for online task execution. To ensure robustness against evolving interfaces, execution failures trigger a vision-based re-grounding fallback that repairs the failed action and updates the memory. This design drastically improves both efficiency and accuracy: on Reddit tasks from the WebArena benchmark, our agent achieves 95% task success with on average a single LLM call, compared to 66% for the strongest vision-only baseline, while reducing cost by 11.8x and end-to-end latency by 2x. Together, these components yield scalable and reliable GUI interaction by combining global programmatic planning, crawler-validated action templates, and node-level execution with localized validation and repair.

------------------------------------------------------------------------

28\. · 100% match · 2025 · 350 cit/yr\
**A-MEM: Agentic Memory for LLM Agents** ([link](https://doi.org/10.48550/arXiv.2502.12110))\
Wujiang Xu et al.\
*ArXiv* · Feb 17, 2025 · 426 citations

> While large language model (LLM) agents can effectively use external tools for complex real-world tasks, they require memory systems to leverage historical experiences. Current memory systems enable basic storage and retrieval but lack sophisticated memory organization, despite recent attempts to incorporate graph databases. Moreover, these systems’fixed operations and structures limit their adaptability across diverse tasks. To address this limitation, this paper proposes a novel agentic memory system for LLM agents that can dynamically organize memories in an agentic way. Following the basic principles of the Zettelkasten method, we designed our memory system to create interconnected knowledge networks through dynamic indexing and linking. When a new memory is added, we generate a comprehensive note containing multiple structured attributes, including contextual descriptions, keywords, and tags. The system then analyzes historical memories to identify relevant connections, establishing links where meaningful similarities exist. Additionally, this process enables memory evolution - as new memories are integrated, they can trigger updates to the contextual representations and attributes of existing historical memories, allowing the memory network to continuously refine its understanding. Our approach combines the structured organization principles of Zettelkasten with the flexibility of agent-driven decision making, allowing for more adaptive and context-aware memory management. Empirical experiments on six foundation models show superior improvement against existing SOTA baselines. The source code for evaluating performance is available at https://github.com/WujiangXu/A-mem, while the source code of the agentic memory system is available at https://github.com/WujiangXu/A-mem-sys.

------------------------------------------------------------------------

29\. · 100% match · 2026 · 4.0 cit/yr\
**Enhancing Web Agents with a Hierarchical Memory Tree** ([link](https://www.semanticscholar.org/paper/bddff0e7853344b7f8e2bccc7e9145630b6e8b3e))\
Yunteng Tan, Zhiqiang Gao, and Xinxiao Wu\
Mar 7, 2026 · 2 citations

> Large language model-based web agents have shown strong potential in automating web interactions through advanced reasoning and instruction following. While retrieval-based memory derived from historical trajectories enables these agents to handle complex, long-horizon tasks, current methods struggle to generalize across unseen websites. We identify that this challenge arises from the flat memory structures that entangle high-level task logic with site-specific action details. This entanglement induces a workflow mismatch in new environments, where retrieved contents are conflated with current web, leading to logically inconsistent execution. To address this, we propose Hierarchical Memory Tree (HMT), a structured framework designed to explicitly decouple logical planning from action execution. HMT constructs a three-level hierarchy from raw trajectories via an automated abstraction pipeline: the Intent level maps diverse user instructions to standardized task goals; the Stage level defines reusable semantic subgoals characterized by observable pre-conditions and post-conditions; and the Action level stores action patterns paired with transferable semantic element descriptions. Leveraging this structure, we develop a stage-aware inference mechanism comprising a Planner and an Actor. By explicitly validating pre-conditions, the Planner aligns the current state with the correct logical subgoal to prevent workflow mismatch, while the Actor grounds actions by matching the stored semantic descriptions to the target page. Experimental results on Mind2Web and WebArena show that HMT significantly outperforms flat-memory methods, particularly in cross-website and cross-domain scenarios, highlighting the necessity of structured memory for robust generalization of web agents.

------------------------------------------------------------------------

30\. · 100% match · 2026\
**Environment Maps: Structured Environmental Representations for Long-Horizon Agents** ([link](https://www.semanticscholar.org/paper/8ff9c033934b39ec676e42bc84baa654e2453cc6))\
Yenchia Feng, Chirag Sharma, and Karime Maamari\
Mar 24, 2026 · 0 citations

> Although large language models (LLMs) have advanced rapidly, robust automation of complex software workflows remains an open problem. In long-horizon settings, agents frequently suffer from cascading errors and environmental stochasticity; a single misstep in a dynamic interface can lead to task failure, resulting in hallucinations or trial-and-error. This paper introduces $`\textit{Environment Maps}`$: a persistent, agent-agnostic representation that mitigates these failures by consolidating heterogeneous evidence, such as screen recordings and execution traces, into a structured graph. The representation consists of four core components: (1) Contexts (abstracted locations), (2) Actions (parameterized affordances), (3) Workflows (observed trajectories), and (4) Tacit Knowledge (domain definitions and reusable procedures). We evaluate this framework on the WebArena benchmark across five domains. Agents equipped with environment maps achieve a 28.2% success rate, nearly doubling the performance of baselines limited to session-bound context (14.2%) and outperforming agents that have access to the raw trajectory data used to generate the environment maps (23.3%). By providing a structured interface between the model and the environment, Environment Maps establish a persistent foundation for long-horizon planning that is human-interpretable, editable, and incrementally refinable.

------------------------------------------------------------------------

31\. · 100% match · 2025\
**Beyond Training: Enabling Self-Evolution of Agents with MOBIMEM** ([link](https://doi.org/10.48550/arXiv.2512.15784))\
Zibin Liu et al.\
*ArXiv* · Dec 15, 2025 · 0 citations

> Large Language Model (LLM) agents are increasingly deployed to automate complex workflows in mobile and desktop environments. However, current model-centric agent architectures struggle to self-evolve post-deployment: improving personalization, capability, and efficiency typically requires continuous model retraining/fine-tuning, which incurs prohibitive computational overheads and suffers from an inherent trade-off between model accuracy and inference efficiency. To enable iterative self-evolution without model retraining, we propose MOBIMEM, a memory-centric agent system. MOBIMEM first introduces three specialized memory primitives to decouple agent evolution from model weights: (1) Profile Memory uses a lightweight distance-graph (DisGraph) structure to align with user preferences, resolving the accuracy-latency trade-off in user profile retrieval; (2) Experience Memory employs multi-level templates to instantiate execution logic for new tasks, ensuring capability generalization; and (3) Action Memory records fine-grained interaction sequences, reducing the reliance on expensive model inference. Building upon this memory architecture, MOBIMEM further integrates a suite of OS-inspired services to orchestrate execution: a scheduler that coordinates parallel sub-task execution and memory operations; an agent record-and-replay (AgentRR) mechanism that enables safe and efficient action reuse; and a context-aware exception handling that ensures graceful recovery from user interruptions and runtime errors. Evaluation on AndroidWorld and top-50 apps shows that MOBIMEM achieves 83.1% profile alignment with 23.83 ms retrieval time (280x faster than GraphRAG baselines), improves task success rates by up to 50.3%, and reduces end-to-end latency by up to 9x on mobile devices.

------------------------------------------------------------------------

32\. · 100% match · 2025 · 44 cit/yr\
**G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems** ([link](https://doi.org/10.48550/arXiv.2506.07398))\
Gui-Min Zhang et al.\
*ArXiv* · Jun 9, 2025 · 40 citations

> Large language model (LLM)-powered multi-agent systems (MAS) have demonstrated cognitive and execution capabilities that far exceed those of single LLM agents, yet their capacity for self-evolution remains hampered by underdeveloped memory architectures. Upon close inspection, we are alarmed to discover that prevailing MAS memory mechanisms (1) are overly simplistic, completely disregarding the nuanced inter-agent collaboration trajectories, and (2) lack cross-trial and agent-specific customization, in stark contrast to the expressive memory developed for single agents. To bridge this gap, we introduce G-Memory, a hierarchical, agentic memory system for MAS inspired by organizational memory theory, which manages the lengthy MAS interaction via a three-tier graph hierarchy: insight, query, and interaction graphs. Upon receiving a new user query, G-Memory performs bi-directional memory traversal to retrieve both $`\textit{high-level, generalizable insights}`$ that enable the system to leverage cross-trial knowledge, and $`\textit{fine-grained, condensed interaction trajectories}`$ that compactly encode prior collaboration experiences. Upon task execution, the entire hierarchy evolves by assimilating new collaborative trajectories, nurturing the progressive evolution of agent teams. Extensive experiments across five benchmarks, three LLM backbones, and three popular MAS frameworks demonstrate that G-Memory improves success rates in embodied action and accuracy in knowledge QA by up to $`20.89\%`$ and $`10.12\%`$, respectively, without any modifications to the original frameworks. Our codes are available at https://github.com/bingreeky/GMemory.

------------------------------------------------------------------------

33\. · 100% match · 2026 · 18 cit/yr\
**AutoSkill: Experience-Driven Lifelong Learning via Skill Self-Evolution** ([link](https://doi.org/10.48550/arXiv.2603.01145))\
Yutao Yang et al.\
*ArXiv* · Mar 1, 2026 · 9 citations

> In practical LLM applications, users repeatedly express stable preferences and requirements, such as reducing hallucinations, following institutional writing conventions, or avoiding overly technical wording, yet such interaction experience is seldom consolidated into reusable knowledge. Consequently, LLM agents often fail to accumulate personalized capabilities across sessions. We present AutoSkill, an experience-driven lifelong learning framework that enables LLM agents to automatically derive, maintain, and reuse skills from dialogue and interaction traces. AutoSkill abstracts skills from user experience, supports their continual self-evolution, and dynamically injects relevant skills into future requests without retraining the underlying model. Designed as a model-agnostic plugin layer, it is compatible with existing LLMs and introduces a standardized skill representation for sharing and transfer across agents, users, and tasks. In this way, AutoSkill turns ephemeral interaction experience into explicit, reusable, and composable capabilities. This paper describes the motivation, architecture, skill lifecycle, and implementation of AutoSkill, and positions it with respect to prior work on memory, retrieval, personalization, and agentic systems. AutoSkill highlights a practical and scalable path toward lifelong personalized agents and personal digital surrogates.

------------------------------------------------------------------------

34\. · 100% match · 2025 · 49 cit/yr\
**What Deserves Memory: Adaptive Memory Distillation for LLM Agents** ([link](https://www.semanticscholar.org/paper/c7104ee40e801e802cdd6e85c26f1ca8dcc00b19))\
Wenquan Ma, Jiayan Nan, Wenlong Wu, and Yize Chen\
Aug 5, 2025 · 37 citations

> Memory systems for LLM agents struggle to determine what information deserves retention. Existing approaches rely on predefined heuristics such as importance scores, emotional tags, or factual templates, encoding designer intuition rather than learning from the data itself. Inspired by cognitive ideas, we propose NEMORI, an adaptive memory distillation framework that casts the assessment of experience’s future utility as a matter of predictability. Specifically, NEMORI comprises two cascading modules: Episodic Memory Integration transforms raw interactions into coherent narratives, and Semantic Knowledge Distillation extracts insights via prediction error. Centering on distillation, the framework remains agnostic to downstream management. Extensive experiments confirm that NEMORI achieves strong performance, efficiency, and storage reduction. Our work suggests that observing the intrinsic properties of interaction sequences offers a viable, data-driven alternative to heuristic-based memory design. Code: https://github.com/nemori-ai/nemori.

------------------------------------------------------------------------

35\. · 100% match · 2026 · 2.0 cit/yr\
**Darwinian Memory: A Training-Free Self-Regulating Memory System for GUI Agent Evolution** ([link](https://doi.org/10.48550/arXiv.2601.22528))\
Hongze Mi et al.\
*ArXiv* · Jan 30, 2026 · 1 citations

> Multimodal Large Language Model (MLLM) agents facilitate Graphical User Interface (GUI) automation but struggle with long-horizon, cross-application tasks due to limited context windows. While memory systems provide a viable solution, existing paradigms struggle to adapt to dynamic GUI environments, suffering from a granularity mismatch between high-level intent and low-level execution, and context pollution where the static accumulation of outdated experiences drives agents into hallucination. To address these bottlenecks, we propose the Darwinian Memory System (DMS), a self-evolving architecture that constructs memory as a dynamic ecosystem governed by the law of survival of the fittest. DMS decomposes complex trajectories into independent, reusable units for compositional flexibility, and implements Utility-driven Natural Selection to track survival value, actively pruning suboptimal paths and inhibiting high-risk plans. This evolutionary pressure compels the agent to derive superior strategies. Extensive experiments on real-world multi-app benchmarks validate that DMS boosts general-purpose MLLMs without training costs or architectural overhead, achieving average gains of 18.0% in success rate and 33.9% in execution stability, while reducing task latency, establishing it as an effective self-evolving memory system for GUI tasks.

------------------------------------------------------------------------

36\. · 100% match · 2026\
**APEX-EM: Non-Parametric Online Learning for Autonomous Agents via Structured Procedural-Episodic Experience Replay** ([link](https://www.semanticscholar.org/paper/16c110756c0f0395fe9cc9568434d9e5621cd464))\
Pratyay Banerjee, Masud Moshtaghi, and Ankit Chadha\
Mar 31, 2026 · 0 citations

> LLM-based autonomous agents lack persistent procedural memory: they re-derive solutions from scratch even when structurally identical tasks have been solved before. We present APEX-EM, a non-parametric online learning framework that accumulates, retrieves, and reuses structured procedural plans without modifying model weights. APEX-EM introduces: (1) a structured experience representation encoding the full procedural-episodic trace of each execution – planning steps, artifacts, iteration history with error analysis, and quality scores; (2) a Plan-Retrieve-Generate-Iterate-Ingest (PRGII) workflow with Task Verifiers providing multi-dimensional reward signals; and (3) a dual-outcome Experience Memory with hybrid retrieval combining semantic search, structural signature matching, and plan DAG traversal – enabling cross-domain transfer between tasks sharing no lexical overlap but analogous operational structure. Successful experiences serve as positive in-context examples; failures as negative examples with structured error annotations. We evaluate on BigCodeBench, KGQAGen-10k, and Humanity’s Last Exam using Claude Sonnet 4.5 and Opus 4.5. On KGQAGen-10k, APEX-EM achieves 89.6% accuracy versus 41.3% without memory (+48.3pp), surpassing the oracle-retrieval upper bound (84.9%). On BigCodeBench, it reaches 83.3% SR from a 53.9% baseline (+29.4pp), exceeding MemRL’s +11.0pp gain under comparable frozen-backbone conditions (noting backbone differences controlled for in our analysis). On HLE, entity graph retrieval reaches 48.0% from 25.2% (+22.8pp). Ablations show component value is task-dependent: rich judge feedback is negligible for code generation but critical for structured queries (+10.3pp), while binary-signal iteration partially compensates for weaker feedback.

------------------------------------------------------------------------

37\. · 100% match · 2025 · 3.3 cit/yr\
**Recon-Act: A Self-Evolving Multi-Agent Browser-Use System via Web Reconnaissance, Tool Generation, and Task Execution** ([link](https://doi.org/10.48550/arXiv.2509.21072))\
Kaiwen He, Zhiwei Wang, Chenyi Zhuang, and Jinjie Gu\
*ArXiv* · Sep 25, 2025 · 2 citations

> Recent years, multimodal models have made remarkable strides and pave the way for intelligent browser use agents. However, when solving tasks on real world webpages in multi-turn, long-horizon trajectories, current agents still suffer from disordered action sequencing and excessive trial and error during execution. This paper introduces Recon-Act, a self-evolving multi-agent framework grounded in Reconnaissance-Action behavioral paradigm. The system comprises a Reconnaissance Team and an Action Team: the former conducts comparative analysis and tool generation, while the latter handles intent decomposition, tool orchestration, and execution. By contrasting the erroneous trajectories with successful ones, the Reconnaissance Team infers remedies, and abstracts them into a unified notion of generalized tools, either expressed as hints or as rule-based codes, and register to the tool archive in real time. The Action Team reinference the process empowered with these targeting tools, thus establishing a closed-loop training pipeline of data-tools-action-feedback. Following the 6 level implementation roadmap proposed in this work, we have currently reached Level 3 (with limited human-in-the-loop intervention). Leveraging generalized tools obtained through reconnaissance, Recon-Act substantially improves adaptability to unseen websites and solvability on long-horizon tasks, and achieves state-of-the-art performance on the challenging VisualWebArena dataset.

------------------------------------------------------------------------

38\. · 100% match · 2025 · 5.3 cit/yr\
**Sample-Efficient Online Learning in LM Agents via Hindsight Trajectory Rewriting** ([link](https://doi.org/10.48550/arXiv.2510.10304))\
Michael Hu, Benjamin Van Durme, Jacob Andreas, and Harsh Jhamtani\
*ArXiv* · Oct 11, 2025 · 3 citations

> Language model (LM) agents deployed in novel environments often exhibit poor sample efficiency when learning from sequential interactions. This significantly hinders the usefulness of such agents in environments where interaction is costly (for example, when they interact with humans or reset physical systems). While a number of existing LM agent architectures incorporate various mechanisms for experience storage and reflection, they make limited use of LMs’abilities to directly generate or reason about full counterfactual trajectories. We introduce ECHO (Experience Consolidation via Hindsight Optimization), a prompting framework that adapts hindsight experience replay from reinforcement learning for language model agents. ECHO generates optimized trajectories for alternative goals that could have been achieved during failed attempts, effectively creating synthetic positive examples from unsuccessful interactions. Our approach consists of two components: a hindsight rule that uses the language model itself to identify relevant subgoals and generate optimized trajectories, and an update rule that maintains compressed trajectory representations in memory. We evaluate ECHO on stateful versions of XMiniGrid, a text-based navigation and planning benchmark, and PeopleJoinQA, a collaborative information-gathering enterprise simulation. Across both domains, ECHO outperforms vanilla language agent baselines by up to 80%; in XMiniGrid, it also outperforms a number of sophisticated agent architectures including Reflexion and AWM, demonstrating faster adaptation to novel environments through more effective utilization of past experiences.

------------------------------------------------------------------------

39\. · 100% match · 2026\
**BrainMem: Brain-Inspired Evolving Memory for Embodied Agent Task Planning** ([link](https://www.semanticscholar.org/paper/9e5eb6557069adc35643a2efacd4f5d1670dc348))\
Xiaoyu Ma et al.\
Mar 12, 2026 · 0 citations

> Embodied task planning requires agents to execute long-horizon, goal-directed actions in complex 3D environments, where success depends on both immediate perception and accumulated experience across tasks. However, most existing LLM-based planners are stateless and reactive, operating without persistent memory and therefore repeating errors and struggling with spatial or temporal dependencies. We propose BrainMem(Brain-Inspired Evolving Memory), a training-free hierarchical memory system that equips embodied agents with working, episodic, and semantic memory inspired by human cognition. BrainMem continuously transforms interaction histories into structured knowledge graphs and distilled symbolic guidelines, enabling planners to retrieve, reason over, and adapt behaviors from past experience without any model fine-tuning or additional training. This plug-and-play design integrates seamlessly with arbitrary multi-modal LLMs and greatly reduces reliance on task-specific prompt engineering. Extensive experiments on four representative benchmarks, including EB-ALFRED, EB-Navigation, EB-Manipulation, and EB-Habitat, demonstrate that BrainMem significantly enhances task success rates across diverse models and difficulty subsets, with the largest gains observed on long-horizon and spatially complex tasks. These results highlight evolving memory as a promising and scalable mechanism for generalizable embodied intelligence.

------------------------------------------------------------------------

40\. · 100% match · 2026\
**M2: Dual-Memory Augmentation for Long-Horizon Web Agents via Trajectory Summarization and Insight Retrieval** ([link](https://doi.org/10.48550/arXiv.2603.00503))\
Dawei Yan et al.\
*ArXiv* · Feb 28, 2026 · 0 citations

> Multimodal Large Language Models (MLLMs) based agents have demonstrated remarkable potential in autonomous web navigation. However, handling long-horizon tasks remains a critical bottleneck. Prevailing strategies often rely heavily on extensive data collection and model training, yet still struggle with high computational costs and insufficient reasoning capabilities when facing complex, long-horizon scenarios. To address this, we propose M$`^2`$, a training-free, memory-augmented framework designed to optimize context efficiency and decision-making robustness. Our approach incorporates a dual-tier memory mechanism that synergizes Dynamic Trajectory Summarization (Internal Memory) to compress verbose interaction history into concise state updates, and Insight Retrieval Augmentation (External Memory) to guide the agent with actionable guidelines retrieved from an offline insight bank. Extensive evaluations across WebVoyager and OnlineMind2Web demonstrate that M$`^2`$ consistently surpasses baselines, yielding up to a 19.6% success rate increase and 58.7% token reduction for Qwen3-VL-32B, while proprietary models like Claude achieve accuracy gains up to 12.5% alongside significantly lower computational overhead.

------------------------------------------------------------------------

41\. · 100% match · 2023 · 76 cit/yr\
**REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction** ([link](https://doi.org/10.48550/arXiv.2306.15724))\
Zeyi Liu, Arpit Bahety, and Shuran Song\
*ArXiv* · Jun 27, 2023 · 217 citations

> The ability to detect and analyze failed executions automatically is crucial for an explainable and robust robotic system. Recently, Large Language Models (LLMs) have demonstrated strong reasoning abilities on textual inputs. To leverage the power of LLMs for robot failure explanation, we introduce REFLECT, a framework which queries LLM for failure reasoning based on a hierarchical summary of robot past experiences generated from multisensory observations. The failure explanation can further guide a language-based planner to correct the failure and complete the task. To systematically evaluate the framework, we create the RoboFail dataset with a variety of tasks and failure scenarios. We demonstrate that the LLM-based framework is able to generate informative failure explanations that assist successful correction planning.

------------------------------------------------------------------------

42\. · 100% match · 2026 · 2.0 cit/yr\
**SkillX: Automatically Constructing Skill Knowledge Bases for Agents** ([link](https://www.semanticscholar.org/paper/24566e0b5989b1b32951ff9a10b6d6b0162683f5))\
Chenxi Wang et al.\
Apr 6, 2026 · 1 citations

> Learning from experience is critical for building capable large language model (LLM) agents, yet prevailing self-evolving paradigms remain inefficient: agents learn in isolation, repeatedly rediscover similar behaviors from limited experience, resulting in redundant exploration and poor generalization. To address this problem, we propose SkillX, a fully automated framework for constructing a \textbf{plug-and-play skill knowledge base} that can be reused across agents and environments. SkillX operates through a fully automated pipeline built on three synergistic innovations: \textit{(i) Multi-Level Skills Design}, which distills raw trajectories into three-tiered hierarchy of strategic plans, functional skills, and atomic skills; \textit{(ii) Iterative Skills Refinement}, which automatically revises skills based on execution feedback to continuously improve library quality; and \textit{(iii) Exploratory Skills Expansion}, which proactively generates and validates novel skills to expand coverage beyond seed training data. Using a strong backbone agent (GLM-4.6), we automatically build a reusable skill library and evaluate its transferability on challenging long-horizon, user-interactive benchmarks, including AppWorld, BFCL-v3, and $`\tau^2`$-Bench. Experiments show that SkillKB consistently improves task success and execution efficiency when plugged into weaker base agents, highlighting the importance of structured, hierarchical experience representations for generalizable agent learning. Our code will be publicly available soon at https://github.com/zjunlp/SkillX.

------------------------------------------------------------------------

43\. · 100% match · 2025 · 26 cit/yr\
**GUI-explorer: Autonomous Exploration and Mining of Transition-aware Knowledge for GUI Agent** ([link](https://doi.org/10.48550/arXiv.2505.16827))\
Bin Xie et al.\
*Annual Meeting of the Association for Computational Linguistics* · May 22, 2025 · 25 citations

> GUI automation faces critical challenges in dynamic environments. MLLMs suffer from two key issues: misinterpreting UI components and outdated knowledge. Traditional fine-tuning methods are costly for app-specific knowledge updates. We propose GUI-explorer, a training-free GUI agent that incorporates two fundamental mechanisms: (1) Autonomous Exploration of Function-aware Trajectory. To comprehensively cover all application functionalities, we design a Function-aware Task Goal Generator that automatically constructs exploration goals by analyzing GUI structural information (e.g., screenshots and activity hierarchies). This enables systematic exploration to collect diverse trajectories. (2) Unsupervised Mining of Transition-aware Knowledge. To establish precise screen-operation logic, we develop a Transition-aware Knowledge Extractor that extracts effective screen-operation logic through unsupervised analysis the state transition of structured interaction triples (observation, action, outcome). This eliminates the need for human involvement in knowledge extraction. With a task success rate of 53.7% on SPA-Bench and 47.4% on AndroidWorld, GUI-explorer shows significant improvements over SOTA agents. It requires no parameter updates for new apps. GUI-explorer is open-sourced and publicly available at https://github.com/JiuTian-VL/GUI-explorer.

------------------------------------------------------------------------

44\. · 100% match · 2026\
**Aligning Progress and Feasibility: A Neuro-Symbolic Dual Memory Framework for Long-Horizon LLM Agents** ([link](https://www.semanticscholar.org/paper/d79865a4e99248187eb1fcf28fb2407c261be74d))\
Bin Wen, Ruoxuan Zhang, Yangtao Chen, Hongxia Xie, and Lan-Zhe Guo\
Apr 3, 2026 · 0 citations

> Large language models (LLMs) have demonstrated strong potential in long-horizon decision-making tasks, such as embodied manipulation and web interaction. However, agents frequently struggle with endless trial-and-error loops or deviate from the main objective in complex environments. We attribute these failures to two fundamental errors: global Progress Drift and local Feasibility Violation. Existing methods typically attempt to address both issues simultaneously using a single paradigm. However, these two challenges are fundamentally distinct: the former relies on fuzzy semantic planning, while the latter demands strict logical constraints and state validation. The inherent limitations of such a single-paradigm approach pose a fundamental challenge for existing models in handling long-horizon tasks. Motivated by this insight, we propose a Neuro-Symbolic Dual Memory Framework that explicitly decouples semantic progress guidance from logical feasibility verification. Specifically, during the inference phase, the framework invokes both memory mechanisms synchronously: on one hand, a neural-network-based Progress Memory extracts semantic blueprints from successful trajectories to guide global task advancement; on the other hand, a symbolic-logic-based Feasibility Memory utilizes executable Python verification functions synthesized from failed transitions to perform strict logical validation. Experiments demonstrate that this method significantly outperforms existing competitive baselines on ALFWorld, WebShop, and TextCraft, while drastically reducing the invalid action rate and average trajectory length.

------------------------------------------------------------------------

45\. · 100% match · 2025 · 44 cit/yr\
**SWE-Exp: Experience-Driven Software Issue Resolution** ([link](https://doi.org/10.48550/arXiv.2507.23361))\
Silin Chen et al.\
*ArXiv* · Jul 31, 2025 · 34 citations

> Recent advances in large language model (LLM) agents have shown remarkable progress in software issue resolution, leveraging advanced techniques such as multi-agent collaboration and Monte Carlo Tree Search (MCTS). However, current agents act as memoryless explorers - treating each problem separately without retaining or reusing knowledge from previous repair experiences. This leads to redundant exploration of failed trajectories and missed chances to adapt successful issue resolution methods to similar problems. To address this problem, we introduce SWE-Exp, an experience-enhanced approach that distills concise and actionable experience from prior agent trajectories, enabling continuous learning across issues. Our method introduces a multi-faceted experience bank that captures both successful and failed repair attempts. Specifically, it extracts reusable issue resolution knowledge at different levels - from high-level problem comprehension to specific code changes. Experiments show that SWE-Exp achieves a Pass@1 resolution rate of 73.0% on SWE-Bench Verified using the state-of-the-art LLM Claude 4 Sonnet, significantly outperforming prior results under other agent frameworks. Our approach establishes a new paradigm in which automated software engineering agents systematically accumulate and leverage repair expertise, fundamentally shifting from trial-and-error exploration to strategic, experience-driven issue resolution.

------------------------------------------------------------------------

46\. · 100% match · 2026\
**SkillClaw: Let Skills Evolve Collectively with Agentic Evolver** ([link](https://www.semanticscholar.org/paper/3d795acefb5939ec88767d9a01dffb765fb90111))\
Ziyu Ma et al.\
Apr 9, 2026 · 0 citations

> Large language model (LLM) agents such as OpenClaw rely on reusable skills to perform complex tasks, yet these skills remain largely static after deployment. As a result, similar workflows, tool usage patterns, and failure modes are repeatedly rediscovered across users, preventing the system from improving with experience. While interactions from different users provide complementary signals about when a skill works or fails, existing systems lack a mechanism to convert such heterogeneous experiences into reliable skill updates. To address these issues, we present SkillClaw, a framework for collective skill evolution in multi-user agent ecosystems, which treats cross-user and over-time interactions as the primary signal for improving skills. SkillClaw continuously aggregates trajectories generated during use and processes them with an autonomous evolver, which identifies recurring behavioral patterns and translates them into updates to the skill set by refining existing skills or extending them with new capabilities. The resulting skills are maintained in a shared repository and synchronized across users, allowing improvements discovered in one context to propagate system-wide while requiring no additional effort from users. By integrating multi-user experience into ongoing skill updates, SkillClaw enables cross-user knowledge transfer and cumulative capability improvement, and experiments on WildClawBench show that limited interaction and feedback, it significantly improves the performance of Qwen3-Max in real-world agent scenarios.

------------------------------------------------------------------------

47\. · 100% match · 2025 · 11 cit/yr\
**PolySkill: Learning Generalizable Skills Through Polymorphic Abstraction** ([link](https://doi.org/10.48550/arXiv.2510.15863))\
Simon Yu, Gang Li, Weiyan Shi, and Pengyuan Qi\
*ArXiv* · Oct 17, 2025 · 6 citations

> Large language models (LLMs) are moving beyond static uses and are now powering agents that learn continually during their interaction with external environments. For example, agents can learn reusable skills while navigating web pages or toggling new tools. However, existing methods for skill learning often create skills that are over-specialized to a single website and fail to generalize. We introduce PolySkill, a new framework that enables agents to learn generalizable and compositional skills. The core idea, inspired by polymorphism in software engineering, is to decouple a skill’s abstract goal (what it accomplishes) and its concrete implementation (how it is executed). Experiments show that our method (1) improves skill reuse by 1.7x on seen websites and (2) boosts success rates by up to 9.4% on Mind2Web and 13.9% on unseen websites, while reducing steps by over 20%. (3) In self-exploration settings without specified tasks, our framework improves the quality of proposed tasks and enables agents to learn generalizable skills that work across different sites. By enabling the agent to identify and refine its own goals, the PolySkill enhances the agent’s ability to learn a better curriculum, leading to the acquisition of more generalizable skills compared to baseline methods. This work provides a practical path toward building agents capable of continual learning in adaptive environments. Our findings show that separating a skill’s goal from its execution is a crucial step toward developing autonomous agents that can learn and generalize across the open web continuously. Our code can be found in https://github.com/simonucl/PolySkill.

------------------------------------------------------------------------

48\. · 100% match · 2025 · 4.2 cit/yr\
**Coarse-to-Fine Grounded Memory for LLM Agent Planning** ([link](https://doi.org/10.48550/arXiv.2508.15305))\
Wei Yang et al.\
*Conference on Empirical Methods in Natural Language Processing* · Aug 21, 2025 · 3 citations

> Recent advancements in Large Language Models (LLMs) have driven growing interest in LLM-based agents for complex planning tasks. To avoid costly agent training, many studies adopted memory mechanism that enhances LLM with offline experiences or online trajectory analysis. However, existing works focus on single-granularity memory derived from dynamic environmental interactions, which are inherently constrained by the quality of the collected experiences. This limitation, in turn, constrain the diversity of knowledge and the flexibility of planning. We propose Coarse-to-Fine Grounded Memory (\Ours{}), a novel framework that grounds coarse-to-fine memories with LLM, thereby fully leverage them for flexible adaptation to diverse scenarios. \Ours{} grounds environmental information into coarse-grained focus points to guide experience collection in training tasks, followed by grounding of actionable hybrid-grained tips from each experience. At inference, \Ours{} retrieves task-relevant experiences and tips to support planning. When facing environmental anomalies, the LLM grounds the current situation into fine-grained key information, enabling flexible self-QA reflection and plan correction.

------------------------------------------------------------------------

49\. · 100% match · 2026 · 2.0 cit/yr\
**AndroTMem: From Interaction Trajectories to Anchored Memory in Long-Horizon GUI Agents** ([link](https://www.semanticscholar.org/paper/1b4c03b4374e581df75c8128de879afb2792623c))\
Yi Shi et al.\
Mar 19, 2026 · 1 citations

> Long-horizon GUI agents are a key step toward real-world deployment, yet effective interaction memory under prevailing paradigms remains under-explored. Replaying full interaction sequences is redundant and amplifies noise, while summaries often erase dependency-critical information and traceability. We present AndroTMem, a diagnostic framework for anchored memory in long-horizon Android GUI agents. Its core benchmark, AndroTMem-Bench, comprises 1,069 tasks with 34,473 interaction steps (avg. 32.1 per task, max. 65). We evaluate agents with TCR (Task Complete Rate), focusing on tasks whose completion requires carrying forward critical intermediate state; AndroTMem-Bench is designed to enforce strong step-to-step causal dependencies, making sparse yet essential intermediate states decisive for downstream actions and centering interaction memory in evaluation. Across open- and closed-source GUI agents, we observe a consistent pattern: as interaction sequences grow longer, performance drops are driven mainly by within-task memory failures, not isolated perception errors or local action mistakes. Guided by this diagnosis, we propose Anchored State Memory (ASM), which represents interaction sequences as a compact set of causally linked intermediate-state anchors to enable subgoal-targeted retrieval and attribution-aware decision making. Across multiple settings and 12 evaluated GUI agents, ASM consistently outperforms full-sequence replay and summary-based baselines, improving TCR by 5%-30.16% and AMS by 4.93%-24.66%, indicating that anchored, structured memory effectively mitigates the interaction-memory bottleneck in long-horizon GUI tasks. The code, benchmark, and related resources are publicly available at <https://github.com/CVC2233/AndroTMem>.

------------------------------------------------------------------------

50\. · 100% match · 2025 · 6.5 cit/yr\
**MemOrb: A Plug-and-Play Verbal-Reinforcement Memory Layer for E-Commerce Customer Service** ([link](https://doi.org/10.48550/arXiv.2509.18713))\
Yizhe Huang et al.\
*ArXiv* · Sep 23, 2025 · 4 citations

> Large Language Model-based agents(LLM-based agents) are increasingly deployed in customer service, yet they often forget across sessions, repeat errors, and lack mechanisms for continual self-improvement. This makes them unreliable in dynamic settings where stability and consistency are critical. To better evaluate these properties, we emphasize two indicators: task success rate as a measure of overall effectiveness, and consistency metrics such as Pass$`^k`$ to capture reliability across multiple trials. To address the limitations of existing approaches, we propose MemOrb, a lightweight and plug-and-play verbal reinforcement memory layer that distills multi-turn interactions into compact strategy reflections. These reflections are stored in a shared memory bank and retrieved to guide decision-making, without requiring any fine-tuning. Experiments show that MemOrb significantly improves both success rate and stability, achieving up to a 63 percentage-point gain in multi-turn success rate and delivering more consistent performance across repeated trials. Our results demonstrate that structured reflection is a powerful mechanism for enhancing long-term reliability of frozen LLM agents in customer service scenarios.

*Showing top 50 of 110 papers. Full details available via CSV or BibTeX export.*
