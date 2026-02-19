---
name: "🐛 Anomaly Briefing"
description: "Found a deviation from the expected high-fidelity behavior?"
title: "fix: <brief_description>"
labels: ["bug"]
assignees: []

body:
  - type: markdown
    attributes:
      value: |
        ## 🛡️ Anomaly Report
        > [!WARNING]
        > Before reporting, please ensure this is not a known architectural limitation.

  - type: textarea
    id: context
    attributes:
      label: "Architectural Context"
      description: "What was the intended orchestration? (e.g. GUI Test on DuckDuckGo)"
      placeholder: "Intent: Standard GUI search verification..."
    validations:
      required: true

  - type: textarea
    id: reproduction
    attributes:
      label: "Surgical Reproduction"
      description: "Exact steps to trigger the anomaly."
      placeholder: |
        1. Run `run_tests.bat`
        2. Wait for GUI execution...
    validations:
      required: true

  - type: textarea
    id: outcomes
    attributes:
      label: "Technical Drift"
      description: "Expected vs Actual outcomes."
      placeholder: |
        Expected: Element visible in 5s.
        Actual: Timeout after 10s.
    validations:
      required: true

  - type: textarea
    id: evidence
    attributes:
      label: "Visual/Log Evidence"
      description: "Attach screenshots, console telemetry, or report fragments."
