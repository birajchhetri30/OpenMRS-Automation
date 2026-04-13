import pytest
from playwright.sync_api import sync_playwright
from keyword_core.page_provider import set_page, clear_page


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function", autouse=True)
def page(browser):
    page = browser.new_page()
    set_page(page)
    yield page
    clear_page()
    page.close()