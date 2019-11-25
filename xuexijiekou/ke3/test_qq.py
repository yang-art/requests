#coding:utf-8
import requests
import unittest

class TestQQ(unittest.TestCase):

    def setUp(self):
        '''数据准备  公共部分'''
        self.url = 'http://japi.juhe.cn/qqevaluate/qq'

    def test_01(self):
        '''测试QQ接口：key是错误的，qq是正确的  期望是："KEY ERROR!"'''
        # 参数
        par = {
            'key': '8dbee1fcd8627fb6699bce7b986abc45',
            'qq': '3256814316'
        }
        # 发送请求
        r = requests.post(self.url, params=par)
        print(r.text)
        # 获取结果
        res = r.json()["reason"]
        print('实际结果：%s' % res)
        #assert res == "KEY ERROR!"
        self.assertTrue(res=="KEY ERROR!")  #断言
        self.assertEqual(res,"KEY ERROR!")
    def test_02(self):
        '''key为空，QQ正确'''
        # 参数
        par = {
            'key': '',
            'qq': '3256814316'
        }
        # 发送请求
        r = requests.post(self.url, params=par)
        print(r.text)
        # 获取结果
        res = r.json()["reason"]
        print('实际结果：%s' % res)
        # assert res == "KEY ERROR!"
        self.assertTrue(res == "KEY ERROR!")  # 断言
        self.assertEqual(res, "KEY ERROR!")
    def test_03(self):
        '''key是错误的  QQ号为空'''

        # 参数
        par = {
            'key': '8dbee1fcd8627fb6699bce7b986abc45',
            'qq': ''
        }
        # 发送请求
        r = requests.post(self.url, params=par)
        print(r.text)
        # 获取结果
        res = r.json()["reason"]
        print('实际结果：%s' % res)
        # assert res == "KEY ERROR!"
        self.assertTrue(res == "KEY ERROR!")  # 断言
        self.assertEqual(res, "KEY ERROR!")
    def test_04(self):
        '''key为空 QQ号为空'''

        # 参数
        par = {
            'key': '',
            'qq': ''
        }
        # 发送请求
        r = requests.post(self.url, params=par)
        print(r.text)
        # 获取结果
        res = r.json()["reason"]
        print('实际结果：%s' % res)
        # assert res == "KEY ERROR!"
        self.assertTrue(res == "KEY ERROR!")  # 断言
        self.assertEqual(res, "KEY ERROR!")

    def tearDown(self):      #数据清理 tearDown

        print('清理数据')

if __name__ =="__main__":
    unittest.main()

