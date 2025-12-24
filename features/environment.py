import os
import datetime
import json
import logging
import re
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.base_page import BasePage
from pages.book_store_page import BookStorePage
from pages.checkbox_page import CheckBoxPage
from pages.dynamic_properties_page import DynamicPropertiesPage
from pages.forms_page import FormsPage

logger = logging.getLogger(__name__)

# ---------------------- HELPER ----------------------
def valid_filename(name):
    """Replace invalid Windows filename characters with underscore"""
    return re.sub(r'[<>:"/\\|?*]', '_', name)

# ---------------------- BEFORE ALL ----------------------
def before_all(context):
    """Initialize project paths and load configuration"""
    logger.info("Starting test execution...")

    context.base_dir = os.getcwd()
    context.screenshots_dir = os.path.join(context.base_dir, "screenshots")
    os.makedirs(context.screenshots_dir, exist_ok=True)

    # Clean old screenshots
    for file in os.listdir(context.screenshots_dir):
        if file.endswith(".png"):
            os.remove(os.path.join(context.screenshots_dir, file))
    logger.info("Old screenshots cleaned")

    # Load config
    config_path = os.path.join(context.base_dir, "config", "config.json")
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path, "r") as f:
        context.config_data = json.load(f)

    context.base_url = context.config_data.get("base_url")
    logger.info(f"Base URL loaded: {context.base_url}")

# ---------------------- BEFORE SCENARIO ----------------------
def before_scenario(context, scenario):
    """Create a new browser instance per scenario"""
    try:
        options = Options()
        options.add_argument("--start-maximized")
        context.driver = webdriver.Chrome(options=options)
        context.driver.implicitly_wait(5)

        # Initialize page objects
        context.base_page = BasePage(context.driver)
        context.checkbox_page = CheckBoxPage(context.driver)
        context.dynamic_properties = DynamicPropertiesPage(context.driver)
        context.forms_page = FormsPage(context.driver)
        context.book_store_page = BookStorePage(context.driver)

        logger.info(f"Browser launched for scenario: {scenario.name}")

    except Exception:
        logger.exception("Failed to initialize browser")
        raise

# ---------------------- AFTER STEP ----------------------
def after_step(context, step):
    """Capture screenshot for step and attach to Allure"""
    try:
        if not hasattr(context, "driver"):
            return

        status = step.status.name.lower()

        # Only include timestamp for failed steps to avoid duplicates
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") if status == "failed" else ""
        safe_step_name = valid_filename(step.name.replace(' ', '_'))
        screenshot_name = f"{safe_step_name}_{status}"
        if timestamp:
            screenshot_name += f"_{timestamp}"
        screenshot_name += ".png"

        screenshot_path = os.path.join(context.screenshots_dir, screenshot_name)
        context.driver.save_screenshot(screenshot_path)

        # places step name in the Allure attachment as well
        attachment_name = valid_filename(f"{step.name} [{status}]")
        allure.attach.file(
            screenshot_path,
            name=attachment_name,
            attachment_type=allure.attachment_type.PNG
        )

        logger.info(f"Screenshot captured for step '{step.name}' [{status}]")

    except Exception:
        logger.exception("Failed to capture screenshot (ignored)")

# ---------------------- AFTER SCENARIO ----------------------
def after_scenario(context, scenario):
    """Attach failure screenshot and quit browser"""
    try:
        if scenario.status == "failed" and hasattr(context, "driver"):
            allure.attach(
                context.driver.get_screenshot_as_png(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
    except Exception:
        logger.exception("Failed to attach failure screenshot")
    finally:
        if hasattr(context, "driver"):
            context.driver.quit()
            logger.info(f"Browser closed for scenario: {scenario.name}")

# ---------------------- AFTER ALL ----------------------
def after_all(context):
    """Optional: finalize test execution"""
    logger.info("All scenarios completed. Test execution finished.")
