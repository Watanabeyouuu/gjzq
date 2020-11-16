"""
@author: Francis | 韩 心 海
@contact: xinhai_han@icloud.com
@file: url_crawler.py
@date: 2020/11/16 4:50 下午

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

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/85.0.4183.83 Safari/537.36 "
}
cookies = {'cookie': ''}

url_lst = []


def url_data(url):
    res = requests.get(url, cookies=cookies, headers=headers)
    d = res.text
    soup = BeautifulSoup(d, "html.parser")
    return soup


def text_url_c():  # 用于爬取所有文章的url
    soup = url_data('http://www.csindex.com.cn/zh-CN/indices/notices-and-announcements?index=&start_date=&end_date'
                    '=&notice_type=2&index_series=all')
    title = soup.find_all('tr')

    # print(title[1].a['href'])  # 链接
    # print(title[1].a.get_text())  # 文件名
    for i in range(1, len(title)):
        url_lst.append(title[i].a['href'])
    print(url_lst)  #所有url


def text_c():  # 爬取文章内容
    soup = url_data('http://www.csindex.com.cn/zh-CN/indices/notices-and-announcements-detail/1424')
    # print(soup)
    print(soup.find_all('p'))


if __name__ == '__main__':
    # text_c()
    text_url_c()