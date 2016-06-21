# #!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
url = 'http://apis.baidu.com/showapi_open_bus/showapi_joke/joke_text'
headers = {"apikey":"32fef326202400cc1bb3c08488c8775b"}
params = {'page':'1'}
r = requests.get(url, params=params,headers=headers)
r = r.json()
#r = r.keys() //获取key,这个有两层

if(r):
#json_result = json.loads(content) #转换为字典对象
#  下面从这个字典中获得笑话的标题和正文
    content_list = r['showapi_res_body']['contentlist']

# 只取第一条笑话的标题和正文
    #first_title = content_list[0]['title'].encode('utf8')
    #first_text = content_list[0]['text'].encode('utf8')
    #print('标题：'+ first_title.decode('utf-8'))
    #print('内容：'+ first_text.decode('utf-8'))

#  都打印出来
    t = r['showapi_res_body']['contentlist']
    for line in t:
        title = line['title']
        text = line['text']
        print('--------------')
        print('标题:' + title)
        print('内容:' + text)
else:
    print(error)
