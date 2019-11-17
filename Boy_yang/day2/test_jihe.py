# coding:utf-8
list_1 = [1,4,5,7,3,6,7,9]
list_1 = set(list_1)  #将 list_1 变成集合
print(list_1,type(list_1))  #打印数据类型

list_2 = set([2,6,0,66,22,8,4])
print(list_1,list_2)

#交集 相同字符
print(list_1.intersection(list_2))
print(list_1 & list_2)

#并集 去掉重复字符 合并
print(list_1.union(list_2))
print(list_1 | list_2)

#差集 in list_1 but not list_2
print(list_1.difference(list_2))
print(list_1 - list_2)

#子集
print(list_1.issubset(list_2))

#对称差集
print(list_1.symmetric_difference(list_2))
print('--------------------')


