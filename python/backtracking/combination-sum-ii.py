# Given a collection of candidate numbers (candidates) 
# and a target number (target), find all unique combinations 
# in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        cur = []

        def backtrack(remain, i):
            if remain == 0:
                res.append(cur[:])
                return
            if remain < 0:
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if candidates[j] > remain:
                    return
                cur.append(candidates[j])
                backtrack(remain - candidates[j], j + 1)
                cur.pop()

        backtrack(target, 0)
        return res
    
# Time complexity: O(n*2^n), in the worst case, let us assume that each number is unique.
# The number of combinations for an array of size N would be 2^N, i.e. each number is 
# included or excluded in a combination.
# Space complexity: O(n), combination of size n is stored in the result list.