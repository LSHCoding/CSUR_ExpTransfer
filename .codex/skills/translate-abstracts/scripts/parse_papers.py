#!/usr/bin/env python3
"""Parse a markdown file of papers (Title/URL/Abstract format, ------ delimited) into JSON.

Usage:
    python parse_papers.py <input.md>

Output: JSON array of paper objects to stdout.
"""

import json
import re
import sys
from pathlib import Path


def parse_papers(filepath: str) -> list[dict]:
    content = Path(filepath).read_text(encoding="utf-8")

    # Split on lines that are only dashes (4+). Keep each paper block text so
    # callers can preserve the original Title/URL/Abstract fields when writing.
    blocks = re.split(r'^\s*-{4,}\s*$', content, flags=re.MULTILINE)

    papers = []
    for block in blocks:
        block = block.strip()
        if not block:
            continue

        # Extract Title: first line starting with "Title:"
        title_match = re.search(r'^Title:\s*(.+)$', block, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else ""

        # Extract URL
        url_match = re.search(r'^URL:\s*(.+)$', block, re.MULTILINE)
        url = url_match.group(1).strip() if url_match else ""

        # Extract Abstract: from "Abstract:" to end of block (multiline)
        abstract_match = re.search(r'^Abstract:\s*(.+)$', block, re.MULTILINE | re.DOTALL)
        abstract = abstract_match.group(1).strip() if abstract_match else ""

        papers.append({
            "index": len(papers),
            "title": title,
            "url": url,
            "abstract": abstract,
            "raw_block": block,
        })

    return papers


def main():
    if len(sys.argv) < 2:
        print("Usage: parse_papers.py <markdown_file>", file=sys.stderr)
        sys.exit(1)

    filepath = sys.argv[1]
    if not Path(filepath).exists():
        print(f"Error: file not found: {filepath}", file=sys.stderr)
        sys.exit(1)

    papers = parse_papers(filepath)
    json.dump(papers, sys.stdout, ensure_ascii=False, indent=2)
    print()  # trailing newline


if __name__ == "__main__":
    main()
