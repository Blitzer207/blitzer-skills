---
name: atlassian-cli
description: >
  Use this skill whenever the user wants to interact with Jira, Confluence, or Bitbucket via the
  command line (CLI). Trigger on any request involving: installing jira-cli, confluence-cli, or bkt
  tools, writing shell commands or scripts to create/update/query Jira issues, epics, sprints, or
  transitions, publishing or updating Confluence pages from Markdown files, managing pull requests,
  branches, repos, or pipelines in Bitbucket from the terminal, managing Atlassian Cloud or Data Center
  resources from a terminal or CI pipeline, or troubleshooting CLI authentication with API tokens.
  Also trigger for requests like "how do I create a Jira issue from the terminal", "upload markdown to
  Confluence", "script Jira status transitions", "create a PR in Bitbucket from CLI", "automate
  Atlassian from shell", "bkt pr", "bkt repo", or "Bitbucket CLI keyring timeout".
  Always use this skill — don't guess CLI syntax from memory.
---

# Atlassian CLI Skill

Covers three CLI tools for **Jira**, **Confluence**, and **Bitbucket** daily operations:

| Tool | Command | Purpose | Platform |
|------|---------|---------|----------|
| jira-cli (ankitpokhrel) | `jira` | Issues, epics, sprints | Jira Cloud |
| confluence-cli (pchuri) | `confluence` | Pages, comments, attachments | Confluence Cloud |
| bitbucket-cli (avivsinai) | `bkt` | Repos, PRs, branches, pipelines | Bitbucket Cloud + Data Center |

For detailed command references, see:
- `references/jira-cli.md` — full Jira CLI command reference
- `references/confluence-cli.md` — full Confluence CLI command reference
- `references/bkt-commands.md` — full Bitbucket CLI command reference

---

## 1. Installation

### jira-cli
```bash
# Windows install 
# 1. Download latest release from https://github.com/ankitpokhrel/jira-cli/releases
# 2. Unzip and add jira.exe to PATH
# 3. verify with `jira version`
```

### confluence-cli
```bash
# Via npm (requires Node.js ≥16)
npm install -g confluence-cli

# Verify
confluence --version
```

### bkt (Bitbucket CLI)
```bash
# macOS/Linux — via Homebrew
brew install avivsinai/tap/bitbucket-cli

# Windows — via Scoop
scoop bucket add avivsinai https://github.com/avivsinai/scoop-bucket
scoop install bitbucket-cli

# Go
go install github.com/avivsinai/bitbucket-cli/cmd/bkt@latest

# Verify
bkt --version
```

---

## 2. Authentication Setup

### Jira — jira-cli (Cloud)
```bash
# 1. Get API token: https://id.atlassian.com/manage-profile/security/api-tokens
export JIRA_API_TOKEN="your_token_here"   # add to ~/.zshrc or ~/.bashrc

# 2. Initialize config (interactive wizard)
jira init
# → Select: Cloud
# → Enter: your-domain.atlassian.net      ← no https:// prefix
# → Enter: your email
# → Enter: default project key (e.g. DEV)
```
Config saved to: `~/.config/.jira/.config.yml`

### Confluence — confluence-cli (Cloud)
```bash
# 1. Get API token: https://id.atlassian.com/manage-profile/security/api-tokens

# 2. Run interactive setup
confluence init
# → Protocol:          HTTPS
# → Confluence domain: your-domain.atlassian.net   ← no https:// prefix
# → REST API path:     /wiki/rest/api
# → Auth method:       Basic (credentials)
# → Email:             your@email.com
# → API token:         your_token_here
```
Config saved to: `~/.confluence-cli/config.json`

### Bitbucket — bkt (Cloud)
```bash
# 1. Create API token: https://id.atlassian.com/manage-profile/security/api-tokens
#    Select "Bitbucket" as application, required scope: Account: Read

# 2. Login
bkt auth login https://bitbucket.org --kind cloud --username your@email.com --token <api-token>

# 3. Create context
bkt context create cloud-team --host bitbucket.org --workspace myworkspace --set-active

# Check status
bkt auth status
```

### Bitbucket — bkt (Data Center)
```bash
bkt auth login https://bitbucket.example.com --username alice --token <PAT>
bkt context create dc-prod --host bitbucket.example.com --project ABC --set-active
```

---

## 3. Quick Reference — Jira Daily Operations

> See `references/jira-cli.md` for full flag details.

```bash
# --- QUERY ---
jira issue list                                    # list issues (current project)
jira issue list -p PROJ                            # specific project
jira issue list -a$(jira me)                       # assigned to me
jira issue list -s"In Progress"                    # by status
jira issue list --jql "project=DEV AND priority=High AND updatedDate > -7d"
jira issue view DEV-123                            # view issue detail
jira issue view DEV-123 --plain                    # plain text output

# --- CREATE ---
jira issue create -p DEV -t Bug -s "Fix login crash"
jira issue create -p DEV -t Story -s "User auth" -b "Description here" --priority High
jira issue create                                  # interactive wizard

# --- UPDATE ---
jira issue edit DEV-123 -s "New title" --no-input
jira issue assign DEV-123 myusername
jira issue assign DEV-123 x                        # unassign

# --- TRANSITIONS ---
jira issue move DEV-123 "In Progress"
jira issue move DEV-123 "Done"

# --- COMMENTS ---
jira issue comment add DEV-123 -m "Deployed to staging"

# --- EPICS & SPRINTS ---
jira epic list -p DEV
jira epic create -p DEV -s "Q3 Auth Epic"
jira sprint list -p DEV
jira sprint add SPRINT_ID DEV-123 DEV-124
```

---

## 4. Quick Reference — Confluence Daily Operations

> See `references/confluence-cli.md` for full flag details.

```bash
# --- READ & SEARCH ---
confluence read 123456789                          # read page by ID
confluence read 123456789 --format markdown        # output as markdown
confluence search "deployment guide" --limit 10

# --- CREATE & UPDATE ---
confluence create --space DEV --title "My Page" --file page.md
confluence create --space DEV --title "Notes" --file notes.md --parent 98765432
confluence update 123456789 --file updated.md
confluence update 123456789 --title "New Title" --file content.md

# --- DELETE ---
confluence delete 123456789                        # move to trash

# --- COMMENTS ---
confluence comments 123456789                      # list comments
confluence comment 123456789 --content "LGTM!"     # add footer comment

# --- ATTACHMENTS ---
confluence attachments 123456789                   # list attachments
confluence attachments 123456789 --download --dest ./downloads
confluence attach 123456789 --file diagram.png     # upload attachment

# --- EXPORT / BACKUP ---
confluence export 123456789 --dest ./backup/
```

---

## 5. Quick Reference — Bitbucket Daily Operations

> See `references/bkt-commands.md` for full flag details.

```bash
# --- REPOS ---
bkt repo list
bkt repo view my-repo
bkt repo clone my-repo --ssh
bkt repo create new-repo --description "My service"

# --- PULL REQUESTS ---
bkt pr list --state OPEN
bkt pr view 42
bkt pr create --title "feat: add cache" --source feature/cache --target main --reviewer alice
bkt pr approve 42
bkt pr comment 42 --text "LGTM"
bkt pr merge 42
bkt pr checks 42 --wait                            # wait for CI to complete

# --- BRANCHES ---
bkt branch list
bkt branch create feature/my-feature --from main
bkt branch delete feature/old-stuff

# --- PIPELINES (Cloud only) ---
bkt pipeline run --ref main --var ENV=staging
bkt pipeline list
bkt pipeline logs <uuid>

# --- OUTPUT ---
bkt pr list --json | jq '.pull_requests[0].title'  # JSON for scripting
bkt pr list --yaml                                  # YAML output
```

---

## 6. Common Patterns

### Batch close Jira issues
```bash
for issue in DEV-101 DEV-102 DEV-103; do
  jira issue move "$issue" "Done"
  echo "Closed $issue"
done
```

### List my open Jira issues → file
```bash
jira issue list -a$(jira me) -s"To Do" --plain --no-headers \
  --columns KEY,SUMMARY,PRIORITY > my-issues.txt
```

### Publish Markdown file to Confluence
```bash
confluence create --space TEAM --title "Sprint 42 Notes" \
  --file sprint42.md --parent 98765432
```

### Update Confluence page from CI
```bash
confluence update $PAGE_ID --file README.md --minor
```

### Create Bitbucket PR and wait for CI
```bash
bkt pr create --title "fix: crash on login" --source fix/login --target main
PR_ID=$(bkt pr list --state OPEN --json | jq '.[0].id')
bkt pr checks $PR_ID --wait --timeout 10m
```

### JQL tips for daily use
```bash
jira issue list --jql "project=DEV AND updatedDate > -1d ORDER BY updated DESC"
jira issue list --jql "assignee=currentUser() AND issuetype=Bug AND status != Done"
jira issue list --jql "project=DEV AND sprint in openSprints()"
```

---

## 7. Troubleshooting

| Problem | Tool | Solution |
|---------|------|----------|
| `401 Unauthorized` | jira | Check `JIRA_API_TOKEN` is exported; use email as username for Cloud |
| `jira: command not found` | jira | Add `$GOPATH/bin` or `$HOME/go/bin` to `$PATH` |
| `confluence: command not found` | confluence | Run `npm install -g confluence-cli`; check Node ≥16 |
| Domain entered with `https://` | confluence | Re-run `confluence init`; enter only `your-domain.atlassian.net` |
| `403 Forbidden` | confluence | API token expired or wrong; test with `curl -u email:token URL` |
| `bkt: command not found` | bkt | Re-install; check `$PATH` includes Go bin or Scoop shims |
| `keyring timeout` | bkt | Set `BKT_KEYRING_TIMEOUT=2m` or `BKT_ALLOW_INSECURE_STORE=1` |
| Wrong project/workspace | any | Use explicit flags: `-p PROJECT`, `--workspace WORKSPACE`, `--context NAME` |
| Page not found | confluence | Verify page ID from URL: `.../pages/PAGE_ID/...` |
