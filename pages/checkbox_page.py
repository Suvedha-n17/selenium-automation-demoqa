from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from utils.logger import get_logger

logger = get_logger(__name__)


class CheckBoxPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=15, poll_frequency=1)

    ELEMENTS_MENU_ITEM = "//div[@class='element-list collapse show']//span[text()='{}']"
    HOME_CHECKBOX = "//span[text()='{}']"
    EXPAND_ALL_BTN = "//button[@title='{}']"
    CHECKBOX_ELEMENTS = "//span[text()='{}']"
    PARENT_CHECKBOX = "//span[text()='{}']/preceding-sibling::span[@class='rct-checkbox']"
    PARENT_NODE = "//span[text()='{}']/ancestor::li"
    NESTED_CHECKBOXES = "svg[class='rct-icon rct-icon-check']"
    CHECKBOX_ICON = "//*[contains(@class,'rct-icon-uncheck')]"
    CHECKED_ITEMS = (By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-check"]')
    TITLE_ITEM = './/ancestor::span[@class="rct-text"]'
    PARENT_OF_CHECKED_ITEM = './ancestor::li//span[@class="rct-title"][1]'
    IS_HALF_CHECKED = "//*[@class='rct-title' and text() = '{}']/preceding-sibling::*[@class = 'rct-checkbox']/*[@class = 'rct-icon rct-icon-half-check']"
    PARENT_NODE_OF_GIVEN_NODE = "//span[@class='rct-title' and text()='{}']/ancestor::li[2]//span[@class='rct-title']"
    NODE_INPUT = "//span[@class='rct-title' and text()='{}']/ancestor::label//input[@type='checkbox']"
    GET_CHECKBOX_NODE ="//*[@class='rct-title' and text() = '{}']/preceding-sibling::*[@class = 'rct-checkbox']/*[@class = 'rct-icon rct-icon-uncheck']"
    ALL_CHILDREN_OF_GIVEN_NODE = "//*[@class = 'rct-title' and text() = '{}']/ancestor::span[@class = 'rct-text']/following-sibling::*/li/span//*[@class = 'rct-title']"

    def is_unchecked(self, icon):
        return "rct-icon-uncheck" in icon.get_attribute("class")

    def get_children_icons(self, node_name):
        return self.driver.find_elements(By.XPATH, CheckBoxPage.ALL_CHILDREN_OF_GIVEN_NODE)
