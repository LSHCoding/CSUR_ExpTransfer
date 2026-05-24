#!/usr/bin/env python3
"""Download, unpack, and clean TeX sources for one arXiv paper."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
import tempfile
from pathlib import Path

from arxiv_tex_common import DEFAULT_OUTPUT_DIR, fetch_title_by_id, sanitize_filename, unique_directory_path
from clean_tex_tree import clean_tree
from download_source import download_source
from failure_records import clear_titles_from_search_failed_files
from title_match import find_existing_title_directory
from unpack_source import unpack_source


def download_one(
    arxiv_id: str,
    title: str | None = None,
    output_dir: Path = DEFAULT_OUTPUT_DIR,
    overwrite: bool = False,
    timeout: int = 120,
) -> dict[str, object]:
    paper_title = title or fetch_title_by_id(arxiv_id, timeout=timeout) or arxiv_id
    safe_title = sanitize_filename(paper_title, fallback=arxiv_id.replace("/", "_"))
    existing_dir = find_existing_title_directory(paper_title, output_dir)
    if existing_dir and not overwrite:
        updated_search_failed_files = clear_titles_from_search_failed_files([paper_title])
        return {
            "arxiv_id": arxiv_id,
            "title": paper_title,
            "directory": str(existing_dir),
            "matched_directory_name": existing_dir.name,
            "skipped_existing": True,
            "updated_search_failed_files": [str(path) for path in updated_search_failed_files],
        }

    output_dir.mkdir(parents=True, exist_ok=True)

    target_dir = existing_dir if existing_dir and overwrite else output_dir / safe_title
    if target_dir.exists():
        if overwrite:
            shutil.rmtree(target_dir)
        else:
            target_dir = unique_directory_path(target_dir)

    target_dir.mkdir(parents=True, exist_ok=False)
    try:
        with tempfile.TemporaryDirectory() as temp_root:
            archive = Path(temp_root) / f"{arxiv_id.replace('/', '_')}.tar.gz"
            download_source(arxiv_id, archive, timeout=timeout)
            unpack_result = unpack_source(archive, target_dir)
        clean_result = clean_tree(target_dir)
    except Exception:
        if target_dir.exists():
            shutil.rmtree(target_dir)
        raise
    updated_search_failed_files = clear_titles_from_search_failed_files([paper_title])

    return {
        "arxiv_id": arxiv_id,
        "title": paper_title,
        "directory": str(target_dir),
        "unpack": unpack_result,
        "clean": clean_result,
        "updated_search_failed_files": [str(path) for path in updated_search_failed_files],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("arxiv_id")
    parser.add_argument("--title")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--timeout", type=int, default=120)
    args = parser.parse_args()

    try:
        result = download_one(
            args.arxiv_id,
            title=args.title,
            output_dir=args.output_dir,
            overwrite=args.overwrite,
            timeout=args.timeout,
        )
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
