#!/usr/bin/env python

def groceryList():
    menuItem = ""
    myList = []
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
            exit()

groceryList()
