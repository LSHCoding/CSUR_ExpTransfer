---
name: arxiv-tex-downloader
description: Download arXiv paper TeX source files for this project. Use when Codex needs to process an arXiv paper ID, arXiv abs/pdf/e-print URL, Markdown paper list, or CSV file with Title and URL columns, then fetch source archives, extract TeX/image assets, and save cleaned folders under the project PaperTexs directory.
---

# arXiv TeX Downloader

## Overview

Use the bundled scripts to deterministically parse inputs, find arXiv IDs, download source archives, unpack them, and keep only `.tex` plus image assets. Do not manually parse paper lists or hand-edit downloaded trees when a script can do it.

Run all Python scripts with:

```bash
/Users/lingshuai/opt/anaconda3/envs/cc/bin/python
```

The default output directory is:

```text
/Users/lingshuai/Projects/AgentProjects/CSUR_ExpTransfer/AgentData/PaperTexs
```

## Primary Workflow

From this skill directory, run the dispatcher:

```bash
/Users/lingshuai/opt/anaconda3/envs/cc/bin/python scripts/run.py "<input>"
```

Accepted inputs:

- arXiv ID, e.g. `2501.12485`
- arXiv URL, e.g. `https://arxiv.org/abs/2501.12485` or `https://arxiv.org/pdf/2501.12485.pdf`
- Markdown or text file containing one arXiv ID or URL per non-empty line
- CSV file containing exact `Title` and `URL` columns

The dispatcher prints JSON with downloaded folders, skipped existing folders, and counts. Before downloading, `scripts/download_one.py` checks the output directory for an existing folder whose normalized name matches the paper title; if found, it returns `skipped_existing: true` and does not download. Use `--overwrite` only when the user explicitly wants existing output folders replaced.

## Existing Output Detection

Use `scripts/title_match.py` for reusable title matching:

```bash
/Users/lingshuai/opt/anaconda3/envs/cc/bin/python scripts/title_match.py --title "A/B: C?" --candidate "A B C"
/Users/lingshuai/opt/anaconda3/envs/cc/bin/python scripts/title_match.py --title "A/B: C?" --paper-tex-dir /Users/lingshuai/Projects/AgentProjects/CSUR_ExpTransfer/AgentData/PaperTexs
```

The script prints JSON. Compare mode returns `match`; scan mode returns `exists`, `directory`, and `matched_name`.

Normalization rules:

- HTML-unescape the title.
- Remove the downloader's numeric duplicate suffix such as ` [2]`.
- Apply Unicode NFKD normalization and casefolding.
- Keep only alphanumeric characters; drop punctuation, symbols, whitespace, path separators, and combining marks.

This handles the filename-cleaning gap because characters like `:`, `/`, `?`, repeated whitespace, and case differences disappear on both sides before comparison.

## CSV Rules

For CSV input, use `scripts/process_csv.py` through `scripts/run.py` unless debugging a CSV-specific problem.

The CSV logic is:

1. Require exact `Title` and `URL` columns.
2. If `URL` contains `arxiv` case-insensitively, extract the arXiv ID directly from the URL.
3. If no arXiv ID is extracted, search arXiv by `Title` and accept the best match only when the title similarity score is at least `--min-score` (default `0.82`).
4. Download every found paper.
5. Write unfound paper titles to `{csv_stem}_not_found_in_arxiv.md` next to the CSV, one Markdown bullet per title.
6. When a later retry successfully downloads a paper, remove that title from matching `*_search_failed.md` files. This includes failure files next to the retry CSV and the project default `AgentData/Data/PaperMetaInfos` directory, so temporary retry CSVs can clean up the original batch failure log.

The default `--search-delay 3.0` is intentional for arXiv API politeness. Lower it only for controlled local tests.

## Script Map

- `scripts/extract_arxiv_id.py`: extract one normalized arXiv ID from text, DOI, or URL.
- `scripts/title_match.py`: normalize titles, compare title keys, and scan existing paper folders.
- `scripts/parse_input.py`: classify a single user input and parse Markdown/text lists.
- `scripts/search_arxiv_by_title.py`: query arXiv by paper title and return a scored best match.
- `scripts/download_source.py`: download one arXiv source payload from `/e-print/<id>`.
- `scripts/unpack_source.py`: safely unpack tar/gzip/single-file source payloads.
- `scripts/clean_tex_tree.py`: remove every extracted file except `.tex` and image assets.
- `scripts/download_one.py`: compose download, unpack, clean, and title-based folder naming for one ID.
- `scripts/process_csv.py`: implement the CSV-specific URL/title-search workflow.
- `scripts/run.py`: top-level dispatcher to use for normal requests.
- `scripts/self_test.py`: offline validation for parsing, title sanitizing, unpacking, and cleaning.

## Validation

Before relying on script changes, run:

```bash
/Users/lingshuai/opt/anaconda3/envs/cc/bin/python -m compileall scripts
/Users/lingshuai/opt/anaconda3/envs/cc/bin/python scripts/self_test.py
```

If a live download, title search, or default output-directory write fails due to network or sandbox permissions, request the required approval and rerun the same command rather than replacing the script workflow with manual steps.
