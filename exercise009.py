#!/usr/bin/env python

def maxList(Li):
    currentMax = Li[0]
    for index in Li:
        if index > currentMax:
            currentMax = index
    return currentMax

myList = ['3', '4', '6', '3', '-100']
print(maxList(myList))
