numbers = [1,2,3,4,5,6]

def count_even(numbers):
    count_even = 0

    for num in numbers:
        if num  % 2 == 0:
            count_even = count_even + 1
    
    return count_even

print(count_even(numbers))