"""Pulls pictures from account page on website"""
from bs4 import BeautifulSoup

def pic_pull(browser):
    pic_elem = browser.find_elements_by_class_name('carpopup')
    for link in pic_elem:
        link.click()
