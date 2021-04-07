import requests
import re
import json

# 定义浏览器头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"
    }

# 定义下载图片函数
def down_image(url,name,headers):
    r = requests.get(url,headers = headers)
    filename = re.search('/public/(.*?)$',url,re.S).group(1)
    with open("film_pic/"+name.split('/')[0]+".jpg",'wb') as f:
        f.write(r.content)

# 定义解析网页函数
def parse_html(url):
    response = requests.get(url, headers=headers)
    text = response.text
    # 正则表达式头部([1:排名 2:图片] [3:名称 4:别名] [5:导演 6:年份/国家/类型] [7:评星 8:评分 9:评价人数] [10:评价])
    regix = '<div class="pic">.*?<em class="">(.*?)</em>.*?<img.*?src="(.*?)" class="">.*?' \
            'div class="info.*?class="hd".*?class="title">(.*?)</span>.*?class="other">(.*?)'\
            '</span>.*?<div class="bd">.*?<p class="">(.*?)<br>(.*?)</p>.*?' \
            'class="star.*?<span class="(.*?)"></span>.*?span class="rating_num".*?average">(.*?)</span>.*?<span>(.*?)</span>.*?' \
            'span class="inq"?>(.*?)</span>'
    # 匹配出所有结果
    res = re.findall(regix, text, re.S)
    for item in res:
        rank = item[0]
        down_image(item[1],item[2],headers = headers)
        name = item[2] + ' ' + re.sub('&nbsp;','',item[3])
        actor =  re.sub('&nbsp;','',item[4].strip())
        year = item[5].split('/')[0].strip('&nbsp;').strip()
        country = item[5].split('/')[1].strip('&nbsp;').strip()
        tp = item[5].split('/')[2].strip('&nbsp;').strip()
        tmp = [i for i in item[6] if i.isnumeric()]
        if len(tmp) == 1:
            score = tmp[0] + '星/' + item[7] + '分'
        else:
            score = tmp[0] + '星半/' + item[7] + '分'
        rev_num = item[8][:-3]
        inq = item[9]
        # 生成字典
        yield {
            '电影名称': name,
            '导演和演员': actor,
            '类型': tp,
            '年份': year,
            '国家': country,
            '评分': score,
            '排名': rank,
            '评价人数': rev_num,
            '评价': inq
        }

# 定义输出函数
def write_movies_file(str):
    with open('top250_douban_film.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(str,ensure_ascii=False) + '\n')

# 定义主函数
def main():
    for offset in range(0, 250, 25):
        url = 'https://movie.douban.com/top250?start=' + str(offset) +'&filter='
        for item in parse_html(url):
            print(item)
            write_movies_file(item)

if __name__ == '__main__':
    main()