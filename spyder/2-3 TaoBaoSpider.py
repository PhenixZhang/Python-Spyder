import requests
import re

infoList = []
#获取html文本
def getHTMLText(url):
    #异常处理函数，当响应时间超过30s或无法正常返回响应，则返回空字符串
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

#解析网页
def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        llt = re.findall(r'\"view_sales\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            link = eval(llt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price,link,title])
    except:
        print("")

# #输出商品列表依次为序号、价格、付款人数、商品名称
# def printGoodsList(ilt):
#     tplt = "{:4}\t{:8}\t{:12}\t{:40}"
#     print(tplt.format("序号", "价格", "付款人数","商品名称"))
#     count = 0
#     for g in ilt:
#         count = count + 1
#         print(tplt.format(count, g[0], g[1],g[2]))


#写入txt
def Write2txt(ilt):
    for item in infoList:
        with open('1.txt','a',encoding = 'utf-8') as fp:
            fp.write(str(item).strip('[',']') + '\n')

#主函数
def main():
    goods = '书包'
    depth = 10
    start_url = 'https://s.taobao.com/search?q=' + goods
    global infoList
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    # printGoodsList(infoList)
    Write2txt(infoList)


main()
# for i in sorted(infoList,key = lambda x:eval(x[0])):
#     print(i)
with open('1.txt','r',encoding = 'utf-8') as fp:
    for i in fp.readlines():
        print(i)