# There is an integer array nums sorted in ascending order 
# (with distinct values).
# Prior to being passed to your function, nums is possibly 
# rotated at an unknown pivot index k (1 <= k < nums.length) 
# such that the resulting array is 
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, 
# return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.
# Constraints:
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find minimum, search 2 strictly increasing lists

        length = len(nums)

        # 1 element case
        if length == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        # if not shifted, we can skip step
        is_sorted = False
        if nums[0] < nums[-1]:
            is_sorted = True

        

        # find inflection if sorted, if not call it 0
        middle = 0
        if not is_sorted:
            left = 0
            right = length - 1

            while left <= right:
                middle = (left + right)//2

                # break conditions (make sure middle is set to minimum)
                if nums[middle] > nums[middle + 1]:
                    middle = middle + 1
                    break
                elif nums[middle - 1] > nums[middle]:
                    break

                # shift conditions
                # if current is greater than start, we need to move right
                if nums[middle] > nums[0]:
                    left = middle + 1
                # if current is less than start, we need to move left
                else:
                    right = middle - 1

        # binary search both 0 to middle-1 and middle to end
        res1 = self._binarySearch(nums[0:middle], target)
        res2_new_index = self._binarySearch(nums[middle::], target)
        if res2_new_index != -1:
            res2 = middle + res2_new_index
        else:
            res2 = -1

        return max(res1, res2)

    def _binarySearch(self, array, target):
        length = len(array)

        left = 0
        right = length - 1

        while left <= right:
            middle = (left + right)//2

            if array[middle] == target:
                return middle
            # if we're greater than, shift left
            elif array[middle] > target:
                right = middle - 1
            # if we're less than, shift right
            else:
                left = middle + 1

        return -1