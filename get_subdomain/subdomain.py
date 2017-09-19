#!/usr/bin/env python
# coding=utf-8
import re
import requests
from pprint import pprint
import time

def crawl_page(domain):

	global check_domain
	checked_domain = set()
	while True:
		time.sleep(1)
		for url in list(check_domain):
			if url in checked_domain:continue
			checked_domain.add(url)
			print('[*] Crawl URL: {0}'.format(url))
			try:
				req = requests.get('http://%s' % url, timeout=30)
				content = req.text
				link_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", content)
				for url in link_list:
					result = re.findall(r'http://(.*?)\.37\.com', url)
					if len(result) > 0:
						check_domain.add('{0}.{1}'.format(result[0], domain))
			except:
				pass
		if len(set(check_domain)) == len(set(checked_domain)):break
	return check_domain

if __name__ == '__main__':
	main_domain = '37.com'
	check_domain = set(['www.37.com'])
	crawl_page(main_domain)
	print "all domain from %s list bellow" % main_domain
	for url in check_domain:
		print url
		with open('domain.txt', 'a') as f:
			f.write(url + '\n')
