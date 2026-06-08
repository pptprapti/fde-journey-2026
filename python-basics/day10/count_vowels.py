name = input("Enter your name: ")
name = name.lower()
counter = 0
vowels = ['a','e','i','o','u']
for ch in name:
    if ch in vowels:
        counter = counter + 1
    
print (counter)