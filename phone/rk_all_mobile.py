# 将所有数据入库
import csv
import re

import pymysql


def zgc_mobile_rk(table_name, file_path, add_flag):
    csv_file = open(file_path)  # 打开csv文件
    csv_reader_lines = csv.reader(csv_file)  # 逐行读取csv文件
    data = []  # 创建列表准备接收csv各行数据

    for one_line in csv_reader_lines:
        data.append(one_line)

    # db = pymysql.connect("localhost", "root", "123456", "zgc", charset='utf8')
    db = pymysql.connect("rm-uf6xl20b441n3f2mwoo.mysql.rds.aliyuncs.com", "yumh_db", "yumh123!@#", "bi_data",
                         charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    insert_sql = "INSERT INTO " + table_name + \
                 " (`id`,`mobile_name`, `mobile_name_ori`, `brand`, `top5_brand`, `price`, `OLED`," \
                 "`IP`, `full_screen`, `screen_per`, `screen_per_group`, `screen_size`, `back_cam_lst`, " \
                 "`back_cam_num`, " \
                 "`back_cam_1_group`, `back_cam_1`," \
                 "`back_cam_2`, " \
                 "`back_cam_3`,`back_cam_4`, `back_cam_5`, `front_cam_lst`, `front_cam_num`, `front_cam_1_group`," \
                 "`front_cam_1`," \
                 "`front_cam_2`, `front_cam_3`,`front_cam_4`, `front_cam_5`,`cpu_brand`, " \
                 "`cpu`,`ram`, `rom`,`5G`, `dpi`, `ppi`, `ppi_group`, `screen_area_m2`, `device_length`," \
                 "`device_width`, `device_thickness`,`fingerprint_type`, `release_date`," \
                 "`release_Y`, `release_M`, `quick_charge`, `wireless_charge`, `battery_vol`, `battery_vol_group`) " \
                 "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
                 " %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    create_drop = "DROP TABLE IF EXISTS " + table_name
    try:
        if add_flag == 0:
            cursor.execute(create_drop)
            sql = """CREATE TABLE """ + table_name + """ (
                 id VARCHAR(80) PRIMARY KEY,
                 mobile_name VARCHAR(255) NOT NULL,
                 mobile_name_ori VARCHAR(80),
                 brand VARCHAR(80),
                 top5_brand VARCHAR(40),
                 price VARCHAR(30), 
                 OLED VARCHAR(50),
                 IP VARCHAR(50),
                 full_screen VARCHAR(50),
                 screen_per VARCHAR(50),
                 screen_per_group VARCHAR(50),
                 screen_size VARCHAR(50),
                 back_cam_lst VARCHAR(225),
                 back_cam_num VARCHAR(50),
                 back_cam_1_group VARCHAR(50),
                 back_cam_1 VARCHAR(50),
                 back_cam_2 VARCHAR(50),
                 back_cam_3 VARCHAR(50),
                 back_cam_4 VARCHAR(50),
                 back_cam_5 VARCHAR(50),
                 front_cam_lst VARCHAR(225),
                 front_cam_num VARCHAR(50),
                 front_cam_1_group VARCHAR(50),
                 front_cam_1 VARCHAR(50),
                 front_cam_2 VARCHAR(50),
                 front_cam_3 VARCHAR(50),
                 front_cam_4 VARCHAR(50),
                 front_cam_5 VARCHAR(50),
                 cpu_brand VARCHAR(50),
                 cpu VARCHAR(100),
                 ram VARCHAR(50),
                 rom VARCHAR(50),
                 5G VARCHAR(50),
                 dpi VARCHAR(150),
                 ppi VARCHAR(50),
                 ppi_group VARCHAR(50),
                 screen_area_m2 VARCHAR(50),
                 device_length VARCHAR(255),
                 device_width VARCHAR(255),
                 device_thickness VARCHAR(255),
                 fingerprint_type VARCHAR(50),
                 release_date VARCHAR(50),
                 release_Y VARCHAR(50),
                 release_M VARCHAR(50),
                 wireless_charge VARCHAR(50),
                 quick_charge VARCHAR(50),
                 battery_vol VARCHAR(50),
                 battery_vol_group VARCHAR(50)
                 )"""
            cursor.execute(sql)
        # 提交插入操作
        for i in range(1, len(data)):
            mobile_name = data[i][0].replace("参数", "")
            brand = data[i][1][:-2]
            index = data[i][2]
            price = data[i][3]
            OLED = data[i][4]
            IP = data[i][5]
            full_screen = data[i][6]
            screen_per = data[i][7]
            screen_size = data[i][8]
            back_cam_lst = data[i][9]
            back_cam_num = data[i][10]
            back_cam_1 = data[i][11]
            back_cam_2 = data[i][12]
            back_cam_3 = data[i][13]
            back_cam_4 = data[i][14]
            back_cam_5 = data[i][15]
            front_cam_lst = data[i][16]
            front_cam_num = data[i][17]
            front_cam_1 = data[i][18]
            front_cam_2 = data[i][19]
            front_cam_3 = data[i][20]
            front_cam_4 = data[i][21]
            front_cam_5 = data[i][22]
            CPU_brand = data[i][23]
            CPU = data[i][24]
            ram = data[i][25]
            rom = data[i][26]
            WG = data[i][27]
            dpi = data[i][28]
            ppi = data[i][29]
            size = data[i][30]
            device_length = data[i][31]
            device_width = data[i][32]
            device_thickness = data[i][33]
            fingerprint_type = data[i][34]
            release_date = data[i][35]
            releaseY = data[i][36]
            releaseM = data[i][37]
            wireless_charge = data[i][38]
            quick_charge = data[i][39]
            battery_vol = data[i][40]

            try:
                screen_area_m2 = float(device_width) * float(device_length) * float(screen_per) / 100000000
            except Exception as e:
                screen_area_m2 = ""
            try:  # 五大品牌
                if brand == "OPPO" or brand == "realme":
                    top5_brand = "OPPO(含realme)"
                elif brand == "小米" or brand == "红米":
                    top5_brand = "小米(含红米）"
                elif brand == "华为" or brand == "荣耀":
                    top5_brand = "华为(含荣耀)"
                elif brand == "苹果":
                    top5_brand = "苹果"
                elif brand == "vivo" or brand == "iQOO":
                    top5_brand = "vivo(含iQOO)"
                else:
                    top5_brand = "其他"

                if len(back_cam_1) > 0:
                    bcg1 = int(back_cam_1)
                else:
                    bcg1 = 0

                if len(front_cam_1) > 0:
                    fcg1 = int(front_cam_1)
                else:
                    fcg1 = 0

                if len(battery_vol) > 0:  # 电池
                    batt = int(battery_vol)
                else:
                    batt = 0

                if len(ppi) > 0:  # ppi
                    ppi_l = int(ppi[:-3])
                else:
                    ppi_l = 0

                if len(screen_per) > 0:
                    screen_per_l = float(screen_per)
                else:
                    screen_per_l = 0

                if bcg1 == 0:  # 后摄像头分组
                    back_cam1_group = ""
                elif bcg1 <= 1000:
                    back_cam1_group = "0"
                elif bcg1 <= 1300:
                    back_cam1_group = "1001-1300"
                elif bcg1 <= 2000:
                    back_cam1_group = "1301-2000"
                elif bcg1 < 4000:
                    back_cam1_group = "2001-3999"
                elif bcg1 < 4800:
                    back_cam1_group = "4000-4799"
                elif bcg1 < 6400:
                    back_cam1_group = "4800-6399"
                elif bcg1 < 10800:
                    back_cam1_group = "6400-10799"
                else:
                    back_cam1_group = "10800-"

                if fcg1 == 0:  # 前摄像头1分组
                    front_cam1_group = ""
                elif fcg1 <= 500:
                    front_cam1_group = "0-500"
                elif fcg1 <= 1000:
                    front_cam1_group = "501-1000"
                elif fcg1 <= 1300:
                    front_cam1_group = "1001-1300"
                elif fcg1 <= 2000:
                    front_cam1_group = "1301-2000"
                else:
                    front_cam1_group = "2000-"

                if batt == 0:  # 电池容量分组
                    battery_vol_group = ""
                elif batt <= 2000:
                    battery_vol_group = "0-2000"
                elif batt <= 3000:
                    battery_vol_group = "2001-3000"
                elif batt <= 4000:
                    battery_vol_group = "3001-4000"
                else:
                    battery_vol_group = "4000-"

                if ppi_l == 0:  # ppi分组
                    ppi_group = ""
                elif ppi_l <= 200:  # ppi分组
                    ppi_group = ""
                elif ppi_l <= 300:  # ppi分组
                    ppi_group = "201-300"
                elif ppi_l <= 400:
                    ppi_group = "301-400"
                elif ppi_l <= 500:
                    ppi_group = "401-500"
                else:
                    ppi_group = "500-"

                if screen_per_l == 0:
                    screen_per_group = ""
                elif screen_per_l <= 50:
                    screen_per_group = "-50%"
                elif screen_per_l <= 60:
                    screen_per_group = "50-60%"
                elif screen_per_l <= 70:
                    screen_per_group = "60-70%"
                elif screen_per_l <= 80:
                    screen_per_group = "70-80%"
                elif screen_per_l <= 90:
                    screen_per_group = "80-90%"
                elif screen_per_l > 90:
                    screen_per_group = "90%-"
                else:
                    screen_per_group = ""

                m_name = re.sub('\\（.*?\\）', '', mobile_name)
                val = (
                    index, mobile_name, m_name, brand, top5_brand, price, OLED, IP, full_screen, screen_per,
                    screen_per_group,
                    screen_size, back_cam_lst, back_cam_num, back_cam1_group, back_cam_1, back_cam_2, back_cam_3,
                    back_cam_4,
                    back_cam_5, front_cam_lst, front_cam_num, front_cam1_group, front_cam_1, front_cam_2, front_cam_3,
                    front_cam_4,
                    front_cam_5, CPU_brand, CPU, ram, rom, WG, dpi, ppi, ppi_group, screen_area_m2, device_length,
                    device_width,
                    device_thickness, fingerprint_type, release_date, releaseY, releaseM, quick_charge, wireless_charge,
                    battery_vol, battery_vol_group

                )
                cursor.execute(insert_sql, val)
            except Exception as e:
                print("问题是：", e)
                continue

        db.commit()


    except Exception as e:
        print(e)
        # Rollback in case there is any error
        db.rollback()

    # 关闭数据库连接
    db.close()


if __name__ == '__main__':

    # 对应文件里的数据
    # add_flag = 0
    # table_name = "tab_mobile_file_info"
    # file_path = 'data/爬虫_中关村在线_匹配数据.csv'

    # 所有数据
    # add_flag = 0
    # table_name = "tab_mobile_all_info"
    # file_path = 'data/爬虫_中关村在线_所有数据.csv'

    # 新增数据
    add_flag = 1
    table_name = "tab_mobile_file_info"
    file_path = 'data/爬虫_中关村在线_新增数据.csv'

    zgc_mobile_rk(table_name, file_path, add_flag)
