#!/usr/bin/env python

def groceryList():
    myList = []
    menuItem = None
    userinputItem = None
    while (menuItem != ":q"):
        menuItem = input("(:e)dit (:v)iew (:q)uit: ")
        if (menuItem == ":e"):
            print("(enter) to move to next line (:c)ancel")
            while (userinputItem != ":c"):
                userinputItem = input()
                myList.append(userinputItem)
                if (userinputItem == ":c"):
                    break
        if (menuItem == ":v"):
            print(myList)
        if (menuItem) == ":q":
            exit()

groceryList()
