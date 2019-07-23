#!/usr/bin/env python

some_var = 5 #variable declaration

#if statement
if some_var > 10:
    print("bigger than 10")
elif some_var < 10:
    print("less than 10")
else:
    print("some_var is 10")

#for loops
for usernames in ["nathaniel", "nat7202", "nathanielam0ah"]:
    print("{0} is nathaniel" .format(username))

#for loop in ranges
for i in range(3):
    print(i)

#while loops
x = 0
while x < 4:
    print(x)
    x += 1

# Handle exceptions with a try/except block
try:
    raise IndexError("This is an index error")
except IndexError as e:
    pass
except (TypeError, NameError):
    pass
else:
    print "All good!"
finally:
    print "We can clean up resources here"

#instead of try/finally
with open("myfile.txt") as f:
for line in f:
print line
