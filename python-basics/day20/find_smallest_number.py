numbers = [15, 8, 22, 3, 19]
smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num 

print(f" The smallest number is: {smallest}")
