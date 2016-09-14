#/usr/bin/env python3.5
# -*- coding: utf-8 -*-
__author__ = 'zenway33'
#dytt8 2016新片精品 ftp地址获取
from bs4 import BeautifulSoup
import requests
from multiprocessing import Pool
import time
import random
import re
import os

headers = {
       #'User-Agent': ua,
       'User-Agent': 'Mozilla/5.8 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       #'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       #'Accept-Encoding' : 'gzip, deflate, sdch',
       #'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
       'Connection': 'keep-alive'
}

# http://s.dydytt.net/plus/search.php?kwtype=0&keyword=2015%20%B6%AF%BB%AD

web_url = 'http://s.dydytt.net/plus/search.php?kwtype=0&keyword=2016%20%B6%AF%BB%AD'
wb_data = requests.get(web_url,headers=headers)
wb_data.encoding = 'gb2312' #保证不乱码
soup = BeautifulSoup(wb_data.text, 'lxml')
#print(soup.prettify())d(1) > td:nth-child(2) > b > a
links = [a.attrs.get('href') for a in soup.select('a[href^=/html/gndy/jddy]')]
#links = soup.select('b > a')
moive_names = soup.select('div > ul > tr')

print(links)
#print(moive_names)

root_url = 'http://www.ygdy8.com'

# get vide page urls  list
def get_video_page_url():
    urllist=[] #定义一个列表
    for  link in links:
        link = root_url +link
        urllist.append(link)
    return urllist

page_urls = get_video_page_url()
# 去重url,并保留原来的顺序
page_urls_uniq = sorted(set(page_urls),key=page_urls.index)
print(page_urls_uniq)

# 抓取页面
def get_url_within(pages):
    for page_num in  range(1,pages+1):
        wb_data = requests.get('http://s.dydytt.net/plus/search.php?kwtype=0&keyword=2016%20%B6%AF%BB%AD&PageNo={}'.format(page_num))

#get_url_within(3)

'''
2016 动画
1、 输入年限 2016
2、 获取页数
3、 获得取URL

'''
