# Given an array of intervals intervals where intervals[i] = [starti, endi], 
# return the minimum number of intervals you need to remove to make the 
# rest of the intervals non-overlapping.

# Note that intervals which only touch at a point are non-overlapping. 
# For example, [1, 2] and [2, 3] are non-overlapping.

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by increasing end
        intervals.sort(key = lambda x: x[1])

        # anytime we are overlapping, iterate res
        res = 0
        last_end = float('-inf')
        for interval in intervals:
            start = interval[0]
            end = interval[1]

            if start < last_end:
                res += 1
            else:
                last_end = end

        return res
    
# Time complexity: O(n log n) for sorting
# Space complexity: O(1) for the in-place sorting