#coding:utf-8
#__author__='易木'

class Dog:
    def __init__(self,name):
        self.name = name

    def bulk(self):
        print('%s汪汪汪'%self.name)

d1 = Dog('jeff')
d2 = Dog('make')

d1.bulk()
d2.bulk()
