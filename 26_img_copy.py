#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Date   : 2022/10/8
@Author : shenBF
@Desc   : 
"""

srcFile = open('26_img.png', 'rb')
targetFile = open('26_img_copy.png', 'wb')
targetFile.write(srcFile.read())
targetFile.close()
srcFile.close()
