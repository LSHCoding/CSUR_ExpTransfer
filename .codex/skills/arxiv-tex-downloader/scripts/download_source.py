#!/usr/bin/env python3
"""Download one arXiv source archive to a local file."""

from __future__ import annotations

import argparse
import shutil
import sys
import urllib.parse
import urllib.request
from pathlib import Path

from arxiv_tex_common import ARXIV_SOURCE_URL, USER_AGENT, urlopen_with_retries


def download_source(arxiv_id: str, destination: Path, timeout: int = 120) -> Path:
    destination.parent.mkdir(parents=True, exist_ok=True)
    source_url = ARXIV_SOURCE_URL.format(arxiv_id=urllib.parse.quote(arxiv_id, safe="/"))
    request = urllib.request.Request(source_url, headers={"User-Agent": USER_AGENT})
    with urlopen_with_retries(request, timeout=timeout) as response:
        with destination.open("wb") as handle:
            shutil.copyfileobj(response, handle)
    return destination


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("arxiv_id")
    parser.add_argument("destination", type=Path)
    parser.add_argument("--timeout", type=int, default=120)
    args = parser.parse_args()

    try:
        path = download_source(args.arxiv_id, args.destination, timeout=args.timeout)
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
