import csv
import pymysql

index_aim = []
no_match_lst = []
# --------------------------------------
# 需要读取的
file_ori = 'data/手机机型信息.csv'
# 爬虫爬到的
file_all = 'data/forprintall.csv'
# 匹配好的数据 同时会再次打开进行如库操作
file = 'data/match_mobile_info.csv'
# --------------------------------------
duplic_lst = []
# 读取所有index
csv_file = open(file_all)  # 打开csv文件
csv_reader_lines = csv.reader(csv_file)  # 逐行读取csv文件
index_all_lst = []  # 创建列表准备接收csv各行数据
for one_line in csv_reader_lines:
    # index_new.append(one_line)  # 将读取的csv分行数据按行存入列表‘date’中
    # print(one_line[2])
    index_all_lst.append(one_line)

# 读取需要的index
csv_file_ori = open(file_ori)  # 打开csv文件
csv_reader_lines_ori = csv.reader(csv_file_ori)  # 逐行读取csv文件
index_ori_lst = []  # 创建列表准备接收csv各行数据
for one_line in csv_reader_lines_ori:
    # index_new.append(one_line)  # 将读取的csv分行数据按行存入列表‘date’中
    # print(one_line)
    index_ori_lst.append(one_line)
# print(index_ori_lst[0])
print(len(index_all_lst), len(index_ori_lst))
# print(index_all_lst)
# for i in range(0, len(index_all_lst)):
#     for j in range(0, len(index_ori_lst)):
#         if index_ori_lst[j][1] == index_all_lst[i][2]:
#             index_aim.append(index_all_lst)
#
# print(index_ori_lst)
pp = 0
dup = 0
for i in range(0, len(index_all_lst)):
    for j in range(0, len(index_ori_lst)):
        if index_ori_lst[j][1] == index_all_lst[i][2]:
            if index_ori_lst[j][1] in duplic_lst:
                dup = dup + 1
                continue
            duplic_lst.append(index_ori_lst[j][1])
            index_aim.append(index_all_lst[i])
            pp = pp + 1
print("匹配到:", pp)
print("DROP重复项目：", dup)
# print(no_match_lst)
# print("有", len(no_match_lst), "个数据未匹配")
with open(file, "w", encoding='utf-8-sig') as file:
    csv_writer = csv.writer(file)
    for i in range(0, len(index_aim)):
        # print(url)
        csv_writer.writerow(index_aim[i])

# 执行入库操作--------------
# 读取match好的数据
csv_file = open('data/match_mobile_info.csv')  # 打开csv文件
csv_reader_lines = csv.reader(csv_file)  # 逐行读取csv文件
data = []  # 创建列表准备接收csv各行数据
for one_line in csv_reader_lines:
    # index_new.append(one_line)  # 将读取的csv分行数据按行存入列表‘date’中
    # print(one_line[2])
    data.append(one_line)
    # print(one_line)
db = pymysql.connect("localhost", "root", "123456", "zgc", charset='utf8')
# 使用cursor()方法获取操作游标
cursor = db.cursor()

insert_sql = "INSERT INTO tab_mobile_all_info(`id`,`mobile_type`, `mobile_brand`,`mobile_price`, `mobile_OLED`," \
             "`mobile_IP`, `mobile_full_screen`, `mobile_screen_size`,`mobile_back_cam_num`, `mobile_back_cam_1`,`mobile_back_cam_2`, " \
             "`mobile_back_cam_3`,`mobile_back_cam_4`, `mobile_back_cam_5`,`mobile_front_cam_num`, `mobile_front_cam_1`," \
             "`mobile_front_cam_2`, `mobile_front_cam_3`,`mobile_front_cam_4`, `mobile_front_cam_5`,`mobile_cpu_brand`, " \
             "`mobile_cpu`,`mobile_ram`, `mobile_rom`,`mobile_5G`, `mobile_dpi`,`mobile_ppi`, `mobile_device_length`," \
             "`mobile_device_width`, `mobile_device_thickness`,`mobile_fingerprint_type`, `mobile_release_date`," \
             "`mobile_release_Y`, `mobile_release_M`,`mobile_wireless_charge`, `mobile_battery_vol`) " \
             "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
             "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

# 修改操作
# update_sql = "update test_table set `name`='不是区区名字' where `name` = '区区名字'"
# 获取操作
create_drop = "DROP TABLE IF EXISTS tab_mobile_all_info"
# select_sql = "select * from test_table where `name` = '不是区区名字'"
try:
    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute(create_drop)
    sql = """CREATE TABLE tab_mobile_all_info (
         id VARCHAR(80) PRIMARY KEY,
         mobile_type VARCHAR(255) NOT NULL,
         mobile_brand VARCHAR(20),
         mobile_price VARCHAR(30), 
         mobile_OLED VARCHAR(50),
         mobile_IP VARCHAR(50),
         mobile_full_screen VARCHAR(50),
         mobile_screen_size VARCHAR(50),
         mobile_back_cam_num VARCHAR(50),
         mobile_back_cam_1 VARCHAR(50),
         mobile_back_cam_2 VARCHAR(50),
         mobile_back_cam_3 VARCHAR(50),
         mobile_back_cam_4 VARCHAR(50),
         mobile_back_cam_5 VARCHAR(50),
         mobile_front_cam_num VARCHAR(50),
         mobile_front_cam_1 VARCHAR(50),
         mobile_front_cam_2 VARCHAR(50),
         mobile_front_cam_3 VARCHAR(50),
         mobile_front_cam_4 VARCHAR(50),
         mobile_front_cam_5 VARCHAR(50),
         mobile_cpu_brand VARCHAR(50),
         mobile_cpu VARCHAR(100),
         mobile_ram VARCHAR(50),
         mobile_rom VARCHAR(50),
         mobile_5G VARCHAR(50),
         mobile_dpi VARCHAR(50),
         mobile_ppi VARCHAR(50),
         mobile_device_length VARCHAR(255),
         mobile_device_width VARCHAR(255),
         mobile_device_thickness VARCHAR(255),
         mobile_fingerprint_type VARCHAR(50),
         mobile_release_date VARCHAR(50),
         mobile_release_Y VARCHAR(50),
         mobile_release_M VARCHAR(50),
         mobile_wireless_charge VARCHAR(50),
         mobile_battery_vol VARCHAR(50)
         )"""
    cursor.execute(sql)
    # 提交插入操作
    for i in range(1, len(data)):
        val = (
        data[i][2], data[i][0], data[i][1], data[i][3], data[i][4], data[i][5], data[i][6], data[i][7], data[i][9],
        data[i][10], data[i][11], data[i][12], data[i][13], data[i][14], data[i][16], data[i][17], data[i][18],
        data[i][19], data[i][20], data[i][21], data[i][22], data[i][23], data[i][24], data[i][25], data[i][26],
        data[i][27], data[i][28], data[i][29], data[i][30], data[i][31], data[i][32], data[i][33], data[i][34],
        data[i][35], data[i][36], data[i][37])
        cursor.execute(insert_sql, val)

    db.commit()


except Exception as e:
    print(e)
    # Rollback in case there is any error
    db.rollback()

# 关闭数据库连接
db.close()

