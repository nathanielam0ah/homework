#!/usr/bin/env python

import a

print("starting from b")
print("b started")

def hi_from_b():
    print("hello from b villa")

if __name__ == "__main__":
    hi_from_b()
    a.hi_from_a()
