# TaxonomyV2 — Enhanced Taxonomy with Abstract-Augmented Annotations

> 基于 `Taxonomy.md` + `arxiv_abstracts_merged.md` + 四件套增强。
> 符号体系见 `Experience_Carrier.md` / `Transformation_Defination.md` / `Analysis_Framework.md`。
>
> **Carrier 记号速查**：`N-Tok` = Narrative Tokenized | `S-Tok` = Schematic Tokenized | `Lat` = Latent | `π-Par` = Policy Parameter | `V-Par` = Evaluator Parameter
> **注解**：`raw` / `refined` / `skill` / `rule` / `summary` / `SOP` / `workflow` / `trajectory` / `insight`
> **正交属性**：Modality `[txt]` `[vis+txt]` `[GUI]` `[embodied]` `[cross-modal]` | Source `{self}` `{human}` `{teacher}` | Method `⟨LLM-extract⟩` `⟨SFT⟩` `⟨RL: GRPO/PPO/DPO/ReST⟩` `⟨hybrid⟩`
> **来源**：`[src: abs]` = abstract | `[src: 四件套]` = 基准文件 | `[src: inferred]` = 推断

---

## Pathway P1: N-Tok → N-Tok（Intra-Tokenized Abstraction）

Raw trajectories → reflections / rules / summaries / insights / skills / strategies / hints / guidelines。
同层语义抽象，源与目标都是 Narrative Tokenized。

---

### Reflexion: Language Agents with Verbal Reinforcement Learning
- [原] Textual (Raw Experience) -> Textual (Reflection)
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, reflection)  [src: 四件套, abs]
- [Utilization] 生成的 reflection text 存入 episodic memory buffer，后续 trial 中 prepend 到 agent context 以诱导更好的决策；无参数更新  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] verbal RL：agent 对 task feedback 进行语言化反思，将反思文本维持在 episodic memory 中，用于后续 trial 的 decision-making  [src: abs]

---

### [新增] Reflection-Driven Control for Trustworthy Code Agents
- [Pathway] N-Tok (raw, txt, code generation trace) → N-Tok (refined, security guideline, repair example)  [src: abs, 四件套]
- [Utilization] agent 在生成过程中持续运行 internal reflection loop 监控和评估自身决策路径；检测到风险时从 evolving reflective memory 检索相关 repair examples 和 secure coding guidelines，注入后续推理步骤  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] 将 "self-reflection" 从 post hoc patch 提升为 agent reasoning process 中的显式步骤；evolving reflective memory 持续积累 repair examples 和 guidelines  [src: abs]

---

### ExpeL: LLM Agents Are Experiential Learners
- [原] Textual (Raw Experience) -> Textual (Reflection, Insights)
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, reflection, insight)  [src: 四件套, abs]
- [Utilization] 在 inference 时 recall 提取的 insights 和 past experiences，prepend 到 context 作为决策依据；无参数更新，适用于 proprietary API-based models  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] agent 从 training tasks 中自主收集经验并用自然语言提取知识，inference 时召回提取的 insights 和 past experiences 做 informed decisions  [src: abs]

---

### AutoManual: Constructing Instruction Manuals by LLM Agents via Interactive Environmental Learning
- [原] Textual (Raw Experience) -> Textual (Rule, Reflection)
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, rule, reflection)  [src: 四件套, abs]
- [Utilization] Planner agent 基于当前 rules 编码可执行计划；Formulator 将 rules 编译为 comprehensive manual，指导后续 planning；可 guide 更小的 LLM  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] 两 agent 协作：Planner 基于 rules 制定计划与环境交互，Builder 通过 structured rule system 在线更新规则，Formulator 编译为 manual；引入 case-conditioned prompting 缓解幻觉  [src: abs]

---

### AutoGuide: Automated Generation and Selection of Context-Aware Guidelines for LLM Agents
- [原] Textual (Raw Experience) -> Textual (Guideline)
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, guideline)  [src: 四件套, abs]
- [Utilization] 测试时按当前状态检索最相关的 guideline，prepend 到 context 提供 conditional guidance；替代 demonstration-based ICL  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] 从 offline experiences 自动生成 concise natural language 的 context-aware guidelines，采用 conditional structure 描述适用场景  [src: abs]

---

### Experiential Reflective Learning for Self-Improving LLM Agents (ERL)
- [原] (在 Experiential Reflective Learning 条目，无独立标注行；H²R 条目共用)
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, heuristic)  [src: 四件套, abs]
- [Utilization] 测试时基于当前 task 检索相关 heuristics，注入 agent context 指导执行；selective retrieval 对效果至关重要  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] 对 task trajectories 和 outcomes 进行反思生成 heuristics（actionable lessons），跨任务迁移；相比 few-shot trajectory prompting，heuristics 提供更 transferable 的抽象  [src: abs]

---

### H²R: Hierarchical Hindsight Reflection for Multi-Task LLM Agents
- [原] Textual (Raw Experience) -> Textual (Reflection)
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, reflection)  [src: 四件套, abs]
- [Utilization] 分层检索：high-level planning memory 与 low-level execution memory 分别检索，prepend 到 agent context 用于新任务决策  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] hierarchical memory architecture + Hierarchical Hindsight Reflection (H²R)：将 past agent-environment interactions 蒸馏为可复用的分层知识，解耦 planning memory 与 execution memory  [src: abs]

---

### Agent S: An Open Agentic Framework that Uses Computers Like a Human
- [原] Token (Visual + Textual, Raw Experience) -> Textual (Summary, Reflection)
- [Pathway] N-Tok (raw, GUI) → N-Tok (refined, summary, reflection)  [src: 四件套, abs]
- [Utilization] experience-augmented hierarchical planning：从 external knowledge search 和 internal experience retrieval 中学习，多层级指导 task planning 和 subtask execution  [src: abs]
- [Modality] [GUI]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] Agent-Computer Interface (ACI) 增强 MLLM 的 reasoning 和 control 能力；experience 来自过往 GUI 交互的 retrieval  [src: abs]

---

### ELITE: Experiential Learning and Intent-Aware Transfer for Self-improving Embodied Agents
- [原] Token (Visual + Textual, Raw Experience) -> Textual (Summary)
- [Pathway] N-Tok (raw, embodied) → N-Tok (refined, strategy)  [src: 四件套, abs]
- [Utilization] intent-aware retrieval 从 strategy pool 中识别相关策略并应用于当前任务；self-reflective knowledge construction 持续更新 strategy pool  [src: abs]
- [Modality] [embodied]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] self-reflective knowledge construction 从 execution trajectories 中提取 reusable strategies，通过 structured refinement operations 维护 evolving strategy pool  [src: abs]

---

### Learn Like Humans: Use Meta-cognitive Reflection for Efficient Self-Improvement (MARS)
- [原] Textual (Raw Experience) -> Textual (Strategy)
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, rule, strategy)  [src: 四件套, abs]
- [Utilization] 将 synthesized insights 优化为 instructions，系统性地 refine reasoning logic，注入后续推理；单次 recurrence cycle 内完成  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] principle-based reflection（抽象规范性规则避免错误）+ procedural reflection（导出 step-by-step 成功策略），在单次循环内实现高效 self-evolution  [src: abs]

---

### Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory
- [原] Textual (Raw Experience) -> Textual (Summary)
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, summary, strategy)  [src: 四件套, abs]
- [Utilization] persistent evolving memory 在 inference time 存储和复用 accumulated strategies / code snippets / insights；self-curated，聚焦 concise transferable snippets  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] test-time learning：无需 ground-truth labels 或 human feedback，agent 自主积累和复用解题策略；memory 是 self-curated，聚焦 concise transferable snippets  [src: abs]

---

### AutoSkill: Experience-Driven Lifelong Learning via Skill Self-Evolution
- [原] Textual (Raw Experience) -> Textual (Skill)
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, skill)  [src: 四件套, abs]
- [Utilization] 动态将相关 skills 注入 future requests，无需 retrain underlying model；model-agnostic plugin layer  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] 从 dialogue 和 interaction traces 中自动 derive / maintain / reuse skills；支持 continual self-evolution；standardized skill representation 支持跨 agent/user/task 共享  [src: abs]

---

### XSkill: Continual Learning from Experience and Skills in Multimodal Agents
- [原] Token(Visual + Textual, Raw Experience) -> Textual (Skill)
- [Pathway] N-Tok (raw, vis+txt) → N-Tok (refined, skill)  [src: 四件套, abs]
- [Utilization] 双流 retrieval：experiences 提供 action-level guidance（tool selection + decision making），skills 提供 task-level guidance（planning + tool use）；visual observations 作为 retrieval grounding  [src: abs]
- [Modality] [cross-modal]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] visually grounded summarization + cross-rollout critique：从 multi-path rollouts 中 distill experiences 和 skills，形成 continual learning loop  [src: abs]

---

### SkillClaw: Let Skills Evolve Collectively with Agentic Evolver
- [原] Token (Raw Experience, Visual + Textual) -> Textual (Skill)
- [Pathway] N-Tok (raw, vis+txt) → N-Tok (refined, skill)  [src: 四件套, abs]
- [Utilization] shared skill repository 跨用户同步；autonomous evolver 识别 recurring behavioral patterns 并转化为 skill updates（refine 或 extend） [src: abs]
- [Modality] [cross-modal]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] cross-user collective skill evolution：将 multi-user heterogeneous experiences 转化为 reliable skill updates，通过 refining existing skills 或 extending with new capabilities  [src: abs]

---

### Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills
- [原] Textual (Raw Experience) -> Textual (Skill)
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, skill)  [src: 四件套, abs]
- [Utilization] skill directory 作为 declarative knowledge 注入 agent，无需 parameter updates / external retrieval modules；skills 跨 LLM scales 和 OOD settings 迁移  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] parallel fleet of sub-agents 分析 diverse execution pool，提取 trajectory-specific lessons 后 hierarchical consolidation 为 unified conflict-free skill directory；trajectory-grounded evolution，不 memorize task instances  [src: abs]

---

### FLEX: Continuous Agent Evolution via Forward Learning from Experience
- [原] Textual (Raw Experience) -> Textual (Strategy)
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, strategy)  [src: 四件套, abs]
- [Utilization] structured experience library 通过 continual reflection 积累，为后续推理提供 strategy guidance；gradient-free，无参数更新  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] 从 successes 和 failures 中持续反思构建 structured experience library；发现 experiential growth 的 scaling law 和 experience inheritance 现象  [src: abs]

---

### Human-Inspired Continuous Learning of Internal Reasoning Processes
- [原] 与 FLEX 共享标注：Textual (Raw Experience) -> Textual (Strategy)，使用 LLM 进行抽取，无参数微调
- [Pathway] N-Tok (raw, txt, reasoning trajectories + environmental interactions) → N-Tok (refined, strategy, structured learning material)  [src: 四件套, abs]
- [Utilization] 记录的 internal reasoning trajectories 和 environmental interactions 作为 structured learning material，优化 task-level content 和 reasoning activities 的 organization/scheduling/evolution；learning alongside processing：cognitive structures 在执行中持续改进  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩（无参数更新，treats internal thinking processes as primary learning objects） [src: abs]
- [机制] 将 internal thinking processes 显式视为 primary learning objects：systematically record internal reasoning trajectories + environmental interactions → optimize reasoning organization/scheduling/evolution；hierarchical learning-to-learn mechanism 联合适应 task-level parameters 和 learning strategies  [src: abs]
- [Pathway 说明] 原 Taxonomy.md 中本文与 FLEX 共享同一行标注，视为相似路径归入 P1。若后续发现两者机制有显著差异，可拆分。  [src: inferred]

---

### EvoSkill: Automated Skill Discovery for Multi-Agent Systems
- [原] Textual (Raw Experience) -> Textual (Skill)
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, skill)  [src: 四件套, abs]
- [Utilization] 自动发现和 refine 的 skills 存入 structured reusable skill folders；Pareto frontier selection 保留提升 validation performance 的 skills  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] 从 execution failures 分析中 iterative failure analysis → propose new skills or edits → materialize into structured folders；model frozen，skills 可 zero-shot transfer  [src: abs]

---

### EvoTool: Self-Evolving Tool-Use Policy Optimization
- [原] Textual (Raw Experience) -> Textual (tool-use policy)
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, tool-use policy)  [src: 四件套, abs]
- [Utilization] 优化的 modular tool-use policy（Planner/Selector/Caller/Synthesizer）在推理时指导 agent 的工具调用决策；gradient-free evolutionary paradigm  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] Trajectory-Grounded Blame Attribution 定位 failure 到具体 module → Feedback-Guided Targeted Mutation 用自然语言 critique 编辑 → Diversity-Aware Population Selection 保持 solution diversity  [src: abs]

---

### AutoAgent: Evolving Cognition and Elastic Memory Orchestration for Adaptive Agents
- [原] Textual (Raw Experience) -> Textual (Summary)
- [原] Textual (Raw Experience) -> Programmatic (composite action)
- [Pathway] (a) N-Tok (raw, txt) → N-Tok (refined, summary, episodic abstraction)  [src: 四件套, abs]
- [Pathway] (b) N-Tok (raw, txt) → S-Tok (composite action)  [src: 四件套, abs]
- [Utilization] structured prompt-level cognition（tools / self-capabilities / peer expertise / task knowledge）与 live task context 结合选择 actions（tool calls / LLM-based generation / inter-agent requests）；Elastic Memory Orchestrator 动态组织 interaction history：preserve raw records / compress redundant trajectories / construct reusable episodic abstractions  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩（closed-loop cognitive evolution, 无 external retraining） [src: abs]
- [机制] closed-loop cognitive evolution：intended actions 与 observed outcomes 对齐持续更新 cognition 并 expand reusable skills；Elastic Memory Orchestrator 减少 token overhead 同时保留 decision-critical evidence  [src: abs]

---

### AgentEHR: Advancing Autonomous Clinical Decision-Making via Retrospective Summarization
- [原] Textual (Raw Experience) -> Textual (Summary)
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, summary)  [src: 四件套, abs]
- [Utilization] RetroSum：retrospective summarization mechanism 动态重评 interaction history 防止 long-context information loss；evolving strategy 从 memory bank 检索 accumulated experience  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] retrospective summarization 防止 long-context information loss + unbroken logical coherence；evolving strategy 从 memory bank 检索经验桥接 domain gap  [src: abs]

---

### Contextual Experience Replay for Self-Improvement of Language Agents (CER)
- [原] Textural (Raw Experience) -> Textual (Skill)
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, skill)  [src: 四件套, abs]
- [Utilization] 测试时从 dynamic memory buffer 检索 relevant knowledge 并 augment agent context；experiences 涵盖 environment dynamics 和 common decision-making patterns  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] training-free：accumulate and synthesize past experiences into dynamic memory buffer，跨任务复用 environment dynamics 和 decision patterns  [src: abs]

---

### JEF-Hinter: Leveraging Offline Knowledge for Improving Web Agents Adaptation
- [原] Textual (Raw Experience) -> Textual (Hints)
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, hint)  [src: 四件套, abs]
- [Utilization] 推理时 retriever 为当前 state 选择 relevant hints，提供 targeted guidance；同时利用 successful 和 failed trajectories  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] zooming mechanism 突出长轨迹中的 decisive steps，capture strategies 和 pitfalls；从 offline traces 蒸馏 compact context-aware hints  [src: abs]

---

### Iterative Experience Refinement of Software-Developing Agents
- [原] Textual (Raw Experience) -> Textual (shortcut-oriented experience)
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, shortcut-oriented experience)  [src: 四件套, abs]
- [Utilization] refined experiences 注入 agent 减少 errors 和提升效率；heuristic experience elimination 优先保留 high-quality frequently-used experiences  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] successive pattern（batch 内基于最近经验 refine）+ cumulative pattern（跨 batch 积累）；heuristic elimination 用 11.54% 高质量子集达到更好性能  [src: abs]

---

### MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents
- [原] Textual (Raw Experience) -> Textual
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, memory skill)  [src: 四件套, abs]
- [Utilization] controller 学习选择 relevant skills → LLM-based executor 产生 skill-guided memories；designer 定期 review hard cases 并 refine/evolve skill set  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] 将记忆操作重新定义为 learnable evolvable memory skills（extract / consolidate / prune）；closed-loop：skill-selection policy 和 skill set 同时改进  [src: abs]

---

### MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs
- [原] Textual (Raw Experience) -> Textual (Reflection, Feedback)
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, reflection)  [src: 四件套, abs]
- [Utilization] multi-agent multi-persona debaters 生成的 reflections 用于改进 agent reasoning；避免单一 LLM self-reflection 的 thought degeneration  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] 用 multi-agent with multi-persona debaters 替代单一 self-reflection，提高 reflection diversity，克服 degeneration of thought  [src: abs]

---

### ProcMEM: Learning Reusable Procedural Memory from Experience via Non-Parametric PPO
- [原] Textual (Raw Experience) -> Textual (Procedural)
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, procedural skill)  [src: 四件套, abs]
- [Utilization] procedural memory（Skill-MDP 定义的 executable Skills）在推理时复用，减少 computational redundancy 和 execution instability  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩（Non-Parametric PPO 用于 Skill verification，无参数更新） [src: abs, inferred]
- [机制] Skill-MDP 形式化：passive episodic narratives → executable Skills (activation/execution/termination conditions)；Non-Parametric PPO 用 semantic gradients 做候选生成 + PPO Gate 做 robust verification  [src: abs]

---

### Memp: Exploring Agent Procedural Memory
- [原] Textual (Raw Experience) -> Textual (Procedural)
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, procedural)  [src: 四件套, abs]
- [Utilization] procedural memory 提供 fine-grained step-by-step instructions 和 higher-level script-like abstractions，推理时检索复用  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] 从 past agent trajectories 蒸馏为 step-by-step instructions + script-like abstractions；dynamic regimen 持续 update/correct/deprecate，procedural memory 可跨模型迁移  [src: abs]

---

### Remember Me, Refine Me: A Dynamic Procedural Memory Framework (ReMe)
- [原] Textual (Raw Experience) -> Textual (Procedural)
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, procedural)  [src: 四件套, abs]
- [Utilization] context-adaptive reuse：scenario-aware indexing 将 historical insights 适配到新 context；utility-based refinement 维护 compact high-quality experience pool  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] multi-faceted distillation（success patterns + failure triggers + comparative insights）+ utility-based refinement（自主 add valid / prune outdated）；memory-scaling effect：Qwen3-8B+ReMe 超越无 memory 的 Qwen3-14B  [src: abs]

---

### ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory
- [原] Textual (Raw Experience) -> Textual
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, reasoning strategy)  [src: 四件套, abs]
- [Utilization] 测试时检索 relevant memories 注入 agent interaction；MaTTS（memory-aware test-time scaling）通过 scaling compute 产生更多样经验，反过来提升 memory 质量  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] 从 agent's self-judged successful and failed experiences 中蒸馏 generalizable reasoning strategies；MaTTS 建立 memory 与 test-time scaling 的正反馈循环  [src: abs]

---

### MemEvolve: Meta-Evolution of Agent Memory Systems
- [原] Textual (Raw Experience) -> Textual
- [Pathway] N-Tok (raw, txt) → N-Tok (refined)  [src: 四件套, abs]
- [Utilization] meta-evolutionary：不仅 evolve agent 的 experiential knowledge，还 evolve memory architecture 本身，使其适应 diverse task contexts  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] meta-evolutionary framework：同时 evolve agents' experiential knowledge 和 memory architecture（encode/store/retrieve/manage 四模块），跨 task 和 LLM backbone 泛化  [src: abs]

---

### MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory
- [原] Textual (Raw Experience) -> Textual
- [Pathway] N-Tok (raw, txt) → N-Tok (refined)  [src: 四件套, abs]
- [Utilization] Two-Phase Retrieval 过滤 noise 并识别 high-utility strategies，通过 environmental feedback 持续更新；runtime improvement 无需 weight updates  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩（模仿 RL，non-parametric） [src: abs, inferred]
- [机制] decouple stable reasoning from plastic memory；non-parametric approach 在 episodic memory 上做 RL，reconcile stability-plasticity dilemma  [src: abs]

---

### Meta-Policy Reflexion: Reusable Reflective Memory and Rule Admissibility
- [原] Textual (Raw Experience) -> Textual
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, rule, reflection)  [src: 四件套, abs]
- [Utilization] soft memory-guided decoding + hard rule admissibility checks (HAC)：structured predicate-like Meta-Policy Memory (MPM) 在推理时约束 agent decisions  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] 将 LLM-generated reflections 整合为 structured predicate-like MPM，通过 soft decoding + hard rule admissibility 两个 complementary 机制在推理时使用；无需 weight updates  [src: abs]

---

### Learning Hierarchical Procedural Memory for LLM Agents (MACLA)
- [原] Textual (Raw Experience) -> Textual (Procedural)
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, procedural)  [src: 四件套, abs]
- [Utilization] Bayesian posteriors 跟踪 reliability → expected-utility scoring 选择 action → contrastive refinement 通过对比 successes/failures 改进 procedures；frozen LLM  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] 从 trajectories 提取 reusable procedures，Bayesian selection + contrastive refinement；2851 trajectories → 187 procedures（56s 构建，2800x 快于参数训练 baseline） [src: abs]

---

### Learning How to Remember: A Meta-Cognitive Management Method (MCMA)
- [原] Textual (Raw Experience) -> Textual
- [Pathway] N-Tok (raw, txt) → N-Tok (refined)  [src: 四件套, abs]
- [Utilization] memory copilot（用 DPO 训练）决定 memories 的 structure / abstraction / reuse 方式；hierarchy of abstraction levels 支持 selective reuse  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩ + ⟨RL: DPO⟩（memory copilot 训练） [src: abs, inferred]
- [机制] 将 memory abstraction 视为 learnable cognitive skill：frozen task model + learned memory copilot（DPO 训练），memory hierarchy 支持 selective reuse by task similarity  [src: abs]

---

### SE-Agent: Self-Evolution Trajectory Optimization in Multi-Step Reasoning
- [原] Textual (Raw Experience) -> Textual
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, trajectory)  [src: 四件套, abs]
- [Utilization] revision / recombination / refinement 三种操作优化 prior trajectories，生成的 improved trajectories 注入 agent 指导后续 reasoning  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] evolutionary mechanism 对 prior pilot trajectories 做 revision/recombination/refinement；cross-trajectory inspiration 扩展 search space beyond local optima  [src: abs]

---

### Trajectory-Informed Memory Generation for Self-Improving Agent Systems
- [原] Textual (Raw Experience) -> Textual (Rule, Reflections, Summaries)
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, strategy tip, recovery tip, optimization tip)  [src: 四件套, abs]
- [Utilization] Adaptive Memory Retrieval System 基于 multi-dimensional similarity 将 relevant learnings 注入 agent prompts  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] 四组件：Trajectory Intelligence Extractor → Decision Attribution Analyzer → Contextual Learning Generator（三种 guidance：strategy tips / recovery tips / optimization tips）→ Adaptive Memory Retrieval  [src: abs]

---

### Training-Free Group Relative Policy Optimization
- [原] Textual (Raw Experience) -> Textual (Rule, Reflections, Summaries)
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, experiential knowledge as token prior)  [src: 四件套, abs]
- [Utilization] learned token prior 在 LLM API 调用时无缝集成以 guide model behavior；替代 costly parameter updates  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] 利用 group relative semantic advantage（非 numerical），在多轮 learning 中迭代蒸馏高质量 experiential knowledge 作为 token prior，无需任何 parameter update  [src: abs]

---

### Skill Set Optimization: Reinforcing Language Model Behavior via Transferable Skills
- [原] Textual (Raw Experience) -> Textual
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, skill)  [src: 四件套, abs]
- [Utilization] skills 以 in-context 方式提供给 LLM actor 以 reinforce high-reward behaviors；skill set 通过 pruning 持续优化  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] 提取 common high-reward subtrajectories → 生成 subgoals 和 instructions 代表每个 skill；pruning 去除不再产生 high rewards 的 skills  [src: abs]

---

### GEMS: Agent-Native Multimodal Generation with Memory and Skills
- [原] Textual (Raw Experience) -> Textual (Summaries, Reflections)
- [Pathway] N-Tok (raw, vis+txt) → N-Tok (refined, summary, reflection)  [src: 四件套, abs]
- [Utilization] Agent Memory 提供 persistent trajectory-level memory，hierarchically 存储 factual states 和 compressed experiential summaries；Agent Skill 提供 on-demand domain-specific expertise  [src: abs]
- [Modality] [cross-modal]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] 三组件：Agent Loop（multi-agent closed-loop optimization）+ Agent Memory（hierarchical trajectory-level）+ Agent Skill（extensible domain expertise）；不修改生成模型参数  [src: abs]

---

### Aligning Agentic World Models via Knowledgeable Experience Learning (WorldMind)
- [原] Token (Visual + Textual, Raw Experience) -> Textual (Heuristic, Reflection Causal Rule)
- [Pathway] N-Tok (raw, embodied) → N-Tok (refined, heuristic, causal rule)  [src: 四件套, abs]
- [Utilization] symbolic World Knowledge Repository 在推理时提供 physical feasibility 约束和 task optimality 指导；无需 training/fine-tuning  [src: abs]
- [Modality] [embodied]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] 两类经验统一：Process Experience（通过 prediction errors 强制 physical feasibility）+ Goal Experience（通过 successful trajectories 指导 task optimality）；跨模型跨环境迁移  [src: abs]

---

### [新增] HiMemVLN: Enhancing Reliability of Open-Source Zero-Shot VLN with Hierarchical Memory System
- [Pathway] N-Tok (raw, embodied) → N-Tok (refined, hierarchical visual memory)  [src: abs, 四件套]
- [Utilization] Hierarchical Memory System 增强 visual perception recall 和 long-term localization；mitigate "Navigation Amnesia"（导航过程中的信息遗忘），使 open-source VLN 性能接近 closed-source 方法  [src: abs]
- [Modality] [embodied]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩（无参数更新） [src: abs]
- [机制] 识别 "Navigation Amnesia" 为 open-source vs closed-source VLN 性能差距的关键因素；Hierarchical Memory System 融入 multimodal large model 改善 visual perception recall  [src: abs]

---

### R⁴: Retrieval-Augmented Reasoning for Vision-Language Models in 4D Spatio-Temporal Space
- [原] Token (Raw Experience, Visual + Textual) -> Textual
- [Pathway] N-Tok (raw, embodied) → N-Tok (refined, 4D knowledge)  [src: 四件套, abs]
- [Utilization] 4D knowledge database 在推理时通过 semantic/spatial/temporal keys 检索 relevant observations 并注入 VLM reasoning；training-free  [src: abs]
- [Modality] [embodied]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] 持续构建 4D knowledge database（object-level semantic descriptions 锚定在 metric space and time），retrieval 直接在 4D space 操作  [src: abs]

---

### Agentic Rubrics as Contextual Verifiers for SWE Agents
- [原] Policy Parameter -> Textual (Rubrics Rules)
- [Pathway] π-Par → N-Tok (refined, rubric checklist)  [src: 四件套, abs]
- [Pathway 说明] 该路径本质是 π-Par → N-Tok（参数化知识外化为 Tokenized rubric），但 rubric 本身作为 verifier 使用（Utilization），而非用于下游训练。在 P1 节归类因为 rubric generation 的核心机制是 LLM-extract（交互式上下文探索 + 文本合成），无 Evaluator 参数更新。  [src: inferred]
- [Utilization] 生成的 context-grounded rubric checklist 在推理时对 candidate patches 评分，无需 test execution；rubric scores 与 ground-truth tests 一致，且能捕获测试未覆盖的问题  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] expert agent 与 repository 交互创建 context-grounded rubric checklist；agentic context gathering 对产生 codebase-specific unambiguous criteria 至关重要  [src: abs]

---

### ReCreate: Reasoning and Creating Domain Agents Driven by Experience
- [原] Textual (Raw Experience) -> Textual
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, domain pattern)  [src: 四件套, abs]
- [Utilization] experience storage and retrieval → reasoning-creating synergy pipeline 将 execution experience 映射为 scaffold edits → hierarchical updates 抽象为 reusable domain patterns  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] agent-as-optimizer paradigm：从 interaction histories 中学习，三组件（experience storage/retrieval + reasoning-creating synergy + hierarchical updates）自动创建 domain agents  [src: abs]

---

## Pathway P2: N-Tok → S-Tok（Intra-Tokenized Formalization）

Raw trajectories / logs → code / workflows / SOPs / graphs / APIs / decision trees。
同层形式化程度提升。

---

### AFlow: Automating Agentic Workflow Generation
- [原] Textual (Raw Experience) -> Workflow
- [Pathway] N-Tok (raw, txt) → S-Tok (workflow, code-represented)  [src: 四件套, abs]
- [Utilization] 搜索到的最优 workflow（code-represented）在推理时执行，orchestrate LLM-invoking nodes  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩ + MCTS 搜索  [src: abs]
- [机制] 将 workflow optimization 重构为 code-represented workflows 上的搜索问题，MCTS 迭代 refine workflows through code modification, tree-structured experience, and execution feedback  [src: abs]

---

### A²Flow: Automating Agentic Workflow Generation via Self-Adaptive Abstraction Operators
- [原] Textual (Raw Experience) -> Workflow
- [Pathway] N-Tok (raw, txt) → S-Tok (workflow)  [src: 四件套, abs]
- [Utilization] 生成的 execution operators 作为 reusable building blocks 构建 workflow，operator memory mechanism 保留历史 outputs 丰富 context  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩ + MCTS  [src: abs]
- [机制] 三阶段 operator extraction：case-based initial generation → operator clustering and abstraction → deep extraction with long CoT；self-adaptive abstraction 无需手动预定义 operators  [src: abs]

---

### Agent Workflow Memory (AWM)
- [原] Textual (Raw Experience) -> Workflow
- [Pathway] N-Tok (raw, txt) → S-Tok (workflow)  [src: 四件套, abs]
- [Utilization] 从 training examples 或 test queries 中 induce workflows，selectively provide workflows 给 agent 指导后续 actions；适用于 offline 和 online 场景  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] induce commonly reused routines (workflows) 并选择性提供给 agent；跨 task/website/domain 泛化  [src: abs]

---

### Investigate-Consolidate-Exploit: A General Strategy for Inter-Task Agent Self-Evolution (ICE)
- [原] Textual (Raw Experience) -> Textual (Workflow, Pipeline)
- [Pathway] N-Tok (raw, txt) → S-Tok (workflow, pipeline)  [src: 四件套, abs]
- [Utilization] consolidated workflows 和 pipelines 用于 improved task execution；API calls 减少 80%，GPT-3.5+ICE 匹配 raw GPT-4  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] investigate planning/execution trajectories → consolidate into simplified workflows/pipelines → exploit for future tasks；跨任务知识迁移  [src: abs]

---

### [新增] KG-RAG: Enhancing GUI Agent Decision-Making via Knowledge Graph-Driven RAG
- [Pathway] N-Tok (raw, GUI) → S-Tok (UI Transition Graph, vector database)  [src: abs, 四件套]
- [Utilization] intent-guided LLM search 从 structured vector database 检索 actionable navigation paths 增强 agent decision-making；KG-Android-Bench 和 KG-Harmony-Bench 两个 benchmark  [src: abs]
- [Modality] [GUI]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] 将 fragmented UI Transition Graphs (UTGs) 转化为 structured vector databases；intent-guided retrieval 生成 actionable navigation paths  [src: abs]

---

### SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills
- [原] Token(Visual + Textual, Raw Experience) -> Structural (API)
- [Pathway] N-Tok (raw, GUI) → S-Tok (API)  [src: 四件套, abs]
- [Utilization] API library 作为 lightweight plug-and-play APIs 在推理时调用；APIs 可在不同 web agents 间共享，弱 agent 使用强 agent 合成的 APIs 可提升 54.3%  [src: abs]
- [Modality] [GUI]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] 在新网站上自主 discover skills → execute for practice → distill practice experiences into robust APIs；iterative exploration 持续扩展 API library  [src: abs]

---

### Code as Policies: Language Model Programs for Embodied Control
- [原] Textual (Raw Experience) -> Structural (Programmic)
- [Pathway] N-Tok (raw, txt) → S-Tok (code, robot policy)  [src: 四件套, abs]
- [Utilization] 生成的 robot policy code 在 robot 上执行：express functions/feedback loops，process perception outputs，parameterize control primitive APIs  [src: abs]
- [Modality] [embodied]  [src: abs]
- [Source] {human}（few-shot prompting 中的 example commands） [src: abs, inferred]
- [Method] ⟨LLM-extract⟩（few-shot prompting，无参数更新） [src: abs]
- [机制] LLM 通过 few-shot prompting 从自然语言命令生成 robot policy code；hierarchical code-gen（递归定义 undefined functions）支持 complex code  [src: abs]

---

### AriGraph: Learning Knowledge Graph World Models with Episodic Memory for LLM Agents
- [原] Textual (Raw Experience) -> Structural (Graph)
- [Pathway] N-Tok (raw, txt) → S-Tok (knowledge graph)  [src: 四件套, abs]
- [Utilization] memory graph（集成 semantic + episodic memories）在 exploration 中持续更新，support planning 和 decision-making  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] agent 在探索环境时构建和更新 memory graph，集成 semantic 和 episodic memories；增强复杂交互式文本游戏中的 planning 和 reasoning  [src: abs]

---

### [新增] CraniMem: Cranial Inspired Gated and Bounded Memory for Agentic Systems
- [Pathway] N-Tok (raw, txt) → S-Tok (knowledge graph) + N-Tok (refined, consolidated memory)  [src: abs, 四件套]
- [Utilization] goal-conditioned gating + utility tagging + bounded episodic buffer（near-term continuity）+ structured long-term knowledge graph（durable semantic recall）；scheduled consolidation loop replays high-utility traces into graph while pruning low-utility items  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] neurocognitively motivated multi-stage memory：gated and bounded design 防止 unstable retention 和 distractor content；consolidation loop 控制 memory growth 和 interference  [src: abs]

---

### A-Mem: Agentic Memory for LLM Agents
- [原] Textual (Raw Experience) -> Structured (Graph)
- [Pathway] N-Tok (raw, txt) → S-Tok (knowledge graph)  [src: 四件套, abs]
- [Utilization] 动态组织记忆为 interconnected knowledge networks，通过 dynamic indexing and linking 实现 memory evolution；新记忆触发历史记忆的 contextual representations 更新  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] Zettelkasten-inspired：每条新记忆生成含 structured attributes 的 comprehensive note，分析历史记忆建立 meaningful connections，触发 memory evolution  [src: abs]

---

### GAAMA: Graph Augmented Associative Memory for Agents
- [原] (无独立标注，GSEM 条目共用)
- [Pathway] N-Tok (raw, txt) → S-Tok (knowledge graph)  [src: 四件套, abs]
- [Utilization] 四种节点类型（episode/fact/reflection/concept）+ 五种边类型；retrieval 结合 cosine-similarity kNN 与 edge-type-aware Personalized PageRank  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] concept-mediated hierarchical knowledge graph 三步构建：verbatim episode preservation → LLM-based atomic facts + topic-level concept nodes extraction → higher-order reflections synthesis  [src: abs]

---

### GSEM: Graph-based Self-Evolving Memory for Experience Augmented Clinical Reasoning
- [原] Textual (Raw Experience) -> Structural (Knowledge Graph)
- [Pathway] N-Tok (raw, txt) → S-Tok (knowledge graph)  [src: 四件套, abs]
- [Utilization] dual-layer memory graph 支持 applicability-aware retrieval 和 online feedback-driven calibration of node quality and edge weights  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] dual-layer memory graph：capture decision structure within each experience + relational dependencies across experiences；online feedback-driven calibration  [src: abs]

---

### SGMem: Sentence Graph Memory for Long-Term Conversational Agents
- [原] Textual (Raw Experience) -> Structural (Graph)
- [Pathway] N-Tok (raw, txt) → S-Tok (sentence graph)  [src: 四件套, abs]
- [Utilization] 结合 retrieved raw dialogue 与 generated memory（summaries/facts/insights），为 LLM 提供 coherent relevant context 用于 response generation  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] sentence-level graphs within chunked units，capture associations across turn-/round-/session-level contexts；combine raw dialogue retrieval with generated memory  [src: abs]

---

### Zep: A Temporal Knowledge Graph Architecture for Agent Memory
- [原] Textual (Raw Experience) -> Structural (Graph)
- [Pathway] N-Tok (raw, txt) → S-Tok (temporal knowledge graph)  [src: 四件套, abs]
- [Utilization] Graphiti engine 动态合成 unstructured conversational data 和 structured business data，保持 historical relationships 用于 cross-session information synthesis  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] temporally-aware knowledge graph engine (Graphiti) 动态合成对话和业务数据，保持历史关系；在 LongMemEval 上 accuracy 提升 18.5% 同时 latency 降 90%  [src: abs]

---

### G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems
- [原] Textual (Raw Experience) -> Structural (Graph)
- [原] Textual (Raw Experience) -> Textual (Insights)
- [Pathway] N-Tok (raw, txt) → S-Tok (graph, three-tier) + N-Tok (refined, insight)  [src: 四件套, abs]
- [Utilization] bi-directional memory traversal：检索 high-level generalizable insights（跨 trial 知识）+ fine-grained condensed interaction trajectories（prior collaboration experiences） [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] three-tier graph hierarchy（insight/query/interaction graphs），inspired by organizational memory theory；bi-directional traversal 检索 cross-trial knowledge + collaboration experiences  [src: abs]

---

### GPTSwarm: Language Agents as Optimizable Graphs
- [原] Textual (Raw Experience) -> Structural (Graph)
- [Pathway] N-Tok (raw, txt) → S-Tok (computational graph)  [src: 四件套, abs]
- [Utilization] graph optimizers 在推理前 refine node-level LLM prompts（node optimization）和 graph connectivity（edge optimization）；通过训练优化 graph 参数  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩ + 训练优化（automatic graph optimizers） [src: abs, inferred]
- [机制] 将 LLM-based agents 描述为 computational graphs（nodes=functions processing multimodal data or querying LLMs, edges=information flow）；graph 可递归组合表示 inter-agent collaboration  [src: abs]

---

### Arbor: A Framework for Reliable Navigation of Critical Conversation Flows
- [原] Decision Tree -> edge-list representation (Execution Graph)
- [Pathway] S-Tok (decision tree) → S-Tok (execution graph, DAG)  [src: 四件套, abs]
- [Utilization] DAG-based orchestration：runtime 时 iteratively retrieve current node's outgoing edges → evaluate valid transitions via LLM → delegate response generation；per-turn latency 降低 57.1%  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {human}（decision tree 来自 clinical triage 领域知识） [src: inferred]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] 将 decision tree 标准化为 edge-list representation 存储，DAG-based orchestration 在 runtime 动态检索和评估 transitions  [src: abs]

---

### Automated Design of Agentic Systems (ADAS / Meta Agent Search)
- [原] Textual (Raw Experience) -> Structural (Programmic)
- [Pathway] N-Tok (raw, txt) → S-Tok (code, agentic system)  [src: 四件套, abs]
- [Utilization] meta agent 编程生成的新 agents（in code）直接在目标任务上执行；ever-growing archive of discoveries 用于迭代改进  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] Meta Agent Search：meta agent 在 code 中迭代编程新的 agentic systems，利用 ever-growing archive of previous discoveries；agent 可跨 domain 和 model 迁移  [src: abs]

---

### CoEvoSkills: Self-Evolving Agent Skills via Co-Evolutionary Verification
- [原] Textual (Raw Experience) -> Structural (Skill)
- [Pathway] N-Tok (raw, txt) → S-Tok (skill, multi-file package)  [src: 四件套, abs]
- [Utilization] 生成的 multi-file skill packages 在推理时加载执行；Surrogate Verifier 提供 informative actionable feedback 无需 ground-truth test content  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] Skill Generator 迭代 refine skills + Surrogate Verifier 共同进化提供 feedback；skills 是 structured bundles of interdependent multi-file artifacts（超越 simple tools） [src: abs]

---

### [新增] Organizing, Orchestrating, and Benchmarking Agent Skills at Ecosystem Scale (AgentSkillOS)
- [Pathway] N-Tok (raw, txt) → S-Tok (DAG-based skill pipeline)  [src: abs, 四件套]
- [Utilization] capability tree 组织 skills 为 hierarchical categories 支持 efficient discovery；DAG-based orchestration 执行 multi-skill pipelines；tree-based retrieval 有效逼近 oracle skill selection；200-200K skills 规模下验证  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] 首个 principled framework for skill selection / orchestration / ecosystem-level management；DAG-based orchestration 显著优于 native flat invocation  [src: abs]

---

### [新增] SkillNet: Create, Evaluate, and Connect AI Skills
- [Pathway] heterogeneous sources → S-Tok (skill, unified ontology)  [src: abs, 四件套]
- [Utilization] 200K+ skills 的 open infrastructure：unified ontology 支持 multi-dimensional evaluation（Safety / Completeness / Executability / Maintainability / Cost-awareness）；ALFWorld / WebShop / ScienceWorld 上提升 average rewards 40%，减少 execution steps 30%  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self} + {human}（heterogeneous sources） [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] 将 skills 形式化为 evolving composable assets，建立从 transient experience 到 durable mastery 的基础设施  [src: abs]

---

### Meta Context Engineering via Agentic Skill Evolution (MCE)
- [原] Textual (Raw Experience) -> Textual (Pattens, Summmaries) -> Structured/Programmatic
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, pattern, summary) → S-Tok (code, context artifact)  [src: 四件套, abs]
- [Utilization] base-level agent 执行 skills 并优化 context 为 flexible files and code；meta-level agent 通过 agentic crossover 搜索和 refine engineering skills  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] bi-level framework：meta-level agent 通过 agentic crossover（deliberative search over history of skills/executions/evaluations）refine engineering skills；base-level agent 执行 skills 并优化 context  [src: abs]

---

## Pathway P3: Tokenized → Latent（Latent Compression）

Raw trajectories → KV cache / soft prompts / continuous memory tokens。
跨层压缩，Tokenized → Latent。

---

### MemGen: Weaving Generative Latent Memory for Self-Evolving Agents
- [原] Textual (Raw Experience) -> Latent hidden state
- [Pathway] N-Tok (raw, txt) → Lat (cross-session)  [src: 四件套, abs]
- [Utilization] memory trigger 监控 agent reasoning state 决定是否 invoke memory；memory weaver 以 agent current state 为 stimulus 构建 latent token sequence 参与 attention 计算  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL: GRPO⟩ + SFT  [src: abs, inferred]
- [机制] dynamic generative memory：memory trigger（门控）+ memory weaver（生成 latent tokens）；emergent human-like memory faculties（planning/procedural/working memory）无 explicit supervision  [src: abs]

---

### CLaRa: Bridging Retrieval and Generation with Continuous Latent Reasoning
- [原] Textual (Raw Experience) -> Latent-state
- [Pathway] N-Tok (raw, txt) → Lat (cross-session)  [src: 四件套, abs]
- [Utilization] embedding-based compression 将 documents 压缩为 continuous vectors → reranker and generator end-to-end 训练 → differentiable top-k 实现 joint optimization  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL: GRPO⟩（unified language modeling loss with differentiable top-k） [src: abs, inferred]
- [机制] SCP (key-preserving data synthesis via QA and paraphrase supervision) → continuous latent space 中 joint optimization of reranker and generator；text compression rate 达 16x  [src: abs]

---

### LatentMem: Customizing Latent Memory for Multi-Agent Systems
- [原] Textual (Raw Experience) -> Latent-state
- [Pathway] N-Tok (raw, txt) → Lat (cross-session)  [src: 四件套, abs]
- [Utilization] memory composer 以 retrieved experience + agent-specific contexts 为条件合成 compact latent memories；LMPO（Latent Memory Policy Optimization）通过 latent memories 传递 task-level optimization signals  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL: GRPO⟩（LMPO） [src: abs]
- [机制] experience bank（lightweight 存储 raw trajectories）+ memory composer（合成 role-aware compact latent memories）；LMPO 将 task-level signals 经 latent memories 传播到 composer  [src: abs]

---

### Self-Consolidation for Self-Evolving Agents
- [原] Textual (Raw Experience) -> Textual
- [原] Textual -> Learnable Prompt
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, contrastive reflection)  [src: 四件套, abs]
- [Pathway] N-Tok (refined, txt) → Lat (cross-session, learnable parameters)  [src: 四件套, abs]
- [Utilization] self-consolidation mechanism 将 non-parametric textual experience 蒸馏为 compact learnable parameters，直接 internalize 到 latent space；避免 context window exhaustion  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩ + SFT（consolidation distillation） [src: abs, inferred]
- [机制] contrastive reflection 显式总结 error-prone patterns + reusable insights → self-consolidation 将 textual experience 蒸馏为 compact learnable parameters（latent space 中的经验内部化） [src: abs]

---

### LatentEvolve: Self-Evolving Test-Time Scaling in Latent Space
- [原] Textual (Raw Experience) -> Latent-state -> Parameter
- [Pathway] N-Tok (raw, txt) → Lat (session-scoped, historical latent representations) → Lat (cross-session, refined latent predictor)  [src: 四件套, abs]
- [Pathway 修正] 原: -> Parameter（非 Policy/Evaluator 参数）→ 改: -> Lat (cross-session)，该 Parameter 是学习"如何从 context embedding 和 base latent 预测更好的 refined latent"的 composer 参数，属于 Latent carrier 体系  [src: abs, 四件套]
- [Utilization] daytime scaling：快速检索历史 latent representations 指导当前 reasoning；nighttime scaling：整合 past latent optimizations 类似人脑睡眠中的经验巩固  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩（fully unsupervised, gradient-free） [src: abs, inferred]
- [机制] CLS theory-inspired：daytime scaling（快速召回历史 latents）+ nighttime scaling（slow consolidation of past optimizations），fast-slow evolution cycle  [src: abs]

---

## Pathway P4: Tokenized → Evaluator (V-Par)（Evaluator Internalization）

Trajectories → RM / PRM / verifier / critic / judge。
经验固化为评估能力。

---

### AgentRM: Enhancing Agent Generalization with Reward Modeling
- [原] Textual (Raw Experience) -> Evaluator (Reward Model)
- [Pathway] N-Tok (raw, txt) → V-Par (Reward Model)  [src: 四件套, abs]
- [Utilization] 测试时 AgentRM 对候选轨迹打分（Best-of-N sampling + step-level beam search）指导 policy model 选择更好的 action；也可 boost fine-tuned policy model  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩（explicit / implicit reward modeling / LLM-as-a-judge） [src: abs]
- [机制] 三种 reward model 构建方式全面调研（explicit/implicit/LLM-as-a-judge）；AgentRM 展现 weak-to-strong generalization：LLaMA-3-70B 提升 12.6  [src: abs]

---

### Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations
- [原] Textual (Raw Experience) -> Evaluator (Process Reward Model)
- [Pathway] N-Tok (raw, txt) → V-Par (Process Reward Model)  [src: 四件套, abs]
- [Utilization] (a) Verification：reranking multiple LLM outputs；(b) Reinforcement Learning：step-by-step PPO 用 Math-Shepherd 提供 process rewards 训练 policy  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩（automatically constructed process-wise supervision data） [src: abs]
- [机制] 自动构建 process-wise supervision data 打破人工标注瓶颈；Mistral-7B 的 GSM8K 从 77.9%→84.1%，MATH 从 28.6%→33.0%  [src: abs]

---

### Free Process Rewards without Process Labels
- [原] Textual (Raw Experience) -> Evaluator (Process Reward Model)
- [Pathway] N-Tok (raw, txt) → V-Par (implicit PRM)  [src: 四件套, abs]
- [Utilization] implicit PRM 用于 Best-of-N 和 RLHF 中的 process reward 信号；也可通过 majority voting 进一步增强  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩（implicit PRM 通过 ORM training 获得，无需额外成本） [src: abs]
- [机制] implicit PRM 无需 step-level labels：仅需 response-level labels 训练 ORM，参数化 outcome reward 为 policy 与 reference model 的 log-likelihood ratio，即可获得等价 PRM  [src: abs]

---

### FreePRM: Training Process Reward Models Without Ground Truth Process Labels
- [原] Textual (Raw Experience) -> Evaluator (Process Reward Model)
- [Pathway] N-Tok (raw, txt) → V-Par (Process Reward Model)  [src: 四件套, abs]
- [Utilization] weakly supervised PRM 提供 step-level evaluation，用于 reasoning 过程的 fine-grained supervision  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩ + pseudo-labeling with Buffer Probability noise mitigation  [src: abs]
- [机制] FreePRM：基于 outcome correctness 生成 pseudo step-level labels → Buffer Probability 消除 pseudo labeling 噪声；ProcessBench F1=53.0%，超越 Math-Shepherd 训练的 fully supervised PRM +24.1%  [src: abs]

---

### Entropy-Regularized Process Reward Model (ER-PRM)
- [原] Textual (Raw Experience) -> Evaluator (Process Reward Model)
- [Pathway] N-Tok (raw, txt) → V-Par (Process Reward Model)  [src: 四件套, abs]
- [Utilization] ER-PRM 在 Best-of-N evaluation 和 RLHF 中提供 process rewards  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩ + KL-regularized MDP  [src: abs]
- [机制] KL-regularized MDP 平衡 policy optimization 与防止 policy 偏离初始分布；从初始 policy sampling 推导最优 reward model 的理论结果  [src: abs]

---

### Dyve: Thinking Fast and Slow for Dynamic Process Verification
- [原] Textual (Raw Experience) -> Evaluator (Verifier Model)
- [Pathway] N-Tok (raw, txt) → V-Par (Process Verifier)  [src: 四件套, abs]
- [Utilization] System 1（immediate token-level confirmation）+ System 2（comprehensive analysis）自适应应用于不同复杂度的步骤；在 Best-of-N 设置中提升性能  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩ + Monte Carlo estimation with LLM-based evaluation  [src: abs]
- [机制] Kahneman's Systems Theory 启发：fast thinking（System 1 token-level）+ slow thinking（System 2 comprehensive analysis）；step-wise consensus-filtered process supervision 从 noisy data 中提取高质量信号  [src: abs]

---

### SCAN: Self-Denoising Monte Carlo Annotation for Robust Process Reward Learning
- [原] Textual (Raw Experience) -> Evaluator (Process Reward Model)
- [Pathway] N-Tok (raw, txt) → V-Par (Process Reward Model)  [src: 四件套, abs]
- [Utilization] PRM 提供 fine-grained step-level evaluations 用于 complex reasoning（如数学推理）中的过程监督  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩ + self-denoising strategy + robust learning  [src: abs]
- [机制] MC estimation 合成数据噪声高（annotation models 同时 under/over-estimate step correctness）；SCAN 用 self-denoising strategy 使 1.5B 轻量模型也能产生高质量标注，F1 从 19.9→59.1  [src: abs]

---

### GM-PRM: A Generative Multimodal Process Reward Model
- [原] Token (Visual + Textual, Raw Experience) -> Evaluator (Process Reward Model)
- [Pathway] N-Tok (raw, vis+txt) → V-Par (Generative Multimodal PRM)  [src: 四件套, abs]
- [Utilization] Refined Best-of-N (Refined-BoN)：GM-PRM 不仅评分，还生成第一个错误步骤的 correction，引导 policy model 向更 promising reasoning trajectory  [src: abs]
- [Modality] [vis+txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩  [src: abs]
- [机制] 将 PRM 从 passive judge 转变为 active reasoning collaborator：输出 step intent/visual alignment/logical soundness 的 fine-grained analysis + corrected version of first erroneous step  [src: abs]

---

### SPARK: Stepwise Process-Aware Rewards for Reference-Free RL
- [原] Textual (Raw Experience) -> Evaluator (Process Reward Model)
- [Pathway] N-Tok (raw, txt) → V-Par (generative PRM with CoT verification)  [src: 四件套, abs]
- [Utilization] PRM-CoT 作为 RL training 的 reward model（mathematical reasoning），format constraints 防止 reward hacking  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩（synthetic training data from verifier outputs）→ PRM as reward signal in RL  [src: abs]
- [机制] 三阶段：generator 产生 diverse solutions + verifier 用 parallel scaling（self-consistency）和 sequential scaling（meta-critique）评估 → 合成数据训练 generative PRM → PRM-CoT 作为 RL reward；reference-free 超越 ground-truth 方法  [src: abs]

---

### SPARE: Single-Pass Annotation with Reference-Guided Evaluation
- [原] Textual (Raw Experience) -> Evaluator (Process Reward Model)
- [原] Textual (Raw Experience) -> Evaluator (ORPO)
- [Pathway] N-Tok (raw, txt) → V-Par (Process Reward Model)  [src: 四件套, abs]
- [Utilization] PRM 用于 ranking and aggregating multiple generations；fine-tuning models via offline RL for greedy decoding  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩  [src: abs]
- [机制] single-pass annotation framework：jointly align solution steps to reference solutions 并判断 accuracy with explicit reasoning；仅用 ~16% 训练样本即可达到 human-labeled baselines 的 OOD 泛化，比 MCTS 方法快 2.3x  [src: abs]

---

### From Outcomes to Processes: Guiding PRM Learning from ORM (SP-PRM)
- [原] Textual (Raw Experience) -> Evaluator (Process Reward Model)
- [Pathway] N-Tok (raw, txt) → V-Par (Process Reward Model)  [src: 四件套, abs]
- [Utilization] inference-time alignment：SP-PRM 在 RGS (reward-guided search) 中提供 process rewards；dialogue/summarization/reasoning 任务上 GPT-4 evaluation 提升 3.6%-10.3%  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩（dual-consistency framework：score consistency + preference consistency） [src: abs]
- [机制] 将 PRM 引入 reward-guided search：SP-PRM 满足 Score Consistency（partial vs complete response 评估一致）+ Preference Consistency（partial sequence 评估对齐人类偏好），无需 human annotation  [src: abs]

---

### Listwise Reward Estimation for Offline Preference-based RL (LiRE)
- [原] Textual (Raw Experience) -> Evaluator (Reward Model)
- [Pathway] N-Tok (raw, txt) → V-Par (Reward Model)  [src: 四件套, abs]
- [Utilization] learned reward model 用于 offline PbRL，评估 trajectories；second-order preference（relative strength of preference）增强 reward estimation  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {human}（preference feedback） [src: abs, inferred]
- [Method] ⟨SFT⟩  [src: abs]
- [机制] Listwise Reward Estimation：利用 Ranked List of Trajectories (RLT) 捕获 second-order preference，从 ternary feedback 高效构建  [src: abs]

---

### Regularizing Hidden States Enables Learning Generalizable Reward Model for LLMs
- [原] Textual (Raw Experience) -> Evaluator (Reward Model)
- [Pathway] N-Tok (raw, txt) → V-Par (Reward Model)  [src: 四件套, abs]
- [Utilization] generalized RM 用于 RLHF 中的 policy optimization；regularization 减轻 reward over-optimization  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {human}（human preference data） [src: abs, inferred]
- [Method] ⟨SFT⟩ + text-generation losses as regularization  [src: abs]
- [机制] 保留 base model's language model head + text-generation losses 保持 hidden states' text-generation capabilities，同时学习 reward head；提高 OOD 泛化和缓解 RLHF 中的 over-optimization  [src: abs]

---

### [新增] Reward-SQL: Boosting Text-to-SQL via Stepwise Reasoning and Process-Supervised Rewards
- [Pathway] N-Tok (raw, txt) → V-Par (Process Reward Model) → π-Par  [src: abs, 四件套]
- [Utilization] "cold start, then PRM supervision"：先训练模型用 Chain-of-CTEs 分解 SQL → 再用 PRM 作为 online training signal (GRPO) + PRM-guided inference (best-of-N sampling)  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩ + ⟨RL: GRPO⟩（PRM-guided） [src: abs]
- [机制] 系统探索如何将 PRM 有效融入 Text-to-SQL reasoning：四种 PRM integration 策略对比，GRPO + best-of-N 组合最优，BIRD dev set 68.9%  [src: abs]

---

### Graph-Reward-SQL: Execution-Free RL for Text-to-SQL
- [原] Textual (Raw Experience) -> Evaluator (Reward Model)
- [Pathway] N-Tok (raw, txt) → V-Par (Reward Model, GMNScore outcome + StepRTM stepwise)  [src: 四件套, abs]
- [Utilization] GMNScore 提供 outcome reward，StepRTM 提供 intermediate supervision over CTE subqueries；用于 RL-based Text-to-SQL 训练  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩  [src: abs]
- [机制] SQL graph representations 提供准确 reward signals 同时大幅降低 time cost 和 GPU memory；stepwise reward 鼓励 SQL 的 functional correctness 和 readability  [src: abs]

---

### SRR-Judge: Step-Level Rating and Refinement for Search-Integrated Reasoning
- [原] Textual (Raw Experience) -> Evaluator (step-level judge model)
- [Pathway] N-Tok (raw, txt) → V-Par (step-level judge)  [src: 四件套, abs]
- [Utilization] rate-and-refine workflow：SRR-Judge 提供 fine-grained guidance for search-integrated reasoning；SRR-annotated data 通过 iterative rejection sampling fine-tuning 增强 deep search capability  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩（iterative rejection sampling fine-tuning） [src: abs]
- [机制] 对 reasoning 和 search actions 做 step-level assessment，比 DeepSeek-V3.1 等更大模型更可靠；ratings 与 final answer correctness 强相关  [src: abs]

---

### Becoming Experienced Judges: Selective Test-Time Learning for Evaluators (LWE)
- [原] (空条目，基本信息仅有标题)
- [Pathway] N-Tok (refined, meta-prompt) → N-Tok (refined, meta-prompt)  [src: abs, inferred]
- [Pathway 说明] 该工作本质是 evaluator 在推理时通过 self-generated feedback 持续改进 evaluation meta-prompt（N-Tok → N-Tok 的自更新），不涉及 evaluator 参数更新。若视 evaluator 自身的 evaluation policy 为一种 Parametric 行为，则属于 evaluator utilization 的优化  [src: inferred]
- [Utilization] evolving meta-prompt 产生 sample-specific evaluation instructions；Selective LWE 仅在 self-inconsistent cases 上更新，计算效率更高  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] Learning While Evaluating (LWE)：evaluator 在 sequential testing 中通过 self-generated feedback 持续改进 meta-prompt；Selective LWE 只在 self-inconsistent cases 上更新  [src: abs]

---

## Pathway P5: Tokenized → Policy (π-Par)（Policy Internalization）

Trajectories → policy weights via SFT / RL。
经验固化为决策能力。

---

### FireAct: Toward Language Agent Fine-tuning
- [原] Policy Parameter -> Textual (Raw Experience) -> Policy Parameter
- [Pathway] π-Par (teacher) → N-Tok (raw, txt) → π-Par (student)  [src: 四件套, abs]
- [Utilization] fine-tuned LM 直接作为 agent 执行 task-solving，替代 few-shot prompting with off-the-shelf LMs  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {teacher}（GPT-4 生成 trajectories） [src: abs]
- [Method] ⟨SFT⟩  [src: abs]
- [机制] 用 GPT-4 生成的 agent trajectories 对较小的 LM（如 Llama2-7B）做 SFT；multi-task + multi-prompting-method 的多样化 fine-tuning data 进一步提升效果；HotpotQA 提升 77%  [src: abs]

---

### Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training
- [原] Policy Parameter -> Textual (Raw Experience) -> Policy Parameter
- [Pathway] π-Par → N-Tok (raw, txt) → π-Par  [src: 四件套, abs]
- [Utilization] fine-tuned policy 在后续交互中能 timely recover from errors；MCTS 构造的 correction data 持续改进模型的 error correction 能力  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩（iterative self-training） [src: abs]
- [机制] MCTS 构造从错误轨迹恢复正确轨迹的训练数据；model-guided critique construction：actor 识别失败轨迹中第一个错误步骤，splice 到相邻正确路径；迭代 refine error correction 和 dataset construction  [src: abs]

---

### Agent0: Unleashing Self-Evolving Agents from Zero Data
- [原] Policy Parameter -> Textual (Raw Experience) -> Policy Parameter
- [Pathway] π-Par → N-Tok (raw, txt) → π-Par  [src: 四件套, abs]
- [Utilization] 更新后的 executor policy 直接作为下一轮 rollout 的 policy；curriculum agent 根据 executor 的能力提升生成更难任务  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL: GRPO⟩（curriculum self-play） [src: abs, inferred]
- [机制] symbiotic competition：curriculum agent 提出 increasingly challenging frontier tasks + executor agent 学习解决，tool integration 增强 executor 能力反哺 curriculum 生成更复杂的 tool-aware tasks  [src: abs]

---

### AgentEvolver: Towards Efficient Self-Evolving Agent System
- [原] Policy Parameter -> Textual (Raw Experience) -> Policy Parameter
- [Pathway] π-Par → N-Tok (raw, txt) → π-Par  [src: 四件套, abs]
- [Utilization] 更新后的 policy 反哺后续迭代：self-questioning 生成新任务 → self-navigating 高效探索 → self-attributing 精细 reward 归因 → GRPO 优化 policy  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL: GRPO⟩  [src: abs]
- [机制] 三机制协同：self-questioning（curiosity-driven task generation）、self-navigating（experience reuse + hybrid policy guidance 提高探索效率）、self-attributing（基于贡献度的 differentiated rewards 提高样本效率） [src: abs]

---

### Beyond Human Data: Scaling Self-Training for Problem-Solving (ReST^EM)
- [原] Policy Parameter -> Textual (Raw Experience) -> Policy Parameter
- [Pathway] π-Par → N-Tok (raw, txt) → π-Par  [src: 四件套, abs]
- [Utilization] fine-tuned model 在下一轮生成更高质量的样本，形成 self-training loop  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩（ReST^EM：EM-based self-training with binary feedback filtering） [src: abs]
- [机制] ReST^EM：(1) generate samples from model, (2) filter with binary feedback (验证器), (3) fine-tune on filtered samples, (4) repeat；在 MATH 和 APPS 上显著超越仅用 human data 的 SFT  [src: abs]

---

### Self-Instruct: Aligning Language Models with Self-Generated Instructions
- [原] Policy Parameter -> Token (Raw Experience) -> Policy Parameter
- [Pathway] π-Par → N-Tok (raw, txt) → π-Par  [src: 四件套, abs]
- [Utilization] SFT 后的 model 直接作为 instruction-following LM 部署；bootstrapping 方式减少对人类标注的依赖  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩  [src: abs]
- [机制] pipeline: generate instructions/input/output from LLM → filter invalid/similar ones → fine-tune original model；GPT3 在 Super-NaturalInstructions 上提升 33%  [src: abs]

---

### Self-Questioning Language Models (SQLM)
- [原] Policy Parameter -> Token (Raw Experience) -> Policy Parameter
- [Pathway] π-Par (proposer) → N-Tok (raw, txt, question) → π-Par (solver)  [src: 四件套, abs]
- [Utilization] solver 回答 proposer 生成的问题；proposer 学习生成难度适中的问题，solver 通过 RL 学习解决  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL⟩（asymmetric self-play with majority voting as proxy reward） [src: abs]
- [机制] asymmetric self-play framework：proposer（奖励=not too easy/difficult）+ solver（奖励=majority voting），无需外部数据或 ground-truth answers  [src: abs]

---

### [新增] One Model, All Roles: Multi-Turn, Multi-Agent Self-Play RL for Conversational Social Intelligence (OMAR)
- [Pathway] π-Par → N-Tok (raw, txt, multi-turn conversation) → π-Par  [src: abs, 四件套]
- [Utilization] single model role-plays all participants in conversation simultaneously；hierarchical advantage estimation（turn-level + token-level）确保长对话训练稳定性；learned policy 展现 emergent social intelligence（empathy / persuasion / compromise seeking） [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL⟩（multi-turn multi-agent self-play with hierarchical advantage estimation） [src: abs]
- [机制] 单一模型同时扮演对话中所有角色，从动态社交互动中学习长期目标和复杂社交规范；emergent fine-grained social intelligence 无需 human supervision  [src: abs]

---

### START: Self-taught Reasoner with Tools
- [原] Policy Parameter -> Token (Raw Experience) -> Policy Parameter
- [Pathway] π-Par → N-Tok (raw, txt, tool-augmented CoT) → π-Par  [src: 四件套, abs]
- [Utilization] fine-tuned model 作为 tool-integrated long CoT reasoner；推理时执行 code 实现 complex computations/self-checking/self-debugging  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩（Hint-RFT: Hint-infer + Rejection Sampling Fine-Tuning） [src: abs]
- [机制] Hint-infer：在 LRM 推理过程中插入人工设计的 hints（如 "Wait, maybe using Python here is a good idea."）激发 tool use；Hint-RFT 对 tool-invoked reasoning trajectories 做 scoring/filtering/modifying 后 fine-tune  [src: abs]

---

### Beyond Policy Optimization: A Data Curation Flywheel (BPO)
- [原] Policy Parameter -> Textual (Raw Experience) -> Policy Parameter
- [Pathway] π-Par → N-Tok (raw, txt) → π-Par  [src: 四件套, abs]
- [Utilization] refined policy 在下轮迭代中生成更高质量 trajectories；self-improving data flywheel：bootstrapping → extrapolation → refinement  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩ + Curriculum Learning  [src: abs]
- [机制] three-stage：bootstrapping（planning quaternions with long-short CoT fusion）→ extrapolation（complexity-stratified curriculum learning 到 OOD tasks）→ refinement（reward-gated rejection sampling 筛选经验） [src: abs]

---

### Entropy-Based Adaptive Weighting for Self-Training (EAST)
- [原] Policy Parameter -> Textual (Raw Experience) -> Policy Parameter
- [Pathway] π-Par → N-Tok (raw, txt) → π-Par  [src: 四件套, abs]
- [Utilization] self-training：model 生成 reasoning paths → EAST 按 uncertainty 加权 → fine-tune model  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩  [src: abs]
- [机制] EAST：用 tunable parameter 控制 weighting sharpness，对 model 更 uncertain 的数据分配更高权重，引导 model 关注更 informative 和 challenging 的样本  [src: abs]

---

### Improving Retrospective Language Agents via Joint Policy Gradient Optimization (RetroAct)
- [原] Policy Parameter -> Token (Raw Experience) -> Policy Parameter
- [原] Policy Parameter -> Token (Reflection) -> Policy Parameter
- [Pathway] π-Par → N-Tok (raw, txt) → π-Par  [src: 四件套, abs]
- [Pathway] π-Par → N-Tok (refined, reflection) → π-Par  [src: 四件套, abs]
- [Utilization] optimized policy 同时具备 task-planning 和 self-reflective evolution 能力；fine-tuned agents 能持续学习和进化  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩ + ⟨RL⟩（off-policy joint policy gradient optimization with imitation learning regularization） [src: abs]
- [机制] two-stage joint optimization：imitation learning + RL；off-policy joint policy gradient optimization with imitation learning regularization 提高 data efficiency 和 training stability  [src: abs]

---

### The Path of Self-Evolving LLMs: Data-Efficient Learning via Intrinsic Feedback
- [原] Policy Parameter -> Token (Raw Experience) -> Policy Parameter
- [Pathway] π-Par → N-Tok (raw, txt, self-proposed task) → π-Par  [src: 四件套, abs]
- [Utilization] self-aware difficulty prediction 优先选择 challenging yet solvable tasks；self-aware limit breaking 在超出 capability boundary 时主动请求外部数据  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩  [src: abs]
- [机制] self-aware RL：模型学习评估 task difficulty relative to own abilities（self-aware difficulty prediction）和识别 capability boundary（self-aware limit breaking）；53.8% 相对提升，仅需 <1.2% 额外数据  [src: abs]

---

### ATLaS: Agent Tuning via Learning Critical Steps
- [原] Textual (Raw Experience) -> Policy Parameter
- [Pathway] N-Tok (raw, txt) → π-Par  [src: 四件套, abs]
- [Utilization] fine-tuned LLM 直接作为 generalist agent 在多种环境中交互；仅需 30% 的关键步骤即可超越全量 SFT  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {teacher}（expert trajectories） [src: abs]
- [Method] ⟨SFT⟩（仅对 critical steps） [src: abs]
- [机制] 识别 expert trajectories 中的 critical steps（planning / complex reasoning / strategic decision-making），仅对这些步骤 SFT；减少 expert bias 和 overfitting，提升跨环境泛化  [src: abs]

---

### [新增] Retrieval-Augmented LLM Agents: Learning to Learn from Experience
- [Pathway] N-Tok (raw, txt, retrieved trajectories) → π-Par  [src: abs, 四件套]
- [Utilization] LoRA-based SFT 使 agent 学习如何有效利用 retrieved trajectories in-context；experience retrieval 集成到 fine-tuning 流程中；显著提升 unseen tasks 泛化  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩（LoRA）+ experience retrieval integration  [src: abs]
- [机制] 系统研究如何训练 retrieval-augmented LLM agents：SFT recipe + experience retrieval design choices（storage / querying / trajectory selection）+ 将 experience retrieval 集成到 fine-tuning 流程  [src: abs]

---

### [新增] Watch Every Step! LLM Agent Learning via Iterative Step-Level Process Refinement (IPR)
- [Pathway] N-Tok (raw, txt) → π-Par  [src: abs, 四件套]
- [Utilization] Monte Carlo method 估计 step-level rewards → agent 沿 expert trajectory 探索生成新 actions → 与 expert 对应步骤比较产生 contrastive action pairs → 作为训练数据 SFT agent  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self} + {teacher}（expert trajectory as reference） [src: abs]
- [Method] ⟨SFT⟩（iterative step-level process refinement with contrastive action pairs） [src: abs]
- [机制] IPR 提供 detailed step-by-step guidance 增强 agent training；区别于 outcome reward only 的方法，在每步与 expert 比较产生 contrastive signals  [src: abs]

---

### DeepAnalyze: Agentic LLMs for Autonomous Data Science
- [原] Textual (Raw Experience) -> Policy Parameter
- [Pathway] N-Tok (raw, txt) → π-Par  [src: 四件套, abs]
- [Utilization] fine-tuned 8B model 作为 data science agent 端到端执行数据任务（QA / specialized analytical tasks / open-ended data research） [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}（data-grounded trajectory synthesis framework） [src: abs]
- [Method] ⟨SFT⟩ + ⟨RL: GRPO⟩  [src: abs]
- [机制] curriculum-based agentic training paradigm 模拟人类数据科学家的学习轨迹；data-grounded trajectory synthesis 构建高质量训练数据  [src: abs]

---

### InfiGUIAgent: A Multimodal Generalist GUI Agent
- [原] Token(Visual + Textual, Raw Experience) -> Policy Parameter
- [Pathway] N-Tok (raw, GUI) → π-Par  [src: 四件套, abs]
- [Utilization] fine-tuned MLLM 作为 GUI agent 在 GUI 环境中执行 multi-step reasoning 和 action  [src: abs]
- [Modality] [GUI]  [src: abs]
- [Source] {self}（synthesized data） [src: abs]
- [Method] ⟨SFT⟩（two-stage：Stage 1 GUI understanding/grounding, Stage 2 hierarchical reasoning + expectation-reflection reasoning） [src: abs]
- [机制] two-stage SFT pipeline：Stage 1 增强 GUI understanding 和 grounding，Stage 2 用 synthesized data 整合 hierarchical reasoning 和 expectation-reflection reasoning  [src: abs]

---

### [新增] TongUI: Internet-Scale Trajectories from Multimodal Web Tutorials for Generalized GUI Agents
- [Pathway] π-Par → N-Tok (raw, GUI, from web tutorials) → π-Par (TongUI agent, via SFT)  [src: abs, 四件套]
- [Utilization] GUI-Net dataset（143K trajectories, 5 OS, 200+ apps）用于 fine-tune Qwen2.5-VL-3B/7B → TongUI agent；grounding 和 navigation benchmarks 上提升约 10%  [src: abs]
- [Modality] [GUI]  [src: abs]
- [Source] {teacher}（online GUI tutorials: videos + articles） [src: abs]
- [Method] ⟨SFT⟩  [src: abs]
- [机制] 从在线 GUI tutorials（视频和文章）爬取和处理为 agent trajectory data 解决 GUI agent 训练数据稀缺问题  [src: abs]

---

### [新增] UI-TARS-2 Technical Report: Advancing GUI Agent with Multi-Turn Reinforcement Learning
- [Pathway] π-Par → N-Tok (raw, GUI) → π-Par  [src: abs, 四件套]
- [Utilization] data flywheel for scalable data generation + stabilized multi-turn RL framework + hybrid GUI environment（file systems + terminals）+ unified sandbox for large-scale rollouts  [src: abs]
- [Modality] [GUI]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL⟩（multi-turn RL with stabilized training）+ ⟨SFT⟩  [src: abs]
- [机制] systematic training methodology：data flywheel → stabilized multi-turn RL（解决训练不稳定）→ hybrid GUI environment → unified sandbox；OSWorld 47.5, AndroidWorld 73.3  [src: abs]

---

### GUI-ReWalk: Massive Data Generation for GUI Agent
- [原] Policy Parameter -> Token (Raw Experience)
- [Pathway] π-Par → N-Tok (raw, GUI)  [src: 四件套, abs]
- [Pathway 修正] 原标注仅为单向（Policy Parameter -> Token），未形成闭环。该工作是数据合成框架，产出轨迹用于下游训练（N-Tok → π-Par）。完整路径：π-Par (base VLM) → N-Tok (raw, GUI) → π-Par (downstream agent)。  [src: abs, inferred]
- [Utilization] GUI-ReWalk 合成的 GUI trajectories 数据集用于训练 Qwen2.5-VL-7B 等下游 GUI agent model（SFT） [src: abs]
- [Modality] [GUI]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩（数据合成框架，无参数更新）；下游使用 ⟨SFT⟩  [src: abs, inferred]
- [机制] stochastic exploration（模拟人类 trial-and-error）+ reasoning-guided phase（inferred goals 驱动 coherent interactions）+ multi-stride task generation（长 horizon 跨应用） [src: abs]

---

### OS-Genesis: Automating GUI Agent Trajectory Construction
- [原] Policy Parameter -> Token (Raw Experience, Visual + Textual)
- [Pathway] π-Par → N-Tok (raw, GUI)  [src: 四件套, abs]
- [Pathway 修正说明] 与 GUI-ReWalk 类似，是数据合成框架。合成的轨迹用于下游训练，完整闭环：π-Par (VLM) → N-Tok (raw, GUI) → π-Par (trained agent)。  [src: abs, inferred]
- [Utilization] 生成的 GUI trajectories 用于训练 GUI agents，显著提升在线 benchmark 表现  [src: abs]
- [Modality] [GUI]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩（reverse task synthesis + trajectory reward model） [src: abs]
- [机制] reverse task synthesis：agent 先感知环境进行 step-wise interactions → retrospectively derive high-quality tasks；trajectory reward model 确保轨迹质量  [src: abs]

---

### OmegaUse: Building a General-Purpose GUI Agent
- [原] Token (Raw Experience, Visual + Textual) -> Policy Parameter
- [Pathway] N-Tok (raw, GUI) → π-Par  [src: 四件套, abs]
- [Utilization] fine-tuned MoE model 作为 general-purpose GUI agent 在 mobile 和 desktop 平台自主执行任务  [src: abs]
- [Modality] [GUI]  [src: abs]
- [Source] {self}（automated synthesis + curated open-source datasets） [src: abs]
- [Method] ⟨SFT⟩ + ⟨RL: GRPO⟩  [src: abs]
- [机制] decoupled training：SFT（建立基本交互语法）→ GRPO（改善 spatial grounding 和 sequential planning）；data-construction pipeline 结合 bottom-up autonomous exploration 和 top-down taxonomy-guided generation  [src: abs]

---

### MAI-UI Technical Report: Real-World Centric Foundation GUI Agents
- [原] Token(Visual + Textual, Raw Experience) -> Policy Parameter
- [Pathway] N-Tok (raw, GUI) → π-Par  [src: 四件套, abs]
- [Utilization] foundation GUI agents（2B/8B/32B/235B）部署在真实设备上；native device-cloud collaboration system 根据 task state 路由执行  [src: abs]
- [Modality] [GUI]  [src: abs]
- [Source] {self}（self-evolving data pipeline） [src: abs]
- [Method] ⟨SFT⟩ + ⟨RL: GRPO⟩（online RL with advanced optimizations） [src: abs]
- [机制] self-evolving data pipeline（扩展到 user interaction + MCP tool calls）+ online RL framework（scaling parallel environments 32→512 提升 +5.2 points） [src: abs]

---

### Act Wisely: Cultivating Meta-Cognitive Tool Use (HDPO / Metis)
- [原] Token (Raw Experience, Visual + Textual) -> Policy Parameter
- [Pathway] N-Tok (raw, vis+txt) → π-Par  [src: 四件套, abs]
- [Utilization] Metis model 在推理时自我仲裁 internal knowledge vs external tool use，减少盲目 tool invocation  [src: abs]
- [Modality] [vis+txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL⟩（HDPO：decoupled accuracy + efficiency channels） [src: abs, inferred]
- [机制] HDPO 将 tool efficiency 从 competing scalar objective 重构为 strictly conditional objective：accuracy channel（maximize task correctness）+ efficiency channel（仅在 accurate trajectories 内 enforce execution economy） [src: abs]

---

### E^2CL: Exploration-based Error Correction Learning for Embodied Agents
- [原] Textual (Raw Experience) -> Policy Parameter
- [Pathway] N-Tok (raw, embodied) → π-Par  [src: 四件套, abs]
- [Utilization] fine-tuned agent 在 embodied 环境中自主探索并从 exploration-induced errors 和 environmental feedback 中学习 self-correction  [src: abs]
- [Modality] [embodied]  [src: abs]
- [Source] {self} + {teacher}（teacher-guided exploration） [src: abs]
- [Method] ⟨SFT⟩  [src: abs]
- [机制] teacher-guided + teacher-free explorations 收集 environmental feedback；agent 学习提供 feedback 和 self-correct，增强对目标环境的适应性  [src: abs]

---

### Learning From Failure: Integrating Negative Examples when Fine-tuning LLMs as Agents
- [原] Token (Raw Experience) -> Policy Parameter
- [Pathway] N-Tok (raw, txt) → π-Par  [src: 四件套, abs]
- [Utilization] fine-tuned model 直接作为 agent 执行任务，包括 mathematical reasoning / multi-hop QA / strategic QA  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}（包含 failed trajectories） [src: abs]
- [Method] ⟨SFT⟩（正负轨迹都用，加 prefix/suffix 指示成功/失败） [src: abs]
- [机制] 首次系统证明 negative trajectories 的价值：加 prefix/suffix 告诉模型是否生成 successful trajectory，提供 valuable information 和 errors 之间的更好 trade-off  [src: abs]

---

### PROPA: Toward Process-level Optimization in Visual Reasoning via RL
- [原] Token (Raw Experience, Visual + Textual) -> Policy Parameter
- [原] Token (Raw Experience, Visual + Textual) -> Evaluator (Reward Model)
- [Pathway] N-Tok (raw, vis+txt) → π-Par  [src: 四件套, abs]
- [Pathway] N-Tok (raw, vis+txt) → V-Par (Process Reward Model)  [src: 四件套, abs]
- [Utilization] policy model 通过 MCTS+GRPO 联合优化获得 process-level reasoning 能力；PRM 在 inference-time search 中引导 policy  [src: abs]
- [Modality] [vis+txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL: GRPO⟩ + ⟨SFT⟩（interleaved） [src: abs]
- [机制] MCTS 生成 dense process-level rewards 无需 human annotations；interleave GRPO updates with SFT 克服 cold-start 问题；PRM 训练对齐 test-time search 信号  [src: abs]

---

### Reflective Planning: Vision-Language Models for Multi-Stage Long-Horizon Robotic Manipulation
- [原] Token(Visual + Textual, Raw Experience) -> Policy Parameter
- [Pathway] N-Tok (raw, embodied) → π-Par（但实现方式为 test-time computation + reflection，需核实是否真的更新参数） [src: abs, inferred]
- [Utilization] test-time computation framework：iteratively improve pretrained VLM with reflection mechanism；generative model 想象 future world states 指导 action selection  [src: abs]
- [Modality] [embodied]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] UNCLEAR (abstract-only) —— 描述为 "test-time computation framework" 和 "iteratively improves a pretrained VLM"，可能不涉及参数更新  [src: abs]
- [机制] reflection mechanism：generative model 想象 future world states → guide action selection → reflect on potential suboptimalities → refine reasoning；显著超越 MCTS  [src: abs]

---

### EVOLVE-VLA: Test-Time Training from Environment Feedback
- [原] Token (Visual + Textual, Raw Experience) -> Policy Parameter
- [Pathway] N-Tok (raw, embodied) → π-Par  [src: 四件套, abs]
- [Utilization] test-time training：VLA 在部署中通过 environment interaction 持续适应；updated policy 直接用于 robot manipulation  [src: abs]
- [Modality] [embodied]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL: GRPO⟩  [src: abs]
- [机制] learned progress estimator 提供 dense feedback 替代 oracle reward；accumulative progress estimation（平滑 noisy estimates）+ progressive horizon extension（渐进策略演化）；1-shot 提升 +22.0%，cross-task generalization 20.8%  [src: abs]

---

### LongNav-R1: Horizon-Adaptive Multi-Turn RL for Long-Horizon VLA Navigation
- [原] （标题存在但无独立标注行）
- [Pathway] N-Tok (raw, embodied) → π-Par  [src: 四件套, abs]
- [Utilization] fine-tuned VLA policy 在 long-horizon navigation 中执行 multi-turn reasoning；zero-shot 泛化到 real-world settings  [src: abs]
- [Modality] [embodied]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL⟩（multi-turn RL with Horizon-Adaptive Policy Optimization） [src: abs]
- [机制] 将 navigation 重构为 continuous multi-turn conversation between VLA policy and embodied environment；Horizon-Adaptive Policy Optimization 考虑 varying horizon lengths 做 accurate temporal credit assignment  [src: abs]

---

### ReTool: Reinforcement Learning for Strategic Tool Use in LLMs
- [原] Textual (Raw Experience) -> Policy Parameter
- [Pathway] N-Tok (raw, txt) → π-Par  [src: 四件套, abs]
- [Utilization] fine-tuned policy 在推理时 dynamic interleaving real-time code execution within natural language reasoning；模型自主发现最优 tool invocation patterns  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩（cold-start）+ ⟨RL⟩（outcome feedback） [src: abs]
- [机制] synthetic cold-start data 生成 code-augmented long-form reasoning traces → SFT → RL 用 task outcomes 作为 reward 迭代 refine tool use strategy；涌现 code self-correction "aha moment"  [src: abs]

---

### ToolRL: Reward is All Tool Learning Needs
- [原] Textual (Raw Experience) -> Policy Parameter
- [Pathway] N-Tok (raw, txt) → V-Par (rule-based evaluator) → π-Par  [src: 四件套, abs]
- [Pathway 修正] 原标注: Textural -> Evaluator -> Policy Parameter, 但说明 Evaluator 是 Rule-based Evaluator。Rule-based evaluator 不是 Parametric carrier，因此中间步骤是 rule-based filtering，不是 V-Par。但最终的 GRPO 训练仍构成 N-Tok → π-Par。建议将 rule-based 阶段标注为 ⟨LLM-extract⟩ filtering，不作为独立 pathway 步骤。  [src: abs, 四件套]
- [Utilization] GRPO-trained policy 用于 tool selection and application  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL: GRPO⟩  [src: abs]
- [机制] 系统研究 tool use RL 的 reward design：types/scales/granularity/temporal dynamics；principled reward design tailored for tool use，GRPO 训练，17% 超越 base model，15% 超越 SFT  [src: abs]

---

### ToolSample: Dual Dynamic Sampling Methods with Curriculum Learning
- [原] Textual (Raw Experience) -> Policy Parameter
- [Pathway] N-Tok (raw, txt) → π-Par  [src: 四件套, abs]
- [Utilization] RL-trained policy 用于 tool-learning 任务；DSCL 方法提升训练效率  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL⟩（DSCL: Dynamic Sampling with Curriculum Learning） [src: abs]
- [机制] Reward-Based Dynamic Sampling（用 multi-dimensional reward statistics mean/variance 优先处理有价值数据）+ Task-Based Dynamic Curriculum Learning（自适应聚焦 less-mastered sub-tasks） [src: abs]

---

### SPA-RL: Reinforcing LLM Agents via Stepwise Progress Attribution
- [原] Textual (Raw Experience) -> Policy Parameter
- [Pathway] N-Tok (raw, txt) → π-Par  [src: 四件套, abs]
- [Utilization] RL-trained agent 在 ALFWorld / WebShop / VirtualHome 中执行多步交互任务；stepwise progress rewards 提供更有效的中间监督  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL: PPO⟩（Stepwise Progress Attribution reward redistribution） [src: abs]
- [机制] SPA：将 final reward 分解为 stepwise contributions，每个 contribution 反映该步对任务完成的 incremental progress；progress estimator 积累 stepwise contributions 以匹配 task completion  [src: abs]

---

### PRL: Process Reward Learning Improves LLMs' Reasoning Ability
- [原] Textual (Raw Experience) -> Policy Parameter
- [Pathway] N-Tok (raw, txt) → π-Par  [src: 四件套, abs]
- [Utilization] PRL-trained policy 在推理时表现更好的 pass@n 和 pass@n 边界扩展能力  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL⟩（entropy regularized RL with process reward decomposition） [src: abs]
- [机制] 将 entropy regularized RL objective 分解为 intermediate steps，从 outcome reward 转为 process supervision signals；理论推导保证 PRL 等价于 reward maximization + KL-divergence penalty  [src: abs]

---

### SkillRL: Evolving Agents via Recursive Skill-Augmented RL
- [原] Textual (Raw Experience) -> Textual (Skill) -> Policy Parameter
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, skill) → π-Par  [src: 四件套, abs]
- [Utilization] SkillBank 中的 skills 在 RL 过程中与 policy 共同进化；adaptive retrieval 提供 general + task-specific heuristics  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩ + ⟨SFT⟩ + ⟨RL: GRPO⟩  [src: abs, inferred]
- [机制] experience-based distillation 构建 hierarchical SkillBank → adaptive retrieval → recursive evolution：skill library 与 policy 在 RL 中 co-evolve；ALFWorld/WebShop 超越强 baselines 15.3%  [src: abs]

---

### MobileGUI-RL: Advancing Mobile GUI Agent through RL in Online Environment
- [原] Policy Parameter -> Token (Raw Experience, Visual + Textual) -> Policy Parameter
- [Pathway] π-Par → N-Tok (raw, GUI) → π-Par  [src: 四件套, abs]
- [Utilization] updated policy 在 online mobile GUI 环境中执行点击/滑动/输入等操作  [src: abs]
- [Modality] [GUI]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL: GRPO⟩（trajectory-aware advantages + composite rewards） [src: abs]
- [机制] online RL（非 offline pre-collected trajectories）：self-exploration and filtering 合成 learnable tasks 的 curriculum + GRPO adapted to GUI navigation with trajectory-aware advantages  [src: abs]

---

### [新增] Weak-for-Strong: Training Weak Meta-Agent to Harness Strong Executors (W4S)
- [Pathway] N-Tok (raw, txt) → π-Par (meta-agent, 7B)  [src: abs, 四件套]
- [Utilization] trained weak meta-agent 在推理时 design and optimize workflows for harnessing stronger models（如 GPT-4o）；RLAO (RL for agentic workflow optimization) 训练 meta-agent 通过环境交互学习设计越来越 effective 的 workflows  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL⟩（RLAO: RL for agentic workflow optimization, multi-turn MDP） [src: abs]
- [机制] 将 workflow design 形式化为 multi-turn MDP；7B meta-agent 仅需 1 GPU hour 训练即可超越 strongest baseline 2.9%~24.6%；strong generalization across seen and unseen tasks  [src: abs]

---

### Self-Training LLMs for Improved Visual Program Synthesis With Visual Reinforcement
- [原] Policy Parameter -> Token (Raw Experience, Visual + Textual) -> Policy Parameter
- [Pathway] π-Par → N-Tok (raw, vis+txt) → π-Par  [src: 四件套, abs]
- [Utilization] self-trained LLM 作为 visual program synthesis 的 policy，生成用于 compositional computer vision tasks 的程序  [src: abs]
- [Modality] [vis+txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL⟩（reinforced self-training with coarse reward from vision-language task annotations） [src: abs]
- [机制] 利用 vision-language task 的现有 annotations 构造 coarse reward signal → LLM as policy → reinforced self-training 改善 visual program synthesis  [src: abs]

---

### Agent Learning via Early Experience
- [原] Policy Parameter -> Textual (Raw Experience) -> Policy Parameter
- [原] Policy Parameter -> Textual (Raw Experience + Reflection) -> Policy Parameter
- [Pathway] π-Par → N-Tok (raw, txt) → π-Par  [src: 四件套, abs]
- [Pathway] π-Par → N-Tok (refined, reflection, txt) → π-Par  [src: 四件套, abs]
- [Utilization] (a) Implicit world modeling：collected states 用于 grounding policy in environment dynamics；(b) Self-reflection：agent 从 suboptimal actions 中学习改进 reasoning 和 decision-making  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩  [src: abs]
- [机制] "early experience" 范式：agent 自身 actions 产生的 interaction data，future states 作为 supervision 无需 reward signals；成为 imitation learning 和 fully experience-driven agents 之间的实用桥梁  [src: abs]

---

### Internalizing Agency from Reflective Experience (LEAFE)
- [原] Policy Parameter -> Token (Raw Experience, Reflection) -> Policy Parameter
- [Pathway] π-Par → N-Tok (raw, txt) → N-Tok (refined, reflection) → π-Par  [src: 四件套, abs]
- [Utilization] LEAFE-trained policy 在后续交互中能更有效地从错误中恢复；Pass@1 和 Pass@k 均超越 outcome-driven baselines (GRPO) 和 Early Experience  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩（distill experience-guided corrections） [src: abs]
- [机制] exploration 阶段：agent 将 environment feedback 总结为 actionable experience → backtrack 到 earlier decision points → explore alternative branches → distill corrections into model via SFT  [src: abs]

---

### [新增] On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes (GKD)
- [Pathway] π-Par (teacher) → N-Tok (raw, txt, self-generated sequences) → π-Par (student)  [src: abs, 四件套]
- [Utilization] student 在自生成输出序列上训练，teacher 提供 feedback；flexible alternative loss functions；seamless integration of distillation with RL fine-tuning (RLHF)  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self} + {teacher}  [src: abs]
- [Method] ⟨SFT⟩（Generalized Knowledge Distillation: on-policy self-generated outputs + teacher feedback） [src: abs]
- [机制] 解决 auto-regressive sequence models 的 distribution mismatch（训练时看到的 vs 推理时生成的）；student 在自生成序列上训练，teacher 提供 feedback  [src: abs]

---

### Distilling LLM Agent into Small Models with Retrieval and Code Tools
- [原] Policy Parameter -> Textual (Raw Experience) -> Policy Parameter
- [Pathway] π-Par (teacher LLM agent) → N-Tok (raw, txt) → π-Par (small LM)  [src: 四件套, abs]
- [Utilization] distilled small LM（0.5B-3B）作为 tool-using agent，在推理时使用 retrieval 和 code tools 执行任务  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {teacher}（LLM agent trajectories） [src: abs]
- [Method] ⟨SFT⟩（first-thought prefix prompting + self-consistent action generation） [src: abs]
- [机制] Agent Distillation：transfer full task-solving behavior（不仅是 reasoning capability）；first-thought prefix 提升 teacher trajectory 质量，self-consistent action generation 提升 test-time robustness  [src: abs]

---

### Agentic Reasoning and Tool Integration for LLMs via RL (ARTIST)
- [原] Textual -> Policy Parameter
- [Pathway] N-Tok (raw, txt) → π-Par  [src: 四件套, abs]
- [Utilization] fine-tuned policy 在 multi-turn reasoning chains 中 autonomously decide when/how/which tools to invoke  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL⟩（outcome-based RL, no step-level supervision） [src: abs]
- [机制] ARTIST 将 agentic reasoning / RL / tool integration 紧密结合；outcome-based RL 学习 robust tool use 和 environment interaction 策略，无需 step-level supervision  [src: abs]

---

### [新增] MemFactory: Unified Inference & Training Framework for Agent Memory
- [Pathway] N-Tok (raw, txt) → π-Par (memory management policy, via GRPO)  [src: abs, 四件套]
- [Utilization] GRPO 优化的 memory management policy 控制 memory 生命周期（extraction / updating / retrieval）；plug-and-play "Lego-like" architecture 支持 custom memory agents  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL: GRPO⟩（multi-dimensional environmental rewards 驱动 memory management policy 优化） [src: abs]
- [机制] 首个统一 memory-augmented agent 训练推理框架；GRPO fine-tune internal memory management policies；跨 Memory-R1 / RMM / MemAgent 等范式  [src: abs]
- [Pathway 说明] MemFactory 是 infrastructure/framework 而非 transformation 方法本身，但其 GRPO 训练的 memory management policy 构成 N-Tok → π-Par 的 experience-driven 训练。  [src: inferred]

---

### Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management (AgeMem)
- [原] Textual -> Policy Parameter
- [Pathway] N-Tok (raw, txt) → π-Par  [src: 四件套, abs]
- [Utilization] AgeMem policy 自主决定 when/what to store/retrieve/update/summarize/discard；memory operations 作为 tool-based actions 直接集成到 agent's policy  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL: step-wise GRPO⟩（three-stage progressive RL） [src: abs]
- [机制] 将 LTM 和 STM 管理统一为 tool-based actions；three-stage progressive RL + step-wise GRPO 解决 memory operations 引起的 sparse/discontinuous rewards  [src: abs]

---

### Learning from Trials and Errors: Reflective Test-Time Planning for Embodied LLMs
- [原] Token(Visual + Textual, Raw Experience) -> Textual (Reflection) -> Policy Parameter
- [Pathway] N-Tok (raw, embodied) → N-Tok (refined, reflection) → π-Par  [src: 四件套, abs]
- [Utilization] reflection-in-action（test-time scaling 生成并评分多个候选 actions）+ reflection-on-action（test-time training 更新 internal reflection model 和 action policy）；retrospective reflection 做 proper long-horizon credit assignment  [src: abs]
- [Modality] [embodied]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩ + ⟨RL⟩  [src: abs]
- [机制] two modes of reflection：reflection-in-action（执行前用 test-time scaling 生成多个候选 actions 并内部反思评分）+ reflection-on-action（执行后用外部反思更新 reflection model 和 action policy） [src: abs]

---

## Pathway P6: V-Par → π-Par（Preference Alignment）

Evaluator 信号 → policy weights via RLHF / DPO。
参数间转化，兼具 transformation 与 utilization 双重性质。

---

### SWEET-RL: Training Multi-Turn LLM Agents on Collaborative Reasoning Tasks
- [原] Textual (Raw Experience) -> Evaluator (critic) -> Policy Parameter
- [Pathway] N-Tok (raw, txt) → V-Par (critic) → π-Par  [src: 四件套, abs]
- [Utilization] critic 提供 step-level rewards 改善 policy model；π-Par 在 multi-turn collaborative tasks 中执行  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self} + {human}（collaborator interaction） [src: abs]
- [Method] ⟨RL: DPO⟩（critic trained with access to additional training-time information） [src: abs]
- [机制] SWEET-RL 用 training-time information 训练 critic model 提供 step-level rewards；在 ColBench 上 6% 绝对提升，Llama-3.1-8B 匹配或超越 GPT-4o  [src: abs]

---

### From Novice to Expert: LLM Agent Policy Optimization via Step-wise RL (StepAgent)
- [原] Textual (Raw Experience) -> Policy Parameter
- [原] Textual (Raw Experience) -> Evaluator (Discriminator) -> Policy Parameter
- [Pathway] N-Tok (raw, txt) → V-Par (discriminator) → π-Par  [src: 四件套, abs]
- [Pathway] N-Tok (raw, txt) → π-Par（直接 SFT/RL） [src: 四件套, abs]
- [Utilization] step-wise reward 提供 fine-grained optimization；implicit-reward 和 inverse RL 技术促进 agent reflection 和 policy adjustment  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self} + {teacher}（expert actions for comparison） [src: abs]
- [Method] ⟨RL: DPO, PPO⟩  [src: abs]
- [机制] novice-to-expert：比较 expert 和 agent 的 actions 自动生成 intermediate rewards；理论分析证明 agent action distribution 收敛到 expert  [src: abs]

---

### ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search
- [原] Textual (Raw Experience) -> Policy Parameter
- [原] Textual (Raw Experience) -> Evaluator (Process Reward Model)
- [Pathway] N-Tok (raw, txt) → V-Par (Process Reward Model)  [src: 四件套, abs]
- [Pathway] N-Tok (raw, txt) → π-Par（via tree-search policy） [src: 四件套, abs]
- [Pathway] V-Par (PRM) → π-Par（process rewards 指导 self-training） [src: 四件套, inferred]
- [Utilization] tree-search policy 在推理时 achieve higher accuracy within search budget；PRM 同时用于 refine policy model 和 reward model  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩ + MCTS*（process reward guided tree search） [src: abs]
- [机制] MCTS* 结合 process reward guidance 收集高质量 reasoning traces + per-step value；inferred process rewards 双用途：value targets for PRM training + high-quality traces selection for policy self-training  [src: abs]

---

### Self-Improving VLM Judges Without Human Annotations
- [原] Policy Parameter -> Token (Raw Experience) -> Evaluator (Judge Model)
- [Pathway] π-Par → N-Tok (raw, vis+txt) → V-Par (Judge Model)  [src: 四件套, abs]
- [Utilization] self-trained VLM judge 在 Multimodal RewardBench / VL-RewardBench 上评估 correctness/preference/reasoning/safety/VQA  [src: abs]
- [Modality] [vis+txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩（iterative self-training with self-synthesized data） [src: abs]
- [机制] 三阶段迭代：(1) generate diverse multimodal instruction-response pairs at varying quality levels, (2) generate reasoning traces and judgments, filter mismatches, (3) train on correct judge answers；无需任何 human preference annotations  [src: abs]

---

## Pathway P7: π-Par → Tokenized（Knowledge Externalization）

Policy 权重 → synthetic trajectories / demonstrations。
隐式经验外化为显式载体。

---

### BugPilot: Complex Bug Generation for Efficient Learning of SWE Skills
- [原] Policy Parameter -> Textual (Raw Experience)
- [Pathway] π-Par (SWE agent) → N-Tok (raw, txt, buggy code + test)  [src: 四件套, abs]
- [Utilization] 生成的 bugs 作为下游 SWE agents 的 SFT 训练数据（FrogBoss/FrogMini 模型训练） [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩（数据合成）→ 下游 ⟨SFT⟩  [src: abs]
- [机制] instruct SWE Agents 引入 feature → unintentionally break tests → realistic bugs（与 human-authored edits 模式更接近）；1.2k bugs 超过 3k 其他数据集的 SFT 效果  [src: abs]

---

### EvoCUA: Evolving Computer Use Agents via Learning from Scalable Synthetic Experience
- [原] Policy Parameter -> Token (Raw Experience) -> Policy Parameter
- [Pathway] π-Par → N-Tok (raw, GUI) → π-Par  [src: 四件套, abs]
- [Utilization] iterative evolving learning：reinforcing successful routines + transforming failure trajectories into rich supervision through error analysis and self-correction  [src: abs]
- [Modality] [GUI]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL: GRPO⟩（evolutionary cycle with verifiable synthesis engine） [src: abs, inferred]
- [机制] self-sustaining evolutionary cycle：verifiable synthesis engine 自动生成 diverse tasks + executable validators → scalable sandbox rollouts（tens of thousands）→ iterative evolving learning with capability boundary detection  [src: abs]

---

### Self-Training Large Language Models for Improved Visual Program Synthesis
- [原] Policy Parameter -> Token (Raw Experience, Visual + Textual) -> Policy Parameter
- [Pathway] π-Par → N-Tok (raw, vis+txt) → π-Par  [src: 四件套, abs]
- [Utilization] reinforced self-training loop：policy 生成 visual programs → 执行获得 feedback → 作为训练信号改善 policy  [src: abs]
- [Modality] [vis+txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL⟩（reinforced self-training） [src: abs]
- [机制] 利用 vision-language task annotations 构造 coarse reward signal → LLM as policy → reinforced self-training 改善 visual program synthesis ability  [src: abs]

---

## Composite Pipelines（多路径组合 / 链式复合）

以下论文将多条 pathway 链式组合作为整体方法。
完整 anatomy 应在 Section 7 (Composite Pipelines) 中进行。
此处标注涉及的子 pathway 及衔接方式。

---

### EvolveR: Self-Evolving LLM Agents through an Experience-Driven Lifecycle
- [原] Textual (Raw Experience) -> Textual (Principle) -> Policy Parameter
- [Pathway] (a) N-Tok (raw, txt) → N-Tok (refined, principle)  [src: 四件套, abs]
- [Pathway] (b) N-Tok (refined, principle) → π-Par  [src: 四件套, abs]
- [Composite Pattern] Extract-then-Train：Offline Self-Distillation（trajectories → structured repository of abstract reusable strategic principles）→ Online Interaction（retrieve distilled principles 指导 decision-making + policy reinforcement mechanism 迭代更新 agent） [src: abs]
- [Utilization] distilled principles 在 online interaction 中检索并 prepend 到 agent context；policy reinforcement mechanism 基于 performance 迭代更新 agent  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩（cold start）+ ⟨RL: GRPO⟩  [src: abs]
- [机制] 完整 closed-loop experience lifecycle：Offline Self-Distillation（trajectories → abstract reusable principles）→ Online Interaction（principles 指导决策 + 积累 diverse trajectories）→ policy reinforcement 迭代更新  [src: abs]

---

### SaMuLe: Self-Learning Agents Enhanced by Multi-level Reflection
- [原] Textual (Raw Experience) -> Textual (Reflection) -> Reflection Parameter
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, reflection) → π-Par (retrospective model)  [src: 四件套, abs]
- [Pathway 修正] 原: -> Reflection Parameter → 改: -> π-Par (retrospective language model)。该"Reflection Parameter"是 fine-tuned 的 retrospective language model 权重，属于 Policy Parameter（生成 reflection 的 actor 权重）。  [src: abs, 四件套]
- [Composite Pattern] Extract-then-Train：Multi-Level Reflection Synthesis（micro/meso/macro 三层 reflection）→ SFT retrospective model → inference 时 model 生成 reflections 指导 agent  [src: abs]
- [Utilization] fine-tuned retrospective model 在推理时生成 reflections 指导 agent；foresight-based reflection 在交互式设置中比较 predicted vs actual responses 触发主动反思  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩（reflection synthesis）+ ⟨SFT⟩（retrospective model） [src: abs]
- [机制] 三层 reflection synthesis：Single-Trajectory Learning (micro-level error correction) → Intra-Task Learning (meso-level error taxonomies) → Inter-Task Learning (macro-level transferable insights)  [src: abs]

---

### SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from Experience
- [原] Token(Visual + Textual, Raw Experience) -> Evaluator
- [原] Token(Visual + Textual, Raw Experience) -> Textual
- [原] Token(Visual + Textual, Raw Experience) -> Policy Parameter
- [Pathway] (a) N-Tok (raw, GUI) → V-Par (World State Model)  [src: 四件套, abs]
- [Pathway] (b) N-Tok (raw, GUI) → N-Tok (refined, curriculum tasks)  [src: 四件套, abs]
- [Pathway] (c) N-Tok (raw, GUI) → π-Par  [src: 四件套, abs]
- [Composite Pattern] Evaluate-then-Train + Curriculum Self-Generation：World State Model 做 step-wise trajectory assessment → Curriculum Generator 生成 increasingly diverse/challenging tasks → GRPO 更新 policy + adversarial imitation of failure actions  [src: abs]
- [Utilization] World State Model 评估轨迹质量；Curriculum Generator 提供训练任务；updated policy 在 novel software 环境中执行  [src: abs]
- [Modality] [GUI]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩ + ⟨RL: GRPO⟩ + Curriculum Learning  [src: abs]
- [机制] specialist-to-generalist training：experiential learning（adversarial imitation of failures + GRPO on successes）→ 从多个 specialist agents 整合 experiential insights → 训练更强的 generalist CUA  [src: abs]

---

### Agentic Proposing: Enhancing LLM Reasoning via Compositional Skill Synthesis
- [原] Textual (Raw Experience) -> Textual (Skill) -> Policy Parameter
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, skill) → π-Par (Agentic-Proposer-4B)  [src: 四件套, abs]
- [Pathway 修正] 原: -> Policy Parameter（合成数据的 proposer 的参数）。该 π-Par 是 proposer 的权重，proposer 再生成数据用于下游 solvers 训练。这是两层 transformation：(1) raw → skill → proposer π-Par (MGPO 训练内化 skill synthesis 能力)；(2) proposer π-Par → N-Tok (synthetic trajectories) → downstream solver π-Par。  [src: abs, inferred]
- [Composite Pattern] Extract-then-Train + Data Synthesis Loop：modular reasoning skills 动态组合 → MGPO 训练 proposer → proposer 生成 high-precision verifiable training trajectories → 下游 solvers 训练  [src: abs]
- [Utilization] Agentic-Proposer-4B 生成高质量合成数据（11K trajectories），下游 30B solver 在 AIME25 上达到 SOTA 91.6%  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL: MGPO⟩（Multi-Granularity Policy Optimization for proposer）+ ⟨SFT⟩（downstream solvers） [src: abs]
- [机制] 将 problem synthesis 建模为 goal-driven sequential decision process：agent 动态选择并组合 modular reasoning skills；iterative internal reflection + tool-use 生成 high-precision verifiable trajectories  [src: abs]

---

### Skill-SD: Skill-Conditioned Self-Distillation for Multi-turn LLM Agents
- [原] Textual (Raw Experience) -> Textual (Skill) -> Policy Parameter
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, skill) → π-Par  [src: 四件套, abs]
- [Composite Pattern] Extract-then-Distill：completed trajectories → compact natural language skills（描述 successful behaviors / mistakes / workflows）→ skills as dynamic privileged information conditioning teacher → importance-weighted reverse-KL distillation to student（policy） [src: abs]
- [Utilization] student policy 在 plain task prompt 下运行，无需 inference-time skill retrieval；skills 在训练中被 internalize 进参数  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL: GRPO⟩ + self-distillation（importance-weighted reverse-KL loss） [src: abs]
- [机制] 将 agent's own trajectories 转为 dynamic training-only supervision：skills 浓缩成功行为/错误/工作流 → 仅 teacher 可见 → student 通过蒸馏 internalize guidance；teacher-student synchronization 稳定训练  [src: abs]

---

### SKILL0: In-Context Agentic RL for Skill Internalization
- [原] Textual (Skill) -> Policy Parameter
- [Pathway] N-Tok (refined, skill) → π-Par  [src: 四件套, abs]
- [Composite Pattern] Curriculum Internalization：training-time curriculum 从 full skill context 逐步 withdraw → Dynamic Curriculum 评估每个 skill 的 on-policy helpfulness → 保留当前 policy 仍受益的 skills → 最终 agent 在 zero-shot（无 skill retrieval）下运行  [src: abs]
- [Utilization] internalized policy 在推理时无需任何 runtime skill retrieval，零 token overhead from skills  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL: PPO⟩（with in-context skill curriculum） [src: abs]
- [机制] skills 按 category 分组 + interaction history 渲染为 compact visual context → Dynamic Curriculum 线性递减 budget → skills 逐步 internalize 直到 fully zero-shot；ALFWorld +9.7%, Search-QA +6.6%  [src: abs]

---

### ScoreFlow: Mastering LLM Agent Workflows via Score-based Preference Optimization
- [原] Textual (Raw Experience) -> Policy Model -> Structural (Workflow)
- [Pathway] N-Tok (raw, txt) → π-Par (Workflow Generator) → S-Tok (workflow)  [src: 四件套, abs]
- [Pathway 修正] 原: Policy Model（中间态）不是被转化的载体，而是 Workflow Generator 的 π-Par 权重。准确表述：通过 Score-DPO（DPO 变体，incorporates quantitative feedback）优化 Workflow Generator 的 π-Par，使 Generator 产生的 S-Tok (workflow) 质量更高。  [src: abs, 四件套]
- [Composite Pattern] Evaluate-then-Optimize：Score-DPO 用 quantitative feedback 优化连续空间中的 Workflow Generator → Generator 输出高质量 workflow  [src: abs]
- [Utilization] 生成的 workflows 在 reasoning / coding / math 任务中 orchestrating agent behavior  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL: Score-DPO⟩（DPO variant with quantitative feedback） [src: abs]
- [机制] ScoreFlow 用 gradient-based optimization in continuous space 替代 discrete optimization；Score-DPO 融入 quantitative feedback，较小模型可超越更大模型  [src: abs]

---

### Reinforcement Learning for Self-Improving Agent with Skill Library (SAGE)
- [原] Textual (Raw Experience) -> Policy Parameter -> Textual (skill)
- [Pathway] N-Tok (raw, txt) → π-Par → N-Tok (refined, skill)  [src: 四件套, abs]
- [Composite Pattern] Self-Generation Loop with Skill Library：Sequential Rollout 在 task chain 中迭代部署 agent → skills 从先前 tasks 积累到 library → Skill-integrated Reward 同时奖励任务成功和 skill generation/utilization  [src: abs]
- [Utilization] library 中的 skills 在后续 tasks 中可用；updated policy 生成更高质量的 skills  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL: GRPO⟩（Skill Augmented GRPO for self-Evolution） [src: abs]
- [机制] Sequential Rollout 沿 task chain 迭代部署 agent，skills 跨任务积累；Skill-integrated Reward 补充 outcome-based rewards；AppWorld 上 +8.9% Scenario Goal Completion，-26% interaction steps  [src: abs]

---

### On-Policy Context Distillation for Language Models (OPCD)
- [原] 与 Online Experiential Learning 共享标注：Textual (Raw Experience) -> Textual -> Policy Parameter
- [Pathway] N-Tok (raw, txt, historical solution traces) → N-Tok (refined, experiential knowledge) → π-Par  [src: 四件套, abs]
- [Composite Pattern] Extract-then-Distill：historical solution traces → extract transferable experiential knowledge → on-policy context distillation (student trains on its own generated trajectories, minimizing reverse KL divergence against context-conditioned teacher) → internalized knowledge 不再需要 context demonstrations  [src: abs]
- [Utilization] distilled student model 在推理时不再需要在 context 中提供 demonstrations；支持 cross-size distillation（smaller student internalizes knowledge from larger teacher） [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩（on-policy context distillation with reverse KL-divergence minimization） [src: abs]
- [机制] 桥接 on-policy distillation 与 context distillation：experiential knowledge distillation（从历史 solution traces 提取可迁移知识）+ system prompt distillation（internalize optimized prompt behaviors）；on-policy consistency 保证 student 在自生成轨迹上学习  [src: abs]

---

### Online Experiential Learning for Language Models (OEL)
- [原] Textual (Raw Experience) -> Textual -> Policy Parameter
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, experiential knowledge) → π-Par  [src: 四件套, abs]
- [Composite Pattern] Extract-then-Distill (Online)：user-side interaction trajectories → extract transferable experiential knowledge → on-policy context distillation 将 knowledge 内化到 parameters → improved model 收集更高质量 trajectories  [src: abs]
- [Utilization] consolidated π-Par 在部署中直接执行，无需访问 user-side environment；on-policy consistency 对有效学习至关重要  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩ + ⟨SFT⟩（on-policy context distillation） [src: abs]
- [机制] online learning loop：extract transferable knowledge from deployment trajectories → consolidate into parameters via on-policy context distillation（无需访问 user environment）→ improved model generates better trajectories  [src: abs]

---

### EvoAgentX: An Automated Framework for Evolving Agentic Workflows
- [原] Policy Parameter -> Workflow
- [Pathway] π-Par → S-Tok (workflow)  [src: 四件套, abs]
- [Utilization] evolved workflows（agent prompts / tool configurations / workflow topologies）在推理时 orchestrate multi-agent systems  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩（TextGrad / AFlow / MIPRO 三种优化算法） [src: abs]
- [机制] modular five-layer architecture；三种 MAS optimization algorithms 用于 iterative refine agent prompts/tool configurations/workflow topologies  [src: abs]

---

### [新增] ABot-Claw: A Foundation for Persistent, Cooperative, and Self-Evolving Robotic Agents
- [Pathway] (a) N-Tok (raw, embodied) → N-Tok (refined, multimodal memory)  [src: abs, 四件套]
- [Pathway] (b) N-Tok (raw, embodied) → V-Par (generalist reward model)  [src: abs, 四件套]
- [Composite Pattern] Memory-Augmented + Critic-Guided Self-Evolution：visual-centric cross-embodiment multimodal memory（persistent context retention + grounded retrieval）+ critic-based closed-loop feedback with generalist reward model（online progress evaluation + local correction + replanning）→ progressively self-evolving robotic agents  [src: abs]
- [Utilization] multimodal memory 提供 persistent context retention and grounded retrieval；critic-based feedback loop 做 online progress evaluation / local correction / replanning  [src: abs]
- [Modality] [embodied]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩ + ⟨RL⟩（critic-based feedback with reward model） [src: abs, inferred]
- [机制] decoupled architecture spanning OpenClaw layer / shared service layer / robot embodiment layer；unified embodiment interface with capability-driven scheduling for heterogeneous robot coordination  [src: abs]

---

### MetaClaw: Just Talk — An Agent That Meta-Learns and Evolves in the Wild
- [原] (未在 Taxonomy.md 中独立列出)
- [Pathway] (a) N-Tok (raw, txt) → N-Tok (refined, skill)  [src: abs, inferred]
- [Pathway] (b) N-Tok (raw, txt) → π-Par (via LoRA + RL-PRM)  [src: abs, inferred]
- [Composite Pattern] Skill-driven Fast Adaptation + Opportunistic Policy Optimization：failure trajectory analysis → LLM evolver synthesizes new skills (zero downtime) + Opportunistic Meta-Learning Scheduler triggers LoRA fine-tuning + RL-PRM during user-inactive windows → refined policy 产生更好 trajectories for skill synthesis  [src: abs]
- [Utilization] skills 注入 agent 提供 immediate improvement；refined π-Par 在后续交互中表现更好；skills 与 policy 相互强化  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩ + ⟨SFT⟩(LoRA) + ⟨RL: GRPO⟩(with PRM)  [src: abs]
- [机制] continual meta-learning：skill-driven fast adaptation（zero downtime）+ opportunistic policy optimization（仅在 user-inactive 时触发）；skills 和 policy 相互强化，Kimi-K2.5 从 21.4% → 40.6%  [src: abs]

---

> **备注（Q4 — Skill/Carrier 分类边界）**：部分工作（如 `CoEvoSkills`、`Automated Design of Agentic Systems`、`SkillWeaver`）产生的 artifacts 同时包含自然语言描述（N-Tok）和结构化可执行组件（S-Tok）。当前约定：若产物以可执行为主要复用方式，归入 S-Tok；若以自然语言理解为主要复用方式，归入 N-Tok。Composite 条目中逐条列出子路径即可区分，不再进一步拆分。

---

## [新增] Papers from arxiv_abstracts_merged.md not in original Taxonomy.md

以下论文出现在 `arxiv_abstracts_merged.md` 中但未在原始 `Taxonomy.md` 中标注，现基于 abstract 信息补标。标记 `[新增]` 以区别于原有条目。

---

### [新增] Voyager: An Open-Ended Embodied Agent with Large Language Models
- [Pathway] N-Tok (raw, embodied) → S-Tok (code, skill)  [src: abs, 四件套]
- [Utilization] skill library 中的 executable code skills 在后续 Minecraft 任务中检索和组合执行；iterative prompting mechanism 融入 environment feedback / execution errors / self-verification 做 program improvement  [src: abs]
- [Modality] [embodied]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩（blackbox GPT-4 queries, iterative prompting, 无参数更新） [src: abs]
- [机制] 三组件：automatic curriculum（最大化探索）+ skill library（executable code for storing/retrieving complex behaviors）+ iterative prompting（environment feedback + execution errors + self-verification）；skills 是 temporally extended / interpretable / compositional  [src: abs]

---

### [新增] WizardLM: Empowering Large Pre-trained Language Models to Follow Complex Instructions
- [Pathway] π-Par → N-Tok (raw, txt, instruction) → π-Par  [src: abs, 四件套]
- [Utilization] Evol-Instruct 生成的 instruction data 用于 fine-tune LLaMA，fine-tuned model 直接作为 instruction-following LM 部署  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩  [src: abs]
- [机制] Evol-Instruct：从初始指令集出发，用 LLM 逐步 rewrite 为更复杂的指令，混合所有生成数据 fine-tune LLaMA；在 complexity-balanced test bed 上超越人类创建的指令  [src: abs]

---

### [新增] Self-Generated In-Context Examples Improve LLM Agents for Sequential Decision-Making Tasks
- [Pathway] N-Tok (raw, txt, successful trajectories) → N-Tok (refined, in-context example)  [src: abs, 四件套]
- [Utilization] database of self-generated successful trajectories 作为 in-context examples 在后续任务中 prepend；database-level curation（population-based training）+ exemplar-level curation（empirical utility 筛选） [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩（无参数更新） [src: abs]
- [机制] naive accumulation of successful trajectories 即带来显著提升（ALFWorld 73%→89%）；population-based training 传播高性能 example collections，exemplar-level curation 基于 empirical utility 选择性保留；最终 ALFWorld 93%，超越使用更强 LLM 和 hand-crafted components 的方法  [src: abs]

---

### [新增] VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought (ICAL)
- [Pathway] N-Tok (raw, vis+txt, suboptimal trajectory) → N-Tok (refined, strategy, annotation, txt)  [src: abs, 四件套]
- [Utilization] ICAL examples 用于 retrieval-augmented generation 或 fine-tuning；abstracted strategies and action annotations 显著改善 decision-making；example library 增长使 agent 更高效地抽象新 examples  [src: abs]
- [Modality] [cross-modal]  [src: abs]
- [Source] {self} + {human}（human feedback for iterative refinement） [src: abs]
- [Method] ⟨LLM-extract⟩ + ⟨SFT⟩（下游） [src: abs]
- [机制] 将 suboptimal trajectories 转化为高质量训练数据：VLM 抽象 trajectories 为 generalized strategies and action annotations（causal relationships / object state changes / temporal subgoals / task-relevant visual elements），通过 human feedback 迭代 refine  [src: abs]

---

### [新增] WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance
- [Pathway] N-Tok (raw, web) → N-Tok (refined, summary, episodic experience)  [src: abs, 四件套]
- [Utilization] Coach 基于 similarity and recency 检索相关 experiences，决定是否通过 runtime hooks 向 agent 注入 task-specific advice；WebCondenser 标准化 raw logs 为 concise summaries  [src: abs]
- [Modality] [GUI]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩（model-agnostic, 无 retraining） [src: abs]
- [机制] 三组件：WebCondenser（raw logs → concise summaries）+ External Memory Store（完整 trajectories as episodic experiences）+ Coach（retrieve + decide injection）；持续 curation of episodic memory 实现 self-evolution  [src: abs]

---

### [新增] WISE-Flow: Workflow-Induced Structured Experience for Self-Evolving Conversational Service Agents
- [Pathway] N-Tok (raw, txt, service interactions) → S-Tok (workflow, prerequisite-augmented action blocks)  [src: abs, 四件套]
- [Utilization] deployment 时将 agent's execution trajectory 对齐到 retrieved workflows，prerequisite-aware feasibility reasoning 产生 state-grounded next actions  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] workflow-centric：将历史 service interactions 转化为 reusable procedural experience by inducing workflows with prerequisite-augmented action blocks  [src: abs]

---

### [新增] UI-Mem: Self-Evolving Experience Memory for Online RL in Mobile GUI Agents
- [Pathway] N-Tok (raw, GUI) → S-Tok (workflow template, subtask skill) + N-Tok (refined, failure pattern)  [src: abs, 四件套]
- [Composite] Memory-Augmented Online RL：Hierarchical Experience Memory 积累 structured knowledge（high-level workflows / subtask skills / failure patterns）→ Stratified Group Sampling 在不同 trajectories 间注入不同级别 guidance → Self-Evolving Loop 持续 abstract 新策略和错误  [src: abs]
- [Utilization] parameterized templates 实现跨任务跨应用迁移；Stratified Group Sampling 保持 outcome diversity 驱动 unguided policy 内化 guided behaviors  [src: abs]
- [Modality] [GUI]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL⟩（online RL with Hierarchical Experience Memory）+ ⟨LLM-extract⟩（Self-Evolving Loop） [src: abs]
- [机制] 不同于传统 replay buffer，memory 积累 structured knowledge（workflow/skill/failure templates）；Stratified Group Sampling 在 rollout group 内注入不同级别 guidance 保持 diversity；Self-Evolving Loop 持续抽象新策略和错误保持 memory 与 evolving policy 对齐  [src: abs]

---

### [新增] WebEvolver: Enhancing Web Agent Self-Improvement with Coevolving World Model
- [Pathway] π-Par (agent) → N-Tok (raw, web) → π-Par (agent) + π-Par (World Model)  [src: abs, 四件套]
- [Composite] World-Model-Augmented Self-Improvement：co-evolving World Model LLM 双重角色：(1) virtual web server 生成 self-instructed training data 持续 refine agent policy；(2) imagination engine 在推理时做 look-ahead simulation 指导 action selection  [src: abs]
- [Utilization] World Model 在推理时作为 imagination engine 模拟 action 后果；agent policy 通过世界模型生成的 self-instructed data 持续 refine  [src: abs]
- [Modality] [GUI]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL⟩ + World Model training  [src: abs, inferred]
- [机制] 针对 self-improvement stagnation：引入 co-evolving World Model 打破 exploration 瓶颈，利用 LLM 的 pretrained web knowledge 作为 virtual web server 和 imagination engine  [src: abs]

---

### [新增] SLEA-RL: Step-Level Experience Augmented RL for Multi-Turn Agentic Training
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, experience library) + π-Par  [src: abs, 四件套]
- [Composite] Experience-Augmented RL with Step-Level Retrieval：step-level observation clustering 分组等价环境状态 → self-evolving experience library 蒸馏成功策略和失败模式 → policy optimization with step-level credit assignment  [src: abs]
- [Utilization] 每一步基于当前 observation 检索相关 experiences 注入 policy；experience library 通过 semantic analysis（非 gradient updates）与 policy 共同进化  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL⟩（step-level credit assignment）+ ⟨LLM-extract⟩（experience library evolution） [src: abs]
- [机制] 区别于 static retrieval（仅基于初始 task description 检索一次），SLEA-RL 在每一步基于当前 observation 做 step-level retrieval；score-based admission + rate-limited extraction 控制 experience library 质量  [src: abs]

---

### [新增] When Agents go Astray: Course-Correcting SWE Agents with PRMs (SWE-PRM)
- [Pathway] N-Tok (raw, txt, SWE trajectories) → V-Par (Process Reward Model)  [src: abs, 四件套]
- [Utilization] inference-time PRM 在 execution 期间 detect and course-correct trajectory-level errors（redundant exploration / looping / failure to terminate）；taxonomy-guided feedback 优于 unguided 或 explicit action-prescriptive variants  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩（PRM training with taxonomy of common inefficiencies） [src: abs]
- [机制] SWE-PRM 利用 common inefficiencies taxonomy 提供 lightweight interpretable feedback，不修改 underlying policy；SWE-bench Verified 上从 40.0%→50.6%，最大收益在 medium and hard tasks  [src: abs]

---

### [新增] V-Zero: Self-Improving Multimodal Reasoning with Zero Annotation
- [Pathway] π-Par (Questioner) → N-Tok (raw, vis+txt, questions) → π-Par (Solver)  [src: abs, 四件套]
- [Utilization] co-evolutionary loop：Questioner 学习合成高质量 challenging questions（dual-track reasoning reward 对比 intuitive guesses 与 reasoned results）；Solver 用 majority voting pseudo-labels 优化；两者通过 GRPO 迭代训练  [src: abs]
- [Modality] [vis+txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL: GRPO⟩（Questioner + Solver co-evolution） [src: abs]
- [机制] 完全无 human annotation：Questioner 和 Solver 互为对手协同进化，mutual enhancement cycle；visual mathematical reasoning +1.7，general vision-centric +2.6  [src: abs]

---

### [新增] Self-Distillation Zero: Self-Revision Turns Binary Rewards into Dense Supervision (SD-Zero)
- [Pathway] π-Par (Generator) → N-Tok (raw, txt) → π-Par (via Reviser self-distillation)  [src: abs, 四件套]
- [Utilization] Generator 产生 initial response → Reviser 基于 response + binary reward 产生 improved response → on-policy self-distillation 将 Reviser 的 token distributions 蒸馏到 Generator；最终 Generator 独立运行  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩（on-policy self-distillation, 无 external teacher） [src: abs]
- [机制] 单一模型扮演两个角色（Generator + Reviser）：Reviser 基于 binary reward 做 token-level self-localization（识别需修改的关键 tokens）→ iterative self-evolution（改善 revision 能力蒸馏回 generation） [src: abs]

---

### [新增] Self-Distillation Zero: Self-Revision Turns Binary Rewards into Dense Supervision (SD-Zero)
- [Pathway] π-Par (Generator) → N-Tok (raw, txt) → π-Par (via Reviser self-distillation)  [src: abs, 四件套]
- [Utilization] Generator 产生 initial response → Reviser 基于 response + binary reward 产生 improved response → on-policy self-distillation 将 Reviser 的 token distributions 蒸馏到 Generator；最终 Generator 独立运行  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩（on-policy self-distillation, 无 external teacher） [src: abs]
- [机制] 单一模型扮演两个角色（Generator + Reviser）：Reviser 基于 binary reward 做 token-level self-localization（识别需修改的关键 tokens）→ iterative self-evolution（改善 revision 能力蒸馏回 generation） [src: abs]

---

### [新增] SkillFoundry: Building Self-Evolving Agent Skill Libraries from Heterogeneous Scientific Resources
- [Pathway] heterogeneous resources (repos/APIs/docs) → S-Tok (skill, validated package)  [src: abs, 四件套]
- [Utilization] mined skills 提升 coding agent 在 MoSciBench 和 genomics tasks 上的表现；skill library 通过 closed-loop validation 迭代 expand/repair/merge/prune  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] domain knowledge tree 组织目标领域 → mine resources from high-value branches → extract operational contracts → compile into executable skill packages（含 task scope / inputs-outputs / execution steps / environment assumptions / provenance / tests）；closed-loop validation 实现 self-evolving  [src: abs]

---

### [新增] WebSynthesis: World-Model-Guided MCTS for Efficient WebUI-Trajectory Synthesis
- [Pathway] π-Par (policy agent) → N-Tok (raw, web, virtual environment) → π-Par  [src: abs, 四件套]
- [Utilization] WebSynthesis 合成的 trajectories 用于 refine agent policy；learned world model 仿真 virtual web environments 支持 efficient reversible tree-based planning  [src: abs]
- [Modality] [GUI]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩ + MCTS（world-model-guided） [src: abs]
- [机制] 针对两大挑战：(1) uncontrollable environment states（用 learned world model 替代真实环境，可逆可复现）；(2) high API costs（virtual environment 中高效 MCTS）；小规模合成数据集训练的 agent 达到或超越大规模真实数据训练的模型  [src: abs]

---

### [新增] Mobile-Agent-v3 / GUI-Owl: Fundamental Agents for GUI Automation
- [Pathway] π-Par → N-Tok (raw, GUI) → π-Par（Self-Evolving GUI Trajectory Production） [src: abs, 四件套]
- [Utilization] GUI-Owl 作为 foundational GUI agent model 支持 end-to-end decision-making 或作为 multi-agent system 的 modular component；TRPO (Trajectory-aware Relative Policy Optimization) 做 online RL  [src: abs]
- [Modality] [GUI]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨SFT⟩ + ⟨RL⟩（TRPO: Trajectory-aware Relative Policy Optimization, online RL） [src: abs]
- [机制] 三项创新：(1) cloud-based virtual environment（Android/Ubuntu/macOS/Windows）支持 Self-Evolving GUI Trajectory Production；(2) 集成 UI grounding / planning / action semantics / reasoning patterns；(3) scalable RL with fully asynchronous training  [src: abs]

---

### [新增] Test-Time Adaptation for LLM Agents via Environment Interaction
- [Pathway] N-Tok (raw, txt, environment interaction) → π-Par (lightweight adaptation vector)  [src: abs, 四件套]
- [Utilization] (a) online syntactic alignment (SA)：学习 lightweight adaptation vector 偏置 model output distribution 快速对齐环境 response format；(b) deployment-time dynamics grounding (DG)：persona-driven exploration 系统性探测环境 causal dynamics，构建 in-context world model  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩（adaptation vector via gradient-based optimization）+ ⟨LLM-extract⟩（DG in-context world model） [src: abs, inferred]
- [机制] 区分两种 test-time failure：syntactic misunderstanding（环境 specific 格式）+ semantic misunderstanding（状态转移 dynamics）；SA 和 DG 分别针对；WebArena multi-site split 上 DG 将 success rate 从 2% 提升到 23%  [src: abs]

---

### [新增] SymAgent: A Neural-Symbolic Self-Learning Agent Framework for Complex Reasoning over KGs
- [Pathway] N-Tok (raw, txt) → S-Tok (symbolic rules from KG) → π-Par  [src: abs, 四件套]
- [Composite] Neural-Symbolic Self-Learning：Agent-Planner 用 LLM inductive reasoning 从 KG 提取 symbolic rules → Agent-Executor 自主调用 action tools 整合 KG 和外部文档 → self-learning framework（online exploration + offline iterative policy updating）自动合成 reasoning trajectories  [src: abs]
- [Utilization] symbolic rules 指导 question decomposition；Agent-Executor 在推理时自主调用预定义 action tools；self-learning 迭代更新 policy  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩ + ⟨RL⟩（offline iterative policy updating） [src: abs, inferred]
- [机制] 将 KG 概念化为 dynamic environment，将复杂推理转化为 multi-step interactive process；能识别 missing triples 促进自动 KG 更新  [src: abs]

---

### [新增] SEAL: Self-Evolving Agentic Learning for Conversational QA over Knowledge Graphs
- [Pathway] N-Tok (raw, txt, dialog history) → S-Tok (S-expression) + N-Tok (refined, reflection)  [src: abs, 四件套]
- [Utilization] self-evolving mechanism 整合 local and global memory with reflection module，从 dialog history 和 execution feedback 中持续 adapt 无需 explicit retraining  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] two-stage semantic parsing：LLM 提取 minimal S-expression core → agentic calibration module 纠正 syntactic inconsistencies → template-based completion with question-type prediction；self-evolving mechanism 持续 adapt  [src: abs]

---

### [新增] Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory
- [Pathway] N-Tok (raw, txt, conversation) → N-Tok (refined, consolidated memory) + S-Tok (graph)  [src: abs, 四件套]
- [Utilization] dynamically extract / consolidate / retrieve salient information from ongoing conversations；graph-based variant capture complex relational structures；91% lower p95 latency，90%+ token cost savings vs full-context  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] memory-centric architecture：dynamic extraction + consolidation + retrieval of conversational information；graph memory 增强版 capture relational structures among conversational elements  [src: abs]

---

### [新增] HiMem: Hierarchical Long-Term Memory for LLM Long-Horizon Agents
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, episode memory, note memory)  [src: abs, 四件套]
- [Utilization] 两种 memory 语义链接形成 hierarchical structure：Episode Memory（concrete interaction events）+ Note Memory（stable knowledge）；hybrid / best-effort retrieval strategies；conflict-aware Memory Reconsolidation 基于 retrieval feedback 修正和补充 stored knowledge  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] Topic-Aware Event-Surprise Dual-Channel Segmentation 构建 cognitively consistent Episode Memory；multi-stage information extraction 构建 Note Memory；Memory Reconsolidation 实现 continual memory self-evolution  [src: abs]

---

### [新增] Where LLM Agents Fail and How They can Learn From Failures (AgentDebug)
- [Pathway] N-Tok (raw, txt, failure trajectory) → N-Tok (refined, corrective feedback)  [src: abs, 四件套]
- [Utilization] AgentDebug 提供 targeted corrective feedback 使 LLM agents 能 iteratively recover from failures；AgentErrorTaxonomy（memory/reflection/planning/action/system-level）分类 failure modes  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] 首个系统性 agent failure 数据集 AgentErrorBench（ALFWorld/GAIA/WebShop 的 annotated failure trajectories）；AgentDebug isolate root-cause failures → corrective feedback → iterative improvement，task success 相对提升 up to 26%  [src: abs]

---

### [新增] Self-Distillation Fine-Tuning (SDFT): On-Policy Learning from Demonstrations
- [Pathway] N-Tok (raw, txt, demonstrations) → π-Par（on-policy self-distillation） [src: abs, 四件套]
- [Utilization] SDFT 使模型在不依赖显式 reward function 的情况下从 demonstrations 持续学习；on-policy learning 减少 catastrophic forgetting  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {teacher}（demonstrations）+ {self}（on-policy generation） [src: abs]
- [Method] ⟨SFT⟩（demonstration-conditioned model as own teacher, on-policy distillation） [src: abs]
- [机制] 用 demonstration-conditioned model 作为自身 teacher，生成 on-policy training signals；既保留 prior capabilities 又 acquire new skills；sequential learning 中单模型积累多种 skills 无性能退化  [src: abs]

---

### [新增] Self-Distilled RL for Co-Evolving Agentic Recommender Systems (CoARS)
- [Pathway] N-Tok (raw, txt, interaction trajectory) → π-Par (recommender) + π-Par (user agent)  [src: abs, 四件套]
- [Composite] Co-Evolution via Self-Distilled RL：interaction reward（同一 trajectory 为 recommender + user agent 提供 coupled task-level supervision）+ self-distilled credit assignment（historical trajectories → token-level credit signals under teacher-student conditioning） [src: abs]
- [Utilization] co-evolved recommender agent 和 user agent 通过多轮交互 iterative preference elicitation 和 refinement  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨RL⟩（self-distilled RL with interaction reward + self-distilled credit assignment） [src: abs, inferred]
- [机制] 超越 Reflexion-style external memory：将 interaction experience internalize 到 parameters；capture ARS 的 interactive nature（recommender 和 user agent 持续相互影响产生 endogenous supervision） [src: abs]

---

### [新增] Language Agent Tree Search (LATS): Unifying Reasoning Acting and Planning
- [Pathway] π-Par → N-Tok (raw, txt, search trace) → N-Tok (refined, self-reflection, value function)  [src: abs, 四件套, inferred]
- [Utilization] MCTS 用 LLM-powered value functions 和 self-reflections 做 exploration；environment 提供 external feedback；search trace 中的 reflections 和 values 指导后续 search decisions  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩（gradient-free, MCTS + self-reflection, 无参数更新） [src: abs]
- [机制] 将 MCTS 与 LLM 的 reasoning/acting/planning 能力结合：LM-powered value functions + self-reflections 做 proficient exploration；external environment feedback 提供更 deliberate adaptive problem-solving  [src: abs]
- [Pathway 说明] LATS 更接近 search/planning 方法而非 experience transformation；self-reflection 和 value function 在 search tree 内使用但未持久化跨任务复用。归入 P1 因其核心机制为 N-Tok (raw search traces) → N-Tok (refined self-reflections within tree)，但 transformation 发生在单次 search 内部。  [src: inferred]

---

### [新增] ReAct: Synergizing Reasoning and Acting in Language Models
- [Pathway] π-Par → N-Tok (raw, txt, interleaved reasoning + action traces)  [src: abs, 四件套, inferred]
- [Utilization] interleaved reasoning traces 和 actions 在推理时协同：reasoning traces 帮助 model induce/track/update action plans 并处理 exceptions，actions 允许与外部环境交互获取额外信息  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩（few-shot prompting, 无参数更新） [src: abs]
- [机制] foundational agent framework：将 reasoning 和 acting 以 interleaved 方式结合；reasoning traces 增强 interpretability 和 trustworthiness  [src: abs]
- [Pathway 说明] ReAct 是 foundational architecture 而非 experience transformation 方法。归入此处的理由：ReAct 产生的 interleaved reasoning+acting traces 是后续几乎所有 experience transformation 工作的 raw experience 来源格式（即其他方法的 N-Tok raw input 大多采用 ReAct-style 轨迹格式）。标注为 `[新增]` 并在正文中作为 raw experience 格式的参照系引用。  [src: inferred]

---

## Under-Specified / Information-Limited Entries (Q1)

以下论文在原始 `Taxonomy.md` 中信息不足或为空条目，或 abstract 信息有限无法完整标注。集中存放于此。

---

### HyCodePolicy: Hybrid Language Controllers for Multimodal Monitoring and Decision in Embodied Agents
- [原] (空条目)
- [Pathway] N-Tok (raw, embodied) → S-Tok (code, executable program) → S-Tok (repaired code)  [src: abs, inferred]
- [Pathway 说明] UNCLEAR (abstract-only)：abstract 描述 code synthesis from natural language → VLM-based perceptual monitoring → repair，但未明确 experience 如何在多次任务间积累和复用。若 repair feedback 仅用于当前任务内的 self-correction 而未跨任务复用，则不属于 experience transformation（单任务内闭环修复不满足经验跨任务复用的 transformation 定义）。  [src: inferred]
- [Utilization] VLM 在 selected checkpoints 观察检测 execution failures → infer failure causes → repair programs；hybrid dual feedback（structured execution traces + VLM perceptual feedback） [src: abs]
- [Modality] [embodied]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩（code synthesis + perceptual monitoring + iterative repair, 无参数更新） [src: abs]
- [机制] closed-loop programming cycle：decompose instruction into subgoals → generate executable program grounded in object-centric geometric primitives → VLM monitors checkpoints → detect failures → repair  [src: abs]

---

### ALFWorld: Aligning Text and Embodied Environments for Interactive Learning
- [原] 提出了一个 benchmark：ALFWorld
- [Pathway] N/A —— benchmark，非 transformation 方法  [src: 四件套]
- [备注] 本文提出了 ALFWorld benchmark（TextWorld + ALFRED 的对接），BUTLER agent 是其示例 agent。后续大量工作（AutoManual、Agent Learning via Early Experience 等）在此 benchmark 上评估。作为 benchmark 论文不纳入 pathway 分类，但在正文中作为 evaluation platform 引用。

---

## Pathway Attribution Uncertain (Q2)

以下论文的 pathway 归属存在多义性，需进一步讨论确认。每条标注了存疑原因和候选归属。

---

### Reflective Planning: Vision-Language Models for Multi-Stage Long-Horizon Robotic Manipulation
- **存疑原因**：abstract 描述为 "test-time computation framework" 和 "iteratively improves a pretrained VLM"，未明确是参数更新（P5）还是纯 test-time compute（P1）。"reflection mechanism" 使用 generative model 想象 future world states 并 refine reasoning——这种 iterative improvement 若涉及梯度更新则为 P5（N-Tok → π-Par），若仅为 prompt-based iterative refinement 则为 P1（N-Tok → N-Tok reflection）。
- **候选归属**：P1（若 test-time compute only）或 P5（若涉及参数更新 via test-time training）
- **当前暂标**：P1，Method 标注为 UNCLEAR

### Agentic Rubrics as Contextual Verifiers for SWE Agents
- **存疑原因**：pathway 为 π-Par → N-Tok（rubric checklist），但 rubrics 的核心用途是 verification（类似 Evaluator 功能角色）。若 rubric 作为 rule-based verifier 使用，则 utilization mode 为 Score-and-Select，但不涉及 V-Par 训练。这造成了 P1（N-Tok 生成）与 P4（Evaluator 功能）的交叉。
- **候选归属**：P1（按 carrier 类型：rubric 是 N-Tok）或 P4 的 utilization 子类（按功能角色：rubric 充当 verifier）。按"载体形式优先"原则暂归 P1。
- **当前暂标**：P1，附 [Pathway 说明]

### Self-Consolidation for Self-Evolving Agents
- **存疑原因**：self-consolidation 将 non-parametric textual experience 蒸馏为 "compact learnable parameters"——这些参数的载体归属在 Latent 与 Parametric 边界上。按 `Experience_Carrier.md` 的"可学习 memory 表示不解码回 token 归入 Latent"判定为 Lat (cross-session)，但 learnable parameters 的形式接近 Parametric 层。
- **候选归属**：Lat (cross-session)（按 Experience_Carrier.md 边界澄清规则）或一种介于 Latent 与 Parametric 之间的新型 carrier
- **当前暂标**：Lat (cross-session, learnable parameters)，附注其参数性质接近 Parametric 边界

### Becoming Experienced Judges: Selective Test-Time Learning for Evaluators (LWE)
- **存疑原因**：本质是 evaluator 的 meta-prompt（N-Tok）通过 self-generated feedback 持续 self-update（N-Tok → N-Tok），不涉及 evaluator 参数（V-Par）更新。这属于 evaluator utilization 的优化而非 experience transformation？若视 evaluator 自身的 evaluation policy 为一种能力，meta-prompt 的改进算是对该能力的"经验积累"吗？
- **候选归属**：P1（N-Tok → N-Tok meta-prompt self-update）或排除在 transformation 框架外（视为 pure utilization optimization）
- **当前暂标**：P1，附 [Pathway 说明]

### HyCodePolicy
- **存疑原因**：abstract 信息不足以判定经验是否跨任务积累和复用。单任务内的 code synthesis → execution → perceptual monitoring → repair 环若不跨任务复用经验，不满足 experience transformation 定义。
- **候选归属**：待确认是否满足跨任务经验复用条件后决定
- **当前暂标**：Under-Specified 节，标注 UNCLEAR

---

## Remaining Abstracts Papers — Categorized

以下论文出现在 `arxiv_abstracts_merged.md` 中但尚未在前述各节中出现。按其与 Experience Transformation 框架的关系分为四组。

---

### Group A: Borderline Methods — Pathway Uncertain or Weak Transformation（保留待定）

以下论文涉及经验转化但 pathway 不够清晰，或 transformation 语义较弱。保留在此待进一步讨论。

---

#### [新增] ReCAP: Recursive Context-Aware Reasoning and Planning for LLM Agents
- [Pathway] N-Tok (raw, txt) → N-Tok (refined, hierarchical plan)  [src: abs, 四件套, inferred]
- [Utilization] plan-ahead decomposition（生成完整 subtask list → 执行第一步 → refine 剩余）+ structured re-injection of parent plans（递归返回时保持多层 context 一致性）+ memory-efficient execution（active prompt bounded, costs scale linearly） [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [机制] hierarchical framework with shared context：解决 sequential prompting 的 context drift / goal loss / recurrent failure cycles  [src: abs]
- [Pathway 说明] ReCAP 更接近 planning architecture 而非 experience transformation；transformation 发生在单任务内而非跨任务复用。  [src: inferred]

---

#### [新增] Search-o1: Agentic Search-Enhanced Large Reasoning Models
- [Pathway] π-Par → N-Tok (refined, retrieved document) → N-Tok (refined, reasoning chain with external knowledge)  [src: abs, 四件套, inferred]
- [Utilization] agentic search workflow 在推理过程中遇到不确定知识时动态检索外部知识；Reason-in-Documents module 深度分析检索到的文档后注入推理链  [src: abs]
- [Modality] [txt]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩（agentic RAG, 无参数更新） [src: abs]
- [Pathway 说明] Search-o1 更接近 RAG 增强推理而非 experience transformation；经验来自外部检索而非 agent 自身交互历史。  [src: inferred]

---

#### [新增] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success
- [Pathway] π-Par (OpenVLA) → π-Par (OpenVLA-OFT, via optimized fine-tuning recipe)  [src: abs, 四件套, inferred]
- [Utilization] OFT recipe（parallel decoding / action chunking / continuous action representation / L1 regression）提升 inference efficiency + policy performance；LIBERO 76.5%→97.1%，action generation throughput 提升 26×  [src: abs]
- [Modality] [embodied]  [src: abs]
- [Source] {teacher}（robot demonstration datasets） [src: abs]
- [Method] ⟨SFT⟩（optimized fine-tuning recipe for VLA adaptation） [src: abs]
- [Pathway 说明] VLA fine-tuning 策略优化研究，不直接涉及 experience transformation（缺少从 agent 自身交互经验中学习的 e=(c,a,o,f) 结构）。对 P5 pathway 的 engineering 维度有参考价值。  [src: inferred]

---

#### [新增] Uncertainty-Aware GUI Agent (RecAgent)
- [Pathway] N-Tok (raw, GUI) → N-Tok (refined, component recommendation)  [src: abs, 四件套, inferred]
- [Utilization] component recommendation mechanism 识别最相关 UI elements 减少 perceptual uncertainty；interactive module 在 ambiguous situations 请求 user feedback  [src: abs]
- [Modality] [GUI]  [src: abs]
- [Source] {self} + {human}（human-in-the-loop refinement） [src: abs]
- [Method] ⟨LLM-extract⟩  [src: abs]
- [Pathway 说明] RecAgent 更接近 GUI agent perception optimization 而非 experience transformation。  [src: inferred]

---

#### [新增] Visual Test-time Scaling for GUI Agent Grounding (RegionFocus)
- [Pathway] N-Tok (raw, GUI) → N-Tok (refined, zoomed region)  [src: abs, 四件套, inferred]
- [Utilization] image-as-map mechanism 可视化关键 landmarks；dynamic zoom-in on relevant regions 减少 background clutter 改善 grounding accuracy  [src: abs]
- [Modality] [GUI]  [src: abs]
- [Source] {self}  [src: abs]
- [Method] ⟨LLM-extract⟩（visual test-time scaling, 无参数更新） [src: abs]
- [Pathway 说明] RegionFocus 是 visual perception 方法，不是 experience transformation。transformation 语义较弱。  [src: inferred]

---

#### [新增] Self-Distillation Enables Continual Learning (SDFT) — 重复条目
- [备注] 此条目与前面 P5 节 [新增] Self-Distillation Fine-Tuning 为同一论文（arxiv 2601.19897）。此处保留仅为标记 abstracts 覆盖完整性。正文定稿时合并。  [src: inferred]

---

### Group B: Benchmarks & Datasets（非 transformation 方法，标注说明）

以下论文主要贡献为 benchmark / dataset / evaluation protocol，不作为 experience transformation 方法纳入 pathway 分类。

---

- **Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory** — benchmark for evaluating self-evolving memory in LLM agents（streaming benchmark, 10+ memory modules, 10 datasets）。提供 ExpRAG baseline 和 ReMem pipeline。不纳入 pathway 分类。
- **How Well Do Agentic Skills Work in the Wild** — benchmark study of skill usage in realistic settings（34K real-world skills, 7 agent-model configs, 7308 trajectories）。分析 skill benefits degradation。不纳入 pathway 分类。
- **How Well Does Agent Development Reflect Real-World Work?** — analysis of 43 benchmarks and 72,342 tasks against US labor market。agent development alignment study。不纳入 pathway 分类。
- **ScienceWorld: Is your Agent Smarter than a 5th Grader?** — interactive text environment benchmark for scientific reasoning。不纳入 pathway 分类。
- **SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks** — benchmark of 86 tasks across 11 domains with curated Skills and deterministic verifiers。不纳入 pathway 分类。
- **SpreadsheetBench: Towards Challenging Real World Spreadsheet Manipulation** — benchmark of 912 real spreadsheet questions from online Excel forums。不纳入 pathway 分类。
- **SWE-Skills-Bench: Do Agent Skills Actually Help in Real-World Software Engineering?** — benchmark isolating marginal utility of agent skills in SWE（49 skills, 565 task instances）。不纳入 pathway 分类。
- **WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents** — simulated e-commerce website environment（1.18M products, 12K instructions）。不纳入 pathway 分类。

---

### Group C: General Methods — Out of Scope for Experience Transformation（标注排除理由）

以下论文的核心贡献不在 agent experience transformation 范围。简要说明排除理由。

---

- **Compositional Semantic Parsing on Semi-Structured Tables** — 2015 年 semantic parsing 工作，远早于 LLM-based agent 范式。排除。
- **DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via RL** — 通用 LLM reasoning RL 训练（DeepSeek-R1）。虽然是许多 agent 工作的 base model，但其本身不涉及 agent-environment 交互经验的转化。排除。
- **Fine-Tuning Vision-Language-Action Models** — 已在 Group A 标注，此处仅说明：其核心是 VLA fine-tuning 策略的 ablation study，非经验转化方法本身。
- **Focused Transformer: Contrastive Training for Context Scaling** — context length extension via contrastive training（LongLLaMA）。不涉及 agent experience。排除。
- **Language Agents as Optimizable Graphs** — 已作为 GPTSwarm 在 P2 节标注。此处避免重复。
- **Let's Verify Step by Step** — PRM training methodology（PRM800K dataset）。foundational work for process reward models，但不直接涉及 agent experience transformation。在 P4 pathway 讨论中作为 foundational reference 引用。排除独立标注。
- **Memorizing Transformers** — kNN-augmented language model for memorization at inference time。不涉及 agent decision-making experience。排除。
- **OpenVLA: An Open-Source Vision-Language-Action Model** — base VLA model（7B, 970K robot demonstrations）。foundational model，不是 experience transformation 方法。排除独立标注（Fine-Tuning VLA Models 已在 Group A 标注）。
- **Reflection-Driven Self-Optimization 6G Agentic AI RAN** — domain-specific（6G radio access networks）。虽然使用了 reflection-driven self-optimization，但应用场景过于专域。排除。
- **ScreenLLM: Stateful Screen Schema for Efficient Action Understanding and Prediction** — GUI state representation model。是 perception/representation 方法而非经验转化。排除。
- **Self-evolving Embodied AI** — survey paper，定义 self-evolving embodied AI 范式。作为 related work reference，不纳入 pathway 分类。
- **Externalization in LLM Agents: A Unified Review** — survey paper on externalization in LLM agents。作为 related work reference，不纳入 pathway 分类。
- **Tree of Thoughts: Deliberate Problem Solving with Large Language Models** — general reasoning framework（ToT）。不涉及 agent 跨任务经验积累。排除。
- **VLM-R1: A Stable and Generalizable R1-style Large Vision-Language Model** — general VLM RL training framework。不特定于 agent experience。排除。
- **Vision-R1: Evolving Human-Free Alignment in LVLMs via Vision-Guided RL** — general LVLM alignment via RL。不特定于 agent experience。排除。

---
