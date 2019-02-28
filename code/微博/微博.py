from urllib.parse import urlencode  #url编码
import requests #python网络请求库
from pyquery import PyQuery as pq      #网页解析库库

base_url = 'https://m.weibo.cn/api/container/getIndex?' #基本url
headers = {
    'Host':'m.weibo.cn',
    'Referer':'https://m.weibo.cn/u/1216903164',
    'User-Agent':'Mozilla/5.0(Macintoch;Intel Mac OS X 10_13_3)AppleWebkit/537.36(KHTML,like Gecko)chrome/65.0.3325.162 Safari/537.6',
    'X-Requested-With':'XMLHttpRequest',
}               #请求头

# 用于获取页面
def get_page(page):
    params = {
        'type':'uid',
        'value':'1216903164',
        'containerid':'1076031216903164',
        'page':page
    }           #get参数
    url = base_url + urlencode(params) #组合http请求
    try:            #异常处理
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)

#用于解析页面
def parse_page(json):
    if json:    #如果json不为空,即已爬到数据,继续执行
        items = json.get('data').get('cards')   #
        for item in items:
            item = item.get('mblog')
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            weibo['attitudes'] = item.get('attributes_count')
            weibo['comments'] = item.get('comments_count')
            weibo['reposts'] = item.get('reposts_count')
            yield weibo

#将其保存为txt
def save2txt(result):
    with open('aaa.txt','a+',encoding = 'utf-8') as fp:
        resultstring = str(result)
        fp.write(resultstring)
        fp.write('\n')
        
#主程序
if __name__ == "__main__":
    for page in range(1,101):
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            print(result)
            save2txt(result)