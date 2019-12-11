"""
The file contains tests using selenium webdriver
"""

from lesson_9.page_object.CatalogPage import CatalogPage
from lesson_9.page_object.LoginPage import LoginPage
from lesson_9.page_object.MainPage import MainPage
from lesson_9.page_object.ProductPage import ProductPage
from lesson_9.page_object.common.Header import Header
from lesson_9.page_object.common.Menu import Menu


def test_admin_login(open_browser):
    """
The test checks the correct login to admin panel
    """
    LoginPage(open_browser) \
        .input_username("user") \
        .input_password("user") \
        .submit() \
        .verify_logged_on()


def test_search_product(open_browser):
    """
The test checks the search item
    """
    Header(open_browser).search("Samsung Galaxy")
    CatalogPage(open_browser).find_product() \
        .compare_product_name("Samsung Galaxy")


def test_open_catalog(open_browser):
    """
The test checks opening the catalog
    """
    Menu(open_browser).open_menu()
    CatalogPage(open_browser).find_categories() \
        .find_product() \
        .compare_product_name("Samsung Galaxy")


def test_open_item_from_main_page(open_browser):
    """
The test checks opening the product card from the main page
    """
    MainPage(open_browser).open_product_page()
    ProductPage(open_browser).find_breadcrumb() \
        .find_product_images() \
        .find_description_block() \
        .add_to_cart()


def test_write_review(open_browser):
    """
The test checks writing the review for the product
    """
    MainPage(open_browser).open_product_page()
    ProductPage(open_browser).find_review_block() \
        .write_name("user") \
        .write_name("This is test comment for the item") \
        .write_rating() \
        .click_continue()
