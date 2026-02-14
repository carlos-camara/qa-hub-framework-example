# 🧪 QA Hub Framework Example

<div align="center">
  <img src="assets/logo.png" width="180" alt="QA Hub Logo">
  
  ### Better Testing • Faster Feedback • Total Confidence
  
  [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](https://opensource.org/licenses/MIT)
  [![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg?style=flat-square)](https://www.python.org/downloads/release/python-3100/)
  [![Lint Status](https://github.com/carlos-camara/qa-hub-framework-example/actions/workflows/lint.yml/badge.svg?style=flat-square)](https://github.com/carlos-camara/qa-hub-framework-example/actions/workflows/lint.yml)
  [![Tests Status](https://github.com/carlos-camara/qa-hub-framework-example/actions/workflows/tests.yml/badge.svg?style=flat-square)](https://github.com/carlos-camara/qa-hub-framework-example/actions/workflows/tests.yml)
  
  **A premier reference implementation for the QA Hub Framework.**
</div>

---

## 🌟 Overview

The **QA Hub Framework Example** showcases how to build world-class, hybrid automation suites (API + GUI) using specialized **QA Hub** patterns. This repository serves as a blueprint for engineering leads and specialized QA engineers who seek to bridge the gap between technical excellence and business value.

## 🏗️ Technical Architecture

This project strictly adheres to the **QA Hub Decoupled Architecture**, ensuring that test logic remains independent of implementation details and environment configurations.

```mermaid
graph TD
    subgraph "Scenario Layer"
        F[Gherkin Features]
    end
    subgraph "Implementation Layer"
        S[Step Definitions]
        E[Environment Hooks]
    end
    subgraph "Data & Locators"
        P[YAML Page Objects]
        C[Config YAMLs]
    end
    subgraph "QA Hub Core"
        QA[Framework Engine]
    end

    F --> S
    S --> QA
    QA --> P
    QA --> C
    E --> QA
```

## 🎯 Value Propositions

- **🚀 Velocity**: Out-of-the-box support for parallel execution and optimized CI/CD pipelines.
- **🧩 Composability**: Leverage existing framework steps or create your own with minimal boilerplate.
- **📊 Observability**: Built-in `ContextualLogger` and automatic artifact generation on failures.
- **🛡️ Quality Gates**: Standardized linting and regression testing integrated into every Pull Request.

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/carlos-camara/qa-hub-framework-example

# Install everything with one command
pip install -r requirements.txt
```

### 2. Execution Registry

| Target | Core Command |
| :--- | :--- |
| **GUI Context** | `python -m qa_framework.cli run --path features/duckduckgo/gui --tags '@smoke'` |
| **API Context** | `python -m qa_framework.cli run --path features/duckduckgo/api --tags '@smoke'` |

## 📁 Repository Blueprint

```text
├── .github/             # Modular CI/CD & Project Governance
├── assets/              # Branding & Visual Identity
├── features/
│   ├── config/          # Environment-driven Configuration
│   ├── duckduckgo/      # Domain-specific Scenarios
│   ├── page_objects/    # Zero-Code YAML Locators (POM)
│   ├── steps/           # Reusable Step Logic
│   └── environment.py   # Global Hook Registry
└── docs/                # Technical Documentation & Guides
```

## 🔧 Developer Experience (DX)

- **Local Validation**: Run `lint_local.bat` to ensure code compliance before pushing.
- **Self-Healing Dependencies**: Automated weekly updates via **Dependabot**.
- **Guided Contributions**: Clear `CONTRIBUTING.md` and Issue Templates for seamless collaboration.
- **API/GUI Step Library**: Reference `docs/steps.md` for the full Gherkin vocabulary.

---

<div align="center">
  <i>Designed & Engineered by <b>[Carlos Cámara](https://github.com/carlos-camara)</b></i>
</div>
