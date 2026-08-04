# repro-EM

Companion website for the Microscopy & Microanalysis 2026 talk
**Open Formats, Standard Metadata, and Benchmarks: A Reproducibility Framework
for Materials Electron Microscopy** (Colin Ophus, Stanford University).

## Building the site

The site is built with [MyST Markdown](https://mystmd.org/):

```bash
npm install -g mystmd   # or: pip install mystmd
myst start              # local dev server with live reload
myst build --html       # static site in _build/html
```

The book-theme is patched after the template downloads, to keep the top-level
TOC sections expanded and to replace the modal search with a flat input in the
top bar:

```bash
python3 scripts/patch_theme.py
```

Re-run it whenever `_build/` is cleared. The deploy workflow does this
automatically between a warm-up build and the real build.

## Deployment

Pushes to `main` trigger the GitHub Actions workflow in
`.github/workflows/deploy.yml`, which builds the site and publishes it to
GitHub Pages. One-time setup on GitHub: repository **Settings → Pages →
Source → GitHub Actions**.

## Layout

- `index.md`: landing page
- `assets/`: images and logos
- `style.css`: theme overrides for the MyST book-theme
- `scripts/patch_theme.py`: post-download theme patches (search, TOC)
