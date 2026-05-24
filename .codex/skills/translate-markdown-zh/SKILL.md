---
name: translate-markdown-zh
description: Translate English Markdown files or folders into Chinese bilingual copies. Use when Codex is asked to translate .md content, add Chinese translations to Markdown, process a Markdown folder, or create *_zh_cn.md files while preserving the original text, document structure, tables, references, table of contents, citation keys, and technical terms.
---

# Translate Markdown Zh

## Overview

Translate English Markdown into Chinese by creating a new bilingual Markdown file next to each source file. Keep every original line read-only and insert Chinese translations after the relevant headings, paragraphs, and tables.

## Workflow

1. Resolve input targets:
   - If the user gives a file, process that Markdown file.
   - If the user gives a folder, process all `.md` files in that folder recursively unless the user asks for top-level only.
   - Skip files already named `*_zh_cn.md`.
2. Read the source file and identify non-translatable ranges:
   - A file-opening table of contents, usually headed `Table of Contents`, `Contents`, or made of Markdown links to headings.
   - A file-ending references section starting at a heading such as `References`, `Bibliography`, or `Works Cited`.
   - Fenced code blocks, math blocks, raw HTML blocks, URLs, paths, identifiers, citation keys, and Markdown syntax.
3. Create the output file in the same directory using `{original_stem}_zh_cn.md`.
4. Preserve the entire original file exactly, in the same order. Insert only new translation content.
5. Validate the result with `scripts/validate_translation.py`.

Use the project Python interpreter when running scripts in this repository:

```bash
/Users/lingshuai/opt/anaconda3/envs/cc/bin/python .codex/skills/translate-markdown-zh/scripts/validate_translation.py path/to/source.md
```

## Translation Rules

- Translate prose paragraphs that are normal body text.
- Translate headings outside the opening table of contents and ending references section. Insert the translated heading after the original heading with one blank line between English and Chinese.
- Do not translate the file-opening table of contents or the file-ending references list.
- Preserve citation markers exactly, including forms like `[Xu26e]`, `\[Xu26e\]`, `[Xu et al., 2026]`, and parenthetical citation groups.
- Translate common technical concepts into Chinese. Do not leave broad technical phrases in English merely because they are common in papers.
- Keep English only for the small set that is awkward or unsafe to translate: model names, dataset names, method/system names, acronyms, equations, code identifiers, file paths, URLs, command names, and exact citation keys.
- Keep English under 5% of the inserted Chinese translation text, excluding preserved citation keys, URLs, equations, and code.
- Use a "translate by default" policy for terminology. When a term has a natural Chinese academic rendering, translate it even if the source paper uses English.
- Keep inline Markdown syntax intact: emphasis, links, inline code, math, footnote markers, and citation brackets must remain valid.
- Do not rewrite, polish, shorten, reorder, or delete the English source.

## Chinese Quality Bar

- The inserted translation must read as Chinese academic prose, not as a mixed English-Chinese gloss.
- Avoid sentence patterns where half of the content words remain English.
- Translate multi-word technical phrases as a unit when possible.
- Keep English for names and brittle identifiers, not for ordinary concepts.
- If the translated paragraph visually looks close to half English, revise it before saving.

Examples of terms that should normally be translated:

- `single carrier`: 单一载体
- `perceptual memory`: 感知记忆
- `cognitive memory`: 认知记忆
- `latent perception memory`: 隐空间感知记忆
- `latent thinking memory`: 隐空间思维记忆
- `one-token procedural memory`: 单 token 程序性记忆
- `compact reusable procedures`: 紧凑的可复用过程
- `decomposition and adaptation`: 分解与适配
- `small latent consolidator`: 小型隐空间整合器
- `semantic memory`: 语义记忆
- `perceptual residue`: 感知残留
- `division of labor`: 分工关系

## Default Terminology

Prefer these Chinese renderings unless the local context clearly needs another wording:

- `experience`: 经验
- `transformation`: 转化
- `carrier`: 载体
- `single carrier`: 单一载体
- `trajectory`: 轨迹
- `trace`: 轨迹记录
- `policy`: 策略
- `base policy`: 基础策略
- `evaluator`: 评估器
- `verifier`: 验证器
- `judge`: 裁判器
- `reward model`: 奖励模型
- `latent`: 隐空间
- `latent memory`: 隐空间记忆
- `tokenized`: token 化
- `parametric`: 参数化
- `rollout`: 采样轨迹
- `replay`: 回放
- `feedback`: 反馈
- `supervision`: 监督信号
- `credit assignment`: 信用分配
- `warm-start`: 暖启动
- `cold-start`: 冷启动
- `bootstrapping`: 引导启动
- `self-improvement`: 自我改进
- `self-evolving`: 自演化
- `verification`: 验证
- `ground truth`: 真实标注
- `failure`: 失败样本
- `failure type`: 失败类型
- `failure pattern`: 失败模式
- `repair`: 修复
- `robustness`: 鲁棒性
- `generalization`: 泛化
- `transfer`: 迁移
- `evaluation`: 评估
- `benchmark`: 基准
- `dataset`: 数据集
- `state`: 状态
- `action`: 动作
- `observation`: 观察
- `partial progress`: 部分进展
- `reusable knowledge`: 可复用知识
- `teacher`: 教师模型
- `student`: 学生模型
- `warm-start exploration`: 暖启动探索
- `cold-start scarcity`: 冷启动稀缺

## Heading Handling

- For each translatable heading, keep the original heading line unchanged.
- Insert one blank line, then a Chinese heading using the same Markdown heading level.
- Insert one blank line after the Chinese heading before the next content.
- Translate the heading text fully; do not leave English phrases in translated headings unless they are names, acronyms, or citation-like identifiers.
- Do not translate headings inside the opening table of contents or the ending references section.

## Paragraph Handling

- For each translatable body paragraph, insert the Chinese translation immediately after the original paragraph.
- Keep the original paragraph untouched, including line breaks inside the paragraph.
- Do not add labels such as `Translation:` or `中文：`.
- For list items, keep the original bullet or number line unchanged. Insert the Chinese translation as an indented continuation line under the same item, not as a new bullet or numbered item.
- For blockquotes, preserve the original quoted block and insert the translated quoted block immediately after it using the same quote prefix.

## Table Handling

- Keep the original Markdown table exactly as it appears.
- Insert a complete translated Markdown table immediately after the original table.
- Preserve the same number of columns, row order, alignment row, and Markdown table syntax.
- Translate all human-readable cells, including header cells and row labels.
- Preserve citation keys, code, formulas, numeric values, dataset names, model names, URLs, and identifiers.
- Apply the same low-English rule to table cells; translated tables should read primarily as Chinese.

## Validation

Run the bundled validator after writing each output file or folder:

```bash
/Users/lingshuai/opt/anaconda3/envs/cc/bin/python .codex/skills/translate-markdown-zh/scripts/validate_translation.py path/to/source.md
/Users/lingshuai/opt/anaconda3/envs/cc/bin/python .codex/skills/translate-markdown-zh/scripts/validate_translation.py path/to/folder
```

The validator checks that:

- Every non-generated source file has a corresponding `*_zh_cn.md` output.
- Original lines appear in the translated file unchanged and in order.
- The translated file contains inserted Chinese text.
- Each translatable heading is followed by a Chinese heading at the same level.
- Each detected Markdown table is followed by another Markdown table.
- Inserted translation text stays below the configured English ratio threshold.

If validation fails, fix the output file rather than changing the source file.
