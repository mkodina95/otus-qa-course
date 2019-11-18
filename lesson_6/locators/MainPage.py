class MainPage:
    """
The file contains locators for the Main page
    """
    class Header:
        logo = "logo"  # id
        search_input = ".//*[@class='form-control input-lg']"  # class
        search_button = ".//*[@class='btn btn-default btn-lg']"  # class
        cart_button = ".//*[@id='cart']//*[@type='button']"  # xpath

    class Menu:
        menu = ".//*[@class='navbar']"  # class
        dropdown_tablets = ".//*[contains(@class, 'navbar-nav')]//*[text()='Tablets']"  # xpath
        dropdown = ".//*[contains(@class, 'navbar-nav')]//*[text()='[0]']"  # xpath
        dropdown_menu = dropdown + "/ancestor::li"  # xpath
        dropdown_menu_item = dropdown_menu + "//*[contains(text(), [1])]"  # xpath

    class Promo:
        promo_block = "slideshow0"  # id
        promo_mac_block = ".//*[@id='slideshow0']//*[@alt='MacBookAir']"  # xpath
        promo_iphone_block = ".//*[@id='slideshow0']//*[@alt='iPhone 6']"  # xpath
        promo_next_button = ".//*[@id='slideshow0']//ancestor::*[@class='swiper-viewport']//*[@class='swiper-button-next']"  # xpath
        promo_prev_button = ".//*[@id='slideshow0']//ancestor::*[@class='swiper-viewport']//*[@class='swiper-button-prev']"

    class Footer:
        footer = ".//*[text()='OpenCart']/ancestor::div[@class='container']"
        footer_item = footer + "[text()=[0]"
