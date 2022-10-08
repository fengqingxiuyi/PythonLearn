#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Date   : 2022/10/8
@Author : shenBF
@Desc   : 
"""

import os
path = os.getcwd()
childPath = os.path.join(path, './python_package')
list_files = os.walk(childPath)
for dirPath, dirName, fileName in list_files:
    print(dirPath)
    print(dirName)
    print(fileName)
    print('----------------------')
