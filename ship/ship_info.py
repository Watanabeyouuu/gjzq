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
data_lst = []
all_data_lst = []


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


def write_c():
    with open('data/IMO_MMSI.csv', "w", newline='', encoding='utf-8-sig') as f:
        field_names = ["Name", "IMO", "MMSI"]
        f_csv = csv.DictWriter(f, fieldnames=field_names)
        f_csv.writeheader()
        for i in data_lst:
            f_csv.writerow(
                {
                    "Name": i['Name'],
                    "IMO": i['IMO'],
                    "MMSI": i['MMSI'],

                }
            )


def main():
    read_c()
    for i in name_lst:
        try:
            soup = url_data('http://searchv3.shipxy.com/shipdata/search3.ashx?f=auto&kw=%s' % i)
            data = json.loads(soup.text)['ship'][0]
            IMO = data['i']
            MMSI = data['m']
            # print('NAME:', i, 'IMO:', IMO, 'MMSI:', MMSI)
            data_lst.append({
                'Name': i,
                'IMO': IMO,
                'MMSI': MMSI
            })
        except Exception as e:
            continue
    write_c()


if __name__ == '__main__':
    main()
