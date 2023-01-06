# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

def runningSum(nums):
    runningSum = [nums[0]]
    sum = nums[0]
    for i in range(1, len(nums)):
        sum += nums[i]
        runningSum.append(sum)
    return runningSum
print(runningSum([1,2,3,4]))