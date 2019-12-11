"""
The file contains locators for the login page
"""


class Login:
    logo = {"id": "header-logo"}
    panel_heading = {"id": "panel-heading"}
    panel_block = {"id": "panel-body"}
    username_input = {"id": "input-username"}
    password_input = {"id": "input-password"}
    forgotten_password_line = {"id": "help-block"}
    login_button = {"xpath": ".//*[@class='btn btn-primary']"}
    user = {"xpath": ".//*[@alt='John Doe']"}
