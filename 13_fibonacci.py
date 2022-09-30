#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Date   : 2022/9/30
@Author : shenBF
@Desc   : 斐波那契数列
"""


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(6))

for i in range(1, 7):
    print(fib(i), end='\t')
