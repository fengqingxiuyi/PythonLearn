#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Date   : 2022/9/18
@Author : shenBF
@Desc   :
"""

# 输出数字
print(10)
print(10.5)

# 输出字符串
print('hello')
print("helloworld")
print(chr(0b100111001011000))  # 使用二进制输出 乘
print(ord('乘'))  # 输出 乘 的十进制

# 输出表达式的结果
print(1 + 1)

# 不进行换行输出
print('hello', 'world', 'PyCharm')

# 输出到当前目录下的print.txt文件中，
# mode为a+，表示如果文件不存在就先创建再添加内容，如果存在就追加内容
fp = open('02_print.txt', 'a+')
print('helloworld', file=fp)
fp.close()
