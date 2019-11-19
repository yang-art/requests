#coding:utf-8
#__author__='易木'
import requests
#百度URL
url = "https://www.baidu.com"
r = requests.get(url,verify = False) #发送请求

print(r.text) #出现乱码时候  è§åé¦</a>&nbsp;äº¬ICP
print(r.content.decode('utf-8'))  #解码   content.decode(utf-8)



