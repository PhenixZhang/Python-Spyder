import time
import requests

base_url = 'http://www.tianqihoubao.com/aqi/'
citys = ['beijing',     'shanghai',    'tianjin',   'chongqing',\
        'haerbin',      'changchun',   'shenyang',  'huhehaote',\
        'shijiazhuang', 'taiyuan',     'xian' ,     'jinan',\
        'wulumuqi',     'lasa',        'xining',    'lanzhou',\
        'yinchuan',     'zhengzhou',   'nanjing',   'taibei',\
        'wuhan',        'hangzhou',    'fuzhou',    'nanchang',\
        'changsha',     'guiyang',     'chengdu',   'guangzhou',\
        'kunming',      'nanning',     'shenzhen',  'haikou']
a = 0
for i in range(len(citys)):
    time.sleep(5)
    url = base_url + citys[i] + '-201811.html'
    response = requests.get(url)
    response.raise_for_status()
    print(a + 1)