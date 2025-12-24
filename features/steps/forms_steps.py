from behave import when
from behave import then, given
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from utils.logger import get_logger

logger = get_logger(__name__)

@when('the user clicks on the "{field_name}" button')
def step_click_submit(context, field_name):
    try:
        context.base_page.click(context.forms_page.FIELD_BY_ID.format(field_name))
        logger.info(f"Clicked on '{field_name}' button")
    except Exception as e:
        logger.exception(f"Failed to click on '{field_name}' button: {e}")
        raise

@then('the "{field_name}" field should be highlighted as invalid')
def step_validate_first_name(context, field_name):
    try:
        field = context.base_page.find_element(By.XPATH,context.forms_page.FIELD_BY_ID.format(field_name))
        context.forms_page.validate_field_invalid(field, field_name)
        logger.info(f"Field '{field_name}' highlighted as invalid")
    except Exception:
        logger.exception(f"Failed to validate '{field_name}' field")
        raise

@when('the user enters "{field_value}" in the "{field_name}" field')
def step_enter_first_name(context, field_value, field_name):
    try:
        field = context.base_page.find_element(By.XPATH,context.forms_page.FIELD_BY_ID.format(field_name))
        field.send_keys(field_value)
        logger.info(f"User entered value in :'{field_name}' successfully ")
    except Exception:
        logger.exception(f"Failed to enter value in '{field_name}' field")
        raise

@when('the user selects Gender as "{gender_option}"')
def step_select_gender(context, gender_option):
    try:
        field_id = context.base_page.find_element(By.XPATH,context.forms_page.GENDER.format(gender_option))
        context.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", field_id
        )
        field_id.click()
        logger.info(f"User selected gender as :'{gender_option}' successfully ")
    except Exception:
        logger.exception(f"Failed to select gender as :'{gender_option}' ")
        raise

@then('a modal with title "{message}" should be displayed')
def step_verify_modal_title(context, message):
    try:
        modal_title = context.base_page.find_element(By.XPATH,context.forms_page.SUCCESS_MODAL_TITLE).text
        assert modal_title == message, f"Unexpected modal title: {modal_title}"
        logger.info("Modal title verified successfully")
    except Exception:
        logger.exception("Modal title verification failed")
        raise

@then("upon submission modal window should display the following data")
def step_verify_submitted_data(context):
    """Verify that the modal window displays the correct data."""
    try:
        # Fetch all table cells
        cells = context.base_page.find_elements(By.XPATH, context.forms_page.MODAL_DATA_TABLE)
        table_text = [cell.text for cell in cells]

        for row in context.table:
            expected_label = row['Label']
            expected_value = row['Value']

            assert expected_value in table_text, f"{expected_label} value '{expected_value}' not found in modal"
            logger.info(f"{expected_label} validated successfully in modal")

    except Exception:
        logger.exception("Modal data verification failed")
        raise