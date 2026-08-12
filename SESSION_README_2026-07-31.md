# Session README - 2026-07-31

This file records the main repository changes and checks from the July 31, 2026 protocol-website cleanup session.

## Current Site Structure Updates

- Added homepage links for the new top-level protocol collections:
  - `protocols/histology/`
  - `protocols/Histology/`
  - `protocols/Crispr Cas9 Electroporation/`
  - `protocols/Transfection/`
  - `protocols/Transduction/`
  - `protocols/Pertub_Seq/`
- Added missing landing pages so homepage links open Quarto pages instead of raw directory listings:
  - `protocols/Crispr Cas9 Electroporation/index.qmd`
  - `protocols/Crispr Cas9 Electroporation/MaxCyte/index.qmd`
  - `protocols/Transfection/index.qmd`
  - `protocols/Transduction/index.qmd`
  - `protocols/Transduction/Retronectin/index.qmd`
  - `protocols/Pertub_Seq/index.qmd`
  - `protocols/Histology/index.qmd`
- Updated `protocols/Transduction/Retronectin/fluorescent protein imaging.md` with a YAML description so it can appear cleanly in listing tables.

## Recent Organization Work

- Created or populated protocol collections for:
  - CRISPR-Cas9 Electroporation: `Lonza`, `Neon`, and `MaxCyte`.
  - Transfection: `Plat_E` and `HEK293T and Lentivirus`.
  - Transduction: `Polybrene` and `Retronectin`.
  - Perturb-seq resources in `protocols/Pertub_Seq/`.
  - Histology resources in both `protocols/histology/` and `protocols/Histology/`.
- Moved associated source files with their Markdown pages where practical, including PDFs, DOCX files, PNG page images, SVG icons, and extracted artifact folders.
- Converted multiple PDF-backed protocol pages to PNG page images and simplified the Markdown pages to keep YAML metadata, a title, a download button, and embedded images.
- Standardized many local file links as download-style buttons.

## Script Update

Updated `scripts/check_quarto_collisions.py`.

The script now checks:

- duplicate Quarto renderable source stems, such as both `file.md` and `file.qmd`;
- same-stem `.html` files left in the source tree;
- stale local Markdown links in `index.md` and `index.qmd` files by default;
- all local Markdown links when run with `--check-links all`.

Default pre-render command:

```bash
python3 scripts/check_quarto_collisions.py
```

Full local-link audit:

```bash
python3 scripts/check_quarto_collisions.py --check-links all
```

The default check currently passes.

## Stale Links Fixed

The updated script found and these were fixed:

- Removed the stale `ScienceDirect_files_26Nov2019_21-45-47.888/index.qmd` folder link from `protocols/Goldrath_Protocols/The Master Folder/MRC/RetroProduction_Tcells/index.qmd`.
- Updated the old `Mirus.qmd` link in `protocols/infections/retrovirus/index.md` to point to `protocols/Transfection/Plat_E/Mirus.qmd`.
- Updated stale `Top_20` source links after protocol moves:
  - Lonza electroporation source links now point to `protocols/Crispr Cas9 Electroporation/Lonza/`.
  - Polybrene source links now point to `protocols/Transduction/Polybrene/`.
  - Retronectin source links now point to `protocols/Transduction/Retronectin/`.
  - Plat-E transfection source links now point to `protocols/Transfection/Plat_E/`.

## Remaining Known Full-Audit Issues

The stronger all-file audit still reports missing media assets in older converted/imported pages. These are not blocking the default pre-render check, but should be fixed if those pages need their images restored.

Known missing local media references:

- `protocols/Cloning/Protocol for CRISPR amplicon sequencing 2025-11-06 (etr_PxVJqvYTzT) Custom_low_plex_LsgA_cloning_MRC.md`
  - `media/image1.png`
  - `media/image2.png`
- `protocols/Giovanni_s_Protocols/human/CB18.Red blood cell lysis with ACK buffer.md`
  - `media/image1.emf`
- `protocols/Giovanni_s_Protocols/molecular/MB2.Mycoplasma_PCR.md`
  - `media/image1.jpeg`
- `protocols/Goldrath_Protocols/Old_Protocols/Hemacytometer.md`
  - `media/image1.jpeg`
- `protocols/Goldrath_Protocols/Old_Protocols/Listeria production.md`
  - `media/image1.png`
  - `media/image2.png`
- `protocols/Goldrath_Protocols/The Master Folder/MRC/Caecum_orthotopic_protocol_MRC.md`
  - `media/image1.jpeg`
- `protocols/Goldrath_Protocols/The Master Folder/MRC/MYCO_PCR.md`
  - `media/image1.jpeg`
- `protocols/Goldrath_Protocols/The Master Folder/MRC/guide design and sequence.md`
  - `media/image1.tiff`
  - `media/image2.emf`
  - `media/image3.emf`
- `protocols/Goldrath_Protocols/VSV-ova related material/VSV-ova titer 092707  (main 2007 VSV-ova lot).md`
  - `media/image1.wmf`
- `protocols/Transduction/Retronectin/CB2.Calcium flux assay.md`
  - `media/image1.png`
  - `media/image2.png`
  - `media/image3.png`
  - `media/image4.png`

## Useful Commands

Clean Quarto render with an external cache:

```bash
XDG_CACHE_HOME=/tmp/protocols-quarto-cache quarto render
```

Render one page:

```bash
XDG_CACHE_HOME=/tmp/protocols-quarto-cache quarto render path/to/file.md
```

Check repository status before committing:

```bash
git status
git status --short
```

Stage all changes, including moved and untracked files:

```bash
git add -A
```

Create and push the working branch:

```bash
git switch -c kitty-version2
git commit -m "Reorganize protocol website"
git push -u origin kitty-version2
```

## GitHub Pages Note

The current workflow in `.github/workflows/publish.yml` builds pushes to `main` and deploys the rendered `_site` output to `cf-pages`.

For branch testing, temporarily changing the workflow trigger from `main` to `kitty-version2` will make `kitty-version2` build into `cf-pages`, but that means the live GitHub Pages branch is overwritten by the test branch. That is easy to toggle, but it is not a true separate preview environment.
