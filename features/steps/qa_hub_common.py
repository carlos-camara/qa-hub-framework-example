from behave import given, when, then, step
from qa_framework.steps.common_steps import *
from qa_framework.steps.gui_steps import *
from qa_framework.steps.api_steps import *
from qa_framework.utils.logger import ContextualLogger
import time


# ---------------------------------------------------------
# Custom Steps for Missing Framework Functionality
# ---------------------------------------------------------


@step('I handle the consent popup')
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
