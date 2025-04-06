# Given an integer array nums, find a subarray that has 
# the largest product, and return the product.

#The test cases are generated so that the answer will 
# fit in a 32-bit integer.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        curMin = 1
        curMax = 1
        # Max of current nums up to n
        for n in nums:
            if n == 0:
                curMin = 1
                curMax = 1
                continue
            temp = curMin
            curMin = min(n * curMin, n * curMax, n)
            curMax = max(n * temp, n * curMax, n)
            res = max(res, curMax)

        return res