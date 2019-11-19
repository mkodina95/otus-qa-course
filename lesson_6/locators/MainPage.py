class MainPage:
    """
The file contains locators for the Main page
    """
    class Header:
        logo = "logo"
        search_input = ".//*[@class='form-control input-lg']"
        search_button = ".//*[@class='btn btn-default btn-lg']"
        cart_button = ".//*[@id='cart']//*[@type='button']"

    class Menu:
        menu = ".//*[@class='navbar']"
        dropdown_tablets = ".//*[contains(@class, 'navbar-nav')]//*[text()='Tablets']"
        dropdown = ".//*[contains(@class, 'navbar-nav')]//*[text()='[0]']"
        dropdown_menu = dropdown + "/ancestor::li"
        dropdown_menu_item = dropdown_menu + "//*[contains(text(), [1])]"

    class Promo:
        promo_block = "slideshow0"
        promo_mac_block = ".//*[@id='slideshow0']//*[@alt='MacBookAir']"
        promo_iphone_block = ".//*[@id='slideshow0']//*[@alt='iPhone 6']"
        next_button = ".//*[@id='slideshow0']//ancestor::*[@class='swiper-viewport']//*[@class='swiper-button-next']"
        prev_button = ".//*[@id='slideshow0']//ancestor::*[@class='swiper-viewport']//*[@class='swiper-button-prev']"

    class Footer:
        footer = ".//*[text()='OpenCart']/ancestor::div[@class='container']"
        footer_item = footer + "[text()=[0]"
