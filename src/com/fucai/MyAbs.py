#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' my abs '

__author__ = 'fucai'

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


def my_student(id, name='fucai', age=25):
    return id, name, age


def person2(name, age, **kz):
    print(name, age, kz)


def person4(name, age, *, city, job):
    print(name, age, city, job)


def person(name, age, *args, city, job):
    print(name, age, args, city, job)


def person3(name, age, *, city, **kz):
    print(name, age, city, kz)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n+1
    return 'done'


def err(num):
    try:
        if num is None:
            print("is none")
        elif not isinstance(num, int):
            raise TypeError("is not int type")
        print("--------")
    except TypeError:
        print("type error")


#当在本模块启动运行的时候，__name__的值是main ,当在别的模块调用的时候，是模块名，所以该__name__判断可以用在本地测试，而使别的的模块调用的时候不会执行这块代码
if __name__ == '__main__':
    print(my_abs(-10))
