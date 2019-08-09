#!/usr/bin/env python

def key_sub( **args ):
    args = {'first':0, 'second':0}
    tty1 = 0
    tty1 = args.get(0) - args.get(1)
    print(tty1)
    return tty1

key_sub(first= 23, first= 34)
