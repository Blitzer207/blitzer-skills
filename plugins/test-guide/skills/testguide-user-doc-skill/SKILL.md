---
name: testguide-user-doc-skill
description: Use when answering test.guide product usage, UI operation, configuration, administration, integration, troubleshooting, FAQ, glossary, report management, release management, Q-gate, monitoring, artifact management, execution task, playbook, workflow automation, dashboard, project setting, system setting, and end-user documentation questions from the bundled official test.guide user manual.
---

# test.guide User Documentation Skill

## Scope

Use this skill to answer how-to and conceptual questions about using test.guide from the official user documentation.

- Main reference: `references/user-documentation.md`.
- Figures and screenshots: `references/test.guide user documentation-media/`.
- Source metadata in the bundled Markdown says the manual was created and published on 2026-04-13.

Do not use this skill as the main source for direct REST/OpenAPI client code. Use `testguide-rest-api-skill` for endpoint paths, schemas, authentication details, and generated HTTP automation. Use `testguide-flowkit-skill` for flow.kit bundle authoring, `flow_definition.py`, block selection, validation, execution, or visualization.

## Required Workflow

1. Classify the question by feature area and locate the relevant section in `references/user-documentation.md`.
2. Read the exact section plus nearby headings before answering.
3. If the section contains a figure that affects the answer, inspect the linked image under `references/test.guide user documentation-media/`.
4. Answer in the user's language. Keep product names and UI terms such as `test.guide`, `ecu.test`, `Q-gate`, `ResourceAdapter`, `Flow trigger`, `Flow task`, `SCM`, `TR`, and `TRM` precise.
5. State when the manual does not cover a requested detail. Do not invent menu paths, permissions, environment variables, or behavior.
6. Prefer concise operational answers: what to open, what to configure, what result to expect, and which documented caveat matters.

## Section Map

Use these entry points before searching the full document:

| Question area | Start in the manual |
|---|---|
| Product overview, installation, modules | `1 Introduction`, `1.2 Installing`, `1.3 Key modules` |
| Report upload, filters, test case details, comparison, exports | `2.1 Using the test report management` |
| Review workflow, defects/issues, bulk reviews, ecu.test review | `2.1.2 Using the review feature` |
| Coverage, release trains, releases, Q-gates | `2.2 Using the release management` |
| ResourceAdapter setup, test resource monitoring, activities, aggregated states | `2.3 Using the monitoring of test resources` |
| Depositories and artifact management | `2.4 Using the artifact management` |
| Execution tasks, test bundles, delayed/recurring tasks, direct test bench assignment | `2.5.2 Execution tasks` |
| Execution with ecu.test, Jenkins, or generic tasks | `2.5.3`, `2.5.4`, `2.5.5` |
| Playbooks, variables, constants, environment variables, failure behavior | `2.5.6 Playbooks` |
| Workflow automation UI, flow triggers, flow tasks | `2.6 Using the workflow automation` |
| Integrating with ecu.test, Jenkins, or test.guide | `3 Integrating` |
| Project administration, users, filters, reviews, reporting, issue trackers, uploads | `4 Project Settings` sections such as `4.2 Project users` and `4.8 Upload Rules` |
| System administration, authentication, user management, groups, projects, email, backup | `5 System configuration` sections |
| Dashboards, report filters, PDF export customization | `6 Customizing` |
| Developer-facing usage described in the user manual | `7 Developing` |
| Logs and troubleshooting | `8 Troubleshooting` |
| FAQs and terminology | `9 FAQs`, `10 Glossary` |

## Search Hints

From the skill root, use narrow searches first:

```powershell
Select-String -Path 'references\user-documentation.md' -Pattern 'Q-gate|staging|quality gate'
Select-String -Path 'references\user-documentation.md' -Pattern 'ResourceAdapter|test resource|monitoring'
Select-String -Path 'references\user-documentation.md' -Pattern 'playbook|environment variables|constants'
Select-String -Path 'references\user-documentation.md' -Pattern 'upload rule|report remove|recycle bin'
```

For a how-to question, search both the user's wording and likely official wording:

```powershell
Select-String -Path 'references\user-documentation.md' -Pattern 'How do I create execution tasks|delayed|recurring'
Select-String -Path 'references\user-documentation.md' -Pattern 'filter|notification|share|dashboard'
```

When headings are enough to find a region:

```powershell
Select-String -Path 'references\user-documentation.md' -Pattern '^## |^### |^#### '
```

## Answer Rules

- Ground every factual step in the bundled manual. If the manual has screenshots but not enough procedural text, say that the manual shows the UI context and summarize only what is visible or stated.
- Preserve documented option names, states, variables, and role names exactly.
- When the user's question is broad, first give the shortest useful path, then mention the documented section for deeper detail.
- When the user's question asks for implementation code, check whether it is really a user-doc task. Route REST code to `testguide-rest-api-skill` and flow.kit code to `testguide-flowkit-skill`.
- If the manual appears internally duplicated or partially translated in a section, reconcile by using the most complete matching section and mention only stable documented facts.

## Common Mistakes

- Answering from general test management knowledge instead of searching the bundled manual.
- Mixing user-documentation concepts with REST API schemas or flow.kit block behavior.
- Guessing UI menu labels when the manual only describes a concept.
- Treating screenshots as sufficient proof for details that are not visible or stated.
- Translating product identifiers or abbreviations inconsistently.
