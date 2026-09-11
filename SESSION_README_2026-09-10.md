# Session handoff: Lambda, Codex, GitHub build, and deployment

This document records the work completed on September 9–10, 2026 for the
Goldrath protocols website. It is intended to let Kitty or a future Codex
session reproduce the working setup on another Lambda computer.

## Final result

- Repository: `https://github.com/kpc002/protocols-website.git`
- Working directory: `/home/kpcheung/Desktop/Kitty/protocols-website`
- Publishing branch: `main`
- Successful source commit: `b56caa4` (`Fix Quarto deployment without legacy R`)
- Generated-site branch: `cf-pages`
- Successful generated-site commit: `b6eb25b` (`deploy: b56caa4...`)
- Successful GitHub Actions run: [Quarto Publish run 34419828795](https://github.com/kpc002/protocols-website/actions/runs/34419828795)
- GitHub Pages: <https://kpc002.github.io/protocols-website/>
- Custom site: <https://protocols.heeg.io/>

Both website URLs returned HTTP 200 after deployment. The full clean Quarto
test rendered all 454 pages and created `_site/index.html`.

## What was changed on the Lambda computer

The current Lambda account uses `/home/kpcheung`. Older project notes that
refer to `/home/goldrath` describe the previous computer/account and should not
be copied literally.

The following setup was verified on this Lambda:

```text
Miniconda:  /home/kpcheung/miniconda3
Conda:      26.7.1
Codex env:  /home/kpcheung/miniconda3/envs/codex_env
Quarto env: /home/kpcheung/miniconda3/envs/quarto
Node.js:    v22.23.2
npm:        10.9.8
Codex CLI:  0.154.0
Quarto:     1.9.38
```

Important details:

- Codex and Node.js were installed inside a Conda environment in the user's
  home directory. No `sudo` access was required.
- Quarto is kept in a separate Conda environment.
- System R was not upgraded. R 4.1.2 remains installed locally, and
  `renv.lock` still records R 4.1.2 with Bioconductor 3.14.
- The Git checkout was changed from the local `upgrade-r46-bioc323` branch to
  `main` before committing and pushing. The publish workflow runs on pushes to
  `main`, not on pushes to arbitrary branches.
- The repository remote was verified as
  `https://github.com/kpc002/protocols-website.git`.
- The Git identity was verified as `Kitty <kpc002@ucsd.edu>`.
- `gh auth status` reported an expired GitHub CLI token. This did not prevent
  `git push`, because Git's HTTPS credentials were working separately.

No system-wide packages were installed with `sudo` during the successful fix.

## Install Codex with Miniconda without sudo

The official OpenAI documentation supports installing Codex with npm. Conda
was used here to provide a user-owned Node.js installation, so npm's global
package directory remains inside the Conda environment instead of a protected
system directory. See the [official OpenAI Codex CLI documentation](https://developers.openai.com/codex/cli/).

### 1. Install Miniconda if needed

These commands are for a Linux x86-64 Lambda computer:

```bash
cd /tmp
curl -fsSLO https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p "$HOME/miniconda3"
source "$HOME/miniconda3/etc/profile.d/conda.sh"
conda init bash
```

Close and reopen the terminal after `conda init bash`. If Miniconda is already
installed, initialize it in the current terminal with:

```bash
source "$HOME/miniconda3/etc/profile.d/conda.sh"
```

### 2. Create the Codex environment

Do this only if `codex_env` does not already exist:

```bash
conda create --name codex_env --channel conda-forge nodejs=22 --yes
conda activate codex_env
```

### 3. Install and verify Codex

```bash
npm install --global @openai/codex
which node
which npm
which codex
node --version
npm --version
codex --version
```

The paths should contain `miniconda3/envs/codex_env`. On this Lambda,
`which codex` resolves to:

```text
/home/kpcheung/miniconda3/envs/codex_env/bin/codex
```

Do not run `sudo npm install`. If npm asks for system-directory permission,
stop and confirm that `codex_env` is active.

### 4. Sign in and start Codex

```bash
codex login
codex login status
cd /home/kpcheung/Desktop/Kitty/protocols-website
codex
```

The first launch can also present the ChatGPT sign-in choice. If browser
authentication is awkward on a remote machine, inspect the available login
options with:

```bash
codex login --help
```

### 5. Use or update Codex later

```bash
source "$HOME/miniconda3/etc/profile.d/conda.sh"
conda activate codex_env
cd /home/kpcheung/Desktop/Kitty/protocols-website
codex
```

Update within the same environment:

```bash
conda activate codex_env
npm install --global @openai/codex
codex --version
```

## Prepare the repository on a new Lambda computer

If the repository is not present:

```bash
mkdir -p "$HOME/Desktop/Kitty"
cd "$HOME/Desktop/Kitty"
git clone https://github.com/kpc002/protocols-website.git
cd protocols-website
```

If it is already present:

```bash
cd /home/kpcheung/Desktop/Kitty/protocols-website
git remote set-url origin https://github.com/kpc002/protocols-website.git
git fetch origin --prune
git switch main
git pull --ff-only origin main
```

Verify Git identity and repository state:

```bash
git config user.name "Kitty"
git config user.email "kpc002@ucsd.edu"
git remote -v
git status --short --branch
git branch -vv
```

Expected remote:

```text
origin  https://github.com/kpc002/protocols-website.git (fetch)
origin  https://github.com/kpc002/protocols-website.git (push)
```

If GitHub CLI authentication is needed, renew it independently:

```bash
gh auth login -h github.com
gh auth setup-git
gh auth status
```

Do not replace working Git credentials merely because `gh auth status` fails;
`git push` and the `gh` CLI can use different credential stores.

## Why GitHub could push but could not build or deploy

Pushing was successful. The failure was inside GitHub Actions, before Quarto
rendering or deployment began.

Failed run `34385521545` stopped at `Set up R` with this annotation:

```text
Failed to get R 4.1.2: Failed to install R:
The process '/usr/bin/sudo' failed with exit code 100
```

The old workflow requested this environment:

```yaml
- name: Set up R
  uses: r-lib/actions/setup-r@v2
  with:
    r-version: "4.1.2"

- name: Restore R packages
  uses: r-lib/actions/setup-renv@v2
```

Changing `runs-on` from `ubuntu-latest` to `ubuntu-22.04` did not solve it.
GitHub Actions could no longer install that exact old R release on the runner.
The job failed before the system-dependency, render, and deploy steps.

An earlier problem had occurred while compiling `RCurl` during
`renv::restore()`. Adding `libcurl4-openssl-dev` addressed that older problem,
but it could not address the new failure because R itself no longer installed.

## The successful R-related design change

The website publishes protocols and R examples; it does not need to execute
the analyses every time the documentation changes.

Only one tutorial still made Quarto invoke the R/knitr engine:

```text
protocols/bioinformatics/nextflow_rna_seq/index.qmd
```

Its three executable-cell opening markers (three backticks followed by `{r}`)
were changed to ordinary syntax-highlighting markers (three backticks followed
by `r`). The R source remains visible to readers, but Quarto no longer sends it
to knitr during the website build.

The other main R tutorial,
`protocols/bioinformatics/introduction-to-deseq2/index.qmd`, already contains:

```yaml
execute:
  enabled: false
```

After the fence change, the complete site rendered without invoking R. The
GitHub workflow could therefore remove all of these unreliable CI steps:

- `r-lib/actions/setup-r@v2`
- `sudo apt-get install ...`
- `r-lib/actions/setup-renv@v2`

The `renv.lock` file was deliberately left unchanged. It remains historical
information for anyone who wants to reproduce the old analysis environment,
but it is no longer part of website publishing.

If executable analysis is required in the website in the future, create a
separate upgrade branch and update R, Bioconductor, the packages, and
`renv.lock` together. Do not fix this by changing only the workflow's R version;
Bioconductor releases are tied to compatible R releases.

## Final GitHub Actions workflow

The working `.github/workflows/publish.yml` is:

```yaml
on:
  workflow_dispatch:
  push:
    branches: main

name: Quarto Publish

jobs:
  build-deploy:
    runs-on: ubuntu-22.04
    timeout-minutes: 30
    permissions:
      contents: write
    steps:
      - name: Check out repository
        uses: actions/checkout@v5
        with:
          fetch-depth: 0

      - name: Set up Quarto
        uses: quarto-dev/quarto-actions/setup@v2

      - name: Fix timestamps
        run: bash .github/scripts/fix-timestamps

      - name: Render Quarto Project
        uses: quarto-dev/quarto-actions/render@v2
        with:
          path: .

      - name: Deploy
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_branch: cf-pages
          publish_dir: _site
```

Additional workflow changes:

- `actions/checkout` was updated from v4 to v5.
- A 30-minute job timeout was added.
- The deploy action still publishes `_site` to `cf-pages` using GitHub's
  automatically provided `GITHUB_TOKEN`.
- The workflow still supports manual runs through `workflow_dispatch`.

## Other repository changes made during the fix

The pre-render collision checker originally called `path.is_file()` before
checking whether a path was inside an excluded directory. A broken Python
symlink in the local `.venv` caused a `PermissionError` even though `.venv` was
supposed to be excluded.

The order in `scripts/check_quarto_collisions.py` was changed to exclude
`.git`, `.quarto`, `_site`, `.venv`, and `site_libs` before calling
`path.is_file()`.

The following files were included in commit `b56caa4`:

```text
.github/workflows/publish.yml
README.md
codex install.md
protocols/bioinformatics/nextflow_rna_seq/index.qmd
scripts/check_quarto_collisions.py
```

## Install and use Quarto locally without sudo

The `quarto` Conda environment already exists on this Lambda. On a new Lambda,
create it with:

```bash
source "$HOME/miniconda3/etc/profile.d/conda.sh"
conda create --name quarto --channel conda-forge quarto --yes
```

Always activate the environment before calling Quarto:

```bash
source "$HOME/miniconda3/etc/profile.d/conda.sh"
conda activate quarto
quarto --version
```

Calling the environment's `bin/quarto` directly without activation can fail
because Conda's activation scripts set Quarto resource paths. An alternative
that performs activation automatically is:

```bash
conda run --name quarto quarto --version
```

## Local checks before every push

Run these from the repository root:

```bash
cd /home/kpcheung/Desktop/Kitty/protocols-website
python3 scripts/check_quarto_collisions.py
git diff --check
```

Then render with an isolated cache:

```bash
source "$HOME/miniconda3/etc/profile.d/conda.sh"
conda activate quarto
XDG_CACHE_HOME=/tmp/protocols-quarto-cache quarto render
test -f _site/index.html
```

The full render processes 454 pages and can take several minutes. Do not
interrupt it merely because some large PDFs or SVG collections are slow.

The render currently emits non-fatal legacy warnings, including:

- stale links in several `Top_20` pages;
- unresolved DESeq2 cross-references;
- an obsolete `quarto-ext/lightbox` warning.

The stricter command below is useful for future cleanup, but it currently
reports known stale links and is not a required deployment check:

```bash
python3 scripts/check_quarto_collisions.py --check-links all
```

## Commit and push safely

The publish workflow triggers only from `main`, so check the branch first:

```bash
git status --short --branch
git branch --show-current
```

Review and stage intentional files explicitly:

```bash
git diff --check
git diff --stat
git add .github/workflows/publish.yml \
  README.md \
  "codex install.md" \
  protocols/bioinformatics/nextflow_rna_seq/index.qmd \
  scripts/check_quarto_collisions.py
git diff --cached --check
git diff --cached --stat
```

Commit and push:

```bash
git commit -m "Fix Quarto deployment without legacy R"
git push origin main
```

For later updates, use a message that describes the new work instead of
reusing the session's commit message.

## Monitor and verify deployment

Open the Actions page:

<https://github.com/kpc002/protocols-website/actions/workflows/publish.yml>

The required successful steps are:

```text
Check out repository
Set up Quarto
Fix timestamps
Render Quarto Project
Deploy
```

Verify that the generated branch moved:

```bash
git fetch origin cf-pages
git log -1 --oneline origin/cf-pages
```

Verify both live endpoints:

```bash
curl --fail --location --output /dev/null \
  --write-out '%{http_code}\n' \
  https://kpc002.github.io/protocols-website/

curl --fail --location --output /dev/null \
  --write-out '%{http_code}\n' \
  https://protocols.heeg.io/
```

Expected result for each URL:

```text
200
```

## Node.js 20 deprecation warning in the Pages build

After the successful deployment, GitHub displayed this annotation in the
automatically generated `pages build and deployment` workflow:

```text
Node.js 20 is deprecated. The following actions target Node.js 20 but are
being forced to run on Node.js 24: actions/upload-artifact@v4.
```

This was a warning, not the R-related build error described earlier. The
managed Pages run completed successfully:

<https://github.com/kpc002/protocols-website/actions/runs/34420727289>

### Why this warning appears

The repository's `.github/workflows/publish.yml` does not call
`actions/upload-artifact`. The sequence is:

1. `Quarto Publish` renders the site.
2. `peaceiris/actions-gh-pages@v4` pushes `_site` to `cf-pages`.
3. GitHub notices the updated Pages branch and starts its own generated
   `pages build and deployment` workflow.
4. That GitHub-managed workflow currently calls `actions/upload-artifact@v4`,
   which declares a Node.js 20 runtime.
5. GitHub forces the action to run on Node.js 24 and emits the warning.

Because the old action is inside GitHub's generated workflow, adding a new
`actions/upload-artifact` step to this repository would not replace it and
would not remove the warning.

As of September 10, 2026, GitHub has published
[`upload-pages-artifact@v5`](https://github.com/actions/upload-pages-artifact/releases/tag/v5.0.0),
which uses the Node.js 24-compatible `upload-artifact@v7`. GitHub must update
its managed workflow before this repository receives that improvement
automatically.

### Safe response when this is only a warning

Do not change the working deployment solely to silence this annotation.
Instead:

1. Open both the `Quarto Publish` run and the generated
   `pages build and deployment` run.
2. Confirm that each run's overall conclusion is `success`.
3. Confirm that `Render Quarto Project` and `Deploy` completed successfully.
4. Check that `origin/cf-pages` advanced.
5. Confirm that both live URLs return HTTP 200.
6. Leave the workflow unchanged and allow GitHub to update its managed action.

Useful commands:

```bash
git fetch origin cf-pages
git log -1 --oneline origin/cf-pages

curl --fail --location --output /dev/null \
  --write-out 'GitHub Pages: %{http_code}\n' \
  https://kpc002.github.io/protocols-website/

curl --fail --location --output /dev/null \
  --write-out 'Custom site: %{http_code}\n' \
  https://protocols.heeg.io/
```

### If it becomes a real failure later

First identify which workflow failed:

- If `Quarto Publish` failed, inspect this repository's workflow and its
  directly referenced actions.
- If only the generated `pages build and deployment` workflow failed on
  `upload-artifact@v4`, the failing action is still controlled by GitHub.

Check whether this repository has begun calling the action directly:

```bash
cd /home/kpcheung/Desktop/Kitty/protocols-website
rg -n 'upload-artifact|upload-pages-artifact|deploy-pages' .github
```

If a future repository-owned workflow directly uses an obsolete artifact
action, review the current official GitHub release notes and update the direct
reference in a separate branch. Do not blindly reuse the version numbers in
this dated handoff, because action versions may have changed again.

### Why switching deployment systems is not currently the safe fix

It is technically possible to change GitHub Pages from branch publishing to a
custom Actions deployment using GitHub's `configure-pages`,
`upload-pages-artifact`, and `deploy-pages` actions. Do not make that migration
only to remove this warning because:

- the current Quarto and managed Pages runs both succeed;
- `protocols.heeg.io` may rely on Cloudflare reading the `cf-pages` branch;
- replacing `peaceiris/actions-gh-pages` could stop updating `cf-pages`;
- the change requires repository Pages settings and workflow permissions to
  be changed together;
- an incomplete migration could leave GitHub Pages or the custom domain stale.

If a migration becomes necessary, first document the current Cloudflare Pages
source branch and build settings, create a rollback point, test the new
workflow in a branch, and confirm how `cf-pages` will continue to be updated.
Only then change **Settings → Pages → Build and deployment → Source** to
`GitHub Actions`. Verify both domains before removing the old deployment path.

## Short recovery checklist

Use this sequence on the next Lambda computer or after reconnecting:

```bash
source "$HOME/miniconda3/etc/profile.d/conda.sh"
conda activate codex_env

cd "$HOME/Desktop/Kitty/protocols-website"
git fetch origin --prune
git switch main
git pull --ff-only origin main

python3 scripts/check_quarto_collisions.py
git diff --check

conda activate quarto
XDG_CACHE_HOME=/tmp/protocols-quarto-cache quarto render

git status --short --branch
# Stage only reviewed files, then commit.
git push origin main
```

After pushing, wait for `Quarto Publish` to complete and confirm that both site
URLs return HTTP 200.
