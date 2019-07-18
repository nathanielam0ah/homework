#!/usr/bin/env python

def grades(raw_marks):
    if raw_marks >= 80:
        print("you got an A")
    elif raw_marks >= 65:
        print("you got a B")
    elif raw_marks >= 55:
        print("you got a C")
    else:
        print("you got a D")

grades(int(input("what is your mark?: ")))
