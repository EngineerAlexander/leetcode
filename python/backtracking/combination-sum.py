# Given an array of distinct integers candidates and a 
# target integer target, return a list of all unique 
# combinations of candidates where the chosen numbers 
# sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited 
# number of times. Two combinations are unique if the frequency 
# of at least one of the chosen numbers is different.

# The test cases are generated such that the number of 
# unique combinations that sum up to target is less than 
# 150 combinations for the given input.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        comb = []

        def backtrack(remain, start):
            if remain == 0:
                results.append(list(comb))
                return
            elif remain < 0:
                # exceeded the scope so stop exploration
                return

            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtrack(remain - candidates[i], i)
                comb.pop()

        backtrack(target, 0)

        return results
    
# Time complexity: O(N^(T/M+1)), Let N be the number of candidates, 
# T be the target value, and M be the minimal value among the candidates.
# Space complexity: O(T/M), The maximum depth of recursion is T/M,