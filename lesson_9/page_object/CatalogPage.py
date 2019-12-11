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

