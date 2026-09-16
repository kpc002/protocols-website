# Starting Codex after a terminal or computer restart

This checklist is for the Codex CLI on Kitty's Lambda computer. Codex is
installed in the Miniconda environment `codex_env`, and the website repository
is at `/home/kpcheung/Desktop/Kitty/protocols-website`.

## Every new terminal session

```bash
source "$HOME/miniconda3/etc/profile.d/conda.sh"
conda activate codex_env
cd /home/kpcheung/Desktop/Kitty/protocols-website
codex login status
codex
```

If `conda` is already available, the `source` line is optional. The `codex`
command should come from
`/home/kpcheung/miniconda3/envs/codex_env/bin/codex`; check with `which codex`
if it is not found or a different version starts.

**You do not normally need to log in again after each restart.** Codex reuses
its saved sign-in and refreshes ChatGPT tokens during use. `codex login status`
shows whether the CLI is signed in. If it reports that you are not logged in,
run:

```bash
codex login
```

Complete the ChatGPT sign-in in the browser that opens (or open the URL printed
in the terminal), then return to the terminal and check:

```bash
codex login status
codex
```

Use the same ChatGPT account you intend to use with Codex. Do **not** run
`codex logout` as part of normal startup; it removes the CLI's saved login.
Do not put passwords, one-time codes, API keys, or the contents of
`~/.codex/auth.json` in this repository.

## What happened on September 14, 2026

- The local Codex CLI was available from `codex_env` and reported version
  `0.154.0` when checked.
- The local login log records a browser login starting at approximately
  **9:54 a.m. PDT**, but no successful callback for that attempt.
- A second browser login started at approximately **10:58 a.m. PDT**. Its
  browser callback and token exchange succeeded at **10:59 a.m. PDT**.
- The saved credential cache was updated at **10:59 a.m. PDT**. A subsequent
  `codex login status` reported **`Logged in using ChatGPT`**.

The practical fix today was to complete the browser sign-in flow after
starting `codex login`; activating `codex_env` makes the installed `codex`
command available in a fresh terminal. There is no evidence that reinstalling
Codex or signing out of ChatGPT is required for each restart.

## If browser sign-in does not complete

On a remote/headless machine, or if the browser cannot return to Codex's
localhost callback, try device-code login:

```bash
codex login --device-auth
```

Open the displayed link on a browser-capable device, sign in, and enter the
one-time code. Device-code login must be enabled in ChatGPT security settings
or by the workspace administrator. If the normal browser flow stalls, retry
`codex login` and finish the browser flow before starting `codex`.

See the official OpenAI documentation for [Codex authentication](https://learn.chatgpt.com/docs/auth)
and the [Codex CLI](https://learn.chatgpt.com/docs/codex/cli). For installation
and updates on this computer, see [`codex install.md`](../codex%20install.md).
