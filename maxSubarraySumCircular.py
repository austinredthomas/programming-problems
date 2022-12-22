def maxSubarraySumCircular(nums):
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
    
    # find min and max
    currentMax = maxSum = nums[0]
    currentMin = minSum = nums[0]
    for i in range(1, len(nums)):
        currentMax = max(nums[i], nums[i] + currentMax)
        maxSum = max(currentMax, maxSum)
        currentMin = min(nums[i], currentMin + nums[i])
        minSum = min(currentMin, minSum)
    if minSum == sum:
        return maxSum
    return max(maxSum, sum - minSum)

print(maxSubarraySumCircular([-3,-2,-3]))