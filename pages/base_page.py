from selenium.common import TimeoutException, WebDriverException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import get_logger

logger = get_logger(__name__)


class BasePage:
    HEADER_CARD = "//h5[normalize-space()='{}']"
    GROUP_HEADER_MENU_ITEMS = "//*[@class = 'group-header']//*[@class = 'header-text' and text() = '{}']/ancestor::span/following-sibling::*[@class = 'element-list collapse show']//*[@class = 'text']"
    EXPAND_GROUP_HEADER = "//span[@class = 'group-header']//*[@class = 'header-text' and text() = '{}']/ancestor::span/following-sibling::div[@class = 'element-list collapse show']"
    ELEMENTS_MENU = "//span[text()='{}']"

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=15, poll_frequency=1)

    def click(self, locator):
        try:
            if isinstance(locator, str):
                locator = (By.XPATH, locator)
            element = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(locator)
            )
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});", element
            )
            element.click()
            self.wait_for_page_load()
            logger.info(f"Clicked on element with locator: {locator}")
        except (TimeoutException, WebDriverException) as e:
            logger.error(f"Element with locator not clickable: {locator}. Exception: {e}")
            raise

    def find_element(self, by, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((by, locator)
                                               ))
            logger.info(f"Element found: {locator}")
            return element
        except (TimeoutException, WebDriverException) as e:
            logger.error(f"Element not visible: {locator}. Exception: {e}")
            raise Exception(f"Element not visible: {locator}")

    def find_elements(self, by, locator, timeout=15):
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((by, locator)
                                               ))
            logger.info(f"{len(elements)} elements found for: ({by}, '{locator}')")
            return elements
        except (TimeoutException, WebDriverException) as e:
            logger.error(f"Elements NOT visible: ({by}, '{locator}'). Exception: {e}")
            raise

    def is_element_present(self, locator, timeout=10):
        logger.info(f"Checking presence of element: {locator}")
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            logger.info(f"Element is visible: {locator}")
            return element
        except TimeoutException:
            logger.error(f"Element NOT present in DOM: {locator}")
            raise

    def send_keys(self, locator, text, timeout=10):
        logger.info(f"Sending keys to element: {locator} | Text: {text}")
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
        logger.info("Text entered successfully")

    def is_element_displayed(self, locator, timeout=15):
        try:
            self.scroll_visibleTo(locator, timeout)
            logger.info(f"Element displayed: {locator}")
            return True
        except Exception as e:
            logger.warning(f"Element NOT displayed: {locator} . Exception: {e}")
            return False

    def wait_for_page_load(self, timeout=15):
        # "Wait until page readyState is complete"
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def scroll_visibleTo(self, locator, timeout=15):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            logger.info(f"Element is visible with locator: {locator}")
            return element
        except TimeoutException as e:
            logger.error(f"Element is not visible with locator: {locator}. Exception: {e}")
            raise

    def elements_are_present(self, locator: tuple[str, str]) -> list[WebElement]:
        logger.info(f'{locator} - Check if these elements are present')
        return self.wait.until(
            EC.presence_of_all_elements_located(locator),
            message=f'Cannot find elements by locator {locator}',
        )

    def poll_till_visible(self, locator, timeout=10, poll_frequency=1):
        try:
            logger.info(f"Fluently waiting for visibility: {locator}")
            return WebDriverWait(
                self.driver,
                timeout,
                poll_frequency,
                ignored_exceptions=(NoSuchElementException, StaleElementReferenceException)
            ).until(EC.visibility_of_element_located((By.XPATH, locator)))
        except TimeoutException:
            logger.error(f"Timeout waiting for visibility: {locator}", exc_info=True)
            raise

