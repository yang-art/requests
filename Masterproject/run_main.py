#coding:utf-8
from common.HTMLreport import HTMLTestRunner
import unittest
import os

#查找的目录
curpash =os.path.dirname(os.path.realpath(__file__))
print(curpash)

startdir = os.path.join(curpash,'cases')
print(startdir)

discover = unittest.defaultTestLoader.discover(startdir,
                                               pattern='test*.py')

print(discover)
reportpath = os.path.join(curpash,'report','result.html')
print(reportpath)

fp = open(reportpath,'wb')

#生成报告
runner = HTMLTestRunner(stream=fp,
                     title="接口测试报告",
                     description='自动化测试用例')
runner.run(discover)

fp.close()  #关闭




