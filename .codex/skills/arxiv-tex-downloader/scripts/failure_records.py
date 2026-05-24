#!/usr/bin/env python3
"""Maintain Markdown failure records written by CSV download runs."""

from __future__ import annotations

from pathlib import Path

from arxiv_tex_common import DEFAULT_OUTPUT_DIR, normalize_space

SEARCH_FAILED_SUFFIX = "_search_failed.md"
SEARCH_ERROR_PREFIXES = (
    "HTTP Error",
    "Skipped after",
    "<urlopen error",
    "timed out",
    "The read operation timed out",
    "[Errno",
    "Remote end closed",
)


def search_failed_path_for_csv(csv_path: Path) -> Path:
    return csv_path.with_name(f"{csv_path.stem}{SEARCH_FAILED_SUFFIX}")


def default_paper_meta_dir() -> Path:
    return DEFAULT_OUTPUT_DIR.parent / "Data" / "PaperMetaInfos"


def candidate_search_failed_files(
    csv_path: Path | None = None,
    extra_paths: list[Path] | None = None,
    include_default_metadata: bool = True,
) -> list[Path]:
    candidates: list[Path] = []
    if csv_path is not None:
        candidates.append(search_failed_path_for_csv(csv_path))
        candidates.extend(csv_path.parent.glob(f"*{SEARCH_FAILED_SUFFIX}"))

    if include_default_metadata:
        meta_dir = default_paper_meta_dir()
        if meta_dir.exists():
            candidates.extend(meta_dir.glob(f"*{SEARCH_FAILED_SUFFIX}"))

    if extra_paths:
        candidates.extend(extra_paths)

    deduped: list[Path] = []
    seen: set[Path] = set()
    for path in candidates:
        key = path.resolve(strict=False)
        if key in seen:
            continue
        seen.add(key)
        if path.exists():
            deduped.append(path)
    return deduped


def _line_matches_title(line: str, titles: set[str]) -> bool:
    if not line.startswith("- "):
        return False
    body = normalize_space(line[2:])
    for title in titles:
        separator = f"{title}: "
        if not body.startswith(separator):
            continue
        error_text = body[len(separator) :]
        if error_text.startswith(SEARCH_ERROR_PREFIXES):
            return True
    return False


def clear_titles_from_search_failed_files(
    titles: list[str],
    csv_path: Path | None = None,
    extra_paths: list[Path] | None = None,
    include_default_metadata: bool = True,
) -> list[Path]:
    normalized_titles = {normalize_space(title) for title in titles if normalize_space(title)}
    if not normalized_titles:
        return []

    changed: list[Path] = []
    for path in candidate_search_failed_files(
        csv_path=csv_path,
        extra_paths=extra_paths,
        include_default_metadata=include_default_metadata,
    ):
        original_lines = path.read_text(encoding="utf-8").splitlines()
        kept_lines = [
            line for line in original_lines if not _line_matches_title(line, normalized_titles)
        ]
        if kept_lines == original_lines:
            continue
        path.write_text(
            "\n".join(kept_lines) + ("\n" if kept_lines else ""),
            encoding="utf-8",
        )
        changed.append(path)
    return changed
