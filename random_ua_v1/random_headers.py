import random
def aheader(hd={}):
	'''
	# Function: 存储各种HTTP的headers信息，随机返回各自headers
	# Notes   : 1. 为了统一本机IP和headers的IP，这里加了个ip参数，由调用者统一过来。
				2. 参数hd代表标准headers字典格式，由使用处传进来。如Referer参数指定来源网址，
					那么在调用本函数时应该写：headers(hd={'Referer':'http://www.xxx.com'})这样的
					优先使用调用者的headers，如果没有指定则在这里定义默认的。
	'''
	# 来源浏览器
	agents = []
	agents.append('Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))') # IE
	agents.append('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36') # Chrome
	agents.append('Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25') # Safari Mobile
	agents.append('Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30') # Android Webkit Browser
	agents.append('Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25') # Safari Mobile
	# if not hd.has_key('User-Agent'): hd['User-Agent'] = agents[ random.randint(0,len(agents)-1) ]
	hd['User-Agent'] = agents[ random.randint(0,len(agents)-1) ]
	# 请求的多媒体类型
	# if not hd.has_key('Content-Type'): hd['Content-Type'] = 'application/x-www-form-urlencoded'
	# 来自链接
	# hd['Referer']      = '' # 暂时空白，由使用处定义
	# 优先使用的连接类型
	# if not hd.has_key('Connection'): hd['Connection'] = 'keep-alive'
	# 接受的回应内容类型
	# if not hd.has_key('Accept'): hd['Accept'] = 'text/html'
	# 接受的字符集
	# if not hd.has_key('Accept-Encoding'): hd['Accept-Encoding'] = 'utf-8'
	# 接受的编码方式列表
	# if not hd.has_key('Charset'): hd['Charset'] = 'gzip, deflate'
	# 之前由服务器通过Set-Cookie发送的一个Cookie
	# hd['Cookie'] = ''
	# print 'Using the HTTP-Headers with %s'%repr(hd) # 测试用
	return hd
def TEST_aheader():
	headers = aheader()
	print(headers)

TEST_aheader()