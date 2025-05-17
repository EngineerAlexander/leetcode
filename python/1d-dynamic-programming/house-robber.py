# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed, the only constraint 
# stopping you from robbing each of them is that adjacent houses have 
# security systems connected and it will automatically contact the police 
# if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each 
# house, return the maximum amount of money you can rob tonight without 
# alerting the police.

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0
        # [rob1, rob2, n, n+1, ...]
        # n = max(n + rob1, rob2)
        # n = maximum achievable for first n houses
        for n in nums:
            res = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = res

        return rob2
    
# Time complexity: O(n)
# Space complexity: O(1)