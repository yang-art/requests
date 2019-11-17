#coding:utf-8
#__author__='易木'
import requests
url = "https://www.baidu.com"
r = requests.get(url,verify = False)

print(r.text) #出现乱码时候  è§åé¦</a>&nbsp;äº¬ICP
print(r.content.decode('utf-8'))  #解码   content.decode(utf-8)



