# 目标

创建一个名为 `arxiv-tex-downloader` 的 skill，用于根据用户输入下载 arXiv 论文的 TeX 源码。

# 支持的输入形式

该 skill 需要识别并处理以下四种输入：

1. **arXiv 论文 ID**：如 `2501.12485`
2. **arXiv 论文 URL**：如 `https://arxiv.org/abs/2501.12485` 或 `https://arxiv.org/pdf/2501.12485.pdf`
3. **Markdown 文件**：包含一个 arXiv 论文列表，每行一篇论文，每行格式为论文 ID 或论文 URL（即上述第 1、2 种形式之一）
4. **CSV 文件**：包含多列，其中必有 `Title` 和 `URL` 两列

# 各输入形式的处理逻辑

## 形式 1、2、3（ID / URL / Markdown）

直接从输入中提取 arXiv 论文 ID，然后下载对应论文的 TeX 源码。

## 形式 4（CSV 文件）

CSV 文件的处理较为复杂，按以下步骤进行：

1. **逐行判断 `URL` 列是否为 arXiv 链接**：
   - 判断标准：`URL` 字符串中是否包含子串 `arXiv`。
   - 包含 `arXiv` 的链接一般形如 `https://doi.org/10.48550/arXiv.2409.07429`，其中 `2409.07429` 即为 arXiv 论文 ID，可直接从链接中提取。
   - 不包含 `arXiv` 的链接形式多样（例如指向会议页面的链接），无法直接提取 ID。

2. **处理不含 `arXiv` 的链接**：
   - 这类论文大概率仍存在于 arXiv 上（`URL` 可能只是会议链接）。
   - 此时改用 `Title` 列的标题在 arXiv 上检索该论文，若检索到，提取其 arXiv 论文 ID。

3. **下载与记录**：
   - 对所有能在 arXiv 上找到的论文，下载其 TeX 源码。
   - 对所有**无法**在 arXiv 上找到的论文，将其 `Title` 写入一个 Markdown 文件，每篇论文占一行。该文件与输入的 CSV 文件位于同一目录，文件名为 `{csv_file_name}_not_found_in_arxiv.md`。

# 下载与解压流程

对每一篇确定了 arXiv ID 的论文：

1. 从 arXiv 下载 TeX 源码，通常为一个 `.tar.gz` 压缩包。
2. 将压缩包/解压后的文件夹命名为该论文的标题。**注意**：必须对标题中的特殊字符进行清洗，确保文件名符合 macOS 的命名规则（例如去除或替换 `/`、`:`、换行符等非法字符）。
3. 解压压缩包，**只保留 TeX 文件（`.tex`）和图片文件（如 `.png`、`.jpg`、`.jpeg`、`.pdf`、`.eps` 等），删除其余所有文件**。
4. 处理完成后，该论文对应的 TeX 文件夹应存放在：
   `/Users/lingshuai/Projects/AgentProjects/CSUR_ExpTransfer/AgentData/PaperTexs`
5. 原始的 `.tar.gz` 压缩包无需保留，处理完成后删除。

# 技术约束

1. **Python 环境**：如需运行 Python 代码，使用环境 `/Users/lingshuai/opt/anaconda3/envs/cc`，该环境已包含所有所需的 Python 包，无需额外安装。
2. **优先使用脚本**：凡是能通过脚本（如 Python、Shell）确定性实现的操作，一律用脚本实现，不要依赖手动操作或让模型按自身理解临时处理，以减少不确定性。
3. **脚本拆分原则**：脚本应当模块化，尽量做到每个脚本只完成一个独立功能（例如：输入解析、ID 提取、arXiv 检索、源码下载、解压与清洗等各为一个脚本），不要用一个大而全的脚本完成所有功能。这样便于单独调试、复用和排查问题。


这个 skill 只为当前项目所用，保存在当前项目的 `.codex/skills`

在创建这个 skill 的过程中，可以遵循下面的 guidelines：

```
Behavioral guidelines to reduce common LLM coding mistakes. Merge with project-specific instructions as needed.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

---

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.
```