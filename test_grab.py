import defaultdict
pic_elem = browser.find_elements_by_class_name('carpopup')
car_links = defaultdict(list)
for i in pic_elem:
    part_link = i.find_element_by_css_selector('a').get_attribute('href')
    full_link = "http://www.nikkyo.gr.jp" + part_link
    code_no = i.text
    car_links[code_no].append(full_link)
