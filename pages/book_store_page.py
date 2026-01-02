from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class BookStorePage(BasePage):
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=15, poll_frequency=1)

    BOOK_ROWS = "//div[@class='rt-tr-group']"

    # Cells in order: Title, Author
    BOOK_TITLE_CELL = ".//div[@class='rt-td'][2]"
    BOOK_AUTHOR_CELL = ".//div[@class='rt-td'][3]"
    BOOK_PUBLISHER_CELL = ".//div[@class='rt-td'][4]"
    API_URL = "https://demoqa.com/BookStore/v1/Books"

