#!/usr/bin/env python3
"""Parse a single user input into arXiv download work items."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from arxiv_tex_common import extract_arxiv_id


def parse_markdown(path: Path) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        value = line.strip()
        if not value:
            continue
        arxiv_id = extract_arxiv_id(value)
        if not arxiv_id:
            raise ValueError(f"Line {line_number} does not contain an arXiv ID: {value}")
        items.append({"arxiv_id": arxiv_id, "source": value})
    return items


def parse_input(value: str) -> dict[str, object]:
    path = Path(value).expanduser()
    if path.exists():
        suffix = path.suffix.lower()
        if suffix == ".csv":
            return {"type": "csv", "path": str(path)}
        if suffix in {".md", ".markdown", ".txt"}:
            return {"type": "papers", "items": parse_markdown(path)}
        raise ValueError(f"Unsupported input file type: {path.suffix}")

    arxiv_id = extract_arxiv_id(value)
    if arxiv_id:
        return {"type": "papers", "items": [{"arxiv_id": arxiv_id, "source": value}]}
    raise ValueError(f"Input is neither a supported file nor an arXiv ID/URL: {value}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="arXiv ID, arXiv URL, Markdown list, or CSV file")
    args = parser.parse_args()

    try:
        print(json.dumps(parse_input(args.input), ensure_ascii=False, indent=2))
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
