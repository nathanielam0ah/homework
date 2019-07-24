#!/usr/bin/env python

class Account:
    charges = None
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def withdraw(self, amount):
        self.balance = self.balance - amount - Account.charges
        return (self.name + "your balance is " + self.balance)

name = str(input("name: "))
balance = int(input("balance: "))
myAccount = Account(name, balance)
