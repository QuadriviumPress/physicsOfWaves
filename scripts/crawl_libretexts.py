"""Crawl the LibreTexts edition and cache HTML + outline.json."""

from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import unquote, urljoin

from bs4 import BeautifulSoup

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import HTML_CACHE, LIBRETEXTS_BASE, OUTLINE, USER_AGENT
from html_to_myst import slugify

DELAY_S = 0.35


def fetch(url: str, retries: int = 4) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    last = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=90) as resp:
                return resp.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as exc:
            last = exc
            if exc.code in (429, 500, 502, 503, 504):
                time.sleep(1.5 * (attempt + 1))
                continue
            raise
        except Exception as exc:  # noqa: BLE001
            last = exc
            time.sleep(1.0 * (attempt + 1))
    raise RuntimeError(f"Failed to fetch {url}: {last}")


def cache_path_for(url: str) -> Path:
    rel = url[len(LIBRETEXTS_BASE) :].lstrip("/") if url.startswith(LIBRETEXTS_BASE) else url
    rel = unquote(rel).replace(":", "_").replace("/", "__")
    if not rel:
        rel = "index"
    safe = re.sub(r"[^\w.\-]+", "_", rel)
    return Path(HTML_CACHE) / f"{safe}.html"


def child_pages(url: str, html: str) -> list[tuple[str, str]]:
    soup = BeautifulSoup(html, "html.parser")
    out: list[tuple[str, str]] = []
    for a in soup.find_all("a", href=True):
        href = urljoin(url, a["href"]).split("#")[0]
        if not href.startswith(LIBRETEXTS_BASE):
            continue
        if href.rstrip("/") == url.rstrip("/"):
            continue
        if not href.startswith(url.rstrip("/") + "/"):
            continue
        # only direct children (one extra path segment)
        rest = href[len(url.rstrip("/")) + 1 :]
        if "/" in rest.rstrip("/"):
            continue
        title = a.get_text(" ", strip=True)
        if not title or len(title) > 160:
            continue
        # skip "next/prev" chrome
        if title.lower() in {"next", "previous", "back", "home"}:
            continue
        out.append((title, href))
    seen = set()
    uniq = []
    for t, h in out:
        if h not in seen:
            seen.add(h)
            uniq.append((t, h))
    return uniq


def parse_chapter_meta(title: str, url: str) -> dict:
    m = re.match(r"^(\d+)\s*:\s*(.+)$", title.strip())
    if m:
        num = int(m.group(1))
        name = m.group(2).strip()
        slug = f"ch-{num:02d}-{slugify(name)}"
        return {"kind": "chapter", "number": num, "title": name, "slug": slug, "url": url}
    if "Front_Matter" in url or title.lower().startswith("front"):
        return {"kind": "front", "title": "Front Matter", "slug": "front", "url": url}
    if "Back_Matter" in url or title.lower().startswith("back"):
        return {"kind": "back", "title": "Back Matter", "slug": "back", "url": url}
    return {"kind": "other", "title": title, "slug": slugify(title), "url": url}


def section_slug(title: str, chapter_num: int | None) -> str:
    # "5.2: Euler's ..." or "5.E: ..."
    m = re.match(r"^(\d+)\.([0-9A-Za-z]+)\s*:\s*(.+)$", title.strip())
    if m:
        sec = m.group(2).lower()
        name = slugify(m.group(3))
        return f"{int(m.group(1)):02d}-{sec}-{name}"
    m2 = re.match(r"^(\d+)\.([0-9A-Za-z]+)\b", title.strip())
    if m2:
        return f"{int(m2.group(1)):02d}-{m2.group(2).lower()}-{slugify(title)}"
    return slugify(title)


def crawl() -> dict:
    os.makedirs(HTML_CACHE, exist_ok=True)
    root_html = fetch(LIBRETEXTS_BASE)
    cache_path_for(LIBRETEXTS_BASE).write_text(root_html, encoding="utf-8")
    time.sleep(DELAY_S)

    top = child_pages(LIBRETEXTS_BASE, root_html)
    outline: dict = {
        "book": {
            "title": "The Physics of Waves",
            "authors": ["Howard Georgi"],
            "license": "CC-BY-NC-SA-4.0",
            "source_url": LIBRETEXTS_BASE,
            "libretexts_url": LIBRETEXTS_BASE,
        },
        "front": [],
        "chapters": [],
        "back": [],
    }

    for title, url in top:
        meta = parse_chapter_meta(title, url)
        print(f"→ {title}", flush=True)
        html = fetch(url)
        cache_path_for(url).write_text(html, encoding="utf-8")
        time.sleep(DELAY_S)
        kids = child_pages(url, html)
        sections = []
        for stitle, surl in kids:
            print(f"   · {stitle}", flush=True)
            shtml = fetch(surl)
            cache_path_for(surl).write_text(shtml, encoding="utf-8")
            time.sleep(DELAY_S)
            sections.append(
                {
                    "title": stitle,
                    "url": surl,
                    "cache": str(cache_path_for(surl).relative_to(Path(HTML_CACHE).parent.parent)
                                  if False else cache_path_for(surl).name),
                    "slug": section_slug(stitle, meta.get("number")),
                }
            )
            # fix cache field properly
            sections[-1]["cache"] = cache_path_for(surl).name

        entry = {
            **meta,
            "cache": cache_path_for(url).name,
            "sections": sections,
        }
        if meta["kind"] == "chapter":
            outline["chapters"].append(entry)
        elif meta["kind"] == "front":
            outline["front"] = sections
        elif meta["kind"] == "back":
            outline["back"] = sections
        else:
            outline.setdefault("other", []).append(entry)

    outline["chapters"].sort(key=lambda c: c["number"])
    Path(OUTLINE).write_text(json.dumps(outline, indent=2), encoding="utf-8")
    print(f"Wrote {OUTLINE} with {len(outline['chapters'])} chapters, "
          f"{len(outline['front'])} front, {len(outline['back'])} back pages.")
    return outline


if __name__ == "__main__":
    crawl()
