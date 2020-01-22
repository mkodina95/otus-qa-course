""" File runs tests on the remote grid"""

import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities={'browserName': 'firefox'})
    request.addfinalizer(wd.quit)
    return wd


def test_grid(driver):
    """Test for checking correct remote run"""
    driver.get("http://www.google.com")
    if "Google" not in driver.title:
        raise Exception("Unable to load google page!")
    elem = driver.find_element_by_name("q")
    elem.click()
