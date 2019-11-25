#coding:utf-8

import requests
s = requests.session()

#抓包登录cookeis

c = requests.cookies.RequestsCookieJar()
c.set('.CNBlogsCookie','3BD5B157AEAEFE17355B15390BE4E4150B49CE75EDBCA6DAFB52C1BAFDB4389BE0E21142A4EAAA9FF0E6BD25E5695EEFFB2599EAE2624377CBB3FF8231F5B32140271550AD32CCFBD0D9F508C62C0935B25BFF5A')
s.cookies.update(c)  #更新cookies

#验证是否登录成功
r = s.get("https://www.cnblogs.com/y325681/p/11561979.html",verify = False)
result = (r.text) #实际结果
print(result)
expect = 'while、for - 井底的鱼 - 博客园'

assert expect in result   #断言

