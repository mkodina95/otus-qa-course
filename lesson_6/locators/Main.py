"""
The file contains locators for the Main page
"""


class Main:
    promo_block = {"xpath": ".//*[@id='slideshow0']"}
    promo_mac_block = {"xpath": ".//*[@id='slideshow0']//*[@alt='MacBookAir']"}
    promo_mac_block_active = {"xpath": ".//*[@id='slideshow0']//*[contains(@class, "
                                       "'swiper-slide-active')]//*[@alt='MacBookAir']"}
    promo_iphone_block = {"xpath": ".//*[@id='slideshow0']//*[@alt='iPhone 6']"}
    promo_iphone_block_active = {"xpath": ".//*[@id='slideshow0']//*[contains(@class,"
                                          " 'swiper-slide-active')]//*[@alt='iPhone 6']"}
    next_button = {"xpath": ".//*[@id='slideshow0']//ancestor::*"
                            "[@class='swiper-viewport']//*[@class='swiper-button-next']"}
    prev_button = {"xpath": ".//*[@id='slideshow0']//ancestor::*["
                            "@class='swiper-viewport']//*[@class='swiper-button-prev']"}
