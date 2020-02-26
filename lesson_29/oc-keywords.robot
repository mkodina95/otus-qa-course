*** Settings ***
Library  Selenium2Library

*** Keywords ***
Open admin page
    Open browser    http://127.0.0.1/admin   Firefox
    Input Text      id:input-username     user
    Input Text      id:input-password     user
    Click Button    css:button[type='submit']