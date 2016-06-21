
#简书首页抓取
from bs4 import BeautifulSoup
import requests
from multiprocessing.pool import ThreadPool as Pool
import time
import random
import re
import os

headers = {
       'User-Agent': 'Mozilla/5.8 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'
}

#list-container > ul.article-list.thumbnails > li:nth-child(5) > div > h4 > a
#list-container > ul.article-list.thumbnails > li:nth-child(3) > div > p > a

web_url = 'http://www.jianshu.com/'
wb_data = requests.get(web_url,headers=headers)
soup = BeautifulSoup(wb_data.text, 'lxml')

titles = soup.select('div > h4 > a')
links = [a.attrs.get('href') for a in soup.select('a[href^=/p/]')]
authors = soup.select('div > p > a')
#views = soup.select('div >  a[target="_blank"]')
read = soup.find_all('a', text=re.compile(r'阅读'))
comment = soup.find_all('a', text=re.compile(r'评论'))


# 获取数字的函数
def trans2numbers(string):
    return int(''.join(a for a in string.strip() if a.isdigit()))

def get_numbers(read):
    result = []
    for i in read:
        result.append(trans2numbers(i.string))
    return result

reads = get_numbers(read)
'''
def comment_numbers(comment):
    result = []
    for i in comment:
        result.append(trans2numbers(i.string))
    return result
'''
comments = get_numbers(comment)


'''
for title in titles:
    title = title.get_text()
    print(title)

for link in links:
    base = 'http://www.jianshu.com'
    url = base + link
    print(url)
'''

for author,title,link,read,comment in zip(authors,titles,links,reads,comments):
    data = {
        'author' : author.get_text(),
        'title' : title.get_text(),
        'link' : 'http://www.jianshu.com' + link,
        'read' : read,
        'comment' : comment
        #'view' :

    }
    print(data)


