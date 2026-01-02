import requests
from behave import when, then, When
from selenium.webdriver.common.by import By

from utils.logger import get_logger

logger = get_logger(__name__)


@when("the user retrieves the list of books displayed in the UI")
def step_get_books_ui(context):
    try:
        rows = context.base_page.find_elements(By.XPATH, context.book_store_page.BOOK_ROWS)
        context.ui_books = []

        for row in rows:
            title = row.find_element(By.XPATH, context.book_store_page.BOOK_TITLE_CELL).text.strip()
            if not title:
                continue
            book = {
                "title": row.find_element(By.XPATH, context.book_store_page.BOOK_TITLE_CELL).text.strip(),
                "author": row.find_element(By.XPATH, context.book_store_page.BOOK_AUTHOR_CELL).text.strip(),
                "publisher": row.find_element(By.XPATH, context.book_store_page.BOOK_PUBLISHER_CELL).text.strip()
            }
            context.ui_books.append(book)

        logger.info(f"{len(context.ui_books)} books retrieved from UI")
        # Log the title and author of each book
        for book in context.ui_books:
            logger.info(f"Book title: {book['title']}")
            logger.info(f"Book author: {book['author']}")

    except Exception:
        logger.exception("Failed to retrieve book details from UI")
        raise


@when("the user retrieves the list of books available in the API")
def step_get_books_api(context):
    try:
        response = requests.get(context.book_store_page.API_URL)
        response.raise_for_status()
        data = response.json()
        context.api_books = []

        for book in data["books"]:
            context.api_books.append({
                "title": book.get("title", "").strip(),
                "author": book.get("author", "").strip(),
                "publisher": book.get("publisher", "").strip()
            })

        logger.info(f"{len(context.api_books)} books retrieved from API")
        # Log the title and author of each book
        for book in context.api_books:
            logger.info(f"Book title: {book['title']}")
            logger.info(f"Book author: {book['author']}")

    except Exception:
        logger.exception("Failed to retrieve book details from API")
        raise


@When("the Book Store API should be available")
def step_check_book_store_api(context):
    try:
        response = requests.get(context.book_store_page.API_URL)
        logger.info(f"Book Store API response status code: {response.status_code}")

        assert response.status_code == 200, (
            f"Book Store API is not available. "
            f"Expected 200, got {response.status_code}"
        )

        logger.info("Book Store API is available and responding successfully")

    except Exception:
        logger.exception("Book Store API availability check failed")
        raise


@then("the list of books in the UI should match the API response accordingly")
def step_validate_ui_vs_api_full(context):
    try:
        ui_books_set = {(b["title"], b["author"], b["publisher"]) for b in context.ui_books}
        api_books_set = {(b["title"], b["author"], b["publisher"]) for b in context.api_books}

        missing_in_ui = api_books_set - ui_books_set
        extra_in_ui = ui_books_set - api_books_set
        matching_books = ui_books_set & api_books_set

        assert not missing_in_ui, f"Books missing in UI: {missing_in_ui}"
        assert not extra_in_ui, f"Extra books in UI: {extra_in_ui}"

        logger.info(f"UI vs API validation passed. {len(matching_books)} matching books found")
    except Exception:
        logger.exception("UI vs API book validation failed")
        raise
