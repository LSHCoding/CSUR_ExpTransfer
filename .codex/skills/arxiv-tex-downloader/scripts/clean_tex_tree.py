#!/usr/bin/env python3
"""Keep only TeX and image files in an extracted source tree."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from arxiv_tex_common import KEEP_EXTENSIONS


def clean_tree(root: Path, keep_extensions: set[str] | None = None) -> dict[str, int]:
    keep = keep_extensions or KEEP_EXTENSIONS
    removed_files = 0
    kept_files = 0
    removed_dirs = 0

    for path in sorted(root.rglob("*"), reverse=True):
        if path.is_file():
            if path.suffix.lower() in keep:
                kept_files += 1
            else:
                path.unlink()
                removed_files += 1

    for path in sorted(root.rglob("*"), reverse=True):
        if path.is_dir() and not any(path.iterdir()):
            path.rmdir()
            removed_dirs += 1

    return {
        "kept_files": kept_files,
        "removed_files": removed_files,
        "removed_dirs": removed_dirs,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    args = parser.parse_args()

    if not args.root.exists():
        print(f"Path does not exist: {args.root}", file=sys.stderr)
        return 2
    print(json.dumps(clean_tree(args.root), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
