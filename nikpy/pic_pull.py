"""Pulls pictures from account page on website"""
import os
from .data_util import get_table_data

def pic_pull(browser): # maybe change this to just get pics and then create another to download the pictures or nah?
    """Pulls picture URLs from page, then iterates through and downloads pictures"""
    #TODO: Break this down into a smaller function to make it more readable
    pic_elem = browser.find_elements_by_class_name('carpopup')
    car_links = []
    table_data = []
    downloaded = os.listdir('Car Photos') # list of images already downloaded
    table_links = []
    for link in pic_elem:
        pic_url = link.get_attribute('href')
        code_no = link.text
        if code_no in downloaded:
            print('These images have already been downloaded.')
            files = [f for f in os.listdir(os.path.join('Car Photos', code_no))]
            car_data = 'car_data.json'
            if car_data in files:
                print('Table uploaded!')
                continue
            else:
                print('Table not uploaded') #TODO: Start pulling tables here. How to make pull happen with viewing below...maybe remove other else statement?
                """
                car_links.append((code_no,pic_url))
                # This breaks main code somehow TODO: Fix this later
                # Maybe just delete all images and have new program pull all pictures!
                for code, link in car_links:
                    browser.get(link)
                    car_info_table = get_table_data(browser)[0] # gets html table data about the cars || This works after testing with pdb

                    table_links.append((code, car_info_table))
                """
            continue
        else:
            car_links.append((code_no,pic_url))

    pic_links = []

    if not table_links:
        for code, link in car_links:
            print('Navigating to car with CODE no.: %s' % code)
            browser.get(link)

            car_info_table = get_table_data(browser)[0] # gets html table data about the cars || This works after testing with pdb
            thumbnails = browser.find_elements_by_class_name('poppic')

            inner_links = []
            print('Downloading URLs from thumbnails for CODE no.: %s' % code)
            for picture in thumbnails:
                car_pic = picture.get_attribute('href')
                basename = os.path.basename(car_pic)
                print("URL for pic %s grabbed" % basename)
                inner_links.append(car_pic)
           #pic_links.append(((code, car_info_table), inner_links)) # pic_links is structured like this so it can be turned into a dictionary
            table_links.append((code, car_info_table)) # This works as well therefore issue must be in nikpy.py
            pic_links.append((code, inner_links)) # pic_links is structured like this so it can be turned into a dictionary

    return pic_links, table_links # switch from car_links to pic_links
