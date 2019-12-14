"""
The file contains tests for the adding, editing and deleting product using selenium webdriver
"""
from lesson_9.page_object.CartPage import CartPage
from lesson_9.page_object.MainPage import MainPage
from lesson_9.page_object.ProductPage import ProductPage
from lesson_9.page_object.common.Header import Header


def test_add_to_cart(open_browser, quantity="3"):
    """
The test checks the adding product to shopping cart
    """
    MainPage(open_browser).open_product_page()
    ProductPage(open_browser).input_quantity_of_products(quantity) \
        .add_to_cart() \
        .verify_quantity_in_cart(quantity)


def test_delete_from_cart(open_browser):
    """
The test checks the deleting product from the shopping cart
    """
    MainPage(open_browser).open_product_page()
    ProductPage(open_browser).add_to_cart()
    Header(open_browser).open_cart_block() \
        .delete_from_cart_block()


def test_edit_cart(open_browser, quantity="5"):
    """
The test checks the editing the quantity of the product in the shopping cart
    """
    MainPage(open_browser).open_product_page()
    ProductPage(open_browser).add_to_cart()
    Header(open_browser).open_cart_block() \
        .move_to_checkout_from_cart_block()
    CartPage(open_browser).edit_product_quantity(quantity)
    ProductPage(open_browser).verify_quantity_in_cart(quantity)

