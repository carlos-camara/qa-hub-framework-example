<div align="center">
  <h1>📖 Step Reference Guide</h1>
  <p><i>High-fidelity blueprint for Gherkin-driven technical validation.</i></p>
</div>

This document provides a reference of the most common Gherkin steps available in the **QA Hub Framework** and the custom steps specific to this example project.

## 🛠️ Common Framework Steps

### 🖥️ GUI / Web Interaction
- `Given I navigate to "{url}"` - Navigates to a specific URL.
- `Then the "{page_name}" page is displayed` - Sets the current page context and verifies its visibility.
- `When I type "{text}" into the "{element_name}"` - Types text into a specific element on the current page.
- `And I click on the "{element_name}"` - Clicks a specific element.
- `Then the text of "{element_name}" should be "{text}"` - Verifies the text content of an element.
- `And I wait until the text "{text}" is visible` - **[NEW]** Adaptive wait for asynchronous content with failure diagnostics.
- `And I wait for "{seconds}" seconds` - Explicit wait (use sparingly).

### 🌐 API Interaction
- `When I send a GET request to "{endpoint}"` - Sends an API GET request.
- `Then the response status should be "{status_code}"` - Verifies the HTTP status code.

## 🧪 Example Specific Steps (`features/steps/qa_hub_common.py`)

- `Given I handle the consent popup` - Specialized step for DuckDuckGo/European consent banners.
- `When I store the text of "{element_name}" as "{variable_name}"` - Captures UI text for later use or validation.

---

> [!TIP]
> **Adaptive Waiting**: Always prefer `I wait until the text "{text}" is visible` over explicit sleeps. It makes your tests faster and more resilient by continuing as soon as the element appears.
>
> [!NOTE]
> All steps support **I18n tokens** ([LANG:key]) and **Variables** ([UUID], [NOW]) automatically via the framework's token resolution engine.
