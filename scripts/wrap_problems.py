#!/usr/bin/env python3
"""Wrap end-of-chapter problems in MyST ``{exercise}`` directives.

Georgi's problems are numbered ``N.M`` (sometimes starred). MyST's standard
admonition for that is ``{exercise}``, with ``:enumerator:`` keeping the book
number so cross-references can use ``[](#prb-N-M)``.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "chapters"

# ``**2.1.**``, ``**3.4*.**``, ``**12.1***``, ``1.1.``, ``1.2a.``, ``**11.10**``
PROBLEM_RE = re.compile(
    r"^(?:"
    r"\*\*(\d+)\.(\d+)(\*)?\.?\*\*"
    r"|(\d+)\.(\d+)(?!\.\d)(\*)?([a-z])?\.?"
    r")"
    r"(?:\s+\*\*([^*]+?)\*\*)?"
    r"\s*(.*)$"
)

PROBLEMS_HEAD_RE = re.compile(
    r"^(?:#{2,3}\s+(?:\d+\.\d+:\s+)?Problems?|Problems)\s*$",
    re.M,
)
H2_RE = re.compile(r"^## ", re.M)

# "problem (2.4)", "problem (1.2e)", "problem 7.5", "problem (1.1.1)"
PROSE_PAREN_RE = re.compile(
    r"(?<!\[)\b([Pp]roblems?)\s*\((\d+)\.(\d+)(?:\.(\d+))?([a-z])?\)"
)
PROSE_BARE_RE = re.compile(
    r"(?<!\[)\b([Pp]roblem)\s+(\d+)\.(\d+)\b(?!\.\d)"
)


def problem_label(chapter: str, number: str) -> str:
    return f"prb-{chapter}-{number}"


def fence_for(body: str) -> str:
    n = 3
    for m in re.finditer(r"^(:+)", body, re.M):
        n = max(n, len(m.group(1)))
    return ":" * (n + 1)


def wrap_exercise(
    *,
    enumerator: str,
    label: str,
    title: str,
    body: str,
    starred: bool,
) -> str:
    body = body.strip()
    fence = fence_for(body)
    title_arg = f" {title.strip()}" if title.strip() else ""
    lines = [f"{fence}{{exercise}}{title_arg}", f":label: {label}"]
    lines.append(f":enumerator: {enumerator}")
    if starred and "*" not in enumerator:
        # Keep the book's optional-problem mark visible in the enumerator.
        lines[-1] = f":enumerator: {enumerator}*"
    lines.append("")
    if body:
        lines.append(body)
        lines.append("")
    lines.append(fence)
    return "\n".join(lines)


def parse_problem_line(line: str) -> dict | None:
    m = PROBLEM_RE.match(line)
    if not m:
        return None
    if m.group(1) is not None:
        chapter, number, star = m.group(1), m.group(2), bool(m.group(3))
        letter = ""
    else:
        chapter, number = m.group(4), m.group(5)
        star = bool(m.group(6))
        letter = m.group(7) or ""
    title = (m.group(8) or "").strip(" —-")
    rest = (m.group(9) or "").strip()
    if letter:
        rest = f"{letter}. {rest}".strip() if rest else f"{letter}."
    return {
        "chapter": chapter,
        "number": number,
        "starred": star,
        "title": title,
        "rest": rest,
    }


def split_problems(block: str) -> list[dict]:
    lines = block.splitlines()
    items: list[dict] = []
    current: dict | None = None
    buf: list[str] = []

    def flush() -> None:
        nonlocal current, buf
        if current is None:
            return
        body = "\n".join(buf).strip()
        if current["rest"]:
            body = (current["rest"] + ("\n\n" + body if body else "")).strip()
        items.append({**current, "body": body})
        current = None
        buf = []

    for line in lines:
        parsed = parse_problem_line(line)
        if parsed:
            flush()
            current = parsed
            buf = []
            continue
        if current is None:
            # Preamble under the Problems heading (should be empty).
            continue
        buf.append(line)
    flush()
    return items


def problems_span(text: str) -> tuple[int, int, str] | None:
    """Return (head_end, body_end, heading_block) for the problems region."""
    matches = list(PROBLEMS_HEAD_RE.finditer(text))
    if not matches:
        return None

    first = matches[0]
    # Chapter 1 has both "1.10: Problem" and a duplicate "1.11: Problems".
    second = None
    for m in matches[1:]:
        if re.match(r"^## \d+\.\d+: Problems?\s*$", m.group(0)):
            second = m
            break

    after_first = first.end()
    # Body ends at the next H2 that is not a Problems heading, or EOF.
    h2_after = [
        m
        for m in H2_RE.finditer(text, after_first)
        if not re.match(
            r"^## \d+\.\d+: Problems?\s*$",
            text[m.start() : text.find("\n", m.start())],
        )
    ]
    body_end = h2_after[0].start() if h2_after else len(text)

    if second and second.start() < body_end:
        heading = text[first.start() : first.end()] + "\n\n" + second.group(0)
        return first.start(), body_end, heading
    heading = first.group(0)
    if heading.strip() == "Problems":
        heading = "### Problems"
    return first.start(), body_end, heading


def wrap_chapter(text: str) -> tuple[str, int]:
    span = problems_span(text)
    if span is None:
        return text, 0
    start, end, heading = span
    region = text[start:end]
    if "{exercise}" in region:
        return text, 0

    # Body is everything after the last Problems heading in this span.
    last_head = list(PROBLEMS_HEAD_RE.finditer(region))[-1]
    body = region[last_head.end() :]
    items = split_problems(body)
    if not items:
        return text, 0

    blocks = [heading.strip(), ""]
    for item in items:
        enum = f"{item['chapter']}.{item['number']}"
        blocks.append(
            wrap_exercise(
                enumerator=enum,
                label=problem_label(item["chapter"], item["number"]),
                title=item["title"],
                body=item["body"],
                starred=item["starred"],
            )
        )
        blocks.append("")
    new_region = "\n".join(blocks).rstrip() + "\n"
    if end < len(text) and not text[end].startswith("\n"):
        new_region += "\n"
    return text[:start] + new_region + text[end:], len(items)


def known_labels(chapters: list[Path]) -> set[str]:
    labels: set[str] = set()
    for path in chapters:
        labels.update(
            re.findall(r"^:label: (prb-\S+)$", path.read_text(encoding="utf-8"), re.M)
        )
    return labels


def link_prose(text: str, labels: set[str]) -> tuple[str, int]:
    n = 0

    def repl_paren(m: re.Match) -> str:
        nonlocal n
        word, ch, num, extra, letter = m.groups()
        # LibreTexts ``\PageIndex{1}`` in "problem (\PageIndex{1})" became 1.1.1.
        if extra and extra != "1":
            return m.group(0)
        label = problem_label(ch, num)
        if label not in labels:
            return m.group(0)
        shown = f"{ch}.{num}{letter or ''}"
        n += 1
        return f"[{word} {shown}](#{label})"

    def repl_bare(m: re.Match) -> str:
        nonlocal n
        word, ch, num = m.groups()
        label = problem_label(ch, num)
        if label not in labels:
            return m.group(0)
        n += 1
        return f"[{word} {ch}.{num}](#{label})"

    text = PROSE_PAREN_RE.sub(repl_paren, text)
    text = PROSE_BARE_RE.sub(repl_bare, text)
    return text, n


def main() -> int:
    paths = sorted(CHAPTERS.glob("ch-*.md"))
    total = 0
    for path in paths:
        text = path.read_text(encoding="utf-8")
        new, count = wrap_chapter(text)
        if new != text:
            path.write_text(new, encoding="utf-8")
        print(f"{path.name}: {count} exercises")
        total += count

    labels = known_labels(paths)
    linked = 0
    for path in paths:
        text = path.read_text(encoding="utf-8")
        new, n = link_prose(text, labels)
        if new != text:
            path.write_text(new, encoding="utf-8")
        linked += n
    print(f"wrapped {total} problems, linked {linked} prose refs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
