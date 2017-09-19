import requests
import re

content =  requests.get('http://www.jinse.com/').text
messages = re.findall(r'data-topic-id.*?\<a\ href=\"(\S+)\"\ target=\"_blank"\ title=\"(\S+)\"\>.*?\<li\ class=\"left\"\>(\S+)\<\/li\>', content, flags=re.DOTALL)
for message in messages:
	if re.findall(r'\d', message[2]):
		print("title: %s url:%s time: %s" % (message[1], message[0], message[2]))