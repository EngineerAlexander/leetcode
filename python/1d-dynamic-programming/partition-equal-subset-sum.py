# Given an integer array nums, return true if you can partition 
# the array into two subsets such that the sum of the elements 
# in both subsets is equal or false otherwise.

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)

        target = sum(nums)//2
        for num in nums:
            new_dp = set()
            for d in dp:
                new_dp.add(num + d)
                new_dp.add(d)
            dp = new_dp
            if target in dp:
                return True

        if target in dp:
            return True
        else:
            return False
        
# Time complexity: O(n * target)
# Space complexity: O(target)
# Where target = sum(nums)