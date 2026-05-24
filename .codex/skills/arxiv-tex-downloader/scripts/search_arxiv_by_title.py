#!/usr/bin/env python3
"""Search arXiv by title and return the best matching arXiv ID."""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
import urllib.parse

from arxiv_tex_common import ARXIV_API_URL, atom_entries, normalize_space, request_url


def normalize_title(value: str) -> str:
    value = normalize_space(value).casefold()
    value = re.sub(r"[^0-9a-z\u0080-\uffff]+", " ", value)
    return normalize_space(value)


def title_score(query: str, candidate: str) -> float:
    query_norm = normalize_title(query)
    candidate_norm = normalize_title(candidate)
    if not query_norm or not candidate_norm:
        return 0.0
    if query_norm == candidate_norm:
        return 1.0
    if query_norm in candidate_norm or candidate_norm in query_norm:
        return 0.95
    return difflib.SequenceMatcher(None, query_norm, candidate_norm).ratio()


def query_arxiv(title: str, search_field: str, max_results: int, timeout: int) -> list[dict[str, str]]:
    params = urllib.parse.urlencode(
        {
            "search_query": f'{search_field}:"{title}"',
            "start": "0",
            "max_results": str(max_results),
        }
    )
    return atom_entries(request_url(f"{ARXIV_API_URL}?{params}", timeout=timeout))


def find_arxiv_by_title(
    title: str,
    min_score: float = 0.82,
    max_results: int = 5,
    timeout: int = 60,
) -> dict[str, object] | None:
    candidates: list[dict[str, str]] = []
    for field in ("ti", "all"):
        candidates.extend(query_arxiv(title, field, max_results=max_results, timeout=timeout))
        if candidates:
            break

    best: dict[str, object] | None = None
    for entry in candidates:
        score = title_score(title, entry.get("title", ""))
        if not entry.get("id"):
            continue
        result = {
            "arxiv_id": entry["id"],
            "matched_title": entry.get("title", ""),
            "score": round(score, 4),
        }
        if best is None or score > float(best["score"]):
            best = result

    if best is None or float(best["score"]) < min_score:
        return None
    return best


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("title", help="Paper title to search")
    parser.add_argument("--min-score", type=float, default=0.82)
    parser.add_argument("--max-results", type=int, default=5)
    parser.add_argument("--timeout", type=int, default=60)
    args = parser.parse_args()

    try:
        result = find_arxiv_by_title(
            args.title,
            min_score=args.min_score,
            max_results=args.max_results,
            timeout=args.timeout,
        )
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        return 1

    if result is None:
        print("No confident arXiv match found", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
