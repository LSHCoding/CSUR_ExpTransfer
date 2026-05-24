#!/usr/bin/env python3
"""Offline tests for parsing, sanitizing, unpacking, and cleaning helpers."""

from __future__ import annotations

import tarfile
import tempfile
from pathlib import Path

from arxiv_tex_common import extract_arxiv_id, sanitize_filename
from clean_tex_tree import clean_tree
from failure_records import clear_titles_from_search_failed_files
from parse_input import parse_markdown
from title_match import find_existing_title_directory, normalize_title_for_match, titles_match
from unpack_source import unpack_source


def assert_equal(actual, expected) -> None:
    if actual != expected:
        raise AssertionError(f"Expected {expected!r}, got {actual!r}")


def main() -> int:
    assert_equal(extract_arxiv_id("2501.12485"), "2501.12485")
    assert_equal(extract_arxiv_id("https://arxiv.org/abs/2501.12485"), "2501.12485")
    assert_equal(extract_arxiv_id("https://arxiv.org/pdf/2501.12485.pdf"), "2501.12485")
    assert_equal(extract_arxiv_id("https://doi.org/10.48550/arXiv.2409.07429"), "2409.07429")
    assert_equal(sanitize_filename("A/B: C\nD"), "A B C D")
    assert_equal(normalize_title_for_match("A/B: C? D"), "abcd")
    assert_equal(titles_match("LLaMA-2: A/B Test?", "llama 2 a b test"), True)
    assert_equal(titles_match("", "llama 2"), False)

    with tempfile.TemporaryDirectory() as temp_root:
        root = Path(temp_root)
        md = root / "papers.md"
        md.write_text("2501.12485\nhttps://arxiv.org/pdf/2409.07429.pdf\n", encoding="utf-8")
        assert_equal([item["arxiv_id"] for item in parse_markdown(md)], ["2501.12485", "2409.07429"])

        paper_tex_dir = root / "PaperTexs"
        paper_tex_dir.mkdir()
        (paper_tex_dir / "LLaMA 2 A B Test").mkdir()
        (paper_tex_dir / "Agent Workflow Learning [2]").mkdir()
        assert_equal(
            find_existing_title_directory("LLaMA-2: A/B Test?", paper_tex_dir).name,
            "LLaMA 2 A B Test",
        )
        assert_equal(
            find_existing_title_directory("Agent Workflow Learning", paper_tex_dir).name,
            "Agent Workflow Learning [2]",
        )
        assert_equal(find_existing_title_directory("Different Paper", paper_tex_dir), None)

        source_root = root / "source"
        source_root.mkdir()
        (source_root / "main.tex").write_text("\\documentclass{article}", encoding="utf-8")
        (source_root / "fig.png").write_bytes(b"png")
        (source_root / "notes.bbl").write_text("remove", encoding="utf-8")
        archive = root / "paper.tar.gz"
        with tarfile.open(archive, "w:gz") as tar:
            tar.add(source_root / "main.tex", arcname="main.tex")
            tar.add(source_root / "fig.png", arcname="figures/fig.png")
            tar.add(source_root / "notes.bbl", arcname="notes.bbl")

        extracted = root / "extracted"
        unpack_source(archive, extracted)
        result = clean_tree(extracted)
        assert_equal(result["kept_files"], 2)
        assert_equal((extracted / "main.tex").exists(), True)
        assert_equal((extracted / "figures" / "fig.png").exists(), True)
        assert_equal((extracted / "notes.bbl").exists(), False)

        csv_path = root / "retry.csv"
        current_failure = root / "retry_search_failed.md"
        sibling_failure = root / "P3_search_failed.md"
        current_failure.write_text(
            "- Paper A: Subtitle: HTTP Error 429: Too Many Requests\n"
            "- Paper B: Skipped after 3 title-search errors\n",
            encoding="utf-8",
        )
        sibling_failure.write_text(
            "- Paper A: Subtitle: HTTP Error 429: Unknown Error\n"
            "- Paper A: Longer Subtitle: HTTP Error 429: Unknown Error\n"
            "- Paper C: HTTP Error 429: Unknown Error\n",
            encoding="utf-8",
        )
        changed = clear_titles_from_search_failed_files(
            ["Paper A: Subtitle"],
            csv_path=csv_path,
            include_default_metadata=False,
        )
        assert_equal(sorted(path.name for path in changed), ["P3_search_failed.md", "retry_search_failed.md"])
        assert_equal(
            current_failure.read_text(encoding="utf-8"),
            "- Paper B: Skipped after 3 title-search errors\n",
        )
        assert_equal(
            sibling_failure.read_text(encoding="utf-8"),
            "- Paper A: Longer Subtitle: HTTP Error 429: Unknown Error\n"
            "- Paper C: HTTP Error 429: Unknown Error\n",
        )

        changed = clear_titles_from_search_failed_files(
            ["Paper A"],
            csv_path=csv_path,
            include_default_metadata=False,
        )
        assert_equal(changed, [])

    print("offline self-test passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
