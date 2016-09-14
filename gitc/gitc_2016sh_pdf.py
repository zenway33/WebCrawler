#/usr/bin/env python3.5
# -*- coding: utf-8 -*-
__author__ = 'zenway33'

from bs4 import BeautifulSoup
import requests
import time
import os
from multiprocessing import Process, Pool

pdf_dir = 'gitc2016'
if not os.path.isdir(pdf_dir):
    os.mkdir(pdf_dir)


headers = {
       #'User-Agent': ua,
       'User-Agent': 'Mozilla/5.8 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       #'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       #'Accept-Encoding' : 'gzip, deflate, sdch',
       #'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
       'Connection': 'keep-alive'
}

web_url = 'http://www.thegitc.com/2016shanghai/view/ppt.html'


# 获取pdf url
def get_pdf_urls(web_url):
    wb_data = requests.get(web_url,headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    pdfs = soup.select('area[href^="http://"]')

    pdf_urls=[]
    for pdf_url in pdfs:
        pdf = pdf_url.get('href').strip('#')
        pdf_urls.append(pdf)
    return pdf_urls

urls = get_pdf_urls(web_url)

#print(urls)

# 下载pdf文件
def download_pdf(pdf_url):
    r = requests.get(pdf_url, stream = True,headers=headers)
    pdf_name = pdf_url.split('/')[-1]
    with open(os.path.join(pdf_dir, pdf_name), 'wb') as fs:
        fs.write(r.content)

    print("filename: %s , downnload -> image_url: %s" % (pdf_name , pdf_url))

# 多线程下载执行
def get_pdf_status():
    start_time = time.time()
    pool = Pool(30)
    pdf_urls = urls
    #print(pdf_urls)
    results = pool.map(download_pdf, pdf_urls)
    print("--- %s seconds ---" % (time.time() - start_time))

get_pdf_status()