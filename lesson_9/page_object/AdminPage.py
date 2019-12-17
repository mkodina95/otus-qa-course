from selenium.common import exceptions

from lesson_6.locators.Admin import Admin
from lesson_9.page_object.BasePage import BasePage


class AdminPage(BasePage):
    def input_username(self, text):
        try:
            self._input(Admin.username_input, text)
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
            self._input(Admin.password_input, text)
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
            self._click(Admin.login_button)
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

    def verify_logged_on(self):
        try:
            self._element(Admin.user)
            return self
        except exceptions.NoSuchElementException as e:
            print("\n Cannot find an element: " + str(e))
            assert False

    def add_new_download(self):
        try:
            self._click(Admin.add_new_download_button)
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

    def upload_file(self, filename):
        try:
            self._click(Admin.upload_file_button)
            self._input_file(Admin.upload_file_input, filename)
            self._accept_alert()
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
