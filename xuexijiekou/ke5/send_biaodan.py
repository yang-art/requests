#coding:utf-8
import requests
from ke3.login import Login_zentao

#登录
s = requests.session()
res = Login_zentao(s,'admin','5b2440d1a879179957ed91dc1b55744c')

#上传表单
URL = "http://127.0.0.1:82/zentao/bug-create-1-0-moduleID=0.html"
body_file = {
    'product':1,
    "module":0,
    'project':'',
    "openedBuild[]":'trunk',
    "assignedTo":'admin',
    "deadline":'',
    'type':'codeerror',
    'os':'',
    "browser":'',
    "color":'',
    'title':'新增一个Bug',
    "severity":3,
    'pri':0,
    'steps':'<p><img src="file-read-5.jpg" alt="" />[步骤]</p><p>[结果]Bug11111</p><p>[期望]期望值2222</p>',
    'story':0,
    'task':0,
    "mailto[]":'',
    "keywords":'',
    'files[]':'',
    "labels[]":'',
    'uid':'5defa2d583131',
    'case':0,
    "caseVersion":0,
    'result':0,
    "testtask":0

}
r = s.post(URL,data=body_file)
print(r.text)