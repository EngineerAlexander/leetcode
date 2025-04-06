# Given an integer array nums, return the length of the 
# longest strictly increasing subsequence.

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [1] * length

        for i in range(length - 1, -1, -1):
            for j in range(i + 1, length, 1):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)
    
# Time complexity: O(n^2)
# Space complexity: O(n)