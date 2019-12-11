"""
The file contains locators for top menu block
"""


class Menu:
    menu = {"xpath": ".//*[@class='navbar']"}
    dropdown_tablets = {"xpath": ".//*[contains(@class, 'navbar-nav')]//*[text()='Tablets']"}
    dropdown = {"xpath": ".//*[contains(@class, 'navbar-nav')]//*[text()='[0]']"}
    dropdown_menu = {"xpath": dropdown['xpath'] + "/ancestor::li"}
    dropdown_menu_item = {"xpath": dropdown_menu['xpath'] + "//*[contains(text(), [1])]"}
