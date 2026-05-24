#!/usr/bin/env python3
"""Top-level dispatcher for arXiv TeX source downloads."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from arxiv_tex_common import DEFAULT_OUTPUT_DIR
from download_one import download_one
from parse_input import parse_input
from process_csv import process_csv


def run(
    user_input: str,
    output_dir: Path = DEFAULT_OUTPUT_DIR,
    overwrite: bool = False,
    min_score: float = 0.82,
    search_delay: float = 3.0,
    download_delay: float = 0.0,
    max_search_errors: int = 3,
    resume: bool = False,
    timeout: int = 120,
) -> dict[str, object]:
    parsed = parse_input(user_input)
    if parsed["type"] == "csv":
        return process_csv(
            Path(str(parsed["path"])),
            output_dir=output_dir,
            min_score=min_score,
            search_delay=search_delay,
            download_delay=download_delay,
            max_search_errors=max_search_errors,
            overwrite=overwrite,
            resume=resume,
            timeout=timeout,
        )

    downloaded = []
    skipped_existing = []
    for item in parsed["items"]:  # type: ignore[index]
        result = download_one(
            str(item["arxiv_id"]),
            output_dir=output_dir,
            overwrite=overwrite,
            timeout=timeout,
        )
        if result.get("skipped_existing"):
            skipped_existing.append(result)
        else:
            downloaded.append(result)
    return {
        "input": user_input,
        "downloaded_count": len(downloaded),
        "skipped_existing_count": len(skipped_existing),
        "downloaded": downloaded,
        "skipped_existing": skipped_existing,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="arXiv ID, arXiv URL, Markdown list, or CSV file")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--min-score", type=float, default=0.82)
    parser.add_argument("--search-delay", type=float, default=3.0)
    parser.add_argument("--download-delay", type=float, default=0.0)
    parser.add_argument("--max-search-errors", type=int, default=3)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--timeout", type=int, default=120)
    args = parser.parse_args()

    try:
        result = run(
            args.input,
            output_dir=args.output_dir,
            overwrite=args.overwrite,
            min_score=args.min_score,
            search_delay=args.search_delay,
            download_delay=args.download_delay,
            max_search_errors=args.max_search_errors,
            timeout=args.timeout,
            resume=args.resume,
        )
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
