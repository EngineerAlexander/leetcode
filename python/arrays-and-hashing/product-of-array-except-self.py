# Given an integer array nums, return an array answer such that answer[i] 
# is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 
# 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using 
# the division operation.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        create arrays for lhs product and rhs product (not including element i).
        multiply together at each element to get product/i (product excluding i)
        """

        length = len(nums)

        # rhs product
        res = [1]*length
        for i in range(length-2, -1, -1):
            res[i] = res[i + 1] * nums[i + 1]

        # lhs product
        running_lhs_product = 1
        for i in range(1, length, 1):
            running_lhs_product *= nums[i-1]
            res[i] *= running_lhs_product

        return res
    
# Time complexity: O(n)
# Space complexity: O(1), Note the trick with res to solve in O(1) space complexity