#!/usr/bin/env python
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
