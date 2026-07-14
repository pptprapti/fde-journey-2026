def findMaxAverage(nums, k):

    currSum = sum(nums[0:k])
    maxSum = currSum
    
    for i in range(len(nums) - k):
        currSum = currSum - nums[i] + nums[i+k]
        maxSum = max(maxSum, currSum)

    return maxSum/k
        



nums = [1,12,-5,-6,50,3]
k = 4

result = findMaxAverage(nums, k)
print(result)