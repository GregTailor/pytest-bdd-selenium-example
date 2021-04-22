import pytest
from selenium import webdriver


@pytest.fixture()
def browser(request):
    driver = request.config.getoption("--webdriver")

    if driver == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        browser = webdriver.Chrome(options=options)
    elif driver == 'firefox':
        browser = webdriver.Firefox()

    yield browser
    browser.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--webdriver",
        action='store',
        choices=['chrome', 'firefox'],
        required=True)
