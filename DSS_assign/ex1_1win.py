"""
@author: Francis | 韩 心 海
@contact: xinhai_han@icloud.com
@file: ex1_1win.py
@date: 2020/11/5 10:31 下午

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
from tkinter import *
from DSS_assign import ex1_lr


class Application(tk.Frame):
    data = ['', '']

    def __init__(self, root):
        super().__init__(root)
        self.master = root
        self.pack()
        self.envar = tk.StringVar(None, "***")
        self.intWind()

    def EX1(self):
        data = ex1_lr.ex1_1()
        self.envar = tk.StringVar(None, data[0])
        # self.score = tk.StringVar(None, ex1_lr.ex1_1()[1])
        # self.expense = tk.StringVar(None, ex1_lr.ex1_1()[2])
        # self.price = tk.StringVar(None, ex1_lr.ex1_1()[3])

    def intWind(self):
        Label(self, text='回归公式', width=10).grid(row=0, column=0)
        # Entry(self, width=70, textvariable=self.envar).grid(row=0, column=1)
        # Label(self, text='拟合效果', width=10).grid(row=1, column=0)
        # Entry(self, textvariable=self.score).grid(row=1, column=1)
        # Label(self, text='广告支出费需要达到:', width=15).grid(row=2, column=0)
        # Entry(self, textvariable=self.expense).grid(row=2, column=1)

        text1 = Text(self, width=30, height=1)
        text1.insert(END, self.data[0])
        text1.grid(row=0, column=1)
        # text1.insert(END, self.data[0])

        # text.grid()
        # text.insert('end', '123')
        Button(self, text='登陆', width=15, command=self.EX1).grid(row=3, column=1)


if __name__ == '__main__':
    root = tk.Tk()
    application = Application(root=root)
    application.mainloop()
