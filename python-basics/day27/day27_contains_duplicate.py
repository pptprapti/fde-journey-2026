def contains_duplicates(nums):
    frequency ={}
    
    for n in nums:
        if n in frequency:
            return True
        else:
            frequency[n] =  1

    return False  

nums = [1,2,3,4]

result = contains_duplicates(nums)

print(result)