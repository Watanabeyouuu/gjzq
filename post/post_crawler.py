"""
@author: Francis | 韩 心 海
@contact: xinhai_han@icloud.com
@file: post_crawler.py
@date: 2020/11/5 10:29 上午

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
import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/85.0.4183.83 Safari/537.36 "
}


def url_data(url):
    res = requests.get(url, headers=headers)
    print(res.encoding)
    d = res.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(res.text)[0])
    soup = BeautifulSoup(d, "html.parser")
    return soup


soup = url_data('http://www.spb.gov.cn/xw/dtxx_15079/202010/t20201016_3241093.html')

data = soup.find_all('tr')
for i in data:
    print(i.get_text())
# print(data.get_text())

# print(data[0].get_text())

# for data in data:
#     print(data)
