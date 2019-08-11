#!/usr/bin/env python3

from mysql_module01 import mydb

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

print("1 record inserted, ID:", mycursor.lastrowid)
