# Session README - 2026-09-17

This file records the link-maintenance workflow used during the September 17, 2026 session.

## Link maintenance workflow

When moving or deleting a page, search the repository for references before and after the change:

```bash
rg -n --glob '*.md' --glob '*.qmd' --glob '*.yml' --glob '*.yaml' \
  'old_filename|old_folder|old/path' .
```

Update every matching Markdown link, folder index table, YAML listing, and explicit sidebar entry. If the target was deleted, remove the entry instead of leaving a dead link. If it was moved, use its new relative path.

## Safe link patterns

```text
Same-folder target: protocol.md
Sibling-folder target: ../cDNA/cDNA.md
Folder-index target: ../../Crispr_Design_and_Cloning/crispr_validation/index.md
```

For site-root links, begin at `/protocols/` and URL-encode spaces. Never use a local filesystem path such as `/home/kpcheung/Desktop/Kitty/protocols-website/...` in website content.

Before adding an image, PDF artifact, or download link, confirm that the target exists. Do not create links for deleted files or missing conversion artifacts. For documentation examples that are not intended to be clickable, use plain text or inline code rather than Markdown link syntax.

## Validation commands

Run the repository checker after link changes:

```bash
python3 scripts/check_quarto_collisions.py --check-links all
```

Then render the site:

```bash
quarto render /home/kpcheung/Desktop/Kitty/protocols-website
```

The default pre-render checker validates index files. The `--check-links all` option also checks links in regular protocol pages.

## Work completed today

- Updated moved-file links for CRISPR validation, cDNA synthesis, and FACS resources.
- Removed the stale Markdown-link syntax from the README example.
- Left missing image and deleted-artifact references unchanged for later review, as requested.
- Confirmed the default pre-render checker passes; the full checker reports only the intentionally deferred image/artifact references.
