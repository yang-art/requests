#coding:utf-8
#__author__='易木'
import requests

url = 'http://japi.juhe.cn/qqevaluate/qq'
#参数
par = {
    'key':'8dbee1fcd8627fb6699bce7b986abc45',
    'qq':'3256814316'
}
#发送请求
r = requests.post(url,params = par)
print(r.text)

#requests 内容
print(r.request.url)
print(r.request.headers)

#response   内容

print(r.status_code)    #返回状态码
print(r.headers)   # 头部
print(r.text)   #打印文本返回结果
print(type(r.text))   #查看类型
print(r.json())    #json解析 成dict
print(r.encoding)
print(r.cookies)   #打印cookies 参数
