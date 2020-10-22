"""
@author: Francis | 韩 心 海
@contact: xinhai_han@icloud.com
@file: test.py
@date: 2020/10/22 7:10 下午

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

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/85.0.4183.83 Safari/537.36 "
}
cookies = {'cookie': 'ip_ck=4sGF5Pryj7QuNTY0MzA1LjE1OTk1MzU0MTM%3D; '
                     'z_pro_city=s_provice%3Dshanghai%26s_city%3Dshanghai; '
                     'Hm_lvt_ae5edc2bc4fc71370807f6187f0a2dd0=1599535425; visited_subcateId=57; '
                     'visited_subcateProId=57-0; userProvinceId=2; userCityId=0; userCountyId=0; userLocationId=26; '
                     'realLocationId=26; userFidLocationId=26; '
                     'z_day=izol110770%3D3%26izol110792%3D5%26izol110769%3D3%26izol110794%3D2%26ixgo20%3D1%26rdetail'
                     '%3D9; questionnaire_pv=1599523236; '
                     'visited_serachKw=%u5C0F%u7C73%7C%u534E%u4E3A%7C%u590F%u666EAQUOS%20mini%20SH-03H; Adshow=5; '
                     'lv=1599543319; vn=2; Hm_lpvt_ae5edc2bc4fc71370807f6187f0a2dd0=1599543319; listSubcateId=57'}


def url_data(url):
    res = requests.get(url, cookies=cookies, headers=headers)
    d = res.text
    return d

data = url_data('https://www.google.com/?client=safari')
print(data)