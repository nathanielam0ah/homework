#!/usr/bin/env python3

from mysql_module01 import mydb

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
