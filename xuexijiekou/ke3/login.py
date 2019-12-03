#coding:utf-8
import requests
def Login_zentao(s,user,psw):
    # s = requests.session()
    url = 'http://127.0.0.1:82/zentao/user-login-L3plbnRhby9teS5odG1s.html'

    body = {
        'account': user,
        'password': psw,
        'referer': '/zentao/my.html'
    }
    r = s.post(url,data=body)
    # print(r.text)
    return r.content.decode("utf-8")

def login_success(result):
    '''判断是否登录成功，成功返回 True,失败返回  False'''
    if "parent.location" in result:
       return True
    else:
        return False

def houtai(s):
    r1 = s.get('http://127.0.0.1:82/zentao/admin/')
    b = r1.content.decode('utf-8')
    # print(b)
    if '当前系统的版本是9.3.beta' in b:
        print('访问成功！')
        return  True
    else:
        print('访问失败！')
        return False

if __name__=="__main__":
    '''该代码是调试函数功能用的'''
    s = requests.session()
    res=Login_zentao(s,"admin",'5b2440d1a879179957ed91dc1b55744c')
    login_result = login_success(res)
    print(login_result)
    c = houtai(s)
    print(c)








