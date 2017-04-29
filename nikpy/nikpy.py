from datetime import datetime
from os import environ # used to get setup variables from the environ
from selenium import webdriver
from login_util import login_user

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

  #TODO: Add additional functions to class.

