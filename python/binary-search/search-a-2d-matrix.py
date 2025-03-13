# You are given an m x n integer matrix matrix with the following two properties:
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix)
        C = len(matrix[0])

        low = 0
        high = R - 1
        while low <= high:
            mid = (low + high) // 2
            first = matrix[mid][0]
            last = matrix[mid][C - 1]
            if (first <= target) and (last >= target):
                break
            elif (first < target) and (last < target):
                low = mid + 1
            else:
                high = mid - 1


        low = 0
        high = C - 1
        while low <= high:
            mid2 = (low + high) // 2
            value = matrix[mid][mid2]
            if (value == target):
                return True
            elif (value < target):
                low = mid2 + 1
            else:
                high = mid2 - 1

        return False
    
# Time complexity: O(log(m))+O(log(n)) = O(log(m * n))
# Space complexity: O(1)