#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Date   : 2022/10/8
@Author : shenBF
@Desc   : 
"""

import schedule

def job():
    print('哈哈...')

schedule.every(3).seconds.do(job)

while True:
    schedule.run_pending()
