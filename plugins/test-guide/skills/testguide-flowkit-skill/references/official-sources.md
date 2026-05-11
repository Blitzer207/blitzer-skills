# Official Source Index

Use this index to route flow.kit questions to files relative to this skill directory.

## Repository Contract

- Numeric folders in the project root are flow bundles.
- `flow-bundle-windows` in the project root is the official template bundle.
- Official Markdown docs are copied into this skill under `references\official-docs\docs-md`.
- Custom files in each bundle are normally:
  - `flow_definition.py`
  - `test_user_code.py`
  - `image.png`

## Official Documentation

| Topic | Path |
|---|---|
| Docs entrypoint | `references\official-docs\docs-md\index.md` |
| Concepts and block state | `references\official-docs\docs-md\introduction.md` |
| Flow definition syntax | `references\official-docs\docs-md\how_to_build_a_flow_definition.md` |
| Validate/execute/visualize | `references\official-docs\docs-md\validate_execute_visualize.md` |
| Python environment | `references\official-docs\docs-md\python_environment.md` |
| Proxy configuration | `references\official-docs\docs-md\proxy.md` |
| Retries configuration | `references\official-docs\docs-md\retries.md` |

## Block Documentation

| Block family | Path |
|---|---|
| control_flow | `references\official-docs\docs-md\Block documentation\flow_kit.library.control_flow.md` |
| ecu_test | `references\official-docs\docs-md\Block documentation\flow_kit.library.ecu_test.md` |
| environment | `references\official-docs\docs-md\Block documentation\flow_kit.library.environment.md` |
| file_operation | `references\official-docs\docs-md\Block documentation\flow_kit.library.file_operation.md` |
| test_guide | `references\official-docs\docs-md\Block documentation\test_guide\index.md` |
| tools | `references\official-docs\docs-md\Block documentation\tools\*.md` |

## API Stubs

Prefer `.pyi` stubs for exact imports, constructor signatures, class names, parameter constants, and result types.

| API area | Path |
|---|---|
| flow core | `..\..\..\flow-bundle-windows\flow_kit\core\**\*.pyi` |
| block library | `..\..\..\flow-bundle-windows\flow_kit\library\**\*.pyi` |
| tool helpers | `..\..\..\flow-bundle-windows\flow_kit\tools\**\*.pyi` |
| third-party/runtime stubs | `..\..\..\flow-bundle-windows\site-packages\**\*.pyi` |

## Snippets And Examples

| Resource | Path |
|---|---|
| Skill-local snippet copy | `references\flow-kit-snippets.code-snippets` |
| Skill-local condensed flow guide | `references\how_to_build_a_flow_definition.md` |
| Skill-local BatchProcessing copy | `examples\batch_processing_usage.py` |
| Skill-local official docs copy | `references\official-docs\docs-md\**\*.md` |

## Validation Modes

All modes must run in the target bundle directory with that bundle's interpreter.

| Mode | Command |
|---|---|
| validate | `.\interpreter\python.exe .\main.py --validate --validate-runs-unittests` |
| visualize | `.\interpreter\python.exe .\main.py --visualize` |
| execute | `.\interpreter\python.exe .\main.py --execute --validate-runs-unittests` |

Set `TT_RUN_IN_FLOW_AUTOMATION=True` for every mode. Execute mode also needs `TEST_GUIDE_URL`, `TEST_GUIDE_AUTH_KEY`, `FLOW_KIT_HIDE_TEST_GUIDE_AUTH_KEY=True`, `TEST_GUIDE_PROJECT_ID`, and `TRIGGER_PAYLOAD`.
