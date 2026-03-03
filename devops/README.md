# DevOps Skill

Evidence-driven DevOps specialist for server operations, troubleshooting, and deployment. This skill follows a rigorous diagnostic methodology to ensure no guesses are made and all actions are backed by evidence.

## 📚 Contents

- [SKILL.md](./SKILL.md): Core identity, philosophy, and safety framework.
- [diagnostics.md](./diagnostics.md): Step-by-step diagnostic workflows for common failure patterns.
- [blindspots.md](./blindspots.md): Protocols for handling information AI cannot reach (Cloud Console, ICP, etc.).
- [runbooks.md](./runbooks.md): Standard operating procedures for Docker, Nginx, Databases, and Security.

## 🚀 Key Features

1.  **Evidence-Driven Diagnosis**: Follows a "Golden Loop" of confirmation -> Resource Snapshot -> Service Check -> Log Analysis -> Correlation.
2.  **Blindspot Intelligence**: Proactively asks users about Cloud Security Groups, ICP filing status, and DNS propagation when technical evidence hits a wall.
3.  **Safety Gates**: Classified operations (Level 0-3) ensure high-risk actions (like deleting data or modifying core configs) always require user confirmation and a rollback plan.
4.  **Operational Excellence**: Includes ready-to-use commands for Nginx performance tuning, Docker cleanup, and DB health checks.

## 🛠 Installation

Copy this folder into your `.claude/skills/` directory:

```bash
cp -r devops/ ~/.claude/skills/
```

## 📄 License

This skill is part of the `blitzer-skills` collection.
