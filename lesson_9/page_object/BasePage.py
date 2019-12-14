from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _element(self, selector: dict):
        by = None
        if 'xpath' in selector.keys():
            by = By.XPATH
            selector = selector['xpath']
        elif 'id' in selector.keys():
            by = By.ID
            selector = selector['id']
        elif 'partial link text' in selector.keys():
            by = By.PARTIAL_LINK_TEXT
            selector = selector['partial link text']

        try:
            return self.driver.find_element(by, selector)
        except Exception:
            return None

    def _input(self, selector, text):
        element = self._element(selector)
        element.clear()
        element.send_keys(text)

    def _get_text(self, selector):
        element = self._element(selector)
        return element.text

    def _click(self, selector, wait=5):
        method = list(selector)[0]
        locator = list(selector.values())[0]

        element = WebDriverWait(self.driver, wait).until(
            EC.element_to_be_clickable((method, locator)))

        element.click()

    def _hover(self, selector):
        ActionChains(self.driver).move_to_element(self._element(selector)).perform()

    @staticmethod
    def _format_locator(source: dict, *values):
        method = list(source)[0]
        source[method] = source[method].format(*values)
