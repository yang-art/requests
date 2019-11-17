#-*-coding:utf-8-*-

age = 18  #全局变量
def change_name(name):
    global age  #申明下修改全局变量
    age = 20
    print('before change',name)
    name = "Jeff"  #这个函数就是这个变量的作用域
    print('after change',name)


name = 'jeff'
change_name(name)
print(name)
print(age)



