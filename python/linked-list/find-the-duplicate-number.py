# Given an array of integers nums containing n + 1 integers 
# where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array 
# nums and using only constant extra space.

# Constraints:
# All the integers in nums appear only once except for 
# precisely one integer which appears two or more times.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # integers between 1 -> n, there's one duplicate.
        # we can use array like a linked list (with a loop in it for the repeat)
        
        # Floyd's Algo
        # first iteration outside of loop
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        # reset fast pointer, increment until they're equal (at enterance to loop which is duplicate)
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
    
# Time complexity: O(n)
# Space complexity: O(1) because we are using constant space.