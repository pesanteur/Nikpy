from selenium import webdriver
# this module is used to pull information from environ
# example: environ.get('USERNAME')
# exported as export USERNAME='<insert username here>'
from os import environ
from time import sleep
from bs4 import BeautifulSoup
from collections import OrderedDict
import json
import time

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
   # search_date.send_keys(date)
    search_date.send_keys(date)
   # search_btn = browser.find_element_by_id('btn_srch')
    search_btn = browser.find_element_by_id('btn_srch')
    search_btn.click()

def get_page_source():
    html_source = browser.page_source
    return html_source

def find_table():
    source = get_page_source()
    soup = BeautifulSoup(source, 'lxml')
    table = soup.find('table', attrs={'id': 'GeneralPurchases'})
    return table

def scrape_table():
    table = find_table()
    rows = table.findAll('tr')
    return table

def build_dictionary():
    table = scrape_table()
    table_data = [[cell.text for cell in row('td')] for row in table('tr')]
    table_headers = [cell.text for cell in table('th')]
    results = []
    # slicing here ignores blanks caused by header cells
    for data in table_data[1:]:
       test = OrderedDict(zip(table_headers, data))
       results.append(test)
    return results
if __name__ == "__main__":
    browser = start_browser()
    user = environ.get('NIK_USER')
    pwd = environ.get('NIK_PWD')
    login(user, pwd)
    get_acct_page()
    input_start_date()
    time.sleep(1) # improve on this by using built in wait functions for selenium
    get_page_source()
    time.sleep(1)
    find_table()
    scrape_table()
    results = build_dictionary()
    with open('cars.json', 'w') as outfile:
        json.dump(results, outfile)
    # TODO: Include logic to pull page source.
