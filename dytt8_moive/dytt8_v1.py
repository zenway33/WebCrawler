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


web_url = 'http://www.dytt8.net/'
wb_data = requests.get(web_url,headers=headers)
wb_data.encoding = 'gb2312' #保证不乱码
soup = BeautifulSoup(wb_data.text, 'lxml')
#print(soup.prettify())
#header > div > div.bd2 > div.bd3 > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(2) > div.title_all > p > strong
#<a href="/html/gndy/dyzz/20160610/51200.html">2016年传记喜剧《飞鹰艾迪》BD中英双字幕</a>
links = [a.attrs.get('href') for a in soup.select('a[href^=/html/gndy/dyzz/2016]')]
moive_names = soup.select('div > ul > tr')

#print(links)
#link = 'http://www.dytt8.net/html/gndy/dyzz/20160617/51247.html'

root_url = 'http://www.dytt8.net'

# get vide page urls  list
def get_video_page_url():
    urllist=[] #定义一个列表
    for  link in links:
        link = root_url +link
        urllist.append(link)
    return urllist

urllists = get_video_page_url()
#print(urllists)


'''
    for moive_name,link  in zip(moive_names,links):
        data = {
            'moive_name' : moive_name.get_text().strip('\n'),
            'link' : 'http://www.dytt8.net' + link
         }
        #print(data)
        return data['link']
'''

#get video download url
def get_video_data(link):
    wb_data = requests.get(link, headers=headers)
    wb_data.encoding = 'gb2312'
    soup = BeautifulSoup(wb_data.text, 'lxml')
    #thunder = soup.select('tr > td > a')[0].get_text()
    #print(thunder)
    return soup.select('tr > td > a')[0].get_text()


# 采用单进程模式耗时47秒.
'''
def show_video_stats():
    start_time = time.time()
    video_page_urls = urllists
    for video_page_url  in video_page_urls:
        print(get_video_data(video_page_url))
    print("--- %s seconds ---" % (time.time() - start_time))
    #--- 47.005714893341064 seconds ---
'''

#get_video_page_urls()
# 先获得要抓取页面的url,然后再通过一个方法批量的抓取数据;
def show_video_stats():
    start_time = time.time()
    pool = Pool(30)
    video_page_urls = urllists
    #for video_page_url  in video_page_urls:
         #print(get_video_data(video_page_url))
    results = pool.map(get_video_data, video_page_urls)
    #print ftp_url
    for ftp_url in results:
        print(ftp_url)
    #print(results)
    print("--- %s seconds ---" % (time.time() - start_time))
    #--- 7.236294984817505 seconds ---

show_video_stats()


















