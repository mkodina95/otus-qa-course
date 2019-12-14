from selenium.common import exceptions

from lesson_6.locators import Catalog
from lesson_9.page_object.BasePage import BasePage


class CatalogPage(BasePage):
    def find_product(self):
        try:
            self._element(Catalog.product_item)
            return self
        except exceptions.NoSuchElementException as e:
            print("\n Cannot find an element: " + str(e))
            assert False
        except Exception as e:
            print("\n Something went wrong: " + str(e))
            assert False

    def compare_product_name(self, text):
        try:
            self._element({"partial link text": text})
            return self
        except exceptions.NoSuchElementException as e:
            print("\n Cannot find an element: " + str(e))
            assert False
        except Exception as e:
            print("\n Something went wrong: " + str(e))
            assert False

    def find_categories(self):
        try:
            self._element(Catalog.categories_list)
            return self
        except exceptions.NoSuchElementException as e:
            print("\n Cannot find an element: " + str(e))
            assert False
        except Exception as e:
            print("\n Something went wrong: " + str(e))
            assert False

    def get_title(self, item):
        try:
            assert item in self._get_text(Catalog.categories_title)
            return self
        except exceptions.NoSuchElementException as e:
            print("\n Cannot find an element: " + str(e))
            assert False
        except Exception as e:
            print("\n Something went wrong: " + str(e))
            assert False

    def open_category_item(self, *values):
        try:
            BasePage._format_locator(Catalog.category_item, *values)
            self._click(Catalog .category_item)
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

    def add_to_cart(self):
        try:
            self._click(Catalog.add_to_cart_button)
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

    def not_present_item(self, *values):
        try:
            BasePage._format_locator(Catalog.category_item, *values)
            element = self._element(Catalog.category_item)
            assert element is not None
            return self
        except Exception as e:
            print("\n Something went wrong: " + str(e))
            assert False

