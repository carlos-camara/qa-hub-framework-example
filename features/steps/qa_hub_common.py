from behave import given, when, then
from qa_framework.steps.common_steps import *
from qa_framework.steps.gui_steps import *
from qa_framework.steps.api_steps import *
from qa_framework.utils.logger import ContextualLogger
import time


# ---------------------------------------------------------
# Custom Steps for Missing Framework Functionality
# ---------------------------------------------------------

@given('I handle the consent popup')
def step_handle_consent(context):
    """
    Conditionally click the consent button if it appears.
    This is a common requirement for European based tests.
    """
    try:
        # We try to find the 'cookie_button' in the 'duckduckgo_home' page object
        btn = get_element_from_page_object(context, 'cookie_button', 'duckduckgo_home')
        if btn and btn.is_displayed():
            ContextualLogger.info("Consent popup detected. Clicking to accept.", context)
            btn.click()
            time.sleep(1)
    except Exception as e:
        ContextualLogger.debug(f"Consent popup not found or could not be clicked: {str(e)}", context)
        pass  # If not found or not clickable, we ignore and continue

@then('I wait until the text "{text}" is visible')
def step_wait_for_text_visible(context, text):
    """
    Wait until the specified text is present in the page body.
    Useful for ensuring asynchronous content has loaded.
    """
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    
    timeout = 15
    ContextualLogger.info(f"Waiting up to {timeout}s for text: '{text}'", context)
    
    def check_text(driver):
        try:
            body_text = driver.find_element(By.TAG_NAME, "body").text
            if text.lower() in body_text.lower():
                return True
            # Log current state periodically if not found (debugging)
            return False
        except Exception:
            return False

    try:
        WebDriverWait(context.driver, timeout).until(
            check_text,
            message=f"Timed out waiting for text '{text}'"
        )
    except Exception as e:
        # Diagnostic capture on failure
        current_url = context.driver.current_url
        current_title = context.driver.title
        ContextualLogger.error(f"Wait Failed. URL: {current_url}, Title: {current_title}", context)
        raise e
