"""Assemble MyST Markdown from cached LibreTexts HTML."""

from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.request
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import BUILD, HTML_CACHE, IMAGES, OUTLINE, ROOT, USER_AGENT
from html_to_myst import HtmlToMyst, slugify

SECTION_NUM_RE = re.compile(r"^(\d+\.[0-9A-Za-z]+)\s*:")


def section_number(title: str) -> str | None:
    """"5.2: Euler's Differential Equation" -> "5.2"."""
    m = SECTION_NUM_RE.match(title.strip())
    return m.group(1) if m else None

FRONT_SKIP = {
    "titlepage",
    "infopage",
    "table-of-contents",
    "tableofcontents",
    "licensing",
}
BACK_SKIP = {"index", "detailed-licensing"}


def load_outline() -> dict:
    with open(OUTLINE, encoding="utf-8") as fh:
        return json.load(fh)


def read_cache(name: str) -> str:
    path = Path(HTML_CACHE) / name
    return path.read_text(encoding="utf-8")


def download_images(pending: list[tuple[str, Path]]) -> None:
    Path(IMAGES).mkdir(parents=True, exist_ok=True)
    seen = set()
    for url, dest in pending:
        if str(dest) in seen:
            continue
        seen.add(str(dest))
        if dest.exists() and dest.stat().st_size > 0:
            continue
        print(f"  img {dest.name}", flush=True)
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=90) as resp:
                dest.write_bytes(resp.read())
        except Exception as exc:  # noqa: BLE001
            print(f"  ! failed {url}: {exc}", flush=True)
        time.sleep(0.15)


def front_matter(title: str, short: str, label: str) -> str:
    return (
        f"---\n"
        f'title: "{title}"\n'
        f'short_title: "{short}"\n'
        f"label: {label}\n"
        f"---\n\n"
    )


def should_skip_front(title: str) -> bool:
    s = slugify(title)
    return any(k in s for k in FRONT_SKIP)


def should_skip_back(title: str) -> bool:
    s = slugify(title)
    return any(k in s for k in BACK_SKIP)


def convert_section(
    section: dict,
    *,
    chapter_num: str | None,
    image_map: dict,
    heading_level: int = 2,
) -> tuple[str, list]:
    html = read_cache(section["cache"])
    conv = HtmlToMyst(
        page_url=section["url"],
        chapter_num=chapter_num,
        section_num=section_number(section["title"]),
        image_dir=Path(IMAGES),
        image_url_prefix="../images",
        image_map=image_map,
    )
    body = conv.convert(html, heading_level=heading_level)
    title = section["title"]
    # Prefer a clean heading from the LibreTexts title
    heading = "#" * heading_level + f" {title}"
    # Drop duplicate H1/H2 if converter already emitted the same title
    lines = body.splitlines()
    if lines and re.match(r"^#{1,6}\s+", lines[0]):
        first = re.sub(r"^#{1,6}\s+", "", lines[0]).strip()
        if slugify(first) == slugify(title) or first.lower() in title.lower():
            body = "\n".join(lines[1:]).lstrip()
    return f"{heading}\n\n{body}".rstrip() + "\n", conv.pending_downloads


def write_chapter(ch: dict, image_map: dict) -> list:
    num = ch["number"]
    title = f"{num}. {ch['title']}"
    label = ch["slug"]
    # A MyST target labels what *follows* it, so it has to precede the H1.
    parts = [
        front_matter(title, f"Chapter {num}", label),
        f"(ch-{num})=\n",
        f"# {title}\n",
    ]
    pending: list = []
    for sec in ch["sections"]:
        # Exercises / Summary as H2 like other sections
        text, pend = convert_section(
            sec, chapter_num=str(num), image_map=image_map, heading_level=2
        )
        parts.append(text)
        pending.extend(pend)
    out = Path(ROOT) / "chapters" / f"{label}.md"
    out.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)} ({len(ch['sections'])} sections)")
    return pending


def write_front(sections: list, image_map: dict) -> list:
    pending: list = []
    Path(ROOT, "front").mkdir(exist_ok=True)
    for sec in sections:
        if should_skip_front(sec["title"]):
            print(f"skip front {sec['title']}")
            continue
        slug = slugify(sec["title"])
        # normalize known names
        if "preface" in slug:
            slug = "preface"
        elif "prologue" in slug:
            slug = "prologue"
        text, pend = convert_section(
            sec, chapter_num=None, image_map=image_map, heading_level=2
        )
        pending.extend(pend)
        body = front_matter(sec["title"], sec["title"], slug) + f"# {sec['title']}\n\n"
        # remove the duplicate H2 we added
        text = re.sub(rf"^##\s+{re.escape(sec['title'])}\s*\n+", "", text)
        out = Path(ROOT) / "front" / f"{slug}.md"
        out.write_text(body + text, encoding="utf-8")
        print(f"wrote {out.relative_to(ROOT)}")
    return pending


def write_back(sections: list, image_map: dict) -> list:
    pending: list = []
    Path(ROOT, "back").mkdir(exist_ok=True)
    for sec in sections:
        if should_skip_back(sec["title"]):
            print(f"skip back {sec['title']}")
            continue
        slug = slugify(sec["title"])
        if "epilogue" in slug:
            slug = "epilogue"
        elif "glossary" in slug:
            slug = "glossary"
        text, pend = convert_section(
            sec, chapter_num=None, image_map=image_map, heading_level=2
        )
        pending.extend(pend)
        body = front_matter(sec["title"], sec["title"], slug) + f"# {sec['title']}\n\n"
        text = re.sub(rf"^##\s+{re.escape(sec['title'])}\s*\n+", "", text)
        out = Path(ROOT) / "back" / f"{slug}.md"
        out.write_text(body + text, encoding="utf-8")
        print(f"wrote {out.relative_to(ROOT)}")
    return pending


def write_index(outline: dict) -> None:
    book = outline["book"]
    text = f"""---
title: {book['title']}
---

# {book['title']}

by [Howard Georgi]({book['source_url']}) (Harvard University).

This MyST edition is a web-native conversion of the structured
[LibreTexts]({book['libretexts_url']}) edition of Georgi's open textbook
on vibrations and waves.

## Source and license

© Howard Georgi. Originally published by Prentice Hall (1993); rights returned
to the author for the online edition.
Licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

Suggested citation: Georgi, H. *The Physics of Waves*. Harvard University.
LibreTexts edition.

## Preview locally

```bash
npm install
npm run start
```

## Table of contents

:::{{toc}}
:context: project
:::
"""
    Path(ROOT, "index.md").write_text(text, encoding="utf-8")


def write_myst_yml(outline: dict) -> None:
    book = outline["book"]
    lines = [
        "version: 1",
        "project:",
        "  id: physics-of-waves",
        f"  title: {book['title']}",
        "  short_title: Physics of Waves",
        "  description: >-",
        "    A web-native MyST edition of Howard Georgi's open textbook on",
        "    vibrations and waves.",
        "  authors:",
        "    - name: Howard Georgi",
        "      affiliations:",
        "        - institution: Harvard University",
        "  license:",
        "    content: CC-BY-NC-SA-4.0",
        "  open_access: true",
        "  github: QuadriviumPress/physicsOfWaves",
        "  keywords:",
        "    - waves",
        "    - vibrations",
        "    - oscillations",
        "    - acoustics",
        "    - Fourier analysis",
        "  numbering:",
        "    heading_2: false",
        "    heading_3: false",
        # The book numbers its own equations; those numbers are carried through
        # as \tag{}. Auto-numbering would renumber every display equation from
        # 1 per page — including the ones marked \notag.
        "    equation: false",
        "  toc:",
        "    - file: index.md",
    ]
    # Include all generated front-matter files (sorted for stable TOC).
    front_dir = Path(ROOT) / "front"
    if front_dir.is_dir():
        for path in sorted(front_dir.glob("*.md")):
            lines.append(f"    - file: front/{path.name}")
    for ch in outline["chapters"]:
        lines.append(f"    - file: chapters/{ch['slug']}.md")
    back_dir = Path(ROOT) / "back"
    if back_dir.is_dir():
        back_files = sorted(back_dir.glob("*.md"))
        if back_files:
            lines.append("    - title: Closing")
            lines.append("      children:")
            for path in back_files:
                lines.append(f"        - file: back/{path.name}")
    lines += [
        "site:",
        "  template: book-theme",
        f"  title: {book['title']}",
        "  options:",
        "    favicon: images/favicon.svg",
        "  actions:",
        "    - title: LibreTexts edition",
        f"      url: {book['source_url']}",
        "  nav: []",
        "",
    ]
    Path(ROOT, "myst.yml").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    outline = load_outline()
    image_map: dict[str, str] = {}
    pending: list = []
    pending.extend(write_front(outline.get("front") or [], image_map))
    for ch in outline["chapters"]:
        pending.extend(write_chapter(ch, image_map))
    pending.extend(write_back(outline.get("back") or [], image_map))
    download_images(pending)
    write_index(outline)
    write_myst_yml(outline)
    # persist image map for reruns
    Path(BUILD).mkdir(parents=True, exist_ok=True)
    Path(BUILD, "image_map.json").write_text(
        json.dumps(image_map, indent=2), encoding="utf-8"
    )
    print(f"Done. {len(image_map)} images mapped.")


if __name__ == "__main__":
    main()
