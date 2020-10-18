import pymysql
import pandas as pd
from pandas import DataFrame, Series

# 打开数据库连接(host一般都是localhost，user填写用户名，password是密码，port一般也是3306)
db = pymysql.connect(host='rm-uf6xl20b441n3f2mwoo.mysql.rds.aliyuncs.com', user='intern', password='intern_Gjzq',
                     port=3306, db="bi_data")
cursor = db.cursor()  # 获取游标
data = cursor.execute("SELECT * FROM tab_co_type_datas")  # 执行SQL查询，获取数据
data = list(cursor.fetchall())  # 获取单条数据
# print(data)
db.close()  # 关闭数据库连接

# # 获取的数据存入本地（也可在下面的模型中直接使用 data ）
# re_outfile = u'D:\\pythondata\\re_zhibiao.xlsx'
# data_re.to_excel(re_outfile)
# print(u'数据读取结束，并保存至本地：', str(outputfile))

columnDes = cursor.description  # 获取连接对象的描述信息
columnNames = [columnDes[i][0] for i in range(len(columnDes))]  # 获取列名
df = pd.DataFrame([list(i) for i in data], columns=columnNames)  # 得到的data为二维元组，逐行取出，转化为列表，再转化为df
print(df)
