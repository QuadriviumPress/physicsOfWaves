"""Convert LibreTexts HTML content into MyST Markdown."""

from __future__ import annotations

import html as html_lib
import re
from pathlib import Path
from urllib.parse import urljoin, urlparse, unquote

from bs4 import BeautifulSoup, NavigableString, Tag

SKIP_FOOTER_RE = re.compile(
    r"^(Contributors and Attributions|Footnotes|References|This page titled)",
    re.I,
)
PAGEINDEX_RE = re.compile(r"\\PageIndex\{(\d+)\}")

# LibreTexts writes counters as \(\PageIndex{1}\) and expands them, at render
# time, against the *section* the counter appears in: \PageIndex{1} inside
# section 5.2 means "5.2.1".  The section number therefore has to be supplied
# here — prefixing with the chapter number instead collapses every figure in a
# chapter onto a handful of numbers.
PAGEINDEX_ANY_RE = re.compile(
    r"\\\(\s*\\PageIndex\{([^{}]*)\}\s*\\\)"   # \(\PageIndex{1}\)
    r"|\$\\PageIndex\{([^{}]*)\}\$"            # $\PageIndex{1}$
    r"|\\PageIndex\{([^{}]*)\}"                # bare
)


def scrub_pageindex(text: str, section: str | None = None) -> str:
    """Expand LibreTexts \\PageIndex{n} to "<section>.<n>" (or bare "n")."""

    def repl(m: re.Match) -> str:
        n = next(g for g in m.groups() if g is not None).strip()
        return f"{section}.{n}" if section else n

    return PAGEINDEX_ANY_RE.sub(repl, text)



def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[-\s]+", "-", text).strip("-")
    return text[:80] or "section"


def decode_entities(text: str) -> str:
    text = html_lib.unescape(text)
    text = text.replace("\xa0", " ")
    return text


def clean_math(tex: str) -> str:
    tex = decode_entities(tex)
    tex = tex.replace("\u200b", "")
    # The source uses a bare % as a soft line break, but it is a LaTeX comment:
    # everything after it — including the closing delimiter — is swallowed.
    tex = re.sub(r"(?<!\\)%", "", tex)
    # Blank lines inside $$…$$ break CommonMark/MyST math fencing, so KaTeX
    # never sees the equation and raw $$ / \begin{array} leak into the HTML.
    tex = re.sub(r"\n\s*\n+", "\n", tex)
    # LibreTexts often uses \[4pt] spacing in align — keep as-is (valid amsmath)
    return tex.strip()


# A row break inside amsmath is "\\", so "\\(" is a break followed by an open
# paren, not an inline-math delimiter. The lookbehind keeps it that way.
DISPLAY_MATH_RE = re.compile(r"(?<!\\)\\\[(.*?)(?<!\\)\\\]", re.S)
INLINE_MATH_RE = re.compile(r"(?<!\\)\\\((.*?)(?<!\\)\\\)", re.S)
EQUATION_ENV_RE = re.compile(r"\\begin\{(equation\*?)\}(.*?)\\end\{\1\}", re.S)


def normalize_inline_math(text: str) -> str:
    """Turn \\( \\) / \\[ \\] into $ / $$ forms used by MyST."""

    def repl_display(m: re.Match) -> str:
        body = clean_math(m.group(1))
        # Display math occasionally wraps inline delimiters; leaving them in
        # would nest $…$ inside $$…$$, which KaTeX rejects.
        body = INLINE_MATH_RE.sub(lambda i: i.group(1), body)
        return f"\n$$\n{body}\n$$\n"

    def repl_inline(m: re.Match) -> str:
        return f"${clean_math(m.group(1))}$"

    text = DISPLAY_MATH_RE.sub(repl_display, text)
    # A handful of LibreTexts pages write \begin{equation}…\end{equation} with
    # no \[ \] around it; without this it reaches the reader as raw LaTeX.
    text = EQUATION_ENV_RE.sub(
        lambda m: "\n$$\n" + clean_math(m.group(2)) + "\n$$\n", text
    )
    text = INLINE_MATH_RE.sub(repl_inline, text)
    return text


def inline_math_only(text: str) -> str:
    """Normalise math for a context that cannot hold a display block."""
    text = DISPLAY_MATH_RE.sub(lambda m: f"${clean_math(m.group(1))}$", text)
    text = INLINE_MATH_RE.sub(lambda m: f"${clean_math(m.group(1))}$", text)
    return text


def figure_enumerator(caption: str) -> tuple[str, str]:
    """Return (enumerator, cleaned caption).

    \\PageIndex has already been expanded by the time this runs, so the caption
    reads "Figure 5.2.1: ..." and the enumerator is taken verbatim.
    """
    cap = re.sub(r"^Figure\s+", "", caption, flags=re.I).strip()
    # Segments can be alphanumeric: exercise sections number as "6.E.1".
    m = re.match(r"^(\d+(?:\.[0-9A-Za-z]+)+)\s*:\s*(.*)$", cap, re.S)
    if m:
        return m.group(1), m.group(2).strip()
    m = re.match(r"^(\d+(?:\.[0-9A-Za-z]+)+)\s*$", cap)
    if m:
        return m.group(1), ""
    return "", cap


def figure_label(enum: str) -> str:
    return "fig-" + enum.replace(".", "-")


def alt_text(caption: str, fallback: str) -> str:
    """Prefer the caption over LibreTexts' filename-as-alt-text."""
    if re.fullmatch(r"[\w.\- ]+\.(png|jpe?g|gif|svg)", fallback or "", re.I):
        fallback = ""
    text = re.sub(r"\s+", " ", (caption or fallback or "Figure")).strip()
    text = re.sub(r"\$([^$]*)\$", r"\1", text)  # alt text cannot hold math
    return (text[:297] + "…") if len(text) > 300 else text


def download_name_from_url(url: str) -> str:
    path = unquote(urlparse(url).path)
    name = Path(path).name
    name = re.sub(r"[^\w.\-]+", "_", name)
    if not name or name == "files":
        name = "image.png"
    return name.lower()


class HtmlToMyst:
    def __init__(
        self,
        *,
        page_url: str,
        chapter_num: str | None = None,
        section_num: str | None = None,
        image_dir: Path,
        image_url_prefix: str = "../images",
        image_map: dict[str, str] | None = None,
    ):
        self.page_url = page_url
        self.chapter_num = chapter_num
        self.section_num = section_num
        self.image_dir = image_dir
        self.image_url_prefix = image_url_prefix
        self.image_map = image_map if image_map is not None else {}
        self.pending_downloads: list[tuple[str, Path]] = []
        self.figure_labels: list[str] = []

    def convert(self, html: str, *, heading_level: int = 2) -> str:
        # Expand \PageIndex against this section before anything else looks at
        # the text: figure captions, example legends and prose references all
        # depend on it, and normalize_inline_math() would otherwise bury the
        # counter inside a $…$ span where nothing can read it.
        html = scrub_pageindex(html, self.section_num)
        soup = BeautifulSoup(html, "html.parser")
        main = (
            soup.select_one("#mt-content-container")
            or soup.select_one(".mt-content-container")
            or soup.select_one("#elm-main-content")
        )
        if main is None:
            return ""

        # Drop LibreTexts chrome inside content
        for sel in (
            "script",
            "style",
            "nav",
            ".lt-discussion",
            ".printfooter",
            "#printfooter",
            ".noprint",
            ".hidden",
            "footer",
        ):
            for el in main.select(sel):
                el.decompose()

        self._normalize_figures(main, soup)

        parts: list[str] = []
        for child in list(main.children):
            chunk = self._render_node(child, heading_level=heading_level)
            if chunk and chunk.strip():
                parts.append(chunk.strip())
        text = "\n\n".join(parts)
        text = normalize_inline_math(text)
        text = self._link_footnotes(text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip() + "\n"

    CAPTION_START_RE = re.compile(r"^\s*Figure\s+\d", re.I)
    BLOCK_IN_LI = ("figure", "table", "ul", "ol", "blockquote", "div")

    def _list_item(self, li: Tag, *, heading_level: int = 2) -> str:
        """Render a list item, keeping any block content (an exercise figure,
        a nested list) as a block rather than flattening it into the text."""
        if not li.find(self.BLOCK_IN_LI):
            return self._inline(li).strip()
        parts: list[str] = []
        for child in li.children:
            chunk = self._render_node(child, heading_level=heading_level)
            if chunk and chunk.strip():
                parts.append(chunk.strip())
        return "\n\n".join(parts).strip()

    def _normalize_figures(self, main: Tag, soup: BeautifulSoup) -> None:
        """Reduce LibreTexts' two figure markups to <figure><figcaption>.

        Most pages use <figure>, but some put the <img> *inside* the
        <figcaption>, and others use a bare <p><img></p> followed by a
        <p>Figure n: …</p>. Only the first form carries a caption through the
        renderer, so the rest lose their number and their description.
        """
        # (1) <figure><figcaption><img>…</figcaption></figure>, and
        #     <figure><img><p>Figure n: …</p></figure> with no <figcaption>
        for fig in main.find_all("figure"):
            cap = fig.find("figcaption")
            if cap is None:
                for p in fig.find_all("p"):
                    if self.CAPTION_START_RE.match(p.get_text(" ", strip=True)):
                        p.name = "figcaption"
                        cap = p
                        break
            if cap is None:
                continue
            img = cap.find("img")
            if img is None:
                continue
            if fig.find("img") is img:      # the only image — hoist it out
                cap.insert_before(img.extract())
            for br in cap.find_all("br"):
                br.decompose()

        # (2) <p><img></p> + <p>Figure n: …</p>
        for p in list(main.find_all("p")):
            if p.parent is None:
                continue
            imgs = p.find_all("img")
            if len(imgs) != 1 or p.get_text(strip=True):
                continue
            cap_p = p.find_next_sibling()
            if cap_p is None or cap_p.name != "p":
                continue
            if not self.CAPTION_START_RE.match(cap_p.get_text(" ", strip=True)):
                continue
            figure = soup.new_tag("figure")
            caption = soup.new_tag("figcaption")
            p.insert_before(figure)
            figure.append(imgs[0].extract())
            for child in list(cap_p.children):
                caption.append(child.extract())
            figure.append(caption)
            p.decompose()
            cap_p.decompose()

    def _link_footnotes(self, text: str) -> str:
        """Turn LibreTexts' <sup>n</sup> notes into real MyST footnotes.

        A note is a top-level paragraph that *starts* with <sup>n</sup>; only
        markers whose number has such a definition in the same section are
        rewritten, so ordinary exponents (18<sup>th</sup>, x<sup>2</sup>) are
        left alone.
        """
        defs = {
            m.group(1)
            for m in re.finditer(r"^<sup>(\d+)</sup>\s*(?=\S)", text, re.M)
        }
        markers = {
            m.group(1)
            for m in re.finditer(r"(?<!\n)<sup>(\d+)</sup>", text)
        }
        # A note whose marker sits in another section stays as it is: MyST drops
        # a footnote definition that nothing references, which would lose it.
        defs &= markers
        if not defs:
            return text
        prefix = (self.section_num or "n").replace(".", "-")

        def repl_def(m: re.Match) -> str:
            return f"[^{prefix}-{m.group(1)}]: "

        def repl_marker(m: re.Match) -> str:
            n = m.group(1)
            return f"[^{prefix}-{n}]" if n in defs else m.group(0)

        text = re.sub(r"<sup>(\d+)</sup>", repl_marker, text)
        text = re.sub(rf"^\[\^{prefix}-(\d+)\]\s*(?=\S)", repl_def, text, flags=re.M)
        # A note definition must not be swallowed by the rule above it.
        text = re.sub(r"^---\n+(?=\[\^)", "", text, flags=re.M)
        return text

    def _render_node(self, node, heading_level: int = 2) -> str:
        if isinstance(node, NavigableString):
            s = str(node)
            if not s.strip():
                return ""
            return decode_entities(s.strip())

        if not isinstance(node, Tag):
            return ""

        name = node.name.lower()

        if name in ("script", "style", "nav"):
            return ""

        if name in ("h1", "h2", "h3", "h4", "h5", "h6"):
            level = int(name[1])
            # remap: page section title → heading_level
            hashes = "#" * min(heading_level + level - 1, 6)
            title = decode_entities(node.get_text(" ", strip=True))
            title = PAGEINDEX_RE.sub(r"\1", title)
            if SKIP_FOOTER_RE.match(title):
                return ""
            return f"{hashes} {title}"

        if name == "p":
            text = self._inline(node)
            text = text.strip()
            if not text:
                return ""
            if SKIP_FOOTER_RE.match(text):
                return ""
            if text.startswith("Howard Georgi") or text.startswith("Douglas Cline"):
                return ""
            return text

        if name in ("ul", "ol"):
            items = []
            ordered = name == "ol"
            for i, li in enumerate(node.find_all("li", recursive=False), 1):
                body = self._list_item(li, heading_level=heading_level)
                if not body:
                    continue
                prefix = f"{i}." if ordered else "-"
                indent = " " * (len(prefix) + 1)
                first, *rest = body.split("\n")
                lines = [f"{prefix} {first}"]
                lines += [indent + ln if ln else "" for ln in rest]
                items.append("\n".join(lines))
            return "\n\n".join(items)

        if name == "blockquote":
            body = self._inline(node).strip()
            return "\n".join(f"> {ln}" if ln else ">" for ln in body.splitlines())

        if name == "figure":
            return self._figure(node)

        if name == "img":
            return self._image_only(node)

        if name == "table":
            return self._table(node)

        if name == "hr":
            return "---"

        if name == "div" and any(
            c.startswith("box-") for c in (node.get("class") or [])
        ):
            return self._box(node, heading_level=heading_level)

        if name in ("div", "section", "span", "article"):
            # unwrap containers
            parts = []
            for child in node.children:
                chunk = self._render_node(child, heading_level=heading_level)
                if chunk and chunk.strip():
                    parts.append(chunk.strip())
            return "\n\n".join(parts)

        if name in ("dl",):
            parts = []
            for child in node.children:
                if getattr(child, "name", None) == "dt":
                    parts.append(f"**{self._inline(child).strip()}**")
                elif getattr(child, "name", None) == "dd":
                    parts.append(self._inline(child).strip())
            return "\n\n".join(p for p in parts if p)

        # fallback: inline text
        return self._inline(node)

    def _inline(self, node: Tag) -> str:
        bits: list[str] = []
        for child in node.children:
            if isinstance(child, NavigableString):
                bits.append(decode_entities(str(child)))
                continue
            if not isinstance(child, Tag):
                continue
            n = child.name.lower()
            if n in ("br",):
                bits.append("\n")
            elif n in ("strong", "b"):
                bits.append(f"**{self._inline(child).strip()}**")
            elif n in ("em", "i"):
                bits.append(f"*{self._inline(child).strip()}*")
            elif n == "code":
                bits.append(f"`{child.get_text()}`")
            elif n == "a":
                href = child.get("href") or ""
                label = self._inline(child).strip() or href
                if href.startswith("http") or href.startswith("/"):
                    href = urljoin(self.page_url, href)
                    bits.append(f"[{label}]({href})")
                else:
                    bits.append(label)
            elif n == "sub":
                bits.append(f"<sub>{self._inline(child)}</sub>")
            elif n == "sup":
                bits.append(f"<sup>{self._inline(child)}</sup>")
            elif n == "img":
                # Inline context (a table cell, a run of text): a block-level
                # figure directive here would break the surrounding structure.
                bits.append(self._inline_image(child))
            elif n == "span":
                bits.append(self._inline(child))
            else:
                bits.append(self._inline(child))
        text = "".join(bits)
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"[ \t]{2,}", " ", text)
        return text

    def _register_image(self, src: str) -> str:
        abs_url = urljoin(self.page_url, src)
        # strip query for filename stability but keep URL with revision for fetch
        base_name = download_name_from_url(abs_url.split("?")[0])
        # uniquify by path hash fragment if collision
        if abs_url not in self.image_map:
            dest_name = base_name
            dest = self.image_dir / dest_name
            n = 1
            while dest.exists() and self.image_map.get(abs_url) != dest_name:
                # allow reuse if same file already mapped elsewhere with same name
                stem, suf = Path(base_name).stem, Path(base_name).suffix
                dest_name = f"{stem}-{n}{suf}"
                dest = self.image_dir / dest_name
                n += 1
                if any(v == dest_name for v in self.image_map.values()):
                    # already planned for another URL — keep looping
                    continue
                break
            # simpler: use content-derived unique name from file id
            m = re.search(r"/files/(\d+)/", abs_url)
            if m:
                dest_name = f"lt-{m.group(1)}-{base_name}"
            self.image_map[abs_url] = dest_name
            self.pending_downloads.append((abs_url, self.image_dir / dest_name))
        return f"{self.image_url_prefix}/{self.image_map[abs_url]}"

    def _box(self, node: Tag, *, heading_level: int = 2) -> str:
        """Render a LibreTexts box-* div (examples, notes) as an admonition.

        Unwrapping these into bare paragraphs, as the generic div branch does,
        loses both the title and the boundary — the reader cannot tell where a
        worked example starts or ends.
        """
        kind = next(
            (c[4:] for c in (node.get("class") or []) if c.startswith("box-")),
            "note",
        )
        legend = node.find(
            lambda t: t.name == "p" and "box-legend" in (t.get("class") or [])
        )
        title = ""
        if legend is not None:
            title = normalize_inline_math(self._inline(legend).strip())
            legend.decompose()

        parts: list[str] = []
        for child in node.children:
            chunk = self._render_node(child, heading_level=heading_level)
            if chunk and chunk.strip():
                parts.append(chunk.strip())
        body = "\n\n".join(parts).strip()
        if not body and not title:
            return ""

        # Four colons so nested figures (which use three) still close cleanly.
        head = f"::::{{admonition}} {title}" if title else "::::{note}"
        lines = [head]
        if title:
            lines.append(f":class: {kind}")
        lines.append("")
        lines.append(body)
        lines.append("::::")
        return "\n".join(lines)

    def _figure(self, node: Tag) -> str:
        img = node.find("img")
        if img is None:
            return self._inline(node).strip()
        src = img.get("src") or ""
        alt = img.get("alt") or "Figure"
        path = self._register_image(src)
        cap_el = node.find("figcaption")
        caption = self._inline(cap_el).strip() if cap_el else ""
        caption = normalize_inline_math(caption)
        enum, cap_body = figure_enumerator(caption)
        caption_text = cap_body or (caption if not enum else "")
        lines = [f":::{{figure}} {path}"]
        if enum:
            label = figure_label(enum)
            self.figure_labels.append(label)
            lines.append(f":label: {label}")
            lines.append(f":enumerator: {enum}")
        else:
            lines.append(":enumerated: false")
        # LibreTexts alt text is just the source filename; the caption is a far
        # better description for anyone using a screen reader.
        lines.append(f":alt: {alt_text(caption_text, alt)}")
        if caption_text:
            lines.append("")
            lines.append(caption_text)
        lines.append(":::")
        return "\n".join(lines)

    def _inline_image(self, node: Tag) -> str:
        src = node.get("src") or ""
        if not src or "logo" in src.lower() or "favicon" in src.lower():
            return ""
        path = self._register_image(src)
        return f"![{alt_text('', node.get('alt') or '')}]({path})"

    def _image_only(self, node: Tag) -> str:
        src = node.get("src") or ""
        if not src or "logo" in src.lower() or "favicon" in src.lower():
            return ""
        alt = node.get("alt") or "Illustration"
        path = self._register_image(src)
        return (
            f":::{{figure}} {path}\n"
            f":enumerated: false\n"
            f":alt: {alt_text('', alt)}\n:::"
        )

    # LibreTexts ships an instructional first table in every glossary, with a
    # worked example from a biology text. It is scaffolding, not book content.
    GLOSSARY_TEMPLATE_RE = re.compile(
        r"Words \(or words that have the same definition\)", re.I
    )

    def _table(self, node: Tag) -> str:
        if self.GLOSSARY_TEMPLATE_RE.search(node.get_text(" ", strip=True)):
            return ""

        head_rows, body_rows = [], []
        thead = node.find("thead")
        for tr in node.find_all("tr"):
            # A cell has to stay on one line: a pipe row cannot contain a
            # newline, and a list-table item would end at a blank line. Its
            # display math has to become inline math for the same reason.
            cells = [
                re.sub(r"\s*\n\s*", " ", inline_math_only(self._inline(td))).strip()
                for td in tr.find_all(["th", "td"])
            ]
            if not cells:
                continue
            in_head = (thead is not None and tr.find_parent("thead") is thead) or (
                thead is None
                and not body_rows
                and not head_rows
                and tr.find("th") is not None
            )
            (head_rows if in_head else body_rows).append(cells)
        rows = head_rows + body_rows
        if not rows:
            return ""
        width = max(len(r) for r in rows)
        head_rows = [r + [""] * (width - len(r)) for r in head_rows]
        body_rows = [r + [""] * (width - len(r)) for r in body_rows]

        if not head_rows:
            # A pipe table always renders its first row as a header, which
            # promotes data (an exercise item, a definition) to a column title.
            # list-table carries no header unless one is declared.
            lines = ["::::{list-table}"]
            for r in body_rows:
                for i, cell in enumerate(r):
                    lines.append(("* - " if i == 0 else "  - ") + (cell or " "))
            lines.append("::::")
            return "\n".join(lines)

        def row(cells: list[str]) -> str:
            return "| " + " | ".join(c.replace("|", "\\|") for c in cells) + " |"

        lines = [row(head_rows[0])]
        lines.append("| " + " | ".join("---" for _ in range(width)) + " |")
        for r in head_rows[1:] + body_rows:
            lines.append(row(r))
        return "\n".join(lines)
