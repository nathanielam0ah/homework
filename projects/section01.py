#!/user/bin/env python

#numbers
3

#simple math
print(1 + 1)
print(8 - 1)
print(10 * 2)
print(35 / 5)

#division
print(5 / 20)

#division with floats
#2.0 is a float data type
print( 11.0 / 4.0 )

#integer division
print(5//30)
print(4//30)

#mod operation
print(55 % 6)

#exponentiation
print(2**4)

#enforce with parentheses
print((1 + 3) * 2)

#Boolean Operators
#note the *and* & *or* are case-sensitive
print(True and False)
print(True or False)

#equality
print(1 == 2)
print(2 == 1)

#inequality
print(1 != 2)
print(2 != 1)

#more comparison
print(1 < 10)
print(1 > 10)
print(2 <= 2)
print(1 >= 10)

#chanined comparisons
print(1 < 6 < 10)
print(2 < 78 < 3 )

#string created with ""/''
print("Hello, World!")
print('Hello, Nathaniel')

#Concatenations
print("Welcome, " + "Nathaniel")
print("Let's " + "learn " + "Python")

#Concatenations without the "+"
print("Python dey"" be")

#string multiplication
print("Hello" * 3)

#array
print("this is a little string"[0])

#finding the length of a string
print(len("this string"))

#string formatting with %
x = 'seed'
y = 'water'
z = "the items in the set are %s and %s" % (x, y)
print(z)

#using .format
myList = "the item in my inventory are {} and {}" .format(x ,y)
print(myList)

#none is an object
None

#comparing items to None
print("etc" is None)
print(None is None)

#object in boolean context
print(bool(0))
print(bool(" "))
