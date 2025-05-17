# You are given an integer array coins representing coins of different 
# denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, 
# return -1.

# You may assume that you have an infinite number of each kind of coin.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")]*(amount + 1)
        dp[0] = 0 # Can fill up 0 amount with 0 coins

        for a in range(1, amount + 1):
            for c in coins:
                if (a - c) >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        if dp[amount] == float("inf"):
            return -1
        else:
            return dp[amount]
        
# Time complexity: O(n * m), where n is the amount and m is the number of coins
# Space complexity: O(n), for the dp array