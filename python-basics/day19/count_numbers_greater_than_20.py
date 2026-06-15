numbers = []

for i in range(5):
    nums = int(input("Enter the 5 numbers:\n "))
    numbers.append(nums)

count = 0

for num in numbers:
    if num > 20:
        count += 1

print(f"The total count for numbers greater than 20 are: {count}")
