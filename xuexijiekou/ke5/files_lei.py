#coding:utf-8
#coding:utf-8
import requests
class SendFiles():
    def __init__(self,s):
        self.s = s
    def send_file(self):
        # 上传图片接口
        url = "http://127.0.0.1:82/zentao/file-ajaxUpload-5defa2d583131.html?dir=image"
        body_file = {
            "localUrl": (None, 'C:\fakepath\tt.jpg'),
            "imgFile": ("tt.jpg", open('E:\\img\\tt.jpg', 'rb'), 'image/jpeg')

        }
        r = self.s.post(url, files=body_file)
        try:
            res = r.json()
            return res
        except:
            print('json解析报错：%s'%r.text)
            return r.text

if __name__ == '__main__':
    from ke3.login import Login_zentao
    # 登录
    s = requests.session()
    res = Login_zentao(s, 'admin', '5b2440d1a879179957ed91dc1b55744c')
    file = SendFiles(s)
    f = file.send_file()
    print(f)
    assert f['error']==0


















