#!/usr/bin/env python

def infinitAdd( *the_number ):
    sum = 0
    for x in the_number:
        sum = sum + x
    print(sum)
    return sum

infinitAdd(1, 2, 4, 5, 100)
