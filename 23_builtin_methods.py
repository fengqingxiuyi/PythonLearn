#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Date   : 2022/10/8
@Author : shenBF
@Desc   : 
"""

import sys, time, urllib.request, math

print(sys.getsizeof(11))  # 整数11所占的字节数
print(time.localtime(time.time()))
print(urllib.request.urlopen('https://www.baidu.com').read())
print(math.pi)  # π
