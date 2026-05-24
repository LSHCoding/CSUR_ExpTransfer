#!/usr/bin/env python3
"""Validate bilingual Markdown translations produced by translate-markdown-zh."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ZH_SUFFIX = "_zh_cn.md"
CJK_RE = re.compile(r"[\u3400-\u9fff]")
LATIN_RE = re.compile(r"[A-Za-z]+")
HEADING_RE = re.compile(r"^(#{1,6})\s+\S")
TABLE_SEPARATOR_RE = re.compile(
    r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$"
)
REFERENCE_HEADING_RE = re.compile(r"^#{1,6}\s+(References|Bibliography|Works Cited)\s*$", re.I)
TOC_HEADING_RE = re.compile(r"^#{1,6}\s+(Table of Contents|Contents)\s*$", re.I)
CITATION_RE = re.compile(r"\\?\[[^\]\n]{1,120}\\?\]")
URL_RE = re.compile(r"https?://\S+|doi:\s*\[[^\]]+\]\([^)]+\)")
INLINE_CODE_RE = re.compile(r"`[^`]*`")
MATH_RE = re.compile(r"\$[^$]*\$")


def is_markdown_source(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() == ".md" and not path.name.endswith(ZH_SUFFIX)


def translated_path(source: Path) -> Path:
    return source.with_name(f"{source.stem}_zh_cn.md")


def collect_sources(paths: list[Path]) -> list[Path]:
    sources: list[Path] = []
    for path in paths:
        if path.is_dir():
            sources.extend(p for p in sorted(path.rglob("*.md")) if is_markdown_source(p))
        elif is_markdown_source(path):
            sources.append(path)
        else:
            print(f"SKIP {path}: not a source .md file", file=sys.stderr)
    return sorted(dict.fromkeys(sources))


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def match_original_lines(source_lines: list[str], target_lines: list[str]) -> tuple[list[int], str | None]:
    matches: list[int] = []
    target_index = 0
    for source_line_no, source_line in enumerate(source_lines, start=1):
        while target_index < len(target_lines) and target_lines[target_index] != source_line:
            target_index += 1
        if target_index >= len(target_lines):
            return matches, f"missing or modified original line {source_line_no}: {source_line!r}"
        matches.append(target_index)
        target_index += 1
    return matches, None


def is_heading(line: str) -> bool:
    return HEADING_RE.match(line) is not None


def heading_level(line: str) -> int:
    match = HEADING_RE.match(line)
    return len(match.group(1)) if match else 0


def translatable_heading_indices(lines: list[str]) -> set[int]:
    indices: set[int] = set()
    in_toc = False
    in_references = False

    for index, line in enumerate(lines):
        if REFERENCE_HEADING_RE.match(line):
            in_references = True
        if in_references:
            continue

        if TOC_HEADING_RE.match(line):
            in_toc = True
            continue

        if in_toc and line.startswith("## ") and not TOC_HEADING_RE.match(line):
            in_toc = False

        if in_toc:
            continue
        if is_heading(line):
            indices.add(index)
    return indices


def next_nonblank_index(lines: list[str], start: int) -> int | None:
    for index in range(start, len(lines)):
        if lines[index].strip():
            return index
    return None


def validate_headings(
    source_lines: list[str], target_lines: list[str], matched_indices: list[int]
) -> list[str]:
    errors: list[str] = []
    heading_indices = translatable_heading_indices(source_lines)

    for source_index in sorted(heading_indices):
        if source_index >= len(matched_indices):
            continue
        target_index = matched_indices[source_index]
        translated_index = next_nonblank_index(target_lines, target_index + 1)
        if translated_index is None:
            errors.append(f"heading at source line {source_index + 1} has no translated heading")
            continue

        translated = target_lines[translated_index]
        if not is_heading(translated):
            errors.append(f"heading at source line {source_index + 1} is not followed by a heading")
            continue
        if heading_level(translated) != heading_level(source_lines[source_index]):
            errors.append(f"heading at source line {source_index + 1} uses a different heading level")
        if not CJK_RE.search(translated):
            errors.append(f"translated heading after source line {source_index + 1} has no Chinese")

    return errors


def is_table_start(lines: list[str], index: int) -> bool:
    return (
        index + 1 < len(lines)
        and "|" in lines[index]
        and TABLE_SEPARATOR_RE.match(lines[index + 1]) is not None
    )


def table_blocks(lines: list[str]) -> list[tuple[int, int]]:
    blocks: list[tuple[int, int]] = []
    index = 0
    while index < len(lines):
        if not is_table_start(lines, index):
            index += 1
            continue

        end = index + 2
        while end < len(lines) and "|" in lines[end] and lines[end].strip():
            end += 1
        blocks.append((index, end))
        index = end
    return blocks


def find_block(block: list[str], lines: list[str]) -> int:
    if not block:
        return -1
    last_start = len(lines) - len(block)
    for index in range(last_start + 1):
        if lines[index : index + len(block)] == block:
            return index
    return -1


def validate_tables(source_lines: list[str], target_lines: list[str]) -> list[str]:
    errors: list[str] = []
    for start, end in table_blocks(source_lines):
        block = source_lines[start:end]
        target_start = find_block(block, target_lines)
        if target_start < 0:
            errors.append(f"could not find original table starting at source line {start + 1}")
            continue

        translated_start = target_start + len(block)
        while translated_start < len(target_lines) and not target_lines[translated_start].strip():
            translated_start += 1

        if not is_table_start(target_lines, translated_start):
            errors.append(
                f"table starting at source line {start + 1} is not followed by a translated table"
            )
    return errors


def strip_exempt_english(text: str) -> str:
    text = URL_RE.sub("", text)
    text = CITATION_RE.sub("", text)
    text = INLINE_CODE_RE.sub("", text)
    text = MATH_RE.sub("", text)
    return text


def english_ratio(lines: list[str]) -> float:
    text = "\n".join(strip_exempt_english(line) for line in lines)
    english_chars = sum(len(match.group(0)) for match in LATIN_RE.finditer(text))
    cjk_chars = len(CJK_RE.findall(text))
    counted = english_chars + cjk_chars
    if counted == 0:
        return 0.0
    return english_chars / counted


def validate_pair(source: Path, target: Path, check_tables: bool, max_english_ratio: float) -> list[str]:
    errors: list[str] = []
    if target.name != f"{source.stem}_zh_cn.md":
        errors.append(f"unexpected translated filename: {target.name}")
    if not target.exists():
        return [f"missing translated file: {target}"]

    source_lines = read_lines(source)
    target_lines = read_lines(target)
    matched_indices, match_error = match_original_lines(source_lines, target_lines)
    if match_error:
        errors.append(match_error)

    matched = set(matched_indices)
    inserted_lines = [
        line for index, line in enumerate(target_lines) if index not in matched and line.strip()
    ]
    if not inserted_lines:
        errors.append("no inserted translation lines found")
    elif not any(CJK_RE.search(line) for line in inserted_lines):
        errors.append("inserted lines do not appear to contain Chinese text")
    else:
        ratio = english_ratio(inserted_lines)
        if ratio > max_english_ratio:
            errors.append(
                f"inserted translation English ratio is {ratio:.1%}, above {max_english_ratio:.1%}"
            )

    errors.extend(validate_headings(source_lines, target_lines, matched_indices))

    if check_tables:
        errors.extend(validate_tables(source_lines, target_lines))

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate *_zh_cn.md bilingual Markdown outputs against original source files."
    )
    parser.add_argument("paths", nargs="+", type=Path, help="Markdown source file(s) or folder(s)")
    parser.add_argument(
        "--no-table-check",
        action="store_true",
        help="Skip the check that every original table is followed by a translated table.",
    )
    parser.add_argument(
        "--max-english-ratio",
        type=float,
        default=0.05,
        help="Maximum Latin-letter ratio allowed in inserted translations after excluding citations, URLs, inline code, and math.",
    )
    args = parser.parse_args()

    sources = collect_sources(args.paths)
    if not sources:
        print("No source Markdown files found.", file=sys.stderr)
        return 2

    failed = False
    for source in sources:
        target = translated_path(source)
        errors = validate_pair(
            source,
            target,
            check_tables=not args.no_table_check,
            max_english_ratio=args.max_english_ratio,
        )
        if errors:
            failed = True
            print(f"FAIL {source}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK {source} -> {target}")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
