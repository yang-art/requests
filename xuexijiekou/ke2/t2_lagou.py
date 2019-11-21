#coding:utf-8

import requests
import re    #导致正则包
s = requests.session()
url = 'https://passport.lagou.com/login/login.html?utm_source=m_cf_cpt_baidu_pcbt'

h = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'

}
s.headers.update(h)   #更新头部信息
r = s.get(url,verify=False)

#获取  window.X_Anti_Forge_Token = 'ba06d0fe-eab3-4fc9-9377-48a4cb5517f8';
 # window.X_Anti_Forge_Code = '80620998';

X_Anti_Forge_Token = re.findall("window.X_Anti_Forge_Token = '(.+?)'",r.content.decode('utf-8')) #用正则去获取动态参数
print(X_Anti_Forge_Token[0])

X_Anti_Forge_Code = re.findall("window.X_Anti_Forge_Code = '(.+?)'",r.content.decode('utf-8'))
print(X_Anti_Forge_Code[0])


h2 = {
    'X-Requested-With':'XMLHttpRequest',
    'X-Anit-Forge-Token':'X_Anti_Forge_Token[0]',
    'X-Anit-Forge-Code':'X_Anti_Forge_Code[0]'
}
s.headers.update(h2)

url_login = 'https://passport.lagou.com/login/login.json'
body = {
    'isValidate':'true',
    'username':'18130658789',
    'password':'990eb670f81e82f546cfaaae1587279a',
    'request_form_verifyCode':'',
    'submit':'',
    'challenge':'11d7d0bb1edf3f316b536ed0d55d7b1b'

}

r2 = s.post(url_login,data=body,verify=False)
print(r2.text)
