#!/usr/bin/env python3
"""Shared helpers for arXiv TeX source download scripts."""

from __future__ import annotations

import html
import os
import re
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


DEFAULT_OUTPUT_DIR = Path(
    "/Users/lingshuai/Projects/AgentProjects/CSUR_ExpTransfer/AgentData/PaperTexs"
)

ARXIV_API_URL = "https://export.arxiv.org/api/query"
ARXIV_SOURCE_URL = "https://arxiv.org/e-print/{arxiv_id}"
USER_AGENT = "Codex arxiv-tex-downloader/1.0"
TRANSIENT_HTTP_CODES = {429, 500, 502, 503, 504}

KEEP_EXTENSIONS = {
    ".tex",
    ".png",
    ".jpg",
    ".jpeg",
    ".pdf",
    ".eps",
    ".gif",
    ".bmp",
    ".tif",
    ".tiff",
    ".svg",
}

MODERN_ID_RE = re.compile(r"(?i)(?<!\d)(\d{4}\.\d{4,5})(?:v\d+)?(?!\d)")
OLD_ID_RE = re.compile(r"(?i)([a-z-]+(?:\.[a-z]{2})?/\d{7})(?:v\d+)?")
ARXIV_PREFIX_RE = re.compile(
    r"(?i)arxiv[.:/\s]+([a-z-]+(?:\.[a-z]{2})?/\d{7}|\d{4}\.\d{4,5})(?:v\d+)?"
)
VERSION_RE = re.compile(r"(?i)v\d+$")
CONTROL_RE = re.compile(r"[\x00-\x1f\x7f]")
UNSAFE_FILENAME_RE = re.compile(r'[<>:"/\\|?*]+')


def _retry_delay(exc: BaseException, attempt: int, base_delay: float) -> float | None:
    if isinstance(exc, urllib.error.HTTPError):
        if exc.code not in TRANSIENT_HTTP_CODES:
            return None
        retry_after = exc.headers.get("Retry-After")
        if retry_after and retry_after.isdecimal():
            return min(max(float(retry_after), 1.0), 300.0)
    elif not isinstance(exc, urllib.error.URLError):
        return None
    return min(base_delay * (2**attempt), 120.0)


def urlopen_with_retries(
    request: urllib.request.Request,
    timeout: int = 60,
    retries: int = 4,
    base_delay: float = 10.0,
):
    for attempt in range(retries + 1):
        try:
            return urllib.request.urlopen(request, timeout=timeout)
        except (urllib.error.HTTPError, urllib.error.URLError) as exc:
            delay = _retry_delay(exc, attempt, base_delay)
            if delay is None or attempt >= retries:
                raise
            time.sleep(delay)
    raise RuntimeError("unreachable retry state")


def request_url(url: str, timeout: int = 60) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen_with_retries(request, timeout=timeout, retries=2) as response:
        return response.read()


def strip_arxiv_version(arxiv_id: str) -> str:
    return VERSION_RE.sub("", arxiv_id.strip())


def extract_arxiv_id(value: str | None) -> str | None:
    if not value:
        return None

    text = urllib.parse.unquote(str(value)).strip()
    text = text.strip("`'\" \t\r\n")

    parsed = urllib.parse.urlparse(text)
    if parsed.netloc.lower().endswith("arxiv.org"):
        path = parsed.path.strip("/")
        for prefix in ("abs/", "pdf/", "e-print/", "format/"):
            if path.lower().startswith(prefix):
                candidate = path[len(prefix) :]
                candidate = candidate.removesuffix(".pdf")
                candidate = candidate.strip("/")
                if candidate:
                    return strip_arxiv_version(candidate)

    prefixed = ARXIV_PREFIX_RE.search(text)
    if prefixed:
        return strip_arxiv_version(prefixed.group(1))

    modern = MODERN_ID_RE.search(text)
    if modern:
        return strip_arxiv_version(modern.group(1))

    old = OLD_ID_RE.search(text)
    if old:
        return strip_arxiv_version(old.group(1))

    return None


def atom_entries(payload: bytes) -> list[dict[str, str]]:
    root = ET.fromstring(payload)
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    entries: list[dict[str, str]] = []
    for entry in root.findall("atom:entry", ns):
        title = entry.findtext("atom:title", default="", namespaces=ns)
        entry_id = entry.findtext("atom:id", default="", namespaces=ns)
        summary = entry.findtext("atom:summary", default="", namespaces=ns)
        entries.append(
            {
                "id": extract_arxiv_id(entry_id) or "",
                "entry_url": entry_id.strip(),
                "title": normalize_space(html.unescape(title)),
                "summary": normalize_space(html.unescape(summary)),
            }
        )
    return entries


def fetch_title_by_id(arxiv_id: str, timeout: int = 60) -> str | None:
    params = urllib.parse.urlencode({"id_list": arxiv_id})
    payload = request_url(f"{ARXIV_API_URL}?{params}", timeout=timeout)
    entries = atom_entries(payload)
    if not entries:
        return None
    return entries[0].get("title") or None


def normalize_space(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def sanitize_filename(title: str | None, fallback: str = "untitled", max_length: int = 180) -> str:
    value = normalize_space(title or "")
    value = unicodedata.normalize("NFC", value)
    value = CONTROL_RE.sub(" ", value)
    value = UNSAFE_FILENAME_RE.sub(" ", value)
    value = normalize_space(value).strip(" .")
    if not value:
        value = fallback
    if len(value) > max_length:
        value = value[:max_length].rstrip(" .")
    return value or fallback


def unique_directory_path(base: Path) -> Path:
    if not base.exists():
        return base

    parent = base.parent
    stem = base.name
    for index in range(2, 1000):
        candidate = parent / f"{stem} [{index}]"
        if not candidate.exists():
            return candidate
    raise RuntimeError(f"Could not create a unique directory near {base}")


def ensure_within_directory(root: Path, candidate: Path) -> None:
    root_resolved = root.resolve()
    candidate_resolved = candidate.resolve()
    if os.path.commonpath([root_resolved, candidate_resolved]) != str(root_resolved):
        raise ValueError(f"Unsafe archive member path: {candidate}")
