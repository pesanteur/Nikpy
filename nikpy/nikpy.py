from datetime import datetime
from os import environ # used to get setup variables from the environ
from selenium import webdriver
from .login_util import login_user
from .navi_util import date_range
from .data_util import get_car_data_as_json, get_table_data
from .pic_pull import pic_pull, thumbnail_dl, download_images
from collections import OrderedDict
import json
import os
import requests
import pdfkit # converts html to pdf
from  datetime import datetime

class NikPy:
    "Class to be instantiated to use the script"
    def __init__(self, username=None, password=None):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(25) #causes selenium to wait 25 seconds before throwing an error

        self.log_file = open('./logs/log_file.txt', 'a')
        self.log_file.write('Session started - %s\n'\
                            % (datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        self.username = username or environ.get('NIK_USER')
        self.password = password or environ.get('NIK_PW')
        self.date = None # standard date, can be updated. Date Form: 2016/09/14

    def login(self):
        "Used to login the user with the Nik username and password"
        if not login_user(self.browser, self.username, self.password):
            print('The login details are incorrect.')
            self.log_file.write('Wrong login details.\n')

            self.aborting = True
        else:
            print('Logged in successfully!')
            self.log_file.write('Logged in successfully!\n')

        return self

    def navigate(self, date):
        "Used to navigate to main account page."
        self.date = date
        #TODO: Include start and end date range in date range util
        date_range(self.browser, self.date)
        print('Navigated to desired page!')
        self.log_file.write('Navigated to desired page\n')
        print('Start date %s' % date)
        self.log_file.write('Start date %s ' % date)
        return self

    def get_car_info(self):
        "Used to grab car info from table"
        results = get_car_data_as_json(self.browser, self.date)
        print('Car data pulled!')
        self.log_file.write('Car data pulled!\n')
        # for some reason context manager below does not work when filename built.
        # Context manager did not work as you need to create a path like in table_path below
        with open('car_info.json', 'w') as outfile:
            json.dump(results, outfile)

        return self

    def get_pic_urls(self, download=False):
        "Used to grab pic urls and download to desired folders"
        #TODO: Make this more pythonic. Test context manager.
        urls, table = pic_pull(self.browser) # this fixed issue of table pul
        if download == True:
            url_data = OrderedDict(urls)
            with open('urls.json', 'w') as outfile:
                json.dump(url_data, outfile)
            print('Urls downloaded.')
            self.log_file.write('Urls downloaded.\n')
        else:
            print('Urls obtained')
            self.log_file.write('Urls obtained!\n')
            url_dict = dict(urls)
            for key, values in url_dict.items():
                folder_path = os.path.join('Car Photos', key)
                if os.path.exists(folder_path): #This may be redundant as pic pull already checks that images have been downloaded
                    print('Folder path: %s already exists' % folder_path)
                    self.log_file.write('Folder path: %s already exists\n' % folder_path)
                    continue
                else:
                    print('Building folder: %s' % folder_path)
                    make_folder = os.makedirs(folder_path)
                    for value in values:
                        print("Now downloading image file: %s" % os.path.basename(value))
                        self.log_file.write('Now downloading image file:%s\n '% os.path.basename(value))
                        res = requests.get(value)
                        image_file = open(os.path.join(folder_path, os.path.basename(value)), 'wb')
                        for chunk in res.iter_content(100000):
                            image_file.write(chunk)
                        image_file.close()


            table_data = OrderedDict(table)
            table_dict = dict(table)
            for key, value in table_dict.items():
                folder_path = os.path.join('Car Photos', key)
                # Below now works
                if os.path.exists(folder_path):
                    print('Checking Folder path: %s for data tables.' % folder_path)
                    self.log_file.write('Checking Folder path: %s for data tables.\n' % folder_path)
                    table_path = os.path.join(folder_path, 'car_data.json')
                    if os.path.exists(table_path):
                        continue
                    else:
                        with open(table_path, 'w') as table_file:
                            json.dump(value, table_file)
                        print('Downloaded data table!')
                        self.log_file.write('Car tables downloaded!\n')
                else:
                    print('No such vehicle yet!')
            print("Downloading complete!")
            self.log_file.write('Downloading complete!\n')
        return self


    def get_by_code(self, code):
        #TODO: Expand on this function
        """Grabs car info by NIKKYO Code no."""
        car_url = "http://www.nikkyocars.com/n2014/stock/stock-view.asp?history=true&code=" + code + "&lang=en"
        self.browser.get(car_url)
        folder_path = os.path.join('Car Photos', code)
        if os.path.exists(folder_path):
            print('Folder path: %s already exists' % folder_path)
            self.log_file.write('Folder path: %s already exists\n' % folder_path)
        else:
            print('Building folder: %s' % folder_path)
            make_folder = os.makedirs(folder_path)
        # TODO: break down get pic urls into multiple functions so we can pull further
        thumbnails = self.browser.find_elements_by_class_name('poppic')
        if thumbnails:
            links = thumbnail_dl(self.browser)
            download_images(links, code)
        else:
            print('There is no such code on the Nikkyo Database')
            self.log_file.write('There is no NK code: %s\n' % code)
        return self


    # TODO: Create function that pulls invoicing information by code
    # use pdfkit to convert html to pdf
    """
    def get_invoice_info(self, code):
        "Grabs invoice info and stores it as a pdf programmatically"
        pass
        excertificate_eng_url_structure = "http://www.nikkyocars.com/n2014/member/account/cce_menu.asp?code="+ code +"&cetype=2"
        excertificate_jap_url_structure = "http://www.nikkyocars.com/n2014/member/account/ccj_menu.asp?code="
        chassis_no = None #TODO: Get last four digits of Chassis No. from somewhere above!
        pdfkit.from_url([invoice url, excertificate_eng_url_structure, excertificate_jap_url_structure], '%s.pdf' % chassis_no)
        # HOWTO: grab html behind login pages using requests --> https://stackoverflow.com/questions/40644929/create-pdf-of-a-https-webpage-which-requires-login-using-pdfkit
    """

    def end(self):
        """Closes the current session"""
        if self.browser:
            print("Closing browser")
            self.browser.delete_all_cookies()
            self.browser.close()
            print("Browser closed.")
        print('')
        print('Session ended')
        print('--------------')

        self.log_file.write('\nSession ended - {}\n'.format(
            datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            )
        )
        self.log_file.write('-' * 20 + '\n\n')
        self.log_file.close()
