#! /usr/bin/evn python3
# -*- coding: utf-8 -*-

'muli thread'
import threading

__author__ = 'fucai'

#创建锁
lock = threading.Lock()
#创建全局变量
thread_local = threading.local


def loop():
    #加锁
    lock.acquire()
    try:
        print('thread %s is running...' % threading.current_thread().name)
        n = 0
        while n < 5:
            n = n+1
            print('thread %s >>> %s' % (threading.current_thread().name, n))
        print('thread %s ended.' % threading.current_thread().name)
    finally:
        #释放锁
        lock.release()


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)