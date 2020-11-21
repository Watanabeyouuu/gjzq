"""
@author: Francis | 韩 心 海
@contact: xinhai_han@icloud.com
@file: ship_info.py
@date: 2020/11/21 3:26 下午

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
import json
from urllib.request import urlretrieve

import requests
from bs4 import BeautifulSoup
import pandas as pd

threads = []

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/85.0.4183.83 Safari/537.36 "
}
cookies = {'cookie': ''}
name_lst = []


def url_data(url):
    res = requests.get(url, cookies=cookies, headers=headers)
    d = res.text
    soup = BeautifulSoup(d, "html.parser")
    return soup


def read_c():
    df = pd.read_excel('data/Listing_20201120123932.xlsx', header=None)  # 打开csv文件
    ship_name = df.loc[4:, :][2]
    for i in ship_name:
        name_lst.append(i)
        # name_lst.append(one_line)  # 将读取的csv分行数据按行存入列表‘date’中


def main():
    for i in name_lst:
        try:
            soup = url_data('http://searchv3.shipxy.com/shipdata/search3.ashx?f=auto&kw=%s' % i)
            data = json.loads(soup.text)['ship'][0]
            IMO = data['i']
            MMSI = data['m']
            print('NAME:', i, 'IMO:', IMO, 'MMSI:', MMSI)
        except Exception as e:
            continue


if __name__ == '__main__':
    read_c()
    print(name_lst)
    main()
