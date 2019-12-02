from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from lesson_8.locators.TrashPage import TrashPage


class DragAndDropActionChain:

    @staticmethod
    def drag_and_drop_to_trash(open_browser):
        """ The method contains action chain to drag and drop element"""
        document = DragAndDropActionChain.get_element_or_none(open_browser, By.XPATH, TrashPage.document)
        trash = open_browser.find_element(By.XPATH, TrashPage.trash)

        while document is not None:
            ActionChains(open_browser).drag_and_drop(document, trash).perform()
            document = DragAndDropActionChain.get_element_or_none(open_browser, By.XPATH, TrashPage.document)

    @staticmethod
    def get_element_or_none(element, by, value):
        """ The method gets the web-element or returns None"""
        elements = element.find_elements(by, value)
        if len(elements) > 0:
            return elements[0]
        return None
