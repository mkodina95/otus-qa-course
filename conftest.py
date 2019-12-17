"""
The file contains the fixtures for tests
"""

import pytest
from selenium import webdriver
from selenium.common import exceptions


@pytest.fixture()
def open_browser(request, browser_param, wait_param, url_param):
    """
The fixture returns the params for the necessary browser
    """
    try:
        driver = None
        if browser_param == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            driver = webdriver.Chrome(options=options)
        elif browser_param == "ff":
            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            driver = webdriver.Firefox(options=options)
        elif browser_param == "ie":
            options = webdriver.IeOptions()
            driver = webdriver.Ie(options=options)
        else:
            return driver
        driver.implicitly_wait(wait_param)
        request.addfinalizer(driver.close)

        def open(path=""):
            return driver.get(url_param + path)
        driver.open = open
        driver.open()
        return driver
    except exceptions.WebDriverException:
        # Exception in case when we don't have suitable browser (for example, IE for MacOS)
        print("\n WebDriverException reached")
        return None
    except Exception as e:
        print("\n" + type(e).__name__ + ".Something went wrong")
        return None


def pytest_addoption(parser):
    """
The function for returning browser and url using addoption
    """
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="The request browser",
        required=False
    )

    parser.addoption(
        "--url",
        action="store",
        default="http://localhost/",
        help="This is default opencart url",
        required=False
    )

    parser.addoption(
        "--wait",
        action="store",
        default="10",
        help="This is default wait time",
        required=False
    )


@pytest.fixture
def url_param(request):
    """
The fixture returns opencart url
    """
    return request.config.getoption("--url")


@pytest.fixture
def browser_param(request):
    """
The fixture returns browser
    """
    return request.config.getoption("--browser")


@pytest.fixture
def wait_param(request):
    """
The fixture returns wait time
    """
    return request.config.getoption("--wait")


@pytest.fixture()
def trash_url():
    """
The fixture returns the url for moving docs to trash
    """
    return 'https://marcojakob.github.io/dart-dnd/basic/'
