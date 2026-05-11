---
name: testguide-flowkit-skill
description: Create, debug, and optimize flow.kit-based test.guide workflows in flow bundle workspaces. Use when designing or modifying flows with FlowBuilder/add_block_with/Assign, selecting and connecting flow.kit blocks such as triggers, test.guide, control-flow, and user-code blocks, running main.py to validate/execute/visualize, or consulting bundled flow.kit snippets, official docs, and API stubs.
---

# test.guide flow.kit Bundle Skill

## Scope

Use this skill for flow.kit workflow work inside a flow bundle workspace.

- A flow bundle contains the flow.kit runtime plus the custom workflow files.
- The custom files are normally `flow_definition.py`, `test_user_code.py`, and optionally `image.png` or trigger payload fixtures.
- Edit workflow behavior in `flow_definition.py`.
- Put helper logic referenced by `GenericUserCode` or unit tests in `test_user_code.py`.
- Prefer the target bundle's own interpreter or documented local run command when validating, executing, or visualizing.

Do not edit copied runtime/template files in a flow bundle unless the user explicitly asks for bundle infrastructure changes.

## Authoritative Sources

Prefer local source evidence in this order:

1. Current target bundle files: `flow_definition.py`, `test_user_code.py`, `image.png`, payload files, and run/debug configuration files.
2. Skill-bundled official docs: `references/official-docs/docs-md/*.md`.
3. Skill-bundled official block docs: `references/official-docs/docs-md/Block documentation/**/*.md`.
4. Skill-bundled snippets and examples:
   - `references/how_to_build_a_flow_definition.md`
   - `references/flow-kit-snippets.code-snippets`
   - `references/official-sources.md`
   - `examples/batch_processing_usage.py`
5. Target bundle or template API stubs when present: `flow_kit/**/*.pyi` and `site-packages/**/*.pyi`.

If a class name, import path, `PAR__...` parameter identifier, result type, constructor argument, trigger payload shape, or execution command is uncertain, read the official docs, snippets, stubs, or bundle-local configuration before writing code.

## Required Workflow

1. Identify the target flow bundle and inspect only the relevant custom files first.
2. Determine the trigger from the user request, existing trigger block, and payload/config files when relevant.
3. Search snippets and block docs for candidate blocks before inventing flow code.
4. Implement the workflow in `get_flow() -> Flow` with `FlowBuilder().add_block_with(...).build()`.
5. Put helper logic referenced by `GenericUserCode` or tests in `test_user_code.py`.
6. Validate from the target bundle directory with the bundle interpreter or documented local command.
7. Execute only when the user provided, or the bundle already has, the required test.guide environment variables/auth key.

## Flow Definition Rules

- Use one trigger block that matches the actual trigger type.
- Keep block references with the walrus operator when downstream blocks need `to_block_result(...)`, `required_blocks=[...]`, or `out_block`.
- Use `.with_label("...")` for readable reporting and visualization.
- Assign required parameters with `Assign(PAR__...).to_static_value(...)`, `.to_block_result(...)`, or `.to_user_expression(...)`.
- Use `result_alias="..."` before referencing a block result in `to_user_expression("alias.field")`.
- Add `required_blocks=[...]` when ordering is important and not already implied by parameter assignment.
- Use `GenericUserCode` for nontrivial conversions, filtering, payload parsing, or custom business logic.
- Use `BatchProcessing` for per-item subflows instead of unrolled duplicate blocks.
- Prefer trigger filters over late `ConditionalSkip` blocks when the workflow can be rejected before execution.

## Search Hints

PowerShell examples from the skill or bundle root:

```powershell
Get-ChildItem -Recurse -File 'references\official-docs\docs-md' -Filter '*.md' |
  Select-String -Pattern 'StartReportGeneration|GetArtifact|BatchProcessing'

Get-ChildItem -Recurse -File 'flow_kit' -Filter '*.pyi' |
  Select-String -Pattern 'class StartReportGeneration|PAR__|result'

Select-String -Path 'references\flow-kit-snippets.code-snippets' -Pattern '"GetArtifact"|"BatchProcessing"'
```

When inspecting block documentation, start from `references/official-docs/docs-md/index.md` to find the correct module area:

| Need | First docs to inspect |
|---|---|
| Flow syntax, assignments, labels, dependencies | `references/official-docs/docs-md/how_to_build_a_flow_definition.md` |
| Validate/execute/visualize behavior | `references/official-docs/docs-md/validate_execute_visualize.md` |
| Trigger blocks | `references/official-docs/docs-md/Block documentation/flow_kit.library.trigger.md` and trigger stubs |
| test.guide artifacts/executions/reports/releases | `references/official-docs/docs-md/Block documentation/test_guide/*.md` |
| File operations | `references/official-docs/docs-md/Block documentation/flow_kit.library.file_operation.md` |
| Control flow | `references/official-docs/docs-md/Block documentation/flow_kit.library.control_flow.md` |
| User code blocks | `flow_kit/library/user_code/*.pyi`, bundle-local stubs, and snippets |

## Validation Commands

Always run commands after `cd` into the target bundle.

If the bundle contains an `interpreter` directory:

```powershell
$env:TT_RUN_IN_FLOW_AUTOMATION='True'
.\interpreter\python.exe .\main.py --validate --validate-runs-unittests
```

If the bundle documents another interpreter or launch command, use the bundle-local command instead of system Python.

Visualize:

```powershell
$env:TT_RUN_IN_FLOW_AUTOMATION='True'
.\interpreter\python.exe .\main.py --visualize
```

Execute locally only when required environment values are available:

```powershell
$env:TT_RUN_IN_FLOW_AUTOMATION='True'
$env:TEST_GUIDE_URL='https://testguide.one-cx.cn'
$env:TEST_GUIDE_AUTH_KEY='<auth_key>'
$env:FLOW_KIT_HIDE_TEST_GUIDE_AUTH_KEY='True'
$env:TEST_GUIDE_PROJECT_ID='<project_id>'
$env:TRIGGER_PAYLOAD='{}'
.\interpreter\python.exe .\main.py --execute --validate-runs-unittests
```

Do not invent `TEST_GUIDE_PROJECT_ID`, auth keys, payloads, or production URLs. Read them from the user request or bundle-local `.env`/sample/config files.

## Common Mistakes

- Running validation from the repository root instead of the bundle directory.
- Using system Python when the bundle provides an interpreter.
- Guessing `PAR__...` identifiers or import paths instead of reading snippets, block docs, or `.pyi` stubs.
- Editing copied runtime/template files inside a flow bundle when only `flow_definition.py` or `test_user_code.py` should change.
- Forgetting `result_alias` before using `to_user_expression("alias.field")`.
- Assuming dependency order from visual layout; use parameter assignments or `required_blocks`.
- Executing against test.guide without required environment variables or without hiding the auth key.
