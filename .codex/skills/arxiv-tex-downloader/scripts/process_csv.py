#!/usr/bin/env python3
"""Process a CSV with Title and URL columns and download arXiv TeX sources."""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from pathlib import Path

from arxiv_tex_common import DEFAULT_OUTPUT_DIR, extract_arxiv_id
from download_one import download_one
from failure_records import clear_titles_from_search_failed_files, search_failed_path_for_csv
from search_arxiv_by_title import find_arxiv_by_title
from title_match import find_existing_title_directory


def not_found_path(csv_path: Path) -> Path:
    return csv_path.with_name(f"{csv_path.stem}_not_found_in_arxiv.md")


def process_csv(
    csv_path: Path,
    output_dir: Path = DEFAULT_OUTPUT_DIR,
    min_score: float = 0.82,
    search_delay: float = 3.0,
    download_delay: float = 0.0,
    max_search_errors: int = 3,
    overwrite: bool = False,
    resume: bool = False,
    timeout: int = 120,
) -> dict[str, object]:
    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None or "Title" not in reader.fieldnames or "URL" not in reader.fieldnames:
            raise ValueError("CSV must contain exact Title and URL columns")
        rows = list(reader)

    downloaded: list[dict[str, object]] = []
    skipped_existing: list[dict[str, object]] = []
    not_found_titles: list[str] = []
    failed_downloads: list[dict[str, object]] = []
    search_failures: list[dict[str, object]] = []
    updated_search_failed_files: set[str] = set()
    search_error_count = 0

    def clear_successful_titles(*titles: str) -> None:
        changed = clear_titles_from_search_failed_files(list(titles), csv_path=csv_path)
        updated_search_failed_files.update(str(path) for path in changed)

    for index, row in enumerate(rows, start=1):
        title = (row.get("Title") or "").strip()
        url = (row.get("URL") or "").strip()
        arxiv_id = None
        match = None

        if "arxiv" in url.casefold():
            arxiv_id = extract_arxiv_id(url)

        if not arxiv_id and title:
            if max_search_errors >= 0 and search_error_count >= max_search_errors:
                search_failures.append(
                    {
                        "row": index,
                        "title": title,
                        "error": f"Skipped after {search_error_count} title-search errors",
                    }
                )
                continue
            try:
                match = find_arxiv_by_title(title, min_score=min_score, timeout=timeout)
            except Exception as exc:
                search_error_count += 1
                search_failures.append({"row": index, "title": title, "error": str(exc)})
                if search_delay > 0:
                    time.sleep(search_delay)
                continue
            if match:
                arxiv_id = str(match["arxiv_id"])
            if search_delay > 0:
                time.sleep(search_delay)

        if not arxiv_id:
            not_found_titles.append(title or f"Row {index}")
            continue

        if resume and not overwrite:
            existing_dir = find_existing_title_directory(title or arxiv_id, output_dir)
            if existing_dir:
                result: dict[str, object] = {
                    "row": index,
                    "arxiv_id": arxiv_id,
                    "title": title or arxiv_id,
                    "directory": str(existing_dir),
                    "matched_directory_name": existing_dir.name,
                    "skipped_existing": True,
                }
                if match:
                    result["search_match"] = match
                skipped_existing.append(result)
                clear_successful_titles(title or arxiv_id)
                continue

        try:
            result = download_one(
                arxiv_id,
                title=title or None,
                output_dir=output_dir,
                overwrite=overwrite,
                timeout=timeout,
            )
        except Exception as exc:
            failed_downloads.append(
                {
                    "row": index,
                    "title": title or f"Row {index}",
                    "arxiv_id": arxiv_id,
                    "error": str(exc),
                }
            )
            if download_delay > 0:
                time.sleep(download_delay)
            continue
        if match:
            result["search_match"] = match
        if result.get("skipped_existing"):
            skipped_existing.append(result)
        else:
            downloaded.append(result)
        result_title = str(result.get("title") or "")
        clear_successful_titles(title, result_title)
        if download_delay > 0:
            time.sleep(download_delay)

    missing_path = not_found_path(csv_path)
    missing_path.write_text(
        "".join(f"- {title}\n" for title in not_found_titles),
        encoding="utf-8",
    )
    failed_path = csv_path.with_name(f"{csv_path.stem}_download_failed.md")
    failed_path.write_text(
        "".join(
            f"- {item['title']} ({item['arxiv_id']}): {item['error']}\n"
            for item in failed_downloads
        ),
        encoding="utf-8",
    )
    search_failed_path = search_failed_path_for_csv(csv_path)
    search_failed_path.write_text(
        "".join(
            f"- {item['title']}: {item['error']}\n"
            for item in search_failures
        ),
        encoding="utf-8",
    )

    return {
        "csv": str(csv_path),
        "downloaded_count": len(downloaded),
        "skipped_existing_count": len(skipped_existing),
        "not_found_count": len(not_found_titles),
        "failed_download_count": len(failed_downloads),
        "search_failed_count": len(search_failures),
        "not_found_file": str(missing_path),
        "failed_download_file": str(failed_path),
        "search_failed_file": str(search_failed_path),
        "updated_search_failed_files": sorted(updated_search_failed_files),
        "downloaded": downloaded,
        "skipped_existing": skipped_existing,
        "failed_downloads": failed_downloads,
        "search_failures": search_failures,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--min-score", type=float, default=0.82)
    parser.add_argument("--search-delay", type=float, default=3.0)
    parser.add_argument("--download-delay", type=float, default=0.0)
    parser.add_argument("--max-search-errors", type=int, default=3)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--timeout", type=int, default=120)
    args = parser.parse_args()

    try:
        result = process_csv(
            args.csv_path,
            output_dir=args.output_dir,
            min_score=args.min_score,
            search_delay=args.search_delay,
            download_delay=args.download_delay,
            max_search_errors=args.max_search_errors,
            overwrite=args.overwrite,
            resume=args.resume,
            timeout=args.timeout,
        )
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
