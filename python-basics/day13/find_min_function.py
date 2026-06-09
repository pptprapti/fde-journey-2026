numbers = [10, 25, 7, 40, 15]

def find_min(numbers):

    smallest = numbers[0]

    for num in numbers:
        if num < smallest:
            smallest = num

    return smallest

smallest = find_min(numbers)

print(smallest)