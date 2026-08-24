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

### Full R render remains environment-dependent

The bioinformatics tutorials use R and Bioconductor. The lockfile requires R 4.1.2 and Bioconductor 3.14. Full rendering can fail locally when the R library is incomplete or network access is unavailable.

Typical errors:

- `Bioconductor version cannot be validated; no internet connection`
- `there is no package called 'ggplot2'`
- `The project is out-of-sync`

`renv::restore()` only installs packages already recorded in `renv.lock`. When source code uses packages not recorded in the lockfile, install them deliberately and then snapshot. Do not run `snapshot()` merely to silence an unknown discrepancy.

```bash
RENV_CONFIG_SANDBOX_ENABLED=FALSE Rscript -e 'renv::status()'
RENV_CONFIG_SANDBOX_ENABLED=FALSE Rscript -e 'renv::restore(prompt = FALSE)'
RENV_CONFIG_SANDBOX_ENABLED=FALSE Rscript -e 'renv::snapshot(prompt = FALSE)'
```

`.renvignore` excludes generated Quarto output while retaining the bioinformatics source files for dependency discovery:

```text
_site/
_freeze/
.quarto/
site_libs/
protocols/**/index_files/
```

Non-blocking Quarto warnings still present in legacy bioinformatics content:

- Unresolved DESeq2 cross-references such as `@fig-pca` and `@tbl-counts`; fix the labels or remove the references.
- `quarto-ext/lightbox` is built into current Quarto; remove the legacy extension with `quarto remove extension quarto-ext/lightbox` when ready.

## Fix GitHub Actions before the next publish

GitHub Actions run `32753258355` failed during `renv::restore()`. The root error was RCurl:

```text
checking for curl-config... no
Cannot find curl-config
ERROR: configuration failed for package 'RCurl'
```

All listed Bioconductor failures were downstream of RCurl. Add this step after `Set up R` and before `Restore R packages` in `.github/workflows/publish.yml`:

```yaml
      - name: Install R system dependencies
        run: |
          sudo apt-get update
          sudo apt-get install --yes cmake libcurl4-openssl-dev libpng-dev pandoc
```

The workflow log also identified these required system packages: `cmake`, `libcurl4-openssl-dev`, `libpng-dev`, and `pandoc`.

## Publish successfully

1. Apply the GitHub Actions system-dependency fix above.
2. Review the complete change set. This repository has intentional large file moves and deletions, so do not stage blindly.

```bash
git status --short
git diff --check
git add -A
git diff --cached --name-status
git diff --cached --stat
```

3. Commit and push `main`:

```bash
git commit -m "Install R dependencies for publishing"
git push origin main
```

4. Open the GitHub Actions page and wait for `Quarto Publish` to complete. On success, the workflow writes `_site` to `cf-pages`, which Cloudflare Pages serves.
