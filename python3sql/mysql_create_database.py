#!/usr/bin/env python3

from mysql_module00 import mydb

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE database01")
