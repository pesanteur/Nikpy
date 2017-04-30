"""Collects specific data from account page"""
from bs4 import BeautifulSoup
from collections import OrderedDict
import json
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

def get_car_data_as_json(browser, date, table_id='GeneralPurchases'):
    """Gets data about cars from main table."""
    delay = 4 # seconds
    try:
        element_present = EC.presence_of_element_located((By.ID, table_id))
        WebDriverWait(browser, delay).until(element_present)
        print('Page is ready')
    except TimeoutException:
        print('Loading took too much time.')
    html_source = browser.page_source
    soup = BeautifulSoup(html_source, 'lxml')
    table = soup.find('table', attrs={'id': table_id})
    rows = table.findAll('tr') # not sure if I still need this, leave until tested
    table_data = [[cell.text for cell in row('td')] for row in table('tr')] # gets all table data except headers and places it into a list
    table_headers = [cell.text for cell in table('th')] # gets table headers and places it into a list
    results = []
    for data in table_data[1:]: # slicing here ignores blank list created because of headers
        data_dictionary = OrderedDict(zip(table_headers, data))
        results.append(data_dictionary)
    #TODO: have this build json file without deleting previous file. Possibly use log to improve
    return results, date, table_id
"""
    # I think below doesn't work because it's writing within this function
    filename = "%s_%s.json" % (table_id, date)
    with open(filename, 'w') as outfile:
        json.dump(results, outfile)
"""
