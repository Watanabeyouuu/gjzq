import csv
import re

import requests
from bs4 import BeautifulSoup

# 全局
index_zol_lst = []
brand_lst = []  # 所有手机型号
brand_url_lst = []  # 型号的url
page_lst = []  # 该品牌下的页数
all_url_lst = []  # 所有手机的detail页面
OLED_lst = []  # OLED列
full_screen_lst = []  # full screen列
phone_name_lst = []  # 手机型号列
back_cam_num_lst = []  # 摄像头列

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/85.0.4183.83 Safari/537.36 "
}
cookies = {'cookie': 'ip_ck=4sGF5Pryj7QuNTY0MzA1LjE1OTk1MzU0MTM%3D; '
                     'z_pro_city=s_provice%3Dshanghai%26s_city%3Dshanghai; '
                     'Hm_lvt_ae5edc2bc4fc71370807f6187f0a2dd0=1599535425; visited_subcateId=57; '
                     'visited_subcateProId=57-0; userProvinceId=2; userCityId=0; userCountyId=0; userLocationId=26; '
                     'realLocationId=26; userFidLocationId=26; '
                     'z_day=izol110770%3D3%26izol110792%3D5%26izol110769%3D3%26izol110794%3D2%26ixgo20%3D1%26rdetail'
                     '%3D9; questionnaire_pv=1599523236; '
                     'visited_serachKw=%u5C0F%u7C73%7C%u534E%u4E3A%7C%u590F%u666EAQUOS%20mini%20SH-03H; Adshow=5; '
                     'lv=1599543319; vn=2; Hm_lpvt_ae5edc2bc4fc71370807f6187f0a2dd0=1599543319; listSubcateId=57'}


def url_data(url):
    res = requests.get(url, cookies=cookies, headers=headers)
    d = res.text
    return d


data = url_data("http://detail.zol.com.cn/cell_phone_index/subcate57_list_1.html")  # 主页面
soup = BeautifulSoup(data, "html.parser")
for b in range(2, 96):  # 获取手机品牌lst 和 该品牌url 完整为range(2, 96)
    brand_url_ori = soup.select("#J_ParamBrand > a:nth-child(" + str(b) + ")")  # 品牌url
    brand_url = "http://detail.zol.com.cn" + (re.compile(r'\"(.*?)\"').findall(str(brand_url_ori)))[0]
    brand_url_lst.append(brand_url)

    brand = (soup.select("#J_ParamBrand > a:nth-child(" + str(b) + ")"))[0].get_text()  # 品牌名
    brand_lst.append(brand)
    print(brand)

for u in brand_url_lst:  # 获取每个品牌的有效页数
    data = url_data(u)
    soup = BeautifulSoup(data, "html.parser")
    try:
        page = str(soup.select("body > div.wrapper.clearfix > div.content > div.page-box > div.pagebar")[0].get_text())
    except Exception as e:
        page = "1"
    # print(u, page)
    page_num = re.compile(r'\d+\.?\d*').findall(page)
    page_lst.append(page_num[0])
    # print(page_lst)

# 爬取某个品牌每一页url 并作为最外层循环开始爬取所有手机的detail页面url
count = -1
for bul in brand_url_lst:
    count += 1
    for p in range(1, len(page_lst[count]) + 1):
        url_aim = bul[:-5] + "_0_1_2_0_" + str(p) + ".html"
        # print(url_aim)
        # data = url_data(url_aim)
        # soup = BeautifulSoup(data, "html.parser")
        for i in range(1, 49):  # 每一页12x4个 range(1, 49)
            try:
                data = url_data(url_aim)
                soup = BeautifulSoup(data, "html.parser")
                single_p = soup.select("#J_PicMode > li:nth-child(" + str(i) + ") > h3 > a")[0]
                # single_p = soup.select("#J_PicMode > li:nth-child(" + "2" + ") > h3 > a")[0]
                # print(";;;;;;", single_p)
                all_url = "http://detail.zol.com.cn" + single_p['href']
                print(all_url)
            except Exception as e:  # 通常最后一页不是12x4个 所以需要con掉
                continue
            # 对本次循环获取到的单机url 进一步选择并获取详细信息页面的url 有两种方式

            # ******方法一****** 进入手机页面后通过css选择器进入'详细页面' 速度慢 但url提取准确率为100%

            # data = url_data(all_url)
            # soup = BeautifulSoup(data, "html.parser")
            # detail_url = soup.select("#secondsUnderstand > div.tab-con > div > div > a")
            # print(detail_url)
            # try:
            #     detail_url = "http://detail.zol.com.cn" + detail_url[0]['href']
            #     print(detail_url)
            #     all_url_lst.append(detail_url)  # 所有url入主列
            # except Exception as e:
            #     print("出现了异常")
            #     continue
            # --------------------

            # ******方法二******直接url拼接 速度快 准确率也极高、但还未测试（错误的url会被自动drop 不会有脏数据）

            # print(all_url)
            index = re.findall("\d+", all_url)
            detail_url = "http://detail.zol.com.cn/" + str(index[0][:-3]) + "/" + str(index[0]) + "/param.shtml"
            print(detail_url)
            # print("---")
            all_url_lst.append(detail_url)  # 所有url入主列
# print(all_url_lst)
# -------------------------------------------------------------------------------
# 已爬取中关村在线所有手机的detail url
# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
print(all_url_lst)
with open("data/all_url.csv", "w", encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    for url in all_url_lst:
        # print(url)
        csv_writer.writerow([url])

# # 循环一下获取到的主lst 对detail info进行爬取
# for d_url in all_url_lst:
#     # print("------", d_url)
#     data = url_data(d_url)  # 读取detail url的信息
#     soup = BeautifulSoup(data, "html.parser")
#     print(d_url)
#     phone_name = soup.select("body > div.product-model.page-title.clearfix > h1")  # 手机型号列
#     phone_name_lst.append(phone_name[0].get_text())
#     index_zol = re.findall(".*/(.*)/param.shtml.*", d_url)  # 正则 匹配index_zol列
#     index_zol_lst.append(index_zol)  # 将index_zol存入其主列
#
#     for ol in range(0, 100):
#         OLED = "0"
#         try:
#             OLED_ori = soup.select("#newPmVal_" + str(ol))  # OLED列
#             OLED = OLED_ori[0].get_text()
#
#             if "OLED" in OLED:
#                 # print(OLED)
#                 OLED = "1"
#                 OLED_lst.append(OLED)
#                 break
#             else:
#                 pass
#             # print("---", OLED_1)
#         except Exception as e:
#             # print(OLED)
#             OLED = "0"
#             OLED_lst.append(OLED)
#             break
#
#     for fc in range(0, 100):
#         f_screen = "0"
#         try:
#             full_screen = soup.select("#newPmVal_" + str(fc))  # full_screen列
#             # full_screen = full_screen[0].get_text()
#             full_screen = full_screen[0].get_text()
#             if "全面" in full_screen:
#                 f_screen = "1"
#                 full_screen_lst.append(f_screen)
#                 break
#             else:
#                 pass
#         except Exception as e:
#             f_screen = "0"
#             full_screen_lst.append(f_screen)
#             break
#
#     for bcn in range(0, 100):
#         back_cam_num = "0"
#         try:
#             back_cam_num = soup.select("#newPmVal_" + str(bcn))  # back_cam_num列
#             # full_screen = full_screen[0].get_text()
#             back_cam_num = back_cam_num[0].get_text()
#             if "摄像" in back_cam_num:
#                 back_cam_num_lst.append(back_cam_num)
#                 print(back_cam_num)
#                 break
#             # if "全面" in back_cam_num:
#             #     f_screen = "1"
#             #     full_screen_lst.append(f_screen)
#             #     break
#             # else:
#             #     pass
#         except Exception as e:
#             print("未知")
#             back_cam_num_lst.append(back_cam_num)
#             break
#
# # -------------------------------------------------------------------------------
# # 保存操作
# # -------------------------------------------------------------------------------
# # -------------------------------------------------------------------------------
# print(len(all_url_lst), len(index_zol_lst), len(OLED_lst), len(full_screen_lst))
# print(OLED_lst)
# file_path = "/Users/hanxinhai/PycharmProjects/gjzq/data/phone_detail_info.csv"
# with open(file_path, "w", newline='', encoding='utf-8-sig') as f:
#     fieldnames = ["型号", "index_zol", "OLED", "full screen", "back_cam_num"]
#     f_csv = csv.DictWriter(f, fieldnames=fieldnames)
#     f_csv.writeheader()
#     for i in range(0, len(index_zol_lst)):
#         f_csv.writerow(
#             {
#                 "型号": phone_name_lst[i],
#                 "index_zol": index_zol_lst[i][0],
#                 "OLED": OLED_lst[i],
#                 "full screen": full_screen_lst[i],
#                 "back_cam_num": back_cam_num_lst[i]
#             }
#         )
