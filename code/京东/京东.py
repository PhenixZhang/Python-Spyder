import re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import pandas as pd
a = pd.DataFrame()
browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)

def search():
	try:
		browser.get('http://www.jd.com')
		browser.maximize_window()
		input = wait.until(
			EC.presence_of_element_located((By.CSS_SELECTOR,'#key'))
		)
		submit = wait.until(
			EC.element_to_be_clickable((By.CSS_SELECTOR,'#search > div > div.form > button')))
		input.send_keys('手机')
		submit.click()
		total = wait.until(
			EC.presence_of_element_located((By.CSS_SELECTOR,'#J_bottomPage > span.p-skip > em:nth-child(1) > b')))
		return total.text
	except TimeoutException:
		return search()

def next_page(pageNumber):
	try:
		browser.execute_script("window.scrollTo(0,6000)")
		time.sleep(2)
		input = wait.until(
			EC.presence_of_element_located((By.CSS_SELECTOR,"#J_bottomPage > span.p-skip > input")))
		submit = wait.until(
			EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_bottomPage > span.p-skip > a')))
		input.clear()
		input.send_keys(pageNumber)
		submit.click()
		wait.until(
			EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#J_bottomPage > span.p-num > a.curr'),str(pageNumber)))
		return get_products()
	except TimeoutException:
		next_page(pageNumber)

p = re.compile('<[^>]+>')

def get_products():
	browser.execute_script("window.scrollTo(0,9700)")
	time.sleep(2)
	wait.until(
		EC.presence_of_element_located((By.CSS_SELECTOR,"#J_goodsList")))
	html = browser.page_source
	soup = BeautifulSoup(html,'lxml')
	items = soup.select("#J_goodsList li.gl-item")
	result = []
	for item in items:
		product = {}
		try:
			product['image'] = 'https:' + item.select(".p-img a img")[0]['src']
		except:
			product['image'] = 'https:' + item.select(".p-img a img")[0]['data-lazy-img']	
		try:
			product['shop'] = item.select('.p-shop a')[0].text
		except:
			product['shop'] = None
		product['price'] = item.select('.p-price strong i')[0].text
		temp = str(item.select('.p-name.p-name-type-2 em')[0])
		print(temp)
		product['item_name'] = str(p.sub("",temp)).strip()
		result.append(product)
	return result

def get_pages(maxpage):
	total_pages = int(search())
	data = get_products()
	for i in range(2,maxpage):
		temp = next_page(i)
		data.extend(temp)
	return data

def write2xls(data):
	df = pd.DataFrame(data,columns=['item_name','price','shop','image'])
	print(len(df))
	# print(df.head(5))
	df.to_excel('phones.xls')

if __name__ == '__main__':
	data = get_pages(50)
	write2xls(data)