#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Date   : 2022/10/8
@Author : shenBF
@Desc   : 
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '在吃饭')


stu1 = Student('张三', 20)
stu2 = Student('李四', 30)
# 动态绑定属性
stu2.gender = '女'
print(stu2.name, stu2.age, stu2.gender)


# 动态绑定方法
def show():
    print('定义在类之外的，称为函数')


stu2.show = show
stu2.show()
