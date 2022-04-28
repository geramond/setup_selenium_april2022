import os

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--drivers", default=os.path.expanduser("~\\Downloads\\drivers"))


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")
    if browser_name == "chrome":
        browser = webdriver.Chrome(executable_path=f"{drivers}/chromedriver")
    elif browser_name == "firefox":
        browser = webdriver.Firefox(executable_path=f"{drivers}/geckodriver")
    elif browser_name == "safari":
        browser = webdriver.Safari()
    else:
        raise ValueError("Browser not supported!")

    browser.maximize_window()
    request.addfinalizer(browser.close)

    return browser
