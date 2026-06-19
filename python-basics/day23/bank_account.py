class BankAccount:

    def __init__(self,owner,balance):
      self.owner = owner
      self.balance = balance
      print(f"{self.owner}, {self.balance}")

    def deposit(self,amount):
      self.balance += amount

    
    def withdrawal(self,amount):
      if amount <= self.balance:
          self.balance -= amount
      else:
          print(f"invalid amount for withdrawal request. You balance is: {self.balance}")

    def is_overdrawn(self):
      return self.balance < 0 


owner1 = BankAccount("Prapti", 10000000)
owner1.deposit(10000)
print(owner1.balance)
owner1.withdrawal(10010001)
owner1.withdrawal(10000)
print(owner1.balance)
print(owner1.is_overdrawn())



  

