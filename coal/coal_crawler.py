"""
@author: Francis | 韩 心 海
@contact: xinhai_han@icloud.com
@file: coal_crawler.py
@date: 2020/10/16 11:31 上午

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
import re
import json
import requests
from bs4 import BeautifulSoup

area_list = []

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/85.0.4183.83 Safari/537.36 "
}


def url_data(url):
    res = requests.get(url, headers=headers)
    d = res.text
    soup = BeautifulSoup(d, "html.parser")
    return soup


# 焦炭库存分地区走势
def coal_area():
    soup = url_data(
        "https://api.mysteel.com/tpl/zhanting_data.html?indexCodes=CO_0001264515,CO_0001264516,CO_0001264517,"
        "CO_0001264518,CO_0001264519,"
        "CO_0001264520&startTime=2019-10-16&callback=jQuery1830451560469201848_1602820643617&_=1602820644095"
        "")  # 主页面

    string = str(soup)
    area_t = re.findall(re.compile(r"[\[](.*?)[\]]", re.S), string)
    area_date = area_t[0].replace('"', '').split(',')
    area_db = area_t[1].replace("{\"yAxis\":[", "").replace('"', '').split(',')
    area_hb = area_t[2].replace('"', '').split(',')
    area_xb = area_t[3].replace('"', '').split(',')
    area_hz = area_t[4].replace('"', '').split(',')
    area_hd = area_t[5].replace('"', '').split(',')
    area_xn = area_t[6].replace('"', '').split(',')
    #
    # print(area_date)
    # print(area_db)
    # print(area_hb)
    # print(area_xb)
    # print(area_hz)
    # print(area_hd)
    # print(area_xn)
    #
    # print(len(area_date))
    # print(len(area_db))
    # print(len(area_hb))
    # print(len(area_xb))
    # print(len(area_hz))
    # print(len(area_hd))
    # print(len(area_xn))
    with open('data/焦炭库存分地区走势.csv', "w", newline='', encoding='utf-8-sig') as f:
        field_names = ["日期", "东北地区", "华北地区", "西北地区", "华中地区", "华东地区", "西南地区"]
        f_csv = csv.DictWriter(f, fieldnames=field_names)
        f_csv.writeheader()
        for i in range(0, len(area_date)):
            f_csv.writerow(
                {
                    "日期": area_date[i],
                    "东北地区": area_db[i],
                    "华北地区": area_hb[i],
                    "西北地区": area_xb[i],
                    "华中地区": area_hz[i],
                    "华东地区": area_hd[i],
                    "西南地区": area_xn[i]
                }
            )


#  焦炭库存分规模走势
def coal_capacity():
    soup = url_data("https://api.mysteel.com/tpl/zhanting_data.html?indexCodes=CO_0001264524,CO_0001264525,"
                    "CO_0001264526&startTime=2019-10-16&callback=jQuery18306527873777966918_1602826049855&_"
                    "=1602826080151")

    string = str(soup)
    capacity_t = re.findall(re.compile(r"[\[](.*?)[\]]", re.S), string)
    capacity_date = capacity_t[0].replace('"', '').split(',')
    capacity1 = capacity_t[1].replace("{\"yAxis\":[", "").replace('"', '').split(',')
    capacity2 = capacity_t[2].replace('"', '').split(',')
    capacity3 = capacity_t[3].replace('"', '').split(',')

    # print(capacity_date)
    # print(capacity1)
    # print(capacity2)
    # print(capacity3)
    # print(len(capacity_date))
    # print(len(capacity1))
    # print(len(capacity2))
    # print(len(capacity3))
    with open('data/焦炭库存分规模走势.csv', "w", newline='', encoding='utf-8-sig') as f:
        field_names = ["日期", "产能<100", "产能100-200", "产能≥200"]
        f_csv = csv.DictWriter(f, fieldnames=field_names)
        f_csv.writeheader()
        for i in range(0, len(capacity_date)):
            f_csv.writerow(
                {
                    "日期": capacity_date[i],
                    "产能<100": capacity1[i],
                    "产能100-200": capacity2[i],
                    "产能≥200": capacity3[i]
                }
            )


#  煤焦各品种库存走势图
def coal_trend():
    soup = url_data("https://api.mysteel.com/tpl/zhanting_data.html?indexCodes=CO_0003918032&startTime=2019-10-16"
                    "&callback=jQuery18306527873777966918_1602826049859&_=1602826080146")

    string = str(soup)
    trend_t = re.findall(re.compile(r"[\[](.*?)[\]]", re.S), string)
    trend_date = trend_t[0].replace('"', '').split(',')
    trend1 = trend_t[1].replace("{\"yAxis\":[", "").replace('"', '').split(',')

    with open('data/煤焦各品种库存走势图.csv', "w", newline='', encoding='utf-8-sig') as f:
        field_names = ["日期", "数量"]
        f_csv = csv.DictWriter(f, fieldnames=field_names)
        f_csv.writeheader()
        for i in range(0, len(trend_date)):
            f_csv.writerow(
                {
                    "日期": trend_date[i],
                    "数量": trend1[i]
                }
            )


if __name__ == '__main__':
    coal_area()  # 焦炭库存分地区走势
    coal_capacity()  # 焦炭库存分规模走势
    coal_trend()  # 煤焦各品种库存走势图
