from bs4 import BeautifulSoup
import requests
import lxml
import re
import time

url = 'http://baozoumanhua.com/catalogs/gif?page=3'

wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'html.parser')

titles = soup.select('div.article-content > h4 > a[target="_blank"]')
imgs = soup.select('div.article-content > video')

#imgs = soup.findAll('video')
#print(titles)
#print(imgs)
for title,img in zip(titles,imgs):
    data = {
        'title' :title.get_text(),
        'img' :img.get('data-original-image-url')
    }
    print(data)

'''
/usr/local/bin/python3 /Users/netseek/github/python_practice/test1.py
{'title': '这体重，一会怎么救上来', 'img': 'http://wanzao2.b0.upaiyun.com/system/pictures/36074785/original/1464255479_240x131.gif'}
{'title': '放上点特效就是不一样的画风了', 'img': 'http://wanzao2.b0.upaiyun.com/system/pictures/36072280/original/1464243973_400x283.gif'}
{'title': '睡一觉起来感觉好饿。随便吃点吧！', 'img': 'http://wanzao2.b0.upaiyun.com/system/pictures/36073551/original/1464250611_440x303.gif'}
{'title': '宝宝好困。宝宝要睡觉！', 'img': 'http://wanzao2.b0.upaiyun.com/system/pictures/36073503/original/1464250382_350x229.gif'}
{'title': '你这是侮辱佛门 还是侮辱自己 替表演者感到羞愧！', 'img': 'http://wanzao2.b0.upaiyun.com/system/pictures/36073802/original/1464251597_320x240.gif'}
{'title': '有谁试过', 'img': 'http://wanzao2.b0.upaiyun.com/system/pictures/36071341/original/1464239840_233x413.gif'}
{'title': '机智。', 'img': 'http://wanzao2.b0.upaiyun.com/system/pictures/36071680/original/1464241151_400x207.gif'}
{'title': '叫你买个好的女朋友。', 'img': 'http://wanzao2.b0.upaiyun.com/system/pictures/36071797/original/1464241611_300x299.gif'}

Process finished with exit code 0

'''
