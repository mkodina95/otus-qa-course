
*** Settings ***
Documentation    Suite description
Library          Selenium2Library
Resource  oc-keywords.robot

*** Variables ***
${CATALOG}                      id:menu-catalog
${CATEGORIES}                   xpath=//*[text()='Categories']
${ADD_NEW_BUTTON}               xpath=//*[@id='content']//*[@data-original-title='Add New']
${CATEGORY_NAME_FIELD}          xpath=//*[@id="input-name1"]
${META_TAG_TITLE_FIELD}         xpath=//*[@id="input-meta-title1"]
${SAVE_BUTTON}                  xpath=//*[@id='content']//*[@data-original-title='Save']
${CATEGORY_NAME}                xpath=//*[text()='Category Name']
${CATEGORY_NAME_BEFORE_SORT}    xpath=//*[text()='Cameras']
${CATEGORY_NAME_AFTER_SORT}     xpath=//*[text()='Tablets']
${NEW_CATEGORY}                 Apple
${NEW_TAG}                      apple
${CATEGORY_TO_DELETE}           xpath=//*[@id='content']//tbody//*[@type='checkbox'][1]
${DELETE_BUTTON}                xpath=//*[@id='content']//*[@data-original-title='Delete']

*** Test Cases ***
Add New category
    Open admin page
    Click Element                       ${CATALOG}
    Wait Until Element Is Visible       ${CATEGORIES}
    Click Element                       ${CATEGORIES}
    Click Element                       ${ADD_NEW_BUTTON}
    Click Element                       ${CATEGORY_NAME_FIELD}
    Input Text                          ${CATEGORY_NAME_FIELD}             ${NEW_CATEGORY}
    Click Element                       ${META_TAG_TITLE_FIELD}
    Input Text                          ${META_TAG_TITLE_FIELD}            ${NEW_TAG}
    Click Element                       ${SAVE_BUTTON}
    Wait Until Element Is Not Visible   ${SAVE_BUTTON}
    Close browser

Delete the category
    Open admin page
    Click Element                       ${CATALOG}
    Wait Until Element Is Visible       ${CATEGORIES}
    Click Element                       ${CATEGORIES}
    Wait Until Element Is Visible       ${CATEGORY_TO_DELETE}
    Click Element                       ${CATEGORY_TO_DELETE}
    Click Element                       ${DELETE_BUTTON}
    Handle Alert
    Close browser

Change the order of categories
    Open admin page
    Click Element                       ${CATALOG}
    Wait Until Element Is Visible       ${CATEGORIES}
    Click Element                       ${CATEGORIES}
    Wait Until Element Is Visible       ${CATEGORY_NAME_BEFORE_SORT}
    Click Element                       ${CATEGORY_NAME}
    Wait Until Element Is Not Visible   ${CATEGORY_NAME_BEFORE_SORT}
    Wait Until Element Is Visible       ${CATEGORY_NAME_AFTER_SORT}
    Close browser