# test.guide flow.kit workflow assistant

Create, debug, and optimize flow.kit-based `test.guide` workflows (flow bundles) by editing `flow_definition.py` and running local validation/execution/visualization.

This repository contains the skill instructions plus bundled references (snippets + condensed docs) to help an AI agent work effectively in a flow bundle workspace.

## Quick start

- Install this skill into your tool’s skills folder (Codex / Claude Code / Cursor):
  - Copy the `testguide-flowkit` folder into your skills directory, or
  - Install the packaged `testguide-flowkit.skill` file (if you have one).
- Use it by asking for help with:
  - building a flow definition (`FlowBuilder`, `add_block_with`, `Assign`)
  - selecting and connecting flow.kit blocks (triggers, test.guide, control-flow, user-code)
  - running `main.py` to validate/execute/visualize a flow bundle

## Suggested development loop (in a flow bundle workspace)

- Edit the workflow in `flow_definition.py`.
- Validate after every change:
  - `python main.py --validate`
  - optionally: `python main.py --validate --validate-runs-unittests`
- Execute locally:
  - prepare `payload.json` next to `flow_definition.py`
  - create/update `.env` in the flow bundle root (do not commit it)
  - run: `python main.py --execute`
- Visualize the flow (experimental):
  - run: `python main.py --visualize`
  - renders as PlantUML from the generated `*.puml`

## Repo layout

- `SKILL.md`: primary skill instructions
- `references/flow-kit-snippets.code-snippets`: VS Code snippet templates for blocks (`.add_block_with(...)`, parameter identifiers, types, return types)
- `references/how_to_build_a_flow_definition.md`: condensed guide for building flow definitions (FlowBuilder / Assign / special blocks)
- `examples/batch_processing_usage.py`: full `BatchProcessing` example

## Requirements

- A local flow bundle workspace containing:
  - `flow_definition.py`, `main.py`, `.vscode/launch.json`, `payload.json`, `.env.sample`
  - the bundled `flow_kit/**/*.pyi` and `site-packages/**/*.pyi` stubs (for type/interface lookup)
