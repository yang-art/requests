#coding:utf-8
import requests
import unittest
import warnings
from ke3.login import Login_zentao,login_success
class Test_login(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)   #忽略相关警告
        self.s = requests.session()
    def test_login01(self):
        '''登录成功用例：  正确账号 正确密码'''
        res = Login_zentao(self.s, "admin", '5b2440d1a879179957ed91dc1b55744c')
        login_result = login_success(res)
        print(login_result)  #True
        self.assertTrue(login_result)  #期望结果是True

    def test_login02(self):
        '''登录成功用例：  错误账号 正确密码'''
        res = Login_zentao(self.s, "admin11", '5b2440d1a879179957ed91dc1b55744c')
        login_result = login_success(res)
        print(login_result)   #False
        self.assertFalse(login_result)   #期望结果是False

if __name__=='__main__':
    unittest.main()






