from behave import then, given
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from utils.logger import get_logger

logger = get_logger(__name__)


@then('the user waits until the button labeled "Visible After 5 Seconds" is displayed')
def step_wait_for_visible_button(context):
    button = context.base_page.poll_till_visible(context.dynamic_properties.VISIBLE_AFTER_BUTTON)
    assert button.is_displayed(), f"Button Visible after 5 seconds is not visible"
    logger.info("'Visible after 5 seconds' button is now visible.")

@given('the initial "color" of the button is recorded by the user')
def step_fetch_initial_color(context):
    try:
        button = context.base_page.find_element(By.XPATH,context.dynamic_properties.COLOR_CHANGE_BUTTON)
        context.initial_color = button.value_of_css_property("color")
        logger.info(f"Initial button color: {context.initial_color}")
    except Exception as e:
        logger.exception(f"Error while fetching CSS property : {e}")
        raise

@given('the user waits for the button color transition')
def step_wait_for_color_change(context):
    try:
        context.dynamic_properties.wait_for_css_property_change(context.dynamic_properties.COLOR_CHANGE_BUTTON,'color',
            context.initial_color)
        logger.info("Button color has been changed.")
    except TimeoutException:
        logger.error("Button color did not change within timeout", exc_info=True)
        raise AssertionError("Button color did not change within expected time")

@given('the user captures the modified "color" value')
def step_fetch_changed_color(context):
    try:
        button = context.base_page.find_element(By.XPATH, context.dynamic_properties.COLOR_CHANGE_BUTTON)
        context.changed_color = button.value_of_css_property("color")
        logger.info(f"Changed button color: {context.changed_color}")
    except Exception as e:
        logger.exception(f"Error fetching on changed CSS property : {e}")
        raise

@then('the updated color should not match the original')
def step_assert_color_changed(context):
    assert context.initial_color != context.changed_color, (
        f"Expected button color to change but it did not. "
        f"Initial: {context.initial_color}, Changed: {context.changed_color}"
    )
    logger.info("Color change assertion passed")