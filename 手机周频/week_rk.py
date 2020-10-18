import csv
from isoweek import Week
import pymysql

db = pymysql.connect("rm-uf6xl20b441n3f2mwoo.mysql.rds.aliyuncs.com", "biuser", "biusergjzq", "gjzq_db2",
                     charset='utf8')
# db = pymysql.connect("localhost", "root", "123456", "week_mobile", charset='utf8')
# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 读取需要的data
csv_file = open('data/周频.csv')  # 打开csv文件
csv_reader_lines = csv.reader(csv_file)  # 逐行读取csv文件
mobile_sale_info_lst = []  # 创建列表准备接收csv各行数据
for one_line in csv_reader_lines:
    mobile_sale_info_lst.append(one_line)
mobile_sale_info_lst.remove(mobile_sale_info_lst[0])

insert_sql = "INSERT INTO tab_mobile_sales(`hist_date`, `mobile_name`,`date_original`, `sales`, `date_month`, " \
             "`date_week`, `m_index`)" \
             " values (%s, %s, %s, %s, %s, %s, %s)"

create_drop = "DROP TABLE IF EXISTS tab_mobile_sales"
# select_sql = "select * from test_table where `name` = '不是区区名字'"
try:
    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute(create_drop)
    sql = """CREATE TABLE tab_mobile_sales(
         hist_date VARCHAR (60),
         mobile_name VARCHAR(255) NOT NULL,
         date_original VARCHAR(20),
         sales INTEGER(30),
         date_month INTEGER(15),
         date_week INTEGER (15),
         m_index VARCHAR(20))"""
    cursor.execute(sql)
    # 提交插入操作
    for mobile_sale_info_lst in mobile_sale_info_lst:
        w = Week(2020, int(mobile_sale_info_lst[4]))
        # hist_date = str(w.thursday())
        if mobile_sale_info_lst[2] in "\\" or mobile_sale_info_lst[2] in "nan":
            # print(mobile_sale_info_lst[2])
            continue
        val = (str(w.thursday()), mobile_sale_info_lst[0], mobile_sale_info_lst[1], mobile_sale_info_lst[2],
               mobile_sale_info_lst[3], mobile_sale_info_lst[4], mobile_sale_info_lst[5])
        cursor.execute(insert_sql, val)
    db.commit()

except Exception as e:
    print("这出错了", e)
    # Rollback in case there is any error
    db.rollback()

# 关闭数据库连接
db.close()
