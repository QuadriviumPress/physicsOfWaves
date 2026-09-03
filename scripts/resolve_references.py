#!/usr/bin/env python3
"""Resolve the book's own numbering scheme into MyST cross-references.

LibreTexts carries the book's equation numbers as ``\\label{5.6}`` on the
equation and ``\\ref{5.6}`` in the prose, both of which MyST knows nothing
about: ``\\ref`` survives into the page as literal text, and MyST renumbers
every display equation sequentially instead of using the book's number.

This pass rewrites both sides so they agree:

* every labelled equation keeps the book's number as a KaTeX ``\\tag{}``
  (auto-numbering is off in ``myst.yml``, so nothing else is numbered);
* ``\\label{5.6}`` becomes a filename-safe MyST identifier;
* ``\\ref{5.6}`` becomes a link to it, whose text is the book's number;
* prose mentions of "Figure 5.2.1" link to the figure of that number.

Idempotent: safe to re-run after convert.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIRS = [ROOT / "chapters", ROOT / "front", ROOT / "back"]

CHAPTER_NUM = re.compile(r"^ch-(\d+)-")
LABEL_RE = re.compile(r"\\label\{([^}]*)\}")
TAG_RE = re.compile(r"\\tag\{((?:[^{}]|\{[^{}]*\})*)\}")
REF_RE = re.compile(r"\\(?:eq)?ref\{([^}]*)\}")
MATH_BLOCK_RE = re.compile(r"^\$\$\n(.*?)\n\$\$", re.S | re.M)
# amsmath row separator: \\ optionally followed by a spacing argument
ROW_SPLIT_RE = re.compile(r"(?<!\\)\\\\(?:\[[^\]]*\])?")
# "5.6", "eq:5.6", "A.12" — the forms LibreTexts uses for a printed number
BOOK_NUMBER_RE = re.compile(r"^(?:eq:\s*)?(\d+\.\d+[a-z]?|[A-Z]\.\d+)$")


def chapter_num(path: Path) -> str | None:
    m = CHAPTER_NUM.match(path.stem)
    return (m.group(1).lstrip("0") or "0") if m else None


# --------------------------------------------------------------------------
# hand-fixed source errors
# --------------------------------------------------------------------------


def fix_hard_errors(path: Path, text: str) -> str:
    name = path.name

    if name == "ch-02-review-of-newtonian-mechanics.md":
        text = text.replace(
            r"\Delta U_{a \rightarrow b} & = & -",
            r"\Delta U_{a \rightarrow b} &= -",
        )
        text = text.replace(r"\\ & = & -Gm_1m_0", r"\\ &= -Gm_1m_0")

    if name == "ch-04-nonlinear-systems-and-chaos.md":
        # KaTeX has no \dddot
        text = text.replace(r"\dddot{", r"\overset{\ldots}{")

    if name == "ch-07-symmetries-invariance-and-the-hamiltonian.md":
        text = text.replace(
            r"$L(q_{i},\dot{q_{i}% },\ddot{q_{i}},t)$",
            r"$L(q_{i},\dot{q_{i}},\ddot{q_{i}},t)$",
        )
        text = text.replace(r"\frac{% \partial L}", r"\frac{\partial L}")
        text = text.replace(
            r"a Lagrangian multiplier $% \lambda$ introduced.",
            r"a Lagrangian multiplier $\lambda$ introduced.",
        )
        text = text.replace(r"and mass $% m$ with", r"and mass $m$ with")

    if name == "ch-12-non-inertial-reference-frames.md":
        text = text.replace(
            r"\frac{d}{dt} (mr'' ^2 \omega )",
            r"\frac{d}{dt} (m r^{\prime\prime 2} \omega )",
        )

    if name == "ch-16-analytical-formulations-for-continuous-systems.md":
        text = text.replace(r"(q_{j-1} – q_j)", r"(q_{j-1} - q_j)")

    text = text.replace("\u00ad", "").replace("\u200b", "")
    return text


def rename_ch14_labels(text: str) -> str:
    """Chapter 14 carries second-edition numbering (12.x) from LibreTexts."""
    text = re.sub(r"\\label\{12\.(\d+(?:\.\d+)*)\}", r"\\label{14.\1}", text)
    text = re.sub(r"\\(eqref|ref)\{12\.(\d+(?:\.\d+)*)\}", r"\\\1{14.\2}", text)
    return text


# --------------------------------------------------------------------------
# labels
# --------------------------------------------------------------------------


def anchor_for(label: str, chapter: str | None) -> str:
    """Filename-safe MyST identifier for a LibreTexts label."""
    body = re.sub(r"^eq:\s*", "", label.strip())
    # Already converted by fix_crossrefs.py — leave alone.
    if re.fullmatch(r"eq-\d+(?:-\d+[a-z]?)*", body):
        return body
    slug = re.sub(r"[^0-9a-zA-Z]+", "-", body).strip("-").lower()
    if not slug:
        slug = "eq"
    if BOOK_NUMBER_RE.match(label.strip()):
        # A printed equation number is unique across the whole book.
        return f"eq-{slug}"
    # Ad-hoc ids ("a", "alpha", "b1") repeat in every chapter that uses them.
    return f"eq-{chapter}-{slug}" if chapter else f"eq-{slug}"


def display_number(label: str) -> str | None:
    m = BOOK_NUMBER_RE.match(label.strip())
    return m.group(1) if m else None


def clean_tag(tag: str) -> str:
    """"$A$" -> "A", "\\text{b}" -> "b"."""
    tag = tag.strip()
    tag = re.sub(r"^\$(.*)\$$", r"\1", tag).strip()
    tag = re.sub(r"^\\(?:text|mathrm)\{(.*)\}$", r"\1", tag).strip()
    return tag


def ref_text(number: str) -> str:
    """Link text for a reference; a Greek tag has to stay math."""
    return f"${number}$" if "\\" in number else number


def fix_tag_math(text: str) -> str:
    """KaTeX typesets \\tag{} in text mode, where \\alpha is undefined.

    The source tags equations with bare commands ("\\tag{ \\alpha }"), which
    MathJax reads as math. Wrapping restores that reading.
    """

    def repl(m: re.Match) -> str:
        body = m.group(1).strip()
        if "\\" not in body:
            return m.group(0)
        if body.startswith("$") and body.endswith("$"):
            return m.group(0)
        # A tag that mixes text and math ("k, $\lambda$ > 0") has to become one
        # math span; nesting $…$ inside $…$ is a KaTeX error.
        return rf"\tag{{${body.replace('$', '')}$}}"

    return TAG_RE.sub(repl, text)


class LabelBook:
    """Assigns each \\label{} a unique MyST identifier.

    Two kinds of label need opposite treatment:

    * A printed equation number ("5.6") identifies one equation for the whole
      book. Summaries and later chapters restate those equations, labels
      included, which would give MyST several nodes claiming one identifier —
      so only the first definition keeps the label and the rest point at it.
      Matching on the number, rather than on whether the heading says
      "summary", is what stops an ordinary section like "18.2: Brief summary
      of the origins of quantum theory" from losing its only labels.
    * An ad-hoc id ("a", "alpha", "b1") is local to one worked example and is
      reused freely, so each occurrence needs its own identifier and a
      reference resolves to the nearest one above it.
    """

    def __init__(self) -> None:
        self.numbers: dict[str, tuple[str, str | None]] = {}
        self.restated: dict[str, int] = {}
        self.adhoc: dict[str, list[str]] = {}   # anchor -> [raw label]
        self.counts: dict[str, int] = {}

    def start_file(self) -> None:
        self.adhoc = {}
        self.counts = {}

    def assign(
        self, label: str, chapter: str | None, number: str | None
    ) -> tuple[str, str | None, bool]:
        """Return (anchor, printed number, keep_label)."""
        if display_number(label):
            anchor = anchor_for(label, chapter)
            if anchor in self.numbers:
                self.restated[anchor] = self.restated.get(anchor, 0) + 1
                return self.numbers[anchor][0], self.numbers[anchor][1], False
            self.numbers[anchor] = (anchor, number or display_number(label))
            return anchor, self.numbers[anchor][1], True

        base = anchor_for(label, chapter)
        self.counts[base] = self.counts.get(base, 0) + 1
        anchor = base if self.counts[base] == 1 else f"{base}-{self.counts[base]}"
        self.adhoc.setdefault(anchor, []).append(label)
        return anchor, number, True

    def alias(self, label: str, own_anchor: str, primary: str) -> None:
        """Point a label that could not keep its own identifier at `primary`."""
        if display_number(label):
            self.numbers[own_anchor] = (primary, self.numbers[own_anchor][1])
        else:
            self.adhoc.pop(own_anchor, None)
            self.adhoc.setdefault(primary, []).append(label)

    def lookup_number(self, label: str) -> tuple[str, str | None] | None:
        anchor = anchor_for(label, None)
        entry = self.numbers.get(anchor)
        return entry if entry else None


def relabel_equations(
    text: str, chapter: str | None, book: LabelBook
) -> str:
    """Rewrite \\label{}, add \\tag{} carrying the book's number."""

    def fix_block(m: re.Match) -> str:
        body = m.group(1)
        if "\\label{" not in body:
            return m.group(0)

        rows = ROW_SPLIT_RE.split(body)
        seps = ROW_SPLIT_RE.findall(body)
        primary: str | None = None
        emitted = False
        out_rows: list[str] = []

        for row in rows:
            if not LABEL_RE.search(row):
                out_rows.append(row)
                continue
            row_tag = TAG_RE.search(row)

            def repl_label(lm: re.Match) -> str:
                nonlocal primary, emitted
                label = lm.group(1).strip()
                tag_text = clean_tag(row_tag.group(1)) if row_tag else None
                anchor, number, keep = book.assign(label, chapter, tag_text)
                if primary is None:
                    primary = anchor
                # MyST holds one identifier per math node, so only the first
                # label in the block becomes one; the rest keep their printed
                # number and are aliased onto the block's anchor so references
                # to them still land on the right equation.
                if keep and emitted:
                    book.alias(label, anchor, primary)
                    keep = False
                if keep:
                    emitted = True
                tag = ""
                if number and not row_tag:
                    tag = rf"\tag{{{number}}} "
                return f"{tag}\\label{{{anchor}}}" if keep else tag.rstrip()

            out_rows.append(LABEL_RE.sub(repl_label, row))

        rebuilt = out_rows[0]
        for sep, row in zip(seps, out_rows[1:]):
            rebuilt += sep + row
        return f"$$\n{rebuilt}\n$$"

    return MATH_BLOCK_RE.sub(fix_block, text)


# --------------------------------------------------------------------------
# references
# --------------------------------------------------------------------------


def rewrite_equation_refs(
    text: str, book: LabelBook, adhoc: dict[str, list[str]]
) -> tuple[str, list[str]]:
    """\\ref{5.6} -> [5.6](#eq-5-6), matching how LibreTexts renders it."""
    unresolved: list[str] = []
    # Where each ad-hoc anchor was defined, so "\ref{a}" inside one worked
    # example resolves to that example's (a), not another chapter's.
    positions = [
        (m.start(), m.group(1))
        for m in LABEL_RE.finditer(text)
        if m.group(1) in adhoc
    ]

    def nearest_adhoc(label: str, at: int) -> str | None:
        best = None
        for pos, anchor in positions:
            if pos > at:
                break
            if label in adhoc[anchor]:
                best = anchor
        if best is None:
            best = next(
                (a for _, a in positions if label in adhoc[a]), None
            )
        return best

    def repl(m: re.Match) -> str:
        label = m.group(1).strip()
        entry = book.lookup_number(label)
        if entry is not None:
            anchor, number = entry
            return f"[{ref_text(number or label)}](#{anchor})"
        anchor = nearest_adhoc(label, m.start())
        if anchor is not None:
            return f"[{ref_text(label)}](#{anchor})"
        unresolved.append(label)
        # LibreTexts references a few equations it never labelled. Print the
        # tag the way the book does rather than leaving raw LaTeX on the page.
        return f"({ref_text(display_number(label) or label)})"

    # References the source wrapped in inline math ("equation $\ref{alpha}$")
    # are prose references too — KaTeX has no \ref.
    text = re.sub(r"\$\s*(\\(?:eq)?ref\{[^}]*\})\s*\$", r"\1", text)
    text = sub_outside_math(REF_RE, repl, text)
    # A \ref left inside a formula cannot become a link, but it must not stay
    # a raw control sequence either: print the tag, as MathJax would.
    text = REF_RE.sub(lambda m: rf"\text{{({m.group(1).strip()})}}", text)
    return text, unresolved


MATH_SPAN_RE = re.compile(r"\$\$.*?\$\$|(?<!\\)\$(?:\\.|[^$\\])*\$", re.S)


def sub_outside_math(pattern: re.Pattern, repl, text: str) -> str:
    out: list[str] = []
    pos = 0
    for m in MATH_SPAN_RE.finditer(text):
        out.append(pattern.sub(repl, text[pos : m.start()]))
        out.append(m.group(0))
        pos = m.end()
    out.append(pattern.sub(repl, text[pos:]))
    return "".join(out)


FIGURE_MENTION_RE = re.compile(
    r"\bFigure\s+"
    r"(?:\$\(?(\d+(?:\.\w+)+)\)?\$|\(?(\d+(?:\.\w+)+)\)?)"
)


def rewrite_figure_refs(text: str, labels: set[str]) -> tuple[str, list[str]]:
    """"Figure 5.2.1" -> a link to the figure of that number."""
    unresolved: list[str] = []

    def repl(m: re.Match) -> str:
        # Already linked.
        if m.start() > 0 and text[m.start() - 1] == "[":
            return m.group(0)
        num = (m.group(1) or m.group(2)).rstrip(".")
        label = "fig-" + num.replace(".", "-")
        if label not in labels:
            # "Figure 13.20.2a" names panel (a) of figure 13.20.2.
            panel = re.match(r"^(\d+(?:\.[0-9A-Za-z]+)*\.\d+)[a-z]$", num)
            label = "fig-" + panel.group(1).replace(".", "-") if panel else label
            if label not in labels:
                unresolved.append(num)
                return m.group(0)
        return f"[Figure {num}](#{label})"

    return sub_outside_math(FIGURE_MENTION_RE, repl, text), unresolved


# --------------------------------------------------------------------------
# driver
# --------------------------------------------------------------------------


def content_files() -> list[Path]:
    """Chapter order matters: the first definition of an equation number is
    the one that keeps the label, and chapters restate earlier ones."""
    return [p for d in CONTENT_DIRS if d.is_dir() for p in sorted(d.glob("*.md"))]


def main() -> int:
    paths = content_files()
    book = LabelBook()
    texts: dict[Path, str] = {}
    adhoc: dict[Path, dict[str, list[str]]] = {}
    fig_labels: set[str] = set()

    for path in paths:
        text = fix_hard_errors(path, path.read_text(encoding="utf-8"))
        if path.name == "ch-14-coupled-linear-oscillators.md":
            text = rename_ch14_labels(text)
        book.start_file()
        text = fix_tag_math(text)
        text = relabel_equations(text, chapter_num(path), book)
        adhoc[path] = book.adhoc
        fig_labels.update(re.findall(r"^:label: (fig-[\w-]+)$", text, re.M))
        texts[path] = text

    changed, dangling_eq, dangling_fig = [], [], []
    for path, text in texts.items():
        text, missing = rewrite_equation_refs(text, book, adhoc[path])
        dangling_eq += [(path.name, label) for label in missing]
        text, missing_fig = rewrite_figure_refs(text, fig_labels)
        dangling_fig += [(path.name, num) for num in missing_fig]
        if text != path.read_text(encoding="utf-8"):
            path.write_text(text, encoding="utf-8")
            changed.append(path.relative_to(ROOT))

    restated = sum(book.restated.values())
    print(
        f"Resolved {len(book.numbers)} numbered equations, "
        f"{sum(len(v) for v in adhoc.values())} local ids, "
        f"{len(fig_labels)} figures."
    )
    print(f"  {restated} restated equation(s) point at their first definition.")
    print(f"Updated {len(changed)} files.")
    if dangling_eq:
        print(f"  ! {len(dangling_eq)} equation reference(s) with no target:")
        for name, label in dangling_eq:
            print(f"      {name}: \\ref{{{label}}}")
    if dangling_fig:
        print(f"  ! {len(dangling_fig)} figure mention(s) with no target:")
        for name, num in sorted(set(dangling_fig)):
            print(f"      {name}: Figure {num}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
