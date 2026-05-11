---
name: translate-abstracts
description: Translate English paper abstracts to Chinese from a markdown file by calling Codex CLI once per paper and assembling a bilingual markdown output. Use whenever the user wants to translate academic paper abstracts, convert English abstracts to Chinese, add Chinese translations to a paper collection, or process a Title/URL/Abstract formatted paper list. Triggers on "translate abstracts", "翻译摘要", "翻译论文摘要", "英译中", "add Chinese translation to papers", "翻译成中文", or when given a paper list file needing Chinese translation.
---

# Abstract Translation via Codex CLI

Translate English paper abstracts to Chinese by running `codex exec` from the terminal. Do not use subagents for translation. Make exactly one Codex CLI call per paper.

## Input Format

A markdown file where each paper block follows this exact structure:

```
Title: {paper title}

URL: {paper url}

Abstract: {english abstract text}

------

```

- Papers are delimited by `------` (4+ dashes on a line by itself, surrounded by blank lines)
- Title, URL, Abstract fields each start the line with the field name followed by `:` and a space
- The Abstract field may span multiple lines or paragraphs
- The file may contain any number of papers

## Output Format

A new file `{original_name}_en+cn.md` saved to the **same directory** as the input file:

```
Title: {paper title}

URL: {paper url}

Abstract: {english abstract text}

中文翻译：{chinese translation}

------

```

Preserve every original paper block. Add `中文翻译：` immediately after the Abstract field, containing the full Chinese translation. Keep paper order the same as the input file.

## Workflow

### 1. Parse the input

Read the entire input markdown file. Split papers by separator lines containing 4+ dashes. For each block, extract `Title`, `URL`, and `Abstract`.

Use the bundled `scripts/parse_papers.py` for reliable parsing:

```bash
/Users/lingshuai/opt/anaconda3/envs/cc/bin/python .codex/skills/translate-abstracts/scripts/parse_papers.py <input_file>
```

This outputs a JSON array of paper objects with `index`, `title`, `url`, `abstract`, and `raw_block`. The `raw_block` field is used to preserve the original Title/URL/Abstract text when assembling the output.

If the script is unavailable or the format is slightly irregular, parse manually: split on `\n------\n` and use regex `^Title:\s*(.+)$`, `^URL:\s*(.+)$`, `^Abstract:\s*(.+)$` (with `re.DOTALL` for Abstract) to extract fields.

### 2. Run one Codex CLI call per paper

Prefer the bundled runner:

```bash
/Users/lingshuai/opt/anaconda3/envs/cc/bin/python .codex/skills/translate-abstracts/scripts/translate_with_codex.py <input_file>
```

Useful options:

- `--output <path>`: set the output file path; default is `{original_name}_en+cn.md`
- `--model <model>`: default `gpt-5.4-mini`
- `--reasoning-effort <effort>`: default `low`
- `--limit <n>`: translate at most `n` new papers in this run, useful for staged/resumable batches
- `--workdir <dir>`: override the isolated working directory passed to `codex exec`; default is a system temporary directory
- `--force`: ignore cached per-paper translations and retranslate
- `--dry-run`: parse input and print the first Codex prompt without calling Codex

The runner:

- creates `.translate_abstracts_state/<input_stem>/` next to the input file
- stores per-paper logs under `logs/`
- stores successful per-paper translations under `translations/`
- resumes by skipping papers whose translation file already exists
- retries rate-limit or quota-like failures with exponential backoff
- assembles all available translations in original input order
- starts each child `codex exec` from an isolated temporary directory by default, so the child translator does not load project-level `AGENTS.md`, `CLAUDE.md`, or other repository context

For each paper, the runner calls:

```bash
codex exec \
  -s workspace-write \
  -m "$MODEL" \
  -c 'approval_policy="never"' \
  -c "model_reasoning_effort=\"$REASONING_EFFORT\"" \
  -C "$WORKDIR" \
  --skip-git-repo-check \
  "$PROMPT"
```

### 3. Manual per-paper prompt template

If the runner cannot be used, call `codex exec` once per paper and use this prompt shape:

```text
You are translating one English academic paper abstract into Chinese.

Return exactly one tagged block:
<TRANSLATION>
Chinese translation text only
</TRANSLATION>

RULES:
- Translate the full abstract faithfully; do not summarize, omit, or add content.
- Return only the Chinese translation inside the tags. Do not include Title, URL, Abstract, commentary, bullets, or code fences.
- Use natural Chinese academic prose for CS survey writing.
- Preserve all LaTeX math, code identifiers, URLs, and arXiv IDs exactly.
- Keep English acronyms and model names as-is, including LLM, RLHF, RAG, GPT, BERT, LLaMA, CLIP, ViT, GPU, API.

TRANSLATION QUALITY:
- Use standard Chinese academic CS terminology:
  - transformer → Transformer, attention → 注意力, fine-tuning → 微调
  - embedding → 嵌入, reinforcement learning → 强化学习
  - latent space → 潜空间, token → token, prompt → prompt
  - retrieval-augmented → 检索增强, chain-of-thought → 思维链
- Keep English acronyms AS-IS: LLM, RLHF, RAG, BERT, GPT, GPU, API
- Preserve ALL LaTeX math ($...$, $$...$$) and URLs exactly
- Translate faithfully — do not summarize, omit, or add content
- Read as natural Chinese academic prose, not stiff literal translation
- Match the formal/professional tone of the original

Title:
{paper title}

Abstract:
{english abstract}
```

Strip the `<TRANSLATION>` tags before inserting the result into the final markdown.

### 4. Assemble

For each successful paper, write:

```text
{raw original paper block}

中文翻译：{Chinese translation}

------
```

Write the assembled result to `{original_name}_en+cn.md` in the same directory as the input file unless the user specifies another path.

### 5. Report summary

Tell the user:
- How many papers were translated
- Output file path
- State/log directory path
- Any papers that failed or are still missing translations

## Translation Quality Reference

### Standard CS Term Translations

| English | 中文 |
|---------|------|
| large language model (LLM) | 大语言模型 |
| agent / LLM agent | 智能体 / LLM 智能体 |
| memory system | 记忆系统 |
| tool use / tool calling | 工具使用 / 工具调用 |
| attention mechanism | 注意力机制 |
| transformer | Transformer |
| fine-tuning | 微调 |
| pre-training | 预训练 |
| reinforcement learning | 强化学习 |
| supervised fine-tuning (SFT) | 监督微调 |
| RLHF (RL from human feedback) | 基于人类反馈的强化学习 |
| chain-of-thought (CoT) | 思维链 |
| embedding / representation | 嵌入 / 表征 |
| latent space | 潜空间 |
| tokenization | 分词 |
| inference | 推理 |
| retrieval-augmented generation (RAG) | 检索增强生成 |
| knowledge graph | 知识图谱 |
| prompt engineering | 提示工程 |
| zero-shot / few-shot | 零样本 / 少样本 |
| hallucination | 幻觉 |
| multimodal | 多模态 |
| benchmark / dataset | 基准 / 数据集 |
| baseline | 基线 |
| state-of-the-art (SOTA) | 当前最优 |
| ablation study | 消融实验 |
| generalization | 泛化 |

### Hard Rules

- **Never translate** acronyms that are proper nouns or model names: GPT, BERT, LLaMA, CLIP, ViT, ResNet
- **Never translate** mathematical notation, LaTeX, or code identifiers
- **Never alter** URLs or arXiv IDs
- **Never summarize** — translate the full abstract, every sentence
- If a term has no established Chinese equivalent, keep the English and optionally add Chinese explanation in parentheses on first occurrence
