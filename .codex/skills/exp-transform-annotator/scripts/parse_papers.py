#!/usr/bin/env python3
"""Parse Title/URL/Abstract markdown into JSON paper records.

Reads a markdown file in the format produced by csv-to-markdown or handwritten
in the same style, splits on dashed separators, and extracts Title / URL /
Abstract for each paper. Outputs a JSON object on stdout for downstream
annotation.
"""

import argparse
import json
import re
import sys
from pathlib import Path


SEPARATOR = re.compile(r"^-{3,}\s*$", re.MULTILINE)
FIELD_KEYS = ("Title", "URL", "Abstract")


def parse_block(block: str, idx: int):
    """Extract Title / URL / Abstract from one block."""
    positions = {}
    for key in FIELD_KEYS:
        match = re.search(rf"^{key}:\s*", block, flags=re.MULTILINE)
        if match:
            positions[key] = (match.start(), match.end())

    missing = [key for key in ("Title", "Abstract") if key not in positions]
    if missing:
        return None, f"missing required field(s): {', '.join(missing)}"

    sorted_keys = sorted(positions.keys(), key=lambda key: positions[key][0])

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
    blocks = [block.strip() for block in SEPARATOR.split(text)]
    blocks = [block for block in blocks if block]

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
