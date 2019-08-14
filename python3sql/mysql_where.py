#!/usr/bin/env python3

from mysql_module01 import mydb, mycursor

#select with filter
sql = "SELECT * FROM customers WHERE address = 'Valley 345'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print("\n")

#wildcard characters
sql = "SELECT * FROM customers WHERE address LIKE '%Mountain%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print("\n")

#prevent sql injection
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Lowstreet 4", )
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
