numbers = [10,20,30,40]



def calculate_sum(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return (total)

result = calculate_sum(numbers)
print(result)