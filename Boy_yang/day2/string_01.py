#coding:utf-8

name = "my name is {name} and i am {year} old"
print(name.capitalize())  #首字母大写
print(name.count('f'))  #统计字符串相同的
print(name.center(50,'-'))  #打印50个字符，用户名放中间，不够的用'-'补上
print(name.endswith('ff'))  #判断字符串以什么结尾
#print(name.expandtabs(tabsize=40))
print(name.find('name'))
print(name[name.find('name'):7]) #字符串切片、
print(name.format(name = 'make',year = 23))
print(name.format_map({'name':'make','year':'23'}))
print(name.isalnum())
print(','.join(['1','2','3']))
print(name.ljust(50,'*'))
print(name.rjust(50,'-'))

print('LI wang'.swapcase())  #大小写转换
print('mr li'.title())    #变成 title  大写
print('mr li'.zfill(50))


