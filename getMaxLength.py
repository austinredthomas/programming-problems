# Find the maximum length of a subarray with positive product
def getMaxLength(nums):
    # Edge case for nums length == 1
    if len(nums) == 1:
        if nums[0] > 0:
            return 1
        else:
            return 0

    maxLength = 0
    currentLength = 0
    negativePrefix = 0
    negativeSuffix = 0
    negativeCount = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            currentLength = negativePrefix = negativeSuffix = negativeCount = 0
        # Case for positive number
        elif nums[i] > 0:
            currentLength += 1
            if negativeCount > 0:
                negativeSuffix += 1
        # Case for negative number
        elif nums[i] < 0:
            currentLength += 1
            if negativeCount == 0:
                negativePrefix = currentLength
                negativeCount += 1
                negativeSuffix += 1
            else:
                negativeSuffix = 1
                negativeCount += 1
        # Determine and update maxLength
        if negativeCount % 2 == 0:
            maxLength = max(currentLength, maxLength)
        # In the event of odd negative count, remove the shortest prefix/suffix from the length
        else:
            maxLength = max(maxLength, currentLength - min(negativePrefix, negativeSuffix))
    return maxLength
print(getMaxLength([1,2,3,5,-6,4,0,10]))