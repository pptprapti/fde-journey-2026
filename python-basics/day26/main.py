#from bank import BankAccount
import bank

owner1= bank.BankAccount("Prapti", 500000)
owner2 = bank.BankAccount("Aditya", 60000)


owner1.deposit(20000)
owner2.withdrawal(35000)

print(owner1.balance)
print(owner2.balance)

print(owner1)
print(bank.BankAccount.total_account)

