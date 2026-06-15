num1 = int(input("Enter any number: "))
num2 = int(input("Enter any number: "))

try:
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Cannot Divide Zero") 