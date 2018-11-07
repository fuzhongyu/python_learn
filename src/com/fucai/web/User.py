#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 用户类 '

__author__ = 'fucai'


class User(Model):
    __tbale__ = 'user'

    id = IntegerFiled(primary_key=True)