# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints 
# of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, 
# such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        left = 0
        right = length - 1

        max_area = 0
        while left < right:
            l_height = height[left]
            r_height = height[right]
            new_area = min(l_height, r_height) * (right - left)
            max_area = max(max_area, new_area)

            if l_height <= r_height:
                left += 1
            else:
                right -= 1

        return max_area
    
# Time complexity: O(n)
# Space complexity: O(1)