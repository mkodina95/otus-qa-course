"""
The file contains tests for catalog page
"""
from helper import HelperUrl
from lesson_9.page_object.CatalogPage import CatalogPage
from lesson_9.page_object.MainPage import MainPage
from lesson_9.page_object.ProductPage import ProductPage
from lesson_9.page_object.common import Menu


def test_add_to_comparison(open_browser):
    """
The test checks the adding product to comparison
    """
    HelperUrl.user_base_url(open_browser)
    MainPage(open_browser).open_product_page()
    ProductPage(open_browser).add_to_comparison()\
        .move_to_comparison()
    CatalogPage(open_browser).compare_product_name("Samsung Galaxy")


def test_open_catalog_from_menu(open_browser, item="PC"):
    """
The test checks the opening catalog from header menu
    """
    HelperUrl.user_base_url(open_browser)
    Menu(open_browser).open_menu("Desktops")\
        .open_menu_item("Desktops", item)
    CatalogPage(open_browser).find_categories()\
        .get_title(item)


def test_open_product_from_catalog(open_browser):
    """
The test checks the opening product from catalog
    """
    HelperUrl.user_base_url(open_browser)
    Menu(open_browser).open_menu("Desktops") \
        .open_menu_item("Desktops", "Show All")
    CatalogPage(open_browser).find_categories()\
        .open_category_item("Tablets")\
        .compare_product_name("Samsung Galaxy")


def test_add_to_cart_from_catalog(open_browser):
    """
The test checks the adding product to cart from the catalog
    """
    HelperUrl.user_base_url(open_browser)
    Menu(open_browser).open_menu("Desktops") \
        .open_menu_item("Desktops", "Show All")
    CatalogPage(open_browser).find_categories() \
        .open_category_item("Tablets")\
        .add_to_cart()
    ProductPage(open_browser).verify_quantity_in_cart("1")


def test_move_to_catalog_items(open_browser):
    """
The test checks if the subitems in catalog menu are hidden
    """
    HelperUrl.user_base_url(open_browser)
    Menu(open_browser).open_menu("Desktops") \
        .open_menu_item("Desktops", "Show All")
    CatalogPage(open_browser).find_categories()\
        .open_category_item("Desktops")\
        .get_title("Desktops") \
        .open_category_item("PC") \
        .open_category_item("Mac") \
        .open_category_item("Laptops & Notebooks")\
        .not_present_item("PC")\
        .not_present_item("Mac")
