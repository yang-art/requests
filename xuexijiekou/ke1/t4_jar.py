#coding:utf-8
#__author__='易木'

import requests

url = "https://www.chsi.com.cn"

h = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Upgrade-Insecure-Requests':'1'

}

r = requests.get(url,headers=h,verify = False)

#RequestsCookieJar 格式的cookies
coks = r.cookies
print(coks)
print(dict(coks))  #转换成字典格式
#jar的格式
r2 =requests.get(url,headers=h,cookies=coks,verify=False)
print(r2)