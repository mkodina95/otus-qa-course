from helper import HelperUrl
from lesson_9.page_object.CheckExistenceDB import CheckExistenceDB
from lesson_9.page_object.MainPage import MainPage
from lesson_9.page_object.ProductPage import ProductPage
from lesson_9.page_object.common import Header


def test_delete_from_cart(open_browser, mysql_executor):
    """
The test checks the deleting product from the shopping cart
    """
    HelperUrl.user_base_url(open_browser)
    MainPage(open_browser).open_product_page()
    ProductPage(open_browser).add_to_cart()
    CheckExistenceDB(mysql_executor).check_exist()
    Header(open_browser).open_cart_block() \
        .delete_from_cart_block()
    CheckExistenceDB(mysql_executor).check_is_not_exist()
