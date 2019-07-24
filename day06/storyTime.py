#!/usr/bin/env python

def storyFuntion():
    noun = input("enter a noun(person/animal): ") #valid for a person or animal
    verb = input("enter a verb(continuous): ")
    place = input("enter a place: ")

    storyLine = ("{} is {} to the {}" .format(noun, verb, place))
    print(storyLine)

storyFuntion()
