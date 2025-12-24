
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from utils.logger import get_logger


logger = get_logger(__name__)


class DynamicPropertiesPage(BasePage):
    VISIBLE_AFTER_BUTTON = "//button[@id = 'visibleAfter']"
    COLOR_CHANGE_BUTTON = "//button[@id = 'colorChange']"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def poll_till_changes(self, locator, css_property,initial_color=None):
            try:
                logger.info(f"Waiting for '{css_property}' to change from '{initial_color}'")

                WebDriverWait(self.driver, timeout=10, poll_frequency=0.5).until(
                    lambda d: d.find_element(By.XPATH, locator)
                              .value_of_css_property(css_property) != initial_color
                )

                new_value = self.driver.find_element(By.XPATH, locator) .value_of_css_property(css_property)
                logger.info(f"'{css_property}' changed to '{new_value}'")
                return new_value

            except Exception:
                logger.exception(
                    f"CSS '{css_property}' did not change for element: {locator}",
                    exc_info=True
                )
                raise