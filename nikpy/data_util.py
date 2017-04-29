"""Collects specific data from account page"""

def get_car_data(browser, date='2016/06/14'):
    acct_elem = browser.find_element_by_id('account_report_btn')
    acct_elem.click()


