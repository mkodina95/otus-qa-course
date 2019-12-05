"""
The file contains tests for the adding, editing and deleting product using selenium webdriver
"""
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from lesson_6.locators.CartPage import CartPage
from lesson_6.locators.MainPage import MainPage
from lesson_6.locators.ProductPage import ProductPage


def test_add_to_cart(open_browser, url_param, quantity="3"):
    """
The test checks the adding product to shopping cart
    """
    if open_browser is None:
        print("\n WebDriver is not initialized")
        assert False

    try:
        wait = WebDriverWait(open_browser, 10)
        open_browser.get(url_param)
        open_browser.find_element(By.XPATH, MainPage.Promo.promo_iphone_block).click()
        wait.until(EC.element_to_be_clickable((By.ID, ProductPage.quantity_input))).click()
        open_browser.find_element(By.ID, ProductPage.quantity_input).clear()
        open_browser.find_element(By.ID, ProductPage.quantity_input).send_keys(quantity)
        open_browser.find_element(By.ID, ProductPage.add_to_card_button).click()
        assert quantity in wait.until(EC.presence_of_element_located(
            (By.XPATH, MainPage.Header.cart_button_text))).text
    except exceptions.NoSuchElementException as e:
        print("\n Cannot find an element: " + str(e))
        assert False
    except exceptions.ElementNotInteractableException as e:
        print("\n Cannot interact with an element: " + str(e))
        assert False
    except exceptions.InvalidElementStateException as e:
        print("\n Cannot edit an element: " + str(e))
        assert False
    except exceptions.TimeoutException as e:
        print("\n Timeout has reached - " + str(e))
        assert False
    except Exception as e:
        print("\n" + type(e).__name__ + ". Something went wrong with " + test_add_to_cart.__name__ + " - " + str(e))
        assert False
    finally:
        open_browser.close()


def test_delete_from_cart(open_browser, url_param):
    """
The test checks the deleting product from the shopping cart
    """
    if open_browser is None:
        print("\n WebDriver is not initialized")
        assert False

    try:
        wait = WebDriverWait(open_browser, 10)
        open_browser.get(url_param)
        open_browser.find_element(By.XPATH, MainPage.Promo.promo_iphone_block).click()
        wait.until(EC.element_to_be_clickable((By.ID, ProductPage.add_to_card_button))).click()
        open_browser.find_element(By.XPATH, MainPage.Header.cart_button).click()
        wait.until(EC.presence_of_element_located((By.XPATH, MainPage.Header.cart_block)))
        open_browser.find_element(By.XPATH, MainPage.Header.cart_delete_item_button).click()
        assert "0 item(s)" in wait.until(EC.presence_of_element_located(
            (By.XPATH, MainPage.Header.cart_button_text))).text
    except exceptions.NoSuchElementException as e:
        print("\n Cannot find an element: " + str(e))
        assert False
    except exceptions.ElementNotInteractableException as e:
        print("\n Cannot interact with an element: " + str(e))
        assert False
    except exceptions.InvalidElementStateException as e:
        print("\n Cannot edit an element: " + str(e))
        assert False
    except exceptions.TimeoutException as e:
        print("\n Timeout has reached - " + str(e))
        assert False
    except Exception as e:
        print("\n" + type(e).__name__ + ". Something went wrong with " + test_add_to_cart.__name__ + " - " + str(e))
        assert False
    finally:
        open_browser.close()


def test_edit_cart(open_browser, url_param, quantity="5"):
    """
The test checks the editing the quantity of the product in the shopping cart
    """
    if open_browser is None:
        print("\n WebDriver is not initialized")
        assert False

    try:
        wait = WebDriverWait(open_browser, 10)
        open_browser.get(url_param)
        open_browser.find_element(By.XPATH, MainPage.Promo.promo_iphone_block).click()
        wait.until(EC.element_to_be_clickable((By.ID, ProductPage.add_to_card_button))).click()
        open_browser.find_element(By.XPATH, MainPage.Header.cart_button).click()
        wait.until(EC.presence_of_element_located((By.XPATH, MainPage.Header.cart_block)))
        open_browser.find_element(By.XPATH, MainPage.Header.cart_checkout).click()
        wait.until(EC.presence_of_element_located((By.XPATH, CartPage.shopping_cart_block)))
        open_browser.find_element(By.XPATH, CartPage.quantity_input_field).click()
        open_browser.find_element(By.XPATH, CartPage.quantity_input_field).clear()
        open_browser.find_element(By.XPATH, CartPage.quantity_input_field).send_keys(quantity)
        open_browser.find_element(By.XPATH, CartPage.quantity_refresh_button).click()
        assert quantity + " item(s)" in wait.until(EC.presence_of_element_located(
            (By.XPATH, MainPage.Header.cart_button_text))).text
    except exceptions.NoSuchElementException as e:
        print("\n Cannot find an element: " + str(e))
        assert False
    except exceptions.ElementNotInteractableException as e:
        print("\n Cannot interact with an element: " + str(e))
        assert False
    except exceptions.InvalidElementStateException as e:
        print("\n Cannot edit an element: " + str(e))
        assert False
    except exceptions.TimeoutException as e:
        print("\n Timeout has reached - " + str(e))
        assert False
    except Exception as e:
        print("\n" + type(e).__name__ + ". Something went wrong with " + test_add_to_cart.__name__ + " - " + str(e))
        assert False
    finally:
        open_browser.close()
