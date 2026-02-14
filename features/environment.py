
import os
from qa_framework.utils.hooks import FrameworkHooks

# 2. Hooks Delegation
def before_all(context):
    FrameworkHooks.bootstrap(context, default_lang="en")

def before_scenario(context, scenario):
    # Skip browser initialization for API tests
    tags = list(scenario.tags) + list(scenario.feature.tags)
    if 'api' in tags or 'API' in tags:
        return
        
    FrameworkHooks.before_scenario(context, scenario)

def after_step(context, step):
    # Capture screenshots on failure (Only for GUI tests with driver)
    if hasattr(context, 'driver') and context.driver:
        screenshots_dir = os.path.join(os.getcwd(), "test_results", "screenshots")
        FrameworkHooks.handle_step_failure(context, step, screenshots_dir)

def after_scenario(context, scenario):
    tags = list(scenario.tags) + list(scenario.feature.tags)
    is_api = 'api' in tags or 'API' in tags

    if not is_api:
        FrameworkHooks.after_scenario(context, scenario)

def after_feature(context, feature):
    FrameworkHooks.after_feature(context, feature)

def after_all(context):
    FrameworkHooks.teardown(context)
