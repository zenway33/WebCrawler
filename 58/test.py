import requests
from lxml import html

'''
page=requests.get('http://bj.58.com/shoujihao/pn2')
tree=html.fromstring(page.text)
empty=tree.xpath('//*[@id="infolist"]/div/ul/div[1]/ul/li[2]/a[1]/span[1]')
print(empty)
'''
#//*[@id="infolist"]/div/ul/div[1]/ul/li[2]/a[1]/span[1]

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = lxml(page.text)

t = tree.xpath('//div/ul/div[1]/ul/li[2]/a[1]/span[1]')
print(t)

