"""Structural checks for the converted MyST book."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIRS = ("chapters", "front", "back")

# Source constructs MyST does not understand. Any of these reaching the
# Markdown means a reader sees raw LaTeX on the page.
LEFTOVERS = {
    r"\\PageIndex": "unexpanded \\PageIndex counter",
    r"\\(?:eq)?ref\{": "unresolved \\ref — should be a MyST link",
    r"\$\\PageIndex": "unexpanded \\PageIndex counter",
}


def content_files() -> list[Path]:
    return [p for d in CONTENT_DIRS for p in sorted((ROOT / d).glob("*.md"))]


def check_leftovers(errors: list[str]) -> None:
    for path in content_files():
        text = path.read_text(encoding="utf-8")
        for pattern, why in LEFTOVERS.items():
            n = len(re.findall(pattern, text))
            if n:
                errors.append(f"{path.name}: {n} × {why}")


def check_references(errors: list[str]) -> None:
    """Every internal link must have a target somewhere in the book."""
    targets: set[str] = set()
    links: list[tuple[str, str]] = []
    for path in content_files():
        text = path.read_text(encoding="utf-8")
        targets.update(re.findall(r"\\label\{([^}]+)\}", text))
        targets.update(re.findall(r"^:label: (\S+)$", text, re.M))
        targets.update(re.findall(r"^\((\S+)\)=$", text, re.M))
        links += [
            (path.name, m)
            for m in re.findall(r"\]\(#([^)]+)\)", text)
        ]
    for name, target in links:
        if target not in targets:
            errors.append(f"{name}: link to #{target} has no target")


def check_duplicate_labels(errors: list[str]) -> None:
    seen: dict[str, str] = {}
    for path in content_files():
        text = path.read_text(encoding="utf-8")
        found = re.findall(r"\\label\{([^}]+)\}", text) + re.findall(
            r"^:label: (\S+)$", text, re.M
        )
        for label in found:
            if label in seen:
                errors.append(
                    f"{path.name}: label {label} already defined in {seen[label]}"
                )
            seen[label] = path.name


def check_footnotes(errors: list[str]) -> None:
    """MyST drops a footnote definition nothing references."""
    for path in content_files():
        text = path.read_text(encoding="utf-8")
        defs = re.findall(r"^\[\^([\w.-]+)\]:", text, re.M)
        refs = re.findall(r"\[\^([\w.-]+)\]", text)
        for note in defs:
            if refs.count(note) <= 1:
                errors.append(f"{path.name}: footnote [^{note}] has no marker")


def check_structure(errors: list[str]) -> None:
    outline = json.loads((ROOT / "outline.json").read_text(encoding="utf-8"))

    for ch in outline["chapters"]:
        path = ROOT / "chapters" / f"{ch['slug']}.md"
        if not path.exists():
            errors.append(f"missing chapter file: {path.name}")
            continue
        text = path.read_text(encoding="utf-8")
        if len(text) < 200:
            errors.append(f"chapter too short: {path.name}")
        for sec in ch["sections"]:
            if f"## {sec['title']}" not in text:
                errors.append(f"{path.name}: missing section {sec['title']!r}")

    myst = ROOT / "myst.yml"
    if not myst.exists():
        errors.append("missing myst.yml")
    else:
        yml = myst.read_text(encoding="utf-8")
        for ch in outline["chapters"]:
            if ch["slug"] not in yml:
                errors.append(f"myst.yml missing toc entry for {ch['slug']}")
        if "equation: false" not in yml:
            errors.append(
                "myst.yml must disable equation auto-numbering; the book "
                "carries its own numbers as \\tag{}"
            )


def check_images(errors: list[str]) -> None:
    for path in content_files():
        text = path.read_text(encoding="utf-8")
        for rel in re.findall(r":::\{figure\}\s+\.\./images/(\S+)", text):
            if not (ROOT / "images" / rel).exists():
                errors.append(f"{path.name}: missing image {rel}")


def main() -> int:
    errors: list[str] = []
    check_structure(errors)
    check_leftovers(errors)
    check_references(errors)
    check_duplicate_labels(errors)
    check_footnotes(errors)
    check_images(errors)

    if errors:
        print("VERIFY FAILED")
        for e in errors[:50]:
            print(" -", e)
        if len(errors) > 50:
            print(f" ... and {len(errors) - 50} more")
        return 1

    n_ch = len(json.loads((ROOT / "outline.json").read_text())["chapters"])
    n_img = len(list((ROOT / "images").glob("*")))
    n_eq = sum(
        len(re.findall(r"\\label\{", p.read_text(encoding="utf-8")))
        for p in content_files()
    )
    n_fig = sum(
        len(re.findall(r"^:label: fig-", p.read_text(encoding="utf-8"), re.M))
        for p in content_files()
    )
    print(
        f"OK: {n_ch} chapters, {n_eq} labelled equations, {n_fig} numbered "
        f"figures, {n_img} images, myst.yml present"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
