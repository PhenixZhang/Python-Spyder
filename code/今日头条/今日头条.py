import requests
import time
from bs4 import BeautifulSoup
import pandas as pd
import json
import random
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

head = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip,deflate',
    'Accept-Language': 'zh-CN,en-US;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; HUAWEI CAZ-AL10 Build/HUAWEICAZ-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36 JsSdk/2 NewsArticle/7.0.1 NetType/wifi',
    'X-Requested-With': 'com.ss.android.article.news'
}

def get_one_page(keyword,offset):
    url = "https://is-lq.snssdk.com/search/?keyword="\
        + keyword + \
        "&from=news"\
        "&is_incognito=0"\
        "&loadId=4"\
        "&keyword_type=hist"\
        "&cur_tab_title=search_tab"\
        "&pd=information"\
        "&source=search_history"\
        "&search_position=search_bar"\
        "&action_type=history_keyword_search"\
        "&search_start_time=1584336475527"\
        "&plugin_enable=3"\
        "&iid=107809327345"\
        "&device_id=68769901841"\
        "&ac=wifi"\
        "&mac_address=14%3A3C%3AC3%3A6A%3A74%3A24"\
        "&channel=store_tengxun_wzl"\
        "&aid=13"\
        "&app_name=news_article"\
        "&version_code=764"\
        "&version_name=7.6.4"\
        "&device_platform=android"\
        "&device_type=SEA-AL10"\
        "&device_brand=HUAWEI"\
        "&language=zh"\
        "&os_api=29"\
        "&os_version=10"\
        "&openudid=35df37eedec6124f"\
        "&manifest_version_code=7640"\
        "&resolution=1080*2259"\
        "&dpi=480"\
        "&update_version_code=76414"\
        "&_rticket=1584336473842"\
        "&plugin=18762"\
        "&tma_jssdk_version=1.55.0.4"\
        "&is_ttwebview=0"\
        "&fetch_by_ttnet=1"\
        "&search_sug=1"\
        "&forum=1"\
        "&from_pd"\
        "&format=json"\
        "&count=10"\
        "&offset="\
        + offset + \
        "&search_id=2020031613561801012902621017163C79"\
        "&traffic_source=undefined"
    req = requests.get(url=url, headers=head,verify=False).json()
    soup = BeautifulSoup(req['scripts'],"lxml")
    contents = soup.find_all('script',attrs={"type":"application/json"})
    res = []
    for content in contents:
        js = json.loads(content.contents[0])
        abstract = js['abstract']
        article_url = js['article_url']
        comment_count = js['comment_count']
        raw_title = js['display']['emphasized']['title']
        title = raw_title.replace("<em>","").replace("</em>","")
        source = js['display']['emphasized']['source']
        data = {
            'title':title,
            'article_url':article_url,
            'abstract':abstract,
            'comment_count':comment_count,
            'source':source
        }
        res.append(data)
    return res

def write2excel(result):
  json_result = json.dumps(result)
  with open('article.json','w') as f:
    f.write(json_result)
  with open('article.json','r') as f:
    data = f.read()
  data = json.loads(data)
  df = pd.DataFrame(data,columns=['title','article_url','abstract','comment_count','source'])
  df.to_excel('article.xlsx',index=False)


def get_pages(keyword,page_n):
  res_n = []
  for page_id in range(page_n):
    page = get_one_page(keyword = keyword,offset = str(page_id*10))
    res_n.extend(page)
    time.sleep(random.randint(1,10))
  return res_n

if __name__ == '__main__':
  keyword = "疫情"
  page_n = 10
  result = get_pages(keyword,page_n)
  write2excel(result)