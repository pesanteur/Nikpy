from selenium import webdriver
# this module is used to pull information from environ
# example: environ.get('USERNAME')
# exported as export USERNAME='<insert username here>'
from os import environ

url = "http://www.nikkyo.gr.jp"

browser = webdriver.Chrome()
browser.get(url)

def login(user, pwd):
	username = browser.find_element_by_id('userlogin')
	password = browser.find_element_by_id('password')
	username.send_keys(user)
	password.send_keys(pwd)
	password.submit()

def get_stock_page():
	stock_elem = browser.find_element_by_link_text('MY NIKKYO')
	stock_elem.click()

def get_acct_page():
	acct_elem = browser.find_element_by_id('account_report_btn')
	acct_elem.click()

def input_start_date():
	search_date = browser.find_element_by_id('srch_term_start')
	search_date.send_keys('2016/06/14')
	search_btn = browser.find_element_by_id('btn_srch')
	search_btn.click()

if __name__ == "__main__":
	user = environ.get('USERNAME')
	pwd = environ.get('PASSWORD')
	login(user, pwd)
	get_stock_page()
	get_acct_page()
        # TODO: Fix input start date. Currently doesn't work as is.
	input_start_date()
        # TODO: Include logic to pull page source.
