class CartPage:
    """
    The file contains the locators for the shopping cart page
    """
    shopping_cart_block = ".//*[@id='content']/*[contains (text(),'Shopping Cart')]"
    quantity_input_field = ".//*[@class='input-group btn-block']/*[@type='text']"
    quantity_refresh_button = ".//*[@class='input-group btn-block']//*[@type='submit']"
