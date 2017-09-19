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
       'User-Agent': 'Mozilla/5.8 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       #'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       #'Accept-Encoding' : 'gzip, deflate, sdch',
       #'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
       'Connection': 'keep-alive'
}


web_url = 'http://www.jinse.com/'
wb_data = requests.get(web_url,headers=headers)
soup = BeautifulSoup(wb_data.text, 'lxml')

#links = soup.select('ul > h3 > a')
links = [a.attrs.get('href') for a in soup.select('ul > h3 > a')]
titles = [a.attrs.get('title') for a in soup.select('ul > h3 > a')]
#date_time = soup.select('div > ol > ul > ul > ul > li')

#//*[@id="main1"]/div[1]/ol[2]/ul/ul
#main1 > div:nth-child(1) > ol:nth-child(2) > ul > ul > li:nth-child(2)
#print(date_time)

#print(links)
#print(titles)
#print(len(links))
#print(len(titles))


for title,link in zip(titles,links):
    data = {
        'title' :title,
        'link'  :link
    }
    print(data)
