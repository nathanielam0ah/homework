#!/usr/bin/env python

class Employee(object):
    employeeCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def displayCount(self):
        print("total employees: {}".format(Employee.employeeCount))
    def displayEmployee(self):
        print("Name: {}".format(self.name))

emp = Employee("Van", 344)
emp.displayEmployee()

class Parent(object):
    def parent_method():
        print("Parent method")
    def __init__(self, name):
        self.parent_name = name

class Child(Parent):
    child_attribute = "i am 16 years"
    def __init__(self, name):
        self.child_name = name
