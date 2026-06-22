class BankAccount:

    total_account = 0

    def __init__ (self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.trans_history = []
        BankAccount.total_account += 1

    
    @staticmethod
    def is_valid_account_number(account_number):
        return len(account_number) == 10  and account_number.isdigit() 

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

    def __str__(self):
        return f"BankAccount(Owner: {self.owner}, balance = {self.balance}) "
    
    def __repr__(self):
        return f"BankAccount_repr(Owner: {self.owner}, balance = {self.balance})"
    
    def __eq__(self,other):
        return self.owner == other.owner and self.balance == other.balance
    
   
