# You are given an array of integers nums, there is a sliding 
# window of size k which is moving from the very left of the 
# array to the very right. You can only see the k numbers in 
# the window. Each time the sliding window moves right by one position.
# Return the max sliding window.

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()

        for idx, num in enumerate(nums):
            while q and q[-1] < num:
                q.pop()
            q.append(num)

            if idx >= k and nums[idx - k] == q[0]:
                q.popleft()
            
            if idx >= k - 1:
                res.append(q[0])
        
        return res

# Time complexity: O(n)
# Space complexity: O(k)