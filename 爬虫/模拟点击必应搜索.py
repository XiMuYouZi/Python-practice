# -*- coding: utf-8 -*-
__docformat__ = 'restructuredtext en'

import time
import spynner
import pyquery
from bs4 import  BeautifulSoup
import  requests

'''
主要实现在必应上搜索关键字python，然后模拟点击，然后针对搜索结果做抓取
此代码只是得到了点击之后的url，如果需要对搜索结果进行筛选处理，可以使用和beautifulsoup处理静态网页类似的技术来处理
'''

br = spynner.Browser(
#    debug_level=4
)
br.load('http://cn.bing.com/')
br.create_webview()
br.show()

br.wk_fill('input[id=sb_form_q]', 'python')  #在搜索框中输入python
br.wk_click("input[id=sb_form_go]", wait_load=True, timeout=20)   #模拟点击搜索按钮
br.snapshot().save('example.png')   #保存点击之后的网页为图片
request=requests.get(url=br.url)
soup=BeautifulSoup( request.text)
print soup
