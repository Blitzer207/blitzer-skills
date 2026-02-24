#!/usr/bin/env python
"""Minimal .env loader for local configuration."""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Dict, Optional, Tuple


def load_dotenv(path: Path | None = None) -> Dict[str, str]:
    """Load key=value pairs from .env into os.environ (non-destructive)."""
    if path is None:
        path = Path(__file__).resolve().parent.parent / ".env"
    if not path.exists():
        return {}

    values: Dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if not key:
            continue
        if (value.startswith('"') and value.endswith('"')) or (
            value.startswith("'") and value.endswith("'")
        ):
            value = value[1:-1]
        values[key] = value
        os.environ.setdefault(key, value)

    return values


_HOME_KEY_RE = re.compile(r"^ECU_TEST_(\d+)_(\d+)(?:_(\d+))?_HOME$")


def _parse_version_key(key: str) -> Optional[Tuple[int, int, int]]:
    match = _HOME_KEY_RE.match(key)
    if not match:
        return None
    major = int(match.group(1))
    minor = int(match.group(2))
    patch = int(match.group(3) or 0)
    return major, minor, patch


def _normalize_version(version: str) -> str:
    # Accept "2025.4", "2025_4", "2025-4", or "2025.4.1".
    raw = version.strip().replace("-", ".").replace("_", ".")
    parts = [p for p in raw.split(".") if p]
    if len(parts) < 2 or not all(p.isdigit() for p in parts):
        raise ValueError(f"Invalid ecu.test version: {version!r}")
    major = int(parts[0])
    minor = int(parts[1])
    patch = int(parts[2]) if len(parts) >= 3 else None
    if patch is None:
        return f"{major}_{minor}"
    return f"{major}_{minor}_{patch}"


def get_ecu_test_home(version: str | None = None) -> str:
    """Resolve ecu.test install root.

    Resolution order:
      1) If version is provided: ECU_TEST_<version>_HOME (from .env or environment)
      2) ECU_TEST_HOME (from environment)
      3) Highest ECU_TEST_<version>_HOME found in environment
    """
    load_dotenv()

    if version:
        key = f"ECU_TEST_{_normalize_version(version)}_HOME"
        home = os.environ.get(key)
        if home:
            return home
        raise KeyError(f"{key} is not set (define it in .env)")

    home = os.environ.get("ECU_TEST_HOME")
    if home:
        return home

    candidates: list[Tuple[Tuple[int, int, int], str]] = []
    for key, value in os.environ.items():
        ver = _parse_version_key(key)
        if ver and value:
            candidates.append((ver, value))
    if candidates:
        candidates.sort()
        return candidates[-1][1]

    raise RuntimeError(
        "No ecu.test home configured. Set ECU_TEST_HOME or ECU_TEST_<version>_HOME in .env."
    )
