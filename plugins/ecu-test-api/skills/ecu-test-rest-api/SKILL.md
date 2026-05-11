---
name: ecu-test-rest-api
description: Use when creating, modifying, reviewing, or migrating external ecu.test REST/OpenAPI HTTP automation, including local or remote API access, configuration start, package or project execution, operation polling, report upload, base URL or port handling, and version-specific 2024.3/2026.1 REST API work.
---

# ecu.test REST API

## Scope

Use this skill for external programs that control ecu.test through the OpenAPI-based REST API.

- Execution environment: external HTTP client. ecu.test must be running with REST API enabled.
- Interface: HTTP/OpenAPI, default local base URL `http://127.0.0.1:5050/api/v2`.
- Interactive docs: `http://127.0.0.1:5050/api/v2/ui` when ecu.test is running.
- Supported platforms: Windows and Linux.
- Supported target versions: `ecu.test 2024.3` and `ecu.test 2026.1`.

Do not use this skill for COM automation, external Object API file editing, or internal ecu.test Python code. Use the corresponding ecu.test API skill for those environments.

## Supported ecu.test Versions

- 2024.3: use `references/2024.3/general_api/rest-api.md`.
- 2026.1: use `references/2026.1/general_api/rest-api.md`.
- Default version: `2026.1` when the user does not specify a version.

## Version Routing

Always identify the target version before generating or changing code.

1. If the user explicitly names `2024.3`, use only the 2024.3 REST docs for generated code.
2. If the user explicitly names `2026.1`, use only the 2026.1 REST docs for generated code.
3. If the user does not specify a version, default to `2026.1` and state that default in the response.
4. For migration or downgrade tasks, read both versions: first the source version, then the target version.
5. If an endpoint, payload field, status value, operation polling pattern, return field, or startup flag is uncertain, check the target-version docs before using it.
6. Label generated or modified code as applying to `ecu.test 2024.3` or `ecu.test 2026.1`.

Similarity between 2024.3 and 2026.1 is not a compatibility guarantee. Do not infer compatibility from memory.

## Bundled Authoritative Docs

| Version | Required doc |
|---|---|
| 2024.3 | `references/2024.3/general_api/rest-api.md` |
| 2026.1 | `references/2026.1/general_api/rest-api.md` |

The bundled docs include the core Python workflow. If the user asks for a complete endpoint schema and ecu.test is available, prefer the live OpenAPI UI for exact current schemas, but still respect the target version requested by the user.

## Required Workflow

For new REST automation:

1. Determine the target version. Default to `2026.1` if unspecified.
2. Read the target version's `rest-api.md`.
3. Confirm base URL, local vs remote access, port, endpoint path, payload, and polling behavior.
4. Generate code using only endpoints and fields confirmed in the target version.
5. Include `raise_for_status()` or equivalent error handling for generated HTTP code.

For migrations:

1. Identify the direction: `2024.3 -> 2026.1` or `2026.1 -> 2024.3`.
2. Read the source version's `rest-api.md`.
3. Read the target version's `rest-api.md`.
4. Preserve workflow logic and update endpoint paths, payload fields, status handling, report upload handling, and startup assumptions.
5. In the answer, include source version, target version, key docs checked, and a short modification summary.

## Demand Keyword Routing

| User mentions | Search first in `rest-api.md` |
|---|---|
| base URL, port, local API, OpenAPI UI | `127.0.0.1:5050/api/v2`, `/ui`, `--restApiPort` |
| remote REST access, remote host | `--restApiEnableRemoteAccess` |
| health check, reachability, live state | `/live`, `requests.get` |
| load or start TBC/TCF, configuration | `/configuration`, `tbcPath`, `tcfPath` |
| execute package or project, test run | `/execution`, `testCasePath` |
| wait or poll async operation | `WaitForOperationEnd`, `WAITING`, `RUNNING`, `status` |
| report ID, report upload, test.guide upload | `testReportId`, `/reports/{reportId}/upload`, `testGuideUrl` |
| Python requests example | `requests`, `raise_for_status`, `json=` |
| Linux control | REST API docs; do not switch to COM |

## Implementation Checks

Before finalizing REST code, verify these against the target-version docs:

- ecu.test is running and REST API availability is an explicit prerequisite.
- Remote access requires the documented command-line option.
- Non-default port handling changes the base URL consistently.
- Long-running endpoints are polled until the documented terminal status.
- HTTP errors are checked.
- Payload keys match the target-version docs.
- Generated code states whether it targets `ecu.test 2024.3` or `ecu.test 2026.1`.

## Search Hints

```powershell
Select-String -Path 'references\2026.1\general_api\rest-api.md' -Pattern 'BASE_URL|/live|/configuration|/execution|/reports|WaitForOperationEnd'
Select-String -Path 'references\2026.1\general_api\rest-api.md' -Pattern 'restApiEnableRemoteAccess|restApiPort|127.0.0.1|api/v2/ui'
Select-String -Path 'references\2024.3\general_api\rest-api.md' -Pattern 'configuration|execution|testReportId|upload|WAITING|RUNNING'
```

Adjust the version path to match the requested target.

## Common Mistakes

- Defaulting silently. If no version is specified, state that `2026.1` was used.
- Migrating from memory. Read both source and target docs.
- Assuming REST is remotely reachable without `--restApiEnableRemoteAccess`.
- Starting execution and immediately reading results without polling operation status.
- Using COM on Linux instead of REST.
- Using Object API to execute tests instead of REST or COM.

## Related Skills

- `ecu-test-com-api`: use for Windows COM automation.
- `ecu-test-object-api`: use for file/object creation before REST execution.
- `ecu-test-report-api`: use for detailed report parsing after execution.
- `ecu-test-internal-api`: use for internal ecu.test Python APIs.
