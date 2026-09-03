#!/usr/bin/env python3
"""Replace hard-coded figure/equation numbers with MyST cross-references.

LibreTexts (and the converted Markdown) prints book numbers as plain text —
``Figure $9.1$``, ``(9.6)`` — with no targets to click. Georgi's PDF carries
the real numbered equations (via hyperref destinations). This pass:

1. Promotes ``![Figure](…)`` + ``Figure $N.M$: …`` into labelled figure
   directives (caption body without the hard-coded number);
2. Turns orphan ``Figure $N.M$: …`` captions (no image in LibreTexts) into
   labelled MyST targets;
3. Tags main-body display math with ``\\tag{N.M} \\label{eq-N-M}`` using the
   PDF's equation order (Problems / checklist math stays unnumbered);
4. Rewrites prose mentions into Markdown links ``[Figure 9.1](#fig-9-1)`` and
   ``[9.6](#eq-9-6)``.

Requires the book PDF at ``work/onenew.pdf`` (or ``ONENEW_PDF``). Idempotent.
"""

from __future__ import annotations

import os
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "chapters"
PDF_DEFAULT = ROOT / "work" / "onenew.pdf"
PDF_URL = (
    "https://www.dropbox.com/scl/fi/98w680pnx72z6akq5bexe/onenew.pdf"
    "?rlkey=i2u6ks8gyl1nfiamb61ep6qpe&dl=1"
)

CHAPTER_RE = re.compile(r"^ch-(\d+)-")
MATH_RE = re.compile(r"(?<!\$)\$\$(?!\$)(.+?)(?<!\$)\$\$(?!\$)", re.S)
MATH_SPAN_RE = re.compile(r"\$\$.*?\$\$|(?<!\\)\$(?:\\.|[^$\\])*\$", re.S)

BARE_FIGURE_RE = re.compile(
    r"^!\[([^\]]*)\]\(([^)]+)\)\s*\n+"
    r"(?:\*\*)?Figure\s+"
    r"(?:\$\s*(\d+(?:\.\d+)+)\s*\$|(\d+(?:\.\d+)+))"
    r"\s*:\s*(.+?)\s*(?:\*\*)?\s*$",
    re.M,
)

ORPHAN_CAPTION_RE = re.compile(
    r"^(?:\*\*)?Figure\s+"
    r"(?:\$\s*(\d+(?:\.\d+)+)\s*\$|(\d+(?:\.\d+)+))"
    r"\s*:\s*(.+?)\s*(?:\*\*)?\s*$",
    re.M,
)

# Figure number may be wrapped in $…$ (LibreTexts style).
FIGURE_MENTION_RE = re.compile(
    r"\b([Ff]igure)\s+(?:\$\s*)?(\d+(?:\.\d+)+)(?:\s*\$)?"
)

EQ_MENTION_RE = re.compile(
    r"(?<!\[)"
    r"(?P<prefix>(?:[Ee]quation|[Ee]q\.?)\s+)?"
    r"\((?P<num>\d{1,2}\.\d+)\)"
    r"(?!\])"
)

# "computer problem, (9.6)" / "see problem (3.2)" — not equation refs.
PROBLEM_CONTEXT_RE = re.compile(r"\bproblems?\b[,:]?\s*$", re.I)

CUT_RE = re.compile(
    r"(?=^::::\{admonition\} Chapter Checklist|^##\s+.*\bChecklist\b|^##\s+.*\bProblems\b|^Problems\s*$)",
    re.M | re.I,
)

# Environments where \tag must sit outside, after \end{…}.
INNER_ENV_RE = re.compile(
    r"\\begin\{(array|matrix|pmatrix|bmatrix|vmatrix|Vmatrix|cases)\}"
)


def chapter_num(path: Path) -> int | None:
    m = CHAPTER_RE.match(path.stem)
    return int(m.group(1)) if m else None


def sub_outside_display_math(pattern: re.Pattern, repl, text: str) -> str:
    """Apply ``pattern`` outside ``$$…$$`` only (inline $…$ stays in scope).

    ``repl`` receives ``(match, segment)`` so lookbehinds can use the segment
    being rewritten (match offsets are relative to that segment).
    """
    out: list[str] = []
    pos = 0
    for m in re.finditer(r"\$\$.*?\$\$", text, re.S):
        segment = text[pos : m.start()]

        def _repl(mm, seg=segment):
            return repl(mm, seg)

        out.append(pattern.sub(_repl, segment))
        out.append(m.group(0))
        pos = m.end()
    segment = text[pos:]

    def _repl_tail(mm, seg=segment):
        return repl(mm, seg)

    out.append(pattern.sub(_repl_tail, segment))
    return "".join(out)


def ensure_pdf(path: Path) -> Path:
    if path.exists() and path.stat().st_size > 1000:
        return path
    alt = Path("/tmp/onenew.pdf")
    if alt.exists() and alt.stat().st_size > 1000:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(alt.read_bytes())
        return path
    print(f"Downloading book PDF → {path}", flush=True)
    path.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(PDF_URL, headers={"User-Agent": "physicsOfWaves/1.0"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        path.write_bytes(resp.read())
    return path


def pdf_figure_numbers(pdf: Path) -> dict[int, list[str]]:
    """Ordered figure numbers per chapter from PDF named destinations."""
    data = pdf.read_bytes()
    found = set(re.findall(rb"figure\.(\d+)\.(\d+)", data))
    by_ch: dict[int, list[str]] = {}
    for ch_b, n_b in found:
        ch, n = int(ch_b), int(n_b)
        by_ch.setdefault(ch, []).append(f"{ch}.{n}")
    for ch, nums in by_ch.items():
        by_ch[ch] = sorted(nums, key=lambda s: int(s.split(".")[1]))
    return by_ch


def pdf_equation_numbers(pdf: Path) -> dict[int, list[str]]:
    """Ordered unique ``N.M`` equation tags per chapter from pdftotext."""
    import subprocess
    import tempfile

    with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as tmp:
        txt_path = Path(tmp.name)
    try:
        subprocess.run(
            ["pdftotext", "-layout", str(pdf), str(txt_path)],
            check=True,
            capture_output=True,
        )
        content = txt_path.read_text(encoding="utf-8", errors="replace")
    finally:
        txt_path.unlink(missing_ok=True)

    eq_line = re.compile(
        r"^(?P<body>.*?)\s*\((?P<num>(?P<ch>\d{1,2})\.\d+)\)\s*$", re.M
    )
    by_ch: dict[int, list[str]] = {}
    seen: dict[int, set[str]] = {}
    for m in eq_line.finditer(content):
        ch = int(m.group("ch"))
        if ch < 1 or ch > 14:
            continue
        body = m.group("body").strip()
        if not body or body.lower().startswith("figure") or "...." in body:
            continue
        num = m.group("num")
        bucket = seen.setdefault(ch, set())
        if num in bucket:
            continue
        bucket.add(num)
        by_ch.setdefault(ch, []).append(num)
    return by_ch


BARE_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")


def promote_bare_images(
    text: str, fig_numbers: list[str], chapter: int | None
) -> tuple[str, int]:
    """Wrap caption-less images, inferring numbers from nearby prose or PDF order."""
    if not fig_numbers and chapter is None:
        return text, 0

    claimed = set(re.findall(r"^:label: (fig-[\w-]+)$", text, re.M))
    claimed.update(re.findall(r"^\((fig-[\w-]+)\)=$", text, re.M))
    remaining = [
        n for n in fig_numbers if ("fig-" + n.replace(".", "-")) not in claimed
    ]

    cut = CUT_RE.search(text)
    main = text[: cut.start()] if cut else text
    tail = text[cut.start() :] if cut else ""

    ch_prefix = f"{chapter}." if chapter else None
    mention_re = (
        re.compile(rf"\b[Ff]igure\s+(?:\$\s*)?({re.escape(str(chapter))}\.\d+)")
        if chapter
        else None
    )

    n = 0
    out: list[str] = []
    pos = 0
    for m in BARE_IMAGE_RE.finditer(main):
        before = main[max(0, m.start() - 40) : m.start()]
        if re.search(r":::\{figure\}\s*$", before):
            continue

        num = None
        if mention_re:
            preceding = main[max(0, m.start() - 2500) : m.start()]
            free = []
            for mm in mention_re.finditer(preceding):
                cand = mm.group(1)
                label = "fig-" + cand.replace(".", "-")
                if label not in claimed:
                    free.append(cand)
            if free:
                # Earliest book number among recent unclaimed mentions —
                # handles "shown in fig A … and fig B" before a single image of A.
                num = min(free, key=_num_key)
            else:
                following = main[m.end() : m.end() + 200]
                for mm in mention_re.finditer(following):
                    cand = mm.group(1)
                    label = "fig-" + cand.replace(".", "-")
                    if label not in claimed:
                        num = cand
                        break
        if num is None and remaining:
            num = remaining[0]
        if num is None:
            continue

        label = "fig-" + num.replace(".", "-")
        if label in claimed:
            continue
        if num in remaining:
            remaining.remove(num)

        alt = (m.group(1) or "Figure").strip() or "Figure"
        path = m.group(2).strip()
        claimed.add(label)
        n += 1
        caption = "" if alt.lower() == "figure" else alt
        out.append(main[pos : m.start()])
        out.append(_figure_block(path, num, caption, alt))
        pos = m.end()
    out.append(main[pos:])
    return "".join(out) + tail, n


def _figure_block(path: str | None, num: str, caption: str, alt: str) -> str:
    label = "fig-" + num.replace(".", "-")
    alt_clean = re.sub(r"\$([^$]*)\$", r"\1", caption or alt)
    alt_clean = re.sub(r"\s+", " ", alt_clean).strip() or f"Figure {num}"
    if len(alt_clean) > 300:
        alt_clean = alt_clean[:297] + "…"
    if not path:
        # LibreTexts caption with no image — still provide a clickable target.
        return f"({label})=\n\n*{caption}*\n"
    return (
        f":::{{figure}} {path}\n"
        f":label: {label}\n"
        f":enumerator: {num}\n"
        f":alt: {alt_clean}\n"
        f"\n"
        f"{caption}\n"
        f":::"
    )


def promote_figures(text: str) -> tuple[str, int]:
    """Turn bare image+caption pairs into labelled ``{figure}`` directives."""
    n = 0
    claimed: set[str] = set(re.findall(r"^:label: (fig-[\w-]+)$", text, re.M))

    def from_bare(m: re.Match) -> str:
        nonlocal n
        alt = (m.group(1) or "Figure").strip() or "Figure"
        path = m.group(2).strip()
        num = (m.group(3) or m.group(4) or "").strip()
        caption = re.sub(r"\s+", " ", m.group(5)).strip()
        label = "fig-" + num.replace(".", "-")
        if label in claimed:
            return m.group(0)
        claimed.add(label)
        n += 1
        return _figure_block(path, num, caption, alt)

    pieces: list[str] = []
    pos = 0
    for m in BARE_FIGURE_RE.finditer(text):
        before = text[max(0, m.start() - 80) : m.start()]
        if re.search(r":::\{figure\}[^\n]*\s*$", before):
            continue
        pieces.append(text[pos : m.start()])
        pieces.append(from_bare(m))
        pos = m.end()
    pieces.append(text[pos:])
    text = "".join(pieces)

    # Orphan captions (LibreTexts sometimes has the caption but no image).
    def from_orphan(m: re.Match) -> str:
        nonlocal n
        num = (m.group(1) or m.group(2) or "").strip()
        caption = re.sub(r"\s+", " ", m.group(3)).strip()
        label = "fig-" + num.replace(".", "-")
        if label in claimed:
            return m.group(0)
        # Skip if this line sits inside an existing figure directive body.
        before = text[max(0, m.start() - 200) : m.start()]
        if re.search(r":::\{figure\}[^:]*$", before, re.S):
            return m.group(0)
        claimed.add(label)
        n += 1
        return _figure_block(None, num, caption, caption)

    text = ORPHAN_CAPTION_RE.sub(from_orphan, text)
    return text, n


def _attach_tag(body: str, num: str, label: str) -> str:
    """Append ``\\tag``/``\\label`` in a KaTeX-safe place."""
    tag = f" \\tag{{{num}}} \\label{{{label}}}"
    body = body.rstrip() + "\n"

    # If the outermost env is array/matrix/cases, tag after the last \end.
    # For aligned/gather/multline, tag on the last row (before \end).
    ends = list(re.finditer(r"\\end\{([^}]+)\}", body))
    if not ends:
        return body.rstrip() + tag + "\n"

    last = ends[-1]
    env = last.group(1)
    if env in {"array", "matrix", "pmatrix", "bmatrix", "vmatrix", "Vmatrix", "cases"}:
        # Walk outward: if parent is aligned/gather, put tag before that \end.
        for prev in reversed(ends[:-1]):
            if prev.group(1) in {
                "aligned",
                "align",
                "align*",
                "gather",
                "gather*",
                "multline",
                "multline*",
                "eqnarray",
                "eqnarray*",
                "gathered",
            }:
                return body[: prev.start()] + tag + "\n" + body[prev.start() :]
        return body[: last.end()] + tag + body[last.end() :]

    # aligned / gather / etc.: tag before \end{…}
    return body[: last.start()] + tag + "\n" + body[last.start() :]


def tag_equations(text: str, numbers: list[str]) -> tuple[str, int]:
    """Attach ``\\tag`` / ``\\label`` to main-body display math in book order."""
    if not numbers:
        return text, 0

    cut = CUT_RE.search(text)
    main = text[: cut.start()] if cut else text
    tail = text[cut.start() :] if cut else ""

    # Numbers already labelled in this file (e.g. partial prior conversion).
    already = set(re.findall(r"\\label\{eq-(\d+(?:-\d+)*)\}", main))
    already_nums = {a.replace("-", ".") for a in already}

    tagged = 0
    num_i = 0
    out: list[str] = []
    pos = 0
    for m in MATH_RE.finditer(main):
        out.append(main[pos : m.start()])
        body = m.group(1)

        existing_label = re.search(r"\\label\{(eq-[\w-]+)\}", body)
        existing_tag = re.search(r"\\tag\{(\d+\.\d+[a-z]?)\}", body)

        if existing_label:
            # Already fully labelled — advance PDF cursor if we can.
            slug = existing_label.group(1).removeprefix("eq-").replace("-", ".")
            while num_i < len(numbers) and _num_key(numbers[num_i]) < _num_key(slug):
                num_i += 1
            if num_i < len(numbers) and numbers[num_i] == slug:
                num_i += 1
            out.append(m.group(0))
        elif existing_tag:
            num = existing_tag.group(1)
            label = "eq-" + num.replace(".", "-")
            if f"\\label{{{label}}}" not in body:
                body = body.replace(
                    existing_tag.group(0),
                    existing_tag.group(0) + f" \\label{{{label}}}",
                    1,
                )
                tagged += 1
            out.append(f"$$\n{body.strip()}\n$$")
            while num_i < len(numbers) and _num_key(numbers[num_i]) < _num_key(num):
                num_i += 1
            if num_i < len(numbers) and numbers[num_i] == num:
                num_i += 1
        elif num_i < len(numbers):
            # Skip PDF numbers already claimed by earlier labelled blocks.
            while num_i < len(numbers) and numbers[num_i] in already_nums:
                num_i += 1
            if num_i >= len(numbers):
                out.append(m.group(0))
            else:
                num = numbers[num_i]
                num_i += 1
                label = "eq-" + num.replace(".", "-")
                body = _attach_tag(body, num, label)
                tagged += 1
                out.append(f"$$\n{body.strip()}\n$$")
        else:
            out.append(m.group(0))
        pos = m.end()
    out.append(main[pos:])
    return "".join(out) + tail, tagged


def _num_key(num: str) -> tuple[int, ...]:
    parts = re.split(r"\D+", num)
    return tuple(int(p) for p in parts if p)


def collect_labels(text: str) -> tuple[set[str], set[str]]:
    figs = set(re.findall(r"^:label: (fig-[\w-]+)$", text, re.M))
    figs.update(re.findall(r"^\((fig-[\w-]+)\)=$", text, re.M))
    eqs = set(re.findall(r"\\label\{(eq-[\w-]+)\}", text))
    return figs, eqs


def rewrite_figure_mentions(text: str, labels: set[str]) -> tuple[str, int]:
    n = 0

    def repl(m: re.Match, segment: str) -> str:
        nonlocal n
        word, num = m.group(1), m.group(2).rstrip(".")
        label = "fig-" + num.replace(".", "-")
        if label not in labels:
            return m.group(0)
        if m.start() > 0 and segment[m.start() - 1] == "[":
            return m.group(0)
        after = segment[m.end() : m.end() + 2]
        if after.startswith(":"):
            return m.group(0)
        n += 1
        return f"[{word} {num}](#{label})"

    return sub_outside_display_math(FIGURE_MENTION_RE, repl, text), n


def rewrite_equation_mentions(text: str, labels: set[str]) -> tuple[str, int]:
    n = 0

    def repl(m: re.Match, segment: str) -> str:
        nonlocal n
        num = m.group("num")
        label = "eq-" + num.replace(".", "-")
        if label not in labels:
            return m.group(0)
        lead = segment[max(0, m.start() - 48) : m.start()]
        if PROBLEM_CONTEXT_RE.search(lead):
            return m.group(0)
        prefix = m.group("prefix") or ""
        n += 1
        return f"{prefix}[{num}](#{label})"

    return sub_outside_display_math(EQ_MENTION_RE, repl, text), n


def process_all(
    eq_by_ch: dict[int, list[str]], fig_by_ch: dict[int, list[str]]
) -> dict[str, int]:
    paths = sorted(CHAPTERS.glob("ch-*.md"))
    texts: dict[Path, str] = {}
    stats: dict[Path, dict[str, int]] = {}

    for path in paths:
        original = path.read_text(encoding="utf-8")
        text = original
        st = {"figures": 0, "eq_tags": 0, "fig_refs": 0, "eq_refs": 0}
        ch = chapter_num(path)
        figs = fig_by_ch.get(ch or -1, [])
        text, n1 = promote_figures(text)
        text, n2 = promote_bare_images(text, figs, ch)
        st["figures"] = n1 + n2
        text, st["eq_tags"] = tag_equations(text, eq_by_ch.get(ch or -1, []))
        texts[path] = text
        stats[path] = st

    fig_labels: set[str] = set()
    eq_labels: set[str] = set()
    for text in texts.values():
        f, e = collect_labels(text)
        fig_labels |= f
        eq_labels |= e

    # Mentions of figures that still have no target (missing LibreTexts image):
    # add a lightweight anchor so links resolve.
    missing_figs = set()
    probe = "\n".join(texts.values())
    for m in FIGURE_MENTION_RE.finditer(probe):
        num = m.group(2).rstrip(".")
        label = "fig-" + num.replace(".", "-")
        if label not in fig_labels:
            missing_figs.add((label, num))

    for path, text in list(texts.items()):
        ch = chapter_num(path)
        extras = []
        for label, num in sorted(missing_figs):
            if not num.startswith(f"{ch}."):
                continue
            if label in collect_labels(text)[0]:
                continue
            extras.append(f"({label})=\n")
            fig_labels.add(label)
        if extras:
            # Insert before checklist/problems so anchors live in the chapter.
            cut = CUT_RE.search(text)
            block = "\n" + "\n".join(extras) + "\n"
            if cut:
                text = text[: cut.start()] + block + text[cut.start() :]
            else:
                text = text + block
            texts[path] = text

    for path, text in texts.items():
        text, stats[path]["fig_refs"] = rewrite_figure_mentions(text, fig_labels)
        text, stats[path]["eq_refs"] = rewrite_equation_mentions(text, eq_labels)
        if text != path.read_text(encoding="utf-8"):
            path.write_text(text, encoding="utf-8")

    totals = {"figures": 0, "eq_tags": 0, "fig_refs": 0, "eq_refs": 0, "files": 0}
    for path, st in stats.items():
        if any(st.values()):
            totals["files"] += 1
            for k, v in st.items():
                totals[k] += v
            print(
                f"  {path.name}: figures+{st['figures']} "
                f"tags+{st['eq_tags']} "
                f"figrefs+{st['fig_refs']} "
                f"eqrefs+{st['eq_refs']}"
            )
    return totals


def main() -> int:
    pdf = Path(os.environ.get("ONENEW_PDF", PDF_DEFAULT))
    try:
        ensure_pdf(pdf)
    except Exception as exc:  # noqa: BLE001
        print(f"error: could not obtain book PDF: {exc}", file=sys.stderr)
        return 1

    print(f"Reading equation/figure numbers from {pdf} …", flush=True)
    eq_by_ch = pdf_equation_numbers(pdf)
    fig_by_ch = pdf_figure_numbers(pdf)
    print(
        f"  {sum(len(v) for v in eq_by_ch.values())} equations, "
        f"{sum(len(v) for v in fig_by_ch.values())} figures.",
        flush=True,
    )

    totals = process_all(eq_by_ch, fig_by_ch)
    print(
        f"Updated {totals['files']} files "
        f"({totals['figures']} figures, {totals['eq_tags']} equation tags, "
        f"{totals['fig_refs']} figure links, {totals['eq_refs']} equation links)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
