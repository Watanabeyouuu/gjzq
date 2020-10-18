# 用于导出文件中所有index值 并拼接成url
# 运行完此文件后 data下会生成file_url.csv
# 之后运行find_detail即可爬取所有file_url.csv下手机的数据

import csv

detail_url = []
all_url_lst = []
file_ori = 'data/手机机型信息.csv'
# 读取需要的index
csv_file_ori = open(file_ori)  # 打开csv文件
csv_reader_lines_ori = csv.reader(csv_file_ori)  # 逐行读取csv文件
index_ori_lst = []  # 创建列表准备接收csv各行数据
for one_line in csv_reader_lines_ori:
    # index_new.append(one_line)  # 将读取的csv分行数据按行存入列表‘date’中
    index_ori_lst.append(one_line[1])
index_ori_lst.remove('index_zol')
print(index_ori_lst)

# ******方法二******直接url拼接 速度快 准确率也极高（错误的url会被自动drop 不会有脏数据）

# print(all_url)
# index = re.findall("\d+", all_url)
for index in index_ori_lst:
    index = index.replace(' ', '')
    print(index)
    print(detail_url)
    index_left = int(index[:-3]) + 1
    detail_url = "http://detail.zol.com.cn/" + str(index_left) + "/" + str(index) + "/param.shtml"
    all_url_lst.append(detail_url)  # 所有url入主列

print(len(all_url_lst))

with open("data/file_url.csv", "w", encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    for url in all_url_lst:
        # print(url)
        csv_writer.writerow([url])
