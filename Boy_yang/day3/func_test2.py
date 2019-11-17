#-*- coding:utf-8 -*-


'''def test(x,y,z = 6):
    print(x)
    print(y)
    print(z)

test(1,y = 6)
'''''
# 参数组  用于形参不固定 转换成元组的形式
'''def test (*args):
    print(args)
test(1,2,5,6)
test(*[1,5,4,8,6]) #args = tuple([1,5,4,8,6])
'''

def test1(x,*args):
    print(x)
    print(args)
if __name__ =="__main__" :
   test1(1,5,4,8,6)

# **kwargs:把n个 关键字参数转换成dict的点的方式

def test2(**kwargs):
    print(kwargs)
test2(name = 'make',age = 18, sex = 'f')
