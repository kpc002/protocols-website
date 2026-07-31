#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote, urlsplit


RENDERABLE_SUFFIXES = {".md", ".qmd", ".ipynb"}
HTML_SUFFIX = ".html"
EXCLUDED_PARTS = {".git", ".quarto", "_site", ".venv", "site_libs"}
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\n]+)\)")
URL_SCHEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
INDEX_FILENAMES = {"index.md", "index.qmd"}


def iter_relevant_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in EXCLUDED_PARTS for part in path.parts):
            continue
        suffix = path.suffix.lower()
        if suffix in RENDERABLE_SUFFIXES or suffix == HTML_SUFFIX:
            yield path


def iter_link_check_files(root: Path, mode: str):
    if mode == "none":
        return

    for path in iter_relevant_files(root):
        if path.suffix.lower() not in {".md", ".qmd"}:
            continue
        if mode == "index" and path.name not in INDEX_FILENAMES:
            continue
        yield path


def normalize_link_target(raw_target: str) -> str | None:
    target = raw_target.strip()
    if not target or target.startswith("#"):
        return None

    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()

    if target.startswith(("{{<", "{{%")):
        return None

    if URL_SCHEME_RE.match(target):
        return None

    split = urlsplit(target)
    path = unquote(split.path)
    if not path:
        return None

    return path


def candidate_paths(repo_root: Path, source: Path, target: str):
    if target.startswith("/"):
        resolved = repo_root / target.lstrip("/")
    else:
        resolved = source.parent / target

    yield resolved

    if resolved.suffix == HTML_SUFFIX:
        yield resolved.with_suffix(".qmd")
        yield resolved.with_suffix(".md")
        yield resolved.with_suffix(".ipynb")

    if not resolved.suffix:
        yield resolved.with_suffix(".qmd")
        yield resolved.with_suffix(".md")
        yield resolved.with_suffix(".ipynb")
        yield resolved / "index.qmd"
        yield resolved / "index.md"


def link_target_exists(repo_root: Path, source: Path, target: str) -> bool:
    return any(path.exists() for path in candidate_paths(repo_root, source, target))


def find_missing_local_links(repo_root: Path, mode: str):
    missing: dict[str, list[str]] = defaultdict(list)

    for source in iter_link_check_files(repo_root, mode):
        try:
            text = source.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = source.read_text(encoding="utf-8", errors="replace")

        for match in MARKDOWN_LINK_RE.finditer(text):
            target = normalize_link_target(match.group(1))
            if target is None:
                continue
            if not link_target_exists(repo_root, source, target):
                rel_source = str(source.relative_to(repo_root))
                missing[rel_source].append(match.group(1).strip())

    return {source: sorted(set(targets)) for source, targets in sorted(missing.items())}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Check Quarto source files for duplicate render targets, source-side "
            "HTML collisions, and stale local links."
        )
    )
    parser.add_argument(
        "--check-links",
        choices=("none", "index", "all"),
        default="index",
        help=(
            "Validate local Markdown links. 'index' checks only index.md/index.qmd "
            "files and is the default pre-render setting; 'all' checks every "
            "Markdown/Quarto source file."
        ),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
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
    missing_links = find_missing_local_links(repo_root, args.check_links)

    if not duplicate_renderables and not html_collisions and not missing_links:
        return 0

    print("Quarto source check failed.", file=sys.stderr)
    print(
        "Keep exactly one renderable source per page basename, do not leave "
        "same-stem HTML files in the source tree, and remove stale local links.",
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

    if missing_links:
        print("\nMissing local links:", file=sys.stderr)
        for source in sorted(missing_links):
            print(f"  {source}", file=sys.stderr)
            for target in missing_links[source]:
                print(f"    - {target}", file=sys.stderr)

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
