#! /usr/bin/evn python3
# -*- coding: utf-8 -*-

' Month Enum'
from enum import Enum

__author__ = 'fucai'


Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


if __name__ == '__main__':
    for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)