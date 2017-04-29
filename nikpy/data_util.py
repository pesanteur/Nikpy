"""Collects specific data from account page"""
from bs4 import BeautifulSoup
from collections import OrderedDict
import json

def get_car_data(browser, date='2016/06/14', table_id='GeneralPurchases'):


    def get_page_source(browser):
        html_source = browser.page_source
        return html_source

    def find_table(table_id):
        source = get_page_source()
        soup = BeautifulSoup(source, 'lxml')
        table = soup.find('table', attrs={'id': table_id})
        rows = table.findAll('tr')
        return table

    def build_dictionary():
        table = find_table(table_id)
        table_data = [[cell.text for cell in row('td')] for row in table('tr')]
        table_headers = [cell.text for cell in table('th')]
        results = []
        for data in table_data[1:]:
            test = OrderedDict(zip(table_headers, data))
            results.append(test)
        return results

    def build_json():
        #TODO: have this build json file without deleting previous file. Possibly use log to improve
        results = build_dictionary()
        filename = "%s_%s.json" % (table_id, date)
        with open(filename, 'w') as outfile:
            json.dump(results, outfile)

