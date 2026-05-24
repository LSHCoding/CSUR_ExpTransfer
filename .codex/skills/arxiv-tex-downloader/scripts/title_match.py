#!/usr/bin/env python3
"""Reusable title matching helpers for arXiv TeX output directories."""

from __future__ import annotations

import argparse
import html
import json
import re
import unicodedata
from pathlib import Path


UNIQUE_SUFFIX_RE = re.compile(r"\s+\[\d+\]\s*$")


def normalize_title_for_match(value: str | None) -> str:
    """Return a compact title key that ignores filename-sanitizing differences."""
    text = html.unescape(value or "")
    text = UNIQUE_SUFFIX_RE.sub("", text.strip())
    text = unicodedata.normalize("NFKD", text).casefold()
    return "".join(
        char
        for char in text
        if char.isalnum() and not unicodedata.category(char).startswith("M")
    )


def titles_match(left: str | None, right: str | None) -> bool:
    left_key = normalize_title_for_match(left)
    right_key = normalize_title_for_match(right)
    return bool(left_key and right_key and left_key == right_key)


def find_existing_title_directory(title: str | None, paper_tex_dir: Path) -> Path | None:
    target_key = normalize_title_for_match(title)
    if not target_key or not paper_tex_dir.is_dir():
        return None

    for candidate in sorted(paper_tex_dir.iterdir(), key=lambda path: path.name.casefold()):
        if candidate.is_dir() and normalize_title_for_match(candidate.name) == target_key:
            return candidate
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--title", required=True, help="Original paper title to match")
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument("--candidate", help="Candidate title or folder name to compare")
    target.add_argument("--paper-tex-dir", type=Path, help="Directory containing paper folders")
    args = parser.parse_args()

    normalized_title = normalize_title_for_match(args.title)
    if args.candidate is not None:
        normalized_candidate = normalize_title_for_match(args.candidate)
        payload = {
            "mode": "compare",
            "title": args.title,
            "candidate": args.candidate,
            "normalized_title": normalized_title,
            "normalized_candidate": normalized_candidate,
            "match": bool(normalized_title and normalized_title == normalized_candidate),
        }
    else:
        existing_dir = find_existing_title_directory(args.title, args.paper_tex_dir)
        payload = {
            "mode": "scan",
            "title": args.title,
            "paper_tex_dir": str(args.paper_tex_dir),
            "normalized_title": normalized_title,
            "exists": existing_dir is not None,
            "directory": str(existing_dir) if existing_dir else None,
            "matched_name": existing_dir.name if existing_dir else None,
        }

    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
