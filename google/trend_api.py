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
import json

import requests


def get_token(keyword):
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
                  'NID=202=xLozp9-VAAGa2d3d9-cqyqmRjW9nu1zmK0j50IM4pdzJ6wpWTO_Z49JN8W0s1OJ8bySeirh7pSMew1WdqRF890iJLX4HQwwvVkRZ7zwsBDxzeHIx8MOWf27jF0mVCxktZX6OmMmSA0txa0zyJ_AJ3i9gmtEdLeopK5BO3X0LWRA; 1P_JAR=2020-4-9-2 '
    }
    url = 'https://trends.google.com/trends/api/explore?hl=zh-CN&tz=-480&req={{"comparisonItem":[{{"keyword":"{}",' \
          '"geo":"","time":"now 7-d"}}],"category":0,"property":""}}&tz=-480'.format(keyword)
    r = requests.get(url, headers=headers)
    data = json.loads(r.text[5:])
    req = data['widgets'][0]['request']
    token = data['widgets'][0]['token']
    result = {'req': req, 'token': token}
    return result


def google(keyword):
    """谷歌指数"""
    info = get_token(keyword)
    req = info['req']
    token = info['token']
    # print("REQ:", req)
    # print("TOKEN:", token)
    url = 'https://trends.google.com/trends/api/widgetdata/multiline?hl=zh-CN&tz=-480&req={}&token={}&tz=-480'.format(
        req, token)
    r = requests.get(url)
    if r.status_code == 200:
        data = json.loads(r.text.encode().decode('unicode_escape')[6:])['default']['timelineData']
        print(data)
        for data_e in data:
            timestamp = int(data_e['time']) * 1000
            vis_date = data_e['formattedTime']
            value = data_e['value'][0]
            keyword = keyword
            print(vis_date, timestamp, value, keyword)


google("iphone 12")
