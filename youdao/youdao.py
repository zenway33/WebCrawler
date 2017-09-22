#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 有道翻译词及句子
import requests
from bs4 import BeautifulSoup


headers = {
       #'User-Agent': ua,
       'User-Agent': 'Mozilla/5.8 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       #'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       #'Accept-Encoding' : 'gzip, deflate, sdch',
       #'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
       'Connection': 'keep-alive'
}

def youdao(word):
    url = 'http://dict.youdao.com/w/{}/#keyfrom=dict2.top'.format(word.strip())
    print(url)

    wb_data = requests.get(url,headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')

    #num = word.split(' ')
    #i = int(len(num))
    #print(i)

    if  int(len(word.split(' '))) > 3:
        # > two words
        transl = soup.select('div > p')
        #print(transl)
        print(transl[1].get_text().strip())
    else:
        transl = soup.select('div.title > span')
        #print(transl)
        print(transl[0].get_text().strip())



def query():
    print('*' * 33)
    while True:
        word = input('>>>')
        youdao(word)
        print('*' * 33)

if __name__ == '__main__':
    query()

