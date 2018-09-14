#! /usr/bin/evn python3
# -*- coding:utf-8 -*-

' io test'
from io import StringIO

__author__ = 'fucai'



with open('/Users/fucai/Desktop/test.txt', 'r', encoding='gbk') as f:
    con = f.readline()


with open('/Users/fucai/Desktop/test.txt', 'r', encoding='gbk') as f:
    for line in f.readlines():
        print(line.strip())


with open('/Users/fucai/Desktop/test.txt', 'w', encoding='gbk') as w:
    w.write('Hello world\nHe')


# 先用流存储，后读取
io = StringIO()
with open('/Users/fucai/Desktop/test.txt', 'r', encoding='gbk') as f:
    for line in f.readlines():
        io.write(line)
#必须重置指针位置
io.seek(0, 0)
while True:
    s = io.readline()
    if s == '':
        break
    print('--', s)
