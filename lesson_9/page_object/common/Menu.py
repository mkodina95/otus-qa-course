from selenium.common import exceptions

from lesson_6.locators import Menu as M
from lesson_9.page_object.BasePage import BasePage


class Menu(BasePage):

    def open_menu(self):
        try:
            self._element(M.menu)
            self._click(M.dropdown_tablets)
        except exceptions.NoSuchElementException as e:
            print("\n Cannot find an element: " + str(e))
            assert False

        except exceptions.ElementNotInteractableException as e:
            print("\n Cannot interact with an element: " + str(e))
            assert False

        except Exception as e:
            print("\n Something went wrong: " + str(e))
            assert False
