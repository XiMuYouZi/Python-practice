__author__ = 'Mia'
#coding=utf-8
import requests


session=requests.session()
url='http://www.zhihu.com/login/email'
#请求数据包里面的form data，也就是post到服务器上的数据，必须放到构造的post请求里面，可以看到这里面有用户名和密码
login_data={
            'email':'476333301176@qq.com',
            'password':'ws1www3995210'
            }

#构造用于获取登录后主页的http header，由于知乎主页是在用户登陆之后才会呈现出来，所以要用到用户的登录信息，可以使用header里面报考的referer和cookie来实现
header1={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'no-cache',
'Connection':'keep-alive',
'Cookie':'_za=49d55e41-86e7-47da-92c6-db404977ef3d; q_c1=89e8965393ff48359eb75be547d2f7e2|1435187586000|1432183091000; _xsrf=b6340d60298753b9bcb2eeef40cbd067; cap_id="MjBlNTJiNDA0Y2U3NDQwNGI0Mjg0OTg0OWMzOTk5ZWY=|1436483096|16e6951722b8c9df2775ef641c1ad0441dad3998"; z_c0="QUFDQW83WWFBQUFYQUFBQVlRSlZUYXJYeDFYTHJsaUl2MmhRQkhEaXRxdzBOTGt2UTVCcjJnPT0=|1436568234|ba17553c078a7210e57f6bf1dcd6f2c7c588ae7c"; _ga=GA1.2.2047737073.1432177279; __utma=51854390.2047737073.1432177279.1436519851.1436567754.4; __utmb=51854390.66.9.1436570461022; __utmc=51854390; __utmz=51854390.1436567754.4.3.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/32043825/answer/54425757; __utmv=51854390.100-1|2=registration_date=20130405=1^3=entry_date=20130405=1',
'Host':'www.zhihu.com',
'Pragma':'no-cache',
'Referer':'http://www.zhihu.com/people/jing-xin-53',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36',
'X-FirePHP-Version':'0.0.6'
}


#构造用于抓取在知乎关注的人的页面的http  header，这个必须要，因为这个页面是从登录成功页面跳转进来的，所以要用到header里面的cookie和refer，
header2={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'no-cache',
'Connection':'keep-alive',
'Cookie':'_za=49d55e41-86e7-47da-92c6-db404977ef3d; q_c1=89e8965393ff48359eb75be547d2f7e2|1435187586000|1432183091000; _xsrf=b6340d60298753b9bcb2eeef40cbd067; cap_id="MjBlNTJiNDA0Y2U3NDQwNGI0Mjg0OTg0OWMzOTk5ZWY=|1436483096|16e6951722b8c9df2775ef641c1ad0441dad3998"; z_c0="QUFDQW83WWFBQUFYQUFBQVlRSlZUYXJYeDFYTHJsaUl2MmhRQkhEaXRxdzBOTGt2UTVCcjJnPT0=|1436568234|ba17553c078a7210e57f6bf1dcd6f2c7c588ae7c"; unlock_ticket="QUFDQW83WWFBQUFYQUFBQVlRSlZUYkpSb0ZVOFFhOGcwcWFqTkdrb1c5Tnd6LUU5ZVRYZXpnPT0=|1436568234|ff02f33013230dd69f62a8a0df26d6513bca1745"; _ga=GA1.2.2047737073.1432177279; _gat=1; __utmt=1; __utma=51854390.2047737073.1432177279.1436519851.1436567754.4; __utmb=51854390.51.8.1436568889084; __utmc=51854390; __utmz=51854390.1436567754.4.3.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/32043825/answer/54425757; __utmv=51854390.100-1|2=registration_date=20130405=1^3=entry_date=20130405=1',
'Host':'www.zhihu.com',
'Pragma':'no-cache',
'Referer':'http://www.zhihu.com/people/jing-xin-53/followers',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36',
'X-FirePHP-Version':'0.0.6'
}
#构造post请求，带上url，post数据，header
r=session.post(url=url, data=login_data)

#登录之后，再去抓取个人主页的内容，如果没有登录就去抓取个人主页，会被重定向到知乎的登陆界面
r1=session.get('http://www.zhihu.com/people/jing-xin-53')
print r1.text

#登录之后，再去抓取关注的人页面的内容，如果没有登录就去抓取关注，会被重定向到知乎的登陆界面，注意一定要带上header。不然就会被重定向到未登陆的主页
r2= session.get('http://www.zhihu.com/people/jing-xin-53/followees',headers=header2)
print r2.text

#登录之后，再去抓取知乎主页的内容，如果没有登录就去抓取关注，会被重定向到知乎的登陆界面，注意一定要带上header。不然就会被重定向到未登陆的主页
r3= session.get('http://www.zhihu.com',headers=header1)
print r3.text

