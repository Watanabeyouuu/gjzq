import csv
import datetime
import re
from threading import Lock

import requests
from bs4 import BeautifulSoup

# 全局变量

lock = Lock()

index_zol_lst = []
brand_lst = []  # 所有手机型号
brand_url_lst = []  # 型号的url
page_lst = []  # 该品牌下的页数
all_url_lst = []  # 所有手机的detail页面
OLED_lst = []  # OLED列
full_screen_lst = []  # full screen列
phone_name_lst = []  # 手机型号列
cam_num_lst = []  # 摄像头列
front_cam_lst = []  # 前置摄像头列
back_cam_lst = []  # 后置摄像头列
CPU_lst = []  # CPU列
ram_lst = []  # ram列
dpi_lst = []  # dpi列
ppi_lst = []  # ppi列
size_lst = []  # size列
release_date_lst = []  # release date列
battery_vol_lst = []  # battery vol列
rom_lst = []  # rom列
WG_lst = []  # 5G列
price_lst = []  # price列
IP_lst = []  # IP列
unlock_lst = []  # fingerprint type列
back_cam_num_lst = []  # 后摄像头数量
back_cam_1 = []  # 5个后摄像头像素
back_cam_2 = []
back_cam_3 = []
back_cam_4 = []
back_cam_5 = []
front_cam_num_lst = []  # 前摄像头数量
front_cam_1 = []  # 5个前摄像头像素
front_cam_2 = []
front_cam_3 = []
front_cam_4 = []
front_cam_5 = []
device_length = []  # 设备尺寸
device_width = []
device_thickness = []
releaseY = []  # 发布年
releaseM = []  # 发布月
CPU_brand = []  # CPU品牌
wireless_charge_lst = []  # 无线充电列
screen_size_lst = []  # 屏幕尺寸列
mbrand_lst = []  # 手机品牌列
# ------------------------------

csv_file = open('data/file_url.csv')  # 打开csv文件
csv_reader_lines = csv.reader(csv_file)  # 逐行读取csv文件
all_url_lst = []  # 创建列表准备接收csv各行数据
for one_line in csv_reader_lines:
    all_url_lst.append(one_line)  # 将读取的csv分行数据按行存入列表‘date’中
# for d_url in all_url_lst:
#     print(d_url[0])
# print(len(all_url_lst))

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


starttime = datetime.datetime.now()
print("开始时间:", starttime)


# 循环一下获取到的主lst 对detail info进行爬取
def grab_all(d_url):
    # threadpools = ThreadPoolExecutor(max_workers=3)
    try:  # 有时会出现out of range的错误
        # print("------", d_url)
        try:
            data = url_data(d_url)  # 读取detail url的信息
            soup = BeautifulSoup(data, "html.parser")
            print(d_url)
            # print("1")
            phone_name = soup.select("body > div.product-model.page-title.clearfix > h1")  # 手机型号列
            # print(phone_name)
            phone_name_lst.append(phone_name[0].get_text()[:-2])
        except Exception as e:
            phone_name_lst.append("")

        index_zol = re.findall(".*/(.*)/param.shtml.*", d_url)  # 正则 匹配index_zol列
        index_zol_lst.append(index_zol)  # 将index_zol存入其主列

        # CPU列
        # try:
        #     cpu = soup.select("body > div.wrapper.clearfix.mt30 > div.info-list-fr > ul > li:nth-child(1) > div > "
        #                       "span.product-link")
        #     cpu = cpu[0].get_text()
        #     # print(cpu)
        #     CPU_lst.append(cpu)
        # except Exception as e:
        #     try:
        #         cpu = soup.select(
        #             "body > div.wrapper.clearfix.mt30 > div.info-list-fr > ul > li:nth-child(1) > div > a")
        #         cpu = cpu[0].get_text()
        #         CPU_lst.append(cpu)
        #     except Exception as e:
        #         CPU_lst.append("")

        # 后置像素列
        # try:
        #     back_cam = soup.select(
        #         "body > div.wrapper.clearfix.mt30 > div.info-list-fr > ul > li:nth-child(2) > div.box-item-fl > "
        #         "span.product-link")
        #     back_cam = back_cam[0].get_text()
        #     back_cam_lst.append(back_cam)
        # except Exception as e:
        #     try:
        #         back_cam = soup.select(
        #             "body > div.wrapper.clearfix.mt30 > div.info-list-fr > ul > li.info-item.t-xiangsu-hd > "
        #             "div.box-item-fl > span.product-link")
        #         back_cam = back_cam[0].get_text()
        #         # print("back", back_cam, back_cam == null)
        #         back_cam_lst.append(back_cam)
        #     except Exception as e:
        #         # print("back", back_cam, back_cam == null)
        #         back_cam_lst.append("")
        # if back_cam == "":
        #     back_cam_lst.append("")
        # 前置像素列
        # try:
        #     try:
        #         front_cam = soup.select(
        #             "body > div.wrapper.clearfix.mt30 > div.info-list-fr > ul > li:nth-child(3) > div.box-item-fl > "
        #             "span.product-link")
        #         front_cam = front_cam[0].get_text()
        #     except Exception as e:
        #         front_cam = soup.select(
        #             "body > div.wrapper.clearfix.mt30 > div.info-list-fr > ul > li:nth-child(3) > div.box-item-fl > a")
        #         front_cam = front_cam[0].get_text()
        #     # print(front_cam)
        #     if "GB" not in front_cam:
        #         front_cam_lst.append(front_cam)
        #         # print(front_cam)
        #     else:
        #         front_cam_lst.append("")
        # except Exception as e:
        #     try:
        #         front_cam = soup.select(
        #             "body > div.wrapper.clearfix.mt30 > div.info-list-fr > ul > li.info-item.t-xiangsu-putong > "
        #             "div.box-item-fl > a")
        #         front_cam = front_cam[0].get_text()
        #         # print(front_cam)
        #         if "GB" not in front_cam:
        #             front_cam_lst.append(front_cam)
        #             # print(front_cam)
        #         else:
        #             front_cam_lst.append("")
        #     except Exception as e:
        #         front_cam_lst.append("")

        # 内存ram
        # try:
        #     ram = soup.select(
        #         "body > div.wrapper.clearfix.mt30 > div.info-list-fr > ul > li.info-item.t-ramrongliang-liuchang > "
        #         "div.box-item-fl > a")
        #     ram = ram[0].get_text()
        #     # print(ram)
        #     ram_lst.append(ram)
        # except Exception as e:
        #     ram_lst.append("")

        # 分辨率
        # try:
        #     dpi = soup.select(
        #         "body > div.wrapper.clearfix.mt30 > div.info-list-fr > ul > li.info-item.t-fenbianlv-hd > "
        #         "div.box-item-fl > span.product-link")
        #     dpi = dpi[0].get_text()
        #     # print(dpi)
        #     dpi_lst.append(dpi)
        # except Exception as e:
        #     try:
        #         dpi = soup.select("body > div.wrapper.clearfix.mt30 > div.info-list-fr > ul > "
        #                           "li.info-item.t-fenbianlv-hd > div.box-item-fl > a")
        #         dpi = dpi[0].get_text()
        #         # print(dpi)
        #         dpi_lst.append(dpi)
        #     except Exception as e1:
        #         dpi_lst.append("")

        # 电池容量
        # try:
        #     battery_vol = soup.select("body > div.wrapper.clearfix.mt30 > div.info-list-fr > ul > "
        #                               "li.info-item.t-dianchirongliang-yiban > div.box-item-fl > span.product-link")
        #     battery_vol = battery_vol[0].get_text()
        #     battery_vol_lst.append(battery_vol[:-3])
        # except Exception as e:
        #     battery_vol_lst.append("")

        # 屏幕尺寸
        # try:
        #     screen_size = soup.select("body > div.wrapper.clearfix.mt30 > div.info-list-fr > ul > "
        #                               "li.info-item.t-shuangshou > div.box-item-fl > span.product-link")
        #     screen_size = screen_size[0].get_text()
        #     screen_size_lst.append(screen_size[:-2])
        # except Exception as e:
        #     screen_size_lst.append("")

        # 手机品牌
        try:
            mbrand = soup.select("#_j_breadcrumb")
            mbrand = mbrand[0].get_text()
            mbrand_lst.append(mbrand)
        except Exception as e:
            mbrand_lst.append("")

        # ----对所有detail行进行遍历，直到寻找到需要的数据即停止---- flag == 0 不执行
        # OLED列
        all_num = 61
        all_count = all_num - 1

        OLED_flag = 1
        full_screen_flag = 1
        ppi_flag = 1
        size_flag = 1
        release_date_flag = 1
        rom_flag = 1
        WG_flag = 1
        price_flag = 1
        IP_flag = 1
        unlock_flag = 1
        wireless_charge_flag = 1
        screen_size_flag = 1
        front_cam_flag = 1
        back_cam_flag = 1
        ram_flag = 1
        battery_vol_flag = 1
        CPU_flag = 1
        dpi_flag = 1

        for i in range(0, all_num):

            try:
                soup_Val = soup.select("#newPmVal_" + str(i))
                soup_Val = soup_Val[0].get_text()
                # OLED列
                try:
                    if OLED_flag == 1:
                        OLED = soup_Val
                        if "OLED" in OLED:
                            OLED = "1"
                            OLED_lst.append(OLED)
                            OLED_flag = 0
                        elif i == all_count:
                            OLED_lst.append("0")
                            OLED_flag = 0
                            pass
                except Exception as e:
                    OLED_lst.append("0")
                    OLED_flag = 0

                # full screen列
                try:
                    if full_screen_flag == 1:
                        full_screen = soup_Val
                        if "全面" in full_screen:
                            f_screen = "1"
                            full_screen_lst.append(f_screen)
                            full_screen_flag = 0
                        elif i == all_count:
                            full_screen_lst.append("0")
                            full_screen_flag = 0
                            pass
                except Exception as e:
                    full_screen_lst.append("0")
                    full_screen_flag = 0

                # ppi列
                try:
                    if ppi_flag == 1:
                        ppi = soup_Val
                        if "ppi" in ppi:
                            ppi_lst.append(ppi)
                            ppi_flag = 0
                        elif i == all_count:
                            ppi_lst.append("")
                            ppi_flag = 0
                            pass
                except Exception as e:
                    ppi_lst.append("")
                    ppi_flag = 0

                # 手机尺寸
                try:
                    if size_flag == 1:
                        size = soup_Val
                        if "mm" in size and ("x" in size or "*" in size):
                            size_lst.append(size)
                            size_flag = 0
                        elif i == all_count:
                            size_lst.append("")
                            size_flag = 0
                            pass
                except Exception as e:
                    size_lst.append("")
                    size_flag = 0

                # 发布会时间
                try:
                    if release_date_flag == 1:
                        release_date = soup.select("#newPmName_" + str(i))
                        release_date = release_date[0].get_text()
                        if "发布会" or "上市" in release_date:
                            release_date_lst.append(soup_Val)
                            release_date_flag = 0
                        elif i == all_count:
                            release_date_lst.append("")
                            release_date_flag = 0
                            pass
                except Exception as e:
                    release_date_lst.append("")
                    release_date_flag = 0

                # CPU
                try:
                    if CPU_flag == 1:
                        CPU = soup.select("#newPmName_" + str(i))
                        CPU = CPU[0].get_text()
                        if "CPU" in CPU:
                            CPU_lst.append(soup_Val)
                            CPU_flag = 0
                        elif i == all_count:
                            CPU_lst.append("")
                            CPU_flag = 0
                            pass
                except Exception as e:
                    CPU_lst.append("")
                    CPU_flag = 0

                # CPU
                try:
                    if dpi_flag == 1:
                        dpi = soup.select("#newPmName_" + str(i))
                        dpi = dpi[0].get_text()
                        if "主屏分辨率" in dpi:
                            dpi_lst.append(soup_Val.split(">")[0])
                            dpi_flag = 0
                        elif i == all_count:
                            dpi_lst.append("")
                            dpi_flag = 0
                            pass
                except Exception as e:
                    dpi_lst.append("")
                    dpi_flag = 0

                # 电池容量
                try:
                    if battery_vol_flag == 1:
                        battery_vol = soup.select("#newPmName_" + str(i))
                        battery_vol = battery_vol[0].get_text()
                        if "电池容量" in battery_vol:
                            battery_vol_val = re.findall(r'\d+', soup_Val)
                            if len(battery_vol_val) > 0:
                                battery_vol_lst.append(battery_vol_val[0])
                            else:
                                battery_vol_lst.append("")
                            battery_vol_flag = 0
                        elif i == all_count:
                            battery_vol.append("")
                            battery_vol = 0
                            pass
                except Exception as e:
                    battery_vol_lst.append("")
                    battery_vol_flag = 0

                # 5G
                try:
                    if WG_flag == 1:
                        WG = soup_Val
                        if "5G手机" in WG:
                            WG_lst.append("1")
                            WG_flag = 0
                        elif i == all_count:
                            WG_lst.append("")
                            WG_flag = 0
                            pass
                except Exception as e:
                    WG_lst.append("")
                    WG_flag = 0

                # ROM
                try:
                    if rom_flag == 1:
                        rom_val = soup_Val
                        rom = soup.select("#newPmName_" + str(i))
                        rom = rom[0].get_text()
                        if "ROM容量" in rom:
                            rom_val = re.findall(r'\d+GB', rom_val)  # 取值
                            rom_lst.append(rom_val[0])
                            # print(rom_val[0])
                            rom_flag = 0
                        elif i == all_count:
                            rom_lst.append("")
                            rom_flag = 0
                            pass
                except Exception as e:
                    rom_lst.append("")
                    rom_flag = 0

                # RAM
                try:
                    if ram_flag == 1:
                        ram_val = soup_Val
                        ram = soup.select("#newPmName_" + str(i))
                        ram = ram[0].get_text()
                        if "RAM容量" in ram:
                            ram_val = re.findall(r'\d+GB', ram_val)  # 取值
                            ram_lst.append(ram_val[0])
                            # print(ram_val[0])
                            ram_flag = 0
                        elif i == all_count:
                            ram_lst.append("")
                            ram_flag = 0
                            pass
                except Exception as e:
                    rom_lst.append("")
                    rom_flag = 0

                # price
                try:
                    if price_flag == 1:
                        price = soup_Val
                        if "￥" in price:
                            price = price.split("￥")
                            price_lst.append(price[1])
                            price_flag = 0
                        elif i == all_count:
                            price_lst.append("")
                            price_flag = 0
                            pass
                except Exception as e:
                    price_lst.append("")
                    price_flag = 0

                # IP
                try:
                    if IP_flag == 1:
                        IP = soup_Val
                        if "IP" in IP:
                            pattern = re.compile(r'(?<=IP)\d+')
                            new_IP = pattern.findall(IP)
                            IP_lst.append("IP" + str(new_IP[0]))
                            IP_flag = 0
                        elif i == all_count:
                            IP_lst.append("")
                            IP_flag = 0
                            pass
                except Exception as e:
                    IP_lst.append("")
                    IP_flag = 0

                # 解锁方式
                try:
                    unlock_val_new = ""
                    if unlock_flag == 1:
                        unlock_val = soup_Val
                        unlock = soup.select("#newPmName_" + str(i))
                        unlock = unlock[0].get_text()
                        if "解锁方式" in unlock:
                            if "前置" in unlock_val:
                                unlock_val_new = unlock_val_new + "前置指纹 "
                            if "后置" in unlock_val:
                                unlock_val_new = unlock_val_new + "后置指纹 "
                            if "屏幕" in unlock_val:
                                unlock_val_new = unlock_val_new + "屏幕指纹 "
                            if "侧面" in unlock_val:
                                unlock_val_new = unlock_val_new + "侧面指纹"
                            unlock_lst.append(unlock_val_new)
                            unlock_flag = 0
                        elif i == all_count:
                            unlock_lst.append("")
                            unlock_flag = 0
                            pass
                except Exception as e:
                    unlock_lst.append("")
                    unlock_flag = 0

                # 无线充电
                try:
                    if wireless_charge_flag == 1:
                        wireless_charge_val = soup_Val
                        wireless_charge = soup.select("#newPmName_" + str(i))
                        wireless_charge = wireless_charge[0].get_text()
                        if "电池充电" in wireless_charge:
                            if "无线" in wireless_charge_val:
                                wireless_charge_lst.append("1")
                            else:
                                wireless_charge_lst.append("")
                            wireless_charge_flag = 0
                        elif i == all_count:
                            wireless_charge_lst.append("")
                            wireless_charge_flag = 0
                            pass
                except Exception as e:
                    wireless_charge_lst.append("")
                    wireless_charge_flag = 0

                # 屏幕尺寸
                try:
                    if screen_size_flag == 1:
                        screen_size_val = soup_Val
                        screen_size = soup.select("#newPmName_" + str(i))
                        screen_size = screen_size[0].get_text()
                        if "主屏尺寸" in screen_size:
                            screen_size_val = re.findall(r'-?\d+\.?\d*e?-?\d*?', screen_size_val)
                            screen_size_lst.append(screen_size_val[0])
                            screen_size_flag = 0
                        elif i == all_count:
                            screen_size_lst.append("")
                            screen_size_flag = 0
                except Exception as e:
                    screen_size_lst.append("")
                    screen_size_flag = 0

                #  前置摄像头
                try:
                    if front_cam_flag == 1:
                        front_cam_val = soup_Val
                        front_cam = soup.select("#newPmName_" + str(i))
                        front_cam = front_cam[0].get_text()
                        if "前置摄像" in front_cam:
                            front_cam_lst.append(front_cam_val)
                            front_cam_flag = 0
                        elif i == all_count:
                            front_cam_lst.append("")
                            front_cam_flag = 0
                except Exception as e:
                    front_cam_lst.append("")
                    front_cam_flag = 0

                #  后置摄像头
                try:
                    if back_cam_flag == 1:
                        back_cam_val = soup_Val
                        back_cam = soup.select("#newPmName_" + str(i))
                        back_cam = back_cam[0].get_text()
                        if "后置摄像" in back_cam:
                            back_cam_lst.append(back_cam_val)
                            back_cam_flag = 0
                        elif i == all_count:
                            back_cam_lst.append("")
                            back_cam_flag = 0
                except Exception as e:
                    back_cam_lst.append("")
                    back_cam_flag = 0

            except Exception as e:  # 为空属性append一个""
                # print("该机型有某个数据缺失 已经置空")
                if ppi_flag == 1:
                    ppi_lst.append("")
                if size_flag == 1:
                    size_lst.append("")
                if OLED_flag == 1:
                    OLED_lst.append("0")
                if full_screen_flag == 1:
                    full_screen_lst.append("")
                if release_date_flag == 1:
                    release_date_lst.append("")
                if rom_flag == 1:
                    rom_lst.append("")
                if WG_flag == 1:
                    WG_lst.append("")
                if price_flag == 1:
                    price_lst.append("")
                if IP_flag == 1:
                    IP_lst.append("")
                if unlock_flag == 1:
                    unlock_lst.append("")
                if wireless_charge_flag == 1:
                    wireless_charge_lst.append("")
                if screen_size_flag == 1:
                    screen_size_lst.append("")
                if front_cam_flag == 1:
                    front_cam_lst.append("")
                if back_cam_flag == 1:
                    back_cam_lst.append("")
                if ram_flag == 1:
                    ram_lst.append("")
                if battery_vol_flag == 1:
                    battery_vol_lst.append("")
                if CPU_flag == 1:
                    CPU_lst.append("")
                if dpi_flag == 1:
                    dpi_lst.append("")
                break
        # print(len(phone_name_lst) == len(mbrand_lst) == len(index_zol_lst) == len(price_lst) == len(OLED_lst) ==
        # len(IP_lst) == len(full_screen_lst) == len(screen_size_lst) == len(back_cam_lst) == len(front_cam_lst) ==
        # len(CPU_lst) == len(ram_lst) == len(rom_lst) == len(WG_lst) == len(dpi_lst) == len(ppi_lst) == len(
        # unlock_lst) == len(release_date_lst) == len(wireless_charge_lst) == len(battery_vol_lst) == len(size_lst))
    except Exception as e:
        print("被drop的URL", d_url[0])
        # continue


def save_all():
    # # 拆分字段-------------------------------------------------------------------------------

    # 后置摄像头字段拆分
    for i in back_cam_lst:
        if i != "":
            all_back_cam = re.findall(r'\d+', i)
            # for ii in all_back_cam:
            #     if int(ii) < 100:
            #         all_back_cam.remove(ii)
            n = len(all_back_cam)
            back_cam_num_lst.append(n)
            if n > 0:
                if n == 1:
                    back_cam_1.append(all_back_cam[0])
                    back_cam_2.append("")
                    back_cam_3.append("")
                    back_cam_4.append("")
                    back_cam_5.append("")
                if n == 2:
                    back_cam_1.append(all_back_cam[0])
                    back_cam_2.append(all_back_cam[1])
                    back_cam_3.append("")
                    back_cam_4.append("")
                    back_cam_5.append("")
                if n == 3:
                    back_cam_1.append(all_back_cam[0])
                    back_cam_2.append(all_back_cam[1])
                    back_cam_3.append(all_back_cam[2])
                    back_cam_4.append("")
                    back_cam_5.append("")
                if n == 4:
                    back_cam_1.append(all_back_cam[0])
                    back_cam_2.append(all_back_cam[1])
                    back_cam_3.append(all_back_cam[2])
                    back_cam_4.append(all_back_cam[3])
                    back_cam_5.append("")
                if n >= 5:
                    back_cam_1.append(all_back_cam[0])
                    back_cam_2.append(all_back_cam[1])
                    back_cam_3.append(all_back_cam[2])
                    back_cam_4.append(all_back_cam[3])
                    back_cam_5.append(all_back_cam[4])
            else:
                back_cam_1.append("")
                back_cam_2.append("")
                back_cam_3.append("")
                back_cam_4.append("")
                back_cam_5.append("")

        else:
            back_cam_num_lst.append("")
            back_cam_1.append("")
            back_cam_2.append("")
            back_cam_3.append("")
            back_cam_4.append("")
            back_cam_5.append("")

    # 前置摄像头字段拆分
    for i in front_cam_lst:
        if i != "":
            all_front_cam = re.findall(r'\d+', i)
            # for ii in all_front_cam:
            #     if int(ii) < 100:
            #         all_front_cam.remove(ii)
            n = len(all_front_cam)
            if n > 0:
                front_cam_num_lst.append(n)
                if n == 1:
                    front_cam_1.append(all_front_cam[0])
                    front_cam_2.append("")
                    front_cam_3.append("")
                    front_cam_4.append("")
                    front_cam_5.append("")
                if n == 2:
                    front_cam_1.append(all_front_cam[0])
                    front_cam_2.append(all_front_cam[1])
                    front_cam_3.append("")
                    front_cam_4.append("")
                    front_cam_5.append("")
                if n == 3:
                    front_cam_1.append(all_front_cam[0])
                    front_cam_2.append(all_front_cam[1])
                    front_cam_3.append(all_front_cam[2])
                    front_cam_4.append("")
                    front_cam_5.append("")
                if n == 4:
                    front_cam_1.append(all_front_cam[0])
                    front_cam_2.append(all_front_cam[1])
                    front_cam_3.append(all_front_cam[2])
                    front_cam_4.append(all_front_cam[3])
                    front_cam_5.append("")
                if n >= 5:
                    front_cam_1.append(all_front_cam[0])
                    front_cam_2.append(all_front_cam[1])
                    front_cam_3.append(all_front_cam[2])
                    front_cam_4.append(all_front_cam[3])
                    front_cam_5.append(all_front_cam[4])
            else:
                front_cam_1.append("")
                front_cam_2.append("")
                front_cam_3.append("")
                front_cam_4.append("")
                front_cam_5.append("")

        else:
            front_cam_num_lst.append("")
            front_cam_1.append("")
            front_cam_2.append("")
            front_cam_3.append("")
            front_cam_4.append("")
            front_cam_5.append("")

    # 拆分size
    for i in size_lst:
        i = str(i)[:-2]
        if i != "" and ("*" in i or "x" in i):
            i = i.replace("*", "x").split("x")
            try:
                device_length.append(i[0])
            except Exception as e:
                device_length.append("")
            try:
                device_width.append(i[1])
            except Exception as e:
                device_width.append("")
            try:
                device_thickness.append(i[2])
            except Exception as e:
                device_thickness.append("")
        else:
            device_length.append("")
            device_width.append("")
            device_thickness.append("")

    # 拆出CPU品牌
    for i in CPU_lst:
        if i != "":
            i = i.split(" ")
            CPU_brand.append(i[0])
        else:
            CPU_brand.append("")

    # 拆分发布日期
    for i in release_date_lst:
        i = str(i)
        if i != "":
            i = re.findall(r'\d+', i)
            try:
                releaseY.append(i[0])
            except Exception as e:
                releaseY.append("")
            try:
                releaseM.append(i[1])
            except Exception as e:
                releaseM.append("")
        else:
            releaseY.append("")
            releaseM.append("")
    # 保存操作
    # -------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------

    file_path = "data/file_mobile.csv"
    with open(file_path, "w", newline='', encoding='utf-8-sig') as f:
        fieldnames = ["型号", "brand", "index_zol", "price", "OLED", "IP", "full screen", "screen_size", "back_cam_lst",
                      "back_cam_num", "back_cam_1",
                      "back_cam_2",
                      "back_cam_3", "back_cam_4", "back_cam_5", "front_cam_lst", "front_cam_num", "front_cam_1",
                      "front_cam_2",
                      "front_cam_3", "front_cam_4", "front_cam_5", "CPU_brand", "CPU",
                      "ram", "rom", "5G", "dpi", "ppi", "device_length", "device_width", "device_thickness",
                      "fingerprint_type", "release date", "releaseY", "releaseM", "wireless_charge", "battery vol"]

        f_csv = csv.DictWriter(f, fieldnames=fieldnames)
        f_csv.writeheader()
        for i in range(0, len(index_zol_lst)):
            f_csv.writerow(
                {
                    "型号": phone_name_lst[i],
                    "brand": mbrand_lst[i],
                    "index_zol": index_zol_lst[i][0],
                    "price": price_lst[i],
                    "OLED": OLED_lst[i],
                    "IP": IP_lst[i],
                    "full screen": full_screen_lst[i],
                    "screen_size": screen_size_lst[i],
                    "back_cam_lst": back_cam_lst[i],
                    "back_cam_num": back_cam_num_lst[i],
                    "back_cam_1": back_cam_1[i],
                    "back_cam_2": back_cam_2[i],
                    "back_cam_3": back_cam_3[i],
                    "back_cam_4": back_cam_4[i],
                    "back_cam_5": back_cam_5[i],
                    "front_cam_lst": front_cam_lst[i],
                    "front_cam_num": front_cam_num_lst[i],
                    "front_cam_1": front_cam_1[i],
                    "front_cam_2": front_cam_2[i],
                    "front_cam_3": front_cam_3[i],
                    "front_cam_4": front_cam_4[i],
                    "front_cam_5": front_cam_5[i],
                    "CPU_brand": CPU_brand[i],
                    "CPU": CPU_lst[i],
                    "ram": ram_lst[i][:-2],
                    "rom": rom_lst[i][:-2],
                    "5G": WG_lst[i],
                    "dpi": dpi_lst[i],
                    "ppi": ppi_lst[i],
                    "device_length": device_length[i],
                    "device_width": device_width[i],
                    "device_thickness": device_thickness[i],
                    "fingerprint_type": unlock_lst[i],
                    "release date": release_date_lst[i].replace("年", "/").replace("月", "/").replace("日", ""),
                    "releaseY": releaseY[i],
                    "releaseM": releaseM[i],
                    "wireless_charge": wireless_charge_lst[i],
                    "battery vol": battery_vol_lst[i]
                }
            )
    endtime = datetime.datetime.now()
    print("Starttime:", starttime)
    print("Endtime:", endtime)
    print("This Program runs ", (endtime - starttime).seconds, " seconds！")


# if __name__ == '__main__':
#     with ProcessPoolExecutor(max_workers=3) as p:
#         for url in all_url_lst[0:10]:
#             p.submit(grab_all, url[0])
#     save_all()
#     print("343434")
# threads = []
# n = 0
# p = 0
# for d_url in all_url_lst:
#     # try:
#     # if p % 100 == 0:
#     #     time.sleep(10)
#     #     print("暂停10s")
#     t = threading.Thread(target=grab_all, args=(d_url[0],))
#     threads.append(t)
#     # t.setDaemon(True)
#     # t.start()
#     # if n > 15:
#     #     # time.sleep(4)
#     #     t.join()
#     #     print("join")
#     #     n = 0
# for t in threads:
#     p = p + 1
#     # print("执行了join")
#     if p % 300 == 0:
#         time.sleep(10)
#         p = 0
#     t.start()
# for t in threads:
#     # print("执行了join")
#     t.join()
# tasks = []
# for url in all_url_lst[0]:
#     c = url_data(url)
#     d_url = asyncio.ensure_future(c)
#     d_url.add_done_callback(grab_all)
#     tasks.append(d_url)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
for url in all_url_lst:
    grab_all(url[0])
save_all()

# while len(threading.enumerate()) > 1:
#     pass
