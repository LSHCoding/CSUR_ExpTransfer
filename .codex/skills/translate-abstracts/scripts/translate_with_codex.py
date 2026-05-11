#!/usr/bin/env python3
"""Translate paper abstracts by calling `codex exec` once per paper."""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import tempfile
import time
from datetime import datetime
from pathlib import Path

from parse_papers import parse_papers


DEFAULT_MODEL = os.environ.get("TRANSLATE_ABSTRACTS_MODEL", "gpt-5.4-mini")
DEFAULT_REASONING_EFFORT = os.environ.get("TRANSLATE_ABSTRACTS_REASONING_EFFORT", "low")
INITIAL_SLEEP = int(os.environ.get("TRANSLATE_ABSTRACTS_INITIAL_SLEEP", "300"))
MAX_SLEEP = int(os.environ.get("TRANSLATE_ABSTRACTS_MAX_SLEEP", "3600"))

RETRYABLE_LIMIT_RE = re.compile(
    r"rate limit|usage limit|too many requests|try again later|retry later|"
    r"overloaded|credits|quota|throttl",
    re.IGNORECASE,
)


def timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def default_output_path(input_path: Path) -> Path:
    suffix = input_path.suffix or ".md"
    return input_path.with_name(f"{input_path.stem}_en+cn{suffix}")


def safe_name(paper: dict) -> str:
    title = paper.get("title", "")[:70]
    text = f"{paper['index']:04d}_{title}"
    text = re.sub(r"[^A-Za-z0-9._-]+", "_", text).strip("_")
    return text or f"{paper['index']:04d}"


def mark_once(path: Path, value: str) -> None:
    existing = set()
    if path.exists():
        existing = {line.strip() for line in path.read_text(encoding="utf-8").splitlines()}
    if value not in existing:
        with path.open("a", encoding="utf-8") as handle:
            handle.write(value + "\n")


def build_prompt(paper: dict) -> str:
    return f"""You are translating one English academic paper abstract into Chinese.

Return exactly one tagged block:
<TRANSLATION>
Chinese translation text only
</TRANSLATION>

Rules:
- Translate the full abstract faithfully; do not summarize, omit, or add content.
- Return only the Chinese translation of the abstract inside the tags. Do not translate or include the paper title.
- Do not include Title, URL, Abstract, commentary, bullets, or code fences.
- Use natural Chinese academic prose for CS survey writing.
- Preserve all LaTeX math, code identifiers, URLs, and arXiv IDs exactly.
- Keep English acronyms and model names as-is, including LLM, RLHF, RAG, GPT, BERT, LLaMA, CLIP, ViT, GPU, API.
- Use standard terms: agent -> 智能体, large language model -> 大语言模型, memory system -> 记忆系统, tool calling -> 工具调用, attention -> 注意力, Transformer -> Transformer, fine-tuning -> 微调, reinforcement learning -> 强化学习, embedding -> 嵌入, representation -> 表征, latent space -> 潜空间, retrieval-augmented generation -> 检索增强生成, chain-of-thought -> 思维链.

Title:
{paper.get("title", "")}

Abstract:
{paper.get("abstract", "")}
"""


def extract_translation(output: str) -> str:
    matches = re.findall(r"<TRANSLATION>\s*(.*?)\s*</TRANSLATION>", output, flags=re.DOTALL | re.IGNORECASE)
    if matches:
        text = matches[-1]
    else:
        text = output
        if "中文翻译：" in text:
            text = text.split("中文翻译：", 1)[1]
        text = re.sub(r"^\s*```(?:\w+)?\s*", "", text)
        text = re.sub(r"\s*```\s*$", "", text)
        text = re.sub(r"^\s*<TRANSLATION>\s*", "", text, flags=re.IGNORECASE)
        text = re.sub(r"\s*</TRANSLATION>\s*$", "", text, flags=re.IGNORECASE)
        text = re.sub(r"\n\s*-{4,}\s*$", "", text)
    return text.strip()


def run_codex(prompt: str, log_file: Path, args: argparse.Namespace) -> tuple[int, str]:
    cmd = [
        "codex",
        "exec",
        "-s",
        "workspace-write",
        "-m",
        args.model,
        "-c",
        'approval_policy="never"',
        "-c",
        f'model_reasoning_effort="{args.reasoning_effort}"',
        "-C",
        str(args.codex_workdir),
        "--skip-git-repo-check",
        prompt,
    ]

    output_parts: list[str] = []
    with log_file.open("w", encoding="utf-8") as log:
        proc = subprocess.Popen(
            cmd,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )
        assert proc.stdout is not None
        for line in proc.stdout:
            print(line, end="")
            log.write(line)
            output_parts.append(line)
        return_code = proc.wait()

    return return_code, "".join(output_parts)


def assemble_output(papers: list[dict], translations_dir: Path, output_path: Path) -> tuple[int, list[int]]:
    blocks: list[str] = []
    missing: list[int] = []

    for paper in papers:
        translation_path = translations_dir / f"{paper['index']:04d}.txt"
        if not translation_path.exists():
            missing.append(paper["index"])
            continue
        translation = translation_path.read_text(encoding="utf-8").strip()
        blocks.append(f"{paper['raw_block'].rstrip()}\n\n中文翻译：{translation}\n\n------")

    output_path.write_text("\n\n".join(blocks) + ("\n" if blocks else ""), encoding="utf-8")
    return len(blocks), missing


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_file", type=Path)
    parser.add_argument("--output", type=Path, help="Output markdown path. Defaults to <input>_en+cn.md")
    parser.add_argument(
        "--workdir",
        type=Path,
        default=None,
        help="Working directory passed to codex exec. Defaults to an isolated temporary directory.",
    )
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--reasoning-effort", default=DEFAULT_REASONING_EFFORT)
    parser.add_argument("--limit", type=int, default=0, help="Maximum newly translated papers this run; 0 means all")
    parser.add_argument("--initial-sleep", type=int, default=INITIAL_SLEEP)
    parser.add_argument("--max-sleep", type=int, default=MAX_SLEEP)
    parser.add_argument("--force", action="store_true", help="Retranslate papers even if a cached translation exists")
    parser.add_argument("--dry-run", action="store_true", help="Parse input and print the first Codex prompt without running Codex")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    input_path = args.input_file.expanduser().resolve()
    output_path = (args.output.expanduser().resolve() if args.output else default_output_path(input_path).resolve())

    if args.limit < 0:
        print("ERROR: --limit must be >= 0", file=sys.stderr)
        return 2
    if not input_path.exists():
        print(f"ERROR: input file not found: {input_path}", file=sys.stderr)
        return 2

    papers = parse_papers(str(input_path))

    print(f"[{timestamp()}] INPUT  {input_path}")
    print(f"[{timestamp()}] OUTPUT {output_path}")
    print(f"[{timestamp()}] PAPERS {len(papers)}")

    if args.dry_run:
        if papers:
            print(build_prompt(papers[0]))
        return 0

    state_dir = input_path.parent / ".translate_abstracts_state" / input_path.stem
    logs_dir = state_dir / "logs"
    translations_dir = state_dir / "translations"
    done_file = state_dir / "done_papers.txt"
    failed_file = state_dir / "failed_papers.txt"
    logs_dir.mkdir(parents=True, exist_ok=True)
    translations_dir.mkdir(parents=True, exist_ok=True)
    done_file.touch()
    failed_file.touch()

    print(f"[{timestamp()}] STATE  {state_dir}")

    new_success_count = 0
    failed_indices: list[int] = []

    temp_workdir = None
    if args.workdir is None:
        temp_workdir = tempfile.TemporaryDirectory(prefix="translate_abstracts_codex_")
        args.codex_workdir = Path(temp_workdir.name).resolve()
    else:
        args.codex_workdir = args.workdir.expanduser().resolve()
        args.codex_workdir.mkdir(parents=True, exist_ok=True)

    print(f"[{timestamp()}] CODEX_WORKDIR {args.codex_workdir}")

    try:
        for paper in papers:
            index = paper["index"]
            translation_path = translations_dir / f"{index:04d}.txt"

            if translation_path.exists() and not args.force:
                print(f"[{timestamp()}] SKIP   paper {index}: {paper.get('title', '')}")
                continue

            if args.limit and new_success_count >= args.limit:
                print(f"[{timestamp()}] REACHED LIMIT {new_success_count} paper(s)")
                break

            prompt = build_prompt(paper)
            sleep_seconds = args.initial_sleep

            while True:
                log_file = logs_dir / f"{safe_name(paper)}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
                print(f"[{timestamp()}] START  paper {index}: {paper.get('title', '')}")
                print(f"[{timestamp()}] LOG    {log_file}")

                return_code, raw_output = run_codex(prompt, log_file, args)
                if return_code == 0:
                    translation = extract_translation(raw_output)
                    if not translation:
                        print(f"[{timestamp()}] ERROR  empty translation for paper {index}")
                        failed_indices.append(index)
                        mark_once(failed_file, str(index))
                        break

                    translation_path.write_text(translation + "\n", encoding="utf-8")
                    mark_once(done_file, str(index))
                    print(f"[{timestamp()}] DONE   paper {index}")
                    new_success_count += 1
                    break

                if RETRYABLE_LIMIT_RE.search(raw_output):
                    print(f"[{timestamp()}] WAIT   hit limit for paper {index}")
                    print(f"[{timestamp()}] SLEEP  {sleep_seconds}s")
                    time.sleep(sleep_seconds)
                    sleep_seconds = min(sleep_seconds * 2, args.max_sleep)
                    continue

                print(f"[{timestamp()}] ERROR  non-retryable failure for paper {index}")
                print(f"[{timestamp()}] CHECK  {log_file}")
                failed_indices.append(index)
                mark_once(failed_file, str(index))
                break
    finally:
        if temp_workdir is not None:
            temp_workdir.cleanup()

    translated_count, missing_indices = assemble_output(papers, translations_dir, output_path)
    print(f"[{timestamp()}] FINISHED translated={translated_count}/{len(papers)} new={new_success_count}")
    if failed_indices:
        print(f"[{timestamp()}] FAILED failed_indices={failed_indices}")
    if missing_indices:
        print(f"[{timestamp()}] MISSING missing_indices={missing_indices}")

    return 1 if failed_indices else 0


if __name__ == "__main__":
    raise SystemExit(main())
