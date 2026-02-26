import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(params=["chromium"])  # pode adicionar "firefox", "webkit" se quiser
def browser(request):
    with sync_playwright() as p:
        browser = getattr(p, request.param).launch(
            headless=True,   # sempre headless
            slow_mo=0        # sem delay
        )
        yield browser
        browser.close()

@pytest.fixture
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture
def certificacao_page(context):
    page = context.new_page()
    page.goto("https://qualidade.apprbs.com.br/certificacao")
    yield page
    page.close()
