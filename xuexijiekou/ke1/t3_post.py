#coding:utf-8
#__author__='易木'

import requests
# 接口地址  垃圾分类查询数据接口
url = "http://apis.juhe.cn/rubbish/category"

par= {
    'key':'b3843e6c185969aa4dbdba27bf93c43e'

}

r = requests.post(url,params=par)
print(r.text)