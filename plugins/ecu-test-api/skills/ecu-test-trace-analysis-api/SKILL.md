---
name: ecu-test-trace-analysis-api
description: Use when creating, modifying, reviewing, or migrating ecu.test Python trace analysis step templates, including NumPy array-based templates, event-based templates, stream-based templates, custom parameter GUIs, trace synchronization, signal filtering helpers, available Python libraries, and version-specific 2024.3/2026.1 Trace Analysis API work.
---

# ecu.test Trace Analysis API

## Scope

Use this skill for Python-based trace step templates used in ecu.test trace analyses.

- Execution environment: internal ecu.test trace analysis template execution.
- Main purpose: create custom trace step templates and related parameter GUI or trace synchronization logic.
- Template families: array-based NumPy, event-based, and stream-based trace steps.
- Supported target versions: `ecu.test 2024.3` and `ecu.test 2026.1`.

Do not use this skill for external Object API trace-analysis file editing, REST/COM execution control, or generic internal API code unless the task specifically involves trace analysis template APIs.

## Supported ecu.test Versions

- 2024.3: use references under `references/2024.3/TraceanalysisAPI/...`.
- 2026.1: use references under `references/2026.1/TraceAnalysisAPI/...`.
- Default version: `2026.1` when the user does not specify a version.

Note the directory casing difference: 2024.3 uses `TraceanalysisAPI`; 2026.1 uses `TraceAnalysisAPI`.

## Version Routing

Always identify the target version before generating or changing code.

1. If the user explicitly names `2024.3`, use only the 2024.3 Trace Analysis docs for generated code.
2. If the user explicitly names `2026.1`, use only the 2026.1 Trace Analysis docs for generated code.
3. If the user does not specify a version, default to `2026.1` and state that default in the response.
4. For migration or downgrade tasks, read both versions: first the source version, then the target version.
5. If a base class, hook signature, signal container, parameter definition, report method, decorator, library, or synchronization API is uncertain, check the target-version docs before using it.
6. Label generated or modified code as applying to `ecu.test 2024.3` or `ecu.test 2026.1`.

Similarity between 2024.3 and 2026.1 is not a compatibility guarantee. Do not infer compatibility from memory. `custom_trace_synchronization.md` is bundled only for 2026.1 in this plan.

## Bundled Authoritative Docs

| Version | Required docs |
|---|---|
| 2024.3 | `references/2024.3/TraceanalysisAPI/index.md` |
| 2024.3 | `references/2024.3/TraceanalysisAPI/array_based_templates.md` |
| 2024.3 | `references/2024.3/TraceanalysisAPI/event_based_templates.md` |
| 2024.3 | `references/2024.3/TraceanalysisAPI/stream_based_templates.md` |
| 2024.3 | `references/2024.3/TraceanalysisAPI/custom_param_gui.md` |
| 2024.3 | `references/2024.3/TraceanalysisAPI/python_libraries.md` |
| 2026.1 | `references/2026.1/TraceAnalysisAPI/index.md` |
| 2026.1 | `references/2026.1/TraceAnalysisAPI/array_based_templates.md` |
| 2026.1 | `references/2026.1/TraceAnalysisAPI/event_based_templates.md` |
| 2026.1 | `references/2026.1/TraceAnalysisAPI/stream_based_templates.md` |
| 2026.1 | `references/2026.1/TraceAnalysisAPI/custom_param_gui.md` |
| 2026.1 | `references/2026.1/TraceAnalysisAPI/custom_trace_synchronization.md` |
| 2026.1 | `references/2026.1/TraceAnalysisAPI/python_libraries.md` |

## Required Workflow

For new trace step templates:

1. Determine the target version. Default to `2026.1` if unspecified.
2. Read the target version's `index.md`.
3. Choose the template family from the user's data model: array-based, event-based, or stream-based.
4. Read the selected template family doc and any required parameter GUI or library doc.
5. Generate code using only APIs confirmed in the target version.

For migrations:

1. Identify the direction: `2024.3 -> 2026.1` or `2026.1 -> 2024.3`.
2. Read the source version docs for the current template family.
3. Read the target version docs for the target template family.
4. Preserve analysis logic and update base classes, hook signatures, signal/parameter definitions, report usage, decorators, GUI integration, and library assumptions.
5. For 2026.1 trace synchronization migration, read `custom_trace_synchronization.md`; for 2024.3, do not claim that doc exists unless user provides it.
6. In the answer, include source version, target version, key docs checked, and a short modification summary.

## Demand Keyword Routing

| User mentions | Read first |
|---|---|
| overview, which trace template type | `index.md` |
| NumPy, array, vectorized signal processing, sample arrays | `array_based_templates.md` |
| event, signal event, hold, event range, discrete signal changes | `event_based_templates.md` |
| stream, streaming trace data, incremental processing | `stream_based_templates.md` |
| custom parameter panel, parameter GUI, TraceStepDataAPI | `custom_param_gui.md` |
| custom synchronization, align traces, synchronization signals | 2026.1: `custom_trace_synchronization.md`; 2024.3: not bundled |
| NumPy, matplotlib, filters, decorators, allowed libraries | `python_libraries.md` |
| report output, report table, verdict text | selected template family doc, search `Report` and `ReportTable` |
| signal definition, parameter definition, recording info | selected template family doc, search `SignalDefinition`, `ParameterDefinition`, `RecordingInfo` |

## Implementation Checks

Before finalizing trace analysis code, verify these against the target-version docs:

- The selected template family matches the user's processing model.
- Base class names and hook signatures are copied from the target version.
- Signal and parameter definitions match the target version.
- Report and report table usage matches the selected template family.
- Custom GUI code uses the target-version `ParameterPanel` and `TraceStepDataAPI` contracts.
- Available Python libraries and decorators are confirmed in `python_libraries.md`.
- 2026.1-only custom synchronization is not used for 2024.3 without documentation.
- Complex bus or diagnostics data shapes are checked with `ecu-test-data-structures`.
- Generated code states whether it targets `ecu.test 2024.3` or `ecu.test 2026.1`.

## Search Hints

```powershell
Select-String -Path 'references\2026.1\TraceAnalysisAPI\array_based_templates.md' -Pattern 'NumpyBasedTraceStep|SignalDefinition|ParameterDefinition|Report|ReportTable'
Select-String -Path 'references\2026.1\TraceAnalysisAPI\event_based_templates.md' -Pattern 'DataContainer|SignalEvent|Hold|Parameters|Range|Report'
Select-String -Path 'references\2026.1\TraceAnalysisAPI\stream_based_templates.md' -Pattern 'DataContainer|Parameters|RecordingInfo|Range|Report'
Select-String -Path 'references\2026.1\TraceAnalysisAPI\custom_param_gui.md' -Pattern 'ParameterPanel|TraceStepDataAPI'
Select-String -Path 'references\2024.3\TraceanalysisAPI\*.md' -Pattern 'TraceStep|SignalDefinition|ParameterDefinition|Report|decorator|numpy'
```

Adjust the version path to match the requested target.

## Common Mistakes

- Defaulting silently. If no version is specified, state that `2026.1` was used.
- Migrating from memory. Read both source and target docs.
- Confusing trace analysis templates with Object API trace-analysis file objects.
- Using array-based APIs for event or stream processing without checking the template family docs.
- Using 2026.1 `custom_trace_synchronization.md` patterns in 2024.3 code without target docs.
- Importing arbitrary Python libraries without checking `python_libraries.md`.

## Related Skills

- `ecu-test-data-structures`: use for bus, diagnostics, media, DLT, or trace-analysis-specific structures.
- `ecu-test-object-api`: use for external creation or editing of trace analysis files/templates.
- `ecu-test-internal-api`: use for broader internal ecu.test APIs outside trace analysis templates.
- `ecu-test-report-api`: use for parsing generated report files, not for trace template report output.
