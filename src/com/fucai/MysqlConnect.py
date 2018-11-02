#! /usr/bin/evn python3
# -*- coding : utf-8 -*-

' mysql connect '

import mysql.connector

__author__ = 'fucai'


conn = mysql.connector.connect(user='root', password='', database='boot')
cursor = conn.cursor()
cursor.execute('SELECT * FROM user')
values = cursor.fetchall()
print(values)