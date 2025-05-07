# Given a collection of candidate numbers (candidates) 
# and a target number (target), find all unique combinations 
# in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(target, start, comb):
            if target < 0:
                return
            if target == 0:
                res.append(comb)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                dfs(target-candidates[i], i+1, comb+[candidates[i]])

        dfs(target, 0, [])
        return res