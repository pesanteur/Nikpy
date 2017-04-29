"""Navigates Nik page"""

def get_acct_page(browser):
    acct_elem = browser.find_element_by_id('account_report_btn')
    acct_elem.click()

def input_start_date(browser, date='2016/06/14'):
    search_date = browser.find_element_by_id('srch_term_start')
    search_date.clear()
    search_date.send_keys(date)
    search_btn = browser.find_element_by_id('btn_srch')
    search_btn.click()


