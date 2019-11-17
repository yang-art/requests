#coding:utf-8

name = ['yang','Jeff','ZhangYang','Guyun']
#for i in name:  #for 循环
    #print(i)
'''name.append('jack') #新增一个用户
name.insert(2,'jack') #插入一个用户
name.insert(3,'Angel')
name[2] = '凯'        #修改用户名
#name.remove("凯")     #删除一个用户
del name [2] #删除一个用户
'''

print(len(name))
print(name)
#print(name[0],name[2])
print(name[1:3])   #切片
print(name[:3])  #取最前面三个值
print(name[3]) #取最后一个值
print(name[-1]) #取最后一个值
print(name[-2:])   #取最后两个值

print(name.index('Jeff'))   #使用 index索引查询用户所在位置



