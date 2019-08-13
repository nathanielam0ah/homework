#!/usr/bin/env python3

from mysql_module01 import mydb,mycursor

#select from table
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print("\n")

#selecting columns
mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print("\n")

#using fetchone() method
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()
print(myresult)
