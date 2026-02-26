import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(params=["chromium"]) # "firefox", "webkit"
def browser(playwright, request):
    browser = getattr(playwright, request.param).launch(headless=True, slow_mo=2000)
    yield browser
    browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture
def certificacao_page(page):
    page.goto("https://qualidade.apprbs.com.br/certificacao")
    return page
