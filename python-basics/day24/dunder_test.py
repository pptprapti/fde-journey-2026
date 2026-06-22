class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"BankAccount(Owner: {self.owner}, balance = {self.balance}) "
    
    def __repr__(self):
        return f"BankAccount_repr(Owner: {self.owner}, balance = {self.balance})"

owner1 = BankAccount("Prapti", 100000)
print(owner1)
print([owner1])

