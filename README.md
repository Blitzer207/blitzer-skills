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

## 🚀 Installation

To use these skills in your tool (Claude Code / Cursor / Codex):

1. Copy the desired skill folder into your skills directory
2. Or install the packaged `.skill` file (if available)

## 📝 Contributing

Feel free to submit issues and pull requests to improve these skills.

## 📄 License

See individual skill directories for license information.
