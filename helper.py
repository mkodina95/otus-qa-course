"""
Helper file contains functions for choosing the correct url for the tests
"""


class HelperUrl:
    @staticmethod
    def get_admin_base_url(open_browser):
        base_path = open_browser.current_url
        result = base_path + "admin/"
        return result

    @staticmethod
    def get_user_base_url(open_browser):
        base_path = open_browser.current_url
        result = base_path + "index.php"
        return result

    @staticmethod
    def change_to_url(open_browser, path):
        open_browser.get(path)

    @staticmethod
    def user_base_url(open_browser):
        open_browser.get(HelperUrl.get_user_base_url(open_browser))

    @staticmethod
    def admin_base_url(open_browser):
        open_browser.get(HelperUrl.get_admin_base_url(open_browser))

    @staticmethod
    def admin_catalog_downloads(open_browser):
        catalog_download_url = "index.php?route=catalog/download"
        base_url = HelperUrl.get_admin_base_url(open_browser)
        HelperUrl.change_to_url(open_browser, base_url + catalog_download_url)
