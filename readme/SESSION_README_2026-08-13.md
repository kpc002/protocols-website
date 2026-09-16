# Session README - 2026-08-13

This file summarizes the protocol website work completed on Thursday, August 13, 2026, and is intended to make it easy to resume tomorrow.

## Main Changes

- Moved `protocols/Alex_s_Protocols/CRISPR_Amplicon_Sequencing/` to top-level `protocols/CRISPR_Amplicon_Sequencing/`.
- Moved `protocols/Angelica_s protocols/Sanger Sequencing Preparation.md` into `protocols/CRISPR_Amplicon_Sequencing/`.
- Moved `protocols/Cloning/Protocol for CRISPR amplicon sequencing 2025-11-06 (etr_PxVJqvYTzT) Custom_low_plex_LsgA_cloning_MRC.md` and its `.docx` into `protocols/CRISPR_Amplicon_Sequencing/`.
- Restored `protocols/Giovanni_s_Protocols/molecular/MB6.Perturb-seq/10X_protocol.md`, `10X_protocol.pdf`, and `10X_protocol_artifacts/` back to their original `MB6.Perturb-seq` location after an initial move to `CRISPR_Amplicon_Sequencing/`.
- Moved `protocols/Cloning/cDNA.md` back to `protocols/mol_bio/cDNA.md`.
- Updated `protocols/Cloning/index.qmd` listing fields to include `image`.

## Cloning Folder State

- The landing page source is `protocols/Cloning/index.qmd`.
- `protocols/Cloning/cDNA.md` was removed from Cloning and restored to `protocols/mol_bio/cDNA.md`.
- The Cloning landing page successfully rendered after the `cDNA.md` move.
- `protocols/Cloning/2024_NEB_Logo_lg.png` is currently untracked.

## CRISPR Amplicon Sequencing Folder State

Current notable contents of `protocols/CRISPR_Amplicon_Sequencing/`:

- `index.md`
- `dna.svg`
- `Example_Amplicon_DNA_Files/`
- `Example_Amplicon_DNA_Files.zip`
- `Sanger Sequencing Preparation.md`
- `Protocol for CRISPR amplicon sequencing 2025-11-06 (etr_PxVJqvYTzT) Custom_low_plex_LsgA_cloning_MRC.md`
- `Protocol for CRISPR amplicon sequencing 2025-11-06 (etr_PxVJqvYTzT) Custom_low_plex_LsgA_cloning_MRC.docx`

Important:

- `10X_protocol.*` is no longer in `protocols/CRISPR_Amplicon_Sequencing/`.
- There is still a leftover nested empty path under `protocols/CRISPR_Amplicon_Sequencing/protocols/Giovanni_s protocols/molecular/MB6.Perturb-seq/` from the earlier move/restore cycle. It looks safe to clean up, but it has not been removed yet.

## 10X Protocol Restore

These were restored to their original location:

- `protocols/Giovanni_s_Protocols/molecular/MB6.Perturb-seq/10X_protocol.md`
- `protocols/Giovanni_s_Protocols/molecular/MB6.Perturb-seq/10X_protocol.pdf`
- `protocols/Giovanni_s_Protocols/molecular/MB6.Perturb-seq/protocols/Giovanni_s protocols/molecular/MB6.Perturb-seq/10X_protocol_artifacts/`

Also restored:

- `10X_protocol.md` front matter image back to `oligo.svg`.

## Current Git Status Snapshot

Observed from `git status --short` during this session:

- Deleted from old locations:
  - `protocols/Alex_s_Protocols/CRISPR_Amplicon_Sequencing/...`
  - `protocols/Angelica_s protocols/Sanger Sequencing Preparation.md`
  - `protocols/Cloning/Protocol for CRISPR amplicon sequencing 2025-11-06 (etr_PxVJqvYTzT) Custom_low_plex_LsgA_cloning_MRC.md`
  - `protocols/Cloning/Protocol for CRISPR amplicon sequencing 2025-11-06 (etr_PxVJqvYTzT) Custom_low_plex_LsgA_cloning_MRC.docx`
  - `protocols/Cloning/cDNA.md`
- Modified:
  - `protocols/Cloning/index.qmd`
  - `protocols/Cloning/NucleoBond Xtra Plasmid DNA Purification User Manual.md`
  - `protocols/Cloning/nebuilder-hifi-dna-assembly-reaction-protocol.md`
  - `protocols/Cloning/protocol-for-q5-high-fidelity-2x-master-mix-m0492.md`
- Untracked:
  - `protocols/CRISPR_Amplicon_Sequencing/`
  - `protocols/Cloning/2024_NEB_Logo_lg.png`
  - `protocols/mol_bio/cDNA.md`
  - `SESSION_README_2026-08-13.md`

## Render Status

A full project render was started with:

```bash
XDG_CACHE_HOME=/tmp/protocols-quarto-cache quarto render /home/goldrath/Desktop/Kitty/protocols-website
```

Status when this note was written:

- The render was still in progress.
- It had successfully passed the restored `protocols/Giovanni_s_Protocols/molecular/MB6.Perturb-seq/10X_protocol.md`.
- It had reached at least item `267/450`.

Warnings observed so far during the full render:

- In `protocols/bioinformatics/introduction-to-deseq2/index.qmd`:
  - unresolved crossref `@tbl-counts`
  - unresolved crossref `@fig-pca`
  - unresolved crossref `@fig-distance`
  - unresolved crossref `@fig-ma_plot`
  - unresolved crossref `@fig-ma_plot_lfc`
- Quarto extension warning:
  - `quarto-ext/lightbox` appears built in and may not need to remain installed
- In `protocols/bioinformatics/scenic/02_prepare_input/index.md`:
  - shortcode `lightbox` not found

Because the render had not finished yet, this file does not claim a final pass/fail result for the full site render.

## Suggested First Steps Tomorrow

1. Re-run `git status --short` to confirm the current tree matches the notes above.
2. Decide whether to remove the leftover empty nested directory under `protocols/CRISPR_Amplicon_Sequencing/protocols/.../MB6.Perturb-seq/`.
3. Re-run the full Quarto render and capture the final exit status and any late-stage errors.
4. Decide whether the moved CRISPR amplicon pages need additional associated media, especially the `Custom_low_plex_LsgA_cloning_MRC` page, which still references `media/image1.png` and `media/image2.png`.
5. Stage moves with `git add -A` once the folder layout is confirmed.

## Useful Commands

```bash
git -C /home/goldrath/Desktop/Kitty/protocols-website status --short
XDG_CACHE_HOME=/tmp/protocols-quarto-cache quarto render /home/goldrath/Desktop/Kitty/protocols-website
XDG_CACHE_HOME=/tmp/protocols-quarto-cache quarto render /home/goldrath/Desktop/Kitty/protocols-website/protocols/Cloning/index.qmd
```
