#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Date   : 2022/10/8
@Author : shenBF
@Desc   : 多态
"""


class Animal(object):
    def eat(self):
        print('动物要吃东西')


class Dog(Animal):
    def eat(self):
        print('狗吃肉')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')


class Person(object):
    def eat(self):
        print('人吃五谷杂粮')


def fun(animal):
    animal.eat()

fun(Dog())
fun(Cat())
fun(Animal())
print('----------------')
fun(Person())  # 也算多态，被称为鸭子类型
# 动态语言的多态崇尚“鸭子类型”，当看到一只鸟走起来像鸭子、游泳起来像鸭子、飞起来也像鸭子，那么这只鸟就可以被称为鸭子。
# 在鸭子类型中，不需要关心对象是什么类型，到底是不是鸭子，只关心对象的行为。
