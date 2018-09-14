#! /usr/bin/evn python3
# -*- coding:utf-8 -*-

' student '
import json

__author__= 'fucai'


class Student(object):

    #限制实例属性，只允许对Strudent 实例添加name 和age属性
    # __slots__ = ('__name', '__score')

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    # def get_name(self):
    #     return self.__name
    #
    # def get_score(self):
    #     return self.__score

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    #定义__len__后，可以通过len()函数调用
    def __len__(self):
        return len(self.__name)

    def __str__(self):
        return 'Student object (%s)' % self.__name



# 定义测试
if __name__ == '__main__':
    bart = Student('fucai', 98)
    # print(bart.get_name(), bart.get_score())
    #通过dir()方法获取类的属性和方法
    print(dir(bart))
    if hasattr(bart, '_Student__name'):
        print(getattr(bart, '_Student__name'))
    # bart.age=10
    # print(bart.age)
    bart.name='fc'
    print(bart.name)
    print(len(bart))
    print(bart)
    #使用__slots__的时候，则class不是__dict__
    print(json.dumps(bart, default=lambda obj: obj.__dict__))

