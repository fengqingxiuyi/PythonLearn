#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Date   : 2022/10/8
@Author : shenBF
@Desc   : 自定义上下文管理器

ContentManager实现了特殊方法__enter__()和__exit__()称为该类对象遵守了上下文管理器协议。
该类对象的实例对象称为上下文管理器，即ContentManager()。

"""


class ContentManager:
    def __enter__(self):
        print('enter方法被调用了')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用了')

    def show(self):
        print('自定义的方法')
