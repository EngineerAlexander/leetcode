# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)

        res = []
        # if first is positive, it is imposible
        if nums[0] > 0:
            return res

        # loop over entire nums (selecting nums[i])
        for i in range(length):
            # skip repeated i
            if (i != 0) and (nums[i - 1] == nums[i]):
                continue

            # run two sum with fixed 'first' (i), append to res
            res.extend(self.twoSum(i, nums, length))

        return res

    def twoSum(self, i, nums, length):
        res = []
        target = -nums[i]

        # two pointer method (assumes nums is sorted)
        ptr1 = i + 1
        ptr2 = length - 1
        while ptr1 < ptr2:
            if nums[ptr1] + nums[ptr2] == target:
                res.append([-target, nums[ptr1], nums[ptr2]])
                ptr1 += 1
                while (ptr1 < ptr2) and (nums[ptr1] == nums[ptr1 - 1]):
                    ptr1 += 1
            elif nums[ptr1] + nums[ptr2] > target:
                ptr2 -= 1
            else:
                ptr1 += 1

        return res
    
# Time complexity: O(n^2)
# Space complexity: O(1)