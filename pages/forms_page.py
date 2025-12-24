from selenium.common import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from utils.logger import get_logger
from selenium.webdriver.support import expected_conditions as EC

logger = get_logger(__name__)


class FormsPage(BasePage):
    FIELD_BY_ID = "//*[@id = '{}']"
    GENDER = "//label[text()='{}']"
    SUCCESS_MODAL_TITLE = "//*[contains(@id, 'example-modal-sizes-title-lg')]"
    MODAL_DATA_TABLE ="//div[contains(@class, 'modal-content')]//td"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def validate_field_invalid(self,element, field_name):
        try:
            border_color = element.value_of_css_property("border-color")
            logger.info(f"{field_name} border color: {border_color}")

            assert border_color in (
                "rgb(220, 53, 69)",
                "rgba(220, 53, 69, 1)"
            ), f"{field_name} is not marked invalid"

        except Exception:
            logger.exception(f"{field_name} validation failed")
            raise
