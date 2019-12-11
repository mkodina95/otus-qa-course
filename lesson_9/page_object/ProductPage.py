from selenium.common import exceptions

from lesson_6.locators import Product, Header
from lesson_9.page_object.BasePage import BasePage


class ProductPage(BasePage):
    def input_quantity_of_products(self, quantity):
        try:
            self._input(Product.quantity_input, quantity)
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
        except Exception as e:
            print("\n Something went wrong: " + str(e))
            assert False

    def verify_quantity_in_cart(self, quantity):
        try:
            assert quantity + " item(s)" in self._get_text(Header.cart_button_text)
            return self
        except exceptions.NoSuchElementException as e:
            print("\n Cannot find an element: " + str(e))
            assert False
        except Exception as e:
            print("\n Something went wrong: " + str(e))
            assert False

    def add_to_cart(self):
        try:
            self._click(Product.add_to_cart_button)
            return self
        except exceptions.NoSuchElementException as e:
            print("\n Cannot find an element: " + str(e))
            assert False
        except Exception as e:
            print("\n Something went wrong: " + str(e))
            assert False

    def find_breadcrumb(self):
        try:
            self._element(Product.breadcrumb)
            return self
        except exceptions.NoSuchElementException as e:
            print("\n Cannot find an element: " + str(e))
            assert False
        except Exception as e:
            print("\n Something went wrong: " + str(e))
            assert False

    def find_product_images(self):
        try:
            self._element(Product.product_images)
            return self
        except exceptions.NoSuchElementException as e:
            print("\n Cannot find an element: " + str(e))
            assert False
        except Exception as e:
            print("\n Something went wrong: " + str(e))
            assert False

    def find_description_block(self):
        try:
            if self._element(Product.description_active_button):
                self._element(Product.description_block)
            else:
                self._element(Product.review_active_button)
                self._click(Product.description_button)
                self._element(Product.description_active_button)
                self._element(Product.description_block)
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

    def find_review_block(self):
        try:
            if self._element(Product.description_active_button):
                self._click(Product.review_button)
                self._element(Product.review_active_button)
                self._element(Product.review_block)
            else:
                self._element(Product.review_active_button)
                self._element(Product.review_block)
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

    def write_name(self, text):
        try:
            self._input(Product.review_input_name, text)
            return self
        except exceptions.NoSuchElementException as e:
            print("\n Cannot find an element: " + str(e))
            assert False

        except exceptions.InvalidElementStateException as e:
            print("\n Cannot edit an element: " + str(e))
            assert False

        except Exception as e:
            print("\n Something went wrong: " + str(e))
            assert False

    def write_review(self, text):
        try:
            self._input(Product.review_input_review, text)
            return self
        except exceptions.NoSuchElementException as e:
            print("\n Cannot find an element: " + str(e))
            assert False

        except exceptions.InvalidElementStateException as e:
            print("\n Cannot edit an element: " + str(e))
            assert False

        except Exception as e:
            print("\n Something went wrong: " + str(e))
            assert False

    def write_rating(self):
        try:
            self._click(Product.review_input_rating)
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

    def click_continue(self):
        try:
            self._click(Product.review_continue_button)
            self._element(Product.alert_line)
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
