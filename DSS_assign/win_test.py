"""
@author: Francis | 韩 心 海
@contact: xinhai_han@icloud.com
@file: win_test.py
@date: 2020/11/5 8:24 下午

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


class Application(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.master = root
        self.pack()
        self.envar = tk.StringVar(None, '123')

        self.intWind()

    def intWind(self):
        Label(self, text='截距', width=5).grid(row=0, column=0)
        Entry(self, textvariable=self.envar).grid(row=0, column=1)
        Label(self, text='回归公示', width=5).grid(row=1, column=0)
        Entry(self, textvariable=self.envar).grid(row=1, column=1)
        Label(self, text='123', width=5).grid(row=2, column=0)
        Entry(self, textvariable=self.envar).grid(row=2, column=1)

        Button(self, text='登陆', width=15).grid(row=3, column=1)
        # text = Text(self)
        # text.grid()
        # text.insert('end', '123')


if __name__ == '__main__':
    root = tk.Tk()
    application = Application(root=root)
    application.mainloop()
