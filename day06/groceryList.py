#!/usr/bin/env python

def groceryList():
    myList = []
    userinputItem = ""
    while (userinputItem != ":x"):
        userinputItem = input()
        myList.append(userinputItem)
        if userinputItem == ":x":
            exit()

groceryList()
