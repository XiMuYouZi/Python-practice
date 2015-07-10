__author__ = 'Mia'
#coding=utf-8
import requests


session=requests.session()
url='http://www.zhihu.com/login/email'
#请求数据包里面的form data，也就是post到服务器上的数据，必须放到构造的post请求里面，可以看到这里面有用户名和密码
login_data={'_xsrf':'b6340d60298753b9bcb2eeef40cbd067',
            'email':'476301176@qq.com',
            'password':'ws1399593613210'
            }

#由于zhihu不检查header，所以在发送post请求的时候可以不带header参数
header={
'Accept-Language':'zh-CN,zh;q=0.8',''
'Cache-Control':'no-cache',
'Connection':'keep-alive',
'Content-Length':'105',
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
'CSP':'active',
'X-Requested-With':'XMLHttpRequest',
'Host':'www.zhihu.com',
'Origin':'http://www.zhihu.com',
'Pragma':'no-cache',
'Referer':'http://www.zhihu.com/',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36'
}

#构造post请求，带上url，post数据，header
r=session.post(url=url, data=login_data, headers=header)
#登录之后，再去抓取个人主页的内容，如果没有登录就去抓取个人主页，会被重定向到知乎的登陆界面
r1= session.get('http://www.zhihu.com/people/jing-xin-53')
print r1.text
