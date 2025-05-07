# Given an unsorted array of integers nums, return the length of the 
# longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # set for constant lookup
        num_set = set(nums)

        total_longest = 0
        for num in num_set:
            # only do anything if first number of sequence
            if (num-1) not in num_set:
                current_num = num
                current_longest = 1
            
                # find sequence length and record
                while (current_num+1) in num_set:
                    current_num += 1
                    current_longest += 1
                total_longest = max(total_longest, current_longest)

        return total_longest
    
# Time complexity: O(n)
# Space complexity: O(n)