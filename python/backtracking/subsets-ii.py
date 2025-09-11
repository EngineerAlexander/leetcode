# Given an integer array nums that may contain duplicates, 
# return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. 
# Return the solution in any order.

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        cur = []
        def backtrack(i):
            res.append(cur[:])

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue

                cur.append(nums[j])
                backtrack(j + 1)
                cur.pop()

        backtrack(0)
        return res

# Time complexity: O(n * 2^n)
# Space complexity: O(n)