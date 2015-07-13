import  requests



session=requests.session()
url='http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)'

#登录新浪需要的header和提交的数据
header={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'no-cache',
'Connection':'keep-alive',
'Content-Length':'728',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':'UOR=www.baidu.com,blog.sina.com.cn,; U_TRS1=000000bf.25173b8d.556284b8.bdeeebe2; SINAGLOBAL=113.96.89.191_1432519864.670074; vjuids=e9d46641.14d88d6741a.0.bb62521a; SGUID=1432519866796_24941560; lxlrtst=1436166758_o; lxlrttp=1436166758; ULV=1436167227809:6:2:2:113.64.47.150_1436166916.435507:1436166915934; vjlast=1436166932.1436573787.11; SUB=_2AkMi_PdQdcNhrAFSnf0UzGPjZYxH-jjGiefBAH-8JXpBHRivJ2y4oMAqcEuNptv7rSxmpvLphA..; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9W5Ak3QNdbGsz9bGK566gI.c; Apache=113.96.89.204_1436760873.55131; ULOGIN_IMG=gz-b1c964594b8993d0a79856cd3ab5cb71de2a',
'Host':'login.sina.com.cn',
'Origin':'http://weibo.com',
'Pragma':'no-cache',
'Referer':'http://weibo.com/',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36',
'X-FirePHP-Version':'0.0.6'
}

form_data={
'entry':'weibo',
'gateway':'1',
'from':'',
'savestate':'7',
'useticket':'1',
'pagerefer':'https://www.google.com/',
'wsseretry':'servertime_error',
'pcid':'gz-b1c964594b8993d0a79856cd3ab5cb71de2a',
'door':'u6eqw',
'vsnf':'1',
'su':'d3M0NzYzMDExNzYlNDAxNjMuY29t',
'service':'miniblog',
'servertime':'1436761313',
'nonce':'607NT7',
'pwencode':'rsa2',
'rsakv':'1330428213',
'sp':'3229b601b2de07c5b8d07dace36f42b5e9f5b501a6c24d5661727fd5de595e6787232ea115656ee28b854630c041f545372ac2d08df6f8cbc427b1d050da49cd1d0bcfcfb52c9a0d7646c5352c3492d2d7193dc375044895f598556e7cd7652dc824aed39715cb6abea367601dc8915d2a247a478eefa8053e52706dbb6d6491',
'sr':'1440*900',
'encoding':'UTF-8',
'prelt':'79',
'url':'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
'returntype':'META'
}
post=session.post(url=url,data=form_data,headers=header)
print post


#登录微博主页的需要的header，从chrome中的network中抓包获取的
header2={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'no-cache',
'Connection':'keep-alive',
'Cookie':'SINAGLOBAL=7314977776259.184.1432630704813; login_sid_t=3c6ec2c239a65af8ae9cdc2b41dcb0b4; YF-Ugrow-G0=9642b0b34b4c0d569ed7a372f8823a8e; _s_tentry=www.google.com; Apache=7030131181236.356.1436760871679; ULV=1436760872653:15:7:1:7030131181236.356.1436760871679:1436579938007; UOR=www.csdn.net,widget.weibo.com,www.google.com; un=ws476301176@163.com; wvr=6; YF-V5-G0=8e216c747d9e492b2dcf025e8c7f492c; SUS=SID-2355108191-1436761704-GZ-h7r86-ababd38ad29e7a8813fae0561be19108; SUE=es%3Dab19f5e1bab9487d84e29b6d19589daa%26ev%3Dv1%26es2%3Daab5e169dbb3392374feb0e5a3402f64%26rs0%3DYhjSUfjuTE83%252Fp1yBKqci%252F1qTvwGPlR1YRo%252Bej1pyZv7FnZ84LpxNrf3sG5wnbxNoLVLWW4JjaUITwl3jbu6lOK65aLSBrili4fr5zGv0onlIE3f7aXIZYxFGNleBXnyaoLuCeK3BbCLMXCVO8YQi5h28d%252BdqTnQD9YU7smVk%252B0%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1436761704%26et%3D1436848104%26d%3Dc909%26i%3D9108%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D2%26st%3D0%26uid%3D2355108191%26name%3Dws476301176%2540163.com%26nick%3D%25E8%258E%25AB%25E6%2580%259D%25E5%25BD%2592%26fmp%3D%26lcp%3D2013-04-19%252007%253A55%253A25; SUB=_2A254p044DeTxGeRN7lcQ8CbNwj2IHXVb1TjwrDV8PUNbuNBeLW-nkW9B1UMSqZycNMT5gvNxqyJnt2Rw6w..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5Ak3QNdbGsz9bGK566gI.c5JpX5K2t; SUHB=05iLf--UM1-tNN; ALF=1468297704; SSOLoginState=1436761704; YF-Page-G0=b35da6f93109faa87e8c89e98abf1260',
'Host':'weibo.com',
'Pragma':'no-cache',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36',
'X-FirePHP-Version':'0.0.6'
}

#打开微博的主页，只能登录之后才可以打开，需要添加header
s=session.get('http://weibo.com/u/2355108191/home?wvr=5&lf=reg',headers=header2)
print s.text