#!/usr/bin/env python

def groceryList():
    print("grocery list console v1./n enter :edit to edit your list :view to read your list and :exit to close")
    menuItem = input()
    myList = []
    userinputItem = ""
    while (menuItem != "exit"):
        if (menuItem == "edit"):
            print("hit enter to move to a new line and :q to exit")
            while (userinputItem != ":q"):
                userinputItem = input()
                myList.append(userinputItem)
                if (userinputItem == ":q"):
                    break
        if (menuItem == ":view"):
            print(myList)
            break
        elif menuItem == ":exit":
            exit()

groceryList()
