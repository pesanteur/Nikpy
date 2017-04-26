from selenium import webdriver
# this module is used to pull information from environ
# example: environ.get('USERNAME')
# exported as export USERNAME='<insert username here>'
from os import environ
from time import sleep
from bs4 import BeautifulSoup



def start_browser():
        url = "http://www.nikkyo.gr.jp"
        browser = webdriver.Chrome()
        browser.get(url)
        return  browser

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

def input_start_date(date='2016/06/14'):
	search_date = browser.find_element_by_id('srch_term_start')
	search_date.clear()
        search_date.send_keys(date)
	search_btn = browser.find_element_by_id('btn_srch')
        search_btn.click()

def get_page_source():
        html_source = browser.page_source
        return html_source

def find_table():
        source = get_page_source()
        soup = BeautifulSoup(source)
        table = soup.find('table', attrs={'id': 'GeneralPurchases'})
        return table

def scrape_table():
        table = find_table()
        rows = table.findAll('tr')

if __name__ == "__main__":
	browser = start_browset()
        user = environ.get('USERNAME')
	pwd = environ.get('PASSWORD')
	login(user, pwd)
	get_acct_page()
	input_start_date()
        # TODO: Include logic to pull page source.
