#!/usr/bin/env python

account01 = {"firstname":"Nathaniel", "lastname":"Amoah", "accountType":"Savings", "balance":500.00}
balance01 = account01.get("balance")
account02 = {"firstname":"James", "lastname":"Gunn", "accountType":"Loans", "balance":500.00}
balance02 = account02.get("balance")
account03 = {"firstname":"Hanzou", "lastname":"Hasashi", "accountType":"Investment", "balance":500.00}
balance03 = account03.get("balance")

bankAccounts = [account01, account02, account03]
print(bankAccounts)

def deposit(balance,amountToDeposit):
	return balance+amountToDeposit
def withdraw(balance,amountToWithdraw):
	return balance - amountToWithdraw

acc_01 = deposit(balance01,5645)
acc_001 = withdraw(balance01,123)
print(acc_01)
print(acc_001)

acc_02 = deposit(balance02,789)
acc_002 = withdraw(balance02,132)
print(acc_02)
print(acc_002)

acc_03 = deposit(balance03,200)
acc_003 = withdraw(balance03,300)
print(acc_03)
print(acc_003)
 
