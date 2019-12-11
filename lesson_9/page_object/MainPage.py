from selenium.common import exceptions

from lesson_6.locators import Main
from lesson_9.page_object.BasePage import BasePage


class MainPage(BasePage):
    def open_product_page(self):
        try:
            if self._element(Main.promo_mac_block_active):
                self._hover(Main.next_button)
                self._click(Main.next_button)
                self._click(Main.promo_iphone_block_active)
            else:
                self._click(Main.promo_iphone_block_active)
        except exceptions.NoSuchElementException as e:
            print("\n Cannot find an element: " + str(e))
            assert False

        except exceptions.ElementNotInteractableException as e:
            print("\n Cannot interact with an element: " + str(e))
            assert False

        except Exception as e:
            print("\n Something went wrong: " + str(e))
            assert False

