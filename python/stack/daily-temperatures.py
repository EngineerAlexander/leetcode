# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have 
# to wait after the ith day to get a warmer temperature. If there is no 
# future day for which this is possible, keep answer[i] == 0 instead.

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)

        res = [0]*length

        stack = []
        for i in range(length - 1):
            if temperatures[i + 1] <= temperatures[i]:
                stack.append(i)
            else:
                res[i] = 1
                while stack and (temperatures[stack[-1]] < temperatures[i + 1]):
                    old_index = stack.pop()
                    res[old_index] =  i + 1 - old_index

        return res

# Time complexity: O(n)
# Space complexity: O(n)