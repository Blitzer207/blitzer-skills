# jira-cli Full Command Reference

Tool: `jira` by ankitpokhrel  
Repo: https://github.com/ankitpokhrel/jira-cli  
Target: Jira Cloud (atlassian.net)

---

## Global Flags

| Flag | Description |
|------|-------------|
| `-p, --project` | Project key (overrides config default) |
| `-c, --config` | Config file path |
| `--debug` | Show debug output |

---

## jira issue

### list
```bash
jira issue list [flags]

# Key flags:
-p, --project string        Project key
-t, --type string           Issue type (Bug, Story, Task, Epic…)
-s, --status string         Filter by status
-a, --assignee string       Filter by assignee (use $(jira me) for self)
-P, --priority string       Filter by priority (High, Medium, Low)
-l, --label strings         Filter by label(s)
-q, --reporter string       Filter by reporter
    --jql string            Raw JQL query (overrides other filters)
    --paginate string        e.g. "20" or "10:50" (offset:limit)
    --plain                  Plain table output (pipe-friendly)
    --no-headers             Omit column headers
    --columns string         Comma-separated columns: KEY,SUMMARY,STATUS,ASSIGNEE,PRIORITY,CREATED,UPDATED,LABELS

# Examples:
jira issue list
jira issue list -p DEV -s "To Do" --plain --columns KEY,SUMMARY,STATUS
jira issue list --jql "sprint in openSprints() AND assignee = currentUser()"
jira issue list --paginate 50    # show 50 results
```

### view
```bash
jira issue view ISSUE_KEY [flags]

# Flags:
    --plain     Plain text output
-c, --comments  Show comments
    --debug     Debug output

# Examples:
jira issue view DEV-123
jira issue view DEV-123 --plain --comments
```

### create
```bash
jira issue create [flags]

# Flags:
-p, --project string     Project key (required)
-t, --type string        Issue type: Bug | Story | Task | Epic | Sub-task
-s, --summary string     Issue title/summary
-b, --body string        Description body
-P, --priority string    Priority: Highest | High | Medium | Low | Lowest
-a, --assignee string    Assignee username
-l, --label strings      Labels (repeatable)
    --fix-version        Fix version
    --parent string      Parent issue key (for sub-tasks)
    --no-input           Skip interactive prompts (requires -s flag)

# Examples:
jira issue create -p DEV -t Bug -s "Login crash on mobile" -P High
jira issue create -p DEV -t Story -s "User auth" -b "Implement OAuth2" -a johndoe
jira issue create    # fully interactive wizard
jira issue create -p DEV -t Task -s "Deploy v2.0" --no-input
```

### edit
```bash
jira issue edit ISSUE_KEY [flags]

# Flags:
-s, --summary string     New summary
-b, --body string        New description
-P, --priority string    New priority
-a, --assignee string    New assignee
-l, --label strings      Add labels
    --no-input           Non-interactive (apply flags directly)

# Examples:
jira issue edit DEV-123 -s "Updated title" --no-input
jira issue edit DEV-123    # interactive editor
```

### move (transition)
```bash
jira issue move ISSUE_KEY STATUS [flags]

# STATUS must match an available transition name exactly (case-insensitive)
# Common statuses: "To Do", "In Progress", "In Review", "Done", "Blocked"

# Examples:
jira issue move DEV-123 "In Progress"
jira issue move DEV-123 Done
```

### assign
```bash
jira issue assign ISSUE_KEY ASSIGNEE

# Use 'x' to unassign
jira issue assign DEV-123 johndoe
jira issue assign DEV-123 x          # unassign
jira issue assign DEV-123 $(jira me) # assign to self
```

### comment
```bash
jira issue comment add ISSUE_KEY [flags]

-m, --comment string    Comment body (if omitted, opens editor)

# Examples:
jira issue comment add DEV-123 -m "Fixed in commit abc123"
jira issue comment add DEV-123    # opens $EDITOR
```

### clone
```bash
jira issue clone ISSUE_KEY [flags]

# Clones the issue with same fields
-s, --summary string    Override summary for clone
-p, --project string    Clone to different project

jira issue clone DEV-123
jira issue clone DEV-123 -s "Clone of login bug" -p OPS
```

### link
```bash
jira issue link ISSUE_KEY LINK_TYPE TARGET_ISSUE_KEY

# LINK_TYPE examples: "blocks", "is blocked by", "relates to", "duplicates"
jira issue link DEV-123 blocks DEV-124
jira issue link DEV-123 "relates to" DEV-99
```

### delete
```bash
jira issue delete ISSUE_KEY [--cascade]

jira issue delete DEV-123
jira issue delete DEV-123 --cascade    # also delete sub-tasks
```

---

## jira epic

```bash
jira epic list -p DEV                    # list all epics
jira epic create -p DEV -s "Q3 Features" # create epic
jira epic add EPIC_KEY DEV-101 DEV-102   # add issues to epic
jira epic remove DEV-101                  # unlink issue from epic
```

---

## jira sprint

```bash
jira sprint list -p DEV                  # list sprints
jira sprint list -p DEV --table          # table view
jira sprint add SPRINT_ID DEV-101        # add issue to sprint
```

---

## jira project

```bash
jira project list                        # list all accessible projects
```

---

## jira me

```bash
jira me                                  # print current user's account ID
# Useful in scripts: jira issue assign DEV-123 $(jira me)
```

---

## jira open

```bash
jira open DEV-123                        # open issue in browser
jira open -p DEV                         # open project in browser
```

---

## Output Tips for Scripting

```bash
# Machine-readable plain output for shell scripting:
jira issue list --plain --no-headers --columns KEY,STATUS

# Pipe to grep, awk, etc:
jira issue list --plain --no-headers --columns KEY,SUMMARY | grep "crash"

# Count results:
jira issue list --plain --no-headers | wc -l
```
