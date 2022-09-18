#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Date   : 2022/9/18
@Author : shenBF
@Desc   : 转义符
"""

# 转义字符
print('hello\nworld')    # 换行，光标移动到下一行的开头
print('hello\tworld')    # tab键，光标移动到下一组4个空格的开始处，这里的\t占三个位置
print('helloooo\tworld') # 这里的\t占四个位置
print('hello\rworld')    # 回车，光标移动到本行的开头，输出：world
print('hello\bworld')    # 回退一个字符，输出：hellworld

print('http:\\\\www.baidu.com') # 使用\\输出字符\
print('老师说：\'大家好\'') # 使用\'输出字符'
print('老师说：\"大家好\"') # 使用\"输出字符"

# 原字符：不希望字符串中的转义字符起作用，在字符串之前加上r或R即可
print(r'hello\nworld')
#print(r'hello\nworld\') # 最后不能有单个\，会报错
print(r'hello\nworld\\')
