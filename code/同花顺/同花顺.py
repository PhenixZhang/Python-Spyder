import requests
from bs4 import BeautifulSoup
import time
import json
import pandas as pd

def craw_page(page_id):
	headers = {
		'host':'q.10jqka.com.cn',
		'Referer':'http://q.10jqka.com.cn/',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3554.0 Safari/537.36',
		'X-Requested-With':'XMLHttpRequest'
	}
	url = 'http://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/%s/ajax/1/' % page_id
	res = requests.get(url,headers=headers)
	res.encoding = 'GBK'
	soup = BeautifulSoup(res.text,'lxml')
	tr_list = soup.select('tbody tr')
	# print(tr_list)
	yeji = []
	for each_tr in tr_list:
		td_list = each_tr.select('td')
		data = {
		'股票代码':td_list[1].text,
		'股票简称':td_list[2].text,
		'现价':td_list[3].text,
		'涨幅':td_list[4].text,
		'涨跌':td_list[5].text,
		'涨速':td_list[6].text,
		'换手':td_list[7].text
		}
		yeji.append(data)
	return yeji

def craw_pages(page_n):
	YEJI = []
	for page_id in range(1,page_n+1):
		page = craw_page(page_id)
		YEJI.extend(page)
		time.sleep(10)
	return YEJI

def write2csv(result):
	json_result = json.dumps(result)
	with open('yeji.json','w') as f:
		f.write(json_result)
	with open('yeji.json','r') as f:
		data = f.read()
	data = json.loads(data)
	df = pd.DataFrame(data,columns=['股票代码','股票简称','现价','涨幅','涨跌','涨速','换手'])
	df.to_csv('yeji.csv',encoding='GBK',index=False)

if __name__ == '__main__':
	result = craw_pages(10)
	write2csv(result)