#!/usr/bin/env python3
"""Safely unpack an arXiv source archive into a target directory."""

from __future__ import annotations

import argparse
import gzip
import shutil
import sys
import tarfile
from pathlib import Path

from arxiv_tex_common import ensure_within_directory


def safe_extract_tar(archive: Path, target_dir: Path) -> int:
    extracted = 0
    target_dir.mkdir(parents=True, exist_ok=True)
    with tarfile.open(archive, mode="r:*") as tar:
        for member in tar.getmembers():
            destination = target_dir / member.name
            ensure_within_directory(target_dir, destination)
        for member in tar.getmembers():
            tar.extract(member, target_dir)
            extracted += 1
    return extracted


def unpack_source(archive: Path, target_dir: Path) -> dict[str, int | str]:
    target_dir.mkdir(parents=True, exist_ok=True)
    if tarfile.is_tarfile(archive):
        return {"mode": "tar", "extracted": safe_extract_tar(archive, target_dir)}

    with archive.open("rb") as handle:
        magic = handle.read(2)

    if magic == b"\x1f\x8b":
        output = target_dir / "main.tex"
        with gzip.open(archive, "rb") as source, output.open("wb") as destination:
            shutil.copyfileobj(source, destination)
        return {"mode": "gzip-single", "extracted": 1}

    output = target_dir / "main.tex"
    shutil.copyfile(archive, output)
    return {"mode": "single", "extracted": 1}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path)
    parser.add_argument("target_dir", type=Path)
    args = parser.parse_args()

    try:
        result = unpack_source(args.archive, args.target_dir)
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
