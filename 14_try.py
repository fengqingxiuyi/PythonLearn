#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Date   : 2022/9/30
@Author : shenBF
@Desc   : 
"""
try:
    a = int(input('请输入第一个整数'))
    b = int(input('请输入第二个整数'))
    result = a / b
except ZeroDivisionError:
    print('除数不允许为0')
except ValueError:
    print('不能将字符串转换为数字')
except BaseException as e:
    print(e)
else:
    print('结果为：', result)
finally:
    print('程序结束')
