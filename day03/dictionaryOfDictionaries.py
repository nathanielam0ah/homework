#!/usr/bin/env python

account01 = {"firstname":"Nathaniel", "lastname":"Amoah", "accountType":"Savings", "balance":500.00}
balance01 = account01.get("balance")
account02 = {"firstname":"James", "lastname":"Gunn", "accountType":"Loans", "balance":500.00}
balance02 = account02.get("balance")
account03 = {"firstname":"Hanzou", "lastname":"Hasashi", "accountType":"Investment", "balance":500.00}
balance03 = account03.get("balance")

bank_accounts={"001":"account01", "002":"account02", "003":"account03"}
print(bank_accounts)

def deposit(balance,amountToDeposit):
	return balance+amountToDeposit
def withdraw(balance,amountToWithdraw):
	return balance - amountToWithdraw

acc_01 = deposit(balance01,5234)
acc_001 = withdraw(balance01,3346)
print(acc_01)
print(acc_001)

acc_02 = deposit(balance02,47457)
acc_002 = withdraw(balance02,856)
print(acc_02)
print(acc_002)

acc_03 = deposit(balance03,689)
acc_003 = withdraw(balance03,989)
print(acc_03)
print(acc_003)
 
