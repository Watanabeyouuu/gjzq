"""
@author: Francis | 韩 心 海
@contact: xinhai_han@icloud.com
@file: tdxj.py
@date: 2020/11/6 5:18 下午

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
import pandas as pd
import numpy as np


def gradientDescent(X, y, theta, alpha, iters):
    temp = np.matrix(np.zeros(theta.shape))
    parameters = int(theta.ravel().shape[1])
    cost = np.zeros(iters)

    for i in range(iters):
        error = (X * theta.T) - y

        for j in range(parameters):
            term = np.multiply(error, X[:, j])
            temp[0, j] = theta[0, j] - ((alpha / len(X)) * np.sum(term))

        theta = temp
        cost[i] = computeCost(X, y, theta)

    return theta, cost


# 这个部分实现了Ѳ的更新


def computeCost(X, y, theta):
    inner = np.power(((X * theta.T) - y), 2)
    return np.sum(inner) / (2 * len(X))


# 这个部分计算J(Ѳ)，X是矩阵
# 这个部分实现了Ѳ的更新
alpha = 0.01
iters = 1500
data2 = pd.read_csv("../data/mlt.csv", header=None, names=['Size', 'Bedrooms', 'Price'])
# print(data2)
data2 = (data2 - data2.mean()) / data2.std()
# print(data2)
# 加一列常数项
data2.insert(0, 'Ones', 1)

# 初始化X和y
cols = data2.shape[1]
print(data2)
print(cols)
X2 = data2.iloc[:, 0:cols - 1]
y2 = data2.iloc[:, cols - 1:cols]
print(X2)
print(y2)
# 转换成matrix格式，初始化theta
X2 = np.mat(X2.values)
y2 = np.mat(y2.values)
theta2 = np.mat(np.array([0, 0, 0]))

# 运行梯度下降算法
g2, cost2 = gradientDescent(X2, y2, theta2, alpha, iters)
print(g2)

