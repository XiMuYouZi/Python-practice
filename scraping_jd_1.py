#coding=utf-8
import spynner
import pyquery
import time
from bs4 import BeautifulSoup

#sdsd
url1='http://list.jd.com/list.html?cat=670%2C671%2C672&page='+'%d&JL=6_0_0'%i
browser = spynner.Browser()
browser.create_webview()
browser.set_html_parser(pyquery.PyQuery)
browser.load(url1, 10)

try:
    browser.wait_load(10)
except:
    pass

string = browser.html
browser.close()

soup = BeautifulSoup(string)
time.sleep(2)

soup1=soup.select('.j-sku-item')
for item in soup1:
    print u'价格：'+item.select('strong')[0].text, '||', u'型号：'+ item.select('em')[1].text, '||', u'商品链接：'+item.a['href'], '||', u'评论数：'+item.select('a')[2].text

