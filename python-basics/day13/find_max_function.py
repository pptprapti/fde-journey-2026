numbers = [10, 25, 7, 40, 15]
largest = numbers[0]
def find_max(numbers):
    largest = numbers[0]

    for num in numbers:
        
        if num > largest:
            largest = num
    return largest

result = find_max(numbers)
print(result)
        
