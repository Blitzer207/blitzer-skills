---
name: testguide-rest-api-skill
description: Use when creating, modifying, reviewing, or debugging external test.guide REST/OpenAPI HTTP automation, including auth keys or bearer auth, base URL and context-path handling, project-scoped requests, artifacts, executions, reports, report management, flow triggers/tasks, coverage, q-gates, releases, SCM, monitoring, platform, users, webhooks, health checks, and any task requiring the bundled test.guide OpenAPI YAML specs.
---

# test.guide REST API Skill

## Scope

Use this skill for external programs that call test.guide through HTTP REST APIs.

- Interface: OpenAPI 3 YAML specs bundled under `references/restapi-docs`.
- Authentication: the specs define `TestGuideAuthKey` and/or `BearerAuth`; verify the target spec before generating code.
- Base URL pattern: combine the user's test.guide host with the server path in the relevant spec, for example `/api/report`, `/api/artifact`, or `/api/execution`.
- Some deployments use a context path such as `/test-guide`; use the matching server entry from the spec when needed.

Do not use this skill for flow.kit block graph authoring. Use `testguide-flowkit-skill` when the task is about `flow_definition.py`, `FlowBuilder`, blocks, bundle validation, or flow visualization.

## Bundled OpenAPI Specs

Read the relevant YAML before writing endpoint paths, payloads, response parsing, or polling logic.

| Area | Spec |
|---|---|
| Artifacts and depositories | `references/restapi-docs/artifactsApi.yaml` |
| Coverage | `references/restapi-docs/coverageApi.yaml` |
| Execution tasks, playbooks, variables, secrets | `references/restapi-docs/executionApi.yaml` |
| flow.kit triggers and flow tasks | `references/restapi-docs/flowApi.yaml` |
| Health, readiness, version, description | `references/restapi-docs/healthApi.yaml` |
| Monitoring and activity/status endpoints | `references/restapi-docs/monitoringApi.yaml` |
| Platform projects, notification, maintenance | `references/restapi-docs/platformApi.yaml` |
| Q-gates and plans | `references/restapi-docs/qGatesApi.yaml` |
| Releases | `references/restapi-docs/releasesApi.yaml` |
| Reporting templates and exports | `references/restapi-docs/reportingApi.yaml` |
| Report upload, TCEs, reviews, ATX export | `references/restapi-docs/reportMgmtApi.yaml` |
| SCM configurations and indexing | `references/restapi-docs/scmApi.yaml` |
| Test infrastructure and resources | `references/restapi-docs/testInfrastructureApi.yaml` |
| Users, roles, auth keys, project assignment | `references/restapi-docs/userMgmtApi.yaml` |
| Webhooks | `references/restapi-docs/webhookApi.yaml` |

## Required Workflow

1. Identify the task area and select the spec from the table above.
2. Read the selected YAML sections: `servers`, `security`, the target `paths` entry, request body schema, parameters, responses, and referenced component schemas.
3. Build the URL from the user's host plus the selected spec's server path. Preserve context path handling when the user gives a URL containing `/test-guide` or another deployment prefix.
4. Generate HTTP code using only confirmed methods, parameters, payload keys, content types, and response fields.
5. Include explicit HTTP error handling such as `raise_for_status()` or equivalent.
6. For asynchronous endpoints returning task IDs, read and use the corresponding status/download/delete endpoint from the same spec; do not guess terminal states.
7. Avoid printing auth keys or bearer tokens in logs, examples, or error messages.

## Search Hints

Use exact endpoint, operation, schema, or domain words:

```powershell
Select-String -Path 'references\restapi-docs\reportMgmtApi.yaml' -Pattern '/reports|uploadstatus|TaskRef|converterId'
Select-String -Path 'references\restapi-docs\artifactsApi.yaml' -Pattern '/depositories|/storages|Storage|share'
Select-String -Path 'references\restapi-docs\executionApi.yaml' -Pattern '/task|/playbook|execute|status'
Select-String -Path 'references\restapi-docs\flowApi.yaml' -Pattern '/triggers|/tasks|start'
```

When the target area is unclear, search all specs:

```powershell
Get-ChildItem 'references\restapi-docs' -Filter '*.yaml' |
  Select-String -Pattern 'operationId|summary|/reports|/artifacts|/task|/projects'
```

## Implementation Rules

- Do not infer endpoint availability from another test.guide API area; each YAML file owns its own server path and component schemas.
- Preserve required query/path parameters such as `projectId`, IDs, task IDs, and filter IDs exactly as documented.
- Match content types. For example, report upload and artifact upload/download endpoints may use binary or multipart content instead of JSON.
- Use request timeouts for generated Python `requests` code.
- Keep generated examples small and runnable: configure `TEST_GUIDE_URL` and auth via environment variables or function parameters.
- If an endpoint references a component schema, inspect that schema before constructing payload examples.
- If a user gives existing code, map each call back to the exact YAML path and response before changing it.

## Common Mistakes

- Joining URLs as `host + path` without including the spec server base path such as `/api/report`.
- Treating all endpoints as JSON when the spec says `application/zip`, binary, or another content type.
- Guessing async task status fields instead of reading the matching status endpoint.
- Mixing report management endpoints with reporting-template endpoints.
- Printing `TEST_GUIDE_AUTH_KEY`, bearer tokens, or complete request headers.
- Using flow.kit block docs when the user asked for direct REST/OpenAPI automation.
