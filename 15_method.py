#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Date   : 2022/9/30
@Author : shenBF
@Desc   : 
"""


class Student:  # 类名，规范要求每个单词的首字母大写，其余小写
    native_place = '地址'  # 类属性

    # 构造方法
    def __init__(self, name):
        # self.name称为实体属性，这里进行了一个赋值的操作，将局部变量的name的值赋给了实体属性
        self.name = name

    # 实例方法
    def eat(self):
        print('吃饭...')

    # 静态方法
    @staticmethod
    def sm():
        print('静态方法')

    # 类方法
    @classmethod
    def cm(cls):
        print('类方法', cls)


# 函数
def drink():
    print('喝水...')


stu = Student("")
print(type(stu))  # 输出 <class '__main__.Student'>
print(stu)  # stu为实例对象
print(type(Student))  # 输出 <class 'type'>
print(Student)  # Student是类对象

print("----------------")

stu = Student("")
print(Student.native_place)
print(stu.native_place)
print(Student.cm())
print(stu.cm())
print(Student.sm())
print(stu.sm())

