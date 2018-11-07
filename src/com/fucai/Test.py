#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 标题 '

__author__ = 'fucai'


def coroutine():
    reply = yield 'hello'
    yield reply


c = coroutine()
print(next(c))
print(c.send('world'))