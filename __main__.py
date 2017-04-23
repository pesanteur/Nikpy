from selenium import webdriver

url = "http://www.nikkyo.gr.jp"

browser = webdriver.Chrome()
browser.get(url)

def login(username, password):
	username = browser.find_element_by_id('userlogin')
	password = browser.findd_element_by_id('password')
	username.send_keys(username)
	password.send_keys(password)
	password.submit()
	
def get_stock_page():
	stock_elem = browser.find_element_by_link_text('STOCK')
	stock_elem.click()
