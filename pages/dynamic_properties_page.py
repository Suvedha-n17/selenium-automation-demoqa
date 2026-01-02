from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from utils.logger import get_logger


logger = get_logger(__name__)


class DynamicPropertiesPage(BasePage):
    VISIBLE_AFTER_BUTTON = "//button[@id='visibleAfter']"
    COLOR_CHANGE_BUTTON = "//button[@id='colorChange']"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # ---------- INTERNAL EXPECTED CONDITION ----------
    class _CssPropertyValueChanged:
        def __init__(self, locator, css_property, initial_value):
            self.locator = locator
            self.css_property = css_property
            self.initial_value = initial_value

        def __call__(self, driver):
            element = driver.find_element(By.XPATH, self.locator)
            return element.value_of_css_property(self.css_property) != self.initial_value

    # ---------- PUBLIC PAGE METHOD ----------
    def wait_for_css_property_change(
        self,
        locator: str,
        css_property: str,
        initial_value: str | None = None,
        timeout: int = 10
    ):
        """
        Wait until the given CSS property value changes for an element
        """
        try:
            logger.info(
                f"Waiting for CSS '{css_property}' to change from '{initial_value}'"
            )
            WebDriverWait(self.driver, timeout=timeout, poll_frequency=0.5).until(
                self._CssPropertyValueChanged(
                    locator, css_property, initial_value
                )
            )
            new_value = (
                self.driver.find_element(By.XPATH, locator)
                .value_of_css_property(css_property)
            )
            logger.info(f"CSS '{css_property}' changed to '{new_value}'")
            return new_value
        except Exception:
            logger.exception(
                f"CSS '{css_property}' did not change for element: {locator}",
                exc_info=True
            )
            raise
