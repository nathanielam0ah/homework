#!/usr/bin/env python3

def sqr(the_number):
	return the_number * the_number

init = [1, 2 , 3, 4 , 5, 6, 7, 8, 9, 10,]
init_Two = []

for x in init:
	init_Two.append( sqr(x) )

print(init_Two)
