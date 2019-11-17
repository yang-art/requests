a = [1,2,3,4,5,6,]
b = a[:]
print(b)

b = a[0:-1:1]
print(b)

c = a[:3]  #取最前面三个值
print(c)

d = a[0:5:3]  #从第一个位置到第6个位置，每三个取一个值
print(d)

#反向取值
d = a[5:0:-1]
print(d)

d1 = a[::-1]
print(d1)
