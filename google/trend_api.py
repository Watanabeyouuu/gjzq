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
country_lst = {
    "east timor": "TP",
    "samoa": "WS",
    "japan": "JP",
    "french southern territories": "TF",
    "tokelau": "TK",
    "cayman islands": "KY",
    "azerbaijan": "AZ",
    "north korea": "KP",
    "djibouti": "DJ",
    "french guiana": "GF",
    "malta": "MT",
    "guinea-bissau": "GW",
    "hungary": "HU",
    "taiwan": "TW",
    "cyprus": "CY",
    "haiti": "HT",
    "barbados": "BB",
    "eastern asia": "UN030",
    "bhutan": "BT",
    "yugoslavia": "YU",
    "lithuania": "LT",
    "congo - kinshasa": "CD",
    "micronesia": "UN057",
    "andorra": "AD",
    "union of soviet socialist republics": "SU",
    "rwanda": "RW",
    "aruba": "AW",
    "liberia": "LR",
    "argentina": "AR",
    "norway": "NO",
    "sierra leone": "SL",
    "somalia": "SO",
    "ghana": "GH",
    "falkland islands": "FK",
    "belarus": "BY",
    "saint helena": "SH",
    "cuba": "CU",
    "middle africa": "UN017",
    "central asia": "UN143",
    "french polynesia": "PF",
    "southern europe": "UN039",
    "guatemala": "GT",
    "isle of man": "IM",
    "belgium": "BE",
    "world": "UN001",
    "congo - brazzaville": "CG",
    "southern asia": "UN034",
    "kazakhstan": "KZ",
    "burkina faso": "BF",
    "aland islands": "AX",
    "kyrgyzstan": "KG",
    "netherlands": "NL",
    "portugal": "PT",
    "central america": "UN013",
    "denmark": "DK",
    "philippines": "PH",
    "montserrat": "MS",
    "senegal": "SN",
    "moldova": "MD",
    "latvia": "LV",
    "croatia": "HR",
    "bosnia and herzegovina": "BA",
    "chad": "TD",
    "switzerland": "CH",
    "western europe": "UN155",
    "mali": "ML",
    "bulgaria": "BG",
    "jamaica": "JM",
    "albania": "AL",
    "angola": "AO",
    "colombia": "CO",
    "serbia and montenegro": "CS",
    "northern america": "UN021",
    "palestinian territory": "PS",
    "lebanon": "LB",
    "malaysia": "MY",
    "christmas island": "CX",
    "mozambique": "MZ",
    "greece": "GR",
    "zaire": "ZR",
    "nicaragua": "NI",
    "new zealand": "NZ",
    "southern africa": "UN018",
    "canada": "CA",
    "afghanistan": "AF",
    "qatar": "QA",
    "oceania": "UN009",
    "palau": "PW",
    "turkmenistan": "TM",
    "equatorial guinea": "GQ",
    "pitcairn": "PN",
    "guinea": "GN",
    "panama": "PA",
    "nepal": "NP",
    "central african republic": "CF",
    "luxembourg": "LU",
    "solomon islands": "SB",
    "south america": "UN005",
    "swaziland": "SZ",
    "cook islands": "CK",
    "tuvalu": "TV",
    "netherlands antilles": "AN",
    "namibia": "NA",
    "nauru": "NR",
    "venezuela": "VE",
    "australia and new zealand": "UN053",
    "outlying oceania": "QO",
    "europe": "UN150",
    "brunei": "BN",
    "iran": "IR",
    "british indian ocean territory": "IO",
    "united arab emirates": "AE",
    "south georgia and the south sandwich islands": "GS",
    "saint kitts and nevis": "KN",
    "sri lanka": "LK",
    "paraguay": "PY",
    "china": "CN",
    "armenia": "AM",
    "western asia": "UN145",
    "kiribati": "KI",
    "belize": "BZ",
    "tunisia": "TN",
    "ukraine": "UA",
    "melanesia": "UN054",
    "yemen": "YE",
    "northern mariana islands": "MP",
    "libya": "LY",
    "trinidad and tobago": "TT",
    "mayotte": "YT",
    "gambia": "GM",
    "finland": "FI",
    "macedonia": "MK",
    "americas": "UN019",
    "mauritius": "MU",
    "antigua and barbuda": "AG",
    "niue": "NU",
    "syria": "SY",
    "dominican republic": "DO",
    "people's democratic republic of yemen": "YD",
    "jersey": "JE",
    "burma": "BU",
    "pakistan": "PK",
    "romania": "RO",
    "seychelles": "SC",
    "metropolitan france": "FX",
    "czech republic": "CZ",
    "myanmar": "MM",
    "el salvador": "SV",
    "egypt": "EG",
    "neutral zone": "NT",
    "guam": "GU",
    "africa": "UN002",
    "papua new guinea": "PG",
    "wallis and futuna": "WF",
    "united states": "US",
    "austria": "AT",
    "greenland": "GL",
    "mongolia": "MN",
    "ivory coast": "CI",
    "thailand": "TH",
    "honduras": "HN",
    "niger": "NE",
    "fiji": "FJ",
    "comoros": "KM",
    "turkey": "TR",
    "united kingdom": "GB",
    "madagascar": "MG",
    "iraq": "IQ",
    "bangladesh": "BD",
    "mauritania": "MR",
    "eastern europe": "UN151",
    "bolivia": "BO",
    "uruguay": "UY",
    "france": "FR",
    "bahamas": "BS",
    "vatican": "VA",
    "slovakia": "SK",
    "gibraltar": "GI",
    "ireland": "IE",
    "laos": "LA",
    "british virgin islands": "VG",
    "south korea": "KR",
    "anguilla": "AI",
    "malawi": "MW",
    "ecuador": "EC",
    "israel": "IL",
    "peru": "PE",
    "algeria": "DZ",
    "serbia": "RS",
    "tanzania": "TZ",
    "puerto rico": "PR",
    "montenegro": "ME",
    "tajikistan": "TJ",
    "svalbard and jan mayen": "SJ",
    "togo": "TG",
    "jordan": "JO",
    "chile": "CL",
    "martinique": "MQ",
    "oman": "OM",
    "turks and caicos islands": "TC",
    "nigeria": "NG",
    "spain": "ES",
    "sao tome and principe": "ST",
    "georgia": "GE",
    "eastern africa": "UN014",
    "bouvet island": "BV",
    "asia": "UN142",
    "northern europe": "UN154",
    "american samoa": "AS",
    "polynesia": "UN061",
    "morocco": "MA",
    "sweden": "SE",
    "heard island and mcdonald islands": "HM",
    "gabon": "GA",
    "guyana": "GY",
    "western africa": "UN011",
    "grenada": "GD",
    "guadeloupe": "GP",
    "hong kong": "HK",
    "russia": "RU",
    "u.s. virgin islands": "VI",
    "cocos islands": "CC",
    "bahrain": "BH",
    "zimbabwe": "ZW",
    "estonia": "EE",
    "mexico": "MX",
    "reunion": "RE",
    "india": "IN",
    "new caledonia": "NC",
    "lesotho": "LS",
    "antarctica": "AQ",
    "australia": "AU",
    "saint vincent and the grenadines": "VC",
    "saint pierre and miquelon": "PM",
    "uganda": "UG",
    "burundi": "BI",
    "kenya": "KE",
    "macao": "MO",
    "botswana": "BW",
    "italy": "IT",
    "western sahara": "EH",
    "south africa": "ZA",
    "east germany": "DD",
    "cambodia": "KH",
    "ethiopia": "ET",
    "bermuda": "BM",
    "vanuatu": "VU",
    "marshall islands": "MH",
    "cameroon": "CM",
    "zambia": "ZM",
    "benin": "BJ",
    "brazil": "BR",
    "saudi arabia": "SA",
    "singapore": "SG",
    "faroe islands": "FO",
    "iceland": "IS",
    "saint lucia": "LC",
    "monaco": "MC",
    "costa rica": "CR",
    "united states minor outlying islands": "UM",
    "slovenia": "SI",
    "germany": "DE",
    "caribbean": "UN029",
    "san marino": "SM",
    "dominica": "DM",
    "suriname": "SR",
    "eritrea": "ER",
    "tonga": "TO",
    "maldives": "MV",
    "south-eastern asia": "UN035",
    "uzbekistan": "UZ",
    "northern africa": "UN015",
    "norfolk island": "NF",
    "poland": "PL",
    "indonesia": "ID",
    "cape verde": "CV",
    "sudan": "SD",
    "liechtenstein": "LI",
    "vietnam": "VN",
    "guernsey": "GG",
    "kuwait": "KW"
}


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
    # for c in country_lst:
    #     country = country_lst[c]  # 国家
    #     print(country)
    #     key = "iphone 12"  # 搜索关键字
    #     google(key, country)
    #     save('data/' + key + '_' + c + '谷歌趋势.csv')
    for i in ['iphone 12', 'iphone 12', 'mate40', 'mate 40', '华为mate40', '华为mate 40']:
        dict_lst= []
        country = ""  # 国家
        key = i  # 搜索关键字
        google(key, country)
        save('data/' + key + '_' + "全球_" + '谷歌趋势.csv')
