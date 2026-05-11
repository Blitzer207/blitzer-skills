---
name: ecu-test-report-api
description: Use when creating, modifying, reviewing, or migrating ecu.test Report API parser code, including tts.core.report.parser objects, report database paths, packages, projects, activities, artifacts, attributes, configuration data, verdict/result colors, iterating report items or comments, and version-specific 2024.3/2026.1 report parsing work.
---

# ecu.test Report API

## Scope

Use this skill for parsing ecu.test report data through the Report API.

- Execution environment: standalone report parsing or internal ecu.test use, depending on the user's script context.
- Namespace: `tts.core.report.parser.*` and related `tts.core.report.db.*` objects documented in `apireport.md`.
- Main entry point: `ReportApi`.
- Supported target versions: `ecu.test 2024.3` and `ecu.test 2026.1`.

Do not use this skill to execute tests or create reports. Use REST or COM for execution, and use this skill for reading or analyzing report output after it exists.

## Supported ecu.test Versions

- 2024.3: use `references/2024.3/general_api/apireport.md`.
- 2026.1: use `references/2026.1/general_api/apireport.md`.
- Default version: `2026.1` when the user does not specify a version.

## Version Routing

Always identify the target version before generating or changing code.

1. If the user explicitly names `2024.3`, use only the 2024.3 Report API docs for generated code.
2. If the user explicitly names `2026.1`, use only the 2026.1 Report API docs for generated code.
3. If the user does not specify a version, default to `2026.1` and state that default in the response.
4. For migration or downgrade tasks, read both versions: first the source version, then the target version.
5. If a parser object, method, iterator, database object, return value, result value, or configuration accessor is uncertain, check the target-version docs before using it.
6. Label generated or modified code as applying to `ecu.test 2024.3` or `ecu.test 2026.1`.

Similarity between 2024.3 and 2026.1 is not a compatibility guarantee. Do not infer compatibility from memory.

## Bundled Authoritative Docs

| Version | Required doc |
|---|---|
| 2024.3 | `references/2024.3/general_api/apireport.md` |
| 2026.1 | `references/2026.1/general_api/apireport.md` |

The bundled docs are large single-page references. Search for the specific object or method before reading broad sections.

## Required Workflow

For new report parsing code:

1. Determine the target version. Default to `2026.1` if unspecified.
2. Read or search the target version's `apireport.md`.
3. Identify whether the task needs top-level report metadata, package/project structure, report items, artifacts, configuration, attributes, or comments.
4. Confirm the relevant parser and database object methods in the target docs.
5. Generate code using only APIs confirmed in the target version.

For migrations:

1. Identify the direction: `2024.3 -> 2026.1` or `2026.1 -> 2024.3`.
2. Search source and target `apireport.md` for the current parser objects and methods.
3. Preserve parsing/reporting logic and update constructors, iterators, getters, object names, and return handling.
4. In the answer, include source version, target version, key docs checked, and a short modification summary.

## Demand Keyword Routing

| User mentions | Search first in `apireport.md` |
|---|---|
| open report, analyze path, report DB, report directory | `ReportApi`, `AnalysePath`, `GetDbDir`, `GetDbFile`, `GetReportDir` |
| main package, package item, package structure | `GetMainPackage`, `GetPackage`, `Package`, `IterItems` |
| project report, main project | `IsProjectReport`, `GetMainProject`, `Project` |
| root activity, report items, activities, verdicts | `GetRootActivity`, `IterItems`, `Activity`, `GetResult` |
| artifacts, attached files | `GetArtifacts`, `Artifact`, `GetFilePath`, `GetFileName` |
| configuration, TBC, TCF, tools, bus/model configuration | `GetConfiguration`, `Configuration`, `TestBenchConfiguration`, `TestConfiguration` |
| attributes, user comments | `Attribute`, `IterUserComments`, `GetValue`, `GetName` |
| result colors, source colors, templates, settings | `GetResultColor`, `GetResultBgColor`, `GetSrcColor`, `GetTemplateDir`, `GetSetting` |
| SCM info, patches | `GetPackageScmInfo`, `GetPatchInfo` |

## Implementation Checks

Before finalizing report code, verify these against the target-version docs:

- The code parses existing report data; it does not claim to execute tests.
- Report path, database path, and relative artifact paths are handled with documented methods.
- Iterators are used according to target-version docs.
- `Has...` methods are used before optional configuration or object access when documented.
- Color, verdict, and result values are not hardcoded unless the docs confirm them.
- Complex report payload objects are checked against Report API docs and, if needed, `ecu-test-data-structures`.
- Generated code states whether it targets `ecu.test 2024.3` or `ecu.test 2026.1`.

## Search Hints

```powershell
Select-String -Path 'references\2026.1\general_api\apireport.md' -Pattern 'ReportApi|AnalysePath|GetRootActivity|IterItems|GetArtifacts'
Select-String -Path 'references\2026.1\general_api\apireport.md' -Pattern 'Configuration|TestBenchConfiguration|TestConfiguration|IterTools|IterBusConfigurations'
Select-String -Path 'references\2026.1\general_api\apireport.md' -Pattern 'Artifact|Attribute|IterUserComments|GetPackageScmInfo|GetPatchInfo'
Select-String -Path 'references\2024.3\general_api\apireport.md' -Pattern 'ReportApi|Package|Project|Activity|GetResult|GetReportDir'
```

Adjust the version path to match the requested target.

## Common Mistakes

- Defaulting silently. If no version is specified, state that `2026.1` was used.
- Migrating from memory. Read both source and target docs.
- Using Report API to execute tests or generate new test results.
- Guessing report item object types instead of checking parser classes.
- Accessing optional configuration data without checking documented `Has...` methods.
- Confusing Object API report file objects with Report API parser objects.

## Related Skills

- `ecu-test-rest-api`: use for REST execution that produces report IDs or report data.
- `ecu-test-com-api`: use for COM execution that produces report data.
- `ecu-test-object-api`: use for report-related file objects in Object API.
- `ecu-test-data-structures`: use for complex bus, diagnostics, media, DLT, or variable structures inside reports.
