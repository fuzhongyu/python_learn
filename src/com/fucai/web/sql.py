#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging;

import aiomysql

logging=logging.basicConfig(level=logging.INFO)
import asyncio

' 操作数据库工具类 '

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
        minsize=kw.get('minsize', 1),
        loop=loop

    )


async def select(sql, args, size=None):
    logging.log(sql, args)
    global  __pool
    async with __pool.get() as conn:
        #aiomysql.DictCursor的作用是查询返回的格式为字典形式
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(sql.replace('?', '%s'), args or ())
            if size:
                rs = await cur.fetchmany(size)
            else:
                rs = await cur.fetchall()
            logging.info('rows returned: %s' % len(rs))
            return rs


async def execute(sql, args, automcommit=True):
    logging.log(sql)
    async with  __pool.get() as conn:
        if not automcommit:
            await conn.begin()
        try:
            async with conn.cursor() as cur:
                await cur.execute(sql.replace('?', '%s'), args)
                affected = cur.rowcount()
            if not automcommit:
                await conn.commit()
        except BaseException as e:
            if not automcommit:
                await conn.roolback()
            raise
        return affected


if __name__ == '__main__':
    connInfo = {'user':'root', 'password':'', 'db':'boot'}
    create_pool(asyncio.get_event_loop(), **connInfo)
    print(select('select * from user where  id=?', 1))
