---
name: ecu-test-internal-api
description: Use when creating, modifying, reviewing, or migrating ecu.test internal Python API code that runs inside ecu.test, including `api.` expression-control usage, `tts.core.api.internalApi.*`, current test configuration or testbench access, test environment execution info, ToolAccess, credentials, DataBrowser, services, workspace checks, and version-specific 2024.3/2026.1 internal API work.
---

# ecu.test Internal API

## Scope

Use this skill for ecu.test Internal API code that runs inside ecu.test.

- Execution environment: internal ecu.test Python execution, not an external controller script.
- Namespace: `tts.core.api.internalApi.*` and closely related internal API namespaces documented in `api.md`.
- Common entry point in expression controls, test steps, and utilities: `api.`.
- Entry point for function variables or other user code when no `api` object is injected:

```python
from tts.core.api.internalApi.Api import Api
api = Api()
```

- Supported target versions: `ecu.test 2024.3` and `ecu.test 2026.1`.

Do not use this skill for external `ApiClient`, REST, or COM automation. Use Object API, REST API, or COM API skills for external scripts and execution control. If an internal script uses `api.ObjectApi`, also use `ecu-test-object-api` to confirm Object API methods.

## Supported ecu.test Versions

- 2024.3: use references under `references/2024.3/general_api/api.md`.
- 2026.1: use references under `references/2026.1/general_api/api.md`.
- Default version: `2026.1` when the user does not specify a version.

## Version Routing

Always identify the target version before generating or changing code.

1. If the user explicitly names `2024.3`, use only the 2024.3 Internal API docs for generated code.
2. If the user explicitly names `2026.1`, use only the 2026.1 Internal API docs for generated code.
3. If the user does not specify a version, default to `2026.1` and state that default in the response.
4. For migration or downgrade tasks, read both versions: first the source version, then the target version.
5. If a method name, attribute, import path, return value, execution context, injected object, or namespace is uncertain, check the target-version docs before using it.
6. Label generated or modified code as applying to `ecu.test 2024.3` or `ecu.test 2026.1`.

Similarity between 2024.3 and 2026.1 is not a compatibility guarantee. Do not infer compatibility from memory. Some documented entry points differ by version; for example, confirm availability of items such as `ToolAccess`, `Workspace`, `TestGuideApiClient`, and credential helpers in the target-version `api.md`.

## Bundled Authoritative Docs

Read these files from this skill directory. They are copied into the skill and are the source of truth for this skill.

| Version | Required doc |
|---|---|
| 2024.3 | `references/2024.3/general_api/api.md` |
| 2026.1 | `references/2026.1/general_api/api.md` |

The bundled docs are large single-page API references. Do not read the whole file unless the task is broad. Use the routing and search hints below to jump to relevant classes, methods, and attributes.

## Required Workflow

For new internal API code:

1. Determine the target version. Default to `2026.1` if unspecified.
2. Identify whether the user code already receives injected `api` or must instantiate `Api`.
3. Search the target version's `api.md` for the relevant entry point, class, method, and attribute names.
4. Generate code using only APIs confirmed in the target version.
5. State that the code runs inside ecu.test, not from an external Python process.

For migrations:

1. Identify the direction: `2024.3 -> 2026.1` or `2026.1 -> 2024.3`.
2. Search the source version's `api.md` for the current API surface.
3. Search the target version's `api.md` for the target API surface.
4. Preserve business logic and update imports, entry point use, method names, attributes, return handling, and execution-context assumptions.
5. In the answer, include source version, target version, key docs checked, and a short modification summary.

## Demand Keyword Routing

Use this table before reading broad Internal API references. Match the user's concrete noun, object name, or operation to the smallest likely section, then search the matching versioned `api.md`.

| User mentions | Search first in `api.md` |
|---|---|
| `api.`, `Api()`, internal API entry point, ecu.test version, settings path | `API entry point`, `class Api`, `GetVersion`, `GetSetting` |
| current TCF, test configuration, bus systems, ECUs, models, global constants | `CurrentTestConfiguration`, `TestConfiguration`, `BusSystem`, `Ecu`, `Model`, `GlobalConstants` |
| current TBC, testbench, tools, ports, start/stop tool, tool status | `CurrentTestbenchConfiguration`, `TestbenchConfiguration`, `TestBench`, `TestbenchTool`, `ToolAccess` |
| execution context, current package, log folder, report DB, last result, keyword info | `TestEnvironment`, `TestExecutionInfo`, `AnalysisEnvironment`, `AnalysisExecutionInfo`, `KeywordInfo` |
| wait inside internal execution, elapsed time, report document from DB | `TestEnvironment`, `Wait`, `TimeElapsing`, `GenerateTestReportDocumentFromDB` |
| analysis jobs, trace analysis runtime, signal cache | `AnalysisEnvironment`, `AnalysisExecutionInfo`, `ClearSignalCache` |
| data browser, A2L, bus, diagnostics, logging, media, model, service, SGBD browser | `DataBrowser`, `A2lBrowser`, `BusBrowser`, `DiagBrowser`, `LoggingBrowser`, `MediaBrowser`, `ModelBrowser`, `ServiceBrowser`, `SgbdBrowser` |
| credentials, certificates, private keys, vault, secrets, seed-and-key | `Credentials API`, `Credentials`, `KeyStore`, `Secret`, `Certificate`, `PrivateKey`, `SeedAndKey` |
| multimedia, OCR, object detector, speech-to-text, text-to-speech | `Multimedia`, `MultimediaApi`, `ImageFiltersApi` |
| services, service ports, service proxy, generate service, service functions | `Service`, `ServicePort`, `ServiceProxy` |
| SCM, workspace revision, file status, repository URL | `Scm`, `GetCheckoutRevision`, `GetFileRevision`, `GetFileStatus`, `GetUrl` |
| workspace check, findings | `Workspace`, `Finding`, `Check` |
| keyword catalog, catalog project, variant | `KeywordCatalog` |
| TestGuide, test.guide execution API, execution client | `TestGuideApiClient`, `TestGuideExecutionApi` |
| test management access from internal API | `TestManagement`; use `ecu-test-test-management-api` for User TMS adapter modules |
| internal Object API access | `ObjectApi`; use `ecu-test-object-api` for object methods |
| units, quantities, unit conversion metadata | `UnitInfo` |
| math helpers | `Math` |

## Implementation Checks

Before finalizing code, verify these against the target-version docs:

- The code is meant to run inside ecu.test, or imports and instantiates `Api` only for an internal ecu.test Python context.
- If `api` is injected by the execution context, do not add unnecessary imports.
- If the code runs in function variables or other user code without injected `api`, use the documented `Api` import.
- Exact attribute capitalization is preserved, such as `CurrentTestConfiguration`, `TestEnvironment`, `Credentials`, or `DataBrowser`.
- Methods and return values are confirmed in the target version.
- 2026.1-only entry points are not used in 2024.3 code without checking 2024.3 docs.
- Internal `api.ObjectApi` usage is checked against Object API docs as well.
- Complex bus, diagnostics, media, DLT, or variable data shapes are checked with `ecu-test-data-structures`.
- Generated code states whether it targets `ecu.test 2024.3` or `ecu.test 2026.1`.

## Search Hints

Use targeted searches before loading large sections:

```powershell
Select-String -Path 'references\2026.1\general_api\api.md' -Pattern 'API entry point|class Api|GetVersion|GetSetting|CurrentTestConfiguration'
Select-String -Path 'references\2026.1\general_api\api.md' -Pattern 'TestEnvironment|TestExecutionInfo|AnalysisExecutionInfo|GetCurrentPackageFilename|LogFolder|ReportDb'
Select-String -Path 'references\2026.1\general_api\api.md' -Pattern 'TestBench|TestbenchConfiguration|ToolAccess|GetToolStatus|StartTool|GetPortJobExecutor'
Select-String -Path 'references\2026.1\general_api\api.md' -Pattern 'Credentials|CreateSecret|Certificate|PrivateKey|SeedAndKey|DiagSeedAndKey|XcpSeedAndKey'
Select-String -Path 'references\2024.3\general_api\api.md' -Pattern 'ToolAccess|Workspace|TestGuideApiClient|Credentials|ObjectApi'
```

Adjust the version path and pattern to match the requested target.

## Common Mistakes

- Defaulting silently. If no version is specified, state that `2026.1` was used.
- Migrating from memory. Read both source and target docs.
- Running internal API code as a standalone external Python script.
- Mixing `ApiClient` Object API imports into internal API code unless the user is explicitly working with external Object API.
- Assuming the injected `api` object exists in contexts where the docs require `from tts.core.api.internalApi.Api import Api`.
- Guessing class or method capitalization from related APIs.
- Using 2026.1-only entries in 2024.3 code without checking 2024.3 `api.md`.
- Treating User Test Management adapters or User Utilities as generic Internal API scripts without using their dedicated skills.

## Related Skills

- `ecu-test-object-api`: use when internal code accesses `api.ObjectApi` or when external scripts use `ApiClient`.
- `ecu-test-user-utility-api`: use for User Utility scripts built on `TsUserUtility` or `TsAXSUtility`.
- `ecu-test-test-management-api`: use for User Test Management adapter modules.
- `ecu-test-data-structures`: use when internal API values involve complex bus, diagnostics, media, DLT, or variable structures.
- `ecu-test-tools-api`: use for User Tool, Model-based Bus Port, or Tool Adapter APIs.
- `ecu-test-trace-analysis-api`: use for trace analysis Python templates.
