from selenium.common import exceptions

from lesson_6.locators import Login
from lesson_9.page_object.BasePage import BasePage


class LoginPage(BasePage):
    def input_username(self, text):
        try:
            self._input(Login.username_input, text)
            return self
        except exceptions.NoSuchElementException as e:
            print("\n Cannot find an element: " + str(e))
            assert False

        except exceptions.ElementNotInteractableException as e:
            print("\n Cannot interact with an element: " + str(e))
            assert False

        except exceptions.InvalidElementStateException as e:
            print("\n Cannot edit an element: " + str(e))
            assert False

    def input_password(self, text):
        try:
            self._input(Login.password_input, text)
            return self
        except exceptions.NoSuchElementException as e:
            print("\n Cannot find an element: " + str(e))
            assert False

        except exceptions.ElementNotInteractableException as e:
            print("\n Cannot interact with an element: " + str(e))
            assert False

        except exceptions.InvalidElementStateException as e:
            print("\n Cannot edit an element: " + str(e))
            assert False

    def submit(self):
        try:
            self._click(Login.login_button)
            return self
        except exceptions.NoSuchElementException as e:
            print("\n Cannot find an element: " + str(e))
            assert False

        except exceptions.ElementNotInteractableException as e:
            print("\n Cannot interact with an element: " + str(e))
            assert False

        except Exception as e:
            print("\n Cannot interact with an element: " + str(e))
            assert False

    def verify_logged_on(self):
        try:
            self._element(Login.user)
            return self
        except exceptions.NoSuchElementException as e:
            print("\n Cannot find an element: " + str(e))
            assert False
