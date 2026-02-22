<div align="center">
  <h1>📔 Project Changelog</h1>
  <p><i>High-fidelity documentation of the project's architectural evolution and technical milestones.</i></p>
</div>

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.2.0] - 2026-02-19

### 🚀 Ecosystem Evolution & Intelligence Generalization
- **PR Intelligence Integration**: Migrated local scripts to the global `carlos-camara/qa-hub-actions/pr-intelligence` action.
- **Churn Analysis**: Integrated `carlos-camara/qa-hub-actions/pr-churn-analyzer` for automated test debt detection.
- **Framework Core Synchronization**: Adopted the new robust `wait_for_text_visible` core step, removing ~200 lines of local custom logic.
- **Elite Standards Refactor**: Modernized all repository documentation (`README`, `CONTRIBUTING`, `SECURITY`, `CoC`) to high-fidelity "Elite" status.

### Added
- High-fidelity YAML Issue Forms for Bug Reports and Feature Requests.
- Pre-commit hooks for local code quality enforcement.
- Dependabot configuration for automated maintenance.

## [1.1.0] - 2026-02-18

### Changed
- Standardized S3 report deployment via `deploy-reports-s3` action.
- Unified Linting pipeline using `qa-hub-actions/lint-codebase`.
- Concurrency and timeout controls for all CI/CD workflows.
- Permissions hardening for all automated jobs.
