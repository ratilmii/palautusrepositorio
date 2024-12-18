*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  ellak
    Set Password  ellak123
    Set Password Confirmation  ellak123
    Submit Registration Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ee
    Set Password  ellak123
    Set Password Confirmation  ellak123
    Submit Registration Credentials
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  ellak
    Set Password  ell
    Set Password Confirmation  ell
    Submit Registration Credentials
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  ellak
    Set Password  ellakalle
    Set Password Confirmation  ellakalle
    Submit Registration Credentials
    Register Should Fail With Message  Password must contain at least one number

Register With Nonmatching Password And Password Confirmation
    Set Username  ellak
    Set Password  ellak123
    Set Password Confirmation  ellak456
    Submit Registration Credentials
    Register Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  ellak123
    Set Password Confirmation  ellak123
    Submit Registration Credentials
    Register Should Fail With Message  Username already exists

Login After Successful Registration
    Set Username  ellak
    Set Password  ellak123
    Set Password Confirmation  ellak123
    Submit Registration Credentials
    Register Should Succeed
    Click Link  Continue to main page
    Click Button  Logout
    Login Page Should Be Open
    Set Username  ellak
    Set Password  ellak123
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Set Username  ellak
    Set Password  ell
    Set Password Confirmation  ell
    Submit Registration Credentials
    Register Should Fail With Message  Password must be at least 8 characters long
    Click Link  Login
    Login Page Should Be Open
    Set Username  ellak
    Set Password  ell
    Click Button  Login
    Page Should Contain  Invalid username or password   


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${expected_message}
    Register Page Should Be Open
    Page Should Contain  ${expected_message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}    

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}        

Submit Registration Credentials
    Click Button  Register    

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

