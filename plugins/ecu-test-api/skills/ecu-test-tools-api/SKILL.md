---
name: ecu-test-tools-api
description: Use when creating, modifying, reviewing, or migrating ecu.test Tools API code, including User Tool API, UserTool/UserPort/UserJob/UserRecorder interfaces, model-based bus port APIs, BusToModelPathResolver, Tool Adapter API in 2024.3, and version-specific 2024.3/2026.1 tools API work.
---

# ecu.test Tools API

## Scope

Use this skill for ecu.test Tools APIs.

- Execution environment: internal ecu.test tool integration code, not an external controller script.
- Covered APIs: User Tool API, Model-based Bus Port API, and 2024.3 Tool Adapter API.
- Supported target versions: `ecu.test 2024.3` and `ecu.test 2026.1`.

Do not use this skill for User Utilities, User Test Management adapters, external Object API scripts, REST/COM automation, or generic internal API work unless the task specifically involves a Tool API surface.

## Supported ecu.test Versions

- 2024.3: use references under `references/2024.3/tools/...`.
- 2026.1: use references under `references/2026.1/tools/...`.
- Default version: `2026.1` when the user does not specify a version.

## Version Routing

Always identify the target version before generating or changing code.

1. If the user explicitly names `2024.3`, use only the 2024.3 Tools docs for generated code.
2. If the user explicitly names `2026.1`, use only the 2026.1 Tools docs for generated code.
3. If the user does not specify a version, default to `2026.1` and state that default in the response.
4. For migration or downgrade tasks, read both versions: first the source version, then the target version.
5. If an interface, hook, class, method, port contract, setting, constant, or adapter feature is uncertain, check the target-version docs before using it.
6. Label generated or modified code as applying to `ecu.test 2024.3` or `ecu.test 2026.1`.

Similarity between 2024.3 and 2026.1 is not a compatibility guarantee. The plan bundles Tool Adapter API docs only for 2024.3; do not claim 2026.1 Tool Adapter support from 2024.3 docs.

## Bundled Authoritative Docs

| Version | Required docs |
|---|---|
| 2024.3 | `references/2024.3/tools/index.md` |
| 2024.3 | `references/2024.3/tools/usertool-api/usertool-api.md` |
| 2024.3 | `references/2024.3/tools/modelbasedbusport-api/modelbasedbusport-api.md` |
| 2024.3 | `references/2024.3/tools/tool-adapters/tooladapter-api.md` |
| 2026.1 | `references/2026.1/tools/index.md` |
| 2026.1 | `references/2026.1/tools/usertool-api/usertool-api.md` |
| 2026.1 | `references/2026.1/tools/modelbasedbusport-api/modelbasedbusport-api.md` |

## Required Workflow

For new Tools API code:

1. Determine the target version. Default to `2026.1` if unspecified.
2. Read the target version's `tools/index.md`.
3. Choose User Tool API, Model-based Bus Port API, or 2024.3 Tool Adapter API based on the task.
4. Read the selected API doc and confirm required interfaces, hooks, and method signatures.
5. Generate code using only APIs confirmed in the target version.

For migrations:

1. Identify the direction: `2024.3 -> 2026.1` or `2026.1 -> 2024.3`.
2. Read source and target docs for the selected Tool API surface.
3. Preserve integration logic and update interface methods, port contracts, settings, constants, and adapter-specific pieces.
4. If migrating 2024.3 Tool Adapter code to 2026.1, state that no 2026.1 Tool Adapter doc is bundled unless the repository now contains one or the user provides it.
5. In the answer, include source version, target version, key docs checked, and a short modification summary.

## Demand Keyword Routing

| User mentions | Read first |
|---|---|
| tools overview, which tool API | `tools/index.md` |
| User Tool, custom tool, `UserTool` | `usertool-api/usertool-api.md` |
| `UserPort`, `UserImagePort`, `UserTouchInput`, `UserModelPort` | `usertool-api/usertool-api.md` |
| recorder, simulation manager, tool job | `UserRecorder`, `UserSimulationManager`, `UserJob` in `usertool-api.md` |
| model-based bus port, bus-to-model path mapping | `modelbasedbusport-api/modelbasedbusport-api.md` |
| `BusToModelPathResolver`, settings, constants | `modelbasedbusport-api/modelbasedbusport-api.md` |
| Tool Adapter, adapter interface, 2024.3 adapter | 2024.3: `tool-adapters/tooladapter-api.md`; 2026.1: not bundled |
| bus, diagnostics, media, DLT value structures inside a tool | also use `ecu-test-data-structures` |

## Implementation Checks

Before finalizing Tools API code, verify these against the target-version docs:

- The requested Tool API surface is documented for the target version.
- Required interface methods and hook signatures match the target docs.
- User Tool port classes and job/recorder contracts are not guessed from names.
- Model-based bus port settings and constants are target-version confirmed.
- Tool Adapter code is not claimed for 2026.1 unless 2026.1 docs are available.
- Generated code states whether it targets `ecu.test 2024.3` or `ecu.test 2026.1`.

## Search Hints

```powershell
Select-String -Path 'references\2026.1\tools\usertool-api\usertool-api.md' -Pattern 'UserTool|UserPort|UserImagePort|UserTouchInput|UserModelPort|UserJob|UserRecorder'
Select-String -Path 'references\2026.1\tools\modelbasedbusport-api\modelbasedbusport-api.md' -Pattern 'BusToModelPathResolver|Settings|Constants|model|bus|path'
Select-String -Path 'references\2024.3\tools\tool-adapters\tooladapter-api.md' -Pattern 'ToolAdapter|adapter|interface|class|def'
Select-String -Path 'references\2024.3\tools\*.md','references\2024.3\tools\*\*.md' -Pattern 'UserTool|Model-based|ToolAdapter|BusToModelPathResolver'
```

Adjust the version path to match the requested target.

## Common Mistakes

- Defaulting silently. If no version is specified, state that `2026.1` was used.
- Migrating from memory. Read both source and target docs.
- Treating User Utilities as User Tools.
- Treating User Test Management adapters as Tool Adapters.
- Claiming 2026.1 Tool Adapter support from 2024.3-only docs.
- Using external REST/COM/Object API patterns inside Tool API code.

## Related Skills

- `ecu-test-user-utility-api`: use for User Utility scripts; they are not User Tools.
- `ecu-test-test-management-api`: use for User Test Management adapter modules.
- `ecu-test-internal-api`: use for broader internal ecu.test APIs.
- `ecu-test-data-structures`: use for complex bus, diagnostics, media, DLT, or variable structures in tools.
- `ecu-test-object-api`: use for external file/object automation.
