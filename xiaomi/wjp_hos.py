"""
@author: Francis | 韩 心 海
@contact: xinhai_han@icloud.com
@file: wjp_hos.py
@date: 2020/11/11 2:34 下午

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
from pyecharts import Geo, Map

areas = []
values = []
province = []


# 数据准备
def r_data(file):
    province_c = []
    csv_file = open(file)  # 打开csv文件
    csv_reader_lines = csv.reader(csv_file)  # 逐行读取csv文件
    for one_line in csv_reader_lines:
        # print(one_line)
        province_c.append(one_line)
    # print(province_c)

    for i in province_c[1:]:
        province.append(i[0].replace("省", "").replace("自治区", "").replace("壮族", "").replace("回族", "").replace("维吾尔", ""))
        values.append(i[1])
        print(i)

    map = Map("医院数量地区分布图", '2020年', width=1500, height=750)
    map.add("", province, values, visual_range=[0, 10], maptype='china', is_visualmap=True,
            visual_text_color='#000', is_map_symbol_show=False, is_label_show=True)
    map.render(path="data/wjp.html")


if __name__ == '__main__':
    r_data("data/wjp.csv")
