import requests
import time
from pyquery import PyQuery as pq
import re
from urllib.parse import urlencode
import csv

base_url="https://movie.douban.com/subject/26683723/comments?"
headers={
 'Cookie':'**************************',
   }

def save_to_csv(list):
    with open("后来的我们.csv","w",encoding = 'utf-8',newline='') as f:
        writer = csv.writer(f)
        for info in list:
            #print(info)
            writer.writerow([info])
 
def parse_content(html):
    doc = pq(html)  # 得到网页源码
    contents = doc('.comment-item p').items()
    return contents
 
def get_page_html(page):
 
    data={
        'start':(page-1)*20,
        'limit':20,
        'status':'F'
    }
    queries=urlencode(data)
    url=base_url+queries
    html=get_html(url)
    return html
 
#解析html页面
def get_html(url):
    print('crawing ', url) # 输出正在爬去的url
    response = requests.get(url,headers=headers)
    time.sleep(1)  # 暂停一秒
    return response.text
 
#获取总的评论的条数
def parse_comment(html):
    doc=pq(html) # 得到网页源码
    num=doc('#content > div > div.article > div.clearfix.Comments-hd > ul > li.is-active > span').text()#获取span标签的内容
    num=re.findall('\d+',num)[0]
    return num
 
def main():
    comment_list=[]
    print("start")
    index_html=get_html("https://movie.douban.com/subject/26683723/comments?status=F")
    print(parse_comment(index_html))
    total_num=parse_comment(index_html)
    pagenum=int(total_num)/20+1
    for page in range(1, int(pagenum)):
         print('page= '+str(page))
         page_html=get_page_html(page)
         if page_html:
             contents=parse_content(page_html)
             for content in contents:
                 print(content.text())
                 comment_list = comment_list + [content.text()]
    save_to_csv(comment_list)
 
 
 
if __name__=="__main__" :
    main()