# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the 
# array whose sum equals k and remove them from the array.

# Return the maximum number of operations you can perform 
# on the array.

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        seen = {}
        operations = 0
        for num in nums:
            if (k - num) in seen:
                operations += 1
                seen[(k-num)] -= 1
                if seen[(k-num)] < 1:
                    del seen[(k-num)]
            else:
                if num in seen:
                    seen[num] += 1
                else:
                    seen[num] = 1

        return operations
    
# Time complexity: O(n)
# Space complexity: O(n)