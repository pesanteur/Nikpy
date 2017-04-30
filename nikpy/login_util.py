"""Module used for the login portion of the script"""
from time import sleep

def login_user(browser, username, password):
    """Login with user password and username"""
    browser.get('http://www.nikkyocars.com')
    username_elem = browser.find_element_by_id('userlogin')
    password_elem = browser.find_element_by_id('password')
    username_elem.send_keys(username)
    password_elem.send_keys(password)
    password_elem.submit()

    sleep(3)

    main_div = browser.find_elements_by_id('main_div') # Check is main_div, this div only on main page
    if main_div:
        return False
    else:
        return True
