"""
@author: Francis | 韩 心 海
@contact: xinhai_han@icloud.com
@file: zgc_detail_crawler.py
@date: 2020/9/16 2:42 下午

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
import datetime
import re
import threading
import time

import requests
from bs4 import BeautifulSoup

threads = []

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

dict_lst = []
all_url_lst = []  # 创建列表准备接收csv各行数据


def r_data(file):
    csv_file = open(file)  # 打开csv文件
    csv_reader_lines = csv.reader(csv_file)  # 逐行读取csv文件
    for one_line in csv_reader_lines:
        all_url_lst.append(one_line)  # 将读取的csv分行数据按行存入列表‘date’中


def url_data(url):
    res = requests.get(url, cookies=cookies, headers=headers)
    d = res.text
    soup = BeautifulSoup(d, "html.parser")
    return soup


#
# # <a class=​"param-baike-enent" id=​"newPmName_9" href=​"/​bk/​57.html#ram-rom" data-text>​RAM容量​</a>​
def spy(urls):
    mobile_name = ""
    brand = ""
    soup = url_data(urls[0])
    print(urls[0])
    index_zol = re.findall(".*/(.*)/param.shtml.*", urls[0])  # 正则 匹配index_zol列
    try:
        brand = soup.select("#_j_breadcrumb")[0].get_text()
        brand = brand
    except Exception as e:
        brand = ""
    try:
        mobile_name = soup.select("body > div.product-model.page-title.clearfix > h1")[0].get_text()
    except Exception as e:
        mobile_name = ""
    data1 = soup.find_all('td', class_='hover-edit-param')
    data2 = soup.find_all('th')
    # print(data1, data2)
    # 变量置空
    date = ""
    releaseY = ""
    releaseM = ""
    cpu = ""
    CPU_brand = ""
    price = ""
    OLED = ""
    WG = ""
    dpi = ""
    ppi = ""
    IP = ""
    full_screen = ""
    screen_size = ""
    back_cam_lst = ""
    front_cam_lst = ""
    ram = ""
    rom = ""
    size = ""
    wireless_charge = ""
    quick_charge = ""
    battery_vol = ""
    finger_print_type = ""
    screen_per = ""
    front_cam_num = ""
    front_cam_1 = ""
    front_cam_2 = ""
    front_cam_3 = ""
    front_cam_4 = ""
    front_cam_5 = ""
    back_cam_num = ""
    back_cam_1 = ""
    back_cam_2 = ""
    back_cam_3 = ""
    back_cam_4 = ""
    back_cam_5 = ""
    device_length = ""
    device_width = ""
    device_thickness = ""
    #  开关
    date_flag = 1
    cpu_flag = 1
    price_flag = 1
    OLED_flag = 1
    ppi_flag = 1
    IP_flag = 1
    full_screen_flag = 1
    screen_size_flag = 1
    back_cam_lst_flag = 1
    front_cam_lst_flag = 1
    ram_flag = 1
    rom_flag = 1
    WG_flag = 1
    dpi_flag = 1
    size_flag = 1
    wireless_charge_flag = 1
    quick_charge_flag = 1
    battery_vol_flag = 1
    finger_print_type_flag = 1
    screen_per_flag = 1
    for i in range(0, len(data1)):  # data1是右边栏
        left_l = data2[i].get_text().replace("纠错", "")
        right_l = data1[i].get_text().replace("纠错", "")
        # print(data2[i].get_text(), data1[i].get_text())
        if ("上市日期" in left_l) and (date_flag == 1):
            date = right_l
            date_flag = 0

        if ("CPU型号" in left_l) and (cpu_flag == 1):
            cpu = right_l
            cpu_flag = 0

        if ("报价" in left_l) and (price_flag == 1):
            rl = right_l
            price = rl.split("¥")
            try:
                price = price[1]
            except Exception as e:
                price = ""
            price_flag = 0

        if ("OLED" in right_l) and (OLED_flag == 1):
            OLED = "1"
            OLED_flag = 0

        if ("像素密度" in left_l) and (ppi_flag == 1):
            ppi = right_l
            ppi_flag = 0

        if ("IP" in right_l) and (IP_flag == 1):
            IP = right_l
            IP_flag = 0

        if ("全面屏" in right_l) and (full_screen_flag == 1):
            full_screen = "1"
            full_screen_flag = 0

        if ("主屏尺寸" in left_l) and (screen_size_flag == 1):
            screen_size = right_l
            screen_size_flag = 0

        if ("后置摄像头" in left_l) and (back_cam_lst_flag == 1):
            back_cam_lst = right_l
            back_cam_lst_flag = 0

        if ("前置摄像头" in left_l) and (front_cam_lst_flag == 1):
            front_cam_lst = right_l
            front_cam_lst_flag = 0

        if ("RAM容量" in left_l) and (ram_flag == 1):
            ram = re.findall(r'\d+', right_l)[0]
            ram_flag = 0

        if ("ROM容量" in left_l) and (rom_flag == 1):
            rom = re.findall(r'\d+', right_l)[0]
            rom_flag = 0

        if ("5G" in right_l) and (WG_flag == 1):
            WG = "1"
            WG_flag = 0

        if ("主屏分辨率" in left_l) and (dpi_flag == 1):
            dpi = right_l
            dpi_flag = 0

        if ("手机尺寸" in left_l) and (size_flag == 1):
            size = right_l
            size_flag = 0

        if ("电池充电" in left_l) and (wireless_charge_flag == 1):
            if "无线" in right_l:
                wireless_charge = "1"
            wireless_charge_flag = 0

        if ("电池充电" in left_l) and (quick_charge_flag == 1):
            if ("快" in right_l) or ("闪" in right_l):
                quick_charge = "1"
            quick_charge_flag = 0

        if ("电池容量" in left_l) and (battery_vol_flag == 1):
            battery_vol = right_l
            battery_vol = (re.findall(r'\d+', battery_vol))[0]
            battery_vol_flag = 0

        if ("解锁方式" in left_l) and (finger_print_type_flag == 1):
            if "前置" in right_l:
                finger_print_type = finger_print_type + "前置指纹 "
            if "后置" in right_l:
                finger_print_type = finger_print_type + "后置指纹 "
            if "屏幕" in right_l:
                finger_print_type = finger_print_type + "屏幕指纹 "
            if "侧面" in right_l:
                finger_print_type = finger_print_type + "侧面指纹 "
            finger_print_type_flag = 0

        if ("屏幕占比" in left_l) and (screen_per_flag == 1):
            screen_per = right_l
            screen_per_flag = 0

    # apart_data(front_cam_lst, back_cam_lst, size, date, cpu)
    # 执行拆分
    try:
        screen_per = screen_per.split("%")[0]
    except Exception as e:
        pass

    try:
        screen_size = screen_size.split("英寸")[0]
    except Exception as e:
        pass

    try:
        dpi = dpi.split("像素")[0]
    except Exception as e:
        pass

    try:
        pattern = re.compile(r'(?<=IP)\d+')
        IP = pattern.findall(IP)
        if len(IP) > 0:
            IP = "IP" + IP[0]
        else:
            IP = ""
    except Exception as e:
        pass

    all_front = re.findall(r'\d+', front_cam_lst)  # 拆分后置摄像头
    front_cam_num = len(all_front)
    try:
        front_cam_1 = all_front[0]
        front_cam_2 = all_front[1]
        front_cam_3 = all_front[2]
        front_cam_4 = all_front[3]
        front_cam_5 = all_front[4]
    except Exception as e:
        pass

    all_back = re.findall(r'\d+', back_cam_lst)  # 拆分后置摄像头
    back_cam_num = len(all_back)
    try:
        back_cam_1 = all_back[0]
        back_cam_2 = all_back[1]
        back_cam_3 = all_back[2]
        back_cam_4 = all_back[3]
        back_cam_5 = all_back[4]
    except Exception as e:
        pass

    size_l = re.findall(r'-?\d+\.?\d*e?-?\d*?', size)  # 拆分屏幕尺寸
    try:
        device_length = size_l[0]
        device_width = size_l[1]
        device_thickness = size_l[2]
    except Exception as e:
        pass

    date_l = re.findall(r'\d+', date)  # 拆分发布日期
    try:
        releaseY = date_l[0]
        releaseM = date_l[1]
    except Exception as e:
        pass
    pass

    cpu_l = cpu.split(" ")
    CPU_brand = cpu_l[0]

    dict_lst.append(
        {
            "型号": mobile_name,
            "brand": brand,
            "index_zol": index_zol[0],
            "price": price,
            "OLED": OLED,
            "IP": IP,
            "full_screen": full_screen,
            "screen_size": screen_size,
            "back_cam_lst": back_cam_lst,
            "back_cam_num": back_cam_num,
            "back_cam_1": back_cam_1,
            "back_cam_2": back_cam_2,
            "back_cam_3": back_cam_3,
            "back_cam_4": back_cam_4,
            "back_cam_5": back_cam_5,
            "front_cam_lst": front_cam_lst,
            "front_cam_num": front_cam_num,
            "front_cam_1": front_cam_1,
            "front_cam_2": front_cam_2,
            "front_cam_3": front_cam_3,
            "front_cam_4": front_cam_4,
            "front_cam_5": front_cam_5,
            "CPU_brand": CPU_brand,
            "CPU": cpu,
            "ram": ram,
            "rom": rom,
            "5G": WG,
            "dpi": dpi,
            "ppi": ppi,
            "size": size,
            "device_length": device_length,
            "device_width": device_width,
            "device_thickness": device_thickness,
            "fingerprint_type": finger_print_type,
            "release_date": date,
            "releaseY": releaseY,
            "releaseM": releaseM,
            "wireless_charge": wireless_charge,
            "battery_vol": battery_vol,
            "screen_per": screen_per,
            "quick_charge": quick_charge

        }
    )


# print(dict_lst)


def save(file):
    with open(file, "w", newline='', encoding='utf-8-sig') as f:
        field_names = ["型号", "brand", "index_zol", "price", "OLED", "IP", "full_screen", "screen_per", "screen_size",
                       "back_cam_lst",
                       "back_cam_num", "back_cam_1", "back_cam_2", "back_cam_3", "back_cam_4", "back_cam_5",
                       "front_cam_lst",
                       "front_cam_num", "front_cam_1", "front_cam_2", "front_cam_3", "front_cam_4", "front_cam_5",
                       "CPU_brand", "CPU", "ram", "rom", "5G", "dpi", "ppi", "size", "device_length", "device_width",
                       "device_thickness",
                       "fingerprint_type", "release_date", "releaseY", "releaseM", "wireless_charge", "quick_charge",
                       "battery_vol"]
        f_csv = csv.DictWriter(f, fieldnames=field_names)
        f_csv.writeheader()
        for i in dict_lst:
            f_csv.writerow(
                {
                    "型号": i['型号'],
                    "brand": i['brand'],
                    "index_zol": i['index_zol'],
                    "price": i['price'],
                    "OLED": i['OLED'],
                    "IP": i['IP'],
                    "full_screen": i['full_screen'],
                    "screen_per": i['screen_per'],
                    "screen_size": i['screen_size'],
                    "back_cam_lst": i['back_cam_lst'],
                    "back_cam_num": i['back_cam_num'],
                    "back_cam_1": i['back_cam_1'],
                    "back_cam_2": i['back_cam_2'],
                    "back_cam_3": i['back_cam_3'],
                    "back_cam_4": i['back_cam_4'],
                    "back_cam_5": i['back_cam_5'],
                    "front_cam_lst": i['front_cam_lst'],
                    "front_cam_num": i['front_cam_num'],
                    "front_cam_1": i['front_cam_1'],
                    "front_cam_2": i['front_cam_2'],
                    "front_cam_3": i['front_cam_3'],
                    "front_cam_4": i['front_cam_4'],
                    "front_cam_5": i['front_cam_5'],
                    "CPU_brand": i['CPU_brand'],
                    "CPU": i['CPU'],
                    "ram": i['ram'],
                    "rom": i['rom'],
                    "5G": i['5G'],
                    "dpi": i['dpi'],
                    "ppi": i['ppi'],
                    "size": i['size'],
                    "device_length": i['device_length'],
                    "device_width": i['device_width'],
                    "device_thickness": i['device_thickness'],
                    "fingerprint_type": i['fingerprint_type'],
                    "release_date": i['release_date'],
                    "releaseY": i['releaseY'],
                    "releaseM": i['releaseM'],
                    "wireless_charge": i['wireless_charge'],
                    "quick_charge": i['quick_charge'],
                    "battery_vol": i['battery_vol']
                }
            )


def main():
    for urls in all_url_lst[:]:
        t = threading.Thread(target=spy, args=(urls,))
        # t.daemon = True
        # t.join()
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__ == '__main__':
    starttime = datetime.datetime.now()
    print("开始时间:", starttime)

    # 对应文件里的数据
    ori_file = "data/file_url.csv"  # 数据源
    aim_file = 'data/爬虫_中关村在线_匹配数据.csv'  # 目标文件

    # ori_file = "data/all_url.csv"  # 数据源
    # aim_file = 'data/爬虫_中关村在线_所有数据.csv'  # 目标文件

    # # 新增数据
    # ori_file = "data/add_url.csv"  # 数据源
    # aim_file = 'data/爬虫_中关村在线_新增数据.csv'  # 目标文件

    r_data(ori_file)
    main()
    save(aim_file)

    endtime = datetime.datetime.now()
    print("Starttime:", starttime)
    print("Endtime:", endtime)
    print("This Program runs ", (endtime - starttime).seconds, " seconds！")
