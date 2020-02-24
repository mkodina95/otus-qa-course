"""File runs tests on the cloud grid - browserstack"""
import pytest
from selenium import webdriver


@pytest.fixture()
def driver(request):
    wd = webdriver.Remote(
        command_executor='http://marina433:FLYaq7T4RLnD9Ts75pCv@hub.browserstack.com:80/wd/hub',
        desired_capabilities=desired_cap)
    request.addfinalizer(wd.quit)
    return wd


def test_google(driver):
    driver.get("http://www.google.com/ncr")
    if "Google" not in driver.title:
        raise Exception("Unable to load google page!")
    elem = driver.find_element_by_name("q")
    elem.send_keys("BrowserStack")
    elem.submit()
    print(driver.title)


desired_cap = {
    'browser': 'Chrome',
    'browser_version': '79.0',
    'os': 'Windows',
    'os_version': '10',
    'resolution': '1024x768',
    'name': 'Bstack-[Python] Sample Test'
}
