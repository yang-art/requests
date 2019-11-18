#coding:utf-8
#__author__='易木'

import requests

url = "http://127.0.0.1:82/zentao/user-login-L3plbnRhby9teS5odG1s.html"
body = {
    'account':'admin',
    'password':'5b2440d1a879179957ed91dc1b55744c',
    'referer':'/zentao/my.html'
}
#抓包查看头部 Content-Type
# --application/json--------这种是传json参数
#--application/x-www-form-unlencode--------这种传 data参数
r = requests.post(url,data=body)
result = r.content.decode('utf-8')  #实际结果
print('实际结果：%s'%result)
expect = "parent.location"  #期望结果

#判断标准，（期望结果）
assert expect in result
