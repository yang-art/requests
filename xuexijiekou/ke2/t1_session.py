#coding:utf-8
#__author__='易木'

import requests
s = requests.session()   #无界面的微型浏览器

#不走登录流程登录禅道
c = requests.cookies.RequestsCookieJar()
c.set('zp','e68fc195fc97fc8878f96a604d2ec40cbce72d20')
c.set('zentaosid','kiic4n50tpog3fnqd04poh86k5')   #传cookies参数

s.cookies.update(c)  #更新cookies
print(s.cookies)

url = 'http://127.0.0.1:82/zentao/bug-browse-1.html'
r = s.get(url)
print(r.content.decode('utf-8'))