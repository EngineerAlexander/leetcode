# Given an integer array nums of unique elements, 
# return all possible subsets (the power set).

# The solution set must not contain duplicate 
# subsets. Return the solution in any order.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        def backtrack(i):
            if i == len(nums):
                res.append(cur[:])
                return

            backtrack(i + 1)
            
            cur.append(nums[i])
            backtrack(i + 1)
            cur.pop()

        backtrack(0)
        return res
    
# Time complexity: O(n*2^n) for recursion calls 2^n (either can include or exclude each element), then copy takes n time
# Space complexity: O(n) for the recursion stack