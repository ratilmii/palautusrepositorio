*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  ellak
    Set Password  ellak123
    Set Password Confirmation ellak123
    Submit Credentials
    Register Should Succeed


Register With Too Short Username And Valid Password
    Set Username  ee
    Set Password  ellak123
    Set Password Confirmation ellak123
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  ellak
    Set Password  ell
    Set Password Confirmation ell
    Submit Credentials
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  ellak
    Set Password  ellak
    Set Password Confirmation ellak
    Submit Credentials
    Register Should Fail With Message  Password must contain at least one number

Register With Nonmatching Password And Password Confirmation
    Set Username  ellak
    Set Password  ellak123
    Set Password Confirmation ellak456
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  ellak123
    Set Password Confirmation ellak123
    Submit Credentials
    Register Should Fail With Message  Username already exists

*** Keywords ***
Register Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${expected_message}
    Page Should Contain  ${expected_message}

Submit Credentials
    Click Button  Register    

*** Keywords ***
Reset Application Create User And Go To Login Page
    Reset Application
    Create User  kalle  kalle123
    Go To Login Page