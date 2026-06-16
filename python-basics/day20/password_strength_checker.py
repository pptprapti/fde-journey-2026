password = input("Enter password: ")

has_digit = False

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for ch in password:
    if ch in digits:
        has_digit = True
        break

if len(password) >= 8 and has_digit:
    print("Strong Password")
else:
    print("Weak Password")
