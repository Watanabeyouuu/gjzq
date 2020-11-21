import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from urllib.request import urlretrieve
import os
import pdfkit

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/85.0.4183.83 Safari/537.36 "
}
cookies = {'cookie': ''}

url_lst = []


def url_data(url):
    res = requests.get(url, cookies=cookies, headers=headers)
    d = res.text
    soup = BeautifulSoup(d, "html.parser")
    return soup


def text_url_c():  # 用于爬取所有文章的url
    url = 'http://www.csindex.com.cn/zh-CN/indices/notices-and-announcements?index=&start_date=&end_date=&notice_type=2&index_series=all'
    soup = url_data(url)
    tr_list = soup.find_all('tr')

    doc_array = []
    for index in range(1, len(tr_list)):
        tr_info = tr_list[index]
        td_list = tr_info.findAll('td')
        notice_title = tr_info.a.get_text().strip()
        notice_url = tr_info.a['href'].strip()
        notice_type = td_list[1].get_text().strip()
        index_series = td_list[2].get_text().strip()
        release_date = td_list[3].get_text().strip()
        doc_array.append([notice_title, notice_url, notice_type, index_series, release_date])
    dataframe = pd.DataFrame(doc_array, columns=['公告标题', '公告地址', '公告类型', '相关指数系列', '发布时间'])
    dataframe.to_csv('data/notices.csv', index=False)
    # print(title[1].a['href'])  # 链接
    # print(title[1].a.get_text())  # 文件名
    # for i in range(1, len(title)):
    #     url_lst.append(title[i].a['href'])
    # print(url_lst)  # 所有url


def text_c():  # 爬取文章内容
    soup = url_data('http://www.csindex.com.cn/zh-CN/indices/notices-and-announcements-detail/1424')

    # print(soup)
    print(soup.find_all('p'))


def saveHtml(file_name, file_content):
    with open(file_name, "wb") as f:
        f.write(file_content)


def get_notice_detail(pdf_folder, notice_url):
    soup = url_data(notice_url)
    nDetails = soup.find_all(name='div', attrs={"class": "nDetails"})
    if not nDetails or len(nDetails) < 1:
        print("error %s %s" % (pdf_folder, notice_url))
        return None
    # pdfkit.from_string('<head><meta charset="UTF-8"></head>' + nDetails[0].prettify(),
    #                    'data/notices/%s.pdf' % notice_title)

    pdf_urls = nDetails[0].find_all('a')
    for pdf_url in pdf_urls:
        # if not 'href' in pdf_url:
        #     continue
        url = pdf_url.get('href')
        if not url or not url.endswith(".pdf"):
            continue
        if 'http://www.csindex.com.cn/' not in url:
            url = 'http://www.csindex.com.cn' + url
        if not pdf_url.span:
            continue
        # if not os.path.exists(pdf_folder):
        #     os.makedirs(pdf_folder)
        urlretrieve(url, '%s_%s.pdf' % (pdf_folder, pdf_url.span.text))
    return nDetails[0].prettify()


def get_notices():
    notices = pd.read_csv('data/notices.csv', index_col=False)
    nDetails_html = '<head><meta charset="UTF-8"></head>'
    doc_array = []
    for index, row in notices.iterrows():
        notice_title = row['公告标题']
        release_date = row['发布时间']
        notice_url = row['公告地址']

        indexs = re.findall(r"关于修订(.+?)指数", notice_title)
        if indexs:
            nDetails = get_notice_detail('data/files/%s_%s指数' % (release_date, indexs[0]), notice_url)
            if nDetails:
                nDetails_html = nDetails_html + nDetails + '<br /><br /><br />'
            continue
        indexs = re.findall(r"关于变更(.+?)指数", notice_title)
        if indexs:
            nDetails = get_notice_detail('data/files/%s_%s指数' % (release_date, indexs[0]), notice_url)
            if nDetails:
                nDetails_html = nDetails_html + nDetails + '<br /><br /><br />'
            continue
        doc_array.append([notice_title, notice_url, row['公告类型'], row['相关指数系列'], release_date])

    dataframe = pd.DataFrame(doc_array, columns=['公告标题', '公告地址', '公告类型', '相关指数系列', '发布时间'])
    dataframe.to_csv('data/类别三列表.excel', index=False)
    pdfkit.from_string(nDetails_html, 'data/%s.pdf' % '中证指数')


# if __name__ == '__main__':
#     # text_c()
#     text_url_c()


# text_url_c()
get_notices()
# get_notice_detail('data/test', 'http://www.csindex.com.cn/zh-CN/indices/notices-and-announcements-detail/1505')
