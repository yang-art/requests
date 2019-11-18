#coding:utf-8
#__author__='易木'
import requests
import urllib3
urllib3.disable_warnings()

#博客园URL
url = "https://zzk.cnblogs.com/s/blogpost"
#传头部headers
h = {
    'cookie':'SBNoRobotCookie=CfDJ8DeHXSeUWr9KtnvAGu7_dX9zx07ZT75yW7i5OgW015LfwiF671iL8cB918l'
             '_WnQJ6B3NHb9B-odSCWwNaOHR66wDF6x_-diO0zp76h91qppsaTHt07pVCGBM7uBVR6t_vw'

}
par = {
    'w':'yy'
}
#verify = False   不校验ssl证书问题
#发送博客园接口地址
r1 = requests.get(url,params=par,verify=False,headers = h)
print(r1.text)
