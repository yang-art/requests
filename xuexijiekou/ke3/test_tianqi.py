#coding:utf-8
#__author__='易木'
import requests
import unittest

class Tianqi(unittest.TestCase):  #历时天气查询接口用例

    @classmethod
    def setUpClass(cls):
        cls.url = 'http://v.juhe.cn/historyWeather/weather'
        cls.s = requests.session()

    def test_01(self):
        '''测试历史天气数据接口
           正确的城市id  日期,格式:2019-07-15，日期不能大于等于今日日期'''
        par = {
            'city_id': '26',
            'weather_date': '2019-11-02',
            'key': '9da5b0a8da65f33eebba98e3ca1c250d'
        }
        #发送请求
        r = self.s.get(self.url, params=par, verify=False)
        print(r.text)
        #获取结果
        res =r.json()["reason"]
        print("实际结果：%s"%res)
        #断言
        self.assertTrue(res=="查询成功")
    def test_02(self):
        '''城市city_id 为空时'''
        par = {
            'city_id':'',
            'weather_date': '2019-11-02',
            'key': '9da5b0a8da65f33eebba98e3ca1c250d'
        }
        # 发送请求
        r = self.s.get(self.url, params=par, verify=False)
        print(r.text)
        # 获取结果
        res = r.json()["reason"]
        print("实际结果：%s" % res)
        self.assertEqual(res,'城市ID格式错误')
    def test_03(self):
        '''当wearher_date 为空时 '''
        par = {
            'city_id': '26',
            'weather_date':'',
            'key': '9da5b0a8da65f33eebba98e3ca1c250d'
        }
        # 发送请求
        r = self.s.get(self.url, params=par, verify=False)
        print(r.text)
        # 获取结果
        res = r.json()["reason"]
        print("实际结果：%s" % res)
        self.assertEqual(res,'日期格式不正确')
    def test_04(self):
        '''当weather_date为空 city_id为空时   期望：城市ID格式错误'''
        par = {
            'city_id':'',
            'weather_date':'',
            'key': '9da5b0a8da65f33eebba98e3ca1c250d'
        }
        # 发送请求
        r = self.s.get(self.url, params=par, verify=False)
        print(r.text)
        res = r.json()['reason']
        print("实际结果：%s" % res)
        self.assertEqual(res, '城市ID格式错误')  #断言
    def test_05(self):
        '''当weather_date city_id正确，key错误时  期望：错误的请求KEY'''
        par = {
            'city_id': '26',
            'weather_date': '2019-11-01',
            'key': '9da5b0a8da65f33eebba98e3ca1'
        }
        # 发送请求
        r = self.s.get(self.url, params=par, verify=False)
        print(r.text)
        res = r.json()['reason']
        print("实际结果：%s" % res)
        self.assertEqual(res, '错误的请求KEY')  # 断言

    def test_06(self):
        '''key为空时  期望：错误的请求KEY'''
        par = {
            'city_id':'21',
            'weather_date':'2019-10-23',
            'key': ''
        }
        # 发送请求
        r = self.s.get(self.url, params=par, verify=False)
        print(r.text)
        res = r.json()['reason']
        print("实际结果：%s" % res)
        self.assertEqual(res, '错误的请求KEY')  # 断言

    def test_07(self):
        '''不传参数key'''
        par = {
            'city_id': '26',
            'weather_date': '2019-11-01'

        }
        # 发送请求
        r = self.s.get(self.url, params=par, verify=False)
        print(r.text)
        res = r.json()['reason']
        print("实际结果：%s" % res)
        self.assertEqual(res, '错误的请求KEY')  # 断言

    @classmethod  # 作用就是申明是个类方法
    def tearDownClass(cls):
        cls.s.close()


if __name__=='__main__':
    unittest.main()





