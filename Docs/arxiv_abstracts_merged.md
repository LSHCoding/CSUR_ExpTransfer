# A-MEM: Agentic Memory for LLM Agents

**arXiv ID**: 2502.12110
**arXiv URL**: https://arxiv.org/abs/2502.12110

## Abstract

While large language model (LLM) agents can effectively use external tools for complex real-world tasks, they require memory systems to leverage historical experiences. Current memory systems enable basic storage and retrieval but lack sophisticated memory organization, despite recent attempts to incorporate graph databases. Moreover, these systems' fixed operations and structures limit their adaptability across diverse tasks. To address this limitation, this paper proposes a novel agentic memory system for LLM agents that can dynamically organize memories in an agentic way. Following the basic principles of the Zettelkasten method, we designed our memory system to create interconnected knowledge networks through dynamic indexing and linking. When a new memory is added, we generate a comprehensive note containing multiple structured attributes, including contextual descriptions, keywords, and tags. The system then analyzes historical memories to identify relevant connections, establishing links where meaningful similarities exist. Additionally, this process enables memory evolution - as new memories are integrated, they can trigger updates to the contextual representations and attributes of existing historical memories, allowing the memory network to continuously refine its understanding. Our approach combines the structured organization principles of Zettelkasten with the flexibility of agent-driven decision making, allowing for more adaptive and context-aware memory management. Empirical experiments on six foundation models show superior improvement against existing SOTA baselines. The source code for evaluating performance is available at https://github.com/WujiangXu/A-mem, while the source code of the agentic memory system is available at https://github.com/WujiangXu/A-mem-sys.



---


# ABot-Claw: A Foundation for Persistent, Cooperative, and Self-Evolving Robotic Agents

**arXiv ID**: 2604.10096
**arXiv URL**: https://arxiv.org/abs/2604.10096

## Abstract

Current embodied intelligent systems still face a substantial gap between high-level reasoning and low-level physical execution in open-world environments. Although Vision-Language-Action (VLA) models provide strong perception and intuitive responses, their open-loop nature limits long-horizon performance. Agents incorporating System 2 cognitive mechanisms improve planning, but usually operate in closed sandboxes with predefined toolkits and limited real-system control. OpenClaw provides a localized runtime with full system privileges, but lacks the embodied control architecture required for long-duration, multi-robot execution. We therefore propose ABot-Claw, an embodied extension of OpenClaw that integrates: 1) a unified embodiment interface with capability-driven scheduling for heterogeneous robot coordination; 2) a visual-centric cross-embodiment multimodal memory for persistent context retention and grounded retrieval; and 3) a critic-based closed-loop feedback mechanism with a generalist reward model for online progress evaluation, local correction, and replanning. With a decoupled architecture spanning the OpenClaw layer, shared service layer, and robot embodiment layer, ABot-Claw enables real-world interaction, closes the loop from natural language intent to physical action, and supports progressively self-evolving robotic agents in open, dynamic environments.



---


# AFlow: Automating Agentic Workflow Generation

**arXiv ID**: 2410.10762
**arXiv URL**: https://arxiv.org/abs/2410.10762

## Abstract

Large language models (LLMs) have demonstrated remarkable potential in solving complex tasks across diverse domains, typically by employing agentic workflows that follow detailed instructions and operational sequences. However, constructing these workflows requires significant human effort, limiting scalability and generalizability. Recent research has sought to automate the generation and optimization of these workflows, but existing methods still rely on initial manual setup and fall short of achieving fully automated and effective workflow generation. To address this challenge, we reformulate workflow optimization as a search problem over code-represented workflows, where LLM-invoking nodes are connected by edges. We introduce AFlow, an automated framework that efficiently explores this space using Monte Carlo Tree Search, iteratively refining workflows through code modification, tree-structured experience, and execution feedback. Empirical evaluations across six benchmark datasets demonstrate AFlow's efficacy, yielding a 5.7% average improvement over state-of-the-art baselines. Furthermore, AFlow enables smaller models to outperform GPT-4o on specific tasks at 4.55% of its inference cost in dollars. The code is available at https://github.com/FoundationAgents/AFlow.



---


# ALFWorld: Aligning Text and Embodied Environments for Interactive Learning

**arXiv ID**: 2010.03768
**arXiv URL**: https://arxiv.org/abs/2010.03768

## Abstract

Given a simple request like Put a washed apple in the kitchen fridge, humans can reason in purely abstract terms by imagining action sequences and scoring their likelihood of success, prototypicality, and efficiency, all without moving a muscle. Once we see the kitchen in question, we can update our abstract plans to fit the scene. Embodied agents require the same abilities, but existing work does not yet provide the infrastructure necessary for both reasoning abstractly and executing concretely. We address this limitation by introducing ALFWorld, a simulator that enables agents to learn abstract, text based policies in TextWorld (Côté et al., 2018) and then execute goals from the ALFRED benchmark (Shridhar et al., 2020) in a rich visual environment. ALFWorld enables the creation of a new BUTLER agent whose abstract knowledge, learned in TextWorld, corresponds directly to concrete, visually grounded actions. In turn, as we demonstrate empirically, this fosters better agent generalization than training only in the visually grounded environment. BUTLER's simple, modular design factors the problem to allow researchers to focus on models for improving every piece of the pipeline (language understanding, planning, navigation, and visual scene understanding).



---


# ATLaS: Agent Tuning via Learning Critical Steps

**arXiv ID**: 2503.02197
**arXiv URL**: https://arxiv.org/abs/2503.02197

## Abstract

Large Language Model (LLM) agents have demonstrated remarkable generalization capabilities across multi-domain tasks. Existing agent tuning approaches typically employ supervised finetuning on entire expert trajectories. However, behavior-cloning of full trajectories can introduce expert bias and weaken generalization to states not covered by the expert data. Additionally, critical steps, such as planning, complex reasoning for intermediate subtasks, and strategic decision-making, are essential to success in agent tasks, so learning these steps is the key to improving LLM agents. For more effective and efficient agent tuning, we propose ATLaS that identifies the critical steps in expert trajectories and finetunes LLMs solely on these steps with reduced costs. By steering the training's focus to a few critical steps, our method mitigates the risk of overfitting entire trajectories and promotes generalization across different environments and tasks. In extensive experiments, an LLM finetuned on only 30% critical steps selected by ATLaS outperforms the LLM finetuned on all steps and recent open-source LLM agents. ATLaS maintains and improves base LLM skills as generalist agents interacting with diverse environments.



---


# Act Wisely: Cultivating Meta-Cognitive Tool Use in Agentic Multimodal Models

**arXiv ID**: 2604.08545
**arXiv URL**: https://arxiv.org/abs/2604.08545

## Abstract

The advent of agentic multimodal models has empowered systems to actively interact with external environments. However, current agents suffer from a profound meta-cognitive deficit: they struggle to arbitrate between leveraging internal knowledge and querying external utilities. Consequently, they frequently fall prey to blind tool invocation, resorting to reflexive tool execution even when queries are resolvable from the raw visual context. This pathological behavior precipitates severe latency bottlenecks and injects extraneous noise that derails sound reasoning. Existing reinforcement learning protocols attempt to mitigate this via a scalarized reward that penalizes tool usage. Yet, this coupled formulation creates an irreconcilable optimization dilemma: an aggressive penalty suppresses essential tool use, whereas a mild penalty is entirely subsumed by the variance of the accuracy reward during advantage normalization, rendering it impotent against tool overuse. To transcend this bottleneck, we propose HDPO, a framework that reframes tool efficiency from a competing scalar objective to a strictly conditional one. By eschewing reward scalarization, HDPO maintains two orthogonal optimization channels: an accuracy channel that maximizes task correctness, and an efficiency channel that enforces execution economy exclusively within accurate trajectories via conditional advantage estimation. This decoupled architecture naturally induces a cognitive curriculum-compelling the agent to first master task resolution before refining its self-reliance. Extensive evaluations demonstrate that our resulting model, Metis, reduces tool invocations by orders of magnitude while simultaneously elevating reasoning accuracy.



---


# Agent Learning via Early Experience

**arXiv ID**: 2510.08558
**arXiv URL**: https://arxiv.org/abs/2510.08558

## Abstract

A long-term goal of language agents is to learn and improve through their own experience, ultimately outperforming humans in complex, real-world tasks. However, training agents from experience data with reinforcement learning remains difficult in many environments, which either lack verifiable rewards (e.g., websites) or require inefficient long-horizon rollouts (e.g., multi-turn tool use). As a result, most current agents rely on supervised fine-tuning on expert data, which is challenging to scale and generalizes poorly. This limitation stems from the nature of expert demonstrations: they capture only a narrow range of scenarios and expose the agent to limited environment diversity. We address this limitation with a middle-ground paradigm we call early experience: interaction data generated by the agent's own actions, where the resulting future states serve as supervision without reward signals. Within this paradigm we study two strategies of using such data: (1) Implicit world modeling, which uses collected states to ground the policy in environment dynamics; and (2) Self-reflection, where the agent learns from its suboptimal actions to improve reasoning and decision-making. We evaluate across eight diverse environments and multiple model families. Our approaches consistently improve effectiveness and out-of-domain generalization, highlighting the value of early experience. Moreover, in environments with verifiable rewards, our results provide promising signals that early experience offers a strong foundation for subsequent reinforcement learning, positioning it as a practical bridge between imitation learning and fully experience-driven agents.



---


# Agent S2: A Compositional Generalist-Specialist Framework for Computer Use Agents

**arXiv ID**: 2504.00906
**arXiv URL**: https://arxiv.org/abs/2504.00906

## Abstract

Computer use agents automate digital tasks by directly interacting with graphical user interfaces (GUIs) on computers and mobile devices, offering significant potential to enhance human productivity by completing an open-ended space of user queries. However, current agents face significant challenges: imprecise grounding of GUI elements, difficulties with long-horizon task planning, and performance bottlenecks from relying on single generalist models for diverse cognitive tasks. To this end, we introduce Agent S2, a novel compositional framework that delegates cognitive responsibilities across various generalist and specialist models. We propose a novel Mixture-of-Grounding technique to achieve precise GUI localization and introduce Proactive Hierarchical Planning, dynamically refining action plans at multiple temporal scales in response to evolving observations. Evaluations demonstrate that Agent S2 establishes new state-of-the-art (SOTA) performance on three prominent computer use benchmarks. Specifically, Agent S2 achieves 18.9% and 32.7% relative improvements over leading baseline agents such as Claude Computer Use and UI-TARS on the OSWorld 15-step and 50-step evaluation. Moreover, Agent S2 generalizes effectively to other operating systems and applications, surpassing previous best methods by 52.8% on WindowsAgentArena and by 16.52% on AndroidWorld relatively. Code available at https://github.com/simular-ai/Agent-S.



---


# Agent S: An Open Agentic Framework that Uses Computers Like a Human

**arXiv ID**: 2410.08164
**arXiv URL**: https://arxiv.org/abs/2410.08164

## Abstract

We present Agent S, an open agentic framework that enables autonomous interaction with computers through a Graphical User Interface (GUI), aimed at transforming human-computer interaction by automating complex, multi-step tasks. Agent S aims to address three key challenges in automating computer tasks: acquiring domain-specific knowledge, planning over long task horizons, and handling dynamic, non-uniform interfaces. To this end, Agent S introduces experience-augmented hierarchical planning, which learns from external knowledge search and internal experience retrieval at multiple levels, facilitating efficient task planning and subtask execution. In addition, it employs an Agent-Computer Interface (ACI) to better elicit the reasoning and control capabilities of GUI agents based on Multimodal Large Language Models (MLLMs). Evaluation on the OSWorld benchmark shows that Agent S outperforms the baseline by 9.37% on success rate (an 83.6% relative improvement) and achieves a new state-of-the-art. Comprehensive analysis highlights the effectiveness of individual components and provides insights for future improvements. Furthermore, Agent S demonstrates broad generalizability to different operating systems on a newly-released WindowsAgentArena benchmark. Code available at https://github.com/simular-ai/Agent-S.



---


# Agent Workflow Memory

**arXiv ID**: 2409.07429
**arXiv URL**: https://arxiv.org/abs/2409.07429

## Abstract

Despite the potential of language model-based agents to solve real-world tasks such as web navigation, current methods still struggle with long-horizon tasks with complex action trajectories. In contrast, humans can flexibly solve complex tasks by learning reusable task workflows from past experiences and using them to guide future actions. To build agents that can similarly benefit from this process, we introduce Agent Workflow Memory (AWM), a method for inducing commonly reused routines, i.e., workflows, and selectively providing workflows to the agent to guide subsequent generations. AWM flexibly applies to both offline and online scenarios, where agents induce workflows from training examples beforehand or from test queries on the fly. We experiment on two major web navigation benchmarks -- Mind2Web and WebArena -- that collectively cover 1000+ tasks from 200+ domains across travel, shopping, and social media, among others. AWM substantially improves the baseline results by 24.6% and 51.1% relative success rate on Mind2Web and WebArena while reducing the number of steps taken to solve WebArena tasks successfully. Furthermore, online AWM robustly generalizes in cross-task, website, and domain evaluations, surpassing baselines from 8.9 to 14.0 absolute points as train-test task distribution gaps widen.



---


# Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training

**arXiv ID**: 2501.11425
**arXiv URL**: https://arxiv.org/abs/2501.11425

## Abstract

Large Language Models (LLMs) agents are increasingly pivotal for addressing complex tasks in interactive environments. Existing work mainly focuses on enhancing performance through behavior cloning from stronger experts, yet such approaches often falter in real-world applications, mainly due to the inability to recover from errors. However, step-level critique data is difficult and expensive to collect. Automating and dynamically constructing self-critique datasets is thus crucial to empowering models with intelligent agent capabilities. In this work, we propose an iterative self-training framework, Agent-R, that enables language Agent to Reflect on the fly. Unlike traditional methods that reward or penalize actions based on correctness, Agent-R leverages MCTS to construct training data that recover correct trajectories from erroneous ones. A key challenge of agent reflection lies in the necessity for timely revision rather than waiting until the end of a rollout. To address this, we introduce a model-guided critique construction mechanism: the actor model identifies the first error step (within its current capability) in a failed trajectory. Starting from it, we splice it with the adjacent correct path, which shares the same parent node in the tree. This strategy enables the model to learn reflection based on its current policy, therefore yielding better learning efficiency. To further explore the scalability of this self-improvement paradigm, we investigate iterative refinement of both error correction capabilities and dataset construction. Our findings demonstrate that Agent-R continuously improves the model's ability to recover from errors and enables timely error correction. Experiments on three interactive environments show that Agent-R effectively equips agents to correct erroneous actions while avoiding loops, achieving superior performance compared to baseline methods (+5.59%).



---


# Agent0: Unleashing Self-Evolving Agents from Zero Data via Tool-Integrated Reasoning

**arXiv ID**: 2511.16043
**arXiv URL**: https://arxiv.org/abs/2511.16043

## Abstract

Large Language Model (LLM) Agents, often trained with Reinforcement Learning (RL), are constrained by a dependency on human-curated data, limiting scalability and tethering AI to human knowledge. Existing self-evolution frameworks offer an alternative but are typically restricted by the model's inherent capabilities and single-round interactions, hindering the development of complex curricula involving tool use or dynamic reasoning. We introduce Agent0, a fully autonomous framework that evolves high-performing agents without external data through multi-step co-evolution and seamless tool integration. Agent0 establishes a symbiotic competition between two agents initialized from the same base LLM: a curriculum agent that proposes increasingly challenging frontier tasks, and an executor agent that learns to solve them. We integrate external tools to enhance the executor's problem-solving capacity; this improvement, in turn, pressures the curriculum agent to construct more complex, tool-aware tasks. Through this iterative process, Agent0 establishes a self-reinforcing cycle that continuously produces high-quality curricula. Empirically, Agent0 substantially boosts reasoning capabilities, improving the Qwen3-8B-Base model by 18% on mathematical reasoning and 24% on general reasoning benchmarks. Code is available at https://github.com/aiming-lab/Agent0.



---


# AgentEHR: Advancing Autonomous Clinical Decision-Making via Retrospective Summarization

**arXiv ID**: 2601.13918
**arXiv URL**: https://arxiv.org/abs/2601.13918

## Abstract

Large Language Models have demonstrated profound utility in the medical domain. However, their application to autonomous Electronic Health Records~(EHRs) navigation remains constrained by a reliance on curated inputs and simplified retrieval tasks. To bridge the gap between idealized experimental settings and realistic clinical environments, we present AgentEHR. This benchmark challenges agents to execute complex decision-making tasks, such as diagnosis and treatment planning, requiring long-range interactive reasoning directly within raw and high-noise databases. In tackling these tasks, we identify that existing summarization methods inevitably suffer from critical information loss and fractured reasoning continuity. To address this, we propose RetroSum, a novel framework that unifies a retrospective summarization mechanism with an evolving experience strategy. By dynamically re-evaluating interaction history, the retrospective mechanism prevents long-context information loss and ensures unbroken logical coherence. Additionally, the evolving strategy bridges the domain gap by retrieving accumulated experience from a memory bank. Extensive empirical evaluations demonstrate that RetroSum achieves performance gains of up to 29.16% over competitive baselines, while significantly decreasing total interaction errors by up to 92.3%.



---


# AgentEvolver: Towards Efficient Self-Evolving Agent System

**arXiv ID**: 2511.10395
**arXiv URL**: https://arxiv.org/abs/2511.10395

## Abstract

Autonomous agents powered by large language models (LLMs) have the potential to significantly enhance human productivity by reasoning, using tools, and executing complex tasks in diverse environments. However, current approaches to developing such agents remain costly and inefficient, as they typically require manually constructed task datasets and reinforcement learning (RL) pipelines with extensive random exploration. These limitations lead to prohibitively high data-construction costs, low exploration efficiency, and poor sample utilization. To address these challenges, we present AgentEvolver, a self-evolving agent system that leverages the semantic understanding and reasoning capabilities of LLMs to drive autonomous agent learning. AgentEvolver introduces three synergistic mechanisms: (i) self-questioning, which enables curiosity-driven task generation in novel environments, reducing dependence on handcrafted datasets; (ii) self-navigating, which improves exploration efficiency through experience reuse and hybrid policy guidance; and (iii) self-attributing, which enhances sample efficiency by assigning differentiated rewards to trajectory states and actions based on their contribution. By integrating these mechanisms into a unified framework, AgentEvolver enables scalable, cost-effective, and continual improvement of agent capabilities. Preliminary experiments indicate that AgentEvolver achieves more efficient exploration, better sample utilization, and faster adaptation compared to traditional RL-based baselines.



---


# AgentRM: Enhancing Agent Generalization with Reward Modeling

**arXiv ID**: 2502.18407
**arXiv URL**: https://arxiv.org/abs/2502.18407

## Abstract

Existing LLM-based agents have achieved strong performance on held-in tasks, but their generalizability to unseen tasks remains poor. Hence, some recent work focus on fine-tuning the policy model with more diverse tasks to improve the generalizability. In this work, we find that finetuning a reward model to guide the policy model is more robust than directly finetuning the policy model. Based on this finding, we propose AgentRM, a generalizable reward model, to guide the policy model for effective test-time search. We comprehensively investigate three approaches to construct the reward model, including explicit reward modeling, implicit reward modeling and LLM-as-a-judge. We then use AgentRM to guide the answer generation with Best-of-N sampling and step-level beam search. On four types of nine agent tasks, AgentRM enhances the base policy model by $8.8$ points on average, surpassing the top general agent by $4.0$. Moreover, it demonstrates weak-to-strong generalization, yielding greater improvement of $12.6$ on LLaMA-3-70B policy model. As for the specializability, AgentRM can also boost a finetuned policy model and outperform the top specialized agent by $11.4$ on three held-in tasks. Further analysis verifies its effectiveness in test-time scaling. Codes will be released to facilitate the research in this area.



---


# Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents

**arXiv ID**: 2601.01885
**arXiv URL**: https://arxiv.org/abs/2601.01885

## Abstract

Large language model (LLM) agents face fundamental limitations in long-horizon reasoning due to finite context windows, making effective memory management critical. Existing methods typically handle long-term memory (LTM) and short-term memory (STM) as separate components, relying on heuristics or auxiliary controllers, which limits adaptability and end-to-end optimization. In this paper, we propose Agentic Memory (AgeMem), a unified framework that integrates LTM and STM management directly into the agent's policy. AgeMem exposes memory operations as tool-based actions, enabling the LLM agent to autonomously decide what and when to store, retrieve, update, summarize, or discard information. To train such unified behaviors, we propose a three-stage progressive reinforcement learning strategy and design a step-wise GRPO to address sparse and discontinuous rewards induced by memory operations. Experiments on five long-horizon benchmarks demonstrate that AgeMem consistently outperforms strong memory-augmented baselines across multiple LLM backbones, achieving improved task performance, higher-quality long-term memory, and more efficient context usage.



---


# Agentic Proposing: Enhancing Large Language Model Reasoning via Compositional Skill Synthesis

**arXiv ID**: 2602.03279
**arXiv URL**: https://arxiv.org/abs/2602.03279

## Abstract

Advancing complex reasoning in large language models relies on high-quality, verifiable datasets, yet human annotation remains cost-prohibitive and difficult to scale. Current synthesis paradigms often face a recurring trade-off: maintaining structural validity typically restricts problem complexity, while relaxing constraints to increase difficulty frequently leads to inconsistent or unsolvable instances. To address this, we propose Agentic Proposing, a framework that models problem synthesis as a goal-driven sequential decision process where a specialized agent dynamically selects and composes modular reasoning skills. Through an iterative workflow of internal reflection and tool-use, we develop the Agentic-Proposer-4B using Multi-Granularity Policy Optimization (MGPO) to generate high-precision, verifiable training trajectories across mathematics, coding, and science. Empirical results demonstrate that downstream solvers trained on agent-synthesized data significantly outperform leading baselines and exhibit robust cross-domain generalization. Notably, a 30B solver trained on only 11,000 synthesized trajectories achieves a state-of-the-art 91.6% accuracy on AIME25, rivaling frontier-scale proprietary models such as GPT-5 and proving that a small volume of high-quality synthetic signals can effectively substitute for massive human-curated datasets.



---


# Agentic Reasoning and Tool Integration for LLMs via Reinforcement Learning

**arXiv ID**: 2505.01441
**arXiv URL**: https://arxiv.org/abs/2505.01441

## Abstract

Large language models (LLMs) have achieved remarkable progress in complex reasoning tasks, yet they remain fundamentally limited by their reliance on static internal knowledge and text-only reasoning. Real-world problem solving often demands dynamic, multi-step reasoning, adaptive decision making, and the ability to interact with external tools and environments. In this work, we introduce ARTIST (Agentic Reasoning and Tool Integration in Self-improving Transformers), a unified framework that tightly couples agentic reasoning, reinforcement learning, and tool integration for LLMs. ARTIST enables models to autonomously decide when, how, and which tools to invoke within multi-turn reasoning chains, leveraging outcome-based RL to learn robust strategies for tool use and environment interaction without requiring step-level supervision. Extensive experiments on mathematical reasoning and multi-turn function calling benchmarks show that ARTIST consistently outperforms state-of-the-art baselines, with up to 22% absolute improvement over base models and strong gains on the most challenging tasks. Detailed studies and metric analyses reveal that agentic RL training leads to deeper reasoning, more effective tool use, and higher-quality solutions. Our results establish agentic RL with tool integration as a powerful new frontier for robust, interpretable, and generalizable problem-solving in LLMs.



---


# Agentic Rubrics as Contextual Verifiers for SWE Agents

**arXiv ID**: 2601.04171
**arXiv URL**: https://arxiv.org/abs/2601.04171

## Abstract

Verification is critical for improving agents: it provides the reward signal for Reinforcement Learning and enables inference-time gains through Test-Time Scaling (TTS). Despite its importance, verification in software engineering (SWE) agent settings often relies on code execution, which can be difficult to scale due to environment setup overhead. Scalable alternatives such as patch classifiers and heuristic methods exist, but they are less grounded in codebase context and harder to interpret. To this end, we explore Agentic Rubrics: an expert agent interacts with the repository to create a context-grounded rubric checklist, and candidate patches are then scored against it without requiring test execution. On SWE-Bench Verified under parallel TTS evaluation, Agentic Rubrics achieve a score of 54.2% on Qwen3-Coder-30B-A3B and 40.6% on Qwen3-32B, with at least a +3.5 percentage-point gain over the strongest baseline in our comparison set. We further analyze rubric behavior, showing that rubric scores are consistent with ground-truth tests while also flagging issues that tests do not capture. Our ablations show that agentic context gathering is essential for producing codebase-specific, unambiguous criteria. Together, these results suggest that Agentic Rubrics provide an efficient, scalable, and granular verification signal for SWE agents.



---


# Aligning Agentic World Models via Knowledgeable Experience Learning

**arXiv ID**: 2601.13247
**arXiv URL**: https://arxiv.org/abs/2601.13247

## Abstract

Current Large Language Models (LLMs) exhibit a critical modal disconnect: they possess vast semantic knowledge but lack the procedural grounding to respect the immutable laws of the physical world. Consequently, while these agents implicitly function as world models, their simulations often suffer from physical hallucinations-generating plans that are logically sound but physically unexecutable. Existing alignment strategies predominantly rely on resource-intensive training or fine-tuning, which attempt to compress dynamic environmental rules into static model parameters. However, such parametric encapsulation is inherently rigid, struggling to adapt to the open-ended variability of physical dynamics without continuous, costly retraining. To bridge this gap, we introduce WorldMind, a framework that autonomously constructs a symbolic World Knowledge Repository by synthesizing environmental feedback. Specifically, it unifies Process Experience to enforce physical feasibility via prediction errors and Goal Experience to guide task optimality through successful trajectories. Experiments on EB-ALFRED and EB-Habitat demonstrate that WorldMind achieves superior performance compared to baselines with remarkable cross-model and cross-environment transferability.



---


# Arbor: A Framework for Reliable Navigation of Critical Conversation Flows

**arXiv ID**: 2602.14643
**arXiv URL**: https://arxiv.org/abs/2602.14643

## Abstract

Large language models struggle to maintain strict adherence to structured workflows in high-stakes domains such as healthcare triage. Monolithic approaches that encode entire decision structures within a single prompt are prone to instruction-following degradation as prompt length increases, including lost-in-the-middle effects and context window overflow. To address this gap, we present Arbor, a framework that decomposes decision tree navigation into specialized, node-level tasks. Decision trees are standardized into an edge-list representation and stored for dynamic retrieval. At runtime, a directed acyclic graph (DAG)-based orchestration mechanism iteratively retrieves only the outgoing edges of the current node, evaluates valid transitions via a dedicated LLM call, and delegates response generation to a separate inference step. The framework is agnostic to the underlying decision logic and model provider. Evaluated against single-prompt baselines across 10 foundation models using annotated turns from real clinical triage conversations. Arbor improves mean turn accuracy by 29.4 percentage points, reduces per-turn latency by 57.1%, and achieves an average 14.4x reduction in per-turn cost. These results indicate that architectural decomposition reduces dependence on intrinsic model capability, enabling smaller models to match or exceed larger models operating under single-prompt baselines.



---


# AriGraph: Learning Knowledge Graph World Models with Episodic Memory for LLM Agents

**arXiv ID**: 2407.04363
**arXiv URL**: https://arxiv.org/abs/2407.04363

## Abstract

Advancements in the capabilities of Large Language Models (LLMs) have created a promising foundation for developing autonomous agents. With the right tools, these agents could learn to solve tasks in new environments by accumulating and updating their knowledge. Current LLM-based agents process past experiences using a full history of observations, summarization, retrieval augmentation. However, these unstructured memory representations do not facilitate the reasoning and planning essential for complex decision-making. In our study, we introduce AriGraph, a novel method wherein the agent constructs and updates a memory graph that integrates semantic and episodic memories while exploring the environment. We demonstrate that our Ariadne LLM agent, consisting of the proposed memory architecture augmented with planning and decision-making, effectively handles complex tasks within interactive text game environments difficult even for human players. Results show that our approach markedly outperforms other established memory methods and strong RL baselines in a range of problems of varying complexity. Additionally, AriGraph demonstrates competitive performance compared to dedicated knowledge graph-based methods in static multi-hop question-answering.



---


# AutoAgent: Evolving Cognition and Elastic Memory Orchestration for Adaptive Agents

**arXiv ID**: 2603.09716
**arXiv URL**: https://arxiv.org/abs/2603.09716

## Abstract

Autonomous agent frameworks still struggle to reconcile long-term experiential learning with real-time, context-sensitive decision-making. In practice, this gap appears as static cognition, rigid workflow dependence, and inefficient context usage, which jointly limit adaptability in open-ended and non-stationary environments. To address these limitations, we present AutoAgent, a self-evolving multi-agent framework built on three tightly coupled components: evolving cognition, on-the-fly contextual decision-making, and elastic memory orchestration. At the core of AutoAgent, each agent maintains structured prompt-level cognition over tools, self-capabilities, peer expertise, and task knowledge. During execution, this cognition is combined with live task context to select actions from a unified space that includes tool calls, LLM-based generation, and inter-agent requests. To support efficient long-horizon reasoning, an Elastic Memory Orchestrator dynamically organizes interaction history by preserving raw records, compressing redundant trajectories, and constructing reusable episodic abstractions, thereby reducing token overhead while retaining decision-critical evidence. These components are integrated through a closed-loop cognitive evolution process that aligns intended actions with observed outcomes to continuously update cognition and expand reusable skills, without external retraining. Empirical results across retrieval-augmented reasoning, tool-augmented agent benchmarks, and embodied task environments show that AutoAgent consistently improves task success, tool-use efficiency, and collaborative robustness over static and memory-augmented baselines. Overall, AutoAgent provides a unified and practical foundation for adaptive autonomous agents that must learn from experience while making reliable context-aware decisions in dynamic environments.



---


# AutoGuide: Automated Generation and Selection of Context-Aware Guidelines for Large Language Model Agents

**arXiv ID**: 2403.08978
**arXiv URL**: https://arxiv.org/abs/2403.08978

## Abstract

Recent advances in large language models (LLMs) have empowered AI agents capable of performing various sequential decision-making tasks. However, effectively guiding LLMs to perform well in unfamiliar domains like web navigation, where they lack sufficient knowledge, has proven to be difficult with the demonstration-based in-context learning paradigm. In this paper, we introduce a novel framework, called AutoGuide, which addresses this limitation by automatically generating context-aware guidelines from offline experiences. Importantly, each context-aware guideline is expressed in concise natural language and follows a conditional structure, clearly describing the context where it is applicable. As a result, our guidelines facilitate the provision of relevant knowledge for the agent's current decision-making process, overcoming the limitations of the conventional demonstration-based learning paradigm. Our evaluation demonstrates that AutoGuide significantly outperforms competitive baselines in complex benchmark domains, including real-world web navigation.



---


# AutoManual: Constructing Instruction Manuals by LLM Agents via Interactive Environmental Learning

**arXiv ID**: 2405.16247
**arXiv URL**: https://arxiv.org/abs/2405.16247

## Abstract

Large Language Models (LLM) based agents have shown promise in autonomously completing tasks across various domains, e.g., robotics, games, and web navigation. However, these agents typically require elaborate design and expert prompts to solve tasks in specific domains, which limits their adaptability. We introduce AutoManual, a framework enabling LLM agents to autonomously build their understanding through interaction and adapt to new environments. AutoManual categorizes environmental knowledge into diverse rules and optimizes them in an online fashion by two agents: 1) The Planner codes actionable plans based on current rules for interacting with the environment. 2) The Builder updates the rules through a well-structured rule system that facilitates online rule management and essential detail retention. To mitigate hallucinations in managing rules, we introduce a *case-conditioned prompting* strategy for the Builder. Finally, the Formulator agent compiles these rules into a comprehensive manual. The self-generated manual can not only improve the adaptability but also guide the planning of smaller LLMs while being human-readable. Given only one simple demonstration, AutoManual significantly improves task success rates, achieving 97.4\% with GPT-4-turbo and 86.2\% with GPT-3.5-turbo on ALFWorld benchmark tasks. The code is available at https://github.com/minghchen/automanual.



---


# AutoSkill: Experience-Driven Lifelong Learning via Skill Self-Evolution

**arXiv ID**: 2603.01145
**arXiv URL**: https://arxiv.org/abs/2603.01145

## Abstract

In practical LLM applications, users repeatedly express stable preferences and requirements, such as reducing hallucinations, following institutional writing conventions, or avoiding overly technical wording, yet such interaction experience is seldom consolidated into reusable knowledge. Consequently, LLM agents often fail to accumulate personalized capabilities across sessions. We present AutoSkill, an experience-driven lifelong learning framework that enables LLM agents to automatically derive, maintain, and reuse skills from dialogue and interaction traces. AutoSkill abstracts skills from user experience, supports their continual self-evolution, and dynamically injects relevant skills into future requests without retraining the underlying model. Designed as a model-agnostic plugin layer, it is compatible with existing LLMs and introduces a standardized skill representation for sharing and transfer across agents, users, and tasks. In this way, AutoSkill turns ephemeral interaction experience into explicit, reusable, and composable capabilities. This paper describes the motivation, architecture, skill lifecycle, and implementation of AutoSkill, and positions it with respect to prior work on memory, retrieval, personalization, and agentic systems. AutoSkill highlights a practical and scalable path toward lifelong personalized agents and personal digital surrogates.



---


# Automated Design of Agentic Systems

**arXiv ID**: 2408.08435
**arXiv URL**: https://arxiv.org/abs/2408.08435

## Abstract

Researchers are investing substantial effort in developing powerful general-purpose agents, wherein Foundation Models are used as modules within agentic systems (e.g. Chain-of-Thought, Self-Reflection, Toolformer). However, the history of machine learning teaches us that hand-designed solutions are eventually replaced by learned solutions. We describe a newly forming research area, Automated Design of Agentic Systems (ADAS), which aims to automatically create powerful agentic system designs, including inventing novel building blocks and/or combining them in new ways. We further demonstrate that there is an unexplored yet promising approach within ADAS where agents can be defined in code and new agents can be automatically discovered by a meta agent programming ever better ones in code. Given that programming languages are Turing Complete, this approach theoretically enables the learning of any possible agentic system: including novel prompts, tool use, workflows, and combinations thereof. We present a simple yet effective algorithm named Meta Agent Search to demonstrate this idea, where a meta agent iteratively programs interesting new agents based on an ever-growing archive of previous discoveries. Through extensive experiments across multiple domains including coding, science, and math, we show that our algorithm can progressively invent agents with novel designs that greatly outperform state-of-the-art hand-designed agents. Importantly, we consistently observe the surprising result that agents invented by Meta Agent Search maintain superior performance even when transferred across domains and models, demonstrating their robustness and generality. Provided we develop it safely, our work illustrates the potential of an exciting new research direction toward automatically designing ever-more powerful agentic systems to benefit humanity.



---


# A²Flow: Automating Agentic Workflow Generation via Self-Adaptive Abstraction Operators

**arXiv ID**: 2511.20693
**arXiv URL**: https://arxiv.org/abs/2511.20693

## Abstract

Large language models (LLMs) have shown strong potential in automating the design of agentic workflows. However, existing methods still rely heavily on manually predefined operators, limiting generalization and scalability. To address this issue, we propose $A^2Flow$, a fully automated framework for agentic workflow generation based on self-adaptive abstraction operators. $A^2Flow$ employs a three-stage operator extraction process: 1) Case-based Initial Operator Generation: leveraging expert demonstrations and LLM reasoning to generate case-specific operators; 2) Operator Clustering and Preliminary Abstraction: grouping similar operators across tasks to form preliminary abstractions; and 3) Deep Extraction for Abstract Execution Operators: applying long chain-of-thought prompting and multi-path reasoning to derive compact and generalizable execution operators. These operators serve as reusable building blocks for workflow construction without manual predefinition. Furthermore, we enhance node-level workflow search with an operator memory mechanism, which retains historical outputs to enrich context and improve decision-making. Experiments on general and embodied benchmarks show that $A^2Flow$ achieves a 2.4\% and 19.3\% average performance improvement and reduces resource usage by 37\% over state-of-the-art baselines. Homepage:https://github.com/pandawei-ele/A2FLOW



---


# Becoming Experienced Judges: Selective Test-Time Learning for Evaluators

**arXiv ID**: 2512.06751
**arXiv URL**: https://arxiv.org/abs/2512.06751

## Abstract

Automatic evaluation with large language models, commonly known as LLM-as-a-judge, is now standard across reasoning and alignment tasks. Despite evaluating many samples in deployment, these evaluators typically (i) treat each case independently, missing the opportunity to accumulate experience, and (ii) rely on a single fixed prompt for all cases, neglecting the need for sample-specific evaluation criteria. We introduce Learning While Evaluating (LWE), a framework that allows evaluators to improve sequentially at inference time without requiring training or validation sets. LWE maintains an evolving meta-prompt that (i) produces sample-specific evaluation instructions and (ii) refines itself through self-generated feedback. Furthermore, we propose Selective LWE, which updates the meta-prompt only on self-inconsistent cases, focusing computation where it matters most. This selective approach retains the benefits of sequential learning while being far more cost-effective. Across two pairwise comparison benchmarks, Selective LWE outperforms strong baselines, empirically demonstrating that evaluators can improve during sequential testing with a simple selective update, learning most from the cases they struggle with.



---


# Beyond Human Data: Scaling Self-Training for Problem-Solving with Language Models

**arXiv ID**: 2312.06585
**arXiv URL**: https://arxiv.org/abs/2312.06585

## Abstract

Fine-tuning language models~(LMs) on human-generated data remains a prevalent practice. However, the performance of such models is often limited by the quantity and diversity of high-quality human data. In this paper, we explore whether we can go beyond human data on tasks where we have access to scalar feedback, for example, on math problems where one can verify correctness. To do so, we investigate a simple self-training method based on expectation-maximization, which we call ReST$^{EM}$, where we (1) generate samples from the model and filter them using binary feedback, (2) fine-tune the model on these samples, and (3) repeat this process a few times. Testing on advanced MATH reasoning and APPS coding benchmarks using PaLM-2 models, we find that ReST$^{EM}$ scales favorably with model size and significantly surpasses fine-tuning only on human data. Overall, our findings suggest self-training with feedback can substantially reduce dependence on human-generated data.



---


# Beyond Policy Optimization: A Data Curation Flywheel for Sparse-Reward Long-Horizon Planning

**arXiv ID**: 2508.03018
**arXiv URL**: https://arxiv.org/abs/2508.03018

## Abstract

Large Language Reasoning Models have demonstrated remarkable success on static tasks, yet their application to multi-round agentic planning in interactive environments faces two fundamental challenges. First, the intractable credit assignment problem renders conventional reinforcement learning ineffective in sparse-reward settings. Second, the computational overhead of verbose, step-by-step reasoning histories is prohibitive. To address these challenges, we propose BPO, a three-stage framework (bootstrapping, extrapolation, and refinement) that establishes a self-improving data flywheel to develop robust reasoning models for long-horizon, sparse-reward environments. Our framework first bootstraps efficient reasoning using the proposed planning quaternions with long-short chain-of-thought fusion. It then extrapolates to out-of-distribution tasks through complexity-stratified curriculum learning. Finally, the model iteratively refines itself by learning exclusively on experiences selected via reward-gated rejection sampling. Experiments on ALFWorld, ScienceWorld, and WebShop demonstrate that our approach achieves state-of-the-art with significant token efficiency, providing a new recipe for reasoning models in agentic planning.



---


# BugPilot: Complex Bug Generation for Efficient Learning of SWE Skills

**arXiv ID**: 2510.19898
**arXiv URL**: https://arxiv.org/abs/2510.19898

## Abstract

High quality bugs are key to training the next generation of language model based software engineering (SWE) agents. We introduce a novel method for synthetic generation of difficult and diverse bugs. Our method instructs SWE Agents to introduce a feature into the codebase whereby they may unintentionally break tests, resulting in bugs. Prior approaches often induce an out-of-distribution effect by generating bugs intentionally (e.g. by introducing local perturbation to existing code), which does not reflect realistic development processes. We perform qualitative analysis to demonstrate that our approach for generating bugs more closely reflects the patterns found in human-authored edits. Through extensive experiments, we demonstrate that our bugs provide more efficient training data for supervised fine-tuning, outperforming other bug datasets by 2% with half the training data (1.2k vs. 3k bugs). We train on our newly generated bugs in addition to existing bug datasets to get FrogBoss a state-of-the-art 32B parameter model on SWE-bench Verified with a pass@1 of 54.6% and FrogMini a state-of-the-art 14B model on SWE-bench Verified with a pass@1 of 45.3% on SWE-bench Verified averaged over three seeds.



---


# CLaRa: Bridging Retrieval and Generation with Continuous Latent Reasoning

**arXiv ID**: 2511.18659
**arXiv URL**: https://arxiv.org/abs/2511.18659

## Abstract

Retrieval-augmented generation (RAG) enhances large language models (LLMs) with external knowledge but still suffers from long contexts and disjoint retrieval-generation optimization. In this work, we propose CLaRa (Continuous Latent Reasoning), a unified framework that performs embedding-based compression and joint optimization in a shared continuous space. To obtain semantically rich and retrievable compressed vectors, thereby reducing the document length fed into the generator, we introduce SCP, a key-preserving data synthesis framework based on question answering and paraphrase supervision. CLaRa then trains the reranker and generator end-to-end via a single language modeling loss, with gradients flowing through both modules using a differentiable top-k estimator. Theoretically, this unified optimization aligns retrieval relevance with answer quality. Experiments across multiple QA benchmarks show that CLaRa achieves state-of-the-art compression and reranking performance, even at a text compression rate of 16, outperforming text-based fine-tuned baselines.



---


# CoEvoSkills: Self-Evolving Agent Skills via Co-Evolutionary Verification

**arXiv ID**: 2604.01687
**arXiv URL**: https://arxiv.org/abs/2604.01687

## Abstract

Anthropic proposes the concept of skills for LLM agents to tackle multi-step professional tasks that simple tool invocations cannot address. A tool is a single, self-contained function, whereas a skill is a structured bundle of interdependent multi-file artifacts. Currently, skill generation is not only label-intensive due to manual authoring, but also may suffer from human--machine cognitive misalignment, which can lead to degraded agent performance, as evidenced by evaluations on SkillsBench. Therefore, we aim to enable agents to autonomously generate skills. However, existing self-evolving methods designed for tools cannot be directly applied to skills due to their increased complexity. To address these issues, we propose CoEvoSkills, a self-evolving skills framework that enables agents to autonomously construct complex, multi-file skill packages. Specifically, CoEvoSkills couples a Skill Generator that iteratively refines skills with a Surrogate Verifier that co-evolves to provide informative and actionable feedback without access to ground-truth test content. On SkillsBench, CoEvoSkills achieves the highest pass rate among five baselines on both Claude Code and Codex, and also exhibits strong generalization capabilities to six additional LLMs.



---


# Code as Policies: Language Model Programs for Embodied Control

**arXiv ID**: 2209.07753
**arXiv URL**: https://arxiv.org/abs/2209.07753

## Abstract

Large language models (LLMs) trained on code completion have been shown to be capable of synthesizing simple Python programs from docstrings [1]. We find that these code-writing LLMs can be re-purposed to write robot policy code, given natural language commands. Specifically, policy code can express functions or feedback loops that process perception outputs (e.g.,from object detectors [2], [3]) and parameterize control primitive APIs. When provided as input several example language commands (formatted as comments) followed by corresponding policy code (via few-shot prompting), LLMs can take in new commands and autonomously re-compose API calls to generate new policy code respectively. By chaining classic logic structures and referencing third-party libraries (e.g., NumPy, Shapely) to perform arithmetic, LLMs used in this way can write robot policies that (i) exhibit spatial-geometric reasoning, (ii) generalize to new instructions, and (iii) prescribe precise values (e.g., velocities) to ambiguous descriptions ("faster") depending on context (i.e., behavioral commonsense). This paper presents code as policies: a robot-centric formulation of language model generated programs (LMPs) that can represent reactive policies (e.g., impedance controllers), as well as waypoint-based policies (vision-based pick and place, trajectory-based control), demonstrated across multiple real robot platforms. Central to our approach is prompting hierarchical code-gen (recursively defining undefined functions), which can write more complex code and also improves state-of-the-art to solve 39.8% of problems on the HumanEval [1] benchmark. Code and videos are available at https://code-as-policies.github.io



---


# Compositional Semantic Parsing on Semi-Structured Tables

**arXiv ID**: 1508.00305
**arXiv URL**: https://arxiv.org/abs/1508.00305

## Abstract

Two important aspects of semantic parsing for question answering are the breadth of the knowledge source and the depth of logical compositionality. While existing work trades off one aspect for another, this paper simultaneously makes progress on both fronts through a new task: answering complex questions on semi-structured tables using question-answer pairs as supervision. The central challenge arises from two compounding factors: the broader domain results in an open-ended set of relations, and the deeper compositionality results in a combinatorial explosion in the space of logical forms. We propose a logical-form driven parsing algorithm guided by strong typing constraints and show that it obtains significant improvements over natural baselines. For evaluation, we created a new dataset of 22,033 complex questions on Wikipedia tables, which is made publicly available.



---


# Contextual Experience Replay for Self-Improvement of Language Agents

**arXiv ID**: 2506.06698
**arXiv URL**: https://arxiv.org/abs/2506.06698

## Abstract

Large language model (LLM) agents have been applied to sequential decision-making tasks such as web navigation, but without any environment-specific experiences, they often fail in these complex tasks. Moreover, current LLM agents are not designed to continually learn from past experiences during inference time, which could be crucial for them to gain these environment-specific experiences. To address this, we propose Contextual Experience Replay (CER), a training-free framework to enable efficient self-improvement for language agents in their context window. Specifically, CER accumulates and synthesizes past experiences into a dynamic memory buffer. These experiences encompass environment dynamics and common decision-making patterns, allowing the agents to retrieve and augment themselves with relevant knowledge in new tasks, enhancing their adaptability in complex environments. We evaluate CER on the challenging WebArena and VisualWebArena benchmarks. On VisualWebArena, CER achieves a competitive performance of 31.9%. On WebArena, CER also gets a competitive average success rate of 36.7%, relatively improving the success rate of the GPT-4o agent baseline by 51.0%. We also conduct a comprehensive analysis on it to prove its efficiency, validity and understand it better.



---


# CraniMem: Cranial Inspired Gated and Bounded Memory for Agentic Systems

**arXiv ID**: 2603.15642
**arXiv URL**: https://arxiv.org/abs/2603.15642

## Abstract

Large language model (LLM) agents are increasingly deployed in long running workflows, where they must preserve user and task state across many turns. Many existing agent memory systems behave like external databases with ad hoc read/write rules, which can yield unstable retention, limited consolidation, and vulnerability to distractor content. We present CraniMem, a neurocognitively motivated, gated and bounded multi-stage memory design for agentic systems. CraniMem couples goal conditioned gating and utility tagging with a bounded episodic buffer for near term continuity and a structured long-term knowledge graph for durable semantic recall. A scheduled consolidation loop replays high utility traces into the graph while pruning low utility items, keeping memory growth in check and reducing interference. On long horizon benchmarks evaluated under both clean inputs and injected noise, CraniMem is more robust than a Vanilla RAG and Mem0 baseline and exhibits smaller performance drops under distraction. Our code is available at https://github.com/PearlMody05/Cranimem and the accompanying PyPI package at https://pypi.org/project/cranimem.



---


# DeepAnalyze: Agentic Large Language Models for Autonomous Data Science

**arXiv ID**: 2510.16872
**arXiv URL**: https://arxiv.org/abs/2510.16872

## Abstract

Autonomous data science, from raw data sources to analyst-grade deep research reports, has been a long-standing challenge, and is now becoming feasible with the emergence of powerful large language models (LLMs). Recent workflow-based data agents have shown promising results on specific data tasks but remain fundamentally limited in achieving fully autonomous data science due to their reliance on predefined workflows. In this paper, we introduce DeepAnalyze-8B, the first agentic LLM designed for autonomous data science, capable of automatically completing the end-toend pipeline from data sources to analyst-grade deep research reports. To tackle high-complexity data science tasks, we propose a curriculum-based agentic training paradigm that emulates the learning trajectory of human data scientists, enabling LLMs to progressively acquire and integrate multiple capabilities in real-world environments. We also introduce a data-grounded trajectory synthesis framework that constructs high-quality training data. Through agentic training, DeepAnalyze learns to perform a broad spectrum of data tasks, ranging from data question answering and specialized analytical tasks to open-ended data research. Experiments demonstrate that, with only 8B parameters, DeepAnalyze outperforms previous workflow-based agents built on most advanced proprietary LLMs. The model, code, and training data of DeepAnalyze are open-sourced, paving the way toward autonomous data science.



---


# DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

**arXiv ID**: 2501.12948
**arXiv URL**: https://arxiv.org/abs/2501.12948

## Abstract

General reasoning represents a long-standing and formidable challenge in artificial intelligence. Recent breakthroughs, exemplified by large language models (LLMs) and chain-of-thought prompting, have achieved considerable success on foundational reasoning tasks. However, this success is heavily contingent upon extensive human-annotated demonstrations, and models' capabilities are still insufficient for more complex problems. Here we show that the reasoning abilities of LLMs can be incentivized through pure reinforcement learning (RL), obviating the need for human-labeled reasoning trajectories. The proposed RL framework facilitates the emergent development of advanced reasoning patterns, such as self-reflection, verification, and dynamic strategy adaptation. Consequently, the trained model achieves superior performance on verifiable tasks such as mathematics, coding competitions, and STEM fields, surpassing its counterparts trained via conventional supervised learning on human demonstrations. Moreover, the emergent reasoning patterns exhibited by these large-scale models can be systematically harnessed to guide and enhance the reasoning capabilities of smaller models.



---


# Distilling LLM Agent into Small Models with Retrieval and Code Tools

**arXiv ID**: 2505.17612
**arXiv URL**: https://arxiv.org/abs/2505.17612

## Abstract

Large language models (LLMs) excel at complex reasoning tasks but remain computationally expensive, limiting their practical deployment. To address this, recent works have focused on distilling reasoning capabilities into smaller language models (sLMs) using chain-of-thought (CoT) traces from teacher LLMs. However, this approach struggles in scenarios requiring rare factual knowledge or precise computation, where sLMs often hallucinate due to limited capability. In this work, we propose Agent Distillation, a framework for transferring not only reasoning capability but full task-solving behavior from LLM-based agents into sLMs with retrieval and code tools. We improve agent distillation along two complementary axes: (1) we introduce a prompting method called first-thought prefix to enhance the quality of teacher-generated trajectories; and (2) we propose a self-consistent action generation for improving test-time robustness of small agents. We evaluate our method on eight reasoning tasks across factual and mathematical domains, covering both in-domain and out-of-domain generalization. Our results show that sLMs as small as 0.5B, 1.5B, 3B parameters can achieve performance competitive with next-tier larger 1.5B, 3B, 7B models fine-tuned using CoT distillation, demonstrating the potential of agent distillation for building practical, tool-using small agents. Our code is available at https://github.com/Nardien/agent-distillation.



---


# Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory

**arXiv ID**: 2504.07952
**arXiv URL**: https://arxiv.org/abs/2504.07952

## Abstract

Despite their impressive performance on complex tasks, current language models (LMs) typically operate in a vacuum: Each input query is processed separately, without retaining insights from previous attempts. Here, we present Dynamic Cheatsheet (DC), a lightweight framework that endows a black-box LM with a persistent, evolving memory. Rather than repeatedly re-discovering or re-committing the same solutions and mistakes, DC enables models to store and reuse accumulated strategies, code snippets, and general problem-solving insights at inference time. This test-time learning enhances performance substantially across a range of tasks without needing explicit ground-truth labels or human feedback. Leveraging DC, Claude 3.5 Sonnet's accuracy more than doubled on AIME math exams once it began retaining algebraic insights across questions. Similarly, GPT-4o's success rate on Game of 24 increased from 10% to 99% after the model discovered and reused a Python-based solution. In tasks prone to arithmetic mistakes, such as balancing equations, DC enabled GPT-4o and Claude to reach near-perfect accuracy by recalling previously validated code, whereas their baselines stagnated around 50%. Beyond arithmetic challenges, DC yields notable accuracy gains on knowledge-demanding tasks. Claude achieved a 9% improvement in GPQA-Diamond and an 8% boost on MMLU-Pro problems. Crucially, DC's memory is self-curated, focusing on concise, transferable snippets rather than entire transcript. Unlike finetuning or static retrieval methods, DC adapts LMs' problem-solving skills on the fly, without modifying their underlying parameters. Overall, our findings present DC as a promising approach for augmenting LMs with persistent memory, bridging the divide between isolated inference events and the cumulative, experience-driven learning characteristic of human cognition.



---


# Dyve: Thinking Fast and Slow for Dynamic Process Verification

**arXiv ID**: 2502.11157
**arXiv URL**: https://arxiv.org/abs/2502.11157

## Abstract

We present Dyve, a dynamic process verifier that enhances reasoning error detection in large language models by integrating fast and slow thinking, inspired by Kahneman's Systems Theory. Dyve adaptively applies immediate token-level confirmation System 1 for straightforward steps and comprehensive analysis System 2 for complex ones. Leveraging a novel step-wise consensus-filtered process supervision technique, combining Monte Carlo estimation with LLM based evaluation, Dyve curates high-quality supervision signals from noisy data. Experimental results on ProcessBench and the MATH dataset confirm that Dyve significantly outperforms existing process-based verifiers and boosts performance in Best-of-N settings.



---


# E2CL: Exploration-based Error Correction Learning for Embodied Agents

**arXiv ID**: 2409.03256
**arXiv URL**: https://arxiv.org/abs/2409.03256

## Abstract

Language models are exhibiting increasing capability in knowledge utilization and reasoning. However, when applied as agents in embodied environments, they often suffer from misalignment between their intrinsic knowledge and environmental knowledge, leading to infeasible actions. Traditional environment alignment methods, such as supervised learning on expert trajectories and reinforcement learning, encounter limitations in covering environmental knowledge and achieving efficient convergence, respectively. Inspired by human learning, we propose Exploration-based Error Correction Learning (E2CL), a novel framework that leverages exploration-induced errors and environmental feedback to enhance environment alignment for embodied agents. E2CL incorporates teacher-guided and teacher-free explorations to gather environmental feedback and correct erroneous actions. The agent learns to provide feedback and self-correct, thereby enhancing its adaptability to target environments. Extensive experiments in the VirtualHome environment demonstrate that E2CL-trained agents outperform those trained by baseline methods and exhibit superior self-correction capabilities.



---


# ELITE: Experiential Learning and Intent-Aware Transfer for Self-improving Embodied Agents

**arXiv ID**: 2603.24018
**arXiv URL**: https://arxiv.org/abs/2603.24018

## Abstract

Vision-language models (VLMs) have shown remarkable general capabilities, yet embodied agents built on them fail at complex tasks, often skipping critical steps, proposing invalid actions, and repeating mistakes. These failures arise from a fundamental gap between the static training data of VLMs and the physical interaction for embodied tasks. VLMs can learn rich semantic knowledge from static data but lack the ability to interact with the world. To address this issue, we introduce ELITE, an embodied agent framework with {E}xperiential {L}earning and {I}ntent-aware {T}ransfer that enables agents to continuously learn from their own environment interaction experiences, and transfer acquired knowledge to procedurally similar tasks. ELITE operates through two synergistic mechanisms, \textit{i.e.,} self-reflective knowledge construction and intent-aware retrieval. Specifically, self-reflective knowledge construction extracts reusable strategies from execution trajectories and maintains an evolving strategy pool through structured refinement operations. Then, intent-aware retrieval identifies relevant strategies from the pool and applies them to current tasks. Experiments on the EB-ALFRED and EB-Habitat benchmarks show that ELITE achieves 9\% and 5\% performance improvement over base VLMs in the online setting without any supervision. In the supervised setting, ELITE generalizes effectively to unseen task categories, achieving better performance compared to state-of-the-art training-based methods. These results demonstrate the effectiveness of ELITE for bridging the gap between semantic understanding and reliable action execution.



---


# EVOLVE-VLA: Test-Time Training from Environment Feedback for Vision-Language-Action Models

**arXiv ID**: 2512.14666
**arXiv URL**: https://arxiv.org/abs/2512.14666

## Abstract

Achieving truly adaptive embodied intelligence requires agents that learn not just by imitating static demonstrations, but by continuously improving through environmental interaction, which is akin to how humans master skills through practice. Vision-Language-Action (VLA) models have advanced robotic manipulation by leveraging large language models, yet remain fundamentally limited by Supervised Finetuning (SFT): requiring hundreds of demonstrations per task, rigidly memorizing trajectories, and failing to adapt when deployment conditions deviate from training. We introduce EVOLVE-VLA, a test-time training framework enabling VLAs to continuously adapt through environment interaction with minimal or zero task-specific demonstrations. The key technical challenge is replacing oracle reward signals (unavailable at test time) with autonomous feedback. We address this through a learned progress estimator providing dense feedback, and critically, we design our framework to ``tame'' this inherently noisy signal via two mechanisms: (1) an accumulative progress estimation mechanism smoothing noisy point-wise estimates, and (2) a progressive horizon extension strategy enabling gradual policy evolution. EVOLVE-VLA achieves substantial gains: +8.6\% on long-horizon tasks, +22.0\% in 1-shot learning, and enables cross-task generalization -- achieving 20.8\% success on unseen tasks without task-specific demonstrations training (vs. 0\% for pure SFT). Qualitative analysis reveals emergent capabilities absent in demonstrations, including error recovery and novel strategies. This work represents a critical step toward VLAs that truly learn and adapt, moving beyond static imitation toward continuous self-improvements.



---


# Entropy-Based Adaptive Weighting for Self-Training

**arXiv ID**: 2503.23913
**arXiv URL**: https://arxiv.org/abs/2503.23913

## Abstract

The mathematical problem-solving capabilities of large language models have become a focal point of research, with growing interests in leveraging self-generated reasoning paths as a promising way to refine and enhance these models. These paths capture step-by-step logical processes while requiring only the correct answer for supervision. The self-training method has been shown to be effective in reasoning tasks while eliminating the need for external models and manual annotations. However, optimizing the use of self-generated data for model training remains an open challenge. In this work, we propose Entropy-Based Adaptive Weighting for Self-Training (EAST), an adaptive weighting strategy designed to prioritize uncertain data during self-training. Specifically, EAST employs a mapping function with a tunable parameter that controls the sharpness of the weighting, assigning higher weights to data where the model exhibits greater uncertainty. This approach guides the model to focus on more informative and challenging examples, thereby enhancing its reasoning ability. We evaluate our approach on GSM8K and MATH benchmarks. Empirical results show that, while the vanilla method yields virtually no improvement (0%) on MATH, EAST achieves around a 1% gain over backbone model. On GSM8K, EAST attains a further 1-2% performance boost compared to the vanilla method.



---


# Entropy-Regularized Process Reward Model

**arXiv ID**: 2412.11006
**arXiv URL**: https://arxiv.org/abs/2412.11006

## Abstract

Large language models (LLMs) have shown promise in performing complex multi-step reasoning, yet they continue to struggle with mathematical reasoning, often making systematic errors. A promising solution is reinforcement learning (RL) guided by reward models, particularly those focusing on process rewards, which score each intermediate step rather than solely evaluating the final outcome. This approach is more effective at guiding policy models towards correct reasoning trajectories. In this work, we propose an entropy-regularized process reward model (ER-PRM) that integrates KL-regularized Markov Decision Processes (MDP) to balance policy optimization with the need to prevent the policy from shifting too far from its initial distribution. We derive a novel reward construction method based on the theoretical results. Our theoretical analysis shows that we could derive the optimal reward model from the initial policy sampling. Our empirical experiments on the MATH and GSM8K benchmarks demonstrate that ER-PRM consistently outperforms existing process reward models, achieving 1% improvement on GSM8K and 2-3% improvement on MATH under best-of-N evaluation, and more than 1% improvement under RLHF. These results highlight the efficacy of entropy-regularization in enhancing LLMs' reasoning capabilities.



---


# Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory

**arXiv ID**: 2511.20857
**arXiv URL**: https://arxiv.org/abs/2511.20857

## Abstract

Statefulness is essential for large language model (LLM) agents to perform long-term planning and problem-solving. This makes memory a critical component, yet its management and evolution remain largely underexplored. Existing evaluations mostly focus on static conversational settings, where memory is passively retrieved from dialogue to answer queries, overlooking the dynamic ability to accumulate and reuse experience across evolving task streams. In real-world environments such as interactive problem assistants or embodied agents, LLMs are required to handle continuous task streams, yet often fail to learn from accumulated interactions, losing valuable contextual insights, a limitation that calls for test-time evolution, where LLMs retrieve, integrate, and update memory continuously during deployment. To bridge this gap, we introduce Evo-Memory, a comprehensive streaming benchmark and framework for evaluating self-evolving memory in LLM agents. Evo-Memory structures datasets into sequential task streams, requiring LLMs to search, adapt, and evolve memory after each interaction. We unify and implement over ten representative memory modules and evaluate them across 10 diverse multi-turn goal-oriented and single-turn reasoning and QA datasets. To better benchmark experience reuse, we provide a baseline method, ExpRAG, for retrieving and utilizing prior experience, and further propose ReMem, an action-think-memory refine pipeline that tightly integrates reasoning, task actions, and memory updates to achieve continual improvement.



---


# EvoAgentX: An Automated Framework for Evolving Agentic Workflows

**arXiv ID**: 2507.03616
**arXiv URL**: https://arxiv.org/abs/2507.03616

## Abstract

Multi-agent systems (MAS) have emerged as a powerful paradigm for orchestrating large language models (LLMs) and specialized tools to collaboratively address complex tasks. However, existing MAS frameworks often require manual workflow configuration and lack native support for dynamic evolution and performance optimization. In addition, many MAS optimization algorithms are not integrated into a unified framework. In this paper, we present EvoAgentX, an open-source platform that automates the generation, execution, and evolutionary optimization of multi-agent workflows. EvoAgentX employs a modular architecture consisting of five core layers: the basic components, agent, workflow, evolving, and evaluation layers. Specifically, within the evolving layer, EvoAgentX integrates three MAS optimization algorithms, TextGrad, AFlow, and MIPRO, to iteratively refine agent prompts, tool configurations, and workflow topologies. We evaluate EvoAgentX on HotPotQA, MBPP, and MATH for multi-hop reasoning, code generation, and mathematical problem solving, respectively, and further assess it on real-world tasks using GAIA. Experimental results show that EvoAgentX consistently achieves significant performance improvements, including a 7.44% increase in HotPotQA F1, a 10.00% improvement in MBPP pass@1, a 10.00% gain in MATH solve accuracy, and an overall accuracy improvement of up to 20.00% on GAIA. The source code is available at: https://github.com/EvoAgentX/EvoAgentX



---


# EvoCUA: Evolving Computer Use Agents via Learning from Scalable Synthetic Experience

**arXiv ID**: 2601.15876
**arXiv URL**: https://arxiv.org/abs/2601.15876

## Abstract

The development of native computer-use agents (CUA) represents a significant leap in multimodal AI. However, their potential is currently bottlenecked by the constraints of static data scaling. Existing paradigms relying primarily on passive imitation of static datasets struggle to capture the intricate causal dynamics inherent in long-horizon computer tasks. In this work, we introduce EvoCUA, a native computer use agentic model. Unlike static imitation, EvoCUA integrates data generation and policy optimization into a self-sustaining evolutionary cycle. To mitigate data scarcity, we develop a verifiable synthesis engine that autonomously generates diverse tasks coupled with executable validators. To enable large-scale experience acquisition, we design a scalable infrastructure orchestrating tens of thousands of asynchronous sandbox rollouts. Building on these massive trajectories, we propose an iterative evolving learning strategy to efficiently internalize this experience. This mechanism dynamically regulates policy updates by identifying capability boundaries -- reinforcing successful routines while transforming failure trajectories into rich supervision through error analysis and self-correction. Empirical evaluations on the OSWorld benchmark demonstrate that EvoCUA achieves a success rate of 56.7%, establishing a new open-source state-of-the-art. Notably, EvoCUA significantly outperforms the previous best open-source model, OpenCUA-72B (45.0%), and surpasses leading closed-weights models such as UI-TARS-2 (53.1%). Crucially, our results underscore the generalizability of this approach: the evolving paradigm driven by learning from experience yields consistent performance gains across foundation models of varying scales, establishing a robust and scalable path for advancing native agent capabilities.



---


# EvoSkill: Automated Skill Discovery for Multi-Agent Systems

**arXiv ID**: 2603.02766
**arXiv URL**: https://arxiv.org/abs/2603.02766

## Abstract

Coding agents are increasingly used as general-purpose problem solvers, but their flexibility does not by itself confer the domain expertise needed for specialized tasks. Recent work addresses this through \textit{agent skills}: reusable workflows, and code, that augment agents with domain-specific capabilities. Most skills today are hand-crafted, and existing evolutionary approaches optimize low-level artifacts (e.g. prompts \& code) that are tightly coupled to specific models and tasks. We introduce \textbf{EvoSkill}, a self-evolving framework that automatically discovers and refines agent skills through iterative failure analysis. EvoSkill analyzes execution failures, proposes new skills or edits to existing ones, and materializes them into structured, reusable skill folders. A Pareto frontier of agent programs governs selection, retaining only skills that improve held-out validation performance while the underlying model remains frozen. We evaluate EvoSkill on two benchmarks: OfficeQA, a grounded reasoning benchmark over U.S.\ Treasury data, where it improves exact-match accuracy by \textbf{7.3\%} (60.6\% $\to$ 67.9\%); and SealQA, a search-augmented QA benchmark with noisy retrieval, where it yields a \textbf{12.1\%} gain (26.6\% $\to$ 38.7\%). We also investigate the zero-shot transfer capabilties of skills evolved on one task to the other; in particular: skills evolved from SealQA transfers zero-shot to BrowseComp, improving accuracy by \textbf{5.3\%} without modification demonstrating that skill-level optimization produces transferable capabilities beyond the training task.



---


# EvoTool: Self-Evolving Tool-Use Policy Optimization in LLM Agents via Blame-Aware Mutation and Diversity-Aware Selection

**arXiv ID**: 2603.04900
**arXiv URL**: https://arxiv.org/abs/2603.04900

## Abstract

LLM-based agents depend on effective tool-use policies to solve complex tasks, yet optimizing these policies remains challenging due to delayed supervision and the difficulty of credit assignment in long-horizon trajectories. Existing optimization approaches tend to be either monolithic, which are prone to entangling behaviors, or single-aspect, which ignore cross-module error propagation. To address these limitations, we propose EvoTool, a self-evolving framework that optimizes a modular tool-use policy via a gradient-free evolutionary paradigm. EvoTool decomposes agent's tool-use policy into four modules, including Planner, Selector, Caller, and Synthesizer, and iteratively improves them in a self-improving loop through three novel mechanisms. Trajectory-Grounded Blame Attribution uses diagnostic traces to localize failures to a specific module. Feedback-Guided Targeted Mutation then edits only that module via natural-language critique. Diversity-Aware Population Selection preserves complementary candidates to ensure solution diversity. Across four benchmarks, EvoTool outperforms strong baselines by over 5 points on both GPT-4.1 and Qwen3-8B, while achieving superior efficiency and transferability. The code will be released once paper is accepted.



---


# EvolveR: Self-Evolving LLM Agents through an Experience-Driven Lifecycle

**arXiv ID**: 2510.16079
**arXiv URL**: https://arxiv.org/abs/2510.16079

## Abstract

Current Large Language Model (LLM) agents show strong performance in tool use, but lack the crucial capability to systematically learn from their own experiences. While existing frameworks mainly focus on mitigating external knowledge gaps, they fail to address a more fundamental limitation: the inability to iteratively refine problem-solving strategies. In this work, we introduce EvolveR, a framework designed to enable agent to self-improve through a complete, closed-loop experience lifecycle. This lifecycle comprises two key stages: (1) Offline Self-Distillation, where the agent's interaction trajectories are synthesized into a structured repository of abstract, reusable strategic principles; (2) Online Interaction, where the agent interacts with tasks and actively retrieves distilled principles to guide its decision-making, accumulating a diverse set of behavioral trajectories. This loop employs a policy reinforcement mechanism to iteratively update the agent based on its performance. We demonstrate the effectiveness of EvolveR on complex multi-hop question-answering benchmarks, where it achieves superior performance over strong agentic baselines. Our work presents a comprehensive blueprint for agents that learn not only from external data but also from the consequences of their own actions, paving the way for more autonomous and continuously improving systems. Code is available at https://github.com/Edaizi/EvolveR.



---


# ExpeL: LLM Agents Are Experiential Learners

**arXiv ID**: 2308.10144
**arXiv URL**: https://arxiv.org/abs/2308.10144

## Abstract

The recent surge in research interest in applying large language models (LLMs) to decision-making tasks has flourished by leveraging the extensive world knowledge embedded in LLMs. While there is a growing demand to tailor LLMs for custom decision-making tasks, finetuning them for specific tasks is resource-intensive and may diminish the model's generalization capabilities. Moreover, state-of-the-art language models like GPT-4 and Claude are primarily accessible through API calls, with their parametric weights remaining proprietary and unavailable to the public. This scenario emphasizes the growing need for new methodologies that allow learning from agent experiences without requiring parametric updates. To address these problems, we introduce the Experiential Learning (ExpeL) agent. Our agent autonomously gathers experiences and extracts knowledge using natural language from a collection of training tasks. At inference, the agent recalls its extracted insights and past experiences to make informed decisions. Our empirical results highlight the robust learning efficacy of the ExpeL agent, indicating a consistent enhancement in its performance as it accumulates experiences. We further explore the emerging capabilities and transfer learning potential of the ExpeL agent through qualitative observations and additional experiments.



---


# Experiential Reflective Learning for Self-Improving LLM Agents

**arXiv ID**: 2603.24639
**arXiv URL**: https://arxiv.org/abs/2603.24639

## Abstract

Recent advances in large language models (LLMs) have enabled the development of autonomous agents capable of complex reasoning and multi-step problem solving. However, these agents struggle to adapt to specialized environments and do not leverage past interactions, approaching each new task from scratch regardless of their accumulated experience. We introduce Experiential Reflective Learning (ERL), a simple self-improvement framework that enables rapid environment adaptation through experiential learning. ERL reflects on task trajectories and outcomes to generate heuristics, capturing actionable lessons that transfer across tasks. At test time, relevant heuristics are retrieved based on the current task and injected into the agent's context to guide execution. On the Gaia2 benchmark, ERL improves success rate by 7.8% over a ReAct baseline, with large gains in task completion reliability, and outperforms prior experiential learning methods. Through systematic ablations, we find that selective retrieval is essential and that heuristics provide more transferable abstractions than few-shot trajectory prompting. These results demonstrate that reflecting on single-attempt experiences to extract transferable heuristics enables effective agent self-improvement.



---


# Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering

**arXiv ID**: 2604.08224
**arXiv URL**: https://arxiv.org/abs/2604.08224

## Abstract

Large language model (LLM) agents are increasingly built less by changing model weights than by reorganizing the runtime around them. Capabilities that earlier systems expected the model to recover internally are now externalized into memory stores, reusable skills, interaction protocols, and the surrounding harness that makes these modules reliable in practice. This paper reviews that shift through the lens of externalization. Drawing on the idea of cognitive artifacts, we argue that agent infrastructure matters not merely because it adds auxiliary components, but because it transforms hard cognitive burdens into forms that the model can solve more reliably. Under this view, memory externalizes state across time, skills externalize procedural expertise, protocols externalize interaction structure, and harness engineering serves as the unification layer that coordinates them into governed execution. We trace a historical progression from weights to context to harness, analyze memory, skills, and protocols as three distinct but coupled forms of externalization, and examine how they interact inside a larger agent system. We further discuss the trade-off between parametric and externalized capability, identify emerging directions such as self-evolving harnesses and shared agent infrastructure, and discuss open challenges in evaluation, governance, and the long-term co-evolution of models and external infrastructure. The result is a systems-level framework for explaining why practical agent progress increasingly depends not only on stronger models, but on better external cognitive infrastructure.



---


# FLEX: Continuous Agent Evolution via Forward Learning from Experience

**arXiv ID**: 2511.06449
**arXiv URL**: https://arxiv.org/abs/2511.06449

## Abstract

Autonomous agents driven by Large Language Models (LLMs) have revolutionized reasoning and problem-solving but remain static after training, unable to grow with experience as intelligent beings do during deployment. We introduce Forward Learning with EXperience (FLEX), a gradient-free learning paradigm that enables LLM agents to continuously evolve through accumulated experience. Specifically, FLEX cultivates scalable and inheritable evolution by constructing a structured experience library through continual reflection on successes and failures during interaction with the environment. FLEX delivers substantial improvements on mathematical reasoning, chemical retrosynthesis, and protein fitness prediction (up to 23% on AIME25, 10% on USPTO50k, and 14% on ProteinGym). We further identify a clear scaling law of experiential growth and the phenomenon of experience inheritance across agents, marking a step toward scalable and inheritable continuous agent evolution. Project Page: https://flex-gensi-thuair.github.io.



---


# Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success

**arXiv ID**: 2502.19645
**arXiv URL**: https://arxiv.org/abs/2502.19645

## Abstract

Recent vision-language-action models (VLAs) build upon pretrained vision-language models and leverage diverse robot datasets to demonstrate strong task execution, language following ability, and semantic generalization. Despite these successes, VLAs struggle with novel robot setups and require fine-tuning to achieve good performance, yet how to most effectively fine-tune them is unclear given many possible strategies. In this work, we study key VLA adaptation design choices such as different action decoding schemes, action representations, and learning objectives for fine-tuning, using OpenVLA as our representative base model. Our empirical analysis informs an Optimized Fine-Tuning (OFT) recipe that integrates parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective to altogether improve inference efficiency, policy performance, and flexibility in the model's input-output specifications. We propose OpenVLA-OFT, an instantiation of this recipe, which sets a new state of the art on the LIBERO simulation benchmark, significantly boosting OpenVLA's average success rate across four task suites from 76.5% to 97.1% while increasing action generation throughput by 26$\times$. In real-world evaluations, our fine-tuning recipe enables OpenVLA to successfully execute dexterous, high-frequency control tasks on a bimanual ALOHA robot and outperform other VLAs ($π_0$ and RDT-1B) fine-tuned using their default recipes, as well as strong imitation learning policies trained from scratch (Diffusion Policy and ACT) by up to 15% (absolute) in average success rate. We release code for OFT and pretrained model checkpoints at https://openvla-oft.github.io/.



---


# FireAct: Toward Language Agent Fine-tuning

**arXiv ID**: 2310.05915
**arXiv URL**: https://arxiv.org/abs/2310.05915

## Abstract

Recent efforts have augmented language models (LMs) with external tools or environments, leading to the development of language agents that can reason and act. However, most of these agents rely on few-shot prompting techniques with off-the-shelf LMs. In this paper, we investigate and argue for the overlooked direction of fine-tuning LMs to obtain language agents. Using a setup of question answering (QA) with a Google search API, we explore a variety of base LMs, prompting methods, fine-tuning data, and QA tasks, and find language agents are consistently improved after fine-tuning their backbone LMs. For example, fine-tuning Llama2-7B with 500 agent trajectories generated by GPT-4 leads to a 77% HotpotQA performance increase. Furthermore, we propose FireAct, a novel approach to fine-tuning LMs with trajectories from multiple tasks and prompting methods, and show having more diverse fine-tuning data can further improve agents. Along with other findings regarding scaling effects, robustness, generalization, efficiency and cost, our work establishes comprehensive benefits of fine-tuning LMs for agents, and provides an initial set of experimental designs, insights, as well as open questions toward language agent fine-tuning.



---


# Focused Transformer: Contrastive Training for Context Scaling

**arXiv ID**: 2307.03170
**arXiv URL**: https://arxiv.org/abs/2307.03170

## Abstract

Large language models have an exceptional capability to incorporate new information in a contextual manner. However, the full potential of such an approach is often restrained due to a limitation in the effective context length. One solution to this issue is to endow an attention layer with access to an external memory, which comprises of (key, value) pairs. Yet, as the number of documents increases, the proportion of relevant keys to irrelevant ones decreases, leading the model to focus more on the irrelevant keys. We identify a significant challenge, dubbed the distraction issue, where keys linked to different semantic values might overlap, making them hard to distinguish. To tackle this problem, we introduce the Focused Transformer (FoT), a technique that employs a training process inspired by contrastive learning. This novel approach enhances the structure of the (key, value) space, enabling an extension of the context length. Our method allows for fine-tuning pre-existing, large-scale models to lengthen their effective context. This is demonstrated by our fine-tuning of $3B$ and $7B$ OpenLLaMA checkpoints. The resulting models, which we name LongLLaMA, exhibit advancements in tasks requiring a long context. We further illustrate that our LongLLaMA models adeptly manage a $256 k$ context length for passkey retrieval.



---


# Free Process Rewards without Process Labels

**arXiv ID**: 2412.01981
**arXiv URL**: https://arxiv.org/abs/2412.01981

## Abstract

Different from its counterpart outcome reward models (ORMs), which evaluate the entire responses, a process reward model (PRM) scores a reasoning trajectory step by step, providing denser and more fine grained rewards. However, training a PRM requires labels annotated at every intermediate step, presenting significant challenges for both manual and automatic data collection. This paper aims to address this challenge. Both theoretically and empirically, we show that an \textit{implicit PRM} can be obtained at no additional cost, by simply training an ORM on the cheaper response-level labels. The only assumption is to parameterize the outcome reward as the log-likelihood ratios of the policy and reference models, which can be optimized regardless of the specific choice of loss objectives. In experiments, we instantiate our implicit PRMs with various objectives and evaluate their performance on MATH. We show that our implicit PRM outperforms a strong MCTS-based baseline \textit{á la} Math-Shepherd using less than $1/38$ of the training data. Its performance can be further improved with majority voting. We further find that scaling up instructions and responses benefits our implicit PRM, and the latter brings a larger gain. Particularly, we find that our implicit PRM, when instantiated with the cross-entropy (CE) loss, is more data-efficient and can keep improving generation models even when trained with only one response per instruction, the setup that suffers from extreme data scarcity and imbalance. Further, instructions should be relevant to downstream tasks while the diversity of responses does not bring gains. Surprisingly, training on extra Math-Shepherd step labels brings no further improvements to our implicit PRM trained on only outcome data. We hope that our work will encourage a rethinking of PRM training approaches and contribute to making training PRMs more accessible.



---


# FreePRM: Training Process Reward Models Without Ground Truth Process Labels

**arXiv ID**: 2506.03570
**arXiv URL**: https://arxiv.org/abs/2506.03570

## Abstract

Recent advancements in Large Language Models (LLMs) have demonstrated that Process Reward Models (PRMs) play a crucial role in enhancing model performance. However, training PRMs typically requires step-level labels, either manually annotated or automatically generated, which can be costly and difficult to obtain at scale. To address this challenge, we introduce FreePRM, a weakly supervised framework for training PRMs without access to ground-truth step-level labels. FreePRM first generates pseudo step-level labels based on the correctness of final outcome, and then employs Buffer Probability to eliminate impact of noise inherent in pseudo labeling. Experimental results show that FreePRM achieves an average F1 score of 53.0% on ProcessBench, outperforming fully supervised PRM trained on Math-Shepherd by +24.1%. Compared to other open-source PRMs, FreePRM outperforms upon RLHFlow-PRM-Mistral-8B (28.4%) by +24.6%, EurusPRM (31.3%) by +21.7%, and Skywork-PRM-7B (42.1%) by +10.9%. This work introduces a new paradigm in PRM training, significantly reducing reliance on costly step-level annotations while maintaining strong performance.



---


# From Novice to Expert: LLM Agent Policy Optimization via Step-wise Reinforcement Learning

**arXiv ID**: 2411.03817
**arXiv URL**: https://arxiv.org/abs/2411.03817

## Abstract

The outstanding capabilities of large language models (LLMs) render them a crucial component in various autonomous agent systems. While traditional methods depend on the inherent knowledge of LLMs without fine-tuning, more recent approaches have shifted toward the reinforcement learning strategy to further enhance agents' ability to solve complex interactive tasks with environments and tools. However, previous approaches are constrained by the sparse reward issue, where existing datasets solely provide a final scalar reward for each multi-step reasoning chain, potentially leading to ineffectiveness and inefficiency in policy learning. In this paper, we introduce StepAgent, which utilizes step-wise reward to optimize the agent's reinforcement learning process. Inheriting the spirit of novice-to-expert theory, we first compare the actions of the expert and the agent to automatically generate intermediate rewards for fine-grained optimization. Additionally, we propose implicit-reward and inverse reinforcement learning techniques to facilitate agent reflection and policy adjustment. Further theoretical analysis demonstrates that the action distribution of the agent can converge toward the expert action distribution over multiple training cycles. Experimental results across various datasets indicate that StepAgent outperforms existing baseline methods.



---


# From Outcomes to Processes: Guiding PRM Learning from ORM for Inference-Time Alignment

**arXiv ID**: 2506.12446
**arXiv URL**: https://arxiv.org/abs/2506.12446

## Abstract

Inference-time alignment methods have gained significant attention for their efficiency and effectiveness in aligning large language models (LLMs) with human preferences. However, existing dominant approaches using reward-guided search (RGS) primarily rely on outcome reward models (ORMs), which suffer from a critical granularity mismatch: ORMs are designed to provide outcome rewards for complete responses, while RGS methods rely on process rewards to guide the policy, leading to inconsistent scoring and suboptimal alignment. To address this challenge, we introduce process reward models (PRMs) into RGS and argue that an ideal PRM should satisfy two objectives: Score Consistency, ensuring coherent evaluation across partial and complete responses, and Preference Consistency, aligning partial sequence assessments with human preferences. Based on these, we propose SP-PRM, a novel dual-consistency framework integrating score consistency-based and preference consistency-based partial evaluation modules without relying on human annotation. Extensive experiments on dialogue, summarization, and reasoning tasks demonstrate that SP-PRM substantially enhances existing RGS methods, achieving a 3.6%-10.3% improvement in GPT-4 evaluation scores across all tasks.



---


# G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems

**arXiv ID**: 2506.07398
**arXiv URL**: https://arxiv.org/abs/2506.07398

## Abstract

Large language model (LLM)-powered multi-agent systems (MAS) have demonstrated cognitive and execution capabilities that far exceed those of single LLM agents, yet their capacity for self-evolution remains hampered by underdeveloped memory architectures. Upon close inspection, we are alarmed to discover that prevailing MAS memory mechanisms (1) are overly simplistic, completely disregarding the nuanced inter-agent collaboration trajectories, and (2) lack cross-trial and agent-specific customization, in stark contrast to the expressive memory developed for single agents. To bridge this gap, we introduce G-Memory, a hierarchical, agentic memory system for MAS inspired by organizational memory theory, which manages the lengthy MAS interaction via a three-tier graph hierarchy: insight, query, and interaction graphs. Upon receiving a new user query, G-Memory performs bi-directional memory traversal to retrieve both $\textit{high-level, generalizable insights}$ that enable the system to leverage cross-trial knowledge, and $\textit{fine-grained, condensed interaction trajectories}$ that compactly encode prior collaboration experiences. Upon task execution, the entire hierarchy evolves by assimilating new collaborative trajectories, nurturing the progressive evolution of agent teams. Extensive experiments across five benchmarks, three LLM backbones, and three popular MAS frameworks demonstrate that G-Memory improves success rates in embodied action and accuracy in knowledge QA by up to $20.89\%$ and $10.12\%$, respectively, without any modifications to the original frameworks. Our codes are available at https://github.com/bingreeky/GMemory.



---


# GAAMA: Graph Augmented Associative Memory for Agents

**arXiv ID**: 2603.27910
**arXiv URL**: https://arxiv.org/abs/2603.27910

## Abstract

AI agents that interact with users across multiple sessions require persistent long-term memory to maintain coherent, personalized behavior. Current approaches either rely on flat retrieval-augmented generation (RAG), which loses structural relationships between memories, or use memory compression and vector retrieval that cannot capture the associative structure of multi-session conversations. There are few graph based techniques proposed in the literature, however they still suffer from hub dominated retrieval and poor hierarchical reasoning over evolving memory. We propose GAAMA, a graph-augmented associative memory system that constructs a concept-mediated hierarchical knowledge graph through a three-step pipeline: (1)~verbatim episode preservation from raw conversations, (2)~LLM-based extraction of atomic facts and topic-level concept nodes, and (3)~synthesis of higher-order reflections. The resulting graph uses four node types (episode, fact, reflection, concept) connected by five structural edge types, with concept nodes providing cross-cutting traversal paths that complement semantic similarity. Retrieval combines cosine-similarity-based $k$-nearest neighbor search with edge-type-aware Personalized PageRank (PPR) through an additive scoring function. On the LoCoMo-10 benchmark (1,540 questions across 10 multi-session conversations), GAAMA achieves 78.9\% mean reward, outperforming a tuned RAG baseline (75.0\%), HippoRAG (69.9\%), A-Mem (47.2\%), and Nemori (52.1\%). Ablation analysis shows that augmenting graph-traversal-based ranking (Personalized PageRank) with semantic search consistently improves over pure semantic search on graph nodes (+1.0 percentage point overall).



---


# GEMS: Agent-Native Multimodal Generation with Memory and Skills

**arXiv ID**: 2603.28088
**arXiv URL**: https://arxiv.org/abs/2603.28088

## Abstract

Recent multimodal generation models have achieved remarkable progress on general-purpose generation tasks, yet continue to struggle with complex instructions and specialized downstream tasks. Inspired by the success of advanced agent frameworks such as Claude Code, we propose \textbf{GEMS} (Agent-Native Multimodal \textbf{GE}neration with \textbf{M}emory and \textbf{S}kills), a framework that pushes beyond the inherent limitations of foundational models on both general and downstream tasks. GEMS is built upon three core components. Agent Loop introduces a structured multi-agent framework that iteratively improves generation quality through closed-loop optimization. Agent Memory provides a persistent, trajectory-level memory that hierarchically stores both factual states and compressed experiential summaries, enabling a global view of the optimization process while reducing redundancy. Agent Skill offers an extensible collection of domain-specific expertise with on-demand loading, allowing the system to effectively handle diverse downstream applications. Across five mainstream tasks and four downstream tasks, evaluated on multiple generative backends, GEMS consistently achieves significant performance gains. Most notably, it enables the lightweight 6B model Z-Image-Turbo to surpass the state-of-the-art Nano Banana 2 on GenEval2, demonstrating the effectiveness of agent harness in extending model capabilities beyond their original limits.



---


# GM-PRM: A Generative Multimodal Process Reward Model for Multimodal Mathematical Reasoning

**arXiv ID**: 2508.04088
**arXiv URL**: https://arxiv.org/abs/2508.04088

## Abstract

Multimodal Large Language Models (MLLMs) demonstrate remarkable capabilities but often struggle with complex, multi-step mathematical reasoning, where minor errors in visual perception or logical deduction can lead to complete failure. While Process Reward Models (PRMs) offer step-by-step supervision, existing multimodal PRMs are limited to being binary verifiers that can identify but not correct errors, offering little explanatory power. To address these deficiencies, we introduce the Generative Multimodal Process Reward Model (GM-PRM), a novel paradigm that transforms the PRM from a passive judge into an active reasoning collaborator. Instead of a simple scalar score, GM-PRM provides a fine-grained, interpretable analysis of each reasoning step, evaluating its step intent, visual alignment, and logical soundness. More critically, GM-PRM is trained to generate a corrected version of the first erroneous step it identifies. This unique corrective capability enables our new test-time inference strategy, Refined Best-of-N (Refined-BoN). This framework actively enhances solution quality by using the PRM's generated correction to guide the policy model toward a more promising reasoning trajectory, thereby improving the diversity and correctness of the solution pool. We demonstrate that GM-PRM achieves state-of-the-art results on multiple multimodal math benchmarks, significantly boosting policy model performance with remarkable data efficiency, requiring only a 20K-sample training dataset. Our code will be released upon acceptance.



---


# GSEM: Graph-based Self-Evolving Memory for Experience Augmented Clinical Reasoning

**arXiv ID**: 2603.22096
**arXiv URL**: https://arxiv.org/abs/2603.22096

## Abstract

Clinical decision-making agents can benefit from reusing prior decision experience. However, many memory-augmented methods store experiences as independent records without explicit relational structure, which may introduce noisy retrieval, unreliable reuse, and in some cases even hurt performance compared to direct LLM inference. We propose GSEM (Graph-based Self-Evolving Memory), a clinical memory framework that organizes clinical experiences into a dual-layer memory graph, capturing both the decision structure within each experience and the relational dependencies across experiences, and supporting applicability-aware retrieval and online feedback-driven calibration of node quality and edge weights. Across MedR-Bench and MedAgentsBench with two LLM backbones, GSEM achieves the highest average accuracy among all baselines, reaching 70.90\% and 69.24\% with DeepSeek-V3.2 and Qwen3.5-35B, respectively. Code is available at https://github.com/xhan1022/gsem.



---


# GUI-ReWalk: Massive Data Generation for GUI Agent via Stochastic Exploration and Intent-Aware Reasoning

**arXiv ID**: 2509.15738
**arXiv URL**: https://arxiv.org/abs/2509.15738

## Abstract

Graphical User Interface (GUI) Agents, powered by large language and vision-language models, hold promise for enabling end-to-end automation in digital environments. However, their progress is fundamentally constrained by the scarcity of scalable, high-quality trajectory data. Existing data collection strategies either rely on costly and inconsistent manual annotations or on synthetic generation methods that trade off between diversity and meaningful task coverage. To bridge this gap, we present GUI-ReWalk: a reasoning-enhanced, multi-stage framework for synthesizing realistic and diverse GUI trajectories. GUI-ReWalk begins with a stochastic exploration phase that emulates human trial-and-error behaviors, and progressively transitions into a reasoning-guided phase where inferred goals drive coherent and purposeful interactions. Moreover, it supports multi-stride task generation, enabling the construction of long-horizon workflows across multiple applications. By combining randomness for diversity with goal-aware reasoning for structure, GUI-ReWalk produces data that better reflects the intent-aware, adaptive nature of human-computer interaction. We further train Qwen2.5-VL-7B on the GUI-ReWalk dataset and evaluate it across multiple benchmarks, including Screenspot-Pro, OSWorld-G, UI-Vision, AndroidControl, and GUI-Odyssey. Results demonstrate that GUI-ReWalk enables superior coverage of diverse interaction flows, higher trajectory entropy, and more realistic user intent. These findings establish GUI-ReWalk as a scalable and data-efficient framework for advancing GUI agent research and enabling robust real-world automation.



---


# Graph-Reward-SQL: Execution-Free Reinforcement Learning for Text-to-SQL via Graph Matching and Stepwise Reward

**arXiv ID**: 2505.12380
**arXiv URL**: https://arxiv.org/abs/2505.12380

## Abstract

Reinforcement learning (RL) has been widely adopted to enhance the performance of large language models (LLMs) on Text-to-SQL tasks. However, existing methods often rely on execution-based or LLM-based Bradley-Terry reward models. The former suffers from high execution latency caused by repeated database calls, whereas the latter imposes substantial GPU memory overhead, both of which significantly hinder the efficiency and scalability of RL pipelines. To this end, we propose a novel reward model framework for RL-based Text-to-SQL named Graph-Reward-SQL, which employs the GMNScore outcome reward model. We leverage SQL graph representations to provide accurate reward signals while significantly reducing time cost and GPU memory usage. Building on this foundation, we further introduce StepRTM, a stepwise reward model that provides intermediate supervision over Common Table Expression (CTE) subqueries. This encourages both functional correctness and readability of SQL. Extensive comparative and ablation experiments on standard benchmarks, including Spider and BIRD, demonstrate that our method consistently outperforms existing reward models.



---


# HiMemVLN: Enhancing Reliability of Open-Source Zero-Shot Vision-and-Language Navigation with Hierarchical Memory System

**arXiv ID**: 2603.14807
**arXiv URL**: https://arxiv.org/abs/2603.14807

## Abstract

LLM-based agents have demonstrated impressive zero-shot performance in vision-language navigation (VLN) tasks. However, most zero-shot methods primarily rely on closed-source LLMs as navigators, which face challenges related to high token costs and potential data leakage risks. Recent efforts have attempted to address this by using open-source LLMs combined with a spatiotemporal CoT framework, but they still fall far short compared to closed-source models. In this work, we identify a critical issue, Navigation Amnesia, through a detailed analysis of the navigation process. This issue leads to navigation failures and amplifies the gap between open-source and closed-source methods. To address this, we propose HiMemVLN, which incorporates a Hierarchical Memory System into a multimodal large model to enhance visual perception recall and long-term localization, mitigating the amnesia issue and improving the agent's navigation performance. Extensive experiments in both simulated and real-world environments demonstrate that HiMemVLN achieves nearly twice the performance of the open-source state-of-the-art method. The code is available at https://github.com/lvkailin0118/HiMemVLN.



---


# HiMem: Hierarchical Long-Term Memory for LLM Long-Horizon Agents

**arXiv ID**: 2601.06377
**arXiv URL**: https://arxiv.org/abs/2601.06377

## Abstract

Although long-term memory systems have made substantial progress in recent years, they still exhibit clear limitations in adaptability, scalability, and self-evolution under continuous interaction settings. Inspired by cognitive theories, we propose HiMem, a hierarchical long-term memory framework for long-horizon dialogues, designed to support memory construction, retrieval, and dynamic updating during sustained interactions. HiMem constructs cognitively consistent Episode Memory via a Topic-Aware Event--Surprise Dual-Channel Segmentation strategy, and builds Note Memory that captures stable knowledge through a multi-stage information extraction pipeline. These two memory types are semantically linked to form a hierarchical structure that bridges concrete interaction events and abstract knowledge, enabling efficient retrieval without sacrificing information fidelity. HiMem supports both hybrid and best-effort retrieval strategies to balance accuracy and efficiency, and incorporates conflict-aware Memory Reconsolidation to revise and supplement stored knowledge based on retrieval feedback. This design enables continual memory self-evolution over long-term use. Experimental results on long-horizon dialogue benchmarks demonstrate that HiMem consistently outperforms representative baselines in accuracy, consistency, and long-term reasoning, while maintaining favorable efficiency. Overall, HiMem provides a principled and scalable design paradigm for building adaptive and self-evolving LLM-based conversational agents. The code is available at https://github.com/jojopdq/HiMem.



---


# How Well Do Agentic Skills Work in the Wild: Benchmarking LLM Skill Usage in Realistic Settings

**arXiv ID**: 2604.04323
**arXiv URL**: https://arxiv.org/abs/2604.04323

## Abstract

Agent skills, which are reusable, domain-specific knowledge artifacts, have become a popular mechanism for extending LLM-based agents, yet formally benchmarking skill usage performance remains scarce. Existing skill benchmarking efforts focus on overly idealized conditions, where LLMs are directly provided with hand-crafted, narrowly-tailored task-specific skills for each task, whereas in many realistic settings, the LLM agent may have to search for and select relevant skills on its own, and even the closest matching skills may not be well-tailored for the task. In this paper, we conduct the first comprehensive study of skill utility under progressively challenging realistic settings, where agents must retrieve skills from a large collection of 34k real-world skills and may not have access to any hand-curated skills. Our findings reveal that the benefits of skills are fragile: performance gains degrade consistently as settings become more realistic, with pass rates approaching no-skill baselines in the most challenging scenarios. To narrow this gap, we study skill refinement strategies, including query-specific and query-agnostic approaches, and we show that query-specific refinement substantially recovers lost performance when the initial skills are of reasonable relevance and quality. We further demonstrate the generality of retrieval and refinement on Terminal-Bench 2.0, where they improve the pass rate of Claude Opus 4.6 from 57.7% to 65.5%. Our results, consistent across multiple models, highlight both the promise and the current limitations of skills for LLM-based agents. Our code is available at https://github.com/UCSB-NLP-Chang/Skill-Usage.



---


# How Well Does Agent Development Reflect Real-World Work?

**arXiv ID**: 2603.01203
**arXiv URL**: https://arxiv.org/abs/2603.01203

## Abstract

AI agents are increasingly developed and evaluated on benchmarks relevant to human work, yet it remains unclear how representative these benchmarking efforts are of the labor market as a whole. In this work, we systematically study the relationship between agent development efforts and the distribution of real-world human work by mapping benchmark instances to work domains and skills. We first analyze 43 benchmarks and 72,342 tasks, measuring their alignment with human employment and capital allocation across all 1,016 real-world occupations in the U.S. labor market. We reveal substantial mismatches between agent development that tends to be programming-centric, and the categories in which human labor and economic value are concentrated. Within work areas that agents currently target, we further characterize current agent utility by measuring their autonomy levels, providing practical guidance for agent interaction strategies across work scenarios. Building on these findings, we propose three measurable principles for designing benchmarks that better capture socially important and technically challenging forms of work: coverage, realism, and granular evaluation.



---


# Human-Inspired Continuous Learning of Internal Reasoning Processes

**arXiv ID**: 2602.11516
**arXiv URL**: https://arxiv.org/abs/2602.11516

## Abstract

Learning internal reasoning processes is crucial for developing AI systems capable of sustained adaptation in dynamic real-world environments. However, most existing approaches primarily emphasize learning task-specific outputs or static knowledge representations, while overlooking the continuous refinement of internal reasoning structures, action scheduling policies, and learning mechanisms themselves. In this paper, we propose a human-inspired continuous learning framework that unifies reasoning, action, reflection, and verification within a sequential reasoning model enhanced by parallel learning. The framework explicitly treats internal thinking processes as primary learning objects. It systematically records internal reasoning trajectories and environmental interactions as structured learning material, enabling the system to optimize not only task-level content but also the organization, scheduling, and evolution of reasoning activities. This design realizes learning alongside processing, allowing cognitive structures to improve during execution. Furthermore, the framework supports controlled replacement of predefined logic with learned procedures and introduces a hierarchical learning-to-learn mechanism that jointly adapts task-level parameters and learning strategies. As a result, the system progressively evolves its internal cognitive architecture while preserving operational stability. Experimental results on a temperature sensor abnormality detection task show that incorporating internal-process learning reduces average runtime by 23.9%.



---


# HyCodePolicy: Hybrid Language Controllers for Multimodal Monitoring and Decision in Embodied Agents

**arXiv ID**: 2508.02629
**arXiv URL**: https://arxiv.org/abs/2508.02629

## Abstract

Recent advances in multimodal large language models (MLLMs) have enabled richer perceptual grounding for code policy generation in embodied agents. However, most existing systems lack effective mechanisms to adaptively monitor policy execution and repair codes during task completion. In this work, we introduce HyCodePolicy, a hybrid language-based control framework that systematically integrates code synthesis, geometric grounding, perceptual monitoring, and iterative repair into a closed-loop programming cycle for embodied agents. Technically, given a natural language instruction, our system first decomposes it into subgoals and generates an initial executable program grounded in object-centric geometric primitives. The program is then executed in simulation, while a vision-language model (VLM) observes selected checkpoints to detect and localize execution failures and infer failure reasons. By fusing structured execution traces capturing program-level events with VLM-based perceptual feedback, HyCodePolicy infers failure causes and repairs programs. This hybrid dual feedback mechanism enables self-correcting program synthesis with minimal human supervision. Our results demonstrate that HyCodePolicy significantly improves the robustness and sample efficiency of robot manipulation policies, offering a scalable strategy for integrating multimodal reasoning into autonomous decision-making pipelines.



---


# H²R: Hierarchical Hindsight Reflection for Multi-Task LLM Agents

**arXiv ID**: 2509.12810
**arXiv URL**: https://arxiv.org/abs/2509.12810

## Abstract

Large language model (LLM)-based agents have shown strong potential in multi-task scenarios, owing to their ability to transfer knowledge across diverse tasks. However, existing approaches often treat prior experiences and knowledge as monolithic units, leading to inefficient and coarse-grained knowledge transfer. In this work, we propose a novel hierarchical memory architecture that enables fine-grained knowledge transfer by decoupling high-level planning memory from low-level execution memory. To construct and refine these hierarchical memories, we introduce Hierarchical Hindsight Reflection (H$^2$R), a mechanism that distills reusable and hierarchical knowledge from past agent-environment interactions. At test time, H$^2$R performs retrievals of high-level and low-level memories separately, allowing LLM-based agents to efficiently access and utilize task-relevant knowledge for new tasks.Experimental results across two benchmarks demonstrate that H$^2$R can improve generalization and decision-making performance, outperforming prior baselines such as Expel.



---


# Improving Retrospective Language Agents via Joint Policy Gradient Optimization

**arXiv ID**: 2503.01490
**arXiv URL**: https://arxiv.org/abs/2503.01490

## Abstract

In recent research advancements within the community, large language models (LLMs) have sparked great interest in creating autonomous agents. However, current prompt-based agents often heavily rely on large-scale LLMs. Meanwhile, although fine-tuning methods significantly enhance the capabilities of smaller LLMs, the fine-tuned agents often lack the potential for self-reflection and self-improvement. To address these challenges, we introduce a novel agent framework named RetroAct, which is a framework that jointly optimizes both task-planning and self-reflective evolution capabilities in language agents. Specifically, we develop a two-stage joint optimization process that integrates imitation learning and reinforcement learning, and design an off-policy joint policy gradient optimization algorithm with imitation learning regularization to enhance the data efficiency and training stability in agent tasks. RetroAct significantly improves the performance of open-source models, reduces dependency on closed-source LLMs, and enables fine-tuned agents to learn and evolve continuously. We conduct extensive experiments across various testing environments, demonstrating RetroAct has substantial improvements in task performance and decision-making processes.



---


# InfiGUIAgent: A Multimodal Generalist GUI Agent with Native Reasoning and Reflection

**arXiv ID**: 2501.04575
**arXiv URL**: https://arxiv.org/abs/2501.04575

## Abstract

Graphical User Interface (GUI) Agents, powered by multimodal large language models (MLLMs), have shown great potential for task automation on computing devices such as computers and mobile phones. However, existing agents face challenges in multi-step reasoning and reliance on textual annotations, limiting their effectiveness. We introduce \textit{InfiGUIAgent}, an MLLM-based GUI Agent trained with a two-stage supervised fine-tuning pipeline. Stage 1 enhances fundamental skills such as GUI understanding and grounding, while Stage 2 integrates hierarchical reasoning and expectation-reflection reasoning skills using synthesized data to enable native reasoning abilities of the agents. \textit{InfiGUIAgent} achieves competitive performance on several GUI benchmarks, highlighting the impact of native reasoning skills in enhancing GUI interaction for automation tasks. Resources are available at \url{https://github.com/Reallm-Labs/InfiGUIAgent}.



---


# Internalizing Agency from Reflective Experience

**arXiv ID**: 2603.16843
**arXiv URL**: https://arxiv.org/abs/2603.16843

## Abstract

Large language models are increasingly deployed as autonomous agents that must plan, act, and recover from mistakes through long-horizon interaction with environments that provide rich feedback. However, prevailing outcome-driven post-training methods (e.g., RL with verifiable rewards) primarily optimize final success signals, leaving rich environment feedback underutilized. Consequently, they often lead to distribution sharpening: the policy becomes better at reproducing a narrow set of already-successful behaviors, while failing to improve the feedback-grounded agency needed to expand problem-solving capacity (e.g., Pass@k) in long-horizon settings.   To address this, we propose LEAFE (Learning Feedback-Grounded Agency from Reflective Experience), a framework that internalizes recovery agency from reflective experience. Specifically, during exploration, the agent summarizes environment feedback into actionable experience, backtracks to earlier decision points, and explores alternative branches with revised actions. We then distill these experience-guided corrections into the model through supervised fine-tuning, enabling the policy to recover more effectively in future interactions. Across a diverse set of interactive coding and agentic tasks under fixed interaction budgets, LEAFE consistently improves Pass@1 over the base model and achieves higher Pass@k than outcome-driven baselines (GRPO) and experience-based methods such as Early Experience, with gains of up to 14% on Pass@128.



---


# Investigate-Consolidate-Exploit: A General Strategy for Inter-Task Agent Self-Evolution

**arXiv ID**: 2401.13996
**arXiv URL**: https://arxiv.org/abs/2401.13996

## Abstract

This paper introduces Investigate-Consolidate-Exploit (ICE), a novel strategy for enhancing the adaptability and flexibility of AI agents through inter-task self-evolution. Unlike existing methods focused on intra-task learning, ICE promotes the transfer of knowledge between tasks for genuine self-evolution, similar to human experience learning. The strategy dynamically investigates planning and execution trajectories, consolidates them into simplified workflows and pipelines, and exploits them for improved task execution. Our experiments on the XAgent framework demonstrate ICE's effectiveness, reducing API calls by as much as 80% and significantly decreasing the demand for the model's capability. Specifically, when combined with GPT-3.5, ICE's performance matches that of raw GPT-4 across various agent tasks. We argue that this self-evolution approach represents a paradigm shift in agent design, contributing to a more robust AI community and ecosystem, and moving a step closer to full autonomy.



---


# Iterative Experience Refinement of Software-Developing Agents

**arXiv ID**: 2405.04219
**arXiv URL**: https://arxiv.org/abs/2405.04219

## Abstract

Autonomous agents powered by large language models (LLMs) show significant potential for achieving high autonomy in various scenarios such as software development. Recent research has shown that LLM agents can leverage past experiences to reduce errors and enhance efficiency. However, the static experience paradigm, reliant on a fixed collection of past experiences acquired heuristically, lacks iterative refinement and thus hampers agents' adaptability. In this paper, we introduce the Iterative Experience Refinement framework, enabling LLM agents to refine experiences iteratively during task execution. We propose two fundamental patterns: the successive pattern, refining based on nearest experiences within a task batch, and the cumulative pattern, acquiring experiences across all previous task batches. Augmented with our heuristic experience elimination, the method prioritizes high-quality and frequently-used experiences, effectively managing the experience space and enhancing efficiency. Extensive experiments show that while the successive pattern may yield superior results, the cumulative pattern provides more stable performance. Moreover, experience elimination facilitates achieving better performance using just 11.54% of a high-quality subset.



---


# JEF-Hinter: Leveraging Offline Knowledge for Improving Web Agents Adaptation

**arXiv ID**: 2510.04373
**arXiv URL**: https://arxiv.org/abs/2510.04373

## Abstract

Large language model (LLM) agents perform well in sequential decision-making tasks, but improving them on unfamiliar domains often requires costly online interactions or fine-tuning on large expert datasets. These strategies are impractical for closed-source models and expensive for open-source ones, with risks of catastrophic forgetting. Offline trajectories offer reusable knowledge, yet demonstration-based methods struggle because raw traces are long, noisy, and tied to specific tasks. We present Just-in-time Episodic Feedback Hinter (JEF-Hinter), an agentic system that distills offline traces into compact, context-aware hints. A zooming mechanism highlights decisive steps in long trajectories, capturing both strategies and pitfalls. Unlike prior methods, JEF-Hinter leverages both successful and failed trajectories, extracting guidance even when only failure data is available, while supporting parallelized hint generation and benchmark-independent prompting. At inference, a retriever selects relevant hints for the current state, providing targeted guidance with transparency and traceability. Experiments on MiniWoB++, WorkArena-L1, and WebArena-Lite show that JEF-Hinter consistently outperforms strong baselines, including human- and document-based hints.



---


# KG-RAG: Enhancing GUI Agent Decision-Making via Knowledge Graph-Driven Retrieval-Augmented Generation

**arXiv ID**: 2509.00366
**arXiv URL**: https://arxiv.org/abs/2509.00366

## Abstract

Despite recent progress, Graphic User Interface (GUI) agents powered by Large Language Models (LLMs) struggle with complex mobile tasks due to limited app-specific knowledge. While UI Transition Graphs (UTGs) offer structured navigation representations, they are underutilized due to poor extraction and inefficient integration. We introduce KG-RAG, a Knowledge Graph-driven Retrieval-Augmented Generation framework that transforms fragmented UTGs into structured vector databases for efficient real-time retrieval. By leveraging an intent-guided LLM search method, KG-RAG generates actionable navigation paths, enhancing agent decision-making. Experiments across diverse mobile apps show that KG-RAG outperforms existing methods, achieving a 75.8% success rate (8.9% improvement over AutoDroid), 84.6% decision accuracy (8.1% improvement), and reducing average task steps from 4.5 to 4.1. Additionally, we present KG-Android-Bench and KG-Harmony-Bench, two benchmarks tailored to the Chinese mobile ecosystem for future research. Finally, KG-RAG transfers to web/desktop (+40% SR on Weibo-web; +20% on QQ Music-desktop), and a UTG cost ablation shows accuracy saturates at ~4h per complex app, enabling practical deployment trade-offs.



---


# Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models

**arXiv ID**: 2310.04406
**arXiv URL**: https://arxiv.org/abs/2310.04406

## Abstract

While language models (LMs) have shown potential across a range of decision-making tasks, their reliance on simple acting processes limits their broad deployment as autonomous agents. In this paper, we introduce Language Agent Tree Search (LATS) -- the first general framework that synergizes the capabilities of LMs in reasoning, acting, and planning. By leveraging the in-context learning ability of LMs, we integrate Monte Carlo Tree Search into LATS to enable LMs as agents, along with LM-powered value functions and self-reflections for proficient exploration and enhanced decision-making. A key feature of our approach is the incorporation of an environment for external feedback, which offers a more deliberate and adaptive problem-solving mechanism that surpasses the constraints of existing techniques. Our experimental evaluation across diverse domains, including programming, interactive question-answering (QA), web navigation, and math, validates the effectiveness and generality of LATS in decision-making while maintaining competitive or improved reasoning performance. Notably, LATS achieves state-of-the-art pass@1 accuracy (92.7%) for programming on HumanEval with GPT-4 and demonstrates gradient-free performance (average score of 75.9) comparable to gradient-based fine-tuning for web navigation on WebShop with GPT-3.5. Code can be found at https://github.com/lapisrocks/LanguageAgentTreeSearch



---


# Language Agents as Optimizable Graphs

**arXiv ID**: 2402.16823
**arXiv URL**: https://arxiv.org/abs/2402.16823

## Abstract

Various human-designed prompt engineering techniques have been proposed to improve problem solvers based on Large Language Models (LLMs), yielding many disparate code bases. We unify these approaches by describing LLM-based agents as computational graphs. The nodes implement functions to process multimodal data or query LLMs, and the edges describe the information flow between operations. Graphs can be recursively combined into larger composite graphs representing hierarchies of inter-agent collaboration (where edges connect operations of different agents). Our novel automatic graph optimizers (1) refine node-level LLM prompts (node optimization) and (2) improve agent orchestration by changing graph connectivity (edge optimization). Experiments demonstrate that our framework can be used to efficiently develop, integrate, and automatically improve various LLM agents. The code can be found at https://github.com/metauto-ai/gptswarm.



---


# LatentEvolve: Self-Evolving Test-Time Scaling in Latent Space

**arXiv ID**: 2509.24771
**arXiv URL**: https://arxiv.org/abs/2509.24771

## Abstract

Test-time Scaling (TTS) has been demonstrated to significantly enhance the reasoning capabilities of Large Language Models (LLMs) during the inference phase without altering model parameters. However, existing TTS methods are largely independent, implying that LLMs have not yet evolved to progressively learn how to scale more effectively. With the objective of evolving LLMs to learn ``how to scale test-time computation,'' we propose LatentEvolve, a self-evolving latent TTS framework inspired by the complementary learning system (CLS) theory. Analogous to the human brain's dual system of a fast-recall hippocampus and a slow-consolidating neocortex, LatentEvolve comprises two evolutionary components: \textit{daytime scaling}, which rapidly retrieves historical latent representations to better guide current LLM reasoning; and \textit{nighttime scaling}, which integrates past latent optimizations in a manner akin to the human brain's consolidation of experiences during sleep. The alternation of daytime and nighttime processes facilitates a fast and slow evolution of LLM TTS, mirroring human cognitive dynamics in a fully unsupervised manner. Extensive experiments across eight benchmarks and five model backbones demonstrate that our LatentEvolve surpasses state-of-the-art TTS methods such as LatentSeek and TTRL by up to $13.33\%$ and exhibits exceptional cross-domain and cross-backbone generalization.



---


# LatentMem: Customizing Latent Memory for Multi-Agent Systems

**arXiv ID**: 2602.03036
**arXiv URL**: https://arxiv.org/abs/2602.03036

## Abstract

Large language model (LLM)-powered multi-agent systems (MAS) demonstrate remarkable collective intelligence, wherein multi-agent memory serves as a pivotal mechanism for continual adaptation. However, existing multi-agent memory designs remain constrained by two fundamental bottlenecks: (i) memory homogenization arising from the absence of role-aware customization, and (ii) information overload induced by excessively fine-grained memory entries. To address these limitations, we propose LatentMem, a learnable multi-agent memory framework designed to customize agent-specific memories in a token-efficient manner. Specifically, LatentMem comprises an experience bank that stores raw interaction trajectories in a lightweight form, and a memory composer that synthesizes compact latent memories conditioned on retrieved experience and agent-specific contexts. Further, we introduce Latent Memory Policy Optimization (LMPO), which propagates task-level optimization signals through latent memories to the composer, encouraging it to produce compact and high-utility representations. Extensive experiments across diverse benchmarks and mainstream MAS frameworks show that LatentMem achieves a performance gain of up to $19.36$% over vanilla settings and consistently outperforms existing memory architectures, without requiring any modifications to the underlying frameworks.



---


# Learn Like Humans: Use Meta-cognitive Reflection for Efficient Self-Improvement

**arXiv ID**: 2601.11974
**arXiv URL**: https://arxiv.org/abs/2601.11974

## Abstract

While Large Language Models (LLMs) enable complex autonomous behavior, current agents remain constrained by static, human-designed prompts that limit adaptability. Existing self-improving frameworks attempt to bridge this gap but typically rely on inefficient, multi-turn recursive loops that incur high computational costs. To address this, we propose Metacognitive Agent Reflective Self-improvement (MARS), a framework that achieves efficient self-evolution within a single recurrence cycle. Inspired by educational psychology, MARS mimics human learning by integrating principle-based reflection (abstracting normative rules to avoid errors) and procedural reflection (deriving step-by-step strategies for success). By synthesizing these insights into optimized instructions, MARS allows agents to systematically refine their reasoning logic without continuous online feedback. Extensive experiments on six benchmarks demonstrate that MARS outperforms state-of-the-art self-evolving systems while significantly reducing computational overhead.



---


# Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents

**arXiv ID**: 2402.11651
**arXiv URL**: https://arxiv.org/abs/2402.11651

## Abstract

Large language models (LLMs) have achieved success in acting as agents, which interact with environments through tools such as search engines. However, LLMs are optimized for language generation instead of tool use during training or alignment, limiting their effectiveness as agents. To resolve this problem, previous work has first collected interaction trajectories between LLMs and environments, using only trajectories that successfully finished the task to fine-tune smaller models, making fine-tuning data scarce and acquiring it both difficult and costly. Discarding failed trajectories also leads to significant wastage of data and resources and limits the possible optimization paths during fine-tuning. In this paper, we argue that unsuccessful trajectories offer valuable insights, and LLMs can learn from these trajectories through appropriate quality control and fine-tuning strategies. By simply adding a prefix or suffix that tells the model whether to generate a successful trajectory during training, we improve model performance by a large margin on mathematical reasoning, multi-hop question answering, and strategic question answering tasks. We further analyze the inference results and find that our method provides a better trade-off between valuable information and errors in unsuccessful trajectories. To our knowledge, we are the first to demonstrate the value of negative trajectories and their application in agent-tunning scenarios. Our findings offer guidance for developing better agent-tuning methods and low-resource data usage techniques.



---


# Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement

**arXiv ID**: 2512.18950
**arXiv URL**: https://arxiv.org/abs/2512.18950

## Abstract

We present MACLA, a framework that decouples reasoning from learning by maintaining a frozen large language model while performing all adaptation in an external hierarchical procedural memory. MACLA extracts reusable procedures from trajectories, tracks reliability via Bayesian posteriors, selects actions through expected-utility scoring, and refines procedures by contrasting successes and failures. Across four benchmarks (ALFWorld, WebShop, TravelPlanner, InterCodeSQL), MACLA achieves 78.1 percent average performance, outperforming all baselines. On ALFWorld unseen tasks, MACLA reaches 90.3 percent with 3.1 percent positive generalization. The system constructs memory in 56 seconds, 2800 times faster than the state-of-the-art LLM parameter-training baseline, compressing 2851 trajectories into 187 procedures. Experimental results demonstrate that structured external memory with Bayesian selection and contrastive refinement enables sample-efficient, interpretable, and continually improving agents without LLM parameter updates.



---


# Learning How to Remember: A Meta-Cognitive Management Method for Structured and Transferable Agent Memory

**arXiv ID**: 2601.07470
**arXiv URL**: https://arxiv.org/abs/2601.07470

## Abstract

Large language model (LLM) agents increasingly rely on accumulated memory to solve long-horizon decision-making tasks. However, most existing approaches store memory in fixed representations and reuse it at a single or implicit level of abstraction, which limits generalization and often leads to negative transfer when distribution shift. This paper proposes the Meta-Cognitive Memory Abstraction method (MCMA), which treats memory abstraction as a learnable cognitive skill rather than a fixed design choice. MCMA decouples task execution from memory management by combining a frozen task model with a learned memory copilot. The memory copilot is trained using direct preference optimization, it determines how memories should be structured, abstracted, and reused. Memories are further organized into a hierarchy of abstraction levels, enabling selective reuse based on task similarity. When no memory is transferable, MCMA transfers the ability to abstract and manage memory by transferring the memory copilot. Experiments on ALFWorld, ScienceWorld, and BabyAI demonstrate substantial improvements in performance, out-of-distribution generalization, and cross-task transfer over several baselines.



---


# Learning from Trials and Errors: Reflective Test-Time Planning for Embodied LLMs

**arXiv ID**: 2602.21198
**arXiv URL**: https://arxiv.org/abs/2602.21198

## Abstract

Embodied LLMs endow robots with high-level task reasoning, but they cannot reflect on what went wrong or why, turning deployment into a sequence of independent trials where mistakes repeat rather than accumulate into experience. Drawing upon human reflective practitioners, we introduce Reflective Test-Time Planning, which integrates two modes of reflection: \textit{reflection-in-action}, where the agent uses test-time scaling to generate and score multiple candidate actions using internal reflections before execution; and \textit{reflection-on-action}, which uses test-time training to update both its internal reflection model and its action policy based on external reflections after execution. We also include retrospective reflection, allowing the agent to re-evaluate earlier decisions and perform model updates with hindsight for proper long-horizon credit assignment. Experiments on our newly-designed Long-Horizon Household benchmark and MuJoCo Cupboard Fitting benchmark show significant gains over baseline models, with ablative studies validating the complementary roles of reflection-in-action and reflection-on-action. Qualitative analyses, including real-robot trials, highlight behavioral correction through reflection.



---


# Let's Verify Step by Step

**arXiv ID**: 2305.20050
**arXiv URL**: https://arxiv.org/abs/2305.20050

## Abstract

In recent years, large language models have greatly improved in their ability to perform complex multi-step reasoning. However, even state-of-the-art models still regularly produce logical mistakes. To train more reliable models, we can turn either to outcome supervision, which provides feedback for a final result, or process supervision, which provides feedback for each intermediate reasoning step. Given the importance of training reliable models, and given the high cost of human feedback, it is important to carefully compare the both methods. Recent work has already begun this comparison, but many questions still remain. We conduct our own investigation, finding that process supervision significantly outperforms outcome supervision for training models to solve problems from the challenging MATH dataset. Our process-supervised model solves 78% of problems from a representative subset of the MATH test set. Additionally, we show that active learning significantly improves the efficacy of process supervision. To support related research, we also release PRM800K, the complete dataset of 800,000 step-level human feedback labels used to train our best reward model.



---


# Listwise Reward Estimation for Offline Preference-based Reinforcement Learning

**arXiv ID**: 2408.04190
**arXiv URL**: https://arxiv.org/abs/2408.04190

## Abstract

In Reinforcement Learning (RL), designing precise reward functions remains to be a challenge, particularly when aligning with human intent. Preference-based RL (PbRL) was introduced to address this problem by learning reward models from human feedback. However, existing PbRL methods have limitations as they often overlook the second-order preference that indicates the relative strength of preference. In this paper, we propose Listwise Reward Estimation (LiRE), a novel approach for offline PbRL that leverages second-order preference information by constructing a Ranked List of Trajectories (RLT), which can be efficiently built by using the same ternary feedback type as traditional methods. To validate the effectiveness of LiRE, we propose a new offline PbRL dataset that objectively reflects the effect of the estimated rewards. Our extensive experiments on the dataset demonstrate the superiority of LiRE, i.e., outperforming state-of-the-art baselines even with modest feedback budgets and enjoying robustness with respect to the number of feedbacks and feedback noise. Our code is available at https://github.com/chwoong/LiRE



---


# LongNav-R1: Horizon-Adaptive Multi-Turn RL for Long-Horizon VLA Navigation

**arXiv ID**: 2602.12351
**arXiv URL**: https://arxiv.org/abs/2602.12351

## Abstract

This paper develops LongNav-R1, an end-to-end multi-turn reinforcement learning (RL) framework designed to optimize Visual-Language-Action (VLA) models for long-horizon navigation. Unlike existing single-turn paradigm, LongNav-R1 reformulates the navigation decision process as a continuous multi-turn conversation between the VLA policy and the embodied environment. This multi-turn RL framework offers two distinct advantages: i) it enables the agent to reason about the causal effects of historical interactions and sequential future outcomes; and ii) it allows the model to learn directly from online interactions, fostering diverse trajectory generation and avoiding the behavioral rigidity often imposed by human demonstrations. Furthermore, we introduce Horizon-Adaptive Policy Optimization. This mechanism explicitly accounts for varying horizon lengths during advantage estimation, facilitating accurate temporal credit assignment over extended sequences. Consequently, the agent develops diverse navigation behaviors and resists collapse during long-horizon tasks. Experiments on object navigation benchmarks validate the framework's efficacy: With 4,000 rollout trajectories, LongNav-R1 boosts the Qwen3-VL-2B success rate from 64.3% to 73.0%. These results demonstrate superior sample efficiency and significantly outperform state-of-the-art methods. The model's generalizability and robustness are further validated by its zero-shot performance in long-horizon real-world navigation settings. All source code will be open-sourced upon publication.



---


# MAI-UI Technical Report: Real-World Centric Foundation GUI Agents

**arXiv ID**: 2512.22047
**arXiv URL**: https://arxiv.org/abs/2512.22047

## Abstract

The development of GUI agents could revolutionize the next generation of human-computer interaction. Motivated by this vision, we present MAI-UI, a family of foundation GUI agents spanning the full spectrum of sizes, including 2B, 8B, 32B, and 235B-A22B variants. We identify four key challenges to realistic deployment: the lack of native agent-user interaction, the limits of UI-only operation, the absence of a practical deployment architecture, and brittleness in dynamic environments. MAI-UI addresses these issues with a unified methodology: a self-evolving data pipeline that expands the navigation data to include user interaction and MCP tool calls, a native device-cloud collaboration system routes execution by task state, and an online RL framework with advanced optimizations to scale parallel environments and context length. MAI-UI establishes new state-of-the-art across GUI grounding and mobile navigation. On grounding benchmarks, it reaches 73.5% on ScreenSpot-Pro, 91.3% on MMBench GUI L2, 70.9% on OSWorld-G, and 49.2% on UI-Vision, surpassing Gemini-3-Pro and Seed1.8 on ScreenSpot-Pro. On mobile GUI navigation, it sets a new SOTA of 76.7% on AndroidWorld, surpassing UI-Tars-2, Gemini-2.5-Pro and Seed1.8. On MobileWorld, MAI-UI obtains 41.7% success rate, significantly outperforming end-to-end GUI models and competitive with Gemini-3-Pro based agentic frameworks. Our online RL experiments show significant gains from scaling parallel environments from 32 to 512 (+5.2 points) and increasing environment step budget from 15 to 50 (+4.3 points). Finally, the native device-cloud collaboration system improves on-device performance by 33%, reduces cloud model calls by over 40%, and preserves user privacy.



---


# MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs

**arXiv ID**: 2512.20845
**arXiv URL**: https://arxiv.org/abs/2512.20845

## Abstract

LLMs have shown the capacity to improve their performance on reasoning tasks through reflecting on their mistakes, and acting with these reflections in mind. However, continual reflections of the same LLM onto itself exhibit degeneration of thought, where the LLM continues to repeat the same errors again and again even with the knowledge that its wrong. To address this problem, we instead introduce multi-agent with multi-persona debators as the method to generate reflections. Through out extensive experimentation, we've found that the leads to better diversity of in the reflections generated by the llm agent. We demonstrate an accuracy of 47% EM HotPot QA (question answering) and 82.7% on HumanEval (programming), both performances surpassing reflection with a single llm.



---


# Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations

**arXiv ID**: 2312.08935
**arXiv URL**: https://arxiv.org/abs/2312.08935

## Abstract

In this paper, we present an innovative process-oriented math process reward model called \textbf{Math-Shepherd}, which assigns a reward score to each step of math problem solutions. The training of Math-Shepherd is achieved using automatically constructed process-wise supervision data, breaking the bottleneck of heavy reliance on manual annotation in existing work. We explore the effectiveness of Math-Shepherd in two scenarios: 1) \textit{Verification}: Math-Shepherd is utilized for reranking multiple outputs generated by Large Language Models (LLMs); 2) \textit{Reinforcement Learning}: Math-Shepherd is employed to reinforce LLMs with step-by-step Proximal Policy Optimization (PPO). With Math-Shepherd, a series of open-source LLMs demonstrates exceptional performance. For instance, the step-by-step PPO with Math-Shepherd significantly improves the accuracy of Mistral-7B (77.9\%$\to$84.1\% on GSM8K and 28.6\%$\to$33.0\% on MATH). The accuracy can be further enhanced to 89.1\% and 43.5\% on GSM8K and MATH with the verification of Math-Shepherd, respectively. We believe that automatic process supervision holds significant potential for the future evolution of LLMs.



---


# Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory

**arXiv ID**: 2504.19413
**arXiv URL**: https://arxiv.org/abs/2504.19413

## Abstract

Large Language Models (LLMs) have demonstrated remarkable prowess in generating contextually coherent responses, yet their fixed context windows pose fundamental challenges for maintaining consistency over prolonged multi-session dialogues. We introduce Mem0, a scalable memory-centric architecture that addresses this issue by dynamically extracting, consolidating, and retrieving salient information from ongoing conversations. Building on this foundation, we further propose an enhanced variant that leverages graph-based memory representations to capture complex relational structures among conversational elements. Through comprehensive evaluations on LOCOMO benchmark, we systematically compare our approaches against six baseline categories: (i) established memory-augmented systems, (ii) retrieval-augmented generation (RAG) with varying chunk sizes and k-values, (iii) a full-context approach that processes the entire conversation history, (iv) an open-source memory solution, (v) a proprietary model system, and (vi) a dedicated memory management platform. Empirical results show that our methods consistently outperform all existing memory systems across four question categories: single-hop, temporal, multi-hop, and open-domain. Notably, Mem0 achieves 26% relative improvements in the LLM-as-a-Judge metric over OpenAI, while Mem0 with graph memory achieves around 2% higher overall score than the base configuration. Beyond accuracy gains, we also markedly reduce computational overhead compared to full-context method. In particular, Mem0 attains a 91% lower p95 latency and saves more than 90% token cost, offering a compelling balance between advanced reasoning capabilities and practical deployment constraints. Our findings highlight critical role of structured, persistent memory mechanisms for long-term conversational coherence, paving the way for more reliable and efficient LLM-driven AI agents.



---


# MemEvolve: Meta-Evolution of Agent Memory Systems

**arXiv ID**: 2512.18746
**arXiv URL**: https://arxiv.org/abs/2512.18746

## Abstract

Self-evolving memory systems are unprecedentedly reshaping the evolutionary paradigm of large language model (LLM)-based agents. Prior work has predominantly relied on manually engineered memory architectures to store trajectories, distill experience, and synthesize reusable tools, enabling agents to evolve on the fly within environment interactions. However, this paradigm is fundamentally constrained by the staticity of the memory system itself: while memory facilitates agent-level evolving, the underlying memory architecture cannot be meta-adapted to diverse task contexts. To address this gap, we propose MemEvolve, a meta-evolutionary framework that jointly evolves agents' experiential knowledge and their memory architecture, allowing agent systems not only to accumulate experience but also to progressively refine how they learn from it. To ground MemEvolve in prior research and foster openness in future self-evolving systems, we introduce EvolveLab, a unified self-evolving memory codebase that distills twelve representative memory systems into a modular design space (encode, store, retrieve, manage), providing both a standardized implementation substrate and a fair experimental arena. Extensive evaluations on four challenging agentic benchmarks demonstrate that MemEvolve achieves (I) substantial performance gains, improving frameworks such as SmolAgent and Flash-Searcher by up to $17.06\%$; and (II) strong cross-task and cross-LLM generalization, designing memory architectures that transfer effectively across diverse benchmarks and backbone models.



---


# MemFactory: Unified Inference & Training Framework for Agent Memory

**arXiv ID**: 2603.29493
**arXiv URL**: https://arxiv.org/abs/2603.29493

## Abstract

Memory-augmented Large Language Models (LLMs) are essential for developing capable, long-term AI agents. Recently, applying Reinforcement Learning (RL) to optimize memory operations, such as extraction, updating, and retrieval, has emerged as a highly promising research direction. However, existing implementations remain highly fragmented and task-specific, lacking a unified infrastructure to streamline the integration, training, and evaluation of these complex pipelines. To address this gap, we present MemFactory, the first unified, highly modular training and inference framework specifically designed for memory-augmented agents. Inspired by the success of unified fine-tuning frameworks like LLaMA-Factory, MemFactory abstracts the memory lifecycle into atomic, plug-and-play components, enabling researchers to seamlessly construct custom memory agents via a "Lego-like" architecture. Furthermore, the framework natively integrates Group Relative Policy Optimization (GRPO) to fine-tune internal memory management policies driven by multi-dimensional environmental rewards. MemFactory provides out-of-the-box support for recent cutting-edge paradigms, including Memory-R1, RMM, and MemAgent. We empirically validate MemFactory on the open-source MemAgent architecture using its publicly available training and evaluation data. Across the evaluation sets, MemFactory improves performance over the corresponding base models on average, with relative gains of up to 14.8%. By providing a standardized, extensible, and easy-to-use infrastructure, MemFactory significantly lowers the barrier to entry, paving the way for future innovations in memory-driven AI agents.



---


# MemGen: Weaving Generative Latent Memory for Self-Evolving Agents

**arXiv ID**: 2509.24704
**arXiv URL**: https://arxiv.org/abs/2509.24704

## Abstract

Agent memory shapes how Large Language Model (LLM)-powered agents, akin to the human brain, progressively refine themselves through environment interactions. Existing paradigms remain constrained: parametric memory forcibly adjusts model parameters, and retrieval-based memory externalizes experience into structured databases, yet neither captures the fluid interweaving of reasoning and memory that underlies human cognition. To address this gap, we propose MemGen, a dynamic generative memory framework that equips agents with a human-esque cognitive faculty. It consists of a \textit{memory trigger}, which monitors the agent's reasoning state to decide explicit memory invocation, and a \textit{memory weaver}, which takes the agent's current state as stimulus to construct a latent token sequence as machine-native memory to enrich its reasoning. In this way, MemGen enables agents to recall and augment latent memory throughout reasoning, producing a tightly interwoven cycle of memory and cognition. Extensive experiments across eight benchmarks show that MemGen surpasses leading external memory systems such as ExpeL and AWM by up to $38.22\%$, exceeds GRPO by up to $13.44\%$, and exhibits strong cross-domain generalization ability. More importantly, we find that without explicit supervision, MemGen spontaneously evolves distinct human-like memory faculties, including planning memory, procedural memory, and working memory, suggesting an emergent trajectory toward more naturalistic forms of machine cognition.



---


# MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory

**arXiv ID**: 2601.03192
**arXiv URL**: https://arxiv.org/abs/2601.03192

## Abstract

The hallmark of human intelligence is the self-evolving ability to master new skills by learning from past experiences. However, current AI agents struggle to emulate this self-evolution: fine-tuning is computationally expensive and prone to catastrophic forgetting, while existing memory-based methods rely on passive semantic matching that often retrieves noise. To address these challenges, we propose MemRL, a non-parametric approach that evolves via reinforcement learning on episodic memory. By decoupling stable reasoning from plastic memory, MemRL employs a Two-Phase Retrieval mechanism to filter noise and identify high-utility strategies through environmental feedback. Extensive experiments on HLE, BigCodeBench, ALFWorld, and Lifelong Agent Bench demonstrate that MemRL significantly outperforms state-of-the-art baselines, confirming that MemRL effectively reconciles the stability-plasticity dilemma, enabling continuous runtime improvement without weight updates. Code is available at https://github.com/MemTensor/MemRL.



---


# MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents

**arXiv ID**: 2602.02474
**arXiv URL**: https://arxiv.org/abs/2602.02474

## Abstract

Most Large Language Model (LLM) agent memory systems rely on a small set of static, hand-designed operations for extracting memory. These fixed procedures hard-code human priors about what to store and how to revise memory, making them rigid under diverse interaction patterns and inefficient on long histories. To this end, we present \textbf{MemSkill}, which reframes these operations as learnable and evolvable memory skills, structured and reusable routines for extracting, consolidating, and pruning information from interaction traces. Inspired by the design philosophy of agent skills, MemSkill employs a \emph{controller} that learns to select a small set of relevant skills, paired with an LLM-based \emph{executor} that produces skill-guided memories. Beyond learning skill selection, MemSkill introduces a \emph{designer} that periodically reviews hard cases where selected skills yield incorrect or incomplete memories, and evolves the skill set by proposing refinements and new skills. Together, MemSkill forms a closed-loop procedure that improves both the skill-selection policy and the skill set itself. Experiments on LoCoMo, LongMemEval, HotpotQA, and ALFWorld demonstrate that MemSkill improves task performance over strong baselines and generalizes well across settings. Further analyses shed light on how skills evolve, offering insights toward more adaptive, self-evolving memory management for LLM agents.



---


# Memorizing Transformers

**arXiv ID**: 2203.08913
**arXiv URL**: https://arxiv.org/abs/2203.08913

## Abstract

Language models typically need to be trained or finetuned in order to acquire new knowledge, which involves updating their weights. We instead envision language models that can simply read and memorize new data at inference time, thus acquiring new knowledge immediately. In this work, we extend language models with the ability to memorize the internal representations of past inputs. We demonstrate that an approximate kNN lookup into a non-differentiable memory of recent (key, value) pairs improves language modeling across various benchmarks and tasks, including generic webtext (C4), math papers (arXiv), books (PG-19), code (Github), as well as formal theorems (Isabelle). We show that the performance steadily improves when we increase the size of memory up to 262K tokens. On benchmarks including code and mathematics, we find that the model is capable of making use of newly defined functions and theorems during test time.



---


# Memp: Exploring Agent Procedural Memory

**arXiv ID**: 2508.06433
**arXiv URL**: https://arxiv.org/abs/2508.06433

## Abstract

Large Language Models (LLMs) based agents excel at diverse tasks, yet they suffer from brittle procedural memory that is manually engineered or entangled in static parameters. In this work, we investigate strategies to endow agents with a learnable, updatable, and lifelong procedural memory. We propose Memp that distills past agent trajectories into both fine-grained, step-by-step instructions and higher-level, script-like abstractions, and explore the impact of different strategies for Build, Retrieval, and Update of procedural memory. Coupled with a dynamic regimen that continuously updates, corrects, and deprecates its contents, this repository evolves in lockstep with new experience. Empirical evaluation on TravelPlanner and ALFWorld shows that as the memory repository is refined, agents achieve steadily higher success rates and greater efficiency on analogous tasks. Moreover, procedural memory built from a stronger model retains its value: migrating the procedural memory to a weaker model can also yield substantial performance gains. Code is available at https://github.com/zjunlp/MemP.



---


# Meta Context Engineering via Agentic Skill Evolution

**arXiv ID**: 2601.21557
**arXiv URL**: https://arxiv.org/abs/2601.21557

## Abstract

The operational efficacy of large language models relies heavily on their inference-time context. This has established Context Engineering (CE) as a formal discipline for optimizing these inputs. Current CE methods rely on manually crafted harnesses, such as rigid generation-reflection workflows and predefined context schemas. They impose structural biases and restrict context optimization to a narrow, intuition-bound design space. To address this, we introduce Meta Context Engineering (MCE), a bi-level framework that supersedes static CE heuristics by co-evolving CE skills and context artifacts. In MCE iterations, a meta-level agent refines engineering skills via agentic crossover, a deliberative search over the history of skills, their executions, and evaluations. A base-level agent executes these skills, learns from training rollouts, and optimizes context as flexible files and code. We evaluate MCE across five disparate domains under offline and online settings. MCE demonstrates consistent performance gains, achieving 5.6--53.8% relative improvement over state-of-the-art agentic CE methods (mean of 16.9%), while maintaining superior context adaptability, transferability, and efficiency in both context usage and training.



---


# Meta-Policy Reflexion: Reusable Reflective Memory and Rule Admissibility for Resource-Efficient LLM Agent

**arXiv ID**: 2509.03990
**arXiv URL**: https://arxiv.org/abs/2509.03990

## Abstract

Large language model (LLM) agents achieve impressive single-task performance but commonly exhibit repeated failures, inefficient exploration, and limited cross-task adaptability. Existing reflective strategies (e.g., Reflexion, ReAct) improve per-episode behavior but typically produce ephemeral, task-specific traces that are not reused across tasks. Reinforcement-learning based alternatives can produce transferable policies but require substantial parameter updates and compute. In this work we introduce Meta-Policy Reflexion (MPR): a hybrid framework that consolidates LLM-generated reflections into a structured, predicate-like Meta-Policy Memory (MPM) and applies that memory at inference time through two complementary mechanisms soft memory-guided decoding and hard rule admissibility checks(HAC). MPR (i) externalizes reusable corrective knowledge without model weight updates, (ii) enforces domain constraints to reduce unsafe or invalid actions, and (iii) retains the adaptability of language-based reflection. We formalize the MPM representation, present algorithms for update and decoding, and validate the approach in a text-based agent environment following the experimental protocol described in the provided implementation (AlfWorld-based). Empirical results reported in the supplied material indicate consistent gains in execution accuracy and robustness when compared to Reflexion baselines; rule admissibility further improves stability. We analyze mechanisms that explain these gains, discuss scalability and failure modes, and outline future directions for multimodal and multi-agent extensions.



---


# MetaClaw: Just Talk — An Agent That Meta-Learns and Evolves in the Wild

**arXiv ID**: 2603.17187
**arXiv URL**: https://arxiv.org/abs/2603.17187

## Abstract

Large language model (LLM) agents are increasingly used for complex tasks, yet deployed agents often remain static, failing to adapt as user needs evolve. This creates a tension between the need for continuous service and the necessity of updating capabilities to match shifting task distributions. On platforms like OpenClaw, which handle diverse workloads across 20+ channels, existing methods either store raw trajectories without distilling knowledge, maintain static skill libraries, or require disruptive downtime for retraining. We present MetaClaw, a continual meta-learning framework that jointly evolves a base LLM policy and a library of reusable behavioral skills. MetaClaw employs two complementary mechanisms. Skill-driven fast adaptation analyzes failure trajectories via an LLM evolver to synthesize new skills, enabling immediate improvement with zero downtime. Opportunistic policy optimization performs gradient-based updates via cloud LoRA fine-tuning and Reinforcement Learning with a Process Reward Model (RL-PRM). This is triggered during user-inactive windows by the Opportunistic Meta-Learning Scheduler (OMLS), which monitors system inactivity and calendar data. These mechanisms are mutually reinforcing: a refined policy generates better trajectories for skill synthesis, while richer skills provide higher-quality data for policy optimization. To prevent data contamination, a versioning mechanism separates support and query data. Built on a proxy-based architecture, MetaClaw scales to production-size LLMs without local GPUs. Experiments on MetaClaw-Bench and AutoResearchClaw show that skill-driven adaptation improves accuracy by up to 32% relative. The full pipeline advances Kimi-K2.5 accuracy from 21.4% to 40.6% and increases composite robustness by 18.3%. Code is available at https://github.com/aiming-lab/MetaClaw.



---


# Mobile-Agent-v3: Fundamental Agents for GUI Automation

**arXiv ID**: 2508.15144
**arXiv URL**: https://arxiv.org/abs/2508.15144

## Abstract

This paper introduces GUI-Owl, a foundational GUI agent model that achieves state-of-the-art performance among open-source end-to-end models on ten GUI benchmarks across desktop and mobile environments, covering grounding, question answering, planning, decision-making, and procedural knowledge. GUI-Owl-7B achieves 66.4 on AndroidWorld and 29.4 on OSWorld. Building on this, we propose Mobile-Agent-v3, a general-purpose GUI agent framework that further improves performance to 73.3 on AndroidWorld and 37.7 on OSWorld, setting a new state-of-the-art for open-source GUI agent frameworks. GUI-Owl incorporates three key innovations: (1) Large-scale Environment Infrastructure: a cloud-based virtual environment spanning Android, Ubuntu, macOS, and Windows, enabling our Self-Evolving GUI Trajectory Production framework. This generates high-quality interaction data via automated query generation and correctness validation, leveraging GUI-Owl to refine trajectories iteratively, forming a self-improving loop. It supports diverse data pipelines and reduces manual annotation. (2) Diverse Foundational Agent Capabilities: by integrating UI grounding, planning, action semantics, and reasoning patterns, GUI-Owl supports end-to-end decision-making and can act as a modular component in multi-agent systems. (3) Scalable Environment RL: we develop a scalable reinforcement learning framework with fully asynchronous training for real-world alignment. We also introduce Trajectory-aware Relative Policy Optimization (TRPO) for online RL, achieving 34.9 on OSWorld. GUI-Owl and Mobile-Agent-v3 are open-sourced at https://github.com/X-PLUG/MobileAgent.



---


# MobileGUI-RL: Advancing Mobile GUI Agent through Reinforcement Learning in Online Environment

**arXiv ID**: 2507.05720
**arXiv URL**: https://arxiv.org/abs/2507.05720

## Abstract

Recently, there has been a surge of vision-based GUI agents designed to automate everyday mobile and web tasks. These agents interpret raw GUI screenshots and autonomously decide where to click, scroll, or type, which bypasses handcrafted rules and app-specific APIs. However, most existing methods trained GUI agent in the offline environment using pre-collected trajectories. This approach limits scalability, causes overfitting to specific UI templates, and leads to brittle policies when faced with unseen environment. We present MobileGUI-RL, a scalable framework that trains GUI agent in online environment. MobileGUI-RL contains two key components. It (i) synthesizes a curriculum of learnable tasks through self-exploration and filtering, and (ii) adapts GRPO to GUI navigation with trajectory-aware advantages and composite rewards that balance task success and execution efficiency. Experiments on three online mobile-agent benchmarks show consistent gains, validating the effectiveness of our approach.



---


# OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis

**arXiv ID**: 2412.19723
**arXiv URL**: https://arxiv.org/abs/2412.19723

## Abstract

Graphical User Interface (GUI) agents powered by Vision-Language Models (VLMs) have demonstrated human-like computer control capability. Despite their utility in advancing digital automation, a critical bottleneck persists: collecting high-quality trajectory data for training. Common practices for collecting such data rely on human supervision or synthetic data generation through executing pre-defined tasks, which are either resource-intensive or unable to guarantee data quality. Moreover, these methods suffer from limited data diversity and significant gaps between synthetic data and real-world environments. To address these challenges, we propose OS-Genesis, a novel GUI data synthesis pipeline that reverses the conventional trajectory collection process. Instead of relying on pre-defined tasks, OS-Genesis enables agents first to perceive environments and perform step-wise interactions, then retrospectively derive high-quality tasks to enable trajectory-level exploration. A trajectory reward model is then employed to ensure the quality of the generated trajectories. We demonstrate that training GUI agents with OS-Genesis significantly improves their performance on highly challenging online benchmarks. In-depth analysis further validates OS-Genesis's efficiency and its superior data quality and diversity compared to existing synthesis methods. Our codes, data, and checkpoints are available at https://qiushisun.github.io/OS-Genesis-Home/.



---


# OmegaUse: Building a General-Purpose GUI Agent for Autonomous Task Execution

**arXiv ID**: 2601.20380
**arXiv URL**: https://arxiv.org/abs/2601.20380

## Abstract

Graphical User Interface (GUI) agents show great potential for enabling foundation models to complete real-world tasks, revolutionizing human-computer interaction and improving human productivity. In this report, we present OmegaUse, a general-purpose GUI agent model for autonomous task execution on both mobile and desktop platforms, supporting computer-use and phone-use scenarios. Building an effective GUI agent model relies on two factors: (1) high-quality data and (2) effective training methods. To address these, we introduce a carefully engineered data-construction pipeline and a decoupled training paradigm. For data construction, we leverage rigorously curated open-source datasets and introduce a novel automated synthesis framework that integrates bottom-up autonomous exploration with top-down taxonomy-guided generation to create high-fidelity synthetic data. For training, to better leverage these data, we adopt a two-stage strategy: Supervised Fine-Tuning (SFT) to establish fundamental interaction syntax, followed by Group Relative Policy Optimization (GRPO) to improve spatial grounding and sequential planning. To balance computational efficiency with agentic reasoning capacity, OmegaUse is built on a Mixture-of-Experts (MoE) backbone. To evaluate cross-terminal capabilities in an offline setting, we introduce OS-Nav, a benchmark suite spanning multiple operating systems: ChiM-Nav, targeting Chinese Android mobile environments, and Ubu-Nav, focusing on routine desktop interactions on Ubuntu. Extensive experiments show that OmegaUse is highly competitive across established GUI benchmarks, achieving a state-of-the-art (SOTA) score of 96.3% on ScreenSpot-V2 and a leading 79.1% step success rate on AndroidControl. OmegaUse also performs strongly on OS-Nav, reaching 74.24% step success on ChiM-Nav and 55.9% average success on Ubu-Nav.



---


# On-Policy Context Distillation for Language Models

**arXiv ID**: 2602.12275
**arXiv URL**: https://arxiv.org/abs/2602.12275

## Abstract

Context distillation enables language models to internalize in-context knowledge into their parameters. In our work, we propose On-Policy Context Distillation (OPCD), a framework that bridges on-policy distillation with context distillation by training a student model on its own generated trajectories while minimizing reverse Kullback-Leibler divergence against a context-conditioned teacher. We demonstrate the effectiveness of OPCD on two important applications: experiential knowledge distillation, where models extract and consolidate transferable knowledge from their historical solution traces, and system prompt distillation, where models internalize beneficial behaviors encoded in optimized prompts. Across mathematical reasoning, text-based games, and domain-specific tasks, OPCD consistently outperforms baseline methods, achieving higher task accuracy while better preserving out-of-distribution capabilities. We further show that OPCD enables effective cross-size distillation, where smaller student models can internalize experiential knowledge from larger teachers.



---


# On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes

**arXiv ID**: 2306.13649
**arXiv URL**: https://arxiv.org/abs/2306.13649

## Abstract

Knowledge distillation (KD) is widely used for compressing a teacher model to reduce its inference cost and memory footprint, by training a smaller student model. However, current KD methods for auto-regressive sequence models suffer from distribution mismatch between output sequences seen during training and those generated by the student during inference. To address this issue, we introduce Generalized Knowledge Distillation (GKD). Instead of solely relying on a fixed set of output sequences, GKD trains the student on its self-generated output sequences by leveraging feedback from the teacher on such sequences. Unlike supervised KD approaches, GKD also offers the flexibility to employ alternative loss functions between the student and teacher, which can be useful when the student lacks the expressivity to mimic the teacher's distribution. Furthermore, GKD facilitates the seamless integration of distillation with RL fine-tuning (RLHF). We demonstrate the efficacy of GKD for distilling auto-regressive language models on summarization, translation, and arithmetic reasoning tasks, and task-agnostic distillation for instruction-tuning.



---


# One Model, All Roles: Multi-Turn, Multi-Agent Self-Play Reinforcement Learning for Conversational Social Intelligence

**arXiv ID**: 2602.03109
**arXiv URL**: https://arxiv.org/abs/2602.03109

## Abstract

This paper introduces OMAR: One Model, All Roles, a reinforcement learning framework that enables AI to develop social intelligence through multi-turn, multi-agent conversational self-play. Unlike traditional paradigms that rely on static, single-turn optimizations, OMAR allows a single model to role-play all participants in a conversation simultaneously, learning to achieve long-term goals and complex social norms directly from dynamic social interaction. To ensure training stability across long dialogues, we implement a hierarchical advantage estimation that calculates turn-level and token-level advantages. Evaluations in the SOTOPIA social environment and Werewolf strategy games show that our trained models develop fine-grained, emergent social intelligence, such as empathy, persuasion, and compromise seeking, demonstrating the effectiveness of learning collaboration even under competitive scenarios. While we identify practical challenges like reward hacking, our results show that rich social intelligence can emerge without human supervision. We hope this work incentivizes further research on AI social intelligence in group conversations.



---


# Online Experiential Learning for Language Models

**arXiv ID**: 2603.16856
**arXiv URL**: https://arxiv.org/abs/2603.16856

## Abstract

The prevailing paradigm for improving large language models relies on offline training with human annotations or simulated environments, leaving the rich experience accumulated during real-world deployment entirely unexploited. We propose Online Experiential Learning (OEL), a framework that enables language models to continuously improve from their own deployment experience. OEL operates in two stages: first, transferable experiential knowledge is extracted and accumulated from interaction trajectories collected on the user side; second, this knowledge is consolidated into model parameters via on-policy context distillation, requiring no access to the user-side environment. The two stages are iterated to form an online learning loop, where the improved model collects higher-quality trajectories that yield richer experiential knowledge for subsequent rounds. We evaluate OEL on text-based game environments across multiple model scales and both thinking and non-thinking variants. OEL achieves consistent improvements over successive iterations, enhancing both task accuracy and token efficiency while preserving out-of-distribution performance. Our analysis further shows that extracted experiential knowledge is significantly more effective than raw trajectories, and that on-policy consistency between the knowledge source and the policy model is critical for effective learning.



---


# OpenVLA: An Open-Source Vision-Language-Action Model

**arXiv ID**: 2406.09246
**arXiv URL**: https://arxiv.org/abs/2406.09246

## Abstract

Large policies pretrained on a combination of Internet-scale vision-language data and diverse robot demonstrations have the potential to change how we teach robots new skills: rather than training new behaviors from scratch, we can fine-tune such vision-language-action (VLA) models to obtain robust, generalizable policies for visuomotor control. Yet, widespread adoption of VLAs for robotics has been challenging as 1) existing VLAs are largely closed and inaccessible to the public, and 2) prior work fails to explore methods for efficiently fine-tuning VLAs for new tasks, a key component for adoption. Addressing these challenges, we introduce OpenVLA, a 7B-parameter open-source VLA trained on a diverse collection of 970k real-world robot demonstrations. OpenVLA builds on a Llama 2 language model combined with a visual encoder that fuses pretrained features from DINOv2 and SigLIP. As a product of the added data diversity and new model components, OpenVLA demonstrates strong results for generalist manipulation, outperforming closed models such as RT-2-X (55B) by 16.5% in absolute task success rate across 29 tasks and multiple robot embodiments, with 7x fewer parameters. We further show that we can effectively fine-tune OpenVLA for new settings, with especially strong generalization results in multi-task environments involving multiple objects and strong language grounding abilities, and outperform expressive from-scratch imitation learning methods such as Diffusion Policy by 20.4%. We also explore compute efficiency; as a separate contribution, we show that OpenVLA can be fine-tuned on consumer GPUs via modern low-rank adaptation methods and served efficiently via quantization without a hit to downstream success rate. Finally, we release model checkpoints, fine-tuning notebooks, and our PyTorch codebase with built-in support for training VLAs at scale on Open X-Embodiment datasets.



---


# Organizing, Orchestrating, and Benchmarking Agent Skills at Ecosystem Scale

**arXiv ID**: 2603.02176
**arXiv URL**: https://arxiv.org/abs/2603.02176

## Abstract

The rapid proliferation of Claude agent skills has raised the central question of how to effectively leverage, manage, and scale the agent skill ecosystem. In this paper, we propose AgentSkillOS, the first principled framework for skill selection, orchestration, and ecosystem-level management. AgentSkillOS comprises two stages: (i) Manage Skills, which organizes skills into a capability tree via node-level recursive categorization for efficient discovery; and (ii) Solve Tasks, which retrieves, orchestrates, and executes multiple skills through DAG-based pipelines. To evaluate the agent's ability to invoke skills, we construct a benchmark of 30 artifact-rich tasks across five categories: data computation, document creation, motion video, visual design, and web interaction. We assess the quality of task outputs using LLM-based pairwise evaluation, and the results are aggregated via a Bradley-Terry model to produce unified quality scores. Experiments across three skill ecosystem scales (200 to 200K skills) show that tree-based retrieval effectively approximates oracle skill selection, and that DAG-based orchestration substantially outperforms native flat invocation even when given the identical skill set. Our findings confirm that structured composition is the key to unlocking skill potential. Our GitHub repository is available at:https://github.com/ynulihao/AgentSkillOS.



---


# PRL: Process Reward Learning Improves LLMs' Reasoning Ability and Broadens the Reasoning Boundary

**arXiv ID**: 2601.10201
**arXiv URL**: https://arxiv.org/abs/2601.10201

## Abstract

Improving the reasoning abilities of Large Language Models (LLMs) has been a continuous topic recently. But most relevant works are based on outcome rewards at the trajectory level, missing fine-grained supervision during the reasoning process. Other existing training frameworks that try to combine process signals together to optimize LLMs also rely heavily on tedious additional steps like MCTS, training a separate reward model, etc., doing harm to the training efficiency. Moreover, the intuition behind the process signals design lacks rigorous theoretical support, leaving the understanding of the optimization mechanism opaque. In this paper, we propose Process Reward Learning (PRL), which decomposes the entropy regularized reinforcement learning objective into intermediate steps, with rigorous process rewards that could be assigned to models accordingly. Starting from theoretical motivation, we derive the formulation of PRL that is essentially equivalent to the objective of reward maximization plus a KL-divergence penalty term between the policy model and a reference model. However, PRL could turn the outcome reward into process supervision signals, which helps better guide the exploration during RL optimization. From our experiment results, we demonstrate that PRL not only improves the average performance for LLMs' reasoning ability measured by average @ n, but also broadens the reasoning boundary by improving the pass @ n metric. Extensive experiments show the effectiveness of PRL could be verified and generalized.



---


# PROPA: Toward Process-level Optimization in Visual Reasoning via Reinforcement Learning

**arXiv ID**: 2511.10279
**arXiv URL**: https://arxiv.org/abs/2511.10279

## Abstract

Despite significant progress, Vision-Language Models (VLMs) still struggle with complex visual reasoning, where multi-step dependencies cause early errors to cascade through the reasoning chain. Existing post-training paradigms are limited: Supervised Fine-Tuning (SFT) relies on costly step-level annotations, while Reinforcement Learning with Verifiable Rewards (RLVR) methods like GRPO provide only sparse, outcome-level feedback, hindering stable optimization. We introduce PROPA (Process-level Reasoning Optimization with interleaved Policy Alignment), a novel framework that integrates Monte Carlo Tree Search (MCTS) with GRPO to generate dense, process-level rewards and optimize reasoning at each intermediate step without human annotations. To overcome the cold-start problem, PROPA interleaves GRPO updates with SFT, enabling the model to learn from both successful and failed reasoning trajectories. A Process Reward Model (PRM) is further trained to guide inference-time search, aligning the test-time search with the training signal. Across seven benchmarks and four VLM backbones, PROPA consistently outperforms both SFT- and RLVR-based baselines. It achieves up to 17.0% gains on in-domain tasks and 21.0% gains on out-of-domain tasks compared to existing state-of-the-art, establishing a strong reasoning and generalization capability for visual reasoning tasks. The code isavailable at: https://github.com/YanbeiJiang/PROPA.



---


# ProcMEM: Learning Reusable Procedural Memory from Experience via Non-Parametric PPO for LLM Agents

**arXiv ID**: 2602.01869
**arXiv URL**: https://arxiv.org/abs/2602.01869

## Abstract

LLM-driven agents demonstrate strong performance in sequential decision-making but often rely on on-the-fly reasoning, re-deriving solutions even in recurring scenarios. This insufficient experience reuse leads to computational redundancy and execution instability. To bridge this gap, we propose ProcMEM, a framework that enables agents to autonomously learn procedural memory from interaction experiences without parameter updates. By formalizing a Skill-MDP, ProcMEM transforms passive episodic narratives into executable Skills defined by activation, execution, and termination conditions to ensure executability. To achieve reliable reusability without capability degradation, we introduce Non-Parametric PPO, which leverages semantic gradients for high-quality candidate generation and a PPO Gate for robust Skill verification. Through score-based maintenance, ProcMEM sustains compact, high-quality procedural memory. Experimental results across in-domain, cross-task, and cross-agent scenarios demonstrate that ProcMEM achieves superior reuse rates and significant performance gains with extreme memory compression. Visualized evolutionary trajectories and Skill distributions further reveal how ProcMEM transparently accumulates, refines, and reuses procedural knowledge to facilitate long-term autonomy.



---


# R4: Retrieval-Augmented Reasoning for Vision-Language Models in 4D Spatio-Temporal Space

**arXiv ID**: 2512.15940
**arXiv URL**: https://arxiv.org/abs/2512.15940

## Abstract

Humans perceive and reason about their surroundings in four dimensions by building persistent, structured internal representations that encode semantic meaning, spatial layout, and temporal dynamics. These multimodal memories enable them to recall past events, infer unobserved states, and integrate new information into context-dependent reasoning. Inspired by this capability, we introduce R4, a training-free framework for retrieval-augmented reasoning in 4D spatio-temporal space that equips vision-language models (VLMs) with structured, lifelong memory. R4 continuously constructs a 4D knowledge database by anchoring object-level semantic descriptions in metric space and time, yielding a persistent world model that can be shared across agents. At inference, natural language queries are decomposed into semantic, spatial, and temporal keys to retrieve relevant observations, which are integrated into the VLM's reasoning. Unlike classical retrieval-augmented generation methods, retrieval in R4 operates directly in 4D space, enabling episodic and collaborative reasoning without training. Experiments on embodied question answering and navigation benchmarks demonstrate that R4 substantially improves retrieval and reasoning over spatio-temporal information compared to baselines, advancing a new paradigm for embodied 4D reasoning in dynamic environments.



---


# ReAct: Synergizing Reasoning and Acting in Language Models

**arXiv ID**: 2210.03629
**arXiv URL**: https://arxiv.org/abs/2210.03629

## Abstract

While large language models (LLMs) have demonstrated impressive capabilities across tasks in language understanding and interactive decision making, their abilities for reasoning (e.g. chain-of-thought prompting) and acting (e.g. action plan generation) have primarily been studied as separate topics. In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with external sources, such as knowledge bases or environments, to gather additional information. We apply our approach, named ReAct, to a diverse set of language and decision making tasks and demonstrate its effectiveness over state-of-the-art baselines, as well as improved human interpretability and trustworthiness over methods without reasoning or acting components. Concretely, on question answering (HotpotQA) and fact verification (Fever), ReAct overcomes issues of hallucination and error propagation prevalent in chain-of-thought reasoning by interacting with a simple Wikipedia API, and generates human-like task-solving trajectories that are more interpretable than baselines without reasoning traces. On two interactive decision making benchmarks (ALFWorld and WebShop), ReAct outperforms imitation and reinforcement learning methods by an absolute success rate of 34% and 10% respectively, while being prompted with only one or two in-context examples. Project site with code: https://react-lm.github.io



---


# ReCAP: Recursive Context-Aware Reasoning and Planning for Large Language Model Agents

**arXiv ID**: 2510.23822
**arXiv URL**: https://arxiv.org/abs/2510.23822

## Abstract

Long-horizon tasks requiring multi-step reasoning and dynamic re-planning remain challenging for large language models (LLMs). Sequential prompting methods are prone to context drift, loss of goal information, and recurrent failure cycles, while hierarchical prompting methods often weaken cross-level continuity or incur substantial runtime overhead. We introduce ReCAP (Recursive Context-Aware Reasoning and Planning), a hierarchical framework with shared context for reasoning and planning in LLMs. ReCAP combines three key mechanisms: (i) plan-ahead decomposition, in which the model generates a full subtask list, executes the first item, and refines the remainder; (ii) structured re-injection of parent plans, maintaining consistent multi-level context during recursive return; and (iii) memory-efficient execution, bounding the active prompt so costs scale linearly with task depth. Together these mechanisms align high-level goals with low-level actions, reduce redundant prompting, and preserve coherent context updates across recursion. Experiments demonstrate that ReCAP substantially improves subgoal alignment and success rates on various long-horizon reasoning benchmarks, achieving a 32% gain on synchronous Robotouille and a 29% improvement on asynchronous Robotouille under the strict pass@1 protocol.



---


# ReCreate: Reasoning and Creating Domain Agents Driven by Experience

**arXiv ID**: 2601.11100
**arXiv URL**: https://arxiv.org/abs/2601.11100

## Abstract

Large Language Model agents are reshaping the industrial landscape. However, most practical agents remain human-designed because tasks differ widely, making them labor-intensive to build. This situation poses a central question: can we automatically create and adapt domain agents in the wild? While several recent approaches have sought to automate agent creation, they typically treat agent generation as a black-box procedure and rely solely on final performance metrics to guide the process. Such strategies overlook critical evidence explaining why an agent succeeds or fails, and often require high computational costs. To address these limitations, we propose ReCreate, an experience-driven framework for the automatic creation of domain agents. ReCreate systematically leverages agent interaction histories, which provide rich concrete signals on both the causes of success or failure and the avenues for improvement. Specifically, we introduce an agent-as-optimizer paradigm that effectively learns from experience via three key components: (i) an experience storage and retrieval mechanism for on-demand inspection; (ii) a reasoning-creating synergy pipeline that maps execution experience into scaffold edits; and (iii) hierarchical updates that abstract instance-level details into reusable domain patterns. In experiments across diverse domains, ReCreate consistently outperforms human-designed agents and existing automated agent generation methods, even when starting from minimal seed scaffolds.



---


# ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search

**arXiv ID**: 2406.03816
**arXiv URL**: https://arxiv.org/abs/2406.03816

## Abstract

Recent methodologies in LLM self-training mostly rely on LLM generating responses and filtering those with correct output answers as training data. This approach often yields a low-quality fine-tuning training set (e.g., incorrect plans or intermediate reasoning). In this paper, we develop a reinforced self-training approach, called ReST-MCTS*, based on integrating process reward guidance with tree search MCTS* for collecting higher-quality reasoning traces as well as per-step value to train policy and reward models. ReST-MCTS* circumvents the per-step manual annotation typically used to train process rewards by tree-search-based reinforcement learning: Given oracle final correct answers, ReST-MCTS* is able to infer the correct process rewards by estimating the probability this step can help lead to the correct answer. These inferred rewards serve dual purposes: they act as value targets for further refining the process reward model and also facilitate the selection of high-quality traces for policy model self-training. We first show that the tree-search policy in ReST-MCTS* achieves higher accuracy compared with prior LLM reasoning baselines such as Best-of-N and Tree-of-Thought, within the same search budget. We then show that by using traces searched by this tree-search policy as training data, we can continuously enhance the three language models for multiple iterations, and outperform other self-training algorithms such as ReST$^\text{EM}$ and Self-Rewarding LM. We release all code at https://github.com/THUDM/ReST-MCTS.



---


# ReTool: Reinforcement Learning for Strategic Tool Use in LLMs

**arXiv ID**: 2504.11536
**arXiv URL**: https://arxiv.org/abs/2504.11536

## Abstract

While reasoning models (e.g., DeepSeek R1) trained with reinforcement learning (RL), excel in textual reasoning, they struggle in scenarios requiring structured problem-solving, such as geometric reasoning, concise computation, or complex equation solving-areas where computational tools like code interpreters (CI) demonstrate distinct advantages. To bridge this gap, we propose ReTool, which enhances long-form reasoning with tool-integrated learning, including two key features: (1) dynamic interleaving of real-time code execution within natural language reasoning processes, and (2) an automated RL paradigm that allows policy rollouts with multi-turn real-time code execution and teaches the model in learning when and how to invoke tools based on outcome feedback. ReTool employs a systematic training framework, beginning with synthetic cold-start data generation to produce code-augmented long-form reasoning traces for fine-tuning base models. Subsequent RL training leverages task outcomes as rewards to iteratively refine the model's tool use strategy, enabling autonomous discovery of optimal tool invocation patterns without human priors. Experiments on the challenging MATH Olympiad benchmark AIME demonstrate ReTool's superiority: Our 32B model achieves 67% accuracy with 400 training steps, outperforming text-based RL baseline (40% accuracy, 1080 steps) in efficiency and performance. Remarkably, ReTool-32B attains 72.5% accuracy in extended settings, surpassing OpenAI's o1-preview by 27.9%. Further analysis reveals emergent behaviors such as code self-correction, signaling an ''aha moment'' in which the model autonomously masters adaptive tool use. These findings highlight the promise of outcome-driven tool integration for advancing complex mathematical reasoning and offer new insights into hybrid neuro-symbolic systems.



---


# ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory

**arXiv ID**: 2509.25140
**arXiv URL**: https://arxiv.org/abs/2509.25140

## Abstract

With the growing adoption of large language model agents in persistent real-world roles, they naturally encounter continuous streams of tasks. A key limitation, however, is their failure to learn from the accumulated interaction history, forcing them to discard valuable insights and repeat past errors. We propose ReasoningBank, a novel memory framework that distills generalizable reasoning strategies from an agent's self-judged successful and failed experiences. At test time, an agent retrieves relevant memories from ReasoningBank to inform its interaction and then integrates new learnings back, enabling it to become more capable over time. Building on this powerful experience learner, we further introduce memory-aware test-time scaling (MaTTS), which accelerates and diversifies this learning process by scaling up the agent's interaction experience. By allocating more compute to each task, the agent generates abundant, diverse experiences that provide rich contrastive signals for synthesizing higher-quality memory. The better memory in turn guides more effective scaling, establishing a powerful synergy between memory and test-time scaling. Across web browsing and software engineering benchmarks, ReasoningBank consistently outperforms existing memory mechanisms that store raw trajectories or only successful task routines, improving both effectiveness and efficiency; MaTTS further amplifies these gains. These findings establish memory-driven experience scaling as a new scaling dimension, enabling agents to self-evolve with emergent behaviors naturally arise. Our code can be found at https://github.com/google-research/reasoning-bank.



---


# Reflection-Driven Control for Trustworthy Code Agents

**arXiv ID**: 2512.21354
**arXiv URL**: https://arxiv.org/abs/2512.21354

## Abstract

Contemporary large language model (LLM) agents are remarkably capable, but they still lack reliable safety controls and can produce unconstrained, unpredictable, and even actively harmful outputs. To address this, we introduce Reflection-Driven Control, a standardized and pluggable control module that can be seamlessly integrated into general agent architectures. Reflection-Driven Control elevates "self-reflection" from a post hoc patch into an explicit step in the agent's own reasoning process: during generation, the agent continuously runs an internal reflection loop that monitors and evaluates its own decision path. When potential risks are detected, the system retrieves relevant repair examples and secure coding guidelines from an evolving reflective memory, injecting these evidence-based constraints directly into subsequent reasoning steps. We instantiate Reflection-Driven Control in the setting of secure code generation and systematically evaluate it across eight classes of security-critical programming tasks. Empirical results show that Reflection-Driven Control substantially improves the security and policy compliance of generated code while largely preserving functional correctness, with minimal runtime and token overhead. Taken together, these findings indicate that Reflection-Driven Control is a practical path toward trustworthy AI coding agents: it enables designs that are simultaneously autonomous, safer by construction, and auditable.



---


# Reflection-Driven Self-Optimization 6G Agentic AI RAN via Simulation-in-the-Loop Workflows

**arXiv ID**: 2512.20640
**arXiv URL**: https://arxiv.org/abs/2512.20640

## Abstract

The escalating complexity of sixth-generation (6G) networks demands unprecedented levels of autonomy beyond the capabilities of traditional optimization-based and current AI-based resource management approaches. While agentic AI has emerged as a promising paradigm for autonomous RAN, current frameworks provide sophisticated reasoning capabilities but lack mechanisms for empirical validation and self-improvement. This article identifies simulation-in-the-loop validation as a critical enabler for truly autonomous networks, where AI agents can empirically verify decisions and learn from outcomes. We present the first reflection-driven self-optimization framework that integrates agentic AI with high-fidelity network simulation in a closed-loop architecture. Our system orchestrates four specialized agents, including scenario, solver, simulation, and reflector agents, working in concert to transform agentic AI into a self-correcting system capable of escaping local optima, recognizing implicit user intent, and adapting to dynamic network conditions. Extensive experiments validate significant performance improvements over non-agentic approaches: 17.1\% higher throughput in interference optimization, 67\% improved user QoS satisfaction through intent recognition, and 25\% reduced resource utilization during low-traffic periods while maintaining service quality.



---


# Reflective Planning: Vision-Language Models for Multi-Stage Long-Horizon Robotic Manipulation

**arXiv ID**: 2502.16707
**arXiv URL**: https://arxiv.org/abs/2502.16707

## Abstract

Solving complex long-horizon robotic manipulation problems requires sophisticated high-level planning capabilities, the ability to reason about the physical world, and reactively choose appropriate motor skills. Vision-language models (VLMs) pretrained on Internet data could in principle offer a framework for tackling such problems. However, in their current form, VLMs lack both the nuanced understanding of intricate physics required for robotic manipulation and the ability to reason over long horizons to address error compounding issues. In this paper, we introduce a novel test-time computation framework that enhances VLMs' physical reasoning capabilities for multi-stage manipulation tasks. At its core, our approach iteratively improves a pretrained VLM with a "reflection" mechanism - it uses a generative model to imagine future world states, leverages these predictions to guide action selection, and critically reflects on potential suboptimalities to refine its reasoning. Experimental results demonstrate that our method significantly outperforms several state-of-the-art commercial VLMs as well as other post-training approaches such as Monte Carlo Tree Search (MCTS). Videos are available at https://reflect-vlm.github.io.



---


# Reflexion: Language Agents with Verbal Reinforcement Learning

**arXiv ID**: 2303.11366
**arXiv URL**: https://arxiv.org/abs/2303.11366

## Abstract

Large language models (LLMs) have been increasingly used to interact with external environments (e.g., games, compilers, APIs) as goal-driven agents. However, it remains challenging for these language agents to quickly and efficiently learn from trial-and-error as traditional reinforcement learning methods require extensive training samples and expensive model fine-tuning. We propose Reflexion, a novel framework to reinforce language agents not by updating weights, but instead through linguistic feedback. Concretely, Reflexion agents verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer to induce better decision-making in subsequent trials. Reflexion is flexible enough to incorporate various types (scalar values or free-form language) and sources (external or internally simulated) of feedback signals, and obtains significant improvements over a baseline agent across diverse tasks (sequential decision-making, coding, language reasoning). For example, Reflexion achieves a 91% pass@1 accuracy on the HumanEval coding benchmark, surpassing the previous state-of-the-art GPT-4 that achieves 80%. We also conduct ablation and analysis studies using different feedback signals, feedback incorporation methods, and agent types, and provide insights into how they affect performance.



---


# Regularizing Hidden States Enables Learning Generalizable Reward Model for LLMs

**arXiv ID**: 2406.10216
**arXiv URL**: https://arxiv.org/abs/2406.10216

## Abstract

Reward models trained on human preference data have been proven to effectively align Large Language Models (LLMs) with human intent within the framework of reinforcement learning from human feedback (RLHF). However, current reward models have limited generalization capabilities to unseen prompts and responses, which can lead to an unexpected phenomenon known as reward over-optimization, resulting in a decline in actual performance due to excessive optimization of rewards. While previous research has advocated for constraining policy optimization, our study introduces a novel approach to enhance the reward model's generalization ability against distribution shifts by regularizing the hidden states. Specifically, we retain the base model's language model head and incorporate a suite of text-generation losses to preserve the hidden states' text-generation capabilities, while concurrently learning a reward head behind the same hidden states. Our experimental results demonstrate that the introduced regularization technique markedly improves the accuracy of learned reward models across a variety of out-of-distribution (OOD) tasks and effectively alleviates the over-optimization issue in RLHF, offering a more reliable and robust preference learning paradigm.



---


# Reinforcement Learning for Self-Improving Agent with Skill Library

**arXiv ID**: 2512.17102
**arXiv URL**: https://arxiv.org/abs/2512.17102

## Abstract

Large Language Model (LLM)-based agents have demonstrated remarkable capabilities in complex reasoning and multi-turn interactions but struggle to continuously improve and adapt when deployed in new environments. One promising approach is implementing skill libraries that allow agents to learn, validate, and apply new skills. However, current skill library approaches rely primarily on LLM prompting, making consistent skill library implementation challenging. To overcome these challenges, we propose a Reinforcement Learning (RL)-based approach to enhance agents' self-improvement capabilities with a skill library. Specifically, we introduce Skill Augmented GRPO for self-Evolution (SAGE), a novel RL framework that systematically incorporates skills into learning. The framework's key component, Sequential Rollout, iteratively deploys agents across a chain of similar tasks for each rollout. As agents navigate through the task chain, skills generated from previous tasks accumulate in the library and become available for subsequent tasks. Additionally, the framework enhances skill generation and utilization through a Skill-integrated Reward that complements the original outcome-based rewards. Experimental results on AppWorld demonstrate that SAGE, when applied to supervised-finetuned model with expert experience, achieves 8.9% higher Scenario Goal Completion while requiring 26% fewer interaction steps and generating 59% fewer tokens, substantially outperforming existing approaches in both accuracy and efficiency.



---


# Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution

**arXiv ID**: 2512.10696
**arXiv URL**: https://arxiv.org/abs/2512.10696

## Abstract

Procedural memory enables large language model (LLM) agents to internalize "how-to" knowledge, theoretically reducing redundant trial-and-error. However, existing frameworks predominantly suffer from a "passive accumulation" paradigm, treating memory as a static append-only archive. To bridge the gap between static storage and dynamic reasoning, we propose $\textbf{ReMe}$ ($\textit{Remember Me, Refine Me}$), a comprehensive framework for experience-driven agent evolution. ReMe innovates across the memory lifecycle via three mechanisms: 1) $\textit{multi-faceted distillation}$, which extracts fine-grained experiences by recognizing success patterns, analyzing failure triggers and generating comparative insights; 2) $\textit{context-adaptive reuse}$, which tailors historical insights to new contexts via scenario-aware indexing; and 3) $\textit{utility-based refinement}$, which autonomously adds valid memories and prunes outdated ones to maintain a compact, high-quality experience pool. Extensive experiments on BFCL-V3 and AppWorld demonstrate that ReMe establishes a new state-of-the-art in agent memory system. Crucially, we observe a significant memory-scaling effect: Qwen3-8B equipped with ReMe outperforms larger, memoryless Qwen3-14B, suggesting that self-evolving memory provides a computation-efficient pathway for lifelong learning. We release our code and the $\texttt{reme.library}$ dataset to facilitate further research.



---


# Retrieval-Augmented LLM Agents: Learning to Learn from Experience

**arXiv ID**: 2603.18272
**arXiv URL**: https://arxiv.org/abs/2603.18272

## Abstract

While large language models (LLMs) have advanced the development of general-purpose agents, achieving robust generalization to unseen tasks remains a significant challenge. Current approaches typically rely on either fine-tuning or training-free memory-augmented generation using retrieved experience; yet both have limitations: fine-tuning often fails to extrapolate to new tasks, while experience retrieval often underperforms compared to supervised baselines. In this work, we propose to combine these approaches and systematically study how to train retrieval-augmented LLM agents to effectively leverage retrieved trajectories in-context. First, we establish a robust supervised fine-tuning (SFT) recipe using LoRA that outperforms several state-of-the-art agent training pipelines. Second, we provide a detailed analysis of key design choices for experience retrieval, identifying optimal strategies for storage, querying, and trajectory selection. Finally, we propose a pipeline that integrates experience retrieval into the fine-tuning process. Our results demonstrate that this combined approach significantly improves generalization to unseen tasks, providing a scalable and effective framework for building agents that learn to learn from experience.



---


# Reward-SQL: Boosting Text-to-SQL via Stepwise Reasoning and Process-Supervised Rewards

**arXiv ID**: 2505.04671
**arXiv URL**: https://arxiv.org/abs/2505.04671

## Abstract

Recent advances in large language models (LLMs) have significantly improved performance on the Text-to-SQL task by leveraging their powerful reasoning capabilities. To enhance accuracy during the reasoning process, external Process Reward Models (PRMs) can be introduced during training and inference to provide fine-grained supervision. However, if misused, PRMs may distort the reasoning trajectory and lead to suboptimal or incorrect SQL generation. To address this challenge, we propose Reward-SQL, a framework that systematically explores how to incorporate PRMs into the Text-to-SQL reasoning process effectively. Our approach follows a "cold start, then PRM supervision" paradigm. Specifically, we first train the model to decompose SQL queries into structured stepwise reasoning chains using common table expressions (Chain-of-CTEs), establishing a strong and interpretable reasoning baseline. Then, we investigate four strategies for integrating PRMs, and find that combining PRM as an online training signal (e.g.,GRPO) with PRM-guided inference (e.g., best-of-N sampling) yields the best results. Empirically, on the BIRD benchmark, Reward-SQL enables models supervised by PRM (7B) to achieve a 13.1% performance gain across various guidance strategies. Notably, our GRPO-aligned policy model based on Qwen2.5-Coder-7B-Instruct achieves 68.9% accuracy on the BIRD development set, outperforming all baseline methods under the same model size. These results demonstrate the effectiveness of Reward-SQL in leveraging reward-based supervision for Text-to-SQL reasoning.



---


# SAMULE: Self-Learning Agents Enhanced by Multi-level Reflection

**arXiv ID**: 2509.20562
**arXiv URL**: https://arxiv.org/abs/2509.20562

## Abstract

Despite the rapid advancements in LLM agents, they still face the challenge of generating meaningful reflections due to inadequate error analysis and a reliance on rare successful trajectories, especially in complex tasks. In this work, we propose SAMULE, a new framework for self-learning agents powered by a retrospective language model that is trained based on Multi-Level Reflection Synthesis. It first synthesizes high-quality reflections across three complementary levels: Single-Trajectory Learning (micro-level) for detailed error correction; Intra-Task Learning (meso-level) to build error taxonomies across multiple trials of the same task, and Inter-Task Learning (macro-level) to extract transferable insights based on same typed errors from diverse task failures. Then we fine-tune a language model serving as the retrospective model to generate reflections during inference. We further extend our framework to interactive settings through a foresight-based reflection mechanism, enabling agents to proactively reflect and adapt during user interactions by comparing predicted and actual responses. Extensive experiments on three challenging benchmarks - TravelPlanner, NATURAL PLAN, and Tau-bench - demonstrate that our approach significantly outperforms reflection-based baselines. Our results highlight the critical role of well-designed reflection synthesis and failure-centric learning in building self-improving LLM agents.



---


# SCAN: Self-Denoising Monte Carlo Annotation for Robust Process Reward Learning

**arXiv ID**: 2509.16548
**arXiv URL**: https://arxiv.org/abs/2509.16548

## Abstract

Process reward models (PRMs) offer fine-grained, step-level evaluations that facilitate deeper reasoning processes in large language models (LLMs), proving effective in complex tasks like mathematical reasoning. However, developing PRMs is challenging due to the high cost and limited scalability of human-annotated data. Synthetic data from Monte Carlo (MC) estimation is a promising alternative but suffers from a high noise ratio, which can cause overfitting and hinder large-scale training. In this work, we conduct a preliminary study on the noise distribution in synthetic data from MC estimation, identifying that annotation models tend to both underestimate and overestimate step correctness due to limitations in their annotation capabilities. Building on these insights, we propose Self-Denoising Monte Carlo Annotation (SCAN), an efficient data synthesis and noise-tolerant learning framework. Our key findings indicate that: (1) Even lightweight models (e.g., 1.5B parameters) can produce high-quality annotations through a self-denoising strategy, enabling PRMs to achieve superior performance with only 6% the inference cost required by vanilla MC estimation. (2) With our robust learning strategy, PRMs can effectively learn from this weak supervision, achieving a 39.2 F1 score improvement (from 19.9 to 59.1) in ProcessBench. Despite using only a compact synthetic dataset, our models surpass strong baselines, including those trained on large-scale human-annotated datasets such as PRM800K. Furthermore, performance continues to improve as we scale up the synthetic data, highlighting the potential of SCAN for scalable, cost-efficient, and robust PRM training.



---


# SE-Agent: Self-Evolution Trajectory Optimization in Multi-Step Reasoning with LLM-Based Agents

**arXiv ID**: 2508.02085
**arXiv URL**: https://arxiv.org/abs/2508.02085

## Abstract

Large Language Model (LLM)-based agents have recently shown impressive capabilities in complex reasoning and tool use via multi-step interactions with their environments. While these agents have the potential to tackle complicated tasks, their problem-solving process, i.e., agents' interaction trajectory leading to task completion, remains underexploited. These trajectories contain rich feedback that can navigate agents toward the right directions for solving problems correctly. Although prevailing approaches, such as Monte Carlo Tree Search (MCTS), can effectively balance exploration and exploitation, they ignore the interdependence among various trajectories and lack the diversity of search spaces, which leads to redundant reasoning and suboptimal outcomes. To address these challenges, we propose SE-Agent, a Self-Evolution framework that enables Agents to optimize their reasoning processes iteratively. Our approach revisits and enhances former pilot trajectories through three key operations: revision, recombination, and refinement. This evolutionary mechanism enables two critical advantages: (1) it expands the search space beyond local optima by intelligently exploring diverse solution paths guided by previous trajectories, and (2) it leverages cross-trajectory inspiration to efficiently enhance performance while mitigating the impact of suboptimal reasoning paths. Through these mechanisms, SE-Agent achieves continuous self-evolution that incrementally improves reasoning quality. We evaluate SE-Agent on SWE-bench Verified to resolve real-world GitHub issues. Experimental results across five strong LLMs show that integrating SE-Agent delivers up to 55% relative improvement, achieving state-of-the-art performance among all open-source agents on SWE-bench Verified. Our code and demonstration materials are publicly available at https://github.com/JARVIS-Xs/SE-Agent.



---


# SEAL: Self-Evolving Agentic Learning for Conversational Question Answering over Knowledge Graphs

**arXiv ID**: 2512.04868
**arXiv URL**: https://arxiv.org/abs/2512.04868

## Abstract

Knowledge-based conversational question answering (KBCQA) confronts persistent challenges in resolving coreference, modeling contextual dependencies, and executing complex logical reasoning. Existing approaches, whether end-to-end semantic parsing or stepwise agent-based reasoning, often suffer from structural inaccuracies and prohibitive computational costs, particularly when processing intricate queries over large knowledge graphs. To address these limitations, we introduce SEAL, a novel two-stage semantic parsing framework grounded in self-evolving agentic learning. In the first stage, a large language model (LLM) extracts a minimal S-expression core that captures the essential semantics of the input query. This core is then refined by an agentic calibration module, which corrects syntactic inconsistencies and aligns entities and relations precisely with the underlying knowledge graph. The second stage employs template-based completion, guided by question-type prediction and placeholder instantiation, to construct a fully executable S-expression. This decomposition not only simplifies logical form generation but also significantly enhances structural fidelity and linking efficiency. Crucially, SEAL incorporates a self-evolving mechanism that integrates local and global memory with a reflection module, enabling continuous adaptation from dialog history and execution feedback without explicit retraining. Extensive experiments on the SPICE benchmark demonstrate that SEAL achieves state-of-the-art performance, especially in multi-hop reasoning, comparison, and aggregation tasks. The results validate notable gains in both structural accuracy and computational efficiency, underscoring the framework's capacity for robust and scalable conversational reasoning.



---


# SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from Experience

**arXiv ID**: 2508.04700
**arXiv URL**: https://arxiv.org/abs/2508.04700

## Abstract

Repurposing large vision-language models (LVLMs) as computer use agents (CUAs) has led to substantial breakthroughs, primarily driven by human-labeled data. However, these models often struggle with novel and specialized software, particularly in scenarios lacking human annotations. To address this challenge, we propose SEAgent, an agentic self-evolving framework enabling CUAs to autonomously evolve through interactions with unfamiliar software. Specifically, SEAgent empowers computer-use agents to autonomously master novel software environments via experiential learning, where agents explore new software, learn through iterative trial-and-error, and progressively tackle auto-generated tasks organized from simple to complex. To achieve this goal, we design a World State Model for step-wise trajectory assessment, along with a Curriculum Generator that generates increasingly diverse and challenging tasks. The agent's policy is updated through experiential learning, comprised of adversarial imitation of failure actions and Group Relative Policy Optimization (GRPO) on successful ones. Furthermore, we introduce a specialist-to-generalist training strategy that integrates individual experiential insights from specialist agents, facilitating the development of a stronger generalist CUA capable of continuous autonomous evolution. This unified agent ultimately achieves performance surpassing ensembles of individual specialist agents on their specialized software. We validate the effectiveness of SEAgent across five novel software environments within OS-World. Our approach achieves a significant improvement of 23.2% in success rate, from 11.3% to 34.5%, over a competitive open-source CUA, i.e., UI-TARS.



---


# SGMem: Sentence Graph Memory for Long-Term Conversational Agents

**arXiv ID**: 2509.21212
**arXiv URL**: https://arxiv.org/abs/2509.21212

## Abstract

Long-term conversational agents require effective memory management to handle dialogue histories that exceed the context window of large language models (LLMs). Existing methods based on fact extraction or summarization reduce redundancy but struggle to organize and retrieve relevant information across different granularities of dialogue and generated memory. We introduce SGMem (Sentence Graph Memory), which represents dialogue as sentence-level graphs within chunked units, capturing associations across turn-, round-, and session-level contexts. By combining retrieved raw dialogue with generated memory such as summaries, facts and insights, SGMem supplies LLMs with coherent and relevant context for response generation. Experiments on LongMemEval and LoCoMo show that SGMem consistently improves accuracy and outperforms strong baselines in long-term conversational question answering.



---


# SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization

**arXiv ID**: 2604.02268
**arXiv URL**: https://arxiv.org/abs/2604.02268

## Abstract

Agent skills, structured packages of procedural knowledge and executable resources that agents dynamically load at inference time, have become a reliable mechanism for augmenting LLM agents. Yet inference-time skill augmentation is fundamentally limited: retrieval noise introduces irrelevant guidance, injected skill content imposes substantial token overhead, and the model never truly acquires the knowledge it merely follows. We ask whether skills can instead be internalized into model parameters, enabling zero-shot autonomous behavior without any runtime skill retrieval. We introduce SKILL0, an in-context reinforcement learning framework designed for skill internalization. SKILL0 introduces a training-time curriculum that begins with full skill context and progressively withdraws it. Skills are grouped offline by category and rendered with interaction history into a compact visual context, teaching he model tool invocation and multi-turn task completion. A Dynamic Curriculum then evaluates each skill file's on-policy helpfulness, retaining only those from which the current policy still benefits within a linearly decaying budget, until the agent operates in a fully zero-shot setting. Extensive agentic experiments demonstrate that SKILL0 achieves substantial improvements over the standard RL baseline (+9.7\% for ALFWorld and +6.6\% for Search-QA), while maintaining a highly efficient context of fewer than 0.5k tokens per step. Our code is available at https://github.com/ZJU-REAL/SkillZero.



---


# SKILLFOUNDRY: Building Self-Evolving Agent Skill Libraries from Heterogeneous Scientific Resources

**arXiv ID**: 2604.03964
**arXiv URL**: https://arxiv.org/abs/2604.03964

## Abstract

Modern scientific ecosystems are rich in procedural knowledge across repositories, APIs, scripts, notebooks, documentation, databases, and papers, yet much of this knowledge remains fragmented across heterogeneous artifacts that agents cannot readily operationalize. This gap between abundant scientific know-how and usable agent capabilities is a key bottleneck for building effective scientific agents. We present SkillFoundry, a self-evolving framework that converts such resources into validated agent skills, reusable packages that encode task scope, inputs and outputs, execution steps, environment assumptions, provenance, and tests. SkillFoundry organizes a target domain as a domain knowledge tree, mines resources from high-value branches, extracts operational contracts, compiles them into executable skill packages, and then iteratively expands, repairs, merges, or prunes the resulting library through a closed-loop validation process. SkillFoundry produces a substantially novel and internally valid skill library, with 71.1\% of mined skills differing from existing skill libraries such as SkillHub and SkillSMP. We demonstrate that these mined skills improve coding agent performance on five of the six MoSciBench datasets. We further show that SkillFoundry can design new task-specific skills on demand for concrete scientific objectives, and that the resulting skills substantially improve performance on two challenging genomics tasks: cell type annotation and the scDRS workflow. Together, these results show that automatically mined skills improve agent performance on benchmarks and domain-specific tasks, expand coverage beyond hand-crafted skill libraries, and provide a practical foundation for more capable scientific agents.



---


# SLEA-RL: Step-Level Experience Augmented Reinforcement Learning for Multi-Turn Agentic Training

**arXiv ID**: 2603.18079
**arXiv URL**: https://arxiv.org/abs/2603.18079

## Abstract

Large Language Model (LLM) agents have shown strong results on multi-turn tool-use tasks, yet they operate in isolation during training, failing to leverage experiences accumulated across episodes. Existing experience-augmented methods address this by organizing trajectories into retrievable libraries, but they retrieve experiences only once based on the initial task description and hold them constant throughout the episode. In multi-turn settings where observations change at every step, this static retrieval becomes increasingly mismatched as episodes progress. We propose SLEA-RL (Step-Level Experience-Augmented Reinforcement Learning), a framework that retrieves relevant experiences at each decision step conditioned on the current observation. SLEA-RL operates through three components: (i) step-level observation clustering that groups structurally equivalent environmental states for efficient cluster-indexed retrieval; (ii) a self-evolving experience library that distills successful strategies and failure patterns through score-based admission and rate-limited extraction; and (iii) policy optimization with step-level credit assignment for fine-grained advantage estimation across multi-turn episodes. The experience library evolves alongside the policy through semantic analysis rather than gradient updates. Experiments on long-horizon multi-turn agent benchmarks demonstrate that SLEA-RL achieves superior performance compared to various reinforcement learning baselines.



---


# SPA-RL: Reinforcing LLM Agents via Stepwise Progress Attribution

**arXiv ID**: 2505.20732
**arXiv URL**: https://arxiv.org/abs/2505.20732

## Abstract

Reinforcement learning (RL) holds significant promise for training LLM agents to handle complex, goal-oriented tasks that require multi-step interactions with external environments. However, a critical challenge when applying RL to these agentic tasks arises from delayed rewards: feedback signals are typically available only after the entire task is completed. This makes it non-trivial to assign delayed rewards to earlier actions, providing insufficient guidance regarding environmental constraints and hindering agent training. In this work, we draw on the insight that the ultimate completion of a task emerges from the cumulative progress an agent makes across individual steps. We propose Stepwise Progress Attribution (SPA), a general reward redistribution framework that decomposes the final reward into stepwise contributions, each reflecting its incremental progress toward overall task completion. To achieve this, we train a progress estimator that accumulates stepwise contributions over a trajectory to match the task completion. During policy optimization, we combine the estimated per-step contribution with a grounding signal for actions executed in the environment as the fine-grained, intermediate reward for effective agent training. Extensive experiments on common agent benchmarks (including Webshop, ALFWorld, and VirtualHome) demonstrate that SPA consistently outperforms the state-of-the-art method in both success rate (+2.5\% on average) and grounding accuracy (+1.9\% on average). Further analyses demonstrate that our method remarkably provides more effective intermediate rewards for RL training. Our code is available at https://github.com/WangHanLinHenry/SPA-RL-Agent.



---


# SPARE: Single-Pass Annotation with Reference-Guided Evaluation for Automatic Process Supervision and Reward Modelling

**arXiv ID**: 2506.15498
**arXiv URL**: https://arxiv.org/abs/2506.15498

## Abstract

Process or step-wise supervision has played a crucial role in advancing complex multi-step reasoning capabilities of Large Language Models (LLMs). However, efficient, high-quality automated process annotation remains a significant challenge. To address this, we introduce Single-Pass Annotation with Reference-Guided Evaluation (SPARE), a novel structured framework that enables efficient per-step annotation by jointly aligning solution steps to reference solutions and determine its accuracy with explicit reasoning in single generation. We demonstrate SPARE's effectiveness across four diverse datasets spanning mathematical reasoning (GSM8K, MATH), multi-hop question answering (MuSiQue-Ans), and spatial reasoning (SpaRP), showing consistent improvements in two applications: (1) training Process Reward Models (PRMs) for ranking and aggregating multiple generations, and (2) fine-tuning models via offline reinforcement learning for greedy decoding. On ProcessBench, SPARE demonstrates data-efficient out-of-distribution generalization, using only $\sim$16% of training samples compared to human-labeled and other synthetically trained baselines. Additionally, it achieves competitive performance with MCTS-based methods while offering 2.3$\times$ speedup in terms of total token count. Manual analysis reveals complementary precision-recall characteristics with MCTS approaches, suggesting potential for ensemble methods. These results establish SPARE as a practical and scalable solution for automatic process supervision in LLM reasoning.



---


# SPARK: Stepwise Process-Aware Rewards for Reference-Free Reinforcement Learning

**arXiv ID**: 2512.03244
**arXiv URL**: https://arxiv.org/abs/2512.03244

## Abstract

Process reward models (PRMs) that provide dense, step-level feedback have shown promise for reinforcement learning, yet their adoption remains limited by the need for expensive step-level annotations or ground truth references. We propose SPARK: a three-stage framework where in the first stage a generator model produces diverse solutions and a verifier model evaluates them using parallel scaling (self-consistency) and sequential scaling (meta-critique). In the second stage, we use these verification outputs as synthetic training data to fine-tune generative process reward models, which subsequently serve as reward signals during training. We show that aggregating multiple independent verifications at the step level produces training data for process reward models that surpass ground-truth outcome supervision, achieving 67.5 F1 on ProcessBench (a benchmark for identifying erroneous steps in mathematical reasoning) compared to 66.4 for reference-guided training and 61.9 for GPT-4o. In the final stage, we apply our generative PRM with chain-of-thought verification (PRM-CoT) as the reward model in RL experiments on mathematical reasoning, and introduce format constraints to prevent reward hacking. Using Qwen2.5-Math-7B, we achieve 47.4% average accuracy across six mathematical reasoning benchmarks, outperforming ground-truth-based RLVR (43.9%). Our work enables reference-free RL training that exceeds ground-truth methods, opening new possibilities for domains lacking verifiable answers or accessible ground truth.



---


# SRR-Judge: Step-Level Rating and Refinement for Enhancing Search-Integrated Reasoning in Search Agents

**arXiv ID**: 2602.07773
**arXiv URL**: https://arxiv.org/abs/2602.07773

## Abstract

Recent deep search agents built on large reasoning models (LRMs) excel at complex question answering by iteratively planning, acting, and gathering evidence, a capability known as search-integrated reasoning. However, mainstream approaches often train this ability using only outcome-based supervision, neglecting the quality of intermediate thoughts and actions. We introduce SRR-Judge, a framework for reliable step-level assessment of reasoning and search actions. Integrated into a modified ReAct-style rate-and-refine workflow, SRR-Judge provides fine-grained guidance for search-integrated reasoning and enables efficient post-training annotation. Using SRR-annotated data, we apply an iterative rejection sampling fine-tuning procedure to enhance the deep search capability of the base agent. Empirically, SRR-Judge delivers more reliable step-level evaluations than much larger models such as DeepSeek-V3.1, with its ratings showing strong correlation with final answer correctness. Moreover, aligning the policy with SRR-Judge annotated trajectories leads to substantial performance gains, yielding over a 10 percent average absolute pass@1 improvement across challenging deep search benchmarks.



---


# START: Self-taught Reasoner with Tools

**arXiv ID**: 2503.04625
**arXiv URL**: https://arxiv.org/abs/2503.04625

## Abstract

Large reasoning models (LRMs) like OpenAI-o1 and DeepSeek-R1 have demonstrated remarkable capabilities in complex reasoning tasks through the utilization of long Chain-of-thought (CoT). However, these models often suffer from hallucinations and inefficiencies due to their reliance solely on internal reasoning processes. In this paper, we introduce START (Self-Taught Reasoner with Tools), a novel tool-integrated long CoT reasoning LLM that significantly enhances reasoning capabilities by leveraging external tools. Through code execution, START is capable of performing complex computations, self-checking, exploring diverse methods, and self-debugging, thereby addressing the limitations of LRMs. The core innovation of START lies in its self-learning framework, which comprises two key techniques: 1) Hint-infer: We demonstrate that inserting artificially designed hints (e.g., ``Wait, maybe using Python here is a good idea.'') during the inference process of a LRM effectively stimulates its ability to utilize external tools without the need for any demonstration data. Hint-infer can also serve as a simple and effective sequential test-time scaling method; 2) Hint Rejection Sampling Fine-Tuning (Hint-RFT): Hint-RFT combines Hint-infer and RFT by scoring, filtering, and modifying the reasoning trajectories with tool invocation generated by a LRM via Hint-infer, followed by fine-tuning the LRM. Through this framework, we have fine-tuned the QwQ-32B model to achieve START. On PhD-level science QA (GPQA), competition-level math benchmarks (AMC23, AIME24, AIME25), and the competition-level code benchmark (LiveCodeBench), START achieves accuracy rates of 63.6%, 95.0%, 66.7%, 47.1%, and 47.3%, respectively. It significantly outperforms the base QwQ-32B and achieves performance comparable to the state-of-the-art open-weight model R1-Distill-Qwen-32B and the proprietary model o1-Preview.



---


# SWE-Skills-Bench: Do Agent Skills Actually Help in Real-World Software Engineering?

**arXiv ID**: 2603.15401
**arXiv URL**: https://arxiv.org/abs/2603.15401

## Abstract

Agent skills, structured procedural knowledge packages injected at inference time, are increasingly used to augment LLM agents on software engineering tasks. However, their real utility in end-to-end development settings remains unclear. We present SWE-Skills-Bench, the first requirement-driven benchmark that isolates the marginal utility of agent skills in real-world software engineering (SWE). It pairs 49 public SWE skills with authentic GitHub repositories pinned at fixed commits and requirement documents with explicit acceptance criteria, yielding approximately 565 task instances across six SWE subdomains. We introduce a deterministic verification framework that maps each task's acceptance criteria to execution-based tests, enabling controlled paired evaluation with and without the skill. Our results show that skill injection benefits are far more limited than rapid adoption suggests: 39 of 49 skills yield zero pass-rate improvement, and the average gain is only +1.2%. Token overhead varies from modest savings to a 451% increase while pass rates remain unchanged. Only seven specialized skills produce meaningful gains (up to +30%), while three degrade performance (up to -10%) due to version-mismatched guidance conflicting with project context. These findings suggest that agent skills are a narrow intervention whose utility depends strongly on domain fit, abstraction level, and contextual compatibility. SWE-Skills-Bench provides a testbed for evaluating the design, selection, and deployment of skills in software engineering agents. SWE-Skills-Bench is available at https://github.com/GeniusHTX/SWE-Skills-Bench.



---


# SWEET-RL: Training Multi-Turn LLM Agents on Collaborative Reasoning Tasks

**arXiv ID**: 2503.15478
**arXiv URL**: https://arxiv.org/abs/2503.15478

## Abstract

Large language model (LLM) agents need to perform multi-turn interactions in real-world tasks. However, existing multi-turn RL algorithms for optimizing LLM agents fail to perform effective credit assignment over multiple turns while leveraging the generalization capabilities of LLMs and it remains unclear how to develop such algorithms. To study this, we first introduce a new benchmark, ColBench, where an LLM agent interacts with a human collaborator over multiple turns to solve realistic tasks in backend programming and frontend design. Building on this benchmark, we propose a novel RL algorithm, SWEET-RL (RL with Step-WisE Evaluation from Training-time information), that uses a carefully designed optimization objective to train a critic model with access to additional training-time information. The critic provides step-level rewards for improving the policy model. Our experiments demonstrate that SWEET-RL achieves a 6% absolute improvement in success and win rates on ColBench compared to other state-of-the-art multi-turn RL algorithms, enabling Llama-3.1-8B to match or exceed the performance of GPT4-o in realistic collaborative content creation.



---


# ScienceWorld: Is your Agent Smarter than a 5th Grader?

**arXiv ID**: 2203.07540
**arXiv URL**: https://arxiv.org/abs/2203.07540

## Abstract

We present ScienceWorld, a benchmark to test agents' scientific reasoning abilities in a new interactive text environment at the level of a standard elementary school science curriculum. Despite the transformer-based progress seen in question-answering and scientific text processing, we find that current models cannot reason about or explain learned science concepts in novel contexts. For instance, models can easily answer what the conductivity of a known material is but struggle when asked how they would conduct an experiment in a grounded environment to find the conductivity of an unknown material. This begs the question of whether current models are simply retrieving answers by way of seeing a large number of similar examples or if they have learned to reason about concepts in a reusable manner. We hypothesize that agents need to be grounded in interactive environments to achieve such reasoning capabilities. Our experiments provide empirical evidence supporting this hypothesis -- showing that a 1.5 million parameter agent trained interactively for 100k steps outperforms a 11 billion parameter model statically trained for scientific question-answering and reasoning from millions of expert demonstrations.



---


# ScoreFlow: Mastering LLM Agent Workflows via Score-based Preference Optimization

**arXiv ID**: 2502.04306
**arXiv URL**: https://arxiv.org/abs/2502.04306

## Abstract

Recent research has leveraged large language model multi-agent systems for complex problem-solving while trying to reduce the manual effort required to build them, driving the development of automated agent workflow optimization methods. However, existing methods remain inflexible due to representational limitations, a lack of adaptability, and poor scalability when relying on discrete optimization techniques. We address these challenges with ScoreFlow, a simple yet high-performance framework that leverages efficient gradient-based optimization in a continuous space. ScoreFlow incorporates Score-DPO, a novel variant of the direct preference optimization method that accounts for quantitative feedback. Across six benchmarks spanning question answering, coding, and mathematical reasoning, ScoreFlow achieves an 8.2% improvement over existing baselines. Moreover, it empowers smaller models to outperform larger ones with lower inference costs. Project: https://github.com/Gen-Verse/ScoreFlow



---


# ScreenLLM: Stateful Screen Schema for Efficient Action Understanding and Prediction

**arXiv ID**: 2503.20978
**arXiv URL**: https://arxiv.org/abs/2503.20978

## Abstract

Graphical User Interface (GUI) agents are autonomous systems that interpret and generate actions, enabling intelligent user assistance and automation. Effective training of these agent presents unique challenges, such as sparsity in supervision signals, scalability for large datasets, and the need for nuanced user understanding. We propose stateful screen schema, an efficient representation of GUI interactions that captures key user actions and intentions over time. Building on this foundation, we introduce ScreenLLM, a set of multimodal large language models (MLLMs) tailored for advanced UI understanding and action prediction. Extensive experiments on both open-source and proprietary models show that ScreenLLM accurately models user behavior and predicts actions. Our work lays the foundation for scalable, robust, and intelligent GUI agents that enhance user interaction in diverse software environments.



---


# Search-o1: Agentic Search-Enhanced Large Reasoning Models

**arXiv ID**: 2501.05366
**arXiv URL**: https://arxiv.org/abs/2501.05366

## Abstract

Large reasoning models (LRMs) like OpenAI-o1 have demonstrated impressive long stepwise reasoning capabilities through large-scale reinforcement learning. However, their extended reasoning processes often suffer from knowledge insufficiency, leading to frequent uncertainties and potential errors. To address this limitation, we introduce \textbf{Search-o1}, a framework that enhances LRMs with an agentic retrieval-augmented generation (RAG) mechanism and a Reason-in-Documents module for refining retrieved documents. Search-o1 integrates an agentic search workflow into the reasoning process, enabling dynamic retrieval of external knowledge when LRMs encounter uncertain knowledge points. Additionally, due to the verbose nature of retrieved documents, we design a separate Reason-in-Documents module to deeply analyze the retrieved information before injecting it into the reasoning chain, minimizing noise and preserving coherent reasoning flow. Extensive experiments on complex reasoning tasks in science, mathematics, and coding, as well as six open-domain QA benchmarks, demonstrate the strong performance of Search-o1. This approach enhances the trustworthiness and applicability of LRMs in complex reasoning tasks, paving the way for more reliable and versatile intelligent systems. The code is available at \url{https://github.com/sunnynexus/Search-o1}.



---


# Self-Consolidation for Self-Evolving Agents

**arXiv ID**: 2602.01966
**arXiv URL**: https://arxiv.org/abs/2602.01966

## Abstract

While large language model (LLM) agents have demonstrated impressive problem-solving capabilities, they typically operate as static systems, lacking the ability to evolve through lifelong interaction. Existing attempts to bridge this gap primarily rely on retrieving successful past trajectories as demonstrations. However, this paradigm faces two critical limitations. First, by focusing solely on success, agents overlook the rich pedagogical value embedded in failed attempts, preventing them from identifying and avoiding recurrent pitfalls. Second, continually accumulating textual experiences not only increases the time consumption during retrieval but also inevitably introduces noise and exhausts the largest context window of current LLMs. To address these challenges, we propose a novel self-evolving framework for LLM agents that introduces a complementary evolution mechanism: First, a contrastive reflection strategy is introduced to explicitly summarize error-prone patterns and capture reusable insights. Second, we propose a self-consolidation mechanism that distills non-parametric textual experience into compact learnable parameters. This enables the agent to internalize extensive historical experience directly into its latent space. Extensive experiments demonstrate the advantages of our method in long-term agent evolution.



---


# Self-Distillation Enables Continual Learning

**arXiv ID**: 2601.19897
**arXiv URL**: https://arxiv.org/abs/2601.19897

## Abstract

Continual learning, enabling models to acquire new skills and knowledge without degrading existing capabilities, remains a fundamental challenge for foundation models. While on-policy reinforcement learning can reduce forgetting, it requires explicit reward functions that are often unavailable. Learning from expert demonstrations, the primary alternative, is dominated by supervised fine-tuning (SFT), which is inherently off-policy. We introduce Self-Distillation Fine-Tuning (SDFT), a simple method that enables on-policy learning directly from demonstrations. SDFT leverages in-context learning by using a demonstration-conditioned model as its own teacher, generating on-policy training signals that preserve prior capabilities while acquiring new skills. Across skill learning and knowledge acquisition tasks, SDFT consistently outperforms SFT, achieving higher new-task accuracy while substantially reducing catastrophic forgetting. In sequential learning experiments, SDFT enables a single model to accumulate multiple skills over time without performance regression, establishing on-policy distillation as a practical path to continual learning from demonstrations.



---


# Self-Distillation Zero: Self-Revision Turns Binary Rewards into Dense Supervision

**arXiv ID**: 2604.12002
**arXiv URL**: https://arxiv.org/abs/2604.12002

## Abstract

Current post-training methods in verifiable settings fall into two categories. Reinforcement learning (RLVR) relies on binary rewards, which are broadly applicable and powerful, but provide only sparse supervision during training. Distillation provides dense token-level supervision, typically obtained from an external teacher or using high-quality demonstrations. Collecting such supervision can be costly or unavailable. We propose Self-Distillation Zero (SD-Zero), a method that is substantially more training sample-efficient than RL and does not require an external teacher or high-quality demonstrations. SD-Zero trains a single model to play two roles: a Generator, which produces an initial response, and a Reviser, which conditions on that response and its binary reward to produce an improved response. We then perform on-policy self-distillation to distill the reviser into the generator, using the reviser's token distributions conditioned on the generator's response and its reward as supervision. In effect, SD-Zero trains the model to transform binary rewards into dense token-level self-supervision. On math and code reasoning benchmarks with Qwen3-4B-Instruct and Olmo-3-7B-Instruct, SD-Zero improves performance by at least 10% over the base models and outperforms strong baselines, including Rejection Fine-Tuning (RFT), GRPO, and Self-Distillation Fine-Tuning (SDFT), under the same question set and training sample budget. Extensive ablation studies show two novel characteristics of our proposed algorithm: (a) token-level self-localization, where the reviser can identify the key tokens that need to be revised in the generator's response based on reward, and (b) iterative self-evolution, where the improving ability to revise answers can be distilled back into generation performance with regular teacher synchronization.



---


# Self-Distilled Reinforcement Learning for Co-Evolving Agentic Recommender Systems

**arXiv ID**: 2604.10029
**arXiv URL**: https://arxiv.org/abs/2604.10029

## Abstract

Large language model-empowered agentic recommender systems (ARS) reformulate recommendation as a multi-turn interaction between a recommender agent and a user agent, enabling iterative preference elicitation and refinement beyond conventional one-shot prediction. However, existing ARS are mainly optimized in a Reflexion-style paradigm, where past interaction trajectories are stored as textual memory and retrieved as prompt context for later reasoning. Although this design allows agents to recall prior feedback and observations, the accumulated experience remains external to model parameters, leaving agents reliant on generic reasoning rather than progressively acquiring recommendation-specific decision-making ability through learning. Reinforcement learning (RL) therefore provides a natural way to internalize such interaction experience into parameters. Yet existing RL methods for ARS still suffer from two key limitations. First, they fail to capture the interactive nature of ARS, in which the recommender agent and the user agent continuously influence each other and can naturally generate endogenous supervision through interaction feedback. Second, they reduce a rich multi-turn interaction process to final outcomes, overlooking the dense supervision embedded throughout the trajectory. To this end, we propose CoARS, a self-distilled reinforcement learning framework for co-evolving agentic recommender systems. CoARS introduces two complementary learning schemes: interaction reward, which derives coupled task-level supervision for the recommender agent and the user agent from the same interaction trajectory, and self-distilled credit assignment, which converts historical trajectories into token-level credit signals under teacher-student conditioning. Experiments on multiple datasets show that CoARS outperforms representative ARS baselines in recommendation performance and user alignment.



---


# Self-Generated In-Context Examples Improve LLM Agents for Sequential Decision-Making Tasks

**arXiv ID**: 2505.00234
**arXiv URL**: https://arxiv.org/abs/2505.00234

## Abstract

Improving Large Language Model (LLM) agents for sequential decision-making tasks typically requires extensive task-specific knowledge engineering--custom prompts, curated examples, and specialized observation/action spaces. We investigate a different approach where agents automatically improve by learning from their own successful experiences without human intervention. Our method constructs and refines a database of self-generated trajectories that serve as in-context examples for future tasks. Even naive accumulation of successful trajectories yields substantial performance gains across three diverse benchmarks: ALFWorld (73% to 89%), Wordcraft (55% to 64%), and InterCode-SQL (75% to 79%). These improvements exceed those achieved by upgrading from gpt-4o-mini to gpt-4o and match the performance of allowing multiple attempts per task. We further enhance this approach with two innovations: database-level curation using population-based training to propagate high-performing example collections, and exemplar-level curation that selectively retains trajectories based on their empirical utility as in-context examples. With these enhancements, our method achieves 93% success on ALFWorld--surpassing approaches that use more powerful LLMs and hand-crafted components. Our trajectory bootstrapping technique demonstrates that agents can autonomously improve through experience, offering a scalable alternative to labor-intensive knowledge engineering.



---


# Self-Improving VLM Judges Without Human Annotations

**arXiv ID**: 2512.05145
**arXiv URL**: https://arxiv.org/abs/2512.05145

## Abstract

Effective judges of Vision-Language Models (VLMs) are crucial for model development. Current methods for training VLM judges mainly rely on large-scale human preference annotations. However, such an approach is costly, and the annotations easily become obsolete as models rapidly improve. In this work, we present a framework to self-train a VLM judge model without any human preference annotations, using only self-synthesized data. Our method is iterative and has three stages: (1) generate diverse multimodal instruction-response pairs at varying quality levels, (2) generate reasoning traces and judgments for each pair, removing the ones that do not match our expected quality levels, and (3) training on correct judge answers and their reasoning traces. We evaluate the resulting judge on Multimodal RewardBench and VL-RewardBench across domains: correctness, preference, reasoning, safety, and visual question-answering. Our method improves a Llama-3.2-11B multimodal judge from 0.38 to 0.51 in overall accuracy on VL-RewardBench, often outperforming much larger models including Llama-3.2-90B, GPT-4o, and Claude 3.5 Sonnet, with particularly strong gains in general, hallucination, and reasoning dimensions. The overall strength of these human-annotation-free results suggest the potential for a future self-judge that evolves alongside rapidly improving VLM capabilities.



---


# Self-Instruct: Aligning Language Models with Self-Generated Instructions

**arXiv ID**: 2212.10560
**arXiv URL**: https://arxiv.org/abs/2212.10560

## Abstract

Large "instruction-tuned" language models (i.e., finetuned to respond to instructions) have demonstrated a remarkable ability to generalize zero-shot to new tasks. Nevertheless, they depend heavily on human-written instruction data that is often limited in quantity, diversity, and creativity, therefore hindering the generality of the tuned model. We introduce Self-Instruct, a framework for improving the instruction-following capabilities of pretrained language models by bootstrapping off their own generations. Our pipeline generates instructions, input, and output samples from a language model, then filters invalid or similar ones before using them to finetune the original model. Applying our method to the vanilla GPT3, we demonstrate a 33% absolute improvement over the original model on Super-NaturalInstructions, on par with the performance of InstructGPT-001, which was trained with private user data and human annotations. For further evaluation, we curate a set of expert-written instructions for novel tasks, and show through human evaluation that tuning GPT3 with Self-Instruct outperforms using existing public instruction datasets by a large margin, leaving only a 5% absolute gap behind InstructGPT-001. Self-Instruct provides an almost annotation-free method for aligning pre-trained language models with instructions, and we release our large synthetic dataset to facilitate future studies on instruction tuning. Our code and data are available at https://github.com/yizhongw/self-instruct.



---


# Self-Questioning Language Models

**arXiv ID**: 2508.03682
**arXiv URL**: https://arxiv.org/abs/2508.03682

## Abstract

Can large language models improve without external data -- by generating their own questions and answers? We hypothesize that a pre-trained language model can improve its reasoning skills given only a single prompt specifying the topic (e.g., algebra word problems) and asking the model to generate its own questions. To do this, we propose Self-Questioning Language Models (SQLM): an asymmetric self-play framework where a proposer is given the topic and generates a question for a solver, who tries to answer it. Both the proposer and solver are trained via reinforcement learning. The proposer receives a reward if the problem is not too easy or too difficult, and the solver receives a reward based on majority voting, a proxy for correctness in the absence of ground-truth answers. For coding, the proposer can instead generate unit tests which are used for verification. We study this asymmetric self-play framework on three benchmarks: three-digit multiplication, algebra problems from the OMEGA benchmark, and programming problems from Codeforces. By continually generating more interesting problems and attempting to solve them, language models can improve on downstream benchmarks without access to any curated training datasets.



---


# Self-Training Large Language Models for Improved Visual Program Synthesis With Visual Reinforcement

**arXiv ID**: 2404.04627
**arXiv URL**: https://arxiv.org/abs/2404.04627

## Abstract

Visual program synthesis is a promising approach to exploit the reasoning abilities of large language models for compositional computer vision tasks. Previous work has used few-shot prompting with frozen LLMs to synthesize visual programs. Training an LLM to write better visual programs is an attractive prospect, but it is unclear how to accomplish this. No dataset of visual programs for training exists, and acquisition of a visual program dataset cannot be easily crowdsourced due to the need for expert annotators. To get around the lack of direct supervision, we explore improving the program synthesis abilities of an LLM using feedback from interactive experience. We propose a method where we exploit existing annotations for a vision-language task to improvise a coarse reward signal for that task, treat the LLM as a policy, and apply reinforced self-training to improve the visual program synthesis ability of the LLM for that task. We describe a series of experiments on object detection, compositional visual question answering, and image-text retrieval, and show that in each case, the self-trained LLM outperforms or performs on par with few-shot frozen LLMs that are an order of magnitude larger. Website: https://zaidkhan.me/ViReP



---


# Self-evolving Embodied AI

**arXiv ID**: 2602.04411
**arXiv URL**: https://arxiv.org/abs/2602.04411

## Abstract

Embodied Artificial Intelligence (AI) is an intelligent system formed by agents and their environment through active perception, embodied cognition, and action interaction. Existing embodied AI remains confined to human-crafted setting, in which agents are trained on given memory and construct models for given tasks, enabling fixed embodiments to interact with relatively static environments. Such methods fail in in-the-wild setting characterized by variable embodiments and dynamic open environments. This paper introduces self-evolving embodied AI, a new paradigm in which agents operate based on their changing state and environment with memory self-updating, task self-switching, environment self-prediction, embodiment self-adaptation, and model self-evolution, aiming to achieve continually adaptive intelligence with autonomous evolution. Specifically, we present the definition, framework, components, and mechanisms of self-evolving embodied AI, systematically review state-of-the-art works for realized components, discuss practical applications, and point out future research directions. We believe that self-evolving embodied AI enables agents to autonomously learn and interact with environments in a human-like manner and provide a new perspective toward general artificial intelligence.



---


# Skill Set Optimization: Reinforcing Language Model Behavior via Transferable Skills

**arXiv ID**: 2402.03244
**arXiv URL**: https://arxiv.org/abs/2402.03244

## Abstract

Large language models (LLMs) have recently been used for sequential decision making in interactive environments. However, leveraging environment reward signals for continual LLM actor improvement is not straightforward. We propose Skill Set Optimization (SSO) for improving LLM actor performance through constructing and refining sets of transferable skills. SSO constructs skills by extracting common subtrajectories with high rewards and generating subgoals and instructions to represent each skill. These skills are provided to the LLM actor in-context to reinforce behaviors with high rewards. Then, SSO further refines the skill set by pruning skills that do not continue to result in high rewards. We evaluate our method in the classic videogame NetHack and the text environment ScienceWorld to demonstrate SSO's ability to optimize a set of skills and perform in-context policy improvement. SSO outperforms baselines by 40% in our custom NetHack task and outperforms the previous state-of-the-art in ScienceWorld by 35%.



---


# Skill-SD: Skill-Conditioned Self-Distillation for Multi-turn LLM Agents

**arXiv ID**: 2604.10674
**arXiv URL**: https://arxiv.org/abs/2604.10674

## Abstract

Reinforcement learning (RL) has been widely used to train LLM agents for multi-turn interactive tasks, but its sample efficiency is severely limited by sparse rewards and long horizons. On-policy self-distillation (OPSD) alleviates this by providing dense token-level supervision from a privileged teacher that has access to ground-truth answers. However, such fixed privileged information cannot capture the diverse valid strategies in agent tasks, and naively combining OPSD with RL often leads to training collapse. To address these limitations, we introduce Skill-SD, a framework that turns the agent's own trajectories into dynamic training-only supervision. Completed trajectories are summarized into compact natural language skills that describe successful behaviors, mistakes, and workflows. These skills serve as dynamic privileged information conditioning only the teacher, while the student always acts under the plain task prompt and learns to internalize the guidance through distillation. To stabilize the training, we derive an importance-weighted reverse-KL loss to provide gradient-correct token-level distillation, and dynamically synchronize the teacher with the improving student. Experimental results on agentic benchmarks demonstrate that Skill-SD substantially outperforms the standard RL baseline, improving both vanilla GRPO (+14.0%/+10.9% on AppWorld/Sokoban) and vanilla OPD (+42.1%/+40.6%). Project page: https://k1xe.github.io/skill-sd/



---


# SkillClaw: Let Skills Evolve Collectively with Agentic Evolver

**arXiv ID**: 2604.08377
**arXiv URL**: https://arxiv.org/abs/2604.08377

## Abstract

Large language model (LLM) agents such as OpenClaw rely on reusable skills to perform complex tasks, yet these skills remain largely static after deployment. As a result, similar workflows, tool usage patterns, and failure modes are repeatedly rediscovered across users, preventing the system from improving with experience. While interactions from different users provide complementary signals about when a skill works or fails, existing systems lack a mechanism to convert such heterogeneous experiences into reliable skill updates. To address these issues, we present SkillClaw, a framework for collective skill evolution in multi-user agent ecosystems, which treats cross-user and over-time interactions as the primary signal for improving skills. SkillClaw continuously aggregates trajectories generated during use and processes them with an autonomous evolver, which identifies recurring behavioral patterns and translates them into updates to the skill set by refining existing skills or extending them with new capabilities. The resulting skills are maintained in a shared repository and synchronized across users, allowing improvements discovered in one context to propagate system-wide while requiring no additional effort from users. By integrating multi-user experience into ongoing skill updates, SkillClaw enables cross-user knowledge transfer and cumulative capability improvement, and experiments on WildClawBench show that limited interaction and feedback, it significantly improves the performance of Qwen3-Max in real-world agent scenarios.



---


# SkillNet: Create, Evaluate, and Connect AI Skills

**arXiv ID**: 2603.04448
**arXiv URL**: https://arxiv.org/abs/2603.04448

## Abstract

Current AI agents can flexibly invoke tools and execute complex tasks, yet their long-term advancement is hindered by the lack of systematic accumulation and transfer of skills. Without a unified mechanism for skill consolidation, agents frequently ``reinvent the wheel'', rediscovering solutions in isolated contexts without leveraging prior strategies. To overcome this limitation, we introduce SkillNet, an open infrastructure designed to create, evaluate, and organize AI skills at scale. SkillNet structures skills within a unified ontology that supports creating skills from heterogeneous sources, establishing rich relational connections, and performing multi-dimensional evaluation across Safety, Completeness, Executability, Maintainability, and Cost-awareness. Our infrastructure integrates a repository of over 200,000 skills, an interactive platform, and a versatile Python toolkit. Experimental evaluations on ALFWorld, WebShop, and ScienceWorld demonstrate that SkillNet significantly enhances agent performance, improving average rewards by 40% and reducing execution steps by 30% across multiple backbone models. By formalizing skills as evolving, composable assets, SkillNet provides a robust foundation for agents to move from transient experience to durable mastery.



---


# SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning

**arXiv ID**: 2602.08234
**arXiv URL**: https://arxiv.org/abs/2602.08234

## Abstract

Large Language Model (LLM) agents have shown stunning results in complex tasks, yet they often operate in isolation, failing to learn from past experiences. Existing memory-based methods primarily store raw trajectories, which are often redundant and noise-heavy. This prevents agents from extracting high-level, reusable behavioral patterns that are essential for generalization. In this paper, we propose SkillRL, a framework that bridges the gap between raw experience and policy improvement through automatic skill discovery and recursive evolution. Our approach introduces an experience-based distillation mechanism to build a hierarchical skill library SkillBank, an adaptive retrieval strategy for general and task-specific heuristics, and a recursive evolution mechanism that allows the skill library to co-evolve with the agent's policy during reinforcement learning. These innovations significantly reduce the token footprint while enhancing reasoning utility. Experimental results on ALFWorld, WebShop and seven search-augmented tasks demonstrate that SkillRL achieves state-of-the-art performance, outperforming strong baselines over 15.3% and maintaining robustness as task complexity increases. Code is available at this https://github.com/aiming-lab/SkillRL.



---


# SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills

**arXiv ID**: 2504.07079
**arXiv URL**: https://arxiv.org/abs/2504.07079

## Abstract

To survive and thrive in complex environments, humans have evolved sophisticated self-improvement mechanisms through environment exploration, hierarchical abstraction of experiences into reuseable skills, and collaborative construction of an ever-growing skill repertoire. Despite recent advancements, autonomous web agents still lack crucial self-improvement capabilities, struggling with procedural knowledge abstraction, refining skills, and skill composition. In this work, we introduce SkillWeaver, a skill-centric framework enabling agents to self-improve by autonomously synthesizing reusable skills as APIs. Given a new website, the agent autonomously discovers skills, executes them for practice, and distills practice experiences into robust APIs. Iterative exploration continually expands a library of lightweight, plug-and-play APIs, significantly enhancing the agent's capabilities. Experiments on WebArena and real-world websites demonstrate the efficacy of SkillWeaver, achieving relative success rate improvements of 31.8% and 39.8%, respectively. Additionally, APIs synthesized by strong agents substantially enhance weaker agents through transferable skills, yielding improvements of up to 54.3% on WebArena. These results demonstrate the effectiveness of honing diverse website interactions into APIs, which can be seamlessly shared among various web agents.



---


# SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks

**arXiv ID**: 2602.12670
**arXiv URL**: https://arxiv.org/abs/2602.12670

## Abstract

Agent Skills are structured packages of procedural knowledge that augment LLM agents at inference time. Despite rapid adoption, there is no standard way to measure whether they actually help. We present SkillsBench, a benchmark of 86 tasks across 11 domains paired with curated Skills and deterministic verifiers. Each task is evaluated under three conditions: no Skills, curated Skills, and self-generated Skills. We test 7 agent-model configurations over 7,308 trajectories. Curated Skills raise average pass rate by 16.2 percentage points(pp), but effects vary widely by domain (+4.5pp for Software Engineering to +51.9pp for Healthcare) and 16 of 84 tasks show negative deltas. Self-generated Skills provide no benefit on average, showing that models cannot reliably author the procedural knowledge they benefit from consuming. Focused Skills with 2--3 modules outperform comprehensive documentation, and smaller models with Skills can match larger models without them.



---


# SpreadsheetBench: Towards Challenging Real World Spreadsheet Manipulation

**arXiv ID**: 2406.14991
**arXiv URL**: https://arxiv.org/abs/2406.14991

## Abstract

We introduce SpreadsheetBench, a challenging spreadsheet manipulation benchmark exclusively derived from real-world scenarios, designed to immerse current large language models (LLMs) in the actual workflow of spreadsheet users. Unlike existing benchmarks that rely on synthesized queries and simplified spreadsheet files, SpreadsheetBench is built from 912 real questions gathered from online Excel forums, which reflect the intricate needs of users. The associated spreadsheets from the forums contain a variety of tabular data such as multiple tables, non-standard relational tables, and abundant non-textual elements. Furthermore, we propose a more reliable evaluation metric akin to online judge platforms, where multiple spreadsheet files are created as test cases for each instruction, ensuring the evaluation of robust solutions capable of handling spreadsheets with varying values. Our comprehensive evaluation of various LLMs under both single-round and multi-round inference settings reveals a substantial gap between the state-of-the-art (SOTA) models and human performance, highlighting the benchmark's difficulty.



---


# SymAgent: A Neural-Symbolic Self-Learning Agent Framework for Complex Reasoning over Knowledge Graphs

**arXiv ID**: 2502.03283
**arXiv URL**: https://arxiv.org/abs/2502.03283

## Abstract

Recent advancements have highlighted that Large Language Models (LLMs) are prone to hallucinations when solving complex reasoning problems, leading to erroneous results. To tackle this issue, researchers incorporate Knowledge Graphs (KGs) to improve the reasoning ability of LLMs. However, existing methods face two limitations: 1) they typically assume that all answers to the questions are contained in KGs, neglecting the incompleteness issue of KGs, and 2) they treat the KG as a static repository and overlook the implicit logical reasoning structures inherent in KGs. In this paper, we introduce SymAgent, an innovative neural-symbolic agent framework that achieves collaborative augmentation between KGs and LLMs. We conceptualize KGs as dynamic environments and transform complex reasoning tasks into a multi-step interactive process, enabling KGs to participate deeply in the reasoning process. SymAgent consists of two modules: Agent-Planner and Agent-Executor. The Agent-Planner leverages LLM's inductive reasoning capability to extract symbolic rules from KGs, guiding efficient question decomposition. The Agent-Executor autonomously invokes predefined action tools to integrate information from KGs and external documents, addressing the issues of KG incompleteness. Furthermore, we design a self-learning framework comprising online exploration and offline iterative policy updating phases, enabling the agent to automatically synthesize reasoning trajectories and improve performance. Experimental results demonstrate that SymAgent with weak LLM backbones (i.e., 7B series) yields better or comparable performance compared to various strong baselines. Further analysis reveals that our agent can identify missing triples, facilitating automatic KG updates.



---


# Test-Time Adaptation for LLM Agents via Environment Interaction

**arXiv ID**: 2511.04847
**arXiv URL**: https://arxiv.org/abs/2511.04847

## Abstract

Large language model (LLM)-based agents struggle to generalize to novel and complex environments, such as unseen websites or new sets of functions, due to a fundamental mismatch between their pre-training and test-time conditions. This challenge stems from two distinct failure modes: a syntactic misunderstanding of environment-specific components like observation formats, and a semantic misunderstanding of state-transition dynamics, which are only revealed at test time. To address these issues, we propose two distinct strategies for adapting LLM agents by leveraging environment-specific information from interaction that is available during deployment. First, an online syntactic alignment (SA) method parameterizes environmental nuances by learning a lightweight adaptation vector that biases the model's output distribution, enabling rapid alignment with an environment response format. Second, a deployment-time dynamics grounding (DG) method employs a persona-driven exploration phase to systematically probe and learn the environment's causal dynamics before task execution, equipping the agent with an in-context world model. We evaluate these strategies across diverse agentic benchmarks, including function calling and web navigation. Our empirical results show the effectiveness of both strategies across all benchmarks with minimal computational cost. We find that dynamics grounding is particularly effective in complex environments where unpredictable dynamics pose a major obstacle, demonstrating a robust path toward more generalizable and capable LLM-based agents. For example, on the WebArena multi-site split, this method increases the agent's success rate from 2% to 23%. We release our code.



---


# The Path of Self-Evolving Large Language Models: Achieving Data-Efficient Learning via Intrinsic Feedback

**arXiv ID**: 2510.02752
**arXiv URL**: https://arxiv.org/abs/2510.02752

## Abstract

Reinforcement learning (RL) has demonstrated potential in enhancing the reasoning capabilities of large language models (LLMs), but such training typically demands substantial efforts in creating and annotating data. In this work, we explore improving LLMs through RL with minimal data. Our approach alternates between the LLM proposing a task and then attempting to solve it. To minimize data dependency, we introduce two novel mechanisms grounded in self-awareness: (1) self-aware difficulty prediction, where the model learns to assess task difficulty relative to its own abilities and prioritize challenging yet solvable tasks, and (2) self-aware limit breaking, where the model recognizes when a task is beyond its capability boundary and proactively requests external data to break through that limit. Extensive experiments on nine benchmarks showing a 53.8% relative improvement with less than 1.2% extra data demonstrate the efficacy of self-aware RL and underscore the promise of self-evolving agent training.



---


# TongUI: Internet-Scale Trajectories from Multimodal Web Tutorials for Generalized GUI Agents

**arXiv ID**: 2504.12679
**arXiv URL**: https://arxiv.org/abs/2504.12679

## Abstract

Building Graphical User Interface (GUI) agents is a promising research direction, which simulates human interaction with computers or mobile phones to perform diverse GUI tasks. However, a major challenge in developing generalized GUI agents is the lack of sufficient trajectory data across various operating systems and applications, mainly due to the high cost of manual annotations. In this paper, we propose the TongUI framework that builds generalized GUI agents by learning from rich multimodal web tutorials. Concretely, we crawl and process online GUI tutorials (such as videos and articles) into GUI agent trajectory data, through which we produce the GUI-Net dataset containing 143K trajectory data across five operating systems and more than 200 applications. We develop the TongUI agent by fine-tuning Qwen2.5-VL-3B/7B models on GUI-Net, which show remarkable performance improvements on commonly used grounding and navigation benchmarks, outperforming baseline agents about 10\% on multiple benchmarks, showing the effectiveness of the GUI-Net dataset and underscoring the significance of our TongUI framework. We will fully open-source the code, the GUI-Net dataset, and the trained models soon.



---


# ToolRL: Reward is All Tool Learning Needs

**arXiv ID**: 2504.13958
**arXiv URL**: https://arxiv.org/abs/2504.13958

## Abstract

Current Large Language Models (LLMs) often undergo supervised fine-tuning (SFT) to acquire tool use capabilities. However, SFT struggles to generalize to unfamiliar or complex tool use scenarios. Recent advancements in reinforcement learning (RL), particularly with R1-like models, have demonstrated promising reasoning and generalization abilities. Yet, reward design for tool use presents unique challenges: multiple tools may be invoked with diverse parameters, and coarse-grained reward signals, such as answer matching, fail to offer the finegrained feedback required for effective learning. In this work, we present the first comprehensive study on reward design for tool selection and application tasks within the RL paradigm. We systematically explore a wide range of reward strategies, analyzing their types, scales, granularity, and temporal dynamics. Building on these insights, we propose a principled reward design tailored for tool use tasks and apply it to train LLMs using Group Relative Policy Optimization (GRPO). Empirical evaluations across diverse benchmarks demonstrate that our approach yields robust, scalable, and stable training, achieving a 17% improvement over base models and a 15% gain over SFT models. These results highlight the critical role of thoughtful reward design in enhancing the tool use capabilities and generalization performance of LLMs. All the codes are released to facilitate future research.



---


# ToolSample: Dual Dynamic Sampling Methods with Curriculum Learning for RL-based Tool Learning

**arXiv ID**: 2509.14718
**arXiv URL**: https://arxiv.org/abs/2509.14718

## Abstract

While reinforcement learning (RL) is increasingly used for LLM-based tool learning, its efficiency is often hampered by an overabundance of simple samples that provide diminishing learning value as training progresses. Existing dynamic sampling techniques are ill-suited for the multi-task structure and fine-grained reward mechanisms inherent to tool learning. This paper introduces Dynamic Sampling with Curriculum Learning (DSCL), a framework specifically designed to address this challenge by targeting the unique characteristics of tool learning: its multiple interdependent sub-tasks and multi-valued reward functions. DSCL features two core components: Reward-Based Dynamic Sampling, which uses multi-dimensional reward statistics (mean and variance) to prioritize valuable data, and Task-Based Dynamic Curriculum Learning, which adaptively focuses training on less-mastered sub-tasks. Through extensive experiments, we demonstrate that DSCL significantly improves training efficiency and model performance over strong baselines, achieving a 3.29\% improvement on the BFCLv3 benchmark. Our method provides a tailored solution that effectively leverages the complex reward signals and sub-task dynamics within tool learning to achieve superior results.



---


# Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills

**arXiv ID**: 2603.25158
**arXiv URL**: https://arxiv.org/abs/2603.25158

## Abstract

Equipping Large Language Model (LLM) agents with domain-specific skills is critical for tackling complex tasks. Yet, manual authoring creates a severe scalability bottleneck. Conversely, automated skill generation often yields fragile or fragmented results because it either relies on shallow parametric knowledge or sequentially overfits to non-generalizable trajectory-local lessons. To overcome this, we introduce Trace2Skill, a framework that mirrors how human experts author skills: by holistically analyzing broad execution experience before distilling it into a single, comprehensive guide. Instead of reacting sequentially to individual trajectories, Trace2Skill dispatches a parallel fleet of sub-agents to analyze a diverse pool of executions. It extracts trajectory-specific lessons and hierarchically consolidates them into a unified, conflict-free skill directory via inductive reasoning. Trace2Skill supports both deepening existing human-written skills and creating new ones from scratch. Experiments in challenging domains, such as spreadsheet, VisionQA and math reasoning, show that Trace2Skill significantly improves upon strong baselines, including Anthropic's official xlsx skills. Crucially, this trajectory-grounded evolution does not merely memorize task instances or model-specific quirks: evolved skills transfer across LLM scales and generalize to OOD settings. For example, skills evolved by Qwen3.5-35B on its own trajectories improved a Qwen3.5-122B agent by up to 57.65 absolute percentage points on WikiTableQuestions. Ultimately, our results demonstrate that complex agent experience can be packaged into highly transferable, declarative skills -- requiring no parameter updates, no external retrieval modules, and utilizing open-source models as small as 35B parameters.



---


# Training-Free Group Relative Policy Optimization

**arXiv ID**: 2510.08191
**arXiv URL**: https://arxiv.org/abs/2510.08191

## Abstract

Recent advances in Large Language Model (LLM) agents have demonstrated their promising general capabilities. However, their performance in specialized real-world domains often degrades due to challenges in effectively integrating external tools and specific prompting strategies. While methods like agentic reinforcement learning have been proposed to address this, they typically rely on costly parameter updates, for example, through a process that uses Supervised Fine-Tuning (SFT) followed by a Reinforcement Learning (RL) phase with Group Relative Policy Optimization (GRPO) to alter the output distribution. However, we argue that LLMs can achieve a similar effect on the output distribution by learning experiential knowledge as a token prior, which is a far more lightweight approach that not only addresses practical data scarcity but also avoids the common issue of overfitting. To this end, we propose Training-Free Group Relative Policy Optimization (Training-Free GRPO), a cost-effective solution that enhances LLM agent performance without any parameter updates. Our method leverages the group relative semantic advantage instead of numerical ones within each group of rollouts, iteratively distilling high-quality experiential knowledge during multi-epoch learning on a minimal ground-truth data. Such knowledge serves as the learned token prior, which is seamlessly integrated during LLM API calls to guide model behavior. Experiments on mathematical reasoning and web searching tasks demonstrate that Training-Free GRPO, when applied to DeepSeek-V3.1-Terminus, significantly improves out-of-domain performance. With just a few dozen training samples, Training-Free GRPO outperforms fine-tuned small LLMs with marginal training data and cost.



---


# Trajectory-Informed Memory Generation for Self-Improving Agent Systems

**arXiv ID**: 2603.10600
**arXiv URL**: https://arxiv.org/abs/2603.10600

## Abstract

LLM-powered agents face a persistent challenge: learning from their execution experiences to improve future performance. While agents can successfully complete many tasks, they often repeat inefficient patterns, fail to recover from similar errors, and miss opportunities to apply successful strategies from past executions. We present a novel framework for automatically extracting actionable learnings from agent execution trajectories and utilizing them to improve future performance through contextual memory retrieval. Our approach comprises four components: (1) a Trajectory Intelligence Extractor that performs semantic analysis of agent reasoning patterns, (2) a Decision Attribution Analyzer that identifies which decisions and reasoning steps led to failures, recoveries, or inefficiencies, (3) a Contextual Learning Generator that produces three types of guidance -- strategy tips from successful patterns, recovery tips from failure handling, and optimization tips from inefficient but successful executions, and (4) an Adaptive Memory Retrieval System that injects relevant learnings into agent prompts based on multi-dimensional similarity. Unlike existing memory systems that store generic conversational facts, our framework understands execution patterns, extracts structured learnings with provenance, and retrieves guidance tailored to specific task contexts. Evaluation on the AppWorld benchmark demonstrates consistent improvements, with up to 14.3 percentage point gains in scenario goal completion on held-out tasks and particularly strong benefits on complex tasks (28.5~pp scenario goal improvement, a 149\% relative increase).



---


# Tree of Thoughts: Deliberate Problem Solving with Large Language Models

**arXiv ID**: 2305.10601
**arXiv URL**: https://arxiv.org/abs/2305.10601

## Abstract

Language models are increasingly being deployed for general problem solving across a wide range of tasks, but are still confined to token-level, left-to-right decision-making processes during inference. This means they can fall short in tasks that require exploration, strategic lookahead, or where initial decisions play a pivotal role. To surmount these challenges, we introduce a new framework for language model inference, Tree of Thoughts (ToT), which generalizes over the popular Chain of Thought approach to prompting language models, and enables exploration over coherent units of text (thoughts) that serve as intermediate steps toward problem solving. ToT allows LMs to perform deliberate decision making by considering multiple different reasoning paths and self-evaluating choices to decide the next course of action, as well as looking ahead or backtracking when necessary to make global choices. Our experiments show that ToT significantly enhances language models' problem-solving abilities on three novel tasks requiring non-trivial planning or search: Game of 24, Creative Writing, and Mini Crosswords. For instance, in Game of 24, while GPT-4 with chain-of-thought prompting only solved 4% of tasks, our method achieved a success rate of 74%. Code repo with all prompts: https://github.com/princeton-nlp/tree-of-thought-llm.



---


# UI-Mem: Self-Evolving Experience Memory for Online Reinforcement Learning in Mobile GUI Agents

**arXiv ID**: 2602.05832
**arXiv URL**: https://arxiv.org/abs/2602.05832

## Abstract

Online Reinforcement Learning (RL) offers a promising paradigm for enhancing GUI agents through direct environment interaction. However, its effectiveness is severely hindered by inefficient credit assignment in long-horizon tasks and repetitive errors across tasks due to the lack of experience transfer. To address these challenges, we propose UI-Mem, a novel framework that enhances GUI online RL with a Hierarchical Experience Memory. Unlike traditional replay buffers, our memory accumulates structured knowledge, including high-level workflows, subtask skills, and failure patterns. These experiences are stored as parameterized templates that enable cross-task and cross-application transfer. To effectively integrate memory guidance into online RL, we introduce Stratified Group Sampling, which injects varying levels of guidance across trajectories within each rollout group to maintain outcome diversity, driving the unguided policy toward internalizing guided behaviors. Furthermore, a Self-Evolving Loop continuously abstracts novel strategies and errors to keep the memory aligned with the agent's evolving policy. Experiments on online GUI benchmarks demonstrate that UI-Mem significantly outperforms traditional RL baselines and static reuse strategies, with strong generalization to unseen applications. Project page: https://ui-mem.github.io



---


# UI-TARS-2 Technical Report: Advancing GUI Agent with Multi-Turn Reinforcement Learning

**arXiv ID**: 2509.02544
**arXiv URL**: https://arxiv.org/abs/2509.02544

## Abstract

The development of autonomous agents for graphical user interfaces (GUIs) presents major challenges in artificial intelligence. While recent advances in native agent models have shown promise by unifying perception, reasoning, action, and memory through end-to-end learning, open problems remain in data scalability, multi-turn reinforcement learning (RL), the limitations of GUI-only operation, and environment stability. In this technical report, we present UI-TARS-2, a native GUI-centered agent model that addresses these challenges through a systematic training methodology: a data flywheel for scalable data generation, a stabilized multi-turn RL framework, a hybrid GUI environment that integrates file systems and terminals, and a unified sandbox platform for large-scale rollouts. Empirical evaluation demonstrates that UI-TARS-2 achieves significant improvements over its predecessor UI-TARS-1.5. On GUI benchmarks, it reaches 88.2 on Online-Mind2Web, 47.5 on OSWorld, 50.6 on WindowsAgentArena, and 73.3 on AndroidWorld, outperforming strong baselines such as Claude and OpenAI agents. In game environments, it attains a mean normalized score of 59.8 across a 15-game suite-roughly 60% of human-level performance-and remains competitive with frontier proprietary models (e.g., OpenAI o3) on LMGame-Bench. Additionally, the model can generalize to long-horizon information-seeking tasks and software engineering benchmarks, highlighting its robustness across diverse agent tasks. Detailed analyses of training dynamics further provide insights into achieving stability and efficiency in large-scale agent RL. These results underscore UI-TARS-2's potential to advance the state of GUI agents and exhibit strong generalization to real-world interactive scenarios.



---


# Uncertainty-Aware GUI Agent: Adaptive Perception through Component Recommendation and Human-in-the-Loop Refinement

**arXiv ID**: 2508.04025
**arXiv URL**: https://arxiv.org/abs/2508.04025

## Abstract

Graphical user interface (GUI) agents have shown promise in automating mobile tasks but still struggle with input redundancy and decision ambiguity. In this paper, we present \textbf{RecAgent}, an uncertainty-aware agent that addresses these issues through adaptive perception. We distinguish two types of uncertainty in GUI navigation: (1) perceptual uncertainty, caused by input redundancy and noise from comprehensive screen information, and (2) decision uncertainty, arising from ambiguous tasks and complex reasoning. To reduce perceptual uncertainty, RecAgent employs a component recommendation mechanism that identifies and focuses on the most relevant UI elements. For decision uncertainty, it uses an interactive module to request user feedback in ambiguous situations, enabling intent-aware decisions. These components are integrated into a unified framework that proactively reduces input complexity and reacts to high-uncertainty cases via human-in-the-loop refinement. Additionally, we propose a dataset called \textbf{ComplexAction} to evaluate the success rate of GUI agents in executing specified single-step actions within complex scenarios. Extensive experiments validate the effectiveness of our approach. The dataset and code will be available at https://github.com/Fanye12/RecAgent.



---


# V-Zero: Self-Improving Multimodal Reasoning with Zero Annotation

**arXiv ID**: 2601.10094
**arXiv URL**: https://arxiv.org/abs/2601.10094

## Abstract

Recent advances in multimodal learning have significantly enhanced the reasoning capabilities of vision-language models (VLMs). However, state-of-the-art approaches rely heavily on large-scale human-annotated datasets, which are costly and time-consuming to acquire. To overcome this limitation, we introduce V-Zero, a general post-training framework that facilitates self-improvement using exclusively unlabeled images. V-Zero establishes a co-evolutionary loop by instantiating two distinct roles: a Questioner and a Solver. The Questioner learns to synthesize high-quality, challenging questions by leveraging a dual-track reasoning reward that contrasts intuitive guesses with reasoned results. The Solver is optimized using pseudo-labels derived from majority voting over its own sampled responses. Both roles are trained iteratively via Group Relative Policy Optimization (GRPO), driving a cycle of mutual enhancement. Remarkably, without a single human annotation, V-Zero achieves consistent performance gains on Qwen2.5-VL-7B-Instruct, improving visual mathematical reasoning by +1.7 and general vision-centric by +2.6, demonstrating the potential of self-improvement in multimodal systems. Code is available at https://github.com/SatonoDia/V-Zero



---


# VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought

**arXiv ID**: 2406.14596
**arXiv URL**: https://arxiv.org/abs/2406.14596

## Abstract

Large-scale generative language and vision-language models (LLMs and VLMs) excel in few-shot learning but require high-quality demonstrations. We propose In-Context Abstraction Learning (ICAL), enabling VLM agents to transform suboptimal trajectories into high-quality training data through self-reflection and human feedback. Given imperfect task demonstrations, a VLM abstracts trajectories into generalized strategies and action annotations by correcting inefficiencies and annotating cognitive abstractions: causal relationships, object state changes, temporal subgoals, and task-relevant visual elements. These annotations are iteratively refined through human feedback during execution in similar environments. The resulting examples significantly improve decision-making when used for retrieval-augmented generation or fine-tuning. As the agent's example library grows, it becomes more efficient at abstracting new examples, requiring less human feedback and fewer environment interactions. ICAL achieves state-of-the-art results across multiple benchmarks. In TEACh dialogue-based instruction following, combining fine-tuning and retrieval on ICAL examples outperforms raw human demonstrations and expert examples by 17.5% in goal-condition success. In VisualWebArena, retrieval-augmented GPT-4V with ICAL improves task success 1.6x, while fine-tuned Qwen2-VL achieves 2.8x improvement over the base model. In Ego4D action forecasting, we surpass few-shot GPT-4V and remain competitive with supervised models. Our approach scales 2x better than raw demonstrations and significantly reduces manual prompt engineering requirements.



---


# VLM-R1: A Stable and Generalizable R1-style Large Vision-Language Model

**arXiv ID**: 2504.07615
**arXiv URL**: https://arxiv.org/abs/2504.07615

## Abstract

Recently DeepSeek R1 has shown that reinforcement learning (RL) can substantially improve the reasoning capabilities of Large Language Models (LLMs) through a simple yet effective design. The core of R1 lies in its rule-based reward formulation, which leverages tasks with deterministic ground-truth answers to enable precise and stable reward computation. In the visual domain, we similarly observe that a wide range of visual understanding tasks are inherently equipped with well-defined ground-truth annotations. This property makes them naturally compatible with rule-based reward mechanisms. Motivated by this observation, we investigate the extension of R1-style reinforcement learning to Vision-Language Models (VLMs), aiming to enhance their visual reasoning capabilities. To this end, we develop VLM-R1, a dedicated framework designed to harness RL for improving VLMs' performance on general vision-language tasks. Using this framework, we further explore the feasibility of applying RL to visual domain. Experimental results indicate that the RL-based model not only delivers competitive performance on visual understanding tasks but also surpasses Supervised Fine-Tuning (SFT) in generalization ability. Furthermore, we conduct comprehensive ablation studies that uncover a series of noteworthy insights, including the presence of reward hacking in object detection, the emergence of the "OD aha moment", the impact of training data quality, and the scaling behavior of RL across different model sizes. Through these analyses, we aim to deepen the understanding of how reinforcement learning enhances the capabilities of vision-language models, and we hope our findings and open-source contributions will support continued progress in the vision-language RL community. Our code and model are available at https://github.com/om-ai-lab/VLM-R1



---


# Vision-R1: Evolving Human-Free Alignment in Large Vision-Language Models via Vision-Guided Reinforcement Learning

**arXiv ID**: 2503.18013
**arXiv URL**: https://arxiv.org/abs/2503.18013

## Abstract

Large Vision-Language Models (LVLMs) typically follow a two-stage training paradigm-pretraining and supervised fine-tuning. Recently, preference optimization, derived from the language domain, has emerged as an effective post-training reinforcement strategy to enhance capabilities of LVLMs. However, constructing high-quality human-annotated preference data and developing robust reward models to mimic these preferences are both costly and challenging. Motivated by this observation, we propose Vision-R1, a novel vision-guided R1-like reinforcement learning algorithm for LVLMs that rewards models with definitive vision feedback. It only leverages curated instruction data, eliminating the need for specialized reward models and handcrafted preference datasets. We incorporate a criterion-driven reward function that further integrates multi-dimensional feedback to evaluate model completions comprehensively based on the vision task logic. Furthermore, we introduce a progressive rule refinement strategy that dynamically adjusts the reward criteria during training, enabling continuous model improvement and mitigating reward hacking. Extensive experiments on both in-distribution and out-of-distribution benchmarks demonstrate that fine-tuning the 7B LVLMs with Vision-R1 achieves consistent performance gains, with even up to 50% improvement and surpassing the state-of-the-art 10x size model.



---


# Visual Test-time Scaling for GUI Agent Grounding

**arXiv ID**: 2505.00684
**arXiv URL**: https://arxiv.org/abs/2505.00684

## Abstract

We introduce RegionFocus, a visual test-time scaling approach for Vision Language Model Agents. Understanding webpages is challenging due to the visual complexity of GUI images and the large number of interface elements, making accurate action selection difficult. Our approach dynamically zooms in on relevant regions, reducing background clutter and improving grounding accuracy. To support this process, we propose an image-as-map mechanism that visualizes key landmarks at each step, providing a transparent action record and enables the agent to effectively choose among action candidates. Even with a simple region selection strategy, we observe significant performance gains of 28+\% on Screenspot-pro and 24+\% on WebVoyager benchmarks on top of two state-of-the-art open vision language model agents, UI-TARS and Qwen2.5-VL, highlighting the effectiveness of visual test-time scaling in interactive settings. We achieve a new state-of-the-art grounding performance of 61.6\% on the ScreenSpot-Pro benchmark by applying RegionFocus to a Qwen2.5-VL-72B model. Our code will be released publicly at https://github.com/tiangeluo/RegionFocus.



---


# Voyager: An Open-Ended Embodied Agent with Large Language Models

**arXiv ID**: 2305.16291
**arXiv URL**: https://arxiv.org/abs/2305.16291

## Abstract

We introduce Voyager, the first LLM-powered embodied lifelong learning agent in Minecraft that continuously explores the world, acquires diverse skills, and makes novel discoveries without human intervention. Voyager consists of three key components: 1) an automatic curriculum that maximizes exploration, 2) an ever-growing skill library of executable code for storing and retrieving complex behaviors, and 3) a new iterative prompting mechanism that incorporates environment feedback, execution errors, and self-verification for program improvement. Voyager interacts with GPT-4 via blackbox queries, which bypasses the need for model parameter fine-tuning. The skills developed by Voyager are temporally extended, interpretable, and compositional, which compounds the agent's abilities rapidly and alleviates catastrophic forgetting. Empirically, Voyager shows strong in-context lifelong learning capability and exhibits exceptional proficiency in playing Minecraft. It obtains 3.3x more unique items, travels 2.3x longer distances, and unlocks key tech tree milestones up to 15.3x faster than prior SOTA. Voyager is able to utilize the learned skill library in a new Minecraft world to solve novel tasks from scratch, while other techniques struggle to generalize. We open-source our full codebase and prompts at https://voyager.minedojo.org/.



---


# WISE-Flow: Workflow-Induced Structured Experience for Self-Evolving Conversational Service Agents

**arXiv ID**: 2601.08158
**arXiv URL**: https://arxiv.org/abs/2601.08158

## Abstract

Large language model (LLM)-based agents are widely deployed in user-facing services but remain error-prone in new tasks, tend to repeat the same failure patterns, and show substantial run-to-run variability. Fixing failures via environment-specific training or manual patching is costly and hard to scale. To enable self-evolving agents in user-facing service environments, we propose WISE-Flow, a workflow-centric framework that converts historical service interactions into reusable procedural experience by inducing workflows with prerequisite-augmented action blocks. At deployment, WISE-Flow aligns the agent's execution trajectory to retrieved workflows and performs prerequisite-aware feasibility reasoning to achieve state-grounded next actions. Experiments on ToolSandbox and $τ^2$-bench show consistent improvement across base models.



---


# Watch Every Step! LLM Agent Learning via Iterative Step-Level Process Refinement

**arXiv ID**: 2406.11176
**arXiv URL**: https://arxiv.org/abs/2406.11176

## Abstract

Large language model agents have exhibited exceptional performance across a range of complex interactive tasks. Recent approaches have utilized tuning with expert trajectories to enhance agent performance, yet they primarily concentrate on outcome rewards, which may lead to errors or suboptimal actions due to the absence of process supervision signals. In this paper, we introduce the Iterative step-level Process Refinement (IPR) framework, which provides detailed step-by-step guidance to enhance agent training. Specifically, we adopt the Monte Carlo method to estimate step-level rewards. During each iteration, the agent explores along the expert trajectory and generates new actions. These actions are then evaluated against the corresponding step of expert trajectory using step-level rewards. Such comparison helps identify discrepancies, yielding contrastive action pairs that serve as training data for the agent. Our experiments on three complex agent tasks demonstrate that our framework outperforms a variety of strong baselines. Moreover, our analytical findings highlight the effectiveness of IPR in augmenting action efficiency and its applicability to diverse models.



---


# Weak-for-Strong: Training Weak Meta-Agent to Harness Strong Executors

**arXiv ID**: 2504.04785
**arXiv URL**: https://arxiv.org/abs/2504.04785

## Abstract

Efficiently leveraging of the capabilities of contemporary large language models (LLMs) is increasingly challenging, particularly when direct fine-tuning is expensive and often impractical. Existing training-free methods, including manually or automated designed workflows, typically demand substantial human effort or yield suboptimal results. This paper proposes Weak-for-Strong Harnessing (W4S), a novel framework that customizes smaller, cost-efficient language models to design and optimize workflows for harnessing stronger models. W4S formulates workflow design as a multi-turn markov decision process and introduces reinforcement learning for agentic workflow optimization (RLAO) to train a weak meta-agent. Through iterative interaction with the environment, the meta-agent learns to design increasingly effective workflows without manual intervention. Empirical results demonstrate the superiority of W4S that our 7B meta-agent, trained with just one GPU hour, outperforms the strongest baseline by 2.9% ~ 24.6% across eleven benchmarks, successfully elevating the performance of state-of-the-art models such as GPT-3.5-Turbo and GPT-4o. Notably, W4S exhibits strong generalization capabilities across both seen and unseen tasks, offering an efficient, high-performing alternative to directly fine-tuning strong models.



---


# WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance

**arXiv ID**: 2511.12997
**arXiv URL**: https://arxiv.org/abs/2511.12997

## Abstract

Multimodal LLM-powered agents have recently demonstrated impressive capabilities in web navigation, enabling agents to complete complex browsing tasks across diverse domains. However, current agents struggle with repetitive errors and lack the ability to learn from past experiences across sessions, limiting their long-term robustness and sample efficiency. We introduce WebCoach, a model-agnostic self-evolving framework that equips web browsing agents with persistent cross-session memory, enabling improved long-term planning, reflection, and continual learning without retraining. WebCoach consists of three key components: (1) a WebCondenser, which standardizes raw navigation logs into concise summaries; (2) an External Memory Store, which organizes complete trajectories as episodic experiences; and (3) a Coach, which retrieves relevant experiences based on similarity and recency, and decides whether to inject task-specific advice into the agent via runtime hooks. This design empowers web agents to access long-term memory beyond their native context window, improving robustness in complex browsing tasks. Moreover, WebCoach achieves self-evolution by continuously curating episodic memory from new navigation trajectories, enabling agents to improve over time without retraining. Evaluations on the WebVoyager benchmark demonstrate that WebCoach consistently improves the performance of browser-use agents across three different LLM backbones. With a 38B model, it increases task success rates from 47% to 61% while reducing or maintaining the average number of steps. Notably, smaller base models with WebCoach achieve performance comparable to the same web agent using GPT-4o.



---


# WebEvolver: Enhancing Web Agent Self-Improvement with Coevolving World Model

**arXiv ID**: 2504.21024
**arXiv URL**: https://arxiv.org/abs/2504.21024

## Abstract

Agent self-improvement, where the backbone Large Language Model (LLM) of the agent are trained on trajectories sampled autonomously based on their own policies, has emerged as a promising approach for enhancing performance. Recent advancements, particularly in web environments, face a critical limitation: their performance will reach a stagnation point during autonomous learning cycles, hindering further improvement. We argue that this stems from limited exploration of the web environment and insufficient exploitation of pre-trained web knowledge in LLMs. To improve the performance of self-improvement, we propose a novel framework that introduces a co-evolving World Model LLM. This world model predicts the next observation based on the current observation and action within the web environment. Leveraging LLMs' pretrained knowledge of abundant web content, the World Model serves dual roles: (1) as a virtual web server generating self-instructed training data to continuously refine the agent's policy, and (2) as an imagination engine during inference, enabling look-ahead simulation to guide action selection for the agent LLM. Experiments in real-world web environments (Mind2Web-Live, WebVoyager, and GAIA-web) show a 10% performance gain over existing self-evolving agents, demonstrating the efficacy and generalizability of our approach, without using any distillation from more powerful close-sourced models. Our work establishes the necessity of integrating world models into autonomous agent frameworks to unlock sustained adaptability. Code is available at https://github.com/Tencent/SelfEvolvingAgent



---


# WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents

**arXiv ID**: 2207.01206
**arXiv URL**: https://arxiv.org/abs/2207.01206

## Abstract

Existing benchmarks for grounding language in interactive environments either lack real-world linguistic elements, or prove difficult to scale up due to substantial human involvement in the collection of data or feedback signals. To bridge this gap, we develop WebShop -- a simulated e-commerce website environment with $1.18$ million real-world products and $12,087$ crowd-sourced text instructions. Given a text instruction specifying a product requirement, an agent needs to navigate multiple types of webpages and issue diverse actions to find, customize, and purchase an item. WebShop provides several challenges for language grounding including understanding compositional instructions, query (re-)formulation, comprehending and acting on noisy text in webpages, and performing strategic exploration. We collect over $1,600$ human demonstrations for the task, and train and evaluate a diverse range of agents using reinforcement learning, imitation learning, and pre-trained image and language models. Our best model achieves a task success rate of $29\%$, which outperforms rule-based heuristics ($9.6\%$) but is far lower than human expert performance ($59\%$). We also analyze agent and human trajectories and ablate various model components to provide insights for developing future agents with stronger language understanding and decision making abilities. Finally, we show that agents trained on WebShop exhibit non-trivial sim-to-real transfer when evaluated on amazon.com and ebay.com, indicating the potential value of WebShop in developing practical web-based agents that can operate in the wild.



---


# WebSynthesis: World-Model-Guided MCTS for Efficient WebUI-Trajectory Synthesis

**arXiv ID**: 2507.04370
**arXiv URL**: https://arxiv.org/abs/2507.04370

## Abstract

Recent advancements in large language models (LLMs) have significantly improved the capabilities of web agents. However, effectively navigating complex and dynamic web environments still requires more advanced trajectory-level planning and execution. Prior studies have addressed self-improving agents by collecting extensive GUI trajectories from real-environment interactions. Despite their effectiveness, these approaches encounter two critical challenges: (1) Uncontrollable environment states, where real or sandboxed web environments often yield unstable and non-deterministic feedback, complicating the reproduction and debugging of agent behaviors; and (2) High API costs, as generating even a single interaction trajectory can involve hundreds of queries, leading to considerable API usage and computational expenses. To address these limitations and enable scalable self-improvement for agents, we propose WebSynthesis, a novel framework for trajectory synthesis and training. WebSynthesis leverages a learned world model to simulate virtual web environments, allowing a policy agent to perform efficient and reversible tree-based planning. This approach supports the large-scale generation of diverse and high-quality trajectories, which are subsequently utilized to refine the agent's policy. Experimental results demonstrate that an agent trained using WebSynthesis on a small-scale synthetic dataset achieves performance comparable to or even surpassing that of models trained on large-scale real-world data.



---


# When Agents go Astray: Course-Correcting SWE Agents with PRMs

**arXiv ID**: 2509.02360
**arXiv URL**: https://arxiv.org/abs/2509.02360

## Abstract

Large Language Model (LLM) agents are increasingly deployed for complex, multi-step software engineering (SWE) tasks. However, their trajectories often contain costly inefficiencies, such as redundant exploration, looping, and failure to terminate once a solution is reached. Prior work has largely treated these errors in a post-hoc manner, diagnosing failures only after execution. In this paper, we introduce SWE-PRM, an inference-time Process Reward Model (PRM) that intervenes during execution to detect and course-correct trajectory-level errors. Our PRM design leverages a taxonomy of common inefficiencies and delivers lightweight, interpretable feedback without modifying the underlying policy. On SWE-bench Verified, closed-source PRMs improve resolution from 40.0% to 50.6% (+10.6 p.p.), with the largest gains on medium and hard tasks. Among feedback strategies, taxonomy-guided PRMs outperform unguided or explicit action-prescriptive variants, increasing success rate while reducing trajectory length. These benefits come at an acceptable added inference cost of as low as $0.2, making PRMs a practical and scalable mechanism for improving SWE agents' reliability and efficiency.



---


# Where LLM Agents Fail and How They can Learn From Failures

**arXiv ID**: 2509.25370
**arXiv URL**: https://arxiv.org/abs/2509.25370

## Abstract

Large Language Model (LLM) agents, which integrate planning, memory, reflection, and tool-use modules, have shown promise in solving complex, multi-step tasks. Yet their sophisticated architectures amplify vulnerability to cascading failures, where a single root-cause error propagates through subsequent decisions, leading to task failure. Current systems lack a framework that can comprehensively understand agent error in a modular and systemic way, and therefore fail to detect these errors accordingly. We address this gap with three contributions. First, we introduce the AgentErrorTaxonomy, a modular classification of failure modes spanning memory, reflection, planning, action, and system-level operations. Second, we construct AgentErrorBench, the first dataset of systematically annotated failure trajectories from ALFWorld, GAIA, and WebShop, grounding error analysis in real-world agent rollouts. Third, we propose AgentDebug, a debugging framework that isolates root-cause failures and provides corrective feedback, enabling agents to recover and iteratively improve. Experiments on AgentErrorBench show that AgentDebug achieves 24% higher all-correct accuracy and 17% higher step accuracy compared to the strongest baseline. Beyond detection, the targeted feedback generated by AgentDebug enables LLM agents to iteratively recover from failures, yielding up to 26% relative improvements in task success across ALFWorld, GAIA, and WebShop. These results establish principled debugging as a pathway to more reliable and adaptive LLM agents. The code and data will be available at https://github.com/ulab-uiuc/AgentDebug



---


# WizardLM: Empowering large pre-trained language models to follow complex instructions

**arXiv ID**: 2304.12244
**arXiv URL**: https://arxiv.org/abs/2304.12244

## Abstract

Training large language models (LLMs) with open-domain instruction following data brings colossal success. However, manually creating such instruction data is very time-consuming and labor-intensive. Moreover, humans may struggle to produce high-complexity instructions. In this paper, we show an avenue for creating large amounts of instruction data with varying levels of complexity using LLM instead of humans. Starting with an initial set of instructions, we use our proposed Evol-Instruct to rewrite them step by step into more complex instructions. Then, we mix all generated instruction data to fine-tune LLaMA. We call the resulting model WizardLM. Human evaluations on a complexity-balanced test bed and Vicuna's testset show that instructions from Evol-Instruct are superior to human-created ones. By analyzing the human evaluation results of the high complexity part, we demonstrate that outputs from our WizardLM are preferred to outputs from OpenAI ChatGPT. In GPT-4 automatic evaluation, WizardLM achieves more than 90\% capacity of ChatGPT on 17 out of 29 skills. Even though WizardLM still lags behind ChatGPT in some aspects, our findings suggest that fine-tuning with AI-evolved instructions is a promising direction for enhancing LLMs. Our code and data are public at https://github.com/nlpxucan/WizardLM



---


# XSkill: Continual Learning from Experience and Skills in Multimodal Agents

**arXiv ID**: 2603.12056
**arXiv URL**: https://arxiv.org/abs/2603.12056

## Abstract

Multimodal agents can now tackle complex reasoning tasks with diverse tools, yet they still suffer from inefficient tool use and inflexible orchestration in open-ended settings. A central challenge is enabling such agents to continually improve without parameter updates by learning from past trajectories. We identify two complementary forms of reusable knowledge essential for this goal: experiences, providing concise action-level guidance for tool selection and decision making, and skills, providing structured task-level guidance for planning and tool use. To this end, we propose XSkill, a dual-stream framework for continual learning from experience and skills in multimodal agents. XSkill grounds both knowledge extraction and retrieval in visual observations. During accumulation, XSkill distills and consolidates experiences and skills from multi-path rollouts via visually grounded summarization and cross-rollout critique. During inference, it retrieves and adapts this knowledge to the current visual context and feeds usage history back into accumulation to form a continual learning loop. Evaluated on five benchmarks across diverse domains with four backbone models, XSkill consistently and substantially outperforms both tool-only and learning-based baselines. Further analysis reveals that the two knowledge streams play complementary roles in influencing the reasoning behaviors of agents and show superior zero-shot generalization.



---


# Zep: A Temporal Knowledge Graph Architecture for Agent Memory

**arXiv ID**: 2501.13956
**arXiv URL**: https://arxiv.org/abs/2501.13956

## Abstract

We introduce Zep, a novel memory layer service for AI agents that outperforms the current state-of-the-art system, MemGPT, in the Deep Memory Retrieval (DMR) benchmark. Additionally, Zep excels in more comprehensive and challenging evaluations than DMR that better reflect real-world enterprise use cases. While existing retrieval-augmented generation (RAG) frameworks for large language model (LLM)-based agents are limited to static document retrieval, enterprise applications demand dynamic knowledge integration from diverse sources including ongoing conversations and business data. Zep addresses this fundamental limitation through its core component Graphiti -- a temporally-aware knowledge graph engine that dynamically synthesizes both unstructured conversational data and structured business data while maintaining historical relationships. In the DMR benchmark, which the MemGPT team established as their primary evaluation metric, Zep demonstrates superior performance (94.8% vs 93.4%). Beyond DMR, Zep's capabilities are further validated through the more challenging LongMemEval benchmark, which better reflects enterprise use cases through complex temporal reasoning tasks. In this evaluation, Zep achieves substantial results with accuracy improvements of up to 18.5% while simultaneously reducing response latency by 90% compared to baseline implementations. These results are particularly pronounced in enterprise-critical tasks such as cross-session information synthesis and long-term context maintenance, demonstrating Zep's effectiveness for deployment in real-world applications.
