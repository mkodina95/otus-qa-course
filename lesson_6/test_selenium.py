"""
The file contains tests using selenium webdriver
"""
from selenium.webdriver.common.by import By

from lesson_6.locators.CatalogPage import CatalogPage
from lesson_6.locators.LoginPage import LoginPage
from lesson_6.locators.MainPage import MainPage
from lesson_6.locators.ProductPage import ProductPage


def test_admin_login(open_browser, url_param):
    """
The test checks the correct login to admin panel
    """
    open_browser.get(url_param)
    open_browser.find_element(By.ID, LoginPage.logo)
    open_browser.find_element(By.ID, LoginPage.username_input).click()
    open_browser.find_element(By.ID, LoginPage.username_input).send_keys("user")
    open_browser.find_element(By.ID, LoginPage.password_input).click()
    open_browser.find_element(By.ID, LoginPage.password_input).send_keys("user")
    open_browser.find_element(By.XPATH, LoginPage.login_button).click()
    open_browser.find_element(By.XPATH, LoginPage.user)
    open_browser.close()


def test_search_product(open_browser, url_param):
    """
The test checks the search item
    """
    open_browser.get(url_param)
    open_browser.find_element(By.XPATH, MainPage.Header.search_input).click()
    open_browser.find_element(By.XPATH, MainPage.Header.search_input).send_keys("Samsung Galaxy")
    open_browser.find_element(By.XPATH, MainPage.Header.search_button).click()
    open_browser.find_element(By.XPATH, CatalogPage.product_item)
    open_browser.find_element_by_partial_link_text("Samsung Galaxy")
    open_browser.close()


def test_open_catalog(open_browser, url_param):
    """
The test checks opening the catalog
    """
    open_browser.get(url_param)
    open_browser.find_element(By.XPATH, MainPage.Menu.menu)
    open_browser.find_element(By.XPATH, MainPage.Menu.dropdown_tablets).click()
    open_browser.find_element(By.XPATH, CatalogPage.categories_list)
    open_browser.find_element(By.XPATH, ProductPage.breadcrumb)
    open_browser.find_element(By.XPATH, CatalogPage.product_item)
    open_browser.find_element_by_partial_link_text("Samsung Galaxy")
    open_browser.close()


def test_open_item_from_main_page(open_browser, url_param):
    """
The test checks opening the product card from the main page
    """
    open_browser.get(url_param)
    open_browser.find_element(By.XPATH, MainPage.Promo.promo_iphone_block).click()
    open_browser.find_element(By.XPATH, ProductPage.breadcrumb)
    open_browser.find_element(By.XPATH, ProductPage.product_images)
    open_browser.find_element(By.XPATH, ProductPage.description_active_button)
    open_browser.find_element(By.ID, ProductPage.description_block)
    open_browser.find_element(By.ID, ProductPage.add_to_card_button)
    open_browser.close()


def test_write_review(open_browser, url_param):
    """
The test checks writing the review for the product
    """
    open_browser.get(url_param)
    open_browser.find_element(By.XPATH, MainPage.Promo.promo_iphone_block).click()
    open_browser.find_element(By.XPATH, ProductPage.review_button).click()
    open_browser.find_element(By.XPATH, ProductPage.review_active_button)
    open_browser.find_element(By.ID, ProductPage.review_block)
    open_browser.find_element(By.ID, ProductPage.review_input_name).send_keys("user")
    open_browser.find_element(By.ID, ProductPage.review_input_review).send_keys(
        "This is test comment for the item"
    )
    open_browser.find_element(By.XPATH, ProductPage.review_input_rating).click()
    open_browser.find_element(By.ID, ProductPage.review_continue_button).click()
    open_browser.find_element(By.XPATH, ProductPage.alert_line)
    open_browser.close()
