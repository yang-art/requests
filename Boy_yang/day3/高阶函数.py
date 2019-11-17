#高阶函数

# def add(a,b,f):
#     return f(a) +f(b)
# res = add(3,-6,abs)
# print(res)


# import time
# def bar():
#     time.sleep(2)
#     print('in the bar ')
#
# def test(fanc):
#     print(fanc)
#     return fanc
#
#  print(test(bar))
# bar = test(bar)
# bar()


#嵌套函数
x = 0
def grandpa():
    def dad():
        x = 2
        def son():
            x =3
            print(x)
        son()
    dad()
grandpa()


import  json
d = {'name':'yang','age':22}

print(type(d))
print(d)
j = json.dumps(d)   #字典转化为字符串
print(j)
print(json.loads(j)) #字符串转化为dict


