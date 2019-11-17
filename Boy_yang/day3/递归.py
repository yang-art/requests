
#在函数内部，可以调用其他函数，如果一个函数在内部调用自身本身，这个函数就是递归函数。

def calc(n):
    print(n)
    if int(n/2) >0:
        return calc(int(n/2))
    print("->",n)

calc(10)

