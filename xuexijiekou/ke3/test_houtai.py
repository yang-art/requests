#coding:utf-8
import requests
import unittest
import warnings
from ke3.login import Login_zentao,houtai
class Test_Houtai(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)   #忽略相关警告
        self.s = requests.session()

    def test_houtai01(self):
        '''登录'''
        Login_zentao(self.s,"admin",'5b2440d1a879179957ed91dc1b55744c')
        '''访问后台'''
        result= houtai(self.s)
        print("访问后台结果：%s"%result)
        self.assertTrue(result)
if __name__=="__main__":
    unittest.main()


