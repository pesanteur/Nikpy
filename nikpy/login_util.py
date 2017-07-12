"""Module used for the login portion of the script"""
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sleenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

def login_user(browser, username, password):
    """Login with user password and username"""
    account_report_id = "account_report_btn" # used to navigate to next step: account report
    browser.get('http://www.nikkyocars.com')
    username_elem = browser.find_element_by_id('userlogin')
    password_elem = browser.find_element_by_id('password')
    username_elem.send_keys(username)
    password_elem.send_keys(password)
    password_elem.submit()

    delay = 3 # seconds
    try:
        element_present = EC.presence_of_element_located((By.ID, account_report_id))
        WebDriverWait(browser, delay).until(element_present)
    except TimeoutException:
        print('Loading took too much time.')
