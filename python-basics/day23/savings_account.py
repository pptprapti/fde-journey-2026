class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        self.trans_history = []

    def deposit(self,amount):
        self.balance += amount
        self.trans_history.append(f"Deposit of Rs {amount}, New Balance: {self.balance} ")

    def withdrawal(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            self.trans_history.append(f"Withdrawn Rs {amount}, New Balance: {self.balance}")
        else:
            print(f"You've not entered a valid amount. Your current balance is: {self.balance}")

    def is_overdrawn(self):
        return self.balance < 0
 


class SavingsAccount(BankAccount):
    def __init__(self,owner,balance,interest_rate):
        super().__init__(owner,balance)
        self.interest_rate = interest_rate
        
    def add_interest_rate(self):
        self.balance = self.balance + (self.balance * self.interest_rate)
        self.trans_history.append(f" Added Interest rate for the month. New Balance: {self.balance}")
        

owner1 = SavingsAccount("Prapti",100000,0.25)

for history in owner1.trans_history:
    print(f"----The transaction history ---- {history}")


owner1.deposit(25000)
owner1.withdrawal(20000)
owner1.add_interest_rate()

for history in owner1.trans_history:
    print(f"----The transaction history ---- {history}")
