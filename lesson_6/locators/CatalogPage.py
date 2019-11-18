class CatalogPage:
    """
The file contains locators for the catalog page
    """
    categories_list = ".//*[@class='list-group']"  # class
    category_item = ".//*[@class='list-group']/*[contains(text(),[0])]"
    content_block = "content"  # id
    sort_list_button = ".//*[@data-original-title='List']"
    sort_grid_button = ".//*[@data-original-title='Grid']"
    sort_dropdown = ".//*[@id='input-sort']/*[text()=[0]]"
    sort_button = "input-sort"  # id
    items_per_page_dropdown = ".//*[@id='input-limit']/*[text()='Default']"
    items_per_page_button = "input-limit"  # id
    product_item = ".//*[contains(@class, 'product-layout')]"
    product_item_image = product_item + "//*[@class='image']"
    product_item_description = product_item + ".//*[@class='caption']"
    product_item_price = product_item + ".//*[@class='price']"
    add_to_cart_button = product_item + "//*[contains(@class, 'fa-shopping-cart')]"
    add_to_wishlist_button = product_item + "//*[contains(@class, 'fa-heart')]"
    compare_button = product_item + "//*[contains(@class, 'fa-exchange')]"
