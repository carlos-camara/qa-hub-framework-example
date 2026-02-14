<div align="center">

# 🧪 QA Hub Framework Example

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg?style=flat-square)](https://www.python.org/downloads/release/python-3100/)
[![Lint Status](https://github.com/carlos-camara/qa-hub-framework-example/actions/workflows/lint.yml/badge.svg?style=flat-square)](https://github.com/carlos-camara/qa-hub-framework-example/actions/workflows/lint.yml)
[![Tests Status](https://github.com/carlos-camara/qa-hub-framework-example/actions/workflows/tests.yml/badge.svg?style=flat-square)](https://github.com/carlos-camara/qa-hub-framework-example/actions/workflows/tests.yml)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=flat-square)](https://github.com/carlos-camara/qa-hub-framework-example/graphs/commit-activity)

**A professional, minimal example of how to use QA Hub Framework to validate web applications.**

[Key Features](#-key-features) • [Quick Start](#-quick-start) • [Project Structure](#-project-structure) • [CI/CD](#-cicd)

---
</div>

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

#### 🖥️ GUI Verification
```bash
python -m qa_framework.cli run --path features/duckduckgo/gui --tags @smoke
```

#### 🌐 API Verification
```bash
python -m qa_framework.cli run --path features/duckduckgo/api --tags @smoke
```

## 🏗️ Project Structure

```text
├── .github/
│   ├── workflows/       # Modular CI/CD Pipelines (Lint & Tests)
│   └── pull_request_template.md
├── features/
│   ├── config/          # Environment & Browser Configuration
│   ├── duckduckgo/      # DuckDuckGo Test Scenarios (API & GUI)
│   ├── page_objects/    # Zero-Code YAML Locators
│   ├── steps/           # Shared & Custom Step Definitions
│   └── environment.py   # Global Framework Hooks
├── .gitignore
├── requirements.txt
└── README.md
```

## 🧩 Key Features

*   **Zero-Code Page Objects**: Define locators in clean YAML. No more brittle selector classes.
*   **Human-Readable Verification**: Gherkin steps designed for clarity and reusability.
*   **Hybrid Testing Engine**: Seamless orchestration of API and Selenium/Playwright tests.
*   **Contextual Logging**: Automatic traceability with built-in `ContextualLogger`.
*   **Automated Proof of Work**: Automatic screenshots and reports on execution failures.

## 🤖 CI/CD Infrastructure

The project utilizes modular GitHub Actions for automated quality gates:
- **💅 Lint Codebase**: Automated style checks using global standards.
- **🧪 Standard Test Suite**: Automated execution of all smoke tests on every PR.

---

<div align="center">
  Built with ❤️ by <b>Carlos Camara</b>
</div>