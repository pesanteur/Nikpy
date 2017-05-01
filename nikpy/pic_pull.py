"""Pulls pictures from account page on website"""
from bs4 import BeautifulSoup
import requests

def pic_pull(browser): # maybe change this to just get pics and then create another to download the pictures or nah?
    """Pulls picture URLs from page, then iterates through and downloads pictures"""
    pic_elem = browser.find_elements_by_class_name('carpopup')
    car_links = []
    for link in pic_elem:
        pic_url = link.get_attribute('href')
        code_no = link.text
        car_links.append((code_no,pic_url))
    # can turn this into a dictionary in future by simply doing dict(car_links) or using OrderedDict
    pic_links = []
    # print(car_links)

    for code, link in car_links:
        browser.get(link)
        thumbnails = browser.find_elements_by_class_name('popic')

        inner_links = []
        for picture in thumbnails:
      #  Ideally I want this whole function to just grab links as that way we can close selenium instead of having it open - which is slow.
      #  So need to store links in a way that we can save them and refer to them. Only thing unique is code number so we should probably use that.
            car_pic = picture.get_attribute('href')
            inner_link.append(car_pic)

        pic_links.append((code, inner_links))
    browser.close()

    return car_links
