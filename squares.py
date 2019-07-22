#!/usr/bin/env python3

def sqr(the_number):

init = [1, 2 , 3, 4 , 5, 6, 7, 8, 9, 10,]
init_two = []
for x in init:
	init_two.append( sqr(x) )
return the_number * the_number

print(init_two)
