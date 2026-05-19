

### Table 3-1: Narrative → Narrative Works Overview

**功能**:为本子节涉及的工作提供统一索引;正文 prose 只展开关键代表。

**列设计**(6 列):


| 列名                 | 内容                                                                                      | 说明                                                                            |
| ------------------ | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Work**           | 论文引用                                                                                    | 标准 BibTeX key                                                                 |
| **Operation Mode** | Single-pass / Iterative / Multi-trajectory / Multi-agent / Hybrid (Structured Pipeline) | 多模式叠加时逗号分隔;GAAMA / CraniMem 等多步结构化 pipeline 标为 "Hybrid (Structured Pipeline)" |
| **Product Label**  | 论文自身用语(abstract 原始措辞,斜体)                                                                | 不做翻译或归并;此列是把"论文自我命名的多样性"显式留在表格里、而把正文从这一负担中解放的设计                               |
| **Modality**       | `[txt]` / `[vis+txt]` / `[GUI]` / `[embodied]` / `[cross-modal]`                        | §2 Notation 正交属性标签                                                            |
| **Method**         | `⟨LLM-extract⟩` / `⟨SFT⟩` / `⟨RL: ...⟩` / `⟨hybrid⟩`                                    | §2 Notation Method 标签                                                         |


**行组织**:按 Operation Mode 分组(Single-pass → Iterative → Multi-trajectory → Multi-agent → Hybrid),组间 `\midrule`。

**完整条目**(41 行,按 Operation Mode 分组,组间 `\midrule`):

**Single-pass**(10 篇):


| Work                                   | Operation Mode | Product Label                                    | Modality            | Method        |
| -------------------------------------- | -------------- | ------------------------------------------------ | ------------------- | ------------- |
| Reflexion                              | Single-pass    | *reflective text / linguistic feedback*          | [txt]               | ⟨LLM-extract⟩ |
| Dynamic Cheatsheet                     | Single-pass    | *self-curated cheatsheet*                        | [txt]               | ⟨LLM-extract⟩ |
| AgentEHR                               | Single-pass    | *retrospective summary*                          | [txt]               | ⟨LLM-extract⟩ |
| Experiential Reflective Learning / H²R | Single-pass    | *heuristics / hierarchical hindsight reflection* | [txt]               | ⟨LLM-extract⟩ |
| Agent S                                | Single-pass    | *summary / reflection*                           | [vis+txt, GUI]      | ⟨LLM-extract⟩ |
| ELITE                                  | Single-pass    | *self-reflective knowledge*                      | [vis+txt, embodied] | ⟨LLM-extract⟩ |
| Aligning Agentic World Models          | Single-pass    | *heuristic / causal rule / reflection*           | [vis+txt]           | ⟨LLM-extract⟩ |
| GEMS                                   | Single-pass    | *summaries / reflections*                        | cross-modal]        | ⟨LLM-extract⟩ |
| Learn Like Humans                      | Single-pass    | *principle-based and procedural reflection*      | [txt]               | ⟨LLM-extract⟩ |
| Self-Consolidation (N-Sym branch)      | Single-pass    | *contrastive reflection / reusable insights*     | [txt]               | ⟨LLM-extract⟩ |


**Iterative**(1 篇):


| Work                            | Operation Mode | Product Label         | Modality | Method        |
| ------------------------------- | -------------- | --------------------- | -------- | ------------- |
| Iterative Experience Refinement | Iterative      | *shortcut experience* | [txt]    | ⟨LLM-extract⟩ |


**Multi-trajectory**(24 篇):


| Work                                     | Operation Mode   | Product Label                             | Modality       | Method        |
| ---------------------------------------- | ---------------- | ----------------------------------------- | -------------- | ------------- |
| ExpeL                                    | Multi-trajectory | *extracted insights and past experiences* | [txt]          | ⟨LLM-extract⟩ |
| AutoGuide                                | Multi-trajectory | *context-aware guideline*                 | [txt]          | ⟨LLM-extract⟩ |
| JEF-Hinter                               | Multi-trajectory | *context-aware hints*                     | [txt]          | ⟨LLM-extract⟩ |
| WebCoach                                 | Multi-trajectory | *cross-session advice*                    | [vis+txt, web] | ⟨LLM-extract⟩ |
| Trajectory-Informed Memory Generation    | Multi-trajectory | *strategy / recovery / optimization tips* | [txt]          | ⟨LLM-extract⟩ |
| AutoSkill                                | Multi-trajectory | *skill description*                       | [txt]          | ⟨LLM-extract⟩ |
| Contextual Experience Replay             | Multi-trajectory | *skill / dynamic memory*                  | [txt]          | ⟨LLM-extract⟩ |
| Skill Set Optimization                   | Multi-trajectory | *transferable skills*                     | [txt]          | ⟨LLM-extract⟩ |
| EvoTool                                  | Multi-trajectory | *tool-use policy text*                    | [txt]          | ⟨LLM-extract⟩ |
| SkillClaw                                | Multi-trajectory | *collective skill*                        | [vis+txt]      | ⟨LLM-extract⟩ |
| FLEX                                     | Multi-trajectory | *strategy*                                | [txt]          | ⟨LLM-extract⟩ |
| Mem^p (step-by-step instructions branch) | Multi-trajectory | *step-by-step instructions*               | [txt]          | ⟨LLM-extract⟩ |
| Learning Hierarchical Procedural Memory  | Multi-trajectory | *procedural memory*                       | [txt]          | ⟨LLM-extract⟩ |
| Remember Me, Refine Me                   | Multi-trajectory | *procedural memory*                       | [txt]          | ⟨LLM-extract⟩ |
| Learning How to Remember                 | Multi-trajectory | *meta-cognitive memory*                   | [txt]          | ⟨LLM-extract⟩ |
| HiMem                                    | Multi-trajectory | *note memory + episode memory*            | [txt]          | ⟨LLM-extract⟩ |
| MemSkill                                 | Multi-trajectory | *memory skills*                           | [txt]          | ⟨LLM-extract⟩ |
| MemRL                                    | Multi-trajectory | *episodic memory*                         | [txt]          | ⟨LLM-extract⟩ |
| Meta-Policy Reflexion                    | Multi-trajectory | *meta-policy memory*                      | [txt]          | ⟨LLM-extract⟩ |
| ReasoningBank                            | Multi-trajectory | *reasoning strategies*                    | [txt]          | ⟨LLM-extract⟩ |
| ReCreate                                 | Multi-trajectory | *domain patterns*                         | [txt]          | ⟨LLM-extract⟩ |
| SE-Agent                                 | Multi-trajectory | *revised / enhanced trajectories*         | [txt]          | ⟨LLM-extract⟩ |
| R⁴                                       | Multi-trajectory | *4D knowledge database*                   | [vis+txt, 4D]  | ⟨LLM-extract⟩ |
| ICE                                      | Multi-trajectory | *simplified workflows and pipelines*      | [txt]          | ⟨LLM-extract⟩ |


**Multi-agent**(5 篇):


| Work        | Operation Mode                | Product Label                                  | Modality  | Method        |
| ----------- | ----------------------------- | ---------------------------------------------- | --------- | ------------- |
| MAR         | Multi-agent                   | *reflection / feedback*                        | [txt]     | ⟨LLM-extract⟩ |
| XSkill      | Multi-agent                   | *skill (action-level + task-level)*            | [vis+txt] | ⟨LLM-extract⟩ |
| AutoManual  | Iterative, Multi-agent        | *diverse rules → comprehensive manual*         | [txt]     | ⟨LLM-extract⟩ |
| Trace2Skill | Multi-trajectory, Multi-agent | *skill directory*                              | [txt]     | ⟨LLM-extract⟩ |
| MemEvolve   | Multi-trajectory, Multi-agent | *experiential knowledge + memory architecture* | [txt]     | ⟨LLM-extract⟩ |


**Hybrid (Structured Pipeline)**(1 篇):


| Work      | Operation Mode   | Product Label              | Modality | Method        |
| --------- | ---------------- | -------------------------- | -------- | ------------- |
| AutoAgent | Multi-trajectory | *summary / elastic memory* | [txt]    | ⟨LLM-extract⟩ |


> **排除条目**: Training-Free GRPO(归属 P1 vs P5 待定,见 Open Question 2); EvoSkill(归属 N→N vs N→Sch 待定,见 Open Question 3); ProcMEM(Write Plan 归入 §3.2.2 Workflow,移入 Table 3-2)。
>
> **ICE 归属说明**: Taxonomy 将 ICE 归入 P2(N→Sch,产物为 workflow/pipeline),但 Write Plan §3.1.2 将其作为 Mode 3(Multi-trajectory)代表在 N→N 下讨论。本表暂从 Write Plan 归入 Table 3-1,最终归属待确认。

---

