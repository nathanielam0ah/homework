#!/usr/bin/env python3

from mysql_module01 import mydb

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Sandy', 'Valley 345')
]

mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "was inserted")
