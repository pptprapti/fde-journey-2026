numbers = [10, 25, 7, 40, 15]
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num

print(smallest)