#!/usr/bin/env python

def groceryList():
    menuItem = ""
    myList = []
<<<<<<< HEAD
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
=======
    userinputItem = ""
    while (menuItem != "exit"):
        print("grocery list console v1./n enter :edit to edit your list :view to read your list and :exit to close")
        menuItem = input()
        if (menuItem == "edit"):
            print("hit enter to move to a new line and :q to exit")
            while (userinputItem != ":q"):
                userinputItem = input()
                myList.append(userinputItem)
                if (userinputItem == ":q"):
                    break
        if (menuItem == ":view"):
            print(myList)
        elif menuItem == ":exit":
>>>>>>> 2418a3c8208e083267afcaae825db8f38c75b4ff
            exit()

groceryList()
