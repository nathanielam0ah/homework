#!/usr/bin/env python

#print statements
print ("Welcome to python3. Nice to meet you!")

#input data from console
firstInput = input("enter some data: ")
print(firstInput)

#assigning variables
mySelf = "male"
print(mySelf)

#if statements
print("google!") if 3 > 2 else 2

#Lists
li = []
otherList = [4,5,6,6] #prefilled list

#adding to Lists
li.append(1)
li.append(2)
li.append(4)
li.append(3)

#removing from end of Lists
li.pop()

#access a list
li[0]
li[0] = "nathanielam0ah" #changing values

#slice syntax of Lists
print(li[1:3]) #range
print(li[2:]) #omit the begining
print(li[:3]) #omit the end
print(li[::3]) #select every second entry
print(li[::-1]) # reverse a copy of list

#viewing the values
print(li[0:3])

#adding list together
print (li + otherList)

#Concatenating Lists
li.extend(otherList)
print(li)

#removing from Lists
li.remove(2)

#inserting to specific index
li.insert(1,2)

#getting a specific index
print(li.index(2))

#check for existence in Lists
print(1 in li)

#length of Lists
print(len(li))

#TUPLES TUPLES
#tuples are immutable
tup = (1,2,3)

print(len(tup)) #length of tuple
tup + (4,5,6,7)
print(tup[:2])
print(2 in tup)

#unpacking tuples
a,b,c = (1,2,3)

#DICTIONARIES DICTIONARIES
filledDict = {"one": 1, "two": 2, "three": 3}
print(filledDict["one"])
print(filledDict.keys()) #printing dict keys

filledDict.values() #getting DICTIONARIES values
print(filledDict.items()) #get values as tuples
print(1 in filledDict)

filledDict.get("one")
filledDict.get("one" , 4)

#set the value of key with a syntax
filledDict["two"] = 2

filledDict.setdefault("one", 1)

empty_set = set()
some_set = set([1,4,5,4]) #initializing a set

another_set = set([3,4,5,6])

filled_set = {2,3,4,5}
filled_set.add(1)


#set intersection
other_set = {3,4,5,3}
filled_set & other_set

#set union
filled_set | other_set

#set differences
print({1,2,3,4} - {2,4})

#symetric differences
print({1,2,3,4} ^ {2,3,4,5})

#set on the left is a superset of set on the right
print({1,2} >= {1,2,3})

#check if set on the left is a subset of set on the right
print({1,2} <= {1,2,3,4})

#check for existence in set with in
print(2 in fiilled_set)

print(type(li))
print(type(filledDict))
print(type(5))
