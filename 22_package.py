#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Date   : 2022/10/8
@Author : shenBF
@Desc   : 
"""

import python_package.moduleA as mA
import python_package.moduleB as mB

from python_package import moduleA
from python_package.moduleA import a

print(mA.a)
print(mB.b)
