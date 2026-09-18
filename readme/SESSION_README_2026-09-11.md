# Protocols website session handoff

This document records the September 10–11, 2026 work on the Goldrath
protocols website. It is a practical checklist for starting Quarto, editing the
site, checking changes, pushing to GitHub, and recovering from failed renders.

## Project locations and publishing model

- Local repository: `/home/kpcheung/Desktop/Kitty/protocols-website`
- GitHub repository: `https://github.com/kpc002/protocols-website`
- Source branch: `main`
- Generated website branch: `cf-pages`
- Quarto output directory: `_site/`
- GitHub Pages: `https://kpc002.github.io/protocols-website/`
- Custom website: `https://protocols.heeg.io/`

Only source files belong on `main`. GitHub Actions renders the site into
`_site/` and publishes that output to `cf-pages`.

## Start Quarto in a new terminal

Quarto is installed in a Miniconda environment owned by the current user. No
`sudo` access is needed.

```bash
source /home/kpcheung/miniconda3/etc/profile.d/conda.sh
conda activate quarto
cd /home/kpcheung/Desktop/Kitty/protocols-website
```

Verify the active programs before working:

```bash
which conda
which quarto
quarto --version
git status --short --branch
```

The expected Quarto environment is:

```text
/home/kpcheung/miniconda3/envs/quarto
```

If Conda is already initialized by the shell, this shorter sequence is enough:

```bash
conda activate quarto
cd /home/kpcheung/Desktop/Kitty/protocols-website
```

Quarto can also be run without activating the environment:

```bash
/home/kpcheung/miniconda3/bin/conda run -n quarto quarto --version
/home/kpcheung/miniconda3/bin/conda run -n quarto quarto render /home/kpcheung/Desktop/Kitty/protocols-website
```

When finished:

```bash
conda deactivate
```

## Start Codex in a separate terminal

Codex uses a separate Miniconda environment:

```bash
source /home/kpcheung/miniconda3/etc/profile.d/conda.sh
conda activate codex_env
cd /home/kpcheung/Desktop/Kitty/protocols-website
codex
```

For full installation details, see `codex install.md` and
`SESSION_README_2026-09-10.md` in the repository root.

## Important project configuration

The beginning of `_quarto.yml` should retain these settings:

```yaml
project:
  type: website
  pre-render:
    - python3 scripts/check_quarto_collisions.py
  output-dir: _site
```

These settings make the directory a website project, run the source/link
check before rendering, and direct completed website output to `_site/`.

Search is configured so a document initially appears once even when several
sections match a term:

```yaml
website:
  search:
    location: navbar
    collapse-after: 1
```

Do not remove the pre-render check merely to make a failing build green. Fix
the collision, invalid YAML, or stale link that the check reports.

## Recommended editing workflow

### 1. Begin from a known repository state

Before pulling, make sure there are no uncommitted changes that could be
overwritten or mixed with incoming work:

```bash
cd /home/kpcheung/Desktop/Kitty/protocols-website
git status --short --branch
git branch --show-current
git remote -v
```

If the tree is clean, update `main`:

```bash
git switch main
git pull --ff-only origin main
```

If the tree is not clean, finish, commit, or deliberately stash the current
work before pulling. Do not use `git reset --hard` to solve an unclear state.

### 2. Edit source files, not generated pages

Edit `.md`, `.qmd`, `.ipynb`, CSS, YAML, and supporting assets. Do not edit
generated copies in `_site/` or same-name `.html` files.

Use Git-aware commands when moving or deleting files:

```bash
git mv "old folder/old protocol.md" "new folder/new protocol.md"
git rm "folder/protocol to delete.md"
```

After a move, search for references to the old path and update them:

```bash
rg -n -F "old folder/old protocol.md" . --glob '*.md' --glob '*.qmd' --glob '*.yml' --glob '*.yaml'
```

Use relative Markdown links from the file containing the link. For example,
two files in the same directory should link like this:

```markdown
Retroviral transduction → transduction.md
```

Do not repeat the parent path inside a relative link. That caused this broken
target during the session:

```text
protocols/Transfection and Transduction/Transfection and Transduction/Polybrene/transduction.md
```

### 3. Check source files before rendering

Run the repository check after moves, deletions, link edits, or YAML edits:

```bash
python3 scripts/check_quarto_collisions.py
```

It checks for:

- multiple renderable files with the same page basename;
- `.html` files beside matching `.md`, `.qmd`, or `.ipynb` sources;
- links to missing local files or folders.

Also check whitespace and Git state:

```bash
git diff --check
git status --short
```

### 4. Preview while editing

Start the preview from the project root:

```bash
quarto preview
```

Navigate to the page being edited in the browser. Stop the preview with
`Ctrl-C` when finished.

Avoid using `quarto render some-file.md` as the normal workflow for this site.
A single-document render can leave `some-file.html` next to the source,
especially when a render fails or is interrupted.

### 5. Perform a complete project render

Before committing, render from the repository root with no file argument:

```bash
cd /home/kpcheung/Desktop/Kitty/protocols-website
python3 scripts/check_quarto_collisions.py
quarto render
```

The site contains hundreds of pages and can take longer than five minutes.
Allow it to finish. Do not add a short timeout and do not interrupt a healthy
full render.

Successful output should end with a message similar to:

```text
Output created: _site
```

Then check again:

```bash
python3 scripts/check_quarto_collisions.py
git status --short
```

`_site/` is ignored by Git. It should not appear among files to commit.

## Recover after a failed or interrupted render

A failed or interrupted render may leave generated HTML beside source files.
The next render will then be stopped by the collision check.

First list only HTML files that have a matching source. This does not delete
anything:

```bash
cd /home/kpcheung/Desktop/Kitty/protocols-website
python3 - <<'PY'
from pathlib import Path

excluded = {".git", "_site", "_freeze", "node_modules"}

for html in Path(".").rglob("*.html"):
    if any(part in excluded for part in html.parts):
        continue
    if any(html.with_suffix(suffix).exists()
           for suffix in (".md", ".qmd", ".ipynb")):
        print(html)
PY
```

Review the entire list. Standalone HTML files without a Markdown, Quarto, or
notebook counterpart are intentionally excluded.

If the list is correct, remove only those generated counterparts:

```bash
python3 - <<'PY'
from pathlib import Path

excluded = {".git", "_site", "_freeze", "node_modules"}
removed = 0

for html in Path(".").rglob("*.html"):
    if any(part in excluded for part in html.parts):
        continue
    if any(html.with_suffix(suffix).exists()
           for suffix in (".md", ".qmd", ".ipynb")):
        html.unlink()
        print(f"Removed: {html}")
        removed += 1

print(f"Removed {removed} generated HTML counterparts")
PY
```

Tracked files removed this way remain recoverable from Git until the deletion
is committed. Untracked files are not recoverable from Git, which is why the
preview step is mandatory.

Verify recovery before rendering again:

```bash
python3 scripts/check_quarto_collisions.py
git status --short
```

Do not run a broad command such as `rm -rf`, `git clean -fdx`, or
`git reset --hard`. Do not add `*.html` to `.gitignore`, because the project
may contain intentional standalone HTML resources.

## YAML front matter checks

Empty YAML values can stop the entire build. This failed during the session:

```yaml
author:
```

Remove an unused field or provide a valid value:

```yaml
author: "Goldrath Lab"
```

For multiple authors, use a YAML list:

```yaml
author:
  - name: First Author
  - name: Second Author
```

When Quarto reports a line number, inspect that document's opening `---`
block first.

## Review, commit, and push

Never commit immediately after a large move or cleanup. Review what Git will
record:

```bash
git status --short
git diff --stat
git diff --check
```

Stage intended additions, modifications, moves, and deletions:

```bash
git add -A
git status --short
git diff --cached --stat
git diff --cached --check
```

If the staged list contains generated HTML, `_site/`, `site_libs/`, or
unexpected files, stop and investigate before committing.

Commit and push only after the source check and full render succeed:

```bash
git commit -m "Describe the website changes"
git push origin main
```

A successful `git push` only means GitHub received the source commit. It does
not mean that the website build or deployment succeeded.

## Watch GitHub Actions and deployment

Every push to `main` triggers `.github/workflows/publish.yml`. The workflow:

1. checks out the repository;
2. installs Quarto;
3. restores source timestamps;
4. renders the website;
5. publishes `_site/` to `cf-pages`.

Watch the newest run:

```bash
gh run watch --repo kpc002/protocols-website --exit-status
```

List recent runs:

```bash
gh run list --repo kpc002/protocols-website --limit 5
```

If a run fails, copy its numeric run ID and retrieve only the failed log:

```bash
gh run view RUN_ID --repo kpc002/protocols-website --log-failed
```

If `gh` is not authenticated:

```bash
gh auth login -h github.com
gh auth status
```

After a successful workflow, verify both sites:

```bash
curl -I https://kpc002.github.io/protocols-website/
curl -I https://protocols.heeg.io/
```

Look for an HTTP `200` response.

## Session summary

Work completed during this session included:

- Updated the homepage to remove the link to the absent `Top_20` directory.
- Compared protocol documents and removed duplicate copies from `Top_20` while
  preserving originals in their canonical folders.
- Identified and corrected invalid empty YAML front matter such as `author:`.
- Configured Quarto search with `collapse-after: 1` so a matching page is
  initially grouped into one search result.
- Diagnosed GitHub Actions failures using the actual failed-run logs.
- Determined that a successful push can still be followed by a failed render.
- Removed generated HTML files that had been committed beside their Markdown,
  Quarto, or notebook counterparts.
- Removed stale links to absent `Curated protocols`, `Ilkka`, `Kyla`, and
  `Laura` pages.
- Corrected the duplicated relative path in `Transduction Polybrene.md`.
- Kept the project output directed to `_site/` and retained the pre-render
  collision/link checker.
- Confirmed that the Node.js 20 deprecation message is a warning about action
  runtime compatibility; the actual exit-code-1 failures in this session came
  from Quarto source validation, invalid YAML, and stale links.

The earlier successful deployment removed the need to install or restore old
R 4.1.2 packages in GitHub Actions. R examples remain visible as code, but the
website build does not execute the legacy analyses. This avoids the previous
`sudo`, R installation, and `renv` failures on GitHub-hosted runners.

## Fast checklist

Use this compact checklist for routine updates:

```bash
source /home/kpcheung/miniconda3/etc/profile.d/conda.sh
conda activate quarto
cd /home/kpcheung/Desktop/Kitty/protocols-website

git status --short --branch
git switch main
git pull --ff-only origin main

# Edit files; use git mv and git rm for moves and deletions.

python3 scripts/check_quarto_collisions.py
git diff --check
quarto render
python3 scripts/check_quarto_collisions.py

git status --short
git add -A
git diff --cached --stat
git diff --cached --check
git commit -m "Describe the website changes"
git push origin main

gh run watch --repo kpc002/protocols-website --exit-status
```

If the render is interrupted, run the HTML preview and cleanup commands in
the recovery section before attempting the next render.
