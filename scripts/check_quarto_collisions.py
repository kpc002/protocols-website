#!/usr/bin/env python3

from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path


RENDERABLE_SUFFIXES = {".md", ".qmd", ".ipynb"}
HTML_SUFFIX = ".html"
EXCLUDED_PARTS = {".git", ".quarto", "_site", ".venv", "site_libs"}


def iter_relevant_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in EXCLUDED_PARTS for part in path.parts):
            continue
        suffix = path.suffix.lower()
        if suffix in RENDERABLE_SUFFIXES or suffix == HTML_SUFFIX:
            yield path


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    renderables: dict[str, list[str]] = defaultdict(list)
    html_files: dict[str, list[str]] = defaultdict(list)

    for path in iter_relevant_files(repo_root):
        rel = path.relative_to(repo_root)
        key = str(rel.with_suffix(""))
        suffix = path.suffix.lower()
        rel_str = str(rel)
        if suffix in RENDERABLE_SUFFIXES:
            renderables[key].append(rel_str)
        elif suffix == HTML_SUFFIX:
            html_files[key].append(rel_str)

    duplicate_renderables = {
        key: sorted(paths)
        for key, paths in renderables.items()
        if len(paths) > 1
    }
    html_collisions = {
        key: {
            "renderables": sorted(renderables[key]),
            "html": sorted(html_files[key]),
        }
        for key in sorted(set(renderables) & set(html_files))
    }

    if not duplicate_renderables and not html_collisions:
        return 0

    print("Quarto source collision check failed.", file=sys.stderr)
    print(
        "Keep exactly one renderable source per page basename, and do not leave "
        "same-stem HTML files in the source tree.",
        file=sys.stderr,
    )

    if duplicate_renderables:
        print("\nDuplicate renderable source stems:", file=sys.stderr)
        for key in sorted(duplicate_renderables):
            print(f"  {key}", file=sys.stderr)
            for path in duplicate_renderables[key]:
                print(f"    - {path}", file=sys.stderr)

    if html_collisions:
        print("\nHTML files colliding with renderable sources:", file=sys.stderr)
        for key in sorted(html_collisions):
            print(f"  {key}", file=sys.stderr)
            for path in html_collisions[key]["renderables"]:
                print(f"    - renderable: {path}", file=sys.stderr)
            for path in html_collisions[key]["html"]:
                print(f"    - html: {path}", file=sys.stderr)

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
