#!/usr/bin/env python3

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="PE.prah111",
  database="database01"
)
