#coding:utf-8
#__author__='易木'
user,passwd = "Jeff","123456"
import time
def auth(func):
    def wrapper(*args,**kwargs):
        username = input('Username:').strip()
        password = input('Password:').strip()

        if user == username and passwd == password:
            print("\033[32;1mUser has passed authentication\033[0m")
            func(args,kwargs)
        else:
            exit("\033[31;1mImvalid username or password\033[0m")
        return wrapper



def index():
    print('welcome to index page')
@auth
def home():
    print('welcome to home page')
    return 'from  home'
@auth
def bbs():
    print('welcome to bbs page')
    return 'from bbs'

index()
home()
bbs()
