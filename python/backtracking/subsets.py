# Given an integer array nums of unique elements, 
# return all possible subsets (the power set).

# The solution set must not contain duplicate 
# subsets. Return the solution in any order.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        def backtracking(i):
            if i == len(nums):
                res.append(cur[:])
                return

            backtracking(i + 1)

            cur.append(nums[i])
            backtracking(i + 1)
            cur.pop()

        backtracking(0)
        return res
    
# Time complexity: O(2^n) for recursion calls (either can include or exclude each element)
# Space complexity: O(n) for the recursion stack