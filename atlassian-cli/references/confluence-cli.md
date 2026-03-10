# confluence-cli Full Command Reference

Tool: `confluence` by pchuri  
Repo: https://github.com/pchuri/confluence-cli  
Install: `npm install -g confluence-cli`  
Target: Confluence Cloud (*.atlassian.net)

---

## Environment Variables

```bash
export CONFLUENCE_URL="https://your-domain.atlassian.net"
export CONFLUENCE_USERNAME="your@email.com"
export CONFLUENCE_API_TOKEN="your_api_token"

# For scoped tokens (optional):
export CONFLUENCE_API_URL="https://api.atlassian.com/ex/confluence/CLOUD_ID/"
```

Get your Cloud ID: `https://your-domain.atlassian.net/_edge/tenant_info`

---

## Setup

```bash
confluence setup    # interactive wizard — detects Cloud vs Server, sets auth method
```

---

## confluence read

```bash
confluence read PAGE_ID [flags]

# Flags:
--format markdown    Output as Markdown (default: Confluence storage format)
--format html        Output as HTML

# Find PAGE_ID in the URL: .../pages/PAGE_ID/...
# Or from a full URL:
confluence read "https://your-domain.atlassian.net/wiki/viewpage.action?pageId=123456789"

# Examples:
confluence read 123456789
confluence read 123456789 --format markdown
```

---

## confluence search

```bash
confluence search "QUERY" [flags]

--limit int      Number of results (default: 10)
--space string   Limit to space key

# Examples:
confluence search "deployment runbook"
confluence search "API guide" --space DEV --limit 5
```

---

## confluence create

```bash
confluence create [flags]

--space string    Space key (required)
--title string    Page title (required)
--file string     Path to content file (.md, .html, or storage XML)
--parent string   Parent page ID
--format string   Content format: markdown | html | storage (default: auto-detect)

# Examples:
confluence create --space DEV --title "My New Page" --file page.md
confluence create --space DEV --title "Sprint Notes" --file notes.md --parent 98765432
confluence create --space OPS --title "Runbook" --file runbook.html --format html
```

---

## confluence update

```bash
confluence update PAGE_ID [flags]

--file string     Path to new content file
--title string    New page title
--format string   Content format: markdown | html | storage
--minor           Mark as minor edit (no notification to watchers)

# Examples:
confluence update 123456789 --file updated-notes.md
confluence update 123456789 --title "Renamed Page" --file content.md
confluence update 123456789 --file patch.md --minor
```

---

## confluence delete

```bash
confluence delete PAGE_ID

# Moves page to trash (recoverable from Confluence UI)
confluence delete 123456789
```

---

## confluence comments

```bash
# List comments
confluence comments PAGE_ID [flags]

--location string    footer | inline | all (default: all)
--format markdown    Output as markdown

confluence comments 123456789
confluence comments 123456789 --location footer --format markdown

# Add comment
confluence comment PAGE_ID [flags]

--content string     Comment text (Markdown supported)
--parent int         Reply to a specific comment ID
--location string    footer (default) | inline

confluence comment 123456789 --content "Looks good, approved!"
confluence comment 123456789 --content "See my note" --parent 998877   # reply
```

---

## confluence attachments

```bash
# List attachments
confluence attachments PAGE_ID [flags]

--pattern string    Filter by filename pattern (e.g. "*.png")
--limit int         Max results

# Download attachments
confluence attachments PAGE_ID --download --dest ./downloads [--pattern "*.pdf"]

# Upload attachment
confluence attach PAGE_ID --file ./diagram.png

# Delete attachment
confluence attachment-delete ATTACHMENT_ID

# Examples:
confluence attachments 123456789
confluence attachments 123456789 --pattern "*.png" --download --dest ./img/
confluence attach 123456789 --file architecture.png
```

---

## confluence export

```bash
# Export a page and all its attachments to a local folder
confluence export PAGE_ID --dest ./backup/

# Useful for backups before major edits
confluence export 123456789 --dest ./backup/sprint42/
```

---

## confluence properties

```bash
# Page content properties (key-value metadata)
confluence properties PAGE_ID                             # list all properties
confluence property PAGE_ID KEY                           # get one property
confluence property-set PAGE_ID KEY VALUE                 # set property
confluence property-delete PAGE_ID KEY                    # delete property
```

---

## Finding Page IDs

Page IDs appear in the URL:
```
https://your-domain.atlassian.net/wiki/spaces/SPACE/pages/123456789/Page+Title
                                                         ^^^^^^^^^^^
                                                         This is the PAGE_ID
```

Or use search:
```bash
confluence search "page title" --limit 1
# Output includes page ID
```

---

## Scripting Tips

```bash
# Create a page from a script-generated markdown file
cat > /tmp/release-notes.md << 'EOF'
# Release v2.1.0
- Fixed login bug
- Added dark mode
EOF
confluence create --space RELEASES --title "v2.1.0 Release Notes" --file /tmp/release-notes.md

# Update a page from CI pipeline
confluence update $PAGE_ID --file ./docs/deployment.md --minor

# Backup a page before editing
confluence export $PAGE_ID --dest ./backup/
```
