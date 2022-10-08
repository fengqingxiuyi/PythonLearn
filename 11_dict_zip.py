#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Date   : 2022/9/28
@Author : shenBF
@Desc   : 
"""

items = ['Fruits', 'Books', 'Others']
prices = [96, 78, 85]
lst = zip(items, prices)
print(list(lst))  # 输出 [('Fruits', 96), ('Books', 78), ('Others', 85)]

prices2 = [96, 78, 85, 20]
lst2 = zip(items, prices2)
print(list(lst2))  # 输出 [('Fruits', 96), ('Books', 78), ('Others', 85)]

lst3 = {item.upper(): price for item, price in zip(items, prices)}
print(list(lst3))  # 输出 ['FRUITS', 'BOOKS', 'OTHERS']
