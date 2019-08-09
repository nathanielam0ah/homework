#!/usr/bin/env python

def minimalinList(listOne):
    currentMin = listOne[0]
    currentMin2 = currentMin
    for index in listOne:
        if (index < currentMin):
            currentMin = index
    for index2 in listOne:
        if (currentMin >= currentMin2):
            currentMin2 = index2
    return (currentMin, currentMin2)

myList = [-200,89, 3, 4, 6, 7, -100]
print(minimalinList(myList))

#to be continued
