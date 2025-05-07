# Given an integer array nums that may contain duplicates, 
# return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. 
# Return the solution in any order.

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        currentSubset = []
        self.subsetsWithDupHelper(subsets, currentSubset, nums, 0)
        return subsets

    def subsetsWithDupHelper(self, subsets, currentSubset, nums, index):
        subsets.append(list(currentSubset))
        for i in range(index, len(nums)):
            if i != index and nums[i] == nums[i-1]:
                continue
            currentSubset.append(nums[i])
            self.subsetsWithDupHelper(subsets, currentSubset, nums, i+1)
            currentSubset.pop()

# Time complexity: O(n * 2^n)
# Space complexity: O(n)