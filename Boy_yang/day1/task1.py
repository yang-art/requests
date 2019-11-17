#coding:utf-8

#作业1
_uesrname = 'yang'
_password = 'yangtong'
for i in range(3):
    name = input("请输入用户名：")
    password = input('输入密码:')
    if name == _uesrname and password == _password:
        print(name,"欢迎回来！")
        break
    else:
        print("\033[31;1m请重新输入：\033[0m")   #高亮显示提示
else:
    print("\033[41;1m用户账号信息输入三次错误，已被锁定！\033[0m")


