#-*- coding:utf-8 -*-
def test(x,y):
    print(x)
    print(y)

test(1,2)  #位置参数与形参一一对应

test(y = 3,x = 1) #关键字参数与形参顺序无关

#默认参数
def test1(x,y=3):
    print(x)
    print(y)
#test1(4)
test1(4,6)
# 默认参数特点：调用函数的时候，默认参数非必须传递





