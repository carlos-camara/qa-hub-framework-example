# <div align="center">🤝 QA HUB CONTRIBUTION BLUEPRINT</div>

<div align="center">
  <p><i>Building the future of Next-Gen Orchestration & Engineering Intelligence.</i></p>
</div>

---

First off, **thank you** for considering contributing! Your engineering excellence is what drives this ecosystem forward.

> [!IMPORTANT]
> **Elite Quality Gate**: All code contributions must pass the local `pre-commit` hooks and the CI `Lint - Super-Linter` pipeline before being considered for merge.

## 📑 Registry of Guidelines
- [Code of Conduct](#-code-of-conduct)
- [Technical Standards](#-technical-standards)
- [The Contribution Workflow](#-the-contribution-workflow)
- [Conventional Commits](#-conventional-commits)

---

## 📜 Code of Conduct
This project adheres to a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## 🎨 Technical Standards
- **Framework Priority**: Always utilize the **[QA Hub Framework](https://github.com/carlos-camara/qa-hub-framework)** core before implementing local logic.
- **Generic Step Strategy**: Leverage standardized steps for text validation, interaction, and visual audits.
- **Registry-Driven POM**: Externalize all selectors in the YAML-driven locator files.
- **Intelligence Synchronization**: Ensure any new logic is compatible with the `pr-intelligence` and `pr-churn-analyzer` actions.

## 🔄 The Contribution Workflow
1. **Branch Orchestration**: Use semantic naming: `feat/`, `fix/`, `docs/`, or `refactor/`.
2. **Commit Chronology**: Follow [Conventional Commits](https://www.conventionalcommits.org/) standards.
3. **Self-Verification**: 
   - Run `.\lint_local.bat` to verify zero-debt standards.
   - Run `.\run_tests.bat` locally to ensure no functional drift.
4. **Pull Request**: Open against the `devel` branch with a comprehensive description.

## 📝 Conventional Commits
- `feat`: A new feature or test scenario.
- `fix`: Resolution of a technical anomaly.
- `docs`: Documentation polish or updates.
- `refactor`: Structural changes without functional drift.
- `test`: Verification suite updates.

---
<div align="center">
  <i>Thank you for architecting the future of QA Hub! 🚀</i>
</div>
