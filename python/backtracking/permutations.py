# Given an array nums of distinct integers, 
# return all the possible permutations. 
# You can return the answer in any order.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack():
            if len(cur) == len(nums):
                ans.append(cur[:])
                return

            for num in nums:
                if num not in cur:
                    cur.append(num)
                    backtrack()
                    cur.pop()

        ans = []
        cur = []
        backtrack()
        return ans
    
# Time complexity: O(n*n!), The number of permutations is n! and it takes O(n) time to copy each permutation into ans.
# Space complexity: O(n), The space used by cur.