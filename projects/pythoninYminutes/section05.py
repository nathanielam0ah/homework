#!/usr/bin/env python

class Human:
    species = "H. sapiens"

    #basic initializer
    def __init__(self, name):
        self.name = name
        self.age = 0

    #instance method
    def say(self, msg):
        return "{0}: {1}".format(self.name, msg)

    #class method is shared among all instances in the class
    @classmethod
    def get_species(cls):
        return cls.species

    #called without a class or instance reference
    @staticmethod
    def grunt():
        return "*grunt*"

    #turns the method age() into a read only attrib
    @property
    def age(self):
        return self._age

    #allows the property to be set
    @age.setter
    def age(self, age):
        self._age = age

    #this allows a property to be deleted
    @age.deleter
    def age(self):
        del self._age

#Instantiating a class
i = Human(name = "Nathaniel")
print(i.say("Hello"))

j = Human(name = "Kwame")
print(j.say("Hello"))

#call out class method
print(i.get_species())

#changing the shared attributes
Human.species = "H. neanderthalensis"
print(i.get_species())
print(j.get_species())

#calling the static method
print(Human.grunt())

#update the property
i.age = 42

#get the property
print(i.age)

#delete the property
del i.age
