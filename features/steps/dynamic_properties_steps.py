from behave import then, given
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from utils.logger import get_logger

logger = get_logger(__name__)


@then('the user should fluently wait until the button with text "Visible After 5 Seconds" becomes visible')
def step_wait_for_visible_button(context):
    button = context.base_page.poll_till_visible(context.dynamic_properties.VISIBLE_AFTER_BUTTON)
    assert button.is_displayed(), f"Button Visible after 5 seconds is not visible"
    logger.info("'Visible after 5 seconds' button is now visible.")

@given('the user fetches initial "color" of the button')
def step_fetch_initial_color(context):
    try:
        button = context.base_page.find_element(By.XPATH,context.dynamic_properties.COLOR_CHANGE_BUTTON)
        context.initial_color = button.value_of_css_property("color")
        logger.info(f"Initial button color: {context.initial_color}")
    except Exception as e:
        logger.exception(f"Error while fetching CSS property : {e}")
        raise

@given('the user fluently wait until the button color changes')
def step_wait_for_color_change(context):
    try:
        context.dynamic_properties.poll_till_changes(context.dynamic_properties.COLOR_CHANGE_BUTTON,'color',
            context.initial_color)
        logger.info("Button color has been changed.")
    except TimeoutException:
        logger.error("Button color did not change within timeout", exc_info=True)
        raise AssertionError("Button color did not change within expected time")

@given('the user fetches the changed "color" of the button')
def step_fetch_changed_color(context):
    try:
        button = context.base_page.find_element(By.XPATH, context.dynamic_properties.COLOR_CHANGE_BUTTON)
        context.changed_color = button.value_of_css_property("color")
        logger.info(f"Changed button color: {context.changed_color}")
    except Exception as e:
        logger.exception(f"Error fetching on changed CSS property : {e}")
        raise

@then('user asserts if the color of the button has been changed')
def step_assert_color_changed(context):
    assert context.initial_color != context.changed_color, (
        f"Expected button color to change but it did not. "
        f"Initial: {context.initial_color}, Changed: {context.changed_color}"
    )
    logger.info("Color change assertion passed")