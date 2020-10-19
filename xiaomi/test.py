"""
@author: Francis | 韩 心 海
@contact: xinhai_han@icloud.com
@file: test.py
@date: 2020/10/19 11:35 上午

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


def save(content):
    f = open('data/test.txt', 'a')
    f.write(content + "\n")
    f.close()


mijia_dct = ""
dict_lst = []
with open("data/xiaomizhijia.txt", "r") as f:  # 打开文件
    data = f.read()  # 读取文件
    # print(data)

# print(data)
mijia = re.findall(re.compile(r"[\[](.*?)[\]]", re.S), data)
# mijia = json.dumps(mijia[0])
# mijia = json.loads(mijia)
print(len(mijia))
for details in mijia:
    mijia_lst = re.findall(re.compile(r"[{](.*?)[}]", re.S), details)
    # print(mijia_lst)
    for detail in mijia_lst:
        # print(detail)
        aim_data = detail.encode('utf-8').decode(encoding='unicode-escape')
        # print(aim_data)
        mijia_dct = "{" + aim_data + "}"
        dict = json.loads(mijia_dct)
        # print(dict["name"])
        # save(mijia_dct)
        dict_lst.append(
            {
                "name": dict["name"],
                "reserve": dict["reserve"],
                "tel": dict["tel"],
                "address": dict["address"],
                "pinyin": dict["pinyin"],
                "province_name": dict["province_name"],
                "city_name": dict["city_name"]
            }
        )


with open('data/test.csv', "w", newline='', encoding='utf-8-sig') as f:
    field_names = ['name', 'reserve', 'tel', 'address', 'pinyin', 'province_name', 'city_name']
    f_csv = csv.DictWriter(f, fieldnames=field_names)
    f_csv.writeheader()
    for i in dict_lst:
        f_csv.writerow(
            {
                "name": i["name"],
                "reserve": i["reserve"],
                "tel": i["tel"],
                "address": i["address"],
                "pinyin": i["pinyin"],
                "province_name": i["province_name"],
                "city_name": i["city_name"]
            }
        )

print(dict_lst)

