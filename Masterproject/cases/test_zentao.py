#coding:utf-8
import requests
import unittest

s = requests.session()
class TestZentao(unittest.TestCase):
    def  setUp(self):
        '''数据准备  接口地址'''
        self.url = "http://127.0.0.1:82/zentao/user-login-L3plbnRhby9teS5odG1s.html"

    def test_01(self):
        '''禅道登录接口 错误账号  正确密码登录'''
        body = {
            'account':'admin',
            'password':'5b2440d1a879179957ed91dc1b55744c',
            'referer':'http://127.0.0.1:82/zentao/product/'

        }
        r =s.post(self.url,data = body,verify=False)
        reult = r.content.decode('utf-8')
        print('实际结果：%s'%reult)
        expect = 'parent.location'     #期望结果
        assert expect in reult

    def test_02(self):
        '''输入账号为空  正确密码登录'''
        body = {
            'account': '',
            'password': '5b2440d1a879179957ed91dc1b55744c',
            'referer': 'http://127.0.0.1:82/zentao/product/'

        }
        r = s.post(self.url, data=body, verify=False)
        reult = r.content.decode('utf-8')
        print('实际结果：%s' % reult)
        expect = 'parent.location'  # 期望结果
        assert expect in reult

    def test_03(self):
        '''输入正确账号 错误密码登录'''
        body = {
            'account': 'admin',
            'password': '5b2440d1a879179957ed91dc1b5574',
            'referer': 'http://127.0.0.1:82/zentao/product/'

        }
        r = s.post(self.url, data=body, verify=False)
        reult = r.content.decode('utf-8')
        print('实际结果：%s' % reult)
        expect = 'parent.location'  # 期望结果
        assert expect in reult

    def test_04(self):
        '''输入正确账号 密码为空登录'''
        body = {
            'account': 'admin',
            'password': '',
            'referer': 'http://127.0.0.1:82/zentao/product/'

        }
        r = s.post(self.url, data=body, verify=False)
        reult = r.content.decode('utf-8')
        print('实际结果：%s' % reult)
        expect = 'parent.location'  # 期望结果
        assert expect in reult

    def test_05(self):
        '''登录账号为空 密码为空'''
        body = {
            'account': '',
            'password': '',
            'referer': 'http://127.0.0.1:82/zentao/product/'

        }
        r = s.post(self.url, data=body, verify=False)
        reult = r.content.decode('utf-8')
        print('实际结果：%s' % reult)
        expect = 'parent.location'  # 期望结果
        assert expect in reult

if __name__== "__main__":
    unittest.main()






