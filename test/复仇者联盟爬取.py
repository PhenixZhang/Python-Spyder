# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 08:20:39 2019

@author: Administrator
"""

import jieba
import requests
import pandas as pd
import time
import random
from lxml import etree
##除了首页，后面的每页 url 地址中只有 start= 的值逐页递增，其他都是不变的。
def start_spider():
    base_url = 'https://movie.douban.com/subject/26266893/comments'
    start_url = base_url + '?start=0' 

    number = 1
    html = request_get(start_url) 

    while html.status_code == 200:
        # 获取下一页的 url
        selector = etree.HTML(html.text)
        nextpage = selector.xpath("//div[@id='paginator']/a[@class='next']/@href")
        nextpage = nextpage[0]
        next_url = base_url + nextpage
        # 获取评论
        comments = selector.xpath("//div[@class='comment']")
        marvelthree = []
        for each in comments:
            marvelthree.append(get_comments(each))

        data = pd.DataFrame(marvelthree)
        # 写入csv文件,'a+'是追加模式
        try:
            if number == 1:
                csv_headers = ['用户', '是否看过', '五星评分', '评论时间', '有用数', '评论内容']
                data.to_csv('Marvel3_yingpping.csv', header=csv_headers, index=False, mode='a+', encoding='utf-8')
            else:
                data.to_csv('Marvel3_yingpping.csv', header=False, index=False, mode='a+', encoding='utf-8')
        except UnicodeEncodeError:
            print("编码错误, 该数据无法写到文件中, 直接忽略该数据")

        data = []

        html = request_get(next_url)
        

def request_get(url):
    '''
    使用 Session 能够跨请求保持某些参数。
    它也会在同一个 Session 实例发出的所有请求之间保持 cookie
    '''
    timeout = 3

    UserAgent_List = [
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36",
            ]
    header = {
            'User-agent': random.choice(UserAgent_List),
            'Host': 'movie.douban.com',
            'Referer': 'https://movie.douban.com/subject/26266893/',
            }

    session = requests.Session()

    cookie = {'cookie': 'bid=qdeUbOmuN98; __utmz=30149280.1554126892.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmz=223695111.1554126892.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ll="118254"; ap_v=0,6.0; _pk_ses.100001.4cf6=*; __utma=30149280.2135661188.1554126892.1554279665.1554358243.3; __utmb=30149280.0.10.1554358243; __utmc=30149280; __utma=223695111.433701188.1554126892.1554279665.1554358243.3; __utmb=223695111.0.10.1554358243; __utmc=223695111; dbcl2="194445243:sZId/cLZWc8"; ck=EoG5; ps=y; push_noty_num=0; push_doumail_num=0; _pk_id.100001.4cf6=4f0d8646b2a483de.1554126891.3.1554358432.1554279775.'}
    time.sleep(random.randint(10, 20))  
    response = requests.get(url, headers=header,cookies=cookie, timeout = 5)
    if response.status_code != 200:
        print(response.status_code)
    return response

##数据获取        
def get_comments(eachComment):
    commentlist = []
    user = eachComment.xpath("./h3/span[@class='comment-info']/a/text()")[0]  # 用户
    watched = eachComment.xpath("./h3/span[@class='comment-info']/span[1]/text()")[0]  # 是否看过
    rating = eachComment.xpath("./h3/span[@class='comment-info']/span[2]/@title")  # 五星评分
    if len(rating) > 0:
        rating = rating[0]
    comment_time = eachComment.xpath("./h3/span[@class='comment-info']/span[3]/@title")  # 评论时间
    if len(comment_time) > 0:
        comment_time = comment_time[0]
    else:
        # 有些评论是没有五星评分, 需赋空值
        comment_time = rating
        rating = ''

    votes = eachComment.xpath("./h3/span[@class='comment-vote']/span/text()")[0]  # "有用"数
    content = eachComment.xpath("./p/span/text()")[0]  # 评论内容
##//*[@id="comments"]/div[1]/div[2]/p
    commentlist.append(user)
    commentlist.append(watched)
    commentlist.append(rating)
    commentlist.append(comment_time)
    commentlist.append(votes)
    commentlist.append(content.strip())
    print(list)
    return commentlist

if __name__=="__main__" :
    start_spider()



        

    



        
        

        
       