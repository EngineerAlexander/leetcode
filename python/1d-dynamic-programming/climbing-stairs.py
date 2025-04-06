# You are climbing a staircase. It takes n steps 
# to reach the top.

# Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?

# DP Draw out problem, think of splitting into subproblems
# 1. Base case: if n == 0 or n == 1, return 1
class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1

        for _ in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one
    
# Time complexity: O(n), cause of loop
# Space complexity: O(1), only using two variables