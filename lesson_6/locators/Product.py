"""
The file contains locators for the product page
"""


class Product:
    breadcrumb = {"xpath": ".//*[@class='breadcrumb']"}
    product_images = {"xpath": ".//*[@class='thumbnails']"}
    alert_line = {"xpath": ".//*[contains(@class, 'alert')]"}
    wishlist_button = {"xpath": ".//*[contains(@class, 'fa-heart')]"
                                "/ancestor::*[@class='btn btn-default']"}
    compare_button = {"xpath": ".//*[contains(@class, 'fa-exchange')]"
                               "/ancestor::*[@class='btn btn-default']"}
    quantity_input = {"id": "input-quantity"}
    add_to_cart_button = {"id": "button-cart"}
    share_buttons = {"class": "addthis_toolbox addthis_default_style"}
    description_button = {"xpath": ".//*[@class='nav nav-tabs']//*[text()='Description']"}
    description_active_button = {"xpath": description_button['xpath']
                                          + "/ancestor::li[@class='active']"}
    description_block = {"id": "tab-description"}
    review_button = {"xpath": ".//*[@class='nav nav-tabs']//*[contains(text(),'Reviews')]"}
    review_active_button = {"xpath": review_button['xpath'] + "/ancestor::li[@class='active']"}
    review_block = {"id": "form-review"}
    review_input_name = {"id": "input-name"}
    review_input_review = {"id": "input-review"}
    review_input_rating = {"xpath": ".//*[@name='rating'][@value='5']"}
    review_continue_button = {"id": "button-review"}
