#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Date   : 2022/10/8
@Author : shenBF
@Desc   : 使用自定义的模块
"""

import calc

print(calc.add(1, 2))

from calc import sub

print(sub(2, 1))
