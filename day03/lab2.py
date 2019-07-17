#!/usr/bin/env python

account01 = ["Nathaniel", "Amoah", "Savings", 500.00]
balance01 = account01.pop(3)
account02 = ["Kofi" , "Addae", "Current", 300.00]
balance02 = account02.pop(3)
account03 = ["Kwame","Peprah","Investment",20.00]
balance03 = account03.pop(3)

b_accts={"001":"account01", "002":"account02", "003":"account03"}
print(b_accts)

def deposit(balance,amountToDeposit):
	return balance+amountToDeposit
def withdraw(balance,amountToWithdraw):
	return balance - amountToWithdraw

acc_01 = deposit(balance01,450)
acc_001 = withdraw(balance01,640)
print(acc_01)
print(acc_001)

acc_02 = deposit(balance02,454)
acc_002 = withdraw(balance02,5657)
print(acc_02)
print(acc_002)

acc_03 = deposit(balance03,458)
acc_003 = withdraw(balance03,845)
print(acc_03)
print(acc_003)
 
