---
name: ecu-test-object-api
description: Use when creating, modifying, reviewing, or migrating ecu.test Object API automation that reads or writes ecu.test files through external ApiClient scripts, including projects, packages, configurations, mappings, variables, test steps, expectations, reports, trace analyses, artifacts, and version-specific 2024.3/2026.1 Object API work.
---

# ecu.test Object API

## Scope

Use this skill for object-based ecu.test file automation.

- Execution environment: external client script with ecu.test already running.
- Primary Python entry point: `from ApiClient import ApiClient`, then `api = ApiClient()`.
- Namespace: `ApiClient.*`.
- Main purpose: read, create, or modify ecu.test files such as `.pkg`, `.prj`, `.tcf`, `.tbc`, reports, mappings, variables, and test steps.
- Supported target versions: `ecu.test 2024.3` and `ecu.test 2026.1`.

Do not use Object API as the primary API for executing test cases. For execution control, use REST API or COM API. For ecu.test-internal scripts, use the internal API skill unless the user explicitly asks for `api.ObjectApi` and the Object API docs confirm the pattern.

## Supported ecu.test Versions

- 2024.3: use references under `references/2024.3/general_api/...`.
- 2026.1: use references under `references/2026.1/general_api/...`.
- Default version: `2026.1` when the user does not specify a version.

## Version Routing

Always identify the target version before generating or changing code.

1. If the user explicitly names `2024.3`, use only the 2024.3 Object API docs for generated code.
2. If the user explicitly names `2026.1`, use only the 2026.1 Object API docs for generated code.
3. If the user does not specify a version, default to `2026.1` and state that default in the response.
4. For migration or downgrade tasks, read both versions: first the source version, then the target version.
5. If a method name, constructor, property accessor, argument default, return type, object class, or file save/open workflow is uncertain, check the target-version docs before using it.
6. Label generated or modified code as applying to `ecu.test 2024.3` or `ecu.test 2026.1`.

Similarity between 2024.3 and 2026.1 is not a compatibility guarantee. Do not infer compatibility from memory.

## Bundled Authoritative Docs

Read these files from this skill directory. They are copied into the skill and are the source of truth for Object API work.

| Version | Start here |
|---|---|
| 2024.3 | `references/2024.3/general_api/objectApi.md` |
| 2024.3 | `references/2024.3/general_api/objectApiExamples.md` |
| 2026.1 | `references/2026.1/general_api/objectApi.md` |
| 2026.1 | `references/2026.1/general_api/objectApiExamples.md` |

2024.3 Object API is mostly documented through top-level `*Api.md` pages. 2026.1 includes the same top-level pages plus many per-object subpages under directories such as `PackageApi/`, `TestStepApi/`, `ConfigurationApi/`, `MappingApi/`, and `TraceAnalysisApi/`. Do not load all 2026.1 subpages at once; read the top-level API page first, then the specific object subpages named or linked by that page.

## Required Workflow

For new scripts:

1. Determine the target version. Default to `2026.1` if unspecified.
2. Read the target version's `objectApi.md`.
3. Read `objectApiExamples.md` if the task resembles creating packages, mappings, variables, expressions, or test steps from scratch.
4. Identify the involved API areas and read their top-level `*Api.md` files.
5. For 2026.1, follow links into matching subdirectories only for the concrete object types being created or edited.
6. Generate code using only APIs confirmed in the target version.

For migrations:

1. Identify the direction: `2024.3 -> 2026.1` or `2026.1 -> 2024.3`.
2. Read the source version's `objectApi.md` and relevant `*Api.md` files.
3. Read the target version's `objectApi.md` and relevant `*Api.md` files.
4. For 2026.1 source or target work, inspect relevant subpages for object-specific signatures.
5. Preserve the user's file-processing logic and update API calls, imports, object constructors, property accessors, default arguments, and save/open behavior as needed.
6. In the answer, include source version, target version, key docs checked, and a short modification summary.

## Demand Keyword Routing

Use this table before reading broad Object API references. Match the user's concrete noun, object name, file type, or operation to the smallest likely API area, then read the matching versioned files.

| User mentions | Read first |
|---|---|
| `ApiClient`, client setup, connection, application version, Java client, .NET client | `objectApi.md` |
| example package generation, create package from scratch, sample script | `objectApiExamples.md`, then the specific API pages used by the example |
| `.pkg`, package, package section, test case file, package save/open | `PackageApi.md` |
| test step, `Ts*`, wait, read, write, check, block, trace step, append step | `TestStepApi.md`; for 2026.1 search `TestStepApi/*.md` |
| variable, numeric variable, initial value, record variable, package variable | `VariableApi.md`; use `ecu-test-data-structures` for complex value shapes |
| mapping, model mapping, bus signal mapping, reference name, `checkTarget`, global mapping | `MappingApi.md`, `GlobalMappingApi.md` |
| expectation, expression, tolerance, comparison, check condition | `ExpectationApi.md`, `ExpressionApi.md` |
| `.tcf`, test configuration, platform, model, tool, port, model access | `ConfigurationApi.md`; for 2026.1 search `ConfigurationApi/*.md` |
| `.prj`, project, test suite, package reference, TMS ID on project/package | `ProjectApi.md`, then `PackageApi.md` if package metadata is changed |
| component, component configuration, component port | `ComponentApi.md` |
| parameter, parameter set, parameter value | `ParameterApi.md` |
| report, report filter, result file, verdict data | `ReportApi.md`, `ReportFilterApi.md` |
| signal, signal description, signal recording, symbol | `SignalApi.md`, `SignalDescriptionApi.md`, `SignalRecordingApi.md`, `SymbolApi.md` |
| trace analysis, trace file, trace step template | `TraceAnalysisApi.md`, `TraceFileApi.md`, `TraceStepTemplateApi.md` |
| analysis job, artifact | `AnalysisJobApi.md`, `ArtifactApi.md` |
| multimedia, image/audio/video object, touch input | `MultimediaApi.md`, `TouchInputApi.md` |
| workspace, settings | `WorkspaceApi.md`, `SettingsApi.md` |
| relation, linked object, dependency between objects | `RelationApi.md` |
| migration helper in 2024.3 | `references/2024.3/general_api/MigrationApi.md` |

## API Area Selection

| User need | Read first |
|---|---|
| Client setup, `ApiClient()`, Java or .NET client notes, API entry points | `objectApi.md` |
| Full examples for creating packages, variables, mappings, expressions, and test steps | `objectApiExamples.md` |
| Create/open/save packages, package structure, sections, local mappings | `PackageApi.md` |
| Create or edit test steps, test step blocks, waits, reads, writes, trace steps | `TestStepApi.md` and in 2026.1 matching `TestStepApi/*.md` |
| Variables, initial values, recording, package variable types | `VariableApi.md`; use `ecu-test-data-structures` for complex values |
| Mappings, model mappings, bus signal mappings, reference names | `MappingApi.md` and `GlobalMappingApi.md` |
| Expectations and expressions for read/check steps | `ExpectationApi.md` and `ExpressionApi.md` |
| Test configurations, TCF files, platforms, models, tools, ports | `ConfigurationApi.md`; in 2026.1 follow `ConfigurationApi/*.md` |
| Projects, test suites, package references, project-level metadata | `ProjectApi.md` |
| Components and component configurations | `ComponentApi.md` |
| Parameters and parameter sets | `ParameterApi.md` |
| Reports and report filters | `ReportApi.md` and `ReportFilterApi.md` |
| Signals, signal descriptions, recordings, symbols | `SignalApi.md`, `SignalDescriptionApi.md`, `SignalRecordingApi.md`, `SymbolApi.md` |
| Trace analyses, trace files, trace step templates | `TraceAnalysisApi.md`, `TraceFileApi.md`, `TraceStepTemplateApi.md` |
| Analysis jobs and artifacts | `AnalysisJobApi.md` and `ArtifactApi.md` |
| Multimedia and touch input objects | `MultimediaApi.md` and `TouchInputApi.md` |
| Workspace and settings operations | `WorkspaceApi.md` and `SettingsApi.md` |
| Relations between objects | `RelationApi.md` |
| 2024.3 migration helper API | `references/2024.3/general_api/MigrationApi.md`; no corresponding top-level 2026.1 file is bundled |

## 2026.1 Subpage Rule

For 2026.1, many top-level API pages are indexes into object-specific files. When a task names or implies a concrete object class, read both:

- `references/2026.1/general_api/<Area>Api.md`
- `references/2026.1/general_api/<Area>Api/<ObjectName>.md`

Examples:

- For a wait test step, start with `TestStepApi.md`, then search `references/2026.1/general_api/TestStepApi/*.md` for `TsWait`.
- For package variables, start with `VariableApi.md`, then search `references/2026.1/general_api/VariableApi/*.md` for the variable class.
- For model or tool configuration edits, start with `ConfigurationApi.md`, then search `references/2026.1/general_api/ConfigurationApi/*.md` for the platform, model, port, or tool object.

## Implementation Checks

Before finalizing Object API code, verify these against the target-version docs:

- `PYTHONPATH` or runtime setup points to the target ecu.test installation's `Templates\ApiClient`.
- ecu.test is expected to be running before the external client script connects.
- Imports and client construction match the target language: Python `ApiClient`, Java client JAR, or .NET `ApiClient.dll`.
- File paths, workspace-relative paths, and escaping are correct for the generated language.
- Objects are created through the documented API entry point rather than by guessing class constructors.
- Mutated files are explicitly saved with the documented `Save(...)` pattern.
- Mapping creation uses documented `checkTarget` behavior, especially when no matching model is loaded.
- Test step creation, block nesting, expectations, and expression strings use target-version methods.
- 2024.3 code does not use 2026.1-only object subpage APIs without checking 2024.3 docs.
- Generated code states whether it targets `ecu.test 2024.3` or `ecu.test 2026.1`.

## Search Hints

Use targeted searches before loading large files:

```powershell
Select-String -Path 'references\2026.1\general_api\objectApi.md' -Pattern 'ApiClient|GetApplicationVersion|PackageApi|ConfigurationApi|TestStepApi'
Select-String -Path 'references\2026.1\general_api\objectApiExamples.md' -Pattern 'CreatePackage|CreateTs|Create.*Variable|Create.*MappingItem|Save'
Select-String -Path 'references\2026.1\general_api\TestStepApi.md','references\2026.1\general_api\TestStepApi\*.md' -Pattern 'TsWait|TsRead|TsWrite|TsBlock|SetDelay|SetExpectation'
Select-String -Path 'references\2026.1\general_api\ConfigurationApi.md','references\2026.1\general_api\ConfigurationApi\*.md' -Pattern 'OpenTestConfiguration|Platform|ModelAccess|SetFile|Save'
Select-String -Path 'references\2024.3\general_api\*.md' -Pattern 'CreatePackage|OpenPackage|CreateTsRead|CreateTsWait|CreateModelMappingItem'
```

Adjust the version path and API area to match the requested target.

## Common Mistakes

- Defaulting silently. If no version is specified, state that `2026.1` was used.
- Migrating from memory. Read both source and target docs.
- Using Object API to execute tests instead of using REST or COM for execution control.
- Mixing external `ApiClient` scripts with internal User Utility or internal API imports.
- Creating objects through guessed constructors instead of documented `api.<Area>Api.Create...` methods.
- Forgetting to call `Save(...)` after modifying `.pkg`, `.prj`, `.tcf`, or related files.
- Loading every 2026.1 subpage before narrowing the task.
- Assuming 2024.3 has the same object subpage granularity as 2026.1.

## Related Skills

- `ecu-test-rest-api`: use when the user wants HTTP control or test execution.
- `ecu-test-com-api`: use when the user wants COM automation or external execution control.
- `ecu-test-data-structures`: use when Object API values involve complex variables, bus, diagnostics, media, or DLT structures.
- `ecu-test-test-management-api`: use when Object API code is part of a User Test Management adapter.
- `ecu-test-user-utility-api`: use for internal User Utility scripts; they are not external Object API scripts.
- `ecu-test-internal-api`: use for broader internal ecu.test scripting.
