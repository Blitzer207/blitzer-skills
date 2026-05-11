---
name: ecu-test-user-utility-api
description: Use when creating, modifying, or migrating ecu.test User Utility Python scripts for the internal ecu.test execution environment, including TsUserUtility, TsAXSUtility, custom utility dialogs, ThreadDialog UI interactions, test case variables, utility reports, AXS keyword-style arguments and return values, or version-specific 2024.3/2026.1 user utilities.
---

# ecu.test User Utility API

## Scope

Use this skill for ecu.test user-defined Utility scripts that run inside ecu.test.

- Execution environment: internal ecu.test Python execution, not an external controller.
- Namespace: `tts.testExecution.api.*`
- Main base classes: `TsUserUtility`, `TsAXSUtility`
- Supported target versions: `ecu.test 2024.3` and `ecu.test 2026.1`

Do not use this skill for external `ApiClient`, REST, or COM automation. Use the corresponding ecu.test API skill for those environments.

## Version Routing

Always identify the target version before generating or changing code.

1. If the user explicitly names `2024.3`, use only the 2024.3 User Utility docs and examples for generated code.
2. If the user explicitly names `2026.1`, use only the 2026.1 User Utility docs and examples for generated code.
3. If the user does not specify a version, default to `2026.1` and state that default in the response.
4. For migration or downgrade tasks, read both versions: first the source version, then the target version.
5. If a method name, import path, hook signature, parameter declaration, return value, UI pattern, or helper class is uncertain, check the target-version docs before using it.
6. Label generated or modified code as applying to `ecu.test 2024.3` or `ecu.test 2026.1`.

Similarity between 2024.3 and 2026.1 is not a compatibility guarantee. Do not infer compatibility from memory.

## Bundled Authoritative Docs

Read these files from this skill directory. They are copied into the skill and are the source of truth for this skill.

| Version | Required docs |
|---|---|
| 2024.3 | `references/2024.3/user-utility/user-utility.md` |
| 2024.3 | `references/2024.3/user-utility/example-utilities.md` |
| 2026.1 | `references/2026.1/user-utility/user-utility.md` |
| 2026.1 | `references/2026.1/user-utility/example-utilities.md` |

Official examples to inspect for structure:

| Pattern | 2024.3 path | 2026.1 path |
|---|---|---|
| Small custom UI utility | `references/2024.3/ExampleUtilities/SmallExample/TsSmallExample.py` | `references/2026.1/ExampleUtilities/SmallExample/TsSmallExample.py` |
| Small custom UI dialog | `references/2024.3/ExampleUtilities/SmallExample/DlgSmallExample.py` | `references/2026.1/ExampleUtilities/SmallExample/DlgSmallExample.py` |
| Simple AXS calculation | `references/2024.3/ExampleUtilities/SimpleCalculationExample/TsSimpleCalculationExample.py` | `references/2026.1/ExampleUtilities/SimpleCalculationExample/TsSimpleCalculationExample.py` |
| Runtime dialog utility | `references/2024.3/ExampleUtilities/ShowDialogExample/TsShowDialogExample.py` | `references/2026.1/ExampleUtilities/ShowDialogExample/TsShowDialogExample.py` |
| Runtime dialog class | `references/2024.3/ExampleUtilities/ShowDialogExample/RunDialogExample.py` | `references/2026.1/ExampleUtilities/ShowDialogExample/RunDialogExample.py` |
| Linspace AXS utility | `references/2024.3/ExampleUtilities/LinspaceExample/TsLinspaceExample.py` | `references/2026.1/ExampleUtilities/LinspaceExample/TsLinspaceExample.py` |

## Required Workflow

For new utilities:

1. Determine the target version. Default to `2026.1` if unspecified.
2. Read the target version's `user-utility.md`.
3. Read the target version's `example-utilities.md`.
4. Inspect the matching `ExampleUtilities/**` source files for imports, class structure, hook signatures, parameter declarations, and UI interaction style.
5. Generate code using only APIs confirmed in the target version.

For migrations:

1. Identify the direction: `2024.3 -> 2026.1` or `2026.1 -> 2024.3`.
2. Read the source version's `user-utility.md` and `example-utilities.md`.
3. Read the target version's `user-utility.md` and `example-utilities.md`.
4. Compare relevant `Ts*.py`, `Dlg*.py`, and `Run*.py` examples in both versions.
5. Preserve business logic and prioritize changes to API calls, import paths, parameter declarations, execution hooks, report output, and dialog handling.
6. Mention any behavior that cannot be confirmed in the target-version docs.

## Utility Type Selection

Choose the base class after reading the target docs:

| Need | Likely base class |
|---|---|
| Custom configuration dialog, custom instance state, direct test case variable access | `TsUserUtility` |
| Keyword-like utility with declared arguments and return values | `TsAXSUtility` |
| Generated ecu.test UI based on an interface declaration | `TsAXSUtility` |
| Manual wx dialog or `ThreadDialog` interaction | Usually `TsUserUtility`, unless target docs/examples show an AXS pattern |

Confirm lifecycle signatures in the target version before writing code. Common hooks include `UtilityInit`, `GetDialog`, `OnPreProcess`, `OnRun`, `OnPostProcess`, `UtilityReport`, `GetInterface`, and `GetReportInfos`, but their signatures must come from the selected version.

## Implementation Checks

Before finalizing code, verify these against the target-version docs/examples:

- Imports from `tts.testExecution.api.*` and any supporting `tts.*` namespaces.
- Class metadata such as `ID`, `NAME`, and `DESCRIPTION`.
- `SERIALIZE` keys, type names, and defaults for persisted `TsUserUtility` instance fields.
- `GetInterface()` argument and return declarations for `TsAXSUtility`.
- `OnRun` signature and how inputs/outputs are read or written.
- `GetVariableValue`, `SetVariableValue`, and variable existence checks when accessing test case variables.
- `ThreadDialog` use for dialogs opened during execution.
- `UtilityReport` and `reportDataObject` use when writing report information.

Use stable UUIDs for utility `ID` values. Do not generate a new ID at runtime.

## Search Hints

Use targeted searches before loading large files:

```powershell
Select-String -Path 'references\2026.1\user-utility\user-utility.md' -Pattern 'TsAXSUtility|TsUserUtility|ThreadDialog|SERIALIZE|OnRun|GetInterface'
Select-String -Path 'references\2024.3\ExampleUtilities\*\*.py' -Pattern '^from |^class |def OnRun|def GetDialog|def GetInterface|SERIALIZE|ThreadDialog'
```

Adjust the version path to match the requested target.

## Common Mistakes

- Defaulting silently: if no version is specified, state that `2026.1` was used.
- Migrating from memory: read both source and target docs.
- Mixing internal User Utility code with external `ApiClient`, REST, or COM patterns.
- Reusing 2026.1-only APIs in a 2024.3 target without checking 2024.3 docs.
- Changing the utility `ID` during migration unless the user explicitly wants a new utility identity.
- Calling wx dialogs directly during execution when the version examples require `ThreadDialog`.

## Related Skills

- `ecu-test-internal-api`: use when the utility needs `self.api` or internal ecu.test objects.
- `ecu-test-report-api`: use for detailed report parser/report object work beyond User Utility examples.
- `ecu-test-data-structures`: use when utility inputs or variables use bus, diagnostic, media, DLT, or other complex ecu.test structures.
- `ecu-test-trace-analysis-api`: use for trace-analysis Python templates; they are not User Utilities.
