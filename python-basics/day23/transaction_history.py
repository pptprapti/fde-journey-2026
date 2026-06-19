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
    
owner1 = BankAccount("Prapti", 1000000)
owner1.deposit(25000)
owner1.deposit(25000)

owner1.withdrawal(50000)

for history in owner1.trans_history:
    print(f"----The transaction history ---- {history}")

