#coding:utf-8
import requests
import unittest
from ke3.login import Login_zentao
from ke5.files_lei import SendFiles

class TestFile(unittest.TestCase):
    def setUp(self):           #前置
        self.s = requests.session()
        res = Login_zentao(self.s, 'admin', '5b2440d1a879179957ed91dc1b55744c')
        self.file = SendFiles(self.s)
    def test_file01(self):
        '''上传图片'''
        f = self.file.send_file()
        print(f)
        self.assertTrue(f['error']==0)

