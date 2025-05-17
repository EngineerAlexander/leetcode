# Given an integer array nums and an integer k, 
# return the kth largest element in the array.

# Note that it is the kth largest element 
# in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """"Sorting method"""
        nums.sort()
        return nums[-k]
    
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """"Quickselect method"""
        length = len(nums)
        # Index we're looking for if the array was sorted
        k = length - k

        def quickSelect(l, r):
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return nums[p]

        return quickSelect(0, length - 1)
    
# First Solution Complexity
# Time complexity: O(n log n) for sorting
# Space complexity: O(1) not using any extra space

# Second Solution Complexity
# Time complexity: O(n) on average, O(n^2) in the worst case
# Space complexity: O(1) for the in-place partitioning