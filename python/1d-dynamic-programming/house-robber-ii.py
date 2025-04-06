# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed. All houses at this 
# place are arranged in a circle. That means the first house is the 
# neighbor of the last one. Meanwhile, adjacent houses have a security 
# system connected, and it will automatically contact the police if two 
# adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each 
# house, return the maximum amount of money you can rob tonight without 
# alerting the police.

class Solution:
    def rob(self, nums: List[int]) -> int:
        def robArray(nums):
            rob1 = 0
            rob2 = 0
            for num in nums:
                res = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = res

            return rob2

        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]

        # We can't rob first and last together since they are adjacent
        return max(robArray(nums[:-1]), robArray(nums[1:]))