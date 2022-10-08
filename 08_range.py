#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Date   : 2022/9/27
@Author : shenBF
@Desc   : 
"""

r = range(10)
print(r)  # range(0, 10)
print(list(r))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

r = range(1, 10)
print(list(r))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

r = range(1, 10, 2)
print(list(r))  # [1, 3, 5, 7, 9]

print(1 in r)
print(10 not in r)
