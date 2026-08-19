# Protocols Website Session Handoff

This file summarizes the current state of the protocols website so a future Codex session can resume without reconstructing the recent work.

## Working directory

```text
/home/goldrath/Desktop/Kitty/protocols-website
```

From `/home/goldrath/Desktop/Kitty`, enter the project with:

```bash
cd protocols-website
```

## Git state

- Current branch: `main`
- Current commit: `f4db32f` (`Describe the reorganization`)
- At the time this handoff was created, `main`, `origin/main`, and `origin/kitty-version2` pointed to the same commit.
- The worktree contains substantial intentional file moves/deletions, metadata edits, and some generated Quarto output. Review `git status --short` before staging anything.

The publish workflow runs on pushes to `main` only. It renders the project and deploys `_site` to the `cf-pages` branch:

```text
.github/workflows/publish.yml
```

## Completed organization work

- Renamed `protocols/Crispr Design and Cloning` to `protocols/Crispr_Design_and_Cloning` and updated homepage references.
- Added/organized top-level sections including `General Cloning`, `Mitochondria`, `human`, `infections/listeria`, `mice`, `orga/mouse_transfer`, and `Transfection and Transduction/HEK293T and Lentivirus`.
- Moved mitochondria-related protocols into `protocols/Mitochondria`, including calcium flux, Seahorse, mitochondria dye, ADP/ADT, Bodipy/mitotracker, and general Seahorse files.
- Converted `Lentivirus_Production_and_Transduction.docx` to Markdown before moving it with its source document.
- Deleted the now-empty source folders `Alex_s_Protocols`, `Dhruv_s_Protocols`, and `Angelica_s protocols` after their relevant files were moved.
- Updated non-index Anthony protocol front matter authors to `Anthony Phan`.
- Removed homepage links for deleted source folders and added direct links for current top-level sections.

## Current landing pages

- Root homepage: `index.qmd`
- CRISPR landing page: `protocols/Crispr_Design_and_Cloning/index.qmd`
- Mitochondria landing page: `protocols/Mitochondria/index.qmd`

The Mitochondria page uses a Quarto table listing with `filename`, `author`, and `description` fields and links each filename to its protocol.

## Known render issue

The latest targeted render of `protocols/Mitochondria` reached a Quarto-generated listing error because this directory is missing:

```text
protocols/index_files
```

Create the compatibility directory, then retry the targeted render:

```bash
mkdir -p protocols/index_files
XDG_CACHE_HOME=/tmp/protocols-quarto-cache quarto render protocols/Mitochondria
```

After that succeeds, run a full project render:

```bash
XDG_CACHE_HOME=/tmp/protocols-quarto-cache quarto render .
```

Record any remaining warnings or errors. Previous full renders also reported unresolved cross-references in `protocols/bioinformatics/introduction-to-deseq2/index.qmd` and missing `lightbox` shortcode warnings in the SCENIC content; verify whether those remain.

## Generated files to review

The worktree currently includes generated or possibly generated files such as:

- `site_libs/`
- `protocols/index-listing.json`
- `protocols/Mitochondria/index-listing.json`
- `protocols/infections/index-listing.json`
- `protocols/infections/index.html`

Do not stage or delete these automatically. First check whether the repository intentionally tracks generated output and whether the latest render created them.

## Useful checks

```bash
git status --short --branch
git diff --stat
git diff -- index.qmd protocols/Mitochondria/index.qmd
rg -n "Crispr Design and Cloning|Alex_s_Protocols|Dhruv_s_Protocols|Angelica_s protocols|TissuePreps" --glob '*.qmd' --glob '*.md' .
```

Before pushing:

```bash
git diff --check
git status --short
quarto render .
git add -A
git diff --cached --stat
git commit -m "Update protocol organization and listings"
git push origin main
```

The GitHub Actions workflow should then appear under the repository's Actions tab for the `main` branch.
