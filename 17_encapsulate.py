#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Date   : 2022/10/8
@Author : shenBF
@Desc   : 封装
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 年龄不希望在类的外部被使用，所以加了两个__

    def show(self):
        print(self.name, self.__age)

    def __show2(self):
        print('私有的show方法', self.name, self.__age)


stu = Student('张三', 20)
stu.show()
# 在类的外部使用name与age
print(stu.name)
# print(stu.__age)
print(dir(stu))  # 列出stu可以访问的属性与方法
print(stu._Student__age)
# 还可以修改改属性
stu._Student__age = 30
print(stu._Student__age)
stu.show()
# 访问私有方法
# stu.__show2()
stu._Student__show2()

