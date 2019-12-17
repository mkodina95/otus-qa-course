"""
The file contains locators for the admin page
"""


class Admin:
    logo = {"id": "header-logo"}
    panel_heading = {"id": "panel-heading"}
    panel_block = {"id": "panel-body"}
    username_input = {"id": "input-username"}
    password_input = {"id": "input-password"}
    forgotten_password_line = {"id": "help-block"}
    login_button = {"xpath": ".//*[@class='btn btn-primary']"}
    user = {"xpath": ".//*[@alt='John Doe']"}
    add_new_download_button = {"xpath": ".//*[@class='btn btn-primary']"}
    upload_file_button = {"id": "button-upload"}
    upload_file_input = {"xpath": ".//*[@id='form-upload']/input"}
