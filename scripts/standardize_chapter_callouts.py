#!/usr/bin/env python3
"""Standardize chapter Preview and Checklist as MyST admonitions.

Preview copy is taken from each LibreTexts chapter landing page (cached under
``work/html/chapter-landing-NN.html``). Checklist copy is kept from the chapter
Markdown, rewrapped. Both sit outside numbered section headings; Problems is a
plain ``## Problems`` heading after the checklist.
"""

from __future__ import annotations

import json
import re
import sys
import time
import urllib.request
from pathlib import Path

from bs4 import BeautifulSoup, Tag

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "chapters"
CACHE = ROOT / "work" / "html"
OUTLINE = ROOT / "outline.json"
UA = "QuadriviumPress-myst-converter/0.1 (OER CC BY-NC-SA reuse)"

PLACEHOLDER_RE = re.compile(r"^[\s*]+$")
LT_MATH_RE = re.compile(r"\\\((.+?)\\\)")
H1_RE = re.compile(r"^# .+$", re.M)
CHECKLIST_HEAD_RE = re.compile(
    r"^##+\s+(?:\d+\.\d+:\s+)?Chapter Checklist\s*$", re.M
)
PROBLEMS_HEAD_RE = re.compile(
    r"^##+\s+(?:\d+\.\d+:\s+)?Problems?\s*$", re.M
)
EXERCISE_RE = re.compile(r"^:{3,}\{exercise\}", re.M)
LEARNING_OBJ_RE = re.compile(
    r"^::::\{admonition\} Learning Objectives\n:class: objectives\n\n",
    re.M,
)


def fetch(url: str, dest: Path) -> str:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 2000:
        return dest.read_text(encoding="utf-8", errors="replace")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    html = urllib.request.urlopen(req, timeout=90).read().decode("utf-8", "replace")
    dest.write_text(html, encoding="utf-8")
    time.sleep(0.35)
    return html


def myst_math(text: str) -> str:
    return LT_MATH_RE.sub(r"$\1$", text).strip()


def is_section_index(text: str) -> bool:
    t = text.strip()
    if re.match(r"^\d+\.\d+:\s", t):
        return True
    if "Chapter Checklist" in t and re.search(r"\d+\.\d+:", t):
        return True
    return False


def is_placeholder(text: str) -> bool:
    return not text or bool(PLACEHOLDER_RE.match(text))


def extract_preview(html: str) -> tuple[list[str], str | None]:
    """Return (intro paragraphs, preview markdown or None if empty)."""
    soup = BeautifulSoup(html, "html.parser")
    main = soup.select_one("section.mt-content-container")
    if main is None:
        return [], None

    intro: list[str] = []
    lead: list[str] = []
    items: list[str] = []
    seen_preview = False

    def consume(node: Tag) -> None:
        nonlocal seen_preview
        name = node.name
        if name in {"footer", "nav"}:
            return
        cls = " ".join(node.get("class") or [])
        if "mt-guide" in cls or "mt-content-footer" in cls:
            return
        if name == "div" and "mt-section" in cls:
            for child in node.children:
                if isinstance(child, Tag):
                    consume(child)
            return
        text = node.get_text(" ", strip=True)
        if not seen_preview:
            if name in {"h1", "h2", "h3", "p"} and text.lower() == "preview":
                seen_preview = True
                return
            if name == "p" and text:
                intro.append(myst_math(text))
            return
        if name in {"h1", "h2", "h3"}:
            return
        if name in {"ol", "ul"}:
            for li in node.find_all("li", recursive=False):
                item = myst_math(li.get_text(" ", strip=True))
                if item and not is_placeholder(item):
                    items.append(item)
            return
        if name == "p" and text:
            if is_section_index(text):
                return
            if text.lower() == "preview":
                return
            cleaned = myst_math(text)
            if cleaned and not is_placeholder(cleaned) and cleaned.lower() != "the":
                lead.append(cleaned)

    for child in main.children:
        if isinstance(child, Tag):
            consume(child)

    if not lead and not items:
        return intro, None

    lines = ["::::{admonition} Chapter Preview", ":class: preview", ""]
    for para in lead:
        lines.append(para)
        lines.append("")
    for i, item in enumerate(items, 1):
        lines.append(f"{i}. {item}")
        lines.append("")
    while lines and lines[-1] == "":
        lines.pop()
    lines.append("::::")
    return intro, "\n".join(lines)


def wrap_checklist(body: str) -> str:
    body = LEARNING_OBJ_RE.sub("", body)
    body = re.sub(r"^::::\s*$", "", body, flags=re.M)
    body = body.strip()
    if body.startswith("::::{admonition}"):
        # already some other admonition — unwrap inner title if leftover
        body = re.sub(
            r"^::::\{admonition\}[^\n]*\n(?::class: [^\n]+\n)?\n?",
            "",
            body,
        )
        body = re.sub(r"\n::::\s*$", "", body)
        body = body.strip()
    lines = [
        "::::{admonition} Chapter Checklist",
        ":class: checklist",
        "",
        body,
        "::::",
    ]
    return "\n".join(lines)


def split_end_matter(text: str) -> tuple[str, str, str]:
    """Return (before_checklist, checklist_body, problems_block)."""
    cm = CHECKLIST_HEAD_RE.search(text)
    if not cm:
        raise ValueError("no Chapter Checklist heading")
    before = text[: cm.start()].rstrip() + "\n\n"
    rest = text[cm.end() :]
    pm = PROBLEMS_HEAD_RE.search(rest)
    em = EXERCISE_RE.search(rest)
    if pm and (em is None or pm.start() < em.start()):
        checklist_body = rest[: pm.start()]
        problems = rest[pm.end() :]
    elif em:
        checklist_body = rest[: em.start()]
        problems = rest[em.start() :]
    else:
        checklist_body = rest
        problems = ""
    problems = re.sub(
        r"^##+\s+\d+\.\d+:\s+Problems?\s*\n+",
        "",
        problems.lstrip(),
        flags=re.M,
    )
    if problems and not problems.startswith("\n"):
        problems = "\n" + problems
    return before, checklist_body, problems


def insert_opening(text: str, intro: list[str], preview: str | None) -> str:
    if "{admonition} Chapter Preview" in text:
        return text
    m = H1_RE.search(text)
    if not m:
        raise ValueError("no H1")
    insert_at = m.end()
    after = text[insert_at:]
    skip = re.match(r"\n+", after)
    pad = skip.group(0) if skip else "\n"
    chunks = ["\n\n"]
    for para in intro:
        chunks.append(para)
        chunks.append("\n\n")
    if preview:
        chunks.append(preview)
        chunks.append("\n")
    opening = "".join(chunks)
    if not intro and not preview:
        return text
    return text[:insert_at] + opening + "\n" + after[len(pad) :]


def transform_chapter(path: Path, landing_html: str) -> None:
    text = path.read_text(encoding="utf-8")
    intro, preview = extract_preview(landing_html)
    text = insert_opening(text, intro, preview)
    if CHECKLIST_HEAD_RE.search(text):
        before, checklist_body, problems = split_end_matter(text)
        checklist = wrap_checklist(checklist_body)
        text = before + checklist + "\n\n## Problems\n" + problems
    text = re.sub(r"\n{3,}", "\n\n", text)
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8")


def main() -> int:
    outline = json.loads(OUTLINE.read_text(encoding="utf-8"))
    for ch in outline["chapters"]:
        n = ch["number"]
        dest = CACHE / f"chapter-landing-{n:02d}.html"
        html = fetch(ch["url"], dest)
        path = CHAPTERS / f"{ch['slug']}.md"
        transform_chapter(path, html)
        print(f"updated {path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
