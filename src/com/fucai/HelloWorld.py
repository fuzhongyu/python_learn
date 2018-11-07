#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' hello world '
from datetime import datetime

from src.com.fucai.Student import Student

__author__ = 'fucai'

from collections import Iterable
from functools import reduce

from src.com.fucai.MyAbs import *

'''
多行注释方式
'''


print('hello', 'world')

helloWorld = """Hello
World
"""
print(helloWorld)

# name = input()
# print(name)
a = 100
if a >= 50:
    print(a)
else:
    print(-a)
print(r'\'naiad')
print('ab\nc')
if True:
    print('fucai')

print('中午'.encode('utf-8'))

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

print('Hello,{0},你的成绩是{1:.2f}'.format('fucai', 80.234))

s1 = 130.0
s2 = 80
r = s1 / s2
print(s1 // s2)
print('%.2f' % r)

arr1 = ['a', 'b']
arr2 = [arr1, 'c']
arr3 = ('d',)
arr2[0].append('m')
print(arr2)

print(abs(-10))

print(my_abs(-111))

print(my_student(1, 'fc'))

dic = {'name': 'fucai', 'age': 25}
se = set([1, 2, 2])
print(dic, se)
#获取不存在的属性，会报错
# print(dic['sex'])
#使用get请求，返回none
print(dic.get('sex'))

person2('f', 24, city='hz', province='zj')

person('fuc', '25', 1, 2, city='hangzhou', job='cxy')

person3('fuc2', '25', city=None, job=None, pow=12)

person4('fuc4', 25, city='hangzhou', job='python')

for i, v in enumerate(arr1):
    print(i)


fibarr = fib(5)
if isinstance(fibarr, Iterable):
    for v in fibarr:
            print("--", v)


# while True:
#     try:
#         print(next(fibarr))
#     except StopIteration as e:
#         print(e.value)
#         break


#切片
print('ABCDE'[:3])
print('ABCDE'[::2])

#列表生成器
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)

#数组使用迭代器
ite = iter(arr1)
while True:
    try:
        print(next(ite))
    except StopIteration as e:
        print(e)
        break


#函数式编程，高价函数，map,reduce
def normalize(name):
    return name.capitalize()


L3 = ['adam', 'LISA', 'barT']
L4 = list(map(normalize, L3))
print(L4)


def add(x, y):
    return x+y


print(reduce(add, [1, 2, 3]))


#异常处理 raise, try , expect
err('a')


#filter函数
def not_empty(s):
    #字符串做逻辑运算的时候，None或者空字符串 返回false
    return s and s.strip()


print(list(filter(not_empty, ['A', '   ', None, 'B'])))

#排序函数sorted
print(sorted([1, -2, 3]))
print(sorted([1, -2, 3], key=abs))


#返回函数
def lazy_sum(*args):
    def sum():
       return reduce(add, *args)
    return sum


f = lazy_sum([1, 2, 3, 4])
print(f())

#lambda 匿名函数
print(reduce(lambda x, y: x+y, [1, 2, 3]))

#.__name__可以获取到函数的名字
print(f.__name__)


# type函数判断类型
print(type(123) == int)

now_time = datetime.now()
print(now_time)
print(datetime.timestamp(now_time))







