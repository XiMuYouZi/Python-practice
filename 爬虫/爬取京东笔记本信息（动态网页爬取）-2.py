
#coding=utf-8
import spynner
import pyquery
from bs4 import  BeautifulSoup

'''
这个方法比较成熟稳定，可以快速自动的抓取多个网页，不会崩溃和出现timeout的情况，建议把timeout时间设置到5
'''
jd_goods_info=open('jd_goods.txt','a+')

#抓取淘宝笔记本分类前十页的信息
i=0
while i<10:
 i+=1
 url1='http://list.jd.com/list.html?cat=670%2C671%2C672&page='+'%d&JL=6_0_0'%i #使用%d参数来改变网页的url从1-10页面
 browser = spynner.Browser(debug_level=spynner.DEBUG)
 browser.create_webview()
 browser.set_html_parser(pyquery.PyQuery)
 browser.load(url1)
 browser.wait(5)

 browser.soup.make_links_absolute(base_url=browser.url)
 taobao_html=browser.soup('html').html() #因为html元素是整个网页的开头和结尾，所以使用html元素把整个网页全部保存下来
 soup=BeautifulSoup(taobao_html)

 soup1=soup.select('.j-sku-item')
 for item in soup1:
  #因为一次打印出所有信息出来的结果是tuple，无法转换编码，而分次打印出来信息然后合并出来的是unicode编码，最转换到str类型保存到文件
    price= u'价格：'+item.select('strong')[0].text+'   '
    modle=u'型号：'+ item.select('em')[1].text+'   '
    goods_link=u'商品链接：'+item.a['href']+'   '
    # browser.download(item.a['href'])
    comments=u'评论数：'+item.select('a')[2].text
    jd_goods= price+modle+goods_link+comments
  # 循环分行写入笔记本的电脑信息
    for jd_good  in jd_goods:
       jd_goods_info.write(jd_goods.encode('utf-8'))
       jd_goods_info.write('\n')
       break

jd_goods_info.close()






