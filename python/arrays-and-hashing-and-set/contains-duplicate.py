# Given an integer array nums, return true if any value appears at least 
# twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for el in nums:
            if el in seen:
                return True
            else:
                seen.add(el)
        return False
    
# Time complexity: O(n)
# Space complexity: O(n)