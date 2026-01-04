from behave import given,then
from selenium.common import WebDriverException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)

@given('User launches the application')
def step_launch_website(context):
    try:
        context.page = BasePage(context.driver)
        context.driver.get(context.base_url)
        logger.info(f"Application launched: {context.base_url}")
    except WebDriverException as e:
        logger.error(f"Unable to launch the application: {e}")
        raise

@given('the user navigate to "{section_name}" section')
def step_open_section(context, section_name):
    try:
        context.base_page.click(context.page.HEADER_CARD.format(section_name))
        logger.info(f"Clicked on '{section_name}' card")
    except Exception as e:
        logger.error(f"Failed to click on '{section_name}' card: {e}")
        raise

@then('verify user is navigated to "{page_name}" page')
def step_verify_user(context, page_name):
    try:
        config_key = page_name.lower().replace(" ", "_")
        expected_url = context.config_data[config_key]

        WebDriverWait(context.driver, 20).until(
            lambda d: expected_url in d.current_url
        )
        logger.info(
            f"Navigated successfully to '{page_name}'. "
            f"Current URL: {context.driver.current_url}"
        )
    except KeyError:
        logger.error(
            f"Page '{page_name}' not found in config.json. "
            f"Expected key: '{config_key}'"
        )
        raise
    except TimeoutException:
        logger.error(
            f"Timeout: Expected URL '{expected_url}' not found. "
            f"Current URL: {context.driver.current_url}"
        )
        raise

@then('expand "{header_name}" card')
def step_header(context, header_name):
    try:
        expand_header = context.base_page.is_element_displayed(context.page.EXPAND_GROUP_HEADER.format(header_name))
        logger.info(f"Menu list expanded check for '{header_name}': {expand_header}")
    except Exception as e:
        logger.error(f"Unable to expand for '{header_name}': {e}")
        raise

@then('all options should be displayed under "{menu_name}"')
def step_verify_option_under_menu(context, menu_name):
    """Verify that the Elements menu has the expected items."""
    try:
        for row in context.table:
            option = row["Options"]
            element = context.base_page.is_element_displayed(context.base_page.ELEMENTS_MENU.format(option))
            assert element, f"{option} menu not displayed"
            logger.info(f"Verified presence of the menu: {option}")
    except Exception:
        logger.exception("One or more items not displayed")
        raise
