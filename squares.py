#!/usr/bin/env python3

def sqr(the_number):
	return the_number * the_number

init = [1, 2 , 3, 4 , 5, 6, 7, 8, 9, 10,]
initTwo = []

for x in init:
	initTwo.append( sqr(x) )

print(initTwo)
