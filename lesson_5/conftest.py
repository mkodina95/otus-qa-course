"""
The file contains the fixtures for tests
"""
import pytest
from selenium import webdriver


@pytest.fixture()
def open_browser(browser_param):
    """
The fixture returns the params for the necessary browser
    """
    if browser_param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        return driver
    elif browser_param == "ff":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        return driver
    elif browser_param == "ie":
        options = webdriver.IeOptions()
        options.add_argument("--headless")
        driver = webdriver.Ie(options=options)
        return driver


def pytest_addoption(parser):
    """
The function for returning browser and url using addoption
    """
    parser.addoption(
        "--browser",
        action="store",
        default="ff",
        help="The request browser",
        required=False
    )

    parser.addoption(
        "--url",
        action="store",
        default="http://localhost/index.php",
        help="This is default opencart url",
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
