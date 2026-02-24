# ecu-test (multi-version, RST-first when available)

Local ecu.test documentation knowledge base for API and feature lookups.

This repository provides the skill instructions plus helper scripts. It does not include any vendor docs; it expects a local ecu.test installation (2024.3+ including 2025.x). You can pin a specific version via `ECU_TEST_HOME` (`.env` or environment variable).

## Quick start
- Install this skill into your tools' skills folder (Claude Code / Codex / Cursor). You can either:
  - Copy the `ecutest-api-skill` folder into your skills directory, or
  - From your skills folder, run:
    - `git clone https://github.com/Blitzer207/ecutest-api-skill.git`
- Optional: create/update `.env` and set one or more of:
  - `ECU_TEST_2024_3_HOME=...`
  - `ECU_TEST_2025_4_HOME=...`
  - (optional override) `ECU_TEST_HOME=...`
- Search docs by keyword (outputs local RST paths by default):
  - `python scripts/search_api.py --version 2025.4 --query AnalysisJobApi`
  - `python scripts/search_api.py --version 2025.4 --docset traceanalysis --query templates`
  - `python scripts/search_api.py --version 2025.4 --docset tracestep --query Threshold`
- Run generic text searches/trees:
  - `python scripts/scan_docs.py --version 2025.4 tree --depth 2`
  - `python scripts/scan_docs.py --version 2025.4 search --path "C:\\Program Files\\ecu.test 2025.4\\Help\\api" --query "AnalysisJobApi" --glob "*.html"`

## Repo layout
- `SKILL.md`: primary skill instructions
- `references/`: living docs (e.g. coding standards) that evolve with team experience
- `scripts/`: helper scripts for searching and scanning docs

## Requirements
- Python 3.x
- ecu.test installed locally
