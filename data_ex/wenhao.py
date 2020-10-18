#
from isoweek import Week
#
# a = "23"
# # b = "46"
# # c = "421"
# #
# # print(len(a) == len(b) == len(c))
#
# str = "3gag5"
# str = str.split(" ")
# print(str[0])
import multiprocessing
import re
lst = []
# i = "F镜头63.075"
# all_back_cam = re.findall(r'-?\d+\.?\d*e?-?\d*?', i)
# print(all_back_cam)
# n = len(all_back_cam)
# lst.append(all_back_cam)
# lst.append("343")
# if n == 0:
#     print("yes0")
# if n >= 5:
#     print("yes")
# lst.append("heuf欧式风".split(">")[0])
# print(lst)
# cpu_count = multiprocessing.cpu_count()
# print('Cpu count:', cpu_count)
# str = "高通 骁龙625（MSM8953）更多高通 骁龙625（MSM8953）手机>，手机性能排行>"
# str1 = str.split("更多")[1]
# print(str1)


# w = Week(2020, 11)
# print("Week %s starts on %s" % (w, w.thursday()))
#
# print("Current week number is", Week.thisweek().week)
# print("Next week is", Week.thisweek() + 1)
# i = ""
# ss = re.findall(r'\d+', i)
# print(ss)
str = "￥4999￥10758"
str1 = str.split('￥')
print(str1)