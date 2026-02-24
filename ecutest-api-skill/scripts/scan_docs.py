#!/usr/bin/env python
"""
Generate directory trees and search hits for local ecu.test docs.

Examples (replace <ECU_TEST_HOME> with your install path):
  # <=2025.1 (RST is shipped):
  python scripts/scan_docs.py tree --path "<ECU_TEST_HOME>\\Help\\APIDoc\\_sources" --depth 3
  python scripts/scan_docs.py search --path "<ECU_TEST_HOME>\\Help\\APIDoc\\_sources" --query "deprecated" --glob "*.rst.txt"

  # >=2025.2 (no _sources, HTML only):
  python scripts/scan_docs.py search --path "<ECU_TEST_HOME>\\Help\\api" --query "AnalysisJobApi" --glob "*.html"
  python scripts/scan_docs.py search --path "<ECU_TEST_HOME>\\Help\\trcp" --query "Threshold" --glob "*.html"

  # Pin a version from .env (ECU_TEST_<version>_HOME):
  python scripts/scan_docs.py --version 2025.4 tree --depth 2
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Iterable

from env import get_ecu_test_home, load_dotenv


def _iter_entries(path: Path, dirs_only: bool) -> list[Path]:
    try:
        entries = list(path.iterdir())
    except (OSError, PermissionError):
        return []
    entries.sort(key=lambda p: (not p.is_dir(), p.name.lower()))
    if dirs_only:
        entries = [p for p in entries if p.is_dir()]
    return entries


def _build_tree(
    root: Path,
    max_depth: int,
    max_entries: int,
    dirs_only: bool,
) -> list[str]:
    lines: list[str] = [str(root)]

    def walk(path: Path, prefix: str, depth: int) -> None:
        if max_depth >= 0 and depth > max_depth:
            return
        entries = _iter_entries(path, dirs_only)
        truncated = False
        if max_entries > 0 and len(entries) > max_entries:
            entries = entries[:max_entries]
            truncated = True

        for idx, entry in enumerate(entries):
            is_last = idx == len(entries) - 1 and not truncated
            branch = "`-- " if is_last else "+-- "
            lines.append(f"{prefix}{branch}{entry.name}")
            if entry.is_dir():
                extension = "    " if is_last else "|   "
                walk(entry, prefix + extension, depth + 1)

        if truncated:
            lines.append(f"{prefix}`-- ... ({len(_iter_entries(path, dirs_only)) - max_entries} more entries)")

    walk(root, "", 0)
    return lines


def _write_output(lines: Iterable[str], output: str | None) -> None:
    text = "\n".join(lines)
    if output:
        Path(output).write_text(text, encoding="utf-8")
    else:
        print(text)


def _rg_available() -> bool:
    return shutil.which("rg") is not None


def _search_with_rg(query: str, root: Path, globs: list[str], case_sensitive: bool) -> int:
    args = ["rg", "--line-number", "--no-heading"]
    if not case_sensitive:
        args.append("-i")
    for g in globs:
        args.extend(["-g", g])
    args.extend([query, str(root)])
    proc = subprocess.run(args, text=True)
    return proc.returncode


def _search_fallback(query: str, root: Path, globs: list[str], case_sensitive: bool, max_results: int) -> int:
    flags = 0 if case_sensitive else re.IGNORECASE
    pattern = re.compile(query, flags)

    def match_glob(path: Path) -> bool:
        if not globs:
            return True
        return any(path.match(g) for g in globs)

    hits = 0
    for file in root.rglob("*"):
        if not file.is_file():
            continue
        if not match_glob(file):
            continue
        try:
            with file.open("r", encoding="utf-8", errors="ignore") as f:
                for line_no, line in enumerate(f, 1):
                    if pattern.search(line):
                        print(f"{file}:{line_no}:{line.rstrip()}")
                        hits += 1
                        if max_results > 0 and hits >= max_results:
                            return 0
        except (OSError, UnicodeDecodeError):
            continue
    return 0 if hits else 1


def main() -> int:
    load_dotenv()
    parser = argparse.ArgumentParser(description="ecu.test doc scanner")
    parser.add_argument(
        "--version",
        help="ecu.test version to use (e.g. 2025.4). Resolved via ECU_TEST_<version>_HOME in .env",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    tree_parser = subparsers.add_parser("tree", help="Print a directory tree")
    tree_parser.add_argument("--path", help="Root path to scan (default: ECU_TEST_HOME or latest ECU_TEST_<version>_HOME)")
    tree_parser.add_argument("--depth", type=int, default=3, help="Max depth (0=root only)")
    tree_parser.add_argument("--max-entries", type=int, default=200, help="Max entries per directory")
    tree_parser.add_argument("--dirs-only", action="store_true", help="List directories only")
    tree_parser.add_argument("--output", help="Write output to a file")

    search_parser = subparsers.add_parser("search", help="Search for a query in files")
    search_parser.add_argument("--path", help="Root path to search (default: ECU_TEST_HOME or latest ECU_TEST_<version>_HOME)")
    search_parser.add_argument("--query", required=True, help="Regex or literal query")
    search_parser.add_argument("--glob", action="append", default=[], help="Glob filter (repeatable)")
    search_parser.add_argument("--case-sensitive", action="store_true", help="Case-sensitive search")
    search_parser.add_argument("--max-results", type=int, default=200, help="Stop after N hits (fallback mode)")

    args = parser.parse_args()
    if not getattr(args, "path", None):
        args.path = get_ecu_test_home(args.version)
    root = Path(args.path)
    if not root.exists():
        print(f"Path not found: {root}", file=sys.stderr)
        return 2

    if args.command == "tree":
        lines = _build_tree(root, args.depth, args.max_entries, args.dirs_only)
        _write_output(lines, args.output)
        return 0

    if args.command == "search":
        if _rg_available():
            return _search_with_rg(args.query, root, args.glob, args.case_sensitive)
        return _search_fallback(args.query, root, args.glob, args.case_sensitive, args.max_results)

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
