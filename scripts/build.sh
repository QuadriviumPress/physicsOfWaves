#!/bin/sh
# Regenerate the MyST edition from the LibreTexts HTML cache (and crawl if needed).
set -e
cd "$(dirname "$0")/.."
if [ ! -f outline.json ] || [ "${FORCE_CRAWL:-}" = "1" ]; then
  python3 scripts/crawl_libretexts.py
fi
python3 scripts/build_book.py
python3 scripts/fix_crossrefs.py
# resolve_references.py targets LibreTexts \\ref{N.M} labels; this book uses
# hard-coded numbers fixed by fix_crossrefs.py instead.
