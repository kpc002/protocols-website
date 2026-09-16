# Protocols Website Session Handoff

This file records the current state of the Quarto protocols website and how to continue publishing it.

## Working directory and Git state

```bash
cd /home/goldrath/Desktop/Kitty/protocols-website
```

- Branch: `main`
- Current pushed commit at the time of this handoff: `a2b6f98` (`Reorganize protocols and restore media assets`)
- Pushing to `main` runs `.github/workflows/publish.yml`, renders the site, and deploys `_site` to the `cf-pages` branch. Do not push directly to `cf-pages`.

## Organization and homepage

- The old source folders `Kelsey_s_Protocols` and `Kitty_s_Protocols` were removed after their content was reorganized.
- `index.qmd` was updated to remove deleted-folder links and add FACS, Human Samples, and Mitochondria.
- The current top-level protocol sections include `FACS`, `human`, `Mitochondria`, `mice`, `infections`, `mol_bio`, `t_cells`, CRISPR/cloning sections, and others.
- `protocols/index_files/` exists as a compatibility directory required by a Quarto listing.

## Media recovery completed

Missing images were recovered from their matching `.docx` files into adjacent `media/` or artifact folders. The static link audit now passes.

- Fixed moved CB7 ADP/ADT image paths to `CB7.ADP_ADT assay_artifacts/`.
- Recovered CRISPR amplicon, guide-design, Mycoplasma PCR, calcium-flux, ACK-buffer, VSV, Listeria, caecum orthotopic, and hemacytometer media.
- Converted the caecum orthotopic and hemacytometer JPEGs to PNG and updated their links.
- EMF/WMF assets were retained in their original formats because ImageMagick and LibreOffice could not convert them in this environment.

## Local verification

Run these checks before committing:

```bash
python3 scripts/check_quarto_collisions.py --check-links all
git diff --check
XDG_CACHE_HOME=/tmp/protocols-quarto-cache quarto render index.qmd
```

For a targeted protocol render, use an isolated Quarto cache to avoid the local Sass cache database error:

```bash
XDG_CACHE_HOME=/tmp/protocols-quarto-cache quarto render path/to/protocol.md
```

## Rendering issues and fixes

### Resolved source issues

- Missing `protocols/index_files`: created the compatibility directory.
- Stale links to deleted/moved folders: updated homepage, Top 20, Etv3, Tamoxifen, and related protocol links.
- Missing local media: recovered the assets from the source Word documents.
- Tamoxifen bibliography path: changed to `../references.bib`.
- Source-side HTML collision: remove any untracked generated HTML file with the same basename as a `.md` or `.qmd` source. A previous example was `protocols/Top_20/Spleen and Lymph Node Prep.html`.
- Quarto Sass cache error (`unable to open database file`): set `XDG_CACHE_HOME=/tmp/protocols-quarto-cache` for the render command.
- To skip executable code, use `quarto render --no-execute`; `--execute false` is parsed as a file named `false` and fails with `pandoc: false: withBinaryFile: does not exist`.
- `quarto preview protocols` can still block on the bioinformatics R pages. When the R environment is unavailable, preview the already-rendered site instead: `python3 -m http.server 4200 --bind 127.0.0.1 --directory _site`, then open `http://127.0.0.1:4200/protocols/`.

### R examples are static during website builds

The bioinformatics tutorials contain example R code, but the publishing job does not execute it. The examples in `nextflow_rna_seq/index.qmd` use ordinary highlighted `r` code fences, and the DESeq2 tutorial disables execution. This keeps website publishing independent of the legacy R 4.1.2/Bioconductor 3.14 environment recorded in `renv.lock`.

Use a separate compatible R environment when running those analyses interactively. Restoring or upgrading `renv.lock` is no longer part of the website deployment.

Non-blocking Quarto warnings still present in legacy bioinformatics content:

- Unresolved DESeq2 cross-references such as `@fig-pca` and `@tbl-counts`; fix the labels or remove the references.
- `quarto-ext/lightbox` is built into current Quarto; remove the legacy extension with `quarto remove extension quarto-ext/lightbox` when ready.

## GitHub Actions R setup failure and fix

GitHub Actions run `34385521545` failed before rendering because `setup-r` could no longer install R 4.1.2 on Ubuntu 22.04:

```text
Failed to install R: The process '/usr/bin/sudo' failed with exit code 100
```

The workflow no longer installs R or restores `renv`, because the website does not need to execute the tutorial examples. It now checks out the repository, installs Quarto, renders all 454 pages, and publishes `_site` to `cf-pages`.

## Publish successfully

1. Review the complete change set. This repository has intentional large file moves and deletions, so do not stage blindly.

```bash
git status --short
git diff --check
git add -A
git diff --cached --name-status
git diff --cached --stat
```

2. Commit and push `main`:

```bash
git commit -m "Fix Quarto deployment"
git push origin main
```

3. Open the GitHub Actions page and wait for `Quarto Publish` to complete. On success, the workflow writes `_site` to `cf-pages`, which Cloudflare Pages serves.
