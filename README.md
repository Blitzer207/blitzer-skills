# blitzer-skills

A curated collection of Claude Code skills and AI agent capabilities.

## 📚 Available Skills

### [ecutest-api-skill](./ecutest-api-skill/)
Local ecu.test 2024.3 documentation knowledge base with Codex skill, references, and helper scripts.

**Features:**
- Multi-version support (2024.3+ including 2025.x)
- API and function lookup for ecu.test
- Search and scan utilities

**Usage:**
```bash
# Search API
python scripts/search_api.py --version 2025.4 --query AnalysisJobApi

# Scan documentation
python scripts/scan_docs.py --version 2025.4 tree --depth 2
```

---

### [testguide-flowkit-skill](./testguide-flowkit-skill/)
Create, debug, and optimize flow.kit-based `test.guide` workflows.

**Features:**
- Flow definition building with `FlowBuilder` and `add_block_with`
- Local validation and execution
- Flow visualization (experimental)

**Development Loop:**
```bash
# Validate
python main.py --validate

# Execute
python main.py --execute

# Visualize
python main.py --visualize
```

---

### [devops](./devops/)
Evidence-driven DevOps specialist for server operations, troubleshooting, and deployment.

**Features:**
- **Evidence-Driven**: Multi-layer diagnostics (Network -> System -> Service -> App)
- **Blindspot Awareness**: Explicit protocols for cloud console, ICP filing, and DNS issues
- **Safety First**: 4-level operation safety framework with confirmation gates
- **Multi-Cloud Ready**: Patterns for Alibaba, Tencent, and Huawei Cloud

**Usage:**
```bash
# Register the skill
# Copy 'devops' folder to your .claude/skills/ directory
```

---

### [atlassian-cli](./atlassian-cli/)
Atlassian 命令行工具集，覆盖 Jira、Confluence、Bitbucket 日常操作。

**Features:**
- `jira` CLI — Issues、Epics、Sprints 管理
- `confluence` CLI — Pages、Comments、Attachments 管理
- `bkt` CLI — Repos、PRs、Branches、Pipelines 管理
- 支持 Atlassian Cloud 和 Data Center

**Usage:**
```bash
# Jira — 查询我的 issues
jira issue list -a$(jira me)

# Confluence — 发布 Markdown 到页面
confluence create --space DEV --title "My Page" --file page.md

# Bitbucket — 创建 PR
bkt pr create --title "feat: add cache" --source feature/cache --target main
```

---

### [ecutest-code](./ecutest-code/)
用 `ecutest_code` 库编写 ecu.test Python 自动化测试。

**Features:**
- `ToolAccess` 三态状态机生命周期管理
- 变量注册（model_var、meas_var、bus_signal）、job/diag 调用、recording
- pytest fixture 模板（函数式 / 类式）
- test.guide 上传插件集成
- LSP 驱动的 API 验证工作流

**Requirements:** Python 3.12+，ecu.test 2026.1+

---

## 🚀 Installation

To use these skills in your tool (Claude Code / Cursor / Codex):

1. Copy the desired skill folder into your skills directory
2. Or install the packaged `.skill` file (if available)

## 📝 Contributing

Feel free to submit issues and pull requests to improve these skills.

## 📄 License

See individual skill directories for license information.
