---
name: ecu-test-generator-api
description: Use when creating, modifying, reviewing, or migrating ecu.test generator code for automatically creating projects, packages, or parameter sets, including Project Generator API, Package Generator API, Parameter Set Generator API, generator index differences, and version-specific 2024.3/2026.1 generator API work.
---

# ecu.test Generator API

## Scope

Use this skill for ecu.test Generator APIs that automatically create many projects, packages, or parameter sets.

- Execution environment: external generator-oriented automation as documented by the generator APIs.
- Covered generators: project generator, package generator, and parameter set generator.
- Supported target versions: `ecu.test 2024.3` and `ecu.test 2026.1`.

Do not use this skill for generic Object API package editing, REST/COM test execution, internal User Utilities, or trace analysis templates. Use the corresponding ecu.test API skill for those environments.

## Supported ecu.test Versions

- 2024.3: use `references/2024.3/generators/index.md`.
- 2026.1: use `references/2026.1/generators/index.md` and detailed generator API pages.
- Default version: `2026.1` when the user does not specify a version.

## Version Routing

Always identify the target version before generating or changing code.

1. If the user explicitly names `2024.3`, use only the 2024.3 generator docs for generated code.
2. If the user explicitly names `2026.1`, use only the 2026.1 generator docs for generated code.
3. If the user does not specify a version, default to `2026.1` and state that default in the response.
4. For migration or downgrade tasks, read both versions: first the source version, then the target version.
5. If a generator class, input schema, command, folder layout, return value, or generated artifact type is uncertain, check the target-version docs before using it.
6. Label generated or modified code as applying to `ecu.test 2024.3` or `ecu.test 2026.1`.

2024.3 has only the bundled generator index in this plan. 2026.1 has separate detailed pages for project, package, and parameter set generators. Do not assume 2026.1 detailed APIs exist in 2024.3 unless confirmed by 2024.3 docs or user-provided docs.

## Bundled Authoritative Docs

| Version | Required docs |
|---|---|
| 2024.3 | `references/2024.3/generators/index.md` |
| 2026.1 | `references/2026.1/generators/index.md` |
| 2026.1 | `references/2026.1/generators/projectgenerator-api/projectgenerator-api.md` |
| 2026.1 | `references/2026.1/generators/packagegenerator-api/packagegenerator-api.md` |
| 2026.1 | `references/2026.1/generators/parametersetgenerator-api/parametersetgenerator-api.md` |

## Required Workflow

For new generator code:

1. Determine the target version. Default to `2026.1` if unspecified.
2. Read the target version's `generators/index.md`.
3. For 2026.1, read the specific generator page matching the requested artifact.
4. For 2024.3, do not invent detailed generator APIs beyond what `index.md` confirms.
5. Generate code or guidance using only APIs confirmed in the target version.

For migrations:

1. Identify the direction: `2024.3 -> 2026.1` or `2026.1 -> 2024.3`.
2. Read source and target generator docs.
3. Preserve generation intent and update generator type, input configuration, API calls, and output artifact assumptions.
4. If downgrading to 2024.3 and the detailed API is not confirmed, say what cannot be confirmed instead of fabricating compatibility.
5. In the answer, include source version, target version, key docs checked, and a short modification summary.

## Demand Keyword Routing

| User mentions | Read first |
|---|---|
| generator overview, which generator to use | `generators/index.md` |
| project generator, create projects, bulk project creation | 2026.1: `projectgenerator-api/projectgenerator-api.md`; 2024.3: `index.md` |
| package generator, create many packages, package variants | 2026.1: `packagegenerator-api/packagegenerator-api.md`; 2024.3: `index.md` |
| parameter set generator, parameter sets, parameter variants | 2026.1: `parametersetgenerator-api/parametersetgenerator-api.md`; 2024.3: `index.md` |
| generated package structure after creation | also use `ecu-test-object-api` if the task edits generated `.pkg` files |
| generated project structure after creation | also use `ecu-test-object-api` if the task edits generated `.prj` files |

## Implementation Checks

Before finalizing generator code or guidance, verify these against the target-version docs:

- Target version is explicit.
- The requested generator type is documented for that target version.
- 2024.3 answers do not borrow 2026.1 detailed generator APIs without documentation.
- Generated artifacts and follow-up edits are routed to Object API when needed.
- Generated code states whether it targets `ecu.test 2024.3` or `ecu.test 2026.1`.

## Search Hints

```powershell
Select-String -Path 'references\2026.1\generators\index.md' -Pattern 'Project Generator|Package Generator|Parameter Set Generator'
Select-String -Path 'references\2026.1\generators\projectgenerator-api\projectgenerator-api.md' -Pattern 'class|def |Project|Generator|parameter|return'
Select-String -Path 'references\2026.1\generators\packagegenerator-api\packagegenerator-api.md' -Pattern 'class|def |Package|Generator|parameter|return'
Select-String -Path 'references\2026.1\generators\parametersetgenerator-api\parametersetgenerator-api.md' -Pattern 'class|def |Parameter|Generator|parameter|return'
Select-String -Path 'references\2024.3\generators\index.md' -Pattern 'Generator|Project|Package|Parameter'
```

## Common Mistakes

- Defaulting silently. If no version is specified, state that `2026.1` was used.
- Migrating from memory. Read both source and target docs.
- Treating 2026.1 detailed generator pages as confirmed 2024.3 API.
- Using generator APIs for one-off manual object edits better handled by Object API.
- Using generator APIs for execution control instead of REST or COM.

## Related Skills

- `ecu-test-object-api`: use for `.pkg`, `.prj`, `.tcf`, or `.tbc` edits after generation.
- `ecu-test-rest-api`: use for HTTP execution after generated artifacts exist.
- `ecu-test-com-api`: use for COM execution after generated artifacts exist.
- `ecu-test-data-structures`: use when generated artifacts include complex variable or bus structures.
