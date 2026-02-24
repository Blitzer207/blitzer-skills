#!/usr/bin/env python
"""Search ecu.test Sphinx search index for titles, terms, and objects.

Usage examples:
  # Use default version (ECU_TEST_HOME or latest ECU_TEST_<version>_HOME from .env)
  python scripts/search_api.py --query AnalysisJobApi

  # Pin a specific version from .env:
  python scripts/search_api.py --version 2025.4 --query AnalysisJobApi

  # Search a specific docset:
  python scripts/search_api.py --version 2025.4 --docset traceanalysis --query templates
  python scripts/search_api.py --version 2025.4 --docset tracestep --query Threshold

Notes:
  - Older Sphinx builds expose `docnames` (no extension).
  - Newer Sphinx builds (e.g. 8.x) expose `docurls` (includes .html) and may omit `_sources/`.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from typing import Iterable

from env import get_ecu_test_home, load_dotenv


def _pick_base(home: str, docset: str) -> str:
    """Pick a Sphinx doc root for the given version/docset.

    We pick the first directory that contains a `searchindex.js`.
    """
    if docset == "main":
        candidates = [
            os.path.join(home, "Help", "APIDoc"),
            os.path.join(home, "Help", "api"),
        ]
    elif docset == "traceanalysis":
        candidates = [
            os.path.join(home, "Help", "APIDoc", "TraceanalysisAPI"),
            os.path.join(home, "Help", "api", "TraceAnalysisAPI"),
            os.path.join(home, "Help", "api", "TraceanalysisAPI"),
        ]
    elif docset == "tracestep":
        candidates = [
            os.path.join(home, "Help", "TraceStepTemplatesDoc"),
            os.path.join(home, "Help", "trcp"),
        ]
    else:
        raise ValueError(f"Unknown docset: {docset}")

    for base in candidates:
        if os.path.exists(os.path.join(base, "searchindex.js")):
            return base

    raise FileNotFoundError(
        "searchindex.js not found for docset="
        f"{docset!r}. Tried: " + ", ".join(candidates)
    )


def _load_index(base_dir: str) -> dict:
    index_path = os.path.join(base_dir, "searchindex.js")
    if not os.path.exists(index_path):
        raise FileNotFoundError(index_path)
    with open(index_path, "r", encoding="utf-8") as f:
        text = f.read()
    match = re.search(r"Search\.setIndex\((.*)\)\s*$", text, re.S)
    if not match:
        raise ValueError("searchindex.js format not recognized")
    return json.loads(match.group(1))


def _doc_url(index: dict, docid: int) -> str:
    """Return the HTML URL (relative to the Sphinx base) for a doc id."""
    docurls = index.get("docurls")
    if isinstance(docurls, list) and 0 <= docid < len(docurls):
        return str(docurls[docid])
    docnames = index.get("docnames")
    if isinstance(docnames, list) and 0 <= docid < len(docnames):
        return str(docnames[docid]) + ".html"
    raise IndexError(f"docid out of range: {docid}")


def _format_path(
    base_dir: str, index: dict, docid: int, anchor: str | None, fmt: str, has_sources: bool
) -> tuple[str, str | None]:
    """Return (path, anchor_for_info) for the requested output format."""
    fmt_effective = fmt
    if fmt_effective == "auto":
        fmt_effective = "rst" if has_sources else "html"
    if fmt_effective == "rst" and not has_sources:
        # Do not print non-existing RST paths for Sphinx builds that do not ship sources.
        fmt_effective = "html"

    doc_url = _doc_url(index, docid)
    doc_url = doc_url.replace("/", os.sep)

    if fmt_effective == "html":
        path = os.path.join(base_dir, doc_url)
        if anchor:
            path = f"{path}#{anchor}"
        return path, None

    # RST is stored under _sources with a .rst.txt suffix in ecu.test doc builds.
    rst_rel = doc_url
    if rst_rel.endswith(".html"):
        rst_rel = rst_rel[: -len(".html")]
    path = os.path.join(base_dir, "_sources", rst_rel + ".rst.txt")
    # Anchors do not apply to RST files, but it's still useful context for users.
    return path, anchor


def _normalize_doc_ids(value) -> list[int]:
    if isinstance(value, int):
        return [value]
    if isinstance(value, list):
        return [v for v in value if isinstance(v, int)]
    return []


def _iter_objects(objects: dict) -> Iterable[tuple[str, list]]:
    for key, value in objects.items():
        if isinstance(value, list):
            yield key, value
        elif isinstance(value, dict):
            for subkey, subval in _iter_objects(value):
                full = f"{key}.{subkey}" if key else subkey
                yield full, subval


def search_index(
    index: dict, base_dir: str, query: str, kinds: set[str], fmt: str
) -> list[tuple[str, str, str, str | None]]:
    q = query.lower()
    results: list[tuple[str, str, str, str | None]] = []
    seen = set()
    has_sources = os.path.isdir(os.path.join(base_dir, "_sources"))

    if "titles" in kinds:
        for title, entries in index.get("alltitles", {}).items():
            if q in title.lower():
                for docid, anchor in entries:
                    path, anchor_out = _format_path(base_dir, index, docid, anchor, fmt, has_sources)
                    key = ("title", title, path, anchor_out)
                    if key not in seen:
                        seen.add(key)
                        results.append(key)

    if "terms" in kinds:
        for term, value in index.get("terms", {}).items():
            if q in term.lower():
                for docid in _normalize_doc_ids(value):
                    path, anchor_out = _format_path(base_dir, index, docid, None, fmt, has_sources)
                    key = ("term", term, path, anchor_out)
                    if key not in seen:
                        seen.add(key)
                        results.append(key)

    if "objects" in kinds:
        for prefix, entries in _iter_objects(index.get("objects", {})):
            for entry in entries:
                if not isinstance(entry, list) or len(entry) < 5:
                    continue
                docid = entry[0]
                name = entry[4]
                full = f"{prefix}.{name}" if prefix else name
                if q in full.lower():
                    path, anchor_out = _format_path(base_dir, index, docid, None, fmt, has_sources)
                    key = ("object", full, path, anchor_out)
                    if key not in seen:
                        seen.add(key)
                        results.append(key)

    return results


def main() -> int:
    load_dotenv()
    parser = argparse.ArgumentParser(description="Search ecu.test Sphinx API index")
    parser.add_argument(
        "--version",
        help="ecu.test version to use (e.g. 2025.4). Resolved via ECU_TEST_<version>_HOME in .env",
    )
    parser.add_argument(
        "--docset",
        default="main",
        choices=["main", "traceanalysis", "tracestep"],
        help="Which Sphinx docset to search (default: main)",
    )
    parser.add_argument("--query", required=True, help="Search string (case-insensitive)")
    parser.add_argument("--base", help="Override Sphinx base directory (advanced)")
    parser.add_argument("--limit", type=int, default=25, help="Max results to print")
    parser.add_argument(
        "--format",
        default="auto",
        choices=["auto", "rst", "html"],
        help="Output format for paths (default: auto = rst if _sources exists else html)",
    )
    parser.add_argument(
        "--kind",
        default="all",
        choices=["all", "titles", "terms", "objects"],
        help="Which index sections to search",
    )
    args = parser.parse_args()

    kinds = {"titles", "terms", "objects"} if args.kind == "all" else {args.kind}
    home = get_ecu_test_home(args.version)
    base = args.base or _pick_base(home, args.docset)

    try:
        index = _load_index(base)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

    if args.format == "rst" and not os.path.isdir(os.path.join(base, "_sources")):
        print("Note: _sources not found under base. Falling back to HTML paths.", file=sys.stderr)

    results = search_index(index, base, args.query, kinds, args.format)

    if not results:
        print("No matches found.")
        return 1

    for kind, name, path, anchor in results[: args.limit]:
        if anchor and args.format in {"rst", "auto"} and os.path.isdir(os.path.join(base, "_sources")):
            print(f"[{kind}] {name} -> {path} (anchor: {anchor})")
        else:
            print(f"[{kind}] {name} -> {path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
