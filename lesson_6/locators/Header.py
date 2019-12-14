"""
The file contains locators for header block
"""


class Header:
    logo = {"xpath": ".//*[@id='logo']"}
    search_input = {"xpath": ".//*[@class='form-control input-lg']"}
    search_button = {"xpath": ".//*[@class='btn btn-default btn-lg']"}
    cart_button = {"xpath": ".//*[@id='cart']//*[@type='button']"}
    cart_button_text = {"xpath": cart_button['xpath'] + "//*[@id='cart-total']"}
    cart_block = {"xpath": ".//*[@id='cart']//*[contains(@class, 'dropdown-menu')]"}
    cart_delete_item_button = {"xpath": cart_block['xpath'] + "//*[@title='Remove']"}
    cart_checkout_button = {"xpath": ".//*[@id='cart']//*[contains(@class,"
                                     " 'dropdown-menu')]//*[@class='text-right']//a"}
