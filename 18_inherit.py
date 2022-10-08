#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Date   : 2022/10/8
@Author : shenBF
@Desc   : 继承
"""


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('姓名：{0}，年龄：{1}'.format(self.name, self.age))


class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score

    def info(self):
        super().info()
        print('分数：', self.score)
        # print('姓名：{0}，年龄：{1}，分数：{2}'.format(self.name, self.age, self.score))


stu = Student('张三', 20, 100)
stu.info()
