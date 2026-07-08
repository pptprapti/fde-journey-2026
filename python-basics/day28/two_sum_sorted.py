def two_sum_sorted(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left < right :
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum > target:
            right -=1
        else: 
            left +=1

numbers = 1,2,3,4,5,6,7,8,9,10,11
target = 16

result = two_sum_sorted(numbers,target)

print(result)


    