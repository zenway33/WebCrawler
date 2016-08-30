#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get('https://www.jianshu.com/')
elem = driver.find_element_by_id('q')
elem.send_keys(u'爬虫')
elem.send_keys(Keys.RETURN)
print(driver.page_source)