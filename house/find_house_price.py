import csv
import re
import time
import urllib.request
import selenium.webdriver
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote, unquote

all_lst = []
province_url_lst = []
year_lst = []
province_lst = []
city_name_lst = []
price_lst = []

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/85.0.4183.83 Safari/537.36 "
}

year = ""
province = ""
city_name = ""
price = ""


# cookies = {'cookie': }

def url_data(url):
    res = requests.get(url, headers=headers)
    d = res.text
    return d


for y in range(2011, 2021):
    year = y
    time.sleep(1)
    data = url_data("https://www.anjuke.com/fangjia/quanguo" + str(y) + "/")  # 主页面
    soup = BeautifulSoup(data, "html.parser")
    for i in range(2, 30):  # 爬取城市页面 range(2, 30)
        # for i in range(17, 18):  # 爬取城市页面 range(2, 30)
        #     if (i == 9):
        if (i == 9) or (i == 17):  # 第9是海南（数据有问题） 第17是吉林，需要单独爬
            continue
        time.sleep(0.001)
        try:

            province_data = soup.select("body > div.main-content > div.div-border.items-list > div > span.elem-l > "
                                        "a:nth-child(" + str(i) + ")")
            print(province_data)
            province_url = province_data[0]['href']
            province = province_data[0].get_text()
            province_url_lst.append(province_url)
            # print(province_url)
        except Exception as e:
            print("ERROR!!!!")
            continue

        city_data = url_data(province_url)
        city_soup = BeautifulSoup(city_data, "html.parser")
        for j in range(1, 60):
            time.sleep(0.000001)
            try:
                city_name = city_soup.select(
                    "body > div.main-content > div.avger.clearfix > div.fjlist-wrap.clearfix > div:nth-child(1) > ul "
                    "> li:nth-child(" + str(j) + ") > a > b")
                city_name = city_name[0].get_text()
                # yxcs = city_name[:-2][5:]
                price = city_soup.select(
                    "body > div.main-content > div.avger.clearfix > div.fjlist-wrap.clearfix > div:nth-child(1) > ul "
                    "> li:nth-child(" + str(j) + ") > a > span")
                price = price[0].get_text()
                # print(city_name)
                # if province == "一线城市":
                #     province = yxcs
                all_lst.append(
                    {
                        "年份": y,
                        "省份": province,
                        "城市": city_name[:-2][5:],
                        "房价": price[:-3]
                    }
                )
            except Exception as e:
                break

print(all_lst)
file_path = "data/house_price.csv"
with open(file_path, "w", encoding='utf-8-sig') as f:
    fieldnames = ["年份", "省份", "城市", "房价"]
    f_csv = csv.DictWriter(f, fieldnames=fieldnames)
    f_csv.writeheader()
    for i in range(0, len(all_lst)):
        f_csv.writerow(
            {
                "年份": all_lst[i]['年份'],
                "省份": all_lst[i]['省份'],
                "城市": all_lst[i]['城市'],
                "房价": all_lst[i]['房价']
            }
        )
