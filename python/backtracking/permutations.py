# Given an array nums of distinct integers, 
# return all the possible permutations. 
# You can return the answer in any order.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []

        def backtrack(i):
            if i == len(nums):
                res.append(cur[:])
                return

            for num in nums:
                if num not in cur:
                    cur.append(num)
                    backtrack(i + 1)
                    cur.pop()

        backtrack(0)
        return res
    
# Time complexity: O(n*n!), The number of permutations is n! and it takes O(n) time to copy each permutation into ans.
# Space complexity: O(n), The space used by cur.