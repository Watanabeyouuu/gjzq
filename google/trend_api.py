"""
@author: Francis | 韩 心 海
@contact: xinhai_han@icloud.com
@file: trend_api.py
@date: 2020/10/22 7:06 下午

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
import json

import requests

dict_lst = []


def get_token(keyword, country):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/80.0.3987.163 Safari/537.36',
        'x-client-data': 'CIu2yQEIo7bJAQjEtskBCKmdygEIy67KAQjQr8oBCLywygEIl7XKAQjttcoBCI66ygEYx7fKAQ==',
        'referer': 'https://trends.google.com/trends/explore?date=today%201-m&q=bitcoin,blockchain,eth',
        'cookie': '__utmc=10102256; __utma=10102256.31392724.1583402727.1586332529.1586398363.11; '
                  '__utmz=10102256.1586398363.11.11.utmcsr=shimo.im|utmccn=('
                  'referral)|utmcmd=referral|utmcct=/docs/qxW86VTXr8DK6HJX; __utmt=1; '
                  '__utmb=10102256.9.9.1586398779015; '
                  'ANID=AHWqTUlRutPWkqC3UpC_-5XoYk6zqoDW3RQX5ePFhLykky73kQ0BpL32ATvqV3O0; CONSENT=WP.284bc1; '
                  'NID=202=xLozp9-VAAGa2d3d9'
                  '-cqyqmRjW9nu1zmK0j50IM4pdzJ6wpWTO_Z49JN8W0s1OJ8bySeirh7pSMew1WdqRF890iJLX4HQwwvVkRZ7zwsBDxzeHIx8MOWf27jF0mVCxktZX6OmMmSA0txa0zyJ_AJ3i9gmtEdLeopK5BO3X0LWRA; 1P_JAR=2020-4-9-2 '
    }
    url = 'https://trends.google.com/trends/api/explore?hl=zh-CN&tz=-480&req={{"comparisonItem":[{{"keyword":"{}",' \
          '"geo":"{}","time":"today 3-m"}}],"category":0,"property":""}}&tz=-480'.format(keyword, country)
    # print(url)
    r = requests.get(url, headers=headers)
    # print(r)
    data = json.loads(r.text[5:])
    # print(data['widgets'][0])
    req = data['widgets'][0]['request']
    token = data['widgets'][0]['token']
    result = {'req': req, 'token': token}
    print("GET:", token)
    return result


def google(keyword, country):
    """谷歌指数"""
    info = get_token(keyword, country)
    req = info['req']
    # print(type(req))
    token = info['token']
    print("google:", token)

    url = 'https://trends.google.com/trends/api/widgetdata/multiline?hl=zh-CN&tz=-480&req={}&token={}&tz=-480'.format(
        req, token)
    # print(url.replace("\"", "'"))
    r = requests.get(url)
    if r.status_code == 200:
        data = json.loads(r.text.encode().decode('unicode_escape')[6:])['default']['timelineData']
        # print(data)
        for data_e in data:
            timestamp = int(data_e['time']) * 1000
            vis_date = data_e['formattedTime']
            value = data_e['value'][0]
            keyword = keyword
            print(vis_date, timestamp, value, keyword)

            dict_lst.append(
                {
                    "关键字": keyword,
                    "国家": country,
                    "日期": vis_date,
                    "时间戳": timestamp,
                    "值": value
                }
            )
    print(dict_lst)

def save(file):
    with open(file, "w", newline='', encoding='utf-8-sig') as f:
        field_names = ["关键字", "国家", "日期", "时间戳", "值"]
        f_csv = csv.DictWriter(f, fieldnames=field_names)
        f_csv.writeheader()
        for i in dict_lst:
            f_csv.writerow(
                {
                    "关键字": i['关键字'],
                    "国家": i['国家'],
                    "日期": i['日期'],
                    "时间戳": i['时间戳'],
                    "值": i['值']
                }
            )


if __name__ == '__main__':
    country = "US"  # 国家
    key = "iphone 12"  # 搜索关键字
    google(key, country)

    save('data/' + key + '谷歌趋势.csv')
