#Given an array of integers nums and an integer target, 
#return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, 
#and you may not use the same element twice.
#You can return the answer in any order.
#nums is at least length two and only one valid solution exists.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            num = nums[i]
            comp = target - num
            if comp not in seen:
                seen[num] = i
            else:
                return [i, seen[comp]]
            
# Time complexity: O(n)
# Space complexity: O(n)