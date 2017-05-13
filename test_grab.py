from collections import defaultdict
import requests
import re

pic_elem = browser.find_elements_by_class_name('carpopup')
car_links = defaultdict(list)
for i in pic_elem:
    # part_link = i.find_element_by_css_selector('a').get_attribute('href')
    # full_link = "http://www.nikkyo.gr.jp" + part_link
    link = i.get_attribute('href') # must be signed in to view these links, cannot scrape otherwise
    code_no = i.text # code is also in URL
    car_links[code_no].append(full_link)
    # TODO: Build these links into a list/dictionary/json file. Then scrape with a tool like scrapy to speed up the process


browser.get(pic_url) # this can then be navigated to get the pictures (hopefully)
thumbnails = browser.find_elements_by_class_name('popic')
pic_list = []

for i in thumbnails:
    car_pic = i.get_attribute('href') # Don't need to be logged in to pull these so can be done outside of selenium to improve speed
    pic_list.append(car_pic)
    # TODO: to pull code from this url
    """Url here would look like https://www.website.com/n2014/etc/etc-view.asp?history=true&code={CODENO}&lang=en"""


# TODO: Iterate through list and download image using requests
for picture in pic_list:
    res = requests.get(picture)
    image_file = open(os.path.join('nik_pictures', os.path.basename(picture)), 'wb') # TODO: Regex is too much work just use split
    """Url here would look like https://etc.etc.com/etc/etc/2017/AB/AB{CODENO}-{PICNO}.jpg"""
    # to split above into code number  picture.split('/')[-1].splt(-)[0] You'll get make code here as well can be split out in future but might be important
    for chunk in res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()
