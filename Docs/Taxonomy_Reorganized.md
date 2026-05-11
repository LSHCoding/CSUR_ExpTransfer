# Taxonomy — Reorganized by Carrier Transformation Pathway (V2)

## 0. 符号与标注约定

**Carrier 记号**
- `N-Tok` = Narrative Tokenized（反思、摘要、规则、insight、skill 文本描述、raw trajectories）
- `S-Tok` = Schematic Tokenized（code、workflow、SOP、graph、API spec、decision tree）
- `Lat` = Latent（KV cache、prefix cache、activation、learnable soft prompt、continuous memory token、trained composer 输出的 latent）
- `π-Par` = Policy Parameter（LLM/VLA/GUI agent 权重、LoRA）
- `V-Par` = Evaluator Parameter（RM、PRM、verifier、critic、judge）

> Latent 不作进一步子类划分（见 `Experience_Carrier.md`）。需要时可用属性标签 `[session-scoped]`（如 KV cache、prefix cache）/ `[cross-session]`（如 learnable soft prompt、trained composer）区分实现形态。

**Raw 的归属**：`N-Tok (raw)` = 最低抽象度的 Narrative Tokenized；`N-Tok (refined)` = 经语义抽象的 Narrative。

**正交属性**
- Modality：`[txt]` / `[vis+txt]` / `[GUI]` / `[embodied]` / `[cross-modal]`
- Source：`{self}` / `{human}` / `{teacher}`
- Method：`⟨LLM-extract⟩`（无参数更新） / `⟨SFT⟩` / `⟨RL: GRPO/PPO/DPO/ReST⟩` / `⟨hybrid⟩`

**Pathway 记号**：`X → Y` 表示 Carrier X 到 Y 的单步转化；多步组合用 `X → Y → Z` 并在 §8 单列讨论。

**V2 新增标注约定**：
- `[Abs: "关键短语"]` — 表示该信息来自 abstract 原文关键短语（≤15 词）
- `[Abs confirms]` — abstract 确认了 V1 已有标注
- `[CANDIDATE_NEW_ENTRY]` — abstract 中存在但尚未进入 Taxonomy.md 的论文
- `[CANDIDATE_NEW_PATTERN]` — 从 abstract 中识别出的候选新复合模式
- `UNCLEAR (abstract-only)` — abstract 信息不足以判定


---

## 1. Pathway P1：Narrative → Narrative（intra-Tokenized abstraction）

> **本质**：在 Tokenized 层内提升抽象程度，保留可读性与可编辑性；raw trajectories 被提炼为 reflection / summary / rule / insight / skill description / procedural memory。源与目标都是 Narrative Tokenized，同层语义抽象。多数工作无参数更新，复用方式为 retrieve-and-prepend。

### 1.1 Reflection / Insight 类产物（事后反省型抽象）

| Work | Transformation | Tags | Note |
|---|---|---|---|
| Reflexion | `N-Tok (raw) → N-Tok (reflection)` | [txt] {self} ⟨LLM-extract⟩ | 奠基性工作；verbal RL 存入 episodic memory buffer；[Abs: "reinforce language agents not by updating weights, but instead through linguistic feedback"] |
| ExpeL | `N-Tok (raw) → N-Tok (reflection + insights)` | [txt] {self} ⟨LLM-extract⟩ | 自主经验收集+自然语言知识抽取；[Abs: "autonomously gathers experiences and extracts knowledge using natural language"]；跨任务迁移验证 |
| Experiential Reflective Learning / H²R | `N-Tok (raw) → N-Tok (reflection)` | [txt] {self} ⟨LLM-extract⟩ | ERL: [Abs: "reflects on task trajectories and outcomes to generate heuristics"]；H²R: 层级化 hindsight reflection；解耦 high-level planning 与 low-level execution memory |
| MAR | `N-Tok (raw) → N-Tok (reflection + feedback)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "multi-agent with multi-persona debators as the method to generate reflections"]；缓解 thought degeneration |
| Agent S | `N-Tok (raw) → N-Tok (summary + reflection)` | [vis+txt, GUI] {self} ⟨LLM-extract⟩ | [Abs: "experience-augmented hierarchical planning, which learns from external knowledge search and internal experience retrieval"]；Domain: OSWorld |
| ELITE | `N-Tok (raw) → N-Tok (summary)` | [vis+txt, embodied] {self} ⟨LLM-extract⟩ | [Abs: "self-reflective knowledge construction and intent-aware retrieval"; "continuously learn from their own environment interaction experiences"]；Domain: EB-ALFRED, EB-Habitat |
| Aligning Agentic World Models | `N-Tok (raw) → N-Tok (heuristic + causal rule + reflection)` | [vis+txt] {self} ⟨LLM-extract⟩ | [Abs: "autonomously constructs a symbolic World Knowledge Repository"; "Process Experience to enforce physical feasibility"; "Goal Experience to guide task optimality"] |

**完整题目**
- Reflexion — *Reflexion: Language Agents with Verbal Reinforcement Learning*
- ExpeL — *ExpeL: LLM Agents Are Experiential Learners*
- Experiential Reflective Learning / H²R — *Experiential Reflective Learning for Self-Improving LLM Agents* / *H²R: Hierarchical Hindsight Reflection for Multi-Task LLM Agents*
- MAR — *MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs*
- Agent S — *Agent S: An Open Agentic Framework that Uses Computers Like a Human*
- ELITE — *ELITE: Experiential Learning and Intent-Aware Transfer for Self-improving Embodied Agents*
- Aligning Agentic World Models — *Aligning Agentic World Models via Knowledgeable Experience Learning*

### 1.2 Summary / Cheatsheet 类产物（压缩型抽象）

| Work | Transformation | Tags | Note |
|---|---|---|---|
| AgentEHR | `N-Tok (raw) → N-Tok (summary)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "RetroSum, a novel framework that unifies a retrospective summarization mechanism with an evolving experience strategy"]；clinical EHR decision-making |
| Dynamic Cheatsheet | `N-Tok (raw) → N-Tok (adaptive cheatsheet)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "lightweight framework that endows a black-box LM with a persistent, evolving memory"; "self-curated, focusing on concise, transferable snippets"]；无参数更新 |
| AutoAgent | `N-Tok (raw) → N-Tok (summary)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "closed-loop cognitive evolution process"; "Elastic Memory Orchestrator dynamically organizes interaction history"]；见 §2.3 亦有 Schematic 产物 |
| GEMS | `N-Tok (raw) → N-Tok (summaries + reflections)` | [cross-modal] {self} ⟨LLM-extract⟩ | [Abs: "persistent, trajectory-level memory that hierarchically stores both factual states and compressed experiential summaries"]；agent-native multimodal generation |

**完整题目**
- AgentEHR — *AgentEHR: Advancing Autonomous Clinical Decision-Making via Retrospective Summarization*
- Dynamic Cheatsheet — *Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory*
- AutoAgent — *AutoAgent: Evolving Cognition and Elastic Memory Orchestration for Adaptive Agents*
- GEMS — *GEMS: Agent-Native Multimodal Generation with Memory and Skills*

### 1.3 Rule / Guideline / Principle 类产物（规范型抽象）

| Work | Transformation | Tags | Note |
|---|---|---|---|
| AutoManual | `N-Tok (raw) → N-Tok (rule + reflection)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "categorizes environmental knowledge into diverse rules and optimizes them in an online fashion"]；Planner+Builder+Formulator 三角色 |
| AutoGuide | `N-Tok (raw) → N-Tok (context-aware guideline)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "automatically generating context-aware guidelines from offline experiences"; "each context-aware guideline is expressed in concise natural language and follows a conditional structure"] |
| JEF-Hinter | `N-Tok (raw) → N-Tok (hints)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "distills offline traces into compact, context-aware hints"; "zooming mechanism highlights decisive steps in long trajectories"]；leverages both successful and failed trajectories |
| Training-Free GRPO | `N-Tok (raw) → N-Tok (rule + reflection + summary)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "leverages the group relative semantic advantage instead of numerical ones"; "iteratively distilling high-quality experiential knowledge"]；token prior 机制 |
| Trajectory-Informed Memory Generation | `N-Tok (raw) → N-Tok (rule + reflection + summary)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "Trajectory Intelligence Extractor"; "Decision Attribution Analyzer"; "produces three types of guidance -- strategy tips, recovery tips, and optimization tips"] |
| WebCoach | `N-Tok (raw) → N-Tok (advice)` | [vis+txt, web] {self} ⟨LLM-extract⟩ | [Abs: "WebCondenser standardizes raw navigation logs; Coach retrieves relevant experiences and injects task-specific advice via runtime hooks"; "self-evolution by continuously curating episodic memory from new navigation trajectories"]；cross-session memory；WebVoyager 47%→61% |

**完整题目**
- AutoManual — *AutoManual: Constructing Instruction Manuals by LLM Agents via Interactive Environmental Learning*
- AutoGuide — *AutoGuide: Automated Generation and Selection of Context-Aware Guidelines for Large Language Model Agents*
- JEF-Hinter — *JEF-Hinter: Leveraging Offline Knowledge for Improving Web Agents Adaptation*
- Training-Free GRPO — *Training-Free Group Relative Policy Optimization*
- Trajectory-Informed Memory Generation — *Trajectory-Informed Memory Generation for Self-Improving Agent Systems*
- WebCoach — *WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance*

> Agentic Rubrics 的主要贡献为 `π-Par → N-Tok`（P7），已移至 §7。

### 1.4 Skill-description 类产物（可复用能力的自然语言描述）

> 注：若 skill 以 code/API/typed library 形式存在，归入 §2。本小节限于 skill 以 natural-language description 形式存在者。

| Work | Transformation | Tags | Note |
|---|---|---|---|
| AutoSkill | `N-Tok (raw) → N-Tok (skill description)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "abstracts skills from user experience, supports their continual self-evolution, and dynamically injects relevant skills into future requests"]；model-agnostic plugin layer |
| Contextual Experience Replay | `N-Tok (raw) → N-Tok (skill)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "accumulates and synthesizes past experiences into a dynamic memory buffer"; "experiences encompass environment dynamics and common decision-making patterns"]；Domain: web navigation |
| EvoSkill | `N-Tok (raw) → N-Tok (skill)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "automatically discovers and refines agent skills through iterative failure analysis"; "Pareto frontier of agent programs governs selection"] |
| Skill Set Optimization | `N-Tok (raw) → N-Tok (skill)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "constructing and refining sets of transferable skills"; "extracting common subtrajectories with high rewards and generating subgoals and instructions"] |
| Trace2Skill | `N-Tok (raw) → N-Tok (skill)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "dispatches a parallel fleet of sub-agents to analyze a diverse pool of executions"; "hierarchically consolidate them into a unified, conflict-free skill directory"]；cross-model transferable |
| EvoTool | `N-Tok (raw) → N-Tok (tool-use policy text)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "decomposes agent's tool-use policy into four modules"; "Trajectory-Grounded Blame Attribution uses diagnostic traces to localize failures"]；gradient-free evolutionary |
| XSkill | `N-Tok (raw) → N-Tok (skill)` | [vis+txt] {self} ⟨LLM-extract⟩ | [Abs: "dual-stream framework for continual learning from experience and skills"; "grounds both knowledge extraction and retrieval in visual observations"] |
| SkillClaw | `N-Tok (raw, vis+txt) → N-Tok (skill)` | [vis+txt] {self} ⟨LLM-extract⟩ | [Abs: "collective skill evolution in multi-user agent ecosystems"; "continuously aggregates trajectories generated during use"]；cross-user knowledge transfer |

**完整题目**
- AutoSkill — *AutoSkill: Experience-Driven Lifelong Learning via Skill Self-Evolution*
- Contextual Experience Replay — *Contextual Experience Replay for Self-Improvement of Language Agents*
- EvoSkill — *EvoSkill: Automated Skill Discovery for Multi-Agent Systems*
- Skill Set Optimization — *Skill Set Optimization: Reinforcing Language Model Behavior via Transferable Skills*
- Trace2Skill — *Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills*
- EvoTool — *EvoTool: Self-Evolving Tool-Use Policy Optimization in LLM Agents via Blame-Aware Mutation and Diversity-Aware Selection*
- XSkill — *XSkill: Continual Learning from Experience and Skills in Multimodal Agents*
- SkillClaw — *SkillClaw: Let Skills Evolve Collectively with Agentic Evolver*

### 1.5 Strategy / Heuristic 类产物（元认知型抽象）

| Work | Transformation | Tags | Note |
|---|---|---|---|
| FLEX / Human-Inspired Continuous Learning | `N-Tok (raw) → N-Tok (strategy)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "gradient-free learning paradigm that enables LLM agents to continuously evolve through accumulated experience"; "identify a clear scaling law of experiential growth and the phenomenon of experience inheritance"] |
| Learn Like Humans | `N-Tok (raw) → N-Tok (strategy)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "integrating principle-based reflection (abstracting normative rules) and procedural reflection (deriving step-by-step strategies)"; "achieves efficient self-evolution within a single recurrence cycle"] |

**完整题目**
- FLEX — *FLEX: Continuous Agent Evolution via Forward Learning from Experience* (亦作 *Human-Inspired Continuous Learning of Internal Reasoning Processes: Learning How to Think for Adaptive AI Systems*)
- Learn Like Humans — *Learn Like Humans: Use Meta-cognitive Reflection for Efficient Self-Improvement*

### 1.6 Procedural-Memory 类产物（程序性记忆，natural language 承载）

| Work | Transformation | Tags | Note |
|---|---|---|---|
| Mem^p | `N-Tok (raw) → N-Tok (procedural)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "distills past agent trajectories into both fine-grained, step-by-step instructions and higher-level, script-like abstractions"]；cross-model transfer 验证 |
| Learning Hierarchical Procedural Memory | `N-Tok (raw) → N-Tok (procedural)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "decouples reasoning from learning by maintaining a frozen LLM while performing all adaptation in an external hierarchical procedural memory"; "2800 times faster than LLM parameter-training"] |
| ProcMEM | `N-Tok (raw) → N-Tok (procedural)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "transforms passive episodic narratives into executable Skills defined by activation, execution, and termination conditions"; "Non-Parametric PPO"] |
| Remember Me, Refine Me | `N-Tok (raw) → N-Tok (procedural)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "multi-faceted distillation"; "context-adaptive reuse"; "utility-based refinement"; "8B+ReMe > memoryless 14B"] |
| Learning How to Remember | `N-Tok (raw) → N-Tok (meta-cognitive)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "treats memory abstraction as a learnable cognitive skill rather than a fixed design choice"; "memory copilot is trained using direct preference optimization"] |
| HiMem | `N-Tok (raw) → N-Tok (note memory + episode memory)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "hierarchical long-term memory with Topic-Aware Event-Surprise Dual-Channel Segmentation"; "Note Memory captures stable knowledge through multi-stage information extraction"]；memory reconsolidation 机制；long-horizon dialogues |

**完整题目**
- Mem^p — *Mem^p: Exploring Agent Procedural Memory*
- Learning Hierarchical Procedural Memory — *Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement*
- ProcMEM — *ProcMEM: Learning Reusable Procedural Memory from Experience via Non-Parametric PPO for LLM Agents*
- Remember Me, Refine Me — *Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution*
- Learning How to Remember — *Learning How to Remember: A Meta-Cognitive Management Method for Structured and Transferable Agent Memory*
- HiMem — *HiMem: Hierarchical Long-Term Memory for LLM Long-Horizon Agents*

### 1.7 Generic / Hybrid 类产物（难以严格归入上述子类）

| Work | Transformation | Tags | Note |
|---|---|---|---|
| MemEvolve | `N-Tok (raw) → N-Tok` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "meta-evolutionary framework that jointly evolves agents' experiential knowledge and their memory architecture"]；EvolveLab 统一 codebase |
| MemSkill | `N-Tok (raw) → N-Tok` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "reframes memory operations as learnable and evolvable memory skills"; "controller learns to select relevant skills, paired with LLM-based executor"] |
| MemRL / Meta-Policy Reflexion | `N-Tok (raw) → N-Tok` | [txt] {self} ⟨LLM-extract⟩ | MemRL: [Abs: "non-parametric approach that evolves via reinforcement learning on episodic memory"; "Two-Phase Retrieval mechanism"]；MPR: [Abs: "consolidates LLM-generated reflections into a structured, predicate-like Meta-Policy Memory"] |
| Iterative Experience Refinement | `N-Tok (raw) → N-Tok (shortcut experience)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "two fundamental patterns: the successive pattern and the cumulative pattern"; "experience elimination facilitates achieving better performance using just 11.54%"] |
| ReasoningBank | `N-Tok (raw) → N-Tok` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "distills generalizable reasoning strategies from an agent's self-judged successful and failed experiences"; "memory-aware test-time scaling (MaTTS)"] |
| ReCreate | `N-Tok (raw) → N-Tok`（★关注） | [txt] {self} ⟨LLM-extract⟩ | [Abs: "experience-driven framework for the automatic creation of domain agents"; "agent-as-optimizer paradigm"; "hierarchical updates that abstract instance-level details into reusable domain patterns"] |
| SE-Agent | `N-Tok (raw) → N-Tok` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "revisits and enhances former pilot trajectories through three key operations: revision, recombination, and refinement"]；SWE-bench Verified SOTA |
| R⁴ | `N-Tok (raw, vis+txt) → N-Tok (txt)` | [vis+txt, 4D] {self} ⟨LLM-extract⟩ | [Abs: "continuously constructs a 4D knowledge database by anchoring object-level semantic descriptions in metric space and time"]；training-free |
| Self-Consolidation (N-Tok 分支) | `N-Tok (raw) → N-Tok` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "contrastive reflection strategy to explicitly summarize error-prone patterns and capture reusable insights"]；另有 Lat 分支见 §3 |

**完整题目**
- MemEvolve — *MemEvolve: Meta-Evolution of Agent Memory Systems*
- MemSkill — *MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents*
- MemRL — *MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory*
- Meta-Policy Reflexion — *Meta-Policy Reflexion: Reusable Reflective Memory and Rule Admissibility for Resource-Efficient LLM Agents*
- Iterative Experience Refinement — *Iterative Experience Refinement of Software-Developing Agents*
- ReasoningBank — *ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory*
- ReCreate — *ReCreate: Reasoning and Creating Domain Agents Driven by Experience*
- SE-Agent — *SE-Agent: Self-Evolution Trajectory Optimization in Multi-Step Reasoning with LLM-Based Agents*
- R⁴ — *R⁴: Retrieval-Augmented Reasoning for Vision-Language Models in 4D Spatio-Temporal Space*

---

## 2. Pathway P2：Narrative → Schematic（intra-Tokenized formalization）

> **本质**：在 Tokenized 层内从弱形式化（自然语言）转为强形式化（语法/拓扑结构）。同层形式化。产物通过 parsing / execution / graph traversal 复用。多数无参数更新。

### 2.1 Graph 结构产物（Knowledge / Memory / Execution Graph）

| Work | Transformation | Tags | Note |
|---|---|---|---|
| A-Mem | `N-Tok (raw) → S-Tok (memory graph)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "create interconnected knowledge networks through dynamic indexing and linking"; "Zettelkasten method"]；memory evolution: new memories trigger updates to existing nodes |
| AriGraph | `N-Tok (raw) → S-Tok (KG world model)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "constructs and updates a memory graph that integrates semantic and episodic memories while exploring the environment"]；Domain: TextWorld |
| Zep | `N-Tok (raw) → S-Tok (temporal KG)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "temporally-aware knowledge graph engine that dynamically synthesizes both unstructured conversational data and structured business data"]；outperforms MemGPT on DMR |
| GAAMA | `N-Tok (raw) → S-Tok (KG)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "constructs a concept-mediated hierarchical knowledge graph"; "four node types (episode, fact, reflection, concept) connected by five structural edge types"]；Personalized PageRank retrieval |
| GSEM | `N-Tok (raw) → S-Tok (KG)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "dual-layer memory graph, capturing both the decision structure within each experience and the relational dependencies across experiences"]；clinical decision support |
| SGMem | `N-Tok (raw) → S-Tok (sentence graph)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "represents dialogue as sentence-level graphs within chunked units, capturing associations across turn-, round-, and session-level contexts"]；3D conversational agents |
| G-Memory | `N-Tok (raw) → S-Tok (hierarchical graph) + N-Tok (insights)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "three-tier graph hierarchy: insight, query, and interaction graphs"; "bi-directional memory traversal"]；multi-agent |
| GPTSwarm | `N-Tok (raw) → S-Tok (graph)` | [txt] {self} ⟨训练⟩ | [Abs: "LLM-based agents as computational graphs"; "automatic graph optimizers refine node-level LLM prompts and improve agent orchestration"]；edge optimization |
| CraniMem | `N-Tok (raw) → S-Tok (KG)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "gated and bounded multi-stage memory design; couples goal conditioned gating and utility tagging with bounded episodic buffer and structured long-term knowledge graph"; "scheduled consolidation loop replays high-utility traces into the graph while pruning low-utility items"] |

**完整题目**
- A-Mem — *A-Mem: Agentic Memory for LLM Agents*
- AriGraph — *AriGraph: Learning Knowledge Graph World Models with Episodic Memory for LLM Agents*
- Zep — *Zep: A Temporal Knowledge Graph Architecture for Agent Memory*
- GAAMA — *GAAMA: Graph Augmented Associative Memory for Agents*
- GSEM — *GSEM: Graph-based Self-Evolving Memory for Experience Augmented Clinical Reasoning*
- SGMem — *SGMem: Sentence Graph Memory for Long-Term Conversational Agents*
- G-Memory — *G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems*
- GPTSwarm — *GPTSwarm: Language Agents as Optimizable Graphs*
- CraniMem — *CraniMem: Cranial Inspired Gated and Bounded Memory for Agentic Systems*

### 2.2 Workflow / SOP / Pipeline 结构产物

| Work | Transformation | Tags | Note |
|---|---|---|---|
| AFlow | `N-Tok (raw) → S-Tok (workflow)` | [txt] {self} ⟨MCTS⟩ | [Abs: "reformulate workflow optimization as a search problem over code-represented workflows"; "iteratively refining workflows through code modification, tree-structured experience, and execution feedback"] |
| A²Flow | `N-Tok (raw) → S-Tok (workflow)` | [txt] {self} ⟨MCTS + LLM-extract⟩ | [Abs: "three-stage operator extraction process"; "self-adaptive abstraction operators"; "operator memory mechanism"]；37% resource reduction vs SOTA |
| Agent Workflow Memory | `N-Tok (raw) → S-Tok (workflow)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "inducing commonly reused routines, i.e., workflows, and selectively providing workflows to guide subsequent generations"]；Mind2Web + WebArena |
| ICE | `N-Tok (raw) → S-Tok (workflow + pipeline)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "dynamically investigates planning and execution trajectories, consolidates them into simplified workflows and pipelines"]；reducing API calls by 80% |
| ScoreFlow | `N-Tok (raw) → π-Par (workflow generator) → S-Tok (workflow)` | [txt] {self} ⟨DPO⟩ | [Abs: "leverages efficient gradient-based optimization in a continuous space"; "Score-DPO, a novel variant accounting for quantitative feedback"]；见 §8 |
| WISE-Flow | `N-Tok (raw) → S-Tok (workflow)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "converts historical service interactions into reusable procedural experience by inducing workflows with prerequisite-augmented action blocks"; "prerequisite-aware feasibility reasoning to achieve state-grounded next actions"]；user-facing service agents |

**完整题目**
- AFlow — *AFlow: Automating Agentic Workflow Generation*
- A²Flow — *A²Flow: Automating Agentic Workflow Generation via Self-Adaptive Abstraction Operators*
- Agent Workflow Memory — *Agent Workflow Memory*
- ICE — *Investigate-Consolidate-Exploit: A General Strategy for Inter-Task Agent Self-Evolution*
- ScoreFlow — *ScoreFlow: Mastering LLM Agent Workflows via Score-based Preference Optimization*
- WISE-Flow — *WISE-Flow: Workflow-Induced Structured Experience for Self-Evolving Conversational Service Agents*

### 2.3 Code / API / Programmatic 结构产物

| Work | Transformation | Tags | Note |
|---|---|---|---|
| Code as Policies | `N-Tok (raw) → S-Tok (program)` | [embodied] {self} ⟨LLM-extract⟩ | [Abs: "code-writing LLMs can be re-purposed to write robot policy code"; "hierarchical code-gen"]；spatial-geometric reasoning |
| Automated Design of Agentic Systems | `N-Tok (raw) → S-Tok (programmatic)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "meta agent iteratively programs interesting new agents based on an ever-growing archive of previous discoveries"]；Turing Complete |
| SkillWeaver | `N-Tok (raw) → S-Tok (API)` | [vis+txt, web] {self} ⟨LLM-extract⟩ | [Abs: "autonomously discovers skills, executes them for practice, and distills practice experiences into robust APIs"]；WebArena 31.8% relative improvement |
| CoEvoSkills | `N-Tok (raw) → S-Tok (typed skill)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "couples a Skill Generator that iteratively refines skills with a Surrogate Verifier that co-evolves"]；multi-file skill packages |
| AutoAgent (composite action) | `N-Tok (raw) → S-Tok (composite action)` | [txt] {self} ⟨LLM-extract⟩ | Self-evolving multi-agent framework；另一产物通道见 §1.2 |
| Meta Context Engineering | `N-Tok (raw) → N-Tok (pattern) → S-Tok (programmatic)` | [txt] {self} ⟨LLM-extract⟩ | [Abs: "bi-level framework that supersedes static CE heuristics by co-evolving CE skills and context artifacts"]；见 §8 |

**完整题目**
- Code as Policies — *Code as Policies: Language Model Programs for Embodied Control*
- Automated Design of Agentic Systems — *Automated Design of Agentic Systems*
- SkillWeaver — *SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills*
- CoEvoSkills — *CoEvoSkills: Self-Evolving Agent Skills via Co-Evolutionary Verification*
- Meta Context Engineering — *Meta Context Engineering via Agentic Skill Evolution*

---

## 3. Pathway P3：Tokenized → Latent（latent compression）

> **本质**：把离散 token 经验压入连续向量空间，以连续向量 / hidden state 形式直接参与模型 attention 或 hidden-state 计算。省去前置编码开销，换取可解释性与可编辑性损失。跨层压缩。

| Work | Transformation | Tags | Note |
|---|---|---|---|
| MemGen | `N-Tok (raw) → Lat (generative latent memory)` | [txt] {self} ⟨SFT + GRPO⟩ [cross-session] | [Abs: "memory trigger monitors reasoning state; memory weaver constructs latent token sequence as machine-native memory"; "spontaneously evolves distinct human-like memory faculties including planning, procedural, and working memory"] |
| LatentMem | `N-Tok (raw) → Lat (composer output)` | [txt] {self} ⟨LMPO (GRPO-style)⟩ [cross-session] | [Abs: "experience bank stores raw interaction trajectories; memory composer synthesizes compact latent memories conditioned on retrieved experience and agent-specific contexts"]；multi-agent |
| LatentEvolve | `N-Tok (raw) → Lat → V-Par (refiner)` | [txt] {self} ⟨训练⟩ [cross-session] | [Abs: "daytime scaling rapidly retrieves historical latent representations; nighttime scaling integrates past latent optimizations akin to human brain's consolidation during sleep"]；见 §8 |
| CLaRa | `N-Tok (raw) → Lat (continuous reasoning)` | [txt] {self} ⟨训练⟩ [cross-session] | [Abs: "embedding-based compression and joint optimization in a shared continuous space"; "differentiable top-k estimator"]；text compression rate of 16 |
| Self-Consolidation (learnable prompt 分支) | `N-Tok (raw) → Lat (learnable prompt)` | [txt] {self} ⟨SFT⟩ [cross-session] | [Abs: "distills non-parametric textual experience into compact learnable parameters"; "internalize extensive historical experience directly into its latent space"]；另有 N-Tok 分支见 §1.7 |

**完整题目**
- MemGen — *MemGen: Weaving Generative Latent Memory for Self-Evolving Agents*
- LatentMem — *LatentMem: Customizing Latent Memory for Multi-Agent Systems*
- LatentEvolve — *LatentEvolve: Self-Evolving Test-Time Scaling in Latent Space*
- CLaRa — *CLaRa: Bridging Retrieval and Generation with Continuous Latent Reasoning*
- Self-Consolidation — *Self-Consolidation for Self-Evolving Agents*

> **观察 1**：当前已归集的所有 P3 工作均为 cross-session 实现形态（需训练）。Session-scoped 实现（如 KV cache compression、prefix reuse）在已归集的材料中为空——标记后续 Literature Scoping 的重点补录区。
>
> **观察 2**：Cross-session Latent 产物背后都有"额外的训练/优化过程"（非 free lunch），与 §1、§2 的纯 LLM-extract 形成鲜明代价对比——可作为 B2 (代价—增益) 与 C1 (trade-off) 的关键对照点。

---

## 4. Pathway P4：Tokenized → Parametric (Evaluator)（evaluator internalization）

> **本质**：把经验固化为"评估能力"（RM、PRM、verifier、critic、judge），即经验固化为评估 $(c,a,o,f)$ 的判断器权重。本 pathway 的目标态仅到 Evaluator；若继续 Evaluator→Policy 则归 §6 或 §8。

### 4.1 Outcome-level Reward Model

| Work | Transformation | Tags | Note |
|---|---|---|---|
| AgentRM | `N-Tok (raw) → V-Par (RM)` | [txt] {self/human} ⟨SFT⟩ | [Abs: "finetuning a reward model to guide the policy model is more robust than directly finetuning the policy model"; "Best-of-N sampling and step-level beam search"] |
| Regularizing Hidden States | `N-Tok (raw) → V-Par (RM)` | [txt] {human} ⟨SFT⟩ | [Abs: "retain the base model's language model head and incorporate text-generation losses to preserve hidden states' text-generation capabilities"]；prevents reward over-optimization |
| Listwise Reward Estimation | `N-Tok (raw) → V-Par (RM)` | [txt] {human} ⟨listwise train⟩ | [Abs: "leverages second-order preference information by constructing a Ranked List of Trajectories"] |
| Graph-Reward-SQL | `N-Tok (raw) → V-Par (graph-match RM)` | [txt, SQL] {self} ⟨SFT⟩ | [Abs: "leverage SQL graph representations to provide accurate reward signals while significantly reducing time cost and GPU memory usage"]；StepRTM stepwise reward |

**完整题目**
- AgentRM — *AgentRM: Enhancing Agent Generalization with Reward Modeling*
- Regularizing Hidden States — *Regularizing Hidden States Enables Learning Generalizable Reward Model for LLMs*
- Listwise Reward Estimation — *Listwise Reward Estimation for Offline Preference-based Reinforcement Learning*
- Graph-Reward-SQL — *Graph-Reward-SQL: Execution-Free Reinforcement Learning for Text-to-SQL via Graph Matching and Stepwise Reward*

### 4.2 Process-level Reward / Verifier Model（PRM）

| Work | Transformation | Tags | Note |
|---|---|---|---|
| Math-Shepherd | `N-Tok (raw) → V-Par (PRM)` | [txt, math] {self} ⟨SFT⟩ | [Abs: "assigns a reward score to each step of math problem solutions"; "automatically constructed process-wise supervision data"] |
| Entropy-Regularized PRM | `N-Tok (raw) → V-Par (PRM)` | [txt, math] {self} ⟨SFT⟩ | [Abs: "integrates KL-regularized MDP to balance policy optimization"; "derive the optimal reward model from the initial policy sampling"] |
| Free Process Rewards（★关注） | `N-Tok (raw) → V-Par (PRM)` | [txt, math] {self} ⟨无 step label⟩ | [Abs: "implicit PRM can be obtained at no additional cost, by simply training an ORM on the cheaper response-level labels"]；1/38 training data vs Math-Shepherd |
| FreePRM | `N-Tok (raw) → V-Par (PRM)` | [txt, math] {self} ⟨无 step label⟩ | [Abs: "generates pseudo step-level labels based on the correctness of final outcome"; "Buffer Probability to eliminate impact of noise"]；53.0% F1 on ProcessBench |
| Scan | `N-Tok (raw) → V-Par (PRM)` | [txt, math] {self} ⟨MC annotation + denoise⟩ | [Abs: "Self-Denoising Monte Carlo Annotation"; "lightweight models (1.5B) can produce high-quality annotations through self-denoising"]；39.2 F1 improvement |
| SPARE | `N-Tok (raw) → V-Par (PRM + ORPO)` | [txt, math] {self} ⟨single-pass⟩ | [Abs: "Single-Pass Annotation with Reference-Guided Evaluation"; "jointly aligning solution steps to reference solutions"; "2.3x speedup vs MCTS"] |
| SPARK | `N-Tok (raw) → V-Par (PRM)` | [txt] {self} ⟨stepwise⟩ | [Abs: "generator produces diverse solutions, verifier evaluates them using parallel and sequential scaling"; "reference-free RL training that exceeds ground-truth methods"] |
| From Outcomes to Processes | `N-Tok (raw) → V-Par (PRM)` | [txt] {self} ⟨ORM→PRM⟩ | [Abs: "dual-consistency framework integrating score consistency-based and preference consistency-based partial evaluation"] |
| ReST-MCTS (PRM 分支) | `N-Tok (raw) → V-Par (PRM)` | [txt, math] {self} ⟨MCTS + train⟩ | [Abs: "infer the correct process rewards by estimating the probability this step can help lead to the correct answer"]；另含 π-Par 分支，见 §5 / §8 |
| Dyve | `N-Tok (raw) → V-Par (dynamic verifier)` | [txt] {self} ⟨SFT⟩ | [Abs: "integrating fast and slow thinking, inspired by Kahneman's Systems Theory"; "step-wise consensus-filtered process supervision"] |
| SRR-Judge | `N-Tok (raw) → V-Par (step-level judge)` | [txt, search] {self} ⟨SFT⟩ | [Abs: "reliable step-level assessment of reasoning and search actions"; "iterative rejection sampling fine-tuning"] |
| PRL | `N-Tok (raw) → V-Par (process reward)` + `→ π-Par` | [txt] {self} ⟨hybrid⟩ | [Abs: "decomposes the entropy regularized RL objective into intermediate steps, with rigorous process rewards"]；见 §8 |
| GM-PRM | `N-Tok (raw) → V-Par (multimodal PRM)` | [vis+txt, math] {self} ⟨SFT⟩ | [Abs: "transforms PRM from passive judge into active reasoning collaborator"; "generates corrected version of the first erroneous step it identifies"; "Refined Best-of-N"]；geometry-grounded |

**完整题目**
- Math-Shepherd — *Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations*
- Entropy-Regularized PRM — *Entropy-Regularized Process Reward Model*
- Free Process Rewards — *Free Process Rewards without Process Labels*
- FreePRM — *FreePRM: Training Process Reward Models Without Ground Truth Process Labels*
- Scan — *Scan: Self-Denoising Monte Carlo Annotation for Robust Process Reward Learning*
- SPARE — *SPARE: Single-Pass Annotation with Reference-Guided Evaluation for Automatic Process Supervision and Reward Modelling*
- SPARK — *SPARK: Stepwise Process-Aware Rewards for Reference-Free Reinforcement Learning*
- From Outcomes to Processes — *From Outcomes to Processes: Guiding PRM Learning from ORM for Inference-Time Alignment*
- ReST-MCTS — *ReST-MCTS: LLM Self-Training via Process Reward Guided Tree Search*
- Dyve — *Dyve: Thinking Fast and Slow for Dynamic Process Verification*
- SRR-Judge — *SRR-Judge: Step-Level Rating and Refinement for Enhancing Search-Integrated Reasoning in Search Agents*
- PRL — *PRL: Process Reward Learning Improves LLMs' Reasoning Ability and Broadens the Reasoning Boundary*
- GM-PRM — *GM-PRM: A Generative Multimodal Process Reward Model for Multimodal Mathematical Reasoning*

### 4.3 Critic / Judge 模型

| Work | Transformation | Tags | Note |
|---|---|---|---|
| SWEET-RL | `N-Tok (raw) → V-Par (critic) → π-Par` | [txt, collaborative] {self} ⟨DPO⟩ | [Abs: "trains a critic model with access to additional training-time information"; "step-level rewards for improving the policy model"]；见 §6 / §8 |
| Self-Improving VLM Judges | `π-Par → N-Tok (raw) → V-Par (judge)` | [vis+txt] {self} ⟨SFT⟩ | [Abs: "self-train a VLM judge model without any human preference annotations, using only self-synthesized data"]；见 §8 |
| From Novice to Expert (Discriminator 分支) | `N-Tok (raw) → V-Par (discriminator) → π-Par` | [txt] {self} ⟨DPO + PPO⟩ | [Abs: "compare the actions of expert and agent to automatically generate intermediate rewards"; "implicit-reward and inverse RL techniques"]；见 §6 / §8 |
| PROPA (reward 分支) | `N-Tok (raw, vis+txt) → V-Par (RM)` | [vis+txt] {self} ⟨train⟩ | [Abs: "integrates MCTS with GRPO to generate dense, process-level rewards"; "interleaves GRPO updates with SFT to overcome cold-start"]；另含 π-Par 分支，见 §5 |

**完整题目**
- SWEET-RL — *SWEET-RL: Training Multi-Turn LLM Agents on Collaborative Reasoning Tasks*
- Self-Improving VLM Judges — *Self-Improving VLM Judges Without Human Annotations*
- From Novice to Expert — *From Novice to Expert: LLM Agent Policy Optimization via Step-wise Reinforcement Learning*
- PROPA — *PROPA: Toward Process-level Optimization in Visual Reasoning via Reinforcement Learning*

> Becoming Experienced Judges 已移至 §9（边界案例）——test-time meta-prompt 自修正，无持久 carrier transformation。

---

## 5. Pathway P5：Tokenized → Parametric (Policy)（policy internalization）

> **本质**：把经验固化为决策能力（trajectories → policy weights via SFT / RL）；产物为 LLM / VLA / GUI agent 的 policy 权重。是文献中数量最多的 pathway，内部按监督类型与模态进一步分组。

### 5.1 纯 SFT 内化（有监督模仿，不涉及 reward）

| Work | Transformation | Tags | Note |
|---|---|---|---|
| ATLaS | `N-Tok (raw, critical steps) → π-Par` | [txt] {self} ⟨SFT on critical⟩ | [Abs: "identifies the critical steps in expert trajectories and finetunes LLMs solely on these steps"; "only 30% critical steps outperforms finetuning on all steps"] |
| E²CL | `N-Tok (raw + errors) → π-Par` | [embodied] {self} ⟨SFT⟩ | [Abs: "leverages exploration-induced errors and environmental feedback to enhance environment alignment"; "teacher-guided and teacher-free explorations"] |
| Learning From Failure | `N-Tok (raw, pos+neg) → π-Par` | [txt] {self} ⟨SFT⟩ | [Abs: "unsuccessful trajectories offer valuable insights"; "adding a prefix or suffix that tells the model whether to generate a successful trajectory"]；正负轨迹联合 SFT |
| InfiGUIAgent | `N-Tok (raw) → π-Par` | [vis+txt, GUI] {self/human} ⟨SFT⟩ | [Abs: "two-stage supervised fine-tuning pipeline"; "Stage 1 enhances GUI understanding and grounding; Stage 2 integrates hierarchical reasoning and expectation-reflection reasoning"] |
| Act Wisely | `N-Tok (raw) → π-Par` | [vis+txt] {self} ⟨SFT cold + RL⟩ | [Abs: "HDPO reframes tool efficiency from a competing scalar objective to a strictly conditional one"; "two orthogonal optimization channels: accuracy and efficiency"]；见 §8 |
| Reflective Planning | `N-Tok (raw) → π-Par` | [vis+txt, embodied] {self} ⟨train⟩ | [Abs: "iteratively improves a pretrained VLM with a reflection mechanism"; "uses a generative model to imagine future world states"]；multi-stage robotic manipulation |

**完整题目**
- ATLaS — *ATLaS: Agent Tuning via Learning Critical Steps*
- E²CL — *E²CL: Exploration-based Error Correction Learning for Embodied Agents*
- Learning From Failure — *Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents*
- InfiGUIAgent — *InfiGUIAgent: A Multimodal Generalist GUI Agent with Native Reasoning and Reflection*
- Act Wisely — *Act Wisely: Cultivating Meta-Cognitive Tool Use in Agentic Multimodal Models*
- Reflective Planning — *Reflective Planning: Vision-Language Models for Multi-Stage Long-Horizon Robotic Manipulation*

### 5.2 RL 内化（GRPO / PPO / 其他 policy-gradient）

| Work | Transformation | Tags | Note |
|---|---|---|---|
| Agentic Reasoning & Tool Integration | `N-Tok (raw) → π-Par` | [txt] {self} ⟨GRPO⟩ | [Abs: "ARTIST: enables models to autonomously decide when, how, and which tools to invoke within multi-turn reasoning chains"; "outcome-based RL"] |
| Agentic Memory (learning memory mgmt) | `N-Tok (raw) → π-Par` | [txt] {self} ⟨step-wise GRPO⟩ | [Abs: "exposes memory operations as tool-based actions"; "three-stage progressive RL strategy"; "step-wise GRPO to address sparse and discontinuous rewards"] |
| DeepAnalyze | `N-Tok (raw) → π-Par` | [txt, data-sci] {self} ⟨SFT + GRPO⟩ | [Abs: "curriculum-based agentic training paradigm that emulates the learning trajectory of human data scientists"]；end-to-end data science |
| AgentEvolver | `π-Par → N-Tok (raw) → π-Par` | [txt] {self} ⟨GRPO⟩ | [Abs: "self-questioning enables curiosity-driven task generation; self-navigating improves exploration efficiency; self-attributing enhances sample efficiency"]；见 §8 |
| SPA-RL | `N-Tok (raw) → π-Par` | [txt] {self} ⟨SFT + PPO⟩ | [Abs: "decomposes the final reward into stepwise contributions, each reflecting its incremental progress toward overall task completion"] |
| ReTool | `N-Tok (raw) → π-Par` | [txt, tool] {self} ⟨SFT + PPO⟩ | [Abs: "dynamic interleaving of real-time code execution within natural language reasoning"; "emergent behaviors such as code self-correction"]；AIME 72.5% |
| ToolRL | `N-Tok (raw) → π-Par`（rule-based Evaluator） | [txt] {self} ⟨GRPO⟩ | [Abs: "first comprehensive study on reward design for tool selection and application tasks within the RL paradigm"]；不训练独立 Evaluator |
| ToolSample | `N-Tok (raw) → π-Par` | [txt] {self} ⟨RL + curriculum⟩ | [Abs: "Reward-Based Dynamic Sampling and Task-Based Dynamic Curriculum Learning"; "multi-dimensional reward statistics"] |
| MobileGUI-RL | `π-Par → N-Tok (raw) → π-Par` | [vis+txt, GUI] {self} ⟨GRPO⟩ | [Abs: "synthesizes a curriculum of learnable tasks through self-exploration and filtering"; "adapts GRPO to GUI navigation with trajectory-aware advantages"]；见 §8 |
| OmegaUse | `N-Tok (raw) → π-Par` | [vis+txt, GUI] {self/human} ⟨GRPO⟩ | [Abs: "MoE backbone"; "two-stage: SFT to establish fundamental interaction syntax, followed by GRPO to improve spatial grounding and sequential planning"]；mobile+desktop |
| MAI-UI | `N-Tok (raw) → π-Par` | [vis+txt, GUI] {self/human} ⟨SFT + RL⟩ | [Abs: "self-evolving data pipeline"; "native device-cloud collaboration system"; "online RL with advanced optimizations scaling to 512 parallel environments"] |
| EVOLVE-VLA | `N-Tok (raw) → π-Par (VLA)` | [vis+txt, embodied] {self} ⟨GRPO⟩ | [Abs: "test-time training framework enabling VLAs to continuously adapt through environment interaction"; "learned progress estimator providing dense feedback"]；+22% in 1-shot |
| LongNav-R1 | `N-Tok (raw) → π-Par` | [vis+txt, embodied] {self} ⟨multi-turn RL⟩ | [Abs: "reformulates navigation as continuous multi-turn conversation between VLA policy and embodied environment"; "Horizon-Adaptive Policy Optimization"] |
| PROPA (policy 分支) | `N-Tok (raw) → π-Par` | [vis+txt] {self} ⟨RL⟩ | [Abs: "process-level visual RL"; "up to 17.0% gains on in-domain tasks and 21.0% on out-of-domain"]；另含 V-Par，见 §4.3 |
| PRL (policy 分支) | `N-Tok (raw) → π-Par` | [txt] {self} ⟨RL with PRL⟩ | [Abs: "turns outcome reward into process supervision signals"; "improves both average@n and pass@n"] |

**完整题目**
- Agentic Reasoning & Tool Integration — *Agentic Reasoning and Tool Integration for LLMs via Reinforcement Learning*
- Agentic Memory — *Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents*
- DeepAnalyze — *DeepAnalyze: Agentic Large Language Models for Autonomous Data Science*
- AgentEvolver — *AgentEvolver: Towards Efficient Self-Evolving Agent System*
- SPA-RL — *SPA-RL: Reinforcing LLM Agents via Stepwise Progress Attribution*
- ReTool — *ReTool: Reinforcement Learning for Strategic Tool Use in LLMs*
- ToolRL — *ToolRL: Reward is All Tool Learning Needs*
- ToolSample — *ToolSample: Dual Dynamic Sampling Methods with Curriculum Learning for RL-based Tool Learning*
- MobileGUI-RL — *MobileGUI-RL: Advancing Mobile GUI Agent through Reinforcement Learning in Online Environment*
- OmegaUse — *OmegaUse: Building a General-Purpose GUI Agent for Autonomous Task Execution*
- MAI-UI — *MAI-UI Technical Report: Real-World Centric Foundation GUI Agents*
- EVOLVE-VLA — *EVOLVE-VLA: Test-Time Training from Environment Feedback for Vision-Language-Action Models*
- LongNav-R1 — *LongNav-R1: Horizon-Adaptive Multi-Turn RL for Long-Horizon VLA Navigation*
- （Reflective Planning / PROPA / PRL 的完整题目在前述章节中已列出）

### 5.3 自训练循环：π-Par → N-Tok → π-Par（ReST / Rejection / Filtering）

> 该模式在文献中非常普遍。此处**先按 P5 归集**（主轴是 Tokenized→Policy），在 §8.1 作为 **Self-Reinforce 复合模式**集中讨论。

| Work | Transformation | Tags | Note |
|---|---|---|---|
| FireAct | `π-Par → N-Tok (raw) → π-Par` | [txt] {self} ⟨SFT⟩ | [Abs: "fine-tuning LMs with trajectories from multiple tasks and prompting methods"; "more diverse fine-tuning data can further improve agents"]；奠基性 agent fine-tuning |
| Agent Learning via Early Experience | `π-Par → N-Tok (raw) → π-Par` | [txt] {self} ⟨SFT⟩ | [Abs: "interaction data generated by the agent's own actions, where the resulting future states serve as supervision without reward signals"; "Implicit world modeling + Self-reflection"] |
| Agent-R | `π-Par → N-Tok (raw+correction) → π-Par` | [txt] {self} ⟨SFT iter⟩ | [Abs: "leverages MCTS to construct training data that recover correct trajectories from erroneous ones"; "model-guided critique construction mechanism identifies the first error step"] |
| Agent0 | `π-Par → N-Tok (raw) → π-Par` | [txt] {self} ⟨curriculum RL⟩ | [Abs: "symbiotic competition between curriculum agent and executor agent"; "self-reinforcing cycle that continuously produces high-quality curricula"] |
| Beyond Human Data (ReST^EM) | `π-Par → N-Tok (raw) → π-Par` | [txt, math/code] {self} ⟨SFT + 二值 verifier⟩ | [Abs: "generate samples from the model and filter them using binary feedback, fine-tune, repeat"; "scales favorably with model size"] |
| Beyond Policy Optimization | `π-Par → N-Tok (raw) → π-Par` | [txt] {self} ⟨SFT + curriculum⟩ | [Abs: "three-stage framework establishing a self-improving data flywheel"; "planning quaternions with long-short chain-of-thought fusion"] |
| Entropy-Based Adaptive Weighting | `π-Par → N-Tok (raw) → π-Par` | [txt] {self} ⟨SFT w/ entropy⟩ | [Abs: "adaptive weighting strategy designed to prioritize uncertain data during self-training"; "assigning higher weights to data where model exhibits greater uncertainty"] |
| Distilling LLM Agent into Small Models | `π-Par → N-Tok (raw) → π-Par` | [txt] {teacher→student} ⟨SFT⟩ | [Abs: "transferring not only reasoning capability but full task-solving behavior from LLM-based agents into sLMs with retrieval and code tools"] |
| Internalizing Agency (LEAFE) | `π-Par → N-Tok (raw + reflection) → π-Par` | [txt] {self} ⟨SFT⟩ | [Abs: "summarizes environment feedback into actionable experience, backtracks to earlier decision points, and explores alternative branches"; "distills experience-guided corrections into model"]；见 §8.1/§8.3 |
| Improving Retrospective Language Agents (RetroAct) | `π-Par → N-Tok (raw + reflection) → π-Par` | [txt] {self} ⟨SFT + RL⟩ | [Abs: "jointly optimizes both task-planning and self-reflective evolution capabilities"; "off-policy joint policy gradient optimization with imitation learning regularization"]；见 §8.1/§8.3 |
| Self-Instruct | `π-Par → N-Tok (raw) → π-Par` | [txt] {self} ⟨SFT⟩ | [Abs: "generates instructions, input, and output samples from a language model, then filters invalid or similar ones before fine-tuning"] |
| START | `π-Par → N-Tok (raw) → π-Par` | [txt, tool] {self} ⟨train⟩ | [Abs: "Hint-infer stimulates tool use without demonstration data"; "Hint Rejection Sampling Fine-Tuning"]；self-taught reasoner with tools |
| The Path of Self-Evolving LLMs | `π-Par → N-Tok (raw) → π-Par` | [txt] {self} ⟨SFT⟩ | [Abs: "self-aware difficulty prediction and self-aware limit breaking"; "53.8% relative improvement with less than 1.2% extra data"] |
| EvoCUA（★关注） | `π-Par → N-Tok (raw) → π-Par` | [vis+txt, CUA] {self} ⟨train⟩ | [Abs: "verifiable synthesis engine autonomously generates diverse tasks"; "iterative evolving learning strategy dynamically regulates policy updates by identifying capability boundaries"]；OSWorld 56.7% |
| On-Policy Context Distillation | `π-Par → N-Tok → π-Par` | [txt] {self} ⟨distill⟩ | [Abs: "trains a student model on its own generated trajectories while minimizing reverse KL divergence against a context-conditioned teacher"] |
| Online Experiential Learning | `π-Par → N-Tok (raw) → N-Tok → π-Par` | [txt] {self} ⟨hybrid⟩ | [Abs: "extracts transferable experiential knowledge from interaction trajectories; consolidates into model parameters via on-policy context distillation"]；含中间 refined Narrative step；见 §8 |
| Self-Questioning LMs | `π-Par → N-Tok (raw) → π-Par` | [txt] {self} ⟨RL⟩ | [Abs: "asymmetric self-play framework where a proposer generates questions and a solver answers"; "continually generating more interesting problems"]；见 §8 |
| Self-Training for Visual Program Synthesis | `π-Par → N-Tok (raw) → π-Par` | [vis+txt] {self} ⟨RL⟩ | [Abs: "exploit existing annotations for a vision-language task to improvise a coarse reward signal"; "reinforced self-training"]；见 §8 |

**完整题目**
- FireAct — *FireAct: Toward Language Agent Fine-tuning*
- Agent Learning via Early Experience — *Agent Learning via Early Experience*
- Agent-R — *Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training*
- Agent0 — *Agent0: Unleashing Self-Evolving Agents from Zero Data via Tool-Integrated Reasoning*
- Beyond Human Data — *Beyond Human Data: Scaling Self-Training for Problem-Solving with Language Models*
- Beyond Policy Optimization — *Beyond Policy Optimization: A Data Curation Flywheel for Sparse-Reward Long-Horizon Planning*
- Entropy-Based Adaptive Weighting — *Entropy-Based Adaptive Weighting for Self-Training*
- Distilling LLM Agent — *Distilling LLM Agent into Small Models with Retrieval and Code Tools*
- Internalizing Agency — *Internalizing Agency from Reflective Experience*
- Improving Retrospective Language Agents — *Improving Retrospective Language Agents via Joint Policy Gradient Optimization*
- Self-Instruct — *Self-Instruct: Aligning Language Models with Self-Generated Instructions*
- START — *START: Self-taught Reasoner with Tools*
- The Path of Self-Evolving LLMs — *The Path of Self-Evolving Large Language Models: Achieving Data-Efficient Learning via Intrinsic Feedback*
- EvoCUA — *EvoCUA: Evolving Computer Use Agents via Learning from Scalable Synthetic Experience*
- On-Policy Context Distillation — *On-Policy Context Distillation for Language Models*
- Online Experiential Learning — *Online Experiential Learning for Language Models*

### 5.4 Evaluator-mediated / Refined-Narrative-mediated Policy 内化（经过中间态）

> 这些工作主干仍是 Policy 内化，但显式经过 Evaluator 或 refined Narrative 中间态，属于 §8 最重要的复合模式之一。此处保留一份引用表便于对照。

| Work | Transformation | Tags | Note |
|---|---|---|---|
| From Novice to Expert | `N-Tok (raw) → V-Par (disc) → π-Par` | [txt] {self} ⟨DPO + PPO⟩ | [Abs: "StepAgent utilizes step-wise reward to optimize RL process"; "action distribution of agent can converge toward expert action distribution"]；见 §8.2 |
| ReST-MCTS (policy 分支) | `N-Tok (raw) → V-Par (PRM) → π-Par` | [txt, math] {self} ⟨MCTS + SFT⟩ | [Abs: "tree-search policy achieves higher accuracy compared with prior baselines"; "continuously enhance three language models for multiple iterations"]；见 §8.2 |
| SWEET-RL | `N-Tok (raw) → V-Par (critic) → π-Par` | [txt] {self} ⟨DPO⟩ | [Abs: "critic provides step-level rewards for improving the policy model"; "6% absolute improvement in success and win rates"]；见 §8.2 |
| EvolveR | `N-Tok (raw) → N-Tok (principle) → π-Par` | [txt] {self} ⟨SFT + GRPO⟩ | [Abs: "Offline Self-Distillation synthesizes trajectories into structured repository of abstract, reusable strategic principles"; "policy reinforcement mechanism iteratively updates agent"]；见 §8.3 |
| SaMuLe | `N-Tok (raw) → N-Tok (reflection) → π-Par` | [txt] {self} ⟨LLM-extract + SFT⟩ | [Abs: "Multi-Level Reflection Synthesis across three levels: Single-Trajectory, Intra-Task, and Inter-Task"; "fine-tunes a retrospective language model"]；见 §8.3 |
| Learning from Trials and Errors | `N-Tok (raw) → N-Tok (reflection) → π-Par` | [vis+txt, embodied] {self} ⟨SFT⟩ | [Abs: "reflection-in-action uses test-time scaling; reflection-on-action uses test-time training"; "retrospective reflection for long-horizon credit assignment"]；见 §8.3 |
| SkillRL | `N-Tok (raw) → N-Tok (skill) → π-Par` | [txt] {self} ⟨SFT + GRPO⟩ | [Abs: "experience-based distillation mechanism to build hierarchical skill library SkillBank"; "skill library co-evolves with agent's policy during RL"]；见 §8.3 |
| Skill-SD | `N-Tok (raw) → N-Tok (skill) → π-Par` | [txt] {self} ⟨GRPO⟩ | [Abs: "turns agent's own trajectories into dynamic training-only supervision"; "completed trajectories summarized into compact natural language skills"]；见 §8.3 |
| Agentic Proposing | `N-Tok (raw) → N-Tok (skill) → π-Par (proposer) → N-Tok (synth) → π-Par (down)` | [txt] {self→teacher→student} ⟨RL⟩ | [Abs: "models problem synthesis as goal-driven sequential decision process"; "Multi-Granularity Policy Optimization (MGPO)"]；见 §8.3 |
| SKILL0 | `N-Tok (skill) → π-Par` | [txt] ⟨PPO⟩ | [Abs: "training-time curriculum begins with full skill context and progressively withdraws it"; "Dynamic Curriculum evaluates each skill file's on-policy helpfulness"] |
| RL for Self-Improving Agent with Skill Library | `N-Tok (raw) → π-Par → N-Tok (skill)` | [txt] {self} ⟨RL⟩ | **逆向拓扑**：先 π-Par 内化再外化 skill library；见 §8.6 |
| SAGE | `N-Tok (raw) → π-Par → N-Tok (refined: skills)` | [txt] {self} ⟨RL (GRPO) + sequential rollout⟩ | [Abs: "Skill Augmented GRPO for self-Evolution"; "Sequential Rollout iteratively deploys agents across a chain of similar tasks"]；见 §8.6 |

**完整题目**
- EvolveR — *EvolveR: Self-Evolving LLM Agents through an Experience-Driven Lifecycle*
- SaMuLe — *SaMuLe: Self-Learning Agents Enhanced by Multi-level Reflection*
- Learning from Trials and Errors — *Learning from Trials and Errors: Reflective Test-Time Planning for Embodied LLMs*
- SkillRL — *SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning*
- Skill-SD — *Skill-SD: Skill-Conditioned Self-Distillation for Multi-turn LLM Agents*
- Agentic Proposing — *Agentic Proposing: Enhancing Large Language Model Reasoning via Compositional Skill Synthesis*
- SKILL0 — *SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization*
- RL for Self-Improving Agent with Skill Library — *Reinforcement Learning for Self-Improving Agent with Skill Library*
- SAGE — *Reinforcement Learning for Self-Improving Agent with Skill Library* (Skill Augmented GRPO with sequential rollout)

> （From Novice to Expert / ReST-MCTS / SWEET-RL 的完整题目见 §4.2 / §4.3。）


---

## 6. Pathway P6：Parametric (Evaluator) → Parametric (Policy)（preference alignment）

> **本质**：用训练好的 Evaluator 提供的 reward 信号去更新 Policy 权重，即 RLHF / DPO 主干。
>
> **P6 的特殊性**：P6 兼具 transformation 与 utilization 的双重性质——Evaluator 的 utilization（推理时输出评估信号）同时充当了 transformation 的驱动机制。
>
> 文献中**几乎总是作为复合链条的一段出现**，很少作为独立工作。本文档中该步骤嵌入在 §5.4 与 §8.2 的 composition 中；单独成立的工作当前池内无。

| Work | Transformation | Tags | Note |
|---|---|---|---|
| — | `V-Par → π-Par` | — | 嵌入在 §5.4 与 §8.2 中 |

> **观察**：这一现象本身有分析价值——文献习惯把 V-Par 训练与 V-Par→π-Par 的对齐作为"同一篇工作两步"来报告，而非单独发布"冻结某个 RM 然后做 RLHF"。综合分析 Section 可讨论该现象。


---

## 7. Pathway P7：Parametric → Tokenized（knowledge externalization）

> **本质**：权重 → synthetic trajectories / demonstrations。隐式经验外化为显式载体。**注意区分**：此处指的是"外化后不再直接用回自己训练"的纯外化；若外化后又吞回自己（`π → N → π`），归 §5.3 的 self-reinforce 模式。外化方向可以是 `π-Par → N-Tok`（生成 raw trajectories）或 `π-Par → S-Tok`（生成 workflow 结构）。

| Work | Transformation | Tags | Note |
|---|---|---|---|
| BugPilot | `π-Par → N-Tok (raw, synthetic bugs)` | [txt, code] {teacher} ⟨synthesis⟩ | [Abs: "instructs SWE Agents to introduce a feature into the codebase whereby they may unintentionally break tests, resulting in bugs"]；realistic development process |
| GUI-ReWalk | `π-Par → N-Tok (raw)` | [vis+txt, GUI] {teacher} ⟨stochastic exploration⟩ | [Abs: "stochastic exploration phase emulates human trial-and-error; reasoning-guided phase drives coherent interactions"; "multi-stride task generation for long-horizon workflows"] |
| OS-Genesis | `π-Par → N-Tok (raw)` | [vis+txt, GUI] {teacher} ⟨reverse task synthesis⟩ | [Abs: "reverses the conventional trajectory collection process"; "agents first perceive environments and perform step-wise interactions, then retrospectively derive tasks"] |
| Agentic Rubrics | `π-Par → N-Tok (rubric checklist)` | [txt, SWE] {self} ⟨agentic context gathering⟩ | [Abs: "expert agent interacts with repository to create context-grounded rubric checklist"; "candidate patches scored against it without requiring test execution"] |
| EvoAgentX | `π-Par → S-Tok (evolved workflow)` | [txt] {self} ⟨evolutionary optimization⟩ | [Abs: "automates generation, execution, and evolutionary optimization of multi-agent workflows"; "integrates three MAS optimization algorithms"] |

**完整题目**
- BugPilot — *BugPilot: Complex Bug Generation for Efficient Learning of SWE Skills*
- GUI-ReWalk — *GUI-ReWalk: Massive Data Generation for GUI Agent via Stochastic Exploration and Intent-Aware Reasoning*
- OS-Genesis — *OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis*
- Agentic Rubrics — *Agentic Rubrics as Contextual Verifiers for SWE Agents*
- EvoAgentX — *EvoAgentX: An Automated Framework for Evolving Agentic Workflows*

> **V2 新增观察**：abstract 信息表明，P7 中 GUI 数据合成方向（GUI-ReWalk, OS-Genesis）正在快速成长，形成 "Synthetic Data Flywheel" 子方向。P7 不再是孤立的"外化即终点"，而是越来越多地作为更大的 self-improvement loop 中的 "数据供给" 阶段——这与 §8.7 的 Externalize-for-Training 模式形成呼应。


---

## 8. Composition Patterns（多步路径组合）

> **对应 Survey 架构**：Layer B\*（复合管线解构层）与 Layer C2（Compositional Grammar）的核心材料。
>
> **V2 增强**：从 abstract 中提取各 pattern 的 integration mechanism 描述线索，以 `[Abs integration clue: ...]` 标注。

### 8.1 Self-Reinforce 模式：`π-Par → N-Tok → π-Par`

- **定义**：由当前 policy 生成轨迹，经筛选 / 标注 / 反思后再训练更新 policy。
- **成员（高频）**：
  FireAct · Agent Learning via Early Experience · Agent-R · Agent0 · Beyond Human Data · Beyond Policy Optimization · Entropy-Based Adaptive Weighting · Distilling LLM Agent · Internalizing Agency · Improving Retrospective LMs · Self-Instruct · Self-Questioning LMs · START · The Path of Self-Evolving LLMs · EvoCUA · MobileGUI-RL · Self-Training for Visual Program Synthesis · On-Policy Context Distillation · AgentEvolver
- **必然性**：`P5` 单步在"从哪里来训练数据"上缺一环——数据必须先存在才能 fine-tune。Self-Reinforce 把"数据来源"与"策略更新"纳入同一闭环。
- **Integration mechanism clues（V2 新增）**：
  - Agent-R: [Abs: "MCTS to construct training data that recover correct trajectories from erroneous ones; model-guided critique construction identifies first error step"]
  - EvoCUA: [Abs: "iterative evolving learning strategy dynamically regulates policy updates by identifying capability boundaries -- reinforcing successful routines while transforming failure trajectories into rich supervision"]
  - Agent0: [Abs: "symbiotic competition between curriculum agent and executor agent; self-reinforcing cycle"]
  - Internalizing Agency: [Abs: "summarizes environment feedback into actionable experience, backtracks to earlier decision points, explores alternative branches with revised actions"]
- **子变体**：
  - 加 reflection 中间层（Internalizing Agency、Improving Retrospective、Agent-R 严格意义上）
  - 加 curriculum 难度调度（Agent0、Beyond Policy Optimization）
  - 跨模型蒸馏变体（Distilling LLM Agent 为 teacher→student）

### 8.2 Evaluate-then-Optimize 模式：`N-Tok → V-Par → π-Par`

- **定义**：先把 Tokenized 经验固化为 Evaluator，再用 Evaluator 提供的信号更新 Policy。
- **成员**：
  From Novice to Expert · ReST-MCTS · SWEET-RL · PRL (hybrid)
- **必然性**：解决"用 raw 作监督噪声大、逐步奖励难标"的问题，Evaluator 作为"可训练的噪声过滤器"。
- **Integration mechanism clues（V2 新增）**：
  - ReST-MCTS: [Abs: "infer correct process rewards by estimating probability this step can help lead to correct answer; inferred rewards serve dual purposes as value targets for refining PRM and selecting high-quality traces"]
  - SWEET-RL: [Abs: "trains a critic model with access to additional training-time information; critic provides step-level rewards"]
  - From Novice to Expert: [Abs: "compare actions of expert and agent to automatically generate intermediate rewards; implicit-reward and inverse RL techniques"]
- **与 P6 的关系**：`V-Par → π-Par` 步骤是 P6，但文献中几乎只以该复合形式出现，几乎无"冻结 RM 做 alignment"的独立工作——见 §6 的 observation。

### 8.3 Refine-then-Internalize 模式：`N-Tok (raw) → N-Tok (refined) → π-Par`

- **定义**：先在 Tokenized 层内做语义抽象（reflection / principle / skill / strategy），再将 refined Narrative 作为监督内化为权重。
- **成员**：
  EvolveR (principle) · SaMuLe (reflection) · Learning from Trials and Errors (reflection) · Online Experiential Learning (refined Narrative) · SkillRL (skill) · Skill-SD (skill) · Agentic Proposing (skill) · Internalizing Agency / LEAFE (reflection via backtracking) · Improving Retrospective LMs / RetroAct (reflection + joint policy gradient) · MetaClaw (skill + policy optimization)
- **必然性**：raw 噪声过大时，先 refine 降噪再内化；但该模式假设 refine 步骤本身的噪声低于 raw——否则劣化 SFT。
- **Integration mechanism clues（V2 新增）**：
  - EvolveR: [Abs: "Offline Self-Distillation synthesizes trajectories into structured repository of abstract, reusable strategic principles; policy reinforcement mechanism iteratively updates agent based on performance"]
  - SaMuLe: [Abs: "Multi-Level Reflection Synthesis: Single-Trajectory (micro), Intra-Task (meso), Inter-Task (macro); fine-tunes retrospective language model to generate reflections"]
  - SkillRL: [Abs: "experience-based distillation builds hierarchical skill library; adaptive retrieval for general and task-specific heuristics; recursive evolution"]
  - Skill-SD: [Abs: "turns agent's own trajectories into dynamic training-only supervision; importance-weighted reverse-KL loss for gradient-correct token-level distillation"]
  - MetaClaw: [Abs: "Skill-driven fast adaptation analyzes failure trajectories via LLM evolver to synthesize new skills; Opportunistic policy optimization via cloud LoRA and RL-PRM triggered during user-inactive windows"]；同时属于 §8.1（π→N→π 闭环）
- **观察**：Skill 系列（SkillRL / Skill-SD / Agentic Proposing）构成一个**子模式 cluster**——中间态为 skill，可进一步细分。LEAFE 和 RetroAct 的中间 reflection 步骤与 Self-Reinforce 模式（§8.1）重叠——它们同时属于 §8.1（π→N→π 闭环）和 §8.3（中间有 refined Narrative），体现了两种 pattern 的交叉地带。MetaClaw 同样横跨两种 pattern：其 Skill-driven fast adaptation 属于 §8.3，Opportunistic policy optimization 属于 §8.1。

### 8.4 Compress-then-Use 模式：`N-Tok → Lat (+ 其他)`

- **定义**：压入 Latent 后可直接用或继续训练。
- **成员**：
  MemGen · LatentMem · LatentEvolve (+ `→ V-Par` refiner) · CLaRa · Self-Consolidation (learnable prompt 分支)
- **Integration mechanism clues（V2 新增）**：
  - MemGen: [Abs: "memory trigger monitors reasoning state; memory weaver takes current state as stimulus to construct latent token sequence"]
  - LatentMem: [Abs: "LMPO propagates task-level optimization signals through latent memories to composer, encouraging compact and high-utility representations"]
  - LatentEvolve: [Abs: "daytime scaling rapidly retrieves historical latent representations; nighttime scaling integrates past latent optimizations akin to sleep consolidation"]
- **观察**：LatentEvolve 含 `N-Tok → Lat → V-Par` 三段链路，但 Evaluator 不是 policy 的 evaluator，而是"如何预测 refined latent"的 refiner——**边界案例**，可作为 A3 判定边界的讨论素材。

### 8.5 Formalize-then-Optimize 模式：`N-Tok → S-Tok → π-Par / workflow`

- **定义**：先形式化为 Schematic，再以该结构为对象进行权重优化或 workflow 搜索。
- **成员**：
  ScoreFlow（`N-Tok → π-Par (generator) → S-Tok`，工作流生成器本身被 DPO 优化）· Meta Context Engineering（`N-Tok → N-Tok (pattern) → S-Tok (programmatic)`）· EvoAgentX（`π-Par → S-Tok`）
- **Integration mechanism clues（V2 新增）**：
  - ScoreFlow: [Abs: "Score-DPO accounts for quantitative feedback; gradient-based optimization in continuous space for workflow generation"]
  - Meta Context Engineering: [Abs: "bi-level framework: meta-level agent refines engineering skills via agentic crossover; base-level agent executes skills and optimizes context"]
- **观察**：该模式在文献中数量**少于 8.1/8.3**，但代表"Schematic Tokenized 结构成为显式优化对象"这一结构性新方向。

### 8.6 Internalize-then-Externalize 模式：`N-Tok → π-Par → N-Tok (skill)`

- **定义**：先把经验内化进 policy 权重，再由已更新的 policy 反向外化为可复用的 tokenized skill。拓扑方向与 8.3 Refine-then-Internalize 恰好相反。
- **成员**：
  Reinforcement Learning for Self-Improving Agent with Skill Library · SAGE
- **必然性**：假设某些 skill 只有在 policy 能"做出来"后才能被正确描述——先学会再总结；与 8.3 "先总结再学会"形成对照。
- **Integration mechanism clues（V2 新增）**：
  - SAGE: [Abs: "Sequential Rollout iteratively deploys agents across chain of similar tasks; skills from previous tasks accumulate in library and become available for subsequent tasks; Skill-integrated Reward complements outcome-based rewards"]
- **观察**：当前池内 2 篇明确代表，未达 3 篇 pattern 门槛，宜在 §D2 作为**萌芽模式**处理；是否升格为独立 pattern 取决于后续文献补录结果。

### 8.7 Externalize-for-Training 模式：`π-Par → N-Tok (raw) → V-Par`

- **定义**：由 policy 生成数据用于**训练 Evaluator**（而非训练 policy 自身）。
- **成员**：
  Self-Improving VLM Judges · (部分 Free Process Rewards 工作间接属此)
- **Integration mechanism clues（V2 新增）**：
  - Self-Improving VLM Judges: [Abs: "generate diverse multimodal instruction-response pairs; generate reasoning traces and judgments; train on correct judge answers; iterative self-improvement without human annotations"]
- **观察**：这是 `P7 + P4` 的混合，是 §D3 空白格中**最早开始被填补的那一种**——可作为 agenda 讨论的具体示例。

### 8.8 Multi-target 模式：一篇工作同时产出多类 Carrier

- **定义**：单篇工作的 Transformation 分支不止一条 Carrier 目标态。
- **代表**：
  - **SEAgent（★关注）**：`N-Tok (raw, vis+txt) → V-Par`、`→ N-Tok (refined)`、`→ π-Par`——[Abs: "World State Model for step-wise trajectory assessment; Curriculum Generator; adversarial imitation of failure actions and GRPO on successful ones; specialist-to-generalist training strategy"]
  - **G-Memory**：`N-Tok → S-Tok (graph)` + `N-Tok → N-Tok (insights)`
  - **AutoAgent**：`N-Tok → N-Tok (summary)` + `N-Tok → S-Tok (composite action)`
- **观察**：这类工作在 Survey 的单 pathway 章节中难以整体呈现，但恰好是 **Composition Section 的最佳案例**——证明"把 Pathway 作为分类原语"比"把工作作为分类原语"在分析粒度上更合适。

### 8.9 [CANDIDATE_NEW_PATTERN] Co-Evolving World Model 模式

- **定义**：policy agent 与 world model LLM 协同进化——world model 预测环境状态用于生成训练数据和推理时 look-ahead，policy 的改进反哺 world model 的数据质量。
- **候选成员**：
  - **WebEvolver** (2504.21024): [Abs: "co-evolving World Model LLM predicts next observation; serves dual roles: virtual web server generating self-instructed training data, and imagination engine during inference enabling look-ahead simulation"] — `π-Par ↔ V-Par (world model)` 双向协同
  - **WebSynthesis** (2507.04370): [Abs: "learned world model to simulate virtual web environments; policy agent performs efficient and reversible tree-based planning"] — `N-Tok → V-Par (world model) → N-Tok (synthetic) → π-Par`
  - **SEAgent** (已在 §8.8): 含 World State Model 组件
- **门槛评估**：WebEvolve + WebSynthesis 已达 2 篇，加 SEAgent 的 world model 组件 = 2.5 篇，接近 ≥3 篇门槛。命名可考虑 *World-Model-Augmented Self-Improvement* 或 *Co-Evolving World Model*。
- **与已知 pattern 的关系**：此模式与 Self-Reinforce (§8.1) 的区别在于 world model 是独立训练的 parametric 组件（而非仅用 LLM 做 self-reflection）；与 Evaluate-then-Optimize (§8.2) 的区别在于 world model 产出的是模拟环境/预测状态而非评估信号。
- **处置**：暂不升格为正式 pattern，保留 `[CANDIDATE_NEW_PATTERN]` 标记供 §D2 讨论。

**完整题目（仅 §8 独有新增，未在前述章节出现者）**
- SEAgent — *SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from Experience*