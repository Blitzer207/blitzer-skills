---
name: ecu-test-test-management-api
description: Use when creating, modifying, or reviewing ecu.test User Test Management adapters, including TmUserAdapter implementations, USER_TMS modules, login/logout handling, project or package import/export, custom test-management context menu actions, TmObjectInfo trees, or 2026.1-only test management API questions.
---

# ecu.test Test Management API

## Scope

Use this skill for ecu.test User Test Management adapter scripts that run inside ecu.test.

- Execution environment: internal ecu.test Python execution, not an external controller.
- Namespace: `tts.extension.testManagementService.*`
- Main adapter class: `TmUserAdapter`
- Module marker: `MODULE_TYPE = 'USER_TMS'`
- Data object: `TmObjectInfo`
- Supported documented target version: `ecu.test 2026.1`

Do not use this skill for external `ApiClient`, REST, COM automation, User Utilities, or generic Object API edits unless the task specifically involves a user test management adapter. Use the corresponding ecu.test API skill for those environments.

## Version Routing

Always identify the target version before generating or changing code.

1. If the user explicitly names `2026.1`, use the bundled 2026.1 User Test Management docs.
2. If the user does not specify a version, default to `2026.1` and state that default in the response.
3. If the user explicitly asks for `2024.3`, state that this plan found no corresponding `userTestmanagement/` documentation for 2024.3 and do not claim 2024.3 support from the 2026.1 docs.
4. For downgrade or migration tasks involving 2024.3, read the 2026.1 docs first to identify the API surface, then report that the target/source 2024.3 Test Management API cannot be confirmed from bundled docs unless the user provides additional 2024.3 documentation.
5. If a method name, import path, adapter marker, property schema, callback signature, return value, or `TmObjectInfo` field is uncertain, check the 2026.1 docs before using it.
6. Label generated or modified code as applying to `ecu.test 2026.1`.

Do not infer 2024.3 compatibility from other ecu.test APIs or from the existence of similar concepts.

## Bundled Authoritative Docs

Read these files from this skill directory. They are copied into the skill and are the source of truth for this skill.

| Version | Required docs |
|---|---|
| 2026.1 | `references/2026.1/userTestmanagement/index.md` |
| 2026.1 | `references/2026.1/userTestmanagement/tmuser-api.md` |

No 2024.3 reference files are bundled because `api-skills-plan.md` records no discovered 2024.3 `userTestmanagement/` directory.

## Required Workflow

For new adapters:

1. Determine the target version. Default to `2026.1` if unspecified.
2. Read `references/2026.1/userTestmanagement/index.md`.
3. Read `references/2026.1/userTestmanagement/tmuser-api.md`.
4. Confirm `MODULE_TYPE`, class name, constructor signature, required methods, optional methods, property schema, callback signatures, and return types from the docs.
5. Generate code using only APIs confirmed in the 2026.1 docs.

For reviews or modifications:

1. Check that the module declares `MODULE_TYPE = 'USER_TMS'`.
2. Check that the adapter meets the documented `TmUserAdapter` interface.
3. Verify method signatures and return values against `tmuser-api.md`.
4. Verify that object lists returned for import dialogs use `TmObjectInfo` with documented fields.
5. If project/package files are modified through Object API, also use `ecu-test-object-api`.

For 2024.3 requests:

1. Search only to confirm whether the repository now contains 2024.3 User Test Management docs.
2. If no docs exist, say the API is not confirmed for `ecu.test 2024.3`.
3. Do not generate supposedly 2024.3-compatible adapter code from the 2026.1 docs alone.

## Adapter Surface

Confirm the exact signatures in `tmuser-api.md` before writing code.

| Need | API surface |
|---|---|
| Register adapter module | `MODULE_TYPE = 'USER_TMS'` |
| Adapter identity | `TmUserAdapter.GetName()` |
| Configuration options in ecu.test settings | `TmUserAdapter.GetAvailableProperties()` |
| Runtime configured values | `TmUserAdapter.__init__(properties)` |
| Authentication state | `Login()`, `Logout()`, `IsLoggedIn()` |
| Export `.prj` files to TMS | `ExportProject(filePaths)` |
| Import `.prj` files from TMS | `ImportProject(targetDirectory, tmsIds)` |
| Export `.pkg` files to TMS | `ExportPackage(filePaths)` |
| Export changed `.pkg` files | `ExportPackageChanges(filePaths)` |
| Import `.pkg` files from TMS | `ImportPackage(targetDirectory, tmsIds)` |
| Context menu actions | `GetCustomPackageActions()`, `GetCustomProjectActions()`, `GetCustomDirectoryActions()` |
| Import selection root lists | `GetProjectsFromTms()`, `GetPackagesFromTms()` |
| Import selection child lists | `FetchChildrenForProjectImport(tmsId)`, `FetchChildrenForPackageImport(tmsId)` |
| Attribute synchronization | `UpdateAttributeDefinitions()` |
| Import tree/list objects | `TmObjectInfo(name, tmsId, attributes=None)` |

## Implementation Checks

Before finalizing code, verify these against `tmuser-api.md`:

- `MODULE_TYPE` is exactly the documented test-management module marker.
- The adapter class satisfies the documented `TmUserAdapter` interface.
- Required methods are implemented; optional methods are only included when needed.
- `GetAvailableProperties()` returns the documented nested dictionary shape, including property `Description`, `Type`, and `Default` fields where used.
- Custom action methods accept lists of selected paths, not a single path, when registered for context menus.
- Import list/tree methods return documented `TmObjectInfo` instances or lists of those instances.
- Import/export methods use `.prj` for projects and `.pkg` for packages.
- Project/package TMS identifiers are set through the correct Object API methods when needed, after checking the Object API docs.

## Search Hints

Use targeted searches before loading the full API file:

```powershell
Select-String -Path 'references\2026.1\userTestmanagement\tmuser-api.md' -Pattern 'MODULE_TYPE|USER_TMS|TmUserAdapter|TmObjectInfo'
Select-String -Path 'references\2026.1\userTestmanagement\tmuser-api.md' -Pattern 'GetAvailableProperties|Login|Logout|IsLoggedIn|ExportProject|ImportProject|ExportPackage|ImportPackage'
Select-String -Path 'references\2026.1\userTestmanagement\tmuser-api.md' -Pattern 'GetCustomPackageActions|GetCustomProjectActions|GetCustomDirectoryActions|FetchChildren|GetProjectsFromTms|GetPackagesFromTms'
```

For a 2024.3 availability check:

```powershell
Get-ChildItem -Path '2024.3-APIDoc-MD' -Recurse -File | Where-Object { $_.FullName -match 'userTest|testManagement|tmuser' }
```

## Common Mistakes

- Claiming 2024.3 support even though no 2024.3 Test Management docs are bundled.
- Mixing User Test Management adapters with User Utility classes such as `TsUserUtility` or `TsAXSUtility`.
- Implementing an external automation script instead of an internal ecu.test adapter module.
- Omitting `MODULE_TYPE = 'USER_TMS'`.
- Returning plain dictionaries where the docs require `TmObjectInfo`.
- Registering custom context menu callbacks that only handle a single file path.
- Guessing Object API calls for setting project or package TMS IDs without reading the Object API docs.

## Related Skills

- `ecu-test-object-api`: use when the adapter generates or modifies `.prj` or `.pkg` files through Object API, including project test suite IDs or package test script IDs.
- `ecu-test-user-utility-api`: use for User Utility scripts; they are not Test Management adapters.
- `ecu-test-internal-api`: use for broader internal ecu.test APIs outside the User Test Management interface.
- `ecu-test-data-structures`: use if adapter properties or imported object metadata involve complex ecu.test data structures.
