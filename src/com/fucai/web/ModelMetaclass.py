#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging; logging=logging.basicConfig(level=logging.INFO)

' Model元类 '

__author__ = 'fucai'

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        #排除Model类本身
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        #获取table名称
        tableName = attrs.get('__table__', None) or name
        logging.info('found model : %s (table : %s)' % (name, tableName))
        #获取去所以偶的Field和主键名：
        mappings = dict()
        fields = []
        primaryKey = None
        for k,v in attrs.items():
            if isinstance(v, Field):
