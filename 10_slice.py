#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Date   : 2022/9/27
@Author : shenBF
@Desc   : 
"""

lst = [1, 2, 3, 4, 5]
print('原列表', id(lst))
lst2 = lst[1:3:1]
print('切的片段', id(lst2))
print(lst[1:3])  # 默认步长为1，输出：[2, 3]
print(lst[1:3:])  # 默认步长为1，输出：[2, 3]
print(lst[1:3:2])  # 默认步长为2，输出：[2]
print(lst[:3:2])  # start采用默认，默认步长为2，输出：[1, 3]
print(lst[1::2])  # stop采用默认，默认步长为2，输出：[2, 4]
