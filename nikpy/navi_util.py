"""Navigates Nik page"""

def date_range(browser, date):
    #browser.get("http://www.nikkyocars.com/n2014/member/account/accountreport.asp") # clicking seems to be faster than just getting here
    #TODO: Switch back to click
    acct_elem = browser.find_element_by_id('account_report_btn')
    acct_elem.click()
    search_date = browser.find_element_by_id('srch_term_start')
    search_date.clear()
    search_date.send_keys(date)
    search_btn = browser.find_element_by_id('btn_srch')
    search_btn.click()

    return True
