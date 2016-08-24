
# -*- coding: utf-8 -*-

# 思路:获取 URL 列表,再获取详细页,再获取页面信息
#

import requests, time, pymongo
from bs4 import BeautifulSoup

def gender_info(soup):  # 获取性别信息
    gender = 'female' if soup.find_all('div','div.member_ico1') else 'male'
    return gender

#获取具体页面的信息
def get_info(url):
    wb_data = requests.get(url)  # 向服务器请求页面
    wb_data.encoding ='utf-8'  # 标明编码为utf-8,以免出现解码错误
    soup = BeautifulSoup(wb_data.text,'lxml')  # 以lxml方式对页面进行解析
    title = soup.select('h4 em')[0].text
    address = soup.select('span.pr5')[0].text
    price = int(soup.select('div.day_l span')[0].text)
    img = soup.select('#curBigImage')[0].get('src')
    hostPic = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')[0].get('src')
    hostName = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')[0].text
    hostGender = gender_info(soup)
    data = {
        'title' : title,
        'address': address,
        'price' : price,
        'img' :img,
        'hostPic' : hostPic,
        'hostName' : hostName,
        'hostGender' : hostGender
    }
    #print
    print(data)
    return data

# 获取页面中所有详细房源的url
def get_list_url(pageURL):
    listUrl = []
    wb_data = requests.get(pageURL)
    wb_data.encoding = 'utf-8'
    soup = BeautifulSoup(wb_data.text,'lxml')
    pageList = soup.select('div.result_btm_con.lodgeunitname')
    for i in pageList:
        listUrl.append(i.get('detailurl'))
    print(listUrl)
    #print('get_list_url Done')
    return listUrl

 # 获取整个页面的信息
def get_info_by_page(startPage, endPage, baseURL,database):
    for i in range(startPage,endPage+1):
        url = baseURL.format(i)
        print(i)
        print(url)
        listUrl = get_list_url(url)
        for j in listUrl:
            time.sleep(4)
            dataInfo = get_info(j)  # 获取每个页面的信息
            database.insert_one(dataInfo)  # 将信息插入到指定的页面中
    print('input to database Done')



client = pymongo.MongoClient('localhost',27017)  # 连接mongodb
xiaozhu = client['xiaozhu3']  # 创建一个名叫xiaozhu的库文件
home_info = xiaozhu['home_info'] # 创建一个home_info的页面
pageBaseUrl = 'http://bj.xiaozhu.com/search-duanzufang-p{}-0/'  # 构造共同url连接

# 调用函数抓取1,3页相关页面的具体数据:
get_info_by_page(1,1,pageBaseUrl,home_info)

for info in home_info.find({'price':{'$gte':500}}):
    print(info)

#统计mongodb有多少条记录

db = client.xiaozhu3
result = db.home_info.count()
#result1 = db.home_info.distinct('title').length
print('共计: %s 条数据' % result)
ll = len(db.home_info.distinct('title'))
print('去重后共计: %s 条数据' % ll)



'''
mongo
>help
> show dbs;
> use xiaozhu3
> show collections
home_info
> db.home_info.find({'price':{'$gte':2000}})
{ "_id" : ObjectId("57bd004effa6ae080ae10615"), "title" : "东单金宝街美术馆超赞四合院", "address" : "北京市东城区东四南大街演乐胡同\n                                  ", "img" : "http://image.xiaozhustatic1.com/00,800,533/6,0,72,184,1800,1200,cc913890.jpg", "hostName" : "王小山和他的朋友们", "hostPic" : "http://image.xiaozhustatic1.com/21/3,0,12,4011,278,278,178728c4.jpg", "price" : 2599, "hostGender" : "male" }
> db.home_info.count({'price':{'$gte':500}})
7
> db.home_info.count({'price':{'$gte':2000}})  #统计价格大于2000的有多少.
1
> db.home_info.count()   #共计72条记录
72
> db.home_info.distinct('title').length   #去重后统计数据
71
> db.home_info.count()
126

> db.home_info.find({'price':{'$gte':500}}).count()
38
> db.home_info.find().count()
222

'''