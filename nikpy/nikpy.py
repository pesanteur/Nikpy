from datetime import datetime
from os import environ # used to get setup variables from the environ
from selenium import webdriver
from .login_util import login_user
from .navi_util import date_range
from .data_util import get_car_data_as_json, get_table_data
from .pic_pull import pic_pull
from collections import OrderedDict
import json
import os
import requests
from tqdm import tqdm

#TODO: For every print add log details, so we can keep track of where this fails
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
        self.date = '2016/09/14' # standard date, can be updated. TODO: Update this to date range

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
        #TODO: Include start and end date range in date range util
        date_range(self.browser, self.date)
        print('Navigated to desired page!')
        self.log_file.write('Navigated to desired page\n')

        return self

    def get_car_info(self):
        "Used to grab car info from table"
        results = get_car_data_as_json(self.browser, self.date)
        print('Car data pulled!')
        self.log_file.write('Car data pulled!\n')
        # for some reason context manager below does not work when filename built. TODO: figure out why in future
        with open('car_info.json', 'w') as outfile:
            json.dump(results, outfile)

        return self

    def get_pic_urls(self, download=False):
        "Used to grab pic urls and download to desired folders"
        #TODO: Make this more pythonic. Test context manager.
        urls = pic_pull(self.browser)
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
                folder_path = os.path.join('Car Photos', key[0])
                if os.path.exists(folder_path):
                    print('Folder path: %s already exists' % folder_path)
                    self.log_file.write('Folder path: %s already exists\n' % folder_path)
                    continue
                else:
                    print('Building folder: %s' % folder_path)
                    make_folder = os.makedirs(folder_path)
                    # This can break url_dict in main module. Need to fix this.
                    # Error that comes up in main module is : TypeError:- unhashable type list
                    car_desc_file = open(os.path.join(folder_path, os.path.basename(key[0])), 'wb')
                    car_desc_file.write(key[1])
                    car_desc_file.close()
                    for value in values:
                        print("Now downloading image file: %s" % os.path.basename(value))
                        self.log_file.write('Now downloading image file:%s\n '% os.path.basename(value))
                        res = requests.get(value)
                        image_file = open(os.path.join(folder_path, os.path.basename(value)), 'wb')
                        for chunk in res.iter_content(100000):
                            image_file.write(chunk)
                        image_file.close()
            print("Downloading complete!")
            self.log_file.write('Downloading complete!\n')
        return self


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
