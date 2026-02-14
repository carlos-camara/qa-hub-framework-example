<div align="center">

# 🧪 QA Hub Framework Example

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Lint Status](https://github.com/Carlos/qa-hub-framework-example/actions/workflows/lint.yml/badge.svg)](https://github.com/Carlos/qa-hub-framework-example/actions/workflows/lint.yml)
[![Tests Status](https://github.com/Carlos/qa-hub-framework-example/actions/workflows/tests.yml/badge.svg)](https://github.com/Carlos/qa-hub-framework-example/actions/workflows/tests.yml)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/Carlos/qa-hub-framework-example/graphs/commit-activity)

> **A professional, minimal example of how to use QA Hub Framework to validate web applications.**

[Key Features](#-key-features) • [Quick Start](#-quick-start) • [Project Structure](#-project-structure) • [CI/CD](#-cicd)

</div>

---

## 🌟 Overview

This project demonstrates a real-world implementation of the **QA Hub Framework** to test **DuckDuckGo Search** (GUI) and **DuckDuckGo Availability** (API). It serves as a blueprint for building scalable, maintainable, and readable automation suites.

## 🚀 Quick Start

### 1. Prerequisites
- **Python 3.10+**
- **Chrome Browser** (for GUI tests)

### 2. Installation
To install the project and the framework dependencies:

```bash
pip install -r requirements.txt
```

> [!NOTE]
> This command will automatically download and install the **latest version** of `qa-hub-framework` directly from GitHub.

### 3. Running Tests

#### 🖥️ Run GUI Tests (DuckDuckGo Search)
```bash
python -m qa_framework.cli run --path features/duckduckgo/gui/duckduckgo_interaction.feature --tags @smoke
```

#### 🌐 Run API Tests (Connectivity)
```bash
python -m qa_framework.cli run --path features/duckduckgo/api/duckduckgo_api.feature --tags @smoke
```

## 🏗️ Project Structure

```text
├── .github/
│   ├── workflows/       # CI Github Actions
│   └── pull_request_template.md
├── features/
│   ├── config/          # Configuration (Browser, Environment)
│   ├── duckduckgo/      # DuckDuckGo Test Suite
│   │   ├── api/         # API Test Scenarios
│   │   └── gui/         # GUI Test Scenarios
│   ├── page_objects/    # YAML Locators (Zero-Code POM)
│   ├── steps/           # Custom step definitions
│   └── environment.py   # Framework Hooks (The "Glue")
├── .gitignore
├── requirements.txt
└── README.md
```

## 🧩 Key Features Demonstrated

1.  **Zero-Code Page Objects**: Define locators in clean YAML files. No more brittle selector classes.
2.  **English-like Steps**: Feature files that stakeholders can actually read.
3.  **Hybrid Testing**: Seamlessly mix API and GUI checks in the same project.
4.  **Integrated Logging**: Automatic `ContextualLogger` support for crystal-clear test logs.
5.  **Failure Analysis**: Automatic screenshots on GUI failures.

## 🤖 CI/CD

The project includes a GitHub Actions workflow (`.github/workflows/ci.yml`) that automatically:
- Lints the codebase using `black` and `flake8`.
- Runs Smoke Tests (API & GUI) on every Push and Pull Request.

---

<p align="center">
  Built by Carlos Camara
</p>