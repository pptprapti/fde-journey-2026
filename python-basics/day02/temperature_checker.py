temperature = int(input("Enter Temperature: "))

if temperature > 35:
    print("Hot")
elif temperature >= 20 and temperature <=35:
    print("Pleasant")
else:
    print("Cold")

# temperature > 20 and temperature <=35 can also be written as 20<=temperature<=35