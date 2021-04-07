import time
import requests
from bs4 import BeautifulSoup


##import re
class spider_douban():
    def __init__(self):
        self.href = []  # 电影链接
        self.movie_name = []  # 电影名：list中英other
        self.derector_act = []  # 电影导演和主演等
        self.review = []  # 简评
        self.comment = []  # 评分和评价数
        self.errors = []

    def getHtml(self, page):
        url = 'https://movie.douban.com/top250?start=%s&filter=' % page
        print("url:  " + url)
        req = requests.get(url)
        ##    req.encoding = "UTF-8"
        return req.text

        # bs4

    def parseHtml_bs4(self, text):

        soup = BeautifulSoup(text, "lxml")  # 解析器lxml或者html.parser
        content = soup.select("#wrapper #content")  # 返回列表，列表内的内容才能select
        title = content[0].select("h1")[0].text  # list没有text，所以得[0]先取出
        ##    print(title)
        content2 = content[0].select(".article .grid_view")
        ##        print(len(content2))
        for li in content2[0].select("li"):
            try:
                # li>item下主要两个标签pic和info
                ##        pic_href = li.select(".item .pic")#该电影链接和图片，info中也有电影链接
                ##        href = pic_href[0].select("a")[0]["href"]
                # info下主要两个标签hd>a和bd
                hd = li.select(".item .info .hd a")  # 包括电影链接、中英文名、简评
                self.href.append(hd[0]["href"])  # 电影链接
                movie_namec_e = hd[0].select(".title")  # 返回列表[中文名，英文名]
                ##        for i in movie_namec_e:
                ##            print(i)
                ##        break
                zh_name = movie_namec_e[0].text
                try:  # 可能不存在英文名
                    en_name = movie_namec_e[1].text
                except:
                    en_name = None
                    ##        print(en_name)
                    ##        break
                try:
                    oth_name = hd[0].select(".other")[0].text
                except:
                    oth_name = None
                self.movie_name.append([zh_name, en_name, oth_name])
                ##        for i in L:
                ##            print (i)
                bd = li.select(".item .info .bd")  # 包括导演、主演、发行时间国家、电影类型；评星评分和评价数；简评
                ##        print(bd)
                movie_infor = bd[0].select("p")
                self.derector_act.append(movie_infor[0].text)
                self.review.append(movie_infor[1].text)  # 简评
                ##        print(derector_act,comment)
                L2 = []
                for span in bd[0].select(".star"):
                    ##            print(span.text)
                    if span.text:
                        L2.append(span.text.strip("\n"))  # 评分和评价数
                self.comment.append(L2)
                ##        print(L2)
                ##           break
            except Exception as e:
                self.errors.append(e)

    def save(self):
        if self.errors:  # 保存error信息
            print("(self.errors)It's bad,there is something wrong waiting for handling!!")
        else:
            print(None, "good")
            ##        for href,movie_name,derector_act,review,comment in\
            ##            zip(self.href,self.movie_name,self.derector_act, self.review, self.comment):
            ##            print(href,movie_name,derector_act,review,comment)
            ##            print("----------------")

    def page_to_page(self, start, end):
        i = 0
        while i <= 9:
            getHtml(25 * i)


def start():
    startt = time.clock()
    errors = []  # 存放网页打不开等错误
    i = 0
    demo = spider_douban()
    while i <= 9:
        try:
            text = demo.getHtml(25 * i)
        except Exception as e:
            text = False
            errors.append(e)
        finally:
            if text:
                demo.parseHtml_bs4(text)
            i += 1
    demo.save()
    if errors:
        print("It's bad,there is something wrong waiting for handling!!")
    else:
        print(None, "perfect!!")
    endt = time.clock()
    print("run over!!cost total_time:%s" % (endt - startt))


if __name__ == "__main__":
    start()