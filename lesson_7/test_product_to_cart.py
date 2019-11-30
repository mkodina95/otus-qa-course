"""
The file contains tests for the adding, editing and deleting product using selenium webdriver
"""
from selenium.webdriver.common.by import By

from lesson_6.locators.CartPage import CartPage
from lesson_6.locators.MainPage import MainPage
from lesson_6.locators.ProductPage import ProductPage


def test_add_to_cart(open_browser, url_param, quantity="3"):
    """
The test checks the adding product to shopping cart
    """
    open_browser.get(url_param)
    open_browser.find_element(By.XPATH, MainPage.Promo.promo_iphone_block).click()
    open_browser.find_element(By.ID, ProductPage.quantity_input).click()
    open_browser.find_element(By.ID, ProductPage.quantity_input).clear()
    open_browser.find_element(By.ID, ProductPage.quantity_input).send_keys(quantity)
    open_browser.find_element(By.ID, ProductPage.add_to_card_button).click()
    assert quantity in open_browser.find_element(By.XPATH, MainPage.Header.cart_button_text).text
    open_browser.close()


def test_delete_from_cart(open_browser, url_param):
    """
The test checks the deleting product from the shopping cart
    """
    open_browser.get(url_param)
    open_browser.find_element(By.XPATH, MainPage.Promo.promo_iphone_block).click()
    open_browser.find_element(By.ID, ProductPage.add_to_card_button).click()
    open_browser.find_element(By.XPATH, MainPage.Header.cart_button).click()
    open_browser.find_element(By.XPATH, MainPage.Header.cart_block)
    open_browser.find_element(By.XPATH, MainPage.Header.cart_delete_item_button).click()
    assert "0 item(s)" in open_browser.find_element(By.XPATH, MainPage.Header.cart_button_text).text
    open_browser.close()


def test_edit_cart(open_browser, url_param, quantity="5"):
    """
The test checks the editing the quantity of the product in the shopping cart
    """
    open_browser.get(url_param)
    open_browser.find_element(By.XPATH, MainPage.Promo.promo_iphone_block).click()
    open_browser.find_element(By.ID, ProductPage.add_to_card_button).click()
    open_browser.find_element(By.XPATH, MainPage.Header.cart_button).click()
    open_browser.find_element(By.XPATH, MainPage.Header.cart_block)
    open_browser.find_element(By.XPATH, MainPage.Header.cart_checkout).click()
    open_browser.find_element(By.XPATH, CartPage.shopping_cart_block)
    open_browser.find_element(By.XPATH, CartPage.quantity_input_field).click()
    open_browser.find_element(By.XPATH, CartPage.quantity_input_field).clear()
    open_browser.find_element(By.XPATH, CartPage.quantity_input_field).send_keys(quantity)
    open_browser.find_element(By.XPATH, CartPage.quantity_refresh_button).click()
    assert quantity + " item(s)" in open_browser.find_element(By.XPATH, MainPage.Header.cart_button_text).text
    open_browser.close()
