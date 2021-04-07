import requests
from bs4 import BeautifulSoup
import re
import random
import time
import pandas as pd

s = requests.session()#使用session来保存登陆信息

#获取动态ip，防止ip被封
def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list
#随机从动态ip链表中选择一条ip
def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies
 
#实现模拟登陆
def Login(headers,loginUrl,formData):
    r = s.post(loginUrl, data=formData, headers=headers) # 提交登录信息
    print (r.url)
    print (formData["redir"])
    if r.url == formData["redir"]:
        print ("登陆成功") # 若登录后返回的页面是想要爬去的页面则说明登录成功
    else:
        print ("第一次登陆失败")
        page = r.text
        soup = BeautifulSoup(page, "html.parser")
        captchaAddr = soup.find('img', id='captcha_image')['src'] # 获得登录验证码的URL
        print (captchaAddr)
 
        reCaptchaID = r'<input type="hidden" name="captcha-id" value="(.*?)"/'
        captchaID = re.findall(reCaptchaID, page)
 
        captcha = input('输入验证码：')
 
        formData['captcha-solution'] = captcha
        formData['captcha-id'] = captchaID
 
        r = s.post(loginUrl, data=formData, headers=headers)# 再次提交登录信息，加上了手动输入的验证码
        print (r.status_code)
        return r.cookies # 记录下cookie信息
#获取评论内容和下一页链接
def get_data(html):
    soup = BeautifulSoup(html,"lxml")
    username_list = [s.get_text() for s in soup.select('.comment-info > a')]
    time_list = [s.get_text() for s in soup.select('.comment-info > span.comment-time')]
    useful_list = [s.get_text() for s in soup.select('.comment-vote > span')]
    comment_list = [s.get_text() for s in soup.select('.comment > p')]
    next_page = soup.select('.next')[0].get('href')
    return username_list,time_list,useful_list,comment_list,next_page
 
if __name__ =="__main__":
    absolute = 'https://movie.douban.com/subject/26752088/comments'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}
    loginUrl = 'https://www.douban.com/accounts/login?source=movie'
    formData = {
        "redir":"https://movie.douban.com/subject/26752088/comments",
        "form_email":"账号",
        "form_password":"密码",
        "login":u'登录'
    }
    #获取动态ip
    url = 'http://www.xicidaili.com/nn/'
    cookies = Login(headers,loginUrl,formData)
    ip_list = get_ip_list(url, headers=headers)
    proxies = get_random_ip(ip_list)
 
    current_page = absolute
    next_page = ""
    time_list = []
    useful_list = []
    username_list = []
    comment_list = []
    temp_list = []
    num = 0
    while(1):
        html = s.get(current_page, cookies=cookies, headers=headers, proxies=proxies).content
        temp0_list,temp1_list,temp2_list,temp_list,next_page = get_data(html)
        if next_page is None:
            break
        current_page = absolute + next_page
        username_list = username_list + temp0_list
        time_list = time_list + temp1_list
        useful_list = useful_list + temp2_list
        comment_list = comment_list + temp_list
        #time.sleep(1 + float(random.randint(1, 100)) / 20)
        num = num + 1
        #每20次更新一次ip
        if num % 20 == 0:
            proxies = get_random_ip(ip_list)
        print (current_page)

    #写入csv文件
    infos = {'username': username_list,'date': time_list,'useful': useful_list,'comment': comment_list}
    data = pd.DataFrame(infos, columns=['username','date','useful','comment'])
    data.to_csv("D:/豆瓣《我不是药神》.csv")