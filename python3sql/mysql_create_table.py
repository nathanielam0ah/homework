#!/usr/bin/env python3

from mysql_module01 import mydb

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
