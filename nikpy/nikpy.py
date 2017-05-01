from datetime import datetime
from os import environ # used to get setup variables from the environ
from selenium import webdriver
from .login_util import login_user
from .navi_util import date_range
from .data_util import get_car_data_as_json
from .pic_pull import pic_pull
from collections import OrderedDict
import json

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
        self.date = '2016/06/14' # standard date, can be updated

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

    def navigate(self):
        "Used to navigate to main account page."
        date_range(self.browser, self.date)
        print('Navigated to desired page!')
        self.log_file.write('Navigated to desired page')

        return self

    def get_car_info(self):
        "Used to grab car info from table"
        results = get_car_data_as_json(self.browser, self.date)
        print('Car data pulled!')
        self.log_file.write('Car data pulled!')
        # for some reason context manager below does not work when filename built. TODO: figure out why in future
        with open('test.json', 'w') as outfile:
            json.dump(results, outfile)

        return self

    def get_pic_urls(self, download=False):
        "Used to grab pic urls"
        urls = pic_pull(self.browser)
        if download == True:
            url_data = OrderedDict(urls)
            with open('urls.json', 'w') as outfile:
                json.dump(url_data, outfile)
            print('Urls downloaded.')
            self.log_file.write('Urls downloaded.')
        else:
            print('Urls obtained')
            print(urls)

        return self
  #TODO: Include function to download all images from URL

