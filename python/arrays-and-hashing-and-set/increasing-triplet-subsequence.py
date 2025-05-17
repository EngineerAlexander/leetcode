# Given an integer array nums, return true if there exists a 
# triple of indices (i, j, k) such that i < j < k and 
# nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

# Follow up: Could you implement a solution that runs in 
# O(n) time complexity and O(1) space complexity?

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Linear scan, if less than first num new first num, elif less than second num, new 2nd num, ellse we found our triple
        first = float('inf')
        second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True

        return False
    
# Time complexity: O(n) because just linear scan
# Space complexity: O(1) because just 2 variables