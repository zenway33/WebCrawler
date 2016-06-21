# -*- coding: utf-8 -*-
"""
Created on 2016/06/02
@author: zenway33
"""


from bs4 import BeautifulSoup
import requests
import time
import os


# 建立一个目录用于存储下载的文件:
path = os.getcwd()
path = os.path.join(path,'jiandanxxoo')
if not os.path.exists(path):
    os.mkdir(path)


headers = {
       'User-Agent': 'Mozilla/5.8 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'
}

# 单个页面的内容抓取分析
'''
url = 'http://jandan.net/ooxx/page-2007'
wb_data = requests.get(url,headers=headers)
soup = BeautifulSoup(wb_data.text, 'html.parser')

imgs = soup.select('p > img')

for img_url in imgs:
    url = img_url.get('src')
    print(url)
'''

#构造下载方法
def download(url):
    r = requests.get(url, stream = True,headers=headers)
    #with open(path + '/' + file_name, "wb") as fs:
    with open(path + '/' + '{}.jpg'.format(index), "wb") as fs:
        fs.write(r.content)
        fs.close
    print("%s ... is download" % url)

#下载图片,输入年限如 2003,2006（年的图片）
for page_num in range(1997,2008):
    wb_data =requests.get('http://jandan.net/ooxx/page-{}'.format(page_num), headers=headers)
    time.sleep(5)
    soup = BeautifulSoup(wb_data.text, 'html.parser')
    imgs =  soup.select('p > img')
    #print(imgs)

    for index,img_url in enumerate(imgs):
        url = img_url.get('src')
        #file_name = url.split('/')[-1]
        #print(file_name)
        #print(url)
        download(url)



