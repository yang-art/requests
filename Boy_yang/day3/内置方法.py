#coding:utf-8
#__author__='易木'

# print(all([0,5,6]))
# print(any([0,5,3]))  #一个为真就  True
# print(ascii([0,5,'中文']))
#
# print(bool(5))

a = bytes('abcde',encoding='utf-8')
print(a.capitalize(),a)


#把数字十进制转化二进制
a = bin(25)
b = bin(100)
print(a,b)


#将两个变量值对应拼接在一起   用内置行数  zip()
a  = [1,2,3,4,6,7]
j = ['a','b','c','d']
for i in zip(a,j):
    print(i)


a
