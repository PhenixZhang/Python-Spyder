import requests
import pandas as pd
from bs4 import BeautifulSoup
res = requests.get("http://roll.mil.news.sina.com.cn/col/zgjq/index.shtml")
res.encoding = 'GB2312'
# print(res.text)
soup = BeautifulSoup(res.text,'html.parser')
fList = soup.select('.fixList')
# print(fList)
for each in fList[0].select('li'):
	te = each.text.rstrip()[:-14]
	# te = each.text.rstrip()[:-14].rstrip('(图)')
	ti = each.select('.time')[0].text
	a = each.select('a')[0]['href']
	# print(te,ti,a)
text = []
for each in fList[0].select('li'):
	alink = {}
	alink['title'] = te = each.text.rstrip()[:-14]
	alink['time'] = each.select('.time')[0].text
	alink['url'] = each.select('a')[0]['href']
	# print(alink)
	text.append(alink)
df = pd.DataFrame(text)
df.to_csv('text.csv',encoding='GB2312',index=False)