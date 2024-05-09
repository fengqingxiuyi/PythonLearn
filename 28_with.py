#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Date   : 2022/10/8
@Author : shenBF
@Desc   : 使用with语句操作文件不需要关闭文件资源，因为with语句实现了__exit__()方法，该方法内部执行了关闭文件资源的操作。
"""

with open('02_print.txt') as srcFile:
    print(srcFile.read())
