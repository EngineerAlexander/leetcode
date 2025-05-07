# Given a binary array nums and an integer k, 
# return the maximum number of consecutive 1's 
# in the array if you can flip at most k 0's.

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_consec = 0
        replace = 0

        left = 0
        for right in range(len(nums)):
            if nums[right] == 1:
                max_consec = max(max_consec, right - left + 1)
            else:
                if replace < k:
                    replace += 1
                    max_consec = max(max_consec, right - left + 1)
                else:
                    while (left < right) and (replace >= k):
                        if nums[left] == 0:
                            replace -= 1
                        left += 1

        return max_consec

# Time complexity: O(n)
# Space complexity: O(1)