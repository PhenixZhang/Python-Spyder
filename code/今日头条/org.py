# -*- coding: UTF-8 -*-
import requests
from urllib import request
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pyquery import PyQuery as pq
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import json
class app_data:
    def __init__(self):
        self.headers = {'Accept-Charset': 'UTF-8',
                   'X-Requested-With': 'XMLHttpRequest',
                   'Host': 'lf-hl.snssdk.com',
                   'Connection': 'Keep-Alive',
                   'Accept-Encoding': 'gzip',
                   'X-SS-REQ-TICKET': '1544235590880',
                   'sdk-version': '1',
                   'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.0; HUAWEI CAZ-AL10 Build/HUAWEICAZ-AL10) NewsArticle/7.0.1 cronet/TTNetVersion:pre_blink_merge-277498-gd2bb364e 2018-08-24',
                   'X-SS-TC': '0'
                   }
        self.headers2 = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip,deflate',
            'Accept-Language': 'zh-CN,en-US;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; HUAWEI CAZ-AL10 Build/HUAWEICAZ-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36 JsSdk/2 NewsArticle/7.0.1 NetType/wifi',
            'X-Requested-With': 'com.ss.android.article.news'
        }


    def catch_app_data(self,link):
        if not link:
            link=self.heros_url1
        req = requests.get(url=link, headers=self.headers,verify=False).json()

        data = req.get("data")
        name = data.get("name")
        print('账号：', name)

        verified_content = data.get("verified_content")
        print('认证：', verified_content)

        area = data.get("area")
        print('位置：', area)

        description = data.get("description")
        print('简介：', description)

        user_id = data.get("user_id")
        print('user_id：', user_id)


    def cat_app_list(self,keyword='中餐厅'):
        url = 'https://lf-hl.snssdk.com/api/search/content/?from=search_tab' \
                     '&keyword='+keyword+'' \
                     '&cur_tab_title=search_tab' \
                     '&plugin_enable=3' \
                     '&iid=53115531269' \
                     '&device_id=52727404130' \
                     '&ac=wifi' \
                     '&channel=huawei&aid=13' \
                     '&app_name=news_article' \
                     '&version_code=701' \
                     '&version_name=7.0.1' \
                     '&device_platform=android' \
                     '&ab_group=94567' \
                     '%252C102749%252C181430' \
                     '&abflag=3' \
                     '&device_type=HUAWEI%2BCAZ-AL10' \
                     '&device_brand=HUAWEI' \
                     '&language=zh' \
                     '&os_api=24' \
                     '&os_version=7.0' \
                     '&uuid=864590038380239' \
                     '&openudid=47628a3804ad50be' \
                     '&manifest_version_code=701' \
                     '&resolution=1080*1788' \
                     '&dpi=480' \
                     '&update_version_code=70108' \
                     '&_rticket=1544497762334' \
                     '&fp=DrT_L2w1cST5FlT_F2U1FYK7FrxO' \
                     '&tma_jssdk_version=1.5.4.2' \
                     '&rom_version=emotionui_5.0.4_caz-al10c00b386' \
                     '&plugin=26958&search_sug=1' \
                     '&forum=1&count=10' \
                     '&format=json' \
                     '&source=input' \
                     '&pd=synthesis' \
                     '&keyword_type=' \
                     '&action_type=input_keyword_search' \
                     '&search_position=search_tab' \
                     '&from_search_subtab=' \
                     '&offset=0' \
                     '&search_id=' \
                     '&has_count=0&qc_query='

        head = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip,deflate',
            'Accept-Language': 'zh-CN,en-US;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; HUAWEI CAZ-AL10 Build/HUAWEICAZ-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36 JsSdk/2 NewsArticle/7.0.1 NetType/wifi',
            'X-Requested-With': 'com.ss.android.article.news'
        }
        req = requests.get(url=url, headers=head,verify=False).json()
        data = req.get("data")

        url_list = []
        for item in data:
            display_list = item.get('display')
            if display_list:
                album_group_dict = display_list.get('album_group')
                if album_group_dict:
                    extra = str(album_group_dict.get('extra'))
                    item_list = extra.split(',')
                    for e in item_list:
                        if e.find("album_group_url") > -1:
                            url = e[e.find(":") + 1:]
                            url = url.replace("\"", "")
                            url_list.append(url)
                            break
                else:
                    url = display_list.get('url')
                    if url:
                        url_list.append(url)


        print(url_list)

    def catchdata_sogo(self,url):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.set_page_load_timeout(10)
        self.driver.maximize_window()
        # self.driver = webdriver.PhantomJS(service_args=['--load-images=false'])
        # self.driver.set_page_load_timeout(20)
        # self.driver.maximize_window()
        try:
            self.driver.get(url)
            print(url)
            # handles = self.driver.window_handles  # 获取当前窗口句柄集合（列表类型）
            # self.driver.switch_to.window(handles[2 - 1])
            time.sleep(2)

            selenium_html = self.driver.execute_script("return document.documentElement.outerHTML")
            doc = pq(selenium_html)
            elements = doc("div[class='content-txt']").find("p")
            for element in elements.items():
                print(element.text())

            elements = doc("p[class='mod-base-item']").find("span")
            for element in elements.items():
                print(element.text())



        except Exception as ex:
            print(ex)

    def catchdata_so(self, url):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.set_page_load_timeout(10)
        self.driver.maximize_window()
        # self.driver = webdriver.PhantomJS(service_args=['--load-images=false'])
        # self.driver.set_page_load_timeout(20)
        # self.driver.maximize_window()
        try:
            self.driver.get(url)
            print(url)
            # handles = self.driver.window_handles  # 获取当前窗口句柄集合（列表类型）
            # self.driver.switch_to.window(handles[2 - 1])
            time.sleep(2)

            selenium_html = self.driver.execute_script("return document.documentElement.outerHTML")
            doc = pq(selenium_html)
            elements = doc("div[class='cp-info-main']")
            for element in elements.items():
                print(element('h3').text())
                # print(element("p[class='js-info-upinfo']").text())
                print(element('p').text())




        except Exception as ex:
            print(ex)
    def test(self,link):
        req = requests.get(url=link, headers=self.headers2, verify=False)
        json_str = req.content.decode()
        print(json_str)



if __name__ == '__main__':
    obj = app_data()
    # http://m.video.so.com/android/va/Zs5sb3Ny7JA4DT.html
    # https://m.douguo.com/search/trecipe/%E4%B8%AD%E9%A4%90%E5%8E%85/0?f=tt
    # https://baike.sogou.com/m/fullLemma?ch=jrtt.search.item&cid=xm.click&lid=167408303
    # obj.catch_app_data('')
    # 湖南卫视中餐厅

    # keywords = ['湖南卫视中餐厅','农广天地','看台','十年','CCTV-4远方的家','CCTV热线12']
    # for keyword in keywords:
    #     obj.cat_app_list(keyword)
    #     print('\n')
    obj.cat_app_list('CCTV热线12')
    # obj.catchdata_sogo('https://baike.sogou.com/m/fullLemma?ch=jrtt.search.item&cid=xm.click&lid=167408303#lemmaHome')
    # obj.catchdata_so('http://m.video.so.com/android/va/Zs5sb3Ny7JA4DT.html')
    # obj.catchdata_so('http://m.video.so.com/android/va/YcMpcKVv82YBDz.html')
    # obj.parserurl()
    # obj.test('http://m.video.so.com/android/va/Zs5sb3Ny7JA4DT.html')