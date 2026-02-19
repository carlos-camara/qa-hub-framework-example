# <div align="center">🤝 QA HUB CONTRIBUTION BLUEPRINT</div>

<div align="center">
  <p><i>Building the future of Next-Gen Orchestration & Engineering Intelligence.</i></p>
</div>

---

First off, **thank you** for considering contributing! Your engineering excellence is what drives this ecosystem forward.

> [!NOTE]
> These are guidelines designed to maintain high-fidelity engineering standards while keeping the contribution process friction-free.

## 📑 Table of Contents
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

## 🔄 The Contribution Workflow
1. **Branch Orchestration**: `feat/`, `fix/`, or `docs/`.
2. **Commit Chronology**: Follow [Conventional Commits](https://www.conventionalcommits.org/).
3. **Self-Verification**: Run `run_tests.bat` locally.
4. **Pull Request**: Open against `devel` branch with the provided template.

## 📝 Conventional Commits
- `feat`: A new feature or test scenario.
- `fix`: Resolution of a technical anomaly.
- `docs`: Documentation polish.
- `refactor`: Structural changes without functional drift.
- `test`: Verification suite updates.

---
<div align="center">
  <i>Thank you for architecting the future of QA Hub! 🚀</i>
</div>
