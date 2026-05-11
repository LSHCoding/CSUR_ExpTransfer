#!/usr/bin/env python3
"""Parse Title/URL/Abstract markdown into JSON paper records.

Reads a markdown file in the format produced by csv-to-markdown (or hand-written
in the same style), splits on '------' separators, and extracts Title / URL /
Abstract for each paper. Outputs a JSON object on stdout for downstream
annotation.

Input format (one block per paper, blocks separated by a line of >= 3 dashes):

    Title: ...

    URL: ...

    Abstract: ...

    ------

Output format on stdout:

    {
      "count": <int>,
      "papers": [
        {"index": 1, "title": "...", "url": "...", "abstract": "..."},
        ...
      ],
      "errors": [{"block": <int>, "reason": "..."}]
    }

The script does not write any files. The caller is responsible for downstream
annotation and persistence.
"""

import argparse
import json
import re
import sys
from pathlib import Path


SEPARATOR = re.compile(r"^-{3,}\s*$", re.MULTILINE)
FIELD_KEYS = ("Title", "URL", "Abstract")


def parse_block(block: str, idx: int):
    """Extract Title / URL / Abstract from one block.

    Returns (record, None) on success or (None, error_message) on failure.
    URL is optional; Title and Abstract are required.
    """
    positions = {}
    for key in FIELD_KEYS:
        m = re.search(rf"^{key}:\s*", block, flags=re.MULTILINE)
        if m:
            positions[key] = (m.start(), m.end())

    missing = [k for k in ("Title", "Abstract") if k not in positions]
    if missing:
        return None, f"missing required field(s): {', '.join(missing)}"

    sorted_keys = sorted(positions.keys(), key=lambda k: positions[k][0])

    record = {"index": idx}
    for i, key in enumerate(sorted_keys):
        value_start = positions[key][1]
        value_end = (
            positions[sorted_keys[i + 1]][0]
            if i + 1 < len(sorted_keys)
            else len(block)
        )
        record[key.lower()] = block[value_start:value_end].strip()

    record.setdefault("url", "")
    return record, None


def parse_papers(text: str):
    blocks = [b.strip() for b in SEPARATOR.split(text)]
    blocks = [b for b in blocks if b]

    papers = []
    errors = []
    for idx, block in enumerate(blocks, 1):
        record, err = parse_block(block, idx)
        if err is not None:
            errors.append({"block": idx, "reason": err})
        else:
            papers.append(record)

    return papers, errors


def main():
    parser = argparse.ArgumentParser(
        description="Parse Title/URL/Abstract markdown into JSON paper records."
    )
    parser.add_argument("input_md", help="Path to the input markdown file")
    args = parser.parse_args()

    path = Path(args.input_md)
    if not path.is_file():
        print(f"Error: file not found: {args.input_md}", file=sys.stderr)
        sys.exit(1)

    text = path.read_text(encoding="utf-8")
    papers, errors = parse_papers(text)

    json.dump(
        {"count": len(papers), "papers": papers, "errors": errors},
        sys.stdout,
        ensure_ascii=False,
        indent=2,
    )
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
