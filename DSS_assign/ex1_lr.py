"""
@author: Francis | 韩 心 海
@contact: xinhai_han@icloud.com
@file: ex1_lr.py
@date: 2020/11/5 3:43 下午

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
from builtins import print

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame, Series
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def ex1():
    sales = pd.read_csv("data/ex1.csv")
    sales = pd.DataFrame(sales)
    # print(sales.iloc[:, 1:5])
    s_data = sales.iloc[:, 1:5]
    # print(sales.iloc[:, 2:])
    # 数据描述
    # print(s_data.describe())
    s_data.boxplot()
    plt.show()
    # 相关系数0~0.3弱相关0.3~0.6中等程度相关0.6~1强相关
    # print(s_data.corr())
    sns.pairplot(s_data, x_vars=["", "price", "expenses", "production"], y_vars='sales', height=7, kind='reg')
    plt.show()

    X_train, X_test, Y_train, Y_test = train_test_split(sales.iloc[:, 2:], sales.sales, train_size=.60)

    # print("原始数据特征:", sales.iloc[:, 2:].shape,
    #       ",训练数据特征:", X_train.shape,
    #       ",测试数据特征:", X_test.shape)
    #
    # print("原始数据标签:", sales.sales.shape,
    #       ",训练数据标签:", Y_train.shape,
    #       ",测试数据标签:", Y_test.shape)

    model = LinearRegression()
    model.fit(X_train, Y_train)
    a = model.intercept_  # 截距
    b = model.coef_  # 回归系数
    print("最佳拟合线:截距", a, ",回归系数：", b)

    score = model.score(X_test, Y_test)
    print("拟合效果", score)
    # 对线性回归进行预测
    Y_pred = model.predict(X_test)
    # print("X_test", X_test)
    print(Y_pred)
    plt.plot(range(len(Y_pred)), Y_pred, 'b', label="predict")
    # 显示图像
    # plt.savefig("predict.jpg")
    plt.show()
    plt.figure()
    plt.plot(range(len(Y_pred)), Y_pred, 'b', label="predict")
    plt.plot(range(len(Y_pred)), Y_test, 'r', label="test")
    plt.legend(loc="upper right")  # 显示图中的标签
    plt.xlabel("the number of sales")
    plt.ylabel('value of sales')
    plt.show()

    # def predict(price, exp, pro):
    #     sales = a + b[0] * price + b[1] * exp + b[2] * pro
    #     return sales
    pre_expense = (265.32130 * 1.1 - b[0] * 41.26383 - b[2] * 157.00) / b[1]
    print('广告支出费需要达到:', pre_expense)
    pre_price = (265.32130 * 1.1 - b[1] * 114.18541 - b[2] * 157.00) / b[0]
    print('价格下降到到:', pre_price)


if __name__ == '__main__':
    ex1()
