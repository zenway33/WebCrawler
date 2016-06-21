# #!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
url = 'http://apis.baidu.com/txapi/mvtp/meinv'
#url = 'http://apis.baidu.com/txapi/mvtp/meinv?num=10'

headers = {"apikey":"32fef326202400cc1bb3c08488c8775b"}
params = {'num':'10'}
r = requests.get(url, params=params,headers=headers)
r = r.json()

def saveImage(imgUrl, imgName = 'default.jpg'):
    response = requests.get(imgUrl,stream = True)
    image = response.content
    dst = "/Users/netseek/python/baidu/"
    path = dst + imgName
    #print 'save the file:'+path+'\n'
    with open(path,'wb') as img:
        img.write(image)
    img.close()

def run():
    for line in r['newslist']:
        title = line['title']
        picUrl = line['picUrl']
        print(title)
        print(picUrl)
        saveImage(picUrl,imgName=title+'.jpg')
run()
