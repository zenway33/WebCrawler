find_all 相关实例

soup.find_all("a")
soup.find("a")
soup.a.get("href")
soup.a.string
soup.p.find_all("a")
soup.find_all("a", class_="link", href="/link")
soup.find_all("a", attrs={"class": "link", "href": "/link"})
soup.find_all(class_="link", href="/link")
soup.find_all(attrs={"class": "link", "href": "/link"})
soup.find_all('ul', class_='clearfix')

#
soup.find_all("table", attrs={"width": "100%"})
bookstar = subsoup.find('span',attrs={"class": "rating_nums"}).string # 图书星级：9.0
bookcommentnum = subsoup.find('span',attrs={"class": "pl"}).string.strip('\r\n ()人评价') # 评价人数：190325

# 正则相关
import re
soup.find_all(re.compile("^b"))
soup.find_all(href=re.compile("link"))
soup.find_all("a", text=re.compile("hello"))

# Beautiful Soup CSS selector
from pprint import pprint
from bs4 import BeautifulSoup

html_content = open('bs_sample3.html')
# http://dl.dropbox.com/u/49962071/blog/python/resource/bs_sample3.html
soup = BeautifulSoup(html_content) # making soap

pprint(soup.select("title")) # get title tag
pprint(soup.select("body a")) # all a tag inside body
pprint(soup.select("html head title")) # html->head->title
pprint(soup.select("head > title")) # head->title
pprint(soup.select("p > a")) # all a tag that inside p
pprint(soup.select("body > a")) # all a tag inside body
pprint(soup.select(".sister")) # select by class
pprint(soup.select("#link1")) # select by id
pprint(soup.select('a[href="http://example.com/elsie"]'))
# find tags by attribute value
pprint(soup.select('a[href^="http://example.com/"]'))
# find tags by attribute value, all contains 'http://example.com/'
pprint(soup.select('p[lang|=en]')) # Match language codes


# css
soup.select("#link1")
soup.select('a[href^="http://"]')
soup.prettify()

#
titles = soup.select('div.property_title > a[target="_blank"]')
imgs = soup.select('img[width="160"]')
cates = soup.select('div.p13n_reasoning_v2  ')

for title,img,cate in zip(titles,imgs,cates):
    data = {
        'title': title.get_text(),
        'img': img.get('src'),
        'cate': list(cate.stripped_strings)
        }
    print(data)

# 获取数字的函数
def trans2numbers(string):
    return int(''.join(a for a in string.strip() if a.isdigit()))

def get_numbers(read):
    result = []
    for i in read:
        result.append(trans2numbers(i.string))
    return result


#取列表的奇数位:
[j for i , j in enumerate(['a', 'b','c']) if not i%2]

#定义列表,获取奇数列
def carrier_list():
    carrier_list = []
    list_a = [j for i, j in enumerate(carriers) if not i%2]
    for i in list_a:
        carrier_list.append(i)
    return carrier_list

carriers = carrier_list()

# 编辑器快捷键
https://www.zhihu.com/question/38946886
右移,选中代码块，按Tab。
要是想往左移，就按Shift + Tab

#数据分析工具
1. 在线分词工具：基于深度学习的中文在线抽词-PullWord (梁斌penny)
2. 在线词云生成工具：TAGUL - WORD CLOUD ART
3. 图表：ECharts
4. 数据爬取：Python Scrapy开发程序

# sys cli argv
if len(sys.argv) < 2:
    print("Usage: python {0} <page_start> <page_stop>\n   example: python {0} 1 10".format(sys.argv[0]))
else:
    get_image(sys.argv[1], sys.argv[2])

# 创建目录
path = os.getcwd()
path = os.path.join(path,'baozou2016')
if not os.path.exists(path):
    os.mkdir(path)

# 定义下载图片函数
# download function url,filename
def download(img_url,file_name):
    r = requests.get(img_url, stream = True,headers=headers)
    # print(r.status_code)
    #print(file_name
    with open(path + '/' + file_name, "wb") as fs:
        fs.write(r.content)
    print("%s => %s" % (img_url, file_name))

# 利用zip将数据装入字典
for title,img in zip(titles,imgs):
    data = {
        'title' :title.get_text(),
        'img_url' :img.get('data-original-image-url')
    }


# 获取pdf url,返回列表
def get_pdf_urls(web_url):
    wb_data = requests.get(web_url,headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    pdfs = soup.select('area[href^="http://"]')

    pdf_urls=[]
    for pdf_url in pdfs:
        pdf = pdf_url.get('href').strip('#')
        pdf_urls.append(pdf)
    return pdf_urls

urls = get_pdf_urls(web_url)


'''
定义下载列表页函数
'''
def get_page_within(pages):
    for page_num in  range(1,pages+1):
        wb_data = requests.get('http://baozoumanhua.com/catalogs/gif?page={}'.format(page_num))
        ....

get_page_within(3)



#main
if __name__ == '__main__':
    start()

#获取列表页,format范例
urls = ['http://www.guazi.com/tj/buy/o{}/'.format(str(i)) for i in range(1, 30, 1)]
