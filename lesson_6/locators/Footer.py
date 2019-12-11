"""
The file contains locators for footer block
"""


class Footer:
    footer = {"xpath": ".//*[text()='OpenCart']/ancestor::div[@class='container']"}
    footer_item = {"xpath": footer['xpath'] + "[text()=[0]"}
