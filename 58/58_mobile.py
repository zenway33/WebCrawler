from bs4 import BeautifulSoup
import requests
import time
import sys


headers = {
       'User-Agent': 'Mozilla/5.8 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'
}

'''
# 获取首页手机号信息
def get_link(url):

    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'lxml')

    carriers  = soup.select('a.t > span')
    # carriers = soup.xpath("//a[1]/span[1]")
    numbers = soup.select('a.t > strong')
    #print(carriers)
    list_a = [j for i, j in enumerate(carriers) if not i%2]
    print(list_a)

    for i in list_a:
        print(i.get_text().strip())

#[j for i , j in enumerate(['a', 'b','c']) if not i%2]

get_link('http://bj.58.com/shoujihao/pn2')

'''

# mobile_url 获取
def get_image(page_start,page_stop):

    try:
            page_start = int(page_start)
            page_stop = int(page_stop)
            if page_start < 0 or page_stop < 0 or page_stop < page_start:
                    raise ValueError("Usage: python xx.py page_start page_stop")
    except:
            raise ValueError

    for page_num in range(page_start,page_stop):

            #headers = random_header()

            wb_data =requests.get('http://bj.58.com/shoujihao/pn{}'.format(page_num), headers=headers)
            #time.sleep(5)
            soup = BeautifulSoup(wb_data.text,'lxml')
            #titles  = soup.select('strong.number ')
            carriers  = soup.select('a.t > span')
            numbers  = soup.select('a.t > strong')
            print(page_num)

            #定义列表,获取奇数列
            def carrier_list():
                carrier_list = []
                list_a = [j for i, j in enumerate(carriers) if not i%2]
                for i in list_a:
                    carrier_list.append(i)
                return carrier_list

            carriers = carrier_list()

            #print(carriers)

            try:
               for carrier,number in zip(carriers,numbers):
                   data = {
                       'carrier' : carrier.get_text().strip(),
                       'number' : number.get_text()
                   }
                   print(data)
            except:
                pass

if __name__ == "__main__":
    start_time = time.time()
    if len(sys.argv) < 2:
        print("Usage: python {0} <page_start> <page_stop>\n   example: python {0} 1 10".format(sys.argv[0]))
    else:
        get_image(sys.argv[1], sys.argv[2])
    #get_image_info()
    print("--- %s seconds ---" % (time.time() - start_time))



'''
目标: http://bj.58.com/shoujihao/  抓取手机号
分页: http://bj.58.com/shoujihao/pn1 ~ N
难点: <span>移动</span>, <span class="date">1小时</span> 处理取运营商
思路: 获取奇数列表,再对奇数列表进行处理.
'''

'''
#结果
{'number': '13901365238', 'carrier': '移动'}
{'number': '13901192888', 'carrier': '移动'}
{'number': '13901032789', 'carrier': '移动'}
{'number': '13901160777', 'carrier': '移动'}
{'number': '13901055558', 'carrier': '移动'}
'''