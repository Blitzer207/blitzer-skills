# ecu.test API Plugin

This plugin packages 11 ecu.test API skills as separate, routeable skills with bundled 2024.3 and 2026.1 references.

## Included Skills

- `ecu-test-com-api`
- `ecu-test-data-structures`
- `ecu-test-generator-api`
- `ecu-test-internal-api`
- `ecu-test-object-api`
- `ecu-test-report-api`
- `ecu-test-rest-api`
- `ecu-test-test-management-api`
- `ecu-test-tools-api`
- `ecu-test-trace-analysis-api`
- `ecu-test-user-utility-api`

## Codex

Codex plugin metadata lives in:

- `.codex-plugin/plugin.json`
- repository marketplace: `.agents/plugins/marketplace.json`

## Claude Code

Claude Code plugin metadata lives in:

- `.claude-plugin/plugin.json`
- repository marketplace: `.claude-plugin/marketplace.json`

After this repository is pushed to GitHub, add and install it in Claude Code with:

```text
/plugin marketplace add Blitzer207/blitzer-skills
/plugin install ecu-test-api@blitzer-skills
/reload-plugins
```

For local testing from this checkout:

```text
/plugin marketplace add C:\Users\leili\Desktop\Bitbucket-Repos\13-github-projects\07-blitzer-skills
/plugin install ecu-test-api@blitzer-skills
/reload-plugins
```

The plugin is self-contained: skill entrypoints and their references are under `skills/`, so installed plugin caches do not need files outside the plugin root.
