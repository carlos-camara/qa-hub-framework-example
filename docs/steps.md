# 📖 Step Reference Guide

This document provides a reference of the most common Gherkin steps available in the **QA Hub Framework** and the custom steps specific to this example project.

## 🛠️ Common Framework Steps

### 🖥️ GUI / Web Interaction
- `Given I navigate to "{url}"` - Navigates to a specific URL.
- `Then the "{page_name}" page is displayed` - Sets the current page context and verifies its visibility.
- `When I type "{text}" into the "{element_name}"` - Types text into a specific element on the current page.
- `And I click on the "{element_name}"` - Clicks a specific element.
- `Then the text of "{element_name}" should be "{text}"` - Verifies the text content of an element.
- `And I wait for "{seconds}" seconds` - Explicit wait.

### 🌐 API Interaction
- `When I send a GET request to "{endpoint}"` - Sends an API GET request.
- `Then the response status should be "{status_code}"` - Verifies the HTTP status code.

## 🧪 Example Specific Steps (`features/steps/qa_hub_common.py`)

- `Given I handle the consent popup` - Specialized step for DuckDuckGo/European consent banners.
- `When I store the text of "{element_name}" as "{variable_name}"` - Captures UI text for later use or validation.

---

> [!TIP]
> Use these steps as building blocks to create complex and readable test scenarios.
