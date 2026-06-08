numbers = [10, 5, 4, 20, 30, 25, 90, 14]
largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print(f"The largest among {numbers} is: {largest}")
print(f"The smallest among {numbers} is: {smallest}")
