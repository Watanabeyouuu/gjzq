import csv
import pandas as pd

# 全局lst变量
date_val_lst = []
value_lst = []
month_lst = []
week_lst = []

# 数据源
io = "data/手机销量周频数据最终版(5).xlsx"
# io = "/Users/hanxinhai/PycharmProjects/gjzq/data/1111.xlsx" # Test
P_data = pd.read_excel(io, sheet_name=0)
P_data.rename(columns={P_data.columns[1]: '1.1-1.5', P_data.columns[2]: '1.6-1.12', P_data.columns[3]: '1.13-1.19',
                       P_data.columns[4]: '1.20-1.26', P_data.columns[5]: '1.27-1.31', P_data.columns[6]: '2.1-2.2',
                       P_data.columns[7]: '2.3-2.9', P_data.columns[8]: '2.10-2.16', P_data.columns[9]: '2.17-2.23',
                       P_data.columns[10]: '2.24-2.29', 7.31: "7.31-7.31"}, inplace=True)
# print(P_data.head())
# print(P_data.columns)
# P_type = P_data.iloc[:, 0]
P_col = P_data.columns[1:]  # 表头
P_value = P_data.loc[:, P_col]  # 销量值df
# print(len(P_col))

P_type = P_data['机型列表']
# print(P_type)
# print(P_value)
for row in P_value.itertuples():
    value_lst.append(row[:])  # 按 行->列 顺序获取到每一个value值，并且存入tuple [( ), ( )]
for i in range(0, P_value.shape[0]):
    for j in range(0, P_value.shape[1]):
        # print(P_type[i], P_col[j], value_lst[i][j + 1])
        date_val_lst.append(  # dict存入主列
            {
                "机型": P_type[i],
                "日期": P_col[j],
                "销量": value_lst[i][j + 1]
            }
        )
        pass
print(date_val_lst)
# 计算月份
# print(len(date_val_lst))
for i in range(0, len(date_val_lst)):
    date = str(date_val_lst[i]["日期"])
    # print(date)
    month = date.split('.')[0]
    if len(month) == 1:
        month = "0" + month
    elif len(month) == 2:
        month = month
    else:
        month = "N/A"
    month_lst.append(month)  # 生成"月"序列
# print(date_val_lst)
# print(month_lst)
# date_val_lst[29]['月份'] = month_lst[29]
# print(date_val_lst)
for i in range(0, len(date_val_lst)):  # 将月份列添加进主lst
    date_val_lst[i]['月份'] = month_lst[i]

# 计算周数
sub = 0
w = 0
flag = 0  # 第二次计算的控制开关
count = 0  # 行计数器
for i in range(0, len(date_val_lst)):
    count += 1
    # if i != 0:
    date = str(date_val_lst[i]["日期"])
    # print(date)
    d = date.split('-')
    try:  # 非标准日期格式
        sub = int(d[1].split('.')[1]) - int(d[0].split('.')[1])
    except Exception as e:
        sub = "null"
    if count > len(P_col):  # 每循环一行进行一次周数重置 同时对计数器count重置
        w = 0
        count = 1
    if d[0] == "3.1":
        w += 1
    if sub != 6:  # 连续出现差值非6时, 对第二个非6，周数-1，同时关闭开关
        # print(type(d[0]))
        if flag == 1:
            w -= 1
            flag = 0
        w += 1
        flag = 1
        pass
    else:
        w += 1
        flag = 0
    week_lst.append(w)

for i in range(0, len(date_val_lst)):  # 将周数列添加进主lst
    date_val_lst[i]['周数'] = week_lst[i]
    # print(w, "---", sub, d[0].split('.')[0] + "." + d[0].split('.')[1], "count:", count)
    # else:
    #     w = 1
    #     print(w)
# print(week_lst)

# 保存到csv
file_path = "data/周频.csv"
with open(file_path, "w", newline='', encoding='utf-8-sig') as f:
    fieldnames = ["机型", "日期", "销量", "月份", "周数"]
    f_csv = csv.DictWriter(f, fieldnames=fieldnames)
    f_csv.writeheader()
    for i in range(0, len(date_val_lst)):
        f_csv.writerow(
            date_val_lst[i]
        )
