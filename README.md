# The Physics of Waves (MyST edition)

Web-native [MyST Markdown](https://mystmd.org/) edition of Howard Georgi's
*The Physics of Waves* (Harvard University).

## Status

Full book converted from the structured
[LibreTexts edition](https://phys.libretexts.org/Bookshelves/Waves_and_Acoustics/The_Physics_of_Waves_(Goergi))
(shelf path spells the author `Goergi`), with figures downloaded from LibreTexts.

- **Live site**: [quadriviumpress.com/physicsOfWaves](https://quadriviumpress.com/physicsOfWaves/)
- **CI/CD**: `.github/workflows/ci.yml` on pull requests;
  `.github/workflows/deploy.yml` publishes to GitHub Pages on pushes to `main`.

## Source and license

© Howard Georgi. Originally published by Prentice Hall (1993); rights returned
to the author for the online edition.
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

LibreTexts: [The Physics of Waves (Goergi)](https://phys.libretexts.org/Bookshelves/Waves_and_Acoustics/The_Physics_of_Waves_(Goergi))

## Build

```bash
npm install
npm run start          # preview
npm run build          # static site in _build/html/
```

## Convert from LibreTexts

```bash
npm run crawl          # fetch HTML → work/html + outline.json
npm run convert        # HTML → Markdown + images
npm run verify
```

Requires Python 3 with `beautifulsoup4`, and Node ≥ 20.

## Layout

| Path | Role |
| --- | --- |
| `outline.json` | LibreTexts page tree |
| `myst.yml` | Project metadata and TOC |
| `scripts/` | Crawl + HTML→MyST pipeline |
| `work/html/` | Cached LibreTexts pages (git-ignored) |
| `chapters/` | Fourteen chapter Markdown files |
| `front/` / `back/` | Front and back matter from LibreTexts |
| `images/` | Figures from LibreTexts |

Chapter files concatenate LibreTexts sections; display math is kept as `$$…$$`
from the LibreTexts LaTeX source.
