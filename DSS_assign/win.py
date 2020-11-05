"""
@author: Francis | 韩 心 海
@contact: xinhai_han@icloud.com
@file: win.py
@date: 2020/11/5 7:59 下午

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
import tkinter as tk
from DSS_assign import ex1_lr

window = tk.Tk()
window.title('my window')
window.geometry('800x400')

# 创建输入框entry，用户输入任何内容都显示为*

# 创建一个文本框用于显示
t1 = tk.Text(window, height=1, width=70)
t1.grid(row=0, column=1)
t2 = tk.Text(window, height=1, width=70)
t2.grid(row=1, column=1)
t3 = tk.Text(window, height=1, width=70)
t3.grid(row=2, column=1)


# 定义触发事件时的函数
def insert_point():
    data = ex1_lr.ex1_1()
    print(data)
    t1.insert('insert', data[0])
    t2.insert('insert', data[1])
    t3.insert('insert', data[2])


tk.Label(text='公式', width=6).grid(row=0, column=0)
tk.Label(text='拟合效果', width=6).grid(row=1, column=0)
tk.Label(text='广告支出', width=6).grid(row=2, column=0)
b1 = tk.Button(window, text='开始拟合', width=15, height=2, command=insert_point)
b1.grid(row=3, column=1)

window.mainloop()
