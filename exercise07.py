#!/usr/bin/env python

def test( *numbers ):
    div = 0
    ran = [500, ... , 2500]
    for x in ran:
        if (div % x == 0):
            div = div % x
        else:
            print("not divisible")

test(502, 503)
