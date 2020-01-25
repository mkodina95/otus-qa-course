import allure
from selenium.common import exceptions

from lesson_6.locators import Menu as M
from lesson_9.page_object.BasePage import BasePage


class Menu(BasePage):

    def open_menu_tablets(self):
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

    def open_menu(self, *values):
        with allure.step("Open the menu"):
            try:
                self._element(M.menu)
                BasePage._format_locator(M.dropdown, *values)
                self._click(M.dropdown)
                return self
            except exceptions.NoSuchElementException as e:
                print("\n Cannot find an element: " + str(e))
                assert False

            except exceptions.ElementNotInteractableException as e:
                print("\n Cannot interact with an element: " + str(e))
                assert False

            except Exception as e:
                print("\n Something went wrong: " + str(e))
                assert False

    def open_menu_item(self, *values):
        with allure.step("Open the menu item"):
            try:
                BasePage._format_locator(M.dropdown_menu_item, *values)
                self._click(M.dropdown_menu_item)
                return self
            except exceptions.NoSuchElementException as e:
                print("\n Cannot find an element: " + str(e))
                assert False

            except exceptions.ElementNotInteractableException as e:
                print("\n Cannot interact with an element: " + str(e))
                assert False

            except Exception as e:
                print("\n Something went wrong: " + str(e))
                assert False
