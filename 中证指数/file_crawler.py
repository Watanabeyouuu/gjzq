"""
@author: Francis | 韩 心 海
@contact: xinhai_han@icloud.com
@file: file_crawler.py
@date: 2020/11/16 3:50 下午

# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓   ┏┓
            ┏┛┻━━━┛┻━━┓
            ┃    ☃    ┃
            ┃  ┳┛  ┗┳ ┃
            ┃     ┻   ┃
            ┗━┓     ┏━┛
              ┃     ┗━━━━━┓
              ┃  神兽保佑  ┣┓
              ┃　永无BUG！ ┏┛
              ┗━━━┓┓┏━━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import csv
import datetime
import re
import threading
import time
import os
from urllib.request import urlretrieve

import requests
from bs4 import BeautifulSoup

threads = []

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/85.0.4183.83 Safari/537.36 "
}
cookies = {'cookie': ''}


def url_data(url):
    res = requests.get(url, cookies=cookies, headers=headers)
    d = res.text
    soup = BeautifulSoup(d, "html.parser")
    return soup


soup = url_data('http://www.csindex.com.cn/uploads/indices/info/files/20191105/1572934794798584.pdf')
print(soup)
os.makedirs('data/', exist_ok=True)  # 创建目录存放文件
image_url = 'http://www.csindex.com.cn/uploads/indices/info/files/20191105/1572934794798584.pdf'
urlretrieve(image_url, 'data/ppp.pdf')
