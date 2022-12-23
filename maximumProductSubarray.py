def maxProduct(nums):
    maxProductHere = minProductHere = nums[0]
    maxProduct = nums[0]
    for i in range(1, len(nums)):
        # find the maximum product at the current position
        tempMaxProductHere = maxProductHere
        maxProductHere = max(nums[i], nums[i] * maxProductHere, nums[i] * minProductHere)

        # find the minimum product at the current position
        minProductHere = min(nums[i], nums[i] * tempMaxProductHere, nums[i] * minProductHere)
        if maxProductHere > maxProduct:
            maxProduct = maxProductHere
    return maxProduct
print(maxProduct([-2,-3,-4]))