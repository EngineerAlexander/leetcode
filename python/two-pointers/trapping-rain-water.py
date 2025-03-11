# Given n non-negative integers representing an elevation map 
# where the width of each bar is 1, compute how much water it 
# can trap after raining.

class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        left_step = [0]*length
        right_step = [0]*length

        cur_height = 0
        for i in range(length):
            cur_height = max(height[i], cur_height)
            left_step[i] = cur_height

        cur_height = 0
        for j in reversed(range(length)):
            cur_height = max(height[j], cur_height)
            right_step[j] = cur_height

        cumulative_sum = 0
        for i in range(length):
            cumulative_sum = cumulative_sum + min(left_step[i], right_step[i]) - height[i]

        return cumulative_sum
    
# Time complexity: O(n)
# Space complexity: O(n)