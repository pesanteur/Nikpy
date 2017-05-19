"""Pulls pictures from account page on website"""
import os
from .data_util import get_table_data

def pic_pull(browser): # maybe change this to just get pics and then create another to download the pictures or nah?
    """Pulls picture URLs from page, then iterates through and downloads pictures"""
    pic_elem = browser.find_elements_by_class_name('carpopup')
    car_links = []
    table_data = []
    downloaded = os.listdir('Car Photos') # list of images already downloaded
    for link in pic_elem:
        pic_url = link.get_attribute('href')
        code_no = link.text
        if code_no in downloaded:
            print('These images have already been downloaded.')
            continue
        else:
            car_links.append((code_no,pic_url))
    # can turn this into a dictionary in future by simply doing dict(car_links) or using OrderedDict
    pic_links = []
    table_links = []
    # print(car_links)

    for code, link in car_links:
        print('Navigating to car with CODE no.: %s' % code)
        browser.get(link)
        # TODO: pull table data for cars here
        car_info_table = get_table_data(browser)[0] # gets html table data about the cars
        thumbnails = browser.find_elements_by_class_name('poppic')

        inner_links = []
        print('Downloading URLs from thumbnails for CODE no.: %s' % code)
        for picture in thumbnails:
            car_pic = picture.get_attribute('href')
            basename = os.path.basename(car_pic)
            print("URL for pic %s grabbed" % basename)
            inner_links.append(car_pic)
       #pic_links.append(((code, car_info_table), inner_links)) # pic_links is structured like this so it can be turned into a dictionary
        table_links.append((code, car_info_table))
        pic_links.append((code, inner_links)) # pic_links is structured like this so it can be turned into a dictionary
    #TODO: Continue to build out table pull
"""
    for code in downloaded:
         car_info_table = get_table_data(browser)[0] # gets html table data about the cars
"""
    return pic_links, table_links # switch from car_links to pic_links
