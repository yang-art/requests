#coding:utf-8
import requests
from ke3.login import Login_zentao

#登录
s = requests.session()
res = Login_zentao(s,'admin','5b2440d1a879179957ed91dc1b55744c')

#上传图片接口
url = "http://127.0.0.1:82/zentao/file-ajaxUpload-5defa2d583131.html?dir=image"
body_file= {
    "localUrl":(None,'C:\fakepath\tt.jpg'),
    "imgFile": ("tt.jpg",open('E:\\img\\tt.jpg','rb'),'image/jpeg')


}
r = s.post(url,files=body_file)
print(r.json())
assert r.json()['error']==0

# print(r.status_code)
# print(r.cookies)
# print(r.headers)
