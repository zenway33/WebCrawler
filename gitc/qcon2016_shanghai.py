#/usr/bin/env python3.5
# -*- coding: utf-8 -*-
__author__ = 'zenway33'
from bs4 import BeautifulSoup
import requests
from multiprocessing import Pool
import time
import random
import re
import os

headers = {
       #'User-Agent': ua,
       'User-Agent': 'mozilla/5.0 (iphone; cpu iphone os 5_1_1 like mac os x) applewebkit/534.46 (khtml, like gecko) mobile/9b206 micromessenger/5.0',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       #'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       #'Accept-Encoding' : 'gzip, deflate, sdch',
       #'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
       'Connection': 'keep-alive'
}


web_url = 'http://ppt.geekbang.org/qconsh2016'
wb_data = requests.get(web_url,headers=headers)
#wb_data.encoding = 'gb2312' #保证不乱码
soup = BeautifulSoup(wb_data.text, 'lxml')
#print(soup.prettify())
links = [a.attrs.get('href') for a in soup.select('a[href^=/slide/download]')]
titles = soup.find_all(class_="link")


for title,link in zip(titles,links):
    data = {
        'title': title.get_text(),
        'link' : 'http://ppt.geekbang.org/' + link.strip('/13')
    }
    print(data)













