# Coachly — Brand source of truth

Canonical reference: [`assets/brand/visual-identity-v2.jpg`](assets/brand/visual-identity-v2.jpg)
("COACHLY — VISUAL IDENTITY V2 — The Operating System for Modern Coaches").

All design tokens in `assets/css/styles.css` are derived from that sheet. When the
brandbook changes, update this file and the `:root` token blocks together.

## Color

| Token | Value | Brandbook name |
|-------|-------|----------------|
| `--accent-500` | `#E1102E` | Coachly Red (accent, ~5% coverage) |
| `--accent-600` | `#C20E28` | Red, darkened for light-mode text/contrast |
| `--accent-700` | `#9C0B20` | Red, pressed |
| `--text-primary` (light) | `#080808` | Obsidian |
| `--bg` (light) | `#F7F7F5` | Cloud |
| `--surface-hover` (dark) | `#242629` | Graphite |
| `--surface-2` (light) | `#F1F2F3` | Grey 100 |
| placeholder A/B | `#D7D9DC` / `#B4B8BE` | Grey 300 / Grey 500 |
| `--text-secondary` (light) | `#454A52` | Grey 700 |
| `--text-tertiary` (light) | `#8B9098` | Grey 500 |

Dark theme uses Obsidian `#080808` as the base and Cloud `#F7F7F5` as primary text.
Red keeps white (`--text-on-accent: #FFFFFF`) on top in both themes.

## Typography

- English: **Geist** (`--font-en`), loaded from Google Fonts in `build.py`.
- Persian: **Vazirmatn** (`--font-fa`) stands in for the brandbook's Persian display
  face until the licensed family is supplied; Geist is the Latin fallback inside `fa`.

## Logo mark

Circular emblem: a bold "C" with a thin swoosh arc orbiting its left side,
both in a red→obsidian gradient (`#F0142E` → `#C20E28` → `#4E0813` → `#0F0F0F`,
lit from top). Built as two stroked circular arcs on a 48×48 grid
(C = r14 / stroke 7.6; swoosh = r20 / stroke 2.3).

- Standalone vector: [`assets/brand/coachly-mark.svg`](assets/brand/coachly-mark.svg)
- Full lockup reference (mark + "COACHLY" wordmark): [`assets/brand/logo-lockup.jpg`](assets/brand/logo-lockup.jpg)
- In the site it's inlined as `BRAND_MARK` in `build.py` (nav + footer `.brand`),
  30×30, styled by `.brand-mark svg` in `styles.css`.

`coachly-mark.svg` is a hand-built vector approximation of the supplied JPG —
replace with the designer's original vector when available.

## Favicon

Inline SVG data-URI in `build.py` head (and the two hand-authored `index.html`):
obsidian `#141414` rounded square with the red gradient mark.
