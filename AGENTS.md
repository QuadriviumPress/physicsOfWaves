# AGENTS.md

## Standard

This book follows the [QuadriviumPress MyST baseline](https://github.com/QuadriviumPress/bindery/blob/main/doc/myst-baseline.md) and the [presentation skill](https://github.com/QuadriviumPress/bindery/blob/main/skills/quadrivium-myst-presentation/SKILL.md).

## Commands

```bash
npm run start
npm run build
npm run verify
npm run check
npm run convert
npm run crawl
```

`npm run check` is the production-equivalent verification and HTML build.

## Intentional differences

- `verify` runs `python3 scripts/verify_book.py`.
- `convert` (`sh scripts/build.sh`) and `crawl` (`python3 scripts/crawl_libretexts.py`) are source-conversion tools. They are not part of `check`.

## Presentation gap

Problems are `{exercise}` directives with a manual `:enumerator:`. Chapter numbers are typed into headings, and the sampled chapters do not hide answers in `{solution}` dropdowns. Source numbering is kept until a later presentation pass.
