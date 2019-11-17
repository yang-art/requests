#coding:utf-8

bool_l = 30
count = 0
while count < 3:   #while循环
    bool = int(input('请输入正确的年龄：'))
    if bool == bool_l:
        print('太棒了，答对了')
        break    #结束本次循环

    elif bool > bool_l:

        print("你把我想的太大了，再重新输入一次吧，亲")
    else:
        print("我没那么小，再大点")
    count = count + 1
    if count == 3:
        confirm_jixu = input('还想继续猜吗？')
        if confirm_jixu != "No":
            count = 0



#if count == 3:
else:
    print("输入错误次数太多")














