"""
The file contains tests for uploading the file
"""
from helper import HelperUrl
from lesson_9.page_object.AdminPage import AdminPage


def test_upload(open_browser):
    HelperUrl.admin_catalog_downloads(open_browser)
    AdminPage(open_browser) \
        .input_username("user") \
        .input_password("user") \
        .submit() \
        .verify_logged_on() \
        .add_new_download() \
        .upload_file("/Users/m.kodina/otus-qa-course/lesson_10/img/123.jpeg") \
