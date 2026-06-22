class BankAccount:
    total_account = 0

    def __init__ (self, owner, balance):
        self.owner = owner
        self.balance = balance
        BankAccount.total_account += 1

    
    @staticmethod
    def is_valid_account_number(account_number):
        return len(account_number) == 10  and account_number.isdigit() 


owner1= BankAccount("Prapti", 50000)
owner2 = BankAccount("Aditya", 200000)
owner3 = BankAccount("Rupam", 100000)

print(owner1.total_account)  #3
print(BankAccount.total_account)  #3
print(BankAccount.is_v                                                                                                                                                                                                                                 alid_account_number("1234567891"))
print(BankAccount.is_valid_account_number("12234abcd"))

#Both are giving same value but what's the difference?
#Since total_account is only ever updated through the class name, there's a single shared value living on the class itself. When you access it through an object like owner1.total_account, Python doesn't find it directly on the object — so it automatically looks up to the class and finds it there. That's why accessing it through any object or through the class name directly gives you the same number — they're all pointing to that one shared value, not separate copies."