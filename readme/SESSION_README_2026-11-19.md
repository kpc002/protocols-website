# Session README - 2026-11-19

This file records the Mice-protocol reorganization and deployment workflow from the November 19, 2026 session.

## Work completed

- Reorganized Mice protocols into the `Before`, `During`, and `After- The Takedown` stages, with related materials placed in `genotyping` and `phenotyping` where appropriate.
- Added landing pages for `Before`, `During`, and `After- The Takedown`.
- Updated the Mice landing page so it shows experiment stages in one section and the remaining top-level folders in another.
- Moved the Masopust Gut Prep Protocol beneath `After- The Takedown` and removed it from the Mice landing-page listing.
- Updated affected Markdown, Quarto, and configuration links after each move.

## Validation

The complete site render succeeded:

```bash
quarto render /home/kpcheung/Desktop/Kitty/protocols-website
```

Quarto rendered 462 pages with no build errors. It reported five non-fatal unresolved cross-reference warnings in `protocols/bioinformatics/introduction-to-deseq2/index.qmd` for `@tbl-counts`, `@fig-pca`, `@fig-distance`, `@fig-ma_plot`, and `@fig-ma_plot_lfc`.

## Push to GitHub and deploy

This repository deploys automatically when changes are pushed to `main`. The GitHub Actions **Quarto Publish** workflow renders the site and publishes `_site` to the `cf-pages` branch. Do not push directly to `cf-pages`.

Review the pending changes, commit them, and push to GitHub:

```bash
cd /home/kpcheung/Desktop/Kitty/protocols-website
git status
git diff --cached --stat
git commit -m "Reorganize Mice protocols"
git push origin main
```

If intended changes are not staged yet, stage selected files first:

```bash
git add _quarto.yml index.qmd protocols/mice
```

Use `git add -A` only after confirming every current working-tree change belongs in the same commit.

After pushing, open the repository's **Actions** tab and wait for the **Quarto Publish** workflow to complete successfully. The public site is available at <https://kpc002.github.io/protocols-website/>.

## Link-maintenance command

After moving or renaming a file or folder, search for references and update any results:

```bash
rg -n --glob '*.md' --glob '*.qmd' --glob '*.yml' --glob '*.yaml' \
  'old_filename|old_folder|old/path' .
```

## Before landing-page listings

The `Protocols` table on `protocols/mice/Before/index.qmd` automatically lists Markdown and Quarto pages placed directly in the `Before` folder. Use root-anchored globs so files in child folders, such as `Tumor`, are not included in this table:

```yaml
- id: protocols
  type: table
  contents: ["/*.md", "/*.qmd"]
  sort: title
  fields: [title, description, author]
```

Quarto globs are recursive by default. The leading `/` limits these patterns to the same folder as the landing page. The separate `Tumor` listing continues to use `contents: ["Tumor/*.md"]` inside a collapsible `<details>` section.
