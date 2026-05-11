---
name: exp-transform-annotator
description: "Annotate Title/URL/Abstract markdown paper lists for the CSUR Experience Transformation survey: decide scope, assign Carrier and Pathway labels, identify source/target experience, modality, experience source, utilization, method, and mechanism. Use for 批量打标签, Pathway 归属, experience transformation 标注, carrier 体系归类, taxonomy 底稿, paper abstract annotation, P1–P7 分类, or out-of-scope screening for this survey."
---

# Experience-Transformation Paper Annotation

将 Title/URL/Abstract 三段式 markdown 论文清单批量标注为本 Survey 的结构化字段。只根据 Abstract 可直接支持的信息下判断；缺失信息写 `不清楚`，不要臆测、扩写或为了凑字段强行归类。

## Mandatory Context Refresh

Before any annotation in this repository, read these files again:

1. `CLAUDE.md` for repository access restrictions and writing expectations.
2. `Project_Infos.md` for the latest Experience / Carrier / Transformation definitions, scope rules, 7 known pathways, and composite-pipeline policy.
3. `Notions.md` for notation: `N-Tok`, `S-Tok`, `Lat`, `π-Par`, `V-Par`, modality/source/method tags, and P1–P7 labels.

Follow `CLAUDE.md` strictly. Do not read unrelated project folders unless the user or these instructions explicitly require them.

## Python Environment

Use the project conda Python:

```bash
/Users/lingshuai/opt/anaconda3/envs/cc/bin/python
```

## Workflow

### 1. Parse Input

Use the bundled parser:

```bash
/Users/lingshuai/opt/anaconda3/envs/cc/bin/python .codex/skills/exp-transform-annotator/scripts/parse_papers.py <input.md>
```

The parser reads Title/URL/Abstract markdown blocks separated by lines of 3+ dashes and prints JSON:

```json
{
  "count": 2,
  "papers": [
    {"index": 1, "title": "...", "url": "...", "abstract": "..."}
  ],
  "errors": [{"block": 3, "reason": "..."}]
}
```

If `errors` is non-empty, keep them for the final `Parser Errors` section and continue annotating valid `papers`.

### 2. Annotate Each Paper

For every parsed paper, apply the Pathway decision process below and emit one annotation block. Separate blocks with one blank line.

Core discipline:

- Judge scope first. If a paper is out of scope after careful analysis, mark it as out of scope and give the reason. Do not force a Pathway label.
- Only annotate what the abstract supports. If the abstract does not identify a field, write `不清楚`.
- Use current Carrier terms: `Narrative`, `Schematic`, `Latent`, `Policy`, `Evaluator`.
- Old terms such as Textual, Structured, and Multimodal Raw may appear only when quoting or explaining paper wording.

### 3. Write Output

- If the user provides an output path, write there.
- If the user does not provide an output path, write beside the input file using:

```text
<input_basename>_gpt5.5_annotated.md
```

Example: `/path/to/papers.md` -> `/path/to/papers_gpt5.5_annotated.md`.

### 4. Append Optional Sections

At the end of the output file, append only the non-empty sections:

```text
## New Tags Introduced
- ⟨RL: XXX⟩ —— 一句话定义；首次出现：「<论文标题>」

## Annotation Failures
- 「<论文标题>」（block #N）—— 失败原因

## Parser Errors
- block #N —— <parser 报告的原因>
```

## Output Template

Use this exact field order for in-scope papers:

```text
[Title]: <论文完整标题>
- [Pathway]: <X → Y> 或 <X → Y → Z>，若命中 P1–P7 末尾标 (Pn)
- [Source Experience]: <源端经验的具体形式>
- [Target Experience]: <目标端经验的具体形式>
- [Source Modality]: <[txt] / [vis+txt] / [GUI] / [embodied] / [cross-modal] 或新模态>
- [Target Modality]: <同上>
- [Experience Source]: <{self} / {human} / {teacher} 之一或组合>
- [Utilization]: <转化后经验如何被复用；摘要未明示则写 "不清楚">
- [Method]: <⟨LLM-extract⟩ / ⟨SFT⟩ / ⟨RL: GRPO/PPO/DPO/ReST⟩ / ⟨MCTS⟩ / ⟨hybrid⟩ 或新方法>
- [Mechanism]: <源经验通过什么具体过程变成目标经验>
```

For out-of-scope papers, use the short block:

```text
[Title]: <论文完整标题>
- [Pathway]: Out of Scope
- [Mechanism]: <一句话说明排除理由，并对应 Project_Infos.md §3.2 的排除类型或边界原因>
```

For failed annotations where the abstract is too thin or ambiguous:

```text
[Title]: <论文完整标题>
- [Pathway]: Annotation Failed
- [Mechanism]: <失败原因>
```

## Field Rules

`[Pathway]`:

- X, Y, Z must come from `{Narrative, Schematic, Latent, Policy, Evaluator}`.
- Use `X → Y` for direct single-step transformation.
- Use `X → Y → Z` only when the paper's main contribution is the linked pipeline and the intermediate carrier is part of the method.
- If the path matches P1–P7, append `(Pn)`.
- If it is a new path, do not invent a P number. Explain why known pathways do not cover it in `[Mechanism]`.

`[Source Experience]` and `[Target Experience]`:

- Prefer concrete nouns from the abstract, such as raw trajectories, reflections, skill library, workflow, KV cache, reward model, verifier, policy weights, or synthetic demonstrations.
- Do not add a carrier object that the abstract does not mention or imply through method details.

`[Source Modality]` and `[Target Modality]`:

- Prefer tags from `Notions.md`: `[txt]`, `[vis+txt]`, `[GUI]`, `[embodied]`, `[cross-modal]`.
- Add a new modality tag only when the existing tags would lose essential information.

`[Experience Source]`:

- Prefer `{self}`, `{human}`, `{teacher}`.
- Use comma-separated combinations for mixed sources, e.g. `{self}, {human}`.
- If the source is not clear, write `不清楚`.

`[Utilization]`:

- State how the transformed experience is reused: prompt prefix, RAG memory, SFT data, RM scoring signal, RL feedback, workflow execution, benchmark construction, etc.
- If the abstract does not say, write `不清楚`.

`[Method]`:

- Prefer `Notions.md` tags: `⟨LLM-extract⟩`, `⟨SFT⟩`, `⟨RL: GRPO⟩`, `⟨RL: PPO⟩`, `⟨RL: DPO⟩`, `⟨RL: ReST⟩`, `⟨MCTS⟩`, `⟨hybrid⟩`.
- Single method: `⟨X⟩`.
- Clear staged methods: `⟨X⟩, ⟨Y⟩`, with stages bound in `[Mechanism]`.
- Three or more interwoven methods, or hard-to-separate method mixtures: use `⟨hybrid⟩` and list the components in `[Mechanism]`.

`[Mechanism]`:

- Explain the transformation process, not just the topic.
- For `⟨LLM-extract⟩`, describe extraction signals such as reflection trigger, filtering rule, iteration loop, or summarization target.
- For training methods, name the supervision signal and objective when the abstract supports it.
- For composite paths, break down stages and map each stage to known P labels, e.g. `Stage 1 对应 P2；Stage 2 对应 P5`.
- If a new tag is introduced, add a quote block immediately after `[Mechanism]`:

```text
> New tag: <标签名> — <一句话定义；说明为何既有标签不足以覆盖>
```

## Pathway Decision Process

### 1. Scope Check

A paper is in scope only if it satisfies both:

- It contains decision-process semantics mappable to `e=(c,a,o,f)`.
- The action belongs to a heterogeneous LLM-based agent action space: reasoning traces, tool calls, planning decomposition, environment control, multi-agent communication, GUI actions, embodied actions, etc.

Mark `[Pathway]: Out of Scope` when the abstract indicates one of these exclusion cases:

- Static-corpus pretraining with no decision-process semantics.
- Single-step classification or annotation SFT with no heterogeneous action space.
- Pure Parametric → Parametric distillation where the experience semantic chain is broken.
- Pure image classification or visual foundation-model training with no sequential decision semantics.
- Non-LLM-based systems such as traditional RL, unless the abstract clearly frames an LLM-based agent.
- Any other case that fails the two inclusion criteria after careful analysis.

For out-of-scope papers, output only `[Title]`, `[Pathway]: Out of Scope`, and `[Mechanism]` with the reason.

### 2. Identify Source Carrier

Classify the consumed input:

- Natural-language logs, reflections, screenshot/video sequences, interaction logs, hints, rules, skill descriptions, strategies, insights -> `Narrative`.
- Code, workflows, SOPs, API specs, graphs, typed skill libraries, procedural templates, routines -> `Schematic`.
- KV cache, prefix cache, soft prompts, continuous memory tokens, activation memory -> `Latent`.
- LLM/VLA/GUI-agent weights, LoRA adapters, actor policy weights -> `Policy`.
- Reward models, PRMs, verifiers, critics, judges -> `Evaluator`.

Frequent pitfalls:

- Workflow / SOP / routine / procedural template / pipeline counts as `Schematic` even if it is written in natural language, because the carrier is organized as an executable or topological procedure.
- Rule / guideline / hint / skill description / strategy / insight remains `Narrative` unless the abstract states explicit syntax, topology, execution, or parsing constraints.
- Embeddings used only as retrieval indices for tokenized memory do not count as `Latent`; classify the retrieved content's carrier.

### 3. Identify Target Carrier

Use the same carrier table for the produced object. Focus on the new reusable experience carrier, not incidental evaluation metrics or datasets unless dataset construction is the target transformation.

### 4. Decide Single-Step, Composite, or Multi-Target

- Direct source-to-target transformation -> annotate the main `X → Y`.
- Linked method where a middle carrier is essential -> annotate `X → Y → Z` and stage the mechanism.
- Multiple independent outputs from one source -> annotate the main path in `[Pathway]`; list secondary branches in `[Mechanism]` with P labels where possible.
- If the current policy generates rollouts that are fed back to train the same policy, prefer `Policy → Narrative → Policy` over pure P7.
- If the paper trains an evaluator and then trains a policy using that evaluator, prefer `Narrative → Evaluator → Policy` over single-step P6.

### 5. Attach Known P Labels

| Label | Pathway | Shorthand |
| --- | --- | --- |
| P1 | Narrative → Narrative | raw -> reflection / rule / insight / skill |
| P2 | Narrative → Schematic | logs -> code / workflow / graph |
| P3 | Tokenized → Latent | tokens -> KV cache / soft prompt |
| P4 | Tokenized → Parametric (Evaluator) | trajectories -> RM / PRM / verifier |
| P5 | Tokenized → Parametric (Policy) | trajectories -> policy via SFT/RL |
| P6 | Parametric (Evaluator) → Parametric (Policy) | RM signal -> policy via RLHF/DPO |
| P7 | Parametric → Tokenized | weights -> synthetic trajectories / demonstrations |

Use `Narrative` or `Schematic` in the output path when the tokenized subtype is knowable. For P3/P4/P5, `Tokenized` in the table may be rendered as `Narrative` or `Schematic` if the abstract identifies the subtype.

## Open Vocabulary Discipline

`Notions.md` is an open dictionary, not a closed enum. Add tags only under these rules:

1. Reuse existing tags whenever possible.
2. Add only within existing dimensions: Modality, Source, Method, or Pathway.
3. Keep syntax consistent: `[modality]`, `{source}`, `⟨method⟩`.
4. Do not create synonyms of existing tags.
5. Mark the first use with `> New tag: ...` and summarize it in `## New Tags Introduced`.

## Failure Handling

- Parser errors do not stop the run. Report them at the end.
- If one paper lacks enough abstract evidence for source/target/pathway, mark it `Annotation Failed` and keep processing.
- Failed or out-of-scope annotations are better than unsupported pathway labels.

## Minimal Example

```text
[Title]: Training-Free Group Relative Policy Optimization
- [Pathway]: Narrative → Narrative (P1)
- [Source Experience]: Raw interaction rollouts / raw trajectories
- [Target Experience]: Experiential knowledge / rules
- [Source Modality]: [txt]
- [Target Modality]: [txt]
- [Experience Source]: {self}
- [Utilization]: 作为 learned token prior 在 LLM API 调用时集成，用于 guide model behavior
- [Method]: ⟨LLM-extract⟩
- [Mechanism]: 不更新 LLM 参数，而是通过多轮 rollout、组内语义相对比较和自我反思，把成功 / 失败经验蒸馏成自然语言经验库；经验库再作为 prompt / token prior 注入模型。
```
