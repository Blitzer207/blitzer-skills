# test.guide Plugin

This plugin packages two test.guide skills as separate, routeable skills with bundled local references.

## Included Skills

- `testguide-rest-api-skill`
- `testguide-flowkit-skill`

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
/plugin install test-guide@blitzer-skills
/reload-plugins
```

For local testing from this checkout:

```text
/plugin marketplace add C:\Users\leili\Desktop\Bitbucket-Repos\13-github-projects\07-blitzer-skills
/plugin install test-guide@blitzer-skills
/reload-plugins
```

The plugin is self-contained: skill entrypoints and their references are under `skills/`, so installed plugin caches do not need files outside the plugin root.
