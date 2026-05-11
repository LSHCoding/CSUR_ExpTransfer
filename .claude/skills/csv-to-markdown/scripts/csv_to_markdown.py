#!/usr/bin/env python3
"""Read a CSV of papers and output Title/URL/Abstract as formatted markdown."""

import argparse
import csv
import sys
from pathlib import Path


def find_columns(headers: list[str]) -> dict[str, str]:
    """Map canonical column names to actual header names (case-insensitive)."""
    canonical = ["Title", "URL", "Abstract"]
    header_lower = {h.strip().lower(): h.strip() for h in headers}
    mapping = {}
    for key in canonical:
        if key.lower() in header_lower:
            mapping[key] = header_lower[key.lower()]
        else:
            print(f"Error: required column '{key}' not found in CSV. Available columns: {headers}",
                  file=sys.stderr)
            sys.exit(1)
    return mapping


def main():
    parser = argparse.ArgumentParser(
        description="Convert CSV of papers to markdown with Title/URL/Abstract entries."
    )
    parser.add_argument("csv_file", help="Path to the CSV file")
    parser.add_argument("-o", "--output", default=None,
                        help="Output markdown file path (default: <csv_name>.md in cwd)")
    args = parser.parse_args()

    csv_path = Path(args.csv_file)
    if not csv_path.is_file():
        print(f"Error: file not found: {args.csv_file}", file=sys.stderr)
        sys.exit(1)

    if args.output is None:
        args.output = str(csv_path.with_suffix(".md").name)

    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            print("Error: CSV has no headers", file=sys.stderr)
            sys.exit(1)
        col_map = find_columns(list(reader.fieldnames))

        entries = []
        for row in reader:
            title = row.get(col_map["Title"], "").strip()
            url = row.get(col_map["URL"], "").strip()
            abstract = row.get(col_map["Abstract"], "").strip()
            entries.append((title, url, abstract))

    lines = []
    for title, url, abstract in entries:
        lines.append(f"Title: {title}")
        lines.append("")
        lines.append(f"URL: {url}")
        lines.append("")
        lines.append(f"Abstract: {abstract}")
        lines.append("")
        lines.append("------")
        lines.append("")

    output = "\n".join(lines).rstrip("\n")

    out_path = Path(args.output)
    out_path.write_text(output, encoding="utf-8")
    print(f"Written {len(entries)} entries to {out_path}")


if __name__ == "__main__":
    main()
