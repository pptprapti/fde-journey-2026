class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdrawal(self,amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print(f"invalid amount for withdrawal request. You balance is: {self.balance}")

    def is_overdrawn(self):
        return self.balance < 0
    

Owner1 = BankAccount("Prapti",10000000)
Owner2 = BankAccount("Rahul", 500000)
Owner3 = BankAccount("Anita", 2000000)

accounts = [Owner1, Owner2, Owner3]

for acc in accounts:
    print(f"Owner Name: {acc.owner}, Balance : {acc.balance}")





        