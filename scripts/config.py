"""Shared paths for The Physics of Waves MyST conversion."""

from __future__ import annotations

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTLINE = os.path.join(ROOT, "outline.json")
BUILD = os.path.join(ROOT, "build")
WORK = os.path.join(ROOT, "work")
HTML_CACHE = os.path.join(WORK, "html")
IMAGES = os.path.join(ROOT, "images")

# LibreTexts shelf path spells the author "Goergi" (not Georgi).
LIBRETEXTS_BASE = (
    "https://phys.libretexts.org/Bookshelves/Waves_and_Acoustics/"
    "The_Physics_of_Waves_(Goergi)"
)
SOURCE_HOME = LIBRETEXTS_BASE
USER_AGENT = "QuadriviumPress-myst-converter/0.1 (OER CC BY-NC-SA reuse)"
AUTHOR_NAME = "Howard Georgi"
