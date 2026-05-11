---
name: ecu-test-com-api
description: Use when creating, modifying, reviewing, or migrating external ecu.test COM automation, including COMApplication_ET, opening projects/packages/configurations, starting ecu.test, executing packages or projects, waiting for test execution, reading reports or results, C# COM examples, Excel/VBA COM examples, and version-specific 2024.3/2026.1 COM API work.
---

# ecu.test COM API

## Scope

Use this skill for external programs that control a running ecu.test instance through COM.

- Execution environment: external Windows COM client. ecu.test must be installed and started or startable through COM.
- Namespace: `tts.core.api.comApi.*`.
- Main entry point: `COMApplication_ET`.
- Typical clients: C#, VBA/Excel, and other COM-capable Windows automation environments.
- Supported target versions: `ecu.test 2024.3` and `ecu.test 2026.1`.

Do not use this skill for REST HTTP control, external Object API file editing, or internal ecu.test Python code. Use the corresponding ecu.test API skill for those environments.

## Supported ecu.test Versions

- 2024.3: use references under `references/2024.3/...`.
- 2026.1: use references under `references/2026.1/...`.
- Default version: `2026.1` when the user does not specify a version.

## Version Routing

Always identify the target version before generating or changing code.

1. If the user explicitly names `2024.3`, use only the 2024.3 COM docs and examples for generated code.
2. If the user explicitly names `2026.1`, use only the 2026.1 COM docs and examples for generated code.
3. If the user does not specify a version, default to `2026.1` and state that default in the response.
4. For migration or downgrade tasks, read both versions: first the source version, then the target version.
5. If a COM class, method, property, argument, return value, wait state, or execution workflow is uncertain, check the target-version docs before using it.
6. Label generated or modified code as applying to `ecu.test 2024.3` or `ecu.test 2026.1`.

Similarity between 2024.3 and 2026.1 is not a compatibility guarantee. Do not infer compatibility from memory.

## Bundled Authoritative Docs

Read these files from this skill directory. They are copied into the skill and are the source of truth for this skill.

| Version | Required docs and examples |
|---|---|
| 2024.3 | `references/2024.3/general_api/com-api.md` |
| 2024.3 | `references/2024.3/ExampleCOM/ECU-TEST_SmallExample.cs` |
| 2024.3 | `references/2024.3/ExampleCOM/ECU-TEST_LargerExample.cs` |
| 2024.3 | `references/2024.3/ExampleCOM/ECU-TEST_Demo.xlsm` |
| 2026.1 | `references/2026.1/general_api/com-api.md` |
| 2026.1 | `references/2026.1/ExampleCOM/ECU-TEST_SmallExample.cs` |
| 2026.1 | `references/2026.1/ExampleCOM/ECU-TEST_LargerExample.cs` |
| 2026.1 | `references/2026.1/ExampleCOM/ECU-TEST_Demo.xlsm` |

For code generation, prefer the `.cs` examples for C# structure. The `.xlsm` file is bundled as an official example artifact but does not need to be read unless the task specifically involves Excel/VBA.

## Required Workflow

For new COM automation:

1. Determine the target version. Default to `2026.1` if unspecified.
2. Read the target version's `com-api.md`.
3. Read the matching example source for the requested client language or workflow.
4. Confirm the COM class, method names, polling/wait pattern, and result handling in the target docs.
5. Generate code using only APIs confirmed in the target version.

For migrations:

1. Identify the direction: `2024.3 -> 2026.1` or `2026.1 -> 2024.3`.
2. Read the source version's `com-api.md` and relevant example.
3. Read the target version's `com-api.md` and relevant example.
4. Preserve business logic and update COM object creation, method calls, wait loops, result handling, and close/quit behavior.
5. In the answer, include source version, target version, key docs checked, and a short modification summary.

## Demand Keyword Routing

Use this table before reading broad COM references.

| User mentions | Search first in `com-api.md` |
|---|---|
| start ecu.test, connect, quit, exit, idle, version, settings | `COMApplication_ET`, `Start`, `RunApplication`, `WaitForIdle`, `GetVersion`, `Quit`, `Exit` |
| open or close `.pkg`, package list, package variables | `OpenPackage`, `ClosePackage`, `COMPackage`, `COMPackages`, `COMVariable` |
| open or close `.prj`, project packages, project checks | `OpenProject`, `CloseProject`, `COMProject`, `COMProjects` |
| load TBC or TCF, global constants, report base folder | `OpenTestbenchConfiguration`, `OpenTestConfiguration`, `COMTestbenchConfiguration`, `COMTestConfiguration` |
| execute package, execute project, archive execution | `COMTestEnvironment`, `ExecutePackage`, `ExecuteProject`, `ExecuteProjectArchive` |
| execution state, result, abort, report DB, wait completion | `COMTestExecutionInfo`, `WaitForTestexecutionCompletion`, `GetState`, `GetResult`, `Abort` |
| analysis job, analysis result, merge reports | `COMAnalysisEnvironment`, `COMAnalysisExecutionInfo`, `ExecuteJob`, `MergeJobReports` |
| caches, A2L/bus/model/service cache | `COMCache`, `COMCaches` |
| keyword catalog, project, variant | `COMKeywordCatalog` |
| test management through COM | `GetTestManagementModule`; use `ecu-test-test-management-api` for adapter modules |
| Object API Python path from COM | `GetObjectApiPythonPath`; use `ecu-test-object-api` for Object API calls |
| C# examples | `ExampleCOM/ECU-TEST_SmallExample.cs`, then `ECU-TEST_LargerExample.cs` |
| Excel or VBA example | `ExampleCOM/ECU-TEST_Demo.xlsm` |

## Implementation Checks

Before finalizing COM code, verify these against the target-version docs/examples:

- The code is an external Windows COM client, not an internal ecu.test Python script.
- ecu.test startup/connect behavior is explicit: start application, connect to an existing instance, or assume it is already running.
- Long-running operations use the documented execution info or wait methods.
- Tests are not assumed complete immediately after `ExecutePackage` or `ExecuteProject`.
- Opened packages/projects/configurations are closed or the application is quit only when that matches the user's workflow.
- COM method names and property capitalization match the target version.
- Generated code states whether it targets `ecu.test 2024.3` or `ecu.test 2026.1`.

## Search Hints

```powershell
Select-String -Path 'references\2026.1\general_api\com-api.md' -Pattern 'COMApplication_ET|Start|RunApplication|WaitForIdle|Quit'
Select-String -Path 'references\2026.1\general_api\com-api.md' -Pattern 'ExecutePackage|ExecuteProject|COMTestExecutionInfo|WaitForTestexecutionCompletion|GetResult'
Select-String -Path 'references\2026.1\ExampleCOM\*.cs' -Pattern 'COMApplication|Execute|Wait|GetResult|OpenPackage|OpenProject'
Select-String -Path 'references\2024.3\general_api\com-api.md' -Pattern 'COMApplication_ET|COMTestEnvironment|COMAnalysisEnvironment|GetObjectApiPythonPath'
```

Adjust the version path to match the requested target.

## Common Mistakes

- Defaulting silently. If no version is specified, state that `2026.1` was used.
- Migrating from memory. Read both source and target docs.
- Using COM patterns for Linux. Use REST API for cross-platform remote control.
- Treating execution start as execution completion without waiting for execution info.
- Mixing external COM automation with internal `tts.core.api.internalApi.*` code.
- Using Object API for execution control instead of COM or REST.

## Related Skills

- `ecu-test-rest-api`: use for HTTP/OpenAPI execution control or Linux-compatible remote control.
- `ecu-test-object-api`: use for external object-based file creation or mutation through `ApiClient`.
- `ecu-test-internal-api`: use for internal ecu.test Python APIs.
- `ecu-test-report-api`: use for detailed report parser work after COM execution creates report data.
