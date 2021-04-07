# import requests
# res = requests.get("https://www.baidu.com")
# print(type(res))
# print(res.status_code)
# print(type(res.text))
# print((res.text)[:15])
# print(res.cookies)


# import requests
# res = requests.get("http://httpbin.org/get")
# print(res.text)


# import requests
# data = {
# 	'building':"zhongyuan",
# 	'nature':"administrative"
# }
# res = requests.get("http://httpbin.org/get",params=data)
# print(res.text)



# import requests
# res = requests.get("http://httpbin.org/get")
# print(type(res.text))
# print(res.json())
# print(type(res.json()))

# import requests
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
# }
# res = requests.get("http://httpbin.org/get",headers=headers)
# print(res.text)


# import requests
# data = {
#     'user': 'admin',
#     'pass': 'admin'
# }
# res = requests.post('http://httpbin.org/post', data=data) 
# print(res.text)


import re
# content= "hello 123 4567 World_This is a regex Demo"
# result = re.match('^hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$',content)
# print(result)
# print(result.group()) #获取匹配的结果
# print(result.span())  #获取匹配字符串的长度范围


# content= "hello 123 4567 World_This is a regex Demo"
# result = re.match('^hello.*Demo$',content)
# print(result)
# print(result.group())
# print(result.span())


# content= "hello 123 4567 World_This is a regex Demo"
# result = re.match('^hello\s(\d+).*Demo$',content)
# print(result.group())
# print(result.group(1))


# content= "hello 123 4567 World_This is a regex Demo"
# result = re.match('^hello.*(?P<name>\d+).*Demo$',content)
# print(result.group())
# print(result.group(1))
# print(result.groupdict())


# content= "hello 123 4567 World_This is a regex Demo"
# result = re.match('^hello.*?(?P<name>\d+).*Demo$',content)
# print(result.group())
# print(result.group(1))
# print(result.groupdict())


# content= "heLLo 123 4567 World_This is a regex Demo"
# result = re.match('hello',content,re.I)
# print(result.group())

# content= '''hahhaha hello 123 4567 world'''
# result = re.search('hello.*world',content)
# print(result.group())

# content= '''
#     <url>http://httpbin.org/get</url>
#     <url>http://httpbin.org/post</url>
#     <url>https://www.baidu.com</url>'''
# urls = re.findall('<url>(.*)</url>',content)
# for url in urls:
#     print(url)


# content= '''hello 123 4567 world'''
# str = re.sub('123.*world','future',content)
# print(str)


# content= '''hello 123 4567 world'''
# pattern = '123.*world'
# regex = re.compile(pattern)
# str = re.sub(regex,'future',content)
# print(str)


from lxml import etree
text = '''<html><body><div>
    <ul>
        <li class="item-0"><a href="link1.html">first</a></li>
        <li class="item-1"><a href="link2.html">second</a>
        <li class="item-2"><a href="link3.html">third</a></li>
        <li class="item-3"><a href="link4.html">fourth</a></li>
    </ul>
</div>'''
html = etree.HTML(text)
result = etree.tostring(html)
# print(result.decode('utf-8'))

# print(html.xpath('//*')) # 获取所有的节点
# print(html.xpath('//li')) # 获取所有li节点
# print(html.xpath('//li/a')) # 所有li下是所有直接a子节点
# print(html.xpath('//ul//a')) # 所有ul下的子孙a节点​


# 找到所有a节点中href为links.html的父节点的class值
#  ..  来实现查找父节点
# print(html.xpath('//a[@href="link1.html"]/../@class'))

# 找到class值为item-0是节点
# print(html.xpath('//li[@class="item-0"]')) 

# # 匹配到class值为item-0节点中的a标签中的文本
# print(html.xpath('//li[@class="item-0"]/a/text()'))

# 找到li下a中的href属性值
# print(html.xpath('//li/a/@href'))  

#只要节点属性class中包含li就能匹配出来
# print(html.xpath('//li[contains(@class,"item")]/a/text()')) 

# 匹配节点属性class值为item，class值为item-0的节点
# print(html.xpath('//li[contains(@class,"item") and @class="item-0"]/a/text()'))


html = '''
<!DOCTYPE html>
<html>
<head>
    <meta content="text/html;charset=utf-8" http-equiv="content-type" />
    <meta content="IE=Edge" http-equiv="X-UA-Compatible" />
    <meta content="always" name="referrer" />
    <link href="https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/bdorz/baidu.min.css" rel="stylesheet" type="text/css" />
    <title>百度一下，你就知道 </title>
</head>
<body link="#0000cc">
  <div id="wrapper">
    <div id="head">
        <div class="head_wrapper">
          <div id="u1">
            <a class="mnav" href="http://news.baidu.com" name="tj_trnews">新闻 </a>
            <a class="mnav" href="https://www.hao123.com" name="tj_trhao123">hao123 </a>
            <a class="mnav" href="http://map.baidu.com" name="tj_trmap">地图 </a>
            <a class="mnav" href="http://v.baidu.com" name="tj_trvideo">视频 </a>
            <a class="mnav" href="http://tieba.baidu.com" name="tj_trtieba">贴吧 </a>
            <a class="bri" href="//www.baidu.com/more/" name="tj_briicon" style="display: block;">更多产品 </a>
          </div>
        </div>
    </div>
  </div>
</body>
</html>'''


# from bs4 import BeautifulSoup 
# bs = BeautifulSoup(html,"html.parser") # 缩进格式
# print(bs.prettify()) # 获取title标签的所有内容
# print(bs.title) # 获取title标签的名称
# print(bs.title.name) # 获取title标签的文本内容
# print(bs.title.string) # 获取head标签的所有内容
# print(bs.head) # 获取第一个div标签中的所有内容
# print(bs.div) # 获取第一个div标签的id的值
# print(bs.div["id"]) # 获取第一个a标签中的所有内容
# print(bs.a) # 获取所有的a标签中的所有内容
# print(bs.find_all("a")) # 获取id="u1"
# print(bs.find(id="u1")) # 获取所有的a标签，并遍历打印a标签中的href的值
# for item in bs.find_all("a"): 
#     print(item.get("href")) # 获取所有的a标签，并遍历打印a标签的文本值
# for item in bs.find_all("a"): 
#     print(item.get_text())


# # [document] #bs 对象本身比较特殊，它的 name 即为 [document]
# print(bs.name) 
# # head #对于其他内部标签，输出的值便为标签本身的名称
# print(bs.head.name) 
# # 在这里，我们把 a 标签的所有属性打印输出了出来，得到的类型是一个字典。
# print(bs.a.attrs) 
# #还可以利用get方法，传入属性的名称，二者是等价的
# print(bs.a['class']) # 等价 bs.a.get('class')
# # 可以对这些属性和内容等等进行修改
# bs.a['class'] = "newClass"
# print(bs.a) 
# # 还可以对这个属性进行删除
# del bs.a['class'] 
# print(bs.a)



# print(bs.title.string) 
# print(type(bs.title.string))



# print(bs.a)
# # 此时不能出现空格和换行符，a标签如下：
# # <a class="mnav" href="http://news.baidu.com" name="tj_trnews"><!--新闻--></a>
# print(bs.a.string) # 新闻
# print(type(bs.a.string)) # <class 'bs4.element.Comment'>


# from bs4 import BeautifulSoup 
# import re 
# t_list = bs.find_all(re.compile("a")) 
# for item in t_list: 
#    print(item)


# from bs4 import BeautifulSoup 
# import re 
# # 返回只有一个结果的列表
# t_list = bs.find_all("title",limit=1) 
# print(t_list) 
# # 返回唯一值
# t = bs.find("title") 
# print(t) 
# # 如果没有找到，则返回None
# t = bs.find("abc") 
# print(t)

# print(bs.select('title'))
# print(bs.select('a'))

# print(bs.select('.mnav'))


from pyquery import PyQuery as pq

# doc = pq(html)
# print(doc('title').text()) # '标题'
# print(doc('div').filter('.head_wrapper').text()) # '文字1'
# print(doc('a[name=tj_trnews]').text()) # 同上，只是这种方法支持除了id和class之外的属性筛选
# print(doc('div').filter('#u1').find('a').text()) # '列表1第1项 列表1第2项'
# print(doc('div#u1 a').text()) # 简化形式
# print(doc('div#u1 > a').text()) # 节点之间用>连接也可以，但是加>只能查找子元素，空格子孙元素


# 字符串初始化：
from pyquery import PyQuery as pq
doc=pq(html)
# print(doc('li'))
# # URL初始化
# doc=pq(url="https://ww.baidu.com")
# print(doc)
# # 文件初始化
# a = open('test.html','r',encoding='utf8')
# doc=pq(a.read())
# print(doc)

# # id 为container,class为list下的所有li
# print(doc('.head_wrapper #u1 a'))

# # .find():查找所有子孙节点
# items = doc('#u1')
# print(items.find('a'))

# # .children():查找子节点
# items=doc('#u1')
# print(items.children('.mnav'))

# # 父节点
# doc=pq(html)
# items=doc('.mnav')
# print(items.parent())
# print(items.parents())

# # 兄弟节点
# doc=pq(html)
# li=doc('.mnav')
# print(li.siblings('.bri'))


# # 用items()函数生成列表生成器进行遍历
# doc=pq(html)
# lis=doc('a').items()
# for li in lis:
#   print(li)


# # 获取属性
# a=doc('.head_wrapper #u1 .bri')
# # attr只会输出第一个a节点属性，要用items()遍历
# print(a.attr('href'))


# # 获取文本
# # .text()
# a=doc('.head_wrapper #u1 .bri')
# # text()函数会输出所有的li文本内容
# print(a.text())

# # .html()
# li=doc('a')
# # html()只会输出第一个li节点内的HTML文本
# print(li.html())





# removeClass addClass
a=doc('.head_wrapper #u1 .bri')
print(a)
a.removeClass('bri')  # 移除active的class
print(a)
a.addClass('bri')   # 增加active的class
print(a)

# attr text html
a.attr('name','link')    # 增加属性name=link
a.text('changed item')   # 改变文本 changed item
a.html('<span>changed item </span>')   # 改变HTML
print(a)

 # remove()
u1=doc('#u1')
# 删除wrap中p节点
u1.find('a').remove()
print(u1.text())
# 伪类选择器