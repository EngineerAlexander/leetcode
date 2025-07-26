# Given an integer array nums that may contain duplicates, 
# return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. 
# Return the solution in any order.

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sorting will help us to skip a number that have been
        # already used at i-th position at specific permutation.
        nums.sort()
        ans = []
        cur = []
        def backtrack(i, cur):
            ans.append(cur[:])
            
            for j in range(i, len(nums)):
                # We can re-use numbers, but not at this position
                # and same previous premutation
                if j > i and nums[j] == nums[j-1]:
                    continue
                cur.append(nums[j])
                backtrack(j+1, cur)
                cur.pop()
        backtrack(0, cur)
        return ans

# Time complexity: O(n * 2^n)
# Space complexity: O(n)