#coding:utf-8


#购物车程序
#定义一个商品的列表
product_list = [
    ('iPhone6s',2700),
    ('Mac Pro',9800),
    ('Bike',800),
    ('Coffee',30),
    ('Book',20),
    ('Watch',88)
]
shopping_list = [] #定义一个购物车列表，起初是空的，所以列表为空
salary = input("请输入你的工资:")
if salary.isdigit():     #python isdigit（）方法是检查字符串是否由数字组成
    salary = int(salary)
    while True:
        for item in product_list:
            print(product_list.index(item),item)  #找到商品对应下标   用 .index 方法

        user_choice = input("请选择你需要购买的商品：")

        if  user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and  user_choice >= 0:
               p_item = product_list[user_choice]  #获取到商品的价格
               if p_item[1] <= salary:  #买的起
                   shopping_list.append(p_item)
                   salary -= p_item[1]
                   print("Added %s into shopping cart ,您的余额还剩多少\033[31;1m%s\033[0m"%(p_item,salary)) #高亮显示
               else:
                   print("\033[41;1m你的余额只剩[%s]啦,还买个锤子啊！！！\033[0m"%salary)
            else:
               print("商品不存在")

        elif  user_choice == 'q':
            print("----shoping list-----")
            for p in shopping_list:
                print(p)
            print("您的余额为:\033[31;1m%s\033[0m"%salary)
            exit()
        else:
            print('输入错误,请重新输入！')

else:
    print("\033[31;1m您的输入有误，请重新输入：\033[0m")
#break





