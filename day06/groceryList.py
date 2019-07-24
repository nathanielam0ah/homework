#!/usr/bin/env python

def groceryList():
    myList = []
    menuItem = None
    userinputItem = None
    while 1:
        menuItem = input("(:e)dit (:v)iew (:q)uit: ")
        if (menuItem == ":e"):
            print("(enter) to move to next line (:c)ancel")
            while 1:
                userinputItem = input()
                myList.append(userinputItem)
                if (userinputItem == ":c"):
                    myList.pop()
                    break
        if (menuItem == ":v"):
            print(myList)
        if (menuItem) == ":q":
            exit()

groceryList()
