#coding:utf-8

#文件写入
#f = open('yesterday','a',encoding = 'utf-8') # append 追加
'''f.write('青春是梦，\n')
f.write('一晃二十多年 \n')
f.write('孤军奋战！！')'''

#f.write('东方红。太阳升\n')
#f. write('阅读')
#文件只读
'''f = open('yesterday','r',encoding = 'utf-8')
f.read()
print(f)
'''


f =open('yesterday2','r',encoding = 'utf-8')
print(f.read())
for i in range(3):
    print(f.readline())


f.close()

#with 语句
with open('yesterday2','r',encoding = 'utf-8') as f:
    for line in f:
        print(line)



