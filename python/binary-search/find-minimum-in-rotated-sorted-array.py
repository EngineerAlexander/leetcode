# Suppose an array of length n sorted in ascending order is rotated 
# between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] 
# might become:
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 
# 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# Given the sorted rotated array nums of unique elements, 
# return the minimum element of this array.
# You must write an algorithm that runs in O(log n) time.
# Constraints:
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # in unrotated (roated length times) min is start, every other is greater

        # if random num is greater than end, min is to the right
        # if random num is less than end, we could be on min or it is to the left
        low = 0
        high = len(nums) - 1
        end = nums[-1]
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > end:
                low = mid + 1
            elif nums[mid] < end:
                high = mid

        return nums[low]
    
# Time complexity: O(log n)
# Space complexity: O(1)