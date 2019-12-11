"""
The file contains the locators for the shopping cart page
"""


class Cart:
    shopping_cart_block = {"xpath": ".//*[@id='content']/*[contains (text(),'Shopping Cart')]"}
    quantity_input_field = {"xpath": ".//*[@class='input-group btn-block']/*[@type='text']"}
    quantity_refresh_button = {"xpath": ".//*[@class='input-group btn-block']//*[@type='submit']"}
