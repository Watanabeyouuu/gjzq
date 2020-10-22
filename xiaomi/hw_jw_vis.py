"""
@author: Francis | 韩 心 海
@contact: xinhai_han@icloud.com
@file: mi_jw_vis.py
@date: 2020/10/22 1:38 下午

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

from pyecharts import Geo, Map

province_c = []
areas = []
values = []


# 数据准备
def r_data(file):
    csv_file = open(file)  # 打开csv文件
    csv_reader_lines = csv.reader(csv_file)  # 逐行读取csv文件
    for one_line in csv_reader_lines:
        if one_line == "city_name":
            continue
        # all_url_lst.append(one_line)  # 将读取的csv分行数据按行存入列表‘date’中
        province_c.append(one_line[-4])


def vis_map():
    c = collections.Counter(province_c)  # 从list创建
    print(c)
    for i in c.keys():
        areas.append(i.replace("省", "").replace("自治区", "").replace("壮族", "").replace("回族", "").replace("维吾尔", ""))
        values.append(c[i])

    #     print(i)
    #     print(c[i])
    print(areas)
    print(values)

    # areas = ['辽宁']
    # values = [183]
    try:
        test_geo = Geo("华为零售店全国分布图", "2020年", title_color="#fff", title_pos="center", width=1000, height=500)
        test_geo.use_theme('dark')
    except Exception as e:
        pass
    test_geo.add("", areas[1:], values[1:], visual_range=[0, 950], maptype='china', is_visualmap=True, is_label_show=False, visual_type="size",
                 border_color='#fff')
    test_geo.render(path="data/华为.html")


if __name__ == '__main__':
    r_data("data/store_list.csv")
    vis_map()
