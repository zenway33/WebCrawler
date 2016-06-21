
from bs4 import BeautifulSoup
import requests
import os

# 建立一个目录用于存储下载的文件:
path = os.getcwd()
path = os.path.join(path,'baozou2016')
if not os.path.exists(path):
    os.mkdir(path)

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36',
    'Referer': 'http://baozoumanhua.com/',
}

# download function url,filename
def download(img_url,file_name):
    r = requests.get(img_url, stream = True,headers=headers)
    # print(r.status_code)
    #print(file_name
    with open(path + '/' + file_name, "wb") as fs:
        fs.write(r.content)
        fs.close
    print("%s => %s" % (img_url, file_name))

'''
# 调试打印单页的相关图片;

#urls = 'http://baozoumanhua.com/catalogs/gif?page=1'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'html.parser')

titles = soup.select('div.article-content > h4 > a[target="_blank"]')
imgs = soup.select('div.article-content > video')


# 打印标题及图表相关的信息,并构造成字典
for title,img in zip(titles,imgs):
    data = {
        'title' :title.get_text(),
        'img_url' :img.get('data-original-image-url')
    }

    print(data)
    #title = print(data['title'])
    #url = print(data['img_url'])

'''

#构建函数获取页面相关的图片.
def get_page_within(pages):
    for page_num in  range(1,pages+1):
        wb_data = requests.get('http://baozoumanhua.com/catalogs/gif?page={}'.format(page_num))
        soup = BeautifulSoup(wb_data.text, 'html.parser')
        titles = soup.select('div.article-content > h4 > a[target="_blank"]')
        imgs = soup.select('div.article-content > video')

        for title,img in zip(titles,imgs):
            data = {
                'title' :title.get_text(),
                'img_url' :img.get('data-original-image-url')
            }
            #print(data)
            img_url = data['img_url']
            file_name = data['title'] + '.gif'
            #file_name = "test.gif"
            #
            download(img_url,file_name)

    print('woo ... %d pages done' % pages)


#获取3页里的信息
get_page_within(3)

'''
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