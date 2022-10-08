#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Date   : 2022/10/8
@Author : shenBF
@Desc   : 
"""

'''
错误信息：UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc3 in position 0: invalid continuation byte

# 因为25_file.txt文件的编码格式是gbk，而当前文件的编码格式是utf-8，所以会报错。
# file = open('25_file.txt', 'r')
# 解决方案：指定编码格式
file = open('25_file.txt', 'r', encoding='gbk')
'''

file = open('25_file.txt', 'r', encoding='gbk')
print(file.readlines())
file.close()
