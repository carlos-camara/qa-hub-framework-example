# 🧪 QA Hub Framework Example

<div align="center">
  <img src="https://raw.githubusercontent.com/carlos-camara/qa-hub-framework-example/main/assets/logo.png" width="160" alt="QA Hub Logo">
  
  ### Better Testing. Faster Feedback. Total Confidence.
  
  [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](https://opensource.org/licenses/MIT)
  [![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg?style=flat-square)](https://www.python.org/downloads/release/python-3100/)
  [![Lint Status](https://github.com/carlos-camara/qa-hub-framework-example/actions/workflows/lint.yml/badge.svg?style=flat-square)](https://github.com/carlos-camara/qa-hub-framework-example/actions/workflows/lint.yml)
  [![Tests Status](https://github.com/carlos-camara/qa-hub-framework-example/actions/workflows/tests.yml/badge.svg?style=flat-square)](https://github.com/carlos-camara/qa-hub-framework-example/actions/workflows/tests.yml)
  
  **A world-class blueprint for modern automated quality assurance.**
</div>

---

## 🌟 Overview

The **QA Hub Framework Example** is a premium reference implementation designed to showcase how to build scalable, hybrid automation suites (API + GUI) using the **QA Hub Framework**. 

Built for speed, readability, and maintainability, it provides a clean structure that bridges the gap between technical implementation and business requirements.

## 🎯 Key Pillars

| Pillar | Description |
| :--- | :--- |
| **🚀 Speed** | Parallel execution and optimized environment setup for rapid feedback. |
| **🧩 Modularity** | True separation of concerns with YAML-based Page Objects and shared steps. |
| **📊 Visibility** | Contextual logging and automated failure artifacts (screenshots, reports). |
| **🛡️ Health** | Integrated CI/CD gates for linting and regression testing. |

## 🚀 Getting Started

### 1. Simple Setup

```bash
# Clone the repository
git clone https://github.com/carlos-camara/qa-hub-framework-example
cd qa-hub-framework-example

# Install dependencies (Framework included)
pip install -r requirements.txt
```

### 2. Run your first test

| Target | Command |
| :--- | :--- |
| **GUI (Search)** | `python -m qa_framework.cli run --path features/duckduckgo/gui --tags '@smoke'` |
| **API (Connectivity)** | `python -m qa_framework.cli run --path features/duckduckgo/api --tags '@smoke'` |

## 🏗️ Premium Architecture

```text
├── .github/             # Modular CI/CD (Lint, Tests, Dependabot)
├── features/
│   ├── config/          # Centralized configuration
│   ├── duckduckgo/      # Domain-specific test scenarios
│   ├── page_objects/    # Zero-Code YAML Locators (POM)
│   ├── steps/           # Reusable Gherkin glue
│   └── environment.py   # Global framework lifecycle hooks
└── docs/                # Extended documentation (Step Reference, etc.)
```

## 🔧 Developer Experience (DX)

- **One-Click Linting**: Run `lint_local.bat` to verify your changes locally.
- **Auto-Updates**: Stay secure and current with built-in Dependabot integration.
- **Issue Templates**: Professional interaction with standardized contribution flows.

---

<p align="center">
  Built with excellence by <b>Carlos Camara</b>
</p>