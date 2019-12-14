"""
The file contains locators for the catalog page
"""


class Catalog:
    categories_title = {"xpath": ".//*[@id='content']/h2"}
    categories_list = {"xpath": ".//*[@class='list-group']"}
    category_item = {"xpath": ".//*[@class='list-group']/*[contains(text(),'{0}')]"}
    content_block = "content"
    sort_list_button = {"xpath": ".//*[@data-original-title='List']"}
    sort_grid_button = {"xpath": ".//*[@data-original-title='Grid']"}
    sort_dropdown = {"xpath": ".//*[@id='input-sort']/*[text()='{0}']"}
    sort_button = "input-sort"
    items_per_page_dropdown = {"xpath": ".//*[@id='input-limit']/*[text()='Default']"}
    items_per_page_button = "input-limit"
    product_item = {"xpath": ".//*[contains(@class, 'product-layout')]"}
    product_item_image = {"xpath": product_item['xpath'] + "//*[@class='image']"}
    product_item_description = {"xpath": product_item['xpath'] + ".//*[@class='caption']"}
    product_item_price = {"xpath": product_item['xpath'] + ".//*[@class='price']"}
    add_to_cart_button = {"xpath": product_item['xpath'] + "//*[contains("
                                                           "@class, 'fa-shopping-cart')]"}
    add_to_wishlist_button = {"xpath": product_item['xpath'] + "//*[contains(@class, 'fa-heart')]"}
    compare_button = {"xpath": product_item['xpath'] + "//*[contains(@class, 'fa-exchange')]"}
