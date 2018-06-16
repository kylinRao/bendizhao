#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/19 19:57
# @Author  : Aries
# @Site    : 
# @File    : test1.py
# @Software: PyCharm
from db.dbInit01 import lockTableForWrite
count = 20
while count>0:
    count = count-1
    lockTableForWrite()