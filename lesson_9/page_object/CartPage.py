import allure
from selenium.common import exceptions


from lesson_6.locators import Cart
from lesson_9.page_object.BasePage import BasePage


class CartPage(BasePage):
    def edit_product_quantity(self, quantity):
        with allure.step("Edit the quantity of items"):
            try:
                self._click(Cart.quantity_input_field)
                self._input(Cart.quantity_input_field, quantity)
                self._click(Cart.quantity_refresh_button)
            except exceptions.NoSuchElementException as e:
                print("\n Cannot find an element: " + str(e))
                assert False

            except exceptions.InvalidElementStateException as e:
                print("\n Cannot edit an element: " + str(e))
                assert False

            except Exception as e:
                print("\n Something went wrong: " + str(e))
                assert False
