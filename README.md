# blitzer-skills

A curated collection of Claude Code and Codex plugins, skills, and AI agent capabilities.

## Plugin Marketplaces

This repository exposes plugin marketplace metadata for both Codex and Claude Code.

### Claude Code

After the changes are pushed to GitHub:

```text
/plugin marketplace add Blitzer207/blitzer-skills
/plugin install ecu-test-api@blitzer-skills
/plugin install test-guide@blitzer-skills
/reload-plugins
```

For local testing from this checkout:

```text
/plugin marketplace add C:\Users\leili\Desktop\Bitbucket-Repos\13-github-projects\07-blitzer-skills
/plugin install ecu-test-api@blitzer-skills
/plugin install test-guide@blitzer-skills
/reload-plugins
```

Claude Code marketplace file: `.claude-plugin/marketplace.json`

### Codex

Codex marketplace file: `.agents/plugins/marketplace.json`

## Plugins

### [ecu-test-api](./plugins/ecu-test-api/)

Plugin bundle for ecu.test API and automation skills with bundled references.

Includes:
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
- `ecutest-code`

### [test-guide](./plugins/test-guide/)

Plugin bundle for test.guide REST API automation and flow.kit workflow development.

Includes:
- `testguide-rest-api-skill`
- `testguide-flowkit-skill`

## Standalone Skills

### [devops](./devops/)

Evidence-driven DevOps specialist for server operations, troubleshooting, and deployment.

Features:
- Evidence-driven diagnostics across network, system, service, and app layers
- Blindspot protocols for cloud console, ICP filing, and DNS issues
- Safety-first operation guidance
- Multi-cloud operation patterns

### [atlassian-cli](./atlassian-cli/)

Atlassian CLI guidance for Jira, Confluence, and Bitbucket daily operations.

Features:
- `jira` CLI issue, epic, and sprint workflows
- `confluence` CLI page, comment, and attachment workflows
- `bkt` CLI repository, pull request, branch, and pipeline workflows
- Atlassian Cloud and Data Center support

## Installation

Use plugins when possible. They are self-contained under `plugins/` and include their own skill references.

For standalone skills, copy the desired skill folder into your tool's skills directory.

## Contributing

Feel free to submit issues and pull requests to improve these plugins and skills.

## License

See individual plugin and skill directories for license information.
