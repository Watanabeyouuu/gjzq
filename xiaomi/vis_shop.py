"""
@author: Francis | 韩 心 海
@contact: xinhai_han@icloud.com
@file: vis_shop.py
@date: 2020/10/20 7:05 下午

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
import collections
import csv

from pyecharts import Map

province_c = []


def r_data(file):
    csv_file = open(file)  # 打开csv文件
    csv_reader_lines = csv.reader(csv_file)  # 逐行读取csv文件
    for one_line in csv_reader_lines:
        # all_url_lst.append(one_line)  # 将读取的csv分行数据按行存入列表‘date’中
        province_c.append(one_line[5])


def vis_map():
    c = collections.Counter(province_c)  # 从list创建
    print(c)

    province_distribution = c
    provice = list(province_distribution.keys())
    values = list(province_distribution.values())
    map = Map("小米之家全国分布图", '2020年', width=1200, height=600)
    map.add("", provice, values, visual_range=[0, 50], maptype='china', is_visualmap=True,
            visual_text_color='#000')
    map.render(path="中国地图.html")


if __name__ == '__main__':
    r_data("data/小米之家.csv")
    vis_map()
