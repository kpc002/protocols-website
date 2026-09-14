# Codex install with Miniconda (no sudo)

This setup installs Node.js and the Codex CLI inside a Miniconda environment in
your home directory. It does not require administrator access or `sudo`.

## 1. Install Miniconda (skip if already installed)

For a Linux x86-64 computer:

```bash
cd /tmp
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p "$HOME/miniconda3"
source "$HOME/miniconda3/etc/profile.d/conda.sh"
conda init bash
```

Close and reopen the terminal after `conda init bash`.

If Miniconda is already installed but `conda` is not available in the current
terminal, run:

```bash
source "$HOME/miniconda3/etc/profile.d/conda.sh"
```

## 2. Create an environment for Codex

```bash
conda create --name codex_env --channel conda-forge nodejs=22 --yes
conda activate codex_env
```

Using a separate environment prevents Codex and Node.js packages from changing
other Conda projects.

## 3. Install the Codex CLI

```bash
npm install --global @openai/codex
```

Although this is an npm "global" install, the active Conda environment places
it under `$HOME/miniconda3/envs/codex_env`; it does not write to system folders
and therefore does not need `sudo`.

Verify the installation:

```bash
which codex
codex --version
```

The `which` output should look similar to:

```text
/home/YOUR_USERNAME/miniconda3/envs/codex_env/bin/codex
```

## 4. Sign in and start Codex

```bash
codex login
codex login status
codex
```

Follow the browser sign-in instructions shown by `codex login`. For the
official installation and authentication guidance, see the
[OpenAI Codex CLI documentation](https://developers.openai.com/codex/cli/).

## Use Codex later

In each new terminal session, activate the environment before starting Codex:

```bash
conda activate codex_env
cd /path/to/your/project
codex
```

For the login-status check, browser sign-in steps, and the September 14, 2026
login example, see [`CODEX_LOGIN_README.md`](CODEX_LOGIN_README.md). A saved
login normally survives a terminal restart, so `codex login` is only needed
when `codex login status` says you are signed out.

When finished:

```bash
conda deactivate
```

## Update Codex

```bash
conda activate codex_env
npm install --global @openai/codex@latest
codex --version
```

## Troubleshooting

If `conda activate` reports that the shell is not initialized:

```bash
source "$HOME/miniconda3/etc/profile.d/conda.sh"
conda activate codex_env
```

If `npm install --global` reports a permissions error, confirm that the Conda
environment is active and that Node and npm come from it:

```bash
conda activate codex_env
which node
which npm
```

Both paths should contain `miniconda3/envs/codex_env`. Do not use `sudo npm`.
