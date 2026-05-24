#!/usr/bin/env python3
"""Extract a normalized arXiv ID from text, DOI, or arXiv URL."""

from __future__ import annotations

import argparse
import sys

from arxiv_tex_common import extract_arxiv_id


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("value", help="arXiv ID, arXiv URL, DOI URL, or text containing one")
    args = parser.parse_args()

    arxiv_id = extract_arxiv_id(args.value)
    if not arxiv_id:
        print("No arXiv ID found", file=sys.stderr)
        return 2
    print(arxiv_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
