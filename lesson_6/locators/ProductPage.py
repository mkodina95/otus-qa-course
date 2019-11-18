class ProductPage:
    """
The file contains locators for the product page
    """
    breadcrumb = ".//*[@class='breadcrumb']"  # class
    product_images = ".//*[@class='thumbnails']"  # class
    alert_line = ".//*[contains(@class, 'alert')]"  # xpath
    wishlist_button = ".//*[contains(@class, 'fa-heart')]/ancestor::*[@class='btn btn-default']"
    compare_button = ".//*[contains(@class, 'fa-exchange')]/ancestor::*[@class='btn btn-default']"
    quantity_input = "input-quantity"  # id
    add_to_card_button = "button-cart"  # id
    share_buttons = "addthis_toolbox addthis_default_style"  # class
    description_button = ".//*[@class='nav nav-tabs']//*[text()='Description']"
    description_active_button = description_button + "/ancestor::li[@class='active']"
    description_block = "tab-description"  # id
    review_button = ".//*[@class='nav nav-tabs']//*[contains(text(),'Reviews')]"
    review_active_button = review_button + "/ancestor::li[@class='active']"
    review_block = "form-review"  # id
    review_input_name = "input-name"  # id
    review_input_review = "input-review"  # id
    review_input_rating = ".//*[@name='rating'][@value='5']"
    review_continue_button = "button-review"  # id
