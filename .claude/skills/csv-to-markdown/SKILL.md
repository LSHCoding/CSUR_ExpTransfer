---
name: csv-to-markdown
description: |
  Convert a CSV file of academic papers into a formatted markdown file. Use this skill whenever
  the user provides or mentions a CSV that contains paper metadata (Title, URL, Abstract columns)
  and wants to convert, export, or format it as markdown. Triggers on: "convert CSV to markdown",
  "export papers from CSV", "format CSV as markdown", "generate markdown from paper list",
  or any request involving a CSV with academic paper records and markdown output.
---

# CSV to Markdown Converter

Convert a CSV file containing paper metadata into a markdown file with Title, URL, and Abstract entries.

## Python environment

Always use the project Python environment:

```
/Users/lingshuai/opt/anaconda3/envs/cc/bin/python
```

## How to use

Run from the project root (`/Users/lingshuai/Projects/AgentProjects/CSUR_ExpTransfer`):

```bash
/Users/lingshuai/opt/anaconda3/envs/cc/bin/python \
  .claude/skills/csv-to-markdown/scripts/csv_to_markdown.py <csv_file> [-o <output.md>]
```

- `<csv_file>`: path to the input CSV (required).
- `-o <output.md>`: path to the output markdown file. If omitted, the file is saved to the project root with the same basename as the CSV (e.g. `papers.csv` → `papers.md`).

If the user specifies an output path/name, pass it via `-o`. The user may describe it in natural language ("save as xxx.md", "put it in the Docs/ folder"), in which case construct the appropriate path relative to the project root.

The script handles UTF-8 BOM headers and matches columns case-insensitively. If the CSV lacks any of the three required columns, the script prints an error listing the available columns.

## Output format

```
Title: {Title}

URL: {URL}

Abstract: {Abstract}

------

... (repeated for each row)
```
