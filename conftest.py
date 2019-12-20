"""
The file contains the fixtures for tests
"""
from datetime import datetime
import pytest

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

import logging
from lesson_12.logging import logger
import urllib.parse

from lesson_12.proxy import client, server


@pytest.fixture()
def open_browser(request, browser_param, wait_param, url_param):
    """
The fixture returns the params for the necessary browser
    """

    try:
        driver = None
        if browser_param == "chrome":
            options = webdriver.ChromeOptions()
            url = urllib.parse.urlparse(client.proxy).path
            options.add_argument('--proxy-server=%s' % url)
            options.add_argument("--headless")
            options.add_experimental_option('w3c', False)
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
        wd = EventFiringWebDriver(driver, EventListener())
        wd.implicitly_wait(wait_param)
        request.addfinalizer(wd.close)
        request.addfinalizer(server.stop)

        def open(path=""):
            return wd.get(url_param + path)

        wd.open = open
        wd.open()
        return wd
    except exceptions.WebDriverException:
        # Exception in case when we don't have suitable browser (for example, IE for MacOS)
        logger.log(logging.ERROR, msg="WebDriverException reached")
        return None
    except Exception as e:
        logger.log(logging.ERROR, msg=(type(e).__name__ + ".Something went wrong"))
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


class EventListener(AbstractEventListener):

    def before_find(self, by, value, driver):
        logger.log(logging.INFO, msg=("Trying to find: " + by + " " + value))

    def after_find(self, by, value, driver):
        logger.log(logging.INFO, msg=("Found: " + by + " " + value))

    def on_exception(self, exception, driver):
        now = datetime.now()
        driver.save_screenshot('/Users/m.kodina/otus-qa-course/lesson_12/screenshots/exception '
                               + now.strftime("%Y-%m-%d %H:%M:%S") + '.png')
        logger.log(logging.ERROR, msg=("Something went wrong: " + exception))


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
