#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging;

import aiomysql

logging=logging.basicConfig(level=logging.INFO)
import asyncio

' 标题 '

__author__ = 'fucai'

#创建连接池
@asyncio.coroutine
def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = yield from aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw.get('user'),
        password=kw.get('password'),
        db=kw.get('db'),
        charset=kw.get('charset', 'utf-8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize= kw.get('minsize', 1),
        loop=loop

    )

async def select(sql, args, size=None):
    logging.log(sql, args)
    global  __pool
    with (await __pool) as conn:
        cur =await conn.cursor(aiomysql.DictCursor)
        await cur.execute(sql.replace('?', '%s'), args or ())
        if size:
            rs = await cur.fetchmany(size)